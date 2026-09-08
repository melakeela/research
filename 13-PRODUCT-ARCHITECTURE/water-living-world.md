# WATER — the first Living World, and the pattern a second is built from

**Written:** 2026-09-08
**Branch:** `claude/water-living-world-pattern-ex1tcr`
**Unit type:** specification. Not research, not public copy, not a page brief.
No sentence in it may be lifted onto a page.
**Backlog items:** 27 (WATER, under *Three flagship experiences*) and 38
(WATER, under *Living Worlds*).
**Programme register row:** `BL-27; BL-38` in
`13-PRODUCT-ARCHITECTURE/authoritative-programme/canonical-programme-register.csv`,
Release 1, role `flagship`.
**Retrieval performed for this unit:** yes — ten rows, `SRC-089` to `SRC-098`,
logged 2026-09-08. One hold opened: `HOLD-007`. Register:
`03-REGISTERS/water-living-world-readiness.csv`, ten rows. Archive audit:
`04-AUDITS/ARCHIVE-AND-POWER-AUDIT.csv` `APA-W-001`.

---

## 0. What this document is, and the rules it runs under

### 0.1 What it specifies

Two things, and item 38 is explicit that the second is the more important:

> **27. WATER.** *Inherited work:* WATER is the strongest proposed first
> Living World, connecting Dholavira, palaeoclimate, engineering, South Indian
> water infrastructure, Tamil sources and Chennai hydrology. The continuity
> belongs initially to the human problem, not automatically to one
> civilization. *Build out:* Select a bounded route with dated records,
> material mechanisms, discontinuities and modern stakes. Use Bhavani Raman’s
> Chennai water work and relevant archaeological/environmental scholarship
> where appropriate. *Gate:* Gaps remain gaps; ancient-to-modern juxtaposition
> does not become an unsupported chain of cultural continuity.
>
> **38. WATER.** *Inherited work:* Same research programme as item 27, but
> here WATER is the first repeatable Living World model rather than merely one
> flagship exhibit. *Build out:* Define the reusable pattern—ancient problem,
> material evidence, text/language, ecological change, modern system,
> discontinuities and action/question—without implying a single uninterrupted
> tradition. *Gate:* The model can support a second water case without
> rebuilding the interface.

*(`06-BACKLOG/MELAKEELA-89-ITEM-MASTER-EXECUTION-PROMPT-v1.md` lines 316–322
and 410–416, both items complete. The source's own bold headings and italic
run-in labels are preserved; the **model** emphasis in item 38 is added here
and is not in the source, which is why "verbatim" is not claimed for it. `06-BACKLOG/README.md` records that file as the "exact
complete 89-item source document, preserved verbatim", and `CLAUDE.md`'s
inheritance rule means quoting it accurately promotes nothing.)*

So this document specifies:

1. **The pattern** — seven slots, each a typed position with a defined
   evidence requirement, a defined render contract, and a defined behaviour
   when it cannot be filled (§3, §4). The pattern is world-independent.
2. **WATER as its first instance** — what each slot would hold, and which of
   those holdings this repository can currently evidence (§4, §6).
3. **How the interface prevents the ancient-to-modern juxtaposition from
   becoming an unsupported chain of cultural continuity** (§5). This is the
   part the brief asks be specified *rather than trusted to the copy*, and it
   is the longest section for that reason.
4. **What a second Living World needs that this does not yet provide** (§9).

### 0.2 The rules it inherits, and does not restate

- `CLAUDE.md` in full: the status vocabulary, the inheritance rule, the
  fourteen-step method, the negative-evidence standard, the translation
  standard, the two adversarial tests, source independence, the attestation
  gradient, and the rule that only retrieval promotes.
- `13-PRODUCT-ARCHITECTURE/museum-framework.md` §10.1 (the Living World
  pattern), §10.2 (WATER), §3.7 (Absence records), §3.10 (proportionality and
  the Exclusion Note), §4.4 (bridges and the seven domains), §4.5 (edge
  display), §7 (the primary-source viewer and evidence search), §11.2 and
  §11.4 (community authority, consent).
- `13-PRODUCT-ARCHITECTURE/experience-object-model.md` §2 (the grounding
  rule), §7.4 (the step-14 public-copy shape as fields), §9 (Challenge),
  §11 (Journey, and §11.3's Living World constraints, and §11.4's rule that
  route is an assertion).

Where this document appears to add a rule that one of those already carries,
it is narrowing it to this pattern, not replacing it.

### 0.2.1 How section references read

**A bare `§x.y` is a section of this document.** Every reference to another
document names it: `museum framework §4.4`, `experience-object-model §11.3`,
`constitution §4E`, `CLAUDE.md`.

This inverts `experience-object-model.md` §0.3.1, which makes a bare `§x.y` a
museum-framework section, and the inversion is deliberate rather than
careless. That document specifies the framework's own objects and cites the
framework on nearly every line; this one specifies a pattern, and most of its
cross-references are to its own seven slots. A convention should follow the
traffic. **Because the two documents disagree, this section exists** — a
reader arriving from the sibling specification will otherwise read `§4.4`
here as bridges when it is slot 4.

An earlier draft declared the opposite convention and then broke it in about
forty places, including inside §7, where the bias-test record pointed at the
museum framework in the one section whose purpose is to let a later reader
check what the tests changed. Both the convention and the forty references
were corrected in one pass. The numbers that collide are 3.4, 4.2 to 4.7,
6.1, 6.2 and 11, and every external use of them here is prefixed.

### 0.3 What it deliberately does not do

- **It does not decide whether WATER is first.** That is
  `09-DECISIONS/OWNER-DECISIONS.csv` **D-005**, `OPEN`. Museum framework
  museum framework §10.2 already says the same. This document is written so that a "no" costs
  nothing: the pattern is the deliverable and it survives WATER being second
  or third.
- **It does not write WATER's claims.** No claim in this document is about
  the past. Every historical proposition it names is named as a slot
  candidate with its current retrieval standing, never asserted.
- **It does not choose the second world.** D-053.
- **It does not decide what the modern slot may name.** D-054.
- **It does not settle the accepted-publication threshold.** D-010, and
  experience-object-model §7.4.1 already explains why nothing can publish
  until it is answered.

### 0.4 The status of every proposition in this document

Museum framework §14.4 puts every design proposition that document contains at
`HYPOTHESIS`. The same applies here, with one distinction that matters:

| What kind of statement | Status |
|---|---|
| Every design proposition — the slots, their contracts, the ten mechanisms of §5 | `HYPOTHESIS`. None has been tested against a built interface or a visitor. |
| Every statement about what backlog items 27 and 38 ask for | `INHERITED-UNVERIFIED`. It is inherited text, quoted, and quoting it accurately does not promote it. |
| Every statement about what this repository can and cannot reach (§6) | `VERIFIED` where a probe row backs it, and each is cited to its `SRC-` row. These are claims about us, and the probe is the retrieval event. |
| Every historical proposition named as slot content | Unstatused **because it is not asserted**. Where a source was reached, the row says what was reached and at what depth; that is a fact about a retrieval, not about the past. |

---

## 1. Why a pattern, and why the two backlog items are not one item

Items 27 and 38 carry the same subject and different deliverables, and the
programme register merges them into one row (`BL-27; BL-38`). The merge is
convenient and it hides the harder half.

- **Item 27's deliverable is a route.** *"Select a bounded route with dated
  records, material mechanisms, discontinuities and modern stakes."* Its gate
  is about that route's honesty.
- **Item 38's deliverable is a mould.** Its gate is about a *second* case:
  *"the model can support a second water case without rebuilding the
  interface."*

A route can be honest and still be unrepeatable — that is in fact the normal
outcome, because the honest route is the one shaped tightly to the evidence
that happens to exist for it. **A pattern is only proven by the case it was
not designed around.** So item 38's gate cannot be satisfied by building
WATER well. It is satisfied when a second thread drops into the same seven
slots and the interface does not move.

This is why the specification is written slot-first and world-second, and why
§9 is a required section rather than a courtesy: a pattern whose author cannot
say what it fails to provide for its second instance has not been tested at
all.

### 1.1 What a Living World is, in the object model, and what a slot adds

Experience-object-model §11.1: *"a Living World is a Journey with
`living_world = true` and §10.1's requirements enforced."* Nothing here
changes that. WATER is a `mk:jny:` and it inherits experience-object-model §11.3's five validation
rules unchanged.

What experience-object-model §11 does not give it is **structure inside the traversal**. A Journey is
an ordered set of Exhibits with a through-line. Item 38 asks for something
narrower: seven *named positions*, each answering a different question, so
that a second thread can be checked for completeness rather than merely for
length.

The slot is that. And it is deliberately **not** a new object type.

> **Declined: `mk:slt:`.** Adding an identifier namespace for slots would make
> every slot addressable, citable and exportable in its own right, which sounds
> like an improvement and is not. A slot is a position in a template; the thing
> a visitor reads and a scholar cites is the Exhibit in it. Two addressable
> things where one is meant is how `challenge` came to mean three things
> (experience-object-model §9.2). The slot is therefore a **record on the
> Journey**, and §3.3 gives its fields.

---

