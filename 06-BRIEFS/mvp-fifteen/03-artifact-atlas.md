# `artifact-atlas` — page brief

**Page:** *Artifact Atlas: 175 Ancient South Asian Sites Mapped* · MVP rank **3** of 15 · `Living Signal Field` · Decision `Keep` · Risk `Low`

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

**QUESTION.** Where was each of these objects found, how precisely is each findspot and date known, and which regions are unknown rather than empty?

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

**8 words of prose**, 88 estimated source entries, 0 external links, 0 tables, 2
inline SVGs, 56 inbound links. Type `atlas`. H1: *"Where the objects were
found."* Decision `Keep`, Risk **Low**, MVP rank 3.

The title asserts a number — *"175 Ancient South Asian Sites Mapped"* — and the
number is one side of an open contradiction. Framework §8.1 relays the schema
assessment's collision A, whose words these are — `INHERITED-UNVERIFIED`, quoted
inside a `HYPOTHESIS` document, and not the framework's own verdict: the count
was *"adopted as settled fact, put in a page title, and rated low-risk."*

The `Low` risk rating deserves reading against the instrument that produced it.
`method-limits.csv` says source visibility was estimated from *"visible
Sources/References sections"* and that *"a visible bibliography does not prove
claim-level support or source quality."* 88 visible entries against 8 words of
prose is what produced `Low`. It is a measurement of a page's furniture.


---

## 2. Environment and epistemic posture

**Environment:** `Living Signal Field`. **Posture — the visitor's relation to the knowledge:** *known by relation*. **`Avoid` — the failure this posture invites:** *"No gaming HUD or arbitrary links"*.

The workbook's own function and effect cells for this environment: function *"Relationships, movement, comparison"*, desired effect *"Connected evidence"*, palette role *"Midnight, cyan, sage, orange"* (`environment-map.csv`, `INHERITED-UNVERIFIED`).


### Modes available in this posture

| Posture | Source | Atlas | Investigation | Field | Classroom |
|---|---|---|---|---|---|
| Living Signal Field | mandatory | mandatory | available | available | available |

*(Framework §1.7.)*


### Derivation

**Derived posture: underivable today.** §1.5 derives a posture from the
exhibit's Claim Objects and its Absence records, in seven precedence steps. This
page has neither: no Claim Object exists for any proposition on it, and no
absence on it has been typed under constitution §6. Derivation therefore returns
nothing — not `Reading Room`, which is rule 7's residual and would be a false
output, since rule 7 fires on a claim set that has been examined and did not
match rules 1–6.

**Assigned posture: Living Signal Field, editorially, by the workbook.** That assignment is
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


**Atlas Mode is mandatory** (§1.7), and §8.7 lists eight things the Atlas may
never do. Four are at issue for this page, and only the first can be checked
here, because the build has not been retrieved:

1. *Show a total in its own voice* — the only one checkable from here, and it
   fails: the title in `page-audit.csv` states a count.
2. *Render an approximate location as a precise point* — the risk `IH-105`'s 145
   assumed rows create. Whether v1 in fact renders them as precise points is not
   knowable without the build.
3. *Render unknown as blank* — constitution §13 requires unknown regions to stay
   visibly unknown; a blank map *"reads as empty and empty reads as nobody."*
   Untestable from here.
4. *Let a filter silently drop the weak evidence to produce a cleaner picture.*
   Untestable from here.

§8.1's resolution is the one that makes the page launchable at all: **the Atlas
has no headline count.** A count is a claim with a status, an inclusion rule and
a falsifier, shown inside the Atlas with its status visible, or it is not shown.
Under that rule the Atlas ships *before* D-034 is answered, because it never
asserts a total in its own voice.


---

## 3. The evidence it rests on

**No register row in this repository names this page.** A scan of all 14 registers in `03-REGISTERS/` carrying a `supports_page` column returns zero rows for `artifact-atlas` (`04-AUDITS/mvp-fifteen-briefs-build.py`, `scan_supports_page`). Under `CLAUDE.md`'s register format, `supports_page` is what ties a claim to the page it feeds — so on the repository's own accounting, this page is supported by nothing.


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
| `IH-105` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L230` | The atlas holds 194 site records, 315 class-windows and 14 classes, with **54 of 199 site-class rows dated from excavation reports and 145 marked assumed**. Three quarters of the dating is flagged as assumption inside the dataset itself. |
| `IH-250` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L474` | Contradiction X-01: 140 / 150 / 158 / 167→175 / 194 / 199 sites, and 299 against 315 windows. Resolution path: extract the dataset to JSON, count, and generate every stated figure from it. |
| `IH-057` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L158` | Correction C-37: three different counts on three live surfaces. |
| `IH-060` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L164` | Correction C-40: the owner's visual-concept document and VELI-03 disagree on sites and windows; the handoff blocks the prospectus on it. |
| `IH-201` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L382` | `/artifact-atlas` returns no text to a fetcher because it is JS-rendered. An atlas unreadable without JavaScript fails release gate 5 before any accessibility review begins. |
| `IH-002` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L10` | No count in the handoff was re-run against the atlas HTML. Every figure above is a report of a report. |


