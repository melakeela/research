#!/usr/bin/env python3
"""
check-withdrawn-phrasings.py — stop a retracted claim from living on in prose.

The domain J unit retracted claims in 03-REGISTERS/ four times and left the
same claims standing as findings in 06-BRIEFS/ and 04-AUDITS/ each time. Three
rounds of adversarial review caught it; nothing mechanical did. DJ-001 names
the gap in terms — a byte-identity reproduction "cannot compare prose to
register" — in the very commit that reintroduced the failure, and RA-019 asks
for this check.

The rule this enforces: a phrase listed in 04-AUDITS/WITHDRAWN-PHRASINGS.csv
may appear ONLY where the surrounding text also names what withdrew it. A
correction, a bias-log entry or a method note quoting the old wording is fine
and is the point of keeping correction history visible (CLAUDE.md, standing
constraints). An unqualified restatement is not.

Exit 0 if clean, 1 with the offending file, line and phrase otherwise.

Deliberately dumb: substring matching over tracked text, a fixed context
window, no parsing. A check that is easy to reason about gets run; a clever one
gets skipped, and skipped is how BF-015's future_control failed.
"""
import csv
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "04-AUDITS" / "WITHDRAWN-PHRASINGS.csv"

# Characters either side of a hit in which an exonerating marker may appear.
# Wide enough for a CSV notes cell, narrow enough that a marker three
# paragraphs away does not launder an unqualified assertion.
WINDOW = 700

# Never scanned: inherited text is committed as the owner wrote it and is
# never corrected in place (CLAUDE.md, the inheritance rule); the withdrawal
# register itself quotes every phrase by construction; and the bias log and
# re-audit queue exist precisely to hold retracted wording, so quoting it there
# is their function rather than a lapse. Exempting those two whole files is a
# real weakening and is stated here rather than hidden: an unqualified
# restatement inside BIAS-FAILURE-LOG.csv would not be caught.
SKIP_DIRS = {"01-INHERITED", ".git", "node_modules", "__pycache__"}
SKIP_FILES = {"WITHDRAWN-PHRASINGS.csv", "check-withdrawn-phrasings.py",
              "BIAS-FAILURE-LOG.csv", "REAUDIT-QUEUE.csv"}
SUFFIXES = {".md", ".csv", ".py"}


def tracked_files():
    out = subprocess.run(["git", "-C", str(ROOT), "ls-files"],
                         capture_output=True, text=True, check=True).stdout
    for line in out.splitlines():
        p = ROOT / line
        if p.suffix not in SUFFIXES:
            continue
        if p.name in SKIP_FILES:
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        yield p


def markers(row):
    """Tokens whose presence near a hit marks it as a correction, not a claim."""
    out = {row["withdrawn_by"]}
    out.update(x.strip() for x in row["superseded_by"].split(";") if x.strip())
    out.update({row["withdrawal_id"], "WITHDRAWN", "withdrawn", "retracted",
                "CORRECTED", "corrected", "no longer", "was wrong",
                "is wrong", "false", "struck", "supplement",
                # a register row narrating its own revision history
                "Version 1", "Version 2", "failed re-review", "earlier version",
                "this row earlier", "until the second review",
                "until the third review", "quoted here as the error"})
    return {m for m in out if m}


def main():
    if not REGISTER.exists():
        print("check-withdrawn-phrasings: no register; nothing to enforce")
        return 0
    rules = list(csv.DictReader(open(REGISTER, newline="", encoding="utf-8")))
    failures = []
    for path in tracked_files():
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        lowered = text.lower()
        for rule in rules:
            phrase = rule["phrase"]
            needle = phrase.lower()
            start = 0
            while True:
                i = lowered.find(needle, start)
                if i < 0:
                    break
                start = i + len(needle)
                ctx = text[max(0, i - WINDOW): i + len(needle) + WINDOW]
                if not any(m in ctx for m in markers(rule)):
                    line = text.count("\n", 0, i) + 1
                    failures.append(
                        "%s:%d  %s  — withdrawn by %s (%s), and nothing in "
                        "context marks this as a correction"
                        % (path.relative_to(ROOT), line, repr(phrase),
                           rule["withdrawn_by"], rule["withdrawal_id"]))
    if failures:
        print("check-withdrawn-phrasings: %d unqualified restatement(s)"
              % len(failures))
        for f in failures:
            print("  " + f)
        return 1
    print("check-withdrawn-phrasings: all %d withdrawn phrasings appear only "
          "in correcting context" % len(rules))
    return 0


if __name__ == "__main__":
    sys.exit(main())