## 2. The continuity rule, which is the whole difficulty

### 2.1 What item 27 actually says

> *"The continuity belongs initially to the human problem, not automatically
> to one civilization."*

Read carefully, this is not a modesty clause. It is a positive statement about
where the thread's unity lives, and it has a consequence the copy cannot
carry: **the Living World's through-line claim is a claim about a problem, not
about a people.**

### 2.2 The through-line, stated as a proposition that could be false

Experience-object-model §11.2 requires `through_line_claims[]` to be non-empty
and shown, statused, at the entrance. experience-object-model §11.5: *"A Journey that asserts no
through-line is a saved search, and should be one."*

WATER's through-line, written so that it can be contradicted:

> **Human settlements in South Asia have repeatedly had to solve the problem of
> holding water through a dry season, and the solutions they built, the words
> they used for them, the labour they required and the failures they suffered
> are separately recoverable — from material, text, environment and living
> systems — at different dates, in different places, by different people, with
> no assumption that any one solution descends from another.**

Three things about that sentence:

1. **It is falsifiable, and the falsifier is easy to state.** If the material,
   textual and environmental records for a given place and period cannot be
   separately recovered — if each turns out to depend on the others for its
   dating or its interpretation — the through-line fails and the thread is a
   single argument wearing four costumes. §8 records this and two more.
2. **Its subject is a recurring problem, not a tradition.** "Repeatedly" is
   doing the work. A recurrence is not a descent.
3. **The last clause is a constraint on the institution, not a finding about
   the past.** It says what WATER will not assume. That belongs in the
   through-line because a visitor is entitled to know the thread's rules
   before walking it.

### 2.3 The failure this invites, named before it is designed against

The failure mode is not that someone writes "and this unbroken tradition
continues today." Nobody on this project would write that sentence. The
failure is quieter and it is structural:

**Seven slots running from an ancient problem to a modern system, presented in
that order, in one continuous surface, under one title, will be read as a
history of one thing** — regardless of the copy. The visitor supplies the
continuity the institution declined to assert, because the *form* asserted it.
Prose disclaimers do not survive this. They are read as modesty about a story
the layout has already told.

That is why §5 specifies mechanisms in the data and render layers rather than
rules for writers. A rule a writer must remember is a rule that fails on the
day the writer is someone else.

### 2.4 And the symmetrical failure, which is likelier here

Experience-object-model §11.4 states the rule with both examples deliberately:
a route running steppe → Punjab → Ganges asserts a migration, and *"a route
running one Indian site to the next in an unbroken sequence asserts
continuity, autochthony or descent just as firmly, and it does so more
quietly, because a route that never leaves is read as no route at all."*

WATER is the second kind. Dholavira → South Indian tanks → Chennai never
leaves South Asia, and the sequence therefore reads as no claim at all. It is
a claim, and it is a claim about a span of roughly four millennia.

What that span contains is not stated here. An earlier draft wrote that it
crosses "two language families, at least three unrelated hydraulic
technologies and a colonial rupture", which reads as scene-setting and is
three unsourced historical propositions — the third of them an independence
claim about technology, load-bearing for the discontinuity reading this
document prefers. §0.4 says every historical proposition here is named as a
slot candidate with its retrieval standing and never asserted, and those three
were asserted. Removed.

**What the world asserts is the through-line at §2.2 and nothing beyond it.**
Whether the span contains one hydraulic tradition or several is a question for
slots 2 and 3, at their statuses, and the world is not entitled to the answer
in its framing.

---

## 3. The pattern

### 3.1 What a slot is

**A slot is a named position in a Living World that asks one question of the
thread, admits only evidence of a stated kind, and — when the thread cannot
answer it — renders a typed absence rather than closing up.**

The last clause is the one that makes gaps stay gaps. A slot that could
disappear when empty would let a world look complete by being narrow. A slot
that must render even when empty makes the thread's shape visible, and the
shape is evidence about the archive.

### 3.2 The seven slots

| # | Slot | The question it asks the thread | Domain of its content |
|---|---|---|---|
| 1 | **ANCIENT PROBLEM** | What did people have to solve, where, and when? | environment + settlement |
| 2 | **MATERIAL EVIDENCE** | What survives that shows them solving it? | artifact + place |
| 3 | **TEXT AND LANGUAGE** | What did they call it, and who wrote that down? | language + text |
| 4 | **ECOLOGICAL CHANGE** | What changed underneath them, and how do we know the date? | environment |
| 5 | **MODERN SYSTEM** | What holds the water there now, and who decides? | modern identity + polity |
| 6 | **DISCONTINUITIES** | What broke, what is missing, and what we cannot see | the archive itself |
| 7 | **THE ASK** | What the visitor is invited to do or decide | — |

Slot 6 is not a caveat appended to the other six. It is a slot with the same
weight, the same render budget and the same evidence requirement, and §5's
mechanism M-2 places it so that it cannot be walked past.

### 3.3 The slot record

A field structure on the Journey, one per slot. No new identifier namespace
(§1.1).

| Field | Type | Notes |
|---|---|---|
| `slot_key` | enum(7) | the seven above; fixed vocabulary, world-independent |
| `slot_question` | `mk:qst:` | the question this slot asks **in this world**, as a real Question object. Non-empty even when the slot is unfilled — a slot with no question is a container, and containers are what experience-object-model §11.5 calls a saved search. |
| `filled_by` | `mk:exh:` or null, except slot 7 which takes `mk:chl:` or `mk:qst:` | the object standing in the slot. Null is a legitimate state — see §3.4 invariant 7 on what it is not sufficient for. An earlier draft typed this `mk:exh:` throughout while §4.7 assigned slot 7 a Challenge or a Question, so the field could not hold the content the specification gave it. |
| `admission` | vocabulary reference | which evidence classes and which attestation modes this slot admits (§4, per slot) |
| `absences[]` | array of `mk:abs:` | **non-empty when `filled_by` is null**, and permitted alongside a filled slot. Typed under museum framework §3.7. An array, not a single record: experience-object-model §11.2 types the Journey's `absences[]` as an array, and slot 6 is an entire slot made of absences — as a singular field it could hold exactly one. |
| `inapplicable` | bool + reason | true where the slot's question **has no evidence class in this world**, as against having one that is unevidenced. See §9.1a: this is the field a LANGUAGE world needs and it is specified here rather than left to be discovered, because without it such a world must mint a typed absence for a slot that has nothing to be absent. |
| `entry_point` | bool | whether a visitor may begin the world here. See M-8, and the typing gap it records: experience-object-model §11.2 types a Journey's `entry_points[]` as an array of `mk:exh:`, so an unfilled slot cannot be an entry point in the object model as it stands. |
| `inbound_edges[]` | array of `mk:rel:` | the relationships that justify drawing a connection from another slot **to** this one. Empty is normal and is not a defect. |
| `render_budget` | derived | computed from the proportionality block of the claims in `filled_by`, advisory under museum framework §3.10 |
| `constraint_block` | Constraint Block | experience-object-model §5.2, inherited unchanged |

### 3.4 Slot invariants

1. **All seven slots exist in every Living World.** A world does not choose
   its slots. A world with five slots is a different product and needs its own
   specification.
2. **A slot is either filled or typed.** `filled_by` null and `absence` null
   together is a validation failure, not a draft state.
3. **`slot_question` is never null.** The question survives the absence of an
   answer; that is most of what slot 6 is for.
4. **No slot may be filled by an Exhibit created for it.** Experience-object-
   model §11.3, rule 1: a Living World *"creates no private content"*. Every
   Exhibit in a slot stands alone and is reachable without the world.
5. **No slot may borrow another's certainty.** Method step 4: *"One class
   cannot borrow certainty from another."* The interface expression of this is
   M-3.
6. **A slot's absence records are displayed inside the slot**, at the position
   where a visitor would look for the thing that is missing — museum framework
   museum framework §10.1's *"it carries its own absences"*, narrowed from the world to the
   slot, because a world-level absence list at the end is an appendix and
   experience-object-model §11.6 forbids exactly that.
7. **Filling slots is not the same as being a publishable Living World, and
   the slot record does not relax one rule of experience-object-model §11.3.**
   A Journey needs `traverses[]` non-empty with a minimum of two, and a Living
   World needs at least four postures crossed including Extraction /
   Collection or Reconnection. Two filled slots yield at most two postures.
   So a world with slots 6 and 7 filled and the rest typed absent is a
   legitimate, honest, **unpublishable** object: it fails experience-object-model §11.3 rule 2 and
   should. §6.2's build-sequence recommendation is written against this
   invariant and not around it.

---

## 4. The seven slots, with evidence requirements

Each slot below gives: **the question**, **the evidence requirement** (what
must be true of an object before it may fill the slot), **the WATER
candidate**, and **the current retrieval standing** of that candidate in this
repository. §6 collects the standings into one table.

The evidence requirement is the reusable half. The WATER candidate is not.

### 4.1 Slot 1 — ANCIENT PROBLEM

**Question.** What did people at this place have to solve, and when?

**Evidence requirement.**

1. A **Place Assertion** (museum framework §2.8) with its type — evidenced,
   approximate, or inferred — never a modern administrative name standing in
   for an ancient location.
