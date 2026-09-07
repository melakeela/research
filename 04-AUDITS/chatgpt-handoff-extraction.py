# -*- coding: utf-8 -*-
"""Register 01-INHERITED/chatgpt-project-handoff.md into inherited-claims.csv.

Identifier namespace
--------------------
    IH-001 .. IH-369   the Claude handoff (01-INHERITED/claude-project-handoff.md).
                       DECISIONS-NEEDED.md L253 cites that range as a block, so it
                       is not extended here.
    CG-001 ..          this document, 01-INHERITED/chatgpt-project-handoff.md.
                       A separate prefix because the whole point of this pass is
                       telling the two handoffs apart where they disagree.

Status
------
Every row is INHERITED-UNVERIFIED. The handoff's own seven labels -- OWNER
DECISION, VERIFIED FINDING, PROVISIONAL FINDING, HYPOTHESIS, REJECTED,
SUPERSEDED, OPEN -- are recorded in the notes column as a source label and are
never used as the status. The inheritance rule (CLAUDE.md) applies to this
document exactly as it applied to the Claude handoff: the document was written
by a model summarising its own prior conversations, no retrieval happened during
that summarising, and only a retrieval event logged in 02-SOURCES/access-ledger.csv
promotes any row out of INHERITED-UNVERIFIED.

The handoff's own label definitions are worth reading before its labels are
trusted: CG-018 records that its VERIFIED FINDING means only "directly
established in this pass, usually a fact about an inspected document", which it
says explicitly does not verify the history that document discusses.

Locators are file plus line, against the committed copy.
"""
import csv

SRC = "01-INHERITED/chatgpt-project-handoff.md"
ROWS = []

def add(cid, claim, lines, notes):
    ROWS.append((cid, claim, "INHERITED-UNVERIFIED", "", "%s %s" % (SRC, lines), "", "", notes))

# ---------- SECTION 1 : read this before resuming work ----------
add("CG-001",
    "The project's immediate problem is continuity and evidentiary control: earlier counts, research interpretations, design directions and completion claims have repeatedly survived after being corrected, so the useful work must be preserved but its corrections carried with it.",
    "L10",
    "Section 1, the handoff's own framing of why it exists. Unlabelled. Same diagnosis the Claude handoff reaches from the other side of the project (IH-185, IH-251, IH-362); the two handoffs agree that corrections outlive their corrections here.")
add("CG-002",
    "Source-repair v2.1 is a bounded research hold, not a completed linguistic finding: the record may be preserved while unrelated work proceeds, but it cannot populate an established Dravidian-loanword Atlas layer or support conclusions depending on unresolved etymologies.",
    "L14",
    "Section 1, boundary 1 of three. Handoff label: none stated at this line; developed at L209-L210 as VERIFIED FINDING (disposition) and SUPERSEDED/RETAINED. No counterpart anywhere in IH-001 to IH-369 - the Claude handoff records no source-repair sequence at all.")
add("CG-003",
    "The P1-P3 concept direction was retained while its implementation handoff was rejected: evidence/claim/relationship separation and the Atlas ideas survive, but prose rules inside schemas do not constitute enforced validation.",
    "L15",
    "Section 1, boundary 2 of three. Developed at L280 as VERIFIED FINDING (audit disposition). No counterpart in IH-001 to IH-369.")
add("CG-004",
    "Research Batch 1 was rejected as complete and retained as preflight material: source discovery and representative passages are not the requested exhaustive, reproducible corpus registers.",
    "L16",
    "Section 1, boundary 3 of three. Developed at L243 as REJECTED (checkpoint). No counterpart in IH-001 to IH-369.")
add("CG-005",
    "The three boundaries are findings about the retrieved audit records only; the audits use approval language, but their titles and imperative wording alone do not prove that the owner personally ratified every instruction.",
    "L18",
    "Section 1. The handoff's own guard on its evidence. Directly parallel to the Claude handoff's separation of owner decisions from Claude proposals (IH-082), reached independently.")
add("CG-006",
    "The accessible project context lists five substantive ChatGPT threads plus the handoff thread.",
    "L22",
    "Section 1, coverage limits. Distinct from the Claude handoff's five Claude conversations (IH-007 to IH-011); ten threads total across the two handoffs, matching the owner's request at L71 for a setup integrating five Claude and five ChatGPT threads.")
add("CG-007",
    "Two personal-context searches returned selected conversation excerpts and project-file references but explicitly did not return complete transcripts, stable conversation IDs, or a reliable exhaustive conversation inventory; the second search reported its retrieval budget exhausted.",
    "L22",
    "Section 1, coverage limits. The ChatGPT handoff therefore has no thread IDs at all, where the Claude handoff carries hex conversation IDs (IH-007 to IH-011). Asymmetry to preserve: the ChatGPT record is the less locatable of the two.")
add("CG-008",
    "A filename search located extensive project artifacts and 22 Markdown records were downloaded; relevant controlling records, audits, programme sections and design standards were inspected, but not every line of every downloaded document was individually reviewed.",
    "L22",
    "Section 1, coverage limits. Compare IH-363, where the Claude handoff claims all twelve of its project files were read in full. The two handoffs make different completeness claims about their own reading.")
add("CG-009",
    "ZIP internals, PPTX slide content, PDFs and logo pixels were not inspected in this handoff pass.",
    "L22",
    "Section 1, coverage limits. Bears on section 13's artifact register, whose second half is metadata-only.")
add("CG-010",
    "The handoff does not claim that every message in all conversations was reviewed.",
    "L26", "Section 1, coverage limits. Restated at L454 as non-repetition instruction 11.")
add("CG-011",
    "Thread sections use visible thread titles and excerpts; documentary continuations are identified as probable thematic associations, not proven message provenance.",
    "L27",
    "Section 1, coverage limits. Means the T1-T6 attributions in sections 4-8 are association, not provenance - the file-to-thread mapping is explicitly not established (repeated at L98, L157).")
add("CG-012",
    "Historical claims in the handoff are inherited research/audit claims unless explicitly identified otherwise; no new external historical, legal, funding or live-site verification was conducted during compilation.",
    "L28",
    "Section 1, coverage limits. The direct basis for entering every row of this block as INHERITED-UNVERIFIED, exactly as IH-002 and IH-365 are for the Claude handoff. The two handoffs make the same admission independently.")
add("CG-013",
    "The present repository, deployment, branch, source datasets and external Claude threads were not inspected in compiling the handoff.",
    "L29",
    "Section 1, coverage limits. The ChatGPT handoff had no sight of the Claude handoff or of this repository; the cross-references in this register are therefore made here for the first time, not inherited from either document.")
add("CG-014",
    "No project chat links are invented, and the thread labels T1-T6 are local handoff identifiers rather than platform IDs.",
    "L30", "Section 1, coverage limits. T1-T6 in this document are not the T1-T5 of the Claude handoff (IH-007 to IH-011); the two label sets collide and must never be merged.")
add("CG-015",
    "The newest visible project excerpt extends the GitHub/Claude Code setup discussion, and its final setup result is not available.",
    "L31",
    "Section 1, coverage limits. The unrecovered ending is the setup this repository is the outcome of; compare IH-003/IH-364, where the Claude handoff likewise could not retrieve its own most recent session.")
add("CG-016",
    "A full export of the five substantive ChatGPT threads remains necessary to certify completeness; the document is usable meanwhile because it states the missing evidence rather than filling gaps with invented continuity.",
    "L33", "Section 1. Restated at L457 as the outstanding completeness requirement. Parallel to IH-364.")

# ---------- SECTION 2 : status vocabulary and authority ----------
add("CG-017",
    "In the handoff's own vocabulary, OWNER DECISION means a direct owner instruction visible in an excerpt, or one explicitly recorded as owner direction in a source document, with the evidence basis stated; a question or hypothesis is not an approval.",
    "L39",
    "Section 2, label definition. Recorded so that every OWNER DECISION label below can be read against its own definition. Under the inheritance rule an owner decision asserted here is still INHERITED-UNVERIFIED and gets no 09-DECISIONS/OWNER-DECISIONS.csv row; a register row is not a promotion. Same treatment the Claude handoff's HD-01 to HD-20 receive.")
add("CG-018",
    "In the handoff's own vocabulary, VERIFIED FINDING means only that something was directly established in that compilation pass - usually a fact about an inspected document or its stated disposition - and does not independently verify the history discussed by that document.",
    "L40",
    "Section 2, label definition, and the most consequential one. Every VERIFIED FINDING in this document is a statement about a file, not about the past. Read this row before treating any row labelled VERIFIED FINDING below as verified in this repository's sense.")
add("CG-019",
    "In the handoff's own vocabulary, REJECTED means a claim, output or readiness assertion explicitly refused or withdrawn in the available record, with the rejector recorded where known.",
    "L43",
    "Section 2, label definition. Note the qualifier 'where known': many REJECTED items in sections 6-12 do not name who rejected them, so an audit rejection and an owner rejection are not always distinguishable in this document.")
add("CG-020",
    "The handoff's remaining labels are PROVISIONAL FINDING (prior analysis or reported result requiring original-evidence or current-state confirmation), HYPOTHESIS (a proposed explanation requiring tests, which may be the owner's preferred explanation without becoming an institutional conclusion), SUPERSEDED (a prior state displaced by a later correction within the same scope, preserved for chronology) and OPEN (missing evidence, unresolved choice, uncompleted task or access dependency).",
    "L41-L45", "Section 2, label definitions.")
add("CG-021",
    "Authority rule: a direct later owner instruction governs its scope and documentary instructions must be reconciled with it; an assistant's 'approved' is not an owner approval; and implementation permission may not be inferred from a research request, a positive concept review, a filename containing 'final', or an automatically generated closing phrase.",
    "L47",
    "Section 2. Independently reached and materially identical to the Claude handoff's separation of adopted owner decisions from Claude proposals (IH-082) and to the 'a badge is not a record' rule (IH-167, IH-350). Two handoffs converging on the same discipline from different records.")
add("CG-022",
    "The seven handoff labels do not replace the application's separate epistemic, editorial, publication and access statuses: a supported claim may still be under review, private, or dependent on restricted evidence.",
    "L49", "Section 2. Developed as a product requirement at L293 (mixing all statuses into one field is REJECTED) and L290 (access separate from quality and independence).")

# ---------- SECTION 3 : thread inventory ----------
add("CG-023",
    "The thread dates in the inventory identify thread start labels in project context, not the date of every event inside the thread; within-thread excerpts can be later.",
    "L53", "Section 3. Chronology gate on every date in sections 4-8.")
add("CG-024",
    "Thread T1 'Create SVG Diagram Master' (start label 30 Aug 2026, 02:14) carries the design system, the site audit and the repository/agent operating transition, available only as truncated project excerpts plus design/site documents and the latest setup questions.",
    "L57", "Section 3, thread inventory.")
add("CG-025",
    "Thread T2 'Logo concepts for MelaKeela' (start label 3 Sep 2026, 14:00) carries the logo correction sequence and unresolved final artwork, available as truncated direct dialogue plus artifact metadata.",
    "L58", "Section 3, thread inventory.")
add("CG-026",
    "Thread T3 'Create Research Prompt' (start label 4 Sep 2026, 12:21) carries the research-to-site pipeline and the requested implementation follow-through, available as truncated dialogue plus research/controller/recovery documents.",
    "L59", "Section 3, thread inventory.")
add("CG-027",
    "Thread T4 'Create Deck Storyboard' (start label 4 Sep 2026, 18:48) carries the institutional narrative, audience variants and rejected visual execution, available as truncated dialogue, selected timestamped retrieval and deck metadata.",
    "L60", "Section 3, thread inventory.")
add("CG-028",
    "Thread T5 'Critical Historiography Research' (start label 4 Sep 2026, 19:10) carries linguistics, archive/power, chronology, routes and the corrected research holds, available as truncated owner questions plus extensive thematic research records.",
    "L61", "Section 3, thread inventory. The substantive research thread; section 8 is its content.")
add("CG-029",
    "Thread T6 'Create Project Handoff Markdown' (start label 6 Sep 2026, 17:25) is the handoff thread itself and produced no independent historical findings.",
    "L62", "Section 3, thread inventory.")
add("CG-030",
    "Two related conversations sit outside the confirmed project inventory: 'Compare Mayalakila Content' (2 Sep), which requested a comparison of MelaKeela with Praveen Mohan, Clyde Winters and Iravatham Mahadevan and asked about ahimsa versus the early Rigvedic mandalas; and 'Assessing Praveen Mohan' (2 Sep), on credibility and profitability. Their answers were not retrieved.",
    "L64",
    "Section 3. Explicitly dependencies to recover, not completed comparative findings. Mahadevan is already load-bearing in this repository through IH-142 (megalithic graffiti continue Indus signs); Winters and Mohan appear nowhere in IH-001 to IH-369. New recovery dependency.")

# ---------- SECTION 4 : T1, design / site / operating transition ----------
add("CG-031",
    "The owner renamed the GitHub account from ZoaltOPS to melakeela and the original repository from melakeela to site.",
    "L70",
    "Section 4. Handoff label: OWNER DECISION - direct excerpt, with the handoff noting these are owner-reported changes, not verified remote state. Corroborated in this repository by CLAUDE.md ('the website lives in melakeela/site') and by this repository's own path melakeela/research, though that corroboration is a repository fact and does not promote the row.")
add("CG-032",
    "The owner wants a thorough operating setup integrating five Claude threads, five ChatGPT threads and the existing Claude Code work; later questions request a description/README for a new research repository, sensible chat names, linking a new Claude Code thread, and Codex setup.",
    "L71",
    "Section 4. Handoff label: OWNER DECISION - direct excerpt. This repository is the partial answer; CLAUDE.md records Codex as the independent PR reviewer. Compare IH-368/IH-269, where the Claude handoff names the missing Git repository as the highest standing risk. The two handoffs converge on this repository as the fix.")
add("CG-033",
    "The creation and configuration of the research repository, its README, permissions, branches and linkage are not proved by the available excerpts; the owner reports holding the latest research ZIP and claude-project-handoff.md, whose exact contents were not inspected.",
    "L72",
    "Section 4. Handoff label: OPEN. Partly closed by this repository, which now holds claude-project-handoff.md and this file; the research ZIP contents remain uninspected.")
add("CG-034",
    "The 1 September curatorial audit assessed 96 HTML pages: 46 keep, 20 revise, 15 hold, 11 split, 4 merge, with risk buckets of 52 low, 23 medium, 6 high and 15 critical.",
    "L73",
    "Section 4. Handoff label: PROVISIONAL FINDING - documentary, with the handoff stressing these are historical audit categories, not a current inventory or a certification of historical truth. Every figure is reproduced exactly by the audit committed to this repository: 01-INHERITED/curatorial-audit-v1.1/summary.csv (96/46/20/15/11/4) and page-audit.csv tallied by column (Low 52, Medium 23, High 6, Critical 15; MVP Yes 15). That establishes the handoff quoted its source correctly. It does not promote the row: the audit itself is INHERITED-UNVERIFIED and its own method-limits.csv calls it editorial and source-risk triage, not completed peer review.")
add("CG-035",
    "PHASE-1-PROPOSAL.md explicitly describes itself as a proposal with no site mutations, and identifies a 105-page archive against a 96-page curatorial baseline.",
    "L74",
    "Section 4. Handoff label: VERIFIED FINDING - document content, meaning a fact about the inspected file (see CG-018). PHASE-1-PROPOSAL.md is not in this repository; the 96-page baseline is (01-INHERITED/curatorial-audit-v1.1, baseline veli-site(3).zip, 2026-09-01).")
