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

The numeral inventory was **not** assembled from the numbers §4J names.
`04-AUDITS/rv-pur-numeral-scan.py` scans every one of the **721 distinct
lemmas** occurring in the 103 passages and returns **26 candidates** — 11 from
an unambiguous number word, 15 from an ambiguous one, 0 from a stem fallback —
small enough to adjudicate one by one, and derived from the corpus's own
lexicon rather than from expectation.

**The first version of this scan was not exhaustive, and the claim that it was
is withdrawn** (`PUR4J-031`). It matched German number words with hard word
boundaries against glossed lemmas only, and leaked three ways:

1. **Gloss coverage.** Only **585 of 721** lemmas carry a Grassmann gloss. The
   scan reached 81% of the lexicon and the unit called it exhaustive.
2. **Word boundaries.** `\bhundert\b` matches "hundert Kräfte" and fails on
   "hundertfache", so `śatā́magha-` and `śatā́tman-` were never candidates.
3. **German only.** Grassmann glosses `śatábhuji-` as **"centuplex"** — Latin.
   No German number word appears in it at all.

And the scan script was **not committed**: `rv-pur-counts.py` hard-coded the
result, so the "12 candidates" figure could not be checked against anything.
All four repairs are in place. The stem fallback returning **zero** now
*demonstrates* that the 136 glossless lemmas cost nothing here, where before it
was an assumption nobody had tested.

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
| **100** | **9** | 1.53.8 · 2.14.6 · 4.27.1 · 4.30.20 · **6.31.4** · 6.48.8 · 7.3.7 · 7.16.10 · 9.48.2 |
| **99** | **6** | 1.54.6 · 2.19.6 · 4.26.3 · 7.19.5 · 7.99.5 · 8.93.2 |
| **7** | **4** | 1.63.7 · 1.174.2 · 6.20.10 · 7.18.13 |
| **90** | **2** | 1.130.7 · 3.12.6 |
| "the hundredth" (ordinal) | 2 | 4.26.3 · 7.19.5 — both inside the 99 set |

§4J's "other counts" resolves to **seven**, and to nothing else.

**RV 6.31.4 was first read as "hundreds", an unbounded figure, and given its own
category.** That was wrong twice: `śatā́ni` there is the same form as `śatā́` at
RV 1.53.8 — ACC.N.PL of `śatá-` — which this register reads as "a hundred", so
the rule was applied inconsistently *within* the register; and Griffith,
Geldner and Grassmann are unanimous for "a hundred" at 6.31.4, a departure the
row recorded no override for. Neuter plural of `śatá-` with a plural noun is the
ordinary Vedic way of saying "a hundred X".

### 4.5 The three answers §4J and the reconciliation brief asked for

**Which passages state 99.** The six above. The reading is secure — the
padapāṭha analyses the words separately and Griffith, Geldner and Grassmann all
render 99 at all six — but **99 is never a single numeral**. It is two words,
`náva` "nine" and `navatí-` "ninety", joined by `ca` in three passages and
separated by intervening words in four. RV 1.54.6d splits them around the verb:
`púro navatíṁ dambhayo náva`.

**Is it modal?** **No. One hundred is, 9 passages to 6.** This answers the
question the reconciliation brief left open at §2.6 item 2.

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

**And two things cut the other way.** First, the numbers are *not* freely
interchangeable ornament: they sort by narrative cycle. Seven forts go with
Purukutsa and the Pūru in all four of their passages, in wording near-verbatim
at 1.174.2b and 6.20.10c (`saptá … púraḥ śárma śā́radīḥ`); 99 and 100 go with
Divodāsa, Atithigva and Śambara. Second, the strongest diagnostic is gone.

So the reading rests on **two clear diagnostics of four**, not three, and the
supported version is narrower than the convenient one: **a formula system with
slots filled by cycle**, not "the numbers are meaningless". `PUR4J-I-01` holds
it at `PROVISIONAL`, carries the withdrawal in its own `evidence_against` cell,
states its falsifiers, and states explicitly what it does not establish — that
a formulaic count says nothing about whether anything was besieged, and that
the five-way typology is assigned per passage and never inherited from this
row.

### 4.7 One field this unit does not fill

Two of the six 99-passages complete the count with an ordinal that modifies a
**dwelling word** — `veśyà-`, `nivéśana-` — and not `púr-`. A search restricted
to numerals attached to the fort word misses the completion that gives the 99
its shape. This is noted as a limit of the extraction, not repaired by it.

