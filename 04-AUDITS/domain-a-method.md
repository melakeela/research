# Domain A — method, and the two adversarial tests

**Domain:** constitution §4.A, Rigvedic chronology and transmission.
**Run:** 2026-09-07, branch `claude/rigvedic-chronology-arnold-5raqe3`.
**Named trap:** neither "a perfect audio recording" nor "Pāṇini rewrote it".

This unit was commissioned to **examine** the programme's dependence on
Arnold's metrical strata rather than to use it, and to test whether any
instrument independent of Arnold is retrievable. Both were done. What
follows is the method, then the two §8 tests.

---

## 1. The fourteen steps, as actually run

**1. Bound the question.** The proposition under test is not "when was
the Rigveda composed". It is: *what does this repository's relative
chronology actually rest on, and is there anything else?* Date range:
the instruments, 1876–2026, not the text. Geography: not applicable and
recorded as such in the hypothesis gate rather than left blank. Seven
hypotheses were framed and gated (`domain-a-hypothesis-eligibility.csv`),
including both of the constitution's named reductions, so that neither
could be refused by assertion.

**2. Chronology first.** Eight dates, kept apart throughout and stated
as a block at `DA-I-010` and in measurement block 10. The one that
mattered most in practice was the distinction between a **publication**
date and a **composition** date: Grassmann 1876-7 and Oldenberg 1888
predate Arnold 1897 and 1905, and that single fact is what makes
`DA-M-012` load-bearing — a marked set fixed in 1876 cannot have been
copied from a book published in 1905. The same separation was then
applied to a person: Wüst's book is 1928, the regime is from 1933, the
reception literature is 2008–2024 (`APA-A-003`, `BF-014`).

**3. Geography and contact.** Not applicable to a transmission
question. Recorded rather than skipped.

