# MVP fifteen — page briefs

**Written:** 2026-09-08 · **revised:** 2026-09-09
**Unit type:** page briefs. One per page in the curatorial audit's MVP set.
Fifteen briefs, `01-index.md` to `15-the-archive.md`, in the workbook's rank
order. This README is the index and the shared-gate reference; it is not a
sixteenth brief.
**Built by:** `04-AUDITS/mvp-fifteen-briefs-build.py`.
**Inputs, read and reproduced at build time:** `mvp.csv`, `page-audit.csv`,
`asset-register.csv` and `environment-map.csv` from
`01-INHERITED/curatorial-audit-v1.1/` (`INHERITED-UNVERIFIED` without
exception); `03-REGISTERS/inherited-claims.csv`; and `03-REGISTERS/*.csv`
scanned for `supports_page`.
**Inputs quoted and checked, not reproduced:**
`13-PRODUCT-ARCHITECTURE/museum-framework.md` (every design proposition
`HYPOTHESIS`, per its own §14.4), `00-CONTROLLER/METHODOLOGY-CONSTITUTION.md`,
`SCHEMA.md`, `method-limits.csv`, `summary.csv`, `claim-risk.csv`,
`overlap-tensions.csv`, `02-SOURCES/access-ledger.csv`, `DECISIONS-NEEDED.md`,
`RESEARCH-QUEUE.md`, `CLAUDE.md` and `04-AUDITS/BIAS-FAILURE-LOG.csv`. The
generator makes **100 assertions** against those files and fails the build
if one does not hold — covering the §1.5 derivation rules *with their numbers*
(the briefs cite the numbers), the negative-evidence type names, and `SRC-052`'s
probe list and constraint.

Fourteen of the assertions are **pairing** checks rather than existence checks:
each brief prints one §1.1 posture row and one §1.7 mode row, composed from two
tables in the generator, and the composed row is asserted against the framework.
Asserting the framework's rows as loose strings would have let a swapped table
entry pass while six briefs printed the wrong row — which is what an earlier
version of this check did.

**What the check does and does not do.** It catches *drift* — a quoted fragment
edited or deleted in its source. It does not catch *misreading*: a fragment can
resolve while being attributed to the wrong speaker, given the wrong status, or
used to support something it does not say. One such case was found by review in
the first draft and corrected. The check narrows the space for silent error; it
does not close it, and no claim here rests on its having done so.
**Every count this directory *argues from* is derived at build time**, and the
scope of that sentence is narrower than the blanket claim two earlier builds made
— *"Every count in this directory is derived at build time. None is a typed
literal"* — which was false when written and is corrected rather than deleted
(`BF-029`). The workbook figures inside each brief's *What the workbook records
as observed* block are transcribed from `page-audit.csv` by hand and are not
checked by the build; so are the `IH-` claim texts in each evidence table. What is
derived is every count on which a finding rests: the register scan and its
statuses, the inherited-row total, the diagram sets, the `supports_page` values,
the quote total, and the two inbound-link figures §7 of `03-artifact-atlas.md`
compares. The inheritance's standing rule 14 is the rule here; stating a
compliance that is broader than the compliance achieved is itself a way of
breaking it.

**No retrieval was performed for this unit.** No row was added to
`02-SOURCES/access-ledger.csv`; no claim moved status; no domain was requested.
A brief is a statement of what a page would have to be and what it would have
to rest on. **None of it is public copy**, and no sentence in it may be lifted
onto a page.

---

## 0. Two standing controls this unit ran against

Recorded first because they bear on whether the unit should exist, and the
review that found them was right that citing D-032 ten times without quoting its
last sentence was a serious omission.

**`DECISIONS-NEEDED.md` D-032 ends:** *"Nothing in this repository acts on the
MVP set until this is answered."*

**`RESEARCH-QUEUE.md` lists *"Page and exhibit briefs"* under `## Not yet`.**

This unit was produced on the owner's instruction, given in the session of
2026-09-08. **That instruction is not registered as an owner decision and this
unit does not allocate one for it.** `CLAUDE.md` puts every owner decision taken
in this repository in `09-DECISIONS/OWNER-DECISIONS.csv`, and an instruction to
carry out a piece of work is not the same object as a standing decision that the
work may precede its queue position; treating it as one would put an
unverifiable authority into the decision namespace, which is what the `HD-01` to
`HD-20` convention exists to refuse. If the owner wants the placement settled
rather than the task done, that is a fresh `D-` and it has not been allocated
here.

**An earlier draft of this section argued that the instruction cleared the
queue's placement because `OWNER-DECISIONS.csv` D-008 makes queue ordering an
owner matter. That argument was withdrawn under review and is recorded rather
than deleted.** It failed three ways: D-008 governs the queue's *ordering below
its first item*, and `## Not yet` is a membership list, not a position; D-008's
own state is `BLOCKED`, so it is an unexercised slot and cannot be the authority
under which anything is permitted; and the instruction itself has no row anyone
can check. Replacing *not noticing two controls* with *clearing them by an
authority the repository cannot verify* would have been the worse failure of the
two.

