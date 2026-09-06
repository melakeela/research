# research
Private research and evidence repository for MelaKeela. Source ledgers, evidence registers, audits, and page briefs for the ancient South Asia programme. Not the website — no site code here.


# MelaKeela — Research

Institutional memory and evidence base for the MelaKeela project.
The public website lives in `melakeela/site`. **No site code belongs here.**

## What this repository is

A verifiable record of what has been claimed, what has been checked,
against what source, and what remains open. Its output is evidence
packages and page briefs — not prose, not summaries, not reports.

## Evidence status vocabulary

Every claim carries exactly one status. Nothing is unstatused.

| Status | Meaning |
|---|---|
| `VERIFIED` | Re-checked against a named source with locator + retrieval date |
| `PROVISIONAL` | Supported, but by a single or dependent source |
| `HYPOTHESIS` | Proposed, not yet tested |
| `INHERITED-UNVERIFIED` | Carried in from prior chat threads; **not** evidence |
| `REJECTED` | Tested and failed; retained so it is not re-proposed |
| `SUPERSEDED` | Replaced; retains a pointer to what replaced it |
| `HOLD` | Blocked on source access; see `05-HOLDS/` |

A claim may not be promoted by argument. Promotion requires a
retrieval event recorded in the source ledger.

## Standing constraints

- Source independence: two citations tracing to the same author or
  dataset count as one.
- No false equivalence between a contested claim and an established one.
- Chronology and geography gates apply to every claim.
- Rejected reasoning stays rejected. Correction history is preserved.

## Structure

```
00-CONTROLLER/     research constitution, status rules, stopping rules
01-INHERITED/      prior-thread handoffs (all INHERITED-UNVERIFIED)
02-SOURCES/        access ledger, dependency map, retrieval notes
03-REGISTERS/      evidence registers (CSV, one claim per row)
04-AUDITS/         adversarial reviews and repairs
05-HOLDS/          claims blocked on genuinely unavailable sources
```

## Working

`CLAUDE.md` is the operating controller. `AGENTS.md` mirrors it for
Codex. `RESEARCH-QUEUE.md` is the only backlog. `DECISIONS-NEEDED.md`
is the only place that asks anything of the owner.

Releases go out as pull requests against `main`, reviewed
independently before merge.
