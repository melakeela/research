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
# A YES or NO may carry a condition, and the condition decides the verdict.
# This was a table of literal sentences until adversarial review pointed out
# that only ONE sentence was encoded: "YES, when the Brahui literature is
# retrievable" read SOURCE-BLOCKED, while "YES, when the Kurux literature is
# retrievable" and "YES, pending sources" both read ELIGIBLE. The correction
# the migration report claims - that a conditional answer follows the
# register's stated symmetry rather than its surface grammar - was true of one
# row and of no rule. It is a rule now.
#
# An answer conditional on OBTAINING SOURCES is not eligible today, whichever
# word it opens with: that is what NOT-ELIGIBLE-SOURCE-BLOCKED means, and it
# is why the two Brahui hypotheses land together instead of one being granted
# analytical space over its rival on a difference of wording.
SOURCE_CONDITION = re.compile(
    r"\b(SOURCE|SOURCES|LITERATURE|RETRIEVABLE|RETRIEVAL|RETRIEVED|"
    r"PUBLICATION|EDITION|CORPUS|ACCESS|ACCESSIBLE|DIGITISATION|DIGITIZATION)\b")
CONDITIONAL = re.compile(r"^(YES|NO)\s*[,;:-]\s*(?P<rest>.+)$", re.S)

GATE_SYNONYMS = [
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
    m = CONDITIONAL.match(upper)
    if m:
        rest = m.group("rest")
        if SOURCE_CONDITION.search(rest):
            # Conditional on obtaining sources, whichever word it opens with.
            return "NOT-ELIGIBLE-SOURCE-BLOCKED"
        return "DEFERRED"          # conditional on something else
    for prose, term in GATE_SYNONYMS:
        if upper.startswith(prose) and upper.strip() == prose:
            return term            # a bare YES or NO, with no condition
    return "UNASSIGNED"
