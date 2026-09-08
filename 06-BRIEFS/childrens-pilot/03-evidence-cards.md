# Evidence cards — every piece of evidence the child sees

**Written:** 2026-09-08
**Rule this file exists to enforce:** framework §10.4.4 — *"No fabricated
evidence, ever. If the institution would not show it to an adult as evidence, it
is not shown to a child as evidence."* Every string a child reads that purports
to be evidence appears below, with its register row, its locator and its status.
Anything not below may not appear on a screen.

**Diacritics — read this before quoting anything below.** Some register rows
carry the accented Saṃhitā text (the `text_samhita` column of
`rigveda-pur-passages.csv`); most of the passage strings in the *locator* fields
of `rigveda-pur-4j-claims.csv` are **unaccented transliterations**. Every string
below is reproduced **exactly as the register has it**, accented or not. No
accent, macron or diacritic has been supplied by this unit, and none may be:
supplying one is a reconstruction of the text, not a quotation of it. Gate
**G-05** requires the accented forms to be pulled from the pinned corpus
(`SRC-020`, `SRC-084`) before any of this reaches a screen, and the unaccented
strings replaced rather than decorated.

---

## EC-01 — The stanza, three ways *(screen S-01)*

Register row: `PUR-P-041` in `03-REGISTERS/rigveda-pur-passages.csv`.
Occurrence: `PUR-OCC-042` in `rigveda-pur-family-occurrences.csv`.

| Row | Content | Source |
|---|---|---|
| Saṃhitā | `śatám aśmanmáyīnām purā́m índro vy āā̀syat / dívodāsāya dāśúṣe` | `SRC-020` Aufrecht 1877 |
| Padapāṭha | `śatam \| aśman-mayīnām \| purām \| indraḥ \| vi \| āsyat \| divaḥ-dāsāya \| dāśuṣe` | `SRC-021` |
| Devanāgarī | as set in `rigveda/versions/eichler.csv` | `SRC-084` |

**Defect to fix before build.** The Saṃhitā string as stored reads `vy āā̀syat`
where `PUR4J-014`'s locator gives `vy asyat`. The doubled vowel is an encoding
artefact of the register file, not a reading. `G-05` blocks the screen until it
is resolved against the pinned corpus.

Word count in the padapāṭha row: **8**. This is the number the child counts.

**Status of what is asserted from this card:** the three rows exist and are what
they say they are — `VERIFIED` (`SRC-020`, `SRC-021`, `SRC-084`, all `VERIFIED`
in the access ledger). Nothing about a fort is asserted here.

---

## EC-02 — The word `púr-` *(screen S-02)*

Worked to constitution §7, at reading age.

| §7 field | Value | Row |
|---|---|---|
| Original script | as `EC-01`, Devanāgarī row | `SRC-084` |
| Transliteration | `purā́m` | `PUR-OCC-042` |
| Grammatical form | genitive plural, feminine; a root noun | `PUR-OCC-042`, `PUR4J-020` |
| Semantic range (lexicon) | *Wall aus Steinen und Lehm, Verschanzung, Palisade* | `PUR4J-021` `VERIFIED` |
| Plain-English rendering of the gloss | "a wall of stones and clay, a bank dug for defence, a fence of stakes" | this unit, from the German above |
| Textual context | governed by `śatám` "a hundred" across a pāda break | `PUR-N-024` in `rigveda-pur-counts.csv` |
| Edition | Aufrecht 1877 | `SRC-020` |
| Locator | RV 4.30.20, pāda b, token 1 | `PUR-OCC-042` |
| Translations available | fort 63 · castle 33 · stronghold 5 · fortress 4 · city 1 (Griffith 1890); *Burg* 79 · *Feste* 9 · *Bollwerk* 1 · *Wall* 1 (Geldner 1951); *Burg* 84 · *Feste* 9 (Grassmann 1876–7); *forteresse* 34 · *citadelle* 22 (Renou) | `PUR4J-022` `VERIFIED` |
| Interpretive consequence | the English word chosen decides whether the child spends the rest of the investigation reasoning about a city, a castle or an earth bank | `PUR4J-I-03` `PROVISIONAL` |

**What the child is not told.** That any of these is right. The child picks one
and it becomes their label (S-02).

**Independence warning that must travel with this card.** These are not four
independent witnesses. `DEP-021` records Grassmann's translation as the same
judgement as his glosses; `DEP-023` records Elizarenkova as having worked with
Geldner in view. The menu may not be presented as four checks agreeing. Gate
**G-06**.

---

## EC-03 — The six ninety-nine passages *(screen S-05)*

From `PUR4J-004`, `VERIFIED`. Reproduced exactly as the register's locator
carries them, unaccented.

