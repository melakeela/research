# Decisions needed

The only place that asks anything of the owner. One decision per
section. Nothing here is actionable by an agent alone.

Qualifying categories:
- payment or institutional access required
- lawful acquisition of a source
- two consequential interpretive positions both remaining viable
- living-community consent
- publication approval

---

## D-001 — Widen the network egress allowlist

**Raised by:** queue item 1, source access audit, 2026-09-06
**Blocks:** every `VERIFIED` promotion in the programme

The environment's network egress proxy blocks archive.org,
indianculture.gov.in, GRETIL, jstor.org, arxiv.org, doi.org and
en.wikipedia.org. Only `api.github.com` is reachable. `WebSearch`
returns usable locators, but none of the URLs it returns can be
fetched, so no retrieval event can be recorded for any of them.

Under the rule in `README.md` that promotion requires a retrieval
event, this caps every claim in the programme at `HYPOTHESIS`.

**Decision:** which domains should be added to the environment's egress
allowlist? Suggested minimum for this programme:

| Domain | Why |
|---|---|
| `archive.org` | ASI reports, *Epigraphia Indica*, Digital Library of India |
| `indianculture.gov.in` | Ministry of Culture / National Virtual Library |
| `gretil.sub.uni-goettingen.de` | Sanskrit e-text corpus |
| `doi.org` | DOI resolution and citation verification |
| `arxiv.org` | full text behind Scholar Feed hits |

Egress policy is set on the environment, not in this repository, so
this cannot be changed from a session. See
https://code.claude.com/docs/en/cloud-environments

**Status update, 2026-09-07 — largely resolved by re-probe, not by action.**
Every domain in the table above except JSTOR now answers through the
proxy. Re-probed at 01:20 UTC and logged as `SRC-025`, `SRC-027`,
`SRC-028`, `SRC-029`, `SRC-030`, `SRC-031`, `SRC-032`, `SRC-033`:

| Domain | 2026-09-06 | 2026-09-07 |
|---|---|---|
| `archive.org` | blocked | **HTTP 200** — Arnold 1905 retrieved from it today |
| `gretil.sub.uni-goettingen.de` | blocked | **HTTP 200**, full index page |
| `indianculture.gov.in` | blocked | **HTTP 301**, host answers |
| `doi.org` | blocked | **HTTP 302**, resolver answers |
| `arxiv.org` | blocked | **HTTP 200** |
| `en.wikipedia.org` | blocked | **HTTP 200** (still not citable here) |
| `titus.uni-frankfurt.de` | not probed | **HTTP 200** |
| `www.jstor.org` | blocked | still blocked, 403 to CONNECT |

The earlier rows are marked `SUPERSEDED` rather than edited. The claim
in this decision that "only `api.github.com` is reachable" no longer
holds, and the cap it described — every claim in the programme stuck at
`HYPOTHESIS` for want of a retrieval channel — is lifted for everything
but the paywalled journal literature.

**What remains for the owner.** Only these are still refused at the
gateway, and only JSTOR is consequential:

| Domain | Consequence | Ledger |
|---|---|---|
| `www.jstor.org` | journal literature unreachable; this is the real remaining gap | `SRC-032` |
| `www.muktabodha.org` | Sanskrit e-text archive unreachable | `SRC-034` |
| `vedaweb.uni-koeln.de` | not blocking — the same data is on GitHub | `SRC-035` |
| `www.gutenberg.org` | not blocking — archive.org covers it | `SRC-036` |

JSTOR would in any case need an institutional subscription, so
allowlisting alone may not be enough; that part of the decision stands.

---

## D-002 — `CLAUDE.md`, `AGENTS.md` and `RESEARCH-QUEUE.md` do not exist

**Raised by:** queue item 1, 2026-09-06

`README.md` names `CLAUDE.md` as the operating controller, `AGENTS.md`
as its Codex mirror, and `RESEARCH-QUEUE.md` as the only backlog. None
of the three exists on any branch; the repository contained only
`README.md` before this change.

