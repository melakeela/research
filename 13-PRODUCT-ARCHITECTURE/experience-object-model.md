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
namespace. The framework's two operative clauses hold here in full: *"This
document proposes; it does not adopt. Where it recommends, the recommendation is
labelled as such and the alternative is stated at equal seriousness."*

**Where this document does adopt, it says so at the point of adoption, and names
the framework rule it narrows.** There are three such places and they are listed
here so a reader does not have to find them: §5.4 binds the Constraint Block at
every age band within this layer, on the task's instruction and on an argument
from the absence of an age gate; §7.4 sets a publication threshold for the
"WHAT THE EVIDENCE SUPPORTS" register, subject to `OWNER-DECISIONS.csv` D-010;
and §10.5 narrows §10.3's opt-in server-side store, escalated as D-052. Nothing
else in this document adopts where the framework left a choice.

**Rule S-3 — Specification does not promote.** Naming an object model does not
create the objects. Nothing in this file is a finding, and no Character, Mission
or Journey described here exists.

### 0.3 The rule it adds

**Rule S-4 — The experience layer holds no content of its own.** Every sentence
an experience object shows a visitor is a rendering of an object in the evidence
layer, or it is editorial framing marked as such under museum framework §3.4 and
§6.4. There is no third category. The whole of §2 below is the argument for this
rule and the mechanism that enforces it.

### 0.3.1 How section references read

A bare `§x.y` is a section of **`museum-framework.md`**, which is what most of
them are. A reference to this document is written **"§x.y of this document"** or
appears inside a sentence that names the object being specified. Where the two
could be confused the source is named in full. Constitution references are
written `constitution §x` or `Step n`.

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
(§10.1) with no record type for a traversal. `mk:qst:` and `mk:exh:` appear in the
identifier table at §2.1 and in a dozen field definitions, and neither is given a
field list: §6.6 describes in prose what a Question carries, and nothing anywhere
describes an Exhibit.

The classroom set is the exception that shows the shape of the gap. §10.5.1 gives
it *"a Field Bag with a teacher's notes attached and its own identifier"* — a
container that **is** addressed, precisely because the framework was specifying
the Field Bag at the time. Everything the framework specified as a record got
one; everything it described as a walk, a stage, a traversal or a set of stages
did not.

### 1.3 Why the gap is not cosmetic

An unmodelled layer is not an empty layer. It is a layer whose contents are
unaddressable, unstatused, unexportable, uncorrectable and unwithdrawable — and
those five properties are exactly the ones the rest of the architecture exists to
guarantee.

Concretely, four failures follow from leaving it unmodelled, each of them a
failure the framework closes off everywhere else:

**F-1. The unrouted sentence.** Museum framework §3.4: *"any claim-bearing
sentence on any surface exposes, without leaving the page, its `mk:clm:` id, its
status, its Evidence Links with locators and retrieval dates, and a link into
Source Mode. A sentence that cannot do this is not published in the institution's
voice; it is published as editorial framing and marked as such."* That is a
routing rule with two outputs, and both of them require an object: the first
needs a claim to resolve to, the second needs a surface on which "marked as such"
can be recorded and counted. An activity prompt, a mission briefing, a journey
introduction and a character's line are sentences on a surface with neither. They
are not forbidden by the framework — they are unrouted by it, which is worse,
because a rule with no third branch and no way to reach one is a rule that will
be resolved in practice by whoever is writing the prompt.

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

Formally: for every object of type `qst`, `exh`, `act`, `chl`, `jny`, `lob` or
`chr`, the set of Grounding Links (§4) whose subject is that object and whose
object resolves to `mk:evd:`, `mk:clm:`, `mk:rel:`, `mk:abs:`, `mk:src:`,
`mk:lex:`, `mk:txt:`, `mk:plc:`, `mk:agt:`, `mk:obl:`, `mk:cns:`, `mk:cor:` or
`mk:dec:` must be non-empty.

**`msn` is the single exception**, and it is the only one: a Mission is a pure
container with no assertion of its own, and it grounds through the composition
path at §2.5. Every other object in this layer, containers included, carries a
direct link — the reason is at §2.5.

Note what is *not* on the list: `qst`, `exh`, `act`, `chl`, `msn`, `jny`, `lob`
and `chr`. **An experience object never grounds another experience object.** A
Challenge pointed only at a Question, or a Mission pointed only at a Question, is
ungrounded; each carries a separate evidence-layer link, specified at §9.4 and
§10.3.

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
  the status on every surface that shows the claim (framework §7.2).
- Grounding is not endorsement. An Activity may be grounded in a `REJECTED`
  claim — showing rejected reasoning is a stated purpose of the record (§3.6) —
  provided the rejection is what is shown.
- Grounding count is not weight. Ten links do not make an Activity important, and
  the proportionality discipline (§3.10) applies to experience objects exactly as
  it applies to claims.

### 2.5 Composition, and the one permitted transitivity

Experience objects compose: a Journey holds Exhibits, a Mission holds Activities.
The question is whether a container inherits its members' grounding.

**The answer is no, except for the Mission.** The test is whether the container
asserts anything of its own:

- An **Exhibit** speaks in the institution's voice, so it resolves on its own
  (§7.3). A **Journey** asserts a through-line, so it resolves on its own
  (§11.5). A **Challenge** puts a specific claim at risk, so it resolves on its
  own (§9.4).
- A **Mission** asserts nothing its Activities do not. It is an ordering and a
  scope. Requiring it to restate its members' grounding would add a row and no
  information.

**Composition transitivity is therefore permitted for the Mission only, within
the experience layer only, and must terminate in a direct Grounding Link.** A
Mission whose Activities are all removed or suspended becomes ungrounded at that
moment and is unpublishable from that moment — it does not retain grounding it
once had through a member it no longer has. This is not hypothetical: an Activity
suspends automatically when a consent lapses (§8.7), so a Mission can lose its
grounding with nobody editing it.

**This is not in tension with museum framework §4.4's ban on transitive
bridges, and the difference is worth stating because the two rules look
contradictory.** §4.4 forbids deriving A→C from A→B and B→C across the constitution's
*seven domains* — language, ancestry, culture, artifact, religion, polity and
modern identity — because each such edge is an assertion about the past and
assertions do not chain. Composition asserts nothing about the past. "This Mission contains
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
assertion, and address no visitor about a subject. They are specified across
museum framework §5.2 (export), §7 (search and the viewer), §10.4.5 (the
measurement policy), §11.9 (accessibility controls) and §11.10 (interface
language), and are not objects here.

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
   Link — or, for a Mission alone, one composition member that has one. This is a
   cardinality constraint across the object table and the link table, enforced at
   commit rather than as a workflow step: it is not a field a form can leave
   blank and come back to.
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

**The closed vocabularies this document adds**, which framework §5.3 requirement
3 requires to be published as enumerations with definitions and stability
guarantees, and which are therefore listed once here rather than left to be
gathered: the 11 experience predicates (§4.2), the 5 `surface_role` values
(§4.3), the 4 `decay_behaviour` values (§4.3), the 14 `compare_term_class`
values (§5.2), the 19 `interaction_pattern` values (§8.2), the 7
`challenge_form` values (§9.3), the 5 Challenge `outcome_forms` (§9.3), the 5
`objective_type` values (§12.3), the 4 `assertion_form` values (§12.2), the 4
`character_kind` values (§13.2), and the 3 `change_type` additions (§3.3).
Framework §5.3's list is incomplete until these are added to it.

**`surface_role` is not a second evidence-role vocabulary.** Framework §3.3's
eleven roles say what a piece of evidence does *for a claim*; `surface_role` says
what an object does *on a surface*. They meet at one point, stated at §2.3: a
`surface_role` of `context` is the display counterpart of the `contextualises`
role, and carries the same prohibition — it cannot on its own ground an object
that asks the visitor to conclude something.

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
- **`change_type` gains three values** for this layer, alongside §3.6's list:
  `grounding-added` · `grounding-lost` · `constraint-block-revised`.
  `grounding-lost` is the value that fires on §2.7's continuous check, and it is
  a revision of the experience object even though nobody edited it, because the
  object did change: what it resolves to is what it is. A Character suspended by
  a consent withdrawal takes §3.6's existing `retracted-for-consent`; this layer
  adds no synonym for it.

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

Structural links that assert nothing — a Mission's ordered list of its own
Activities, a Journey's ordered list of Exhibits — are **ordinary typed fields
holding identifiers, not `mk:rel:` records.** They are not Relationship Objects
and do not carry §4.2's required fields: a `mechanism`, an `alternatives` set and
a `falsifiers` array on a Mission-contains-Activity edge would be nonsense, and a
`status` on it would be a status on a fact about a product rather than about the
past. Where §10.2 and §11.2 name `assembles` and `traverses`, the predicate names
the field's meaning; it does not make the field a record.

One consequence, stated because it would otherwise be a silent hole: **§4.3's
rule that a Grounding Link's status may never exceed its target's has no
application to composition fields**, and no experience object carries a status of
its own. Status lives in the evidence layer; the experience layer inherits
display obligations from it and adds none.

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
| `reward_mechanic` | enum | `none`. **The only permitted value, on every object, at every age band.** No points, scores, badges, streaks, completion percentages or congratulations. §10.4.4 bans competition, scoreboards and time pressure throughout the children's mode; §10.4.7's second constraint is the case that *"survives any later relaxation of that rule"* and does not widen with age band; §9.3 removes scoring from PROVE IT for all visitors. Since all three converge and §5.4 binds the block at every band, the enum has one value rather than an unstated remainder that no schema could be written from. |
| `persecution_treatment` | enum | `not-present` · `read-as-record`. Never `staged`, `dramatised`, `role-played`, `simulated`, `scored` or `reconstructed-as-experience`. Those values do not exist. Persecution is told with its evidence and its status, as §10.4.6 permits a custody record to be read. |
| `role_play` | enum | `none` · `present-day-method` — the second permitting only "do what a researcher does with this evidence now", never "be a person in the past". No role-play of a historical person, and no role-play of any position in a classification, in any period, at any age. |
| `identity_attribution` | enum | `none`. No object may attribute an ethnicity, race, caste, ancestry component, religion-as-identity or modern nationality to a person, an object, a set of remains or a place as a property. Every such link is a museum framework §4.4 bridge with its mechanism, its rivals and its governance, or it is not displayed (§6.7). |
| `age_bands[]` | array | The audiences the object is built for. **Declarative, not a gate** — see §5.4. |
| `field_mode_postures_respected` | bool | Asserted true at publication by re-checking §1.7: no Field-Mode object exists in the Extraction / Collection or Reconnection postures. |
| `constraint_reviewer`, `constraint_review_date` | metadata | A person and a date. The block is not self-certifying. |

**The block is authoritative for the fields it holds.** `age_bands[]`,
`compare_terms[]`, `compare_term_class[]` and `identity_attribution` appear again
in the field tables of §6 to §13 for readability, because a field table a
designer reads should be complete. Where the two differ, the block governs, and a
generated schema takes these fields from the block once rather than eight times.

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
   object (framework §8.4, layer 8), or to an archaeological culture being used
   as a stand-in for a population, is refused whatever `compare_term_class` was
   declared for it.
   A rule that trusted the declaration would be defeated by a mislabelled row.

### 5.4 Age bands are declarative, and the constraints do not vary by them

`age_bands[]` says who an object was built for. It is **not an age gate.**

The reasoning is a derivation, not a restatement of the framework, and is set out
so it can be disagreed with. Museum framework §10.4.5 requires that *"no account
[is] required and none offered to under-16 visitors"*, and §10.4.5 forbids
behavioural analytics and third-party trackers *"on any surface, at any age"*.
An institution with no accounts and no tracking has no reliable knowledge of who
is on a surface. It could ask — a self-declared birth date on entry — but a
declaration is not knowledge, it is a gate that admits anyone who types a number,
and building one would put an age claim about a visitor into the product where
§10.4.5 has removed every other visitor datum.

**So the working assumption is that a child can reach every surface**, and an
experience layer whose protections activate only in a children's mode protects
children only where the institution guessed right about who was looking.

**What this does to two framework rules, stated rather than left implicit.**
§10.3 says the Field Bag *"for under-16 visitors … does not exist at all"* as a
server-side store, and §10.4.5 says no account is *offered* to them. Under this
derivation neither is implementable as a check on a particular visitor; both are
implementable as a property of the product — offer no accounts and no server-side
store to anyone, which satisfies the under-16 rule by construction and is what
§10.5 specifies. If the owner prefers a declared-age gate, the derivation fails
and §5.4 and §10.5 both change; that possibility is part of D-046 and D-052.

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

### 5.5 Fields every experience object carries

Specified once here rather than eight times, and required on all eight object
types. The publication gate (§14.3) checks them on whatever it is gating, so an
object without them cannot pass it.

