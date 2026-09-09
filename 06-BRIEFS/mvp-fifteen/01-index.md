# `index` — page brief

**Page:** *Veli: A Digital Museum of Ancient South Asia* · MVP rank **1** of 15 · `Nocturnal Veḷi` · Decision `Revise` · Risk `Medium`

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

**QUESTION.** What was taken out of the record of ancient South Asia, who took it out, and what does this institution actually hold in its place?

### Why the remaining six slots are empty

Step 14 draws public copy **from accepted claims**. This page has none: §3 below records that nothing bearing on it stands above `INHERITED-UNVERIFIED`. Drafting
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

The audited page is 861 words, type `threshold`, with **0 estimated source
entries, 0 external links, 0 tables and 1 inline SVG**, and **0 inbound links** —
the only page of the fifteen that nothing else on the site points at, which is
what a front door is. Its central public claim, as the workbook records it, is
*"Something was emptied out of this place. Here is what it held. A reproducible
museum of ancient South Asia, from Meluhha to Keezhadi."*

That is three claims in one strapline: an extraction claim (*something was
emptied out*), a holdings claim (*here is what it held*), and a method claim
(*reproducible*). The page carries no source section for any of them.


---

## 2. Environment and epistemic posture

**Environment:** `Nocturnal Veḷi`. **Posture — the visitor's relation to the knowledge:** *not yet known*. **`Avoid` — the failure this posture invites:** *"No fantasy portal or occult styling"*.

The workbook's own function and effect cells for this environment: function *"Threshold, deep time, unknowns"*, desired effect *"Vastness without menace"*, palette role *"Blue-black, moon-white, cyan, gold"* (`environment-map.csv`, `INHERITED-UNVERIFIED`).


### Modes available in this posture

| Posture | Source | Atlas | Investigation | Field | Classroom |
|---|---|---|---|---|---|
| Nocturnal Veḷi | mandatory | available | available | available | available |

*(Framework §1.7.)*


### Derivation

**Derived posture: underivable today.** §1.5 derives a posture from the
exhibit's Claim Objects and its Absence records, in seven precedence steps. This
page has neither: no Claim Object exists for any proposition on it, and no
absence on it has been typed under constitution §6. Derivation therefore returns
nothing — not `Reading Room`, which is rule 7's residual and would be a false
output, since rule 7 fires on a claim set that has been examined and did not
match rules 1–6.

**Assigned posture: Nocturnal Veḷi, editorially, by the workbook.** That assignment is
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


**A derivation tension, recorded and not resolved.** The page's central claim is
that something *was emptied out* — an extraction claim. §1.5's derivation runs in
precedence order, and rule 1 fires first: an exhibit whose central claims depend
on material whose access status is `NOT ACCESSIBLE`, or on a refused or
unanswered access request, derives to **Extraction / Collection**. Rule 3
(absence dominance → Nocturnal Veḷi) is three steps later. On its strapline
alone this page would derive to Extraction / Collection, not to the Nocturnal
Veḷi it is assigned.

This cannot be settled here, for a reason worth stating: derivation runs over
Claim Objects and typed absences, and the page has none, so what looks like a
conflict between a derived and an assigned posture is really two editorial
readings of one unsourced sentence. It is recorded so that when the strapline is
decomposed into claims (§6), the derivation is run rather than assumed. Note the
consequence if it did derive to Extraction / Collection: that posture's `Avoid`
is *"no spectacle or unsupported allegation"*, and *"something was emptied out of
this place"* with no source section is an allegation with no support attached.


---

## 3. The evidence it rests on

