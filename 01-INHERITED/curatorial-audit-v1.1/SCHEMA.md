# Curatorial Audit v1.1 — What This Workbook Is

**Artefact:** `melakeela-curatorial-audit-v1.1.xlsx`, extracted to eight CSVs
in this directory.
**Baseline it describes:** `veli-site(3).zip`, supplied 2026-09-01, 96 HTML pages.
**Status of everything in it:** `INHERITED-UNVERIFIED`, without exception.

The workbook labels its own decisions "provisional" and its own scope "not a
completed peer review." That self-description does not promote it. Nor does the
fact that its numbers were produced by a script rather than by prose: no
retrieval event is logged in `02-SOURCES/access-ledger.csv` for the archive it
parsed, so its counts are claims about a file this repository has never opened.

---

## 1. What the workbook is as a system

It is a **triage instrument applied to a site build**, not to a body of
knowledge. Its unit of analysis is the *page*: every sheet is keyed, directly or
transitively, to one of 96 slugs. It answers "which of these 96 documents may be
published, in what order, needing what" — and it answers that question without
opening a single historical source.

That is worth stating precisely, because it is the workbook's defining boundary.
`Claim Risk` has a column called `Verification required` containing 38 identical
strings. Not 38 assessments — 38 copies of one instruction. The workbook
identifies *which* claims need verification and *stops there*. It never performs
one. Its "Risk" is a scheduling variable, and the sheet says so: "Risk means
verification priority, not falsehood."

### What it does that nothing else in this repository does

`03-REGISTERS/inherited-claims.csv` holds 369 claims extracted from
`01-INHERITED/claude-project-handoff.md`. Those claims are *about the project's
own conversation record* — what was decided, when, by whom, and where the records
disagree. Their locators point at line ranges in a markdown handoff.

This workbook is the only artefact here keyed to **published surface**. It is the
only place where a claim is tied to the page a reader would actually encounter
it on, the only place carrying a publish/withhold decision, and the only place
that treats visual assets, rights clearance, and inter-page duplication as
first-class objects. Nothing else in the repository knows that `before-the-indus`
is a page, let alone that it is 1,724 words with 17 unlinked bibliography
entries.

Conversely, the workbook has no concept of a source. `02-SOURCES/access-ledger.csv`
tracks 18 named sources with probe calls, auth states and blocking constraints.
The workbook counts bibliography *entries* — a quantity — and never names one.
The two artefacts do not intersect at any join key. There is no path today from
"this page cites 88 things" to "here is what one of those 88 things is."

### Vocabulary the workbook introduces

Six controlled vocabularies, none of which appears anywhere else in the repository:

| Vocabulary | Values | Scope |
|---|---|---|
| **Decision** | Keep · Revise · Hold · Split · Merge | 96 pages |
| **Risk** | Low · Medium · High · Critical | 96 pages |
| **Environment** | 7 named environments (§3) | 96 pages |
| **Type** | 29 values, from `atlas` to `semantic-field` | 96 pages |
| **Source state** | 5 values, `no detected source section` → `visible bibliography plus live links` | 96 pages |
| **Risk type** | 5 detectable language patterns (§6) | 38 pages |

**Decision does not map onto the repository's evidence-status vocabulary, and must
not be treated as doing so.** `Hold` is the near-miss: the workbook's `Hold` means
"withhold from launch pending review," while `CLAUDE.md`'s `HOLD` means "blocked
on source access, record in `05-HOLDS/`." A page can be workbook-`Keep` and every
claim on it `INHERITED-UNVERIFIED`; 46 pages currently are. The Summary sheet says
this itself, in the only sentence in the workbook that is doing load-bearing
epistemic work: *"None of these labels certifies historical truth."*

### The sheet graph

```
                       Page Audit  (96 rows — the spine; every other sheet joins here on Slug)
                            |
   ┌────────────┬───────────┼──────────────┬─────────────────┐
   │            │           │              │                 │
Summary     Claim Risk   MVP           Asset Register   Overlap & Tensions
(rollup,    (38 rows,    (15 rows,     (96 rows, 1:1)   (9 clusters + 23 pairs;
 no join)    Risk≥Med)    MVP=Yes)                       joins on sets of slugs)
                            |
                    Environment Map (7 rows — the vocabulary Page Audit and
                    Asset Register both draw their Environment values from)

Method & Limits — no join. Declares the procedure and the boundary.
```

