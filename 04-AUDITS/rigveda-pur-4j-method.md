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

---

## 4. The counts — §4J's "90; 99; 100; other counts"

`03-REGISTERS/rigveda-pur-counts.csv`, 49 rows, one per numeral token in a
passage. Built by `rv-pur-counts.py` (instruments) then
`rv-pur-counts-adjudicate.py` (verdicts).

### 4.1 Finding the numerals without deciding in advance which ones matter

The numeral inventory was **not** assembled from the numbers §4J names. Every
one of the **721 distinct lemmas** occurring in the 103 passages was looked up
in Grassmann's gloss (`info/matched_lemmata.json`) and scanned for a German
number word. That returns **12 candidates** — small enough to adjudicate one by
one, and derived from the corpus's own lexicon rather than from expectation.

Ten were kept: `śatá-` 100, `navatí-` 90, `náva- 1` 9, `sahásra-` 1000,
`saptá-` 7, `pañcāśát-` 50, `trí-` 3, `śatatamá-` "hundredth", `éka-` 1,
`ubhá-` "both". Two were excluded, with the reason recorded in the script
rather than dropped silently:

- **`śatákratu-`** "having a hundred powers" — an Indra epithet. The hundred is
  a property of the god, never of a fort.
- **`ā́rya-`** — a **false positive of the scan**, matching *drei* inside
  Grassmann's gloss "Angehöriger der drei oberen Grosskasten". Not a numeral;
  and the gloss is itself an artefact for the §7 category audit, since it
  renders a Rigvedic word by the later caste system.

Recording the false positive matters more than removing it: it is the measure
of how noisy the instrument is, and one in twelve is the number.

### 4.2 The attachment test — three instruments, reported separately

`04-AUDITS/rigveda-pur-family-method.md` §7 measured that `navatí-` occurs in
family stanzas at **33.5× its corpus rate** and `śatá-` at 10.7×, and declined
to read the result: "a measurement of the profile and nothing more". §4J needs
the thing that measurement is not — whether a numeral **governs** `púr-`.

| Instrument | What it can show | Where it fails |
|---|---|---|
| **A. Agreement** — case, gender, number shared with the `púr-` token | strong when positive | **under-reports by construction.** `navatí-` is a feminine *singular* collective — "a ninety" — governing a plural `púraḥ`. It agrees in case and gender and never in number. A three-key agreement test drops **five of the six ninety-nine passages.** |
| **B. Proximity** — same pāda / hemistich / stanza | cheap, and orders candidates | a stanza routinely holds two numerals counting different things (§4.3) |
| **C. Translation** — how many of Griffith, Geldner, Grassmann and Elizarenkova render "N forts" | the only instrument reflecting someone who read the syntax | not independent of A and B; and Grassmann's translation is not independent of the Grassmann glosses that fixed the family (`DEP-021`) |

The three are carried through into the register in their own columns, and the
verdict is a separate column. **Six rows record the verdict overriding an
instrument**, each naming which instrument and why. That is the audit trail: a
reader can see exactly where the machine and the reading part company.

### 4.3 Why a stanza-level co-occurrence count cannot answer this

Three passages settle it, and the third is decisive.

- **RV 2.14.6** carries *two* `śatám`. Pāda a's counts Śambara's forts; pāda c's
  counts Varcin's men.
- **RV 6.48.8** carries *two* `śatám`. Pāda c's counts forts; pāda d's counts
  **winters** — a lifespan formula.
- **RV 10.104.8** carries `navatíṁ … náva ca` and the fort-word epithet
  `pūrbhít` in the same stanza. The ninety-nine counts **rivers**:
  `navatíṁ srotyā́ náva ca srávantīr`. Griffith "nine-and-ninety flowing
  streams"; Geldner "die neunundneunzig fließenden Ströme"; Grassmann "Die
  neunundneunzig Flüsse". All three agree, and `pūrbhít` is nominative singular
  masculine, an epithet of Indra, taking no numeral.

A stanza-level measure scores all three as "numeral co-occurs with fort word".
Two are wrong and the third is the control case for the whole unit.