| Passage | Text | The two words |
|---|---|---|
| RV 1.54.6d | `puro navatim dambhayo nava` | `navatim` … `nava` |
| RV 2.19.6c | `navatim ca nava` | `navatim` … `nava` |
| RV 4.26.3b | `nava sakam navatih` | `nava` … `navatih` |
| RV 7.19.5b | `nava yat puro navatim ca` | `nava` … `navatim` |
| RV 7.99.5b | `nava puro navatim ca` | `nava` … `navatim` |
| RV 8.93.2a | `nava yo navatim puro` | `nava` … `navatim` |

Joined by `ca` in three; separated by other words in four. `PUR4J-004`.

`navatí-` is feminine **singular** — a collective, "a ninety" — in five of the
six; only RV 4.26.3 has the agreeing plural `navatih`. `PUR4J-005`.

**The completion.** RV 4.26.3c `satatamam vesyam`; RV 7.19.5c `nivesane
satatama`. In both, "the hundredth" modifies a dwelling word, not the fort word.
`PUR4J-008`.

---

## EC-04 — The river passage *(screen S-06)*

From `PUR4J-006`, `VERIFIED`. **The hinge card.**

> RV 10.104.8c — `navatim srotya nava ca sravantir`
> padapāṭha — `navatim | srotyah | nava | ca | sravantih`

| Translator | Rendering | Source |
|---|---|---|
| Griffith 1890 | "nine-and-ninety flowing streams" | `SRC-073` |
| Geldner 1951 | "die neunundneunzig fließenden Ströme" | `SRC-072` |
| Grassmann 1876–7 | "Die neunundneunzig Flüsse" | `SRC-074` |

`pūrbhíd` — "wall-breaker" — stands in pāda b of the same stanza, `NOM.SG.M`, an
epithet of Indra, and takes no numeral. `PUR4J-006`, `PUR-004`.

**Why this card carries the investigation.** The same two words. A different
thing counted. A fort word in the same stanza. A stanza-level co-occurrence
measure would have called this "ninety-nine forts", and `PUR4J-006`'s own note
says this is the case that defeats such a measure. A child can see all of that
in one line.

---

## EC-05 — The materials *(screen S-07)*

From `PUR4J-012`, `VERIFIED`.

| Material | Lemma | Passages | Locators |
|---|---|---:|---|
| of metal | `āyasá-` | 8 | RV 1.58.8, 2.20.8, 4.27.1, 7.3.7, 7.15.14, 7.95.1, 8.100.8, 10.101.8 |
| of stone | `aśmanmáya-` | **1** | RV 4.30.20 |
| raw, unbaked | `āmá-` | 1 | RV 2.35.6 |
| *(none stated)* | — | **93** | typed `NOT PRODUCED` |

The unbaked one: RV 2.35.6 `amasu pursu paro apramrsyam / na aratayo vi nasan` —
in the raw forts, neither malice nor deceptions reach him. `PUR4J-014`.

**The metal crux.** Griffith prints "iron" at all eight; Geldner prints *ehern*
— of ore, brass, bronze — at all eight; Grassmann mixes (*Erz* at 1.58.8,
*Eisen* at 4.27.1, *ehern* at the rest, and does not render the word at 7.3.7).
Neither Griffith nor Geldner argues the point. `PUR4J-023`, `VERIFIED` as a
statement about what is printed; the metal itself is a `WE DON'T KNOW`.

**Translation of RV 4.30.20 — NOT YET RETRIEVED.** The spec's draft copy at S-07
uses the register's own paraphrase ("Indra threw down a hundred stone forts, for
Divodāsa who gave offerings", `PUR4J-014`). The translators' verbatim renderings
at this stanza are in `SRC-072`/`SRC-073`/`SRC-074` in the pinned clone and were
**not pulled in this unit**. Gate **G-05**: they must be pulled and the
paraphrase replaced before the screen is built. A museum paraphrase standing
where a translator's words belong is exactly the move the translation standard
exists to stop.

---

## EC-06 — The counts *(screens S-04, S-11)*

From `PUR4J-001`, `PUR4J-002`, `PUR4J-003`, `PUR4J-009`, all `VERIFIED`.

- 103 passages in the corpus at the stanza unit; **21** state a count, **82** do
  not. (`PUR4J-001`)
- Of the 21: **100** in 9 — RV 1.53.8, 2.14.6, 4.27.1, **4.30.20**, 6.31.4,
  6.48.8, 7.3.7, 7.16.10, 9.48.2. **99** in 6 — RV 1.54.6, 2.19.6, 4.26.3,
  7.19.5, 7.99.5, 8.93.2. **7** in 4 — RV 1.63.7, 1.174.2, 6.20.10, 7.18.13.
  **90** in 2 — RV 1.130.7, 3.12.6. (`PUR4J-002`)
