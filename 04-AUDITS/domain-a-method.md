# Domain A — method note, 2026-09-07

Rigvedic chronology and transmission. What was bounded, what was measured,
what was got wrong on the way, and how both adversarial tests came out.

---

## 1. What the unit was for

`DEP-001` already recorded that every chronological claim in this repository
reads through Arnold's metrical strata, and that VedaWeb's `strata.json` and
Arnold 1905 are one source rather than two. `PUR-026` carried the consequence
in its own note: *"No second, independent stratification instrument was
applied."*

The unit was commissioned to **examine that dependency rather than use it**.
So the question was not "what does Arnold say about the Rigveda" but "is any
instrument of Rigvedic relative chronology retrievable here that is not
Arnold, and what happens when it is applied to the same text".

## 2. Step 2 — the dates, kept apart

Constitution §5.2 requires composition, attestation, copying, redaction,
translation, excavation, publication and modern interpretation to be treated
as different dates. For domain A they are:

| Date | What it is | Standing here |
|---|---|---|
| Composition | when the hymns were made | not established by anything in this unit |
| Redaction | the arrangement of hymns into books | `RCI-010` measures its principle, not its date |
| Recitational fixing | when the Saṃhitā text's sandhi was fixed | `RCT-002` measures the gap it left, not when it opened |
| Padapāṭha analysis | the word-by-word analysis | `RCT-003` measures its behaviour |
| Manuscript copying | surviving manuscripts | out of scope; none consulted |
| Editing | Aufrecht; Lubotsky; van Nooten & Holland 1994 | `SRC-105`–`SRC-107` |
| Digitisation and annotation | Gunkel, Ryan, Scarlata, Kölligan, Zürich, 2020 | `SRC-019`, `SRC-023`, `SRC-090`, `SRC-092` |
| Modern interpretation | Grassmann 1876 → Witzel 1995 → Hellwig 2020/2021 | the instruments themselves |

Nothing in this unit dates the composition of anything. Every result is a
statement about **relative** position, or about the relation between two
modern instruments. That restriction is not modesty; it is what the evidence
retrieved can carry.

## 3. Step 4 — evidence classes, kept apart

Five classes were touched and none is allowed to borrow certainty from
another:

- **Textual**: four transmissions of the same poems — the Saṃhitā, the
  Padapāṭha, Lubotsky's concordance and van Nooten and Holland's restored
  text (`RCT-001`, `RCT-011`, `RCT-012`).
- **Metrical**: Arnold's strata; van Nooten and Holland's restoration.
- **Morphological**: the Zürich token layer (`RCT-006`, `RCT-007`).
- **Grammatical-tradition**: Pāṇini's Vedic-scope rules (`RCT-008`).
- **Historiographical**: five scholars' late-addition judgements, 1876 to
  1995 (`RCI-001`–`RCI-012`).

The last of these is the one worth naming carefully. A scholar's judgement
that a stanza is a late addition is **not** an evidence class about the
Rigveda. It is a datum about the history of the discipline that happens to
be correlated with the text. It is used here as an instrument, which is
legitimate, and it is never counted as textual evidence, which would not be.

## 4. What was got wrong, and how it was caught

The first pass at the transmission measurement paired `lubotsky.csv` against
`vnh.csv`, treating the first as the transmitted Saṃhitā. It is not: it is
Lubotsky's **word concordance**, with sandhi undone. RV 1.1.2c reads there
`sá devā́n ā́ ihá vakṣati` where the Saṃhitā has `sá devā́m̐ éhá vakṣati`.

The error produced a plausible-looking table — 79.8% canonical rising to
97.0%, *as then computed, before the counter itself was corrected under
`BF-023`* — that would have been reported as "restoration repairs the
transmitted text" when what it actually showed was two different operations
on a third text.

It was caught by looking at the cases that ran the wrong way. 3,333 pādas —
again, as then computed — came out **shorter** after "restoration". A result
that clean should not have 8.4% of its cases pointing backwards, and
inspecting eight of them showed the concordance splitting sandhi rather than
the restoration undoing it. The measurement was rebuilt on Aufrecht at stanza level, where the
segmentations align.

Recorded because it is the general case: *the anomalous minority is where an
instrument tells you what it actually is.* The number that survived,
`RCT-003`, says something true and much narrower — undoing sandhi word by
word is not the same operation as restoring metre, and does not achieve it.

