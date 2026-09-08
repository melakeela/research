# Occurrence sweep — the Mohenjo-daro negative identification and the river cause

**Unit:** step 13 (check MelaKeela itself) plus the two adversarial tests of
constitution §8, run on a sentence in the visual-doctrine prototype for
`dasa-forts-rigveda.html`.
**Date:** 2026-09-08.
**Instruction:** register the method failure, sweep the live site for the same
or a similar claim, register each occurrence, and register the owner's two
positions separately at `INHERITED-UNVERIFIED` linked by a typed relationship.
**Explicitly out of scope, by instruction:** resolving either position, and
writing replacement copy. Nothing below adjudicates the chronology, the cause of
the Late Harappan decline, or the identification. No site file is edited by this
unit.

---

## 1. The sentence

> Whatever the ninety-nine forts were, they were not Mohenjo-daro. That city
> fell to a river, and it fell before anyone was writing about it.

The owner raised it against the visual-doctrine prototype. The sweep found it
in four files, one of which is the live page itself, verbatim in all four.

## 2. What was searched, and how it can be re-run

The site was retrieved as a working tree, not read through a search snippet:

```
git clone --depth 1 https://github.com/melakeela/site /home/user/site
git -C /home/user/site rev-parse HEAD
# 769a6f646de8f6cd5e9e76874bad5c0ab12a32cc
# ("Merge pull request #3 from melakeela/prototypes/visual-doctrine")
```

Logged as `SRC-089`. Every locator in
`03-REGISTERS/site-occurrences-mohenjo-daro.csv` is `file:line` against that
commit and is re-findable by checking out that SHA.

Search patterns, run over every file in the tree (`.html`, `.json`, `.md`):

| Pattern | What it was looking for |
|---|---|
| `fell to a river` | the pull quote, exactly |
| `not Mohenjo-daro` | the negative identification, exactly |
| `centuries too late` | the headline form of the same exclusion |
| `three to four centuries` | the chronological gap as a premise |
| `Mohenjo` (all files) | every page that names the city at all — 15 files |
| `collapse\|decline\|abandon\|deurban\|fell` within 180 characters of `river\|flood\|hydrolog\|Ghaggar\|drying\|monsoon\|climate\|Sarasvat` | any other page asserting a cause for the Indus decline |
| `centuries\|century\|too late\|already empty\|already ruins\|abandoned` intersected with `rigved\|hymn\|vedic\|indus\|harapp\|mohenjo` | any other page excluding something on a Rigveda-versus-Indus date |

**Coverage limit, stated rather than assumed.** This is a text search over the
repository at one commit. It finds the claim where it is written in words. It
would not find the same claim made by a graphic, an SVG label, a chart caption
generated at runtime, or a page not in this repository. Two of the counted
occurrences (`search-index.json`, and the card text in `exhibits.html` and
`research-index.html`) are derived surfaces that repeat a headline; if the
headline changes and those are not regenerated, they will keep carrying it.

## 3. What the sweep found

Fifteen occurrences, registered as `MDO-OCC-001` to `MDO-OCC-015` in
`03-REGISTERS/site-occurrences-mohenjo-daro.csv`. In summary:

| Where | Carries |
|---|---|
| `dasa-forts-rigveda.html` — **live page**, 6 places incl. the `<h1>`, the `<title>`, three social-card `<meta>` tags, the pull quote at line 420, the candidate table at line 451 | breach 1 throughout; breach 2 at line 420 |
| `prototypes/a2-object.html`, `prototypes/b2-object.html`, `prototypes/c-semantic.html` — the visual-doctrine set | both breaches, verbatim |
| `research-index.html`, `exhibits.html`, `search-index.json` | breach 1, as the page's headline repeated on index surfaces |
| `vedic-ritual-economy.html` | a **near neighbour that does not breach**: the same cause account, attributed and hedged ("the best current evidence points to") |
| `who-writes-the-textbook.html` | the platform's **own contradicting statement**: the causes are "genuinely contested" |
| `dasa-forts-rigveda.html` lines 548–557 | the page's **own contradicting statement**: the conventional dating is unresolved, and "anyone who tells you otherwise is choosing a date to fit a conclusion" |

