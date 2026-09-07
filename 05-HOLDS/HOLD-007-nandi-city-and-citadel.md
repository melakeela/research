# HOLD-007 — Nandi, "The City and the Citadel"

**Raised:** 2026-09-07 by the domain J unit.
**Blocks:** promotion of `HYP-J-001`'s gate verdict above a verdict taken on a
publisher's abstract.
**Does not block:** the rest of domain J. The corpus, the counts, the fields,
the typology and the twelve measurements `DJ-001`–`DJ-012` do not depend on it.
**Owner decision:** `D-046` (payment and lawful acquisition).
**Ledger:** `SRC-086` identified-not-retrieved; `SRC-087` every host
`EGRESS_BLOCKED`; `SRC-088` a second, stronger instance of the same thesis,
also unreachable.

## What is needed

R. N. Nandi, "The City and the Citadel", chapter 4 of *An Outline of the Aryan
Civilization*, Routledge/Taylor & Francis 2017, DOI `10.4324/9781315101149-4`.

## Why the hold is on this and not on the finding

Constitution §4J gives this domain one prohibition — *"Do not automatically
translate pur into a Mature Harappan city"* — and this chapter is that
translation in its canonical published form. **The domain's named trap and the
domain's unreadable source are the same object.**

The gate ran anyway, because a thesis stated clearly enough can be tested
against a corpus that is in hand, and refusing to run it would have left §4J's
prohibition standing with nothing behind it. But the distinction the hold
preserves is the whole point:

- **The thesis was gated.** Its four named terms were checked against the
  pinned corpus, and two of four do not denote fortified settlements on the
  lexicon in hand (`DJ-010`, `DJ-011`).
- **The argument was not gated.** Nobody here has read a line of it. Nandi may
  argue the identification from archaeological stratigraphy, site plans or
  comparative Bronze Age fortification — evidence classes this unit holds none
  of and therefore could not weigh. A chapter is not its abstract.

`HYP-J-001` therefore returns `NOT-ELIGIBLE-SOURCE-BLOCKED`, not
`NOT-ELIGIBLE`. **The verdict is that this repository cannot adjudicate the
thesis, and can say exactly why. It is not a verdict that the thesis is false,
and it must not be reported as one.**

## What was tried

| Channel | Hosts | Result |
|---|---|---|
| `curl` via the egress proxy | taylorfrancis.com, doi.org, routledge.com, researchgate.net, pragyata.com, api.crossref.org, api.openalex.org | `EGRESS_BLOCKED`, HTTP 000, all seven |
| `WebFetch` | taylorfrancis.com | `error_type EGRESS_BLOCKED` |
| `WebSearch` | — | bibliographic identity and an abstract summary; **discovery, not retrieval** |

Both retrieval channels refuse the same host, so the block is the
environment's, not one tool's. `CLAUDE.md` forbids treating a WebSearch snippet
as a substitute for the source, and it is not treated as one: the only content
taken from it is the four-term list, used to decide *which terms to test*, and
every gate leg records that the argument is unread.

## What would close it

1. The chapter, by purchase or institutional access — `D-046` option (a).
2. Failing that, `doi.org`, `api.crossref.org` and `api.openalex.org` unblocked
   would upgrade `SRC-086` from a search-index summary to a publisher record.
   That does **not** close this hold; it closes a smaller defect inside it.
3. A reachable statement of the same thesis. `SRC-088` (Semenenko) is a
   stronger form of it and is equally unreachable; no reachable substitute has
   been found.

## What would change the verdict rather than the hold

An archaeological source, or any absolute chronology for the Rigveda, would let
the two gate legs that **could not be run** — chronology and geography — be run
at all. Those are the two legs the thesis most depends on, and no amount of
corpus work supplies them. A pre-modern or non-European commentary reading
`durgá-` or `vr̥trá-` as a fortification would move `DJ-010` and `DJ-011` off
the single German lexicon they currently rest on (`DEP-021`, `DEP-022`,
`RA-015`).
