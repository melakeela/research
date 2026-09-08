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
**Revision:** rev. 2, 2026-09-08. Independent adversarial review was run on
rev. 1 before the pull request was opened and returned six blocking findings and
nine high ones. What it found is repaired below and recorded in §11.4 rather than
quietly fixed; three of the six were method failures in this unit's own work and
two of those had already been committed into `04-AUDITS/`. Rev. 1's derivation
argument, its subject-selection argument and its claim inventory did not survive.

---

## 0. Standing controls this unit ran against, and the boundary it rests on

**`RESEARCH-QUEUE.md` `## Not yet` lists "Product and institutional
specification (§12) — pending `D-012`", and lists "Anything touching
`melakeela/site`".** `DECISIONS-NEEDED.md` **`D-032`** ends *"Nothing in this
repository acts on the MVP set until this is answered."*

**Rev. 1 put the loop's arrival on `index`, which is MVP rank 1, and argued that
specifying a route through a page is not acting on the set.** Independent review
rejected the argument, and it was right to: §6.1 specified `index`'s content down
to *"No image. No second claim. No navigation menu."* That is not routing through
a page, it is designing one. **Corrected in rev. 2:** the arrival is the Question
node's own landing surface, `mk:qst:varna-23`, which framework §6.6 makes a
first-class addressable node with its own landing and its own default posture.
No MVP page appears in the loop. `index` is recorded in §9 as a variant that
waits on `D-032` with the rest.

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
  After the rev. 2 correction it also specifies the content of no MVP page.
- It **writes no site code**, per `CLAUDE.md`'s standing prohibition and §12's
  closing line. There is no markup, no CSS and no script below; where a
  behaviour needs naming it is named as a behaviour.
- It **does not touch `melakeela/site`**. On the contrary, §6.3 below turns the
  fact that the live page cannot be read from this session into a displayed
  element rather than working around it.
- Nothing here promotes a claim, because nothing here retrieved anything.

**A second decision is engaged and rev. 1 missed it.** `DECISIONS-NEEDED.md`
**`D-021`** — *"A guided sequence is a real service and it is also an argument"* —
is the closest existing decision to what this file specifies. It is raised
against the Atlas's seven §13 settings rather than against a page loop, but its
principle reaches here unchanged: **a route is an argument, and this one asserts
that these five relationships in this order are how a visitor should meet this
evidence.** `D-021`'s option 2 requires that a guided sequence *"gets an
`mk:clm:` with sources, alternatives and falsifiers."* This loop has none.
§15 supplies the falsifier and the rivals so the sequence can be argued with;
allocating it a claim id is `W-10` and is `D-021`'s to decide, not this file's.

**And the boundary may still not hold.** If the owner reads a specification that
names `index` even as a declined variant as acting on the MVP set, the correct
disposition is that this unit waits on `D-032` with the rest.

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

**Why this subject.** Rev. 1 wrote that *varṇa* is *"the only subject in this
repository that carries a dense set of `VERIFIED` claims"* and the five other
properties the loop needs, and that *"no other body of work here has all five."*
**Both halves are false and independent review derived the numbers that break
them.** `VERIFIED` rows by register: `rigveda-pur-counts.csv` 49,
`domain-e-measurements.csv` 30, `rigveda-pur-family.csv` 25,
`rigveda-pur-4j-claims.csv` 23, `domain-m-brahui-position.csv` 20,
`domain-e-claims.csv` 19, **`rigveda-varna.csv` 7.** *varṇa* has the **thinnest**
`VERIFIED` set of any subject register in this repository, and the forts meet all
five properties at roughly fourteen times the density — 97 `VERIFIED` rows across
three registers, `PUR-028` at `HYPOTHESIS`, `HOLD-006` and inherited owed rows,
`BF-012`/`BF-014`/`BF-017` logged on their own rows, and a live page whose
central public claim is contradicted by `PUR4J-003`. Logged as `BF-023`.

**The real reason, which is narrower and is a choice rather than a fact.** No
other subject here offers the shape S4 needs: **one register column, twenty-three
rows, uniformly empty, sitting in an instrument the visitor has just watched
work.** The forts' unknowns are distributed across typologies, holds and
overrides; they are larger and they are not displayable in a single column at the
granularity of the evidence. That is a design judgement about legibility, not a
finding about which evidence base is stronger, and it is recorded as one.

**And it is a Vedic Sanskrit subject on a Tamil-named platform, chosen from a
shelf the egress policy stocked.** `04-AUDITS/ARCHIVE-AND-POWER-AUDIT.csv`
`APA-E-003` records that this session's retrieval channel reaches what exists as
a public git repository and little else, that *"attested and reconstructed
families have machine-readable derivatives on GitHub; proposals about unattested
donors do not"*, and that for domain E *"the split follows the channel, not the
evidence."* `HOLD-002` to `HOLD-005` are the receipts. Logged as `BF-021`.

**The sharper asymmetry, which rev. 1's own bias tests did not name and which
`RA-015` had already recorded.** Every instrument in this loop *"sits in one
German philological line"*, and — `RA-015`, `OPEN`, `HIGH` — *"There is NO
non-European scholarly source anywhere in the unit. Sāyaṇa's commentary — the
indigenous exegetical tradition, and the one Griffith leaned on — is not in the
pinned corpus and was not retrieved. This is an archival asymmetry, not a neutral
fact about what exists."* `RA-015` is blocked on egress (`SRC-080` to `SRC-083`)
and related to `D-043`. §11.1 carries this and §6.2 displays it.

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

**One caution, because rev. 1 over-read this.** That posture is a display and
navigation axis with no evidentiary authority (framework §1.3) means a loop can
demonstrate the thesis without the derivation having produced its postures. Rev. 1
argued the reverse — that a derived posture proved the thesis — and §3.4 withdraws
it. The thesis is exercised here by the subject staying fixed while the
relationship changes, and that is all it needs.

---

## 3. The postures the loop passes through, in order, and why in that order

| # | Screen | Posture | The visitor's relation to the knowledge | Framework basis for the assignment |
|---|---|---|---|---|
| S1 | Arrival | **Nocturnal Veḷi** | *not yet known* | §6.6 — Nocturnal Veḷi is the Question route's default posture, and the Question landing is the arrival surface (§0) |
| S2 | Investigation | **Living Signal Field** | *known by relation* | §6.4 — Living Signal Field is the Word route's default posture; §1.5 rule 4 |
| S3 | The argument | **Tamil Retrofuture** | *known against an official account* | §1.5 rule 6; page-audit assigns `what-varna-meant` this environment (`INHERITED-UNVERIFIED`) |
| S4 | The uncertainty | **Nocturnal Veḷi** | *not yet known — and now we can show you why* | **Editorial, with the reason logged.** §1.5's derivation does **not** produce it — see §3.4 |
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
strata, against books, against the compound boundary. Framework §6.4 makes
Living Signal Field the Word route's default posture, and that is the whole basis
for this assignment.

**Rev. 1 also cited §1.5 rule 4 and the citation is withdrawn.** Rule 4 requires
the exhibit's substance to be **Relationship Objects** in framework §4's sense.
S2's substance is Claim Objects and occurrence records. On §1.5 alone S2 would
fall through to rule 7 and land in Reading Room as a residual, flagged
`derived_residual = true`. It survives as Living Signal Field on the route
default, not on the derivation — which is the second instance in this file of
§1.5 not reaching a screen (§3.4 is the first), and §12 finding 5 treats the two
together.

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

### 3.4 Why Nocturnal Veḷi again, fourth — and why rev. 1's argument for it was wrong

**Rev. 1 claimed this posture was derived. It is not, and the claim was made by
misquoting the rule.** The correction matters more than the conclusion, because
the misquote ran in the direction that made a design choice look like a finding.

**What framework §1.5 rule 3 actually says:**

> **Absence dominance.** If the **majority** of the exhibit's load-bearing
> propositions resolve to typed absences rather than to positive claims →
> **Nocturnal Veḷi**.

**What rev. 1 wrote:** *"Rule 3 fires: the exhibit's load-bearing proposition —
what do these twenty-three occurrences mean — resolves to a typed absence."*
Singular, where the rule says majority. Re-run properly, over the claims §7 says
S4 displays — `VAR-003`, `VAR-004`, `VAR-007`, `VAR-008`, `IH-086`, `IH-287` —
**exactly one resolves to a typed absence.** `VAR-004` does. The other five are
positive claims: Grassmann glosses eight senses, the compounds number 23 over 12,
the sort is owed, the count was inherited, the work was recorded. **One of six is
not a majority. Rule 3 does not fire.**

