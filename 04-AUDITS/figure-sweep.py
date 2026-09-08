#!/usr/bin/env python3
"""
figure-sweep.py — find statistics in the prose and registers that no script
in this repository emits.

Written 2026-09-07 after a hand-written sweep for withdrawn figures failed
twice, the second time missing two numbers inside the very section that
described the sweep failure (BF-026).

The principle: a figure in a register row or a method note is a claim about
a measurement. If no script emits it, either the claim is stale, or it was
computed somewhere that leaves no trace - and both are defects the
source_id rule is meant to prevent.

WHAT THIS TOOL CANNOT DO, and it is the important limitation. `known` is
"every numeric token any script emits anywhere". A figure that has gone
stale in ONE row while remaining live in ANOTHER output is therefore
invisible to it. That is not a corner case: the two withdrawn odds ratios
this tool was written to catch, 15.4 and 3.63, are both still emitted - on
the group-label rows of m8b that RCI-011 abandoned - so this tool would not
have caught them. Answering "does the script this locator names emit this
figure in this role" needs the locator, and nothing here reads locators.
Use this to catch figures no script emits at all. It does not certify a
figure that it passes.

Usage:
    python3 04-AUDITS/figure-sweep.py <outputs-dir> [file ...]

<outputs-dir> holds the TSVs the domain scripts write, and optionally their
captured stdout as .log or .txt - many figures are printed and never
tabulated, and without the logs those all surface as false positives.

Numbers marked as correction history - a cell or line containing
"corrected", "published as", "recorded as", "withdrawn", "first version",
"as then computed" - are not reported, because this repository requires
withdrawn figures to stay visible. CSVs are parsed as CSV so that a marker
in one row cannot suppress a figure in its neighbours.

Exit 0 always. Advisory, not a gate: a legitimate figure can come from a
source rather than a script.
"""
import csv
import os
import re
import sys

DEFAULT_TARGETS = [
    "03-REGISTERS/rigveda-chronology-instruments.csv",
    "03-REGISTERS/rigveda-transmission.csv",
    "04-AUDITS/domain-a-method.md",
    "02-SOURCES/domain-a-manifest-2026-09-07.md",
    "05-HOLDS/HOLD-009-arnold-1905-not-re-readable.md",
    "05-HOLDS/HOLD-010-oldenberg-1888-not-retrieved.md",
    "05-HOLDS/HOLD-011-hellwig-scarlata-widmer-2021.md",
]
HISTORY = re.compile(
    r"corrected|published as|recorded as|withdrawn|first version|"
    r"as then computed|superseded|before BF-", re.I)

# Identifier-shaped strings, stripped before tokenising so that SRC-091 does
# not read as the figure 091. Case-sensitive and word-bounded: an earlier
# version listed bare `D|E|C` under re.I, and `E-\d+` then ate the exponent
# of every p-value in the tree - 4.9e-37 became 4.9 - so the tool could not
# see a p-value at all.
IDENT = re.compile(
    r"\b(?:SRC|RCI|RCT|PUR|DEP|BF|HOLD|IC|RA|HYP|IH|DME|DE|EM|GEO|HYD|RES|VAR|D)-\d+\b"
    r"|§\s*\d+(?:\.\w+)?"
    r"|\b\d{1,2}\.\d{1,3}\.\d{1,3}\b"        # stanza ids 01.001.01
    r"|\b\d\.\d\.\d+\b")                     # sutra ids 4.2.55
YEAR = re.compile(r"^(1[6-9]\d\d|20\d\d|21\d\d)$")
TOKEN = re.compile(r"(?<![\w.,-])("
                   r"\d{1,3}(?:,\d{3})+"          # 12,348
                   r"|\d+\.\d+e[+-]?\d+"          # 4.9e-37
                   r"|\d+\.\d{1,4}"               # 3.58, 0.0233
                   r"|\d{3,}"                     # 18228
                   r")(?![\w.-])")


