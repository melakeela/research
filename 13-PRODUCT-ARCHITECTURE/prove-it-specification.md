# PROVE IT — the investigation mode, its evidence packet, and one worked case

**Written:** 2026-09-08
**Unit type:** product specification. Report only.
**Companion to:** `13-PRODUCT-ARCHITECTURE/museum-framework.md` §9,
`13-PRODUCT-ARCHITECTURE/experience-object-model.md` §9.
**Worked case drawn from:** `03-REGISTERS/rigveda-pur-family.csv`,
`03-REGISTERS/rigveda-pur-4j-claims.csv`,
`03-REGISTERS/rigveda-pur-4j-interpretations.csv`,
`03-REGISTERS/rigveda-pur-counts.csv`, `03-REGISTERS/rigveda-pur-passages.csv`,
`03-REGISTERS/rigveda-pur-typology.csv`, `03-REGISTERS/rigveda-pur-fields.csv`,
`06-BRIEFS/rv01-reconciliation.md`, `02-SOURCES/dependency.csv`,
`05-HOLDS/HOLD-006-rigvedic-poet-attributions.md`,
`04-AUDITS/rigveda-pur-4j-method.md`, `04-AUDITS/BIAS-FAILURE-LOG.csv`.

---

## 0. What this document is, and the rules it runs under

### 0.1 What it specifies

Three things, and nothing else.

1. **The nine-stage run sequence**, and its reconciliation with museum framework
   §9.2's six stages and constitution Step 14's seven headings. The three
   sequences are not the same sequence and the differences are load-bearing.
2. **The Evidence Packet** — a new object, `mk:pkt:`, which is the reusable
   data structure a run is built from, and which is what makes the conclusions
   a surface offers a *derivation* rather than a menu.
3. **One worked case**, at §5: *did Indra's poets destroy ninety-nine forts?*
   Its **decision-bearing** fields are built out — `claims[]`, `status_floor`,
   `gates[]`, `absences[]`, `falsifiers[]`, `conclusion_set[]`,
   `withheld_conclusions[]` — with every claim identifier named and every
   ceiling and refusal derived. Its **rendering** fields are not:
   `evidence[]`, `translation_blocks[]`, `used_by[]`, the nine Activities' own
   EOM §8.3 fields, and the reviewer signature are named as unbuilt at §5.10
   rather than sketched. A worked case that filled them by invention would be
   the fabricated evidence §10.4.4 forbids.

The case is the point. Museum framework §9 and experience-object-model §9 have
already specified PROVE IT twice in the general. What neither has is an instance,
and the two design failures this document actually found — §6.1 and §6.2 — were
both found by building one, not by reasoning about the type.

### 0.2 The rules it inherits

The museum framework's three rules and the experience object model's fourth
govern here unchanged.

**Rule S-1 — No specification may cite a claim above its register status.** Every
claim used in the worked case is cited at the status its register gives it, and
the packet computes a floor rather than letting the reader infer one.

**Rule S-2 — Where a choice is the owner's and has not been made, the choice is
recorded, not taken.** This document raises no new `D-` row: everything it needed
was either already reserved (D-010, D-024, D-045, D-052) or is a specification
choice it may make and does make openly at §4.6.

**Rule S-3 — Specification does not promote.** Nothing here is a finding about
the past. No packet exists; the one at §5 is a worked design, not a built object.
No claim changes status because it appears in it.

**Rule S-4 — The experience layer holds no content of its own.** Every sentence
this document's worked case shows a visitor resolves to a register row, an
absence, a hold, a dependency row or a decision row, or it is marked as editorial
framing.

### 0.3 The rule it adds

**Rule S-5 — A surface may not offer a conclusion its packet cannot carry, and
may not conceal one it refuses.**

Both halves, or neither. The first half alone produces an institution that
quietly narrows what a visitor may think and calls it rigour. The second half
alone produces a menu with no discipline behind it. Together they produce the
only defensible form: the set of conclusions is derived from the evidence, the
derivation is shown, and every conclusion a visitor might reasonably want and
cannot have is displayed with the specific reason it is not available and the
specific thing that would make it available.

§4.5 is the mechanism. §5.8 is what it looks like when it is pointed at this
institution's own published page headline and refuses it.

### 0.4 What it deliberately does not do

- It does not settle **D-024** — whether PROVE IT is the correction intake. The
  packet is specified so that a negative answer removes §4.7's submission route
  and leaves everything else standing.
- It does not settle **D-010**, the accepted threshold. §4.4's `offer_ceiling`
  is written against the threshold parameter, not against a fixed status list.
- It does not settle **D-045**, whether the site's forts artefact keeps the
  inherited name. The worked case at §5.8 refuses a conclusion that the current
  name asserts; that is a finding about the interface, not a ruling on the name.
- It specifies no visual design, no copy and no page.
- It creates nothing. The three prerequisites the worked case turned out to need
  — a missing absence record, a missing asymmetry claim, a missing typed
  conclusion register — are named at §5.10 and left unbuilt.

### 0.5 How section references read

A bare `§x.y` is a section of **`museum-framework.md`**. A reference to this
document is written **"§x.y of this document"**. `experience-object-model.md` is
named in full or written **EOM §x.y**. Constitution references are written
`constitution §x` or `Step n`.

---

## 1. What is already specified, and what is missing

### 1.1 Already settled, and not restated here

Museum framework §9 fixes what PROVE IT is for: the product expression of
constitution §2's requirement that the record stay capable of contradicting
*"MelaKeela's own pages, the owner's preferred hypothesis, and your own previous
answer"*. It fixes six stages (§9.2), six rules (§9.3) and the correction route
(§9.4). EOM §9 gives it an object — the Challenge, `mk:chl:` — with a field
table, the grounding rule that a Challenge grounds on its evidence set and not on
its target (§9.4), the Challenge/run distinction (§9.5), and six things a
Challenge may never be (§9.8).

None of that is re-specified. This document takes all of it as given.

### 1.2 The three gaps

**Gap 1 — the run sequence is specified twice, differently.** Framework §9.2
gives six stages ending on the falsifier. Constitution Step 14 gives seven
headings ending on WHAT WOULD CHANGE IT with the institution's interpretation
sixth. The sequence this document is asked to specify has nine and puts the
institution's reading eighth. Three orderings, one mode. §2 reconciles them.

**Gap 2 — there is no object between the register and the Challenge.** EOM
§9.3's `evidence_set[]`, `rivals[]`, `absences[]`, `falsifiers[]`,
`exclusion_notes[]`, `bias_tests_shown[]` and `institution_position` are seven
fields on the Challenge. Assembling them is most of the work of building a run,
and every one of them is the same assembly for every Challenge on the same
bounded question. Under the present specification a second Challenge on the
ninety-nine forts re-assembles all seven by hand, with no record that it is the
same selection, and no way to see that the two selections have drifted apart.
§3 and §4 supply the missing object.

**Gap 3 — nothing constrains the conclusions.** EOM §9.3 gives five
`outcome_forms` — `agree`, `disagree`, `undecided`, `insufficient-evidence`,
`question-is-malformed`. Those are the visitor's positions *on the target claim*.
They say nothing about which **readings of the past** the interface may put in
front of a visitor, and a run whose evidence cannot reach a conclusion may still
offer it. That is the failure EOM §9.8 item 2 names — *"a Challenge whose evidence
set omits the evidence that bears against the claim has been curated into an
argument"* — in its mirror form: a Challenge whose *options* exceed its evidence
has been curated into a poll. §4.4 to §4.6 close it.

---

## 2. The nine-stage sequence

### 2.1 The stages

```
1 CLAIM  →  2 WHAT WAS FOUND  →  3 WHY THIS READING  →  4 COMPLICATION
→  5 UNKNOWN  →  6 WHAT WOULD CHANGE IT  →  7 YOU DECIDE
→  8 MELAKEELA'S READING  →  9 WHY WE MAY DISAGREE
```

Each stage is an Activity (`mk:act:`, EOM §8) with exactly one
`interaction_pattern`, so EOM §8.2's answer postures and §5.2's Constraint Block
apply without restatement. The Challenge holds them in `activities[]` in this
order and the order is fixed.

| # | Stage | `interaction_pattern` | `has_right_answer` | `recorded_output` |
|---|---|---|---|---|
| 1 | CLAIM | `READ` | true — `record-property` (the claim id, revision and status) | `nothing` |
| 2 | WHAT WAS FOUND | `SEARCH` | true — `record-property` (a count with its corpus and method) | `observation` |
| 3 | WHY THIS READING | `WEIGH` | **false** | `note` |
| 4 | COMPLICATION | `WEIGH` | **false** | `note` |
| 5 | UNKNOWN | `TYPE-THE-ABSENCE` | **false** | `observation` |
| 6 | WHAT WOULD CHANGE IT | `READ` | true — `record-property` (the Falsifier record and its `blocked_by`) | `nothing` |
| 7 | YOU DECIDE | `DECIDE` | **false** | `decision` |
| 8 | MELAKEELA'S READING | `READ` | true — `record-property` (the institution's claim set and its statuses) | `nothing` |
| 9 | WHY WE MAY DISAGREE | `READ` | true — `record-property` (the two Bias Test records) | `note` |

The five stages that ask the visitor to think — 3, 4, 5, 7 and the note at 9 —
all carry `has_right_answer = false`. The four that carry `true` are true about
the record, never about the past: what a register row says, what a search
returns, what a falsifier names, what the institution holds. EOM §8.2's rule
does the work: *"an Activity may not require a visitor to be right about
something the institution has not verified."*

### 2.2 Mapping to the two sequences already specified

| This document | Framework §9.2 | Constitution Step 14 |
|---|---|---|
| 1 CLAIM | 1 the proposition | QUESTION |
| 2 WHAT WAS FOUND | 3 the evidence | WHAT IS OBSERVED |
| 3 WHY THIS READING | 2 the rivals · 4 the gates | WHAT THE EVIDENCE SUPPORTS |
| 4 COMPLICATION | 2 the rivals that survive | WHAT COMPLICATES IT |
| 5 UNKNOWN | 5 the absences | WHAT REMAINS UNKNOWN |
| 6 WHAT WOULD CHANGE IT | 6 the falsifier | WHAT WOULD CHANGE IT |
| 7 YOU DECIDE | — | — |
| 8 MELAKEELA'S READING | §9.3 disclosure rule | MELAKEELA'S CURRENT INTERPRETATION |
| 9 WHY WE MAY DISAGREE | §9.3 bias-test rule | — |

**Three differences, stated rather than smoothed over.**

**D-1. The falsifiers move from last to sixth.** Step 14 ends public copy on
WHAT WOULD CHANGE IT. A run cannot: the visitor decides at stage 7, and a
falsifier they meet at stage 9 is a falsifier that could not inform the decision.
The reordering is not cosmetic and it is not a licence to reorder Step 14 for
static copy — an Exhibit keeps Step 14's order (EOM §7.4, *"the order is fixed"*).
A run is not an Exhibit.

**D-2. Two stages are new.** YOU DECIDE and WHY WE MAY DISAGREE have no
counterpart in either sequence. YOU DECIDE is where §4.4's conclusion set is
exercised; it is the stage this document exists to specify. WHY WE MAY DISAGREE
promotes framework §9.3's bias-test rule from a rule about what must be *visible
somewhere in a run* to a stage with its own screen, because a bias-test surface a
visitor can miss is a bias-test surface that was not shown.

**D-3. The rivals and the gates have no stage of their own.** Framework §9.2
gives each one. Here they are distributed into stages 3, 4 and 7. That is the
sequence's one real hazard, and §2.3 is its mitigation.

### 2.3 Stage 3 is plural, or the sequence is broken

**WHY THIS READING is not MelaKeela's reading.** Read at face value the title
says otherwise, and a run built on the face-value reading discloses the
institution's position at stage 3 and violates framework §9.3's *"the
institution's own position is disclosed, and disclosed last"* five stages before
stage 8 gets there.

The rule that prevents it:

> **Stage 3 states the inferential step from measurement to reading for
> *every* rival in the packet, each on its strongest evidence, and names
> none of them as the institution's.** Framework §9.2's stage 2 — *"every
> viable explanation, plus the null explanation, independently stated"* — and
> stage 4 — the five gates, *"each applied by the visitor, with the data needed
> to apply it present on the surface"* — are both discharged here. A stage 3
> that argues one reading has become an argument, and the run is a defence
> (EOM §9.8 item 2).

