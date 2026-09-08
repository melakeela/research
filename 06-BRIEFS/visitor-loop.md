# The smallest complete visitor loop — specification

**Artefact class:** specification. Not research, not public copy, not site code.
No sentence in this file may be lifted onto a page.
**Directory:** `06-BRIEFS/`, alongside the other briefs; the object specified is
a route through exhibits, not an exhibit.
**Written:** 2026-09-08.
**Governing documents:** `13-PRODUCT-ARCHITECTURE/museum-framework.md` (every
design proposition in it is `HYPOTHESIS` by its own §14.4);
`01-INHERITED/curatorial-audit-v1.1/environment-map.csv`
(`INHERITED-UNVERIFIED`); `00-CONTROLLER/METHODOLOGY-CONSTITUTION.md` §5 step 14
and §12; `CLAUDE.md`.
**Status of every design statement below:** `HYPOTHESIS`, inherited from the
framework. Status of every statement drawn from the curatorial audit:
`INHERITED-UNVERIFIED`. Statuses of the content the loop displays are given
individually in §7 and are not inherited from this file.
**Retrieval:** none was performed for this unit. No row was added to
`02-SOURCES/access-ledger.csv`. No claim moved status. No domain was requested.

---

## 0. Standing controls this unit ran against, and the boundary it rests on

**`RESEARCH-QUEUE.md` `## Not yet` lists "Product and institutional
specification (§12) — pending `D-012`", and lists "Anything touching
`melakeela/site`".** `DECISIONS-NEEDED.md` **`D-032`** ends *"Nothing in this
repository acts on the MVP set until this is answered."* The loop's arrival
screen is `index`, which is MVP rank 1.

This unit was produced on the owner's instruction, given in the session of
2026-09-08. **That instruction is not registered as an owner decision and no
`D-` is allocated for it**, following the precedent set and argued in
`06-BRIEFS/mvp-fifteen/README.md` §0: an instruction to carry out a piece of
work is not a standing decision that the work may precede its queue position,
and treating it as one would put an unverifiable authority into the decision
namespace.

The boundary this unit rests on, drawn explicitly:

- It **specifies a sequence**. It schedules no launch, approves no page, orders
  no work, allocates no budget, and assumes no answer to `D-012` or `D-032`.
- It **writes no site code**, per `CLAUDE.md`'s standing prohibition and §12's
  closing line. There is no markup, no CSS and no script below; where a
  behaviour needs naming it is named as a behaviour.
- It **does not touch `melakeela/site`**. On the contrary, §6.3 below turns the
  fact that the live page cannot be read from this session into a displayed
  element rather than working around it.
- Nothing here promotes a claim, because nothing here retrieved anything.

**And the boundary may not hold.** If the owner reads specifying a route
*through* `index` as acting on the MVP set, the correct disposition is that this
unit waits on `D-032` with the rest. §9 names the one substitution that would
detach the loop from `index` entirely, so that reading is cheap to act on.

---

## 1. What is being specified

**One loop.** One arrival, one investigation, one moment of genuine uncertainty,
one exit that leaves the visitor able to return. Five screens. Four postures,
one of them entered twice. Source Mode reachable in one interaction from all
five, per framework §1.7.

**Smallest** means: remove any one of the five screens and the loop stops being
complete — it loses either its arrival, its investigation, its uncertainty or
its return. §10 states the removal test screen by screen.

**Complete** means: the visitor arrives knowing nothing, leaves knowing (a)
something the institution has established, (b) something the institution has
*not* established, (c) the evidence for both, and (d) how to come back and find
out whether either has changed.

**The subject is one word.** *varṇa* in the Rigveda, and its twenty-three
occurrences. The loop does not change subject between stops. That is deliberate
and is the load-bearing design decision of the whole specification: see §3.

**Why this subject, stated before anything else.** It is the only subject in
this repository that carries a dense set of `VERIFIED` claims, a `HYPOTHESIS`
that names exactly what is missing, an owed-work record with a date, a logged
method failure on one of its own rows, and a live MelaKeela page whose central
public claim outruns all of it. No other body of work here has all five. **It is
also, and this must be said in the same breath, a Vedic Sanskrit subject on a
Tamil-named platform, and it was chosen partly by the egress policy** —
`04-AUDITS/ARCHIVE-AND-POWER-AUDIT.csv` `APA-E-003` records that this session's
retrieval channel reaches what exists as a public git repository and nothing
else, that VedaWeb does and the Dravidian comparative literature does not, and
that the resulting split *"follows the retrieval channel rather than the
evidence."* `HOLD-002` to `HOLD-005` are the receipts. Logged as `BF-021`.

---

## 2. The thesis the loop is built on

`01-INHERITED/curatorial-audit-v1.1/environment-map.csv`, second line
(`INHERITED-UNVERIFIED`):

> *"Themes change with the visitor's relationship to knowledge; the
> institutional shell remains stable."*

Framework §1.1 reads the seven environments as seven **relationships between a
visitor and a body of knowledge** rather than seven subjects, and §1.2 gives
four structural consequences, of which two govern this loop:

- **C-1, posture survives revision.** A page moved between postures has changed
  only what the institution can presently say about it; the content need not
  change at all.
- **C-2, posture is the visitor-facing consequence of a claim set's status
  distribution**, computed by §1.5's derivation and then confirmed or overridden
  editorially with the override logged.

**What this implies for a loop, and it is not obvious.** If postures were
subjects, a loop would be a tour: five topics, five rooms. Because postures are
relationships, a loop is a **sequence of relationships to one body of
knowledge** — and the only way to demonstrate that inside the loop itself is to
**hold the subject constant and let the posture change**. A loop that changed
topic at every stop could not distinguish "the posture changed" from "the
subject changed", and the thesis would be untestable in the one artefact built
to express it.

So: one word, four postures, five screens.

---

## 3. The postures the loop passes through, in order, and why in that order

| # | Screen | Posture | The visitor's relation to the knowledge | Framework basis for the assignment |
|---|---|---|---|---|
| S1 | Arrival | **Nocturnal Veḷi** | *not yet known* | §6.6 — Nocturnal Veḷi is the Question route's default posture |
| S2 | Investigation | **Living Signal Field** | *known by relation* | §6.4 — Living Signal Field is the Word route's default posture; §1.5 rule 4 |
| S3 | The argument | **Tamil Retrofuture** | *known against an official account* | §1.5 rule 6; page-audit assigns `what-varna-meant` this environment (`INHERITED-UNVERIFIED`) |
| S4 | The uncertainty | **Nocturnal Veḷi** | *not yet known — and now we can show you why* | §1.5 rule 3, absence dominance. **Derived, not chosen** — see §3.4 |
| S5 | Exit | **Reconnection** | *knowable again* | §1.6.2 — the correction ledger is a Reconnection surface; §9.4 |

### 3.1 Why Nocturnal Veḷi first

Because the visitor's relationship to this knowledge at the moment of arrival is
*not yet known*, and any other opening posture asserts something before the
visitor has seen anything. Framework §6.6 makes Nocturnal Veḷi the Question
route's default for exactly this reason, calls the Question route *"the
institution's honest surface"*, and rules that *"open questions may outnumber
answered ones and this is not a defect."* The formulation that carries the
screen is `06-BRIEFS/mvp-fifteen/04-veli.md` §1's, in its step-14 table:
**a question asserts nothing.**

The alternative openings and why each fails: opening in Living Signal Field
hands the visitor a distribution before they know what is being distributed;
opening in Tamil Retrofuture hands them the counter-account before the
measurement, which is the preferred-counter-narrative failure expressed as
navigation; opening in Reading Room prejudges `D-015`, which asks whether
Reading Room is a posture at all.

### 3.2 Why Living Signal Field second

