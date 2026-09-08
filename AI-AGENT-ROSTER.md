# AI agent roster

**Eight Claude subagents, an operating structure and a mechanical register
check.** Installed from the `melakeela-team` archive on 2026-09-07 and
reconciled against `CLAUDE.md`, `00-CONTROLLER/METHODOLOGY-CONSTITUTION.md`,
`00-CONTROLLER/CONTROLLER-RECONCILIATION.md`, the inherited handoff and
`04-AUDITS/BIAS-FAILURE-LOG.csv` in the same pass. Renamed from
`README-TEAM.md` on 2026-09-08; the old path resolves through
`00-CONTROLLER/PATH-MIGRATION.csv`.

## What these are, and what they are not

They are **prompts given to Claude subagents**. They are separations of
concern that make the method mechanical, and nothing more.

They are **not** a research team, not scholars, not advisers, not partners,
not community representatives, not employees, and not independent human
reviewers. An agent's output is model-generated and stays model-generated
until a named human reviews it. `adversarial-reviewer` finding nothing is not
peer review; it is one model prompted to attack what another model wrote.

Nobody outside this repository is engaged by anything in it. Scholars named
anywhere in MelaKeela's prose — living or dead, cited approvingly or
critically — are **sources or subjects**, never collaborators:

- **Living scholars** are sources or subjects of critique. Citing someone may
  create a right-of-reply obligation; it never creates an advisory role.
- **Deceased and historical scholars** belong in source genealogy and
  historiography. They cannot be listed as advisers under any framing.
- **Prospective collaborators, reviewers, institutions and funders** named in
  planning documents are targets or leads unless a separate agreement exists.
  Naming a person or an institution in project prose is not permission to
  present a relationship, and no document in this repository establishes one.
- **Communities** — Brahui, Kurukh, Malto, Tamil and others — are not
  reducible to a scholar citation or a generic "community voice". Authority
  requires a named body or person, a scope, a consent basis, a representation
  claim and a withdrawal route. `community-authority.csv` is specified and
  does not yet exist; `D-016` is open on whether reconnection surfaces may
  publish before any community-led work.

The one human authority in this repository is the **owner**. Assistant prose
must not manufacture approval, and `09-DECISIONS/OWNER-DECISIONS.csv` is where
an owner decision actually lives.

```
.claude/agents/                    eight subagent prompts
.claude/settings.json              the PreToolUse hook wiring
.claude/hooks/
  block-push-on-register-failure.sh   local early feedback, not the gate
.github/workflows/
  validate-registers.yml           the gate, once D-050 requires it
00-CONTROLLER/PROGRAMME.md         operating structure, lanes, gates
04-AUDITS/validate-registers.py    mechanical enforcement
04-AUDITS/OVERRIDE-LOG.csv         the only way past a failing check
```

## The eight

Each prompt carries its citations. A constraint in an agent file traces to a
rule in `CLAUDE.md`, the constitution, the reconciliation, the inherited
handoff, or a logged row in `04-AUDITS/BIAS-FAILURE-LOG.csv`. If it cites
nothing, it does not belong in the file — that is the standard the
reconciliation pass applied, and the standard for anything added later.
`00-CONTROLLER/PROGRAMME.md` is authoritative for the lanes; this table
describes them and may not add one.

| Agent | Lane |
|---|---|
| `retriever` | Opens sources, pins hashes, logs access; never interprets |
| `corpus-analyst` | Reproducible counts and distributions; measurements only |
| `chronology-gate` | Steps 2, 3 and 7 — chronology, geography, eligibility verdicts |
| `source-genealogist` | How many independent observations are actually behind this |
| `historiography-auditor` | Step 6 and §4.V — archive, power, credit, custody |
| `adversarial-reviewer` | Tries to make the work fail; has no Write or Edit tool |
| `museum-translator` | Accepted claims into briefs and copy; waits for review |
| `rights-steward` | Rights, consent, custody, institutional claims |

`memory: project` on each writes to `.claude/agent-memory/<name>/`, which is
project-scoped and versionable.

## The register check

`04-AUDITS/validate-registers.py` checks every governed CSV in
`02-SOURCES/`, `03-REGISTERS/`, `04-AUDITS/`, `06-BACKLOG/`, `09-DECISIONS/`
and `00-CONTROLLER/`: identifier uniqueness within a namespace, allowed status
values in each of the four dimensions, locator specificity, claim-to-source
joins against the ledger, source dependency resolution, `SUPERSEDED` rows
pointing at a replacement, `HOLD` rows pointing at a hold file, every `D-`
reference resolving, and release eligibility. `--report` prints the counts it
does not enforce.

**Where the check runs, and what it can actually stop.**

`.github/workflows/validate-registers.yml` runs it on every pull request and
every push to `main`. That is the only place it can see a change made through
the GitHub UI or API, by another git client, or by a session that is not
Claude Code. It becomes binding when the check is required in branch
protection, which only the owner can set: `D-050`.

`.claude/hooks/block-push-on-register-failure.sh` runs it before a `git push`
issued through this session's Bash tool. It is **early feedback, not a gate**.
It cannot see any of the paths above, and it was previously weaker still: any
command whose text contained `MELAKEELA_REGISTER_GATE=off` — including inside
a quoted string or an `echo` — caused it to return no decision at all. That
override is removed (`CR-016`).

**Override.** There is no command-line, environment or comment-based bypass.
The only way past a failing check is a committed row in
`04-AUDITS/OVERRIDE-LOG.csv` naming the actor, the date, the reason, the exact
validation failures it covers, and an expiry date. The hook reads that file
from `HEAD`, not from the working tree, so an override exists only once it is
committed and visible in a diff. An expired row does not apply, and a row does
not cover a failure it does not name. Editing the validator to make failing
rows pass is not an available move.

**The check currently passes.** `04-AUDITS/VALIDATOR-FINDINGS-2026-09-07.md`
and `04-AUDITS/validator-source-id-splitting-2026-09-07.md` describe the tree
and the validator as they stood on 2026-09-07 and are kept as correction
history, not as a description of the present. A passing validator is a floor,
not a warrant: it sees whether a row was written claiming a retrieval, never
whether the retrieval happened.
