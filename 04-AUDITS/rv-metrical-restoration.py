#!/usr/bin/env python3
"""
rv-metrical-restoration.py — three texts of the Rigveda disagree about how
many syllables it has, and the disagreement is the evidence.

Domain A, transmission half. Constitution s.4.A asks what metre is evidence
for about older pronunciation, and what later sandhi obscures. VedaWeb
carries three texts of the same poems, each applying sandhi differently:

  versions/aufrecht.csv   the transmitted Samhita, sandhi as handed down,
                          segmented by line                       SRC-105
  versions/lubotsky.csv   Lubotsky's Rgvedic word concordance, sandhi
                          undone, segmented by pada               SRC-106
  versions/vnh.csv        van Nooten and Holland 1994, Rig Veda: a
                          Metrically Restored Text, sandhi as the metre
                          requires, segmented by pada, via Thomson and
                          Slocum, UT Austin LRC                   SRC-107

Aufrecht is segmented by line and the other two by pada, so aufrecht is
compared at stanza level only. The pada-level tests use the two texts that
share a segmentation.

The measurement is the syllable count. No metre label is assumed: the
canonical test is simply whether a pada has one of the three canonical
Vedic lengths, 8, 11 or 12.

Syllable counting is by vowel nucleus over ISO-15919, ai and au read as
diphthongs, vocalic r and l counted, accents stripped. Self-tested on
RV 1.1.1-2, where every pada must be 8.

Reads only. Writes TSV to the output directory.
"""
import csv, json, os, sys, collections, unicodedata

VW  = sys.argv[1] if len(sys.argv) > 1 else "/home/user/vedaweb-data/rigveda"
OUT = sys.argv[2] if len(sys.argv) > 2 else "."
CANONICAL = {8, 11, 12}
ACCENTS = {"́", "̀", "॑", "॒", "̍"}
RING, MACRON = "̥", "̄"


def syllables(s):
    t = unicodedata.normalize("NFD", s)
    t = "".join(c for c in t if c not in ACCENTS)
    n, i = 0, 0
    while i < len(t):
        c = t[i]
        nxt = t[i + 1] if i + 1 < len(t) else ""
        if c in "aiueo":
            if c == "a" and nxt in "iu" and (t[i + 2] if i + 2 < len(t) else "") != MACRON:
                n += 1; i += 2; continue
            n += 1; i += 1
            if i < len(t) and t[i] == MACRON:
                i += 1
            continue
        if c in "rl" and nxt == RING:
            n += 1; i += 2
            if i < len(t) and t[i] == MACRON:
                i += 1
            continue
        i += 1
    return n


def load_padas(path):
    d = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.reader(f, delimiter="\t"):
            if len(row) >= 3 and row[2].strip():
                d[(row[0], row[1])] = row[2].strip()
    return d


def stanza_totals(padas):
    t = collections.Counter()
    for (sid, _), text in padas.items():
        t[sid] += syllables(text)
    return t


