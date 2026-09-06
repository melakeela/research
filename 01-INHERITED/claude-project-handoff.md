# MELAKEELA / VEḶI · PROJECT HANDOFF FOR THE RESEARCH HEADQUARTERS
### Compiled 6 September 2026 from the five conversations in this project and the twelve project files dated 30 Aug – 1 Sep 2026.

---

## 0 · WHAT THIS IS, AND WHAT IT IS NOT

This is a structured transfer of the project's state — decisions, findings by status, corrections in the order they happened, files, concepts, dependencies, contradictions and open work — so that a later agent does not repeat reasoning that has already been rejected.

**It is not a verification pass.** No count in this document was re-run against `gret_scan.json`, the atlas HTML or any corpus during compilation. Every number below is attributed to the file or thread that reported it. Where two records disagree, both are shown and the disagreement is logged in §9. Under Rule 14 (counts come from data), nothing here upgrades a figure's status.

**Retrieval limits, stated so they are not mistaken for findings:**

- Five conversations exist in this project. Four were fully searchable. The fifth and longest — *"Retrieving previous conversation content"* (`6d35aeae…`, 30 Aug → 6 Sep) — was searchable through 2 September but its most recent session (updated 6 Sep 2026, the session immediately before this one) was **not retrievable** by the tools available. If the failures named in the Rules message (Para-Munda false-equivalence, Witzel source-dependency, Rigvedic stratification overreach, unexecuted searches, preflight-vs-verified) were articulated there in those words, that articulation is not quoted here. Each is instead reconstructed from the retrievable record in §3, with the reconstruction marked as such.
- Content of the redacted session is therefore a **NOT FOUND IN THIS SEARCH** condition, not an absence.
- Files created inside conversations (VELI-10 to VELI-13, the deck, `DECK_GAP_ANALYSIS.md`, `MELA_KEELA_INSTRUCTIONS.md`, `NAMING_LEDGER.md`, `VELI_INSTRUCTIONS.md`, the built HTML pages) live in those chats' output folders. **Only the twelve files listed in §7.0 are in this project's knowledge.** Anything else is on Enn's disk or in a chat, not here.

---

## 1 · STATUS VOCABULARY USED THROUGHOUT

| Tag | Meaning here |
|---|---|
| **OWNER DECISION** | Enn stated it, in writing, in a conversation. Binding until Enn changes it. Thread and date given. |
| **VERIFIED FINDING** | Machine-verified from a shipped artefact, or a primary text checked verbatim, or counted in the original language against a named corpus. The count itself was not re-run for this document. |
| **PROVISIONAL FINDING** | Rests on a named peer-reviewed source not independently re-run (VELI-03 `VERIFIED-SECONDARY` / VELI-09 `CITED`), or on a corpus run whose method carries a stated caveat. |
| **HYPOTHESIS** | Live, underdetermined; the burdens on each side are recorded. |
| **REJECTED** | Enn or the evidence rejected it. Do not re-argue it. |
| **SUPERSEDED** | A prior position replaced by a later one, with the replacement named. |
| **OPEN** | Unresolved. The specific uncertainty is named (date, reading, source access, etc.), per Rule 11. |
| **HELD** | A load-bearing source was not directly accessed (Rule 7). |
| **NOT FOUND IN THIS SEARCH** | Searched; not located; existence not settled (Rule 8). |
| **CLAUDE-ORIGIN** | The item exists only because a Claude thread produced it and no owner or external check has occurred. Flagged so the Rules message's instruction — do not defend a conclusion merely because an earlier thread produced it — can be applied. |

---

## 2 · THREAD MAP (chronological)