**No register row in this repository names this page.** A scan of all 15 registers in `03-REGISTERS/` carrying a `supports_page` column returns zero rows for `index` (`04-AUDITS/mvp-fifteen-briefs-build.py`, `scan_supports_page`). Under `CLAUDE.md`'s register format, `supports_page` is what ties a claim to the page it feeds — so on the repository's own accounting, this page is supported by nothing.


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
| `IH-174` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L319` | The strapline's own name. The handoff records *'Meluhha to Keezhadi'* as **superseded** by *Veli* (S-01). The threshold page still runs it. |
| `IH-258` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L482` | Contradiction X-09: the project's records disagree on the brand architecture across four successive positions, and the handoff's ruling is that every affected document *'should be read as carrying an unresolved name'*. The threshold is the document where a name is load-bearing. |
| `IH-250` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L474` | Contradiction X-01: six figures in circulation for the atlas site count. The handoff's resolution path is that *'until then no document prints a site count'*. A threshold that promises a museum must not size it. |
| `IH-018` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L67` | Correction C-06: no meta-commentary or process narration anywhere on the site; corrections go to a corrections log. Binding on threshold copy, which is where drafting residue survives longest. |
| `IH-002` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L10` | The handoff states of itself that no count in it was re-run against any corpus. Nothing quantitative on this page can be sourced to the inheritance. |


### Lowest status among them

**`INHERITED-UNVERIFIED`** — the status of every row above, and of every row that could be listed.


**On "lowest status".** `INHERITED-UNVERIFIED` is not the bottom rung of a
ladder. Framework §3.2: six of the seven statuses describe evidential standing
and one describes *where the assertion came from* — a prior model's summary of
its own conversation — so *"the interface must therefore never sort or
colour `INHERITED-UNVERIFIED` between `PROVISIONAL` and `HYPOTHESIS` as though
the statuses formed a single ladder."* The floor above is therefore stated by
rule rather than by sorting: a row carrying `INHERITED-UNVERIFIED` has had no
retrieval event behind it, so no set containing one stands above it. **Nothing bearing on this page stands above `INHERITED-UNVERIFIED`.**
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


Two of the four slots are unfillable as specified.

- **`claim-specific diagram`** — embargoed. Framework §3.12: *"a derived asset may
  not be commissioned or published while the claim it depicts is
  `INHERITED-UNVERIFIED` or `HOLD`."* Every claim on this page is at that floor.
- **`source facsimile`** — a facsimile is a reproduction of a source. The page has
  **0 source entries**. There is nothing for it to be a facsimile of until §6 runs.

`opening atmosphere asset` and `social card` are unblocked in principle, but a
social card carries the strapline, and the strapline is what `IH-174` and
`IH-258` put in question.


---

## 5. What would have to be true before it can launch

Every page in the release carries the shared gates in
`06-BRIEFS/mvp-fifteen/README.md` §4 — the workbook's seven release gates, its
five *Not completed* publication gates, and the ten framework gates F1–F10. They
are not repeated here. What follows is what this page needs **beyond** them.

1. The strapline's name is settled. `IH-174` records *'Meluhha to Keezhadi'* as superseded and `IH-258` records the brand architecture as contradicted; `09-DECISIONS/OWNER-DECISIONS.csv` **D-004** (what Veḷi principally is) is the open decision. This is an owner call, not a retrieval.
2. No site count, page count or holdings figure appears in threshold copy, per `IH-250`'s own resolution path and `DECISIONS-NEEDED.md` **D-034**.
3. The three claims in the strapline exist as three separate Claim Objects with computed statuses (§3.1–3.2), and the extraction claim in particular carries either evidence or a typed absence — not a mood.
4. The posture is derived and then assigned, with the override reason logged in the Editorial Register (§11.5), given the tension recorded in §2.
5. Source Mode is reachable from the threshold itself (§1.7, mandatory in every posture). A front door from which the visitor cannot reach the claims behind the promise is the one thing this page may not be.


---

## 6. What unit of work would verify it

**MVP-U1 — threshold claim decomposition.** No retrieval; entirely in-repository.
Decompose the strapline into Claim Objects, one per assertion; write each into a
register with `supports_page = index`; type the extraction claim's absence under
constitution §6 if it is to be argued from silence; record falsifiers. Then run
both §8 adversarial tests on the result — this is the page where the
prestige-bias test and the preferred-counter-narrative test bite hardest, because
a threshold is written to be affecting.

**What it cannot do.** It cannot promote anything. The decomposition produces
`HYPOTHESIS` rows at best, which is the correct output: the strapline's holdings
claim is a claim about this institution's own collection, and the institution has
no collection register yet. The naming question is not a research question at
all and returns to the owner as D-004.


---

*Brief written 2026-09-08, revised 2026-09-09. Nothing in it is public copy. Nothing in it promotes a claim: promotion requires a retrieval event logged in `02-SOURCES/access-ledger.csv`, and this unit performed none.*
