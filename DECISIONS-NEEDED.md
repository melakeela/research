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

### Update 2026-09-07 — the two site-review running lists are now committed; the backlog is not

Two versions of the site review running list are now in this repository at
`01-INHERITED/site-review/`, committed byte-for-byte as supplied:

| File | Version | Lines | Standing |
|---|---|---|---|
| `MELAKEELASITEREVIEWRUNNINGLIST.md` | **12** | 1349 | current |
| `MELAKEELASITEREVIEWRUNNINGLIST2.md` | **10** | 1116 | superseded |

**The filename numbering is inverted: the file marked `2` is the earlier
document.** Version established from each file's own change log. Version 12
supersedes Version 10 — it contains it byte-for-byte through line 899, then
adds sections 23 and 24 and rewrites five passages. They are not parallel
records. `01-INHERITED/site-review/RUNNING-LIST-RECONCILIATION.md` gives the
full comparison.

Their coverage items are registered: `03-REGISTERS/inherited-claims.csv` rows
`IH-370`–`IH-438`, being 51 `LS-` and 18 `COR-` items at
`INHERITED-UNVERIFIED`. The register stands at 438 rows.

**This does not close this entry.** Three things follow, and the first is the
reason the entry stays open:

1. **Neither file is the 89-item backlog.** The string `89` does not occur in
   either document, and neither contains a section answering to "MelaKeela.com
   v2 — Master Research, Product & Institutional Backlog". The owner states
   this, and the documents confirm it. `06-BACKLOG/BACKLOG-COVERAGE.csv`
   remains blocked in full, and owner decisions **D-008, D-009 and D-011 remain
   blocked with it**. The 51 `LS-` and 18 `COR-` items are the running list's
   own coverage series; they are not the 89 items, and coverage rows must not
   be written from them.

2. **The prompt-pack is still absent, and it is larger than the table above
   records.** Version 12 names five companion files. Two are not in this
   entry's request list and none is in this repository:

   | Named in Version 12 | In the table above | Present |
   |---|---|---|
   | `MELA-KEELA-CLAUDE-FULL-SEQUENCE.md` | yes | no |
   | `MELA-KEELA-LANGUAGE-RESEARCH-PROMPTS.md` | yes | no |
   | `MELA-KEELA-CLAUDE-LIVE-SITE-AUDIT-PROMPT.md` | yes | no |
   | `MELA-KEELA-CLAUDE-SAY-NEXT-RESEARCH-PROMPT.md` | **no — add** | no |
   | `MELA-KEELA-WHO-MADE-THE-PAST.md` | **no — add** | no |

   §16 of the constitution requires reading every file in the prompt-pack. Five
   are named; none is readable.

3. **The body of this entry above is now partly superseded.** It refers to
   `MELAKEELASITEREVIEWRUNNINGLIST.md` in the singular as "the only related
   material available". There are two, ten and twelve versions deep, and the
   later one is present. The paragraph is left standing rather than edited,
   under the rule that correction history stays visible.

**Decision, restated:** supply the 89-item v2 backlog and the five companion
prompt-pack files, or say they are superseded. The running-list gap is closed;
the backlog gap is not, and closing the first did not close the second.

A current route inventory for the live site remains outstanding. Version 12's
§23.1 contains a preliminary public-site reconciliation, but it is a prior
thread's reading, not a retrieval, and it enters as `INHERITED-UNVERIFIED` like
everything else in the file.


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

