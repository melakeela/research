#!/usr/bin/env python3
"""
Domain A - Rigvedic chronology and transmission. Measurements only.

Runs over the tables built by domain-a-build.py. Every block prints a
labelled measurement; none of them interprets one. Blocks:

  1  corpus shape by book                     (attestation facts)
  2  Arnold's strata against book order       (are they one instrument or two)
  3  the five stanza-level stratifications    (Grassmann, Oldenberg, Arnold
                                               Sketch, Wuest, Witzel)
  4  Oldenberg's Noten as an attention map
  5  arrangement analysis                     (Oldenberg / Pincott principles)
  6  Samhitapatha against the metrically restored text
  7  Padapatha

Ledger: SRC-019 / SRC-059 / SRC-069 through SRC-073.
"""
import sys, os, csv, math, collections, itertools, random

WORK = sys.argv[1] if len(sys.argv) > 1 else "."
csv.field_size_limit(10**7)

def load(name):
    with open(os.path.join(WORK, name), encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))

PAD, STZ, HYM = load("padas.tsv"), load("stanzas.tsv"), load("hymns.tsv")

STRATA = [("A", "Archaic"), ("S", "Strophic"), ("N", "Normal"),
          ("C", "Cretic"),  ("P", "Popular")]
SCHOLARS = ["grassmann", "oldenberg", "arnold", "wuest", "witzel"]
SCHOLAR_SRC = {
    "grassmann": "Grassmann 1876-7 (translation, marked stanzas)",
    "oldenberg": "Oldenberg 1888 Prolegomena / 1909-12 Noten",
    "arnold":    "Arnold 1897 JAOS 18 Sketch of the Historical Grammar",
    "wuest":     "Wuest 1928 Stilgeschichte und Chronologie des Rgveda",
    "witzel":    "Witzel 1995 Rgvedic History, in Erdosy (ed.)",
}

def chisq(obs, exp):
    return sum((o - e) ** 2 / e for o, e in zip(obs, exp) if e > 0)

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

def cramers_v(table):
    """table: dict[row][col] -> count"""
    rows = sorted(table)
    cols = sorted({c for r in table.values() for c in r})
    n = sum(v for r in table.values() for v in r.values())
    rs = {r: sum(table[r].values()) for r in rows}
    cs = {c: sum(table[r].get(c, 0) for r in rows) for c in cols}
    x2 = 0.0
    for r in rows:
        for c in cols:
            e = rs[r] * cs[c] / n
            if e > 0:
                x2 += (table[r].get(c, 0) - e) ** 2 / e
    k = min(len(rows), len(cols)) - 1
    return x2, (len(rows) - 1) * (len(cols) - 1), \
           math.sqrt(x2 / (n * k)) if n and k else 0.0, n

def head(n, t):
    print("\n" + "=" * 74)
    print("BLOCK %s. %s" % (n, t))
    print("=" * 74)

# ------------------------------------------------------------------ 1
head(1, "CORPUS SHAPE BY BOOK (attestation, not date)")
byb = collections.defaultdict(lambda: collections.Counter())
for r in HYM:
    byb[int(r["book"])]["hymns"] += 1
    byb[int(r["book"])]["stanzas"] += int(r["n_stanzas"])
    byb[int(r["book"])]["syllables"] += int(r["syl_vnh_hymn"])
for r in PAD:
    if r["has_vnh"] == "1":
        byb[int(r["book"])]["padas"] += 1
print("%-5s %7s %8s %7s %10s %10s" %
      ("book", "hymns", "stanzas", "padas", "syllables", "syl/stanza"))
tot = collections.Counter()
for b in range(1, 11):
    c = byb[b]; tot.update(c)
    print("%-5d %7d %8d %7d %10d %10.2f" %
          (b, c["hymns"], c["stanzas"], c["padas"], c["syllables"],
           c["syllables"] / c["stanzas"]))
print("%-5s %7d %8d %7d %10d %10.2f" %
      ("all", tot["hymns"], tot["stanzas"], tot["padas"], tot["syllables"],
       tot["syllables"] / tot["stanzas"]))

