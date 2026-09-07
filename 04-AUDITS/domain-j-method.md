# Domain J — method, denominators and the two adversarial tests

**Written:** 2026-09-07
**Unit type:** measurement and gate. Registers are the product.
**Specification:** `00-CONTROLLER/METHODOLOGY-CONSTITUTION.md` §4J
**Builds on:** `06-BRIEFS/rv01-reconciliation.md`,
`06-BRIEFS/pur-4j-corpus.md`, `04-AUDITS/rigveda-pur-4j-method.md`
**Script:** `04-AUDITS/rv-pur-nandi-gate.py`
**Registers:** `03-REGISTERS/domain-j-measurements.csv` (16),
`03-REGISTERS/domain-j-interpretations.csv` (3),
`03-REGISTERS/HYPOTHESIS-ELIGIBILITY.csv` `HYP-J-001`

---

## 0. What this unit inherited, and on what terms

The §4J passage corpus was built on branch
`claude/pur-corpus-4j-extension-ux9wdc`. That branch is **not merged to
`main` and had no open pull request**; its work was therefore sitting where
nothing could review or release it. This unit merged it as a base rather than
rebuilding it, and then treated it as work to be reproduced and audited, not as
findings to inherit. `DJ-001` records the reproduction and says in terms what it
is worth.

Nothing in that branch was promoted by being merged. Its claim rows keep the
status they were written with. What this unit adds is in `DJ-`-prefixed rows,
and where it disagrees with the base it says so on the row (`RA-016`, `RA-017`).

---

## 1. Reproduction, and what reproduction is worth

The pinned corpus was re-cloned in this container: HEAD
`d3eb8af7324338161520d2d35eae8f7e985a19a5`, identical to `SRC-019`, `SRC-059`
and `SRC-069`. The seven-script pipeline of `rigveda-pur-4j-method.md` §7A was
re-run end to end. `rv-token-extract.py` reproduced **164,758 tokens over
10,552 stanzas**, and all four registers came out **byte-identical** to the
committed files.

**This tests the pipeline, not the corpus.** Identical code over identical input
must give identical output; what it establishes is that the registers are what
the committed scripts produce and that no step depended on a container that no
longer exists. It is not corroboration and `DJ-001` says so on the row. The
checks that bear on the corpus are `DJ-002` to `DJ-005`, and they were written
without reference to the scripts they check.

---

## 2. Denominators, and every exclusion

No count in this unit is stated without one.

| Measurement | Denominator | Exclusions |
|---|---|---|
| 19 stanzas carry the 99 expression | 10,552 stanzas / 164,758 tokens of the `SRC-022` layer | none — the whole corpus. **But 3 of the 19 do not yield 99 as the quantity of the object** (1.53.9 = 60,099; 10.98.10 = 99 *thousand*; 1.191.13 a genitive plural). Strict denominator 16 |
| 7 of those are in the púr- corpus | the 19 | — |
| 6 of those count forts | the 7; RV 10.104.8 counts streams | — |
| 21 `durgá-` tokens, *most* not a fortification | all `durgá-` in the corpus | `durgáha-` (8), `durgŕ̥bhi-` (1), `durgŕ̥bhiśvan-` (1) are separate lemmas and are not counted. The 21 are at most **15 distinct formulations**: RV 1.106.1–6 is one refrain and 7.60.12 = 7.61.7 verbatim. RV 5.34.7 **is** a fortification on all three translators |
| no lemma glossed "brick" or "city" | **9,196 of 10,031 lemmas (91.7%), covering 78.98% of tokens** | the 835 unglossed lemmas; German probes only |
| 3 of 83 simplex `púr-` tokens are locative | the 83 simplex tokens of `PUR-003` | the 23 compound-family tokens |
| 1 of 6 fort-adjacent lemmas carries the 99 expression | the six of `PUR-006` | — |

Three limits travel with the brick/city absence and are not optional. The 835
unglossed lemmas are overwhelmingly verbal roots and particles (`√as- 1`,
`√kr̥-`, `√dhā- 1`, `√bhū-`, `íd`), so the gap is unlikely to hide a noun — but
it is not empty. The probes are German because the gloss column is German, and
**exactly one** gloss in the corpus is Latin — `śatábhuji-` "centuplex" — which
no German probe reaches. And per `DEP-005` the lemmatisation and the gloss are
**one source**, so this is a gloss column reporting an absence, not the corpus
doing so unmediated.

