# Artifact Atlas v2 — build specification

**Artefact class:** specification. Not research, not site code, not a page brief.
**Extends:** `13-PRODUCT-ARCHITECTURE/museum-framework.md` §8, which states what the
Atlas *is*; this document states what has to be built for §8 to be true of a
running thing. Of the four record shapes it specifies, one is named by the
framework and left unspecified (**Place**, `mk:plc:`, referenced throughout §2–§8
and never given fields); the other three are **new constructs introduced here** —
**Extent Assertion**, **Route** and **Place-Evidence Link** — as are the
Confidence Polygon, the Coverage record, `absence_scope`, `boundary_basis` and
Rule S-5. Saying which are which matters, because a specification that presented
its own inventions as the framework's would be borrowing authority it has not
got.
**Constitutional basis:** `00-CONTROLLER/METHODOLOGY-CONSTITUTION.md` §13
(the language-movement artifact atlas, the eleven layers, the four artifact
states, the visibly-unknown requirement), §12 (product and institutional
specification stage), Step 2 (chronology), Step 3 (geography and contact),
Step 4 (evidence classes), Step 6 (archive audit), Step 10 (bridges),
§6 (negative evidence), §4E (attestation gradient).
**Directory:** `13-PRODUCT-ARCHITECTURE/`, per constitution §15.
**Status of every design proposition in this file:** `HYPOTHESIS`, except where a
statement restates constitution §13 (a constitutional instruction, not an
evidentiary claim), restates the museum framework or the experience object model
(both `HYPOTHESIS`), or restates a register row or the curatorial audit — in
which case the row's own status is carried and marked at the point of use.

**No code.** This file contains no HTML, CSS, JavaScript, SQL or schema-language
source, per constitution §12's closing line and `CLAUDE.md`'s prohibition on
writing site code in this repository. Where it specifies a check, it specifies
what the check asserts and what failing it means, not the program that runs it.

---

## 0. What this document is, and the rules it runs under

### 0.1 What it specifies

Eight things, in dependency order:

1. **The geometry contract** — a constrained GeoJSON profile, positional
   certainty, confidence polygons, and the drawn form of `zone-unknown` (§2 of this document).
2. **The Place object** — `mk:plc:`, with stable opaque identifiers, plural dated
   extents, names as assertions, and excavation coverage as a required field (§3 of this document).
3. **The time contract** — signed structured dates on a single axis that crosses
   BCE/CE without a year-zero fault, radiocarbon handled as radiocarbon, and a
   second axis for chronology that is only relative (§4 of this document).
4. **The Route object** — `mk:rte:`, with origin, destination, ordered waypoints,
   direction as a separate claim, and a six-valued route uncertainty that decides
   whether a line may be drawn at all (§5 of this document).
5. **The language-evidence state** — the four-value field constitution §13
   requires when a visitor clicks an artifact, specified as a required, derived,
   non-null field on every Place-Evidence Link (§6 of this document).
6. **The transitivity block** — the mechanism by which closure across the
   constitution's seven domains is disabled, so a map of trade goods cannot
   become a map of languages (§7 of this document).
7. **The unknown and the count** — how unknown regions are rendered as objects
   rather than as absence, and the structural reason the Atlas cannot display a
   headline site count (§8 of this document).
8. **The eleven layers** — each specified against the object model, each with a
   statement of which registered claims could populate it today and which could
   not (§9 of this document).

Then the transition record (§10), the conformance checks (§11), an honest
statement of what the first buildable Atlas actually contains (§12), the owner
decisions (§13), the adversarial tests (§14) and this file's status (§15) — all
of this document; see §0.4 on how references read.

### 0.2 The rules it inherits

The museum framework's three rules and the experience object model's fourth
govern here unchanged.

**Rule S-1 — No specification may cite a claim above its register status.**
Everything drawn from `01-INHERITED/` is `INHERITED-UNVERIFIED` and is marked at
the point of use. This document's inherited inputs are the v1 atlas audit
(`IH-057`, `IH-060`, `IH-105`, `IH-197`, `IH-250`, `IH-270`, `IH-329`) and the
contradiction `X-01`. None of them is used as a finding; they are used as a
description of what the previous build did.

**Rule S-2 — Where a choice is the owner's and has not been made, the choice is
recorded, not taken.** Three are recorded here as `D-053`, `D-054` and `D-055` in
`09-DECISIONS/OWNER-DECISIONS.csv`. In each case the specification is written so
that it is buildable under either answer, and the default it builds under is
stated.

**The threshold, stated because this document escalates a two-letter type code
and adopts several new record shapes without asking.** Rule S-2 governs *choices
that are the owner's* — product positions, publication positions, and amendments
to documents this one does not own. It does not govern specification work, which
is what this document was commissioned to do: inventing a Confidence Polygon or
an `absence_scope` field is the task, not a decision taken in the owner's place.
`D-054` is escalated precisely because it is the one construct that would *edit
another specification's table* — framework §2.1's identity codes — rather than
add to this one. Where this document instead **adopts** on a question the
framework left open, it says so at the point of adoption and names what it
narrows; there are two such places, at §8.2 (the scope polygon) and §8.5 rule 4
(distribution readouts, which resolve a contradiction between framework §8.4 and
framework §8.1 that neither anticipated).

**Rule S-3 — Specification does not promote.** Naming a Place object does not
create a place record. No `mk:plc:`, `mk:rte:` or transition described in this
file exists. Nothing here is a finding.

**Rule S-4 — The experience layer holds no content of its own**
(experience object model §0.3). The Atlas is a surface, and every sentence it
shows is a rendering of an evidence-layer object or is editorial framing marked
as such.

### 0.3 The rule it adds

**Rule S-5 — The map may draw only what a row asserts, and it may draw it only
as strongly as the row asserts it.**

Two halves, and the second is the one that gets lost. The first half is
already the framework's: §8.2's *"it may display nothing that is not an object
with a status"*. The second half is this document's, because a map violates it in
a way a page cannot. A page that overclaims does so in words that can be read and
disputed. A map overclaims in *grammar* — in a dot where the source gave a
district, in a line between two findspots, in a filled polygon where an analyst
drew a boundary freehand, in six decimal places on a coordinate that was
published to two. Each of those is a statement the record does not contain, made
in a form that carries no sentence to argue with.

Rule S-5 is therefore enforced by the geometry vocabulary rather than by review:
the constructs that would overclaim are not available. `point` is not a permitted
geometry for an approximate location (§2.3 of this document). A `LineString` is
not a permitted geometry for a route whose path is unevidenced (§5.3 of this
document). A continuous colour ramp is not a permitted rendering for a hand-drawn
extent (§2.4 of this document). An extent is not a permitted property of a
reconstructed proto-language at all (§2.6 of this document). None of these
is a style guideline; each is a validity condition, and an object that fails one
does not render.

### 0.4 How section references read

A bare `§x.y` is a section of **`museum-framework.md`**. A reference to this
document is written **"§x.y of this document"**. The experience object model is
named in full. Constitution references are written `constitution §x` or `Step n`.
Register rows are cited by claim identifier and file
(`DE-M-021`, `03-REGISTERS/domain-e-measurements.csv`).

### 0.5 What it deliberately does not do

- It does not choose the visual design, the projection, the basemap or the map
  orientation. Per §12.3 the visual system is a separate handoff. One note
  belongs here rather than there, because it is an evidence question wearing a
  design costume: **map orientation is a convention, not a finding.** The v1 page
  is recorded as *"a south-up atlas"* (`IH-197`, `INHERITED-UNVERIFIED`), and
  whichever orientation v2 takes, it is a decision with a stated reason and not a
  default. This document's geometry contract is orientation-neutral: it stores
  coordinates, not a view.
- It does not resolve `D-021` (a guided sequence through the seven settings),
  `D-022` (layer grouping and first-load defaults), `D-023` (whether the mode
  animates) or `D-034` (the site count). Each is cited where it bites and the
  specification survives either answer.
- It does not specify the editorial CMS, authentication, or any service. §5.3's
  "API readiness" is a property of the records, and this document adds the Atlas's
  records to it without proposing an API.
- It does not create any place, route, transition or layer instance, and it does
  not promote any claim. No retrieval happened while writing it.

### 0.6 A correction to this task's premise

The task named `03-REGISTERS/domain-m-measurements.csv`. **No file of that name
exists in this repository.** Domain M's registered measurements are in
`03-REGISTERS/domain-m-brahui-position.csv` (26 rows, `DMB-001` to `DMB-026`),
and that is the file read for §9 of this document. The geographic quantities it
produces are also carried in `03-REGISTERS/domain-e-geography.csv`
(`GEO-DR-01`..`06`, `GEO-MU-01`..`06`). Nothing in the task depended on the
missing name; it is recorded because a specification that silently substituted a
different file would be doing the thing this repository exists to prevent.

---

## 1. The three enforcement requirements, stated before the machinery

Three requirements from the record have to hold structurally rather than by
editorial care. They are stated here in one place so that a reader can check the
rest of the document against them, and each is specified in full later.

**REQ-1 — Clicking an artifact must say what it supplies for language.**
Constitution §13: clicking an artifact must state whether it *"supplies
linguistic evidence"*, *"provides only a possible contact setting"*,
*"demonstrates material movement"*, or *"provides no language evidence"*.
Specified at §6 of this document as `language_evidence_state`: a **required,
non-null, derived, four-valued field on every Place-Evidence Link**, computed
from the object's Evidence Links by a published function, not enterable by an
editor, displayed on selection, exported, faceted, and guarded by a distribution
check because §8.6 requires the fourth state to be *common*.

**REQ-2 — Transitive closure is disabled across the seven domains.**
§4.4 rule 5: *"If A (artifact) bridges to B (polity) and B bridges to C
(language), the system must not derive or display A→C… This is a database-level
rule because it is the mechanism by which a map of trade goods silently becomes a
map of languages."* Specified at §7 of this document as five interlocking
mechanisms — total domain tagging, no transitive operator exposed to any
rendering surface, a traversal allow-list with bridges as terminal edges, a ban
on persisting or rendering any derived edge, and an export that carries the
domain pair so that a downstream user who chains anyway does it visibly.

**REQ-3 — Unknown regions stay visibly unknown, and the Atlas carries no headline
count.** Constitution §13: *"Unknown regions must remain visibly unknown."*
§8.1: *"The Atlas has no headline count."* The count is not a stylistic
restraint: `IH-250` (`INHERITED-UNVERIFIED`, contradiction `X-01`) records the
project's own records disagreeing across **six values** — 140, 150, 158,
167→175, 194, 199 — and one of them, 175, *"adopted as settled fact, put in a
page title, and rated low-risk"* is in the live page title now. Specified at §8
of this document: unknown is a Feature with an absence record behind it, blank is
reserved for out-of-scope and out-of-scope is itself drawn, layer 11 cannot be
switched off beneath a language layer, and the title slot of the Atlas surface
admits no numeric token at all while any cardinality readout is bound to the
filter component that produced it and carries its exclusion set.

---

## 2. Identity and the geometry contract

### 2.1 Identifiers the Atlas uses

The framework's scheme (§2.1) is used unchanged: `mk:<type>:<key>`, opaque
10-character Crockford base32 keys from a random 50-bit source with a checksum,
never reused, never deleted, revision-addressable as `@r<n>`, sub-addressable as
`#<anchor>`, resolvable at `<institution-domain>/id/<type>/<key>`.

The Atlas reads `evd`, `clm`, `rel`, `abs`, `src`, `agt`, `plc`, `lex`, `txt`,
`exh`, and — for the editorial decisions and corrections this document requires at
§3.2, §3.7 and §6.3 of it — `dec` and `cor`. It adds **one code**, and the
addition is declared rather than assumed:

| Code | Object | Status of the addition |
|---|---|---|
| `rte` | **Route** — §5 of this document | An extension to §2.1's code table. §2.1 is the framework's, so the extension is raised as **`D-054`** and the specification is written to work without it (§5.1 of this document gives the fallback modelling). |

Two sub-identifiers are used inside a Place and are **not** separate objects:
`assertion_id` on an Extent Assertion and on a Place Assertion, addressed as
`mk:plc:<key>#ext-<n>` and `mk:evd:<key>#plc-<n>`. They are addressable because a
citation of a location is a citation of *one* asserted location, and a footnote
that resolves to "the place record" resolves to a disagreement.

**A key carries no geography.** Not a modern district, not a site code, not a
coordinate hash. The point of the framework's opaque-key rule bites hardest here:
places are re-localised, split and merged more often than any other object type,
and an identifier that encoded a location would have to be either wrong or
reissued. §3.7 of this document specifies split, merge and re-localisation.

### 2.2 The GeoJSON profile

Geometry is **RFC 7946 GeoJSON**, constrained. The constraints exist because
unconstrained GeoJSON is capable of stating things this record cannot support.

| # | Constraint | Why |
|---|---|---|
| G-1 | **WGS 84 (CRS84), longitude then latitude, decimal degrees.** No `crs` member; alternative CRSs are not accepted on input and are converted at ingest with the conversion logged. | RFC 7946 fixes one CRS. A silent CRS assumption is a systematic positional error with no visible symptom. |
| G-2 | **Every geometry is wrapped in a `Feature`.** A bare geometry is not a valid Atlas object. | A geometry with its properties stripped is §5.2's *"spreadsheet of claims with the status column stripped"* in map form. |
| G-3 | **Required Feature properties**, all non-null: `mk:id`, `mk:revision`, `mk:object_type`, `mk:status`, `mk:attestation_mode`, `mk:positional_certainty`, `mk:geometry_semantics`, `mk:date_type`, `mk:earliest`, `mk:latest`, `mk:source_ids`, `mk:locator`. Plus `mk:language_evidence_state` on every Feature that carries a Place-Evidence Link (§6 of this document), and `mk:absence_ref` on every `zone-unknown` Feature (§2.5). | A Feature that reaches a renderer without a status cannot be drawn under §4.5 and cannot be exported under §5.2. Making the properties required at the geometry level means the two rules have one enforcement point. |
| G-4 | **No `GeometryCollection`.** A place with two disjoint candidate locations is two Features with two certainties, not one geometry with two parts. | A `GeometryCollection` renders as one shape and hides that it is a disagreement. `MultiPolygon` remains available for a single extent that is genuinely discontinuous (an island group, a two-mound site). |
| G-5 | **Polygon winding follows RFC 7946** — exterior rings counter-clockwise, holes clockwise — and rings are closed and non-self-intersecting. | Interoperability, and because a self-intersecting "extent" has no defined interior and therefore no defined claim. |
| G-6 | **No third coordinate.** Elevation is a property of a place, recorded as a field with its source, not a coordinate. | An elevation smuggled into a coordinate array is unsourced and unstatused. |
| G-7 | **Coordinate precision is capped at the source's precision.** Every Feature carries `mk:coordinate_precision_dp`, taken from the source, and no surface — display, export, tooltip or URL — renders more decimal places than that. | This is §8.7 rule 4 (*"render an approximate location as a precise point"*) in its numeric form. A district-level attribution stored at six decimal places is a false statement whether or not anyone draws it. |
| G-8 | **Antimeridian and polar cases follow RFC 7946 §3.1.9.** Not expected in this region; stated so that an imported dataset cannot introduce the fault silently. | |
| G-9 | **No geometry may be computed from another geometry and stored as evidence.** Buffers, convex hulls, centroids, simplifications and least-cost paths are *derived assets* under §3.12 — they carry `is_primary = derivative`, name the method and its parameters, point at the claim they depict, and inherit §3.12's rule that they may not be published while that claim is `INHERITED-UNVERIFIED` or `HOLD`. | A centroid of a region, stored as a point, is how an approximate extent becomes a precise site over two migrations of a dataset. |

**Centroids specifically.** A renderer may compute a centroid to place a label.
It may not store one, export one, or expose one as the object's location, and a
label anchor is not a marker: the label attaches to the drawn extent and moves
with it.

### 2.3 `positional_certainty`, and the rule that governs which geometries are legal

Every Place Assertion, Extent Assertion and Feature carries
`positional_certainty`, and the value **determines which geometry types are
valid**. This is the single most load-bearing constraint in §2 of this document.