add("CG-036",
    "The Phase-1 proposal reports that script-src 'self' blocked inline JavaScript, that the Artifact Atlas and mlecha rendered only navigation under a CSP reproduction and search was nonfunctional, and it recommends externalising scripts without weakening CSP.",
    "L75",
    "Section 4. Handoff label: PROVISIONAL FINDING - reported technical test; the handoff did not rerun the browser test or establish whether the breakage remains. Independent partial corroboration in the Claude handoff: IH-201 records /artifact-atlas returning no text to a fetcher because it is JS-rendered, and IH-009 records the same from a live check. Two handoffs, two records, the same symptom on the same page - but neither is a retrieval, and the CSP diagnosis is only in this one.")
add("CG-037",
    "Correction 1 of 6 in T1's ordered chronology: a 96-page archive supported the original audit and the proposed 15-page launch.",
    "L79", "Section 4, corrections in order. Corroborated by 01-INHERITED/curatorial-audit-v1.1 (96 pages, 15 MVP candidates).")
add("CG-038",
    "Correction 2 of 6: the later 105-page archive invalidated direct reuse of the 96-page inventory, because renamed routes and additional pages required reconciliation.",
    "L80", "Section 4, corrections in order.")
add("CG-039",
    "Correction 3 of 6: a separate 58-file working subset was incorrectly treated as the whole platform.",
    "L81",
    "Section 4, corrections in order. CONTRADICTS the Claude handoff on the same 58: IH-007 and IH-185 treat 58 as the platform's true size on 30 August, the first term of a growth series 58-69-75-85. Here 58 is not a date in a growth series but a subset error. Corroborated on the ChatGPT side by 01-INHERITED/site-review/MELAKEELASITEREVIEWRUNNINGLIST.md L642. Both readings registered; not resolved here.")
add("CG-040",
    "Correction 4 of 6: a 108-route report corrected the 58-file subset error but was itself later overtaken by a reported 133-route/page integration.",
    "L82",
    "Section 4, corrections in order. Corroborated at 01-INHERITED/site-review/MELAKEELASITEREVIEWRUNNINGLIST.md L558 and L642. Neither 108 nor 133 appears anywhere in IH-001 to IH-369; the Claude handoff's series tops out at 127 counted and ~135 including routes and .md files (IH-054, IH-251).")
add("CG-041",
    "Correction 5 of 6: the running list withdrew unsupported absence claims that had been based on the 58-file subset, and required current-route reconciliation.",
    "L83",
    "Section 4, corrections in order. Restated at L303. A negative-evidence failure of exactly the class the constitution's section 6 governs: absence asserted from a partial corpus. Compare the Claude handoff's own instance, IH-047, where 33 NO-SRC pages proved on reading to be mostly false positives.")
add("CG-042",
    "Correction 6 of 6: the later owner setup requests move toward an integrated research/production workflow but do not establish that remote setup is complete.",
    "L84", "Section 4, corrections in order.")
add("CG-043",
    "All older scale figures are superseded as statements of current platform size and remain valid only as explicitly bounded historical snapshots; pages, HTML files, content routes and redirects must not be added or compared as though they are the same unit.",
    "L86",
    "Section 4. Handoff label: SUPERSEDED. The unit-conflation rule is sharper than anything in the Claude handoff, which records the disagreement (IH-251) and the fix 'whichever count is derivable from the repository at build time' (IH-185) without naming the four different units. Both registered; this one adds the diagnosis.")
add("CG-044",
    "The early architecture separates threshold, foyer, Explore, Exhibits, Evidence and Learn/Index functions; later running-list direction asks for a short visual Veli threshold, an evidence-rich foyer, a selective gallery and an exhaustive Research Index, and these functions must not become several versions of one card catalogue.",
    "L90", "Section 4, page/exhibit and visual work.")
add("CG-045",
    "One compact internal header carrying logo, search and menu symbol, with no repeated Method row and no duplicate search; a threshold without a conventional header; and concise contextual evidence access rather than repeated public audit labels.",
    "L92",
    "Section 4. Handoff label: OWNER DECISION - recorded in running list. Corroborated in this repository at 01-INHERITED/site-review/MELAKEELASITEREVIEWRUNNINGLIST.md L45 and L47, which the handoff has cited accurately. No counterpart in IH-001 to IH-369; the Claude handoff records the header question only through the external review's accessibility list (IH-318).")
add("CG-046",
    "There is an open visual conflict: the earlier doctrine explicitly rejects uniform near-black treatment and makes an open living field the master environment, while the later public-copy standard explicitly reinstates a near-black field under 'THE FIELD REVEALS THE RECORD'; the two must not be silently collapsed into one approved palette.",
    "L94",
    "Section 4. Handoff label: OPEN visual conflict; developed at L350-L356. CONTRADICTS the Claude handoff, which records the dark ground not as one side of a live conflict but as a settled owner decision - IH-065 ('dark ground, velippatu, colour encodes argument, grey #5f6f7a means NO DATA always') and IH-066 (the owner's 'I like the darkness'). Both registered. The disagreement is not resolved here and is a candidate for DECISIONS-NEEDED.md.")
add("CG-047",
    "The T1 associated records are mela-keela-curatorial-audit-v1.xlsx and its (1) copy, both curatorial-plan Markdown files, mela-keela-curatorial-package-v1.zip, PHASE-1-PROPOSAL.md, design/brand kits, site ZIP versions, MELA-KEELA-VELI-DESIGN-DOCTRINE.md and the running review list; the exact creation-thread mapping is not established by file metadata.",
    "L98", "Section 4, artifacts and dependencies. See CG-011: file-to-thread attribution is association, not provenance.")
add("CG-048",
    "T1 completion work outstanding: inspect the current site repository and deployment; reconcile routes and data counts; preserve redirects; verify the CSP fixes and entry CTA; finish approved prototypes with desktop and mobile evidence; recover all setup outputs; and import the Claude and ChatGPT handoffs without replacing one with the other.",
    "L100",
    "Section 4. Handoff label: OPEN completion, with the note that no repository creation or production change was performed in the handoff pass. 'Without replacing one with the other' is the instruction this register pass is executing: both handoffs are registered, neither overwrites the other.")

# ---------- SECTION 5 : T2, logo ----------
add("CG-049",
    "The owner asked for a mark grounded in MelaKeela's up/down or upside-down meaning and its association with Melakam/Keezhadi.",
    "L106",
    "Section 5, step 1 of the correction chronology. Handoff label: OWNER DECISION - direct excerpt, with the handoff stating this records brand intent, not a verified linguistic etymology. The mela/kila etymology is owed Tamil-dictionary and native-speaker confirmation on the Claude side too (IH-314). The Keezhadi association is a separate claim from the Keezhadi excavation record (IH-113).")
add("CG-050", "The owner requested eight distinct professional logo concepts.", "L107",
    "Section 5, step 2. Handoff label: OWNER DECISION.")
add("CG-051",
    "The first logo results did not settle the direction; the owner asked for another attempt using a rotated M and K, stacked and potentially Brahmi-like, with alternatives including up/down/lateral arrows and star-like smaller spokes.",
    "L108", "Section 5, step 3. Handoff label: REJECTED / revision requested.")
add("CG-052",
    "The owner selected a variation of the 'top right' concept, with only the vertical line black and the other lines in one shared colour.",
    "L109",
    "Section 5, step 4. Handoff label: OWNER DECISION. The most specific artwork decision in either handoff. IH-001 to IH-369 record no logo selection at all; the Claude handoff's only mark-related row is IH-199, which lists 'a wordmark not a symbol' among visual directions explicitly NOT adopted. Registered as a disagreement in emphasis rather than in fact: the Claude record has a gap here, not a contrary claim.")
add("CG-053",
    "The final logo phrase 'Yes let's run with this by not + veli by veli' is ambiguous in the available excerpt, and final lockup wording must not be invented from it.",
    "L110", "Section 5, step 5. Handoff label: OPEN.")
add("CG-054",
    "A misspelled 'keela' logo was rejected on 1 September; the assistant then proposed mathematical glyph mapping, vector paths and rotation testing, which is a proposal and not proof that the final mark was produced.",
    "L111",
    "Section 5, step 6. Handoff label: REJECTED, from a separately retrieved earlier logo exchange whose exact thread attribution is unavailable. Spelling is load-bearing in both handoffs: IH-062 fixes the name as Veli with retroflex l, and L345 here requires exact wordmark spelling.")
add("CG-055",
    "Multiple concept grids, ambigram explorations, horizon/reflection marks and VELI Compass Field Logo.png exist in the discovered artifact inventory, but their existence does not identify the selected final master.",
    "L115", "Section 5. Handoff label: VERIFIED FINDING - metadata only. See CG-018 and CG-009: metadata only, no pixels inspected.")
add("CG-056",
    "Outstanding logo work: retrieve the actual selected image together with the owner's response; identify the final vector master, spelling, permitted colour variants and lockup; and verify 90 and 180 degree rotation and small-size readability.",
    "L117", "Section 5. Handoff label: OPEN. Corresponds to intake priority 9 at L429.")
add("CG-057",
    "Brahmi inspiration in the mark must not be presented as an authenticated ancient letter reading without epigraphic evidence, and a concept sheet is not a deployable identity system.",
    "L117",
    "Section 5. Handoff label: OPEN. Bears directly on IH-023 and IH-151, where the Claude handoff records that Brahmi is morphologically the feminine of brahman and that the script name is a retroactive label (IH-102). A Brahmi-like mark carries that whole contested history into the identity.")
add("CG-058",
    "The logo thread established no historical research conclusion, and the logo must not be regenerated or substituted while unrelated page work proceeds.",
    "L119", "Section 5. Restated at L453 as non-repetition instruction 10.")

# ---------- SECTION 6 : T3, research prompt and research operating system ----------
add("CG-059",
    "The supplied text introduces 'THE FIELD REVEALS THE RECORD': a trace enters alone; date and place constrain it; relationships are earned; dashed and broken lines mark uncertainty; and contradiction may interrupt the composition. The quoted text calls the narrative locked, but its authorship and approval chain are not fully visible.",
    "L125",
    "Section 6. Handoff label: PROVISIONAL FINDING / design proposal. The same phrase reappears at L354 as the later dark-field standard and at L214 in the deck constitution the Claude handoff records as IH-214 ('the field reveals the record'). One phrase, three records - the only point where the two handoffs quote the same string.")
add("CG-060",
    "The owner asked what else should update MelaKeela.com and followed with 'Ok,' 'Where is it?' and 'So build it?', which are requests for concrete follow-through rather than an invitation to keep producing prompts indefinitely.",
    "L126", "Section 6. Handoff label: OWNER DECISION - direct excerpt.")
add("CG-061",
    "The exact promised build scope and its subsequent implementation are not recoverable from the excerpt; it must neither be claimed as built nor erased by an older generic hold.",
    "L127", "Section 6. Handoff label: OPEN.")
add("CG-062",
    "The source-independence update and the universal constitution require preserving accumulated work, auditing inherited claims, recording source ancestry and correcting the current substrate packet before resuming its dependent queue, and they reject balanced-narrative theatre in favour of evidence weighting.",
    "L131",
    "Section 6, documentary continuation. This is the ancestor of this repository's governing principle: CLAUDE.md 'Do not balance narratives. Weight explanations.' and 00-CONTROLLER/METHODOLOGY-CONSTITUTION.md. The constitution is committed here unchanged, so the requirement is live, not merely inherited - but this row records the handoff's report of it, which stays INHERITED-UNVERIFIED.")
add("CG-063",
    "The controller update requires DECK-SITE-COVERAGE.csv and coverage of backlog items 1-89, and the amended-checkpoint audit reports 89 backlog IDs and 41 vision items of which 23 are NOT FOUND.",
    "L133",
    "Section 6. Handoff label: VERIFIED FINDING - inspected records, with the handoff stating these figures describe that checkpoint and are not independently verified live gaps. The 89-item backlog is what this repository's 06-BACKLOG/ is for; DECK-SITE-COVERAGE.csv and BACKLOG-COVERAGE.csv do not yet exist here. Nothing in IH-001 to IH-369 carries an 89-item backlog; the Claude handoff's backlog is VELI-03 items 1-11 (IH-195).")
add("CG-064",
    "Structural presence was mistaken for research completion: complete-looking folders, CSVs or JSON do not demonstrate exhaustive searches, valid etymologies or production readiness.",
    "L135",
    "Section 6. Handoff label: REJECTED - audit disposition. The single most transferable failure in this document and the one most directly aimed at a register-building pass like this one. Compare IH-347 (a search named as owed is a dependency; a page depending on it is INCOMPLETE) and IH-349 (counts are data-derived, never a stated figure taken on trust). Restated at L446 as non-repetition instruction 4.")
add("CG-065",
    "Core principle to retain: separate event, composition, attestation, redaction, copying, translation, excavation and publication dates.",
    "L139",
    "Section 6. Live in this repository as CLAUDE.md method step 2 and constitution section 5. Independently present in the Claude handoff as IH-336 (two chronological instruments) and IH-339 (attestation is not derivation is not meaning).")
add("CG-066",
    "Core principle to retain: treat language, ancestry, population, material culture, religion, polity, caste and modern identity as separate domains.",
    "L140",
    "Section 6. Live as CLAUDE.md method step 10 and the bridges register. Independently present in the Claude handoff as IH-030 (language and ancestry move independently) and IH-359.")
add("CG-067",
    "Core principle to retain: every cross-domain bridge is a claim with evidence, mechanism and limitations.",
    "L141", "Section 6. Live as CLAUDE.md method step 10.")
add("CG-068",
    "Core principle to retain: source access, methodological quality and independence are three different dimensions.",
    "L142",
    "Section 6. Live as CLAUDE.md source-independence constraint and 02-SOURCES/dependency.csv. Independently present as IH-344 (every scholar cited through another scholar or a slide is HELD until read) and IH-345.")
add("CG-069",
    "Core principle to retain: decolonization, debrahminization and de-Indo-Europeanization remove inherited privileges but do not predetermine the preferred counter-narrative.",
    "L143",
    "Section 6. Live as CLAUDE.md governing principle. Word-for-word convergent with the Claude handoff's IH-361, 'debrahminize = strip the thumb from the scale, not press the other pan'. The two handoffs state the same rule in different metaphors.")
add("CG-070",
    "Core principle to retain: the museum may contradict its owner, prior models, canonical scholarship and nationalist claims when the evidence warrants it.",
    "L144", "Section 6. Live as CLAUDE.md governing principle and constitution section 2.")
add("CG-071",
    "Core principle to retain: record absence by cause - not produced, not preserved, not excavated, not published, not accessible, not recognized, documented destruction, or absent after adequate search.",
    "L145",
    "Section 6. The eight-way typing is live as CLAUDE.md's negative-evidence standard and constitution section 6, and matches it exactly. On the Claude side the same discipline appears as IH-342 (silence in a curated record is not refutation) and IH-005 (NOT FOUND IN THIS SEARCH is not an absence), but without the eight types.")
add("CG-072",
    "The programme recovers Artifact Atlas v2, PROVE IT, WATER, WITNESS, TIME + PLACE, Field Bag, primary-source viewing, evidence search, learning entry and comparative worlds as distinct visitor functions, which is not a commitment to ten separate engines.",
    "L149",
    "Section 6, public-experience outputs. Overlaps the Claude handoff's engine counts: IH-010 (six engines, T4), IH-210 (nine engines, VELI-12), IH-260. Contradiction row X on the Claude side is IH-259/IH-260; the ChatGPT reading at L310 is 'four/six/nine engines'. WITNESS matches IH-212's Witness engine and Field Bag matches IH-212's on-device Field Bag - the strongest product-level agreement between the two handoffs.")
