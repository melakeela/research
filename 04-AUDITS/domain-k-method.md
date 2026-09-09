# Domain K — Indus writing and institutional discontinuity

**Unit of work:** 2026-09-09
**Registers:** `03-REGISTERS/domain-k-indus-measurements.csv` (26 rows),
`domain-k-indus-signs.csv` (397 sign classes),
`domain-k-rigveda-lexicon.csv` (15 rows),
`domain-k-rigveda-writing-candidates.csv` (63 lookups),
`domain-k-rigveda-marking-occurrences.csv` (232 occurrences),
`domain-k-absences.csv` (13 typed absences),
`domain-k-hypothesis-eligibility.csv` (11 gated hypotheses)
**Sources:** `SRC-099`–`SRC-116`  **Dependencies:** `DEP-029`–`DEP-033`
**Hold:** `HOLD-008`  **Method failure:** `BF-027`
**Re-audits:** `RA-022`–`RA-025`  **Contradictions:** `IC-K-001`–`IC-K-005`
**Reproduce:** `04-AUDITS/domain-k-indus-corpus.py`, then
`rv-token-extract.py`, `rv-writing-lexicon-scan.py`,
`rv-marking-occurrences.py`

---

## 1. What this unit is, and what it is not

§4.K asks twelve things. This unit could reach evidence on three of them
— the absence of an unambiguous Rigvedic description of Indus writing,
whether relevant terminology may be unrecognised, and (partly) durability
— and could reach no evidence at all on seals as an object class,
sealings, tablets, proposed functions, distribution, post-urban survival,
whether the script had become unreadable, or institutional rupture.

The split is not a judgement about which questions matter. It is the
egress boundary. The Rigveda is on GitHub; the Indus corpus is in print
volumes, on `archive.org`, at `asi.nic.in` and behind `nature.com`, and
all of those are refused (`SRC-099`, `SRC-109`–`SRC-114`).

So this unit is: a full measurement of the Rigvedic half, a bounded
measurement of one small derivative of the Indus corpus, thirteen typed
absences, eleven gated hypotheses, and a hold. It is not an account of
Indus writing, and it does not compare the two bodies of evidence. The
comparison §4.K asks for — Indus technologies against the early Rigvedic
archive — is not attempted, because one side of it has no measurements.

## 2. The retrieval picture

Reachable on 2026-09-09: the git proxy's anonymous lane for public GitHub
repositories, and `raw.githubusercontent.com`. That reached three Indus
datasets and the VedaWeb Rigveda.

Refused: sixteen scholarly and archival hosts, on `curl` and on `WebFetch`
alike; the GitHub REST API for anything outside this session's own
repositories, which is a narrowing since `SRC-057` and meant repository
names had to be found by WebSearch and then fetched by git; and every
literature connector.

The four named targets of the task were all probed and the outcome logged
either way: Mahadevan's concordance refused (`SRC-109`), the Wells sign
list refused (`SRC-110`), ASI excavation reports refused (`SRC-111`), and
a machine-readable sign corpus on GitHub **retrieved** (`SRC-102`,
`SRC-103`).

## 3. The Indus side

`mayig/indus-valley-script-corpus` @ `ad2f1e2` is one annotator's
work-in-progress digitization of CISI. What it contains, exactly:

| | |
|---|---|
| objects | 179, one side each, CISI M-1 to M-184, five numbers missing |
| site | Mohenjo-daro, all of them |
| object class | unicorn seals, all of them, in five sub-types |
| graphemes | 1,003, of which 19 are the damage placeholder P000 |
| sign tokens | 984, in 181 classes, 77 of them hapax |
| length | 1 to 13 signs, median 5, mean 5.50 |
| lines | 990 graphemes on line 1, 13 on line 2 |
| fields per record | three: id, description, graphemes |

Every one of those numbers is a property of the file set. The last row is
the one that governs the rest: there is no find-spot, no stratum, no
date, no material, no dimension and no museum number anywhere in it
(`DK-M-016`). That is why §4.K's distribution and function questions have
no measurement rows in this unit rather than weak ones.

**The crosswalk is the one genuinely new measurement.** The 397 sign
entries carry, for each class, the Parpola V-numbers, Wells W-numbers and
Mahadevan M-numbers the annotator folded into it. Counted:

| System | Distinct numbers | Classes taking >1 | Largest fold | Classes taking none |
|---|---|---|---|---|
| Parpola V | 662 | 195 | 7 | 1 |
| Wells W | 498 | 76 | 17 | 66 |
| Mahadevan M | 359 | 29 | 5 | 63 |

Thirteen Mahadevan numbers appear under more than one Parpola class,
which makes the crosswalk not a function at those points. The
interpretive consequence is held to one line and one register row
(`DK-M-015`, `DK-A-011`): the number of Indus signs is a property of a
sign list and its allography rules. Four lists in one file disagree by a
factor of 1.8. Any argument that runs from inventory size to whether the
signs are writing inherits that.