### Lowest status among them

**`INHERITED-UNVERIFIED`** — the status of every row above, and of every row that could be listed.


**On "lowest status".** `INHERITED-UNVERIFIED` is not the bottom rung of a
ladder. Framework §3.2: six of the seven statuses describe evidential standing
and one describes *where the assertion came from* — a prior model's summary of
its own conversation — so *"the interface must therefore never sort or
colour `INHERITED-UNVERIFIED` between `PROVISIONAL` and `HYPOTHESIS` as though
the statuses formed a single ladder."* What can be said exactly is the operative
ceiling, and it is the same for all fifteen pages: **nothing bearing on this
page stands above `INHERITED-UNVERIFIED`.** Where the handoff labelled a finding
`VERIFIED` or `PROVISIONAL`, that label came in with it and did not survive
intake — `CLAUDE.md`, the inheritance rule.


---

## 4. Required asset class

From `01-INHERITED/curatorial-audit-v1.1/asset-register.csv`, verbatim (`INHERITED-UNVERIFIED`):


| Field | Value |
|---|---|
| Required asset set | verified dataset; accessible SVG/map; legend; mobile alternative; downloadable table |
| Documentary standard | Verified source, licence, credit, alt text, claim supported, date/place, manipulation disclosure |
| Priority | `MVP` |
| Source / commission route | To research |
| Status | `Needed` |


**How this class should be derived instead.** Framework §1.6.3(a) replaces genre-driven asset classes with a mapping from the exhibit's **evidence-class composition** — the constitution's step 4 inventory. The workbook derived this row from the page's `Type`, a 29-value vocabulary with 17 singletons that `SCHEMA.md` §3 finds *"too sparse to do reliably"* the production-planning work it is doing. Under §1.6.3(a) a page with no recorded evidence classes yields **no** production class, which is the correct output and is this page's actual state.


This is the one page of the fifteen whose asset set is not embargoed by §3.12 —
its assets are a dataset and its presentation, not diagrams derived from
individual claims. It is instead gated on the dataset existing as objects:
`verified dataset` presupposes Universal Evidence Objects with typed Place
Assertions and typed Date Assertions (§2.7, §2.8), and the 145 rows marked
*assumed* must each be typed rather than rendered. The `downloadable table` and
the exclusion export (§5.2) are the parts that make every absence argument on the
map checkable, and they are the parts most easily deferred.


---

## 5. What would have to be true before it can launch

Every page in the release carries the shared gates in
`06-BRIEFS/mvp-fifteen/README.md` §4 — the workbook's seven release gates, its
five *Not completed* publication gates, and the ten framework gates F1–F10. They
are not repeated here. What follows is what this page needs **beyond** them.

1. No headline count anywhere on the page, per §8.1. The number in view is a property of the current filter and is shown with the filter.
2. Every mapped thing is an object with a status and an attestation mode; a findspot and an attributed provenance are never the same marker (§8.2).
3. The 145 `assumed` date rows are typed as assertions with their basis, or excluded. Rendering them identically to the 54 report-dated rows is `IH-105` published as if it were `IH-105` solved.
4. Unknown zones are a rendered layer, and the excavation/survey coverage overlay exists (§8.2) — without it no absence on the map is checkable.
5. The page renders without JavaScript, or has a documented equivalent (`IH-201`; release gate 5).
6. The exclusion set is exportable (§5.2).


---

## 6. What unit of work would verify it

**MVP-U3 — atlas dataset extraction and count derivation.** The unit is already
specified, by the inheritance itself: `IH-250`'s recorded resolution path is
*"extract the atlas dataset to JSON, count, and generate every stated figure from
it."* Done properly it produces a register of site records with typed place and
date assertions, a dependency map for the 88 bibliography entries (framework §3.5
— 88 citations tracing to a handful of excavation reports count as a handful),
and a derived count with an inclusion rule.

**Blocked on one thing, and it is not egress.** The atlas data lives in
`artifact-atlas.html` inside `veli-site(3).zip`, supplied 2026-09-01. That archive
**is not in this repository** and has no access-ledger row — which is why the
whole workbook is `INHERITED-UNVERIFIED` rather than merely unverified. The
unblocking action is the owner supplying the archive, or naming the authoritative
build (D-033). Until then a `HOLD` row is owed, and this page cannot be the
release's connective heart on a dataset nobody here has opened.


---

*Brief written 2026-09-08. Nothing in it is public copy. Nothing in it promotes a claim: promotion requires a retrieval event logged in `02-SOURCES/access-ledger.csv`, and this unit performed none.*
