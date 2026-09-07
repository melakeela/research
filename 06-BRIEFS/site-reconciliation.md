# Site reconciliation — SITE-INVENTORY.md against the inherited record

**Compiled** 2026-09-07.
**Sources read, in full:**

| Short name | File | Locator basis |
|---|---|---|
| the inventory | `06-BRIEFS/SITE-INVENTORY.md` | line numbers in that file; page entries cited by filename |
| the handoff | `01-INHERITED/claude-project-handoff.md` | `L<n>` line numbers |
| the register | `03-REGISTERS/inherited-claims.csv` | `IH-nnn` claim IDs |

The inventory was retrieved from `melakeela/site` `main` at commit
`e6b6b67a62563f701922b67b7adf4ee1119ab094`, blob `342cc55b0933813bc6a27fe32d0935242037fbf8`,
and committed here byte-identical. The retrieval is logged as `SRC-019` in
`02-SOURCES/access-ledger.csv`.

---

## 0 · Status of everything below

**Nothing in this document promotes a claim.** All 369 rows of
`03-REGISTERS/inherited-claims.csv` carry `INHERITED-UNVERIFIED`, and every row's
`supports_page` field is empty (checked across all 369 rows). No register row is
tied to a page by the register itself; every page-to-claim link named below is a
link this document draws by reading the two texts together, not one the register
already asserts.

Two different kinds of statement appear below, and they do not carry the same weight:

- **Statements about what the inventory says.** `VERIFIED` against `SRC-019`, with a
  filename or line locator. The inventory is a named source, retrieved and hash-checked.
- **Statements about the deployed site.** `PROVISIONAL` at best. The inventory records
  each page's `<title>`, `<meta name="description">` and a one-line summary drawn from
  its `<h1>`–`<h3>` headings (inventory L5–L6). It does not record page bodies. A claim
  present in a body but absent from a heading is invisible to it, so the inventory can
  show that something **is** asserted on a page; it can rarely show that something is
  **not**.

The handoff is itself explicit that it is not a verification pass (L10, `IH-002`) and
that it could not confirm whether items marked "verify done" were completed (L623).
Reading it against a site inventory does not repair that. It relocates the question.

