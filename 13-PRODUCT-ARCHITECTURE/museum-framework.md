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
   primary-source viewer and evidence search (§7) reached from wherever the
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

Modes: **Source Mode** (§1.6.1, §7) · **Atlas Mode** (§8) · **Investigation
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

---

## 4. The Relationship Object

### 4.1 Why relationships are objects

Because relationships are the claims that are hardest to see and easiest to
smuggle. Constitution Step 10: *"Every link among language, ancestry, culture,
artifact, religion, polity and modern identity is a separate claim."* If a
relationship is an edge in a graph rather than a record with a status, a
speculative link renders identically to an attested one, and the institution has
argued by drawing a line. `environment-map.csv`'s `Avoid` for the Living Signal
Field names this exactly: *"No gaming HUD or arbitrary links."*

A Relationship Object is therefore a Claim Object's sibling, not a foreign key.
It carries a status, evidence, falsifiers and a revision history of its own.

### 4.2 Fields

| Field | Notes |
|---|---|
| `id` | `mk:rel:<key>` |
| `subject`, `object` | any two `mk:*` identifiers, including other relationships |
| `predicate` | the controlled vocabulary, §4.3 |
| `directionality` | `directed` · `symmetric` · `direction-unknown` |
| `status` | the same seven-value vocabulary as claims — a relationship is unstatused only if it is unpublished |
| `attestation_mode` | inherited semantics from §2.6 |
| `date_assertions` | when the relationship held, typed as in §2.7 — **not** the dates of its endpoints |
| `place_assertions` | where it held |
| `mechanism` | the process by which it could have obtained — **required for any relationship implying transfer or descent** |
| `alternatives` | array of `mk:rel:*`: the rival relationships that would explain the same observation |
| `evidence_links` | as §3.3 |
| `strength` | `decisive` · `substantial` · `weak` · `suggestive-only` |
| `falsifiers` | as §3.9 |
| `bridge_type` | null, or one of the seven-domain bridge kinds, §4.4 |
| `display_weight` | derived, advisory; §4.5 |

### 4.3 The predicate vocabulary

Grouped by what kind of claim the predicate is. The grouping matters because the
groups have different evidential requirements and must not be visually
interchangeable.

**Chronological** — `precedes` · `contemporary-with` · `postdates` ·
`stratigraphically-above` · `stratigraphically-below`.

**Spatial** — `found-at` · `made-at` · `used-at` · `deposited-at` ·
`held-at` · `on-route-between` · `separated-by-barrier`.

**Transmission** — `copied-from` · `redacted-from` · `translated-from` ·
`transmits` · `derived-from` · `depicts`.

**Linguistic** — `cognate-with` · `borrowed-from` · `substrate-of` ·
`sound-correspondence-with` · `reconstructed-ancestor-of` ·
`convergent-with` (areal) · `unexplained-residue-in`.
These five-plus predicates are kept distinct because collapsing them is the
specific conflation the audit's Overlap cluster 8 names
(`INHERITED-UNVERIFIED`): *"separate sound correspondence, contact borrowing,
substrate inference, genetic relationship and script history."*

**Population-genetic** — `shares-ancestry-component-with` ·
`descends-from-population` · `admixed-with`.
Constrained by Overlap cluster 5's requirement (`INHERITED-UNVERIFIED`):
*"do not treat ancestry components as peoples, languages or moral categories."*
Enforced at §4.4.

**Material** — `same-material-source-as` · `same-technique-as` ·
`typologically-similar-to` · `traded-along`.

**Social and institutional** — `patronised-by` · `composed-in-milieu-of` ·
`ruled-by` · `classified-by` · `custody-transferred-to` · `criticises` ·
`responds-to`.

**Epistemic** — `supports` · `refutes` · `contradicts` · `supersedes` ·
`depends-on` (source genealogy) · `re-reads`.

### 4.4 Bridges — the seven-domain rule

The constitution's seven domains: **language · ancestry · culture · artifact ·
religion · polity · modern identity.** A relationship whose subject and object
sit in different domains is a **bridge**, and bridges carry additional
requirements:

1. `mechanism` is required and may not be a restatement of the correlation.
2. `alternatives` must be non-empty: at minimum, the null relationship (the two
   things co-occur without a link) must be listed and its evidence given.