So the unit rests on the boundary alone, drawn explicitly:

- These briefs **describe** the fifteen pages the workbook nominated and state
  what each would need. That is preparatory work, and it is what was asked for.
- They **do not act on the MVP set**: nothing here schedules a launch, approves
  a page, orders the work, assigns the release's shape, or assumes an answer to
  D-032. §3's retrieval-capability table is a statement about which sources are
  reachable, not a work order; §6 records the `before-the-indus` conflict and
  takes no position on it.
- Nothing here promotes a claim, because nothing here retrieved anything.

**And the boundary may not hold.** If the owner reads it as too fine — if
writing briefs for a set whose membership is undecided *is* acting on that set —
then the correct disposition is that this unit waits on D-032 with the rest.
Nothing here forecloses that reading; it is written down so the judgement can be
made rather than assumed, and the briefs are recoverable work either way, since
what they mostly record is what is *missing*. `RESEARCH-QUEUE.md` has been
amended to record the unit and its standing.

---

## 0.1 The two adversarial tests, run on this unit

Constitution §8 and `CLAUDE.md`: both tests before a unit is called finished,
logged whether or not they found anything, and *"running one is a failed test"*
(framework §3.11). Method failures are logged at
`04-AUDITS/BIAS-FAILURE-LOG.csv` `BF-018` to `BF-020`; re-audits at
`04-AUDITS/REAUDIT-QUEUE.csv` `RA-019`. Independent adversarial review was run on this
unit in successive rounds before it was called finished, and every round found
blocking defects; what they found is in those rows rather than quietly repaired.
The number of rounds is deliberately not stated here — it is a figure about this
unit that nothing derives, and standing rule 14 is what this unit has already
broken once.

**Prestige-bias challenge — did this unit privilege a claim because it is
canonical, Sanskritic, Brahmanical, Indo-European, European, colonial,
institutionally prestigious, repeatedly cited or nationally useful?**

Found: **yes, once, by omission.** The set cites the inheritance's correction
record repeatedly — `IH-051` (six headlines overstated *in the platform's own
direction*), `IH-012` (the Vedic caste-word claim corrected), standing rule 17 —
and initially cited none of the one logged case running the other way,
`IH-029`/R-09, where the handoff records that *"Claude's caution understated a
well-supported finding."* A correction record quoted only in the direction that
flatters the corrector is not a correction record. `IH-029` is now cited with its
R-09 note in `09-the-water-city.md` and in `07-keeladi.md`. Logged as `BF-018`.