# ------------------------------------------------------------------ 2
head(2, "ARNOLD'S STRATA AGAINST BOOK ORDER")
tab = collections.defaultdict(collections.Counter)
for r in PAD:
    s = r["stratum"].upper()
    if s:
        tab[int(r["book"])][s] += 1
print("padas per book by stratum, row percentages")
print("%-5s %7s %7s %7s %7s %7s %8s" %
      ("book", "Archaic", "Stroph", "Normal", "Cretic", "Popular", "n"))
for b in range(1, 11):
    n = sum(tab[b].values())
    print("%-5d %6.1f%% %6.1f%% %6.1f%% %6.1f%% %6.1f%% %8d" %
          tuple([b] + [100.0 * tab[b][k] / n for k, _ in STRATA] + [n]))
n_all = sum(sum(tab[b].values()) for b in tab)
base = {k: sum(tab[b][k] for b in tab) / n_all for k, _ in STRATA}
print("corpus  " + "  ".join("%s %.1f%%" % (nm[:4], 100 * base[k])
                             for k, nm in STRATA))
x2, df, v, n = cramers_v({b: dict(tab[b]) for b in tab})
print("\nbook x stratum: chi2 = %.1f on %d df, p = %.3g, Cramer's V = %.3f, n = %d"
      % (x2, df, p_from_chisq(x2, df), v, n))
print("Reading: V is the share of the stratum label that book order alone")
print("already carries. V = 0 would make them independent instruments.")

# how well does book alone predict the stratum of a pada?
maj = {b: max(tab[b].items(), key=lambda kv: kv[1])[0] for b in tab}
correct = sum(tab[b][maj[b]] for b in tab)
biggest = max(sum(tab[b][k] for b in tab) for k, _ in STRATA)
print("majority-stratum-per-book classifier: %.1f%% of padas, against a"
      % (100.0 * correct / n_all))
print("single-label baseline of %.1f%%." % (100.0 * biggest / n_all))

print("\nlower-case (metre-variation-only) stratum codes by book:")
low = collections.Counter()
tot_b = collections.Counter()
for r in PAD:
    if r["stratum"]:
        tot_b[int(r["book"])] += 1
        if r["stratum"].islower():
            low[int(r["book"])] += 1
for b in range(1, 11):
    print("  book %2d  %5d / %5d  %5.1f%%" %
          (b, low[b], tot_b[b], 100.0 * low[b] / tot_b[b]))
print("  corpus   %5d / %5d  %5.1f%%" %
      (sum(low.values()), sum(tot_b.values()),
       100.0 * sum(low.values()) / sum(tot_b.values())))

# ------------------------------------------------------------------ 3
head(3, "THE FIVE STANZA-LEVEL STRATIFICATIONS")
flag = {s: {r["stanza"] for r in STZ if r[s]} for s in SCHOLARS}
for s in SCHOLARS:
    print("%-10s %5d stanzas (%.1f%% of 10552)   %s"
          % (s, len(flag[s]), 100.0 * len(flag[s]) / len(STZ), SCHOLAR_SRC[s]))

print("\npairwise agreement (Jaccard above the diagonal, "
      "overlap count below)")
print("%-11s" % "" + "".join("%11s" % s[:9] for s in SCHOLARS))
for a in SCHOLARS:
    row = "%-11s" % a
    for b in SCHOLARS:
        if a == b:
            row += "%11s" % "-"
        elif SCHOLARS.index(b) > SCHOLARS.index(a):
            j = len(flag[a] & flag[b]) / len(flag[a] | flag[b])
            row += "%11.3f" % j
        else:
            row += "%11d" % len(flag[a] & flag[b])
    print(row)

print("\nphi coefficient over all 10552 stanzas")
print("%-11s" % "" + "".join("%11s" % s[:9] for s in SCHOLARS))
N = len(STZ)
allstz = {r["stanza"] for r in STZ}
for a in SCHOLARS:
    row = "%-11s" % a
    for b in SCHOLARS:
        if a == b:
            row += "%11s" % "-"
            continue
        n11 = len(flag[a] & flag[b]); n10 = len(flag[a] - flag[b])
        n01 = len(flag[b] - flag[a]); n00 = N - n11 - n10 - n01
        den = math.sqrt((n11+n10)*(n01+n00)*(n11+n01)*(n10+n00))
        row += "%11.3f" % ((n11*n00 - n10*n01)/den if den else 0.0)
    print(row)