**Derivation, tested against the extracted data.** Several columns that look like
independent judgement are recomputations of Page Audit:

- `Claim Risk.Publication gate` = `Page Audit.Decision`, mechanically:
  Hold→"Hold" (15/15), everything else→"Revise before release" (23/23).
- `Claim Risk.Risk` matches `Page Audit.Risk` on all 38 rows.
- `Asset Register.Priority` = MVP→`MVP`; else Risk∈{Critical,High}→`High`;
  else `Later`. Holds for all 96 rows with no exceptions.
- `Asset Register.Environment` = `Page Audit.Primary environment` on all 96 rows.
- `Page Audit.Decision = Merge` (4 pages) = exactly the four pages named as merge
  targets in the Overlap clusters: `criminalised-today`, `the-computed-dawn`,
  `the-insertions`, `the-nine-enemies`.

The workbook is therefore **more tightly coupled than its eight tabs suggest**.
Read as an independent cross-check it will confirm itself. The genuinely
independent content sits in four columns only: `Written assessment`,
`Central claim`, `Required asset set`, and the Overlap `Recommendation` column.

---

## 2. Sheet-by-sheet

### Page Audit — 96 rows × 15 columns

The spine. One row per page: `Slug`, `Title`, `H1 / central finding`, `Words`,
`Type`, `Primary environment`, `Secondary environment`, `Written assessment`,
`Source entries (est.)`, `External links`, `Decision`, `Risk`, `Required action`,
`MVP`, `Inbound links`.

Corpus shape: 157,721 words total; median page 1,375 words; range 8 to 6,069.
960 estimated bibliography entries; median 8 per page; **14 pages have zero**.
`artifact-atlas` carries 88 entries against 8 words of prose.

**78 of 96 pages have zero external links.** Nine have any live-linked
bibliography at all. The dominant source state — 41 pages — is "substantial
bibliography, mostly non-linked." Whatever else the audit found, this is the
single largest structural fact about the corpus: it cites heavily and links
almost never, so essentially none of its sourcing is checkable by a reader
without manual re-derivation.

Two columns do no work. `Secondary environment` is `Reading Room` on all 96
rows — a constant, not a variable (§3). `Required action` holds five boilerplate
strings keyed 1:1 to `Decision`, so it restates the decision rather than
specifying anything page-specific.

### Summary — 14 rows

Rollup and release gates. 96 pages → Keep 46, Revise 20, Hold 15, Split 11,
Merge 4; 15 MVP candidates. Counts reconcile exactly against Page Audit.

Carries seven numbered release gates: claim-level citation review; cross-page
consistency; image rights and provenance; specialist/community review; browser,
accessibility and mobile testing; prototype approval; production domain and
deployment allowlist. Gates 1 and 2 are what this repository exists to do. Gates
3–7 are outside it entirely and have no home in the current structure.

### Claim Risk — 38 rows × 8 columns

One row per page with `Risk ≥ Medium`. Extracts the page's `Central claim` as a
quotable string and assigns `Risk type(s)`, `Source state`, `Verification
required`, `Publication gate`, `Owner/status`.

Two columns are constants: `Verification required` (38 identical strings) and
`Owner/status` (`Unassigned`, 38/38). **Nothing in the workbook is assigned to
anyone.**

Two coverage facts:

- All 21 Critical/High pages are present. **Six of the 23 Medium-risk pages are
  not**: `custody`, `jatization`, `the-computed-dawn`, `the-gap`,
  `the-words-of-caste`, `who-named-india`. `custody` is MVP rank 14. Its central
  claim was never extracted.
- **Nine of the 15 Critical rows carry a blank `Risk type(s)`** — and every blank
  in the sheet is a Critical row. `academia-battlefield`, `before-the-indus`,
  `origin-myths`, `the-borrowed-ancestor`, `the-king-they-claimed`,
  `the-medicine-question`, `the-narrowing`, `they-already-knew`,
  `why-the-ranked-defend-the-ranking`. Their Critical rating rests on the
  assessor's prose judgement of subject sensitivity, not on any recorded signal.
  That is a defensible judgement to make, but it is not the same instrument as
  the pattern-detector that produced the other rows, and the sheet does not mark
  the difference.

### MVP — 15 rows

