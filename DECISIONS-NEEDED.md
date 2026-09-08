# Decisions needed

The prose case for the owner decisions that **block work in progress**.
One decision per section. Nothing here is actionable by an agent alone.

Qualifying categories:
- payment or institutional access required
- lawful acquisition of a source
- two consequential interpretive positions both remaining viable
- living-community consent
- publication approval

## Identifiers

`09-DECISIONS/OWNER-DECISIONS.csv` is **authoritative** for the decision-ID
namespace and for each decision's `status`. Every `D-` identifier in this
repository is allocated there, including every decision written up below;
this file allocates none of its own. A new escalation takes the next free
`D-` from the CSV, gets a row there with `detail_ref` pointing back at its
section here, and is then written up.

Where the two disagree on wording or status, the CSV governs. What the CSV
cannot hold — the argument, the options table, the evidence a decision turns
on — lives here and is not duplicated into the CSV.

`DECISIONS-NEEDED.md` and `OWNER-DECISIONS.csv` shared IDs at D-004, D-005
and D-006 until 2026-09-07. The three sections in this file were renumbered
to D-032, D-033 and D-034; the CSV rows kept their numbers, because
`OWNER-DECISIONS.csv` D-004 to D-011 map one-to-one onto
`METHODOLOGY-CONSTITUTION.md` §14 bullets 1 to 8. Every old identifier and
its replacement is recorded in `09-DECISIONS/DECISION-ID-MAP.csv`, which is
how a `D-` reference in a document written before that date is resolved.

A second collision was cleared on 2026-09-07. `DECISIONS-NEEDED.md` briefly
carried two `## D-032` sections: the `before-the-indus` question, which owns
that identifier in the CSV, and a domain E egress ruling written in the same
window as the renumbering. The egress section is now **D-042**. Five further
decisions raised on the domain E branch — two written up here as `D-015` and
`D-016`, three carried only as CSV rows at `D-017` to `D-019` — had taken the
highest number visible in the file being written rather than the next free one
from the CSV; they are now **D-043** and **D-038** to **D-041**. Every move is
in `09-DECISIONS/DECISION-ID-MAP.csv`, and the identifiers already on `main`
did not move. The egress section moved a third time when `main`
merged PR #18 and allocated `D-036` to the mandated-registers question: it is
now **D-042**, the next free identifier above `main`'s highest, and `main`'s
`D-036` is untouched.

A third collision was cleared on 2026-09-07, when `main` merged PR #17 and
allocated `D-037` to the question of which section of
`MELA-KEELA-WHO-MADE-THE-PAST.md` carries the racialization-of-"Aryan"
programme. The substrate-literature egress-allowlist section, which this
branch held at `D-037`, is now **D-043**: `D-038` to `D-042` stand above
`main`'s highest but are already held by this branch's own rows, so `D-043`
is the next free identifier. `main`'s `D-037` is untouched, and the move is
recorded in `09-DECISIONS/DECISION-ID-MAP.csv`, keyed by branch.

A third series exists and is not part of this namespace. The inherited handoff
numbered its own owner decisions `D-01` to `D-20`; those are now written
`HD-01` to `HD-20`, they stay `INHERITED-UNVERIFIED`, and they are never
escalated here. Nothing in this file is an `HD-` decision.

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

**Second status update, 2026-09-07T03:03–03:12Z — the reopening did not
hold.** Re-probed during the domain M Brahui unit and logged as `SRC-052`.
Every host below now returns 403 at CONNECT. Only `github.com` and
`raw.githubusercontent.com` answer.

