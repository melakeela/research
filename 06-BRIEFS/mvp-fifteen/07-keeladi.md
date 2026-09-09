# `keeladi` — page brief

**Page:** *Keeladi: A Literate Tamil City from 6th Century BCE* · MVP rank **7** of 15 · `Living Tiṇai` · Decision `Keep` · Risk `Low`

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

**QUESTION.** What was excavated at Keeladi, what dates the deposits and the inscribed material, and what happened administratively to the excavation and its reports?

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

1,164 words, type `place`, 14 estimated source entries, 0 external links, 1
table, 8 inbound links. Decision `Keep`, Risk `Low`. H1: *"Keeladi: a literate
southern city — and an excavation the state could not leave alone."* The title
asserts a date: *"A Literate Tamil City from 6th Century BCE."*

Two arguments run in one page, and they belong to different evidence classes and
different verification routes. One is archaeological and epigraphic — deposits,
dates, inscribed sherds. The other is institutional — transfers, reports,
rework requests, evaluations. The second names a state body and asserts
interference.



---

## 2. Environment and epistemic posture

**Environment:** `Living Tiṇai`. **Posture — the visitor's relation to the knowledge:** *known through place and material*. **`Avoid` — the failure this posture invites:** *"No generic landscape decoration"*.

The workbook's own function and effect cells for this environment: function *"Ecology, place, material practice"*, desired effect *"Land as evidence"*, palette role *"Dark green, river blue, clay, sage"* (`environment-map.csv`, `INHERITED-UNVERIFIED`).


### Modes available in this posture

| Posture | Source | Atlas | Investigation | Field | Classroom |
|---|---|---|---|---|---|
| Living Tiṇai | mandatory | available | available | mandatory | available |

*(Framework §1.7.)*


### Derivation

**Derived posture: underivable today.** §1.5 derives a posture from the
exhibit's Claim Objects and its Absence records, in seven precedence steps. This
page has neither: no Claim Object exists for any proposition on it, and no
absence on it has been typed under constitution §6. Derivation therefore returns
nothing — not `Reading Room`, which is rule 7's residual and would be a false
output, since rule 7 fires on a claim set that has been examined and did not
match rules 1–6.

**Assigned posture: Living Tiṇai, editorially, by the workbook.** That assignment is
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


**Field Mode is mandatory in Living Tiṇai** (§1.7) — and here it collides with an
open owner decision. `09-DECISIONS/OWNER-DECISIONS.csv` **D-006** asks whether
Keezhadi or an inscription is the children's pilot. So the posture's mandatory
mode, for this page, is the subject of a decision nobody has taken. Recorded, not
resolved; see the same tension under `tinai` §2.

**The institutional half of the page does not sit in this posture at all.** An
excavation *"the state could not leave alone"* is a claim about withheld or
controlled knowledge, which is Extraction / Collection — §1.5's derivation rule 1
and rule 6 both reach for it before rule 5 (place/material dominance) fires.
Whether the page is one exhibit in two postures or two exhibits is an editorial
question the Editorial Register does not yet exist to hold.


---

## 3. The evidence it rests on

**No register row in this repository names this page.** A scan of all 15 registers in `03-REGISTERS/` carrying a `supports_page` column returns zero rows for `keeladi` (`04-AUDITS/mvp-fifteen-briefs-build.py`, `scan_supports_page`). Under `CLAUDE.md`'s register format, `supports_page` is what ties a claim to the page it feeds — so on the repository's own accounting, this page is supported by nothing.


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
| `IH-113` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L243` | Provisional finding P-05 in the handoff, from secondary sources: *5,500 artefacts, then transfer, then a 982-page report in January 2023, then a May 2025 rework request, then a 114-page evaluation* — with the handoff's own caveat, **'pin each step'**. One artefact count and four administrative events — a transfer, a report, a rework request, an evaluation — none pinned to an issuing body and a document. |
| `IH-061` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L166` | Correction C-41: among the sentences banned from the prospectus is *'any Keeladi claim beyond a specific inscribed mark'*, alongside *'any number not derivable from the repository'*. The project has already written itself a rule about how far Keeladi claims may go. |
| `IH-215` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L406` | Work item 44: contacting Dr. G. Sundar of the Roja Muthiah Research Library, as a bridge to UTSC Digital Tamil Studies and the TNSDA Tamil-Brahmi graffiti project, is *'the most important single verification task in the file'* — and the handoff records that **nothing has been sent to any of the nine outreach roles**. |
| `IH-212` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L402` | The Dig engine, a PWA over Keezhadi with an on-device Field Bag, plus a Children's Council and a Living Worlds Council with veto over misrepresentation and false continuity — T5 concepts, **none recorded as adopted by the owner**. |


`IH-061` deserves emphasis because it is a rule the project wrote for itself and
this page is where it applies. If no Keeladi claim may go beyond a specific
inscribed mark in a funding prospectus, the standard on a public exhibit page
cannot be looser. *"A literate Tamil city from 6th century BCE"* is a claim about
a date and a claim about literacy, and the second is carried by the inscribed
material the rule points at.

**The preferred-counter-narrative test, run on this page.** Keeladi carries the
strongest Tamil-nationalist valence of the fifteen, and both halves of the page
are congenial to a position this project holds: an early literate southern city,
and a state that interfered with the excavation. That is a reason to press
harder, not softer. Three specific pressures follow.

*On the date.* An early date for southern literacy is the finding this project
would most like to be true, which is exactly the condition under which a
secondary-source chain gets accepted. `IH-113` is `PROVISIONAL` in the handoff
and `INHERITED-UNVERIFIED` here, and the handoff's own instruction is *pin each
step*. The correct posture is that the date is unestablished in this repository,
not that it is established and awaiting citation.