| Field | Type | Notes |
|---|---|---|
| `release_state` | enum | `draft` · `in-review` · `published` · `withdrawn` · `superseded` |
| `editorial_decision_ref` | `mk:dec:` | the row in `03-REGISTERS/editorial-decisions.csv` carrying the publication decision, its rationale and the person who took it, rendered `publication:*` so it can never be read as an evidence status (§11.5). Museum framework §11.5 exists because *"nothing in `03-REGISTERS/` records a publication decision"*; an experience object that publishes without one reproduces the gap in a new layer. |
| `accessibility_equivalent` | reference | the non-visual equivalent carrying the same evidential content including status, attestation mode and uncertainty (§11.9.1–2). For a container, it is satisfied by its members' equivalents plus an equivalent for whatever the container itself adds — a Journey's through-line, a Mission's ordering. |
| `preconditions[]` | array | the consent, obligation, rights and community-authority records that must be **in force**, not merely requested (§8.7). Aggregated upward by containers. |
| `bias_test_context` | `mk:exh:` or Bias Test records | for an object inside an Exhibit, the Exhibit's tests (§3.11) satisfy this. **A Journey and a Learning Objective have no containing Exhibit and carry their own pair** — a Journey because its through-line is an assertion no single Exhibit makes, an objective because it can leave the institution on its own. |
| `revision`, `created`, `created_by`, `revised`, `revised_by` | metadata | museum framework §3.6 requires an actor on every revision record; these are where it comes from. |

Where §6 to §13 list one of these in their own field tables, the entry is
repeated for readability and this section governs.

### 5.6 The block does not soften anything else

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
| *(common fields)* | §5.5 | `release_state`, `editorial_decision_ref`, `accessibility_equivalent`, `preconditions[]`, `bias_test_context`, revision metadata — carried by all eight object types and not repeated in the seven tables below |

### 6.3 Grounding

A Question is grounded by **at least one** of:

1. a `bears-on` Grounding Link to evidence, a claim or a source;
2. an Absence record typed under §3.7;
3. a `mk:src:` Grounding Link to the source that is blocked, whose access-ledger
   row and `05-HOLDS/` record name what is needed. (The link is to the source,
   not to the hold file: a filesystem path is not an identifier and cannot
   satisfy §2.1.)

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

---

## 7. Exhibit — `mk:exh:`

### 7.1 What it is

**An Exhibit is the publishable unit a visitor lands on.** Museum framework §2.1
says exactly that and stops there. It is referenced throughout — `supports_exhibit`
on the Claim Object, `exhibit` as a search facet, the unit both adversarial tests
run on, the unit posture is assigned to, the unit the export bundles — and it has
no field list.

It is the successor to the workbook's *page*. That word is deliberately not used:
a page is a file with a slug, and the audited inventory shows what happens when
the publishable unit is defined by its file — 96 pages carrying 29 `Type` values,
17 of them singletons, 34 assigned to a residual environment, and a taxonomy
*"doing production-planning work it is too sparse to do reliably"* (`SCHEMA.md`
§3, `INHERITED-UNVERIFIED`). An Exhibit is defined by the claims it presents.

### 7.2 Fields

| Field | Type | Notes |
|---|---|---|
| `id` | identifier | `mk:exh:<key>` |
| `revision` | integer | append-only |
| `title` | string | **may not contain a count, a total or a superlative unless that number is itself a `presents` claim on this Exhibit** — §8.1's Atlas rule, generalised. The audited `"Artifact Atlas: 175 Ancient South Asian Sites Mapped"` is the case: a contested count (`IH-250`, X-01; D-034) in a title, rated `Low` risk — all `INHERITED-UNVERIFIED`. |
| `presents[]` | array of `mk:rel:` (`presents`) | the claims, relationships and absences shown in the institution's voice. **Non-empty. This is the Exhibit's grounding.** |
| `question_refs[]` | array of `mk:qst:` | the questions this Exhibit is an attempt on |
| `posture_assignment` | Posture Block | `derived_posture` · `assigned_posture` · `override_reason` · `derived_residual` · `decided_by` · `decided_date`, per §1.5. An override with an empty reason is invalid. Written to the Editorial Register (§11.5). |
| `modes_enabled[]` | enum(5) | Source · Atlas · Investigation · Field · Classroom, constrained by the §1.7 matrix for the assigned posture. Source Mode is mandatory and cannot be disabled. |
| `entry_routes[]` | enum(5) | object · place · word · text · question |
| `public_copy` | Step 14 Block | the seven required headings, §7.4 |
| `plain_language_summary` | string | required (§11.9.6), **carrying the same statuses as the full text** |
| `genre` | label | free vocabulary, navigation and search facets only. **No downstream authority**: it may not determine asset class, priority or posture (§1.6.3c). |
| `production_classes[]` | derived | from the evidence-class composition of what it presents (§1.6.3a), never from genre. An Exhibit with no recorded evidence classes yields none, which is the correct output. |
| `bias_tests[]` | array of Bias Test records | §3.11. **Both required before publication; running one is a failed test.** |
| `obligations[]` | array of `mk:obl:` | notably right-of-reply where a named living party is criticised (§11.3) |
| `right_of_reply_state` | enum | `not-triggered` · `notified` · `awaiting` · `replied` · `non-response-published` · `exchange-open` |
| `consent_refs[]` | array of `mk:cns:` | required where any `oral-living` evidence appears |
| `authority_refs[]` | array of `mk:agt:` + `mk:rel:` | where a community holds interpretive authority over material here (§11.2) |
| `characters[]` | array of `mk:chr:` | §13 |
| `activities[]` | array of `mk:act:` | §8 |
| `space_allocation` | Proportionality Block | §3.10, per claim presented |
| `editorial_decision_ref` | `mk:dec:` | the publication decision in the Editorial Register, rendered `publication:keep` / `publication:hold` etc. so it can never be read as an evidence status (§11.5) |
| `release_state` | enum | `draft` · `in-review` · `published` · `withdrawn` · `superseded` |
| `constraint_block` | Constraint Block | §5.2 |
| `export_profile` | reference | the §5.2 exhibit bundle this Exhibit produces |

### 7.3 Grounding

**An Exhibit with no `presents` link cannot exist.** Not "cannot publish" —
cannot be created. There is no draft state in which an Exhibit is a title and a
posture waiting for content, because that state is precisely how the audited
inventory acquired 32 pages typed `research-essay`, which `SCHEMA.md` §4 finds is
*"what a page is called when the audit did not classify it further"*
(`INHERITED-UNVERIFIED`).

Composition transitivity (§2.5) does **not** apply to an Exhibit. An Exhibit
grounds itself directly. It may not borrow grounding from the Activities it
contains or the Journey that traverses it, because it is the unit that speaks in
the institution's voice, and a unit that speaks must resolve on its own.

### 7.4 The public-copy shape is a field, not a template

Constitution Step 14 fixes the shape of public copy: **QUESTION / WHAT IS
OBSERVED / WHAT THE EVIDENCE SUPPORTS / WHAT COMPLICATES IT / WHAT REMAINS
UNKNOWN / MELAKEELA'S CURRENT INTERPRETATION / WHAT WOULD CHANGE IT.**

It is specified here as seven required fields on the Exhibit, each with a
constraint on what it may resolve to:

| Heading | Field | Must resolve to |
|---|---|---|
| QUESTION | `copy_question` | one or more `mk:qst:`, shown in `plain_form` |
| WHAT IS OBSERVED | `copy_observed` | evidence objects, described separately from interpretation (§2.4's iconographic rule generalised) |
| WHAT THE EVIDENCE SUPPORTS | `copy_supports` | claims at or above the **accepted threshold**, with statuses shown. Step 14: *"Draft public copy only from accepted claims."* §7.4.1. |
| WHAT COMPLICATES IT | `copy_complicates` | rival claims, contradicting relationships, dependency findings, contested readings |
| WHAT REMAINS UNKNOWN | `copy_unknown` | Absence records with their types, and `05-HOLDS/` rows. **Not prose about uncertainty** — typed absences, so a reader can tell `NOT EXCAVATED` from `ABSENT DESPITE ADEQUATE SEARCH` (§3.7). |
| MELAKEELA'S CURRENT INTERPRETATION | `copy_interpretation` | a claim set with statuses, attributed to the institution, and **disclosed after the evidence, never before** — the same ordering §9.3 requires of PROVE IT |
| WHAT WOULD CHANGE IT | `copy_falsifiers` | Falsifier records (§3.9). Non-empty, **or** the explicit value `none-required-at-this-status` where every claim presented is at `HYPOTHESIS` or below — §3.1 requires falsifiers only *"for any claim above `HYPOTHESIS`"*, and an Exhibit presenting only hypotheses has no source of them. The escape carries the claim ids it applies to, so an Exhibit cannot use it while presenting one claim above `HYPOTHESIS`. |

#### 7.4.1 The accepted threshold is the owner's, and this field does not set it

Constitution Step 14 says public copy is drafted *"only from accepted claims"*
and nowhere defines *accepted*. Whether `PROVISIONAL` — supported, but by a
single source or by dependent sources — counts as accepted for the register
headed WHAT THE EVIDENCE SUPPORTS is a publication threshold, and it is the
substance of `OWNER-DECISIONS.csv` **D-010**, *"which institutional claims can
presently be published"*, which is `OPEN`. Museum framework §0.3 lists D-010
among the decisions it does not settle, and this document does not settle it
either.

`copy_supports` is therefore specified against a **named threshold parameter**
rather than a fixed status list:

- `accepted_threshold` is a property of the institution, set once by the answer
  to D-010, and it is `VERIFIED` or `VERIFIED + PROVISIONAL`.
- `copy_supports` admits claims at or above it. Everything below it that bears on
  the exhibit appears under WHAT COMPLICATES IT or WHAT REMAINS UNKNOWN, which
  are not lesser registers — they are the two headings this record most often
  needs.
- **Statuses are shown either way**, so the threshold changes what is asserted in
  the institution's voice and never what a visitor can see.

Until D-010 is answered the field cannot validate, and an Exhibit cannot publish
under §14.3. That is the correct behaviour: an institution that has not decided
what it may assert should not be asserting.

Two rules on the shape:

- **No heading may be empty and none may be omitted.** An Exhibit with nothing
  under WHAT COMPLICATES IT has either found a genuinely uncomplicated corner of
  the record — which is possible and should be stated as such, with the
  adversarial tests that looked for complication — or has not looked. The field
  distinguishes them: `copy_complicates` accepts an explicit `none-found` value
  carrying the bias-test rows that searched.
- **The order is fixed.** The interpretation comes sixth. An Exhibit that leads
  with what MelaKeela thinks has inverted the shape, and the inversion is not a
  design variation.

### 7.5 Rules

- **Every claim-bearing sentence resolves** (§3.4). A sentence that cannot
  expose its `mk:clm:`, status, Evidence Links and route into Source Mode is
  published as editorial framing and marked as such. `editorial_framing` is a
  distinct span type in the copy fields, and the proportion of an Exhibit that
  is framing is countable and is a review finding when it grows.
- **Source Mode is reachable from every Exhibit in one interaction** (§1.7).
  Not a footer link.
- **Posture is assigned, not chosen for tone** (§1.3). The derived value is
  computed from the claim set and the absences; a divergence needs a reason;
  a residual assignment is flagged `derived_residual` so the unclassified set
  stays countable (§1.6.1).
- **Field Mode is forbidden where §1.7 forbids it.** An Exhibit in the
  Extraction / Collection or Reconnection posture may hold no Activity whose
  mode is Field. If a posture reassignment moves an Exhibit into one of those
  postures, its Field Activities are suspended by that reassignment, not left to
  be noticed.
- **Proportionality is per claim presented** (§3.10), advisory, and compared at
  review. Layout does not settle which explanation is stronger.
- **An Exhibit is not a Journey stop that happens to have content.** It stands
  alone: a visitor arriving from a search result, an external citation or a
  Journey sees the same object with the same statuses. Journeys add route, not
  content (§11.4).
- **Decay.** When a presented claim is superseded, the Exhibit revises and shows
  the succession (§3.6 pins both directions). When a presented claim is rejected,
  the Exhibit does not silently drop it: `REJECTED` rows persist and stay visible,
  and an Exhibit that argued from one now shows that it did. When consented
  material is withdrawn, the material goes and the record that it was here and
  was withdrawn remains (§11.4) — `decay_behaviour = retract` for the material,
  `disclose` for the fact.

### 7.6 What an Exhibit is not permitted to do

1. **Assert in its own voice anything not in `presents[]`.**
2. **Carry a count, total or superlative in its title** that is not itself a
   statused claim on the Exhibit (§7.2).
3. **Open with an interpretation** where its entry route is the object route
   (§6.2's page order: material description, present holder and terms, asserted
   provenance with its type, custody chain with gaps, dates by type, the §4V
   provenance questions with the unanswered ones displayed as unanswered, and
   only then the claims).
4. **Present a bridge as a property of its subject** (§6.7): an object does not
   have a language, a place does not have an ethnicity, a word does not have a
   people, a text does not have a race.
5. **Publish without both adversarial tests** (§3.11).
6. **Publish media at `rights_status = unknown`** (§11.8.2). The rights
   placeholder states what exists, where, and why it is not shown.
7. **Vary its historical content by interface language** (§11.10.2). Two
   visitors in two languages see the same claims with the same statuses.

---

## 8. Activity — `mk:act:`

### 8.1 What it is

**An Activity is the smallest unit of visitor doing.** One interaction pattern,
one prompt, one thing recorded. It is the atom the rest of the layer is built
from: a Mission is an ordered set of Activities, a Challenge is an Activity
sequence with a claim at risk, the children's five stages are five Activities,
and PROVE IT's six stages are six.

It is the object where the §10.4.7 prohibitions actually bite, because they are
prohibitions on interaction patterns and the Activity is the only object that has
one.

**An Activity resolves to the claims it exercises.** That is the task's phrasing
and it is exact: an Activity is not *about* a topic, it is reasoning *over* a
specific set of claims, relationships or absences, and if that set is empty there
is nothing for the visitor to do except accept what they are told.

### 8.2 The interaction pattern vocabulary

Controlled, closed, and extended only by revision of this document — because an
open vocabulary would let a forbidden pattern re-enter under a new name.

**The children's five** (museum framework §10.4.3): `LOOK` · `ASK` ·
`FIND-OUT` · `DECIDE` · `CHECK`.

**The vertical slice's additions** (`06-BACKLOG/EXPANSION-PROMPT-2026-09-07.md`
L247, `INHERITED-UNVERIFIED`): `DIG-IT` · `WHAT-DID-YOU-FIND` · `COMPARE` ·
`WHAT-DO-YOU-THINK`. (`PROVE IT` and `FIELD BAG` are not Activities: the first is
a Challenge, §9; the second is the Field Bag, §10.3 of the framework.)

