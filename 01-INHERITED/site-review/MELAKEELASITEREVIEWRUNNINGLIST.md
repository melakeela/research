# Mela Keela — Site Review Running List

**Status:** Active review document. Not yet approved as a Claude Code implementation brief.  
**Started:** 4 September 2026  
**Purpose:** Record confirmed defects, visitor-experience problems, open design questions and ideas while the live site is tested.

## Review principles

- Optimize for what a visitor wants to understand, discover or experience—not repository accounting or internal workflow.
- Keep confirmed defects separate from ideas that still require a design decision.
- A unified identity should not make every exhibit feel like the same text template.
- Movement and interaction must explain evidence, chronology, geography, comparison, uncertainty or transmission; avoid decorative motion.
- Audit recommendations and internal process history belong in internal records. Public disclosures should be short, specific and useful.
- Do not send this list to Claude Code until the owner asks for a consolidated implementation brief.

## 1. Information architecture and page roles

### Problem

The present top-level destinations—Enter, Explore, Exhibits, Evidence and Index—are concise but insufficiently differentiated. Research Index and Exhibits currently look and behave too similarly, while Evidence is presented as a navigation category even though its visitor purpose is not immediately clear.

### Roles to resolve

- **Enter:** Should function as a foyer/orientation experience: a small number of strong starting paths for a first-time visitor, not another catalogue.
- **Explore:** Should enable thematic, spatial, chronological or question-led discovery. It should feel exploratory rather than duplicate a list of exhibits.
- **Exhibits:** Should be the curated collection: editorially composed stories and interactive experiences, grouped into understandable collections.
- **Evidence:** Should lead directly to sources, datasets, corpora, claim records, methods and evidence instruments. Determine whether it deserves a hub rather than linking to one ledger page.
- **Index:** Should be the exhaustive finding aid: every public content page, searchable and filterable, with minimal editorial presentation.

### Decisions still required

- Decide whether all five destinations are genuinely necessary.
- Consider clearer public labels while retaining the poetic Veḷi identity.
- Ensure each destination has a visibly different visitor task and interface.
- Remove duplication between Research Index and Exhibits.

## 2. Navigation and categorized discovery

### Confirmed need

The museum has too many pages for a flat five-link navigation system. Visitors need a categorized menu that exposes the collection without requiring them to know page titles or search terms.

### Menu structure to develop

- A single compact header row on internal pages.
- Logo at left, open search field in the available middle space, hamburger symbol at right.
- No visible word “Menu,” duplicate search field, Method row or contextual navigation row.
- The Veḷi threshold remains free of the conventional site header.
- Menu should include every public exhibit through organized categories and a searchable “all pages” route.

### Candidate subject categories

- Archaeology and material culture
- Language, scripts and etymology
- Genetics, ancestry and migration
- Caste, law and social order
- Religion, philosophy and śramaṇa traditions
- Trade, oceans and connected worlds
- Texts, manuscripts and knowledge custody
- Food, landscape, ecology, music and everyday life
- Institutions, excavation, historiography and who controls the record

These categories are provisional. Page assignment, overlap, cross-listing and naming still need to be designed.

### Candidate discovery modes

- Browse by subject
- Browse by period
- Browse by place
- Browse by evidence type
- Browse by exhibit format: map, timeline, corpus, comparison, object record, source audit
- Search all exhibits and evidence pages

## 3. Header and global interface

### Confirmed defects or requirements

- Four-row mobile header is excessive.
- Keep the mobile and desktop header to one row wherever possible.
- Search may remain visibly open between the logo and hamburger.
- Remove duplicate search fields.
- Replace the word “Menu” with the familiar menu symbol and an accessible name.
- Move Method text into a dedicated Method/Evidence destination or the relevant page body.
- Move contextual trails and related-page links out of the header and into page content or the footer.
- Confirm that the lower word in the logo reads as `keela`, not an inverted repetition of `mela` or an illegible approximation.

## 4. Visitor flow and broken links

- The Exhibits link/CTA immediately after the Veḷi landing experience does not work, although Exhibits is reachable through the menu.
- Reproduce the failure and identify whether it is caused by the link target, overlay, transition state or event handling.
- Verify repaired flow by pointer, keyboard and direct navigation.
- Review the complete visitor path: Veḷi threshold → continuation → foyer → exhibit selection → related exhibit.

## 5. Visual and experiential depth

### Current problem

Many pages present as text on text on text. The shared dark typography is coherent, but the collection lacks sufficient visual evidence, objects, images, spatial variation and immediately discoverable interaction. The result often reads as a set of essays rather than a digital museum.

### Experience requirements to develop

- Give each major exhibit a recognizable visual or interactive idea near its opening—not necessarily above every word, but early enough to establish what makes that exhibit distinct.
- Use object photography, excavation images, maps, inscriptions, manuscript folios, diagrams, comparative plates and facsimiles where they materially support the argument.
- Use public-domain, openly licensed or permission-cleared imagery with creator/institution, date, object identity, licence and source recorded.
- Provide informative captions and alt text; do not use imagery merely as atmosphere.
- Introduce visual rhythm: evidence plates, annotated objects, maps, timelines, quotations, diagrams, controlled reveals and comparison states.
- Retain strong static editorial composition when interaction adds no explanatory value.

### Meaningful interaction candidates

- Scroll-linked or stepped chronology
- Before/after or competing-interpretation comparison
- Layered archaeological and linguistic maps
- Object hotspots and annotated artefact viewers
- Manuscript or inscription viewers with transcription/translation layers
- Evidence-to-claim tracing
- Corpus exploration and verse distribution
- Uncertainty, absence and preservation-bias visualization
- Networks of transmission, custody, funding and institutional control

## 6. Visitor-facing copy and editorial economy

### Remove or reduce

- Counts of total pages, routes, entries or files unless a visitor task genuinely requires them.
- Statements such as “All 102 content pages” and explanations of which utility routes are excluded.
- Repetitive “this page does…” and “this platform does…” narration.
- Internal batch numbers, dates, draft states, recommended statuses and audit workflow.
- Large Method preambles before exhibits.
- Boilerplate explaining the site instead of beginning the subject.

### Veḷi copy under review

The sentence “Not a metaphor they reached for … before anyone built a philosophy on it” is rhetorically heavy and may imply an unestablished chronological priority.

Candidate replacement:

> The siddhars did not invent veḷi as an abstraction. They took a living word—open, outside, clear, light, true—and made it carry the highest thing they knew.

This remains a proposed edit, not yet final.

## 7. Method, disclosure and audit language

- Detailed audit history belongs in the Curatorial Workbench and internal registers.
- Public pages should not display “SOURCE AUDIT · BATCH…,” “INTERNAL DRAFT,” candidate recommendations or HOLD instructions.
- When a material limitation exists, use a concise page-specific disclosure explaining the actual issue.
- Put detailed qualifications beside the affected claim or in an evidence/limits section.
- Do not blanket the collection with “provisional,” “being verified” or equivalent warnings.
- Previously reviewed pages must not be automatically downgraded because a new audit vocabulary was introduced.

## 8. Argument quality and false balance

- Remove rebuttals to weak positions that no serious cited source actually advances.
- Specifically review formulations such as “invasion as a single military event.” This can create a straw opponent and inadvertently legitimize the wrong framing.
- Address the strongest real propositions: migration, mobility, admixture, conflict, elite formation, language transmission and institutional restructuring.
- A contested label must point to a real attributed claim and a real evidentiary disagreement.
- Preserve historically relevant or directly quoted terminology when properly attributed; do not mechanically delete the word “invasion.”
- Avoid structuring pages around concessions to dominant narratives when those concessions are not required by the evidence.

## 9. Known live inconsistencies requiring later correction

- Research Index contains stale and unnecessary page-count language.
- Research Index still uses “held from publication”/HELD language inconsistent with the owner’s public-publication decision.
- `the-proxy.html` says the Irula-proxy premise was removed, while later prose and SVG labels still repeat versions of it. The correction must cascade through prose, captions, accessible names and graphics.
- Artifact Atlas document title says 175 sites while the interface says 158.
- Production includes a Cloudflare analytics request; verification language should distinguish package-originated external requests from infrastructure-injected analytics.
- Google may temporarily show cached descriptions from older versions; distinguish caching from current live content.

## 10. Genetics and ancestry presentation safeguards

- Rakhigarhi must not be presented as the only relevant evidence: the Indus Periphery Cline materially strengthens the inference.
- An evidence-calibrated formulation may state that available IVC-associated genomes carry little, if any, Steppe pastoralist-related ancestry and indicate it was not ubiquitous in the sampled IVC-associated population.
- Do not claim absolute absence across every IVC community and period.
- Do not equate Y-chromosome frequencies with autosomal genome-wide ancestry.
- Do not turn living communities into direct ancient-population proxies.
- Explain Iranian-related ancestry without presenting it as simple descent from later sampled Iranian farmers.
- Distinguish observation in ancient samples, statistical modelling, present-day inference and historical interpretation.

## 11. Artifact Atlas — continue reviewing

Items previously reported as corrected but still requiring owner testing on the live experience:

- Slider stability and absence of visual glitches
- Whether time movement actually communicates chronological change
- Zoom and pan clarity
- North-up/south-up orientation and 180-degree rotation rather than mirroring
- Immediate visibility of selected-site details
- Mobile bottom-sheet usability
- Clear affordances and explanation of controls
- Consistency between title count and dataset count
- Source-record coverage and its visitor-facing explanation

## 12. Questions for subsequent review

- Which pages most urgently need real object or archival imagery?
- Which pages should open with an interaction, and which should begin with narrative?
- Which current exhibits are genuinely distinct below the first viewport?
- Should Explore be organized primarily by questions, themes, time or geography?
- Should Evidence remain a main navigation destination, and what exactly should it contain?
- What is the smallest top-level navigation that still makes the collection understandable?
- How should pages appear in multiple categories without creating duplicated catalogues?
- Which visitor-facing AI experiences provide unique value beyond deterministic interfaces?

## 13. Independent-assessment findings — triaged, not automatically accepted

The external assessment supplied on 4 September 2026 contains valuable defect reports, strategic recommendations and some conclusions that require separate verification. Its language is not itself an implementation brief. Every item below must retain one of three states: **confirmed**, **verify**, or **strategic option**.

### A. High-priority consistency checks

- **Atlas counts — verify and then generate from data.** Reported surface values are 140 sites on Enter, 158 on Explore and 175 in the Atlas title/metadata, with corresponding evidence-window counts of 299 or 315. Confirm every live occurrence and identify the canonical dataset/query. Once confirmed, generate all displayed totals from that one source rather than typing them into page copy.
- **Research Index totals — confirmed as stale in earlier inspection.** Remove unnecessary visitor-facing inventory counts. Internally, add a build check comparing generated entries with the canonical public-page registry.
- **Rakhigarhi/Rigveda seafaring claim — verify semantic scope before editing.** The absolute sentence “The Rigveda contains no seafaring” may conflict with references to `naú-/nā́v-` and the Bhujyu episode. However, occurrences of “boat” do not by themselves establish maritime seafaring. Audit the exact Sanskrit passages, translations, semantic category and intended claim. Replace an absolute claim only with wording the corpus and philology actually support.
- **Conversational drafting residue — verify repository-wide.** Search published `.html`, `.md`, figure captions, accessible labels and downloadable documents for phrases such as “you asked,” “you’re pointing at,” “my hand-curation,” references to “this chat,” and other assistant/user residue. Convert genuine residues to an editorial or clearly attributed first-person voice without erasing legitimate authorship notes.
- **Correction-cascade test.** Every confirmed correction must scan prose, titles, metadata, captions, SVG text, accessible names, downloadable data/docs, search records and related pages—not only the paragraph where the error was noticed.

### B. Reproducibility promise

The threshold promise “every claim is a query you can re-run” should describe a visitor-available capability, not merely internal files.

Audit whether visitors can reach, understand and reuse:

- `gret_scan_v2.json`
- `dedr_roots.json`
- Rigveda token/strata tables
- Kuṟaḷ token/count data
- relevant analysis scripts such as `extract.py`, `lexicon.py` and `analyze.py`
- a rerun guide, licences, version identifiers and checksums

Required outcome if the promise is retained:

- Every computed exhibit links to the exact data and method behind its result.
- Provide a human-readable “reproduce this result” path, not only a raw file.
- Provide stable versions/checksums and state which software/environment is required.
- Where the full query cannot yet be rerun publicly, narrow the claim locally instead of pretending the capability exists.
- Consider a public repository and archival release/DOI as a strategic option; hosting and maintenance implications need approval.

### C. Editorial accountability and right of reply

- Pages that evaluate named living people or institutions need a visible corrections route and a right-of-reply/contact route.
- Separate documented events, direct quotations, institutional findings, inference and the museum’s characterization.
- Do not infer motive or causal linkage merely from chronology or proximity on a timeline.
- Consider a legal/editorial review for pages making misconduct, competence, motive or coordinated-operation claims.
- The assessment recommends naming an editor, institution and external review panel. This is a **strategic option**, not an accepted requirement: the owner’s privacy and safety must be considered. Possible alternatives include a named publishing entity, role-based editorial attribution, a public methodology statement, a contact address and a documented correction/right-of-reply process.
- Remove any language implying private correspondence is public evidence. Restricted correspondence may guide internal research, but public claims require public corroboration.

### D. Danino chronology — urgent verification

- Audit every Michel Danino reference against the precise court orders, dates, parties and subject matter.
- Specifically verify the reported March 2026 direction concerning an NCERT Class 8 judiciary chapter and the reported May 2026 modification using the actual court orders first, then reliable legal reporting.
- Do not place a judiciary-textbook controversy inside a migration-denial chronology in a way that implies the court action concerned migration views unless a source explicitly establishes that relationship.
- Update or remove stale wording only after the primary legal record has been checked.
- Record the correction in the universal correction register and scan related pages, metadata, timelines, captions and Sources entries.

### E. Headline and claim-strength audit

- Audit forceful headlines independently of their page disclosures. A qualification below the fold does not cure a headline that states more than the evidence supports.
- Build a list of headlines whose rhetoric may outrun the underlying source record, starting with “Caste was abuse, encoded as law, disguised as religion.”
- For each, identify whether it is a documented quotation, a synthesis, an interpretation or a rhetorical thesis.
- Preserve force where supported. Do not flatten the museum’s voice merely because a claim is contested.
- Ensure screenshot/social-card metadata does not strip away an essential qualification.

### F. Brand and naming consistency

- Establish a small naming standard for **Mela Keela**, **Veḷi**, transliterated `Veli`, and phrases such as “into Veḷi.”
- Define which is the institution, which is the threshold/space/concept, and when transliteration without diacritics is permitted for URLs, metadata, search and accessibility.
- Do not force a single spelling where technical constraints require ASCII, but prevent unexplained mixed forms on the same visitor surface.