**4. Evidence classes, inventoried separately.** Six classes were kept
apart and never allowed to borrow certainty: the **metrical** (Arnold's
strata, the restored text), the **editorial** (five scholars' stanza
markings, Oldenberg's page concordance), the **redactional**
(arrangement), the **morphological** (the Zürich annotation), the
**segmentational** (padapāṭha against modern lemmatisation), and the
**bibliographic** (what the connectors returned). The most important
result of the whole unit came from noticing that two of these were the
same class in disguise: `DEP-025`, metrical restoration and metrical
stratification read one signal.

**5. Source genealogy.** Five dependency rows, `DEP-021` to `DEP-025`,
and this is where the unit's central finding lives. The corpus appears
to offer five stratifications. Measured, it offers three: Oldenberg and
Wüst are one set at φ = 0.904, and Arnold 1897 and Arnold 1905 are one
author at φ = 0.825. Citation count is not independent confirmation and
neither is column count.

**6. Archive audit.** Five rows, `APA-A-001` to `APA-A-005`. The one
that changes how this unit should be read is `APA-A-004`: every
analytical layer of the digital corpus — lemmatisation, morphology,
metrical restoration, stratum transcription — is made in Europe or North
America, the corpus carries translations into German, French, English
and Russian and none into any South Asian language, and the one South
Asian contribution its own metadata records is **data entry**, credited
to "members of the Sansknet Project" with no individual named.

**7. Hypothesis gating.** Seven hypotheses gated before analysis. Two
rejected (A-3 Pāṇini-rewrote, A-5 arrangement-encodes-chronology), one
rejected as an absolute (A-2 the recording), three provisional, one held
at `HYPOTHESIS` — A-1, Arnold's periods, which is the whole question.
Rejections got a paragraph each and not a section, per step 7.

**8. Independent evaluation.** Each instrument was measured on its own
before any was compared with another. The arrangement analysis in
particular was run and reported before it was asked whether it agreed
with anything, which is why it could be reported as clean: it is silent
on date by construction (`BR-A-003`).

**9. Proportional space.** A-6, corpus heterogeneity — the one
hypothesis with convergent support from instruments that do not share a
signal — got the largest share. A-3 got a paragraph.

**10. Bridges tested.** Four, `BR-A-001` to `BR-A-004`. Three refused,
one not testable. `BR-A-001` is the one the commissioning instruction
asked for by name and it is refused **in both directions**: a maṇḍala
number does not deliver a date, and a later-or-redacted classification
does not erase the attestation fact of where a hymn sits.

**11. Current standing.** Not establishable, and this is the unit's
sharpest limit. Every connector that reaches this literature returns
abstracts; the one that reads full text was out of quota (`APA-A-005`,
`HOLD-009`).

**12. Falsifiers.** Recorded per hypothesis and per interpretation. The
serious ones are `HOLD-010` for A-1 and the circularity falsifier for
A-7.

**13. MelaKeela checked.** `06-BRIEFS/rv01-reconciliation.md` ships a
chronological-stratum column with `DEP-001` and `PUR-028` caveats
attached. Those caveats are now quantified and the brief's wording may
no longer be adequate; queued as `RA-015`. No live site page was found
to depend on the strata. `IC-A-002` records one contradiction with a
widely restated summary claim about the family books' size ordering.

**14. Public copy.** Not drafted. Nothing in this unit is finished
enough: A-1 is at `HYPOTHESIS`, four holds are open, and step 14 draws
only from accepted claims.

---

## 2. What the unit set out to find, and what it found

The commissioning question was whether **any instrument independent of
Arnold is retrievable**. Three were, and one was not.

| Instrument | Independent of Arnold? | What it can date |
|---|---|---|
| Oldenberg's arrangement analysis, reproduced from the corpus | **Yes, completely.** Its content is hymn length and addressee. | Nothing. It is a redaction fact and its silence is what makes it usable. |
| The four non-Arnold stanza markings (Grassmann, Oldenberg, Wüst, Witzel) | **Yes as authorship** — two published before Arnold. **Unknown as criterion**: whether they share metre as a criterion is `DA-I-002` and is unresolved. | The late end only. Nothing about the ordering of the other four periods. |
| Oldenberg's *Noten* page concordance | Yes. | Nothing about date; it maps editorial attention, and that attention is flat across Arnold's strata (`DA-M-017`). |
| The Zürich annotation used as its own evidence | **No, not usable as a check.** `DEP-026`: it is the annotation layer of the same group whose work Hellwig et al. analysed, and citing that paper as an independent check on a result computed from this annotation would be circular. | Reported raw and uncontrolled; offered as neither confirming nor refuting. |

And the sharpest single number the unit produced is not about any of
them. It is `DA-M-007`: **five book-by-stratum cells are exactly zero.**
Books 3, 4 and 7 contain no Archaic pāda at all, book 6 no Strophic,
books 4 and 8 no Cretic — 43.6% of the coded corpus. A zero cell is not
a small count. Whether that is Arnold's finding, Arnold's assumption or
the transcription's artefact cannot be told from the file, and `HOLD-010`
holds the check.

## 3. What Hellwig et al. 2021 actually tested

Because the instruction commissioning this unit was right that the
result is not a universal falsification, and because the narrower
question turned out to be unanswerable here.

From the abstract, retrieved in full through the Consensus connector
(`SRC-082`): the paper reviewed stratifications proposed in previous
literature; assessed support for them with statistical analyses of
**allomorphic** features that had been claimed to bear signals of
stratification; and ran a cluster analysis of the ten books on the same
data. Its result: once **metrical positioning, prosodic structure and
content** are controlled for, the allomorph distributions do not lend
significant support for **any** of the proposed stratifications; and
the cluster analysis favours book 10 occupying a special position while
overall differences across the ten books are not substantial.

What that does **not** cover, on the abstract's own wording: metre
itself — which is Arnold's instrument and not an allomorph — the
arrangement, the saṃhitā/padapāṭha relation, and absolute date.

What the abstract does not supply, and this record therefore does not
have (`HOLD-009`): **which** stratifications were tested, so whether
Arnold's five periods were among them is unknown; **which** allomorphic
features; and the author list, which the connector truncates to "Oliver
Hellwig et al.", leaving the Scarlata and Widmer attribution the
instruction supplied at `INHERITED-UNVERIFIED` (`BF-015`).

One thing can be said without the article. This repository's own data
reproduces the reason the controls matter: seventeen inflectional
categories give strong ordered patterns across Arnold's strata
(`DA-M-031`), and then book 9 — the one book addressed almost entirely
to a single deity — turns out to be the outlier on every one of them
(`DA-M-033`). Content moves these numbers by more than stratum does,
and that is visible here without citing anybody.

---

## 4. Prestige-bias challenge

*Did this privilege a claim because it is canonical, Sanskritic,
Brahmanical, Indo-European, European, colonial, institutionally
prestigious, repeatedly cited or nationally useful?*

**Two failures found and logged.**

`BF-012`. The first reading of `stanza_properties.json` treated its
five columns as five independent stratifications and would have
reported five-way convergence on Arnold's Popular stratum as strong
corroboration. Five names is a more satisfying result than three, and
the canonical instrument was the one that would have been flattered.
Corrected by measuring pairwise agreement **before** counting anything:
`DEP-022` and `DEP-023` collapse five to three.

`BF-013`. Restoration load runs heaviest in the Archaic stratum and
lightest in the Popular — exactly the direction an older-layer
hypothesis predicts — and the draft reported it as confirmation.
Corrected at `DEP-025`: both are metrical instruments on one text and
read one signal. `BR-A-002` records the bridge as failing.

**Three places the challenge was passed rather than failed.** The
arrangement result is strong (p = 3e-22) and was *not* converted into a
chronology, because its content is length and addressee (`BR-A-003`).
The morphological gradients are strong and ordered and were reported as
raw and uncontrolled, with the book 9 confound stated in the same
breath. And `DA-D-001` reports the finding that is least flattering to
this repository's own earlier work being wrong: no VERIFIED claim falls
if Arnold fails — which sounds like vindication and is not, because
fifteen rows would keep their truth and lose their point.

**One place the bias is structural and could not be corrected.**
`APA-A-005`: every instrument this unit could actually use is a
machine-readable European or North American analysis, and every
argument about them was unreadable. Machine-readable data was
over-weighted relative to argument for the whole unit, not by choice.

## 5. Preferred-counter-narrative challenge

*Did this accept a claim too easily because it is Dravidian,
Indigenous, anti-colonial, anti-Brahmanical, subaltern, diffusionist or
politically corrective?*

**One failure found and logged.**

`BF-014`. On finding that one of the five stratification authorities is
Walther Wüst — named in the retrieved reception literature among the
few German Sanskrit scholars who actively supported the National
Socialist regime — the first move was toward treating his markings as
tainted and setting them aside. That is the anti-colonial correction
applied *without doing the chronology*, and it is the mirror image of
accepting a source because it is canonical. Corrected by separating the
dates as the method requires (1928; 1933–45; 2008–2024), recording the
reception as an archive fact at `APA-A-003` because a record that must
stay capable of contradicting canonical scholarship has to be able to
state it, and noting that it changes nothing evidentially for the
reason `DEP-022` already established: Wüst's marked set *is*
Oldenberg's set, so no claim rested on him independently. Had it rested
on him, the correct move would still have been to read the book.

**Where the challenge was passed.** The obvious corrective narrative
available to this unit was *colonial philology invented the Rigvedic
strata and they are an artefact of it*. Four of the five authorities are
nineteenth- and early-twentieth-century German and British philologists
working at the imperial height, the corpus records South Asian
contribution only as data entry, and `DA-M-007`'s structural zeros
would have made a satisfying centrepiece for that story. It is not
told, because the evidence does not carry it: `DA-M-012` and `DA-M-013`
show three of those scholars converging on the same late residue, two
of them before Arnold, and something real is being tracked at that end.
`DA-I-002` states both readings and refuses to choose, which is the
honest position and not the comfortable one for either side.

**And the counter-narrative that was not adopted by default.** Nothing
here treats Pāṇini, the padapāṭha tradition or the prātiśākhyas as
either authoritative or as merely normative. `DA-I-009` reports that
the prātiśākhyas record their own uncertainty about the padapāṭha in
their own vocabulary — *sandeha*, *saṃśaya* — which is a tradition
describing its analysis as uncertain, and is used neither to elevate
that tradition as self-critical nor to dismiss it as unreliable.

---

## 6. What this unit did not do

Five of constitution §4.A's twelve sub-questions were reached: the
family books, books 8 and 9, books 1 and 10, compilation and canonical
organisation, and the Saṃhitā/padapāṭha relation with the metrical
question inside it. Four were touched at abstract level only —
Pāṇini's *chandasi* rules, metre as evidence for older pronunciation
beyond the restoration measurement, natural oral change before
fixation, and what may already have changed before preservation became
controlled. Three were not reached at all: recitational analysis beyond
the padapāṭha, what was preserved extraordinarily well as a positive
claim rather than a negative one, and the relation of any of this to a
composition date.

No public copy was drafted. No claim was promoted out of
`INHERITED-UNVERIFIED`. No VERIFIED claim anywhere in the repository
was downgraded, and `DA-D-001` explains why that is a finding and not
an absence of work.