Queue item 1 was executed from the task description alone. Its scope was
taken to be "audit source access and produce the access ledger", which
matches the description given, but it was **not** read from the queue and
may not match what the queue intends.

These files were deliberately not authored in this pass. A research
constitution and a backlog are owner-level artifacts; drafting them from
an agent's guess would put unsourced content at the exact point in the
repository where the evidence rules are defined.

**Decision:** author `CLAUDE.md` and `RESEARCH-QUEUE.md` directly, or
commission them as an explicit task with their intended content stated.

**Resolved 2026-09-07.** The owner supplied the methodology directly. It is
committed unchanged as `00-CONTROLLER/METHODOLOGY-CONSTITUTION.md`;
`CLAUDE.md` was rewritten as the operating controller under it and
`RESEARCH-QUEUE.md` reseeded from its §4 and §11. `AGENTS.md` already
existed. The row is kept, not deleted, because the reasoning it records —
that a controller must not be drafted from an agent's guess — is what the
constitution now formalises.

---

## D-003 — Connector surface for this programme

**Raised by:** queue item 1, 2026-09-06

Of four connectors enabled in this chat, two are legal-research tools
with no bearing on ancient South Asia (a2aj, Descrybe — and Descrybe's
token has expired), one is quota-exhausted until 2026-10-01 (Scite), and
one works but covers only arXiv CS/AI (Scholar Feed, anonymous, no API
key attached).

Three installed connectors that are plausibly relevant are **not**
enabled in this chat and remain untested: **Consensus**, **Scholar
Gateway**, **alphaXiv**.

**Decision:** enable Consensus, Scholar Gateway and alphaXiv for this
project so their coverage can be probed and added to the ledger; and
confirm whether a Scholar Feed API key and a paid Scite tier are in
scope. Whether to keep the two legal connectors enabled is a separate
call — they cost tool surface and return nothing for this programme.

---


## D-014 — The 89-item v2 backlog and the prompt-pack are not in the repository

**Raised by:** controller amendment, 2026-09-07
**Blocks:** `06-BACKLOG/BACKLOG-COVERAGE.csv` entirely; owner decisions
D-008, D-009 and D-011; the R1–R19 half of the amended stage queue

`00-CONTROLLER/METHODOLOGY-CONSTITUTION.md` §10 declares the 89-item
"MelaKeela.com v2 — Master Research, Product & Institutional Backlog"
binding and requires one coverage row per item. §16 requires reading "every
file in the previously supplied prompt-pack ZIP". Neither document is in this
repository, on any branch, and neither was attached to the task that
installed the constitution. The only related material available is
`MELAKEELASITEREVIEWRUNNINGLIST.md`, a site review document that *references*
the prompt-pack by filename but does not contain it.

Eighty-nine coverage rows cannot be written from a document that is not
present. Reconstructing them from the running list's topic tables would
produce a complete-looking CSV with nothing behind it — the exact failure the
constitution's §1 names.

**Decision:** commit the two documents, or say they are superseded.

| Document | Needed for | Proposed location |
|---|---|---|
| MelaKeela.com v2 — Master Research, Product & Institutional Backlog (89 items) | §10, `BACKLOG-COVERAGE.csv`, D-008/D-009/D-011 | `06-BACKLOG/` |
| `MELA-KEELA-CLAUDE-FULL-SEQUENCE.md` | R1–R19 sequencing | `00-CONTROLLER/` |
| `MELA-KEELA-LANGUAGE-RESEARCH-PROMPTS.md` | R1–R19 packet definitions | `00-CONTROLLER/` |
| `MELA-KEELA-CLAUDE-LIVE-SITE-AUDIT-PROMPT.md` | the live-site audit that precedes the packets | `00-CONTROLLER/` |

A current route inventory for the live site is a fourth input, needed for
D-009 and for Step 13's self-contradiction check. The site lives in
`melakeela/site`, which this session cannot read.