print("\neach scholar's flagged stanzas against Arnold's METRICAL strata")
print("(stanza-level stratum = the code, MIXED where a stanza's padas differ)")
stz_stratum = {r["stanza"]: r["stratum_stanza"] for r in STZ}
labels = [k for k, _ in STRATA] + ["MIXED"]
base_c = collections.Counter(stz_stratum.get(s, "") for s in allstz)
base_n = sum(base_c[l] for l in labels)
print("%-12s " % "corpus" + "".join("%9s" % l[:7] for l in labels) + "%9s" % "n")
print("%-12s " % "" + "".join("%8.1f%%" % (100.0*base_c[l]/base_n)
                              for l in labels) + "%9d" % base_n)
for s in SCHOLARS:
    c = collections.Counter(stz_stratum.get(x, "") for x in flag[s])
    n = sum(c[l] for l in labels)
    obs = [c[l] for l in labels]
    exp = [base_c[l] * n / base_n for l in labels]
    x2 = chisq(obs, exp)
    print("%-12s " % s + "".join("%8.1f%%" % (100.0*c[l]/n) for l in labels)
          + "%9d" % n + "   chi2=%.1f df=%d p=%.3g"
          % (x2, len(labels)-1, p_from_chisq(x2, len(labels)-1)))

print("\nagreement of each scholar with Arnold's Popular stratum, as a")
print("two-by-two: flagged-late x stanza-is-Popular")
for s in SCHOLARS:
    n11 = sum(1 for x in flag[s] if stz_stratum.get(x) == "P")
    n10 = len(flag[s]) - n11
    n01 = sum(1 for x in allstz
              if stz_stratum.get(x) == "P" and x not in flag[s])
    n00 = N - n11 - n10 - n01
    den = math.sqrt((n11+n10)*(n01+n00)*(n11+n01)*(n10+n00))
    phi = (n11*n00 - n10*n01)/den if den else 0.0
    x2v = N * phi * phi
    print("  %-10s flagged&Popular %4d  flagged&not %4d  phi = %+.3f  "
          "chi2 = %.1f  p = %.3g" %
          (s, n11, n10, phi, x2v, p_from_chisq(x2v, 1)))

print("\nstanzas flagged by how many of the five:")
cnt = collections.Counter(sum(1 for s in SCHOLARS if r[s]) for r in STZ)
for k in sorted(cnt):
    print("  %d of 5 : %5d stanzas" % (k, cnt[k]))
five = {r["stanza"] for r in STZ if sum(1 for s in SCHOLARS if r[s]) == 5}
c5 = collections.Counter(stz_stratum.get(x, "") for x in five)
n5 = sum(c5[l] for l in labels)
print("  the %d flagged by all five, by Arnold stratum: " % len(five)
      + " ".join("%s %.1f%%" % (l[:4], 100.0*c5[l]/n5) for l in labels))

# ------------------------------------------------------------------ 4
head(4, "OLDENBERG'S NOTEN AS AN ATTENTION MAP")
noted = {r["stanza"] for r in STZ if r["oldenberg_noten_refs"]}
print("stanzas carrying at least one page reference in Oldenberg 1909/1912:"
      " %d of %d (%.1f%%)" % (len(noted), N, 100.0*len(noted)/N))
print("%-5s %8s %8s %8s" % ("book", "noted", "stanzas", "share"))
nb = collections.Counter(); sb = collections.Counter()
for r in STZ:
    sb[int(r["book"])] += 1
    if r["oldenberg_noten_refs"]:
        nb[int(r["book"])] += 1
for b in range(1, 11):
    print("%-5d %8d %8d %7.1f%%" % (b, nb[b], sb[b], 100.0*nb[b]/sb[b]))