Also found: the prestige-bias test was initially dismissed in one line on
`08-before-the-indus.md` (*"quiet here — the claim is not canonical"*) and never
run on the four pages where it bites — `the-other-laws` (dharmaśāstra),
`sound-changes` (Sanskrit's phoneme inventory as the reference point),
`the-water-city` (the canonical Indus urbanism literature) and `the-archive`
(Indology). Running it per page is `RA-019`; it is not closed by this unit.

**Preferred-counter-narrative challenge — did this unit accept a claim too
easily because it is Dravidian, Indigenous, anti-colonial, anti-Brahmanical,
subaltern, diffusionist or politically corrective?**

Found: **yes, once.** `07-keeladi.md` initially treated the page's
institutional-interference framing as a posture-derivation problem and a
right-of-reply problem, and never as a claim whose evidence might be thin.
Keeladi carries the strongest Tamil-nationalist valence in the set and was
receiving the least evidentiary pressure of the fifteen. The brief now runs the
test on the page explicitly, in three parts — the date, the interference
narrative, and the direction of correction. Logged as `BF-019`.

**Further failures, not bias failures but method failures of the same class,
found by the same reviews and logged with them (`BF-018`(b), `BF-020`):** the
unit stated its own diagram count from memory rather than deriving it, and
claimed to read two files at build time that its generator never opened — both
repaired, both recorded. And the first draft expanded *"Kenoyer et al. 1983"* —
the only form any source in this repository uses — into a full author list
supplied from model memory, in a brief whose subject is that the publication has
never been read. Bibliography from memory is the failure the inheritance rule
exists to prevent, and it is more dangerous than a wrong claim because it looks
sourced. Removed; the brief now states that obtaining the full citation is the
first act of the unit. Logged as `BF-018`'s second row.

**The asymmetry statement** (§11.2, required so the pair is not presented as
balanced): these two failure modes are symmetrical in form and asymmetrical in
power. The archives, the institutional positions, the citation counts and the
funding behind the canonical accounts on these fifteen subjects are not equal to
those behind the counter-accounts, and correcting a counter-narrative bias does
not restore a balance that never existed. Both were corrected; neither
correction implies the two bodies of scholarship start level.

---

## 0.2 What the second build changed, and what found it

The first build was committed on 2026-09-08. Between then and 2026-09-09
`03-REGISTERS/water-living-world-readiness.csv` was added to the repository on
another branch. It is the fifteenth register carrying a `supports_page` column,
and one of its rows, `WLW-001`, carries `supports_page = the-water-city` at
`VERIFIED`. *(That status is stated here as the historical fact it is — what
arrived on 2026-09-08, and the reason it mattered. §0.2's rule against typed
statuses governs the briefs' live readings, not this record of an event; a
draft applied it here and made the audit trail vaguer than the thing it
records.)*

The generator caught part of this by itself and missed the rest, and the split is
the argument for building briefs from a script rather than writing them out.

**The derived part self-corrected.** `09-the-water-city.md` §3's opening sentence
is composed from the scan, so on re-running it changed from *"No register row in
this repository names this page"* to a statement of the row it found. In the
other fourteen briefs the same sentence kept its shape and its register count
moved from 14 to 15; in `09-the-water-city.md` the count is no longer printed
there at all, because the sentence that carried it is the one the scan replaced.

**The fixed part did not.** Four passages of prose in every one of the fifteen
briefs asserted the scan's *result* rather than printing it — that no row in any
register names the slug, that nothing bearing on the page stands above
`INHERITED-UNVERIFIED`, that this *"is the same for all fifteen pages"*, and the
lowest-status line, which was a typed literal in all fifteen. Two more were in
this README: §2's *"zero rows naming any of the fifteen slugs"* and the table's
floor column.

**What was actually false, stated exactly.** For the fourteen unlinked slugs
those sentences remained true; a first draft of this section said all of them
went false at once, which is the same overstatement in the opposite direction.
What went false was the two `the-water-city` instances and, in every brief, the
quantifier — *"the same for all fifteen pages"* — which is the sentence that made
the error a directory-wide one rather than a page-level one. The failure is not
that the prose was wrong everywhere; it is that nothing in the build could tell
where it had gone wrong.

The repairs below came in three rounds. The first three items were the repair
pass; items 4 to 7 were forced by independent adversarial review of it (`BF-029`);
item 8 by a second review of that repair (`BF-030`). They are listed with what
each review found rather than folded in silently, because two of the three rounds
found that the previous round's own account of itself was wrong.

1. **The linkage finding is derived.** §2 above and each brief's §3 now compose
   their statement from the scan rather than asserting its result. A page with a
   linked row says so and reads the row; a page without one says that. §2 prints
   what the scan returned and stops: it does not summarise the readings, because
   a sentence generalising over them is the `BF-027` failure again, and a first
   version of it duly hard-coded *"in the one case on file"* beside a derived
   count that would eventually contradict it.
2. **The floor is derived and the rule for it is stated.** Each brief's *lowest
   status* line is now computed from the statuses actually present. It is not a
   sort — framework §3.2 forbids ordering `INHERITED-UNVERIFIED` against the six
   evidential statuses — so the floor is stated by rule: a row carrying
   `INHERITED-UNVERIFIED` has had no retrieval event behind it, so no set
   containing one stands above it. A page whose evidence contains no such row
   stops the build instead of publishing Python's `None` as a status, which is
   what a first version did.
3. **A linked row cannot be read by the generator, so it is not read by the
   generator.** A link records that someone tied a row to a page; what the row
   carries is a judgement. A page with a linked row must supply `linked_reading`
   and `linked_licenses_copy`, and the build fails without them. That is why a
   register row added on a later branch cannot silently change what a brief
   claims: it stops the build until a person writes down what it means. A row
   declared to license public copy also fails the build, because §1's account of
   why the step 14 slots are empty would no longer hold.

   A first version of this gate tested `page.get("linked_licenses_copy")`, which
   a missing key satisfies, so the second half of the gate this README advertised
   did not exist. Both fields are now required by presence. Every gate in the
   file also raises `SystemExit` rather than asserting: a bare `assert` vanishes
   under `python3 -O`, and a gate an interpreter flag can switch off is not one.
4. **The floor is not a two-rung ladder.** A first version of the derivation
   called every status that was not `INHERITED-UNVERIFIED` *"above the floor"* —
   which is the ordering framework §3.2 forbids, and which would have printed a
   `REJECTED` row as standing above one. The briefs now name the other statuses
   present without ranking them against the floor, and an unstatused linked row
   stops the build instead of being rendered as empty backticks.
5. **`03-artifact-atlas.md` §7 derives what it argues from.** The two
   inbound-link figures and their ordering, the `mvp.csv` and `page-audit.csv`
   cells, D-034's status, and whether `claim-risk.csv` holds a row for the page
   are all read at build time. A first draft of the section retyped every one of
   them and called 56 the highest inbound-link count in the set; it is the
   second, behind `enter`'s 113.
6. **`WLW-001` is quote-checked.** The build's 100 assertions guard quotations from
   the framework, the constitution and the workbook; the row this whole build
   exists to respond to was guarded by none, and it has already been amended once
   under review. Its claim text, its locator and its `notes` are now checked, and
   the *"14 registers"* / *"15 registers"* comparison in
   `09-the-water-city.md` §3 derives its second figure instead of typing it.
7. **Nothing is written until everything is built.** A gate firing halfway
   through the loop used to leave the directory half-regenerated and looking
   clean — for a directory whose entire claim is that its output is derived, the
   worst available failure state. Every brief is now composed before any file is
   opened for writing.
8. **A derived value that falsifies its own sentence stops the build.** Reading a
   value at build time is not enough if the sentence around it presumes a
   particular value: substituting D-034's live status into *"a settlement …
   against a decision that is `OPEN`"* produced *"a decision that is `ANSWERED`"*
   and built cleanly. `owner_decision` now takes the status the argument needs and
   `claim_risk_absent` halts if the row it argues from the absence of appears —
   the pattern `atlas_inbound` already used. The same review found the ranking
   language removed from `status_floor` surviving verbatim in the hand-written
   reading it prints, three false scan-result sentences still standing in this
   README after two sweeps that claimed to have removed them, and §0.2's own
   prestige-bias entry still carrying the misattribution the narrative eight lines
   above it had corrected — with one of its sentences made false by the previous
   repair. All are fixed above and marked where they stood.

9. **Every superlative over the workbook's columns has a check behind it.**
   `BF-028`'s own standing control had been applied to the one page under review
   when it was written; four more sat typed and unguarded in `01-index.md`,
   `02-enter.md`, `05-tinai.md`, `13-the-other-laws.md` and §6 of this README.
   All five now stop the build if the workbook moves under them, and each check
   names the brief that prints the claim.
10. **A section is emitted for every page whose source defines one.** The
   substitutions §7 of `03-artifact-atlas.md` takes are specific to that page,
   and a guard written to scope them was wrapped around the emission as well —
   which silently deleted `08-before-the-indus.md` §7, sixty-three lines
   recording owner decision D-032, and left four references in committed output
   pointing at nothing. The guard now covers the substitution only. This is the
   worst thing any round of this work has done: a repair that had spent three
   commits insisting that withdrawn text is recorded and never deleted removed a
   live record of an `OPEN` decision, and the round that did it logged five
   findings without noticing. `BF-031`; the class is `RA-025`.

**The direction of the failures is the finding of the third round.** `BF-029`
recorded a repair leaning toward leaving the launch order alone. `BF-030` records
the correction of it leaning the other way — §7 began preferring the arm that
changes the title, through an unhedged *"requires"* on a `HYPOTHESIS` proposition,
a launch condition smuggled into §5's gate 1, and a cost stated for two arms and
withheld from the third. That is what an overcorrection looks like when the author
is correcting their own overcorrection, and it is why the arms now each carry a
labelled cost.

`03-artifact-atlas.md` also gained the §7 the first build did not write. The
title-count conflict was raised in its §1 and then **answered in its §2**, which
wrote that §8.1's rule *"is the one that makes the page launchable at all"* and
that *"under that rule the Atlas ships before D-034 is answered."* That is a
settlement of an `OPEN` owner decision in the brief's own voice, and locating it
took a second review — a first draft of this section attributed it to §1 and §5,
neither of which resolves anything, which is why the first repair pass left the
strongest instance standing. §2 now withdraws the sentence and keeps it visible;
§7 disclaims §2 by name, records the conflict in the form
`08-before-the-indus.md` §7 uses, and sets out three arms without ranking them.

**What this did not change.** No retrieval was performed for the second build
either, no claim moved status, and no page gained support: `WLW-001` is
`VERIFIED` about the state of this repository's registers at a timestamp, not
about the past `the-water-city` describes. The finding the directory was written
under stands — no proposition any of the fifteen pages makes about the past is
supported by a register row — and it now stands on a derivation instead of on a
sentence.

The method failures are logged at `04-AUDITS/BIAS-FAILURE-LOG.csv` `BF-027`,
`BF-028` and `BF-029`. `BF-029` is the whole of the third list above: independent
adversarial review of the repair pass returned seven blocking findings, every one
a defect in the repair rather than in the work it repaired, and two of them ran
toward leaving the launch order and the framework's authority undisturbed.
`BF-027` and `BF-028` were corrected in place by that review — both had
miscounted, in rows about miscounting — and the corrections are marked inside the
rows. Re-audits: `RA-022` asks the same question of every document in the
repository that states a count or a coverage finding in prose; `RA-023` asks
whether any other gate in this repository's scripts is one only in the sense that
these two were.

### The two tests, re-run on the second build

Constitution §8 requires both before a unit is called finished, and *"running one
is a failed test"* (framework §3.11). §0.1 records them for the first build.

**Prestige-bias challenge.** Found: **yes, and it is why §7 of
`03-artifact-atlas.md` had to be written.** The prestige at work is internal.
`13-PRODUCT-ARCHITECTURE/museum-framework.md` is this repository's own
specification, it reads with the authority of a rule, and every design
proposition in it is `HYPOTHESIS` by its own §14.4. The first build let its §8.1
close the atlas title-count conflict — **§2** of that brief presented §8.1's
no-headline-count rule as *"the resolution that makes the page launchable at
all"* and concluded that *"under that rule the Atlas ships before D-034 is
answered"* — while D-034 sat `OPEN` in `09-DECISIONS/OWNER-DECISIONS.csv` with a
note saying in as many words that §8.1 neutralises the number without answering
it. A `HYPOTHESIS` document was allowed to settle an owner decision because it is
ours and it is well argued.

*This entry said §1 and §5 for two builds, and added that they were left
unchanged so the failing reading would stay visible. Both halves were wrong:
neither §1 nor §5 resolves anything, which is why the first repair pass missed
the sentence that did; and the third build then rewrote both of them, so the
claim that they were unchanged became false as well. Corrected here rather than
overwritten, because an audit-trail entry that quietly acquires the right answer
is not an audit trail. §2 now withdraws the sentence in place and keeps it
visible; §7 disclaims §2 by name.*

A second, smaller instance is `BF-028`: the arm of the conflict that would move
the page out of rank 3 was argued with an inflated cost — 56 inbound links called
the highest in the set when `enter` has 113 — which is the error a reader
attached to the existing launch order would make.

**Preferred-counter-narrative challenge.** Found: **yes, once, and it runs
against this unit's own product.** `WLW-001` arrived at `VERIFIED` — stated
here as the historical fact, per §0.2 — and its arrival
falsified the sentence this directory was built around: *"No page in the MVP set
has a single register row behind it."* The reading in `09-the-water-city.md` §3
lets the substance of that sentence stand — the row is about the registers, not
about the past; it is a timestamped probe; it and this brief are one source
rather than two. Each of those three is defensible and each of them is also
convenient, and the reading was written by the unit whose headline finding the
row threatened. That is the shape of motivated reading whether or not the reading
is right. It is recorded here rather than resolved by its author: what would
overturn it is a linked row whose subject is the past a page describes, carrying
a status other than `INHERITED-UNVERIFIED`, and the correct response to one would be to
rewrite §2 rather than to read it down. The scepticism this repository runs on is
not neutral when it is pointed at a claim that would cost the current unit its
result.

**A third finding, from the review rather than from either test.** `RA-019` is
open, `HIGH`, and its standing control is *"re-check whether any brief accepted a
workbook `Risk` rating as an evidentiary judgement rather than a scheduling
one."* This build added prose squarely inside that scope — §7 of
`03-artifact-atlas.md` argues about what the `Keep` and `Low` ratings can and
cannot settle — without running the control, and got the columns wrong in the
process. §1 now separates `Curatorial decision` from `Claim risk`, quotes each
layer's own limit from `method-limits.csv`, and marks the causal reading of `Low`
as an inference the brief cannot check. `RA-019` is not closed by this; adding
material to an open re-audit's class without running it is the failure worth
recording.

**The asymmetry statement** (§11.2): the two failures above are symmetrical in
form and asymmetrical in what they defend. The first defends an internal
specification's authority over an open owner decision; the second defends this
unit's own finding against a row that contradicted it. Neither is a bias about
the ancient world, and neither should be read as one — which is itself worth
stating, because a unit that runs both tests and reports only internal findings
may have run them only against itself. On the fifteen pages' *subjects* the tests
were not re-run in this build; `RA-019` still holds for the four pages where the
prestige test bites, and it is not closed here.

---

## 1. The fifteen

| # | Slug | Environment / posture | Decision | Risk | Lowest status of its evidence |
|---:|---|---|---|---|---|
| 1 | [`index`](01-index.md) | Nocturnal Veḷi — *not yet known* | `Revise` | `Medium` | `INHERITED-UNVERIFIED` |
| 2 | [`enter`](02-enter.md) | Tamil Retrofuture — *known against an official account* | `Revise` | `Medium` | `INHERITED-UNVERIFIED` |
| 3 | [`artifact-atlas`](03-artifact-atlas.md) | Living Signal Field — *known by relation* | `Keep` | `Low` | `INHERITED-UNVERIFIED` |
| 4 | [`veli`](04-veli.md) | Nocturnal Veḷi — *not yet known* | `Keep` | `Low` | `INHERITED-UNVERIFIED` |
| 5 | [`tinai`](05-tinai.md) | Living Tiṇai — *known through place and material* | `Keep` | `Low` | `INHERITED-UNVERIFIED` |
| 6 | [`the-ledger`](06-the-ledger.md) | Reading Room — *known by argument from sources* | `Keep` | `Low` | `INHERITED-UNVERIFIED` |
| 7 | [`keeladi`](07-keeladi.md) | Living Tiṇai — *known through place and material* | `Keep` | `Low` | `INHERITED-UNVERIFIED` |
| 8 | [`before-the-indus`](08-before-the-indus.md) | Nocturnal Veḷi — *not yet known* | `Hold` | `Critical` | `INHERITED-UNVERIFIED` |
| 9 | [`the-water-city`](09-the-water-city.md) | Living Tiṇai — *known through place and material* | `Keep` | `Low` | `INHERITED-UNVERIFIED` (+1 linked, `VERIFIED`) |
| 10 | [`kural`](10-kural.md) | Tamil Retrofuture — *known against an official account* | `Revise` | `Medium` | `INHERITED-UNVERIFIED` |
| 11 | [`sound-changes`](11-sound-changes.md) | Living Signal Field — *known by relation* | `Revise` | `Medium` | `INHERITED-UNVERIFIED` |
| 12 | [`the-languages-we-lost`](12-the-languages-we-lost.md) | Nocturnal Veḷi — *not yet known* | `Keep` | `Low` | `INHERITED-UNVERIFIED` |
| 13 | [`the-other-laws`](13-the-other-laws.md) | Tamil Retrofuture — *known against an official account* | `Split` | `Low` | `INHERITED-UNVERIFIED` |
| 14 | [`custody`](14-custody.md) | Extraction / Collection — *known but withheld* | `Keep` | `Medium` | `INHERITED-UNVERIFIED` |
| 15 | [`the-archive`](15-the-archive.md) | Extraction / Collection — *known but withheld* | `Revise` | `Medium` | `INHERITED-UNVERIFIED` |

---

## 2. The finding that applies across the fifteen

**1 of the fifteen has a register row recorded against it; the other 14 have none.**

A scan of every register in `03-REGISTERS/` carrying a `supports_page` column (15 files) returns rows for: `the-water-city` — `WLW-001` in `water-living-world-readiness.csv` (`VERIFIED`) (read in [`the-water-city`](09-the-water-city.md) §3). Every other slug returns zero. **A link is not support.** A link records that someone tied a row to a page; whether the row carries a proposition the page asserts is a judgement, and each linked page's brief makes it in its own §3 under the gate described in §0.2. This section prints what the scan returned and does not summarise those readings — a sentence generalising over them is the failure `BF-027` was logged for.

The 24 `supports_page` values actually in use are: `atlas layer`, `brahui`, `forts (proposed)`, `geography (proposed)`, `method`, `none — infrastructure`, `substrate (proposed)`, `the-killed.html`, `the-northwest-cousin.html`, `the-water-city`, `water-living-world`, `water-living-world §0.4`, `water-living-world §4.1`, `water-living-world §4.2`, `water-living-world §4.3`, `water-living-world §4.4`, `water-living-world §4.5`, `water-living-world §6.1`, `water-living-world §6.2`, `water-living-world §9`, `what-varna-meant.html`, `§4.4`, `§4.5`, `§8`.
`03-REGISTERS/inherited-claims.csv` holds 369 rows, all
`INHERITED-UNVERIFIED`, and **all 369 have an empty `supports_page`**.

**The scan's exclusion set, printed rather than implied** (`BF-017`'s standing
control on arguments from absence): 11 further CSVs in `03-REGISTERS/`
carry rows and **no `supports_page` column at all** — `CROSS-DOMAIN-BRIDGES.csv`, `HYPOTHESIS-ELIGIBILITY.csv`, `domain-e-cdial-attribution-stats.csv`, `domain-e-cdial-loan-candidates.csv`, `domain-e-evidence-mass.csv`, `domain-e-geography.csv`, `domain-e-hydronyms.csv`, `domain-e-hypothesis-eligibility.csv`, `domain-e-retroflex-residue.csv`, `rigveda-pur-family-occurrences.csv`, `rigveda-varna-occurrences.csv`. Some hold
claim rows: a page could in principle be supported by one of them and the scan
would not see it. It would still not be *recorded* as supporting the page, which
is what `CLAUDE.md`'s register format requires, so the finding stands — but it
stands on the column, not on an exhaustive reading of every row in the
repository.