| Domain | 02:19 UTC | 03:03 UTC | Consequence |
|---|---|---|---|
| `archive.org` | 200 | **403** | scans unreachable again |
| `doi.org` | 302 | **403** | no citation verification |
| `arxiv.org` | 200 | **403** | no preprint full text |
| `glottolog.org` | not probed | **403** | reached via GitHub instead |
| `dsal.uchicago.edu` | 403 | 403 | DEDR still unreachable, `HOLD-002` |
| `api.github.com` | 200 | **403** | git over https still works |
| `api.crossref.org` | not probed | **403** | no bibliographic verification |
| `api.openalex.org` | not probed | **403** | " |
| `api.semanticscholar.org` | not probed | **403** | " |
| `zenodo.org` | not probed | **403** | dataset DOIs unresolvable |
| `royalsocietypublishing.org` | not probed | **403** | source paper unreadable |
| `pmc.ncbi.nlm.nih.gov`, `europepmc.org` | not probed | **403** | " |
| `www.degruyter.com`, `benjamins.com` | not probed | **403** | linguistics presses |

Three things follow, and the second is the one that matters for how this
file is read.

1. **The gap is wider than JSTOR.** The paragraph above says JSTOR is "the
   real remaining gap." At 03:03 UTC that is no longer true: the whole
   scholarly web is refused, and the domains added to the request are
   Crossref, OpenAlex, Semantic Scholar, Zenodo, `glottolog.org`,
   `royalsocietypublishing.org` and the PMC hosts.
2. **Reachability rows in the ledger are perishable.** Egress state changed
   twice in one day, in both directions. `RA-003` already queues `SRC-025`
   and `SRC-027`–`SRC-036` for re-audit on these grounds; that queue entry
   should be read as covering `SRC-045` and the first status update above
   as well. No unit may cite a reachability row as evidence that a source is
   *currently* obtainable without re-probing.
3. **GitHub is doing real work.** The domain M unit was completed anyway,
   because `lexibank/dravlex` and `glottolog/glottolog` are on GitHub
   (`SRC-049`, `SRC-051`). That is a narrow escape and not a substitute:
   what GitHub yields is datasets and bibliographic records, never a page
   of a book. `HOLD-004` is the direct cost.

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

### Update 2026-09-07 — the backlog is recovered in title form; the text is not

The 89 numbered item titles, their thirteen section headings and the six
unnumbered programme names were recovered from a ChatGPT conversation and are
committed unchanged at `06-BACKLOG/BACKLOG-v2-ITEMS.md`. They enter
`INHERITED-UNVERIFIED`. `06-BACKLOG/BACKLOG-COVERAGE.csv` now exists, with 95
rows on the column set §10 specifies — items 1–89 plus the six programmes,
which the original leaves unnumbered between items 65 and 66 and which the CSV
keeps in that position.

**What is now closed:** the row-allocation half. Eighty-nine coverage rows can
no longer be said to be unwritable for want of a list, and the body of this
entry above — "eighty-nine coverage rows cannot be written from a document
that is not present" — no longer describes the situation for `backlog_id` and
`title`.

**What is not closed, and why this entry stays OPEN:**

1. **The full original text of every item is still outstanding.** What was
   recovered is a title list. A title is not a specification. "WATER",
   "OBJECT", "FIELD", "PROVE IT", "Revision history" and "Layered depth" do
   not state their own scope, gate or deliverable. Seven columns of
   `BACKLOG-COVERAGE.csv` — `research_required`, `product_spec_required`,
   `technical_dependency`, `institutional_dependency`,
   `proposed_destination`, `release`, `final_zip_location` — are empty for
   that reason and cannot be filled by inference from a one-line title.

2. **A second document arrived in the same recovery and is not that text.**
   `06-BACKLOG/EXPANSION-PROMPT-2026-09-07.md` is a ChatGPT expansion and
   execution prompt dated 7 September 2026. It carries per-item prose under
   "Inherited work", "Build out" and "Gate", written from prior conversation
   context with no retrieval. It is committed separately, not merged into the
   items file, and its header says plainly that it is a model's
   reconstruction. Reading it as the recovered original would be precisely
   the substitution this entry was opened to prevent, and it is the more
   dangerous version of that failure because it *looks* like the missing
   text. Nothing in it promotes a claim, closes a decision or authorises
   work. Its "Execution sequence" and "Required deliverables" sections are
   proposals recovered from a chat, not instructions this repository has
   accepted.

