#!/usr/bin/env bash
# PreToolUse hook: refuse a git push while 04-AUDITS/validate-registers.py fails.
#
# WHAT THIS IS. Early feedback, not the gate. It runs before a `git push`
# issued through this session's Bash tool, and before the GitHub MCP tools that
# write to the repository. It cannot see a push from another git client, from
# the GitHub web UI or REST API, or from any session that is not this one. The
# gate is .github/workflows/validate-registers.yml, and it only becomes binding
# once the check is required in branch protection — D-050, which only the owner
# can set. Do not describe this hook as enforcement.
#
# WHAT CHANGED ON 2026-09-08. The previous version returned no decision for any
# command whose text contained MELAKEELA_REGISTER_GATE=off, anywhere, including
# inside a quoted string or an echo. `echo MELAKEELA_REGISTER_GATE=off; git
# push` therefore bypassed it exactly as the documented assignment did, which
# made the mechanism advisory by construction. That override is removed. It
# also failed open on a missing validator; it now fails closed.
#
# THE ONLY WAY PAST A FAILING CHECK is a row in 04-AUDITS/OVERRIDE-LOG.csv
# that is:
#   * committed — the file is read from HEAD, not from the working tree, so an
#     override does not exist until it is in a commit and visible in a diff;
#   * unexpired — expiry is a date and today must not be past it;
#   * specific — affected_validation_failures must name what it covers, and a
#     row that names nothing covers nothing;
#   * attributed — actor, date and reason are all required.
# Every use is therefore a committed record with a name on it and an end date,
# and must be stated in the pull request. Editing the validator to make failing
# rows pass is not an available move.
#
# Contract (Claude Code hooks reference):
#   - stdin carries the hook payload as JSON, including tool_name and tool_input
#   - exit 0 with no stdout  -> no decision; normal permission flow applies
#   - stdout {"hookSpecificOutput":{"hookEventName":"PreToolUse",
#             "permissionDecision":"deny","permissionDecisionReason":"..."}}
#     -> the tool call is blocked and Claude is shown the reason
set -uo pipefail

ROOT="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
VALIDATOR="$ROOT/04-AUDITS/validate-registers.py"

PAYLOAD="$(cat)"

decision=$(ROOT="$ROOT" VALIDATOR="$VALIDATOR" python3 - "$PAYLOAD" <<'PY'
import csv, io, json, os, re, subprocess, sys
from datetime import date

ROOT = os.environ["ROOT"]
VALIDATOR = os.environ["VALIDATOR"]
OVERRIDE_PATH = "04-AUDITS/OVERRIDE-LOG.csv"

# Tools that write to the repository. Bash is inspected for a push; the GitHub
# MCP write tools are treated as a push unconditionally, because they reach the
# remote without a local git command at all.
GITHUB_WRITE = {
    "mcp__github__push_files",
    "mcp__github__create_or_update_file",
    "mcp__github__delete_file",
    "mcp__github__merge_pull_request",
}


def deny(reason):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": reason,
    }}))
    sys.exit(0)


try:
    payload = json.loads(sys.argv[1])
except (ValueError, IndexError):
    sys.exit(0)                      # cannot identify a push: express no opinion

tool = payload.get("tool_name")
if tool in GITHUB_WRITE:
    pushing = True
elif tool == "Bash":
    command = (payload.get("tool_input") or {}).get("command") or ""
    # Match a segment that RUNS git, however it is spelled: an absolute path,
    # an env/command/exec/sudo wrapper, or sh -c. There is no text marker that
    # turns the check off, so there is nothing to spell around.
    SEGMENT = re.compile(r"&&|\|\||;|\||\n")
    RUNS_GIT = re.compile(
        r"""(^|[\s"'(])                    # start, or a boundary
            (?:\w+=\S*\s+)*                # inline VAR=value assignments
            (?:(?:command|exec|sudo|env|nohup|time|xargs)\s+)*
            (?:/[\w./-]*/)?git\b""", re.VERBOSE)
    PUSH_VERB = re.compile(r"(?<![\w-])push(?![\w-])")
    pushing = any(RUNS_GIT.search(seg) and PUSH_VERB.search(seg)
                  for seg in SEGMENT.split(command))
else:
    sys.exit(0)

if not pushing:
    sys.exit(0)

if not os.path.exists(VALIDATOR):
    # Fail closed. A missing validator used to mean "nothing to enforce", which
    # made deleting it a way past the check.
    deny("Push blocked: 04-AUDITS/validate-registers.py is missing. The check "
         "cannot be run, so it cannot be said to pass. Restore it.")

proc = subprocess.run([sys.executable, VALIDATOR], cwd=ROOT,
                      capture_output=True, text=True)
if proc.returncode == 0:
    sys.exit(0)                      # registers clean: defer to normal flow

lines = [ln for ln in proc.stdout.splitlines() if ln.strip()]
head, rest = lines[:20], lines[20:]
detail = "\n".join(head) + (f"\n  ... and {len(rest)} more" if rest else "")

# --- the only override: a committed, unexpired, specific, attributed row -----
try:
    blob = subprocess.run(["git", "show", f"HEAD:{OVERRIDE_PATH}"], cwd=ROOT,
                          capture_output=True, text=True)
    committed = blob.stdout if blob.returncode == 0 else ""
except OSError:
    committed = ""

today = date.today().isoformat()
live, rejected = [], []
for row in csv.DictReader(io.StringIO(committed)):
    oid = (row.get("override_id") or "").strip()
    missing = [c for c in ("actor", "date", "reason",
                           "affected_validation_failures", "expiry")
               if not (row.get(c) or "").strip()]
    if missing:
        rejected.append(f"{oid or '(no id)'}: missing {', '.join(missing)}")
        continue
    expiry = row["expiry"].strip()
    if expiry < today:
        rejected.append(f"{oid}: expired {expiry}")
        continue
    live.append(row)

if live:
    ids = ", ".join(r["override_id"] for r in live)
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "allow",
        "permissionDecisionReason": (
            f"Register check failing, and a committed override is in force: "
            f"{ids}.\n\n{detail}\n\nState the override and its reason in the "
            f"pull request. It expires and does not renew itself."),
    }}))
    sys.exit(0)

extra = ""
if rejected:
    extra = ("\n\nOverride rows found and NOT applied:\n  "
             + "\n  ".join(rejected))

deny(
    "Push blocked: 04-AUDITS/validate-registers.py is failing.\n\n"
    f"{detail}{extra}\n\n"
    "CLAUDE.md: a VERIFIED row is backed by a logged retrieval event, its "
    "source_id resolves to 02-SOURCES/access-ledger.csv, and every D- "
    "reference resolves to a row in 09-DECISIONS/OWNER-DECISIONS.csv. Fix the "
    "rows, or record the disagreement as an owner decision. Do not weaken the "
    "validator to get past this.\n\n"
    "There is no command-line or environment bypass. If these failures are "
    "known, recorded and deliberately not being fixed, add a row to "
    "04-AUDITS/OVERRIDE-LOG.csv with override_id, actor, date, reason, the "
    "exact affected_validation_failures it covers, and an expiry date, COMMIT "
    "it, and push again — the file is read from HEAD, so an uncommitted "
    "override does not apply."
)
PY
)

status=$?
if [ $status -ne 0 ]; then
  # A hook that crashes must not become a way past the check.
  printf '%s\n' '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"Push blocked: the register-check hook failed to run, so the check cannot be said to pass. Run 04-AUDITS/validate-registers.py directly and fix the hook."}}'
  exit 0
fi

if [ -n "$decision" ]; then
  printf '%s\n' "$decision"
fi
exit 0
