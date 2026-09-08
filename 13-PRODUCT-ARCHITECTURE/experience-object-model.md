# Experience Object Model — the visitor's side of the record

**Artefact class:** specification. Not research, not site code, not a page brief.
**Extends:** `13-PRODUCT-ARCHITECTURE/museum-framework.md` — the evidence,
claim, relationship and governance layers. This document adds the experience
layer and nothing else.
**Constitutional basis:** `00-CONTROLLER/METHODOLOGY-CONSTITUTION.md` §12
(product and institutional specification stage), §5 step 14 (public copy shape),
§6 (negative evidence), §7 (translation), §8 (adversarial tests), §4V
(provenance and intellectual authorship).
**Directory:** `13-PRODUCT-ARCHITECTURE/`, per constitution §15.
**Status of every design proposition in this file:** `HYPOTHESIS`, except where
a statement restates §12/§13 (a constitutional instruction, not an evidentiary
claim), restates the museum framework (itself `HYPOTHESIS`), or restates the
curatorial audit or the v2 backlog (`INHERITED-UNVERIFIED`, marked at the point
of use).

---

## 0. What this document is, and the rules it runs under

### 0.1 What it specifies

Eight object types, as first-class records with fields, relationships and stable
identifiers:

**Question · Exhibit · Activity · Challenge · Mission · Journey ·
Learning Objective · Character.**

They are specified in dependency order rather than in the order they were
commissioned, because Exhibit is defined in terms of Question, Activity in terms
of Exhibit, and Mission, Journey and Learning Objective in terms of Activity.
Character is last because it is the one that can only be specified once
everything it might otherwise have been permitted to do has been given somewhere
else to live.

It specifies behaviour and data, not markup. It contains no HTML, no CSS and no
JavaScript, per constitution §12's closing line — *"Do not create production
code"* — and per `CLAUDE.md`'s standing prohibition on writing site code in this
repository.

### 0.2 The rules it inherits

The museum framework's three rules govern here unchanged.

**Rule S-1 — No specification may cite a claim above its register status.**
Everything taken from `01-INHERITED/` is `INHERITED-UNVERIFIED` and is marked as
such at the point of use. This document's one substantial inherited input is
`06-BACKLOG/EXPANSION-PROMPT-2026-09-07.md` L247's children's vertical slice,
which is `INHERITED-UNVERIFIED` and is expansion prose rather than the original
backlog item text.

**Rule S-2 — Where a choice is the owner's and has not been made, the choice is
recorded, not taken.** Recorded in `DECISIONS-NEEDED.md` against rows allocated
in `09-DECISIONS/OWNER-DECISIONS.csv`, which is authoritative for the identifier
namespace.

**Rule S-3 — Specification does not promote.** Naming an object model does not
create the objects. Nothing in this file is a finding, and no Character, Mission
or Journey described here exists.

### 0.3 The rule it adds

**Rule S-4 — The experience layer holds no content of its own.** Every sentence
an experience object shows a visitor is a rendering of an object in the evidence
layer, or it is editorial framing marked as such under museum framework §3.4 and
§6.4. There is no third category. The whole of §2 below is the argument for this
rule and the mechanism that enforces it.

### 0.4 What it deliberately does not do

- It does not settle whether WATER is the first Living World
  (`09-DECISIONS/OWNER-DECISIONS.csv` D-005), which children's pilot is built
  (D-006), or the order of the first three builds (D-007). Journeys and Missions
  are specified as patterns; no instance is created.
- It does not specify visual design, per museum framework §12.
- It does not resolve the museum framework's own open decisions D-015 to D-031.
  Where one of them changes an experience object's shape — D-015 most obviously,
  since it changes the posture count every Exhibit is assigned from — the
  dependency is named at the point it bites and the specification is written so
  that it survives either answer.
- It does not enumerate the deferred and DO-NOT-BUILD set. That register
  (museum framework §13.1) waits on the v2 backlog, which is not in this
  repository (`DECISIONS-NEEDED.md` D-014).

---

## 1. Why the framework has no experience layer, and what its absence risks

### 1.1 What the framework already models

`museum-framework.md` models what the institution **holds** and what it
**asserts**: the Universal Evidence Object (§2), the Claim Object (§3), the
Relationship Object (§4), Absence records (§3.7), and the governance records
that bind them — obligations, consent, community authority, corrections,
editorial decisions (§11). It models where a visitor **arrives**: five entry
routes (§6). It models how the record is **displayed**: seven postures, five
modes, the Atlas, Source Mode (§1.7, §7, §8).

### 1.2 What it does not model

It does not model what a visitor is asked to **do**, what a designed sequence of
doing consists of, what the doing is supposed to leave behind, or who — if
anyone — appears to be addressing them.

The framework names these things repeatedly and specifies none of them as
objects. PROVE IT is described as *"a structured walk"* in six stages (§9.2) with
no record type for a stage. The children's investigation has five stages (§10.4.3)
with no record type for a stage. The Living World is *"a themed traversal"*
(§10.1) with no record type for a traversal. Classroom mode assembles *"a
classroom set"* (§10.5.1) out of items that have identifiers, into a container
that does not. `mk:qst:` and `mk:exh:` appear in the identifier table at §2.1 and
in a dozen field definitions, and neither is given a field list anywhere in the
document.

