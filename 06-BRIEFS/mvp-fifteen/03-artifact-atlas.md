# `artifact-atlas` — page brief

**Page:** *Artifact Atlas: 175 Ancient South Asian Sites Mapped* · MVP rank **3** of 15 · `Living Signal Field` · Decision `Keep` · Risk `Low`

**Written:** 2026-09-08 · **revised:** 2026-09-09
**Unit type:** page brief. A brief is a statement of what a page would have to
be and what it would have to rest on. It is **not public copy**, and no
sentence in it may be lifted onto a page.
**Status of this brief:** every design statement is `HYPOTHESIS`, inherited
from `13-PRODUCT-ARCHITECTURE/museum-framework.md`, whose own §14.4 puts every
design proposition it contains at `HYPOTHESIS`. Every statement drawn from
`01-INHERITED/curatorial-audit-v1.1/` is `INHERITED-UNVERIFIED`. No retrieval
was performed to write this brief and no row was added to
`02-SOURCES/access-ledger.csv`.
**Method:** `04-AUDITS/mvp-fifteen-briefs-build.py`; index and shared gates in
`06-BRIEFS/mvp-fifteen/README.md`.


---

## 1. The question, in step 14 form

**QUESTION.** Where was each of these objects found, how precisely is each findspot and date known, and which regions are unknown rather than empty?

### Why the remaining six slots are empty

Step 14 draws public copy **from accepted claims**. This page has none: §3 below records that every row bearing on it carries `INHERITED-UNVERIFIED` and no other status appears. Drafting
`WHAT THE EVIDENCE SUPPORTS` from claims at that standing would be writing public
copy for unverified claims, which is what `CLAUDE.md`'s inheritance rule and the
museum framework's Rule S-1 forbid. The slots are therefore left open, with the
work that would fill them named in §6.

| Step 14 slot | Draftable today | Why not |
|---|---|---|
| QUESTION | yes | stated above; a question asserts nothing |
| WHAT IS OBSERVED | partly | the workbook's structural counts are observations *about a page*, not about the past; the page's own observations are unretrieved |
| WHAT THE EVIDENCE SUPPORTS | no | no claim outside the `INHERITED-UNVERIFIED` floor |
| WHAT COMPLICATES IT | no | complications are claims too, and carry the same floor |
| WHAT REMAINS UNKNOWN | no | requires the negative-evidence typing of constitution §6, not yet performed |
| MELAKEELA'S CURRENT INTERPRETATION | no | an interpretation over an unverified claim set states confidence retrieval has not earned |
| WHAT WOULD CHANGE IT | no | falsifiers attach to claims; there are no claim rows to attach them to |


### What the workbook records as observed

**8 words of prose**, 88 estimated source entries, 0 external links, 0 tables, 2
inline SVGs, 56 inbound links. Type `atlas`. H1: *"Where the objects were
found."* Decision `Keep`, Risk **Low**, MVP rank 3.

The title asserts a number — *"175 Ancient South Asian Sites Mapped"* — and the
number is one side of an open contradiction. Framework §8.1 relays the schema
assessment's collision A, whose words these are — `INHERITED-UNVERIFIED`, quoted
inside a `HYPOTHESIS` document, and not the framework's own verdict: the count
was *"adopted as settled fact, put in a page title, and rated low-risk."*

**`Keep` and `Low` are two different columns produced by two different
instruments, and an earlier draft of this brief collapsed them.** `method-limits.csv`
gives *Curatorial decision* as *"Keep, Revise, Hold, Split or Merge based on role,
source visibility, risk and overlap"*, limited by *"Decisions remain provisional
until factual and specialist review."* It gives *Claim risk* separately, as
*"Flagged categorical, causal, priority/origin, institutional and quantitative
central claims"*, limited by the sentence one clause of `RA-019`'s
`what_to_recheck` puts a standing control on:
*"Risk means verification priority, not falsehood."* `Low` is therefore not a
judgement that the page is sound; it is a judgement that the page is not near the
front of the verification queue.