3. **The route inventory is still missing, and now blocks two named
   columns.** `06-BRIEFS/SITE-INVENTORY.md` does not exist on any branch, and
   no other current route list is in the repository. `current_site_coverage`
   and `existing_route` therefore carry an explicit `NOT ESTABLISHED` marker
   in all 95 rows. Three substitutes were considered and rejected — the
   frozen 2026-09-01 curatorial-audit baseline (D-033 leaves open whether it
   describes the live build), the registers' `supports_page` values (almost
   all marked *proposed*; the one live page named anywhere in them is
   `the-killed.html`, which nothing maps to a backlog item), and the handoff
   counts (`INHERITED-UNVERIFIED` and mutually contradictory, per `IH-104`,
   `IH-250`, `IH-251`). The reasoning is in `06-BACKLOG/README.md`.

**Decision, restated:** supply the **full original text** of the 89-item
backlog, or declare the title list sufficient and the text superseded. Supply
`06-BRIEFS/SITE-INVENTORY.md` or a current route list; that alone regenerates
two of the four unpopulated column groups without touching anything else.
D-008, D-009 and D-011 remain blocked, because a release cannot be scoped from
titles alone.


# Decisions raised by the curatorial audit v1.1 schema review

`01-INHERITED/curatorial-audit-v1.1/`, 2026-09-07. These three sections were
raised as D-004, D-005 and D-006 in this file and were renumbered on
2026-09-07 to clear the collision with `09-DECISIONS/OWNER-DECISIONS.csv`.
`09-DECISIONS/DECISION-ID-MAP.csv` carries the mapping.

---

## D-032 — `before-the-indus` is inside the MVP set and marked withhold-from-MVP

**Renumbered from D-004** on 2026-09-07 (`09-DECISIONS/DECISION-ID-MAP.csv`).

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

## D-033 — `rakhigarhi` is in the contradiction register but not in the audited build

**Renumbered from D-005** on 2026-09-07 (`09-DECISIONS/DECISION-ID-MAP.csv`).

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

## D-034 — The audit's "96 pages" is a seventh page count, not a resolution

**Renumbered from D-006** on 2026-09-07 (`09-DECISIONS/DECISION-ID-MAP.csv`).

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

**Identifier-space note.** The D-004 to D-006 collision this block was written
around was resolved on 2026-09-07: the three colliding sections in this file
became D-032 to D-034 and `09-DECISIONS/OWNER-DECISIONS.csv` is now
authoritative for the whole namespace. D-015 to D-031 were not renumbered.

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

## D-042 — Egress reach is not stable between sessions. Does domain E run under a GitHub-only policy?

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

---

## D-043 — Egress allowlist: the substrate literature is unreachable

**Raised:** 2026-09-07, domain E. **Category:** institutional access.
**Blocks:** four of the eleven distinctions constitution §4.E requires.

`05-HOLDS/HOLD-004-substrate-literature.md` records that Witzel 1999,
Kuiper 1991, Masica 1979, Krishnamurti 2003, Rau 2019 and Shorto 2006
cannot be retrieved from this session by any available channel. Every
plausible host is refused at the egress gateway: `archive.org`,
`dsal.uchicago.edu`, `www.jstor.org`, `gretil.sub.uni-goettingen.de`,
`titus.uni-frankfurt.de`, `www.ejvs.laurasianacademy.com`.

This is escalated rather than accumulated because the blockage is not
neutral. Attested families have machine-readable derivatives on GitHub;
proposals about unattested donors do not. So the network policy
systematically disadvantages one side of the argument, and any register
built under it will look like evidence for the side that happens to
have datasets. `BF-008` logs this as a live failure mode.

