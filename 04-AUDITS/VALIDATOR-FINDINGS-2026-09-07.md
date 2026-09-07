# validate-registers.py — findings against the tree of 2026-09-07

**Run:** `python3 04-AUDITS/validate-registers.py` from the repository root
**Result:** exit 1, 43 failures
**Deliberately not fixed in the session that recorded them.** This file is the
list, so the owner can see the current state of the registers before deciding
what each failure means. Nothing below was repaired, downgraded or deleted.

The failures fall into three classes, and the first two are disagreements about
a rule rather than rows that are simply wrong.

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

---

## Resolution, 2026-09-07 — owner answered `D-042`; both classes closed

These findings were recorded and deliberately left for the owner. They then
stopped being theoretical: the validator was wired as a push-blocking hook,
so the 43 failures blocked every push rather than merely recording a
disagreement, and the hook's own documented escape was unavailable in the
session that hit it. Raised as `D-042`; the owner chose **findings option 1
for class 1, plus the class 2 fix**, and both were made.

**Class 1 — multi-valued `source_id` cells (42 failures).** `validate-registers.py`
gains `source_ids()`, which splits a `source_id` cell on `;` and resolves each
identifier separately.

The module docstring now records why this is **stricter than what it replaced,
not looser** — which is the objection the original findings raised against
itself, and it does not survive inspection. Reading a four-identifier cell as
one identifier made it fail *wholesale*, so the identifiers inside it were
never checked at all. A negative test on a scratch tree makes the direction
concrete:

| row | cell | old | new |
|---|---|---|---|
| all four identifiers real | `SRC-001; SRC-002` | **fails** (uninformative) | passes |
| one identifier invented | `SRC-001; SRC-999` | fails, names the whole cell | **fails, names `SRC-999`** |
| single bad identifier | `SRC-404` | fails | fails |

The old rule could not distinguish a cell of four good identifiers from a cell
of three good and one invented. The new rule can. That is the whole of the
change.

**Class 2 — a status cell carrying prose (1 failure).**
`03-REGISTERS/domain-e-hypothesis-eligibility.csv` row `E-11`: `status` is now
`VERIFIED`, and the qualification it was carrying — *"as a measurement; not a
claim about origins"* — moved to the **head** of the `reason` cell rather than
being dropped. It is the constitution §4.E guard that stops the 253-lemma
retroflex residue from being cited as a count of borrowings, and the original
findings were right that changing this field carelessly is how a guard gets
quietly loosened. It is stated more prominently now than it was before, not
less. The row's `eligible_for_extended_analysis` cell already read
`NOT-A-HYPOTHESIS — a residue, never a rival explanation` and is untouched.

**Class 3** was already at zero.

**Result:** `validate-registers.py` exits 0 on the whole tree. 43 failures to
0, **none of them suppressed**. No register row was deleted, no status was
promoted, no claim changed its evidentiary standing, and the validator was not
weakened to get past its own gate.
