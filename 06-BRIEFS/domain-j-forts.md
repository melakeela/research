# Domain J — the Rigvedic forts: what this unit added, and what it could not do

**Written:** 2026-09-07
**Unit type:** measurement and gate. The registers are the product; this is the
argument over them.
**Specification:** `00-CONTROLLER/METHODOLOGY-CONSTITUTION.md` §4J
**Method, denominators, both §8 tests:** `04-AUDITS/domain-j-method.md`
**Registers:** `03-REGISTERS/domain-j-measurements.csv` (12),
`domain-j-interpretations.csv` (3), `HYPOTHESIS-ELIGIBILITY.csv` `HYP-J-001`
**Builds on:** `06-BRIEFS/rv01-reconciliation.md` and
`06-BRIEFS/pur-4j-corpus.md`

---

## 0. The state this unit found, and what it did about it

`06-BRIEFS/rv01-reconciliation.md` established that **106 counts word-tokens of
seven `púr-`-derived lemmas and 99 counts forts named in passages, and they are
different objects.** That finding stands untouched here. Nothing below
reconciles them, and nothing below uses 106 as a quantity of forts.

It also scored the then-existing register at **1 of §4J's 15 enumerated items
delivered and 14 absent**. That gap had already been closed — on branch
`claude/pur-corpus-4j-extension-ux9wdc`, which built the 103-passage corpus, the
counts, the fields and the five-way typology. **That branch was not merged to
`main` and had no open pull request.** This unit merged it as a base and then
did to it what it was built for: reproduced it, audited it, and finished the
part of §4J it did not reach.

Nothing was promoted by being merged. The reproduction is `DJ-001` and the row
states what reproduction is worth — identical code over identical input must
give identical output, so it tests the pipeline and not the corpus.

---

## 1. Ninety-nine, established rather than assumed

The reconciliation brief left four things open. Three are now closed and the
fourth has moved.

**Which passages state it.** Six: RV 1.54.6, 2.19.6, 4.26.3, 7.19.5, 7.99.5,
8.93.2. Re-derived here from the raw token layer without reference to the
counts register, and the two derivations agree exactly (`DJ-002`).

**Is it modal?** No. One hundred is, at 8 passages to 6. It is not maximal
either — 100, "hundreds" and 1000 are larger. **It is the most quotable, and
nothing more.**

**Is it formulaic?** The evidence for that reading is now twelvefold larger
than it was, and it did not come from the fort corpus. The expression that
yields ninety-nine — the cardinal `náva- 1` "nine" with `navatí-` "ninety" —
occurs in **19 stanzas of the Rigveda. Seven are in the púr- corpus and twelve
are not** (`DJ-003`). What the other twelve count:

> flowing rivers · a retinue of Suśravas · Vṛtras · rivers, or venom-stayers ·
> the arms of Uraṇa · Vāyu's harnessed steeds · a serpent's coils · Śambara's
> ramparts · unnamed things battered down · gifts of strength · the mighty ·
> thousands of oblations

Forts take the expression in 6 of 19 uses — **under a third.** The prior brief
rested this on one control case, RV 10.104.8, where the ninety-nine flowing
streams sit in the same stanza as the epithet `pūrbhít` "fort-breaker". That
case is the cleanest, and it is not alone.

**The reading this does *not* license** is in `DJ-I-01`'s `evidence_against`
column, because it is the reason the formulaicity answer was not simply taken:
the numbers **sort by narrative cycle**. Seven goes with Purukutsa and the Pūru
in all four of their passages; 99 and 100 go with Divodāsa, Atithigva and
Śambara. Ornament does not sort by story. A quantity used for twelve kinds of
object is still doing something when it is chosen, and 19 stanzas is a modest
denominator. `DJ-I-01` is `PROVISIONAL` and says why.

---

## 2. The seventh passage, and the number that changes

**RV 6.47.2 has Indra smash `navatíṁ náva ca dehyò` — ninety-nine of them — and
they are Śambara's.** Same expression, same opponent as three of the six, a
different noun: `dehī́-`, which Grassmann glosses "Aufwurf, Damm, Wall", an
earth-heap, from √*dih* "smear, plaster up". Griffith renders "ramparts",
Geldner "Mauern", Grassmann "Wälle", Elizarenkova "валы". All four render the
wall and all four render the number (`DJ-005`).

`dehī́-` is one of the six fort-adjacent lemmas that `PUR-006` excludes **by
design**, on an etymological membership test. So:

> **"Six Rigvedic passages state ninety-nine forts" is true on the
> etymological reading of §4J's "complete corpus" and false on the semantic
> one, where it is seven.**

Reconciliation C-2 was until now a defensible choice with no number attached to
it. It has one. Choosing between the readings is the owner's (C-4); the
consequence is queued as `RA-016`, and it reaches further than this sentence —
a semantic corpus changes the denominator of every count, field and typology
row.

---

## 3. The Nandi gate

R. N. Nandi, "The City and the Citadel" (Routledge 2017), argues that the
Rigvedic fortified settlements — named, per its abstract, by `púr-`, `durgá-`,
`vr̥trá-` and `vr̥jána-` — are the walled habitations and citadels of the
Greater Indus belt. **This is §4J's prohibition in its canonical published
form**, and §4J's one instruction for this domain is written against it.