This is constitution Step 8 as an interface rule: *"Reconstruct each eligible
hypothesis on its strongest evidence before comparing it with rivals."* It is
also why the visitor meets the full rival set at stage 3 and merely **selects**
at stage 7. A rival first seen on the decision screen has been introduced too
late to be weighed.

Weight follows evidence and reachability does not, per EOM §9.7's resolution of
`IC-X-001`: every rival, the null included, is one interaction away at stage 3;
extent, prominence and finish follow the evidence. A `HYPOTHESIS` rival rendered
with the finish of a `VERIFIED` one has made a claim nobody wrote.

### 2.4 What the sequence does not change

- **No score, no points, no streak, no "correct", no completion state.**
  `reward_mechanic = none` on all nine Activities, per EOM §5.2, framework §9.3
  and §10.4.4. This holds at every age band and is not relaxed for adults.
- **No tally.** EOM §9.8 item 3: aggregating visitor outcomes into a displayed
  count would make agreement a measurement. Triage counts are published in
  aggregate for the *correction pipeline* (framework §9.4) and never as a
  running score on the run itself.
- **No affirmation.** A visitor whose conclusion matches the institution's is
  told nothing at stage 8 that a visitor whose conclusion differs is not told.
  Stage 8 renders the same claim set, the same statuses and the same confidence
  inputs either way. Congratulation is a score with the number removed.
- **Free text is private.** `output_is_private = true` on stages 3, 4, 5, 7 and
  9, at every band (EOM §8.3). A run is local by default (EOM §9.5).

---

## 3. The Evidence Packet — why a new object

### 3.1 The argument

A packet is a **named, versioned, statused selection over the evidence layer,
bound to one bounded question, carrying the conclusions that selection can and
cannot support.**

Four reasons it is an object and not a convenience.

**P-1. A selection is an assertion, and EOM §9.4 already says so.** *"A Challenge
that displays four of a claim's nine Evidence Links has made a selection, and a
selection is an assertion — ... Giving the selection its own records gives it a
status, a revision history, and something a challenger can contest."* EOM applies
that to a single Challenge's links. The same argument applied one level up gives
the packet: a *reusable* selection is a *reused* assertion, and reusing an
assertion without a record of it is how a curated argument propagates silently
across a dozen surfaces.

**P-2. The status floor is a property of the selection, not of any claim in it.**
Constitution Step 4: *"One class cannot borrow certainty from another."* The
product form is narrower and sharper — a **surface cannot borrow certainty from
its strongest row**. Twenty-eight `VERIFIED` measurements and one `HYPOTHESIS`
assumption underneath them make a packet whose floor is `HYPOTHESIS`, and there
is no honest way for any conclusion resting on that assumption to be offered
above it. The floor is computable only over a defined set, so the set must be an
object.

**P-3. Reuse is the normal case and the dangerous one.** The ninety-nine forts
work already supports an adult Challenge, a proposed atlas entry, a children's
investigation, an Exhibit and a comparison surface. Five hand-assembled selections
of the same evidence will diverge, and the divergence will be invisible because
nothing records that they were meant to be the same.

**P-4. A conclusion set needs somewhere to live.** It is not a property of the
Challenge — two Challenges on the same question must offer the same conclusions
or one of them is steering. It is not a property of a claim. It is a property of
the selection, which is the packet.

### 3.2 Identity

`mk:pkt:<key>`, allocated under museum framework §2.1's scheme without
modification: opaque 10-character key, never reused, never deleted,
revision-addressable as `mk:pkt:<key>@r<n>`, externally resolvable at
`<institution-domain>/id/pkt/<key>`. EOM §3.1 allocated six new codes under the
same scheme and the same argument applies: §2.1 is a scheme, and this is an
allocation under it.

**The packet's label is not its identifier.** The worked case at §5 is referred
to throughout as *the ninety-nine packet*; that is a `label`, it will be wrong
the moment the case is understood better, and framework §2.1 exists so that being
wrong about a label costs nothing.

**Three declarations the allocation obliges, stated here rather than left to be
inferred.**

1. **A packet is never a grounding target.** EOM §2.1 enumerates what a Grounding
   Link may resolve to, and `pkt` is deliberately **not** added to that list. A
   packet is neither an evidence object nor an experience object: it is a
   *selection over* the evidence layer, and grounding an experience object on a
   selection rather than on the evidence would put a curatorial act where a
   record should be. §4.8's generated links point at the evidence-layer objects
   the packet names, never at the packet.
2. **A packet carries no Constraint Block.** EOM §5.2 binds the block on *"every
   object in §6 to §13 without exception"* — eight experience objects, each with
   an interaction. A packet has none. Its `conclusion_set[]` statements are
   surfaced by objects that do carry a block, and the block governs them there.
   This is a scope statement, not an exemption, and it is written down because an
   object that quietly sits outside that block is how a prohibition stops
   binding.
3. **Two new closed vocabularies** are added and must join EOM §3.1's published
   list: `why_absent` (6 values, §4.5) and Withheld Conclusion `provenance`
   (3 values, §4.5). EOM §3.1 already records that framework §5.3's enumeration
   list *"is incomplete until these are added to it"*; this adds two more.

### 3.3 What a packet is not

1. **Not a cache.** A packet does not copy claim text, status or locators. It
   holds pinned references. A claim's status is read from the register at render
   time and the pin tells the visitor which revision the packet was built
   against.
2. **Not a subject folder.** A packet is bound to one bounded question with
   Step 1's fields filled. "The Rigvedic forts" is not a bounded question and
   cannot have a packet.
3. **Not a publication.** A packet with no Challenge, Exhibit or Activity using
   it shows nobody anything. `CLAUDE.md`: *"Evidence that supports nothing is not
   collected."*
4. **Not a place to put an argument.** Every field is a reference or a derived
   value. The one prose field, `derivation_note` on a conclusion, states the
   inferential step and cites the rows it steps between; a `derivation_note` that
   introduces a proposition not in `rests_on[]` is a Rule S-4 violation.

---

## 4. The Evidence Packet — specification

### 4.1 Header and scope

| Field | Type | Notes |
|---|---|---|
| `id` | identifier | `mk:pkt:<key>` |
| `revision` | integer | append-only, framework §3.6 |
| `label` | string | short human name; not an identifier, and expected to become wrong |
| `bounded_question` | `mk:qst:` | exactly one |
| `scope_block` | Block | constitution Step 1's fields, below |
| `built_by`, `built_date` | metadata | |
| `packet_reviewer`, `packet_review_date` | metadata | a named person and a date. A packet is not self-certifying, for the same reason EOM §5.2's Constraint Block is not. |

`scope_block` carries Step 1 in full and no field may be empty:
`proposition` · `date_range` · `geography` · `evidence_classes_required` ·
`terms_requiring_original_language` · `viable_explanations[]` ·
`null_explanation`.

### 4.2 Contents

Every array holds pinned references. None holds prose.

| Field | Type | Rule |
|---|---|---|
| `claims[]` | array of `mk:clm:<key>@r<n>` | **Non-empty.** Every claim any conclusion, gate, complication or falsifier in this packet rests on. Pinned. |
| `evidence[]` | array of `mk:evd:` | what the visitor can open in the primary-source viewer (§7.1), each with locator, edition, retrieval date and `independence_group` |
| `independence_groups[]` | array | the genealogy keys present, and the tree over them (§3.5). `independence_tree_shown` is `true` on every Challenge using the packet — EOM §9.3 already fixes this. |
| `dependency_findings[]` | array of `dependency_id` | rows from `02-SOURCES/dependency.csv` that cap or collapse the independence count. **Non-empty or explicitly `none-found` with the audit that looked.** |
| `absences[]` | array of `mk:abs:` | with `absence_type`. §3.7's rule travels with them: only `ABSENT DESPITE ADEQUATE SEARCH` may function as evidence against a proposition. |
| `holds[]` | array of `05-HOLDS/` paths | **`hold_disclosure` is required and non-null on every Challenge using a packet with a non-empty `holds[]`** (framework §9.3). |
| `translation_blocks[]` | array | framework §3.8, complete or the packet is invalid, for every consequential ancient word the conclusions turn on |
| `falsifiers[]` | array of Falsifier records | with `direction`, `currently_testable`, `blocked_by` |
| `bias_tests[]` | array of Bias Test records | **both types, or the packet is invalid** (§3.11). Plus the asymmetry statement (§11.2), which is itself a `mk:clm:` and must be in `claims[]`. |
| `gates[]` | array of Gate Results | chronological · geographical · mechanism · positive-evidence · diagnostic, each with the data needed to apply it |
| `rivals[]` | array of `mk:clm:` | every viable explanation **plus the null explanation** |
| `exclusion_notes[]` | array of Gate Results | rivals gated out, with the gate they failed, at §3.10's fixed small footprint |
| `conclusion_set[]` | array of Conclusion Options | §4.4 |
| `withheld_conclusions[]` | array of Withheld Conclusions | §4.5. **Non-empty**, or the explicit value `none-foreseeable` carrying the review record that looked. |
| `institution_position` | array of `mk:clm:` | disclosed at stage 8 only |
| `target_is_preferred_position` | bool | editorially set and logged, so framework §11.6 rule 5's split can be computed |
| `used_by[]` | array | `mk:chl:`, `mk:exh:`, `mk:act:` using this packet at this revision |

### 4.3 Status floor and status census

Two derived fields, both computed, neither asserted.

| Field | Derivation |
|---|---|
| `status_floor` | the **lowest** status among `claims[]`, on the ordering `VERIFIED` > `PROVISIONAL` > `HYPOTHESIS` > `INHERITED-UNVERIFIED`. `HOLD`, `REJECTED` and `SUPERSEDED` are not points on this ordering — see below. |
| `status_census` | the count of `claims[]` at each status |

**Both are displayed, and the census never replaces the floor.** A packet of
twenty-eight `VERIFIED` rows and one `HYPOTHESIS` has a floor of `HYPOTHESIS`,
and showing only the census would let a surface present that packet as
overwhelmingly verified while a conclusion rests on the one assumption underneath
it. Showing only the floor would be the opposite error — it would present
twenty-eight measurements as a hypothesis. The census makes the shape visible;
the floor makes the ceiling enforceable.

**Three statuses are not ordinal and are handled separately.**

- A `HOLD` claim in `claims[]` triggers `hold_disclosure` and does not set the
  floor: a hold is a statement about source access, not about the claim's
  standing.
- A `REJECTED` claim may be in `claims[]` — rejected reasoning stays visible so
  it is not re-proposed (`CLAUDE.md`) — and it may appear in `withheld_conclusions[]`
  as the reason a conclusion is refused. It may never appear in `rests_on[]` of a
  Conclusion Option.
- A `SUPERSEDED` claim in `claims[]` is a build defect. The packet fails
  validation and names the claim that replaced it.

### 4.4 Conclusion Options — what may be offered

A Conclusion Option is a conclusion **about the past** that the interface offers a
visitor at stage 7. It is not an `outcome_form`; §4.7 relates the two.

| Field | Notes |
|---|---|
| `option_id` | |
| `statement` | the exact words shown. Not a paraphrase of them, and not a label for them. |
| `rests_on[]` | Pinned `mk:clm:` references, each of which is in `claims[]`. **Non-empty unless `no_positive_support` is true.** |
| `derivation_note` | the inferential step from those rows to this statement, in one or two sentences, introducing no proposition not in `rests_on[]`. **Where the step runs through a pinned row's `what_it_does_not_establish` or `evidence_against` field rather than its proposition, the note names the field** — a claim's caveat is not the claim, and a derivation that silently reads one as the other has cited a row for something the row denies. |
| `annotated_against[]` | claims in `claims[]` that bear **against** this option and are rendered with it. Distinct from `rests_on[]` and **excluded from `offer_ceiling`**: evidence against a conclusion is not evidence the conclusion rests on, and letting it into the ceiling computation would make a well-refuted option look well-founded. |
| `annotation_status` | derived: the lowest status among `annotated_against[]`. This is the figure W-R1 tests. |
| `no_positive_support` | bool. **True where the packet holds no claim supporting this option** — an eligible rival that nothing in this evidence base positively supports. Displayed on the option's face, in those words. `rests_on[]` is then empty and `offer_ceiling` is `HYPOTHESIS` by definition: a proposal is not a finding. Constitution Step 7 gates hypotheses on positive evidence, and this field is where a rival that fails that gate but survives the others is offered honestly rather than either hidden or dressed up. |
| `offer_ceiling` | derived: the **lowest** status among `rests_on[]`, or `HYPOTHESIS` where `no_positive_support` is true. Displayed with the option. |
| `is_null_explanation` | bool. **Exactly one option in `conclusion_set[]` carries it.** Framework §9.2 stage 2 and §8.5 both require the null explanation to be present; a packet whose null is missing, or whose null restates one of its named rivals, has four rivals wearing five hats. §7 records the instance of that in this document's own draft. |
| `bridges_crossed[]` | every §4.4 bridge the statement crosses — language, ancestry, culture, artifact, religion, polity, modern identity. **Each must itself be a claim in `claims[]`.** A conclusion that crosses an unwritten bridge is not offered; it is withheld under `bridge-not-established`. |
| `implies_outcome` | the `outcome_form` this option would ordinarily imply, shown as a changeable default and never inferred silently (§4.7) |
| `counter_to_institution` | bool. Feeds framework §11.6 rule 5's tracking. |