**Two of these would close most of it:** `archive.org` and
`dsal.uchicago.edu`. Both were reachable in an earlier session on the
same calendar date (`SRC-025`, and `SRC-028`/`SRC-033` for GRETIL and
TITUS), so the policy narrowed between sessions rather than these being
permanently out of reach.

**Asked of the owner:** add `archive.org` and `dsal.uchicago.edu` to the
environment egress allowlist, or supply the six works as files.

## D-038 — Two DEDR digitizations disagree, and one is published

**Raised:** 2026-09-07, domain E. **Category:** two consequential
positions both viable. **Affects:** a live page.

`IC-E-001` measures a 10.3% disagreement between the DEDR digitization
MelaKeela ships (`dedr_roots.json`, from `ArimeKannada/Dictionary`) and
the DSAL-derived one used in this unit, across the 18 languages whose
labels correspond one-to-one. Neither is a subset of the other.

`IC-E-002` is the consequence. `the-northwest-cousin.html` publishes
"counted directly from the Dravidian etymological dictionary, 191 of
Brahui's 262 recorded roots have Tamil cognates". The site's arithmetic
is exactly right for its own data. The same computation over this
unit's data gives 223 of 273 — 82% against 73%. The raw count moves as
well as the percentage the page correctly warns readers about.

Neither can be adjudicated while `dsal.uchicago.edu` is blocked, so
this is downstream of D-043 but is escalated separately because it
touches published copy.

**Asked of the owner:** whether the page should name its digitization
and carry the range in the interim. The change itself belongs in
`melakeela/site`, not here. Queued as `RA-009`.

## D-046 — Do the §10.4.7 prohibitions bind the whole institution?

**Raised by:** experience object model §5.4
**Category:** publication approval; two consequential positions both viable

Museum framework §10.4.7 states three prohibitions — no sorting of human
beings into types, no reward mechanic on extremist categories, no
persecution as spectacle — and scopes them to the children's mode:
*"anywhere in the children's mode, in any Living World, in any pilot."*

Two facts about the architecture put that scope under pressure.

First, **the institution cannot know who is looking.** §10.4.5 requires
that no account is offered to under-16 visitors and the Field Bag is local
by default. There is therefore no age gate anywhere, and a child can reach
every surface. Protections that activate only in a children's mode protect
children only where the institution guessed right.

Second, **the prohibitions are on interaction patterns, not on subjects.**
§10.4.7 says so: *"the same interaction is the same interaction whatever is
loaded into it."* A rule of that form does not obviously have an audience
scope at all — the argument that a sorting interface teaches that the
categories are operable does not weaken when the person sorting is
nineteen.

The experience object model takes the extension **within its own layer**:
the Constraint Block binds all eight object types at every age band. That
was the instruction the document was written under, and it is what the
no-gate architecture implies for objects that ask a visitor to do
something.

It does not extend the prohibitions beyond that layer, because the costs
there are real and are not the model's to weigh.

| Option | Consequence |
|---|---|
| **Bind the whole institution.** No surface anywhere offers an interaction that sorts, scores or stages people | The rule becomes checkable in one place and cannot be defeated by an audience guess. Cost: an exhibit whose *subject* is a nineteenth-century racial schema may need to reproduce that schema's operation to analyse it, and a blanket interaction ban could stop the historiography the record most needs — the `WMP-9` programme is precisely a study of how a racial category was built. |
| **Bind the experience layer only** (the position this model takes for itself) | Anything asking a visitor to do or conclude something is covered, at any age. Cost: a register view, an Atlas layer combination or a long-form Reading Room exhibit is outside, and the boundary between "arranging the record" and "asking the visitor to do something" will be argued over. |
| **Bind child-facing surfaces only**, as §10.4.7 states | Nothing changes and the owner's wording governs unaltered. Cost: the guarantee is only as good as an audience guess the institution has deliberately made itself unable to make. |