### 1.3 Why the gap is not cosmetic

An unmodelled layer is not an empty layer. It is a layer whose contents are
unaddressable, unstatused, unexportable, uncorrectable and unwithdrawable — and
those five properties are exactly the ones the rest of the architecture exists to
guarantee.

Concretely, four failures follow from leaving it unmodelled, each of them a
failure the framework closes off everywhere else:

**F-1. The unresolvable sentence.** Museum framework §3.4: *"any claim-bearing
sentence on any surface exposes, without leaving the page, its `mk:clm:` id, its
status, its Evidence Links … A sentence that cannot do this is not published in
the institution's voice."* An activity prompt, a mission briefing, a journey
introduction and a character's line are all sentences on a surface. If they are
not objects, they are the only sentences in the institution that no rule reaches.

**F-2. The status-free assertion.** Status is derived, never typed (§3.2). An
object with no evidence links has no derivation, so it has no status, so it
cannot be too high. An unmodelled experience layer is therefore not a place where
status is hard to check; it is a place where status does not apply. That is a
better hiding place for an unsupported claim than any field the framework
protects.

**F-3. The unrecallable surface.** Consent is per-purpose and per-surface
(§11.4), and withdrawal must be *"effective on the live surfaces without
negotiation."* A surface that is not an object cannot be enumerated in a consent
record, cannot be checked against one, and cannot be swept on withdrawal.
Consented material can therefore appear on it in breach of the consent that
governs it, and nobody will be able to prove it did.

**F-4. The unaudited interaction.** §10.4.7's three constraints are prohibitions
on *interaction patterns* — sorting, scoring, staging. The section says so
itself: *"This is an interface rule; a subject filter would not implement it,
because the same interaction is the same interaction whatever is loaded into
it."* A prohibition on a pattern can only be enforced if the pattern is a
recorded property of a record. Otherwise it is enforced by whoever remembers it,
which is the enforcement regime this entire repository exists to replace.

### 1.4 What this document therefore is

The experience layer specified so that it is subject to the same discipline as
everything else: addressable, revision-pinned, statused where it asserts,
exportable, challengeable, withdrawable, and checkable against a stated
constraint at publication.

It adds no new epistemic authority. **No experience object may raise a claim's
status, and no experience object may assert anything the evidence layer does not
already carry.** The experience layer arranges the record. It does not extend it.

---

## 2. The grounding rule

### 2.1 The rule

> **Every experience object must carry at least one Grounding Link to an object
> in the evidence or governance layer. An experience object with no such link
> cannot be created, cannot be published, and cannot be exported. There is no
> waiver, no draft state that exempts it, and no editorial override.**

Formally: for every object of type `qst`, `exh`, `act`, `chl`, `msn`, `jny`,
`lob` or `chr`, the set of Grounding Links (§4) whose subject is that object and
whose object resolves to `mk:evd:`, `mk:clm:`, `mk:rel:`, `mk:abs:`, `mk:src:`,
`mk:lex:`, `mk:txt:`, `mk:plc:`, `mk:agt:`, `mk:obl:`, `mk:cns:` or `mk:cor:`
must be non-empty, either directly or through the composition path permitted in
§2.5.

### 2.2 Why — six reasons, none of them stylistic

**G-1. It is the standing rule, read in the other direction.** `CLAUDE.md`:
*"Evidence that supports nothing is not collected."* The register format carries
`supports_page` for exactly this purpose. The symmetric statement is the one this
layer needs: **experience that exercises nothing is not built.** An institution
that refuses to collect evidence with no purpose, and then builds surfaces with
no evidence, has applied its discipline to the half of the system nobody sees.

**G-2. An ungrounded object is a display-only object, and there are none.**
Museum framework §5.3, requirement 5: *"No display-only fields exist. Anything a
page shows is in the record."* An experience object with no grounding shows
something that is in no record. It is not a field that violates the rule; it is
an entire object that does.

**G-3. Ungroundedness is the mechanism of fabrication, not merely its
opportunity.** This is the reason that matters most and it is easiest to see in
the object it was hardest to specify. An ungrounded Character is not a Character
missing a citation. It is an invented person — that is what an ungrounded
Character *is*, because a Character is nothing but the evidence it resolves to
plus a way of presenting it. The same holds one step less obviously elsewhere: an
ungrounded Activity is a task about nothing, which means its content came from
the person who wrote the prompt; an ungrounded Question is a headline; an
ungrounded Mission is a story with objects in it. In every case the missing link
is not an omission in the record of the object. It is the whole difference
between a rendering and an invention.

**G-4. Nothing else can attach.** Status derives from evidence links (§3.2).
Rights attach to objects (§11.8). Consent enumerates surfaces (§11.4).
Corrections target objects at revisions (§11.6). Bias tests are run on units
(§3.11). Proportionality compares weight to allocated space (§3.10). Every one of
these mechanisms takes an object with links as its input. An ungrounded object is
outside all of them simultaneously, and it is outside them silently.

