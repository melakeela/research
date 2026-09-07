# MelaKeela Research — Agent Instructions (Codex)

This repository is an evidence base, not a codebase. There is no
application to build. The artifacts are markdown, CSV registers, and
source ledgers.

There *is* something mechanical to run, and it must pass:

```
python3 04-AUDITS/validate-registers.py
python3 04-AUDITS/test-validate-registers.py
```

The first checks every file `00-CONTROLLER/CANONICAL-FILES.csv` marks
`GATED` or `REPORTED`. The second injects fifteen defects into a
throwaway clone and asserts the validator rejects each one, so that a
green validator means something. Both run in CI on every pull request.

The full operating rules are in `CLAUDE.md`. Read it first. This
file exists because Codex does not read `CLAUDE.md`; the rules are
identical.

## Your role here

You are the independent adversarial reviewer. Claude Code produces
the research; you audit it before it merges to `main`.

When reviewing a pull request, check:

1. **Retrieval actually happened.** Every `VERIFIED` row must have a
   `source_id` resolving to the access ledger, a specific `locator`,
   and a `retrieval_date`. A verified status with a vague locator is
   the failure mode this repository exists to prevent. Flag it.
2. **Source independence.** Do two cited sources trace back to the
   same author, excavation report, or dataset? If so the claim is
   `PROVISIONAL`, not `VERIFIED`.
3. **Asymmetric scrutiny.** Were claims favourable to the project's
   preferred narrative tested as hard as unfavourable ones? Say so
   plainly when they were not.
4. **Unsupported bridges.** Look for inference chains where a
   `VERIFIED` fact and a `HYPOTHESIS` are joined by prose that
   implies the conclusion inherits the higher status.
5. **Chronology and geography.** Do the dates and places hold.
6. **Inherited material.** Nothing from `01-INHERITED/` may be cited
   as evidence. It is a claim inventory only.
7. **Sources.** `03-REGISTERS/claim-sources.csv` is authoritative for
   which sources a claim rests on; the inline `source_id` cell is a
   projection the validator forces to agree with it. New rows should put
   one identifier in one cell, but **1,195 existing cells hold several**
   and were deliberately not rewritten (MH-009) — the join expands them.
   Do not flag those as defects; they are recorded.

   Do check `independence_group` before accepting "multiple sources":
   two join rows in one group are one independent observation. **28
   `VERIFIED` claims currently cite sources that collapse this way**, and
   the data does not distinguish an assessed-and-cleared collapse from an
   unassessed one. `RA-012` queues that reading; the validator lists the
   28 on every run.
8. **Status dimensions.** `evidence_status` is the only evidence gate.
   A row that is `APPROVED` editorially and `PROVISIONAL` evidentially
   is a `PROVISIONAL` claim. Flag any prose that reads otherwise.
9. **Overrides.** If the pull request was pushed past a failing
   validator, `00-CONTROLLER/OVERRIDE-LOG.csv` carries a row saying
   why, by whom, and when it expires. No row, no override — and an
   override is not an answer to a defect.

## What not to do

Do not rewrite the research to fix it. Report findings as review
comments and let Claude Code repair. Do not approve a pull request
that contains a `VERIFIED` row you could not trace.

Do not accept a register row that was reworded to make the validator
pass. A row that cannot be migrated without changing its meaning
belongs in `00-CONTROLLER/MIGRATION-HOLDS.csv` unchanged; if a
migration commit altered what a claim asserts, that is the finding.