add("CG-073",
    "Each research packet is expected to include page purpose, headline options, page copy, evidence sequence, visual brief, interaction brief, mobile flow, child/family entry, source drawer, claims-used register, assets/rights register and acceptance tests.",
    "L151",
    "Section 6. Twelve required components. Compare CLAUDE.md method step 14, which fixes the public-copy shape (QUESTION / WHAT IS OBSERVED / WHAT THE EVIDENCE SUPPORTS / WHAT COMPLICATES IT / WHAT REMAINS UNKNOWN / MELAKEELA'S CURRENT INTERPRETATION / WHAT WOULD CHANGE IT) but not the packet envelope. Not contradictory; the two describe different layers.")
add("CG-074",
    "A file called approved-page-copy.md cannot imply approval while its status remains provisional; the audit permits the required filename only with the actual status explicit inside it.",
    "L151",
    "Section 6. Handoff label: REJECTED. Same defect class as IH-167 (a 'Verified - scite' badge is not a verification record) and IH-350. Restated at L312 and at L446 as non-repetition instruction 4.")
add("CG-075",
    "Unfinished T3 work: complete the corrections in sections 8-9; reconcile coverage by intellectual substance rather than titles; recover the actual current pages and source datasets; and turn only adequately supported independent claims into page briefs. The running list and source repair are inputs, not substitutes for corpus work or production code.",
    "L155", "Section 6. Handoff label: none; unfinished-work list.")
add("CG-076",
    "T3-associated artifacts include the controller, update and consolidated prompt ZIPs, the 00-04 methodology files, the research-first override, the research-batch rejection, the source-repair audits and the P1-P3 audit; their exact origin thread is not established.",
    "L157", "Section 6. See CG-011.")

# ---------- SECTION 7 : T4, deck storyboard ----------
add("CG-077",
    "The assistant review of 5 Sep 00:39 UTC recommended REVISE rather than rebuild: retain the record/investigation spine and PROVE IT, reduce overlapping diagrams, clarify public experience versus evidence infrastructure, strengthen the Canada case and concrete Living Worlds, and replace startup-style roadmap language.",
    "L163", "Section 7, step 1. Handoff label: PROVISIONAL FINDING - retrieved assistant review, timestamped.")
add("CG-078",
    "The owner directed a revision of the master content architecture without visual redesign in that pass, distinguishing current/live, in development and institutional concept.",
    "L164",
    "Section 7, step 2. Handoff label: OWNER DECISION - retrieved user record, 5 Sep 00:40 UTC. The three-way current/proposed/future separation recurs at L175, L181 and L430 and is the deck's central discipline.")
add("CG-079",
    "The owner directed four audience variants - University/Scholar, Museum/Heritage, Government/Foundation, Major Donor/Philanthropy - sharing a common first 10-12 slides with tailored endings.",
    "L165",
    "Section 7, step 3. Handoff label: OWNER DECISION - retrieved user record, 5 Sep 00:42 UTC. No counterpart in IH-001 to IH-369; the Claude handoff records one 16-slide deck (IH-210) and a nine-role prospectus explicitly NOT adopted (IH-082), not four audience variants.")
add("CG-080",
    "The later Prompt 7 text presents the narrative and audience architecture as locked and requests serious institutional art direction rather than another product-design exercise.",
    "L166", "Section 7, step 4.")
add("CG-081",
    "The decks' visual quality was poor: generic vectors, dashboard and diagram-led layouts, insufficient material presence, and placeholder or process-board language.",
    "L167",
    "Section 7, step 5. Handoff label: REJECTED - direct owner excerpt plus retrieved record, 5 Sep 15:49 UTC. The clearest owner rejection in this document. Compare IH-214, where the Claude handoff records the deck constitution (dark field, vector art from the material culture, evidentiary weight sets visual scale) without any record that its execution was rejected. Registered as a gap on the Claude side, and see CG-105 for the instruction not to let this rejection erase every underlying principle.")
add("CG-082",
    "The owner asked, at 5 Sep 15:53 UTC, whether 16 pages was actually required and whether the content was right.",
    "L168", "Section 7, step 6. Handoff label: OPEN / reopened - direct owner question.")
add("CG-083",
    "In reply, 16 was treated as a continuity constraint rather than an intrinsic requirement and a 15-slide alternative was proposed; the assistant flagged inconsistent and unverified metrics, questionable Keezhadi and PROVE IT specifics, and unapproved governance policies.",
    "L169",
    "Section 7, step 7. Handoff label: PROVISIONAL FINDING - assistant reply, with the handoff noting these concerns are not a fresh slide audit. The Keezhadi caution matches the Claude handoff's own: IH-061 bans any Keeladi claim beyond a specific inscribed mark, and IH-113 records the contested report sequence.")
add("CG-084",
    "'Narrative locked' cannot override the owner's later question about factual content, and no recovered evidence establishes acceptance of a revised 15-slide deck or of a final visual system.",
    "L171",
    "Section 7. Handoff labels: SUPERSEDED within the affected pass, and OPEN. Restated at L308.")
add("CG-085",
    "The current public experience, the proposed prototype and the long-term institution must be visually and verbally distinct.",
    "L175", "Section 7, institutional boundaries.")
add("CG-086",
    "Named academics, museums, universities and potential funders are prospective until their roles are agreed; a suggested council, public governance policy, open licence or partner must not be turned into an existing commitment.",
    "L175",
    "Section 7. Convergent with the Claude handoff independently: IH-061 bans any partner named before written yes, IH-216 records that no contact has been made with the top-ranked partner, and IH-215 records the RMRL bridge as owed. Two handoffs, same rule, different evidence.")
add("CG-087",
    "The children's programme, one-site pilot, language rollout, number of worlds and agency schedule are proposals rather than a financed operating plan; the running list explicitly marks the children's and funding dossier proposed, not adopted, and keeps the Keezhadi versus Tamil-Brahmi or other pilot choice open. The museum is broader than an ages 8-11 product.",
    "L177",
    "Section 7. Corroborated in this repository at 01-INHERITED/site-review/MELAKEELASITEREVIEWRUNNINGLIST.md, section heading L393 ('Children's product and funding dossier - proposed, not adopted') and L404 ('Phase-one audience: ages 8-11 only'), so the handoff has cited its source accurately. On the Claude side IH-210 and IH-212 describe the same children's product (VELI-10, DIG) with age bands but do not record it as unadopted; IH-267 records T4 deferring a separate kids' site against VELI-10 designing it. The proposed-not-adopted status is carried only by this handoff.")
add("CG-088",
    "Deck artifacts found by metadata include multiple institutional vision PPTX versions, a 16-slide PPTX and montage, a three-slide prototype, MELAKEELA-VELI-DECK-v0.1.pdf and art-direction board PPTX variants; no file should be treated as the final approved deck merely because it is newest or contains '16'.",
    "L179",
    "Section 7. MELAKEELA-VELI-DECK-v0.1 and the 16-slide deck are the same artifacts the Claude handoff records at IH-210, built with pptxgenjs and sharp. Both handoffs see the file; only this one warns against reading '16' or recency as approval.")
add("CG-089",
    "Deck completion work outstanding: read the actual deck versions side by side; recover the original vision and the accepted content architecture; correct every current, proposed and future claim; select length to fit content; produce evidence-led visual prototypes; and recover the owner's response before making final-brand claims.",
    "L181", "Section 7. Handoff label: OPEN completion. Corresponds to intake priority 10 at L430.")
add("CG-090",
    "Deck source dependencies: the current inventory, one real source-backed visitor journey, rights-cleared imagery, pilot cost, and signed partner and funding facts.",
    "L181",
    "Section 7. Rights-cleared imagery is the same blocker the Claude handoff records at IH-193 (no photographs are possible from Claude; open-licence or owner-supplied images required) and IH-214 (six hero frames deferred until a rights-cleared visual corpus exists, rights work measured in months).")

# ---------- SECTION 8 : T5, critical historiography ----------
add("CG-091",
    "The owner set the research scope: what Brahui, Kurukh and Malto speakers say about themselves; marginalized and highland geography; persistence versus migration; Balochi and earlier Iranian contact; Indo-Iranian entry chronology; pre-Zarathustrian religion, earlier reform and Zarathustra's historicity; and Proto-Dravidian z notation.",
    "L187",
    "Section 8. Handoff label: OWNER DECISION - research scope. This is the charter for this repository's domain-M work (03-REGISTERS/domain-m-brahui-position.csv, 04-AUDITS/domain-m-method.md). On the Claude side the same subject enters as a hypothesis and a burden-of-proof argument (IH-031, IH-135, IH-156), never as a scoped owner commission; the community-self-description and Zarathustra strands are new here.")
add("CG-092",
    "Owner hypothesis: longer Dravidian continuity and a broader lost distribution may explain Brahui better than a long migration preserving the language, and highland isolation may preserve earlier language features.",
    "L189",
    "Section 8. Handoff label: HYPOTHESIS - owner, explicitly research hypotheses and not accepted evidence of Bronze Age speech geography. Materially the same position the Claude handoff registers at IH-031 and IH-135, and as hypothesis IH-143. Both handoffs agree it is a hypothesis; neither promotes it. Non-repetition instruction 2 (L445) governs its use.")
add("CG-093",
    "The owner doubts a stated post-1500 BCE arrival claim; that disagreement must not be transformed into a verified chronology, nor may the conventional date be made unquestionable by default, and populations, languages, texts and routes must be separated with each dating method's actual reach specified.",
    "L191",
    "Section 8. Handoff label: HYPOTHESIS / expressed disagreement. The symmetrical treatment - neither the owner's doubt nor the conventional date gets a free pass - is the constitution's section 2 discipline applied to the owner. Compare IH-026 (admixture dates are lower bounds on arrival, not arrival dates), which is the Claude handoff's version of the same caution about what a method establishes.")
add("CG-094",
    "The inherited research separates four histories of Brahui - language, ancestry, tribal/political identity and contact strata - and modern genetics does not date the language.",
    "L195",
    "Section 8. Recorded on the Claude side as a page concept, 'Brahui: Four Histories, Not One' at L328 here, and as the principle at IH-030 and IH-359 ('ancient ancestry is not late language'). 'Genes Do Not Speak' at L328 is the same rule as a page title. Strong convergence between the handoffs.")
add("CG-095",
    "Balochi and other Iranian contacts must be dated independently, and continuity, later migration, lost broader distribution and mixed models must all be tested with falsifiers and global controls.",
    "L195",
    "Section 8. Four rival models, not two. The Claude handoff frames it as two (relict versus late migration, IH-031, IH-156); this handoff adds lost-broader-distribution and mixed models as separately testable. Registered as an expansion, not a contradiction.")
add("CG-096",
    "Community oral history needs source language, authorship, translation and context; it is neither disposable nor automatically a literal Bronze Age chronology.",
    "L195",
    "Section 8. The evenhanded treatment the constitution requires for oral/living evidence as its own class. Compare IH-081, where the owner's own field observation is recorded as overriding secondary sources on Tamil cultural practice - a stronger position than this row grants. Both registered.")
add("CG-097",
    "Proto-Dravidian *z must not be read as an ordinary /z/, and reconstruction symbols, phones, phonemes, branch outcomes and script accommodation must be distinguished.",
    "L197",
    "Section 8. The five-way distinction is sharper than the attestation gradient in CLAUDE.md and has no counterpart in IH-001 to IH-369. Relevant to this repository's 03-REGISTERS/domain-e-retroflex-residue.csv work and to the page concept at L327, 'Proto-Dravidian Without a Sanskrit Sibilant Series'.")
add("CG-098",
    "Sound systems and analytical traditions must be compared feature by feature; the Sanskrit five-place analysis, the Tamil 6+6+6 organization and later spelling must not be turned into claims of language superiority.",
    "L197",
    "Section 8. Cuts against prestige bias and counter-narrative bias in one sentence, which is what the two adversarial tests in CLAUDE.md require. Compare IH-103 (Sanskrit lacks the retroflex l, alveolar trill and alveolar n that Tamil-Brahmi invented letters for), which is exactly the kind of finding this row says must not become a superiority claim.")
add("CG-099",
    "Inherited PIE features, Indo-Iranian innovations, BMAC/Oxus contact, Iranian and Indo-Aryan developments, South Asian areality and later scholarly systematization must be separated; shared Vedic and Avestan material is not automatically PIE.",
    "L199", "Section 8. Six strata. No counterpart in IH-001 to IH-369.")
add("CG-100",
    "Neither a peaceful-Iranian versus violent-Indian binary nor a universal religion-versus-economy binary is supported by comparing differently selected archives.",
    "L199",
    "Section 8. An archive-audit finding of the class CLAUDE.md method step 6 requires. Compare IH-071 (northern priority is an artefact of excavation density and publication politics) - same reasoning, different archive.")

# ---------- section 8 : source-repair chronology table ----------
add("CG-101",
    "Source-repair stage 1: the initial inherited substrate packet's bare loanword totals and early-stratum absence depended on sources and strata that were themselves under examination; REJECTED for unreproducible totals and circular dependence, with lists, denominators, chronology and etymologies to be independently reconstructed.",
    "L205",
    "Section 8, source-repair chronology, stage 1 of 6. Handoff label: REJECTED. All six stages are registered separately because the handoff's instruction at L201 is to preserve all stages. Nothing in IH-001 to IH-369 records this sequence.")
add("CG-102",
    "Source-repair stage 2: the amended checkpoint audit claimed 'accepted Dravidian candidates' absent from the family-book core and asserted Tier A comparative security; REJECTED because its own passages include family-book candidates, because it itself cites mayura at RV 3.45.1, and because no complete comparative dossiers supported the secure labels.",
    "L206",
    "Section 8, stage 2 of 6. Handoff label: REJECTED. A self-refuting audit: the document asserting absence cites an instance. mayura at RV 3.45.1 is a checkable locator and is the kind of item this repository's VedaWeb work could settle (02-SOURCES/vedaweb-manifest-2026-09-07.md); it is not checked here and stays INHERITED-UNVERIFIED.")
add("CG-103",
    "Source-repair stage 3: source-repair v2 claimed every family-book occurrence was late or redacted and used later classifications as exclusions; REJECTED because those classifications were not retrieved or were contested, because the Aitareya Brahmana attribution was overextended through Talageri, and because the danda locator is RV 7.33.6, not 7.33.11.",
    "L207",
    "Section 8, stage 3 of 6. Handoff label: REJECTED, with the handoff stating these are audit-reported corrections and not passages newly checked in the handoff pass. Two checkable locators - danda RV 7.33.6 and the corrected 7.33.11 - and one source-dependency failure of the class IH-344 governs (a scholar reached through another scholar). Talageri appears nowhere in IH-001 to IH-369.")
add("CG-104",
    "Source-repair stage 4: the v2 audit's replacement wording said 'most words' fall outside the family books and that occurrence distribution is more secure than chronology; SUPERSEDED by the v2.1 review because the register is non-exhaustive for every candidate, so the replacement itself overclaims.",
    "L208",
    "Section 8, stage 4 of 6. Handoff label: SUPERSEDED. A correction that had to be corrected - the pattern CG-001 names as the project's central problem.")
add("CG-105",
    "Source-repair stage 5: the v2.1 owner-review document found the files present and important errors withdrawn but substantive searches and dossiers incomplete, and it is accepted only as an incomplete HOLD, reporting 0 of 23 exhaustive searches and 0 of 23 complete comparative dossiers.",
    "L209",
    "Section 8, stage 5 of 6. Handoff label: VERIFIED FINDING - disposition, meaning a fact about the document's stated disposition (see CG-018). 0/23 and 0/23 are the sharpest completion figures in either handoff. Belongs in 05-HOLDS/ if and when the underlying register is recovered.")
