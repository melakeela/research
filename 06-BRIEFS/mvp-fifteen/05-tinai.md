# `tinai` — page brief

**Page:** *Tinai: The Tamil Poetics of Five Landscapes* · MVP rank **5** of 15 · `Living Tiṇai` · Decision `Keep` · Risk `Low`

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

**QUESTION.** What is tiṇai in the Tamil poetic tradition, in which texts is the five-landscape scheme actually set out, when were those texts composed and redacted, and what does the scheme claim about the relation between land and social life?

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

1,407 words, type `concept`, 19 estimated source entries and **2 external
links** — the only page of the fifteen with any live external link at all — 1
table, 8 inbound links. Decision `Keep`, Risk `Low`. H1: *"Tiṇai: a poetics that
thinks with the land."* The workbook's assessment: *"Defines a knowledge
framework rather than merely describing a historical topic."*

That assessment is the whole problem in one line. A page that defines a framework
the rest of the institution then uses is not one exhibit among fifteen; it is a
dependency of the others. `Living Tiṇai` is a posture named after it.


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


**Field Mode is mandatory in Living Tiṇai** (§1.7). The children's investigation
and the Field Bag (§10.4) are not an enhancement for this page; the matrix makes
them a condition of the posture. Nothing of the sort exists, and the closest
inherited artefact — the Dig engine (`IH-212`) — is recorded as *not adopted by
the owner*, with `09-DECISIONS/OWNER-DECISIONS.csv` **D-006** (Keezhadi or an
inscription as the children's pilot) still open.

Recorded, not resolved: either the matrix's *mandatory* is a launch condition,
in which case no Living Tiṇai page launches before a Field Mode exists, or it
describes the posture's finished state rather than its first release. The
framework does not distinguish the two, and this brief does not decide it. It
affects three of the fifteen (`tinai`, `keeladi`, `the-water-city`).


---

## 3. The evidence it rests on

**No register row in this repository names this page.** A scan of all 15 registers in `03-REGISTERS/` carrying a `supports_page` column returns zero rows for `tinai` (`04-AUDITS/mvp-fifteen-briefs-build.py`, `scan_supports_page`). Under `CLAUDE.md`'s register format, `supports_page` is what ties a claim to the page it feeds — so on the repository's own accounting, this page is supported by nothing.


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
| `IH-314` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L552` | Work item 46: *tinai* is explicitly among the terms for which **Tamil-dictionary and native-speaker confirmation is owed**, alongside *mela/kila, suvadu, adukku, nokku, navalam* and *porul*. The word this page defines is on the list of words the project records as not yet checked. |
| `IH-176` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L321` | Superseded row S-03: *TINAI* is also a component of the three-word brand system (VELI / TINAI / MELAKEELA-as-mode), itself superseded the following day. The term is simultaneously an analytic category and a product name. |
| `IH-248` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L462` | Section 8 HELD register: *Sangam, Tolkappiyam, Tevaram, the Pali canon, the Asokan edicts, the Saunaka Atharvaveda and a clean Chandogya* — recorded as a load-bearing source *'currently reached via NOT OBTAINED / NOT FOUND'*, carrying *'Everything Tamil, Pali and Prakrit that is not the Kural'*. Under the handoff's Rule 7 every claim resting on it is HELD. |


`IH-248` is the operative row. It names *Sangam* and *Tolkappiyam* among the
sources recorded as NOT OBTAINED / NOT FOUND — and those are the sources a
tiṇai page would have to rest on, since the page's own subject is a Tamil poetic
scheme. **Where exactly the scheme is set out is not something this brief can
state**: naming the chapter and the text that carries it would be a claim about
the contents of documents the same row records as unread here, which is the
error the page is suspected of. What can be said is the structural position: the
page defines a framework from primary texts that no one in this project's record
has read directly, which is a different and more serious position than having
read them and cited them thinly.


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


`claim-specific diagram` — the obvious one being a five-landscape diagram — is
embargoed under §3.12, and would in any case be the single asset most likely to
harden a poetic scheme into a map of real territory.

**The `Avoid` constraint is load-bearing for the `opening atmosphere asset`:**
*"no generic landscape decoration."* The five tiṇai are named for landscapes, and
a stock photograph of hills would fail the constraint and misstate the scheme in
one move — the tiṇai are poetic-situational categories, and illustrating them as
scenery is the reading the page exists to correct.


---

## 5. What would have to be true before it can launch

Every page in the release carries the shared gates in
`06-BRIEFS/mvp-fifteen/README.md` §4 — the workbook's seven release gates, its
five *Not completed* publication gates, and the ten framework gates F1–F10. They
are not repeated here. What follows is what this page needs **beyond** them.

1. The Tolkāppiyam *Poruḷatikāram* passages that set out the scheme are read in a named edition with exact locators, or the page states that they have not been and carries no claim about what the scheme says.
2. Chronology is established before interpretation (method step 2): composition, redaction, commentarial layer and modern interpretation of the tiṇai scheme are four different dates, and the commentarial tradition is where much of the systematisation lives.
3. A Translation Block for *tiṇai* itself (constitution §7), with the semantic range across 'landscape', 'class', 'genre', 'situation' — and the interpretive consequence of choosing among them, since the page's title takes one.
4. The brand use and the analytic use of the word are separated on the page, per `IH-176`/`IH-258`. A reader must not have to work out whether *tiṇai* is being used as a Tamil poetic term or as this institution's product vocabulary.
5. Field Mode resolved for this posture (see §2), and D-006 answered if the children's pilot is where it comes from.


---

## 6. What unit of work would verify it

**MVP-U5 — the tiṇai primary-source pass.** Retrieve a named edition of the
Tolkāppiyam *Poruḷatikāram*, locate the tiṇai chapters, record the scheme with
exact locators, and separate the text's own statements from the commentators'.

**Retrieval state: the likely hosts are refused, the git lane is untested.**
`SRC-083` records `sacred-texts.com` and `wisdomlib.org` refused at
2026-09-07T15:10Z, `SRC-080` GRETIL, `SRC-081` the Internet Archive, `SRC-082`
TITUS. Whether a citable edition is served over the still-open git lane
(`SRC-058`) is **untested**, and testing it is step 1 of the unit — so this
brief does not state that the text is unreachable, only that every host probed
so far has refused. A `05-HOLDS/` row is owed once that search has been run and
failed, naming the edition and what it would settle.


---

*Brief written 2026-09-08, revised 2026-09-09. Nothing in it is public copy. Nothing in it promotes a claim: promotion requires a retrieval event logged in `02-SOURCES/access-ledger.csv`, and this unit performed none.*
