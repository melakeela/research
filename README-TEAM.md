# MelaKeela research team

Eight subagents, an operating structure and a mechanical register gate.
Installed from the `melakeela-team` archive on 2026-09-07 and reconciled
against `CLAUDE.md`, `00-CONTROLLER/METHODOLOGY-CONSTITUTION.md`,
`00-CONTROLLER/CONTROLLER-RECONCILIATION.md`, the inherited handoff and
`04-AUDITS/BIAS-FAILURE-LOG.csv` in the same pass.

```
.claude/agents/                    eight subagent definitions
.claude/settings.json              the PreToolUse hook wiring
.claude/hooks/
  block-push-on-register-failure.sh
00-CONTROLLER/PROGRAMME.md         operating structure, gates, batch proposal
04-AUDITS/validate-registers.py    mechanical enforcement
04-AUDITS/VALIDATOR-FINDINGS-2026-09-07.md
                                   what the validator currently reports
```

## The agents

Each carries its citations. A constraint in an agent file traces to a rule in
`CLAUDE.md`, the constitution, the reconciliation, the inherited handoff, or a
logged row in `04-AUDITS/BIAS-FAILURE-LOG.csv`. If it cites nothing, it does not
belong in the file — that is the standard the reconciliation pass applied, and
the standard for anything added later.

| Agent | Lane |
|---|---|
| `retriever` | Opens sources, pins hashes, logs access; never interprets |
| `corpus-analyst` | Reproducible counts and distributions; measurements only |
| `chronology-gate` | Steps 2, 3 and 7 — chronology, geography, eligibility verdicts |
| `source-genealogist` | How many independent observations are actually behind this |
| `historiography-auditor` | Step 6 and §4.V — archive, power, credit, custody |
| `adversarial-reviewer` | Tries to make the work fail; has no Write or Edit tool |
| `museum-translator` | Accepted claims into briefs and copy; waits for review |
| `rights-steward` | Rights, consent, custody, institutional claims |

`memory: project` on each writes to `.claude/agent-memory/<name>/`, which is
project-scoped and versionable.

## The register gate

`.claude/settings.json` registers a `PreToolUse` hook on the `Bash` tool. Before
any `git push`, `.claude/hooks/block-push-on-register-failure.sh` runs
`04-AUDITS/validate-registers.py`; if the validator exits non-zero the hook
returns a `permissionDecision` of `deny` and the push does not happen. If the
validator passes, the hook prints nothing and the normal permission flow
applies.

It matches only a command segment whose leading token is `git`, so the literal
string inside a quoted argument, a heredoc or a comment does not trip it. It is
a guard rail, not a sandbox: a push assembled through a shell variable will get
through, and the point is to stop the accident, not to defeat a determined
session.

**Override.** Where the failures are known, recorded and deliberately not being
fixed, write the push with the marker in the command:

```
MELAKEELA_REGISTER_GATE=off git push -u origin <branch>
```

The hook reads that marker out of the command text, not out of its own
environment — a `PreToolUse` hook runs in Claude Code's environment, before the
command does, so an exported variable would be invisible to it. Putting it in
the command is the better record anyway: the override is visible in the
transcript and in the tool call, one push at a time, and every use is stated in
the pull request with the reason. Editing the validator to make failing rows
pass is not an available move.

**The gate is currently closed.** The validator reports 43 failures against the
tree — see `04-AUDITS/VALIDATOR-FINDINGS-2026-09-07.md`, which lists them,
classes them, and says what each would take. Until they are resolved, or the
`source_id` rule is settled, every push needs the override. That is a decision
for the owner, not something to be worked around quietly.