- 99 is not the modal count. 100 is, by 9 to 6. (`PUR4J-003`)
- No irregular figure occurs anywhere in the corpus. (`PUR4J-009`)

**Note for the tally board.** RV 4.30.20 — the stone fort the child met at S-01
— is a **hundred**-fort passage, not a ninety-nine one. The child therefore
meets the famous number for the first time *after* meeting a verse that does not
use it. That ordering is deliberate.

---

## EC-07 — The cases *(screen S-08)*

From `PUR4J-020`, `VERIFIED`. Of the 83 simplex `púr-` tokens:

| Form | Count |
|---|---:|
| `ACC.PL` *puraḥ* | 45 |
| `ACC.SG` *puram* | 11 |
| `GEN.PL` *purām* | 10 |
| `INS.PL` *pūrbhiḥ* | 6 |
| `NOM.SG` *pūḥ* | 5 |
| `NOM.PL` *puraḥ* | 2 |
| `LOC.SG` *puri* | 2 |
| `LOC.PL` *pūrṣu* | 1 |
| `INS.SG` *purā* | 1 |

Accusative 56 of 83 (67.5%). Locative **3** of 83 (3.6%), one of them RV 2.35.6
`āmāsu pūrṣu`, which is also the unbaked fort of `EC-05`.

---

## EC-08 — The strata *(screen S-09)*

From `PUR-014`, `PUR-016`, `PUR-017`, `PUR-020`, `PUR-021`, all `VERIFIED`;
read chronologically only through `PUR-026` (`PROVISIONAL`) and `PUR-028`
(`HYPOTHESIS`).

| Arnold period | Family tokens | Corpus share | Expected |
|---|---:|---:|---:|
| Archaic | 31 | 20.6% | 21.8 |
| Strophic | 32 | 22.7% | 24.0 |
| Normal | 17 | 24.8% | 26.3 |
| Cretic | 23 | 18.0% | 19.1 |
| Popular | **3** | 13.9% | **14.8** |

The three Popular tokens: RV 8.100.8b, 10.87.22a, 10.101.8c. (`PUR-017`)

Second instrument, family books 2–7 against the rest: 6.98 per 10,000 against
6.07, χ² = 0.50, 1 df, p = 0.48 — **a null**. (`PUR-020`)

Entanglement: 61.3% of all Popular tokens are in book 10, and book 10 is 46.7%
Popular. The Popular deficit and the low book-10 rate are largely the same
observation counted twice. (`PUR-021`, `DEP-004`)

14 of the 106 occurrence rows carry `stratum_certainty =
metrical-variations-only`, Arnold's lower-confidence assignment. A stratum shown
without that flag overstates the evidence (`PUR-011`,
`06-BRIEFS/rv01-reconciliation.md` §3). The S-09 counters must carry it.

---

## EC-09 — The named fort, or not *(screen S-10)*

From `PUR4J-015`, `VERIFIED`.

> RV 1.149.3a — `a yah puram narminim adided`

| Reader | Reads `narmin-` as | Rendering |
|---|---|---|
| Geldner 1951 | a proper name | "Der die Burg Narmini beschien" |
| Griffith 1890 | an adjective | "He who hath lighted up the joyous castle" |
| Grassmann | *declines to choose* | "Name (oder Beiwort) einer púr-" |

If Geldner is right, this is the only named fort in 103 passages. If Griffith is
right, there are none. The register records the dispute rather than resolving
it, and so does the screen.

---

## EC-10 — The ledger *(screen S-10)*

`02-SOURCES/access-ledger.csv`, all 88 rows, shown at reading age with each
row's category.

**What the child will find:** primary corpora, primary texts, primary
annotations, translations, lexicons, editorial apparatus, comparative datasets,
retrieval channels, infrastructure probes, one monograph on metre (Arnold 1905).

**What the child will not find, because it is not there:** any excavation
report, site report, survey, archaeological dataset, museum object record, or
geographic source. Zero rows. `HOLD-007`.

**This card is the investigation's answer to its own question** and it is the
only screen where the child interrogates the museum rather than the poem.

---

## What is deliberately absent from every card

- **No image of a fort.** None exists that would not be a reconstruction
  (§10.4.4).
- **No map.** `PUR4J-018` — there is no geographic source, and a map would
  supply by adjacency what no source supplies.
- **No person, group, people or population as an operable term.** `PUR-022` and
  `PUR4J-030` carry names; they appear only inside quoted lines, read and never
  sorted (§10.4.7, and `04-rules-and-gates.md` §2).
- **No `INHERITED-UNVERIFIED` row.** The `the-forts` page headline
  ("Ninety-nine forts, in Indus country, three centuries too late") has no
  recorded source, is rated Medium risk / "Revise before release" by the
  curatorial audit, and does not appear anywhere in this investigation.