---

## 5. The semantic fields — §4J's patron, poet lineage, opponent, description, material, water, cattle, treasure, mountain or river, geography

`03-REGISTERS/rigveda-pur-fields.csv`, 103 rows. Built by
`04-AUDITS/rv-pur-fields.py`, which states every definition in its own docstring
**before** the field is filled.

The reconciliation brief §6 said of water, cattle and treasure: *"Not
retrievable until the semantic fields are stated. Undefined, they become places
to put what the reader already believes."* That is the risk this section is
built against, so each definition is a **rule over the corpus's own lexicon** —
Grassmann's glosses for all 721 lemmas occurring in the 103 passages — rather
than a word list chosen for what it would show.

### 5.1 Description and material: agreement, at three scopes, both of which fail

A descriptor is defined as a token agreeing with a `púr-` family token in
**case, gender and number**. Agreement is the corpus's own marking of
attribution; nothing is called a descriptor for sounding like one.

**All three scopes are reported in separate columns, because each has a
demonstrated failure and they fail in opposite directions.**

| Scope | Passages | Its demonstrated failure |
|---|---:|---|
| same pāda | 43 | **Misses** `āyasá-` at RV 7.15.14 — a predicate nominative two pādas from its subject `pū́ḥ`, and the passage where the metal-fort image is clearest. Also misses `aśmanmáya-` at RV 4.30.20 across a pāda break. |
| same hemistich | +22 | intermediate |
| elsewhere in stanza | +23 | **Admits** `srúc-` "wooden sacrificial ladle" at RV 5.41.12, NOM.PL.F agreeing with `púraḥ` but in a different clause; and `ádri-` "rock" at RV 7.6.2, GEN.SG.M agreeing with `puraṃdarásya` but belonging to "they bring him from the mountain". |

A single scope would have to choose which error to make. Three columns let the
reader see the evidence. The two false positives are listed per row in
`agreeing_but_excluded`, with the reason, rather than deleted.

### 5.2 What the forts are made of

**Three lemmas, ten passages of 103.**

| Lemma | Gloss | Passages |
|---|---|---:|
| `āyasá-` | "eisern" — of metal | 8 |
| `aśmanmáya-` | "steinern, aus Fels gemacht" | 1 |
| `āmá-` | "roh, ungekocht" — raw, unbaked | 1 |

93 of 103 state no material. **NOT PRODUCED**: a hymn celebrating the breaking
of a fort had no occasion to say what it was built of, and the silence is not
evidence that the poets did not know or that the forts were insubstantial.

**The distribution of the metal forts is the finding.** Seven of the eight are
protective, mythic or metaphorical, and only **one** is an enemy's:

| | Passage | What the metal fort is |
|---|---|---|
| 1 | RV 1.58.8 | Agni asked to protect the singer **with** iron forts |
| 2 | **RV 2.20.8** | **Indra casts down the Dasyus' iron forts — the only enemy fort** |
| 3 | RV 4.27.1 | a hundred iron forts **confine** the speaking eagle |
| 4 | RV 7.3.7 | Agni asked to protect us with a hundred iron forts |
| 5 | RV 7.15.14 | `pū́r bhavā śatábhujiḥ` — Agni asked **to be** an iron *púr* |
| 6 | RV 7.95.1 | `sárasvatī dharúṇam ā́yasī pū́ḥ` — **the river Sarasvatī is** an iron *púr* |
| 7 | RV 8.100.8 | the falcon **escapes** the iron fort |
| 8 | RV 10.101.8 | priests told to **make** iron forts, in a ritual exhortation |

This is the measurement that bears hardest on §4J's *"Do not automatically
translate pur into a Mature Harappan city."* The metal forts are overwhelmingly
not enemy settlements, and in two passages the fort **is** a god or a river. A
reading that takes `āyasá- púr-` as evidence for metal-using fortified
settlements has to account for the seven, not only the one.

**The challengeable case, anticipated.** RV 4.27.1 and 8.100.8 — a hundred
metal forts confining the eagle in the Soma-theft myth — could be called
hostile: something adversarial is holding the bird. They are counted among the
seven because the claim is about a specific thing, *the stronghold of a named
adversary, stormed*, and in those two the holder is unnamed, the setting is a
myth of Soma's descent rather than a raid, and the action is escape rather than
assault. Counting them as hostile makes it **3 of 8 rather than 1 of 8**, and
does not disturb what the row is used for: on either count a majority of the
metal forts are not enemy settlements, and RV 7.15.14 and 7.95.1 — where the
fort *is* Agni and *is* the river Sarasvatī — are unaffected either way.

