# Domain A — Rigvedic chronology and transmission: method

**Run:** 2026-09-08 / 2026-09-09
**Branch:** `claude/rigvedic-chronology-dependency-h449cc`
**Registers:** `03-REGISTERS/domain-a-measurements.csv` (21),
`domain-a-claims.csv` (15), `domain-a-eight-dates.csv` (8),
`domain-a-conventional-date-basis.csv` (7),
`domain-a-arnold-dependency.csv` (48),
`domain-a-hypothesis-eligibility.csv` (5)
**Script:** `04-AUDITS/domain-a-instruments.py` → `04-AUDITS/domain-a-tables/`
**Manifest:** `02-SOURCES/vedaweb-manifest-2026-09-09-domain-a.md`
**Ledger:** `SRC-099` … `SRC-118`. **Dependencies:** `DEP-029` … `DEP-036`.
**Contradictions:** `IC-A-001` … `IC-A-004`. **Bias failures:** `BF-027` … `BF-030`.
**Repaired 2026-09-09** against adversarial review; §15 lists what changed.
**Hold:** `HOLD-008`.

---

## 0. What this unit was for

Nearly every chronological claim in this repository rests on Arnold's metrical
strata, single-sourced via `DEP-001`, because VedaWeb's strata layer is a
transcription of Arnold 1905 and the two citations are one source. This unit
**examines that dependency rather than using it.**

That framing carries its own risk and it is named at the top rather than at the
bottom: a unit commissioned to audit an instrument has an incentive to find it
wanting. §8 below records what was done about that, and `DA-006` is the finding
that runs the other way — reported in the claims register at the same weight as
the findings that run with the framing.

## 1. Bound the question

**Proposition under test.** That the Rigveda cannot be treated as one
synchronic document, and that this repository's means of saying so are sound.

**Date range.** Second and first millennia BCE for the object; 1876–2021 for
the instruments; 2020 for the digital bundle.

**Geography.** Not the operative axis here. Where it enters — the Mitanni
material in northern Mesopotamia, the Near Eastern iron horizon — it is flagged
as a place the argument silently travels to (`DA-C-002`, `DA-C-003`).

