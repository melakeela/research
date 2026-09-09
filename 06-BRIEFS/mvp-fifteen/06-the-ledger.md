# `the-ledger` — page brief

**Page:** *The Source Ledger: Ranking Evidence and Checking Scholars* · MVP rank **6** of 15 · `Reading Room` · Decision `Keep` · Risk `Low`

**Written:** 2026-09-08 · **revised:** 2026-09-09
**Unit type:** page brief. A brief is a statement of what a page would have to
be and what it would have to rest on. It is **not public copy**, and no
sentence in it may be lifted onto a page.
**Status of this brief:** every design statement is `HYPOTHESIS`, inherited
from `13-PRODUCT-ARCHITECTURE/museum-framework.md`, whose own §14.4 puts every
design proposition it contains at `HYPOTHESIS`. Every statement drawn from
`01-INHERITED/curatorial-audit-v1.1/` is `INHERITED-UNVERIFIED`. No retrieval
was performed to write this brief and no row was added to
`02-SOURCES/access-ledger.csv`.
**Method:** `04-AUDITS/mvp-fifteen-briefs-build.py`; index and shared gates in
`06-BRIEFS/mvp-fifteen/README.md`.


---

## 1. The question, in step 14 form

**QUESTION.** By what rule does this institution rank evidence, and how may a visitor check that rule against any claim the institution makes?

### Why the remaining six slots are empty

Step 14 draws public copy **from accepted claims**. This page has none: §3 below records that every row bearing on it carries `INHERITED-UNVERIFIED` and no other status appears. Drafting
`WHAT THE EVIDENCE SUPPORTS` from claims at that standing would be writing public
copy for unverified claims, which is what `CLAUDE.md`'s inheritance rule and the
museum framework's Rule S-1 forbid. The slots are therefore left open, with the
work that would fill them named in §6.

| Step 14 slot | Draftable today | Why not |
|---|---|---|
| QUESTION | yes | stated above; a question asserts nothing |
| WHAT IS OBSERVED | partly | the workbook's structural counts are observations *about a page*, not about the past; the page's own observations are unretrieved |
| WHAT THE EVIDENCE SUPPORTS | no | no claim outside the `INHERITED-UNVERIFIED` floor |
| WHAT COMPLICATES IT | no | complications are claims too, and carry the same floor |
| WHAT REMAINS UNKNOWN | no | requires the negative-evidence typing of constitution §6, not yet performed |
| MELAKEELA'S CURRENT INTERPRETATION | no | an interpretation over an unverified claim set states confidence retrieval has not earned |
| WHAT WOULD CHANGE IT | no | falsifiers attach to claims; there are no claim rows to attach them to |


### What the workbook records as observed

948 words, type `research-essay`, 26 estimated source entries, 0 external links,
0 tables, 0 inline SVGs, 10 inbound links. Decision `Keep`, Risk `Low`. H1: *"The
Ledger."* The workbook's assessment names the trap: *"its readiness depends on
claim-level citations, not prose confidence."*

Note the shape. 26 bibliography entries, no table, no external link, on a page
whose subject is how to check sources.


---

## 2. Environment and epistemic posture

**Environment:** `Reading Room`. **Posture — the visitor's relation to the knowledge:** *known by argument from sources*. **`Avoid` — the failure this posture invites:** *"No visual fatigue or luxury minimalism"*.

The workbook's own function and effect cells for this environment: function *"Long argument, sources, methods"*, desired effect *"Deep legibility"*, palette role *"Warm paper, ink, restrained gold"* (`environment-map.csv`, `INHERITED-UNVERIFIED`).


### Modes available in this posture

| Posture | Source | Atlas | Investigation | Field | Classroom |
|---|---|---|---|---|---|
| Reading Room | mandatory | available | mandatory | forbidden | available |

*(Framework §1.7.)*


### Derivation

**Derived posture: underivable today.** §1.5 derives a posture from the
exhibit's Claim Objects and its Absence records, in seven precedence steps. This
page has neither: no Claim Object exists for any proposition on it, and no
absence on it has been typed under constitution §6. Derivation therefore returns
nothing — not `Reading Room`, which is rule 7's residual and would be a false
output, since rule 7 fires on a claim set that has been examined and did not
match rules 1–6.

**Assigned posture: Reading Room, editorially, by the workbook.** That assignment is
`INHERITED-UNVERIFIED` and carries no override reason, because the register that
would hold one does not exist. `SCHEMA.md` §7: *"Nothing in `03-REGISTERS/`
records a publication decision, an environment assignment, or a duplication
finding."* Creating the Editorial Register — specified at §11.5 as
`03-REGISTERS/editorial-decisions.csv`, with `decision_type` including
`posture-assignment`, and with `value`, `derived_value`, `override_reason` and
`derived_residual` — is a prerequisite for this page, not a nicety: an
assignment with no derivation to disagree with cannot be audited.