**The three admission tests.** An option is offered only if all three pass.

1. **Derivation.** `rests_on[]` is non-empty, every member is in `claims[]`, and
   the `derivation_note` steps only between them.
2. **Bridges.** Every bridge the statement crosses is a written claim
   (constitution Step 10: *"Every link among language, ancestry, culture,
   artifact, religion, polity and modern identity is a separate claim"*).
3. **Ceiling.** `offer_ceiling` is computed and displayed. It does **not** gate
   admission — a `HYPOTHESIS`-ceilinged option is offerable and must be, or the
   mode only ever offers what the institution has already established. What the
   ceiling gates is the *finish*: extent, prominence and rendering follow it,
   per EOM §9.7 and framework §12.3 V-8.

**A Conclusion Option's `statement` is not asserted in the institution's voice.**
EOM §9.8 item 6 confines what a Challenge asserts to `targets`, `rivals[]`,
`evidence_set[]` and `institution_position`, and a `statement` is on none of
those four. It is a proposition *offered for the visitor to hold*, rendered as
such, and it resolves to `rests_on[]` — or, where `no_positive_support` is true,
to the explicit statement that nothing in the packet supports it. **This is an
extension of EOM §9.8 item 6 and is declared as one**: the item's list needs a
fifth member, `conclusion_set[]` and `withheld_conclusions[]` statements, or
every offered conclusion is a prohibited assertion. The prohibition's substance
is untouched — a statement that resolves to none of the five is still forbidden,
which is what admission test 1 enforces.

**`unknown` is never an option** (§3.7). "The evidence does not settle it" is an
`outcome_form` the visitor may reach and is offered as such at §4.7; it is not a
rival explanation and never sits in `conclusion_set[]` beside named readings.

### 4.5 Withheld Conclusions — what must be refused, and shown to be refused

| Field | Notes |
|---|---|
| `withheld_id` | |
| `statement` | **The conclusion in full, in the words a visitor would use.** Not softened, not paraphrased into something easier to refuse, not reduced to a category name. A withheld conclusion the visitor cannot recognise as the thing they were about to think has not been disclosed. |
| `why_absent` | enum, below |
| `what_would_admit_it` | the specific claim, retrieval or gate result that would move this into `conclusion_set[]`. **Required.** Not "more evidence". |
| `reason_rests_on[]` | the **statused** objects the refusal rests on — claims, absences, holds, gate results — pinned |
| `reason_supported_by[]` | unstatused records that corroborate the refusal: bias-failure rows, re-audit rows, dependency rows, scope statements. **Displayed, and excluded from `reason_status`.** A refusal that reached a status by counting an audit row has computed a number over things that have none. |
| `reason_status` | derived: the lowest status among `reason_rests_on[]`. **Displayed.** |
| `provenance` | `editorial` · `from-a-rival-gated-out` · `from-a-declined-challenge` |

`why_absent` ∈

| Value | Meaning |
|---|---|
| `no-claim-of-required-kind` | the packet holds no claim of the kind the conclusion needs — a geography, a date, a material |
| `bridge-not-established` | the conclusion crosses a §4.4 bridge that is not a written claim |
| `gate-failed` | a rival failed a Step 7 gate; the Exclusion Note carries the gate and its data |
| `absence-not-of-usable-type` | the conclusion argues from a silence typed as something other than `ABSENT DESPITE ADEQUATE SEARCH` (§3.7) |
| `source-blocked-hold` | the evidence that would decide it is in `05-HOLDS/` |
| `outside-packet-scope` | the conclusion is about a question this packet is not bound to; names the question it belongs to |

**The four rules that keep this honest.**

**W-R1. Withholding on a weak reason is forbidden.** Wherever `reason_status` is
computed — that is, wherever `reason_rests_on[]` is non-empty — and it falls
below the institution's `accepted_threshold` (D-010), the conclusion is **not
withheld**. It moves into `conclusion_set[]` with the reason attached in
`annotated_against[]` and rendered against it. Refusing a conclusion is the
strongest thing this interface does, and doing it on something the institution
has not itself verified is the mode's characteristic failure in the direction
nobody watches. §6.2 records the instance of this caught in drafting this
document.

**W-R1 is not confined to `gate-failed`, and an earlier draft of it was.** That
draft carved out the other five values as *"statements about what the packet
contains, not judgements about the past"*. The carve-out was wrong twice. It is
false on its face — §5.8's W-1, W-2 and W-5 compute `reason_status =
PROVISIONAL` precisely because those refusals rest on contestable readings — and
it is gameable, which is worse: the exact conclusion §6.2 caught could be
re-withheld by relabelling its `why_absent` as `no-claim-of-required-kind` on
identically sub-threshold reasoning, and the rule would never fire. A rule a
designer escapes by choosing a different enum value is not a rule. Corrected on
adversarial review; logged with §6.2 as part of `BF-025`.

A refusal with an **empty** `reason_rests_on[]` — `outside-packet-scope`, and
`no-claim-of-required-kind` where the packet simply holds nothing of the kind —
has no `reason_status` and W-R1 does not apply. Those are facts about the
packet's contents and are checkable by looking.

**W-R2. The withheld set is never behind a fold.** It renders at stage 7 with the
offered options, at §3.10's fixed small footprint. Not collapsed by default, not
on a second screen, not in a tooltip. §3.10's Exclusion Note component is the
form; concealment is what the component exists to prevent.

**W-R3. The set grows from real attempts.** `provenance = from-a-declined-challenge`
is how a conclusion a visitor actually tried to reach, and that the correction
pipeline declined with a reason, enters the display for the next visitor. A
withheld set that is only ever `editorial` is a list of the conclusions the
designers happened to imagine, which is not the same list as the conclusions
visitors reach. This is the one place where framework §9.4's triage output feeds
back into the run rather than only into the register.

**W-R4. The withheld set is non-empty.** Or it carries the explicit value
`none-foreseeable` with the review record that searched, on the model of EOM
§7.4's `none-found` for WHAT COMPLICATES IT. A packet with nothing withheld has
either found a corner of the record where every foreseeable conclusion is
supported — possible, and to be stated as such — or has not looked.

### 4.5.1 What the mechanism does not reach

Rule S-5 is **not** fully enforceable from the fields specified, and a mechanism
oversold is worse than one honestly bounded (EOM §8.4 makes the same move for
COMPARE). Four residues, stated so they are reviewed rather than assumed
automated:

1. **`bridges_crossed[]` is a judgement, not a resolution.** Deciding what a
   statement asserts — and therefore which of framework §4.4's seven bridges it
   crosses — is a reading. The field is designer-populated and a validator can
   check only that each named bridge is a written claim, never that the set is
   complete. A conclusion that crosses an unnoticed bridge passes admission
   test 2. This is the same limit EOM §8.4 records for *"an archaeological
   culture used as a stand-in for a population"*, and it has the same remedy:
   a named reviewer, not a check.
2. **"In the words a visitor would use" has no test.** A withheld conclusion can
   be defused by phrasing — stated so narrowly, or so technically, that the
   visitor about to reach it does not recognise it as theirs. The rule is real
   and the enforcement is a reviewer reading the six statements and asking
   whether they are the six things people actually say.
3. **§3.10's footprint is advisory.** W-R2 requires the withheld set at the
   Exclusion Note's *"fixed small footprint"*, and framework §3.10 declares that
   proportionality is *"deliberately advisory, not enforced"*. So "not behind a
   fold" is checkable and "at the right weight" is not.
4. **Selection completeness is unfalsifiable from inside the packet.** Nothing in
   the schema can show that a claim bearing against the target was left out of
   `claims[]` — EOM §9.8 item 2's failure. Only a reader with the registers can.
   W-R3's `from-a-declined-challenge` provenance is the partial remedy, and it is
   partial because it works only after the omission has cost somebody something.

**One tension declared rather than resolved.** W-R1 moves a `gate-failed`
conclusion into `conclusion_set[]` with the gate result standing, and framework
§3.10 says an Exclusion Note *"cannot be expanded into an exhibit without the
gate result being overturned first."* W-R2 also applies the Exclusion Note
component to refusals that are not gated-out hypotheses at all. Both are
extensions of §3.10's scope; neither is smuggled. Logged as `IC-X-002` in
`04-AUDITS/INTERNAL-CONTRADICTIONS.csv`, with the reading this document works
under stated there: §3.10 governs a *gated-out hypothesis given an exhibit*, and
a conclusion offered to a visitor with its gate rendered against it is neither an
exhibit nor an unqualified offer. Whether that is what §3.10 intended is the
framework author's to say.

### 4.6 The choice this document makes, and states

Rule S-2 requires that a choice the owner has not made is recorded, not taken.
**This is not one of those**, and the distinction matters: whether a conclusion
set is constrained at all is a specification question, not an owner question, and
this document answers it.

It is answered **yes, with disclosure**, over two alternatives that were real:

- *Unconstrained, with the evidence shown.* Offer any conclusion; trust the
  visitor. Rejected: an interface that offers "the ninety-nine forts were
  Harappan cities" beside "the counts are formulaic" has asserted that its
  evidence bears on the first, which it does not. Offering a conclusion is a
  claim that the packet can carry it.
- *Constrained silently.* Offer only what the evidence supports and say nothing
  about the rest. Rejected: it is indistinguishable from curation, it cannot be
  audited, and it teaches the visitor that the institution's list is the world.

Two costs of the answer taken, both stated rather than absorbed. §6.1: a listed
option is one click and the free-text escape is work, so the constrained set has
a thumb on the scale in favour of readings the institution has already written
down. §4.5.1: the constraint is enforceable in part and reviewed in part, and
the reviewed part is where a determined designer would get around it.

### 4.7 The visitor's own conclusion, and the escape

Two records come out of stage 7 and they are different things.

1. **A conclusion** — a selection from `conclusion_set[]`, or free text under
   **"None of these — say what you conclude"**.
2. **An `outcome_form`** on the target claim — `agree` · `disagree` ·
   `undecided` · `insufficient-evidence` · `question-is-malformed` (EOM §9.3).

The option's `implies_outcome` is shown as a **default the visitor may change,
with the derivation visible**. It is never inferred silently: agreeing with a
conclusion the institution also holds, for reasons the institution does not
hold, is not agreement with the claim, and an interface that records it as
agreement has made a measurement out of a coincidence.

**The escape is not a lesser option.** It renders at the same visual weight as
the listed options, in the same list, not beneath it. This is the control on
§6.1's finding and it is a hard requirement: **the constraint governs what the
interface asserts is concludable; it never governs what the visitor may
conclude.** A visitor who reaches a conclusion the packet cannot carry has done
one of two things — found a gap in the packet, or made an inference the record
does not support — and both are worth having. The first is a correction; the
second is what stage 7's free text is private for.

Free text at stage 7 is `output_is_private = true`, local, deleted with the run
unless the visitor explicitly submits it (EOM §9.5). Submission creates a
`mk:cor:` with `channel = PROVE IT run` (framework §9.4, EOM §9.6), subject to
**D-024**.

### 4.8 Reuse

The requirement the packet exists for.

- **A packet is reusable by any surface whose bounded question is the packet's,
  or a narrowing of it.** Never a widening. The conclusion set and the withheld
  set were derived for a scope; a wider question changes what "the evidence
  cannot support" means and needs its own packet.
- **Reuse is recorded** in `used_by[]`, so a change to the packet has a list of
  the surfaces it touches.
- **Every Challenge still emits its own `puts-in-evidence` records.** EOM §9.4 is
  not relaxed *mechanically*: those links carry the Challenge as subject and are
  what the Challenge grounds on. They are **generated from the packet** and each
  carries `packet_id` and `packet_revision`.
- **But EOM §9.4's substantive rule is narrowed, and the narrowing is declared.**
  EOM §9.4's reason for new records is that *"a Challenge chooses what it
  shows … a selection is an assertion"*. Under reuse the Challenge becomes the
  subject of records asserting a selection the **packet** made. What survives is
  that the selection has a status, a revision history and something a challenger
  can contest — which was the point. What changes is authorship: the packet
  **authored** the selection, the surface **adopted** it, and the generated link
  records both, so a challenger can contest the packet's selection once rather
  than each surface's copy of it separately. A surface that wants to assert its
  own selection does not reuse a packet; it builds one.
- **A surface may narrow `evidence_set[]`, and must show what it dropped.** The
  same rule as `conclusion_set[]` below, and for a sharper reason: `status_floor`
  travels with the packet, so a surface showing a subset would otherwise carry a
  floor computed over rows the visitor never saw. Where the subset's own floor
  differs from the packet's, **both are displayed**, labelled.
- **A surface may narrow a packet's `conclusion_set[]`** — a children's
  investigation will — and must record which options it dropped and why. It may
  **never narrow `withheld_conclusions[]`**, because narrowing that set is
  exactly concealment.
- **Reuse never re-derives status.** `status_floor` travels. A second surface
  does not get a better floor by showing fewer rows.
- **Two packets on one surface must pin the same revision of any claim they
  share.** Two revisions of one claim rendered side by side is a defect.

### 4.9 Decay

`decay_behaviour` on the grounding links (EOM §4.3) governs, with three packet-level
rules on top:

- **A claim in `claims[]` revises** → the packet does not silently re-point. The
  pins hold, the surfaces using it show that a newer revision exists and how it
  differs (§2.1), and the packet is queued for editorial re-issue. A conclusion
  whose `offer_ceiling` would change is flagged in that queue.
- **A claim in `claims[]` is rejected** → every Conclusion Option resting on it
  is withdrawn from `conclusion_set[]` and appears in `withheld_conclusions[]`
  with `why_absent` naming the rejection. The run stays resolvable and shows that
  the institution came to agree with the visitors who disagreed — EOM §9.7's
  rule, and the last outcome to hide.
- **A source in the packet enters `05-HOLDS/`** → `hold_disclosure` becomes
  required and the packet cannot render without it.

---

## 5. The worked case: did Indra's poets destroy ninety-nine forts?

Everything below is a design instance. Rule S-3: no packet exists, nothing here
promotes anything, and three prerequisites at §5.10 mean this packet could not be
built today even though its research is done.

### 5.1 Header

| Field | Value |
|---|---|
| `id` | `mk:pkt:<key>` — opaque, per §3.2. Referred to here as **the ninety-nine packet**, which is a label. |
| `label` | Ninety-nine forts |
| `bounded_question` | `mk:qst:<key>` — *Did Indra's poets destroy ninety-nine forts?* |
| `target_is_preferred_position` | **true** — the target claim is MelaKeela's own deflationary reading, and framework §11.6 rule 5 requires challenges against the institution's preferred position to be tracked separately |
| `status_floor` | **`HYPOTHESIS`** — §5.3 |

`scope_block`:

| Field | Value |
|---|---|
| `proposition` | The Rigveda records the destruction of ninety-nine forts. |
| `date_range` | **Composition:** undated in absolute terms in this packet. **Relative order of composition:** Arnold's five periods, which is itself `HYPOTHESIS` (`PUR-028`). **Publication** — a different date type, per Step 2 and framework §2.7, and not evidence about the text's age: Grassmann 1876–7 (`SRC-074`), Griffith 1890 (`SRC-073`), Arnold 1905 (`SRC-026`), Geldner 1951 (`SRC-072`), Renou (`SRC-076`), Elizarenkova 1989–99 (`SRC-075`). **Annotation and digitisation:** Zürich layer (`SRC-022`), VedaWeb clone at `d3eb8af` (`SRC-069`), retrieved 2026-09-07. |
| `geography` | **None.** The pinned corpus carries no geographic content (`PUR4J-018`). This is a scope statement, not an omission, and it is why §5.8's W-3 exists. |
| `evidence_classes_required` | textual; linguistic; historiographical. **Not** material, epigraphic, genetic or environmental — none is in this packet, and no conclusion may reach for one. |
| `terms_requiring_original_language` | `púr-`; `navatí-`; `náva`; `śatá-`; `śatatamá-`; `ā́yasa-`; `aśmanmáya-`; `dāsá-`/`dāsī́-`. Translation Blocks required for each (§3.8) — see §5.10 prerequisite 3. |
| `viable_explanations[]` | (a) formula — the counts are stock quantities (`PUR4J-I-01`); (b) enumeration — the counts preserve a remembered figure the tradition rounded (`PUR4J-007`, `PUR4J-010`); (c) both — a conventional count attached to remembered fighting (`PUR4J-026` with `PUR4J-I-01`'s `what_it_does_not_establish`); (d) late layer — the counting passages are a late accretion (`PUR-026` bears against). |
| `null_explanation` | No account of the number's provenance is required. Six passages state ninety-nine and nine state one hundred; nothing beyond the text saying so is needed to explain that they do. The null asserts nothing about whether the number is stock or remembered, and it is offered as **C-1**. |

**Bounding the question is the first thing the packet does to it.** The question
as asked has four parts and the packet bears on one and a half:

| Part of the question | Does the packet bear on it? |
|---|---|
| *ninety-nine* | **Yes.** Six passages state it; it is not the modal count. |
| *forts* | **Partly.** The word is `púr-`, an earthwork in the corpus's own lexicon; the corpus does not describe one kind of object. |
| *destroy* | **Partly.** The verbs are in the text. Whether anything was destroyed is not in this packet. |
| *Indra's poets* | **No.** No claim in this packet bears on any human agent, and there is no route from this packet to one. That in the text it is Indra who breaks the forts is read off the `addressee` and `samhita_text` columns of `rigveda-pur-passages.csv` — **evidence, not a claim**: no register row asserts the grammatical agent of the six passages. That gap is itself a prerequisite (§5.10). |

That fourth row is what makes `question-is-malformed` a live outcome at §5.7,
and it is stated at stage 1, before any evidence, because a visitor who does not
know what the question conflates cannot weigh the answer.

### 5.2 Stage 1 — CLAIM

**Target:** `PUR4J-I-02@r<n>` — *"The prominence of ninety-nine in modern
citation of the Rigvedic forts is a fact about reception, not a property of the
corpus."* Status **`PROVISIONAL`**. Exactly one target, revision-pinned
(EOM §9.3).

The target is the institution's own reading, and the deflationary one. It was
chosen over `PUR4J-002` (a `VERIFIED` count, which nobody needs a run to test)
and over `PUR4J-I-01` (the formula reading, which §5.5 shows has already failed
once in this institution's favour) because framework §9.1 sets the bar at *"the
institution is wrong here"* and the only way to clear it is to put at risk a
claim the institution would mind losing.

### 5.3 Every claim the packet draws on, and the floor

`claims[]`, in full. Forty-three rows.

**`VERIFIED` — 28 rows**

| claim_id | What it contributes |
|---|---|
| `PUR-003` | the simplex `púr-` lemma at 83 tokens; surface breakdown incl. `púraḥ` 45 ACC.PL |
| `PUR-004` | six further `púr-` lemmas: `puraṃdara-` 11, `pūrbhíd-` 8, `pūrbhidya-` 1, `pūrpati-` 1, `purohán-` 1, `púrya-` 1 |
| `PUR-005` | the family totals: 106 tokens, 104 pādas, 103 stanzas, 86 hymns |
| `PUR-011` | what Arnold's stratum letters mean — A Archaic, S Strophic, N Normal, C Cretic, P Popular — verified against Arnold's own text |
| `PUR-013` | the strata layer is Arnold 1905, single-sourced |
| `PUR-014` | family by stratum: A 31, S 32, N 17, C 23, P 3 |
| `PUR-016` | the corpus baseline by stratum |
| `PUR-017` | the Popular deficit: 3 observed against 14.8 expected |
| `PUR-018` | χ² 14.57, 4 df, p = 0.0057 at the hymn unit |
| `PUR-022` | the collocation profile: `navatí-` 33.5×, `śámbara-` 41.5×, `ā́yasa-` 36.9×, `dāsī́-` 43.0× |
| `PUR4J-001` | 21 of 103 passages state a count; **82 state none** |
| `PUR4J-002` | 100 in 9 · **99 in 6** · 7 in 4 · 90 in 2 |
| `PUR4J-003` | ninety-nine is **not** the modal count; one hundred is, 9 to 6 |
| `PUR4J-004` | ninety-nine is never a single numeral: `náva` + `navatí-` |
| `PUR4J-005` | `navatí-` is a feminine singular collective governing a plural in 5 of 6 |
| `PUR4J-006` | the identical expression counts ninety-nine **rivers** at RV 10.104.8 |
| `PUR4J-008` | two of the six append "the hundredth", on a dwelling word |
| `PUR4J-009` | every count is 7, 90, 99 or 100 — no irregular figure in 21 passages |
| `PUR4J-011` | the ninety-nine set is 4 of 6 Strophic; the seven-fort set 3 of 4 Archaic |
| `PUR4J-012` | 10 of 103 passages state a material: `ā́yasa-` 8, `aśmanmáya-` 1 (RV 4.30.20), `ámā-` 1 |
| `PUR4J-016` | Geldner's per-hymn heading names a poet for 55 of 103 passages and a deity, metre or collection for 48 |
| `PUR4J-018` | §4J's geography field cannot be filled from the pinned corpus |
| `PUR4J-020` | `púr-` is 67.5% accusative and 3.6% locative across 83 simplex tokens |
| `PUR4J-021` | Grassmann defines `púr-` as *Wall aus Steinen und Lehm, Verschanzung, Palisade* |
| `PUR4J-022` | no translator renders `púr-` "city" but once in 103 passages |
| `PUR4J-023` | Griffith renders `ā́yasa-` "iron" in all eight passages, Geldner "ehern" in all eight |
| `PUR4J-028` | `síndhu-` is the only lemma in the 103 passages that can name a river, and it is ambiguous |
| `PUR4J-030` | 22 passages carry a patron-side name and 22 an opponent-side name, on Grassmann's classification of the **name** |

**`PROVISIONAL` — 13 rows**

| claim_id | What it contributes |
|---|---|
| `PUR-026` | the `púr-` vocabulary is not a late accretion |
| `PUR4J-007` | Śámbara's forts: 99 in three passages, 100 in two |
| `PUR4J-010` | the counts sort by narrative cycle, not by opponent alone |
| `PUR4J-013` | only one of eight metal forts is a stormed adversary's stronghold |
| `PUR4J-014` | the stone fort (RV 4.30.20) is an enemy's; the unbaked one is a refuge |
| `PUR4J-024` | three of §4J's five types cannot be assigned from the text |
| `PUR4J-025` | 48 textual stronghold · 47 poetic formula · 3 both · 5 unclassifiable |
| `PUR4J-026` | **all six ninety-nine passages are textual strongholds** |
| `PUR4J-027` | 8 of the 10 material passages are not plain textual strongholds |
| `PUR4J-032` | `śatábhuji-` "hundredfold" agrees with the fort word and is **not** a count |
| `PUR4J-I-01` | the formula reading |
| `PUR4J-I-02` | **the target** — the salience of 99 is reception |
| `PUR4J-I-03` | the corpus does not describe a single kind of object |

**`HYPOTHESIS` — 2 rows**

| claim_id | What it contributes |
|---|---|
| `PUR-028` | **Arnold's five periods correspond to real chronological stages of composition.** Every stratum statement in the packet rests on it. |
| `PUR-027` | `púr-` is a fortification the composers attack rather than inhabit — see §6.3, its status is stale |

`status_census`: **`VERIFIED` 28 · `PROVISIONAL` 13 · `HYPOTHESIS` 2 ·
`INHERITED-UNVERIFIED` 0 · `HOLD` 0 · `REJECTED` 0 · `SUPERSEDED` 0.**

> **`status_floor` = `HYPOTHESIS`.**

Set by `PUR-028`, and it cannot be avoided by dropping the row: every stratum
statement in `PUR-014`, `PUR-016`, `PUR-017`, `PUR-018`, `PUR-026` and
`PUR4J-011` depends on Arnold's periodisation being chronological, Arnold himself
called his period names *provisional* (1905 §§60–61), and the claim has been
contested since. Dropping `PUR-028` from `claims[]` would raise the floor to
`PROVISIONAL` by concealing the assumption — which is the reason §4.2 requires
`claims[]` to hold *"every claim any conclusion, gate, complication or falsifier
in this packet rests on"* and not merely the ones a surface intends to cite.

The census is the other half of the reading: 28 of 43 rows are verified
measurements over a pinned corpus, and a surface that showed only the floor would
misrepresent that as badly as a surface that showed only the census would
misrepresent the assumption.

**Also in the packet, resolving to something other than a claim id:**
`PUR-N-002`, `-003`, `-012`, `-013`, `-020`, `-021`, `-022`, `-024`, `-032`,
`-033`, `-034`, `-036`, `-037`, `-043`, `-044` (adjudicated count rows, evidence);
`PUR-P-007`, `-041` and the other passage rows (evidence);
`DEP-001`, `DEP-021`, `DEP-022`, `DEP-023`, `DEP-024` (dependency findings);
`HOLD-006` (hold); `BF-013`, `BF-014` (bias tests); `RA-014`, `RA-015`
(re-audit queue); `D-045` (owner decision, `OPEN`).

### 5.4 Stage 2 — WHAT WAS FOUND

`interaction_pattern = SEARCH`. Right answers permitted, and only on record
properties: a count with its corpus and its method.

**The corpus.** 106 tokens of seven `púr-`-derived lemmas, in 104 pādas, 103
stanzas, 86 hymns, over a pinned clone of the VedaWeb Rigveda at commit
`d3eb8af` (`PUR-003`, `PUR-004`, `PUR-005`).

**The counts.** Of the 103 passages, **21 state a count of the fort word and 82
state none** (`PUR4J-001`). Among the 21: one hundred in 9, ninety-nine in 6,
seven in 4, ninety in 2 (`PUR4J-002`). **Ninety-nine is not the most frequent
count. One hundred is, by nine passages to six** (`PUR4J-003`).

**The six ninety-nine passages**, with the expression, the stratum and the
addressee, from `rigveda-pur-counts.csv` and `rigveda-pur-passages.csv`:

| Stanza | Expression | Arnold stratum | Addressee | Typology |
|---|---|---|---|---|
| RV 1.54.6 | `púro navatíṁ … náva` | Cretic | Indra | textual stronghold |
| RV 2.19.6 | `navatíṁ ca náva … púraḥ śámbarasya` | Archaic | Indra | textual stronghold |
| RV 4.26.3 | `náva … navatī́ḥ śámbarasya` + `śatatamáṁ veśyàm` | Strophic | Indra | textual stronghold |
| RV 7.19.5 | `náva yát púro navatíṁ ca` + `nivéśane śatatamā́` | Strophic | Indra | textual stronghold |
| RV 7.99.5 | `náva púro navatíṁ ca śámbarasya` | Strophic | Indra and Viṣṇu | textual stronghold |
| RV 8.93.2 | `náva yó navatím púro bibhéda` | Strophic | Indra | textual stronghold |

**Ninety-nine is never a single word.** It is `náva` "nine" plus `navatí-`
"ninety", joined by `ca` in three passages and split around other words in four
(`PUR4J-004`). `navatí-` is a feminine **singular** collective governing a plural
`púraḥ` in five of the six; only RV 4.26.3 has the agreeing plural `navatī́ḥ`
(`PUR4J-005`).

**One token can carry many forts.** `púr-` is 67.5% accusative across its 83
simplex tokens and 3.6% locative — three tokens in the whole corpus put anyone
*inside* one (`PUR4J-020`). `púraḥ` is accusative plural in 45 of 83
(`PUR-003`). So a single word in a single pāda denotes ninety-nine forts, and no
count of *tokens* can ever be a count of *forts*.

**A stone fort.** RV 4.30.20: `śatám aśmanmáyīnām purā́m índro vy āā̀syat /
dívodāsāya dāśúṣe` — Indra overthrew a hundred stone forts for Divodāsa. It is
one of only ten passages in 103 that state a material at all, and the only one
with `aśmanmáya-` "of stone" (`PUR4J-012`, `PUR4J-014`). **It states a hundred,
not ninety-nine** (`PUR-N-024`) — which is a fact about the record, and is where
this stage stops. What follows from it is stage 3's and stage 4's business.

**What is not a count.** `śatábhuji-` "hundredfold" agrees in full case, gender and
number with the fort word at RV 7.15.14 and RV 1.166.8 and is **not** adjudicated a
fort count (`PUR4J-032`). The instrument that identifies counts is agreement plus
proximity plus translator reading, and it is overridden by hand where the
instrument is wrong by construction — which it is on `navatí-`, a feminine
singular collective that can never agree in number with the plural it governs, so
a number-agreement test under-reports it by construction and drops five of the
six ninety-nine passages. Six rows in the counts register are adjudicated
**against** the instruments, each naming on the row what it overrides. Three of
those six sit in ninety-nine passages — RV 2.19.6, 4.26.3 and 7.19.5 — and of
the three only `PUR-N-012` at RV 2.19.6 carries the value 99; the other two are
the "hundredth" rows of `PUR4J-008`.

**And the count the corpus does not produce.** No sub-count of the register
returns 99: 106 tokens, 104 pādas, 103 stanzas, 86 hymns, 83 simplex tokens, 82
simplex stanzas, 70 simplex hymns, 102 excluding book 9, 78 string hits, 48
padapāṭha resolutions, 156 admitting `púraṃdhi-`, 107 admitting `purāṣáh-`. The
nearest are 103 and 104 (`06-BRIEFS/rv01-reconciliation.md` §2.4). A full-text
scan of every tracked file finds no corpus operation anywhere in this repository
that yields 99 (`rv01-reconciliation.md` §§2.5–2.6).
That absence is typed **`ABSENT DESPITE ADEQUATE SEARCH`** — and under §3.7 it is
the *only* absence in this packet that may function as evidence against a
proposition.

### 5.5 Stage 3 — WHY THIS READING

Plural, per §2.3. Four readings, each on its strongest evidence, none named as
the institution's, plus the independence tree.

**Reading (a) — formula.** `PUR4J-I-01`, `PROVISIONAL`. Four diagnostic
predictions for an enumeration reading. The row's enumerated results are
**(1) inconclusive, (2) fails, (3) fails, (4) fails**; the row's own summary
sentence says *"two fail decisively, one holds, and one is INCONCLUSIVE"*, and
its `evidence_against` and `notes` say "two" and "three" respectively of the same
quantity. The row is internally inconsistent and this run shows the enumerated
results, which are the derivable part, and logs the inconsistency as `IC-P-004`
(§6.6). The enumeration reading **fails** that an enumeration should not migrate to another class
of object: `náva navatí-` counts ninety-nine *rivers* at RV 10.104.8, in a stanza
that also carries `pūrbhíd-` (`PUR4J-006`). It **fails** that an enumeration
should not be systematically completed by a round number: two of the six append
"the hundredth" (`PUR4J-008`), so 99 functions as one-short-of-a-hundred. It
**fails** that an enumeration should occasionally produce an irregular figure:
every count in 21 passages, ten books and every Arnold stratum is 7, 90, 99 or 100
(`PUR4J-009`).

**Reading (b) — enumeration.** `PUR4J-007` and `PUR4J-010`, both `PROVISIONAL`.
The counts are not free ornament: they **sort by narrative cycle**. All four
seven-fort passages carry Purukutsa or the Puru, near-verbatim at RV 1.174.2b and
6.20.10c; ninety-nine and one hundred go with Divodāsa, Atithigva and Śámbara.
Ornament should not sort by story. And Śámbara's own forts are 99 three times and
100 twice — nearly stable, and compatible with an enumeration that rounds.

**Reading (c) — both.** `PUR4J-026`, `PROVISIONAL`: all six ninety-nine passages
are **textual strongholds** — the text presents a fort as an object in its own
narrative world. The formulaic character of the *count* does not make the
*passage* formulaic. `PUR4J-I-01`'s own `what_it_does_not_establish` says the
same from the other side: *"A formulaic count can be attached to a real siege."*

**Reading (d) — late layer.** The reading that the counting passages are a late
accretion. The stratum evidence runs **against** it: the family is
over-represented in Archaic (31 against 21.8 expected) and under-represented in
Popular (3 against 14.8), χ² 14.57 on 4 df, p = 0.0057 at the conservative hymn
unit (`PUR-014`, `PUR-016`, `PUR-017`, `PUR-018`, `PUR-026`); the ninety-nine set
is 4 of 6 Strophic and 1 Archaic (`PUR4J-011`). **All of which rests on
`PUR-028`, which is `HYPOTHESIS`** — see §5.8, where this is why reading (d) is
offered rather than withheld.

**The null.** Nothing about any event need be posited.

**The independence tree**, rendered — framework §9.2 stage 3 calls this *"the
single most instructive thing this mode can teach"*, and this case teaches more
than was expected of it.

The tree is drawn over the **fourteen distinct `source_id` values on the 43 rows
of `claims[]`** — SRC-019, 020, 021, 022, 023, 024, 026, 069, 070, 072, 073,
074, 075, 076. (It is not a tree of the counting register, which carries seven:
SRC-020, 021, 022, 069, 072, 073, 074.)

```
14 source ids over 43 claim rows
└── one clone, VedaWeb @ d3eb8af   (SRC-019 = SRC-069, and SRC-085 elsewhere; DEP-024)
    ├── Aufrecht Saṃhitā (SRC-020)
    ├── padapāṭha (SRC-021)              — partially independent of SRC-022 (DEP-003)
    ├── Zürich morphology (SRC-022)      — glosses taken from Grassmann's Wörterbuch
    ├── strata.json (SRC-023) ── a transcription of Arnold 1905 (DEP-001) ──┐
    ├── TEI header (SRC-024)                                               │
    ├── addressees.json (SRC-070)  — Geldner's arrangement, three removes   │
    └── translations                                                       │
        ├── Griffith 1890  (SRC-073)   independent                         │
        ├── Geldner 1951   (SRC-072)   independent                         │
        ├── Renou          (SRC-076)   independent; NO dependency row exists│
        ├── Grassmann 1876-7 (SRC-074) ── same author as the Wörterbuch ────┤
        └── Elizarenkova   (SRC-075)   made with Geldner in view (DEP-023)  │
                                                                           │
  Arnold 1905 = SRC-026 ────────────────────────────────────────────────────┘
  ... and Grassmann's Wörterbuch is ALSO cited as SRC-026. See below.
  stanza_properties' 'arnold' column is Arnold 1897 — same man (DEP-022, BF-013)
```

**The tree cannot be finished, and that is the finding.** `SRC-026` in
`02-SOURCES/access-ledger.csv` is *"E. V. Arnold, Vedic Metre in its Historical
Development, Cambridge University Press 1905"*. The family register uses it that
way (`PUR-011`, `PUR-026`). But the §4J register cites `SRC-026` for **Grassmann's
Wörterbuch** in six gloss claims — `PUR4J-012`, `-013`, `-014`, `-021`, `-028`,
`-030` — and `DEP-021`, the row whose whole purpose is stopping Grassmann being
counted twice, is written `source_a = SRC-074, source_b = SRC-026` with the text
*"Grassmann 1876-7 translation and Grassmann Woerterbuch zum Rig-Veda are the
same author."* **One source id, two different works, and no ledger row for
Grassmann's Wörterbuch at all** — against `CLAUDE.md`'s requirement that
*"`source_id` must resolve to a row in the access ledger."* Found while drawing
this packet's tree; logged as `IC-P-003` and queued as `RA-023` (§6.5). Until it
is resolved, `PUR4J-021` — a `rests_on[]` member of W-2 — cites a source id that
resolves to the wrong book, and the packet cannot state whether its lexical
claim and its entire chronological layer are one source or two.

Read plainly, with that caveat: **fourteen source ids, one repository, four
independent translating voices** (Griffith, Geldner, Grassmann, Renou) with
Elizarenkova a dependent fifth, **one metrical periodisation, one lexicon which
is also one of the four translators, one unresolvable id collision, and no
non-European scholarly source anywhere.** Sāyaṇa's commentary — the indigenous
exegetical tradition, and the one Griffith leaned on — is not in the pinned
corpus and was not reachable (`RA-015`, `HIGH`, blocked on egress). No dependency
row covers Renou in either direction.

`PUR-013` is what makes the strata branch legible: it records that VedaWeb
attributes `strata.json` to Arnold 1905 outright, so every claim resting on it is
dependent, not corroborated. Where a count row reads "3/4 translators" that is
Griffith, Geldner and Grassmann; where it reads "1/4", Griffith alone.

**The five gates, with the data to apply them.** Framework §9.2 stage 4 requires
each gate applied by the visitor with its data on the surface; `gates[]` is the
field. Applied here to reading (b), enumeration, as the rival that most needs
gating:

| Gate | Data on the surface | Result |
|---|---|---|
| Chronological | Arnold strata: the ninety-nine set is 4 of 6 Strophic, 1 Archaic, 1 Cretic (`PUR4J-011`); the family runs Archaic 31 against 21.8 expected (`PUR-014`, `PUR-016`, `PUR-017`) | **PASSES at `HYPOTHESIS`** — the whole instrument rests on `PUR-028` |
| Geographical | none. The pinned corpus carries no geographic content (`PUR4J-018`) | **CANNOT BE APPLIED.** Not a pass and not a fail; the packet has no data. |
| Mechanism | none. No claim in the packet describes how a remembered count would reach a hymn | **CANNOT BE APPLIED** |
| Positive evidence | the counts sort by narrative cycle (`PUR4J-010`); Śámbara's forts are 99 three times and 100 twice (`PUR4J-007`) | **PASSES at `PROVISIONAL`** |
| Diagnostic predictions | `PUR4J-I-01`'s four, enumerated results (1) inconclusive (2) fails (3) fails (4) fails | **FAILS at `PROVISIONAL`** |

Two of five cannot be applied at all, and the interface says *cannot be applied*
rather than leaving a blank a visitor will read as a pass. Applied to reading
(d), the late-layer reading, the chronological gate **fails** — and it fails at
`HYPOTHESIS`, which is why W-R1 sends (d) to `conclusion_set[]` as C-6 rather
than to the withheld set. §6.2.

### 5.6 Stage 4 — COMPLICATION · Stage 5 — UNKNOWN · Stage 6 — WHAT WOULD CHANGE IT

**Stage 4 — COMPLICATION.**

1. **The counts sort by story** (`PUR4J-010`). The single strongest thing against
   the formula reading, and it is in the packet at the same weight as the
   diagnostics that support it.
2. **The institution has already got this wrong, in its own favour.**
   `PUR4J-007` as first written was `VERIFIED` and was the strongest of the four
   diagnostics behind the formula reading. Three of its five parts were false and
   **all three errors ran toward the deflationary conclusion**. It was caught by
   an independent reviewer, not by the unit's own adversarial test, which had
   interrogated the conclusion instead of re-deriving the evidence. Logged as
   `BF-014`. The formula reading now stands on two clear diagnostics of four, and
   its strongest one is gone.
3. **The passages are not formulaic even where the count is** (`PUR4J-026`).
4. **The expression is genuinely marked.** `PUR4J-I-02`'s own `evidence_against`:
   one hundred is the ordinary Vedic "very many"; `náva navatí-` is distinctive,
   and Griffith's *"nine-and-ninety castles"* is the likely path into English.
   The salience of 99 may be a property of the expression rather than of the
   count — which is not the same as being a fact about reception alone.
5. **The corpus does not describe one kind of object** (`PUR4J-I-03`). Nearly half
   the 103 passages are figurative; 48 present a fort as a narrative object.
6. **The material passages are the least ordinary ones.** Eight of the ten
   passages stating a material are not plain textual strongholds on the hand
   classification, and four are not on the rules alone (`PUR4J-027`); only one
   of the eight metal forts is a named adversary's stormed stronghold
   (`PUR4J-013`). So the stone fort at RV 4.30.20 is not a typical case that
   happens to state its material — the material passages are a peculiar set,
   and it is one of the two that read as an enemy's.
7. **A stale figure inside the target's own row.** `PUR4J-I-02`'s
   `evidence_for` reads *"6 passages against 8 for one hundred"* and cites
   `PUR4J-003`, which reads **9**. Found while building this packet; logged as
   `IC-P-002` (§6.4). It does not change the direction of the target claim — the
   margin is wider at 9 than at 8 — and it is shown because a run that hid a
   defect in its own target claim would be the defence EOM §9.8 item 2 forbids.

**Stage 5 — UNKNOWN.** Typed absences, and the type is the whole content:

| Absence | Type | Consequence |
|---|---|---|
| No corpus operation anywhere yields 99 | **`ABSENT DESPITE ADEQUATE SEARCH`** | The only one that may function as evidence. The search was a full-text scan of every tracked file in a repository small enough for it to be exhaustive. |
| Poet lineage for **4** of the 6 passages | `NOT PRODUCED` | Geldner's headings name a deity rather than a poet at RV 2.19.6, 4.26.3, 7.19.5 and 7.99.5; he names one at RV 1.54.6 ("hymns of Savya") and RV 8.93.2 ("hymns of Śrutakakṣa and others"). Across the whole corpus a poet is named for 55 of 103 (`PUR4J-016`). An arrangement's silence is not anonymity, and the two that *are* named are Geldner's 1951 arrangement following the Anukramaṇī tradition, three removes from composition. Blocked: **`HOLD-006`**. |
| Any geography | `NOT PRODUCED` | The pinned corpus carries none (`PUR4J-018`). |
| Material in 93 of 103 passages | `NOT PRODUCED` | A hymn praising a fort's breaking had no occasion to say what it was built of (`PUR4J-012`). |
| What metal `ā́yasa-` names | `NOT RECOGNISED` | Griffith "iron" ×8, Geldner "ehern" ×8, neither arguing the point (`PUR4J-023`). An open crux, not a gap. |
| Any non-European scholarship | `NOT ACCESSIBLE` | `RA-015`, blocked on egress. An archival asymmetry, not a fact about what exists. |

**One thing that is *not* an absence, moved out of this stage on review.**
§4J's archaeological-fortification, inferred-geography and unsupported-identification
types are recorded `NOT ASSIGNED` in `rigveda-pur-typology.csv`. `NOT ASSIGNED`
is not one of framework §3.7's eight `absence_type` values and must not be typed
as one — stage 5's `interaction_pattern` is `TYPE-THE-ABSENCE`, so putting it
here would ask a visitor to apply an enum that has no value for it. It is a
**scope statement**: `PUR4J-024` records that these three are *"verdicts on an
argument someone else must make first"*, so they sit in `scope_block` and in
`exclusion_notes[]`, not in `absences[]`.

**The hold disclosure**, required because `holds[]` is non-empty (§4.2,
framework §9.3). Shown before stage 3, in the institution's voice: *"One thing
this run asks you to weigh is bounded by a source we could not reach. An
Anukramaṇī or any per-hymn poet attribution independent of Geldner would test
whether the six ninety-nine passages share a lineage — which is one of the
falsifiers below, and the one that would most strengthen the formula reading.
`SRC-080` to `SRC-083` (GRETIL, archive.org, TITUS, fallbacks) all returned
`EGRESS_BLOCKED` on 2026-09-07. `HOLD-006`."*

**Stage 6 — WHAT WOULD CHANGE IT.**

| Falsifier | Direction | Testable? |
|---|---|---|
| A passage stating an irregular count (23, 41) — breaks `PUR4J-009` | would-weaken formula | **Yes**, and cheap: the corpus is pinned |
| `náva navatí-` at RV 10.104.8 shown to be an editorial intrusion | would-weaken formula | Yes, on the manuscript tradition |
| The six passages shown to share one poet lineage | would-strengthen formula | **No** — blocked by `HOLD-006` |
| A pre-Griffith English source giving the number | would-weaken `PUR4J-I-02`'s transmission path | Yes; not attempted |
| A document deriving MelaKeela's 99 from a corpus operation | **would-reject** `rv01-reconciliation` §2.6 and `PUR4J-I-02` | Yes, inside this repository |
| An archaeological or geographic argument tied to a named passage | would move `PUR4J-024`'s three unassigned types | No source retrieved; bounded by the research hold on identifying the forts with one archaeological culture |
| Sāyaṇa, or any Indian-language scholarship on these passages | would test rather than supplement | **No** — `RA-015`, egress-blocked |

Three of seven are currently blocked, and the interface says so rather than
listing seven falsifiers as though they were equally available.

### 5.7 Stage 7 — YOU DECIDE: what is offered

Seven options. `offer_ceiling` is the lowest status among `rests_on[]` and is
shown beside each. Nothing here is scored; nothing is preferred by position.

| # | Statement shown | `rests_on[]` | Ceiling | `implies_outcome` |
|---|---|---|---|---|
| **C-1** | "The Rigveda states ninety-nine forts in six passages, and one hundred in nine. Ninety-nine is not the number it gives most often. Nothing further about where the number came from is needed to explain that." — **the null explanation**, `is_null_explanation = true` | `PUR4J-001`, `PUR4J-002`, `PUR4J-003`, `PUR4J-004` | `VERIFIED` | `undecided` |
| **C-2** | "The counts are formulaic. Ninety-nine is a stock quantity of the poetic tradition, not a remembered number." | `PUR4J-I-01`, `PUR4J-006`, `PUR4J-008`, `PUR4J-009` | `PROVISIONAL` | `agree` |
| **C-3** | "The counts may preserve something enumerated that the tradition rounded. They sort by story, and ornament should not." | `PUR4J-007`, `PUR4J-010` | `PROVISIONAL` | `disagree` |
| **C-4** | "Both: a conventional number attached to fighting the tradition remembered. The passages are narrative even where the count is formulaic." | `PUR4J-026`, `PUR4J-025`, and `PUR4J-I-01` **through its `what_it_does_not_establish` field** — *"A formulaic count can be attached to a real siege"* — named in the derivation note, because that field is the row's caveat and not its proposition | `PROVISIONAL` | `disagree` |
| **C-5** | "Ninety-nine is prominent today because `náva navatí-` is a striking phrase and Griffith rendered it strikingly — a fact about the expression, not only about reception." | `PUR4J-004`, and `PUR4J-I-02` **through its `evidence_against` field**, named in the derivation note: this option is built from the target row's own qualification of itself | `PROVISIONAL` | `disagree` |
| **C-6** | "The counting passages are a late layer in the Rigveda." | **empty — `no_positive_support = true`**, shown on the option's face: *nothing in this packet supports this.* `annotated_against[]` = `PUR-014`, `PUR-016`, `PUR-017`, `PUR-018`, `PUR-026`, `PUR4J-011`; `annotation_status` = **`HYPOTHESIS`** via `PUR-028` | **`HYPOTHESIS`** | `disagree` |
| **C-7** | "The question is malformed: nothing in this evidence bears on any human agent, and nearly half the fort passages are figurative." | `PUR4J-020`, `PUR4J-025`, `PUR4J-024` | `PROVISIONAL` | `question-is-malformed` |

Plus, at the same visual weight and in the same list (§4.7):

- **"The evidence does not settle it."** — `outcome_form = insufficient-evidence`.
  Not a rival explanation, and never rendered as one; `unknown` is never a rival
  (§3.7).
- **"I have not decided."** — `outcome_form = undecided`, reachable without
  selecting any conclusion. EOM §9.3 requires all five outcome forms to be
  first-class, and a run in which `undecided` is unreachable has quietly made
  deciding compulsory.
- **"None of these — say what you conclude."** — free text, private, local,
  submitted only by an explicit act.

**C-6 is the one to look at, and it is the one that reshaped the schema.** It is
offered because W-R1 forbids refusing it: the reason to refuse — that the `púr-`
vocabulary is over-represented in the earliest stratum — is a chronological gate
result resting on `PUR-028`, which the institution has not verified. But it
cannot be *derived* either: the packet holds no claim supporting lateness, and an
earlier draft listed the stratum rows as its `rests_on[]`, which would have had
the option deriving itself from the evidence that refutes it and taking an
`offer_ceiling` from rows that argue the opposite. That is why §4.4 now separates
`annotated_against[]` from `rests_on[]` and adds `no_positive_support`. C-6 is
offered with an empty `rests_on[]`, the words *nothing in this packet supports
this* on its face, and the stratum evidence rendered against it at
`HYPOTHESIS`. §6.2.

### 5.8 Stage 7 — YOU DECIDE: what is refused, and why

Six, rendered inline at §3.10's fixed small footprint, never folded (W-R2).

| # | Statement, in the words a visitor would use | `why_absent` | `what_would_admit_it` | `reason_rests_on[]` (statused) · `reason_supported_by[]` (not) | Reason status |
|---|---|---|---|---|---|
| **W-1** | "Ninety-nine forts were destroyed." | `bridge-not-established` | A claim tying any one of the six passages to a destruction event — a stratigraphic horizon, a datable burning, a named place. No such claim exists in this packet, and the packet's `evidence_classes_required` does not include material evidence. | `PUR4J-024` · *supported by:* `scope_block.evidence_classes_required`, which does not include material evidence | `PROVISIONAL` |
| **W-2** | "The ninety-nine forts were Harappan cities." | `bridge-not-established` | Three separate claims, none held: a geography, an archaeological identification, and a chronological bridge between the corpus and Indus urbanism. The corpus's own lexicon calls a `púr-` a wall of stones and clay, and one translator in 103 passages renders it "city", once. | `PUR4J-021`, `PUR4J-022`, `PUR4J-018`, `PUR4J-024` | `PROVISIONAL` |
| **W-3** | "The ninety-nine forts were in [any place]." | `no-claim-of-required-kind` | Any geographic claim at all. The packet has none: the pinned corpus carries no geographic content, and `síndhu-` — the one lemma that can name a river — is read differently by Griffith and Geldner across the six passages where it occurs. | `PUR4J-018`, `PUR4J-028` | `VERIFIED` |
| **W-4** | "The forts belonged to the Dāsas, so the Dāsas were a people who lived in forts" — **and its mirror, "the forts were the composers' own and the named enemies held none."** Both directions, refused on the same ground and in the same row. | `bridge-not-established` | A claim attaching a named group to a fort **by the syntax of a passage**, not by sharing a stanza with it. `dāsī́-` co-occurs in family stanzas at 43× its corpus rate, and that is a co-occurrence statistic; the 22 opponent-side names are Grassmann's classification of the *name*, not a reading of any passage's grammar. `BF-014` is the logged instance of this exact inference being made in this repository and being wrong. | `PUR-022`, `PUR4J-030` · *supported by:* `BF-014`, `RA-014` | `VERIFIED` |
| **W-5** | "No fort in the Rigveda was ever a real fortification." | `absence-not-of-usable-type` | An absence typed `ABSENT DESPITE ADEQUATE SEARCH`. The silences here are `NOT PRODUCED` — 93 of 103 passages state no material because a hymn about breaking a fort had no occasion to. Forty-eight passages present a fort as an object with a named holder, a stated material in two cases, and a gate. | `PUR4J-012`, `PUR4J-025`, `PUR4J-I-03` | `PROVISIONAL` |
| **W-6** | "Ninety-nine is the number the Rigveda gives for the forts." | `gate-failed` — positive evidence | Nothing would; it is measured false. One hundred is stated in nine passages and ninety-nine in six, and 82 of the 103 fort passages state no count at all. | `PUR4J-002`, `PUR4J-003`, `PUR4J-001` | **`VERIFIED`** |

**W-6 is the test of whether any of this is real.** MelaKeela's live `the-forts`
page is headlined *"Ninety-nine forts, in Indus country, three centuries too
late"* (`INHERITED-UNVERIFIED`; no source recorded, rated `Medium` risk and
"Revise before release" by the curatorial audit); the inherited RV-01
specification is titled *"The 99 Forts Database"* (`INHERITED-UNVERIFIED` in
every part including its title); Version 12 carries the figure at five separate
lines (`INHERITED-UNVERIFIED`). None of the three is cited as evidence for
anything here — they are the thing being refused. The interface refuses the
conclusion its own institution publishes, states the measurement that refuses it,
and says that nothing would admit it. `D-045` — whether the site artefact keeps
the inherited name — stays `OPEN` and this changes nothing about it; the
withheld row is a statement about what the evidence supports, not a ruling on a
title.

**W-4 is the one that matters most,** and it is written in both directions on
purpose. It is the conclusion a visitor is most likely to reach unaided, it is
where the Aryan-invasion narrative and its mirror both enter, and its refusal
rests on a `VERIFIED` measurement — `PUR4J-030` records that the 22 opponent-side
names are *"Grassmann's classification of the NAME, not a reading of any
passage's syntax"* — plus `BF-014`, the logged instance of this institution
making that exact stanza-co-occurrence inference and being wrong.

**The correction-history check that `CLAUDE.md` requires, run and shown.**
Inherited correction `R-04` (`01-INHERITED/claude-project-handoff.md`) records
that *"every demon is somebody's local enemy"* was corrected for omitting the
direction, and `IH-020` in `03-REGISTERS/inherited-claims.csv` states that
direction: the composers are the incomers and the named enemies are *"the people
already there, holding forts."* W-4 must not re-suppress what that correction
restored. It does not, and the distinction is the point:

- W-4 refuses an **evidentiary route** — from a name sharing a stanza to a
  population that held forts — not a direction. Its `what_would_admit_it` names
  the syntax that would support the direction, and that syntax is retrievable
  from the pinned corpus.
- `IH-020` is `INHERITED-UNVERIFIED`, so under Rule S-1 it cannot ground a
  conclusion in either direction and is not in `claims[]`. Promotion needs the
  per-passage reading, not an argument.
- Writing only the first direction would have made the refusal look like a
  political correction of one narrative. Writing both makes it what it is: this
  packet cannot say who held the forts, and that is a statement about
  `rigveda-pur-fields.csv`'s `roles_basis` column, not about who did.

The Constraint Block backs the row independently but less absolutely than an
earlier draft claimed: EOM §5.2's `identity_attribution = none` means such a link
*"is a museum framework §4.4 bridge with its mechanism, its rivals and its
governance, **or** it is not displayed"* — it can be written down, with the
bridge; it cannot be written down as a property.

**Provenance of the six.** All six are `editorial` on a first build. W-R3 expects
that to change: the withheld set a packet ships with is the list of conclusions
its designers imagined, and the list of conclusions visitors actually reach is a
different list, which arrives through the correction pipeline.

### 5.9 Stage 8 — MELAKEELA'S READING · Stage 9 — WHY WE MAY DISAGREE

**Stage 8, disclosed only here.** MelaKeela currently holds `PUR4J-I-02` at
`PROVISIONAL`: the prominence of ninety-nine in modern citation is a fact about
reception, not a property of the corpus. Alongside it, `PUR4J-I-01` at
`PROVISIONAL`: the counts are formulaic. Both are shown with their status, their
`rests_on`, their `evidence_against` and — required, not optional —
`PUR4J-I-01`'s note that it lost its strongest diagnostic on review and that
`BF-014` records the failure.

The visitor is told nothing about their own conclusion here. No affirmation, no
comparison, no tally (§2.4).

**Stage 9, both tests, with the asymmetry statement.**

*Prestige-bias.* The live risk is preferring the measured corpus work because it
arrives with a commit hash, a χ² and German lexicography, and demoting the number
in the page headline because it arrives in a headline. Corrected in the register
itself: 99 is a `VERIFIED` count of six passages with locators, and it **outranks**
the 106-token family count on the question of how many forts a passage names.
What is demoted is only its claim to be *the* number, and that demotion is a
measurement (`PUR4J-003`). Four further instances were caught inside the research
unit — Grassmann nearly counted twice (`DEP-021`), Arnold nearly counted twice
(`DEP-022`, `BF-013`), the mechanical agreement test preferred over a reading it
gets wrong by construction on `navatí-`, and Geldner's standing as the reference
translation treated as correctness rather than reception.

*Preferred-counter-narrative.* The available soft landing is to declare 99
formulaic and be done — deflationary, flattering to a sceptical posture, costless
to assert. The unit named it in advance, built four controls, and **the test
still failed**: `BF-014`, three false parts of one claim, all three running toward
the deflationary conclusion, caught by an independent reviewer rather than by the
author's own pass. That failure is displayed at stage 4 and again here, because
it is the single best evidence a visitor has that this institution's preferred
direction is a real force on its output.

*The asymmetry statement* (§11.2) is required here and states, in the
institution's voice, that the two failure modes are symmetrical in form and
asymmetrical in power — the archives, the chairs, the journals and the syllabi
were not equally available to the positions in question. This packet's own
independence tree is a local instance of exactly that: one European philological
line, no Indian-language commentary, and Sāyaṇa unreachable (`RA-015`). **The
statement is itself a `mk:clm:` with sources, a status and falsifiers, not a
slogan — and no such claim exists in this repository yet.** See §5.10.

### 5.10 What this packet could not be built with today

**Nine prerequisites, not the three an earlier draft claimed.** Rule S-3 forbids
creating any of them here, and finding them is the point of building the case
rather than describing it — six of the nine were invisible until an adversarial
reviewer re-derived the packet against its own rules.

1. **An Absence record for the packet's only usable absence.** *"No corpus
   operation in this repository yields 99"* is typed `ABSENT DESPITE ADEQUATE
   SEARCH` and is the one silence in the packet that may do argumentative work
   (§3.7). It exists as a finding in `06-BRIEFS/rv01-reconciliation.md` §2.6 and
   has **no register row and no `mk:abs:` id**. Under §4.2 the packet cannot cite
   it. The absence needs to become a record.
2. **The asymmetry statement as a claim.** §11.2 requires it to be a `mk:clm:`
   with sources, a status and falsifiers. There is none. Without it, stage 9
   cannot render, and a bias-test surface with the two tests and no asymmetry
   statement is the false-balance failure §3.11 exists to prevent.
3. **Translation Blocks** (§3.8) for all eight terms `scope_block` names —
   `púr-`, `navatí-`, `náva`, `śatá-`, `śatatamá-`, `ā́yasa-`, `aśmanmáya-`,
   `dāsá-`/`dāsī́-` — each complete in all eleven fields. **Two of the eight are
   on the constitution's own list of English categories to audit**: *fort*, and
   *slave* for `dāsá-`, which is the term W-4 — the case's most consequential
   refusal — turns on. `06-BRIEFS/pur-translation-standard.md` is the nearest
   thing in hand and is not the block.
4. **A claim asserting the grammatical agent of the six passages.** C-7 and
   §5.1's bounding table both turn on it being Indra who breaks the forts in the
   text, and that is currently read off an evidence column, not a claim row.
5. **Six further `mk:abs:` records.** §4.2 makes `absences[]` an array of
   `mk:abs:`; §5.6 has six typed absences beyond the one that does argumentative
   work, and none is a record.
6. **A prestige-bias Bias Test record for the underlying research unit.** §4.2:
   *"both types, or the packet is invalid."* `BF-013` is in the packet, and its
   own `bias_or_method_failure` reads *"Source-independence failure"* — it is not
   the prestige-bias test. That test exists as prose at
   `04-AUDITS/rigveda-pur-4j-method.md` §8.1 and prose is not a record. **As
   specified, this packet is invalid under its own rule until it is written.**
7. **Gate Results** as records for the five gates §5.5 tabulates.
8. **Falsifier records** to framework §3.9's six fields; §5.6 supplies the
   substance for seven and the field structure for none.
9. **An `mk:qst:` for `bounded_question`**, and the `mk:clm:@r<n>` pinning that
   `D-019` has not yet made resolvable.

The research for this case is finished to a standard most of this repository has
not reached. It is the **product-layer records** that are missing — and the count
went from three to nine on review, which is itself the finding: a specification
author counts the prerequisites he happened to notice.

---

## 6. What building the case did to the specification

Four findings, all from the instance and none from the type.

### 6.1 The offered set has a thumb on the scale — prestige bias, logged `BF-024`

A listed conclusion is one click; the free-text escape is work. So a constrained
set systematically favours the readings the institution has already written down,
which is prestige bias in its institutional form: privileging a claim because the
institution holds it, dressed as rigour.

It cannot be designed away — some conclusions must be listed or stage 7 is a
blank box — so it is controlled in three places rather than denied: the escape
renders at the same weight and in the same list, not beneath it (§4.7); the
withheld set is displayed inline and grows from declined challenges (W-R2, W-R3);
and `counter_to_institution` is a field, so it is visible how many of the offered
conclusions run against the institution. **That last control was first written as
supplying framework §11.6 rule 5's split, and it does not**: rule 5's split is
over *corrections* against the institution's preferred position, and EOM §9.6's
`target_is_preferred_position` already supplies it — §5.1 sets it true.
`counter_to_institution` measures a different and smaller thing, the composition
of the offered set. Corrected on review. Logged as `BF-024`.

### 6.2 Withholding on a weak reason — caught in drafting, logged `BF-025`

The first draft of §5.8 had **"the counting passages are a late layer"** in the
withheld set, `why_absent = gate-failed`, on the strength of the stratum
distribution. That would have used `PUR-028` — `HYPOTHESIS`, Arnold's own
periodisation, which Arnold called provisional and which has been contested since
— to **refuse a visitor a conclusion**.

Refusal is the strongest act this interface performs. Performing it on an
assumption the institution has not verified, in defence of the institution's own
measured result (`PUR-026`), is the institution being easier on itself, which is
the failure `CLAUDE.md`'s two tests exist to catch and which `BF-014` shows this
subject has already produced once.

Corrected by **W-R1** at §4.5, which is a general rule and not a patch on this
case: a gate result below the accepted threshold annotates a conclusion, it never
withholds one. The conclusion is now offered as **C-6** with a `HYPOTHESIS`
ceiling and the stratum evidence rendered against it. Logged as `BF-025`.

Both tests were run by the author of this document, and `BF-014`'s own
`future_control` warns that an author-run test tends to interrogate the
conclusion rather than re-derive the evidence. The re-derivation that found
§6.2 was of `PUR-028`'s status, not of the conclusion drawn from it — which is
the right direction, and is not a substitute for independent review.

### 6.3 `PUR-027`'s status is stale — queued `RA-022`

`PUR-027` ("the Rigvedic `púr-` is a fortification the composers attack rather
than inhabit") sits at `HYPOTHESIS` with the note *"testing it requires reading
each of the 106 passages for the grammatical role of `púr-`, which this unit did
not do."* The later §4J unit **did** read them: `PUR4J-020` measures 67.5%
accusative and 3.6% locative over the 83 simplex tokens, and the typology
register classifies all 103 passages.

Nothing is promoted here — only retrieval promotes, and this document retrieves
nothing. The row is queued as `RA-022` for re-derivation by a unit that can do
it. It stays in the packet at `HYPOTHESIS` and does not set the floor, because
`PUR-028` already does.

### 6.4 A stale figure inside the target claim — logged `IC-P-002`

`PUR4J-I-02`'s `evidence_for` reads *"6 passages against 8 for one hundred"* and
cites `PUR4J-003`, which reads **9**. `PUR4J-003` carries its own correction note
recording the change; the interpretation row was written against the
pre-correction figure and not updated with it. `IC-P-001` records the same stale
8 in `D-045`'s notes and flagged it to `RA-015`; this is a **second** location,
and it is inside the interpretation the run at §5 puts at risk.

Direction, stated because it matters: the correction widens the margin **in the
direction the row's own argument prefers**, from 8–6 to 9–6. Nothing is
overturned. Logged as `IC-P-002`, severity `LOW` for the argument and `HIGH` for
hygiene, action: update the row's `evidence_for` in a unit that can re-derive it.

### 6.5 One source id, two works — logged `IC-P-003`, queued `RA-023`

`SRC-026` resolves in `02-SOURCES/access-ledger.csv` to Arnold 1905, *Vedic Metre
in its Historical Development*. `03-REGISTERS/rigveda-pur-family.csv` uses it that
way. `03-REGISTERS/rigveda-pur-4j-claims.csv` uses the same id for **Grassmann's
Wörterbuch zum Rig-Veda** in six gloss claims, and `02-SOURCES/dependency.csv`
`DEP-021` — the row that exists to stop Grassmann being counted twice — is
written `source_a = SRC-074, source_b = SRC-026` and describes both as Grassmann.
There is no ledger row for the Wörterbuch anywhere.

`CLAUDE.md` requires that *"`source_id` must resolve to a row in the access
ledger"*, and this one resolves to the wrong book for six claims, one of which
(`PUR4J-021`) is a `rests_on[]` member of a withheld conclusion. The consequence
for the packet is direct: it cannot state whether its lexical claim and its
entire chronological layer are one source or two, so §5.5's independence tree is
drawn with the collision shown rather than resolved.

The finding is not that anyone reasoned wrongly — the 4J unit logged `DEP-021`
*before* using the translations, which is the control working. It is that the
control was recorded against an identifier that already meant something else.
Logged as `IC-P-003`, queued as `RA-023`. Nothing here re-attributes it: that
needs a ledger row and a re-derivation, and Rule S-3 forbids both.

**This is what the object was built to do.** An evidence packet's independence
tree is a forcing function: assembling one made a source-identity collision
visible that four registers, a dependency map and a method note had passed over.

### 6.6 The formula reading's diagnostics do not add up — logged `IC-P-004`

`PUR4J-I-01`'s `evidence_for` opens *"Two fail decisively, one holds, and one is
INCONCLUSIVE"* and then enumerates **(1) INCONCLUSIVE (2) FAILS (3) FAILS (4)
FAILS**. Its `evidence_against` says the support is *"two clear diagnostics of
four"*; its `notes` say *"diagnostics 2, 3 and 4 are unaffected"* — three.
`BF-014`'s `correction` field says two. Four statements of one quantity, giving
three different answers, inside the row that reading (a) rests on.

This is the `IC-P-002` class again and it is the second instance found while
assembling one packet. Direction, because it matters: understating the surviving
support **overstates the institution's self-criticism**, which is the flattering
error here and the one the preferred-counter-narrative test is least likely to
catch, since it looks like rigour. The first draft of §5.5 reproduced the summary
sentence and then printed three failures underneath it. Corrected to show the
enumerated results; logged as `IC-P-004`.

---

## 7. Adversarial tests on this document

**Prestige-bias challenge.** *Did this privilege a claim because it is canonical,
Sanskritic, Indo-European, European, institutionally prestigious, repeatedly
cited or nationally useful?*

Two findings. The first is `BF-024` at §6.1: the offered/free-text asymmetry
privileges the institution's own written readings, controlled at §4.7 and W-R2/3.
The second is about this document's choice of case. The ninety-nine forts is
the best-evidenced corner of this repository — 43 claim rows, a pinned corpus, an
adjudicated count register — and picking it makes the mechanism look easy. What
is genuinely untested: an `INHERITED-UNVERIFIED` `status_floor`, an almost-empty
`conclusion_set[]`, a `REJECTED` row inside `claims[]`, and a packet whose
`withheld_conclusions[]` outnumbers what it can offer. `hold_disclosure` was
listed among the untested paths in an earlier draft and **is** exercised —
`HOLD-006` is in the packet, so §4.2 makes the disclosure mandatory, and §5.6 now
carries it. Stated, not corrected: one case was asked for and one was built. The
untested paths are named so a second packet is built against them rather than
against another well-evidenced subject.

**Preferred-counter-narrative challenge.** *Did this accept a claim too easily
because it is corrective, anti-colonial, subaltern or politically corrective?*

One finding, `BF-025` at §6.2, and it is the substantive one: the draft used a
`HYPOTHESIS` to refuse a visitor a conclusion, in defence of the institution's
own measured result. Corrected by a general rule rather than by deleting the row.

**A second finding, and it is not small: the packet had no null explanation.**
`scope_block.null_explanation` as first written read *"the six passages are fully
explained by the poetic tradition's own stock of numbers and its formulaic
diction"* — which is viable explanation (a), `PUR4J-I-01`, the formula reading,
restated. MelaKeela's own preferred reading was occupying two of five rival
slots, and the genuine null — that nothing about the number's provenance need be
accounted for at all — appeared in neither `conclusion_set[]` nor
`withheld_conclusions[]`. That is Rule S-5's second half failing on the one rival
framework §9.2 stage 2 and §8.5 both make mandatory, and this document's own
counter-narrative test did not find it; an adversarial reviewer did. Corrected:
the null is restated, C-1 carries `is_null_explanation`, and §4.4 now requires
exactly one option to carry it. Logged as `BF-026`.

A third, smaller: the worked case gives reading (b), enumeration, two
`PROVISIONAL` claims and one paragraph, against reading (a)'s four diagnostics.
Checked against EOM §9.7 and framework §12.3 V-8 — that is the evidence, and
weight follows evidence. What must be equal is **reachability**, and C-3 sits in
the same list as C-2 at the same ceiling, one interaction away, not behind a
fold. No correction.

**The asymmetry statement** required with this pair: the two failure modes are
symmetrical in form and asymmetrical in power. This document's own case is the
illustration — the packet's entire evidentiary base sits in one European
philological line, and the source that would test rather than supplement it is
egress-blocked (`RA-015`). Presenting the two tests as an even pair, here, would
misdescribe that.

**How these tests were actually run, stated because it changes what they are
worth.** Both were first run by the author of this document, and both found
something (`BF-024`, `BF-025`). An independent adversarial review then re-derived
the worked case against the registers and against this document's own rules, and
found substantially more: the source-id collision at §6.5, the diagnostics
inconsistency at §6.6, the missing null explanation, the C-6 schema defect that
made `BF-025`'s correction a paragraph rather than a mechanism, W-R1's gameable
carve-out, four factual errors in the worked case, and six of the nine
prerequisites at §5.10. `BF-014`'s `future_control` predicted this: an
author-run test interrogates its own conclusion. The corrections are in the
document; the fact that the author's pass cleared what the review found is part
of the record.

Logged: `BF-024`, `BF-025`, `BF-026` in `04-AUDITS/BIAS-FAILURE-LOG.csv`;
`RA-022`, `RA-023`, `RA-024` in `04-AUDITS/REAUDIT-QUEUE.csv`; `IC-P-002`,
`IC-P-003`, `IC-P-004`, `IC-X-002` in
`04-AUDITS/INTERNAL-CONTRADICTIONS.csv`.

---

## 8. Decisions

**No new `D-` identifier is allocated by this document.**
`09-DECISIONS/OWNER-DECISIONS.csv` is authoritative for the namespace and every
choice this document met was either already reserved there or was a
specification choice it may take, and takes openly at §4.6.

Cited and not re-raised:

| ID | Decision | Where it bites here |
|---|---|---|
| `D-010` | which institutional claims may presently be published | sets `accepted_threshold`, which W-R1 is written against. EOM §7.4.1 already fixes the parameter to one of two values — `VERIFIED`, or `VERIFIED + PROVISIONAL` — so **W-R1 is decidable now for every `reason_status` except `PROVISIONAL`**, and the worked case's only `gate-failed` refusal (W-6, `VERIFIED`) holds under either answer. An earlier draft called this load-bearing and said no withheld set could be validated until D-010 was answered; that was an overstatement, and it ran in the direction that excuses the mechanism from being testable today. What D-010 actually decides is the `PROVISIONAL` band: under the stricter answer, W-1, W-2 and W-5 would all move from the withheld set into `conclusion_set[]` under W-R1. |
| `D-024` | is PROVE IT the correction intake | removes §4.7's submission route and W-R3's `from-a-declined-challenge` provenance if answered negatively; everything else stands |
| `D-019` | the join between `mk:` identifiers and the register CSVs | `claims[]` pins `mk:clm:@r<n>`, and the resolution of `PUR-003` to a row in `rigveda-pur-family.csv` runs through whatever D-019 settles |
| `D-045` | does the forts artefact keep the name "The 99 Forts Database" | §5.8 W-6 refuses a conclusion the current name asserts. This is a finding about the interface and takes no position on the name. |
| `D-052` | any server-side per-visitor state | runs are local by default under either answer (EOM §9.5) |

---

## 9. Status of this document

Every design proposition here is `HYPOTHESIS`. No object described exists.

Every claim from `03-REGISTERS/` is cited at its register status and the statuses
are listed in full at §5.3 rather than summarised. Everything from
`01-INHERITED/` — the `the-forts` headline, the RV-01 specification, the Version
12 lines, and `R-04`/`IH-020` at §5.8 — is `INHERITED-UNVERIFIED`, is marked as
such at the point of use, and is cited as evidence for nothing. An earlier draft
made this claim in this section and did not carry the marking at §5.8, which is
the only place the three are used; corrected.

Nothing was retrieved. No row was added to `02-SOURCES/access-ledger.csv` and no
domains were requested.

Per constitution §15 and museum framework Rule S-3: this is a specification. It
is not an implemented page, the packet at §5 does not exist, and it must not be
described as one.