### Update 2026-09-07 — site-review running list: delivery attempted, not received

A task dated 2026-09-07 (branch `claude/site-review-reconciliation-a624jt`)
instructed that **two versions of the site review running list** were attached,
to be committed unchanged to `01-INHERITED/site-review/` under their distinct
filenames, then reconciled against each other and mined for `LS-` and `COR-`
items.

**No files reached the session container.** Both attachment mount points
(`/mnt/attach`, `/mnt/user-data/uploads`) were empty; a filesystem-wide search
for `*MELAKEELA*`, `*RUNNINGLIST*` and `*RUNNING-LIST*` returned nothing; and
`git log --all --diff-filter=A` shows no such file added on any branch. The
files were named in the instruction but not transmitted with it.

Nothing was committed to `01-INHERITED/site-review/`, no
`RUNNING-LIST-RECONCILIATION.md` was written, and no `LS-`/`COR-` rows were
added to `03-REGISTERS/inherited-claims.csv`, which stands at 369 rows
(`IH-001`–`IH-369`). Reconstructing any of those three products from the
document titles alone would have produced exactly the complete-looking,
unsourced artefact this entry was opened to prevent.

Two things are nonetheless now on the record:

1. **The owner states the two site-review files are not the 89-item backlog.**
   Committing them would therefore not have closed the gap this entry names.
   `06-BACKLOG/BACKLOG-COVERAGE.csv` remains blocked, and owner decisions
   D-008, D-009 and D-011 remain blocked with it.
2. **The running list is intended for the repository**, at
   `01-INHERITED/site-review/`, in two distinct versions rather than one. This
   supersedes the singular `MELAKEELASITEREVIEWRUNNINGLIST.md` referred to in
   the body of this entry above; the reconciliation between the two versions
   is outstanding work, not a settled question.

**Decision unchanged, with one addition:** re-attach the two site-review
running-list versions so the delivery can be retried, *and* commit the four
documents in the table above, or say they are superseded. The backlog gap and
the running-list gap are separate; closing the second does not close the first.


## D-004 — `before-the-indus` is inside the MVP set and marked withhold-from-MVP

**Raised by:** curatorial audit v1.1 schema review, 2026-09-07
**Category:** two consequential positions both remaining viable / publication approval

In `01-INHERITED/curatorial-audit-v1.1/`, the page `before-the-indus`
("Before the Indus: Baghor Shrine and Mesolithic Sun Graves") is
simultaneously:

- `MVP` sheet, **rank 8 of 15**
- `page-audit.csv`, `MVP = Yes`
- `asset-register.csv`, `Priority = MVP`
- `page-audit.csv`, `Decision = Hold`, `Risk = Critical`
- `MVP` sheet, `Release dependency` = *"Withhold from MVP until
  load-bearing claims receive claim-level citations and
  specialist/editorial review."*

The row instructs the reader not to do what the sheet it appears on
does. It is the only one of the fifteen in this state, and the only
Critical-risk page in the launch set.

This is not resolvable by an agent: either the page is in the launch
and its Hold is overridden, or it is out and the MVP set is fourteen
pages with a gap at rank 8. Both are defensible curatorial positions
and the choice changes what launches.

**Decision:** does `before-the-indus` launch, or does it come out of
the MVP set? Nothing in this repository acts on the MVP set until this
is answered.

---

## D-005 — `rakhigarhi` is in the contradiction register but not in the audited build

**Raised by:** curatorial audit v1.1 schema review, 2026-09-07
**Category:** two consequential positions both remaining viable

`03-REGISTERS/inherited-claims.csv` row `IH-263` (contradiction X-14)
concerns the live `rakhigarhi` page: it asserts there is no seafaring in
the Rigveda while the site's own corpus file records `nau-` at n = 40.

`rakhigarhi` is **not among the 96 pages** in the audited baseline
`veli-site(3).zip` (supplied 2026-09-01). It appears nowhere in any
sheet of the workbook.