*(Note for the framework's own re-audit: §1.5 names these fields
`derived_posture` / `assigned_posture` / `override_reason`, and §11.5 names them
`value` / `derived_value` / `override_reason` / `derived_residual`. The two
sections of the specification do not agree on the field names for the same
record. This brief follows §11.5, which is the section that defines the
register. Recorded, not resolved — it is a defect in the specification, not in
this page.)*

**Secondary environment.** The workbook gives this page `Reading Room` as
secondary — as it does for all 96. Framework §1.6.1 rules that a value constant
across every row is not a value: it is the single statement *"Source Mode
exists"*, and the column should be retired rather than migrated. This brief
treats the page's secondary environment as **Source Mode**, a universal display
state, not as a second posture.


**This page is the type case of Reading Room *as posture*.** §1.6.1 distinguishes
Reading Room the posture — an exhibit *"whose substance is the argument itself:
methods pages, historiography, the ledger"* — from Reading Room the substrate,
the fallback state 34 of 96 pages were filed under because the audit had nothing
more specific to say. `the-ledger` is named in the framework as an example of the
former. Its assignment is therefore the one Reading Room assignment in the
fifteen that is not suspected of being residual.

**And it is the page most exposed to an open owner decision.**
`DECISIONS-NEEDED.md` **D-015** asks whether Reading Room remains a seventh peer
posture at all or is demoted entirely to Source Mode, leaving six. If it is
demoted, this page does not lose its content — but the institution loses the
posture it was assigned to, and the page becomes an exhibit displayed in Source
Mode. Recorded, not resolved.

**Investigation Mode is mandatory; Field Mode is forbidden** (§1.7).


---

## 3. The evidence it rests on

**No register row in this repository names this page.** A scan of all 15 registers in `03-REGISTERS/` carrying a `supports_page` column returns zero rows for `the-ledger` (`04-AUDITS/mvp-fifteen-briefs-build.py`, `scan_supports_page`). Under `CLAUDE.md`'s register format, `supports_page` is what ties a claim to the page it feeds — so on the repository's own accounting, this page is supported by nothing.


**Adjacency is not support.** Where verified work in this repository happens to
be *about subjects a page discusses*, it is still not *linked to that page*: no
row in any register carries `supports_page` naming this slug. Under framework §3.3 a
claim's status comes from its own Evidence Links, so a page cannot inherit
standing by sitting next to a register. Linking is an editorial act (§11.5) and
transfers nothing by itself; the page's propositions have to be written as Claim
Objects and evidenced in their own right.


What exists instead is inherited material that **bears on** this page without being linked to it. Every row below is from `03-REGISTERS/inherited-claims.csv`, whose 369 rows all carry `INHERITED-UNVERIFIED` and all carry an empty `supports_page`.