**The research patterns**, available at every age band: `READ` (a primary source
at its locator in the viewer) · `TRACE` (a custody or transmission chain, gaps
included) · `WEIGH` (rival explanations against their evidence) · `LOCATE` ·
`DATE` (which date type, on what basis) · `SEARCH` (a reproducible corpus query
with its method) · `MAP` (a filtered Atlas view with its exclusion set) ·
`TYPE-THE-ABSENCE` (apply the §3.7 typing to a silence) · `FOLLOW-THE-SOURCE`
(walk an independence tree to its root) · `RE-READ` (set a variant reading beside
the one the institution cites).

Every pattern carries a fixed answer posture:

| Pattern class | Has a right answer? |
|---|---|
| `LOOK`, `ASK`, `WHAT-DID-YOU-FIND`, `DECIDE`, `WHAT-DO-YOU-THINK`, `WEIGH`, `TYPE-THE-ABSENCE` | **No.** These record what the visitor observed, asked or concluded. |
| `READ`, `TRACE`, `LOCATE`, `DATE`, `SEARCH`, `MAP`, `FOLLOW-THE-SOURCE`, `RE-READ`, `FIND-OUT`, `CHECK` | **Only where the answer is a `VERIFIED` claim or a mechanical property of the record** (a locator, an edition, a chain step, a count with its corpus and method). Never where it is `PROVISIONAL` or below. |
| `COMPARE` | **No**, and its terms are constrained — §8.4. |
| `DIG-IT` | **No.** See §8.5. |

`has_right_answer = true` on a claim below `VERIFIED` is refused at creation.
This is the derivation rule of §3.2 applied to pedagogy: **an Activity may not
require a visitor to be right about something the institution has not verified.**

### 8.3 Fields

| Field | Type | Notes |
|---|---|---|
| `id` | identifier | `mk:act:<key>` |
| `revision` | integer | append-only |
| `interaction_pattern` | enum | §8.2. Exactly one. An Activity that does two things is two Activities. |
| `prompt` | string | the exact words asked of the visitor. Not a summary of them. |
| `prompt_plain` | string | the same prompt at the lowest reading age the Activity's `age_bands[]` includes |
| `exercises[]` | array of `mk:rel:` (`exercises`) | the claims, relationships and absences the reasoning is over. **Non-empty. This is the Activity's grounding.** |
| `objects_used[]` | array of `mk:evd:`, `mk:plc:`, `mk:lex:`, `mk:txt:` | what is put in front of the visitor, each with `is_primary` and `attestation_mode` rendered (§2.5, §2.6) |
| `has_right_answer` | bool | constrained by §8.2 |
| `has_right_answer_kind` | enum or null | `verified-claim` · `record-property`. **Required when `has_right_answer` is true.** §8.2 permits a right answer on a mechanical property of the record — a locator, an edition, a chain step, a count with its corpus and method — and such a property is not a `mk:clm:`; without the discriminator the model could not express the right answer for `READ`, `LOCATE`, `DATE`, `TRACE` or `FOLLOW-THE-SOURCE`, which is most of the research set. |
| `right_answer_ref` | `mk:clm:`, or a `mk:<type>:<key>#<anchor>` sub-locator, or null | **required when `has_right_answer` is true.** Where `has_right_answer_kind = verified-claim` it is a `mk:clm:` and its status must be `VERIFIED`. Where it is `record-property` it is the addressed anchor itself — the locator, the edition row, the chain step — and correctness is resolution, not status. |
| `recorded_output` | enum | `observation` · `question` · `decision` · `note` · `selection` · `nothing`. What goes to the Field Bag. |
| `output_is_private` | bool | **true for every free-text output at every age band.** §10.4.5: a child's written text is never published, never transmitted by default, never enters the correction pipeline as a public artefact. Specified at every band because §5.4's no-gate argument holds for adults' notes too and because a private note is the only kind a visitor can write honestly. |
| `compare_terms[]`, `compare_term_class[]` | Constraint Block | §5.2, §8.4 |
| `mode` | enum(5) | which of the five modes this Activity runs in, constrained by the containing Exhibit's posture through §1.7 |
| `posture_context` | enum(7) | derived from the containing Exhibit |
| `age_bands[]` | array | declarative, §5.4 |
| `preconditions[]` | array | consent, rights and community-authority records that must be in force before this Activity can run (§8.7) |
| `accessibility_equivalent` | reference | **required.** The non-visual, non-motor equivalent that carries the same evidential content including status, attestation mode and uncertainty (§11.9.1–2). An Activity without one is not built. |
| `duration_estimate` | interval | advisory, never enforced — §10.4.4 forbids time pressure |
| `objective_refs[]` | array of `mk:lob:` | via `prepares-for` |
| `constraint_block` | Constraint Block | §5.2 |

### 8.4 COMPARE

COMPARE is the pattern museum framework §10.4.7 singles out, and this is where
its rule is implemented rather than restated.

**The rule.** *"COMPARE may not take people, remains, named individuals or
populations as its terms anywhere in the children's mode, in any Living World, in
any pilot."* Under §5.4 this model binds it at every age band within the
experience layer.

**How it is implemented.** Not as a check that runs on a finished Activity. As a
shape the Activity cannot be given:

1. `compare_terms[]` is required and non-empty when `interaction_pattern =
   COMPARE`, and each term is an identifier, never a label.
2. `compare_term_class[]` runs parallel to it and draws on the enumeration in
   §5.2, which has fourteen values and **no value for a person, a group of
   people, human remains, a personal name, a population, an ancestry component,
   an archaeological culture used as a stand-in for a people, or a language used
   as a proxy for one.** A designer who wants a child — or an adult — to compare
   two skulls, two portraits, two names or two ancestry profiles finds there is
   no way to write it down.
3. The validator checks the **resolved referent**, not the declared class
   (§5.3), and refuses an identifier resolving to an `mk:agt:` of kind person or
   community, to a UEO in the human-remains subclass set, or to an ANCESTRY-layer
   object (framework §8.4, layer 8 — the Atlas layer, not §8.4 of this
   document), whatever class was declared for it.
4. A COMPARE Activity has `has_right_answer = false` unconditionally. Comparison
   produces observations, not verdicts.

**What the mechanism does not reach, stated plainly.** Three residues, because
a mechanism oversold is worse than one honestly bounded:

- **The human-remains subclass set does not yet exist.** Framework §2.3 gives
  `evidence_subclass` as *"controlled"* with examples and no enumeration. Until
  that set is published (framework §5.3 requirement 3), item 3's second test
  cannot run and the check falls back on `mk:agt:` kind and layer membership.
  Publishing it is a prerequisite of this rule, not an implementation detail.
- **"An archaeological culture used as a stand-in for a population" is a
  judgement, not a resolution.** It cannot be validated, for the same reason
  §8.4 gives below for refusing the framing exemption: intent is not a field. It
  is a review finding, listed here so it is reviewed rather than assumed
  automated. The same holds for a language used as a proxy for a people.
- **`claim` is a permitted class, and a claim can be about a population.** Two
  claims about populations resolve to `mk:clm:` and pass every mechanical test.
  This is the sort at one remove, it is real, and it is caught — if at all — by
  the Constraint Block reviewer named at §5.2, not by the validator. A COMPARE
  Activity whose terms are claims about populations is the case that most needs a
  human to look, and the review signature exists for cases like it.

**Why the framing exemption is refused.** §10.4.7: *"Framing the exercise as a
debunking of racial classification does not lift the prohibition; the child still
performs the sort."* This model adds the mechanical reason. The Activity object
records `interaction_pattern`, `compare_terms[]` and `compare_term_class[]`. It
does not record intent, and it could not: intent is not a field, it is not
exportable, it is not checkable at publication, and it is not what the visitor
experiences. Two Activities with identical patterns and identical terms are the
same interaction whatever the surrounding copy says about why. The framework says
this in prose; the object model makes it the case that no other implementation is
expressible.

**What COMPARE is for.** On pots, scripts, seeds, beads, strata, reading
variants, date assertions, source trees and typed absences, it is *"the reasoning
the mode exists to teach"* (§10.4.7). Nothing in this section narrows that. The
fourteen permitted classes are the working range of comparative reasoning in this
record, and they are more than the flow ever needed.

### 8.5 DIG-IT, and the buckets problem

Museum framework §10.4.7 finds that the specified vertical slice supplies its own
categories: *"DIG IT produces the items, COMPARE produces the categories, and
PROVE IT then asks the child to defend the result."* The sequence is what makes
the sort feel discovered rather than handed over.

Three constraints on `DIG-IT` follow, and they are constraints on the Activity,
not on the flow, so that reordering the flow cannot evade them:

1. **DIG-IT yields only real objects.** §10.4.4: *"No fabricated evidence, ever.
   No invented objects, no composite 'typical' artefacts."* Every item a DIG-IT
   Activity produces is a `mk:evd:` that exists, with a findspot, a holder and a
   custody chain, or it is a labelled derivative of one.
2. **DIG-IT never yields a person, a set of remains or a named individual as an
   item.** Not because remains cannot be discussed — §10.4.4 permits their
   display where community authority and consent allow, *"at the least
   sensational presentation possible, and never as a puzzle to be solved"* — but
   because an item produced by DIG-IT becomes a term available to the next
   Activity, and the next Activity is COMPARE. The prohibition has to sit at the
   producing step or it arrives too late.
3. **The categories a subsequent COMPARE offers are declared on the COMPARE
   Activity**, in `compare_term_class[]`, before the DIG-IT Activity runs. A
   sequence cannot generate its own permitted classes at runtime.

### 8.6 Rules

- **No score, no points, no streak, no badge, no timer, no "correct"**
  (§9.3, §10.4.4). `reward_mechanic = none` in the Constraint Block, at every
  age band on classification material and throughout the children's mode.
- **Disagreement with the institution is a first-class output** (§9.3), on
  `DECIDE`, `WEIGH` and `WHAT-DO-YOU-THINK`. Where it is recorded it routes to
  the Challenge object's correction intake (§9.6), and only ever with the
  visitor's explicit act — never automatically, and never for a child's free text
  (§10.4.5).
- **"I don't know" is always available and is never scored as a failure**
  (§10.4.3, stage 4). It is a value of `recorded_output`, not the absence of one.
- **Status travels into the output.** A claim a visitor puts in their Field Bag
  from an Activity carries the status it had, and the bag shows what changed
  since (§10.3).
- **Every Activity states what it is showing and at what remove.** The
  `is_primary` gradient is rendered on `objects_used[]`: a visitor looking at a
  photograph of a plate in an edition of a text is three steps from the text and
  the Activity says so (§2.5).
- **An Activity may not be the place a translation choice is made silently.**
  Where a term does work, the alternatives and the interpretive consequence are
  one interaction away on the same surface (§3.8).
- **Reconstructions carry their marker in the visitor's own words** (§10.4.4),
  with what the reconstruction was based on shown.

### 8.7 Preconditions, and why they are a field

Museum framework §10.4.2 makes the point about the children's pilot: *"the site
pilot has a consent precondition and the inscription pilot has a rights
precondition, and neither can be scheduled as though it were only a content
task."*

`preconditions[]` generalises that to every Activity. It holds the `mk:cns:`,
`mk:obl:` and community-authority records that must be **in force**, not merely
requested, before the Activity can run. Two behaviours:

- **A precondition that lapses suspends the Activity.** §11.4: a consent with a
  review date passes to `lapsed` on that date and the material comes down until
  it is renewed. The Activity goes with it, automatically, and the suspension is
  a revision record with `change_type = grounding-lost` (§3.3).
- **A precondition that was never obtained blocks creation.** An Activity built
  on `oral-living` evidence with no `consent_ref` is invalid at the evidence
  layer already (§2.3 requires it non-null); this field makes the same failure
  visible at the surface that would have shown it.