**G-5. It cannot be contradicted.** Constitution §2 requires the record to stay
capable of contradicting *"MelaKeela's own pages … and your own previous
answer."* A visitor can only contradict something that resolves to evidence they
can check. An ungrounded surface is not merely unsupported; it is
**unfalsifiable**, and unfalsifiable content in a museum that publishes falsifiers
on everything else is worse than unsupported content, because its unfalsifiability
is invisible beside neighbours that carry falsifiers on their face.

**G-6. The alternative has already been observed and named.** `SCHEMA.md`
records, `INHERITED-UNVERIFIED`, that 78 of 96 audited pages carry zero external
links and that *"essentially none of its sourcing is checkable by a reader
without manual re-derivation."* That is what a layer without a grounding rule
looks like after it has been built. The experience layer is being specified
before it is built, which is the one opportunity to make that state unreachable
rather than merely regrettable.

### 2.3 What grounding is not

Four things that look like grounding and are not. Each is rejected by the link
model rather than by review, because a rule enforced only at review is a rule
enforced only when someone is looking.

| Not grounding | Why |
|---|---|
| **Adjacency.** An evidence object displayed next to an activity | A Grounding Link is a record with a role. Proximity on a surface is not a record and is not exported. |
| **Aboutness in prose.** A mission briefing that mentions Keezhadi | The briefing is a string. The link is to `mk:plc:` or to the claims. If the string and the links disagree, the links are what the object is. |
| **A link with a null role.** A pointer with no stated relation | Roles are the controlled vocabulary in §4.2. A link whose role is not in it does not exist. |
| **A `contextualises`-class link alone, where the object asserts.** | Museum framework §3.3: *"`contextualises` cannot promote."* An Activity that asks a visitor to conclude something needs `exercises` links to the claims the conclusion is about. Setting is not substance here either. |

### 2.4 What grounding does not license

Grounding makes an experience object legitimate. It does not make it correct, and
it does not raise anything.

- An Activity grounded in a `HYPOTHESIS` claim is a legitimate Activity about a
  hypothesis. It may not present the hypothesis as settled, and the visitor sees
  the status (§5.2).
- Grounding is not endorsement. An Activity may be grounded in a `REJECTED`
  claim — showing rejected reasoning is a stated purpose of the record (§3.6) —
  provided the rejection is what is shown.
- Grounding count is not weight. Ten links do not make an Activity important, and
  the proportionality discipline (§3.10) applies to experience objects exactly as
  it applies to claims.

### 2.5 Composition, and the one permitted transitivity

Experience objects compose: a Journey holds Exhibits, a Mission holds Activities.
Requiring every container to repeat its members' grounding would be noise.

**Composition transitivity is permitted, within the experience layer only, and
must terminate in a direct Grounding Link.** A Journey is grounded if the
Exhibits it traverses are grounded. A Mission is grounded if its Activities are.
A container whose every member is removed becomes ungrounded at that moment and
is unpublishable from that moment — it does not retain grounding it once had
through a member it no longer has.

**This is not in tension with museum framework §4.4's ban on transitive
bridges, and the difference is worth stating because the two rules look
contradictory.** §4.4 forbids deriving A→C from A→B and B→C *across evidence
domains*, because each such edge is an assertion about the past and assertions do
not chain. Composition asserts nothing about the past. "This Mission contains
this Activity" is a fact about a product, verifiable by inspection, and it is the
only kind of link that may be traversed for grounding purposes. **A Grounding
Link may never be inherited through an evidence-layer relationship.** An Activity
grounded in claim X does not thereby become grounded in everything X is related
to, and a Journey does not acquire an Exhibit's claims as its own.

### 2.6 What is outside this layer, and therefore outside the rule

The rule would be dishonest if it were stated so broadly that nobody could
comply. It applies to the **experience layer**: the objects that ask a visitor to
do something, understand something, or attend to something in particular.

It does not apply to the **shell**: navigation, search controls, the language
switcher, the export dialogue, error states, the cookie and measurement policy,
the accessibility controls. These carry no content about the past, make no
assertion, and address no visitor about a subject. They are specified in museum
framework §7, §11.9 and §11.10 and are not objects here.

The boundary is testable: **if removing it would remove something the visitor
would otherwise learn or conclude about the past, the institution or the record,
it is an experience object and the grounding rule applies.** If removing it would
only make the site harder to operate, it is shell. An "About this exhibit" panel
is an experience surface. A back button is not.

Decorative and atmospheric assets are neither. Museum framework §12.3, V-5:
*"Nothing decorative is placed where evidence goes … Atmosphere assets are
labelled as such and never occupy an evidence slot."* An atmosphere asset is a
`mk:evd:` with `is_primary = derivative` and a stated non-evidential purpose; it
is never the grounding of anything.

### 2.7 How the rule is checked

Three checkpoints, because a rule checked once is checked at the wrong time.

1. **At creation.** An object cannot be persisted without at least one Grounding
   Link or one composition member that has one. This is a schema constraint, not
   a workflow step.
