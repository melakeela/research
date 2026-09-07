# Domain J — method, denominators and the two adversarial tests

**Written:** 2026-09-07
**Unit type:** measurement and gate. Registers are the product.
**Specification:** `00-CONTROLLER/METHODOLOGY-CONSTITUTION.md` §4J
**Builds on:** `06-BRIEFS/rv01-reconciliation.md`,
`06-BRIEFS/pur-4j-corpus.md`, `04-AUDITS/rigveda-pur-4j-method.md`
**Script:** `04-AUDITS/rv-pur-nandi-gate.py`
**Registers:** `03-REGISTERS/domain-j-measurements.csv` (12),
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
| 19 stanzas carry the 99 expression | 10,552 stanzas / 164,758 tokens of the `SRC-022` layer | none — the whole corpus |
| 7 of those are in the púr- corpus | the 19 | — |
| 6 of those count forts | the 7; RV 10.104.8 counts streams | — |
| 21 `durgá-` tokens, none a fortification | all `durgá-` in the corpus | `durgáha-` (8), `durgŕ̥bhi-` (1), `durgŕ̥bhiśvan-` (1) are separate lemmas and are not counted |
| no lemma glossed "brick" or "city" | **9,196 of 10,031 lemmas (91.7%), covering 78.98% of tokens** | the 835 unglossed lemmas; German probes only |
| 3 of 83 simplex `púr-` tokens are locative | the 83 simplex tokens of `PUR-003` | the 23 compound-family tokens |
| 1 of 6 fort-adjacent lemmas carries the 99 expression | the six of `PUR-006` | — |

Three limits travel with the brick/city absence and are not optional. The 835
unglossed lemmas are overwhelmingly verbal roots and particles (`√as- 1`,
`√kr̥-`, `√dhā- 1`, `√bhū-`, `íd`), so the gap is unlikely to hide a noun — but
it is not empty. The probes are German because Grassmann wrote German, and a
handful of his glosses are Latin and are not reached. And per `DEP-005` the
lemmatisation and the gloss are **one source**: this is Grassmann's lexicon
reporting an absence, not the corpus doing so unmediated.

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
inhabited fort the corpus never asserts. Keeping them apart is what let the
second reading survive the first.

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
- **The legs that ran cut both ways**, and the register records both
  directions. Two of Nandi's four terms do not denote fortified settlements on
  the lexicon in hand (`DJ-010`, `DJ-011`); one, `vr̥jána-`, supports his
  "politically administered territory" directly; `pū́rpati-` "lord of the fort"
  is a real if single-token piece of positive evidence for the same.

**This is not a finding that Nandi is wrong, and it must not be reported as
one.** It is a finding that this repository cannot adjudicate the thesis, and
can say exactly why: no archaeological source, no absolute chronology, no
geography, and one nineteenth-century German lexicon standing behind every
lexical result.

---

## 5. The two adversarial tests

Both were run before this note was written, and both caught something. The
catches are logged as `BF-015` and `BF-016`, not described only here.

### Prestige-bias challenge

*Did this privilege a claim because it is canonical, Sanskritic, Brahmanical,
Indo-European, European, colonial, institutionally prestigious, repeatedly
cited or nationally useful?*

**Caught, and not fully correctable.** Every lexical result in this unit is
Grassmann 1873 — a nineteenth-century German dictionary — and the unit used it
to adjudicate a term list from an Indian scholar whose chapter it could not
read. That is a European philological lexicon sitting in judgement on a
non-European reading of the same text, and the asymmetry is not neutralised by
noting it.

What was done: `DEP-021` and `DEP-022` cap every such result at a statement
about Grassmann rather than about Rigvedic meaning; `APA-J-002` records the
asymmetry as an archive finding; `HYP-J-001`'s `independent_support` column
states plainly that the gate "has heard the case for the identification only as
its opponent's lexicon states it"; and the verdict carries `SOURCE-BLOCKED`
rather than `NOT-ELIGIBLE` for exactly this reason. `RA-015` already queued the
absence of any non-European source in this domain and stands.

What was **not** done and would be the real correction: Sāyaṇa. The one
pre-modern commentary that sits outside the European line is not in the pinned
corpus and was not retrieved. `DJ-011` — the strongest single result against
Nandi's term list — would be a different claim if a pre-modern commentator read
`durgá-` as a fortification in those 21 passages.

A second form of the same bias was caught earlier: the reproduction in `DJ-001`
arrives with a commit hash, a byte-identical diff and a seven-script pipeline,
and none of that is evidence about the Rigveda. The row says so.

### Preferred-counter-narrative challenge

*Did this accept a claim too easily because it is Dravidian, Indigenous,
anti-colonial, anti-Brahmanical, subaltern, diffusionist or politically
corrective?*

**Caught twice.**

**`BF-016`, the substantive one.** A draft of `DJ-I-02` read: the Rigveda has no
word for brick and no word for city, therefore a púr- is not a Harappan-style
city. Deflationary, quotable, congenial to a record trying not to be captured
by an Indus-identification narrative, and free — it needed no further evidence.
It was also an untyped absence in a German dictionary converted into a fact
about Bronze Age architecture. Corrected by typing the absence twice
(`DJ-009`: `ABSENT DESPITE ADEQUATE SEARCH` for the lexicon, `NOT PRODUCED` for
the historical question) and by reading the three locative passages properly:
RV 6.2.7 "like an old man in a fort" and RV 9.107.10 "as a man enters the fort"
are similes, and a simile draws on the ordinary — so both **presuppose** the
inhabited fort the corpus never asserts. The strongest evidence against the
convenient conclusion was inside the passages the convenient conclusion cites.

**`BF-015`, the instrument one.** The independent re-derivation of the six
99-passages first returned **zero**, appearing to debunk a correct register —
the flattering direction for a session auditing someone else's work. The cause
was a silent-zero query: the corpus disambiguates `náva- 1` "nine" from
`náva- 2` "new", and a search on a bare `náva-` matches neither. Caught by
testing the zero against a known-positive case before reporting it. Logged
because a broken search is how an archival silence gets manufactured, and the
negative-evidence standard is worthless if the search itself is broken.

**What the second test did *not* find.** It did not find that the unit went
easy on the deflationary reading of the counts. `DJ-I-01` widens the
formulaicity control from one stanza to twelve, which strengthens a
deflationary conclusion — so its `evidence_against` column carries the finding
that cuts against it: the numbers **sort by narrative cycle** (7 with Purukutsa
and the Pūru, 99 and 100 with Divodāsa and Śambara), and ornament does not sort
by story. The row states that a quantity used for twelve kinds of object is
still doing something when it is chosen.

---

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