Rev. 1 also derived over the wrong unit. §1.5 derives over *"the exhibit's Claim
Objects and its Absence records"*; rev. 1 derived over one screen's claim set and
then declared a divergence against `page-audit.csv`'s posture for
`what-varna-meant`, which is a **page**. Run over the page's claim set —
`VAR-001` to `VAR-009` and the page's own central claim — positive claims
dominate overwhelmingly, rule 3 is not close, and **rule 6 fires**: the page's
principal relationship is `contradicts` against a named dominant account. Rule 6
yields **Tamil Retrofuture**, which is what `page-audit.csv` already assigns.

**So there is no divergence between derivation and assignment at the page level,
and rev. 1's structural argument — that the gap between derived and assigned
"is the loop" — is withdrawn.** It was the most quotable sentence in the
document and it was not true. Logged as `BF-024`.

#### What S4's posture actually rests on

**An editorial assignment with its reason on the record**, which is what §1.5
provides for: *"Derivation is advisory. The assigned posture is editorial and is
written to the Editorial Register (§11.5)… An override with an empty reason is
invalid."* The reason, stated so it can be argued with:

> S4's subject is not what the twenty-three occurrences mean. S4's subject is
> **that we do not know, and what our not-knowing is made of.** A surface whose
> content is one typed absence, one search's coverage, one dated obligation and
> one scoping limit is a surface about the edge of the record. Nocturnal Veḷi is
> the posture for the edge of the record — function *"Threshold, deep time,
> unknowns"*, effect *"vastness without menace"* — and no other of the seven is.

That is a judgement. It is defensible and it is not a derivation, and the
difference is the whole of `BF-024`.

#### The framework gap this exposed, which is the real finding

**§1.5 has no derivation unit below the exhibit, and a loop's screens are not
exhibits.** Every one of the seven rules is written over "the exhibit"; a
five-screen route through one subject has five claim sets and one exhibit, and
the framework offers no way to posture a screen. Rev. 1 papered over this by
silently treating a screen as an exhibit.

**And rule 3 is not countable as written.** "The majority of the exhibit's
load-bearing propositions" needs three things the framework does not define:
which propositions are load-bearing, how a proposition that is *about* an absence
(`VAR-008`: the sort is owed) is scored against one that *is* an absence
(`VAR-004`), and whether the denominator is claims, propositions or screens.
Under one reading S4 is 1 of 6 and under another it is 4 of 6. A rule whose
output depends on an undefined denominator cannot settle a posture, and rev. 1's
failure is the predictable consequence of using it as though it could.

Both go to §12 as findings against the framework, and `W-1` builds the register
that would have caught the override at the point it was made.

#### What survives, and it is the part worth keeping

**The same posture means something different on the way out.** At S1 the unknown
is the visitor's: they do not yet know what *varṇa* means in the Rigveda. At S4
the unknown is the institution's, and the visitor can see the table where it
lives. The environment map's claim that a posture describes a *relationship*
rather than a topic is demonstrated if one posture can be occupied twice, with
different content, under the same discipline — and that demonstration does not
need the derivation to have fired. It needs the two screens to be honestly
different, which they are.

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
  place or material dominance and a Place anchor. **Rev. 1 excluded it by
  quoting `PUR4J-018`'s clause *"contains no geographic content of any kind"*,
  and that over-extends the claim.** `PUR4J-018` is scoped to constitution
  §4J's *geography field* and its locator is `info/rv_locations.tsv`, a
  citation-format conversion table; its own notes continue: *"What the corpus
  CAN support is which hydronym lemmas occur in a passage (`PUR4J-017`), which
  is a textual fact; the step from a hydronym to a place on a map is a separate
  claim needing separate evidence."* And the corpus does support it —
  `03-REGISTERS/domain-e-hydronyms.csv` holds 469 hydronym occurrence rows in
  the same pinned corpus, **two of them in *varṇa* stanzas** (`01.113.02`,
  `09.105.04`).

  **The correct exclusion is narrower and it holds.** Living Tiṇai needs a
  **Place** anchor (`mk:plc:`), and the step from a hydronym lemma to a place is
  the separate claim `PUR4J-018`'s notes name — unregistered here, and bounded
  by a research hold. Two hydronym tokens in two of twenty-three stanzas is not
  place dominance under rule 5 on any reading. So Living Tiṇai is excluded for
  want of a Place and for want of dominance, **not** because the corpus has no
  geographic content. The row's `Avoid` — *"No generic landscape decoration"* —
  is what a surface built on two tokens would earn. Logged as `BF-025`; the same
  over-extension sits in `RESEARCH-QUEUE.md`'s domain J row, which this unit
  edited without noticing it, and is `RA-021`.
- **Extraction / Collection** (*known but withheld*). The sense absence is typed
  `NOT PRODUCED`: the Zurich annotation was not built to record sense
  (`VAR-004`, `VERIFIED`). **Nobody withheld it.** Dressing a `NOT PRODUCED`
  absence as extraction is precisely the *"unsupported allegation"* the row's
  `Avoid` forbids. The one genuine access failure in range is the institution's
  own — it cannot read its own live page (`SRC-086`) — and the loop displays
  that at S4, in Nocturnal Veḷi, as a limit on its own ignorance-claim rather
  than as a grievance. The second candidate, `RA-015`'s finding that no
  non-European scholarly source is reachable, is a real `NOT ACCESSIBLE`
  asymmetry; it is displayed at S2 (§6.2) rather than made a posture, because it
  bears on the loop's instruments everywhere and not on one screen.
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
The departure is recorded rather than hidden.

**Rev. 1 justified it with `PUR4J-018`'s "no geography" clause, which §3.6 has
now withdrawn as an over-extension. The departure survives on two of §8.7's
named prohibitions instead**, which is narrower and checkable. Two hydronym
tokens across twenty-three stanzas can be mapped only by rendering approximate
locations as points — §8.7 prohibition 4 — and the twenty-one stanzas carrying
none would render as blank, which is prohibition 5, *"Render unknown as
blank."* A map of this claim set violates two of the eight whatever care is
taken, because the failure is in the data's shape rather than in the rendering.

**So the finding against the matrix stands, stated more carefully:**
"mandatory" in the Atlas column cannot hold for a Living Signal Field exhibit
whose relations are not spatial, because §1.7 and §8.7 then contradict each
other and §8.7 is the one carrying a falsifiable list. Recorded in §12.

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

**Surface.** The Question node's own landing, `mk:qst:varna-23` (framework
§6.6). **Not `index`** — see §0 and §9. Posture **Nocturnal Veḷi**; environment map function
*"Threshold, deep time, unknowns"*, desired effect *"Vastness without menace"*
(`INHERITED-UNVERIFIED`).

**Displays.**

1. The question, in full, as §4 states it.
2. `VAR-001` (`VERIFIED`) — the word occurs **23 times** in the Rigveda, in 23
   stanzas and 21 hymns — with its status badge, its source ids and its
   retrieval date `2026-09-07` visible on the face of the screen, not behind a
   control.
3. The corpus, named by edition and commit, not by date. §4.
4. Nothing else: no image, no second claim, no menu. **This is a constraint on
   the Question landing, which the loop is specifying. It is not a
   specification of any MVP page's content** — rev. 1 wrote it about `index`
   and independent review was right that doing so crossed `D-032`.

**Actions.**

- **`Begin`** → S2.
- **`Sources`** → Source Mode on the Question node. What Source Mode shows here
  is short and is the point: `SRC-019`, `SRC-022`, `SRC-023`, `SRC-085`, and the
  fact that **no Date Assertion for the Rigveda exists in any register**. The
  visitor learns at the arrival screen that the institution will tell them what
  it has not got.

  **That last statement has no register row, and the loop may not display it
  until it has one.** It is exactly the shape of `VAR-008` — a claim about what
  this repository does and does not hold — and `VAR-008` was given a `VERIFIED`
  row and a ledger row (`SRC-086`) precisely because a statement of that shape
  needs one. Rev. 1 displayed it unrostered. It is `U3` in §7.6 and `W-8` in
  §8.1.

**Rules.**

- **The arrival asserts one claim and it is `VERIFIED`.** A question asserts
  nothing (§3.1); the count is offered beside it as the size of the evidence,
  not as an answer.
- **The arrival leads with the question, not with the ignorance.** The openness
  at S1 lives in the question's second clause — *"and what does it mean
  there?"* — rather than in an announcement. Saying it at S1 and showing it at
  S4 would make S4 a restatement; the loop's arc is the difference between
  saying and showing.

  **Rev. 1 wrote this rule as "the arrival does not preview S4", which described
  a withholding rather than an ordering, and it paired with a second withholding
  at S2 that independent review was right to call dramaturgy.** §6.2 now states
  the rule that governs both: nothing in the loop is hidden from the visitor at
  any screen; Source Mode reaches the whole register from all five, and the
  sequence chooses what to *lead* with, not what to make available.

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
`03-REGISTERS/rigveda-varna-occurrences.csv`, `VAR-OCC-001` to `VAR-OCC-023`.