### G. Progressive enhancement and accessibility

- Verify each JS-dependent instrument with JavaScript disabled, keyboard-only use and a screen reader before accepting the assessment’s claim that it is an “empty shell.”
- The Atlas, Claim Inspector, Endogamy Clock and future instruments should expose a meaningful static summary or data table when scripting fails or is unavailable.
- Provide stable links to the underlying data independent of the interactive layer.
- Ensure dynamic state changes have programmatic names, focus management and live-region behavior where appropriate.
- Do not assume that a JS interface is inaccessible merely because it is JS; test the actual rendered accessibility tree and fallbacks.

### H. Learning and onboarding

- Replace the empty Learn state with a useful minimum experience.
- Candidate first release: three short guided paths—“Caste in the counts,” “Who was at Rakhigarhi?” and “One Tamil text”—plus a glossary.
- Define varṇa, jāti, gotra, śramaṇa, AASI, Steppe_MLBA and other specialist terms on first meaningful use or through accessible inline definitions.
- Support time-boxed visits such as “start here in 10 minutes” without turning the entire museum into a school lesson.
- Later option: teacher-created source sheets or reading paths, provided source versions and claim IDs remain stable.

### I. Museum objects and evidence-led visuals

- The assessment reinforces the existing finding that the site often behaves like an essay collection rather than a museum.
- Prioritize a small, rights-cleared object set before attempting large immersive reconstructions: seals, sherds, inscriptions, burial plans, excavation drawings, manuscript leaves, instruments and trade objects.
- Every object should have identity, date/range, provenance/custody, institution/source, rights, alt text, caption and links to the claims that use it.
- Candidate later experiences: annotated high-resolution object, 3D viewer, excavation-plan layers and reconstructions with **excavated / inferred / conjectured** toggles.
- Do not accept “no images on the site” as a repository-wide fact based on a limited page sample; inventory the collection first.

### J. Strategic benchmark patterns to study

These are design references, not instructions to imitate their visual style or scope:

- **SlaveVoyages:** a filter changes the visual result and the underlying rows are downloadable.
- **ORBIS:** the interface operates a historical model rather than displaying a static map.
- **Digital Benin:** custody, naming, objects and institutions become navigable linked data.
- **Sefaria:** addressable source passages, commentary links and reusable source sheets.
- **Digital Giza / Rijksmuseum:** a visual or reconstruction links back to the archive and documents how it was produced.
- **Vesuvius Challenge:** open questions, reproducible data and external participation.
- **Attentat 1942:** evidence-led narrative can remain rigorous while becoming exploratory and emotionally engaging.
- **Smithsonian Voyager:** reusable object annotation and guided-view patterns.

Before using any benchmark, verify its current functionality, licences, accessibility, technology and relevance. The assessment’s links and descriptions are leads, not adopted specifications.

### K. Product direction emerging from the assessment

Candidate north star:

> **The museum where the evidence is the exhibit.**

Useful interpretation for later design work:

- Claims may become stable, addressable records with sources, limits, counterevidence, change history and data pointers.
- Visitor actions should operate the evidence: filter, compare, trace, count, replay or inspect.
- No-data and uncertainty should remain visible rather than being silently interpolated.
- Pages should compose claims, objects and instruments; they should not all become identical five-field forms.
- The full five-field claim structure may be available in an expandable inspector, but forcing a large card onto every page could worsen the existing text-and-template problem. Prototype before adopting site-wide.

### L. Claims from the assessment not accepted without evidence

- The estimated team size, production time and USD 500k–1.1M replacement cost are speculative and should not enter the implementation brief.
- “There are no objects,” “no images were visible,” and “search engines and assistive tech see an empty shell” reflect a limited audit sample and require repository/browser verification.
- “No page meets source-audited standard” describes the current register policy, not necessarily the intrinsic reliability of every page.
- A high proportion of disclosed pages does not by itself mean the labels are bad; the visitor-language, placement and necessity must be reviewed page by page.
- Naming individuals is not the only route to accountability; any solution must balance credibility, privacy, safety and legal responsibility.
- `naú-/nā́v-` occurrences alone do not settle the narrower proposition “seafaring”; the underlying passages and category definition must be audited.

## 14. New audit workstreams implied by the assessment

Do not start these until the owner authorizes an implementation/audit phase:

1. **Generated-count audit:** Atlas, Research Index, search, sitemap and corpus counts.
2. **Internal-contradiction audit:** page claims against shipped corpora/data and related exhibits.
3. **Publication-residue audit:** conversational language, internal workflow labels and private-source traces.
4. **Named-person/legal-framing audit:** precise event, quotation, attribution, inference and right-of-reply review.
5. **Reproducibility audit:** public download, rerun, versioning, licences and checksums for every instrument.
6. **Headline-strength audit:** headline, social metadata and evidence-strength alignment.
7. **Progressive-enhancement audit:** no-JS, accessibility-tree and static-data fallbacks.
8. **Brand-language audit:** Mela Keela / Veḷi / Veli usage.
9. **Visual-evidence inventory:** existing images/objects, rights status and gaps.
10. **Learning-layer definition:** audience, glossary and first three guided paths.

## 15. Critical entry-page redesign — owner direction

### Veḷi threshold

- The threshold should become a more compelling visual and spatial experience, not a text-heavy explanation of the platform.
- It remains a threshold rather than a conventional homepage: no standard internal header and no redundant Mela Keela logo treatment.
- Use a restrained visual transformation, motion or reveal that makes the meaning of veḷi—open, outside, clear, light—felt before it is explained.
- Keep the passage short. Visitors should not have to read an institutional manifesto before entering.
- The continuation control must work reliably by touch, pointer and keyboard and make its destination clear.
- The threshold should create atmosphere and curiosity; it does not need to catalogue the museum.

### Enter / museum foyer

- Because every visitor has already passed through the Veḷi threshold, Enter should not repeat another abstract introduction.
- Enter is where visitors should first encounter actual museum material: objects, sites, maps, inscriptions, excavation images, manuscript fragments or evidence visualizations.
- It should orient without becoming another index. Offer a small number of strong, visual starting paths based on visitor curiosity.
- Candidate foyer paths include: **See an object**, **Follow a place**, **Test a claim**, **Trace a word**, and **Enter an exhibit**. Final labels require design testing.
- Feature a small rotating or editorially selected set of real exhibits; do not present all pages at once.
- Remove site counts, system explanations, audit mechanics and long Method copy from the foyer.
- The visual system should make the museum’s range immediately legible: archaeology, language, caste/history, genetics, texts and the politics of the record.

### Exhibits hub

- Exhibits must look and behave like a gallery of designed experiences, not a second Research Index.
- Each exhibit entry needs a meaningful visual identity drawn from its actual subject: object, site, map, text fragment, diagram or evidence pattern.
- Use curated collections and category rooms rather than one undifferentiated card grid.
- Cards should communicate a visitor proposition—what the visitor will encounter or do—not internal status, page length or repository metadata.
- Allow useful filtering by subject, period, place and experience type, but keep the default view editorial and inviting.
- The hub should highlight visual/interactive exhibits first while still making text-led essays reachable.
- Do not fabricate archaeological imagery. Use licensed evidence images, clearly labelled reconstructions or abstract/data-native visuals.
- Research Index remains the exhaustive finder; Exhibits is selective, visual and curatorial.

### Relationship among the three pages

- **Veḷi:** feel the premise and cross the threshold.
- **Enter:** see the museum’s world and choose a direction.
- **Exhibits:** browse curated, visually distinct experiences.
- These pages must not repeat the same copy, cards or visitor task.
- Explore, Evidence and Research Index remain outside this prototype scope except where links are needed to demonstrate a complete path.

### Treatment of the supplied build plan

- The six-engine/data-layer proposal is a strategic architecture candidate, not an approved immediate rebuild.
- Useful principles to retain for later evaluation: one generated number per dataset, evidence-linked visuals, stable claim/data identifiers, reusable map/corpus/sequence/object components and progressive depth.
- Do not begin bulk claim extraction, child-facing rewrites, Atlas replacement, corpus re-indexing, 3D ingestion, AI docent work or repository-wide component migration as part of the three-page redesign.
- Do not force a large claim card above every h1; this could intensify the current templated, text-heavy experience. Prototype claim inspection in context first.
- Any prototype should use the current repository and existing data/assets, preserve public routes and remain isolated from production until owner approval.

## 16. Children’s product and funding dossier — proposed, not adopted

### Strategic proposition

- Treat the children’s experience as a possible second product using the same evidence layer—not as a simplified duplicate of the adult museum.
- Its central action is investigation: children excavate, compare, question sources and reach conclusions at the strength supported by the evidence.
- The strongest product distinction is teaching **how people know about the past**, rather than presenting another set of historical conclusions.
- Do not let this proposed product delay or absorb the current adult-site review, entry-page redesign or correction work.

### Product boundary proposed for evaluation

- Phase-one audience: ages 8–11 only.
- One vertical slice: one site, one dig, one mystery, one evidence card system and one on-device Field Bag.
- Keezhadi is the preferred candidate only if suitable image/object rights and adequate evidence records can be secured. A Tamil-Brahmi cave inscription is a proposed fallback.
- No child accounts, public child profiles, public user-generated-content feed, leaderboard, streaks, coins, XP, confetti or manipulative engagement mechanics.
- Persistent state should remain on-device in the first phase. Any classroom sharing should be teacher-controlled and reviewed.
- English/French may be necessary for a Canadian funding application; Tamil must be treated as a first-class data and design requirement rather than a late translation layer. Exact launch languages remain undecided.

### Evidence rules worth carrying forward

- The child certainty display must derive from the same adult evidence record; never maintain a parallel truth/status system by hand.
- Colour must never be the only carrier. Use consistent text and symbols for directly found evidence, supported inference, disagreement, unchecked material and no data.
- “I don’t know” is a legitimate conclusion and must not be penalized against an unsupported guess.
- Different conclusions are not automatically equally good. The product should assess whether the child cited sufficient and relevant evidence—not reward confidence or ideological agreement.
- Every claim needs an accessible **Prove it** route; every source needs a child-appropriate **Who made/wrote this record?** route.
- No migration arrows, no ethnonyms attached to ancestry components, no conversion of statistical components into internally uniform peoples, and no reconstructed scene presented as excavation fact.
- Reconstructions must visibly distinguish attested/excavated, inferred and conjectured elements.
- Child-facing text should be a controlled rendering of the same record, with human review; it must not become a second untracked set of claims.

### Candidate vertical-slice sequence

The dossier proposes a testable sequence rather than a full children’s platform:

1. A visual door offering a small number of actions.
2. South-up map introduction and optional orientation flip.
3. Simplified but honestly labelled trench grid.
4. Tactile/keyboard excavation reveal.
5. Real object image or explicitly labelled illustration.
6. Evidence card with found / supported / disputed / unknown distinctions.
7. Stratigraphy task including a disturbed-layer complication.
8. One investigation—provisionally “Could they read?”—using conflicting evidence.
9. On-device Field Bag connecting the collected records.
10. “Do not touch” route to a safe random record.
11. Teacher page with a 40-minute lesson and evaluation materials.

This is a concept for testing. It is not authorized for production and must be checked against the adult entry-page redesign so the two experiences do not compete or duplicate one another.

### Rights and safeguarding gates

- Image and object rights are likely the practical critical path. Begin no evidentiary object experience without an explicit rights record covering web display, interaction, derivative crops/annotations, languages and child-facing use.
- Prefer open-access or permission-cleared photographs and scans. Never substitute AI-generated archaeology for a real evidentiary object.
- Preserve custody/provenance information when using objects held outside their place of origin.
- Before any child testing or school partnership: safeguarding policy, parental consent process, privacy/data map, moderation boundary, accessibility plan and incident/escalation contact.
- Children’s privacy requirements must be reviewed for the jurisdictions actually served; the dossier’s references to PIPEDA, Quebec Law 25, COPPA, GDPR-K and the UK code are issue flags, not a completed legal analysis.

### Learning evaluation

- Candidate outcomes: distinguish observation from inference; ask who created a record; accept uncertainty; understand simple stratigraphy and disturbance.
- Test learning through a small pre/post task and observed use, not engagement time alone.
- An external education/museum-learning partner or evaluator is desirable so the platform is not grading its own product.
- Verify the licence and suitability of any adapted assessment instrument before use.
- Children and teachers should participate in design testing, but recruitment, compensation, consent and safeguarding must be properly resourced.

### Funding architecture — strategic option

- The dossier proposes a Canadian non-profit/charitable core, academic partnerships for research grants and a commercial subsidiary only if commercial revenue or programme eligibility later requires it.
- This structure is **not adopted**. Obtain Canadian charity, corporate, tax and intellectual-property advice before incorporating multiple entities or promising that profits can flow between them.
- Do not create a subsidiary merely to chase a grant or tax credit.
- Funding must not constrain findings, source access, editorial conclusions or correction publication.
- Government or institutional rights/data partnerships must be contractually separated from editorial control.
- Any application must disclose actual governance, capacity, ownership, partner commitments, rights status and project readiness accurately.

### Funding leads requiring fresh verification

Treat all amounts, deadlines and eligibility statements in the dossier as leads until checked directly against the current programme rules:

- Digital Museums Canada Digital Projects and Community Stories
- SSHRC Partnership Engage / Connection / Partnership Development
- Mitacs Accelerate
- Canada Media Fund programmes
- Ontario Trillium Foundation
- Ontario Creates and OIDMTC
- SR&ED
- Jacobs Foundation / Digital Museum of Learning / LEVANTE
- LEGO Foundation Fellowship
- Spencer Foundation
- Horizon Europe Cluster 2
- NEH Digital Humanities Advancement Grants
- Wikimedia and UNESCO routes

Priority verification questions:

- Is the stated 1 December 2026 Digital Museums Canada deadline current and confirmed?
- Is a web-native museum without a physical collection eligible, and under which legal form?
- Are bilingual delivery, agency procurement, accessibility and advance-payment descriptions accurate?
- Can the current organization apply before charitable registration?
- Which costs and in-kind founder labour are eligible?
- Does any proposed partner or subsidiary arrangement affect control of data, IP or editorial independence?

### Financial and operating caution

- The Phase 0–3 budgets are preliminary planning ranges, not validated quotes.
- A CA$150k–300k vertical slice is far beyond what should be committed before rights, eligibility, scope and partner assumptions are confirmed.
- The dossier assumes agency delivery; compare agency, small specialist team and internally led prototype scenarios before choosing.
- Founder capacity is a major constraint. Do not run adult-site remediation, claim/data restructuring, incorporation, grant writing, school recruitment and a child PWA build as one simultaneous critical path.
- The first financial gate should be a low-cost feasibility package: rights responses, eligibility confirmation, one interaction prototype, curriculum check, safeguarding outline, partner interest and a credible quote.

