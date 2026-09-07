# The §4J forts corpus

**Written:** 2026-09-07
**Unit type:** corpus build with findings. Registers are the product; this is
the argument over them.
**Specification:** `00-CONTROLLER/METHODOLOGY-CONSTITUTION.md` §4J
**Extends:** `03-REGISTERS/rigveda-pur-family.csv` (28 claims, 106 tokens) and
`06-BRIEFS/rv01-reconciliation.md`
**Method and denominators:** `04-AUDITS/rigveda-pur-4j-method.md`
**Translation standard:** `06-BRIEFS/pur-translation-standard.md`

---

## What was built

**Every finding below carries its status.** Findings 1–4 are `VERIFIED`
measurements. Finding 5 and the typology are `PROVISIONAL` readings, and are
marked as such where they appear — the register/interpretation split exists to
stop a reading inheriting a measurement's standing by sitting next to one, and a
narrative document is where that leak happens.

| Register | Rows | Kind |
|---|---:|---|
| `rigveda-pur-passages.csv` | 103 | the passage index |
| `rigveda-pur-counts.csv` | 49 | every numeral token, with the attachment test |
| `rigveda-pur-fields.csv` | 103 | §4J's semantic fields |
| `rigveda-pur-typology.csv` | 103 | the five-way classification |
| `rigveda-pur-4j-claims.csv` | 32 | measurements — 22 `VERIFIED`, 10 `PROVISIONAL` |
| `rigveda-pur-4j-interpretations.csv` | 3 | readings, all `PROVISIONAL`, each with its counter-evidence |

The reconciliation brief scored the prior register at **1 of §4J's 15
enumerated items delivered and 14 absent**, with the row basis partial and the
typology absent. All fifteen are now addressed. Two — *proposed geography* and,
independently, *poet lineage* at full strength — are addressed by establishing
that the source does not exist in this container and typing the absence, which
is what the negative-evidence standard asks for and is not the same as filling
them.

---

## The five findings

### 1. Ninety-nine is not the modal count. One hundred is. `VERIFIED`

**21 of 103 passages state a cardinal count of forts; 82 state none.**

| Count | Passages |
|---|---:|
| **100** | **9** |
| **99** | **6** |
| 7 | 4 |
| 90 | 2 |

The six that state 99 are RV 1.54.6, 2.19.6, 4.26.3, 7.19.5, 7.99.5, 8.93.2.
The reading is secure — the padapāṭha analyses the words separately and
Griffith, Geldner and Grassmann render 99 at all six — but **99 is never a
single numeral.** It is two words, `náva` "nine" and `navatí-` "ninety", joined
by `ca` in three passages and separated by intervening words in four.

The reconciliation brief left three options open: modal, maximal, or merely
quotable. It is **not modal** (100 beats it 9 to 6) and **not maximal** (100 and
1000 are larger). It is the most quotable. §4J's "other counts" resolves to
**seven**, and to nothing else.

### 2. Śambara's forts are counted two ways, not five `PROVISIONAL`

| Passage | Śambara's forts |
|---|---|
| RV 2.19.6 | **99** |
| RV 4.26.3 | **99**, plus "the hundredth" completing it |
| RV 7.99.5 | **99** |
| RV 2.14.6 | **100** |
| RV 6.31.4 | **100** |

**This finding replaces a stronger one that was wrong.** It first read
"Śambara alone has every count the constitution enumerates" — 90, 99, 100, the
hundredth and hundreds across six passages — and it was the strongest evidence
for finding 5. Three of the five were errors, all running toward finding 5's
conclusion, and an independent reviewer found them:

- **RV 1.130.7's ninety are not Śambara's.** `bhinát púro navatím indra pūráve
  / dívodāsāya` breaks them **for Pūru and Divodāsa**; Śambara is in a separate
  clause with no genitive tying the forts to him. The claim rested on his
  merely occurring in the stanza — the inference finding 3 exists to refute.
- **"The hundredth"** is an ordinal completing the 99, not a sixth count.
- **"Hundreds" at RV 6.31.4 is one hundred** — `śatā́ni` is the same form as
  `śatā́` at RV 1.53.8, and three translators are unanimous.

What survives is **99 three times and 100 twice**, which is nearly stable, and
because the 99 and the hundredth are one schema it may be one value expressed
two ways. `BF-014` logs the failure; `PUR4J-007` carries the restatement.

### 3. The same expression counts rivers `VERIFIED`

RV 10.104.8c: `navatíṁ srotyā́ náva ca srávantīr` — the identical
`náva`+`navatí-` expression, in the identical construction, counting
**ninety-nine flowing streams**. Griffith "nine-and-ninety flowing streams";
Geldner "die neunundneunzig fließenden Ströme"; Grassmann "Die neunundneunzig
Flüsse". All three agree.

The stanza also carries `pūrbhít` "fort-breaker", an epithet of Indra taking no
numeral. So this is simultaneously the control case for formulaicity **and** the
case that defeats any stanza-level co-occurrence measure. The prior method note
measured `navatí-` at 33.5× its corpus rate inside family stanzas and declined
to read it; RV 10.104.8 is why that restraint was correct.