The wording of the three constraints is `INHERITED-UNVERIFIED`
(`MELA-KEELA-WHO-MADE-THE-PAST.md` §9 is not in this repository;
`RESEARCH-QUEUE.md` `WMP-9` records the provenance and the numbering
discrepancy raised as D-037). Their standing as constraints does not
depend on that — they are prohibitions on what the institution builds, not
claims about the past — but their **scope** is the owner's, and it is what
is being asked here.

**Decision:** do the three prohibitions bind the whole institution, the
experience layer, or child-facing surfaces only?

## D-047 — Which curricula do Learning Objectives map to?

**Raised by:** experience object model §12.6
**Category:** publication approval
**Related:** `09-DECISIONS/OWNER-DECISIONS.csv` D-008 (Release 1 scope),
museum framework D-031 (language commitments)

Museum framework §10.5.2 settles the discipline and leaves the scope open:
*"Curriculum-alignable, not curriculum-bound. The institution may map its
material to a syllabus as a convenience layer. It may not alter a claim, a
status or an absence to fit one."* And, in the sentence that makes
alignment safe to offer at all: where the record and a curriculum disagree,
classroom mode *"says that they disagree and shows the evidence"*, in both
directions — *"this applies equally where the curriculum is the one this
project would prefer."*

The experience object model implements all of that. `curriculum_alignments[]`
is metadata: it may not appear in `taught_on[]`, may not affect
`assertion_form`, and may not raise a claim's status. An alignment that would
require a `knows-that` objective on a claim below `VERIFIED` is refused.

What is not settled is whether any curriculum is mapped, and which.

| Option | Consequence |
|---|---|
| **Map to named curricula** | Teachers find the material through the route they actually use, which is the difference between a resource that is used and one that is admired. Cost: each mapping is a standing maintenance commitment of the kind §11.10.4 describes for a language — a curriculum revises, and a stale alignment misroutes a teacher toward material that no longer answers what they were sent for. It is also a positioning claim: mapping to one national syllabus and not another says something about who the institution is for. |
| **No alignment** | Nothing to maintain and nothing implied about audience. Cost: the teachers §10.5.1 is written for — *"not a specialist and has an hour"* — have to do the mapping themselves, and most will not. |
| **Defer** | Reasonable, since the answer depends on D-008 and D-031 and costs nothing while objectives publish with the field empty. |

This is a live question rather than a hypothetical one for this record
specifically: the material touches topics that appear in national curricula
in forms the evidence does not support, and an aligned objective is the
surface where the institution's disagreement with a syllabus becomes visible
to the person teaching it.

**Decision:** which curricula, if any, are mapped?

## D-048 — Does an individual's consent suffice where a community holds authority?

**Raised by:** experience object model §13.3.3
**Category:** living-community consent

A `present-day-investigator` Character is a living person shown doing the
work — an excavator, a translator, a conservator, a community member. §11.4
requires a consent record from them, per purpose and per surface. §11.2
separately records where a **community**, not the institution, holds
interpretive authority over the material.

When the person is a member of that community and the material is within
that authority's scope, the two mechanisms meet and neither says which
governs.

The tension runs in both directions and neither side is safe.

- **Requiring community sign-off** makes the institution the arbiter of who
  counts as a representative — which §11.2 warns against in its own terms:
  *"an institution that consults one organisation and reports 'the community
  agreed' has made a claim it cannot support."* It also gives a community
  body an effective veto over an individual member speaking about their own
  practice.
- **Not requiring it** lets the institution obtain one person's consent and
  publish the result where a visitor will read it as the community's account.
  §11.2's requirement that representation be recorded *"including its
  limits"* — *"who was consulted, how they were identified, and who this does
  not speak for"* — is a mitigation, not an answer.

