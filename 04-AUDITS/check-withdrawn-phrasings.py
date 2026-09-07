#!/usr/bin/env python3
"""
check-withdrawn-phrasings.py — stop a retracted claim from living on in prose.

The domain J unit retracted claims in 03-REGISTERS/ four times and left the
same claims standing as findings in 06-BRIEFS/ and 04-AUDITS/ each time. Three
rounds of adversarial review caught it; nothing mechanical did. DJ-001 names
the gap in terms — a byte-identity reproduction "cannot compare prose to
register" — in the very commit that reintroduced the failure, and RA-019 asks
for this check.

WHAT THE FIRST VERSION OF THIS FILE GOT WRONG, MEASURED
-------------------------------------------------------
Version 1 exonerated an occurrence if any "correction marker" appeared within
700 characters. Its docstring claimed the window was "narrow enough that a
marker three paragraphs away does not launder an unqualified assertion." That
was asserted, not tested — the same failure this whole unit is a record of —
and it is false. Run against commit a121e47, the exact tree an independent
reviewer called a blocker, version 1 caught **1 of 9** real regressions.

Worse, it failed hardest where the risk is highest. In the old brief, the §4
assertion "The Rigveda carries the fired/unfired opposition brick technology
turns on" passed because the preceding sentence read "That was never measured,
and it is wrong" — the correction of a DIFFERENT claim. The narration of
correction A exonerated assertion B two sentences later, which is exactly the
mechanism the reviewer had diagnosed in the prose ("§0a bought credibility the
prose then spent"), reproduced inside the tool built to stop it.

Tightening the markers to structured ids only does NOT fix it: still 1 of 9,
because `DJ-009` and `RA-019` appear naturally wherever their own subject is
discussed, which is precisely where the withdrawn phrase also sits. Proximity
cannot distinguish "correcting this occurrence" from "discussing this topic".

WHAT THIS VERSION DOES INSTEAD
------------------------------
Per-occurrence licensing. A withdrawn phrase may appear only if its own
withdrawal id — `W-006`, and no other token — appears within LICENCE_WINDOW
characters. `W-` ids occur nowhere in ordinary prose, so the author must place
one deliberately at each quotation, naming WHICH withdrawal licenses THIS
occurrence. Against a121e47 this catches 9 of 9.

The cost is real and is the point: quoting a retracted claim now takes an
explicit act. That is the correct price for text this repository has now
mis-shipped four times.

A GREEN CHECK IS NOT A SWEPT TREE. This enforces a list, and nothing enforces
that the list is complete: a claim withdrawn without a W- row is invisible
here. The list is maintained by hand, and a control whose invocation is
discretionary is how BF-015's future_control failed.

Matching is whitespace-insensitive, because markdown wraps and a substring
search over raw text sees neither a wrapped quotation nor a wrapped assertion.

Exit 0 if clean, 1 otherwise.
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "04-AUDITS" / "WITHDRAWN-PHRASINGS.csv"

# Tight, because the licence is an explicit token rather than an inference.
LICENCE_WINDOW = 400

# Inherited text is committed as the owner wrote it and is never corrected in
# place (CLAUDE.md, the inheritance rule). The register quotes every phrase by
# construction. NOTHING ELSE IS EXEMPT: version 1 excused BIAS-FAILURE-LOG.csv
# and REAUDIT-QUEUE.csv, which bought one borderline hit and three that would
# have passed anyway — a hole for no benefit, in exactly the files an author
# edits while writing a correction, which is where this unit's discipline
# lapsed every time.
SKIP_DIRS = {"01-INHERITED", ".git", "node_modules", "__pycache__"}
SKIP_FILES = {"WITHDRAWN-PHRASINGS.csv", "check-withdrawn-phrasings.py"}
SUFFIXES = {".md", ".csv", ".py"}

# Ids the withdrawn_by column may name, so the list cannot point at nothing.
WITHDRAWER = re.compile(r"^(BF|RA|DEP|D)-\d+$")


def scan_files():
    """Walk the worktree, not `git ls-files`.

    Version 1 read the index, so a new brief that had not been `git add`ed got
    a free pass — the check would run clean on a tree containing the very file
    it was meant to police.
    """
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or p.suffix not in SUFFIXES:
            continue
        if p.name in SKIP_FILES:
            continue
        if any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts):
            continue
        yield p


def normalise(text):
    """Collapse runs of whitespace, returning the flat text and an offset map.

    Markdown wraps. "the act\n  of building" is the same claim as "the act of
    building" and a substring search over the raw text sees neither — which
    silently exempted a real quotation in this repository, and would equally
    exempt a real assertion. Matching happens on the flattened text; the map
    carries each flat offset back to its original position so line numbers and
    the licence window stay honest.
    """
    out = []
    idx = []
    prev_space = False
    for i, ch in enumerate(text):
        if ch.isspace():
            if prev_space:
                continue
            out.append(" ")
            idx.append(i)
            prev_space = True
        else:
            out.append(ch)
            idx.append(i)
            prev_space = False
    return "".join(out), idx


def main():
    if not REGISTER.exists():
        print("check-withdrawn-phrasings: no register; nothing to enforce")
        return 0
    rules = list(csv.DictReader(open(REGISTER, newline="", encoding="utf-8")))

    failures = []

    # The list must itself resolve: a W- row naming no real withdrawal is a
    # rule nobody can satisfy and nobody can audit. This is FORWARD resolution
    # only. The reverse — that every withdrawal has a W- row — is not
    # mechanisable and is the standing hole this file's docstring names.
    known = set()
    for reg, col in ((ROOT / "04-AUDITS" / "BIAS-FAILURE-LOG.csv", "failure_id"),
                     (ROOT / "04-AUDITS" / "REAUDIT-QUEUE.csv", "reaudit_id"),
                     (ROOT / "02-SOURCES" / "dependency.csv", "dependency_id"),
                     (ROOT / "09-DECISIONS" / "OWNER-DECISIONS.csv",
                      "decision_id")):
        if reg.exists():
            with open(reg, newline="", encoding="utf-8") as f:
                known.update(r[col] for r in csv.DictReader(f) if r.get(col))
    for r in rules:
        wb = r["withdrawn_by"].strip()
        if not WITHDRAWER.match(wb):
            failures.append("WITHDRAWN-PHRASINGS.csv: %s names withdrawn_by "
                            "%r, which is not a BF-/RA-/DEP-/D- identifier"
                            % (r["withdrawal_id"], wb))
        elif wb not in known:
            failures.append("WITHDRAWN-PHRASINGS.csv: %s names withdrawn_by "
                            "%s, which resolves to no row in the bias log, "
                            "re-audit queue, dependency or decisions register"
                            % (r["withdrawal_id"], wb))

    for path in scan_files():
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        flat, omap = normalise(text)
        lowered = flat.lower()
        for rule in rules:
            needle = " ".join(rule["phrase"].split()).lower()
            wid = rule["withdrawal_id"]
            start = 0
            while True:
                i = lowered.find(needle, start)
                if i < 0:
                    break
                start = i + len(needle)
                ctx = flat[max(0, i - LICENCE_WINDOW):
                           i + len(needle) + LICENCE_WINDOW]
                if wid not in ctx:
                    line = text.count("\n", 0, omap[i]) + 1
                    failures.append(
                        "%s:%d  %s\n        withdrawn by %s. To quote it here, "
                        "put %s within %d characters of the phrase; otherwise "
                        "remove it."
                        % (path.relative_to(ROOT), line, repr(rule["phrase"]),
                           rule["withdrawn_by"], wid, LICENCE_WINDOW))

    if failures:
        print("check-withdrawn-phrasings: %d unlicensed restatement(s)"
              % len(failures))
        for f in failures:
            print("  " + f)
        return 1
    print("check-withdrawn-phrasings: %d withdrawn phrasings, every occurrence "
          "licensed by its own W- id." % len(rules))
    print("  A green check is not a swept tree: this enforces the list, and "
          "nothing enforces that the list is complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
