# Domain M — the six models, the North Dravidian measurement, and the Balochi chronology

**Unit:** domain M run under the fourteen-step method, 2026-09-07, building on
the measurements PR #16 left in the register.
**Registers:** `03-REGISTERS/domain-m-measurements.csv` (DMM-001…022),
`domain-m-interpretations.csv` (DMI-001…012),
`domain-m-model-gates.csv` (DMG-1…6),
`domain-m-balochi-chronology.csv` (DMC-001…006).
**Script:** `04-AUDITS/domain-m-dedr-north-dravidian.py`.
**Method failures:** `BF-007`, `BF-008`, `BF-009`.
**Re-audits:** `RA-006`, `RA-007`, `RA-008`.
**Holds:** `HOLD-005` opened; `HOLD-002` and `HOLD-004` narrowed, both still open.
**Owner decisions:** `D-038`, `D-039`, `D-040`, `D-041`.

---

## 0. The headline, stated before the argument

**No §4.M model was closed and none was allowed to be.** All six read
`CANNOT-GATE`, never `FAIL`, and each gate row names the criterion that could
not be applied and the source that would supply it (`DMG-1` … `DMG-6`).

What *did* change is the instrument. PR #16 measured North Dravidian on
`DravLex`, a 100-concept wordlist, and said in its own header that this was the
wrong instrument. This unit measured it on **DEDR** — Burrow and Emeneau's
comparative dictionary, 5,520 entries, 26 languages — reached through a
re-encoding on GitHub because GitHub is the one host that answers. That is the
first Dravidian etymological dictionary read in this project.

---

## 1. Bound the question (step 1)

**Propositions under test.** (a) Do Brahui, Kurukh and Malto form a subgroup,
and does the evidence for the node that attaches Brahui differ in kind or in
strength from the evidence for the node that joins Kurukh and Malto?
(b) When did Balochi expand into Balochistan, on the retrievable record?
(c) What Indo-Aryan and Balochi contact layers are measurable in Brahui?
(d) Which of the six §4.M models does any of this bear on?

**The null explanation, carried throughout.** That the observed exclusive
sharing is what the attestation frequencies alone would produce. This is not
a rhetorical null: it is implemented, and §4 reports it.

**Four histories, separated at the register level and not only in prose.**
Language history, speaker ancestry, political and tribal identity, and
loanword history. `DMM-015` dates a confederacy and says so; `DMM-020` is
ancestry and says so; `DMC-002` and `DMC-006` carry a `which_of_the_four_histories`
column because the chronology register is where they are most likely to be
run together. `BF-008` is what happened when they were not kept apart.

---

## 2. Chronology and geography before comparison (steps 2, 3)

The chronology of this domain is the problem, not the background. Every dated
statement retrieved is in `03-REGISTERS/domain-m-balochi-chronology.csv`, with
a column for what each one actually dates and a column for the hedge in the
source. Six rows. The summary:

- **One linguist-authored date frame**, and it is a 500-year window offered as
  what is "generally thought" — Balochi arriving from the northwest in waves
  between 1000 and 1500 AD (`DMC-001`).
- **One precise chronology**, and it is political: the fifteenth-century Rind
  and Lāshār migration from western Makran, Mīr Chākar Khān Rind ruling from
  Sibi 1487–1511 (`DMC-002`). It falls inside the first window and dates a
  different object.
- **One relative chronology**, retrieved as full text with a resolvable DOI,
  placing Balochi as transitional between Northwest and Southwest Iranian
  (`DMC-004`).
- **One statement that the pre-modern record cannot support a chronology at
  all**, from authors working inside Baloch historiography (`DMC-005`).
- **One community-authored, oral-historical migration date**, recent and
  westward, held at `HOLD` pending the rights steward (`DMC-006`).

**Nothing retrieved dates Brahui.** Not its arrival, not its presence, in
either direction, at any period. That single fact is why all six models read
`CANNOT-GATE`: the chronological criterion cannot be applied at all. Absence
of a date is not a failed date check.

**Geography.** Unchanged from PR #16 and not re-measured: Brahui's nearest
attested Dravidian neighbour is Kolami at 1,561.5 km (`DMB-010`, `DMB-011`).
`DMI-011` is a standing row keeping the unknown ancient Balochistan speech
zones visible, as §4.M requires — written as its own row rather than as a
caveat precisely so that it cannot be dropped when this is summarised.

---

## 3. Evidence classes, inventoried separately (step 4)