def interesting(tok):
    """Is this token statistic-shaped enough to be worth reporting?

    An earlier version tested `len(bare.rstrip("0").rstrip(".")) <= 2`,
    which silently discarded 4.0, 250, 29.0, 97.0 and 100 - among them
    Grassmann's Mantel-Haenszel odds ratio of 4.0, the number that demoted
    RCI-012, and the Panini lower bound of 250. Judge by shape, not by the
    length of the string with its zeros removed.
    """
    bare = tok.replace(",", "")
    if "," in tok or "." in tok or "e" in tok.lower():
        return True                       # separators and decimals are figures
    return len(bare) >= 3 and int(bare) >= 100


def emitted(outdir):
    """Every numeric token any script wrote into the outputs directory."""
    seen = set()
    for name in sorted(os.listdir(outdir)):
        if not name.endswith((".tsv", ".log", ".txt")):
            continue
        with open(os.path.join(outdir, name), encoding="utf-8",
                  errors="replace") as f:
            for line in f:
                for cell in re.split(r"[\t\s]+", line.strip()):
                    cell = cell.strip().strip(",;()[]")
                    if not cell:
                        continue
                    seen.add(cell)
                    seen.add(cell.replace(",", ""))
                    for t in TOKEN.findall(cell):
                        seen.add(t)
                        seen.add(t.replace(",", ""))
    widened = set(seen)
    for v in list(seen):
        try:
            f = float(v.replace(",", ""))
        except ValueError:
            continue
        for dp in (0, 1, 2, 3, 4):
            widened.add("%.*f" % (dp, f))
        if f == int(f):
            widened.add("%d" % int(f))
            widened.add("{:,}".format(int(f)))
    return widened


def units(path):
    """(line, text-to-scan, text-to-test-for-history) triples.

    A CSV row is one unit, so that a history marker in one row cannot
    suppress a figure in the row above or below it. Prose wraps, so a
    marker may fall on a neighbouring line - but only the history test
    looks at the neighbours. Scanning the window for figures too would
    report each figure once per line of the window, which is how an
    earlier version turned 38 findings into 130.
    """
    if path.endswith(".csv"):
        with open(path, newline="", encoding="utf-8") as f:
            for n, row in enumerate(csv.reader(f), start=1):
                joined = " ".join(row)
                yield n, joined, joined
    else:
        lines = open(path, encoding="utf-8").read().splitlines()
        for n, line in enumerate(lines, start=1):
            yield n, line, " ".join(lines[max(0, n - 2):n + 2])


def sweep(path, known):
    out = []
    for n, unit, context in units(path):
        if HISTORY.search(context):
            continue
        for tok in TOKEN.findall(IDENT.sub(" ", unit)):
            bare = tok.replace(",", "")
            if "," not in tok and YEAR.match(bare):
                continue                  # a plain 1888 is a date, 1,954 is not
            if tok in known or bare in known:
                continue
            if not interesting(tok):
                continue
            out.append((n, tok, unit.strip()[:110]))
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 0
    outdir = sys.argv[1]
    targets = sys.argv[2:] or DEFAULT_TARGETS
    known = emitted(outdir)
    print("figures emitted by the scripts in %s: %d distinct tokens"
          % (outdir, len(known)))
    total = 0
    for t in targets:
        if not os.path.exists(t):
            print("  (missing: %s)" % t)
            continue
        hits = sweep(t, known)
        total += len(hits)
        if hits:
            print("\n%s — %d figure(s) no script emits:" % (t, len(hits)))
            seen_line = set()
            for n, tok, line in hits:
                key = (n, tok)
                if key in seen_line:
                    continue
                seen_line.add(key)
                print("  %s:%d  %-12s %s" % (t, n, tok, line))
    print("\n%d figure(s) to check by hand. A figure here is not necessarily"
          % total)
    print("wrong - it may come from a source rather than a script - but every")
    print("one needs a reason that is not 'it was true in an earlier run'.")
    print("And a figure NOT here is not thereby current: see the limitation")
    print("at the top of this file.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
