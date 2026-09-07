# Domain E — Dravidian, Munda and unidentified substrate claims

**Unit of work:** 2026-09-07
**Registers:** `03-REGISTERS/domain-e-claims.csv` (26 claims),
`03-REGISTERS/domain-e-hypothesis-eligibility.csv` (11 rows),
`03-REGISTERS/domain-e-retroflex-residue.csv` (253 lemmas),
`03-REGISTERS/domain-e-hydronyms.csv` (469 occurrences)
**Sources:** `SRC-019`–`SRC-024`, `SRC-026`, `SRC-037`–`SRC-047`
**Holds:** `HOLD-002`, `HOLD-003`  **Decision raised:** `D-042`
**Reproduce:** `04-AUDITS/rv-token-extract.py`, then
`rv-retroflex-classify.py`, `rv-retroflex-aggregate.py`,
`rv-hydronym-census.py`

---

## 1. What this unit is, and what it is not

The constitution names the mishandling of Dravidian and "Para-Munda" as
the failure the whole methodology exists to correct (§1). This unit was
supposed to be the one that does that domain properly.

It could not be, in one half. Every etymological and comparative source
was refused at the session's egress gateway — `dsal.uchicago.edu`
(DEDR), `archive.org`, the Cologne dictionaries, EJVS, GRETIL, TITUS,
fifteen hosts in all, on both the `curl` and the WebFetch channel.
Ninety minutes earlier, in the previous session, four of those had
answered HTTP 200 and are recorded as reachable at `SRC-025`, `SRC-028`,
`SRC-029` and `SRC-033`. Neither record is wrong; the policy narrowed
between them. That is `D-042`.

So the unit split in two:

- **The comparative half** — items 1–3 and 5–8 and 10 of §4.E — is on
  hold, with `HOLD-002` and `HOLD-003` naming exactly what is needed and
  `03-REGISTERS/domain-e-hypothesis-eligibility.csv` carrying each row
  gated as `NOT-ELIGIBLE-SOURCE-BLOCKED` rather than judged.
- **The corpus-internal half** was run in full, because it does not
  depend on the blocked sources. It measures the Old Indo-Aryan side of
  the question: what the Rigveda's own phonology and geography constrain,
  before any donor is named.

Nothing here measures Dravidian, Munda or Para-Munda material. `DME-026`
says so as a claim, so that it is auditable rather than implicit.

## 2. The eleven distinctions, and why the register has eleven rows

§4.E requires that eleven things never stand in for one another. The
eligibility register gives each its own row and its own gate verdict.
Three of the eleven are not hypotheses at all and are marked
`NOT-A-HYPOTHESIS`: attested Dravidian (E-1), attested Munda (E-5), and
the residue of genuinely unidentified vocabulary (E-11). Two more are
reconstructions rather than attestations (E-2, E-6) and sit one step down
the gradient. Only the remaining six are gateable propositions.

The gate outcomes, from §5 step 7:

| Row | Gate | Space allocated |
|---|---|---|
| E-4 Dravidian substrate forms | **ELIGIBLE** — chronology and geography both pass | none, for want of evidence, not for want of eligibility |
| E-9 Kubhā–Vipāś unknown prefixing language | **ELIGIBLE** — and this unit advanced its geographical gate | small |
| E-3 accepted OIA Dravidian loans | source-blocked | none |
| E-7 deeper Austroasiatic | source-blocked | none |
| E-8 Witzel's Para-Munda | source-blocked | none |
| E-10 Masica's Language X | **gate failed on scope** — a claim about Hindi vocabulary and the Gangetic plain, not about the Rigvedic corpus | a concise exclusion |

E-9 is the only row whose gate this unit actually moved, and it moved on
evidence generated here: both ends of the named region are attested in
the corpus, and the western end is attested inside the Archaic stratum
(§4 below).

E-8 is carried as *a named position whose content is not retrieved*. It
is neither excluded for being wrong nor admitted for being famous.
Writing out what the proposal says from recollection would manufacture
precisely the evidentiary standing the inheritance rule withholds, and it
would do it for the one hypothesis whose mishandling the constitution
names in §1. That is `BF-003`.

## 3. Measurement one — retroflexion

### What was measured

Every retroflex segment in all 10,031 Rigvedic lemma citation forms was
classified by whether one of two regular Old Indo-Aryan rules derives it:

- **RUKI** — `s > ṣ` immediately after `i ī u ū e o ai au r r̥ r̥̄ k`;
- **nati** — `n > ṇ` when `r`, `r̥` or `ṣ` precedes in the same word with
  no palatal, dental, retroflex stop, `l`, `s` or `ś` intervening, and
  `ṇ` is followed by a vowel, `y v n m` or is word-final;
- plus **cluster** conditioning for a retroflex stop after `ṣ` or after
  another retroflex.

| | segments | lemmas | tokens |
|---|---:|---:|---:|
| derived by the rules | 2,399 | 1,806 (18.0%) | 12,264 (7.4%) |
| **not derived** | **267** | **253 (2.52%)** | **1,257 (0.76%)** |
| no retroflex at all | — | 7,972 (79.5%) | 151,237 (91.8%) |

Every one of the 2,666 decisions is written out individually in
`rv_retroflex-segments.tsv` so that any single one can be overturned
without re-running the classification.

### The word-initial result

No Old Indo-Aryan rule produces a word-initial retroflex. That position
is therefore the sharpest diagnostic available, and in the Rigvedic lemma
inventory it is **empty**: every word-initial retroflex is `ṣ-`, and all
eight such lemmas are the numeral *ṣáṣ-* "six" or a compound of it —
*ṣáṣ-, ṣaṣṭí-, ṣaḷakṣá-, ṣaṭtriṃśá-, ṣoḷhā́, ṣáḍvidhāna-, ṣáḷara-,
ṣáḷaśva-*. There is no lemma beginning `ṭ ṭh ḍ ḍh ṇ ḷ ḷh`.

`DME-021` states what this does and does not weigh against. It weighs
against a donor contributing retroflex-initial vocabulary unadapted. It
does not weigh against contact-induced retroflexion, because borrowing
routinely adapts a loan to the recipient's phonotactics and later
Indo-Aryan does acquire initial retroflexes. The claim is scoped to
lemmas, not to surface forms, because the lemma layer normalises sandhi
away — `DEP-007`.

### Why 253 is an upper bound and not a residue

The rules operate on a string. They cannot see a deleted conditioning
segment. The two highest-frequency members of the "residue" are the
proof:

> *tváṣṭar-* (65 tokens) and *táṣṭar-* (7) are built on √*takṣ-*. RUKI
> applies after `k`; the `k` is then lost in `kṣ + t > ṣṭ`. The rule sees
> `ṣ` after `a` and reports it underived.

That is `DME-014`, recorded as a worked false positive rather than
asserted to be rare. Several further internal sources are deliberately
not implemented, because each needs an etymology per word rather than a
rule over a string: `*-zdh- > -ḍh-` (*mīḍhá-* < `*mizdha-`), `*-lt-` and
`*-ln-` clusters, seam assimilations, the PIE `*l`/`*r` merger, frozen
sandhi in compounds.

A formal sub-typology marks the shapes where those are most likely, on
string criteria alone and asserting no derivation:

| class | lemmas | tokens |
|---|---:|---:|
| F1 unconditioned `ṣ` before a retroflex stop | 39 | 158 |
| F2 unconditioned aspirated retroflex `ḍh`/`ḷh` | 19 | 100 |
| F4 word-initial `ṣ` | 8 | 30 |
| F3 lemma begins `dū-` | 4 | 15 |
| **F5 none of the above** | **183** | **953** |

So the pool a substrate proposal has to explain is at most 183 lemmas,
and probably fewer. Narrowing it further needs per-word etymologies, and
every etymological source was refused (`HOLD-002`, `DME-025`). Under the
negative-evidence standard that absence is typed **NOT ACCESSIBLE**: a
fact about this session's network, with no bearing on the lexicon.

## 4. Measurement two — the corpus geography

The Zurich/Grassmann layer carries no hydronym category, and it files
several rivers under something else:

| surface | lemma it is filed under |
|---|---|
| *sárasvatī* | *sárasvant-*, the masculine stem |
| *asiknyā́* | *ásita-* "black" |
| *páruṣṇīm* | *paruṣá-* "knotty" |

A lemma-name search loses all three and would have supported the false
statement that the corpus does not name them. That is `BF-002`, and it is
inherited correction **C-04** running in the opposite direction: C-04 was
a stem search over-counting, this was a lemma search under-counting. Both
mistake an annotation layer for the text.

The census was therefore rebuilt over accent-stripped **surface** forms
against an explicit name list, and every one of the 469 hits was typed by
hand as `RIVER`, `AMBIGUOUS`, `DERIVATIVE`, `REGION-OR-EPITHET` or
`NOT-RIVER`.