**Evidence classes needed.** Textual (three transmitted forms), metrical
(Arnold), editorial-apparatus (five scholars' flags), secondary literature.
Archaeological and epigraphic evidence bears on the pillars and none of it was
retrievable in this session beyond abstracts.

**Terms needing original-language work.** `ayas-` (the whole of pillar 3 turns
on it), `chandas-` (Pāṇini's term, and the corpus term the strata partition),
`ṛṣi-` and the Anukramaṇī ascriptions. §7 below.

**The null explanation.** That the observable heterogeneity of the Rigveda is
genre, metre, subject and regional style, with no recoverable time axis. This
is a live rival throughout and it is never treated as the residue: it is the
explanation `DA-M-005` and `DA-M-006` are designed to be able to support.

## 2. Chronology first — the eight dates

Kept in their own register precisely so that one cannot stand for another.
Composition · oral circulation before fixation · collection and arrangement ·
Saṃhitāpāṭha fixation · the Padapāṭha analysis · Pāṇini · manuscript copying ·
modern scholarly interpretation.

**Six of the eight are `HYPOTHESIS` or `HOLD` in this record.** Two are
`VERIFIED`, and they are the two that need no external evidence: that no date
is attested anywhere in the corpus (`DA-D-001`), and the dates of the
instruments themselves (`DA-D-008`). The apparatus by which this repository
knows anything about Rigvedic chronology was made between 1876 and 2021, and
its chronological core was made in 1905.

## 3. Geography and contact

Not run as a separate gate: the proposition is temporal. Two geographic facts
are recorded where they bear on the pillars. The Mitanni evidence is in
northern Mesopotamia and is not the Rigveda; the iron chronology retrieved for
pillar 3 (`SRC-113`) is for the Near East and not South Asia. Both are cases of
an argument borrowing a place it does not declare.

## 4. Evidence classes, inventoried separately

**Textual.** Three complete forms of the same text in one bundle: the
transmitted Saṃhitāpāṭha (`SRC-020`), the Padapāṭha (`SRC-021`), and a modern
metrical restoration (`SRC-078`). The third is an editorial reconstruction and
is never treated as a witness.

**Metrical.** `strata.json` (`SRC-023`) — one metre label and one stratum code
for each of 39,833 pādas. One source: Arnold 1905.

**Editorial apparatus.** `stanza_properties.json` (`SRC-071`) — five scholars'
stanza-level flags. Measured, not assumed, to be fewer instruments than five.

**Secondary literature.** Ten works reached, all at abstract or snippet level.
The one that matters:

> **Hellwig, Scarlata and Widmer, "Reassessing Rigvedic Strata", JAOS 2021**
> (`SRC-105`, abstract as returned by Consensus on 2026-09-08):
>
> "In this article we review stratifications proposed in previous literature and
> assess the support for these strata by performing statistical analyses with
> allomorphic linguistic features that have been claimed to bear signals of
> stratification. In addition, we run a cluster analysis exploring how the books
> are grouped given the same allomorphic linguistic data. Our results show that
> once we control for metrical positioning, prosodic structure, and content, the
> allomorph distributions do not lend significant support for any of the
> proposed stratifications. Moreover, the cluster analysis favors the assumption
> that book 10 occupies a special position, but overall differences across the
> ten books of the Rigveda are not substantial."

**What that tested, precisely** — because the record must state it and not a
summary of it. The units are *allomorphic linguistic features previously claimed
to bear stratification signals*. The comparison is against *the stratifications
proposed in previous literature*. The controls are *metrical positioning,
prosodic structure and content*. The result is that the allomorph distributions
do not significantly support those proposals.

**What it therefore does not establish**, none of it claimed by the abstract:
that the Rigveda is chronologically homogeneous; that Arnold's metrical
stratification in particular is unsupported — the controls *include* metrical
positioning, which is a different move from testing metre; or that no relative
chronology exists. It is a null on one evidence class against one set of
proposals. `DA-008`.

**And it cannot be read more finely than that here.** The full text was not
retrieved. Which allomorphs, which stratifications, which controls — none is
checkable. `HOLD-008`.

**Class boundaries were not crossed.** The metrical evidence is never allowed
to borrow certainty from the textual, and the 2021 allomorphic result is not
imported as a verdict on metre.

## 5. Source genealogy — the unit's central operation

Seven dependency rows, `DEP-029` … `DEP-035`. Three were measured rather than
asserted, which is the point of method step 5:

- **`DEP-030`. Oldenberg and Wüst are approximately one instrument.** They share
  641 of their 699 and 709 flagged stanzas; Jaccard 0.836. The 2026-09-07
  manifest described these columns as "four further scholars' judgements … from
  different evidence (style, grammar, textual criticism, history)" and asked
  whether they agree with Arnold. Half the answer is that they are not four.
- **`DEP-035`. `DEP-022` with a number.** 94.12% of the Arnold(*Sketch*, 1897)
  flags sit inside Arnold's (1905) late strata, against a 29.0% corpus rate —
  the highest enrichment of the five columns and 17 points above the next.
  One scholar being consistent with himself across eight years.
- **`DEP-031`. The most promising independent metrical instrument is by the man
  who transcribed Arnold.** Kevin M. Ryan is named in the TEI header as one of
  the two compilers of `strata.json` and is the author of `SRC-112`, the 2021
  cadence argument that Consensus returned. Whether that paper delimits "oldest
  material" independently of Arnold decides whether it is an instrument at all,
  and the abstract does not say. Recorded as **UNDETERMINED**, not resolved
  either way. Queued as `RA-022`.

- **`DEP-036`. The one instrument that supports Arnold got the least scrutiny.**
  Added 2026-09-09 after adversarial review. Grassmann's independence from
  Arnold was measured *column against column* inside `stanza_properties.json`,
  which cannot see whether Arnold 1905 **read** Grassmann 1876–7 — and
  Grassmann's edition is among the works nineteenth-century metrical chronology
  was built on. `DEP-031` asks exactly this of Ryan and answers UNDETERMINED; no
  equivalent row existed for Grassmann until the review asked for it. Untestable
  here: Arnold 1905 is `EGRESS_BLOCKED`. `DA-M-023`, `BF-029`, `RA-027`.

After these, the count of instruments bearing on Arnold's strata that are
neither Arnold nor entangled with each other is **one**: Grassmann 1876–7 —
and whether *that* one is independent of Arnold is now itself an open row.

## 6. Archive audit

**Who made the surviving record.** The Rigvedic evidence base of this
repository is a git clone of printed editions made by European philologists
between 1876 and 1994, annotated at Cologne and Zürich in 2020. There is no
manuscript in it (`DA-D-007`) and no non-European scholarly source anywhere in
it — the same finding the §4J unit recorded as its "one live risk not fully
closed", now true of this unit too. Sāyaṇa is absent. The Anukramaṇī tradition
reaches this record only through Geldner's hymn-group headings, at three
removes, as the 2026-09-07 extension records.

**What preserved it.** A recitational tradition that preserved syllable count
and accent extraordinarily well and normalised boundary phonology uniformly
(`DA-012`). That is a real asymmetry in what survives, and it is the reason a
metrical instrument is possible at all and the reason it is noisy.

**What was unlikely to be recorded.** Everything that was not a hymn admitted
to this collection. The Rigveda is an anthology of one priestly tradition's
liturgical poetry; the constitution's own §4B genre-and-survivorship warning
applies with full force and is inherited here rather than re-argued.

**What is unexcavated or unrecognised — for this unit specifically.** Not
soil: *shelf*. Arnold 1905, Oldenberg 1888, the Hellwig–Scarlata–Widmer full
text and every Pāṇini source are all unreadable from this session. The
blockage is one-sided in a way worth naming: what remains reachable is the
transcribed digital layer, and what is blocked is every document that would let
that layer be checked.

**Who got the credit.** `strata.json` is Arnold's analysis under Gunkel and
Ryan's compilation and CCeH's publication. The recitational tradition that
produced and preserved both the Saṃhitāpāṭha and the Padapāṭha — the object of
every measurement in §7 of this note — is named nowhere in the bundle's own
bibliography. Preservation is not authorship, and codification is not
invention; here the codifiers are credited and the preservers are not.
Constitution §4V.

## 7. Hypothesis gate

Five gated in `domain-a-hypothesis-eligibility.csv`. One `ELIGIBLE` (the
conventional date, **as a range only**), two `NOT-ELIGIBLE`, one
`NOT-ELIGIBLE-SOURCE-BLOCKED`, one `CANNOT-GATE`.

Arnold's strata are `NOT-ELIGIBLE-SOURCE-BLOCKED` and that verdict is
deliberate. They did not fail. The two documents that would decide them —
Arnold 1905 and the 2021 reassessment — are both unreadable in this session,
and gating on abstracts is the failure the inheritance rule exists to prevent.

**Translation standard, and what this unit did not do.** Two consequential
words were identified and neither was worked:

- **`áyas-`.** Pillar 3 turns entirely on whether it means iron, copper, bronze
  or metal generally, and on whether the answer differs by passage. The full §7
  block — script, transliteration, grammatical form, semantic range, textual
  context, edition, exact locator, translation used, alternatives, interpretive
  consequence — was **not** produced. Until it is, the absence-of-iron argument
  cannot be assessed here at all, and `DA-C-003` says so rather than assessing
  it. `PUR4J-012` records `ayasa-` "of metal" in eight `púr-` passages without
  deciding which metal, and that is the honest state of the record.
- **`chandas-`.** Pāṇini's term for the Vedic register and the thing Arnold's
  strata partition. No Pāṇini source has ever been retrieved here (`DA-D-006`),
  so the word has no entry in this record.

**One §4.A item was filed in the wrong place and is now separated.** *Metre as
evidence for older pronunciation* (item 8) is a different claim from *later
sandhi obscuring an older metrical form* (item 9). Item 9 says the transmitted
text hides a metrical shape; item 8 says the metrical shape tells us how the
language sounded. This unit measured the disyllabic restorations — `-iya-`,
`-uva-` — and filed all of them under item 9. The inference to a phonological
stage was never made. `DA-017` records that as a `HYPOTHESIS`, and `SRC-112` is
the one retrieved work that runs item 8, abstract-only and with its independence
from Arnold undetermined.

The inherited English categories audited before use in this unit: *period*,
*stratum*, *layer*, *early*, *late*, *original*, *interpolation*. Every one of
them is a chronological verdict wearing a descriptive coat, and the registers
are written so that "Arnold's late strata" never contracts to "the late
Rigveda".

## 8. The two adversarial tests

### Prestige-bias challenge

*Did this privilege a claim because it is canonical, Sanskritic, Brahmanical,
Indo-European, European, colonial, institutionally prestigious, repeatedly
cited or nationally useful?*

**Three catches.**

1. **The Cambridge monograph was nearly given standing it has not earned in
   this session.** Arnold 1905 is a canonical work whose result this repository
   has used in nine registers. The first draft of `DA-M-020` was written as
   though the stratum gloss were established. It is established *in this
   repository* from a single OCR reading made once on 2026-09-07 and not
   re-checked, because archive.org refused (`SRC-100`). The row now says so and
   `HOLD-008` records it.
2. **"Four scholars agree with Arnold" was about to be written.** Five column
   headings in a prestigious digital edition read as five instruments. Crossing
   them showed two of them are one (`DEP-030`) and one of them is Arnold
   (`DEP-035`). The dependency rows were logged **before any claim was allowed
   to rest on the columns** — `DEP-030` and `DEP-035` are in commit `8d88fd3`,
   the measurements register in `3bce762`. They were *not* written before the
   figures were computed: overlap and enrichment come out of the same run of
   the script. An earlier draft of `BF-027` said they were, which was false and
   is corrected in that row.
3. **The conventional date was nearly stated as a fact with sources appended.**
   The pillars register is written the other way round — each argument's *form*
   first, then what it can support, then what was actually retrieved — and it
   ends in a range because that is what the retrieved sources support.

### Preferred-counter-narrative challenge

*Did this accept a claim too easily because it is Dravidian, Indigenous,
anti-colonial, anti-Brahmanical, subaltern, diffusionist or politically
corrective?*

**Three catches, and this test bit harder than the first one.**

1. **The unit's own commission is a counter-narrative.** "The chronology rests
   on one 1905 source" is a debunking frame, and a debunking frame finds
   debunkings. The correction is `DA-006`, `DA-M-011` and `DA-M-012`: the
   control that would have made the sceptical result cleanest — removing book
   10, the known confound at `DEP-004` — was run, and it made Arnold look
   *better*, not worse. Grassmann's flags are enriched 2.34× in Arnold's late
   strata within books 1–9. That is reported in the claims register, in the
   commit message and in the summary, not buried in a notes field. A claim that
   Arnold's strata rest on nothing outside Arnold is false and this record does
   not make it.
2. **`SRC-115` was nearly used as a counterweight.** Semenenko 2019 runs the
   absence-of-iron argument form to a date "prior to 2600 BC" — roughly 1,300
   years earlier than the conventional one, and squarely useful to an
   indigenist position. It is recorded, and it is recorded explicitly as
   *evidence about what the argument form can fix*, not as a rival date, and
   `DA-C-003` states that this record adopts neither date. Reversing the
   hierarchy is the same failure as keeping it. Constitution §2.
3. **"Books 8 and 9 are earliest" was available and was not taken.** The
   measurement (`DA-M-004`) is striking: the two books the constitution calls
   internally complicated carry the *lowest* Arnold-late shares in the corpus, a
   result that would embarrass the standard family-book story. `DA-003` refuses
   to draw it, on the ground that a metrical instrument ranking book 9 earliest
   is more likely reporting that book 9 is 73.3% Normal metre than that it is
   old. The measurement stands; the inference is declined.

4. **The failure this test did *not* catch, found by adversarial review.**
   Having corrected itself for running sceptical, the unit then shielded its one
   favourable finding: Grassmann's independence from Arnold was asserted and
   never tested, while the identical question was asked and left open for Ryan.
   Two smaller instances run the same way — `DA-M-006` reported the weakest of
   the available association statistics, the one most favourable to Arnold, with
   the stronger ones computable from the same table; and `DA-008` added an
   exculpation ("that Arnold's metrical stratification in particular is
   unsupported") that the abstract cannot support, since the abstract says *any*
   of the proposed stratifications. All three are repaired and logged as
   `BF-029`. **A unit that has just corrected itself for scepticism is at its
   most vulnerable to the opposite error, and `BF-028` is where that
   vulnerability was created.**
5. **And the bookkeeping failure, `BF-030`.** Three counts the unit made about
   *itself* were wrong or unstated, and the `SRC-026` anomaly — one source id
   naming two different works — was noticed and normalised into 29 notes fields
   instead of being logged. An auditor applying a weaker standard to its own
   record than to the audited material. `IC-A-001`, `IC-A-003`.

**Neither correction pretends the archives are equal.** Arnold, Oldenberg,
Grassmann, Wüst and Geldner were produced and preserved by a European
institutional apparatus that has no counterpart in this record for the
tradition that made and kept the text. Noting that Grassmann corroborates
Arnold does not make the corroboration independent of that apparatus; it makes
it a second reading from inside it.

## 9. Negative evidence, typed

Constitution §6. No absence argument in this unit is made without a type.

| Absence | Type | Why |
|---|---|---|
| No date in the Rigvedic corpus | `NOT PRODUCED` | A hymn is not a document that records its date. Carries no information. |
| No Pāṇini source in this repository | `NOT PRODUCED` | No search has ever been run for one in any session. A fact about this record only. |
| Arnold 1905 unreadable this session | `NOT ACCESSIBLE` | `SRC-100`, archive.org refused at the egress proxy. Was readable on 2026-09-07. |
| Hellwig–Scarlata–Widmer full text | `NOT ACCESSIBLE` | JSTOR venue; `SRC-032` and `SRC-100`. |
| Scite citation-context measurement | `NOT ACCESSIBLE` | `SRC-104`, monthly quota. Step 11 cannot be run. |
| No Archaic pāda in books 3, 4, 7 | **not typed as an absence at all** | It is a property of Arnold's assignment, not of the corpus. Recorded at `DA-M-005` as a fact about the instrument. |
| No stratum-code documentation in the bundle | `NOT PRODUCED` | The publisher documented the glossing abbreviations and not these. `DA-M-020`. |
| No co-variation between book order and Arnold's strata | `ABSENT DESPITE ADEQUATE SEARCH` for the data, `NOT PRODUCED` for the inference | Added 2026-09-09. Coverage is total — all 39,833 pādas — so the absence is not a sampling artefact. But ten books is too few units to resolve: exact two-sided *p* = 0.8651 and the null 95% range of ρ runs to ±0.64. The record establishes that Arnold's instrument supplies **no evidence** that book order tracks lateness, not that it supplies evidence against. `DA-M-003`, `DA-002`, `A-2`. |
| No non-European source in this unit | `NOT ACCESSIBLE` | `SRC-080`–`SRC-083` refused on 2026-09-07 and archive.org again here. |

"Unknown" appears nowhere in these registers as a rival explanation.

## 10. Bridges tested

Every link below is a separate claim and none is assumed:
metrical style → date (`A-1`, source-blocked);
book number → date (`A-2`, fails);
transmitted text → composed text (`A-3`, fails, and `DA-011` measures the gap);
Mitanni Indo-Aryan → Rigvedic language (`DA-C-002`, three incompatible
readings); Gāthic date → Rigvedic date (`DA-C-004`, inherits a 750-year spread);
Near Eastern iron horizon → South Asian text date (`DA-C-003`, the place
changes mid-argument).

## 11. Current standing

`SRC-105` (2021, JAOS, 5 citations at retrieval) is the most recent retrieved
assessment and returns a null on one evidence class. `SRC-104` — Scite, the
instrument that would show how it has been *received*, supporting against
contrasting — refused for quota. **Step 11 could not be run**, and the standing
recorded in `A-1` is "disputed and actively re-tested" rather than a measured
position. That is a gap, not a result.

Citation inertia is visible in the other direction: Arnold 1905 is used in this
repository through a 2020 transcription, and no session before this one had
crossed it against the other columns shipped in the same file.

## 12. Falsifiers

Recorded in the eligibility register per hypothesis. The three that would move
the most here: reading Arnold 1905 §265 and Appendix IV against `strata.json`
directly, to see whether the transcription is faithful and what the criteria
were; reading the 2021 full text, to see whether metre survives its controls;
and a §7 lemma study of `áyas-`, which is the whole of pillar 3. To that list
adversarial review adds a fourth: reading Arnold's bibliography and preface to
see whether he used Grassmann (`DEP-036`, `RA-027`). If he did, this unit's one
favourable finding stops being corroboration.

## 13. Step 13 — check MelaKeela itself

**Not run against `melakeela/site` in this unit.** The site is a separate
repository and no site claim about Rigvedic dating was retrieved here. Queued
as `RA-023` together with the prose sweep, because `SRC-117`'s scan covered
`03-REGISTERS/` only and stratum readings also appear in `06-BRIEFS/` and
`13-PRODUCT-ARCHITECTURE/`.

One internal check *was* run and passed: `DA-M-007` reproduces `PUR-012` exactly
on the uppercase/lowercase split (9,607 / 945) and adds a fact `PUR-012` did not
state — two stanzas mix stratum *letters*. Not a contradiction; an addition.

**Four contradictions were found, none of them by this unit's own step 13.** All
four came out of adversarial review: `IC-A-001` (the unit's count of its own
coverage), `IC-A-002` (sixteen flagged stanzas that `strata.json` does not
contain), `IC-A-003` (`SRC-026` names both Arnold 1905 and Grassmann's
*Wörterbuch*), `IC-A-004` (this unit's `A-1` duplicates `PUR-028`). `IC-A-003`
is the serious one and it was *visible in the material this unit read*.

## 14. Public copy

**None drafted.** Method step 14 draws public copy from accepted claims, and
the accepted claims here are mostly about what this repository cannot yet say.
The two that would carry a page — that the Rigveda transmits two forms of
itself which disagree at nine tenths of its stanzas, and that the conventional
date is inferred rather than attested — are held until `HOLD-008` moves, because
a page built on them would need Arnold and Pāṇini in a way this session did not.


## 15. Repaired against adversarial review, 2026-09-09

An independent reviewer re-ran the script, re-derived every statistic and
cross-checked all 48 dependency rows. **All seventeen tables reproduced
byte-identical and no arithmetic error was found.** The findings were about what
the arithmetic was made to say. What changed:

| Row | Was | Is |
|---|---|---|
| `DA-002` | `VERIFIED`, "maṇḍala number is not a time axis … can be shown" | `PROVISIONAL`, a three-way disjunction; the exact *p* = 0.8651 is stated and the test is called underpowered |
| `DA-M-003` | ρ with no *p*, no interval, no power statement | ρ, exact permutation *p*, null 95 % range, and an explicit "no evidence for, not evidence against" |
| `A-2` | `NOT-ELIGIBLE` — "FAILS on the one instrument" | `CANNOT-GATE`. An instrument that cannot license the positive inference (`DA-003`) cannot license the exclusion either |
| `DA-M-006` | modal-stratum accuracy alone, with a reading attached, `VERIFIED` | measurement only, with Cramér's V = 0.5314, U = 0.2919, MI = 0.668 bits; the reading moved to `DA-016` as `PROVISIONAL` and now runs both ways |
| `DA-M-008` | 1,094 / 1,308 / 2,372 over 10,552 | the A5c population of existing stanzas, plus `DA-M-022` on the sixteen keys that name stanzas `strata.json` lacks |
| `DA-M-015` | 72.04 %, no normalisation caveat; "darśate me > darśata ime" | 72.04 % raw and 70.81 % normalised, 130 stanzas differing only in notation; the 1.2.1 instance corrected to `darśatemé > darśataimé` |
| `DA-M-018` | "about 9 % of the recited text", from a symmetric ratio | directional median 0.9298, i.e. about 7 %, with the padapāṭha noted as the longer string |
| `DA-M-021` / `SRC-117` | five registers, 15 rows in `rigveda-pur-family.csv`, filter unstated | six registers, 14 rows, and the `VERIFIED`-only filter named along with everything it excluded |
| `DA-005` | half of the 2021 sentence | the whole sentence, including "not substantial" |
| `DA-008` | also claimed the null does not touch Arnold's stratification | that exculpation withdrawn: the abstract says *any* of the proposed stratifications, and Arnold's is the canonical one |
| `DA-006`, `A-1` | Grassmann as the independent instrument | independence marked as **untested and untestable here** (`DEP-036`) |
| `DA-015` | claimed the dependency register was complete | states what the filter excluded; the register went from 48 rows to 60 |
| dependency register | 48 rows; 9 excused on a false statement about `SRC-026`; 5 on a criterion false of them; 2 whose column contradicted their own note | 60 rows, every misclassification corrected in place and stated as a correction |
| `BF-027`, `BF-028` | process claims about ordering that git cannot support | withdrawn; what is checkable is stated instead |
| — | — | `BF-029`, `BF-030`, `IC-A-001`…`IC-A-004`, `DEP-036`, `DA-016`, `DA-017`, `DA-M-022`…`DA-M-024`, `RA-025`…`RA-028` opened |

**Three findings the reviewer raised that are recorded rather than repaired**,
because repairing them means changing another unit's registers: `IC-A-003`
(`SRC-026`), `IC-A-004` (`PUR-028` duplicating `A-1`), and `RA-028` (the
`supports_page` value resolves to no brief). The re-audit rows say who decides.

The reviewer also confirmed, and it is recorded here because a negative result
from an adversary is evidence: no bug in the Yates χ², the Jaccard, the Spearman
ρ (176 of 990 pairs hand-checked), the enrichment ratios or the modal-stratum
accuracy; `autojunk` does not bite; `DA-M-007`'s two mixed stanzas are right; no
`01-INHERITED/` material is cited as evidence anywhere in the unit; and `A-1`'s
refusal to gate on abstracts is the right call.