| class | what was retrieved | what it can carry |
|---|---|---|
| lexical / comparative | DEDR re-encoding, 5,520 entries (`SRC-059`) | cognate-set membership; nothing about dates |
| Indo-Aryan comparative | CDIAL re-encoding, 604 cross-references (`SRC-059`) | where Turner chose to compare; not contact |
| phonological | Cathcart 2022 full text (`SRC-072`); Nair 2003, McAlpin 2003 at abstract | Balochi's position; one withdrawn ND isogloss |
| morphological | Kobayashi & Tirkey 2019 at abstract (`SRC-063`) | the one statement of the lower node's morphology |
| historical / textual | Spooner, Badalkhan, Ahmed et al. at abstract | the Balochi date frame and its own limits |
| population-genetic | Singh et al. 2025; four HLA/mtDNA papers | speaker ancestry, and nothing else |
| community-authored | three Al-Burz papers, one Makhz paper | held at ledger level pending `D-041` |

No class borrowed certainty from another. The one place that nearly happened
is logged as `BF-008`.

---

## 4. The measurement (steps 5, 8)

### 4.1 The instrument, and why the null had to hold two margins

Brahui is attested in **269** of 5,520 DEDR entries; Kurux in **775**, Malto
in **704** (`DMM-001`). A raw comparison of exclusive-sharing counts would
therefore be measuring attestation frequency. The randomisation is a
**curveball** trade that holds *both* margins fixed — every entry keeps its
number of attesting languages, every language keeps its number of entries —
so the question it answers is: *is this more co-occurrence than the marginals
force?* 2,000 draws, 100,000 swaps per draw, seed 20260907.

### 4.2 What it returned

| statistic | observed | null mean | 5th–95th | p(≥ obs) |
|---|---|---|---|---|
| Kurux + Malto exclusive | **176** | 0.71 | 0–2 | 0.0005 |
| Brahui + Kurux + Malto exclusive | **7** | 0.00 | 0–0 | 0.0005 |
| Brahui + Kurux exclusive | **1** | 0.19 | 0–1 | 0.17 |
| Brahui + Malto exclusive | **1** | 0.18 | 0–1 | 0.17 |
| confined to North Dravidian | **193** | 5.38 | 2–9 | 0.0005 |

`0.0005` is `1/2001` and is the **floor** at 2,000 draws. It means *never
reached*, not *exactly this probability*, and `DMI-004` says so on the record.

**The randomisation was checked rather than assumed.** Re-running
`curveball()` against the loaded matrix and comparing margins directly:
the multiset of row sums is preserved exactly, every column sum is
preserved exactly, and 5,418 of 5,520 rows differ from the original after
50,000 swaps — so it is randomising and not merely shuffling within rows.
Every headline count was also recomputed from the raw entry-to-language
mapping by code written separately from the script, and agrees: 176, 7, 1,
1, 193, and 269 Brahui entries of which 260 reach outside North Dravidian.

Both halves are reported at equal weight, which is the discipline the numbers
require rather than a gesture:

- The upper node is **not empty**. Seven etymologies is small, and it is
  reported as seven and not as "rank 20 of 2,600" — reporting the rank first
  would repeat `BF-004`. But the null expectation is effectively zero: with
  Brahui in 269 entries, chance produces no such triples at all. Seven is
  real and thin. The seven are listed by DEDR number in `DMM-003`.
- Brahui's **pairwise** sharing with Kurux, and with Malto, is
  **indistinguishable from chance** (`DMM-004`). Whatever supports the upper
  node here is carried entirely by three-way sets.

### 4.3 The number that matters most

**260 of Brahui's 269 DEDR etymologies reach outside North Dravidian**
(`DMM-005`). Brahui's membership of the Dravidian family, in this dictionary,
does not rest on the North Dravidian node at all. `DMI-003` draws the
consequence: doubting the node is not a step toward doubting that Brahui is
Dravidian — and `DMM-012` has McAlpin saying the same from the other side,
that no serious scholar denies the connection and the problem is in the
details.

### 4.4 The instrument checked against published counts

| published | source | measured here |
|---|---|---|
| 515 Kurux–Malto shared etyma | Kobayashi & Tirkey 2019 | 509 |
| 175 of them isolated | Kobayashi & Tirkey 2019 | **176** |
| 195-item Kurux/Malto/Brahui list | unattributed BSOAS review | 193 |

This **verifies the parse and nothing else** — these are counts taken *from*
DEDR being re-taken *from* DEDR (`DEP-013`). Presenting them as three
confirmations of the subgroup was drafted and is logged as `BF-009`. What
they establish is that `DMM-001`–`DMM-005` are reading Burrow and Emeneau
correctly rather than a corrupted file, which is worth having and is all it is.