Under `CLAUDE.md`'s register format, `supports_page` is what ties a claim to the
atlas entry or exhibit it feeds, and *"Evidence that supports nothing is not
collected."* Read the other way round, which is the way that matters here: on the
repository's own accounting, **no page in the launch set has a register row
recorded as supporting a proposition it makes about the past**. That is narrower
than the sentence two earlier builds printed here — *"the launch set is supported
by nothing"* — which appeared in three builds, stopped being true of every page when
`WLW-001` arrived, and is corrected rather than deleted (`BF-030`). What the scan above returned,
and what each linked page's §3 makes of it, is the record.

Three consequences, and they are the shape of the whole unit:

1. **The floor is the same on every page: `INHERITED-UNVERIFIED`.** Every row bearing on any of the fifteen carries `INHERITED-UNVERIFIED`, except the linked row(s) named in §2 above, which carry another status and are read in their pages' §3. A different status is not a higher one: framework §3.2 rules that these do not form a ladder, and the floor is stated by the rule that a row with no retrieval event behind it cannot be stood above.
   Where each brief names inherited rows, they are rows that *bear on* the page,
   not rows that support it.
2. **No public copy may be drafted for any of them.** Method step 14 draws public
   copy from accepted claims. There are none. Each brief therefore states its
   page's QUESTION and leaves the other six step-14 slots open with the reason.