### 8.8 What an Activity may never be

1. **A sort of human beings into types** — as a game, a match, a drag, a quiz,
   or a "which group does this person, name, skull or word belong to" task, with
   the categories renamed, softened, or presented as historical labels the
   visitor applies (§10.4.7, first constraint).
2. **A reward mechanic attached to a racial, racial-nationalist or other
   extremist classification** — and it makes no difference that the
   classification is being taught as false, because *"a scoring interface teaches
   that the categories are operable before it teaches anything about them"*
   (§10.4.7, second constraint).
3. **A staging of persecution** — dramatized, role-played, simulated, scored or
   reconstructed as an experience the visitor moves through (§10.4.7, third
   constraint). Persecution is read as record, with its evidence and its status.
4. **A verdict on a live custody, restitution or legal matter assigned to a
   child** (§10.4.6). A child may read the custody record; "work out whether this
   was looted" is not an Activity.
5. **A task over fabricated evidence** — invented objects, composite artefacts,
   unlabelled reconstructions (§10.4.4).
6. **An identification of an object, a person or a set of remains as ethnic or
   national** (§10.4.4), which is a §4.4 bridge in every case.
7. **An exercise that requires the visitor to be right about a claim below
   `VERIFIED`** (§8.2).
8. **An activity with no accessibility equivalent** (§11.9.1).

---

## 9. Challenge — `mk:chl:`

### 9.1 What it is

**A Challenge is a bounded, designed invitation to test one institutional claim
against the institution's own evidence, with disagreement as a permitted
outcome.** It is the unit PROVE IT is made of.

Museum framework §9.1 states what PROVE IT must be able to do: *"If PROVE IT
cannot produce the outcome 'the institution is wrong here', it is a quiz, and a
quiz that only confirms is publicity."* §9.2 gives it six stages and §9.3 six
rules. Neither gives it an object, so a PROVE IT run is currently unaddressable,
uncitable and unexportable, in a mode whose §9.3 rules require that *"every run
is exportable … A run is citable."*

The Challenge is that object. It is the unit; a **run** is one visitor's pass
through it, and the two are distinguished in §9.5 because they have different
lifetimes and different privacy positions.

Whether PROVE IT is the correction intake this reading takes it to be is museum
framework **D-024** and is not settled here. The specification below is written
so that a negative answer removes §9.6 and leaves the rest standing.

### 9.2 The three things called "challenge", kept apart

Declared at §3.2 and restated here because this is the object where confusion
would do damage:

| Written | Identifier | What it is |
|---|---|---|
| `challenge:experience` | `mk:chl:` | this object — a designed invitation to test a claim |
| `challenge:correction` | `mk:cor:` | a submitted assertion that a claim at a revision is wrong (§11.6) |
| challenge candidate | — | §9.4's transient: a recorded disagreement in a run, before it is submitted |

A bare "challenge" in a column heading, a filter, a facet or a page title is a
defect, exactly as an undifferentiated "hold" is (§11.5).

### 9.3 Fields

| Field | Type | Notes |
|---|---|---|
| `id` | identifier | `mk:chl:<key>` |
| `revision` | integer | append-only |
| `targets` | `mk:rel:` (`targets`) | **exactly one**, to a `mk:clm:@r<n>`, a `mk:qst:` or a `mk:rel:`. Revision-pinned: a Challenge is against a claim as it stood, and a visitor who returns is shown what has changed since. §9.4. |
| `challenge_form` | enum | `test-a-claim` · `weigh-rivals` · `find-the-dependency` · `type-the-absence` · `check-the-locator` · `read-the-variant` · `apply-a-gate` |
| `activities[]` | ordered array of `mk:act:` | the run's stages as Activity objects (§8), so the interaction constraints apply here without restatement |
| `evidence_set[]` | array of `mk:rel:` | the Evidence Links put before the visitor, with roles, locators, editions, retrieval dates and independence groups (§3.3). **Non-empty. This is the Challenge's grounding** — §9.4. |
| `independence_tree_shown` | bool | **true.** §9.2 stage 3: *"nine citations resolving to one 1953 report is the single most instructive thing this mode can teach."* |
| `rivals[]` | array of `mk:clm:` | every viable explanation **plus the null explanation**, independently stated (§9.2 stage 2) |
| `exclusion_notes[]` | array of Gate Results | gated-out explanations with the gate they failed, in the fixed small footprint of §3.10 |
| `gates_offered[]` | enum | chronological · geographical · mechanism · positive-evidence · diagnostic. Each shown with the data needed to apply it. |
| `absences[]` | array of `mk:abs:` | §9.2 stage 5, with types |
| `falsifiers[]` | array of Falsifier records | §9.2 stage 6, with `currently_testable` and `blocked_by` |
| `hold_disclosure` | Block or null | **required and non-null where the target or any evidence is `HOLD`** (§9.3) |
| `institution_position` | `mk:clm:` set | disclosed **after** the visitor has worked the evidence, never before (§9.3) |
| `outcome_forms[]` | enum | `agree` · `disagree` · `undecided` · `insufficient-evidence` · `question-is-malformed`. All five are first-class; none is a failure state. |
| `bias_tests_shown[]` | array of Bias Test records | **both**, with the asymmetry statement (§11.2) |
| `disagreement_route` | enum | `none` · `correction-intake` — §9.6, subject to D-024 |
| `age_bands[]` | array | declarative, §5.4 |
| `preconditions[]` | array | as §8.7 |
| `constraint_block` | Constraint Block | §5.2 |

### 9.4 Grounding, and why it is not the target

**A Challenge grounds on `evidence_set[]`, which is non-empty, not on
`targets`.**

That looks like the wrong choice and is the right one. `targets` may point at a
`mk:qst:`, which is an experience object — and §2.1 is categorical that an
experience object never grounds another. A Challenge on an open Question with no
evidence set would then be a Challenge about nothing, which is exactly the object
the grounding rule exists to refuse: an invitation to weigh evidence, with no
evidence in it.

Grounding on the evidence set also states the substantive rule. A Challenge is
not made legitimate by naming a claim; it is made legitimate by putting the
evidence in front of the visitor. **A Challenge with a target and no evidence set
is a poll.**

`targets` remains required, **exactly one**, and revision-pinned. That is a
separate structural rule and the single-target part of it is not a
simplification. A Challenge with two targets
lets a visitor's disagreement land ambiguously, which makes the correction it
emits unusable: §11.6 requires a challenge to be *"against a specific claim at a
specific revision, with the evidence the challenger relies on."* An investigation
that needs to put three claims at risk is three Challenges, and a Mission is the
object that holds them in sequence (§10).

### 9.5 Challenge and run

A **Challenge** is published, addressable and citable: `mk:chl:<key>@r<n>`.

A **run** is one visitor's pass through it. Runs are:

- **Local by default**, in the Field Bag, on the visitor's own device, with no
  account (§10.3, §10.4.5). Whether a server-side option exists at all is
  **D-052**; under either answer the default is local and the option is never
  the default.
- **Exportable by the visitor** as the claim, the evidence set, the gates and
  their own reasoning (§9.3). The export is the citable artefact.
- **Never transmitted by default.** A run reaches the institution only by the
  visitor's explicit act (§9.6), and never for a child's free text: §10.4.5
  requires that a class submission comes from the teacher's account, as the
  class's.
- **Not aggregated into behavioural analytics.** §10.4.5 permits aggregate,
  non-identifying usage counts with a published measurement policy, and nothing
  else, at any age.

### 9.6 The route from disagreement to correction

Subject to **D-024**. Under the reading museum framework §9.4 takes, a recorded
disagreement is not a comment: it enters the correction pipeline as a challenge
candidate carrying the claim, the revision, the evidence relied on, the gate or
absence read differently, and what the visitor says would settle it.

As an object flow:

1. The visitor's `disagree` outcome, plus their `WEIGH` or `DECIDE` outputs,
   forms a **challenge candidate** — transient, local, and not yet anything.
2. The visitor submits it. Explicitly. A candidate that is not submitted is
   deleted with the run.
3. Submission creates a `mk:cor:` row (§11.6) with `channel = PROVE IT run`,
   the target claim and revision, the evidence offered, and the challenger's
   disclosed affiliation if they offered one.
4. If upheld, the correction produces a revision of the claim (§3.6) whose
   `triggering_record` is the correction id, so the visitor's challenge is
   permanently part of the claim's history.
5. Triage is public in aggregate: received, assessed, upheld, declined, median
   time to assessment — *"published, and updated whether or not the numbers are
   flattering"* (§11.6, rule 4).

**The asymmetry that makes this worth building.** §11.6 rule 5 requires that
challenges against the institution's preferred position be tracked separately and
reported, because *"the failure this whole method guards against is the
institution being easier on itself."* The Challenge object carries
`target_is_preferred_position` (bool, editorially set, logged) so that the split
can actually be computed rather than asserted.

### 9.7 Rules

- **No score, no points, no streak, no "correct"** (§9.3). A Challenge has no
  right answer to withhold, *"because several of the propositions in this
  institution do not have one yet."*
- **The institution's position is disclosed last.** Not withheld — disclosed,
  with its status and its confidence inputs, after the visitor has worked the
  evidence. A Challenge that leads with what MelaKeela thinks has become a
  comprehension exercise.
- **Both adversarial tests are shown, with the asymmetry statement**, and the
  preferred-counter-narrative test is shown on Challenges that contradict a
  dominant account. §9.3: PROVE IT *"is worthless if it applies only the first."*
- **A Challenge never runs on a `HOLD` without showing the hold** (§9.3). A
  visitor must not be asked to weigh evidence the institution has told them it
  could not reach.
- **Rivals are always reachable at one interaction, and are weighted by
  evidence.** This needs care, because two framework rules pull against each
  other and this document may not settle their tension by quoting one of them.
  §4.5 requires that selecting a bridge shows *"its rivals at the same visual
  weight as itself"* — a rule about a bridge and its alternatives. §12.3, V-8
  states the general rule the other way: *"Equal visual weight is a claim, and is
  only made where the evidence is equal. Two rival explanations rendered
  identically when their evidence differs fails §3.10."* `CLAUDE.md` is with V-8:
  *"No false equivalence. A contested claim and an established one do not get
  parallel presentation."*

  **V-8 governs here**, because a Challenge's `rivals[]` is a set of explanations
  with unequal evidence, not a bridge and its alternatives. What is equal is
  **reachability**: every rival, including the null explanation, is one
  interaction away, listed, and never behind a fold. What follows evidence is
  **weight** — extent, prominence and finish. A Challenge that renders a
  `HYPOTHESIS` rival with the finish of a `VERIFIED` one has made a claim it did
  not state, in the direction the preferred-counter-narrative test exists to
  catch.

  The tension between §4.5 and V-8 is the framework's, not this document's, and
  it is logged as `IC-X-001` in `04-AUDITS/INTERNAL-CONTRADICTIONS.csv` rather
  than resolved here.
- **`unknown` is never a rival** (§3.7). `insufficient-evidence` is an outcome
  the visitor may reach; it is not an explanation on the list.
- **The Challenge may not be a Character's argument.** No Character advocates a
  position in a Challenge, and none opposes the visitor. §13.6.
- **Decay.** When the target claim revises, the Challenge does not silently
  re-point: the pin holds, the visitor is shown that a newer revision exists and
  how it differs (§2.1), and the Challenge is queued for editorial re-issue
  against the new revision. When the target is rejected, the Challenge stays
  resolvable and shows that the institution came to agree with the visitors who
  disagreed — which is the outcome the mode exists to make possible and the last
  one to hide.

### 9.8 What a Challenge may never be

1. **A quiz with a withheld answer.** The distinction is the disclosure order
   and the absence of a score, and both are fields.
2. **A defence of the institution.** A Challenge whose evidence set omits the
   evidence that bears against the claim has been curated into an argument — the
   same failure §8.6 names for an Atlas *"in which every artifact turns out to be
   linguistically meaningful."*
3. **A vote.** Aggregating visitor outcomes into a displayed tally would make
   agreement a measurement and disagreement a minority position. Corrections are
   assessed on evidence, not on counts (§11.6, rule 1).
4. **An exercise on a live custody or restitution matter put to a child**
   (§10.4.6). Field Mode is forbidden in the Extraction / Collection and
   Reconnection postures (§1.7), so a child's Challenge cannot run in either.
   Investigation Mode is *mandatory* in Extraction / Collection and *available*
   in Reconnection, so an adult Challenge is expected in the first and permitted
   in the second.
5. **A sort, a scored classification or a staged persecution** (§5.2), by way of
   any Activity it contains.
6. **A surface where a claim the institution has not made gets said** — by a
   prompt, a hint, a framing sentence or a Character. Everything a Challenge
   asserts resolves to `targets`, `rivals[]`, `evidence_set[]` or
   `institution_position`.

---

## 10. Mission — `mk:msn:`

### 10.1 What it is, and how it differs from a Journey

**A Mission is an ordered sequence of Activities directed at exactly one
Question, whose outcome is a record rather than a reward.**