2. A **date range on the problem, not on the solution.** The seasonality or
   scarcity being solved is an environmental claim with its own proxy, its own
   resolution and its own error bars, and it is dated independently of the
   structures in slot 2. If the only evidence that the place was dry is that
   someone built a reservoir there, the slot is circular and the world says so.
3. **The null explanation stated** (method step 1). For a water thread the
   null is that the structure served a purpose unrelated to scarcity — storage
   for craft production, display, ritual, defence, or drainage of too much
   water rather than retention of too little.
4. **No environmental determinism.** Museum framework §10.2, constraint 2: a
   climate proxy explains a climate, not a settlement pattern, without a
   mechanism. Slot 1 states the problem; it does not explain the response. The
   response is slot 2, and the link between them is a bridge (M-5).

**WATER candidate.** Dholavira, Great Rann of Kachchh — a settlement in an
arid zone with a seasonal and partly saline water supply.

**Current standing.** Abstract level only, and the distinction matters here
more than anywhere else in the document, because this is the slot that carries
a date.

What was retrieved is the **abstract** of Sengupta et al. 2020
(`10.1002/jqs.3178`), returned by `SRC-089` probe 1 and repeated in the
metadata block of `SRC-090`'s chunk 1. It states occupation *"at ~5500 years
BP (pre-Harappan), and continuation until ~3800 years BP"* and a settlement
that *"rapidly expanded under favourable monsoonal climate conditions"*. The
article, its calibration, its figures and its supplementary material are not
retrieved (`HOLD-007`).

Three things follow, and the first two are corrections made after adversarial
review:

1. **That range is an abstract's summary of a radiocarbon series, not a date
   this repository holds.** It has no date type attached, no laboratory
   identifiers and no error bars, and M-4 of this document forbids rendering a
   date without its kind. Quoting it here is a record of what a probe
   returned; it is not available to fill slot 1.
2. **`HOLD-007` forbids the stronger statement and that prohibition stands.**
   Nothing may say the Dholavira water structures are dated until the article
   is read rather than excerpted. An occupation range for a settlement and a
   date for a reservoir are different claims, and the second is the one the
   slot actually needs.
3. **Not sufficient to fill the slot; sufficient to know the slot is
   fillable** — which is the whole of what §6 claims for it.

### 4.2 Slot 2 — MATERIAL EVIDENCE

**Question.** What survives that shows them solving it, and who made it?

**Evidence requirement.**

1. **Findspot, context and excavation-report locator for every object.** Not
   a site name. Museum framework §3.4's citation-level provenance, and
   `CLAUDE.md`'s locator rule: "see the article" is not a locator.
2. **Excavation coverage stated for every site the slot generalises over.**
   Excavated area against total area, and publication state. Without it,
   neither presence nor absence in this slot means anything, and slot 6
   depends on it.
3. **The labour question on every water work.** Museum framework §10.2,
   constraint 3, and constitution §4V: who did the labour, who was excluded,
   who got the credit. *"A tank with a donor inscription records a donor; it
   does not record a builder."* Where the builder is unrecorded, the absence is
   typed — `NOT PRODUCED` if the record-making practice never named builders,
   `NOT RECOGNISED` if it did and we have not looked — and the type is
   displayed in slot 2, not deferred to slot 6.
4. **Custody now.** Who holds the object, who may see it, under what terms.
   museum framework §11.8.
5. **No generic landscape decoration.** Museum framework §10.2, constraint 4.
   A photograph of a river is not evidence of a drainage system. An atmosphere
   asset is `is_primary = derivative` with a stated non-evidential purpose and
   may never occupy an evidence position (experience-object-model §2.6).

**WATER candidate.** Dholavira's reservoirs, drains and rock-cut tanks; and,
for a second case, South Indian tank and *eri* systems.

**Current standing.** **Blocked at the level that matters.** The excavation
reports are in no lane reachable from this session (`HOLD-007`). *That they
are R. S. Bisht's ASI volumes is an unretrieved lead: no ledger row records
it, and it is marked rather than dropped because a later session needs to know
what to look for.* What is reachable is secondary and modelling-led:
Ghosh et al. 2019 recomputes Dholavira's hydraulic gradient; Houdas 2024
reports a corpus of 597 hydraulic structures across twelve Indus sites, which
would be the systematic inventory this slot wants, and only its abstract was
returned. Every reachable account depends on excavations we cannot read, and
the dependency is currently **asserted rather than measured**, because Scite —
the instrument step 5 would use — refused for quota (`SRC-091`).

### 4.3 Slot 3 — TEXT AND LANGUAGE

**Question.** What did they call it, in what language, written down by whom,
and how do we know what the word meant?

**Evidence requirement.** The translation standard in full, on every
consequential word: original script where available, transliteration,
grammatical form, semantic range, textual context, edition, exact locator, the
translation used, the alternatives, and the interpretive consequence of
choosing between them.

Additionally, and specific to this slot:

1. **The five-date spine per text** (museum framework §10.2): composition,
   attestation, manuscript, edition, translation are different dates and the
   slot shows all five.
2. **The attestation gradient is rendered, never flattened.** An attested
   Tamil word, a reconstructed Proto-Dravidian form, an accepted loan, a
   proposed substrate form and an unidentified residue are five different
   things (`CLAUDE.md`; constitution §4E). A slot that lists them in one column
   has made a claim by typography.
3. **The inherited English category is audited before use.** *Tank*,
   *reservoir*, *irrigation*, *canal* and *ritual bath* are all translations,
   and so is ***civilization***, which is on `CLAUDE.md`'s own ten-category
   audit list and is the one word from that list the reachable literature on
   this thread actually uses — *"hydraulic civilisation"* is the phrase
   `SRC-089` returned in the Singh et al. 2020 abstract, and `HOLD-007` names
   it as needing audit. An earlier draft of this list omitted it while the
   hold asserted a control for it, so the hold pointed at a rule that did not
   exist.
   This repository has done the equivalent work once, on *pur-*
   (`03-REGISTERS/rigveda-pur-typology.csv`), and that is the model.
4. **No lexical bridge to a people.** A shared word is a `language→language`
   relationship. Reading it as `language→ancestry` or `language→modern
   identity` is a bridge under museum framework §4.4 with all of its's requirements, and it is
   the single most likely place for this world to acquire an argument nobody
   made.

**WATER candidate.** Sangam-corpus hydrological vocabulary; Tamil inscriptions
recording tank construction, donation and maintenance obligation; the
Dravidian water and irrigation lexemes.

**Current standing.** **Empty, and it is the emptiest slot.** No Tamil corpus
lane has ever been opened in this repository — the reachable corpora are
Vedic (`SRC-019` to `SRC-024`, `SRC-069` to `SRC-085`) and comparative-lexical
(`SRC-060` to `SRC-067`). GRETIL and TITUS are refused (`SRC-080`, `SRC-082`).
The Sangam material returned by `SRC-089` is seven English-language articles
*about* Sangam water vocabulary, mostly in journals with no evident review,
and an article about a text is not the text. **This slot cannot be filled for
WATER today at the standard the translation rule sets, and no allowlist change
fixes it** — it needs a corpus lane opened deliberately.

### 4.4 Slot 4 — ECOLOGICAL CHANGE

**Question.** What changed underneath them, how do we know, and how precisely
is it dated?

**Evidence requirement.**

1. **Proxy, resolution, calibration and error, on the face of the display.**
   A palaeoclimate curve rendered without its sampling resolution is a
   picture, and it will be read as more precise than it is.
2. **The environmental date and the settlement date are two dates**, produced
   by different methods, and the interface never renders them on one line
   without showing both error bars.
3. **Every `environment→culture` link is a bridge** with museum framework §4.4's mechanism and
   rivals. Museum framework §10.2, constraint 2, states this as WATER's
   prestige-bias failure mode and it is worth restating why: the environmental
   determinist reading is *attractive* here because it is quantitative, it is
   published in high-prestige journals, and it produces a clean story. Only
   the middle one is a trigger `CLAUDE.md` names — *institutionally
   prestigious* — and an earlier draft claimed all three were. The other two
   are real reasons the reading is tempting and they are this document's
   observation, not the controller's.
4. **A decline narrative is a historiographical object, not a finding.** Who
   proposed it, when, against what, and what its current standing is (method
   step 11).

**WATER candidate.** The 4.2 ka event and the Meghalayan boundary;
Ghaggar-Hakra palaeochannel hydrology. *Unretrieved leads, named in the
retrieved chunks and in no ledger row of their own: the Kotla Dahar, Mawmluh
Cave and Gulf of Oman proxy records.* They are marked because an earlier draft
listed them beside the retrieved candidates in the same typography, which
makes background knowledge indistinguishable from a probe result.

**Current standing.** **The best-served slot, and that is itself a finding.**
`SRC-090` returned passage-level text with DOIs from Sengupta et al.
(`10.1002/jqs.3178`), Singh et al. (`10.1002/jqs.3320`, which `SRC-090`
records as Ghaggar-Hakra and Markanda palaeoflood deposits) and Walker et al.
(`10.1002/jqs.2565`, the Holocene subdivision proposal). The reachable literature is strongest exactly where the
determinist reading is most tempting, and weakest (slots 2 and 3) where the
counter-evidence would come from. **That asymmetry must be displayed in the
world, not corrected for silently** — it is an archive-audit result about our
own reach, and §5's M-9 is where it surfaces.