The one stone fort (`aśmanmáya-`, RV 4.30.20) *is* an enemy's; the one unbaked
fort (`āmá-`, RV 2.35.6) is a refuge. Two data points, recorded as two data
points. With n=1 on each side no distribution follows.

### 5.3 Water, cattle, treasure, mountain — and the two exclusions that changed the numbers

| Field | Passages of 103 | Led by |
|---|---:|---|
| water | 17 | `áp-` 8, `síndhu-` 6 |
| cattle | 13 | `gáv- ~ gó-` 5, `vrajá-` 3 |
| treasure | 12 | `dhána-` 2, `rayí- ~ rāy-` 2 |
| mountain | 7 | `ádri-` 3, `girí-` 2 |
| river lemma present | 6 | `síndhu-` in all six — but see below |

Two exclusions were needed, and **both changed the result**:

- **Bahuvrīhi "having X" epithets.** Without excluding glosses containing
  *habend, besitzend, gewinnend, findend, enthaltend, spendend*, the treasure
  field returns **56 lemmas**, most of them epithets of Indra —
  `bhū́ridātra-` "gabenreich", `śatā́magha-` "hundertfache Fülle besitzend",
  `sudákṣiṇa-` "schöne (freigebige) Rechte habend". It is the field most
  exposed to the brief's warning, and the one most tightened.
- **Owner words.** `páti-` "Herr, Gebieter, **Besitzer**" enters treasure in
  five passages on the string *Besitz*. A word for the owner of a thing is not
  the thing.

A third filter removes Grassmann's **usage notes**: `ádhr̥ṣṭa-`
"unwiderstehlich *(gesagt von Göttern, Felsen, Burgen etc.)*" is not a word for
a mountain — the match is in the note, not in the sense.

These are recorded because each is a place where an undefined field would have
returned a larger and more impressive number.

**And one correction this unit owes itself.** The river column was first headed
*named river* and the claim first read "the Sindhu in all six". That is wrong.
`síndhu-` is the only lemma in the 103 passages that can name a river — an
independent scan of all 721 lemmas for a Grassmann gloss marking a river name
returns it and nothing else — but Grassmann glosses it **"Fluss, Strom; der
Indus"**, the common noun and the proper name at once, and the translators
split: proper name at RV 1.103.8, 1.109.8 and 10.111.10; common noun at
RV 7.95.1 and (plural) 10.89.7; **disputed** at RV 10.104.8, where Griffith has
"the ocean" and Geldner "die Sindhu". The column is now `river_lemma_present`
and carries the caveat on every row (`PUR4J-028`).

This matters out of proportion to its size: a hydronym is the only thread in
this corpus that could ever reach a geography, and the thread is thinner than a
lemma count makes it look. A scan for a lemma glossed as the name of a
**mountain** returns nothing at all, so §4J's *mountain or river* resolves to
common nouns for high ground plus one ambiguous hydronym.

### 5.4 Patron and opponent: what the column is, and what it is not

Names are identified by Grassmann's gloss marking a proper name, then split by
**the role word in Grassmann's own gloss** — *Schützling, Günstling, König,
Fürst, Sänger* to the patron side; *Dämon, Feind, Dasyu, bekämpft, getötet* to
the opponent side. 22 passages carry a patron candidate, 22 an opponent
candidate.

**A bug found by reading the output rather than the code.** The first run put
`purukútsa-` and `trasádasyu-` on the **opponent** side. Both are glossed
*Schützling* — protégé — and Purukutsa is a king; the match was the string
*Dasyu* inside **Trasa**dasyu, and inside Purukutsa's own gloss "des
Trasadasyu Vater". Since Purukutsa is the patron of the seven-fort cycle
(`PUR4J-010`), the bug put the register in contradiction with this unit's own
claim. Three corrections followed: word boundaries on the role words; an
explicit protégé marker settles the side even when the gloss also names an
adversary, because a king is often described by who he was protected against;
and a deity filter, without which `váruṇa-` entered the **patron** column on
the string *Götterkönig*. Opponent candidates fell from 26 passages to 22.

The columns are headed `_candidates` for a reason, stated on every row:

> Grassmann's classification of the **name**, not a reading of this passage's
> syntax. A name can occur in a passage without holding or attacking anything
> in it.