Mission and Journey are the two container objects and the distinction between
them is not size:

| | Mission | Journey |
|---|---|---|
| Organised around | one Question | a through-line across Exhibits |
| Holds | Activities, and Challenges | Exhibits, and Missions |
| Shape | a task with a stated end | a traversal with a stated extent |
| Ends when | the visitor has recorded a decision, or leaves | the visitor has been everywhere, or leaves |
| Asserts | nothing beyond its Activities | its through-line claim set, and its order where the order implies a sequence |

A Mission is the object behind the children's five-stage investigation
(museum framework §10.4.3) and behind any adult equivalent. It is deliberately
small: **one question, one sitting, one thing carried away.**

### 10.2 Fields

| Field | Type | Notes |
|---|---|---|
| `id` | identifier | `mk:msn:<key>` |
| `revision` | integer | append-only |
| `question_ref` | `mk:qst:` | **exactly one, required.** A structural field, not a Grounding Link — a Question is an experience object and cannot ground one (§2.1, §10.3). A Mission with two questions is two Missions. |
| `assembles[]` | ordered array of `mk:rel:` (`assembles`) | Activities and Challenges, in order. **Non-empty.** |
| `order_is_claimed` | bool | see §10.4 |
| `exhibit_context` | `mk:exh:` | the Exhibit the Mission runs within, from which posture and mode constraints derive |
| `outcome_form` | enum | `field-bag-record` · `exported-run` · `none`. **Never a score, a badge, a completion percentage or a streak.** |
| `abandon_state` | enum | `resumable` · `discarded`. A Mission may be left at any point; leaving is not failure and produces no prompt to return. |
| `progress_storage` | enum | `local` · `none` under the position §10.5 argues for; `opt-in-server-side` if the owner answers **D-052** the other way. §10.5. |
| `age_bands[]` | array | declarative, §5.4 |
| `objective_refs[]` | array of `mk:lob:` | via `prepares-for` |
| `preconditions[]` | array | §8.7, aggregated from its Activities and its own |
| `duration_estimate` | interval | advisory; §10.4.4 forbids time pressure and the estimate may not be displayed as a countdown |
| `accessibility_equivalent` | reference | required; the whole sequence must be completable by the equivalents its Activities carry |
| `constraint_block` | Constraint Block | §5.2 |

### 10.3 Grounding

**The Mission is the one object that grounds through composition** (§2.5), and it
is the only one. Its Activities and Challenges are grounded, so it is.

`question_ref` does not ground it. A Question is an experience object, and §2.1
forbids an experience object from grounding another — a Mission whose only link
were to a Question would resolve to nothing in the evidence layer, however
carefully the Question was written. `question_ref` is a required structural
field, and the requirement is about scope: a Mission with no question is a
sequence of exercises with no reason to be in that order.

The consequence is that **a Mission whose Activities are all removed or suspended
becomes ungrounded at that moment and is unpublishable from that moment.** It
does not retain grounding through Activities it no longer has. This is the case
§2.5 exists for and it is not hypothetical: an Activity suspends automatically
when a consent lapses (§8.7), so a Mission can lose its grounding with nobody
editing it.

### 10.4 Order is sometimes a claim

The children's five stages are ordered for a reason — observation before
interpretation, evidence before decision, the institution's position last — and
that order is a pedagogical position, not an assertion about the past.

But an order can assert. A Mission whose steps run *"first this settlement, then
this one, then this one"* has made a chronological claim in its navigation, and a
Mission that ends where the institution's preferred explanation is has made an
argument by sequence.

Museum framework §8.3 has already met this and ruled on it for the Atlas's seven
settings: *"It is not a route. The settings are places the visitor can move
through in any order, and the interface must not present them as an itinerary
with an arrow, because the itinerary is itself the contested claim."*

The rule here is that finding generalised:

> **`order_is_claimed = true` requires that the sequence be carried as a statused
> claim in `exercises` on the Mission, with its own evidence and falsifiers.
> Otherwise the order must be pedagogical only, and the Mission must state that
> its order is a way of working and not a sequence in the world.**

A pedagogical order is still fixed — LOOK before DECIDE is not negotiable — but
it is fixed for a reason the visitor is told.

### 10.5 Progress, and the framework rule this narrows

Museum framework §10.3 permits a server-side Field Bag: *"Local by default. The
bag is stored on the visitor's own device and needs no account. Any server-side
bag is opt-in, and for under-16 visitors it does not exist at all."*

**Under §5.4's derivation that argument does not survive contact with the
architecture**, and the document says so rather than legislating around it. If
the institution offers no accounts and cannot know a visitor's age, then a
server-side store that "does not exist for under-16 visitors" is a store whose
exclusion cannot be applied. An opt-in that a child can take is not an opt-in
with an age condition on it; it is an opt-in.

Two coherent positions follow and the choice between them is the owner's,
because it decides whether the institution holds visitor data at all:

| Position | Consequence |
|---|---|
| **No server-side progress state**, `progress_storage` ∈ `local` · `none` | The institution holds no per-visitor record and the under-16 rule is satisfied by construction. Cost: a visitor who changes device loses their place, and the Field Bag §10.3 offers as opt-in is not offered here. |
| **Keep §10.3's opt-in**, adding `opt-in-server-side` | The framework's rule stands unamended and adults who want continuity get it. Cost: the institution holds behavioural records it cannot show contain no child's data. |

**This document does not decide it.** It specifies both values, writes every
other rule so that either works, and escalates the choice as **D-052**. The
narrower position is the one §10.2's field list is written against as a default,
and the recommendation is labelled as such: it is a recommendation, not an
adoption.

Classroom sets are unaffected either way. They are the teacher's, saved to the
teacher's optional account, holding no student data and no assessment scoring
(§10.5.2).

Classroom sets are the one place a stored, shareable container exists, and they
are the teacher's, saved to the teacher's optional account, holding no student
data and no assessment scoring (§10.5.2).

### 10.6 Rules

- **No completion mechanic.** No badge, no percentage, no streak, no
  congratulation, no "you have finished". A Mission ends when the visitor has
  recorded what they think, and the record is the outcome (§9.3, §10.4.4).
- **"I don't know" completes a Mission.** §10.4.3 stage 4: *"'we don't know' is
  offered and is never scored as a failure."* A Mission whose only recordable
  outcomes are conclusions is a Mission that has scored the visitor.
- **The institution's position comes last** (§10.4.3 stage 5, §9.3), and a
  difference between the visitor's reasoning and the institution's is *"presented
  as interesting, not wrong."*
- **A Mission may not be built on `HOLD` material without disclosing the hold**
  (§9.3), and may not be built on `INHERITED-UNVERIFIED` material at all where
  it asks the visitor to conclude — the derived-asset rule of §3.12 applied to
  experience: *"a derived asset may not be commissioned or published while the
  claim it depicts is `INHERITED-UNVERIFIED` or `HOLD`."*
- **Field-mode Missions do not exist in the Extraction / Collection or
  Reconnection postures** (§1.7). The restriction is on Field Mode, not on
  seriousness: Investigation Mode is mandatory in Extraction / Collection and
  available in Reconnection, so adult work runs in both. The matrix mandates a
  *mode*, never an object instance — an Exhibit satisfies it by making the mode
  available, not by containing a Mission.
- **The Constraint Block binds the Mission independently of its Activities.** A
  sequence of individually permissible Activities can compose a forbidden one —
  §8.5's buckets problem is exactly that — so the Mission declares its own
  `compare_terms[]` aggregate and its own `sorting_of_persons = none`, and the
  publication gate checks the sequence as well as the steps.

---

## 11. Journey — `mk:jny:`

### 11.1 What it is

**A Journey is a traversal of Exhibits along a stated through-line, whose
through-line is itself a claim set.**

Museum framework §10.1 specifies the Living World as *"a themed traversal of the
whole evidence base along a single material or ecological thread, crossing every
posture rather than sitting in one"*, with five pattern requirements. The Journey
is the general object; **a Living World is a Journey with `living_world = true`
and §10.1's requirements enforced.** WATER (§10.2) would be an instance, and
whether it is the first is `OWNER-DECISIONS.csv` D-005 and is not decided here.

Making Living World a subtype rather than a parallel object matters: it means
the institution cannot build a "tour" or a "trail" or a "collection" that escapes
§10.1's requirements by not being called a Living World.

### 11.2 Fields

| Field | Type | Notes |
|---|---|---|
| `id` | identifier | `mk:jny:<key>` |
| `revision` | integer | append-only |
| `through_line` | string | what the thread is |
| `through_line_claims[]` | array of `mk:rel:` (`exercises`) | **the claim set the thread asserts, listed and statused at the entrance** (§10.1). Non-empty. This is what makes a Journey an assertion rather than a menu. |
| `traverses[]` | array of `mk:rel:` (`traverses`) | the Exhibits, with `traversal_order`. **Non-empty; minimum two** — a Journey through one Exhibit is an Exhibit. |
| `traversal_order` | enum | `free` · `suggested` · `fixed`. Constrained by §11.4. |
| `order_is_claimed` | bool | as §10.4; a `fixed` order implying chronology or causation requires a statused claim |
| `postures_crossed[]` | derived, enum(7) | from the assigned postures of its Exhibits |
| `living_world` | bool | when true, §11.3's additional requirements are enforced |
| `absences[]` | array of `mk:abs:` | **what the thread cannot show, and why** (§10.1), typed under §3.7 |
| `missions[]` | array of `mk:msn:` | Missions available along the way |
| `entry_points[]` | array of `mk:exh:` | where a visitor may join. A Journey with one entry point and a fixed order is a corridor, and must justify being one. |
| `export_profile` | reference | exportable as a claim set (§10.1, §5.2) |
| `age_bands[]` | array | declarative |
| `preconditions[]` | array | §8.7, aggregated |
| `constraint_block` | Constraint Block | §5.2 |

### 11.3 Living World requirements, as constraints

When `living_world = true`, museum framework §10.1's five requirements become
validation rules:

1. **It creates no private content.** Every Exhibit it traverses stands alone
   and is reachable without it. `traverses` links may not point at an Exhibit
   whose `release_state` is anything but `published`, and no Exhibit may exist
   solely as a Journey stop. §10.1: *"It creates no private content and no claim
   that does not exist outside it."*
2. **It crosses at least four postures, including at least one of Extraction /
   Collection or Reconnection.** Computed from `postures_crossed[]` and enforced.
   §10.1: *"A Living World that visits only the pleasant postures is a
   brochure."*
3. **Its through-line claim set is listed and statused at the entrance**, before
   the visitor walks it.
4. **It carries its own absences**, typed.
5. **It is exportable as a claim set.**

Requirement 2 depends on the posture count, which museum framework **D-015**
may reduce from seven to six. The rule is written as "at least four of the
assigned postures, including at least one of Extraction / Collection or
Reconnection" — the framework's own wording — so that it survives either answer: neither of the two named
postures is the one D-015 is about.

### 11.4 Route is an assertion, and `fixed` is the exception

Museum framework §8.3 on the language mode's seven settings: *"It is not a
route … because the itinerary is itself the contested claim."* §8.7 lists
*"animate a movement that is not a statused transition"* among the things the
Atlas may never do.

A Journey is an itinerary by construction, so the rule cannot be "no
itineraries". It is:

> **`traversal_order` defaults to `free`. `suggested` requires a stated reason
> that is pedagogical, not historical. `fixed` requires either a stated
> pedagogical necessity or, where the order implies a sequence in time, in
> causation, in influence or in derivation, a statused claim in
> `through_line_claims[]` carrying that sequence with its own evidence,
> alternatives and falsifiers.**

The test for whether an order asserts: **would a visitor who walked it in
reverse learn something false?** If yes, the order is a claim. If they would only
be confused, it is pedagogy.

This is where a Journey most easily becomes an argument the institution has not
made. A route from steppe to Punjab to the Ganges asserts a migration whether or
not a sentence says so, and a route ending on MelaKeela's preferred explanation
asserts that it is where the evidence leads. Both are claims with statuses or
they are not routes.

### 11.5 Grounding

A Journey carries **both** a direct grounding (`through_line_claims[]`,
non-empty) and composition grounding through its Exhibits.

The direct link is required because the through-line is the one thing a Journey
adds. Without it a Journey is a list of Exhibits — which is a legitimate object,
but it is a search result set (§7.2), and search result sets are already
addressable, exportable and citable. **A Journey that asserts no through-line is
a saved search, and should be one.** This is not a demotion: a saved search is
honest about being a filter, and the export at §5.2 carries the query, the
facets, the date and the base revision.

### 11.6 Rules

- **Journeys add route, not content** (§7.5). An Exhibit shows the same claims
  with the same statuses whether reached from a Journey, a search or an external
  citation.
- **The through-line claim set is shown before entry, with statuses.** A
  visitor may decline to walk a thread made of hypotheses; that is a legitimate
  response and the entrance must make it possible.
- **Proportionality applies to the traversal** (§3.10). A Journey that spends
  six Exhibits on the explanation the evidence supports weakly and one on the
  explanation it supports strongly has allocated space against weight, and the
  divergence is a review finding.
