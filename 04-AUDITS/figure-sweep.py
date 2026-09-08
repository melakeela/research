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
source_id rule is meant to prevent. This does not replace reading; it
catches the class of error a hand list cannot, which is the figure you did
not think to look for.

Usage:
    python3 04-AUDITS/figure-sweep.py <outputs-dir> [file ...]

<outputs-dir> is a directory of TSVs produced by the domain scripts. With no
file arguments it sweeps the domain A registers, method note, holds and
manifest.

Numbers explicitly marked as correction history - a sentence containing
"corrected", "published as", "recorded as", "withdrawn", "first version",
"as then computed" - are not reported, because this repository requires
withdrawn figures to stay visible.

Exit 0 always. This is an advisory tool, not a gate: a legitimate figure can
come from a source rather than a script.
"""
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
# Statistic-shaped tokens only. The first version of this pattern reported
# 188 "figures" in the method note, nearly all of them fragments of
# identifiers (SRC-091 -> 091), section numbers and years, which is how a
# tool meant to reduce hand-checking creates more of it.
IDENT = re.compile(r"(?:SRC|RCI|RCT|PUR|DEP|BF|D|HOLD|IC|RA|HYP|IH|DME|E|C)-\d+"
                   r"|§\s*\d+(?:\.\w+)?"
                   r"|\d{1,2}\.\d{1,3}\.\d{1,3}"      # stanza ids 01.001.01
                   r"|\b\d\.\d\.\d+\b", re.I)      # sutra ids 4.2.55
YEAR = re.compile(r"^(1[6-9]\d\d|20\d\d|21\d\d)$")
TOKEN = re.compile(r"(?<![\w.,-])("
                   r"\d{1,3}(?:,\d{3})+"          # 12,348
                   r"|\d+\.\d+e[+-]?\d+"          # 4.9e-37
                   r"|\d+\.\d{1,4}"               # 3.58, 0.0233
                   r"|\d{3,}"                     # 18228
                   r")(?![\w.-])")


def emitted(outdir):
    """Every numeric token any script wrote into the outputs directory."""
    seen = set()
    for name in sorted(os.listdir(outdir)):
        if not name.endswith(".tsv"):
            continue
        with open(os.path.join(outdir, name), encoding="utf-8") as f:
            for line in f:
                for cell in line.rstrip("\n").split("\t"):
                    cell = cell.strip()
                    if not cell:
                        continue
                    seen.add(cell)
                    seen.add(cell.replace(",", ""))
                    for t in TOKEN.findall(cell):
                        seen.add(t)
                        seen.add(t.replace(",", ""))
    # a figure written to 1 dp in prose may be stored to 2 in a TSV
    widened = set(seen)
    for v in list(seen):
        try:
            f = float(v.replace(",", ""))
        except ValueError:
            continue
        for dp in (0, 1, 2, 3, 4):
            widened.add("%.*f" % (dp, f))
        widened.add("%d" % round(f)) if f == int(f) else None
        widened.add("{:,}".format(int(f))) if f == int(f) else None
    return widened


def sweep(path, known):
    out = []
    with open(path, encoding="utf-8") as f:
        text = f.read()
    lines = text.splitlines()
    for n, line in enumerate(lines, start=1):
        # A history marker often falls on the next line in wrapped prose, so
        # test a small window rather than the line alone. Found by running
        # this tool on the method note, where "as then computed, before the
        # counter itself was corrected" wrapped away from its figure.
        window = " ".join(lines[max(0, n - 1):n + 2])
        if HISTORY.search(window):
            continue
        stripped = IDENT.sub(" ", line)
        for tok in TOKEN.findall(stripped):
            if YEAR.match(tok.replace(",", "")):
                continue
            bare = tok.replace(",", "")
            if tok in known or bare in known:
                continue
            if len(bare.rstrip("0").rstrip(".")) <= 2:   # 8, 11, 12, years
                continue
            out.append((n, tok, line.strip()[:110]))
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
            for n, tok, line in hits:
                print("  %s:%d  %-12s %s" % (t, n, tok, line))
    print("\n%d figure(s) to check by hand. A figure here is not necessarily"
          % total)
    print("wrong - it may come from a source rather than a script - but every")
    print("one needs a reason that is not 'it was true in an earlier run'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
