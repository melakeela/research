# Controller reconciliation

`00-CONTROLLER/METHODOLOGY-CONSTITUTION.md` (the owner's amendment,
committed unchanged) against `CLAUDE.md` as it stood before this pass.

This document does four things: names what each has that the other lacks,
names where they conflict and how each conflict is resolved, and separates
the amendment's methodology — which carries over intact — from its
operational instructions, which were written for a Claude Chat packet
workflow that this repository has replaced.

Nothing here amends the constitution. Where the two disagree on a matter of
evidence discipline, the reconciliation says which rule the repository runs
under and why; those resolutions are what the rewritten `CLAUDE.md` encodes.

---

## 1. What `CLAUDE.md` has that the amendment lacks

The amendment is a methodology. It is silent on how a claim becomes a record
in a repository. Everything in this section is repository machinery with no
counterpart in the amendment, and all of it survives.

| Existing rule | Why the amendment does not supply it |
|---|---|
| **Evidence status vocabulary** — `VERIFIED` · `PROVISIONAL` · `HYPOTHESIS` · `INHERITED-UNVERIFIED` · `REJECTED` · `SUPERSEDED` · `HOLD`, exactly one per claim, none unstatused | The amendment has a seven-term list (§3) but it is an inheritance triage vocabulary, not a claim-status vocabulary. See conflict C-1. |
| **The inheritance rule** — promotion out of `INHERITED-UNVERIFIED` requires a logged retrieval event; argument does not promote a claim, confidence does not promote a claim | The amendment says inherited work must be verified but never defines what verification *is* as an event. Without the retrieval requirement, "CONFIRMED" is a model's self-assessment. |
| **Register format** — `claim_id,claim,status,source_id,locator,retrieval_date,supports_page,notes`, one claim per row, `source_id` resolving to the access ledger, locators specific enough to re-find | The amendment specifies columns for two files (`HYPOTHESIS-ELIGIBILITY.csv`, `BIAS-FAILURE-LOG.csv`) and none for claims themselves. |
| **`02-SOURCES/access-ledger.csv`** as the record of retrieval events | The amendment's Step 5 audits source genealogy but assumes sources are already in hand. |
| **Blocked-domain rule** — `EGRESS_BLOCKED` rows, no working around the proxy, no WebSearch snippet standing in for a source, domains listed in the PR | This repository runs behind an egress proxy. A chat workflow did not. |
| **Commit-and-push after every substantive unit** | Chat state persisted in a conversation and a checkpoint ZIP. Repository state persists only in commits. |
| **Directory scheme** `00-CONTROLLER/` … `05-HOLDS/` | The amendment names twelve bare filenames with no location. See conflict C-3. |
| **Owner-settled positions** — Kumari Kandam, Sumerian-Dravidian origin, Austroasiatic-as-oldest are logged claims under examination, never working assumptions | Not mentioned. These are exactly the counter-narrative attractors the amendment's §8 second test guards against, so the two reinforce each other. |
| **Anti-planning rule** — do not stop at "sources identified" and hand back a plan; run the retrieval | The amendment's posture is the opposite by design. See conflict C-6. |
| **Escalation categories and `DECISIONS-NEEDED.md`** — payment/institutional access, lawful acquisition, two viable interpretive positions, living-community consent, publication approval; everything else accumulates rather than interrupts | The amendment's §14 lists eight product and institutional decisions but no rule for what qualifies as an escalation in general. See conflict C-4. |
| **PR as the release gate; Codex as independent adversarial reviewer; `AGENTS.md` as its mirror** | The amendment's gate is owner approval in a chat turn. See §4 below. |
| **"Never write site code here"** — the site lives in `melakeela/site` | The amendment forbids production HTML/CSS/JS for a different reason (stage separation, not repository separation). Same effect, different premise. |

---

## 2. What the amendment has that `CLAUDE.md` lacks

`CLAUDE.md` was an evidence-handling controller. It had no theory of how
analysis goes wrong before any claim is written down. That is the whole
subject of the amendment.

**Named failure pattern.** §1 enumerates eleven specific failure modes and
requires them logged, not merely avoided. `CLAUDE.md` had no failure log and
no requirement to record method failure as distinct from a wrong fact.

**Weighting rather than balancing.** `CLAUDE.md`'s "no false equivalence"
prohibits parallel presentation of unequal claims. §2 goes considerably
further: allocate confidence *and space* by evidence, and stay capable of
contradicting canonical scholarship, colonial scholarship, four named
nationalisms, MelaKeela's own pages, the owner's preferred hypothesis, and
your own previous answer. The last three have no equivalent in `CLAUDE.md`.