### 4.5 Source genealogy, and why this is not a replication of PR #16

`DravLex` and DEDR both descend from the Burrow and Emeneau cognate
judgements (`DEP-012`), and `DravLex` is the Kolipakam et al. 2018 dataset
(`DEP-015`). Agreement between PR #16 and this unit is **expected and is not
corroboration** (`DMI-006`). What differs is scale and purpose: 100 concepts
chosen for basic vocabulary against 5,520 entries built to record everything
the compilers judged cognate. That is why DEDR finds 7 where `DravLex` found
2, and why only DEDR is large enough to have a null at all.

Deeper still: Emeneau states that his Brahui material is Bray 1909 and 1934
plus "no more than eight hours" of contact with speakers in 1936 (`DMM-021`).
DEDR's Brahui entries, Emeneau 1962 and Emeneau 1997 are **one chain**
(`DEP-011`). So `DMM-001`–`DMM-005` measure how one pair of scholars
distributed one earlier scholar's Brahui lexicon across the family.

---

## 5. What could not be measured, typed (step 6, negative-evidence standard)

| absence | type | bound |
|---|---|---|
| Balochi loan annotation in the DEDR encoding (zero lines) | **NOT PRODUCED** | the encoding carries form and gloss fields only; DEDR itself says more |
| Brahui in CDIAL (1 line in 159,756) | **ABSENT DESPITE ADEQUATE SEARCH** | strictly to that dictionary; Turner compared across families 604 times |
| Korn 2005, Elfenbein 1998, Emeneau 1962, Krishnamurti 2003 | **NOT ACCESSIBLE** | no reachable connector's corpus holds them |
| ancient Balochistan speech zones | **NOT RECOGNIZED / NOT EXCAVATED** | not the kind of thing the retrieved instruments record |
| Al-Burz full text | **NOT ACCESSIBLE** | indexed and abstract-readable; publisher host unreachable (`D-039`) |

None of these is a finding about contact, about Brahui, or about the models.
`HOLD-005` exists so the first three cannot later be read as one.

---

## 6. The archive audit (step 6, §4.V)

Three measurements, and together they are the shape of the evidence base:

- Two questions posed in strictly **linguistic** terms returned **population
  genetics** as the plurality of full-text matches (`DMM-018`).
- The standard Indo-Aryan comparative dictionary names Brahui **once** in
  159,756 lines (`DMM-009`).
- The Brahui data under the standard Dravidian etymological record is one
  scholar's publications plus **eight hours** of fieldwork (`DMM-021`).

Brahui is **heavily sampled as a population and thinly documented as a
language** (`DMI-012`). That asymmetry makes genetic answers easy to retrieve
and linguistic answers hard, on a question the constitution says genetics
cannot settle. It is §4.M's trap — living people used as linguistic fossils —
appearing as a property of the archive before any analyst has erred.

And the community-authored scholarship that exists is **indexed but
unreadable** from here: three *Al-Burz* papers were located through a
connector while every University of Balochistan host returns no connection
(`SRC-058`, `D-039`).

---

## 7. Gating the six models (step 7), before any space was allocated

All six read **`CANNOT-GATE`**. The verdict is uniform; the reasons are not,
and `03-REGISTERS/domain-m-model-gates.csv` records per-model chronological
fit, geographical fit, mechanism, positive evidence, contrary evidence,
diagnostic predictions and what would gate it.

- **`DMG-1` northwestern survival.** No source dates Dravidian speech in
  Balochistan. `DMM-005` is weakly consistent and equally fits `DMG-2`,
  `DMG-3` and `DMG-5`. Highland refugia unexamined.
- **`DMG-2` later long-distance migration.** §4.M forbids treating this as
  documented fact and nothing retrieved documents it; Elfenbein 1998 is still
  unread. Its row explicitly refuses `DMC-006` as support: that migration is
  westward, out of Pakistan, in the modern period — wrong direction, wrong
  date. Its being the disfavoured model is not a reason to gate it out either.
- **`DMG-3` broader ancient distribution then replacement.** Most exposed to
  the negative-evidence standard: it can only be argued from typed absences,
  and no absence here has been typed in its favour.
- **`DMG-4` dialect networks then fragmentation.** *Best served by what was
  retrieved.* `DMM-011` (a North Dravidian isogloss withdrawn as areal) and
  `DMM-010` (few identified shared innovations) describe exactly the situation
  it predicts. That is a reason to gate it properly when sources arrive, not
  to advance it now.