A third layer, *Source visibility*, was *"Estimated bibliography entries from
visible Sources/References sections and counted live external links."*, limited
by *"A visible bibliography does not prove claim-level support or source
quality."* The 88 entries belong to that layer. **Whether they are what
produced `Low` is an inference this brief cannot check** — the workbook nowhere
states how the two relate — and an earlier draft asserted it as fact in two
places. What can be said without inference is that 88 estimated entries
against 8 words of prose is a measurement of a page's furniture.

**And the workbook holds no row in which any instrument read the page's central
number.** That is an argument from absence over one document, so it is typed:
`claim-risk.csv` is the sheet whose method is *"Flagged categorical, causal,
priority/origin, institutional and quantitative central claims"* — a site count
in a title being the fifth of those five — and it holds no row for this page. The absence is `NOT PRODUCED` within the workbook's own scope, checked at
build time; it says nothing about whether the number was examined anywhere else,
and `IH-250` records that it was, in the inheritance, and left unresolved.


---

## 2. Environment and epistemic posture

**Environment:** `Living Signal Field`. **Posture — the visitor's relation to the knowledge:** *known by relation*. **`Avoid` — the failure this posture invites:** *"No gaming HUD or arbitrary links"*.

The workbook's own function and effect cells for this environment: function *"Relationships, movement, comparison"*, desired effect *"Connected evidence"*, palette role *"Midnight, cyan, sage, orange"* (`environment-map.csv`, `INHERITED-UNVERIFIED`).


### Modes available in this posture

| Posture | Source | Atlas | Investigation | Field | Classroom |
|---|---|---|---|---|---|
| Living Signal Field | mandatory | mandatory | available | available | available |

*(Framework §1.7.)*


### Derivation

**Derived posture: underivable today.** §1.5 derives a posture from the
exhibit's Claim Objects and its Absence records, in seven precedence steps. This
page has neither: no Claim Object exists for any proposition on it, and no
absence on it has been typed under constitution §6. Derivation therefore returns
nothing — not `Reading Room`, which is rule 7's residual and would be a false
output, since rule 7 fires on a claim set that has been examined and did not
match rules 1–6.

**Assigned posture: Living Signal Field, editorially, by the workbook.** That assignment is
`INHERITED-UNVERIFIED` and carries no override reason, because the register that
would hold one does not exist. `SCHEMA.md` §7: *"Nothing in `03-REGISTERS/`
records a publication decision, an environment assignment, or a duplication
finding."* Creating the Editorial Register — specified at §11.5 as
`03-REGISTERS/editorial-decisions.csv`, with `decision_type` including
`posture-assignment`, and with `value`, `derived_value`, `override_reason` and
`derived_residual` — is a prerequisite for this page, not a nicety: an
assignment with no derivation to disagree with cannot be audited.

*(Note for the framework's own re-audit: §1.5 names these fields
`derived_posture` / `assigned_posture` / `override_reason`, and §11.5 names them
`value` / `derived_value` / `override_reason` / `derived_residual`. The two
sections of the specification do not agree on the field names for the same
record. This brief follows §11.5, which is the section that defines the
register. Recorded, not resolved — it is a defect in the specification, not in
this page.)*

**Secondary environment.** The workbook gives this page `Reading Room` as
secondary — as it does for all 96. Framework §1.6.1 rules that a value constant
across every row is not a value: it is the single statement *"Source Mode
exists"*, and the column should be retired rather than migrated. This brief
treats the page's secondary environment as **Source Mode**, a universal display
state, not as a second posture.


**Atlas Mode is mandatory** (§1.7), and §8.7 lists eight things the Atlas may
never do. Four are at issue for this page, and only the first can be checked
here, because the build has not been retrieved:

1. *Show a total in its own voice* — the only one checkable from here, and it
   fails: the title in `page-audit.csv` states a count.
2. *Render an approximate location as a precise point* — the risk `IH-105`'s 145
   assumed rows create. Whether v1 in fact renders them as precise points is not
   knowable without the build.
3. *Render unknown as blank* — constitution §13 requires unknown regions to stay
   visibly unknown; a blank map *"reads as empty and empty reads as nobody."*
   Untestable from here.
4. *Let a filter silently drop the weak evidence to produce a cleaner picture.*
   Untestable from here.

