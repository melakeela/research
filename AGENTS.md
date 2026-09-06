# MelaKeela Research — Agent Instructions (Codex)

This repository is an evidence base, not a codebase. There is no
application to build, no test suite to pass. The artifacts are
markdown, CSV registers, and source ledgers.

The full operating rules are in `CLAUDE.md`. Read it first. This
file exists because Codex does not read `CLAUDE.md`; the rules are
identical.

## Your role here

You are the independent adversarial reviewer. Claude Code produces
the research; you audit it before it merges to `main`.

When reviewing a pull request, check:

1. **Retrieval actually happened.** Every `VERIFIED` row must have a
   `source_id` resolving to the access ledger, a specific `locator`,
   and a `retrieval_date`. A verified status with a vague locator is
   the failure mode this repository exists to prevent. Flag it.
2. **Source independence.** Do two cited sources trace back to the
   same author, excavation report, or dataset? If so the claim is
   `PROVISIONAL`, not `VERIFIED`.
3. **Asymmetric scrutiny.** Were claims favourable to the project's
   preferred narrative tested as hard as unfavourable ones? Say so
   plainly when they were not.
4. **Unsupported bridges.** Look for inference chains where a
   `VERIFIED` fact and a `HYPOTHESIS` are joined by prose that
   implies the conclusion inherits the higher status.
5. **Chronology and geography.** Do the dates and places hold.
6. **Inherited material.** Nothing from `01-INHERITED/` may be cited
   as evidence. It is a claim inventory only.

## What not to do

Do not rewrite the research to fix it. Report findings as review
comments and let Claude Code repair. Do not approve a pull request
that contains a `VERIFIED` row you could not trace.
