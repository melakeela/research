# Occurrence sweep — the Mohenjo-daro negative identification and the river cause

**Unit:** step 13 (check MelaKeela itself) plus the two adversarial tests of
constitution §8, run on a sentence in the visual-doctrine prototype for
`dasa-forts-rigveda.html`.
**Date:** 2026-09-08. **Revised the same day** after independent adversarial
review; §7 lists what changed and why.
**Instruction:** archived verbatim at
`01-INHERITED/owner-instructions/2026-09-08-mohenjo-daro-bias-audit.md`.
**Explicitly out of scope, by instruction:** resolving either owner position,
and writing replacement copy. Nothing below adjudicates the chronology, the
cause of the Late Harappan decline, or the identification. No site file is
edited by this unit.

---

## 1. The sentence

> Whatever the ninety-nine forts were, they were not Mohenjo-daro. That city
> fell to a river, and it fell before anyone was writing about it.

The owner raised it against the visual-doctrine prototype. It is in four
files, verbatim in all four, and one of them is the live page.

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
commit and is re-findable by checking out that SHA. Every one of them was
re-checked line by line during the revision.

**Corpus.** 229 files, every type: 141 `.html`, 20 `.woff2`, 13 `.js`, 12
`.png`, 11 `.txt`, 8 `.json`, 7 `.svg`, 7 `.md`, 6 `.css`, 2 `.ico`, 1
`.xml`, 1 `.toml`. Derived by
`find . -path ./.git -prune -o -type f -print | sed 's/.*\.//' | sort | uniq -c`.
The first pass searched `.html`, `.json` and `.md` only and said it had
searched every file; that is `BF-030`, and it cost the sweep five
occurrences.

| Pattern | Looking for | Result |
|---|---|---|
| `fell to a river` | the pull quote, exactly | 4 files |
| `not Mohenjo-daro` | the negative identification, exactly | 4 files |
| `centuries too late` | the headline form of the exclusion | 6 files + `search-index.json` |
| `three to four centuries` | the chronological gap as a premise | 5 files |
| `mohenjo`, case-insensitive, **all file types** | every file naming the city | **20 files** (15 of them `.html`) |
| `end\|ends\|ended\|collaps\|declin\|abandon\|deurban\|fell\|fall\|dies\|died\|destroy\|emptied\|drying\|drought` within 150 characters of `harapp\|indus\|mohenjo\|ghaggar\|sarasvat` | any page asserting a cause for the Indus decline | the finding at `MDO-OCC-016`, plus the four counter- and near-neighbour formulations |
| `centuries\|century\|too late\|already empty\|already ruins\|abandoned` intersected with `rigved\|hymn\|vedic\|indus\|harapp\|mohenjo` | any other page excluding something on a Rigveda-versus-Indus date | no further breach |

Counts in this table are `grep`- and `find`-derived, per standing rule 14.
The first pass reported "15 files" for the all-types `mohenjo` pattern; 15
is the `.html`-only figure and 20 is the all-types one.

**Coverage limits, stated as limits and not as assumptions.** This is a text
search over one commit. It finds the claim where it is written in words —
including in `.js` and `.json`, which the corrected pass reads, and where
one of the two most useful findings turned out to live. What it would not
find: a claim made only by a graphic or an SVG label with no text node, a
claim made by a visual property rather than a word (which is a real
mechanism here — see §4), a page not in this repository, and any wording
that shares no search term with the patterns above. The first version of
this section claimed runtime-generated chart captions were unreachable;
they are plain text in `assets/js/` and are now searched. A coverage limit
that describes reachable evidence as unreachable stops the next unit
looking, which is `BF-030`.

## 3. What the sweep found

Twenty-one rows in `03-REGISTERS/site-occurrences-mohenjo-daro.csv` —
14 carrying a breach, 4 counter-occurrences, 2 near neighbours that do not
breach, and 1 adjacent passage on a different explanandum. Counts derived
from the register file, not tallied by hand.