### 4b. The same lesson, not applied, and what it cost

The figures in the paragraph above were themselves wrong when first
committed, and for a reason the paragraph above had already named.

The van Nooten and Holland text writes long vocalic **r̥̄** as the digraph
`r̥r̥` — `mr̥r̥ḷaya`, `jaritr̥r̥ṇáam` — where Aufrecht writes `mr̥ḷaya`. The
syllable counter read it as two nuclei. 273 pādas carry it; 125 of them came
out non-canonical for that reason alone. Every total in `RCT-001`, `RCT-002`,
`RCT-003`, `RCT-011` and `RCT-012` was wrong, and `RCT-004`'s statistics
shifted with them.

The failure is not the bug. It is that §4's own lesson was available and was
not used. The corrected measurement produced **1,200 non-canonical pādas in a
metrically restored edition**, and not one of them was inspected. One
orthographic digraph accounted for a tenth of them. The unit wrote down "the
anomalous minority is where an instrument tells you what it actually is",
then published a second measurement without looking at its anomalous
minority.

The self-test made it worse rather than catching it. `RCT-001`'s locator
advertised "self-tested on RV 1.1.1–2, where every pāda must be 8" — and the
code asserted **two** pādas. No two-pāda assertion can catch a systematic
transliteration bug, and advertising one in a locator makes a register row
look tested when it is not. The test now asserts four hand-checked pādas
**and** the corpus residue: it fails if more than 5% of the restored text is
non-canonical, or if more than ten non-canonical pādas carry the digraph.
`BF-023`.

## 5. Negative-evidence typing

Constitution §6. Three absences were typed rather than argued from.

**The five-scholar layer records positive marks only.** A stanza with no mark
is not thereby judged early by any of the five. Grassmann marked 1,094
stanzas; the other 9,458 are not 9,458 stanzas he called old. Typing:
`NOT PRODUCED` — a judgement of that form was never made in a recordable
way, because these scholars were identifying additions, not classifying the
whole corpus. Every measurement in `RCI-004`–`RCI-011` is therefore built on
marked-versus-unmarked as an *asymmetric* comparison, and no claim reads an
unmarked stanza as positively early.

**Arnold 1905, Oldenberg 1888 and the 2021 reassessment were not read.**
Typing: `NOT ACCESSIBLE`, all three. `HOLD-009`, `HOLD-010`, `HOLD-011`. All
three texts exist, two are out of copyright and digitised, and one has an
open-access copy in an institutional repository. The blockage is an egress
policy in this session, not a gap in the historical record, and it must never
be written up as one.

**No structural zero in the book × stratum table is a fact about the
Rigveda.** Book 3 has no Archaic stanza and book 4 no Cretic (`RCI-005`).
That is not an absence in the text; it is a consequence of Arnold assigning
periods at hymn level, with 93.2% of hymns carrying a single code. Typing:
`NOT PRODUCED`, by the instrument, not by the poets.

## 6. Prestige-bias challenge

*Did this privilege a claim because it is canonical, Sanskritic, Brahmanical,
Indo-European, European, colonial, institutionally prestigious, repeatedly
cited or nationally useful?*

**Partly, and the correction is in the register rather than in this note.**

The instruments used here are five European philologists, four of them
nineteenth- or early-twentieth-century German, publishing 1876 to 1928, plus
Witzel 1995 and a Zürich computational group. That is the entire evidence
base of `RCI-001`–`RCI-012`. It is not a neutral sample of who has studied
the Rigveda; it is the sample that a German-philological tradition digitised
and that a European digital-humanities project encoded. No Indian
commentarial tradition on the internal chronology of the Rigveda was
consulted, and none is present in the retrieved data. Sāyaṇa is not in
`stanza_properties.json`; neither is any Indian scholarship after 1947.

Two specific corrections were made:

1. **The agreement of five European scholars was not allowed to count as
   five measurements.** `RCI-009` measures the pairwise agreement and finds
   Wüst and Oldenberg at Jaccard 0.836 — effectively one instrument
   (`DEP-030`). The count of instruments independent *in authorship* is
   three, not five. That is a different count from the one §7 point 3 gives:
   only **two** of the three survive stratification by book (`RCI-008`), and
   only **one** of those two, Oldenberg, also precedes Arnold 1905
   (`RCI-012`). Three, two and one are three different questions —
   authorship, statistical survival, and priority in date — and no claim
   should quote one number for another.
