# MelaKeela Research Programme — operating structure

This document says how work moves through the repository. `CLAUDE.md`
says what the rules are; `METHODOLOGY-CONSTITUTION.md` says why;
`CONTROLLER-RECONCILIATION.md` says which governs where they differ.
This says who does what, in what order, and what has to be true before
a unit of work is finished. It adds no rule of its own: every gate
below cites the document it comes from.

The coordinating session — the one the owner starts — is the programme
director. It does not do research. It routes work to the roster, enforces
the gates, and opens the PR. If the director finds itself writing a
register row, it has stopped directing.

## The AI agent roster

Eight Claude subagents in `.claude/agents/`. Each has one lane, one trap
it guards against, and persistent memory. They are not personas and they
are not people. They are separations of concern that make the method
mechanical. `AI-AGENT-ROSTER.md` states the standing rule: an agent is a
model, its output is model-generated, and no named scholar or historical
intellectual in this repository is a collaborator.

| Agent | Lane | Where the lane comes from | Produces |
|---|---|---|---|
| retriever | Opens sources, pins hashes, logs access | `CLAUDE.md` access ledger and blocked-domain rules; no constitution step (reconciliation §1) | ledger rows, manifests, holds |
| corpus-analyst | Reproducible searches and counts | Step 4; `BF-001`–`BF-006` controls | measurement rows + scripts |
| chronology-gate | Chronology, geography, hypothesis gating | Steps 2, 3, 7, 11, 12; §4.E attestation gradient | eligibility rows, verdicts |
| source-genealogist | Dependency mapping, independence | Step 5; `CLAUDE.md` source independence | dependency rows |
| historiography-auditor | Archive and power, §4.V, both §8 tests | Steps 6, 11; §4.V; §6 absence typing; §7 category audit | archive-audit rows, category audits |
| adversarial-reviewer | Tries to make the work fail | §8; Step 13; `AGENTS.md` | review findings, never edits |
| museum-translator | Accepted claims → briefs, copy, children | Steps 9 and 14, at brief level (reconciliation C-9) | briefs, copy, visual requirements |
| rights-steward | Rights, consent, custody, institutional claims | §12 specification subjects; §4.V custody; `CLAUDE.md` escalation categories | rights rows, consent records |

Two rules about the roster:

1. **The reviewer is never the author.** Whatever agent produced a
   register does not review it. The adversarial-reviewer reviews
   everything; the historiography-auditor additionally reviews anything
   touching provenance, credit or living communities. This is
   `AGENTS.md`'s independence requirement moved earlier: Codex still
   reviews the PR, and finds a record that has already been attacked.
2. **The translator waits.** Nothing reaches the museum-translator
   until it has passed the adversarial-reviewer. Constitution Step 14:
   draft public copy **only from accepted claims**. The inherited
   record shows what happens otherwise — pages built on searches
   that were named as owed and never run, and later downgraded
   (`IH-045`, correction C-25; inherited standing rule 12).

## A unit of work

Every investigation, regardless of size, moves through this sequence.
The director may collapse steps for a small unit but records which were
collapsed and why.

```
1. BOUND        director       exact proposition, date range, geography,
                               evidence needed, viable explanations, null
                               (Step 1)
2. RETRIEVE     retriever      every source opened, hashed, logged; blocks
                               typed and held
3. GATE         chronology-    every hypothesis: ELIGIBLE / NOT-ELIGIBLE /
                gate           NOT-ELIGIBLE-SOURCE-BLOCKED / CANNOT-GATE —
                               before any analysis (Step 7)
4. MEASURE      corpus-        counts, distributions, concordances; scripts
                analyst        that reproduce them
5. GENEALOGY    source-        how many independent observations; what
                genealogist    depends on what
6. ARCHIVE      historiography who made, recorded, preserved, classified,
                -auditor       got credit; category audit; both §8 tests
7. INTERPRET    director       measurements → interpretations, in separate
                               registers, each naming what it rests on and
                               its falsifier (Steps 8, 10, 12)
8. REVIEW       adversarial-   the fourteen checks; findings back to author
                reviewer
9. REPAIR       author         each finding answered or the row downgraded
10. RE-REVIEW   adversarial-   until clean
                reviewer
11. TRANSLATE   museum-        only now; brief names every claim_id and
                translator     the weakest status
12. RIGHTS      rights-steward every asset and institutional claim in the
                               brief
13. RELEASE     director       commit, push, PR — the release gate
```