§8.1 proposes a rule for the first of those four: **the Atlas has no headline
count.** A count is a claim with a status, an inclusion rule and a falsifier,
shown inside the Atlas with its status visible, or it is not shown.

**The first build of this brief wrote, here, that §8.1's rule "is the one that
makes the page launchable at all" and that "under that rule the Atlas ships
*before* D-034 is answered."** That reading is withdrawn and is recorded rather
than deleted, because it is the failure `BF-029` logs: a design proposition at
`HYPOTHESIS` in a specification this repository wrote was allowed to settle an
`OPEN` owner decision, and the sentence sat four sections away from the conflict
it was settling. `OWNER-DECISIONS.csv` D-034's own `notes` say what §8.1 does:
*"Neutralised but not answered by museum-framework.md §8.1 — the Atlas can be
built without the number and cannot be titled without it."* §7 records the
conflict; nothing in this section decides it.


---

## 3. The evidence it rests on

**No register row in this repository names this page.** A scan of all 15 registers in `03-REGISTERS/` carrying a `supports_page` column returns zero rows for `artifact-atlas` (`04-AUDITS/mvp-fifteen-briefs-build.py`, `scan_supports_page`). Under `CLAUDE.md`'s register format, `supports_page` is what ties a claim to the page it feeds — so on the repository's own accounting, this page is supported by nothing.


**Adjacency is not support.** Where verified work in this repository happens to
be *about subjects a page discusses*, it is still not *linked to that page*: no
row in any register carries `supports_page` naming this slug. Under framework §3.3 a
claim's status comes from its own Evidence Links, so a page cannot inherit
standing by sitting next to a register. Linking is an editorial act (§11.5) and
transfers nothing by itself; the page's propositions have to be written as Claim
Objects and evidenced in their own right.


What exists instead is inherited material that **bears on** this page without being linked to it. Every row below is from `03-REGISTERS/inherited-claims.csv`, whose 369 rows all carry `INHERITED-UNVERIFIED` and all carry an empty `supports_page`.


| claim_id | status | locator | what it bears on |
|---|---|---|---|
| `IH-105` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L230` | The atlas holds 194 site records, 315 class-windows and 14 classes, with **54 of 199 site-class rows dated from excavation reports and 145 marked assumed**. Three quarters of the dating is flagged as assumption inside the dataset itself. |
| `IH-250` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L474` | Contradiction X-01: 140 / 150 / 158 / 167→175 / 194 / 199 sites, and 299 against 315 windows. Recorded resolution path: *"Extract the atlas dataset to JSON, count, and generate every stated figure from it; until then no document prints a site count."* |
| `IH-057` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L158` | Correction C-37: three different counts on three live surfaces. |
| `IH-060` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L164` | Correction C-40: the owner's visual-concept document and VELI-03 disagree on sites and windows; the handoff blocks the prospectus on it. |
| `IH-201` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L382` | `/artifact-atlas` returns no text to a fetcher because it is JS-rendered. An atlas unreadable without JavaScript fails release gate 5 before any accessibility review begins. |
| `IH-002` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L10` | No count in the handoff was re-run against the atlas HTML. Every figure above is a report of a report. |


### Lowest status among them

**`INHERITED-UNVERIFIED`** — the status of every row above, and of every row that could be listed.


**On "lowest status".** `INHERITED-UNVERIFIED` is not the bottom rung of a
ladder. Framework §3.2: six of the seven statuses describe evidential standing
and one describes *where the assertion came from* — a prior model's summary of
its own conversation — so *"the interface must therefore never sort or
colour `INHERITED-UNVERIFIED` between `PROVISIONAL` and `HYPOTHESIS` as though
the statuses formed a single ladder."* The floor above is therefore stated by
rule rather than by sorting: a row carrying `INHERITED-UNVERIFIED` has had no
retrieval event behind it, so no set containing one stands above it. **Every row bearing on this page carries `INHERITED-UNVERIFIED`, and no other status appears.**
Where the handoff labelled a finding `VERIFIED` or `PROVISIONAL`, that label came
in with it and did not survive intake — `CLAUDE.md`, the inheritance rule.


---

## 4. Required asset class

From `01-INHERITED/curatorial-audit-v1.1/asset-register.csv`, verbatim (`INHERITED-UNVERIFIED`):


