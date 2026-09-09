# The children's pilot — index

**Written:** 2026-09-09
**Unit type:** product specification. Specification only; no code, no public copy.
**Directory:** `06-BRIEFS/childrens-pilot/`

## What this unit is

One complete children's investigation, ages 8–11, specified screen by screen,
on the Rigvedic *púr-* ("fort") corpus.

**The question the investigation asks:** *why is a poem not a photograph?*

**What a child should be able to say at the end**, in their own words:

1. what the poem claims;
2. what the ground shows;
3. where the two do not meet.

The third is the finding. On the evidence this repository actually holds, the
answer to (2) is **we have not looked yet**, and (1) and (2) cannot be laid over
each other at all, because the poem states no place and the museum holds no
absolute date for it. That is not a shortfall in the specification. It is the
specification's result, and it is what makes the investigation honest.

## Files

| File | What it is |
|---|---|
| `INVESTIGATION-SPEC.md` | The specification. Every screen, every action, every piece of evidence, every conclusion the child is asked to reach. |
| `EVIDENCE-MANIFEST.csv` | One row per piece of evidence shown to a child. `claim_id`s, source, locator, child badge, and whether the display text is quoted from a register or must be pulled from a pinned source at build. |
| `SCREEN-CLAIM-DEPENDENCY.csv` | One row per screen. Every `claim_id` the screen rests on, the **lowest status among them**, and the unit that would raise it. |
| `REFUSED-AFFORDANCES.csv` | Everything this investigation deliberately does not let a child do, with the rule that forbids it. |
| `VERIFYING-UNITS.csv` | The units named as answers to "if it is not `VERIFIED`, what would verify it". |

## What this unit did not do

No retrieval was performed. No row was added to `02-SOURCES/access-ledger.csv`.
No claim moved status. No domain was requested. No register row was written
except the audit, hold and decision rows listed under *Rows written elsewhere*.

**Nothing here is public copy.** Indicative child-facing wording appears in the
specification so that the reading level and the honesty of each screen are
reviewable. It is specification wording. It has not been through constitution
§5 step 14, and no sentence of it may be lifted onto a page.

## Rows written elsewhere by this unit

| File | Row | Why |
|---|---|---|
| `05-HOLDS/HOLD-008-ground-evidence-for-the-pur-corpus.md` | new | The ground half of this investigation has no source. The hold names what is needed. |
| `09-DECISIONS/OWNER-DECISIONS.csv` | `D-055`, `D-056`, `D-057` | Three decisions this specification raises and does not take. |
| `DECISIONS-NEEDED.md` | `D-055`, `D-056` | The two that block. |
| `04-AUDITS/REAUDIT-QUEUE.csv` | `RQ-…` | A stale figure found in `PUR4J-I-02` while reading for this unit. |

## The three gates, in one place

**G-1 — posture. `BLOCKING`.** Museum framework §1.7 forbids Field Mode in the
Reading Room posture. The curatorial audit assigns `the-forts` to Reading Room
(`INHERITED-UNVERIFIED`). §1.5 derivation over *this investigation's* claim set
returns **Nocturnal Veḷi** (rule 3, absence dominance), where Field Mode is
*available*. The two answers differ, and posture is not the specification's to
assign. `D-055`.

**G-2 — the ground half. `BLOCKING`.** No archaeological source exists in
`02-SOURCES/access-ledger.csv`. Screen `CP-3.5` therefore reports an empty
shelf, truthfully, as the museum's own gap. Whether a children's pilot may ship
with a truthfully empty ground half is a product decision. `D-056`,
`HOLD-008`.

**G-3 — which pilot. `OPEN, not raised here`.** `D-006` asks whether the
children's pilot is Keezhadi or an inscription. This specification is neither.
It is offered as a third option and does not decide `D-006`. `D-057` records
the option so that the choice is made against a real description.

## What the investigation rests on

`03-REGISTERS/rigveda-pur-family.csv` (28 rows), `rigveda-pur-4j-claims.csv`
(32), `rigveda-pur-4j-interpretations.csv` (3), `rigveda-pur-passages.csv`
(103), `rigveda-pur-fields.csv` (103), `rigveda-pur-counts.csv`,
`rigveda-pur-typology.csv`, `domain-e-measurements.csv` (`DE-M-027`),
`04-AUDITS/ARCHIVE-AND-POWER-AUDIT.csv` (`APA-E-006`),
`06-BRIEFS/pur-translation-standard.md`, `06-BRIEFS/rv01-reconciliation.md`,
`13-PRODUCT-ARCHITECTURE/museum-framework.md` §10.

Of the 41 distinct `claim_id`s the investigation uses, **32 are `VERIFIED`, 8
are `PROVISIONAL`, 1 is `HYPOTHESIS`**. The `HYPOTHESIS` is `PUR-028` — that
Arnold's five metrical periods correspond to real stages of composition — and
it sits under the chronology screen, which is where this specification puts it
in front of the child rather than under them.
