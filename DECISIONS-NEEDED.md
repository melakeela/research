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

### Update 2026-09-07 — the prompt-pack arrived; the entry narrows

Five files were attached and are committed unchanged, md5-verified, at
`00-CONTROLLER/prompt-pack/`:

```text
MELAKEELACLAUDECORRECTIVECONTROLLERv2.md
MELAKEELALANGUAGERESEARCHPROMPTS.md
MELAKEELACLAUDEFULLSEQUENCE.md
MELAKEELACLAUDELIVESITEAUDITPROMPT.md
MELAKEELACLAUDESAYNEXTRESEARCHPROMPT.md
```

They are inventoried in `00-CONTROLLER/prompt-pack/PROMPT-PACK-INVENTORY.md`.
Three things change here.

**1. The R1–R19 half of this entry is closed.** All nineteen packets are
defined in full in `MELAKEELALANGUAGERESEARCHPROMPTS.md`.
`RESEARCH-QUEUE.md` now defines them rather than naming them, with the run
order that three of the five files state identically and the binding
dependency graph. `CONTROLLER-RECONCILIATION.md` §5's second outstanding input
is satisfied.

**2. The backlog half narrows but does not close.**
`MELAKEELACLAUDECORRECTIVECONTROLLERv2.md` Part IV **enumerates all
eighty-nine items**, verified 1–89 with no gaps, in nine groups. Constitution
§10 requires a row per item but never listed them, and this entry was opened
because writing eighty-nine rows would have meant inventing them. That is no
longer true for `backlog_id` and `title`, and the grouping determines several
dispositions outright — the "Do not build yet" block (76–89) carries its own,
as do "Later" (66–75) and "Research first" (9–19).

It remains true for `current_site_coverage` and `existing_route`, which need a
live-site route inventory this repository cannot presently produce, and for
`prior_research_available`, which needs the packets to have run.

The question that remains is narrower than the one this entry opened with:

> Is Part IV's list *the* "MelaKeela.com v2 — Master Research, Product &
> Institutional Backlog", or a digest of a longer document that should still
> be committed?

If it is the backlog, `BACKLOG-COVERAGE.csv` can be started now against the
columns that do not depend on the site inventory, and D-008, D-009 and D-011
become answerable in part. If it is a digest, the longer document is still
needed.

**3. One companion file is still missing.**
`MELA-KEELA-WHO-MADE-THE-PAST.md`, the fifth companion named in running-list
Version 12, did not arrive. It is a required input at three points in the pack,
and R8 is instructed to "cross-link the documented contribution model in Who
Made the Past? rather than creating a separate incompatible schema." R8 cannot
be run to that instruction without it.

**Status:** `PARTIALLY-SATISFIED`. Still needed: an answer on Part IV,
`MELA-KEELA-WHO-MADE-THE-PAST.md`, and the 89-item backlog document if Part IV
is a digest.

### Update 2026-09-07 — Who Made the Past arrived; item 3 closes

`MELAKEELAWHOMADETHEPAST.md` was attached and is committed unchanged,
md5-verified, at `00-CONTROLLER/prompt-pack/`. **All five companions named in
running-list Version 12 are now present.** Item 3 above closes: R8's
instruction to "cross-link the documented contribution model in Who Made the
Past? rather than creating a separate incompatible schema" is executable.

Three things follow that are worth recording here rather than only in the
inventory.

1. **It is not a prompt.** The other five files instruct an agent. This one
   makes historical and historiographical assertions and cites roughly thirty
   sources with live URLs, so its content enters
   `03-REGISTERS/inherited-claims.csv` at `INHERITED-UNVERIFIED`, not merely
   the controller. Its §15 source guide is unusually candid about its own
   limits — it separates full texts from publisher abstracts and says museum
   accounts "are not independent evaluations of institutional success" — but
   candour is not retrieval, and nothing in it is promoted by being committed.
   Register intake is queued, not done.
2. **It opens a subject with neither packet nor domain.** §9 makes the
   racialization of "Aryan" a full programme, insisting on a branching concept
   history rather than "an inevitable Sanskrit-to-Holocaust chain".
   Constitution §4 has no domain for it, no R packet covers it, and §9 sets a
   learning requirement — against interfaces that ask children to sort human
   beings into racial types or turn persecution into an aesthetic spectacle —
   that nothing in the controller currently states.
3. **It raises D-039**, on whether the register keeps one `status` column.

**Status unchanged at `PARTIALLY-SATISFIED`.** Still needed: an answer on
Part IV, and the 89-item backlog document if Part IV is a digest.

---

# Decisions raised by the prompt-pack intake

Five prompt-pack files were committed unchanged to
`00-CONTROLLER/prompt-pack/` on 2026-09-07 and inventoried in
`PROMPT-PACK-INVENTORY.md`. Four decisions follow from what they contain, and
D-014 above narrows. The nine conflicts the intake found are recorded as
`PP-1` to `PP-9` in the inventory; `PP-2` to `PP-6` and `PP-9` are resolved
there by extending existing `C-` resolutions and need no owner decision.