c = collections.Counter(stz_stratum.get(x, "") for x in noted)
n = sum(c[l] for l in labels)
print("by Arnold stratum: " + " ".join("%s %.1f%%" % (l[:4], 100.0*c[l]/n)
                                       for l in labels))
obs = [c[l] for l in labels]; exp = [base_c[l]*n/base_n for l in labels]
x2 = chisq(obs, exp)
print("against the corpus baseline: chi2 = %.1f on %d df, p = %.3g"
      % (x2, len(labels)-1, p_from_chisq(x2, len(labels)-1)))

# ------------------------------------------------------------------ 5
head(5, "ARRANGEMENT ANALYSIS")
hym = {}
for r in HYM:
    hym[r["hymn_id"]] = r
order = sorted(hym, key=lambda h: (int(hym[h]["book"]), int(hym[h]["hymn"])))

print("A. book size, in the order the collection puts the books")
print("%-5s %7s %8s %10s" % ("book", "hymns", "stanzas", "syllables"))
for b in range(1, 11):
    print("%-5d %7d %8d %10d" %
          (b, byb[b]["hymns"], byb[b]["stanzas"], byb[b]["syllables"]))
fam = [byb[b]["hymns"] for b in range(2, 8)]
print("family books 2-7 hymn counts:", fam,
      "- monotonically increasing:" , all(x < y for x, y in zip(fam, fam[1:])))
fam_s = [byb[b]["stanzas"] for b in range(2, 8)]
print("family books 2-7 stanza counts:", fam_s,
      "- monotonically increasing:", all(x < y for x, y in zip(fam_s, fam_s[1:])))

print("\nB. within-deity-group decreasing length")
print("Runs are maximal blocks of consecutive hymns sharing an addressee")
print("string. Each adjacent pair inside a run is scored: DOWN if the second")
print("hymn is shorter, TIE if equal, UP if longer. Under a random ordering")
print("of a run, DOWN and UP are equally likely.")
print("%-6s %7s %7s %6s %6s %6s %8s" %
      ("book", "runs", "pairs", "DOWN", "TIE", "UP", "DOWN/(D+U)"))
allrun = collections.Counter()
per_book = {}
for b in range(1, 11):
    hs = [h for h in order if int(hym[h]["book"]) == b]
    runs, cur = [], [hs[0]]
    for h in hs[1:]:
        if hym[h]["addressee_en"] == hym[cur[-1]]["addressee_en"]:
            cur.append(h)
        else:
            runs.append(cur); cur = [h]
    runs.append(cur)
    d = t = u = 0
    for run in runs:
        for x, y in zip(run, run[1:]):
            a, c2 = int(hym[x]["n_stanzas"]), int(hym[y]["n_stanzas"])
            if c2 < a: d += 1
            elif c2 == a: t += 1
            else: u += 1
    per_book[b] = (len([r for r in runs if len(r) > 1]), d, t, u)
    allrun["d"] += d; allrun["t"] += t; allrun["u"] += u
    tot_p = d + t + u
    print("%-6d %7d %7d %6d %6d %6d %8s" %
          (b, len([r for r in runs if len(r) > 1]), tot_p, d, t, u,
           "%.3f" % (d / (d + u)) if d + u else "n/a"))
d, t, u = allrun["d"], allrun["t"], allrun["u"]
x2 = (d - u) ** 2 / (d + u)
print("%-6s %7s %7d %6d %6d %6d %8.3f   sign test chi2 = %.1f on 1 df, p = %.3g"
      % ("all", "", d + t + u, d, t, u, d / (d + u), x2, p_from_chisq(x2, 1)))

print("\nC. book 9, arranged by metre then by decreasing length")
b9 = [h for h in order if int(hym[h]["book"]) == 9]
# metre of a hymn = modal syllable count of its VNH padas
syl_by_hymn = collections.defaultdict(collections.Counter)
for r in PAD:
    if r["syl_vnh"]:
        syl_by_hymn["%02d.%03d" % (int(r["book"]), int(r["hymn"]))][
            int(r["syl_vnh"])] += 1
def modal(h):
    c = syl_by_hymn.get(h)
    return c.most_common(1)[0][0] if c else 0
