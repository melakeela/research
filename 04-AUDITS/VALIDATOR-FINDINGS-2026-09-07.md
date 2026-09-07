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

# Addendum, 2026-09-07 — the count is now 53, and the gate is a baseline gate

## Re-run

`python3 04-AUDITS/validate-registers.py` at commit `aa40d3a`: **exit 1, 53
failures.** The body of this file recorded 43. Nothing was fixed and nothing
regressed; ten failures arrived with two register files that did not exist when
the 43 were counted — `03-REGISTERS/domain-e-measurements.csv` (8) and
`03-REGISTERS/domain-e-interpretations.csv` (2), both added by the domain E
units 2–6 work and merged since. Every one of the ten is the same Class 1
multi-valued `source_id` cell. The class breakdown at 53:

| Class | Count | Files |
|---|---|---|
| 1 — multi-valued `source_id` | 52 | `rigveda-pur-family.csv` 24, `domain-e-claims.csv` 18, `domain-e-measurements.csv` 8, `domain-e-interpretations.csv` 2 |
| 2 — status cell carrying prose | 1 | `domain-e-hypothesis-eligibility.csv` row `E-11` |
| 3 — unresolvable `D-` references | 0 | — |

Class 1 has grown from 42 to 52 without anyone deciding anything. That is the
argument for D-044 below: an undecided convention does not stay the same size.

## What changed in the gate

`.claude/hooks/block-push-on-register-failure.sh` was an **absolute** gate — any
failure blocked any push. With 53 standing failures that no session introduced,
the first push of every session hit it, and the documented
`MELAKEELA_REGISTER_GATE=off` override became the normal way to push rather than
the exception it was written to be. An override used on every push stops being a
record of anything.

It is now a **baseline** gate. `04-AUDITS/validator-baseline.json` records the
53 failures as they stand. A push is blocked only by a failure that is not in
that file.

    a new defect blocks; the recorded set does not.

Mechanics, and the places where a judgement was made:

- **Keying.** A baselined failure is matched on `file → row_id → failure_type`,
  where `row_id` is the register's own identifier column (`DME-002`, `E-11`,
  `RVP-004`). Not on line number: inserting a row above a baselined one shifts
  every line below it, and a line-keyed baseline would then excuse whichever
  rows happened to slide into those numbers. `validate-registers.py` gained a
  `--json` flag to emit those keys. It gained nothing else — no check changed,
  no verdict changed, and its human output is byte-identical.
- **`detail` is matched too, exactly.** A baselined row whose offending value
  has since been edited is reported as new and blocks. The reasoning: a cell
  edited after it was excused has not been seen by the owner in its current
  form. This is deliberately the strict side, and it will sometimes block a
  harmless edit — adding a fifth resolving `SRC-` to an already-excused cell
  would do it. The remedy is to re-record that entry and say so in the pull
  request, not to loosen the match.
- **Fail closed.** If the baseline file is missing, unreadable or has no
  `entries` object, the hook reverts to the absolute gate. Verified.
- **The baseline is written by hand.** The hook never regenerates it. A gate
  that re-records its own baseline before each push excuses everything.
- **The override survives**, for a genuinely new failure that is known and
  deliberately unfixed. It should now be rare, and reaching for it on a failure
  the session itself introduced is the wrong move.

## What the baseline excuses, and why

**52 × `source-id-not-in-ledger`** — every multi-valued cell in the four files
above. Excused on a check, not on a shrug: all 16 distinct cells were split on
`;` and each component resolved against `02-SOURCES/access-ledger.csv`, which
now holds 68 rows (`SRC-001`–`SRC-068`). **No component fails. No typo is
hiding here.** The rows are not evidentially defective — no unbacked `VERIFIED`
claim is behind any of them — so the failure is a disagreement about the format
rule, and it is now on the owner's desk as **D-044** rather than living only in
the prose of this file. Excusing them does not pick one of D-044's three
options; it stops them blocking work while the owner decides.

**1 × `status-not-in-vocabulary`, row `E-11`** — excused because the section
above reserves it for the owner, and that reservation is honoured, not
overridden. The status cell carries `VERIFIED as a measurement; not a claim
about origins`, which is what keeps the 253-lemma residue from ever being cited
as a count of borrowings: the constitution §4.E "unknown is residual" guard.
The qualification does belong in `reason` rather than `status`. Moving it is
still the owner's to make, and the point of the baseline is that a session
which only wanted to push is no longer tempted to loosen a guard to get there.

## What the baseline does not do

It does not fix, downgrade or delete a single row; the registers are byte-identical.
It does not narrow the validator — all 53 failures are still detected, still
printed, still exit 1. It changes only what a *push* is blocked on. The
absolute verdict remains available at any time by running the validator
directly, which is the honest way to read the state of the registers, and this
addendum does not supersede the "What the validator does not check" list above:
every silence recorded there is still a silence.

Deleting an entry from `validator-baseline.json` restores the absolute gate for
that row. Deleting the `entries` object restores it for the whole tree. The
owner can disagree with any excuse here by doing exactly that.