**The fourteen-step method.** §5. Bound the question; chronology before
similarity; geography and contact; evidence classes kept separate so that
one cannot borrow certainty from another; source genealogy; archive audit;
hypothesis gating before extended analysis; independent evaluation on each
hypothesis's strongest form; proportional space; bridge testing; current
specialist standing as distinct from citation inertia; recorded falsifiers;
self-contradiction check against MelaKeela's own material; and a fixed
seven-part template for public copy. `CLAUDE.md` had two of these as
one-line constraints (chronology/geography gates, source independence).

**Negative-evidence standard.** §6. Absence is not an argument until
production probability, survival probability, excavation coverage,
accessibility and recognizability are recorded, and the absence is typed as
one of eight kinds. `CLAUDE.md` said nothing about arguing from silence.

**Translation standard.** §7. Original script, transliteration, grammatical
form, semantic range, edition, exact locator, alternatives, interpretive
consequence — plus an audit of inherited English categories (*race, tribe,
slave, barbarian, fort, religion, caste, civilization, invasion,
indigenous*). `CLAUDE.md`'s locator rule covered where a word is, never how
it was rendered.

**Two adversarial tests.** §8. Prestige-bias and preferred-counter-narrative,
both run before a unit is complete, and corrected without pretending the two
have had equal institutional power. `AGENTS.md` asked Codex to check
asymmetric scrutiny; the amendment makes it a self-check the producing agent
runs first.

**Attestation gradient.** §4E's eleven-way distinction — attested language,
reconstructed proto-language, accepted loan, proposed substrate form,
historical proposal, weaker fallback, residue, unidentified vocabulary — and
the rule that *unknown is residual, not positive evidence*. `CLAUDE.md` had
no vocabulary for the difference between an attested body of evidence and a
hypothetical donor.

**Cross-domain bridges.** Step 10. Language, ancestry, culture, artifact,
religion, polity and modern identity are separate claims and each link
between them is its own claim. `AGENTS.md` had "unsupported bridges" as a
review heuristic; the amendment makes it a register.

**Archive and power audit.** Step 6 and §4V. Who made the object, supplied
the material, performed the labour, spoke without being recorded, copied,
translated, classified, received credit, was excluded, and holds the object
now. Preservation is not authorship; codification is not invention; first
surviving attestation is not origin.

**Twelve persistent files**, with column schemas given for
`HYPOTHESIS-ELIGIBILITY.csv` and `BIAS-FAILURE-LOG.csv`.

**Substantive research inheritance** — §4A–V, twenty-two domains with their
distinctions and traps already worked out. This is the largest single thing
`CLAUDE.md` lacked: `RESEARCH-QUEUE.md` held three items and a "not yet"
list.

**Two new packets** (R20 The Missing Record, R21 Sacrifice, Renunciation and
Appropriation) and the rule that a packet need not produce a page.

**A product and institutional specification stage** (§12) and the
language-movement Atlas specification (§13) — a class of output this
repository had no home for. See conflict C-5.

**Eighty-nine-item backlog reconciliation** (§10) with a fourteen-verb
disposition vocabulary and a requirement that every item get a destination,
a deliverable, an explicit hold or a reasoned rejection. See conflict C-7.

**Eight owner decisions** (§14).

---

## 3. Conflicts and resolutions

### C-1 — Two status vocabularies

`CLAUDE.md`: `VERIFIED` / `PROVISIONAL` / `HYPOTHESIS` /
`INHERITED-UNVERIFIED` / `REJECTED` / `SUPERSEDED` / `HOLD`.

Amendment §3: `CONFIRMED` / `SUPPORTED` / `PLAUSIBLE` /
`REQUIRES VERIFICATION` / `REVISED` / `REJECTED` / `HELD`.

These are not the same seven terms renamed. `CONFIRMED`, `SUPPORTED` and
`PLAUSIBLE` are confidence assessments a model can assign by reasoning.
`VERIFIED` cannot be assigned by reasoning at all — it requires a retrieval
event in the access ledger. Adopting §3's list as the claim vocabulary would
silently delete the inheritance rule, which is the rule this repository was
built around.

**Resolution.** The repository keeps one claim-status vocabulary: the seven
in `CLAUDE.md`. The amendment's seven are retained as an *inheritance
disposition* — a triage judgement recorded alongside the status, never in
place of it, and never promoting a claim on its own. Mapping:

| Amendment disposition | Repository status |
|---|---|
| `CONFIRMED` | `VERIFIED` — only with a ledger row, locator and retrieval date |
| `SUPPORTED` | `PROVISIONAL` |
| `PLAUSIBLE` | `HYPOTHESIS` |
| `REQUIRES VERIFICATION` | `INHERITED-UNVERIFIED` |
| `REVISED` | `SUPERSEDED`, pointing to what replaced it |
| `REJECTED` | `REJECTED` — row never deleted |
| `HELD` | `HOLD`, with a row in `05-HOLDS/` |

An inherited proposition may be dispositioned `CONFIRMED` and still sit at
`INHERITED-UNVERIFIED` until retrieval happens. That gap is the point.

### C-2 — "Do not start from zero" against the inheritance rule

§3 says prior reasoning must not be discarded and re-derived. The inheritance
rule says everything in `01-INHERITED/` enters as `INHERITED-UNVERIFIED`
including material the handoffs label verified.

**Resolution.** No conflict on inspection, and both survive: inherited
*reasoning, distinctions and source leads* are preserved and extended;
inherited *evidentiary standing* is not. §4A–V is preserved as the research
agenda it is. It does not enter as findings.

### C-3 — Twelve bare filenames against a numbered directory scheme

The amendment names twelve files with no paths. Two collide with existing
repository files under different names or formats:

- `SOURCE-DEPENDENCY.json` against `02-SOURCES/dependency.csv` (named in
  `CLAUDE.md`, not yet created).
- `RESEARCH-QUESTION-REGISTER.csv` against the `03-REGISTERS/` claim-row
  format, which registers claims rather than questions.

**Resolution.** Assign homes; do not duplicate stores. Proposed placement,
to be created when the work that fills each begins:

| File | Home |
|---|---|
| `METHODOLOGY-CONSTITUTION.md` | `00-CONTROLLER/` — **exists** |
| `RESEARCH-INHERITANCE.md` | `01-INHERITED/` |
| `RESEARCH-QUESTION-REGISTER.csv` | `03-REGISTERS/` — questions, not claims; separate file from the claim registers |
| `HYPOTHESIS-ELIGIBILITY.csv` | `03-REGISTERS/` |
| `SOURCE-DEPENDENCY.json` | `02-SOURCES/` — see below |
| `ARCHIVE-AND-POWER-AUDIT.csv` | `04-AUDITS/` |
| `CROSS-DOMAIN-BRIDGES.csv` | `03-REGISTERS/` |
| `INTERNAL-CONTRADICTIONS.csv` | `04-AUDITS/` |
| `BIAS-FAILURE-LOG.csv` | `04-AUDITS/` |
| `OWNER-DECISIONS.csv` | `09-DECISIONS/` — **exists** |
| `BACKLOG-COVERAGE.csv` | `06-BACKLOG/` |
| `REAUDIT-QUEUE.csv` | `04-AUDITS/` |

On the dependency store: one source of truth, not two. The recommendation is
that `02-SOURCES/dependency.csv` is authoritative — it is the format the rest
of the evidence base uses and the one a reviewer can diff — and
`SOURCE-DEPENDENCY.json` is generated from it when a JSON consumer exists.
This is a small deviation from the amendment's literal instruction and is
logged as owner decision **D-013**.

### C-4 — Two owner-facing surfaces

`README.md` states that `DECISIONS-NEEDED.md` is "the only thing that asks
anything of the owner." The amendment requires `OWNER-DECISIONS.csv`.

**Resolution.** They are not the same instrument. `DECISIONS-NEEDED.md` is
the escalation surface for blockers arising *from research in progress* —
access, acquisition, consent, two live interpretive positions, publication.
`OWNER-DECISIONS.csv` is a standing register of *product, scope and
institutional* decisions that are not blockers and do not interrupt anything.
Both exist; the sentence in `README.md` is now wrong and is corrected in the
same pass as the rewritten controller. Where an item qualifies for both, it
lives in `DECISIONS-NEEDED.md` and is cross-referenced from the CSV.

**Amended 2026-09-07 — one identifier namespace.** Being two instruments did
not make them two identifier spaces, and they were allocating `D-` numbers
independently: both files used D-004, D-005 and D-006 for different decisions.
`09-DECISIONS/OWNER-DECISIONS.csv` is now authoritative for the namespace and
for `status`, and carries a row for every owner decision including the
blocking ones; `DECISIONS-NEEDED.md` holds the argument and allocates nothing.
The CSV rows kept their numbers because D-004 to D-011 map one-to-one onto the
amendment's §14 bullets 1 to 8; the three colliding sections in
`DECISIONS-NEEDED.md` became D-032 to D-034.
`09-DECISIONS/DECISION-ID-MAP.csv` records every old identifier against its
replacement, which is how a `D-` reference in a document written before this
date is resolved.