3. `status` may not exceed `PROVISIONAL` on correlational evidence alone.
4. The endpoints' domains are rendered on every display of the bridge. A visitor
   must be able to see that a line runs from an *ancestry component* to a
   *language*, which is not the same kind of object.
5. **Bridges are never inherited by transitivity.** If A (artifact) bridges to B
   (polity) and B bridges to C (language), the system must not derive or display
   A→C. Transitive closure is disabled across domain boundaries. This is a
   database-level rule because it is the mechanism by which a map of trade goods
   silently becomes a map of languages.

`bridge_type` records the ordered domain pair, e.g. `ancestry→language`,
`artifact→religion`, `polity→modern-identity`. The last is subject to the extra
governance of §11.2, because claims bridging antiquity to a present community are
where the institution's output becomes politically usable.

### 4.5 Display rules

- **Every rendered edge carries status and attestation mode.** An unstatused edge
  cannot be drawn.
- **Strength maps to a visual variable and the mapping is stated in a legend on
  every surface that draws edges.** No surface may encode strength without a
  legend.
- **`suggestive-only` and `direction-unknown` edges are off by default** in every
  view, reachable by an explicit control labelled with what it turns on.
- **Alternatives are one interaction away from every bridge.** Selecting a bridge
  shows its rivals at the same visual weight as itself, per §3.10's refusal to
  let layout settle a question.
- **Density is a legibility problem, not an evidence problem.** Where a view
  cannot draw everything, it drops by *display filter*, never by *strength* —
  i.e. it never quietly drops weak edges to look cleaner, because that produces a
  picture more confident than the evidence.

---

## 5. Data export and API readiness

### 5.1 The principle

The institution's evidence base must be usable by people who do not trust the
institution. That is not a courtesy feature; it is the only form the standing
"capable of contradicting" requirement (constitution §2) can take in a product.
A visitor who cannot get the claim table out cannot check it independently.

### 5.2 Export

Every surface that displays evidence offers export of exactly what is displayed,
plus what would be needed to check it.

| Level | Formats | Contents |
|---|---|---|
| **Single claim** | CSV, JSON, BibTeX/CSL-JSON | claim, status, evidence links with locators and retrieval dates, sources, independence groups, falsifiers, revision id |
| **Exhibit** | CSV bundle, JSON | all claims, relationships, absences, translation blocks, bias tests, editorial decisions, obligations |
| **Atlas view** | CSV, GeoJSON, JSON | the exact filter state, every object in view with its assertions, every excluded object with the reason it was excluded |
| **Search result set** | CSV, JSON | the query, the result set, the total, and the facets applied |
| **Whole base** | JSON-LD + CSV snapshot, versioned, dated | the register files, the object graph, the access ledger, the dependency map |

Requirements:

- **Exports carry status.** No export produces a bare table of assertions. A
  spreadsheet of claims with the status column stripped is the artefact this
  whole architecture exists to prevent, and the export must make it awkward
  rather than default.
- **Exports carry the exclusion set** where a filter was applied. What a map
  leaves out is part of what it says.
- **Exports are revision-pinned and dated**, with the resolvable base URL for
  every identifier.
- **The register CSVs remain human-readable and diffable.** The columns in
  `CLAUDE.md`'s register format —
  `claim_id,claim,status,source_id,locator,retrieval_date,supports_page,notes` —
  are the export's lowest common denominator and must round-trip.

### 5.3 API readiness

"Readiness", not "API": §12 asks for the property, and building the service is a
later decision.

The property is achieved when all of the following hold, and each is testable
without writing a server:

1. **Every object has a resolvable, revision-addressable identifier** (§2.1).
2. **Every object serialises losslessly** to a documented JSON schema, including
   its status, provenance and revision pointer.
3. **The vocabularies are published as enumerations** with definitions and
   stability guarantees: the 7 statuses, the 7 inheritance dispositions, the 9
   evidence classes, the 5 `is_primary` values, the 5 attestation modes, the 8
   absence types, the 11 evidence roles, the predicate vocabulary, the 12 date
   types, the 8 place types, the 7 postures, the 11 Atlas layers.
4. **Content negotiation** on the identifier URL returns human page or machine
   record from one address.