Three possibilities, and the repository cannot distinguish them without
the owner:

1. The frozen baseline predates the page.
2. The page was removed between the register's sources and the baseline.
3. The two artefacts describe different builds, in which case the
   audit's coverage of the live site is unknown.

This matters beyond one page: if (3), then "96 pages" does not describe
the site the contradiction register is talking about, and every count in
the workbook is scoped to a build no other artefact here references.

**Decision:** which build is authoritative, and is `rakhigarhi` live?

---

## D-006 — The audit's "96 pages" is a seventh page count, not a resolution

**Raised by:** curatorial audit v1.1 schema review, 2026-09-07
**Category:** two consequential positions both remaining viable

`03-REGISTERS/inherited-claims.csv` row `IH-251` (contradiction X-02)
records six page counts in circulation: 58, 69, 85, 102, 127 and ~135.

The workbook's baseline is **96**, which is not among them. The
workbook does not cite the dispute or claim to settle it.

Related, and with more exposure: `IH-250` (X-01) records the atlas site
count as disputed across 140 / 150 / 158 / 167→175 / 194 / 199. The
workbook adopts **175**, carries it in the page title *"Artifact Atlas:
175 Ancient South Asian Sites Mapped"*, places that page at **MVP rank
3**, and rates it `Keep` / `Low` risk with no Claim Risk row. A
contested number is inside a launch page title, presented as settled.

**Decision:** is 96 the authoritative page count, superseding the six on
file, or a seventh unreconciled value? And what is the atlas site count?
The atlas number is load-bearing for a page ranked third in the launch
set.


---

# Decisions raised by the museum framework specification

`13-PRODUCT-ARCHITECTURE/museum-framework.md`, 2026-09-07. Seventeen places
where constitution §12 or §13 leaves a choice the owner has not made. The
specification records them here rather than taking them, per the instruction
governing that task.

**Identifier-space note.** This file and `09-DECISIONS/OWNER-DECISIONS.csv`
already share IDs at D-004 to D-006 — a pre-existing collision. It is not
compounded here: these rows continue this file's own sequence from D-014.
Where a row below refers to a decision in the CSV, the CSV is named explicitly.

---

## D-015 — Is Reading Room a seventh posture, or the substrate?

**Raised by:** museum framework §1.6.1
**Category:** two consequential positions both remaining viable

The curatorial audit's environment scheme makes Reading Room the primary
environment for 34 of 96 pages *and* the secondary environment for all 96 —
a constant, which carries no information. The schema assessment's reading:
34 pages are Reading Room *"because the audit had nothing more specific to
say about them, and the residual category is the largest one."*

The framework splits the name: **Source Mode** is a universal display state
available in every posture, and **Reading Room** keeps a seat among the seven
only for exhibits whose content is argument from sources. That split is
mechanical and is specified either way.

What is not mechanical: whether Reading Room remains a seventh peer posture
at all.

| Option | Consequence |
|---|---|
| **Keep seven.** Reading Room stays a posture; Source Mode is added beside it | Methods, historiography and the ledger have a home posture. Risk: the residual habit returns, mitigated only by the `derived_residual` flag. |
| **Six postures.** Reading Room is wholly absorbed into Source Mode | No residual bucket exists, so unclassified exhibits have to be classified. Cost: long-form argument loses its own posture, and the institution's most common surface has no environment of its own. |

This is a claim the institution makes about its own self-description. It is
not derivable from the page inventory.

**Decision:** seven postures or six?

---

## D-016 — May Reconnection publish before consultation exists?

**Raised by:** museum framework §1.6.2
**Category:** living-community consent

The Environment Map's Reconnection row describes its prototype as *"Future
community-led work"* — unbuilt. Its one assigned page, `criminalised-today`,
is marked `Merge`, so executing the workbook's own recommendation empties the
only posture describing repair.

