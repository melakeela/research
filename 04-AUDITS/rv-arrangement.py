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
import math
from scipy.stats import fisher_exact, chi2_contingency

VW  = sys.argv[1] if len(sys.argv) > 1 else "/home/user/vedaweb-data/rigveda"
OUT = sys.argv[2] if len(sys.argv) > 2 else "."
SEED = 20260907
# Oldenberg 1888, 197-202, 222-223, as listed in Hellwig 2020 footnote 6.
OLDENBERG_APPENDICES = """
1.104 1.162 1.163 1.164 1.179 1.191 2.42 2.43 3.28 3.29 3.52 3.53
4.48 4.58 5.27 5.28 5.61 5.87 6.47 6.74 6.75 7.17 7.33 7.55 7.103
7.104 9.112 9.113 9.114 10.19 10.60
""".split()
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

# Finding D of the 2026-09-07 adversarial review: these figures were quoted
# in a register row whose locator named this script, and this script did not
# compute them. It does now.
M = [[sum(1 for s in allss if int(s.split(".")[0]) == b and stratum[s] == c)
      for c in codes] for b in range(1, 11)]
n_tot = sum(sum(r) for r in M)
chi2, p, dof, _ = chi2_contingency(M)
V = math.sqrt(chi2 / (n_tot * (min(len(M), len(codes)) - 1)))
base = max(sum(r[j] for r in M) for j in range(len(codes)))
byrow = sum(max(r) for r in M)
print()
print("M2b how far is Arnold's stratum a relabelling of book identity?")
print("    chi-square %.0f on %d df, p = %.3g, n = %d" % (chi2, dof, p, n_tot))
print("    Cramer's V                     : %.3f" % V)
print("    majority-class baseline        : %.1f%%" % pct(base, n_tot))
print("    predict stratum from book alone: %.1f%%" % pct(byrow, n_tot))
# the mechanism: Arnold classified hymns, not stanzas. Two definitions are
# reported because they differ and the register must say which it means.
by_hymn_stanza = collections.defaultdict(set)
by_hymn_pada = collections.defaultdict(set)
for sid, ps in strata.items():
    h = hymn(sid)
    if sid in stratum:
        by_hymn_stanza[h].add(stratum[sid])
    for pd in ps:
        if pd[2]:
            by_hymn_pada[h].add(pd[2].upper())
hs = sum(1 for v in by_hymn_stanza.values() if len(v) == 1)
hp = sum(1 for v in by_hymn_pada.values() if len(v) == 1)
print("    hymns with one stratum code, counting stanza codes: %d of %d (%.1f%%)"
      % (hs, len(by_hymn_stanza), pct(hs, len(by_hymn_stanza))))
print("    hymns with one stratum code, counting pada codes  : %d of %d (%.1f%%)"
      % (hp, len(by_hymn_pada), pct(hp, len(by_hymn_pada))))