5. **No display-only fields exist.** Anything a page shows is in the record. If
   a surface computes something (posture derivation, independent-source count,
   evidential weight), the computation is specified and its inputs are exported.
6. **A conformance fixture set** exists: a small number of real objects covering
   every enum value and every required-field rule, used to test any future
   service, export or import.
7. **Rate, licence and attribution terms for reuse are stated** (§11.8), and the
   licence on the *evidence base* is stated separately from the licence on
   *media*, because they will differ (§11.8.3).

**Deliberately deferred, not specified here:** authentication, write access,
federation with other collections, persistent-identifier registration (DOI,
ARK, Handle), and any query language beyond the export filters. Whether the
institution registers external persistent identifiers is **D-020**.

---

## 6. Entry routes: object, place, word, text, question

### 6.1 What an entry route is

§12 names five: **object · place · word · text · question**. They are not five
menus. They are five *kinds of thing a visitor already has in mind* when they
arrive, and each is a first-class addressable node type (`mk:evd:`, `mk:plc:`,
`mk:lex:`, `mk:txt:`, `mk:qst:`) with its own landing surface, its own default
posture and its own way of leading into the same claim graph.

The design constraint that makes them worth separating: **a visitor arriving by
one route must not be silently handed the answers of another.** Someone who
arrives at a word must not be shown a map of a people; someone who arrives at a
place must not be shown a language label. Those are exactly the bridges §4.4
governs, and the entry routes are where the temptation to cross them without a
mechanism is strongest.

Every route converges on the same objects. No route has private content.

### 6.2 Object route

**Node:** a UEO with `evidence_class` ∈ material, epigraphic, iconographic.
**Default posture:** Living Tiṇai if it has a findspot and a material context;
Extraction / Collection if its `access_status` is `restricted`, `by-permission`,
`refused` or `unknown`, or its custody chain contains an `undocumented-gap`.

The object landing states, in this order and before any interpretation:

1. What it is, materially: composition, dimensions, technique.
2. Where it is *now*, and who holds it, and on what terms it can be seen.
3. Where it is *said* to be from, with the place type (§2.8) — and if that is
   `attributed-provenance`, saying so in the same sentence.
4. Its custody chain, gaps included (§3.4).
5. Its dates, by type, with the basis of each (§2.7).
6. Its provenance questions, from constitution §4V: who made it, supplied the
   material, did the labour, spoke without being recorded, copied, translated,
   classified, got the credit, was excluded, holds it now. **Unanswered questions
   are displayed as unanswered, not omitted.**
7. Only then: the claims it is evidence for, each with status and role.

Rule: **an object page never opens with an interpretation.** The interpretation is
a claim with a status and it appears in the claim list, attributed. This is the
Extraction / Collection `Avoid` — *"no spectacle or unsupported allegation"* — as
a page order rather than a tone note.

### 6.3 Place route

**Node:** `mk:plc:`. **Default posture:** Living Tiṇai.

A Place carries: named forms across languages and periods, with the date each
name is attested; geometry with its own certainty; environmental setting as
evidence (`environmental` UEOs); excavation and survey history including **what
has not been excavated and at what coverage**; the objects with assertions here,
by place type; the routes and barriers connecting it (`on-route-between`,
`separated-by-barrier`); political control as dated relationships; and its
present-day setting, communities and holders.

Rules:

- **Excavation coverage is displayed on every place**, because it is the
  denominator for every absence argument made about it (§3.7). A place with 2%
  coverage and a place fully excavated do not produce the same silence.
- **Political control never implies language.** Constitution Step 3. Control
  relationships and linguistic relationships are drawn in visually distinct
  registers and never merged into one "cultural" layer.
- **Modern administrative boundaries are not evidence** and are shown, if at all,
  as a separate reference layer that can be switched off, clearly labelled as
  present-day.
- A place whose location is uncertain renders as a region or as
  `zone-unknown`, never as a point with a confident marker.

### 6.4 Word route

**Node:** `mk:lex:`. **Default posture:** Living Signal Field.