Because the first thing this institution can honestly give a visitor about
*varṇa* is **relations, not meaning**: twenty-three tokens against metrical
strata, against books, against the compound boundary. Framework §1.5 rule 4
assigns Living Signal Field where an exhibit's substance is relationships rather
than claims, and §6.4 makes it the Word route's default.

It is also the only stop at which the visitor's own action produces a result
that **reproduces a `VERIFIED` claim** — group the table by stratum and you get
`VAR-005`; group by book and you get `VAR-006`. That reproduction is the
loop's proof that the institution's numbers are real, and it must happen before
S4 asks the visitor to believe that a different number does not exist.

### 3.3 Why Tamil Retrofuture third

Because only now does the visitor have enough in hand to be shown that the
institution is arguing **against** something. Framework §1.7 makes Investigation
Mode — PROVE IT — **mandatory** in Tamil Retrofuture, and gives the reason:
these are the postures *"where the institution is arguing against something"*
and PROVE IT *"is the mechanism that keeps the argument falsifiable rather than
rhetorical."*

That mandatory pairing is why this posture cannot be moved earlier in the
sequence. Tamil Retrofuture without the measurement behind it is the environment
map's own `Avoid` for the row — *"No kitsch, fake Tamil or neon overload"* —
in argumentative rather than visual form.

### 3.4 Why Nocturnal Veḷi again, fourth — and why this is derived rather than staged

This is the loop's structural argument and it needs stating carefully, because
"return to the opening posture" is the kind of symmetry a designer reaches for
whether or not the material supports it.

**It is derived.** Run framework §1.5's derivation over the claim set S4
displays. Rule 1 (withheld access) does not fire: the central claims do not
depend on material whose access status is `NOT ACCESSIBLE`. Rule 2 (repair
state) does not fire. **Rule 3 fires**: the exhibit's load-bearing proposition —
*what do these twenty-three occurrences mean* — resolves to a typed absence
rather than to a positive claim. Derived posture: **Nocturnal Veḷi**.

**The inherited assignment disagrees.** `page-audit.csv` assigns
`what-varna-meant` to **Tamil Retrofuture** (`INHERITED-UNVERIFIED`). Framework
§1.5 requires that divergence to be written to the Editorial Register (§11.5) as
`derived_posture` / `assigned_posture` / `override_reason` / `decided_by` /
`decided_date`, and that *"an override with an empty reason is invalid."*
**That register does not exist in this repository** — `SCHEMA.md` §7 records
that nothing in `03-REGISTERS/` records an environment assignment — so the
divergence is recorded here instead, and creating the register is `W-1` in §8.

**And the divergence is the loop, not a defect in it.** The page is Tamil
Retrofuture *as published* — it makes a counter-claim against an official
account. It derives as Nocturnal Veḷi *on its evidence*. The loop passes through
both, in that order, and the gap between them is the thing the loop exists to
show. S3 is where the page currently stands; S4 is where its claim set actually
sits.

**The same posture means something different on the way out.** At S1 the unknown
is the visitor's: they do not yet know what *varṇa* means in the Rigveda. At S4
the unknown is the institution's: nobody here knows either, and now the visitor
can see the table where the not-knowing lives. The environment map's claim that
a posture describes a *relationship* rather than a topic is only demonstrated if
one posture can be occupied twice, with different content, under the same
discipline. This loop is the demonstration.

### 3.5 Why Reconnection last

Because framework §9.4 makes PROVE IT *"the public intake for the correction
process"* and *"the reason the Reconnection posture has a correction ledger to
display"*, and §1.6.2 lists the correction ledger's public face among
Reconnection's seven surfaces. A visitor who has just worked a claim and may
disagree with it is standing in the correction pipeline whether or not the
institution says so; Reconnection is the posture that says so.

The exit is governed by that row's `Avoid` — *"Digitization is not
restitution"*, which framework §1.6.2 calls *"the governing rule of the whole
environment"*. Generalised to this loop: **an intake receipt is a record of a
state, not a repair.** §6.5 specifies what the exit may and may not say.

### 3.6 The three postures the loop does not pass through, and why not

Named because a loop that silently omits three of seven postures is making an
unstated claim about them.

- **Living Tiṇai** (*known through place and material*). §1.5 rule 5 requires
  place or material dominance and a Place anchor. `PUR4J-018` (`VERIFIED`)
  records that the pinned corpus *"contains no geographic content of any
  kind."* A place surface on this subject would be fabricated, and the row's
  own `Avoid` — *"No generic landscape decoration"* — names the failure.
- **Extraction / Collection** (*known but withheld*). The sense absence is typed
  `NOT PRODUCED`: the Zurich annotation was not built to record sense
  (`VAR-004`, `VERIFIED`). **Nobody withheld it.** Dressing a `NOT PRODUCED`
  absence as extraction is precisely the *"unsupported allegation"* the row's
  `Avoid` forbids. The one genuine access failure in range is the institution's
  own — it cannot read its own live page (`SRC-086`) — and the loop displays
  that at S4, in Nocturnal Veḷi, as a limit on its own ignorance-claim rather
  than as a grievance.
- **Reading Room** (*known by argument from sources*). Under framework §1.6.1
  Reading Room's substrate role is **Source Mode**, which is mandatory on all
  five screens and reachable in one interaction from each. The loop therefore
  uses Reading Room as a *mode*, continuously, and not as a *stop*. Making it a
  stop would prejudge `D-015`, which asks whether it is a peer posture at all.

---

## 4. The anchor object

`mk:qst:varna-23` — a Question node, framework §6.6.

**Proposition, exactly as the corrections brief already drafted it**
(`CORRECTIONS-PENDING.md` brief 4 §4.4, `QUESTION`):

> How often does *varṇa* appear in the Rigveda, and what does it mean there?

**Scope, per constitution step 1 and framework §6.6.** Corpus: the Rigveda at
the pinned commit `d3eb8af` of the VedaWeb data repository (`SRC-019`). Unit:
the token, assigned to the simplex lemma `lemma_varRa_7738`. Evidence classes
required: textual, linguistic. Terms needing original-language work: *varṇa-*
itself, and — under constitution §7's inherited-category list — the English
words *caste*, *colour* and *class*.

**Date range: not stated.** No register in this repository carries a Date
Assertion for the Rigveda. Framework §2.7 makes dates plural and typed, and §6.5
forbids a text displaying a single date; the honest consequence for a Question
node whose corpus has no registered dates at all is that **the arrival names the
corpus by its pinned edition and not by a period.** A screen that opened with
"c. 1500 BCE" would be stating a claim no row in this repository supports.

**Viable explanations and the null**, both required by §6.6 and both displayed at
S3: see §6.3.

---

## 5. Modes, and the invariant that runs under all five screens

Framework §1.7's matrix, for the four postures the loop uses:

| Posture | Source | Atlas | Investigation | Field | Classroom |
|---|---|---|---|---|---|
| Nocturnal Veḷi | mandatory | available | available | available | available |
| Living Signal Field | mandatory | mandatory | available | available | available |
| Tamil Retrofuture | mandatory | available | **mandatory** | available | available |
| Reconnection | mandatory | available | available | forbidden | available |

**Source Mode is mandatory on every screen and is reachable in one
interaction**, per §1.7's first rule and §6.7's first cross-route invariant.
Concretely, on each of the five screens: a persistent control that opens the
claim rows, statuses, locators, retrieval dates, source genealogy, absences,
falsifiers and revision history behind whatever is on screen, without leaving
the screen's position in the loop.

**Investigation Mode is mandatory at S3** and is the whole of that screen.