The launch set, ranked. Analysed in §5.

### Environment Map — 7 rows

The design vocabulary. Analysed in §3.

### Asset Register — 96 rows × 7 columns

Production requirements. Analysed in §4.

### Overlap & Tensions — two stacked tables

9 thematic clusters, then 23 high-similarity page pairs. Analysed in §6.
(The 40 CSV rows are 3 header/title rows, 9 clusters, 2 spacers, 2 sub-header
rows, and 23 pairs. **There are not 40 clusters.**)

### Method & Limits — 7 procedure rows

The most useful sheet in the workbook, and the one that constrains how the rest
may be read. Seven layers, each with a stated limit:

| Layer | Limit as stated |
|---|---|
| Baseline | Frozen archive; all counts derive from it |
| Structural audit | "Script-heavy content may be undercounted as visible prose" |
| Source visibility | "A visible bibliography does not prove claim-level support or source quality" |
| Claim risk | "Risk means verification priority, not falsehood" |
| Duplication | "Shared vocabulary can inflate similarity; each proposed merge needs human review" |
| Curatorial decision | "Decisions remain provisional until factual and specialist review" |
| Not completed | Primary-source re-performance, legal opinion, community consultation, image-rights clearance, discipline-specific peer review — "publication gates, not optional polish" |

---

## 3. Environment Map — the curatorial thesis

Seven environments, each with a `Function`, prototype pages, a `Palette role`, a
`Desired effect` and — unusually — an `Avoid`.

| Environment | Function | Avoid |
|---|---|---|
| Nocturnal Veḷi | Threshold, deep time, unknowns | No fantasy portal or occult styling |
| Living Signal Field | Relationships, movement, comparison | No gaming HUD or arbitrary links |
| Tamil Retrofuture | Counter-history, public energy, learning | No kitsch, fake Tamil or neon overload |
| Living Tiṇai | Ecology, place, material practice | No generic landscape decoration |
| Reading Room | Long argument, sources, methods | No visual fatigue or luxury minimalism |
| Extraction / Collection | Custody, access, classification, loss | No spectacle or unsupported allegation |
| Reconnection | Return, renewed access, living practice | Digitization is not restitution |

### The thesis

Stated in the sheet's second line: *"Themes change with the visitor's
relationship to knowledge; the institutional shell remains stable."*

The claim is that the organising principle of the institution is **epistemic
posture, not subject matter**. The environments are not Prehistory / Language /
Caste / Religion. They are: *not yet known* (Nocturnal Veḷi), *known by
relation* (Living Signal Field), *known against an official account* (Tamil
Retrofuture), *known through place and material* (Living Tiṇai), *known by
argument from sources* (Reading Room), *known but withheld* (Extraction /
Collection), *knowable again* (Reconnection).

The `Avoid` column is the strongest part of the artefact and the part with no
counterpart anywhere else in this repository. Each entry names the specific
failure mode that the environment's own aesthetic invites — deep time invites
occultism, relational display invites the gaming HUD, counter-history invites
kitsch, custody invites unsupported allegation. These are **falsifiable design
constraints**: for any published page you can state whether it violated one. The
last, "Digitization is not restitution," is not a design note at all. It is a
substantive ethical position that forecloses a claim the project could otherwise
have been tempted to make.

The thesis also carries a load-bearing consequence: because environments are
postures rather than topics, a page can move between them without its content
changing. Assignment is an editorial act, and it is revisable.

### Are the other sheets consistent with it?

**Consistent:**
- All 13 prototype assignments in the map match `Page Audit.Primary environment`
  exactly. No drift between the vocabulary and its use.
- `Asset Register.Environment` matches Page Audit on all 96 rows.
- The `Avoid` constraints reappear as concrete decisions. `academia-battlefield`
  (Extraction / Collection, "no unsupported allegation") is Hold/Critical with
  "right-of-reply discipline" named in its assessment. The Overlap cluster on
  institutional authority requires a "right-of-reply field." The constraint is
  enforced, not decorative.

**Inconsistent, in three ways:**

1. **Reading Room is both a peer environment and the universal substrate.** It is
   the primary environment for 34 of 96 pages — more than twice the next — *and*
   the secondary environment for all 96, including the 34 where it is already
   primary. A value that is constant across every row carries no information. If
   the intended claim is that long-form argument is the default state everything
   falls back to, that is a hierarchy, not a seventh peer; the map presents seven
   coequal rows. As encoded, the thesis "the institutional shell remains stable"
   is true in a way it did not intend: 34 pages are Reading Room because the
   audit had nothing more specific to say about them, and the residual category
   is the largest one.