The other two datasets carry nothing and are logged saying so.
`ramnerd/IVC_script_decoded` claims a complete decoding at 98.84%
correlation with Old Tamil over a 556-row file with no artefact
identifiers and no sign key (`DK-M-019`–`DK-M-021`).
`akksshhaay/Indus-Seal-Dataset` is 327 photographs and a spreadsheet
scraped from `harappa.com` captions that locates 38 of 135 objects even
to a site (`DK-M-022`–`DK-M-024`).

## 4. The Rigvedic side

Two searches, deliberately different in kind.

**Search A, a candidate census.** Twenty-two stems of the later Sanskrit
writing and sealing vocabulary are absent from the corpus's lemma
inventory: `likh`, `lekha`, `lipi`, `libi`, `grantha`, `pattra`,
`patra`, `pustaka`, `phalaka`, `masi`, `kalama`, `lekhaka`, `mudra`,
`aṅkana`, `cihna`, `lāñchana`, `lakṣman`, `lakṣaṇa`, `saṃkhyā`, `tulā`
and the roots `gaṇ-` and `paṇ-`. Positive controls return 543 tokens for
`gáv- ~ gó-`, 471 for `rátha-`, 83 for `púr-`. One control is kept in
its failing form in the output: querying `go` alone returns nothing,
because the Zurich lemma is an alternation — the lookup bug a census
without controls would have published as a finding.

**Search B, a gloss scan of the whole attested lexicon**, then
adjudicated hit by hit. 98.5% of tokens and 97.0% of lemmas carry a
Grassmann gloss.

| Field | True | False positive |
|---|---|---|
| WRITING | 0 | 5 |
| SEAL | 0 | 0 |
| MARK | 9 | 112 |
| INCISE | 1 | 12 |

The false positives are printed with reasons rather than deleted, because
substring matching is what makes the scan exhaustive and what makes it
noisy: German *ausgezeichnet* contains **zeichn**, *spritzen* contains
**ritz**, *Vorschrift* contains **schrift**, *bestrichen* contains
**strich**, *ackerbauend* contains **kerb**, and Grassmann's own
metalanguage — "Bezeichnung eines Volkes" — accounts for 90 hits by
itself.

**What the scan found that the census could not.** `√rikh-`, glossed
exactly *ritzen*, to scratch or incise. Twice, both in RV 6.53: Pūṣan
carrying an `ā́rā`, an awl, and scratching open the hearts of the
stingy. The statement "the root that later means *write* is absent from
the Rigveda" is therefore false, and a candidate list built from
Classical Sanskrit produces exactly that false statement (`DK-R-006`).

**What the corpus does with the words it has.** `akṣára-`, the word that
later names a written character, occurs eight times, and in all eight
both translators render a syllable of chanted speech or the imperishable
— the syllable that measures the metres at 1.164.24, the syllable of the
`r̥c` in the highest heaven at 1.164.39. `√takṣ-` fashions chariots,
hymns, bolts, cups and heaven; its one carving passage carves a
horse-post knob. `√piś-` decks the sky with stars and trims flesh on a
board. `ketú-` is a banner or a light. A keyword scan of both
translations across all 232 registered occurrences returns six stanzas
and not one of them is about writing.

And the corpus is not short of the language of obligation: `bhāgá-`
share 60, `r̥ṇá-` debt 10, `balí-` levy 4, `śulká-` price 2, `√mā-`
measure 90. What it lacks is the language of **recording** them.

## 5. The two adversarial tests

### Prestige-bias challenge

**Item 1, and it governs the unit.** Did this privilege the Sanskritic,
canonical, textual side because that is the side the network reached? Yes,
structurally, and no amount of care removes it. The Rigveda arrived as
164,758 morphologically annotated tokens with four translations; the
Indus material arrived as 179 seals with three fields. Fifteen Rigvedic
claim rows and 232 registered occurrences stand against an Indus side
that cannot state a find-spot.

The corrections applied: no comparative conclusion is drawn anywhere in
this unit; the asymmetry is stated in the manifest before any analysis
(`02-SOURCES/domain-k-manifest-2026-09-09.md` §3); it is audited as a
property of this record at `APA-K-004`; `HOLD-008` forbids the
comparison explicitly; and `RA-024` extends the question to every other
domain in the repository. What could not be corrected is the shape of the
evidence itself, and a reader should treat the Rigvedic half of this unit
as a well-measured half of a question, not as the answer.

**Item 2.** Did the unit privilege the administrative reading of the
seals because it is the familiar, institutionally comfortable one?
`DK-H-003` was gated as source-blocked, and `DK-H-004` — identity,
ritual, kinship, membership — was written and gated identically so that
the administrative reading would not become the default by being the only
one written down. The term audit removes *administrators*, *archive*,
*bureaucracy* and *literacy* from this record's own voice
(`06-BRIEFS/domain-k-translation-blocks.md` §4). "Sign-makers" and
"sign-users" are used throughout with institutional role unresolved, as
the task required.

**Item 3.** Did the unit privilege *writing* as the default reading of
the signs? `DK-H-001` and `DK-H-011` are registered as a pair and gated
identically. The word *script* is reserved for the disputed claim.