2. **At publication.** The publication gate (§14) re-resolves every Grounding
   Link. A link to a retracted, withdrawn or non-resolving object fails the gate.
3. **Continuously, after publication.** Grounding can be lost without anyone
   touching the experience object: the claim it exercises can be superseded, its
   evidence withdrawn for consent, its source moved to `HOLD`. Museum framework
   §10.3 already requires the Field Bag to show a visitor what changed under
   them; the same mechanism serves here. **An experience object whose grounding
   has decayed is flagged, not silently served.** What the surface does then —
   whether it degrades, holds, or displays the decay to the visitor — depends on
   which way it decayed, and is specified per object.

### 2.8 The exception that is not one

There is no exemption for "introductory", "welcome", "framing" or "orientation"
surfaces, which is where an exemption would be asked for first and where it would
do most damage: the first screen a visitor sees is the one that sets what they
think the institution is for. An orientation surface is grounded in the objects
it orients the visitor toward, or it is shell (§2.6) and says nothing about the
past.

---

## 3. Identity

### 3.1 Extension of the identifier scheme

Museum framework §2.1 specifies the scheme — `mk:<type>:<key>`,
`@r<n>` for a revision, `#<anchor>` for a sub-locator, opaque 10-character keys,
never reused, never deleted, revision-addressable, externally resolvable at
`<institution-domain>/id/<type>/<key>`. All of it holds here without modification.

Two of the eight types already have codes in §2.1's table and are given field
specifications for the first time in this document:

| Code | Object | Status in §2.1 |
|---|---|---|
| `qst` | Question | allocated; entry route specified at §6.6; no field list |
| `exh` | Exhibit | allocated; referenced by `supports_exhibit`; no field list |

Six codes are new and are allocated here:

| Code | Object |
|---|---|
| `act` | Activity |
| `chl` | Challenge |
| `msn` | Mission |
| `jny` | Journey |
| `lob` | Learning Objective |
| `chr` | Character |

Whether these six are folded into museum framework §2.1's table, or that table
cites this document, is an editorial tidying decision and is not escalated: §2.1
is a scheme, and this is an allocation under it.

### 3.2 The `chl` / `cor` collision, declared

**`mk:chl:` — a Challenge — is an experience object: a designed, bounded
invitation to test a specific institutional claim.**

**`mk:cor:` — a correction challenge — is a governance record: a submitted
assertion that a specific claim at a specific revision is wrong**
(museum framework §11.6).

They are two different things that English gives one word. A Challenge run may
*emit* a correction (§9.6); a correction may exist with no Challenge behind it
(§11.6's channels include direct submission, right of reply, community authority
and internal re-audit); and most Challenge runs emit nothing at all.

The framework has already met this problem once and solved it the same way.
§11.5: the workbook's editorial `Hold` and `CLAUDE.md`'s evidentiary `HOLD` are
*"two different words that happen to be spelled the same"*, and the register
renders the editorial one as `publication:hold` so that no surface or export can
confuse them. The same discipline applies: **in every surface, export and
register, an experience Challenge is written `challenge:experience` and a
correction is written `challenge:correction`, or they are addressed by
identifier.** A bare "challenge" in a column heading, a filter or a page title is
a defect.

### 3.3 Revision, retraction and the append-only rule

Experience objects carry revision series under museum framework §3.6 without
modification: append-only, nothing edited in place, nothing deleted, retracted
objects resolving to a tombstone, citations pinning with `@r<n>`.

Two additions specific to this layer:

- **A published Mission, Journey, Challenge or Activity that a visitor has
  carried into a Field Bag is citable, and therefore pins.** A visitor who
  exported a Challenge run in March and returns in September is shown what they
  ran, plus what has changed in the claim since — the same behaviour §10.3
  specifies for collected claims, applied to the container.
- **`change_type` gains four values** for this layer, alongside §3.6's list:
  `grounding-added` · `grounding-lost` · `constraint-block-revised` ·
  `character-withdrawn`. `grounding-lost` is the value that fires on §2.7's
  continuous check, and it is a revision of the experience object even though
  nobody edited it, because the object did change: what it resolves to is what
  it is.

---

## 4. The Grounding Link, and the experience predicate group

### 4.1 The link is a Relationship Object

A Grounding Link is not a foreign key and not a new record type. It is a
Relationship Object (`mk:rel:`, museum framework §4.2) whose subject is an
experience object and whose object is an evidence, claim, relationship, absence,
source, place, word, text, agent, obligation, consent or correction record.

Making it a Relationship Object rather than a field buys four things the
framework already argued for at §4.1: it carries a status, it carries a revision
history, it can be challenged, and it cannot be drawn without being statused.
*"If a relationship is an edge in a graph rather than a record with a status, a
speculative link renders identically to an attested one."* A Grounding Link whose
role asserts something about the evidence — that an Activity exercises a claim,
that a Character's words are attested in a source — is exactly such a
relationship.

Structural links that assert nothing (a Mission's ordered list of its own
Activities) are ordinary typed fields, per §2.5.

