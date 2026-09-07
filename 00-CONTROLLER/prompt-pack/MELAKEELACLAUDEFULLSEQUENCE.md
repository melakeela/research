# Mela Keela / Veḷi — Claude live-audit, research and build sequence

**Prepared 5 September 2026.** This is the operating sequence for turning the language-science, ancient-subaltern and Bronze Age corridor programmes into reviewed content and repository-integrated experiences.

## The direct answer

Yes: begin by telling Claude Chat to browse <https://melakeela.com>, discover the current public pages and identify what research or correction each topic needs.

That live audit can replace the earlier idea that Claude Code must inventory the repository before any research begins. It cannot replace the repository check **before implementation**, because the deployed site may lag the current branch and a web crawler cannot see unpublished routes, components, data, redirects, tests or correction history.

Use this order:

```text
Claude Chat live-site audit
→ bounded research packets
→ evidence challenge/revision
→ provisional content release
→ Claude Code repository reconciliation
→ final release reconciliation
→ Claude Code build on a branch
→ preview and owner review
→ separate deployment instruction
```

Ask Claude Chat for research/content/data ZIPs, not production HTML. Claude Code should generate or update the site's HTML/components after it sees the complete current repository. A research chat may include a wireframe or interaction specification, but it should not create isolated pages that later have to be forced into the site.

## What you need

1. `MELA-KEELA-CLAUDE-LIVE-SITE-AUDIT-PROMPT.md`
2. `MELA-KEELA-LANGUAGE-RESEARCH-PROMPTS.md`
3. `MELA-KEELA-CLAUDE-SAY-NEXT-RESEARCH-PROMPT.md` for the one-chat workflow;
4. the current master work list;
5. the Who Made the Past research foundation;
6. access to the public website in Claude Chat;
7. later, the authoritative current Git repository in Claude Code;
8. current project instructions, correction ledger and applicable design assets.

Do not upload two site ZIPs without naming which one is authoritative. Prefer direct Git repository access for Claude Code.

## Stage 1 — Claude Chat audits the public site

Start a fresh Claude Chat with web access. Attach the master work list and research prompts, then paste the complete prompt from `MELA-KEELA-CLAUDE-LIVE-SITE-AUDIT-PROMPT.md`.

The audit starts at:

- `/`
- `/enter`
- `/research-index`
- Explore, Exhibits, Evidence/Ledger and Search;
- every discoverable internal content link.

The research index currently presents itself as a grouped list of the visitor-visible content pages. Claude should verify what it can reach, not treat the index's own completeness claim as independently proven.

Expected output:

```text
MK-live-site-audit-2026-09-05/
  README.md
  crawl-log.csv
  route-inventory.csv
  programme-coverage.csv
  current-claim-risks.csv
  overlap-and-merge-map.csv
  research-priorities.md
  preliminary-route-disposition.csv
  research-inputs/
    R1-current-public-coverage.md
    ...
    R19-current-public-coverage.md
```

The key classifications are:

```text
CONFIRMED COVERAGE
PARTIAL COVERAGE
PASSING MENTION
CONFLICTING COVERAGE
NOT FOUND IN PUBLIC AUDIT
INACCESSIBLE/UNKNOWN
```

**Gate:** Do not commission a new page merely because its proposed title is absent. The underlying subject may already sit inside another page. Public route decisions remain provisional until Stage 7.

## Stage 2 — Create one Claude Project

Create a Claude Project called:

```text
Mela Keela — Veḷi Research Programme
```

Place only shared governing material in Project Knowledge:

- shared research contract;
- master work list;
- Who Made the Past foundation;
- live-audit README, programme coverage and risk/overlap maps;
- project rules for claims, sources, Tamil text and publication;
- a short glossary of stable work IDs.

Keep topic-specific page exports and source PDFs in the corresponding topic chat. Do not load every source into every conversation.

## Stage 3 — Run nineteen bounded research stages

For the simplest owner workflow, paste `MELA-KEELA-CLAUDE-SAY-NEXT-RESEARCH-PROMPT.md` once in the same Claude Project and then reply **next** after each completed stage. The controller must still generate a separate reviewed R packet and cumulative checkpoint for every topic. If a long conversation loses continuity, resume from its latest cumulative checkpoint rather than reconstructing the programme manually.

The lower-context alternative is one chat per R packet: paste the shared research contract, then one R prompt, and attach its `R#-current-public-coverage.md`. This remains useful if one topic requires a different specialist corpus, but it is not required for the owner's “say next” sequence.