The last two rows are why this is registered as a method failure and not as a
disagreement about the Bronze Age. The platform already holds the more careful
formulation, in its own words, on its own pages. The prototype and the live
page publish the less careful one in the largest type on the page.

**One incidental closure.** `CORRECTIONS-PENDING.md` Brief 3 §3.1 records that
the repository could not confirm that `dasa-forts-rigveda.html` carries the
headline attributed to it, that being finding C-6, "Three names for one target",
in `06-BRIEFS/rv01-reconciliation.md` §5. It does carry it, at line 110, and
`the-forts` is not a separate live file at this commit. Queued as `RA-025` so
the caution is narrowed by the unit that owns it rather than by this one.

## 4. A third failure, found by the sweep and not raised by the owner

`prototypes/b2-object.html` line 235 heads the box containing both breaches with
the single word **"Established"**. The live page heads the same box "The
Harappan cities were already empty". `prototypes/README.md` states that every
prototype uses "the real text of an existing page, unedited in substance — same
claims, same counts, same caveats, same stated limits". Substituting an
epistemic status label for a descriptive heading is a substantive edit, and it
runs in the direction of more confidence. Logged as `BF-026`.

Two further facts about the prototype set, recorded so the next unit does not
have to rediscover them: `prototypes/README.md` says the set is "not merged",
and at this commit the files are on `main` — the commit is the merge of PR #3
from `prototypes/visual-doctrine` — carrying `noindex,nofollow` and not linked
from any root page. Present and unlinked is not the same as unmerged.

---

## 5. The owner's two positions, verbatim

Recorded here because register rows point at this section as their locator. They
are the owner's, transcribed from the instruction of 2026-09-08; this repository
holds no other copy of that message.

> **Position 1.** …that the region referred to contained fortified sites.

> **Position 2.** …that the identification has been institutionally dismissed
> rather than evidentially refuted.

Registered as `MDO-P-001` and `MDO-P-002` in
`03-REGISTERS/dasa-forts-mohenjo-daro-positions.csv`, both
`INHERITED-UNVERIFIED`, and linked by `BR-J-001` in
`03-REGISTERS/CROSS-DOMAIN-BRIDGES.csv`.

**They are two claims of different kinds and they are not merged.** Position 1
is a claim about the Bronze Age, answerable by excavation reports, site
gazetteers and dating. Position 2 is a claim about a discipline, answerable by
publication history, review record and citation trail. Under the negative-
evidence standard (constitution §6) Position 2 is an argument from an absence —
the absence of an evidential refutation — and it may not be argued from until
the absence is typed: what refutation should exist, who would have produced it,
where it would have been published, whether it was produced, preserved,
published, accessible, and whether we would recognise it if we saw it. Until
then the honest reading of Position 2 is that it is untested, not that it is
strong.

**Evidential support does not flow between them in either direction**, and the
bridge row says so as its verdict. Fortified sites in the region would not show
that a dismissal was institutional. A documented institutional dismissal would
not put a fort in the ground. Merging them would let a claim about how the
academy behaved do the work of evidence about the second millennium BCE — the
preferred-counter-narrative failure. Splitting them and then quietly dropping
Position 2 as "not archaeology" would be the prestige failure. Both are
recorded, separately, and both are open.

## 6. What this unit did not do

- It did not date the Rigveda, and it holds no position on the c. 1500–1200 BCE
  window. That is domain A, and no domain A retrieval has been run.
- It did not adjudicate the cause of the Late Harappan decline.
- It did not test either owner position, and neither is gated.
- It did not identify, or refuse to identify, the *púr-* of any passage with any
  site.
- It wrote no replacement copy and edited no file in `melakeela/site`.
