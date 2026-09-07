#!/usr/bin/env bash
# PreToolUse hook: refuse a git push while 04-AUDITS/validate-registers.py fails.
#
# Wired in .claude/settings.json under hooks.PreToolUse with matcher "Bash".
# Contract (Claude Code hooks reference):
#   - stdin carries the hook payload as JSON, including tool_name and tool_input
#   - exit 0 with no stdout  -> no decision; normal permission flow applies
#   - stdout {"hookSpecificOutput":{"hookEventName":"PreToolUse",
#             "permissionDecision":"deny","permissionDecisionReason":"..."}}
#     -> the tool call is blocked and Claude is shown the reason
#
# WHAT THIS IS. Early feedback in one tool in one client. It cannot see a push
# made through the GitHub UI or API, another Git client, or any session that is
# not this one. The enforceable gate is .github/workflows/validate-registers.yml
# plus branch protection requiring that check before merge; branch protection is
# a repository setting only the owner can turn on. Do not describe this hook as
# the gate.
#
# NO ORDINARY BYPASS. The one-token MELAKEELA_REGISTER_GATE=off marker was
# removed on 2026-09-07. It made the gate advisory by construction: the hook
# searched the command text before establishing that the marker was an
# environment assignment at all, so `echo MELAKEELA_REGISTER_GATE=off; git push`
# disabled it as surely as the documented form did. A gate anyone can turn off
# in passing is not a gate.
#
# EMERGENCY OVERRIDE. A push that fails validation requires a committed row in
# 00-CONTROLLER/OVERRIDE-LOG.csv carrying reason, actor, raised_date,
# expiry_date and affected_validation_failures. The hook allows the push only
# while an unexpired row waives EVERY failure the validator is currently
# reporting; a row that waives a failure the validator is not reporting does
# nothing, and an expired row does nothing. The waiver is committed before it
# is used, so it lands in the diff a reviewer reads rather than in a transcript
# nobody re-reads.
#
# FAIL CLOSED. An unparseable payload, a missing validator or an error inside
# this hook denies the push. The previous version returned "no opinion" in all
# three cases, which meant the gate opened precisely when it was least able to
# tell whether it should. Weakening the validator to get past this is still not
# an available move.
set -uo pipefail

ROOT="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
VALIDATOR="$ROOT/04-AUDITS/validate-registers.py"

PAYLOAD="$(cat)"

deny() {
  python3 -c '
import json, sys
print(json.dumps({"hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": sys.argv[1],
}}))' "$1"
  exit 0
}

decision=$(ROOT="$ROOT" VALIDATOR="$VALIDATOR" python3 - "$PAYLOAD" <<'PY'
import json, os, re, subprocess, sys

DENY = "DENY\n"

def deny(reason):
    sys.stdout.write(DENY + reason)
    sys.exit(0)

try:
    payload = json.loads(sys.argv[1])
except (ValueError, IndexError):
    deny("Push gate: the hook payload could not be parsed, so this hook cannot "
         "tell whether the command is a push. It fails closed. Repair "
         ".claude/hooks/block-push-on-register-failure.sh.")

if payload.get("tool_name") != "Bash":
    sys.exit(0)

command = (payload.get("tool_input") or {}).get("command") or ""

# Match a push however it is spelled. The previous parser required the segment
# to OPEN with `git`, so `env git push`, `/usr/bin/git push` and
# `sh -c 'git push'` all walked past it. A push assembled entirely out of shell
# variables still gets through; this is a guard rail, not a sandbox, and that
# is why CI is the gate.
SEGMENT = re.compile(r"&&|\|\||;|\||\n")
GIT_TOKEN = re.compile(r"(?:^|[\s'\"/])git(?:\.exe)?(?![\w-])")
PUSH_VERB = re.compile(r"(?<![\w-])push(?![\w-])")

if not any(GIT_TOKEN.search(seg) and PUSH_VERB.search(seg)
           for seg in SEGMENT.split(command)):
    sys.exit(0)

validator = os.environ["VALIDATOR"]
if not os.path.exists(validator):
    deny(f"Push gate: {validator} is missing, so nothing verified these "
         f"registers. It fails closed — restore the validator.")

try:
    proc = subprocess.run([sys.executable, validator], cwd=os.environ["ROOT"],
                          capture_output=True, text=True, timeout=100)
except Exception as exc:                       # noqa: BLE001 - fail closed on anything
    deny(f"Push gate: the validator could not be run ({exc}). It fails closed.")

if proc.returncode == 0:
    sys.exit(0)                                # registers clean: normal flow

# Take only the failures section. The validator also prints notes and a
# warnings block, both indented; treating those as failures would mean no
# waiver could ever match them and every override would be refused.
failures, in_failures = [], False
for ln in proc.stdout.splitlines():
    if re.match(r"validate-registers: \d+ failure\(s\)", ln.strip()):
        in_failures = True
        continue
    if in_failures:
        if ln.startswith("  ") and ln.strip():
            failures.append(ln.strip())
        elif ln.strip():
            in_failures = False

# An unexpired OVERRIDE-LOG row may waive failures. Every current failure must
# be waived by some active row, or the push is denied.
active = []
try:
    listed = subprocess.run([sys.executable, validator, "--list-active-overrides"],
                            cwd=os.environ["ROOT"], capture_output=True,
                            text=True, timeout=100)
    for line in listed.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) >= 3:
            active.append((parts[0], parts[2]))
except Exception:                              # noqa: BLE001
    active = []

def waived(failure):
    for _oid, signatures in active:
        for sig in signatures.split(";"):
            sig = sig.strip()
            if sig and sig in failure:
                return True
    return False

unwaived = [f for f in failures if not waived(f)]
if failures and not unwaived:
    sys.exit(0)                                # every failure carries a live waiver

head, rest = unwaived[:20], unwaived[20:]
detail = "\n".join(head) + (f"\n  ... and {len(rest)} more" if rest else "")

deny(
    "Push blocked: 04-AUDITS/validate-registers.py is failing.\n\n"
    f"{detail}\n\n"
    "CLAUDE.md: a VERIFIED row is backed by a logged retrieval event, its "
    "source_id resolves to 02-SOURCES/access-ledger.csv, every SUPERSEDED row "
    "names its replacement, and every D- reference resolves to a row in "
    "09-DECISIONS/OWNER-DECISIONS.csv. Fix the rows, or record the "
    "disagreement as an owner decision.\n\n"
    "There is no one-token override. If a failure is known, recorded and "
    "deliberately not being fixed, commit a row to "
    "00-CONTROLLER/OVERRIDE-LOG.csv with reason, actor, raised_date, "
    "expiry_date and affected_validation_failures — the last being substrings "
    "that match the exact failure lines above — and say so in the pull "
    "request. Do not weaken the validator to get past this."
)
PY
)

status=$?
if [ $status -ne 0 ]; then
  deny "Push gate: this hook exited non-zero before reaching a decision, so it
cannot say whether the registers are clean. It fails closed. Repair
.claude/hooks/block-push-on-register-failure.sh."
fi

case "$decision" in
  DENY*) deny "${decision#DENY$'\n'}" ;;
  "")    exit 0 ;;
  *)     deny "Push gate: unexpected hook output. Failing closed." ;;
esac