add("CG-106",
    "Source-repair stage 6: the v2.1 permitted continuation stops the rewriting of empty dossiers and allows independent product and specification work to proceed; the global blockade of unrelated programmes is SUPERSEDED, while the hold on unsupported donor-language, borrowing-direction and dependent chronology claims is RETAINED.",
    "L210",
    "Section 8, stage 6 of 6. Handoff labels: SUPERSEDED and RETAINED in one row, as the source has them. Restated at L311 and at L450 as non-repetition instruction 7. This is the boundary that lets the rest of the museum proceed; it is narrow, and CG-002 states what it does not license.")
add("CG-107",
    "The canonical replacement wording preserved from the v2.1 review is: 'The current non-exhaustive register contains proposed candidate attestations both within and outside Mandalas 2-7. It cannot yet establish exhaustive distribution or chronological absence.'",
    "L214",
    "Section 8, block quotation. The only literal quotation the handoff preserves. It is a negative-evidence formulation of exactly the kind CLAUDE.md's negative-evidence standard requires, and its absence type would be NOT PRODUCED or ABSENT DESPITE ADEQUATE SEARCH only after the searches exist - which CG-105 says they do not.")
add("CG-108",
    "The v2.1 review normalizes 30 occurrence rows to 10 VERIFIED, 3 PARTIAL, 14 UNVERIFIED, 2 UNRESOLVED and 1 NOT LOCATED, and its chronology CSV contains 17 chronology-claim rows rather than 30 hymn datings; these are the review's counts, not a rerun against the underlying ZIP.",
    "L218",
    "Section 8, exact numerical repair. 10+3+14+2+1 = 30, so the normalization is internally consistent. Not re-derived here - the underlying ZIP is not in this repository.")
add("CG-109",
    "Even 'VERIFIED' is incomplete as a composite label, because locator, Samhita, Padapatha, morphology and exhaustive search need separate fields.",
    "L218",
    "Section 8. A schema claim, and a direct criticism of the one-status-per-claim register format this repository uses (CLAUDE.md, register format). Worth raising as a standing question: this register's single status column collapses exactly the five dimensions this row says must be separate. Registered, not acted on.")
add("CG-110",
    "REJECTED: using the 13, 14 and 16 unverified counts interchangeably.",
    "L220",
    "Section 8, numerical-repair rejection 1 of 5. Registered individually so an adversarial reviewer can cite it by ID against any draft carrying one of those figures.")
add("CG-111", "REJECTED: the claim '23 of 30 hymn datings unverified'.", "L220",
    "Section 8, numerical-repair rejection 2 of 5. Contradicted by CG-108: the chronology CSV holds 17 chronology-claim rows, not 30 hymn datings.")
add("CG-112", "REJECTED: a stage queue saying source repair is COMPLETE.", "L220",
    "Section 8, numerical-repair rejection 3 of 5. Same defect as CG-064 and CG-074, and as IH-167/IH-350 on the Claude side.")
add("CG-113", "REJECTED: marking all empty templates PROPOSED.", "L220",
    "Section 8, numerical-repair rejection 4 of 5. An empty template given a status is structural presence mistaken for research completion (CG-064).")
add("CG-114",
    "REJECTED: converting a secondarily reported 'not clear' into a rejection verdict.",
    "L220",
    "Section 8, numerical-repair rejection 5 of 5. Restated with its subject at L233 (Mayrhofer). Same source-dependency failure as IH-344 and IH-025 (claims made from a secondary summary were wrong).")

# ---------- section 8 : specific rejected reasoning that must not return ----------
# Fourteen items, one row each, so that a draft can be checked against them by ID.
add("CG-115",
    "REJECTED REASONING 1 of 14: Hellwig, Scarlata and Widmer's 2021 allomorphy result is not a universal falsification of Rigvedic relative chronology.",
    "L224",
    "Section 8, rejected-reasoning list. A named 2021 paper used beyond what it establishes. The paper is listed at L274 as a source still requiring access ('Hellwig-Scarlata-Widmer's actual tested features'), so the project has never read the thing it over-generalised - the failure mode of IH-344 and IH-025. Not in IH-001 to IH-369.")
add("CG-116",
    "REJECTED REASONING 2 of 14: family-book location is an attestation fact and a later-or-redacted classification is a separate scholar and method claim; the former must not be erased using the latter.",
    "L225",
    "Section 8, rejected-reasoning list. Convergent with the Claude handoff's standing rule 4, IH-339: attestation is not derivation is not meaning, give all three. Both handoffs independently forbid collapsing an attestation into an interpretation of it.")
add("CG-117",
    "REJECTED REASONING 3 of 14: Mandalas 1, 8, 9 and 10 are not one uniformly demonstrably late layer, and mandala number is not a time axis.",
    "L226",
    "Section 8, rejected-reasoning list. DIRECTLY RELEVANT to an existing rejection on the Claude side: IH-016 and IH-148 (R-02) record a claim built on Afghan river occurrences 'in Books 5, 8 or 10, the late books', and IH-336 records the resulting standing rule that metrical stratum and book order are two instruments and neither may carry a directional claim alone. This row is the same rule stated from the other direction, and it means the phrase 'the late books' in IH-016 is itself the disallowed move. Flagged for 04-AUDITS/REAUDIT-QUEUE.csv rather than resolved here.")
add("CG-118",
    "REJECTED REASONING 4 of 14: a scholar calling an etymology certain is not a project-completed comparative demonstration.",
    "L227",
    "Section 8, rejected-reasoning list. Convergent with IH-344 (every scholar cited through another scholar or a slide is HELD until read) and IH-345 (verify venue, peer review, reception, co-authors and funding before vouching either way).")
add("CG-119",
    "REJECTED REASONING 5 of 14: pan-Dravidian distribution alone does not establish loan direction, a Bronze Age date or a northwest location.",
    "L228",
    "Section 8, rejected-reasoning list. Three separate inferences forbidden from one distributional fact. Bears on this repository's 03-REGISTERS/domain-e-claims.csv and domain-e-retroflex-residue.csv work and on IH-118 (Dravidian is the strongest single contender for the Indus language but is not proven).")
add("CG-120",
    "REJECTED REASONING 6 of 14: Para-Munda is outside the active explanatory framework for insufficient positive diagnostic evidence, not because modern Munda genetics proves every extinct northwest Austroasiatic-related language impossible.",
    "L229",
    "Section 8, rejected-reasoning list. Reproduces almost exactly 00-CONTROLLER/METHODOLOGY-CONSTITUTION.md L240 ('does not genetically disprove every extinct prefixing language'). On the Claude side the same discipline is IH-033, IH-036 and IH-343, which allow Para-Munda 'a brief historical note with its evidential burden stated' rather than placing it outside the framework. The two handoffs differ in where they put it: outside the active framework here, inside as a noted minority there. Both registered; not resolved.")
add("CG-121",
    "REJECTED REASONING 7 of 14: Elamo-Dravidian and Para-Munda are not evidentially symmetrical hypotheses, and each requires its own tests.",
    "L230",
    "Section 8, rejected-reasoning list. Compare IH-033, where the Claude handoff's recorded failure was treating an attested family and an unattested hypothetical donor as equally standing, and IH-122/IH-146 on the Elamo-Dravidian case resting on McAlpin 1974 and Pathak 2024. Same asymmetry principle, different pairing.")
add("CG-122",
    "REJECTED REASONING 8 of 14: Language X is unresolved etymological residue, not proof of one ancient donor language and not proof of Old Indo-Aryan vocabulary, without item-level attestation.",
    "L231",
    "Section 8, rejected-reasoning list. Convergent with IH-160 (transplanting Masica's 'Language X' out of the northwest is REJECTED) and IH-036. Masica's actual table, list and denominator are named at L274 as still needing access, so the residue's own size is unverified in both handoffs.")
add("CG-123",
    "REJECTED REASONING 9 of 14: Dravidian contact with Old Indo-Aryan, individual Rigvedic loans, and Dravidian in the Indus zone are three claims and not one confidence level.",
    "L232",
    "Section 8, rejected-reasoning list. The bridge-testing rule of CLAUDE.md method step 10 applied to the project's central thesis. Compare IH-118 and IH-136 (the Indus language was Dravidian, registered as hypothesis), which this row says must not borrow confidence from attested contact.")
add("CG-124",
    "REJECTED REASONING 10 of 14: Mayrhofer's secondarily reported 'not clear' does not establish an Iranian derivation and is not a verdict against Dravidian.",
    "L233",
    "Section 8, rejected-reasoning list. Directly meets IH-233, where Mayrhofer's EWAia is recorded as load-bearing for the etymological markings and reached through a footer only, never read. Two handoffs independently identify the same unread source carrying weight; this one records a specific inference drawn from a second-hand report of it.")
add("CG-125",
    "REJECTED REASONING 11 of 14: this project's failure to demonstrate a borrowing is not a verdict that the entire scholarly field knows nothing.",
    "L234",
    "Section 8, rejected-reasoning list. The negative-evidence standard turned on the project itself: a NOT PRODUCED absence in this project's own work is not an absence in the field. No counterpart in IH-001 to IH-369.")
add("CG-126",
    "REJECTED REASONING 12 of 14: 'Harappan administrators' assumes the sign users' institutional role; the neutral formulation is sign-makers or sign-users with role unresolved.",
    "L235",
    "Section 8, rejected-reasoning list. A translation-standard failure of the class CLAUDE.md governs: an inherited English category deciding a historical question. Convergent with IH-159 (positive labels for pre-attestation populations rejected in favour of 'of unknown language, either direction') and with the page concept at L326, 'A City Without a King?'.")
add("CG-127",
    "REJECTED REASONING 13 of 14: Oldenberg and Arnold analysed a transmitted ancient record; they did not create that ancient record.",
    "L236",
    "Section 8, rejected-reasoning list. Preservation is not authorship - CLAUDE.md's provenance rule, constitution section 4V - applied to nineteenth and twentieth-century philology. Arnold's hymn tables and Oldenberg's arrangement analysis are named at L274 as sources still requiring access.")
add("CG-128",
    "REJECTED REASONING 14 of 14: 'Dravidian speakers pre-1856 could not record' confuses modern comparative recognition with much older written traditions.",
    "L237",
    "Section 8, rejected-reasoning list. 1856 is the year of Caldwell's comparative grammar; the row says the founding date of a discipline is not the founding date of its subject's literacy. First attestation is not origin - CLAUDE.md provenance rule. Convergent with IH-102 ('Brahmi' is a retroactive label) and IH-359.")

# ---------- section 8 : research-first override and Batch 1 rejection ----------
add("CG-129",
    "A separate sequence redirects work toward a Rigvedic evidence foundation; the exact relative message chronology against P1-P3 cannot be established from file titles alone, but the dependency chain override, Batch 1 return, rejection is clear.",
    "L241", "Section 8, research-first override.")
add("CG-130",
    "The completed-batch claim was REJECTED at checkpoint: nine of ten required research tables were absent as tables or files, pur evidence was representative rather than exhaustive, no exhaustive query ledger existed, and interpretation was promoted into fact; source leads, candidate passages and methodological cautions are retained as preflight only.",
    "L243",
    "Section 8. Handoff label: REJECTED - checkpoint. 'Interpretation was promoted into fact' is the same failure the inheritance rule in CLAUDE.md exists to prevent. This repository has since done independent pur work (03-REGISTERS/rigveda-pur-family.csv, rigveda-pur-family-occurrences.csv, 04-AUDITS/rigveda-pur-family-method.md) with a recorded method; that work is this repository's, not a promotion of this row.")
add("CG-131",
    "Required substantive CSV 1 of 10: RIGVEDA-TRANSMISSION-EVIDENCE.csv.", "L247",
    "Section 8, ten-register completion gate. Registered individually so the gate can be checked item by item. Does not exist in this repository.")
add("CG-132", "Required substantive CSV 2 of 10: RIGVEDA-CHRONOLOGY-METHODS.csv.", "L248",
    "Section 8, ten-register completion gate. Does not exist in this repository. Would be where CG-115 and CG-117 are settled.")
add("CG-133", "Required substantive CSV 3 of 10: PUR-FORT-PASSAGES.csv.", "L249",
    "Section 8, ten-register completion gate. The nearest thing in this repository is 03-REGISTERS/rigveda-pur-family-occurrences.csv, built here with its own method file; whether it satisfies this gate is not asserted.")
add("CG-134", "Required substantive CSV 4 of 10: PATRONAGE-AND-GIFT-PASSAGES.csv.", "L250",
    "Section 8, ten-register completion gate. Does not exist in this repository.")
add("CG-135", "Required substantive CSV 5 of 10: WAR-RAID-CATTLE-PASSAGES.csv.", "L251",
    "Section 8, ten-register completion gate. Does not exist in this repository. Feeds the public sketch 'PAID IN CATTLE' (CG-141).")
add("CG-136", "Required substantive CSV 6 of 10: DANASTUTI-REGISTER.csv.", "L252",
    "Section 8, ten-register completion gate. Does not exist in this repository.")
add("CG-137", "Required substantive CSV 7 of 10: NAMED-PATRONS-POETS-ENEMIES.csv.", "L253",
    "Section 8, ten-register completion gate. Does not exist in this repository. Bears on IH-020 and IH-150, where the named enemies Sambara, Pipru and Cumuri carry a load-bearing argument, and on IH-094 (Pipru and Rjisvan co-occurrence).")
add("CG-138", "Required substantive CSV 8 of 10: GEOGRAPHIC-REFERENCES.csv.", "L254",
    "Section 8, ten-register completion gate. Does not exist in this repository; 03-REGISTERS/domain-e-hydronyms.csv covers part of the ground. Bears on IH-015 to IH-017 and IH-286, the river-count re-run the Claude handoff still owes.")
add("CG-139", "Required substantive CSV 9 of 10: CLAIM-SOURCE-MATRIX.csv.", "L255",
    "Section 8, ten-register completion gate. Does not exist in this repository under that name; 03-REGISTERS plus 02-SOURCES/access-ledger.csv is the equivalent structure.")
add("CG-140", "Required substantive CSV 10 of 10: SOURCE-ACCESS-LEDGER.csv.", "L256",
    "Section 8, ten-register completion gate. This repository's 02-SOURCES/access-ledger.csv is the live equivalent and is the only mechanism CLAUDE.md allows for promoting anything out of INHERITED-UNVERIFIED.")
add("CG-141",
    "Each of the ten registers requires actual rows, verification state and reproducible search logs recording corpus and version, date, lemma and forms, raw hits, deduplication, exclusions and final count.",
    "L258",
    "Section 8. The eight-field search log is more specific than anything in CLAUDE.md's register format and is directly usable. Convergent with IH-286 ('a lemma-verified re-run with a recorded query') and IH-337 (exact lemma forms; data-source gaps stated on the page).")
add("CG-142",
    "Every pur passage must be classified individually and must not be automatically identified as a Harappan city, a cloud, a stone fortress, a temporary palisade or myth; the 90/99/100 formulaicity interpretation remains a hypothesis to test; and 'mainstream', 'unanimous' or a source-discovery list cannot replace the work.",
    "L258",
    "Section 8. Five default readings forbidden, and the numeral formulaicity question left open. Directly relevant to this repository's own pur work and to the public sketch 'THE 99 FORTS'. No counterpart in IH-001 to IH-369; the Claude handoff's nearest item is the unverified '471 chariots vs 2 merchants' headline (IH-285).")
add("CG-143",
    "The public sketches that follow the evidence are THE RGVEDA IS NOT ONE MOMENT, THE 99 FORTS, PAID IN CATTLE, and a child investigation showing why a poem is not a photograph; no completed Batch 2 or exhibit-ready foundation is established.",
    "L260",
    "Section 8. 'The Rgveda Is Not One Moment' and 'The 99 Forts' and 'Paid in Cattle' recur at L329. The child investigation is the only children's-entry item in this handoff tied to a specific evidentiary finding rather than to the ages 8-11 product (CG-087).")

