# Retrieval notes — 2026-09-06 source access audit

Backing record for `02-SOURCES/access-ledger.csv`. Every row in that
ledger traces to a probe recorded here. Nothing in either file is
inferred from documentation; each result is a live call made in this
session.

## Method

Each candidate source was probed by its own access channel — MCP tool
call, `WebFetch`, or `curl` — with a query drawn from the programme's
actual subject matter rather than a generic health check. A source is
recorded `retrieval_capable=YES` only if a probe returned content.

## Connector probes

`/mcp` is an interactive CLI command and is not callable from this
non-interactive session. `ListConnectors` was used instead, then each
connector enabled in this chat was probed with a real call.

Sixteen connectors are installed on the account. **Four** are enabled in
this chat: Scholar Feed, Scite, a2aj, Descrybe Legal Engine.

- **Scholar Feed** — `search_papers` returned five on-topic arXiv papers,
  including `1702.00523` *Deep Learning the Indus Script* and
  `2608.02999` on the non-specificity of statistical decipherment
  measures. Results carried no `is_saved`/`is_read` keys, which per the
  tool contract indicates an anonymous call; `list_library` then failed
  with an explicit "sent without a Scholar Feed API key" error. So:
  search works, library state does not.
- **Scite** — refused with a monthly MCP usage limit error. 25 calls,
  exhausted, resets 2026-10-01 UTC. Authenticated but unusable this month.
- **a2aj** — `coverage` returned 29 Canadian court and tribunal datasets.
  Working, but Canadian law only; no bearing on this programme.
- **Descrybe Legal Engine** — token expired, requires re-authorization,
  and the server disconnected from the session mid-probe. Also US law
  only; no bearing on this programme.

Three installed-but-not-enabled connectors are plausibly relevant and
remain **untested**: alphaXiv, Consensus, Scholar Gateway. They are
recorded `PROVISIONAL` because their status comes only from the
connector registry, not from a call.

## Network egress

This is the material finding.

`WebSearch` works — it returned eight real URLs for digitized
*Epigraphia Indica* volumes. But every one of those URLs is unfetchable.
`WebFetch` and `curl` were blocked by the environment's network egress
proxy for archive.org, indianculture.gov.in, GRETIL, en.wikipedia.org,
jstor.org, arxiv.org and doi.org. Raw `curl` returned HTTP 000 for all
of them. Only `api.github.com` answered (HTTP 200).

Proxy status confirms `enabled: true` with `selective: false`; the
allowlist admits Anthropic API hosts, package registries and private
ranges, and nothing else.

## Consequence for evidence status

`README.md` holds that a claim may not be promoted by argument, and that
promotion requires a retrieval event recorded in the source ledger.

Against that rule, the audit's result is that **no primary source for
ancient South Asia can currently be retrieved in this environment.**
`WebSearch` can locate a source but cannot retrieve it, so it yields
locators without retrievals and cannot promote anything. The single
working subject-matter channel is Scholar Feed, whose corpus is arXiv
CS/AI — it reaches computational epigraphy, not archaeology, philology
or the epigraphic corpora themselves.

The practical effect: until the egress allowlist is widened, claims in
this programme are capped at `HYPOTHESIS` or `INHERITED-UNVERIFIED`, and
anything depending on the blocked repositories belongs in `05-HOLDS/`.
No holds are filed yet because no claims have been entered.

## Not done in this pass

`CLAUDE.md`, `AGENTS.md` and `RESEARCH-QUEUE.md` do not exist on any
branch of this repository — only `README.md` does. Queue item 1 was
therefore executed from the task description alone, not from the queue
file. The controller and backlog were deliberately not authored here:
inventing a research constitution or a backlog would be exactly the kind
of unsourced content this repository's rules forbid. See
`DECISIONS-NEEDED.md`.