`PUR-027` exists at `HYPOTHESIS` precisely so that the collocation profile is
not mistaken for a claim about who held a fort, and nothing here promotes it.

**And the field imports Grassmann's categories.** *Dämon* is one of them, and
it is doing real work: it is what sorts Śambara, Pipru, Śuṣṇa, Namuci, Varcin,
Vaṅgṛda, Kuyava, Cumuri and Dhuni onto the opponent side of this register.
The constitution §7 list of inherited categories to audit before use — *race,
tribe, slave, barbarian, fort, religion, caste, civilization, invasion,
indigenous* — does not name **demon**, and on the evidence of this field it
should. Logged in `04-AUDITS/REAUDIT-QUEUE.csv`.

### 5.5 Poet lineage — filled at three removes, and held

Geldner's per-hymn group heading names a poet for **55** of the 103 passages.
For the other **48** it names a deity (45 — "hymns to Indra" alone accounts for
26), a metre (1), a collection (1), or a strophe-type that is also a poet's
name (1: "the Pragātha group" at RV 9.107.10, counted as *not* a poet
attribution, which is the conservative reading; the other way the split is
56/47). The 48 are **NOT PRODUCED**, not anonymous: the headings are an
arrangement, and where Geldner arranged by deity he recorded no poet.

The 55 that carry a name carry it at three removes — Geldner 1951 follows the
Anukramaṇī tradition, and that tradition post-dates the text. `HOLD-006`
records that no independent source was reachable: GRETIL, archive.org and TITUS
each returned **403 at the proxy** (`SRC-080`–`SRC-083`), having each returned
**200 earlier the same day** (`SRC-028`, `SRC-025`, `SRC-033`). The egress
policy differs between sessions on this environment, which is `D-042`'s point
with a worked instance attached.

The standing tradition that books 2–7 are the family books of Gṛtsamada,
Viśvāmitra, Vāmadeva, Atri, Bharadvāja and Vasiṣṭha would supply a lineage for
much of the corpus from the book number alone. **It is asserted nowhere in this
unit**, because no retrieval in this container establishes it and confidence
does not promote a claim.

### 5.6 Geography — not filled, and typed

`info/rv_locations.tsv` is a citation-format conversion table (§1.1). **There is
no geographic content in the pinned corpus.** The field carries
`NOT FILLED — no source` on all 103 rows, with the reason in
`geography_basis`. What the corpus supports is which hydronym lemmas occur —
`síndhu-` in six passages — which is a textual fact. The step from a hydronym to
a place on a map is a separate claim, and it is bounded by the research hold at
Version 12 line 1175 against identifying the forts with one archaeological
culture.

---

## 6. The five-way typology

`03-REGISTERS/rigveda-pur-typology.csv`, 103 rows, built by
`04-AUDITS/rv-pur-typology.py`.

### 6.1 The finding that decides the register's shape

§4J asks that five things be distinguished:

> textual stronghold · poetic formula · inferred geography ·
> archaeological fortification · unsupported identification

**They are not five values of one variable.** Two are properties of the text;
three are verdicts on an argument someone else has to make first:

| Type | What it is a property of |
|---|---|
| textual stronghold | the passage |
| poetic formula | the passage |
| inferred geography | *a placement somebody proposed* |
| archaeological fortification | *a site match somebody proposed* |
| unsupported identification | *an identification somebody proposed* |

The last three cannot be read off a Rigvedic stanza **in any state of
knowledge**, because none of them is about the stanza. This unit has no
geographic source — the pinned corpus carries none (`PUR4J-018`) — and no
archaeological source. So **no passage is assigned any of the three.** All 103
rows read `NOT ASSIGNED` in those three columns, with the reason on the row
rather than an unexplained blank.

Assigning them anyway would be the exact failure the typology exists to
prevent: it is how a textual stronghold silently becomes an archaeological one.
The reconciliation brief's C-7 makes the same point from the other end — the
typology is "the instrument that keeps a textual stronghold from becoming an
archaeological one", and RV-01 dropped it.

### 6.2 The two text-decidable types, and what they mean

`TEXTUAL-STRONGHOLD` means **the text presents a fort as an object in its own
narrative world** — held, broken, entered, or belonging to a named holder. It
is **not** a claim that any fort existed, was fortified, or can be located.
That would be the archaeological type, which is not assigned. This definition
is carried on every row in a `type_means` column, because the term invites
exactly the misreading it is trying to prevent.