| Order | Packet | Purpose |
|---|---|---|
| 1 | R1 — Tamil and AI | Defines actual model tasks and a bounded modern experiment. |
| 2 | R9 — Rigvedic sound provenance | Separates inherited sounds, Indic change, areal hypotheses and later analysis. |
| 3 | R16 — Dravidian sibilants | Reconstructs Proto-Dravidian sound categories and later Tamil graphic accommodation. |
| 4 | R3 — Oral normalization | Tests metre, Saṃhitā, Padapāṭha and later normalization on concrete forms. |
| 5 | R10 — Rigvedic strata and society | Re-audits strata, patronage, conflict, forts and canonization. |
| 6 | R12 — Oxus interface | Tests BMAC contact, loan vocabulary, genetics and ritual provenance. |
| 7 | R17 — Same world, two responses | Tests Rigvedic patronage against Old Avestan reform without false peaceful/violent binaries. |
| 8 | R2 — Before Pāṇini | Rebuilds the grammar account after language/transmission distinctions exist. |
| 9 | R4 — Before Tolkāppiyam | Builds Tamil's linguistic/poetic architecture on its own sources. |
| 10 | R11 — Substrates and grammatical ontology | Tests *kīnāśa*, lost-language vocabulary and noun-class comparisons. |
| 11 | R18 — Brahui and the hills | Tests continuity, migration, genetics, contact layers and highland survival. |
| 12 | R13 — Stones and routes | Audits lapis, carnelian, Meluhha/Marhaši and trade/tribute/raiding. |
| 13 | R19 — Before Oil | Builds Hormuz's sourced ancient-to-present corridor history. |
| 14 | R14 — Language that changed | Synthesizes a sound/word/grammar/contact slider from accepted records. |
| 15 | R5 — Mouth, writing and dates | Handles articulation, scripts and Brāhmī chronology. |
| 16 | R6 — Multiple language sciences | Makes worldwide comparisons on matched criteria. |
| 17 | R8 — Sacred attribution | Traces Śiva/Māheśvara and Agastya/Agattiyam attribution histories. |
| 18 | R15 — Before Alexander | Tests actual pre/post-Alexander corridors and Greek–Indian transmission claims. |
| 19 | R7 — Contact and meaning | Handles the hardest directionality claims after the chronologies exist. |

R1 can proceed while historical sources are collected. Preserve these dependencies:

```text
R9 → R16 → R3 → R2
R10 + R12 → R17
R11 + R12 → R18
R13 → R19
R3 + R9 + R11 + R12 + R16 + R18 → R14
R2 + R4 + R5 + R15 → R7
```

Nineteen chats do not mean nineteen pages. A packet may correct several routes, supply one shared dataset, become a section, remain on research hold or show that a proposed page would duplicate existing coverage.

## Stage 4 — Require the same packet ZIP from every chat

Append this instruction to every R prompt:

> Return a downloadable ZIP named `MK-R#-short-title-v1.zip`. Do not create production HTML, CSS or JavaScript and do not redesign the website. Preserve Unicode Tamil, Sanskrit/Avestan diacritics and source URLs. CSV must be UTF-8 and machine-readable. Put long prose in Markdown. If a ZIP cannot be produced, return the same files separately with exact filenames.

```text
MK-R#-short-title-v1/
  README.md
  packet-manifest.json
  research-synthesis.md
  claims.csv
  sources.csv
  chronology.csv
  comparisons.csv
  corrections.md
  open-questions.md
  route-disposition.csv
  rights-and-assets.csv
  copy/
    existing-page-revisions.md
    proposed-new-page-copy.md
  interactions/
    feature-brief.md
  data/
    examples.json
    relations.json
```

Required claim fields:

```text
claim_id,public_sentence,source_id,locator,evidence_role,inference,counter_evidence,scope,date_or_stratum,status,affected_route
```

Every relationship edge must be typed:

```text
genealogy | borrowing | transmission | analogy | shared_source | contact_possible | disputed
```

This prevents an implementation from turning a chronological overlap or visual arrow into a historical conclusion.

## Stage 5 — Challenge and revise every packet

Use the challenge prompt on the v1 packet. The review must reopen the consequential sources, not simply ask another model whether the prose sounds credible.

Request `MK-R#-short-title-v2-reviewed.zip` with:

```text
review/
  accepted-claims.csv
  revised-claims.csv
  held-claims.csv
  source-check-log.csv
  conflicts-with-existing-site.md
```

Claims depending on Vedic accent/metre, Avestan reconstruction, Tolkāppiyam interpretation, etymology, ancient DNA, excavation stratigraphy, museum provenance or ancient textual translation remain held until inspected at the required level or reviewed by a suitable specialist.

**Gate:** Every proposed public claim has a source and exact locator or is excluded from publishable copy.

