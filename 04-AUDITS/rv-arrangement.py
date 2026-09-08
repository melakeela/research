#!/usr/bin/env python3
"""
rv-arrangement.py — Oldenberg's arrangement rule, tested on the text, and
the book-10 control on the five late-addition instruments.

Domain A, second half. rv-chronology-instruments.py established that all
five late-addition instruments concentrate in Arnold 1905's Popular
stratum. This script asks the question that result cannot answer on its
own: is that agreement anything more than every instrument independently
noticing book 10?

It also tests Oldenberg's arrangement rule against the corpus rather than
taking his verdict on trust. The rule, as stated in Hellwig 2020 s.5.4
reporting Oldenberg 1888, 191-197 and 265: the hymns in each book are
arranged according to the numbers of their stanzas, and hymns violating
that rule represent the youngest layer.

Inputs as in rv-chronology-instruments.py. Reads only.
"""
import csv, json, os, random, sys, collections
from scipy.stats import fisher_exact, chi2_contingency

VW  = sys.argv[1] if len(sys.argv) > 1 else "/home/user/vedaweb-data/rigveda"
OUT = sys.argv[2] if len(sys.argv) > 2 else "."
SEED = 20260907
SCHOLARS = ["grassmann", "oldenberg", "arnold", "wuest", "witzel"]