### 4.5 Slot 5 — MODERN SYSTEM

**Question.** What holds the water there now, who decides, and who does
without?

**Evidence requirement.**

1. **The modern slot is a claim set like any other**, with sources, dates and
   statuses. Present-tense material is not exempt from the ledger because it
   is verifiable in principle.
2. **Every ancient→modern link is a bridge** of type
   `polity→modern-identity` or `culture→modern-identity`, under museum framework §4.4 **and**
   under museum framework §11.2's additional governance. Museum framework §10.2, constraint 1.
3. **Adjacency is forbidden as an argument.** The slot sits beside slot 1 in
   the pattern and shares nothing with it unless an edge exists (M-3).
4. **The archive audit runs on the modern record too.** The colonial
   waterworks archive is a created record with an interest: it recorded
   engineering and property, and it is not a neutral witness to what it
   displaced.
5. **A named living community requires museum framework §11.2 and §11.4 to be real first** —
   not planned.

**WATER candidate.** Chennai: the *eri* cascades, the colonial reservoir and
piped network, the twentieth-century filling of tanks, the 2019 reservoir
failure, and the current governance of the four reservoirs.

**Current standing.** **Reachable in outline; blocked at its named source; and
governed by an open decision.** `SRC-090` returned four passages from Coelho
2022 (`10.1111/1468-2427.13087`) covering *eri* boundaries, the 1876 pipe
network, waterbodies turned into land since the 1960s, the Eri Schemes of the
1980s, and the 2019 drought *"experienced in starkly uneven ways across its
territory"*; plus D'Souza 2006 on colonial hydrology and Sankarkumar et al.
2026, which is the source for the reservoir figures of the 2019 crisis. The
2019 material is in both and is attributed to both. The one source backlog item 27 names by name — Bhavani
Raman's Chennai water work — is **not retrieved**: `india-seminar.com` is
refused at the gateway (`SRC-096`), and what is known of the piece comes from
a search-result listing (`SRC-097`), which `CLAUDE.md` forbids treating as a
substitute. **What this slot may name is `D-054`**, and until it is answered
the slot is specified, held, and typed `NOT ACCESSIBLE` on its named source.

### 4.6 Slot 6 — DISCONTINUITIES

**Question.** What broke, what is missing, what was never written down, and
what could we not recognise if we saw it?

**Evidence requirement.** The negative-evidence standard in full, per absence:
what should exist, where, probability produced, probability survived, search
coverage, accessibility, recognisability — then one of the eight types.

Three rules specific to the slot:

1. **Only `ABSENT DESPITE ADEQUATE SEARCH` may function as evidence against a
   proposition.** The other seven types are statements about the archive, and
   museum framework §3.7 requires the interface render them *"in the archive's voice, not the
   past's."* In this world that distinction is load-bearing: "no Tamil
   hydraulic vocabulary in our record" is a fact about our lanes (§4.3), and
   rendering it as a fact about Tamil is the exact failure the whole document
   is designed against.
2. **The institution's own gaps are in this slot, not in a colophon.**
   `HOLD-007` is slot 6 content for WATER. A visitor who can see that we could
   not read the excavation reports is better informed than one who reads a
   confident account built without them.
3. **A break is not a decline.** The end of a hydraulic system is an event
   with a date and a mechanism, and "decline" is an interpretation with an
   author. Slot 6 holds the event; the interpretation is slot 4's
   historiographical object or an Exclusion Note (museum framework §3.10).

**WATER candidates, none of them yet typed.** The abandonment of Dholavira;
the absence of an identified builder for any Indus water work; the interval
between the Indus hydraulic material and the South Indian tank material; the
twentieth-century conversion of Chennai's tanks to land, which `SRC-090` chunk
8 records as running *"since the 1960s, both by private encroachment and,
particularly, by planned state initiatives"*.

Two corrections after adversarial review, both of the same kind — an absence
asserted without the record that licenses it:

- An earlier draft called the Chennai tank filling `DOCUMENTED DESTRUCTION`
  and *"the one absence type in this world with a paper trail"*. That is a
  museum framework §3.7 typing, and that section requires `expected_evidence`, `expected_where`,
  `p_produced`, `p_survived`, `search_coverage`, `accessibility` and
  `recognisability` before a type is assigned. None was recorded. It is a
  candidate for that type, not an instance of it.
- An earlier draft called the interval between the two bodies of material
  *"a real gap and not a transition"*. That is an argument from absence made
  in the framing of a slot whose whole subject is that such arguments need the
  seven-field record first, and it runs toward this document's own preferred
  reading. `04-AUDITS/REAUDIT-QUEUE.csv` `RA-018` is open against exactly this
  pattern. Removed; the interval is named and not characterised.

**Current standing.** **Partly specifiable now, and that is less than an
earlier draft claimed.** The half of slot 6 that is about *our own reach* —
`SRC-089` to `SRC-098`, `HOLD-007`, `APA-W-001` — needs no external retrieval
and is buildable today. The half that is about *the past* is not: §4.2
requirement 2 states that slot 6 depends on excavation coverage, and
`APA-W-001` records that excavated-area-against-total-area for the Indus water
sites is unmeasured, *"so no absence in slot 2 can yet be typed"*. The
abandonment and the absent builder both need that figure.

An earlier draft read *"Specifiable now, and it is the only slot that is"* and
cited `06-BRIEFS/mvp-fifteen/09-the-water-city.md` §6 for the claim that this
needs no retrieval. Two errors, both logged as `BF-025`. The first is the
contradiction above. The second is a misattributed quotation: the brief's
*"the half of this unit that changes the page most"* attaches to the
**recognition criterion for *palace***, a category audit, and the brief's own
MVP-U9 says the negative-evidence record needs excavated area against total
area — that is, retrieval, the opposite of what the sentence was cited for.

### 4.7 Slot 7 — THE ASK

**Question.** What is the visitor invited to do, decide, or disagree with?

**Evidence requirement.**

1. **The ask resolves to a real claim at a real status.** Experience-object-
   model §2: an ungrounded invitation is a headline. A Challenge (`mk:chl:`)
   puts one institutional claim at risk; a Question (`mk:qst:`) is a real
   `mk:qst:` node in the graph, not a rhetorical flourish at the end of the
   copy.
2. **Disagreement must be a reachable outcome.** Museum framework §9.1: *"If
   PROVE IT cannot produce the outcome 'the institution is wrong here', it is
   a quiz, and a quiz that only confirms is publicity."*
3. **The ask may not be an action in the present that the evidence has not
   earned.** This is the slot where a water thread turns into advocacy. "Save
   your local lake" is a good cause and it is not a conclusion of this record.
   If the ask is a present-tense action, it is grounded in slot 5's claims at
   slot 5's statuses, and the visitor can see which.
4. **No scoring, no right answer, no completion state.** Experience-object-
   model §11.6: a Journey may not be paced, and a completion lock is time
   pressure with the clock hidden.

**WATER candidate, and the one this specification recommends.** The strongest
available ask is not about water at all: it is *"here is what we could not
read, and here is what it would change."* WATER's honest ask, on today's
evidence, is a challenge to the institution's own reach — which is a real
claim, at `VERIFIED`, with a falsifier that is an allowlist entry.

**Current standing.** Buildable now, and only in that form.

---

## 5. How the interface prevents the continuity chain

Ten mechanisms. Each is stated as a rule in the data or render layer, with
what it costs and what it does not catch. A mechanism that only a careful
author can honour is not on this list.

**Not all ten are new, and the count should not be read as ten safeguards
added.** Adversarial review found that presenting inherited rules inside a
numbered list inflates what the document appears to contribute. The honest
accounting:

| | Status |
|---|---|
| **M-1, M-2, M-3, M-5, M-8, M-10** | New here, or an existing rule narrowed to a point where it changes what may be built |
| **M-6** | A restatement of museum framework §4.4 rule 5, verbatim in substance, restated because a Living World is where it will be tested |
| **M-9** | Its rule sentence is museum framework §3.10 almost verbatim; the new element is the **slot-fill profile** alone |
| **M-4, M-7** | Inherited requirements (step 2; experience-object-model §11.6) with one added constraint each — M-4's no-connecting-line rule, M-7's withdrawal consequence |

Two of the ten therefore add little, and saying so is cheaper than letting a
reader count safeguards that are already in force elsewhere.

### M-1 · No edge, no line

**Rule.** The interface draws no visual connection between two slots unless a
Relationship Object exists whose subject is in one and object in the other.
Adjacency, sequence number, shared page, shared colour, a continuous scroll,
a connecting rule or a gradient are all connections, and none of them is a
record.

**Why.** Museum framework §4.5: *"Every rendered edge carries status and
attestation mode. An unstatused edge cannot be drawn."* This narrows it: in a
Living World, the layout itself is an edge-drawing device, so the rule has to
bind the layout and not only the diagram.

**Cost.** The world will look disconnected in places, because it is. A
designer will want to bridge the whitespace and must not.