The framework's resolution re-backs Reconnection on registers rather than on
an essay corpus: custody and access status, right of reply, consent records,
withdrawal trail, community-authority statements, the correction ledger, and
an explicit record of what has *not* been repaired. Under that resolution the
posture is non-empty as soon as the institution publishes its first custody
chain or its first refused access request — none of which requires a
community to have been consulted first.

That is precisely the question. Publishing the institution's own account of
its obligations, before the parties to those obligations have been consulted,
is either (a) the honest first step, since the record of a refusal is a fact
about the institution and withholding it is self-serving, or (b) an
institution narrating a relationship it has not yet entered — which is what
the row's own `Avoid` warns against: *"Digitization is not restitution."*

**Decision:** may Reconnection surfaces publish before any community-led work
or consultation exists? If yes, with what stated caveat on the surface itself?

---

## D-017 — Does the institution state a restitution position?

**Raised by:** museum framework §1.6.2
**Category:** publication approval
**Related:** `09-DECISIONS/OWNER-DECISIONS.csv` D-010

*"Digitization is not restitution"* forecloses one claim without asserting
another. The framework publishes custody chains with their undocumented gaps
and publishes refused access requests; a visitor reaching those pages will
reasonably ask what the institution thinks should happen to the objects.

Three positions are available and all are defensible: state a restitution
position; state explicitly that the institution does not take one and why;
or say nothing. The third is the only one that cannot be done well by
default — §13.1 rule 3 holds that a stated "we could not do this well" is
preferred to silence where a visitor would expect an answer.

**Decision:** does the institution state a restitution position, and what is
it?

---

## D-018 — Is the 29-value `Type` vocabulary retired?

**Raised by:** museum framework §1.6.3
**Category:** two consequential positions both remaining viable

29 `Type` values against 7 environments, 32 of 96 pages typed
`research-essay`, 17 types used exactly once — and `Type` drives asset class,
so *"a taxonomy with 17 singleton values is doing production-planning work it
is too sparse to do reliably."*

The framework separates the three jobs `Type` was doing: production class is
rederived from the nine evidence classes the constitution's Step 4 already
requires; posture is derived from claim-set shape; genre survives as a label
with no downstream authority. The rederivation is specified. What remains is
what happens to the existing vocabulary on the site's own navigation.

| Option | Consequence |
|---|---|
| **Retire it** | Navigation is rebuilt on posture and evidence class. Cleanest; loses whatever the 29 labels encoded that nothing else does. |
| **Reduce to a genre facet** | Keeps the labels for search and browse, strips their authority over asset class and environment. Recommended by the framework, and the smallest change. |
| **Keep as-is** | The singleton problem persists and production planning keeps a key it cannot carry. |

**Decision:** retired, reduced to a genre facet, or kept?

---

## D-019 — Register CSVs: `object_id` column, or a crosswalk?

**Raised by:** museum framework §2.1
**Category:** two consequential positions both remaining viable

The identifier scheme addresses the existing registers rather than replacing
them: `mk:src:*` must resolve to a row in `02-SOURCES/access-ledger.csv`,
`mk:clm:*` to a row in `03-REGISTERS/`. Two ways to hold that join.

| Option | Consequence |
|---|---|
| **Add an `object_id` column** to the register CSVs | One place to look; the join cannot drift. Changes the register format `CLAUDE.md` specifies, so the controller would need amending. |
| **Maintain a separate crosswalk file** | Register format untouched. Two files to keep in step, which is how the constitution/CLAUDE.md dependency-store split already went wrong once (`OWNER-DECISIONS.csv` D-013). |

**Decision:** column or crosswalk?

---

## D-020 — External persistent identifiers?

**Raised by:** museum framework §5.3
**Category:** payment or institutional access required

The framework promises that a published identifier resolves forever (§2.1).
That promise is the institution's own to keep unless it registers external
persistent identifiers — DOI, ARK or Handle — which move part of the
guarantee to an infrastructure that outlives the site.

