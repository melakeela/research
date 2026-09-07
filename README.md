# MelaKeela — Research

Private research and evidence repository for the MelaKeela project.
The public website lives in `melakeela/site`. **No site code here.**

## What this is

A verifiable record of what has been claimed, what has been checked,
against what source, and what remains open. Output is evidence
packages and page briefs, not prose.

## Status vocabulary

`VERIFIED` · `PROVISIONAL` · `HYPOTHESIS` · `INHERITED-UNVERIFIED` ·
`REJECTED` · `SUPERSEDED` · `HOLD`

These are the values of `evidence_status`, which is the only evidence gate.
`interpretive_status`, `editorial_status`, `publication_status` and
`gate_verdict` are separate dimensions and none of them promotes a claim:
`00-CONTROLLER/STATUS-DIMENSIONS.md`.

Definitions and promotion rules are in `CLAUDE.md`. The short version:
a claim is promoted only by a logged retrieval event, never by argument.
The method the research runs under is
`00-CONTROLLER/METHODOLOGY-CONSTITUTION.md`.

## Structure

```
00-CONTROLLER/     constitution, reconciliation, repository map, control-plane registers
01-INHERITED/      prior-thread handoffs (all INHERITED-UNVERIFIED)
02-SOURCES/        access ledger, dependency map, retrieval notes
03-REGISTERS/      evidence registers (CSV, one claim per row) and the claim/source join
04-AUDITS/         adversarial reviews, bias-failure log, re-audit queue,
                   measurement scripts, the validator
05-HOLDS/          claims blocked on unavailable sources
06-BACKLOG/        the 89-item backlog: recovered titles and the coverage table
06-BRIEFS/         research briefs
09-DECISIONS/      owner decisions register and decision-ID map
13-PRODUCT-ARCHITECTURE/   product specification
```

`00-CONTROLLER/REPOSITORY-MAP.md` is authoritative for what each folder is
for. The folder numbers are not a scheme — `06` names two folders and `13`
carries a numbering the reconciliation rejected — and
`00-CONTROLLER/PATH-MIGRATION.csv` holds the crosswalk to an unnumbered
structure. Nothing has been moved.

The backlog's coverage table exists and has 95 rows. What is still absent is
the **full original text** of the 89 items: only their titles were
recovered, so seven scope columns are empty and the site-coverage columns
read `NOT ESTABLISHED` because the route inventory lives in `melakeela/site`.
See `06-BACKLOG/README.md` and `00-CONTROLLER/MIGRATION-HOLDS.csv` MH-004.

## Files

- `CLAUDE.md` — operating controller for Claude Code
- `00-CONTROLLER/METHODOLOGY-CONSTITUTION.md` — the methodology, as the
  owner wrote it, committed unchanged
- `00-CONTROLLER/CONTROLLER-RECONCILIATION.md` — how the two fit together
- `AGENTS.md` — the same rules for Codex, which does not read CLAUDE.md
- `.mcp.json` — literature search connectors
- `RESEARCH-QUEUE.md` — the only backlog
- `DECISIONS-NEEDED.md` — the prose case for escalations that block
  research in progress
- `09-DECISIONS/OWNER-DECISIONS.csv` — the owner decisions register, and
  the authority for `D-` identifiers and statuses. Every decision has a
  row here; the ones that block are written up in `DECISIONS-NEEDED.md`
  and linked by `detail_ref`
- `09-DECISIONS/DECISION-ID-MAP.csv` — old identifier to new, for
  resolving a `D-` reference in a document written before the namespaces
  were merged
- `00-CONTROLLER/REPOSITORY-MAP.md` — folder authority; what may go where
- `00-CONTROLLER/CANONICAL-FILES.csv` — the authoritative file for each
  function, and what the validator governs
- `00-CONTROLLER/CONTRADICTION-REGISTER.csv` — contradictions in the control
  plane, as against `04-AUDITS/INTERNAL-CONTRADICTIONS.csv` for
  contradictions in the evidence
- `00-CONTROLLER/PATH-MIGRATION.csv` — every path, its proposed destination,
  and the references a move would break
- `00-CONTROLLER/STATUS-DIMENSIONS.md` — the status dimensions and their
  enumerations
- `00-CONTROLLER/OVERRIDE-LOG.csv` — the only way past a failing validator
- `00-CONTROLLER/MIGRATION-HOLDS.csv` — rows left unchanged because
  migrating them would change what they say
- `04-AUDITS/validate-registers.py` — the mechanical gate, with
  `test-validate-registers.py` proving it still fails when it should

## Working

Claude Code opens pull requests against `main`. Codex reviews them
independently. Nothing merges unverified.

`04-AUDITS/validate-registers.py` runs in CI on every push and pull request.
Requiring it before merge is branch protection, which is a repository
setting only the owner can turn on; until then `main` is unprotected and the
enforceable half of the gate is missing (CR-013).