| claim_id | status | locator | what it bears on |
|---|---|---|---|
| `IH-046` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L134` | Correction C-26, **caught by the owner**: Claude built the Ledger credibility feature and then cited caste-page sources without auditing them, leaving Kabir Babu 2016 (off-field, no findable footprint), Choudhury 2021 (MDPI preprint) and Kumar & Choudhury 2020 visibly carrying claims that Aktor, Davis, Olivelle, Beteille and the corpus actually support. Rejected as R-20; superseded as S-13 — audit-after-build replaced by audit-first. Also recorded as owner decision HD-17 and work item 49. |
| `IH-289` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L525` | Work item 21: synthesis sections 17–19 must be read, **section 18 may be a ledger draft, and this was never done**. The prior articulation of the ledger's own rule has not been read by anyone in the current record. |
| `IH-183` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L328` | Superseded row S-10: 'The Ledger and the First Gallery' was the first of four MVP shapes, none adopted by the owner (X-10). The page is a survivor of a release plan that was replaced three times. |


`IH-046` is the most consequential row in the fifteen, and it is about this page.
The feature that ranks source credibility was built and then found to be resting
on three sources it would itself have demoted. The failure was found by the owner,
not by the system, and the recorded fix was a workflow inversion — audit first.
That inversion is a claim about how this institution works, and it is a claim
this page makes in public.


### Lowest status among them

**`INHERITED-UNVERIFIED`** — the status of every row above, and of every row that could be listed.


**On "lowest status".** `INHERITED-UNVERIFIED` is not the bottom rung of a
ladder. Framework §3.2: six of the seven statuses describe evidential standing
and one describes *where the assertion came from* — a prior model's summary of
its own conversation — so *"the interface must therefore never sort or
colour `INHERITED-UNVERIFIED` between `PROVISIONAL` and `HYPOTHESIS` as though
the statuses formed a single ladder."* The floor above is therefore stated by
rule rather than by sorting: a row carrying `INHERITED-UNVERIFIED` has had no
retrieval event behind it, so no set containing one stands above it. **Every row bearing on this page carries `INHERITED-UNVERIFIED`, and no other status appears.**
Where the handoff labelled a finding `VERIFIED` or `PROVISIONAL`, that label came
in with it and did not survive intake — `CLAUDE.md`, the inheritance rule.


---

## 4. Required asset class

From `01-INHERITED/curatorial-audit-v1.1/asset-register.csv`, verbatim (`INHERITED-UNVERIFIED`):


| Field | Value |
|---|---|
| Required asset set | opening atmosphere asset; claim-specific diagram; source facsimile; social card |
| Documentary standard | Verified source, licence, credit, alt text, claim supported, date/place, manipulation disclosure |
| Priority | `MVP` |
| Source / commission route | To research |
| Status | `Needed` |


**How this class should be derived instead.** Framework §1.6.3(a) replaces genre-driven asset classes with a mapping from the exhibit's **evidence-class composition** — the constitution's step 4 inventory. The workbook derived this row from the page's `Type`, a 29-value vocabulary with 17 singletons that `SCHEMA.md` §3 finds *"too sparse to do reliably"* the production-planning work it is doing. Under §1.6.3(a) a page with no recorded evidence classes yields **no** production class, which is the correct output and is this page's actual state.


`claim-specific diagram` is embargoed under §3.12 — with a particular irony
worth naming, since the diagram a ledger page wants is a diagram of the status
derivation, and that diagram would depict a rule rather than a historical claim.
The embargo is on assets derived from Claim Objects; a diagram of the framework's
own §3.2 derivation table is a diagram of a specification, not of a claim, and
is not blocked. That distinction should be made explicitly rather than left for
a production scheduler to guess.


---

## 5. What would have to be true before it can launch

Every page in the release carries the shared gates in
`06-BRIEFS/mvp-fifteen/README.md` §4 — the workbook's seven release gates, its
five *Not completed* publication gates, and the ten framework gates F1–F10. They
are not repeated here. What follows is what this page needs **beyond** them.

1. The ranking rule the page describes **is** the rule the repository runs: `CLAUDE.md`'s seven statuses, framework §3.2's derivation table, and the independence rule in `02-SOURCES/dependency.csv`. A ledger page describing a different rule from the one the registers implement is a second source of truth.
2. The page states the §3.2 interface consequence in public: no user action can raise a claim's status; there is no status dropdown. This is the institution's strongest verifiable commitment and the cheapest to state.
3. The three sources demoted under C-26/R-20 are gone from wherever they still sit, and the re-attribution recorded as owed on `birth-was-not-always-destiny` and `jatization` is confirmed done — the handoff lists it among the **unconfirmed** items.
4. There are claims to rank. A ledger over a claim set that is entirely `INHERITED-UNVERIFIED` displays one status and demonstrates nothing; at least one page in the release must have rows above the floor before this page has anything to show.
5. Synthesis section 18 is read (`IH-289`, work item 21), or its absence is recorded, before the page asserts a ledger rule that a prior draft may already have stated differently.


---

## 6. What unit of work would verify it

**MVP-U6 — re-derive the ledger rule in-repository.** No egress required, and
that makes this the second unit to run after MVP-U4. Reconstruct the ranking rule
from `CLAUDE.md`'s status vocabulary, `00-CONTROLLER/CONTROLLER-RECONCILIATION.md`
C-1's mapping of the constitution's inheritance dispositions onto statuses, and
framework §3.2; record it as a specification, not as a finding; check it against
what `04-AUDITS/validate-registers.py` actually enforces; and write the C-26
demotions into `02-SOURCES/dependency.csv` so the failure is preserved rather
than described. Correction history is preserved — `CLAUDE.md`: never delete a
`REJECTED` row.

**What it cannot do.** It cannot verify anything about the past, and it must not
be mistaken for evidentiary work. It produces a specification and a correction
record. That is exactly what this page needs and it is the reason this page could
be ready before most of the other fourteen.


---

*Brief written 2026-09-08, revised 2026-09-09. Nothing in it is public copy. Nothing in it promotes a claim: promotion requires a retrieval event logged in `02-SOURCES/access-ledger.csv`, and this unit performed none.*