DOI registration requires a paying membership. ARK is free to use but
requires a registered naming authority and a resolver commitment. Handle
requires a prefix and an annual fee. All three interact with D-028
(succession).

**Decision:** does the institution register external persistent identifiers,
and which?

---

## D-021 — A guided sequence through the seven settings?

**Raised by:** museum framework §8.3
**Category:** two consequential positions both remaining viable

Constitution §13 lists seven settings the visitor should be able to move
through: steppe/Sintashta-related, Oxus/BMAC, Afghanistan and Helmand,
Balochistan and the Indus sphere, Punjab, Kuru regions, Gangetic.

The framework specifies free navigation and states that the interface must
not present the seven as an itinerary with an arrow, **because the itinerary
is itself the contested claim** — the order in which those settings are
listed is one of the most disputed propositions in the field, and rendering
it as a path asserts it in a visual grammar that carries no status field.

But a museum that offers eleven layers, seven settings and free movement, and
no route at all, will be used by very few people. A guided sequence is a real
service and it is also an argument.

| Option | Consequence |
|---|---|
| **Free navigation only** | Asserts nothing; risks being unusable to a non-specialist. |
| **A guided sequence, presented as a statused claim** | Usable, and the claim is visible and challengeable — the sequence itself gets an `mk:clm:` with sources, alternatives and falsifiers. |
| **Several guided sequences, one per rival account** | Most honest; most expensive; each needs its own evidence. |

**Decision:** free navigation only, one guided sequence, or several — and if
guided, what is the sequence claiming?

---

## D-022 — Atlas layer grouping and first-load defaults

**Raised by:** museum framework §8.4
**Category:** two consequential positions both remaining viable

The eleven layers are SOUNDS, WORDS, GRAMMAR, NEIGHBOURS, MATERIALS, RITUALS,
TEXTS, ANCESTRY, ARCHAEOLOGICAL CULTURES, POLITICAL CONTROL, UNKNOWN SPEECH
ZONES. The framework fixes one default: layer 11 cannot be switched off while
any language layer is on, since turning off the unknown while displaying the
known is how a language map becomes a claim about a continent.

Everything else about defaults is interpretive. What loads first is what most
visitors will see and many will never change. Grouping the layers — by
language / material / population / political, or otherwise — teaches a
taxonomy before the visitor has seen any evidence.

**Decision:** how are the eleven grouped for the visitor, and which are on at
first load?

---

## D-023 — Does the language mode animate?

**Raised by:** museum framework §8.5
**Category:** two consequential positions both remaining viable

Animated movement across a map is persuasive in a way a static comparison is
not, and the persuasion is not carried by any field in the record. The
framework permits animation only for transitions passing the ten-field check
of §13, and requires low-confidence and `proposed` transitions to be visually
distinguishable *while moving*, not only when clicked.

That is a mitigation, not an answer. The underlying choice — whether the
institution shows movement as motion at all, or as static compared states —
is interpretive.

**Decision:** animate, or present transitions as static compared states?

---

## D-024 — Is PROVE IT the correction intake?

**Raised by:** museum framework §9.1
**Category:** two consequential positions both remaining viable

§12 names PROVE IT without defining it. The framework reads it as the product
expression of constitution §2's requirement that the record stay capable of
contradicting *"MelaKeela's own pages, the owner's preferred hypothesis, and
your own previous answer"* — and therefore builds it as the public intake for
correction challenges: no score, the institution's own position disclosed
last, disagreement a first-class outcome that enters the correction pipeline
with the run attached.

If the owner intended something else — a guided demonstration of how a claim
was verified, say, or a credibility feature aimed at sceptical readers — then
§9 is the wrong specification and should be replaced rather than adjusted.
The two designs differ at the root: one must be able to conclude that the
institution is wrong, the other must not.

**Decision:** is PROVE IT the correction intake, or something else? If
something else, what is it for?

