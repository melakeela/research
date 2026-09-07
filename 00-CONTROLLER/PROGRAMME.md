# MelaKeela Research Programme — operating structure

This document says how work moves through the repository. CLAUDE.md
says what the rules are; METHODOLOGY-CONSTITUTION.md says why. This
says who does what, in what order, and what has to be true before a
unit of work is finished.

The coordinating session — the one the owner starts — is the
programme director. It does not do research. It routes work to the
team, enforces the gates, and opens the PR. If the director finds
itself writing a register row, it has stopped directing.

## The team

Eight agents in `.claude/agents/`. Each has one lane, one trap it
guards against, and persistent memory. They are not personas. They
are separations of concern that make the method mechanical.

| Agent | Lane | Method steps | Produces |
|---|---|---|---|
| retriever | Opens sources, pins hashes, logs access | 5 (access) | ledger rows, manifests, holds |
| corpus-analyst | Reproducible searches and counts | 4 | measurement rows + scripts |
| chronology-gate | Chronology, geography, hypothesis gating | 2, 3, 7 | eligibility rows, verdicts |
| source-genealogist | Dependency mapping, independence | 5 (genealogy) | dependency rows |
| historiography-auditor | Archive and power, §4.V, both bias tests | 6, 8, 11 | archive-audit rows, category audits |
| adversarial-reviewer | Tries to make the work fail | 8, 13 | review findings, never edits |
| museum-translator | Accepted claims → exhibits, copy, children | 14 | briefs, copy, visual requirements |
| rights-steward | Rights, consent, custody, institutional claims | — | rights rows, consent records |

Two rules about the team:

1. **The reviewer is never the author.** Whatever agent produced a
   register does not review it. The adversarial-reviewer reviews
   everything; the historiography-auditor additionally reviews
   anything touching provenance, credit or living communities.
2. **The translator waits.** Nothing reaches the museum-translator
   until it has passed the adversarial-reviewer. Public copy written
   from unreviewed research is how the current site got 84 pages
   with no documented basis.

## A unit of work

Every investigation, regardless of size, moves through this sequence.
The director may collapse steps for a small unit but records which
were collapsed and why.

```
1. BOUND        director       exact proposition, date range, geography,
                               evidence needed, viable explanations, null
2. RETRIEVE     retriever      every source opened, hashed, logged; blocks
                               typed and held
3. GATE         chronology-    every hypothesis: ELIGIBLE / NOT ELIGIBLE /
                gate           CANNOT GATE — before any analysis
4. MEASURE      corpus-        counts, distributions, concordances; scripts
                analyst        that reproduce them
5. GENEALOGY    source-        how many independent observations; what
                genealogist    depends on what
6. ARCHIVE      historiography who made, recorded, preserved, classified,
                -auditor       got credit; category audit; both bias tests
7. INTERPRET    director       measurements → interpretations, in separate
                               registers, each naming what it rests on and
                               its falsifier
8. REVIEW       adversarial-   the nine checks; findings back to author
                reviewer
9. REPAIR       author         each finding answered or the row downgraded
10. RE-REVIEW   adversarial-   until clean
                reviewer
11. TRANSLATE   museum-        only now; brief names every claim_id and
                translator     the weakest status
12. RIGHTS      rights-steward every asset and institutional claim in the
                               brief
13. RELEASE     director       commit, push, PR with the release template
```

Steps 2–6 run in parallel where they do not depend on each other. Steps
8–10 loop. Nothing skips 8.

## Gates

A unit of work is not finished when its files exist. It is finished
when these are true, and the PR states each:

- **Retrieval gate.** Every VERIFIED row resolves to a ledger row with
  locator and retrieval date. `04-AUDITS/validate-registers.py` passes.
- **Independence gate.** Every VERIFIED claim names its independent
  observation count; single-source claims are PROVISIONAL.
- **Eligibility gate.** No hypothesis received analytical space
  without an eligibility row.
- **Bridge gate.** No inference chain lets a lower status inherit a
  higher one. Checked by the reviewer, stated in the PR.
- **Non-repetition gate.** Nothing on the rejected-reasoning lists
  (chatgpt-project-handoff.md §8 and §16; claude-project-handoff.md
  §3 corrections) has returned.
- **Self-report gate.** The PR summary claims nothing the registers do
  not contain. File and row counts are stated and were counted.
- **Commit gate.** Every unit was pushed as it finished. Uncommitted
  work does not survive a restart, and this project has lost a full
  research release to exactly that.

## The batch sequence

The 89-item backlog runs in the batches the execution prompt
established. Each batch is a set of units; each unit runs the sequence
above. A batch closes with a report of confirmed / corrected /
rejected / held / newly specified / owner decision required.

| Batch | Items | What it establishes |
|---|---|---|
| A | inheritance reconciliation | authoritative files, routes, repository state — separately; historical counts as dated snapshots |
| B | 1–8, 41–46 | truth layer and institutional foundation, in present-state language only |
| C | 9–19 | research programmes, in the dependency order the language pack sets; adversarial review before any claim enters copy |
| D | 20–24, 47–52 | evidence and technical specification, tested against real pilot records |
| E | 25–32, 38–40 | flagship and public-experience specification — the smallest honest visitor loop |
| F | 33–37 | learning, with the pilot chosen by owner decision |
| G | 53–65 | visual system through rendered prototypes, not bulk redesign |
| H | 66–89 | deferred and excluded scope, with trigger conditions so it does not leak |

Batches do not wait on each other unless a dependency says so.
Batch C does not wait for Batch B. Batch E waits for the claims it
needs, not for all of C. The director keeps `RESEARCH-QUEUE.md` as the
one place that says what is running, what is blocked, and on what.

## Escalation

The owner is interrupted only for the categories in CLAUDE.md:
payment or institutional access, lawful acquisition, two consequential
positions both viable, living-community consent, publication approval.
Everything else accumulates in `DECISIONS-NEEDED.md` with a row in
`09-DECISIONS/OWNER-DECISIONS.csv`, and the work continues on the
non-blocked path.

Decisions currently blocking real work, in priority order:

1. Register naming — do the twelve mandated files accumulate under
   their names, or does each domain get its own (D-037)
2. Status dimensions — single column or separated epistemic /
   editorial / publication / product / access (D-039)
3. Atlas site count, currently in an MVP page title while disputed
4. Live-site audit gate — does it precede the research packets (D-035)
5. MVP membership of `before-the-indus`
6. MelaKeela / Veḷi naming architecture
7. Daylight versus near-black visual doctrine

## What "world-class" means here

Not confidence. Not prose. Not being told to act like the leading
scholars. It means that before anything is published, someone whose
only job was to break it has tried and failed, and the record shows
what they tried. The team above is that someone, made structural.
