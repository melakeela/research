# validate-registers.py — findings against the tree of 2026-09-07

**Run:** `python3 04-AUDITS/validate-registers.py` from the repository root
**Result:** exit 1, 43 failures
**Deliberately not fixed in the session that recorded them.** This file is the
list, so the owner can see the current state of the registers before deciding
what each failure means. Nothing below was repaired, downgraded or deleted.

The failures fall into three classes, and the first two are disagreements about
a rule rather than rows that are simply wrong.

> **Correction note added 2026-09-07, on the register-consolidation pass.**
> Everything in this document is preserved as written and was accurate when
> recorded. Most of it is no longer true of the tree, and the change that
> made it untrue is the one this document said it was declining to make.
>
> - **Class 1 is resolved. Option 1 was taken — on the owner's instruction,
>   not by act.** This document said Option 1 "is not taken here because
>   amending the validator to make current rows pass is exactly the move the
>   repository forbids doing casually". The owner subsequently instructed the
>   change in those terms ("accept semicolon-separated `source_id` values,
>   resolving each individually — a measurement resting on four sources
>   records all four"). `04-AUDITS/validate-registers.py` now splits on `;`
>   and resolves each identifier; a cell passes only if every identifier in
>   it resolves, and a cell that is non-empty but names no identifier (`";"`)
>   fails. The 42 Class 1 failures are gone.
> - **The headline counts are stale.** "exit 1, 43 failures" and "42 of 43"
>   describe the tree before that change. The run after it reports **1**
>   failure. The raw output block at the foot of this document is that older
>   run and is kept as the record of it.
> - **"access-ledger.csv, which has 52 rows" is wrong now: it has 68**,
>   `SRC-001` to `SRC-068`. Every identifier this document listed as
>   resolving still resolves.
> - **Class 2 is unchanged and still open.** The `E-11` prose status is the
>   one remaining failure, deliberately not fixed, for the reason this
>   document gives. Its reported line moved from 12 to 61 — the register now
>   carries a header comment block, and the validator reports true file
>   lines.
> - **Class 3 is unchanged.**
> - **One thing Option 1 did not settle.** `CLAUDE.md`'s register format
>   still says a row's `source_id` "must resolve to a row in the access
>   ledger", singular. The multi-source convention is now enforced by the
>   validator and written down nowhere else. Raised as **`D-044`**.
> - **What this document says the validator does not check is still true**,
>   with one subtraction: `D-` references are now resolved through
>   `09-DECISIONS/DECISION-ID-MAP.csv` as well as `OWNER-DECISIONS.csv`.
>   Queued for re-audit as `RA-012`.

---

## Class 1 — multi-valued `source_id` cells (42 of 43)

`03-REGISTERS/rigveda-pur-family.csv` rows 2–26 (24 failures) and
`03-REGISTERS/domain-e-claims.csv` rows 3–19 and 27 (18 failures).

Every one reports `source_id ... not in access ledger` for a cell such as
`SRC-019; SRC-022; SRC-023; SRC-047`. **Each identifier in those cells does
resolve**: `SRC-019`, `SRC-021`, `SRC-022`, `SRC-023`, `SRC-024`, `SRC-026`,
`SRC-037`, `SRC-040`, `SRC-043`, `SRC-046` and `SRC-047` are all present in
`02-SOURCES/access-ledger.csv`, which has 52 rows. What fails is the whole cell
read as one identifier.

This is a real disagreement between two rules, not a typo:

- `CLAUDE.md`'s register format gives one `source_id` per row, and says it
  "must resolve to a row in the access ledger" — singular. The validator
  implements that reading literally.
- The registers as written record every source a claim rests on, which for a
  corpus measurement is routinely four: the repository clone, the lemma layer,
  the strata layer and the derived token table. Splitting one claim across four
  rows would break the one-claim-per-row rule instead.

Three ways out, all of them the owner's call, none taken here:

1. The validator splits on `;` and resolves each identifier. Cheapest, and it
   makes the existing registers pass unchanged.
2. The register format gains an explicit multi-source column
   (`source_ids`, semicolon-delimited) and `CLAUDE.md` is amended to say so.
3. The registers are rewritten to one source per row, and claims that rest on
   several sources gain a dependency row instead.

Option 1 is the smallest change that keeps both rules true. It is not taken
here because amending the validator to make current rows pass is exactly the
move the repository forbids doing casually, and because a note in
`02-SOURCES/dependency.csv` may be the better home for the multi-source case.

## Class 2 — a status cell carrying prose (1 of 43)

`03-REGISTERS/domain-e-hypothesis-eligibility.csv` row 12, hypothesis `E-11`:

    status = "VERIFIED as a measurement; not a claim about origins"

`CLAUDE.md` requires exactly one status per claim from a closed vocabulary, and
`VERIFIED as a measurement; not a claim about origins` is not in it. The
qualification the cell is carrying is correct and load-bearing — the row exists
so that the 253-lemma residue can never be cited as a count of borrowings — but
it belongs in `reason` or `proportional_space`, not in `status`. The row's
`eligible_for_extended_analysis` cell already does the same job properly
(`NOT-A-HYPOTHESIS — a residue, never a rival explanation`).

The fix is to set `status` to `VERIFIED` and move the qualification into
`reason`. It is not made here because the row is the constitution §4.E
"unknown is residual" guard, and changing its status field without the owner
seeing the change is how a guard gets quietly loosened.

## Class 3 — unresolvable `D-` references (0 of 43, previously 2)

The as-received `00-CONTROLLER/PROGRAMME.md` cited two owner decisions numbered
past the end of the register — 037 and 039 — as blocking work. Neither exists;
`09-DECISIONS/OWNER-DECISIONS.csv` ends at `D-035`. (Their identifiers are not
written out here in full, because doing so would put the same two unresolvable
references straight back into the tree.) These two failures were removed by the
same pass that
reconciled `PROGRAMME.md`, because a controller document naming decisions that
were never allocated is a defect in that document rather than a state of the
registers. The underlying questions are preserved in `PROGRAMME.md` without
invented identifiers.

---

## What the validator does not check

Recorded so its silence is not read as a pass:

- It reads only `03-REGISTERS/*.csv`. `02-SOURCES/`, `04-AUDITS/`, `05-HOLDS/`,
  `06-BACKLOG/` and `09-DECISIONS/` are unchecked except as lookup tables.
- It checks that a `VERIFIED` row *has* a locator, never that the locator is
  specific enough to re-find — the failure mode `CLAUDE.md` and `AGENTS.md`
  both single out. "See the article" passes.
- It checks nothing about source independence, so a `VERIFIED` claim resting on
  four identifiers that all trace to one work passes. `DEP-001`, `DEP-008` and
  `DEP-009` record exactly that situation.
- It does not check that a `SUPERSEDED` row points at what replaced it.
- Its `D-` pattern is `D-\d{3}`, so the inherited two-digit `D-01`–`D-20`
  series is invisible to it — correct, since those resolve through
  `09-DECISIONS/DECISION-ID-MAP.csv` and have no `OWNER-DECISIONS.csv` rows.
- It cannot see whether a retrieval happened. It sees whether a row was
  written claiming one.

---

## The raw output

```
validate-registers: 43 failure(s)
  03-REGISTERS/domain-e-claims.csv:3: source_id SRC-019; SRC-022; SRC-023; SRC-047 not in access ledger
  03-REGISTERS/domain-e-claims.csv:4: source_id SRC-019; SRC-022; SRC-023; SRC-047 not in access ledger
  03-REGISTERS/domain-e-claims.csv:5: source_id SRC-019; SRC-022; SRC-023; SRC-047 not in access ledger
  03-REGISTERS/domain-e-claims.csv:6: source_id SRC-019; SRC-022; SRC-023; SRC-047 not in access ledger
  03-REGISTERS/domain-e-claims.csv:7: source_id SRC-019; SRC-022; SRC-023; SRC-047 not in access ledger
  03-REGISTERS/domain-e-claims.csv:8: source_id SRC-019; SRC-022; SRC-023; SRC-047 not in access ledger
  03-REGISTERS/domain-e-claims.csv:9: source_id SRC-019; SRC-022; SRC-023; SRC-047; SRC-026 not in access ledger
  03-REGISTERS/domain-e-claims.csv:10: source_id SRC-019; SRC-022; SRC-023; SRC-047; SRC-026 not in access ledger
  03-REGISTERS/domain-e-claims.csv:11: source_id SRC-019; SRC-022; SRC-023; SRC-047; SRC-026 not in access ledger
  03-REGISTERS/domain-e-claims.csv:12: source_id SRC-019; SRC-022; SRC-023; SRC-047 not in access ledger
  03-REGISTERS/domain-e-claims.csv:13: source_id SRC-019; SRC-022; SRC-023; SRC-047 not in access ledger
  03-REGISTERS/domain-e-claims.csv:14: source_id SRC-019; SRC-022; SRC-023; SRC-047 not in access ledger
  03-REGISTERS/domain-e-claims.csv:15: source_id SRC-019; SRC-022; SRC-023; SRC-047 not in access ledger
  03-REGISTERS/domain-e-claims.csv:16: source_id SRC-019; SRC-022; SRC-023; SRC-047 not in access ledger
  03-REGISTERS/domain-e-claims.csv:17: source_id SRC-019; SRC-022; SRC-023; SRC-047 not in access ledger
  03-REGISTERS/domain-e-claims.csv:18: source_id SRC-019; SRC-022; SRC-023; SRC-047; SRC-026 not in access ledger
  03-REGISTERS/domain-e-claims.csv:19: source_id SRC-019; SRC-022; SRC-023; SRC-047 not in access ledger
  03-REGISTERS/domain-e-claims.csv:27: source_id SRC-037; SRC-040; SRC-043; SRC-046 not in access ledger
  03-REGISTERS/domain-e-hypothesis-eligibility.csv:12: status 'VERIFIED as a measurement; not a claim about origins' not in vocabulary
  03-REGISTERS/rigveda-pur-family.csv:2: source_id SRC-019; SRC-022 not in access ledger
  03-REGISTERS/rigveda-pur-family.csv:3: source_id SRC-019; SRC-022; SRC-023 not in access ledger
  03-REGISTERS/rigveda-pur-family.csv:4: source_id SRC-019; SRC-022 not in access ledger
  03-REGISTERS/rigveda-pur-family.csv:5: source_id SRC-019; SRC-022 not in access ledger
  03-REGISTERS/rigveda-pur-family.csv:6: source_id SRC-019; SRC-022 not in access ledger
  03-REGISTERS/rigveda-pur-family.csv:7: source_id SRC-019; SRC-022 not in access ledger
  03-REGISTERS/rigveda-pur-family.csv:8: source_id SRC-019; SRC-022 not in access ledger
  03-REGISTERS/rigveda-pur-family.csv:9: source_id SRC-019; SRC-022 not in access ledger
  03-REGISTERS/rigveda-pur-family.csv:10: source_id SRC-019; SRC-021; SRC-022 not in access ledger
  03-REGISTERS/rigveda-pur-family.csv:11: source_id SRC-019; SRC-021; SRC-022 not in access ledger
  03-REGISTERS/rigveda-pur-family.csv:13: source_id SRC-019; SRC-023 not in access ledger
  03-REGISTERS/rigveda-pur-family.csv:14: source_id SRC-019; SRC-024 not in access ledger
  03-REGISTERS/rigveda-pur-family.csv:15: source_id SRC-019; SRC-022; SRC-023 not in access ledger
  03-REGISTERS/rigveda-pur-family.csv:16: source_id SRC-019; SRC-022; SRC-023 not in access ledger
  03-REGISTERS/rigveda-pur-family.csv:17: source_id SRC-019; SRC-022; SRC-023 not in access ledger
  03-REGISTERS/rigveda-pur-family.csv:18: source_id SRC-019; SRC-022; SRC-023 not in access ledger
  03-REGISTERS/rigveda-pur-family.csv:19: source_id SRC-019; SRC-022; SRC-023 not in access ledger
  03-REGISTERS/rigveda-pur-family.csv:20: source_id SRC-019; SRC-022 not in access ledger
  03-REGISTERS/rigveda-pur-family.csv:21: source_id SRC-019; SRC-022 not in access ledger
  03-REGISTERS/rigveda-pur-family.csv:22: source_id SRC-019; SRC-022; SRC-023 not in access ledger
  03-REGISTERS/rigveda-pur-family.csv:23: source_id SRC-019; SRC-022 not in access ledger
  03-REGISTERS/rigveda-pur-family.csv:24: source_id SRC-019; SRC-022 not in access ledger
  03-REGISTERS/rigveda-pur-family.csv:25: source_id SRC-019; SRC-022 not in access ledger
  03-REGISTERS/rigveda-pur-family.csv:26: source_id SRC-019; SRC-022 not in access ledger
```