**Atlas Mode is mandatory in Living Signal Field** (§1.7) and is the one place
this loop knowingly departs from the matrix: S2 presents a table, not an atlas.
The departure is recorded rather than hidden. Framework §8.2 makes the Atlas a
view over the object graph and §8.7 lists what it may never do; a
twenty-three-row lexical distribution with no geography (`PUR4J-018`) has
nothing to place on a map, and forcing one would violate §8.7 to satisfy §1.7.
**This is a defect in the matrix, not in the loop**: "mandatory" in the Atlas
column cannot hold for a Living Signal Field exhibit whose relations are not
spatial. Recorded in §11 as a finding against the framework.

**Field Mode is forbidden at S4 by this specification**, extending the principle
of framework §10.4.6. Field Mode is *available* in Nocturnal Veḷi under §1.7,
and this loop declines it at S4: a child may not be handed "decide what *varṇa*
means here" as a Field Bag task when no adult in this institution has done the
reading. This is a proposal, not an existing framework rule, and it is written
as one.

---

## 6. The five screens

Each screen below gives: the surface, what it displays, what the visitor can
do, the rules the surface runs under, and the `Avoid` check for its posture.

---

### 6.1 S1 — ARRIVAL

**Surface.** `index`, the threshold, resolving immediately to the Question node
`mk:qst:varna-23`. Posture **Nocturnal Veḷi**; environment map function
*"Threshold, deep time, unknowns"*, desired effect *"Vastness without menace"*
(`INHERITED-UNVERIFIED`).

**Displays.**

1. The question, in full, as §4 states it.
2. `VAR-001` (`VERIFIED`) — the word occurs **23 times** in the Rigveda, in 23
   stanzas and 21 hymns — with its status badge, its source ids and its
   retrieval date `2026-09-07` visible on the face of the screen, not behind a
   control.
3. The corpus, named by edition and commit, not by date. §4.
4. Nothing else. No image. No second claim. No navigation menu.

**Actions.**

- **`Begin`** → S2.
- **`Sources`** → Source Mode on the Question node. What Source Mode shows here
  is short and is the point: `SRC-019`, `SRC-022`, `SRC-023`, `SRC-085`, and the
  fact that **no Date Assertion for the Rigveda exists in any register**. The
  visitor learns at the arrival screen that the institution will tell them what
  it has not got.

**Rules.**

- **The arrival asserts one claim and it is `VERIFIED`.** A question asserts
  nothing (§3.1); the count is offered beside it as the size of the evidence,
  not as an answer.
- **The arrival does not preview S4.** The openness at S1 lives in the question's
  second clause — *"and what does it mean there?"* — not in an announcement that
  the institution does not know. Saying it here and showing it at S4 would make
  S4 a restatement; the loop's arc is the difference between saying and showing.

**`Avoid` check — *"No fantasy portal or occult styling."*** The restraint here
is a content restraint before it is a visual one: one question, one number, one
edition, one control. Vastness is earned by the corpus being 164,758 tokens
(`PUR-001`, `VERIFIED`, reachable in Source Mode) and the answer being 23, not
by treatment.

---

### 6.2 S2 — INVESTIGATION

**Surface.** The Word route, `mk:lex:varna` (framework §6.4). Posture **Living
Signal Field**; function *"Relationships, movement, comparison"*, desired effect
*"Connected evidence"* (`INHERITED-UNVERIFIED`).

**The screen is one table.** All twenty-three occurrence rows from
`03-REGISTERS/rigveda-varna-occurrences.csv`, `VAR-OCC-001` to `VAR-OCC-023`,
with their real columns: stanza, pada, token index, surface form, lemma,
morphology, Arnold stratum, stratum certainty. The visitor is looking at the
register, not at a rendering of it.

**Displays.** `VAR-001`, `VAR-005`, `VAR-006`, `VAR-007` (all `VERIFIED`);
`VAR-002` (`PROVISIONAL`); `PUR-001`, `PUR-002`, `PUR-011`, `PUR-012`, `PUR-013`
(all `VERIFIED`); `PUR-028` (`HYPOTHESIS`). Non-claim records: `VAR-OCC-001` to
`VAR-OCC-023`; `DEP-001`, `DEP-002`, `DEP-024`; `APA-E-006`.

**Actions.**

- **a. Group by Arnold stratum.** Result: Archaic 4, Strophic 4, Normal 8,
  Cretic 6, Popular 1. The visitor has just reproduced `VAR-005` (`VERIFIED`)
  from the rows.
- **b. Group by book.** Result: book 1 six, book 2 six, book 3 two, book 4 one,
  book 9 six, book 10 two; books 5, 6, 7 and 8 carry none. That is `VAR-006`
  (`VERIFIED`).
- **c. Show stratum certainty.** Three of the twenty-three rows —
  `VAR-OCC-002`, `VAR-OCC-013`, `VAR-OCC-014` — read
  `metrical-variations-only`, not `certain`. `PUR-011` (`VERIFIED`) is what
  makes that column readable: Arnold's letters set in small italics mean the
  period is indicated by the metrical variations alone. `PUR-012` (`VERIFIED`)
  gives the scale — 945 of 10,552 stanzas are lowercase-coded corpus-wide.
- **d. Show the compound boundary.** `VAR-007` (`VERIFIED`): a further **23
  tokens** in **12 distinct compound lemmas** built on *-varṇa-*, headed by
  *híraṇyavarṇa-* "gold-coloured" with 9. Rendered **outside** the 23, in a
  visibly separate register, because the simplex and the compounds are the same
  size and a reader who is not told will merge them.
- **e. Open any row in Source Mode** at its locator —
  `mk:txt:rigveda#01.073.07d` for `VAR-OCC-001` — giving §7.1's stack:
  transcription, the padapatha reading, and the bundled translations, each
  labelled by `is_primary` so the visitor can count the steps between the token
  and the English.

**Rules.**

- **A visitor-generated grouping is a query result, not a claim.** Framework
  §7.2.4 requires every result set to carry its query, its facets, its date and
  its base revision. Actions (a) and (b) reproduce registered claims and are
  labelled with the claim id they reproduce; any *other* grouping the visitor
  builds is returned as an addressable, exportable query over
  `VAR-OCC-001..023` and is **not** given a status badge, because it has no
  register row. This is the distinction that lets the surface be freely
  explorable without manufacturing claims.
- **No distributional inference is computed, at any grouping.** At n = 23 the
  expected count is below 6 in all five stratum cells. `CORRECTIONS-PENDING.md`
  brief 4 §4.2.4 states this and states the consequence: the numbers are
  reported as measurements and nothing more. The grouping control therefore
  renders counts and **no test statistic**, and carries that sentence.
- **Arnold's strata are not dates, and the surface says so at the control, not
  in a footnote.** `PUR-028` is a `HYPOTHESIS` — *"Arnold's five periods
  correspond to real chronological stages of composition"* — and it is
  untested. `APA-E-006` is displayed beside the grouping control, not in Source
  Mode: Arnold, Cambridge 1905, *"working within the philological assumptions of
  his period"*, and *"whether the metrical layering tracks composition date at
  all is an assumption inside the instrument, not a result from it."* The
  control is labelled **"group by Arnold's periodisation"**, never "by period".
  This placement is a correction made under `BF-021`; see §11.
- **Four source ids, one source.** The grouping controls cite `SRC-019`,
  `SRC-022`, `SRC-023` and `SRC-085`. The screen displays `DEP-024` — those are
  *"the same repository at the same commit `d3eb8af`, fetched a third time…
  The three count as ONE source"* — and `DEP-001`, which makes `SRC-023` a
  transcription of `SRC-026` (Arnold 1905) rather than a second witness to it.
  Framework §9.2 stage 3 calls the independence tree *"the single most
  instructive thing this mode can teach"*; this loop teaches it one screen
  early, because S2 is where the visitor is being persuaded that the numbers
  hold.
- **A word never carries a people.** Framework §6.4. No ethnic, ancestral or
  modern-identity label appears anywhere on this screen, in any grouping, in any
  export. On *this* word that rule is not a formality: the whole loop exists
  because the eighth gloss in the standard lexicon is *Kaste*.