seq = [(h, modal(h), int(hym[h]["n_stanzas"])) for h in b9]
print("  modal pada length of book 9 hymns, in collection order (first 60):")
print("  " + " ".join(str(m) for _, m, _ in seq[:60]))
runs = []
cur = [seq[0]]
for e in seq[1:]:
    if e[1] == cur[-1][1]:
        cur.append(e)
    else:
        runs.append(cur); cur = [e]
runs.append(cur)
print("  book 9 falls into %d maximal runs of one modal pada length;"
      " longest run %d hymns" % (len(runs), max(len(r) for r in runs)))
d = u = t = 0
for run in runs:
    for x, y in zip(run, run[1:]):
        if y[2] < x[2]: d += 1
        elif y[2] == x[2]: t += 1
        else: u += 1
print("  decreasing-length inside those runs: DOWN %d TIE %d UP %d  "
      "DOWN/(D+U) = %.3f" % (d, t, u, d / (d + u) if d + u else 0))

print("\nD. book 10, tested for a break between hymns 84 and 85")
b10 = [h for h in order if int(hym[h]["book"]) == 10]
def blockstats(hs, name):
    st = sum(int(hym[h]["n_stanzas"]) for h in hs)
    sy = sum(int(hym[h]["syl_vnh_hymn"]) for h in hs)
    pop = tri = 0
    for r in PAD:
        hid = "%02d.%03d" % (int(r["book"]), int(r["hymn"]))
        if hid in set(hs):
            if r["stratum"].upper() == "P": pop += 1
            if r["stratum"]: tri += 1
    print("  %-14s hymns %3d  stanzas %4d  syll %6d  syl/stanza %5.2f  "
          "Popular %5.1f%%" % (name, len(hs), st, sy, sy / st,
                               100.0 * pop / tri if tri else 0))
blockstats(b10[:84], "10.001-10.084")
blockstats(b10[84:], "10.085-10.191")
d = u = t = 0
for x, y in zip(b10, b10[1:]):
    a, c2 = int(hym[x]["n_stanzas"]), int(hym[y]["n_stanzas"])
    if c2 < a: d += 1
    elif c2 == a: t += 1
    else: u += 1
print("  book 10 as a whole, adjacent hymn length: DOWN %d TIE %d UP %d"
      % (d, t, u))

print("\nE. book 1, by the poet-group the corpus records")
g1 = collections.OrderedDict()
for h in order:
    if int(hym[h]["book"]) != 1:
        continue
    g1.setdefault(hym[h]["group_en"], []).append(h)
print("  %d poet-groups in book 1" % len(g1))
d = u = t = 0
for g, hs in g1.items():
    for x, y in zip(hs, hs[1:]):
        a, c2 = int(hym[x]["n_stanzas"]), int(hym[y]["n_stanzas"])
        if c2 < a: d += 1
        elif c2 == a: t += 1
        else: u += 1
print("  adjacent hymn length inside a poet-group: DOWN %d TIE %d UP %d  "
      "DOWN/(D+U) = %.3f" % (d, t, u, d / (d + u) if d + u else 0))

# ------------------------------------------------------------------ 6
head(6, "SAMHITAPATHA AGAINST THE METRICALLY RESTORED TEXT")
have = [r for r in STZ if r["auf_vnh_same_skeleton"] != ""]
same = sum(1 for r in have if r["auf_vnh_same_skeleton"] == "1")
print("stanzas with both an Aufrecht and a van Nooten-Holland text: %d"
      % len(have))
print("  identical once accents, spacing and editorial marks are removed: "
      "%d (%.1f%%)" % (same, 100.0 * same / len(have)))
print("  differing in their segment string: %d (%.1f%%)"
      % (len(have) - same, 100.0 * (len(have) - same) / len(have)))

print("\nsyllable count, restored text minus transmitted text, per stanza")
delta = collections.Counter()
for r in have:
    if r["syl_vnh_stanza"] and r["syl_aufrecht_stanza"]:
        delta[int(r["syl_vnh_stanza"]) - int(r["syl_aufrecht_stanza"])] += 1
for k in sorted(delta):
    if delta[k]:
        print("  %+3d syllables : %5d stanzas" % (k, delta[k]))