**Does not catch.** Reading order. A visitor walks slot 1 then slot 2 and
infers a link with no line drawn. M-4 and M-8 address that; M-1 alone does
not.

### M-2 · The gap is a position, not the absence of one

**Rule.** Slot 6 is a slot. It has a render budget, an entry point, and it
cannot be collapsed, deferred to the end, or rendered at lower prominence than
slots 1–5. Additionally, per §3.4 invariant 6, a slot-level absence renders
**inside its own slot**, at the position where the missing thing would be.

**Why.** Experience-object-model §11.6: *"Absences are part of the thread, not
an appendix."* An appendix is what an absence becomes the moment it is allowed
to be last.

**Cost.** Six-sevenths of a world is what most museums ship. This one shows the
seventh, and it is the least attractive surface in the product.

**Does not catch.** A slot 6 that is filled with generic epistemic humility
rather than typed absences. The absence-type vocabulary is the control: a
slot 6 whose entries are prose and not `mk:abs:` records fails validation.

### M-3 · Two slots never share a frame

**Rule.** No render composes objects from two slots into one visual unit — one
image, one panel, one card, one animated transition, one before/after pair —
unless an edge licenses it, and where an edge licenses it, the edge's status,
its domain pair and its alternatives render in the same unit.

**Why.** This is the juxtaposition the brief names. A photograph of a
Dholavira reservoir beside a photograph of a dry Chennai reservoir, under one
heading, makes an argument that no sentence made and no register carries. It
is the most efficient unsupported claim available to this world, and it can be
made accidentally by a layout engine balancing a grid.

**Cost.** The most striking possible image in this world is prohibited unless
the bridge exists. If the bridge exists at `PROVISIONAL`, the image ships with
its rivals attached, which is less striking.

**Open dependency, and which rule governs meanwhile.** *At what weight* the
rivals render is not settled. museum framework §4.5 requires a bridge's alternatives at the
same visual weight as the bridge; museum framework §12.3 constraint V-8 states that *"Equal
visual weight is a claim, and is only made where the evidence is equal"*, and
`CLAUDE.md`'s no-false-equivalence constraint says the same. `IC-X-001`
records that the two have not been reconciled and that the reconciliation is
the framework author's.

**Until the scope note `RA-021` asks for exists, V-8 governs.** That is
`RA-021`'s own standing instruction — *"any surface drawing rival explanations
follows V-8"* — and an earlier draft of M-3 cited museum framework §4.5 twice and V-8 never,
which is the failure `BF-022` logged against the sibling document two commits
ago. M-3's **prohibition** is unaffected either way; only the licensed case
differs. Recorded as `IC-W-002`.

**Exemption: the time spine.** M-4's single axis is a composition of objects
from all seven slots and no edge licenses it, so M-3 read literally forbids
M-4. The exemption is narrow and it is the reason M-4 carries its own
no-connecting-line rule: **placing two objects on a shared axis by a property
each of them independently has is not asserting a relationship between them,
provided nothing is drawn between them.** A date is such a property. A theme,
a colour, a region and a "phase" are not, and no other shared-axis
composition inherits this exemption.

**Does not catch.** A single image that contains both — a modern photograph of
an ancient structure still in use. That is one object, not a juxtaposition,
and it needs its own treatment: it is dated to the photograph, not to the
structure, and the date shown is the photograph's.

### M-4 · One dated spine, and every object sits on it with its own date type

**Rule.** Every object in every slot renders with the **kind** of date it
carries — event, composition, attestation, manuscript, excavation, analysis,
publication, photograph — and the world exposes a single time axis on which
all of them can be placed. Two objects may not be rendered as contemporaneous
because they share a century; they share a century, with their error bars.

**And nothing is drawn between the points.** No connecting line, no ribbon,
no animated sweep, no shared band, no "era" shading spanning objects from
different slots. The axis positions; it does not join. This is the condition
on which M-3 exempts the spine at all, and without it the spine is the single
most efficient continuity assertion in the product — a line through seven
slots, drawn by a chart library, licensed by nothing.

**Why.** Method step 2, and the programme register's own requirement for this
item: *"joining dated environment, settlement, crop, storage, labour, ritual,
text and memory records without period collapse."* Period collapse is what a
timeline does when it drops the error bars.

**Cost.** The spine will be mostly empty and visibly uneven. Slot 4's
material is dated to centuries with published uncertainty; slot 3's Tamil
material would be dated to a range that is itself contested; slot 2's is dated
by excavation phase. Showing that honestly makes a worse-looking timeline.

**Does not catch.** A visitor reading left-to-right along the spine as a
narrative. M-8.

### M-5 · The ancient–modern seam is a bridge, and when there is no bridge there is a stated break

**Rule.** The transition from slot 4 to slot 5 is the pattern's highest-risk
edge. It may be rendered as a connection **only** where a
`culture→modern-identity` or `polity→modern-identity` bridge exists with
museum framework §4.4's mechanism, alternatives and status, plus its §11.2 governance. **Where no
such bridge exists, the seam renders as a declared break** — an explicit
statement that the record does not connect these, occupying the space the
connection would have occupied.

**Why.** Museum framework §10.2 constraint 1 requires the thread reach the
present *"through statused bridges, never through adjacency"*. The addition
here is what happens on failure: not silence, and not a smaller gap, but a
break the same size as the connection, so the absence of a bridge is as
visible as its presence would have been.

**Cost.** In WATER as currently evidenced, this seam is a break. The flagship
Living World's most anticipated moment is a statement that we cannot join
these two things.

**Does not catch.** A bridge that exists and is weak. museum framework §4.5 handles that by
requiring rivals at equal weight; it is a different failure.

### M-6 · Transitive closure is off across domains, at the data layer

**Rule.** Museum framework §4.4 rule 5, restated because a Living World is
where it will be tested: if slot 2's artifact bridges to slot 3's language and
slot 3's language bridges to slot 5's modern community, the system must not
derive or display artifact→community. Not in a graph view, not in "related
material", not in search facets, not in an export.

**Why.** museum framework §4.4: *"This is a database-level rule because it is the mechanism by
which a map of trade goods silently becomes a map of languages."* In this
world it is the mechanism by which a reservoir becomes an ethnicity.

**Cost.** "Related material" in a Living World will be sparser than a
recommender could make it. Experience-object-model §2.5's composition
transitivity is the only traversal permitted, and it is about product
structure, not the past.

**Does not catch.** A human author writing the transitive claim in prose. The
grounding rule catches that only if the sentence is required to resolve —
which experience-object-model §7.5 requires of every claim-bearing sentence.

### M-7 · The through-line is a claim with a status, shown before entry, and it may be `REJECTED`

**Rule.** `through_line_claims[]` renders at the entrance with statuses, before
the visitor enters (experience-object-model §11.6). A visitor may decline to
walk a thread made of hypotheses. And the through-line is a claim in the
register like any other, which means **it can be tested and it can fail** —
and a Living World whose through-line is rejected is withdrawn, not quietly
re-titled.

**Why.** Constitution §2 requires the record stay capable of contradicting
MelaKeela's own pages. A world whose premise cannot be rejected is advocacy
infrastructure.

**Cost.** The institution has to be willing to withdraw its flagship.

**Does not catch.** A through-line written so vaguely it cannot fail. §2.2's
falsifiers exist to prevent that, and §8 states them.

### M-8 · The route is `free`, and it can be walked backwards

**Rule.** `traversal_order = free`. `order_is_claimed = false`. Slot 6 is
reachable from every other slot in one interaction. Where any slot is offered
as a starting point, **at least one offered starting point is slot 5 or slot
6** — a visitor can start in the present, or start with what is missing, and
walk outward.

**Corrected after adversarial review, in two places.**

1. **`free`, not `suggested`.** Experience-object-model §11.4 makes `free` the
   default and `suggested` an option requiring a stated pedagogical reason.
   An earlier draft argued only against `fixed` and then adopted `suggested`,
   which is the stronger of the two remaining assertions — while conceding, in
   the same paragraph, that the reverse walk is the truer one. An argument
   that the default order is the less true one is an argument for `free`.
2. **Entry points cannot be expressed for an empty slot, and the rule no
   longer pretends otherwise.** Experience-object-model §11.2 types a
   Journey's `entry_points[]` as an **array of `mk:exh:`**. An unfilled slot
   has no Exhibit, so it cannot be an entry point in the object model as it
   stands. In WATER as evidenced today slot 5 is held by `D-054` and slot 6
   is unfilled, so the earlier draft's requirement — *"at least two slots
   carry `entry_point = true`, one of them slot 5 or 6"* — was unsatisfiable
   by the very world it was written for. The rule is now conditional, and the
   typing gap is carried to §9.4 as something the object model must change
   before any Living World can offer entry at an empty slot.

**Why.** Experience-object-model §11.4's test: *would a visitor who walked it
in reverse learn something false?* Apply it honestly to the seven-slot order.
Walked forwards, 1→5 reads as a history. Walked backwards, 5→1 reads as an
inquiry: here is a modern water system, here is what changed, here is what
people wrote, here is what survives, here is the problem. **The reverse walk
is the truer one**, and the fact that the default order is the less true one is
a defect in the pattern that this mechanism manages rather than removes.

