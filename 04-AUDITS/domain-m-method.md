# Domain M — the Brahui geographic measurement, and North Dravidian

**Unit:** owner challenge to the Brahui leave-one-out geographic
measurement, 2026-09-07.
**Register:** `03-REGISTERS/domain-m-brahui-position.csv`, DMB-001 to DMB-026.
**Scripts:** `04-AUDITS/brahui-loo-geography.py`,
`04-AUDITS/north-dravidian-cognate-sharing.py`.
**Method failures:** `BF-005`, `BF-006`. **Re-audits:** `RA-004`, `RA-005`.
**Holds:** `HOLD-004`. **Owner decision:** `D-035`.

## 0. The premise had to be checked before it could be acted on

The challenge names a measurement. No such measurement exists in this
repository. `git rev-list --all` searched for every leave-one-out
construction returns nothing; there is not a single geographic coordinate
anywhere in the repository at `bbe4803`; and domain E's only geographic
work is the Rigvedic hydronym census, which counts river names inside a
Sanskrit corpus and contains no Dravidian language and no Brahui datapoint.
`DMB-003` records this, `SRC-048` logs the search, `D-035` asks the owner
where the measurement actually lives.

Two consequences ran through everything below. First, `DMB-001` — the
interpretation being superseded — is written out from the owner's
description rather than quoted from an original, because there is no
original here to quote. Second, the measurement had to be **reconstructed**
before it could be assessed, so what is tested at `DMB-012` is a
reconstruction of the design the owner described, not the original run.
That is why `DMB-004` is `PROVISIONAL` and not `VERIFIED`.

## 1. What the two objections are, kept apart

The owner raised two. They are recorded as raised, at `DMB-004` and
`DMB-005`, and neither was resolved by assertion.

**Objection 1** is about interpretation: a leave-one-out result measures
exposure to one datapoint. This is testable by computing every element's
influence rather than one element's, which is what §3 below does.

**Objection 2** bundles two propositions that behave differently under
measurement, and the register keeps them apart in `DMB-005`'s note rather
than averaging them into one status:

- **(a)** a distance-to-reference statistic has no term for shared descent.
  This is a property of the statistic and it is sound. The "Euclidean" half
  is additionally borne out: the metric's error is largest for exactly the
  three languages at issue (`DMB-014`).
- **(b)** Brahui, Kurukh and Malto are a clade. This is a claim about
  Dravidian. The owner explicitly required it be measured, not assumed, and
  §4 measures it.

## 2. Reconstruction: the instrument

Twenty varieties, fixed by DravLex (`SRC-049`), with Glottolog point
coordinates (`SRC-050`). Statistic: `S(R, L)` = great-circle distance from
a reference point `R` to the nearest language in set `L`. Influence of
language *i*: `S(R, L∖{i}) − S(R, L)`.

Three design decisions and why:

- **A grid, not an anchor.** The reference point is the free parameter the
  whole objection turns on, so reporting one anchor would reproduce the
  defect. 221 points at 1° spacing over 24–36 N by 60–76 E — the quadrant
  north and west of the attested range — plus one deliberate non-north-
  western control at 24 N 76 E.
- **Every element's influence, not Brahui's.** The `BF-005` control.
- **Both metrics.** Great-circle throughout, with Euclidean-on-degrees
  computed alongside so the metric's own error is visible rather than
  assumed away.

## 3. What the geography measurement returned

**Reference-free first.** Brahui's nearest attested Dravidian neighbour is
1,561.5 km away, against a median nearest-neighbour distance of 67.0 km and
a second-place Kolami at 372.4 km. Brahui is 23.3× the median (`DMB-010`).
This needs no reference point and is the honest form of "Brahui stands
apart." It dates nothing and is equally predicted by all six models at
constitution §4.M.

**Then the leave-one-out.** Eighteen of the twenty varieties have influence
**exactly zero at all 221 reference points**. Only Brahui and Kolami move
the statistic at all. Brahui is nearest at 94.1% of grid points and carries
81.3% of the summed maximum influence (`DMB-012`). Objection 1 is borne out
near the limit of what it claimed: a statistic to which eighteen of twenty
datapoints contribute nothing is not a measurement of the twenty.