**That gloss column is not Grassmann's dictionary, and this note said it was
until adversarial review.** `SRC-089` reads the TEI header: it is column V,
`LEMMA_ZÜRICH_BEDEUTUNG`, the Zürich lemma-meaning column over Lubotsky's text,
revised 2020–2024, citing Geldner in 181 lemmas, Grassmann *marked off as
`GM:`* — one view among others — in 181, and EWAia/Mayrhofer in 83. Grassmann
1873 cannot cite Mayrhofer 2003. Grassmann's actual *Wörterbuch* has never been
retrieved in this repository. `BF-017`, `DEP-026`, `RA-018`.

**And a fourth limit, found only at the second review, bounds what may be
probed here at all: the gloss column has ZERO coverage of verb roots** — 0 of
700 root lemmas carry a meaning field, 32,025 tokens, **19.4% of the corpus**,
including `√takṣ-` "hew, fashion" (78) and `√mā- 1` (90). A probe of this
column for `bauen`, `errichten` or `zimmern` returns a guaranteed zero whatever
the corpus contains. `DJ-008`'s own absences survive it — *brick* and *city*
are nouns and the nominal lexicon is covered — but **no negative about an
action or process is available from this source**, and `DJ-009`'s first repair
reported exactly such a zero as a finding. `BF-018`, `RA-021`.

**What the corpus does carry, correctly stated.** `pakvá-` "gekocht, gebacken"
(25) against `āmá-` "roh, ungekocht" (11) is a **culinary** pair — all 25
`pakvá-` are food, and 8 of the 11 `āmá-` are one raw-cow/cooked-milk formula.
RV 2.35.6 extends the raw term to a *púr* **once**, and that once is the
finding. Calling the pair "the fired/unfired opposition brick technology turns
on" was an unmeasured leap and is withdrawn. `DJ-009`, `BF-018`.

---

## 3. Measurements and interpretations are in different files

`domain-j-measurements.csv` holds counts, distributions and case profiles.
`domain-j-interpretations.csv` holds three readings, each with an
`evidence_against` column that is populated and load-bearing. `HYP-J-001` holds
the gate.

The separation is not filing. `DJ-006` (3.6% locative) and `DJ-007` (none of
the three locatives asserts habitation) are measurements that an urban reading
would have to answer. `DJ-I-02` is where the inference is drawn, and it draws
the **opposite** of the available one, because the two similes presuppose the
inhabited fort the corpus never asserts.

The separation did real work and it was not sufficient. It let the second
reading survive the first — but `DJ-009` and `DJ-011` were *interpretations
shipped in the measurements file*, at `VERIFIED`, and the file boundary did not
catch either. Both are now `PROVISIONAL`. A row in a measurements register is
not a measurement because of where it sits; it is a measurement if something
was counted, and for those two rows nothing was.

---

## 4. The gate, and why its verdict is what it is

`HYP-J-001` gates the thesis of R. N. Nandi, "The City and the Citadel"
(Routledge 2017), which §4J's prohibition — *"Do not automatically translate
pur into a Mature Harappan city"* — is written against.

**The chapter is not read.** Every publisher, DOI-resolver, repository and
bibliographic-API host is `EGRESS_BLOCKED` on both available channels
(`SRC-087`), and the chapter is paywalled besides (`D-046`, `HOLD-007`). What
was gated is the thesis as the publisher's abstract states it, reached through
a search index (`SRC-086`). The only content taken from it is the four-term
list, used to decide *which terms to test*.

The verdict is **`NOT-ELIGIBLE-SOURCE-BLOCKED`**, and the suffix is the whole
finding:

- **Two legs could not be run at all.** Chronology needs an absolute date for
  the fort passages; this repository has only Arnold's relative strata,
  single-sourced (`DEP-001`). Geography needs the corpus to place a passage
  somewhere; it carries no geographic content. These are the two legs the
  thesis most depends on, and no amount of corpus work supplies them.