| Option | Consequence |
|---|---|
| **Individual consent suffices**, with the individual's own scope stated on the surface | The person speaks for themselves and is shown doing so. Cost: the distinction between "a member of this community says" and "this community says" rests entirely on a caption. |
| **Community agreement additionally required** wherever an authority record covers the material | The community controls how it is represented on its own material. Cost: the institution has to decide whose agreement counts, which is the claim §11.2 says it cannot support. |
| **Required only where the person is presented as speaking for the community** rather than for themselves | Follows the actual claim being made. Cost: the line is drawn by the institution's own framing, and framing drifts. |

The model currently specifies the individual consent as required and the
authority record as carried where one applies, without ruling on precedence.
That is a deliberate gap, not an omission.

**Decision:** which governs, and where is the line?

## D-049 — May the method guide be personified for children?

**Raised by:** experience object model §13.3.4
**Category:** publication approval

The `institutional-voice` Character is MelaKeela speaking as itself: the
Step 14 interpretation register, and the guide that explains what a status
is, what `NOT EXCAVATED` means, and why nine citations can be one source.
The model specifies it unpersonified — no name, no biography, no
personality, no relationship with the visitor.

Whether that holds for children is the owner's.

**The case for personification.** A guide is how most children's material
makes an unfamiliar method approachable, and this institution is asking
children to hold statuses, absence types and an attestation gradient — more
apparatus than a children's museum usually carries, not less.

**The case against.** A friendly guide is the standard vector for smoothing
uncertainty. A character with warmth is read as reassuring, and reassurance
is precisely what a `HYPOTHESIS` claim must not receive — museum framework
§12.3, V-2: *"Confidence is never conveyed by production value."* A
personified guide is also one step from a mascot, which §13.6 item 14
forbids where it stands for a people, a place, a language or a period.

If personification is permitted, the constraints that would have to hold are
already in §13.3.4: no biography, no opinions beyond the institution's
statused positions, speaks last on any question, and says *"we do not know"*,
*"we were refused access"* and *"we were wrong"* as readily as it says
anything else. A guide that cannot say those three things is not the
institutional voice; it is a mascot with a clipboard.

**Decision:** apparatus only, a personified guide with those constraints, or
personification in the children's mode alone?

## D-050 — Does the institution depict past people visually at all?

**Raised by:** experience object model §13.5
**Category:** publication approval
**Related:** museum framework D-026 (human remains)

Any depiction of a past person is an interpretation (`is_primary =
interpretation`, §2.5) with a named maker and a date. It also supplies what
the record does not: a face, a build, a skin, a dress, an age, a bearing.

Each of those is an assertion, and several are identity attributions of the
kind §13.6 item 4 forbids in text. **A drawn face makes an ancestry claim
that a sentence would have had to status.** This is the specific reason the
question is escalated rather than answered by the general rule about marked
reconstructions: the marker travels with the image, but the inference the
viewer draws does not wait for it.

Against that: the total absence of depicted people leaves the past populated
by objects and no one, which is its own distortion, and one this record has
named repeatedly in the form of the §4V provenance questions.

| Option | Consequence |
|---|---|
| **No depiction of past people** | No unstatused visual assertion is possible. Cost: the museum shows things and never people, which reads as a claim that the things made themselves. |
| **Depiction as marked interpretation**, maker and date named, reconstruction marker carried | People are visible and the image is honest about being an image. Cost: every such image asserts appearance, and appearance is where ancestry claims enter without a mechanism. |
| **Only where an attested ancient image exists** — a figurine, a relief, a painted scene — reproduced with description separated from interpretation (§2.4), and nothing commissioned | The institution shows how people were depicted *then*, which is evidence, rather than how they looked, which is not. Cost: coverage is uneven and follows what survives, which is itself an archive bias the surface would have to state. |

Rights (§11.8) and evidential alt text (§11.9.3) apply to any depiction made.

**Decision:** which, and under what marker?

## D-051 — May attested words be voiced, or only quoted?