3. **Every claim-specific diagram in the set is embargoed.** Framework §3.12:
   *"a derived asset may not be commissioned or published while the claim it
   depicts is `INHERITED-UNVERIFIED` or `HOLD`."* **5 of the fifteen** asset
   sets contain a `claim-specific diagram` — `index`, `enter`, `tinai`, `the-ledger`, `before-the-indus` — and all 5 are
   blocked. (The count is derived from `asset-register.csv` at build time, not
   typed; the other ten sets name a different derived asset, or none.) This is
   the framework resolving `SCHEMA.md` §4's finding 3 — 50 claim-specific
   diagrams scheduled by MVP priority, which is driven by low risk, i.e. by the
   pages least examined. Under §3.12 the diagram schedule is a function of the
   verification schedule and cannot invert it.

**And the workbook's `Risk` column is not a measure of truth.** `method-limits.csv`
states it: *"Risk means verification priority, not falsehood"*, and *"a visible
bibliography does not prove claim-level support or source quality."* Two of the
starkest cases sit in this set — `artifact-atlas`, rated `Low` on 88
bibliography entries against 8 words of prose, and `the-archive`, rated `Medium`
with 1 source entry under 5 tables.

---

## 3. What can actually be verified in this session

Of the fifteen units of work named in the briefs, **three have a live retrieval
route** with the access this session has. This is a statement about retrieval
capability, not a work order: sequencing the MVP set is what §0 says this unit
does not do.

