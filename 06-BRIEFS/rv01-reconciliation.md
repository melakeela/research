# RV-01 "The 99 Forts Database" against the púr- family register

**Written:** 2026-09-07
**Unit type:** reconciliation brief. Report only.
**Subjects:**
`00-CONTROLLER/METHODOLOGY-CONSTITUTION.md` §4J "The Rigvedic forts" (lines 373–404);
`01-INHERITED/site-review/MELAKEELASITEREVIEWRUNNINGLIST.md` (Version 12) line 1219,
with lines 1114, 1164, 1169, 1175, 1240, 1259, 1272;
`03-REGISTERS/rigveda-pur-family.csv` (28 claims) and
`03-REGISTERS/rigveda-pur-family-occurrences.csv` (106 rows);
`04-AUDITS/rigveda-pur-family-method.md`;
`01-INHERITED/curatorial-audit-v1.1/page-audit.csv` and `claim-risk.csv`, row `the-forts`.

**Status of this document.** Derived analysis. It establishes the relationship
between two specifications and one register. It promotes nothing, demotes
nothing, and writes no register row. Where it makes a claim of its own, the
claim carries a status inline.

**What this unit did not do.** No corpus was re-run, no source retrieved, no row
added to any register, ledger or decision file, and none of the missing fields
begun. §6 says what the missing work would require; it is not that work.

---

## 1. There are two specifications, and they are not equal

RV-01 is not the governing requirement. The constitution has its own forts
section, written by the owner and committed unchanged.

### 1.1 The governing specification — Constitution §4J

> **J. The Rigvedic forts**
>
> Build the complete corpus rather than using one famous number.
>
> Enumerate:
>
> * 90;
> * 99;
> * 100;
> * other counts;
> * patron;
> * poet lineage;
> * opponent;
> * description;
> * material;
> * water;
> * cattle;
> * treasure;
> * mountain or river;
> * proposed geography;
> * chronological stratum.
>
> Do not automatically translate *pur* into a Mature Harappan city.
>
> Distinguish:
>
> * textual stronghold;
> * poetic formula;
> * inferred geography;
> * archaeological fortification;
> * unsupported identification.

Fifteen enumerated items, one translation prohibition, one five-way typology.
`CONTROLLER-RECONCILIATION.md` records no conflict touching §J, so it stands
unmodified. Per `CLAUDE.md`, §4A–V is "a research agenda, not a body of
findings" — §J is therefore authoritative as a **requirement** and carries no
evidentiary standing of its own.

### 1.2 The derived specification — RV-01, Version 12 line 1219

> | RV-01 | The 99 Forts Database | Every relevant *pur* passage with varying counts, patron, enemy, poet, descriptors, wealth/water context, stratum and geography confidence. | R10 |

Nine fields. RV-01 is a **compression of §J**: every RV-01 field maps onto a §J
item, three §J groups are merged into one field each, three §J requirements are
dropped, and two items are reordered (§J runs *poet lineage · opponent* and ends
on stratum; RV-01 runs *enemy · poet* and ends on geography). It was produced by
a model summarizing prior threads, so it enters at `INHERITED-UNVERIFIED` in
every part, **including its title**, and nothing here promotes it.

**Where the two disagree, §J governs.** RV-01 is inherited; §J is the owner's.

### 1.3 What else in Version 12 binds this work

| Line | Text | Effect |
|---|---|---|
| 1114 | `/dasa-forts-rigveda` — "Update/recheck counts, strata, date claims and candidate framing; **not a new page by default**." | A correction to an existing page, not a greenfield build. |
| 1164 | "The existing ninety-nine-forts page **must be audited before any new forts feature is proposed**." | An audit gate stands in front of RV-01. Not run. |
| 1175 | Research hold: "identification of the ninety-nine forts with one archaeological culture." | Bounds the geography field. |
| 1240 | Q12: "What do the **varying 90/99/100 fort counts** imply about formula, history and scale?" | Version 12 also treats the count as variable and unsettled. |
| 1259 | "Do not force every *pur* to mean an urban city, one material or one historical event." | Version 12's weaker echo of §J's translation prohibition. |
| 1272 | Feature 6 — "full corpus table linked to actual archaeological fortifications **without forced matches**." | The archaeological link is RV-02's, not RV-01's. |