print("  stanzas where the counts agree: %d (%.1f%%)"
      % (delta[0], 100.0 * delta[0] / sum(delta.values())))

print("\nVNH editorial marks, by book. The key to these marks is NOT in the")
print("retrieved repository; they are counted as marks, not read.")
mk = collections.defaultdict(collections.Counter)
for r in PAD:
    for c in r["vnh_marks"]:
        mk[c][int(r["book"])] += 1
print("%-6s %7s  %s" % ("mark", "padas", "by book 1..10"))
for c in sorted(mk, key=lambda c: -sum(mk[c].values())):
    print("%-6s %7d  %s" % (repr(c), sum(mk[c].values()),
                            " ".join("%d" % mk[c][b] for b in range(1, 11))))

print("\npadas carrying at least one VNH mark, by Arnold stratum")
marked = collections.Counter(); tot_s = collections.Counter()
for r in PAD:
    s = r["stratum"].upper()
    if s and r["has_vnh"] == "1":
        tot_s[s] += 1
        if r["vnh_marks"]:
            marked[s] += 1
for k, nm in STRATA:
    print("  %-9s %5d / %5d  %5.2f%%" %
          (nm, marked[k], tot_s[k], 100.0 * marked[k] / tot_s[k]))
obs = [marked[k] for k, _ in STRATA]
tt = sum(tot_s[k] for k, _ in STRATA); mm = sum(obs)
exp = [tot_s[k] * mm / tt for k, _ in STRATA]
x2 = chisq(obs, exp)
print("  chi2 = %.1f on 4 df, p = %.3g" % (x2, p_from_chisq(x2, 4)))

print("\npadas whose restored syllable count is not 8, 11 or 12")
odd = collections.Counter(); allp = collections.Counter()
for r in PAD:
    if r["syl_vnh"]:
        allp[int(r["book"])] += 1
        if int(r["syl_vnh"]) not in (8, 11, 12):
            odd[int(r["book"])] += 1
for b in range(1, 11):
    print("  book %2d  %5d / %5d  %5.2f%%" %
          (b, odd[b], allp[b], 100.0 * odd[b] / allp[b]))
print("  corpus   %5d / %5d  %5.2f%%" %
      (sum(odd.values()), sum(allp.values()),
       100.0 * sum(odd.values()) / sum(allp.values())))

# ------------------------------------------------------------------ 7
head(7, "PADAPATHA")
pp = [r for r in STZ if r["padapatha"]]
print("stanzas with a padapatha text: %d of %d" % (len(pp), N))
w = sum(int(r["n_padapatha_words"]) for r in pp)
cmpd = sum(int(r["n_padapatha_compounds"]) for r in pp)
print("padapatha word slots: %d; of these %d (%.1f%%) are written with an"
      " internal compound boundary" % (w, cmpd, 100.0 * cmpd / w))
print("\npadapatha word slots per stanza, by book")
print("%-5s %9s %9s %9s %9s" %
      ("book", "stanzas", "words", "words/stz", "compound%"))
for b in range(1, 11):
    rs = [r for r in pp if int(r["book"]) == b]
    ww = sum(int(r["n_padapatha_words"]) for r in rs)
    cc = sum(int(r["n_padapatha_compounds"]) for r in rs)
    print("%-5d %9d %9d %9.2f %8.1f%%" %
          (b, len(rs), ww, ww / len(rs), 100.0 * cc / ww))

# ------------------------------------------------------------------ 8
head(8, "ARNOLD'S STRATA: RAW COUNTS, AND THE STRUCTURAL ZEROS")
print("%-5s" % "book" + "".join("%9s" % nm for _, nm in STRATA) + "%9s" % "n")
for b in range(1, 11):
    n = sum(tab[b].values())
    print("%-5d" % b + "".join("%9d" % tab[b][k] for k, _ in STRATA)
          + "%9d" % n)
print("\nbook/stratum cells that are exactly zero:")
for b in range(1, 11):
    z = [nm for k, nm in STRATA if tab[b][k] == 0]
    if z:
        print("  book %2d has no pada at all in: %s" % (b, ", ".join(z)))