*On the interference narrative.* Four administrative events — a transfer, a
report, a rework request, an evaluation — are consistent with interference and
also consistent with ordinary bureaucratic process. `IH-113` supplies the
sequence, not the motive, and the page's H1 supplies the motive. That gap is the
page's largest unsupported step, and it is not a right-of-reply problem before it
is an evidence problem: the right of reply governs how a supported allegation is
published, not whether an unsupported one may be.

*On the direction of correction.* The inheritance contains one logged case where
a correction ran *towards* the canonical finding rather than away from it —
`IH-029`/R-09, where the handoff records that *"Claude's caution understated a
well-supported finding"*. It is cited here because the six-headline correction
record (`IH-051`) otherwise reads as a one-directional story about this project
overclaiming in its own favour, and a one-directional story about one's own bias
is itself a congenial thing to believe.


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
| Required asset set | site/landscape photography; material macro; ecological map; present-context image |
| Documentary standard | Verified source, licence, credit, alt text, claim supported, date/place, manipulation disclosure |
| Priority | `MVP` |
| Source / commission route | To research |
| Status | `Needed` |


**How this class should be derived instead.** Framework §1.6.3(a) replaces genre-driven asset classes with a mapping from the exhibit's **evidence-class composition** — the constitution's step 4 inventory. The workbook derived this row from the page's `Type`, a 29-value vocabulary with 17 singletons that `SCHEMA.md` §3 finds *"too sparse to do reliably"* the production-planning work it is doing. Under §1.6.3(a) a page with no recorded evidence classes yields **no** production class, which is the correct output and is this page's actual state.


**`site/landscape photography` and `present-context image` require physical
presence.** Framework §1.6.3(a) maps environmental and site-bound evidence to
*"site photography — physical presence required"*. There is no route to it from
this session, and none from this repository; it is a commissioning decision with
a travel budget behind it. `material macro` needs object access and therefore a
custody chain and a holder permission (§3.4).

This asset set is the one place in the fifteen where the workbook's schedule and
physical reality are furthest apart: four assets, all requiring someone to be in
Tamil Nadu with permission.


---

## 5. What would have to be true before it can launch

Every page in the release carries the shared gates in
`06-BRIEFS/mvp-fifteen/README.md` §4 — the workbook's seven release gates, its
five *Not completed* publication gates, and the ten framework gates F1–F10. They
are not repeated here. What follows is what this page needs **beyond** them.

1. The date in the title is carried by a claim with a stated basis — which deposits, which method, which report — or the title stops asserting it. `IH-113` rests on secondary sources and the handoff itself says to pin each step.
2. The literacy claim is tied to specific inscribed material with catalogue identifiers, per the project's own C-41 rule (`IH-061`).
3. Each of the four administrative events has an issuing body, a date and a document. Four events reported at second hand is a narrative, not a chronology.
4. The interference claim triggers the right-of-reply obligation (§11.3) against every named institution, and `09-DECISIONS/OWNER-DECISIONS.csv` **D-010** — which institutional claims may presently be published — is the governing open decision.
5. Field Mode resolved for this posture, and D-006 answered if the children's pilot is Keezhadi.
6. Site and object imagery is commissioned with rights, credit and a custody position, or the page ships without it.


---

## 6. What unit of work would verify it

**MVP-U7 — the Keeladi report chain.** Pin each of the five events in `IH-113` to
a document: the excavation reports and their authors, the 982-page report of
January 2023 and its issuing body, the transfer order, the May 2025 rework
request, the 114-page evaluation. Separately, obtain the dating basis for the
6th-century-BCE claim from the excavation reports rather than from press
coverage.

**Retrieval state: `NOT ACCESSIBLE` for the hosts probed, untested for the
rest — and the difference matters.** `SRC-081` to `SRC-083` record the
general-web hosts refused on re-probe at 2026-09-07T15:10Z, and `SRC-052`'s
`blocking_constraint` generalises from a sixteen-host probe list. **No probe of
an ASI, TNSDA or Indian publisher host is recorded anywhere in the ledger**, so
this brief does not assert that they are unreachable. Nor does it type the
absence, because the constitution §6 typology has **no code for "not
searched"** — `NOT RECOGNIZED` means evidence present but unidentifiable, and
using it for an unrun search would be worse than leaving the absence untyped,
since a wrongly typed absence stops looking like an open question.
`04-AUDITS/REAUDIT-QUEUE.csv` `RA-018` already records the gap in the typology.
What is stated instead is the fact: the search has not been run. `indianculture.gov.in` was recorded reachable at `SRC-027`
earlier the same day, and `SRC-080`'s own note states the governing principle:
*"A ledger row is a timestamped probe, not a standing property (D-042)."* The
two rows are therefore not reconcilable from this brief. **Probing the specific
hosts is step 1** of the unit, and its result is a ledger row either way.

**And one part escalates rather than blocks.** `IH-215` names the single most
important verification task in the inherited file as an outreach to a named
librarian, and records that nothing has been sent. Institutional access is one of
`CLAUDE.md`'s five escalation categories. That goes to the owner as an owner
action, not into a `HOLD` row — a hold records an unreachable source, and this
source is reachable by a person writing a letter.


---

*Brief written 2026-09-08, revised 2026-09-09. Nothing in it is public copy. Nothing in it promotes a claim: promotion requires a retrieval event logged in `02-SOURCES/access-ledger.csv`, and this unit performed none.*