| # | Thread (title as saved) | Dates | What it did | Retrieval |
|---|---|---|---|---|
| T1 | **VELI - closed** (`0761d0e4…`) | ≤ 30 Aug → last touched 5 Sep | The original long build session: corpus scans, ~58 pages, landing, naming ledger, `VELI_INSTRUCTIONS.md`, `MANIFEST`/`RERUN` packaging, the INDUSVALLI deck gap-analysis, most of the substantive corrections in §3. 395 turns. | Searchable; read at the deck-corrections turn |
| T2 | **Retrieving previous conversation content** (`6d35aeae…`) | 30 Aug → 6 Sep | Founding pack (VELI-00–05), strategy dossier (VELI-06, merging former 06/07/08), then ~20 "batches" of Scite/Consensus-verified research and page builds (VELI-09), PENDING-RULES, WORKLIST, the anti-deflection law, source-integrity audits, external-review response. Page count grew 58 → 85. | Searchable to 2 Sep; final session (6 Sep) not retrievable |
| T3 | **Intoveli.netlify.app deployment status** (`d32156b4…`) | 31 Aug | Live-site check. Two `.md` 404s; atlas JS-rendered. | Full |
| T4 | **Current HTML capabilities** (`c610a9f6…`) | ≤ 4 Sep | Independent critical assessment of the live site; page-count correction (102 → 127); build plan (six engines, static-only, depth toggle, `lint.py`). | Full |
| T5 | **Child-centered learning through evidence discovery** (`54837714…`) | ≤ 5 Sep | VELI-10 (children's product "DIG"), VELI-11 (scholar map, funding taxonomy), VELI-12 (master plan), VELI-13 (Founding Partners Prospectus), MELAKEELA-VELI-DECK-v0.1 (16 slides); DMC eligibility correction. | Full |

**Reading order for a new agent:** VELI-00 → VELI-01 → PENDING-RULES → WORKLIST → VELI-03 → VELI-09 (§Q, §K, §X, §AB first) → this document §3 and §9. Then VELI-06 only for institutional questions.

---

## 3 · CORRECTION HISTORY — in the order it happened

Read this before reading any finding. Each entry gives: what was said, what corrected it, who corrected it, and the rule that came out of it. Entries are numbered in chronological order as far as the record allows; the T1 session spans many days and internal order within it is approximate.

### 3.1 · Corrections from the original build (T1)

**C-01 · "No caste word in the Vedas."** Claude's early formulation. Contradicted by the platform's own count: *varṇa* occurs 23 times in the Rigveda (VELI-03 §2, `gret_scan.json` record 0) and at 3.1 per 10,000 in the Taittirīya. **Rule (VELI-03):** never write that claim again. The correct finding is that *jāti* is absent from the Saṃhitās and Brāhmaṇas while *varṇa* is present.

**C-02 · Vedic word-total drift.** Three totals in circulation — 700,000 · 660,000 · 840,248 — for what may be different text sets. **Rule (VELI-03 §1, VELI-04 1.8):** no page carries a Vedic total until reconciled from `gret_scan.json`. Still OPEN.

**C-03 · The GRETIL Upaniṣad contamination.** Standard GRETIL Bṛhadāraṇyaka bundles Śaṅkara's 8th-century commentary: 85,467 words against ~17,091 of text. All frequency counts on that file were contaminated. Fixed by using Śatapatha kāṇḍa 14 as the commentary-free text (`bu_clean.txt`). **Rule:** primary-text-only versions for every Upaniṣad count; Chāndogya commentary-free version still NOT FOUND (VELI-03 §9).

**C-04 · Lemma false matches on the river page.** Vipāś reported at 52 and Rasā at 78; stem search was catching *vipaścít* and unrelated lemmas. Correct: **3 and 10**. Also found: Paruṣṇī (Ravi) and Asiknī (Chenab) are absent from the VedaWeb lemmatisation entirely — a gap in the data source, not the text. **Rule:** exact lemma forms; state data-source gaps on the page.

**C-05 · The Rigvedic stratification overreach** (the failure the Rules message names). Claude built the river page on Arnold metrical strata from `rv_tokens.tsv` and wrote *"the rivers of eastern Afghanistan — Kabul, Kurram, Gomal — are in the Archaic stratum… The corpus knows Afghanistan before it knows the Ganges."* Re-counting **by book** reversed it: Kubhā 2, Krumu 2, Gomatī 2, Suvāstu 1 — every occurrence in **Books 5, 8 or 10**, the late books, not the family books. Claude's own admission: *"strata and book order disagree, and I reported only the reading that suited the argument."* Enn's correction is recorded in memory and VELI-04 Part C (*"the oldest hymns know Afghan rivers" — contradicted by my own map page*). **Rules produced:** (a) metrical stratum and book order are two different chronological instruments; when they disagree, say so and privilege neither silently; (b) a directional claim built on one instrument alone is an overreach; (c) check every new claim against the platform's own pages first (Standing Order 6). The corrected picture on the page: *the Rigvedic world is the Indus and the Sarasvatī; everything else is a mention.* — Sindhu 204 · Sarasvatī ~75 · Gaṅgā 1 (Book 10). Those three counts are themselves still **NEEDS-CHECK** (lemma-verified re-run owed, VELI-03 §2).

**C-06 · "That reverses what I said last turn" on a published page.** Enn: that sentence, and any meta-commentary addressed to Enn or narrating Claude's process, must be nowhere on the site. **Rule (VELI-01 §3.8, principle 22):** no meta-commentary on published pages; corrections go in a corrections log, not in page copy.

**C-07 · *Varṇa* "means the colour of a dawn."** Claude led with the harmless sense. Enn: *varṇa* means colour, the social order is named after it, and the one human application in the Rigveda divides *ārya* from the people they fought. Recorded in VELI-04 Part C as the paradigm case of the failure mode. **Rule:** both halves in the same breath; the indictment first, nuance after, never as a replacement. The colour-count "done right" (how many of the 23 apply to humans, and of those how many are colour/skin) is still **OPEN** (WORKLIST 1.3; VELI-03 §2).

**C-08 · "Every demon is somebody's local enemy."** Omits that the composers are the incomers and the named enemies (Śambara, Pipru, Cumuri — names Sanskrit cannot parse) are the people already there, holding forts, grain, wives and sons. Landing corrected in T1; `the-killed.html` h1 corrected 1 Sep (T2). **Rule (anti-deflection law, PENDING-RULES):** state the direction plainly — intrusive vs indigenous — when the evidence supports it.

**C-09 · Kuyava as "bad barley."** The etymology in circulation. Collocation run: *kuyava* has **zero** co-occurrence with barley, field or cultivation in the Rigveda. DEDR 1762 *kuyavaṉ* "potter" is a live candidate Claude had wrongly foreclosed. Enn also challenged the dismissal of *campā/campai* for Śambara ("not not compelling") — status: lexical match without regular correspondences, not an etymology. **Rule (principle 16):** collocation evidence overrides etymological guesses. `the-names.html` h1 ("names that describe what they do to crops") is still listed as a live self-contradiction in VELI-02 §5 — **verify whether the 1 Sep fixes closed it**.

**C-10 · Phonotactic test for Dravidian substrate.** Claude used Sanskrit phonotactics to exclude Dravidian origins for enemy names; Enn pointed out Sanskrit nativisation destroys the test, and that initial *c-* does drop in Dravidian (DEDR 2529, *cintam ~ intam*). **Rule (principle 12):** phonotactic tests are invalid for substrate origin. The one negative result that survives is Pipru: no DEDR match from two independent directions.

**C-11 · Brāhmī "is not from brahmins."** Claude used the Buddhist/Jain attestation of the script's name to obscure that the word is morphologically the feminine of *brahman*. **Rule (anti-deflection law §3):** attestation ≠ derivation ≠ meaning; give all three when they diverge. `brahmi.html` fixed 1 Sep; the index-card-vs-page contradiction ("named after a woman in a Jain story") was still listed in VELI-02 §5 — **verify closed**.

**C-12 · The AHG ancestry inversion.** Preprint v1 of the relevant paper had all three clauses (highest in the South, higher among Dravidian speakers, highest in SC/ST/OBC) inverted relative to the published version. **Rule (principle 18, Standing Order 5):** version-pin every citation; cite the published paper; record that v1 was wrong. Vellalar AHG figure: **NOT OBTAINED — state no number** (VELI-03 §4).

**C-13 · Genetics from summaries.** Several genetics claims were made from a secondary summary and were wrong. **Rule (principle 19):** go to the paper and the supplementary tables.

**C-14 · Admixture dates as arrival dates.** Corrected to principle 11: admixture dates are lower bounds on arrival. VELI-03 §3 adds: movement dates must be tight and sourced (~1900–1500 BCE by admixture dating), never widened toward "slow diffusion."

**C-15 · "Indigenous" for enemy names.** Too strong. **Rule (principles 14–15):** *of undetermined origin* / *no accepted derivation*; "earliest attested as," never "originates in."

**C-16 · The deck-gap analysis, Part 3, applied doubt in one direction** (the asymmetric-skepticism correction, T1 turn 387–388). Enn's instruction, verbatim in substance: don't take the INDUSVALLI deck at face value; we already established more than it records; check every objection to our data for bias too; the deck is a starting point; most Claude-built pages still need a fine-toothed cross-check; publication does not stop, but every page will be gone through; lack of evidence can mean evidence was controlled or destroyed. Claude's Part 6 corrections:
- **6.1 Rakhigarhi is not one individual.** Claude had written "the sample is ONE individual, I6113." Narasimhan et al. (deck p.125) record eleven Indus-Periphery outliers from Gonur and Shahr-i-Sokhta forming a cline of which I6113 is part — **twelve individuals on a cline**, attested again a millennium later in Swat. Claude's caution *understated a well-supported finding*. Action: `steppe.html` and `endogamy-clock.html` must not say "one individual." **Verify done.**
- **6.2 Irula.** Deck p.23 records DNA overlap with the Irula; p.317 records Irula as a late branch from Tamil. The tension is evidence that language and ancestry move independently. Action: check exact wording in Shinde et al. 2019 before publishing — **HELD**.
- **6.3 Brahui — burden of proof inverted.** Claude presented Elfenbein's late-migration hypothesis as the correction to a "contested" claim. Late migration requires an undocumented ~1,500 km movement with no trace; the relict hypothesis requires only that a language island survived a surrounding shift, which is ordinary. Deck p.317 (Tulu–Brahui affinity) is what relict predicts. **Corrected status: both live; late-migration carries the heavier burden and has not discharged it.**
- **6.4 Witzel and Para-Munda.** See C-17.
- **6.5 The standing rule:** for every objection ask what it requires to be true, who holds it and at what cost, whether it is evidence or absence-of-evidence, and whether the corpus needed to settle it has been assembled and funded. Written into `MELA_KEELA_INSTRUCTIONS.md` as B.11 (symmetry of skepticism), B.12 (controlled absence — a gap permits agnosticism, not invention), B.13 (the deck is a question list), B.14 (page provenance stated plainly).

**C-17 · Para-Munda — the false-equivalence problem, both directions** (reconstructed; the 6 Sep articulation was not retrievable). The retrievable record shows two opposite failures around the same hypothesis:
- *First failure (T1, early):* Claude presented Witzel's Para-Munda as "the honest counter you should know about," alongside Dravidian, as if two hypotheses of equal standing — while noting Para-Munda is "a reconstruction of an unattested language." Under Rule 5 (space follows evidence) an attested family and an unattested hypothetical donor are not automatically equivalent, and under Rule 4 (chronology and geography are gates) Munda's attested range is eastern and central India; a Munda-related Indus language must first pass the geography gate.
- *Second failure (T1, Part 6.4):* Claude then argued the asymmetry ("Para-Munda requires a population movement no less speculative than the one Brahui is faulted for… one is career-safe, the other coded as political"). That is a claim about the *citation record*, and it was proposed as a page — *Who gets to be speculative* — with the citation history as the evidence. **No citation history was assembled.** The page concept therefore rests on an unexecuted search (see C-25).
- *What Claude refused, correctly:* Enn asked whether Witzel's funding or motives explain the position. Claude declined to speculate — *"I have no evidence about his funding or motives, and inventing some would wreck the credibility of everything else."* Later batch-5 rule (VELI-09 §J): judge sources by venue, method, reception and declared funding — never by author identity or perceived alignment. **Both stand.** Rule 6 (no authority substitution) and the batch-6 rule (verify funding; where unverified, say so) apply to Witzel exactly as to Sequeira and Pathak.
- **Correct handling going forward:** Para-Munda earns a brief historical note with its evidential burden stated (unattested; prefix-segmentation disputed; geographic gate unmet in the northwest), not equal analytical space with Dravidian; Dravidian-as-Indus-language is the strongest single contender and is **not proven** (VELI-09 §B); Masica's "Language X" is Indus/NW-specific (PENDING-RULE 15). *Prefixing morphology in early Indo-Aryan is a real observation requiring explanation* and must not be dismissed because its best-known proponent is disliked.

**C-18 · Witzel source dependency** (reconstructed). Every Witzel position on the platform is second-hand:
- Para-Munda as the Indus language — via the INDUSVALLI deck, p.294 (a slide quoting Witzel).
- "Witzel now keeps the question open" — cited as *Witzel 2019, via Mukhopadhyay 2021* (VELI-09 §B).
- Substrate word-lists on `who-had-it-first.html` — footer reads *"after Kuiper, Aryans in the Rigveda (1991), and Witzel's substrate papers, with Mayrhofer's etymological markings"* — no locator, no direct access recorded.
- Farmer–Sproat–Witzel 2004 and Rao et al. 2009 — named, not accessed.
**Under Rule 7 every Witzel-dependent claim is HELD** until the primary papers (Witzel 1999 *Substrate Languages in Old Indo-Aryan*; Witzel 2019) are read directly. The same applies to Kuiper 1991 and Mayrhofer (EWAia), which carry the substrate lists.

**C-19 · Greek chronology and the shared Achaemenid state** (T1, `two-classical-languages.html`). Enn's corrections: vowel-writing was not a Greek invention (Linear B syllabary, Ugaritic, Phrygian contemporaneous); the shared Achaemenid state (Ionia from 547/546, Gandhāra and Hindush from c. 518; Scylax c. 515; Indian troops at Plataea 480–479) must be on the page; Greek philosophy does not begin "200 years after" writing returns. Claude accepted the first two; on the arithmetic held at ~140 years (attested writing c. 740 BCE, Thales c. 600) while conceding the underlying point that Greek literature begins at the moment of the Near Eastern import. **Status: page corrected; Enn's "within 50 years" figure not adopted; the 140-year figure is Claude's — CLAUDE-ORIGIN, check against a named chronology.** Enn's broader request — coverage of how Europe claimed foreign concepts as Greek, in chronological order, and of the Gāndhārī scrolls as the oldest manuscripts — was partially built; **treat as OPEN content**.

**C-20 · Sadhguru / Nithyananda.** Enn's brief named them for the godman-economy page. Claude did not name them with allegations — only the convicted (Asaram, Ram Rahim) as court record. **Rule (VELI-09 §S):** anti-deflection *and* anti-defamation together; living figures only on the record.

**C-21 · The unrequested site zip** (T2). Claude bundled deployment config Enn had not asked for. **Owner instruction: files only on request.**

**C-22 · Cross-link from memory.** A link to `one-buys-immortality.html` (does not exist; real page `the-firms.html`). **Rule:** run the cross-link check before every ship; never reference a page from memory.

### 3.2 · Corrections from the founding-pack and research batches (T2)

**C-23 · Container reset vs context compaction.** Claude assumed the working container was wiped and 78 files lost. What happened was a context compaction. Files intact, hash-verified. Written into VELI-00 with explicit language. **Do not repeat.**

**C-24 · Institutional "vibes" instead of checking** (VELI-09 §J → §K). Batch 5 labelled Sequeira Koraga 2024 a preprint and vouched for Pathak as "not Hindutva" without checking. Batch 6: Sequeira is peer-reviewed (*EJHG*, Nature Portfolio, 24 Oct 2025, DOI 10.1038/s41431-025-01963-1; co-author van Driem); its funding is **UNVERIFIED**. Pathak (L1-M22, *iScience*) and Narayan (*Mother Tongue*) remain **UNVERIFIED — do not defend.** **Rule:** verify venue, peer-review status, reception, co-authors and funding before vouching; where funding is unverified, say so.

**C-25 · The unexecuted-search problem** (reconstructed as a pattern from the record). Searches were repeatedly named as owed, then pages built without them. Recorded instances:
- Ali et al. 2014 team standing — "search owed" (VELI-09 §B, §H); never run.
- East-vs-south excavation-coverage and Pataliputra→Patna toponym — "still unrun" (T2, 31 Aug).
- Śramaṇa-roots search — "still unrun."
- Damdama/Mahadaha absolute dates; Indus death-rites ↔ megalith ↔ tribal correlation; ashmound global uniqueness; ASI vs AASI precision for the deep south — "searches owed" (VELI-09 §H, §I); PENDING-RULE 19 says these must be run *before* the contested deep-history claims are published. `before-the-indus.html` was built and later had its headline downgraded (C-31).
- r/l, v/y eastern-Prakrit substrate — "targeted search owed."
- The jāti-etymology Scite verification (PENDING-RULES 4) — "verify before publishing"; `jatization.html` built.
- The Mahābhārata varṇa-mobility lead — sourced only from Quora and wisdomlib; correctly flagged **do not assert** (VELI-09 §P).
- Reich quotes/timeline for "Academia as a battlefield" — "verify before building."
- Kerdoncuff et al. 2024 publication status — "check."
- The Witzel citation-history that would evidence *Who gets to be speculative* — never assembled.
**Rule (this document, from Rule 8 and Rule 13):** a search named as owed is a dependency; a page whose load-bearing claim depends on it is INCOMPLETE, not built. Record each as NOT FOUND IN THIS SEARCH until run.

**C-26 · Audit after build → audit before build** (VELI-09 §Q). Enn caught that Claude built the Ledger (credibility feature) and then cited caste-page sources without auditing them. Result: Kabir Babu 2016 (*Caderno de Relações Internacionais*, off-field, no findable footprint), Choudhury 2021 (MDPI preprint) and Kumar & Choudhury 2020 (*Cogent*) were visibly carrying claims that Aktor, Davis, Olivelle, Béteille and the corpus actually support. **Rule:** audit-first workflow; strong claims rest on strong sources; weak sources demoted to corroboration or dropped. Re-attribution on `birth-was-not-always-destiny.html` and `jatization.html` was "owed next pass" — **verify done**.

**C-27 · Regex scan flags are not findings** (VELI-09 §X). The older-pages audit flagged 33 "NO-SRC" pages and several "overclaim" pages; on reading, nearly all were false positives (corpus-anchored pages; quotations of primary texts). **Rule:** read the flag in context; the corpus count is the platform's strongest evidence type, not a citation gap.

**C-28 · Running page tally drifted** (VELI-09 §T, §U). Claude's count drifted +1; corrected to `ls`-verified only. **Rule:** report `ls` counts, never a running tally.

**C-29 · "Verified · scite" is a badge, not a record** (VELI-09 §AB, external review). Replaced on three pages with a `.cite` block: full bibliography · DOI link · primary/secondary · locus · method · *supports* · *does not support*. **Retrofit across the other ~80 pages is owed.**

**C-30 · Interest disclosure** (Enn's catch, §AB). Patwardhan cited on `the-medicine-question.html` is National Research Professor-AYUSH and ministry adviser — credible and writing from within the project of legitimising Ayurveda. Flagged, not presented as disinterested. **Rule 6 applied to a living author.**

**C-31 · Six headline overstatements, Claude's own** (§AB): `before-the-indus` ("20,000 years older than the Vedas" → "a proposed Palaeolithic shrine" with evidence panel; no directly datable material at the feature) · `the-vedda` ("here first… called a dialect until it died" → qualified) · `one-verse` ("caste system appears exactly once" → "the explicit fourfold varṇa scheme appears together in one verse") · `what-travelled` ×2 (Bali developed hereditary status with Sanskrit categories; "much of contemporary practice is not Vedic in form") · `coverage` ("every gap is a funding decision" → "many gaps follow the money"). **Pattern:** the headline overclaimed in the platform's own direction. Anti-deflection law §5 and Rule 16 both apply.

**C-32 · The packaging bug.** `RIGVEDA_corpus_analysis.md` and `MELUHHA_TO_KEEZHADI_synthesis.md` were referenced by `enter.html` and absent from the zip (only `*.html` zipped). Fixed → 95 files. **This is the same defect T3 saw live as two 404s** — the fix in the zip must be confirmed on the deployed site.

**C-33 · Melakeela-as-primary would reverse PENDING-RULE 18.** Claude stopped and named the settled decision before building (Standing Order 1). Enn held it open (§4, D-14).

### 3.3 · Corrections from the assessment and planning threads (T3–T5)

**C-34 · Claude accepted the site's own page count** (T4). Report used the Research Index's "102 content pages." Enn challenged; Claude counted the entries: 25 + 16 + 29 + 20 + 18 + 19 = **127** (~135 including excluded routes and `.md` files). Claude named it as the same error it had just criticised in the site. Effort estimate revised to 22–36 person-months; disclosure share corrected to 44% (56 of ~127). **Rule 14 applies to Claude's own reports.**

**C-35 · The Danino stage is wrong** (T4, on the live site). The page folds the 11 March 2026 Supreme Court direction concerning Michel Danino into a migration-denial narrative; per the assessment it concerned an NCERT Class 8 judiciary chapter and was modified in late May 2026. **HELD** — the order and the modification must be read directly before the page is corrected; the assessment's characterisation is itself secondary.

**C-36 · "The Rigveda contains no seafaring"** (T4, `rakhigarhi` page) vs the site's own corpus file recording *naú-* (boat) at n = 40. One of the two is wrong; **resolve from `rv_tokens.tsv`**.

**C-37 · Atlas count contradiction on the live site** (T4): 140 on Enter · 158 on Explore · 175 in the page title. See §9 for the full six-way disagreement across documents.

**C-38 · Drafting residue in a published document** (T4). `RIGVEDA_corpus_analysis.md` addresses a "you." Same class as C-06.

**C-39 · DMC eligibility** (T5). VELI-12 anchored Year 1 on a 1 December 2026 Digital Museums Canada application. A ChatGPT response caught that DMC requires the applicant to have existed for at least one year with current legal status at submission. A September 2026 incorporation is ineligible for December 2026. **Revised: DMC December 2027; 2026–27 is institution-building and prototype year.** DMC's eligibility-review deadline (10 Nov, response 17 Nov) allows the 2027 status question to be settled a year early. Recorded in VELI-13 Part B.

**C-40 · The prospectus inventory conflict** (T5). Enn's visual-concept document cites *140 sites, 299 dated object-windows, 25 localised texts, seven trade routes*; VELI-03 says *194 site records, 315 class-windows*. VELI-13 used VELI-03. **Resolve which is current from the atlas data before either number is printed anywhere.**

**C-41 · Sentences banned from the prospectus** (VELI-13 B4): "world-leading," "revolutionary," any usage projection, any health/wellbeing benefit, any Keeladi claim beyond a specific inscribed mark, any partner named before written yes, any number not derivable from the repository. **Note the memory summary for this project uses "world-leading" — that is internal ambition language, not external copy.**

---

## 4 · OWNER DECISIONS (Enn, in writing)

Numbered D-xx. Source thread and date given. These stand until Enn changes them.

| # | Decision | Where | Status |
|---|---|---|---|
| D-01 | Name: **வெளி · Veḷi**, retroflex ḷ, romanised *veli*. Telugu excommunication sense is a feature. | T1; VELI-01 §3.1 | SETTLED |
| D-02 | Posture: "a museum that shows its working," explicitly **not an institute**. | T1; VELI-01 §3.2 | SETTLED; reconciled with a parent body (VELI-06 A1) |
| D-03 | Page frame: every page is MADE VISIBLE · KEPT DARK · PUT OUTSIDE, or it does not belong. | VELI-01 §3.3 | SETTLED |
| D-04 | Voice/design: dark ground, *veḷippaṭu* (content resolving out of blur), colour encodes argument, grey `#5f6f7a` = NO DATA always. | VELI-01 §3.4 | SETTLED |
| D-05 | Immersion over text; "all text doesn't tell enough of a story"; "I like the darkness." | VELI-01 §3.5 | SETTLED |
| D-06 | The consumer/store arm is a separate property on a separate domain. `dravids.com` flagged, not rejected. | VELI-01 §3.7 | SETTLED |
| D-07 | Conduct: no meta-commentary on pages; no hedging findings the evidence supports; check sources rather than flag that you didn't; test rather than defend. | VELI-01 §3.8 | SETTLED |
| D-08 | The position (VELI-01 §2, §2.1): Vedic complex arrived; attacked settled people; varṇa = colour; caste apparatus built afterwards; brahmanism ≠ Vedism ≠ practice; śramaṇa opposed brahmanism. Enn's frame: śramaṇa is the pre-Vedic belief complex; "Hindu in essence, not Brahmin"; brahmanism is the thing that was foreign. **This is the frame, not necessarily the copy.** | T1; VELI-01 §2 | SETTLED as frame. Enn declined to keep debating Indus–śramaṇa continuity: **do not reopen.** How openly stated in copy: OPEN (Q-04) |
| D-09 | The 22 research principles (VELI-01 §4). | T1 | SETTLED |
| D-10 | The anti-deflection law and the northern-bias rule ("THIS IS HUGE"): northern priority is an artefact of excavation density and publication politics; never present as settled. | T2, 1 Sep; PENDING-RULES | SETTLED (hard rule) |
| D-11 | **Build all the pages first, then finalise the look.** Do not restyle now; keep the current Veḷi page system for new pages. | T2, 1 Sep; PENDING-RULES session note | SETTLED |
| D-12 | Files only on request (no unrequested zips). | T2 | SETTLED |
| D-13 | The deck (INDUSVALLI.pdf) is a starting point, not a source; platform pages built by Claude need a full cross-check one day; publication does not stop meanwhile. | T1 turn 387 | SETTLED |
| D-14 | **Melakeela-vs-Veḷi positioning is NOT finalised.** `melakeela.com` is owned. "Melakeela = magazine, Veḷi = institute behind it" is a live option, not adopted; it would supersede PENDING-RULE 18 (Melakeela as perspective mode). Landing page stays as-is. | T2, 1 Sep | **OPEN — this is D1 in the T5 files** |
| D-15 | No 12-page thesis; this is a platform; keep building the archive. | WORKLIST 4.5 | SETTLED |
| D-16 | Living figures: only the convicted, only the record (accepted Claude's handling). | T2 §S | SETTLED by acquiescence |
| D-17 | Source-audit before build; judge sources by method, venue, reception, funding — never by author identity. | T2 §J, §Q | SETTLED |
| D-18 | Enn acts as product and technical lead (T4: "Act as the product and technical lead" was the instruction to Claude; memory records Enn operating in that role). | T4 | Role framing |
| D-19 | Research is at synthesis stage, not foundations; the main gap is external adversarial contact from independent specialists. | T1 | SETTLED |
| D-20 | Enn's field observations (Irula community did not know Rakhigarhi referenced them; Tamil practice) are labelled observation and override secondary sources on Tamil cultural practice. | VELI-03 §8 | SETTLED |

**Proposed by Claude, NOT adopted by Enn (do not treat as decisions):** PENDING-RULES 1–19 in their entirety (page-size rule, emphasis rule, name-the-term rule, Meluhha-as-question, south-up atlas default, Pataliputra test case, two-mode brand, material-culture design system, three depths, five honesty tiers, "A Drop of Water" MVP, collections ingestion layer, four method rules 14–17, the three-word naming system, Before-the-Indus section); VELI-06 C4 decisions 1–8 (identity, brand, domains, "Where we stand" page, NFP incorporation, licensing, MVP §21, §20 deferral); the Cinduism overrule (VELI-06 A9 — *flagged for Enn's explicit ruling, not given*); VELI-06 C8 items 1–7; the T4 architecture (six engines, static-only, depth toggle, `kid_safe=false`, `lint.py`); the T5 nine-role prospectus and funding stack; "Veḷi is the institution and ledger, Melakeela is the door" (T5's own stated assumption, explicitly not adopted).

---

## 5 · FINDINGS BY STATUS

Counts are as reported by the named file. None were re-run for this document.

### 5.1 · VERIFIED FINDINGS (machine-verified or primary-text)

| # | Finding | Corpus / locus | Reported by | Note |
|---|---|---|---|---|
| V-01 | GRETIL register scan: **480 texts / 17,934,563 words** | `gret_scan.json` | VELI-00, VELI-03 | `RERUN.md` states 17,919,338 — 15,225-word discrepancy; JSON wins; RERUN must be corrected (still open) |
| V-02 | *Jāti* = **0** in Vedic Saṃhitās + Brāhmaṇas (840,248 words) | `gret_scan.json` | VELI-03 §2 | Raw string count. **See contradiction X-06** (VELI-09 §V refers to "236 jāti in Śatapatha" as substring noise) — the covered text set must be stated |
| V-03 | *Varṇa* = **23** in the Rigveda (180,196 words) | `gret_scan.json` record 0 | VELI-03 | Human-applied split NEEDS-CHECK |
| V-04 | Rigveda: *śūdra* 1 · *dvija* 7 · *caṇḍāla* 0 · *sapiṇḍa* 0 · *mleccha* 0 · *brāhmaṇaḥ* 0 | Rigveda | VELI-03 | |
| V-05 | *Jāti* present in every other Sanskrit section of the 480 | `gret_scan.json` | VELI-03 | Raw counts per 10,000 must be labelled pre-disambiguation |
| V-06 | Mahābhārata 921,642 words; *śūdra* in Anuśāsana at 100× Droṇa; caste vocabulary concentrated in Śānti and Anuśāsana | MBh parallel text | VELI-03; T1 | Converges with Sukthankar's manuscript dating (independent method) |
| V-07 | GRETIL BU = 85,467 words with Śaṅkara vs ~17,091 text | GRETIL vs `bu_clean.txt` | VELI-03 | The contamination finding |
| V-08 | Tirukkuṟaḷ: 1,330 couplets; zero *cāti*, zero *vētam* | `kural_ta.txt` | VELI-03; MANIFEST | First Tamil corpus |
| V-09 | Vipāś 3 · Rasā 10 (not 52 · 78) | `rv_tokens.tsv` | T1; VELI-03 | Paruṣṇī and Asiknī absent from the lemmatisation |
| V-10 | Afghan rivers Kubhā 2 · Krumu 2 · Gomatī 2 · Suvāstu 1, all in Books 5/8/10 | `rv_tokens.tsv` | T1 | The C-05 correction |
| V-11 | Pipru ↔ Ṛjiśvan at 639× expected co-occurrence; *kuyava* zero with barley/field/cultivation | `colloc.py` | VELI-03 | |
| V-12 | Rudra's strongest collocate is medicine; Dasyu and Dāsa structurally different; Paṇi economic not ethnic | `colloc.py` | VELI-03 | |
| V-13 | Taittirīya Saṃhitā whole-token counts: brāhmaṇa 84 · varṇa 34 · rājanya 27 · śūdra 9 · vaiśya 8 · kṣatriya 6 · **caṇḍāla 0**; fourfold ranked set co-occurs at only **TS 2.5.10.1 and TS 6.2.5.3**, both ritual-assignment contexts | `taittiriya.txt` (163,264 tokens) | VELI-09 §V | Śatapatha not published as counts (unspaced encoding) except caṇḍāla-zero. VELI-03 gives TS as "166,000 words" — token/word basis differs (X-07) |
| V-14 | ŚB 14 (BU) vs ChU 5.10.7 varṇa-womb parallel: the caste application is present in one recension and not the other — an accretion by **inference** from parallel-text difference | `bu_clean.txt`; ChU verified across concordant web sources | VELI-09 §O, §P, §AB | The "accretion" label is INFERENCE and the page says so |
| V-15 | ŚB 1.7.4.3–6 (Rudra shoots Prajāpati; Bhaga, Pūṣan epithets); ŚB 1.4.1 (fire carried east; brahmins had not crossed the Sadānīrā) | primary | VELI-03 §6 | |
| V-16 | Griffith renders RV 1.126.6–7 and 10.61.5–7 into Latin; omits 10.86.16–17 | primary | VELI-03 §6 | Systematic check of other omissions owed |
| V-17 | Manu 10.22 (Licchavi, Draviḍa in vrātya list) and 10.26 (Sūta, Māgadha, Vaidehaka as pratilomas) | primary via synthesis §22 | VELI-03 §6 | "Not yet on any page" as of 30 Aug — check whether built since |
| V-18 | Nakṣatra list TS 4.4.10; Rudra assigned Ārdrā | primary | VELI-03 | |
| V-19 | Aśokan inscriptions do not name their own script; the Lalitavistara (64) and Jain (18) lists postdate Aśoka by ~500 years | primary lists via secondary | VELI-03 §5 | "Brāhmī" is a retroactive label; "Tamil-Brāhmī" is modern |
| V-20 | Sanskrit lacks ḻ ṟ ṉ | linguistic fact | VELI-03 | Tamil-Brāhmī invented letters Sanskrit's script did not need |
| V-21 | Live site: Research Index lists 127 entries under a header claiming 102 | counted by Claude, T4 | T4 | |
| V-22 | Atlas structure: 194 site records · 315 class-windows · 14 classes · **54 of 199 site-class rows dated from excavation reports, 145 `assumed`** | parsed from `artifact-atlas.html` | VELI-02 §6 | Site-count disagreement across documents — X-01 |
| V-23 | 78 shipped files, SHA-256 verified (79 with `rv_tokens.tsv`) | MANIFEST | VELI-00 | MANIFEST has two internal arithmetic errors (VELI-06 C1.4) |
| V-24 | Gāyatrī = RV 3.62.10, in Maṇḍala 3, whose ṛṣi is Viśvāmitra | standard | VELI-09 §T | The kṣatriya→brahmarṣi narrative is later epic/Purāṇic (Pargiter dated) — kept separate on the page |
| V-25 | Kali Yuga epoch (17–18 Feb 3102 BCE) is back-calculated; planets not in conjunction | Sen 1987; Shukla 1987 (IAU) | VELI-09 §W | Science credited; no deceit claimed; authorship of yuga scheme debated |

### 5.2 · PROVISIONAL FINDINGS (named source, not independently re-run, or corpus with caveat)

| # | Finding | Source as recorded | Where | Caveat |
|---|---|---|---|---|
| P-01 | Indus Periphery Cline ~45–82% Iranian-farmer-related, ~11–50% AASI; "Iranian-related" ≠ from Iran | Narasimhan et al. 2019 | VELI-03 §4 | Version-pin |
| P-02 | Rakhigarhi I6113 lacks Steppe marker; sits on a cline with eleven Indus-Periphery outliers; same profile in post-IVC Swat | Narasimhan 2019 (via deck p.125, p.32); Shinde 2019 | T1 Part 6 | Shinde 2019 wording HELD |
| P-03 | Steppe_MLBA ≈ ⅔ Yamnaya-related, ⅓ European-farmer-related; route loops west | Narasimhan 2019 | VELI-03 | |
| P-04 | AHG-related ancestry highest in South, among Dravidian speakers, in SC/ST/OBC | published version only | VELI-03 | v1 inverted |
| P-05 | Keeladi sequence (5,500 artefacts → transfer → 982-page report Jan 2023 → May 2025 rework request → 114-page evaluation) | secondary | VELI-03 §3 | Pin each step |
| P-06 | Ghaggar basin beginnings c. 5500 BCE; Bhirrana ~9000 BP | secondary | VELI-03 | CONTESTED; name the contest |
| P-07 | Eastern Indo-Aryan structurally closer to Munda → language shift not replacement | Peterson 2017b, 2022; Ivani 2020 | VELI-09 §B | |
| P-08 | Aśokan edicts = Middle Indo-Aryan; Prakrits vernacular, Sanskrit liturgical | Cathcart 2020; Hutchinson 2026 | VELI-09 §B | |
| P-09 | Proto-Dravidian ≈ 4,500 years old | Kolipakam, Jordan & Dunn 2018 | VELI-09 §B | STRONG venue |
| P-10 | Dravidian the strongest single Indus-language contender, **not proven**; *pīlu* thread | Mukhopadhyay 2021; Krishnamurti 2003; Parpola 1994 | VELI-09 §B | Witzel-open claim HELD (C-18) |
| P-11 | Munda language arrives ~2000 BCE; O-M95 ancestry ancient in India; male-biased incoming | Rau 2019; Kumar 2007; Chaubey 2010; Tätte 2018 | VELI-09 §C | Ancestry ≠ language rule |
| P-12 | Dharmaśāstra intent to control mobility; caste produced by legal rules; differential penalties | Aktor 2018; Davis 2020/2022/2024 | VELI-09 §A | STRONG sources; Babu/MDPI demoted (C-26) |
| P-13 | Puruṣa-sūkta late interpolation | Alanzi 2022; Kumar & Choudhury 2021; Ambedkar | VELI-09 §A | Mixed-strength sources |
| P-14 | Elamo-Dravidian convergence rests on McAlpin 1974 + Pathak 2024, not Sequeira/Narayan | VELI-09 §J, §K | | Pathak funding UNVERIFIED |
| P-15 | Sequeira Koraga 2024/25 peer-reviewed (*EJHG*); funding unknown | VELI-09 §K | | Do not guess funding |
| P-16 | Baghor I proposed Palaeolithic shrine, contextual dating c. 9000–8000 BCE, no directly datable material at feature | Kenoyer et al. 1983 | VELI-09 §E, §AB | Headline downgraded C-31 |
| P-17 | Mesolithic Ganges cemeteries (Damdama, Mahadaha) with solar-aligned graves | Chattopadhyaya 1996 | VELI-09 §E | Absolute dates OPEN |
| P-18 | Ashmounds ~3000 BCE, S Deccan; Maski; Kupgal | Fuller 2007; Bauer 2015; Boivin 2004 | VELI-09 §F, §N | Global uniqueness OPEN |
| P-19 | Gotra genetics: Y-chromosome village-specific (79%), mtDNA diverse → patrilocality; endogamous stratification 4–6 kya predates varṇa; ~81% autochthonous Y-lineages in Tamil Nadu | Pemberton 2012; ArunKumar 2012 (+2013 correction) | VELI-09 §Y | Pemberton: one Gujarati gol, not generalisable |
| P-20 | Vedda: deep Indian-tribal genetic link, drift, isolation; language lost within living memory | Welikala 2024; Weerasekara 2020 | VELI-09 §J, §AB | "First" and language classification NOT supported — page qualified |
| P-21 | Bronkhorst *Greater Magadha* 2007 | | VELI-03; VELI-09 §M | CONTESTED, respected; now on `the-eastern-tradition.html` |
| P-22 | xwēdōdah praised in Zoroastrian Iran | secondary | VELI-03 | Breaks "IE kinship inherently exogamous" |
| P-23 | Linear Elamite reading (Desset 2022) contains no Meluhha, no Indus reference | | VELI-03 §5 | CONTESTED decipherment; the negative matters |
| P-24 | Achaemenid: Ionia 547/546; Gandhāra/Hindush c. 518; Scylax c. 515; Indian contingents 480–479 (Hdt 7.65, 9.31) | Herodotus; royal inscriptions | T1 | Herodotus cited by locus; inscriptions not by locus |
| P-25 | DMC requires one year of legal existence at submission | DMC guidelines via web search, T5 | T5; VELI-13 B | Guidelines for the 2027 cycle to be re-verified in autumn 2027 |
| P-26 | Live-site Danino page mischaracterises the March 2026 order | T4 web search | T4 | HELD until order read (C-35) |

### 5.3 · HYPOTHESES (live; burdens recorded)

| # | Hypothesis | For | Against / burden | Standing |
|---|---|---|---|---|
| H-01 | Brahui/Kurukh/Malto are a relict distribution (early Dravidian in the northwest) | Kuiper, Southworth, Krishnamurti place early Dravidian in NW; Tulu–Brahui affinity (deck p.317); language islands are ordinary | Elfenbein: c. 1000 CE migration — requires undocumented 1,500 km movement with no trace | Both live; late-migration carries the heavier undischarged burden (C-16 6.3) |
| H-02 | The Indus language was Dravidian | *pīlu* loan; aDNA continuity to modern South Indians; Krishnamurti, Parpola | Script undeciphered; Masica "Language X"; no bilingual | Strongest single contender, NOT proven. Public copy stays here |
| H-03 | Para-Munda / prefixing substrate as the Indus or earliest Rigvedic substrate | Prefixing morphology in early Indo-Aryan is a real observation | Unattested reconstruction; disputed ka-/ki-/ku- segmentation; Munda attested only east/central — geography gate unmet in NW; proponent reportedly now keeps question open (HELD) | Brief historical note, not equal space (C-17). All Witzel claims HELD (C-18) |
| H-04 | Post-urban Indus settlement moved east tracking a weakening monsoon | Correlation | Causation undocumented; no single cause is settled for the decline (VELI-03 §3 debrahminize note) | INFERENCE, labelled |
| H-05 | The yāḻ was abandoned because a harp string cannot bend (gamaka) | Mechanism; Burmese saung-gauk as control | Nobody wrote down why | INFERENCE, labelled |
| H-06 | Steppe movement linked to 2nd-millennium aridization | Widely held | Unproven | INFERENCE |
| H-07 | Śramaṇa traditions represent pre-Vedic indigenous belief | Aśokan *samana/bamhana* pairing; Bronkhorst's Greater Magadha; owner frame D-08 | Indus–śramaṇa continuity specifically is not demonstrable; Enn instructed it not be re-litigated | Frame, not copy. Public copy: śramaṇa opposed *brahmanism*, not "Hinduism" (WORKLIST 2.1) |
| H-08 | Mahadevan: megalithic graffiti continue Indus signs | Sign continuities | Graffiti may not be writing; critics to be named | CONTESTED; cover as claim |
| H-09 | Dravidian presence across much of India before ~1500 BCE | Ali et al. 2014 (genetics) repeating a linguistic date | Cite the linguists, not the geneticists (PENDING-RULE 16); Ali team standing search never run | PROVISIONAL at best; source-discipline gap |
| H-10 | "Who gets to be speculative" — Para-Munda and Dravidian continuity are held to different evidential standards in the citation record | Plausible; T1 Part 6.4 | **No citation history assembled**; would need a bibliometric method, not an assertion | Unexecuted (C-25); page must not be built until the record is compiled |
| H-11 | Varṇa mobility in early texts (śūdra upanayana; "conduct not birth") | Quora/wisdomlib only | No primary or peer-reviewed source located | Do not assert (VELI-09 §P) |
| H-12 | Elamo-Dravidian relationship | McAlpin 1974 (*Language*); Pathak 2024 | Respected-but-contested; Pathak funding unverified; Narayan fringe-adjacent | Live; `the-deep-root.html` marks sources |

### 5.4 · REJECTED

| # | Rejected item | By | Replacement |
|---|---|---|---|
| R-01 | "No caste word in the Vedas" | The count | *Varṇa* present; *jāti* absent |
| R-02 | "The corpus knows Afghanistan before it knows the Ganges" (Archaic-stratum reading) | By-book count | Afghan rivers in Books 5/8/10; the Rigvedic world is Indus + Sarasvatī |
| R-03 | *Varṇa* as "the colour of a dawn" (as the lead) | Enn | Colour; social order named after it; one adversarial human use |
| R-04 | "Every demon is somebody's local enemy" (direction omitted) | Enn | Incomers attacked settled locals |
| R-05 | "Brāhmī is not from brahmins" | Enn | Derivation from *brahman*; attestation Buddhist/Jain — both stated |
| R-06 | Kuyava = "bad barley" | Collocation | Zero co-occurrence with barley; *kuyavaṉ* potter is a live candidate |
| R-07 | Phonotactic exclusion of Dravidian origins for enemy names | Enn (nativisation; DEDR 2529) | Test invalid |
| R-08 | "Indigenous" for enemy names | Enn | "of undetermined origin" |
| R-09 | "The sample is ONE individual (I6113)" | Deck p.125 / Narasimhan | Twelve on a cline |
| R-10 | Brahui late-migration presented as the correction | T1 Part 6.3 | Both live; burden on migration |
| R-11 | Speculation about Witzel's funding/motives | Claude, upheld by batch-5 rule | Method, venue, reception, declared funding only |
| R-12 | Pataliputra as a Dravidian counter-civilisation | PENDING-RULE 7 test case | Mauryan Gangetic capital; its platform story is coverage/archive-bias |
| R-13 | "Dravidian" / "undetermined" as positive labels for pre-attestation populations | PENDING-RULE 14 | "of unknown language," either direction |
| R-14 | Transplanting Masica's "Language X" to South India / Sri Lanka / Ganges | PENDING-RULE 15 | Indus/NW-specific |
| R-15 | "Indu Valley Institute" as parent name; `indusveli.com` as front door | VELI-01 §5; VELI-06 | Continuity claim welded into a name |
| R-16 | "Cinduism" as institution name | VELI-06 A9 (Claude overrule, **awaiting Enn's ruling**) | Project kept as "How a Religion Was Assembled" |
| R-17 | Melakeela as a separate consumer brand | PENDING-RULE 8/18 | Mode inside Veḷi — itself now held open by D-14 |
| R-18 | The 12-page thesis framing | Enn (WORKLIST 4.5) | Platform |
| R-19 | Six headline overstatements (C-31) | External review, Claude | Qualified headlines |
| R-20 | Babu 2016 / MDPI preprint / Cogent as visible authority for central caste claims | Enn, batch 11 | Aktor, Davis, Olivelle, Béteille, corpus |
| R-21 | "verified · scite" badge as a verification record | External review | `.cite` block with DOI, locus, supports/does-not-support |
| R-22 | Naming Sadhguru/Nithyananda with allegations | Claude, accepted | Convicted only, court record |
| R-23 | "Contested" as a verdict | Enn, T1 | Name who, from where, what the objection requires, whether the settling corpus exists |
| R-24 | Period racial vocabulary in the platform's voice | Principle 20 | Quotation only, marked |
| R-25 | Starting the immersive MVP with VR/headsets | PENDING-RULE 12; T4 | Structured content first, web → spatial → AR |
| R-26 | Greek philosophy "200 years after" writing returns | Enn | ~140 years (Claude's figure, CLAUDE-ORIGIN) and the point that literature begins at import |
| R-27 | Vowel-writing as a Greek invention | Enn | Sign assignment Greek/Phrygian; concept Near Eastern; script Phoenician |

### 5.5 · SUPERSEDED

| # | Earlier | Later | Where |
|---|---|---|---|
| S-01 | "Meluhha → Keezhadi" (project name) | Veḷi | T1 |
| S-02 | Container was reset; files lost | Context compaction; files intact | VELI-00 |
| S-03 | "Into Veli = the door" (VELI-06 A9, Model D) | Three-word system VEḶI / TIṆAI / MELAKEELA-as-mode (PENDING-RULE 18) | T2, 31 Aug |
| S-04 | PENDING-RULE 18 (Melakeela as mode) | Held open; Melakeela-as-primary a live option (D-14) | T2, 1 Sep |
| S-05 | Files 06/07/08 | Merged into VELI-06 Strategy Dossier; VELI-00 still tells sessions to attach "06–07" — **stale** | VELI-06 changelog |
| S-06 | Primary domain AncientSouthAsia.com (VELI-06 C4 item 3) | intoveli.com primary (VELI-06 A8, changelog #3) — **C4 not updated; internal contradiction** | VELI-06 |
| S-07 | 30 KB page-size rule; `.box.r` ≤ 2 rule | Proposed replacement by principles (PENDING-RULES 1–2) — Enn "leaning yes," not adopted | PENDING-RULES |
| S-08 | "20 chartless / 5 oversized / a handful over emphasis" | 34 / 11 / 25 (audit on disk) | VELI-02 |
| S-09 | Sequeira "cite as preprint" | Published *EJHG* 2025 | VELI-09 §K |
| S-10 | MVP "The Ledger and the First Gallery" (six exhibit pages) | "Into Veli: The First Door" (VELI-06 A6) → "A Drop of Water" single experience (PENDING-RULE 12) → T4 six-engine plan → T5 "one investigation playable end to end" (DIG) | Four successive MVP shapes; **none adopted by Enn** |
| S-11 | VELI-12 Year 1 anchored on DMC Dec 2026 | DMC Dec 2027 | VELI-13 B (C-39) |
| S-12 | Page counts 58 (30 Aug) → 69 → 75 → 77 → 78 → 79 → 80 → 82 → 83 → 84 → 85 (`ls`, ~2 Sep) → live 102 (site's own header) → 127 (counted, 4 Sep) | Whichever is derivable from the repository at build time | X-02 |
| S-13 | Audit-after-build | Audit-first workflow | VELI-09 §Q |
| S-14 | Batch-5 "not Hindutva" vouching | Batch-6 funding-unverified flags | VELI-09 §K |

---

## 6 · THREAD-BY-THREAD LEDGER

Each thread: substantive findings · owner decisions · rejected/superseded · open questions · files created · page/exhibit concepts · visual directions · source dependencies · work still needed. Cross-references point to §3–§5 to avoid repeating text.

### T1 · "VELI - closed" (the original build; 395 turns)

**Substantive findings.** V-01 to V-12, V-15 to V-20, V-24 (via later batches), P-01 to P-06, P-22 to P-24. Core: the register-wide scan; jāti absent from the Vedic layer and present everywhere else; varṇa 23; Mahābhārata caste vocabulary concentrated in the two late didactic parvans; the GRETIL contamination; the Tirukkuṟaḷ count; the river page corrected by book; the collocation results; the DEDR Veḷi entry set (three entries, 29-language open/expelled complex — memory; the DEDR locators are not in the project files, **HELD**); the Achaemenid shared state; the Griffith Latin omissions.

**Owner decisions.** D-01 to D-09, D-13, D-19, D-20.

**Rejected / superseded.** R-01 to R-11, R-22, R-23, R-26, R-27; S-01.

**Open questions raised here and still open.** The three Vedic totals; "471 chariots vs 2 merchants" (headline number with no recorded query — VELI-03 backlog #2, highest priority); Sindhu/Sarasvatī/Ganges lemma re-run; varṇa human-applied split; *vrīhi* absence; Shinde 2019 wording; Witzel primaries; the "Latin verses" item (WORKLIST 3.5 — Enn asked which page it refers to; unanswered); the doctoral/independent-research pathway's next step (adversarial contact, D-19).

**Files created in this thread (in its chat outputs, not in project knowledge).** ~58 HTML pages (list in MANIFEST); `veli-landing.html` (18 KB, four movements); `artifact-atlas.html` (with Scylax and Achaemenid routes added late); `who-had-it-first.html`; `two-classical-languages.html`; `gret_scan.json`; `rv_tokens.tsv`; `viz.py`, `colloc.py`, `mk.py`, `diachronic.py`; `bu_clean.txt`, `satapatha*.txt`, `taittiriya.txt`, `kural_ta.txt`; `RIGVEDA_corpus_analysis.md`; `MELUHHA_TO_KEEZHADI_synthesis.md` (§21 missing; §§25–38 absent; §18 "CLAIMS LEDGER" never read); `NAMING_LEDGER.md`; `VELI_INSTRUCTIONS.md`; `MANIFEST.md`; `RERUN.md`; `DECK_GAP_ANALYSIS.md` (Parts 1–7); `MELA_KEELA_INSTRUCTIONS.md` (with B.11–B.14); the INDUSVALLI.pdf deck read (790 pp, 716 images, 63,069 words — a question list, D-13).

**Page/exhibit concepts from this thread.** Built: coverage bias and the Keeladi report; the Chinese pilgrims (Faxian, Xuanzang, Yijing); what travelled to Southeast Asia and what did not; Brāhmī origins; the Kuṟaḷ; kinship across the ancient world (65 KB, 12 red boxes — over every limit); the Veḷi concept from DEDR; Prajāpati/Rudra; the godman economy; Mahadevan graffiti; who-had-it-first (zodiac, lunar mansions, Indus); two classical languages. Proposed, not built: *Who gets to be speculative* (blocked by H-10); the eight doors and six numbers of the landing Act III–IV (which eight, which six: not chosen); the atlas as spine with layer toggles (scripts · śramaṇa sites · trade · ports · aDNA · Chinese routes · SE Asia); the three depths (object · one-sentence finding · evidence) — verdict was "the platform has only the third"; sound (Tamil words spoken with DEDR reflexes).

**Visual directions.** D-04/D-05: dark ground, light as mechanic, *veḷippaṭu*, grey = no data, excommunication arriving last in rust. No photographs possible from Claude; open-licence or supplied images required (VELI-04 "what I need from you").

**Source dependencies (HELD unless noted).** Witzel 1999/2019 · Kuiper 1991 · Mayrhofer EWAia · Shinde et al. 2019 · Narasimhan 2019 supplementary tables (version-pin) · Elfenbein on Brahui · Krishnamurti 2003 · Parpola 1994 · Farmer–Sproat–Witzel 2004 · Rao et al. 2009 · Desset 2022 · Olivelle facing-page editions (for BU 6.2 wording) · DEDR entries for *veḷi*, *kuyavaṉ* (1762), *cintu* (1546), *pari* (3963), *cintam* (2529) — DEDR is on GitHub (RERUN §1) so these are **re-checkable**, not HELD, but the checks are not recorded · Achaemenid royal inscriptions by locus · Sukthankar on the late parvans · Burkert on Near-Eastern influence (named on `two-classical-languages.html`, not accessed).

**Work still needed from this thread.** VELI-03 backlog 1–11 in order; the three live self-contradictions (verify closed); Tier 1 structural items (index cards 6 of 58; 34 chartless pages; 11 over size); synthesis archive update; ~145 image-only slides and 318 orphaned footnotes; tripod artefact (do not publish); Sarazm I4290/I4910 (unmapped); Tamil corpora (Sangam, Tolkāppiyam, Tēvāram — Enn must supply); Pali canon and Aśokan edicts as countable corpora; Śaunaka AV (NOT FOUND in five searches); Chāndogya commentary-free (NOT FOUND); Rāmāyaṇa detailed run.

### T2 · "Retrieving previous conversation content" (founding pack → 20 research batches; final session unretrievable)

**Substantive findings.** V-13, V-14, V-24, V-25; P-07 to P-21; VELI-09 in full. Method rules 14–17. The source-integrity audits (§J, §K, §Q, §R, §X). The external-review response (§AB).

**Owner decisions.** D-10, D-11, D-12, D-14, D-15, D-16, D-17.

**Rejected / superseded.** R-12, R-13, R-14, R-16, R-17, R-19, R-20, R-21, R-25; S-02 to S-09, S-13, S-14.

**Open questions raised here.** All VELI-09 "searches owed" (C-25); the Cinduism ruling; PENDING-RULES adoption (1–19); whether the older-54 audit's "optional polish" (explicit "reproducible from corpus" line) is wanted; `.cite` retrofit across ~80 pages; the external review's still-owed list (§AB: homepage to ~3–4 screens; `/enter` as foyer; rendering/accessibility fixes — opacity-0 without fallback on 50 pages, reduced-motion on only 51, contrast, mobile, keyboard, no-JS; palette division; 25 pages with no inbound link; site search; exhibit taxonomy; page-type classification; publication statuses); Śatapatha disambiguation (blocked: needs a Sanskrit segmenter); Śaunaka AV pull; the healing/living-traditions arm beyond one page; whether *Nāvalam*, *Suvadu*, *Poruḷ*, *Tiṇai* names survive Tamil-dictionary and native-speaker confirmation.

**Files created.** VELI-00 to VELI-05; VELI-06 (27 sections; merged 06/07/08); VELI-09 (batches 1–20); PENDING-RULES; WORKLIST; `netlify.toml`, `_headers` (unrequested); ~27 new HTML pages (58 → 85), including: the-words-of-caste · the-late-hymn · caste-was-law · the-three-ancestries · who-named-india · the-eastern-tradition · meluhha-trade · keeladi · the-narrowing · the-water-city · one-script-many-kingdoms · the-womb-doctrine · jatization · birth-was-not-always-destiny · criminalised-today · visvamitra · origin-myths · the-later-count · the-computed-dawn · the-genome-of-caste · tinai · the-medicine-question · before-the-indus · the-vedda · the-deep-root · the-layers-under-the-language ("Palimpsest, not purity") · a Ledger/credibility page; south-up atlas (167 → 175 sites with `mort` class and eight deep-history sites); design reference boards (three) received and recorded, not adopted.

**Page/exhibit concepts, not built.** "Genetics and nationalism" / "Academia as a battlefield" (Reich delay — verify quotes first); the per-topic credibility ledger; "How a Religion Was Assembled"; "Vedism ≠ Hinduism" naming page (WORKLIST 2.1); "A republic made a defective birth" (Manu 10.22/10.26 — check whether built); gotra-level genetics (partly: the-genome-of-caste); Corded Ware animation; minority-control case study; the OUT OF CONTEXT object-journey series; the atlas language-shift layer; the "Many Laws" gallery; "Languages at the edge of the archive" gallery; the Unreturned / Berlin Room (VELI-06 Theme 3).

**Visual directions recorded (NOT adopted; D-11 governs).** Three-voice typography (serif story · sans system · mono evidence); material palette per page (ink, cotton, terracotta, carnelian, turmeric, indigo, monsoon-green, river, stone); ↕ symbol vocabulary (↕ ◎ ○ ≈ ? ←); editorial cover format `MELAKEELA / BODY / 001`; curious-first voice; wordmark not symbol; no unicorn/temple/chakra/lotus/Om/mandala/distressed fonts; "VISUAL HYPOTHESIS" label on reconstructions; darkness → discovery → light as the reason for the dark aesthetic; design derived from material culture (Indus grids, brick ratios, seal geometry, pigments, strata as navigation, rivers as motion); MELA↑/KEELA↓ wordmark treatment only.

**Source dependencies.** Ali et al. 2014 standing (never checked) · Pathak 2024 and Narayan 2025 funding (UNVERIFIED) · Sequeira funding (UNVERIFIED) · Kerdoncuff et al. 2024 publication status · Reich statements · Chattopadhyaya 1996 dates · Kenoyer et al. 1983 (Baghor) · Fuller 2007 / Boivin 2004 (ashmounds) · Premathilake 2017 (Porunthal) · Peterson 2017b/2022 · Cathcart 2020 · Mukhopadhyay 2021 (carries the Witzel-2019 characterisation) · Aktor 2018, Davis 2020–24, Silk 2020 (STRONG) · Béteille 1996 (cited through Kumar & Choudhury — **not directly accessed**) · Sen 1987, Shukla 1987 · Pemberton 2012, ArunKumar 2012 · Welikala 2024 · Patwardhan (interest disclosed) · Seligmann 1911.

**Work still needed.** See §10.

### T3 · "Intoveli.netlify.app deployment status"

**Findings.** Landing, `/enter`, `/endogamy-clock` resolve. `/RIGVEDA_corpus_analysis.md` and `/MELUHHA_TO_KEEZHADI_synthesis.md` **404** (publish-directory or extension handling). `/artifact-atlas` returns no text to a fetcher (JS-rendered) — verify in a browser. **Cross-reference C-32:** the zip fix must be confirmed live. Nothing else.

### T4 · "Current HTML capabilities" (independent assessment + build plan)

**Substantive findings.** V-21; C-34 to C-38; fourteen benchmark digital-museum projects researched (names not in project knowledge — the report `MelaKeela-Veli-Independent-Assessment.md` lives in that chat); scores (museum 5/10 · research 6 design / 3 practice · education 3 · DH 7 · public history 6); the reproducibility promise cannot be exercised by a visitor because no data or code is downloadable from any page read; the Sources page publishes conduct findings about named living scholars with no editorial name, corrections log or right of reply; ~55% of pages carry a draft-status disclosure (later corrected to 44%).

**Owner decisions.** D-18 (role); benchmarking already complete; solo/small-team with heavy AI; the goal is a world-leading interactive museum and learning environment for children and non-specialists while preserving the evidence layer (ambition statement, internal).

**Proposed (Claude), not adopted.** Six engines over one JSON layer (Claim graph · Time-space/Atlas · Corpus query · Sequence · Object portal · Depth renderer); static-only; depth toggle Discover/Deeper/Research; `kid_safe: false` default per claim; `lint.py` build gate; four NOW tasks with first prompts for Claude Code; three NEXT systems; LATER tier; the explicit not-yet list (reconstructions, headsets, separate kids' site, CMS/backend, AI chatbot, video, commissioned illustration, multi-museum ingestion — **note this contradicts PENDING-RULE 13's one-ingestion-layer proposal**, Tamil UI before `claims.json`).

**Open.** All of the above awaits Enn; the Danino order (HELD); the seafaring line; the atlas counts; the editorial-accountability gap on the Sources page (who signs, corrections log, right of reply — Rule 6 and VELI-06 B3 both require this and nothing is built).

### T5 · "Child-centered learning through evidence discovery"

**Substantive findings.** P-25 (DMC); the funding taxonomy (Canada federal/provincial, SSHRC, Mitacs, CMF, Canadian Heritage; international rows flagged VERIFY); the scholar map by function.

**Owner decisions.** Enn's product vision: children learn epistemology through real evidence, not textbook conclusions; deep research and a proposal stakeholders can act on; funding not limited to Canada/India/Sri Lanka; "can't you create the proposal, visually?" → the deck.

**Files created (in that chat).** VELI-10 (DIG: vertical slice, age bands, interaction rules, learning model, funding architecture); VELI-11 (UTSC profiles — Bhavani Raman, Sidharthan Maunaguru; scholar map; funding taxonomy); VELI-12 (master plan: nine engines, five rendering modes, eight evidence classes, eleven working groups, funding stack, three Claude Code builds); VELI-13 (Founding Partners Prospectus, Part A external / Part B internal); MELAKEELA-VELI-DECK-v0.1 (16 slides, PPTX + PDF, pptxgenjs + sharp).

**Concepts.** The Witness engine on "Could they read?" (child page and researcher page from one YAML); the Dig engine as PWA over Keezhadi with an on-device Field Bag; the Living Doors second entrance (Water · Food · Mind · Body · Home · Movement · Nature · Work · Belief · Language · Power · Play — adopted from the ChatGPT comparison as "the single strongest idea in either document," **Claude's judgement, not Enn's**); Children's Council; Living Worlds Council with veto over misrepresentation and false continuity; executive core of 4–6 deciders (from ChatGPT) vs eleven working groups (VELI-12) — Claude conceded the former is better.

**Visual direction (deck constitution).** Dark field; vector art from the material culture; evidentiary weight sets visual scale; line treatment carries status (solid / dashed / dotted = documented / inferred / contested); no fabricated facts; six hero frames deferred until a rights-cleared visual corpus exists ("rights work measured in months"); "the field reveals the record."

**Source dependencies / verification tasks.** Dr. G. Sundar (Roja Muthiah Research Library) as bridge to UTSC Digital Tamil Studies and the TNSDA Tamil-Brāhmī graffiti project — **"the most important single verification task in the file"**; every funding row marked [VERIFY]; DMC 2027 guidelines; SSHRC/Mitacs current rates; CMF non-profit eligibility; MAP digital-only eligibility; Horizon Europe association status.

**Open.** D1 naming (D-14) blocks A1/A10 of the prospectus; the inventory conflict (C-40) blocks printing any site count; `intoveli.netlify.app` is a development URL — a real domain is needed before Part A goes out; the nine outreach roles are sequenced (slow ones now: evaluator, institutional partners, research council; school, elders, donors only after a playable prototype) — **nothing has been sent**; Sharma Centre (Pappu / Akhilesh) is the top-ranked partner and no contact has been made.

---

## 7 · FILES AND ARTIFACTS — where things actually are

### 7.0 · In this project's knowledge (the only files a new session can read without upload)

| File | Dated | Authority | Known staleness |
|---|---|---|---|
| VELI-00-READ-FIRST.md | 30 Aug | Conduct | Tells sessions to attach "06–07"; 07 no longer exists (merged into 06). "58 pages" is stale (85 on disk by 2 Sep; 127 live by 4 Sep). |
| VELI-01-FOUNDING-CONTEXT.md | 30 Aug | Decisions | §5–§6 institution/name question partly superseded by D-14; "58-page platform" stale |
| VELI-02-STATE-OF-THE-PLATFORM.md | 30 Aug | What is built | Audits the 58-page state only; the 27 later pages are not audited here |
| VELI-03-CLAIMS-AND-VERIFICATION.md | 30 Aug | Evidence | Does not include VELI-09's cited claims; varṇa-womb check now resolved (§O) but still listed as backlog here |
| VELI-04-INSTRUCTIONS.md | 30 Aug | How to write/build; work order | Work order not updated with T2 DONE items; WORKLIST.md is the live version |
| VELI-05-pagemeta.json | 30 Aug | Machine-readable 58-page meta | 58 pages only |
| VELI-06-STRATEGY-DOSSIER.md | 30 Aug | Strategy | C4 item 3 contradicts A8 on primary domain; A9 Model D superseded by PENDING-RULE 18 then held open |
| VELI-09-DEEP-HISTORY-FINDINGS.md | 31 Aug → ~2 Sep | Cited research, batches 1–20 | Page-count lines inside are a running log; the last states 85 |
| PENDING-RULES.md | 31 Aug – 1 Sep | Proposals awaiting Enn | None adopted in writing except the anti-deflection law (adopted by Enn's repeated instruction) and the 1 Sep session note (D-11, D-14) |
| WORKLIST.md | 1 Sep | Live work order | Tier 1.1 (varṇa-womb) and 1.2 (corpus expansion) done per VELI-09 §O, §V — WORKLIST not updated |
| RERUN.md | 30 Aug | Reproduction commands | Word total 17,919,338 contradicts `gret_scan.json` |
| MANIFEST.md | 30 Aug | 78/79 shipped files, hashes | Two arithmetic errors (VELI-06 C1.4); describes atlas as "150 sites" |

### 7.1 · Not in project knowledge (exist in chat outputs or on Enn's disk)

VELI-07, VELI-08 (merged; may still exist as files) · VELI-10, 11, 12, 13 · MELAKEELA-VELI-DECK-v0.1 (.pptx/.pdf) · MelaKeela-Veli-Independent-Assessment.md · DECK_GAP_ANALYSIS.md · MELA_KEELA_INSTRUCTIONS.md · VELI_INSTRUCTIONS.md · NAMING_LEDGER.md · the 85 HTML pages and the site zip (95 files) · `gret_scan.json` · `rv_tokens.tsv` · corpora · scripts · INDUSVALLI.pdf · the three design reference boards · Enn's visual-concept document (140 sites / 299 windows) · the Melakeela brand document · the ChatGPT response compared in T5.

**No Git repository exists** (Tier 0.1, open since 30 Aug, named in every file as the highest standing risk). Until it does, "where is the current version of X" has no answer that survives a container reset.

---

## 8 · SOURCE DEPENDENCIES — the HELD register

Load-bearing sources whose direct access is not recorded anywhere in the project files or retrievable threads. Under Rule 7, claims resting on them are HELD until read. Grouped by what they carry.

| Source | Carries | Currently reached via |
|---|---|---|
| Witzel 1999 (substrate); Witzel 2019 | Para-Munda; "keeps question open"; substrate lists | Deck p.294; Mukhopadhyay 2021; page footer |
| Kuiper 1991 *Aryans in the Rigveda* | Substrate lists on `who-had-it-first` | Footer only |
| Mayrhofer EWAia | Etymological markings | Footer only |
| Shinde et al. 2019 | Rakhigarhi; Irula affinity | Deck; press |
| Narasimhan et al. 2019 + supplementary tables | P-01 to P-03 | Deck quotations; summaries (C-13) |
| Elfenbein (Brahui) | Late-migration hypothesis | Named, not read |
| Krishnamurti 2003; Parpola 1994 | Dravidian-Indus position | Named |
| Olivelle facing-page BU/ChU | Exact wording for the womb doctrine | ChU verified across web concordance; BU from `bu_clean.txt`; Olivelle not consulted |
| Béteille 1996 | Liberal varṇa → rigid jāti | Through Kumar & Choudhury 2020 |
| Sukthankar | Late parvans | Named |
| Achaemenid royal inscriptions | Gandāra/Hindush satrapies | Not by locus |
| Chattopadhyaya 1996 | Damdama/Mahadaha | Cited; absolute dates OPEN |
| Kenoyer et al. 1983 | Baghor | Cited; dating basis now stated as contextual |
| Reich (public statements) | Publication delay | Not verified |
| Supreme Court order 11 Mar 2026 and late-May modification (Danino) | Correction to live page | T4 web search only |
| DMC 2027 guidelines | Eligibility | 2026 guidelines via web |
| DEDR entries (veḷi ×3; 1546; 1762; 2529; 3963) | Naming; etymology candidates | On GitHub (RERUN §1) — checkable; checks not logged |
| Sangam · Tolkāppiyam · Tēvāram · Pali canon · Aśokan edicts · Śaunaka AV · Chāndogya (clean) | Everything Tamil/Pali/Prakrit that is not the Kuṟaḷ | NOT OBTAINED / NOT FOUND |

**Access constraint to record (VELI-09 §P):** bash is allow-listed to GitHub/PyPI/npm; GRETIL Göttingen and SARIT return 403 from bash but are reachable by `web_fetch`. Verse verification method that worked: search → concordant independent results → verbatim agreement. A dedicated Indic-text connector would remove the friction.

---

## 9 · CONTRADICTIONS BETWEEN CONVERSATIONS AND DOCUMENTS

Each is a Rule 15 violation (status inconsistent across files) until resolved. The least-complete record determines the canonical status.

| # | What disagrees | Values | Resolution path |
|---|---|---|---|
| X-01 | **Atlas site count** | 140 (live Enter; Enn's visual doc) · 150 (MANIFEST description; VELI-02 "stated 150 carry a note") · 158 (live Explore) · 167 → 175 (VELI-09 §N after additions; live page title) · 194 (VELI-02 §6, VELI-03 parsed records; VELI-13) · 199 (site-class rows) · windows 299 (visual doc) vs 315 (VELI-02/03) | Extract the atlas dataset to JSON (Tier 0.2), count, and generate every stated figure from it. Until then no document prints a site count. |
| X-02 | **Page count** | 58 (VELI-00/01/02/05, 30 Aug) · 69 (external review's build) · 85 `ls` (VELI-09 §AB) · 102 (live Research Index header) · 127 (T4 count of index entries) · ~135 (T4 incl. routes and `.md`) | The live site has more pages than any project file records. Either 42 pages were built between 2 and 4 Sep (in the unretrievable session) or the live index counts routes the files don't. **Count the deployed directory.** |
| X-03 | **Corpus total** | 17,934,563 (`gret_scan.json`, VELI-00/03) vs 17,919,338 (RERUN.md) | JSON wins; correct RERUN and announce (Standing Order 4). |
| X-04 | **Vedic totals** | 700,000 · 660,000 · 840,248 | Reconcile from per-file counts in `gret_scan.json`; no page carries one until done. |
| X-05 | **`the-curve.html` `<title>`** | "1.8 million words… absent from most of it" vs the finding (17.9 M scan; absent from 840,248 = 4.7%) | Fix title (VELI-06 C1.1 "fix first"). Verify done. |
| X-06 | **Jāti in the Brāhmaṇas** | VELI-03: jāti = 0 in Saṃhitās + Brāhmaṇas, "raw string count, absent in every sense" · VELI-09 §V: an earlier "236 jāti in Śatapatha" refused as substring noise | If a raw substring search of the Śatapatha returns 236, then either the 840,248-word set excludes the Śatapatha (added later from a separate GitHub source) or the "0" is a whole-token count, not a raw string count. **State the exact text set and method behind V-02 before it is used again.** |
| X-07 | **Taittirīya size** | 166,000 words (VELI-03, padapāṭha caveat) vs 163,264 whole tokens (VELI-09 §V) | Probably units; record both with basis. |
| X-08 | **Primary domain** | intoveli.com (VELI-06 A8, changelog #3) vs AncientSouthAsia.com (VELI-06 C4 item 3) vs melakeela.com (now owned, D-14) | C4 is stale text; D-14 holds it open. |
| X-09 | **Brand architecture** | Model D "Into Veli = door" (VELI-06 A9) → three-word system, Melakeela = mode (PENDING-RULE 18) → Melakeela-as-primary live option (1 Sep) → T5 files assume "Veḷi = institution and ledger, Melakeela = door" | None adopted by Enn beyond "not finalised." Every T5 document and the deck should be read as carrying an unresolved name. |
| X-10 | **MVP shape** | Four successive proposals (S-10) | None adopted. |
| X-11 | **Ingestion layer** | PENDING-RULE 13: one Veḷi Collections ingestion layer normalising ten museums · T4: multi-museum ingestion explicitly deferred | Both Claude-origin; Enn has decided neither. |
| X-12 | **Working groups** | VELI-12: eleven working groups · T5 comparison: 4–6 person executive core is better | Claude reversed itself within one thread; the prospectus (VELI-13) should be checked for which it uses. |
| X-13 | **DMC date** | VELI-12 Year 1 = Dec 2026 · VELI-13 B = Dec 2027 | VELI-12 must be corrected or marked superseded on its face. |
| X-14 | **Seafaring** | live `rakhigarhi` page: "no seafaring in the Rigveda" · site corpus file: *naú-* n = 40 | Re-run from `rv_tokens.tsv`; correct the page. |
| X-15 | **Live self-contradictions** | VELI-02 §5 lists three (the-killed h1; the-names h1; brahmi card vs page) as open · WORKLIST says the-killed and brahmi fixed 1 Sep · the-names not mentioned as fixed | Verify all three on the deployed site. |
| X-16 | **Institution vs museum** | VELI-01 §5 live contradiction · VELI-06 A1 "living research museum" with institute functions inside · T5 files call it "museum and research institution" | VELI-06's reconciliation is proposed, not adopted (C4 item 1 awaits Enn). |
| X-17 | **Session protocol** | VELI-00 "attach 00–04 and 06–07" | 07 merged into 06; PENDING-RULES, WORKLIST and VELI-09 are not in the protocol at all though they carry the latest state. **Rewrite VELI-00's file table.** |
| X-18 | **Not-yet lists** | T4 defers a separate kids' site · VELI-10 designs the children's product as a vertical slice inside the same evidence layer | Consistent in substance (opt-in per claim); note so no one reads them as conflicting. |
| X-19 | **Batch-16 verdict vs T1 turn 387** | VELI-09 §X: older pages "SOUND… no re-sourcing required" · Enn (T1): "most of your pages were problematic… we will go through each page" | The §X sweep checked *sourcing markers*, not *claims*. It does not discharge Enn's instruction. **Page-by-page claim review remains owed on all Claude-built pages.** |

---

## 10 · WORK THAT STILL NEEDS COMPLETION — ranked

Ranked by what it blocks. Status codes: OPEN · OWED (named in a file as "next pass" and not confirmed done) · HELD · HOLD (must not proceed).

### Tier 0 — custody and truth of counts
1. **Git repository** for site, scripts, docs; corpora in a second. OPEN since 30 Aug. Blocks nothing, protects everything.
2. **Extract atlas to JSON and generate every count** (X-01). OPEN.
3. **`lint.py` or equivalent build gate** so typed numbers must equal data (T4 proposal; Rule 14). Not built.
4. **Count the deployed site** (X-02) and reconcile with `ls`.
5. **Confirm live**: the two `.md` 404s fixed (C-32/T3); the three self-contradictions (X-15); "one individual" removed from `steppe`/`endogamy-clock` (C-16 6.1); the-curve title (X-05).
6. **Resolve X-06** (jāti method and text set) before V-02 is cited again.
7. **RERUN word total** (X-03); MANIFEST arithmetic.

### Tier 1 — decisions only Enn can make (blocking)
8. **D1 / D-14**: Melakeela vs Veḷi. Blocks prospectus A1/A10, deck, domain, landing copy, brand.
9. **Cinduism ruling** (VELI-06 A9). Awaiting.
10. **PENDING-RULES 1–19**: adopt, amend or reject each in writing.
11. **VELI-06 C4 items 1–8** (identity, brand, domains, "Where we stand" page, NFP incorporation, licensing, MVP scope, §20 deferral).
12. **MVP shape** (S-10): pick one.
13. **Which eight doors and six numbers** on the landing.
14. **"Latin verses"** (WORKLIST 3.5): which page.
15. **Images**: which pages need photographs; sources.

### Tier 2 — verification backlog (VELI-03 §10, still open unless noted)
16. Reconcile the three Vedic totals (X-04).
17. **"471 chariots vs 2 merchants"** — verify or remove from the landing. Highest-priority unrecorded headline number.
18. Sindhu 204 / Sarasvatī 75 / Ganges 1 — lemma-verified re-run with recorded query.
19. Varṇa 23 human-applied split; colour/skin count "done right" (WORKLIST 1.3).
20. Label jāti sense-split as "identified instances" everywhere.
21. Read synthesis §17–§19 (§18 may be a ledger draft). Never done.
22. Pin every genetics citation to version and date.
23. Audit which counts have a second-source check.
24. Griffith omissions beyond the three known.
25. Close atlas `assumed` flags — one excavation report per row (145 rows).
26. Vellalar AHG figure — obtain or stop referring to it.
27. *Vrīhi* absence — one command.
28. Seafaring (X-14).
29. Danino page (C-35) — read the order.

### Tier 3 — research owed (C-25 list; each a NOT FOUND IN THIS SEARCH until run)
30. Ali et al. 2014 team standing.
31. East-vs-south excavation-coverage; Pataliputra→Patna toponym.
32. Śramaṇa-roots search.
33. Damdama/Mahadaha absolute dates; Indus death-rites ↔ megalith ↔ tribal; ashmound global uniqueness; ASI vs AASI precision. **Gate for publishing contested deep-history claims (PENDING-RULE 19).**
34. r/l, v/y eastern-Prakrit substrate.
35. Jāti-etymology Scite verification (PENDING-RULES 4).
36. Varṇa-mobility lead — primary sources or drop.
37. Reich timeline/quotes.
38. Kerdoncuff 2024 publication status.
39. Pathak, Narayan, Sequeira funding.
40. **Witzel primaries** (C-18) — Witzel 1999, 2019; Kuiper 1991; Mayrhofer — read directly; then re-status every dependent claim.
41. **Citation history for "Who gets to be speculative"** (H-10) — assemble or drop the page.
42. Shinde 2019 exact wording (Irula).
43. Béteille 1996 direct.
44. Dr. G. Sundar / RMRL bridge verification (T5's top task).
45. Every [VERIFY] row in the VELI-11 funding taxonomy; DMC 2027 guidelines.
46. Tamil-dictionary + native-speaker confirmation for *mēla/kīḻa, suvaḍu, aḍukku, nōkku, tiṇai, nāvalam, poruḷ*; trademark/handle checks (external-research item 1, VELI-06 C5).

### Tier 4 — build and structure (after Tier 1 decisions)
47. Claims ledger as live page (Tier 1.1 in every file) — the product.
48. `.cite` block retrofit across ~80 pages (C-29).
49. Re-attribution on `jatization`, `birth-was-not-always-destiny` (C-26) — confirm done.
50. External review still-owed list (§6 T2).
51. Split/chart/emphasis passes on the older pages (VELI-04 1.2–1.4) — pending PENDING-RULES 1–2 decision.
52. Index cards (6 of 58 → all).
53. Synthesis archive update; §21 missing; §§25–38 absent.
54. ~145 image-only slides; 318 orphaned footnotes.
55. Śatapatha disambiguation (needs segmenter); Śaunaka AV pull; Chāndogya clean text.
56. Tamil corpora acquisition (Enn supplies).
57. Page-by-page claim review of every Claude-built page (X-19, D-13).
58. The editorial-accountability layer for the Sources page (who signs, corrections log, right of reply).
59. Outreach sequence (T5) — only after 8 and 47 exist; nothing sent yet.
60. Incorporation (~Sep 2026 target) to start the DMC clock for Dec 2027.

### HOLD — must not proceed
- Any page count, site count or corpus total in public copy until Tier 0 items 2–7 are done.
- *Who gets to be speculative* until H-10's evidence exists.
- Any deep-history contested claim gated by item 33.
- Any external prospectus send until D1 is decided and X-01 is resolved (VELI-13 B1).
- Tripod artefact; Sarazm I4290/I4910; Vellalar AHG number.
- Production HTML by Claude Chat (Rules message: Claude Chat researches and drafts; Claude Code implements after checkpoint).

---

## 11 · STANDING RULES CONSOLIDATED FROM THE CORRECTION HISTORY

These are the rules the record produced, in addition to the Rules message and VELI-01 §4. A later agent should treat them as binding operational discipline; where they overlap with PENDING-RULES they are marked.

1. Two chronological instruments (metrical stratum, book order) are reported together; neither is used alone for a directional claim. (C-05)
2. Exact lemma forms; data-source gaps stated on the page. (C-04)
3. Collocation beats etymology; phonotactics cannot test substrate origin. (C-09, C-10)
4. Attestation ≠ derivation ≠ meaning; give all three. (C-11; PENDING anti-deflection law §3)
5. Both halves in the same breath; the indictment first; the headline carries the argument. (C-07; anti-deflection law)
6. Symmetry of skepticism: an objection faces the four tests (what it requires; who holds it and at what cost; evidence or absence; has the settling corpus been assembled and funded). "Contested" is not a verdict. (C-16 6.5; B.11)
7. Controlled absence: silence in a curated record is not refutation; a gap permits agnosticism, not invention. (B.12)
8. An attested family and an unattested hypothetical donor are not equal; the unattested one earns a note, not a lane — and is not dismissed on its proponent's identity. (C-17)
9. Every scholar cited through another scholar or a slide is HELD until read. (C-18; Rule 7)
10. Verify venue, peer-review status, reception, co-authors, funding — before vouching either way; say "unverified" when it is. (C-24)
11. Audit before build; strong claims on strong sources; weak sources demoted or dropped. (C-26)
12. A search named as owed is a dependency; a page depending on it is INCOMPLETE. (C-25)
13. Regex flags are read in context before they become findings. (C-27)
14. Counts are `ls`/data-derived, never a running tally or a stated figure taken on trust — including in Claude's own reports. (C-28, C-34)
15. A badge is not a record: DOI, locus, method, supports, does-not-support. (C-29)
16. Interest disclosure for living authors writing from within an institutional project. (C-30)
17. Check the headline for overclaim in the platform's own direction as rigorously as for deflection. (C-31; Rule 16)
18. Living figures: only the convicted, only the record. (C-20)
19. No meta-commentary, no "you," no "that reverses what I said" on a published page or document. (C-06, C-38)
20. Never reference a page from memory; run the cross-link check. (C-22)
21. Files only on request. (C-21)
22. Compaction is not a reset; ask for files, do not reconstruct. (C-23)
23. Version-pin; published version; record that the preprint differed. (C-12)
24. Never back-project a modern language label; "Language X" stays in the northwest; cite the right discipline; ancient ancestry ≠ late language. (PENDING-RULES 14–17, proposed)
25. Northern priority is an artefact of excavation density and publication politics; never present as settled. (D-10)
26. Debrahminize = strip the thumb from the scale, not press the other pan. (VELI-00 SO 11; PENDING-RULE 7)

---

## 12 · HONEST CHECKPOINT (Rule 13, workflow step J)

**Status of this deliverable: COMPLETE as a handoff; the project it describes is INCOMPLETE.**

What this document did: read all twelve project files in full; searched all five threads on the named correction topics; read the T1 asymmetric-skepticism turn in full; reconstructed the chronology of corrections from the retrievable record; separated statuses as instructed; logged nineteen cross-document contradictions and sixty ranked work items.

What it could not do:
- Read the 6 September session of thread T2 (not retrievable). If that session contains decisions or corrections beyond those reconstructed in §3, they must be added by someone who can see it.
- Re-run any count. Every figure here inherits the status of its source file.
- See any file outside the twelve in project knowledge. The existence and current content of VELI-10–13, the deck, the assessment report, the HTML pages and the corpora are attested by threads, not verified on disk.
- Confirm whether items marked "verify done" (C-09, C-11, C-16 6.1, C-26, X-05, X-15) were actually completed; the record says they were owed or fixed in a chat, and the deployed state was not checked.

What would change this document's own status: a Git repository with the deployed site, `gret_scan.json`, the atlas JSON and all VELI files in one place — after which every "verify done" and every X-item becomes a one-command check rather than a question.

**Canonical status of the platform under Rule 15:** the least-complete load-bearing dependency is Tier 0 (no repository; counts not generated from data; live site's own inventory disagrees with every project file). The platform is therefore **INCOMPLETE**, whatever any individual page or file says.