- **`DMG-5` small group plus local adoption.** Carries its own warning: a
  genetic null *looks like* its prediction and does not confirm it.
- **`DMG-6` complex combinations.** A different case in kind. It is held open
  as §4.M requires, but a combination that forbids no observation is not yet
  one hypothesis and cannot pass a step 7 gate. Flagged as needing
  decomposition — a *named* combination with an order and dates can be gated;
  the residual cannot, and letting it absorb every result is the role §6
  forbids "unknown" to play.

**Proportional space allocated: none, to any model** (step 9). That is what
follows from six `CANNOT-GATE` verdicts.

---

## 8. Bridges tested separately (step 10)

- **Shared vocabulary → shared descent.** Not licensed. `DMI-002`: Kurux and
  Malto are neighbours, and exclusive lexical sharing is what both a recent
  common ancestor and long contact produce. The 176 sets establish that the
  count is not an attestation artefact; they do not establish inheritance.
  The thing that would separate them is `DMM-010`'s shared inflectional
  morphology — which is why an abstract with no page locator carries more
  weight for the lower node than this unit's own measurement does.
- **Genome → language.** Not licensed, in either direction (`DMI-009`,
  `BF-008`). The clearest statement of this in the unit is quoted from a
  population-genetics paper against its own subject matter.
- **Subgroup → history.** Not licensed. A clade can arise by survival,
  migration, fragmentation or adoption (`DMI-001`, `DMI-010`).
- **Tribal confederacy → language spread.** Not licensed (`DMC-002`).

---

## 9. Current standing (step 11)

The question is **open in the specialist literature, and open in a specific
way**: the lower node is not in doubt, the upper placement is much debated,
and the stated difficulty is a *shortage of identified shared innovations*
rather than a positive case against (`DMM-010`). At least one named isogloss
has been withdrawn in print (`DMM-011`). Brahui's Dravidian membership is not
in dispute (`DMM-012`). A Bayesian phylogeny recovers the four branches while
reporting "considerable uncertainty with regard to the relationships between
the main branches" (`DMM-013`).

Citation inertia was checked in the one place it was checkable: `DEP-008`
found Glottolog's North Dravidian node citing Krishnamurti 2003 and nothing
else. This unit adds that the counts everyone quotes for Kurux–Malto trace to
DEDR, and that DEDR's Brahui material traces to Bray (`DEP-011`). The
apparent multiplicity of support is thinner than it looks.

---

## 10. Falsifiers (step 12)

- `DMM-002` and `DMM-003` would be **overturned by a parse error** — ruled out
  to the extent §4.4 rules it out — or by a later Jambu commit changing the
  encoding. The script pins commit `dbae3102`; re-pin and re-run rather than
  assuming the numbers carry.
- **`DMI-001` and `DMI-002` would be settled** by Krishnamurti 2003's list of
  North Dravidian innovations: if the innovations are phonological and several
  rest on Brahui, the thin lexical result is beside the point and the upper
  node stands on other evidence. If few or none rest on Brahui, `DMM-004`
  gains weight.
- **`DMI-003` would be overturned** by a demonstration that the 260
  non-North-Dravidian Brahui etymologies are largely loans or chance
  resemblances — which is a question about DEDR's inclusion criteria and needs
  DEDR's prose.
- **`DMC-001` would be displaced** by any dated attestation of Balochi or of
  Brahui in the region, of any kind.
- **Any of the six models would become gateable** by an absolute chronology
  for Brahui. There is none.

---

## 11. Checking this repository against itself (step 13)

The site is not in this repository, so step 13 ran against the registers.