**The chapter is not read.** Every publisher, DOI-resolver, repository and
bibliographic-API host is `EGRESS_BLOCKED` on both available channels, and it
is paywalled besides (`SRC-086`, `SRC-087`, `HOLD-007`, `D-046`). What was
gated is the thesis as the abstract states it. The only content taken from the
abstract is the four-term list, used to decide which terms to test.

**Verdict: `NOT-ELIGIBLE-SOURCE-BLOCKED`.** The suffix is the finding.

*What could not be run.* Chronology needs an absolute date for the fort
passages; this repository has only Arnold's relative strata, single-sourced.
Geography needs the corpus to place a passage somewhere; it carries none.
**These are the two legs the thesis most depends on, and no amount of corpus
work supplies them.**

*What ran, and cut against the thesis.* Of the four named terms, **two do not
denote fortified settlements on the lexicon in hand.** All 21 `durgá-` tokens
are neuter and every one means difficult ground or peril — six of them the same
refrain at RV 1.106.1–6, *"as a chariot from a difficult ravine"* — and not one
is broken, besieged, entered or held (`DJ-011`). The `vr̥trá-` family glosses
as resistance and the demon Vṛtra (`DJ-010`). The Classical Sanskrit
"fortress" sense of `durga-` read back into the Rigveda is exactly the §7
failure the translation standard exists to catch.

*What ran, and cut for it.* `vr̥jána-` — "Gemeinschaft, Territorium einer
Gemeinschaft, Niederlassung", 61 tokens — supports the "politically
administered territory" half **directly**. And `pū́rpati-` "lord of the fort"
(RV 1.173.10) names a political office attached to a `púr`. These are the
strongest items on that side and they are real.

**This is not a finding that Nandi is wrong, and it must not be reported as
one.** It is a finding that this repository cannot adjudicate the thesis, and
can say precisely why: no archaeological source, no absolute chronology, no
geography, and one nineteenth-century German lexicon behind every lexical
result. A chapter is not its abstract, and Nandi may argue the identification
from evidence classes this unit holds none of.

`SRC-088` records that a stronger form of the same thesis is in circulation —
dating the Saṃhitās *from* the fort passages to 3300–2600 BCE — and is equally
unreachable. A domain J that gated only the milder case would have gated the
wrong one.

---

## 4. What the corpus says about brick, and what it does not

No lemma in the Rigveda is glossed "brick" or "city", against a stated
denominator of **91.7% of lemmas and 78.98% of tokens** (`DJ-008`). Grassmann's
own gloss of `púr-` is an earthwork — "Wall aus Steinen und Lehm, Verschanzung,
Palisade". 67.5% of simplex tokens are accusative and **3.6% locative**: the
commonest thing a *púr* does is be the direct object of a verb of breaking.

**The conclusion that suggests is not available, and the reason is in the
passages themselves.** `DJ-009` types the absence twice — `ABSENT DESPITE
ADEQUATE SEARCH` for the lexicon, `NOT PRODUCED` for the historical question —
because a liturgical praise corpus that nowhere describes construction
technique for *any* structure was not going to name a building material
whatever the material was. And of the three locative passages, RV 6.2.7
*"pleasant like an old man in a fort"* and RV 9.107.10 *"as a man enters the
fort"* are **similes**. A simile draws on what its audience finds ordinary, so
both **presuppose the inhabited fort the corpus never asserts** (`DJ-007`).

The strongest evidence against the deflationary reading was inside the passages
the deflationary reading would cite. An earlier draft of `DJ-I-02` asserted it
anyway; that draft is logged as a method failure at `BF-016`.

**The corpus gives no positive lexical evidence that a `púr-` was a brick-built
city, and no evidence that it was not.**

---

## 5. What this unit did not do

- **Did not read Nandi.** `HOLD-007`, `D-046` — payment and lawful acquisition.
- **Did not retrieve any archaeological source, geography, or absolute
  chronology.** The three things the identification question turns on.
- **Did not resolve C-2 or C-4.** `DJ-005` makes C-2 concrete; the ruling is the
  owner's. `RA-016`.
- **Did not re-run the counts, fields or typology over a semantic corpus.**
  Depends on that ruling.
- **Did not test whether the twelve non-fort uses cluster** by book, poet or
  stratum. If they do, `DJ-I-01` weakens. `RA-017`.
- **Did not retrieve Sāyaṇa,** which is the one correction that would move the
  prestige-bias finding rather than merely disclose it.
- **Did not run step 13** against `melakeela/site`, which is outside this
  session's repository scope.

---

## 6. What would change these findings

- **§1 and §2 fall** if the C-2 ruling goes semantic: six 99-passages becomes
  seven, and every denominator in the corpus moves.
- **§1's formulaicity reading weakens** if the twelve non-fort uses cluster by
  book, poet or stratum — a local mannerism, not a corpus-wide formula.
- **§1 is falsified** by a count outside the stock — a 23 or a 41 — attached to
  a fort, which would show the corpus can state an arbitrary number and chooses
  not to.
- **§3's verdict is overturned** by obtaining the chapter and finding its
  argument does not rest on the four-term list its abstract names. It is
  overturned in the other direction by any archaeological or absolute-chronology
  source placing a `púr-` passage in a Harappan settlement.
- **§3 and §4 are both sharpened** by Sāyaṇa, or any lexicon outside the
  Grassmann–Geldner line. `DJ-011` — the strongest single result against the
  term list — is one nineteenth-century German dictionary's reading before it
  is a measurement.
- **§4 falls** if a lemma glossed "brick" or "city" turns up in another
  lexicon, which would also show the single-source dependency was doing the
  work.