Steps 2–6 run in parallel where they do not depend on each other. Steps
8–10 loop. Nothing skips 8.

## Gates

A unit of work is not finished when its files exist. It is finished when
these are true, and the PR states each:

- **Retrieval gate.** Every `VERIFIED` row resolves to a ledger row with
  locator and retrieval date (`CLAUDE.md`, the inheritance rule and
  register format). `04-AUDITS/validate-registers.py` passes.
- **Independence gate.** Every `VERIFIED` claim names its independent
  observation count; single-source claims are `PROVISIONAL`
  (`CLAUDE.md`, standing constraints; Step 5).
- **Eligibility gate.** No hypothesis received analytical space without
  an eligibility row, and no space was allocated beyond what the
  evidence supports (Steps 7 and 9).
- **Bridge gate.** No inference chain lets a lower status inherit a
  higher one (Step 10; `AGENTS.md` §4).
- **Absence gate.** Every argument from silence carries §6's record and
  one of the eight absence types.
- **Non-repetition gate.** Nothing on the rejected-reasoning record has
  returned: `01-INHERITED/claude-project-handoff.md` §5.4 (`R-01`–`R-27`),
  §3 (correction history) and §11 (the twenty-six standing rules), plus
  every `REJECTED` row in `03-REGISTERS/`, which is never deleted
  (`CLAUDE.md`, standing constraints).
- **Failure-log gate.** Every applicable `future_control` in
  `04-AUDITS/BIAS-FAILURE-LOG.csv` was obeyed; any new method failure
  has a `BF-` row and its collateral has a `04-AUDITS/REAUDIT-QUEUE.csv`
  row (`CLAUDE.md`, two adversarial tests; constitution §9).
- **Self-report gate.** The PR summary claims nothing the registers do
  not contain. File and row counts are stated and were counted, not
  tallied — inherited standing rule 14 (from C-28, C-34).
- **Commit gate.** Every unit was pushed as it finished. The branch is
  the checkpoint; there is no archive file (`CLAUDE.md`, "Committing";
  reconciliation §4).

## The batch sequence

**Status: proposed, not adopted.** The eight batches below are
transcribed from the "Execution sequence" of
`06-BACKLOG/EXPANSION-PROMPT-2026-09-07.md`. That document is
`INHERITED-UNVERIFIED` and says of itself that its execution sequence is
"a proposal recovered from a chat, not an instruction this repository
has accepted"; the 89-item backlog it sequences is not in the repository
at all (reconciliation C-7). The batches are recorded here so the
proposal is legible, and they become the programme's order only when
**D-014** (commit the backlog and prompt-pack, or declare them
superseded) and **D-008** (which programmes enter Release 1) are
answered. Until then `RESEARCH-QUEUE.md` governs what runs.

| Batch | Items | What it proposes to establish |
|---|---|---|
| A | inheritance reconciliation | authoritative files, current routes and repository state, inventoried separately; historical counts kept as dated snapshots |
| B | 1–8, 41–46 | truth and governance foundation, in truthful present-state institutional language only |
| C | 9–19 | research programmes, in the language pack's dependency order; adversarial review before any claim enters copy |
| D | 20–24, 47–52 | evidence and technical specification, tested against real pilot records |
| E | 25–32, 38–40 | flagship and public-experience specification — the smallest coherent visitor loop |
| F | 33–37 | learning specification, with the pilot chosen by owner decision |
| G | 53–65 | visual system through rendered prototypes, not bulk redesign |
| H | 66–89 | deferred and excluded scope, with trigger conditions so it does not leak |

Batches do not wait on each other unless a dependency says so. Batch C
does not wait for Batch B. Batch E waits for the claims it needs, not
for all of C. The director keeps `RESEARCH-QUEUE.md` as the one place
that says what is running, what is blocked, and on what.

## Escalation

The owner is interrupted only for the five categories in `CLAUDE.md`:
payment or institutional access, a lawful-acquisition question, two
consequential interpretive positions both viable, a living-community
consent question, publication approval. Those get a prose section in
`DECISIONS-NEEDED.md` **and** a row in
`09-DECISIONS/OWNER-DECISIONS.csv`, whose `detail_ref` points at that
section.