Refusing `fixed` is therefore not a convenience. If the order were `fixed`,
experience-object-model §11.4 would require a statused claim in
`through_line_claims[]` carrying the sequence — and that claim would be
*"these five things are stages of one process"*, which is precisely the
continuity claim the world declines to make. The same argument, one degree
weaker, is why the order is not `suggested` either: a suggestion is still the
institution saying which way round to read it.

**Cost.** A materially weaker first visit, and this is the largest cost in
§5. Under `free` the world offers no recommended path at all, and most
visitors will still walk 1→7 because that is the order the slots are numbered
in — so the risk M-2 and M-5 are designed against remains live for them, and
the institution has given up the one lever that might have redirected it.

**Does not catch.** Anything, for a visitor who walks it once, forwards, and
leaves. That visitor is the one this whole section is about, and no mechanism
here fully protects them. Stated as a limitation, not resolved.

### M-9 · Render budget is computed from evidence and the divergence is shown

**Rule.** Each slot's `render_budget` is computed from the proportionality
blocks of the claims in it (museum framework §3.10), the computed value and
the allocated value are both stored, and a divergence is a review finding.
Additionally, and specific to a Living World: **the world displays its own
slot-fill profile** — which slots are filled, which are typed absent, and at
what evidential depth.

**Why.** museum framework §3.10 is deliberately advisory, and rightly: *"Automating space
allocation from a computed weight would make the interface decide historical
questions."* But a Living World has a failure the per-claim metric misses. In
WATER as evidenced today, slot 4 is rich and slots 2 and 3 are poor. Left
alone, the world would spend most of its space on palaeoclimate and thereby
argue environmental determinism **by allocation** — the exact failure museum framework §10.2
constraint 2 names, arrived at with no author intending it.

The fill profile is how that becomes visible rather than persuasive: the
visitor sees that the thread is well-evidenced on climate and unevidenced on
language, and reads the imbalance as a statement about the archive.

**Cost.** The world advertises its own weakest point on its own surface.

**Does not catch.** The decision to build WATER first rather than a thread with
an even evidence profile. That is D-005 and it is the owner's.

### M-10 · Decay shows as a gap

**Rule.** When the object in a slot is withdrawn, suspended for consent, or
superseded, the slot empties and the world **shows the gap rather than
rerouting around it**. What fills the gap depends on why, and the distinction
is not cosmetic:

| Cause | What the slot shows |
|---|---|
| **Withdrawn for consent** (experience-object-model §8.7) | a consent record, per §11.4. Not an absence type. |
| **Withdrawn for a rights or custody change** | the rights record, per museum framework §11.8. |
| **Superseded** | the supersession, pointing at what replaced it, per museum framework §3.6 — and, if nothing replaced it, the slot is unfilled and §3.4 invariant 2 applies. |
| **The evidence itself turned out not to exist or not to be reachable** | an `mk:abs:` record with all seven museum framework §3.7 fields, typed. |

**Corrected after adversarial review.** An earlier draft had every one of
these mint an absence typed `NOT ACCESSIBLE` or `NOT PUBLISHED`. Three things
were wrong with that. A supersession is not an absence of evidence — this
ledger's own `SRC-088` states the principle: *"that typology types absences of
evidence."* A consent withdrawal is a governance event and typing it as an
archive gap misdescribes a living community's decision as a hole in the
record. And minting a type mechanically bypasses museum framework §3.7's seven required fields
entirely, which is the same failure this document logged against itself at
`BF-025` in slot 6.

**Why.** Experience-object-model §11.6, and museum framework §3.4's custody
rule that *"gaps are steps"* and rendering a three-step chain as two is
laundering. A world that silently closes over a withdrawn slot has made its
thread look more complete than the record.

**Cost.** The world degrades visibly over time, and consent withdrawals
(experience-object-model §8.7) can degrade it without anyone editing it.

**Does not catch.** Grounding decay in the *claims* under a still-present
Exhibit. Experience-object-model §2.7's continuous check covers that; this
mechanism is about the slot.

### 5.1 What the ten mechanisms together do not do

Stated plainly, because a mechanism list reads as a guarantee and this one is
not:

1. **They do not stop a visitor inferring continuity.** They stop the
   institution asserting it, and they make the assertion visible when it is
   made. A visitor who walks seven slots forwards once will probably still
   leave with a story. M-8 admits this.
2. **They do not fix the evidence profile.** M-9 makes the imbalance visible;
   it does not make slot 3 fillable.
3. **They do not survive being partially implemented.** M-1 and M-3 without
   M-5 produce a world that refuses to draw lines and then places the two
   photographs side by side anyway. The set is the specification, not a menu.
4. **They are all `HYPOTHESIS`.** None has been tested against a visitor.
   §8 gives the falsifiers.

---

## 6. What the repository can currently evidence

Item 27 names six candidate materials and one scholar. This is the answer, as
of 2026-09-08, against the probes at `SRC-089` to `SRC-098`. Each row of the
candidate row of the table has a register row in
`03-REGISTERS/water-living-world-readiness.csv` with its locator and retrieval
date — `WLW-002` Dholavira, `WLW-011` engineering, `WLW-003` palaeoclimate,
`WLW-004` South Indian infrastructure, `WLW-005` Tamil sources, `WLW-006`
Chennai, `WLW-007` Raman. `WLW-011` was added after adversarial review, which
found the engineering row of this table had no register row behind it.
`WLW-001`, `WLW-008`, `WLW-009` and `WLW-010` are not table rows: they are the
baseline, the corpus-skew finding, the slot-fill conclusion and this
document's own status. The table is the readable form; the register is the
record.

| Candidate named in item 27 | Slot | Can the repository evidence it today? | Depth reached | Evidence |
|---|---|---|---|---|
| **Dholavira's water engineering** | 2 | **No.** The excavation reports are unreachable and every reachable account depends on them. | Secondary abstracts (Ghosh 2019, Houdas 2024, Asghar 2025) via `SRC-089`. No findspot, no context, no report locator. | `SRC-089`, `HOLD-007` |
| **Palaeoclimate** | 4 | **Partly — the only candidate that is.** Passage-level text with DOIs, from three articles. | Full-text chunks with DOI, journal, volume, pages; not the articles, not the figures, not the supplementary data. | `SRC-090`, `SRC-089` |
| **Engineering** (as a distinct strand) | 2, 4 | **No, and it is the strand most at risk.** What is reachable is modelling of ancient hydraulics by modern engineers — CFD reconstructions, hydraulic-gradient recomputation, Bernoulli-and-Pascal readings of Indus drains. | Abstracts. | `SRC-089` |
| **South Indian water infrastructure** | 2, 5 | **Barely.** One substantial reachable source (Mosse 1997, 389 citations) at abstract level, plus Coelho 2022 at passage level on *eris* in their urban phase. Nothing on tank construction, maintenance obligation or the epigraphy of donation. | Abstract; and passages on the modern phase only. | `SRC-089`, `SRC-090` |
| **Tamil sources** | 3 | **No.** No Tamil corpus lane exists in this repository and none was opened by these probes. | English-language articles *about* Sangam water vocabulary, in journals of unestablished standing. An article about a text is not the text. | `SRC-089`, `SRC-098` |
| **Chennai hydrology** | 5 | **Partly.** Passage-level text on the *eri* cascades, the 1876 colonial network, the 1980s Eri Schemes, the 2019 failure. | Full-text chunks with DOIs from three articles. | `SRC-090` |
| **Bhavani Raman's Chennai water work** *(named by name in item 27)* | 5, 3 | **No.** The host is refused at the gateway. | A search-result listing giving a title, venue and year, which `CLAUDE.md` forbids treating as a source. | `SRC-096`, `SRC-097`, `HOLD-007` |

### 6.1 The finding underneath the table

Three things, in order of how much they should change the plan.

**First: the one slot that is well-served is the one whose over-use is the
named failure mode.** Palaeoclimate is reachable at passage level. The
material and textual records that would constrain a climate-driven reading are
not. A WATER world built from what is reachable today would be an
environmental-determinist argument arrived at by availability, and it would
look rigorous, because the available material is quantitative and
high-prestige. This is not a hypothetical risk; it is the shape of the
evidence as measured.

**Second: the reachable corpus is systematically skewed and the skew is ours.**
The two working lanes are Consensus, which returns abstracts without DOIs, and
Scholar Gateway, whose corpus is Wiley. Neither reaches the Archaeological
Survey of India, Tamil-language scholarship, Indian university presses,
*Economic and Political Weekly*, or *Seminar*. So the material this repository
can reach on a South Asian water thread is disproportionately Anglophone,
Northern-published and engineering-framed. **Under method step 6 that is an
archive audit finding about the institution, and it belongs in slot 6 of the
world itself**, not in a methods footnote.

That skew is written up in full at `04-AUDITS/ARCHIVE-AND-POWER-AUDIT.csv`
`APA-W-001`, and §4.6 places the audit row itself in slot 6 of the world.

**Third: the item's own named source is unreachable.** Item 27 names exactly
one scholar, and `india-seminar.com` is blocked. The specification is
therefore written without the one piece of guidance the backlog was most
specific about, and it says so rather than proceeding as though the omission
were immaterial.