| Unit | Page | Route | Ceiling |
|---|---|---|---|
| **MVP-U4** | `veli` | DEDR/JAMBU (`SRC-060`, `SRC-061`), Proto-Dravidian (`SRC-062`), DravLex (`SRC-067`) | `PROVISIONAL` — single digitisation lineage (§3.2) |
| **MVP-U12** | `the-languages-we-lost` | Glottolog CLDF and languoid tree (`SRC-050`, `SRC-051`) | `PROVISIONAL` — one aggregating classification |
| **MVP-U11** (lexical half only) | `sound-changes` | same Dravidian lexical lane | `PROVISIONAL`; epigraphic half blocked |

Two more need no retrieval at all and could be executed with the access this
session has: **MVP-U1** (threshold claim decomposition, `index`) and **MVP-U6**
(re-deriving the ledger rule in-repository, `the-ledger`), plus the structural
half of **MVP-U14** (creating the Obligations, Consent and Community Authority
registers).

**The rest are blocked, and the block is documented rather than assumed.**
`SRC-052` characterises the session's egress as `github.com` and
`raw.githubusercontent.com` only; `SRC-080` to `SRC-083` record GRETIL, the
Internet Archive, TITUS, sacred-texts and wisdomlib refused on re-probe at
2026-09-07T15:10Z. `SRC-027` records `indianculture.gov.in` reachable earlier the
same day, and `SRC-080`'s own note gives the rule that stops these being
reconciled by assertion: *"A ledger row is a timestamped probe, not a standing
property (D-042)."* A later characterisation does not supersede an earlier
probe of a host it never probed. So **re-probing is the first action of any unit
that needs a host**, and no brief here asserts that a host it has not probed is
unreachable. Hosts never probed at all — ASI, TNSDA, Indian publishers, the
publishers of Aktor and Davis — are recorded as untested, not as blocked.

