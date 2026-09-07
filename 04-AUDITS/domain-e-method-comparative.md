# Domain E — method, findings and the two adversarial tests

**Unit of work:** 2026-09-07
**Domain:** E — Dravidian, Munda and unidentified substrate claims
**Registers:** `03-REGISTERS/domain-e-measurements.csv` (30 rows),
`03-REGISTERS/domain-e-interpretations.csv` (10),
`03-REGISTERS/domain-e-evidence-mass.csv` (22),
`03-REGISTERS/domain-e-cdial-loan-candidates.csv` (289),
`03-REGISTERS/domain-e-geography.csv` (12),
`03-REGISTERS/HYPOTHESIS-ELIGIBILITY.csv` (10),
`03-REGISTERS/CROSS-DOMAIN-BRIDGES.csv` (8)
**Audits:** `ARCHIVE-AND-POWER-AUDIT.csv`, `BIAS-FAILURE-LOG.csv`,
`INTERNAL-CONTRADICTIONS.csv`, `REAUDIT-QUEUE.csv`
**Hold:** `05-HOLDS/HOLD-004-substrate-literature.md`
**Reproduce:** `rv-token-extract.py` → `domain-e-evidence-mass.py` →
`domain-e-cdial-attributions.py` → `domain-e-geography.py` →
`domain-e-dedr-digitisation-check.py`

---

## 1. The shape of the problem

Domain E exists because the programme once presented Witzel's Para-Munda
beside Dravidian as though they were rival answers of the same kind
(`IH-033`). The constitution's fix is eleven distinctions that must never
substitute for one another. The obvious way to honour that is to write
carefully about all eleven. The better way, and the one taken here, is to
find a separate source for each one that has a source, and to say
plainly which ones have none.

That turned out to be possible for five and impossible for four.

| # | Distinction | Source used here |
|---|---|---|
| 1 | attested Dravidian | `SRC-056` DEDR reflexes; `SRC-062` DravLex |
| 2 | reconstructed Proto-Dravidian | `SRC-057`, a **separate table** — DEDR itself reconstructs nothing |
| 3 | accepted OIA Dravidian loans | `SRC-060` CDIAL, Turner's own loan arrows |
| 4 | proposed Dravidian substrate forms | **none retrieved** |
| 5 | attested Munda | `SRC-058` |
| 6 | reconstructed Proto-Munda | `SRC-059` Rau 2019, again a separate table |
| 7 | deeper Austroasiatic | inside `SRC-059` only — Rau citing Shorto and Pinnow, never retrieved themselves |
| 8 | Witzel's Para-Munda | **none retrieved** |
| 9 | the Kubhā-Vipāś fallback | **none retrieved** |
| 10 | Masica's Language X | **none retrieved** |
| 11 | genuinely unidentified vocabulary | `SRC-060`, Turner's own residue — a floor, not an estimate |

Distinctions 2 and 6 are the ones most often collapsed, and keeping them
apart cost nothing here because the data arrived in separate files.
Distinction 7 is the one this record is weakest on and says so: the
Austroasiatic layer exists in the register only as Rau's citations.

## 2. What the retrieval channel decided

The three sources the task named — GRETIL, archive.org, TITUS — are all
refused at the egress gateway in this session, on both available
channels, as is `dsal.uchicago.edu`, which hosts DEDR. All four results
are logged (`SRC-048`–`SRC-051`). Three of them were reachable earlier
the same day from a different session; the manifest records both
readings and supersedes neither.

The one open channel is the git proxy's anonymous lane, which serves
arbitrary public repositories even where the REST API refuses them
(`SRC-053`). Everything below came through it.

That channel has a shape, and the shape is the single most important
methodological fact in this unit. Attested families and published
reconstructions have machine-readable derivatives on GitHub. Proposals
about unattested donors live in journal articles and monographs and do
not. **The four distinctions with no source are exactly the four that
exist only as arguments in the literature.**

So the empty cells are a property of the network policy. Writing
"Dravidian: measurable; Para-Munda: nothing found" would convert an
egress rule into a finding, and would be the programme's original error
running backwards — parity refused in one direction, then refused in the
other. `HOLD-004` states this, `BF-008` logs it as a failure that was
available and declined, and every gate verdict for distinctions 8–10
reads **CANNOT GATE**, never FAIL.

## 3. What was measured

### 3.1 Turner's attributions, and what a naive search does to them

CDIAL marks loans with an arrow and an abbreviation, so the attributions
can be counted rather than recalled. Over 15,417 entries:

| | Dravidian | Munda |
|---|---|---|
| loan arrow into Indo-Aryan | **224** | **55** |
| arrow out of Indo-Aryan | 9 | 1 |
| mentioned at all | 283 | 99 |
| of the arrows, hedged by Turner | 19 (8.5%) | 8 (14.5%) |

Three search errors were caught by reading output rather than trusting
it. All three are the failure correction `C-04` records, in new clothes.