### 6.2 What this means for D-005

D-005 asks whether WATER is the first Living World. Its register row notes,
correctly, that *"No WATER research exists in this repository. Answering does
not commit any retrieval."* That is still true, and this unit adds one thing
to it: **a WATER world could be specified today and could not be filled
today.**

**No slot of the seven can be filled at the standard the constitution sets.**
Slot 6 is the only one with content requiring no external retrieval — the
record of our own reach — and even slot 6 cannot type its Indus absences,
because those need the excavation-coverage figures `APA-W-001` records as
unmeasured. `WLW-009`.

An earlier draft of this section, of §4.6 and of `WLW-009` said instead that
six slots were unfillable and the seventh was fillable, which was the one
positive buildability claim in the unit and was contradicted twice in the same
commit. `BF-025`. The unit also carried three different counts of the same
quantity — five, six and five, in `HOLD-007`, here and §11 — against inherited
standing rule 14, that counts are data-derived and never a running tally.
Reconciled to one: **seven of seven, with a qualified half of slot 6.**

That is not an argument against WATER. It is an argument that the build
sequence starts with the archive half of slot 6 and with slot 7, and that
typing the Indus absences is itself a retrieval task rather than a writing
task.

**And a two-slot world is not yet publishable, which the sequence has to
respect rather than route around.** §3.4 invariant 7: experience-object-model
§11.2 requires `traverses[]` non-empty with a minimum of two, and §11.3 rule 2
requires at least four postures crossed including Extraction / Collection or
Reconnection. Two filled slots yield at most two postures. So the recommended
first increment is an honest internal object that **fails experience-object-model §11.3 and should**;
it becomes a Living World when slots 2 and 3 arrive, and not before.

---

## 7. The two adversarial tests

Run on this document before it was committed, as `CLAUDE.md` requires.

### 7.1 Prestige-bias challenge

*Did this privilege a claim because it is canonical, Sanskritic, Brahmanical,
Indo-European, European, colonial, institutionally prestigious, repeatedly
cited or nationally useful?*

**Two findings, both corrected in place.**

1. **The pattern's default sequence puts the Indus first.** Slot 1's WATER
   candidate is Dholavira and slot 5's is Chennai, which places a Bronze Age
   northwestern site at the origin of a thread whose modern end is Tamil. That
   ordering is the standard Indian-history sequence and it is doing exactly
   the work item 27 warns about. **Correction:** M-8 requires that where any
   starting point is offered, one of them is slot 5 or slot 6, so the world
   can be walked from the present outward; and §4.2 names South Indian tank
   systems as a slot 2 candidate in their own right, not as a later stage of
   an Indus story.
2. **The reachable literature is prestigious in a way that flatters one
   reading.** Quaternary-science journals are high-prestige and quantitative;
   the material that would constrain them is in ASI reports and Tamil
   scholarship we cannot reach. An earlier draft of slot 4 read as though its
   being "well-served" were good news. **Correction:** slot 4 and §6.1
   now state the asymmetry as a finding against the world, and M-9
   makes it visible on the surface. Logged: this correction is `BF-024`'s
   neighbour and is recorded in §7.3 below rather than as its own row.

### 7.2 Preferred-counter-narrative challenge

*Did this accept a claim too easily because it is Dravidian, Indigenous,
anti-colonial, anti-Brahmanical, subaltern, diffusionist or politically
corrective?*

**Three findings.**

1. **"Colonial hydrology" is a framework, not a fact.** D'Souza 2006 proposes
   *colonial hydrology* as a conceptual category and is explicit that the
   third cluster of work it describes *"is yet to achieve visibility"* — i.e.
   it is a research proposal. *(`SRC-090` probe 1, chunk 0 of
   `10.1111/j.1478-0542.2006.00336.x`. That row's own constraint states the
   chunks arrive with markup stripped and characters mangled, "so quotation
   requires the published article", which `SRC-095` shows cannot be reached:
   this is a quotation of what was retrieved, and it may not go onto a page.)* Slot 5 could easily have adopted it as
   established. **Correction:** §4.5 requirement 4 states the archive audit as
   a requirement, and names no framework as its conclusion.
2. **The pre-colonial *eri* system is attractive as a lost commons and that
   reading is contested by the reachable literature itself.** Mosse 1997
   argues *against* the ahistorical "community management" construction of
   Tamil tank systems. A counter-narrative-friendly draft would have used
   Mosse's tank material and skipped his argument. **Correction:** §4.2,
   `WLW-004` and `HOLD-007` name Mosse specifically as an argument against the
   reading the world is likely to reach for.
3. **Slot 7's temptation is advocacy.** A water world ending in "act now" is
   politically corrective and evidentially unearned. **Correction:** §4.7
   requirement 3, explicitly.

### 7.3 Result, and the log rows that are owed