A word landing is a Translation Block (§3.8) expanded into a surface, plus the
attestation record. It carries: original script, transliteration, grammatical
analysis, semantic range with the evidence for each sense, every attested
occurrence with text, locator and edition, the reconstructions proposed and by
whom, the relationships (`cognate-with`, `borrowed-from`, `substrate-of`,
`sound-correspondence-with`, `unexplained-residue-in`) each statused and each
with its mechanism, the alternative translations, and the **inherited-category
audit** for the English word normally used.

Rules:

- **The attestation gradient is the page's spine** (§2.6). An attested form, a
  reconstructed proto-form and a proposed substrate donor are rendered in three
  visibly different registers, always, including in search results and in the
  Atlas's WORDS layer.
- **A word never carries a people.** The word route may not display an ethnic,
  ancestral or modern-identity label as a property of a lexeme. Any such link is
  a `bridge_type = language→modern-identity` relationship with §4.4's
  requirements and §11.2's governance.
- **Occurrence counts are shown with their corpus and search method**, because a
  count without them is not a fact about a language. (The repository already
  holds a worked instance of this discipline in
  `03-REGISTERS/rigveda-pur-family-occurrences.csv` and
  `04-AUDITS/rigveda-pur-family-method.md`.)
- Where the institution's own pages have used the English category uncritically,
  the audit says so and links the correction (§11.6).

### 6.5 Text route

**Node:** `mk:txt:`. **Default posture:** Reading Room.

A Text carries the **five-date spine** as separate, individually sourced Date
Assertions — composition, attestation, copying, redaction, translation — plus
publication and modern interpretation where relevant; its recensions and
witnesses; its transmission custody chain (§3.4); the editions available and
which one each locator is valid in; who composed it, who preserved it, who
copied it, who redacted it, who translated it, who was excluded from it
(constitution §4V); and its passages as addressable sub-locators
(`mk:txt:<key>#<stanza>`).

Rules:

- **No text displays a single date.** The interface shows the spine and requires
  the visitor to see which date is being used for what.
- **Editions are evidence, not transparency.** A passage is always shown as
  "this edition's reading", with variants reachable.
- **A translation is an interpretation** (`is_primary = interpretation`) and is
  rendered as one, attributed to its translator with a date.
- **Composition milieu is not authorship of the ideas.** §4V's
  *"codification is not invention"* is a display rule here: the text route must
  not let the compilers of a corpus absorb credit for what the corpus records.

### 6.6 Question route

**Node:** `mk:qst:`. **Default posture:** Nocturnal Veḷi.

The question route is the constitution's Step 1 made public. A Question carries:
the exact proposition under examination, its date range, its geography, the
evidence classes it would take to answer it, the terms needing original-language
work, **the viable explanations**, and **the null explanation** — all of which
Step 1 already requires researchers to write down.

It then shows, for each viable explanation: its gate results (Step 7 —
chronological, geographical, mechanism, positive evidence, diagnostic
predictions), its independent reconstruction (Step 8), its current standing
(Step 11), and its falsifiers (Step 12). Gated-out explanations appear as
Exclusion Notes (§3.10), not as sections.

Rules:

- **The null explanation is always listed and never last by default.**
- **Open questions may outnumber answered ones and this is not a defect.** The
  question route is the institution's honest surface; it is where Nocturnal
  Veḷi's *"vastness without menace"* is earned by content rather than by palette.
- **A question with no viable explanation still publishes**, with its absences
  typed (§3.7) and its holds named (`05-HOLDS/`).
- The Question route is the entry point for PROVE IT (§9) and for the children's
  investigation (§10.4); both are structured walks over the same object.

### 6.7 Cross-route invariants

- Every route reaches Source Mode in one interaction (§1.7).
- Every route shows the status of everything it displays.
- No route may present a bridge as a property of its own node type: an object
  does not "have" a language, a place does not "have" an ethnicity, a word does
  not "have" a people, a text does not "have" a race. These are relationships
  with mechanisms and rivals, or they are not displayed.
- Every route offers export of what it shows (§5.2).

---

## 7. Source Mode: the primary-source viewer and evidence search

### 7.1 The primary-source viewer

The viewer's job is to let a visitor look at the thing the claim rests on, at the
locator the claim cites, in the edition the claim cites, without leaving the
argument.

**Required behaviours.**