**It is a view over eight of the register's fifteen columns, and the screen says
so and names the other seven.** Shown: stanza, pada, token index, surface form,
lemma, morphology, Arnold stratum, stratum certainty. Not shown by default:
`lemma_id`, `arnold_stratum_code`, `source_id`, `retrieval_date`, and — the two
that matter — **`sense` and `sense_source`**. A control on the screen adds any of
them, and Source Mode reaches the full register in one interaction from here as
from everywhere (§1.7).

**Rev. 1 called this screen *"the register, not a rendering of it"* and did not
name the omitted columns.** Independent review was right that this was
dramaturgy: the institution held a column, filtered it out of the surface it
called the register, and revealed it one screen later for effect — while §6.4
claimed the ignorance was *"not asserted"* but *"displayed at the granularity of
the evidence."* It was displayed at S4 because it had been suppressed at S2.

**The rule that now governs, at S2 and everywhere:** *the loop chooses what to
lead with, never what to make available.* The `sense` column is one control away
at S2 and one interaction away in Source Mode from all five screens. S4 is not a
reveal; it is where the empty column is **read** — against its absence record,
its coverage, its date and its scoping limit, none of which S2 supplies. The arc
survives the correction and is weaker and truer for it. Logged as `BF-026`.

**Displays.** `VAR-001`, `VAR-005`, `VAR-006`, `VAR-007` (all `VERIFIED`);
`VAR-002` (`PROVISIONAL`); `PUR-001`, `PUR-002`, `PUR-011`, `PUR-012`, `PUR-013`
(all `VERIFIED`); `PUR-028` (`HYPOTHESIS`). Non-claim records: `VAR-OCC-001` to
`VAR-OCC-023`; `DEP-001`, `DEP-002`, `DEP-004`, `DEP-005`, `DEP-021`, `DEP-023`,
`DEP-024`; `APA-E-006`; `RA-015`. Rev. 1 displayed three of the seven dependency
rows and not `RA-015`.

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
  transcription (`SRC-020`, Aufrecht), the padapāṭha reading (`SRC-021`,
  Lubotsky), and the bundled translations, each labelled by `is_primary` so the
  visitor can count the steps between the token and the English. **Original
  script is displayed and the transliteration scheme is named**, per framework
  §7.1 rule 5 — *"Original script always available; transliteration is an
  addition, never a replacement, and the transliteration scheme is named"* —
  which rev. 1 specified on no screen while displaying `várṇam` in IAST five
  times, and which independent review caught. It applies to every screen in this
  loop, not only to S2.

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
  expected count is below 6 in **all five** stratum cells, so the numbers are
  reported as measurements and nothing more. The grouping control renders counts
  and **no test statistic**, and carries that sentence, sourced to `VAR-005`.

  **The figure is `VAR-005`'s corrected one, not the one the corrections brief
  prints.** `CORRECTIONS-PENDING.md` brief 4 §4.2.4 still reads *"expected counts
  in three of five cells are below 6"*; `VAR-005`'s note records the correction
  to all five, and that document's §5.1 defect 12 lists the fix as made without
  applying it to §4.2.4's body. Rev. 1 cited §4.2.4 while silently using the
  corrected figure. That is `IC-P-002`'s pattern a second time in the same
  document, one subsection away — recorded as **`IC-P-004`**. It is also what
  `IC-P-003`'s own action column asked for and rev. 1 did not run: *"any
  correction to a `VERIFIED` row needs a sweep of the documents that quote it,
  not a fix at the site where it was noticed."*
- **Arnold's strata are not dates, and the surface says so at the control, not
  in a footnote.** `PUR-028` is a `HYPOTHESIS` — *"Arnold's five periods
  correspond to real chronological stages of composition"* — and it is
  untested. `APA-E-006` is displayed beside the grouping control, not in Source
  Mode: Arnold, Cambridge 1905, *"working within the philological assumptions of
  his period"*, and *"whether the metrical layering tracks composition date at
  all is an assumption inside the instrument, not a result from it."* The
  control is labelled **"group by Arnold's periodisation"**, never "by period".
  This placement is a correction made under `BF-021`; see §11.
- **Four source ids, two sources, one channel.** The grouping controls cite
  `SRC-019`, `SRC-022`, `SRC-023` and `SRC-085`. The screen displays `DEP-024` —
  those are *"Same repository at the same commit `d3eb8af`, fetched a third
  time"*, and *"The three count as ONE source"* — and `DEP-001`, which makes
  `SRC-023` a transcription of `SRC-026`, Arnold 1905, rather than a second
  witness to it. **Rev. 1 wrote "four source ids, one source", which is wrong in
  the direction that flatters the display**: `DEP-001` puts a different author,
  Arnold, behind `SRC-023`'s content. Two sources reached through one retrieval
  channel is the honest count, and the distinction is what the screen is
  teaching. (Rev. 1 also ran an ellipsis across a column boundary inside that
  quotation, joining `DEP-024`'s `relationship` field to its
  `effect_on_status` field as though they were one sentence; the two fragments
  are now quoted separately.)
- **The dependencies that govern what S3 argues from are shown here too**, and
  rev. 1 displayed none of them. `DEP-005`: the Zurich lemmatisation and the
  Grassmann gloss *"travel together in the same annotation layer. A claim that
  cites the lemma and a claim that cites the meaning are one source, not two"* —
  so `VAR-001`, the count, and `VAR-003`, the eight senses, are **one
  instrument**, and S2 and S3 must not present them as two. `DEP-004`: Arnold's
  Popular stratum and the book-order instrument *"are not independent measures of
  lateness"* — so actions (a) and (b), the visitor's two groupings, are not two
  independent views of the same rows, and the screen says so at the second
  grouping rather than letting the reproduction of two `VERIFIED` claims imply
  two instruments.
  Framework §9.2 stage 3 calls the independence tree *"the single most
  instructive thing this mode can teach"* — said of its example, nine citations
  resolving to one 1953 report. This loop teaches it one screen early, because S2
  is where the visitor is being persuaded that the numbers hold.
- **The instrument set is European throughout, and the screen says so.**
  `RA-015` (`OPEN`, `HIGH`): every source in this line of work *"sits in one
  German philological line"*, and *"There is NO non-European scholarly source
  anywhere in the unit. Sayana's commentary — the indigenous exegetical
  tradition, and the one Griffith leaned on — is not in the pinned corpus and was
  not retrieved. This is an archival asymmetry, not a neutral fact about what
  exists."* Displayed beside `APA-E-006`, not behind a control. Rev. 1 put this
  finding in its own §11 and on no screen — which meant the asymmetry the visitor
  saw was the one that flatters the institution, and the asymmetry they did not
  see was the one that does not.
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
smoothed over, not replaced by a strawman, and not omitted.

**Rev. 1 gave a reason for that gap and the reason was wrong.** It cited
`APA-E-003` as typing *"the relevant secondary literature"* — Witzel 1999,
Kuiper 1991, Masica 1979, Krishnamurti 2003, Rau 2019, Shorto 2006 — as `NOT
ACCESSIBLE`, quoting *"attested and reconstructed families have machine-readable
derivatives on GitHub; proposals about unattested donors do not."*
`APA-E-003`'s own scope line says what it is about: *"the entire secondary
literature of the **substrate question**."* Those six works are the substrate
bibliography. **None of them is a source for "Rigvedic *varṇa* already carries a
social sense", and the caste-sense account is not a proposal about an unattested
donor.** The quoted justification does not reach the use. Rev. 1 also printed
`APA-E-003`'s conclusion as *"follows the retrieval channel rather than the
evidence"*, inside quotation marks; the row reads *"the split follows the
channel, not the evidence (DE-I-001, HOLD-005)"*, and the misquote reached
`BF-021` before it was caught.

**What the screen says instead, which is worse for the institution and true.**
**No probe, no ledger row and no `05-HOLDS/` row exists for Vedic social-history
literature at all.** Nobody here has tried. Rival 3 is not blocked — it is
**undone**, which is the exact distinction S4 and `D-046` exist to draw, and
rev. 1 called it "partly blocked" on the one screen whose job is to state the
rival fairly. Calling undone work blocked, in order to present an opponent's
account as a gap rather than as a claim, is `BF-022`'s failure running the other
way, and neither of rev. 1's §11 tests fired on it. Logged as `BF-027`.
Registering rival 3 is `W-4` in §8.1, reclassified there from blocked to undone.

**Stage 3 — the evidence.** The 23 rows from S2, carried forward; `VAR-003`'s
eight glosses; the translations bundled with the corpus. The independence tree
from S2 is shown again here, in its proper place, and it does more work at this
stage than at S2.