---

## D-025 — Publishing refused and unanswered obligations

**Raised by:** museum framework §11.1, §11.7
**Category:** two consequential positions both remaining viable

The Institutional Obligations Register's honest rows are its negative ones:
an access request sent to a collection and unanswered for two years is a fact
about that collection. Publishing it is also an act with consequences for the
relationship and for the next request — and the collections in question are
frequently the ones holding material the institution needs.

The same question governs §11.7's disclosure of attempts to influence
content.

| Option | Consequence |
|---|---|
| **Publish individually, in full** | Maximum accountability; likely cost in future access. |
| **Publish in aggregate** | "Eleven requests sent, four answered" — the pattern is visible, no counterparty is named. Weakest against a specific institution's specific refusal. |
| **Publish individually with prior notice** | The counterparty is told before publication and may respond first (§11.3). Slowest; probably fairest. |

**Decision:** which, and does the same rule apply to funders and to
collections?

---

## D-026 — Does the institution display human remains?

**Raised by:** museum framework §11.4
**Category:** living-community consent

The framework's standing default is non-display absent an explicit
community-authority position, and forbids remains in the children's
investigation as a puzzle in any case. Ancestry evidence (§2.4) requires
recording whether descendant communities were consulted, which means the
question arises for the genetic layer of the Atlas whether or not any image
is ever shown.

Three distinct sub-questions, which may have different answers: images of
remains; the display of ancestry data derived from remains; and the naming of
individuals or sites where remains were sampled.

**Decision:** does the institution display human remains, and under what
authority — and separately, how does it treat ancestry data derived from
them?

---

## D-027 — Challenge publication and challenger anonymity

**Raised by:** museum framework §11.6
**Category:** two consequential positions both remaining viable

Publishing challenges on receipt makes the pipeline visible and makes it
impossible for the institution to quietly bury an inconvenient one. It also
publishes unassessed assertions against the institution's claims, on the
institution's own surface, at whatever quality they arrive in.

Anonymity lowers the cost of challenging a well-defended position — which is
the case the whole correction mechanism exists for — and raises the volume of
bad-faith and automated submissions.

**Decision:** published on receipt or after assessment? Anonymous challenges
accepted, and if so under what handling?

---

## D-028 — Sunset and succession

**Raised by:** museum framework §11.7
**Category:** two consequential positions both remaining viable
**Related:** D-020

§2.1 promises published identifiers resolve forever and §11.4 promises
consent terms are honoured. An institution with no succession plan has made
promises it cannot keep, and the people most exposed are the ones who gave
consent on the strength of them.

Needs positions on: identifier resolution after the institution stops
operating; archival deposit of the evidence base and with whom; what happens
to consented material, whose consent was given to *this* institution and does
not automatically transfer; and what happens to the media rights.

**Decision:** what is the plan, and who holds it?

---

## D-029 — Does the institution assert fair dealing?

**Raised by:** museum framework §11.8.2
**Category:** lawful acquisition / legal exposure

`fair-dealing-asserted` is one of the eight `rights_status` values. Asserting
it is a legal position taken by the institution, in a named jurisdiction, on
a named ground — and it is the value that lets the institution publish
material it cannot clear.

The alternative is that the value is never used: everything published is
cleared, licensed, public-domain or consent-governed, and unclearable material
is represented by a rights placeholder stating what exists and why it is not
shown (§7.1).

This is a lawful-acquisition question and is outside what an agent may decide.

**Decision:** does the institution ever assert fair dealing, in which
jurisdiction, and on whose legal advice?

---

## D-030 — Licence on the evidence base

**Raised by:** museum framework §11.8.3
**Category:** publication approval

The framework requires two separately stated licences: an open one on the
evidence base — claims, statuses, locators, relationships, absences,
registers — because §5.1's argument is that people who distrust the
institution must be able to check it; and per-item terms on media, whose
rights and consent positions vary.