### C-5 — Product specification against "output is evidence packages"

`README.md` says output is evidence packages and page briefs. The amendment's
§12 and §13 require product specifications, data-object models, an Atlas mode
specification, governance, rights, accessibility and multilingual
architecture. That is a different class of artifact, and none of it is site
code.

**Resolution.** Specifications are permitted here — they are not code — but
they need a home and they must not be confused with research. Proposed
`07-PRODUCT-SPECS/`, created when §12 work starts, with a standing rule that
no specification may cite a claim above its register status. Whether product
and institutional specification belongs in this repository at all, or in
`melakeela/site`, is owner decision **D-012**.

### C-6 — Stop-and-wait against the anti-planning rule

Amendment §16 step 12: "Stop. Do not begin the next research stage in the
same response." `CLAUDE.md`: "Do not stop at 'sources identified' and hand
back a plan. Run the retrieval."

**Resolution.** The amendment's stop is a one-time gate on the controller
amendment itself — the task in hand — not a standing rule of work. Once the
controller is approved, the anti-planning rule governs: research runs to
retrieval, and a `HOLD` row plus the next item is the response to an
unreachable source, not a handback. Recorded so that §16 is not later read as
licensing a plan-shaped deliverable.

### C-7 — A binding document that is not present

§10 declares the 89-item "MelaKeela.com v2 — Master Research, Product &
Institutional Backlog" binding. It is not in this repository, and it is not
in the material supplied with this task. §16 likewise requires reading "every
file in the previously supplied prompt-pack ZIP", which is also absent.

**Resolution.** `BACKLOG-COVERAGE.csv` cannot be created without inventing
its eighty-nine rows, which would be exactly the failure the repository
exists to prevent. The requirement stands; it is on `RESEARCH HOLD` pending
the source documents. See §5 below for what is needed.

### C-8 — Two files named "constitution"

`00-CONTROLLER/RESEARCH-CONSTITUTION.md` already existed: twenty-six standing
rules copied verbatim from §11 of the inherited handoff, and marked
`INHERITED-UNVERIFIED` on its own first line. It is inherited material about
method, not a controller, and several of its rules overlap the amendment's
(C-06/C-38 on meta-commentary, C-16 on symmetry of skepticism, C-17 on
attested versus unattested donors, D-10 on northern priority as an excavation
artefact).

**Resolution.** `METHODOLOGY-CONSTITUTION.md` is the methodology this
repository runs under. `RESEARCH-CONSTITUTION.md` stays where it is and keeps
its inherited status: a claim inventory about method, to be tested against
the amendment domain by domain, not a second source of authority. Its
twenty-six rules are candidates for `RESEARCH-INHERITANCE.md` when that file
is built. Nothing cites it as governing.

### C-9 — Proportional space in a repository with no pages

Steps 9 and 14 govern space allocation, map prominence, interface weight and
public copy. This repository produces registers and briefs, not pages.

**Resolution.** Both apply at brief level. Step 9 constrains what a page
brief may allocate; Step 14's seven-part template is the required shape of
any drafted public copy, and copy may only be drafted from accepted claims.
Neither authorises writing pages here.

---

## 4. Methodology that carries over versus chat-workflow mechanics

### Carries over intact

§1 failure pattern · §2 governing principle and the contradiction list ·
§3 as a disposition vocabulary (per C-1) · §4A–V research inheritance ·
§5 the fourteen steps · §6 negative-evidence standard · §7 translation
standard · §8 both adversarial tests · §9's twelve files and the two column
schemas · §10's disposition verbs · §11 R20 and R21 · §12's specification
subject list · §13's Atlas requirements · §14's eight decisions.

### Written for a chat workflow this repository has replaced

These are not wrong. They are addressed to an agent whose state lived in a
conversation and whose deliverable was an archive file. In a git repository
with a pull-request gate they have direct equivalents, and using them
literally would be worse than using the equivalents.