## Stage 6 — Claude Chat creates a provisional release

Start a fresh chat in the same Project. Upload:

- the live-site audit;
- the reviewed R packets selected for the release;
- the master correction ledger if available;
- the current claim/evidence schema.

Ask Claude Chat:

> Reconcile these reviewed packets into a provisional content release. Do not create HTML. Preserve current corrections and list unresolved conflicts instead of choosing silently. Decide extend/merge/new/shared-feature/research-hold provisionally for every affected topic. Produce one claim/source/relationship dataset and one route plan. Keep the first build to the smallest coherent visitor journey plus necessary corrections.

Expected ZIP:

```text
MK-release-01-provisional/
  README.md
  release-manifest.json
  route-plan.csv
  accepted-claims.csv
  held-claims.csv
  sources.csv
  chronology.csv
  relation-types.json
  rights-and-assets.csv
  copy/
  features/
  qa/
```

## Stage 7 — Claude Code reconciles the current repository

Now open Claude Code in the authoritative current Git repository and create a feature branch, for example:

```text
feature/veli-language-corridor-release-01
```

Give Claude Code:

- Prompt 0 from the prompt pack;
- the live-site audit ZIP;
- the provisional release ZIP;
- relevant reviewed packet ZIPs;
- repository instructions and correction ledger.

Tell it: **read-only reconciliation, no edits and no deployment**.

Expected output:

```text
repository-reconciliation/
  README.md
  production-vs-branch.csv
  final-route-disposition.csv
  affected-claims.csv
  prior-corrections.md
  component-reuse.md
  data-migration-needs.md
  asset-and-rights-gaps.csv
  implementation-risks.md
```

The repository is the implementation source of truth. The live audit remains the source of truth for what visitors could see on the audit date. Neither silently overrides the other.

## Stage 8 — Finalize the authorized release

If Stage 7 finds no material conflict, rename the provisional release `MK-release-01-approved` and record the reconciliation manifest.

If it finds conflicts, return only the affected copy/route records to the consolidation chat together with `repository-reconciliation`. Ask for a corrected approved ZIP. Do not rerun all research unless a conflict changes the evidence question.

A sensible first release remains deliberately small:

1. correct high-risk claims on existing Pāṇini/sound/Rigveda pages;
2. add or extend **The Ṛgveda Is Not One Moment**;
3. publish one fully sourced text/transmission comparison;
4. add one Tamil-and-AI page/section with a frozen, accurately described example;
5. build the smallest reusable sound/word/contact component those cases need.

The Oxus interface, complete resource corridor and full slider can follow as a coherent second release if their reviewed data are ready. Do not ship a giant map whose edges have not been sourced.

## Stage 9 — Claude Code builds, tests and previews

Give Claude Code the approved release ZIP and this instruction:

> Work only on the named feature branch. Treat `release-manifest.json` as the authorized content scope and the repository as implementation source of truth. Do not use held claims. Inspect existing components before adding new ones. Correct existing routes before creating duplicates. Update navigation, search, research index, ledger, metadata, evidence records and redirects as required. Do not deploy. Return a local preview, diff summary, claim-change report and validation results.

Recommended commit sequence:

1. `content: correct affected claims and strata`
2. `data: add reviewed evidence and relationship records`
3. `feature: add the first bounded comparison interaction`
4. `content: add or extend approved investigations`
5. `navigation: update index search ledger and routes`
6. `qa: accessibility links rendering and corrections`

Review in this order:

1. factual traceability;
2. chronological and linguistic distinctions;
3. Tamil/Avestan/diacritic rendering;
4. uncertainty and relationship encoding;
5. visitor comprehension;
6. mobile, keyboard, reduced motion, source links, search, CSP and redirects;
7. regression against earlier corrections and routes.

Deployment is a separate owner instruction after preview and diff approval.

## Claims that remain research questions

Do not publish as settled without the required evidence:

- later reciters systematically rewrote early hymns to match Pāṇini;
- reconstructed audio is the historical composers' voice;
- the *kīnāśa*–*kiṇṭu* comparison is an established Dravidian etymology;
- BMAC/Oxus supplied Vedic/Avestan religion as a whole;
- BMAC, Marhaši or Indus languages were Elamite or Dravidian;
- Greek phonetic theory was borrowed from India merely because a corridor existed;
- Rigvedic forts identify Mature Harappan cities or any one excavated culture;
- Tamil is generally harder for AI than other languages;
- tiṇai improves AI without a controlled evaluation;
- typological gender/number resemblance proves ancestry or civilizational psychology.

Their research value lies in showing the current evidence, competing explanations and the test that could change the assessment.
