#!/usr/bin/env python3
"""
The keyword tallies quoted in DK-R-009 and DK-R-011, with their patterns.

Written after adversarial review, which found those two VERIFIED rows
saying their tallies were "reproducible from that file" while the keyword
lists existed only in the session that ran them. A reader reconstructing
the patterns got different numbers, which is the correct outcome of an
unreproducible instrument and not a disagreement about the corpus.

What this is: a coarse scan of ONE English translation (Griffith 1890,
SRC-073) for what the passages are about. It is not a semantic analysis
and it does not read the Sanskrit. Passages match more than one category,
so the columns do not sum to the row total.

Source: 03-REGISTERS/domain-k-rigveda-marking-occurrences.csv
Usage: rv-marking-tallies.py [OCCURRENCES_CSV]
"""
import csv, re, sys

SRC = sys.argv[1] if len(sys.argv) > 1 else \
    "03-REGISTERS/domain-k-rigveda-marking-occurrences.csv"

PATTERNS = {
    "√takṣ-": {
        "chariot or car": r"\bcar\b|\bcars\b|chariot",
        "hymn, song or prayer": r"hymn|song|prayer|praise",
        "horse or steed": r"horse|steed",
        "heaven or earth": r"heaven|earth",
        "thunderbolt": r"\bbolt\b|vajra",
        "cup or vessel": r"cup|bowl|vessel|beaker",
        "wood, tree or post": r"wood|tree|forest|post\b",
        "writing, sign or inscription": r"\bwrit|letter|inscri|engrav|carve",
    },
    "ketú-": {
        "banner or ensign": r"banner|ensign|flag",
        "light, ray or dawn": r"light|ray|beam|shine|shining|dawn",
        "writing, sign or inscription": r"\bwrit|letter|inscri|engrav|carve",
    },
    "√piś-": {
        "adorn or deck": r"adorn|ornament|deck|beauti",
        "cattle, cow or herd": r"\bcow\b|kine|cattle|herd",
        "body or limb": r"body|limb|heart|hand",
        "writing, sign or inscription": r"\bwrit|letter|inscri|engrav|carve",
    },
}

rows = list(csv.DictReader(open(SRC, encoding="utf-8")))
for lemma, pats in PATTERNS.items():
    rs = [r for r in rows if r["zurich_lemma"] == lemma]
    print("%s — %d occurrences" % (lemma, len(rs)))
    for label, pat in pats.items():
        hits = [r["stanza"] for r in rs
                if re.search(pat, r["griffith_1890_stanza"], re.I)]
        print("   %-30s %3d   /%s/" % (label, len(hits), pat))
        if label.startswith("writing") and hits:
            print("       %s" % ", ".join(sorted(set(hits))))
