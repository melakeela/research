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
| `04-rules-and-gates.md` | §10.4 rule-by-rule compliance, posture derivation, adversarial tests, and the twelve build gates |

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

**The investigation rests on 47 claim rows, one hold, and one display
vocabulary.** `02-claim-basis.csv` names all 49 by identifier, with the screens
each feeds and what would verify it.

| Status | Rows | Child word |
|---|---:|---|
| `VERIFIED` | 35 | FOUND |
| `PROVISIONAL` | 10 | WE THINK |
| `HYPOTHESIS` | 2 | MAYBE |
| `HOLD` | 1 | WE DON'T KNOW — we haven't looked yet |
| `INHERITED-UNVERIFIED` | 1 | *(the vocabulary itself — `CP-VOCAB-001`, see below)* |

Four rows (`PUR-022`, `PUR-023`, `PUR4J-030`, and `PUR4J-016` in part) appear on
**no screen**: they are the rows the design reasons *about* — the named-entity
material a forbidden COMPARE step would have used, and the exclusion that would
change every count. They are listed so the audit trail is wider than the
child-facing surface.

### The lowest status is not `HYPOTHESIS`

**Among the claim rows it is `HYPOTHESIS`.** Below that, the investigation rests
on one thing that is `INHERITED-UNVERIFIED`, and it is not a minor one: **the
four-word vocabulary itself.** `FOUND / WE THINK / MAYBE / WE DON'T KNOW` comes
from `01-INHERITED/chatgpt-project-handoff.md` L347 and
`06-BACKLOG/EXPANSION-PROMPT-2026-09-07.md` L254; backlog item 33's flow and
§10.4.7's three prohibitions are inherited too.

A display vocabulary is not a claim about the past, so "verification" does not
apply to it — but the *assertion that it maps onto the seven statuses losing
nothing* is a claim, it is the claim the entire design rests on, and an earlier
draft made it and **it was false**. Corrected at `01-investigation-spec.md`
§0.1, which now states both losses: `WE GOT THIS WRONG` is not a status at all,
and three different things map onto `WE DON'T KNOW`, so the mapping does not run
backwards. §10.4.7's prohibitions bind regardless of their status, because they
are prohibitions on what the institution builds.

### The two `HYPOTHESIS` rows

- **`PUR-028`** — Arnold's five periods as real chronological stages. The whole
  of screen **S-09** stands on it and carries a banner saying so that cannot be
  dismissed.
  **What would verify it:** a stratification by an instrument that is not
  Arnold's metre — a retrieved non-metrical periodisation, or an independent
  metrical one built without reference to Arnold — applied to the same corpus
  and agreeing, together with retrieval of the literature contesting Arnold
  since 1905. It **cannot** be settled from the pinned corpus: `strata.json`
  *is* Arnold (`PUR-013`), so no re-run of it tests it. Arnold himself calls the
  period names "provisional" (1905 §§60–61).
- **`PUR-027`** — the púr- as attacked rather than inhabited. Shown as MAYBE at
  S-08 and S-12, now beside `PUR4J-013`, which argues with it.
  **What would verify it:** a passage-by-passage reading of the grammatical role
  across all 106 tokens. `PUR4J-020` has since measured the case distribution
  over all 83 simplex tokens, which is a substantial part of it; whether that
  discharges the blocker is `RA-020`. Not treated as discharged.

### The hold

**`HOLD-007`**, raised by this unit. Not a claim ranked below `HYPOTHESIS` — a
retrieval nobody has run. Screen **S-10** is entirely about it.

### The ten `PROVISIONAL` rows

Eight are capped at `PROVISIONAL` and can never be anything else:
`04-AUDITS/rigveda-pur-4j-method.md` §7 holds that a `VERIFIED` row is a count,
a form, a gloss or a printed rendering, and each is a *reading*. An independent
second coder raises confidence, not status.