2. **Reconnection has one page, and the workbook proposes to remove it.** The map
   describes its prototype as "Future community-led work" — an admission it is
   unbuilt. But one page is assigned to it: `criminalised-today`, and its
   Decision is `Merge` (into `criminalised`, cluster 2). The workbook's own
   recommendation, if executed, empties the environment. The seventh posture —
   the only one describing repair — has no surface. This is the one place where
   the environment scheme makes a claim about the institution that the page
   inventory does not support.

3. **The `Type` vocabulary is not reconciled to the environment vocabulary.**
   29 `Type` values against 7 environments, with 32 of 96 pages typed
   `research-essay` and 17 types used exactly once. Type drives asset class (§4),
   so a taxonomy with 17 singleton values is doing production-planning work it is
   too sparse to do reliably.

---

## 4. Asset Register — the implied production pipeline

96 rows, 1:1 with pages. `Documentary standard`, `Source / commission route` and
`Status` are constants: every page requires *"Verified source, licence, credit,
alt text, claim supported, date/place, manipulation disclosure"*; every route is
`To research`; every status is `Needed`. **Nothing is sourced. Nothing is
commissioned. Nothing is in progress.** This sheet is a specification of a
pipeline that does not yet exist, not a tracker of one that does.

### Six asset classes

Class is determined by `Page Audit.Type`, not by environment — verified against
the data. The mapping is clean; there is no page whose type belongs to two
classes.

| Class | Pages | Items/page | Slots | Types feeding it |
|---|---:|---:|---:|---|
| **Generic essay set** — opening atmosphere asset; claim-specific diagram; source facsimile; social card | 50 | 4 | 200 | research-essay (32), deep-history (5), cosmology (3), methods (2), + 8 singletons |
| **Data/interactive** — verified dataset; accessible SVG/map; legend; mobile alternative; downloadable table | 14 | 5 | 70 | relational-analysis (6), network (3), comparative-visual (3), atlas, chronology |
| **Text/social-history** — primary-text facsimile; translation excerpt rights; editorial illustration or print ephemera | 13 | 3 | 39 | social-history (11), text, learning |
| **Custody/institutional** — collection record; accession/custody document; object image rights; institutional correspondence; access-status evidence | 7 | 5 | 35 | institutional-critique (5), collection-investigation (2) |
| **Language/script** — manuscript/inscription image; glyph diagram; language map; pronunciation audio where licensed | 6 | 4 | 24 | language (4), script, semantic-field |
| **Place/ecology** — site/landscape photography; material macro; ecological map; present-context image | 6 | 4 | 24 | place (2), ecology-or-material (2), practice, ecology |

**392 discrete asset slots across 96 pages.** By priority: MVP 15 pages / 62
slots; High 20 pages / 77 slots; Later 61 pages / 253 slots.

### What sourcing each class actually requires

These are different acquisition problems with different costs, lead times and
failure modes. The register treats all six as one undifferentiated "To research."

- **Generic essay set (200 slots, 51% of the total).** The "claim-specific
  diagram" is the expensive half: 50 diagrams, each of which must be *correct
  about a contested claim* — so each is downstream of the verification this
  repository does, not commissionable in parallel with it. "Opening atmosphere
  asset" and "social card" are design production, licensable or generated. "Source
  facsimile" needs a real manuscript or print image with a rights position, which
  is class 3's problem appearing inside class 1. **The largest class is also the
  least specified, and it is the class 32 `research-essay` pages fall into by
  default rather than by analysis.**
- **Data/interactive (70 slots, 14 pages).** Not commissioning at all — this is
  engineering plus data curation. Each page needs a dataset that is itself
  verified, an accessible SVG, a mobile alternative and a downloadable table.
  These four are one build repeated 14 times, so the correct unit is a component,
  not 70 assets. Includes `artifact-atlas`, whose "verified dataset" is the atlas
  site count that this repository already records as contradicted (§6).