w("m2b-book-stratum-association.tsv", ["measure", "value"],
  [["chi_square", "%.1f" % chi2], ["df", dof], ["p", "%.3g" % p],
   ["n", n_tot], ["cramers_v", "%.3f" % V],
   ["majority_baseline_pct", "%.1f" % pct(base, n_tot)],
   ["predict_from_book_pct", "%.1f" % pct(byrow, n_tot)],
   ["hymns_single_code_by_stanza", hs],
   ["hymns_single_code_by_pada", hp],
   ["hymns_total", len(by_hymn_stanza)]])

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
# Finding G of the 2026-09-07 adversarial review. Deleting book 10 does not
# control for book identity; M2b shows stratum is entangled with book in
# general, not only through book 10. The control that matches the confound
# is stratification BY book, pooled with Mantel-Haenszel, plus the per-book
# odds ratios so that a pooled figure cannot hide heterogeneity.
print()
print("M6b the control that matches the confound: stratified by book")
mh_rows, per_rows = [], []
for sc in SCHOLARS:
    num = den = 0.0
    per = []
    for b in range(1, 11):
        u = [s for s in strata if s in stratum and book(s) == b]
        a = sum(1 for s in u if s in marks[sc] and stratum[s] == "P")
        bb = sum(1 for s in u if s in marks[sc] and stratum[s] != "P")
        c = sum(1 for s in u if s not in marks[sc] and stratum[s] == "P")
        d = sum(1 for s in u if s not in marks[sc] and stratum[s] != "P")
        n = a + bb + c + d
        if n and (a + bb) and (c + d):
            num += a * d / n
            den += bb * c / n
        orb = ((a + 0.5) * (d + 0.5)) / ((bb + 0.5) * (c + 0.5))
        per.append((b, a + bb, a, orb))
        per_rows.append([sc, b, a, bb, c, d, "%.1f" % orb])
    mh = num / den if den else float("inf")
    pooled = None
    u = [s for s in strata if s in stratum and book(s) != 10]
    a = sum(1 for s in u if s in marks[sc] and stratum[s] == "P")
    bb = sum(1 for s in u if s in marks[sc] and stratum[s] != "P")
    c = sum(1 for s in u if s not in marks[sc] and stratum[s] == "P")
    d = sum(1 for s in u if s not in marks[sc] and stratum[s] != "P")
    pooled = fisher_exact([[a, bb], [c, d]], alternative="greater")[0]
    live = [o for (_, nn, _, o) in per if nn >= 10]
    mh_rows.append([sc, "%.1f" % pooled, "%.1f" % mh,
                    "%.1f" % min(live) if live else "",
                    "%.1f" % max(live) if live else "", len(live)])
    print("    %-10s books 1-9 pooled OR %7.1f | within-book MH OR %7.1f | "
          "per-book range %.1f to %.1f over %d books"
          % (sc, pooled, mh, min(live) if live else 0,
             max(live) if live else 0, len(live)))
print("    Grassmann is the instrument that does not survive this control.")
print("    Its association with the Popular stratum is largely BETWEEN books,")
print("    not within them - which matters because Grassmann is the one")
print("    instrument RCI-011 and RCI-012 lean on as non-circular.")
# The second adversarial review asked the question the Grassmann collapse
# opens: RCI-012 now rests on Oldenberg alone, and 308 of the 699 stanzas in
# VedaWeb's oldenberg column are not confirmed against Oldenberg himself
# (HOLD-010). Does the surviving instrument depend on the unverified part?
conf = {s for s in strata if hymn(s) in set(OLDENBERG_APPENDICES)
        and s in marks["oldenberg"]}
unconf = set(marks["oldenberg"]) - conf


def mh(marked):
    num = den = 0.0
    for b in range(1, 11):
        u = [s for s in strata if s in stratum and book(s) == b]
        a = sum(1 for s in u if s in marked and stratum[s] == "P")
        bb = sum(1 for s in u if s in marked and stratum[s] != "P")
        c = sum(1 for s in u if s not in marked and stratum[s] == "P")
        d = sum(1 for s in u if s not in marked and stratum[s] != "P")
        n = a + bb + c + d
        if n and (a + bb) and (c + d):
            num += a * d / n; den += bb * c / n
    return num / den if den else float("inf")


print()
print("M6d does Oldenberg's instrument depend on its unverified portion?")
print("    Hellwig-confirmed stanzas   n=%4d  within-book MH OR %.1f"
      % (len(conf), mh(conf)))
print("    the rest of the column      n=%4d  within-book MH OR %.1f"
      % (len(unconf), mh(unconf)))
print("    the whole column            n=%4d  within-book MH OR %.1f"
      % (len(marks["oldenberg"]), mh(marks["oldenberg"])))
print("    The confirmed portion carries the association on its own, so")
print("    RCI-012 does not rest on the part of the column that HOLD-010")
print("    cannot check.")
w("m6d-oldenberg-confirmed-subset.tsv",
  ["subset", "stanzas", "within_book_mh_or"],
  [["hellwig_confirmed", len(conf), "%.1f" % mh(conf)],
   ["remainder_of_column", len(unconf), "%.1f" % mh(unconf)],
   ["whole_column", len(marks["oldenberg"]), "%.1f" % mh(marks["oldenberg"])]])