2. **Arnold's own second work was not allowed to corroborate his first.**
   The `arnold` column of the layer is Arnold 1897 and `strata.json` is
   Arnold 1905 (`RCI-003`, `DEP-028`). Its enrichment of ×6.75 is the highest
   of the five and is reported as the **same-author ceiling** against which
   the others are read, never as evidence.

What could not be corrected: the archive itself. There is no counterpart
layer of Indian scholarly judgement in machine-readable form to test these
against, and this session could not go looking for one, because every
non-GitHub host was refused. That is `BF-021`.

## 7. Preferred-counter-narrative challenge

*Did this accept a claim too easily because it is Dravidian, Indigenous,
anti-colonial, anti-Brahmanical, subaltern, diffusionist or politically
corrective?*

**The live risk here was the opposite shape, and it was the more dangerous
one: accepting a debunking too easily.**

The 2021 reassessment is the kind of result this repository is disposed to
like. It is recent, it is quantitative, it uses proper controls, and it cuts
against a canonical nineteenth-century scheme that a colonial-era philologist
built. The tempting move was to write "Arnold's strata do not survive modern
statistical testing" and to treat `PUR-026` as thereby dissolved.

That would have been wrong in three ways, and each was corrected:

1. **The abstract does not say that.** It says the allomorph distributions
   *do not lend significant support* to the proposed stratifications, under
   controls, and that a cluster analysis *still favours* book 10 occupying a
   special position. Failure to find support in one class of evidence is not
   refutation of the thing.
2. **The reproduction confirms the narrow result, not the wide one.**
   `RCT-006` reproduces the pattern on one allomorph pair from this
   repository's own extraction — position beats stratum, p = 4.9e-37 against
   p = 0.353. `RCT-007` then shows the aggregate null is two opposing effects
   cancelling, which is a stronger caution against uncontrolled allomorph
   counts *in either direction*, including a debunking one.
3. **Other instruments do separate the strata, though less than this section
   first claimed.** Metrical restoration rate separates Archaic from the rest
   and Strophic behind it, at Mann-Whitney p = 5.3e-12 and p = 2.9e-10, and
   leaves Cretic, Normal and Popular indistinguishable at p = 0.237
   (`RCT-004`). Two author-independent late-addition instruments concentrate
   in Popular with book identity controlled, not three (`RCI-008`). A reading
   that took the 2021 abstract as dissolving Rigvedic relative chronology
   would still have had to suppress both.

**And this passage is itself the sharpest instance of what it is about.**
Every clause of point 3 was withdrawn elsewhere in the repair pass and
survived here for a further commit: the claim of an Archaic-to-Popular
*ordering* (withdrawn, finding F), the p-value 6.5e-44 (withdrawn, finding
B), the count of *three* instruments (withdrawn, finding G — Grassmann fails
the within-book control), and *the book-10 effect controlled out* (withdrawn,
finding G — that was the wrong control). Four withdrawn claims, all four
running in the direction this section exists to guard against, sitting inside
the guard.

Two distinct failures are tangled here and they should be separated, because
filing the second under the first is a mild instance of the thing this
section guards against.

The **bias** limb is that all four withdrawn claims ran in the direction this
section exists to resist, and that a passage recording what the unit resisted
was the last place they survived. That belongs here.

The **process** limb is that corrections were made where the review pointed —
in the register rows — and the prose *derived* from those rows was not swept.
A withdrawn number does not stay in one file. That is not bias; it is an
incomplete edit, and it belongs to `BF-026`, which owns it.

The sweep is now a step and a tool: `04-AUDITS/figure-sweep.py` builds the
set of live figures from what the scripts actually emit, rather than from
what someone remembered to look for. A hand-written list failed twice, the
second time missing two numbers in the paragraph below this one.

**What that tool does not do has to be stated here, because a guarantee
advertised wider than it is would be exactly the failure `BF-020` logs.** It
answers "does any script emit this token anywhere". It cannot answer "does
the script this locator names emit this figure *in this role*", because
nothing in it reads locators. The two withdrawn odds ratios in the paragraph
below — 15.4 and 3.63 — are both still emitted, on the group-label rows of
`m8b` that `RCI-011` abandoned, so **the tool would not have caught the
failure it was written for.** It catches figures no script emits at all. A
figure it passes is not thereby current, and the fourth adversarial review is
what established that; an earlier draft of this paragraph claimed more.

