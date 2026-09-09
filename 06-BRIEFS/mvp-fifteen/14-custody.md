# `custody` — page brief

**Page:** *Manuscript Custody: Who Held the Texts and Who Was Kept Out* · MVP rank **14** of 15 · `Extraction / Collection` · Decision `Keep` · Risk `Medium`

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

**QUESTION.** Who physically held which manuscript collections, on what terms was access granted or refused and to whom, and what is the present custody and access status of each?

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

1,375 words, type `collection-investigation`, **7 estimated source entries**, 0
external links, 1 table, 55 inbound links. Source state: *limited bibliography*.
Decision `Keep`, Risk `Medium`. H1: *"Every text was kept by someone with
something at stake."* The workbook's assessment: *"Supports the
custody/extraction critique, but **every institutional implication must be
documented**."*

Seven source entries against a claim quantified as *every*.



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


**The `Avoid` is the governing constraint and it is unusually specific:** *"no
spectacle or unsupported allegation."* An institutional-critique page with seven
source entries and a universal quantifier in its headline is on the wrong side of
the second half. §1.2's C-3 makes the point structurally — custody *invites*
unsupported allegation whichever object is in the case.

**Field Mode is forbidden** (§1.7, §10.4.6): *"A child may read a custody record;
a child may not be handed 'decide whether this object was looted' as a Field Bag
task."* **Investigation Mode is mandatory** — this is one of the three
argue-against postures.

**Three open owner decisions govern this page's core mechanism**, and none is a
research question: **D-025** (are refused and unanswered obligations published
individually, in aggregate, or only with prior notice), `OWNER-DECISIONS.csv`
**D-010** (which institutional claims may presently be published), and **D-016**
(may Reconnection surfaces publish before any community-led work exists).


---

## 3. The evidence it rests on

**No register row in this repository names this page.** A scan of all 15 registers in `03-REGISTERS/` carrying a `supports_page` column returns zero rows for `custody` (`04-AUDITS/mvp-fifteen-briefs-build.py`, `scan_supports_page`). Under `CLAUDE.md`'s register format, `supports_page` is what ties a claim to the page it feeds — so on the repository's own accounting, this page is supported by nothing.


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
| `IH-215` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L406` | Work item 44: contacting Dr. G. Sundar of the Roja Muthiah Research Library — a bridge to UTSC Digital Tamil Studies and the TNSDA Tamil-Brahmi graffiti project — is *'the most important single verification task in the file'*, and **nothing has been sent to any of the nine outreach roles**. The page about custody has had no contact with any custodian. |
| `IH-260` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L484` | Contradiction X-11: the records disagree on the ingestion layer — one Veli Collections layer normalising ten museums, against T4's explicit deferral of multi-museum ingestion. Both are Claude-origin and *'the owner has decided neither'*. |
| `IH-039` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L107` | The owner's request for coverage of the Gāndhārī scrolls as the oldest manuscripts was only partially built and is recorded as **OPEN** content. |


**No register row bears on this page's claims**, and the three rows above are
about the project's own unfinished business rather than about any manuscript.
That is the position to state plainly: the custody page rests on nothing this
repository holds.

**And it is load-bearing for the framework's seventh posture.** §1.6.2 resolves
the empty Reconnection environment by making it a register-backed posture that
becomes non-empty *"on the day the institution publishes its first custody chain,
its first refused access request or its first consent grant."* This page is where
the first custody chain would come from. Its `access-status evidence` asset is
that surface. So `custody` is not one exhibit among fifteen — it is the page that
determines whether the institution has seven postures or six in practice.


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
| Required asset set | collection record; accession/custody document; object image rights; institutional correspondence; access-status evidence |
| Documentary standard | Verified source, licence, credit, alt text, claim supported, date/place, manipulation disclosure |
| Priority | `MVP` |
| Source / commission route | To research |
| Status | `Needed` |


**How this class should be derived instead.** Framework §1.6.3(a) replaces genre-driven asset classes with a mapping from the exhibit's **evidence-class composition** — the constitution's step 4 inventory. The workbook derived this row from the page's `Type`, a 29-value vocabulary with 17 singletons that `SCHEMA.md` §3 finds *"too sparse to do reliably"* the production-planning work it is doing. Under §1.6.3(a) a page with no recorded evidence classes yields **no** production class, which is the correct output and is this page's actual state.


**This asset set cannot be filled at all today, and one slot is impossible by
construction.** `institutional correspondence` presumes correspondence exists;
`IH-215` records that nothing has been sent to any of the nine outreach roles.
`collection record` and `accession/custody document` require institutional
access; `object image rights` requires a holder's permission, which requires the
same access; `access-status evidence` is the one slot that can be populated
immediately and in the institution's own voice, because a documented refusal or
an unanswered letter *is* access-status evidence — and §1.6.2 requires that the
not-yet-repaired row be published, or the environment becomes a
self-congratulation surface.

The sequence is therefore: write the letters, log every outcome including
silence, and the asset set starts filling itself.


---

## 5. What would have to be true before it can launch

Every page in the release carries the shared gates in
`06-BRIEFS/mvp-fifteen/README.md` §4 — the workbook's seven release gates, its
five *Not completed* publication gates, and the ten framework gates F1–F10. They
are not repeated here. What follows is what this page needs **beyond** them.

1. The Institutional Obligations Register (§11.1) exists, including its negative rows — refused requests, unanswered letters, consultations not held.
2. The right-of-reply mechanism (§11.3) is live before any named institution is criticised, with its own identifier scheme so a reply is published beside the criticism.
3. **D-025**, **D-010** and **D-016** are answered. Each of the three independently blocks part of what this page does.
4. At least one custody chain is documented end to end (§3.4) — who made it, who held it, who holds it now, on what terms.
5. *'Every text'* is either evidenced as a universal or narrowed to the collections actually documented. Seven source entries do not carry *every*.
6. The overlap cluster *Institutional authority* — `indology`, `coverage`, `who-writes-the-textbook`, `what-the-children-are-taught`, `the-archive`, `custody` — is addressed: the workbook recommends one curated exhibit with claim-level documents and a right-of-reply field, and only two of the six are in the release.


---

## 6. What unit of work would verify it

**MVP-U14 — the first custody chain, and the register behind it.** Two halves
with different blockers.

*In-repository, executable now:* create the Institutional Obligations Register
(§11.1) with its schema, including negative rows; create the Consent Register
(§11.4) and the Community Authority Register (§11.2) as empty, schema'd files, so
the fourth axis `SCHEMA.md` §7 names has somewhere to be written. This is
structure, not evidence, and it must not be described as progress on the page's
claims.

*Requiring outreach, and therefore escalating rather than blocking:* `IH-215`'s
nine outreach roles. **Institutional access is one of `CLAUDE.md`'s five
escalation categories**, so this goes to the owner as an owner action. It is not
a `HOLD` — a hold records a source that cannot be reached, and these custodians
can be reached by someone writing to them. Every outcome, including no reply, is
a row in the Obligations Register and is itself the page's evidence.


---

*Brief written 2026-09-08, revised 2026-09-09. Nothing in it is public copy. Nothing in it promotes a claim: promotion requires a retrieval event logged in `02-SOURCES/access-ledger.csv`, and this unit performed none.*