# ---------- section 8 : Who Made the Past? ----------
add("CG-144",
    "Ancient subaltern history and intellectual provenance are core programme, including Greek-Sanskrit and Latin-Sanskrit alongside English-Sanskrit comparisons; the companion synthesis and integration were reported completed, while specialist cases and production features were not.",
    "L264",
    "Section 8. Handoff label: OWNER DECISION - explicitly recorded 5 September in running-list section 20. Corroborated in this repository: 01-INHERITED/site-review/MELAKEELASITEREVIEWRUNNINGLIST.md L803 is exactly '## 20. Ancient subaltern history and intellectual provenance - core programme'. The handoff has cited its source accurately. On the Claude side the Greek-Sanskrit material exists as page work (IH-038, IH-039, two-classical-languages.html) but not as a core programme decision.")
add("CG-145",
    "Eight feature briefs to retain: What Can We Know?; How a Past Survives; The Same Move, Different Power; Lives Without Names; Admired, Then Racialized; Who Made the Past?; Who Gets the Credit?; Many Hands, Unequal Credit.",
    "L266",
    "Section 8. 'Admired, Then Racialized' overlaps IH-170 (period racial vocabulary in the platform's voice is REJECTED; quotation only, marked). 'Who Gets the Credit?' and 'Many Hands, Unequal Credit' are the closest counterpart to the Claude handoff's unbuilt 'Who gets to be speculative' (IH-034, IH-309, IH-330), which is blocked there until a citation history exists.")
add("CG-146",
    "Maker, teacher, translator, editor, codifier, patron, collector and credited authority must be preserved as different roles.",
    "L266",
    "Section 8. The eight-role separation is live in this repository as CLAUDE.md's provenance questions and constitution section 4V ('preservation is not authorship; codification is not invention; first attestation is not origin'). Convergent with CG-127 on Oldenberg and Arnold.")
add("CG-147", "REJECTED: invented historical-resolution percentages.", "L268",
    "Section 8, Who Made the Past rejection 1 of 7. Same class as IH-349 (counts are data-derived, never a stated figure taken on trust).")
add("CG-148",
    "REJECTED: an illustrative 100-to-1 archive funnel presented as data.",
    "L268",
    "Section 8, Who Made the Past rejection 2 of 7. An illustration promoted to evidence. Compare IH-322 (~145 image-only slides and 318 orphaned footnotes outstanding) for the same drift between visual and evidential registers.")
add("CG-149", "REJECTED: civilizational ownership percentages stated without a denominator.", "L268",
    "Section 8, Who Made the Past rejection 3 of 7. 'Without a denominator' is the recurring diagnosis; compare L274 on Masica's actual table, list and denominator, and CG-101 on unreproducible totals.")
add("CG-150", "REJECTED: orality equated with weakness.", "L268",
    "Section 8, Who Made the Past rejection 4 of 7. Convergent with CG-096 on community oral history and with the archive audit CLAUDE.md method step 6 requires: what was unlikely to be recorded is not what did not exist.")
add("CG-151", "REJECTED: Sanskrit preservation equated with invention.", "L268",
    "Section 8, Who Made the Past rejection 5 of 7. Preservation is not authorship - the same rule as CG-127 and CG-146. This is the prestige-bias direction of the pair; CG-152 is the counter-narrative direction.")
add("CG-152", "REJECTED: transmission inferred from similarity.", "L268",
    "Section 8, Who Made the Past rejection 6 of 7. Bears on IH-142 (megalithic graffiti continue Indus signs, Mahadevan) and on the whole diffusionist family the constitution names. CLAUDE.md method step 2: establish chronology first, before interpreting any similarity.")
add("CG-153",
    "REJECTED: living practice automatically described as uninterrupted ancient continuity.",
    "L268",
    "Section 8, Who Made the Past rejection 7 of 7. Convergent with IH-051, where the platform's own headline 'what travelled' was corrected twice on exactly this point ('much of contemporary practice is not Vedic in form'), and with the discontinuity and appropriation tests at L332.")
add("CG-154",
    "OPEN pilot dossiers: a bounded Hortus Malabaricus contributor and entry case and a Florentine Codex passage; an ancient craft and work comparison; Greek-Sanskrit astral-science transmission; and Babylonian-Greek, Greek-Syriac-Arabic, Sanskrit-Persian and Chinese Buddhist transmission with named contributors and exact sources. These are programme requirements, not completed proof of every proposed connection.",
    "L270",
    "Section 8. Handoff label: OPEN. Every one of these is a transmission claim of the class CG-152 forbids inferring from similarity, so each needs its own documentary chain. None appear in IH-001 to IH-369.")

# ---------- section 8 : source dependencies ----------
add("CG-155",
    "Rigvedic source dependencies still requiring access: primary corpora and editions (VedaWeb, GRETIL, TITUS as appropriate), exact Samhita and Padapatha forms, concordances and two scholarly translations where accessible; Arnold's hymn tables; Oldenberg's arrangement analysis; Hellwig-Scarlata-Widmer's actual tested features; Jamison-Brereton, Lubotsky and Rau; DEDR entries and comparative work by Burrow-Emeneau, Krishnamurti, Southworth, Zvelebil, Mayrhofer, Kuiper, Emeneau and Witzel; and Masica's actual table, list and denominator. Access to each must be recorded rather than assumed from bibliography presence.",
    "L274",
    "Section 8. Overlaps the Claude handoff's HELD register substantially: Mayrhofer (IH-233), Kuiper 1991 (IH-232), Witzel (IH-231), Krishnamurti (IH-237), DEDR (IH-247), GRETIL and access friction (IH-249). Both handoffs independently reach the same conclusion - the load-bearing comparative sources have never been read. This repository has begun closing it: 02-SOURCES/vedaweb-manifest-2026-09-07.md and dravlex-glottolog-manifest-2026-09-07.md are logged retrievals. Arnold, Oldenberg, Hellwig-Scarlata-Widmer, Jamison-Brereton, Lubotsky, Rau, Southworth and Zvelebil are named in neither handoff's ledger as read.")
add("CG-156",
    "Separate source dependencies: community-authored Brahui, Kurukh and Malto work; dated Iranian and Balochi linguistic contact evidence; Old Avestan editions and philology; excavation and object reports with analytical material provenance; and rights and consent for living knowledge.",
    "L276",
    "Section 8. The community-authored and consent items are a living-community question, which CLAUDE.md's escalation rules send to the owner rather than to a research decision. Compare IH-081 (the owner's own field observation on the Irula community) and IH-312 (the RMRL bridge). This repository's 05-HOLDS/HOLD-004 already records the North Dravidian comparative evidence as blocked.")
add("CG-157",
    "Blogs, Wikipedia, Dharmapedia, Pragyata/Semenenko, Grokipedia and partisan compilations may generate leads but cannot carry final locators or load-bearing conclusions without independent recovery.",
    "L276",
    "Section 8. Names specific partisan venues, which IH-001 to IH-369 does not; the Claude handoff's equivalent is the venue-and-funding rule IH-345 and the demotion rule IH-346, plus the specific demotions at IH-046 and IH-166. Same standard, applied to a different list of sources.")

# ---------- SECTION 9 : product specification checkpoint ----------
add("CG-158",
    "The P1-P3 audit approved the concept direction and rejected the implementation handoff; no owner ratification of the entire specification is inferred.",
    "L280",
    "Section 9. Handoff label: VERIFIED FINDING - P1-P3 audit disposition, meaning a fact about the audit's stated disposition (CG-018). Section 9's provenance is explicitly not assigned to a single thread. Nothing in IH-001 to IH-369 records a P1-P3 specification.")
add("CG-159",
    "Preserve from P1-P3: evidence, claims and relationships kept separate. Repair before an implementable handoff: first-class claim-evidence, relationship-evidence and page-claim links carrying roles, locators and verification.",
    "L284", "Section 9, preserve/repair table row 1 of 8.")
add("CG-160",
    "Preserve: unknown speech and uncertain geography kept visible. Repair: a universal envelope plus evidence-class subtypes, because Rigvedic verification fields cannot define a bead or a genome.",
    "L285",
    "Section 9, table row 2 of 8. The bead-and-genome objection is CLAUDE.md's evidence-class rule as a schema problem: one class cannot borrow certainty from another, and here it cannot borrow fields either.")
add("CG-161",
    "Preserve: distinct Atlas movement types. Repair: stable place IDs, GeoJSON, origin and destination, route uncertainty, evidence IDs, and signed structured dates that cross BCE/CE.",
    "L286",
    "Section 9, table row 3 of 8. Bears on the atlas count disagreement at CG-186 and IH-250, and on IH-270 (the atlas must be extracted to JSON and every count generated from it) - the Claude handoff's Tier 0 item is this row's precondition.")
add("CG-162",
    "Preserve: revision history and the challenge concept. Repair: correction, challenge, scan and proposal schemas with explicit transitions, permissions, conflict handling, moderation and a storage/API contract.",
    "L287",
    "Section 9, table row 4 of 8. The correction-history requirement is live in this repository as CLAUDE.md's 'never delete a REJECTED row'.")
add("CG-163",
    "Preserve: contested etymologies prevented from becoming facts. Repair: gate the unsupported origin, donor and direction claims rather than the entire WORDS layer.",
    "L288",
    "Section 9, table row 5 of 8. The same bounded-hold logic as CG-106 and non-repetition instruction 7: hold the specific unresolved claim, not the whole programme.")
add("CG-164",
    "Preserve: research discipline intended as build gates. Repair: actual conditional schema, application and build checks, plus invalid examples proving that rejection works.",
    "L289",
    "Section 9, table row 6 of 8. Convergent with IH-271, where the Claude handoff independently asks for a lint.py or equivalent build gate so typed numbers must equal data. Both handoffs conclude that a written rule is not a gate.")
add("CG-165",
    "Preserve: access provenance. Repair: compute governing access from load-bearing links, and keep access separate from quality and independence.",
    "L290",
    "Section 9, table row 7 of 8. The three-dimension separation restates CG-068 and is live as 02-SOURCES/dependency.csv plus the access ledger.")
add("CG-166",
    "Preserve: restricted records recognized. Repair: physically omit restricted content from public exports, because hiding browser JSON is not access control.",
    "L291",
    "Section 9, table row 8 of 8. A security claim as well as an editorial one, and named at L413 as a major risk (restricted material leaked through public exports). No counterpart in IH-001 to IH-369.")
add("CG-167",
    "REJECTED in the P1-P3 specification: mixing all statuses into one field.",
    "L293",
    "Section 9, rejection 1 of 6. Registered with CG-109, which makes the same objection to composite VERIFIED labels. Both bear on this register's own single status column; noted, not acted on.")
add("CG-168",
    "REJECTED: arbitrary string references that accept nonexistent IDs.", "L293",
    "Section 9, rejection 2 of 6. Directly relevant to this register: CLAUDE.md requires source_id to resolve to a row in 02-SOURCES/access-ledger.csv, and every row in this block carries an empty source_id precisely because no retrieval backs it.")
add("CG-169", "REJECTED: manually enterable supposedly computed warnings.", "L293",
    "Section 9, rejection 3 of 6. Same class as IH-167 (a badge is not a record) and CG-074.")
add("CG-170", "REJECTED: English rules arrays advertised as enforced gates.", "L293",
    "Section 9, rejection 4 of 6. Restated at L451 as non-repetition instruction 8 and stated as boundary 2 at L15: prose rules inside schemas do not constitute enforced validation.")
add("CG-171", "REJECTED: a map schema without usable geometry.", "L293",
    "Section 9, rejection 5 of 6. Paired with CG-161.")
add("CG-172",
    "REJECTED: 'a child is never told a word came from a language' as an absolute; securely attested words and genuinely supported borrowing claims may be explained at appropriate depth.",
    "L293",
    "Section 9, rejection 6 of 6. A rejection of over-correction: the caution against unsupported donor-language claims (CG-002, CG-163) had hardened into a blanket ban. Compare IH-347's layered-depth model and L347 here (children may encounter FOUND / WE THINK / MAYBE / WE DON'T KNOW).")
add("CG-173",
    "OPEN: a corrected implementable P1-P3 package and its review outcome; the original handoff to Claude Code must not be repeated as though the audit passed it.",
    "L295",
    "Section 9. Handoff label: OPEN. Restated at L451 as non-repetition instruction 8 and as intake priority 6 at L426. Directly addressed to a Claude Code session, which is what this one is.")

# ---------- SECTION 10 : cross-thread contradictions ----------
add("CG-174",
    "Contradiction: the 58, 96, 105, 108, 133 and 139 totals are different subsets, archive snapshots and page or redirect units; the current branch and deployment must be recomputed separately and no current total is certified.",
    "L301",
    "Section 10, contradiction 1 of 15. CONTRADICTS the Claude handoff's series at IH-251 and IH-185: 58, 69, 85, 102, 127, ~135. Only 58 is common to both, and CG-039 makes 58 a subset error where IH-007 makes it a dated platform size. 96, 105, 108, 133 and 139 appear in neither IH row; 69, 102 and 127 appear in neither CG row. The two handoffs are counting different things over the same period and neither certifies a total. Both registered; not resolved. 139 appears here only, without a source.")
add("CG-175",
    "Contradiction: Atlas totals of 140, 150, 158, 175 and 194 sites and 299 versus 315 windows are dated or inconsistent displays; all totals must be generated from a defined current dataset and query rather than by picking the largest or latest prose figure.",
    "L302",
    "Section 10, contradiction 2 of 15. NEAR-DUPLICATE of IH-250, which records the same disagreement with two additional terms: 167 rising to 175, and 199 site-class rows. The window figures 299 against 315 match exactly. This is the strongest single agreement between the two handoffs, reached from different records, and it corroborates that the atlas count is genuinely unresolved rather than a reporting artifact of either document. The in-repo curatorial audit's own page title for artifact-atlas reads '175 Ancient South Asian Sites Mapped', a third independent sighting of one of the terms.")
add("CG-176",
    "Contradiction: claims that entire topics were missing from the 58 files were withdrawn or downgraded; renamed, merged, redirected, internal and genuinely absent material must be reconciled.",
    "L303",
    "Section 10, contradiction 3 of 15. Restates CG-041. A negative-evidence typing problem: what was called absent was NOT RECOGNIZED or renamed, not NOT PRODUCED.")
add("CG-177",
    "Contradiction: audit-wide HOLD labels versus the owner's public-publication direction; the later running list opposes blanket public audit warnings and automatic downgrading, and a general publication direction can coexist with specific unresolved source-repair claims remaining held.",
    "L304",
    "Section 10, contradiction 4 of 15. Convergent with IH-074, where the owner's direction is that publication does not stop while cross-checking continues, and with CG-106's bounded hold. Both handoffs record the owner resisting a blanket hold.")
add("CG-178",
    "Contradiction: 'the record is the unit of truth' versus fallible records; institutional intent is retained as accountability, but a record can be provisional or wrong and storage does not make a claim true.",
    "L305",
    "Section 10, contradiction 5 of 15. No counterpart in IH-001 to IH-369. The nearest is IH-369, where the Claude handoff rules the platform INCOMPLETE whatever any individual file says - the same refusal to let a document's existence settle its content.")