### 4. Only one of the eight metal forts is a named adversary's `PROVISIONAL`

Ten passages of 103 state a material: `āyasá-` "of metal" 8, `aśmanmáya-` "of
stone" 1, `āmá-` "raw, unbaked" 1.

Of the eight metal forts, **one** is the stronghold of a named adversary that
is stormed (RV 2.20.8, the Dasyus'). Two more are an unnamed adversary's
confinement of a bird in the Soma myth (4.27.1, 8.100.8) — arguably hostile, and
counting them so makes it 3 of 8, which changes nothing below. The remaining
five are the worshipper's, a god's, or nobody's: a god asked to protect *with*
them (1.58.8, 7.3.7), priests told to *make* them beside stitching armour and
building a cattle-pen (10.101.8), and twice the fort **is** something else —
**Agni is asked to be one** (7.15.14) and **the river Sarasvatī is one**
(7.95.1).

Two axes are involved and they are not the same, which the first version of
this finding ran together: *whose fort is it* and *is the passage figurative*.
`PUR4J-013` now reports both.

§4J says *"Do not automatically translate pur into a Mature Harappan city."*
This is the measurement behind that instruction. A reading that takes
`āyasá- púr-` as evidence for metal-using fortified settlements has to account
for the seven, not only the one.

### 5. The count is probably formulaic. The passages are not. `PROVISIONAL`

This is the load-bearing distinction, and it is why counts and typology are
separate registers.

**The count.** Four predictions were set for an enumeration reading. **Two fail
decisively**: the expression migrates to another class of object (finding 3),
and two of six 99-passages complete it with "the hundredth", so 99 functions as
one-short-of-a-hundred. A third holds: every count is 7, 90, 99 or 100, across
21 passages, ten books and every Arnold stratum — no 23, no 41. **The fourth,
and strongest, is now INCONCLUSIVE**: it claimed the count is unstable per
opponent, and finding 2 shows Śambara's forts are 99 three times and 100 twice,
which an enumeration that rounds would also produce.

**And one prediction fails for the formula reading too**, in the register's
`evidence_against` column rather than a footnote: the numbers **sort by
narrative cycle**. Seven forts go with Purukutsa and the Pūru in all four of
their passages, near-verbatim at RV 1.174.2b and 6.20.10c; 99 and 100 go with
Divodāsa, Atithigva and Śambara. Ornament does not sort by story. So the reading
rests on **two clear diagnostics of four**, and the supported version is **a
formula system with slots filled by cycle** — narrower than "the numbers are
meaningless", which was the available and convenient answer, and weaker than
this brief first claimed.

**The passages.** **All six passages stating ninety-nine are textual
strongholds** — forts as objects, held and broken. So are both 90-passages and
all four 7-passages; 17 of the 21 counting passages in total. *The number is a
formula* and *the passage is a formula* are different claims, and the evidence
separates them.

---

## The typology, and a structural result about it

All `PROVISIONAL`. 103 passages: **48 textual stronghold · 47 poetic formula · 3
both · 5 that cannot be classified from the text**, and **54 · 47 · 0 · 2 on the
rules alone, before any hand override**. Both columns are published and every
row carries `type_before_override`. Poetic sub-kinds: 27 divine epithet, 9
simile, 6 metaphor, 5 protective formula.

The split is near-even, and it only became so after two corrections. A stress
test of the classifier found that the corpus builds the *fort-breaker* epithet
analytically as well as lexically — `purā́m bhindúr`, `púrāṁ dartaḥ`, `dartā́
purā́m ási` — in **nine of the ten** genitive-plural passages, and those tokens
are simplex `púr-` so the epithet rule could not see them. The reviewer then
found a third metaphor missed the same way (RV 10.87.22, "we set thee, Agni,
around us as a *púr*") and a defect by which an override did not carry its
sub-kind. Neither correction touched a cross-tabulation cell that any finding
above rests on (`PUR4J-029`).

**Where the hand judgements do move a result, it is now stated.** Four of the
nine overrides fall inside the ten material passages — against 0.9 expected
under even allocation — and all four move away from `TEXTUAL-STRONGHOLD`. On the
hand classification 8 of 10 material passages are not plain textual
strongholds; on the rules alone it is 4 of 10. `PUR4J-027` publishes both and
withdraws its first claim to have converged *independently* on finding 4, which
it does not: it re-tabulates the same judgements over the same passages.

**Three of §4J's five types are not properties of a passage at all.** Textual
stronghold and poetic formula are properties of the text. *Inferred geography*,
*archaeological fortification* and *unsupported identification* are verdicts on
an argument someone else must make first — a placement, a site match, an
identification. None can be read off a stanza in any state of knowledge. This
unit has no geographic source and no archaeological source, so all 103 rows
read `NOT ASSIGNED` in those three columns, with the reason on the row.

Assigning them anyway is the exact move the typology exists to prevent.

**The five that cannot be classified are named, not resolved to the likelier
type**: RV 1.149.3 (`nā́rmiṇī-` a proper name for Geldner, an adjective for
Griffith), 2.35.6, 5.66.4 (three translators, three different things), 8.1.28
(**Śuṣṇa's *moving* fort** — `cariṣṇú-` rules out a fixed fortification without
supplying a replacement), 10.138.4.

---

## What "fort" does, under §7

The constitution names **fort** among the categories to audit before use, and
it fails as a default gloss.

- **Grassmann's dictionary** — the gloss that fixed this register's family
  boundary — defines `púr-` as **"Wall aus Steinen und Lehm, Verschanzung,
  Palisade"**: an earthwork. Not a city, not a town, not a fortress.
- **67.5%** of the 83 simplex tokens are accusative. **3.6% — three tokens —
  are locative.** The commonest thing a *púr* does is be the direct object of a
  verb of breaking; it is almost never a place anyone is said to be in.
- Across 103 passages **no translator renders `púr-` as a city**, with one
  exception: Griffith at RV 1.173.10 renders `pū́rpati-` as "some city's lord" —
  the one locator where a political office attached to a *púr* is named, which
  is precisely where an urban reading is most consequential. Geldner has
  *Burgherr*, Grassmann *Burgherrn*. Neither German translator ever writes
  *Stadt*.

**One crux is left open with its consequence named.** Griffith renders `āyasá-`
"iron" in 8 of 8 passages; Geldner renders it "ehern" — of ore, brass, bronze —
in 8 of 8. They are systematically describing different metals, neither argues
it, and the two metals have different histories in South Asia, so a
translator's lexical habit can move a chronology. No source retrieved here
settles it and nothing asserts either reading.

---

## What is on hold, and why

- **`HOLD-006` — poet lineage at full strength.** Geldner's group headings name
  a poet for 55 of 103 passages and a deity or metre for 48. No source
  independent of Geldner was reachable. GRETIL, archive.org and TITUS each
  returned **403 at the proxy** (`SRC-080`–`SRC-083`) having each returned
  **200 earlier the same day** (`SRC-028`, `SRC-025`, `SRC-033`). Same hosts,
  same date, opposite result — `D-042`'s point with a worked instance attached.
- **Proposed geography.** `NOT PRODUCED`. The pinned corpus carries no
  geographic content; `info/rv_locations.tsv`, flagged in the reconciliation
  brief as a candidate, is a citation-format conversion table.
- **`RA-015` — the archival asymmetry.** Every source here sits in one German
  philological line. There is no non-European scholarly source anywhere in the
  unit; Sāyaṇa is not in the pinned corpus and was not retrieved. That is not a
  neutral fact about what exists.

---

## How this brief was corrected

An independent adversarial review before the pull request found eleven
problems. The three that changed a result are in findings 1, 2 and 5 above, and
in the typology section: `PUR4J-007` was false in three of five parts with all
three errors running toward finding 5; the numeral scan was not exhaustive and
its script was uncommitted; and `PUR4J-027` reported only the figure the hand
overrides produce. Five hand classifications were demoted from `VERIFIED` to
`PROVISIONAL`. `BF-014` logs the first as a preferred-counter-narrative failure
of this unit's own §8 test, which interrogated its conclusion instead of
re-deriving its evidence.

Nothing here is presented as though it had always read this way.

## What would change these findings

- **Finding 1** falls if a passage stating a count of forts was missed. The
  first version of this brief said a miss "would have to be a numeral Grassmann
  does not gloss as one" — and that is exactly what happened. The scan reached
  only the 585 of 721 lemmas that carry a gloss, its word boundaries failed on
  German compounds, and it read no Latin, so `śatábhuji-` glossed *centuplex*
  was invisible. `04-AUDITS/rv-pur-numeral-scan.py` now exists, prints its own
  coverage, and returns 26 candidates; four missed lemmas are adjudicated and
  none is a fort count. The live risk is now narrower: `śatábhuji-` agrees in
  full with the fort word at RV 7.15.14 and 1.166.8, and if it were read as
  *a hundred forts* rather than *one hundredfold fort*, 100 would stand at 11
  passages (`PUR4J-032`).
- **Finding 3** weakens if RV 10.104.8 is shown to be a scribal or editorial
  intrusion. It now carries more weight than it did, because finding 2 no
  longer supports finding 5 on its own.
- **Finding 4** changes if the `āyasá-` crux resolves, and changes more if
  `HOLD-001` resolves: admitting `púraṃdhi-` would take the family from 106
  tokens to 156 and enlarge the passage corpus.
- **Finding 5** would be replaced by a two-stage account, not a plural one, if
  the figurative passages proved chronologically or dialectally separable from
  the narrative ones.
- **The whole corpus** rests on the etymological membership test (`PUR-006`).
  On a *semantic* reading of "the complete corpus", six fort-adjacent
  non-`púr-` lemmas — `paridhí-`, `dehī́-`, `saṃdíh-`, `harmyá-`, `ádhr̥ṣṭa-`,
  `dārú-` — belong in it and are excluded by design, and `púr-` tokens in
  passages that are not about forts sit inside the 103 and may not belong.
  Reconciliation C-2, unresolved and not resolved here.