| Field | Value |
|---|---|
| Required asset set | verified dataset; accessible SVG/map; legend; mobile alternative; downloadable table |
| Documentary standard | Verified source, licence, credit, alt text, claim supported, date/place, manipulation disclosure |
| Priority | `MVP` |
| Source / commission route | To research |
| Status | `Needed` |


**How this class should be derived instead.** Framework §1.6.3(a) replaces genre-driven asset classes with a mapping from the exhibit's **evidence-class composition** — the constitution's step 4 inventory. The workbook derived this row from the page's `Type`, a 29-value vocabulary with 17 singletons that `SCHEMA.md` §3 finds *"too sparse to do reliably"* the production-planning work it is doing. Under §1.6.3(a) a page with no recorded evidence classes yields **no** production class, which is the correct output and is this page's actual state.


This is the one page of the fifteen whose asset set is not embargoed by §3.12 —
its assets are a dataset and its presentation, not diagrams derived from
individual claims. It is instead gated on the dataset existing as objects:
`verified dataset` presupposes Universal Evidence Objects with typed Place
Assertions and typed Date Assertions (§2.7, §2.8), and the 145 rows marked
*assumed* must each be typed rather than rendered. The `downloadable table` and
the exclusion export (§5.2) are the parts that make every absence argument on the
map checkable, and they are the parts most easily deferred.


---

## 5. What would have to be true before it can launch

Every page in the release carries the shared gates in
`06-BRIEFS/mvp-fifteen/README.md` §4 — the workbook's seven release gates, its
five *Not completed* publication gates, and the ten framework gates F1–F10. They
are not repeated here. What follows is what this page needs **beyond** them.

1. Whatever §8.1's rule is taken to require of this page — its own words are that the number in view is a property of the current filter, "always shown *with* the filter, never as a title", and the page's current title states a total. What follows from that is D-034's to settle and not this brief's: §7 records the conflict and the three arms without choosing one, and this gate states the rule rather than a launch condition derived from it.
2. Every mapped thing is an object with a status and an attestation mode; a findspot and an attributed provenance are never the same marker (§8.2).
3. The 145 `assumed` date rows are typed as assertions with their basis, or excluded. Rendering them identically to the 54 report-dated rows is `IH-105` published as if it were `IH-105` solved.
4. Unknown zones are a rendered layer, and the excavation/survey coverage overlay exists (§8.2) — without it no absence on the map is checkable.
5. The page renders without JavaScript, or has a documented equivalent (`IH-201`; release gate 5).
6. The exclusion set is exportable (§5.2).


---

## 6. What unit of work would verify it

**MVP-U3 — atlas dataset extraction and count derivation.** The unit is already
specified, by the inheritance itself: `IH-250`'s recorded resolution path is
*"Extract the atlas dataset to JSON, count, and generate every stated figure from
it; until then no document prints a site count."* The final clause was cut from
both of this brief's quotations of the row in an earlier draft, and it is the
only part of `IH-250` that constrains what this brief may itself print
(`BF-029`); §7 records where the constraint bites. Done properly it produces a register of site records with typed place and
date assertions, a dependency map for the 88 bibliography entries (framework §3.5
— 88 citations tracing to a handful of excavation reports count as a handful),
and a derived count with an inclusion rule.

**Blocked on one thing, and it is not egress.** The atlas data lives in
`artifact-atlas.html` inside `veli-site(3).zip`, supplied 2026-09-01. That archive
**is not in this repository** and has no access-ledger row — which is why the
whole workbook is `INHERITED-UNVERIFIED` rather than merely unverified. The
unblocking action is the owner supplying the archive, or naming the authoritative
build (D-033). Until then a `HOLD` row is owed, and this page cannot be the
release's connective heart on a dataset nobody here has opened.


---

## 7. The recorded conflict — a disputed count in the title, at rank 3 of the launch set

**This brief records the conflict and does not resolve it.** Three arms are set
out below because a conflict whose consequences are not stated is not legible;
none of them is preferred here, and no sentence in this section is to be read as
choosing one.