add("CG-179",
    "Contradiction: MelaKeela under VELI, Veli as threshold, Veli as infrastructure, and a proposed Turai; MelaKeela remains the working public museum name, final institutional, threshold and infrastructure naming is open, and there must be no silent rename.",
    "L306",
    "Section 10, contradiction 6 of 15. FLAGGED DISAGREEMENT with the Claude handoff. IH-062 states flatly 'The name is Veli (Tamil veli), retroflex l, romanised veli' as an adopted owner decision; IH-176, IH-177, IH-257 and IH-258 record the brand architecture as contested and held open under HD-14, and IH-276 makes the naming decision the owner's and blocking. This handoff instead fixes MelaKeela as the working public museum name and adds a fourth candidate, Turai, which appears nowhere in IH-001 to IH-369. Corroborated on this side by 01-INHERITED/site-review/MELAKEELASITEREVIEWRUNNINGLIST.md L556, which records the same brand contradiction and says current owner direction uses Mela Keela as the museum and Veli as its threshold. Both registered. Not resolved here; this is an owner decision and a candidate for DECISIONS-NEEDED.md.")
add("CG-180",
    "Contradiction: the open/daylight master doctrine versus the later near-black field is a genuine visual-direction conflict; chronology must be preserved and a scoped design resolution requested when building, with no bulk application from the handoff.",
    "L307",
    "Section 10, contradiction 7 of 15. FLAGGED DISAGREEMENT, developed at CG-046 and CG-197. The Claude handoff records the dark ground as settled owner direction (IH-065, IH-066), not as one pole of a conflict. Both registered; not resolved.")
add("CG-181",
    "Contradiction: 'narrative locked' versus the owner's later content challenge; the later challenge reopens factual cleanup and no final 16- or 15-slide requirement is certified.",
    "L308", "Section 10, contradiction 8 of 15. Restates CG-082 and CG-084.")
add("CG-182",
    "Contradiction: a 15-page launch versus all current public pages remaining accessible; a curatorial MVP recommendation is not permission to unpublish the rest, and curated entry, migration scope and publication policy are three different things.",
    "L309",
    "Section 10, contradiction 9 of 15. The 15-page MVP is corroborated in this repository at 01-INHERITED/curatorial-audit-v1.1/summary.csv (MVP candidates 15) and page-audit.csv (MVP Yes 15). No counterpart in IH-001 to IH-369; the Claude handoff's equivalent tension is IH-318, the external review's request to reduce the homepage and make /enter a foyer.")
add("CG-183",
    "Contradiction: four, six or nine engines and numerous worlds are capabilities and ambitions rather than production commitments; reuse must be proved with a complete case and then a second case.",
    "L310",
    "Section 10, contradiction 10 of 15. DUPLICATES the Claude handoff's engine disagreement from the other side: IH-010 records six engines (T4), IH-210 records nine (VELI-12), IH-259 and IH-260 record the MVP and ingestion-layer disagreements. 'Four' appears only here. The prove-reuse-twice test is this handoff's addition and matches CG-072's warning against reading ten visitor functions as ten engines.")
add("CG-184",
    "Contradiction: the entire project blocked on substrate repair versus v2.1's bounded hold; unrelated specification and content work may proceed within authorization.",
    "L311", "Section 10, contradiction 11 of 15. Restates CG-106; restated again at L450 as non-repetition instruction 7.")
add("CG-185",
    "Contradiction: COMPLETE or approved appearing in filenames or a stage queue versus actual contents; contents, evidence and review outcome govern, and failed readiness claims are preserved in correction history.",
    "L312",
    "Section 10, contradiction 12 of 15. Restates CG-064, CG-074 and CG-112. Convergent with IH-167 and IH-350 and with CLAUDE.md's rule that a REJECTED row is never deleted.")
add("CG-186",
    "Contradiction: the current site versus screenshots and ZIPs; screenshots and archives are dated evidence and current live state or completion may not be inferred from them.",
    "L313",
    "Section 10, contradiction 13 of 15. Convergent with IH-366, where the Claude handoff records that files it could not see are attested by threads and not verified on disk, and with CG-013. Both handoffs were working from archives.")
add("CG-187",
    "Contradiction: canonical versus counter-narrative bias; specific evidence must be weighted and source dependence disclosed, and one authority bundle must not be replaced with another.",
    "L314",
    "Section 10, contradiction 14 of 15. The two adversarial tests of CLAUDE.md in one line, and live here as 04-AUDITS/BIAS-FAILURE-LOG.csv. Convergent with IH-361 and CG-069.")
add("CG-188",
    "The running list additionally flags Irula-proxy correction residue in prose and SVGs; the rejected proxy premise must not be reinstated through labels, captions or accessible names.",
    "L316",
    "Section 10, targeted audit item 1 of 5. MEETS the Claude handoff directly: IH-030 records the Irula tension (deck p.23 DNA overlap against p.317 Irula as a late branch from Tamil), IH-081 records the owner's field observation that the Irula community did not know Rakhigarhi referenced them, and IH-310 records that Shinde 2019's exact wording on the Irula is still unchecked. This row adds that the correction was made in prose but left residue in SVGs, captions and accessible names - a propagation failure neither handoff has closed. Strong candidate for 04-AUDITS/REAUDIT-QUEUE.csv.")
add("CG-189",
    "The running list flags Rakhigarhi-only framing that ignores the Indus Periphery.",
    "L316",
    "Section 10, targeted audit item 2 of 5. DUPLICATES the Claude handoff's correction C-13 exactly: IH-029 and IH-155 record that Rakhigarhi is not one individual but twelve on a cline including Gonur and Shahr-i-Sokhta outliers, and IH-110 and IH-273 record the removal of 'one individual' from the steppe and endogamy-clock pages as owed live confirmation. Two independent records of the same defect, which raises confidence that the defect is real without promoting either row.")
add("CG-190",
    "The running list flags Y-chromosome versus autosomal conflation.",
    "L316",
    "Section 10, targeted audit item 3 of 5. Bears on IH-127, where village-specific Y-chromosome lineages at 79 per cent against diverse mtDNA carry a patrilocality argument, and on IH-119 (male-biased Munda incoming). A bridge-testing failure of the class CLAUDE.md method step 10 governs. Not previously registered as an audit item.")
add("CG-191",
    "The running list flags Iranian-related ancestry conflated with later sampled Iranian farmers.",
    "L316",
    "Section 10, targeted audit item 4 of 5. DUPLICATES IH-109 word for word in substance: 'Iranian-related does not mean from Iran'. Two independent records of the same correction.")
add("CG-192",
    "The running list flags infrastructure-injected analytics as distinct from package-originated requests.",
    "L316",
    "Section 10, targeted audit item 5 of 5. A deployment and privacy finding with no counterpart in IH-001 to IH-369. Relevant to any claim about what the live site sends, and to the CSP work at CG-036.")

# ---------- SECTION 11 : page / exhibit recovery catalogue ----------
add("CG-193",
    "The page and exhibit concepts in the recovery catalogue are recorded programme work only; existence, completeness and approval all require current-route reconciliation.",
    "L320", "Section 11, the gate on the whole catalogue.")
add("CG-194",
    "Evidence experience collection: Atlas v2, PROVE IT, WITNESS, TIME + PLACE, Field Bag, source viewer and evidence search, requiring typed claims and links, implementable schemas, real records, correction propagation and rights.",
    "L324",
    "Section 11, collection 1 of 10. WITNESS and Field Bag match IH-212 (the Witness engine on 'Could they read?' and the Dig engine's on-device Field Bag). Correction propagation is the unresolved problem CG-188 instances.")
add("CG-195",
    "Living Worlds collection: Water, Food and Word/Language first, then City, Body, Mind, Movement, Nature, Work, Power, Play and Belief where warranted; later worlds are kept mapped and not commissioned automatically.",
    "L325",
    "Section 11, collection 2 of 10. DIVERGES from IH-211, where the Claude handoff records the Living Doors as twelve - Water, Food, Mind, Body, Home, Movement, Nature, Work, Belief, Language, Power, Play - adopted from a ChatGPT comparison as 'the single strongest idea in either document'. This list has City and lacks Home; it also names Word/Language as one world and gives Water, Food and Word priority ordering that IH-211 does not carry. Both lists registered; the membership difference is unresolved. Corroborated in part at 01-INHERITED/site-review/MELAKEELASITEREVIEWRUNNINGLIST.md L811, which lists Food, Water, Body, Mind, Work, Language, Power, Movement, Nature and 'the other Living Worlds' - agreeing with neither list exactly.")
add("CG-196",
    "Indus and literacy collection: A City Without a King?; Could They Read?; The Script They Didn't Read - requiring governance-inference and absence discipline, inscription context, dating and archaeological sources.",
    "L326",
    "Section 11, collection 3 of 10. 'A City Without a King?' is the exhibit form of CG-126's rejection of 'Harappan administrators'. 'Could They Read?' matches IH-212's Witness engine subject exactly. 'The Script They Didn't Read' bears on IH-037's Farmer-Sproat-Witzel 2004 and Rao et al. 2009, both named and not accessed.")
add("CG-197",
    "Language and naming collection: Who Named India?; Who Mapped Speech?; The Language That Moved; Proto-Dravidian Without a Sanskrit Sibilant Series; The Sounds a Script Learned to Write - requiring dated attestations, comparative phonology, script history, and sound distinguished from spelling.",
    "L327",
    "Section 11, collection 4 of 10. 'Who Named India?' is a built page on the Claude side (IH-197, who-named-india). 'Who Mapped Speech?' is corroborated at 01-INHERITED/site-review/MELAKEELASITEREVIEWRUNNINGLIST.md L894 and L904 as its own running-list section. 'Proto-Dravidian Without a Sanskrit Sibilant Series' is the exhibit form of CG-097 and CG-098; 'The Sounds a Script Learned to Write' is the exhibit form of IH-103.")
add("CG-198",
    "Refugia and movement collection: Brahui: Four Histories, Not One; Continuity Versus Migration; The Languages Left on the Hills; Genes Do Not Speak; Balochistan 3000 BCE-1500 CE - requiring community sources, independently dated contact, unknown polygons and falsifiers, with no ethnic map drawn from DNA.",
    "L328",
    "Section 11, collection 5 of 10. The exhibit form of CG-091 to CG-096. 'Unknown polygons' is a mapping requirement CLAUDE.md method step 3 implies (unknown zones) and that the P1-P3 geometry repair at CG-161 would carry. Directly serves this repository's domain-M work.")
add("CG-199",
    "Vedic and Avestan collection: The Rgveda Is Not One Moment; The Same World, Two Responses; Before and After Zarathustra; Paid in Cattle; The 99 Forts - requiring the ten corpus registers, transmission and chronology kept separate, and genre controls.",
    "L329",
    "Section 11, collection 6 of 10. Gated on CG-131 to CG-140. 'Before and After Zarathustra' is the exhibit form of the owner's scope at CG-091 and bears on IH-130 (xwedodah praised in Zoroastrian Iran). 'The Same World, Two Responses' is where CG-100's rejected peaceful-Iranian versus violent-Indian binary would have to be avoided.")
add("CG-200",
    "Material biographies collection: Blue Road; Red Road; Who Tells the Stone's Story?; When a Network Fragments - requiring geological attribution distinguished from analytical attribution, workshop, exporter, findspot and custody, and independent catalogue sources.",
    "L330",
    "Section 11, collection 7 of 10. The four-way provenance chain is CLAUDE.md's provenance questions applied to objects. No counterpart in IH-001 to IH-369.")
add("CG-201",
    "Corridor power collection: Before Oil: The Strait; When Does a Route Become a Chokepoint?; Before States, Before Imperial War - requiring trade, tribute, taxation, raid, naval control and conquest to be separated, and the ancient layer kept independent of an expiring modern essay.",
    "L331",
    "Section 11, collection 8 of 10. Corroborated as a running-list programme at 01-INHERITED/site-review/MELAKEELASITEREVIEWRUNNINGLIST.md L1182 (section 24, which names the Strait). 'Independent of an expiring modern essay' is a maintenance claim: a page anchored to current geopolitics dates faster than its evidence.")
add("CG-202",
    "Everyday intellectual life collection: Five Landscapes of Love; How Old Is Meditation?; The Hands That Shape Our World - requiring Tamil passages and poetics, dated practice and terminology, craft labour, and discontinuity and appropriation tests.",
    "L332",
    "Section 11, collection 9 of 10. 'Five Landscapes of Love' is the tinai material the Claude handoff records as a built page (IH-197, tinai) and as an owed Tamil-dictionary confirmation (IH-314). The discontinuity and appropriation tests are the operational form of CG-153.")
add("CG-203",
    "Intellectual provenance collection: the eight Who Made the Past? features, requiring documentary case dossiers and role/credit graphs, with no invented voices or ownership shares.",
    "L333", "Section 11, collection 10 of 10. Gated on CG-145, CG-146, CG-149 and CG-154.")
add("CG-204",
    "REJECTED ROUTE SHORTCUT 1 of 6: Mehrgarh's modern name is not evidence of identity with Marhasi.",
    "L335",
    "Section 11. A toponym-resemblance inference, the same class as IH-299's unrun Pataliputra-to-Patna toponym search and as CG-152 (transmission inferred from similarity).")
add("CG-205",
    "REJECTED ROUTE SHORTCUT 2 of 6: Meluhha, Marhasi, Magan and Dilmun must remain distinct until linked.",
    "L335",
    "Section 11. Bears on IH-131 (Desset's 2022 Linear Elamite reading contains no Meluhha and no Indus reference) and on the project's former name, 'Meluhha to Keezhadi' (IH-174), which welded one of these terms into an identity claim.")
add("CG-206",
    "REJECTED ROUTE SHORTCUT 3 of 6: not every blue object is Badakhshan lapis.",
    "L335",
    "Section 11. The geological-versus-analytical attribution distinction of CG-200 stated as a specific error. Gates the 'Blue Road' exhibit.")
add("CG-207",
    "REJECTED ROUTE SHORTCUT 4 of 6: the earliest recovered object is not necessarily the first contact.",
    "L335",
    "Section 11. First attestation is not origin - CLAUDE.md's provenance rule - in its archaeological form, and a negative-evidence claim requiring excavation-coverage typing before it can be read either way. Convergent with IH-027 ('earliest attested as', never 'originates in').")
add("CG-208",
    "REJECTED ROUTE SHORTCUT 5 of 6: ships moored at Agade are not automatically seized ships.",
    "L335",
    "Section 11. A translation and inherited-category failure: the English framing decides whether a text records trade or plunder. Same class as CG-126.")
add("CG-209",
    "REJECTED ROUTE SHORTCUT 6 of 6: trade does not invariably precede war in a universal sequence.",
    "L335",
    "Section 11. Gates the 'Before States, Before Imperial War' exhibit at CG-201 and is the sequencing counterpart of CG-100's rejected universal binaries.")

# ---------- SECTION 12 : visual and public-copy inheritance ----------
add("CG-210",
    "Preserve: a visual idea must communicate evidence, uncertainty, context or change, and motion needs an explanatory task.",
    "L341",
    "Section 12. Convergent with IH-214's deck constitution, where evidentiary weight sets visual scale and line treatment carries status. Both handoffs make decoration a failure state.")
add("CG-211",
    "Preserve: objects, excavation images, inscriptions, manuscripts, real maps and material traces should have greater presence than generic vector diagrams.",
    "L342",
    "Section 12. The positive form of the deck rejection at CG-081. Blocked in practice by the rights dependency at CG-090 and IH-193.")
add("CG-212",
    "Preserve: field relationships are earned, and absence and contradiction remain visible.",
    "L343", "Section 12. Restates the design grammar of CG-059.")
add("CG-213",
    "Preserve: different exhibits may need different environments, and extraction and custody treatment is content-specific rather than universal museum chic.",
    "L344",
    "Section 12. This is the row that makes CG-180's palette conflict resolvable in principle - if environments are per-exhibit, daylight and near-black need not be exclusive. Registered as the handoff's own position, not as a resolution.")