`POETIC-FORMULA` is recorded with one of four sub-kinds, so that "formulaic"
never has to be taken on trust: `DIVINE-EPITHET`, `SIMILE`, `METAPHOR`,
`PROTECTIVE-FORMULA`.

`BOTH` is available, because §4J says *distinguish*, not *choose*. A stronghold
described in formulaic language is both, and forcing one label would destroy
the distinction the section asks for.

`CANNOT-CLASSIFY` is used where the text does not decide — **not** resolved to
the likelier type.

### 6.3 Result

| | With hand overrides | Rules alone |
|---|---:|---:|
| TEXTUAL-STRONGHOLD | **48** | 54 |
| POETIC-FORMULA | **47** | 47 |
| BOTH | 3 | 0 |
| CANNOT-CLASSIFY | 5 | 2 |

Poetic sub-kinds: `DIVINE-EPITHET` 27, `SIMILE` 9, `METAPHOR` 6,
`PROTECTIVE-FORMULA` 5. **Both columns are published**, and every row carries
`type_before_override`, because nine hand judgements over 103 passages are
enough to move a headline and §6.4 shows one they move.

**These are the corrected figures, and the correction is worth its own
paragraph.** The first run returned 60/35, and a stress test of rule R5 —
asking which `TEXTUAL-STRONGHOLD` passages have *neither* a breaking root *nor*
a named opponent — exposed a systematic gap. The corpus builds the
`puraṃdará-` epithet **analytically** as well as lexically: a genitive plural
`purā́m` depending on an agent noun of breaking — `purā́m bhindúr` "breaker of
forts" (RV 1.11.4), `púrāṁ dartaḥ` "O splitter of forts" (1.130.10),
`bhettā́ purā́ṁ śáśvatīnām` "breaker of all forts" (8.17.14), `dartā́ purā́m
ási` "thou art the splitter of forts" (8.98.6), and four more. Those tokens are
simplex `púr-`, so rule R1, which keys on the lexicalised epithet lemmas, could
not see them. **Nine of the ten genitive-plural passages are this.** The tenth,
RV 4.30.20, is a genuine object, where `purā́m` is governed by `śatám` "a
hundred".

