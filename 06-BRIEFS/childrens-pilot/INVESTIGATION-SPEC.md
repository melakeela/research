# THE HUNDRED STONE FORTS — a children's investigation, ages 8–11

**Written:** 2026-09-09
**Unit type:** product specification under museum framework §10.4 and
constitution §12. Specification only. No code. No public copy.
**Working title:** *The Hundred Stone Forts*. Not approved; `D-057`.
**Subject:** the Rigvedic *púr-* corpus — 106 tokens of seven lemmas in 103
stanzas, as registered in `03-REGISTERS/rigveda-pur-*.csv`.
**Governing question:** *why is a poem not a photograph?*

---

## 0. The shape of the thing, before the detail

A child is shown one line of a very old poem. The line says that a hundred
forts made of stone were thrown down. It is the most photograph-like line in
the whole corpus: a number, a material, an action, a beneficiary.

The child then tries to check it, in the order a child actually asks:

- **How many?** One word in that line means a hundred forts. Across the corpus,
  four fifths of the fort-lines give no number at all, and the numbers that do
  appear are only ever four: seven, ninety, ninety-nine, one hundred — and the
  same words that make "ninety-nine" count **rivers** somewhere else.
- **Made of what?** Ten lines of 103 say. Eight say metal, one says stone —
  ours — one says unbaked. Two grown-ups who translated the whole poem disagree
  about which metal.
- **Where?** The poem does not say. The museum's own table has a "where" column
  and it is empty in all 103 rows.
- **When?** The museum can put the lines in an *order*. The order comes from one
  book, by one man, in 1905, who called his own period names *provisional*, and
  who was counting rhythms. The museum has **no year** for the poem at all.
- **Has anyone dug?** People have. **This museum has not read their notebooks.**

Then the child is asked the three things they must be able to say, and the
museum shows them what it currently thinks, with its status, and what would
change its mind.

The lesson is not "old poems are unreliable." The lesson is that a poem and a
photograph answer different questions, and that laying one over the other needs
a **place** and a **date**, and this chain has neither yet. The chronology is
the weakest link and the investigation is built so that the child finds it
rather than being told about it.

**One thing this specification delivers as two-and-a-half of three, and says so
rather than claiming three.** The child's third sentence — *where the poem and
the ground do not meet* — is not, as built, a comparison of two bodies of
evidence. It is six reasons the poem alone cannot be laid on any ground, five of
which come from the poem's side, plus the sixth, which is that the museum has
not been to the ground. That is the honest shape of the thing on the evidence
held today, and it is a genuine finding: **you cannot fail to meet something you
have not gone to look at.** It becomes a real comparison when `U-1` runs and
`HOLD-008` is discharged, and not before. `D-056` is the owner's decision about
whether to ship in the meantime.

---

## 1. Design rules this specification is bound by

### 1.1 Where the rules come from

| Rule | Source | Effect here |
|---|---|---|
| Five stages, each ending in a Field Bag record | framework §10.4.3 | §3 below. Governing structure. |
| No fabricated evidence, ever | §10.4.4 | No reconstruction image, no "a fort would have looked like this", no pin on a map. |
| Reconstructions labelled, with what they were based on | §10.4.4 | None is used. If one is ever added, `REFUSED-AFFORDANCES.csv` R-07 states the condition. |
| No ethnic or national identification of objects, people or remains | §10.4.4 | R-02. |
| Human remains only under §11.2/§11.4, never as a puzzle | §10.4.4 | None in scope. R-04 states the exclusion to the child. |
| No competition, scoreboard or time pressure | §10.4.4 | R-05. |
| No sorting of human beings; no reward for extremist categories; no persecution as spectacle | §10.4.7 | R-01, R-02, R-05. The single hardest constraint on *this* subject. §6. Nothing here stages, dramatizes or role-plays a siege or its aftermath: the third constraint is met by having no such screen, not by moderating one. |
| No account, no analytics, no free-text publication, no photographs of children | §10.4.5 | R-08, R-09. |
| Field Mode forbidden in Reading Room / Extraction / Reconnection | §1.7 | Gate G-1. §2. |
| Source Mode mandatory everywhere | §1.7 | Every badge in this investigation is tappable through to the register row. §1.3. |
| Field Bag is local, keeps status, shows changes, is exportable | §10.3 | §4. |
| Every design proposition in the framework is `HYPOTHESIS` | §14.4 | Inherited by this document. Every design proposition here is `HYPOTHESIS` too. |

### 1.2 Rules from the constitution and `CLAUDE.md`

- **Step 14 shape.** The CHECK stage (§3.5) is constitution §5 step 14's public-copy
  shape at a reading age: QUESTION / WHAT IS OBSERVED / WHAT THE EVIDENCE SUPPORTS /
  WHAT COMPLICATES IT / WHAT REMAINS UNKNOWN / MELAKEELA'S CURRENT INTERPRETATION /
  WHAT WOULD CHANGE IT. The child meets all seven, renamed.
- **§4J's translation prohibition.** *"Do not automatically translate* pur *into a
  Mature Harappan city."* Carried into the children's mode as R-03 and screens
  `CP-3.3` and `CP-3.6`.
- **Attestation gradient (§4E).** An attested word, a translator's English word and
  a modern guess are three different things, and the child is shown all three
  separately at `CP-3.6`.
- **Negative-evidence standard (§6).** Two different absences appear in this
  investigation and they are **not** the same, and the specification never lets
  one wear the other's clothes. §5.
- **Nothing `INHERITED-UNVERIFIED` is shown to a child as evidence.** §1.3.

### 1.3 The four badges

The child-facing vocabulary is fixed by the inheritance:
**FOUND / WE THINK / MAYBE / WE DON'T KNOW**
(`01-INHERITED/chatgpt-project-handoff.md` L347;
`06-BACKLOG/EXPANSION-PROMPT-2026-09-07.md` L254 — both `INHERITED-UNVERIFIED`
as *text*, but they are a display vocabulary, not a claim about the past, so
their standing does not depend on retrieval).

The mapping is a **display** of status. It is `HYPOTHESIS`, like every design
proposition here, and it **never** substitutes for a status:

| Register status | Child badge | Rule |
|---|---|---|
| `VERIFIED` | **FOUND** | |
| `PROVISIONAL` | **WE THINK** | |
| `HYPOTHESIS` | **MAYBE** | |
| `HOLD`, or a typed absence, or no claim at all | **WE DON'T KNOW** | |
| `REJECTED` | **WE WERE WRONG** | Shown only where the museum is correcting itself. Never deleted — constitution's standing constraint. |
| `SUPERSEDED` | **WE CHANGED THIS** | Must point at what replaced it. |
| `INHERITED-UNVERIFIED` | *not shown as evidence at all* | A child cannot hold "somebody said this in an earlier conversation and nobody checked" apart from FOUND, whatever label is attached. Excluded rather than badged. |

**Three properties this mapping must have, and one it must not.**

1. **It is lossy and the loss is stated.** Seven statuses into four badges.
   Every screen that shows **WE DON'T KNOW** must say *which kind* of not-knowing
   it is (§5), because the two kinds in this investigation have opposite
   remedies.
2. **Every badge is tappable.** Source Mode is mandatory in every posture
   (§1.7). Tapping a badge shows the real status word, the `claim_id`, the
   source, the locator and the retrieval date. A child who wants the machinery
   gets the machinery.
3. **A badge is never awarded.** It is a property of the evidence, not of the
   child's answer. Nothing in this investigation scores, ranks or congratulates.
4. **It must not run backwards, and the level matters.** The rule is applied
   **per card**: a card may not show a badge higher than the lowest status among
   the claims *that card* rests on. A screen therefore legitimately carries
   **FOUND** cards and **WE THINK** cards side by side, which several do.
   Separately, a screen's **conclusion** — the thing the child is asked to
   conclude — may not be badged higher than the lowest status among the claims
   the conclusion rests on. `SCREEN-CLAIM-DEPENDENCY.csv` records the
   screen-level floor as a **ceiling on the conclusion**, not as a cap on every
   card, and `EVIDENCE-MANIFEST.csv` carries the per-card badge. Both are
   derived from the status columns, never chosen.
   *(An earlier draft stated this rule screen-wide and was, on its own wording,
   violated on five of fifteen screens. The rule above is what the screens
   actually specify; the wording was the defect, not the design.)*

### 1.4 Reading level

Target: a competent 9-year-old reading alone; an 8-year-old reading with an
adult. Short sentences. Numbers written as words up to ten. No word of
scholarly apparatus without a plain-language gloss in the same sentence.
Sanskrit forms are always shown *and* always transliterated, never replaced.

**One deliberate exception.** The words **poem**, **evidence**, **translation**,
**guess** and **check** are used precisely and repeatedly, because they are the
content. So are the four badges.

### 1.5 The word "fort", and why this document keeps using it

Constitution §7 lists **fort** among the ten inherited English categories that
must be audited before use. `06-BRIEFS/pur-translation-standard.md` §10 ran that
audit and records that **"fort" fails it as a default gloss**:

> *"It is serviceable for the Śambara–Divodāsa passages … It is actively
> misleading at RV 7.95.1 (a river), RV 7.15.14 (a god), RV 8.1.28 (a moving
> one), and RV 8.6.23 (a simile)."*

`04-AUDITS/REAUDIT-QUEUE.csv` **`RA-013`** is `OPEN` on every occurrence of the
word, in page copy and in register column names alike.
`04-AUDITS/BIAS-FAILURE-LOG.csv` **`BF-017`** logs a previous unit that applied
§7 rigorously to *caste* and skipped it on *fort*, and its control is binding
here:

> *"Before any word on the §7 list enters draft copy, cite the audit that
> governs it or state why the default is kept."*

**This document uses the word constantly** — in its working title, in every
screen heading, and in every indicative child-facing sentence. The reason is
stated rather than assumed:

1. **A children's surface cannot present an unglossed Sanskrit stem as its
   subject.** An eight-year-old needs a handle before they can be shown that the
   handle is wrong. There is no English word on §10's list that passes the audit
   — *stronghold* is the least committed and it is still a defended place — so
   the choice is between a failing word used visibly and a failing word used
   invisibly.
2. **`CP-3.6` is the audit, turned into a screen.** It is the only screen whose
   whole content is the §7 finding: Grassmann's earthwork definition, the case
   distribution, the three passages that break any single picture, and the seven
   English words with what each imports. The child is shown that *fort* is a
   translator's choice, on the page that has been calling them forts.
3. **`CP-5.4` says it in the child's last sentence**: *"the word 'fort' is not in
   the poem at all — somebody put it there in English."*

**What this does not do.** It does not close `RA-013`, it does not promote
"fort" past its failed audit, and it does not license the word in public copy —
none of this document is public copy, and step 14 drafting must run the audit
again on whatever wording it produces. Two things follow for the build:

- **The working title is provisional and is part of `D-057`.** *"The Hundred
  Stone Forts"* quotes the poem's own claim, which is defensible, and it also
  puts a failed gloss in the largest type on the page, which is the risk. A
  title built on the corpus's own word — *"A Hundred of Stone"*, or the
  transliterated `púr-` with the gloss beneath — is the alternative, and it is
  the owner's call.
- **Every screen heading that uses "fort" carries the `CP-3.6` link.** A child
  who wants to know why the museum keeps saying a word it says is wrong can get
  there from anywhere.

`§7`'s ten fields for `púr-` are not reproduced here. They are already given in
full in `pur-translation-standard.md` §§1–10, which is the audit this section
cites and does not restate.

---

## 2. Posture, mode, and the gate that blocks the build

Museum framework §1.7: **Field Mode is forbidden in the Reading Room posture.**

`01-INHERITED/curatorial-audit-v1.1/page-audit.csv` assigns `the-forts`
— *"The Dasa Forts: Indus Country, But Centuries Too Late"* — to **Reading
Room**, in both its assigned and recommended columns. That row is
`INHERITED-UNVERIFIED`.

Run §1.5's derivation over **this investigation's own claim set** rather than
over the essay's, strictly, on the wording the framework actually uses:

