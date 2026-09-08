# `the-archive` — page brief

**Page:** *The Archive: What Survived, What Was Lost, and Why* · MVP rank **15** of 15 · `Extraction / Collection` · Decision `Revise` · Risk `Medium`

**Written:** 2026-09-08
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

**QUESTION.** What manuscript and material record survives, what proportion of it has been catalogued, digitised, read or published, and how is each of those proportions measured?

### Why the remaining six slots are empty

Step 14 draws public copy **from accepted claims**. This page has none: §3 below
records that nothing bearing on it stands above `INHERITED-UNVERIFIED`. Drafting
`WHAT THE EVIDENCE SUPPORTS` from claims at that standing would be writing public
copy for unverified claims, which is what `CLAUDE.md`'s inheritance rule and the
museum framework's Rule S-1 forbid. The slots are therefore left open, with the
work that would fill them named in §6.

| Step 14 slot | Draftable today | Why not |
|---|---|---|
| QUESTION | yes | stated above; a question asserts nothing |
| WHAT IS OBSERVED | partly | the workbook's structural counts are observations *about a page*, not about the past; the page's own observations are unretrieved |
| WHAT THE EVIDENCE SUPPORTS | no | no claim above `INHERITED-UNVERIFIED` |
| WHAT COMPLICATES IT | no | complications are claims too, and carry the same floor |
| WHAT REMAINS UNKNOWN | no | requires the negative-evidence typing of constitution §6, not yet performed |
| MELAKEELA'S CURRENT INTERPRETATION | no | an interpretation over an unverified claim set states confidence retrieval has not earned |
| WHAT WOULD CHANGE IT | no | falsifiers attach to claims; there are no claim rows to attach them to |


### What the workbook records as observed

2,052 words, type `collection-investigation`, **1 estimated source entry**, 0
external links, **5 tables**, 1 inline SVG, 51 inbound links. Source state:
*minimal source section*. Decision `Revise`, Risk `Medium`. H1: *"Everything that
survives — and how little of it has been opened."*

**One source entry supporting five tables** is the sharpest source-to-structure
mismatch in the fifteen. Set it beside `artifact-atlas`: 88 entries, 0 tables.
Both were rated by the same instrument; `method-limits.csv` states its limit
directly — *"a visible bibliography does not prove claim-level support or source
quality."*

The headline is two quantitative claims wearing rhetorical clothes. *Everything
that survives* is a denominator. *How little has been opened* is a numerator over
that denominator. Neither is stated as a number, which is why neither reads as a
claim.


---

## 2. Environment and epistemic posture

**Environment:** `Extraction / Collection`. **Posture — the visitor's relation to the knowledge:** *known but withheld*. **`Avoid` — the failure this posture invites:** *"No spectacle or unsupported allegation"*.

The workbook's own function and effect cells for this environment: function *"Custody, access, classification, loss"*, desired effect *"Severance made visible"*, palette role *"Clinical grey, bone, rust"* (`environment-map.csv`, `INHERITED-UNVERIFIED`).


### Modes available in this posture

| Posture | Source | Atlas | Investigation | Field | Classroom |
|---|---|---|---|---|---|
| Extraction / Collection | mandatory | available | mandatory | forbidden | available |

*(Framework §1.7.)*


### Derivation

**Derived posture: underivable today.** §1.5 derives a posture from the
exhibit's Claim Objects and its Absence records, in seven precedence steps. This
page has neither: no Claim Object exists for any proposition on it, and no
absence on it has been typed under constitution §6. Derivation therefore returns
nothing — not `Reading Room`, which is rule 7's residual and would be a false
output, since rule 7 fires on a claim set that has been examined and did not
match rules 1–6.