### Contradictions and stale premises to resolve

- The dossier says the project is missing a repository and tests, but the current Claude Code work reports a Git repository and extensive validation suites. Reconcile against the actual current branch before using this language externally.
- The dossier cites an Atlas dataset of **194 sites / 315 windows**, while other live and review materials cite 140, 158 and 175 sites. This is another unverified count, not the canonical correction.
- The dossier refers to 480→758 corpus files and 145 `assumed` Atlas rows. Recompute from canonical data before including them in a grant.
- “Verified” cannot be used as a child certainty label if the adult evidence register does not support that exact status. The mapping must reflect the finalized vocabulary and access level.
- The dossier simultaneously says Phase 1 is English/French and later describes the case for support as English/French/Tamil. Decide the funded delivery languages and budget them consistently.
- The phrase “the first children’s history product” is a market-superiority claim requiring evidence; avoid in applications unless substantiated.
- Curriculum statements for England, Ontario, Australia, India, Tamil Nadu and Sri Lanka require current primary curriculum documents and exact grade/expectation citations.

### Decisions reserved for the owner

1. Whether the children’s strand becomes a second funded product now, remains a later layer, or receives only a feasibility prototype.
2. Whether the child product communicates the platform’s position primarily through investigative mechanism rather than direct editorial assertion.
3. Whether to retain the internal codename `DIG`, investigate a Tamil action name, or defer naming entirely.
4. Whether and when to incorporate a non-profit; governance and board composition.
5. Keezhadi versus Tamil-Brahmi inscription for the first slice.
6. Which academic, school/library and cultural partners may be approached.
7. The boundary between data/image partnerships and editorial independence.
8. Whether the December funding timetable is realistic without derailing the adult museum.

### Recommended decision sequence before any build

1. Verify the funding programme and eligibility directly.
2. Verify the canonical repository/data state and correct the dossier’s stale counts.
3. Decide whether only feasibility work is authorized.
4. Audit rights availability for the two possible first subjects.
5. Obtain preliminary safeguarding/privacy advice.
6. Produce one small interaction prototype using cleared material.
7. Test it with adults/educators first; involve children only after safeguarding is ready.
8. Obtain delivery quotes and then decide whether to apply and incorporate.

## 17. Proposed merged project instructions — conflicts and usable rules

The supplied `MELA KEELA — PROJECT INSTRUCTIONS` document is an important source of editorial intent, but it must **not** supersede the current repository rules unchanged. It mixes enduring principles, outdated project state, disputed historical conclusions and proposed branding decisions.

### Carry forward as governing principles

- Identify material claims and confirm that cited sources support them before substantive publication changes.
- Distinguish direct observation, model, inference, hypothesis, interpretation, community testimony and established finding.
- State material sample, geographic, chronological and representativeness limits.
- Do not generalize from one individual, site, text, lineage or study beyond its evidentiary scope.
- Never translate Y-chromosome or mtDNA frequencies into genome-wide ancestry.
- Do not turn ancestry components, language families, castes, tribes or civilizations into uniform biological peoples.
- Present serious counterevidence and specify what would change an assessment.
- Never invent a quotation, citation, provenance, comparison, number or consensus.
- Record the level at which each source was actually accessed.
- Apply symmetrical evidentiary scrutiny to claims and objections.
- Treat archival silence cautiously where preservation, excavation, publication or institutional suppression can be demonstrated; silence permits uncertainty, not invention.
- Treat the large research deck as a question/pointer archive, never as a publishable source or image-rights repository.
- Apply every correction across pages, headings, metadata, captions, graphics, data, indexes and future work.
- Preserve user decisions separately from model recommendations and obtain owner approval for substantive public changes.
- AI may propose, organize and help visitors inspect evidence, but may not autonomously publish scholarship.

### Conflicts that must be resolved before adoption

- **Brand contradiction:** Part A says the relationship among Mela Keela, Veḷi and Tuṟai is unresolved; Part F declares the name is Veḷi. Current owner direction uses Mela Keela as the museum and Veḷi as its threshold/concept. No instruction file may silently rename the project.
- **Publication contradiction:** Part E pauses repository-wide editorial changes based on a model switch, while the owner has explicitly authorized continued public publication and later corrective work. Model identity may be recorded, but it does not independently determine publication policy.
- **Stale scale:** the document repeatedly describes 58 pages, while the integrated public site now reports 133 routes/pages. Every inventory and work-order assumption must be regenerated from the current branch.
- **Stale cascade state:** the listed `the-killed`, `the-names` and `brahmi` failures must be checked against the current live files before being called unresolved.
- **Reproducibility overclaim:** “every claim is a query someone can re-run” remains an aspiration until the visitor can access the necessary data, query, version, method and instructions.
- **Template conflict:** mandatory claim/status structures on every page could reproduce the exact meta-heavy, repetitive experience the owner wants removed. Evidence access should be contextual and expandable.
- **Arbitrary design rules:** 30 KB, maximum two rust boxes, and “three tables require a chart” may be useful lint warnings but are not universal quality laws. They must not force artificial page splits or decorative charts.
- **Status/history conflict:** “most of the 58 pages were built without review” is historical process information, not suitable visitor-facing language and not a reliable description of the current 133-page site.

### Historical assertions that require audit rather than adoption as instructions

- Part G states major propositions about Vedic migration, enemy populations, varṇa, caste construction and religious transmission as settled platform positions. These are editorial theses; each load-bearing component must still comply with the evidence rules above.
- “Three enemy names Sanskrit cannot parse,” the counts for Sindhu/Sarasvatī/Ganges and the precise chronology of the west-to-east movement must be linked to reproducible corpus definitions and source access records.
- “The officiant took control of the record, the law and the land” is a broad synthesis requiring chronological and regional specification.
- Claims that several practices are “none Vedic in form” must distinguish absence in particular corpora from historical origin or later development.
- “Everything that damages the received account is contested” and related institutional-cost language may guide adversarial review but cannot replace documented reception evidence.

### Rakhigarhi / Indus Periphery clarification

- Preserve the key distinction: one sampled Rakhigarhi individual is directly from Rakhigarhi; the additional individuals come from Gonur and Shahr-i-Sokhta and are modelled as an Indus Periphery-related cline.
- Do not collapse all twelve into “twelve Rakhigarhi individuals” or imply that every individual was excavated within the IVC heartland.
- Do not reduce the evidence to the single Rakhigarhi individual either. Explain the combined inference and the different archaeological provenances.
- The deck’s statement about Irula affinity is not enough to reverse the audited correction to `the-proxy`. The exact population comparison, statistic, source text and scope must be recovered before any living community is presented as a proxy or closest carrier.

### Brahui and Para-Munda cautions

- The late-migration and relict hypotheses for Brahui must be evaluated using comparative linguistics, documented historical evidence and present-day genetic results; counting assumptions rhetorically does not settle the question.
- An alleged Tulu–Brahui affinity from an unattributed deck slide is not evidence until the linguistic method and source are identified.
- Modern Brahui genetic similarity to neighbouring Balochi/Sindhi populations does not directly determine when the language arrived, but it constrains simplistic population-continuity narratives.
- Para-Munda and Dravidian proposals should be compared under the same evidentiary criteria. Claims of unequal scholarly treatment require an actual citation/reception history rather than presumed career incentives.

### Copy and framing principles retained with limits

- Lead with concrete evidence, names and actions rather than abstract meta-language.
- Keep agents visible where the source establishes agency.
- Use short, high-weight headings, but do not let forceful rhetoric outrun source strength.
- Avoid vague terms such as “contested”; name the position, evidence and unresolved test.
- Avoid passive formulations that obscure documented institutional action.
- Do not ban individual words mechanically. Terms such as “indigenous,” “substrate,” “invasion” or “Vedic period” may be necessary in attributed, technical or historiographic contexts and should be qualified rather than globally prohibited.

### Design principles retained with limits

- Dark, spacious composition; one primary action or evidentiary idea at a time.
- Motion should resolve or reveal evidence, not decorate.
- Grey should consistently represent unavailable/unmeasured/unknown information where that semantic mapping is used.
- Colour must carry meaning and remain accessible without colour perception.
- Exact diacritics and Tamil rendering are mandatory.
- Charts must state units and must not show directional movement unless supported.
- Every motion needs a reduced-motion treatment.
- Technical robustness requirements should live in tested shared components rather than being copied inline across every page.

### Content backlog captured, not authorized

Potential future research/exhibit subjects from the deck-gap analysis:

- Archaeobotany and food/crop dispersals
- Nāga traditions, carefully separating religious/narrative usage from northeastern ethnonyms
- Community histories and testimony, beginning only with ethical consent and source controls
- Ājīvika/Āsīvakam and other śramaṇa traditions
- Embodied traditions and custody/transformation of dance or martial practice
- Theosophy and colonial institutional networks
- A public-facing method/orientation experience
- Countable Aśokan, Pali, Sangam and other corpora
- Isotope and palaeopathology evidence
- Southeast Asian archives presented on their own terms
- Visual archive with documented provenance and rights

These are research leads. None should become a page from deck slides alone.

### Image-deck rule

- Do not publish any of the 716 deck images without locating the original record and verifying creator, institution, licence and permitted use.
- Use the deck only to identify candidate objects, maps, sites and figures.
- Prefer rebuilding maps/charts from cited data, open-access museum records or commissioned/self-made photography.
- Journal figures, unattributed site photographs and screenshots should not be reused merely because they are embedded in the deck.
- Maintain an asset-rights register for every image ultimately selected.

### Work-order integration

- Do not reintroduce the obsolete “build all pages first, design later” sequence. The current priority is correcting and improving the live visitor experience while research continues in controlled batches.
- Claims/data structure, reproducibility and correction tooling are foundation work, but they should not block the visual redesign of Veḷi, Enter and Exhibits or a small evidence-safe `/kids/` preview.
- New content research remains a separate stream from design/integration so unsupported claims cannot enter merely to fill visual gaps.
- Before turning this dossier into a repository instruction file, reconcile it line by line with the owner’s current policy, the post-integration repository state and the master running work list.

## 18. The “108-route true state” report — historical checkpoint, not current inventory

This report corrects a real earlier mistake: Claude had treated 58 files in its working folder as though they were the whole platform. They were a subset. However, the report’s own 108-route snapshot predates the subsequent integration that reported 133 site pages. It therefore cannot be treated as the current canonical state either.

### Inventory rule

- Keep three states distinct: the historical 58-file working subset, the live deployment at the time of inspection, and the current repository branch.
- Generate the authoritative inventory from the current branch’s files, route/register data, redirects, sitemap and search index. Do not infer it from `enter.html`, one route list, an old ZIP or an earlier deployment.
- Compare the current branch with `melakeela.com` explicitly before release. Report deployment drift rather than calling either state current by assumption.
- Generate all page, route, Atlas, search and sitemap totals from their source data. Never type those totals into visitor-facing copy.
- A future `inventory.json` should record, at minimum: route, source file, page type, topic tags, aliases/redirects, public/index/search/sitemap/menu states, disclosure/status, last content-changing commit and deployed-versus-branch state.

### Correct the scope of older documents

- Add a clear archival scope note to `MANIFEST.md`, `HANDOVER.md`, the old work order and the earlier deck-gap analysis wherever they describe the 58-file subset as “the platform.”
- Preserve those documents as historical records; do not silently rewrite them to look prescient.
- Re-run coverage and gap analysis against the current canonical inventory before declaring any subject absent.

### Reconcile the 21 reported “orphans”

Do not assume these pages are missing or automatically restore them. For each, classify it as: current route · renamed or redirected · integrated into another page · superseded · internal-only · duplicate · or genuinely absent material.

- **Linguistics:** `panini` · `two-classical-languages` · `who-had-it-first` · `mlecha` · `the-gap` · `isnad` · `attribution` · `collocations`
- **Textual history:** `the-edits` · `the-insertions` · `who-is-speaking` · `brahmavadini` · `the-renaming` · `not-the-same-thing`
- **Material/economic:** `what-they-had` · `the-land` · `paid-in-cattle` · `the-forts` · `elamite` · `dravidian-sky`

Pending source and corpus verification, protect the distinctive material associated with `collocations`, `who-is-speaking`, `what-they-had` and `the-forts` from accidental loss. Their quoted counts and interpretations must be rerun before reuse.

### Structural pages: existence does not settle purpose

The report confirms that `the-ledger`, `sources`, `research-index`, `search`, `explore`, `exhibits` and `enter` existed at that checkpoint. That does not resolve the owner’s current UX findings:

- Research Index and Exhibits still need clearly different visitor purposes.
- Enter, Explore, Evidence and related labels need plain, predictable meanings.
- Page-count and method blurbs should not occupy prime visitor space.
- The foyer and Exhibits still need a visual, object-led museum experience.
- The full-page inventory belongs in organized navigation/search, not repeated explanatory prose.

### Coverage claims retracted or downgraded

- Earlier declarations that Āsīvakam, folk religion, Vedda and other communities, forest peoples, lost languages, materialists, medicine, Rakhigarhi or Keeladi were absent were not supportable from the 58-file subset.
- Nāga traditions, arts/body, food/archaeobotany and material culture remain possible gaps only. Verify them against the current inventory and page contents before adding them to the content backlog as confirmed absences.
- Never infer what a page contains from its slug. Statements such as “`the-father-tongue` is presumably…” are leads, not findings.

### Historical Atlas and verification claims

- The report’s “140 sites / 299 windows” is another dated Atlas snapshot, not a canonical figure. Other documents cite 150, 158, 175 or 194 sites and 315 windows. Compute today’s count from the current Atlas dataset and feed every display from that one source.
- The report’s praise of verification badges is limited to what was visible at that checkpoint. Later audits found and corrected misleading verification/source-review language; do not reinstate it.
- “The five-field claim structure appears on every entry” requires an actual completeness test. Even where the data exists, do not force repetitive method cards or meta-copy into the top of every visitor page.
- The empty Learn room is a historical observation and a current product opportunity, not a virtue to preserve after useful child and teacher material is ready.

### Implementation boundary

This report authorizes no new page, route restoration, content resurrection, deployment or publication change. Its immediate output is a current-inventory audit and a page-by-page orphan reconciliation. Any recovered material then enters the ordinary evidence, correction and curator-review workflow.

## 19. Institutional vision versus execution architecture — synthesis for review

**Source:** The owner supplied the original thirty-part institutional vision and a comparison proposing a VELI-12A amendment. The complete underlying Claude master plan was not supplied in this turn. Assessments of that plan are therefore limited to the excerpts and descriptions provided.

**Status:** Proposed architecture and diligence work. This section does not ratify a legal structure, rename the museum, establish councils, commit funding, or supersede the current site redesign. The accompanying one-page PDF is a discussion artifact, not a production specification.

### Comparative judgment