- **Text/social-history (39 slots, 13 pages).** Rights-bound and slow. "Translation
  excerpt rights" means negotiating with rightsholders of modern translations —
  the one class with a genuine external dependency and an unbounded timeline. 13
  pages, all Tamil Retrofuture or adjacent, and `kural` is MVP rank 10.
- **Custody/institutional (35 slots, 7 pages).** The hardest class, and the one
  whose difficulty is definitional rather than logistical. "Institutional
  correspondence" and "access-status evidence" are FOI-style acquisition against
  institutions that the pages themselves criticise. Every one of these 7 pages is
  Critical or High risk. Two are MVP (`custody` rank 14, `the-archive` rank 15).
  Sourcing an accession record from a collection is also the moment the "no
  unsupported allegation" constraint becomes testable.
- **Language/script (24 slots, 6 pages).** "Pronunciation audio where licensed"
  is the only slot in the workbook implying a living-speaker recording. If a
  recording were newly made rather than licensed, it raises a consent question —
  which under `CLAUDE.md` is an owner-escalation item, not a production task.
  The hedge "where licensed" suggests the workbook noticed and deferred it.
- **Place/ecology (24 slots, 6 pages).** Requires original site photography, i.e.
  fieldwork or a photographer commission, at named sites. `keeladi` and
  `the-water-city` are MVP ranks 7 and 9. The only class needing physical
  presence somewhere.

### Pipeline implications

1. **The critical path is not asset production, it is rights.** Classes 3, 4 and
   5 are gated on third parties. Release gate 3 ("Image rights and provenance")
   applies to all 392 slots, and Method & Limits lists image-rights clearance
   under "Not completed."
2. **Class 1 is a residual, and it is half the pipeline.** A page lands there by
   being typed `research-essay`, and `research-essay` is what a page is called
   when the audit did not classify it further. The largest production commitment
   in the workbook rests on the weakest classification.
3. **Sequencing is inverted for the diagram work.** 50 claim-specific diagrams
   cannot be commissioned before the claims are verified, but the register
   schedules them by MVP priority, which is driven by *low* risk — i.e. by pages
   least likely to have been examined closely.
4. **No cost, no lead time, no owner.** Three constants and one derived priority
   column mean the register cannot be scheduled from as it stands.

---

## 5. MVP — the implied launch strategy

Fifteen pages, ranked, each with `Environment`, `Decision`, `Risk`, `Release
dependency`, `Status` (`Not started`, 15/15).

Stated intent: *"Fifteen pages that demonstrate the institution, atlas, evidence
standards and range without pretending all 96 are ready."*

### What the fifteen have in common

**They are a coverage sample, not a subject.** Six of seven environments are
represented (Nocturnal Veḷi 4, Tamil Retrofuture 3, Living Tiṇai 3, Living Signal
Field 2, Extraction / Collection 2, Reading Room 1). Thirteen distinct `Type`
values across fifteen pages — close to the maximum diversity available. Only
Reconnection is absent, because it has one page and that page is a Merge.

Note the inversion: **Reading Room is 35% of the corpus and 1/15 of the launch.**
The launch deliberately under-represents the site's dominant mode. What it is
demonstrating is *breadth of posture* — that the institution has seven ways of
knowing — rather than depth in any one.

**They are structurally central.** Median inbound links: 46 for MVP pages, 5 for
the rest — a ninefold gap, and the sharpest discriminator in the workbook. Eight
of the fifteen are navigational hubs (`enter` 113, `artifact-atlas` 56,
`sound-changes` 55, `kural` 55, `custody` 55, `the-archive` 51, `the-other-laws`
47, `veli` 46). The set is chosen so that a visitor arriving anywhere lands
inside it.

**They are not chosen for length or sourcing.** MVP median 1,181 words against
1,399 for non-MVP; median source entries 9 against 8. Neither separates the sets.
Selection is by *position and posture*, not by evidential strength.

**They are risk-tolerant by design.** Decisions: Keep 8, Revise 5, Split 1,
Hold 1. Risk: Low 8, Medium 6, Critical 1. Seven of fifteen require work before
release; the "Release dependency" column is not aspiration but a precondition on
nearly half the set.

**Nothing has started.** All 15 `Status = Not started`. All 15 asset sets
`Needed`. All owners `Unassigned`.

### The strategy this encodes