- **Absences are part of the thread, not an appendix.** What the thread cannot
  show is displayed within it, typed, at the point where a visitor would expect
  to see the thing that is missing.
- **Decay.** When an Exhibit in `traverses[]` is withdrawn, the Journey shows the
  gap rather than closing over it — the same discipline §3.4 requires of a
  custody chain, where *"gaps are steps"* and rendering a three-step chain as two
  is laundering. A Journey that silently reroutes around a withdrawn Exhibit has
  made its route look more complete than the record.
- **A Journey may not be paced.** No timers, no "you are 40% through", no
  sequence lock that withholds a later Exhibit until an earlier one is
  completed. §10.4.4 forbids time pressure; a completion lock is time pressure
  with the clock hidden.
- **The Constraint Block binds the Journey as a whole**, as it binds the Mission
  (§10.6): a sequence of permissible Exhibits can compose an impermissible
  argument, most obviously by ordering material so that a classification appears
  to be discovered.

---

## 12. Learning Objective — `mk:lob:`

### 12.1 What it is

**A Learning Objective states what a visitor should be able to *do* after an
Activity or Mission, and names the objects it is taught on.**

Museum framework §10.5.1 identifies what this institution actually has to teach:
*"The method, taught as the content. The fourteen steps, the negative-evidence
types, the attestation gradient and the difference between citation count and
independent-source count are teachable objects in their own right, and they are
the most transferable thing this institution has."*

That sentence sets the object's centre of gravity. The primary Learning
Objectives of this institution are about **how to handle a record**, not about
what happened in South Asia. A visitor who leaves able to ask "how many
independent sources, and are they independent?" has got something that survives
every revision this record will undergo. A visitor who leaves believing a
`PROVISIONAL` claim has been given something that may not survive the year.

### 12.2 Fields

| Field | Type | Notes |
|---|---|---|
| `id` | identifier | `mk:lob:<key>` |
| `revision` | integer | append-only |
| `objective` | string | stated as a capability: "can distinguish an attested form from a reconstructed one", not "understands the attestation gradient" |
| `objective_plain` | string | the same at the lowest reading age in `age_bands[]` |
| `objective_type` | enum | `method` · `record-literacy` · `evidence-class-literacy` · `institutional-literacy` · `specific-content` |
| `taught_on[]` | array of `mk:rel:` (`taught-on`) | the claims, absences, evidence or relationships used as the worked cases. **Non-empty. This is the objective's grounding.** |
| `claim_status_ceiling` | derived | the highest status among `taught_on[]` targets — constrains `assertion_form`, §12.4 |
| `assertion_form` | enum | `can-state-what-is-claimed` · `can-apply-the-method` · `can-identify` · `knows-that`. **`knows-that` requires every `taught_on[]` target to be `VERIFIED`.** §12.4. |
| `demonstrated_by[]` | array of `mk:act:`, `mk:msn:` | via `prepares-for` |
| `assessment` | enum | `none`. The only permitted value. §12.5. |
| `curriculum_alignments[]` | array | optional, external syllabus codes as a convenience layer only. §12.6. |
| `age_bands[]` | array | declarative |
| `prerequisite_objectives[]` | array of `mk:lob:` | ordering within the objective set, not a lock on content |
| `constraint_block` | Constraint Block | §5.2 |

### 12.3 The five objective types

| Type | What it teaches | Example shape |
|---|---|---|
| `method` | one of the fourteen steps, applied | "can apply a chronology gate to a proposed link" |
| `record-literacy` | how to read the record's own vocabulary | "can tell `NOT EXCAVATED` from `ABSENT DESPITE ADEQUATE SEARCH` and say why the difference matters" |
| `evidence-class-literacy` | what a class of evidence can and cannot show | "can say what a radiocarbon determination dates, and what it does not" |
| `institutional-literacy` | how archives and institutions produce what survives | "can say who made this record, who preserved it, and who is missing from it" |
| `specific-content` | a fact about the past | strictly constrained by §12.4 |

The ordering is deliberate and is a position, not a taxonomy: **`specific-content`
is last and is the one type whose objectives expire.** A record built to
contradict its own previous answers (constitution §2) should not send visitors
away holding its current answers as the thing they learned.

### 12.4 An objective may not outrun the status of what it is taught on

> **A Learning Objective may not require a visitor to hold as true anything the
> institution has not verified.**

`assertion_form` is constrained by `claim_status_ceiling`:

| Highest status in `taught_on[]` | Permitted `assertion_form` |
|---|---|
| `VERIFIED` | any, including `knows-that` |
| `PROVISIONAL` | `can-state-what-is-claimed`, `can-apply-the-method`, `can-identify` |
| `HYPOTHESIS` | `can-state-what-is-claimed`, `can-apply-the-method` |
| `SUPERSEDED` | `can-state-what-is-claimed`, `can-apply-the-method` — and the objective must show the succession, since §3.6 makes it navigable in both directions |
| `INHERITED-UNVERIFIED` | **not publishable** — §12.4.1 |
| `REJECTED` | `can-state-what-is-claimed`, `can-apply-the-method` — teaching why it was rejected is legitimate and valuable |
| `HOLD` | **not publishable** — §12.4.1 |

#### 12.4.1 Why two statuses are not publishable rather than merely capped

This is museum framework §3.2's derivation rule and §3.12's derived-asset rule in
the same register. §3.12: *"a derived asset may not be commissioned or published
while the claim it depicts is `INHERITED-UNVERIFIED` or `HOLD`."* An objective is
a derived asset of the claims it is taught on — it is commissioned from them, it
depicts them, and it goes stale with them — so the rule applies to it whole, and
it is a rule about publication, not about phrasing. An objective whose only
worked cases are `INHERITED-UNVERIFIED` or `HOLD` does not publish at a reduced
assertion form; it does not publish.

An objective may still be *taught on* such a claim among others, provided at
least one worked case sits above the bar, and the `HOLD` is disclosed. The
scheduling consequence is the one §3.12 intends: **the objective schedule is a
function of the verification schedule and cannot invert it.**

**Decay follows automatically.** When a claim taught at `knows-that` is
superseded or rejected, the objective's ceiling drops and the objective is
suspended until it is rewritten. This is `decay_behaviour = hold` (§4.3) and it
is the case that most justifies the whole grounding rule: without it, the
institution's teaching materials are the last thing to learn that its claims have
changed, and they are the part of its output that travels furthest.

### 12.5 No assessment, and what that costs

`assessment = none` is the only permitted value.

Museum framework §10.5.2: *"No student accounts, no student data, no assessment
scoring. The institution supplies material; it does not grade children."* §9.3:
no score, no points, no "correct". §10.4.4: no competition, no scoreboard, no
time pressure.

The cost is that the institution cannot tell whether an objective was met. That
is a real loss, it is not recovered by a proxy, and no substitute is specified:
completion tracking, quiz scores, time-on-task and "confidence sliders" are all
assessment with the word removed, and each of them requires the per-visitor data
§10.5 has ruled out.

What is available instead: the aggregate, non-identifying usage counts §10.4.5
permits with a published measurement policy, and the teacher's own judgement,
which is what classroom mode's preparation material (§10.5.1) exists to support —
*"written for a teacher who is not a specialist and has an hour."*

### 12.6 Curriculum alignment is a convenience layer

Museum framework §10.5.2: *"Curriculum-alignable, not curriculum-bound. The
institution may map its material to a syllabus as a convenience layer. It may not
alter a claim, a status or an absence to fit one."*

As object rules:

- `curriculum_alignments[]` is metadata on the objective. It may not appear in
  `taught_on[]`, may not affect `assertion_form`, and may not affect any claim's
  status.
- **Where the institution's record and a curriculum disagree, the objective says
  they disagree and shows the evidence, in both directions** — *"this applies
  equally where the curriculum is the one this project would prefer."* That
  sentence is the whole reason alignment is safe to offer at all, and it is a
  required behaviour of any aligned objective, not a caveat.
- An alignment that would require `knows-that` on a claim below `VERIFIED` is
  refused. The syllabus does not raise a status.
- Which curricula are mapped, if any, is not decided here: it interacts with
  release scope (`OWNER-DECISIONS.csv` D-008) and language commitments
  (museum framework D-031). Recorded as **D-047**.

### 12.7 Grounding, and the one objective that looks ungrounded

Every Learning Objective needs a non-empty `taught_on[]`, including the `method`
and `record-literacy` types — which is the case where the rule looks hardest to
satisfy and is in fact where it does most good.

"Can tell an attested form from a reconstructed one" is an objective about a
vocabulary (§2.6), and a vocabulary is not an evidence object. But the objective
is not taught on the vocabulary; it is taught on **specific forms**: this
attested word at this locator in this edition, beside this reconstruction with
the method that produced it and the scholar who proposed it. Those are `mk:lex:`
and `mk:evd:` objects with identifiers.

An objective that cannot name its worked cases has not been designed yet, and
the grounding rule catches that at creation rather than at the point where a
teacher opens it and finds an abstraction.

### 12.8 What a Learning Objective may never be

1. **An objective to hold a claim as true above its status** (§12.4).
2. **An assessment, or anything that functions as one** (§12.5).
3. **An objective requiring the visitor to sort people, score a classification
   or move through a staged persecution** — the Constraint Block binds this
   object as it binds the rest (§5.2), and an objective is where such an exercise
   would be justified as pedagogically necessary. It is not available as a
   justification: §10.4.7's second constraint is explicit that *"it makes no
   difference that the classification is being taught as false."*
4. **An objective phrased as an identity claim about the visitor** — "understands
   their own heritage", "connects with their ancestors". Language is not a proxy
   for identity anywhere in the product (§11.10.2), and no surface may vary its
   content by interface language; an objective that assumes who is reading has
   done both.
5. **An objective the institution cannot maintain in every language it offers**
   (§11.10.4). A stale objective is worse than none, for the same reason a stale
   translation is: it publishes superseded material under the institution's name
   to the readers least able to check it.

---

## 13. Character — `mk:chr:`

### 13.1 Why this is the hardest object, and what makes it hard

Every other object in this document is a container for evidence. A Character is
a **person, or something shaped like one**, and the shape is the problem: the
moment an institution puts a figure on a surface, a visitor supplies everything
the record does not — a voice, a face, a motive, an interior. That supplying
happens whether or not the institution intended it, and no disclaimer prevents
it.

Three specific hazards, in ascending order of how easily they are excused.

**H-1. Invented dialogue.** The oldest device in museum interpretation and the
one the record forbids outright. Museum framework §10.4.4: *"No fabricated
evidence, ever. No invented objects, no composite 'typical' artefacts."* A
sentence a historical person did not say is fabricated evidence in the most
persuasive available form, because speech reads as testimony. It does not become
permissible by being plausible, by being marked as imagined, or by being placed
in a children's surface where the marking will not be read.

**H-2. Fabricated interiority.** Harder to see, because it hides in the
connective tissue rather than in quotation marks. "She would have watched the
river rise." "He must have known what the seal meant." "They feared the drought."
None of these is a quotation and each asserts a mental state for which there is
no evidence and could not be. Constitution §4V asks who *"spoke without being
recorded"*; attributing thought to that person is not answering the question,
it is closing it.

**H-3. Voicing the subaltern.** The hardest of the three because the impulse is
generous and the failure is invisible to the person committing it. The record
documents, repeatedly, who was not recorded: the builders behind a donor
inscription (§10.2, constraint 3), the labour behind a tank, the people a
nineteenth-century survey classified without asking. Having established that
silence and typed it — `NOT PRODUCED`, `NOT RECOGNISED` — the institution then
feels the pull to fill it, and filling it feels like restitution.

It is the opposite. **A voiced subaltern character destroys the evidence of the
silence.** The typed absence was the finding; the invented voice replaces a
documented gap in the archive with a satisfying presence, and a visitor who meets
the character does not learn that the archive is missing them — they learn a
story, and they leave believing the record contains something it does not. The
institution has taken the one piece of evidence it actually had about that
person's erasure and covered it over, and it has done so in the register that
feels most like repair.

**Constitution §4V is the ruling here**: *"Preservation is not authorship;
codification is not invention; first attestation is not origin."* The remedy for
a silence is to name who is missing, type the absence, name the archive that
produced it, and leave it visibly unfilled. Museum framework §6.2, item 6
already specifies the display: the §4V provenance questions are shown on every
object and *"unanswered questions are displayed as unanswered, not omitted."*

### 13.2 What a Character therefore is

**A Character is a presentational role bound to evidence, not a person the
institution has invented.** It is a way of attributing something on a surface —
words, a piece of work, a judgement, an act of holding or classifying — to
whoever the record actually attributes it to.

There are exactly four kinds. The enumeration is **exhaustive and mutually
exclusive**, and it is closed: a Character that is not one of these four cannot
be created, and a fifth kind requires a revision of this document rather than a
field value.

| `character_kind` | Is a person? | May speak? | Grounded in |
|---|---|---|---|
| `role` | No — a documented function, never an individual | No | claims establishing that the role existed, there and then |
| `documented-individual` | Yes, a named historical person | Only their attested words, as quotation | sources attesting them, with locators |
| `present-day-investigator` | Yes, a living person | Yes, their own words | their own statements as `oral-living` evidence + a consent record |
| `institutional-voice` | No — the institution speaking as itself | Yes, in the institution's voice | the claim set it is speaking |

