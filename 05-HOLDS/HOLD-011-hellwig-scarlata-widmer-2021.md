# HOLD-011 — the 2021 reassessment was reached in abstract only

**Raised** 2026-09-07, domain A.
**Caps** RCT-006, RCT-007 and RCT-010.

## What is needed

Oliver Hellwig, Salvatore Scarlata and Paul Widmer, "Reassessing Rigvedic
Strata", *Journal of the American Oriental Society* 141.4 (2021): 847–865.

## What this session has

The abstract, retrieved verbatim through the Consensus connector
(`SRC-099`) — the authors' own statement of what they tested and what they
found. From it, three things are firm: they modelled allomorph
distributions; they controlled for metrical positioning, prosodic structure
and content; and under those controls the distributions did not lend
significant support to any of the proposed stratifications, while a cluster
analysis still favoured book 10 occupying a special position.

What the abstract cannot supply is the paper's own statement of its scope —
which allomorph pairs, over what portion of the corpus, and what the authors
themselves say the result does and does not rule out.

## Why it is blocked

- `www.zora.uzh.ch`, the Zurich open-access repository holding the
  author copy: HTTP 403 at CONNECT, and `EGRESS_BLOCKED` from `WebFetch`.
- `www.jstor.org`, `doi.org` and `api.crossref.org`: HTTP 403 at CONNECT.
- Scholar Gateway's corpus is Wiley-weighted and does not carry JAOS
  (`SRC-100`). Scholar Feed and alphaXiv are arXiv-only (`SRC-101`,
  `SRC-102`). Scite's free-tier quota is exhausted until 2026-10-01
  (`SRC-103`).

Five literature connectors and four hosts; one abstract.

## What turns on it

`RCT-006` reproduces the paper's central pattern independently, on one
allomorph pair, from this repository's own extraction: position in the pāda
governs the -ebhiḥ/-aiḥ choice at p = 4.9e-37 while Arnold's strata give
p = 0.353. That reproduction does not depend on the paper.

`RCT-010` does depend on it. It states that the 2021 result is a failure to
find support for stratification in one class of evidence under controls, and
not a demonstration that the Rigveda has no internal chronology. That reading
is well supported by the abstract's own wording — "do not lend significant
support" is not "refute" — and by the abstract's own finding that book 10
still separates. But the authors' scope statement, not this repository's
reconstruction of it, is what should govern a claim about what their paper
shows. `RCT-010` is PROVISIONAL for that reason and should not be cited on a
public page until the article is read.

## Negative-evidence typing

`NOT ACCESSIBLE`. The article has an open-access copy in an institutional
repository. This is an egress policy, not a gap in the record.

## What would clear it

`www.zora.uzh.ch` on the environment egress allowlist (`D-047`), or a
scite/institutional subscription restored.