The original is strongest at explaining what people could experience: living questions, continuity and change, curiosity, and movement between ancient evidence and present life. The merged proposal gives those experiences a more coherent evidence and interaction structure. Its missing layer is an operating case: scope, cost, staffing, ownership, measurable outcomes and cash timing.

Neither architecture quality nor funding readiness can be scored credibly at 9.5 or 10 from these narratives. Replace the self-awarded scores with testable milestones and a decision log.

### Brand and visitor experience

- Preserve the current distinction: **Mela Keela is the museum; Veḷi is its threshold and organizing concept.** “Veḷi is the institution and ledger” remains a possible future institutional arrangement, not an approved name or legal entity.
- Retain Living Worlds/questions as visitor entrances alongside places, periods and objects. Water, Food, Word, Home, Movement, Body & Mind, Nature, Work, Belief, Power and Play are candidates, not a launch menu requiring twelve completed programmes.
- Follow the current design doctrine: objects remain situated in place, ecology, material, makers, community and use. A graph should preserve those relationships rather than turn the museum into an abstract network of detached records.
- Keep the existing adult museum, entry-page redesign and corrections moving. The future investigation product must not absorb their capacity without a deliberate scope decision.
- Cognitive depth, language, audio, accessibility and classroom/family context are separate design dimensions. They can reuse evidence without requiring a visible global mode switch. This qualifies the age-coded proposal in section 16; a primary test cohort remains to be selected.
- PROVE IT should open specific relevant evidence in context. Do not restore obligatory large claim cards, repeated method explanations or depth toggles across every page.

### Canonical structure and evidence discipline

Proposed visitor path: living question → investigation → reusable interactions → inspectable records and evidence. Governance, rights, accessibility and finance operate across that system; they are not later steps in the visitor journey.

Use the more defensible institutional principle:

> The record is the unit of accountability. The investigation is the unit of experience.

A record may be provisional, disputed, superseded or wrong. Storing something does not make it true.

- **Interpretive bridges are claims.** A proposed relationship from archaeological culture to language, ancestry or modern identity needs explicit support and limits. Routine links such as “uses this image” or “has this stable identifier” do not need an invented historical argument.
- Evidence role belongs to the evidence-to-claim relation: supports, contradicts, contextualizes, dates, localizes or identifies, with an explanation and source locator. Strength and discriminating power are separate attributes; “suggests” should not silently stand in for calibrated confidence.
- Material, textual, epigraphic, biological, linguistic, environmental and oral/living categories describe overlapping methods or source types. “Contemporary” describes time or context and may overlap all of them. Preserve the proposed eight labels as a useful vocabulary, but test the schema against real records before treating them as mutually exclusive classes.
- Keep source reliability, claim status, evidential strength, dating uncertainty, geographical uncertainty and interpretation distinct. One certainty badge cannot represent all of them.
- Derive public adaptations from shared record IDs and versions, with human editorial review. Research updates should identify affected public claims, media captions and learning activities for correction.
- Use relational tables or versioned structured files initially if they meet the need. A connected data model does not itself require a dedicated graph database.

### Smallest complete product and build order

The two texts count engines differently and mix engines, controls, modes and workspaces. Do not convert the nine-engine taxonomy into nine engineering commitments.

1. Inventory and select a bounded set of existing records; establish IDs, schema, source locators, uncertainty, rights and revision handling.
2. Build one complete investigation using WITNESS, contextual PROVE IT and an on-device Field Bag. The loop is inspect → compare → conclude → save → reconnect.
3. Connect those same records to a small TIME·PLACE view. Scale atlas coverage only after date ranges, geographic precision and source quality are reconciled.
4. Add DIG when it improves the chosen investigation and suitable evidence/media rights are available. Do not fabricate stratigraphy or findings to make excavation playable.

WATER / Dholavira is an example in the architecture sheet, not a commitment to replace Keezhadi or the inscription fallback. Select the pilot on evidence readiness, rights, learning value and implementation cost.

Proposed pilot acceptance evidence:

- A visitor can explain the question, inspect a source, identify a limit, make a supported conclusion, and recover a saved clue without facilitator rescue.
- A second small case uses the same interaction code; document the content work required and whether new bespoke code was needed.
- Every consequential pilot claim resolves to a reviewed record and source locator; visible reconstructions identify inferred elements.
- Keyboard, mobile and chosen assistive-access paths work through the complete experience.
- Record completion, points of confusion, source inspection, conclusion quality and production effort. Small usability sessions diagnose design problems; they do not establish educational efficacy.

### Governance and IP

- Start with named responsibilities and a small accountable operating group. The proposed four to six executive roles are functions, not a Year-1 salaried staffing plan.
- Separate budget/product decisions, scholarly review, rights/consent decisions and learning evaluation. Define who resolves disagreements and the review turnaround expected for a release.
- Apply editorial independence to every donor, government, university and company. Funding terms must not purchase privileged evidence treatment or pre-publication control.
- Community consent should govern contributed/restricted knowledge, privacy and appropriate use. Establish scope, representation and an appeal route; it is not an unrestricted veto over discussion of public historical evidence.
- Children’s co-design findings can be published as anonymized changes and responses. Publication of raw identifiable notes is not required for accountability.
- Health-practice material documents history and living practice. Clinical efficacy requires separate contemporary evidence and review; antiquity does not establish medical benefit.
- Decide ownership of founder material, commissioned work and improvements before a funding agreement or production contract. Deferring a blanket open-source licence is sensible; deferring ownership is not.
- Open data/content only where rights and consent permit. Do not promise CC0 for third-party metadata or unrestricted reuse of community knowledge. Resolve licensing for the engine, authoring system and institutional implementation separately.
- Treat named academics and institutions as prospective relationships until they have agreed to a defined role. Do not use them as a confirmed advisory board or display partner logos without agreement.

### Funding verification — checked 4 September 2026

