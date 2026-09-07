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
**Revised 2026-09-07 after independent adversarial review**, which overturned
two of this unit's results and corrected the source behind every lexical claim
in it. What changed, and in which direction, is §0a. `BF-017`.

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

## 0a. What adversarial review changed, and which way

An independent reviewer re-derived the corpus work and read the passages. The
measurement arithmetic held. **The source attribution behind every lexical
claim did not, and two results were overturned — all of it in the same
direction, the one that favoured this unit's conclusions.**

| What the unit wrote | What is true | Direction |
|---|---|---|
| Every gloss is "Grassmann 1873, one nineteenth-century German lexicon" | The gloss field is the **Zürich lemma-meaning column** (`SRC-089`), a modern composite citing Geldner, EWAia/Mayrhofer, Scarlata, Oldenberg, Lubotsky, Renou, Kuiper — with Grassmann marked `GM:` where followed. His *Wörterbuch* has never been retrieved here | A **self-criticism more flattering than the truth** |
| `DJ-011`, `VERIFIED`: no `durgá-` is ever "broken, besieged, entered or held" | **False at RV 5.34.7**, where Griffith, Geldner *and Grassmann* all render a fortified place people hold out in. The falsifier `DJ-I-03` set for itself had already fired | Removed the **load-bearing anti-Nandi result** |
| `DJ-009`, `VERIFIED`: the corpus "nowhere describes construction technique" | Never measured. The corpus carries `pakvá-` "baked" (25) against `āmá-` "unbaked" (11) and puts the unfired term **on a fort** | The mechanism that rescued §4 was itself unearned |
| "One philological line" logged as an archival limitation | Renou and Elizarenkova were **retrieved, ledgered, and unread**. Renou has *"forteresses (en briques) crues"* at RV 2.35.6 and *"maître de la cité"* at RV 1.173.10 — brick and city, at the two locators that matter most | A **disclosure substituted for a free check** |

Three of the gate's six diagnostic verdicts are withdrawn and **all three move
toward Nandi**. `DJ-009` and `DJ-011` are demoted to `PROVISIONAL`; `DJ-010` is
split and its term-list half put on `HOLD`; `DJ-013` and `DJ-014` are new and
both cut against this unit.

**A second review round then found three more, and they ran the other way.**
Written while repairing the first round, in rows whose purpose was to correct
an over-deflation, they overstated the case *for* the thesis:

- `DJ-009`'s replacement claimed the corpus has "no lemma glossed for the act
  of building". **The gloss column has zero verb coverage** — 0 of 700 root
  lemmas, 19.4% of tokens — so that probe was a guaranteed zero. This is
  `BF-015`'s own failure mode, in the row written to repair `BF-016` and
  `BF-017`, against `BF-015`'s own stated control. `BF-018`, `RA-021`.
- `DJ-013` reported Renou's *"forteresses (en briques) crues"* as brick "at the
  one púr- passage that states a material". **"En briques" is inside Renou's
  own bracket convention** — he uses parentheses in 93.6% of his rows for
  supplied material, and the Sanskrit `āmā́su pūrṣú` has no material word. That
  is §7's named prohibition, letting the translation decide the question. The
  unbracketed *"maître de la cité"* stands.
- `pakvá-`/`āmá-` was called "the fired/unfired opposition brick technology
  turns on". **It is culinary**: all 25 `pakvá-` are food, and 8 of 11 `āmá-`
  are one raw-cow/cooked-milk formula. RV 2.35.6 extends it to a *púr* once,
  and that once is the finding.

The shape is worth naming because it is not one slip and it is not one
direction: **six of the seven failures were disclosures offered in place of
checks that were free**, and the seventh was a search that could not have
returned anything. A limitation closable by reading a file already in the clone
is not a limitation — it is unfinished work with a caveat on top. And a repair
commit is exactly where the discipline lapses: correcting an error in one
direction is not a licence to stop checking in the other.

---

## 1. Ninety-nine, established rather than assumed

The reconciliation brief left four things open. Three are now closed and the
fourth has moved.

**Which passages state it.** Six: RV 1.54.6, 2.19.6, 4.26.3, 7.19.5, 7.99.5,
8.93.2. Re-derived here from the raw token layer without reference to the
counts register, and the two derivations agree exactly (`DJ-002`).

**Is it modal?** No. Nine passages state a `śatá-` count against six for 99 —
seven with the singular "a hundred" and two with the plural "hundreds"
(`DJ-015`). It is not maximal either. **It is the most quotable, and nothing
more.** (This brief first said "8 passages to 6", inherited from
`pur-4j-corpus.md`. Eight is neither the strict figure, 7, nor the inclusive
one, 9; the register said 9 all along. `RA-019`.)

**Is it formulaic?** The evidence for that reading is now twelvefold larger
than it was, and it did not come from the fort corpus. The expression that
yields ninety-nine — the cardinal `náva- 1` "nine" with `navatí-` "ninety" —
occurs in **19 stanzas of the Rigveda. Seven are in the púr- corpus and twelve
are not** (`DJ-003`). What the other twelve count:

> flowing rivers · a retinue of Suśravas · Vṛtras · rivers, or venom-stayers ·
> the arms of Uraṇa · Vāyu's harnessed steeds · a serpent's coils · Śambara's
> ramparts · unnamed things battered down · gifts of strength · the mighty ·
> thousands of oblations

Forts take the expression in **6 of 19** co-occurrences — and 3 of the 19 do
not yield 99 as the quantity of the object at all (RV 1.53.9 is sixty thousand
and ninety-nine, 10.98.10 is ninety-nine *thousand*, 1.191.13 is a genitive
plural), so on a strict reading it is **6 of 16**. Well under half either way.
The prior brief rested this on one control case, RV 10.104.8, where the
ninety-nine flowing streams sit in the same stanza as the epithet `pūrbhít`
"fort-breaker". That case is the cleanest, and it is not alone. The twelve
non-fort uses span **seven books and at least five Arnold strata**, so they are
not one book's mannerism.

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
different noun: `dehī́-`, which the corpus's gloss column gives as "Aufwurf,
Damm, Wall", an
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
is paywalled besides (`SRC-086`, `SRC-087`, `HOLD-007`, `D-046`).

**Nor is the term list securely Nandi's.** It reaches this repository as a
search index's summary of a publisher's abstract, and a WebSearch query string
is not a re-findable locator. It is now held separately at `HOLD` (`DJ-010B`),
and everything the gate says about the four terms inherits that hold. One item
should have raised the alarm unaided: `vr̥trá-` is *resistance* and a *demon*,
which is an odd word to find on a list of names for settlements — exactly what
a summariser garbles.

**Verdict: `HOLD`, gate reading `NOT-ELIGIBLE-SOURCE-BLOCKED`.** The suffix is
the finding.

*What could not be run.* Chronology needs an absolute date for the fort
passages; this repository has only Arnold's relative strata, single-sourced.
Geography needs the corpus to place a passage somewhere; it carries none.
**These are the two legs the thesis most depends on, and no amount of corpus
work supplies them.**

*What ran and tells against the thesis.* **One leg, and it survived review
intact:** the counts do not behave like an enumeration. Śambara alone carries
90, 99, 100 and "hundreds", and the ninety-nine expression counts rivers, arms,
horses, coils and oblations outside the corpus (§1, `DJ-I-01`).

*What ran and tells for it.* `vr̥jána-` — "Gemeinschaft, Territorium einer
Gemeinschaft, Niederlassung", 61 tokens — supports the territorial half. Note
the bridge, though: the gloss says a community's **territory**, and *politically
administered* is Nandi's phrase; territory → polity → administration is three
claims, and §10 of the method requires each to be tested separately. `pū́rpati-`
"lord of the fort" (RV 1.173.10) names an office attached to a `púr` — one
token, and itself inside a simile (`DJ-014`), which this brief earlier asserted
flatly while scrupulously flagging the same construction elsewhere.

*What the unit thought told against the thesis and does not.* The `durgá-`
result was the sharpest anti-Nandi item here and **it has been withdrawn in its
strong form**. At RV 5.34.7 — `durgé caná dhriyate víśva ā́ purú jáno` —
Griffith has "not even in wide **stronghold** may all the folk **stand firm**",
Geldner "in einer **Bergfeste hält sich** … ein ganzer Volksstamm", Grassmann
"an **festverschlossnem Ort** … **hält nicht lange Stand**". A fortified place,
and the verb is holding out. `DJ-011` is `PROVISIONAL`, the absolute quantifier
struck, and `RA-020` sends all 21 passages back to be read from an edition
rather than through a translation index.

**This is not a finding that Nandi is wrong, and it must not be reported as
one.** It is a finding that this repository cannot adjudicate the thesis, and
can say precisely why: no archaeological source, no absolute chronology, no
geography, one gloss column behind every lexical result, and a term list that
may not be his. A chapter is not its abstract, and Nandi may argue the
identification from evidence classes this unit holds none of.

`SRC-088` records that a stronger form of the same thesis is in circulation —
dating the Saṃhitās *from* the fort passages to 3300–2600 BCE — and is equally
unreachable. A domain J that gated only the milder case would have gated the
wrong one.

---

## 4. What the corpus says about brick, and what it does not

No lemma in the corpus's gloss column is glossed "brick" or "city", against a
stated denominator of **91.7% of lemmas and 78.98% of tokens** (`DJ-008`). The
column's own entry for `púr-` is an earthwork — "Wall aus Steinen und Lehm,
Verschanzung, Palisade". 67.5% of simplex tokens are accusative and **3.6%
locative**: the commonest thing a *púr* does is be the direct object of a verb
of breaking. No lemma is glossed for the act of building.