Everything else is a standing product, scope or institutional decision
that blocks nothing: it gets a row in `09-DECISIONS/OWNER-DECISIONS.csv`
only, does not go in `DECISIONS-NEEDED.md`, and waits for a release
gate. The CSV is authoritative for the `D-` namespace and for each
decision's status; allocate the next free number from it, never from the
highest number seen in a document. The inherited `HD-01`–`HD-20` series
is a separate namespace with no CSV rows.

The three rows whose `status` is `BLOCKED` — meaning they cannot be
answered until something else lands — are **`D-008`, `D-009` and `D-011`**.
`09-DECISIONS/OWNER-DECISIONS.csv` is authoritative for status; the list
below is a different thing, and was previously presented as though it
were the same one.

Decisions that are `OPEN` and are holding up work in practice, each named
by its actual row:

1. **D-001** — which domains are added to the egress allowlist. Blocks
   every `VERIFIED` promotion that depends on an unreachable source;
   `HOLD-002` (DEDR) is the highest-value single unblock.
2. **D-014** — commit the 89-item v2 backlog and the prompt-pack, or
   declare them superseded. Blocks `06-BACKLOG/BACKLOG-COVERAGE.csv`
   scope columns, and D-008 and D-009 behind it.
3. **D-034** — is 96 the authoritative page count, and what is the atlas
   site count. A disputed site count currently sits in an MVP-rank-3
   page title (`X-01`, `X-02`).
4. **D-032** — does `before-the-indus` launch, or come out of the MVP
   set.
5. **D-004** — what Veḷi principally is. The MelaKeela / Veḷi
   positioning behind it is recorded open at `HD-14`.
6. **D-003** — which literature connectors are enabled.

Three items the received draft of this document listed as blocking are
**not** in that list, and are recorded here as findings rather than
carried:

No identifier is quoted for them, because the identifiers the draft used
do not exist and repeating them would put unresolvable references back
into the tree. The highest allocated decision is `D-046`; take the next
free number from `09-DECISIONS/OWNER-DECISIONS.csv` and never from a
figure quoted in a document, this one included.

- *Register naming — do the twelve mandated files accumulate under their
  names, or does each domain get its own?* The draft attributed this to
  an owner-decision row two past the end of the register. The underlying
  question is real and is answered for now by
  `CONTROLLER-RECONCILIATION.md` C-3, which assigns each of the twelve
  files a home. If the owner wants the domain-file pattern reconsidered,
  it needs a freshly allocated row.
- *Status dimensions — single column, or separated epistemic / editorial
  / publication / product / access?* Attributed to another row past the
  end of the register. The five-dimension proposal comes from
  `06-BACKLOG/EXPANSION-PROMPT-2026-09-07.md`, which is
  `INHERITED-UNVERIFIED`. **Taken on 2026-09-07 and pending owner review
  as `D-046`.** `CLAUDE.md` now mandates `evidence_status` as the single
  evidence gate with `interpretive_status`, `editorial_status`,
  `publication_status` and `gate_verdict` beside it; definitions are in
  `00-CONTROLLER/STATUS-DIMENSIONS.md`. The C-1 disposition is unchanged
  and is still recorded alongside a status, never in place of one. This
  paragraph said the opposite until the row existed, which is the defect
  `CR-014` describes: a rule corrected in one surface and left standing
  in another.
- *Live-site audit gate — does it precede the research packets?*
  Attributed to `D-035`, which is a different decision entirely (where
  the challenged Brahui leave-one-out measurement lives). The audit-first
  ordering is settled inherited discipline, not an open decision: audit
  before build (inherited standing rule 11, from C-26; `S-13`), and
  Version 12 of the site-review running list reverses Version 10 to open
  the programme with a live-site audit
  (`01-INHERITED/site-review/RUNNING-LIST-RECONCILIATION.md`).

The draft also listed "daylight versus near-black visual doctrine" as a
blocking decision. `HD-04` settles a dark ground with grey `#5f6f7a`
meaning NO DATA always, `HD-11` says build the pages first and do not
restyle now, and the luminous/dark reconciliation appears only in an
`INHERITED-UNVERIFIED` expansion prompt. It has no `OWNER-DECISIONS.csv`
row and is not blocking anything in this repository.

## What "world-class" means here

Not confidence. Not prose. Not being told to act like the leading
scholars. It means that before anything is published, someone whose only
job was to break it has tried and failed, and the record shows what they
tried. The team above is that someone, made structural.
