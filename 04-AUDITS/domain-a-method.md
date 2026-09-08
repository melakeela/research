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

- **Textual**: three editions of the same poems (`RCT-001`).
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
97.0% — that would have been reported as "restoration repairs the
transmitted text" when what it actually showed was two different operations
on a third text.

It was caught by looking at the cases that ran the wrong way. 3,333 pādas
came out **shorter** after "restoration". A result that clean should not
have 8.4% of its cases pointing backwards, and inspecting eight of them
showed the concordance splitting sandhi rather than the restoration undoing
it. The measurement was rebuilt on Aufrecht at stanza level, where the
segmentations align.

Recorded because it is the general case: *the anomalous minority is where an
instrument tells you what it actually is.* The number that survived,
`RCT-003`, is the same 79.8% against 97.0%, but it now says something true
and much narrower — undoing sandhi word by word is not the same operation as
restoring metre, and does not achieve it.

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
   (`DEP-030`). The count of author-independent instruments in every claim is
   three, not five.
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
   repository's own extraction — position beats stratum, p = 8.9e-44 against
   p = 0.474. `RCT-007` then shows the aggregate null is two opposing effects
   cancelling, which is a stronger caution against uncontrolled allomorph
   counts *in either direction*, including a debunking one.
3. **Other instruments do separate the strata.** Metrical restoration rate
   orders them Archaic → Popular at p = 6.5e-44 (`RCT-004`), and three
   author-independent late-addition instruments concentrate in Popular with
   the book-10 effect controlled out (`RCI-008`). A reading that took the
   2021 abstract as dissolving Rigvedic relative chronology would have had
   to suppress both.

`RCT-010` is where this lands, and it is PROVISIONAL, not VERIFIED, because
the paper itself is on `HOLD-011`.

The second correction under this heading is smaller and concerns Oldenberg.
`RCI-011` looks like strong corroboration — rule-breaking hymns are marked
late at odds ratio 15.4 by Oldenberg. That number is **definitionally
inflated**: violating the arrangement rule is *how Oldenberg identified
appendices*. It is in the output file and is explicitly barred from being
cited as corroboration. The figure that carries the claim is Grassmann's odds
ratio of 3.63, because Grassmann published twelve years before Oldenberg
formulated the rule.

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

- **`RCI-006`, `RCI-008`, `RCI-012`** would move toward REJECTED as claims of
  *corroboration* if Arnold 1905 turns out to have used Grassmann's and
  Oldenberg's judgements in assigning his Popular period. `HOLD-009` names
  the page range that would settle it. The measurements would survive
  unchanged as descriptions of how the layers relate.
- **`RCT-004`** would weaken if van Nooten and Holland's restoration turns
  out to have used Arnold's periodisation as an input. `RCT-005` holds that
  open.
- **`RCT-010`** would change on any reading of the 2021 paper's own scope
  statement that is wider than its abstract (`HOLD-011`).
- **`RCI-010`** would be overturned by a demonstration that VedaWeb's
  addressee strings encode a grouping derived from Oldenberg. The
  label-free segmentation was run precisely to survive that, and it does:
  216 descents against 56 ascents using maximal runs of identical addressee
  string, with no group label involved.
- **`RCT-008`** would move on a critical edition of the Aṣṭādhyāyī giving a
  different sūtra count or a different anuvṛtti reconstruction.

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

`<vedaweb>` is `VedaWebProject/vedaweb-data` at `d3eb8af`, `<ashtadhyayi>` is
`ashtadhyayi-com/data` at `24109f7`. Outputs are in
`04-AUDITS/domain-a-outputs/`. The Monte Carlo in `rv-arrangement.py` is
seeded at 20260907 and is deterministic. `scipy` is the only non-stdlib
dependency.