**An earlier version of this section claimed no `BIAS-FAILURE-LOG.csv` row was
owed**, on the ground that the findings were corrected before commit so there
was no `failed_output` and no `affected_claim`. That argument is wrong, and
this repository had already rejected it three times two commits earlier.
`BF-021` is exactly that case and is logged, with the reason stated in the
row: *"this failure was corrected before the first commit … It is logged
because `CLAUDE.md` and constitution §8 require the result of the test whether
or not it found anything."* `BF-022` and `BF-023` carry `affected_claims:
None` for the same reason, and museum framework §3.11 says the result is
logged either way. Reasoning a specification out of the log, in a repository
whose three most recent log entries were generated by a specification, would
have made the log decorative for exactly this class of unit.

**Two rows logged.**

- **`BF-024`** — prestige bias. The Tamil-studies results of the source probe
  were characterised as being *"in journals of unestablished standing"* and
  with *"no evident review"*, in `WLW-005` and in two places in this document.
  `SRC-089` recorded no such judgement: a citation count was converted into a
  peer-review judgement and applied to the one body of scholarship whose
  exclusion `APA-W-001` is about. §7.1 was run on this document and did not
  catch it. The ten items are now named and the judgement is removed.
- **`BF-025`** — method failure. The slot 6 buildability claim, described at
  §6.2.

**Two further findings recorded without their own rows**, because each is a
draft correction whose substance is now carried by `BF-024`'s and `BF-025`'s
controls: the Indus-first default ordering (§7.1, finding 1) and the "good
news" framing of slot 4 (§7.1, finding 2).

**`REAUDIT-QUEUE.csv`.** No new row. Three existing rows bear on this unit and
are named rather than duplicated: `RA-018` (every argument from absence, for a
stated search coverage — triggered by the two absence assertions corrected in
slot 6), `RA-019` (the prestige-bias test per brief, which already names
`the-water-city`, the page this unit feeds), and `RA-021` (museum framework §4.5 against V-8,
which M-3 depends on).

---

## 8. Falsifiers — what would change this specification

Per `CLAUDE.md` and museum framework §3.9. These attach to the design
propositions in §3 and §5, not to any historical claim.

| # | If this turned out to be true | What changes |
|---|---|---|
| F-1 | The seven slots cannot be filled for any second thread without adding or removing a slot | The pattern fails item 38's gate and is not a pattern. §9 is where this is most likely to be discovered. |
| F-2 | A visitor who walks the world with M-1 through M-10 in place still reports a continuous-tradition reading at the same rate as one who walks it without them | The mechanisms are decorative and the problem is not solvable in the interface layer. §5.1 item 1 already concedes this partially; a test would settle it. |
| F-3 | The four evidence classes in slots 1–4 turn out not to be independently datable for any candidate place — each depends on the others for its chronology | The through-line at §2.2 is false as stated, and WATER is one argument in four presentations rather than four records about one problem. |
| F-4 | Slot 6 renders as an appendix in practice despite M-2, because visitors do not reach it | M-2 is insufficient and slot 6 needs to be an entry point by default rather than optionally. |
| F-5 | The render-budget computation of M-9 turns out to drive editorial decisions rather than merely surface them | M-9 violates museum framework §3.10's deliberate refusal to let a metric settle allocation, and must be reduced to a review report. |
| F-6 | An allowlist change or a new corpus lane makes slots 2 and 3 richly fillable | §6.1's first finding is void, the evidence profile changes, and this document's build-sequence recommendation at §6.2 is wrong. **This is the falsifier most likely to fire**, and it fires on an administrative action, not a discovery. |

---

## 9. What a second Living World needs that this specification does not provide

Item 38's gate is *"the model can support a second water case without
rebuilding the interface."* This specification does not yet meet it. Seven
things are missing, and the first three are the real ones.

### 9.1 The admission vocabularies are written for water, not derived

§4 states each slot's evidence requirement partly in general terms and partly
in water's terms. Slot 1's requirement that the problem be dated independently
of the solution generalises cleanly. Slot 2's *"labour question on every water
work"* does not: it is `CLAUDE.md` §4V applied to hydraulic structures, and
FOOD's equivalent — who cultivated, who cooked, who was fed last — is a
different question with different archives.

**What is needed.** A `SlotAdmission` vocabulary per slot, expressed as
evidence classes and attestation modes rather than as subject-matter prose, so
that a second world declares its admissions rather than inheriting water's.
This document does not provide it and cannot: **one instance is not enough to
tell which parts of a template are the template.** That is the honest answer
and it is why D-053 matters.

### 9.1a A LANGUAGE world has no slot 1 and no slot 4, and an absence is the wrong way to say so

Found in adversarial review, by expressing two hypothetical worlds in the
seven slots. FOOD fits: slot 1 is subsistence and storage, slot 4 is
archaeobotany and climate, slot 2 is residue and querns, slot 5 is the modern
food system. **LANGUAGE breaks two slots outright.**

Slot 1 asks *"What did people have to solve?"* A language thread has no
problem being solved. Slot 4 asks what changed in the environment. Neither
slot is *unevidenced* in a LANGUAGE world; both are **inapplicable** — there
is no evidence class that could fill them.

Under §3.4 as first drafted, invariant 1 said all seven slots exist in every
world and invariant 2 said a slot with nothing filled and nothing typed is a
validation failure. A LANGUAGE world was therefore forced to mint a typed
`mk:abs:` record for a slot with nothing to be absent — **mistyping a category
mismatch as an absence of evidence**, which is the error `SRC-088` was written
to avoid and which museum framework §3.7's eight types have no entry for.

**What is needed, and what is now provided.** §3.3 gains an `inapplicable`
field, boolean with a required reason, and §3.4 invariant 2 is satisfied by
`inapplicable = true` as well as by an absence. That is a repair, not a
solution: **whether a pattern two of whose seven slots do not apply to
LANGUAGE is one pattern or two is exactly what building the second world
decides**, and this document cannot answer it from one instance. §9.4 bullet 1
and bullet 2 are near this and are not it — both assume the absences are
evidence absences and the slots separable-but-collapsing, not inapplicable.

### 9.1b The slot-domain vocabulary is not the bridge-domain vocabulary

§3.2's *"Domain of its content"* column uses *environment*, *settlement*,
*place*, *text* and *the archive itself*. museum framework §4.4's seven domains are **language ·
ancestry · culture · artifact · religion · polity · modern identity**.

The two vocabularies do not meet, and two rules in this document depend on
their meeting. Slot 4's requirement 3 names an `environment→culture` bridge —
a `bridge_type` that cannot exist in museum framework §4.4's enum. M-6's transitive-closure
rule is defined over domain boundaries and cannot be evaluated at all for
slots 1, 4 and 6.

The slippage is inherited: museum framework §10.2 constraint 2 has it too, in the sentence this
document quotes. So it is logged as `IC-W-003` and referred rather than
patched here — a specification is not entitled to extend the framework's
domain enum on its own authority. **Until it is resolved, any slot 1, 4 or 6
link is treated as unevaluable rather than as permitted**, which is the
conservative reading and the one M-6 exists for.

### 9.2 The seam rule is water-specific in its risk profile, and may be wrong elsewhere

M-5 treats the slot 4 → slot 5 seam as the highest-risk edge because in a
water thread the ancient-to-modern juxtaposition is the temptation. In
LANGUAGE it is not: language's highest-risk edge is slot 3 → slot 5, where an
attested ancient form meets a modern speech community, and that is a
`language→modern-identity` bridge which is more politically loaded than
anything in WATER. In FOOD the risk is slot 2 → slot 5, where a Bronze Age
lipid residue meets a living cuisine — item 39's gate names exactly this:
*"Living cuisine is not used as automatic proof of Bronze Age cultural
continuity."*

**What is needed.** The seam rule generalised: **every world declares its
highest-risk edge, and the declared edge gets M-5's break-on-no-bridge
treatment.** The mechanism is right; hard-coding it to one seam is wrong. This
is a change to §5 that a second world will force, and stating it now is
cheaper than discovering it.

### 9.3 There is no test that the interface did not move

The gate is that a second case works *without rebuilding the interface*. That
is a testable proposition and this document gives no test for it.

**What is needed.** A stated acceptance criterion, in the form: a second world
is admitted when it can be expressed entirely as (a) seven slot records, (b)
a through-line claim set, (c) declared admissions, (d) a declared highest-risk
edge, and (e) references to Exhibits that exist independently — **with no new
field, no new render component, and no new mechanism.** Any of those five
requiring an addition is the gate failing, and the addition is the finding.
Until that criterion is written down, "without rebuilding the interface" is a
judgement call, and a judgement call is what a gate is supposed to replace.

### 9.4 Four smaller gaps

- **No worked absence-type mapping per slot.** Slot 3's absences are corpus
  absences and slot 2's are excavation absences; the eight types apply
  differently and the mapping is not written.
- **No rule for a world whose slots overlap.** In LANGUAGE, slot 3 (text and
  language) and slot 2 (material evidence) are the same object when the object
  is an inscription. The pattern assumes they are separable and does not say
  what happens when they are not.
- **No cross-world rule.** WATER and FOOD both reach Indus material. Whether
  two worlds may traverse the same Exhibit, and what a visitor sees when they
  do, is unspecified. Experience-object-model §11.3 rule 1 implies they may —
  the Exhibit stands alone — but the visitor's experience of arriving at the
  same Exhibit under two different through-lines is not designed.
- **Entry into an empty slot is not expressible.** M-8 wants a visitor to be
  able to start at slot 6. Experience-object-model §11.2 types a Journey's
  `entry_points[]` as an array of `mk:exh:`, and an unfilled slot has no
  Exhibit. Either the object model widens that type or no Living World can
  offer entry at a slot it cannot fill — which is the entry point this pattern
  most wants, since slot 6 is the slot most often unfilled.
- **No specification of the world's own export shape.** experience-object-model §11.2 gives Journey an
  `export_profile`; what a Living World's export contains — through-line,
  seven slots, absences, fill profile — is not stated, and the fill profile is
  the part a second world's reviewer would most want.

### 9.5 What this section is not

It is not a list of reasons to defer. Most of the items above are discovered
by building the second world, not by specifying harder. §9.3 is the exception:
the acceptance criterion should be written **before** the second world is
chosen, because a gate written after the candidate is known is not a gate.

**And this section's headline result is a register row, not prose.** That
*"this specification does not yet meet"* item 38's gate is the unit's own
negative finding about itself, and `BF-011`'s control in
`04-AUDITS/BIAS-FAILURE-LOG.csv` is that a finding appearing only in prose has
been demoted. It is `WLW-012` in
`03-REGISTERS/water-living-world-readiness.csv`, at `HYPOTHESIS`, with
falsifier `F-1`.

---

## 10. What this leaves to the owner

| Decision | Status | What it blocks here |
|---|---|---|
| **D-005** — Is WATER the first Living World? | `OPEN` | Nothing in this document. §6.2 gives the evidence position the answer would be made against, which is what the row asks for. |
| **D-053** — Which Living World is built second? | `OPEN`, raised here | Nothing today. §9 is written to be true under any answer, and recommends FOOD or LANGUAGE over a second water case, because a second water case tests only that the slots refill. |
| **D-054** — May the modern slot name a live Chennai dispute? | `OPEN`, raised here | Slot 5, and only slot 5. Written up in `DECISIONS-NEEDED.md`. |
| **D-001** — the egress allowlist | `OPEN` | Slots 2 and 5 partly. `india-seminar.com`, `doi.org` and `hess.copernicus.org` added to the request by this unit. |
| **D-003** — which literature connectors | `OPEN` | The source-genealogy audit for slot 2, via Scite's exhausted quota. |
| **D-010** — the accepted-publication threshold | `OPEN` | Publication of any Exhibit in any slot, per experience-object-model §7.4.1. Not re-raised. |
| **D-015** — seven postures or six | `OPEN` | Nothing. Experience-object-model §11.3 already writes the four-posture rule to survive either answer. |

No new escalation beyond D-053 and D-054. The Tamil-corpus gap at §4.3, the
unmeasured source genealogy at §4.2, the untyped absences at §4.6 and the
reachability re-audit at §6.1 are research-programme scheduling matters, not
owner decisions. They are queued under *Opened by the WATER Living World
specification* in `RESEARCH-QUEUE.md`.

---

## 11. Status of this document

Every design proposition in it is `HYPOTHESIS`. Every statement about backlog
items 27 and 38 is `INHERITED-UNVERIFIED` and quoted. Every statement about
this repository's retrieval reach is `VERIFIED` against the `SRC-` row cited
beside it. No historical claim is asserted anywhere in it, and no register row
was promoted by writing it.

It is a specification, not a build authorisation. Under
`13-PRODUCT-ARCHITECTURE/authoritative-programme/execution-queue.csv` it sits
before Q08 (the WATER record programme) and Q09 (the WATER storyboard), and it
does not discharge either: Q08's stopping condition is *"Every chain link has
record or explicit unknown"*, and §6 of this document shows that **no** slot
of the seven currently has a record, and that the explicit-unknown half is
itself blocked for the Indus absences by the missing excavation coverage
(`WLW-009`, `APA-W-001`).

**Repository scope, restated.** Nothing here is site code. `CLAUDE.md`: *"The
website lives in `melakeela/site`. Never write site code here."* Whether
product specification belongs in this repository at all is `D-012`, `OPEN`;
this document is placed alongside the two specifications already here and
inherits their position rather than settling the question.