**Two things escalate rather than block.** `IH-215` names an outreach to Dr. G.
Sundar of the Roja Muthiah Research Library as *"the most important single
verification task in the file"* and records that nothing has been sent to any of
the nine outreach roles. Institutional access is one of `CLAUDE.md`'s five
escalation categories: that is an owner action, not a `HOLD` row. The same
applies to the audited archive `veli-site(3).zip` itself, which is not in this
repository and has no ledger row — which is why every figure in the workbook is
`INHERITED-UNVERIFIED` rather than merely unchecked.

**`05-HOLDS/` rows are owed** for: the deployed build and the audited archive
(`enter`, `artifact-atlas`); the Tolkāppiyam *Poruḷatikāram* (`tinai`); Kenoyer
et al. 1983 and Chattopadhyaya 1996 (`before-the-indus`); the Keeladi report
chain (`keeladi`); the Indus excavation literature (`the-water-city`); a citable
Tirukkuṟaḷ edition if the git lane does not serve one (`kural`); a Tamil-Brahmi
epigraphic corpus (`sound-changes`); the isolate comparative literature
(`the-languages-we-lost`); Aktor and Davis (`the-other-laws`).

---

## 4. The shared gates

Every brief's §5 lists what its page needs **beyond** these. These apply to all
fifteen and are not repeated in the briefs.

### The workbook's release gates (`summary.csv`, `INHERITED-UNVERIFIED`)

1. Claim-level citation review
2. Cross-page consistency review
3. Image rights and provenance
4. Specialist/community review where relevant
5. Browser, accessibility and mobile testing
6. Prototype approval before migration
7. Confirm production domain and deployment allowlist

### The workbook's *Not completed* list (`method-limits.csv`)

Full primary-source re-performance · legal opinion · community consultation ·
image-rights clearance · discipline-specific peer review. The sheet is explicit
that *"these are publication gates, not optional polish."*

### Framework and constitution gates