### 13.3 The four kinds, specified

#### 13.3.1 `role`

**What it is.** A documented social, occupational or functional position: the
person who fired this pot, the scribe who copied this recension, the surveyor who
recorded this site in 1883, the labourers who cut this tank.

**Requirements.**

- The existence of the role in that place and period is itself a statused claim
  in `exercises[]`. A role nobody has evidenced is an invention with an
  occupational noun on it.
- It is described only in terms the evidence supports: what the work involved,
  what it required, what materials and techniques it used, what the record does
  and does not say about who did it.
- **It is never individuated.** No name, no biography, no single figure standing
  for the role. "A potter" is a role; "a potter named Ila" is an invented person.
- **It carries an explicit unrecorded register.** The §4V questions — who made
  it, supplied the material, did the labour, spoke without being recorded, was
  excluded — are on its face, and the unanswered ones are typed as Absence
  records (§3.7), not written as pathos. "We do not know their name, whether they
  were free, or what they thought, and here is why the record does not say" is
  the correct output and is more informative than any characterisation.
- **It carries no identity attributes.** No ethnicity, ancestry component,
  caste, religion-as-identity or modern nationality (§5.2,
  `identity_attribution = none`).

**Why the role is the workhorse.** Almost everything an institution wants a
Character for — showing that objects were made by people, that texts were copied
by hands, that surveys were conducted by someone with an agenda — is available
here without inventing anybody. The role is what makes it possible to obey H-1
to H-3 and still have people in the museum.

#### 13.3.2 `documented-individual`

**What it is.** A named historical person attested in the record: a donor in an
inscription, an author, a ruler, a translator, a colonial officer, a
nineteenth-century scholar.

**Requirements.**

- Every utterance is `attested-in` a `mk:evd:` at a locator, in an edition, with
  the `is_primary` step rendered (§2.5) so a visitor can count the steps between
  the person and what they are reading.
- **Words appear as quotation, never as dialogue.** Not converted to the present
  tense, not addressed to the visitor, not paraphrased into first person, not
  extended by a clause the source does not carry.
- The Translation Block (§3.8) applies in full where the words are not in the
  visitor's language: original script, transliteration, grammatical form,
  semantic range, textual context, edition, exact locator, translation used,
  alternative translations, interpretive consequence, inherited-category audit.
  **A Character is exactly where a translation would otherwise decide a
  historical question quietly**, because words in a person's mouth are read as
  transparent.
- **A reconstructed, emended or conjectural reading is displayed as one**
  (§2.6). A Character may not speak an editor's conjecture as their own sentence.
- **No interiority beyond their own attested statements**, and those are
  presented as their statements rather than as their mind. A person who wrote "I
  feared" is recorded as having written it; that is a fact about a text.
- **An archive-position statement is required** — §13.4.

#### 13.3.3 `present-day-investigator`

**What it is.** A living person: an excavator, a conservator, an epigraphist, a
translator, a curator, a community member, a technician. The person doing the
work now, shown doing it.

**Requirements.**

- **A consent record is required and non-null** (`mk:cns:`, §11.4), covering
  each surface separately — exhibit, atlas, children's mode, classroom, export,
  third-party reuse. Consent to appear in an exhibit is not consent to appear in
  a children's investigation or under a reuse licence.
- **They speak for themselves.** Their words are `oral-living` evidence
  (§2.4) with recording circumstances, withdrawal terms and whether they hold
  interpretive authority. The institution does not write their lines, does not
  edit them beyond length limits stated in advance (the §11.3 discipline
  generalised), and does not summarise them into the institutional voice.
- **Withdrawal is effective on the live surfaces without negotiation** (§11.4).
  The material goes; the record that it was contributed, published and withdrawn
  on a stated date under a stated term remains. The revision takes §3.6's `retracted-for-consent`, and every Character the
  material appeared in is suspended by it.
- **Interest is disclosed** where they are also the author of a claim the
  surface presents. A researcher explaining their own finding is not a neutral
  guide to it, and the visitor is told which they are looking at.
- **A community member with interpretive authority carries the authority record**
  (§11.2): the community named as it names itself, the representative and how
  they were identified, the scope, and *"who this does not speak for."* Their
  account is carried as theirs, in their own voice, not absorbed into the
  institution's and not "balanced" against a scholarly account as though the two
  were rival hypotheses in the same game.
- Whether an individual's consent suffices where the material is under a
  community authority, or whether the community agreement is additionally
  required, is **D-048**.

#### 13.3.4 `institutional-voice`

**What it is.** MelaKeela speaking as itself: the "MELAKEELA'S CURRENT
INTERPRETATION" register of the Step 14 shape, and the method guide that explains
what a status is, what `NOT EXCAVATED` means, why nine citations can be one
source.

**Requirements.**

- **Grounded like everything else.** The institutional voice speaks a claim set
  with statuses, and every sentence resolves (§3.4). It is not exempt from the
  grounding rule by being the institution's; it is the object where the exemption
  would be asked for and where §2.8 refuses it.
- **Not a persona.** No name, no biography, no personality, no opinions beyond
  the institution's statused positions, no relationship with the visitor.
- **Speaks last on any question** (§9.3, §7.4). The institutional voice does not
  introduce a Challenge or a Mission; it closes one.
- **May say "we do not know", "we were refused access", "we were wrong"** —
  and these are among the most useful things it says. The correction ledger and
  the obligations register are its material as much as the claims are (§1.6.2).
- Whether the method guide may be personified for children — given a name, a
  drawn body, a voice — is **D-049**.

### 13.4 The archive-position statement

**Required on every `documented-individual` Character, and on any `role` whose
evidence comes from a curated archive.**

The set of individuals this record can name is not a sample of the people who
were there. It is the set the archive recorded and preserved: the literate, the
donors, the rulers, the officials, the colonial surveyors, the European
philologists. A museum built out of documented individuals reproduces the
archive's hierarchy exactly, and does so while appearing merely to be citing
sources.

The statement carries, for each such Character: **who recorded them, why that
record was made, what preserved it, and who is absent from the same record and
why** — constitution Step 6's archive audit, attached to the person rather than
to the corpus.

Two display rules follow:

- **A surface may not present its documented individuals as the people who were
  there.** Where named individuals appear, the roles and the typed absences that
  surround them appear with them, at a weight the proportionality discipline
  (§3.10) can be tested against.
- **`CLAUDE.md`'s governing principle applies to the cast.** *"Do not balance
  narratives. Weight explanations."* The corrective is not to invent a
  counterweight of subaltern voices — that is H-3 — but to make the asymmetry
  itself visible, with the asymmetry statement (§11.2) where the two adversarial
  tests are shown.

### 13.5 Fields

| Field | Type | Notes |
|---|---|---|
| `id` | identifier | `mk:chr:<key>` |
| `revision` | integer | append-only |
| `character_kind` | enum(4) | §13.2. Exhaustive, mutually exclusive, closed. |
| `label` | string | for `role`, the function; for `documented-individual`, the name as attested with its source; for `present-day-investigator`, the name as they give it or an agreed anonymisation; for `institutional-voice`, the institution |
| `is_person` | derived bool | false for `role` and `institutional-voice` |
| `attested_in[]`, `speaks_for[]`, `exercises[]` | arrays of `mk:rel:` | named by predicate, as on every other object, so §14.4's export needs no special case for Character. At least one is non-empty; which one is required depends on `character_kind` — §13.7. |
| `attested_utterances[]` | array | each: `mk:evd:` · locator · edition (`mk:src:`) · `is_primary` step · original script · Translation Block ref · reading status (`attested` · `emended` · `conjectural`) |
| `interiority` | enum | `none`. The only permitted value. §13.6, item 2. |
| `archive_position` | Block or null | **required for `documented-individual`**, §13.4 |
| `role_absences[]` | array of `mk:abs:` | **required for `role`**: the typed absences that constitute what is not recorded about the people in it |
| `consent_ref` | `mk:cns:` or null | **required and non-null for `present-day-investigator`** |
| `authority_ref` | `mk:rel:` or null | the community-authority record where one applies (§11.2) |
| `interest_disclosure` | string or null | required where a present-day investigator authored a claim on the same surface |
| `identity_attribution` | enum | `none`. §5.2. |
| `depictions[]` | array of `mk:evd:` | any image, illustration, model or audio. Each `is_primary = interpretation`, with maker, date and reconstruction marker. §13.6, item 8; subject to **D-050**. |
| `voice_rendering` | enum | `quotation-only` (default) · as constrained by **D-051** |
| `surfaces_permitted[]` | array | per consent and per rights, each surface separately (§11.4, §11.8) |
| `withdrawal_state` | enum | `active` · `suspended` · `withdrawn`. A withdrawal is recorded with §3.6's existing `retracted-for-consent`, not a new value. |
| `age_bands[]` | array | declarative |
| `constraint_block` | Constraint Block | §5.2 |

### 13.6 What a Character may never be

The list is long because each item names something that has been done in museums
and would be done again by default. Each is refused by a field constraint, not
only by this prose.

1. **An invented historical person.** Named or unnamed, speaking or silent. No
   composite, no "typical", no representative figure standing in for a
   population — "a Harappan girl", "a Sangam-era merchant", "a village
   ironworker". §10.4.4: no fabricated evidence, no composite artefacts. A
   composite person is a composite artefact in the shape of a human being.
2. **A source of interiority.** No thoughts, feelings, motives, beliefs, fears,
   intentions or sensory experience attributed to any past person, including a
   documented one, beyond what their own attested words state — and those are
   presented as their statement, not as their mind. `interiority = none` has one
   permitted value.
3. **A voice for someone the archive did not record.** §13.1, H-3. Where the
   record documents a silence, the silence is typed, named and left visible. The
   institution does not fill a gap it has just proved exists.
4. **A carrier of identity.** No ethnicity, race, ancestry component, caste,
   religion-as-identity or modern nationality as a property of a Character. Every
   such link is a §4.4 bridge with its mechanism, rivals and governance, or it is
   not displayed (§6.7). §10.4.4 forbids ethnic and national identification of
   objects, people and remains outright in the children's mode.
5. **A speaker of a reconstructed language.** Voicing a reconstruction converts
   `reconstructed` into `attested` in the visitor's ear (§2.6), and no marker
   survives audio. No "how it sounded" for a proto-language at any age, and no
   recorded performance of a reconstructed form without the reconstruction
   marker, the method that produced it and the proposer.
6. **A personified set of human remains.** No "meet the person from grave 4".
   §10.4.4: remains are shown only where community authority and consent permit,
   *"at the least sensational presentation possible, and never as a puzzle to be
   solved"*, and whether they are displayed at all is museum framework D-026.
7. **A named living person without consent, or after withdrawal** (§11.4).
8. **A synthesised likeness or voice of a real person**, living or historical,
   by any means. It is fabricated evidence (§10.4.4) whatever the technique, and
   for a living person it is also a consent violation that consent could not
   cure, because the person did not say the thing.
9. **An avatar the visitor becomes in the past.** `role_play = none` or
   `present-day-method` (§5.2): "do what a researcher does with this evidence
   now" is available; "be a person in the past" is not, and being placed in any
   position within a classification, in any period, at any age, is refused
   absolutely (§10.4.7).
10. **A figure in a staged persecution.** §10.4.7's third constraint. Persecution
    is read as record, with its evidence and its status; it is never
    dramatised, role-played, simulated, scored or reconstructed as an experience
    the visitor moves through.
11. **An opponent, an advocate or a guide with a position.** No Character argues
    for an explanation in a Challenge, none opposes the visitor, and none
    expresses confidence the record does not carry. A Character who says "I think
    the evidence points this way" has published an unstatused claim in the most
    persuasive available register.
12. **A resolver of open questions in dialogue.** Where a Question is `open`, no
    Character closes it; the institutional voice states the open state and the
    absences.
13. **A term in a COMPARE Activity.** §5.2's enumeration has no class for a
    person, and a Character resolves to a person or to a role held by people.
    Two Characters may not be set beside each other as things to be sorted.
14. **A mascot for a people, a place, a language or a period.** That is identity
    attribution (item 4) with a friendly face on it, and it is the form in which
    it is hardest to object to.

### 13.7 Grounding

Every Character carries at least one direct Grounding Link. Composition
transitivity (§2.5) does not apply: a Character is not grounded by the Exhibit it
appears in.

| Kind | Minimum grounding |
|---|---|
| `role` | ≥1 `exercises` link to a claim establishing the role in that place and period, **and** ≥1 Absence record in `role_absences[]` |
| `documented-individual` | ≥1 `attested-in` link to evidence with a locator, **and** an `archive_position` block |
| `present-day-investigator` | ≥1 `speaks-for` link to an `mk:agt:`, **and** a non-null `consent_ref` |
| `institutional-voice` | ≥1 `exercises` link to the claim set being spoken |