`RCT-010` is where this lands, and it is PROVISIONAL, not VERIFIED, because
the paper itself is on `HOLD-011`.

**The fourth correction is the one the unit did not make for itself.** The
adversarial review found it: the paragraph of Hellwig 2020 §5.4 that supplied
the appendix list and the "most frequently cited" quotation continues, in the
same breath, with a caution against exactly the control `RCI-008` presents as
strongest:

> "this strong effect is mainly caused by a few of Oldenberg's appendices
> marked as especially young by the model … The remaining appendices, esp.
> those contained in the Family Books R̥V 2-7, are **not** marked as
> particularly late by the model, but some of them even as quite old as, for
> example, the 'praise of giving' in R̥V 5.27, whose status as an appendix
> has been challenged by Jamison and Brereton (2014, 688) on metrical
> grounds."

`RCI-008` reports the family books 2–7 as the tightest form of the control.
The source it draws on says its own model finds the family-book portion of
that same list *not* late, and one member's appendix status contested. The
favourable half of one paragraph was quoted and the unfavourable half of the
same paragraph was not recorded. Footnote 5 of the same paper adds "*note
that significant p-values can result from the mere sample sizes in this
setting*", while `RCI-008` reported `p = 0` and `p = 4.6e-300`.

This is asymmetric scrutiny of a single source, applied in the direction that
helped, and it is logged as `BF-024`. Both quotations are now in the
`RCI-007` and `RCI-008` notes.

The next correction under this heading is smaller and concerns Oldenberg.
`RCI-011` looks like strong corroboration — rule-breaking hymns are marked
late at odds ratio 19.8 by Oldenberg. That number is **definitionally
inflated**: violating the arrangement rule is *how Oldenberg identified
appendices*. It is in the output file and is explicitly barred from being
cited as corroboration. The figure that carries the claim is Grassmann's odds
ratio of 3.58, because Grassmann published twelve years before Oldenberg
formulated the rule.

Those two numbers were 15.4 and 3.63 until the third repair pass. They are
the group-label figures `RCI-011` abandoned when it moved to the label-free
segmentation, and they sat five paragraphs below the passage that names the
tree-wide sweep as a new step, because a hand-written list of withdrawn
values cannot contain the values nobody thought of. That is why the sweep is
now `04-AUDITS/figure-sweep.py`, which derives the list from what the scripts
actually emit instead. Run against this file it flags both of them, and it
flagged the two in §4 above.

## 8. Step 11 — current standing

- **Arnold 1905's periodisation**: historically influential, still in
  working use as a chronological label in the journal literature as recently
  as 2018 (`SRC-100`, TPS 12141, "late, Popular Rigveda"), and under active
  quantitative challenge (`SRC-099`). Arnold himself called the period names
  provisional (1905 §§60–61, per `PUR-026`).
- **Oldenberg's arrangement rule**: "still among the most frequently cited
  studies on the textual history of the R̥V" (Hellwig 2020 §5.4). Tested
  here and confirmed against the corpus (`RCI-010`).
- **Wüst 1928**: Hellwig 2020 §5.3 records that it "did not meet enthusiastic
  support in Vedic studies". `RCI-009` supplies a mechanical reason to be
  careful with it in this data: its marks are nearly Oldenberg's.
- **The (1–9)(10) split**: "the most widely accepted stratification"
  (Hellwig 2020 §5.4), confirmed by his own model, and consistent with
  everything measured here.

## 9. Step 12 — what would change the conclusions

Constitution step 12 asks this of every accepted claim, and the first version
of this note answered it for 7 of 24. All 26 are below. Falsifiers that
several rows share are stated once and referenced.

**F-1, the transliteration falsifier.** Any pāda where the syllable counter
disagrees with a hand count on a string it has not been shown to handle.
`BF-023` is what happens when this is not looked for. Applies to `RCT-001`,
`RCT-002`, `RCT-003`, `RCT-004`, `RCT-011`, `RCT-012`.

