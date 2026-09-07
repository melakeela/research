# Museum Framework — the institution as a system

**Artefact class:** specification. Not research, not site code, not a page brief.
**Constitutional basis:** `00-CONTROLLER/METHODOLOGY-CONSTITUTION.md` §12 (product
and institutional specification stage) and §13 (language-movement Artifact Atlas).
**Directory:** `13-PRODUCT-ARCHITECTURE/`, per constitution §15's expansion scheme.
**Status of every design claim in this file:** `HYPOTHESIS`, except where a
statement is a restatement of §12/§13 (which is a constitutional instruction, not
an evidentiary claim) or a restatement of the curatorial audit (which is
`INHERITED-UNVERIFIED`).

---

## 0. What this document is, and the three rules it runs under

### 0.1 What it specifies

The institution as a **system**: the objects it stores, the relations between
them, the routes a visitor takes into them, the modes it displays them in, and
the governance that decides what may appear at all. It specifies behaviour and
data, not markup. It contains no HTML, no CSS and no JavaScript, per §12's
closing line — *"Do not create production code"* — and per `CLAUDE.md`'s standing
prohibition on writing site code in this repository.

### 0.2 The three rules it runs under

**Rule S-1 — No specification may cite a claim above its register status.**
From `CONTROLLER-RECONCILIATION.md` C-5. Everything this document takes from
`01-INHERITED/curatorial-audit-v1.1/` is `INHERITED-UNVERIFIED` and is marked as
such at the point of use. A design that depends on a number is a design that
depends on that number's status: the Atlas cannot ship a site count in a title
while the count sits in a contradiction row (`03-REGISTERS/inherited-claims.csv`
`IH-250`, X-01; `DECISIONS-NEEDED.md` D-006).

**Rule S-2 — Where §12 or §13 leaves a choice the owner has not made, the choice
is recorded, not taken.** New entries are written to `DECISIONS-NEEDED.md` as
D-015 onward. This document proposes; it does not adopt. Where it recommends,
the recommendation is labelled as such and the alternative is stated at equal
seriousness. Where §14 has already reserved a decision, the existing
`09-DECISIONS/OWNER-DECISIONS.csv` row is cited rather than duplicated.

**Rule S-3 — Specification does not promote.** Nothing here is a finding. Naming
an object model does not create the objects; naming a register does not populate
it; naming an environment does not build a page. Constitution §15: *"Do not claim
that research specifications are implemented pages."*

### 0.3 What it deliberately does not do

- It does not resolve the workbook's editorial decisions. No page is kept,
  revised, held, split or merged here.
- It does not settle Veḷi's principal meaning (`OWNER-DECISIONS.csv` D-004),
  whether WATER is the first Living World (D-005), the children's pilot (D-006),
  the order of the first three builds (D-007), Release 1 scope (D-008), the
  merges (D-009), publishable institutional claims (D-010), or the deferred set
  (D-011). Those are §14 reservations and remain open.
- It does not specify visual design. The palette roles quoted from the
  Environment Map are quoted, not extended. The visual handoff is scoped in §12
  of this document as a *contract*, not as a design.

### 0.4 Where it sits against `OWNER-DECISIONS.csv` D-012

D-012 asks whether product and institutional specification belongs in this
repository (proposed `07-PRODUCT-SPECS/`) or in `melakeela/site`. The task that
produced this file placed it at `13-PRODUCT-ARCHITECTURE/museum-framework.md`,
which is the constitution §15 name. That answers the location question **for this
artefact**. It does not answer D-012's general form — whether the whole class of
specification work lives here — and D-012 stays open. If the owner later answers
"in `melakeela/site`", this file moves; nothing in it depends on the path.

---

## 1. The organising thesis: environments are epistemic postures

### 1.1 The thesis as inherited

`01-INHERITED/curatorial-audit-v1.1/environment-map.csv`, second line:

> *"Themes change with the visitor's relationship to knowledge; the institutional
> shell remains stable."*

Status: `INHERITED-UNVERIFIED`. It is a design proposition, not a historical
claim, so "verification" in the evidentiary sense does not apply to it; what
applies is whether the rest of the system can be built on it. This document
takes it as the organising axis because it is the only organising axis the
project has articulated, and because it does work no subject taxonomy can do.

The seven environments are not Prehistory / Language / Caste / Religion. They are
seven **relationships between a visitor and a body of knowledge**:

| Environment | Posture — the visitor's relation to the knowledge | `Avoid` (the failure the posture invites) |
|---|---|---|
| Nocturnal Veḷi | *not yet known* | No fantasy portal or occult styling |
| Living Signal Field | *known by relation* | No gaming HUD or arbitrary links |
| Tamil Retrofuture | *known against an official account* | No kitsch, fake Tamil or neon overload |
| Living Tiṇai | *known through place and material* | No generic landscape decoration |
| Reading Room | *known by argument from sources* | No visual fatigue or luxury minimalism |
| Extraction / Collection | *known but withheld* | No spectacle or unsupported allegation |
| Reconnection | *knowable again* | Digitization is not restitution |

### 1.2 Why the system is built on posture rather than subject

Four consequences, all of them structural rather than decorative.

**C-1. Posture survives revision; subject does not.** A page reclassified from
"Language" to "Genetics" has changed what it is about. A page moved from
Nocturnal Veḷi to Living Signal Field has changed only what the institution can
presently say about it — the content need not change at all. The schema
assessment states this: *"because environments are postures rather than topics, a
page can move between them without its content changing. Assignment is an
editorial act, and it is revisable."* A research programme that expects to
overturn its own conclusions (constitution §2: the record must stay capable of
contradicting *"your own previous answer"*) cannot be filed by subject, because
the subject headings encode the conclusions.

**C-2. Posture makes evidence status legible without a badge.** The evidence
vocabulary in `CLAUDE.md` — `VERIFIED`, `PROVISIONAL`, `HYPOTHESIS`,
`INHERITED-UNVERIFIED`, `REJECTED`, `SUPERSEDED`, `HOLD` — is a property of
claims. Posture is the visitor-facing consequence of a claim set's status
distribution. An exhibit whose load-bearing claims are `HYPOTHESIS` and whose
absences are typed `NOT EXCAVATED` **is** Nocturnal Veḷi; that is what the
posture means. This is specified as a computed relationship in §1.5 below, not
as an editorial mood.

**C-3. Posture is where the `Avoid` constraints attach.** The schema assessment
calls the `Avoid` column *"the strongest part of the artefact"* and *"falsifiable
design constraints: for any published page you can state whether it violated
one."* Constraints attach to postures because each failure mode is invited by a
posture, not by a subject. Deep time invites occultism whether the subject is
astronomy or lithics. Custody invites unsupported allegation whether the object
is a seal or a manuscript.

**C-4. Posture forces the institution to own its silences.** Six postures
describe kinds of knowing. One — Extraction / Collection — describes knowledge
that exists and is withheld from the people it came from. One — Reconnection —
describes repair. A subject taxonomy has no slot for either; it files the
custody of a Chola bronze under "Chola bronzes."

### 1.3 What posture is *not* permitted to do

Posture is a display and navigation axis. It has no evidentiary authority.

- Posture **must not** set or influence a claim's status. A Nocturnal Veḷi
  exhibit does not get a lower evidential bar because it is about unknowns; it
  gets a stricter negative-evidence discipline (constitution §6), because that is
  what its posture is made of.
- Posture **must not** substitute for the negative-evidence typing. "This is
  Nocturnal Veḷi" is not a reason; `NOT EXCAVATED` with a stated survey coverage
  is a reason.
- Posture **must not** be inferred from tone. It is derived from the claim set
  (§1.5) and then confirmed or overridden editorially, with the override logged.