Launch **an institution, not an argument**. The fifteen are picked to let a
visitor perceive the shape of the whole — a threshold (`index`, `veli`), a foyer
(`enter`), a data spine (`artifact-atlas`), a stated evidence standard
(`the-ledger`), a self-critical register (`custody`, `the-archive`), and one or
two exhibits per posture. It is a floor plan, deliberately not a thesis.

The cost is accepted openly: the fifteen are not the fifteen best-sourced pages,
and the workbook does not claim they are. `the-ledger` at rank 6 is the hinge —
the page that states the evidence standard is inside the launch set, which is
what makes launching partially-verified material coherent rather than evasive.
Whether it holds depends entirely on whether `the-ledger` is itself honest, and
the audit rates it Keep/Low without extracting a central claim from it.

### One page contradicts the set it is in

**`before-the-indus` is MVP rank 8 and `MVP = Yes` in Page Audit, with
`Asset Register.Priority = MVP` — while its Decision is `Hold`, its Risk is
`Critical`, and its `Release dependency`, printed in the MVP sheet itself, reads:
"Withhold from MVP until load-bearing claims receive claim-level citations and
specialist/editorial review."**

The row instructs the reader not to do what the sheet it appears on does. This is
not a judgement call the workbook makes and defends; it is an unreconciled state
across four columns of three sheets. It should be resolved before the MVP set is
used for anything, and it is exactly the class of defect
`03-REGISTERS/inherited-claims.csv` catalogues as a Rule 15 violation.

Recorded in `DECISIONS-NEEDED.md`. Not resolved here.

---

## 6. Overlap & Tensions — and the 19 contradictions already on file

### What the sheet actually contains

Not 40 clusters. **Nine thematic clusters** (`Cluster`, `Pages`, `Consistency /
contradiction risk`, `Recommendation`, `Status`) followed by **23 high-similarity
page pairs** (`Page A`, `Page B`, `Text similarity`, `Review action`, `Status`).
All 32 rows are `Open`. The `Review action` column is one repeated string across
all 23 pairs.

The nine clusters, with the pages each names:

| # | Cluster | Pages | Recommendation |
|---|---|---|---|
| 1 | Named enemies and forts | the-killed, the-nine-enemies, the-names, the-forts | Merge nine-enemies into killed |
| 2 | Criminalisation | criminalised, criminalised-today | Merge into one exhibit with dated legal cards |
| 3 | Astronomical chronology | sky, dravidian-sky, kali-yuga, the-computed-dawn | Merge computed-dawn into kali-yuga |
| 4 | Caste vocabulary corpus | the-curve, the-later-count, the-words-of-caste, what-varna-meant, jatization, the-late-hymn | One claims ledger; split overview / lexical evidence / interpretation |
| 5 | Genetics | steppe, the-three-ancestries, the-genome-of-caste, endogamy-clock, gotra, academia-battlefield | Shared methods page; expert review required |
| 6 | Textual interpolation | the-edits, the-insertions, one-verse, the-late-hymn, the-womb-doctrine | Merge insertions into edits |
| 7 | Meluhha and Indus | meluhha, meluhha-trade, the-water-city, before-the-indus | Keep distinct; present as one exhibit sequence |
| 8 | Language relationship | sound-changes, two-classical-languages, elamite, the-deep-root, brahmi, one-script-many-kingdoms | Shared methods glossary; specialist linguistic review |
| 9 | Institutional authority | indology, coverage, who-writes-the-textbook, what-the-children-are-taught, the-archive, custody | Curated exhibit with right-of-reply field |

The clusters are the workbook's best independent work. Clusters 4, 5, 6 and 8
each identify a *specific conflation risk* rather than mere topical adjacency —
"do not treat ancestry components as peoples, languages or moral categories";
"separate sound correspondence, contact borrowing, substrate inference, genetic
relationship and script history." These are methodological constraints stated in
the vocabulary of the disciplines involved, and they are the only place in the
workbook where the analysis reaches past the page surface.

Similarity scores run 0.200–0.568, floored at 0.2. Only two pairs exceed 0.34,
and the Method sheet's caution applies with force: at 0.20–0.27, pages on caste
vocabulary will resemble each other because caste vocabulary is what they are
made of. Roughly two-thirds of the pairs are likely to be vocabulary artefacts
rather than duplication. The sheet says so; the sheet is right.

### Do these overlap the 19 contradictions in `03-REGISTERS/inherited-claims.csv`?