| Where | Rows | Carries |
|---|---|---|
| `dasa-forts-rigveda.html` — **live page**: `<h1>`, `<title>`, five `<meta>` tags, the pull quote at :420, the "already empty" box, the :431–432 summary, the candidate table | 6 breach + 1 counter | breach 1 throughout; breach 2 at :420 |
| `what-survived-the-archive.html:179` — **live, indexed, linked from ≥5 pages** | 1 | breach 2: "the monsoon shift **that ends** Harappan urbanism", bold, unattributed |
| `prototypes/a2-object.html`, `b2-object.html`, `c-semantic.html` | 3 | both breaches, verbatim |
| `research-index.html`, `exhibits.html`, `search-index.json`, `SITE-INVENTORY.md` | 4 | breach 1, as derived surfaces repeating the headline (`DEP-027`) |
| `MELUHHA_TO_KEEZHADI_synthesis.md` | 1 | **counter**: "The Late Harappan decline was not purely environmental" |
| `assets/data/page-evidence.json` C-12, and `when-the-mixing-stopped.html:137` | 2 | **counter**: a chronological-gap exclusion the platform already withdrew — "The chronology settles nothing" |
| `dasa-forts-rigveda.html:548–557` | (counted above) | **counter**: the page's own "that gap is unresolved" |
| `vedic-ritual-economy.html`, `assets/js/artifact-atlas.js:366` | 2 | near neighbours that do **not** breach: "the best current evidence points to", "coincides with deurbanization" |
| `who-writes-the-textbook.html:171` | 1 | adjacent, **different explanandum** — the cause of the Harappa *violence*, not the decline |

The counter-occurrences are why this is a method failure and not a
disagreement about the Bronze Age. The platform holds the careful
formulation in four places, one of them on the offending page, one of them
in a document that denies the pull quote outright, and one of them a
published correction retiring this very reasoning form in another domain.

**One incidental closure.** `CORRECTIONS-PENDING.md` Brief 3 §3.1 records
that the repository could not confirm `dasa-forts-rigveda.html` carries the
headline attributed to it — finding C-6, "Three names for one target", in
`06-BRIEFS/rv01-reconciliation.md` §5. It does, at line 110, and there is no
separate `the-forts` file at the root. Queued as `RA-025` so the caution is
narrowed by the unit that owns it.

## 4. A third failure, found by the sweep and not raised by the owner

`prototypes/b2-object.html:235` heads the box containing both breaches with
the single word **"Established"**. The live page heads the same box "The
Harappan cities were already empty". b2's four other `div.lit` boxes carry
descriptive headings, so the word is an outlier, not a design slot.

The doctrine behind it is stated in `prototypes/README.md` lines 57–58:

> **Lit and ruled** = established here, and inspectable.
> **Dim and unruled** = the field around it, where the answer is not settled.

That assigns evidentiary standing **by CSS class**, so a prototype can
promote a claim without changing a character of its text, and a diff against
the source page would not catch it. The word is the symptom; the doctrine is
the mechanism. Logged as `BF-026`, with `RA-024` widened accordingly.

Two further facts about the set: `prototypes/README.md` says it is "not
merged", and at this commit the files are on `main` — the commit *is* the
merge of PR #3 — carrying `noindex,nofollow` and unlinked from any root
page. Present and unlinked is not unmerged.

---

## 5. The owner's positions

Archived verbatim at
`01-INHERITED/owner-instructions/2026-09-08-mohenjo-daro-bias-audit.md`.
Three claims are taken from the instruction:

| Row | Claim | Where |
|---|---|---|
| `MDO-P-001` | The region referred to contained fortified sites | position 1 |
| `MDO-P-002` | The identification has been institutionally dismissed rather than evidentially refuted | position 2 |
| `MDO-P-003` | The cause of Mohenjo-daro's decline is contested | the premise the second breach is raised on |

All three are `INHERITED-UNVERIFIED`. `MDO-P-003` is not one of the two the
instruction asks for; it is registered because this unit first used it as an
unsourced ground for `BF-025` (`BF-028`), and registering it keeps the
owner's premise visible as a premise.

**MDO-P-001 and MDO-P-002 are two claims of different kinds and are not
merged.** Position 1 is about the Bronze Age, answerable by excavation
reports, gazetteers and dating. Position 2 is about a discipline, answerable
by publication history, review record and citation trail. Under the
negative-evidence standard (§6) Position 2 is an argument from an absence —
the absence of an evidential refutation — and may not be argued from until
the absence is typed: what refutation should exist, who would have produced
it, where it would have been published, whether it was produced, preserved,
published, accessible, and whether we would recognise it if we saw it. Until
then it is untested, not strong.