### 1.4 The fourth axis the workbook never named

`SCHEMA.md` §7 separates three judgement axes — **editorial**, **evidentiary**,
**production** — and identifies a fourth that the workbook *"keeps noticing and
never names"*: the **institutional/ethical** axis (right-of-reply discipline,
community consultation, "digitization is not restitution", consent for
pronunciation recordings). It has no vocabulary, no column and no register.

This framework names it and gives it a register. It is specified in §11 as the
**Institutional Obligations Register**, and it is the axis on which the
Reconnection posture stands. See §1.6.2 — the unnamed fourth axis and the empty
seventh posture are the same hole, and closing one closes the other.

### 1.5 Posture derivation — the computed default

Every exhibit carries a **posture assignment** with three parts: a *derived*
posture, an *assigned* posture, and, where they differ, a logged override reason.
Derivation runs over the exhibit's Claim Objects (§3) and its Absence records
(§3.7).

Derivation inputs, in precedence order:

1. **Withheld-access flag.** If the exhibit's central claims depend on material
   whose access status is `NOT ACCESSIBLE`, or whose Institutional Obligations
   Register row records a refused or unanswered access request → **Extraction /
   Collection**.
2. **Repair state.** If the exhibit's governing relationship is a community
   authority record, a consent grant, a withdrawal, a right-of-reply exchange or
   a returned/reopened access → **Reconnection**. (§1.6.2.)
3. **Absence dominance.** If the majority of the exhibit's load-bearing
   propositions resolve to typed absences rather than to positive claims →
   **Nocturnal Veḷi**.
4. **Relation dominance.** If the exhibit's substance is Relationship Objects
   (§4) rather than Claim Objects — comparison, movement, correspondence →
   **Living Signal Field**.
5. **Place/material dominance.** If the majority of supporting evidence is
   material, environmental or site-bound, and the exhibit is anchored to a Place
   → **Living Tiṇai**.
6. **Counter-account.** If the exhibit's principal Relationship Objects are of
   type `contradicts` or `supersedes` against a named dominant account, and the
   asymmetry audit (§11.2) records an archival power differential →
   **Tamil Retrofuture**.
7. **Otherwise → Reading Room.** See §1.6.1 for why this residual is a defect
   in the inherited encoding and how the framework handles it.

Derivation is advisory. The assigned posture is editorial and is written to the
Editorial Register (§11.5) with `derived_posture`, `assigned_posture`,
`override_reason`, `decided_by`, `decided_date`. An override with an empty reason
is invalid. This is the register the repository currently lacks: `SCHEMA.md` §7
records that *"nothing in `03-REGISTERS/` records a publication decision, an
environment assignment, or a duplication finding."*

### 1.6 The three inconsistencies

`SCHEMA.md` §3 finds three ways in which the environment scheme is inconsistent
with the page inventory that uses it. All three are `INHERITED-UNVERIFIED`
findings about a frozen 2026-09-01 build. All three are load-bearing for this
framework, because the framework is built on the scheme they criticise.

---

#### 1.6.1 Inconsistency 1 — Reading Room is both a peer and the substrate

**The finding.** Reading Room is the primary environment for 34 of 96 pages —
more than twice the next — *and* the secondary environment for all 96, including
the 34 where it is already primary. A constant across every row carries no
information. The assessment's conclusion: *"34 pages are Reading Room because the
audit had nothing more specific to say about them, and the residual category is
the largest one."*

**Diagnosis.** Two different things are wearing one name.

- **Reading Room as posture** — *known by argument from sources* — is a real,
  distinguishable relationship to knowledge. It describes an exhibit whose
  substance is the argument itself: methods pages, historiography, the ledger.
- **Reading Room as substrate** — the state every exhibit falls back to when the
  visitor stops looking and starts checking — is not a posture at all. It is a
  **display mode** available on every object in the institution, in every
  environment.

