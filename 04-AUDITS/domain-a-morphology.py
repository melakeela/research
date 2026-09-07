#!/usr/bin/env python3
"""
Domain A - the Zurich morphological annotation used as its own instrument.

Counts inflectional categories per book and per Arnold stratum. This is the
class of feature Hellwig, Scarlata and Widmer 2021 tested; nothing here
reproduces their test, which controlled for metrical position, prosodic
structure and content. These are the RAW distributions, uncontrolled, and
are labelled as such.

Input: rv_tokens.tsv from 04-AUDITS/rv-token-extract.py
Ledger: SRC-019 / SRC-022 / SRC-059.
"""
import sys, csv, math, collections

SRC = sys.argv[1] if len(sys.argv) > 1 else "rv_tokens.tsv"
STRATA = [("A", "Archaic"), ("S", "Strophic"), ("N", "Normal"),
          ("C", "Cretic"),  ("P", "Popular")]

def chisq(o, e):
    return sum((a - b) ** 2 / b for a, b in zip(o, e) if b > 0)

def p_from_chisq(x2, df):
    if x2 <= 0:
        return 1.0
    if df % 2 == 0:
        k, term, s = df // 2, 1.0, 1.0
        for i in range(1, k):
            term *= (x2 / 2) / i
            s += term
        return math.exp(-x2 / 2) * s
    a, x = df / 2.0, x2 / 2.0
    if x < a + 1:
        ap, ssum, dl = a, 1.0 / a, 1.0 / a
        for _ in range(500):
            ap += 1; dl *= x / ap; ssum += dl
            if abs(dl) < abs(ssum) * 1e-14:
                break
        return 1.0 - ssum * math.exp(-x + a * math.log(x) - math.lgamma(a))
    b, c, d = x + 1 - a, 1e300, 1.0 / (x + 1 - a)
    h = d
    for i in range(1, 500):
        an = -i * (i - a); b += 2
        d = an * d + b;  d = 1e-300 if abs(d) < 1e-300 else d
        c = b + an / c;  c = 1e-300 if abs(c) < 1e-300 else c
        d = 1.0 / d; dl = d * c; h *= dl
        if abs(dl - 1.0) < 1e-14:
            break
    return math.exp(-x + a * math.log(x) - math.lgamma(a)) * h

rows = list(csv.DictReader(open(SRC, encoding="utf-8"), delimiter="\t"))
print("tokens: %d" % len(rows))

def feat(r, key):
    for kv in r["morph"].split("|"):
        if kv.startswith(key + "="):
            return kv.split("=", 1)[1]
    return ""

CATS = [
    ("mood=SBJV",  lambda r: feat(r, "mood") == "SBJV"),
    ("mood=INJ",   lambda r: feat(r, "mood") == "INJ"),
    ("mood=OPT",   lambda r: feat(r, "mood") == "OPT"),
    ("mood=IMP",   lambda r: feat(r, "mood") == "IMP"),
    ("mood=PREC",  lambda r: feat(r, "mood") == "PREC"),
    ("non-fin=INF", lambda r: feat(r, "non-finite") == "INF"),
    ("non-fin=CVB", lambda r: feat(r, "non-finite") == "CVB"),
    ("non-fin=GDV", lambda r: feat(r, "non-finite") == "GDV"),
    ("number=DU",  lambda r: feat(r, "number") == "DU"),
    ("tense=AOR",  lambda r: feat(r, "tense") == "AOR"),
    ("tense=PRF",  lambda r: feat(r, "tense") == "PRF"),
    ("tense=IPRF", lambda r: feat(r, "tense") == "IPRF"),
    ("tense=FUT",  lambda r: feat(r, "tense") == "FUT"),
    ("voice=PASS", lambda r: feat(r, "voice") == "PASS"),
    ("secondary=INT", lambda r: feat(r, "secondary conjugation") == "INT"),
    ("secondary=DES", lambda r: feat(r, "secondary conjugation") == "DES"),
    ("case=VOC",   lambda r: feat(r, "case") == "VOC"),
]

print("\n" + "=" * 78)
print("RATE PER 10,000 TOKENS, BY BOOK  (raw, uncontrolled)")
print("=" * 78)
nb = collections.Counter(int(r["book"]) for r in rows)
print("%-14s" % "category" + "".join("%7d" % b for b in range(1, 11))
      + "%9s %10s" % ("corpus", "chi2 p"))
for name, fn in CATS:
    c = collections.Counter(int(r["book"]) for r in rows if fn(r))
    tot = sum(c.values())
    obs = [c[b] for b in range(1, 11)]
    exp = [nb[b] * tot / len(rows) for b in range(1, 11)]
    x2 = chisq(obs, exp)
    print("%-14s" % name
          + "".join("%7.1f" % (10000.0 * c[b] / nb[b]) for b in range(1, 11))
          + "%9.1f %10.3g" % (10000.0 * tot / len(rows),
                              p_from_chisq(x2, 9)))

print("\n" + "=" * 78)
print("RATE PER 10,000 TOKENS, BY ARNOLD STRATUM  (raw, uncontrolled)")
print("=" * 78)
ns = collections.Counter(r["stratum"].upper() for r in rows
                         if r["stratum"])
tot_s = sum(ns[k] for k, _ in STRATA)
print("%-14s" % "category" + "".join("%10s" % nm for _, nm in STRATA)
      + "%10s" % "chi2 p")
for name, fn in CATS:
    c = collections.Counter(r["stratum"].upper() for r in rows
                            if r["stratum"] and fn(r))
    tot = sum(c[k] for k, _ in STRATA)
    obs = [c[k] for k, _ in STRATA]
    exp = [ns[k] * tot / tot_s for k, _ in STRATA]
    x2 = chisq(obs, exp)
    print("%-14s" % name
          + "".join("%10.1f" % (10000.0 * c[k] / ns[k]) for k, _ in STRATA)
          + "%10.3g" % p_from_chisq(x2, 4))

print("\n" + "=" * 78)
print("LEXICAL AND ANNOTATION SHAPE BY BOOK")
print("=" * 78)
lem = collections.defaultdict(set)
for r in rows:
    lem[int(r["book"])].add(r["lemma"])
print("%-6s %9s %9s %9s" % ("book", "tokens", "lemmas", "tok/lemma"))
for b in range(1, 11):
    print("%-6d %9d %9d %9.2f" % (b, nb[b], len(lem[b]), nb[b] / len(lem[b])))
allm = {r["lemma"] for r in rows}
print("%-6s %9d %9d %9.2f" % ("all", len(rows), len(allm),
                              len(rows) / len(allm)))
uniq = collections.Counter()
seen = collections.defaultdict(set)
for r in rows:
    seen[r["lemma"]].add(int(r["book"]))
for l, bs in seen.items():
    if len(bs) == 1:
        uniq[next(iter(bs))] += 1
print("\nlemmas occurring in one book only:")
for b in range(1, 11):
    print("  book %2d  %5d of %5d (%.1f%%)"
          % (b, uniq[b], len(lem[b]), 100.0 * uniq[b] / len(lem[b])))