### 4.2 The experience predicate group

Museum framework §4.3 groups predicates by the kind of claim they make —
chronological, spatial, transmission, linguistic, population-genetic, material,
social and institutional, epistemic. A ninth group is added.

**Experience** — `exercises` · `bears-on` · `traverses` · `presents` ·
`taught-on` · `targets` · `attested-in` · `speaks-for` · `assembles` ·
`prepares-for` · `governed-by`.

| Predicate | Subject → object | Meaning and requirement |
|---|---|---|
| `exercises` | `act` → `clm`, `rel`, `abs` | The visitor is asked to do reasoning that this claim, relationship or absence is the substance of. **Non-empty on every Activity.** |
| `bears-on` | `qst` → `evd`, `clm`, `abs`, `src` | This evidence bears on the question — including evidence that bears against every explanation currently on the table. |
| `traverses` | `jny` → `exh` | The Journey passes through this Exhibit. Ordered by the Journey's `traversal_order`. |
| `presents` | `exh` → `clm`, `rel`, `abs` | The Exhibit shows this claim in the institution's voice. **Non-empty on every published Exhibit.** |
| `taught-on` | `lob` → `clm`, `abs`, `evd`, `rel` | The objective is taught using this object as its worked case. |
| `targets` | `chl` → `clm@r<n>`, `qst`, `rel` | The single object the Challenge puts at risk, pinned to a revision. **Exactly one.** |
| `attested-in` | `chr` → `evd` + locator | A Character's words, actions or existence are attested in this evidence at this locator. Required for `documented-individual`. |
| `speaks-for` | `chr` → `agt` | A present-day investigator speaks for themselves (`agt` = the person) or, where a community authority record exists, as a named representative with its limits recorded (§11.2). Never "for" a past people. |
| `assembles` | `msn` → `act`; `jny` → `msn` | Structural composition, ordered. Asserts nothing about the past (§2.5). |
| `prepares-for` | `act`, `msn` → `lob` | This activity or mission is where the objective is met. |
| `governed-by` | any experience object → `cns`, `obl`, `cor`, `dec` | The consent, obligation, correction or editorial decision that constrains this object. Required where consented or rights-restricted material appears. |

### 4.3 Link fields

Grounding Links carry the Relationship Object fields of §4.2 with the following
put to specific use, plus three of their own:

| Field | Notes |
|---|---|
| `id`, `subject`, `object`, `predicate` | as §4.2 |
| `status` | the seven-value vocabulary. **A Grounding Link's status may never exceed the status of the object it points at.** An Activity cannot exercise a `HYPOTHESIS` claim through a `VERIFIED` link. |
| `locator` | required for `attested-in` and for any link into a text, dataset or recording — specific enough to re-find, per §3.3 |
| `surface_role` | `substance` · `context` · `contrast` · `worked-example` · `counter-case`. What the object is doing on this surface. `context` links may never be the sole grounding of an object that asks the visitor to conclude something (§2.3). |
| `visitor_visible` | bool. Whether this link is shown to the visitor or is internal scaffolding. **Defaults true**, and a false value requires a reason, because a hidden grounding is a grounding the visitor cannot check. |
| `decay_behaviour` | `hold` · `degrade` · `disclose` · `retract`. What happens to the experience object if this link's target is superseded, rejected, withdrawn or held (§2.7). |

### 4.4 One rule about direction

Grounding Links run from the experience layer into the evidence layer and never
the other way. **No evidence, claim, relationship or governance object may carry
a field pointing at an experience object as a condition of its own validity.**
The evidence base must remain complete and meaningful with the entire experience
layer deleted; the reverse is not true and is not meant to be. This keeps the
export at §5.2 clean, keeps the claim registers readable as CSV, and makes it
possible to rebuild the whole visitor-facing institution without touching a
single row of evidence.

The one apparent exception is `supports_exhibit` on the Claim Object
(museum framework §3.1), which points from a claim to an `mk:exh:`. It is the
generalisation of the register format's `supports_page` and it exists to enforce
*"Evidence that supports nothing is not collected."* It is a **statement of
purpose, not a dependency**: a claim whose exhibit is deleted is a claim that now
supports nothing and must be re-purposed or dropped, but it is not a claim that
has become invalid.

---

## 5. The Constraint Block

### 5.1 Why the children's constraints are fields and not prose

Museum framework §10.4.7 states three prohibitions, sourced to
`MELA-KEELA-WHO-MADE-THE-PAST.md` §9 as the owner stated it. That document is not
in this repository, so their wording is `INHERITED-UNVERIFIED`
(`RESEARCH-QUEUE.md` `WMP-9` records the provenance and the section-numbering
discrepancy raised as D-037). Their standing as constraints does not depend on
that, because they are prohibitions on what the institution builds, not claims
about the past. Rule S-1 is not in tension with them: nothing here cites them as
evidence for anything.

- **No interface that asks a child to sort human beings into racial types.**
- **No points, scores, badges or progress awarded for extremist categories.**
- **No interface that turns persecution into spectacle.**

