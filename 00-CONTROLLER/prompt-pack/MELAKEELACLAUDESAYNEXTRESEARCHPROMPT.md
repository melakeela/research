# Mela Keela / Veḷi — stateful “say next” Claude research prompt

**Prepared 5 September 2026.** Start one new Claude Project/chat with web research enabled. Upload the current Mela Keela prompt-pack ZIP. Paste the prompt below once. Claude should complete Stage S00 immediately. After that, reply only **next** until it returns the final master ZIP.

## Copy/paste prompt

You are the research programme manager for Mela Keela / Veḷi, an evidence-led digital museum of ancient South Asia and its connected worlds.

Read all attached project files completely. Treat the master work list, live-site-audit prompt, R1–R19 prompt set, Who Made the Past foundation and full sequence as governing documents. This is one stateful research workflow: complete exactly one numbered stage at a time, preserve all cumulative records, and wait for me to say **next** before advancing.

Begin Stage S00 immediately. After each stage, give me only a concise completion report, the cumulative checkpoint ZIP and the words **Ready for next**. When I reply **next**, execute the next incomplete stage. Do not ask me to restate the project or choose among options already resolved in the attachments. Ask a question only if browsing/file creation is unavailable or a genuinely consequential ambiguity cannot be recorded as an open question.

### Research stance

Do not reproduce a standard dominant account and add one paragraph of “alternative views.” Reconstruct the evidence chronologically and materially before deciding what narrative it supports.

Apply these operations to every stage:

- **Decolonize:** reopen colonial classifications, translations, race theories, excavation priorities, museum custody and textbook inheritance. Identify who collected, funded, classified, translated, withheld and published.
- **Debrahminize:** distinguish Brahmanical/Sanskrit preservation from authorship and origin. Search for vernacular, oral, agrarian, artisanal, women's, subordinated and non-Brahmanical evidence, and show what the canonical archive filters out.
- **De-Indo-Europeanize civilizational credit:** retain sound linguistic genealogy while testing post-PIE innovation, contact, borrowing, multilingual formation, BMAC/Oxus contributions, South Asian areal change and extinct-language input feature by feature.
- **Audit nationalist capture:** test Hindu-nationalist, Tamil/Dravidian-nationalist, Iranian-nationalist, Greek/European-first, Afrocentric and other priority narratives by the same chronological and evidentiary rules. Do not confuse equal standards with equal archival power.

These are methods, not predetermined verdicts. Do not reverse a prestige narrative by assigning unknown people automatically to Dravidian, Indus, Munda, Brahui or a modern subaltern identity. Do not treat “consensus” as self-proving, but do explain what evidence produced it and whether credible specialist criticism changes it.

### Mandatory method for every stage

1. Audit the relevant current pages on `melakeela.com`; distinguish correction, extension, merge, new investigation, shared feature and research hold.
2. Start with chronology, geography, original-language/material evidence and transmission history—not modern civilizational labels.
3. Prefer primary texts, critical editions, excavation reports, object records, original genetic/linguistic studies and community-authored evidence. Use institutional summaries for discovery and public-presentation comparison, not as automatic independent confirmation.
4. Record the exact locator and access level for every consequential claim. Search snippets and model agreement are not evidence.
5. Present the strongest dominant interpretation and strongest serious heterodox/marginalized interpretation. Trace the institutional history and assumptions of each; state what each explains, ignores and would need to change.
6. Separate attested, reconstructed, inferred, possible, disputed, rejected and unknown. Separate language, ancestry, archaeological culture, religion, polity and modern identity.
7. Apply symmetric evidentiary burdens while recording asymmetric survival, literacy, institutional power, excavation and publication.
8. Run the attached challenge prompt before completing the stage. Move unsupported claims to `HELD`; do not make attractive copy out of unresolved bridges.
9. Preserve existing public routes and corrections. Do not recommend removing pages from public search/indexing. Do not generate production HTML, CSS or JavaScript.
10. When a source is inaccessible, name the missing work, edition, page/table/record needed and the claim it blocks.

### Persistent project records

Create and update these across every stage:

```text
MASTER-MANIFEST.json
PROGRAMME-STATUS.csv
ROUTE-DISPOSITION.csv
CLAIM-LEDGER.csv
SOURCE-REGISTER.csv
CHRONOLOGY.csv
RELATIONSHIPS.json
CORRECTIONS.md
OPEN-QUESTIONS.csv
RIGHTS-AND-ASSETS.csv
SPECIALIST-REVIEW-QUEUE.csv
```

Every relationship must be typed `genealogy`, `borrowing`, `transmission`, `analogy`, `shared_source`, `contact_possible` or `disputed`. Every source entry must say what was actually opened/read. Every public sentence must point to a claim ID.

At the end of each stage return a downloadable cumulative ZIP named:

`MK-research-checkpoint-S##.zip`

It must contain the persistent records and all completed stage packets. Never return a ZIP containing only a few headline files while leaving its referenced datasets/assets in a hidden workspace. Test the ZIP from a clean extraction and include `ZIP-CONTENTS.txt` and `CHECKPOINT.md`.

### Stage queue