**`Avoid` check — *"No gaming HUD or arbitrary links."*** The only links out of
this screen are Evidence Links with roles (framework §3.3) and Source Mode at a
locator. No "related words", no score, no progress bar, no completion state.

---

### 6.3 S3 — THE ARGUMENT

**Surface.** A PROVE IT run (framework §9) anchored on `VAR-009`. Posture
**Tamil Retrofuture**; function *"Counter-history, public energy, learning"*,
desired effect *"Spunky cultural memory"* (`INHERITED-UNVERIFIED`). Investigation
Mode is **mandatory** in this posture (§1.7).

The run's six stages, per §9.2:

**Stage 1 — the proposition.** `VAR-009` (`HYPOTHESIS`): *"The 23 occurrences of
varṇa- divide into a human-applied group and a non-human group."* Scoped
exactly: the simplex lemma `lemma_varRa_7738`, at commit `d3eb8af`, 23 tokens.

**Stage 2 — the rivals, and the loop's first honesty crux.**

1. `VAR-009` as stated.
2. **The null explanation** — the 23 do not divide; the word carries one sense
   across them. Listed, and per §6.6's rule **not last by default**.
3. **The official account** — that Rigvedic *varṇa* already carries a social or
   caste sense.

**Rival 3 has no Claim Object in this repository.** It exists here only as
`VAR-003` (`VERIFIED`): Grassmann glosses *varṇa-* with eight senses in a single
undivided string — *Farbe, Stamm, Art, Gattung, Partei, Menschenart, Stand,
Kaste* — and *"assigns none of them to any particular occurrence."* The eighth
is a nineteenth-century lexicographer's interpretive category, and constitution
§7 lists *caste* among the inherited English categories to be audited before
use.

So the screen states, in the institution's own voice: **we cannot state the
rival account from our register, because we have not registered it.** It is not
smoothed over, not replaced by a strawman, and not omitted. The reason is
displayed: `APA-E-003` types the relevant secondary literature — Witzel 1999,
Kuiper 1991, Masica 1979, Krishnamurti 2003, Rau 2019, Shorto 2006 — as **`NOT
ACCESSIBLE`**, structurally, because *"attested and reconstructed families have
machine-readable derivatives on GitHub; proposals about unattested donors do
not."* Registering rival 3 is `W-4` in §8 and is partly blocked.

**Stage 3 — the evidence.** The 23 rows from S2, carried forward; `VAR-003`'s
eight glosses; the nine translations bundled with the corpus, `SRC-072` to
`SRC-077`. The independence tree from S2 is shown again here, in its proper
place.

**Stage 4 — the gates, and two of five are unavailable.**

| Gate | Available here | Why |
|---|---|---|
| Chronological | **no** | `PUR-028` is a `HYPOTHESIS`; Arnold's letters are not dates, and `DEP-001` makes them single-sourced besides |
| Geographical | **no** | `PUR4J-018` (`VERIFIED`) — the pinned corpus carries no geographic content of any kind |
| Mechanism | yes | a semantic split is a proposition about usage; the mechanism is stated and testable against the passages |
| Positive evidence | yes | the 23 passages and the nine translations |
| Diagnostic predictions | yes | `VAR-009` predicts that translators cluster; that is checkable |

**The surface displays the two unavailable gates as unavailable**, with the
claim id that makes each so. A visitor who applies a gate differently from the
institution has that recorded (§9.4) and it is carried to S5.

**Stage 5 — the absences.** Hands off to S4. Framework §9.2 calls this *"the
stage most likely to change a visitor's mind and the one most museums omit"*;
this loop gives it a screen of its own rather than a panel, which is the single
biggest structural decision in the specification.

**Stage 6 — the falsifier.** `CORRECTIONS-PENDING.md` brief 4 §4.4's
`WHAT WOULD CHANGE IT`, in its own terms: the sense reading, *"done and
published with the passages, the competing translations and the reasons for each
choice."* Currently testable: **yes**. Blocked by: nothing but the work. That
last line matters and is displayed — this is not a hold, it is an undone job.

**Both adversarial tests are visible on this screen** (framework §3.11), and the
second is the one that bites.

- **Prestige-bias challenge**, run on the loop's own instruments: every
  instrument in this loop is European philology — a German lexicon (Grassmann),
  a British metrist (Arnold 1905), a Swiss annotation layer (Zurich). `APA-E-006`
  is displayed.
- **Preferred-counter-narrative challenge**, run on MelaKeela: the page's central
  public claim is *"Varṇa means colour. It never means occupation"*
  (`page-audit.csv`, `INHERITED-UNVERIFIED`). **That is a universal negative
  over 23 passages nobody in this institution has read for sense.** The screen
  says so.
- `IH-149` (`INHERITED-UNVERIFIED`) is displayed beside it: the owner already
  **rejected** leading with *varṇa* as "the colour of a dawn" — correction
  `R-03` — with the standing rule *"both halves in the same breath, the
  indictment first, nuance after, never as a replacement."* A sense sort built
  from Grassmann's gloss lands on colour first by construction. The institution
  shows the visitor the rejection it already issued against itself.
- The **asymmetry statement** (framework §11.2) rides with the pair, so the two
  challenges are not presented as balanced. `CLAUDE.md`: *"Correct both without
  pretending their archival and institutional power has been equal."*

**The live page cannot be quoted as retrieved.** `SRC-086`'s blocking constraint
reads: *"It says nothing about what what-varna-meant.html holds:
`melakeela/site` is not accessible from this session."* The phrase *"sorted by
sense"* reaches this repository through the instruction that commissioned brief
4, and brief 4 §4.1 states in terms: *"This repository holds no record of that
string."* **S3 attributes the phrase to the commissioning instruction, never to
the page**, and says which. Closing that gap is `W-6` in §8 and it is an owner
access action, already named in `SRC-086`'s `owner_action_required`.

**Rules.** No score, no streak, no "correct" (§9.3). The institution's own
position is disclosed **last**, and here disclosing it last means disclosing at
S5 that there is not one yet.

**`Avoid` check — *"No kitsch, fake Tamil or neon overload."*** The counter-history
on this screen is made of an unregistered rival, two unavailable gates and a
universal negative the institution cannot support. There is nothing here to
decorate.

---

### 6.4 S4 — THE UNCERTAINTY

**This is the screen the institution is for.** Posture **Nocturnal Veḷi**,
derived by framework §1.5 rule 3 (§3.4 above). Screen title, as a working label
and not as copy: *what we have not done*.

The requirement is that the museum state what it does not know **and** that the
visitor can see the evidence for that ignorance. Four elements, in this order.
Each is a thing on a screen, not a tone.

---

**Element 1 — the column.**

The same twenty-three-row table the visitor sorted twice at S2. One column
changed. The `sense` column of
`03-REGISTERS/rigveda-varna-occurrences.csv`, displayed at full height:

```
VAR-OCC-001  01.073.07 d  várṇam    ACC.M.SG   NOT ASSIGNED
VAR-OCC-002  01.092.10 b  várṇam    ACC.M.SG   NOT ASSIGNED
VAR-OCC-003  01.096.05 a  várṇam    ACC.M.SG   NOT ASSIGNED
   …
VAR-OCC-022  10.003.03 d  várṇaiḥ   INS.M.PL   NOT ASSIGNED
VAR-OCC-023  10.124.07 d  várṇam    ACC.M.SG   NOT ASSIGNED
```

All twenty-three cells read `NOT ASSIGNED`. Beside it the `sense_source` column,
which reads, in all twenty-three rows: *"no retrieved source assigns a sense per
passage."*