And §10.4.7's closing rule: **COMPARE may not take people, remains, named
individuals or populations as its terms** — *"anywhere in the children's mode, in
any Living World, in any pilot … This is an interface rule; a subject filter
would not implement it, because the same interaction is the same interaction
whatever is loaded into it."*

That closing sentence is the specification. A prohibition on an interaction
pattern can only be enforced against an interaction pattern that is recorded. So
each of the eight objects carries a **Constraint Block**: a set of fields whose
permitted values are constrained by the prohibitions, so that a violation is a
schema failure and an export shows what was declared.

**A field with one permitted value is not redundant.** It is the difference
between a rule that holds while someone remembers it and a rule that a validator
asserts, a reviewer reads, an export carries and a challenger can cite. Museum
framework §12.3 makes the same move for the visual system: every constraint is
paired with *"how a violation is detected"*. This is that, in the data model.

### 5.2 The block

Carried by every object in §6 to §13 without exception.

| Field | Type | Permitted values and rule |
|---|---|---|
| `compare_terms[]` | array of identifiers | The terms any comparison on this object takes. Empty where the object contains no comparison. |
| `compare_term_class[]` | enum, parallel to `compare_terms[]` | `object` · `material` · `technique` · `script` · `word-form` · `text-passage` · `reading-variant` · `stratum` · `place` · `date-assertion` · `absence` · `source` · `claim` · `dataset-column`. **The enumeration has no value for a person, a group of people, human remains, a personal name, a population, an ancestry component, an archaeological culture read as a people, or a language used as a proxy for a people. A comparison whose term has no class here cannot be expressed.** |
| `sorting_of_persons` | enum | `none`. The only permitted value. Any interface in which a visitor places people, remains, names, skulls, portraits, populations or ancestry components into categories — as a sort, a match, a drag, a quiz, a "which group does this belong to", or the same with the categories renamed, softened or presented as historical labels to apply — is refused here. |
| `reward_mechanic` | enum | `none`. The only permitted value on any object that touches a racial, racial-nationalist or other extremist classification, and — per §10.4.4's ban on competition, scoreboards and time pressure — on every object in the children's mode. §10.4.7's second constraint survives any later relaxation of §10.4.4, so the field's permitted set does not widen with age band on classification material. |
| `persecution_treatment` | enum | `not-present` · `read-as-record`. Never `staged`, `dramatised`, `role-played`, `simulated`, `scored` or `reconstructed-as-experience`. Those values do not exist. Persecution is told with its evidence and its status, as §10.4.6 permits a custody record to be read. |
| `role_play` | enum | `none` · `present-day-method` — the second permitting only "do what a researcher does with this evidence now", never "be a person in the past". No role-play of a historical person, and no role-play of any position in a classification, in any period, at any age. |
| `identity_attribution` | enum | `none`. No object may attribute an ethnicity, race, caste, ancestry component, religion-as-identity or modern nationality to a person, an object, a set of remains or a place as a property. Every such link is a museum framework §4.4 bridge with its mechanism, its rivals and its governance, or it is not displayed (§6.7). |
| `age_bands[]` | array | The audiences the object is built for. **Declarative, not a gate** — see §5.4. |
| `field_mode_postures_respected` | bool | Asserted true at publication by re-checking §1.7: no Field-Mode object exists in the Extraction / Collection or Reconnection postures. |
| `constraint_reviewer`, `constraint_review_date` | metadata | A person and a date. The block is not self-certifying. |

### 5.3 The COMPARE case, stated once for all eight objects

The specified children's vertical slice is
`DIG IT → WHAT DID YOU FIND? → COMPARE → PROVE IT → FIELD BAG → WHAT DO YOU
THINK?` (`06-BACKLOG/EXPANSION-PROMPT-2026-09-07.md` L247,
`INHERITED-UNVERIFIED`; the item text is title-only in
`06-BACKLOG/BACKLOG-COVERAGE.csv` and this is expansion prose, not the original).

Museum framework §10.4.7 finds that this flow *"would violate the first of these
if applied to material in this area"*, because COMPARE is a sorting-and-matching
step and the flow supplies its own buckets: *"DIG IT produces the items, COMPARE
produces the categories, and PROVE IT then asks the child to defend the result.
Framing the exercise as a debunking of racial classification does not lift the
prohibition; the child still performs the sort."*

In this object model that finding becomes three mechanical facts:

1. **COMPARE is an `interaction_pattern` value on the Activity object** (§8.2),
   not a stage in a hard-coded flow. It is therefore a property that can be
   queried, validated and reported on across every Activity in the institution.
2. **Its terms are `compare_terms[]` with a `compare_term_class[]`**, and the
   enumeration has no value for a person. The prohibition is not a check that
   runs after the activity is designed; it is a shape the activity cannot be
   given. A designer who wants a child to compare two skulls finds there is no
   way to write it down.
3. **The check is on the resolved referent, not on the label.** An entry whose
   identifier resolves to an `mk:agt:` of kind person or community, to a UEO
   whose `evidence_subclass` is in the human-remains set, to an ANCESTRY-layer
   object (§8.4 layer 8), or to an archaeological culture being used as a stand-in
   for a population, is refused whatever `compare_term_class` was declared for it.
   A rule that trusted the declaration would be defeated by a mislabelled row.

