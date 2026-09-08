# Status dimensions

One column named `status` was carrying five different things. This file
defines what replaced it, and it is the enumeration
`04-AUDITS/validate-registers.py` enforces. A value not listed here fails
the build.

## The rule that survives everything below

**`evidence_status` is the evidence gate, and it is the only evidence gate.**
No other dimension promotes a claim, and no combination of them does. A row
that is `APPROVED` editorially and `PUBLISHED` publicly and `PROVISIONAL`
evidentially is a `PROVISIONAL` claim. Promotion out of
`INHERITED-UNVERIFIED` still requires a retrieval event logged in
`02-SOURCES/access-ledger.csv`, exactly as `CLAUDE.md` says. Splitting the
column did not create four gates; it stopped four other things pretending to
be one.

## The dimensions

### `evidence_status` — what the evidence supports

The seven values from `CLAUDE.md`, unchanged. Exactly one per claim; no claim
is unstatused.

`VERIFIED` · `PROVISIONAL` · `HYPOTHESIS` · `INHERITED-UNVERIFIED` ·
`REJECTED` · `SUPERSEDED` · `HOLD`

### `interpretive_status` — what has been made of it

| Value | Meaning |
|---|---|
| `UNASSIGNED` | No interpretive standing recorded. The default, and what every migrated row carries. |
| `MEASUREMENT-ONLY` | A measurement. It is not a claim about causes, origins or relationships, and must not be read as one. |
| `PROPOSED` | An interpretation has been offered and rests on named measurements. |
| `CONTESTED` | Two readings of the same evidence are live. |
| `ACCEPTED` | Survived adversarial review. Still bounded by `evidence_status`. |
| `WITHDRAWN` | The interpretation was withdrawn; the underlying evidence may stand. |

`UNASSIGNED` is not a weak `PROPOSED`. It asserts nothing, which is why the
migration could use it on every row without promoting anything.

### `editorial_status` — where it is in review

`UNASSIGNED` · `DRAFT` · `IN-REVIEW` · `CHANGES-REQUIRED` · `APPROVED` ·
`RETIRED`

`APPROVED` here means the adversarial-reviewer loop in `PROGRAMME.md` steps
8–10 closed. It is not a claim about evidence and it is not owner approval.

### `publication_status` — whether the public can see it

`UNASSIGNED` · `PRIVATE` · `PREVIEW` · `PUBLISHED` · `WITHDRAWN` · `ARCHIVED`

This repository is private and publishes nothing; the column exists so that a
claim can be tied to a public page's state once a route registry exists. Every
row currently reads `UNASSIGNED`, which is the truthful value — not `PRIVATE`,
because no one has decided.

### `gate_verdict` — whether a hypothesis may have analytical space

Constitution step 7. Present on the eligibility registers only. This was
previously being written into the claim status vocabulary, which the old
validator permitted; that is corrected.

`UNASSIGNED` · `ELIGIBLE` · `NOT-ELIGIBLE` · `NOT-ELIGIBLE-SOURCE-BLOCKED` ·
`NOT-ELIGIBLE-GATE-FAILED` · `NOT-A-HYPOTHESIS` · `CANNOT-GATE` · `DEFERRED`

`NOT-A-HYPOTHESIS` is not a failure. An attested language family and a
residue are both ineligible for hypothesis gating for opposite reasons, and
the attestation gradient in constitution §4E depends on not confusing them.

### The qualifier columns

| Column | What goes in it |
|---|---|
| `status_reason` | The qualification that used to be jammed into the status cell. Prose belongs here and nowhere else. |
| `superseded_by` | Required and enforced on every `SUPERSEDED` row: the identifier of what replaced it. A supersession that names nothing is a deletion with extra steps. |
| `blocked_by` | On `04-AUDITS/REAUDIT-QUEUE.csv`: what the row is waiting on. Its status stays the status. |

## What is deliberately not split

`02-SOURCES/access-ledger.csv` `access_status` still mixes record standing,
retrieval events and supersession prose. It gained `superseded_by` and nothing
else. Its `VERIFIED` labels the standing of the probe record, not a retrieval
— `SRC-002` is `VERIFIED` and `retrieval_capable: NO`, a verified record of a
failed retrieval — so re-typing those rows onto a retrieval vocabulary would
assert 50 retrievals that never happened. See `MIGRATION-HOLDS.csv` MH-002 and
`CONTRADICTION-REGISTER.csv` CR-004.

`03-REGISTERS/CROSS-DOMAIN-BRIDGES.csv` `verdict` remains free prose. Its
eight values are eight different findings, not eight spellings of one.
MH-001.

## Inheritance disposition

The constitution's §3 vocabulary — `CONFIRMED` `SUPPORTED` `PLAUSIBLE`
`REQUIRES VERIFICATION` `REVISED` `REJECTED` `HELD` — is unchanged by this
split. It remains a disposition recorded *alongside* a status, never in place
of one, and it never promotes a claim by itself. Mapping: reconciliation C-1.
It has no column here because nothing in the tree currently records one; when
something does, it is `inheritance_disposition`, and it is not
`evidence_status`.