| `positional_certainty` | Meaning | Permitted geometry |
|---|---|---|
| `surveyed-point` | An instrument reading or a published coordinate for a located feature, with the survey named | `Point` |
| `mapped-approximate` | A location known to within a mapped area — a mound, a village territory, a published site polygon | `Polygon` · `MultiPolygon` |
| `region-only` | The source gives a region, district or river reach, not a location | `Polygon` · `MultiPolygon` (the region's own extent) |
| `named-region-unmapped` | The source names a region whose extent is not established | `Polygon` marked `mk:geometry_semantics = named-region-unmapped`, drawn as an unbounded label field, never as a filled boundary |
| `disputed-location` | Two or more candidate locations, each with its own source | Two or more Features, each with its own certainty and its own identification claim (§3.4 of this document). **Never one geometry spanning the candidates.** |
| `unlocated` | No location is asserted | No geometry. The object appears in the Atlas's unlocated tray (§4.6 of this document, framework §8.2) and is counted in every readout. It does not appear on the map and it does not disappear from the interface. |
| `zone-unknown` | The location question is itself the object (§2.5 of this document) | `Polygon` · `MultiPolygon`, with `mk:absence_ref` |

**The point rule, stated on its own because it is the one that will be argued
with:** a `Point` is legal only for `surveyed-point`. There is no permitted path
by which an approximate location becomes a dot. Where a downstream consumer needs
a point — a clustering algorithm, a distance calculation — it computes one under
G-9 as a derivative, with the method named, and the derived point is not the
object's location and cannot be written back.

This has a cost and the cost is real: an Atlas built this way looks less
authoritative than one built of dots, and it is harder to make a distance
measurement from. The register already contains a worked example of what dots
buy and what they cost. `DMB-014` (`VERIFIED`, `SRC-050`) measures a metric
defect — Euclidean distance over raw degrees overstating the great-circle
distance by up to +13.7% — in a calculation whose *inputs* were exact published
point coordinates. Precision in the inputs did not protect the result. Where the
inputs are approximate and the interface has drawn them as exact, nothing does.

### 2.4 Confidence polygons

A **Confidence Polygon** is an ordered set of nested rings expressing how far out
from an evidenced core a claim's spatial extent is being asserted. It is a value
on an Extent Assertion or on a claim's geometry, not an object of its own.

| Field | Notes |
|---|---|
| `rings[]` | Ordered inner-to-outer, ≥1. Each ring: `ring_id`, `geometry` (`Polygon`/`MultiPolygon`), `level_label`, `semantics`, `basis`, `method`, `source_id`, `locator` |
| `semantics` | **Per ring**, from the four values below. Rings in one polygon may not mix `modelled-probability-contour` with any other value |
| `drawn_by` | `mk:agt:` — the analyst or the model. Non-null |
| `drawn_date` | |
| `nesting_validated` | Boolean, set by the check at §11.1 of this document, not by the author |

**The four `semantics` values.**

| Value | What the ring is | Render obligation |
|---|---|---|
| `evidence-hull` | A hull over evidenced locations, with the algorithm and its parameters named (convex, concave with α, buffered with distance and units) | The evidenced locations are drawn *with* the hull. A hull without its points is an assertion about an interior nobody sampled |
| `modelled-probability-contour` | A contour of a named probabilistic model, with its inputs, its assumptions and the contour value (0.5, 0.9) | **The only value that may carry a percentage label or a continuous colour ramp.** The model is a derivative asset under §3.12 and inherits its publication bar |
| `analyst-drawn-extent` | A boundary an analyst drew from judgement | Discrete, visibly hand-drawn boundary; legend names the analyst and the basis. **No ramp, no percentage, no interpolation between rings** |
| `administrative-approximation` | A present-day administrative unit standing in for an extent | Marked present-day and non-evidential (§6.3), switchable off, and excluded from every export of evidence |

**Four rules.**

1. **Nesting is validated, not asserted.** Each ring must be spatially contained
   in the next ring out. A confidence polygon whose rings cross is invalid and
   does not render. Overlapping-but-not-nested candidate extents are a
   `disputed-location`, which is a different construct (§2.3 of this document).
2. **A ramp implies a model.** A continuous fill gradient states that the value
   varies continuously and that someone computed the variation. Only
   `modelled-probability-contour` did. Every other value renders as discrete
   bands with visible edges, because the edge is where the analyst's judgement
   actually is.
3. **A find-density surface is not a confidence polygon** unless the excavation
   and survey coverage overlay (§8.2, §6.3) is rendered with it and the record
   carries the coverage denominator. Density of finds is density of digging until
   the denominator says otherwise. The framework calls this overlay *"what makes
   every absence argument on the map checkable"*; this rule makes it what makes
   every density argument checkable too.
4. **A confidence polygon expresses spatial extent only.** It never encodes a
   claim's status, its strength or its independent-source count. Those are
   rendered as themselves (§4.5), because a claim that is weakly evidenced over a
   small, well-defined area and a claim that is strongly evidenced over a vague
   one are different situations and one visual variable cannot say both.

### 2.5 `zone-unknown` is a geometry, not the absence of one

§2.8 already requires it of the object model: *"`zone-unknown` renders as unknown
and never as empty"*. Its buildable form:

- A `zone-unknown` Feature is a `Polygon` or `MultiPolygon` whose extent is
  **the search space**, not a location — the region within which the question
  "what was spoken here / where was this" has been asked and not answered.
- `mk:absence_ref` is **required and non-null**: an `mk:abs:` record (§3.7)
  carrying `expected_evidence`, `expected_where`, `p_produced`, `p_survived`,
  `search_coverage`, `accessibility`, `recognisability` and one of the eight
  `absence_type` values. A `zone-unknown` polygon with no absence record behind
  it is not a statement about the past; it is a shrug with a border, and it does
  not render.
- The polygon's boundary is itself typed. `boundary_basis` ∈
  `coverage-limit` (the edge of where anyone looked) · `evidence-limit` (the edge
  of where evidence stops) · `analyst-drawn` (a judgement) · `feature-limit` (a
  physical boundary — a coast, a watershed). A boundary drawn where the *survey*
  stopped and a boundary drawn where the *evidence* stopped are different
  statements, and an unknown zone bounded by the first is mostly a statement
  about excavation history.
- **A `zone-unknown` polygon may not be filled with a texture, hatch or colour
  that ranks it against a known zone on the same scale.** Unknown is not a low
  value of known.

### 2.6 What may never carry an extent

**A reconstructed proto-language has no geometry.** No point, no polygon, no
confidence polygon, no homeland. Objects with `attestation_mode = reconstructed`
are excluded from every extent construct in this section.

This is not a new rule; it is the register's own practice made structural.
`DE-M-021` (`VERIFIED`, `SRC-060`) records the exclusion in its note: *"Proto-nodes
are excluded: a reconstructed protolanguage has no location, only a hypothesis
about one."*

What may exist instead is a **homeland proposal**, and it is a different kind of
object: a `mk:clm:` with `attestation_mode = proposed`, carrying its proposer and
the date of the proposal (§2.6's display obligation), whose map, if it has one, is
a **derivative UEO of that author's published figure** — attributed, dated, and
drawn in the author's name, never in the institution's. A visitor sees whose line
it is.

The rule is symmetric by construction and the symmetry is the point: it forbids
an Indo-European homeland polygon and a Proto-Dravidian homeland polygon on
identical grounds, and it forbids the institution drawing either one in its own
voice while permitting both to be shown as what they are — proposals with
authors.

`attestation_mode = unidentified-residue` is excluded from extents on the same
grounds and more strongly. §2.6: it *"must be shown as residue — a gap with a
shape, never a donor"*. A residue with a polygon is a donor with a homeland. The
253-lemma Rigvedic retroflex figure (`DME-004`, `VERIFIED`) is the register's
nearest live instance, with the register's own qualification carried: its note
reads *"This is an UPPER BOUND on the residue, not a loanword list."* An upper
bound is not itself a residue and is not a donor; it has no location and is not
owed one.

---

## 3. The Place object

### 3.1 Why a Place is not a pin

The v1 page mapped sites (`IH-105`, `INHERITED-UNVERIFIED`: *"194 site records,
315 class-windows and 14 classes, with 54 of 199 site-class rows dated from
excavation reports and 145 marked assumed"*). A pin holds a name, a coordinate
and a class. Four things the record requires do not fit in it: that a place's
extent differs by period, that its names are datable assertions in different
languages, that the identification of a textual name with a mapped location is a
separate claim with a status, and that a place's *excavation coverage* is the
denominator for every absence argument made about it (§6.3).

`145 of 199` rows marked *assumed* is what a pin does to the fourth of those. The
Place object exists so that "assumed" is a typed, sourced field rather than a
flag on a spreadsheet.

### 3.2 Fields

| Field | Type | Notes |
|---|---|---|
| `id` | identifier | `mk:plc:<key>`, §2.1 |
| `revision` | integer | append-only (§3.6) |
| `preferred_label` | string | An **editorial decision**, logged as `mk:dec:`, not a property of the place. Carries `label_language` (BCP-47 + script) |
| `names[]` | array of Name Assertions | §3.4 of this document |
| `place_class` | enum | §3.8 of this document — what kind of place it is, distinct from `place_type` |
| `extents[]` | array of Extent Assertions | §3.3 of this document. **Plural, always, and dated** |
| `excavation_coverage[]` | array of Coverage records | §3.5 of this document. **Required**; `unknown` permitted only with a reason |
| `identification_claims[]` | array of `mk:clm:` | §3.4 of this document. The claims that this place is the place a text, a dealer or a tradition names |
| `same_as[]` | array of `mk:rel:` | §3.6 of this document. External concordance, each as a statused relationship |
| `control_relations[]` | array of `mk:rel:` | Dated `ruled-by` relationships. **A relationship about the place, never a property of it** (§2.8, constitution Step 3) |
| `routes[]` | array of `mk:rte:` | Derived index of routes with this place as origin, destination or waypoint. Read-only |
| `absences[]` | array of `mk:abs:` | §3.7 |
| `environmental_setting[]` | array of `mk:evd:` | Environmental-class evidence for the place, as evidence, not as description (§6.3) |
| `present_day` | Present-Day Block | Communities, holders, administrative location, current name in current use. **Marked non-evidential, separately switchable, excluded from evidence exports** |
| `rights`, `access_status`, `consent_ref` | | As §2.3 and §11.8 |
| `created`, `created_by`, `revised`, `revised_by` | metadata | |

**Two fields that are deliberately absent.**

- **No `country`.** A modern state attribution is a present-day reference
  property and lives in `present_day`, where it can be switched off. A place's
  identity is not the polity that currently administers it, and an atlas of
  antiquity that indexes by modern nation has made a claim about continuity it
  did not intend to make and cannot support.
- **No `coordinates`.** There is no scalar location on a Place. Location is
  always an Extent Assertion with a certainty, a date and a source (§3.3 of this
  document). A
  place with one surveyed point has one extent whose geometry is a `Point`; the
  shape of the record does not change.

### 3.3 Extent Assertions — a place's extent is plural and dated

§8.3 requires it of the seven settings: *"the settings have fuzzy, dated,
overlapping extents… 'Punjab' at one date and at another are not the same
polygon."* The Extent Assertion is that requirement as a record, and it applies
to every place, not only to the settings.

`assertion_id` · `geometry` (a Feature under §2.2 of this document) · `positional_certainty` ·
`geometry_semantics` · `confidence_polygon` (optional, §2.4 of this document) · `valid_from` ·
`valid_to` (signed structured dates, §4 of this document) · `date_type` · `basis` · `method` ·
`source_id` · `locator` · `retrieval_date` · `status` · `attestation_mode` ·
`contested_by[]`

Rules:

1. **A Place with no Extent Assertion is `unlocated`, and `unlocated` is an
   extent record**, not an empty field. It carries a source for the statement
   that the location is not established, and it puts the place in the unlocated
   tray rather than off the interface.
2. **Extents do not interpolate.** An extent asserted for one period and an
   extent asserted for another do not imply anything about the interval between
   them. A time control moving across the gap shows the gap (§4.6 of this document).
3. **Two extents for the same period are a disagreement**, rendered as two
   Features with their sources, never merged, never averaged, never unioned.
4. **`valid_from`/`valid_to` carry a `date_type`** like every other date in the
   system (§4.2 of this document). The period over which an extent is *asserted
   to have held* and
   the period over which it was *surveyed* are different assertions.

### 3.4 Names, and the identification claim

**A name is an assertion.** `name_assertion_id` · `form` (original script) ·
`transliteration` · `language` · `script` · `name_type` · `attested_from` ·
`attested_to` (signed dates) · `source_id` · `locator` · `status`.

`name_type` ∈ `endonym` · `exonym` · `scholarly-coinage` ·
`archaeological-site-name` · `modern-administrative` · `dealer-or-catalogue`.
The last two are marked wherever they appear. `scholarly-coinage` covers names an
excavator or a philologist invented — the type an archaeological culture name
normally takes (§9.9 of this document), and one that site names take often enough
that the field cannot be left to a default.

**The identification claim is the load-bearing part.** That a name in a text
denotes a place on the map is a claim with a status, a proposer, evidence,
rivals and a falsifier — not a property of either the text or the place.

- A Place may not carry a name sourced from a text unless an
  `identification_claim` exists linking them, and the map label renders **the
  identification's status**, not the place's.
- An identification claim is a **bridge** under §4.4 whenever its endpoints sit in
  different domains — a lexeme (language) identified with a place (artifact or
  polity domain, by `place_class`) is a bridge and inherits every bridge
  requirement: a non-restating mechanism, non-empty alternatives including the
  null, a status ceiling of `PROVISIONAL` on correlational evidence, endpoint
  domains rendered, and no transitive inheritance (§7 of this document).
- Where an identification is disputed, the place carries `positional_certainty =
  disputed-location` and each candidate is its own Feature (§2.3 of this document).

The register's live case is the Rigvedic hydronyms. `DME-015` (`VERIFIED`) counts
31 named rivers over 251 `RIVER`-typed occurrences; `DME-016` records that nine
of the 31 occur only inside RV 10.75; `DME-018` records that several are not even
lemmatised under themselves, *Sarasvatī* sitting under the masculine stem
*sárasvant-* and *Asiknī* under *ásita-*. Every one of those 31 is a name in a
transmitted text. **Not one of them is a located place in this record**, and the
step from the first to the second is an identification claim that has not been
made here. A build that let a hydronym become a river label would have made 31 of
them silently.

### 3.5 Excavation coverage is a required field, not a nice-to-have

§6.3: *"Excavation coverage is displayed on every place, because it is the
denominator for every absence argument made about it… A place with 2% coverage
and a place fully excavated do not produce the same silence."*

Coverage record: `coverage_id` · `method` (`excavation` · `systematic-survey` ·
`remote-sensing` · `surface-collection` · `none-recorded`) · `extent_surveyed`
(a geometry under §2.2 of this document, or `unquantified`) · `fraction_of_extent` (or
`unquantified` with a reason) · `date_range` · `agent` (`mk:agt:`) ·
`publication` (`mk:src:`) · `unpublished_excavation` (boolean) · `notes`.

Rules:

- **`none-recorded` is a value and must be selected**, with a source for the
  statement that no coverage is recorded. It is not the empty state.
- **Unpublished excavation is coverage that produced no public record**, and it
  is typed as such: it changes `NOT EXCAVATED` into `NOT PUBLISHED`, which is a
  different absence with a different addressee (§3.7).
- **The coverage overlay is available on every view that draws finds** (§8.2),
  and any absence argument made on the map resolves to the coverage records that
  bound it.

### 3.6 External concordance

A Place may carry `same_as[]` links to external gazetteers and site registers.
Each is a `mk:rel:` with a status, because *"this excavation report's site X is
that gazetteer's entry Y"* is a claim, it is sometimes wrong, and it fails
silently: an incorrect concordance produces a plausible record rather than an
error.

Rules: the external identifier is stored with its scheme and its retrieval date;
the external record's own coordinate is **not** ingested as an Extent Assertion
unless its source and certainty are ingested with it; and a chain of `same_as`
links is **not** traversable (§7.4 of this document) — A `same_as` B and B
`same_as` C does not give A `same_as` C, because a wrong link anywhere in a chain
silently merges two places and nothing downstream can detect it.

### 3.7 Split, merge, re-localisation

Because places are revised more than any other object, the three revision cases
are specified rather than left to §3.6's general append-only rule.

- **Re-localisation** — same place, new evidence about where it is. A new Extent
  Assertion is appended; the old one is retained with its `contested_by` filled;
  the identifier does not change. This is why keys carry no geography (§2.1).
- **Split** — one record turns out to be two places. Two new identifiers are
  minted; the original is tombstoned with a `mk:cor:` and resolves to both, with
  the reason. **The original identifier is not reassigned to either child**, even
  where one child holds most of the evidence, because a citation of the original
  cannot be silently redirected to a narrower claim.
- **Merge** — two records turn out to be one place. A new identifier is minted;
  both originals tombstone to it. The merged record carries both name sets and
  both extent histories, and the merge itself is a claim with evidence.

In all three cases every published identifier still resolves, per §2.1, and the
tombstone states what happened, when, under which correction and to what.

### 3.8 `place_class` and `place_type` are different fields, and conflating them is easy

- **`place_class`** is on the **Place**: what kind of place it is —
  `settlement` · `findspot-only` · `cemetery` · `production-site` · `region` ·
  `water-feature` · `route-node` · `unknown-locus` · `holding-institution`.
- **`place_type`** is on the **Place Assertion** (§2.8): what an *object's*
  relation to that place is — `findspot` · `production` · `use` · `deposition` ·
  `discovery` · `current-holding` · `attributed-provenance` · `unlocated`.

One place can be the `findspot` of one object, the `attributed-provenance` of
another and the `current-holding` of a third. §2.8's rule stands and is repeated
here because the Atlas is where it is broken: *"a findspot and an attributed
provenance are never the same marker"*, and `attributed-provenance` is *"where
looted material announces itself, and collapsing it into `findspot` is how a
collection launders provenance."* The Atlas therefore renders the two in visually
distinct registers at every zoom, and a filter that hides `attributed-provenance`
reports it in the exclusion set like any other filter (§8.5 of this document).

---

## 4. Time — signed structured dates

### 4.1 The storage rule

**Every absolute date is stored as a signed integer year in proleptic Gregorian
astronomical numbering, where year 0 is 1 BCE and −1 is 2 BCE.**

The BCE/CE pair with a positive integer is a **display rendering**, computed at
the edge from the signed value, and is never the stored form. The conversion is
one line in each direction and is stated here so that no implementation has to
choose it: display era is BCE where `signed_year ≤ 0`, and the displayed number
is `1 − signed_year`; CE otherwise, displayed as `signed_year`.

The reason is that the conventional numbering has no year zero, so every interval
crossing the boundary needs a special case, and a special case that is applied in
one place and not another produces a one-year error that is invisible until it
lands next to a radiocarbon range. Astronomical numbering exists so that
subtraction, sorting, bucketing and axis placement need no special case at all.
**No arithmetic anywhere in the Atlas operates on the BCE/CE display pair.**

### 4.2 `DateValue` and the Date Assertion

The framework specifies the Date Assertion (§2.7):
`assertion_id` · `date_type` · `earliest` · `latest` · `calendar_or_scale` ·
`basis` · `method` · `source_id` · `locator` · `confidence` · `contested_by[]`,
with `date_type` from the twelve — composition · attestation · copying ·
redaction · translation · excavation · publication · modern interpretation ·
manufacture · deposition · scientific determination · calibration.

This document specifies `earliest` and `latest` as a **`DateValue`**, not an
integer:

| Field | Notes |
|---|---|
| `signed_year` | Integer, astronomical numbering (§4.1 of this document). Null only where `scale = relative-ordinal` or `undated` |
| `precision` | `year` · `decade` · `quarter-century` · `century` · `half-millennium` · `millennium` · `era-only`. **A bound is never more precise than its source** |
| `scale` | `proleptic-gregorian-astronomical` · `julian` · `cal-BCE-CE` · `cal-BP` · `uncal-BP` · `relative-ordinal` · `undated` |
| `source_notation` | The date **as the source wrote it**, verbatim, including its own era marker, its ± and its qualifiers |
| `converted_by` | The rule or agent that produced `signed_year` from `source_notation`, or `not-converted` |
| `qualifier` | `none` · `circa` · `no-earlier-than` · `no-later-than` · `floruit`. `circa` is not a widening of the bounds; the bounds are the bounds, and `circa` records that the source hedged |
| `open` | `none` · `open-before` · `open-after`, with a required `open_reason` |

**`source_notation` is required and is never discarded.** A date that has been
normalised and had its original notation dropped cannot be re-checked, and the
re-check is the whole point: `DE-M-026` (`VERIFIED`) records instruments made
across 114 years, from Arnold 1905 to a 2026 build, and their conventions are not
the same conventions.

### 4.3 Radiocarbon is handled as radiocarbon

- **`uncal-BP` is never converted to a signed year.** It is displayed as BP with
  its laboratory code and its ±1σ, and it does not appear on the calendar axis at
  all. An uncalibrated determination placed on a calendar axis is a fabricated
  date.
- **`cal-BP` and `cal-BCE-CE` carry the calibration curve and its version, the
  program and its version, and the reported probability interval (1σ or 2σ, and
  which).** Two determinations calibrated on different curves are not
  comparable without saying so, and the record says so by carrying both.
- **BP is stored with its reference epoch** (1950 CE) explicitly, never as a bare
  number, because "BP" without its epoch is
  a half-century offset waiting to be applied twice or not at all, and an
  unattributed dataset gives a reader no way to tell which happened.
- A calibrated range is **not** a uniform bar. Where the source publishes a
  probability distribution, the Atlas may render it as a distribution and must
  name the curve; where it publishes only an interval, the Atlas renders an
  interval and does not smooth it into a curve it was not given.

### 4.4 Relative-only chronology gets its own axis

Some of this repository's best-evidenced chronology is **relative and has no
absolute anchor at all.**

`DE-M-027` (`VERIFIED`): *"The attestation dates that would date the languages
themselves — Proto-Dravidian, the Munda arrival, the Rigvedic strata in absolute
years — cannot be established from anything retrieved in this session."* Its note
records that the chronology gate is *"passed only in its relative form, on
Arnold's strata, and is single-sourced there"* (`DEP-001`). The strata themselves
— Archaic, Strophic, Normal, Cretic, Popular — order a great deal of registered
material: `DE-M-012`, `DME-008`, `DME-009`, `DME-010`, `VAR-005`, and the
`arnold_stratum_code` column on all 103 rows of `rigveda-pur-passages.csv` and on
469 hydronym occurrences.

**And the corpus carries a second ordering, which is a separate instrument.**
`DME-011` and `DME-012` are **not** Arnold-strata rows: `DME-011` opens *"The
second instrument, book order, also returns a null"*, and `DME-012` is a
vocabulary-renewal test over books. The inherited standing rule that governs them
(`00-CONTROLLER/RESEARCH-CONSTITUTION.md` standing rule 1, from correction
`C-05`) is that *"Two chronological instruments (metrical stratum, book order)
are reported together; neither is used alone for a directional claim."*
`ordering_id` is therefore **not singular**: where a corpus carries two
orderings, the ordinal track renders both, neither is the default, and a claim
ordered by only one of them says which. A track showing Arnold's five bands alone
would be using one instrument alone, which is what `C-05` corrects.

**A `relative-ordinal` date may not be placed on the absolute axis.** It carries
`ordering_id` (the named ordering — here, Arnold's five strata), `ordinal_position`,
`ordering_source` and `no_absolute_anchor = true`, and it renders on a **second,
separately labelled ordinal track** with its ordering named on the track itself.

Two consequences that are the reason for the rule:

1. **The ordinal track cannot be dragged onto the calendar track**, by a visitor
   or by a filter. There is no interaction that produces an absolute date from a
   relative one, because there is no evidence in the record that would produce
   one.
2. **Each ordering is labelled with its own source and is single-sourced until
   it is not.** Arnold 1905 is the sole source for the metrical strata
   (`DEP-001`), so that track carries its source and its date, and every object
   on it inherits `PROVISIONAL` at best on chronological grounds. A visitor who
   sees five ordered bands and does not see that one 1905 metrical analysis
   produced all five has been misled by a layout.
3. **Where two orderings exist, neither may be shown alone as the chronology.**
   The track renders both, labelled, and a claim ordered by only one says which
   — `C-05`'s rule as a rendering constraint rather than a reporting habit.

### 4.5 Arithmetic, sorting, open bounds

- **Interval arithmetic runs on `signed_year` only.** Duration, overlap,
  containment and gap are integer operations, and the display conversion happens
  after.
- **Sort key is `(signed_year, precision_width)`.** Two dates with the same
  signed year and different precision are not equal and do not collate together:
  "the third millennium BCE" and "2500 BCE" are different assertions.
- **Comparison across scales is refused, not coerced.** An `uncal-BP` value and a
  `cal-BCE-CE` value do not sort against each other; the interface shows them in
  separate registers and says why.
- **A null bound is invalid.** Where a bound is genuinely open, `open` carries
  `open-before` or `open-after` with a reason, and the renderer draws the bar as
  open-ended rather than running it to the edge of the axis. A bar that stops at
  the axis edge asserts the axis edge.

### 4.6 The time control

§8.2 and §2.7 already require that the control name its date type. Four
buildable consequences:

1. **The control's current `date_type` is displayed at all times**, and changing
   it re-queries. A default is permitted; a silent default is not (§2.7).
2. **Objects with no assertion of the selected type are not dropped.** They move
   to a labelled **no-assertion tray** that is part of the view, is counted in
   the view's readouts, and is exported in the exclusion set (§5.2, §8.5 of this
   document). This is the negative-evidence standard applied to a slider: a
   control that silently removes everything lacking a composition date produces a
   cleaner and emptier map, and neither the cleanness nor the emptiness is a
   finding.
3. **An object with several assertions of the selected type appears across the
   union of their spans with the uncertainty drawn** (§8.2), not at a midpoint
   and not at the narrowest span.
4. **The ordinal track is always visible when it is populated**, because hiding
   it is how relative-only material disappears from a chronology and then
   reappears in a summary as though it had been dated.
5. **An object with a Place Assertion and no Date Assertion of any type is
   `undated`, and `undated` is a state rather than a gap.** It sits in the
   no-assertion tray under every setting of the control, and it reaches the map
   only through an explicit, labelled *show undated objects* control, drawn with
   an undated marker that no time filter narrows. It is never quietly included in
   a period view and never quietly dropped from one. This is not a corner case in
   this record: it is the state of the only place-anchored dataset the
   repository holds (§9.2 of this document).

---

## 5. Route objects

### 5.1 Why a route is its own record, and the alternative

The framework's predicate vocabulary already has `on-route-between` (§4.3,
spatial group), so a route could be modelled as a Relationship Object with two
endpoints. **That is the alternative, and it is stated at equal seriousness
because it is genuinely simpler and adds no code to §2.1's identity table.**

It is rejected here for one reason: a route is not a two-place relation. It has
an ordered waypoint sequence, each waypoint with its own evidence and its own
date; it has a path whose evidential status is different from its endpoints';
it has a direction question that is separately evidenced; and it has a period
over which it operated that is not the period of either endpoint. An edge with
`subject` and `object` cannot hold an ordered sequence of independently evidenced
intermediate nodes, and modelling one as a chain of edges reintroduces exactly
the transitive traversal §7 of this document exists to prevent.

**The specification is written so that either modelling works.** Every field in
§5.2 of this document is a field either way; under the fallback they are fields on a Relationship
Object with a `waypoints[]` extension, and `mk:rte:` is not allocated. The choice
is **`D-054`**. This document builds under the default that `rte` is allocated,
and says so.

### 5.2 Fields

| Field | Notes |
|---|---|
| `id` | `mk:rte:<key>` (or the fallback under `D-054`) |
| `revision` | append-only |
| `label` | An editorial name, logged as `mk:dec:`. **Not an ancient name** unless a name assertion and an identification claim exist (§3.4 of this document) |
| `origin`, `destination` | `mk:plc:` references with their own Place Assertions and certainties. Both required |
| `waypoints[]` | Ordered. Each: `mk:plc:`, `sequence_index`, `waypoint_basis`, `evidence_links[]`, `date_assertions[]`, `certainty`. **A waypoint with no evidence link is not a waypoint** |
| `directionality` | `origin-to-destination` · `bidirectional` · `direction-unknown`. §5.5 of this document |
| `date_assertions[]` | When the route is asserted to have operated. Typed (§4.2 of this document). **Not** the dates of its endpoints |
| `path_geometry` | `LineString` · `MultiLineString` · `Polygon` (corridor) · **absent**. Which of these is legal is decided by `route_uncertainty`, §5.3 |
| `route_uncertainty` | The six values, §5.3 of this document. Required |
| `movement_evidence[]` | `mk:evd:` establishing that something moved: `same-material-source-as`, `traded-along`, or a `made-at` ≠ `found-at` pair. **What moved is named** |
| `mechanism` | Required, per §4.4 rule 1 for anything implying transfer. May not restate the correlation |
| `alternatives[]` | Rival routes and the null (no route; the two assemblages are independent). Non-empty |
| `barriers[]` | `mk:rel:` `separated-by-barrier` relations the route crosses, with what made them passable and when |
| `status`, `attestation_mode`, `strength` | As §4.2 of the framework |
| `falsifiers[]` | Non-empty (§3.9) |
| `sources[]` | `mk:src:` resolving in the access ledger, with locators and independence groups |
| `language_evidence_state` | The four-value field (§6 of this document). Required on a route as on any other place-evidence structure |
| `bridge_type` | Derived from the endpoint domains. Non-null wherever the route is used to support a claim in another domain |

### 5.3 `route_uncertainty` — the field that decides whether a line may be drawn

This is the route object's load-bearing field. A drawn line asserts every
kilometre under it, and the case the field is built around is the one where the
endpoints are evidenced and the path is not.

| Value | What is evidenced | Legal `path_geometry` | Render obligation |
|---|---|---|---|
| `endpoints-evidenced-path-unevidenced` | Two places, and something that moved between them. Nothing about how | **No `LineString`.** Optionally a `Polygon` corridor with `geometry_semantics = analyst-drawn-extent` | Endpoints drawn, movement stated, **path drawn as absent**. If a corridor is shown it is labelled as the analyst's terrain envelope, with the analyst named (§2.4 of this document) |
| `waypoint-evidenced` | ≥1 dated intermediate place with its own evidence | `MultiLineString` through evidenced waypoints only | **Gaps are drawn as gaps.** No interpolation, no smoothing, no spline (§5.4 of this document) |
| `physically-traced` | A surveyed and dated physical feature — road, canal, cairn line, tow-path | `LineString` · `MultiLineString` | Drawn as a line. The survey and its date are named; the *dating of the feature* and the *survey of the feature* are separate Date Assertions |
| `documented-itinerary` | A text names the stages | `MultiLineString` over the stages that have identification claims | Each stage identification is its own `mk:clm:` with its own status (§3.4 of this document). The text's date, author and genre are shown: **an itinerary is a claim by its author, not a map** |
| `modelled-least-cost` | A computed path | `LineString`, marked as derivative | A derivative asset under §3.12: the model, the terrain data, the cost function and the parameters are named, and it **may not be published while the claim it depicts is `INHERITED-UNVERIFIED` or `HOLD`**. Rendered visibly distinct from every evidenced path |
| `proposed-only` | A named proposal in the literature | The proposal's own line, as a derivative of that publication | Drawn in the proposer's name with the date of the proposal (§2.6's obligation for `proposed`), never in the institution's |

**Two routes with the same endpoints and different uncertainties are two routes**,
not one route with a range. They are drawn as two, with their sources.

### 5.4 The interpolation ban

**No renderer may interpolate a path.** No splines, no smoothing, no
great-circle fill between waypoints, no snapping to a modern road network, no
"as the crow flies" default. Where a segment is unevidenced it is drawn as
unevidenced.

This is Rule S-5 in its sharpest form. Interpolation is the map's version of the
transitivity failure at §7 of this document: it derives the middle from the ends. The register
already contains a measured demonstration that a geometric convenience applied
between two exactly-known points introduces error that nobody sees — `DMB-014`
(`VERIFIED`, `SRC-050`), where flat-degree distance overstates great-circle
distance by up to +13.7% and, crucially, *"its error is not evenly
distributed"*: the distortion was largest for the language the argument was
about. A smoothing that is worse where the claim is strongest is the general
shape of this failure.

### 5.5 Direction is a separate claim

A route's `directionality` is evidenced separately from its existence, and
`direction-unknown` is the default until it is.

- Material found at B and made at A evidences **movement of that material A→B**.
  It does not evidence a route in the reverse direction, a return flow, or a
  repeated traffic — those are three further claims.
- `direction-unknown` edges are **off by default in every view** and reachable
  by an explicit control naming what it turns on (§4.5). An arrowhead is a
  claim; a line without one is a different, weaker claim; and a renderer that
  adds arrowheads for legibility has upgraded every route in the view.
- **A route's direction never transfers to anything travelling on it.** That a
  material moved A→B does not evidence that a practice, a word, a person or an
  ancestry component moved A→B. Each is a bridge and each is blocked from
  inheriting the route's direction by §7 of this document.

### 5.6 What routes exist in this record today

**None.** No `mk:rte:` can be created from any registered claim in
`03-REGISTERS/` at the time of writing, and the position is worth stating
precisely because a route layer is the easiest thing to populate badly.

The nearest thing in the record is inherited: `IH-060`
(`INHERITED-UNVERIFIED`) reports the owner's visual-concept document citing
*"140 sites, 299 dated object-windows, 25 localised texts and seven trade
routes"*, against `VELI-03`'s 194 site records and 315 class-windows —
part of contradiction `X-01`. Those seven trade routes are **a claim about a
prior document**, not seven routes. Under Rule S-1 they enter as
`INHERITED-UNVERIFIED`, and under `CLAUDE.md`'s inheritance rule only a
retrieval promotes them. Constitution §4R (materials and corridors) and §4S
(Meluhha, Marhaši, Magan, Dilmun) are the research agenda that would produce
real ones, and neither has been run in this repository.

---

## 6. Requirement REQ-1 — the language-evidence state on every place-evidence link

### 6.1 The Place-Evidence Link

Constitution §13 requires that clicking an artifact state what it supplies for
language. §8.6 specifies the four states. This section specifies the record the
field lives on, because "on every artifact" is ambiguous in a system where one
artifact has several relations to several places, and the answer can differ
between them.

**The field lives on the Place-Evidence Link**: the record joining one evidence
object to one place under one place type. A seal made at A and found at B has two
links, and what it supplies for language is not necessarily the same at both.

| Field | Notes |
|---|---|
| `link_id` | `mk:rel:<key>` — a Relationship Object with a place on one end |
| `evidence_id` | `mk:evd:` |
| `place_id` | `mk:plc:` |
| `place_assertion_ref` | `mk:evd:<key>#plc-<n>` — which of the object's Place Assertions this link renders |
| `place_type` | The eight (§2.8) |
| `geometry_ref` | The Feature drawn for this link (§2.2 of this document) |
| `positional_certainty` | §2.3 of this document |
| `date_assertion_refs[]` | Which Date Assertions position this link in time, typed |
| **`language_evidence_state`** | **Required, non-null, one of four, derived not entered** — §6.2–§6.4 of this document |
| `also_true[]` | The other states that also hold, §6.4 of this document |
| `state_basis[]` | The Evidence Links and Relationship Objects the derivation consumed. Non-empty |
| `state_derived_at` | Timestamp of the last derivation, and the derivation-rule version |
| `state_review` | Editorial confirmation record: reviewer, date, and **agreement or dissent** — §6.3 of this document |

### 6.2 The four states, restated as derivation conditions

Constitution §13's four, in §8.6's terms, written as conditions a machine can
evaluate:

| State | Condition | What the surface says |
|---|---|---|
| `supplies-linguistic-evidence` | The evidence object has an Evidence Link with role `attests` or `supports` to a claim whose domain is `language`, **and that claim's status is above `HYPOTHESIS`** | Shows the linguistic claim, the reading, the edition and the alternative readings. §8.6: *"The reading is itself a claim with a status; a disputed reading does not upgrade to evidence"* |
| `demonstrates-material-movement` | The object supports a `same-material-source-as` or `traded-along` relationship, or has a `made-at` Place Assertion different from its `found-at` Place Assertion, and that difference is itself statused | Shows the movement of the material and states **that the movement of a thing is not the movement of a language or of a people**. Offers the statused bridges if any exist |
| `provides-contact-setting-only` | Its links to language-domain claims are `contextualises` only | Says so in those words, shows what contact it makes possible, and states explicitly that possibility of contact is not evidence of contact. **Cannot contribute to a transition's `earliest_evidence`** (§8.5) |
| `provides-no-language-evidence` | None of the above | Says so plainly and **stays on the map** |

The status floor in the first row is not an addition to §8.6; it is §8.6's own
sentence made operable. Without it, "bears writing" would be sufficient, and
every undeciphered inscribed object in South Asia would be classified as
supplying linguistic evidence.

### 6.3 Derived, not entered

**No editor can set `language_evidence_state`.** It is recomputed from the
object's Evidence Links and Relationship Objects by a published function whose
inputs are exported (§5.3 rule 5). This mirrors §3.2's rule that status is
recomputed and *"the editorial CMS has no status dropdown"*, and it exists for
the same reason: a field that can be typed is a field that records an opinion
about what an object shows, and the whole purpose of REQ-1 is that the answer be
forced by the links.

Editorial review remains, and it is a check, not an override:

- `state_review` records a reviewer's **agreement or dissent** with the derived
  value.
- **A dissent does not change the field.** It opens a `mk:cor:` against the
  underlying links, because if the derived state is wrong then one of the links
  is wrong, and that is where the repair belongs. A reviewer who believes an
  object supplies linguistic evidence must produce or correct the Evidence Link
  that would make it so.
- Unreviewed derivations render normally. The derivation is the assertion; review
  is an audit of it.

**A link with no derivable state does not render.** If `state_basis[]` would be
empty — the object has no Evidence Links at all — the derivation returns
`provides-no-language-evidence` with `state_basis` naming the absence of links,
which is a true and useful answer. There is no null state and no "pending" state.

**"Not enterable" is true of the field and would be false of the answer, so it is
stated narrowly.** An editor cannot type the state; an editor *can* author and
change the Evidence Link roles the derivation consumes, and a role changed from
`contextualises` to `supports` moves the state. The field is therefore **not
directly enterable**, and the indirect route is audited: **any change to a link
role that moves a `language_evidence_state` requires a `mk:cor:` and appears in
the link's `state_basis` history with the prior value, the new value and the
reason.** REQ-1 closes against a typo by construction and against intent by
audit, and the difference is worth stating rather than eliding.

### 6.4 Exhaustive, mutually exclusive, and the facts that would otherwise be lost

§8.6 requires the four to be exhaustive and mutually exclusive. Objects do not
oblige: an inscribed seal made at one place and found at another satisfies the
first and the second conditions at once.

**Precedence** for the headline field, highest first:

1. `supplies-linguistic-evidence`
2. `demonstrates-material-movement`
3. `provides-contact-setting-only`
4. `provides-no-language-evidence`

**`also_true[]`** carries every other state whose condition holds, so exclusivity
costs no information. The panel reads *"Supplies linguistic evidence. Also
demonstrates material movement."*

**Clicking an artifact, not a link.** Constitution §13 and framework §8.6 put the
answer on the *artifact*, and an artifact with a `made-at` link and a `found-at`
link has two. The **object-level headline is the highest-precedence state across
all of that object's Place-Evidence Links**, computed by the same function; each
link keeps its own state, and selecting a link shows that link's state beside the
object's. The panel therefore reads *"This object: demonstrates material
movement. At this place: provides no language evidence."* Checked by
`CHK-REQ1-8`.

Two rules keep precedence from being used as a dial:

- **The headline may never sit lower in the precedence than a condition that
  holds.** An object that satisfies condition 1 cannot be presented as
  contact-setting-only. This blocks downgrading a linguistically awkward object
  into the background.
- **The headline may never sit higher than the links support.** This blocks the
  upgrade, which is the failure §13 was written against.

**The disputed or unread reading, which the four states do not distinguish.** An
object whose only language link is `attests` or `supports` to a claim at or below
`HYPOTHESIS` fails condition 1 on the status floor, fails condition 2 if it has no
movement pair, and fails condition 3 because that requires `contextualises`-*only*
links. It falls to `provides-no-language-evidence` — which is the right headline
(no reading of it is a claim the institution can stand behind) and a misleading
one if left bare, because the object plainly bears a form. Two consequences:

- The state carries a **required reason code** where it applies:
  `unread-or-disputed-reading`, with the below-floor claims named. The panel says
  *"provides no language evidence: it bears a form, and no reading of that form is
  a claim above `HYPOTHESIS`"*, and offers the competing readings with their
  statuses.
- **Objects carrying that reason code are excluded from the §6.6 distribution
  guard's count**, in both numerator and denominator. Otherwise a curator could
  satisfy a guard designed to measure honest emptiness by accumulating disputed
  readings, which is the opposite of what the guard measures.

§6.5's seal escapes this only because it happens to have a `made-at` ≠ `found-at`
pair. An undeciphered inscribed object found *in situ* has no such pair, and it
is exactly the case this rule is for.

### 6.5 The worked case that decides the design

An **undeciphered Indus seal found in Mesopotamia**.

- It bears writing. It is therefore linguistically *interesting*.
- Its reading is not a claim above `HYPOTHESIS` — no reading is. Condition 1
  fails.
- It has a `made-at` ≠ `found-at` pair, statused. Condition 2 holds.
- **Derived state: `demonstrates-material-movement`.** `also_true`:
  `provides-contact-setting-only` if `contextualises` links to language claims
  exist.
- The panel says what moved, and says that the movement of a thing is not the
  movement of a language or of a people.

This is the single case the whole field exists for, and the record already refuses
the shortcut in prose: `BR-E-005` (`03-REGISTERS/CROSS-DOMAIN-BRIDGES.csv`)
records the bridge *"a substrate donor in the northwest → the language of the
Indus civilisation"* as **NOT CROSSED**. REQ-1 is that refusal made structural, so
that it survives a data import, a contractor, and a redesign.

### 6.6 The distribution guard

§8.6: *"This state must be common and must be visible. An Atlas in which every
artifact turns out to be linguistically meaningful is an Atlas that has been
curated into an argument."*

A requirement that a value be *common* cannot be enforced per object. It is
enforced on the view:

- **Every Atlas view's legend carries the distribution of the four states across
  the objects in view**, as counts, beside the layer status distributions §8.4
  already requires. It is a *distribution readout* under §8.5 rule 4 of this
  document — bound to the view, carrying its definition string and its exclusion
  count, never a heading and never a single number.
- **A view in which `provides-no-language-evidence` is zero raises a review
  finding.** Not an error and not a block — it can be legitimate for a
  deliberately narrow filter — but it is written to `04-AUDITS/` as a finding to
  be dismissed with a reason, and a *published default view* with a zero there is
  a bias-log entry under §3.11.
- **The per-object states are exported with the view** (§5.2), so the shape of
  the Atlas's language claims is recomputable by someone who does not trust the
  Atlas — which is stronger than exporting the shape and asking them to trust the
  arithmetic.

### 6.7 Where it appears

Per §8.6 the state is *"displayed on hover/selection, not hidden in a detail
pane"*, and it is a search facet (§7.2). Adding to that:

- It appears in the **Atlas view export** (§5.2) on every object, with
  `also_true[]` and `state_basis[]`.
- It appears on **routes** (§5.2) as on any other place-evidence structure.
- It is **not** a filterable-away default: a filter on
  `language_evidence_state` reports its exclusions like any other filter (§8.5
  of this document), so a view showing only linguistically meaningful objects
  announces that it is one.

### 6.8 What is checked

`CHK-REQ1-1` Every Place-Evidence Link has a non-null `language_evidence_state`
from the four-value enumeration. · `CHK-REQ1-2` Every state has non-empty
`state_basis[]`. · `CHK-REQ1-3` No state was written by an editor: every value's
provenance is a derivation record. · `CHK-REQ1-4` For every link, the headline is
the highest-precedence condition that holds, and `also_true[]` contains the
rest. · `CHK-REQ1-5` No `supplies-linguistic-evidence` rests on a language claim
at or below `HYPOTHESIS`. · `CHK-REQ1-6` No `provides-contact-setting-only` object
appears in any transition's `earliest_evidence`. · `CHK-REQ1-7` Every published
default view has a non-zero `provides-no-language-evidence` count, or a logged
dismissal, computed **excluding** objects carrying the
`unread-or-disputed-reading` reason code. · `CHK-REQ1-8` Every evidence object
with more than one Place-Evidence Link has an object-level headline equal to the
highest-precedence state across its links, and the panel shows both the object's
headline and the selected link's state. · `CHK-REQ1-9` Every link-role change
that moved a `language_evidence_state` carries a `mk:cor:` and a `state_basis`
history entry.

---

## 7. Requirement REQ-2 — transitive closure is disabled across the seven domains

### 7.1 What is being prevented, in both directions

§4.4 rule 5 names the failure: *"the mechanism by which a map of trade goods
silently becomes a map of languages."* The chain is short and each link is
individually defensible —

> a bead type moves along a route (**artifact**) → the route lies within a
> polity's control (**polity**) → that polity's inscriptions are in a language
> (**language**) ⇒ the bead distribution is a language distribution.

Nothing in that chain is a lie. The conclusion is not entailed by any of it, and
no surface asserted the conclusion; the map drew it.

**The same mechanism runs the other way**, and the specification is worthless if
it only blocks one direction:

> the Indus assemblage is an archaeological culture (**artifact**) → that culture
> is identified with a population (**ancestry**) → that population is identified
> with a language family (**language**) ⇒ the Indus script is that family's.

Each link in *that* chain is registered as refused, and by the right row:
`BR-E-004` records *"a language family → a population"* as **NOT CROSSED —
DELIBERATELY**, which is the ancestry step; `BR-E-005` records *"a substrate
donor in the northwest → the language of the Indus civilisation"* as **NOT
CROSSED**, which is the conclusion; and `BR-E-003` records *"attested modern
distribution → prehistoric distribution"* as **EXPLICITLY REFUSED**. The mechanism below is symmetric and blocks both chains
by the same rule, which is the only way it can be trusted to block either.

### 7.2 Mechanism 1 — domain tagging is total

Every object carries a `domain` from the constitution's seven — `language` ·
`ancestry` · `culture` · `artifact` · `religion` · `polity` · `modern-identity`
— **or** the eighth non-domain value `apparatus`, for records that are not
assertions about the past: sources, agents, editorial decisions, obligations,
consents, corrections, rights records.

- **No object is domain-null.** A null domain is what makes a bridge invisible,
  because `bridge_type` is derived from the endpoint domains and a null endpoint
  derives nothing.
- **`bridge_type` is derived, never typed.** It is the ordered domain pair of the
  endpoints, computed at write time — `artifact→polity`, `ancestry→language`,
  `polity→modern-identity`. An author cannot omit it by forgetting it, and cannot
  suppress it by leaving it blank.
- **A relationship whose endpoints share a domain has `bridge_type = null`** and
  is an ordinary intra-domain edge.
- Objects that legitimately sit in two domains — a temple is `religion` and
  `artifact`; an inscription is `language` and `artifact` — carry a **primary
  domain** plus `secondary_domains[]`, and **`bridge_type` is derived
  pessimistically**: if any endpoint pairing across primary or secondary domains
  is a cross-domain pairing, the edge is a bridge. Dual membership is never a
  route around the rule.

### 7.3 Mechanism 2 — no transitive operator is exposed

**No rendering surface has access to a transitive-closure operation over the
relationship graph.** No recursive traversal, no path-finding, no reachability
query, no closure materialisation, no `*`-style repetition operator, no
adjacency-matrix product. The Atlas can ask *"which relationships have this
object as an endpoint"* and it cannot ask *"what is reachable from this
object"*.

This is the framework's *"database-level rule"* made concrete. It is stated as a
capability that is absent rather than a query that is forbidden, because a
forbidden query is one refactor away from being issued, and an absent capability
is not.

Where a transitive result is genuinely needed, §7.4 of this document governs.

### 7.4 Mechanism 3 — the traversal allow-list, and the terminal-edge rule

Some traversal is legitimate and the specification would be dishonest to pretend
otherwise. The genealogy tree §3.5 requires — *"nine citations converging on one
1953 excavation report is a shape the visitor should be able to see"* — is a
traversal. So is a custody chain, and so is a transmission chain from an
autograph through copies and translations to an edition.

Traversal is permitted **only** along this allow-list, and every predicate on it
is intra-domain or `apparatus`:

`depends-on` (source genealogy) · `copied-from` · `redacted-from` ·
`translated-from` · `transmits` · `derived-from` · `custody-transferred-to` ·
`supersedes` · `revision-of`.

Three conditions on every permitted traversal:

1. **The terminal-edge rule.** A traversal stops at the first edge whose
   `bridge_type` is non-null. **No path may contain a bridge edge and any other
   edge.** A bridge is always exactly one hop, always drawn as one hop, and never
   a segment of anything longer.
2. **The path is displayed as a path**, with every intermediate node visible and
   every edge's status shown. A traversal result is never collapsed into a direct
   relation between its ends. The genealogy tree is legitimate precisely because
   it shows the convergence rather than concluding from it.
3. **`same_as` is not on the list** (§3.6 of this document), and neither is any
   spatial predicate. Concordance errors and route segments compose in exactly
   the way the rule exists to stop.

**Routes are inside this mechanism, not outside it.** A Route is a multi-endpoint
object of this document's own invention (§5), and object-modelling relocates a
traversal rather than removing it, so three rules attach:

- **`bridge_type` on a Route is computed pairwise**, over every (origin,
  waypoint), (waypoint, waypoint) and (waypoint, destination) pair, not over a
  single "ordered domain pair" that a multi-endpoint object does not have.
  `CHK-REQ2-2` and `CHK-REQ2-4` read the pairwise set.
- **Routes are not composable.** Route A→B and route B→C do not give A→C, are
  never rendered as a continuous path, and no view offers an affordance that
  joins them. Two routes sharing an endpoint are two routes.
- **`Place.routes[]` is a one-hop index and carries no walk.** It is a derived
  read-only index (§3.2 of this document); it is not on the §7.4 allow-list, and
  no surface may follow it from a place to a route to another place to another
  route. Two sequential one-hop queries composed by a renderer are the
  reachability walk mechanism 2 says the Atlas cannot perform.

**Two bridge edges sharing an endpoint are not a chain, and are not drawn as
one.** §7.4's terminal-edge rule governs traversal results; two independently
authored bridges rendered in the same view produce the visual A→C with no derived
edge and no traversal at all. **No view may render two bridge edges sharing an
endpoint without the non-transitivity notice**, which names both domain pairs and
states that the institution has asserted no relation between the outer ends.

**And the one line this document permits that §7.5 would otherwise forbid.**
§5.3's `modelled-least-cost` path renders as a `LineString`. It is not a derived
*relationship*: it is a derived *asset* under framework §3.12, depicting a route
claim that already exists as a row, with its model, terrain data, cost function
and parameters named, visibly distinct from every evidenced path, and barred from
publication while the claim it depicts is `INHERITED-UNVERIFIED` or `HOLD`. §7.5 of this
document forbids rendering a relation nobody asserted; §3.12 permits depicting one
somebody did. The boundary is that a derived asset may depict an existing edge
and may never stand in for a missing one.

The experience object model's one permitted transitivity — Mission composition
(its §2.5) — is not an exception here and does not reach this graph. It traverses
*"this Mission contains this Activity"*, which its own text calls *"a fact about
a product, verifiable by inspection"*. Nothing in the Atlas traverses a
statement about the past.

### 7.5 Mechanism 4 — no derived edge is persisted or rendered

- **A derived relation is never written to the graph.** Nothing computes an A→C
  and stores it, not as a cache, not as a materialised view, not as a
  denormalisation for map performance.
- **A derived relation is never rendered on a public surface.** There is no
  "suggested connection", no "related via", no dotted line, no faint edge.
- **In the editorial environment**, a co-occurrence report is permitted as a
  *research prompt* — a queue item reading "A and C both relate to B; is there a
  relationship?" — and it carries no status, cannot be published, cannot be
  exported, and becomes a relationship only when someone evidences one
  independently and writes a `mk:rel:` row with its own sources, mechanism,
  alternatives and falsifiers.

### 7.6 Mechanism 5 — layers and filters cannot manufacture an edge

§8.4 already requires that co-displayed layers produce a stated *correlation*
rather than a relationship. Buildably:

- **The Atlas has no affordance that creates a connection.** No connect tool, no
  link mode, no lasso that groups selected objects into a relation. The only
  lines it can draw are `mk:rel:` rows and `mk:rte:` rows that already exist.
- **Co-selection of two layers renders the correlation notice**, which states
  that co-location is not a relationship and offers the statused bridges that do
  exist between the two, with their mechanisms and rivals. Where none exists, it
  says none exists — which, in this record, is what it would say for every pair,
  because all eight registered bridges are refusals (§9.12 of this document).
- **No layer may recolour, reshape or relabel another layer's objects** (§8.4).
  Recolouring is the visual form of the derived edge: it writes one layer's
  domain onto another layer's objects without an edge existing at all. The
  MATERIALS layer's constraint states it outright — *"May not be recoloured by
  any linguistic layer"* — and this document extends the prohibition to all
  pairs, in both directions, including a material layer recolouring a language
  layer.
- **Shared symbology across layers is a recolouring.** Two layers that use the
  same colour ramp keyed to the same categories have merged, whatever the toggle
  state says. Layer palettes are allocated so that no two layers share a scale.

### 7.7 Export closure

§5.2's Atlas view export carries *"every object in view with its assertions,
every excluded object with the reason it was excluded"*. Under REQ-2 it also:

- carries **only edges that exist as rows** — no computed adjacency, no
  reachability matrix, no path table;
- carries, on every edge, its `bridge_type` and **both endpoint domains**, so
  that a downstream user chaining edges does so with the domain boundary visible
  in their own data;
- carries a **header statement** naming the rule: that relationships in this
  export are not transitive, that a path through two edges is not a relationship,
  and that the institution has not asserted one.

The institution cannot stop a downstream user from chaining. It can refuse to
hand them a file in which the chaining looks pre-approved.

### 7.8 What is checked

`CHK-REQ2-1` Every object has a non-null `domain`. · `CHK-REQ2-2` Every relationship's
`bridge_type` equals the ordered domain pair of its endpoints, computed
independently of the stored value. · `CHK-REQ2-3` For every connection drawn in
any view, a `mk:rel:` or `mk:rte:` row exists with those endpoints; a drawn
connection with no backing row fails the check. · `CHK-REQ2-4` No traversal result
in any surface contains a path of length > 1 that includes an edge with non-null
`bridge_type`. · `CHK-REQ2-5` No persisted relationship has a provenance of
`derived`. · `CHK-REQ2-6` No two active layers share a colour scale keyed to the
same category set. · `CHK-REQ2-7` Every Atlas export carries endpoint domains,
`bridge_type` and the non-transitivity header. · `CHK-REQ2-8` No view renders two
bridge edges sharing an endpoint without the non-transitivity notice. ·
`CHK-REQ2-9` No route is rendered as continuous with another route, and no
surface traverses `Place.routes[]`.

`CHK-REQ2-3` is the one that catches the failure in practice, because it tests the
*rendering*, not the data. A build can hold a perfectly clean graph and still draw
a line, and the line is what the visitor sees.

---

## 8. Requirement REQ-3 — unknown stays drawn, and the Atlas carries no count

### 8.1 Unknown is a Feature with a record behind it

Specified at §2.5 of this document. Restated here as the requirement rather than
the geometry: **there is no state in which the Atlas represents "we do not know"
by drawing nothing.** Every unknown that the Atlas asserts is a `zone-unknown`
Feature with a non-null `mk:absence_ref` to an `mk:abs:` record carrying the
seven negative-evidence fields and one of the eight `absence_type` values, and a
typed `boundary_basis`.

§8.2's reason is the whole argument and is not improved by paraphrase:
*"Blank map is forbidden as a representation of unknown, because blank reads as
empty and empty reads as nobody."*

### 8.2 Render order, and what blank is reserved for

- **Blank means out-of-scope, and out-of-scope is drawn.** The Atlas declares its
  spatial scope as a polygon. Inside the scope polygon there is no blank: every
  point is inside a known extent, inside a `zone-unknown` extent, or inside a
  declared no-coverage extent. Outside it, the interface says the Atlas does not
  extend there, which is a statement about the Atlas and not about the past.

  **This document adopts here, and names what it narrows.** Requiring a declared
  scope polygon is not in the framework, and which region an atlas covers is an
  interpretive choice with visible consequences — a scope drawn to the seven
  settings of §8.3 already asserts that those seven are the relevant world. The
  adoption is narrow: **the scope polygon is a property of the build or the
  saved view, not a claim about a region.** It is displayed wherever the map is,
  it is logged as a `mk:dec:` with its reason and its decider, it is exported
  with every view, and it carries no status because it asserts nothing about the
  past. What region ships is an editorial decision in that register, adjacent to
  `D-022`; what this document fixes is only that the decision is declared rather
  than implied by where the tiles happen to stop.
- **Layer 11 is not occluded.** Where the unknown layer and any other layer
  overlap, the unknown remains legible at every zoom. It is not a background
  wash that opaque layers cover; a layer that can be painted over has been
  switched off by other means.
- **The enumeration order of the eleven layers is not a render order and not a
  priority.** Constitution §13 lists them in an order that begins with SOUNDS,
  WORDS and GRAMMAR and ends with UNKNOWN SPEECH ZONES. That is a list, written
  in a sentence; a build that took it as a z-order would paint the philological
  layers over the unknown, which is the exact inversion of §8.4's judgement that
  layer 11 *"is the layer that makes the other ten honest"*. Render order is
  specified as a separate decision under `D-022`, subject to the
  non-occlusion rule above.
- **Unlocated objects are visible off-map.** An object with
  `positional_certainty = unlocated` sits in a labelled tray that is part of the
  view, is counted in the view's readouts, and is exported. It has not been
  removed for lacking coordinates.

### 8.3 The layer-11 lock

§8.4: *"Layer 11 cannot be switched off while any language layer (1, 2, 3) is
on. Turning off the unknown while displaying the known is how a language map
becomes a claim about a continent."*

Buildably: the layer-11 toggle is **disabled with a stated reason** while SOUNDS,
WORDS or GRAMMAR is on — not hidden, not silently ignored, not re-enabled by a
URL parameter or an export filter. A visitor who wants layer 11 off turns the
language layers off first, which is the sequence the rule intends. The lock
applies to the shareable view state and to the export, so a saved or shared view
cannot carry a state the interface would refuse to produce.

### 8.4 Unknown is never a rival

§3.7: *"'Unknown' is never a rival… The comparison interfaces — PROVE IT (§9),
the Atlas transition panel (§8.5) — must not list 'unknown' as an option beside
named hypotheses."*

A transition's `alternatives[]` may not contain a member whose content is
"unknown", "unclear", "not established" or any equivalent. The absence of an
explanation is not an explanation, and rendering it as a fifth option in a list
of four gives it a share of the visual space that the record does not give it.
What *is* rendered beside the alternatives is the falsifier set and the absence
records — which say what would settle it and why nothing has, which is the honest
content that "unknown" was standing in for.

### 8.5 The count rule

The Atlas has no headline count (§8.1). The reason is on the record and is not a
matter of taste: `IH-250` (`INHERITED-UNVERIFIED`, contradiction `X-01`) records
six values across the project's own documents — **140** (live Enter and the
owner's visual document), **150** (MANIFEST and VELI-02), **158** (live Explore),
**167 rising to 175** (VELI-09 and the live page title), **194** (VELI-02 §6,
VELI-03, VELI-13) and **199** (site-class rows) — with the window count disputed
in parallel at 299 against 315 (`IH-060`). `IH-057` records three of those six
disagreeing **within the live site itself** — 140 on Enter, 158 on Explore, 175
in the page title — which is the form of the problem a visitor could already
see. The schema assessment's collision A
records 175 as *"adopted as settled fact, put in a page title, and rated
low-risk"*. `IH-270` records the resolution path — extract the atlas to JSON and
generate every figure from it — as an open work item, and `IH-329` records the
standing hold: *"Any page count, site count or corpus total in public copy until
Tier 0 items 2-7 are done."* `D-034` asks the owner what the count is and is
open.

Five structural rules, so that the Atlas can ship before `D-034` is answered:

1. **The title slot carries no count, total or superlative.** The Atlas
   surface's title, heading, breadcrumb, share card, social preview and meta
   description admit no cardinal number, no word numeral ("one hundred and
   seventy-five", "hundreds of"), no total and no superlative ("the largest
   atlas of…"). Checked by `CHK-REQ3-4`. A digit test was drafted first and is
   the wrong test twice over: it passes "hundreds of sites" and fails "Atlas
   v2".

   **Two framework rules bear on this and they point different ways, so both are
   cited and one governs.** `museum-framework.md` §8.1 states flatly that the
   Atlas *"has no headline count"*. `experience-object-model.md` §7.2 states the
   Exhibit rule as a conditional: a title *"may not contain a count, a total or
   a superlative **unless that number is itself a `presents` claim on this
   Exhibit**"* — that is, it permits a number that is a statused claim the
   Exhibit displays. **§8.1 governs for the Atlas surface**, because the
   condition EOM §7.2 attaches cannot currently be met: the only candidate
   number is under contradiction `X-01` with six values and `D-034` open, and
   `IH-329` records a standing hold on any site count in public copy. If
   `D-034` is answered and a count claim is created, EOM §7.2's conditional
   becomes available and this rule should be revisited rather than quietly
   kept. The tension is logged as `IC-X-002` in
   `04-AUDITS/INTERNAL-CONTRADICTIONS.csv`.
2. **Any number the Atlas displays is one of exactly two things**, and there is
   no third: (a) a **count claim** — a `mk:clm:` with a status, a definition of
   what is counted, an inclusion rule, sources and a falsifier, rendered as a
   claim with its status visible; or (b) a **view-cardinality readout**.
3. **A view-cardinality readout is bound to the filter that produced it.** It
   renders only inside the filter component, never in a heading; it carries its
   **definition string** (what is being counted) as a required property; and it
   is always accompanied by its **exclusion count** with a route to the exclusion
   set. "Showing 41; 55 excluded — see why" cannot be misread as a total in the
   way "41 sites" can.
4. **A distribution is a third thing, and the rule would contradict itself
   without saying so.** §6.6 of this document requires the four-state
   distribution in every legend, and framework §8.4 requires status distributions
   there. Those are counts, and rule 2 as first drafted would have rejected the
   numbers this document elsewhere mandates. A **distribution readout** —
   a breakdown of the objects in view across the values of one required field —
   is permitted in a legend on the same three conditions as a cardinality
   readout: bound to the view that produced it, carrying its definition string,
   and shown with its exclusion count. It is never a heading and never a single
   number. A distribution is a shape; a total is a claim.
5. **A view cardinality is never exported as a total.** §5.2's Atlas view export
   carries the filter state, the objects in view and the excluded objects with
   reasons. It does not carry a summary count field, because a summary count
   field in a CSV is a headline count that has escaped the interface. **A
   distribution is not exported as an aggregate either**: the export carries the
   per-object field values from which any distribution is recomputable, which is
   what makes it checkable rather than trusted.
5. **No count claim about the Atlas's contents may be created while `X-01`
   stands.** If the six values are shown at all, they are shown as the
   contradiction record: all six, with their sources, and the statement that the
   project's own documents disagree. That display is honest and it is not a
   count.

### 8.6 What is checked

`CHK-REQ3-1` Every `zone-unknown` Feature has a non-null `mk:absence_ref` resolving
to an `mk:abs:` record with all seven negative-evidence fields and a typed
`absence_type`. · `CHK-REQ3-2` No point inside the declared scope polygon is
outside every extent, unknown zone and declared no-coverage zone. ·
`CHK-REQ3-3` The layer-11 toggle is disabled in every view state, saved view and
export in which layer 1, 2 or 3 is on. · `CHK-REQ3-4` The title, heading, breadcrumb,
share-card, social-preview and meta-description slots of the Atlas surface
contain no cardinal number, word numeral, total or superlative. ·
`CHK-REQ3-5` Every rendered number resolves to one of exactly three things: a
`mk:clm:` count claim with a visible status, a filter-bound cardinality readout,
or a view-bound distribution readout — the last two each carrying a definition
string and an exclusion count. · `CHK-REQ3-6` No export contains a summary total
or an aggregated distribution; per-object field values are present instead. · `CHK-REQ3-7` No transition's `alternatives[]` contains an "unknown"
member. · `CHK-REQ3-8` Every unlocated object appears in the view's tray and in its
readouts.

---

## 9. The eleven layers

### 9.0 What a layer specification contains, and what "populatable today" means

Constitution §13 names eleven layers. §8.4 says what each one *is* in terms of
the object model and what it may not do; that table is not repeated. This section
adds, for each layer, the three things a builder needs: **the object types it
reads**, **the assertions it requires before an object can appear on it**, and
**which registered claims could populate it today and which could not.**

**"Populatable today" is a test with three conditions, all of which must hold.**

1. A row exists in `03-REGISTERS/` with a status **above `INHERITED-UNVERIFIED`**
   — because `CLAUDE.md`'s inheritance rule is that only retrieval promotes, and
   an Atlas built from the handoff would be the v1 page with better geometry.
2. Its `source_id` **resolves to a row in `02-SOURCES/access-ledger.csv`**.
3. It carries, or can carry without a new claim, **the assertions the layer
   plots**: at least one Place Assertion with a permitted geometry (§2.3 of this
   document) and at least one Date Assertion of the type the layer's time control
   filters on (§4.2 of this document).

Condition 3 is the one that fails. Almost everything in this repository satisfies
the first two and cannot satisfy the third, and saying so layer by layer is more
useful than a summary, because the *reasons* differ and some of them are
repairable and some are not.

Three findings recur and are stated once here rather than eleven times:

- **The pinned Rigvedic corpus carries no geography.** `PUR4J-018` (`VERIFIED`,
  `SRC-069`): constitution §4J's proposed geography field *"cannot be filled from
  the pinned corpus, which contains no geographic content of any kind."* Every
  textual, lexical and phonological measurement in this repository inherits that.
- **The corpus's only chronology is relative and single-sourced.** `DE-M-027`
  (`VERIFIED`) and `DEP-001`: Arnold 1905's five metrical strata, which order a
  great deal of registered material and anchor none of it to a year. Under §4.4
  of this document such material renders on the ordinal track, not the calendar
  axis.
- **The only place-anchored registered material in this repository is
  present-day, undated and single-sourced.** 47 Dravidian and 20 Munda attested
  lects with Glottolog coordinates (`DE-M-021`, `DE-M-022`, `VERIFIED`,
  `SRC-060`), and the 20 DravLex varieties (`DMB-008`, `SRC-050`) — which are the
  *same* Glottolog coordinates, per `DE-M-021`'s note and `DEP-027`, so the three
  rows do not add. None of them carries a date assertion: `DMB-008` reads
  *"nothing here dates anything"* and the `SRC-050` ledger row reads *"no date"*.
  And `BR-E-003` records the bridge from that distribution to a prehistoric one
  as **EXPLICITLY REFUSED**.

### 9.1 SOUNDS

**Reads:** `mk:clm:` in the language domain with `evidence_class = linguistic`;
`mk:rel:` with predicate `sound-correspondence-with`; `mk:evd:` linguistic
objects. **Requires to appear:** `attestation_mode` on every item, and — for any
item to appear *on the map* — a localisation that is itself a statused claim
(§8.4's constraint on this layer).

**Could populate today, as layer content:** the Rigvedic retroflexion measurements.
`DME-003` (2,666 retroflex segments over 10,031 lemma citation forms, 2,399 of
them derived by RUKI, nati or a retroflex cluster), `DME-004` (an **upper bound** of 253 lemmas, 2.52%,
carrying a retroflex the two regular rules do not derive, over 1,257 of 164,758
tokens), `DME-005`, `DME-006` (the commonest conditioning environments),
`DME-007` (every word-initial retroflex in the lemma inventory is `ṣ-`, and all
eight such lemmas are `ṣáṣ-` "six" or a compound of it), `DME-013` (the residue's
formal classes), `DME-014` (two lemmas removed from the residue as transparent
`√takṣ-` derivatives), all `VERIFIED`; `DME-019` and `DME-021`, `PROVISIONAL`;
and the 253 rows of `03-REGISTERS/domain-e-retroflex-residue.csv`.

**Could not populate:** **any of it on the map.** Not one of these claims carries
a Place Assertion, and none can acquire one without a localisation claim that has
not been made. RUKI and nati are rules of a transmitted corpus, not events at
coordinates. Chronologically they carry two relative orderings and no absolute
one — Arnold's strata (`DME-008` to `DME-010`) and book order (`DME-011`,
`DME-012`) — so they sit on the ordinal track under §4.4 of this document, on
both of its orderings and not on either alone.

**Verdict: populatable as content, zero map geometry.** The layer's first
honest state is a legend, a rule inventory and an ordinal track, and no marks on
the map at all. `DME-020` and `DME-021` (`PROVISIONAL`) are the layer's two
interpretive claims and both are *negative* — the proxy does not support
accumulation of non-Indo-Aryan material through the period, and the empty
word-initial position weighs against a retroflex-initial donor vocabulary — which
is content a map cannot draw and a panel can.

### 9.2 WORDS

**Reads:** `mk:lex:` with attested occurrences. **Requires to appear:** §8.4 —
plotted *"at the place and date of the attestation, not of the supposed
speaker"*, with the text's findspot and composition place both shown where they
differ.

**Could populate today, off the map:** the lexical inventory is substantial.
`DE-M-009` and `DE-M-010` (`VERIFIED`): of Turner's 224 CDIAL entries with a
Dravidian loan arrow and 55 with a Munda one, the headword occurs as a Rigvedic
simplex lemma in 15 and 5 cases respectively, collapsing to **15 distinct
lemmas**; `DE-M-011`: those 15 account for **21 tokens of 164,758, 0.013%**;
`DE-M-020`: two further candidates attested only inside compounds, with the
simplex/compound/derivative distinction kept separate. Plus the hydronyms —
`DME-015` (31 named rivers over 251 `RIVER`-typed occurrences, `síndhu-` alone
126), `DME-016`, `DME-017`, `DME-018`, and the 469 occurrence rows of
`domain-e-hydronyms.csv`. Plus `VAR-001` (23 tokens of `varṇa-`) and `VAR-007`
(23 more across 12 compound lemmas). Plus the `pur-` family corpus.

**Could not populate:** **none of it can be plotted.** The Rigveda has no
findspot and no established composition place in this record (`PUR4J-018`), so
the "place of the attestation" that this layer requires does not exist for any of
these lemmas. The 31 river *names* are the sharpest case: naming a river is not
locating one, and the step from a hydronym to a mapped channel is an
identification claim (§3.4 of this document) that has not been made here for any
of the 31. A build that let the hydronym list become a river layer would have
made 31 unstatused identification claims in one import.

**What can be plotted:** the present-day lect points — `DE-M-021` (47 Dravidian
lects, 66.56–87.64 °E, 9.59–29.04 °N), `DE-M-022` (20 Munda lects, 77.55–88.34
°E, 18.39–25.04 °N), `DMB-008` (the 20 DravLex varieties, Brahui both
northernmost and westernmost) — all `VERIFIED` against `SRC-060`/`SRC-050`. Two
constraints on them, both structural:

- **They are not points.** A Glottolog coordinate denotes a language, whose
  extent is a speech area; the located object is not a surveyed feature. Under
  §2.3 of this document their `positional_certainty` is `mapped-approximate` at
  best, and a
  `Point` geometry is not legal for them. Every distance in
  `03-REGISTERS/domain-e-geography.csv` and in `DMB-010`–`DMB-014` was computed
  from these representative coordinates and is, under G-9, a derivative with its
  method named — which is exactly how `DMB-014` was able to measure the metric's
  own +13.7% distortion.
- **They carry no date assertion at all.** `DMB-008`'s note is explicit:
  *"Present-day or recent-survey locations only: nothing here dates anything."*
  The ledger row for `SRC-050` says the same of the source — *"Point coordinates
  only. No polygon, no historical extent, no date."* A 2026 retrieval date is a
  retrieval, not an attestation. Under §4.6 rule 2 of this document these objects
  therefore sit in the **no-assertion tray under every setting of the time
  control**, and under §4.6 rule 5 they reach the map only through the explicit
  undated control, drawn with the undated marker. There is no interaction that
  moves them earlier, because `BR-E-003` is refused.
- **They are one source, not two.** `DE-M-021`'s own note reads *"Glottolog
  coordinates as carried by JAMBU"*, and `DMB-008` retrieved the same Glottolog
  coordinates directly. `SRC-060` and `SRC-050` are one upstream
  (`02-SOURCES/dependency.csv` `DEP-027`), so the 47, the 20 and the 20 do not
  add and the layer is single-sourced.

**Verdict: spatially assertable, temporally unasserted, single-sourced.** The
ancient lexicon is registered, measured and unplottable; the one place-anchored
dataset answers no time control.

### 9.3 GRAMMAR

**Reads:** morphological and syntactic features of attested varieties, including
areal features; `convergent-with` drawn distinctly from
`reconstructed-ancestor-of`. **Requires to appear:** features are properties of
attested varieties, never of populations (§8.4).

**Could populate today:** nothing. The pinned corpus carries per-token morphology
(`VAR-004`, `VERIFIED`: the Zurich annotation *"carries lemma and morphology for
each of the 23 tokens and carries no sense field"*), so Vedic morphology is
available as data — but no registered claim states a morphological or syntactic
*feature* with a place and a date, and no comparative grammatical dataset has
been retrieved. `DMB-020` (`VERIFIED`) is explicit that the retrieved instrument
cannot reach this evidence: DravLex is a 100-concept lexical wordlist, *"the
conventional case for North Dravidian is phonological and morphological"*, and no
such comparative material was retrieved.

**Blocked by:** `05-HOLDS/HOLD-004-north-dravidian-comparative-evidence.md`.

**Verdict: not populatable.** The layer exists in the specification and would
render as empty-with-a-reason, which under §7.2 rule 3 is a typed zero result —
"no evidence has been collected in this area", not "no claims match".

### 9.4 NEIGHBOURS

**Reads:** dated adjacency between places and varieties. **Requires to appear:**
§8.4 — *"This layer establishes setting only. Objects on it can never raise a
linguistic claim above `PROVISIONAL` by themselves; it is the map form of the
`contextualises` role."*

**Could populate today:** adjacency among present-day lects, and nothing else.
`DE-M-023` (`VERIFIED`: nearest attested Dravidian lect to any northwestern lect
is Brahui at **393 km**), `DE-M-024` (nearest Munda is Korku at **855 km**),
`DE-M-025` (remove Brahui and the nearest Dravidian is Kolami at **1,055 km**,
farther than Munda's nearest member), `GEO-DR-04`–`06`, `GEO-MU-04`–`06`,
`DMB-010` (Brahui's nearest attested Dravidian neighbour 1,561.5 km, against a
median nearest-neighbour distance of 67.0 km across the twenty varieties),
`DMB-011` (Kurukh 2,038.1 km, Malto 2,139.2 km).

**Could not populate:** adjacency in antiquity, which is what the layer is for.
Every one of the measurements above is between modern survey locations.
`DMB-002` (`VERIFIED`) states the limit on its own instrument in terms this layer
must inherit: the statistic *"does not support any statement about where
Dravidian was spoken at any date: the statistic has no chronological term, the
attested set is a survival sample rather than a sample of past distribution, and
the reference point is a free parameter of the analyst's choosing"* — with
`DMB-013` measuring that free parameter's effect at 0 to 1,453 km depending on
where the analyst puts the reference point.

**And a rule the layer needs, because half of this material is
reference-dependent.** `DE-M-023`, `DE-M-025`, `GEO-DR-04`/`05` and `DMB-012` are
all *distance from a chosen northwestern reference*, and `DMB-013` measures what
the choice is worth: deleting Brahui moves the statistic by between 0 and 1,453
km depending on where the analyst puts the reference point. `BF-005` is the
logged case of exactly this statistic being over-read, and its control requires
the reference point and the per-element influence to be reported wherever the
number is. A line or a distance drawn on a map has nowhere to carry either.
**A reference-dependent statistic may not generate map geometry** unless its
reference point is drawn with it and its influence distribution is one
interaction away; otherwise it is panel content.

**Verdict: populatable only as a present-day adjacency statement**, whose objects
all carry `contextualises` and therefore cannot move any language claim, and half
of whose quantities are panel content rather than geometry. Whether such a layer
should ship at all is **`D-055`**.

### 9.5 MATERIALS

**Reads:** material types, sources, techniques and their movement; `mk:evd:` with
`evidence_class = material`; `same-material-source-as`, `traded-along`,
`same-technique-as`. **Requires to appear:** §2.4's class-specific required
fields — composition, dimensions, excavation or acquisition event, stratigraphic
context or `context-lost`, holder, accession number or `unaccessioned`.

**Could populate today:** nothing. **There is not one material-class evidence
object in `03-REGISTERS/`.** Every register in this repository is textual,
lexical, phonological, geographic-over-modern-lects, or historiographical.

**Could not populate, specifically:** the inherited atlas. `IH-105`
(`INHERITED-UNVERIFIED`) reports 194 site records, 315 class-windows and 14
classes, *"with 54 of 199 site-class rows dated from excavation reports and 145
marked assumed"*. Under Rule S-1 and `CLAUDE.md`'s inheritance rule that is a
claim about a prior page, not a materials dataset, and 145 assumed rows would
arrive as 145 unsourced Date Assertions. Constitution §4R (materials and
corridors) and §4S (Meluhha, Marhaši, Magan, Dilmun) are the research agenda that
would produce this layer and neither has been run here.

**Verdict: not populatable.** This is the layer a visitor most expects an
"artifact atlas" to have, and it is empty.

### 9.6 RITUALS

**Reads:** attested ritual practices with their evidence and dates; `culture`-domain
objects. **Requires to appear:** any link to language, ancestry or polity is a
bridge (§4.4).

**Could populate today:** nothing. Constitution §4U (sacrifice, renunciation and
appropriation) has not been run in this repository. The nearest registered
material is the `pur-` corpus, which is textual and whose typology explicitly
declines every non-textual assignment (§9.10 of this document).

**Verdict: not populatable.**

### 9.7 TEXTS

**Reads:** `mk:txt:` at composition, attestation, redaction and manuscript-witness
places, *"each as a separate typed assertion"*. **Requires to appear:** §8.4 —
*"A text plotted at one point is a lie about transmission; the layer draws the
spread."*

**Could populate today:** one text object, well evidenced as an object.
`DME-001` (`VERIFIED`) records the pinned VedaWeb corpus re-retrieved at commit
`d3eb8af7…` with per-file sha256; `DME-002` and `PUR-001` (`VERIFIED`) give
164,758 tokens over 10,031 lemmas, 10,552 stanzas and 39,832 padas; the editions
and translations are in the ledger — Aufrecht and the padapāṭha, Griffith,
Geldner, Grassmann (`SRC-069`, `SRC-020`, `SRC-022`, `SRC-072`, `SRC-073`,
`SRC-074`), with Arnold 1905 at `SRC-023`.

**Could not populate:** the places. No composition place, no attestation place,
no redaction place and no manuscript-witness place is registered for the
Rigveda in this repository, and `PUR4J-018` establishes that the pinned corpus
contains none. Every place assertion on this text would be `unlocated`, and
`DE-M-027` records that its absolute dates cannot be established from anything
retrieved.

**And the editions are dated but not located either.** `DE-M-026` (`VERIFIED`)
dates the instruments across 114 years — Arnold 1905, Turner 1962–66, Burrow and
Emeneau 1984, Krishnamurti 2003, Rau 2019, and the JAMBU build of 2026-08-30 —
and that is all it does. **The row names no place, its locator names none, and
no Place Assertion for any of the six exists anywhere in `03-REGISTERS/`.**
Framework §2.4's required fields for `evidence_class = historiographical` do not
include one either. So the instrument timeline satisfies condition 2 of §9.0 of
this document and fails condition 3 exactly as the rest of the record does.

**Verdict: not populatable on the map.** The Rigveda would be a text object whose
every Place Assertion is `unlocated`, sitting in the unlocated tray with its
editions beside it — which is honest content and is panel content, not layer
content. It still raises the question at **`D-053`**: the eleven layers have no
home for historiographical evidence, which is the best-*dated* class in this
record even though it is not a located one.

### 9.8 ANCESTRY

**Reads:** genetic samples and ancestry components at sample sites, with dates
and laboratories. **Requires to appear:** §2.4's genetic required fields,
including *"whether the individual's community descendants were consulted"* as a
`consent_ref` or a typed refusal; and §8.4's constraint that **components are not
peoples, languages or moral categories**, with the layer forbidden from being
coloured to match any language layer.

**Could populate today:** nothing. No genetic-class evidence object exists in
this repository. The inherited record mentions pages built on this material
(`IH-197`, `INHERITED-UNVERIFIED`, naming `the-three-ancestries` and
`the-genome-of-caste` among ~27 pages), which is a claim about pages.

**Could not populate, and not merely for want of data:** this layer cannot be
filled by importing a published dataset, because §2.4 requires a consent record
or a typed refusal per sample, and a public data release does not supply one.
Populating ANCESTRY is a rights and consultation process (§11.2, §11.4) before it
is a data process.

**Verdict: not populatable, and blocked twice.**

### 9.9 ARCHAEOLOGICAL CULTURES

**Reads:** named archaeological cultures with defining assemblages, dates, and
**the history of their naming** — who named it, when, on what assemblage, and
whether the name has since been contested. **Requires to appear:** the naming
history is part of the object, and *"a culture is a typological construct, and
the layer says so on its face"* (§8.4).

**Could populate today:** nothing. No archaeological culture object exists, and
none could be created from a gazetteer, because the naming history is a
historiographical retrieval — the defining publication, its author, its date and
its argument — and none has been run here. Under §3.4 of this document every one
of these names is a `scholarly-coinage` name assertion, and a culture imported
with its name and without its namer is exactly the object §8.4 forbids.

**Verdict: not populatable.**

### 9.10 POLITICAL CONTROL

**Reads:** dated `ruled-by` relationships over places. **Requires to appear:**
constitution Step 3 — *"Imperial control does not prove language use"* — and
§8.4's rule that this layer *"may not be used as a proxy for any other layer, and
the interface states this where the two are shown together"*.

**Could populate today:** nothing — and this is the case where the register
contains not merely an absence but an explicit refusal, which is more useful.

The forts corpus is 103 stanzas of the Rigvedic `pur-` family, built at the
stanza and fully registered: `rigveda-pur-passages.csv`,
`rigveda-pur-typology.csv`, `rigveda-pur-fields.csv`, `rigveda-pur-4j-claims.csv`.
Its typology assigns 48 `TEXTUAL-STRONGHOLD`, 47 `POETIC-FORMULA`, 3 `BOTH` and 5
`CANNOT-CLASSIFY`, every row `PROVISIONAL`. And on **all 103 rows** the columns `inferred_geography`,
`archaeological_fortification` and `unsupported_identification` read
`NOT ASSIGNED`, with the register's own reason carried in every row:

> *"These three of §4J's five types are not properties of the passage. Each is a
> verdict on an argument someone else must make first — a placement, a site
> match, an identification. This unit has no geographic source (the pinned
> corpus carries none, `PUR4J-018`) and no archaeological source, so none is
> assigned to any passage. Assigning one anyway is precisely how a textual
> stronghold becomes an archaeological one."*

`PUR4J-024` (`PROVISIONAL`) registers that reasoning as a claim.

**Verdict: not populatable, by the registered evidence's own construction.** The
103 rows are the best-evidenced corpus in this repository for a political-control
layer and they refuse to supply one. That refusal is itself displayable: under
§7.2 rule 3 the layer's zero is typed, and the type here is not "no evidence"
but "the evidence declines the assignment".

### 9.11 UNKNOWN SPEECH ZONES

**Reads:** `mk:abs:` records (§3.7) with typed `absence_type`, rendered as
`zone-unknown` Features (§2.5 of this document). **Requires to appear:** the
seven negative-evidence fields, a typed absence, and a typed `boundary_basis`.

**Could populate today — the layer with the most registered material:**

- `DMB-015` (`VERIFIED`, `SRC-048`): the attested set is a **survival sample** —
  every coordinate is a present-day or recent-survey location of a language that
  was not replaced — and the absence of a Dravidian point between Baluchistan and
  central India is typed on the negative-evidence typology rather than read as a
  fact about the past.
- `DE-M-019` (`VERIFIED`, `SRC-068`): four of constitution §4E's eleven
  distinctions — proposed Dravidian substrate forms, Para-Munda, the Kubhā–Vipāś
  prefixing language, and Language X — yield **zero measurable items** from
  anything retrieved, typed `NOT ACCESSIBLE`, *"the weakest form of absence"*,
  with the note that the row exists *"to stop a later reader treating the empty
  cells as findings"*. `SRC-068` is the substrate literature — Witzel 1999,
  Kuiper 1991, Masica 1979 — for which *"no reachable host serves these texts in
  this session"*.
- The six records in `05-HOLDS/`, and `DME-025`, which is itself `HOLD` and
  therefore appears as a hold record rather than as layer content: framework
  §3.12 bars publishing any derived asset depicting a `HOLD` claim, and a drawn
  zone is a derived asset.
- `BR-E-003`, the refused bridge from modern to prehistoric distribution, which
  is the reason most of the map is unknown rather than merely unlabelled.

**Could not populate — the polygons.** An unknown-speech-zone Feature needs a
`search_coverage` denominator (§2.5, §3.5 of this document), and this repository
holds **corpus** coverage (the pinned Rigvedic corpus, exhaustively searched, is
a real and complete denominator for statements about that corpus) and **no
excavation or survey coverage for any region at all**. Without a denominator the
boundary cannot be typed, and an untyped boundary is the freehand line §2.5 of
this document refuses.

**And one distinction the layer must carry that the framework does not spell
out:** `NOT ACCESSIBLE` in `DE-M-019` is an absence in a **literature**, caused
by egress blocks on the hosts serving Witzel, Kuiper and Masica (`SRC-068`;
`HOLD-005`), not an absence in a **region**. `DME-025` is the same shape and says
so — *"a fact about the network, with no bearing on the lexicon"* — and the DEDR
block is a third (`SRC-056`, `dsal.uchicago.edu`; `HOLD-002`). A polygon drawn
over Balochistan because a dictionary could not be downloaded would be a map of
this session's network policy wearing the costume of a map of the past. Absence
records are therefore scoped —
`absence_scope` ∈ `region` · `corpus` · `literature` · `archive` — and **only
`region`-scoped absences may generate geometry.**

**Verdict: records yes, polygons no.** The absence records exist and are typed;
the denominators that would bound them do not, so no `zone-unknown` geometry can
be validly drawn yet. `DMB-015` is the one region-scoped absence in the set and
it is unquantified — there is no excavation or survey coverage figure for the
corridor it describes — so its boundary cannot be typed under §2.5 of this
document. The rest are corpus- and literature-scoped and are barred from geometry
by rule. The layer's first honest state is a populated panel and an unpopulated
overlay, which is a worse-looking and truer result than a zone drawn to a
boundary nobody measured.

### 9.12 Cross-layer rules, and the state of the bridges

§8.4's four cross-layer rules stand unchanged and are enforced as specified at
§7.6 of this document: no layer recolours another; two layers shown together
produce a stated correlation and not a relationship; layer legends carry status
distributions; layer 11 cannot be switched off beneath a language layer.

To which this record adds one fact that determines what the correlation notice
will actually say. §8.4 requires that where two layers are co-displayed the
surface *"offers the statused bridges that do exist between the two, with their
mechanisms and rivals"*. **In this repository there are none.** All eight rows of
`03-REGISTERS/CROSS-DOMAIN-BRIDGES.csv` are refusals or failures:

| Bridge | From → To | Verdict |
|---|---|---|
| `BR-E-001` | a word in the Rigveda → a language contact event | NOT ESTABLISHED HERE |
| `BR-E-002` | a late metrical stratum → a late date of borrowing | WEAK — three separate failures of independence |
| `BR-E-003` | attested modern distribution → prehistoric distribution | EXPLICITLY REFUSED |
| `BR-E-004` | a language family → a population | NOT CROSSED — DELIBERATELY |
| `BR-E-005` | a substrate donor in the northwest → the language of the Indus civilisation | NOT CROSSED |
| `BR-E-006` | Turner's loan arrow → scholarly acceptance | NOT ESTABLISHED |
| `BR-E-007` | a reconstructed proto-form → an attested word | NOT CROSSED — BY DESIGN |
| `BR-E-008` | a compound member → attestation of the simplex | REFUSED, and the distinction is productive |

The correlation notice therefore reads, for every pair of layers a visitor
switches on together: *co-location is not a relationship, and no statused bridge
exists between these two layers.* That is not a placeholder awaiting content. It
is the current state of the record, it is checkable, and a build in which the
notice ever says otherwise without a new `mk:rel:` row having been evidenced has
failed `CHK-REQ2-3`.

### 9.13 Summary

| # | Layer | Populatable today | What could populate it | What blocks it |
|---|---|---|---|---|
| 1 | SOUNDS | **Content only, no geometry** | `DME-003`–`DME-007`, `DME-013`, `DME-014`, `DME-019`, `DME-021`; 253 residue rows | No localisation claim exists for any sound change; chronology is relative-ordinal only |
| 2 | WORDS | **Partly — undated, single-sourced** | Spatially assertable: `DE-M-021`, `DE-M-022`, `DMB-008` as approximate extents carrying **no date assertion** (`DMB-008` note; `SRC-050`), one Glottolog upstream (`DEP-027`). Unplottable: `DE-M-009`–`DE-M-011`, `DE-M-020`, `DME-015`–`DME-018`, `VAR-001`, `VAR-007`, the `pur-` family | The Rigveda has no attestation place (`PUR4J-018`); hydronym→river is an unmade identification claim; `BR-E-003` refuses the modern→ancient step; and the one mappable set answers no time control |
| 3 | GRAMMAR | **No** | — | `HOLD-004`; `DMB-020` — no comparative phonological or morphological dataset retrieved |
| 4 | NEIGHBOURS | **Present-day only** | `DE-M-023`–`DE-M-025`, `GEO-DR-04`–`06`, `GEO-MU-04`–`06`, `DMB-010`, `DMB-011` | All measurements are between modern survey locations; `DMB-002` and `DMB-013` bound what they support. Shipping it at all is `D-055` |
| 5 | MATERIALS | **No** | — | No material-class evidence object exists in `03-REGISTERS/`. `IH-105` is `INHERITED-UNVERIFIED` with 145 of 199 rows "assumed" |
| 6 | RITUALS | **No** | — | Constitution §4U not run |
| 7 | TEXTS | **No — panel content only** | Off-map: `DME-001`, `DME-002`, `PUR-001`, the editions at `SRC-020`/`022`/`069`/`072`/`073`/`074`, `SRC-023`; `DE-M-026` for the instrument timeline | No composition, attestation, redaction or witness place is registered (`PUR4J-018`); absolute dates unestablished (`DE-M-027`); and `DE-M-026` dates the instruments without locating them |
| 8 | ANCESTRY | **No** | — | No genetic evidence object; and §2.4 requires a consent record or typed refusal per sample, which an import does not supply |
| 9 | ARCH. CULTURES | **No** | — | No culture object; naming history is a historiographical retrieval not yet run |
| 10 | POLITICAL CONTROL | **No** | — | The 103-row `pur-` corpus refuses the assignment on all rows (`PUR4J-018`, `PUR4J-024`) |
| 11 | UNKNOWN SPEECH ZONES | **Partly — records yes, polygons no** | `DMB-015`, `DE-M-019`, `DME-025`, `05-HOLDS/`×6, `BR-E-003` | No excavation or survey coverage denominator for any region; corpus- and literature-scoped absences may not generate geometry |

---

## 10. The transition record

§8.5 specifies the transition — the language-movement mode's unit of assertion —
and its ten required fields from constitution §13. That table is not repeated.
Four things this document adds, because they are where the record shape meets the
geometry and time contracts above.

**Field types.**

| §8.5 field | Type under this document |
|---|---|
| `earliest_evidence` | `mk:evd:` + locator + a Date Assertion (§4.2). Where the earliest is contested, an array of contenders, each with its own source. **A `provides-contact-setting-only` object may not appear here** (§6.2 of this document) |
| `evidence_classes[]` | The nine (§2.3), plural, with the breakdown shown |
| `date_range` | Two `DateValue`s (§4.2 of this document) with `date_type` named and the basis of each bound. **A transition whose only chronology is `relative-ordinal` has no calendar `date_range`** and is not displayable on the map's time axis (§10.2 of this document) |
| `geography` | Typed Place Assertions with geometry and `positional_certainty` (§2.3 of this document); `zone-unknown` permitted and drawn |
| `attestation_mode` | The five-value gradient (§2.6), not a binary |
| `mechanisms[]` | Named processes with the evidence that each was available in that place and period. Non-empty |
| `alternatives[]` | Rival transitions, each independently reconstructed, displayed at equal weight, **with the null always among them and "unknown" never among them** (§8.4 of this document) |
| `confidence` | Derived from status, independent-source count and evidence-class breadth, **displayed with its inputs** |
| `sources[]` | `mk:src:` resolving in the access ledger, with locators, retrieval dates and independence groups |
| `falsifiers[]` | §3.9. Non-empty |

**10.1 The ten-field gate is a render gate.** §8.5: *"a transition with any of
them empty cannot be displayed."* Under §8.5 this also governs animation — the
mode may animate only transitions that pass, and a transition whose
`attestation_mode` is `proposed` or whose confidence is low must be visually
distinguishable **while moving**, not only when clicked. Whether the mode
animates at all is `D-023`.

**10.2 A transition needs a place and a calendar date, and this record has
neither.** The consequence is worth stating plainly rather than leaving a reader
to derive it from §9 of this document: **no transition is constructible from any registered claim
in this repository today.** `geography` requires typed Place Assertions and
`PUR4J-018` establishes that the corpus carries none; `date_range` requires a
named date type with a basis for each bound and `DE-M-027` establishes that the
absolute dates cannot be established from anything retrieved. The
language-movement mode is therefore specified and empty, and an Atlas shipped
now would ship it empty rather than ship it with `INHERITED-UNVERIFIED` content.

**10.3 The panel is the export.** §8.5: *"What the panel shows is exactly what
§5.2 exports for that transition. There is no display-only prose."* Under §5.3
rule 5 this extends to every computed value on the panel — `confidence` and its
inputs, the evidence-class breakdown, the independent-source count — all of which
are exported with their inputs, not as results.

---

## 11. Validation, export and conformance

### 11.1 The checks

Forty-two checks are named in this document. They are grouped here so that a
build has one list, and each is stated as an assertion whose failure means the
object or the view does not render.

**Geometry and time.** `CHK-G-1` every geometry is a Feature with all required
properties non-null · `CHK-G-2` `Point` geometry occurs only where
`positional_certainty = surveyed-point` · `CHK-G-3` no rendered or exported
coordinate exceeds its Feature's `mk:coordinate_precision_dp` · `CHK-G-4` no
`GeometryCollection`, no third coordinate, rings closed and non-self-intersecting
· `CHK-G-5` confidence-polygon rings nest, and no ring with `semantics ≠
modelled-probability-contour` carries a percentage label or a continuous ramp ·
`CHK-G-6` no object with `attestation_mode ∈ {reconstructed,
unidentified-residue}` carries any extent geometry · `CHK-T-1` every stored
absolute date is a signed astronomical year and no arithmetic operates on a
BCE/CE display pair · `CHK-T-2` no `uncal-BP` value appears on the calendar axis
· `CHK-T-3` every BP value carries its reference epoch and calibration state ·
`CHK-T-4` no `relative-ordinal` date is placed on the calendar axis ·
`CHK-T-5` no bound is null; open bounds carry `open` and `open_reason` ·
`CHK-T-6` the time control's current `date_type` is displayed, and objects
lacking an assertion of that type appear in the no-assertion tray and in the
view's readouts.

**Routes.** `CHK-RT-1` `path_geometry` type is legal for the record's
`route_uncertainty` · `CHK-RT-2` no path is interpolated, smoothed or snapped
between waypoints · `CHK-RT-3` no waypoint lacks an evidence link ·
`CHK-RT-4` no route is rendered whose origin and destination are both `unlocated`
or `zone-unknown`.

**REQ-1** — `CHK-REQ1-1` to `CHK-REQ1-9`, §6.8 of this document.
**REQ-2** — `CHK-REQ2-1` to `CHK-REQ2-9`, §7.8 of this document.
**REQ-3** — `CHK-REQ3-1` to `CHK-REQ3-8`, §8.6 of this document.

Three of them test the **rendering** rather than the data, and they are the ones
that catch the failures this document exists to prevent: `CHK-REQ2-3` (no drawn
connection without a backing row), `CHK-REQ3-2` (no blank inside the declared
scope) and `CHK-REQ3-4` (no digit in the title slot). A build can hold a clean
graph and still draw a line, leave a hole, or put a number in a heading.

### 11.2 The Atlas view export

§5.2 already specifies the Atlas view export as CSV, GeoJSON and JSON carrying
*"the exact filter state, every object in view with its assertions, every
excluded object with the reason it was excluded"*. This document adds four
requirements:

1. **The GeoJSON export is the constrained profile** (§2.2 of this document), including all
   required Feature properties. An export that strips them to make a smaller
   file is the status-column-stripped spreadsheet in another format.
2. **The export carries `language_evidence_state`, `also_true[]` and
   `state_basis[]` on every object**, from which the four-state distribution
   (§6.6 of this document) is recomputable. It does not carry the distribution as
   an aggregate — §8.5 rule 5 of this document.
3. **The export carries endpoint domains, `bridge_type`, and the
   non-transitivity header** (§7.7 of this document).
4. **The export carries no summary total** (§8.5 rule 5 of this document). It carries the objects,
   the exclusions and the filter, from which any consumer can count whatever
   they can define.

### 11.3 Fixtures

§5.3 rule 6 requires a conformance fixture set *"covering every enum value and
every required-field rule"*. The Atlas's contribution to it is small and should
be built before any real object is created, because each fixture is a case this
document argues about:

a surveyed point · an approximate extent that may not be a point · a
disputed-location pair · an unlocated object · a `zone-unknown` zone with a
region-scoped absence · a corpus-scoped absence that may **not** generate
geometry · a place with two dated extents that do not interpolate · a date
crossing the BCE/CE boundary · an uncalibrated radiocarbon determination · a
relative-ordinal date on Arnold's strata · a route with unevidenced path · a
route with evidenced waypoints and a gap · one object in each of the four
language-evidence states, including the undeciphered inscribed object of §6.5 of this document ·
a bridge edge that a traversal must terminate at · a view whose
`provides-no-language-evidence` count is zero.

---

## 12. What the first buildable Atlas actually contains

A specification that did not say this would be describing a building with no
contents.

**On the map today, from registered evidence above `INHERITED-UNVERIFIED`:**
one dataset — the attested Dravidian and Munda lect locations (`DE-M-021`,
`DE-M-022`, `DMB-008`), drawn as approximate extents rather than points. Three
qualifications, all of them structural rather than editorial. The three rows are
**one Glottolog upstream, not three datasets** (`DEP-027`), so the layer is
single-sourced and its counts do not add. It carries **no date assertion at all**
(`DMB-008`: *"nothing here dates anything"*; `SRC-050`: *"no date"*), so under
§4.6 of this document it sits in the no-assertion tray under every time-control
setting and reaches the map only through the explicit undated control. And it is
present-day, which `BR-E-003` bars from standing for antiquity. Nothing else. No
site, no artifact, no culture, no polity, no route, no transition.

**Off the map but in the Atlas:** the whole of the lexical, phonological and
textual record — the 15 Rigvedic loan-candidate lemmas and their 21 tokens, the
253-lemma retroflex upper bound, the 31 hydronyms over 251 occurrences, the
103-stanza `pur-` corpus, the 23 tokens of `varṇa-`, and the Rigveda itself with
its editions — every one of them in the unlocated tray, counted in every readout,
exported with every view, and visible as *present and unplaced* rather than
absent. The instrument timeline (`DE-M-026`) is here too, and not on the map: it
dates six instruments across 114 years and locates none of them.

**And the unknown**: a populated panel and an unpopulated overlay. The one
region-scoped absence record in the set (`DMB-015`) has no coverage denominator,
so its boundary cannot be typed and no `zone-unknown` polygon can validly be
drawn from it yet; the rest are corpus- and literature-scoped and are barred from
geometry by rule, because a network block is not a fact about the past.

**Against the eleven layers**, from the table at §9.13 of this document: two are
partly populatable and neither of them is populatable on the map (WORDS, undated
and single-sourced; UNKNOWN SPEECH ZONES, records without polygons), one is
content-only (SOUNDS), one could carry a present-day reference statement only
(NEIGHBOURS, subject to `D-055`), and seven are empty (GRAMMAR, MATERIALS,
RITUALS, TEXTS, ANCESTRY, ARCHAEOLOGICAL CULTURES, POLITICAL CONTROL). That count
is read off the table rather than carried alongside it, per the inherited
standing rule that counts are data-derived and never a running tally.

That is a thin Atlas, and it is not a thin record — the registers behind it hold
several hundred measured, sourced, retrieval-backed rows. The gap between the two
is one fact stated three different ways: **this repository has done a great deal
of textual and lexical work and no geographic work**, because the corpus it works
on carries no geography (`PUR4J-018`) and the only coordinates it holds are
present-day (`DE-M-021`, `DE-M-022`) and are barred from standing for antiquity
(`BR-E-003`).

An Atlas that looked fuller than this could be built today by three moves, and
each is forbidden by a rule in this document: importing the inherited 194 site
records (Rule S-1, and §9.5 of this document), identifying the 31 hydronyms with
modern channels (§3.4 of this document), or reading the present-day lect
distribution back into antiquity (`BR-E-003`, §7 of this document). The Atlas being thin is the specification working, not the
specification failing. What would make it full is retrieval — material,
epigraphic and archaeological sources that this repository has not yet reached —
and `CLAUDE.md`'s rule holds here as everywhere: only retrieval promotes.

---

## 13. Owner decisions

### 13.1 Raised here

Three, allocated in `09-DECISIONS/OWNER-DECISIONS.csv`, which is authoritative
for the `D-` namespace. The specification is buildable under either answer to
each, and the default it builds under is stated.

**`D-053` — Do the eleven layers gain a twelfth for historiographical evidence,
or does it stay in the panel?** None of the eleven is a home for
`evidence_class = historiographical` — which, in this repository, is the
best-*dated* evidence there is (`DE-M-026`: six instruments across 114 years).
**Constitution §13 does not forbid a twelfth**: it reads *"Available layers
should include:"*, which is a floor and not a closed enumeration, so adding one
amends nothing and the reason to escalate is not a constitutional one. The reason
it is escalated is that putting the history of scholarship on the same map as
antiquity is a product position with real interpretive weight — it is the
difference between an atlas of the past and an atlas of the past and of its
study — and it sits directly against `D-022`, which decides layer grouping and
first-load defaults. **Default built under: no twelfth layer.** The instrument
timeline lives in the transition panel's `sources[]`, in the source-genealogy
tree (framework §3.5) and in Source Mode (framework §7), and the Atlas does not
draw it. Blocks nothing.

**`D-054` — Does the Route get its own type code `mk:rte:`, or is it modelled as
a Relationship Object with a waypoint extension?** §5.1 of this document states both and the
reason for preferring the first. Adding a code to §2.1's identity table amends
another specification, which is why it is raised rather than taken. **Default
built under: `rte` is allocated.** Every field in §5.2 of this document is a field under either
modelling. Blocks nothing; changing it later is an identifier migration, which is
why it is better decided before any route exists.

**`D-055` — Does the Atlas ship a present-day language-distribution reference
layer at all?** This is the only layer the record could populate on the map today
(§9.2 and §9.4 of this document), and it is also the layer whose misreading `BR-E-003` explicitly
refuses. §6.3 permits present-day reference material *"if at all"*, and the "if"
is doing real work: a labelled, switchable modern layer is honest, and a visitor
who reads a modern Dravidian distribution as an ancient one has been given the
material to do it by the institution. **Default built under: the layer exists,
off at first load, labelled present-day, excluded from evidence exports.** This
blocks the content of the first Atlas build, so it carries a prose section in
`DECISIONS-NEEDED.md`.

### 13.2 Cited, not re-raised

`D-019` (register `object_id` column or crosswalk — determines how `mk:plc:` and
`mk:rte:` join the register CSVs) · `D-021` (a guided sequence through the seven
settings) · `D-022` (layer grouping, first-load defaults, and — under §8.2 of
this document — render order, subject to the layer-11 non-occlusion rule) ·
`D-023` (whether the mode animates) · `D-034` (the page count and the atlas site
count; neutralised but not answered by §8.5 of this document — the Atlas can be
built without it and cannot be titled without it) · `D-012` (whether product and
institutional specification belongs in this repository or in `melakeela/site`,
whose `blocks` column names *"where the Atlas mode spec and the evidence-object
model live"* — this file is that spec, filed in `13-PRODUCT-ARCHITECTURE/` per
constitution §15 on the same reading `museum-framework.md` §0.4 took, and it
moves wherever `D-012` sends the directory).

---

## 14. Adversarial tests

Both were run at document scope before this file was first committed, per
`CLAUDE.md` §8 and framework §3.11. Both found something. A third row, `BF-026`,
records what **neither of them caught and adversarial review did**, and a reader
is entitled to see that in the same place rather than to find it in the log.
Logged as `BF-024`, `BF-025` and `BF-026` in
`04-AUDITS/BIAS-FAILURE-LOG.csv`, with the earlier work they touch queued as
`RA-022` and `RA-023` in `04-AUDITS/REAUDIT-QUEUE.csv` and the framework tension
one of them surfaced logged as `IC-X-002` in
`04-AUDITS/INTERNAL-CONTRADICTIONS.csv`.

**Prestige-bias challenge — `BF-024`.** *Did this privilege a claim because it is
canonical, Sanskritic, Brahmanical, Indo-European, European, colonial,
institutionally prestigious, repeatedly cited or nationally useful?*

Finding: the draft specified layer render order as "the order constitution §13
lists them", which would have painted SOUNDS, WORDS and GRAMMAR — the
comparative-philology apparatus, an inheritance of nineteenth-century
Indo-European scholarship — over UNKNOWN SPEECH ZONES, the layer §8.4 calls *"the
layer that makes the other ten honest"*. Taking a list written in a sentence as a
z-order is how institutional priority gets encoded as a default nobody chose.
Corrected at §8.2 of this document: the enumeration order is declared **not** a
render order and not a priority, layer 11 is non-occludable at every zoom, and
render order goes to `D-022`. A second, smaller instance was caught in the same
pass: the geometry contract had defaulted to north-up without noticing that
orientation is a convention and that the v1 page was south-up (`IH-197`); §0.5 of this document
now records orientation as a decision with a stated reason and the contract
stores coordinates rather than a view.

**Preferred-counter-narrative challenge — `BF-025`.** *Did this accept a claim
too easily because it is Dravidian, Indigenous, anti-colonial, anti-Brahmanical,
subaltern, diffusionist or politically corrective?*

Two findings.

1. The draft's §9 summary (of this document) read *"the Atlas can draw nothing today"* — a
   satisfying, methodologically self-flattering result that was **false**. The
   47 Dravidian and 20 Munda lect locations (`DE-M-021`, `DE-M-022`, `VERIFIED`)
   are plottable, with modern attestation dates and approximate geometry. The
   honest statement is that the Atlas can draw one thing and it is present-day,
   which is a weaker and more useful finding than the pure zero, and it is what
   §9.2, §9.13 and §12 of this document now say. It also produced `D-055`, which the false version
   would have hidden.
2. The `zone-unknown` construct as first drafted carried an unexamined
   implicature. "Unknown speech zone" reads as *"people were here and we do not
   know what they spoke"* — a populated-past claim, and a congenial one, since it
   corrects the erasure §8.2 warns about (*"blank reads as empty and empty reads
   as nobody"*). But the correction can overshoot: not knowing what was spoken in
   a region and not knowing whether anyone was there are different absences with
   different evidence. §2.5 of this document now requires a typed `boundary_basis` and §9.11 of this document
   requires a scoped `absence_scope`, with only `region`-scoped absences
   permitted to generate geometry — which also stops a network block
   (`SRC-056`, `HOLD-005`) from being drawn as a fact about Balochistan.

**Symmetry check, run as part of the second test.** The three main mechanisms
were checked in both directions and block both: §2.6 of this document forbids an
Indo-European homeland polygon and a Proto-Dravidian one on identical grounds; §7
of this document blocks
artifact→polity→language (trade goods becoming a language map) and
artifact→ancestry→language (`BR-E-005`, the Indus script becoming a family's) by
the same terminal-edge rule; §6.4 of this document's precedence rules block both the upgrade of an
undeciphered object into linguistic evidence and the downgrade of an awkward one
into background. A mechanism that blocked only the direction this repository is
predisposed against would not be a mechanism.

**Found in adversarial review, not by either of those passes — `BF-026`.** The
submitted draft of this file overstated what the register supports in four
places, all in the same direction, and the direction is the one that made the
document's own argument easier. It asserted that `DE-M-026`'s six instruments
*"each"* carry *"a place and a date"* — the row names no place, its locator names
none, and no Place Assertion for any of the six exists in `03-REGISTERS/` — and
rated TEXTS *"partly populatable"* on the strength of it. It said the lect
locations carry modern attestation dates, against rows that say the opposite in
terms (`DMB-008`: *"nothing here dates anything"*; `SRC-050`: *"no date"*). It
counted three selections over one Glottolog coordinate set as three datasets,
against `DE-M-021`'s own note. And it listed `DME-011` and `DME-012` among
Arnold-strata rows when `DME-011` opens *"The second instrument, book order"* —
a breach of `RESEARCH-CONSTITUTION.md` standing rule 1, from correction `C-05`.

The corrections are at §9.7, §9.13, §9.2, §12, §4.6 rule 5, §4.4 and §9.1 of this
document, in `DEP-027`, and in the `D-053` and `D-055` rows. The thing worth
recording is not the four errors but their relation to `BF-025`: that row caught
a false *zero* accepted because it flattered the method, and wrote a control
requiring a finding in the opposite direction to be checked row by row on the
same footing. The control was written and then not applied to the replacement
finding in the same document. A control that is not run on the document that
produced it is a control in name.

**`RA-022`** queues `museum-framework.md` §8.4 for re-audit: its layer table
presents the eleven in constitution §13's order and does not state that the order
is neither a priority nor a render order, which is the omission `BF-024` found
being read as an instruction. **`RA-023`** queues framework §2.8 and §8.4 layer
11: neither types a `zone-unknown` polygon's boundary nor scopes the absence
behind it, which is the gap `BF-025`'s second finding closed inside this document
and left open in the framework.

---

## 15. Status of this document

Every design proposition here is `HYPOTHESIS`.

Every register row cited carries the status it holds in `03-REGISTERS/` and is
marked at the point of use. The claims used from `01-INHERITED/` — `IH-057`,
`IH-060`, `IH-105`, `IH-197`, `IH-250`, `IH-270`, `IH-329` and contradiction
`X-01` — are `INHERITED-UNVERIFIED` and are used as a description of the previous
build, never as a finding. **No claim in this repository is promoted by this
file**, and none could be: `CLAUDE.md`'s rule is that only retrieval promotes,
and no retrieval happened while writing it.

**Nothing here has been retrieved**, so no rows were added to
`02-SOURCES/access-ledger.csv` and **no domains were requested**. Nothing was
blocked at the egress proxy, because nothing was fetched. One row was added to
`02-SOURCES/dependency.csv` — `DEP-027`, recording that `SRC-050` and `SRC-060`
carry one Glottolog coordinate set — which is a restatement of `DE-M-021`'s own
note and not a retrieval.

**This file was repaired after adversarial review and before the pull request.**
Fourteen findings were returned against the first commit; the load-bearing ones
are corrected in place and logged at `BF-026`, and the correction history is
preserved in the commit series rather than squashed, per `CLAUDE.md`'s standing
constraint that rejected reasoning stays visible.

**One correction to the task's premise is recorded at §0.6 of this document**:
`03-REGISTERS/domain-m-measurements.csv` does not exist; domain M's registered
measurements are `03-REGISTERS/domain-m-brahui-position.csv`, which is the file
read here.

This is a specification. Per constitution §12 and §15 and museum framework
Rule S-3: it is not an implemented page, no place, route, transition, layer
instance or Atlas view described here exists, and it must not be described as
one. It contains no code, and none is authorised by it.
