#!/usr/bin/env python3
"""
rv-chronology-instruments.py — measure the Rigvedic relative-chronology
instruments against one another.

Domain A. The repository's chronological claims all read through Arnold's
metrical strata (DEP-001, PUR-013, PUR-026). This script asks what happens
when instruments that are not Arnold are applied to the same text.

Inputs, all local, all pinned:
  rigveda/info/strata.json            Arnold 1905, per pada          SRC-023
  rigveda/info/stanza_properties.json five scholars, per stanza      SRC-090
  rigveda/info/addressees.json        Koelligan 2020, per hymn       SRC-092
  rv_tokens.tsv                       Zurich token layer             SRC-019/022
  Oldenberg's 31 appendix hymns       Hellwig 2020 fn. 6             SRC-094

Legend for stanza_properties (SRC-091, VedaWebProject/vedaweb @ f6f8400,
resources/help/lateAdditions.md): uppercase = the author judged the stanza
certainly a late addition, lowercase = may/might be; Arnold's 1897 Sketch
distinguishes two phases of additions, C1 and C2.

Legend for strata.json (PUR-011, Arnold 1905 Appendix IV s.265): A Archaic,
S Strophic, N Normal, C Cretic, P Popular; lowercase = the period is
indicated by metrical variations alone.

Writes TSV tables to the output directory and prints a summary. Reads only.
"""
import csv, json, math, os, re, sys, collections

VW  = sys.argv[1] if len(sys.argv) > 1 else "/home/user/vedaweb-data/rigveda"
TOK = sys.argv[2] if len(sys.argv) > 2 else "rv_tokens.tsv"
OUT = sys.argv[3] if len(sys.argv) > 3 else "."

# Oldenberg 1888, 197-202, 222-223, as listed in Hellwig 2020 footnote 6.
# Full hymns only; Hellwig states that restriction explicitly.
OLDENBERG_APPENDICES = """
1.104 1.162 1.163 1.164 1.179 1.191 2.42 2.43 3.28 3.29 3.52 3.53
4.48 4.58 5.27 5.28 5.61 5.87 6.47 6.74 6.75 7.17 7.33 7.55 7.103
7.104 9.112 9.113 9.114 10.19 10.60
""".split()

SCHOLARS = ["grassmann", "oldenberg", "arnold", "wuest", "witzel"]
LABEL = {
    "grassmann": "Grassmann 1876-7",
    "oldenberg": "Oldenberg 1888/1909/1912",
    "arnold":    "Arnold 1897 (Sketch)",
    "wuest":     "Wuest 1928",
    "witzel":    "Witzel 1995",
}