**`MuṇḍUp.` is the Muṇḍaka Upaniṣad.** A search for the spelled-out
family name returns 22 entries, ten of which are citations of a Sanskrit
text and contain no reference to any language. Worse, Turner's actual
abbreviation is `Mu.`, so the same search misses most of the real cases.
Measured against the corrected search built from CDIAL's own
abbreviation key: **precision 54.5%, recall 12.1%.**

**The first normaliser stripped macrons along with accents**, merging
*kalā́* with *kālá*, *kúṭa* with *kū́ṭa*, *mā́lā* with *mála*, *śáva*
with *sāvá*. It produced 24 Rigvedic matches where there are 19 — a 26%
inflation, in the direction that flattered the hypothesis this unit's
own gate had passed. Restricted to Vedic tone marks, then two purely
orthographic conventions folded deliberately and separately (Turner's
redundant macron on *e* and *o*; anusvāra overdot against underdot),
which recovered one true match.

**Simplex, compound-member and derivative attestation were collapsed.**
Turner writes "(RV. in cmpd.)" at *kuṇḍá* and "in cmpds. RV." at
*mayū́ra*, and the Zurich layer bears him out exactly: no simplex for
either, but `kuṇḍapā́yya-`, `mayū́raroman-`, `mayū́raśepya-`. A boolean
would have called both unattested. Three columns now. Of the four
matches the containment column raised, two are real and two
(`*garda`→`gardabhá-`, `pōta`→`potár-`) are spelling coincidences, so
the column is labelled string evidence needing case-by-case review.

### 3.2 The Rigvedic signal

Of 279 loan attributions, 20 candidate rows have a Rigvedic simplex.
Those collapse to **15 distinct lemmas** — CDIAL numbers *kūṭa* as four
entries and *píṇḍa* carries both a Dravidian and a Munda attribution —
totalling **21 tokens, 0.013% of the corpus**.

That is a floor produced by one dictionary and one matching rule, and it
is small on any reading, including the reading this record's gate
favours.

10 of the 21 tokens sit in a pāda Arnold assigns to the Popular stratum,
against a corpus share of 13.9%. The binomial tail is small
(2.2 × 10⁻⁴). The number is registered; the inference from it is not.
`BR-E-002` refuses the step from stratum to date on three grounds: the
strata are Arnold 1905 alone (`DEP-001`), Popular is not independent of
book 10 (`DEP-004`), and 15 lemmas with tokens clustered inside them are
not 21 independent draws.

### 3.3 Source genealogy

**85% of Turner's 55 Munda arrows cite Kuiper or PMWS.** Fifty-five
citations tracing to one author count as one, and Kuiper is unretrieved
(`DEP-010`). His 224 Dravidian arrows spread across Mayrhofer (85),
Burrow (81), Kuiper (18), Bloch (15).

And **every Munda attribution names an authority while 29 Dravidian ones
name none.** On this measure Turner is more careful on the side with
less evidence behind it.

### 3.4 Geography, in kilometres

| | nearest attested lect to the northwest |
|---|---|
| Dravidian | **Brahui, 393 km** |
| Munda | **Korku, 855 km** |
| Dravidian **without Brahui** | **Kolami, 1,055 km** |

Munda proper fails the geography gate: no attested Munda lect falls
inside the northwestern envelope. The failure is scoped exactly as §4.E
scopes it — it weakens a Munda-affiliated substrate explanation and does
not transfer to any unattested prefixing language.

And then the third row. **Dravidian's entire northwestern geographic
position is one language.** Remove Brahui and Dravidian is farther from
the northwest than Munda is. That makes Brahui load-bearing for a case
this programme leans toward, and hands the question to domain M, where
`IH-031` already records that the burden was once inverted.

## 4. Step 13 — checking MelaKeela

The site repository was attachable, so this step ran rather than being
held. It found one real problem and two clean passes.

**`IC-E-001`/`IC-E-002`.** The site ships `dedr_roots.json`, built from a
*third* DEDR digitization (`github.com/ArimeKannada/Dictionary`, per
`RERUN.md` line 25). Across the 18 languages whose labels map one-to-one
it disagrees with the DSAL-derived table used here on **10.3%** of
entry-language assignments, and neither is a subset of the other. The
page `the-northwest-cousin.html` publishes "counted directly from the
Dravidian etymological dictionary, 191 of Brahui's 262 recorded roots
have Tamil cognates". Its arithmetic is exactly right for its own data.
The same computation over this unit's data gives **223 of 273 — 82%
against 73%**.

The site is not shown to be wrong. What is shown is that the number is
less stable than "counted directly from the Dravidian etymological
dictionary" implies, and that the raw count moves too, not only the
percentage the page correctly warns about. Print is unreachable from
either side (`SRC-051`), so neither can be adjudicated. Every
DEDR-derived count in this unit inherits the same error bar.