**This is not a message about the table. It is the table.** That is the whole
mechanic and it is why the loop holds one subject across five screens: the
visitor has already sorted this instrument twice and it produced real answers
both times. The third column produces none, in the same instrument, at the same
resolution, on the same rows. The ignorance is not asserted — it is *displayed
at the granularity of the evidence*, cell by cell, and the visitor can check
every cell against the register.

A statement that says "we do not know what these mean" is a claim the visitor
must take on trust. A column of twenty-three `NOT ASSIGNED` cells beside a
column of twenty-three grammatical analyses that are all filled in is the
evidence for the ignorance, and it is falsifiable on sight: one filled cell
would refute it.

---

**Element 2 — the absence record, with its four places distinguished.**

`mk:abs:varna-sense`, all of framework §3.7's fields filled, none elided:

| Field | Value |
|---|---|
| `expected_evidence` | a per-occurrence sense assignment for *varṇa-* in the Rigveda |
| `expected_where` | (i) the Zurich lemma/morphology annotation, `SRC-022`; (ii) the lexicon, Grassmann's gloss via `matched_lemmata.json`, `SRC-026`; (iii) the nine translations bundled with the corpus, `SRC-072`–`SRC-077`; (iv) this repository's own registers, `SRC-086` |
| `p_produced` | **(i) ≈ 0** — `VAR-004` (`VERIFIED`): the Zurich layer carries lemma and morphology and *no sense field*. **(ii) partial** — `VAR-003` (`VERIFIED`): Grassmann supplies the *range*, eight senses undivided, and distributes none of it over passages. **(iii) ≈ 1** — every translator chose an English word for every passage. **(iv) 0** — `SRC-086` establishes the repository held no sense column before the varṇa census |
| `p_survived` | not applicable to a digital annotation; 1 for the printed translations |
| `search_coverage` | `SRC-086`, 2026-09-07T19:15Z: full-tree `git grep` over every tracked file, plus column-name inspection of every CSV in `03-REGISTERS/`, for *varna*, *varRa*, *sense*, *human-applied*, *colour/skin* |
| `accessibility` | `SRC-072`–`SRC-077` reachable inside the `SRC-019` clone; `melakeela/site` **not** reachable (`SRC-086` blocking constraint) |
| `recognisability` | yes for the translations — a translator's English word is recognisable as a sense choice. The difficulty is *adjudicating* between nine of them, which is constitution §7's job and is not a recognition problem |
| `absence_type` | **`NOT PRODUCED`**, and **scoped to (i) alone** |

**The scoping is the honest part and the surface must carry it.** Only place (i)
is an absence. Places (iii) and (iv) are not absences at all: the translations
exist, they are reachable, and the work of reading the 23 passages against them
has simply not been done. Typing that as an absence would be dishonest, and it
would break the standard twice over — `CLAUDE.md`'s eight negative-evidence types
have no entry for it, and the independent review of the corrections unit already
struck down exactly this move, dropping **"NOT ATTEMPTED"** as an invented ninth
type (`CORRECTIONS-PENDING.md` §5.1, defect 9).

Framework §3.7's product rule is displayed with the record: **only `ABSENT
DESPITE ADEQUATE SEARCH` may function as evidence against a proposition.** This
absence is `NOT PRODUCED`, so it is *"a statement about the archive"* and the
interface renders it *"in the archive's voice, not the past's"*. It says nothing
whatever about whether the 23 share a sense.

**So the loop needs a mechanism the framework does not currently give it**: a way
to display *work recorded as owed and not done*, which is neither an absence nor
a hold. Framework §11.1 has negative rows in the Institutional Obligations
Register — *"refused requests, unanswered letters, unreturned objects,
consultations not held"* — but §1.6.2 attaches them to Reconnection only, and
they are obligations to third parties rather than to the record. Raised as
**`D-046`**; see §8, `W-7`, and `DECISIONS-NEEDED.md`.

---

**Element 3 — the receipt, with a date.**

Three records, side by side, each with its status on its face:

- **`IH-287`** (`INHERITED-UNVERIFIED`), verbatim, with its locator
  `01-INHERITED/claude-project-handoff.md L523`: *"The varna 23 human-applied
  split and the colour/skin count done right are owed."* Handoff work item 19,
  Tier 2. **Recorded as owed before this repository existed. Still open.**
- **`IH-086`**'s own note (`INHERITED-UNVERIFIED`): *"The human-applied split is
  marked NEEDS-CHECK."*
- **`VAR-008`** (`VERIFIED`): *"The sense sort published on
  what-varna-meant.html is work this repository records as owed and has not
  done."* With `SRC-086`, the ledger row for the search that established it —
  **including that search's own limit**, quoted: the search *"says nothing about
  what what-varna-meant.html holds."*

That last inclusion is what keeps the screen from being a performance. The
institution is showing the visitor: what it does not know; the table where the
not-knowing lives; the dated record that it owed this work and did not do it;
**and the boundary of its own ignorance-claim** — it cannot currently read its
own live page, so even its account of its own failure is scoped.

---

**Element 4 — the correction that already ran on this material.**

Displayed, not hidden, per `CLAUDE.md`'s rule that correction history is
preserved:

- **`BF-016`** — `VAR-007` was published reading *"24 tokens over 13 distinct
  compound lemmas"*, `VERIFIED`, and called a floor. It was wrong in **both**
  directions: it missed *suvarṇa-* because the lemma carries an acute the string
  test did not, and admitted four lemmas from unrelated stems. The true figure
  on the corrected method is **23 over 12**, and *"24 was above the count, not
  below it, and the floor language was wrong as well."*
- **`RA-017`** — `OPEN`. Every lemma-set selection in this repository made by a
  string test rather than by lemma id or gloss is queued for re-audit on the
  strength of that failure.
- **`IC-P-002`** — recorded by this unit: `CORRECTIONS-PENDING.md` brief 4
  §4.2.2 and its proposed public copy still print **24 tokens / 13 compound
  lemmas**, against `VAR-007`'s corrected **23 / 12**. The corrections document
  records the fix in its own defect table and did not carry it into its body
  text. **The loop displays `VAR-007`'s register figure and displays the
  discrepancy**, because a screen about undone work that quietly used the
  uncorrected number would be the joke telling itself.

**Rules for this screen.**

- **Field Mode is forbidden here**, per §5.
- **No claim on this screen may be displayed without its status**, and the two
  `INHERITED-UNVERIFIED` records are the load-bearing ones. The screen's power
  comes from `IH-287` being *old*, not from it being verified.
- **`unknown` is never a rival** (framework §3.7). Nothing on this screen appears
  in a list beside `VAR-009` and the null as a third option.

**`Avoid` check — *"No fantasy portal or occult styling"*, desired effect
*"Vastness without menace."*** This screen has no imagery. It is a table with
one column changed, a record, three receipts and a correction. The vastness is
that the column is 23 rows long and every cell is empty in the same way.

---

### 6.5 S5 — EXIT

**Surface.** Posture **Reconnection**; function *"Return, renewed access, living
practice"*, desired effect *"Repair without false closure"*, prototype *"Future
community-led work"* (`INHERITED-UNVERIFIED`). Field Mode forbidden (§1.7).

**The exit must leave the visitor able to return.** Three affordances, and they
are the three different things "return" can mean.

**a. The run is citable.** Framework §9.3: every PROVE IT run is exportable *"as
the claim, the evidence set, the gates and the visitor's own reasoning"* and *"a
run is citable."* The visitor leaves with a stable identifier — `mk:run:<id>` —
that carries the **base revision of every claim it displayed**. When `VAR-009`
changes, the run still resolves and shows what it looked like when they worked
it. Framework §5.2 governs the export; §7.2.4's query provenance governs the S2
groupings inside it.

**b. The disagreement is a challenge candidate.** Framework §9.4: a recorded
disagreement *"is not a comment"*; it enters the correction pipeline with the run
attached — the claim, the revision, the evidence relied on, the gate or absence
read differently, and what the visitor says would settle it. It receives an
identifier. Triage is public in aggregate: how many challenges on each claim, how
many assessed, how many changed a claim, how many declined and why.

**c. The claim watches back.** Framework §7.2's *"changed since I last looked"*
facet, scoped to this run's claim set. The exit names the exact event that would
change the loop: the sense reading, done and published with the passages and the
competing translations. `VAR-009`'s revision history (§3.6) is the thing that
will move.

**And the institution's own position, disclosed last, is that it does not have
one.** Framework §9.3 requires the institution's position after the visitor has
worked the evidence. Here it is `CORRECTIONS-PENDING.md` brief 4 §4.4's
`MELAKEELA'S CURRENT INTERPRETATION` slot, which reads, in the drafted copy:
*"(withheld — the sense reading is not done; see above)"*. The exit discloses the
withholding and the reason, which is a disclosure and not an evasion.