**31 named rivers, 251 occurrences typed RIVER.** *síndhu-* takes 126 and
feminine *sárasvant-* 70; the other 29 names share 55. *síndhu-* is both
"river" and the Indus and the lemma layer does not separate the senses,
so 126 is an upper bound on the hydronym reading.

**Nine of the 31 occur only inside RV 10.75**, one hymn: Asiknī, Gaṅgā,
Mehatnū, Silamāvatī, Susartu, Tṛṣṭāmā, Vitastā, Ārjīkīyā, Śvetyā. Gaṅgā
is attested **once** in the entire corpus, the vocative *gaṅge* at
10.75.5. Yamunā three times.

**The western tributaries are attested outside 10.75 and in Archaic-stratum
pādas**: Kubhā and Krumu at 5.53.9, Gomatī at 8.24.30, Suvāstu at
8.19.37. Vipāś at 3.33.1, 3.33.3 and 4.30.11.

That is what gates E-9. Both ends of the Kubhā–Vipāś region are inside
the corpus, and the western end is inside its older stratum. It is also
what makes `DME-023` — the mismatch with the attested range of Munda
proper — a statement about E-5 and about nothing else on the list.

The identification of each ancient name with a modern river is
Grassmann's, carried in the gloss, and is one dependent framework
(`DEP-005`). The occurrence counts are `VERIFIED`; the map is
`PROVISIONAL`.

## 5. Chronology — and a null

Does the residue accumulate through the Rigvedic period, as a
"foreign vocabulary enters over time" claim predicts?

**Type level**, the unit a vocabulary claim is actually about — each
lemma assigned the stratum holding most of its tokens, 8,449 lemmas with
a single majority stratum, 1,582 tied and excluded:

| stratum | lemmas | residue | share | expected |
|---|---:|---:|---:|---:|
| Archaic | 1,796 | 42 | 2.34% | 43.2 |
| Strophic | 1,648 | 36 | 2.18% | 39.6 |
| Normal | 1,930 | 41 | 2.12% | 46.4 |
| Cretic | 1,352 | 33 | 2.44% | 32.5 |
| **Popular** | 1,723 | **51** | **2.96%** | 41.4 |

χ² = 3.21 on 4 df, **p = 0.52**.

**Token level**, reported because the standing rule after correction C-05
is that both units are shown and neither is privileged silently:
71.3 / 74.1 / 74.6 / 80.0 / 85.4 per 10,000 for A / S / N / C / P,
χ² = 4.50 on 4 df, p = 0.34.

**Second instrument**, book order: family books 2–7 at 78.4 per 10,000
against 74.9 for books 1, 8, 9 and 10; χ² = 0.65 on 1 df, p = 0.42. Book
3 is the high outlier at 111.5 and book 9 the low at 57.9.

**Vocabulary renewal**, lemmas confined to one part of the corpus:
only books 2–7, 2.72%; only book 10, 3.20%; only book 1, 2.72%; only
books 8–9, 2.31%.

**The direction, reported as part of the result and not buried.** A
Cochran–Armitage trend test over the ordered strata gives z = **+1.28**,
χ² = 1.64 on 1 df, p = 0.20. Popular against Archaic alone, with Yates
correction, χ² = 1.09, p = 0.30. The point estimate rises monotonically,
in the direction the accumulation claim predicts. The test does not
separate that rise from noise. **Both halves of that sentence are the
result**, and `DME-020` is capped at `PROVISIONAL` for three separate
reasons: the proxy is one diagnostic and not a definition of foreignness;
the chronological instrument is Arnold 1905 via `strata.json`, one source
(`DEP-001`, `DEP-006`), and Arnold called his periods provisional; and a
null is not a refutation, least of all at 253 lemmas.

`BF-004` records that this was first written up as "the residue does not
accumulate through the Rigveda," which is the corrective-sounding
conclusion, and was corrected.

## 6. Where the measurement/interpretation line falls

**VERIFIED — 19 rows.** Every count: the 2,666 segment decisions, the
253/1,806/7,972 lemma split, the eight word-initial lemmas, the five
stratum tables and their χ², the 31 rivers and 251 occurrences, the nine
rivers confined to 10.75, the three misfiled lemmatisations. Each has a
locator that re-finds it and a script that regenerates it.