**Assigned posture: Extraction / Collection, editorially, by the workbook.** That assignment is
`INHERITED-UNVERIFIED` and carries no override reason, because the register that
would hold one does not exist. `SCHEMA.md` §7: *"nothing in `03-REGISTERS/`
records a publication decision, an environment assignment, or a duplication
finding."* Creating the Editorial Register (§11.5) with `derived_posture`,
`assigned_posture`, `override_reason`, `decided_by`, `decided_date` is a
prerequisite for this page, not a nicety: an assignment with no derivation to
disagree with cannot be audited.

**Secondary environment.** The workbook gives this page `Reading Room` as
secondary — as it does for all 96. Framework §1.6.1 rules that a value constant
across every row is not a value: it is the single statement *"Source Mode
exists"*, and the column should be retired rather than migrated. This brief
treats the page's secondary environment as **Source Mode**, a universal display
state, not as a second posture.


Extraction / Collection — *known but withheld* — is the right posture, and the
`Avoid` again does the work: *"no spectacle or unsupported allegation."* A page
about what was lost is where spectacle is cheapest.

**Field Mode is forbidden; Investigation Mode is mandatory** (§1.7). And §1.5's
derivation rule 1 would put this page here on its own terms — an exhibit whose
central claims depend on material whose access status is `NOT ACCESSIBLE` derives
to Extraction / Collection before any other rule fires. Of the fifteen, this and
`custody` are the two whose derived and assigned postures would most likely
agree.

**D-025** governs whether refused and unanswered obligations are published
individually, in aggregate, or only with prior notice — which is the same
question as how this page reports what it could not open.


---

## 3. The evidence it rests on