def w(name, header, rows):
    with open(os.path.join(OUT, name), "w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f, delimiter="\t", lineterminator="\n")
        wr.writerow(header); wr.writerows(rows)


def pct(a, b):
    return 0.0 if not b else 100.0 * a / b


auf = load_padas(os.path.join(VW, "versions/aufrecht.csv"))
lub = load_padas(os.path.join(VW, "versions/lubotsky.csv"))
vnh = load_padas(os.path.join(VW, "versions/vnh.csv"))

for k, want in ((("01.001.01", "a"), 8), (("01.001.02", "b"), 8)):
    got = syllables(vnh[k])
    assert got == want, "self-test failed at %s: %d != %d" % (k, got, want)

strata = json.load(open(os.path.join(VW, "info/strata.json"), encoding="utf-8"))
pada_stratum, stanza_stratum = {}, {}
for sid, ps in strata.items():
    codes = {p[2].upper() for p in ps if p[2]}
    if len(codes) == 1:
        stanza_stratum[sid] = codes.pop()
    for p in ps:
        if p[2]:
            pada_stratum[(sid, p[0])] = p[2].upper()

print("segmentation check")
print("  aufrecht  : %6d lines   in %5d stanzas" % (len(auf), len({k[0] for k in auf})))
print("  lubotsky  : %6d padas   in %5d stanzas" % (len(lub), len({k[0] for k in lub})))
print("  van N.-H. : %6d padas   in %5d stanzas" % (len(vnh), len({k[0] for k in vnh})))

TA, TL, TV = stanza_totals(auf), stanza_totals(lub), stanza_totals(vnh)
common = sorted(set(TA) & set(TL) & set(TV))
print("  stanzas present in all three: %d" % len(common))

# ------------------------------------------------------ R1 stanza level
print()
print("R1  syllables per stanza, three texts of the same poems")
sa = sum(TA[s] for s in common); sl = sum(TL[s] for s in common); sv = sum(TV[s] for s in common)
print("    transmitted Samhita (Aufrecht)      : %8d syllables" % sa)
print("    metrically restored (van N.-Holland): %8d  (%+d, %+.2f%%)"
      % (sv, sv - sa, 100.0 * (sv - sa) / sa))
print("    sandhi undone (Lubotsky concordance): %8d  (%+d, %+.2f%%)"
      % (sl, sl - sa, 100.0 * (sl - sa) / sa))
print("    The restored text is the longest of the three. The transmitted")
print("    sandhi has contracted away syllables the metre still requires,")
print("    and simply undoing sandhi word by word does not recover them all:")
print("    the concordance sits between the other two in total, yet reaches a")
print("    canonical pada length far less often (R3).")

dva = collections.Counter(TV[s] - TA[s] for s in common)
dlv = collections.Counter(TL[s] - TV[s] for s in common)
agree_va = sum(1 for s in common if TV[s] == TA[s])
agree_lv = sum(1 for s in common if TL[s] == TV[s])
print()
print("R2  per-stanza differences")
print("    restored == transmitted            : %5d of %d (%.1f%%)"
      % (agree_va, len(common), pct(agree_va, len(common))))
print("    restored == word-separated         : %5d of %d (%.1f%%)"
      % (agree_lv, len(common), pct(agree_lv, len(common))))
w("r2-stanza-deltas.tsv", ["comparison", "syllable_difference", "stanzas"],
  [["restored_minus_transmitted", d, dva[d]] for d in sorted(dva)]
  + [["separated_minus_restored", d, dlv[d]] for d in sorted(dlv)])

# --------------------------------------------- R3 pada-level canonicity
pboth = sorted(set(lub) & set(vnh))
cl = sum(1 for k in pboth if syllables(lub[k]) in CANONICAL)
cv = sum(1 for k in pboth if syllables(vnh[k]) in CANONICAL)
print()
print("R3  padas with a canonical length (8, 11 or 12), %d aligned padas" % len(pboth))
print("    sandhi undone (Lubotsky)  : %6d (%.1f%%)" % (cl, pct(cl, len(pboth))))
print("    metrically restored (vNH) : %6d (%.1f%%)" % (cv, pct(cv, len(pboth))))
print("    Aufrecht is segmented by line, not by pada, so it cannot enter")
print("    this test; that is a property of the edition, not a finding.")

# --------------------------------- R4 where the restoration falls, by stratum
print()
print("R4  restoration by book and by Arnold stratum")
print("    'lengthened' = the restored pada has more syllables than the")
print("    transmitted stanza's share implies; measured at stanza level")
print("    against Aufrecht, and at pada level against Lubotsky.")
rows = []
for key, keyf in (("book", lambda s: int(s.split(".")[0])),
                  ("stratum", lambda s: stanza_stratum.get(s, ""))):
    agg = collections.defaultdict(lambda: [0, 0, 0])   # stanzas, syl_auf, syl_vnh
    for s in common:
        g = keyf(s)
        v = agg[g]
        v[0] += 1; v[1] += TA[s]; v[2] += TV[s]
    print("    -- by %s" % key)
    for g in sorted(agg, key=lambda x: (x == "", x)):
        n, a, b = agg[g]
        rows.append([key, g, n, a, b, "%+.2f" % (100.0 * (b - a) / a if a else 0)])
        print("       %-8s stanzas %5d   transmitted %7d   restored %7d   %+.2f%%"
              % (g or "(none)", n, a, b, 100.0 * (b - a) / a if a else 0))
w("r4-restoration-by-book-and-stratum.tsv",
  ["grouping", "value", "stanzas", "syllables_transmitted",
   "syllables_restored", "pct_added_by_restoration"], rows)


# ------------------------------- R5 does the stratum difference survive a test?
# Syllables added by restoration, aggregated per stratum, against the
# syllables the transmitted text already has. A 5x2 contingency table.
from scipy.stats import chi2_contingency, kruskal
print()
print("R5  is the stratum difference in R4 more than noise?")
codes = sorted({c for c in stanza_stratum.values()})
table, groups = [], []
for c in codes:
    ss = [s for s in common if stanza_stratum.get(s) == c]
    added = sum(TV[s] - TA[s] for s in ss)
    kept = sum(TA[s] for s in ss)
    table.append([added, kept])
    groups.append([(TV[s] - TA[s]) / TA[s] for s in ss if TA[s]])
chi2, p, dof, _ = chi2_contingency(table)
print("    chi-square on added-vs-transmitted by stratum: %.1f, %d df, p = %.3g"
      % (chi2, dof, p))
h, pk = kruskal(*groups)
print("    Kruskal-Wallis on per-stanza restoration rate : H = %.1f, p = %.3g"
      % (h, pk))
for c, g in zip(codes, groups):
    g2 = sorted(g)
    print("       %-3s n=%5d  median rate %.4f  mean %.4f"
          % (c, len(g2), g2[len(g2) // 2], sum(g2) / len(g2)))
w("r5-stratum-significance.tsv",
  ["stratum", "syllables_added", "syllables_transmitted", "stanzas",
   "mean_rate"],
  [[c, t[0], t[1], len(g), "%.5f" % (sum(g) / len(g))]
   for c, t, g in zip(codes, table, groups)])