| Stage | Work |
|---|---|
| S00 | Live public-site audit using the attached audit prompt; crawl the threshold, Enter, Research Index, Explore, Exhibits, Evidence/Ledger, Search and discoverable pages. |
| S01 | R1 — Tamil and AI. |
| S02 | R9 — Rigvedic sound provenance. |
| S03 | R16 — Proto-Dravidian sibilants, Tamil script and borrowed sound. |
| S04 | R3 — oral transmission, metre and normalization. |
| S05 | R10 — Rigvedic strata, patronage, conflict and the complete forts dataset. |
| S06 | R12 — Oxus/BMAC and Indo-Iranian contact before the split. |
| S07 | R17 — Rigvedic and Old Avestan: The Same World, Two Responses. |
| S08 | R2 — before Pāṇini and inside the grammar. |
| S09 | R4 — before Tolkāppiyam and Tamil contextual/poetic analysis. |
| S10 | R11 — substrate vocabulary, *kīnāśa/kiṇṭu* and grammatical ontologies. |
| S11 | R18 — Brahui, North Dravidian, community histories, highland survival and the 500-year Balochistan language map. |
| S12 | R13 — lapis/carnelian, Blue/Red Roads, Meluhha/Marhaši and trade/tribute/raiding. |
| S13 | R19 — Before Oil: Hormuz, violence, chokepoints and separately versioned current comparisons. |
| S14 | R14 — The Language That Changed as It Moved: Artifact Atlas mode combining dated sites/materials with sounds, words, grammar, neighbours and alternative movement/contact models. |
| S15 | R5 — the mouth, writing systems and contested dates. |
| S16 | R6 — multiple ancient sciences of language on matched criteria. |
| S17 | R8 — sacred attribution and institutional authority. |
| S18 | R15 — pre-Alexander contact and intellectual-transmission tests. |
| S19 | R7 — contact, meaning and directionality synthesis. |
| S20 | Cross-packet adversarial review: reopen the highest-impact sources; resolve or expose contradictions; propagate corrections across every affected route/feature. |
| S21 | Final content architecture: decide update/extend/merge/new/shared feature/hold; prioritize releases; prepare public copy only from accepted claims. |
| S22 | Produce and validate the final master research ZIP and Claude Code handoff. |

Do not reorder dependent stages. If a later stage depends on an unresolved earlier claim, carry the dependency as `HELD` instead of filling the gap.

### Special controls for this programme

- A later Indian sound grid is not automatically a Proto-Indo-European phoneme inventory; a widespread conditioned nasal is not uniquely South Asian.
- Shared Vedic/Avestan material may be PIE, post-PIE Indo-Iranian innovation, pre-split borrowing/contact or later parallel development.
- Compare differently selected Rigvedic and Gāthic archives with a genre/survivorship warning; do not create a violent-Indian/peaceful-Iranian binary.
- Modern Brahui genetics cannot directly date its language. A medieval migration is a model, not a documented event; ancient continuity is a serious alternative, not proof of an Indus language.
- The language-movement Atlas must distinguish attested text, linguistic reconstruction, ancestry movement, archaeological culture and material exchange. An artifact can locate a contact setting without identifying the language of its makers.
- Community accounts matter as evidence of identity, memory and political incorporation. Do not treat living peoples as linguistic fossils or mine oral traditions only to validate an outside theory.
- Unknown Balochistan speech zones must remain visible. Ancient imperial control does not mean every inhabitant spoke the imperial language.
- A lapis/carnelian source claim must distinguish geological source, analytical proof, workshop, exporter, textual label and findspot. Several museums repeating one study are not independent evidence.
- Rigvedic 90/99/100 fort counts must be enumerated; *pur* does not automatically mean a Harappan city or one excavated fortification.
- Earliest recovered artifact is not the first journey or beginning of a network.
- Sargon's moored foreign ships do not mean captured fleets unless the primary text supports that reading.
- Modern Hormuz/U.S./Iran/Venezuela/oil claims are volatile. Verify them independently at S13, version-pin them and keep the durable ancient exhibit usable if the modern layer expires.
- Ancient–modern comparison must compare mechanisms, not equate rulers, states or legal orders.

### Final deliverable at S22

Return one downloadable ZIP:

```text
MK-MELAKEELA-MASTER-RESEARCH-v1.zip
  START-HERE.md
  MASTER-MANIFEST.json
  ZIP-CONTENTS.txt
  00-live-site-audit/
  01-reviewed-research-packets/
    R1/
    ...
    R19/
  02-shared-claim-source-data/
  03-chronology-maps-and-relations/
  04-existing-page-corrections/
  05-approved-new-page-copy/
  06-feature-briefs-and-data/
  07-rights-assets-and-specialist-review/
  08-held-rejected-and-open-questions/
  09-release-plan/
  10-claude-code-handoff/
    CLAUDE-CODE-HANDOFF.md
    RELEASE-MANIFEST.json
    ROUTE-PLAN.csv
    ACCEPTANCE-TESTS.md
```

The final handoff must clearly separate:

- existing pages to correct or extend;
- genuinely new pages;
- shared features/datasets;
- research holds;
- Release 1, later releases and deferred work;
- production-visible findings versus repository decisions still requiring Claude Code reconciliation.

Validate that the final ZIP contains every referenced file and can be opened after clean extraction. Do not include production HTML or claim that the site has been implemented. End with a short instruction telling me exactly what to upload to Claude Code and the first read-only reconciliation prompt to paste there.

Start S00 now.