| | Gate | Source |
|---|---|---|
| **F1** | Source Mode is reachable from the page | §1.7 — mandatory in all seven postures |
| **F2** | Every displayed claim is a Claim Object with a **computed** status; no editor can type `VERIFIED` and the CMS has no status dropdown | §3.1–§3.2 |
| **F3** | The posture is recorded in the Editorial Register with `derived_posture`, `assigned_posture` and, where they differ, a non-empty `override_reason` | §1.5, §11.5 — **this register does not exist** |
| **F4** | No derived asset is commissioned or published while the claim it depicts is `INHERITED-UNVERIFIED` or `HOLD` | §3.12 |
| **F5** | Both adversarial tests are run **as a pair** and logged whether or not they found anything, with the asymmetry statement | §3.11, §11.2, constitution §8 |
| **F6** | Every absence argument is typed under the negative-evidence standard | constitution §6 |
| **F7** | Every consequential ancient word carries a Translation Block | constitution §7, §3.8 |
| **F8** | Proportionality: allocated space is compared against evidential weight at review | §3.10, method step 9 |
| **F9** | Falsifiers are recorded for every load-bearing claim | §3.9, method step 12 |
| **F10** | Step 13 has been run — MelaKeela checked against itself for contradictions, outdated claims, duplicate pages and terminology drift | method step 13 |

### The repository-level gate

**R1.** At least one claim with `supports_page` naming the slug, carrying a
status other than `INHERITED-UNVERIFIED`, **whose subject is a proposition the
page makes about the past**. 1 of the fifteen has a row carrying a status other than `INHERITED-UNVERIFIED` — `the-water-city` — and that page's §3 records what its subject is. **No page in the set passes R1 today.**

*Three earlier builds stated R1 without its second clause and asserted that no
page passed it. As written then, `WLW-001` satisfied R1 — a mechanical test with a
typed verdict that the scan already contradicted (`BF-030`). The clause is what
the gate always meant; the brief's §3 is where it is applied, because whether a
row's subject is the page's past is a judgement and not a scan.*

---

## 5. Open owner decisions that block pages in this set

None of these is a research question and none can be closed by retrieval. They
are listed with the pages they block, not re-argued; the argument is in
`DECISIONS-NEEDED.md` and the authoritative status is in
`09-DECISIONS/OWNER-DECISIONS.csv`.

| Decision | Question | Blocks |
|---|---|---|
| **D-032** | Does `before-the-indus` launch, or come out of the MVP set? | `before-the-indus`; and the release's shape — see §6 |
| **D-033** | Which build is authoritative; is `rakhigarhi` live? | `enter`, `artifact-atlas`, `the-water-city` |
| **D-034** | The page count and the atlas site count | `index`, `enter`, `artifact-atlas` |
| **D-004** (`OWNER-DECISIONS.csv`) | What Veḷi principally is | `index`, `veli` |
| **D-006** (`OWNER-DECISIONS.csv`) | Keezhadi or an inscription as the children's pilot | `keeladi`, and Field Mode for `tinai` and `the-water-city` |
| **D-010** (`OWNER-DECISIONS.csv`) | Which institutional claims may presently be published | `keeladi`, `custody`, `the-archive`, `the-other-laws` |
| **D-015** | Is Reading Room a seventh peer posture or demoted to Source Mode? | `the-ledger` |
| **D-016** | May Reconnection surfaces publish before community-led work exists? | `custody`, `the-languages-we-lost` |
| **D-025** | Are refused and unanswered obligations published individually, in aggregate, or only with notice? | `custody`, `the-archive` |
| **D-029** | Does the institution assert fair dealing, and in which jurisdiction? | `kural`, `the-other-laws` |

**This unit raises no new `D-` identifier.** Everything it found was already
carried by an existing decision, which is the correct outcome: `CLAUDE.md`
allocates a new identifier from `OWNER-DECISIONS.csv`, never from the highest
number visible in a document, and a brief that manufactures decisions inflates
the namespace it is meant to read from.

---

## 6. The `before-the-indus` conflict, recorded and not resolved

`before-the-indus` is **MVP rank 8** in `mvp.csv`, `MVP = Yes` in
`page-audit.csv` and `Priority = MVP` in `asset-register.csv` — and in the same
sheets it is `Decision = Hold`, `Risk = Critical`, with the release dependency
*"Withhold from MVP until load-bearing claims receive claim-level citations and
specialist/editorial review."* It is the only one of the fifteen in this state
and the only Critical-risk page in the launch set.

It is already carried as **D-032** in `DECISIONS-NEEDED.md`, with a row in
`09-DECISIONS/OWNER-DECISIONS.csv`, raised 2026-09-07 and renumbered from D-004
the same day (`09-DECISIONS/DECISION-ID-MAP.csv`). Category: *two consequential
positions both remaining viable / publication approval*.

**This unit records the conflict and takes no position on it.** The full record,
including what each arm changes and what neither changes, is in
`08-before-the-indus.md` §7. Nothing elsewhere in these briefs assumes an
outcome: `09-the-water-city.md` notes that the *Meluhha and Indus* exhibit
sequence loses a second member under one arm, and states it conditionally.

---

*Written 2026-09-08. Every design statement here is `HYPOTHESIS`; everything drawn
from the curatorial audit is `INHERITED-UNVERIFIED`. Nothing in this directory is
public copy, and nothing in it promotes a claim — promotion requires a retrieval
event logged in `02-SOURCES/access-ledger.csv`, and this unit performed none.*