**Evidential support does not flow between them in either direction**, and
`BR-J-001` says so as its verdict. Fortified sites in the region would not
show a dismissal was institutional. A documented institutional dismissal
would not put a fort in the ground. Merging them lets a claim about the
academy do the work of evidence about the second millennium BCE — the
preferred-counter-narrative failure. Splitting them and then dropping
Position 2 as "not archaeology" is the prestige failure. Both are recorded,
separately, and both are open.

## 6. What this unit did not do

- It did not date the Rigveda, and holds no position on the c. 1500–1200 BCE
  window. That is domain A, now queued in `RESEARCH-QUEUE.md`.
- It did not adjudicate the cause of the Late Harappan decline. The first
  version of `BF-025` did, in one sentence, and that is `BF-029`.
- It did not test either owner position, and neither is gated.
- It did not identify, or refuse to identify, the *púr-* of any passage with
  any site, and it does not register the identification as a hypothesis.
- It wrote no replacement copy and edited no file in `melakeela/site`.

## 7. Corrections after adversarial review

An independent reviewer read the first commit and returned sixteen findings,
four of them blocking. The review is filed at
`04-AUDITS/adversarial-review-mohenjo-daro-2026-09-08.md`. Every finding was
checked against the sources before repair; all four blocking findings held.

| Finding | What was wrong | Logged | Repair |
|---|---|---|---|
| F-1 | `MDO-OCC-014` inserted "and collapse" into a quotation about the Harappa **violence**, changing the explanandum; two downstream findings rested on it | `BF-027` | Row re-quoted and re-typed; `BF-025` rebuilt on other evidence; `IC-J-002` re-derived at MEDIUM |
| F-2 | `BF-025` grounded itself in "the literature treats it as contested" — unsourced, and "contested" as a verdict is rejected reasoning (`R-23`) | `BF-028` | Rebuilt on `SRC-089`-internal material only; the owner's premise registered as `MDO-P-003` with R-23's four tests as its promotion path |
| F-3, F-7, F-8 | Verb set missed "ends"; file set excluded `.js`; counts stated not derived; coverage limit disclaimed reachable material | `BF-030` | Re-swept all file types with a wider verb set; six rows added; every count re-derived; §2 rewritten |
| F-4 | Five sentences adjudicated what the unit said four times it would not — including "Refusing a conquest narrative is right" | `BF-029` | All five removed |
| F-5 | Four locators off by one to three lines; "three social-card meta tags" against six locators | in `BF-030` | Every locator re-checked line by line |
| F-6 | `MDO-OCC-009` registered only the search index's `h` and `t` fields; the `b` field carries 2,400 characters including the chronology material | in `BF-030` | Row expanded |
| F-9 | Each bias row ran one §8 test and excluded the other by assertion | — | Both tests run and both results recorded on `BF-024`, `BF-025`, `BF-026` |
| F-10 | "No register row carries this" stated with no search coverage, against `BF-017`'s control | — | Coverage and absence type stated in both rows |
| F-11 | `BF-026` reached the word "Established" but not the doctrine that produces it | — | `BF-026` and `RA-024` widened to the lit/dim rule |
| F-12, F-13 | `BR-J-001` gave an unregistered claim an endpoint, and let a neighbouring case corroborate across a link whose verdict is that nothing flows | — | `link_to` narrowed; the analogy moved into `MDO-P-002` and typed as an analogy |
| F-14 | Unsupported live copy disposed of as a re-audit gated on work nobody had commissioned | — | `D-053` opened; domain A queued in `RESEARCH-QUEUE.md` |
| F-15 | No dependency rows for nine surfaces carrying three texts | — | `DEP-027`, `DEP-028` |
| F-16 | The owner's positions cited a locator that resolved to this unit's own paraphrase | — | Instruction archived under `01-INHERITED/`; the residual limit is stated there |

**What the repair does not fix.** The first commit's message is in the
history and says "three counter-occurrences" where the register labelled
two, and says "fifteen occurrences" where there are now twenty-one. It is
annotated by the second commit rather than rewritten. And a repair pass
written by the agent that produced the defects is not an independent check
of itself: `RA-026` queues the re-review, and the reviewer asked
specifically to look again at whether `BF-025` survives at the severity it
claims once F-1's leg is removed.