**Rules — and this is where the `Avoid` does real work.**

***"Digitization is not restitution."*** Framework §1.6.2 calls this *"the
governing rule of the whole environment"* and adds that Reconnection *"may not
present any of the above as repair achieved"*, and that a published record *"is
a record of a state, including the state 'still withheld'."* Applied to this
exit:

- The receipt says **received**, never *accepted*, *heard*, *valued* or
  *thank you*.
- The intake screen may not display a count of challenges received as an
  institutional achievement. §9.4's aggregate triage is published as **four
  numbers together** — received, assessed, changed a claim, declined with reason
  — never as the first alone.
- The exit may not describe the loop the visitor has just walked as an act of
  transparency. It states what happened: a claim was tested, an absence was
  shown, a disagreement was or was not recorded.
- **The undone work stays undone on this screen.** `IH-287` is still open when
  the visitor leaves. Nothing at S5 may imply that displaying an obligation
  discharges it. This is `BF-022`'s correction; see §11.

**Return path.** S5 → S1, with the question unchanged and the claim set's
revision dates shown. If nothing has changed, the loop returns the visitor to
the same 23. If something has, S1's `VAR-001` row carries a revision marker and
the loop the visitor walks is not the loop they walked before.

---

## 7. Every claim the loop displays, by `claim_id` and status

Every row the five screens put in front of a visitor. Grouped by register.
Statuses are as recorded on 2026-09-08; none was changed by this unit.

### 7.1 `03-REGISTERS/rigveda-varna.csv`

| `claim_id` | Status | What the loop uses it for | Screen |
|---|---|---|---|
| `VAR-001` | `VERIFIED` | the count: 23 tokens, 23 stanzas, 21 hymns | S1, S2 |
| `VAR-002` | `PROVISIONAL` | why the inherited 23 and the measured 23 are not two sources — the denominator does not match | S2 |
| `VAR-003` | `VERIFIED` | Grassmann's eight senses in one undivided string, distributed over nothing | S3, S4 |
| `VAR-004` | `VERIFIED` | the annotation carries no sense field, and no retrieved source assigns a sense per occurrence | S4 |
| `VAR-005` | `VERIFIED` | the stratum distribution the visitor reproduces | S2 |
| `VAR-006` | `VERIFIED` | the book distribution the visitor reproduces | S2 |
| `VAR-007` | `VERIFIED` | the compound boundary: 23 further tokens, 12 lemmas | S2 |
| `VAR-008` | `VERIFIED` | the sense sort is owed and has not been done | S4 |
| `VAR-009` | `HYPOTHESIS` | the proposition the PROVE IT run is anchored on — displayed **as** a hypothesis, which is its correct use | S3, S5 |

### 7.2 `03-REGISTERS/rigveda-pur-family.csv` and `rigveda-pur-4j-claims.csv`

Displayed because S2 shows a stratum column, and a stratum column cannot be
displayed honestly without them.

| `claim_id` | Status | What the loop uses it for | Screen |
|---|---|---|---|
| `PUR-001` | `VERIFIED` | the corpus size, 164,758 tokens — the denominator behind `VAR-002` | S1 (Source Mode), S2 |
| `PUR-002` | `VERIFIED` | every token carries a lemma; 164,755 carry a stratum — the coverage behind `VAR-001` and `VAR-005` | S2 |
| `PUR-011` | `VERIFIED` | what Arnold's letters mean, and what the small italics mean — makes the `stratum_certainty` column readable | S2 |
| `PUR-012` | `VERIFIED` | 9,607 stanzas uppercase, 945 lowercase — the scale of the certainty distinction | S2 |
| `PUR-013` | `VERIFIED` | `strata.json` attributed to Arnold 1905, compiled by Gunkel and Ryan, CC-BY-4.0 | S2 |
| `PUR-028` | `HYPOTHESIS` | that Arnold's periods are real chronological stages — displayed **as untested**, at the grouping control | S2 |
| `PUR4J-018` | `VERIFIED` | the pinned corpus carries no geographic content of any kind — closes the geographical gate at S3 and rules out Living Tiṇai | S3 |

### 7.3 `03-REGISTERS/inherited-claims.csv`

All `INHERITED-UNVERIFIED`, displayed as such. These are the loop's receipts, and
their value is that they are old, not that they are verified.

| `claim_id` | Status | What the loop uses it for | Screen |
|---|---|---|---|
| `IH-086` | `INHERITED-UNVERIFIED` | the inherited count and its `NEEDS-CHECK` note on the human-applied split | S2, S4 |
| `IH-287` | `INHERITED-UNVERIFIED` | handoff work item 19: the split and the colour/skin count *are owed* | S4 |
| `IH-149` | `INHERITED-UNVERIFIED` | correction `R-03` — the owner rejected leading with colour | S3 |

### 7.4 Non-claim records the loop displays

Not claims, and not given claim statuses; each is displayed as the record type it
is.

| Record | Register | Screen |
|---|---|---|
| `VAR-OCC-001` … `VAR-OCC-023` | `03-REGISTERS/rigveda-varna-occurrences.csv` | S2, S4 |
| `DEP-001`, `DEP-002`, `DEP-024` | `02-SOURCES/dependency.csv` | S2, S3 |
| `APA-E-003`, `APA-E-006` | `04-AUDITS/ARCHIVE-AND-POWER-AUDIT.csv` | S2, S3 |
| `BF-016`, `RA-017` | `04-AUDITS/BIAS-FAILURE-LOG.csv`, `REAUDIT-QUEUE.csv` | S4 |
| `IC-P-002` | `04-AUDITS/INTERNAL-CONTRADICTIONS.csv` (added by this unit) | S4 |
| `SRC-019`, `SRC-020`, `SRC-022`, `SRC-023`, `SRC-026`, `SRC-072`–`SRC-077`, `SRC-085`, `SRC-086` | `02-SOURCES/access-ledger.csv` | all five, via Source Mode |
| `mk:abs:varna-sense` | **does not exist**; specified in §6.4 element 2 | S4 |

### 7.5 The count

**19 claims displayed: 13 `VERIFIED`, 1 `PROVISIONAL`, 2 `HYPOTHESIS`, 3
`INHERITED-UNVERIFIED`.** Nine from `rigveda-varna.csv` (7 / 1 / 1 / 0), seven
from the *púr-* registers (6 / 0 / 1 / 0), three inherited (0 / 0 / 0 / 3).

Two of the nineteen are load-bearing while sitting below `VERIFIED`, and both are
displayed as what they are rather than leaned on: `VAR-009` is the hypothesis the
PROVE IT run tests, and `PUR-028` is the untested assumption inside the stratum
instrument. **No `REJECTED`, `SUPERSEDED` or `HOLD` row is displayed by this
loop.** `IH-149` reports a rejection made by the owner in a prior thread and is
itself `INHERITED-UNVERIFIED`, not a `REJECTED` row in this namespace.

