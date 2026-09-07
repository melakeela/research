#!/usr/bin/env python3
"""
gatevocab.py — the eligibility-prose to gate_verdict parse, in one place.

Both the migration that wrote `gate_verdict` and the validator that checks it
still agrees with its prose must use the same table. Two copies would drift,
and a drifting parse is worse than none: it would let the machine-readable
verdict and the prose it came from disagree silently, which is the defect the
column was added to remove.
"""
import re

# Longest-first: NOT-ELIGIBLE-SOURCE-BLOCKED must be tried before NOT-ELIGIBLE.
GATE_TERMS = [
    "NOT-ELIGIBLE-SOURCE-BLOCKED",
    "NOT-ELIGIBLE-GATE-FAILED",
    "NOT-A-HYPOTHESIS",
    "NOT-ELIGIBLE",
    "CANNOT-GATE",
    "DEFERRED",
    "ELIGIBLE",
]

# The two eligibility registers were written in different vocabularies for the
# same column. 03-REGISTERS/domain-e-hypothesis-eligibility.csv opens the cell
# with a gate term; 03-REGISTERS/HYPOTHESIS-ELIGIBILITY.csv answers the column
# heading ("eligible for extended analysis?") with YES or NO. That the two
# disagree is itself a defect, recorded as CR-006; here they are read into one
# gate_verdict.
#
# Each entry maps a prose opening to the gate term asserting the SAME
# proposition. Longest-prefix, so "NO - FOR LACK OF SOURCES" cannot be
# swallowed by bare "NO". The reasoning behind the two Brahui rows and the
# Para-Munda row is in 04-AUDITS/MIGRATION-REPORT-2026-09-07.md; both
# adversarial tests were run against this table.
GATE_SYNONYMS = [
    ("NO - FOR LACK OF SOURCES, NOT FOR LACK OF MERIT", "NOT-ELIGIBLE-SOURCE-BLOCKED"),
    ("NO - FOR LACK OF SOURCES", "NOT-ELIGIBLE-SOURCE-BLOCKED"),
    ("NO, PENDING SOURCES", "NOT-ELIGIBLE-SOURCE-BLOCKED"),
    ("YES, WHEN THE BRAHUI LITERATURE IS RETRIEVABLE", "NOT-ELIGIBLE-SOURCE-BLOCKED"),
    ("YES", "ELIGIBLE"),
    ("NO", "NOT-ELIGIBLE"),
]

GATE_VERDICT = set(GATE_TERMS) | {"UNASSIGNED"}


def parse(cell):
    """Return the gate verdict a prose eligibility cell asserts, or UNASSIGNED."""
    upper = (cell or "").strip().upper()
    if not upper:
        return "UNASSIGNED"
    for term in GATE_TERMS:
        if upper.startswith(term):
            return term
    for prose, term in GATE_SYNONYMS:
        if upper.startswith(prose):
            return term
    return "UNASSIGNED"
