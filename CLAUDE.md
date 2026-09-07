# MelaKeela Research — Operating Controller

This repository is the evidence base for the MelaKeela project.
The website lives in `melakeela/site`. **Never write site code here.**

## What you are doing

Producing verifiable evidence records. Not reports, not summaries,
not synthesis essays. A polished narrative with no register rows
behind it is a failure, not a deliverable.

## Evidence status vocabulary

Every claim carries exactly one status. No claim is unstatused.

| Status | Meaning |
|---|---|
| `VERIFIED` | Re-checked against a named source with locator and retrieval date |
| `PROVISIONAL` | Supported, but by a single source or by dependent sources |
| `HYPOTHESIS` | Proposed, not yet tested |
| `INHERITED-UNVERIFIED` | Carried in from prior chat threads |
| `REJECTED` | Tested and failed |
| `SUPERSEDED` | Replaced; must point to what replaced it |
| `HOLD` | Blocked on source access; record in `05-HOLDS/` |

## The inheritance rule

Everything in `01-INHERITED/` enters as `INHERITED-UNVERIFIED`,
**including anything the handoff files label as verified or
confirmed.** Those handoffs were written by models summarizing
their own prior conversations. No retrieval happened during that
summarizing. Treat every line as a claim to be tested.

Promotion out of `INHERITED-UNVERIFIED` requires an actual
retrieval event logged in `02-SOURCES/access-ledger.csv`.
Argument does not promote a claim. Confidence does not promote
a claim. Only retrieval does.

## Register format

Registers live in `03-REGISTERS/` as CSV, one claim per row:

```
claim_id,claim,status,source_id,locator,retrieval_date,supports_page,notes
```

- `source_id` must resolve to a row in the access ledger.
- `locator` must be specific enough to re-find: page, line, section,
  catalogue number. "See the article" is not a locator.
- `supports_page` ties the claim to the atlas entry or exhibit it
  is meant to feed. Evidence that supports nothing is not collected.

## Standing constraints

- **Source independence.** Two citations tracing to the same author,
  excavation report, or dataset count as one. Record dependency in
  `02-SOURCES/dependency.csv`.
- **No false equivalence.** A contested claim and an established one
  do not get parallel presentation.
- **Chronology and geography gates.** Every claim must survive a date
  check and a place check before it is written down.
- **Correction history is preserved.** Rejected reasoning stays
  visible so it is not re-proposed. Never delete a `REJECTED` row.

  ## Blocked domains

When a retrieval fails at the egress proxy, log it in
02-SOURCES/access-ledger.csv with status EGRESS_BLOCKED, the URL,
and what it was needed for. Do not work around it and do not treat
a WebSearch snippet as a substitute for the source. Collect blocked
domains through the session and list them at the end of the PR
under "Domains requested".

## Committing

Commit and push after every substantive unit of work, not only at
the end of the task. Uncommitted work does not survive a session
restart. If a task produces registers, ledger rows and notes, push
each as it is finished rather than batching them into one final
commit.

## Positions already settled by the owner

Kumari Kandam, Sumerian-Dravidian origin, and Austroasiatic-as-oldest
are **not** working assumptions. They appear only as logged claims
under examination. Do not build arguments on them.

## Stopping and escalation

Do not stop at "sources identified" and hand back a plan. Run the
retrieval. If a source is genuinely unreachable, write a `HOLD`
row naming what is needed and continue with the next item.

Escalate to the owner only for:
- payment or institutional access required
- a lawful-acquisition question
- two consequential interpretive positions both remaining viable
- a living-community consent question
- publication approval

Everything else accumulates in `DECISIONS-NEEDED.md`. Do not
interrupt for anything that can wait for a release gate.

## Work product

Finish a unit of work, commit it, and open a pull request against
`main` with a summary of what was verified, what was rejected, and
what is on hold. The PR is the release gate. Codex reviews it
independently before merge.