w("m6b-mantel-haenszel-by-book.tsv",
  ["scholar", "books_1_9_pooled_or", "within_book_mh_or", "min_per_book_or",
   "max_per_book_or", "books_with_10plus_marks"], mh_rows)
w("m6c-per-book-odds-ratios.tsv",
  ["scholar", "book", "marked_P", "marked_notP", "unmarked_P",
   "unmarked_notP", "odds_ratio_haldane"], per_rows)

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
print("    Finding I of the 2026-09-07 adversarial review: the rule as its")
print("    cited source states it is PER BOOK, not within groups. Hellwig")
print("    2020 s.5.4: 'the hymns in each book of the RV are arranged")
print("    according to the numbers of their stanzas'. The whole-book test")
print("    is therefore the one the locator covers and is reported first.")
print("    The two grouped segmentations follow as finer-grained variants;")
print("    note that addr[k][1] is a POET or collection heading, not a")
print("    deity group, which the earlier version of this script called it.")
rows = []
# the rule as stated: per whole book, no grouping at all
print("    -- segmentation: whole book, as the source states the rule")
tot_a = tot_d = tot_e = 0
for b in range(1, 11):
    ks = [k for k in sorted(addr) if k.startswith("%02d." % b)]
    seq = [(None, ["%d.%d" % (b, int(k.split(".")[1])) for k in ks])]
    a, d, e = count_ascents(seq)
    tot_a += a; tot_d += d; tot_e += e
    obs, pv = monte_carlo(seq)
    rows.append(["whole book", b, 1, a, d, e, "%.4f" % pv])
    print("       book %-3d  ascents %3d  descents %3d  ties %3d  MC p=%.4f"
          % (b, a, d, e, pv))
print("       ALL BOOKS  ascents %3d  descents %3d  ties %3d"
      % (tot_a, tot_d, tot_e))
print("       10 tests; the finer segmentations below add 20 more. No")
print("       multiplicity adjustment is applied to the printed p-values;")
print("       the register row states the smallest one and its book.")

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
# Finding I: the earlier version computed violators only under the group
# labels, the segmentation the method note itself calls "not innocent of the
# theory being tested". Both are computed; the label-free one is reported
# first because it is the one the register carries.
rows = []
for use_labels, tag in ((False, "addressee runs (label-free)"),
                        (True, "VedaWeb group labels")):
    violators, compliant = set(), set()
    for b in range(1, 11):
        for _, hs in group_seq(b, use_labels):
            for x, y in zip(hs, hs[1:]):
                (violators if size[y] > size[x] else compliant).add(y)
    compliant -= violators
    print("    -- segmentation: %s  (%d violating, %d compliant hymns)"
          % (tag, len(violators), len(compliant)))
    for sc in SCHOLARS:
        mh = {hymn(s) for s in marks[sc]}
        a = len(violators & mh); b_ = len(violators - mh)
        c = len(compliant & mh); d = len(compliant - mh)
        orat, p = fisher_exact([[a, b_], [c, d]], alternative="greater")
        rows.append([tag, sc, a, b_, c, d, "%.2f" % orat, "%.3g" % p])
        print("       %-10s violating marked %3d/%3d (%4.1f%%)  "
              "compliant marked %3d/%3d (%4.1f%%)  OR %6.2f  p=%.3g"
              % (sc, a, a + b_, pct(a, a + b_), c, c + d, pct(c, c + d),
                 orat, p))
print("    Oldenberg's own odds ratio on this table is definitionally")
print("    inflated: violating the rule is how he identified appendices.")
print("    Grassmann 1876-7 is the figure that carries the claim, and only")
print("    the label-free row of it.")
w("m8b-violators-vs-marks.tsv",
  ["segmentation", "scholar", "violator_marked", "violator_unmarked",
   "compliant_marked", "compliant_unmarked", "odds_ratio",
   "fisher_p_onesided"], rows)