### 5.4 Age bands are declarative, and the constraints do not vary by them

`age_bands[]` says who an object was built for. It is **not an age gate**, and
nothing in this institution gates by age: museum framework §10.4.5 requires that
no account is offered to under-16 visitors, so the institution does not know a
visitor's age and must not pretend to.

The consequence is unavoidable and is stated rather than worked around: **a child
can reach every surface.** An experience layer whose protections activate only in
a children's mode protects children only where the institution guessed right
about who was looking.

**Therefore, on the instruction of the task that produced this document, the
Constraint Block binds all eight object types at every age band.** This extends
§10.4.7's stated scope, which is the children's mode, to the whole experience
layer. The extension is taken here because within this layer it is what the
instruction requires and what the no-gate architecture implies.

It is not extended beyond this layer. Whether the same prohibitions bind
surfaces outside the experience layer — a research register view, an Atlas layer
combination, an adult Reading Room exhibit that reproduces a nineteenth-century
racial schema as its subject matter — is a wider question about the institution's
self-description, with real costs on both sides, and it is the owner's.
Recorded as **D-046**.

### 5.5 The block does not soften anything else

The Constraint Block sits alongside, and never in place of, museum framework
§10.4.4's rules (no fabricated evidence; reconstructions labelled; no ethnic or
national identification; human remains only where community authority and consent
permit; no competition, scoreboard or time pressure), §10.4.5's safeguarding and
data rules, and §10.4.6's prohibition on assigning a child a verdict on a live
custody question. Where the block and one of those appear to differ, the stricter
governs, and the difference is a defect in this document to be corrected rather
than a permission.

---

## 6. Question — `mk:qst:`

### 6.1 What it is

**A Question is constitution Step 1 made addressable.** Step 1 requires every
investigation to be bounded before it begins: *"Exact proposition, date range,
geography, evidence needed, terms needing original-language work, the viable
explanations, the null explanation."* Museum framework §6.6 makes that record a
public entry route. This section makes it an object.

The Question is the spine of the whole experience layer. A Mission has exactly
one; a Challenge targets one or a claim under one; an Activity is normally
reasoning toward one; a Journey is a set of exhibits that between them address
several. It is placed first because everything else is defined against it.

**A Question is not a claim.** It carries no status of its own in the seven-value
vocabulary, because a question is not true or false — the same boundary museum
framework §2.3 draws when it refuses a truth field on the Universal Evidence
Object. What a Question carries is an `open_state`, which is a fact about the
institution's work rather than about the world.

### 6.2 Fields

| Field | Type | Notes |
|---|---|---|
| `id` | identifier | `mk:qst:<key>`, §3.1 |
| `revision` | integer | append-only, museum framework §3.6 |
| `proposition` | string | the exact proposition under examination, stated so it could be false. One proposition. A question that resolves into three is three Questions. |
| `plain_form` | string | the same question in the plainest language that does not change it. Required — it is what the children's mode and the plain-language summary (§11.9.6) use, and writing it is a test of whether the proposition is actually bounded. |
| `date_range` | Date Assertion bounds | with the **date type** named (§2.7). "Before 300 BCE" is meaningless until it says composition, attestation or deposition. |
| `geography` | array of Place Assertions | typed, with geometry and certainty; `zone-unknown` permitted and drawn |
| `evidence_classes_required[]` | enum(9) | what it would take to answer this, from Step 1's "evidence needed" |
| `terms_needing_original_language[]` | array of `mk:lex:` | Step 1. Each resolves to a word object with a Translation Block (§3.8). |
| `viable_explanations[]` | array of `mk:clm:` | each independently reconstructed (Step 8), each with its own status |
| `null_explanation` | `mk:clm:` | **required, non-null.** Step 1. The explanation that nothing needs explaining — coincidence, independent innovation, an artefact of the archive. |
| `gated_out[]` | array of Gate Results | explanations that failed a Step 7 gate: `explanation` · `gate_failed` (chronological · geographical · mechanism · positive-evidence · diagnostic) · `finding` · `decided_by` · `date`. Rendered as Exclusion Notes (§3.10), never as sections. |
| `bears_on[]` | array of `mk:rel:` (`bears-on`) | the evidence that bears on the question — **including evidence that bears against every explanation currently listed** |
| `absences[]` | array of `mk:abs:` | what should exist if each explanation were true, typed (§3.7) |
| `holds[]` | array of paths | into `05-HOLDS/`, where an answer is blocked on source access |
| `open_state` | enum | `open` · `partly-answered` · `answered-provisionally` · `blocked` · `retired` |
| `retired_reason` | string or null | **required when `open_state = retired`.** A question is retired when it was malformed, not when it was answered. |
| `standing_summary` | derived | the Step 11 standing of each explanation, shown together, never averaged into one number |
| `falsifiers[]` | array of Falsifier records | §3.9, inherited from the explanations plus any that belong to the question itself |
| `entry_routes[]` | enum | which of object · place · word · text · question surfaces reach it (§6) |
| `child_askable` | bool | whether this question can be put to a child at all — see §6.5 |
| `exhibits[]` | array of `mk:exh:` | where it is displayed |
| `challenges[]` | array of `mk:chl:` | the Challenges built on it |
| `constraint_block` | Constraint Block | §5.2 |
| `created`, `created_by`, `revised`, `revised_by` | metadata | |