**F-2, the Arnold-provenance falsifier.** Arnold 1905's own account of how he
assigned the Popular period, if it shows he used Grassmann's or Oldenberg's
judgements as input. `HOLD-009`. Applies to `RCI-006`, `RCI-007`, `RCI-008`,
`RCI-012`, and through them to the `PUR-026` supersession.

**F-3, the edition falsifier.** A critical edition of the Aṣṭādhyāyī, or of
the Padapāṭha, giving different counts. Applies to `RCT-008`, `RCT-009`,
`RCT-011`, `RCT-012`.

| Claim | What would change it |
|---|---|
| `RCI-001` | A VedaWeb release altering `stanza_properties.json`. The 2,350 figure is checkable in one line and was wrong once already. |
| `RCI-002` | A VedaWeb statement of the code semantics that differs from `lateAdditions.md` — the platform page, when reachable, is the obvious check. |
| `RCI-003` | Evidence that the `arnold` column is not Arnold 1897 but a later redaction of it. |
| `RCI-004` | A metre-label grouping finer or coarser than the 66 in `strata.json` that raises prediction well above 40.4%. If metre did determine stratum, every result reading through the strata would be a result about metre. |
| `RCI-005` | Nothing likely; it is a cross-tabulation of a fixed file. It would be *reinterpreted* by evidence that Arnold assigned periods at book level rather than hymn level. |
| `RCI-006` | F-2. Also a sixth instrument, independent of all five, that does *not* concentrate in Popular. |
| `RCI-007` | Oldenberg 1888 itself (`HOLD-010`), showing either that Hellwig's 31 are not his, or that the further 52 hymns in VedaWeb's column are not. |
| `RCI-008` | F-2. Also: any book-level variable correlated with both marking and Popular that book-stratification does not absorb — hymn length is the obvious candidate and was not tested. |
| `RCI-009` | Wüst 1928 itself, showing that his book differs from the marks attributed to him here. The Jaccard of 0.836 is a fact about the VedaWeb column, not necessarily about Wüst. |
| `RCI-010` | A demonstration that hymn *length* is not what the arrangement tracks — that the descending runs follow something else that correlates with length. The whole-book test cannot separate those. |
| `RCI-011` | Evidence that Grassmann 1876–7 had access to an arrangement principle equivalent to Oldenberg's. The claim rests entirely on his priority in date. |
| `RCI-012` | F-2, decisively. This row exists to be settled by it. |
| `RCT-001` | F-1. |
| `RCT-002` | F-1. Also a demonstration that van Nooten and Holland's pāda segmentation *does* encode a metrical judgement about junction sandhi, which would move part of the +2.43% back into the metrical column. |
| `RCT-003` | F-1. Also a canonical-length inventory wider than {8, 11, 12} — the 2.7% residue is not analysed here. |
| `RCT-004` | F-1. Also: any variable that predicts restoration rate and is correlated with stratum and is neither metre label nor book. Both of those were controlled; a third was not looked for. |
| `RCT-005` | van Nooten and Holland 1994 in its own text, showing whether Arnold's periodisation was an input to their restoration. |
| `RCT-006` | A second allomorph pair behaving differently, or the same pair at full corpus scale with the other case-forms Hellwig, Scarlata and Widmer used. The stratum null has 89 tokens in its smallest cell and would not detect a small effect. |
| `RCT-007` | More data, straightforwardly. The non-final limb does not survive multiplicity correction and either direction could be noise. |
| `RCT-008` | F-3. Also a reading of *chandas* in Pāṇini's usage that reclassifies some of the 17 rules about the word, in either direction. |
| `RCT-009` | The translation audit `RCT-009` itself says has not been done. Constitution §7 makes that audit prerequisite to the *count*, not only to its interpretation. |
| `RCT-010` | The 2021 paper's own scope statement (`HOLD-011`), which is what should govern this row and does not yet. |
| `RCT-011` | F-1, F-3. Also a reading of the 61 divergent-but-intact stanzas showing them defective after all, which would move the figure up. |
| `RCT-012` | F-1, F-3. |
| `IC-A-001`, `IC-A-002` | A source for the site's date range, or a resolution of book 8's position. Neither is available here. |
| `IC-A-003` | Oldenberg 1888, Wüst 1928 or Witzel 1995 turning out to have judged RV 10.90 late somewhere the VedaWeb layer does not record. |
| `IC-A-004` | F-3. |

