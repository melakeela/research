# Adversarial review — Mohenjo-daro occurrence sweep, 2026-09-08

**Reviewed:** commit `f587c9a` on `claude/mohenjo-daro-bias-audit-hvap2f`,
the first commit of the unit recorded in
`04-AUDITS/mohenjo-daro-occurrence-sweep-2026-09-08.md`.
**Reviewer:** independent adversarial reviewer, a different agent from the
one that produced the work, with read and search access only. It edited
nothing.
**Verdict returned:** *do not merge.* Four blocking findings, twelve
requiring repair.

Every finding was independently checked against the sources by the author
before repair — the reviewer's assertions were not taken on trust. **All
four blocking findings held.** The corrected re-sweep the review forced then
found five further occurrences the first pass had missed, two of which are
the strongest counter-occurrences in the register.

The dispositions are summarised in §7 of the sweep note. This file records
the findings themselves so the correction history is legible without the
review's originating transcript.

---

## Blocking

**F-1 — a `VERIFIED` row misquoted its own locator, and two findings rested
on it.** `MDO-OCC-014` read "who-writes-the-textbook.html states that the
causes of the post-urban violence **and collapse** are 'Genuinely
contested'". Line 171 reads "The cause of the Harappa violence. Genuinely
contested." Inserting two words changed the explanandum from post-urban
*violence* to urban *decline*. The row also closed the quotation early
without an ellipsis and claimed line 137 carried the same statement, which
it does not. `BF-025` cited it as the platform saying so "twice";
`IC-J-002` rated a contradiction HIGH on "three passages on two other
pages". *Verified: held.* Logged `BF-027`.

**F-2 — "contested" used as a verdict, re-proposing rejected reasoning.**
`BF-025` grounded itself in an unsourced assertion about "the literature",
using a form the project's own correction history deleted: `R-23` in
`01-INHERITED/claude-project-handoff.md` §5.4, restated as standing rule 6
at line 589 — an objection faces four tests, and "Contested" is not a
verdict. `SRC-089`'s ledger row says in terms that it is a source for what
the site *says* and never for whether what it says is true; the row used it
for the second thing. *Verified: held, R-23 and rule 6 both read at their
locators.* Logged `BF-028`.

**F-3 — the sweep missed a live-page occurrence of the pattern it was run to
find.** `what-survived-the-archive.html:179`: "the monsoon shift **that
ends** Harappan urbanism", bold, unattributed, on a page with no `noindex`
linked from at least five others. The first sweep's verb set was
`collapse|decline|abandon|deurban|fell`; "ends" was not in it, while the
method note claimed the pattern was looking for "any other page asserting a
cause for the Indus decline". *Verified: held.* Registered `MDO-OCC-016`;
logged with F-7 and F-8 as `BF-030`.

**F-4 — the unit adjudicated what it said four times it would not.**
`BF-025` contained "vedic-ritual-economy.html holds that line explicitly and
**correctly**. **Refusing a conquest narrative is right.**" — a substantive
position on whether Indo-Aryan speakers destroyed the Indus civilisation,
unsourced, inside the row whose function is the preferred-counter-narrative
test. Four smaller instances in `BF-024`, `IC-J-002`, `MDO-OCC-005` and
`MDO-OCC-014`. *Verified: held.* All five removed; logged `BF-029`.

## Requiring repair

- **F-5** — four locators off by one to three lines (`MDO-OCC-004`, `-006`,
  `-010`, `-011`); "three social-card meta tags" against six locators. Held.
- **F-6** — `MDO-OCC-009` understated its occurrence: the search index's `b`
  field carries 2,400 characters of body text, not just the headline. Held.
  The same finding noted `MDO-OCC-006`'s note asserted the identification is
  a gateable hypothesis in this repository's namespace, which no `HYP-` row
  establishes. Held; removed.
- **F-7** — counts stated rather than derived, against standing rule 14:
  "15 files" was the `.html`-only figure where the note said all files (20);
  "6 places" against seven rows; the commit message's "three
  counter-occurrences" against two labelled. Held.
- **F-8** — the stated coverage limit disclaimed runtime chart captions as
  unreachable when they are plain text in `assets/js/`, which `.js` being
  outside the file set had hidden. Held — and this is where `MDO-OCC-019`
  and, by extension, the `.json` correction record `MDO-OCC-020` were
  found.
- **F-9** — each bias row ran one §8 test and excluded the other by
  assertion. Held. Both now run on `BF-024`, `BF-025` and `BF-026`, and
  both fire on the first two.
- **F-10** — "no register row carries this claim" stated with no search
  coverage, against `BF-017`'s own control. Held.
- **F-11** — `BF-026` reached the word "Established" but not
  `prototypes/README.md` lines 57–58, which assign standing by CSS class
  and which no text diff would catch. Held; `BF-026` and `RA-024` widened.
- **F-12, F-13** — `BR-J-001` let a neighbouring case corroborate across a
  link whose verdict is that nothing flows, and gave an unregistered third
  proposition an endpoint. Held; both repaired.
- **F-14** — unsupported live copy disposed of as a re-audit gated on work
  nobody had commissioned. Held; `D-053` opened and domain A queued.
- **F-15** — no `dependency.csv` rows for nine surfaces carrying three
  texts, so "fifteen occurrences" read as breadth of independent assertion.
  Held; `DEP-027` and `DEP-028`.
- **F-16** — the owner's positions cited a locator resolving to this unit's
  own paraphrase. Held in substance; the instruction is archived under
  `01-INHERITED/` and the residual limit — the transcription is the same
  agent's — is stated there rather than papered over.

## What the reviewer confirmed

- `VERIFIED` is the right status for "page X at line Y carries text Z", and
  the rows are right to say explicitly that the status attaches to the
  occurrence and not to the proposition — *if* the locator resolves.
- `BR-J-001` is genuinely typed and not a label over a merged treatment:
  "the strongest artifact in the commit", with one leak (F-12).
- Standing rule 17 — check the headline for overclaim in the platform's own
  direction as rigorously as for deflection — is obeyed, and that is what
  `BF-024` is.
- Re-running the four exact-string patterns independently returned exactly
  the file sets the register recorded. No occurrence of the sentence itself
  was missed.

## What neither the reviewer nor this unit did

- Neither established whether the Rigvedic dating, the decline cause, or
  either owner position is correct, and no finding above depends on any of
  those.
- Neither diffed the six other visual-doctrine prototypes against their
  source pages (`RA-024`).
- Neither checked whether `CORRECTIONS-PENDING.md` Brief 3 says what
  `BF-024` and `RA-023` claim it says. The reviewer named this as the next
  reviewer's gap; it is folded into `RA-026`.

## Standing

The repair was written by the agent that produced the defects, which is not
an independent check of itself. `RA-026` queues the re-review. The reviewer
stated it would re-review after repair and wanted specifically to look again
at whether `BF-025` survives at the severity it claims once F-1's leg is
removed — on the corrected reading it rests on `MDO-OCC-004`, `-013`, `-018`
and `-019` instead, which is a different and, in the author's view, firmer
base; that view is exactly what the re-review is for.