**Raised by:** experience object model §13.3.2
**Category:** two consequential positions both remaining viable

A `documented-individual` Character presents words attested in a source at a
locator. The model's default is `voice_rendering = quotation-only`: the words
appear as quotation, with the Translation Block (§3.8) and the `is_primary`
step (§2.5) beside them.

Whether they may also be **read aloud** — as audio, a recorded reading, or a
first-person presentation — is a real choice with costs on both sides.

**Against voicing.** A reading adds tone, pace, emphasis, gender, age and
emotion. The record carries none of these, and a listener attributes all of
them to the speaker rather than to the reader. It also carries a translation
choice past the visitor: §3.8's display contract requires the alternatives
and the interpretive consequence *"one interaction away, on the same
surface"*, which audio makes awkward. And it approaches, without crossing,
the line §13.6 item 2 draws at interiority — a performance implies a state
of mind.

**For voicing.** Refusing it entirely leaves ancient words permanently inert
and privileges silent reading of a script most visitors cannot read. That is
an accessibility position as much as an editorial one, and §11.9 makes
accessibility a release gate rather than a preference.

| Option | Consequence |
|---|---|
| **Quotation only** (the model's default) | No performance, no implied state of mind, apparatus always adjacent. Cost: the words reach only readers of the script or of a translation. |
| **Voicing permitted** with the apparatus reachable on the same surface | The words are audible. Cost: everything in the paragraph above, on every listen. |
| **Voicing of attested original-language text only, never of a translation** | Voicing an original is closer to a facsimile than to a performance; voicing a translation is a performance *of an interpretation*, which is a different act. Cost: a visitor who does not know the language hears sound and reads apparatus, which may be exactly right or may be theatre. |

§13.6 item 5's prohibition on voicing reconstructed forms stands under every
option: no proto-language is ever spoken aloud, at any age, because no
marker survives audio.

**Decision:** quotation only, voicing with apparatus, or original-language
voicing only?

## D-052 — Does the institution hold per-visitor progress state?

**Raised by:** experience object model §10.5
**Category:** publication approval; two consequential positions both viable
**Related:** D-046 (both turn on the same no-age-gate derivation)

Museum framework §10.3 permits a server-side Field Bag: *"Local by default.
The bag is stored on the visitor's own device and needs no account. Any
server-side bag is opt-in, and for under-16 visitors it does not exist at
all."*

The experience layer needs a position on the same question for Mission and
Journey progress, and taking one turns out to reopen the framework's rule
rather than merely extend it.

**The derivation.** §10.4.5 offers no account to under-16 visitors and
forbids behavioural analytics *"on any surface, at any age"*. An institution
with no accounts and no tracking cannot know who is on a surface. So a
server-side store whose exclusion is "does not exist for under-16 visitors"
has an exclusion it cannot apply. **An opt-in a child can take is not an
opt-in with an age condition on it; it is an opt-in.**

| Option | Consequence |
|---|---|
| **No server-side per-visitor state at all** (the model's recommendation, labelled as such) | The institution holds no per-visitor record, and the under-16 rule is satisfied by construction rather than by a check it cannot run. Cost: a visitor who changes device loses their place, and §10.3's opt-in bag is withdrawn — a real feature removed on an argument, not on a requirement. |
| **Keep §10.3's opt-in**, and allow `opt-in-server-side` progress beside it | The framework's rule stands unamended and adults who want continuity across devices get it. Cost: the institution holds behavioural records it cannot show contain no child's data, while §10.4.5 states that it holds none. |
| **A declared-age gate** | Rescues §10.3 and §10.4.5 as written, since the under-16 exclusion becomes operable. Cost: it puts an age claim about a visitor into a product from which §10.4.5 has removed every other visitor datum, and a self-declared birth date admits anyone who types a number. |

The experience object model specifies both storage values, writes every
other rule so that either works, and does not choose. Classroom sets are
unaffected under all three options: they are the teacher's, saved to the
teacher's optional account, holding no student data and no assessment
scoring (§10.5.2).

**Decision:** which of the three, and if the first, is §10.3 amended in the
framework or left standing with this layer as its exception?

## D-054 — May the WATER modern-system slot name a live Chennai water dispute?

**Raised by:** `13-PRODUCT-ARCHITECTURE/water-living-world.md` §4.5 (slot 5)
**Category:** living-community consent
**Related:** D-005 (is WATER first), D-048 (individual consent where a
community holds authority), D-001 (india-seminar.com is blocked, so the one
source the backlog names by name for this slot is unread)

The WATER Living World's fifth slot is MODERN SYSTEM. Museum framework
§10.2, constraint 1, is explicit that the slot cannot be dropped: the thread
*"must reach the present — refusing to would be its own distortion — and must
do so through statused bridges, never through adjacency."*

So the question is not whether WATER reaches the present. It is what the
present slot is permitted to name.

**What the reachable evidence contains.** The only literature lane that
answered on Chennai in this session (`SRC-090`, Scholar Gateway) returned
Coelho 2022, *Urban Waterlines* (`10.1111/1468-2427.13087`). Its argument is
that Chennai's water infrastructure produces social difference: the pipe
network is described as *"structured by historical geographies of power,
embodying the exclusions and classifications of colonial rule"*, and the
eco-restoration of urban *eris* from the mid-2000s *"spelled the violent
demolition of homes and livelihoods autoconstructed by lowincome families
over two generations"*, under a regime that *"(selectively) criminalized
actions and people that violated this boundary."*

*(Quoted from the passage chunks returned by `SRC-090`, not from the
published article, which `SRC-095` shows cannot be reached. The connector
strips hyphens and footnote markup — "lowincome" is the chunk's spelling, not
Coelho's — so these are quotations of what was retrieved, and none may be
carried onto a page until the article itself is read.)*

That is the best modern-system evidence available to this repository today.
It is also an account of identifiable living people who were evicted, some
within the last twenty years, in a dispute that is still running.

**Why this is the owner's and not the record's.** Three of the options below
are defensible on the evidence and the evidence does not choose between
them.

| Option | Consequence |
|---|---|
| **Name the dispute, after the §11.2 community-authority and §11.4 consent work is real** | The slot does what the constitution's §4V asks — who did the labour, who was excluded, who got the credit — in the present tense, where it is checkable. Cost: it cannot ship until relationships exist that do not exist now, which pushes the WATER flagship behind work that has not started. |
| **Name the dispute only where it is already a matter of public record, naming no community as a party** | Buildable now, and it keeps the institution off the ground where it would be speaking about people who have not been asked. Cost: "public record" is the colonial-hydrology archive plus the English-language press, which is precisely the archive that recorded the eviction and not the evicted. |
| **Aggregate hydrology and governance only — reservoir volumes, rainfall, network coverage, no named community** | Cleanest consent position, and it still supports a true modern slot: the 2019 reservoir failure is a fact about storage. Cost: it reproduces the depoliticised account that Coelho is arguing against, and it does so by omission, which the negative-evidence standard would type as `NOT PRODUCED` by us. |
| **Defer the slot until Release 1 scope is set** | Honest, and consistent with D-005 being open. Cost: WATER without a modern slot is not a Living World under §10.1; it is six-sevenths of one, and the specification says so. |

**What the specification does under each.** Slot 5 of
`water-living-world.md` (its §4.5) defines the slot's evidence requirement and
its bridge discipline identically under all four; only the permitted subject
changes. Nothing else in the seven-slot pattern moves. The
specification is therefore complete and unblocked as a specification, and
blocked only at the point of filling this one slot.

**Decision:** which of the four, and if the first, does the WATER build wait
on the community-authority work or proceed with the slot held open and
visibly typed as held?