1. **Deep-locator addressing.** The viewer opens at the cited locator — a stanza,
   a line, a plate, a catalogue entry, a dataset row, a timecode — via
   `mk:<type>:<key>#<anchor>`, and the anchor is stable across revisions or
   redirects with a notice.
2. **Facsimile beside transcription beside translation**, with each layer
   labelled by `is_primary` (§2.5) so the visitor can see they are looking at a
   photograph of a page of an edition of a text, and can count the steps.
3. **Variants are first-class.** Where witnesses differ, differences are shown,
   not silently normalised. Where the institution's cited reading is one of
   several, the alternatives are present at the locator.
4. **The quoted span is highlighted, and the quotation stored on the Evidence
   Link is checked against it.** A drift between the two is a data error surfaced
   in review, and it is the cheapest available guard against citation decay.
5. **Original script always available**; transliteration is an addition, never a
   replacement, and the transliteration scheme is named.
6. **Provenance and rights ride along.** Every facsimile displays holder, licence,
   credit and the terms under which it is reproduced (§11.8). A facsimile the
   institution cannot show is represented by a **rights placeholder that states
   what exists, where, and why it is not shown** — never by silence, which would
   misrepresent the evidence base as thinner than it is.
7. **Where the source cannot be reached at all**, the viewer shows the `HOLD`
   record from `05-HOLDS/` and the access-ledger row, including
   `EGRESS_BLOCKED` and paywall states. The institution's own access failures
   are visible to visitors. This is Extraction / Collection applied to the
   institution itself.
8. **No viewer surface interprets.** Interpretation appears as claims beside the
   viewer, attributed and statused.

### 7.2 Evidence search

Search over the object graph, not over page text. Full-text search of published
prose exists too, and is a different, clearly-labelled control.

**Searchable object types:** claims, relationships, evidence objects, absences,
sources, places, words, texts, questions, obligations, corrections, editorial
decisions.

**Facets, all of which are record fields, none of which is a computed opinion:**

- status (7) · inheritance disposition (7)
- evidence class (9) · `is_primary` (5) · attestation mode (5)
- date type and range (12 types) · place type (8) · geometry certainty
- evidence role (11) · relationship predicate group · bridge type
- independent-source count · strength · standing (7)
- absence type (8)
- posture (7) · exhibit
- access status · rights state · consent state
- language and script of the evidence, and of the record
- revision date range · "changed since I last looked"

**Search behaviours that the architecture requires:**

1. **Status is never a hidden filter.** If a default excludes `REJECTED` and
   `SUPERSEDED`, the result header says so and the control to include them is
   visible, not buried. The institution's rejected reasoning is searchable by
   design (§3.6).
2. **Result rows carry status, attestation mode and independent-source count.**
   A result list that looks like a bibliography is a failure of this surface.
3. **Zero results are typed.** "No claims match" and "no evidence has been
   collected in this area" and "this area is blocked on source access" are three
   different answers, and the search must distinguish them by consulting
   absences, holds and the access ledger. An empty result set that reads as
   "nothing exists" is the negative-evidence failure §3.7 exists to prevent,
   reproduced in a search box.
4. **Query provenance.** Every result set is addressable, exportable (§5.2) and
   carries the query, the facets, the date, and the base revision — so a visitor
   can cite a search the way they cite a claim, and someone else can re-run it.
5. **Search across languages and scripts.** A query in Tamil script, in
   transliteration, or in English reaches the same objects (§11.10), and the
   interface states which form it matched on.
6. **No relevance ranking that encodes confidence.** Ranking may use match
   quality, recency of revision and structural centrality. It may **not** rank by
   status, strength or evidential weight, because a ranked list is read as an
   argument. Sorting by status is available as an explicit, labelled sort.

---

## 8. Artifact Atlas v2

### 8.1 What v2 changes

The audited v1 page is `artifact-atlas`, titled *"Artifact Atlas: 175 Ancient
South Asian Sites Mapped"*, MVP rank 3, `Keep`, `Low` risk, with 88 estimated
bibliography entries against 8 words of prose and no Claim Risk row — all
`INHERITED-UNVERIFIED`. The schema assessment's collision A records that the site
count 175 is one side of an open contradiction (`03-REGISTERS/inherited-claims.csv`
`IH-250`, X-01: 140 / 150 / 158 / 167→175 / 194 / 199) *"adopted as settled fact,
put in a page title, and rated low-risk"*.