### R-02 in the inherited non-repetition record

`01-INHERITED/claude-project-handoff.md` §5.4 records `R-02` as REJECTED:
*"The corpus knows Afghanistan before it knows the Ganges" (Archaic-stratum
reading)*, on the ground of a by-book count placing the Afghan rivers in
books 5, 8 and 10.

`RCT-004` raises the standing of Archaic-stratum readings in general, and the
question has to be faced rather than left implicit: **does it revive `R-02`?
It does not, and it cannot.** `R-02` was rejected on *geography*, by a
by-book river count. `RCT-004` measures how much obscured metrical material a
stratum carries. It says nothing about which rivers appear where, and the
strata are in any case entangled with book identity at Cramér's V 0.471
(`RCI-005`), so an Archaic-stratum reading of a by-book distribution is
close to the circularity `R-02` was rejected for. Nothing in this unit
licenses re-proposing it.

## 10. Step 13 — MelaKeela's own pages

`melakeela/site` was attachable, so this step ran. It was checked at
`769a6f6`. Two failures and two passes, all four in
`04-AUDITS/INTERNAL-CONTRADICTIONS.csv`.

**`IC-A-001`.** `the-late-hymn.html` says "Books 1, 8, 9 and 10 are later."
Book 8 is the most contested book in the corpus and the page states it flat.
Hellwig 2020 §5.4 reports his model inducing the ordering
(4, 8) < (1–3, 5–7, 9) < (10) — books 4 and 8 as the **earliest** — notes
that this was already proposed for book 8 by Lanman 1872 and Arnold 1897 and
strongly contested by Hopkins 1896, and says outright that the status of RV 1
and especially RV 8 is disputed. This repository's own data shows the same
fault line: Witzel marks 11.3% of book 8 late, his highest rate for any book,
while Oldenberg marks 1.3% and Wüst 1.5%, their lowest; and Arnold 1905 makes
book 8 43.4% Archaic against 3.8% Popular. `RA-020`.

**`IC-A-002`.** The same page carries "composed centuries before the rest"
and "family books c. 1500–1000 BCE; Books 1/8/9/10 later", attributed to
"standard chronology" with no source. Nothing in this unit dates the
composition of anything — §2 above is the first restriction the method note
states — and Hellwig's model finds "no clear temporal separations between the
remaining nine books". The page's argument is about relative order and does
not need the numerals. `RA-020`.

**`IC-A-003`, a pass, and an upgrade the page can take.** Its central claim —
RV 10.90 sits in the newest book and reads as inserted — is supported by
three retrieved primary instruments, where the page currently rests it on
three secondary sources it honestly marks "source listed, not accessed". All
64 pādas of RV 10.90 carry Arnold 1905's Popular stratum **in uppercase**,
which per `PUR-011` means not by metrical variations alone. Grassmann 1876–7
marks all 16 stanzas. Arnold 1897 marks all 16 as `C2`, the later of his two
addition phases. Two of those three predate Arnold 1905.

And the scope has to be kept honest in the same breath: Oldenberg, Wüst and
Witzel mark **none** of the hymn. Under §5's typing that is `NOT PRODUCED`
and is not disagreement — but it is not agreement either, and the page must
not be given three instruments where it has three silences and two marks.
`RA-021`.

**`IC-A-004`, a second pass.** `panini.html` says "roughly 4,000 sūtras" and
that Pāṇini "distinguishes chandas, the Vedic, from bhāṣā, the spoken
language — and describes both". The retrieved edition has 3,983, and
`RCT-008` puts a proportion under the qualitative claim: 6.35% in explicitly
Vedic scope. Nothing to correct.

No public copy was drafted from this unit. `RCT-010` and `RCI-012`, the two
claims a reader would most want, are both PROVISIONAL and both sit behind
holds.

## 11. Reproducing this

```
python3 04-AUDITS/rv-token-extract.py           <vedaweb>/rigveda/TEI rv_tokens.tsv
python3 04-AUDITS/rv-chronology-instruments.py  <vedaweb>/rigveda rv_tokens.tsv <out>
python3 04-AUDITS/rv-arrangement.py             <vedaweb>/rigveda <out>
python3 04-AUDITS/rv-metrical-restoration.py    <vedaweb>/rigveda <out>
python3 04-AUDITS/rv-registers-and-panini.py    <ashtadhyayi>/sutraani/data.txt rv_tokens.tsv <out>
```