---

## 8. Can the loop be built from `VERIFIED` claims alone? No. What it needs, and which unit produces it

**No, and the reasons are of four different kinds.** Two of them cannot be fixed
by any unit of work, two can, and one is fixed by a unit that would destroy the
screen it fixes.

### 8.0 The two that no retrieval can promote

**The frame is not a claim.** Every posture assignment in this loop comes from
`environment-map.csv` (`INHERITED-UNVERIFIED`) and every design proposition from
`museum-framework.md` (`HYPOTHESIS`, per its own §14.4). No retrieval promotes
either, because they are design propositions, not historical claims —
`CONTROLLER-RECONCILIATION.md` C-1's territory. **This does not block the loop
and must not be presented as blocking it**; it means the loop's *shape* is a
hypothesis while the loop's *content* is largely verified, and those two
standings are recorded separately rather than averaged.

What *can* be done is make the assignment auditable: `W-1`.

**The rejection at S3 is `INHERITED-UNVERIFIED` and stays that way.** `IH-149`
records an owner decision taken in a prior chat thread. `CLAUDE.md` is explicit:
those are the `HD-` namespace, they stay `INHERITED-UNVERIFIED`, and a register
row would be a promotion. If the owner re-affirms `R-03`, that is a fresh `D-`
allocated then. The loop displays it correctly today, as an inherited record.

### 8.1 The units of work