**This is the object §2.2's reason G-3 was written for.** An ungrounded Character
is not a Character with a missing citation. A Character *is* the evidence it
resolves to, plus a way of presenting it; remove the evidence and what remains is
not an incomplete record but an invented person. The grounding rule is not a
documentation requirement here. It is the entire difference between attribution
and fabrication, and it is why the rule admits no waiver, no draft state and no
editorial override.

### 13.8 Decay

- **A superseded or rejected grounding claim suspends a `role`.** A role
  established by a claim that no longer holds is a role the record no longer
  evidences.
- **Withdrawn consent suspends a `present-day-investigator` immediately**, on
  the live surfaces, without negotiation (§11.4). The record that they appeared
  and withdrew remains; the material does not.
- **A contested attestation degrades a `documented-individual` rather than
  removing them.** If a reading that a person said something is challenged —
  §11.6 `nature = translation-dispute` or `factual-error`, or an Evidence Link
  with the `contests-reading` role (§3.3), which is an evidence role and not a
  correction nature — the utterance is shown with the dispute rather than quietly
  dropped — the same discipline §7.1
  item 3 requires of the primary-source viewer, where *"variants are first-class"*
  and differences are *"shown, not silently normalised."*
- **A Character never survives its grounding.** `grounding-lost` (§3.3) suspends
  the Character, and a suspended Character resolves to a record of what it was
  and why it is suspended, in keeping with §2.1's tombstone rule.

### 13.9 The Character that is deliberately not built

The most important Character in a record like this one is the one the institution
does not create: the person who made the object, did the labour, spoke without
being recorded, and was classified without being asked.

They are represented by **an Absence record and a role, never by a figure**.
Concretely, where a donor inscription records a donor and not a builder
(museum framework §10.2, constraint 3), the surface carries:

- the donor as a `documented-individual`, with their archive position — who
  recorded them, why, and what preserved it;
- the builders as a `role`, described from the work itself, with no name, no
  face and no voice;
- an Absence record typed `NOT PRODUCED` or `NOT RECOGNISED`, with what should
  have existed, where, the probability it was produced, whether we would
  recognise it, and the archive audit that explains the shape of the gap;
- the §4V provenance questions, with the unanswered ones displayed as unanswered.

A visitor who leaves that surface knows something true and specific: that the
record preserves donors and not builders, that this is a property of what
inscriptions were for, and that the absence has been measured rather than
regretted. A visitor who instead met an invented builder with a name and a
feeling would leave with a story, and would not know that the record is missing
him.

**That is the whole argument of this section in one comparison, and it is why the
Character object is specified as narrowly as it is.**

---

## 14. Composition, modes and the publication gate

### 14.1 How the eight objects compose

```
Journey ──traverses──▶ Exhibit ──presents──▶ Claim / Relationship / Absence
   │                      │
   │                      ├──activities──▶ Activity ──exercises──▶ Claim / Rel / Absence
   │                      ├──characters──▶ Character ──attested-in / speaks-for──▶ Evidence / Agent
   │                      └──question_refs──▶ Question ──bears-on──▶ Evidence / Claim / Absence
   │
   └──missions──▶ Mission ──question_ref──▶ Question
                     └──assembles──▶ Activity, Challenge ──targets──▶ Claim@r<n>

Learning Objective ──taught-on──▶ Claim / Absence / Evidence
                   ◀──prepares-for── Activity, Mission
```

Every arrow into the right-hand column is a Grounding Link (§4). Every arrow
within the experience layer is composition, which carries grounding only under
§2.5 and asserts nothing about the past.

### 14.2 The mode matrix needs no new row

Museum framework §1.7 gives a posture-to-mode matrix over five modes: Source,
Atlas, Investigation, Field, Classroom. The eight objects add no sixth mode.

**Experience objects are realised *in* modes and inherit the matrix from the
mode they run in.** An Activity has a `mode`; a Mission takes its constraints
from its `exhibit_context`'s posture; a Journey's constraints are the union of
its Exhibits'. Three consequences worth stating because they are load-bearing:

- **Field-mode objects cannot exist in the Extraction / Collection or
  Reconnection postures.** A posture reassignment that moves an Exhibit into one
  of them suspends its Field Activities and the Missions built on them (§7.5,
  §10.6). A child may read a custody record; a child may not be assigned a
  verdict on one (§10.4.6).
- **Investigation Mode is mandatory in Tamil Retrofuture, Reading Room and
  Extraction / Collection**, which means every Exhibit in those three postures
  carries at least one Challenge. That is the framework's own rule (§1.7) with a
  countable consequence: an Exhibit in one of those postures with no `mk:chl:` is
  incomplete, and the gate can say so.
- **Source Mode is mandatory everywhere**, so every experience object is one
  interaction from the claims, statuses and sources behind what it shows.

### 14.3 The publication gate

An experience object publishes when all of the following hold. Each is checkable
without human judgement except where a named person is required, and those are
named rather than implied.

1. **Grounding resolves.** At least one direct Grounding Link — or, for a
   Mission alone, composition members that have one (§2.5); every link's target
   resolves; no target is retracted, withdrawn or tombstoned; no link's target is
   another experience object (§2.1).
2. **Status ceilings hold.** No link's status exceeds its target's (§4.3). No
   Learning Objective's `assertion_form` exceeds its `claim_status_ceiling`
   (§12.4). No Activity has `has_right_answer` on a claim below `VERIFIED`
   (§8.2).
3. **The Constraint Block validates**, on resolved referents rather than
   declared classes (§5.3), for the object and — for containers — for the
   sequence (§10.6, §11.6). `field_mode_postures_respected` is re-asserted
   against the current posture assignment, not the one held at creation.
4. **Preconditions are in force**, not merely requested: consent records
   unlapsed, rights not `unknown`, community-authority agreements current
   (§8.7).
5. **The common fields of §5.5 are present and resolve**: `release_state`,
   `editorial_decision_ref`, `accessibility_equivalent`, `preconditions[]`,
   `bias_test_context` and the revision metadata. An accessibility equivalent
   carries the same evidential content including status, attestation mode and
   uncertainty (§11.9.1–2).
6. **Both adversarial tests have run** — on the containing Exhibit, or on the
   object's own pair where it has no containing Exhibit (§5.5) — with the
   asymmetry statement where they are shown together (§3.11, §11.2).
7. **The Step 14 shape is complete** on the Exhibit, with no heading empty and
   `copy_complicates` either populated or carrying an explicit `none-found` with
   the bias-test rows that searched (§7.4).
8. **A named person has signed the Constraint Block review** (§5.2). The block
   is not self-certifying, and the workbook's `Owner/status = Unassigned` on
   38 of 38 rows (`INHERITED-UNVERIFIED`) is the state this requirement exists to
   end.
9. **An editorial decision row exists** in `03-REGISTERS/editorial-decisions.csv`
   with a rationale and a person, rendered `publication:*` so it can never be
   read as an evidence status (§11.5).
10. **The object-specific invariants hold**, each stated in its own section and
   listed here so the gate is one place: a Journey's `traverses[]` has at least
   two members and, where `living_world = true`, §11.3's five requirements pass;
   a Challenge has `independence_tree_shown = true` and a non-empty
   `evidence_set[]`; an Activity's free-text output has `output_is_private =
   true`; an Exhibit in a posture where Investigation Mode is mandatory has that
   mode enabled; a Learning Objective's `taught_on[]` does not consist wholly of
   `INHERITED-UNVERIFIED` or `HOLD` claims (§12.4.1).

**Three of the ten need a person, and they say so.** Conditions 3, 6 and 7 are
not machine-decidable: the Constraint Block's judgement residues are at §8.4,
the adversarial tests are run by a tester under §3.11, and `copy_complicates`'s
`none-found` value asserts that a search happened. The other seven are checkable
mechanically. Claiming otherwise would be the same overselling §8.4 now warns
against.

**Failing the gate is not a blocker to be waived.** Each of the ten names a
specific missing thing, and the missing thing is the work.

### 14.4 Export

Every experience object exports under museum framework §5.2 with the same
requirements: exports carry status, carry the exclusion set where a filter was
applied, are revision-pinned and dated, and resolve every identifier.

Two additions:

- **An experience export carries its Grounding Links**, with roles and
  `surface_role`. An export of a Mission that listed its Activities but not what
  they exercise would be a table of prompts, which is the artefact §5.2's status
  rule exists to prevent, in this layer's shape.
- **A visitor's own outputs export separately from the institution's content**
  and are never mixed with it (§10.3). Visitor text is the visitor's.

---

## 15. What this specification leaves to the owner

### 15.1 Decisions raised by this document

Written up in `DECISIONS-NEEDED.md`, against rows allocated in
`09-DECISIONS/OWNER-DECISIONS.csv`, which is authoritative for the namespace.

| ID | Decision | Section |
|---|---|---|
| D-046 | Do the §10.4.7 prohibitions bind surfaces outside the experience layer, or only child-facing and experience surfaces? | §5.4 |
| D-047 | Which school curricula, if any, do Learning Objectives map to? | §12.6 |
| D-048 | Does an individual's consent suffice where a community holds authority over the material? | §13.3.3 |
| D-049 | May the institutional method guide be personified for children? | §13.3.4 |
| D-050 | Does the institution depict past people visually at all, and under what marker? | §13.5 |
| D-051 | May attested words be voiced, or only quoted? | §13.3.2 |
| D-052 | Does any per-visitor progress state exist server-side, or is §10.3's opt-in Field Bag withdrawn? | §10.5 |

Four of the seven are Character decisions. That is not an accident of drafting:
it is what §13.1 predicts. Everything else in the experience layer can be settled by
asking what the evidence supports; a Character asks additionally how a person may
be presented, and that question is not fully answerable from the record.

### 15.2 Decisions cited but not re-raised

All of these are rows in `09-DECISIONS/OWNER-DECISIONS.csv`, which `CLAUDE.md`
makes authoritative for the whole namespace; where a row also has a prose section
in `DECISIONS-NEEDED.md`, that is its `detail_ref` and not a second allocation.

**Raised before the museum framework:** D-005 (is WATER the first Living World —
§11.1 of this document), D-006 (Keezhadi or an inscription as the children's
pilot — §8.7), D-008 (Release 1 scope — §12.6), D-010 (which institutional claims
may presently be published — §7.4.1), D-011 (the deferred set — §0.4).

**Raised by the museum framework:** D-015 (seven postures or six — §11.3), D-024
(is PROVE IT the correction intake — §9.1, §9.6), D-026 (human remains — §13.6
item 6), D-031 (which languages are maintained — §12.8 item 5).

**Raised elsewhere and cited here:** D-034 (the page and atlas site counts —
§7.2's title rule) and D-037 (the `MELA-KEELA-WHO-MADE-THE-PAST.md` section
numbering — §5.1), neither of which the framework raised.

**Three are load-bearing.** D-010 gates §7.4's `copy_supports`, and until it is
answered no Exhibit passes the publication gate. D-024 determines whether §9.6
exists at all. D-015 changes the posture count that §11.3's four-posture rule is
stated against; the rule is written so that it does not depend on the answer.

### 15.3 What this specification deliberately did not specify

Offered as input to the deferred register (museum framework §13.1) when the v2
backlog is available:

- Any instance of any of the eight objects. No Question, Exhibit, Activity,
  Challenge, Mission, Journey, Learning Objective or Character is created here.
- The children's pilot's content, which waits on D-006 and on the consent or
  rights precondition that pilot carries (§8.7).
- WATER's Journey instance, which waits on D-005.
- The editorial workflow by which experience objects are drafted and reviewed,
  beyond §14.3's gate and the rule that the Constraint Block is signed by a
  named person.
- Any migration of the 96 audited pages into Exhibits. Migration depends on the
  editorial decisions the museum framework deliberately does not take.
- Cost, lead time and staffing. Nothing here supplies estimates and none should
  be inferred.

---

## 16. Status of this document

Every design proposition here is `HYPOTHESIS`.

Every statement drawn from `01-INHERITED/curatorial-audit-v1.1/` or from
`06-BACKLOG/EXPANSION-PROMPT-2026-09-07.md` is `INHERITED-UNVERIFIED` and is
marked at the point of use. The three constraints at §5.1 are sourced to
`MELA-KEELA-WHO-MADE-THE-PAST.md` §9, which is not in this repository; their
wording is `INHERITED-UNVERIFIED` (`RESEARCH-QUEUE.md` `WMP-9`, numbering
discrepancy at D-037), and their standing as constraints does not depend on that
because they are prohibitions on what the institution builds, not claims about
the past.

**Both adversarial tests were run on this document** before it was submitted, per
`CLAUDE.md` §8, and the results are logged: `BF-X-001` and `BF-X-002` in
`04-AUDITS/BIAS-FAILURE-LOG.csv`, with the earlier work they touch in
`04-AUDITS/REAUDIT-QUEUE.csv`. The framework tension the second test surfaced is
`IC-X-001` in `04-AUDITS/INTERNAL-CONTRADICTIONS.csv`.

Nothing here has been retrieved, so no rows were added to
`02-SOURCES/access-ledger.csv` and no domains were requested.

This is a specification. Per constitution §15 and museum framework Rule S-3: it
is not an implemented page, no object described here exists, and it must not be
described as one.