def w(name, header, rows):
    with open(os.path.join(OUT, name), "w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f, delimiter="\t", lineterminator="\n")
        wr.writerow(header); wr.writerows(rows)


def pct(a, b):
    return 0.0 if not b else 100.0 * a / b


strata = json.load(open(os.path.join(VW, "info/strata.json"), encoding="utf-8"))
props  = json.load(open(os.path.join(VW, "info/stanza_properties.json"), encoding="utf-8"))
props.pop("Book.Hymn.Verse", None)
addr   = json.load(open(os.path.join(VW, "info/addressees.json"), encoding="utf-8"))

stratum = {}
for sid, padas in strata.items():
    codes = {p[2].upper() for p in padas if p[2]}
    if len(codes) == 1:
        stratum[sid] = codes.pop()

marks = {sc: set() for sc in SCHOLARS}
for sid, rec in props.items():
    for sc in rec:
        if sc in marks:
            marks[sc].add(sid)

book = lambda s: int(s.split(".")[0])
hymn = lambda s: "%d.%d" % (int(s.split(".")[0]), int(s.split(".")[1]))

# ---------------------------------------------- M2 book x stratum
codes = sorted(set(stratum.values()))
rows = []
print("M2  book x Arnold 1905 stratum, stanzas, row percent")
print("    book     n  " + "  ".join("%6s" % c for c in codes))
for b in range(1, 11):
    ss = [s for s in strata if book(s) == b and s in stratum]
    d = collections.Counter(stratum[s] for s in ss)
    rows.append([b, len(ss)] + [d[c] for c in codes]
                + ["%.1f" % pct(d[c], len(ss)) for c in codes])
    print("    %-5d %5d  " % (b, len(ss))
          + "  ".join("%5.1f%%" % pct(d[c], len(ss)) for c in codes))
allss = [s for s in strata if s in stratum]
d = collections.Counter(stratum[s] for s in allss)
print("    all   %5d  " % len(allss)
      + "  ".join("%5.1f%%" % pct(d[c], len(allss)) for c in codes))
w("m2-book-by-stratum.tsv",
  ["book", "stanzas"] + ["n_" + c for c in codes] + ["pct_" + c for c in codes],
  rows)

# ------------------------------- M6 the book-10 control on M5
# For each instrument, a 2x2 of marked/unmarked against Popular/not,
# computed over the whole corpus and then inside restricted domains. If
# the association survives inside books 1-9, the instruments are agreeing
# about something finer than "book 10 is late".
def two_by_two(universe, marked):
    a = sum(1 for s in universe if s in marked and stratum.get(s) == "P")
    b = sum(1 for s in universe if s in marked and stratum.get(s) != "P")
    c = sum(1 for s in universe if s not in marked and stratum.get(s) == "P")
    d = sum(1 for s in universe if s not in marked and stratum.get(s) != "P")
    orat, p = fisher_exact([[a, b], [c, d]], alternative="greater")
    return a, b, c, d, orat, p

DOMAINS = {
    "whole corpus":  [s for s in strata if s in stratum],
    "books 1-9":     [s for s in strata if s in stratum and book(s) != 10],
    "book 10 only":  [s for s in strata if s in stratum and book(s) == 10],
    "family 2-7":    [s for s in strata if s in stratum and 2 <= book(s) <= 7],
}
print()
print("M6  is the Popular enrichment anything more than book 10?")
print("    Fisher exact, one-sided, odds ratio for marked-and-Popular")
rows = []
for dom, universe in DOMAINS.items():
    print("    -- %s (n=%d, of which Popular %d)"
          % (dom, len(universe),
             sum(1 for s in universe if stratum.get(s) == "P")))
    for sc in SCHOLARS:
        a, b, c, d, orat, p = two_by_two(universe, marks[sc])
        rows.append([dom, sc, a, b, c, d, "%.2f" % orat, "%.3g" % p,
                     "%.1f" % pct(a, a + b), "%.1f" % pct(c, c + d)])
        print("       %-10s marked %4d of which P %4d (%4.1f%%) | "
              "unmarked P %5.1f%% | OR %5.2f  p=%.2g"
              % (sc, a + b, a, pct(a, a + b), pct(c, c + d), orat, p))
w("m6-popular-enrichment-controlled.tsv",
  ["domain", "scholar", "marked_P", "marked_notP", "unmarked_P",
   "unmarked_notP", "odds_ratio", "fisher_p_onesided",
   "pct_P_among_marked", "pct_P_among_unmarked"], rows)

# ------------------- M8 Oldenberg's arrangement rule, tested directly
# Rule as reported: within a book, hymns are arranged by decreasing number
# of stanzas. VedaWeb's addressees.json already segments each book into
# deity groups; the rule applies within a group. Two cautions are recorded
# in the method note: the group labels are Koelligan's, not the manuscript
# tradition's, and book 7's last group is labelled "appendix", which means
# the segmentation is not innocent of the theory being tested. The runs
# test below therefore also reports a version that ignores the group
# labels entirely and uses maximal runs of identical addressee string.
size = collections.Counter()
for s in strata:
    size[hymn(s)] += 1

def group_seq(b, use_labels=True):
    ks = [k for k in sorted(addr) if k.startswith("%02d." % b)]
    seq, cur, key = [], [], None
    for k in ks:
        g = addr[k][1][1] if use_labels else addr[k][0][1]
        if g != key:
            if cur:
                seq.append((key, cur))
            cur, key = [], g
        cur.append("%d.%d" % (b, int(k.split(".")[1])))
    if cur:
        seq.append((key, cur))
    return seq

def count_ascents(seq):
    """Adjacent pairs inside a group where the later hymn is LONGER."""
    asc = desc = eq = 0
    for _, hs in seq:
        for x, y in zip(hs, hs[1:]):
            if size[y] > size[x]:
                asc += 1
            elif size[y] < size[x]:
                desc += 1
            else:
                eq += 1
    return asc, desc, eq

def monte_carlo(seq, reps=20000, seed=SEED):
    rnd = random.Random(seed)
    obs, _, _ = count_ascents(seq)
    worse = 0
    pool = [[size[h] for h in hs] for _, hs in seq]
    for _ in range(reps):
        a = 0
        for szs in pool:
            v = szs[:]
            rnd.shuffle(v)
            a += sum(1 for x, y in zip(v, v[1:]) if y > x)
        if a <= obs:
            worse += 1
    return obs, (worse + 1) / (reps + 1)

print()
print("M8  Oldenberg's arrangement rule tested on the text")
print("    within deity groups, is hymn length non-increasing?")
rows = []
for use_labels, tag in ((True, "VedaWeb group labels"), (False, "addressee runs")):
    print("    -- segmentation: %s" % tag)
    tot_a = tot_d = tot_e = 0
    for b in range(1, 11):
        seq = group_seq(b, use_labels)
        a, d, e = count_ascents(seq)
        tot_a += a; tot_d += d; tot_e += e
        obs, p = monte_carlo(seq)
        rows.append([tag, b, len(seq), a, d, e, "%.4f" % p])
        print("       book %-3d groups %3d  ascents %3d  descents %3d  "
              "ties %3d  MC p=%.4f" % (b, len(seq), a, d, e, p))
    print("       ALL BOOKS         ascents %3d  descents %3d  ties %3d"
          % (tot_a, tot_d, tot_e))
w("m8-arrangement-runs.tsv",
  ["segmentation", "book", "groups", "ascents", "descents", "ties",
   "monte_carlo_p"], rows)

# Are the hymns that break the rule the ones the scholars call late?
print()
print("M8b are rule-breaking hymns the ones marked as late additions?")
violators, compliant = set(), set()
for b in range(1, 11):
    for _, hs in group_seq(b, True):
        for x, y in zip(hs, hs[1:]):
            (violators if size[y] > size[x] else compliant).add(y)
compliant -= violators
rows = []
for sc in SCHOLARS:
    mh = {hymn(s) for s in marks[sc]}
    a = len(violators & mh); b_ = len(violators - mh)
    c = len(compliant & mh); d = len(compliant - mh)
    orat, p = fisher_exact([[a, b_], [c, d]], alternative="greater")
    rows.append([sc, a, b_, c, d, "%.2f" % orat, "%.3g" % p])
    print("    %-10s violating hymns marked %3d/%3d (%.1f%%)  "
          "compliant marked %3d/%3d (%.1f%%)  OR %.2f  p=%.3g"
          % (sc, a, a + b_, pct(a, a + b_), c, c + d, pct(c, c + d), orat, p))
w("m8b-violators-vs-marks.tsv",
  ["scholar", "violator_marked", "violator_unmarked", "compliant_marked",
   "compliant_unmarked", "odds_ratio", "fisher_p_onesided"], rows)
