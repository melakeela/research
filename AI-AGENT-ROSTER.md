# MelaKeela AI agent roster

Eight Claude subagents, an operating structure and a mechanical register gate.

**These are AI agents, not people.** Each name below is a Claude subagent
definition in `.claude/agents/` — a separation of concern with its own prompt,
tool set and memory. None of them is a scholar, an adviser, a partner, a
community representative, an employee or an independent human reviewer, and
nothing they produce is human-reviewed until a named human reviews it. Named
scholars and historical intellectuals appear in this repository as sources and
as subjects of historiographical audit; being cited is not an engagement, and
no file here may present one as a collaborator.
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

## The roster

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

Agent output is model-generated. `adversarial-reviewer` attacking a register
is not peer review, and `rights-steward` recording a rights position is not
legal advice or community consent.

## The register gate

`.claude/settings.json` registers a `PreToolUse` hook on the `Bash` tool. Before
any `git push`, `.claude/hooks/block-push-on-register-failure.sh` runs
`04-AUDITS/validate-registers.py`; if the validator exits non-zero the hook
returns a `permissionDecision` of `deny` and the push does not happen. If the
validator passes, the hook prints nothing and the normal permission flow
applies.

**What the hook is not.** It is local to Claude Code's Bash tool. It cannot
see a push made through the GitHub UI or API, another Git client, or any
session that is not this one, and a push assembled through a shell variable
still gets past its parser. Calling it "the gate" was an overstatement and is
corrected here: it is early feedback.

**The gate** is `.github/workflows/validate-registers.yml`, which runs the same
validator on every push and pull request, plus branch protection requiring that
check before merge. Branch protection is a repository setting and only the
owner can turn it on; until then `main` is unprotected and the enforceable half
of the gate is missing. That is recorded, not worked around — see
`00-CONTROLLER/CONTRADICTION-REGISTER.csv` CR-013.

**Override.** There is no ordinary bypass. The one-token
`MELAKEELA_REGISTER_GATE=off` marker was removed on 2026-09-07: it made the
gate advisory by construction, and any command text containing the string —
`echo MELAKEELA_REGISTER_GATE=off; git push` included — disabled it.

An emergency override now requires a committed row in
`00-CONTROLLER/OVERRIDE-LOG.csv` carrying the reason, the actor, the date, the
exact validation failures being waived, and an expiry date. The hook reads that
file: a push is allowed only while an unexpired row waives every failure the
validator is currently reporting, and a row that waives a failure the validator
is not reporting does nothing. The override is committed before it is used, so
it is in the diff a reviewer reads rather than in a transcript nobody re-reads.
Editing the validator to make failing rows pass is still not an available move.