## D-035 — Does a live public-site audit gate the first research programme?

**Raised by:** prompt-pack intake, 2026-09-07
**Category:** two consequential positions both remaining viable
**Blocks:** `RESEARCH-QUEUE.md` items 6 and R1–R19; every packet's
`R#-current-public-coverage.md` input
**Related:** D-009, D-014; `PROMPT-PACK-INVENTORY.md` PP-1

`01-INHERITED/site-review/RUNNING-LIST-RECONCILIATION.md` records that
running-list Version 11 reversed the programme's first step. Version 10 opened
with a Claude Code repository inventory; Version 12 opens with a Claude Chat
live public-site audit, and the reconciliation warns that "anything built on
Version 10's step order is working from a superseded sequence."

**The prompt-pack does not re-propose Version 10's order.** The four dated 5
September files are the reversal's own instruments.
`MELAKEELACLAUDEFULLSEQUENCE.md` states it outright — "that live audit can
replace the earlier idea that Claude Code must inventory the repository before
any research begins" — and puts repository reconciliation at Stage 7, after
reviewed packets. On the direction of the reversal, pack and running list agree.

**The conflict is with the constitution, and it is a deletion rather than a
reversal.** `00-CONTROLLER/METHODOLOGY-CONSTITUTION.md` contains no live-site
audit stage at all: the string `melakeela.com` occurs **zero times** in it, and
§16's twelve immediate actions contain no audit step. Site-checking survives
only as §5 Step 13, one step inside the fourteen applied to each individual
investigation. `MELAKEELACLAUDECORRECTIVECONTROLLERv2.md`, which post-dates the
pack and which the constitution expands, does the same.

So the governing document takes neither side of the Version 11 decision. It
drops the gate the decision produced and folds the check into per-investigation
method — with no change-log entry, no reasoning, and no mention in
`CONTROLLER-RECONCILIATION.md`.

Two things make this live rather than academic.

1. **The reversal was about which agent goes first, and there is now one
   agent.** `CONTROLLER-RECONCILIATION.md` §4 rules the Claude Chat / Claude
   Code split "obsolete as a division of labour here. This repository *is*
   Claude Code, and it produces the research." Version 11 chose between two
   agents that no longer exist as separate roles. With one agent the question
   becomes whether a live public-site audit precedes the first research
   programme at all — and nothing in this repository answers it.
2. **The audit is not presently runnable here.**
   `MELAKEELACLAUDELIVESITEAUDITPROMPT.md` requires browsing `melakeela.com`;
   the site lives in `melakeela/site`, which this session cannot read.

This is not a question the record can settle. Reinstating the gate and
ratifying its removal are both programme-ordering decisions.

### Addendum 2026-09-07 — a third voice, which does not settle it

`MELAKEELAWHOMADETHEPAST.md` §13 works from what it calls "a local audit
snapshot" and refuses to treat it as authoritative:

> It is not a verified inventory of the current production site or current
> development branch. The following are integration candidates, not claims that
> a route is currently missing or that an observed issue remains live.
> ... Routes known from previous reports but absent from the local snapshot
> require reconciliation against the actual branch and deployment. Do not
> recreate them merely because they were not in one working folder.

This cuts across the question rather than answering it. It agrees with
`MELAKEELACLAUDELIVESITEAUDITPROMPT.md` that an uninspectable route is unknown
rather than absent — the same rule under a different name — but it treats the
**branch**, not the live site, as what a snapshot must be reconciled against,
which is closer to Version 10's order than Version 11's. Read it as a third
position: neither inventory settles anything alone, and the failure mode it
names — recreating a page because one working folder lacked it — is the failure
mode the audit prompt names from the other direction.

It does not change the finding above. The constitution still has no audit of
either kind.

**Decision:** reinstate the audit-first gate, ratify the constitution's
demotion of it to Step 13, or replace it with a repository-side route
inventory — and if the gate stands, say how the audit is to be run.

---

## D-036 — Does R19's modern layer run, and under what expiry convention?

**Raised by:** prompt-pack intake, 2026-09-07
**Category:** two consequential positions both remaining viable
**Blocks:** R19's modern half; any register convention for expiring claims
**Related:** `PROMPT-PACK-INVENTORY.md` PP-7

R19 requires independent verification, "as of the research date," of
contemporary claims about U.S.–Iran hostilities, blockade, oil flows,
Venezuela, ownership stakes, Maduro, Puerto Rico and commodity shares, using
primary government and legal records, with version-pinned percentages — and
states that "the current-affairs layer expires unless refreshed."

The registers have no expiring state. Every row is durable; `SUPERSEDED`
requires a successor to point at; there is no "stale". A claim that is true on
its retrieval date and silently false a quarter later is a category this
evidence base has not had to hold before, and inventing the convention
casually would weaken the ones that already work.

Constitution §4 domain T keeps the subject, so deferring the layer is a
scoping choice rather than a rejection. **The ancient corridor is not blocked
by this** — R19's Bronze Age to imperial chronology runs under the ordinary
rules whichever way this goes.