**DMC:** Digital Projects is marked closed; its page says the displayed rules are reference material pending a 2027 call. Those rules require qualifying legal status for at least one year when applying. A September 2026 incorporation therefore does not establish a December 2026 route. Treat 2027 as conditional on the eventual call and eligibility review. Published funding is released by approved phases, which matters for cash timing. [DMC Digital Projects](https://www.digitalmuseums.ca/funding/digital-projects/)

**CMF:** The fall Prototyping window is October 27-November 10, 2026. [CMF deadlines](https://cmf-fmc.ca/our-programs/program-deadlines/)

Its core rules exclude nonprofits as direct applicants, require an eligible Canadian-controlled producer/broadcaster, qualifying full-time professional experience in a shareholder, necessary project rights, and a consultation for new applicants. Consultation requests are due at least two weeks before the deadline. Support is a repayable advance under specified conditions. An NPO/company partnership is not an automatic workaround. [CMF IDM core rules, sections 3.1 and 4.1.1](https://cmf-fmc.ca/document/idm-core-guidelines/)

The ordinary Prototyping limit is the lower of 75% of eligible costs and $250,000; the project must still need a subsequent production phase. This is a funding lead requiring entity, project and experience validation. [CMF Prototyping rules](https://cmf-fmc.ca/document/prototyping-guidelines/)

### Financial reconstruction and working capital

The supplied strategy contains capacity ambitions, not accounts or a financed plan. Current cash, founder hours, paid development costs, revenues, unrestricted donations, liabilities and signed commitments were not supplied. The proposed $50,000-$250,000 of first-year capacity and larger later funding ranges are scenarios, not forecasts or valuations.

Build a bottom-up pilot budget covering research and review, rights/media, UX/development, learning evaluation, translation/accessibility, administration and maintenance. Show founder hours at replacement cost separately from cash spending. Do not assume those hours qualify as a funder contribution.

Illustration only: a $100,000 eligible budget at a 75% funding share leaves $25,000 of other eligible financing to secure, before ineligible costs and payment timing. This is arithmetic, not an estimate of Mela Keela’s costs or likely award.

Maintain a rolling 13-week cash forecast. For each payment period show opening available cash, committed receipts, payroll/contracts, rights and other outflows, restricted cash and closing available cash. Peak financing need is the maximum cumulative cash shortfall plus the chosen reserve. An award headline and in-kind labour do not establish spendable runway.

| Scenario | Assumption | Operating response |
|---|---|---|
| No award | No new external funding | Limit commitments to available unrestricted cash; continue current-site fixes and a small evidence/experience demonstration. |
| Funded but delayed | Approved receipts arrive later than planned | Rephase contracts or secure an explicit bridge; calculate the cash shortfall before expanding staffing. |
| Pilot funded and successful | Scope financed and acceptance evidence obtained | Add a second case, measure reuse and authoring effort, then decide whether more engines are justified. |

### Strategic options and systems

- **Buy:** use established commodity tools for infrastructure, authoring and administration when they fit; no evidence currently supports an acquisition.
- **Fix:** correct and improve the existing public museum while validating its inventory and reusable evidence. This is the immediately actionable asset base.
- **Build:** develop the distinctive evidence-to-investigation experience in a bounded pilot. Broader platform licensing remains an unvalidated commercial option.
- **Walk/defer:** decline financing arrangements that undermine independence, require unsuitable ownership changes or leave an unfunded cash gap. Defer nine-engine production, multiple salaried councils and a SaaS forecast until the pilot supports them.

Keep the operating system small: one inventory, one claim/source/rights register, one correction history, one decision/ownership log, one milestone budget and cash forecast, and one usability/evaluation log. Record partner status as target, contacted, interested, scoped or committed. Link records by stable IDs; avoid parallel manual versions of the truth.

### Proposal design implication

The one-page architecture aligns the team. The external showcase should then demonstrate four things visually: what exists, one proposed visitor journey, the reusable mechanism behind it, and a specific funded milestone with acceptance evidence. Distinguish observed current screenshots, labeled interface concepts and later possibilities. The legal identity and institutional organization should remain explicit decisions; aspirational names, future features and funding leads must not appear as existing commitments.

## 20. Ancient subaltern history and intellectual provenance — core programme

**Owner direction, 5 September 2026:** Ancient subaltern history is a major part of Mela Keela and Veḷi. The supplied sixteen-section proposal must receive deep, evidenced analysis and cross-comparison across regions and periods, explicitly including Greek–Sanskrit and Latin–Sanskrit alongside English–Sanskrit. Sections 4, 5, 7, 9, 11, 13, 15 and 16 require distinct feature treatment. This is a core research/content direction, not merely a future method-page idea.

**Companion research artifact:** `MELA-KEELA-WHO-MADE-THE-PAST.md` and its PDF contain the comparative synthesis, source links/access limits, all sixteen section dispositions, eight feature briefs and build dependencies. The research foundation and this work-list integration are completed. Specialist case dossiers and production features remain to be developed; no site deployment or historical-claim publication occurred through this task.

### Governing purpose

**Who Made the Past?** Investigate who produced knowledge, who carried it, what survived, who could authorize it, and who eventually received credit. Apply this programme across Food, Water, Body, Mind, Work, Language, Power, Movement, Nature and the other Living Worlds, as well as through one recognizable curated collection.

- Distinguish creation, transmission, preservation, canonization and attribution. Language of surviving record does not establish the origin of every idea it contains.
- Restore evidenced contribution without inventing a replacement origin mythology. Record unknown makers and missing links honestly.
- Apply symmetrical evidentiary questions while preserving asymmetries of power, responsibility and access to evidence. Do not flatten documented coercion into generic uncertainty.
- Treat synthesis, consent, access, credit and benefit as separate questions. Creative transformation can coexist with coercion or unequal attribution.
- Treat “ancient subaltern” as a relational research question about power and representation, not one timeless caste, race or population.
- Include agency, craft, teaching, adaptation, resistance and collective invention. Marginalized people must not appear only as victims or absences.
- Bring anti-caste intellectual histories, community knowledge and feminist/material histories into the programme alongside Guha, Spivak, Chakrabarty, Trouillot and related scholarship. Do not imply this work began in 1982 or that Mela Keela invented it.
- Study the museum’s own selection, language, translation and attribution through the same evidence procedures.

### Evidence rules made necessary by this programme

1. Replace the simple age-to-visibility gradient with question-specific temporal, spatial, material, linguistic, social and transmission limits. Do not compute a single invented historical-resolution percentage.
2. The illustrative 100-to-1 archive funnel is a thought experiment, not data. Any simulator must visibly identify assumptions and must not present outputs as measured historical losses.
3. Separate non-recording, non-survival, lack of recognition/access and documented suppression or destruction. Specify expected traces, preservation, sampling and detection before drawing conclusions from absence.
4. Orality does not imply marginality or institutional weakness. Writing does not automatically establish elite authorship, and textual prescriptions do not automatically describe actual practice.
5. Separate linguistic genealogy, borrowing/transmission, institutional analogy and retrospective classification. Neither a shared language family nor a similar institution proves the others.
6. “Bridges are claims”: similarities, chronological priority, genetic affinity and common labels cannot silently become transmission, language, religion or modern community identity.
7. Separate evidence basis, inference assessment, disagreement and review state. “Contested” is not a confidence level; a documented source can still support a disputed interpretation.
8. Record contribution roles at the evidence relation: maker, teacher, translator, editor, commentator, codifier, collector, sponsor and publisher. Do not collapse all roles into inventor or owner.
9. Keep physical custody separate from intellectual transmission. Track visibility events and shared source ancestry so repeated citations do not masquerade as independent witnesses.
10. No civilizational ownership percentages without a defensible unit and denominator. Start with bounded cases and disclose the case-set limits.

### Eight priority features

| ID | Feature | Supplied section | Required visitor outcome |
|---|---|---|---|
| AS-01 | What Can We Know? | 4 | Distinguish what a trace reveals, what is inferred and what remains unavailable; compare questions rather than rank civilizations. |
| AS-02 | How a Past Survives | 5 | Follow a documented visibility/custody history; distinguish non-recording, loss, exclusion and rediscovery. |
| AS-03 | The Same Move, Different Power | 7 | Compare authority, access, transformation and credit in two cases; identify a meaningful similarity and consequential difference. |
| AS-04 | Lives Without Names | 9 | Reconstruct evidenced work without silently assigning caste, gender, ethnicity or a first-person voice. |
| AS-05 | Admired, Then Racialized | 11, linked to 10 | Understand how admiration and exclusion coexisted; distinguish linguistic kinship from racial ideology through dated sources. |
| AS-06 | Who Made the Past? collection | 13 | Enter through work, words, objects, ideas and absences; connect existing coverage through curated routes. |
| AS-07 | Who Gets the Credit? | 15 | Inspect a contribution/transmission graph and form an attribution supported by evidence. |
| AS-08 | Many Hands, Unequal Credit | 16 | Evaluate transformation, consent, access, attribution and reward separately; recognize synthesis without erasing coercion. |

These reuse WITNESS, contextual PROVE IT, Field Bag and TIME·PLACE. They are not eight new engine commitments. DIG is optional where archaeological context and rights make it appropriate.

### Whole-programme coverage

Organize the proposed twenty-room outline into five collections: **Traces and Absences; Languages and Authority; Knowledge and Contribution; Empire and Historical Categories; Turning the Lens Around.** Cover every supplied section through these collections and the shared evidence model. Do not create twenty thin pages simply to match the outline.

Keep Sanskrit as language distinct from the institutions and historical processes being investigated. Use Sanskritization in its technical sense where applicable; otherwise name textualization, translation, renaming, legitimation, exclusion or canonization precisely. Treat Greater Magadha as an argued model requiring passage-level comparison, not a settled origin label.

The Aryan reception history requires branching, sourced connections through philology, racialization and political institutions. Do not present Nazism as an inevitable consequence of discovering linguistic kinship, or sanitize its documented racial ideology. Contemporary nationalist claims need specific texts, editions and institutional evidence; lists of ideologies are not comparative analysis.

### Comparative research and pilot order

- **Documentary pilots:** A bounded Hortus Malabaricus contributor/entry dossier and one reviewed Florentine Codex passage. Test contribution, translation and visibility records before attempting less resolvable ancient intellectual origins.
- **Ancient material pilot:** Indus work/food/craft evidence alongside an appropriately contextualized documentary ancient case. The contrast tests historical resolution; it does not claim equivalent societies or equal representativeness.
- **Greek–Sanskrit:** Separate linguistic kinship from documented astral-science transmission and disputed textual chronology. Compare grammatical traditions by the intellectual tasks they perform.
- **Greek–Latin:** Study philosophical adaptation, audience and prestige through primary texts rather than assigning one language all originality.
- **Babylonian–Greek:** Use bounded numerical/astronomical procedures as evidence-bearing transmission cases.
- **Greek–Syriac–Arabic; Sanskrit–Persian:** Commission primary-source dossiers on named contributors, translation, transformation and institutional setting. The Persian lane remains a research requirement, not a completed case.
- **Chinese Buddhist textual transmission:** Separate composition, translation, sponsorship, copying and the survival of a particular object.
- **English publishing today:** Define a corpus and actual contribution/institution data before quantitative comparison. Keep nationality, language and intellectual ancestry separate.
- **Embodied and living knowledge:** Develop specific cases of work, medicine, performance, teaching and custody with appropriate sources and consent. Do not infer unbroken ancient descent from modern resemblance.

### Integrate with existing work before creating pages

The available local audit snapshot contains `the-archive`, `the-unwritten`, `attribution`, `indology`, `panini`, `who-is-speaking`, `the-eastern-tradition` and `the-ledger` precursors. Reconcile them against the actual branch and deployment. These observations do not establish the present production state.

Review candidates include sweeping discipline-origin claims, blanket comparisons about intellectual work outside South Asia, unsupported chronological alignment, corpus findings generalized beyond their denominator, and a debated eastern-origin model written as a categorical conclusion. Preserve earlier audited corrections. Do not reopen Irula/proxy or other settled local corrections using deck assertions or generic subaltern arguments.

Avoid compulsory method cards and global depth toggles. The new programme should provide contextual evidence interactions and distinctive investigations while preserving the existing visitor-experience redesign.

### Production dependencies and completion evidence

1. Reconcile current records, routes and source assets.
2. Produce two bounded documentary dossiers with source locators, original/translated passages, relationships, dates, rights and qualified review.
3. Build the complete inspect → compare → conclude → save → reconnect loop.
4. Reuse records in comparison and time/place views; label transmission, shared source, analogy and disputed connection distinctly.
5. Add the ancient material pilot and evaluate whether the model handles unnamed contributors and genuine absence.
6. Expand only after the second case demonstrates reuse without new bespoke engine code.

Each dossier requires a named editorial owner, appropriate scholarly review, rights/consent responsibility and a correction trail. These are operating functions, not a commitment to a large salaried council. Community expertise must be credited and appropriately compensated; authority over contributed/restricted knowledge must have a defined scope.

Acceptance evidence should assess whether visitors can identify an unsupported bridge, distinguish attestation from origin, recognize non-author contributions, state a limitation and recognize a well-supported conclusion. Small usability sessions diagnose interaction problems; they do not demonstrate general educational efficacy.

Track research, review, rights, translation, authoring and correction effort per case. Do not invent an institutional budget or financial return before these costs and funding commitments are established.


## 21. Who Mapped Speech? — language science, Tamil and AI

**Owner direction, 5 September 2026:** Add the full supplied language-science material to the critical working programme. Distinguish updates to existing coverage, new investigations, shared features, research dependencies and the Claude Chat → Claude Code workflow. Tamil grammar and AI is a priority, alongside Before Pāṇini / Before Tolkāppiyam and worldwide comparisons. This section extends section 20; it does not replace the ancient-subaltern programme.

**Status:** Coverage and production plan recorded. Two contemporary Tamil/NLP research leads checked against their publication abstracts. The many historical assertions supplied in the conversation are research inputs, not collectively verified findings. No new site pages have been implemented. Candidate titles are provisional; reconcile the current branch and deployment before assigning slugs or declaring anything absent.

**Companions:** `MELA-KEELA-CLAUDE-LIVE-SITE-AUDIT-PROMPT.md` supplies the initial public audit; `MELA-KEELA-LANGUAGE-RESEARCH-PROMPTS.md` contains nineteen bounded research prompts, one shared evidence contract, a challenge/revision prompt and a Claude Code integration prompt. `MELA-KEELA-CLAUDE-FULL-SEQUENCE.md` gives the complete live-audit-to-repository workflow. `MELA-KEELA-CLAUDE-SAY-NEXT-RESEARCH-PROMPT.md` turns that sequence into one stateful Claude Chat.

### 21.1 Priority call and central distinctions

Treat **Who Mapped Speech?** as the language-science collection within **Who Made the Past?**, connected to Language, Mind, Work, Power and Living Worlds. Make Tamil's own analytical concepts visible through their sources and examples. Do not reduce Tamil to a supporting example for a Pāṇini exhibit.

Maintain separate histories for:

- A language's changing sounds and grammar.
- Explicit scholarly models of that language.
- Scripts and orthographic conventions.
- Recitation, copying, editing and standardization.
- Institutions, multilingual contact and attribution.
- Modern computational representations and measured model performance.

Do not rank entire languages as high/moderate/low in sophistication. Compare specified phenomena and analytical tasks. Rich inflection is not a measure of total cognitive or expressive capacity. A technical marker in a grammar is not automatically a morpheme in ordinary speech.

### 21.2 Existing-page revision queue

These are candidates from earlier snapshots/reports, not a new live-site audit. Claude Code should produce the branch/production mapping before edits. A candidate absent from the local snapshot is not necessarily absent from the museum.

| Candidate coverage | Required revision or extension | Research dependency |
|---|---|---|
| panini | Separate language from grammatical technology; add worked derivations, technical notation, predecessors, later interpretation and limits of computational analogies. Remove unsupported blanket rankings or precise dating claims. | R2, R6 |
| two-classical-languages | Compare matched questions in Sanskrit and Tamil traditions; retain differences in scope, poetics and historical layers; avoid a derivation-versus-context binary. | R4, R6 |
| sound-changes; relevant phonology pages | Add sourced Vedic/Avestan correspondences and Tamil phoneme/allophone distinctions; show environments, dates, exceptions and script limits. | R3, R5 |
| Rigveda corpus; collocations; who-is-speaking | Preserve original-language reproducibility; separate family books, textual strata, recensions, editions and metrical restorations. Add the owner's retroactive-standardization question explicitly. | R3 |
| tinai; poetics-related coverage | Explain poruḷ, tiṇai, uḷḷuṟai and meyppāṭu through actual passages. Separate historical poetics, modern ecological interpretations and proposed AI experiments. | R4, R1 |
| attribution; the-unwritten; the-archive | Add the school behind a named grammarian, oral institutions, later divine attribution and manuscript/recitation histories. Unknown contributors must not be assigned invented identities. | R2, R8 |
| indology; language-classification coverage | Test Greek/Latin category transfer through actual grammars and editions. Include intellectual contributions and counterexamples as well as distortions. | R6 |
| Scripts/Brāhmī/Tamil-Brāhmī coverage; atlas | Separate script, language, sign identification, archaeological association and dating. Audit each proposed early chronology against excavation and dating evidence. | R5 |
| Rudra/Śiva; gods and renaming coverage | Trace particular names and textual attestations; distinguish Pāṇinian sound strings, later Śiva attribution and Kashmir Śaiva texts. | R8 |
| the-ledger; sources; search; research-index; exhibits | Add new records, contributor roles, research status, cross-links and collection membership; propagate accepted corrections to all affected captions and interfaces. | All packets after reconciliation |

Do not import old HTML pages simply because their slugs appear above. Match their substance to current pages, redirects and prior corrections first. Preserve current visitor-experience requirements against repetitive method cards and universal template controls.

### 21.3 New coverage backlog

**P0:** Research first because it corrects a central premise or supports a reusable pilot. **P1:** Next substantial expansion. **P2:** Specialist or evidence-dependent extension. These are sequencing labels, not judgments of intellectual importance. Each row requires an explicit disposition: extend, merge, new page, shared feature, or research hold.

| ID | Proposed investigation | Core research question and required coverage | Priority / packet |
|---|---|---|---|
| LS-01 | What Tamil Reveals About AI | Where do specified models fail on morphology, agreement, negation, register, ambiguity and cultural context? What can linguistic structure improve in controlled experiments? | P0 / R1 |
| LS-02 | A Word Is Not a Token | Compare character, grapheme, morpheme and tokenizer segmentation; vocabulary size, text normalization and model-specific token cost. More tokens alone do not prove worse understanding. | P0 / R1 |
| LS-03 | Before Pāṇini: The School Behind the Man | Earlier named authorities, phonetic and recitational scholarship, dating, geography and missing intellectual history. Distinguish possible predecessors from demonstrated transmission. | P0 / R2 |
| LS-04 | Inside the Grammar | Pratyāhāras, it/anubandha markers, anuvṛtti, rule conditions, exceptions and interaction through small verified derivations. Include competing interpretations where relevant. | P1 / R2 |
| LS-05 | Did Later Rules Reshape Earlier Speech? | Compare Ṛgveda 2–7 with later grammatical/recitational descriptions. Which preserved or reconstructed forms resist later norms? What evidence could identify normalization and its date? | P0 / R3 |
| LS-06 | Close Languages, Different Records | Old Vedic, Old/Young Avestan and the small Mitanni Indo-Aryan material: what can actually be compared at lexical, phonological, morphological and syntactic levels? | P1 / R3 |
| LS-07 | Before Tolkāppiyam | Textual layers, dating, earlier practices, traditions about Agattiyam/Agastya, commentary histories and possible interactions. Maturity is not proof of one specific lost predecessor text. | P0 / R4 |
| LS-08 | Meaning Has a Landscape | Poruḷ, tiṇai, uḷḷuṟai, meyppāṭu, genre, speaker and situation. Use paired readings and commentary; do not make landscape a deterministic emotional code. | P0 / R4 |
| LS-09 | Two Grammars, Different Questions | Pāṇini and Tolkāppiyam compared through matched examples; explain overlapping and different tasks and documented arguments about influence. | P1 / R2, R4, R6 |
| LS-10 | Who Mapped the Mouth? | Dated evidence for articulatory descriptions across Vedic, Tamil, Greek, Arabic, Chinese, Mesopotamian and Egyptian traditions. Specify the property and source before asserting priority. | P1 / R5, R6 |
| LS-11 | What the Letters Do Not Show | Tamil vallinam/mellinam/iṭaiyinam, phonemes/allophones, stop realization, historical āytam, vowel length and orthographic conventions. Separate old descriptions from modern speech. | P1 / R4, R5 |
| LS-12 | How Writing Packages Speech | Uyir/mei/uyirmei and Brahmic writing compared with other systems, including Meroitic and Geʿez as research cases. Shared encoding principles do not establish borrowing. | P1 / R5 |
| LS-13 | Brāhmī Before Aśoka? | Site-by-site evidence for Sri Lankan and peninsular early inscriptions; sample dates, context association, identification, calibration and alternatives. Earliest attestation is not automatically invention. | P0 / R5 |
| LS-14 | Who Invented Grammar? | Intersecting histories of scribal lists, language teaching, derivation, syntax, lexicography, rhetoric and poetics; include Chinese, Arabic and Tamil on their own terms. | P1 / R6 |
| LS-15 | When a Grammar Becomes the Standard | Sanskrit norm formation compared with Latin and Greek learned norms, literary registers and language change. Investigate who could acquire or enforce correctness. | P1 / R3, R6 |
| LS-16 | Whose Categories Describe a Language? | Greek–Latin inheritance, colonial grammars and alternative Tamil, Sanskrit, Arabic and Chinese analytical categories; test case-specific fit and distortion. | P1 / R6 |
| LS-17 | Who Was Talking to Whom? | Contact zones and routes through Iran, Gandhāra, Mediterranean and South Asia; Pyrrho, Stoics and Indian thought as distinct hypotheses with independent chronologies. | P2 / R7 |
| LS-18 | Language Across Families | Retroflexion and other selected areal features across Indo-Aryan, Dravidian and Munda; mechanisms and directionality, independent changes and shared inheritance. | P1 / R7 |
| LS-19 | When Sound Becomes Meaning | Bhartṛhari, sphoṭa, sentence/word relations, context and cognition; compare appropriate Greek, Tamil and other texts without claiming anticipation of current AI architectures. | P1 / R4, R7 |
| LS-20 | When a Technical System Becomes Divine | Sound-string terminology and later Śiva attribution; Agastya/Agattiyam traditions; distinguish attestation, retrospective authority and historical authorship. | P1 / R8 |
| LS-21 | The Archive Inside the Model | How digitization, corpus selection, tokenization, training and evaluation affect representation; ask what is missing without claiming a model literally runs Greek–Latin school grammar. | P1 / R1, R6 |

LS-01/02/21 may become one substantial page with distinct interactive sections initially; LS-07/08 should retain enough independent space for Tamil intellectual history. LS-14 is a collection anchor, not a substitute for the detailed investigations. The final number of pages follows the content audit and evidence, not this row count.

### 21.4 Contemporary evidence checked for Tamil and AI

**ILAKKANAM (2026):** The publication describes a Tamil-specific benchmark built from 820 Sri Lankan school-examination questions and reports declining performance with increasing grade/linguistic complexity among tested models. This supports a bounded linguistic-evaluation story, not a universal ranking of Tamil against every other language. The original paper, exact model versions, evaluation code and dataset rights must be checked before reproducing results. [Publication](https://aclanthology.org/2026.chipsal-1.17/)

**TamilTok (2026):** The authors report a morphology-aware tokenizer and TamilMorph resource, with improved morphological alignment and downstream performance in their experiments. This is a concrete route from Tamil structure to a testable computational intervention. It does not establish that ancient poetics improves LLMs or that every tokenizer should be replaced. [Publication](https://aclanthology.org/2026.dravidianlangtech-1.7/)

**Three distinct claims:** (1) measured failures on a defined Tamil task; (2) a proposed linguistic intervention; (3) a demonstrated improvement under controlled evaluation. Do not jump from (1) to (3). A tiṇai/context intervention is a research hypothesis until tested.

### 21.5 Tamil/AI evaluation specification

Separate written modern Tamil, spoken varieties, Sri Lankan and Indian usage, transliteration/code-mixing, and historical/literary Tamil. Do not present one school corpus or one standard as all Tamil. Include human reviewers competent in the variety and genre tested; record defensible multiple answers and disagreements.

Build a small, disclosed evaluation set before a public leaderboard. Include morpheme segmentation, agreement, negation, interpretation of clitics, reference resolution, register, context-sensitive meaning and literary inference as separately scored tasks. Poetic interpretation may require a rubric and evidence-based alternatives rather than one correct label.

Compare the same model/settings under controlled conditions: baseline, additional context, modern linguistic annotation and carefully defined historical-poetic annotation where appropriate. Include a length-matched irrelevant-context control so extra tokens alone do not masquerade as the benefit of tiṇai. Keep held-out examples separate from prompt development and check likely training contamination.

For cross-language comparisons, use matched task difficulty and native-authored material where possible, report translation effects, and include relevant typological comparators rather than only English. Tokenization analysis needs fixed tokenizer versions, normalization, vocabulary settings and comparable text. Track tokens, latency and price only for the actual system tested; shorter segmentation does not itself establish better semantics.

Publish run date, model identifier/version, prompt, settings, item IDs, outputs, scoring procedure, per-task denominators and uncertainty. Score with human-reviewed rubrics; avoid circular evaluation by the same model that generated the test. Preserve frozen result snapshots rather than silently updating a historical claim through live API output. No benchmark has been run in this task.

### 21.6 Historical and computational claims requiring correction or testing

- “No Pāṇinian machine” in Mitanni vocabulary is not strong negative evidence: a tiny record of names and technical terms cannot reasonably be expected to preserve a grammatical treatise. Use its positive linguistic evidence and explicit limits; do not call it a controlled experiment.
- Absence of a surviving Avestan treatise does not prove no analytical tradition existed. Closely related languages with different surviving scholarly records do not isolate one causal explanation.
- The supplied quantum-mechanics example attributing its creation to English-speaking scientists is withdrawn. Use named, evidenced contributions if retaining this analogy; do not replace one national origin story with another.
- Do not assert a precise thousand-year gap, a single pre-Pāṇinian sequence, or contemporaneity of texts without dating arguments. Earlier practices may be preserved in later texts; text date and practice date differ.
- Do not make “Greek classifies / Pāṇini derives” an exhaustive account of either tradition. Include syntax, meaning, reasoning and later work where the comparison requires them. Latin adaptation can involve substantive innovation.
- Do not adopt the supplied high/moderate language-complexity league table. Small corpus size measures survival, not inherent linguistic simplicity.
- Pratyāhāra encoding, articulatory alphabet order and the fourteen sound strings are related but distinct structures. Anubandha notation is not agglutinative morphology.
- Do not identify orthographic letters, Unicode code points, grapheme clusters, phonemes, phones, morphemes and model tokens as equivalent units.
- Tamil's three consonant classes are not simply three places of articulation; their modern phonetic descriptions require care. No separate voiced letter does not establish absence of voiced realization. Historical āytam is not settled by its modern uses.
- Tolkāppiyam's three divisions and later fivefold classifications must not be projected onto one unchanged text. Date texts, strata, commentaries and traditions separately. Neither independent invention nor Sanskrit derivation is the default verdict.
- “First formal grammar,” “invented phonetics,” “first mouth map” and “Tamil-Brāhmī predates Aśoka” need defined comparators and original evidence. A handbook's claim is a research lead, not a substitute for its underlying excavation or textual sources.
- Later grammatical standardization may preserve some old forms and reshape others. The owner's question requires particular mismatches, metrical evidence, recensional differences and scholarly arguments—not a yes/no answer from general oral fidelity.
- Do not treat the computational analogy to memorization as an established explanation of the origins of every formal device. Investigate institutional incentives and evidence for alternative explanations.
- Do not assert “Tamil meaning is contextual but Sanskrit/Greek meaning is not.” All languages use context; the historical analytical traditions may organize its study differently.
- Modern LLMs do not generally require explicit noun/verb school categories to learn from text. Test effects of corpora, annotations and training choices rather than presuming a literal inherited Greek–Latin architecture.
- Cultural competency, Tamil linguistic performance and knowledge of Tolkāppiyam are different evaluation targets. One cannot stand as proof of the others.
- Chronology and contact alone do not establish transmission of Stoic, Buddhist or grammatical ideas. Later Bhartṛhari must not become evidence for an earlier influence without an independently attested antecedent.
- Brahmanical-preservation critique must investigate actual contribution and authority; unknown predecessors are not automatically Dravidian, Munda, Indus or subaltern. Apply equally to Tamil canonical and divine-origin traditions.

### 21.7 Shared features to build after their evidence packets

| Feature | Initial scope | Acceptance requirement |
|---|---|---|
| Speech map | Source-linked place/manner descriptions with optional reviewed audio; modern anatomical schematic labeled as modern. | Never infer historical pronunciation from a contemporary audio sample; keyboard/text alternative required. |
| Derivation inspector | A few reviewed Sanskrit derivations and separately modeled Tamil morphological analyses, with rule/source locators. | Exposes markers versus output, alternatives and limits; does not pretend to implement an entire grammar. |
| Transmission comparator | Recited/segmented/edited/reconstructed forms with dates, source and scholar responsible. | Reconstructions visibly differ from witnessed forms; no inferred recording or pronunciation presented as original. |
| Context explorer | A bounded Tamil poem/passage with speaker, genre and interpretive context, plus alternative readings. | Avoids fixed landscape-to-emotion stereotypes; every explanation has an appropriate textual/commentarial basis. |
| Token/morpheme lab | Reviewed words, graphemes, morphemes and actual tokenizer output, with frozen version metadata. | Does not call tokenization a full linguistic analysis or imply improved accuracy without evaluation. |
| Evidence chronology and contribution graph | Text composition/copy dates, inscription context, named contributors and proposed links. | Shared source ancestry, hypothetical bridges and uncertain dates remain inspectable; no decorative proof arrows. |

Reuse section 20's evidence records, contextual PROVE IT, WITNESS, Field Bag and TIME·PLACE. This is not a new six-engine commitment. Start with one language example and one contextual reading before expanding coverage.

### 21.8 Claude Chat → Claude Code workflow

**Yes: first ask Claude Chat to browse the public site, then use separate research sessions for bounded packets and hand reviewed structured content to Claude Code. Do not ask many isolated chats to generate finished HTML pages and dump them into the repository.** The latter increases duplicated claims, conflicting dates, inconsistent components and discarded local corrections.

1. **Claude Chat public-site audit first:** Browse the live threshold, Enter, Research Index, Explore, Exhibits, Evidence/Ledger, Search and discoverable internal links. Produce a dated visitor-visible route/coverage/risk inventory. Mark inaccessible routes unknown rather than absent.
2. **Shared research contract:** Give every topic chat the same programme brief, its live-page coverage export, current correction records where available and required output structure. Supply only relevant evidence assets; a link not opened is not a reviewed source.
3. **Nineteen topic packets:** Run R1–R19 separately in the dependency order in the companion sequence. The additions cover the Oxus/BMAC interface, material/resource corridors, the language-contact slider, pre-Alexander knowledge routes, Dravidian sibilants, Rigvedic–Avestan divergence, Brahui/highland survival and Hormuz. These are research stages, not page commitments.
4. **Evidence challenge and revision:** Use the challenge prompt on each packet. Reopen cited sources and check claims, locators, chronological logic, counterarguments and numeric calculations. A second model's agreement is not verification. Reserve specialist review for claims requiring linguistic, epigraphic, archaeological, genetic or textual expertise.
5. **Provisional content consolidation:** Resolve contradictions across reviewed packets once; maintain shared IDs, date ranges, terminology and rights. Produce a provisional route manifest and accepted page copy while preserving unresolved findings as research holds.
6. **Claude Code repository reconciliation:** Read the actual current branch, routes, redirects, data, tests, correction history and components. Compare production with the branch. Finalize extend/merge/new dispositions before editing; the repository may contain work the live crawler cannot see.
7. **Claude Code integration:** Provide the approved release, accepted scope and asset references. Implement the smallest complete batch using repository components; update navigation/search/ledger/redirects and check mobile, keyboard, Tamil rendering, source links and correction propagation. Return a reviewable preview and diff before deployment.

Do not make research depend on a specific model brand. Claude Chat is useful for bounded synthesis; Claude Code is useful for repository-aware implementation. Neither substitutes for primary evidence or a qualified reader of a difficult source. This task creates the work plan and prompts, not external Claude conversations or a deployed site.

### 21.9 Operating and cost discipline

- **Buy/use:** Existing corpora, tokenizer libraries, authoring and display components where rights permit; evaluate fit before rebuilding them.
- **Fix:** Existing language pages, contradictory dating and unsupported priority claims before multiplying new routes.
- **Build:** Distinctive source-to-interaction components and bounded Tamil/context experiments.
- **Walk/defer:** Unsupported origin verdicts, a full grammar engine, general multilingual model training, live model leaderboards and twenty-one simultaneous page builds.

No current budget or available cash was supplied for this workstream. Reconstruct costs per packet: research, original-language review, media/rights, annotation, development, inference, QA and ongoing corrections. Track founder time separately from cash. Set an inference spending cap and fund specialist commitments before commissioning them; do not assume a future grant can pay present bills.

Scenarios: **limited resources**—correct existing pages and publish reviewed static evidence; **bounded pilot resources**—one token/context comparison and one historical investigation; **partner-supported expansion**—specialist dossiers, licensed corpora and reusable features. The decision to expand should depend on reviewed content readiness and measured second-case production effort, not the number of generated pages.


## 22. Rigvedic sound, transmission and social strata — expanded programme

**Owner direction, 5 September 2026:** The additional analysis of early Rigvedic grammar, phonology, oral transmission, internal textual/social strata, Indo-Iranian comparison and substrate vocabulary must be incorporated. The owner’s central question is whether the surface language now recited for the oldest hymns was altered during transmission and standardization, and which parts of the celebrated Sanskrit system are inherited language, South Asian development, later analysis or canonization.

**Operational decision:** This section established R9–R11; sections 23–24 extend the complete companion pack to R1–R19. Use the live-site-first sequence in `MELA-KEELA-CLAUDE-FULL-SEQUENCE.md`. Claude Chat produces researched Markdown/CSV/JSON packets; Claude Code reconciles and integrates them into the current repository. Independent chat-generated HTML is not the normal handoff.

### Additional coverage items

| ID | Investigation | Required distinction | Packet |
|---|---|---|---|
| LS-22 | The Rigvedic Sound System, Layer by Layer | PIE inheritance, Indo-Iranian change, Indo-Aryan innovation, proposed areal influence, conditioned realization and later classification. | R9 |
| LS-23 | The Grid Was Made | Whether the elegant stop/nasal/articulation table represents inherited phonemes, conditioned sounds and Indic additions organized by later analysis. | R9, R2 |
| LS-24 | Before the Split Was Not a Vacuum | Possible contact underlying Indo-Iranian innovations and recitation practices; chronology and candidate ecologies without inventing a donor. | R9, R7 |
| LS-25 | What Did the Ṛgveda Sound Like Before the Ṛgveda? | Metrical reconstruction, canonical Saṃhitā, Padapāṭha, recension/school evidence and later Classical expectation. | R3 |
| LS-26 | The Ṛgveda Is Not One Moment | Relative strata, internal complexity, genre, compilation and the limits of absolute dating. | R10 |
| LS-27 | Patron, Poet, Raid, Ritual | What older family-book hymns did within elite exchange and conflict; evidence for religion, politics and economy without forcing one label. | R10 |
| LS-28 | What Changed on the Way to Classical Sanskrit? | Persistence, decline and restructuring of moods, infinitives, accent, morphology, phonology and usage; Pāṇini as analyst/norm authority. | R3, R10, R2 |
| LS-29 | The Words Whose Languages Vanished | Lemma-level investigation of proposed Dravidian, Munda, Central Asian and unidentified substrate vocabulary, including rejected etymologies. | R11 |
| LS-30 | How Languages Classify Beings | Gender, noun class, animacy/person/rationality and number across selected languages, without genealogical or social conclusions from a typological match. | R11, R6 |
| LS-31 | Sanskrit Became South Asian | Feature-by-feature account of areal convergence and contact alongside inheritance and internal change. | R9, R11, R7 |

These items add research coverage, not ten automatic new pages. LS-22/23 can become one layered sound feature; LS-25/28 can share a verse/transmission investigation; LS-26/27 can become one major Rigveda-strata experience. LS-29 and LS-30 deserve distinct experiences if the evidence packets are strong.

### Specific evidentiary requirements

- The family books 2–7 provide an older core for many comparisons but remain internally layered. Books 8 and 9 need their own compositional treatment; “1/10 later” must resolve to particular material rather than apply to every hymn.
- A transmitted surface form that does not fit a reconstructed metre can support an earlier pronunciation only through an explicit metrical and phonological argument. Not every metrical difficulty proves normalization, and a philological restoration is not a recording of the original voice.
- Compare Saṃhitā, Padapāṭha, metrical restoration and Classical expectation without calling any one of them simply “the original.” Record school/recension, edition and scholar responsible.
- Pāṇini’s treatment of chandasi/Vedic usage requires exact rule and commentary evidence. Its existence can demonstrate recognized differences; it cannot by itself date the change or show who imposed it.
- Mitanni is an independent, scribally mediated witness to a small set of Indo-Aryan forms. It is not a syntax corpus or a controlled experiment, and absence of a grammatical treatise is not meaningful negative evidence in so small a record.
- Old Avestan is the stronger sister-language comparison. Distinguish Old/Younger Avestan, composition, oral transmission, later writing and modern reconstruction; Avestan transmission has its own transformations.
- Regular correspondences across branches establish the direction of a sound reconstruction more strongly than Sanskrit prestige. Indo-Iranian innovations may still have contact histories; “Indo-Iranian” must not silently mean untouched Proto-Indo-European inheritance.
- Velar/palatal nasal realization through place assimilation occurs beyond South Asia. The five-place Sanskrit nasal grid cannot be treated as five pristine PIE nasal phonemes. Investigate the analytical insight separately from phonemic history.
- Retroflexion is a strong areal question, but separate inherited/internal environments, expansion/phonologization and possible Dravidian, Munda or unidentified-substrate involvement. One feature cannot identify the Indus language.
- Vedic accent offers evidence of preservation of features absent in later ordinary Sanskrit. “Perfect preservation” and “wholesale rewriting” are both inadequate models; show the mixture case by case.
- Richer early verbal categories do not mean the entire older language was globally more complex, and later loss does not mean intellectual decline. Compare specified paradigms and discourse functions.
- Ritual, praise, patronage, political legitimation and conflict can coexist in the same hymns. Do not make “religion” and “raid economy” mutually exclusive classifications.
- A later canonical function does not erase a hymn’s earlier political or social context. Likewise, a hymn about conflict is not a neutral chronicle of the opposing population.
- The supplied language-comparison table is a hypothesis generator. Do not convert “gendered versus beyond gender,” presence/absence of dual, or agglutinative/fusional labels into civilizational psychology or ancestry.
- Akkadian and Egyptian masculine/feminine systems and duals must be described within Semitic/Afroasiatic history where appropriate; feature resemblance alone does not link them genealogically to Indo-European.
- Tamil rational/non-rational, Sumerian person/nonperson and Elamite animate/inanimate categories require their own grammatical contexts. They may support a comparative exhibit without proving relationship.
- Kuiper/Witzel-style vocabulary totals must be reproduced from explicit lemma lists and criteria. Report corpus and denominator; verify context, morphology and proposed etymologies. Search DEDR before saying no Dravidian candidate exists, but a lexical resemblance is not a demonstrated loan.
- “Unknown substrate” is an evidence status, not a covert label for Indus or one marginalized modern population. Show the dark field without filling it ideologically.

### Proposed first build from this expansion

After current-route reconciliation and reviewed packets R9, R3 and R10, build one coherent experience provisionally titled **The Ṛgveda Is Not One Moment**. It should allow a visitor to select a verse and inspect its relative stratum, textual form, social/ritual function and one supported linguistic difference. A fully sourced verse may then open into **What Did It Sound Like?**, comparing textual/metrical representations without presenting a speculative audio track as historical fact.

Connect it to current Rigveda, corpus, phonology, enemy-name, patronage, caste/varṇa and Pāṇini coverage through shared record IDs. Correct affected existing claims before adding spectacle. The next build can add the layered mouth/sound map from R9, followed by substrate vocabulary only after a reproducible lemma register exists.

### Handoff and sequencing rule

Run the public-site audit before research. Run R9 before R3, and R3/R9 before finalizing R2’s public narrative. Run R10 before treating any corpus-wide Rigvedic social claim as a single-period finding. Run R11 separately because etymology and typological comparison require different sources from metrical phonology. Run the Claude Code repository reconciliation after reviewed packets are consolidated provisionally and before any build.

Each research chat returns a ZIP containing synthesis, claims, sources, chronology, comparisons, corrections, route dispositions, copy, feature brief and structured examples. Run the challenge prompt and produce a reviewed v2 packet. Consolidate only accepted claims into one release ZIP. Claude Code then implements the release on a branch, with no deployment until preview and diff review.


## 23. Indo-Iranian contact corridor, material routes and live-site-first planning

**Owner direction, 5 September 2026:** Add the full supplied programme concerning place-conditioned nasals, the historical construction of the Sanskrit sound grid, BMAC/Oxus contact before the Indo-Aryan–Iranian split, ritual and political provenance, pre-Alexander contact, Prakrit/Pāli change, resource corridors, lapis/carnelian, trade/tribute/raiding and the combined language/material Atlas. Begin planning from a Claude Chat audit of the public site.

### 23.1 Preliminary public-site reconciliation

A limited live check on 5 September 2026 confirms that the public Research Index describes **102 content pages** and that several proposed topics already have substantial routes. This is a preliminary mapping, not the full Claude audit:

| Public route | Existing subject | Preliminary disposition |
|---|---|---|
| `/panini` | Pāṇini, Tolkāppiyar, earlier grammarians, sound analysis, Prakrit and language hierarchy | Major evidence/copy audit and extension; do not create a duplicate grammar overview. |
| `/dasa-forts-rigveda` | The ninety-nine forts, corpus distribution, chronology, BMAC and post-urban candidates | Update/recheck counts, strata, date claims and candidate framing; not a new page by default. |
| `/meluhha-trade` | Indus exchange as seen through Mesopotamian sources | Extend with material/provenance records or connect to a shared corridor feature. |
| `/mitanni` | Indo-Aryan names/terms in a Syrian kingdom | Extend only where new comparison evidence is material. |
| `/tinai` | Tamil poetics of five landscapes | Extend/contextualize; do not substitute an AI hypothesis for the historical page. |
| `/dravidian-sounds-sanskrit-lacks` | Dravidian/Sanskrit sound comparison | Correct and link to layered sound provenance; avoid a duplicate sound table. |
| `/two-classical-languages` | Sanskrit and Tamil compared | Reframe through matched criteria and link to the new investigation set. |

The live site already claims production-scale evidence instruments and a page-level correction/limit model. Any new feature must reuse those patterns where the repository supports them. Topics not found in this limited check remain **not yet located**, not confirmed absent.

### 23.2 Additional language and intellectual-history work items

| ID | Investigation/update | Required output | Packet |
|---|---|---|---|
| LS-32 | Nasals Beyond South Asia | Greek and wider cross-linguistic place assimilation; distinguish a phone from a phoneme and the sound from its grammatical classification. | R9, R15 |
| LS-33 | The Oxus Interface | Dated BMAC sites, contacts, loanword evidence, genetics and unknown-language status. | R12 |
| LS-34 | Ritual Before the Split | Common Indo-Iranian poetry, sacrifice and Soma/Haoma separated into inherited, innovative, substrate-proposed and later tradition-specific layers. | R12, R10 |
| LS-35 | Rigvedic and Avestan Worlds | Matched language, genre, transmission, social and ritual comparison without calling either an unchanged Proto-Indo-Iranian culture. | R3, R10, R12 |
| LS-36 | Sanskrit Was Regulated; Speech Kept Moving | Old Indo-Aryan dialects, Pāli and inscriptional/literary Prakrit developments; reject the “corrupted Sanskrit” tree. | R14, R2 |
| LS-37 | Before Alexander | Achaemenid-era contact corridors and the chronology of Greek/Indian linguistic thought; contact possible is not transmission proven. | R15, R7 |
| LS-38 | *kīnāśa* / *kiṇṭu* Candidate File | Lemma, passage, Proto-Dravidian cognates, substitutions, remodeling, alternatives and confidence. | R11 |
| LS-39 | Proto-Indo-Iranian Was Not a Vacuum | Identify which shared traits are PIE, post-PIE innovation or contact candidates; do not use the reconstruction label as a cultural origin claim. | R9, R12 |
| LS-40 | The Language That Changed as It Moved | Accessible sound/word/grammar/neighbour table, then a geography-time slider based only on reviewed records. | R14 |
| LS-41 | Who Praised the King? | Mesopotamian, Egyptian, Elamite, Indo-Iranian and Rigvedic ruler–specialist systems; analogy and transmission kept distinct. | R10, R12 |

### 23.3 Material and corridor work items

| ID | Investigation/update | Required output | Packet |
|---|---|---|---|
| COR-01 | The Southern Corridor | Integrated chronology/map: Mesopotamia–Elam–Marhaši–Helmand–BMAC/Badakhshan–Indus–Gujarat/Gulf. | R13 |
| COR-02 | Lapis | Object-level geological, manufacturing, commercial, textual and findspot provenance; Badakhshan claims tested, not assumed. | R13 |
| COR-03 | Carnelian | Gujarat/Cambay, Iranian and other sources; drilling/etching/workshop evidence and route-specific objects. | R13 |
| COR-04 | Shortugai | What is securely Harappan, its date and material role; “mining colony” treated as a hypothesis. | R13 |
| COR-05 | Marhaši | Textual attestations, proposed geographies, resources and distinction from Meluhha; language unknown. | R13 |
| COR-06 | Meluhha–Magan–Dilmun | Recheck texts, translations, ship routes, commercial intermediaries and public museum claims. | R13 |
| COR-07 | Trade, Gift, Tribute, Raid, Conquest | Typed political-economic relations by commodity and century rather than a universal linear story. | R13 |
| COR-08 | What Moved East? What Moved West? | Shared Atlas layer switching Goods, Genes, Words, Sounds, Rituals, Technologies and War. | R13, R14 |
| COR-09 | War + Raw Materials | Eastern campaigns, route control and extraction tested against primary royal inscriptions and material evidence. | R13 |
| COR-10 | Who Explains the Object? | Museum/institute coverage audit: maker, trader, extraction, route, uncertainty, community naming and rights. | R13 |

### 23.4 Evidence and design controls

- The Sanskrit 5×5 table is a later analysis of a historically layered sound inventory. Its beauty is evidence of classification, not proof that all 25 entries were equally inherited phonemes.
- Place-conditioned `[ŋ]` or `[ɲ]` occurs outside South Asia. The distinctive question is the early explicit articulatory matrix, not human coarticulation itself.
- “Shared Vedic and Avestan” permits at least PIE inheritance, post-PIE Indo-Iranian innovation, pre-split borrowing/contact and parallel later development. Test each feature separately.
- BMAC language affiliation is unknown. Archaeological culture, ancestry components and reconstructed donor lexicon cannot silently name one another.
- A proposed BMAC ritual contribution requires word-level and institution-level evidence. The whole Vedic/Avestan religious complex must not be reassigned from a few loan candidates.
- The *kīnāśa*–*kiṇṭu* resemblance is a high-priority test case, neither dismissed by surface mismatch nor accepted on semantics alone. Unknown substrate is a residual assessment, not a preferred donor.
- Achaemenid connectivity makes pre-Alexander exchange possible. It does not by itself show that Plato, Aristotle or later Greek grammarians borrowed an Indian analysis.
- Material routes require separate fields for geology, manufacture, exporter, findspot and ancient textual label. “Meluhha carnelian” is not automatically a mine coordinate.
- Trade and violence may coexist. A progression from trade to coercion is a testable case model, not a universal law.
- Rigvedic conflict is evidence of an elite archive and genre, not a neutral census of every population or event. The existing ninety-nine-forts page must be audited before any new forts feature is proposed.
- Resource, gene, word and idea arrows require different symbols and source types. Spatial overlap alone must not visually assert causation.

### 23.5 Build disposition

**Likely existing-page corrections/extensions:** Pāṇini/grammar, Dravidian sounds, two classical languages, tiṇai, Mitanni, ninety-nine forts and Meluhha trade.

**Likely new investigations pending the complete live/repository audit:** What Tamil Reveals About AI; The Oxus Interface; Before Alexander; The Language That Changed as It Moved.

**Likely shared features rather than standalone pages:** layered sound-provenance matrix; language/contact slider; Southern Corridor Atlas; object-provenance record; typed trade/tribute/raiding edges; museum-coverage audit.

**Research holds:** full BMAC language identity; whole-religion origin verdicts; established *kīnāśa*–*kiṇṭu* etymology; Greek borrowing verdict; Marhaši=Meluhha/Indus; identification of the ninety-nine forts with one archaeological culture.

### 23.6 Operating sequence

Run the exact public audit in `MELA-KEELA-CLAUDE-LIVE-SITE-AUDIT-PROMPT.md`, then the nineteen research packets in `MELA-KEELA-LANGUAGE-RESEARCH-PROMPTS.md`. Claude Chat returns reviewed research/content/data ZIPs, not production HTML. After provisional consolidation, Claude Code reconciles the current branch and only then implements an approved release. The full step-by-step procedure is in `MELA-KEELA-CLAUDE-FULL-SEQUENCE.md`.


## 24. Final expansion: sound borrowing, divergent archives, language refugia and the Strait

**Owner direction, 5 September 2026:** Complete the research programme with detailed, evidence-forward treatments of Proto-Dravidian sibilant history, the different social/ideological work performed by Rigvedic and Old Avestan corpora, long-term Brahui continuity versus migration, Kurukh/Malto and highland survival, ancient Balochistan language uncertainty, the Blue/Red Roads, the complete forts dataset and Hormuz from Bronze Age corridor to modern chokepoint. The programme must actively decolonize, debrahminize and de-Indo-Europeanize the historical method without replacing one nationalist certainty with another.

### 24.1 Critical method made operational

| Operation | What the research must do | What it must not do |
|---|---|---|
| Decolonize | Reopen colonial classifications, translations, surveys, excavation priorities, museum custody, racial models and textbook inheritance; identify who funded, collected, withheld and published. | Reject a finding merely because a colonial scholar recorded it, or treat a modern institutional summary as primary evidence. |
| Debrahminize | Separate Brahmanical/Sanskrit preservation and normative claims from origin; recover vernacular, oral, artisanal, agrarian, women's, subordinated and non-Brahmanical evidence where it survives. | Presume every Sanskrit source is false or every unnamed predecessor was Dravidian, Indus or subaltern. |
| De-Indo-Europeanize credit | Accept supported language genealogy while testing post-PIE innovation, BMAC/Oxus contact, multilingual formation, areal change, borrowing and extinct-language contributions. | Treat “Indo-European language” as proof of civilizational ownership of its ritual, science, technology or analytical system. |
| Audit nationalism | Test Hindu-nationalist, Tamil/Dravidian-nationalist, Iranian-nationalist, Greek/European-first, Afrocentric and other priority claims against chronology and material evidence. | Create false symmetry about archival power, or select evidence only because it supports the preferred counter-narrative. |

Every packet must include the dominant interpretation, strongest heterodox/marginalized alternative, institutional genealogy of both, evidence each explains, evidence each suppresses or cannot explain, and the narrow conclusion that survives. Unknown is a positive result when the archive cannot decide.

### 24.2 New language, archive and community work items

| ID | Investigation | Coverage/output | Packet |
|---|---|---|---|
| LS-42 | Proto-Dravidian Without a Sanskrit Sibilant Series | Reconstruct `*c`, the status of `/s/`, branch outcomes and the difference between reconstruction symbols, phones and phonemes. | R16 |
| LS-43 | The Sounds a Script Learned to Write | Old Tamil resources, Sanskrit/foreign sound accommodation and dated use of Grantha-derived ஜ/ஷ/ஸ/ஹ without deficiency narratives. | R16 |
| LS-44 | The Same World, Two Responses | Early Rigvedic patron/war/praise economy versus Old Avestan reformist selection, with the corpus/genre mismatch foregrounded. | R17 |
| LS-45 | Before and After Zarathustra | Historicity, date/place, founder/community authorship, pre-reform religion, *deva/daēva*, ritual critique and unknown earlier reformers. | R17, R12 |
| LS-46 | Brahui: Four Histories, Not One | Language, modern ancestry, tribal/political identity and contact strata kept separate. | R18 |
| LS-47 | Continuity Versus Migration | Best versions of northwestern-remnant and first-millennium-CE migration models, with equal explanatory burdens and explicit falsifiers. | R18 |
| LS-48 | The Languages Left on the Hills | Brahui, Kurukh and Malto geography, local oral histories and global refugia/migration controls without ecological determinism. | R18 |
| LS-49 | Genes Do Not Speak | What modern/ancient genetics can constrain, what it cannot date, and why living southern populations are not Bronze Age language proxies. | R18 |
| LS-50 | Balochistan, 3000 BCE–1500 CE | 500-year speech-zone atlas using attested/inferred/possible/unknown polygons and independently dated Iranian/Balochi/Indo-Aryan evidence. | R18 |
| LS-51 | What Would Make an Indus–Dravidian Case Stronger? | Predictions from substrate lexicon, toponymy, Brahui archaisms, repeatable sign readings, archaeology and loan chronology; no isolated rebus proof. | R18, R11 |

### 24.3 New and expanded material/political-economy work items

| ID | Investigation | Coverage/output | Packet |
|---|---|---|---|
| COR-11 | The Blue Road | Object-level Badakhshan-lapis chronology and routes; distinguish source inference from chemical proof and first find from first contact. | R13 |
| COR-12 | The Red Road | Indus/Gujarat carnelian, drilling/etching technology, craft mobility and alternative geological sources. | R13 |
| COR-13 | Who Tells the Stone's Story? | Compare Cambridge, British Museum, Met, Penn and source-country institutions; expose what catalogs establish and whom they omit. | R13 |
| RV-01 | The 99 Forts Database | Every relevant *pur* passage with varying counts, patron, enemy, poet, descriptors, wealth/water context, stratum and geography confidence. | R10 |
| RV-02 | Fort Text Versus Fort Archaeology | Textual/inferred locations kept separate from excavated BMAC, Late/Post-Harappan and other fortifications. | R10, R12 |
| COR-14 | Before Oil: The Strait | Bronze Age to modern Hormuz/Gulf chronology, commodities, powers and changing mechanisms of route control. | R19 |
| COR-15 | When Does a Route Become a Chokepoint? | Trade, tribute, taxation, naval protection, blockade, raid and conquest as typed relations, not one inevitable progression. | R19, R13 |
| COR-16 | Before States, Before Imperial War | Evidence for interpersonal violence, group conflict, fortification and organized warfare without a universal peace-to-war ladder. | R19 |
| COR-17 | When a Network Fragments | Regional Harappan deurbanization, river/climate change, workshop/port disruption and contraction of long-range specialist production. | R13 |
| COR-18 | Ancient–Modern Power Comparison | A separately reviewable/expiring essay on corridor control; current claims version-pinned and independently verified. | R19 |

### 24.4 Key investigation questions

1. Did Proto-Dravidian lack phonemic `/s/`, or is that a shorthand for the current comparative reconstruction? Which daughter changes and uncertain correspondences matter?
2. When and how did Tamil writing distinguish Sanskrit/foreign sibilants, and how did actual pronunciation differ from learned spelling?
3. Do RV 6.31.4, RV 1.130 and other candidates support a patron–praise–divine aid–victory–wealth cycle when read in context and by stratum?
4. Does the Gāthic archive represent a moral reform of a violent inherited social world, or is the contrast principally an artifact of genre and survival?
5. Which features of pre-Zarathustrian religion are genuinely reconstructed across Vedic/Avestan evidence, which may be BMAC/Oxus contact, and which are later projections?
6. What did the 2017 and subsequent Brahui genetic studies actually test and conclude? What demographic models fit the data without assigning language to DNA?
7. Does Brahui loan stratigraphy discriminate between old continuity and recent migration after the chronology of each possible donor is independently established?
8. Are there community-authored Brahui, Kurukh and Malto histories that outside scholarship has ignored or filtered? What can oral history establish without becoming a literal Bronze Age chronicle?
9. Does elevation/refugia improve an explanatory model of present distribution after controlling for known long-distance migrations and state/language-shift history?
10. What ancient Balochistan speech zones can be attested at each interval, and how large is the genuinely unknown field?
11. Which lapis and carnelian objects have material provenance analysis, which merely repeat long-standing source attributions, and how did manufacturing knowledge travel?
12. What do the varying 90/99/100 fort counts imply about formula, history and scale? Which locations can actually be constrained?
13. What did ancient texts mean when they described ships moored at Agade, and how do commerce and military power coexist without implying the ships were seized?
14. Which factors explain the contraction/reorganization of Harappan material networks, and what evidence exists for post-urban violence without reviving the disproven single-invasion collapse story?
15. What changes and what persists in the political economy of Hormuz from copper/beads/shell to petroleum/LNG? Which modern comparisons illuminate structure, and which are rhetorical distortion?

### 24.5 Evidence gates

- Do not turn standard reconstruction into certainty: state evidence, competing reconstructions and the time-depth limit.
- Do not treat Old Avestan as the neutral prehistory of all Iranian religion; it is also a selected transmitted archive.
- Do not infer missing Rigvedic ethical/reformist poetry never existed, or missing Iranian praise poetry never existed.
- Do not identify Zarathustra's opponents, date or homeland more exactly than the sources permit.
- Do not quote community oral histories through colonial paraphrase when community-authored material is available; record language, translator and consent/publication context.
- Do not call living people linguistic fossils, remnants of a race or genetically Dravidian/Indo-European.
- Do not use a modern national or imperial boundary as a speech map.
- Do not infer ancient Dravidian merely from modern Brahui location, but do not make an undocumented medieval migration the default requiring continuity to disprove.
- Do not treat Mehrgarh's modern archaeological place-name as an ancient cognate of Marhaši.
- Do not infer Badakhshan provenance for every blue object; distinguish visual identification, geological plausibility and analytical sourcing.
- Do not infer the start of a route from its earliest recovered object.
- Do not treat a museum label as independent confirmation when institutions cite the same older study.
- Do not force every *pur* to mean an urban city, one material or one historical event.
- Do not publish volatile 2026 political/energy claims without current primary and multi-source verification; store an access/publication date and expiry/review date.
- Do not equate Sargon with a modern leader. Compare mechanisms and explicitly show legal, institutional and economic discontinuities.

### 24.6 Feature architecture

The likely flagship experiences are:

1. **The Language That Moved** — a dedicated Artifact Atlas mode combining time, geography, dated sites/materials and sound/word/grammar/neighbour change, expanded with the Proto-Dravidian sibilant lane and Brahui confidence map.
2. **The Same World, Two Responses** — matched Rigvedic/Old Avestan passage inspection with genre-survival warning.
3. **The Language That Refused to Disappear** — Brahui models controlled by genetics, loanwords, documentation, phylogeny, archaeology, geography and community testimony.
4. **The Languages Left on the Hills** — elevation-first survival/migration comparison with no origin verdict embedded in the map.
5. **The Blue Road / The Red Road** — material biography from source through makers, intermediaries, consumers and modern institutions.
6. **The 99 Forts** — full corpus table linked to actual archaeological fortifications without forced matches.
7. **Before Oil: The Strait** — durable ancient route plus refreshable modern layer.

These are not seven immediate builds. The first implementation release remains one language/transmission path and one Tamil/AI path. The corridor and Brahui experiences require substantially larger reviewed datasets and may form later releases.

### 24.7 Stateful Claude Chat workflow

Use `MELA-KEELA-CLAUDE-SAY-NEXT-RESEARCH-PROMPT.md` when the owner wants one Claude Chat to manage the full sequence. The owner should only need to reply **next**. Claude must maintain a manifest, complete one numbered stage at a time, save cumulative checkpoints and return one final master research ZIP. If context continuity fails, Claude must request only the most recent checkpoint ZIP rather than making the owner reconstruct the project.

### 24.8 Artifact Atlas mode — possible language change with movement

This is a required shared feature, not an optional illustration. It must reveal how proposed language changes line up—or fail to line up—with movement into and within the subcontinent.

**Visitor action:** drag a date/geography control across the steppe–Oxus/BMAC–Afghanistan/Helmand–Balochistan/Indus–Punjab/Kuru–Gangetic corridor. At each interval the visitor can turn on:

- **Sounds:** retroflexion, sibilants, conditioned nasals, aspiration, vowels/diphthongs, liquids and accent;
- **Words:** securely inherited vocabulary and proposed Central Asian, Dravidian, Munda or unidentified contact loans, including agricultural/settlement/ritual examples;
- **Grammar:** moods, dual, infinitives, participles/non-finite chaining, quotatives and later Middle Indo-Aryan restructuring;
- **Neighbours:** attested or hypothesized speech communities with uncertainty polygons;
- **Materials:** relevant BMAC, Helmand, Shortugai, Indus/post-Harappan and later sites/routes;
- **Rituals/institutions:** common Indo-Iranian evidence, proposed contact contributions and later Vedic/Avestan/Pāṇinian developments.

**No single route is the default truth.** The feature must let visitors compare alternative movement/contact models and see which records each requires. A moving linguistic feature, ancestry component, pottery style and commodity route must use different marks. Their overlap is a question generator, not proof of causal identity.

Required state-change record:

```text
feature_id
domain
earlier_state
later_state
date_range_and_basis
earliest_attestation
reconstruction_basis
geography_and_confidence
comparison_languages
internal_change_explanation
contact_candidate_and_evidence
archaeological_or_material_correlate
counter_evidence
assessment
source_ids
```

Required evidence statuses:

`ATTESTED | RECONSTRUCTED | INFERRED | CONTACT-SUPPORTED | CONTACT-POSSIBLE | DISPUTED | UNKNOWN`

Acceptance conditions:

1. Clicking an artifact/site states whether it provides linguistic evidence, only a possible contact context or no linguistic evidence.
2. The interface never makes one archaeological culture, genome cluster or language family the same entity.
3. The Proto-Indo-Iranian label does not erase pre-split contact; the Classical Sanskrit label does not overwrite older Vedic or vernacular change.
4. A static keyboard/screen-reader table provides every conclusion available through the animation.
5. Every transition can open its source, alternative explanation and confidence basis.
6. Unknown zones remain visibly unfilled rather than receiving a modern national/language color.
7. The feature links outward to The Oxus Interface, The Same World Two Responses, the Brahui investigation, the Blue/Red Roads and the Rigvedic forts evidence without duplicating their prose.


## Change log

- **2026-09-04 — Version 1:** Consolidated findings from live-site inspection, screenshot review and owner feedback. Added information-architecture, categorized-menu and visual-experience requirements. No implementation authorized.
- **2026-09-04 — Version 2:** Added and triaged the independent critical assessment. Recorded count contradictions, reproducibility, editorial accountability, Danino, headline strength, brand consistency, progressive enhancement, learning and benchmark ideas. Explicitly separated confirmed defects from matters requiring verification and speculative recommendations. No implementation authorized.
- **2026-09-04 — Version 3:** Added the owner’s direction for a visual Veḷi threshold, evidence-rich museum foyer and genuinely curatorial Exhibits hub. Defined distinct visitor roles for all three and limited the supplied six-engine build plan to future architectural evaluation. No production implementation authorized.
- **2026-09-04 — Version 4:** Added the proposed children’s product and funding dossier as a separate strategic workstream. Preserved the evidence-led concept, vertical-slice idea, rights/safeguarding gates and funding leads while flagging stale repository claims, conflicting counts, unverified deadlines, legal/entity assumptions and capacity risk. No adoption, funding application or build authorized.
- **2026-09-04 — Version 5:** Triaged the proposed merged project instructions. Retained core evidence, correction, copy and design principles; flagged brand, publication, page-count and template conflicts; constrained Rakhigarhi/Indus Periphery, Irula, Brahui and Para-Munda claims; and captured deck-derived content and image leads as unauthorised research backlog.
- **2026-09-04 — Version 6:** Recorded the 108-route report as a historical correction to the earlier 58-file misreading, noted the later 133-page integration, created a current-inventory and 21-orphan reconciliation requirement, and invalidated unsupported deck-gap conclusions. No implementation authorized.
- **2026-09-04 — Version 7:** Compared the institutional vision and proposed VELI-12A synthesis; added a proposed one-page architecture, clarified brand/mode/evidence boundaries, reduced the build to one complete investigation, verified material DMC/CMF constraints, and added cash-flow scenarios and pilot decision criteria. Preserved the current site redesign and all unresolved owner decisions.

- **2026-09-05 — Version 8:** Established ancient subaltern history and intellectual provenance as an owner-directed core research/content programme; added eight feature briefs, whole-proposal coverage, worldwide comparison lanes, evidence rules, existing-coverage reconciliation, pilot dependencies and acceptance criteria. Completed the comparative research foundation and work-list integration; no production site changes or new historical claims published.

- **2026-09-05 — Version 9:** Added the language-science/Tamil-and-AI programme: 21 coverage items, existing-page revisions, six shared features, two checked contemporary NLP leads, historical claim corrections, evaluation protocol, eight-packet Claude Chat research workflow and repository-aware Claude Code integration. Research/build backlog and prompts completed; no new historical verdicts, benchmark runs or production pages implied.

- **2026-09-05 — Version 10:** Expanded language science with ten Rigvedic sound/transmission/social/substrate coverage items and three research packets; added evidence controls for metre, recitation, Mitanni, Avestan, sound-system provenance, ritual patronage, noun-class comparison and substrate vocabulary; and created the complete Claude Chat research-ZIP to Claude Code repository workflow. No historical conclusions, generated HTML or deployment implied.

- **2026-09-05 — Version 11:** Changed the workflow to a Claude Chat live-public-site audit before research and a Claude Code repository reconciliation before implementation. Added the Oxus/BMAC interface, Indo-Iranian ritual provenance, pre-Alexander contact, Prakrit/Pāli change, *kīnāśa* candidate protocol, ruler–specialist comparison, lapis/carnelian/Marhaši/Meluhha resource corridors, trade–tribute–raiding relations, museum object-provenance audit and combined language/material Atlas features. Expanded the prompt pack to R1–R15 and mapped confirmed public-page overlaps; no new historical verdicts, HTML or deployment implied.

- **2026-09-05 — Version 12:** Added Proto-Dravidian sibilant/script history, the Rigvedic–Old Avestan “Same World, Two Responses” investigation, Zarathustra archive/reform questions, Brahui continuity-versus-migration and community-evidence programme, North Dravidian/highland survival, genes/language controls, a 500-year Balochistan uncertainty map, the Blue and Red Roads, complete Rigvedic forts dataset, Harappan network fragmentation, and Before Oil/Hormuz. Made decolonization, debrahminization, de-Indo-Europeanization and nationalist-narrative auditing explicit evidence operations; expanded the research set to R1–R19 and added one stateful “say next” Claude workflow. No historical verdict, HTML or deployment implied.