- **`DMB-019`** (PR #16) found two exclusive Brahui–Kurukh–Malto sets in
  `DravLex`: *horn* and *smoke*. DEDR gives seven, and **`smoke` (DEDR 5131)
  is among them; `horn` is not exclusive in DEDR.** Not a contradiction —
  different instruments at different scales — and recorded in `DMM-003` so it
  is not read as one. `DMM-003` also notes that DEDR 5131's Brahui form is
  cited inside DEDR to Emeneau's own later publication.
- **`DMB-023`** said no inference from McAlpin 1980's title was licensed.
  That stands: `SRC-065` is McAlpin **2003**, not 1980. It is supplemented,
  not superseded, and no row was rewritten.
- **`DMB-026`** refused both verdicts on the subgroup and stays `PROVISIONAL`.
  This unit does not promote it: `DMM-003` and `DMM-004` are new measurements
  on a better instrument, and `HOLD-004` still blocks the verdict.
- **`DMB-006`**, the flag that the leave-one-out design presupposed models 2
  or 5, is unaffected and is why `DMG-2` is written as carefully as it is.
- **No row was deleted.** No `REJECTED` row was touched.

---

## 12. The two adversarial tests (§8)

### Prestige-bias challenge

*Did this privilege a claim because it is canonical, Indo-European, European,
colonial, institutionally prestigious or repeatedly cited?*

**One exposure, corrected.** DEDR is the canonical instrument of Dravidian
comparative linguistics, and the draft treated a measurement taken from it as
a measurement of Dravidian. It is a measurement of Burrow and Emeneau's
judgements, whose Brahui component rests on Bray plus eight hours of contact
(`DMM-021`, `DEP-011`). Every DEDR-derived interpretation is capped at
`PROVISIONAL` on the ground that it inherits a single framework.

**One exposure, declined.** Reproducing three published counts to within 6, 1
and 2 is the most satisfying result in the unit and the most misusable. It
verifies the parse; it cannot verify the claim, because there is one source
throughout (`BF-009`, `DEP-013`).

**One inherited from PR #16, and it now cuts the other way.** `DEP-008`
warned that an instrument informed by a classification would reproduce it.
That still holds — but note the direction here: a dictionary compiled by the
author of the standard Brahui comparative grammar would be expected to include
Brahui *generously*. It puts 9 of Brahui's 269 entries inside North Dravidian.
A thin result from a favourably disposed instrument is worth more than a thin
result from a neutral one, which is an argument for taking `DMM-004` slightly
**more** seriously (`DMI-005`).

**One structural exposure, disclosed not corrected.** Twenty of twenty-two
measurement rows are sourced through connectors indexing Anglophone
journal publishing. The community-authored Brahui scholarship this unit
located is not readable from here (`D-039`). That is an asymmetry in the
evidence base, and `DMI-012` states it rather than letting the record imply
that what was reachable is what exists.

### Preferred-counter-narrative challenge

*Did this accept a claim too easily because it is anti-colonial, Indigenous,
subaltern, corrective or politically useful?*

**The main pull, and it was resisted at the row level.** The retrieved
literature makes an anti-migration reading easy: an unattributed review calls
a three-language northern group "doubtful" (`DMM-007`), a named isogloss has
been withdrawn (`DMM-011`), and this unit's own `DMM-004` is a null. The pull
was to let those settle `DMG-2` out. They do not. `DMG-2` reads `CANNOT-GATE`
with an explicit note that being the disfavoured model is not a reason to gate
it out — and the rejection of migration-as-default in the inherited record
(`R-10`) is a rejection of a *default*, not a finding.

**The specific temptation, logged.** `BF-008`: a genetic null and a lexical
null read as convergent. Both point away from a Brahui–Kurukh–Malto unity;
both are politically legible; neither measures the other's object.

**Three places the pull was resisted and the finding reported at full weight.**

- `DMM-003` reports **seven** exclusive Brahui–Kurukh–Malto etymologies
  against a null of zero. That is a result *for* the upper node, in a unit
  whose other findings run against it, and it is stated first.
- `DMC-006` — the one community-authored chronology retrieved — is at `HOLD`
  and is explicitly refused as support for `DMG-2`, even though a documented
  Brahui migration would be the most quotable thing in the unit. Wrong
  direction, wrong century.
- `DMM-020`, the genetic null, is the most misusable row here and its own
  notes say what it may not be used for.

**Result of both tests.** Three corrections made (`BF-007`, `BF-008`,
`BF-009`), one temptation declined (`DMM-006`'s framing), two structural
asymmetries disclosed (§6, §12). One PR #16 warning re-read as cutting the
opposite way (`DMI-005`). **No claim changed direction as a result of either
test, and no claim was allowed to close a §4.M model.**

---

## 13. What is on hold

`HOLD-004` — **Krishnamurti 2003**, unchanged and still the book everything
traces to. Cambridge University Press is in no reachable connector's corpus.
Two of its six items moved: DEDR is now readable as data, and Kobayashi &
Tirkey is readable at abstract level.

`HOLD-005` — **the Balochi and Indo-Aryan strata**, new. Korn 2005 is the work
that would answer it and was not read. Until it is, the one measurement that
could begin to discriminate among the six models — the depth of the
Brahui–Balochi contact layer relative to `DMC-001`'s expansion frame — cannot
be made.

`HOLD-002` — **DEDR's prose**, narrowed to exactly that.

`D-041` — the **community-authored material** sits at ledger level, unused,
pending the rights steward.
