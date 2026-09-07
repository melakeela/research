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