| | Unit | Produces | Blocked? |
|---|---|---|---|
| **`W-1`** | **The Editorial Register.** Create the register framework §1.5 and §11.5 require and `SCHEMA.md` §7 records as missing: `derived_posture`, `assigned_posture`, `override_reason`, `decided_by`, `decided_date`, `derived_residual`. Write five rows, one per screen, including S4's derived-Nocturnal-Veḷi against `what-varna-meant`'s assigned Tamil Retrofuture (§3.4). | An auditable posture assignment for every screen. Does not promote anything; makes an editorial act visible instead of implicit. | No. Small unit, no retrieval. |
| **`W-2`** | **The denominator.** `VAR-002` is `PROVISIONAL` because `IH-086`'s 180,196 words is not the pinned corpus's 164,758 tokens — a 15,438-token gap between two tokenisations, unexplained. Retrieve `gret_scan.json`, or the tokenisation it used, and reconcile. | `VAR-002` at `VERIFIED`, or a `HOLD` row and a clean statement of the gap. | Partly. The file is not in this repository. If unreachable → `05-HOLDS/`, and S2 states the gap rather than the reconciliation. |
| **`W-3`** | **The sense reading.** The unit brief 4 §4.3 already scopes: all 23 passages against `SRC-072`–`SRC-077` under constitution §7's translation standard — original script, transliteration, grammatical form, semantic range, textual context, edition, exact locator, translation used, alternatives, interpretive consequence — plus the `inherited_category_audit` on *caste*, *colour* and *class*. Tests `VAR-009`. | 23 Translation Blocks; `VAR-009` resolved or refined; the `sense` column filled or explicitly typed per occurrence. | **No. Nothing blocks it but the work.** The translations are inside the `SRC-019` clone. |
| **`W-4`** | **Register the rival.** Give the official account — that Rigvedic *varṇa* already carries a social sense — a Claim Object with its own sources, so S3 stage 2 states a rival rather than a gap. | A rival with a status, sources and a standing (constitution step 11). | **Partly blocked.** `APA-E-003` types the relevant secondary literature `NOT ACCESSIBLE`. Takes a `HOLD` row naming what is needed. Until then S3 shows the gap, which is honest and is also the loop's second display of institutional ignorance. |
| **`W-5`** | **RV 10.90, and the compound stanza list.** Two rows. (a) None of the 23 simplex occurrences falls in RV 10.90 — this follows from `VAR-001` and the 23 stanzas listed in the occurrence register, and needs **no new retrieval**, only a register row. (b) The stanza list for `VAR-007`'s 23 compound tokens, from the corrected census script, which is what makes (a) safely scopable to the simplex. | Two register rows that let the loop connect to the `one-verse` page's claim — *"The explicit fourfold varṇa scheme appears together in one Rigvedic verse"* (`INHERITED-UNVERIFIED`, page-audit Decision `Revise`). | No. Small unit, no retrieval. **Highest value per unit of effort in this list.** See §8.2. |
| **`W-6`** | **Read the live page.** Repository access to `melakeela/site`, so `what-varna-meant.html`'s own text can be retrieved rather than reported. | S3 can attribute the page's claim to the page. Closes `SRC-086`'s stated limit and lets constitution step 13 run properly on this subject. | **Blocked on the owner.** Already named in `SRC-086`'s `owner_action_required`. `RESEARCH-QUEUE.md` `## Not yet` lists *"Anything touching melakeela/site."* |
| **`W-7`** | **A display mechanism for owed work.** Neither an absence (`CLAUDE.md`'s eight types do not cover it, and "NOT ATTEMPTED" was struck down as an invented ninth) nor a hold (nothing blocks it). Framework §11.1's negative rows are the nearest fit and are attached to Reconnection only. | S4 element 3 gets a specified record type instead of an ad-hoc display. | **Blocked on `D-046`**, allocated by this unit. It is a publication-approval question: does the institution publish its own undone work? |

### 8.2 `W-5` deserves a paragraph of its own

The `one-verse` page asserts *"The explicit fourfold varṇa scheme appears
together in one Rigvedic verse."* The 23 simplex occurrences of *varṇa-* are at
the 23 stanzas listed in `rigveda-varna-occurrences.csv`, and **RV 10.90 is not
among them.** If that holds for the compounds too — which `W-5(b)` is what
settles — then the verse the fourfold scheme is read from does not contain the
word.

That is the sharpest thing this loop could put on S3, it is one register row and
one script re-run away, and **the loop may not display it today**, because a
derivation from two registers is not a claim until it is a row. It is written
here so it is not smuggled onto a screen before it is one.

### 8.3 The unit that would destroy S4, and why that is the point

**`W-3` dissolves this loop's uncertainty screen.** When the 23 passages are read
against the nine translations, the `sense` column fills, the `NOT ASSIGNED`
display stops being available, and S4 as specified ceases to exist.

**Good.** A loop whose uncertainty stop cannot be dissolved is not an honest
exhibit of ignorance; it is a pose, and it becomes the institution's most
flattering asset. The specification therefore states its own replacement in
advance: **when `W-3` lands, S4 becomes the per-occurrence Translation Blocks
with the translators' disagreements displayed** — brief 4's own falsifier says
*"because on a word like this one, they do"* — **plus a new, narrower absence
record for whatever the reading cannot settle.** The posture may move: nine
translators disagreeing is Living Signal Field material by §1.5 rule 4, or
Reading Room by content, and the derivation is re-run rather than assumed.

**Review trigger, stated so it can be checked against:** if `W-3` has not been
run and S4 is still displaying `NOT ASSIGNED` at the next release gate, that is a
finding against this loop, not a feature of it. Logged as `BF-022`, re-audit
`RA-020`.

---

## 9. If `D-032` blocks `index`

The one substitution, so the reading in §0 is cheap to act on: **S1 moves off
`index` and onto the Question node's own landing surface**, `mk:qst:varna-23`,
which framework §6.6 makes a first-class addressable node with its own landing
and its own default posture — Nocturnal Veḷi, the same posture. Nothing else in
the loop changes: the posture sequence, the claim inventory, the four elements of
S4 and the three affordances of S5 are all unaffected.

The cost of the substitution is that the loop then has no threshold, and §6.1's
argument about restraint at arrival has to be made by the Question landing
instead. That is a real loss and it is smaller than acting on an undecided MVP
set.

---

## 10. The removal test — why five screens is smallest

| Remove | What the loop loses |
|---|---|
| **S1** | The arrival. The visitor enters mid-argument, at a distribution, without the question that makes it worth distributing. |
| **S2** | The investigation, **and S4's force**. Without having sorted the table twice and got real answers, the `NOT ASSIGNED` column at S4 is just an empty column. The uncertainty screen borrows all of its weight from the instrument having worked. |
| **S3** | The counter-account, the two unavailable gates, and the loop's ability to be *about* anything. Also the mandatory Investigation Mode of Tamil Retrofuture, which is the framework lock that keeps the counter-account falsifiable. |
| **S4** | The institution's distinguishing move. The loop becomes a competent lexical exhibit that any museum could build. |
| **S5** | The return. Everything the visitor did evaporates; the disagreement has nowhere to go; §9.4's correction intake has no surface, and Reconnection's correction ledger has nothing to display. |

**Merging S3 into S4** was considered and rejected. Framework §9.2 makes the
absences stage 5 of a six-stage run, which would make S4 a panel inside S3. The
absences are given a screen because the whole institutional claim of this loop
rests there, and because a panel inside an argument reads as a caveat to the
argument, which is the opposite of what §3.4 derives.

**Adding a sixth screen** — a Living Tiṇai or Extraction / Collection stop — was
rejected on the evidence, per §3.6. Neither posture's derivation rule fires on
this claim set, and occupying a posture the evidence does not support is exactly
what the environment map's `Avoid` column exists to catch.

---

## 11. The two adversarial tests, run on this unit

Constitution §8 and `CLAUDE.md`: both before the unit is called finished, logged
whether or not they found anything, and running one is a failed test (framework
§3.11). **Both found something.**

### 11.1 Prestige-bias challenge

*Did this unit privilege a claim because it is canonical, Sanskritic,
Brahmanical, Indo-European, European, colonial, institutionally prestigious,
repeatedly cited or nationally useful?*

**Found: yes, twice.** Logged as `BF-021`; re-audit `RA-020`.

**(i) The instruments.** The loop is built end to end on European philology — a
German lexicon (Grassmann), a British metrist (Arnold, Cambridge 1905), a Swiss
annotation layer (Zurich) — and the first draft of S2 put `APA-E-006` in Source
Mode, where a visitor reaches it only by choosing to. That presents European
philological infrastructure as the neutral substrate on which a counter-account
is built, which reproduces the prestige the loop means to audit. **Corrected in
§6.2**: `APA-E-006` is a foreground element at the grouping control, and the
control is labelled *"group by Arnold's periodisation"*, never *"by period"*.

**(ii) The subject.** Choosing a Vedic Sanskrit subject for this institution's
smallest complete loop, on a Tamil-named platform, is a prestige choice, and the
defence that "it is where the `VERIFIED` claims are" is not a defence — it is a
restatement of the problem. `APA-E-003` records that the retrieval channel
reaches what exists as a public git repository and that the Dravidian
comparative literature does not; `HOLD-002` through `HOLD-005` are the receipts.
**The loop's subject was selected by the egress policy.** Not corrected — it
cannot be corrected inside this unit, because the alternative subjects are on
hold. **Stated in §1**, and it is the reason `HOLD-002`–`HOLD-005` bear on a
product specification at all.

### 11.2 Preferred-counter-narrative challenge

*Did this unit accept a claim too easily because it is Dravidian, Indigenous,
anti-colonial, anti-Brahmanical, subaltern, diffusionist or politically
corrective?*

**Found: yes, one, and it is structural.** Logged as `BF-022`; re-audit
`RA-020`.

The loop's whole dramatic shape is *the museum admits it cannot back its own
anti-caste headline*. That is **flattering to the institution.** An institution
that displays its ignorance looks rigorous, and this design converts an unmet
obligation — `IH-287`, recorded as owed before this repository existed and still
open — into the loop's most impressive screen.

Displaying owed work is honest. *Staging* it as the institution's distinguishing
move risks converting a failure into an asset, which is Reconnection's `Avoid`
generalised: **digitization is not restitution, and neither is disclosure.**

Three corrections, all made:

1. **S4 element 3 carries the date and the open state** (§6.4). The receipt's
   force is that `IH-287` is old and unactioned, not that the institution is
   candid.
2. **S5 may not congratulate** (§6.5). Received, not accepted; four triage
   numbers together, never the first alone; no self-description as transparency.
3. **§8.3 states the review trigger.** If `W-3` is unrun and S4 still displays
   `NOT ASSIGNED` at the next release gate, that is a finding against this loop.

**The asymmetry is not pretended away.** The two failures above are not equal.
`BF-021`(ii) is a fact about which archives were reachable, which is an
institutional and colonial asymmetry this unit did not create and cannot fix.
`BF-022` is a design choice this unit made and could have made differently.

### 11.3 What the tests did not clear

This unit was not put through independent adversarial review before being
committed. `06-BRIEFS/mvp-fifteen/README.md` §0.1 records the relevant precedent
in terms — a first self-test passed that document and *"should not have"*, and an
independent reviewer then found fourteen defects. **This unit's self-tests should
be read with that record in view, and independent review is owed on it.**

---

## 12. Findings against the framework, raised by trying to build a loop from it

Recorded because a specification that exercises another specification and reports
no friction has probably not exercised it.

1. **The §1.7 matrix over-specifies Atlas Mode.** *Mandatory* in Living Signal
   Field cannot hold for an exhibit whose relations are not spatial. `PUR4J-018`
   makes this concrete on this subject: no geography exists to place. §5 records
   the departure. The matrix needs a condition, or Atlas needs to mean "the
   relationship view" rather than "the map".
2. **There is no record type for owed work.** Between the eight absence types
   (which cover what the archive did not produce) and `05-HOLDS/` (which covers
   what we cannot reach) there is nothing for *what we could do and have not*.
   `IH-287` is that, and S4 needs to display it. **`D-046`.**
3. **The Editorial Register that §1.5 depends on does not exist.** Every posture
   assignment in this repository is currently unlogged, including the four this
   loop makes and the one it overrides. `W-1`.
4. **Framework §1.5's derivation and the inherited assignment disagree on
   `what-varna-meant`** — derived Nocturnal Veḷi, assigned Tamil Retrofuture
   (§3.4). This is the first worked instance of the divergence the framework
   anticipates, and it is a live test of whether §1.5's rules are right. One
   instance settles nothing; it is recorded so a second can be compared to it.

---

## 13. What this specification does not do

- **It writes no copy.** The QUESTION line at §4 and the withheld-interpretation
  line at §6.5 are quoted from `CORRECTIONS-PENDING.md` brief 4, which is itself
  a *proposed* replacement awaiting a release gate. Nothing here is approved for
  publication and `D-010` governs institutional claims.
- **It specifies no visual system.** Framework §12 hands that over separately and
  §12.4 records what the handoff does not authorise. Palettes are quoted from
  `environment-map.csv` only where they identify an environment.
- **It does not schedule anything.** No launch, no order of work, no answer
  assumed to `D-012`, `D-032` or `D-034`.
- **It specifies one loop.** It is not a sitemap, not an information
  architecture, and not a claim that the institution's other 95 pages fit this
  shape.
- **It did not check `melakeela/site`.** Constitution step 13 cannot run properly
  on this subject from this session; `W-6` is what would let it.

---

## 14. Decision raised by this unit

**`D-046`** — Does an exhibit's uncertainty surface display work the record
states is owed and not done? Allocated in `09-DECISIONS/OWNER-DECISIONS.csv`;
prose in `DECISIONS-NEEDED.md`, because it blocks S4 element 3 as specified.

No other `D-` is allocated. The placement question in §0 deliberately allocates
none, following `06-BRIEFS/mvp-fifteen/README.md` §0.