def w(name, header, rows):
    p = os.path.join(OUT, name)
    with open(p, "w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f, delimiter="\t", lineterminator="\n")
        wr.writerow(header)
        wr.writerows(rows)
    return p


def pct(a, b):
    return 0.0 if not b else 100.0 * a / b


def hymn_of(stanza):
    """'01.001.01' -> '1.1'"""
    b, h, _ = stanza.split(".")
    return "%d.%d" % (int(b), int(h))


def book_of(stanza):
    return int(stanza.split(".")[0])


# ---------------------------------------------------------------- load
strata = json.load(open(os.path.join(VW, "info/strata.json"), encoding="utf-8"))
props  = json.load(open(os.path.join(VW, "info/stanza_properties.json"), encoding="utf-8"))
props.pop("Book.Hymn.Verse", None)
addr   = json.load(open(os.path.join(VW, "info/addressees.json"), encoding="utf-8"))

# per-stanza Arnold-1905 stratum. Every pada of a stanza carries the same
# code in this data; assert it rather than assume it.
stanza_stratum, stanza_metre, mixed = {}, {}, 0
pada_pairs = []                       # (metre label, stratum code) per pada
for sid, padas in strata.items():
    codes  = {p[2] for p in padas if p[2]}
    metres = {p[1] for p in padas if p[1]}
    for p in padas:
        if p[1] and p[2]:
            pada_pairs.append((p[1], p[2]))
    if len(codes) > 1:
        mixed += 1
    if codes:
        stanza_stratum[sid] = sorted(codes)[0] if len(codes) == 1 else "|".join(sorted(codes))
    if metres:
        stanza_metre[sid] = sorted(metres)[0] if len(metres) == 1 else "|".join(sorted(metres))

print("stanzas in strata.json           : %d" % len(strata))
print("stanzas with >1 stratum code     : %d" % mixed)
print("padas with metre and stratum     : %d" % len(pada_pairs))

# ------------------------------------------------ M1 metre -> stratum
# How much of Arnold's stratum code is recoverable from his metre label
# alone? Arnold derived the strata from metrical evidence, so a high number
# here is not a discovery about the text; it is the size of the confound
# that any test using the strata has to control for.
tab = collections.defaultdict(collections.Counter)
for m, s in pada_pairs:
    tab[m][s] += 1
n = len(pada_pairs)
correct = sum(c.most_common(1)[0][1] for c in tab.values())
base = collections.Counter(s for _, s in pada_pairs).most_common(1)[0][1]

# normalised mutual information
pm = collections.Counter(m for m, _ in pada_pairs)
ps = collections.Counter(s for _, s in pada_pairs)
mi = 0.0
for m, cs in tab.items():
    for s, c in cs.items():
        mi += (c / n) * math.log((c / n) / ((pm[m] / n) * (ps[s] / n)))
hm = -sum((c / n) * math.log(c / n) for c in pm.values())
hs = -sum((c / n) * math.log(c / n) for c in ps.values())
nmi = mi / math.sqrt(hm * hs) if hm and hs else 0.0

print()
print("M1  metre label -> stratum code, over %d padas" % n)
print("    distinct metre labels        : %d" % len(pm))
print("    distinct stratum codes       : %d" % len(ps))
print("    majority-class baseline      : %.1f%%" % pct(base, n))
print("    predict stratum from metre   : %.1f%%" % pct(correct, n))
print("    normalised mutual information: %.3f" % nmi)
w("m1-metre-by-stratum.tsv", ["metre_label", "stratum", "padas"],
  sorted(((m, s, c) for m, cs in tab.items() for s, c in cs.items()),
         key=lambda r: (-sum(tab[r[0]].values()), r[0], r[1])))

# ------------------------------------- M3 stanza_properties coverage
print()
print("M3  stanza_properties coverage (SRC-090)")
marks = {sc: {} for sc in SCHOLARS}       # scholar -> {stanza: code}
for sid, rec in props.items():
    for sc, code in rec.items():
        if sc in marks:
            marks[sc][sid] = code
rows = []
for sc in SCHOLARS:
    codes = collections.Counter(marks[sc].values())
    rows.append([sc, LABEL[sc], len(marks[sc]),
                 "; ".join("%s=%d" % kv for kv in sorted(codes.items()))])
    print("    %-10s %-26s %5d stanzas   %s"
          % (sc, LABEL[sc], len(marks[sc]),
             " ".join("%s=%d" % kv for kv in sorted(codes.items()))))
w("m3-coverage.tsv", ["scholar", "work", "stanzas_marked", "codes"], rows)

# per book
rows = []
book_tot = collections.Counter(book_of(s) for s in strata)
for b in range(1, 11):
    r = [b, book_tot[b]]
    for sc in SCHOLARS:
        k = sum(1 for s in marks[sc] if book_of(s) == b)
        r += [k, "%.1f" % pct(k, book_tot[b])]
    rows.append(r)
hdr = ["book", "stanzas"]
for sc in SCHOLARS:
    hdr += [sc + "_marked", sc + "_pct"]
w("m3-coverage-by-book.tsv", hdr, rows)
print()
print("M3b marked stanzas as %% of each book")
print("    book  stanzas  " + "  ".join("%-10s" % s[:10] for s in SCHOLARS))
for r in rows:
    print("    %-5s %6d   " % (r[0], r[1])
          + "  ".join("%9s%%" % r[3 + 2 * i] for i in range(len(SCHOLARS))))

# ------------------------------------- M4 pairwise agreement
print()
print("M4  pairwise agreement between the five late-addition instruments")
print("    Jaccard over marked stanzas, and P(column marks | row marks)")
rows = []
for a in SCHOLARS:
    for b in SCHOLARS:
        if a >= b:
            continue
        A, B = set(marks[a]), set(marks[b])
        inter, union = len(A & B), len(A | B)
        rows.append([a, b, len(A), len(B), inter, union,
                     "%.3f" % (inter / union if union else 0),
                     "%.3f" % (inter / len(A) if A else 0),
                     "%.3f" % (inter / len(B) if B else 0)])
        print("    %-10s %-10s |A|=%4d |B|=%4d  A&B=%4d  J=%.3f  "
              "P(B|A)=%.3f  P(A|B)=%.3f"
              % (a, b, len(A), len(B), inter, inter / union if union else 0,
                 inter / len(A) if A else 0, inter / len(B) if B else 0))
w("m4-pairwise-agreement.tsv",
  ["scholar_a", "scholar_b", "a_marked", "b_marked", "both", "either",
   "jaccard", "p_b_given_a", "p_a_given_b"], rows)

# --------------- M5 each instrument's marks against Arnold 1905 strata
# Baseline = distribution of all stanzas over stratum codes, uppercase and
# lowercase folded, since the case distinction is Arnold's confidence, not
# a different period (PUR-011, PUR-012).
def fold(code):
    return code.upper() if code else ""

base_dist = collections.Counter(fold(stanza_stratum.get(s, "")) for s in strata)
base_n = sum(v for k, v in base_dist.items() if k)
print()
print("M5  each instrument's marked stanzas, distributed over Arnold 1905 strata")
print("    corpus baseline: " + "  ".join(
    "%s=%.1f%%" % (k, pct(v, base_n)) for k, v in sorted(base_dist.items()) if k))
codes = sorted(k for k in base_dist if k)
rows = []
for sc in SCHOLARS + ["oldenberg_appendix_hymns"]:
    if sc == "oldenberg_appendix_hymns":
        marked = {s for s in strata if hymn_of(s) in set(OLDENBERG_APPENDICES)}
    else:
        marked = set(marks[sc])
    d = collections.Counter(fold(stanza_stratum.get(s, "")) for s in marked)
    tot = sum(v for k, v in d.items() if k)
    r = [sc, tot]
    line = "    %-26s n=%5d  " % (sc, tot)
    for c in codes:
        obs, exp = d[c], pct(base_dist[c], base_n) * tot / 100.0
        rr = obs / exp if exp else float("nan")
        r += [obs, "%.1f" % pct(obs, tot), "%.2f" % rr]
        line += "%s %.1f%% (x%.2f)  " % (c, pct(obs, tot), rr)
    rows.append(r)
    print(line)
hdr = ["instrument", "stanzas_with_a_stratum"]
for c in codes:
    hdr += [c + "_n", c + "_pct", c + "_rate_ratio"]
w("m5-instruments-vs-arnold1905.tsv", hdr, rows)

# ------------- M7 Hellwig's Oldenberg appendix list vs VedaWeb's oldenberg
print()
print("M7  two transcriptions of Oldenberg 1888, cross-checked")
app_h = set(OLDENBERG_APPENDICES)
app_v = collections.Counter()
for s, c in marks["oldenberg"].items():
    app_v[hymn_of(s)] += 1
hymn_len = collections.Counter(hymn_of(s) for s in strata)
full_v = {h for h, k in app_v.items() if k == hymn_len[h]}
print("    Hellwig 2020 fn.6, full hymns          : %d" % len(app_h))
print("    VedaWeb oldenberg column, hymns touched: %d" % len(app_v))
print("    of those, marked in every stanza       : %d" % len(full_v))
print("    Hellwig's list also fully marked in VedaWeb: %d of %d"
      % (len(app_h & full_v), len(app_h)))
print("    Hellwig's list touched at all in VedaWeb   : %d of %d"
      % (len(app_h & set(app_v)), len(app_h)))
miss = sorted(app_h - set(app_v), key=lambda x: [int(y) for y in x.split(".")])
print("    in Hellwig, untouched in VedaWeb       : %s" % (", ".join(miss) or "none"))
w("m7-oldenberg-cross-check.tsv",
  ["hymn", "in_hellwig_fn6", "vedaweb_stanzas_marked", "hymn_stanzas",
   "vedaweb_fully_marked"],
  [[h, int(h in app_h), app_v.get(h, 0), hymn_len[h], int(h in full_v)]
   for h in sorted(set(app_h) | set(app_v),
                   key=lambda x: [int(y) for y in x.split(".")])])