**What this section disclaims, by name.** §2 above wrote, in the first build,
that §8.1's no-headline-count rule *"is the one that makes the page launchable at
all"* and that *"under that rule the Atlas ships before D-034 is answered."* That
was a settlement, written in this brief's own voice, of a decision that is
`OPEN`. It is withdrawn in §2 and preserved there rather than deleted.

§5's first gate reads, in full, printed from the same string §5 prints:

> Whatever §8.1's rule is taken to require of this page — its own words are that the number in view is a property of the current filter, "always shown *with* the filter, never as a title", and the page's current title states a total. What follows from that is D-034's to settle and not this brief's: §7 records the conflict and the three arms without choosing one, and this gate states the rule rather than a launch condition derived from it.

That is a statement of the rule. It is not a launch condition derived from the
rule, and not a finding that D-034 has an answer.

The page's own title asserts a figure that this repository has logged as disputed
and has not closed, and the same workbook schedules the page third:

| File | Cell | Value |
|---|---|---|
| `page-audit.csv` | `Title` | *"Artifact Atlas: 175 Ancient South Asian Sites Mapped"* |
| `mvp.csv` | `Rank` | **3** of 15 |
| `mvp.csv` | `Decision` / `Risk` | `Keep` / **Low** |
| `mvp.csv` | `Release dependency` | *"Preserve the core argument; complete citation, image-rights, accessibility, and copy review before publication."* |
| `claim-risk.csv` | row for `artifact-atlas` | **none; the build stops if one appears** |
| `03-REGISTERS/inherited-claims.csv` `IH-250` | `INHERITED-UNVERIFIED` | contradiction X-01: 140 / 150 / 158 / 167→175 / 194 / 199 sites |
| `03-REGISTERS/inherited-claims.csv` `IH-057` | `INHERITED-UNVERIFIED` | correction C-37: three different counts on three live surfaces |
| `09-DECISIONS/OWNER-DECISIONS.csv` **D-034** | status | `OPEN` |

*(Every cell in that table is read from its file at build time. §7 of an earlier
draft retyped them, in a section written to remove typed literals — `BF-029`.)*

Rank 3 is not an ordering detail: it is the third page a visitor is
scheduled to meet, and on the current title it meets them with a number the
inheritance records as one of six competing values. Neither column that rated the
page reached that number. §1 above sets out why — `Decision` and `Risk` are
different instruments with different limits, `Risk` means verification priority
and not falsehood, and the `claim-risk.csv` sheet that would have recorded a
publication gate on a quantitative central claim holds no row for this page at
all — checked at build time, and this section will not build if one is added.

**This section prints the six competing counts, and `IH-250` says not to.** The
row's resolution path reads in full: *"Extract the atlas dataset to JSON, count,
and generate every stated figure from it; until then no document prints a site
count."* An earlier draft quoted that row twice and cut the final clause both
times. The clause is restored, and this section is inside its scope: what is
printed above is the *contradiction* — six values none of which is asserted as
the count — rather than a site count, and that is a reading of `IH-250`'s intent,
not a permission it grants. It is recorded here so that a reader who thinks the
row forbids this table can see that the question was noticed rather than avoided.

**Already raised, and not by this brief.** `DECISIONS-NEEDED.md` **D-034** —
renumbered from D-006 on 2026-09-07 (`09-DECISIONS/DECISION-ID-MAP.csv`) — states
it: *"A contested number is inside a launch page title, presented as settled,"*
and *"The atlas number is load-bearing for a page ranked third in the launch
set."* This brief adds no identifier and takes no position; it records that the
conflict survives into the brief set and names what each arm would change.

**What changes under each arm.** Three arms, each given the same three lines and
no others — what it does, what of D-034 it settles, and what it costs. The
structure is fixed because the alternative is tuning: this section's balance has
been found wrong twice, in opposite directions, and both times the asymmetry was
in what one arm's prose was allowed to carry that another's was not (`BF-029`,
`BF-030`). They are in no order of preference and each is reachable without the
other two.

**Arm 1 — the number is settled.**
- *Does:* the dataset is extracted and counted (§6, MVP-U3); X-01 closes.
- *Settles of D-034:* the atlas-count half — the value the decision asks for.
  Not the page-count half. Not what the title then says: §8.1 as read below
  forbids a number in a title under any circumstances, so a settled count makes
  the title question answerable without answering it.