| §1.5 rule | Applies? |
|---|---|
| 1. Withheld access | No. Nothing here is `NOT ACCESSIBLE`. |
| 2. Repair state | No. |
| 3. **Absence dominance** — *"if the majority of the exhibit's **load-bearing propositions** resolve to **typed absences** rather than to positive claims"* | **No, on a strict reading.** §8 counts 42 statused propositions, of which 32 are positive `VERIFIED` measurements. And of the four screens that terminate in an unknown, only two rest on a **typed** absence (`PUR4J-012`'s `NOT PRODUCED`, and the geography absence at `PUR4J-018`). The other two are **not** typed absences and this document says so itself at §5.2: the ground gap is a `HOLD` on our retrieval, and `DE-M-027`'s missing date is untyped. |
| 4. Relation dominance | No. |
| 5. Place/material dominance | No — there is no Place to anchor to, which is the point. |
| 6. Counter-account | Partly: the investigation contradicts MelaKeela's own headline (`CP-3.1f`). Not dominant. |
| 7. **Otherwise → Reading Room**, flagged `derived_residual = true` | **This is what fires.** |

**An earlier draft of this section claimed rule 3 fired, by counting screens
instead of propositions and by reading "an absence or an unknown" where the
framework says "typed absences".** That claim was the only thing keeping this
specification alive, and it was the one conclusion §11 never tested — which is
the failure `BF-025`'s control exists to prevent: *"where a unit's conclusion
rescues its own deliverable, that conclusion is the one the adversarial pass
starts with."* It is corrected here rather than defended.

**What the corrected derivation actually says is: nothing.** Framework §1.6.1
is explicit that the rule-7 residual is not a posture finding —

> *"An exhibit does not become Reading Room by being unclassifiable. Derivation
> rule 7 (§1.5) makes Reading Room the residual **only for derivation**, and
> every residual assignment is flagged `derived_residual = true` … so the size
> of the unclassified set is visible rather than laundered into a posture
> count."*

— and §1.5 closes by stating that **derivation is advisory** and the assigned
posture is editorial, written to the Editorial Register with an override reason.

So there is no derived answer to hand the owner. There are two assignments and
an argument for each, and the specification does not choose:

- **Nocturnal Veḷi** — *not yet known*. Four of six FIND OUT screens terminate
  in an unknown; two of those unknowns are typed absences and two are holds; the
  investigation's own conclusion is that the museum cannot say. Field Mode is
  *available*, and the investigation may be built. Against it: on the framework's
  own counting rule the positive measurements are the majority, so this is an
  editorial override of a derivation that did not fire, and §1.5 requires the
  override reason to be written down.
- **Reading Room** — where the curatorial audit puts `the-forts`
  (`INHERITED-UNVERIFIED`). Field Mode is **forbidden** (§1.7) and the
  specification is **withdrawn**, not amended. Against it: §1.6.1 diagnoses
  exactly this assignment as the audit's residual bucket — *"34 pages are
  Reading Room because the audit had nothing more specific to say about them"* —
  and Reading Room is the secondary environment for all 96 pages, so the
  assignment carries little information.

**And a framework tension this unit surfaces rather than resolves.** §1.7
forbids Field Mode in Reading Room; §1.5 rule 7 makes Reading Room the
derivation residual; §1.6.1 says an exhibit does not become Reading Room by
being unclassifiable. Composed, a `derived_residual = true` assignment
**silently forbids Field Mode on any exhibit the derivation cannot classify** —
which is a prohibition falling out of an admitted encoding defect rather than
out of any judgement about the exhibit. Logged in
`04-AUDITS/INTERNAL-CONTRADICTIONS.csv`. It is not this specification's to
resolve and it does not excuse the specification: if the owner assigns Reading
Room, the specification is withdrawn whatever the tension.

A third possibility is recorded so it is not mistaken for a loophole: an exhibit
may be split, with the long-form argument staying Reading Room and the
investigation standing as its own exhibit with its own assignment. The
curatorial audit already recommends `Split` for `the-forts`. That is an argument
*for* one of `D-055`'s options; it is not a decision, and the split would have
to be real — a separate exhibit with its own posture row, not a Field Mode tab
bolted onto a Reading Room page.

Raised as **`D-055`**, blocking, with a section in `DECISIONS-NEEDED.md`.

A third possibility exists and is recorded so it is not mistaken for a
loophole: an exhibit may be split, with the long-form argument staying Reading
Room and the investigation standing as its own Nocturnal Veḷi exhibit over the
same claim set. The curatorial audit already recommends `Split` for
`the-forts`. That is an argument *for* one of `D-055`'s options; it is not a
decision, and the split would have to be a real one — a separate exhibit with
its own posture assignment, not a Field Mode tab bolted onto a Reading Room
page.

---

## 3. The five stages

Framework §10.4.3 fixes five stages. Backlog item 33
(`06-BACKLOG/EXPANSION-PROMPT-2026-09-07.md` L247, `INHERITED-UNVERIFIED`)
proposes a six-step flow: `DIG IT → WHAT DID YOU FIND? → COMPARE → PROVE IT →
FIELD BAG → WHAT DO YOU THINK?`. §10.4.3 governs; item 33's steps map onto it:

| §10.4.3 stage | Screens | Item 33 step | Note |
|---|---|---|---|
| 1. **Look** | `CP-1.1`, `CP-1.2` | `DIG IT` / `WHAT DID YOU FIND?` | There is no dig. The object is a line of text and the viewer is the primary-source viewer, not a trench. |
| 2. **Ask** | `CP-2.1` | — | The child sets the agenda. |
| 3. **Find out** | `CP-3.1` … `CP-3.6` | `COMPARE` | **`COMPARE` is cleared for this investigation only because its terms are words, numbers, materials and passages.** §6. |
| 4. **Decide** | `CP-4.1` | `WHAT DO YOU THINK?` | |
| 5. **Check** | `CP-5.1` … `CP-5.4` | `PROVE IT` | |
| *(throughout)* | | `FIELD BAG` | §4. A record at every stage, per §10.4.3. |

Fifteen screens. Every one is specified below with: **what is shown**, **what
the child does**, **what the child is asked to conclude**, **the badge and the
claims under it**, and **the Field Bag record**.

---

## 4. The Field Bag in this investigation

Framework §10.3. The bag is shared infrastructure, not a children's feature;
this investigation uses it as specified there and adds nothing.

**Local by default, and for this investigation local absolutely.** §10.4.5: no
account is required and none is offered to under-16 visitors. There is no
server-side bag on this surface at any age, because the surface cannot tell an
11-year-old from an adult and the rule is written for the child.

**What goes in, per stage:**

| Stage | Record | Kind |
|---|---|---|
| Look | the line, by identifier and revision (`mk:` id of `PUR-P-041`) | institutional object |
| Look | the child's observations | visitor-written, never mixed with institutional text in export (§10.3) |
| Ask | the question cards the child picked, mapped onto real `mk:qst:` nodes | institutional objects |
| Ask | the child's own written question, if any | visitor-written, local only |
| Find out | each evidence card the child opened, with its status | institutional objects, status preserved |
| Decide | the child's three statements | visitor-written |
| Check | the museum's three current positions, with status; the falsifiers | institutional objects |

**Everything keeps its status.** A card collected while badged **MAYBE**
displays as **MAYBE** in the bag, and tapping it still reaches
`HYPOTHESIS` and `PUR-028`. §10.3, first required behaviour.

**The bag shows changes.** This matters more here than on most surfaces,
because two of this investigation's cards are expected to move:

- If `HOLD-001` (*puraṃdhi-*) resolves toward inclusion, the corpus goes from
  106 tokens to 156 (`PUR-023`), and every count card in `CP-3.1` changes.
- If `HOLD-008` (ground evidence) is ever discharged, `CP-3.5`'s empty shelf
  stops being empty, and the child who re-opens their bag should see exactly
  that: *the museum has read something since you were here.*

That second one is the best argument in the framework for the bag existing at
all, and it is the reason this specification does not simply delete `CP-3.5`
for being empty.

---

## 5. Two absences, and why they may never be confused

The negative-evidence standard (constitution §6, `CLAUDE.md`) governs arguing
*from* absence. Two absences carry this investigation. They are different in
kind, they have opposite remedies, and both are badged **WE DON'T KNOW**,
which is exactly why each screen must say which one it is.

### 5.1 The poem does not say

*The poem states no place; 93 of 103 fort-passages state no material; 82 of 103
state no count.*

This is an absence **in the record**, and it is typed. `PUR4J-012`'s own note
types the material silence as **`NOT PRODUCED`**: a hymn celebrating the
breaking of a fort had no occasion to state what it was built of, and the
silence is not evidence that the poets did not know or that the forts were
insubstantial. The geography absence is stated at `PUR4J-018` (`VERIFIED`): the
pinned corpus carries no geographic content, and `rigveda-pur-fields.csv`
prints the reason on every one of its 103 rows.

Child-facing form: **"the poem doesn't say."**
Remedy: none available from the poem. More reading will not produce it.

### 5.2 We have not looked

*No archaeological source exists in `02-SOURCES/access-ledger.csv`.*

This is **not** a negative-evidence claim about the past and must never be typed
as one. None of the eight types applies: it is not `NOT EXCAVATED`, because
people have excavated; it is not `NOT PUBLISHED` or `NOT ACCESSIBLE`, because
nothing was requested and refused. It is a gap in **this institution's
retrieval**, and its correct home is a `HOLD` — written as
`05-HOLDS/HOLD-008-ground-evidence-for-the-pur-corpus.md`.

Child-facing form: **"we haven't looked yet."**
Remedy: go and read. Named as `U-1` in `VERIFYING-UNITS.csv`.

### 5.3 The rule this puts on the interface

Every **WE DON'T KNOW** in this investigation carries one of exactly two
second lines, and the interface may not render the badge without one:

> **WE DON'T KNOW** · *the poem doesn't say*
> **WE DON'T KNOW** · *we haven't looked yet*

A third form is forbidden: a bare **WE DON'T KNOW** with no second line reads
as a shrug, and a shrug is the consolation prize this investigation exists to
refuse. Constitution §6: *"Unknown" is residual, never a positive rival
explanation.* A child who leaves able to distinguish these two sentences has
learned the most transferable thing in the whole method.

---

## 6. `COMPARE`, and the constraint that nearly kills this investigation

Framework §10.4.7 is the hardest rule this specification meets, and this
subject is the exact material it was written about.

> *"COMPARE may not take people, remains, named individuals or populations as
> its terms anywhere in the children's mode, in any Living World, in any
> pilot."*

**The corpus supplies the buckets.** `PUR4J-030` (`VERIFIED`): 22 of 103
passages carry a patron-side name and 22 an opponent-side name. Those are two
labelled sets of named human beings, already computed, already in a CSV column,
in the exact shape a drag-into-buckets interface consumes. `rigveda-pur-fields.csv`
has `patron_candidates` and `opponent_candidates` columns. Building COMPARE over
this register without thinking would produce, in about an afternoon, precisely
the interface §10.4.7's first constraint forbids — and it would arrive wearing
the clothes of a debunking, which §10.4.7 says explicitly does not lift the
prohibition.

**It is worse than that, and the worse part is the reason to say it out loud.**
`06-BRIEFS/pur-translation-standard.md` §10 records that the opponent side is
sorted by Grassmann's category **Dämon** — a nineteenth-century German
theological label that decides, before any passage is read, that the holders of
the forts were not people. That finding is already logged in
`04-AUDITS/REAUDIT-QUEUE.csv`. A sorting interface built on that column would
not merely sort human beings; it would hand a child a Victorian lexicographer's
demonology and call it evidence.

### 6.1 What COMPARE is cleared to take here

Words, numbers, materials, grammatical forms, translators' renderings, and
passages. Nothing else. Specifically:

| Cleared | Screen |
|---|---|
| the four numbers the poem uses, against how often each appears | `CP-3.1` |
| the ten passages that state a material, against each other | `CP-3.2` |
| Griffith's column against Geldner's column, on one word | `CP-3.2` |
| the poem's own word against the English words translators reached for | `CP-3.6` |
| the five metrical periods, in the order Arnold put them | `CP-3.4` |

The user's constraint on this unit says it plainly and it is adopted verbatim
as a design rule: **forts and pottery may be compared; their builders may not
be sorted.**

### 6.2 What replaces the forbidden screen

A child *will* ask who lived in the forts. `CP-2.1` therefore offers the
question card — refusing to offer it would teach that the question is
improper, which is not true and is its own distortion. Selecting it opens
`CP-3.7`, a **read-only card with no interaction of any kind**: no buckets, no
matching, no drag, no quiz, no "which side?". §10.4.7's own instruction for
this case is followed exactly — *"the material is read, with its status and its
date, not operated."*

Its content is specified at `CP-3.7`. In short: the poem names people on both
sides; the museum is not going to ask the child to group them; and one reason
is that the dictionary the museum itself uses to sort those names calls one
side *demons*, a word chosen by a man in the 1870s before anybody read the
lines. That is told to the child as a true thing about how the record was made
— which §10.4.6 expressly permits — and it is never handed over as a task.

### 6.3 The metrical-periods case, cleared explicitly

`CP-3.4` lets a child put Arnold's five period names in order. That is a
sorting interaction, so it is checked rather than assumed: its terms are
**metrical periods of a text**, not people, remains, names or populations.
§10.4.7 binds the pattern to those terms and this is not one of them. Cleared.

Two conditions attach anyway, because the screen sits one step from a
chronology that has been used to sort people:

1. The five names — Archaic, Strophic, Normal, Cretic, Popular — are **Arnold's
   labels for rhythms**, and the screen says so in the same breath as it shows
   them. They are not names of peoples, places or periods of history.
2. No stratum may be captioned, coloured or grouped in a way that suggests a
   population, a migration or an arrival. R-02 covers it.

---

## 7. The screens

Notation used in every screen block:

- **Rests on** — every `claim_id` the screen depends on, with the **lowest
  status among them** in bold. Where that is not `VERIFIED`, the unit that would
  verify it is named. Full table: `SCREEN-CLAIM-DEPENDENCY.csv`.
- **Display text** — *quoted* means the words are already in a register row in
  this repository and may be shown as they stand. *Pulled at build* means the
  text must be read from the pinned source at build time and may not be typed
  from memory by anyone, including the person building the screen. The pinned
  clone is **not in this container** (`rv01-reconciliation.md` §6); expect to
  re-clone at `d3eb8af` before any build.
- Indicative child-facing wording is *italic and indented*. **It is not public
  copy** and has not been through step 14.

---

### STAGE 1 — LOOK

#### `CP-1.1` · One line

**Purpose.** The child meets a real object at full quality before anybody tells
them what it means. §10.4.3 stage 1: observations only, no interpretation asked
for yet.

**What is shown.** RV 4.30.20, one stanza of three pādas, in the primary-source
viewer, in four registers stacked and all four visible at once:

| Register | Source | Display text |
|---|---|---|
| Devanagari, accented | `SRC-084` Eichler | pulled at build |
| Saṃhitā, transliterated | `SRC-020` Aufrecht | **quoted** — `PUR-P-041`: `śatám aśmanmáyīnām purā́m índro vy āā̀syat / dívodāsāya dāśúṣe` |
| Padapāṭha, word by word | `SRC-021` | **quoted** — `PUR-P-041`: `śatam \| aśman-mayīnām \| purām \| indraḥ \| vi \| āsyat \| divaḥ-dāsāya \| dāśuṣe` |
| Where it is | `PUR-P-041` | Rigveda, book 4, hymn 30, stanza 20 |

No translation on this screen. Deliberate: the English arrives at `CP-1.2` as a
*choice somebody made*, not as what the line says.

**What the child does.** Taps any word in the Saṃhitā line. The padapāṭha row
below highlights the same word, separated out.

> *These are the same words twice. The top line is how it is sung — the words
> run into each other. The bottom line is how somebody, a very long time ago,
> pulled them apart so you could see where each one starts and stops. Tap a
> word and watch.*

**What the child is asked to conclude.** Nothing. The prompt is *"what do you
notice?"* and the answers are recorded, not marked.

**Badge.** **FOUND** — that this line exists, in these four editions, at this
address. `PUR-P-041`, `PUR-005`.

**Field Bag.** The line, by identifier and revision. The child's observations,
local only.

**Nocturnal Veḷi `Avoid` check.** No starfield, no mystical typography, no
"ancient secrets". The line is presented as a page in a book that people have
been arguing about for two hundred years.

---

#### `CP-1.2` · What the line says — and who says so

**Purpose.** The claim enters, and it enters already attributed.

**What is shown.**

1. **Word by word**, from the padapāṭha, each word tappable to its
   grammatical form and its dictionary gloss:

   | word | what it is | gloss source |
   |---|---|---|
   | `śatam` | a hundred | `SRC-026` Grassmann |
   | `aśman-mayīnām` | made of stone | `SRC-026`; `PUR4J-012` |
   | `purām` | of forts — *the word this whole investigation is about* | `SRC-026`, `PUR4J-021` |
   | `indraḥ` | Indra, a god | `SRC-070` addressee |
   | `vi … āsyat` | threw apart, overthrew | `SRC-026` |
   | `divaḥ-dāsāya dāśuṣe` | for Divodāsa, the one who gave offerings | `SRC-026` |

2. **Four translators, side by side**, on this one stanza: Griffith 1890
   (`SRC-073`), Geldner 1951 (`SRC-072`), Grassmann 1876–7 (`SRC-074`) and
   Elizarenkova 1989–99 (`SRC-075`). **All four** are what `PUR-P-041`
   `translations_present` actually records — `elizarenkova geldner grassmann
   griffith` — and dropping the Russian one to make a tidier screen would be the
   first small dishonesty of the investigation. **Pulled at build.** Two are in
   German and one in Russian; each is shown in its own language, and the English
   beneath is **labelled as the museum's own rough gloss, not as evidence and
   not as a translation** — it has no register row and never will.

   **And a caution that travels with the card, because the screen's own lesson
   depends on it.** These are not four independent witnesses.
   `02-SOURCES/dependency.csv` `DEP-021` records that Grassmann's translation
   and the Grassmann dictionary that fixed this corpus's membership are **one
   man's judgement expressed twice**, and states in terms that Grassmann *"must
   not be counted as an independent vote alongside the Grassmann gloss."*
   `DEP-023` records that Elizarenkova worked with Geldner in view. The word
   glosses in item 1 above come from Grassmann's dictionary, so on this screen
   Grassmann is already speaking before his translation column is reached.

> *Four grown-ups wrote this line out in their own language — two in German,
> one in English, one in Russian. They did not all pick the same words.*
>
> *One more thing, and it is the sort of thing museums usually leave out. Two of
> these four are not really separate people to ask. The dictionary we used to
> tell you what the words mean was written by one of the four translators, so he
> gets two goes. And another of them was working with a copy of the German one
> open beside him. So it is four columns, but it is not four opinions.*

**What the child does.** Reads. Optionally taps a translator's name to see when
they worked and in what language.

**What the child is asked to conclude.** *"What does the poem claim?"* Free
text, plus a scaffold the child may accept or edit:

> *The poem says: a god threw down a hundred forts made of stone, for a man
> called Divodāsa.*

**Badge.** **FOUND** — the poem states a hundred stone forts here. `PUR4J-002`
(the count), `PUR4J-012` (the material), both `VERIFIED`.

Immediately beneath, and on the same screen, a second badge the child cannot
miss:

> **FOUND** · *the poem says it*
> **WE DON'T KNOW** · *we haven't looked yet*
>
> *Those are two different things. The poem saying it is something we can check,
> and we have. Whether it happened is something we would have to go and look at
> the ground for, and nobody here has. Finding out how different those two are
> is the rest of this investigation.*

**Field Bag.** The claim, in the child's words, with the FOUND badge attached
to *"the poem says it"* and only to that.

**Rests on.** `PUR-P-041`, `PUR4J-002`, `PUR4J-012`, `PUR4J-021`, `PUR-005`.
Lowest status: **`VERIFIED`**.

---

### STAGE 2 — ASK

#### `CP-2.1` · Your questions

**Purpose.** §10.4.3 stage 2. The child decides what would have to be true to
check the claim, and their questions are mapped onto the museum's real question
nodes. This screen is the investigation's spine: every card it offers opens a
real screen built on real evidence, and no card is decorative.

**What is shown.** The claim from `CP-1.2`, then:

> *If you wanted to check this, what would you need to know?*

Six cards. The child picks any number, in any order, including all six or one.

| Card | Opens | Real question behind it |
|---|---|---|
| **How many were there really?** | `CP-3.1` | `rv01-reconciliation.md` §2 — 99 against 106, and what each counts |
| **What were they made of?** | `CP-3.2` | constitution §4J *material* |
| **Where were they?** | `CP-3.3` | §4J *proposed geography*; `PUR4J-018` |
| **When was this said?** | `CP-3.4` | §4J *chronological stratum*; `DE-M-027` |
| **Has anyone dug them up?** | `CP-3.5` | `HOLD-008` |
| **What is a "fort", anyway?** | `CP-3.6` | constitution §7 translation standard; §4J's prohibition |

And a seventh card, which behaves differently and is specified at `CP-3.7`:

| **Who lived in them?** | `CP-3.7` | read-only. §10.4.7. |

**Plus the child's own question.** A text field:

> *Is there something else you want to know? Write it here. It stays on this
> device. Nobody at the museum will read it.*

That is not a courtesy, it is §10.4.5: no free-text publication, no
transmission by default, and a child's writing never enters the correction
pipeline as a public artefact. Where a class wants to send the museum a
challenge, the teacher does it from the teacher's account, as the class's
(§9.4, §10.5).

**What the child does.** Picks cards. There is **no required order and no
required number** — R-05: no completion mechanic, no progress bar that shames,
no locked stages. The Field Bag shows which cards are still unopened as a
*record*, never as a score.

**What the child is asked to conclude.** Nothing yet.

**Badge.** None. This screen shows no evidence.

**Field Bag.** The cards picked, as `mk:qst:` nodes. The child's own question,
local only.

**Design note.** The **How many** card is listed first because it is the
question a child actually asks first, and because its screen is the one that
turns the whole investigation. It is not first because it is the most
important.

---

### STAGE 3 — FIND OUT

Six evidence screens plus one read-only card. Any order. Nothing locked.

---

#### `CP-3.1` · How many? — one word can carry a hundred forts

**Purpose.** To break, with evidence and in a child's hands, the assumption
that a text can be counted the way objects can. This is where "a poem is not a
photograph" first bites.

**What is shown, in five moves.**

**(a) The word in our own line.** `purām` at RV 4.30.20 is **one word**. It is
genitive plural and it is governed by `śatam`, "a hundred". One word, a hundred
forts.

> *Look at our line again. There is one fort-word in it. But it does not mean
> one fort. It means a hundred. In this language, one word can hold as many as
> it likes.*

Across the whole poem the commonest form of the fort-word is `púraḥ`,
accusative **plural** — 45 of the 83 simple tokens (`PUR4J-020`). Any one of
them can be one fort or a hundred.

**(b) The counter that will not resolve.** Two counters, side by side:

| times somebody says the fort-word | **106** |
| how many forts that is | **?** |

The **106** is real and tappable: 106 tokens of seven related words, in 104
pādas, 103 stanzas, 86 hymns (`PUR-005`, `VERIFIED`). The **?** never resolves,
and no interaction resolves it.

> *You could count how many times the word appears. Somebody did — it is a
> hundred and six. But you cannot add those up to count forts, because one of
> them might be a hundred forts and the next one might be the same hundred
> forts said again in a different song.*

**(c) Most of the lines give no number at all.** 21 of the 103 fort-passages
state a count. **82 do not** (`PUR4J-001`, `VERIFIED`). Shown as 103 marks,
21 filled.

**(d) The poem only ever uses four numbers.** `PUR4J-009`, `VERIFIED`: every
cardinal count of forts in the corpus is seven, ninety, ninety-nine or one
hundred. No passage states an irregular figure. A small bar, four bars only:

| one hundred | 9 passages |
| ninety-nine | 6 |
| seven | 4 |
| ninety | 2 |

`PUR4J-002`, `VERIFIED`, with all 21 locators available on tap.

> *Four numbers. Nothing else. Not twenty-three forts, not forty-one, not
> eight. If you counted real forts you would sometimes get an awkward number.*

**(e) And the same words count rivers.** `PUR4J-006`, `VERIFIED`. "Ninety-nine"
in this poem is never one numeral — it is two words, `nava` "nine" and
`navatí-` "ninety" (`PUR4J-004`, `VERIFIED`). At RV 10.104.8 those same two
words count **ninety-nine rivers**, in a stanza that also carries a fort-word
epithet. Griffith, Geldner and Grassmann all render ninety-nine there — with
`DEP-021`'s caution attached, since Grassmann's translation is not independent
of the Grassmann dictionary. Shown as the two lines side by side, with the
shared words highlighted in both.

> *Here are the same two words in another part of the same poem. This time they
> are not counting forts. They are counting rivers.*

**(e2) And ninety-nine is one short of a hundred, on purpose.** `PUR4J-008`,
`VERIFIED`: in two of the six ninety-nine passages the poem immediately adds an
ordinal, *"the hundredth"* — at RV 4.26.3 and RV 7.19.5 — applied to a dwelling
word rather than to the fort word. The ninety-nine and the hundredth are one
shape.

> *Twice, straight after the ninety-nine, the poem says "and the hundredth".
> Ninety-nine here is not really a count. It is "one short of a hundred".*

**(f) The museum was wrong, and here is the correction.** One of MelaKeela's own
pages is headlined *"Ninety-nine forts…"*. Ninety-nine is **not** the commonest
fort-count in the poem. One hundred is, by nine passages to six (`PUR4J-003`,
`VERIFIED`).

> **WE WERE WRONG**
> *One of our own pages says "ninety-nine forts". We counted, and ninety-nine
> is not the number the poem uses most. A hundred is. We are leaving our
> mistake here on purpose, so you can see that we make them.*

This card is required, not optional. Constitution §2 puts *"MelaKeela's own
pages"* on the list of things the record must stay capable of contradicting,
and a children's surface that quietly omits the museum's own error is teaching
the opposite of the method. `rv01-reconciliation.md` §2.6 and `PUR4J-I-02`
carry the reception argument; the child gets the correction, not the argument.

**What the child does.**

- Taps a number in the four-bar chart to see its passages listed by locator.
- Taps any of the 21 filled marks to see that passage.
- Compares the fort-line and the river-line at (e) — a COMPARE step whose terms
  are two numerals and two nouns. Cleared under §6.1.

**What the child is asked to conclude.**

> *Does the poem tell you how many forts there were?*

The offered answers, all badged, none scored:

- **No — it gives numbers, but the same four over and over.** ← the evidence
- **No — most of the lines give no number at all.** ← the evidence
- **We don't know.** · *the poem doesn't say*
- *(the child's own words)*

There is deliberately **no** offered answer of the form "yes, a hundred", and
no answer of the form "no, the forts were made up". The first is unsupported;
the second is `PUR4J-I-01`'s deflationary reading, which the register itself
holds at `PROVISIONAL` and warns is the convenient answer (`BF-014`).

**Balance card, required, shown last.** `PUR4J-026` (`PROVISIONAL`): all six
of the ninety-nine passages present a fort as a real thing in the story that
somebody holds and somebody breaks. The number behaving like a formula does not
make the passage a formula, and the register keeps the two as separate claims in
separate files for exactly this reason.

> *Careful. The numbers behaving oddly does not mean the lines are just
> decoration. In every one of the ninety-nine lines, somebody is holding
> something and somebody else is breaking it. We are saying you cannot count
> them. We are not saying nothing happened.*

**Badge.** Each measurement **FOUND**. The balance card **WE THINK**
(`PUR4J-026`, `PROVISIONAL`). The screen's conclusion:
**WE DON'T KNOW** · *the poem doesn't say*.

**Rests on.** `PUR-005`, `PUR4J-001`, `PUR4J-002`, `PUR4J-003`, `PUR4J-004`,
`PUR4J-006`, `PUR4J-009`, `PUR4J-020`, `PUR-P-041` (`VERIFIED`); `PUR4J-026`
(**`PROVISIONAL`**). Lowest status: **`PROVISIONAL`** — `PUR4J-026`, which is
why the balance card is badged **WE THINK** and the measurements around it stay
**FOUND**. Verifying unit: **`U-5`**.

**Field Bag.** The four-number chart; the 106/? pair; the river line; the
correction card.

---

#### `CP-3.2` · Made of what? — the only stone one

**Purpose.** To show that the most concrete-sounding detail in the poem is a
detail the poem almost never gives, and that where it does give one, two expert
translators disagree about what it means.

**What is shown, in three moves.**

**(a) Ten of a hundred and three.** `PUR4J-012`, `VERIFIED`: exactly three
words describe what a fort was made of. Metal (`āyasá-`) in 8 passages, stone
(`aśmanmáya-`) in 1, raw or unbaked (`āmá-`) in 1. Ten passages of 103 say
anything at all.

> *Our line is the only one in the whole poem that says stone.*

And the two odd ones out point opposite ways, which `PUR4J-014` (`PROVISIONAL`)
records as **two data points and not a pattern**, because with one passage on
each side no distribution follows: the stone fort at RV 4.30.20 is an enemy's
and it is thrown down; the unbaked one at RV 2.35.6 is a place nothing bad can
reach you. Shown to the child as two cards, side by side, with the museum's own
caution on them:

> *Two lines. One each. That is not enough to see a pattern in, and we are not
> going to pretend it is.*

The other 93 are shown as blanks, with the type on the card:

> **WE DON'T KNOW** · *the poem doesn't say*
> *A song about knocking a fort down had no reason to mention what it was built
> of. That does not mean the singers didn't know. It means they weren't
> writing it down for us.*

That gloss is `PUR4J-012`'s own note — the `NOT PRODUCED` typing (§5.1) — in a
child's words, and it is the one place in this investigation where the
negative-evidence standard is taught rather than merely obeyed.

**(b) COMPARE — the ten material passages.** Ten cards, laid out together, each
carrying: locator, the material word, and **what kind of thing the fort is in
that line** — an object in a story, a thing asked for, a thing somebody is told
to make, or a god or a river that *is* one. From `PUR4J-013` (`PROVISIONAL`)
and `pur-translation-standard.md` §5.

**The sorting axis is deliberately not "whose fort is it".** An earlier draft
described the cards as *"an enemy's"* against *"a god is asked to protect the
singer with them"*, and that axis is holder identity: the "enemy" values in
`rigveda-pur-fields.csv` come from its `opponent_candidates` column, which §6
of this document has just told the reader is produced by Grassmann's category
**Dämon** and against which `RA-012` is `OPEN`. §10.4.7 binds the *pattern*, and
*"the same interaction is the same interaction whatever is loaded into it"* —
so a child sorting objects by whose side their human holders are on is doing
the forbidden interaction with a thin object in front of it. The axis below is
**what the fort is in the sentence**, which is a property of the line, not of
anybody:

| locator | material | what the fort **is** in that line |
|---|---|---|
| RV 2.20.8 | metal | a thing in the story, and it is thrown down |
| RV 4.30.20 | **stone** | a thing in the story, and it is thrown down · *our line* |
| RV 1.58.8 | metal | a thing asked for — protection |
| RV 7.3.7 | metal | a thing asked for — protection |
| RV 7.15.14 | metal | a **god**, asked to *be* one |
| RV 7.95.1 | metal | a **river** — Sarasvatī *is* one |
| RV 4.27.1 | metal | a thing in a myth: a hundred of them shut a bird in |
| RV 8.100.8 | metal | a thing in a myth: the bird escapes one |
| RV 10.101.8 | metal | a thing to be **made** — an instruction to priests |
| RV 2.35.6 | raw, unbaked | a place nothing bad can reach you |

The child sorts these cards. **Terms: the material word, and what the fort is
in the sentence. No card carries a person, a side, or a holder.** Cleared under
§6.1 on that criterion and not on any other. The suggested groupings offered are
*"a thing in a story"* / *"a thing somebody asks for or makes"* / *"a god or a
river that is one"* — and the child may make their own.

> *Two of these are things that get knocked down in a story. Two of them are
> something a singer is asking a god for. One of them is a river. One is a god.
> One is an instruction to go and build some.*

**(c) Iron or bronze?** `PUR4J-023`, `VERIFIED`. The metal word is `āyasá-`.
**Three** columns, eight rows — the third is the one it would be convenient to
leave out, and `PUR4J-023`'s own locator field records it:

| | Griffith 1890 | Geldner 1951 | Grassmann 1876–7 |
|---|---|---|---|
| all eight passages | **iron**, 8 of 8 | **ehern** — of bronze or brass — 8 of 8 | **mixed**: *Erz* once, *Eisen* once, *ehern* five times, and at RV 7.3.7 he does not render the word at all |

> *Two of them are completely consistent and completely different from each
> other. One says iron every time. One says bronze every time.*
>
> *And the third one is not consistent at all. He says a different thing in
> different places, and in one line he just leaves the word out. We are showing
> you him too, because leaving him out would make our point look tidier than it
> is.*

Neither of the consistent two argues the point, and neither says why.

**Why this is on a children's screen at all**, stated in the spec because a
reviewer will ask: iron and bronze have different histories in this part of the
world, so which metal is meant bears on **when** the lines could have been
composed. `PUR4J-023`'s own note: *"a translator's single lexical habit can
therefore move a chronology."* The child does not need that sentence. The child
needs to see that a grown-up's choice of one English word can change what the
poem is evidence *for*. It is the same lesson as `CP-3.4`, arriving from a
different direction, and it is the constitution §7 case in its purest form.

**What the child does.** Reads (a). Sorts the ten cards in (b). Reads (c) and
taps either column to see all eight locators.

**What the child is asked to conclude.**

> *Does the poem tell you what the forts were made of?*

- **Almost never — ten lines out of a hundred and three.** ← the evidence
- **Ours is the only stone one.** ← the evidence
- **We don't know which metal the other eight were.** · *the poem doesn't say*

**Badge.** Counts **FOUND**. The sorting card in (b) **WE THINK** — its
groupings come from `PUR4J-013`, `PROVISIONAL`, a hand classification. The
metal question **WE DON'T KNOW** · *the poem doesn't say* — and, on tap, the
longer truth: nobody has settled it, and `U-4` is the unit that would try.

**Rests on.** `PUR4J-012` (`VERIFIED`), `PUR4J-013` (**`PROVISIONAL`**),
`PUR4J-014` (**`PROVISIONAL`**), `PUR4J-023` (`VERIFIED`), `PUR-P-041`. Lowest
status: **`PROVISIONAL`** — `PUR4J-013` and `PUR4J-014`. Verifying unit: **`U-5`**. Until then the (b) sorting card is
badged **WE THINK** and may not be badged **FOUND**, and `PUR4J-013`'s own
recorded alternative — that counting the two bird passages as hostile makes it
3 of 8 rather than 1 of 8 — is shown on the card's reverse, because the register
put it there rather than leaving it for a reviewer.

---

#### `CP-3.3` · Where? — the map that stays empty

**Purpose.** To establish that the poem gives no place, using the museum's own
unfilled column as the evidence, and to refuse the identification that this
material invites more than any other.

**What is shown, in four moves.**

**(a) The museum's own table, with the hole in it.** The child is shown a few
rows of `03-REGISTERS/rigveda-pur-fields.csv` — a real register, not a mock-up
— with its `proposed_geography` column visible. Every one of the 103 rows reads:

> `NOT FILLED — no source`

and every row prints its own reason. `PUR4J-018`, `VERIFIED`: constitution
§4J's proposed-geography field **cannot be filled from the pinned corpus, which
contains no geographic content of any kind.**

> *This is our own table. There is a column for "where". It is empty on every
> single line, and we wrote down why on every single line. We did not leave it
> empty because we forgot.*

**(b) The map that stays empty.** A map of nothing. The child may tap *"show me
where"* and the map does not move, does not zoom, and places no pin. The
caption:

> *We have nowhere to put a pin.*

A pin would be fabricated evidence (§10.4.4). An empty map is not: it is a true
statement about what we can locate, rendered.

**(c) The one word that might be a place.** `PUR4J-017` and `PUR4J-028`, both
`VERIFIED`. Of the 103 fort-passages, 7 carry a word for a mountain and 6 carry
`síndhu-` — the only word in the corpus that can name a river. And `síndhu-`
means either "a river" or "the Indus", and **Griffith and Geldner read it
differently across those six passages**.

> *There is one word in six of the lines that might be the name of a river. It
> might also just mean "a river". The two grown-ups who translated the whole
> poem do not agree, and neither of them can ask the person who wrote it.*

**(d) The thing we are not going to say.** Constitution §4J: *"Do not
automatically translate* pur *into a Mature Harappan city."* Version 12 line
1175 holds the identification of the forts with one archaeological culture.
Stated to the child, plainly, as a decision the museum made:

> *There is a story you may meet somewhere else, that these forts were the
> cities archaeologists dug up beside the Indus river. Our museum does not say
> that. Not because it is impossible — because nothing in the poem says where,
> and we would only be guessing and then pretending we weren't.*

The wording matters and is specified rather than left to copy review. The museum
holds **no source recording who has made that identification**, so the screen
must not attribute it to anyone, count anyone, or characterise a field. What the
museum does hold is its own two rules against making it: constitution §4J's
prohibition on translating *pur* into a Mature Harappan city, and the research
hold at Version 12 line 1175. **The screen states the museum's rule, not a claim
about scholarship.**

**What the child does.** Reads the register rows. Taps the empty map. Compares
the two readings of `síndhu-` — terms: one word, two renderings. Cleared under
§6.1.

**What the child is asked to conclude.**

> *Can you say where the forts were?*

- **No — the poem doesn't say.** ← the evidence
- **There is one word that might be a river's name, and the experts disagree.**
- **We don't know.** · *the poem doesn't say*

No offered answer names a region, a culture or a site. R-03.

**Badge.** **WE DON'T KNOW** · *the poem doesn't say*.

**Rests on.** `PUR4J-017`, `PUR4J-018`, `PUR4J-028` — all `VERIFIED`. Lowest
status: **`VERIFIED`**.

**Field Bag.** The empty column. The two readings of `síndhu-`. The refusal at
(d), which is an institutional statement and is stored as one.

---

#### `CP-3.4` · When? — the weakest link in the whole chain

**Purpose.** This is the screen the investigation exists for. Everything else
shows that the poem is not a photograph of a *thing*. This shows that it is not
a photograph of a *moment* — and, more importantly, that the museum's ability
to say when is thinner than anything else it has told the child.

**It is specified to expose that thinness rather than to survive it.** No
composition date is asserted anywhere on this screen or anywhere in this
investigation. What is shown is what the ordering rests on.

**What is shown, in seven moves, in this order.**

**(a) The museum can put the lines in an order.** Five names, in order:
**Archaic · Strophic · Normal · Cretic · Popular** (`PUR-011`, `VERIFIED`).

> *We can put the lines of this poem in an order — which ones sound older, which
> ones sound newer. Watch how.*

**(b) The order comes from counting rhythms.** Not from dates, not from
contents, not from anything anyone dug up. Arnold sorted the poem by the shape
of its metre.

**What the screen may and may not show here.** `PUR-P-041`'s
`arnold_metre_labels` value is `M M M` — a metre-**type code**, one per pāda.
The column's whole vocabulary across the register is `M, MO, MR, PE2, MG, P,
MT, MV, M5, MVR, MOR, M4`, and **no register row in this repository defines what
any of those codes mean.** Nothing here holds a syllable-level scansion of RV
4.30.20. So the screen **may not** display "how the long and short syllables
fall": generating that would be fabricated evidence under §10.4.4 and `R-07`, on
this investigation's centrepiece screen.

What it shows instead is the true and smaller thing: the three pādas of our
line each carry the same code, `M`, and the museum can tell the child that the
code is Arnold's label for a rhythm-shape without being able to show the shape.

> *Arnold listened to the beat. He gave every line a little code for what its
> beat was like. Ours is the code he wrote "M" for, three times, once per line.*
>
> *We would like to show you the long and short beats themselves. We cannot —
> we do not have them written down anywhere, only his codes.*

**Named as a gap, not passed over.** Two things would fix it and neither has
been done: the van Nooten–Holland metrically restored text (`SRC-078`) is in the
pinned clone and carries the restoration; and Arnold 1905 defines his own metre
vocabulary. Extracting either is `U-8`.

**(c) Our line's period.** RV 4.30.20 is **Strophic**, and the museum's record
says `stratum_certainty = certain` for it (`PUR-P-041`) — as against 14 of the
106 fort-tokens where Arnold's assignment rests on metrical variations alone
and is flagged lower-confidence (`PUR-011`, `rv01-reconciliation.md` §3).

> *Our line is in the group Arnold called "Strophic". For some other lines he
> was less sure, and we keep a mark on those. Ours does not have the mark.*

**(d) Where the order comes from: one book, one man, 1905.** The child is shown
**the actual page**. `SRC-026`: E. V. Arnold, *Vedic Metre in its Historical
Development*, Cambridge 1905, Appendix IV, §265 "Explanatory Notes", printed
page 269 — archive.org item `vedicmetreinitsh00arnouoft`, scan OBJECT 289. It
is retrievable, it is out of copyright, and it is where the five names are
defined. `PUR-011`, `VERIFIED`.

> *Here is the actual page. A man called Edward Vernon Arnold worked this out
> and printed it in 1905. Everything we just told you about which lines are
> older comes from this one book.*

**(e) Arnold said himself that he wasn't sure.** He called his own period names
*provisional* (Arnold 1905 §§60–61, recorded at `PUR-026`).

> *He said so himself, in the same book. He called his names for the periods
> "provisional" — which is a grown-up word for "this is my best go, don't build
> anything heavy on it".*

**(f) The museum tried to check it a second way, and the second way could not
tell.** Two instruments, both shown — and the wording here is load-bearing, so
it is specified exactly:

| instrument | what it says about the fort-words |
|---|---|
| Arnold's rhythms | a difference big enough to be worth reporting: the fort-words are commoner in the early-sounding lines and rarer in the late-sounding ones (`PUR-014`, `PUR-016`, `PUR-017`, `PUR-018`; χ² = 14.57 on 4 df at the hymn level, p = 0.0057) |
| the order of the books | **could not resolve a difference this size.** The point estimate leans the same way — 6.98 per 10,000 in books 2–7 against 6.07 in the rest — but on 106 tokens the test cannot separate that from nothing (`PUR-020`: χ² = 0.50 on 1 df, p = 0.48) |

**This is not "the two instruments disagree", and an earlier draft of this
screen said it was.** `04-AUDITS/REAUDIT-QUEUE.csv` `RA-002` is `OPEN` on
exactly that wording, raised by `BF-004`, whose control is binding:
*"any null result in this repository reports the point estimate and its
direction alongside the p-value, and states the power limitation, before it is
allowed to bear on a hypothesis."* `PUR-020` says the difference is *not
significant* — which is a failure to detect, not a detection of no difference.
Turning that into "no difference at all" would make a null into a positive
finding, which constitution §6 forbids in terms: *"unknown" is residual, never a
positive rival explanation.* The error also ran toward this screen's own
preferred story, which is what makes it worth naming rather than quietly fixing.

> *We tried to check it another way, by looking at which book of the poem each
> line is in. That way could not tell. It leans the same direction, but there
> are not enough fort-words in the poem for it to be sure of anything.*
>
> *So we did not get a second answer. We got a shrug. A shrug is not agreement,
> and we are not going to count it as one.*

**Badge on the second instrument: WE DON'T KNOW · *we haven't looked yet*** —
because the remedy is a bigger or better-powered instrument, not a fact about
the poem. It may not be badged **FOUND**.

And the entanglement, because leaving it out would make the two look more
independent than they are: `PUR-021` (`VERIFIED`) records that 61.3% of all
"Popular" material is in book 10, so the two instruments are partly counting the
same thing twice.

**(g) An order is not a date. The museum has no year for this poem.**
`DE-M-027`, `VERIFIED`, quoted with its elision marked:

> *"The attestation dates that would date the languages themselves — … the
> Rigvedic strata in absolute years — cannot be established from anything
> retrieved in this session."*

Two things follow, and they are different sizes:

- **Established**: no absolute date for the Rigvedic strata was obtainable from
  anything retrieved in the session that produced `DE-M-027`. That is the claim,
  and it is scoped to a session.
- **Asserted here, with its coverage stated**: no absolute date for the Rigveda
  appears anywhere in the working tree of this repository. The search was a
  full-text scan of every tracked file for date expressions and era markers, run
  on 2026-09-09 against `main` — **the working tree, not the full history**. On
  the negative-evidence standard that is `ABSENT DESPITE ADEQUATE SEARCH` for
  the tree and nothing at all for the history, and the coverage boundary is
  stated here because `RA-018` is `OPEN` on exactly this omission elsewhere.

This investigation asserts no composition date.

> **WE DON'T KNOW** · *we haven't looked yet*
>
> *We can say which lines sound older than other lines. We cannot say what year
> any of them was made. Not roughly, not "about". We do not have that, and we
> are not going to make one up to finish the sentence.*

**(h) The status the museum itself gives this.** Shown as a card, in the child's
badge and in the real word beneath it:

> *"Arnold's five periods are really older-and-newer."*
> **MAYBE** — `HYPOTHESIS` (`PUR-028`)
>
> *This is the thing everything else on this screen is standing on, and it is
> the least sure thing we have shown you all day. We have not checked it. Nobody
> here has checked it another way that worked.*

`04-AUDITS/ARCHIVE-AND-POWER-AUDIT.csv` `APA-E-006` states it for the adults:
*"whether the metrical layering tracks composition date at all is an assumption
inside the instrument, not a result from it."* The child gets the badge; the
badge reaches the row.

**What the child does.**

- Puts the five period names in order. Terms: metrical periods of a text.
  Cleared under §6.3, with its two conditions.
- Opens the 1905 page and looks at it.
- Drags our line onto a timeline — **and the timeline has no numbers on it.**
  It has five bands and no years, because the museum has no years. Attempting to
  place a year is not a failure state; there is simply nowhere to put one, and
  the screen says why.

**What the child is asked to conclude.** Two questions, deliberately separated:

> *Can you say which lines sound older than others?*
- **Maybe — one man worked it out in 1905 and nobody has checked it another way
  that agreed.** ← the evidence

> *Can you say what year the poem was made?*
- **No.** · *we haven't looked yet*

**Badge.** The screen's own badge is **MAYBE**, because the lowest status
beneath it is `HYPOTHESIS`. It may not be badged higher. §1.3, property 4.

**Rests on.** `PUR-011`, `PUR-012`, `PUR-013`, `PUR-014`, `PUR-015`, `PUR-016`,
`PUR-017`, `PUR-018`, `PUR-019`, `PUR-020`, `PUR-021` (all `VERIFIED`),
`PUR-P-041` (a passage row, no status column), `DE-M-027` (`VERIFIED`),
`APA-E-006` (an archive-and-power-audit row — `ARCHIVE-AND-POWER-AUDIT.csv` has
no status column, so it carries none and may not be cited as `VERIFIED`),
`PUR-026` (**`PROVISIONAL`**), `PUR-028` (**`HYPOTHESIS`**).
**Lowest status: `HYPOTHESIS` — `PUR-028`.**
Verifying units: **`U-2`** (a second, independent stratification instrument
would test `PUR-028` and could move `PUR-026`) and **`U-3`** (retrieve what any
absolute date for the Rigveda rests on, so that this screen can show the
argument rather than only its absence).

**Field Bag.** The five periods. The 1905 page. The two instruments and their
disagreement. The `MAYBE` card, which is the single most important object in
the bag and is stored with `PUR-028` attached.

**Design note — the one temptation to refuse.** It would be easy, and it would
feel generous, to give the child *some* date: "about three and a half thousand
years ago." Every popular account of this material does. This specification
does not, because the repository holds nothing that would support it, and
because a number offered to a child to spare them an unknown is exactly the
move the whole investigation is teaching them to catch. `U-3` is what would
change this, and until `U-3` runs, the timeline has no numbers on it.

---

#### `CP-3.5` · Has anyone dug? — the museum's own notebook

**Purpose.** The ground half of the investigation. It is empty, and the screen
makes the emptiness checkable rather than announcing it.

**The design problem, stated first.** A children's screen about archaeology
that has no archaeology has three possible shapes, and two are forbidden:

1. Show a photograph of an excavated wall and let the child infer a connection.
   **Forbidden** — §10.4.4, fabricated evidence, and R-03.
2. Delete the screen and never raise the question. **Forbidden in effect** —
   the child asked it at `CP-2.1`, and a museum that drops the question it was
   asked is teaching that unanswerable questions are improper.
3. Show what the museum has actually read, and let the child find the gap.

The third is what is specified.

**What is shown.** `02-SOURCES/access-ledger.csv` — the museum's real ledger,
98 rows at the time of writing (`SRC-001`–`SRC-098`, derived with `csv.DictReader`, not from the line count) — rendered as a shelf, grouped by kind:

| kind | roughly what is there |
|---|---|
| the poem itself | four editions, plus the ancient word-by-word analysis |
| dictionaries | Grassmann's, and word-lists |
| translations | six, in four languages |
| a book about rhythms | Arnold 1905 |
| word databases | several |
| websites that would not open | a number of them, each with the date we tried |
| **digging reports** | **nothing** |

The child taps **digging reports**. The shelf is empty. Not "loading", not
"coming soon" — empty, with the count zero and a date.

**The sentence the screen must carry, and the distinction it protects.**

> *Our museum has not read a single digging report. Not one.*
>
> **WE DON'T KNOW** · *we haven't looked yet*
>
> *So we cannot tell you what the ground shows. We also cannot tell you that
> nobody knows, because we have not been to look at what anybody else has
> written down. Those are two different kinds of not knowing and this is the
> second one: ours.*
>
> *That is why we are not going to show you a picture of a wall and tell you it
> is the one in the poem.*

This is §5.2 in the child's words, and getting it exactly right is the whole
point of the screen. **"We haven't looked" and "the poem doesn't say" are
different, and a child who leaves able to tell them apart has the transferable
part of the method.**

**What the child does.** Filters the shelf by kind. Taps any source to see what
it is, when it was retrieved, and — for the ones that would not open — the date
we tried and what the error was.

**What the child is asked to conclude.**

> *Has our museum looked at what came out of the ground?*

- **No. Not yet.** ← the evidence

And, offered separately, because it is the question the first one provokes:

> *Does that mean nobody knows?*

- **We can't tell you.** · *we haven't looked yet*

**The specification is deliberate here, and an earlier draft was not.** It
answered this second question **"No"** — which would have had the museum assert
to a child that somebody, somewhere, knows, on the strength of nothing. The
museum has no source for what the archaeological record contains. It has a
source for what it has itself read, which is the shelf the child just filtered.
Those are the only two things this screen may say, and the second question gets
the honest non-answer rather than the reassuring one.

**Badge.** **FOUND** — that our ledger contains no excavation source. That is a
checkable fact about our record, and the child just checked it. The ground
itself: **WE DON'T KNOW** · *we haven't looked yet*.

**Rests on.** `02-SOURCES/access-ledger.csv` as read on 2026-09-09;
`HOLD-008`. The repository has precedent for citing itself as a searched
source — `SRC-048`, `SRC-086`, `SRC-098`. Lowest status: **`VERIFIED`** for the
statement about our ledger; the ground question carries no claim at all, which
is why it is **WE DON'T KNOW** and not a claim badged low.
Verifying unit: **`U-1`**.

**A note for whoever builds this.** The shelf must read from the ledger at
build time, not from a copy. If `U-1` runs and an excavation report enters the
ledger, this screen must stop saying the shelf is empty **on the same day**, and
every Field Bag holding the old card must show the change (§10.3). A hard-coded
"nothing here" would become a lie the moment the museum did its homework.

---

#### `CP-3.6` · What is a "fort", anyway? — the word is ours, not the poem's

**Purpose.** Constitution §7's translation standard at a reading age, and §4E's
attestation gradient: the poem's word, a translator's English word, and a modern
guess are three different things.

**What is shown, in four moves.**

**(a) The poem's word.** `púr-`. Shown in Devanagari, transliterated, and with
its dictionary definition — Grassmann 1873, the standard nineteenth-century
Rigveda dictionary (`PUR4J-021`, `VERIFIED`):

> *"Wall aus Steinen und Lehm, Verschanzung, Palisade"*
> — a wall of stones and clay, an earthwork, a fence of stakes.

> *Not a city. Not a town. Not a castle. The oldest proper dictionary of this
> poem says: a wall, or a bank of earth, or a fence made of posts.*

**(b) What shape the word usually takes.** `PUR4J-020`, `VERIFIED`, stated
exactly as the register states it and no further: of the 83 simple fort-words,
**67.5% are accusative** — the grammatical shape a word takes when it is the
thing a verb is done *to* — and **3.6%, three of 83, are locative**, the shape
for being *in* something. Shown as 83 marks, coloured two ways.

> *Words in this language change shape depending on their job in the sentence.
> Nearly always, the fort-word is in the shape for "the thing something is done
> to". Three times out of eighty-three it is in the shape for "the place
> somebody is in".*

**What this screen may not say, and an earlier draft did.** It may not say the
forts are *"broken, thrown down, split"*. Accusative case says a verb acts on
the word; it does not say which verb. That reading is `PUR-027`, a
**`HYPOTHESIS`**, whose note records that testing it *"requires reading each of
the 106 passages for the grammatical role of pur-, which this unit did not do."*
Nor may it say that this is not how the words would fall for towns — that is
`PUR4J-I-03` `evidence_for` (1), **`PROVISIONAL`**, and it belongs on the
screen's conclusion card at its own badge, not in the caption of a `VERIFIED`
measurement. `PUR4J-020`'s own note is the discipline: *"a measurement of case
distribution, not an interpretation of it."*

The interpretation is still offered — on its own card, badged **WE THINK**:

> **WE THINK** *(`PUR4J-I-03`, `PROVISIONAL`)*
> *If you were describing towns where people lived, our museum thinks that is
> not how the word-shapes would fall. That is us reading the numbers, not the
> numbers themselves.*

**(c) Three that break any single picture.** Three cards, each a real passage:

| RV 8.1.28 | a fort that **moves** (`cariṣṇú-`) |
| RV 7.95.1 | a fort that **is a river** — Sarasvatī *is* one |
| RV 7.15.14 | a god asked **to be** one |

> *Whatever these are, they are not all the same kind of thing. One of them
> moves. One of them is a river.*

**(d) COMPARE — the words people have used.** Not a quiz. **Eight cards**, each
with the word, who used it, and *what it makes you picture*, drawn from
`pur-translation-standard.md` §9 and `PUR4J-022` (`VERIFIED`). The last two are
the non-English ones, and they are on the card because cutting them would leave
a screen about translation that had quietly translated only into English:

| English word | who | what it makes you picture | what breaks |
|---|---|---|---|
| **city** | Griffith, **once** in 103 passages | streets, houses, thousands of people | the poem says it is a wall of stones and clay; and if you say city, the next step to "so it was one of the dug-up Indus cities" happens almost by itself |
| **castle** | Griffith, 33 times | a stone keep with a lord in it | that is medieval Europe, not this |
| **fort / fortress** | Griffith, 67 times | something built to be defended | fine for the ones that get stormed; wrong for the river and the god |
| **stronghold** | Griffith, 5 times | a defended place, unspecified | the least committed |
| **wall / rampart / palisade** | Grassmann's own definition | an earth bank or a fence, maybe with nothing permanent inside | fits the unbaked one, and the moving one |
| **Burg** | both German translators, ~80 times each | a fortified seat — between fort and castle | neither German translator **ever** writes *Stadt*, "city". But see the caution below: these are not two independent votes |
| **forteresse / citadelle** | Renou, in French, across 58 of the 103 passages | a fortress, or a citadel — a stronghold inside a town | *citadelle* 22 times imports a town for the citadel to sit in |
| **крепость** | Elizarenkova, in Russian | a fortress | `DEP-023`: she worked with Geldner in view |

> *Every one of these is somebody's choice. The poem did not write any of them.
> When you read "ninety-nine castles" in English, the castles were put there by
> a man in 1890.*

**The counting caution, on the card and not in a footnote.** `DEP-021`: the
Grassmann dictionary that supplied the *"wall, rampart, palisade"* row and the
Grassmann translation that helped supply the *Burg* row are **one man's
judgement expressed twice**, and the dependency register says in terms that he
*"must not be counted as an independent vote alongside the Grassmann gloss that
defined the family."* `DEP-023`: Elizarenkova is not independent of Geldner.
Six columns; four judgements at most.

> *Careful with counting. Two of these are the same man twice — he wrote the
> dictionary and one of the translations. And one of them was working with
> another one open beside him. So do not count the columns and think that is how
> many people agreed.*

**And the counts themselves are indicative, not exact.** `PUR4J-022`'s locator
records that they were made by surface-string match and not lemmatised. The card
says so.

**What the child does.** Reads (a)–(c). Turns the cards in (d). **No answer is
scored and no word is marked correct** — R-05, and because there is no correct
one: the register's own finding (`PUR4J-I-03`, `PROVISIONAL`) is that no single
English word or archaeological referent can stand for this corpus.

**What the child is asked to conclude.**

> *Is the poem talking about one kind of thing?*

- **We think not.** ← the museum's position, `PROVISIONAL`
- **The English word was chosen by somebody.** ← the evidence
- **We don't know what most of them were.** · *the poem doesn't say*

**Badge.** (a), (b), (c) and the translator counts: **FOUND**. The conclusion
*"not one kind of thing"*: **WE THINK** — `PUR4J-I-03`, `PROVISIONAL`.

**Rests on**, one status per identifier: `PUR4J-015` (`VERIFIED`), `PUR4J-020`
(`VERIFIED`), `PUR4J-021` (`VERIFIED`), `PUR4J-022` (`VERIFIED`), `PUR4J-025`
(**`PROVISIONAL`**), `PUR4J-I-03` (**`PROVISIONAL`**). Lowest status:
**`PROVISIONAL`**. Verifying unit: **`U-5`**, and the register's own
falsifier — a lexicon independent of the Grassmann–Geldner line rendering
`púr-` as a settlement word would weaken this (`pur-translation-standard.md`
§11); the obvious candidates were unreachable at `SRC-080`–`SRC-083`, so this
is also **`U-6`**.

**Balance check, run and recorded.** This screen could tip into "so the forts
were never real", which is not what the evidence says and is the deflationary
answer `PUR4J-I-01` warns is convenient. `PUR4J-I-03`'s own
`evidence_against` field is therefore shown on the screen's last card, not
buried: **48 of 103 passages do present a fort as an object in the story**;
they have named holders, two of them state a material, one has a gate, and one
may have a name. The card reads:

> *Do not go too far the other way. In about half the lines, a fort is a real
> thing in the story that somebody holds and somebody else breaks. We are not
> saying the poem made all of them up. We are saying you cannot tell, from the
> poem alone, which ones stood anywhere.*

---

#### `CP-3.7` · Who lived in them? — read only, and here is why

**Purpose.** To answer, truthfully, the question a child will certainly ask,
**without building the interface §10.4.7 forbids.** §6.2 sets out the reasoning;
this is the screen.

**Interaction: none.** No buckets. No matching. No drag. No quiz. No "which
side?". No tap-to-sort. The card scrolls and that is all it does. This is not a
degraded version of a better screen; the absence of interaction *is* the
design, per §10.4.7: *"the material is read, with its status and its date, not
operated."*

**What is shown.**

> *The poem names people. Some are the people the songs are for. Some are the
> people the songs are against. You will see their names if you read the lines:
> Divodāsa, Śambara, Pipru, Śuṣṇa.*
>
> *We are not going to ask you to put them into groups.*
>
> *Here is why. To sort those names, we would have to use somebody's list of
> which name goes on which side. The list we have comes from a dictionary
> written in the 1870s, and that dictionary files one side under a word that
> means "demons". A man chose that word before anybody had read these lines
> carefully. If we handed you the list, you would be sorting people using his
> word, not the poem's.*
>
> *So: the poem names people, we can show you the names, and we are not going
> to give you a box to put them in.*

**Status shown with it**, as §10.4.7 requires — with its status and its date:

- That the register's opponent side is sorted by Grassmann's category *Dämon*:
  `pur-translation-standard.md` §10, logged in `04-AUDITS/REAUDIT-QUEUE.csv`.
  Badge: **FOUND** — this is a fact about the dictionary, dated 1873.
- That 22 of 103 passages carry a patron-side name and 22 an opponent-side
  name, **on Grassmann's classification of the name and not on a reading of any
  passage**: `PUR4J-030`, `VERIFIED`. Its own `roles_basis` field, printed on
  every row of `rigveda-pur-fields.csv`, says: *"A name can occur in a passage
  without holding or attacking anything in it."*
- Who held the forts: **WE DON'T KNOW** · ***we haven't looked yet*** — and, on
  tap, the museum's own note that this has been logged unbuilt as `PUR-027`, a
  `HYPOTHESIS`, precisely so that a word-frequency pattern is not mistaken for
  an answer.

  **The second line is the other one, and an earlier draft had it wrong.** It
  read *"the poem doesn't say"*, which closes the question in the museum's
  favour. The poem is not silent: `PUR4J-030` establishes that 22 of 103
  passages carry a patron-side name and 22 an opponent-side name, and `PUR-027`
  says in terms that testing what the fort-word is doing in each passage
  *"requires reading each of the 106 passages … which this unit did not do."*
  The remedy is a reading, not a shrug — so this is *"we haven't looked yet"*.
  Getting this the wrong way round on this screen, of all screens, would have
  been the specification failing its own §5.3 at the point where §5.3 matters
  most.

**What the child is asked to conclude.** Nothing. There is no prompt on this
card. A prompt would be an exercise, and an exercise is what is forbidden.

**Rests on.** `PUR4J-030` (`VERIFIED`), `PUR-022` (`VERIFIED`), `PUR-027`
(**`HYPOTHESIS`**), `pur-translation-standard.md` §10. Lowest status:
**`HYPOTHESIS`** — which is why the "who held them" line is badged **WE DON'T
KNOW** rather than **WE THINK**, and why no version of this card may state who
the fort-holders were.

**What this screen is not.** It is not a lesson about racism dressed as a
history screen, and it is not an accusation against a dead lexicographer. It is
a true statement about how the record the museum uses was assembled, which
§10.4.6 permits a child to be told, and a refusal to hand the child the
categories, which §10.4.7 requires.

---

### STAGE 4 — DECIDE

#### `CP-4.1` · What do you think?

**Purpose.** §10.4.3 stage 4: the child states what they think and what they
are unsure about; two or more real explanations are available; **"we don't
know" is offered and is never scored as a failure.**

This screen is where the user's requirement lands: *a child should end able to
say what the poem claims, what the ground shows, and where the two do not
meet.* It is built as exactly those three sentences.

**What is shown.** The child's own Field Bag, laid out as three unfinished
sentences. Each is completed by choosing from real options, editing them, or
writing from scratch. Nothing is required.

---

**Sentence one — what the poem claims.**

> *The poem says …*

Offered completions, each carrying the badge it earned upstream:

| completion | badge | from |
|---|---|---|
| a god threw down a hundred forts made of stone, for a man called Divodāsa | **FOUND** *(that the poem says it)* | `CP-1.2` |
| forts get broken, over and over, in a hundred and three different lines | **FOUND** | `CP-3.1` |
| the forts are hardly ever described — ten lines out of a hundred and three say what one was made of | **FOUND** | `CP-3.2` |
| a fort in this poem is not always a building. One is a river. One is a god. One moves. | **FOUND** | `CP-3.6` |

---

**Sentence two — what the ground shows.**

> *The ground shows …*

Offered completions — and this is the shortest list on the screen, which is the
point:

| completion | badge |
|---|---|
| **nothing to us yet — our museum has not read a single digging report** | **WE DON'T KNOW** · *we haven't looked yet* |
| I don't know | **WE DON'T KNOW** · *we haven't looked yet* |

**There is no third option**, and specifically there is no option of the form
*"the ground agrees"* or *"the ground disagrees"*, because the museum holds no
evidence that would support either. A child who wants to write one may write
it; the museum will not offer it. If they do write one, the screen does not
mark it wrong — it shows, beside it, the empty shelf from `CP-3.5`.

---

**Sentence three — where the two do not meet.**

> *You cannot put the poem on top of the ground because …*

Multi-select. Each option carries its evidence on tap:

| completion | badge | from |
|---|---|---|
| the poem does not say **where** | **FOUND** | `CP-3.3`, `PUR4J-018` |
| nobody here can say **when** the poem was made — only which lines sound older, and that comes from one book from 1905 | **MAYBE** | `CP-3.4`, `PUR-028`, `DE-M-027` |
| you cannot **count** the forts — one word can mean a hundred | **FOUND** | `CP-3.1`, `PUR4J-020` |
| the poem only ever uses four numbers, and two of them also count rivers | **FOUND** | `CP-3.1`, `PUR4J-006`, `PUR4J-009` |
| the English word "fort" was chosen by a translator, not by the poem | **FOUND** | `CP-3.6`, `PUR4J-021`, `PUR4J-022` |
| **nobody at this museum has looked at the ground yet** | **WE DON'T KNOW** · *we haven't looked yet* | `CP-3.5` |

**What the child does.** Completes as many of the three sentences as they want
to. Edits any completion. Writes their own. **Nothing is submitted.** There is
no send button. §10.4.5: no free-text publication, no transmission by default,
and a child's writing never enters the correction pipeline.

**What the child is asked to conclude.** Exactly the three sentences and
nothing further. There is no fourth sentence asking them to decide whether the
forts were real, because the museum cannot answer that and will not ask a child
to answer what it cannot.

**Badge.** None on the screen itself; every completion carries its own.

**How "we don't know" is handled.** It appears twice as a *first-class
completion*, in the same type at the same size as every other option, with the
same tappable evidence beneath it, and never with softening language. It is
never last in a list, never greyed, and never accompanied by encouragement. It
is an answer the museum itself is giving on the same screen, and the child can
see it is the museum's answer too.

**Rests on.** Everything upstream. Lowest status: **`HYPOTHESIS`** (`PUR-028`,
via sentence three's *when* option, which is badged **MAYBE** accordingly).

---

### STAGE 5 — CHECK

#### `CP-5.1` · What the museum thinks, and how sure it is

**Purpose.** §10.4.3 stage 5, part one: what the institution currently thinks,
with its status.

**What is shown.** Three cards. Not one — three, because the museum's positions
on this material do not agree with each other about how confident to be, and
flattening them would be the false-equivalence failure in reverse.

**Card 1.**
> *"A* púr *is not one kind of thing. No single English word fits them all."*
> **WE THINK** — `PROVISIONAL` (`PUR4J-I-03`)
>
> *Five different measurements point this way. But nearly half the lines still
> describe a fort as a real thing somebody holds and somebody breaks, and we
> have no evidence about whether any of those stood anywhere.*

**Card 2.**
> *"The numbers are the poem's favourite numbers, not a tally."*
> **WE THINK** — `PROVISIONAL`, and weakly held (`PUR4J-I-01`)
>
> *Two of our four tests came out this way. One did not, and it was the
> strongest one: one enemy's forts are counted at ninety-nine three times and at
> a hundred twice, which is what you would get if somebody were counting and
> rounding.*
>
> *We got this one wrong the first time and had to fix it. The record of the
> mistake is kept.*

The Śambara figure in that card is **`PUR4J-007`**, `PROVISIONAL`, and it is
named here because it is the most-corrected row in the register set — `BF-014`
was logged against its first version, which was false in three of five parts
with all three errors running toward this card's own conclusion. A children's
card carrying that figure untraceably would be the same failure at a smaller
size. It is in this screen's `Rests on` list and in `EVIDENCE-MANIFEST.csv`.

**The badge is `WE THINK`, not `MAYBE`, and an earlier draft had it wrong.**
`PUR4J-I-01` is `PROVISIONAL`, and §1.3's mapping sends `PROVISIONAL` to
**WE THINK** without exception. Downgrading it to **MAYBE** to signal "weakly
held" would break the one property that makes the badges trustworthy — that a
child tapping a badge always reaches the same status word (§1.3, property 2).
Weakness is expressed in the card's *text*, which is where it belongs, not by
mislabelling the status.

That last line is required. `PUR4J-I-01` rests partly on a claim that was false
in three of five parts, all three errors running toward its own conclusion, and
the failure is logged as `BF-014` — a preferred-counter-narrative failure. A
children's card that presented this reading as the museum's confident finding
would repeat the error the log exists to prevent.

**Card 3.**
> *"The fort-words are not a late addition to the poem."*
> **WE THINK** — `PROVISIONAL` (`PUR-026`) — *and only if the 1905 book is
> right, which is a* **MAYBE** *(`PUR-028`).*
>
> *This one is stacked on the wobbliest thing we showed you. We are keeping it
> at "we think" instead of "found" for exactly that reason.*

**Badge.** As shown per card. No card may display higher than the lowest claim
beneath it (§1.3, property 4) — which is why card 3 shows both badges rather
than the better one.

**Rests on.** `PUR4J-I-01`, `PUR4J-I-02`, `PUR4J-I-03`, `PUR-026` (all
**`PROVISIONAL`**), `PUR-028` (**`HYPOTHESIS`**). Lowest status:
**`HYPOTHESIS`**.

---

#### `CP-5.2` · Where you agreed, and where you differed

**Purpose.** §10.4.3 stage 5, part two: *"explicitly, where the child's
reasoning matched or differed. A difference is presented as interesting, not
wrong."*

**What is shown.** The child's three sentences from `CP-4.1`, beside the
museum's three cards from `CP-5.1`, aligned on what they are about rather than
scored against each other.

Where they match:
> *You and the museum said the same thing here.*

Where they differ:
> *You said something different from us here. That is worth keeping. Here is
> what we were looking at when we said ours — and if you think we are wrong,
> that is allowed. We have been wrong on this page before.*

Tapping through reaches the evidence on both sides.

**What is never shown.** No score. No count of matches. No "you got 4 of 6".
No badge awarded to the child. R-05, and §10.4.4's prohibition on competition
in full.

**Design note.** The correction card at `CP-3.1f` and card 2 at `CP-5.1` exist
partly so that this screen's offer — *if you think we are wrong, that is
allowed* — is not a pleasantry. The child has already watched the museum
correct itself twice. The invitation is credible because it has been
demonstrated.

---

#### `CP-5.3` · What would change our minds

**Purpose.** Constitution §5 step 12 — record falsifiers — at a reading age.
These are taken from the registers' own `falsifier` fields, not invented for
the screen.

**What is shown.** Four cards, each naming a real thing that could happen:

| If somebody found … | it would change … | from |
|---|---|---|
| **a line of the poem with an awkward number of forts** — twenty-three, or forty-one | our idea that the numbers are just the poem's favourite numbers | `PUR4J-I-01` falsifier |
| **somebody who has read the digging reports**, and a wall of stones somebody has put a date on | this whole page — we would finally have a ground to compare the poem to | `HOLD-008`, `U-1` |
| **a second way of telling which lines are older**, that agreed with the 1905 book | how sure we can be about *when* — right now our second way disagreed | `PUR-028`, `U-2` |
| **an argument that settles whether that metal word means iron or bronze** | *when* again — but only if a further thing is also shown, below | `PUR4J-023`, `U-4` |

**The fourth card carries a rider, and it is a rule of the method rather than a
detail.** "The two metals have different histories here, so settling the word
would move the date" is **two claims joined**, not one: a claim about the
metal-word, and a claim about when each metal was in use in this part of the
world. The museum holds the first (`PUR4J-023`, `VERIFIED`) and **holds nothing
at all for the second** — it survives only in `PUR4J-023`'s notes field, has no
claim row, no locator and no retrieval behind it. Under constitution §5 step 10
that join is a **bridge** between two evidence classes, textual and material,
and every bridge is a separate claim needing its own mechanism and its own
status.

So the card is specified to say the smaller true thing:

> *If somebody settled whether that word means iron or bronze, it might help
> with "when" — but only if somebody else has worked out when each of those
> metals was around here. We have not looked that up either. So this is a
> falsifier with a second half missing, and we are telling you which half.*

Badge: **WE DON'T KNOW** · *we haven't looked yet*. The missing half is `U-4`'s
second requirement.

> *These are not wishes. They are things that could actually turn up. When one
> of them does, we will change what this page says, and we will leave the old
> version where you can see it.*

**Badge.** None — these are conditions, not claims.

---

#### `CP-5.4` · The one thing to take away

**Purpose.** The investigation's answer to its own question, in the child's
hands rather than in the museum's voice.

**What is shown.** One card, and the child's own three sentences beneath it.

> **Why a poem is not a photograph**
>
> *A photograph shows what was in front of the camera, and it usually has a
> date on the back.*
>
> *This poem tells you what somebody said. It does not say where. Nobody here
> can tell you when. One of its words can mean a hundred forts. It uses the same
> four numbers over and over, and two of those words count rivers somewhere
> else. And the word "fort" is not in the poem at all — somebody put it there
> in English.*
>
> *So you cannot lay the poem on top of the ground. Not because the poem is
> lying. Because you would need a place and a date to lay it on, and nobody has
> given us either one yet.*
>
> *That is a real answer. It is not a way of saying we ran out of time.*

**Field Bag, on close.** The bag is offered for export (§10.3, §5.2): a dated,
revision-pinned set of everything collected, statuses intact, the child's own
writing kept separate from the museum's text. No account. No upload. It is a
file on the child's own device.

---

## 8. What the investigation rests on, screen by screen

Full detail in `SCREEN-CLAIM-DEPENDENCY.csv` and `EVIDENCE-MANIFEST.csv`. The
summary:

| Screen | Lowest status beneath it | Screen badge ceiling | Unit that would raise it |
|---|---|---|---|
| `CP-1.1` | `VERIFIED` | FOUND | — |
| `CP-1.2` | `VERIFIED` | FOUND | — |
| `CP-2.1` | *(no evidence shown)* | — | — |
| `CP-3.1` | **`PROVISIONAL`** (`PUR4J-026`, balance card only) | FOUND on the measurements; WE THINK on the balance card | `U-5` |
| `CP-3.2` | **`PROVISIONAL`** (`PUR4J-013`) | WE THINK | `U-5` |
| `CP-3.3` | `VERIFIED` | FOUND | — |
| `CP-3.4` | **`HYPOTHESIS`** (`PUR-028`) | MAYBE | `U-2`, `U-3` |
| `CP-3.5` | `VERIFIED` *(about our ledger)*; **no claim** about the ground | FOUND / WE DON'T KNOW | `U-1` |
| `CP-3.6` | **`PROVISIONAL`** (`PUR4J-I-03`, `PUR4J-025`) | WE THINK | `U-5`, `U-6` |
| `CP-3.7` | **`HYPOTHESIS`** (`PUR-027`) | WE DON'T KNOW | *none proposed — see below* |
| `CP-4.1` | **`HYPOTHESIS`** (`PUR-028`, via *when*) | MAYBE on that option only | `U-2`, `U-3` |
| `CP-5.1` | **`HYPOTHESIS`** (`PUR-028`) | MAYBE on card 3 | `U-2` |
| `CP-5.2` | *(reflects upstream)* | — | — |
| `CP-5.3` | *(conditions, not claims)* | — | — |
| `CP-5.4` | **`HYPOTHESIS`** (`PUR-028`) | as `CP-4.1` | `U-2`, `U-3` |

**`CP-3.7` is the one screen where no verifying unit is named, on purpose.**
`PUR-027` — that the *púr-* is a fortification the composers attack rather than
inhabit — could be tested by reading all 106 passages for the grammatical role
of the fort-word, and that unit is worth running for the adult record. It would
not change this screen, because the screen does not assert who held the forts
and would not assert it at any status. Naming a unit here would imply the card
is waiting to say something it is never going to say.

**The full list of identifiers this investigation uses.** Derived on 2026-09-09
by scanning the body of this document — not §8's own enumeration — and joining
against the register status columns, per the inheritance's standing rule that
counts are data-derived and never a running tally.

**46 identifiers are cited. 43 carry a status: 32 `VERIFIED`, 9 `PROVISIONAL`,
2 `HYPOTHESIS`.** The other three carry no status column at all — two passage
rows, which are addresses rather than claims (`PUR-P-041`, `PUR-P-101`), and one
archive-and-power-audit row (`APA-E-006`).

- `VERIFIED` (32): `PUR-005`, `PUR-011`, `PUR-012`, `PUR-013`, `PUR-014`,
  `PUR-015`, `PUR-016`, `PUR-017`, `PUR-018`, `PUR-019`, `PUR-020`, `PUR-021`,
  `PUR-022`, `PUR-023`, `PUR4J-001`, `PUR4J-002`, `PUR4J-003`, `PUR4J-004`,
  `PUR4J-006`, `PUR4J-008`, `PUR4J-009`, `PUR4J-012`, `PUR4J-015`, `PUR4J-017`,
  `PUR4J-018`, `PUR4J-020`, `PUR4J-021`, `PUR4J-022`, `PUR4J-023`, `PUR4J-028`,
  `PUR4J-030`, `DE-M-027`.
- `PROVISIONAL` (9): `PUR-026`, `PUR4J-007`, `PUR4J-013`, `PUR4J-014`,
  `PUR4J-025`, `PUR4J-026`, `PUR4J-I-01`, `PUR4J-I-02`, `PUR4J-I-03`.
- `HYPOTHESIS` (2): `PUR-028`, load-bearing at `CP-3.4` and the lowest status in
  the investigation; and `PUR-027`, which appears at `CP-3.6` and `CP-3.7`
  **only to mark what the museum has not established** — that the fort-word is
  something attacked rather than inhabited, and who held the forts.

*(An earlier draft stated 45 and 42, listed `PUR4J-008` and `PUR-P-101` in the
enumeration without using them in the body, and omitted `PUR4J-007`, which the
body did use. `PUR4J-008` is now a screen — `CP-3.1(e2)` — and `PUR4J-007` is
named on `CP-5.1` card 2. The counts above are derived rather than typed, which
is what the standing rule requires and what the earlier draft did not do.)*

**Nothing `INHERITED-UNVERIFIED` is shown to a child as evidence.** §1.3.

### 1.3 The four badges

The child-facing vocabulary is fixed by the inheritance:
**FOUND / WE THINK / MAYBE / WE DON'T KNOW**
(`01-INHERITED/chatgpt-project-handoff.md` L347;
`06-BACKLOG/EXPANSION-PROMPT-2026-09-07.md` L254 — both `INHERITED-UNVERIFIED`
as *text*, but they are a display vocabulary, not a claim about the past, so
their standing does not depend on retrieval).

The mapping is a **display** of status. It is `HYPOTHESIS`, like every design
proposition here, and it **never** substitutes for a status:

| Register status | Child badge | Rule |
|---|---|---|
| `VERIFIED` | **FOUND** | |
| `PROVISIONAL` | **WE THINK** | |
| `HYPOTHESIS` | **MAYBE** | |
| `HOLD`, or a typed absence, or no claim at all | **WE DON'T KNOW** | |
| `REJECTED` | **WE WERE WRONG** | Shown only where the museum is correcting itself. Never deleted — constitution's standing constraint. |
| `SUPERSEDED` | **WE CHANGED THIS** | Must point at what replaced it. |
| `INHERITED-UNVERIFIED` | *not shown as evidence at all* | A child cannot hold "somebody said this in an earlier conversation and nobody checked" apart from FOUND, whatever label is attached. Excluded rather than badged. |

**Three properties this mapping must have, and one it must not.**

1. **It is lossy and the loss is stated.** Seven statuses into four badges.
   Every screen that shows **WE DON'T KNOW** must say *which kind* of not-knowing
   it is (§5), because the two kinds in this investigation have opposite
   remedies.
2. **Every badge is tappable.** Source Mode is mandatory in every posture
   (§1.7). Tapping a badge shows the real status word, the `claim_id`, the
   source, the locator and the retrieval date. A child who wants the machinery
   gets the machinery.
3. **A badge is never awarded.** It is a property of the evidence, not of the
   child's answer. Nothing in this investigation scores, ranks or congratulates.
4. **It must not run backwards, and the level matters.** The rule is applied
   **per card**: a card may not show a badge higher than the lowest status among
   the claims *that card* rests on. A screen therefore legitimately carries
   **FOUND** cards and **WE THINK** cards side by side, which several do.
   Separately, a screen's **conclusion** — the thing the child is asked to
   conclude — may not be badged higher than the lowest status among the claims
   the conclusion rests on. `SCREEN-CLAIM-DEPENDENCY.csv` records the
   screen-level floor as a **ceiling on the conclusion**, not as a cap on every
   card, and `EVIDENCE-MANIFEST.csv` carries the per-card badge. Both are
   derived from the status columns, never chosen.
   *(An earlier draft stated this rule screen-wide and was, on its own wording,
   violated on five of fifteen screens. The rule above is what the screens
   actually specify; the wording was the defect, not the design.)*

### 1.4 Reading level

Target: a competent 9-year-old reading alone; an 8-year-old reading with an
adult. Short sentences. Numbers written as words up to ten. No word of
scholarly apparatus without a plain-language gloss in the same sentence.
Sanskrit forms are always shown *and* always transliterated, never replaced.

**One deliberate exception.** The words **poem**, **evidence**, **translation**,
**guess** and **check** are used precisely and repeatedly, because they are the
content. So are the four badges.

### 1.5 The word "fort", and why this document keeps using it

Constitution §7 lists **fort** among the ten inherited English categories that
must be audited before use. `06-BRIEFS/pur-translation-standard.md` §10 ran that
audit and records that **"fort" fails it as a default gloss**:

> *"It is serviceable for the Śambara–Divodāsa passages … It is actively
> misleading at RV 7.95.1 (a river), RV 7.15.14 (a god), RV 8.1.28 (a moving
> one), and RV 8.6.23 (a simile)."*

`04-AUDITS/REAUDIT-QUEUE.csv` **`RA-013`** is `OPEN` on every occurrence of the
word, in page copy and in register column names alike.
`04-AUDITS/BIAS-FAILURE-LOG.csv` **`BF-017`** logs a previous unit that applied
§7 rigorously to *caste* and skipped it on *fort*, and its control is binding
here:

> *"Before any word on the §7 list enters draft copy, cite the audit that
> governs it or state why the default is kept."*

**This document uses the word constantly** — in its working title, in every
screen heading, and in every indicative child-facing sentence. The reason is
stated rather than assumed:

1. **A children's surface cannot present an unglossed Sanskrit stem as its
   subject.** An eight-year-old needs a handle before they can be shown that the
   handle is wrong. There is no English word on §10's list that passes the audit
   — *stronghold* is the least committed and it is still a defended place — so
   the choice is between a failing word used visibly and a failing word used
   invisibly.
2. **`CP-3.6` is the audit, turned into a screen.** It is the only screen whose
   whole content is the §7 finding: Grassmann's earthwork definition, the case
   distribution, the three passages that break any single picture, and the seven
   English words with what each imports. The child is shown that *fort* is a
   translator's choice, on the page that has been calling them forts.
3. **`CP-5.4` says it in the child's last sentence**: *"the word 'fort' is not in
   the poem at all — somebody put it there in English."*

**What this does not do.** It does not close `RA-013`, it does not promote
"fort" past its failed audit, and it does not license the word in public copy —
none of this document is public copy, and step 14 drafting must run the audit
again on whatever wording it produces. Two things follow for the build:

- **The working title is provisional and is part of `D-057`.** *"The Hundred
  Stone Forts"* quotes the poem's own claim, which is defensible, and it also
  puts a failed gloss in the largest type on the page, which is the risk. A
  title built on the corpus's own word — *"A Hundred of Stone"*, or the
  transliterated `púr-` with the gloss beneath — is the alternative, and it is
  the owner's call.
- **Every screen heading that uses "fort" carries the `CP-3.6` link.** A child
  who wants to know why the museum keeps saying a word it says is wrong can get
  there from anywhere.

`§7`'s ten fields for `púr-` are not reproduced here. They are already given in
full in `pur-translation-standard.md` §§1–10, which is the audit this section
cites and does not restate.

---

## 2. Posture, mode, and the gate that blocks the build

Museum framework §1.7: **Field Mode is forbidden in the Reading Room posture.**

`01-INHERITED/curatorial-audit-v1.1/page-audit.csv` assigns `the-forts`
— *"The Dasa Forts: Indus Country, But Centuries Too Late"* — to **Reading
Room**, in both its assigned and recommended columns. That row is
`INHERITED-UNVERIFIED`.

Run §1.5's derivation over **this investigation's own claim set** rather than
over the essay's, strictly, on the wording the framework actually uses:

| §1.5 rule | Applies? |
|---|---|
| 1. Withheld access | No. Nothing here is `NOT ACCESSIBLE`. |
| 2. Repair state | No. |
| 3. **Absence dominance** — *"if the majority of the exhibit's **load-bearing propositions** resolve to **typed absences** rather than to positive claims"* | **No, on a strict reading.** §8 counts 42 statused propositions, of which 32 are positive `VERIFIED` measurements. And of the four screens that terminate in an unknown, only two rest on a **typed** absence (`PUR4J-012`'s `NOT PRODUCED`, and the geography absence at `PUR4J-018`). The other two are **not** typed absences and this document says so itself at §5.2: the ground gap is a `HOLD` on our retrieval, and `DE-M-027`'s missing date is untyped. |
| 4. Relation dominance | No. |
| 5. Place/material dominance | No — there is no Place to anchor to, which is the point. |
| 6. Counter-account | Partly: the investigation contradicts MelaKeela's own headline (`CP-3.1f`). Not dominant. |
| 7. **Otherwise → Reading Room**, flagged `derived_residual = true` | **This is what fires.** |

**An earlier draft of this section claimed rule 3 fired, by counting screens
instead of propositions and by reading "an absence or an unknown" where the
framework says "typed absences".** That claim was the only thing keeping this
specification alive, and it was the one conclusion §11 never tested — which is
the failure `BF-025`'s control exists to prevent: *"where a unit's conclusion
rescues its own deliverable, that conclusion is the one the adversarial pass
starts with."* It is corrected here rather than defended.

**What the corrected derivation actually says is: nothing.** Framework §1.6.1
is explicit that the rule-7 residual is not a posture finding —

> *"An exhibit does not become Reading Room by being unclassifiable. Derivation
> rule 7 (§1.5) makes Reading Room the residual **only for derivation**, and
> every residual assignment is flagged `derived_residual = true` … so the size
> of the unclassified set is visible rather than laundered into a posture
> count."*

— and §1.5 closes by stating that **derivation is advisory** and the assigned
posture is editorial, written to the Editorial Register with an override reason.

So there is no derived answer to hand the owner. There are two assignments and
an argument for each, and the specification does not choose:

- **Nocturnal Veḷi** — *not yet known*. Four of six FIND OUT screens terminate
  in an unknown; two of those unknowns are typed absences and two are holds; the
  investigation's own conclusion is that the museum cannot say. Field Mode is
  *available*, and the investigation may be built. Against it: on the framework's
  own counting rule the positive measurements are the majority, so this is an
  editorial override of a derivation that did not fire, and §1.5 requires the
  override reason to be written down.
- **Reading Room** — where the curatorial audit puts `the-forts`
  (`INHERITED-UNVERIFIED`). Field Mode is **forbidden** (§1.7) and the
  specification is **withdrawn**, not amended. Against it: §1.6.1 diagnoses
  exactly this assignment as the audit's residual bucket — *"34 pages are
  Reading Room because the audit had nothing more specific to say about them"* —
  and Reading Room is the secondary environment for all 96 pages, so the
  assignment carries little information.

**And a framework tension this unit surfaces rather than resolves.** §1.7
forbids Field Mode in Reading Room; §1.5 rule 7 makes Reading Room the
derivation residual; §1.6.1 says an exhibit does not become Reading Room by
being unclassifiable. Composed, a `derived_residual = true` assignment
**silently forbids Field Mode on any exhibit the derivation cannot classify** —
which is a prohibition falling out of an admitted encoding defect rather than
out of any judgement about the exhibit. Logged in
`04-AUDITS/INTERNAL-CONTRADICTIONS.csv`. It is not this specification's to
resolve and it does not excuse the specification: if the owner assigns Reading
Room, the specification is withdrawn whatever the tension.

A third possibility is recorded so it is not mistaken for a loophole: an exhibit
may be split, with the long-form argument staying Reading Room and the
investigation standing as its own exhibit with its own assignment. The
curatorial audit already recommends `Split` for `the-forts`. That is an argument
*for* one of `D-055`'s options; it is not a decision, and the split would have
to be real — a separate exhibit with its own posture row, not a Field Mode tab
bolted onto a Reading Room page.

Raised as **`D-055`**, blocking, with a section in `DECISIONS-NEEDED.md`.

A third possibility exists and is recorded so it is not mistaken for a
loophole: an exhibit may be split, with the long-form argument staying Reading
Room and the investigation standing as its own Nocturnal Veḷi exhibit over the
same claim set. The curatorial audit already recommends `Split` for
`the-forts`. That is an argument *for* one of `D-055`'s options; it is not a
decision, and the split would have to be a real one — a separate exhibit with
its own posture assignment, not a Field Mode tab bolted onto a Reading Room
page.

---

## 3. The five stages

Framework §10.4.3 fixes five stages. Backlog item 33
(`06-BACKLOG/EXPANSION-PROMPT-2026-09-07.md` L247, `INHERITED-UNVERIFIED`)
proposes a six-step flow: `DIG IT → WHAT DID YOU FIND? → COMPARE → PROVE IT →
FIELD BAG → WHAT DO YOU THINK?`. §10.4.3 governs; item 33's steps map onto it:

| §10.4.3 stage | Screens | Item 33 step | Note |
|---|---|---|---|
| 1. **Look** | `CP-1.1`, `CP-1.2` | `DIG IT` / `WHAT DID YOU FIND?` | There is no dig. The object is a line of text and the viewer is the primary-source viewer, not a trench. |
| 2. **Ask** | `CP-2.1` | — | The child sets the agenda. |
| 3. **Find out** | `CP-3.1` … `CP-3.6` | `COMPARE` | **`COMPARE` is cleared for this investigation only because its terms are words, numbers, materials and passages.** §6. |
| 4. **Decide** | `CP-4.1` | `WHAT DO YOU THINK?` | |
| 5. **Check** | `CP-5.1` … `CP-5.4` | `PROVE IT` | |
| *(throughout)* | | `FIELD BAG` | §4. A record at every stage, per §10.4.3. |

Fifteen screens. Every one is specified below with: **what is shown**, **what
the child does**, **what the child is asked to conclude**, **the badge and the
claims under it**, and **the Field Bag record**.

---

## 4. The Field Bag in this investigation

Framework §10.3. The bag is shared infrastructure, not a children's feature;
this investigation uses it as specified there and adds nothing.

**Local by default, and for this investigation local absolutely.** §10.4.5: no
account is required and none is offered to under-16 visitors. There is no
server-side bag on this surface at any age, because the surface cannot tell an
11-year-old from an adult and the rule is written for the child.

**What goes in, per stage:**

| Stage | Record | Kind |
|---|---|---|
| Look | the line, by identifier and revision (`mk:` id of `PUR-P-041`) | institutional object |
| Look | the child's observations | visitor-written, never mixed with institutional text in export (§10.3) |
| Ask | the question cards the child picked, mapped onto real `mk:qst:` nodes | institutional objects |
| Ask | the child's own written question, if any | visitor-written, local only |
| Find out | each evidence card the child opened, with its status | institutional objects, status preserved |
| Decide | the child's three statements | visitor-written |
| Check | the museum's three current positions, with status; the falsifiers | institutional objects |

**Everything keeps its status.** A card collected while badged **MAYBE**
displays as **MAYBE** in the bag, and tapping it still reaches
`HYPOTHESIS` and `PUR-028`. §10.3, first required behaviour.

**The bag shows changes.** This matters more here than on most surfaces,
because two of this investigation's cards are expected to move:

- If `HOLD-001` (*puraṃdhi-*) resolves toward inclusion, the corpus goes from
  106 tokens to 156 (`PUR-023`), and every count card in `CP-3.1` changes.
- If `HOLD-008` (ground evidence) is ever discharged, `CP-3.5`'s empty shelf
  stops being empty, and the child who re-opens their bag should see exactly
  that: *the museum has read something since you were here.*

That second one is the best argument in the framework for the bag existing at
all, and it is the reason this specification does not simply delete `CP-3.5`
for being empty.

---

## 5. Two absences, and why they may never be confused

The negative-evidence standard (constitution §6, `CLAUDE.md`) governs arguing
*from* absence. Two absences carry this investigation. They are different in
kind, they have opposite remedies, and both are badged **WE DON'T KNOW**,
which is exactly why each screen must say which one it is.

### 5.1 The poem does not say

*The poem states no place; 93 of 103 fort-passages state no material; 82 of 103
state no count.*

This is an absence **in the record**, and it is typed. `PUR4J-012`'s own note
types the material silence as **`NOT PRODUCED`**: a hymn celebrating the
breaking of a fort had no occasion to state what it was built of, and the
silence is not evidence that the poets did not know or that the forts were
insubstantial. The geography absence is stated at `PUR4J-018` (`VERIFIED`): the
pinned corpus carries no geographic content, and `rigveda-pur-fields.csv`
prints the reason on every one of its 103 rows.

Child-facing form: **"the poem doesn't say."**
Remedy: none available from the poem. More reading will not produce it.

### 5.2 We have not looked

*No archaeological source exists in `02-SOURCES/access-ledger.csv`.*

This is **not** a negative-evidence claim about the past and must never be typed
as one. None of the eight types applies: it is not `NOT EXCAVATED`, because
people have excavated; it is not `NOT PUBLISHED` or `NOT ACCESSIBLE`, because
nothing was requested and refused. It is a gap in **this institution's
retrieval**, and its correct home is a `HOLD` — written as
`05-HOLDS/HOLD-008-ground-evidence-for-the-pur-corpus.md`.

Child-facing form: **"we haven't looked yet."**
Remedy: go and read. Named as `U-1` in `VERIFYING-UNITS.csv`.

### 5.3 The rule this puts on the interface

Every **WE DON'T KNOW** in this investigation carries one of exactly two
second lines, and the interface may not render the badge without one:

> **WE DON'T KNOW** · *the poem doesn't say*
> **WE DON'T KNOW** · *we haven't looked yet*

A third form is forbidden: a bare **WE DON'T KNOW** with no second line reads
as a shrug, and a shrug is the consolation prize this investigation exists to
refuse. Constitution §6: *"Unknown" is residual, never a positive rival
explanation.* A child who leaves able to distinguish these two sentences has
learned the most transferable thing in the whole method.

---

## 6. `COMPARE`, and the constraint that nearly kills this investigation

Framework §10.4.7 is the hardest rule this specification meets, and this
subject is the exact material it was written about.

> *"COMPARE may not take people, remains, named individuals or populations as
> its terms anywhere in the children's mode, in any Living World, in any
> pilot."*

**The corpus supplies the buckets.** `PUR4J-030` (`VERIFIED`): 22 of 103
passages carry a patron-side name and 22 an opponent-side name. Those are two
labelled sets of named human beings, already computed, already in a CSV column,
in the exact shape a drag-into-buckets interface consumes. `rigveda-pur-fields.csv`
has `patron_candidates` and `opponent_candidates` columns. Building COMPARE over
this register without thinking would produce, in about an afternoon, precisely
the interface §10.4.7's first constraint forbids — and it would arrive wearing
the clothes of a debunking, which §10.4.7 says explicitly does not lift the
prohibition.

**It is worse than that, and the worse part is the reason to say it out loud.**
`06-BRIEFS/pur-translation-standard.md` §10 records that the opponent side is
sorted by Grassmann's category **Dämon** — a nineteenth-century German
theological label that decides, before any passage is read, that the holders of
the forts were not people. That finding is already logged in
`04-AUDITS/REAUDIT-QUEUE.csv`. A sorting interface built on that column would
not merely sort human beings; it would hand a child a Victorian lexicographer's
demonology and call it evidence.

### 6.1 What COMPARE is cleared to take here

Words, numbers, materials, grammatical forms, translators' renderings, and
passages. Nothing else. Specifically:

| Cleared | Screen |
|---|---|
| the four numbers the poem uses, against how often each appears | `CP-3.1` |
| the ten passages that state a material, against each other | `CP-3.2` |
| Griffith's column against Geldner's column, on one word | `CP-3.2` |
| the poem's own word against the English words translators reached for | `CP-3.6` |
| the five metrical periods, in the order Arnold put them | `CP-3.4` |

The user's constraint on this unit says it plainly and it is adopted verbatim
as a design rule: **forts and pottery may be compared; their builders may not
be sorted.**

### 6.2 What replaces the forbidden screen

A child *will* ask who lived in the forts. `CP-2.1` therefore offers the
question card — refusing to offer it would teach that the question is
improper, which is not true and is its own distortion. Selecting it opens
`CP-3.7`, a **read-only card with no interaction of any kind**: no buckets, no
matching, no drag, no quiz, no "which side?". §10.4.7's own instruction for
this case is followed exactly — *"the material is read, with its status and its
date, not operated."*

Its content is specified at `CP-3.7`. In short: the poem names people on both
sides; the museum is not going to ask the child to group them; and one reason
is that the dictionary the museum itself uses to sort those names calls one
side *demons*, a word chosen by a man in the 1870s before anybody read the
lines. That is told to the child as a true thing about how the record was made
— which §10.4.6 expressly permits — and it is never handed over as a task.

### 6.3 The metrical-periods case, cleared explicitly

`CP-3.4` lets a child put Arnold's five period names in order. That is a
sorting interaction, so it is checked rather than assumed: its terms are
**metrical periods of a text**, not people, remains, names or populations.
§10.4.7 binds the pattern to those terms and this is not one of them. Cleared.

Two conditions attach anyway, because the screen sits one step from a
chronology that has been used to sort people:

1. The five names — Archaic, Strophic, Normal, Cretic, Popular — are **Arnold's
   labels for rhythms**, and the screen says so in the same breath as it shows
   them. They are not names of peoples, places or periods of history.
2. No stratum may be captioned, coloured or grouped in a way that suggests a
   population, a migration or an arrival. R-02 covers it.

---

## 7. The screens

Notation used in every screen block:

- **Rests on** — every `claim_id` the screen depends on, with the **lowest
  status among them** in bold. Where that is not `VERIFIED`, the unit that would
  verify it is named. Full table: `SCREEN-CLAIM-DEPENDENCY.csv`.
- **Display text** — *quoted* means the words are already in a register row in
  this repository and may be shown as they stand. *Pulled at build* means the
  text must be read from the pinned source at build time and may not be typed
  from memory by anyone, including the person building the screen. The pinned
  clone is **not in this container** (`rv01-reconciliation.md` §6); expect to
  re-clone at `d3eb8af` before any build.
- Indicative child-facing wording is *italic and indented*. **It is not public
  copy** and has not been through step 14.

---

### STAGE 1 — LOOK

#### `CP-1.1` · One line

**Purpose.** The child meets a real object at full quality before anybody tells
them what it means. §10.4.3 stage 1: observations only, no interpretation asked
for yet.

**What is shown.** RV 4.30.20, one stanza of three pādas, in the primary-source
viewer, in four registers stacked and all four visible at once:

| Register | Source | Display text |
|---|---|---|
| Devanagari, accented | `SRC-084` Eichler | pulled at build |
| Saṃhitā, transliterated | `SRC-020` Aufrecht | **quoted** — `PUR-P-041`: `śatám aśmanmáyīnām purā́m índro vy āā̀syat / dívodāsāya dāśúṣe` |
| Padapāṭha, word by word | `SRC-021` | **quoted** — `PUR-P-041`: `śatam \| aśman-mayīnām \| purām \| indraḥ \| vi \| āsyat \| divaḥ-dāsāya \| dāśuṣe` |
| Where it is | `PUR-P-041` | Rigveda, book 4, hymn 30, stanza 20 |

No translation on this screen. Deliberate: the English arrives at `CP-1.2` as a
*choice somebody made*, not as what the line says.

**What the child does.** Taps any word in the Saṃhitā line. The padapāṭha row
below highlights the same word, separated out.

> *These are the same words twice. The top line is how it is sung — the words
> run into each other. The bottom line is how somebody, a very long time ago,
> pulled them apart so you could see where each one starts and stops. Tap a
> word and watch.*

**What the child is asked to conclude.** Nothing. The prompt is *"what do you
notice?"* and the answers are recorded, not marked.

**Badge.** **FOUND** — that this line exists, in these four editions, at this
address. `PUR-P-041`, `PUR-005`.

**Field Bag.** The line, by identifier and revision. The child's observations,
local only.

**Nocturnal Veḷi `Avoid` check.** No starfield, no mystical typography, no
"ancient secrets". The line is presented as a page in a book that people have
been arguing about for two hundred years.

---

#### `CP-1.2` · What the line says — and who says so

**Purpose.** The claim enters, and it enters already attributed.

**What is shown.**

1. **Word by word**, from the padapāṭha, each word tappable to its
   grammatical form and its dictionary gloss:

   | word | what it is | gloss source |
   |---|---|---|
   | `śatam` | a hundred | `SRC-026` Grassmann |
   | `aśman-mayīnām` | made of stone | `SRC-026`; `PUR4J-012` |
   | `purām` | of forts — *the word this whole investigation is about* | `SRC-026`, `PUR4J-021` |
   | `indraḥ` | Indra, a god | `SRC-070` addressee |
   | `vi … āsyat` | threw apart, overthrew | `SRC-026` |
   | `divaḥ-dāsāya dāśuṣe` | for Divodāsa, the one who gave offerings | `SRC-026` |

2. **Four translators, side by side**, on this one stanza: Griffith 1890
   (`SRC-073`), Geldner 1951 (`SRC-072`), Grassmann 1876–7 (`SRC-074`) and
   Elizarenkova 1989–99 (`SRC-075`). **All four** are what `PUR-P-041`
   `translations_present` actually records — `elizarenkova geldner grassmann
   griffith` — and dropping the Russian one to make a tidier screen would be the
   first small dishonesty of the investigation. **Pulled at build.** Two are in
   German and one in Russian; each is shown in its own language, and the English
   beneath is **labelled as the museum's own rough gloss, not as evidence and
   not as a translation** — it has no register row and never will.

   **And a caution that travels with the card, because the screen's own lesson
   depends on it.** These are not four independent witnesses.
   `02-SOURCES/dependency.csv` `DEP-021` records that Grassmann's translation
   and the Grassmann dictionary that fixed this corpus's membership are **one
   man's judgement expressed twice**, and states in terms that Grassmann *"must
   not be counted as an independent vote alongside the Grassmann gloss."*
   `DEP-023` records that Elizarenkova worked with Geldner in view. The word
   glosses in item 1 above come from Grassmann's dictionary, so on this screen
   Grassmann is already speaking before his translation column is reached.

> *Four grown-ups wrote this line out in their own language — two in German,
> one in English, one in Russian. They did not all pick the same words.*
>
> *One more thing, and it is the sort of thing museums usually leave out. Two of
> these four are not really separate people to ask. The dictionary we used to
> tell you what the words mean was written by one of the four translators, so he
> gets two goes. And another of them was working with a copy of the German one
> open beside him. So it is four columns, but it is not four opinions.*

**What the child does.** Reads. Optionally taps a translator's name to see when
they worked and in what language.

**What the child is asked to conclude.** *"What does the poem claim?"* Free
text, plus a scaffold the child may accept or edit:

> *The poem says: a god threw down a hundred forts made of stone, for a man
> called Divodāsa.*

**Badge.** **FOUND** — the poem states a hundred stone forts here. `PUR4J-002`
(the count), `PUR4J-012` (the material), both `VERIFIED`.

Immediately beneath, and on the same screen, a second badge the child cannot
miss:

> **FOUND** · *the poem says it*
> **WE DON'T KNOW** · *we haven't looked yet*
>
> *Those are two different things. The poem saying it is something we can check,
> and we have. Whether it happened is something we would have to go and look at
> the ground for, and nobody here has. Finding out how different those two are
> is the rest of this investigation.*

**Field Bag.** The claim, in the child's words, with the FOUND badge attached
to *"the poem says it"* and only to that.

**Rests on.** `PUR-P-041`, `PUR4J-002`, `PUR4J-012`, `PUR4J-021`, `PUR-005`.
Lowest status: **`VERIFIED`**.

---

### STAGE 2 — ASK

#### `CP-2.1` · Your questions

**Purpose.** §10.4.3 stage 2. The child decides what would have to be true to
check the claim, and their questions are mapped onto the museum's real question
nodes. This screen is the investigation's spine: every card it offers opens a
real screen built on real evidence, and no card is decorative.

**What is shown.** The claim from `CP-1.2`, then:

> *If you wanted to check this, what would you need to know?*

Six cards. The child picks any number, in any order, including all six or one.

| Card | Opens | Real question behind it |
|---|---|---|
| **How many were there really?** | `CP-3.1` | `rv01-reconciliation.md` §2 — 99 against 106, and what each counts |
| **What were they made of?** | `CP-3.2` | constitution §4J *material* |
| **Where were they?** | `CP-3.3` | §4J *proposed geography*; `PUR4J-018` |
| **When was this said?** | `CP-3.4` | §4J *chronological stratum*; `DE-M-027` |
| **Has anyone dug them up?** | `CP-3.5` | `HOLD-008` |
| **What is a "fort", anyway?** | `CP-3.6` | constitution §7 translation standard; §4J's prohibition |

And a seventh card, which behaves differently and is specified at `CP-3.7`:

| **Who lived in them?** | `CP-3.7` | read-only. §10.4.7. |

**Plus the child's own question.** A text field:

> *Is there something else you want to know? Write it here. It stays on this
> device. Nobody at the museum will read it.*

That is not a courtesy, it is §10.4.5: no free-text publication, no
transmission by default, and a child's writing never enters the correction
pipeline as a public artefact. Where a class wants to send the museum a
challenge, the teacher does it from the teacher's account, as the class's
(§9.4, §10.5).

**What the child does.** Picks cards. There is **no required order and no
required number** — R-05: no completion mechanic, no progress bar that shames,
no locked stages. The Field Bag shows which cards are still unopened as a
*record*, never as a score.

**What the child is asked to conclude.** Nothing yet.

**Badge.** None. This screen shows no evidence.

**Field Bag.** The cards picked, as `mk:qst:` nodes. The child's own question,
local only.

**Design note.** The **How many** card is listed first because it is the
question a child actually asks first, and because its screen is the one that
turns the whole investigation. It is not first because it is the most
important.

---

### STAGE 3 — FIND OUT

Six evidence screens plus one read-only card. Any order. Nothing locked.

---

#### `CP-3.1` · How many? — one word can carry a hundred forts

**Purpose.** To break, with evidence and in a child's hands, the assumption
that a text can be counted the way objects can. This is where "a poem is not a
photograph" first bites.

**What is shown, in five moves.**

**(a) The word in our own line.** `purām` at RV 4.30.20 is **one word**. It is
genitive plural and it is governed by `śatam`, "a hundred". One word, a hundred
forts.

> *Look at our line again. There is one fort-word in it. But it does not mean
> one fort. It means a hundred. In this language, one word can hold as many as
> it likes.*

Across the whole poem the commonest form of the fort-word is `púraḥ`,
accusative **plural** — 45 of the 83 simple tokens (`PUR4J-020`). Any one of
them can be one fort or a hundred.

**(b) The counter that will not resolve.** Two counters, side by side:

| times somebody says the fort-word | **106** |
| how many forts that is | **?** |

The **106** is real and tappable: 106 tokens of seven related words, in 104
pādas, 103 stanzas, 86 hymns (`PUR-005`, `VERIFIED`). The **?** never resolves,
and no interaction resolves it.

> *You could count how many times the word appears. Somebody did — it is a
> hundred and six. But you cannot add those up to count forts, because one of
> them might be a hundred forts and the next one might be the same hundred
> forts said again in a different song.*

**(c) Most of the lines give no number at all.** 21 of the 103 fort-passages
state a count. **82 do not** (`PUR4J-001`, `VERIFIED`). Shown as 103 marks,
21 filled.

**(d) The poem only ever uses four numbers.** `PUR4J-009`, `VERIFIED`: every
cardinal count of forts in the corpus is seven, ninety, ninety-nine or one
hundred. No passage states an irregular figure. A small bar, four bars only:

| one hundred | 9 passages |
| ninety-nine | 6 |
| seven | 4 |
| ninety | 2 |

`PUR4J-002`, `VERIFIED`, with all 21 locators available on tap.

> *Four numbers. Nothing else. Not twenty-three forts, not forty-one, not
> eight. If you counted real forts you would sometimes get an awkward number.*

**(e) And the same words count rivers.** `PUR4J-006`, `VERIFIED`. "Ninety-nine"
in this poem is never one numeral — it is two words, `nava` "nine" and
`navatí-` "ninety" (`PUR4J-004`, `VERIFIED`). At RV 10.104.8 those same two
words count **ninety-nine rivers**, in a stanza that also carries a fort-word
epithet. Griffith, Geldner and Grassmann all render ninety-nine there — with
`DEP-021`'s caution attached, since Grassmann's translation is not independent
of the Grassmann dictionary. Shown as the two lines side by side, with the
shared words highlighted in both.

> *Here are the same two words in another part of the same poem. This time they
> are not counting forts. They are counting rivers.*

**(e2) And ninety-nine is one short of a hundred, on purpose.** `PUR4J-008`,
`VERIFIED`: in two of the six ninety-nine passages the poem immediately adds an
ordinal, *"the hundredth"* — at RV 4.26.3 and RV 7.19.5 — applied to a dwelling
word rather than to the fort word. The ninety-nine and the hundredth are one
shape.

> *Twice, straight after the ninety-nine, the poem says "and the hundredth".
> Ninety-nine here is not really a count. It is "one short of a hundred".*

**(f) The museum was wrong, and here is the correction.** One of MelaKeela's own
pages is headlined *"Ninety-nine forts…"*. Ninety-nine is **not** the commonest
fort-count in the poem. One hundred is, by nine passages to six (`PUR4J-003`,
`VERIFIED`).

> **WE WERE WRONG**
> *One of our own pages says "ninety-nine forts". We counted, and ninety-nine
> is not the number the poem uses most. A hundred is. We are leaving our
> mistake here on purpose, so you can see that we make them.*

This card is required, not optional. Constitution §2 puts *"MelaKeela's own
pages"* on the list of things the record must stay capable of contradicting,
and a children's surface that quietly omits the museum's own error is teaching
the opposite of the method. `rv01-reconciliation.md` §2.6 and `PUR4J-I-02`
carry the reception argument; the child gets the correction, not the argument.

**What the child does.**

- Taps a number in the four-bar chart to see its passages listed by locator.
- Taps any of the 21 filled marks to see that passage.
- Compares the fort-line and the river-line at (e) — a COMPARE step whose terms
  are two numerals and two nouns. Cleared under §6.1.

**What the child is asked to conclude.**

> *Does the poem tell you how many forts there were?*

The offered answers, all badged, none scored:

- **No — it gives numbers, but the same four over and over.** ← the evidence
- **No — most of the lines give no number at all.** ← the evidence
- **We don't know.** · *the poem doesn't say*
- *(the child's own words)*

There is deliberately **no** offered answer of the form "yes, a hundred", and
no answer of the form "no, the forts were made up". The first is unsupported;
the second is `PUR4J-I-01`'s deflationary reading, which the register itself
holds at `PROVISIONAL` and warns is the convenient answer (`BF-014`).

**Balance card, required, shown last.** `PUR4J-026` (`PROVISIONAL`): all six
of the ninety-nine passages present a fort as a real thing in the story that
somebody holds and somebody breaks. The number behaving like a formula does not
make the passage a formula, and the register keeps the two as separate claims in
separate files for exactly this reason.

> *Careful. The numbers behaving oddly does not mean the lines are just
> decoration. In every one of the ninety-nine lines, somebody is holding
> something and somebody else is breaking it. We are saying you cannot count
> them. We are not saying nothing happened.*

**Badge.** Each measurement **FOUND**. The balance card **WE THINK**
(`PUR4J-026`, `PROVISIONAL`). The screen's conclusion:
**WE DON'T KNOW** · *the poem doesn't say*.

**Rests on.** `PUR-005`, `PUR4J-001`, `PUR4J-002`, `PUR4J-003`, `PUR4J-004`,
`PUR4J-006`, `PUR4J-009`, `PUR4J-020`, `PUR-P-041` (`VERIFIED`); `PUR4J-026`
(**`PROVISIONAL`**). Lowest status: **`PROVISIONAL`** — `PUR4J-026`, which is
why the balance card is badged **WE THINK** and the measurements around it stay
**FOUND**. Verifying unit: **`U-5`**.

**Field Bag.** The four-number chart; the 106/? pair; the river line; the
correction card.

---

#### `CP-3.2` · Made of what? — the only stone one

**Purpose.** To show that the most concrete-sounding detail in the poem is a
detail the poem almost never gives, and that where it does give one, two expert
translators disagree about what it means.

**What is shown, in three moves.**

**(a) Ten of a hundred and three.** `PUR4J-012`, `VERIFIED`: exactly three
words describe what a fort was made of. Metal (`āyasá-`) in 8 passages, stone
(`aśmanmáya-`) in 1, raw or unbaked (`āmá-`) in 1. Ten passages of 103 say
anything at all.

> *Our line is the only one in the whole poem that says stone.*

And the two odd ones out point opposite ways, which `PUR4J-014` (`PROVISIONAL`)
records as **two data points and not a pattern**, because with one passage on
each side no distribution follows: the stone fort at RV 4.30.20 is an enemy's
and it is thrown down; the unbaked one at RV 2.35.6 is a place nothing bad can
reach you. Shown to the child as two cards, side by side, with the museum's own
caution on them:

> *Two lines. One each. That is not enough to see a pattern in, and we are not
> going to pretend it is.*

The other 93 are shown as blanks, with the type on the card:

> **WE DON'T KNOW** · *the poem doesn't say*
> *A song about knocking a fort down had no reason to mention what it was built
> of. That does not mean the singers didn't know. It means they weren't
> writing it down for us.*

That gloss is `PUR4J-012`'s own note — the `NOT PRODUCED` typing (§5.1) — in a
child's words, and it is the one place in this investigation where the
negative-evidence standard is taught rather than merely obeyed.

**(b) COMPARE — the ten material passages.** Ten cards, laid out together, each
carrying: locator, the material word, and **what kind of thing the fort is in
that line** — an object in a story, a thing asked for, a thing somebody is told
to make, or a god or a river that *is* one. From `PUR4J-013` (`PROVISIONAL`)
and `pur-translation-standard.md` §5.

**The sorting axis is deliberately not "whose fort is it".** An earlier draft
described the cards as *"an enemy's"* against *"a god is asked to protect the
singer with them"*, and that axis is holder identity: the "enemy" values in
`rigveda-pur-fields.csv` come from its `opponent_candidates` column, which §6
of this document has just told the reader is produced by Grassmann's category
**Dämon** and against which `RA-012` is `OPEN`. §10.4.7 binds the *pattern*, and
*"the same interaction is the same interaction whatever is loaded into it"* —
so a child sorting objects by whose side their human holders are on is doing
the forbidden interaction with a thin object in front of it. The axis below is
**what the fort is in the sentence**, which is a property of the line, not of
anybody:

| locator | material | what the fort **is** in that line |
|---|---|---|
| RV 2.20.8 | metal | a thing in the story, and it is thrown down |
| RV 4.30.20 | **stone** | a thing in the story, and it is thrown down · *our line* |
| RV 1.58.8 | metal | a thing asked for — protection |
| RV 7.3.7 | metal | a thing asked for — protection |
| RV 7.15.14 | metal | a **god**, asked to *be* one |
| RV 7.95.1 | metal | a **river** — Sarasvatī *is* one |
| RV 4.27.1 | metal | a thing in a myth: a hundred of them shut a bird in |
| RV 8.100.8 | metal | a thing in a myth: the bird escapes one |
| RV 10.101.8 | metal | a thing to be **made** — an instruction to priests |
| RV 2.35.6 | raw, unbaked | a place nothing bad can reach you |

The child sorts these cards. **Terms: the material word, and what the fort is
in the sentence. No card carries a person, a side, or a holder.** Cleared under
§6.1 on that criterion and not on any other. The suggested groupings offered are
*"a thing in a story"* / *"a thing somebody asks for or makes"* / *"a god or a
river that is one"* — and the child may make their own.

> *Two of these are things that get knocked down in a story. Two of them are
> something a singer is asking a god for. One of them is a river. One is a god.
> One is an instruction to go and build some.*

**(c) Iron or bronze?** `PUR4J-023`, `VERIFIED`. The metal word is `āyasá-`.
**Three** columns, eight rows — the third is the one it would be convenient to
leave out, and `PUR4J-023`'s own locator field records it:

| | Griffith 1890 | Geldner 1951 | Grassmann 1876–7 |
|---|---|---|---|
| all eight passages | **iron**, 8 of 8 | **ehern** — of bronze or brass — 8 of 8 | **mixed**: *Erz* once, *Eisen* once, *ehern* five times, and at RV 7.3.7 he does not render the word at all |

> *Two of them are completely consistent and completely different from each
> other. One says iron every time. One says bronze every time.*
>
> *And the third one is not consistent at all. He says a different thing in
> different places, and in one line he just leaves the word out. We are showing
> you him too, because leaving him out would make our point look tidier than it
> is.*

Neither of the consistent two argues the point, and neither says why.

**Why this is on a children's screen at all**, stated in the spec because a
reviewer will ask: iron and bronze have different histories in this part of the
world, so which metal is meant bears on **when** the lines could have been
composed. `PUR4J-023`'s own note: *"a translator's single lexical habit can
therefore move a chronology."* The child does not need that sentence. The child
needs to see that a grown-up's choice of one English word can change what the
poem is evidence *for*. It is the same lesson as `CP-3.4`, arriving from a
different direction, and it is the constitution §7 case in its purest form.

**What the child does.** Reads (a). Sorts the ten cards in (b). Reads (c) and
taps either column to see all eight locators.

**What the child is asked to conclude.**

> *Does the poem tell you what the forts were made of?*

- **Almost never — ten lines out of a hundred and three.** ← the evidence
- **Ours is the only stone one.** ← the evidence
- **We don't know which metal the other eight were.** · *the poem doesn't say*

**Badge.** Counts **FOUND**. The sorting card in (b) **WE THINK** — its
groupings come from `PUR4J-013`, `PROVISIONAL`, a hand classification. The
metal question **WE DON'T KNOW** · *the poem doesn't say* — and, on tap, the
longer truth: nobody has settled it, and `U-4` is the unit that would try.

**Rests on.** `PUR4J-012` (`VERIFIED`), `PUR4J-013` (**`PROVISIONAL`**),
`PUR4J-014` (**`PROVISIONAL`**), `PUR4J-023` (`VERIFIED`), `PUR-P-041`. Lowest
status: **`PROVISIONAL`** — `PUR4J-013` and `PUR4J-014`. Verifying unit: **`U-5`**. Until then the (b) sorting card is
badged **WE THINK** and may not be badged **FOUND**, and `PUR4J-013`'s own
recorded alternative — that counting the two bird passages as hostile makes it
3 of 8 rather than 1 of 8 — is shown on the card's reverse, because the register
put it there rather than leaving it for a reviewer.

---

#### `CP-3.3` · Where? — the map that stays empty

**Purpose.** To establish that the poem gives no place, using the museum's own
unfilled column as the evidence, and to refuse the identification that this
material invites more than any other.

**What is shown, in four moves.**

**(a) The museum's own table, with the hole in it.** The child is shown a few
rows of `03-REGISTERS/rigveda-pur-fields.csv` — a real register, not a mock-up
— with its `proposed_geography` column visible. Every one of the 103 rows reads:

> `NOT FILLED — no source`

and every row prints its own reason. `PUR4J-018`, `VERIFIED`: constitution
§4J's proposed-geography field **cannot be filled from the pinned corpus, which
contains no geographic content of any kind.**

> *This is our own table. There is a column for "where". It is empty on every
> single line, and we wrote down why on every single line. We did not leave it
> empty because we forgot.*

**(b) The map that stays empty.** A map of nothing. The child may tap *"show me
where"* and the map does not move, does not zoom, and places no pin. The
caption:

> *We have nowhere to put a pin.*

A pin would be fabricated evidence (§10.4.4). An empty map is not: it is a true
statement about what we can locate, rendered.

**(c) The one word that might be a place.** `PUR4J-017` and `PUR4J-028`, both
`VERIFIED`. Of the 103 fort-passages, 7 carry a word for a mountain and 6 carry
`síndhu-` — the only word in the corpus that can name a river. And `síndhu-`
means either "a river" or "the Indus", and **Griffith and Geldner read it
differently across those six passages**.

> *There is one word in six of the lines that might be the name of a river. It
> might also just mean "a river". The two grown-ups who translated the whole
> poem do not agree, and neither of them can ask the person who wrote it.*

**(d) The thing we are not going to say.** Constitution §4J: *"Do not
automatically translate* pur *into a Mature Harappan city."* Version 12 line
1175 holds the identification of the forts with one archaeological culture.
Stated to the child, plainly, as a decision the museum made:

> *There is a story you may meet somewhere else, that these forts were the
> cities archaeologists dug up beside the Indus river. Our museum does not say
> that. Not because it is impossible — because nothing in the poem says where,
> and we would only be guessing and then pretending we weren't.*

The wording matters and is specified rather than left to copy review. The museum
holds **no source recording who has made that identification**, so the screen
must not attribute it to anyone, count anyone, or characterise a field. What the
museum does hold is its own two rules against making it: constitution §4J's
prohibition on translating *pur* into a Mature Harappan city, and the research
hold at Version 12 line 1175. **The screen states the museum's rule, not a claim
about scholarship.**

**What the child does.** Reads the register rows. Taps the empty map. Compares
the two readings of `síndhu-` — terms: one word, two renderings. Cleared under
§6.1.

**What the child is asked to conclude.**

> *Can you say where the forts were?*

- **No — the poem doesn't say.** ← the evidence
- **There is one word that might be a river's name, and the experts disagree.**
- **We don't know.** · *the poem doesn't say*

No offered answer names a region, a culture or a site. R-03.

**Badge.** **WE DON'T KNOW** · *the poem doesn't say*.

**Rests on.** `PUR4J-017`, `PUR4J-018`, `PUR4J-028` — all `VERIFIED`. Lowest
status: **`VERIFIED`**.

**Field Bag.** The empty column. The two readings of `síndhu-`. The refusal at
(d), which is an institutional statement and is stored as one.

---

#### `CP-3.4` · When? — the weakest link in the whole chain

**Purpose.** This is the screen the investigation exists for. Everything else
shows that the poem is not a photograph of a *thing*. This shows that it is not
a photograph of a *moment* — and, more importantly, that the museum's ability
to say when is thinner than anything else it has told the child.

**It is specified to expose that thinness rather than to survive it.** No
composition date is asserted anywhere on this screen or anywhere in this
investigation. What is shown is what the ordering rests on.

**What is shown, in seven moves, in this order.**

**(a) The museum can put the lines in an order.** Five names, in order:
**Archaic · Strophic · Normal · Cretic · Popular** (`PUR-011`, `VERIFIED`).

> *We can put the lines of this poem in an order — which ones sound older, which
> ones sound newer. Watch how.*

**(b) The order comes from counting rhythms.** Not from dates, not from
contents, not from anything anyone dug up. Arnold sorted the poem by the shape
of its metre.

**What the screen may and may not show here.** `PUR-P-041`'s
`arnold_metre_labels` value is `M M M` — a metre-**type code**, one per pāda.
The column's whole vocabulary across the register is `M, MO, MR, PE2, MG, P,
MT, MV, M5, MVR, MOR, M4`, and **no register row in this repository defines what
any of those codes mean.** Nothing here holds a syllable-level scansion of RV
4.30.20. So the screen **may not** display "how the long and short syllables
fall": generating that would be fabricated evidence under §10.4.4 and `R-07`, on
this investigation's centrepiece screen.

What it shows instead is the true and smaller thing: the three pādas of our
line each carry the same code, `M`, and the museum can tell the child that the
code is Arnold's label for a rhythm-shape without being able to show the shape.

> *Arnold listened to the beat. He gave every line a little code for what its
> beat was like. Ours is the code he wrote "M" for, three times, once per line.*
>
> *We would like to show you the long and short beats themselves. We cannot —
> we do not have them written down anywhere, only his codes.*

**Named as a gap, not passed over.** Two things would fix it and neither has
been done: the van Nooten–Holland metrically restored text (`SRC-078`) is in the
pinned clone and carries the restoration; and Arnold 1905 defines his own metre
vocabulary. Extracting either is `U-8`.

**(c) Our line's period.** RV 4.30.20 is **Strophic**, and the museum's record
says `stratum_certainty = certain` for it (`PUR-P-041`) — as against 14 of the
106 fort-tokens where Arnold's assignment rests on metrical variations alone
and is flagged lower-confidence (`PUR-011`, `rv01-reconciliation.md` §3).

> *Our line is in the group Arnold called "Strophic". For some other lines he
> was less sure, and we keep a mark on those. Ours does not have the mark.*

**(d) Where the order comes from: one book, one man, 1905.** The child is shown
**the actual page**. `SRC-026`: E. V. Arnold, *Vedic Metre in its Historical
Development*, Cambridge 1905, Appendix IV, §265 "Explanatory Notes", printed
page 269 — archive.org item `vedicmetreinitsh00arnouoft`, scan OBJECT 289. It
is retrievable, it is out of copyright, and it is where the five names are
defined. `PUR-011`, `VERIFIED`.

> *Here is the actual page. A man called Edward Vernon Arnold worked this out
> and printed it in 1905. Everything we just told you about which lines are
> older comes from this one book.*

**(e) Arnold said himself that he wasn't sure.** He called his own period names
*provisional* (Arnold 1905 §§60–61, recorded at `PUR-026`).

> *He said so himself, in the same book. He called his names for the periods
> "provisional" — which is a grown-up word for "this is my best go, don't build
> anything heavy on it".*

**(f) The museum tried to check it a second way, and the second way could not
tell.** Two instruments, both shown — and the wording here is load-bearing, so
it is specified exactly:

| instrument | what it says about the fort-words |
|---|---|
| Arnold's rhythms | a difference big enough to be worth reporting: the fort-words are commoner in the early-sounding lines and rarer in the late-sounding ones (`PUR-014`, `PUR-016`, `PUR-017`, `PUR-018`; χ² = 14.57 on 4 df at the hymn level, p = 0.0057) |
| the order of the books | **could not resolve a difference this size.** The point estimate leans the same way — 6.98 per 10,000 in books 2–7 against 6.07 in the rest — but on 106 tokens the test cannot separate that from nothing (`PUR-020`: χ² = 0.50 on 1 df, p = 0.48) |

**This is not "the two instruments disagree", and an earlier draft of this
screen said it was.** `04-AUDITS/REAUDIT-QUEUE.csv` `RA-002` is `OPEN` on
exactly that wording, raised by `BF-004`, whose control is binding:
*"any null result in this repository reports the point estimate and its
direction alongside the p-value, and states the power limitation, before it is
allowed to bear on a hypothesis."* `PUR-020` says the difference is *not
significant* — which is a failure to detect, not a detection of no difference.
Turning that into "no difference at all" would make a null into a positive
finding, which constitution §6 forbids in terms: *"unknown" is residual, never a
positive rival explanation.* The error also ran toward this screen's own
preferred story, which is what makes it worth naming rather than quietly fixing.

> *We tried to check it another way, by looking at which book of the poem each
> line is in. That way could not tell. It leans the same direction, but there
> are not enough fort-words in the poem for it to be sure of anything.*
>
> *So we did not get a second answer. We got a shrug. A shrug is not agreement,
> and we are not going to count it as one.*

**Badge on the second instrument: WE DON'T KNOW · *we haven't looked yet*** —
because the remedy is a bigger or better-powered instrument, not a fact about
the poem. It may not be badged **FOUND**.

And the entanglement, because leaving it out would make the two look more
independent than they are: `PUR-021` (`VERIFIED`) records that 61.3% of all
"Popular" material is in book 10, so the two instruments are partly counting the
same thing twice.

**(g) An order is not a date. The museum has no year for this poem.**
`DE-M-027`, `VERIFIED`, quoted with its elision marked:

> *"The attestation dates that would date the languages themselves — … the
> Rigvedic strata in absolute years — cannot be established from anything
> retrieved in this session."*

Two things follow, and they are different sizes:

- **Established**: no absolute date for the Rigvedic strata was obtainable from
  anything retrieved in the session that produced `DE-M-027`. That is the claim,
  and it is scoped to a session.
- **Asserted here, with its coverage stated**: no absolute date for the Rigveda
  appears anywhere in the working tree of this repository. The search was a
  full-text scan of every tracked file for date expressions and era markers, run
  on 2026-09-09 against `main` — **the working tree, not the full history**. On
  the negative-evidence standard that is `ABSENT DESPITE ADEQUATE SEARCH` for
  the tree and nothing at all for the history, and the coverage boundary is
  stated here because `RA-018` is `OPEN` on exactly this omission elsewhere.

This investigation asserts no composition date.

> **WE DON'T KNOW** · *we haven't looked yet*
>
> *We can say which lines sound older than other lines. We cannot say what year
> any of them was made. Not roughly, not "about". We do not have that, and we
> are not going to make one up to finish the sentence.*

**(h) The status the museum itself gives this.** Shown as a card, in the child's
badge and in the real word beneath it:

> *"Arnold's five periods are really older-and-newer."*
> **MAYBE** — `HYPOTHESIS` (`PUR-028`)
>
> *This is the thing everything else on this screen is standing on, and it is
> the least sure thing we have shown you all day. We have not checked it. Nobody
> here has checked it another way that worked.*

`04-AUDITS/ARCHIVE-AND-POWER-AUDIT.csv` `APA-E-006` states it for the adults:
*"whether the metrical layering tracks composition date at all is an assumption
inside the instrument, not a result from it."* The child gets the badge; the
badge reaches the row.

**What the child does.**

- Puts the five period names in order. Terms: metrical periods of a text.
  Cleared under §6.3, with its two conditions.
- Opens the 1905 page and looks at it.
- Drags our line onto a timeline — **and the timeline has no numbers on it.**
  It has five bands and no years, because the museum has no years. Attempting to
  place a year is not a failure state; there is simply nowhere to put one, and
  the screen says why.

**What the child is asked to conclude.** Two questions, deliberately separated:

> *Can you say which lines sound older than others?*
- **Maybe — one man worked it out in 1905 and nobody has checked it another way
  that agreed.** ← the evidence

> *Can you say what year the poem was made?*
- **No.** · *we haven't looked yet*

**Badge.** The screen's own badge is **MAYBE**, because the lowest status
beneath it is `HYPOTHESIS`. It may not be badged higher. §1.3, property 4.

**Rests on.** `PUR-011`, `PUR-012`, `PUR-013`, `PUR-014`, `PUR-015`, `PUR-016`,
`PUR-017`, `PUR-018`, `PUR-019`, `PUR-020`, `PUR-021` (all `VERIFIED`),
`PUR-P-041`, `DE-M-027` (`VERIFIED`), `APA-E-006` (`VERIFIED`), `PUR-026`
(**`PROVISIONAL`**), `PUR-028` (**`HYPOTHESIS`**).
**Lowest status: `HYPOTHESIS` — `PUR-028`.**
Verifying units: **`U-2`** (a second, independent stratification instrument
would test `PUR-028` and could move `PUR-026`) and **`U-3`** (retrieve what any
absolute date for the Rigveda rests on, so that this screen can show the
argument rather than only its absence).

**Field Bag.** The five periods. The 1905 page. The two instruments and their
disagreement. The `MAYBE` card, which is the single most important object in
the bag and is stored with `PUR-028` attached.

**Design note — the one temptation to refuse.** It would be easy, and it would
feel generous, to give the child *some* date: "about three and a half thousand
years ago." Every popular account of this material does. This specification
does not, because the repository holds nothing that would support it, and
because a number offered to a child to spare them an unknown is exactly the
move the whole investigation is teaching them to catch. `U-3` is what would
change this, and until `U-3` runs, the timeline has no numbers on it.

---

#### `CP-3.5` · Has anyone dug? — the museum's own notebook

**Purpose.** The ground half of the investigation. It is empty, and the screen
makes the emptiness checkable rather than announcing it.

**The design problem, stated first.** A children's screen about archaeology
that has no archaeology has three possible shapes, and two are forbidden:

1. Show a photograph of an excavated wall and let the child infer a connection.
   **Forbidden** — §10.4.4, fabricated evidence, and R-03.
2. Delete the screen and never raise the question. **Forbidden in effect** —
   the child asked it at `CP-2.1`, and a museum that drops the question it was
   asked is teaching that unanswerable questions are improper.
3. Show what the museum has actually read, and let the child find the gap.

The third is what is specified.

**What is shown.** `02-SOURCES/access-ledger.csv` — the museum's real ledger,
98 rows at the time of writing (`SRC-001`–`SRC-098`, derived with `csv.DictReader`, not from the line count) — rendered as a shelf, grouped by kind:

| kind | roughly what is there |
|---|---|
| the poem itself | four editions, plus the ancient word-by-word analysis |
| dictionaries | Grassmann's, and word-lists |
| translations | six, in four languages |
| a book about rhythms | Arnold 1905 |
| word databases | several |
| websites that would not open | a number of them, each with the date we tried |
| **digging reports** | **nothing** |

The child taps **digging reports**. The shelf is empty. Not "loading", not
"coming soon" — empty, with the count zero and a date.

**The sentence the screen must carry, and the distinction it protects.**

> *Our museum has not read a single digging report. Not one.*
>
> **WE DON'T KNOW** · *we haven't looked yet*
>
> *So we cannot tell you what the ground shows. We also cannot tell you that
> nobody knows, because we have not been to look at what anybody else has
> written down. Those are two different kinds of not knowing and this is the
> second one: ours.*
>
> *That is why we are not going to show you a picture of a wall and tell you it
> is the one in the poem.*

This is §5.2 in the child's words, and getting it exactly right is the whole
point of the screen. **"We haven't looked" and "the poem doesn't say" are
different, and a child who leaves able to tell them apart has the transferable
part of the method.**

**What the child does.** Filters the shelf by kind. Taps any source to see what
it is, when it was retrieved, and — for the ones that would not open — the date
we tried and what the error was.

**What the child is asked to conclude.**

> *Has our museum looked at what came out of the ground?*

- **No. Not yet.** ← the evidence

And, offered separately, because it is the question the first one provokes:

> *Does that mean nobody knows?*

- **We can't tell you.** · *we haven't looked yet*

**The specification is deliberate here, and an earlier draft was not.** It
answered this second question **"No"** — which would have had the museum assert
to a child that somebody, somewhere, knows, on the strength of nothing. The
museum has no source for what the archaeological record contains. It has a
source for what it has itself read, which is the shelf the child just filtered.
Those are the only two things this screen may say, and the second question gets
the honest non-answer rather than the reassuring one.

**Badge.** **FOUND** — that our ledger contains no excavation source. That is a
checkable fact about our record, and the child just checked it. The ground
itself: **WE DON'T KNOW** · *we haven't looked yet*.

**Rests on.** `02-SOURCES/access-ledger.csv` as read on 2026-09-09;
`HOLD-008`. The repository has precedent for citing itself as a searched
source — `SRC-048`, `SRC-086`, `SRC-098`. Lowest status: **`VERIFIED`** for the
statement about our ledger; the ground question carries no claim at all, which
is why it is **WE DON'T KNOW** and not a claim badged low.
Verifying unit: **`U-1`**.

**A note for whoever builds this.** The shelf must read from the ledger at
build time, not from a copy. If `U-1` runs and an excavation report enters the
ledger, this screen must stop saying the shelf is empty **on the same day**, and
every Field Bag holding the old card must show the change (§10.3). A hard-coded
"nothing here" would become a lie the moment the museum did its homework.

---

#### `CP-3.6` · What is a "fort", anyway? — the word is ours, not the poem's

**Purpose.** Constitution §7's translation standard at a reading age, and §4E's
attestation gradient: the poem's word, a translator's English word, and a modern
guess are three different things.

**What is shown, in four moves.**

**(a) The poem's word.** `púr-`. Shown in Devanagari, transliterated, and with
its dictionary definition — Grassmann 1873, the standard nineteenth-century
Rigveda dictionary (`PUR4J-021`, `VERIFIED`):

> *"Wall aus Steinen und Lehm, Verschanzung, Palisade"*
> — a wall of stones and clay, an earthwork, a fence of stakes.

> *Not a city. Not a town. Not a castle. The oldest proper dictionary of this
> poem says: a wall, or a bank of earth, or a fence made of posts.*

**(b) What shape the word usually takes.** `PUR4J-020`, `VERIFIED`, stated
exactly as the register states it and no further: of the 83 simple fort-words,
**67.5% are accusative** — the grammatical shape a word takes when it is the
thing a verb is done *to* — and **3.6%, three of 83, are locative**, the shape
for being *in* something. Shown as 83 marks, coloured two ways.

> *Words in this language change shape depending on their job in the sentence.
> Nearly always, the fort-word is in the shape for "the thing something is done
> to". Three times out of eighty-three it is in the shape for "the place
> somebody is in".*

**What this screen may not say, and an earlier draft did.** It may not say the
forts are *"broken, thrown down, split"*. Accusative case says a verb acts on
the word; it does not say which verb. That reading is `PUR-027`, a
**`HYPOTHESIS`**, whose note records that testing it *"requires reading each of
the 106 passages for the grammatical role of pur-, which this unit did not do."*
Nor may it say that this is not how the words would fall for towns — that is
`PUR4J-I-03` `evidence_for` (1), **`PROVISIONAL`**, and it belongs on the
screen's conclusion card at its own badge, not in the caption of a `VERIFIED`
measurement. `PUR4J-020`'s own note is the discipline: *"a measurement of case
distribution, not an interpretation of it."*

The interpretation is still offered — on its own card, badged **WE THINK**:

> **WE THINK** *(`PUR4J-I-03`, `PROVISIONAL`)*
> *If you were describing towns where people lived, our museum thinks that is
> not how the word-shapes would fall. That is us reading the numbers, not the
> numbers themselves.*

**(c) Three that break any single picture.** Three cards, each a real passage:

| RV 8.1.28 | a fort that **moves** (`cariṣṇú-`) |
| RV 7.95.1 | a fort that **is a river** — Sarasvatī *is* one |
| RV 7.15.14 | a god asked **to be** one |

> *Whatever these are, they are not all the same kind of thing. One of them
> moves. One of them is a river.*

**(d) COMPARE — the words people have used.** Not a quiz. **Eight cards**, each
with the word, who used it, and *what it makes you picture*, drawn from
`pur-translation-standard.md` §9 and `PUR4J-022` (`VERIFIED`). The last two are
the non-English ones, and they are on the card because cutting them would leave
a screen about translation that had quietly translated only into English:

| English word | who | what it makes you picture | what breaks |
|---|---|---|---|
| **city** | Griffith, **once** in 103 passages | streets, houses, thousands of people | the poem says it is a wall of stones and clay; and if you say city, the next step to "so it was one of the dug-up Indus cities" happens almost by itself |
| **castle** | Griffith, 33 times | a stone keep with a lord in it | that is medieval Europe, not this |
| **fort / fortress** | Griffith, 67 times | something built to be defended | fine for the ones that get stormed; wrong for the river and the god |
| **stronghold** | Griffith, 5 times | a defended place, unspecified | the least committed |
| **wall / rampart / palisade** | Grassmann's own definition | an earth bank or a fence, maybe with nothing permanent inside | fits the unbaked one, and the moving one |
| **Burg** | both German translators, ~80 times each | a fortified seat — between fort and castle | neither German translator **ever** writes *Stadt*, "city". But see the caution below: these are not two independent votes |
| **forteresse / citadelle** | Renou, in French, across 58 of the 103 passages | a fortress, or a citadel — a stronghold inside a town | *citadelle* 22 times imports a town for the citadel to sit in |
| **крепость** | Elizarenkova, in Russian | a fortress | `DEP-023`: she worked with Geldner in view |

> *Every one of these is somebody's choice. The poem did not write any of them.
> When you read "ninety-nine castles" in English, the castles were put there by
> a man in 1890.*

**The counting caution, on the card and not in a footnote.** `DEP-021`: the
Grassmann dictionary that supplied the *"wall, rampart, palisade"* row and the
Grassmann translation that helped supply the *Burg* row are **one man's
judgement expressed twice**, and the dependency register says in terms that he
*"must not be counted as an independent vote alongside the Grassmann gloss that
defined the family."* `DEP-023`: Elizarenkova is not independent of Geldner.
Six columns; four judgements at most.

> *Careful with counting. Two of these are the same man twice — he wrote the
> dictionary and one of the translations. And one of them was working with
> another one open beside him. So do not count the columns and think that is how
> many people agreed.*

**And the counts themselves are indicative, not exact.** `PUR4J-022`'s locator
records that they were made by surface-string match and not lemmatised. The card
says so.

**What the child does.** Reads (a)–(c). Turns the cards in (d). **No answer is
scored and no word is marked correct** — R-05, and because there is no correct
one: the register's own finding (`PUR4J-I-03`, `PROVISIONAL`) is that no single
English word or archaeological referent can stand for this corpus.

**What the child is asked to conclude.**

> *Is the poem talking about one kind of thing?*

- **We think not.** ← the museum's position, `PROVISIONAL`
- **The English word was chosen by somebody.** ← the evidence
- **We don't know what most of them were.** · *the poem doesn't say*

**Badge.** (a), (b), (c) and the translator counts: **FOUND**. The conclusion
*"not one kind of thing"*: **WE THINK** — `PUR4J-I-03`, `PROVISIONAL`.

**Rests on.** `PUR4J-020`, `PUR4J-021`, `PUR4J-022` (`VERIFIED`), `PUR4J-015`,
`PUR4J-025` (**`PROVISIONAL`**), `PUR4J-I-03` (**`PROVISIONAL`**). Lowest
status: **`PROVISIONAL`**. Verifying unit: **`U-5`**, and the register's own
falsifier — a lexicon independent of the Grassmann–Geldner line rendering
`púr-` as a settlement word would weaken this (`pur-translation-standard.md`
§11); the obvious candidates were unreachable at `SRC-080`–`SRC-083`, so this
is also **`U-6`**.

**Balance check, run and recorded.** This screen could tip into "so the forts
were never real", which is not what the evidence says and is the deflationary
answer `PUR4J-I-01` warns is convenient. `PUR4J-I-03`'s own
`evidence_against` field is therefore shown on the screen's last card, not
buried: **48 of 103 passages do present a fort as an object in the story**;
they have named holders, two of them state a material, one has a gate, and one
may have a name. The card reads:

> *Do not go too far the other way. In about half the lines, a fort is a real
> thing in the story that somebody holds and somebody else breaks. We are not
> saying the poem made all of them up. We are saying you cannot tell, from the
> poem alone, which ones stood anywhere.*

---

#### `CP-3.7` · Who lived in them? — read only, and here is why

**Purpose.** To answer, truthfully, the question a child will certainly ask,
**without building the interface §10.4.7 forbids.** §6.2 sets out the reasoning;
this is the screen.

**Interaction: none.** No buckets. No matching. No drag. No quiz. No "which
side?". No tap-to-sort. The card scrolls and that is all it does. This is not a
degraded version of a better screen; the absence of interaction *is* the
design, per §10.4.7: *"the material is read, with its status and its date, not
operated."*

**What is shown.**

> *The poem names people. Some are the people the songs are for. Some are the
> people the songs are against. You will see their names if you read the lines:
> Divodāsa, Śambara, Pipru, Śuṣṇa.*
>
> *We are not going to ask you to put them into groups.*
>
> *Here is why. To sort those names, we would have to use somebody's list of
> which name goes on which side. The list we have comes from a dictionary
> written in the 1870s, and that dictionary files one side under a word that
> means "demons". A man chose that word before anybody had read these lines
> carefully. If we handed you the list, you would be sorting people using his
> word, not the poem's.*
>
> *So: the poem names people, we can show you the names, and we are not going
> to give you a box to put them in.*

**Status shown with it**, as §10.4.7 requires — with its status and its date:

- That the register's opponent side is sorted by Grassmann's category *Dämon*:
  `pur-translation-standard.md` §10, logged in `04-AUDITS/REAUDIT-QUEUE.csv`.
  Badge: **FOUND** — this is a fact about the dictionary, dated 1873.
- That 22 of 103 passages carry a patron-side name and 22 an opponent-side
  name, **on Grassmann's classification of the name and not on a reading of any
  passage**: `PUR4J-030`, `VERIFIED`. Its own `roles_basis` field, printed on
  every row of `rigveda-pur-fields.csv`, says: *"A name can occur in a passage
  without holding or attacking anything in it."*
- Who held the forts: **WE DON'T KNOW** · ***we haven't looked yet*** — and, on
  tap, the museum's own note that this has been logged unbuilt as `PUR-027`, a
  `HYPOTHESIS`, precisely so that a word-frequency pattern is not mistaken for
  an answer.

  **The second line is the other one, and an earlier draft had it wrong.** It
  read *"the poem doesn't say"*, which closes the question in the museum's
  favour. The poem is not silent: `PUR4J-030` establishes that 22 of 103
  passages carry a patron-side name and 22 an opponent-side name, and `PUR-027`
  says in terms that testing what the fort-word is doing in each passage
  *"requires reading each of the 106 passages … which this unit did not do."*
  The remedy is a reading, not a shrug — so this is *"we haven't looked yet"*.
  Getting this the wrong way round on this screen, of all screens, would have
  been the specification failing its own §5.3 at the point where §5.3 matters
  most.

**What the child is asked to conclude.** Nothing. There is no prompt on this
card. A prompt would be an exercise, and an exercise is what is forbidden.

**Rests on.** `PUR4J-030` (`VERIFIED`), `PUR-022` (`VERIFIED`), `PUR-027`
(**`HYPOTHESIS`**), `pur-translation-standard.md` §10. Lowest status:
**`HYPOTHESIS`** — which is why the "who held them" line is badged **WE DON'T
KNOW** rather than **WE THINK**, and why no version of this card may state who
the fort-holders were.

**What this screen is not.** It is not a lesson about racism dressed as a
history screen, and it is not an accusation against a dead lexicographer. It is
a true statement about how the record the museum uses was assembled, which
§10.4.6 permits a child to be told, and a refusal to hand the child the
categories, which §10.4.7 requires.

---

### STAGE 4 — DECIDE

#### `CP-4.1` · What do you think?

**Purpose.** §10.4.3 stage 4: the child states what they think and what they
are unsure about; two or more real explanations are available; **"we don't
know" is offered and is never scored as a failure.**

This screen is where the user's requirement lands: *a child should end able to
say what the poem claims, what the ground shows, and where the two do not
meet.* It is built as exactly those three sentences.

**What is shown.** The child's own Field Bag, laid out as three unfinished
sentences. Each is completed by choosing from real options, editing them, or
writing from scratch. Nothing is required.

---

**Sentence one — what the poem claims.**

> *The poem says …*

Offered completions, each carrying the badge it earned upstream:

| completion | badge | from |
|---|---|---|
| a god threw down a hundred forts made of stone, for a man called Divodāsa | **FOUND** *(that the poem says it)* | `CP-1.2` |
| forts get broken, over and over, in a hundred and three different lines | **FOUND** | `CP-3.1` |
| the forts are hardly ever described — ten lines out of a hundred and three say what one was made of | **FOUND** | `CP-3.2` |
| a fort in this poem is not always a building. One is a river. One is a god. One moves. | **FOUND** | `CP-3.6` |

---

**Sentence two — what the ground shows.**

> *The ground shows …*

Offered completions — and this is the shortest list on the screen, which is the
point:

| completion | badge |
|---|---|
| **nothing to us yet — our museum has not read a single digging report** | **WE DON'T KNOW** · *we haven't looked yet* |
| I don't know | **WE DON'T KNOW** · *we haven't looked yet* |

**There is no third option**, and specifically there is no option of the form
*"the ground agrees"* or *"the ground disagrees"*, because the museum holds no
evidence that would support either. A child who wants to write one may write
it; the museum will not offer it. If they do write one, the screen does not
mark it wrong — it shows, beside it, the empty shelf from `CP-3.5`.

---

**Sentence three — where the two do not meet.**

> *You cannot put the poem on top of the ground because …*

Multi-select. Each option carries its evidence on tap:

| completion | badge | from |
|---|---|---|
| the poem does not say **where** | **FOUND** | `CP-3.3`, `PUR4J-018` |
| nobody here can say **when** the poem was made — only which lines sound older, and that comes from one book from 1905 | **MAYBE** | `CP-3.4`, `PUR-028`, `DE-M-027` |
| you cannot **count** the forts — one word can mean a hundred | **FOUND** | `CP-3.1`, `PUR4J-020` |
| the poem only ever uses four numbers, and two of them also count rivers | **FOUND** | `CP-3.1`, `PUR4J-006`, `PUR4J-009` |
| the English word "fort" was chosen by a translator, not by the poem | **FOUND** | `CP-3.6`, `PUR4J-021`, `PUR4J-022` |
| **nobody at this museum has looked at the ground yet** | **WE DON'T KNOW** · *we haven't looked yet* | `CP-3.5` |

**What the child does.** Completes as many of the three sentences as they want
to. Edits any completion. Writes their own. **Nothing is submitted.** There is
no send button. §10.4.5: no free-text publication, no transmission by default,
and a child's writing never enters the correction pipeline.

**What the child is asked to conclude.** Exactly the three sentences and
nothing further. There is no fourth sentence asking them to decide whether the
forts were real, because the museum cannot answer that and will not ask a child
to answer what it cannot.

**Badge.** None on the screen itself; every completion carries its own.

**How "we don't know" is handled.** It appears twice as a *first-class
completion*, in the same type at the same size as every other option, with the
same tappable evidence beneath it, and never with softening language. It is
never last in a list, never greyed, and never accompanied by encouragement. It
is an answer the museum itself is giving on the same screen, and the child can
see it is the museum's answer too.

**Rests on.** Everything upstream. Lowest status: **`HYPOTHESIS`** (`PUR-028`,
via sentence three's *when* option, which is badged **MAYBE** accordingly).

---

### STAGE 5 — CHECK

#### `CP-5.1` · What the museum thinks, and how sure it is

**Purpose.** §10.4.3 stage 5, part one: what the institution currently thinks,
with its status.

**What is shown.** Three cards. Not one — three, because the museum's positions
on this material do not agree with each other about how confident to be, and
flattening them would be the false-equivalence failure in reverse.

**Card 1.**
> *"A* púr *is not one kind of thing. No single English word fits them all."*
> **WE THINK** — `PROVISIONAL` (`PUR4J-I-03`)
>
> *Five different measurements point this way. But nearly half the lines still
> describe a fort as a real thing somebody holds and somebody breaks, and we
> have no evidence about whether any of those stood anywhere.*

**Card 2.**
> *"The numbers are the poem's favourite numbers, not a tally."*
> **WE THINK** — `PROVISIONAL`, and weakly held (`PUR4J-I-01`)
>
> *Two of our four tests came out this way. One did not, and it was the
> strongest one: one enemy's forts are counted at ninety-nine three times and at
> a hundred twice, which is what you would get if somebody were counting and
> rounding.*
>
> *We got this one wrong the first time and had to fix it. The record of the
> mistake is kept.*

The Śambara figure in that card is **`PUR4J-007`**, `PROVISIONAL`, and it is
named here because it is the most-corrected row in the register set — `BF-014`
was logged against its first version, which was false in three of five parts
with all three errors running toward this card's own conclusion. A children's
card carrying that figure untraceably would be the same failure at a smaller
size. It is in this screen's `Rests on` list and in `EVIDENCE-MANIFEST.csv`.

**The badge is `WE THINK`, not `MAYBE`, and an earlier draft had it wrong.**
`PUR4J-I-01` is `PROVISIONAL`, and §1.3's mapping sends `PROVISIONAL` to
**WE THINK** without exception. Downgrading it to **MAYBE** to signal "weakly
held" would break the one property that makes the badges trustworthy — that a
child tapping a badge always reaches the same status word (§1.3, property 2).
Weakness is expressed in the card's *text*, which is where it belongs, not by
mislabelling the status.

That last line is required. `PUR4J-I-01` rests partly on a claim that was false
in three of five parts, all three errors running toward its own conclusion, and
the failure is logged as `BF-014` — a preferred-counter-narrative failure. A
children's card that presented this reading as the museum's confident finding
would repeat the error the log exists to prevent.

**Card 3.**
> *"The fort-words are not a late addition to the poem."*
> **WE THINK** — `PROVISIONAL` (`PUR-026`) — *and only if the 1905 book is
> right, which is a* **MAYBE** *(`PUR-028`).*
>
> *This one is stacked on the wobbliest thing we showed you. We are keeping it
> at "we think" instead of "found" for exactly that reason.*

**Badge.** As shown per card. No card may display higher than the lowest claim
beneath it (§1.3, property 4) — which is why card 3 shows both badges rather
than the better one.

**Rests on.** `PUR4J-I-01`, `PUR4J-I-02`, `PUR4J-I-03`, `PUR-026` (all
**`PROVISIONAL`**), `PUR-028` (**`HYPOTHESIS`**). Lowest status:
**`HYPOTHESIS`**.

---

#### `CP-5.2` · Where you agreed, and where you differed

**Purpose.** §10.4.3 stage 5, part two: *"explicitly, where the child's
reasoning matched or differed. A difference is presented as interesting, not
wrong."*

**What is shown.** The child's three sentences from `CP-4.1`, beside the
museum's three cards from `CP-5.1`, aligned on what they are about rather than
scored against each other.

Where they match:
> *You and the museum said the same thing here.*

Where they differ:
> *You said something different from us here. That is worth keeping. Here is
> what we were looking at when we said ours — and if you think we are wrong,
> that is allowed. We have been wrong on this page before.*

Tapping through reaches the evidence on both sides.

**What is never shown.** No score. No count of matches. No "you got 4 of 6".
No badge awarded to the child. R-05, and §10.4.4's prohibition on competition
in full.

**Design note.** The correction card at `CP-3.1f` and card 2 at `CP-5.1` exist
partly so that this screen's offer — *if you think we are wrong, that is
allowed* — is not a pleasantry. The child has already watched the museum
correct itself twice. The invitation is credible because it has been
demonstrated.

---

#### `CP-5.3` · What would change our minds

**Purpose.** Constitution §5 step 12 — record falsifiers — at a reading age.
These are taken from the registers' own `falsifier` fields, not invented for
the screen.

**What is shown.** Four cards, each naming a real thing that could happen:

| If somebody found … | it would change … | from |
|---|---|---|
| **a line of the poem with an awkward number of forts** — twenty-three, or forty-one | our idea that the numbers are just the poem's favourite numbers | `PUR4J-I-01` falsifier |
| **somebody who has read the digging reports**, and a wall of stones somebody has put a date on | this whole page — we would finally have a ground to compare the poem to | `HOLD-008`, `U-1` |
| **a second way of telling which lines are older**, that agreed with the 1905 book | how sure we can be about *when* — right now our second way disagreed | `PUR-028`, `U-2` |
| **an argument that settles whether that metal word means iron or bronze** | *when* again — but only if a further thing is also shown, below | `PUR4J-023`, `U-4` |

**The fourth card carries a rider, and it is a rule of the method rather than a
detail.** "The two metals have different histories here, so settling the word
would move the date" is **two claims joined**, not one: a claim about the
metal-word, and a claim about when each metal was in use in this part of the
world. The museum holds the first (`PUR4J-023`, `VERIFIED`) and **holds nothing
at all for the second** — it survives only in `PUR4J-023`'s notes field, has no
claim row, no locator and no retrieval behind it. Under constitution §5 step 10
that join is a **bridge** between two evidence classes, textual and material,
and every bridge is a separate claim needing its own mechanism and its own
status.

So the card is specified to say the smaller true thing:

> *If somebody settled whether that word means iron or bronze, it might help
> with "when" — but only if somebody else has worked out when each of those
> metals was around here. We have not looked that up either. So this is a
> falsifier with a second half missing, and we are telling you which half.*

Badge: **WE DON'T KNOW** · *we haven't looked yet*. The missing half is `U-4`'s
second requirement.

> *These are not wishes. They are things that could actually turn up. When one
> of them does, we will change what this page says, and we will leave the old
> version where you can see it.*

**Badge.** None — these are conditions, not claims.

---

#### `CP-5.4` · The one thing to take away

**Purpose.** The investigation's answer to its own question, in the child's
hands rather than in the museum's voice.

**What is shown.** One card, and the child's own three sentences beneath it.

> **Why a poem is not a photograph**
>
> *A photograph shows what was in front of the camera, and it usually has a
> date on the back.*
>
> *This poem tells you what somebody said. It does not say where. Nobody here
> can tell you when. One of its words can mean a hundred forts. It uses the same
> four numbers over and over, and two of those words count rivers somewhere
> else. And the word "fort" is not in the poem at all — somebody put it there
> in English.*
>
> *So you cannot lay the poem on top of the ground. Not because the poem is
> lying. Because you would need a place and a date to lay it on, and nobody has
> given us either one yet.*
>
> *That is a real answer. It is not a way of saying we ran out of time.*

**Field Bag, on close.** The bag is offered for export (§10.3, §5.2): a dated,
revision-pinned set of everything collected, statuses intact, the child's own
writing kept separate from the museum's text. No account. No upload. It is a
file on the child's own device.

---

## 8. What the investigation rests on, screen by screen

Full detail in `SCREEN-CLAIM-DEPENDENCY.csv` and `EVIDENCE-MANIFEST.csv`. The
summary:

| Screen | Lowest status beneath it | Screen badge ceiling | Unit that would raise it |
|---|---|---|---|
| `CP-1.1` | `VERIFIED` | FOUND | — |
| `CP-1.2` | `VERIFIED` | FOUND | — |
| `CP-2.1` | *(no evidence shown)* | — | — |
| `CP-3.1` | **`PROVISIONAL`** (`PUR4J-026`, balance card only) | FOUND on the measurements; WE THINK on the balance card | `U-5` |
| `CP-3.2` | **`PROVISIONAL`** (`PUR4J-013`) | WE THINK | `U-5` |
| `CP-3.3` | `VERIFIED` | FOUND | — |
| `CP-3.4` | **`HYPOTHESIS`** (`PUR-028`) | MAYBE | `U-2`, `U-3` |
| `CP-3.5` | `VERIFIED` *(about our ledger)*; **no claim** about the ground | FOUND / WE DON'T KNOW | `U-1` |
| `CP-3.6` | **`PROVISIONAL`** (`PUR4J-I-03`, `PUR4J-025`) | WE THINK | `U-5`, `U-6` |
| `CP-3.7` | **`HYPOTHESIS`** (`PUR-027`) | WE DON'T KNOW | *none proposed — see below* |
| `CP-4.1` | **`HYPOTHESIS`** (`PUR-028`, via *when*) | MAYBE on that option only | `U-2`, `U-3` |
| `CP-5.1` | **`HYPOTHESIS`** (`PUR-028`) | MAYBE on card 3 | `U-2` |
| `CP-5.2` | *(reflects upstream)* | — | — |
| `CP-5.3` | *(conditions, not claims)* | — | — |
| `CP-5.4` | **`HYPOTHESIS`** (`PUR-028`) | as `CP-4.1` | `U-2`, `U-3` |

**`CP-3.7` is the one screen where no verifying unit is named, on purpose.**
`PUR-027` — that the *púr-* is a fortification the composers attack rather than
inhabit — could be tested by reading all 106 passages for the grammatical role
of the fort-word, and that unit is worth running for the adult record. It would
not change this screen, because the screen does not assert who held the forts
and would not assert it at any status. Naming a unit here would imply the card
is waiting to say something it is never going to say.

**The full list of `claim_id`s this investigation uses.** 45 distinct
identifiers are cited. 42 carry a status: **32 `VERIFIED`, 8 `PROVISIONAL`, 2
`HYPOTHESIS`**. The other three carry none — two passage rows, which are
addresses rather than claims (`PUR-P-041`, `PUR-P-101`), and one
archive-and-power-audit row (`APA-E-006`).

- `VERIFIED` (32): `PUR-005`, `PUR-011`, `PUR-012`, `PUR-013`, `PUR-014`,
  `PUR-015`, `PUR-016`, `PUR-017`, `PUR-018`, `PUR-019`, `PUR-020`, `PUR-021`,
  `PUR-022`, `PUR-023`, `PUR4J-001`, `PUR4J-002`, `PUR4J-003`, `PUR4J-004`,
  `PUR4J-006`, `PUR4J-008`, `PUR4J-009`, `PUR4J-012`, `PUR4J-015`, `PUR4J-017`,
  `PUR4J-018`, `PUR4J-020`, `PUR4J-021`, `PUR4J-022`, `PUR4J-023`, `PUR4J-028`,
  `PUR4J-030`, `DE-M-027`.
- `PROVISIONAL` (8): `PUR-026`, `PUR4J-013`, `PUR4J-014`, `PUR4J-025`,
  `PUR4J-026`, `PUR4J-I-01`, `PUR4J-I-02`, `PUR4J-I-03`.
- `HYPOTHESIS` (2): `PUR-028`, load-bearing at `CP-3.4` and the lowest status in
  the whole investigation; and `PUR-027`, referenced at `CP-3.7` only to say
  that the museum has not answered who held the forts.

**Nothing `INHERITED-UNVERIFIED` is shown to a child as evidence.** Three
inherited things are *used* and none of them is evidence: the four-badge
vocabulary (a display convention), backlog item 33's six-step flow (a design
input, superseded here by framework §10.4.3), and the curatorial audit's
posture assignment for `the-forts` (an editorial assignment, and the subject of
`D-055` precisely because it is unverified).

---

## 9. What this investigation will not let a child do

Full table with rule citations: `REFUSED-AFFORDANCES.csv`. Ten refusals. The
three that a builder is most likely to undo without noticing:

- **R-01.** No sorting of the people the poem names, in any interaction, under
  any framing, including a debunking framing. §10.4.7. The corpus supplies the
  buckets ready-made (§6) — this refusal has to be actively held, not merely
  intended.
- **R-03 and R-06.** No archaeological culture, site or region named beside a
  fort, and no pin on the map. §4J; Version 12 line 1175; §10.4.4.
- **R-05.** No score, badge, streak, timer or progress reward anywhere, on any
  screen, including the "well done" that creeps in during copy review.
  §10.4.4, §10.4.7 second constraint.

---

## 10. Gates, and what would open them

| Gate | Kind | What it blocks | Answer needed from |
|---|---|---|---|
| **G-1** posture: Nocturnal Veḷi or Reading Room | blocking | the entire build — Field Mode is forbidden in Reading Room (§1.7) | owner, `D-055` |
| **G-2** may the pilot ship with a truthfully empty ground half? | blocking | release, not build | owner, `D-056` |
| **G-3** is this the pilot at all? | open | scheduling | owner, `D-006`; option recorded at `D-057` |
| **G-4** rights and licences for every asset shown | required before build | `CP-1.1`, `CP-3.4` | `U-7` |
| **G-5** re-clone of the pinned corpus at `d3eb8af` | mechanical | every "pulled at build" item | whoever builds |

**G-4 in detail**, because it is the gate most likely to be discovered late.
Every item this investigation displays needs its rights position recorded per
framework §11.8, including for classroom use:

- the Saṃhitā, padapāṭha, Devanagari and morphological layers (`SRC-020`,
  `SRC-021`, `SRC-022`, `SRC-084`) — VedaWeb distribution terms, per item;
- the metrical strata (`SRC-023`) — attributed CC-BY-4.0, compiled by Gunkel
  and Ryan (`PUR-013`), so the attribution must appear where the five period
  names appear;
- the Arnold 1905 page image (`SRC-026`, archive.org
  `vedicmetreinitsh00arnouoft`) — the book is out of copyright; the **scan** has
  its own terms and they must be read, not assumed;
- the three translations shown at `CP-1.2` (`SRC-072`, `SRC-073`, `SRC-074`) —
  Griffith 1890 and Grassmann 1876–7 are old; Geldner 1951 is not, and its
  status is the one to check first.

No asset may be shown to a child before its row exists. `U-7`.

---

## 11. The two adversarial tests

Run on this specification before it was committed, per constitution §8.

### 11.0 How this section was reached

The first version of this section tested two things — Arnold, and the
deflationary reading — and passed itself on both. An independent adversarial
pass then found eighteen findings, six of them severe, and **the two most
serious were failures of this section itself**: it examined Arnold and missed
the §7 category audit, which is `BF-017` word for word; and it never tested the
one conclusion that kept the specification alive, which is what `BF-025`'s
control exists to prevent. Both are repaired in the document above — §1.5 and
§2 — and both are recorded here rather than quietly absorbed.

`BF-025` `future_control`: *"Where a unit's conclusion rescues its own
deliverable, that conclusion is the one the adversarial pass starts with."*
This section now starts there.

### 11.1 The conclusion that rescues the deliverable

**The conclusion:** that §1.5's derivation returns Nocturnal Veḷi, where Field
Mode is available, rather than Reading Room, where §1.7 forbids it and this
specification is withdrawn.

**It did not survive.** §2 sets out the re-run in full. In summary: the first
draft counted *screens* where the framework says *load-bearing propositions*,
and read *"an absence or an unknown"* where the framework says *"typed
absences"* — and this document's own §5.2 says in terms that two of those four
absences are **not** typed. On the framework's wording rule 3 does not fire,
the derivation falls to rule 7, and rule 7 is the residual that §1.6.1 says is
not a posture finding at all.

**What this cost, and what it did not.** It cost the specification its own
answer: there is no derived posture to hand the owner, only two assignments and
an argument for each, both now in `D-055` and in `DECISIONS-NEEDED.md`. It did
not cost the specification its existence, because the derivation was always
advisory and the assignment was always editorial — which is the thing the first
draft should have said instead of manufacturing a result. `D-055`'s notes have
been rewritten to stop asserting the Nocturnal Veḷi derivation as fact.

No `BIAS-FAILURE-LOG` row is opened for it, because it is a method failure of
this unit caught before the unit was released and repaired in place, and the
framework tension it exposed is logged where it belongs, at
`04-AUDITS/INTERNAL-CONTRADICTIONS.csv` `IC-CP-001`.

### 11.2 Prestige-bias challenge

*Did this privilege a claim because it is canonical, Sanskritic, Brahmanical,
Indo-European, European, colonial, institutionally prestigious, repeatedly
cited or nationally useful?*

**Failure 1 — the category audit, which is `BF-017` repeated.** The first draft
of this section opened *"the real exposure is not the Sanskrit — it is Arnold"*
and went on to examine Arnold. That is `BF-017`'s finding verbatim: a unit that
applied constitution §7 rigorously somewhere else and skipped it on **fort**,
then ran a prestige-bias test that examined Arnold and missed the category audit
entirely. This document had put a failed gloss in its title and used it as an
unglossed default in every sentence, with `RA-013` `OPEN` on every occurrence of
the word and cited nowhere in the unit. Repaired at **§1.5**, which cites
`RA-013` and `BF-017`, states why the default is kept, puts the working title
into `D-057`, and requires every screen heading using the word to link to
`CP-3.6`.

**Failure 2 — Grassmann counted twice, in the child's favour.** `DEP-021` says
plainly that Grassmann's translation and the Grassmann dictionary are one
judgement expressed twice and *"must not be counted as an independent vote"*.
The first draft nevertheless told a child *"three grown-ups … did not all pick
the same words"* on a screen whose glosses came from one of the three, and put
*Burg* and *"Grassmann's own definition"* side by side on one card as if they
were two witnesses. Neither `DEP-021` nor `DEP-023` was cited anywhere.
Repaired at `CP-1.2` and `CP-3.6(d)`, both of which now carry the counting
caution in the child's own words.

**Failure 3 — the two non-Anglo-German witnesses were the ones cut.** `CP-1.2`
showed three translators where the register records four for that exact stanza,
and the one dropped was the Russian. `CP-3.6(d)` showed six English and German
words and omitted Renou's French and Elizarenkova's Russian, both of which
`PUR4J-022` records. That is not a neutral simplification: it is the two
non-Anglophone, non-German voices being trimmed for tidiness on a screen about
translation. Repaired at both.

**Held from the first draft, and still correct.** `CP-3.4` is built so that
Arnold's authority *decreases* across the screen — scheme, single source,
author's own hedge, second instrument, entanglement, absence of any year, and
the `MAYBE` on the assumption underneath. The screen's conclusion ceiling is
`MAYBE` and §1.3 forbids raising it. And `CP-1.1` shows no translation at all,
so the English arrives at `CP-1.2` as a choice rather than as the poem.

**One `BIAS-FAILURE-LOG` question, answered.** `BF-017`'s control names the
repair (cite the audit or state why the default is kept), and the repair is
made. Whether the recurrence itself warrants a fresh `BF-` row is the register
owner's call, not this unit's, and `RA-013` — already `OPEN` on every
occurrence of the word — is where this document's usage now falls to be
re-audited. It is named in `§1.5` so the connection is not lost.

### 11.3 Preferred-counter-narrative challenge

*Did this accept a claim too easily because it is Dravidian, Indigenous,
anti-colonial, anti-Brahmanical, subaltern, diffusionist or politically
corrective?*

**Yes, and the first draft's own answer to this question was where it hid.**
The comfortable investigation available here is: *the poem is just poetry, the
numbers are made up, the forts were never real.* The first draft said so, listed
four corrections, and was right about all four — and then committed a fifth
instance of the same bias in a place its own answer did not look.

**Failure 4 — a null reported as a finding, running toward the preferred
reading.** `CP-3.4(f)` told a child that the book-order instrument says *"no
difference at all"*, badged **FOUND**, and concluded *"our two ways of asking
disagree"*. `PUR-020` says the difference is **not significant** — a failure to
detect, not a detection of nothing — and `RA-002` is `OPEN` on exactly that
wording, raised by `BF-004`, whose control requires the point estimate, the
direction and **the power limitation** before a null may bear on a hypothesis.
The error made a null into a positive rival explanation, which constitution §6
forbids in terms, and it did so in the direction that made this screen's story
about Arnold stronger. Repaired at `CP-3.4(f)`, which now reports the point
estimate, its direction, the power limitation, and a badge of **WE DON'T KNOW**.

**Failure 5 — the wrong "we don't know", closing a question in the museum's
favour.** `CP-3.7` badged *"who held the forts"* as **WE DON'T KNOW ·
the poem doesn't say**. The poem is not silent — `PUR4J-030` records 22
patron-side and 22 opponent-side passages — and `PUR-027` says the passages were
never read for it. The correct line is *we haven't looked yet*, whose remedy is
a reading. The first draft had the specification failing its own §5.3 on the
screen §5.3 matters most, in the direction that made the museum's silence look
like the poem's. Repaired.

**Failure 6 — the museum asserting that somebody knows.** `CP-3.5` told a child
*"people have dug, lots of people, in lots of places"* and answered *"does that
mean nobody knows?"* with *"No"* — two positive statements about the world
outside this repository, on the one screen whose finding is that the museum has
read nothing about that world, with no source behind either. `HOLD-008` used the
same unsourced premises to argue its typing. Repaired at both: the screen now
says *"we can't tell you"*, and the hold's typing argument needs no premise
about what has been excavated.

**Corrections held from the first draft, and still correct.** `CP-3.1` offers no
completion of the form "the forts were made up"; `CP-3.6` ends on `PUR4J-I-03`'s
own `evidence_against` — 48 of 103 passages present a fort as a real object with
named holders; `CP-5.1` card 2 shows the museum's weakest position as weak,
including the test that came out against it; `CP-5.4` ends on *"not because the
poem is lying"*. `CP-3.1`'s balance card on `PUR4J-026` was added for the same
reason.

**The opposite temptation was also refused.** The `the-forts` headline —
*"Ninety-nine forts, in Indus country, three centuries too late"* — carries a
geography and a chronology, is rated Medium risk and *"Revise before release"*,
and has no source on record. This investigation neither repeats it nor rebuts it
to a child. It corrects only the part the registers settle: ninety-nine is not
the commonest count (`CP-3.1f`, `PUR4J-003`).

### 11.4 Findings this reading produced for other people's registers

- **`RA-022`** — `PUR4J-I-02`'s `evidence_for` still reads *"8 for one hundred"*
  after `PUR4J-003` was corrected to 9. No screen uses the stale figure;
  `CP-3.1f` takes 9 from `PUR4J-003`.
- **`RA-023`** — `SRC-026` in the access ledger is Arnold 1905, and several
  `púr-` register rows cite it for glosses from Grassmann's *Wörterbuch*, which
  `DEP-021` names as a distinct source. Locators remain re-findable, so no claim
  is unsupported; the identifier does not resolve to the work it names. This
  unit's manifest cites `SRC-069` for glosses pending the sweep.
- **`IC-CP-001`** — the §1.7 / §1.5 rule 7 / §1.6.1 composition described at §2.

### 11.5 What this section still has not tested

Stated because the first draft's failure was an untested conclusion, and
pretending the second draft has none would repeat it in a new place.

- **`pur-translation-standard.md` §§5, 8–11 and `rv01-reconciliation.md`
  §§2.3–2.6 were not re-audited line by line** for this unit. Several evidence
  rows locate to those briefs and were verified only against the register rows
  that cite them.
- **The `mk:qst:` nodes `CP-2.1` maps onto do not exist.** No register in this
  repository holds them, so that mapping is unverifiable as written and is a
  design proposition, not a citation.
- **No rights position was checked for any asset.** `U-7` and gate `G-4`.

---

## 12. What would change this specification

- **`D-055` answered as Reading Room** — the specification is withdrawn, not
  amended. §2.
- **`U-1` runs and an excavation source enters the ledger** — `CP-3.5` stops
  being an empty shelf, `CP-4.1`'s second sentence gains real completions, and
  the investigation acquires the ground half it currently does not have. This is
  the single change that would most alter the product.
- **`U-3` runs** — `CP-3.4`'s timeline could carry what an absolute date rests
  on, shown as an argument with its own status, rather than only the fact that
  the museum holds none. The screen would get longer and harder, not easier.
- **`U-2` runs and a second stratification instrument agrees with Arnold** —
  `PUR-028` could move off `HYPOTHESIS`, `CP-3.4`'s ceiling rises from `MAYBE`,
  and `CP-5.1` card 3 loses its second badge. If it *disagrees*, the screen gets
  stronger, not weaker: a third instrument disagreeing is better evidence about
  the instrument than two agreeing.
- **`HOLD-001` resolves toward including `puraṃdhi-`** — the corpus goes from
  106 to 156 tokens (`PUR-023`) and every count on `CP-3.1` changes. Field Bags
  holding the old numbers must show the change (§10.3).
- **A framework revision to §10.4.7** — would not licence R-01. The constraint
  binds the pattern, not the topic, and this specification treats it as
  non-negotiable regardless of later relaxation, per §10.4.7's own second
  constraint.

---

## 13. Note on placement and standing

`06-BRIEFS/childrens-pilot/` is created by this unit. `06-BRIEFS/` has no
assigned home in the `CLAUDE.md` layout table; `rv01-reconciliation.md` §9
records the same and the reasoning (reconciliation C-9: briefs are a product of
this repository; C-3: directories are created when the work that fills them
begins). If the owner prefers another home the move is cheap now.

**Status of this document.** A specification. Per constitution §15 and framework
§14.4: it is not an implemented page and must not be described as one. Every
design proposition here is `HYPOTHESIS`. Every claim about the corpus carries
the status of the register row it cites and promotes nothing. No retrieval was
performed and no ledger row was added.