---

## 2. The count: 99 against 106

This is the load-bearing question, because the answer decides whether the
register is a partial build of the forts corpus or a different artefact sharing
its subject.

### 2.1 The governing document has already ruled on it

§J's first line is:

> **Build the complete corpus rather than using one famous number.**

and its enumeration then lists **90; 99; 100; other counts** as four of the
fifteen things to record. The constitution therefore treats 99 as **a value to
be collected**, expressly not as the size of the collection, and directs the
work away from titling the artefact with it. Version 12 Q12 says the same
independently: 90/99/100 are "varying fort counts".

This is not a reconciliation this brief supplies. It is one the owner already
wrote, and RV-01 reinstates the famous number that §J directs the work away
from.

### 2.2 What each number is presented as counting

| | "99" | "106" |
|---|---|---|
| Where it appears | RV-01's title; `the-forts` headline "Ninety-nine forts, in Indus country, three centuries too late"; Version 12 lines 1114, 1164, 1175, 1272; §J as an enumerated value | `PUR-005`; method note §3; the 106 rows of the occurrences register |
| Counts | forts — objects placed in a geography and a period | tokens — instances of seven lemmas in a text |
| Unit | one fort | one word-token |
| Population | forts ascribed to an enemy in Rigvedic narrative | the 164,758-token Zürich layer (`PUR-001`) |
| Denominator | none stated anywhere in this repository | the corpus, per `PUR-016` |
| Status here | `INHERITED-UNVERIFIED` | `VERIFIED` (`PUR-003`, `PUR-004`, `PUR-005`) |
| Retrieval behind it | none on record | `SRC-019`/`SRC-022`, commit `d3eb8af`, 2026-09-07 |

### 2.3 Test 1 — is there a transform between them?

Two figures are the same quantity measured differently only if a stated rule
converts one into the other. There is none, and the failure is structural
rather than a missing formula:

- **Token → fort.** One token can carry any number of forts. `púraḥ` is
  accusative plural in 45 of the 83 simplex tokens (`PUR-003`); one such token
  in a passage naming a hundred forts denotes a hundred forts, not one.
- **Fort → token.** 106 tokens spread over 86 hymns (`PUR-005`). The same forts
  are named repeatedly across hymns, so a token count cannot enumerate distinct
  forts even in principle. It counts mentions, not things mentioned.

### 2.4 Test 2 — can any defensible sub-count of the register return 99?

If 99 were 106 measured differently, some stated sub-selection should yield it.
Every sub-count the register supports, recomputed from the occurrences file for
this brief and agreeing with the claim rows:

| Sub-count | Value | Source |
|---|---:|---|
| Family tokens | **106** | `PUR-005`, recount agrees |
| Family pādas | 104 | `PUR-005`, recount agrees |
| Family stanzas | 103 | `PUR-005`, recount agrees |
| Family hymns | 86 | `PUR-005`, recount agrees |
| Simplex `púr-` tokens | 83 | `PUR-003`, recount agrees |
| Simplex `púr-` stanzas | 82 | recount |
| Simplex `púr-` hymns | 70 | recount |
| Family tokens excluding book 9 | 102 | recount |
| Family tokens admitting `púraṃdhi-` | 156 | `PUR-023` |
| Family tokens admitting `purāṣáh-` | 107 | `PUR-024` |
| String-search hits that are the fort word | 78 | `PUR-007` |
| Bare `puraḥ`/`purā` resolved as `púr-` in the padapāṭha | 48 | `PUR-009` |

**None is 99.** The nearest are 103 and 104, and reaching 99 from either needs
four or five rows deleted on a rule nobody has stated. The hypothesis that 99 is
the register's quantity under another unit is unsupported from the register side.

### 2.5 Test 3 — what does the repository use "99" to count?