- **The legs that ran cut both ways, and after review they cut less sharply
  against the thesis than the unit first wrote.** Of six diagnostic
  predictions, three verdicts were withdrawn on review and **all three moved
  toward the thesis**: the brick and city legs are `INCONCLUSIVE` rather than
  failed, because Renou supplies both words at RV 2.35.6 and 1.173.10
  (`DJ-013`) and the corpus carries the fired/unfired pair (`DJ-009`); and the
  four-term leg is no longer "fails in two of four", because `durgá-` is
  contested rather than failed (`DJ-011`) and the term list itself is on `HOLD`
  (`DJ-010B`). One leg survives intact and tells against the thesis: the counts
  (`DJ-I-01`). On the other side, `vr̥jána-` supports "politically administered
  territory" — though *"politically administered"* is Nandi's phrase and the
  gloss says a community's *territory*, which is a bridge, not a reading. And
  `pū́rpati-` "lord of the fort" is one token, inside a simile (`DJ-014`).

**This is not a finding that Nandi is wrong, and it must not be reported as
one.** It is a finding that this repository cannot adjudicate the thesis, and
can say exactly why: no archaeological source, no absolute chronology, no
geography, one gloss column behind every lexical result, and a four-term list
that may be a search engine's paraphrase rather than Nandi's (`DJ-010B`).

---

## 5. The two adversarial tests

Both were run before this note was first written. **Both then failed to catch
what an independent reviewer caught afterwards**, and that is recorded here
rather than quietly repaired, because a method note claiming two clean catches
would misdescribe how this unit actually went.

### Prestige-bias challenge

*Did this privilege a claim because it is canonical, Sanskritic, Brahmanical,
Indo-European, European, colonial, institutionally prestigious, repeatedly
cited or nationally useful?*

**Run, and it produced a false result in the unit's favour.** The test
concluded that every lexical result rested on "Grassmann 1873, a
nineteenth-century German dictionary", and that the unit had used a European
philological lexicon to adjudicate a term list from an Indian scholar whose
chapter it could not read. The asymmetry it named is real. **The source was
not.** `SRC-089` reads the TEI header: the gloss field is the Zürich
lemma-meaning column, a modern composite citing Geldner, EWAia/Mayrhofer,
Scarlata, Oldenberg, Lubotsky, Renou and Kuiper, with Grassmann marked `GM:`
where followed. Grassmann's *Wörterbuch* has never been retrieved here.

The error is worth stating precisely because of its direction: **the unit
performed a self-criticism that was more flattering than the truth.** "One
nineteenth-century German lexicon" made the results against Nandi look
appropriately hedged while understating how much modern apparatus they lean on
— and it substituted a confession for a retrieval. `BF-017`, `DEP-026`,
`RA-018`.

The second failure was the same move in a different place. `RA-015` and this
section both recorded "one philological line" as an archival limitation.
**Renou (`SRC-076`) and Elizarenkova (`SRC-075`) were ledgered, retrieved, and
sitting in the same clone.** `rv-pur-nandi-gate.py` read three translators and
disclosed the fourth and fifth as a limitation instead of opening them. Renou
supplies *"forteresses (en briques) crues"* at RV 2.35.6 and *"maître de la
cité"* at RV 1.173.10 — **brick and city, the two words the unit reported as
absent, at the two locators where it matters most** (`DJ-013`). A disclosure is
not a correction, and where the check is free the disclosure is a substitute
for work.

What remains true and uncorrected: there is still no non-European scholarly
source anywhere in this unit and no archaeological source at all. Sāyaṇa is not
in the pinned corpus and was not retrieved. `RA-015`, `APA-J-002`.

A third form was caught by the unit itself and stands: `DJ-001`'s reproduction
arrives with a commit hash and a byte-identical diff, and none of that is
evidence about the Rigveda. The row says so — and it also cannot compare prose
to register, which is how the modal-count error at `RA-019` survived it.

### Preferred-counter-narrative challenge

*Did this accept a claim too easily because it is Dravidian, Indigenous,
anti-colonial, anti-Brahmanical, subaltern, diffusionist or politically
corrective?*

**Run, caught one real thing, and missed two larger ones in the same
direction.**