print("A zero cell is not a small count. It says the classification never")
print("assigns that book a pada of that period.")

# ------------------------------------------------------------------ 9
head(9, "HOW MUCH RESTORATION, BY BOOK AND BY STRATUM")
print("Syllables the restored text adds to the transmitted text, per stanza.")
print("%-6s %8s %10s %10s %9s %9s" %
      ("book", "stanzas", "syl_trans", "syl_rest", "added", "added/stz"))
agg = collections.defaultdict(lambda: [0, 0, 0])
for r in STZ:
    if r["syl_vnh_stanza"] and r["syl_aufrecht_stanza"]:
        b = int(r["book"])
        agg[b][0] += 1
        agg[b][1] += int(r["syl_aufrecht_stanza"])
        agg[b][2] += int(r["syl_vnh_stanza"])
for b in range(1, 11):
    n, t, rr = agg[b]
    print("%-6d %8d %10d %10d %9d %9.3f" % (b, n, t, rr, rr - t, (rr - t) / n))
n = sum(a[0] for a in agg.values()); t = sum(a[1] for a in agg.values())
rr = sum(a[2] for a in agg.values())
print("%-6s %8d %10d %10d %9d %9.3f  (%.2f%% of the transmitted count)"
      % ("all", n, t, rr, rr - t, (rr - t) / n, 100.0 * (rr - t) / t))

print("\nsame, by the stanza's Arnold stratum")
agg2 = collections.defaultdict(lambda: [0, 0, 0])
for r in STZ:
    if r["syl_vnh_stanza"] and r["syl_aufrecht_stanza"]:
        agg2[r["stratum_stanza"]][0] += 1
        agg2[r["stratum_stanza"]][1] += int(r["syl_aufrecht_stanza"])
        agg2[r["stratum_stanza"]][2] += int(r["syl_vnh_stanza"])
print("%-10s %8s %10s %9s %9s" %
      ("stratum", "stanzas", "syl_trans", "added", "added/stz"))
for k, nm in STRATA:
    n, t, rr = agg2[k]
    if n:
        print("%-10s %8d %10d %9d %9.3f" % (nm, n, t, rr - t, (rr - t) / n))

print("\nstanzas where the restored text is SHORTER than the transmitted one")
sh = [r for r in STZ if r["syl_vnh_stanza"] and r["syl_aufrecht_stanza"]
      and int(r["syl_vnh_stanza"]) < int(r["syl_aufrecht_stanza"])]
print("  %d stanzas" % len(sh))
print("  by book: " + " ".join("%d:%d" % (b, sum(1 for r in sh
                                                 if int(r["book"]) == b))
                               for b in range(1, 11)))

# ------------------------------------------------------------------ 10
head(10, "THE EIGHT DATES THIS UNIT CAN AND CANNOT SEPARATE")
rows = [
 ("composition", "not datable from anything in this corpus; no absolute "
                 "anchor is present in it"),
 ("attestation", "the corpus as transmitted: every claim in blocks 1-9 is "
                 "an attestation fact"),
 ("copying",     "not represented; no manuscript, no colophon, no scribal "
                 "variant is in the retrieved data"),
 ("redaction",   "block 5 measures redactional arrangement directly; it "
                 "dates nothing, it shows an ordering principle"),
 ("translation", "Grassmann 1876-7, Geldner, Griffith, Renou, Elizarenkova, "
                 "Macdonell, Mueller, Oldenberg: eight translation layers"),
 ("excavation",  "not applicable; there is no excavated Rigveda"),
 ("publication", "Aufrecht 1877; Grassmann 1876-7; Oldenberg 1888/1909/1912; "
                 "Arnold 1897, 1905; Wuest 1928; Witzel 1995; van Nooten and "
                 "Holland 1994; Lubotsky 1997; Zurich 2020; VedaWeb 2020/2023"),
 ("modern interpretation",
                 "the stratum labels, the late-stanza flags and the "
                 "restorations are all modern interpretation, dated to their "
                 "publication and not to the text"),
]
for a, b in rows:
    print("  %-22s %s" % (a, b))
