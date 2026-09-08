# Children's pilot — "A hundred stone forts"

**Written:** 2026-09-08
**Unit type:** product specification. One complete children's investigation,
specified end to end, for ages 8–11.
**Governing framework:** `13-PRODUCT-ARCHITECTURE/museum-framework.md` §10.4
(with §10.3 Field Bag, §10.4.7 interface prohibitions, §1.5 posture derivation,
§1.7 mode matrix, §9 PROVE IT).
**Governing method:** `00-CONTROLLER/METHODOLOGY-CONSTITUTION.md` §4J, §5 step 14,
§6 negative evidence, §7 translation standard, §8 adversarial tests.
**Evidence base:** `03-REGISTERS/rigveda-pur-family.csv` (28 claims),
`rigveda-pur-4j-claims.csv` (32 claims), `rigveda-pur-4j-interpretations.csv`
(3 rows), `rigveda-pur-counts.csv`, `rigveda-pur-fields.csv`,
`rigveda-pur-typology.csv`, `rigveda-pur-passages.csv`,
`rigveda-pur-family-occurrences.csv`; read through
`06-BRIEFS/rv01-reconciliation.md`.

## Files

| File | What it is |
|---|---|
| `README.md` | this index; scope, gates, and the headline status answer |
| `01-investigation-spec.md` | the investigation: 14 screens, every action, every conclusion |
| `02-claim-basis.csv` | every claim the investigation rests on, by `claim_id`, per screen, with what would verify it |
| `03-evidence-cards.md` | the exact evidence a child sees, verbatim, with locators |
| `04-rules-and-gates.md` | §10.4 rule-by-rule compliance, posture derivation, adversarial tests, and the eleven build gates |

## Scope

**Specification only. No code, no markup, no asset.** Nothing here is built and
nothing here is published. `06-BRIEFS/mvp-fifteen/README.md` §0 records that
`DECISIONS-NEEDED.md` D-032 and `RESEARCH-QUEUE.md` both stand in front of page
work; the same controls stand in front of this, and this unit does not clear
them. It was produced on the owner's instruction of 2026-09-08, which is not
registered as a standing decision and is not allocated one here.

**No retrieval was performed.** No row was added to
`02-SOURCES/access-ledger.csv`, no claim moved status, and no domain was
requested. Every figure in this directory is quoted from a register row that
already carried it, with its `claim_id` attached at the point of use.

## The headline answer this unit was asked for

**The investigation rests on 38 register rows, plus one hold.**
`02-claim-basis.csv` names all 39 by identifier, with the screens each feeds and
what would verify it.

| Status | Rows | Child word |
|---|---:|---|
| `VERIFIED` | 27 | FOUND |
| `PROVISIONAL` | 9 | WE THINK |
| `HYPOTHESIS` | 2 | MAYBE |
| `HOLD` | 1 | WE DON'T KNOW — we haven't looked yet |

**The lowest status among the claim rows is `HYPOTHESIS`**, on two:

- **`PUR-028`** — *"Arnold's five periods correspond to real chronological stages
  of composition."* The whole of screen **S-09** stands on it, and S-09 carries a
  banner saying so that cannot be dismissed.
  **What would verify it:** a stratification of the Rigveda by an instrument that
  is not Arnold's metre — a retrieved non-metrical periodisation, or an
  independent metrical one built without reference to Arnold — applied to the
  same corpus and agreeing with it, together with retrieval of the literature
  contesting Arnold since 1905. It **cannot** be settled from the pinned corpus:
  `strata.json` *is* Arnold (`PUR-013`), so no re-run of it tests it. Arnold
  himself calls the period names "provisional" (1905 §§60–61).
- **`PUR-027`** — *"The Rigvedic púr- is a fortification of a kind the composers
  attack rather than inhabit."* Shown on **S-08** and **S-12**, labelled MAYBE.
  **What would verify it:** a passage-by-passage reading of the grammatical role
  of `púr-` across all 106 tokens. `PUR4J-020` has since measured the case
  distribution over all 83 simplex tokens, which is a substantial part of that
  reading; whether it discharges the blocker is a re-audit question, raised here
  as `RA-002`. It is **not** treated as discharged, and the row is quoted at
  `HYPOTHESIS`.

**Separately, one item the investigation rests on is a `HOLD`** — `HOLD-007`,
raised by this unit. It is not a claim ranked below `HYPOTHESIS`; it is a
retrieval that has not been run, and screen **S-10** is entirely about it.

**Nine `PROVISIONAL` rows, and seven of them can never be anything else.**
`04-AUDITS/rigveda-pur-4j-method.md` §7 holds that a `VERIFIED` row is a count,
a form, a gloss or a printed rendering. Every one of the nine is a *reading*, so
the register caps it at `PROVISIONAL` by construction. An independent second
coder would raise confidence in them; it would not raise their status. Two
(`PUR4J-I-02`, `PUR4J-024`) additionally have retrieval that would sharpen them
without promoting them. Where that is the answer, `02-claim-basis.csv` says so
rather than inventing a retrieval that would not change anything.

## What this unit found while specifying

1. **The ground is not in this repository.** All 88 rows of
   `02-SOURCES/access-ledger.csv` were read: there is no excavation report, no
   site report, no archaeological dataset, no survey, no geographic source.
   `PUR4J-018` (`VERIFIED`) and `PUR4J-024` (`PROVISIONAL`) already say so from
   the corpus side. Raised as `05-HOLDS/HOLD-007`. This is **not** typed as an
   absence under constitution §6 — see `04-rules-and-gates.md` §5, which is the
   distinction the investigation exists to teach.
2. **`DEP-021` points at the wrong source.** Its `source_b` is `SRC-026`
   (Arnold 1905, on metre) where its own prose describes Grassmann's
   *Wörterbuch*, which has no ledger row — its glosses reach the registers
   through `matched_lemmata.json` inside the pinned clone. The dependency it
   records is correct and `PUR4J-022` and gate G-06 both rest on it; only the
   pointer is wrong, so the row cannot be checked by following it. Logged as
   `IC-P-003`.
3. **`PUR4J-I-02` carries a stale figure.** Its `evidence_for` reads "6 passages
   against 8 for one hundred"; `PUR4J-002` and `PUR4J-003` were corrected to 9.
   Logged as `IC-P-002` in `04-AUDITS/INTERNAL-CONTRADICTIONS.csv`. The
   investigation quotes 9, from `PUR4J-002`.

## What this unit does not decide

The children's pilot is `OWNER-DECISIONS.csv` **D-006**, which offers Keezhadi
or an inscription. This is neither. **D-046** is allocated and raised in
`DECISIONS-NEEDED.md` for the question this unit cannot answer for the owner:
whether a corpus investigation is admissible as the pilot at all. Until it is
answered, this directory is a specification of a thing that may not be built.
