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
# The gate this enforces is CLAUDE.md's: a VERIFIED row that no logged
# retrieval backs must not reach the branch, and the branch is the checkpoint.
#
# Override, for the case where the failures are known, recorded, and
# deliberately not being fixed in the current session, set the environment
# variable MELAKEELA_REGISTER_GATE to "off" on that one command. The override is
# per-command, is never exported into a profile, and every use of it is stated
# in the pull request with the reason. Weakening the validator itself to get
# past this gate is not an available move.
set -uo pipefail

ROOT="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
VALIDATOR="$ROOT/04-AUDITS/validate-registers.py"

PAYLOAD="$(cat)"

if [ "${MELAKEELA_REGISTER_GATE:-on}" = "off" ]; then
  exit 0
fi

decision=$(ROOT="$ROOT" VALIDATOR="$VALIDATOR" python3 - "$PAYLOAD" <<'PY'
import json, os, re, subprocess, sys

try:
    payload = json.loads(sys.argv[1])
except (ValueError, IndexError):
    sys.exit(0)                      # unparseable payload: express no opinion

if payload.get("tool_name") != "Bash":
    sys.exit(0)

command = (payload.get("tool_input") or {}).get("command") or ""

# Match only a segment whose *leading token* is git (after optional inline
# environment assignments), so that the literal text appearing inside a quoted
# string, a heredoc body or a comment does not trip the gate. A push smuggled
# through a shell variable or an alias is out of scope: this is a guard rail,
# not a sandbox.
SEGMENT = re.compile(r"&&|\|\||;|\||\n")
LEADING_GIT = re.compile(
    r"""^\s*                       # leading whitespace
        (?:\w+=[^\s]*\s+)*         # inline VAR=value assignments
        (?:command\s+|exec\s+)?    # a couple of common wrappers
        git\b""",
    re.VERBOSE,
)
PUSH_VERB = re.compile(r"(?<![\w-])push(?![\w-])")

blocked = False
for segment in SEGMENT.split(command):
    if LEADING_GIT.match(segment) and PUSH_VERB.search(segment):
        blocked = True
        break

if not blocked:
    sys.exit(0)

validator = os.environ["VALIDATOR"]
if not os.path.exists(validator):
    sys.exit(0)                      # nothing to enforce

proc = subprocess.run(
    [sys.executable, validator],
    cwd=os.environ["ROOT"], capture_output=True, text=True,
)
if proc.returncode == 0:
    sys.exit(0)                      # registers clean: defer to normal flow

lines = [ln for ln in proc.stdout.splitlines() if ln.strip()]
head, rest = lines[:20], lines[20:]
detail = "\n".join(head)
if rest:
    detail += f"\n  ... and {len(rest)} more"

reason = (
    "Push blocked: 04-AUDITS/validate-registers.py is failing.\n\n"
    f"{detail}\n\n"
    "CLAUDE.md: a VERIFIED row is backed by a logged retrieval event, its "
    "source_id resolves to 02-SOURCES/access-ledger.csv, and every D- "
    "reference resolves to a row in 09-DECISIONS/OWNER-DECISIONS.csv. Fix "
    "the rows, or record the disagreement as an owner decision, before "
    "pushing. Do not weaken the validator to get past this.\n\n"
    "If these failures are known, recorded and deliberately not being fixed "
    "in this session, set MELAKEELA_REGISTER_GATE=off on the one push "
    "command — and say so, and why, in the pull request."
)

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": reason,
    }
}))
PY
)

status=$?
if [ $status -ne 0 ]; then
  exit 0                             # a hook failure never blocks work silently
fi

if [ -n "$decision" ]; then
  printf '%s\n' "$decision"
fi
exit 0