**The deflationary conclusion is not available, and this brief reached for it
twice before the evidence stopped it.**

*First stop — the passages.* Of the three locative passages, RV 6.2.7
*"pleasant like an old man in a fort"* and RV 9.107.10 *"as a body of troops
enters the fort"* are **similes**. A simile draws on what its audience finds
ordinary, so both **presuppose the inhabited fort the corpus never asserts**
(`DJ-007`). The strongest evidence against the deflationary reading was inside
the passages the deflationary reading would cite. `BF-016`.

*Second stop — the corpus has the vocabulary after all.* The brief then typed
the absence `NOT PRODUCED` on the ground that a liturgical corpus "nowhere
describes construction technique for any structure". **That was never
measured, and it is wrong.** The Rigveda carries the fired/unfired opposition
brick technology turns on — `pakvá-` "gekocht, gebacken" at 25 tokens against
`āmá-` "roh, ungekocht" at 11 — and it puts **the unfired term on a fort**, at
RV 2.35.6 (`DJ-009`).

*Third stop — a translator in the same clone supplies both missing words.*
Renou renders RV 2.35.6 *"Dans les forteresses **(en briques) crues**"* —
unfired **brick**, at the one `púr-` passage stating a material — and RV
1.173.10 *"maître de la **cité**"*, lord of the **city** (`DJ-013`). Renou was
retrieved, ledgered as `SRC-076`, and sitting unread in the pinned clone while
this unit wrote "one philological line" as a disclosed limitation.

**So: the gloss column carries no word for brick or city, and a translation
inside the same corpus carries both, at the two locators where it matters
most.** The first is a fact about a lexicon; the second is a fact about a
reading. Neither settles what a `púr-` was built of, and no argument in either
direction may cite one without the other.

---

## 5. What this unit did not do

- **Did not read Nandi.** `HOLD-007`, `D-046` — payment and lawful acquisition.
- **Did not establish that the four-term list is Nandi's.** It is a search
  index's summary of a publisher's abstract. `DJ-010B`, at `HOLD`.
- **Did not retrieve any archaeological source, geography, or absolute
  chronology.** The three things the identification question turns on.
- **Did not read the `durgá-` passages from an edition.** The claim that they
  are terrain rather than fortification was made through a translation index
  and its absolute form is now withdrawn. `RA-020`.
- **Did not survey what `pakvá-` and `āmá-` modify elsewhere**, which is what
  would tell whether the fired/unfired pair is architectural vocabulary or only
  culinary. `DJ-009` is `PROVISIONAL` for that reason.
- **Did not read Renou and Elizarenkova across the corpus** — only at the
  passages review forced open. Both are in the pinned clone. Doing so is cheap
  and is the first thing the next unit should do.
- **Did not resolve C-2 or C-4.** `DJ-005` makes C-2 concrete; the ruling is the
  owner's. `RA-016`.
- **Did not re-run the counts, fields or typology over a semantic corpus.**
  Depends on that ruling.
- **Did not retrieve Sāyaṇa,** which is the one correction that would move the
  archival asymmetry rather than merely disclose it. `RA-015`.
- **Did not retrieve Grassmann's *Wörterbuch*,** which this unit spent four
  claim rows believing it had. `RA-018`.
- **Did not run step 13** against `melakeela/site`, which is outside this
  session's repository scope.

---

## 6. What would change these findings

- **§1 and §2 fall** if the C-2 ruling goes semantic: six 99-passages becomes
  seven, and every denominator in the corpus moves.
- **§1 is falsified** by a count outside the stock — a 23 or a 41 — attached to
  a fort, which would show the corpus can state an arbitrary number and chooses
  not to. Its formulaicity reading weakens if the six fort uses prove separable
  from the rest by stratum or dialect; the book-and-stratum spread reported in
  §1 is a crude test and a finer one could still find structure.
- **§3's verdict is overturned** by obtaining the chapter and finding its
  argument does not rest on the four-term list its abstract names — or by
  finding that the list is not his at all, which `DJ-010B` treats as live. It is
  overturned in the other direction by any archaeological or
  absolute-chronology source placing a `púr-` passage in a Harappan settlement.
- **§3's remaining anti-thesis leg — the counts — falls** if a fort count
  outside the stock turns up, the same falsifier as §1. It is the only leg that
  survived review intact, so the gate now rests on one measurement.
- **§3 and §4 are both sharpened** by Sāyaṇa, or by any lexicon independent of
  the Zürich gloss column. Note what review already showed: a *European*
  translator, Grassmann, contradicts the gloss column's `durgá-` at RV 5.34.7,
  so the check that moves these sections need not wait on a non-European source
  — it only needed the files already in the clone to be opened.
- **§4 falls** in the deflationary direction if a lemma glossed "brick" or
  "city" turns up in another lexicon, which would also show the single-source
  dependency was doing the work. It has already moved in the other direction
  once, on Renou and on `pakvá-`/`āmá-`.
