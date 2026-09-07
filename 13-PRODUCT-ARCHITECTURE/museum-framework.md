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
| **Correction ledger, public face** — every accepted correction challenge, its outcome and the claim it changed | Correction Register | §11.6 |
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
Mode** (PROVE IT, §9) · **Field Mode** (children's investigation and Field Bag, §10.4) ·
**Classroom Mode**
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

---

## 2. The Universal Evidence Object

### 2.1 Identity — the scheme for the whole graph

Stated here once and used by every object type in §2–§4 and §11.

**Form.** `mk:<type>:<key>` for the object, `mk:<type>:<key>@r<n>` for a specific
revision, `mk:<type>:<key>#<anchor>` for a sub-locator inside one (a stanza, a
line, a region of an image, a column of a dataset).

| Code | Object |
|---|---|
| `evd` | Universal Evidence Object |
| `clm` | Claim Object |
| `rel` | Relationship Object |
| `abs` | Absence record |
| `src` | Source — joins `02-SOURCES/access-ledger.csv.source_id` |
| `agt` | Agent — person, community, institution, publisher, excavator, holder |
| `plc` | Place |
| `lex` | Word / lexeme |
| `txt` | Text |
| `qst` | Question |
| `exh` | Exhibit — the publishable unit a visitor lands on |
| `obl` | Institutional obligation |
| `cns` | Consent record |
| `cor` | Correction |
| `dec` | Editorial decision |

**Properties the scheme must have, and why.**

- **Opaque keys.** The key carries no meaning — not a slug, not a date, not a
  catalogue number. Meaningful identifiers become wrong when the meaning is
  revised, and this institution expects revision. Recommended key: 10-character
  Crockford base32 from a random 50-bit source, checksummed.
- **Never reused, never deleted.** An identifier that has been published resolves
  forever. A retracted object resolves to a tombstone stating that it was
  retracted, when, by which correction (`mk:cor:…`) and what replaced it. This is
  the product expression of `CLAUDE.md`'s *"Never delete a `REJECTED` row."*
- **Revision-addressable.** A citation without `@r<n>` resolves to current; a
  citation with it resolves to that exact revision, and the viewer states that a
  newer revision exists. Every public claim display exposes both forms.
- **Externally resolvable.** Each identifier has a stable URL of the form
  `<institution-domain>/id/<type>/<key>`, content-negotiable to human page or
  machine record (§5).
- **Join-compatible with the existing evidence base.** `mk:src:*` must resolve to
  a row in `02-SOURCES/access-ledger.csv`; `mk:clm:*` to a row in a
  `03-REGISTERS/` register. The identifier scheme does not replace the CSV
  registers; it addresses them. **Whether the register CSVs gain an
  `object_id` column or a separate crosswalk file is maintained is unresolved —
  D-019.**

### 2.2 What the Universal Evidence Object is

The UEO is the single record type for **anything that can be cited as evidence**,
regardless of evidence class. One record type for a seal, a stanza, a
radiocarbon determination, a genome sample, a survey transect, a photograph of an
accession card and a nineteenth-century translator's preface.

The reason for one type rather than nine is constitution Step 4: *"Inventory
evidence classes separately — material, textual, epigraphic, linguistic, genetic,
environmental, iconographic, oral/living, historiographical. One class cannot
borrow certainty from another."* Separate record types would let each class carry
its own conventions and quietly make some classes look more solid than others.
One record type with an explicit `evidence_class` field and **class-specific
required fields** keeps the classes visibly distinct while making them
comparable, searchable and countable in one place.

### 2.3 Core fields — required on every UEO

| Field | Type | Notes |
|---|---|---|
| `id` | identifier | `mk:evd:<key>`, §2.1 |
| `revision` | integer | append-only, §3.6 |
| `label` | string | short human name; not an identifier |
| `evidence_class` | enum(9) | material · textual · epigraphic · linguistic · genetic · environmental · iconographic · oral-living · historiographical |
| `evidence_subclass` | controlled | e.g. `seal`, `stanza`, `radiocarbon-determination`, `aDNA-sample`, `pollen-core`, `accession-record`, `field-recording` |
| `is_primary` | enum | `primary` · `edition` · `derivative` · `interpretation` — see §2.5 |
| `attestation_mode` | enum | `attested` · `reconstructed` · `inferred` · `proposed` · `unidentified-residue` — see §2.6 |
| `date_assertions` | array of Date Assertions | §2.7; **plural, always** |
| `place_assertions` | array of Place Assertions | §2.8; **plural, always** |
| `provenance_chain` | array of Custody Links | §3.4 |
| `source_ids` | array of `mk:src:*` | must resolve in the access ledger |
| `access_status` | enum | `open` · `restricted` · `by-permission` · `refused` · `unlocated` · `destroyed` · `unknown` |
| `rights` | Rights Block | §11.8 |
| `consent_ref` | `mk:cns:*` or null | **required and non-null when `evidence_class = oral-living`** |
| `language_of_record` | BCP-47 + script | the language the *record* is in, not the language of the evidence |
| `created`, `created_by`, `revised`, `revised_by` | metadata | |
| `status_note` | string | free text; may not substitute for a claim status |

**Deliberately absent: a truth field.** A UEO is not true or false. It exists,
it is described, it is dated, it is located, it is held by someone. Truth
predicates belong to Claim Objects (§3). This is the boundary the curatorial
workbook could not draw — `SCHEMA.md` notes its `Risk` column is *"a scheduling
variable"* and that *"none of these labels certifies historical truth"*, which is
correct and is exactly why status must live one level up.

### 2.4 Class-specific required fields

A UEO is invalid if the required fields for its class are absent. Absence is
recorded as an explicit `unknown` with a reason, never as an empty cell.

| Class | Additionally required |
|---|---|
| **material** | material composition; dimensions; excavation or acquisition event; stratigraphic context or `context-lost`; holder; accession number or `unaccessioned` |
| **textual** | work; recension; edition used (`mk:src:*`); manuscript witnesses or `edition-only`; **composition / attestation / copying / redaction / translation dates as separate Date Assertions** (constitution Step 2) |
| **epigraphic** | support material; script; findspot; *in situ* or moved; estampage/photograph reference; published reading and reading variants |
| **linguistic** | form in original script; transliteration; grammatical analysis; semantic range; textual context; edition and exact locator; translation used; alternative translations; interpretive consequence of choosing between them (constitution §7, in full — no reduced form is valid) |
| **genetic** | sample id; site; skeletal element; laboratory; date of extraction; contamination controls; publication; dataset accession; **whether the individual's community descendants were consulted** (`consent_ref` or a typed refusal) |
| **environmental** | proxy type; core/section id; sampling resolution; calibration curve where applicable; laboratory |
| **iconographic** | medium; support; scene description separated from scene interpretation; iconographic parallels cited as Relationship Objects, not as description |
| **oral-living** | speaker or community as `mk:agt:*`; recording circumstances; **`consent_ref`**; withdrawal terms; whether the speaker holds interpretive authority (§11.2) |
| **historiographical** | author; institutional position; date of the *scholarship*; the account it was arguing against; whether a named living party is criticised (triggers §11.3) |

### 2.5 The primary / edition / derivative / interpretation gradient

`is_primary` is four-valued because "primary source" collapses distinctions the
constitution requires:

- **`primary`** — the object or utterance itself: the seal, the inscribed stone,
  the recorded speaker, the sequenced sample, the sediment core.
- **`edition`** — a scholarly presentation of a primary: a critical edition, a
  published reading, a catalogue entry, a dataset release. **An edition is
  evidence about a primary, not the primary.**
- **`derivative`** — a reproduction: photograph, estampage, transliteration,
  scan, digitisation. Digitisation produces derivatives; §1.6.2's rule
  ("digitization is not restitution") is the ethical face of the same
  distinction.
- **`interpretation`** — scholarship: an argument, a translation choice, a
  chronology, an attribution.

The viewer (§6) must render the gradient. A visitor looking at a photograph of a
seal in a museum catalogue is three steps from the seal, and the interface must
say so rather than presenting the photograph as the object.

### 2.6 The attestation gradient

`attestation_mode` implements `CLAUDE.md`'s standing constraint and constitution
§4E: *"An attested language, a reconstructed proto-language, an accepted loan, a
proposed substrate form, a named historical proposal and an unidentified residue
are six different things. Never treat a hypothetical donor as symmetrical with an
attested, reconstructible body of evidence."*

| `attestation_mode` | Display obligation |
|---|---|
| `attested` | may be shown as a form |
| `reconstructed` | must carry the reconstruction marker and the method that produced it |
| `inferred` | must name what it is inferred from and by what rule |
| `proposed` | must name the proposer and the date of the proposal |
| `unidentified-residue` | must be shown as residue — a gap with a shape, never a donor |

**Enforcement rule.** Any display surface that places two UEOs side by side —
the Atlas, evidence search, PROVE IT, a comparison table — must render
`attestation_mode` on both. Symmetrical visual treatment of an attested form and
a proposed substrate form is a violation, catchable in review, and is logged to
`04-AUDITS/BIAS-FAILURE-LOG.csv` when it reaches a published surface.

### 2.7 Date Assertions — why dates are plural

A UEO has no single date. It has a set of Date Assertions, each with:

`assertion_id` · `date_type` · `earliest` · `latest` · `calendar_or_scale` ·
`basis` · `method` · `source_id` · `locator` · `confidence` · `contested_by[]`

`date_type` is drawn from constitution Step 2's list, which is a product
requirement and not merely a research one: **composition · attestation · copying ·
redaction · translation · excavation · publication · modern interpretation** —
plus, for material and environmental evidence, **manufacture · deposition ·
scientific determination · calibration**.

Three consequences:

- Any surface showing "the date of X" must state *which* date type it is showing.
  A default of "earliest attestation" is permitted; a silent default is not.
- Where date types conflict, the conflict is a Relationship Object of type
  `contradicts` (§4), not a resolution made in the display layer.
- The Atlas time control (§8) reads Date Assertions and must expose the type it
  is filtering on. Sliding a timeline that silently mixes composition dates with
  publication dates is the mechanism by which chronology gates fail.

### 2.8 Place Assertions — why places are plural and typed

`assertion_id` · `place_type` · `place_ref` (`mk:plc:*`) · `certainty` ·
`geometry` · `basis` · `source_id` · `locator`

`place_type` ∈ **findspot · production · use · deposition · discovery ·
current-holding · attributed-provenance · unlocated**.

Rules:

- `attributed-provenance` — a place asserted by a dealer, catalogue or tradition
  without an excavation record — is a distinct type and must be displayed as
  such. This is where looted material announces itself, and collapsing it into
  `findspot` is how a collection launders provenance.
- `current-holding` is always populated for material and iconographic evidence,
  or explicitly `unlocated`. It is the join to Reconnection (§1.6.2).
- Geometry carries its own uncertainty: a point, a polygon, a named region or
  `zone-unknown`. **`zone-unknown` renders as unknown and never as empty** —
  constitution §13's *"Unknown regions must remain visibly unknown"* is a
  requirement on the object model, not only on the Atlas.
- Imperial or political control is a Relationship Object about a Place, never a
  Place Assertion on an object. Constitution Step 3: *"Imperial control does not
  prove language use."*

---

## 3. The Claim Object

### 3.1 What it is and what it is for

The Claim Object is the institution's unit of assertion and its unit of
accountability. Everything the museum says in its own voice is a Claim Object or
is derived from one. `CLAUDE.md`: *"Every claim carries exactly one status. No
claim is unstatused."* And: *"Evidence that supports nothing is not collected"* —
the inverse rule, which makes the claim the organising centre rather than the
evidence.

Fields:

| Field | Type | Notes |
|---|---|---|
| `id` | `mk:clm:<key>` | |
| `revision` | integer | append-only |
| `proposition` | string | one proposition, stated so it could be false |
| `status` | enum(7) | `VERIFIED` · `PROVISIONAL` · `HYPOTHESIS` · `INHERITED-UNVERIFIED` · `REJECTED` · `SUPERSEDED` · `HOLD` |
| `inheritance_disposition` | enum(7) or null | `CONFIRMED` · `SUPPORTED` · `PLAUSIBLE` · `REQUIRES VERIFICATION` · `REVISED` · `REJECTED` · `HELD` — recorded **alongside** a status, never in place of one, per `CLAUDE.md` and reconciliation C-1 |
| `evidence_links` | array of Evidence Links | §3.3 — the citation-level join |
| `scope` | Scope Block | proposition · date range · geography · evidence classes required · terms needing original-language work (constitution Step 1) |
| `null_explanation` | string | the null hypothesis this claim is being tested against (Step 1) |
| `rival_claims` | array of `mk:clm:*` | the viable alternatives, each independently reconstructed (Step 8) |
| `bridges` | array of `mk:rel:*` | every language↔ancestry↔culture↔artifact↔religion↔polity↔identity link, each a separate testable claim (Step 10) |
| `standing` | enum | `historically-influential` · `currently-supported` · `revised` · `disputed` · `citation-inertia` · `abandoned` · `rejected` (Step 11) |
| `falsifiers` | array of Falsifier records | §3.9 — **required, non-empty, for any claim above `HYPOTHESIS`** |
| `absences` | array of `mk:abs:*` | §3.7 |
| `supports_exhibit` | array of `mk:exh:*` | the `supports_page` join, generalised |
| `space_allocation` | Proportionality Block | §3.10 |
| `bias_tests` | array of Bias Test records | §3.11 |
| `hold_ref` | path or null | required when `status = HOLD`; points into `05-HOLDS/` |
| `superseded_by` | `mk:clm:*` or null | **required when `status = SUPERSEDED`** |
| `authority` | Authority Block or null | §11.2 — where a community, not the institution, holds interpretive authority |
| `translation_apparatus` | Translation Block or null | **required when the claim turns on the meaning of an ancient word** — §3.8 |

### 3.2 Status is a function of retrieval, not of argument

`VERIFIED` requires a named source with a locator and a retrieval date, and the
retrieval must exist as a row in `02-SOURCES/access-ledger.csv`. The product
consequence is a hard interface rule:

> **No user action, editorial or otherwise, can raise a claim's status. Status is
> recomputed from the claim's Evidence Links and the ledger rows they resolve to.
> An editor can add a link, log a retrieval, or record a rejection. An editor
> cannot type `VERIFIED` into a field.**

This is the product form of `CLAUDE.md`'s *"Argument does not promote a claim.
Confidence does not promote a claim. Only retrieval does."* It also means the
editorial CMS has no status dropdown, which is a deliberate and slightly
uncomfortable design decision and the correct one.

Derivation:

| Condition | Status |
|---|---|
| ≥1 Evidence Link with role `supports`, an access-ledger retrieval, a specific locator, and ≥2 **independent** sources per `02-SOURCES/dependency.csv` | `VERIFIED` |
| as above but sources resolve to one author, excavation, translation, dataset or attribution | `PROVISIONAL` |
| links present, no retrieval logged | `HYPOTHESIS` |
| origin is `01-INHERITED/`, no retrieval | `INHERITED-UNVERIFIED` |
| ≥1 Evidence Link with role `refutes` that survives the challenge process (§11.6) | `REJECTED` |
| a successor claim exists | `SUPERSEDED` |
| a required source is unreachable and a `05-HOLDS/` record exists | `HOLD` |

`INHERITED-UNVERIFIED` is not a weaker `PROVISIONAL`. It is a statement about
*where the claim came from* — a prior model's summary of its own conversation —
and it is unaffected by how confident that summary sounded. `CLAUDE.md`:
inheritance enters as unverified *"including anything the handoff files label as
verified or confirmed."* The interface must therefore never sort or colour
`INHERITED-UNVERIFIED` between `PROVISIONAL` and `HYPOTHESIS` as though the
statuses formed a single ladder. They do not: six of them describe evidential
standing and one describes provenance of the assertion.

### 3.3 Evidence roles — the claim-to-evidence link

An Evidence Link is a first-class record, not a foreign key. It is where
citation-level provenance lives (§3.4).

| Field | Notes |
|---|---|
| `link_id` | `mk:rel:<key>` — Evidence Links are Relationship Objects with a claim on one end |
| `claim_id`, `evidence_id` | |
| `role` | the controlled vocabulary below |
| `locator` | **required**, and specific enough to re-find: page, line, stanza, section, catalogue number, dataset column, timecode. `CLAUDE.md`: *"See the article" is not a locator.* |
| `edition_id` | `mk:src:*` — which edition/printing/release the locator is valid in |
| `retrieval_date`, `retrieval_channel`, `retrieval_agent` | joins the access ledger |
| `quotation` | the exact words relied on, where the evidence is textual |
| `strength` | `decisive` · `substantial` · `weak` · `suggestive-only` |
| `independence_group` | the genealogy key (§3.5) |
| `added_by`, `added_date`, `revision` | |

**Evidence roles.** A role says *what the evidence does for the claim*. Roles are
not opinions about strength; strength is a separate field.

| Role | Meaning |
|---|---|
| `supports` | the evidence, read as cited, makes the proposition more likely |
| `refutes` | it makes the proposition less likely |
| `attests` | it *is* an instance of the thing claimed to exist (a form, an object type, a practice) |
| `dates` | it constrains a Date Assertion the claim depends on |
| `locates` | it constrains a Place Assertion the claim depends on |
| `is-object-of` | the claim is *about* this evidence (a reading, an attribution, a translation) |
| `comparandum` | it is the parallel the claim's analogy rests on |
| `transmits` | it is a link in the copying/redaction/translation chain by which another piece of evidence reaches us |
| `establishes-absence` | it is the survey, excavation report or corpus search that bounds a typed absence (§3.7) |
| `contextualises` | it establishes the setting only, and **cannot on its own move status** |
| `contests-reading` | it offers a different reading of the same primary |

Two rules attached to the vocabulary:

- **`contextualises` cannot promote.** A contact setting is not evidence of
  contact. This is enforced in the derivation table (§3.2, which counts only
  `supports`/`attests`) and it is the same rule §13 states for the Atlas: an
  artifact may *"provide only a possible contact setting"* (§8.6).
- **`comparandum` requires a stated tertium comparationis** — what makes the two
  comparable — recorded in the link's `quotation`/notes. An unstated basis of
  comparison is where prestige bias enters, and the prestige-bias challenge
  (§3.11) tests for it.

### 3.4 Citation-level provenance and the custody chain

**Citation-level provenance** means: for any sentence the institution publishes,
a visitor can reach the exact locator in the exact edition, the retrieval that
put it in the record, and the chain by which the evidence reached that edition.
Not a bibliography. `SCHEMA.md` records what the alternative looks like in
practice: 78 of 96 audited pages with zero external links, 960 estimated
bibliography entries and *"essentially none of its sourcing is checkable by a
reader without manual re-derivation"* (`INHERITED-UNVERIFIED`). Citation-level
provenance is the requirement that makes that state impossible to reproduce.

The **provenance chain** on a UEO is an ordered array of Custody Links:

`step_index` · `from_agent` (`mk:agt:*`) · `to_agent` · `event_type` · `date` ·
`place` · `basis` (the document evidencing this step, as `mk:evd:*`) ·
`documented` (`documented` · `asserted` · `undocumented-gap`) · `notes`

`event_type` ∈ **excavation · surface-collection · purchase · gift · bequest ·
seizure · exchange · loan · transfer · export · repatriation · digitisation ·
publication · translation · copying · redaction · re-attribution · loss ·
destruction**.

Rules:

- **Gaps are steps.** An `undocumented-gap` link is written explicitly, with the
  span it covers. A chain that jumps from a nineteenth-century district to a
  present accession number with nothing between is not a two-step chain; it is a
  three-step chain whose middle step is a gap. Rendering it as two steps is the
  laundering §1.6.2 exists to prevent.
- **Every chain terminates in a present holder** or in `unlocated` / `destroyed`.
- **The chain is public.** Custody is not editorial metadata; it is exhibit
  content in the Extraction / Collection and Reconnection postures.
- **Textual custody uses the same structure.** Composition → oral transmission →
  first written witness → recension → critical edition → translation is a custody
  chain, and `transmits` Evidence Links are its edges. Constitution §4V:
  *"Preservation is not authorship; codification is not invention; first
  attestation is not origin."* The chain is what makes that visible instead of
  merely asserted.

**Every published sentence resolves.** The rendering contract: any claim-bearing
sentence on any surface exposes, without leaving the page, its `mk:clm:` id, its
status, its Evidence Links with locators and retrieval dates, and a link into
Source Mode. A sentence that cannot do this is not published in the institution's
voice; it is published as editorial framing and marked as such (§6.4).

### 3.5 Source genealogy and independence

Constitution Step 5 and `CLAUDE.md`'s source-independence constraint: *"Two
citations tracing to the same author, excavation report, dataset or museum
attribution count as one."*

Every Evidence Link carries an `independence_group`. Groups are formed on the
shared root: the same author, the same excavation, the same translation, the same
dataset release, the same museum attribution. Dependencies are recorded in
`02-SOURCES/dependency.csv` (`dependency_id`, `source_a`, `source_b`,
`relationship`, `effect_on_status`, `notes`).

Product requirements:

- The **independent-source count**, not the citation count, is what the interface
  shows next to a claim. Where they differ the interface shows both: "9
  citations, 2 independent."
- Status derivation (§3.2) counts distinct `independence_group` values.
- The viewer renders the genealogy as a tree: nine citations converging on one
  1953 excavation report is a **shape the visitor should be able to see**, and it
  is the single most effective display the institution can offer against citation
  inertia.
- `standing = citation-inertia` (§3.1) is proposable from this structure but is
  never automatic: it is an editorial judgement, logged, with the genealogy as
  its evidence.

### 3.6 Revision history

**Append-only. Nothing is edited in place. Nothing is deleted.**

Every object in §2, §3, §4 and §11 carries a revision series. A revision record:

`revision` · `object_id` · `timestamp` · `actor` (`mk:agt:*`) · `actor_role`
(`researcher` · `editor` · `community-authority` · `challenger` · `system`) ·
`change_type` · `diff` · `reason` · `triggering_record` (`mk:cor:*`, `mk:cns:*`,
a re-audit queue row, a bias-failure row) · `status_before` · `status_after`

`change_type` ∈ **created · evidence-added · evidence-removed · locator-corrected
· status-recomputed · superseded · rejected · held · released-from-hold ·
scope-narrowed · scope-widened · retracted-for-consent · translation-revised ·
authority-assigned**.

Rules:

- **`REJECTED` rows persist and stay visible.** `CLAUDE.md`: *"Rejected reasoning
  stays visible so it is not re-proposed. Never delete a `REJECTED` row."* The
  product form: a rejected claim keeps its identifier, resolves, renders with its
  rejection, its date, and the evidence that rejected it, and appears in evidence
  search results (filtered out by default, one control away). The institution's
  errors are part of its record.
- **`SUPERSEDED` points forward and backward.** Both directions are navigable.
- **Citations pin.** Any citation of the institution made from a published page
  carries `@r<n>`; a later visitor following it sees what was cited plus a notice
  that it has since changed and how.
- **Consent withdrawal is the single exception to "nothing disappears", and it
  is a narrow one.** Under `retracted-for-consent` the *material* is withdrawn;
  the *record that material existed, was published, and was withdrawn on a stated
  date under a stated consent term* remains. §11.4.
- **A public "what changed" feed** is generated from revision records: the
  institution's changes are themselves an exhibit, in the Reconnection and
  Reading Room postures.

### 3.7 Absence records

Constitution §6 and `CLAUDE.md`'s negative-evidence standard, as an object.

Before any surface argues from absence, an Absence record must exist:

| Field | Notes |
|---|---|
| `id` | `mk:abs:<key>` |
| `expected_evidence` | what should exist if the proposition were true |
| `expected_where` | places, strata, corpora, archives |
| `p_produced` | probability it was produced, with reasoning |
| `p_survived` | probability it survived, with reasoning |
| `search_coverage` | excavation/sampling/corpus coverage actually achieved, with sources |
| `accessibility` | whether we could reach it if it existed |
| `recognisability` | whether we would recognise it if we saw it |
| `absence_type` | `NOT PRODUCED` · `NOT PRESERVED` · `NOT EXCAVATED` · `NOT PUBLISHED` · `NOT ACCESSIBLE` · `NOT RECOGNISED` · `DOCUMENTED DESTRUCTION` · `ABSENT DESPITE ADEQUATE SEARCH` |
| `evidence_links` | `establishes-absence` links to the surveys and searches that bound it |

Product rules:

- **Only `ABSENT DESPITE ADEQUATE SEARCH` may function as evidence against a
  proposition.** The other seven types are statements about the archive, and the
  interface renders them in the archive's voice, not the past's.
- **`unknown` is never a rival.** `CLAUDE.md`: *"'Unknown' is residual, never a
  positive rival explanation."* The comparison interfaces — PROVE IT (§9), the
  Atlas transition panel (§8.5) — must not list "unknown" as an option beside
  named hypotheses.
- **Silence in a curated record is not refutation.** Where an absence sits in an
  archive whose creator had reason not to record the thing (constitution Step 6),
  the Absence record must carry the archive audit, and the display must show it.

### 3.8 The Translation Block

Required whenever a claim turns on the meaning of a consequential ancient word.
Constitution §7, in full — the block is invalid if any field is empty:

`original_script` · `transliteration` · `grammatical_form` · `semantic_range` ·
`textual_context` · `edition` (`mk:src:*`) · `exact_locator` ·
`translation_used` · `alternative_translations[]` ·
`interpretive_consequence` · `inherited_category_audit`

`inherited_category_audit` is the audit of the English word being reached for:
*race, tribe, slave, barbarian, fort, religion, caste, civilization, invasion,
indigenous*. It records what the English term imports that the original does not.

**Display contract.** Wherever a translated term appears in the institution's
voice, the alternative translations and the interpretive consequence are one
interaction away, on the same surface. `CLAUDE.md`: *"Do not let the translation
decide the historical question."* A surface that shows one English word with no
route to the others has let it.

### 3.9 Falsifiers

Constitution Step 12. A Falsifier record: `what_would_change_it` ·
`evidence_class_required` · `where_it_would_come_from` · `direction`
(`would-strengthen` · `would-weaken` · `would-reject`) · `currently_testable`
(bool) · `blocked_by` (`mk:src:*` or a `05-HOLDS/` path).

Non-empty falsifiers are required for any claim above `HYPOTHESIS`. They are
public: they are what PROVE IT (§9) is built on, and they are the honest form of
"what remains unknown" in the §14 public-copy shape.

### 3.10 Proportionality

Constitution Step 9 and `CLAUDE.md`: *"weight follows evidence. No rhetorical
equality where evidence is unequal."*

The Proportionality Block on a claim records `evidential_weight`
(from independent-source count, evidence-class breadth and strength) and
`allocated_space` (words, screen area, or navigation prominence on each exhibit
it appears in). The two are compared at review; a large divergence is a review
finding, not an automatic edit.

This is deliberately **advisory, not enforced**. Automating space allocation from
a computed weight would make the interface decide historical questions, which is
the failure §7 forbids in the translation case. The metric exists so that the
gap is visible and must be defended, not so a layout engine can settle it.

**Where a gated-out hypothesis appears** (constitution Step 7 — failure of the
chronological, geographical, mechanism, positive-evidence or diagnostic gates),
it appears as *"a concise exclusion or historiographical note — not an equal
section."* The product form is a distinct display component with a fixed small
footprint, named **Exclusion Note**, which cannot be expanded into an exhibit
without the gate result being overturned first.

### 3.11 Bias Test records

Constitution §8, `CLAUDE.md`'s two adversarial tests. Both run before any unit of
work is called finished, and the result is logged whether or not it found
anything.

`test_type` ∈ `prestige-bias` · `preferred-counter-narrative`.
Fields: `unit_tested` · `question_asked` · `finding` · `action_taken` ·
`bias_failure_row` (into `04-AUDITS/BIAS-FAILURE-LOG.csv`) · `reaudit_rows`
(into `04-AUDITS/REAUDIT-QUEUE.csv`) · `tester` · `date`.

Both tests are required on every exhibit before publication, and the pair is
required — running one is a failed test, because the two failure modes are
symmetrical in form and asymmetrical in power. `CLAUDE.md`: *"Correct both
without pretending their archival and institutional power has been equal."* The
product consequence is that the bias-test surface must carry the asymmetry
statement (§11.2) rather than presenting the two challenges as a balanced pair,
which would itself be the false-equivalence failure.

### 3.12 Derived assets

A claim-specific diagram, map, chart or reconstruction is an **asset derived from
a Claim Object**, addressed as `mk:evd:<key>` with `is_primary = derivative` and
a `depicts` Relationship to the claim.

Rule: **a derived asset may not be commissioned or published while the claim it
depicts is `INHERITED-UNVERIFIED` or `HOLD`.** This resolves `SCHEMA.md` §4's
finding 3 — 50 claim-specific diagrams scheduled by MVP priority, which is driven
by low risk, i.e. by the pages least examined. Under this rule the diagram
schedule is a function of the verification schedule and cannot invert it.
