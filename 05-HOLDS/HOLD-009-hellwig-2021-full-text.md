# HOLD-009 — Hellwig et al. 2021 is available here only as an abstract

**Raised by:** domain A, 2026-09-07
**Blocks:** `DA-I-004` beyond `PROVISIONAL`; and any statement about
which stratifications the paper tested, which features it used, or who
wrote it.
**Ledger:** `SRC-082`, `SRC-080`, `SRC-077`

## What is held

The Consensus connector returned the abstract of *Reassessing Rigvedic
Strata*, *Journal of the American Oriental Society*, 2021, first author
Oliver Hellwig, in full and verbatim (`SRC-077`). That is a real
retrieval of the abstract and `DA-I-004` is written from it.

Three things the abstract does not supply, and that this record
therefore does not have:

1. **Which stratifications were tested.** The abstract says
   "stratifications proposed in previous literature" and names none.
   Whether Arnold's five metrical periods — the stratification this
   entire repository depends on — were among them is **not
   established**. That is the single most consequential gap in this
   unit, because the paper is being invoked, here and elsewhere, as
   bearing on Arnold.
2. **Which allomorphic features.** The abstract says features "claimed
   to bear signals of stratification" and names none. Without them the
   result cannot be checked against `DA-M-031` and `DA-M-032`, which
   measure seventeen inflectional categories over the same corpus.
3. **The author list.** The connector truncates it to "Oliver Hellwig
   et al." The Scarlata and Widmer co-authorship that the instruction
   commissioning this unit assumed is `INHERITED-UNVERIFIED` and is not
   asserted anywhere in the registers. Volume, issue, pages and DOI are
   likewise not established.

## What was tried

| Channel | Result |
|---|---|
| Consensus (`SRC-077`) | abstract returned in full; no full text on the free tier |
| scite (`SRC-080`) | refused: monthly MCP quota of 25 calls exhausted, resets 2026-10-01. This is the connector that reads full text and citation context. |
| Scholar Gateway (`SRC-078`) | Wiley-only corpus; JAOS not in it |
| Scholar Feed, alphaXiv (`SRC-079`, `SRC-081`) | arXiv-only |
| `doi.org`, `jstor.org` (`SRC-069`) | refused at CONNECT |

## What is *not* claimed

That the paper says less than it says, or more. `DA-I-004` states its
scope from its own words and marks the three gaps as gaps. The
instruction commissioning this unit was right that the result is not a
universal falsification of Rigvedic relative chronology; what could not
be established is the narrower and more useful thing — whether it tested
Arnold at all.

## Release

`D-044`: restore the scite quota, or supply the article as a file, or
allowlist a DOI resolver.