Then, before committing anything derived from them:

```
python3 04-AUDITS/figure-sweep.py <out>
python3 04-AUDITS/validate-registers.py
```

`<vedaweb>` is `VedaWebProject/vedaweb-data` at `d3eb8af`, `<ashtadhyayi>` is
`ashtadhyayi-com/data` at `24109f7`. Outputs are in
`04-AUDITS/domain-a-outputs/`. The Monte Carlo in `rv-arrangement.py` is
seeded at 20260907 and is deterministic. `scipy` is the only non-stdlib
dependency.


---

## 12. The adversarial review, and what it changed

The review ran on `bb61d65` and reported against a tree that had moved twice
under it. It is recorded here in full effect because a review that finds
nothing is worth nothing, and this one found a great deal.

**Nineteen findings. Two rows downgraded in substance, eleven renumbered or
reworded, none withdrawn.** The four that changed what this unit can claim:

1. **The syllable counter was wrong** on a digraph the restored text uses,
   and five VERIFIED rows carried wrong totals. `BF-023`. The conclusions
   survived; the numbers did not.
2. **`RCI-008`'s control was the wrong control.** Deleting book 10 does not
   control for a confound that runs through every book. Under the control
   that does — stratification by book — **Grassmann falls from an odds ratio
   of 15.3 to 4.0**, and Grassmann is the instrument `RCI-011` and `RCI-012`
   lean on as incapable of being downstream of Arnold. `RCI-012` was weakened
   accordingly: it now rests on one pre-Arnold instrument, Oldenberg, not two.
3. **`RCI-010` tested a rule its source does not state.** Hellwig 2020 states
   the arrangement rule *per book*; the unit tested it within groups, and
   called them deity groups when VedaWeb's field is a poet heading. Retested
   as stated, it holds — 388 descents against 214 ascents — but the first
   version's locator did not cover the test it described.
4. **The source was read asymmetrically.** `BF-024`. The favourable half of
   one paragraph of Hellwig 2020 was quoted; the half warning that his model
   finds the family-book appendices *not* late — the region `RCI-008`
   presents as its tightest control — was not.

The pattern across all four is one thing: **the unit checked the results it
expected to be attacked and did not check the ones it expected to hold.**
`RCT-004` and `RCT-006`, the two results most likely to draw fire, had been
given genuine controls before review. `RCI-008` and the syllable counter,
which felt settled, had not.

### The `future_control` checklist

`BF-025` records that three controls already in `04-AUDITS/BIAS-FAILURE-LOG.csv`
were breached by this unit, and each would have caught a defect the review
then found. The column is decorative unless something reads it. This unit's
controls, checked:

| Control | Source | State |
|---|---|---|
| A unit's statement of its inputs is checked against the code, in the same pass as its counts | `BF-020` | **Breached three times.** `RCI-005`, `RCT-001`, `RCT-011`. All repaired. |
| No leave-one-out statistic without the per-element influence of every element | `BF-005` | **Breached** by `RCI-008`. `m6c-per-book-odds-ratios.tsv` now carries every element. |
| A null reports the point estimate, its direction, and the power limitation | `BF-004` | **Breached** by `RCT-006`. Smallest stratum n = 89, now stated. |
| Report the measurement that cuts against the working hypothesis in register-row format | `BF-011` | Held. `RCI-009` and the `RCT-004` medians are register rows, not prose. |
| Where a control variable has a large effect, stratify by it before reporting the null | `BF-022`, written by this unit | **Breached by this unit in the same commit that wrote it**, at `RCI-008`. |
| After any figure is withdrawn, run `04-AUDITS/figure-sweep.py` before the commit that withdraws it | `BF-026`, written by this unit | **Breached twice by the repair passes that wrote it**, which is why it is now a tool rather than a hand list. |
| For any new counting rule, print the census of what it is actually counting before a number leaves the script | `BF-023`, `BF-026` | **Breached** by all three versions of the R1b junction test. The census is now printed. |
| A correction is not made until the diff shows it | `BF-026` | **Breached.** A correction to the `SRC-090` ledger note was reported to the owner and to the reviewer and had not been made. |

A future domain-A unit runs this table before its registers are committed,
not after.