- *Costs:* it is the only arm that waits on the archive (below). The count then
  has to be published as a claim with a status and an inclusion rule, and if the
  title changes with it, the Editorial Register problem below applies here too.

**Arm 2 — the title is changed, the number left open.**
- *Does:* the title drops the figure; the page ships at rank 3 with no total
  in its own voice.
- *Settles of D-034:* neither half. The atlas count stays `OPEN` and unanswered
  rather than resolved, and the page-count half is untouched.
- *Costs:* the Editorial Register that §11.5 specifies to hold *"a publication
  decision, an environment assignment or a duplication finding"* does not exist,
  and §2's finding applies unchanged — *"an assignment with no derivation to
  disagree with cannot be audited."*

**Arm 3 — the rank is changed.**
- *Does:* the page moves out of the first three; the release opens on something
  whose central claim is not an unsettled number.
- *Settles of D-034:* neither half. Both stay `OPEN`, and the title is
  untouched.
- *Costs:* `page-audit.csv` records **56 inbound links** to this page, the
  second count among the fifteen behind `enter`'s 113, so
  demoting it changes the site's link structure and not only an order. The
  Editorial Register problem in arm 2 applies here too.

**One thing all three arms share, and it does not decide between them.** The
count itself cannot be derived here: §6 records that the atlas data lives in
`artifact-atlas.html` inside `veli-site(3).zip`, which is not committed to this
repository and has no `02-SOURCES/access-ledger.csv` row. Under `CLAUDE.md`'s
negative-evidence standard that absence types as **`NOT ACCESSIBLE`** — the
evidence exists, was produced, is known to be held by the owner, and is simply
not here — and not as `NOT PRODUCED`, `NOT PRESERVED` or `ABSENT DESPITE ADEQUATE
SEARCH`. `01-INHERITED/site-review/` holds two inherited running-list documents
that have not been searched for atlas site records, so even the `NOT ACCESSIBLE`
typing is provisional on that search.

That is an access fact, not an evidential one, and it bears on the first arm
only. The second and third arms are editorial decisions about a title and an
order; neither needs the count, and treating them as blocked behind it would
convert a missing archive into a reason to leave the launch order as it is. An
earlier draft of this section did exactly that, closing with *"the title question
is blocked behind the count question"* — which eliminated the second arm by fiat
and left the status quo as the only reading. Withdrawn, and recorded rather than
deleted.

**What §8.1 reaches, read exactly.** A draft of this section said *"§8.1 does not
reach the title at all"*. It does. **§8.1's rule ends** — the section itself
continues past it — "The number of sites in view is a property of the current
filter and is always shown *with* the filter, never as a title." The emphasis on
*with* is the source's and is reproduced because this block claims to read the
rule exactly; a draft dropped it to avoid nesting italics. The rule reaches the
title directly, and the current title breaks it. Three things follow, and none of
them closes D-034.

- The second arm is what §8.1 **would require if the specification were
  adopted** — not an alternative to the rule, and not something the rule can
  compel. §8.1 is a design proposition at `HYPOTHESIS` (framework §14.4). A
  proposition at that standing does not amend a `page-audit.csv` field or
  overrule the workbook's rank, and adopting the specification is itself an owner
  act nobody has recorded. An earlier draft of this bullet wrote *"is what §8.1
  requires"*, which is the same category error §2's withdrawn sentence made,
  pointed at a different arm.
- Even fully adopted, §8.1 would settle only where a number may appear. It says
  nothing about what the number is, which is the half of D-034 the first arm
  addresses and the second does not.
- The framework's own paragraph after the rule reads *"the Atlas can be built and
  shipped before that is answered, because it never asserts a total in its own
  voice"* — which is the sentence §2 of this brief adopted and has withdrawn.
  D-034's `notes` put the same fact the other way round: *"the Atlas can be built
  without the number and cannot be titled without it."* Both are true and neither
  is a count.


---

*Brief written 2026-09-08, revised 2026-09-09. Nothing in it is public copy. Nothing in it promotes a claim: promotion requires a retrieval event logged in `02-SOURCES/access-ledger.csv`, and this unit performed none.*