**Decision:** run the modern layer with a dated-expiry convention (and say
what refreshes it, and how often), defer it and keep the ancient corridor, or
reject it.

---

## D-037 — What model-run budget does R1 have?

**Raised by:** prompt-pack intake, 2026-09-07
**Category:** payment or institutional access required
**Blocks:** R1, first in the agreed run order
**Related:** `PROMPT-PACK-INVENTORY.md` PP-8

R1 specifies a reproducible experiment contrasting baseline, added context,
modern linguistic annotation and a sourced tiṇai intervention, with held-out
data, a length-matched irrelevant-context control, contamination checks,
native or qualified review, and recorded model and tokenizer versions,
settings, date and **spending cap**. It instructs directly: "Do not run paid
APIs without an agreed budget." The pack's operating controls add per-case
effort tracking with founder time separated from cash, and defer paid live
comparisons "until a bounded pilot and budget justify them."

R1 is first in the run order in all three files that state one. The question
cannot be deferred behind the other packet questions without moving R1.

**Decision:** set a spending cap, run R1 with free or local models only and
say so in the method, or defer R1 and start the run order at R9.

---

## D-038 — Is running-list Version 12 the "current master work list"?

**Raised by:** prompt-pack intake, 2026-09-07
**Category:** two consequential positions both remaining viable
**Blocks:** every packet's required input set; the LS/COR/RV cross-reference
for R9–R19
**Related:** D-014; `PROMPT-PACK-INVENTORY.md` §6

All five pack files require "the current master work list" as an attachment,
and `MELAKEELALANGUAGERESEARCHPROMPTS.md` describes itself as "Companion to
master work list Version 12, sections 21–24."

`01-INHERITED/site-review/MELAKEELASITEREVIEWRUNNINGLIST.md` is running-list
Version 12, carries §§21–24, and carries the LS-, COR- and RV- series the pack
refers to. It is most likely the same document under a different name. But no
pack file equates them, `RUNNING-LIST-RECONCILIATION.md` does not, and this
repository will not assert an identity between two titles on a resemblance —
that is the move the evidence rules exist to prevent.

This matters practically: R9–R19 carry no LS IDs in the pack, and their
coverage items are traceable only through that document. If it is the master
work list, the pack's required inputs are complete but for
`MELA-KEELA-WHO-MADE-THE-PAST.md`.

**Decision:** confirm that running-list Version 12 is the master work list, or
name and commit the separate document.


---

## D-039 — One status column, or four axes?

**Raised by:** prompt-pack intake, 2026-09-07
**Category:** two consequential positions both remaining viable
**Blocks:** the `03-REGISTERS/` schema and every register built on it
**Related:** D-019; `PROMPT-PACK-INVENTORY.md` PP-10, PP-11

`CLAUDE.md` is categorical: "Every claim carries exactly one status. No claim
is unstatused," over `VERIFIED · PROVISIONAL · HYPOTHESIS ·
INHERITED-UNVERIFIED · REJECTED · SUPERSEDED · HOLD`.

`MELAKEELAWHOMADETHEPAST.md` §10 argues against exactly that design:

> Do not implement one flat scale reading "documented, inferred, plausible,
> contested, speculative, unknown." A claim can be well documented and
> contested. A document can exist while its interpretation is uncertain.
> Record at least **evidence basis**, **assessment of the inference**,
> **disagreement**, and **review status** separately; simplify their
> presentation in context.

**The objection has force.** The repository's seven values conflate at least
three axes: `VERIFIED` and `PROVISIONAL` grade the evidence basis, `HYPOTHESIS`
grades the inference, `HOLD` is a review state. None of them can say "well
documented and contested" — which is the ordinary condition of most of what
this evidence base will hold, and precisely the condition the governing
principle exists to keep visible. An `INHERITED-UNVERIFIED` row whose source is
known to be dependent has no way to record that in `status` either.

**The single column is also load-bearing.** It is what makes the inheritance
rule enforceable: one field decides whether a claim may be built on. A
four-column scheme invites a row reading `documented / strong / disputed /
unreviewed` that is thereby quietly promoted without a retrieval event ever
being logged — which is the failure the rule exists to prevent, arriving
through the schema instead of through argument.

A third option exists: keep `status` as the gate and add the other three axes
as columns beside it, so the gate stays single while the description gets
richer. That costs a migration of the existing 369 rows and every register
built since, and it is not obviously better than carrying them in `notes`.

Two smaller things ride on this decision. §10's **evidence roles** (`supports ·
contradicts · contextualizes · dates · localizes · identifies · cannot
discriminate`) are adopted regardless — they type the evidence-to-claim
relation, not the claim, and they fill a field the shared research contract
requires but never defines. §14's **claim lifecycle** (`draft · checked ·
reviewed · published · revised · withdrawn`) is an editorial workflow state
that does not belong in `status`, and is a candidate for the review column a
four-axis schema would need.

Until this is answered the single `status` column stands, and the four axes are
carried in `notes` where a row needs them.

**Decision:** keep one `status` column, split into four separately recorded
axes, or keep `status` as the gate and add the other three beside it.

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