**And the effect size is a choice.** Deleting Brahui moves the statistic by
+892 km from 33 N 72 E, +1,043 from 30 N 70 E, +1,418 from 29.5 N 67.5 E,
+1,453 from 36 N 64 E — and by **0 km** from 24 N 76 E (`DMB-013`). A result
that ranges from nothing to 1,453 km according to an unjustified parameter
is not a finding. Choosing a *northwestern* anchor is already a choice to
measure Brahui, because Brahui is the northwesternmost point in the set.

**The unexpected one.** Brahui's nearest attested Dravidian neighbour is
**Kolami**, at 1,561.5 km — not Kurukh (2,038.1) and not Malto (2,139.2)
(`DMB-011`). This complicates objection 2 rather than confirming it, and is
recorded that way. Whatever the subgrouping turns out to be, the geographic
remainder after deleting Brahui is not structured by it.

## 4. What the subgroup measurement returned

Exclusively shared cognate sets — attested in every member of a group and
in no non-member — over all 190 pairs and all 1,140 triples.

| quantity | result | rank |
|---|---|---|
| Kurukh–Malto exclusive sets | **19** | 1 of 190 pairs |
| Kurukh–Malto sharing rate | 48.4% over 95 concepts | each other's top partner |
| Brahui–Kurukh exclusive sets | **1** | 24 of 190 |
| Brahui–Malto exclusive sets | **1** | 25 of 190 |
| Brahui–Kurukh sharing rate | 22.0% | 7th of Brahui's 19 partners |
| Brahui–Malto sharing rate | 17.9% | 15th of Brahui's 19 partners |
| Brahui–Kurukh–Malto exclusive sets | **2** | 4 of 1,140 raw, 6 normalised |

The lower node is strongly supported and the upper node — the one that
attaches Brahui — rests on two words: *horn* (maɾgʰ / maɾag / maɾgadu) and
*smoke* (mo:ʃ / mosaga / mo:ha). The rank of 4 out of 1,140 flatters it: the
median triple scores 0 and the top triple scores 3, so a high rank is worth
two lexical items. Reporting the rank without the absolute count would
repeat `BF-004`.

Three things stop this from being read as a refutation:

- **The instrument is the wrong one.** Krishnamurti's North Dravidian is
  phonological and morphological. DravLex is a 100-concept wordlist. The
  absence is typed **NOT PRODUCED**, and **NOT ACCESSIBLE** for the rest
  (`DMB-020`, HOLD-004). Under the negative-evidence standard neither is a
  refutation.
- **Brahui is lexically distant from everything.** Its best partner reaches
  34.4% where the median pair reaches 38.5%. And its three top-ranked
  partners — Parji, Ollari_Gadba, Kuwi — are exactly the three
  lowest-coverage varieties (64, 59, 56 concepts), so those ranks are the
  least reliable numbers in the table and are *not* a Brahui–Central
  Dravidian finding.
- **The instrument is not independent of the hypothesis.** DravLex's coding
  lists Krishnamurti 2003 among its sources; Glottolog's North Dravidian
  node cites Krishnamurti 2003 *and nothing else*, as do its Central and
  South nodes. One book, re-encoded twice, and never read in this project
  (`DEP-008`, `DMB-021`, `IH-237`).

That last point cuts toward taking the negative slightly *more* seriously,
not less: an instrument informed by a classification would be expected to
reproduce it, and this one reproduces the lower node emphatically and the
upper node barely.

## 5. Contested status

Established: the question is **posed** in the specialist literature.
McAlpin, "Is Brahui Really Dravidian?", BLS 6 (1980) 66–73; Bray, *The
Brahui Language, Part II The Brahui Problem* (1986); McAlpin's
Elamo-Dravidian papers of 1974 and 1975, which supply a wholly different
account of northwestern Dravidian-like material (`DMB-023`, `DMB-024`).

Not established: **what any of them concluded.** These are bibliographic
records from Glottolog's reference set. Every archive, publisher and
bibliographic API is blocked (`SRC-052`); nothing was read. A title is not
an argument, and no inference from "McAlpin asked whether Brahui is really
Dravidian" to any answer is licensed by anything in this repository. This
is why `DMB-023` and `DMB-024` are `PROVISIONAL`.