Encoding them as one value forces a false choice and produces a residual bucket.

**Framework resolution.** Split the name into two mechanisms.

1. **`SOURCE MODE`** — a universal display state, not an environment. Any
   exhibit, atlas layer, PROVE IT run, WATER world or children's investigation
   can be switched into Source Mode. In Source Mode the surface presents claim
   rows, statuses, locators, retrieval dates, source genealogy (constitution
   Step 5), archive audit (Step 6), absences with their types, falsifiers
   (Step 12), and the revision history of every claim shown. Source Mode is the
   primary-source viewer and evidence search (§6, §7) reached from wherever the
   visitor already is. It is the institution's stable shell — which is precisely
   what the Environment Map's thesis line claims: *"the institutional shell
   remains stable."*
2. **Reading Room as posture** retains its seat among the seven, but only for
   exhibits whose *content* is argument from sources. An exhibit does not become
   Reading Room by being unclassifiable. Derivation rule 7 (§1.5) makes Reading
   Room the residual **only for derivation**, and every residual assignment is
   flagged `derived_residual = true` in the Editorial Register so the size of the
   unclassified set is visible rather than laundered into a posture count.

**Consequence for the inherited data.** Under this resolution the `Secondary
environment` column (constant `Reading Room`, 96/96) is not a value at all — it
is the statement "Source Mode exists", made once. It should be retired as a
column rather than migrated. The 34 primary assignments must be re-derived, and
the residual flag will show how many of them were genuine.

**What is left to the owner.** Whether Reading Room remains a seventh peer
posture at all, or is demoted entirely to Source Mode leaving six postures, is an
editorial judgement about the institution's self-description, not a derivable
fact. Recorded as **D-015**.

---

#### 1.6.2 Inconsistency 2 — Reconnection has one page, and the workbook proposes to merge it away

**The finding.** The Environment Map describes Reconnection's prototype as
*"Future community-led work"* — an admission it is unbuilt. One page is assigned
to it, `criminalised-today`, whose Decision is `Merge` (into `criminalised`,
Overlap cluster 2). Executing the workbook's own recommendation empties the
environment. The assessment: *"The seventh posture — the only one describing
repair — has no surface. This is the one place where the environment scheme makes
a claim about the institution that the page inventory does not support."*

**Diagnosis.** This is not a page-count problem and it will not be fixed by
keeping `criminalised-today` unmerged. Reconnection is empty because the
institution has been looking for its surface in the wrong class of object.

The other six postures are satisfied by **exhibits** — essays, atlases, maps,
investigations. Reconnection is not a posture about a *subject the institution
can research*. It is a posture about the institution's own **relations**: to
communities whose material and speech it holds or represents, to the holders of
objects it wants access to, to people who have asked for a right of reply, to
consent that has been given and can be withdrawn. Those relations are records,
not essays. The institution has been generating them all along —
`environment-map.csv` "Digitization is not restitution", the Overlap cluster 9
"right-of-reply field", the Asset Register's *"pronunciation audio where
licensed"* hedge, `Method & Limits`'s "community consultation" under *Not
completed* — and has had nowhere to put any of them.

That nowhere is exactly the unnamed fourth axis of `SCHEMA.md` §7. **The empty
seventh posture and the unnamed fourth axis are the same gap.** Reconnection's
surface is the visitor-facing face of the Institutional Obligations Register
(§11.1).

**Framework resolution.** Reconnection is specified as a **standing environment
backed by a register, not by an essay corpus.** Its surfaces are:

| Reconnection surface | Backed by | Specified in |
|---|---|---|
| **Access status of every held object** — who holds it, whether it can be seen, by whom, on what terms, and what was refused | UEO custody chain + Institutional Obligations Register | §3.4, §11.1 |
| **Right of reply** — a named institution or scholar criticised by an exhibit may respond; the response is published beside the criticism with its own identifier | Obligations Register, `right_of_reply` rows | §11.3 |
| **Consent record** — for every living-community contribution: what was given, by whom, for what use, for how long, and how it is withdrawn | Consent Register | §11.4 |
| **Withdrawal trail** — material withdrawn stays visibly withdrawn: the record that it existed and was withdrawn remains, the material does not | Consent Register + revision history | §11.4, §3.6 |
| **Community authority statements** — where a community holds authority over an interpretation, that authority is named, not absorbed into the institutional voice | Community Authority Register | §11.2 |
| **Correction ledger, public face** — every accepted correction challenge, its outcome and the claim it changed | Correction Register | §10.2 |
| **What has *not* been repaired** — refused requests, unanswered letters, unreturned objects, consultations not held | Obligations Register, negative rows | §11.1 |

**The `Avoid` constraint is the governing rule of the whole environment.**
*"Digitization is not restitution."* Reconnection therefore may not present any
of the above as repair achieved. A published access-status record is a record of
a state, including the state "still withheld". The last row in the table is not
optional garnish: without it the environment becomes a self-congratulation
surface, which is the failure mode its `Avoid` cell names.

**Why this is not merely relabelling.** Under this specification Reconnection is
non-empty on the day the institution publishes its first custody chain, its first
refused access request or its first consent grant — all of which are prerequisites
for other work anyway (`Asset Register` classes 4 and 5). It stops depending on
"future community-led work" existing before the posture has a surface. It also
stops the merge question from being load-bearing: whether `criminalised-today`
merges into `criminalised` is Overlap cluster 2's business and `OWNER-DECISIONS.csv`
D-009's, and under this resolution the merge no longer empties an environment.

**What is left to the owner.** Two things, both genuinely reserved.

- Whether Reconnection surfaces may be published *before* any community-led work
  or consultation exists — i.e. whether an institution may publish its own
  account of its obligations before the parties to those obligations have been
  consulted. Recorded as **D-016**. This is a living-community consent question,
  which `CLAUDE.md` routes to the owner.
- Whether the institution states a restitution position at all, and if so what.
  "Digitization is not restitution" forecloses one claim without asserting
  another. Recorded as **D-017**, cross-referenced to `OWNER-DECISIONS.csv` D-010
  (which institutional claims may presently be published).

---

#### 1.6.3 Inconsistency 3 — the `Type` vocabulary is not reconciled to the environment vocabulary

**The finding.** 29 `Type` values against 7 environments, 32 of 96 pages typed
`research-essay`, 17 types used exactly once. Type drives asset class, *"so a
taxonomy with 17 singleton values is doing production-planning work it is too
sparse to do reliably."* And from §4: `research-essay` *"is what a page is called
when the audit did not classify it further"*, yet it funnels 50 pages and 200 of
392 asset slots into the largest and least specified production class.

**Diagnosis.** `Type` is carrying three unrelated jobs at once:

1. **Genre** — what kind of document this is to a reader (essay, atlas,
   chronology, semantic field).
2. **Production class** — what must be made, licensed and cleared (the six asset
   classes).
3. **Environment hint** — an implicit signal about posture.

A single 29-value enum cannot do three jobs, and the failure shows up as
singletons: `script`, `practice`, `learning`, `network` and thirteen others exist
because a page needed a genre label, not because production or posture needed a
new class.

**Framework resolution.** Separate the three jobs and give each an input it can
actually be computed from.

**(a) Production class is derived from evidence-class composition, not from
genre.** The Universal Evidence Object (§2) already carries `evidence_class`,
from the constitution's Step 4 inventory: material, textual, epigraphic,
linguistic, genetic, environmental, iconographic, oral/living, historiographical.
An exhibit's production requirements follow from the classes of evidence it
displays, because those are what determine rights, lead time and acquisition
route:

