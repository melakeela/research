# `enter` — page brief

**Page:** *Enter Veli: Explore, Exhibits, Evidence, Learn* · MVP rank **2** of 15 · `Tamil Retrofuture` · Decision `Revise` · Risk `Medium`

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

**QUESTION.** What may a visitor take from this institution as established, and what does the institution refuse to assert?

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

1,803 words, type `foyer`, **2 estimated source entries, 0 external links, 0
tables, 0 inline SVGs**, and **113 inbound links** — by a wide margin the most
linked-to page in the audited build. Central public claim: *"Evidence, and what
it will not support."*

Two things follow from those numbers. A page that 113 other pages point at is
load-bearing for the whole site's navigation, so its errors propagate. And a page
whose subject is *evidence* carrying two source entries is asserting a standard
it does not demonstrate.


---

## 2. Environment and epistemic posture

**Environment:** `Tamil Retrofuture`. **Posture — the visitor's relation to the knowledge:** *known against an official account*. **`Avoid` — the failure this posture invites:** *"No kitsch, fake Tamil or neon overload"*.

The workbook's own function and effect cells for this environment: function *"Counter-history, public energy, learning"*, desired effect *"Spunky cultural memory"*, palette role *"Aubergine, magenta, orange, cyan"* (`environment-map.csv`, `INHERITED-UNVERIFIED`).


### Modes available in this posture

| Posture | Source | Atlas | Investigation | Field | Classroom |
|---|---|---|---|---|---|
| Tamil Retrofuture | mandatory | available | mandatory | available | available |

*(Framework §1.7.)*


### Derivation

**Derived posture: underivable today.** §1.5 derives a posture from the
exhibit's Claim Objects and its Absence records, in seven precedence steps. This
page has neither: no Claim Object exists for any proposition on it, and no
absence on it has been typed under constitution §6. Derivation therefore returns
nothing — not `Reading Room`, which is rule 7's residual and would be a false
output, since rule 7 fires on a claim set that has been examined and did not
match rules 1–6.

**Assigned posture: Tamil Retrofuture, editorially, by the workbook.** That assignment is
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


**Investigation Mode is mandatory here.** §1.7 makes PROVE IT mandatory in Tamil
Retrofuture, and §1.7's own rationale says why: this is one of the three postures
*"where the institution is arguing against something"*, and PROVE IT is *"the
mechanism that keeps the argument falsifiable rather than rhetorical."* A foyer
whose claim is *"evidence, and what it will not support"* is the exact case. This
converts a design feature into a launch dependency: **`enter` cannot launch in
this posture before PROVE IT (§9) exists.**


---

## 3. The evidence it rests on

**No register row in this repository names this page.** A scan of all 14 registers in `03-REGISTERS/` carrying a `supports_page` column returns zero rows for `enter` (`04-AUDITS/mvp-fifteen-briefs-build.py`, `scan_supports_page`). Under `CLAUDE.md`'s register format, `supports_page` is what ties a claim to the page it feeds — so on the repository's own accounting, this page is supported by nothing.


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
| `IH-057` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L158` | Correction C-37: the live site gives three atlas counts — **140 on Enter**, 158 on Explore, 175 in the page title. This page is one of the three disagreeing surfaces, and the one a visitor meets first. |
| `IH-250` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L474` | Contradiction X-01, of which C-37 is a part: six figures across the records. Resolution path: extract the dataset, count, generate every stated figure from it; until then no document prints a count. |
| `IH-052` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L146` | Correction C-32: `enter.html` referenced `RIGVEDA_corpus_analysis.md` and `MELUHHA_TO_KEEZHADI_synthesis.md`, both absent from the packaged archive. The fix is recorded as made in the zip and **not confirmed on the deployed site** (work item 5). |
| `IH-201` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L382` | The live check, 31 Aug: those two references return 404 and `/artifact-atlas` returns no text to a fetcher. The foyer's evidence links are the ones that were broken. |
| `IH-183` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L328` | Superseded row S-10: four successive MVP shapes, and the handoff records that **none** was adopted by the owner (X-10, work item 12). A foyer orients a visitor to a release whose shape is not decided. |


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
| Required asset set | opening atmosphere asset; claim-specific diagram; source facsimile; social card |
| Documentary standard | Verified source, licence, credit, alt text, claim supported, date/place, manipulation disclosure |
| Priority | `MVP` |
| Source / commission route | To research |
| Status | `Needed` |


**How this class should be derived instead.** Framework §1.6.3(a) replaces genre-driven asset classes with a mapping from the exhibit's **evidence-class composition** — the constitution's step 4 inventory. The workbook derived this row from the page's `Type`, a 29-value vocabulary with 17 singletons that `SCHEMA.md` §4 finds *"too sparse to do reliably"* the production-planning work it is doing. Under §1.6.3(a) a page with no recorded evidence classes yields **no** production class, which is the correct output and is this page's actual state.


`claim-specific diagram` is embargoed under §3.12 while the page's claims sit at
`INHERITED-UNVERIFIED`. `source facsimile` is buildable in principle — a foyer
about evidence is the natural place for one — but the two source entries the page
has are not yet identified in any register here.


---

## 5. What would have to be true before it can launch

Every page in the release carries the shared gates in
`06-BRIEFS/mvp-fifteen/README.md` §4 — the workbook's seven release gates, its
five *Not completed* publication gates, and the ten framework gates F1–F10. They
are not repeated here. What follows is what this page needs **beyond** them.

1. PROVE IT exists and is reachable from this page (§1.7, mandatory in Tamil Retrofuture).
2. No atlas count appears on it (`IH-057`, `IH-250`, D-034).
3. The two 404s are confirmed fixed **on the build that is actually being released** — which is blocked on `DECISIONS-NEEDED.md` **D-033**, since the repository cannot presently say which build is authoritative.
4. The page's promise about what evidence *will not* support is backed by typed absences under constitution §6, not by a rhetorical gesture. None is typed today.
5. Its 113 inbound links are re-pointed or preserved deliberately: with 14 of the 96 pages in the release, most of what links here will not exist at launch. That is a navigation decision nobody has recorded.


---

## 6. What unit of work would verify it

**MVP-U2 — foyer audit against the released build.** Confirm the C-32 fix live,
confirm which of the 113 inbound links survive into the release, and remove or
source every count. **Blocked twice over.** The audited archive `veli-site(3).zip`
is not in this repository and has no row in `02-SOURCES/access-ledger.csv`, so
the pages cannot be read here; and the deployed site is not reachable — the
session's latest egress characterisation (`SRC-052`) records only `github.com`
and `raw.githubusercontent.com` as reachable, with `SRC-081` to `SRC-083`
recording further hosts blocked on re-probe at 2026-09-07T15:10Z.

**Therefore a `HOLD` row is owed** in `05-HOLDS/`, naming the archive and the
deployed build as the unreachable sources, rather than a substitute audit run off
the workbook's own summary of pages nobody here has opened. D-033 is the
decision that unblocks it.


---

*Brief written 2026-09-08. Nothing in it is public copy. Nothing in it promotes a claim: promotion requires a retrieval event logged in `02-SOURCES/access-ledger.csv`, and this unit performed none.*