**No register row in this repository names this page.** A scan of all 14 registers in `03-REGISTERS/` carrying a `supports_page` column returns zero rows for `the-archive` (`04-AUDITS/mvp-fifteen-briefs-build.py`, `scan_supports_page`). Under `CLAUDE.md`'s register format, `supports_page` is what ties a claim to the page it feeds — so on the repository's own accounting, this page is supported by nothing.


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
| `IH-321` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L561` | Work item 53: the synthesis archive must be updated; **section 21 is missing and sections 25–38 are absent**. The project's own archive of its findings has holes it has recorded and not filled. |
| `IH-289` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L525` | Work item 21: synthesis sections 17–19 must be read and **section 18, the CLAIMS LEDGER, was never read**. |
| `IH-002` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L10` | No count in the handoff was re-run against any corpus during compilation; every number is attributed to the file that reported it. No proportion on this page can be sourced to the inheritance. |


`IH-321` and `IH-289` are about the project's own archive rather than about the
manuscript record, and the coincidence is worth stating without over-reading it:
the page arguing that little of the record has been opened is carried by an
inheritance that records its own sections as unread and missing. That is not an
argument against the page. It is a reason its method must be exact, because the
page's claim form — *a large proportion of X remains unexamined* — is one this
project can be shown to be bad at measuring.

**The negative-evidence standard governs the headline.** *"How little of it has
been opened"* must be typed per collection: `NOT PUBLISHED` where catalogues
exist unpublished, `NOT ACCESSIBLE` where they exist and are closed,
`NOT RECOGNIZED` where material is held unidentified, `DOCUMENTED DESTRUCTION`
where loss is recorded. Those four have different causes and different remedies,
and collapsing them into *"how little"* loses exactly the information the page is
for.


### Lowest status among them

**`INHERITED-UNVERIFIED`** — the status of every row above, and of every row that could be listed.


**On "lowest status".** `INHERITED-UNVERIFIED` is not the bottom rung of a
ladder. Framework §3.2: six of the seven statuses describe evidential standing
and one describes *where the assertion came from* — a prior model's summary of
its own conversation — so the interface *"must never sort or colour
`INHERITED-UNVERIFIED` between `PROVISIONAL` and `HYPOTHESIS` as though the
statuses formed a single ladder."* What can be said exactly is the operative
ceiling, and it is the same for all fifteen pages: **nothing bearing on this
page stands above `INHERITED-UNVERIFIED`.** Where the handoff labelled a finding
`VERIFIED` or `PROVISIONAL`, that label came in with it and did not survive
intake — `CLAUDE.md`, the inheritance rule.


---

## 4. Required asset class

From `01-INHERITED/curatorial-audit-v1.1/asset-register.csv`, verbatim (`INHERITED-UNVERIFIED`):


| Field | Value |
|---|---|
| Required asset set | collection record; accession/custody document; object image rights; institutional correspondence; access-status evidence |
| Documentary standard | Verified source, licence, credit, alt text, claim supported, date/place, manipulation disclosure |
| Priority | `MVP` |
| Source / commission route | To research |
| Status | `Needed` |


**How this class should be derived instead.** Framework §1.6.3(a) replaces genre-driven asset classes with a mapping from the exhibit's **evidence-class composition** — the constitution's step 4 inventory. The workbook derived this row from the page's `Type`, a 29-value vocabulary with 17 singletons that `SCHEMA.md` §4 finds *"too sparse to do reliably"* the production-planning work it is doing. Under §1.6.3(a) a page with no recorded evidence classes yields **no** production class, which is the correct output and is this page's actual state.


The Extraction class, as for `custody`, and the same problem: `collection record`,
`accession/custody document` and `institutional correspondence` all require
institutional contact that `IH-215` records as never initiated.
`access-status evidence` is again the one immediately fillable slot and the one
the page most needs — a documented refusal *is* the evidence for *"how little has
been opened"*, and it is evidence the institution can generate itself.

Note the trap in that: an access-status record is evidence about **this
institution's** access, not about the world's. Generalising from what MelaKeela
could not reach to what has not been opened is the inference this page must not
make silently.


---

## 5. What would have to be true before it can launch

Every page in the release carries the shared gates in
`06-BRIEFS/mvp-fifteen/README.md` §4 — the workbook's seven release gates, its
five *Not completed* publication gates, and the ten framework gates F1–F10. They
are not repeated here. What follows is what this page needs **beyond** them.

1. The denominators exist. For each collection named: holdings count, catalogued count, digitised count, publicly readable count — each with its source and the date it was measured.
2. Each of the five tables has sources at row level. One source entry across five tables is not a citation state a `Revise` fixes by rewording.
3. Every absence is typed under constitution §6, per collection, and the difference between unpublished, inaccessible and unrecognised is preserved rather than aggregated.
4. The inference from *what we could not reach* to *what has not been opened* is either evidenced or dropped.
5. **D-025** and `OWNER-DECISIONS.csv` **D-010** are answered, and right-of-reply positions (§11.3) are set for every named holding institution.
6. The *Institutional authority* overlap cluster is addressed — six pages, two of them in the release, recommended as one curated exhibit with a right-of-reply field.


---

## 6. What unit of work would verify it

**MVP-U15 — the coverage denominators register.** One row per named collection:
holdings, catalogued, digitised, publicly readable, each with source and
measurement date; then the absence typing; then, only then, any proportional
statement.

**Retrieval state unsettled, and step 1 is to settle it.** `indianculture.gov.in`
is recorded reachable at `SRC-027` (2026-09-07 re-probe), and the later
characterisation at `SRC-052` records only `github.com` and
`raw.githubusercontent.com` as reachable, with `SRC-081` to `SRC-083` recording
general-web hosts blocked at 15:10Z the same day. The two are not reconcilable
from this brief, so **re-probing the catalogue hosts is the first action of the
unit**, and its result is a ledger row either way — a reachable host is a
retrieval, and a blocked one is an `EGRESS_BLOCKED` row with the URL and what it
was needed for, per `CLAUDE.md`'s blocked-domains rule.

The half that is executable now needs no host at all: the institution's own
access-status evidence, built from the outreach in MVP-U14, is a documented
coverage measurement of exactly one kind and it is honest about which kind.


---

*Brief written 2026-09-08. Nothing in it is public copy. Nothing in it promotes a claim: promotion requires a retrieval event logged in `02-SOURCES/access-ledger.csv`, and this unit performed none.*