**Item 4.** Did the Rigvedic negative get an easier ride than an Indus
positive would have? This is the one where the answer is close. The
Rigvedic absences are typed `ABSENT DESPITE ADEQUATE SEARCH` and the
Indus absences are typed `NOT ACCESSIBLE` — and that is not a double
standard but the difference between a complete text and an unreachable
archive. The check that keeps it honest is `BR-K-006`: the Rigvedic
absence is refused as evidence about the Rigvedic world, and the
strongest measurement in the unit is therefore also the one whose
inference is most tightly blocked.

### Preferred-counter-narrative challenge

**Item 1.** The one retrieved decipherment claim is a Dravidian-priority
claim (`SRC-104`, 98.84% correlation with Old Tamil). It was retrieved,
read, registered at `DK-M-019`–`DK-M-021` and rejected at `DK-H-007` on
recoverability — its sign identities resolve to no published list, so no
line of it can be checked by any reader. The test that keeps this from
being a political exclusion: the same objection would reject an
Indo-Aryan, Sumerian or Elamite decipherment presented the same way, and
it is the objection the platform's own page already applies to all such
claims.

**Item 2.** Was the Dravidian-Indus reading given an easy ride
elsewhere? The step-13 check found `the-deep-root.html` stating "the
Indus world was Dravidian-related" as the platform's best-supported
reading, labelled as a reading and carrying its own falsifier. This unit
neither adopted nor attacked it: nothing retrieved here bears on the
language of the Indus signs, and `BR-K-007` records the three separate
bridges such a claim must cross.

**Item 3.** Was institutional rupture — the packet's own framing, R20
"THE MISSING RECORD" — accepted because it is the interesting answer?
`DK-H-006` is gated `ELIGIBLE IN PART`: the Rigvedic half was measured
and the Indus half is unreachable, and the join between them is not
made. `DK-H-010`, the null explanation — a liturgical praise corpus
would not describe a graphic technology in any case — is registered
first among the explanations of the silence, because the null is what
the others have to beat. `BR-K-004` records that the end of a practice
and the end of an institution are two claims.

**Item 4.** The trap itself. `DK-H-009` — that the people disappeared
because the signs and the institutions did — is `REJECTED`, and rejected
on the logic rather than on the evidence, because the evidence is
unreachable and the inference is invalid without it. The repository's
aDNA material is inherited and was not cited (`IH-109`, `IH-110`).

## 6. Why only three absences license anything

Thirteen absences are typed. Ten license nothing at all. Three are
`ABSENT DESPITE ADEQUATE SEARCH` — no writing vocabulary, no sealing
vocabulary, no balance or weight standard in the Rigvedic lexicon — and
they earn that type on four grounds: the corpus is complete rather than
sampled, the search is reproducible, two independent instruments agree,
and the coverage gap is stated (296 unglossed lemmas).

Even those three license only statements about the corpus. The bridge to
the society is refused at `BR-K-006` and the archive audit at `APA-K-001`
says why: a liturgical corpus records what the liturgy and the patron
need.

The domain's headline absence — no unambiguous Rigvedic description of
Indus writing — is typed `NOT RECOGNISED` and licenses the least of all,
because we could not identify such a description as *Indus* even if it
were there (`DK-A-004`).

## 7. The gates that could not be run

Method step 2 requires chronology before comparison and step 3 requires
geography. Neither could be run. No absolute date for the Indus sequence
or for Rigvedic composition was retrieved in this session, and this
repository holds no `VERIFIED` date for either; the only chronology in
hand is Arnold's relative stratification inside the Rigveda, which is
recorded per occurrence and claims nothing absolute. Seven of the eleven
hypotheses are therefore `NOT-ELIGIBLE-SOURCE-BLOCKED` rather than
judged, and the gate rows say `CANNOT BE GATED IN THIS SESSION` in the
chronology and geography fields rather than leaving them blank.

## 8. What this unit did not do

- It did not read CISI, ICIT, Mahadevan 1977, any ASI report, or any
  peer-reviewed article on Indus writing.
- It did not measure any Indus object class other than unicorn seals from
  one site, and did not measure distribution, stratigraphy or date.
- It did not read the 224 Rigvedic stanzas in Sanskrit. The passage-level
  check ran through two translations of one philological tradition, which
  is why `DK-A-003` is typed `NOT RECOGNISED` rather than
  `ABSENT DESPITE ADEQUATE SEARCH`.
- It did not read `citrá-` (147 tokens), `nā́man-` (117) or `rūpá-` (49)
  passage by passage; all three are glossed in the field of appearance
  rather than of marking, and the exclusion is a judgement recorded in
  `04-AUDITS/rv-marking-occurrences.py`.
- It did not test whether the later senses of `akṣára-`, `várṇa-` and
  `lipi-` develop where and when they are usually said to; every source
  that would date that development is blocked.
- It drafted no public copy for publication. `06-BRIEFS/domain-k-brief.md`
  is a brief in the step-14 shape, from accepted claims only, and is not
  a page.