v2's first structural change follows directly:

> **The Atlas has no headline count.** A count is a claim (`mk:clm:`) with a
> status, a definition of what is being counted, an inclusion rule and a
> falsifier. It is displayed as a claim, inside the Atlas, with its status
> visible, or it is not displayed. The number of sites in view is a property of
> the current filter and is always shown *with* the filter, never as a title.

`DECISIONS-NEEDED.md` D-006 asks the owner what the atlas site count is. Under
this specification the Atlas can be built and shipped before that is answered,
because it never asserts a total in its own voice.

The other changes from v1 to v2: every mapped thing is a UEO or a Relationship
Object rather than a map pin; every pin carries status and attestation mode;
unknown zones are drawn; the exclusion set is exportable; and the Atlas gains the
language-movement mode (§8.3–§8.7).

### 8.2 The Atlas as a view over the object graph

The Atlas is not a dataset. It is a **projection of the object graph onto space
and time**, and it may display nothing that is not an object with a status.

- **Spatial input:** Place Assertions (§2.8), typed. The map must let the visitor
  see and filter by place type; a findspot and an attributed provenance are never
  the same marker.
- **Temporal input:** Date Assertions (§2.7), typed. **The time control names the
  date type it is filtering on** and refuses to mix types silently. Where an
  object has several assertions of the chosen type, it appears across the union
  of their spans with the uncertainty drawn.
- **Edges:** Relationship Objects (§4), with §4.5's display rules and §4.4's
  transitivity ban.
- **Uncertainty is geometry.** Points, polygons, named regions and
  `zone-unknown`. A precise-looking dot for an approximate location is a false
  statement made in a visual grammar, and is a bias-log finding if published.
- **Unknown is drawn.** Constitution §13: *"Unknown regions must remain visibly
  unknown."* Unknown zones are a rendered layer, not the absence of a rendered
  layer. Blank map is forbidden as a representation of unknown, because blank
  reads as empty and empty reads as nobody.
- **Coverage is drawable.** Excavation and survey coverage (§6.3) is available as
  an overlay, so a visitor can see whether a cluster of finds is a cluster of
  ancient activity or a cluster of modern digging. This overlay is what makes
  every absence argument on the map checkable.
- **The exclusion set is first-class.** Any filtered view can report and export
  what it excluded and why (§5.2).

### 8.3 The language-movement mode

Constitution §13: *"The language feature must combine time and geography without
turning artifacts into language labels."*

That sentence is the mode's specification and its principal risk in one line. The
mode exists because language history is a movement through time and space; it is
dangerous because the visible objects in that space are pots, graves, seals and
metals, and the easiest thing a map can do is colour a pot by a language. The
architecture prevents this in three places: the four-state artifact response
(§8.6), the ban on transitive bridges (§4.4), and the rule that no layer may
recolour another layer's objects (§8.4).

**Settings.** The visitor moves through seven settings, each a Place with its own
geometry, uncertainty and dated relationships:

1. steppe / Sintashta-related settings
2. Oxus / BMAC
3. Afghanistan and Helmand
4. Balochistan and the Indus sphere
5. Punjab
6. Kuru regions
7. Gangetic settings

Two properties are required of the setting list. **It is not a route.** The
settings are places the visitor can move through in any order, and the interface
must not present them as an itinerary with an arrow, because the itinerary is
itself the contested claim. And **the settings have fuzzy, dated, overlapping
extents**: each is drawn with its uncertainty and its extent may differ by
period, so "Punjab" at one date and at another are not the same polygon.

Whether the mode nonetheless offers a *guided* sequence alongside free
navigation, and if so what its default order is and what it is claiming, is an
owner decision — **D-021**.

### 8.4 The eleven layers

Every layer is independently switchable, independently sourced, and independently
statused. Constitution §13 lists them; this section specifies what each one *is*
in terms of the object model, and what it may not do.