A `git grep` over every tracked file for *ninety* and for standalone *99* returns
matches in six text files and one binary. They fall into three groups, and no
group is a corpus operation:

1. **The figure used as a quantity of forts** — the `the-forts` headline
   ("Ninety-nine forts, **in Indus country, three centuries too late**"), §J's
   enumeration, Q12, RV-01's title, and Version 12 lines 1114, 1164, 1169, 1175,
   1272. A token count cannot be in Indus country or late for anything; the
   referent throughout is objects in a landscape.
2. **The gloss "ninety" for the lemma `navatí-`** — `PUR-022` and method §7.
   This is the numeral *as a word in the text*, which is the evidence that the
   counts are stated inside the passages, and it is counted in tokens (9), not
   in forts.
3. **Coincidental matches** — two sha256 substrings in the access ledger and the
   VedaWeb manifest, and the binary
   `01-INHERITED/curatorial-audit-v1.1/melakeela-curatorial-audit-v1.1.xlsx`,
   the workbook the audit CSVs were extracted from.

Group 1 counts forts and group 2 counts words, and the two never meet: nowhere
does a text produce 99 by counting anything in the corpus. RV-01's own body also
makes **counts a per-row field**, and a field whose value varies row by row
cannot also be the number of rows.

There is register evidence that numerals sit with the fort word: `PUR-022` and
method §7 record `navatí-` "ninety" at 9 tokens inside family stanzas, 33.5× its
corpus rate, and `śatá-` "hundred" at 10.7×. That is `VERIFIED`, and consistent
with counts being stated inside the passages. It is not proof of it —
stanza-level co-occurrence is not syntactic attachment, and the register
declines to read the profile (method §7: "a measurement of the profile and
nothing more").

### 2.6 Finding

**They are two different objects, not one quantity measured two ways — and
neither is the corpus §J specifies.**

- `VERIFIED` — 106 counts word-tokens of seven `púr-`-derived lemmas in a pinned
  corpus, with a denominator, a retrieval event and a reproducible method. It is
  not a count of forts and the register never claims it is.
- `VERIFIED` — no sub-count the register supports equals 99 (§2.4).
- `VERIFIED` — nothing in this repository derives 99 from any corpus operation.
  Typed under the negative-evidence standard as **ABSENT DESPITE ADEQUATE
  SEARCH**: the search was a full-text scan of every tracked file, and this
  repository is small enough for that scan to be exhaustive.
- `VERIFIED` — the constitution enumerates 99 as one of at least four count
  values and instructs that the corpus be built "rather than using one famous
  number" (§2.1).
- `PROVISIONAL` — 99 is a quantity of forts named inside Rigvedic passages,
  carried into MelaKeela through the `the-forts` page. Provisional because the
  register holds no numeral field, no passage text and no translation: the
  attachment of `navatí-` to `púr-` in any particular passage is inferred from a
  co-occurrence statistic, not read.

**Not established, and not to be written as though it were:**

1. Which passages state 99, and in what form. The construction usually cited is
   a compound of "ninety" and "nine" rather than a single numeral, so even "99 is
   attested" is a claim about a reading. Untested here.
2. Whether 99 is the modal count, the maximal count, or merely the most quotable.
   §J names 90 and 100 beside it and adds "other counts".
3. Whether the count is formulaic, historical, or both. §J puts *poetic formula*
   and *textual stronghold* in its five-way typology precisely because this is
   open. Nothing in the register bears on it.
4. Where MelaKeela's 99 came from. No source is recorded for the `the-forts`
   headline; the curatorial audit rates it `Medium` risk, "thin or undetected
   bibliography", "Revise before release".

### 2.7 The consequence

RV-01 names a database by a value in one of its own columns, not the size of its
table. Whatever row unit is chosen — token, pāda, stanza, hymn, passage — the
table will not have 99 rows, because none of the candidates is 99 (§2.4). A
reader meeting a table called "The 99 Forts Database" will read the title as a
row count.

This needs an owner ruling, and it is prior to the build rather than cosmetic,
because it decides scope (§5, C-4). **No `D-` identifier is allocated here**:
this is a report-only unit, and allocating from `09-DECISIONS/OWNER-DECISIONS.csv`
(highest present `D-034`) in a unit that is not itself raising the decision
risks colliding with concurrent work.

---

## 3. What the register actually is

`03-REGISTERS/rigveda-pur-family.csv` — 28 claim rows: 25 `VERIFIED`, 1
`PROVISIONAL` (`PUR-026`), 2 `HYPOTHESIS` (`PUR-027`, `PUR-028`).

`03-REGISTERS/rigveda-pur-family-occurrences.csv` — 106 rows:

```
occ_id, stanza, pada, token_index, surface, lemma, morphology,
arnold_metre_label, arnold_stratum_code, arnold_stratum,
stratum_certainty, source_id, retrieval_date
```

It is a **morphological concordance with a metrical stratum attached**. Every
column is an address in the corpus, a property of the word-form, or a property
of the pāda's metre. No column describes the world the passage describes. That
is the shape of the gap in §4: a difference of kind, not of completeness.

Two wrinkles for anyone joining against it:

- The `lemma` column has **eight** distinct values against the register's seven
  lemmas: `pūrbhíd-` (7) and `pūrbhíttama-` (1) are separate strings sharing one
  Grassmann id, which `PUR-004` counts together as 8. Join on the Grassmann id,
  not the lemma string.
- 14 of 106 rows carry `stratum_certainty = metrical-variations-only`, Arnold's
  lower-confidence assignment (`PUR-011`). A stratum column shown without that
  flag overstates the evidence.

---

## 4. Field by field

Against §J's fifteen enumerated items, with RV-01's nine mapped onto them.

| §J item | RV-01 field | Register provides | Assessment |
|---|---|---|---|
| *(row unit — "the complete corpus")* | F1 every relevant *pur* passage | stanza / pāda / token index, surface, lemma, morphology, for 106 tokens | **PARTIAL — index only.** An address list, not passages: no Saṃhitā text, no padapāṭha line, no translation, no passage boundary. Row unit is the token, not the passage (C-1); "relevant" is defined etymologically, which is neither spec's criterion (C-2). |
| 90 · 99 · 100 · other counts | F2 varying counts | nothing per row. Aggregate only: `navatí-` 9 tokens at 33.5×, `śatá-` at 10.7× (`PUR-022`) | **ABSENT.** A corpus statistic over stanzas, not a numeral attached to a fort in a passage. Evidence that the field is fillable, not the field. |
| patron | F3 patron | nothing per row. `PUR-022` lists `dívodāsa-` 8 and `r̥jíśvan-` 5 among high-lift co-occurrences | **ABSENT.** The collocation list ranks by lift and does not distinguish patron from enemy. Reading it as a patron column imports the interpretation the register refused to make. |
| opponent | F4 enemy | nothing per row. `PUR-022`: `śámbara-` 9, `pípru-` 6, `śúṣṇa-` 6, `dā́sī-` 4 | **ABSENT**, same reason. Stanza co-occurrence is not a claim about who held a fort; that reading is logged unbuilt as `PUR-027` at `HYPOTHESIS`. |
| poet lineage | F5 poet | nothing | **ABSENT, and no source in hand.** Needs the Anukramaṇī or an edition carrying attributions. No ledger row records one. The only field with no retrieved source behind it at all. Note RV-01 narrows §J's *lineage* to *poet*: a family attribution and a named individual are different objects. |
| description | F6 descriptors | nothing per row. `PUR-022`: `āyasá-` "of metal" 8 tokens at 36.9× | **ABSENT.** Sharing a stanza does not establish that `āyasá-` modifies the fort word. Agreement is checkable from retrieved data; it was not checked. The link is an untested bridge. |
| material | *(absent from RV-01)* | as above | **ABSENT, and dropped from the derived spec.** §J separates material from description; RV-01 merges them away. This is the field the translation prohibition turns on — see C-7. |
| water · cattle · treasure | F7 wealth/water context | nothing | **ABSENT.** Three §J fields compressed into one RV-01 field, none populated. Needs a defined semantic field before it can be filled at all. |
| mountain or river · proposed geography | F9 geography confidence | nothing | **ABSENT.** The register holds no geographic content of any kind. `info/rv_locations.tsv` is in the pinned clone (`SRC-019` manifest) but is cited by neither the register nor the method note, and was not inspected here; whether it bears on this field is unknown. Bounded by the research hold at line 1175 and overlapping RV-02. |
| chronological stratum | F8 stratum | `arnold_metre_label`, `arnold_stratum_code`, `arnold_stratum`, `stratum_certainty` per token; plus the corpus baseline (`PUR-016`), χ² at token and hymn level (`PUR-018`), the by-book second instrument (`PUR-019`, `PUR-020`), and the entanglement between them (`PUR-021`, `DEP-004`) | **PRESENT, beyond what either spec asks.** Both ask for a column; the register supplies the column, its denominator, a significance test at a conservative unit, an independent second instrument returning a null, and the dependency that stops the two being read as agreement. Caveats that travel with it: single-sourced (`DEP-001`), capped at `PROVISIONAL` where read chronologically (`PUR-026`), resting on `PUR-028` at `HYPOTHESIS`. |
| *five-way typology* | *(absent from RV-01)* | nothing | **ABSENT.** §J requires textual stronghold / poetic formula / inferred geography / archaeological fortification / unsupported identification to be distinguished. No column carries it. |

**Coverage against §J: of the fifteen enumerated items, 1 is delivered
(chronological stratum) and 14 are absent. §J's two further requirements — the
complete-corpus row basis and the five-way typology — are partial and absent
respectively.**
**Coverage against RV-01: 1 field of 9 delivered, 1 partial, 7 absent.**

The register is one column of the specified corpus plus an address list, done to
a standard neither spec asks for.

---

## 5. Where the specifications and the register conflict

Seven conflicts and one boundary note. None is resolved here.

**C-1 — Row unit.** Both specs make the row a *passage*; the register's row is a
*token*. Candidates are 106 tokens / 104 pādas / 103 stanzas / 86 hymns, and
neither spec says which. A naive one-row-per-token build double-counts RV 1.53.7b
(`purā́ púram`) and RV 6.32.3c (`púraḥ purohā́`), where two family tokens share a
pāda (`PUR-005`). The unit must be fixed first, because most fields are
properties of a passage while the stratum is a property of a pāda: whichever
unit is chosen, one group of fields is aggregated or repeated.

**C-2 — What "relevant" means.** The register's membership test is etymological:
derivation from `púr-`, fixed by a Grassmann gloss scan over every lemma in the
corpus (`PUR-006`). RV-01 says "relevant *pur* passage" and §J says "the complete
corpus" — neither defines it. The readings diverge:

- On a *semantic* reading (passages about forts), `PUR-006`'s six fort-adjacent
  non-`púr-` lemmas — `paridhí-`, `dehī́-`, `saṃdíh-`, `harmyá-`, `ádhr̥ṣṭa-`,
  `dārú-` — belong in the corpus and are excluded from the register **by design**.
- On the *etymological* reading, `púraṃdhi-` and its two compounds (50 tokens)
  stay out, but that exclusion is a live judgement on `HOLD-001`, not a settled
  fact; `purāṣáh-` (1 token) is out on Grassmann's gloss alone.
- On either reading, a `púr-` token in a passage that is not about a fort sits in
  the register and may not belong in the corpus.

The register's boundary is defensible and documented. It is simply not the same
boundary, and on the semantic reading the population changes class.

**C-3 — The count.** §2. Two different objects; the register's 106 does not
answer RV-01's title and RV-01's title does not describe the register.

**C-4 — RV-01 contradicts itself, and §J.** Its title fixes one number; its body
requires "varying counts"; §J enumerates 90/99/100/other and says not to build
from one famous number. The specification cannot be satisfied as written. Two
readings survive, producing different databases:

1. *A database titled "The 99 Forts"* — scope is every relevant *pur* passage,
   99 is a legacy label from the page, and the title misdescribes its contents.
2. *A database of the 99 forts* — scope is only passages stating a fort count,
   and the table is much smaller than the register.

Reading 2 makes the register a **superset** of the artefact; reading 1 makes it a
**partial column** of it. §J's opening line points hard at reading 1, but the
title is the owner's to keep or drop. This is the ruling flagged in §2.7.

**C-5 — Evidentiary standing runs the wrong way.** The register is `VERIFIED`
with a pinned commit and a retrieval date. RV-01's title, and the `the-forts`
headline behind it, are `INHERITED-UNVERIFIED` with no recorded source. Building
from the register would put an unverified figure in the title of a verified
table, promoting it by adjacency — what the inheritance rule forbids, since only
retrieval promotes.

**C-6 — Three names for one target.** The register's `supports_page` reads
`forts (proposed)`; the curatorial audit's slug is `the-forts`; Version 12's
route is `/dasa-forts-rigveda`; RV-01 says "The 99 Forts Database"; feature 6
says "The 99 Forts". Whether these are one page or several is established
nowhere. The same drift appears in the register's other `supports_page` value,
`the-killed.html`, against the audit slug `the-killed`. This is a step-13
terminology-drift finding, and it breaks any join the moment `supports_page` is
used to assemble anything.

**C-7 — RV-01 loses §J's epistemic controls.** The compression is not neutral.
RV-01 drops *material*, collapses *mountain or river* and *proposed geography*
into a single "geography confidence" scalar, narrows *poet lineage* to *poet*,
merges *water · cattle · treasure* into one field, and omits the five-way
typology and the prohibition on translating *pur* into a Mature Harappan city
(Version 12 keeps a weaker echo at line 1259). The losses cluster exactly where
§J placed its controls: the typology is the instrument that keeps a textual
stronghold from becoming an archaeological one, and *material* is what a
"Mature Harappan city" claim would have to be argued from. **Building RV-01 as
written produces a weaker artefact than the constitution requires.** Where the
two disagree, §J governs.

**Boundary note, not a conflict.** RV-01 specifies a "Database" — a site-facing
artefact. Per reconciliation C-9 this repository produces registers and briefs,
never pages. The research content belongs here; the presentation does not.

**A false conflict, recorded so it is not re-raised.** The `the-forts` headline
says the forts are "three centuries too late" while `PUR-026` says the `púr-`
vocabulary is *not* a late accretion. These are not in contradiction: `PUR-026`
concerns position *within* the Rigveda on Arnold's periodisation; the headline
concerns the Rigveda's date *relative to* Indus urbanism. Both could hold.
Neither supports the other.

---

## 6. What is missing, typed by what it would take

| §J item | Blocker type | What it needs |
|---|---|---|
| passage text (row basis) | **Extraction, source in hand** | `SRC-020` (Aufrecht Saṃhitā) and `SRC-021` (padapāṭha) are pinned in the `SRC-019` clone at `d3eb8af`, one row per pāda. Joining them to the 106 addresses is mechanical. |
| 90 / 99 / 100 / other counts | **Extraction plus reading, source in hand** | Numeral lemmas are in the Zürich layer (`SRC-022`); extracting them per stanza is mechanical, but establishing that a numeral governs `púr-` rather than merely sharing a stanza requires reading the passage. `PUR-022` is the co-occurrence, not the attachment. |
| patron · opponent | **Reading, not retrieval** | Each passage read for who attacks and who holds. The register declined this deliberately (method §9: "No passage was read for the grammatical role of `púr-`"), and `PUR-027` exists so the collocation profile is not mistaken for the answer. |
| poet lineage | **Retrieval not yet attempted** | No ledger row records an Anukramaṇī or an edition carrying attributions. `SRC-025` (archive.org), `SRC-028` (GRETIL) and `SRC-033` (TITUS) are probed `retrieval_capable=YES` and are the candidates. Whether any carries the attributions is unknown; nothing here says it does. |
| description · material | **Extraction plus judgement, source in hand** | The morphology column supports an agreement test against `púr-`; what counts as a descriptor, and what as a material, needs defining first. §J's translation prohibition constrains the result. |
| water · cattle · treasure | **Definition first** | Not retrievable until the semantic fields are stated. Undefined, they become places to put what the reader already believes. |
| mountain or river · proposed geography | **Definition, then retrieval, then an owner ruling** | Needs a stated confidence scheme; overlaps RV-02; bounded by the research hold at line 1175. `info/rv_locations.tsv` should be inspected before anything else is planned. |
| chronological stratum | **Delivered** | Carry the `stratum_certainty` flag and the `DEP-001` / `PUR-028` caveats, or the column overstates. |
| five-way typology | **Judgement, after the rest** | Cannot be assigned before the passages are read and the geography field exists. It is the last column, not the first. |

**One operational note.** The clone behind every `VERIFIED` row in the register
is session-local and is **not** in this container. Re-running requires a fresh
clone at commit `d3eb8af`; `SRC-019` records that `codeload.github.com` and
`github.com` both returned 403 for it and that the anonymous read lane worked.
Expect to re-clone before anything else.

---

## 7. Adversarial tests on this brief

**Prestige-bias challenge.** The specific risk is preferring 106 because it
arrives with a commit hash, a χ² and German lexicography, and demoting 99 to
"just a formula" because it arrives in a page headline. Corrected at §2.6: the
register's 106 has **no** claim to be the number of forts, because it is not a
count of forts at all. The status asymmetry between the two figures is warranted
by retrieval, not prestige — 106 has a retrieval event and 99 has none. Had 99
come with a locator and a passage, it would outrank 106 on how many forts a
passage names, and 106 would still say nothing about it. A second form of the
same bias was caught in §4: the register's stratum column is excellent, and
excellence in one column is not coverage — it is one item of fifteen. No
`BIAS-FAILURE-LOG` row is warranted; both corrections were made inside this
brief rather than after it.

**Preferred-counter-narrative challenge.** The available soft landing is to
declare 99 formulaic and be done — a conclusion that flatters a deflationary
reading of Rigvedic conflict and costs nothing to assert. Refused at §2.6
item 3: nothing in the register bears on whether the count is formulaic,
historical or both, and §J lists *poetic formula* and *textual stronghold* as
two of five types to be distinguished, not one to be assumed. The opposite
temptation is also refused — the `the-forts` headline's "Indus country, three
centuries too late" is an unverified interpretive claim carrying a geography and
a chronology, rated `Medium` risk and "Revise before release" by the curatorial
audit; this brief neither repeats nor rebuts it.

---

## 8. What would change these findings

- **§2.6 would be overturned** by a document showing MelaKeela's 99 was derived
  from a corpus operation — an earlier count of 99 passages, hymns or
  occurrences — rather than from the text's own numerals. It would then be the
  same object counted badly, and the correct action would be a `SUPERSEDED` row
  against the old count, not a distinction between two objects.
- **§2.6 would be sharpened, not overturned,** by a numeral extraction showing
  which passages state which counts. That is the first piece of the missing work
  and the cheapest: the source is pinned and in hand.
- **C-4 is settled by the owner, not by evidence.** Which reading is intended
  decides whether the register is a superset or a partial column, and no amount
  of retrieval answers it.
- **C-2 would move** if `HOLD-001` resolves. Admitting `púraṃdhi-` raises the
  family from 106 to 156 (`PUR-023`), changing the population of any corpus built
  on the etymological reading while leaving the semantic reading untouched.
- **C-7 would be void** if the owner rules that RV-01 supersedes §J rather than
  compressing it. Nothing in `CONTROLLER-RECONCILIATION.md` currently supports
  that reading.

---

## 9. Note on placement

`06-BRIEFS/` is created by this unit and is not in the `CLAUDE.md` layout table,
which lists `06-BACKLOG/` at that number. Reconciliation C-9 establishes that
briefs are a product of this repository ("registers and briefs, not pages"), and
C-3 assigns homes to files as the work that fills them begins, so the directory
is consistent with the controller. It has no assigned home on record, and if the
owner prefers another the move is cheap now and expensive later.