**`IC-E-003`, `IC-E-004`.** Two passes, recorded so step 13 has both.
`caste-enforcement-mechanism.html` already keeps Para-Munda as a
reconstruction, refuses Language X as a positive explanation, and calls
the residue unidentified — which is what §4.E asks. And
`the-northwest-cousin.html` already holds both Brahui hypotheses open
with the Elfenbein dating named as the pivot.

## 5. The two adversarial tests

### Prestige-bias challenge

*Did this privilege a claim because it is canonical, Sanskritic,
Brahmanical, Indo-European, European, colonial, institutionally
prestigious, repeatedly cited or nationally useful?*

The instrument at the centre of this unit is CDIAL — a British
comparative dictionary of the Indo-Aryan languages, compiled 1962–66,
organised by Indo-Aryan headword. Three ways that could have skewed the
result, and what was done about each.

**It makes Indo-Aryan the frame.** Every loan candidate here is a word
Turner listed because it is Indo-Aryan; Dravidian and Munda enter as
donors to it. A Dravidian-headed instrument would ask a different
question and could return a different set. This is a real limit on the
0.013% and it is stated in `DE-I-003` rather than left implicit.

**Its authority is colonial-era lexicography.** `APA-E-002` records that
Turner could only be as good as the dictionaries available to him, that
Munda lexicography was thinner than Dravidian in his window, and that
this is a live untested alternative explanation for the 4.1-to-1 ratio.
The ratio is therefore registered as a fact about Turner (`DE-I-004`),
not about the Rigveda, and the alternative is queued as `RA-007`.

**Citation count could have stood in for standing.** It does not:
`DE-I-009` is a `VERIFIED` statement that current specialist standing
could not be established at all, because the newest opinion reachable in
this session is Turner's from 1966. Step 11 was run and returned a gap,
which is recorded as a gap rather than filled with the loudest source.

One more, less obvious. The Rigveda is the prestige corpus of this
subject, and using it as the test bed risks treating what a liturgical
text records as a measure of what happened. `APA-E-001` types that
absence as `NOT PRODUCED` and caps the 0.013% as a floor on what a
priestly genre wrote down.

### Preferred-counter-narrative challenge

*Did this accept a claim too easily because it is Dravidian, Indigenous,
anti-colonial, anti-Brahmanical, subaltern, diffusionist or politically
corrective?*

This is the more dangerous of the two here, because the Dravidian case
is the one this programme leans toward and the one the data favoured.

**The strongest evidence against the leaning was measured and
registered at full weight, not noted in prose.** `DE-M-025`: remove
Brahui and Dravidian sits farther from the northwest than Munda. That is
the single most uncomfortable number in this unit for the reading the
platform prefers, and it is a register row with the same standing as the
rows that help. `BF-009` records this as the test passing rather than
as a failure.

**The null explanation was entered first and made to compete.**
`HYP-E-000` is Indo-Aryan-internal explanation with no donor at all. In
a programme whose recorded failure was reaching for donors, the null
cannot be an appendix.

**The Munda geography failure was scoped, not spent.** It would have
been convenient to let "no attested Munda in the northwest" do work
against Para-Munda too. §4.E forbids exactly that, and `HYP-E-002`'s
verdict says so in the row.

**Unavailability was not scored as refutation.** The mirror failure —
correcting the old Para-Munda parity error by treating unretrievable
sources as unsupported claims — was available, is named in `BF-008`,
and is refused. `CANNOT GATE`, never `FAIL`.

**Where the data cut against Munda, the archive was checked before the
conclusion.** `APA-E-005` records that the small Munda evidence base
here is partly a fact about lexicography, and `APA-E-002` that Turner's
preference may be too.

**And the site was checked against, not for.** Step 13's finding
qualifies a published MelaKeela number rather than confirming one.

**What the tests did not catch, stated so it is not mistaken for
absence.** Both challenges are run by the same reader who did the work.
Neither test can establish that the 224 Dravidian etymologies are
individually sound — `BR-E-001` says the bridge from Turner's bracket to
a contact event is not crossed here — and neither can substitute for
retrieving Witzel, Kuiper and Masica and gating them properly.

## 6. What would change the conclusions

- Retrieving Witzel 1999, Kuiper 1991 or Masica 1979 would populate four
  empty distinctions and could move the balance in either direction.
- Retrieving DEDR in print or through DSAL would adjudicate `IC-E-001`
  and remove the ~10% error bar from every DEDR count in the record.
- A larger loan-candidate list — from Kuiper's or Southworth's word
  lists rather than Turner's arrows — could raise the 0.013% by an order
  of magnitude, or could show the stratum skew dissolving.
- Any evidence of Munda-family speech west of Korku at any period would
  revive `HYP-E-002`.
- Any Dravidian trace in the northwest independent of Brahui would stop
  `HYP-E-001`'s geography resting on one language.
- A post-1990 assessment of the substrate question would let step 11 run
  at all.
