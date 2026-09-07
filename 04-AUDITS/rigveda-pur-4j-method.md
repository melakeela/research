# The §4J forts corpus — method

**Unit of work:** 2026-09-07
**Specification:** `00-CONTROLLER/METHODOLOGY-CONSTITUTION.md` §4J, lines 373–404
**Prior units:** `03-REGISTERS/rigveda-pur-family.csv` (28 claims),
`rigveda-pur-family-occurrences.csv` (106 tokens),
`04-AUDITS/rigveda-pur-family-method.md`,
`06-BRIEFS/rv01-reconciliation.md`
**Reproduce:** `04-AUDITS/rv-token-extract.py` →
`04-AUDITS/rv-pur-passage-build.py` → `04-AUDITS/rv-pur-passages-csv.py`

This note records what was done, in the order it was done, with the
denominator and the exclusions for every count. Findings and their statuses
are in the registers; the argument is in `06-BRIEFS/pur-4j-corpus.md`.

---

## 1. Retrieval, and the verification that preceded any counting

`VedaWebProject/vedaweb-data` re-cloned at commit
`d3eb8af7324338161520d2d35eae8f7e985a19a5`. **All twenty files of
`02-SOURCES/vedaweb-manifest-2026-09-07.md` reproduce their recorded sha256
and byte length exactly, zero mismatches**, and the ten-book TEI concatenation
reproduces `8d4711…c68a3`. `04-AUDITS/rv-token-extract.py` re-run against that
tree reproduces **164,758 tokens** over 10,552 stanzas and 39,832 pādas — the
figure `PUR-001` records.

The prior register is therefore reproducible from a commit SHA alone, for the
third recorded time (`SRC-019`, `SRC-047`, `SRC-059`, now `SRC-069`; one
retrieval target, four events, `DEP-020`).

Layers newly brought into use, pinned in
`02-SOURCES/vedaweb-manifest-2026-09-07-extension.md` and logged `SRC-070` …
`SRC-079`: `addressees.json`, `stanza_properties.json`, nine translations,
`vnh.csv`, and the printed-commentary locator indexes.

### 1.1 A file that does not do what its name suggests

`info/rv_locations.tsv` was flagged in the reconciliation brief §4 as possibly
bearing on §4J's *proposed geography*. It does not. Its eight columns are
`DOTS_AND_ZEROS`, `COMMAS_AND_ZEROS`, `DOTS`, `COMMAS`, `GRASSMANN`,
`BOOK_INDEX`, `HYMN_INDEX`, `STANZA_INDEX`: a citation-format conversion table.
"Location" means location *in the text*.

**There is no geographic content of any kind in this clone.** That is a fact
about the source, and it is what §4J's two geography fields have to be built
without.

### 1.2 A parser bug that produced wrong data, not missing data

The VedaWeb text and translation files are plain tab-separated, with no quoting
convention. Geldner, Grassmann and Griffith all open direct speech with a bare
`"`. Under Python's csv default that character opens a quoted field and the
reader consumes every following line until the next one.

The first build lost five Geldner rows and one Grassmann row. **The rows were
not merely absent: they had been merged into their neighbours, so surviving
passages carried the wrong translation text.** Reading `csv.QUOTE_NONE` fixes
it, and the check that the fix is complete is that all four full-coverage
translations now return 10,552 distinct stanza ids over the whole corpus, as do
Aufrecht, van Nooten–Holland and the padapāṭha.

Recorded because a silent merge is exactly the failure that a coverage count
catches and a spot-check does not: RV 4.26.3, the passage this unit most needed,
was **not** among the six that broke.

---

## 2. The row unit, and why it is the stanza

The reconciliation brief's conflict **C-1** is that both specifications make the
row a *passage* while the register's row is a *token*, and neither specification
says what a passage is. The candidates it lists are 106 tokens / 104 pādas /
103 stanzas / 86 hymns.

**Fixed here as the stanza (ṛc). 103 rows.** Four reasons, in order of weight:

1. **The §4J fields are properties of a stanza-sized unit.** Patron, opponent,
   material, water, cattle, treasure and a stated count are things a passage
   *says*. A pāda is one line and routinely splits a clause — RV 4.26.3 puts
   `púraḥ` in pāda a and the numeral `navatī́ḥ` that governs it in pāda a as
   well but `śámbarasya`, whose forts they are, only in the same hemistich. A
   hymn runs to dozens of stanzas on several subjects, and attributing one
   stanza's fort description to all of them would manufacture evidence.