The 19 (`IH-250`–`IH-268`, tagged X-01 to X-19 in `notes`) are **not the same kind
of object**. They record disagreements *between the project's planning documents*
— VELI-00 through VELI-13, RERUN.md, WORKLIST, live pages, owner statements —
about counts, names, dates and decisions. The workbook's clusters record
consistency risks *between published pages* about historical substance. Different
corpora, different join keys, different failure modes.

Slug-level intersection is nearly empty. Matching all 96 workbook slugs against
the full text of each contradiction row yields hits on only five: X-01 (`enter`),
X-02 (`index`), X-05 (`the-curve`), X-09 and X-11 (`veli`), X-15 (`brahmi`,
`the-killed`, `the-names`). Fourteen of nineteen name no page in the workbook at all.

But the two artefacts do **collide at seven points**, and the collisions matter
more than the count suggests:

| | Contradiction on file | Workbook position | Nature of the collision |
|---|---|---|---|
| **A** | **X-01** — atlas site count disputed across 140 / 150 / 158 / 167→175 / 194 / 199 | `artifact-atlas`, titled *"175 Ancient South Asian Sites Mapped"*, MVP **rank 3**, **Keep**, **Low** risk, absent from Claim Risk | The workbook adopts one side of an open contradiction as settled fact, puts it in a page title, and rates the page low-risk. The number is in the launch set's third position. |
| **B** | **X-02** — page count disputed across 58 / 69 / 85 / 102 / 127 / ~135 | Baseline: **96 pages** | 96 appears nowhere in X-02. The workbook does not resolve the dispute — it adds a seventh value. If 96 is authoritative it should retire the others; nothing states that it is. |
| **C** | **X-05** — `the-curve.html` title claims "1.8 million words… absent from most of it" against a 17.9M-word scan and 840,248 Vedic words | `the-curve` is in cluster 4 (caste vocabulary corpus), Decision **Split**, Risk **Medium** | Genuine overlap. The workbook flags the page for structural reasons; the register knows precisely which number on it is wrong. Neither artefact carries the other's information. |
| **D** | **X-10** — MVP shape disputed, four successive proposals at S-10 | The MVP sheet's 15 pages | A **fifth** proposal, presented without reference to the prior four. The register's judgement that MVP shape is unstable applies directly to this sheet. |
| **E** | **X-15** — live self-contradictions on `the-killed` h1, `the-names` h1, and the `brahmi` card; WORKLIST claims two fixed, `the-names` unmentioned | All three are in the audit: `the-killed` and `the-names` in cluster 1, `brahmi` in cluster 8; all Decision **Revise** | Closest true overlap. The workbook groups these pages for *shared-ledger* reasons and never mentions that two of them carry unresolved h1 contradictions. Its per-page assessment did not detect what the register already records. |
| **F** | **X-16** — "institution vs museum" unresolved: "living research museum with institute functions" vs "museum and research institution" | Environment Map thesis: "the institutional shell remains stable"; Summary titles the site *"A Digital Museum of Ancient South Asia"* | The workbook builds its entire organising scheme on a stable institutional identity that the register records as contested. The Environment Map presupposes X-16 is closed. |
| **G** | **X-19** — batch-16 verdict: VELI-09 calls older pages SOUND with no re-sourcing required; the owner said most pages were problematic and every page would be re-examined | **Keep = 46**, of which 44 are Risk Low and absent from Claim Risk entirely | A third position on the same question, closer to VELI-09's than to the owner's. 46 pages are cleared to "proceed to normal review" with no claim extracted. If the owner's position stands, this is the workbook's largest single exposure. |

**Also: X-14 concerns `rakhigarhi` — the live page asserting no seafaring in the
Rigveda against the corpus file's `nau-` at n=40. `rakhigarhi` is not among the
96 pages.** Either the frozen baseline predates it, or it was removed, or the two
artefacts describe different builds. This is unresolved and bears on whether the
audit's "96 pages" covers the site the register is talking about at all.

**Net:** the 19 contradictions and the 32 overlap rows are complementary, not
duplicative — but the workbook is **downstream of five of them without knowing
it** (A, B, D, F, G). Where the register records a dispute, the workbook has
silently picked a side and built on it. That is the specific risk of merging the
two artefacts naively: the workbook's confidence would launder the register's
open questions.

---

