# Mela Keela / Veḷi — language research and implementation prompts

**5 September 2026.** Companion to master work list Version 12, sections 21–24. Run the live public-site audit first, then run the topic packets as separate research conversations with the same shared contract. Produce evidence and content packets first; reconcile them against the current repository and integrate them through Claude Code. None of the prompts below has been run in an external Claude session through this task.

## Recommended order

Start with Prompt A, the live-site audit. Then run R1 (Tamil/AI), R9 (Rigvedic sound provenance), R16 (Dravidian sibilants), R3 (oral normalization), R10 (Rigvedic strata, conflict and patronage), R12 (Oxus/BMAC interface), R17 (Rigvedic–Avestan divergence), R2 (Pāṇini), R4 (Tamil's intellectual architecture), R11 (substrates and grammatical ontology), R18 (Brahui and highland survival), R13 (resource corridors), R19 (Hormuz), and R14 (language-contact slider). Follow with R5, R6 and R8; run R15 (pre-Alexander knowledge routes) after the Indian and Greek chronologies exist, and R7 last when the directionality evidence is ready. A packet can yield several sections, one new page, or revisions to several existing pages. Do not equate nineteen conversations with nineteen pages.

Every conversation should receive: the shared contract below; its topic prompt; the matching public-coverage export from Prompt A; current correction records if available; and the sources relevant to that packet. Missing source access must be reported specifically. Do not paste an entire repository or all preceding conversations into every research session.

## Prompt A — Claude Chat public-site audit before research

Use the complete copy/paste prompt in `MELA-KEELA-CLAUDE-LIVE-SITE-AUDIT-PROMPT.md`. Claude Chat must browse `melakeela.com`, beginning with `/enter` and `/research-index`, and return the route/coverage/research-needs audit. The public site is the visitor-visible baseline. It does not replace the later repository reconciliation.

## Prompt 0 — Claude Code repository reconciliation before build

Read the current repository instructions and inspect the current branch. Do not modify or deploy the site in this pass. Reconcile the live public-site audit and reviewed research packets against actual routes, redirects, content, source records and previous corrections.

Return a table for every work-list item in sections 21–24 with production URL, branch path(s), present coverage, production/branch difference, claims needing review, relevant assets, proposed disposition (extend/merge/new/shared feature/research hold), and research packet R1–R19. Do not infer missing coverage from a route name alone. Treat the repository as implementation source of truth and the live audit as the record of what visitors currently see. Export affected page text and source/claim IDs. Preserve existing naming, navigation and design decisions. Identify component reuse opportunities without starting an engine rewrite.

## Shared research contract — paste before every R prompt

You are preparing an evidence-led research and content packet for Mela Keela / Veḷi. Ancient subaltern history, intellectual provenance and comparative language science are core research programmes. Investigate contribution, preservation, authority and attribution without deciding civilizational ownership beforehand.

Treat supplied conversational claims as hypotheses requiring verification. Read primary texts, original research, authoritative editions and collection records where possible. Give exact source locators. If only an abstract or publisher summary is available, say so and limit the claim accordingly. Never supply an invented quotation, page number, DOI, manuscript date or model result. Search snippets are discovery aids.

Preserve these distinctions: language versus scholarly model; phoneme versus phone versus letter versus grapheme versus token; composition versus copy versus edition; similarity versus contact versus transmission; evidence absence versus demonstrated historical absence; original attestation versus origin. Comparative scrutiny must preserve differences in institutional power and evidentiary survival.

Date and scope every comparison. Do not use whole-language sophistication rankings. Present documented exclusions directly; neither sympathy nor prestige establishes attribution. Do not assign unknown contributors a modern identity. Do not turn Sanskrit, Tamil, Greek, Arabic or any other tradition into an internally uniform agent.

Apply four explicit critical operations throughout:

1. **Decolonize the evidence:** identify categories inherited from colonial philology, archaeology, census-making, racial theory, museum collecting and textbook traditions. Trace who excavated, collected, translated, classified, funded, withheld and published the record. Reopen the underlying evidence rather than accepting or rejecting a conclusion because it is “standard.”
2. **Debrahminize the archive:** distinguish a Brahmanical or Sanskrit textual witness from the origin of every practice or idea it preserves. Look for named and unnamed predecessors, vernacular and oral evidence, artisans, cultivators, women, subordinated communities, non-Brahmanical religious traditions and the institutional interests of transmitters. Do not presume that a Brahmanical source is false, or that every unattributed contribution was Dravidian/subaltern; show the filter and test provenance.
3. **De-Indo-Europeanize civilizational credit:** accept well-supported linguistic genealogy while refusing to make it a universal explanation for ritual, science, social institutions, technology or analytical concepts expressed in an Indo-European language. Test post-PIE innovation, BMAC/Oxus and other contact, borrowing, multilingual formation and extinct-language contributions feature by feature.
4. **Audit nationalist capture:** test Hindu-nationalist, Tamil/Dravidian-nationalist, Iranian-nationalist, Greek/European-first, Afrocentric and civilizational-priority narratives by the same chronological, philological, archaeological and material standards. Equal standards do not require pretending that traditions had equal power to preserve, excavate, translate or globalize their records.

For every major conclusion include an **archive-power note**: whose evidence survives, who preserved or translated it, which population is absent, and whether absence is being mistaken for nonexistence. Also include a **narrative audit** showing the strongest dominant interpretation, the strongest marginalized/heterodox interpretation, the evidence each explains, what each ignores, and what result survives after both are tested.

Produce this packet, in Markdown plus CSV/JSON where useful:

1. A concise answer to the actual research question, with strongest findings and material limits.
2. A claim ledger: local claim ID, exact proposed public sentence, supporting source/locator, source access level, evidence role, inference explanation, counter-evidence, scope/date/variety, status (supported/revise/open/reject), and affected existing page/claim IDs.
3. A source register: author, title, date, publication/edition, URL, pages or passage IDs actually consulted, access limits and rights leads. Do not treat publication prestige as verification.
4. A chronology separating events, composition, redaction, witnesses, commentary and modern interpretation as relevant. Date ranges must carry a basis.
5. A comparison table using matched questions and explicitly identifying unequal evidence. Mark analogy, genealogy, transmission and uncertain relations distinctly.
6. A disposition manifest: existing pages to update, proposed new sections/pages, shared feature needs, merge opportunities and unresolved research. Use LS IDs from the master list.
7. Public-facing draft copy derived only from supported claims, with contextual sources and clear uncertainty. Preserve original-language examples, transliteration, gloss and translation as distinct fields. Difficult examples require qualified review.
8. A bounded interaction brief: visitor question, input records, meaningful action, explanation, source inspection, accessibility alternative, and what would count as success.
9. A correction list for the supplied conversation, including unsupported attractive claims and overconfident objections.
10. Work remaining: specific missing sources or expert tasks, not vague calls for more research.

Do not generate production HTML or rewrite navigation. Do not claim benchmark execution, manuscript examination or corpus counting unless actually performed and logged. Model agreement is not scholarly verification. End with a handoff summary that another researcher or developer can use without the original conversation.

## R1 — What Tamil Reveals About AI

Investigate LS-01, LS-02 and LS-21. Distinguish three questions: where current models fail on specified Tamil tasks; which linguistic interventions might help; and which improvements have actually been demonstrated.

Start with ILAKKANAM and TamilTok, obtaining the original papers, datasets/code and evaluation details where available. Publication discovery links: [ILAKKANAM](https://aclanthology.org/2026.chipsal-1.17/) and [TamilTok](https://aclanthology.org/2026.dravidianlangtech-1.7/). Do not infer a general cross-language ranking from a Tamil-only benchmark or a cultural-understanding result from a tokenizer experiment.

Cover morphology, sandhi where relevant, agreement, negation, clitics, reference, register/diglossia, dialect/variety, code-mixing and transliteration. Separate modern Tamil competence, historical Tamil reading, cultural knowledge and poetic interpretation. Compare Tamil with relevant languages on matched tasks, not only translated English questions.

Design a modest reproducible experiment contrasting baseline, additional context, modern linguistic annotation and a carefully sourced tiṇai/poetic-context intervention. Treat the last as a hypothesis. Include held-out data, a length-matched irrelevant-context control, native/qualified review, alternative valid readings, contamination checks and task-level scoring. Record model/tokenizer versions, settings, date and spending cap. Do not run paid APIs without an agreed budget.

Explain the difference between token efficiency, linguistic segmentation and downstream accuracy. Examine training-data distribution and representations without presuming models literally use Greek–Latin grammatical categories. Deliver a static, frozen-results-first feature specification; live model calls are a later option.

## R2 — Before Pāṇini and Inside the Grammar

Investigate LS-03, LS-04 and the Sanskrit side of LS-09. Explain the Aṣṭādhyāyī through a few actual derivations, not a sequence of programming metaphors. Verify the roles of pratyāhāras, the sound inventory, it/anubandha markers, anuvṛtti, rule conditions, ordering, exceptions and interpretive traditions. Technical markers are not agglutinative morphology.

Build an evidence-ranked account of named predecessors, Śākalya, Yāska where chronologically relevant, recitational/phonetic schools, Kātyāyana and Patañjali. Distinguish attested mentions from reconstructed intellectual relationships; do not assume the dates of all Prātiśākhya material precede Pāṇini.

Evaluate Pāṇini's dating and northwestern association through scholarly arguments. Investigate multilingual context without assigning undocumented home languages or identities. Assess the hypothesis that oral memorization rewarded compressed notation; do not present that explanation as established for every device.

For rule-conflict debates, compare Rajpopat's actual proposal with substantive scholarly responses and established interpretations. Do not repeat a news headline as proof a long-standing problem was conclusively solved. Reserve later divine attribution for R8, sharing source IDs rather than producing incompatible chronologies.

## R3 — Did Later Rules Reshape Earlier Vedic Speech?

The owner's question is specifically whether later recitational or grammatical standardization could have altered earlier transmitted sound patterns and forms, particularly in Ṛgveda books 2–7. Do not answer only that speech existed before grammar or that Pāṇini did not compose the hymns.

Investigate LS-05, LS-06 and LS-15. Compare transmitted Saṃhitā forms, Padapāṭha segmentation, metrical evidence, scholarly restorations, school-specific phonetic treatments and relevant Pāṇinian rules. Identify concrete cases where transmitted forms preserve older features, reflect normalization, or remain disputed. Distinguish attestation from reconstruction and date the proposed intervention where evidence permits.

Use Old Avestan as a comparative witness with its own oral and manuscript history; distinguish Old and Younger Avestan. Use Mitanni's limited Indo-Aryan names and technical vocabulary only for questions its corpus can answer. It cannot supply a full syntax or act as strong negative evidence for the absence of grammatical scholarship.

Produce a small matched example table: source form, normalized transcription, relevant linguistic feature, dating basis, comparison form, proposed later change, alternative explanation and confidence. Include accent, vowels, consonants, morphology and metre where supported. Separate deliberate grammatical intervention from recitational change, natural language change and modern editorial normalization. A mixed or indeterminate answer is acceptable if that is what the evidence supports.

## R4 — Before Tolkāppiyam and Meaning Has a Landscape

Investigate LS-07, LS-08, LS-09, LS-11 and the Tamil-context side of LS-19. Give Tamil's intellectual architecture its own account rather than describing it chiefly as a response to Sanskrit.

Establish the text's divisions, proposed layers, editions, commentary history and contested dating. Distinguish traditions about Agattiyam/Agastya from recoverable predecessor texts. Evaluate particular arguments about Sanskrit interaction without treating influence as either total derivation or contamination.

Use actual passages for eḻuttu, col, poruḷ, tiṇai, uḷḷuṟai and meyppāṭu. Separate the three-part Tolkāppiyam from later fivefold grammatical-literary classifications. Compare poetry, context and grammatical analysis through matched problems; do not imply Sanskrit or Greek lacks contextual meaning.

Explain consonant classifications and articulation carefully, including modern terminology's imperfect fit, phoneme/allophone distinctions, old āytam and uncertainty. Supply original Tamil, edition/verse locator, transliteration, gloss, translation and interpretive alternatives for each exhibit example.

Deliver a context-explorer specification in which genre, speaker and situation change interpretation without mechanically mapping one landscape to one emotion. Supply R1 with a small expert-reviewable candidate set for an AI experiment, explicitly separate from claims about historical intent or proven computational improvement.

## R5 — Who Mapped the Mouth? Writing, Sound and Dates

Investigate LS-10, LS-11, LS-12 and LS-13. Separate articulatory description, phonological classification, writing-system structure and archaeological dating.

For proposed priority claims, define the feature being compared and the surviving source. Include South Asian, Greek, Arabic, Chinese, Mesopotamian and Egyptian evidence appropriate to each period; do not infer absence from an unsearched corpus. Coordinate theoretical comparisons with R6.

Compare Tamil uyir/mei/uyirmei with broader Brahmic mechanisms and selected Meroitic/Geʿez examples. Verify chronology and the actual function of signs. Similar encoding principles are not proof of genealogy or borrowing.

For Brāhmī before Aśoka, build a site-level table for Anurādhapura and relevant peninsular finds. Record inscription identification, proposed language, layer, sample/material dated, laboratory/report locator, calibrated range, association between sample and sherd, incision timing, stratigraphic concerns and alternative readings. Trace recent handbook claims to the underlying excavation and dating reports.

Distinguish earliest known sample, earliest securely dated writing, geographical distribution and place of invention. None automatically entails the next. Design a modern anatomical diagram with historical labels and explicit source links; historical pronunciation cannot be certified by a generated voice.

## R6 — Multiple Sciences of Language

Investigate LS-09, LS-10, LS-14, LS-15 and LS-16. Compare Mesopotamian scribal work, Egyptian language awareness, Sanskrit, Tamil, Greek, Latin, Chinese and Arabic traditions on their own questions and available evidence.

Use a matrix of phonetics, word formation, syntax, meaning, poetics, pedagogy, formal notation, usage and institutional purpose. Distinguish a single handbook from an entire tradition. Include Stoic analyses and Apollonius where relevant; examine Varro, Donatus and Priscian without dismissing adaptation as intellectually empty.

Investigate Greek/Latin category transfer through specific colonial grammars, original terminology and later critiques. Include examples where categories clarified a phenomenon, where they distorted it, and where local analysts supplied alternatives. Do not claim all Western grammar followed one uninterrupted line or that all models of language share one worldview.

Replace whole-language complexity rankings with phenomenon-specific comparisons. If asserting an earliest or unusually systematic account, define the corpus and criterion. Deliver the Who Invented Grammar? collection narrative and reusable comparison records, with overlap mapped to R2/R4 rather than duplicating their core pages.

## R7 — Contact, Meaning and Directionality

Investigate LS-17, LS-18 and LS-19. Separate evidence of travel/contact, linguistic diffusion and transmission of a specific intellectual argument.

For Indo-Aryan, Dravidian and Munda contact, select a few features and test inheritance, internal change, convergence and borrowing. Treat retroflexion with phonological environments and competing explanations; do not let a sound feature establish the origin of grammatical theory.

For Greek–Indian philosophy, distinguish Pyrrho-related hypotheses from claims about Stoicism. Build a chronology of actual texts and testimonia, including the date and distance of later reports. Similar ideas plus possible contact do not establish directionality. Review strong influence proposals and substantive objections with the same questions.

For Bhartṛhari and sphoṭa, use appropriate translations and specialist interpretation. Compare word/sentence, sequential sound and unified meaning without presenting an ancient text as an anticipation of transformers or as evidence for events centuries earlier. Deliver a contribution/contact graph with independently supported and disputed edges distinguished.

## R8 — When Knowledge Becomes Sacred Authority

Investigate LS-20 and relevant updates to attribution, archive and religious-history pages. Trace the names akṣarasamāmnāya, Śiva/Māheśvara Sūtras and the divine-origin narrative through dated witnesses. Distinguish a tradition's account from evidence of an original author's belief. Separate the phonological strings from the later Kashmir Śaiva text bearing a similar title.

Treat Agastya/Agattiyam traditions with the same method. Investigate what later attribution accomplishes institutionally without assuming every sacred attribution is a deliberate theft.

Where Rudra–Śiva, Viṣṇu, Brahmā or the Trimūrti bear on the proposed exhibit, identify actual passages, textual strata and changes in role; do not conflate an adjective, name, deity and later theological system. This is a bounded attribution history, not a request to rewrite all South Asian religion.

Show what can be established about canon formation, authority and named/unnamed predecessors. Return unsupported proposed origin chains to the research ledger. Cross-link the documented contribution model in Who Made the Past? rather than creating a separate incompatible schema.

## R9 — What Is Inherited, Indic and South Asian in Rigvedic Sound?

Decompose the sound system attested or reconstructed for early Rigvedic Sanskrit into claims about Proto-Indo-European inheritance, Proto-Indo-Iranian developments, Indo-Aryan innovations, likely or proposed South Asian areal influence, and later grammatical classification. Do this feature by feature; do not label the whole table as one historical layer.

Cover vowels and vowel history; inherited stop contrasts; palatal developments; dental/retroflex distinctions; sibilants; nasals; liquids including Rigvedic retroflex-lateral realizations; accent; aspiration; sandhi; and the difference between phoneme inventories and conditioned phones. Test the supplied claim that the classical five-place nasal grid regularizes historically heterogeneous material. Compare whether velar and palatal nasals are place-conditioned in other Indo-European languages before treating them as South Asian evidence.

Use Old Avestan, Younger Avestan and appropriate wider Indo-European evidence to establish reconstruction direction. Ask whether shared Indo-Iranian recitation or sound features could themselves reflect earlier contact; identify the relevant chronology, geography and candidate contact populations. Do not assume Proto-Indo-Iranian was culturally isolated or treat every Indo-Iranian innovation as inherited Proto-Indo-European. Separate plausible contact from recoverable donor identification.

Treat retroflexion through dated distributions and phonological environments. Compare internal Indo-Aryan developments, Dravidian, Munda, Nuristani/Dardic and unidentified-substrate hypotheses. “South Asianized” must resolve into specific evidence. Do not use one sound feature to establish the ancestry of Pāṇinian analysis or the identity of an Indus language.

Return a sound-provenance matrix whose rows are particular features and whose columns include earliest evidence, reconstruction, comparison branches, internal derivation, contact hypothesis, alternatives and assessment. Supply data suitable for an interactive layered mouth map while making clear that a later symmetrical classification is an intellectual analysis of a historically developing system.

## R10 — The Rigveda as a Layered Social and Ritual Archive

Investigate the internal stratification and institutional history of the Ṛgveda, especially books 2–7, the distinct histories of 8 and 9, and later material in 1 and 10. Avoid presenting any book as uniform. Provide the scholarly basis and uncertainty for relative chronology; absolute dates remain separate.

Test the supplied account of poet-priest families, patrons, cattle/horses, praise, raids, conflict, ritual exchange and political consolidation. Ask what proportions or distributions can be established from the original-language corpus, which genre conventions affect the evidence, and what social activity the hymns systematically underrepresent. Compare the surviving Avestan ritual-poetic archive only on matched phenomena and explain its different genre/history. Do not call the oldest corpus merely religion, warfare, patronage or history; show the functions its texts perform.

Examine compilation, arrangement, canonization, recitational fixation and later ritual reuse. Distinguish what the collection says about an earlier event from what continued preservation meant to later institutions. Investigate the relation between early social roles and later hereditary varṇa/caste systems without projecting the latter backward. Treat the Puruṣa hymn, marriage, death, cosmology, abstract speculation and deity prominence with passage-level strata. Re-audit the live site's “ninety-nine forts,” enemy-name, payment/patronage and late-hymn pages rather than proposing duplicates. Test fort counts, recurrent numbers, archaeological date ranges and the distinction between Mature Harappan cities, post-urban settlements and BMAC candidates.

Deliver an RV citation schema: hymn/verse, book/collection context, relative stratum and basis, genre/function, named speaker/patron where established, geography, source witness/edition, key linguistic features and limits. For the forts component, enumerate relevant *pur* passages rather than building around one repeated number: record 90/99/100 and other counts, descriptors, enemy, patron, poet lineage, cattle/treasure/water context, proposed geography and whether geography is textual, inferred or unknown. Never place a passage at an archaeological site without a stated inference chain. Add feature briefs for “THE RIGVEDA IS NOT ONE MOMENT” and “THE 99 FORTS: WHAT DID THE POETS CLAIM TO DESTROY?”, and identify existing Mela Keela pages whose generalizations require a stratum label. Add a comparative dossier on ruler–priest–poet legitimation in selected Mesopotamian, Egyptian, Elamite, Indo-Iranian and Rigvedic contexts, distinguishing structural analogy, plausible transmission and demonstrated transmission.

## R11 — Substrate Vocabulary and Grammatical Ontologies

Investigate proposed non-Indo-European vocabulary in the Rigveda and comparisons among Indo-European, Dravidian, Munda, Sumerian, Elamite, Hurrian, Semitic, Egyptian and Old Chinese grammatical categories. Keep lexical borrowing, typological resemblance, areal convergence and genealogical relationship distinct.

For Kuiper, Witzel and subsequent scholarship, do not reproduce headline totals until the exact list, inclusion criteria and denominator are available. Build a lemma-level sample containing Rigvedic locator, meaning in context, morphology/phonotactics, proposed donor or “unknown,” competing etymologies, semantic field, stratum and assessment. Search DEDR and relevant Austroasiatic/Indo-European resources before stating no candidate exists. Unknown does not mean Indus, Para-Munda or Dravidian.

Assess whether suspected loans cluster in agriculture, flora/fauna, craft, household life, music, ritual or names using counted denominators. Separate personal/place names from common vocabulary. Examine what each distribution could imply and what corpus/selection bias prevents it from implying.

Give *kīnāśa* in Ṛgveda 4.57.8 a transparent candidate-etymology record. Test inherited Indo-Aryan proposals; the Tamil/Dravidian *kiṇṭu* “dig/root up” comparison and its reconstructible cognates; possible recipient-language remodeling; proposed Munda/Central-Asian alternatives; and accidental resemblance. Require chronological plausibility and parallel sound substitutions. Do not let an unidentified donor outrank a testable Dravidian candidate by default, and do not promote semantic proximity into proof.

Compare grammatical ontology through matched phenomena: gender/noun class, animacy/person/human distinctions, number and dual, alignment and agreement. Do not equate Tamil uyartiṇai/aḵṟiṇai, Sumerian personal/nonpersonal behavior and Elamite animate classes without describing each actual system. Shared dual number does not demonstrate an Indo-European–Semitic relationship; absence of grammatical gender does not mean a society was “beyond gender.”

Audit Elamo-Dravidian and Sumerian-Dravidian claims according to regular correspondences and scholarly reception. Deliver a feature brief for “HOW LANGUAGES CLASSIFY BEINGS” and a second for “THE WORDS WHOSE LANGUAGES VANISHED,” with the unknown field visible and no invented family assignment.

## R12 — The Oxus Interface and Indo-Iranian Contact Before the Split

Investigate the BMAC/Oxus world as a possible contact environment in the formation of Proto-Indo-Iranian vocabulary, technologies and ritual-poetic institutions. Separate linguistic reconstruction labels from political, genetic and archaeological identities. “Iranian-related ancestry,” “Proto-Iranian,” BMAC material culture and an unknown BMAC language are not interchangeable.

Build a dated geography of Sintashta/Andronovo-related steppe worlds, Bactria–Margiana/Oxus sites, the Iranian plateau, Elam, Afghanistan/Helmand, Shortugai and Indus networks. Use settlement reports and ancient-DNA studies at the individual/site level. Distinguish typical ancestry profiles, outliers, population interaction, language shift and unobserved language; genetics cannot name the BMAC language.

Reproduce proposed common Indo-Iranian non-Indo-European loan lists from the relevant linguistic scholarship. For every included form record the Indo-Aryan and Iranian attestations, meaning, proposed donor phonology, semantic field, chronology, alternative etymologies and confidence. Treat Soma/Haoma carefully: distinguish the inherited/derivable name of the pressed substance from proposed substrate plant, offering or priest terminology. Do not turn a ritual loan layer into “Vedic/Avestan religion was BMAC religion.”

Compare what can actually be reconstructed for common Indo-Iranian ritual poetry, sacrifice, memorization, priestly roles and sacred formula with what is specifically attested later in Vedic and Avestan traditions. Deliver an “OXUS INTERFACE” investigation brief and source-linked contact edges for the Atlas. Candidate language relationships to Elamite, Dravidian, Hurro-Urartian or Indus must remain separately scored hypotheses.

## R13 — Stones, Routes and the Political Economy of Exchange

Investigate lapis lazuli, carnelian and selected companion materials as physical tracers through Badakhshan, BMAC, the Iranian plateau, Elam/Susa, Marhaši, Helmand, Shortugai, the Indus, Gujarat/Kutch, Makran, Magan, Dilmun and Mesopotamia from roughly 4000–1000 BCE. Coordinate with existing Meluhha trade and Artifact Atlas coverage; extend or correct those routes before proposing a duplicate general trade page.

For each artifact or textual claim, separate: geological source, manufacturing source, commercial/export source, findspot, laboratory provenance method, textual provenance label and modern museum attribution. Test Badakhshan attribution for particular lapis objects and Gujarat/Cambay or alternative origins for particular carnelian assemblages. A trade name such as “Meluhha carnelian” or “Marhaši carnelian” need not identify a quarry.

Build a primary-text table for Meluhha, Magan, Dilmun and Marhaši occurrences, including text/edition, ruler/date, genre, spelling, goods, ships/land route, translation alternatives and historical limit. Distinguish Sargon's maritime boast from terrestrial campaign records. Do not collapse Marhaši into Meluhha or assign its language without evidence.

Compare trade, diplomatic gift, tribute, tax/route control, raid and conquest as distinct but overlapping acquisition mechanisms. A proposed progression from commerce to coercion must be tested commodity by commodity, not asserted as a universal law. Add a coverage audit of major museums and research institutes: what their public collections explain about extraction, traders, makers, geological/material provenance and uncertainty, and which communities remain unnamed.

Deliver distinct but linked feature briefs for “THE BLUE ROAD” (lapis), “THE RED ROAD” (carnelian), “WHAT MOVED EAST? WHAT MOVED WEST?” and “FIRST THEY TRADED FOR IT. THEN WHO CONTROLLED THE ROAD?”, plus route/object data suitable for Goods → Genes → Words → Sounds → Rituals → Technologies → War filters. Compare how Cambridge scholarship, the British Museum, the Metropolitan Museum, Penn and relevant source-country institutions describe selected objects; record what each establishes, repeats without direct analysis, omits or cannot know. Every edge must carry date, evidence type, direction, confidence and source; dotted uncertainty is not decoration.

## R14 — The Language That Changed as It Moved

Synthesize only accepted records from R3, R9, R11, R12, R16 and R18 into a chronology-plus-geography model from Proto-Indo-Iranian through early/late Vedic, regulated Sanskrit and vernacular Old/Middle Indo-Aryan. Include Old/Younger Avestan as comparisons, not as stations on a Sanskrit line. Keep Proto-Dravidian, Old Tamil, Munda/Austroasiatic candidates and unknown languages visible as contact fields, not descendants.

Model selected sounds, words and grammatical features rather than an entire language. Candidate rows include retroflexion, sibilants, conditioned nasals, vocalic resonants, diphthongs, aspiration, pitch accent, subjunctive/injunctive, infinitives, dual, quotatives and non-finite chaining. Extend the comparison into securely attested inscriptional Prakrits and appropriately described Pāli; do not invent a written vernacular corpus for 1000 BCE or depict Prakrit as corrupted Classical Sanskrit.

Build this specifically as an **Artifact Atlas mode**. The visitor moves a time control while the map reveals: archaeological sites and dated material cultures; directly attested texts/names; reconstructed speech stages; candidate contact fields; material/ritual routes; and the earliest defensible appearance, loss or restructuring of selected linguistic features. Clicking a site or corridor must explain whether it supplies linguistic evidence, only a plausible contact setting, or no language evidence at all.

For each proposed change record: feature ID; earlier state; later state; earliest attestation; reconstruction basis; location/confidence polygon; comparison language; internal-change account; contact candidate(s); archaeological/material correlate; counter-evidence; and assessment. Allow the visitor to switch among `SOUNDS | WORDS | GRAMMAR | NEIGHBOURS | MATERIALS | RITUALS`, and to compare alternative route models rather than view one authoritative steppe-to-India arrow.

Each state change must be typed as inherited, internal innovation, contact-supported, contact-possible, disputed or unknown. Use separate symbols for attested text, reconstructed language, ancestry movement, material exchange and hypothesized language contact. The slider must never imply that a moving language was a single migrating population, that an artifact identifies its maker's language, or that a modern national boundary identifies an ancient speech community. Deliver the full evidence/data schema and a static accessible table first, then the Atlas interaction brief. No speculative animation may outrun the evidence records.

## R15 — Before Alexander: Contact Corridors and Intellectual Transmission

Build a chronology of Achaemenid, Gandhāran, Greek, Egyptian, West/Central Asian and South Asian contact before and after Alexander. Include administratively connected populations, travel, settlements, embassies, texts/testimonia and securely dated opportunities for exchange. Scylax, Herodotus, Achaemenid rule in Gandhāra, Greek communities within the empire and later Greco-Bactrian/Indo-Greek settings require primary or specialist locators.

Compare the chronology of Indian and Greek phonetic/linguistic analysis. Separate an ordinary sound process such as nasal place assimilation, its pre-contact Greek evidence, explicit Greek description, later grammatical systematization and any proposed Indian influence. A corridor plus resemblance is not a transmission chain. Specify what borrowed terminology, distinctive mechanism, testimony or chronological discontinuity would strengthen an influence claim.

Coordinate philosophical directionality with R7 but do not make this packet prove Pyrrhonism, Stoicism or Buddhism from one another. Deliver a “BEFORE ALEXANDER” Atlas layer with evidence-typed routes and a claim ladder: impossible/possible/plausible/supported/demonstrated. Record unequal survival on both sides without turning missing texts into positive evidence.

## R16 — Proto-Dravidian Sibilants, Tamil Script and Borrowed Sound

Investigate the supplied claim that standard Proto-Dravidian reconstruction lacks a native phonemic `/s/` and has no Sanskrit-style `s/ś/ṣ` series. Begin with full comparative reconstructions rather than modern Tamil spelling. Establish the evidence for Proto-Dravidian `*c`, its proposed phonetic values and daughter-language outcomes, including conditioned or branch-specific s-/h-like developments. Distinguish a reconstruction symbol, phoneme, contextual phone, letter and later transliteration.

Trace Old Tamil's native phonological and orthographic resources through Tamil-Brāhmī, later scripts and the adoption/use of Grantha-derived ஜ, ஷ, ஸ and ஹ. Date each graph's relevant attestations and distinguish Sanskrit loanword representation, learned spelling, actual Tamil pronunciation, code/register and modern standardization. Do not describe Tamil as lacking expressive capacity, “forgetting s,” or becoming complete through Sanskrit; equally, do not imply every later sibilant spelling represents an unchanged ancient phoneme.

Build a matched longitudinal table across Proto-Indo-European, Proto-Indo-Iranian, Rigvedic, Classical Sanskrit, selected Middle Indo-Aryan/Pāli outcomes, Proto-Dravidian, Old Tamil and later Tamil. Show where sibilant distinctions were inherited, developed, collapsed, borrowed or graphically accommodated. Connect the records to R9/R14's slider and audit the live `/dravidian-sounds-sanskrit-lacks`, `/two-classical-languages` and `/panini` pages for oversimplification. Deliver copy and an accessible interaction brief provisionally titled “THE SOUNDS A SCRIPT LEARNED TO WRITE.”

## R17 — The Same World, Two Responses: Rigvedic and Old Avestan Archives

Test the proposed contrast between early Rigvedic praise embedded in warrior-patron exchange and the Old Avestan Gāthās as a reformist moral response within a society that also knew cattle raiding, plunder, violent rivals and priestly competition. Do not compare “violent Indians” with “peaceful Iranians,” and do not mistake two differently selected corpora for complete societies.

Use original-language passages and responsible editions/translations. For Rigvedic candidates including RV 6.31.4 and RV 1.130, identify poem, stratum, speaker/poet lineage, patron, deity, fort/cattle/treasure vocabulary, grammatical uncertainties and whether the passage really supports the proposed wealth → praise → divine aid → victory → redistribution cycle. For Old Avestan, identify passages supporting conflict, pastoral loss, hostile ritual specialists, *aša/druj*, and the critique/reorganization of inherited practice. Do not import later Zoroastrian doctrine into the Gāthās without labeling it.

Evaluate at least four explanations for the divergence: genre/survivorship; a historical Zarathustrian ideological break; different political ecologies; different contact histories. Give each the strongest case and disconfirming evidence. Investigate *deva/daēva* and other apparent inversions through dated linguistic and textual evidence; an ideological contrast is not established merely by cognate vocabulary.

Audit the historicity, dating and location of Zaraθuštra, including founder-versus-community composition models and the limits of later biography. Ask what evidence exists for pre-Zarathustrian criticism or rival reform, and distinguish “not preserved” from “did not exist.” Deliver a split-screen evidence feature titled “THE SAME WORLD, TWO RESPONSES,” but include a genre-warning panel that prevents the visual from making a total-society claim.

## R18 — Brahui, North Dravidian and the Languages Left on the Hills

Investigate Brahui through four separate histories: the language; the ancestry of present speakers; Brahui tribal/political identity; and successive Indo-Aryan, Iranian, Balochi and other contact layers. Do not let modern genetics date a language and do not let a linguistic migration model manufacture a recorded population movement.

Build the strongest version of both principal models: long-term northwestern Dravidian continuity with contraction/language shift, and first-millennium-CE migration from central/western India. For each list what it explains, assumptions required, observations it struggles with and evidence that would falsify it. Trace Elfenbein, Morgenstierne, Krishnamurti, McAlpin and relevant newer phylogenetic work through exact arguments rather than reputation. Distinguish branch divergence time from geographic location. Test whether claimed old Indo-Aryan and later Balochi layers genuinely discriminate between the models, and establish the independent chronology/geography of Balochi expansion before treating absent Old Iranian loans as a clock.

Read the modern Brahui genetic literature at method level: sample size, comparator populations, SNP/whole-genome coverage, model design, result and the authors' actual interpretation. Compare ancient-DNA availability by period/site. “Genes do not speak” is a warning against direct language assignment, not permission to ignore demographic evidence. Modern Tamil/Telugu/Kannada populations are not simple proxies for a hypothetical Bronze Age northwestern Dravidian population.

Investigate Brahui people's own historical accounts and contemporary Brahui scholarship through community-authored and locally published material where accessible. Treat oral history as evidence of identity, displacement and political incorporation, not a literal multi-millennial timestamp. Record colonial mediation, translation and archival gaps. Apply the same approach to Kurukh/Oraon and Malto/Maler traditions, including Rohtas/displacement narratives, while protecting living-community specificity and avoiding romantic “tribal fossil” language.

Test the highland-refugia hypothesis with an elevation/state-access map of Brahui, Kurukh and Malto and carefully chosen comparators such as Burushaski, Basque, Caucasian languages, Sardinian and Nuristani. Geography can help preservation but does not prove former continuity. Compare equally strong examples of long-distance language migration such as Romani and Malagasy, asking whether Brahui contains a comparably ordered loan-route signature.

Produce a 500-year-interval Balochistan/northwestern language map from 3000 BCE to 1500 CE. Use confidence polygons and labels `ATTESTED | INFERRED | POSSIBLE | UNKNOWN`; never color the whole region Iranian, Dravidian or Indus without evidence. Add a research protocol for internal Brahui ecological vocabulary, stratified Iranian/Indo-Aryan loans, toponymy, ancient genomes and intermediary-language traces. Deliver “THE LANGUAGE THAT REFUSED TO DISAPPEAR,” “THE LANGUAGES LEFT ON THE HILLS” and “GENES DO NOT SPEAK” briefs. The result may rank long-term continuity as plausible, but must not present Brahui as proof of the Indus language.

## R19 — Before Oil: Hormuz, Corridors and the Recurrence of Coercive Control

Build a sourced chronology of the Gulf/Strait corridor from Bronze Age Dilmun–Magan–Meluhha exchange through Achaemenid, Hellenistic, medieval Indian Ocean, Portuguese, British-imperial and modern energy/shipping eras. Distinguish the Strait of Hormuz as a physical chokepoint from the wider Gulf–Oman–Makran maritime system. Do not project a modern national map or petroleum economy backward.

Use R13's object/route records for copper, carnelian, shell, lapis, timber, ivory, textiles and other supported commodities. Reopen the relevant Sargon inscription in a critical edition: determine what “ships ... moored at Agade” means and do not imply capture or piracy without textual evidence. Model trade, port access, tribute, naval protection, route taxation, blockade, piracy, raid and conquest as distinct relations.

Research organized violence before states through current archaeological scholarship without imposing a single PEACE → WAR evolutionary ladder. Separate interpersonal violence, episodic group conflict, fortified settlement, sustained raiding, professional military institutions and imperial extraction; record regional variation and contested interpretation.

For the modern section, independently verify every supplied claim as of the research date using primary government/legal records and multiple reliable contemporaneous sources. Do not assume claims about U.S.–Iran hostilities, blockade, oil flows, Venezuela, ownership stakes, Maduro, Puerto Rico or commodity shares are correct because they appeared in the conversation. Record event date, publication date, legal status, changed/contested facts and archived source. Version-pin all shipping/energy percentages.

Compare ancient and modern systems structurally—control of circulation, coercive bargaining, ownership/tribute, military protection and resource dependence—without saying Sargon equals any modern leader or erasing international law, corporations, sovereignty and global finance. Deliver “BEFORE OIL: THE STRAIT” as an ancient-to-present evidence timeline and a separately held essay brief on power over corridors. The current-affairs layer expires unless refreshed; the ancient route must remain usable without it.

## Challenge prompt — apply to each packet before consolidation

Audit this packet against the shared contract. Independently reopen its most consequential sources. Identify unsupported bridges, mistaken locators, dates borrowed from later witnesses, scope inflation, missing alternatives and numbers without denominators. Test objections as rigorously as preferred claims; do not replace supported findings with generic uncertainty.

Return: accepted claims; corrected wording with evidence; claims to hold; specific missing sources; and contradictions with the existing museum correction ledger or other packets. Check whether each proposed interactive implies more certainty than its supporting prose. For technical benchmarks inspect the actual tasks, baselines, evaluation and reproducibility. Agreement with another model is not verification.

Revise the packet after the audit and list unresolved specialist decisions explicitly. Do not silently publish claims labeled open merely because they make an attractive title.

## Claude Code implementation prompt — after repository reconciliation

Inputs: current repository instructions, the live-site audit, repository-reconciliation manifest, approved release, reviewed R packets where needed, accepted claim/source records, assets with rights, agreed first-batch scope, and the current master correction ledger.

First reconcile overlapping claims, dates, terminology and page destinations. Return conflicts that cannot be resolved from accepted evidence; do not invent a synthesis. Preserve accepted research uncertainty in both prose and visuals. Retain stable IDs and trace public statements to source locators.

Implement the agreed batch using current components and design rules. Prefer extensions and shared features over duplicate pages. Begin with one complete source → comparison → explanation → saved record journey. Keep original-language text, gloss and translation separate. Expose evidence contextually rather than adding repeated method cards everywhere.

Update relevant navigation, search, research index, exhibits, ledger, metadata and redirects. Verify source links, diacritics and Tamil rendering, responsive layout, keyboard access, reduced motion and meaningful noninteractive alternatives. Preserve previously corrected claims. Mark generated audio or reconstructions honestly and keep them separate from source evidence.

Return changed files, claim changes, verification results, unresolved dependencies and a preview. Do not deploy without the owner's deployment instruction. Do not substitute generated HTML from unrelated chats for the repository's integrated components. If a research result changes, identify all affected text, examples and visual relationships.

## Operating controls

Use one dated live-site audit, one repository reconciliation, one claim/source register, one rights register and one correction history across all packets. Record research/review/annotation/development effort per case and distinguish founder time from cash. Reuse published tools where suitable; build only the distinctive museum interactions. Defer full grammar engines, model training and paid live comparisons until a bounded pilot and budget justify them.

The first release can consist of revised language coverage, one carefully sourced Tamil example and one historical transmission investigation. Expansion depends on evidence readiness, visitor understanding and the effort required to author a second case—not on how many pages a model can generate.