One further negative, typed: Glottolog's bibliography contains **no work
whose title names North Dravidian** in any spelling, against many naming
Brahui, Kurux and Malto individually (`DMB-025`). Within that bibliography
— large and curated specifically for classification — this is **ABSENT
DESPITE ADEQUATE SEARCH**. It is not an absence claim about the literature
as a whole. It does not show the subgroup is wrong; it shows its support is
carried by survey-level statements, which is what `DEP-008` found from the
other direction.

## 6. The domain M flag

`DMB-006`. The leave-one-out design is **not model-neutral**, and this is
the deepest of the three problems with the original interpretation — deeper
than the statistics and deeper than the metric.

Treating Brahui as *detachable* — a datapoint whose removal leaves the rest
of the family intact and interpretable — presupposes the second or fifth of
the six models constitution §4.M (lines 452–463) requires be held open:
later long-distance migration, or a small migrating group plus local
adoption. On the first, third and fourth — long-term northwestern survival,
broader ancient distribution followed by replacement, dialect networks
followed by fragmentation — Brahui is not detachable at all, because on
those models it is not an addition to the distribution but a survival of
it. §4.M also says in terms: *do not treat medieval Brahui migration as
documented fact* (line 454). The inherited record already `REJECTED`
presenting late migration as the correction (`R-10`, `IH-156`, `IH-031`).

So the instrument builds a verdict on §4.M's open question into its own
shape, before any evidence is consulted. Nothing in this unit closes any of
the six models, and nothing in it was allowed to.

## 7. The two adversarial tests

**Prestige-bias challenge.** Did this privilege a claim because it is
canonical, Indo-European, European, colonial, institutionally prestigious
or repeatedly cited?

One live exposure, and it was corrected. Glottolog is a prestigious,
heavily used reference resource, and the first draft of this unit treated
"Glottolog has a North Dravidian node" as independent corroboration of the
conventional subgrouping. It is not: Glottolog's node cites Krishnamurti
2003 alone, and so does DravLex's coding in part. That is one source, and
the source-independence constraint says two citations tracing to one work
count as one. `DEP-008` and `DMB-021` record it and `DMB-026` is capped at
`PROVISIONAL` because of it. A second exposure was declined rather than
corrected: the temptation to state what McAlpin 1980 and Bray 1986 argue,
on the strength of famous titles, when neither was read (`DMB-023`).

**Preferred-counter-narrative challenge.** Did this accept a claim too
easily because it is anti-colonial, Indigenous, subaltern, corrective or
politically useful?

The structural risk here runs the other way from usual and has to be named
that way. The interpretation being superseded pointed toward *migration*,
which in this project's inherited record is the position already rejected
as a default (`R-10`). Removing a bad argument for migration is exactly the
kind of correction that feels virtuous, and the pull was to let the
supersession slide into support for the relict hypothesis. It does not, and
`DMB-016` says so explicitly: a 1,561 km gap is what a relict looks like
and it is also what a migrant looks like. The statistic has no term that
separates them.

Two specific places the pull was resisted:

- `DMB-011` is a finding that *complicates* the owner's own objection 2 —
  Brahui's nearest neighbour is Kolami, not Kurukh or Malto — and it is
  reported at full weight rather than buried in a note.
- `DMB-022`, Brahui's 60.6% singleton rate, is the single most misusable
  number in this unit. It is consistent with early divergence, which favours
  the relict and broader-distribution models, and equally consistent with
  heavy contact replacement, which every model predicts. The row says so and
  says it establishes nothing about dating.

**Result of both tests:** two corrections made (`DEP-008`, the `PROVISIONAL`
cap on `DMB-026`), one temptation declined (`DMB-023`), one asymmetry
disclosed (§7 above). No claim in this unit changed direction as a result of
either test, and no claim was allowed to close a §4.M model.

## 8. What is on hold

`HOLD-004`. Krishnamurti 2003 is the book everything traces to and it has
never been read in this project. Kobayashi and Tirkey 2017 pp. 11–14 is the
one precise locator for the one node with a second source. Emeneau 1962,
McAlpin 1980 and Elfenbein 1998 are named, not read. `HOLD-002` (DEDR) is
unchanged and reconfirmed. Only `github.com` and `raw.githubusercontent.com`
answered at all (`SRC-052`), which is tighter than the characterisation
taken four hours earlier the same day — `RA-003`'s warning about stale
reachability rows should be read as covering `SRC-045` too.