**The translations are nine and the ledger holds eight, and they are four
independent lines, not nine witnesses.** `SRC-072` to `SRC-077` are Geldner,
Griffith, Grassmann, Elizarenkova, Renou and `SRC-077`'s bundle of Macdonell,
Müller and Oldenberg — **eight**. `02-SOURCES/vedaweb-manifest-2026-09-07-extension.md`
§`translations/` heads its section *"nine translations, four independent lines"*
and lists Otto at 74 rows; **Otto has no ledger row.** Rev. 1 wrote "the nine
translations, `SRC-072`–`SRC-077`" four times, which is an id range that does not
contain nine things. `VAR-004`'s own note still reads *"Nine translations are
bundled with the corpus (SRC-070 to SRC-077)"*, where `SRC-070` and `SRC-071` are
`addressees.json` and `stanza_properties.json` — the exact error
`CORRECTIONS-PENDING.md` §5.1 defect 12 records as corrected and did not apply to
that row. Recorded as **`IC-P-005`**; the ledger row for Otto is `W-9`.

**And the four lines, not nine, are what the screen displays.** `DEP-021`:
Grassmann's 1876–7 translation and his *Wörterbuch* are *"one judgement expressed
twice"*, and the dictionary is what fixed the lemma boundary this whole corpus
rests on. `DEP-023`: Elizarenkova *"was made with Geldner 1951 in view and cites
it throughout"*, so their agreement is weaker than two independent renderings and
their **disagreement** is correspondingly stronger. `CLAUDE.md`'s standing
constraint — *"Two citations tracing to the same author, excavation report or
dataset count as one"* — is the rule, and nine ids treated as nine witnesses is
its own worked example.

**Stage 4 — the gates, and two of five are unavailable.**

| Gate | Available here | Why |
|---|---|---|
| Chronological | **no** | `PUR-028` is a `HYPOTHESIS`; Arnold's letters are not dates, and `DEP-001` makes them single-sourced besides |
| Geographical | **no** | Not because the corpus has no geography — §3.6 withdraws that reading of `PUR4J-018`. `PUR4J-017` (`VERIFIED`) records which hydronym lemmas occur where, and two *varṇa* stanzas carry one; but the step from a hydronym lemma to a place is, in `PUR4J-018`'s own words, *"a separate claim needing separate evidence"*, and no such claim is registered. The gate has no data to be applied to |
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
  (`01-INHERITED/curatorial-audit-v1.1/page-audit.csv`, `what-varna-meant` row,
  `INHERITED-UNVERIFIED`). **That is a universal negative over 23 passages
  nobody in this institution has read for sense.** The screen says so.

  **This claim — the loop's entire argumentative target — has no `claim_id`,**
  and rev. 1's inventory did not list it. It reaches this repository as a cell
  in an inherited audit spreadsheet, not as a register row, so the loop displays
  the institution's own headline at a standing the institution has never
  assigned it. `U1` in §7.6; `W-8` in §8.1.
- **Two inherited rows are displayed beside it, and rev. 1 conflated them into
  one.** `IH-149` (`INHERITED-UNVERIFIED`) is the rejection: *"REJECTED by the
  handoff: Varna as 'the colour of a dawn' used as the lead"*, `R-03`, rejected
  by the owner. `IH-019` (`INHERITED-UNVERIFIED`) is correction `C-07`, and it
  is the row that carries the rule rev. 1 attributed to `IH-149`: *"both halves
  in the same breath, the indictment first, nuance after, never as a
  replacement."* A sense sort built from Grassmann's gloss lands on colour first
  by construction, which is why both rows belong on this screen. The institution
  shows the visitor the rejection it already issued against itself.
- **And the case running the other way, because `BF-018`'s control requires
  it.** *"Where a correction record is cited as evidence about this project's
  own bias, cite the cases running both ways or state that none exists."*
  Rev. 1 cited only the flattering direction. The counter-case is `IH-029`
  (`INHERITED-UNVERIFIED`), correction `C-16`, `R-09`: the handoff records that
  **Claude's caution understated a well-supported finding** — the Rakhigarhi
  sample written up as one individual where the source records twelve on a
  cline. The correction record runs both ways and the screen shows both, which
  is the difference between a correction record and a credential.
- The **asymmetry statement** (framework §11.2) rides with the pair, so the two
  challenges are not presented as balanced. `CLAUDE.md`: *"Correct both without
  pretending their archival and institutional power has been equal."*
  **Framework §11.2 makes the asymmetry statement itself a claim** — *"it is
  itself a `mk:clm:` with sources, a status and falsifiers, not a slogan"* — and
  no such claim exists in this repository. Rev. 1 displayed it as prose. It is
  `U2` in §7.6 and `W-8` in §8.1, and until it has a row the screen displays the
  requirement rather than the statement.

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

`mk:abs:varna-sense`. Framework §3.7 specifies ten fields; **rev. 1 gave eight
and claimed "none elided"**, omitting `id` and — the one that matters —
`evidence_links`, the `establishes-absence` links to the searches that bound the
absence, which is the field that makes a negative-evidence record traceable at
all. Both are restored and the completeness claim is dropped:

| Field | Value |
|---|---|
| `expected_evidence` | a per-occurrence sense assignment for *varṇa-* in the Rigveda |
| `id` | `mk:abs:varna-sense` |
| `expected_where` | (i) the Zurich lemma/morphology annotation, `SRC-022`; (ii) the lexicon, Grassmann's gloss via `matched_lemmata.json` — **`SRC-019`/`SRC-022`, not `SRC-026`.** Rev. 1 wrote `SRC-026`, which is Arnold 1905; there is no ledger row for Grassmann's *Wörterbuch*, the gloss travels inside the VedaWeb annotation layer (`DEP-005`), and `VAR-003`'s own `source_id` reads `SRC-019; SRC-022; SRC-085`. A mis-resolved source id inside the one record on the loop whose whole job is to be checkable; (iii) the translations bundled with the corpus, `SRC-072`–`SRC-077` and the unrostered Otto — eight ledger rows for nine translations, four independent lines (§6.3); (iv) this repository's own registers, `SRC-086` |
| `p_produced` | **(i) ≈ 0** — `VAR-004` (`VERIFIED`): the Zurich layer carries lemma and morphology and *no sense field*. **(ii) partial** — `VAR-003` (`VERIFIED`): Grassmann supplies the *range*, eight senses undivided, and distributes none of it over passages. **(iii) ≈ 1** — every translator chose an English word for every passage. **(iv) 0** — `SRC-086` establishes the repository held no sense column before the varṇa census |
| `p_survived` | not applicable to a digital annotation; 1 for the printed translations |
| `search_coverage` | `SRC-086`, 2026-09-07T19:15Z: full-tree `git grep` over every tracked file, plus column-name inspection of every CSV in `03-REGISTERS/`, for *varna*, *varRa*, *sense*, *human-applied*, *colour/skin* |
| `accessibility` | `SRC-072`–`SRC-077` reachable inside the `SRC-019` clone; `melakeela/site` **not** reachable (`SRC-086` blocking constraint) |
| `recognisability` | yes for the translations — a translator's English word is recognisable as a sense choice. The difficulty is *adjudicating* between nine of them, which is constitution §7's job and is not a recognition problem |
| `absence_type` | **`NOT PRODUCED`**, and **scoped to (i) alone** |
| `evidence_links` | `establishes-absence` → `SRC-086` (the full-tree search that bounds (iv)); `establishes-absence` → `SRC-022` via `VAR-004` (the annotation's field list, which bounds (i)); `establishes-absence` → `VAR-003` (the gloss, which bounds (ii) as a range without a distribution). **Nothing bounds (iii)** — no search of the nine translations has been run, which is why (iii) is not an absence and is `W-3` |

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
absence is `NOT PRODUCED`, so it is one of the seven types the framework calls
*"statements about the archive"*, and the interface renders it *"in the
archive's voice, not the past's"*. It says nothing
whatever about whether the 23 share a sense.

**So the loop needs a mechanism the framework does not currently give it**: a way
to display *work recorded as owed and not done*, which is neither an absence nor
a hold. Framework §11.1 has negative rows in the Institutional Obligations
Register — whose §1.6.2 table row reads *"refused requests, unanswered letters,
unreturned objects, consultations not held"* — but they are attached to
Reconnection only, and they are obligations to third parties rather than to the
record. Inherited standing rule 12 (`IH-347`, `INHERITED-UNVERIFIED`) types the
page's state — *"A search named as owed is a dependency; a page depending on it
is INCOMPLETE"* — and says nothing about what the page may display, which is why
it does not close the gap. Raised as
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
  **including that search's own limit**, quoted whole rather than truncated at a
  comma as rev. 1 quoted it: *"Establishes only what this repository holds. It
  says nothing about what what-varna-meant.html holds: melakeela/site is not
  accessible from this session…"*

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
present any of the above as repair achieved"*, and that *"A published
access-status record is a record of a state, including the state “still
withheld”."* Applied to this
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

Every row the five screens put in front of a visitor. Statuses are as recorded on
2026-09-08; none was changed by this unit.

**Scope of this section.** It inventories what the five *screens* display.
Register ids cited elsewhere in this file — `PUR4J-003` in §1, `IH-347` in `W-7`,
the `BF-` and `RA-` rows in §11 — are evidence *about this specification* and are
not displayed by any screen, so they are not inventoried here.

**Rev. 1's inventory was incomplete and independent review found five omissions
and two wrong screen assignments.** The completeness of a claim inventory is the
one guarantee this repository exists to give — framework §6.7: *"Every route
shows the status of everything it displays"* — so the failure is recorded rather
than silently patched, and §7.6 now carries the propositions the loop displays
that have no register row at all, which rev. 1 did not have a section for.

### 7.1 `03-REGISTERS/rigveda-varna.csv`

| `claim_id` | Status | What the loop uses it for | Screens |
|---|---|---|---|
| `VAR-001` | `VERIFIED` | the count: 23 tokens, 23 stanzas, 21 hymns | S1, S2 |
| `VAR-002` | `PROVISIONAL` | why the inherited 23 and the measured 23 are not two sources — the denominator does not match | S2 |
| `VAR-003` | `VERIFIED` | Grassmann's eight senses in one undivided string, distributed over nothing | S3, S4 |
| `VAR-004` | `VERIFIED` | the annotation carries no sense field, and no retrieved source assigns a sense per occurrence | S4 |
| `VAR-005` | `VERIFIED` | the stratum distribution the visitor reproduces; and the all-five-cells figure the grouping control carries | S2 |
| `VAR-006` | `VERIFIED` | the book distribution the visitor reproduces | S2 |
| `VAR-007` | `VERIFIED` | the compound boundary: 23 further tokens, 12 lemmas | S2, **S4** |
| `VAR-008` | `VERIFIED` | the sense sort is owed and has not been done | S4 |
| `VAR-009` | `HYPOTHESIS` | the proposition the PROVE IT run is anchored on — displayed **as** a hypothesis, which is its correct use | S3, S5 |

### 7.2 `03-REGISTERS/rigveda-pur-family.csv` and `rigveda-pur-4j-claims.csv`

Displayed because S2 shows a stratum column and S3 works a geographical gate,
and neither can be done honestly without them.

| `claim_id` | Status | What the loop uses it for | Screens |
|---|---|---|---|
| `PUR-001` | `VERIFIED` | the corpus size, 164,758 tokens — the denominator behind `VAR-002` | S1 (Source Mode), S2 |
| `PUR-002` | `VERIFIED` | every token carries a lemma; 164,755 carry a stratum — the coverage behind `VAR-001` and `VAR-005` | S2 |
| `PUR-011` | `VERIFIED` | what Arnold's letters mean, and what the small italics mean — makes the `stratum_certainty` column readable | S2 |
| `PUR-012` | `VERIFIED` | 9,607 stanzas uppercase, 945 lowercase — the scale of the certainty distinction | S2 |
| `PUR-013` | `VERIFIED` | `strata.json` attributed to Arnold 1905, compiled by Gunkel and Ryan, CC-BY-4.0 | S2 |
| `PUR-028` | `HYPOTHESIS` | that Arnold's periods are real chronological stages — displayed **as untested**, at the grouping control and at the chronological gate | S2, **S3** |
| `PUR4J-017` | `VERIFIED` | which hydronym lemmas occur in a passage is a textual fact — added in rev. 2; it is what makes the geographical gate's exclusion narrow and true rather than over-extended | S3 |
| `PUR4J-018` | `VERIFIED` | the §4J geography field cannot be filled, and the hydronym-to-place step is a separate unregistered claim — **used at its own scope**, not as "no geographic content of any kind" (§3.6) | S3 |

### 7.3 `03-REGISTERS/inherited-claims.csv`

All `INHERITED-UNVERIFIED`, displayed as such. Their value is that they are old,
not that they are verified, and none of them does evidentiary work anywhere in
the loop: each is displayed as a record that a thing was said or decided.

| `claim_id` | Status | What the loop uses it for | Screens |
|---|---|---|---|
| `IH-019` | `INHERITED-UNVERIFIED` | correction `C-07`, and the standing rule *"both halves in the same breath, the indictment first, nuance after, never as a replacement"* — **added in rev. 2**; rev. 1 attributed this rule to `IH-149` | S3 |
| `IH-029` | `INHERITED-UNVERIFIED` | correction `C-16`, `R-09` — the logged case running the other way, where the handoff records that Claude's caution understated a well-supported finding. **Added in rev. 2** under `BF-018`'s control | S3 |
| `IH-086` | `INHERITED-UNVERIFIED` | the inherited count and its `NEEDS-CHECK` note on the human-applied split | S2, S4 |
| `IH-149` | `INHERITED-UNVERIFIED` | the `REJECTED` row `R-03` itself — leading with *varṇa* as "the colour of a dawn", rejected by the owner | S3 |
| `IH-287` | `INHERITED-UNVERIFIED` | handoff work item 19: the split and the colour/skin count *are owed* | S4 |

### 7.4 Non-claim records the loop displays

Not claims, and not given claim statuses; each is displayed as the record type it
is.

| Record | Register | Screens |
|---|---|---|
| `VAR-OCC-001` … `VAR-OCC-023` | `03-REGISTERS/rigveda-varna-occurrences.csv` | S2, S4 |
| `DEP-001`, `DEP-002`, `DEP-004`, `DEP-005`, `DEP-021`, `DEP-023`, `DEP-024` | `02-SOURCES/dependency.csv` — rev. 1 displayed the first, second and last only | S2, S3 |
| `APA-E-003`, `APA-E-006` | `04-AUDITS/ARCHIVE-AND-POWER-AUDIT.csv` | S2, S3 |
| `RA-015` | `04-AUDITS/REAUDIT-QUEUE.csv` — the no-non-European-source asymmetry. **Added in rev. 2**; rev. 1 restated its finding in §11 without citing it and put it on no screen | S2 |
| `BF-016`, `RA-017` | `04-AUDITS/BIAS-FAILURE-LOG.csv`, `REAUDIT-QUEUE.csv` | S4 |
| `IC-P-002` | `04-AUDITS/INTERNAL-CONTRADICTIONS.csv` (added by this unit) | S4 |
| `mk:abs:varna-sense` | **does not exist**; specified in §6.4 element 2 | S4 |
| `SRC-019`, `SRC-020`, `SRC-021`, `SRC-022`, `SRC-023`, `SRC-026`, `SRC-072`–`SRC-077`, `SRC-085`, `SRC-086` | `02-SOURCES/access-ledger.csv` — `SRC-021` added in rev. 2 | all five, via Source Mode |

### 7.5 The count

| Status | Claims |
|---|---|
| `VERIFIED` | 14 |
| `PROVISIONAL` | 1 |
| `HYPOTHESIS` | 2 |
| `INHERITED-UNVERIFIED` | 5 |
| **Total registered claims displayed** | **22** |

By register, as `VERIFIED` / `PROVISIONAL` / `HYPOTHESIS` /
`INHERITED-UNVERIFIED`: `rigveda-varna.csv` nine rows, 7 / 1 / 1 / 0; the *púr-*
registers eight rows, 7 / 0 / 1 / 0; `inherited-claims.csv` five rows,
0 / 0 / 0 / 5. Rev. 1 listed 19 rows and counted 13 `VERIFIED`; rev. 2 adds
`PUR4J-017`, `IH-019` and `IH-029`.

**This table is a hand tally and that is a known weakness, not a hidden one.**
`06-BRIEFS/mvp-fifteen/README.md` — the precedent this file invokes twice —
states: *"Every count in this directory is derived at build time. None is a typed
literal."* Inherited standing rule 14 says the same. There is no build script for
this unit, every figure here is typed, and rev. 1's inventory was wrong by five
rows while its arithmetic was internally consistent. **Internal consistency is
exactly what a hand tally guarantees and completeness is exactly what it does
not.** A generator that walks §6 and asserts the result against `03-REGISTERS/`
is `W-11`; until it exists, `RA-020` covers this table.

### 7.6 What the loop displays that has no register row

**Five propositions. Rev. 1 had no section for these and displayed all five.**
Framework §6.7: *"Every route shows the status of everything it displays."* Each
of these is displayed without one, so each is a live breach until `W-8` closes
it, and the loop as specified is `INCOMPLETE` in the sense inherited standing
rule 12 gives the word — *"A search named as owed is a dependency; a page
depending on it is INCOMPLETE."*

| | Displayed proposition | Screen | Why it has no row |
|---|---|---|---|
| `U1` | *"Varṇa means colour. It never means occupation."* — the page's central public claim, and the loop's whole argumentative target | S3 | It reaches this repository as a cell in `page-audit.csv`, an inherited audit spreadsheet. No claim register carries it. The institution's own headline has never been assigned a status by the institution |
| `U2` | The §11.2 asymmetry statement, which rides with the two bias tests | S3 | Framework §11.2 requires it be *"itself a `mk:clm:` with sources, a status and falsifiers, not a slogan"*, and no such claim exists here |
| `U3` | *"No Date Assertion for the Rigveda exists in any register"* | S1, Source Mode | It is the same shape as `VAR-008` — a claim about what this repository holds — and `VAR-008` was given a row and a ledger row for exactly that reason |
| `U4` | The n = 23 no-inference sentence at the grouping control | S2 | Now sourced to `VAR-005`, which does carry it. Listed because rev. 1 sourced it to `CORRECTIONS-PENDING.md` §4.2.4, which is prose and carries the superseded figure (`IC-P-004`) |
| `U5` | **The posture sequence itself** — that these five relationships in this order are how a visitor should meet this evidence | the whole loop | `D-021` option 2 requires a guided sequence to get *"an `mk:clm:` with sources, alternatives and falsifiers."* §15 supplies the falsifier and the rivals; the claim id is `D-021`'s to authorise, and is `W-10` |

**No `REJECTED`, `SUPERSEDED` or `HOLD` row is displayed by this loop.**
`IH-149` reports a rejection made by the owner in a prior thread and is itself
`INHERITED-UNVERIFIED`, not a `REJECTED` row in this namespace.

## 8. Can the loop be built from `VERIFIED` claims alone? No. What it needs, and which unit produces it

**No.** Two things the loop stands on cannot be promoted by any retrieval at all
(§8.0). Eleven units of work would close the rest, one of which — `W-3` — would
destroy the screen it fixes, and §8.3 says why that is the point.

**Eleven, not the seven rev. 1 listed.** Independent review added four: `W-8`
(register the five propositions the loop displays with no row, §7.6), `W-9` (the
missing ledger row for the ninth translation, and `VAR-004`'s superseded source
list), `W-10` (a claim id for the sequence, `D-021`'s to authorise) and `W-11`
(a generator for §7, the control that would have caught rev. 1's omissions).
Review also reclassified `W-4` from blocked to undone and enlarged `W-5`.

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
and `IH-019` record an owner decision and a correction taken in prior chat
threads. `CLAUDE.md` is explicit:
those are the `HD-` namespace, they stay `INHERITED-UNVERIFIED`, and a register
row would be a promotion. If the owner re-affirms `R-03`, that is a fresh `D-`
allocated then. The loop displays it correctly today, as an inherited record.

### 8.1 The units of work

| | Unit | Produces | Blocked? |
|---|---|---|---|
| **`W-1`** | **The Editorial Register.** `03-REGISTERS/editorial-decisions.csv`, to framework §11.5's schema — `decision_id` · `subject` · `decision_type` · `value` · `derived_value` · `override_reason` · `derived_residual` · `rationale` · `decided_by` · `decided_date` · `supersedes` · `state` · `notes`, with `decision_type = posture-assignment`. **Rev. 1 specified this register from §1.5's prose field names and dropped seven of §11.5's thirteen columns**, which would have built a register that does not satisfy the section it cites. Write five rows, one per screen, each recording that the posture is assigned rather than derived and why (§3.4) — the S4 row is the one that matters, and had it existed, rev. 1's misquote of rule 3 would have had to be written into an `override_reason` field where it could be checked. | An auditable posture assignment for every screen. Promotes nothing; makes an editorial act visible instead of implicit. | No. Small unit, no retrieval. |
| **`W-2`** | **The denominator.** `VAR-002` is `PROVISIONAL` because `IH-086`'s 180,196 words is not the pinned corpus's 164,758 tokens — a 15,438-token gap between two tokenisations, unexplained. Retrieve `gret_scan.json`, or the tokenisation it used, and reconcile. | `VAR-002` at `VERIFIED`, or a `HOLD` row and a clean statement of the gap. | Partly. The file is not in this repository. If unreachable → `05-HOLDS/`, and S2 states the gap rather than the reconciliation. |
| **`W-3`** | **The sense reading.** The unit brief 4 §4.3 already scopes: all 23 passages against `SRC-072`–`SRC-077` under constitution §7's translation standard — original script, transliteration, grammatical form, semantic range, textual context, edition, exact locator, translation used, alternatives, interpretive consequence — plus the `inherited_category_audit` on *caste*, *colour* and *class*. Tests `VAR-009`. | 23 Translation Blocks; `VAR-009` resolved or refined; the `sense` column filled or explicitly typed per occurrence. | **No. Nothing blocks it but the work.** The translations are inside the `SRC-019` clone. |
| **`W-4`** | **Register the rival.** Give the official account — that Rigvedic *varṇa* already carries a social sense — a Claim Object with its own sources, so S3 stage 2 states a rival rather than a gap. | A rival with a status, sources and a standing (constitution step 11). | **Not blocked. Undone.** Rev. 1 called it "partly blocked" on `APA-E-003`, which covers the *substrate* literature and does not reach the caste-sense account (§6.3). **No probe, no ledger row and no `05-HOLDS/` row exists for Vedic social-history literature: nobody here has tried.** The first step is a retrieval attempt and a ledger row, not a hold. If that attempt fails, *then* a `HOLD`. Logged as `BF-027`. |
| **`W-5`** | **RV 10.90, and the compound stanza list.** Three parts, not two. (a) None of the 23 simplex occurrences falls in RV 10.90 — this follows from `VAR-001` and the 23 stanzas listed in the occurrence register. (b) The stanza list for `VAR-007`'s 23 compound tokens, from the corrected census script, which is what makes (a) safely scopable to the simplex. (c) **`BF-002`'s control, which rev. 1 did not cite and which governs this exactly:** *"No absence claim about a named entity in the Rigveda may rest on a lemma search alone. Surface search plus hand typing, or the claim does not get made."* So (a) is **not** a free register row derivable from what is on file; it needs a surface search of RV 10.90 and hand typing before the claim is made at all. Rev. 1 deferred the *display* and still wrote the proposition into §8.2, which is not the same as not making it. | Register rows that let the loop connect to the `one-verse` page's claim — *"The explicit fourfold varṇa scheme appears together in one Rigvedic verse"* (`INHERITED-UNVERIFIED`, page-audit Decision `Revise`). | No, but larger than rev. 1 said: a surface search plus hand typing, not one row from data on file. Still the highest value per unit of effort in this list. See §8.2. |
| **`W-6`** | **Read the live page.** Repository access to `melakeela/site`, so `what-varna-meant.html`'s own text can be retrieved rather than reported. | S3 can attribute the page's claim to the page. Closes `SRC-086`'s stated limit and lets constitution step 13 run properly on this subject. | **Blocked on the owner.** Already named in `SRC-086`'s `owner_action_required`. `RESEARCH-QUEUE.md` `## Not yet` lists *"Anything touching melakeela/site."* |
| **`W-7`** | **A display mechanism for owed work.** Neither an absence (`CLAUDE.md`'s eight types do not cover it, and "NOT ATTEMPTED" was struck down as an invented ninth) nor a hold (nothing blocks it). Framework §11.1's negative rows — *"refused requests, unanswered letters, unreturned objects, consultations not held"*, listed in §1.6.2's Reconnection table — are the nearest fit and are obligations to third parties rather than to the record. **Inherited standing rule 12 already supplies a disposition and rev. 1 did not mention it:** *"A search named as owed is a dependency; a page depending on it is INCOMPLETE"* (`IH-347`, `INHERITED-UNVERIFIED`). `D-046` must say why rule 12 is not enough — the answer being that rule 12 types the page's *state* and says nothing about what the page may *display*. | S4 element 3 gets a specified record type instead of an ad-hoc display. | **Blocked on `D-046`**, allocated by this unit. A publication-approval question: does the institution publish its own undone work? |
| **`W-8`** | **Register the five unrostered propositions**, §7.6 `U1`–`U5`. Chiefly `U1`: give `what-varna-meant`'s central public claim a `claim_id` and a status, so the institution's own headline is held to the standard the institution applies to everything else. | Closes five live breaches of framework §6.7. | `U1` is partly downstream of `W-6` (the page cannot be read); the audit cell can be registered as *"what the 2026-09-01 audit records the page as claiming"* today. `U2` needs framework §11.2's sources and falsifiers. `U5` is `D-021`'s. |
| **`W-9`** | **Two ledger corrections.** (a) A row for the ninth translation, **Otto**, 74 rows, listed in `vedaweb-manifest-2026-09-07-extension.md` and absent from `02-SOURCES/access-ledger.csv`. (b) `VAR-004`'s note still reads *"SRC-070 to SRC-077"* for the translations, the error `CORRECTIONS-PENDING.md` §5.1 defect 12 records as corrected. `IC-P-005`. | Nine translations addressable by id; a `VERIFIED` row stops citing two JSON files as translations. | No. Small unit, no retrieval — (a) is a ledger row for a file already inside the `SRC-019` clone. |
| **`W-10`** | **A claim id for the sequence**, per `D-021` option 2: *"the sequence itself gets an `mk:clm:` with sources, alternatives and falsifiers."* §15 drafts the alternatives and the falsifier. | The loop becomes challengeable in PROVE IT like anything else it displays. | **`D-021`'s to authorise.** This file does not allocate one. |
| **`W-11`** | **A generator for §7.** A script that walks §6, extracts every id displayed, asserts each against `03-REGISTERS/` and prints the status distribution — so the inventory is derived rather than tallied. | The completeness guarantee §7 claims to give. | No. This is the control that would have caught rev. 1's five omissions. |

### 8.2 `W-5` deserves a paragraph of its own

The `one-verse` page asserts *"The explicit fourfold varṇa scheme appears
together in one Rigvedic verse."* The 23 simplex occurrences of *varṇa-* are at
the 23 stanzas listed in `rigveda-varna-occurrences.csv`, and **RV 10.90 is not
among them.** If that holds for the compounds too — which `W-5(b)` is what
settles — then the verse the fourfold scheme is read from does not contain the
word.

That is the sharpest thing this loop could put on S3, and **the loop may not
display it today.** Two reasons, and rev. 1 gave only the first. A derivation
from two registers is not a claim until it is a row. And `BF-002`'s control
governs it directly: *"No absence claim about a named entity in the Rigveda may
rest on a lemma search alone. Surface search plus hand typing, or the claim does
not get made."* The proposition above rests on a lemma search. So it is not one
register row away — it is a surface search plus hand typing away, and rev. 1
underestimated `W-5` by writing "no new retrieval".

**And writing it out in this paragraph, even to defer its display, is already
close to the line `BF-002` draws.** The sentence is left standing rather than
deleted, in a specification that no visitor sees, with the control named against
it — which is the disposition `CLAUDE.md` prescribes for reasoning that must stay
visible so it is not re-proposed. Whether that is sufficient is a fair thing for
review to press on.

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

## 9. `index`, and why it is not the arrival

Rev. 1 put S1 on `index` — MVP rank 1, Nocturnal Veḷi, the threshold — and
specified its content down to *"No image. No second claim. No navigation
menu."* Independent review held that this crosses `D-032`'s line, *"Nothing in
this repository acts on the MVP set until this is answered"*, and it is right:
specifying what a page contains is designing it, whatever the surrounding
paragraph calls it. Rev. 2 moved the arrival to the Question node's own landing,
which framework §6.6 makes a first-class addressable surface with the same
default posture.

**What the move costs, stated so it is not pretended away.** The loop now has no
threshold. §6.1's argument about restraint at arrival has to be carried by the
Question landing, which is a working surface rather than a doorway, and the
environment map's *"Threshold, deep time, unknowns"* function is exercised by
only one of the loop's two Nocturnal Veḷi screens. That is a real loss.

**What it buys.** No MVP page appears in the loop, so the specification is
independent of `D-032` and of `D-034`, and the owner can act on it without
answering either.

**If `D-032` is later answered in a way that admits `index`**, the variant is one
substitution: S1 moves to `index`, resolving to the same Question node, with the
same posture, the same claim set and the same two actions. Nothing else in the
loop changes — the posture sequence, the inventory, the four elements of S4 and
the three affordances of S5 are all unaffected. The variant is recorded, not
specified: its content would be `index`'s to decide, not this file's.

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
argument, which is the opposite of what §3.4 assigns it — and §3.4 is an
assignment, not a derivation, which is the correction that section carries.

**Adding a sixth screen** — a Living Tiṇai or Extraction / Collection stop — was
rejected on the evidence, per §3.6. Neither posture's derivation rule fires on
this claim set, and occupying a posture the evidence does not support is exactly
what the environment map's `Avoid` column exists to catch.

---

## 11. The two adversarial tests, run on this unit

Constitution §8 and `CLAUDE.md`: both before the unit is called finished, logged
whether or not they found anything, and running one is a failed test (framework
§3.11). **Rev. 1's tests found two things. Independent review then found six more
that the same two tests should have caught, and the pattern in what they missed
is itself the finding.**

### 11.1 Prestige-bias challenge

*Did this unit privilege a claim because it is canonical, Sanskritic,
Brahmanical, Indo-European, European, colonial, institutionally prestigious,
repeatedly cited or nationally useful?*

**Found: yes, four times.** Two by rev. 1's own test (`BF-021`), two by review
(`BF-023`, and the `RA-015` omission below).

**(i) The instruments.** The loop is built end to end on European philology — a
German lexicon (Grassmann), a British metrist (Arnold, Cambridge 1905), a Swiss
annotation layer (Zurich) — and rev. 1 put `APA-E-006` in Source Mode, where a
visitor reaches it only by choosing to. That presents European philological
infrastructure as the neutral substrate on which a counter-account is built.
**Corrected:** `APA-E-006` is a foreground element at the grouping control, and
the control is labelled *"group by Arnold's periodisation"*, never *"by
period"*.

**(ii) The subject.** A Vedic Sanskrit subject for this institution's smallest
complete loop, on a Tamil-named platform. **Not corrected** — it cannot be,
inside this unit, because the alternatives are on `HOLD-002` to `HOLD-005`.
Stated in §1: the loop's subject was chosen from a shelf the egress policy
stocked.

**(iii) The superlative that defended it.** Rev. 1 wrote that *varṇa* is the only
subject here with a *"dense set of `VERIFIED` claims"* and the four other
properties. It has **7** `VERIFIED` rows, the thinnest of any subject register,
and the forts meet all five properties at roughly fourteen times the density.
**This is the prestige failure the test was supposed to catch and instead
committed**: an inconvenient count was asserted rather than derived, in the
direction that justified a choice already made. `BF-023`, corrected in §1.

**(iv) `RA-015`, already on file, uncited and undisplayed.** The re-audit queue
already carried the sharper finding — *"There is NO non-European scholarly source
anywhere in the unit. Sāyaṇa's commentary… is not in the pinned corpus and was
not retrieved. This is an archival asymmetry, not a neutral fact about what
exists."* Rev. 1 restated a weaker version of it in this section as though new,
did not cite `RA-015`, and put it on no screen. **So the asymmetry a visitor met
was the one that flatters the institution and the asymmetry they did not meet was
the one that does not.** Corrected: `RA-015` is displayed at S2 (§6.2), cited in
§1, and added to `BF-021`'s re-audit references.

### 11.2 Preferred-counter-narrative challenge

*Did this unit accept a claim too easily because it is Dravidian, Indigenous,
anti-colonial, anti-Brahmanical, subaltern, diffusionist or politically
corrective?*

**Found: four, and three of them are about the loop flattering its own
institution rather than about the history.**

**(i) The shape.** The loop's dramatic shape is *the museum admits it cannot back
its own anti-caste headline*, and its fourth screen is its most impressive
surface. An institution that displays its ignorance looks rigorous, and this
design converts an unmet obligation — `IH-287`, recorded as owed before this
repository existed, still open — into an asset. `BF-022`. Corrections: S4
element 3 carries the date and the open state; S5 may not congratulate; §8.3
states the review trigger.

**(ii) The reveal.** Rev. 1's S2 called itself *"the register, not a rendering of
it"* while filtering out the `sense` column, so that S4's display of the empty
column read as a discovery. **The institution staged its own candour by
withholding the evidence for one screen.** `BF-026`. Corrected in §6.2: the loop
chooses what to lead with, never what to make available; the omitted columns are
named on the screen and one control away.

**(iii) The rival called blocked.** Rev. 1 wrote that the caste-sense account
could not be registered because the literature is `NOT ACCESSIBLE`, on an audit
row about the substrate question that does not reach it. The truth is that
nobody here has tried. **Calling undone work blocked, on the one screen whose job
is to state an opponent's account fairly, is this failure running in its purest
form**, and it borrowed the vocabulary of institutional constraint to do it.
`BF-027`. Corrected in §6.3 and `W-4`.

**(iv) The correction record cited in one direction.** `BF-018`'s control:
*"Where a correction record is cited as evidence about this project's own bias,
cite the cases running both ways or state that none exists."* Rev. 1 displayed
`R-03` — the owner correcting Claude — and not `IH-029`/`R-09`, where the handoff
records that *"Claude's caution understated a well-supported finding."* A
correction record quoted only in the direction that flatters the corrector is not
a correction record. Corrected in §6.3.

### 11.3 The asymmetry between the two lists, stated rather than balanced

`CLAUDE.md`: *"Correct both without pretending their archival and institutional
power has been equal."*

`11.1(ii)` and `11.1(iv)` are facts about which archives were reachable — a
colonial and institutional asymmetry this unit did not create and cannot fix from
inside a session. Everything else on both lists is a choice this unit made and
could have made differently. **They are not the same kind of finding and the
lists are not a balanced pair.**

### 11.4 What the self-tests did not catch, and what that says

**Six of the eight findings above came from independent adversarial review, not
from §11.** Rev. 1 ran both tests, found one failure each, and called the unit
finished. The pattern in the six it missed is single and it is not subtle:
**every one of them ran in the direction that made this unit's own work look
better** — a derivation that was a choice, a subject defended by a false
superlative, a reveal staged by a withholding, undone work called blocked, a
correction record quoted one way, and an inventory whose arithmetic was internally
consistent and short by five rows.

`06-BRIEFS/mvp-fifteen/README.md` §0.1 records that independent review was run on
that unit *"in successive rounds… and every round found blocking defects"*, and
declines to state the number of rounds because *"it is a figure about this unit
that nothing derives, and standing rule 14 is what this unit has already broken
once."* **Rev. 1 quoted a different document's sentence — `CORRECTIONS-PENDING.md`
§5's *"The first run of these tests… passed this document. It should not have"*
and its fourteen defects — attributed it to that README, and supplied a number
for a unit whose README pointedly refuses to give one.** The misattribution was
committed into `RA-020`'s reason column before it was caught. `BF-028`;
`RA-020`'s text is corrected.

**This unit's self-tests are not a clearance and should not be read as one.**
What cleared rev. 1 was review, and rev. 2 has not been through it.

## 12. Findings against the framework, raised by trying to build a loop from it

Recorded because a specification that exercises another specification and reports
no friction has probably not exercised it. Findings 5 and 6 are rev. 2's and are
the ones review forced.

1. **The §1.7 matrix over-specifies Atlas Mode.** *Mandatory* in Living Signal
   Field cannot hold for an exhibit whose relations are not spatial. A map of
   this claim set violates §8.7 prohibition 4 (approximate location as a precise
   point) and prohibition 5 (*"Render unknown as blank"*) whatever care is taken,
   because the failure is in the data's shape. §1.7 and §8.7 contradict each
   other here and §8.7 is the one carrying a falsifiable list. §5 records the
   departure.
2. **There is no record type for owed work.** Between the eight absence types
   (what the archive did not produce) and `05-HOLDS/` (what we cannot reach)
   there is nothing for *what we could do and have not*. Inherited standing rule
   12 types the page's state — `INCOMPLETE` — and says nothing about what the
   page may display. **`D-046`.**
3. **The Editorial Register that §1.5 depends on does not exist.** Every posture
   assignment in this repository is unlogged, including the five this loop makes.
   `W-1`. Related: §1.5's prose field names and §11.5's thirteen-column schema
   are not the same list, and rev. 1 built `W-1` from the first and broke the
   second.
4. **§1.5's derivation and the inherited assignment agree, and rev. 1 said they
   diverged.** Run over `what-varna-meant`'s claim set, rule 6 fires and yields
   Tamil Retrofuture, which is what `page-audit.csv` assigns. The framework's
   derivation is doing its job on this page. That is worth recording as a
   positive check, and as the correction of a claim this file made in rev. 1.
5. **§1.5 has no derivation unit below the exhibit.** All seven rules are written
   over "the exhibit". A loop has five screens and one exhibit, and nothing in
   the framework postures a screen. This is the gap rev. 1 crossed silently by
   treating a screen as an exhibit, and it will be crossed again by anyone
   specifying a route rather than a page.
6. **Rule 3 is not countable as written.** *"The majority of the exhibit's
   load-bearing propositions"* needs three definitions the framework does not
   give: which propositions are load-bearing; how a claim *about* an absence
   (`VAR-008`: the sort is owed) scores against one that *is* an absence
   (`VAR-004`); and whether the denominator is claims, propositions or screens.
   Under one reading S4 is 1 of 6 and under another 4 of 6. A rule whose output
   depends on an undefined denominator cannot settle a posture, and using it as
   though it could is how `BF-024` happened.
7. **Framework §7.1 rule 5 has no enforcement point.** *"Original script always
   available"* is stated as a viewer behaviour, so a specification can display a
   consequential ancient word in IAST across five screens without tripping
   anything — which rev. 1 did. The rule needs to attach to the surface that
   displays the word, not only to the primary-source viewer.

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
- **It specifies no MVP page's content.** Rev. 1 did, for `index`; §9 records
  what removing that cost and what it bought.
- **It does not claim its own claim inventory is complete.** §7.5 is a hand
  tally, §7.6 lists five propositions the loop displays with no register row at
  all, and `W-11` is the generator that would make the guarantee real. Rev. 1
  made the guarantee without the generator and was short by five rows.
- **It has not been independently reviewed at rev. 2.** Rev. 1 was, and six of
  the eight findings in §11 came from that review rather than from this unit's
  own tests. `RA-020` is `OPEN` on rev. 2.

---

## 14. Decisions raised and engaged by this unit

**`D-046`** — Does an exhibit's uncertainty surface display work the record
states is owed and not done? Allocated in `09-DECISIONS/OWNER-DECISIONS.csv`;
prose in `DECISIONS-NEEDED.md`, because it blocks S4 element 3 as specified.

**`D-021`** — engaged, not allocated. *"A guided sequence is a real service and
it is also an argument."* Raised against the Atlas's seven §13 settings; its
principle reaches this loop unchanged, and its option 2 would require the
sequence to carry an `mk:clm:` with sources, alternatives and falsifiers. §15
supplies the alternatives and the falsifier so the decision can be taken on a
concrete case rather than in the abstract. Rev. 1 did not engage it.

No other `D-` is allocated. The placement question in §0 deliberately allocates
none, following `06-BRIEFS/mvp-fifteen/README.md` §0.

---

## 15. The falsifier for the sequence itself

Required by `D-021` option 2 and by constitution step 12, and absent from
rev. 1 — which specified a route that asserts something and gave no way to
argue with it.

**What the sequence claims.** That a visitor meets this evidence best through
five relationships in this order: *not yet known* → *known by relation* → *known
against an official account* → *not yet known, shown* → *knowable again*. Two
substantive assertions sit inside it: that measurement must precede
counter-account, and that the institution's ignorance must be shown after its
argument rather than before it.

**The rivals, stated rather than gestured at.**

| Rival ordering | What it claims instead |
|---|---|
| **Uncertainty first** — S4 before S2 | That an institution should declare what it does not know before offering anything, so nothing it offers can be mistaken for an answer. Costs the reproduction at S2, which is what makes the empty column legible |
| **No counter-account** — S1, S2, S4, S5 | That framing evidence against an "official account" is itself the prestige move, and a museum should present the measurement and the gap and let the visitor find the rivals. Costs the loop's ability to be about anything |
| **Free navigation, no sequence** | `D-021`'s option 1. Asserts nothing; risks being unusable to a non-specialist, which is `D-021`'s own stated objection |
| **Several sequences, one per rival account** | `D-021`'s option 3, *"most honest; most expensive"*. Each would need its own evidence |

**Falsifier — what would show this ordering wrong.** Visitors who complete the
loop and, at S5, record disagreement citing **the absences (stage 5)** rather
than the evidence or the gates. §9.4 already captures which of the three drove a
disagreement, so the data exists by construction. If absences dominate, S4 is
arriving too late to do its work and the *uncertainty-first* rival is the better
ordering. `direction`: `would-reject`. `currently_testable`: **no** — it needs a
published loop and recorded runs. `blocked_by`: the loop not existing.

**A second, cheaper falsifier.** If `W-3` runs and the sense reading resolves
`VAR-009` cleanly, S4 dissolves (§8.3) and the sequence loses its fourth
relationship. A four-posture loop that still works would show the fourth was
never load-bearing; a four-posture loop that does not would show it was. Either
outcome is informative and neither needs a visitor.

**Where this leaves the sequence.** It is an argument with rivals and a
falsifier, displayed as such, and it has no claim id — which is `W-10`, and
`D-021`'s to authorise.
