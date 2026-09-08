#!/usr/bin/env python3
"""
gatevocab.py — the gate_verdict vocabulary.

**This module no longer infers a verdict from prose, and that is the point.**

It used to. Three versions were tried and all three were wrong in the same
direction. A table of literal sentences encoded one row rather than a rule:
"YES, when the Brahui literature is retrievable" read SOURCE-BLOCKED while
"YES, when the Kurux literature is retrievable" read ELIGIBLE. Generalising it
into a conditional rule was worse — adversarial review showed that
"NO - the hypothesis fails the chronology gate" then read DEFERRED, turning a
gate failure into something that comes back, and "NO - there is no evidence in
the Brahui corpus" read NOT-ELIGIBLE-SOURCE-BLOCKED, whose gloss in this very
register is "NOT FOR LACK OF MERIT" — a rejection on evidence promoted to a
rejection on access, by wording, in the direction constitution §8 exists to
catch. `startswith` also meant that reversing two clauses in one sentence
reversed the verdict.

Inference over a free-text column cannot be made safe here, because the thing
being inferred is whether a hypothesis may have analytical space. So:

  `gate_verdict` is AUTHORED. A person writes one of the terms below into the
  column and the validator checks it is one of them. The eligibility prose
  beside it is commentary and governs nothing.

The cost is that the prose and the verdict can disagree without a machine
noticing, and a reviewer has to read both. That is the honest trade: a wrong
verdict a reviewer can see beats a wrong verdict a parser produced.

The two registers still answer the column in two different vocabularies —
ELIGIBLE/NOT-ELIGIBLE terms in one, YES/NO in the other. That is CR-006 and
MH-003, unresolved, and it is a reason to choose one eligibility authority,
not a reason to bridge them with a guess.
"""

GATE_TERMS = [
    "ELIGIBLE",
    "NOT-ELIGIBLE",
    "NOT-ELIGIBLE-SOURCE-BLOCKED",
    "NOT-ELIGIBLE-GATE-FAILED",
    "NOT-A-HYPOTHESIS",
    "CANNOT-GATE",
    "DEFERRED",
]

GATE_VERDICT = set(GATE_TERMS) | {"UNASSIGNED"}