### 6.3 Grounding

A Question is grounded by **at least one** of:

1. a `bears-on` Grounding Link to evidence, a claim or a source;
2. an Absence record typed under §3.7;
3. a `05-HOLDS/` record naming what is blocked and what is needed.

The disjunction is not a loosening. It is the museum framework's own position
made mechanical: §6.6 states that *"a question with no viable explanation still
publishes, with its absences typed and its holds named"*, and that *"open
questions may outnumber answered ones and this is not a defect."* A question the
institution has looked into and cannot yet answer is one of the most honest
objects it can publish. What it may not publish is a question it has not looked
into: **a Question with no evidence bearing on it, no typed absence and no hold
is not an open question, it is a headline**, and it is refused at creation.

### 6.4 Rules

- **The null explanation is always listed and is never last by default**
  (§6.6). Its position in the list is not the display layer's to choose.
- **`unknown` is never listed as a rival.** `CLAUDE.md`: *"'Unknown' is
  residual, never a positive rival explanation."* The absence of an explanation
  is `absences[]` and `open_state`, not an entry in `viable_explanations[]`.
- **Gated-out explanations are visible and are not sections.** A visitor sees
  what was ruled out and by which gate, in the fixed small footprint of an
  Exclusion Note. Removing them entirely would leave the shortlist looking like
  the whole field, which is the failure §9.2 stage 2 names.
- **Proportionality applies to explanations** (§3.10). Rival explanations are
  allocated space by evidence, not by rhetorical symmetry, and the divergence
  between evidential weight and allocated space is a review finding.
- **Both adversarial tests run on the Question, not only on its claims**
  (§3.11). The prestige-bias test asks whether an explanation is on the list
  because it is canonical; the preferred-counter-narrative test asks whether one
  is on the list because it is corrective. A Question whose explanation set was
  never tested is a bounded question with an unbounded selection behind it.
- **A Question may not be reworded to fit an answer.** Narrowing scope is
  `scope-narrowed` in the revision record (§3.6) with a reason, and the earlier
  wording remains resolvable. Silently narrowing a question until the evidence
  fits is the cheapest way to manufacture a finding and it is the one this rule
  exists to make visible.
- **Decay.** When an explanation is superseded or rejected the Question does not
  degrade; it revises, and the rejected explanation stays visible with its
  rejection (§3.6). When every explanation including the null is rejected, the
  Question's `open_state` returns to `open` and the fact that it was once
  answered is part of its history. This is the `decay_behaviour = disclose` case
  in §4.3.

### 6.5 `child_askable`, and what it is not

`child_askable` records whether the institution will put this question to a
child. It is **not** a difficulty rating and **not** a reading-age flag —
museum framework §10.4.1 is explicit that simplification means *"fewer objects,
more scaffolding on the reasoning, and plainer language"*, never a different
epistemic standard, and that a child can be told *"nobody knows and here is how
we know that nobody knows."* An unanswerable question is a good children's
question.

`child_askable = false` has three legitimate grounds and no others:

1. **The Constraint Block cannot be satisfied.** Answering it would require
   sorting people, scoring a classification, or staging persecution (§5.2). The
   question may still be published for adults; it is not put to a child as a task.
2. **§10.4.6 applies.** It is a live custody, restitution or legal matter, where
   the distinction is *"between telling a child a true thing and assigning a
   child a verdict."* A child may read the custody record; the question "was this
   looted" is not handed to them.
3. **Consent or community authority does not extend to the children's surface**
   (§11.4: consent is per-surface). This is a fact about permission, not about
   the child.

"Too complicated", "too political", "too upsetting" and "no simple answer" are
not grounds. Where one of them is what is meant, the honest record is a
`false` value with ground 1 or 2 named, or a `true` value and a harder piece of
writing. **The field carries `child_askable_ground` and an empty ground with a
`false` value is invalid** — the same rule §1.5 applies to an empty posture
override.

### 6.6 What the Question object gives the rest of the layer

- The **Mission** takes exactly one, and takes its scope from it (§10).
- The **Challenge** targets it or a claim under it (§9).
- The **Activity** exercises claims that are among its explanations (§8).
- The **Learning Objective** is frequently taught on the *shape* of a Question —
  its gates, its null, its absences — rather than on any answer (§12).
- The **children's investigation's** second stage, ASK, maps a child's own
  written question onto real `mk:qst:` nodes (§10.4.3, stage 2). That mapping is
  a Grounding Link with `visitor_visible = true`: the child is shown that their
  question is a question the institution is also asking, which is the single most
  useful thing this object can do for them, and it is a claim about their
  question that must be checkable rather than flattering.