Two metaphors were missed for related reasons — RV 7.52.1 `pū́r devatrā́`
"a *púr* among gods and among mortals" and RV 8.80.7 `índra dŕ̥hyasva pū́r
asi` "Indra, be firm: thou **art** a *púr*" — and one simile, RV 6.2.7
`raṇváḥ purī́va jū́ryaḥ`, where the particle is `iva` rather than `ná`. The
`iva` rule has the same false-positive profile as the `ná` rule: of the three
passages with `iva` in a *púr-* pāda, only this one modifies the fort word
(RV 2.14.6 has `áśmaneva` "as with a stone", RV 10.138.4 `māséva` "like the
moon").

**The correction moved 11 passages and changed none of the unit's headline
findings** (`PUR4J-029`). Every cell of both cross-tabulations in §6.4 is
unchanged, because the eleven that moved are exactly the passages with no
stated count and no stated material. Had even one ninety-nine passage moved out
of `TEXTUAL-STRONGHOLD`, §6.4 would have needed rewriting.

**The five that cannot be classified**, each for a stated reason:

- **RV 1.149.3** `púraṁ nā́rmiṇīm`. Proper name (Geldner, "die Burg Nārmiṇī" —
  then the only named fort in the corpus) or adjective (Griffith, "the joyous
  castle"). Grassmann's gloss declines to choose. The classification turns
  entirely on a disputed word class.
- **RV 2.35.6** `āmā́su pūrṣú`. A locative, so someone is in it — but the
  subject is Apāṃ Napāt, and whether the *púr* is a place or a figure of
  inaccessibility is undecided.
- **RV 5.66.4** `dákṣasya pūrbhíḥ`. Geldner "mit den Burgen des Verstandes"
  (metaphor); Grassmann renders the phrase with no fort word at all; Griffith's
  line is garbled. Three translators, three different things, no majority to
  lean on.
- **RV 8.1.28** `púraṁ cariṣṇvàṁ … śúṣṇasya`. Śuṣṇa's **moving** fort.
  `cariṣṇú-` is not compatible with a fixed fortification and the passage
  supplies no replacement reading.
- **RV 10.138.4** `vásu púryam`. `púrya-` is an adjective modifying "wealth";
  a *púr* is implied by a derived form and never named.

**Nine rule outputs were overridden by hand**, each with its reason on the row.
The simile rules have the highest error rate and it is reported rather than
smoothed: `ná` stands in a `púr-` pāda in ten passages and modifies the fort
word in **seven** (at RV 4.16.13 the simile is "like a garment", at 6.20.7 it
goes with `śávasā`, at 10.89.7 with `síndhūn`); `iva` stands in three and
modifies it in **one**. All were checked against Griffith, Geldner and
Grassmann individually.

### 6.4 The cross-tabulation, which is the sharpest result of the unit

| Count stated | Typology of the passages stating it |
|---|---|
| **99** | **6 of 6 TEXTUAL-STRONGHOLD** |
| 90 | 2 of 2 TEXTUAL-STRONGHOLD |
| 7 | 4 of 4 TEXTUAL-STRONGHOLD |
| 100 | 5 TEXTUAL-STRONGHOLD · 3 POETIC-FORMULA · 1 BOTH |

**Every passage that states ninety-nine forts presents forts as objects held
and broken.** §4 of this note finds the *count* formulaic; this finds the
*passages* are not. "The number is a formula" and "the passage is a formula"
are different claims, and the evidence separates them. That is why the counts
and the typology are separate registers, and it is the single most important
guard in this unit against the deflationary slide the task warned about.

The three poetic hundreds are the protective passages — "guard us with a
hundred forts" — where the count is on a defence being asked for, not on a
target.

And from the other direction, converging with §5.2:

| Material passages that are **not** plain textual strongholds | |
|---|---:|
| on the hand classification | **8 of 10** |
| on the rules alone | **4 of 10** |

**This is the cross-tabulation the overrides move, and the first version of
`PUR4J-027` overstated it.** Four of the register's nine hand overrides fall
inside these ten passages — against 0.9 expected under even allocation — and all
four move away from `TEXTUAL-STRONGHOLD`. They alone produce the 8. The row also
described itself as converging *independently* on §5.2; it does not, since it
re-tabulates the same hand judgements over the same ten passages. Both figures
are now published.

What survives without any override is the weaker and still substantive **4 of
10** — the metaphors at RV 7.15.14 and 7.95.1, where the fort **is** Agni and
**is** the river Sarasvatī, and the protective formulas at RV 1.58.8 and 7.3.7.
No override touches those four. **Anyone reading fort materials as evidence for
building technique is still reading a large minority of figurative passages, and
on the hand reading a majority.**

---

## 7. Measurements against interpretations

The constitution requires the two be separated, and they are separated by file,
not by paragraph.

| File | Contains | Statuses |
|---|---|---|
| `03-REGISTERS/rigveda-pur-passages.csv` | the passage index: address, family tokens with morphology, Arnold metre and stratum, addressee, poet group, Saṃhitā and padapāṭha text, which translations carry it | measurement |
| `03-REGISTERS/rigveda-pur-counts.csv` | one row per numeral token, three instruments in their own columns, a verdict column, and an override column | measurement |
| `03-REGISTERS/rigveda-pur-fields.csv` | §4J's semantic fields, each defined before it was filled | measurement |
| `03-REGISTERS/rigveda-pur-typology.csv` | the five-way classification | reading — every row `PROVISIONAL` |
| `03-REGISTERS/rigveda-pur-4j-claims.csv` | 32 claims | 22 `VERIFIED`, 10 `PROVISIONAL` |
| `03-REGISTERS/rigveda-pur-4j-interpretations.csv` | 3 readings, each with evidence for, **evidence against**, what it does not establish, and falsifiers | all `PROVISIONAL` |

Nothing in this unit is `VERIFIED` on the strength of an argument. Every
`VERIFIED` row is a count, a form, a gloss, or a printed rendering, with a
locator that re-finds it.

**Five rows failed that test and were demoted on review.** `PUR4J-007` (whose
forts are whose), `PUR4J-010` (the count co-varies with the narrative cycle),
`PUR4J-013` and `PUR4J-014` (what the material passages show) and `PUR4J-024`
(what the typology's three unassignable types are) are hand classifications and
readings, not counts, forms, glosses or renderings. `PUR4J-025`–`027`, which are
the same kind of judgement, were already `PROVISIONAL`; these were not, and the
inconsistency was the reviewer's finding. `PUR4J-024` also claimed the three
types cannot be assigned *"in any state of knowledge"* — a modal claim about all
possible evidence, on a locator that established only what the columns currently
read. It now says what the locator supports.

**Every count in this unit carries its denominator.** 21 **of 103** passages
state a count; 6 **of 21** state 99; 3 **of 83** simplex tokens are locative;
10 **of 103** state a material; 55 **of 103** have a poet-naming heading. Where a count has exclusions, they are named at the point
of use: §2.2 lists the four exclusions behind the 103, and §4.1 and §5.3 list
the gloss-scan exclusions behind the numeral and semantic-field inventories.

---

## 7A. Reproduction, checked

The four registers were regenerated in a clean directory from the pinned commit
and the committed scripts, and **all four are byte-identical to the committed
files**:

```
CL=/home/user/vedawebproject/vedaweb-data/rigveda      # clone @ d3eb8af

python3 04-AUDITS/rv-pur-numeral-scan.py    $CL  rv_pur_passages.json   # candidate inventory
python3 04-AUDITS/rv-token-extract.py       $CL/TEI            rv_tokens_vedaweb.tsv
python3 04-AUDITS/rv-pur-passage-build.py   $CL  rv_tokens_vedaweb.tsv  rv_pur_passages.json
python3 04-AUDITS/rv-pur-passages-csv.py    rv_pur_passages.json   03-REGISTERS/rigveda-pur-passages.csv
python3 04-AUDITS/rv-pur-counts.py          rv_pur_passages.json   rv_pur_counts.tsv
python3 04-AUDITS/rv-pur-counts-adjudicate.py  rv_pur_counts.tsv   03-REGISTERS/rigveda-pur-counts.csv
python3 04-AUDITS/rv-pur-fields.py          rv_pur_passages.json  $CL  03-REGISTERS/rigveda-pur-fields.csv
python3 04-AUDITS/rv-pur-typology.py        rv_pur_passages.json   03-REGISTERS/rigveda-pur-typology.csv
```

`rv_tokens_vedaweb.tsv` (30 MB) and `rv_pur_passages.json` (582 KB) are derived
and not committed; both regenerate byte-for-byte from the commit SHA.

**Note the argument orders, which differ between scripts** —
`rv-pur-passage-build.py` takes the clone first and the token file second,
while `rv-pur-fields.py` takes the passages file first and the clone second.
Getting this wrong produces a `NotADirectoryError` rather than a wrong answer,
so it fails loudly; it is recorded because the first reproduction attempt made
exactly that mistake.

---

## 8. The two adversarial tests

Constitution §8. Both run before this unit was called finished.

### 8.1 Prestige-bias challenge

*Did this privilege a claim because it is canonical, Sanskritic, Brahmanical,
Indo-European, European, colonial, institutionally prestigious, repeatedly
cited or nationally useful?*

**Caught, and corrected inside the unit.** Four instances.

1. **Grassmann was about to be counted twice.** His *Wörterbuch* glosses fixed
   the family boundary (`PUR-006`); his 1876–7 translation is one of the five
   in the §7 tally; his gloss category `Dämon` sorts the opponent field. Three
   apparently independent supports, one man. Logged as `DEP-021` **before** the
   translations were used, not after. The §7 brief states it in the table where
   the tally appears.
2. **Arnold was about to be counted twice.** `stanza_properties.json` carries an
   `arnold` column — Arnold 1897, the *Sketch*, on grammar. The register's
   stratum column is Arnold 1905, on metre. Same author, eight years apart.
   Logged as `DEP-022` before the file was opened. This is the trap that
   produced correction `C-05`, and it was set again by a new data file.
3. **The prestige of the machine over the reading.** The mechanical agreement
   test is reproducible, scriptable and wrong about `navatí-`: it is a feminine
   singular collective governing a plural, so a case/gender/number test drops
   **five of the six** ninety-nine passages by construction. Deferring to the
   instrument would have produced a tidy, reproducible, false result. Six rows
   record the override, each naming the instrument it overrides.
4. **The prestige of the standard translation.** Geldner is the reference
   translation, and that is a fact about its reception, not its correctness —
   the ledger row `SRC-072` says so. Where Geldner and Griffith disagree
   (`āyasá-`, `nā́rmiṇī-`) the disagreement is recorded as an open crux and
   neither is preferred.

**One live risk not fully closed.** The whole unit rests on a single German
philological line: Grassmann's lexicon, Grassmann's, Geldner's and Griffith's
translations, Arnold's metre, Zürich's morphology. Elizarenkova and Renou sit
inside the same tradition. **There is no non-European scholarly source anywhere
in this unit**, and none was reachable (`SRC-080`–`SRC-083`). Sāyaṇa's
commentary — the indigenous exegetical tradition, and the one Griffith leaned
on — is not in the pinned corpus and was not retrieved. That is an archival
asymmetry, not a neutral fact about what exists, and it is recorded here rather
than in a caveat at the end. Queued as `RA-015`.

### 8.2 Preferred-counter-narrative challenge

*Did this accept a claim too easily because it is Dravidian, Indigenous,
anti-colonial, anti-Brahmanical, subaltern, diffusionist or politically
corrective?*

**The available soft landing was named in advance, and the refusal was
partly successful and partly not.** The reconciliation brief §7 identified it:
*"declare 99 formulaic and be done — a conclusion that flatters a deflationary
reading of Rigvedic conflict and costs nothing to assert."* The task restated
it. Four controls were put in place, and **this test failed to catch the one
place the landing was taken**.

**What it missed.** `PUR4J-007`, the strongest of the four diagnostics, was
false in three of five parts, and all three errors ran toward the deflationary
conclusion (§4.6). The independent reviewer found them. The reason this section
did not is precise and worth stating: **it interrogated the conclusion instead
of re-deriving the evidence.** It asked whether the formula reading had been
adopted too readily, decided it had not because three controls were real, and
never went back to the text to check that Śambara's forts really are counted
five ways. That is the characteristic weakness of an adversarial test run by the
author, and `BF-014` records it with the control that now stands against it: a
claim of the form *value X attaches to entity Y* must cite the syntax that
attaches them, never stanza co-occurrence — in a unit that has itself proved
co-occurrence invalid.

**Control 1 is withdrawn.** It read "the predictions were fixed before the
evidence was read". That is unauditable: the four predictions first enter the
repository in the same commit that creates
`03-REGISTERS/rigveda-pur-counts.csv`, and nothing predating the counts records
them. It is not disproven; it cannot be checked, and a control that cannot be
checked is not a control. It is not counted.

**The three that stand, and are checkable:**

1. **One prediction failed for the formula reading and is recorded as such**:
   the numbers sort by narrative cycle — seven with Purukutsa and the Pūru in
   all four passages, near-verbatim at 1.174.2b and 6.20.10c; 99 and 100 with
   Divodāsa and Śambara. That failure is in the interpretation row's
   `evidence_against` column, not a footnote, and it narrows the conclusion from
   "the numbers are meaningless" to "a formula system with slots filled by
   cycle".
2. **The typology was kept separate from the counts, and it contradicts the
   easy version.** All six 99-passages are textual strongholds (§6.4). "The
   number is a formula" and "the passage is a formula" are different claims and
   this unit keeps them apart. Had the two been one register, the deflationary
   reading would have propagated from the count to the passage for free.
3. **`PUR4J-I-01` states what it does not establish**, in its own column: a
   formulaic count says nothing about whether anything was besieged, and the
   typology is assigned per passage and never inherited from that row.
4. **`PUR4J-I-03` refuses the inverse error explicitly**: 49 of 103 passages
   present a fort as an object, and this unit has no evidence bearing on
   whether any of them stood anywhere. The plurality finding is about the
   *form* of the answer, not its content.

**And the opposite bias was checked.** Demoting 99 because it arrives in a page
headline rather than a commit hash is the error the reconciliation brief warned
against. 99 is now a `VERIFIED` count of six passages with locators, and it
outranks the register's 106 on the question of how many forts a passage names
(`PUR4J-I-02`). What is demoted is only its claim to be *the* number, and that
demotion is a measurement: 9 passages to 6.

**One error ran the other way**, which is evidence the resistance was not
wholly for show: rule R5's case test over-assigned `TEXTUAL-STRONGHOLD` by
about eleven passages (§6.3), against the deflationary reading, and it was
found and corrected before the reviewer reached it.

### 8.3 Method failures logged

Three rows in `04-AUDITS/BIAS-FAILURE-LOG.csv` — `BF-012`, `BF-013` and
`BF-014` — and four in `04-AUDITS/REAUDIT-QUEUE.csv` (`RA-012` to `RA-015`).

`BF-012` and `BF-013` are failure modes caught in flight. **`BF-014` is not**:
it is a failure that reached a `VERIFIED` register row, propagated into an
interpretation, and was caught only by an independent reviewer. It is logged as
what it is.
