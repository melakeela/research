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

Definitions and promotion rules are in `CLAUDE.md`. The short version:
a claim is promoted only by a logged retrieval event, never by argument.
The method the research runs under is
`00-CONTROLLER/METHODOLOGY-CONSTITUTION.md`.

## Structure

```
00-CONTROLLER/     methodology constitution, reconciliation, stopping rules
01-INHERITED/      prior-thread handoffs (all INHERITED-UNVERIFIED)
02-SOURCES/        access ledger, dependency map, retrieval notes
03-REGISTERS/      evidence registers (CSV, one claim per row)
04-AUDITS/         adversarial reviews, bias-failure log, re-audit queue
05-HOLDS/          claims blocked on unavailable sources
06-BACKLOG/        backlog coverage (awaiting the v2 backlog document)
09-DECISIONS/      owner decisions register and decision-ID map
```

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

## Working

Claude Code opens pull requests against `main`. Codex reviews them
independently. Nothing merges unverified.