## 7. The judgement axes, and which have no register

The workbook's real contribution to this repository's method is that it
**separates three kinds of judgement that a single "is this good?" question would
collapse** — and demonstrates that a page can score differently on each.

| Axis | Question | Vocabulary | Where it lives |
|---|---|---|---|
| **Editorial** | Does this page have a defensible curatorial role, and is it correctly placed and non-duplicative? | Decision (Keep/Revise/Hold/Split/Merge), Environment, Type, cluster membership | Page Audit, Environment Map, Overlap & Tensions |
| **Evidentiary** | Are the load-bearing claims supported, and at what verification priority? | Risk, Risk type, Source state, Central claim | Claim Risk, and Risk/Source-state columns in Page Audit |
| **Production** | What must be made, licensed, cleared and credited before this can ship? | Asset class, Documentary standard, Priority, Source/commission route | Asset Register, Summary release gates |

The separation is real and is demonstrated by the data. `artifact-atlas` is
editorially strong (Keep, MVP rank 3, the connective spine), evidentially
unexamined (8 words of prose, 88 unlinked entries, no Claim Risk row, Low risk by
default because a language-pattern detector cannot flag prose that isn't there),
and production-heavy (5 asset slots including a verified dataset carrying a
disputed number). One page, three different verdicts. Any instrument reporting a
single score would have to lose two of them.

A fourth axis is implied and unnamed: **institutional/ethical** — right-of-reply
discipline, community consultation, "digitization is not restitution," consent
for pronunciation recordings. The workbook scatters it across `Avoid` cells,
cluster recommendations and a "Not completed" row, without a vocabulary or a
column. It is not one of the three the workbook separates; it is the one it keeps
noticing and never names.

### What this repository currently has a register for

**The evidentiary axis, and only partially.** `03-REGISTERS/inherited-claims.csv`
is the sole register: 369 rows, all `INHERITED-UNVERIFIED`, all `source_id` empty,
all `retrieval_date` empty, all `supports_page` empty. Its claims are about the
project's conversation record, not about history. `02-SOURCES/access-ledger.csv`
holds 18 source-access probes. `05-HOLDS/` is empty.

So even on the evidentiary axis, the repository has a register of *inherited
assertions* but not yet a register of *page-level historical claims*. The
`supports_page` column exists in the schema and is empty in all 369 rows — the
join that would connect evidence to published surface is specified and unused.
The 38 central claims in `Claim Risk` are precisely the rows that would populate
it.

### What this repository has no register for

- **The editorial axis — no register.** Nothing in `03-REGISTERS/` records a
  publication decision, an environment assignment, or a duplication finding.
  There is no vocabulary here for Keep/Revise/Hold/Split/Merge and no place a
  decision could be logged, revised, or reversed with a reason. This workbook is
  currently the *only* editorial record in existence, it is a frozen snapshot of
  a build from 2026-09-01, and it is `INHERITED-UNVERIFIED`.

- **The production axis — no register.** Nothing tracks assets, rights, licences,
  credits, alt text, or commissioning. 392 asset slots, 96 rows of `To research`
  and `Needed`, zero owners. Release gate 3 (image rights and provenance) has no
  home in the current structure, and Method & Limits lists image-rights clearance
  under "Not completed."

- **The institutional/ethical axis — no register, and no name.** Community
  consultation, right-of-reply, consent for recordings, restitution posture.
  `CLAUDE.md` routes living-community consent questions to owner escalation but
  provides nowhere to record one that has been raised and is pending.

- **Cross-page consistency — no register.** Release gate 2. The nine clusters are
  the only such record and they are all `Open`.

A concrete consequence: **the workbook's editorial and production judgements
cannot currently be promoted, contested, or superseded**, because promotion in
this repository requires a register row and a logged retrieval, and no register
accepts a row of either type. They can only be re-inherited, whole, from a
spreadsheet.

---

## 8. What this document does not do

Per instruction and per `CLAUDE.md`: nothing here redesigns the workbook, merges
its sheets, or acts on any decision in it. No page has been kept, revised, held,
split or merged. No asset has been sourced. No claim has been promoted.

Everything in this directory remains `INHERITED-UNVERIFIED`. Items requiring a
decision are recorded in `DECISIONS-NEEDED.md`. No retrieval was attempted for
this document, so no access-ledger rows were added and no domains were requested.