| Evidence classes present | Production consequence |
|---|---|
| epigraphic, textual (pre-modern) | facsimile image; edition rights; transliteration; translation-rights position |
| textual (modern translation) | third-party rights negotiation — unbounded timeline |
| material, iconographic | object image rights; custody chain; holder permission |
| environmental, material (site) | site photography — physical presence required |
| oral/living | **consent**, not licence; Consent Register row mandatory |
| genetic, linguistic (dataset) | dataset verification; accessible alternative; downloadable table |
| historiographical | right-of-reply position where a named party is criticised |

This is a mapping from something the evidence base must record anyway to
something production must know. It replaces a 29-value guess with a 9-value
inventory the constitution already mandates. Note that it correctly refuses the
workbook's collapse: the workbook's `oral/living` case appears only as the hedge
*"pronunciation audio where licensed"*, treating a consent question as a
licensing question. Under this mapping that route is unavailable.

**(b) Posture is derived from claim-set shape, not from genre.** §1.5.

**(c) Genre survives as a label with no downstream authority.** Keep it for
navigation and search facets. Forbid it from determining asset class, priority or
environment. A vocabulary with 17 singletons is fine as a label and unusable as a
key; this makes it the former.

**Consequence.** The residual problem does not disappear, it becomes visible.
Under (a), a `research-essay` page with no recorded evidence classes yields *no*
production class — which is the correct output, because an exhibit whose evidence
composition is unknown cannot have its assets scheduled. `SCHEMA.md` §4 finding 3
("sequencing is inverted for the diagram work": 50 claim-specific diagrams
scheduled by MVP priority, which is driven by low risk, i.e. by pages least
examined) is fixed by the same move: a claim-specific diagram is a derived asset
of a Claim Object, and cannot be commissioned before that claim has a status
above `INHERITED-UNVERIFIED`.

**What is left to the owner.** Whether the 29-value `Type` vocabulary is retired,
reduced to a genre facet, or kept as-is is an editorial call about the site's
own navigation. Recorded as **D-018**.

---

### 1.7 The posture-to-mode matrix

Postures are environments. Modes are ways of looking, available across
environments. The framework specifies five modes; the matrix records which are
mandatory, available or forbidden in each posture.

Modes: **Source Mode** (§1.6.1, §6, §7) · **Atlas Mode** (§8) · **Investigation
Mode** (PROVE IT, §9) · **Field Mode** (children's investigation and Field Bag,
§10 of this document's build list — specified in §10.4) · **Classroom Mode**
(§10.5).

| Posture | Source | Atlas | Investigation | Field | Classroom |
|---|---|---|---|---|---|
| Nocturnal Veḷi | mandatory | available | available | available | available |
| Living Signal Field | mandatory | mandatory | available | available | available |
| Tamil Retrofuture | mandatory | available | mandatory | available | available |
| Living Tiṇai | mandatory | available | available | mandatory | available |
| Reading Room | mandatory | available | mandatory | forbidden | available |
| Extraction / Collection | mandatory | available | mandatory | forbidden | available |
| Reconnection | mandatory | available | available | forbidden | available |

Three rules the matrix encodes:

- **Source Mode is mandatory everywhere.** There is no surface in the institution
  from which the visitor cannot reach the claims, statuses and sources behind
  what they are looking at. This is the operational meaning of "the institutional
  shell remains stable."
- **Field Mode is forbidden in Extraction / Collection and Reconnection.** The
  children's investigation invites a visitor to reach a conclusion from evidence.
  Custody and repair are not exercises. A child may *read* a custody record; a
  child may not be handed "decide whether this object was looted" as a Field Bag
  task. See §10.4.6.
- **Investigation Mode is mandatory in Tamil Retrofuture, Reading Room and
  Extraction / Collection.** These are the three postures where the institution
  is arguing against something. PROVE IT is the mechanism that keeps the argument
  falsifiable rather than rhetorical — the direct product expression of
  constitution §2's requirement that the record stay capable of contradicting
  MelaKeela's own pages.