### 4.4 What the corpus states, with the denominator

**21 of 103 passages state a count of the fort word. 82 state none** — 79.6%
of the passages that mention a fort at all do not say how many.

| Count | Passages | Where |
|---|---:|---|
| **100** | **8** | 1.53.8 · 2.14.6 · 4.27.1 · 4.30.20 · 6.48.8 · 7.3.7 · 7.16.10 · 9.48.2 |
| **99** | **6** | 1.54.6 · 2.19.6 · 4.26.3 · 7.19.5 · 7.99.5 · 8.93.2 |
| **7** | **4** | 1.63.7 · 1.174.2 · 6.20.10 · 7.18.13 |
| **90** | **2** | 1.130.7 · 3.12.6 |
| "hundreds" (`śatā́ni`, pl.) | 1 | 6.31.4 |
| "the hundredth" (ordinal) | 2 | 4.26.3 · 7.19.5 — both inside the 99 set |

§4J's "other counts" resolves to **seven** and to the unbounded plural
**"hundreds"**.

### 4.5 The three answers §4J and the reconciliation brief asked for

**Which passages state 99.** The six above. The reading is secure — the
padapāṭha analyses the words separately and Griffith, Geldner and Grassmann all
render 99 at all six — but **99 is never a single numeral**. It is two words,
`náva` "nine" and `navatí-` "ninety", joined by `ca` in three passages and
separated by intervening words in four. RV 1.54.6d splits them around the verb:
`púro navatíṁ dambhayo náva`.

**Is it modal?** **No. One hundred is**, 8 passages to 6 — 9 to 6 if the plural
"hundreds" is counted with the hundreds. This answers the question the
reconciliation brief left open at §2.6 item 2.

**Is it maximal?** No. 100, "hundreds" and 1000 are all larger.

**Then it is the most quotable**, and that is the third of the brief's three
options. `PUR4J-I-02` records what that does and does not establish.

### 4.6 The formulaicity question, tested rather than assumed

The task and the constitution both warn that "formulaic" is the convenient
answer. Four diagnostic predictions were fixed **before** the evidence was
read, and the result is not unanimous.

| Prediction if the count is an enumeration | Outcome |
|---|---|
| stable per opponent | **FAILS.** Śambara's forts are counted at 90, 99, 100, "the hundredth" and "hundreds" across six passages — every value §4J enumerates, on one opponent. |
| does not migrate to another class of object | **FAILS.** The identical `náva`+`navatí-` expression counts rivers at RV 10.104.8. |
| not systematically completed by a round number | **FAILS.** Two of six 99-passages append "the hundredth" (RV 4.26.3c `śatatamáṁ veśyàm`, 7.19.5c `nivéśane śatatamā́`). The 99 is functioning as one-short-of-a-hundred. |
| occasionally produces an irregular figure | **FAILS.** Every count is 7, 90, 99, 100 or "hundreds", across 21 passages, ten books and every Arnold stratum. No 23, no 41. |

**And one prediction the formula reading fails.** The numbers are *not* freely
interchangeable ornament: they sort by narrative cycle. Seven forts go with
Purukutsa and the Pūru in all four of their passages, in wording near-verbatim
at 1.174.2b and 6.20.10c (`saptá … púraḥ śárma śā́radīḥ`); 99 and 100 go with
Divodāsa, Atithigva and Śambara.

So the supported reading is narrower than the convenient one: **a formula
system with slots filled by cycle**, not "the numbers are meaningless".
`PUR4J-I-01` holds it at `PROVISIONAL`, states its falsifiers, and states
explicitly what it does not establish — that a formulaic count says nothing
about whether anything was besieged, and that the five-way typology is assigned
per passage and never inherited from this row.

### 4.7 One field this unit does not fill

Two of the six 99-passages complete the count with an ordinal that modifies a
**dwelling word** — `veśyà-`, `nivéśana-` — and not `púr-`. A search restricted
to numerals attached to the fort word misses the completion that gives the 99
its shape. This is noted as a limit of the extraction, not repaired by it.