**`BF-016`, the genuine catch.** A draft of `DJ-I-02` read: the Rigveda has no
word for brick and no word for city, therefore a *púr-* is not a Harappan-style
city. Deflationary, quotable, congenial to a record trying not to be captured
by an Indus-identification narrative, and free. Corrected from inside the
passages the convenient reading cites: RV 6.2.7 "like an old man in a fort" and
RV 9.107.10 "as a body of troops enters the fort" are **similes**, and a simile
draws on the ordinary, so both presuppose the inhabited fort the corpus never
asserts.

**What it missed, `BF-017`.** The correction it applied — typing the brick
absence `NOT PRODUCED` on the ground that the corpus "nowhere describes
construction technique for any structure" — was itself an unmeasured assertion,
shipped at `VERIFIED`. Measured afterwards, it is wrong: the corpus carries
`pakvá-` "gebacken" (25) against `āmá-` "roh, ungekocht" (11), which *is* the
brick-technology opposition, and puts the unfired term on a fort. **The
mechanism that rescued the unit from an unearned deflation was itself
unearned.**

**And it missed the load-bearing one.** `DJ-011` shipped at `VERIFIED` claiming
no `durgá-` is ever "broken, besieged, entered or held" — the strongest single
result against the gated thesis. At RV 5.34.7 all three cited translators,
Grassmann included, render a fortified place people hold out in. An absolute
quantifier over 21 passages, contradicted by a file already retrieved and
already cited, in the direction the unit preferred. `RA-020`.

**`BF-015` is not a catch of this test and the earlier version of this note
filed it as one.** The silent-zero `náva-` query is a coding defect in the
unit's own script, found by ordinary sanity-checking — testing a zero against a
known-positive case — not by an adversarial challenge. Its bias *direction* is
still worth the row: the result it manufactured was a debunking of correct
prior work, which flatters a session auditing someone else's register.

### The second round, and why it matters more than the first

An independent re-review of the repairs closed ten of seventeen findings and
raised three new ones — **all in the repair commit itself, and all running the
opposite way from the first round.** Written while correcting an over-deflation,
they overstated the case *for* the gated thesis: a guaranteed-zero verb probe
reported as an absence, a translator's bracketed supplement quoted as the text,
and a culinary word-pair called construction vocabulary. `BF-018`.

The first of those is the sharpest thing in this file. `BF-015` had already
logged the guaranteed-zero failure mode and written its own control — *"any
search returning zero is to be tested against a case known to be positive
BEFORE the zero is reported."* That control was not obeyed, in the row written
to repair `BF-016` and `BF-017`. **A `future_control` that is not checked makes
the bias log decorative**, and this unit has now demonstrated it.

### What the tests did get right

`DJ-I-01` widens the formulaicity control from one stanza to twelve, which
strengthens a deflationary conclusion — so its `evidence_against` column
carries the finding that cuts against it: the numbers **sort by narrative
cycle**, and ornament does not sort by story. That hedge survived review. So
did the gate's verdict: `HOLD` with
`NOT-ELIGIBLE-SOURCE-BLOCKED`, and the insistence throughout that this is not a
finding that Nandi is wrong. What did not survive was the evidence under two of
its legs.

### The general lesson, for the next unit

Three of the four failures above share a shape: **the unit disclosed a
limitation instead of running the check that would have removed it**, and each
disclosure made the record look more scrupulous while leaving the favourable
error in place. A limitation that can be closed by reading a file already in
the clone is not a limitation. It is unfinished work with a caveat on top.

## 6. What this unit did not do

- **Did not read Nandi.** `HOLD-007`, `D-046`.
- **Did not retrieve any archaeological source, geography or absolute
  chronology.** These are the three things the identification question turns on
  and this unit has none of them. `HYP-J-001` fails two legs for want of them.
- **Did not resolve reconciliation C-2 or C-4.** `DJ-005` makes C-2 concrete —
  six 99-passages on the etymological reading, seven on the semantic one — and
  queues it as `RA-016`. Choosing is the owner's.
- **Did not re-run the counts, fields or typology registers** over a semantic
  corpus. That is `RA-016`'s work and it depends on the ruling.
- **Did not test whether the twelve non-fort uses of the 99 expression cluster**
  by book, poet or stratum. If they do, `DJ-I-01` weakens. `RA-017`.
- **Did not run step 13** against `melakeela/site`. The site is not in this
  session's repository scope.
