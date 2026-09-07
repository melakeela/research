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