2. **It is the corpus's own unit.** `strata.json`, `addressees.json`,
   `stanza_properties.json` and all nine translations are stanza-keyed. Nothing
   has to be interpolated to build a stanza row.
3. **The stratum column survives the choice, and this was measured rather than
   assumed.** All 103 passages are internally uniform in Arnold stratum code —
   the build reports zero non-uniform passages. So aggregating pāda-level
   stratum to the stanza loses nothing. Had any stanza mixed codes, the choice
   would have cost evidence and would have had to be argued differently.
4. **It is the unit the reader can check.** A stanza is what a translation
   translates and what a citation addresses.

### 2.1 The denominator, and every exclusion in it

| | Count | What it is |
|---|---:|---|
| Family tokens (`PUR-005`, re-verified here) | **106** | word-tokens of the seven lemmas |
| → distinct pādas | 104 | 2 lost: two pairs share a pāda |
| → **distinct stanzas = passage rows** | **103** | 3 lost: three stanzas carry 2 tokens each |
| → distinct hymns | 86 | — |

The three stanzas carrying two family tokens are **RV 1.53.7** (`purā́ púram`,
both in pāda b), **RV 6.32.3** (`púraḥ purohā́`, both in pāda c) and
**RV 8.1.8** (two tokens in *different* pādas).

The reconciliation brief §5 C-1 names only the first two, because it was
reasoning about the pāda unit, where 8.1.8's two tokens fall in different rows
and do not collide. At the stanza unit there are three. **106 − 3 = 103**, and
this is the arithmetic behind every "103" in this unit.

### 2.2 What the 103 excludes, restated so no count travels without it

- **`púraṃdhi-` and its two compounds, 50 tokens.** Excluded on Grassmann's
  gloss "Segensfülle" (`PUR-006`). This is a live judgement, not a settled
  fact — `HOLD-001`. Admitting it would make the family 156 tokens and the
  passage corpus correspondingly larger.
- **`purāṣáh-`, 1 token, RV 10.74.6a.** Excluded on Grassmann's gloss alone.
- **Six fort-adjacent lemmas not derived from `púr-`** — `paridhí-`, `dehī́-`,
  `saṃdíh-`, `harmyá-`, `ádhr̥ṣṭa-`, `dārú-`. Excluded **by design**: the
  membership test is etymological, not semantic. On a semantic reading of "the
  complete corpus" these belong in it. Reconciliation brief C-2.
- **`púr-` tokens in passages that are not about a fort.** These are *in* the
  103 and may not belong in a corpus of forts. Same conflict, other direction.

The 103 is therefore **the etymological corpus at the stanza unit**, and that
phrase, not "the forts corpus", is what the number means.

### 2.3 What this does to the 99/106 question

Nothing, and that is the point. `06-BRIEFS/rv01-reconciliation.md` §2.4
established that no sub-count the register supports equals 99. **103 is a
fourth number, and it is not 99 either.** It is the size of the table, not a
value in it. §4J's 90, 99 and 100 are values *inside* passages, and §3 of this
note goes after them directly.

---

## 3. What the passage index carries

`03-REGISTERS/rigveda-pur-passages.csv`, 103 rows, measurements only.

Address (`passage_id`, `stanza`, `book`, `hymn`, `stanza_n`); the family tokens
with surface, lemma, pāda, token index and full morphology; the Arnold metre
labels and stratum code with its certainty flag; the hymn's addressee and
poet-group heading; the five scholars' stanza-level lateness flags; the
Saṃhitā text and the padapāṭha in full; and which of the nine translations
carry the passage and which do not.

No column in this file says what a passage means, who held a fort, where one
was, or what type it is. Those are later sections and separate registers.

### 3.1 Two things the file says by not saying them

- `stanza_properties_flags` reads `(none)` for **90 of 103** passages. That is
  **NOT PRODUCED** under the negative-evidence standard — none of the five
  scholars marked the stanza — and it is *not* a judgement that the stanza is
  authentic or early. The flagged 13 break down as Grassmann 8, Witzel 5,
  Arnold 1897 4, Oldenberg 1, Wüst 1 (a stanza may carry more than one).
- `translations_absent` is populated for every passage, because Macdonell,
  Müller, Otto and Oldenberg's translations are anthology selections. A missing
  Renou at a stanza is a fact about Renou's selection, **NOT PRODUCED**, and
  carries no information about the stanza.