add("CG-214",
    "Preserve: exact wordmark spelling and the selected owner geometry matter.",
    "L345", "Section 12. Restates CG-052 and CG-054; spelling is load-bearing in both handoffs (IH-062).")
add("CG-215",
    "Preserve: public copy should be concise, lucid, curious, confident in proportion to evidence, and anti-caste and anti-colonial without ethnic triumphalism.",
    "L346",
    "Section 12. 'Confident in proportion to evidence' is CLAUDE.md's proportional-space rule as a voice instruction; 'without ethnic triumphalism' is the counter-narrative adversarial test. Convergent with IH-068 (no hedging findings the evidence supports) and IH-340.")
add("CG-216",
    "Preserve: layered depth uses the same underlying evidence, children may encounter FOUND / WE THINK / MAYBE / WE DON'T KNOW, and uncertainty is not a failure.",
    "L347",
    "Section 12. A four-level child-facing status vocabulary, mapping onto the adult statuses without a separate evidence base. No counterpart in IH-001 to IH-369; the Claude handoff's children's work (IH-210, IH-212) describes engines and age bands, not a status vocabulary. Qualified by CG-172.")
add("CG-217",
    "Preserve: contextual PROVE IT and source access should not force an academic preamble onto every first screen.",
    "L348",
    "Section 12. Convergent with CG-045 (no repeated public audit labels) and with IH-018 and IH-354 (no meta-commentary on a published page). Restated at L452 as non-repetition instruction 9.")
add("CG-218",
    "The older Veli doctrine specifies pearly daylight, open horizons, water, ecology, warm off-white, dawn blue, clay, sage, ink and restrained gold; it explicitly says not to apply the old near-black system uniformly, and it calls for three prototypes - threshold, subject/object in its tinai, and extraction/contested collection.",
    "L352",
    "Section 12, side 1 of the palette conflict. CONTRADICTS IH-065 and IH-066, where the Claude handoff records dark ground and the owner's 'I like the darkness' as settled. The three-prototype gate has no counterpart in IH-001 to IH-369. Both registered.")
add("CG-219",
    "The later 04-MELAKEELA-PUBLIC-COPY-AND-VISUAL-PAGE-STANDARD.md specifies a near-black field, light type, selective gold, rust, orange, sage, slate-blue and olive accents, and no generic SaaS cards or decorative gradients; the deck text gives darkness an epistemic role as the unknown field around evidence.",
    "L354",
    "Section 12, side 2 of the palette conflict. AGREES with IH-065 (dark ground) and IH-214 (dark field) and supplies the epistemic justification neither Claude row records. The banned-motif discipline parallels IH-199's list, which the Claude handoff marks NOT adopted.")
add("CG-220",
    "OPEN: the final palette and environment hierarchy, and whether daylight and night are complementary modes or one supersedes the other; the owner rejected poor execution, not necessarily every underlying visual principle, and that rejection must not be used to erase all prior assets.",
    "L356",
    "Section 12. Handoff label: OPEN. The scoped design resolution CG-180 asks for, and intake priority 9 at L429. Candidate for DECISIONS-NEEDED.md as an owner decision; not raised there by this pass.")
add("CG-221",
    "REJECTED visual approaches: dashboard-like institutional decks; card soup; text-on-text museum pages; generic AI archaeology presented as evidence; invented ancient imagery; decorative continuity lines; and internal workflow language used as visitor content.",
    "L358",
    "Section 12. Seven rejected approaches, developed from CG-081. 'Invented ancient imagery' meets IH-214's VISUAL HYPOTHESIS labelling requirement and IH-199's banned motif list. 'Decorative continuity lines' is the visual form of CG-153: a drawn line asserting continuity the evidence does not carry. 'Internal workflow language as visitor content' restates IH-018 and IH-354.")

# ---------- SECTION 13 : artifact register ----------
add("CG-222",
    "The fifteen filenames D01 to D15 were retrieved as local source records and are sources for the handoff, not all necessarily owner-ratified controllers.",
    "L364",
    "Section 13. The D01-D15 identifiers are this handoff's local artifact labels. They are NOT this repository's D- owner-decision namespace (09-DECISIONS/OWNER-DECISIONS.csv) and must never be resolved through 09-DECISIONS/DECISION-ID-MAP.csv. Collision noted so that a later reader does not read D05 here as an owner decision.")
add("CG-223",
    "D01 MELA-KEELA-SITE-REVIEW-RUNNING-LIST.md is the main dated review and owner-direction record, covering sections 15-24, inventory corrections and research expansion.",
    "L368",
    "Section 13. IN THIS REPOSITORY as 01-INHERITED/site-review/MELAKEELASITEREVIEWRUNNINGLIST.md (Version 12) and ...LIST2.md (Version 10); see RUNNING-LIST-RECONCILIATION.md. The handoff's 'sections 15-24' matches Version 12 exactly, which has numbered sections 1-24 where Version 10 stops at 22 - so the handoff read Version 12, the current one. Its section-level citations check out at L45, L47, L393, L404, L556, L558, L642, L803, L811, L894 and L1182.")
add("CG-224",
    "D02 PHASE-1-PROPOSAL.md is the 1 September proposal recording the archive mismatch and the reported CSP reproduction.",
    "L369", "Section 13. Not in this repository. Source for CG-035 and CG-036.")
add("CG-225",
    "D03 mela-keela-curatorial-and-museum-plan.md carries the 96-page curatorial baseline and the proposed release architecture.",
    "L370",
    "Section 13. Not in this repository as a Markdown file, but its numbers are: 01-INHERITED/curatorial-audit-v1.1/ holds the same 96-page baseline against veli-site(3).zip dated 2026-09-01, and reproduces every figure in CG-034.")
add("CG-226",
    "D04 MELA-KEELA-VELI-DESIGN-DOCTRINE.md carries the open-field and extraction doctrine and the prototype gate.",
    "L371", "Section 13. Not in this repository. Source for CG-218, side 1 of the palette conflict.")
add("CG-227",
    "D05 00-START-HERE-CLAUDE-UPDATE-v3.md carries the consolidated controller read order and coverage reconciliation.",
    "L372",
    "Section 13. Not in this repository. Source for CG-063 (DECK-SITE-COVERAGE.csv and backlog items 1-89).")
add("CG-228",
    "D06 01-MELAKEELA-UNIVERSAL-RESEARCH-CONSTITUTION.md carries evidence weighting and the universal research method.",
    "L373",
    "Section 13. This is the ancestor of 00-CONTROLLER/METHODOLOGY-CONSTITUTION.md, committed to this repository unchanged as the owner wrote it, and of 00-CONTROLLER/RESEARCH-CONSTITUTION.md. Source for CG-062 and CG-065 to CG-071.")
add("CG-229",
    "D07 02-MELAKEELA-SOURCE-INDEPENDENCE-AND-RESEARCH-INHERITANCE.md carries the inherited research questions and the source-dependency repair.",
    "L374",
    "Section 13. The ancestor of this repository's inheritance rule and of 02-SOURCES/dependency.csv. Its title names the two disciplines - source independence and research inheritance - that CLAUDE.md makes standing constraints.")
add("CG-230",
    "D08 03-MELAKEELA-DECK-TO-SITE-CONTENT-RECOVERY.md carries the signature experiences, the investigation catalogue and coverage dispositions.",
    "L375", "Section 13. Not in this repository. Source for sections 6 and 11.")
add("CG-231",
    "D09 04-MELAKEELA-PUBLIC-COPY-AND-VISUAL-PAGE-STANDARD.md carries the public-copy deliverables and the later dark-field direction.",
    "L376", "Section 13. Not in this repository. Source for CG-219, side 2 of the palette conflict, and for CG-073's twelve-part packet.")
add("CG-232",
    "D10 MELAKEELA-AMENDED-CHECKPOINT-v3-AUDIT.md is the first major source-repair rejection and records the retained structural work.",
    "L377", "Section 13. Not in this repository. Source for CG-063 and CG-102.")
add("CG-233",
    "D11 MELAKEELA-SOURCE-REPAIR-v2-CHECKPOINT-AUDIT.md carries the attestation and chronology corrections, the false attribution and the locator corrections.",
    "L378", "Section 13. Not in this repository. Source for CG-103, including the danda RV 7.33.6 locator and the Talageri over-extension.")
add("CG-234",
    "D12 MELAKEELA-SOURCE-REPAIR-v2.1-OWNER-REVIEW.md carries the bounded hold, the numerical repair and the scope of permitted continuation.",
    "L379",
    "Section 13. Not in this repository, and the most consequential missing file: it is the sole source for CG-002, CG-105, CG-106, CG-107 and CG-108, including the 0/23 completion figures and the canonical replacement wording.")
add("CG-235",
    "D13 MELAKEELA-P1-P3-SPECIFICATION-AUDIT.md carries the implementation rejection and the schema and product corrections.",
    "L380", "Section 13. Not in this repository. Sole source for section 9.")
add("CG-236",
    "D14 MELAKEELA-RESEARCH-FIRST-OVERRIDE.md carries the corpus-first foundation scope.",
    "L381", "Section 13. Not in this repository. Source for CG-129.")
add("CG-237",
    "D15 MELAKEELA-RESEARCH-BATCH-1-CHECKPOINT-REJECTION.md carries the incomplete preflight disposition and the ten-register completion gate.",
    "L382", "Section 13. Not in this repository. Source for CG-130 and CG-131 to CG-142.")
add("CG-238",
    "Additional downloaded context: MELAKEELA-CLAUDE-CORRECTIVE-CONTROLLER-v2.md; MELA-KEELA-CLAUDE-FULL-SEQUENCE.md; MELA-KEELA-LANGUAGE-RESEARCH-PROMPTS.md; MELA-KEELA-CLAUDE-LIVE-SITE-AUDIT-PROMPT.md; MELA-KEELA-CLAUDE-SAY-NEXT-RESEARCH-PROMPT.md; MELA-KEELA-WHO-MADE-THE-PAST.md; and mela-keela-curatorial-and-museum-plan(1).md. Their programme role is corroborated through the inspected control and review records; full-line review is not claimed.",
    "L384",
    "Section 13. Five of these seven are prompts addressed to Claude, so the ChatGPT side held the instructions the Claude side was working under - which is why the two handoffs converge on method (CG-069, CG-071, CG-164) while disagreeing on inventory (CG-174) and naming (CG-179).")
add("CG-239",
    "Located by metadata with contents not inspected: site snapshots veli-site.zip through veli-site(4).zip, veli-site-2.zip, melakeela-production-3a3afa8.zip and melakeela-26-new-screenshots.zip.",
    "L388",
    "Section 13. veli-site(3).zip is the frozen baseline of the curatorial audit committed here. melakeela-production-3a3afa8.zip carries a commit hash, which is the only production-revision identifier in either handoff.")
add("CG-240",
    "Located by metadata: curatorial and design artifacts mela-keela-curatorial-audit-v1.xlsx and its (1) copy, mela-keela-curatorial-package-v1.zip, mela-keela-design-kit-v3-final.zip, mela-keela-design-kit-v3-partial.zip, mela-keela-claude-kit-v2.zip, mela-keela-claude-handoff-v1-review.zip and mela-keela-brand-kit.zip.",
    "L389",
    "Section 13. 'v3-final' next to 'v3-partial' is exactly the filename-approval trap CG-021 and CG-185 forbid reading as a status. This repository holds a later revision, melakeela-curatorial-audit-v1.1.xlsx.")
add("CG-241",
    "Located by metadata: research artifacts melakeela-research-handoff-final.zip, MELAKEELA-CLAUDE-AUTONOMOUS-RESEARCH-RUN-v1.zip, melakeela-research-batch-1.zip, MELAKEELA-RESEARCH-BATCH-1-CHECKPOINT-REJECTION.zip, melakeela-amended-checkpoint.zip, melakeela-source-repair-v2-1.zip, MELAKEELA-CHECKPOINT-AUDIT-FOR-CLAUDE.zip and melakeela-p1-p3-specification.zip.",
    "L390",
    "Section 13. melakeela-source-repair-v2-1.zip is the underlying ZIP CG-108 says the review's counts were not re-run against; recovering it is the precondition for settling CG-101 to CG-108.")
add("CG-242",
    "Located by metadata: controller packs MELA-KEELA-CLAUDE-PROMPT-PACK.zip, MELAKEELA-CLAUDE-CONSOLIDATED-PROMPT-PACK-v3.zip and MELAKEELA-CLAUDE-UPDATE-v3.zip.",
    "L391", "Section 13.")
add("CG-243",
    "Located by metadata: deck and architecture artifacts including multiple institutional vision PPTX versions, MelaKeela-Veli-Institutional-Vision-Deck-16.pptx and its montage, a three-slide prototype, MELAKEELA-VELI-DECK-v0.1.pdf, melakeela_montage.png, Veli-Institutional-Art-Direction-Board.pptx and its (1), MELA-KEELA-CANONICAL-ARCHITECTURE-PROPOSED.pdf and MELA-KEELA-WHO-MADE-THE-PAST.pdf.",
    "L392",
    "Section 13. MELAKEELA-VELI-DECK-v0.1 and the 16-slide deck are the artifacts IH-210 records being built with pptxgenjs and sharp - the same files seen from both sides. 'CANONICAL-ARCHITECTURE-PROPOSED' carries its own status in its filename, correctly.")
add("CG-244",
    "Located by metadata: roughly twenty logo and visual exploration PNGs, including VELI Compass Field Logo.png, several ambigram exploration boards, river/sunrise/horizon marks and brand identity moodboards.",
    "L393",
    "Section 13. No pixels inspected (CG-009), so none of these identifies the mark selected at CG-052. Intake priority 9 at L429 turns on recovering the selected image together with the owner's response.")
add("CG-245",
    "Mentioned but not recovered: full ChatGPT transcripts, full Claude transcripts, claude-project-handoff.md, current GitHub README and setup instructions, the final selected SVG, and the complete original thirty-part vision and sixteen-section source proposal as original inputs. Generated artifact existence does not prove delivery acceptance, historical validity or current deployment.",
    "L395",
    "Section 13. claude-project-handoff.md is IN THIS REPOSITORY at 01-INHERITED/claude-project-handoff.md and is registered as IH-001 to IH-369, so one named gap is now closed - which is what makes this cross-reference pass possible. The thirty-part vision and sixteen-section source proposal appear in neither handoff's inventory and are new recovery dependencies.")

# ---------- SECTION 14 : operating case, risks, strategic options ----------
add("CG-246",
    "The handoff is an operating handoff and not a new valuation or funding opinion; no accounts, current available cash, liabilities, signed commitments or costed staffing plan were inspected.",
    "L399", "Section 14. The financial counterpart of CG-012 and CG-013.")
add("CG-247",
    "Proposed agency build budgets, timelines, world counts and first-year capacity ranges are scenarios rather than forecasts; the running list explicitly separates founder labour from cash, award headlines from spendable runway, and eligibility from possible funding routes.",
    "L401",
    "Section 14. Handoff label: PROVISIONAL FINDING. The three separations are sharper than anything in IH-001 to IH-369, whose funding rows (IH-208, IH-313) record a taxonomy with VERIFY flags rather than a cash discipline. Convergent in spirit with IH-061's ban on any number not derivable from the repository.")