**PROVISIONAL — 4 rows.** `DME-019` (that Rigvedic retroflexion is
overwhelmingly rule-governed) is a reading of the classification, not a
count, and inherits the rule formulations, which are one framework and
are not independently sourced here. `DME-020` as above. `DME-021` and
`DME-022` inherit, respectively, a single classification and a single
gloss set.

**HYPOTHESIS — 2 rows.** `DME-023`, the geographical mismatch with Munda
proper, because its second half depends on the attested Munda range and
no Munda source was retrievable. `DME-024`, that the F5 pool is what a
substrate proposal must explain — explicitly not a claim that those 183
lemmas are non-Indo-Aryan.

**HOLD — 1 row.** `DME-025`: whether the residue can be narrowed is
undecidable here.

## 7. The two adversarial tests, §8

### Prestige-bias challenge

*Did this privilege a claim because it is canonical, Sanskritic,
Brahmanical, Indo-European, European, colonial, institutionally
prestigious, repeatedly cited or nationally useful?*

**One failure found and corrected: `BF-003`.** The gating table was about
to record a specialist-standing verdict for Witzel's Para-Munda proposal
and for the accepted-loan corpus, drawn from recollection rather than a
retrieved statement — the assumption being that a famous position is well
enough known that summarising it is not the same as sourcing it. Every
such cell now reads "Not sourced here" and the rows are typed
`NOT-ELIGIBLE-SOURCE-BLOCKED`.

**A structural risk that remains.** The whole evidentiary base of this
unit is a Sanskrit corpus, annotated by a German lexicographical
tradition (Grassmann 1873, via Zürich), periodised by an English
metrician (Arnold 1905). Every measurement here is made *inside*
Indo-European philology's own instruments. That is not neutral ground,
and it is not corrected by anything in this unit — it is the reason
`DME-019`, `DME-020` and `DME-022` are capped. It is recorded here rather
than in the failure log because it is a property of what was reachable,
not a decision that was made wrongly.

**Checked and not found:** the residue was not read as evidence for
inheritance. `DME-004` is stated as an upper bound and `DME-014` supplies
the false positives that shrink it; the unit does not conclude that
because most retroflexion is rule-governed, all of it is.

### Preferred-counter-narrative challenge

*Did this accept a claim too easily because it is Dravidian, Indigenous,
anti-colonial, anti-Brahmanical, subaltern, diffusionist or politically
corrective?*

**One failure found and corrected: `BF-004`**, and it ran in the less
obvious direction. The null result was first written as a refutation of
Kuiper-style accumulation claims — the *anti*-substrate conclusion — on a
weak proxy with limited power. Reporting a null as a refutation is the
same methodological error as reporting a resemblance as a derivation, and
being sceptical of a counter-narrative is not a defence against it. The
trend statistic and its direction are now part of the result.

**Checked and not found:** no Dravidian claim was admitted at any status.
E-4 clears its gate and receives no space, which is the correct outcome
when the gate is cheap and the evidence is absent. E-9's gate was
advanced on a measurement made here, not on the attractiveness of an
unidentified-donor story, and the method doc says explicitly that being
weaker than E-8 is a cost — E-9 predicts less.

**The asymmetry the constitution insists on is real and is not pretended
away.** Grassmann, Arnold and the Zürich annotation were reachable
through a GitHub repository at zero cost. DEDR, the Munda comparative
literature and EJVS were not reachable at all. That is not a fact about
the quality of the scholarship. It is a fact about which traditions have
been digitised, licensed openly and mirrored — and it is the exact
mechanism by which an archive's institutional power becomes a research
result. `D-042` puts it to the owner as a decision rather than absorbing
it as a limitation.

## 8. Known limits

- The classification is over lemma citation forms, which are a modern
  normalisation. `DME-007` is scoped to lemmas for that reason (`DEP-007`).
- `√īḍ- ~ īḷ-` and similar variant pairs are one lemma and are segmented
  from the first variant only.
- One lemma string in the Zürich layer is the metalinguistic
  "Vriddhiableitung von tanū́-" rather than a citation form. It carries no
  retroflex and does not affect any count, but it is in the 10,031.
- 1,582 lemmas have no single majority stratum and are excluded from the
  type-level table. They are not excluded from the token-level one.
- The `síndhu-` figure does not separate "the Indus" from "a river". No
  instrument here can.
- Six occurrences of *ásiknī-* and one of *śvetyā́-* are typed
  `AMBIGUOUS` rather than assigned. They are in the register with that
  type, not silently dropped.