Which open licence the evidence base carries is unresolved. CC0 maximises
reuse and gives up the attribution that this project's provenance discipline
otherwise insists on. CC BY keeps attribution and adds friction for
aggregators. CC BY-SA keeps derivatives open and is incompatible with some
downstream uses. ODbL is built for databases, which this is.

Note the interaction with §11.4: consent-governed material does not travel
under the evidence-base licence unless its consent record says so, and the
licence must be stated to a consenting party *before* consent is given.

**Decision:** which licence on the evidence base?

---

## D-031 — Which languages does the institution commit to?

**Raised by:** museum framework §11.10.3
**Category:** two consequential positions both remaining viable
**Related:** `09-DECISIONS/OWNER-DECISIONS.csv` D-008 (Release 1 scope)

Tamil and English are presupposed by the project's own material. Beyond
those, each added language is a standing maintenance commitment under
§11.10.4: a version whose claims fall behind the source language publishes
superseded and rejected material under the institution's name, to the readers
least able to check it.

So the question is not which languages would be desirable. It is which the
institution can keep current, at what latency, and who maintains them.

**Decision:** which languages, with what maintenance commitment and whose?

---

## D-032 — Egress reach is not stable between sessions. Does domain E run under a GitHub-only policy?

**Raised by:** domain E source probe, 2026-09-07T02:19–02:21Z
**Category:** institutional access required
**Related:** `02-SOURCES/access-ledger.csv` SRC-037 … SRC-047,
`05-HOLDS/HOLD-002-dedr-unreachable.md`, `05-HOLDS/HOLD-003-para-munda-primary-statement.md`

At 2026-09-07T00:45Z and 01:20Z this repository recorded `archive.org`,
GRETIL, TITUS and Wikipedia as reachable, with byte counts (SRC-025,
SRC-028, SRC-033, SRC-029). At 02:19Z, in the next session, every one of
them answered 403 to CONNECT at the egress gateway, on both the `curl`
and the WebFetch channel. Fifteen non-GitHub hosts were probed and all
fifteen were refused; `github.com` over the git lane and
`raw.githubusercontent.com` were the only reachable destinations.

Nothing was withdrawn or changed by the sources. The session egress policy
narrowed. Two consequences the owner has to rule on:

1. **The ledger's meaning.** A row states reachability *at its probe
   timestamp*. It is not a standing property of the domain, and the earlier
   rows are not superseded — they were accurate. Every future unit that
   cites reachability must re-probe rather than inherit. This is now written
   into SRC-045; the owner should confirm it as the reading.

2. **Whether domain E can be run at all under this policy.** The domain is
   defined by the constitution as eleven distinctions among Dravidian, Munda
   and unidentified material. Distinctions 1–4 need a Dravidian etymological
   dictionary; distinctions 5–7 need Munda and Austroasiatic lexicography;
   distinctions 8–9 need Witzel's own published statement. None is on
   GitHub. Under a GitHub-only policy the domain's comparative half cannot
   be evidenced at any status above `HYPOTHESIS`.

| Option | Consequence |
|---|---|
| **Allowlist and re-run.** Add `dsal.uchicago.edu`, `archive.org`, `ejvs.laurasianacademy.com`, `sanskrit-lexicon.uni-koeln.de`, `titus.uni-frankfurt.de` | Domain E's comparative half becomes evidenceable. Cost: a second session on the same domain. |
| **Run the corpus-internal half only, as this unit did** | Yields verified measurement of the Rigvedic side and honest holds on the comparative side. Cost: the register stays open, and nothing about Dravidian or Munda donors is settled. |
| **Defer domain E entirely until access is granted** | Avoids a partial register. Cost: the corpus-internal measurements, which do not depend on the blocked sources, would be delayed for no evidentiary reason. |

This unit took the second option and says so in every affected row.

**Decision:** allowlist the five domains and re-run domain E's comparative
half, or accept the corpus-internal half as the domain's Release 1 state?