| Chat-workflow instruction | Repository equivalent |
|---|---|
| "the prompt-pack ZIP already supplied"; "Read every file in the previously supplied prompt-pack ZIP" (§16.1) | Files committed to the repository. Nothing that is not in the repository or explicitly attached to a task can be read. Absent inputs become `HOLD` rows, not assumptions. |
| "Update the cumulative checkpoint ZIP" (§16.9); "return an amended cumulative checkpoint" | Commits. The branch *is* the checkpoint, and it is cumulative by construction. |
| "Verify that the ZIP opens and contains every referenced file" (§16.10) | A file-existence check across the working tree, run before opening the PR. Same intent, no archive. |
| §15 Final ZIP expansion — directories `11-backlog-coverage/` through `19-one-year-operating-roadmap/` inside an archive | Repository directories. The numbering does not survive: this repository already uses `00-`–`05-` for a different scheme, and renumbering to accommodate an archive layout would break every existing reference. The nine subject areas survive as named directories added when their work begins. |
| `final_zip_location` column in `BACKLOG-COVERAGE.csv` (§10) | `repo_path` — the path of the deliverable in this repository. |
| "Pause the existing stage sequence"; "Do not advance to the next numbered research packet yet" (preamble) | Honoured for this task. `RESEARCH-QUEUE.md` is reseeded and no research is begun. |
| "then stop and say 'Ready for next'" / "After I approve it, I will say 'next'" (§16.12) | The pull request. Approval is a merge, not a chat turn. The stop-and-wait protocol does not become a standing rule — see C-6. |
| "Claude Chat produces researched packets; Claude Code reconciles and integrates" | Obsolete as a division of labour here. This repository *is* Claude Code, and it produces the research. The half of the instruction that survives is the prohibition on production HTML/CSS/JS, which coincides with the existing "never write site code here". |
| "Do not create production HTML, CSS or JavaScript" (preamble, §12) | Retained on the existing ground: the site lives in `melakeela/site`. |

---

## 5. What this repository still needs from the owner

Two documents the amendment treats as already supplied are absent, and the
work that depends on them cannot start:

1. **The 89-item "MelaKeela.com v2 — Master Research, Product &
   Institutional Backlog."** Required by §10 and by `BACKLOG-COVERAGE.csv`.
   Needs to be committed to `06-BACKLOG/` before a single coverage row can
   be written honestly.
2. **The prompt-pack ZIP** — the packet definitions for R1–R19, referenced in
   the site review running list as `MELA-KEELA-CLAUDE-FULL-SEQUENCE.md`,
   `MELA-KEELA-LANGUAGE-RESEARCH-PROMPTS.md` and
   `MELA-KEELA-CLAUDE-LIVE-SITE-AUDIT-PROMPT.md`. Required by §16.1 and by
   the amended stage queue, which can currently name R1–R19 only by the
   short descriptions recoverable from the running list.

Both are recorded in `DECISIONS-NEEDED.md`. Neither is reconstructible by
inference, and reconstructing them would produce a plausible document with
nothing behind it — the specific failure mode named in §1.

### Update 2026-09-07 — the prompt-pack arrived; §5.2 and C-7 narrow

Five files were committed unchanged to `00-CONTROLLER/prompt-pack/` and
inventoried in `prompt-pack/PROMPT-PACK-INVENTORY.md`. The paragraphs above
stand as written on the date they were written; what they say is no longer
current, in two respects.

**Item 2 is satisfied.** R1–R19 are defined in full in
`MELAKEELALANGUAGERESEARCHPROMPTS.md`. `RESEARCH-QUEUE.md` no longer names them
by descriptions recovered from the running list; it defines them, with the run
order that three of the five files state identically and the binding dependency
graph. Note that the files are committed under the owner's upload filenames,
which are unhyphenated; the hyphenated names used above and throughout the
running list refer to the same documents. The correspondence is in the
inventory §1.1.

**Item 1 and C-7 narrow but do not close.**
`MELAKEELACLAUDECORRECTIVECONTROLLERv2.md` Part IV enumerates all eighty-nine
backlog items, verified 1–89 with no gaps. `BACKLOG-COVERAGE.csv` no longer has
to invent `backlog_id` or `title`, and the grouping determines several
dispositions outright. It still cannot be completed: `current_site_coverage` and
`existing_route` need a live-site route inventory, and `prior_research_available`
needs the packets. Whether Part IV *is* the backlog or a digest of a longer
document is the narrowed question at `DECISIONS-NEEDED.md` D-014.

**One companion is still absent.** `MELA-KEELA-WHO-MADE-THE-PAST.md`, the fifth
file named in running-list Version 12, did not arrive; R8 is instructed to
cross-link its contribution model.

The intake also found nine conflicts between the pack and the controller,
recorded as `PP-1` to `PP-9` in the inventory. `PP-2` to `PP-6` and `PP-9` are
resolved there by extending **C-1**, **C-3**, **C-6** and §4 to cover the new
sources; none of those resolutions is changed by the extension. `PP-1` is not
resolvable here and is open as **D-035**: this document does not mention the
live public-site audit anywhere, and the audit gate that running-list Version 11
created has been dropped from the constitution rather than reversed. Recorded
here because §4's retirement of the Claude Chat / Claude Code division of labour
is what removed the terms in which Version 11's decision was framed.
