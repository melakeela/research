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