**Matching method.** Where the handoff names a filename, matching is by filename and is
exact. Where the handoff names only a concept ("the godman economy", "the Chinese
pilgrims"), matching is by subject and is **inference**, marked as such on every line.
Subject inference cannot distinguish a renamed page from a differently-named page
covering similar ground; both readings are stated wherever they diverge.

**Counts.** The inventory states 133 HTML files at the repository root (inventory L3).
Sub-list arithmetic below: 33 + 13 + 3 = 49 pages accounted for by the handoff, 84 not.

---

## 1 · Built and planned

### 1a · Exact filename match — 33 pages

The handoff names these files and the inventory carries them.

**The T2 build list** (handoff L370, `IH-197`) names 26 pages; 25 are present:

`the-words-of-caste` · `the-late-hymn` · `caste-was-law` · `the-three-ancestries` ·
`who-named-india` · `the-eastern-tradition` · `meluhha-trade` · `keeladi` ·
`the-narrowing` · `the-water-city` · `one-script-many-kingdoms` · `the-womb-doctrine` ·
`jatization` · `birth-was-not-always-destiny` · `criminalised-today` · `visvamitra` ·
`origin-myths` · `the-later-count` · `the-computed-dawn` · `the-genome-of-caste` ·
`tinai` · `the-medicine-question` · `before-the-indus` · `the-vedda` · `the-deep-root`

The 26th, `the-layers-under-the-language` ("Palimpsest, not purity"), is absent — see §2.

**Named elsewhere in the handoff** (8 pages):

| Page | Handoff | Register |
|---|---|---|
| `the-killed.html` | L71 (C-08, h1 corrected 1 Sep) | `IH-020` |
| `brahmi.html` | L77 (C-11, fixed 1 Sep) | `IH-023` |
| `steppe.html` | L88 (C-16 6.1, "one individual" must go) | `IH-029` |
| `endogamy-clock.html` | L88 (same); L382 resolves live | `IH-029`, `IH-201` |
| `two-classical-languages.html` | L107 (C-19), L350, L356 | `IH-038`, `IH-194` |
| `enter.html` | L146 (C-32 packaging bug); L382 resolves live | `IH-052`, `IH-201` |
| `artifact-atlas.html` | L230 (V-22), L350; L382 JS-rendered | `IH-105`, `IH-201` |
| `rakhigarhi.html` | L156 (C-36), L487 (X-14) | `IH-056`, `IH-263` |

**Register claims load-bearing for pages in this group** (page-to-claim links drawn here,
not asserted by the register):

- `before-the-indus.html` — `IH-124` (Baghor I, contextual dating c. 9000–8000 BCE, no
  directly datable material at the feature); `IH-051` (headline downgraded from
  "20,000 years older than the Vedas"); `IH-301` (the deep-history search gate, still owed);
  `IH-243` (Kenoyer et al. 1983 HELD — reached via citation, not read).
  The inventory's entry for this page ("Baghor shrine stone, sunrise-facing Mesolithic
  burials") carries no "20,000 years" figure, which is consistent with the C-31 downgrade
  having landed. Consistency is not confirmation: the inventory summarises headings only.
- `the-vedda.html` — `IH-051` (headline qualified from "here first… called a dialect until
  it died"); `IH-128` (P-20: the deep tribal link holds, "first" and the language
  classification do not). Inventory title reads "Ancient Ancestry, Lost Language"; meta says the language
  "disappeared within living memory". Consistent with the correction.
- `the-eastern-tradition.html` — `IH-129` (P-21 Bronkhorst, `CONTESTED` but respected; the
  handoff's note at L259 places it on exactly this page).
- `the-deep-root.html` — `IH-146` (H-12 Elamo-Dravidian, live; the handoff records that this
  page "marks sources"); `IH-131` (Desset 2022 Linear Elamite contains no Meluhha).
- `the-computed-dawn.html` — `IH-108` (Kali Yuga epoch back-calculated, planets not in
  conjunction).
- `keeladi.html` — `IH-113` (the 5,500-artefact → 982-page-report → 114-page-evaluation
  sequence, PROVISIONAL, "pin each step").
- `the-medicine-question.html` — `IH-050` (Patwardhan's AYUSH interest disclosed, C-30).
- `jatization.html` — `IH-303` (the jāti-etymology verification was owed and the page was
  built anyway); `IH-046` and `IH-317` (re-attribution owed, unconfirmed).
- `birth-was-not-always-destiny.html` — `IH-046`, `IH-317` (same re-attribution, unconfirmed).
- `the-womb-doctrine.html` — `IH-097` (the varṇa-womb passage present in ŚB 14, absent from the
  parallel ChU 5.10.7), whose "accretion" label the handoff records as inference (L222).
- `the-genome-of-caste.html` — `IH-127` (gotra genetics: Y-lineage village-specificity 79%,
  endogamous stratification 4–6 kya).
- `steppe.html`, `endogamy-clock.html` — `IH-029` (twelve individuals on a cline, not one).
- `the-killed.html` — `IH-020` (the direction must be stated: incomers, settled locals).
- `brahmi.html` — `IH-023`, `IH-102` (Aśokan inscriptions do not name their own script),
  `IH-103` (Sanskrit lacks ḻ, ṟ, ṉ).
- `artifact-atlas.html` — `IH-105` (194 site records, 315 class-windows, 145 rows `assumed`);
  `IH-250` (X-01, six-way site-count disagreement). See §4.
- `two-classical-languages.html` — `IH-038` (vowel-writing not a Greek invention; the shared
  Achaemenid state must be on the page); `IH-132` (Achaemenid chronology); `IH-241`
  (royal inscriptions HELD, not cited by locus); `IH-194` (Burkert named, not accessed).

### 1b · Subject match, filename differs or was never given — 13 pages

Every line here is **inference**. The handoff names a concept; the inventory carries a page
on that concept under a different or previously unstated filename.

| Built page | Handoff item | Register | Confidence |
|---|---|---|---|
| `excavation-bias-funding.html` | "coverage bias and the Keeladi report" (L352); `coverage` headline corrected to "many gaps follow the money" (L144) | `IH-051` | High — the inventory's meta reproduces the corrected wording verbatim: "Many gaps in the archaeological record follow the money" |
| `four-varnas-one-verse.html` | `one-verse` headline corrected to "the explicit fourfold varṇa scheme appears together in one verse" (L144) | `IH-051`, `IH-096` (TS 2.5.10.1, TS 6.2.5.3) | High — the corrected formulation is the page's meta description |
| `priority-claims-south-asia.html` | `who-had-it-first.html` (L103, L350) | `IH-037`, `IH-190` | Medium — title reads "Who Had It First"; filename differs. Whether this is the same page renamed or a replacement is not determinable from the inventory |
| `foreign-accounts-ancient-india.html` | "the Chinese pilgrims (Faxian, Xuanzang, Yijing)" (L352) | — | Medium — inventory names Faxian and Xuanzang; Yijing does not appear |
| `kural.html` | "the Kuṟaḷ" (L352) | `IH-091` (1,330 couplets, zero *cāti*, zero *vētam*) | High |
| `kinship-terms-south-asia.html` | "kinship across the ancient world (65 KB, 12 red boxes — over every limit)" (L352) | `IH-130` (xwēdōdah breaks IE-exogamy) | High — inventory records xwēdōdah on this page |
| `veli.html` | "the Veḷi concept from DEDR" (L352) | `IH-188` (three DEDR entries, 29-language open/expelled complex) | High |
| `what-travelled.html` | named at L144 as `what-travelled`, two headlines corrected | `IH-051` | High |
| `the-ledger.html` | "a Ledger/credibility page" (L370); the Ledger feature (L134) | `IH-046`, `IH-315` | Medium — see §4, the claims ledger is separately recorded as unbuilt |
| `sources.html` | "the Sources page publishes conduct findings about named living scholars" (L386) | `IH-204`, `IH-326` | High |
| `research-index.html` | "the Research Index lists 127 entries under a header claiming 102" (L229) | `IH-104`, `IH-251` | High |
| `search.html` | "site search" — listed among the external review's still-owed items (L368) | — | High — owed in the handoff, present in the inventory |
| `index.html` | `veli-landing.html`, "18 KB, four movements" (L350); "landing… resolves" (L382) | `IH-190`, `IH-201` | **Low.** The handoff never writes `index.html`. Whether the landing was renamed, replaced, or sits at both paths cannot be settled from the inventory |

### 1c · Recorded as *not built*, present in the inventory — 3 pages

The handoff lists these as conceived and unbuilt (L372, `IH-198`). The inventory carries
them. Their handoff status is stale, and in two cases the build appears to have overtaken a
verification gate — see §4.

| Built page | Handoff status | Register |
|---|---|---|
| `academia-battlefield.html` | "'Genetics and nationalism' / 'Academia as a battlefield' (delayed pending verification of Reich quotes)" | `IH-198`; gate `IH-305` (work item 37) |
| `vedism-is-not-hinduism.html` | "the 'Vedism is not Hinduism' naming page" — not built | `IH-198`; frame at `IH-069`/D-08 |
| `gotra.html` | "gotra-level genetics" — not built; "partly delivered as the-genome-of-caste" | `IH-198`, `IH-127` |

---

## 2 · Planned but not built

Nothing in this section proposes that any of it be built. It records what the handoff names
and the inventory does not carry.

### 2a · Named as a filename, absent from the inventory

| Handoff filename | Where | Register | Reading |
|---|---|---|---|
| `the-layers-under-the-language` | L370, T2 build list, glossed "Palimpsest, not purity" | `IH-197` | Recorded as **built** in T2; no such file at root. No inventory entry mentions "palimpsest" or "purity" (searched). Either renamed beyond recognition, removed, or never shipped — the inventory cannot distinguish these |
| `who-had-it-first.html` | L103, L350 — carries the Kuiper/Witzel/Mayrhofer substrate word-lists in its footer | `IH-037`, `IH-190`, `IH-231` | Recorded as **built** in T1; absent. `priority-claims-south-asia.html` carries the title (§1b). If they are the same page renamed, the substrate word-lists and their HELD footer moved with it; the inventory's summary of that page mentions no substrate list |
| `the-curve.html` | L478 (X-05) — `<title>` overstates: "1.8 million words… absent from most of it" against a 17.9 M scan | `IH-254` | Absent. Two curve pages exist: `the-vocabulary-curve.html` and `caste-vocabulary-curve.html`, neither carrying the disputed title string. X-05 is therefore not visible in the inventory; whether it was fixed, split or dropped is undetermined |
| `veli-landing.html` | L350 | `IH-190` | Absent as a filename. See `index.html`, §1b, low confidence |
| `the-firms.html` | L113 — named as "the real page" a broken cross-link should have pointed to | `IH-042` | Absent. `vedic-ritual-economy.html` is titled "The Ritual Economy: Immortality Bought and Sold", which is the subject of the *broken* link's name (`one-buys-immortality.html`). Three names, one subject, no resolution available from the inventory |
| `one-buys-immortality.html` | L113 — the broken cross-link | `IH-042` | Absent, **as the handoff says it should be**. Consistent |

### 2b · Named as a concept, no page found

| Concept | Where | Register | Note |
|---|---|---|---|
| *Who gets to be speculative* | L352 (T1, proposed not built); L279 (H-10); L547 (work item 41); L572 (HOLD) | `IH-192`, `IH-144`, `IH-309`, `IH-330` | No page of this name. `indology.html` — "Western Indology and Its Asymmetric Evidence Standards… The double standard built into a discipline's founding assumptions" — covers adjacent ground. See §4 |
| The eight doors and six numbers of the landing (Acts III–IV) | L352; work item 13 | `IH-192`, `IH-280` | Never chosen. The inventory records no door or number structure on `index.html` |
| The atlas as spine, with layer toggles (scripts · śramaṇa · trade · ports · aDNA · Chinese routes · SE Asia) | L352 | `IH-192` | Inventory records side panels for texts, unlocated finds and current selection — no layer toggles |
| The atlas language-shift layer | L372 | `IH-198` | Not visible in the atlas entry |
| The three depths (object · one-sentence finding · evidence) | L352, with the verdict "the platform has only the third" | `IH-192` | No depth toggle recorded anywhere in the inventory |
| Sound (Tamil words spoken with DEDR reflexes) | L352 | `IH-192` | Three music pages exist (`music`, `where-music-begins`, `the-lost-harp`); none is described as carrying audio |
| The godman economy | L109 (C-20), L352 (built in T1) | `IH-040` | Recorded as **built** in T1. No page found: "godman", "guru", "swami", "Asaram", "Ram Rahim" return nothing in the inventory. The nearest is `the-borrowed-lineage.html` (a retreat invoking the siddhars), which is not the same subject |
| Mahadevan graffiti | L352 (built in T1) | `IH-142` (H-08) | Recorded as **built** in T1. No standalone page; `brahmi.html` covers "the graffiti evidence" as one of five subjects |
| Prajāpati / Rudra | L352 (built in T1) | `IH-101` (nakṣatra list, Rudra assigned Ārdrā) | Recorded as **built** in T1. No page of that name. `rigveda-word-collocations.html` covers "Rudra, Indra, Dasyu and Dāsa, Paṇi, Muni and Keśin" — a collocation page, not a Prajāpati/Rudra page. Ambiguous |
| "How a Religion Was Assembled" | L372; also the retained project name after the Cinduism overrule (L302) | `IH-198`, `IH-162` (Cinduism rejected; project kept as "How a Religion Was Assembled"), `IH-277` (the ruling is still awaited) | No page. The subject is distributed across several built pages; no single page carries the name |
| "A republic made a defective birth" (Manu 10.22, 10.26) | L372; V-17 at L225 flags "not yet on any page as of 30 Aug — check whether built since" | `IH-198`, `IH-100` | No page found: "Licchavi", "vrātya", "Manu 10" return nothing in the inventory. `the-fifth-was-a-guess.html` covers the fifth varṇa and the Niṣāda, which is adjacent but is not the *pratiloma* material |
| The per-topic credibility ledger | L372 | `IH-198`, `IH-315` | `bronkhorst.html` ("Auditing a Source We Rely On") is a per-source audit page. Whether that constitutes the per-topic ledger is not determinable |
| Corded Ware animation | L372 | `IH-198` | No animation recorded — though the inventory records only titles, meta and headings, so an embedded animation would not appear in it either way. `the-expansions.html` covers Indo-European expansion |
| Minority-control case study | L372 | `IH-198` | Not identifiable in the inventory |
| The OUT OF CONTEXT object-journey series | L372 | `IH-198` | No series recorded |
| The "Many Laws" gallery | L372 | `IH-198` | `non-brahmanical-legal-traditions.html` catalogues "dozens of non-brahmanical legal systems" — a page, not a gallery. Adjacent, not equivalent |
| "Languages at the edge of the archive" gallery | L372 | `IH-198` | `the-languages-we-lost.html` covers South Asian isolates — again a page, not a gallery |
| The Unreturned / Berlin Room (VELI-06 Theme 3) | L372 | `IH-198` | No page. "Berlin", "repatriation", "returned" return nothing |

### 2c · Structural work named as owed, not visible in the inventory

The inventory records titles, meta descriptions and headings. Page furniture below the
heading level is outside what it can show, so **absence here is not evidence of absence** —
these are listed because they are named as owed and nothing in the inventory confirms them.

- The claims ledger as a live page — "Tier 1.1 in every file… the product" (L555, `IH-315`).
  `the-ledger.html` exists and is described as a *source*-grading page ("how this platform
  ranks its sources by venue, author, funding and independence"), not a claims ledger. The
  handoff distinguishes the two: the credibility Ledger was built in T2 (L134, `IH-046`),
  the claims ledger is work item 47 and unbuilt.
- `.cite` block retrofit across ~80 pages (L556, `IH-316`).
- The editorial-accountability layer for the Sources page — who signs, corrections log,
  right of reply (L566, `IH-326`, `IH-204`). The inventory's `sources.html` entry describes
  four questions and graded source lists; no editorial name, log or reply mechanism appears.
- Index cards, 6 of 58 → all (L560).
- Downloadable data or code — the handoff records that "the reproducibility promise cannot
  be exercised by a visitor because no data or code is downloadable from any page read"
  (L386, `IH-203`). No inventory entry mentions a download.
- The two `.md` files that 404'd live, `RIGVEDA_corpus_analysis.md` and
  `MELUHHA_TO_KEEZHADI_synthesis.md` (L146, L382, `IH-052`, `IH-201`). **The inventory
  covers HTML files only** (L3), so it cannot speak to either, in any direction.

---

## 3 · Built but not planned

84 of the 133 pages are not accounted for by any handoff build list, plan list, or
correction. The handoff's own X-02 (L475, `IH-251`) anticipates exactly this: "The live
site has more pages than any project file records… Either 42 pages were built between 2 and
4 Sep (in the unretrievable session) or the live index counts routes the files don't."
The unretrievable session is the 6 Sep session of thread T2 (L14, `IH-003`), which the
handoff classifies as `NOT FOUND IN THIS SEARCH`, not as absence (L15, `IH-005`).

### 3a · Built, attested in the handoff as existing, never named in a build or plan list — 7 pages

These seven are a subset of the 84, pulled out because the handoff discusses them; each is
also carried in the alphabetical list at §3b, marked *(also §3a)*.

The handoff discusses these pages as live without ever listing them as planned or built.

| Page | Handoff attestation | Register |
|---|---|---|
| `who-writes-the-textbook.html` | "the live site… folds the 11 March 2026 Supreme Court direction concerning Michel Danino into a migration-denial narrative" (L154, C-35); P-26 (L264) | `IH-134` |
| `the-vocabulary-curve.html` | via `the-curve.html` (L478, X-05) — filename does not match | `IH-254` |
| `caste-vocabulary-curve.html` | via `the-curve.html` (L478) — filename does not match | `IH-254`, `IH-084`, `IH-085` |
| `the-nine-enemies.html` | the nine-enemies material is attributed to `the-killed.html` (L71) | `IH-020` |
| `elamo-dravidian-hypothesis.html` | H-12 is recorded as sitting on `the-deep-root.html` (L281) | `IH-146` |
| `rigveda-word-collocations.html` | the `colloc.py` results (L219, V-11, V-12) and the T1 "Prajāpati/Rudra" page (L352) | `IH-192` |
| `the-northwest-cousin.html` | H-01 Brahui relict distribution (L270); no page is named for it | `IH-135`, `IH-156`, `IH-236` |

### 3b · The full residual list — all 84 pages

Alphabetical, covering every one of the 84. The seven from §3a are marked *(also §3a)*;
the other 77 are absent from the handoff entirely. Register claims are noted where a register
row is load-bearing for what the inventory says the page asserts; the link is drawn here, not
by the register.

| Page | Title | Load-bearing register claims |
|---|---|---|
| `ancient-south-asian-astronomy.html` | Star Names and Sky Knowledge in Ancient South Asia | `IH-101` (nakṣatra list TS 4.4.10) |
| `authorship-attribution-ancient-texts.html` | Who Gets Credit: Attribution in Ancient Indian Texts | — |
| `beneath-both-waves.html` | Beneath Both Waves: The Forager Lineages of South Asia | `IH-109` (AASI fraction of the Indus Periphery Cline), `IH-119` (ancestry ≠ language), `IH-127` |
| `brahmavadini.html` | Brahmavadini: Women Who Studied the Vedas, and the Closing | — |
| `bronkhorst.html` | Bronkhorst and Greater Magadha: Auditing a Source We Rely On | `IH-129` (P-21, CONTESTED but respected) |
| `caste-enforcement-mechanism.html` | The Mechanism: How Social Hierarchy Was Enforced | `IH-120` (Dharmaśāstra intent, differential penalties) |
| `caste-survives-conversion.html` | Caste Survives Conversion: The Test the Law Refuses | — |
| `caste-vocabulary-curve.html` | *(also §3a)* The Caste Vocabulary Curve Across the Vedic Corpus | `IH-084`, `IH-085`, `IH-088`, `IH-096`, `IH-255`, `IH-274` |
| `chains-of-transmission.html` | Isnad and Chains of Transmission in Text Criticism | — |
| `climbing-the-ladder.html` | Climbing the Ladder: Sanskritisation and Its Price | `IH-145` (H-11 varṇa mobility — Quora/wisdomlib only, "do not assert") |
| `counted-as-nothing.html` | Counted as Nothing: How a Death Stops Being Manual Scavenging | — |
| `dasa-forts-rigveda.html` | The Dasa Forts: Indus Country, But Centuries Too Late | `IH-022`, `IH-153`, `IH-338` (phonotactic test invalid) |
| `dravidian-sky.html` | Dravidian Star Names and Indigenous South Indian Astronomy | `IH-101` |
| `dravidian-sounds-sanskrit-lacks.html` | Sound Changes: Dravidian Phonemes Sanskrit Could Not Write | `IH-103` |
| `elamo-dravidian-hypothesis.html` | *(also §3a)* Elamite and Dravidian: The Contested Language Link | `IH-146` (H-12, live), `IH-131` (Desset 2022 Linear Elamite: no Meluhha, no Indus reference) |
| `exhibits.html` | Exhibits: the arguments, grouped by what they follow | `IH-258` (brand — see §4) |
| `explore.html` | Explore Mela Keela: the atlas, the instruments, the evidence | `IH-057` (140/158/175), `IH-250`, `IH-258` |
| `forest-peoples-sanskrit-record.html` | Forest Peoples in the Sanskrit Record | — |
| `geography-in-vedic-texts.html` | Mapping the Geography Inside the Vedic Texts | `IH-016` (the rejected "Archaic stratum knows Afghanistan first" reading, R-02), `IH-092` (Vipāś 3, Rasā 10), `IH-017`, `IH-286` |
| `how-buddhism-left.html` | How Buddhism Left India: A Disappearance With No Single Cause | — |
| `indology.html` | Western Indology and Its Asymmetric Evidence Standards | `IH-144` (H-10), `IH-330` (HOLD), `IH-034` |
| `indus-to-vedic-gap.html` | The Gap Between the Indus and the Vedic Texts | `IH-136` (H-02), `IH-137` (H-03), `IH-036` (Para-Munda earns a note, not a lane) |
| `manuscript-custody.html` | Manuscript Custody: Who Held the Texts and Who Was Kept Out | — |
| `material-culture-ancient-south-asia.html` | What They Had: Material Culture of Ancient South Asia | — |
| `mitanni.html` | Mitanni: Indo-Aryan Names in a Syrian Kingdom | — |
| `mlecha.html` | Mleccha: The Word for Those Who Spoke Wrongly | `IH-087` (*mleccha* 0 in the Rigveda) |
| `music.html` | Tamil Pan to Raga: Music Systems of Ancient South Asia | `IH-139` (H-05 yāḻ/gamaka, labelled INFERENCE) |
| `naming-in-ancient-india.html` | Names and Naming in the Ancient South Asian Record | `IH-021` (collocation beats etymology), `IH-027`/`IH-154` ("of undetermined origin", never "originates in") |
| `non-brahmanical-legal-traditions.html` | Law Beyond the Dharmasastra: Other Legal Traditions | `IH-120` |
| `oral-traditions-unwritten.html` | The Unwritten: Oral Traditions That Left No Text | — |
| `paid-in-cattle.html` | Paid in Cattle: What Vedic Poets Were Given for Hymns | `IH-099` (Griffith's Latin renderings and omission) |
| `panini.html` | Panini's Grammar and the Sanskrit It Standardised | — |
| `rigveda-geography.html` | The Land in the Rigveda: Rivers, Regions and Geography | `IH-017`, `IH-286`; see §4 for a title/heading mismatch |
| `rigveda-outsider-contempt-count.html` | Counting Contempt for Outsiders in the Rigveda | `IH-020`, `IH-087` (Rigvedic counts: *śūdra* 1, *mleccha* 0, *caṇḍāla* 0), `IH-095` |
| `rigveda-word-collocations.html` | *(also §3a)* Word Company in the Rigveda: Gods, Enemies, Collocations | `IH-094` (Pipru↔Ṛjiśvan at 639× expected; *kuyava* zero with barley/field/cultivation), `IH-095` (Rudra's strongest collocate is medicine; Dasyu and Dāsa structurally different; Paṇi economic not ethnic) |
| `sacred-ash.html` | Sacred Ash: The Ashmounds and What They Do Not Prove | `IH-126` (~3000 BCE), `IH-301` (gate); see §4 |
| `sanskritisation-of-place-names.html` | The Renaming: Places, Peoples and Sanskritised Names | `IH-045` (Pataliputra→Patna toponym search, never run), `IH-158` (R-12) |
| `siddha-and-ayurveda.html` | Siddha and Ayurveda Compared on Their Own Terms | `IH-050` |
| `the-borrowed-ancestor.html` | The Borrowed Ancestor: How Local Myths Get Absorbed | — |
| `the-borrowed-lineage.html` | The Borrowed Lineage: Invoking the Siddhas Without Them | `IH-040` (living figures: only the convicted, only the record) |
| `the-broken-chain.html` | The Broken Chain: The Order of Nuns That Could Not Return | — |
| `the-definition.html` | The Definition: Hindutva's Own Test, Applied to Its Authors | — |
| `the-expansions.html` | The Expansions: Indo-European, From the Volga to Everywhere | `IH-111` (Steppe_MLBA ≈ ⅔ Yamnaya-related, route loops west), `IH-026` (admixture dates are lower bounds on arrival) |
| `the-father-tongue.html` | The Father Tongue: The Arrival That Ended Up at the Bottom | `IH-119` (Munda ~2000 BCE; O-M95 ancient in India; male-biased incoming), `IH-115` (eastern Indo-Aryan closer to Munda → shift not replacement), `IH-127` |
| `the-fifth-was-a-guess.html` | The Fifth Was a Guess: How the Outcaste Entered the Scheme | `IH-100` (Manu 10.22/10.26 — V-17, "not yet on any page" as of 30 Aug), `IH-087` |
| `the-gods-people-had.html` | The Gods People Had: Yakṣas Before Anyone Else Arrived | — |
| `the-grants-that-survived.html` | The Grants That Survived: Ritual Rank Converted Into Land | — |
| `the-guilds-and-the-raid.html` | The Guilds and the Raid: Tamil Reach Across the Bay | — |
| `the-king-they-claimed.html` | The King They Claimed: Suheldev and the Rajbhars | — |
| `the-languages-we-lost.html` | Language Isolates of South Asia: Burushaski, Kusunda, Nihali | `IH-128` (P-20 Vedda: deep tribal link, language lost within living memory), `IH-051` (the Vedda headline qualified) |
| `the-lost-harp.html` | The Lost Harp: The Yāḻ and What Extinction Looks Like | `IH-139` |
| `the-lost-materialists.html` | The Lost Materialists: Cārvāka, Known Only From Refutations | — |
| `the-margins.html` | The Margins: Where the Oldest Lineages Survive, and Why | `IH-127` |
| `the-markers-themselves.html` | The Markers Themselves: Y-Lineages Across Caste and Tribe | `IH-127`, `IH-119` |
| `the-maternal-line.html` | The Maternal Line: What the Women's Record Refuses | `IH-127` (mtDNA diverse against village-specific Y) |
| `the-nine-enemies.html` | *(also §3a)* The Nine Named Enemies of the Rigveda, and Who Was Paid | `IH-020`, `IH-094`, `IH-027`/`IH-154` ("of undetermined origin") |
| `the-northwest-cousin.html` | *(also §3a)* The Northwest Cousin: Brahui, Tamil and 191 Shared Roots | `IH-135`, `IH-156`, `IH-236`, `IH-194` |
| `the-other-half.html` | The Other Half of the Indus: What Pakistan Holds | `IH-045` (east-vs-south excavation coverage, never run) |
| `the-plateau.html` | The Plateau: Elam, the Indus, and the People Between | `IH-146`, `IH-131` |
| `the-proxy.html` | The Proxy: Who Carries the Indus Woman's Ancestry Now | `IH-029`, `IH-109` (P-01 Indus Periphery Cline), `IH-112` (P-04 AHG distribution, published version only) |
| `the-seal-still-holds.html` | The Seal Still Holds: Endogamy Measured in the Present | `IH-127` |
| `the-shape-of-a-grave.html` | The Shape of a Grave: Indus Burials and the Megaliths | `IH-301` (Indus death-rites ↔ megalith ↔ tribal correlation, owed; gate) |
| `the-survey-not-done.html` | The Survey Not Done: LiDAR and South Asia's Blind Spot | `IH-045` |
| `the-third-party.html` | The Third Party: Who Data Sovereignty Was Built For | — |
| `the-third-tradition.html` | The Third Tradition: The Ājīvikas, Known Only Through Rivals | `IH-129` |
| `the-uneven-arrival.html` | Hittites Spoke Indo-European. Their DNA Lacks Steppe Markers | `IH-111`, `IH-026`, `IH-119` (ancestry ≠ language) |
| `the-unread-script.html` | The Unread Script: Why Nobody Can Be Proved Wrong | `IH-136` (H-02 Dravidian-Indus, strongest contender, not proven), `IH-036` |
| `the-vocabulary-curve.html` | *(also §3a)* The Vocabulary Curve: When Exclusion Enters the Texts | `IH-084`, `IH-087`, `IH-274` |
| `therigatha.html` | Therigatha: Poems by the First Buddhist Women | — |
| `they-already-knew.html` | They Already Knew: Anti-Caste Movements and What Followed | — |
| `two-archaeologists.html` | Two Archaeologists: Who Gets the Museum, Who Gets Moved | `IH-040` (living figures: only the convicted, only the record) |
| `two-scarcities.html` | Two Scarcities: Real at Rakhigarhi, Made at Keeladi | `IH-113`, `IH-029` |
| `vedic-corpus-insertions.html` | Interpolations: Passages Added to the Vedic Corpus | `IH-121` (Puruṣa-sūkta late interpolation), `IH-089` (MBh caste vocabulary concentrated in Śānti and Anuśāsana) |
| `vedic-interpolations.html` | The Edits: Later Insertions in the Vedic Corpus | `IH-121`, `IH-089` |
| `vedic-ritual-economy.html` | The Ritual Economy: Immortality Bought and Sold | `IH-042`; see §2a and §4 |
| `voice-authority-ancient-texts.html` | Who Is Speaking: Voice and Authority in Ancient Texts | — |
| `what-survived-the-archive.html` | The Archive: What Survived, What Was Lost, and Why | `IH-248` (Sangam, Tolkāppiyam, Tēvāram, Pali canon, Śaunaka AV — NOT OBTAINED) |
| `what-the-children-are-taught.html` | What Indian Children Are Taught, and What Is Left Out | `IH-134` (the Danino order, HELD) |
| `what-varna-meant.html` | What Varna Meant in the Rigveda: All 23 Occurrences | `IH-086`, `IH-019`, `IH-287`; see §4 |
| `when-the-mixing-stopped.html` | When the Mixing Stopped: Founder Events and Dravidian | `IH-127`, `IH-117` |
| `where-music-begins.html` | Where Music Begins: Instruments Before and Around the Indus | `IH-139` |
| `who-was-allowed-to-know.html` | Who Was Allowed to Know: Secrecy as a Social Instrument | — |
| `who-writes-the-textbook.html` | *(also §3a)* Who Writes India's History Textbooks: The Danino Case | `IH-134` |
| `why-the-ranked-defend-the-ranking.html` | Why the Ranked Defend the Ranking: Hindutva Without Brahmins | — |

---

## 4 · Contradictions

Each item names what disagrees, where each side is recorded, and what the disagreement
turns on. None is resolved here; the inventory cannot resolve any of them, because it
describes the site rather than being the site.

**X-01 · The atlas count, now published on the atlas page.**
`artifact-atlas.html` carries the title "Artifact Atlas: 175 Ancient South Asian Sites
Mapped" and a meta description asserting "175 archaeological sites and 315 dated evidence
windows". The inventory also records that this page carries no headings in the HTML, its
headings being rendered at runtime by `assets/js/artifact-atlas.js` (inventory L7–L9) —
which matches T3's live finding that `/artifact-atlas` returns no text to a fetcher (L382,
`IH-201`). The handoff records six competing site counts — 140, 150, 158, 167→175, 194, 199
— and two window counts, 299 against 315 (L474, `IH-250`), and pairs 315 with **194**, not
with 175 (L230, V-22, `IH-105`). The atlas page therefore prints a pairing that appears in
no project record. Two further constraints bear directly: work item 2 requires the atlas be
extracted to JSON and every count generated from it (L502), and the HOLD at L571 (`IH-329`)
bars "any page count, site count or corpus total in public copy" until that is done. The
page publishes both numbers. The live three-way split C-37 records (140 on Enter, 158 on
Explore, 175 in the title — L158, `IH-057`) cannot be checked from the inventory: neither
`enter.html` nor `explore.html` states a number in its title, meta or headings.

**X-02 · The page count, with a seventh value.**
The handoff's series runs 58 · 69 · 85 · 102 · 127 · ~135 (L475, `IH-251`; L330, `IH-185`).
The inventory states 133 HTML files at the repository root (L3) — a new value, closest to
the ~135 that included routes and `.md` files. It is `ls`-derived, which is what standing
rule 14 requires (L597), but it counts root HTML files only and so is not directly
commensurable with the "127 index entries" or "102 header" figures. `research-index.html`
is described as indexing "every page on the site" without stating a count, so the
102-versus-127 discrepancy (L229, `IH-104`) is not visible in the inventory either way.

**X-06 and the corpus-total HOLD, against two published curve pages.**
`caste-vocabulary-curve.html` publishes "Corpus counts of caste vocabulary across a
17.9-million-word register — the jāti and dharma curves". `the-vocabulary-curve.html`
publishes "Machine-counted across 480 texts" and "Sudra appears once in the Rigveda and
1,053 times in the law books". The handoff records: the corpus total is itself contested,
17,934,563 against 17,919,338 (L476, `IH-252`); the jāti = 0 finding cannot be cited again
until the exact text set and method are stated (L479 and L506, `IH-255`, `IH-274`); the
jāti sense-split must be labelled "identified instances" everywhere (L524, `IH-288`); and
no corpus total may appear in public copy until Tier 0 items 2–7 are done (L571, `IH-329`).
The 1,053 figure appears nowhere in the handoff or the register.

**Varṇa's human-applied split: recorded as owed, published as done.**
`what-varna-meant.html` is titled "What Varna Meant in the Rigveda: All 23 Occurrences",
with a meta description asserting "Varna means colour in every Rigvedic instance. Its only
clear human application is ethnic and adversarial", and headings covering "All 23 Rigvedic
occurrences of varṇa sorted by sense". The register carries the count (`IH-086`, 23
occurrences in 180,196 words) but the handoff attaches "Human-applied split NEEDS-CHECK" to
it (L211), lists the split and the colour/skin count "done right" as work item 19 and still
owed (L523, `IH-287`), and records the same as OPEN at L69 (`IH-019`) and L348 (`IH-189`).
The page presents the sorted result the record says is not yet produced.

**The ashmound dates disagree, and the gate is open.**
`sacred-ash.html` states "Cattle-dung mounds in the Deccan, redated to c.2500–1800 BCE".
The register carries "~3000 BCE in the South Deccan, including Maski and Kupgal"
(`IH-126`, P-18, from Fuller 2007 / Bauer 2015 / Boivin 2004). These are different date
ranges from the same literature; the inventory gives no source for the redating. Separately,
ashmound global uniqueness is one of the four searches at work item 33 that PENDING-RULE 19
makes a **gate** for publishing contested deep-history claims (L539, `IH-301`), and the
same item sits on the HOLD list (L573). The page's own framing — "and What They Do Not
Prove", "where the evidence stops" — is not the contradiction; the date and the gate are.

**The phonotactic test, rejected, appears as a page heading.**
`dasa-forts-rigveda.html` covers "whether Śambara, Pipru and Cumuri can be Dravidian names
by phonotactics". C-10 records that Sanskrit phonotactics cannot test substrate origin
because nativisation destroys the test (L75, `IH-022`); it is REJECTED as R-07 (L293,
`IH-153`) and carried into standing rule 3 (L586, `IH-338`). The heading may frame the test
in order to reject it — the inventory cannot tell which — but the rejected instrument is
named as a line of enquiry on a built page.

**H-10 is on HOLD; a page on its subject is live.**
"Who gets to be speculative" must not be built until the citation history exists (L572,
`IH-330`; L547, `IH-309`; L279, `IH-144`), because the claim is about the *citation record*
and no citation history was ever assembled (L96, `IH-034`). `indology.html` is titled
"Western Indology and Its Asymmetric Evidence Standards" and its meta reads "How Sanskrit
derivations were treated as settled while Dravidian ones were stress-tested. The double
standard built into a discipline's founding assumptions." Whether this is the held claim in
another form, or a history of the discipline that makes no bibliometric assertion, is not
determinable from title and headings alone.

**Academia as a battlefield: gated on Reich verification, built.**
`academia-battlefield.html` is live and covers "findings that were withheld and the cost of
speaking". The handoff lists the page as not built, "delayed pending verification of Reich
quotes" (L372, `IH-198`), with the verification itself outstanding as work item 37 (L543,
`IH-305`) and Reich's public statements in the HELD register as "not verified" (L458).

**The Danino page: HELD, and two pages carry the subject.**
C-35 records that the live page "folds the 11 March 2026 Supreme Court direction… into a
migration-denial narrative", that per the T4 assessment the order concerned an NCERT Class 8
judiciary chapter and was modified in late May 2026, and that the page is **HELD** because
the order and the modification must be read directly — the assessment's characterisation
being itself secondary (L154, `IH-134`; L459; work item 29). `who-writes-the-textbook.html`
now states in its meta that Danino "was later barred by the Supreme Court", with no mention
of a modification, and `what-the-children-are-taught.html` covers the same NCERT changes.
Both readings remain HELD; the inventory adds a second page to the same held subject.

**Seafaring (X-14) is not visible either way.**
The live `rakhigarhi` page said "The Rigveda contains no seafaring" against the site's own
corpus file recording *naú-* at n = 40 (L156 and L487, `IH-056`, `IH-263`). The inventory's
`rakhigarhi.html` entry mentions neither seafaring nor *naú-*. The contradiction is neither
confirmed nor cleared. The same entry's meta does say "Twelve Indus-associated genomes",
which matches the C-16 6.1 correction (`IH-029`); the action item, however, named
`steppe.html` and `endogamy-clock.html`, and neither of those entries mentions individual
counts at all.

**The naming decision is open, and the site uses both names.**
D-14 records Melakeela-versus-Veḷi as **not finalised** (L189, `IH-075`), blocking prospectus
A1/A10, the deck, the domain and the landing copy (L510, `IH-276`); X-09 records four
successive brand architectures with none adopted (L482, `IH-258`); X-08 records three
candidate primary domains (L481, `IH-257`). In the inventory, `index.html` is titled "Veli:
A Digital Museum of Ancient South Asia" and `enter.html` "Enter Veli", while
`exhibits.html`, `explore.html` and `research-index.html` say "the Mela Keela museum",
"Explore Mela Keela" and "Every Page on Mela Keela". The unresolved decision is published on
both sides of itself, in `<title>` and `<meta>` text.

**Pairs of pages on one subject, where the handoff names one.**
Six subjects carry two pages each. In each case the handoff names one page, or none:

| Subject | Pages | Handoff names |
|---|---|---|
| The named Rigvedic enemies (nine, 117 mentions) | `the-killed.html`, `the-nine-enemies.html` | `the-killed.html` only (L71, `IH-020`) |
| Elamo-Dravidian | `the-deep-root.html`, `elamo-dravidian-hypothesis.html` | `the-deep-root.html` only (L281, `IH-146`) |
| The caste-vocabulary curve | `the-vocabulary-curve.html`, `caste-vocabulary-curve.html` | `the-curve.html` — neither (L478, `IH-254`) |
| Vedic interpolations | `vedic-interpolations.html`, `vedic-corpus-insertions.html` | neither |
| Vedic-text geography | `rigveda-geography.html`, `geography-in-vedic-texts.html` | neither |
| Ayurveda and Siddha | `the-medicine-question.html`, `siddha-and-ayurveda.html` | `the-medicine-question.html` only (L142, `IH-050`) |

Three music pages (`music.html`, `where-music-begins.html`, `the-lost-harp.html`) form a
seventh cluster; the handoff names none of them. This bears on standing rule 20 —
"never reference a page from memory; run the cross-link check" (L603, `IH-042`) — and on
X-02: which member of each pair the index and cross-links point at is not determinable from
the inventory.

**A page whose title and headings describe different subjects.**
`rigveda-geography.html` is titled "The Land in the Rigveda: Rivers, Regions and Geography"
with a meta description about "what geography the Rigveda actually knows, which rivers it
names", while the inventory's heading-derived summary reads "Land tenure and status — the
Chola land register, where priests received land and where they did not, the group with no
tenure category, land reform, and two diasporas." Title and metadata describe Rigvedic river
geography; the headings describe medieval and modern land tenure. This is one instance found
while reading; no systematic check of all 133 entries for title-heading mismatch was run,
so the count of such cases is unknown.

**Three pages the handoff records as built are absent, and one absent page has a
subject-twin.**
The godman-economy page, the Mahadevan-graffiti page and the Prajāpati/Rudra page are all
listed as built in T1 (L352) and none is present (§2b). `the-firms.html`, named at L113 as
the real page a broken cross-link should have pointed to (`IH-042`), is absent, while
`vedic-ritual-economy.html` carries the title "The Ritual Economy: Immortality Bought and
Sold" — the subject of `one-buys-immortality.html`, the page the handoff says does not
exist. Under X-02 all four are consistent with either renaming or removal.

---

## 5 · Where the handoff is ambiguous about whether something exists

Stated separately because these are not contradictions between two records; they are single
records that do not settle their own question.

1. **The 6 September session of T2 is unretrievable** (L14, `IH-003`) and its content is
   recorded as `NOT FOUND IN THIS SEARCH`, "not an absence" (L15, `IH-005`). Every one of
   the 84 unaccounted pages in §3 falls inside the window that session covers. The handoff
   itself offers the two readings — 42 pages built in that session, or the index counting
   routes the files do not (L475, `IH-251`) — and settles neither.
2. **"Verify done" items were never confirmed.** The handoff lists C-09, C-11, C-16 6.1,
   C-26, X-05 and X-15 as items whose completion it could not check (L623; L505, `IH-273`).
   The inventory does not close any of them. For C-11 (`brahmi.html`) and C-16 6.1 it shows
   pages whose titles and headings are consistent with the fix, which is not the fix. For
   C-09 and C-26 the fixes are below heading level and invisible to it. For X-05 and the
   `the-names.html` half of X-15 the named file is absent entirely, so there is nothing to
   check against.
3. **`the-names.html`** (L73, `IH-021`) is recorded as carrying a live self-contradiction in
   its h1, with VELI-02 listing it open and WORKLIST not mentioning it as fixed (L488,
   `IH-264`). No file of that name exists in the inventory. Whether it was renamed, merged
   or removed is unresolved; `naming-in-ancient-india.html` and `the-nine-enemies.html` are
   candidates on subject, neither on filename.
4. **Built-versus-built-and-INCOMPLETE.** Standing rule 12 (L595, `IH-045`) holds that "a
   search named as owed is a dependency; a page depending on it is INCOMPLETE, not built."
   Several pages in §1 and §3 rest on searches the handoff records as never run —
   `before-the-indus.html` on work item 33 (`IH-301`), `jatization.html` on the jāti-etymology
   verification (`IH-303`), `sanskritisation-of-place-names.html` and `the-other-half.html`
   on the excavation-coverage and Pataliputra searches (`IH-045`). By the handoff's own rule
   these are not "built" in the sense §1 uses. This document lists them as built because the
   inventory records the file; the distinction is the handoff's, and it stands.
5. **The two `.md` 404s** (L146, L382, `IH-052`, `IH-201`) cannot be checked: the inventory
   covers HTML at the repository root only (L3).
6. **Whether the site the inventory describes is the site the handoff describes.** The
   handoff records the platform at `intoveli.netlify.app`, a development URL (L408,
   `IH-216`), and records that no Git repository existed as of compilation — Tier 0 item 1,
   "open since 30 Aug… named in every file as the highest standing risk" (L435, L501). A
   `melakeela/site` repository now exists and was cloned for this reconciliation. Nothing in
   either document establishes that its `main` branch is what was deployed at
   `intoveli.netlify.app`, or that it is the same file set the handoff's page counts
   describe.

---

## 6 · What this document does not do

It does not propose what should be built, rank anything, or assess the quality, accuracy or
value of any page. It promotes no claim out of `INHERITED-UNVERIFIED`: the only retrieval
event it performed was of `SITE-INVENTORY.md` itself (`SRC-019`), which is evidence about a
description of the site, not about the site. Where a register claim is load-bearing for a
built page, the `claim_id` is noted so the dependency is visible; noting it does not verify
either the claim or the page.