Two are not simply capped, and the CSV says so rather than hiding them under the
cap: **`PUR4J-I-02`** has a specific, cheap, unattempted retrieval behind it
(where MelaKeela's 99 came from; a pre-Griffith English source), and
**`PUR4J-024`** is part retrieval and part judgement. And three `VERIFIED` rows
— `PUR-003`, `PUR-004`, `PUR-005` — carry `RA-001` open against them, so
"already `VERIFIED`" is the one thing they are not; their CSV rows now say so.

## Adversarial review

This unit was adversarially reviewed on 2026-09-08 by an agent that did not
produce it, and repaired. Four repairs changed a position rather than a
sentence, and all four are recorded in place:

1. **The posture derivation gives Reading Room, where Field Mode is
   forbidden — so this investigation can only be built on a logged editorial
   override.** It took two review passes to get here. The first draft asserted
   §1.5 rule 3 (absence dominance) without counting, and had silently amended
   the rule to "typed absences **or holds**" — the holds `04-rules-and-gates.md`
   §5 insists are not typed absences, so §3 and §5 contradicted each other. The
   first repair counted properly (2 rows of 47; rule 3 fails) but then treated
   §1.5 as a **ballot** — listing rules 3, 4 and 7 as parallel candidates and
   noting "two of the three permit Field Mode" — when §1.5's own words are
   *"Derivation inputs, **in precedence order**"*. That tally cannot exist, it
   made a binary outcome look 2:1 favourable, and it also skipped rule 6
   entirely. §3 now runs the cascade in order: rules 1–6 all fail (rule 6 on
   `ARCHIVE-AND-POWER-AUDIT.csv`, whose six rows are all domain E and none bear
   on this corpus), and rule 7 gives **Reading Room**. Gate G-01 is the
   override, not a re-derivation. Also logged `IC-P-004`: §1.7's table and its
   own prose disagree about Reading Room, and this rests on the table.
2. **`PUR4J-013` was missing from the entire unit, and adding it introduced a
   fresh bias failure — logged as `BF-021`.** The row records that only one of
   the eight metal forts is a named enemy's, and that in two of them the fort
   *is* a god or a river. Omitting it left `PUR-027` less challenged than the
   register leaves it. But the card written to fix that took 1-of-8 — the figure
   most favourable to a deflationary reading — while `PUR4J-013`'s own note
   states the 3-of-8 alternative; dropped the two Soma-myth passages so the
   arithmetic did not close, on a counting screen; and said "five are asking for
   protection" where the row supports two. **All three drifted the same way,
   on the screen added to correct the opposite bias.** `BF-014` had already
   logged that direction against this material in the parent unit, which is why
   `BF-021`'s control is a standing rule: when copy is added to correct a bias,
   the test for the opposite bias is re-run against that addition, because the
   original test predates it.
3. **S-08 performed the excluded move with the vocabulary removed** — "the
   other side", "somebody else's forts" — while S-10 told the child the museum
   was not showing them that material. The COMPARE terms are now the verb and
   the grammatical role.
4. **Four child-facing FOUND statements overstated their rows**, and all four
   overstated toward this investigation's own thesis. That direction is the
   finding, not the four sentences.

Also repaired across the two passes: unsourced dates removed throughout (nothing
in this repository dates the Rigveda); `PUR4J-I-02` labelled FOUND at
`PROVISIONAL` on the one line where the inherited "99" reached an evidence
screen, which gate G-04 passed; the §0.1 claim that the status mapping "loses
nothing", false in two ways; S-11's bins, which first collapsed the three kinds
of WE DON'T KNOW and then labelled one statement by the status of its
*negation* — fixed by flipping the statement, at the cost of the one card a
child could place wrong; S-09's token-level distribution, which `PUR-018` says
overstates, now the hymn unit under gate G-12 with two aggregation rules it also
lacks; `HOLD-007` naming a period and a region it has no source for; and
`RA-002` colliding with an existing identifier.

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