add("CG-248",
    "DMC and CMF were discussed in a 4 September record covering eligibility, applicant structure, deadlines, phased payments and rights dependencies; those are dated research notes, the original programme rules must be retrieved and reverified before use in an application, and no current deadline or eligibility conclusion is certified.",
    "L403",
    "Section 14. Handoff label: OPEN funding dependencies. DIVERGES from the Claude handoff by omission rather than contradiction: IH-059 records a specific DMC correction - the one-year legal-existence requirement making a September 2026 incorporation ineligible for December 2026, with the plan revised to December 2027 - and IH-133, IH-184, IH-262, IH-313 and IH-328 carry it forward. This handoff certifies no eligibility conclusion at all. The safer reading is this one, since IH-246 records that the DMC 2027 guidelines were never accessed and the 2026 guidelines were reached via web only. Both registered.")
add("CG-249",
    "Scenario 'no award': bound paid commitments to unrestricted cash, and improve the existing museum and a small evidence and experience case.",
    "L407", "Section 14, scenario 1 of 3.")
add("CG-250",
    "Scenario 'award delayed': model payment timing and peak cash shortfall, and rephase contracts or identify an explicit bridge.",
    "L408", "Section 14, scenario 2 of 3.")
add("CG-251",
    "Scenario 'funded pilot succeeds': add a second case and measure reuse, authoring effort and learning or usability observations before expanding.",
    "L409",
    "Section 14, scenario 3 of 3. The prove-reuse-with-a-second-case test of CG-183, stated as a funding gate.")
add("CG-252",
    "Buy commodity infrastructure and administration where suitable, with no acquisition case established; fix the current museum's inventory, contradictions, source access and visitor experience; build bounded evidence-to-investigation capabilities after a corrected specification; and walk away from or defer arrangements compromising editorial independence, ownership or unfunded cash capacity, along with premature multi-engine staffing and licensing forecasts.",
    "L411",
    "Section 14. 'Editorial independence' as a walk-away condition is the strongest institutional statement in either handoff and bears on the partner and governance cautions at CG-086 and IH-061.")
add("CG-253",
    "Major risks: source dependence disguised as corroboration; incomplete corpus work presented as proof; stale inventories; design directions merged without decision; restricted material leaked through public exports; partner and governance aspirations presented as facts; rights gaps; correction residue across visuals and metadata; and founder time consumed by repeated narrative rewrites. These attach to concrete records rather than being hypothetical reasons to pause all work.",
    "L413",
    "Section 14. Nine risks, each instanced elsewhere in this register: source dependence (CG-124, CG-155, IH-344), incomplete corpus as proof (CG-105, CG-130), stale inventories (CG-174), directions merged without decision (CG-180), restricted exports (CG-166), aspirations as facts (CG-086), rights gaps (CG-090), correction residue (CG-188), narrative rewrites (CG-001). The first is CLAUDE.md's source-independence constraint and this repository's 02-SOURCES/dependency.csv.")

# ---------- SECTION 15 : Research Headquarters intake and completion queue ----------
add("CG-254",
    "The intake sequence is a proposed implementation-neutral queue derived from the unresolved work; it does not create a repository or override later owner authorization.",
    "L417", "Section 15, the gate on the queue.")
add("CG-255",
    "Intake priority 1: import the five substantive ChatGPT thread exports and the Claude handoff and latest ZIP, with completion evidence being thread IDs, dates, original messages and attachments indexed, and exact missing intervals stated.",
    "L421",
    "Section 15. PARTLY DONE by this repository: 01-INHERITED/claude-project-handoff.md and 01-INHERITED/chatgpt-project-handoff.md are both committed and registered. Neither thread exports nor the research ZIP are here, and no thread IDs exist for the ChatGPT side at all (CG-007), so the completion evidence this row requires cannot yet be produced.")
add("CG-256",
    "Intake priority 2: reconcile the approval and decision history so that each decision links to an owner message or explicitly remains a model or document recommendation.",
    "L422",
    "Section 15. The discipline CG-021 states and that IH-082 applies on the Claude side. In this repository the mechanism is 09-DECISIONS/OWNER-DECISIONS.csv, which no inherited decision may enter without a fresh owner re-affirmation.")
add("CG-257",
    "Intake priority 3: verify the GitHub, Claude Code and Codex setup state with actual repository URLs, branch and commit, README and session roles, assuming nothing from renamed labels.",
    "L423", "Section 15. Partly closed by this repository's existence; the ZoaltOPS and site renames at CG-031 remain owner-reported.")
add("CG-258",
    "Intake priority 4: preserve the source-repair and Batch 1 holds with correct counts and statuses, withdrawn statements retained alongside their replacements, and dependent claims tagged.",
    "L424",
    "Section 15. This register block is the first half of that work; the second half - a 05-HOLDS/ entry for source-repair v2.1 - awaits recovery of D12 (CG-234).")
add("CG-259",
    "Intake priority 5: establish the current source and deployment inventory, distinguishing and version-pinning content routes, utilities, redirects, datasets and generated counts.",
    "L425",
    "Section 15. The fix for CG-174 and IH-251 alike, and the same requirement as IH-270 and IH-272 on the Claude side. Both handoffs make an inventory the precondition for any public number.")
add("CG-260",
    "Intake priority 6: repair P1-P3 implementability with valid and invalid examples, link objects, status separation, geometry, projections and runnable enforcement.",
    "L426", "Section 15. Gated on CG-158 to CG-173 and on recovery of D13.")
add("CG-261",
    "Intake priority 7: complete the substantive Rigvedic foundation when resumed, with ten populated CSVs, query logs, actual accessed sources and counts that are reproducible or explicitly partial.",
    "L427", "Section 15. Gated on CG-131 to CG-142.")
add("CG-262",
    "Intake priority 8: reconcile deck, site and backlog coverage with existing, partial, renamed, merged, absent and unknown dispositions supported by actual routes and content.",
    "L428",
    "Section 15. The six dispositions are a finer instrument than a binary present/absent and are the operational answer to CG-041 and CG-176. This repository's 06-BACKLOG/ is where it would live.")
add("CG-263",
    "Intake priority 9: resolve the visual hierarchy and the selected logo through an owner-scoped choice with an approved reference or prototype, not a merged memory description.",
    "L429", "Section 15. Gated on CG-052, CG-056, CG-180 and CG-220. Two owner decisions, not one.")
add("CG-264",
    "Intake priority 10: correct the deck content and demonstrate one experience, with current/proposed/future separation, real records and assets, rights, and one complete visitor loop.",
    "L430", "Section 15. Gated on CG-089 and CG-090.")
add("CG-265",
    "Intake priority 11: expand independent dossiers and museum pages with reviewed bounded claims, source locators, appropriate uncertainty, production screenshots and correction propagation.",
    "L431", "Section 15. Correction propagation is the open failure CG-188 instances.")
add("CG-266",
    "Intake priority 12: cost and finance an actual pilot with bottom-up costs, founder labour separately, rights, review, translation, accessibility and maintenance, cash timing and signed commitments.",
    "L432", "Section 15. Gated on CG-246 to CG-252.")
add("CG-267",
    "Minimal persistent records to carry into Headquarters, preserving existing register names where they exist: RESEARCH-INHERITANCE.md, HYPOTHESIS-ELIGIBILITY.csv, SOURCE-DEPENDENCY.json, BIAS-FAILURE-LOG.csv, REAUDIT-QUEUE.csv, INTERNAL-CONTRADICTIONS.csv, DECK-SITE-COVERAGE.csv, BACKLOG-COVERAGE.csv, source-access ledgers, and withdrawn and replaced-claim history.",
    "L436",
    "Section 15. Present in this repository: 04-AUDITS/BIAS-FAILURE-LOG.csv, 04-AUDITS/REAUDIT-QUEUE.csv, 02-SOURCES/access-ledger.csv, 03-REGISTERS/domain-e-hypothesis-eligibility.csv, and 01-INHERITED/RESEARCH-INHERITANCE.md per the CLAUDE.md layout. Absent: INTERNAL-CONTRADICTIONS.csv, DECK-SITE-COVERAGE.csv, BACKLOG-COVERAGE.csv. SOURCE-DEPENDENCY.json exists as 02-SOURCES/dependency.csv, a renamed and reformatted equivalent.")
add("CG-268",
    "Add explicit original-message provenance to owner decisions, and do not silently rename all inherited IDs.",
    "L436",
    "Section 15. FLAG - this instruction is already in tension with a decision taken in this repository. CLAUDE.md renames the inherited handoff's owner decisions from D-01 to D-20 into HD-01 to HD-20 so that D- means one thing here, and records the renaming in 09-DECISIONS/DECISION-ID-MAP.csv. The rename is documented rather than silent, so the letter of the instruction is met; whether the substance is met is an owner question, not one this pass resolves. Registered, not acted on. The same instruction is why the ChatGPT handoff's D01-D15 artifact labels are kept unrenamed at CG-222 and simply flagged as a separate namespace.")
add("CG-269",
    "For each correction record: original claim; source, thread and locator; author; prior status; correction date or known sequence; reason; replacement; remaining uncertainty; affected pages, data, SVGs, captions and metadata; and propagation state. Mark exact dates unknown where unavailable.",
    "L438",
    "Section 15. An eleven-field correction schema, materially richer than this register's eight columns, and the field 'affected pages, data, SVG, captions and metadata' is precisely what CG-188's Irula residue needed. Registered as a schema proposal for a future corrections register; not adopted here.")
add("CG-270",
    "For each task record: desired visitor or research outcome; source dependencies; inherited work; acceptance evidence; authority and scope; blocking versus nonblocking hold; and current artifact version. A future agent should be able to resume from the latest checkpoint without asking the owner to reconstruct the project.",
    "L440",
    "Section 15. The blocking-versus-nonblocking distinction is live in this repository as the split between DECISIONS-NEEDED.md and 09-DECISIONS/OWNER-DECISIONS.csv. The closing sentence is the test this whole handoff is written against, and the same test IH-368 states from the Claude side.")

# ---------- SECTION 16 : non-repetition instructions ----------
# Twelve instructions, one row each, so drafts can be checked against them by ID.
add("CG-271",
    "NON-REPETITION 1 of 12: do not restart from a generic standard narrative or a generic project brief.",
    "L444",
    "Section 16. The instruction against the failure CLAUDE.md's governing principle names - reproducing a dominant account. Compare IH-004: the Claude handoff's own reconstructed failures were reconstructed, not quoted, and reconstruction is where generic narrative re-enters.")
add("CG-272",
    "NON-REPETITION 2 of 12: do not treat an owner's research hypothesis as a historical finding.",
    "L445",
    "Section 16. Governs CG-092 and CG-093 directly, and on the Claude side IH-069 (the owner's position), IH-135 to IH-146 (the hypothesis block) and IH-081. Both handoffs make the owner's preferred explanation testable rather than privileged.")
add("CG-273",
    "NON-REPETITION 3 of 12: do not repeat a rejected claim simply because it remains in an older deck, ZIP or summary.",
    "L446",
    "Section 16. The reason CLAUDE.md forbids deleting a REJECTED row: the rejection has to stay visible where the stale copy is still circulating. Compare IH-074 (the INDUSVALLI deck is a starting point, not a source) and IH-191.")
add("CG-274",
    "NON-REPETITION 4 of 12: do not label a packet complete because files exist or because a closing phrase says ready for review.",
    "L447",
    "Section 16. Restates CG-064, CG-074, CG-112 and CG-185, and is convergent with IH-167 and IH-350. The most frequently restated instruction in the document.")
add("CG-275",
    "NON-REPETITION 5 of 12: do not treat inaccessible or secondarily reported sources as directly inspected.",
    "L448",
    "Section 16. Identical in substance to the Claude handoff's standing rule 9, IH-344: every scholar cited through another scholar or a slide is HELD until read. Instances: CG-124 (Mayrhofer), CG-103 (Talageri), IH-231 to IH-248, IH-200.")
add("CG-276",
    "NON-REPETITION 6 of 12: do not use a partial corpus to certify exhaustive absence or distribution.",
    "L449",
    "Section 16. The negative-evidence standard in one line, and the failure CG-101, CG-104, CG-107 and CG-176 all instance. Convergent with IH-342 and IH-005.")
add("CG-277",
    "NON-REPETITION 7 of 12: do not make the entire museum wait for one unresolved substrate question.",
    "L450",
    "Section 16. The bounded hold of CG-002, CG-106 and CG-184. Convergent with IH-074, where the owner's direction is that publication does not stop while cross-checking continues. Also a caution against this register: an INHERITED-UNVERIFIED block is not a stop order.")
add("CG-278",
    "NON-REPETITION 8 of 12: do not build from the rejected P1-P3 handoff without addressing its actual defects.",
    "L451",
    "Section 16. Restates CG-173. Addressed to a Claude Code session, and the defects are enumerated at CG-159 to CG-172.")
add("CG-279",
    "NON-REPETITION 9 of 12: do not expose internal audit machinery as repetitive visitor copy.",
    "L452",
    "Section 16. Convergent with IH-018 and IH-354 (no meta-commentary, no 'you', no 'that reverses what I said' on a published page) and with CG-045 and CG-217. This register is internal audit machinery and none of it is page copy.")
add("CG-280",
    "NON-REPETITION 10 of 12: do not silently rename MelaKeela, replace its selected mark, adopt a uniform aesthetic, or revive unaccepted governance.",
    "L453",
    "Section 16. Four bans in one line, each meeting an open item: the name (CG-179, against IH-062), the mark (CG-052, CG-058), the aesthetic (CG-180, CG-220, against IH-065 and IH-066), and governance (CG-086, IH-082). Where this instruction and the Claude handoff conflict, the conflict is registered at CG-179 and CG-180 and is not resolved by either document.")
add("CG-281",
    "NON-REPETITION 11 of 12: do not claim current deployment or all-conversation coverage from this document.",
    "L454", "Section 16. Restates CG-010, CG-013 and CG-186.")
add("CG-282",
    "NON-REPETITION 12 of 12: preserve both the successful work and the chronology explaining why other work failed.",
    "L455",
    "Section 16. The closing instruction, and the reason the six-stage source-repair chronology at CG-101 to CG-106 and the six-step correction order at CG-037 to CG-042 are registered stage by stage rather than as outcomes. Live in this repository as CLAUDE.md's 'correction history is preserved'.")
add("CG-283",
    "Outstanding completeness requirement: append transcript-level evidence and exact message and attachment locators when full conversation exports become available, and keep this reconstruction's limitations visible until that reconciliation is complete.",
    "L457",
    "Section 16, closing requirement. The condition on which any row in this block could begin to be promoted, alongside a logged retrieval in 02-SOURCES/access-ledger.csv. Parallel to IH-368 and IH-364.")

# ---------- front matter, registered last so the CG-001..CG-283 body numbering
# ---------- follows the document's own section order ----------
add("CG-284",
    "The document identifies itself as the MelaKeela / Veli ChatGPT Project Handoff, prepared 7 September 2026 UTC for a future Research Headquarters, with the status 'evidence-bounded reconstruction; not a complete transcript export', and requests the filename chatgpt-project-handoff.md.",
    "L1-L6",
    "Front matter. Self-description of the document's own provenance, the counterpart of IH-001 for the Claude handoff. The requested filename is honoured by the committed copy at 01-INHERITED/chatgpt-project-handoff.md. 'Not a complete transcript export' is the document's own headline limitation and is developed at CG-006 to CG-016. Prepared the same day this register pass was made, so the document had no sight of this repository (CG-013).")

# ---------- emit ----------
if __name__ == "__main__":
    ids = [r[0] for r in ROWS]
    assert len(ids) == len(set(ids)), "duplicate claim_id"
    with open("03-REGISTERS/inherited-claims.csv", "a", newline="") as fh:
        csv.writer(fh, quoting=csv.QUOTE_ALL, lineterminator='\n').writerows(ROWS)
    print("appended %d rows: %s .. %s" % (len(ROWS), ids[0], ids[-1]))