| # | Layer | What it draws | Governing constraint |
|---|---|---|---|
| 1 | **SOUNDS** | Attested and reconstructed sound correspondences and changes, located and dated where the evidence permits | Every item carries `attestation_mode`. A reconstructed change is never drawn as an event with a place unless the localisation is itself a statused claim. |
| 2 | **WORDS** | Lexemes (`mk:lex:`) with their attested occurrences, plotted at the place and date of the *attestation*, not of the supposed speaker | An occurrence is a fact about a text; the text has a findspot and a composition place, which may differ. Both are shown. |
| 3 | **GRAMMAR** | Morphological and syntactic features, including areal features | Features are properties of attested varieties, never of populations. Convergence (`convergent-with`) is drawn distinctly from inheritance (`reconstructed-ancestor-of`). |
| 4 | **NEIGHBOURS** | Who was adjacent to whom, when — the contact-possibility layer | This layer establishes *setting only*. Objects on it can never raise a linguistic claim above `PROVISIONAL` by themselves; it is the map form of the `contextualises` role (§3.3). |
| 5 | **MATERIALS** | Material types, sources, techniques and their movement | **May not be recoloured by any linguistic layer.** A material distribution is a material distribution. |
| 6 | **RITUALS** | Attested ritual practices, their evidence and their dates | Practice is a `culture`-domain object. Any link to language, ancestry or polity is a bridge (§4.4). |
| 7 | **TEXTS** | Texts (`mk:txt:`) at their composition, attestation, redaction and manuscript-witness places, each as a separate typed assertion | A text plotted at one point is a lie about transmission; the layer draws the spread. |
| 8 | **ANCESTRY** | Genetic samples and ancestry components, at sample sites, with dates and laboratories | **Components are not peoples, languages or moral categories** (Overlap cluster 5, `INHERITED-UNVERIFIED`). Component names appear with their defining publication and its date; the layer may not be coloured to match any language layer. |
| 9 | **ARCHAEOLOGICAL CULTURES** | Named archaeological cultures with their defining assemblages, dates and the history of their naming | The naming history is part of the object: who named it, when, on what assemblage, and whether the name has since been contested. A culture is a typological construct, and the layer says so on its face. |
| 10 | **POLITICAL CONTROL** | Dated control relationships over places | Constitution Step 3: *"Imperial control does not prove language use."* This layer may not be used as a proxy for any other layer, and the interface states this where the two are shown together. |
| 11 | **UNKNOWN SPEECH ZONES** | Regions and periods for which there is no evidence of what was spoken | **Not a background. A drawn layer with its own sources** — the Absence records (§3.7) that establish why the zone is unknown, typed (`NOT EXCAVATED`, `NOT PRESERVED`, `NOT RECOGNISED`…). This is the layer that makes the other ten honest. |

**Cross-layer rules.**

- **No layer may recolour, reshape or relabel another layer's objects.** Layers
  overlay; they do not modify. This is the technical statement of "without
  turning artifacts into language labels."
- **Any two layers shown together produce a *correlation*, and the interface says
  so.** Where a visitor switches on ANCESTRY and WORDS, the surface states that
  co-location is not a relationship and offers the statused bridges that do exist
  between the two, with their mechanisms and rivals.
- **Layer legends carry status distributions.** A layer whose contents are mostly
  `HYPOTHESIS` looks different from one that is mostly `VERIFIED`, and the
  difference is stated, not merely implied by a colour ramp.
- **Layer 11 cannot be switched off** while any language layer (1, 2, 3) is on.
  Turning off the unknown while displaying the known is how a language map
  becomes a claim about a continent.

Whether the eleven layers are grouped for the visitor (e.g. language / material /
population / political) and what the default-on set is at first load are
interface decisions with real interpretive weight, and are recorded as
**D-022**.

### 8.5 Transitions — the per-transition requirements of §13

A **transition** is the mode's unit of assertion: a statused claim that some
layer-state changed between settings, or within a setting across time. It is a
`mk:clm:` with a `mk:rel:` spine, and the Atlas may not animate, draw or narrate
any change that is not one.

Constitution §13 requires every transition to identify ten things. Each is a
required field; a transition with any of them empty cannot be displayed.

| §13 requirement | Field | Specification |
|---|---|---|
| earliest evidence | `earliest_evidence` | `mk:evd:` + locator + Date Assertion. The *earliest* item, not a representative one, and if the earliest is contested, all contenders. |
| evidence class | `evidence_classes[]` | from the nine (§2.3). Plural, because a transition supported by three classes is a different object from one supported by one, and the panel shows the breakdown. |
| date range | `date_range` | earliest/latest with the **date type** named (§2.7) and the basis of each bound |
| geography | `geography` | typed Place Assertions with geometry and certainty; `zone-unknown` permitted and drawn |
| whether attested or reconstructed | `attestation_mode` | the five-value gradient (§2.6), not a binary — §13's phrasing is a floor, and a `proposed` donor is not a `reconstructed` proto-form |
| possible mechanisms | `mechanisms[]` | each a named process — migration, trade, elite dominance, exogamy, prestige borrowing, areal convergence, inheritance, independent innovation — with the evidence that the mechanism was available in that place and period. **Non-empty.** |
| alternative explanations | `alternatives[]` | rival transitions, each independently reconstructed (Step 8) and displayed at equal weight to the primary; **the null explanation is always among them** |
| confidence | `confidence` | derived from the claim's status, independent-source count and evidence-class breadth; **displayed with its inputs**, never as a bare number or a bare word |
| source | `sources[]` | `mk:src:` rows resolving in `02-SOURCES/access-ledger.csv`, with locators, retrieval dates and independence groups (§3.5) |
| what would change the interpretation | `falsifiers[]` | §3.9. **Non-empty.** |

**The transition panel.** Selecting a transition opens a panel that shows all ten,
in this order, with alternatives adjacent to the primary rather than below a
fold. Two additional requirements:

- **The panel is the same object as the export.** What the panel shows is exactly
  what §5.2 exports for that transition. There is no display-only prose.
- **Animation is subordinate to the panel.** If the mode animates movement across
  the map, the animation may only render transitions that pass the ten-field
  check, and a transition whose `attestation_mode` is `proposed` or whose
  `confidence` is low must be visually distinguishable while moving — not only
  when clicked. Motion is persuasive; unlabelled motion is an argument the
  institution has not made.

Whether the mode animates at all, or presents transitions as static compared
states, is **D-023**: it is a real interpretive choice, not a styling one.

### 8.6 Clicking an artifact — the four states

Constitution §13 requires that clicking an artifact state whether it supplies
linguistic evidence, provides only a possible contact setting, demonstrates
material movement, or provides no language evidence. This is specified as a
**required, exhaustive, mutually exclusive four-value field on every artifact in
the language-movement mode**, computed from the artifact's Evidence Links and
checked editorially:

| State | Condition | What the interface says and does |
|---|---|---|
| **Supplies linguistic evidence** | the UEO has an `attests` or `supports` link to a claim in the language domain — normally because it bears writing, or a form on it is linguistically analysable | Shows the linguistic claim, the reading, the edition, and the alternatives. The reading is itself a claim with a status; a disputed reading does not upgrade to evidence. |
| **Provides only a possible contact setting** | its links to language claims are `contextualises` only | Says so in those words. Shows what contact it makes possible, and states explicitly that possibility of contact is not evidence of contact. Cannot contribute to a transition's `earliest_evidence`. |
| **Demonstrates material movement** | it supports a `same-material-source-as`, `traded-along` or `made-at`≠`found-at` relationship | Shows the movement of the material and states that the movement of a thing is not the movement of a language or of a people. Offers the statused bridges, if any exist. |
| **Provides no language evidence** | none of the above | Says so plainly, and stays on the map. **This state must be common and must be visible.** An Atlas in which every artifact turns out to be linguistically meaningful is an Atlas that has been curated into an argument. |

The state is displayed on hover/selection, not hidden in a detail pane, and it is
a search facet (§7.2).

### 8.7 What the Atlas may never do

A short list, because these are the failure modes the mode invites, and they
correspond to the Living Signal Field's `Avoid` — *"no gaming HUD or arbitrary
links"*:

1. Colour an artifact, culture or region by a language.
2. Draw an edge without a status and a strength legend.
3. Animate a movement that is not a statused transition.
4. Render an approximate location as a precise point.
5. Render unknown as blank.
6. Show a total in its own voice.
7. Let a filter silently drop the weak evidence to produce a cleaner picture.
8. Derive an A→C relationship across domains from A→B and B→C.
