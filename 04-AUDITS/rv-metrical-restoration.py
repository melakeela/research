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
    """Syllable nuclei in an ISO-15919 / IAST Vedic string.

    The digraph rule is load-bearing. The van Nooten and Holland text
    writes long vocalic r̥̄ as the DIGRAPH "r̥r̥" - mr̥r̥ḷaya, jaritr̥r̥ṇáam -
    where Aufrecht writes mr̥ḷaya. Read naively that is two nuclei and the
    pada comes out one syllable over. 273 padas carry it. An earlier
    version of this function got that wrong and the error reached a
    committed register row; see 04-AUDITS/domain-a-method.md section 4.
    """
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
            # the digraph: r̥r̥ is one nucleus, long vocalic r̥̄
            if i + 1 < len(t) and t[i] == c and t[i + 1] == RING:
                i += 2
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

# ---------------------------------------------------------------- self-test
# Two hand-checked padas cannot catch a systematic transliteration bug, and
# the first version of this script proved it. The test that can is the
# corpus itself: the restored text is a metrical edition, so all but a small
# residue of its padas must have a canonical length, and any residue
# concentrated on one orthographic string is a bug in the counter, not a
# fact about the text.
_HAND = {("01.001.01", "a"): 8, ("01.001.02", "b"): 8,
         ("01.012.09", "c"): 8, ("01.025.03", "a"): 8}
for k, want in _HAND.items():
    got = syllables(vnh[k])
    assert got == want, "self-test failed at %s%s: %d != %d" % (k[0], k[1], got, want)

_resid = [k for k in vnh if syllables(vnh[k]) not in CANONICAL]
_digraph = [k for k in _resid if "r\u0325r\u0325" in unicodedata.normalize("NFD", vnh[k])]
print("self-test: %d of %d restored padas are non-canonical (%.1f%%)"
      % (len(_resid), len(vnh), 100.0 * len(_resid) / len(vnh)))
print("           of those, %d contain the r̥r̥ digraph" % len(_digraph))
assert len(_resid) < 0.05 * len(vnh), (
    "more than 5%% of the restored text is non-canonical (%d padas): the "
    "counter is wrong, not the edition" % len(_resid))
assert len(_digraph) <= 10, (
    "%d non-canonical padas carry the r̥r̥ digraph: the digraph rule has "
    "regressed" % len(_digraph))

strata = json.load(open(os.path.join(VW, "info/strata.json"), encoding="utf-8"))
pada_stratum, stanza_stratum, stanza_metre = {}, {}, {}
for sid, ps in strata.items():
    codes = {p[2].upper() for p in ps if p[2]}
    if len(codes) == 1:
        stanza_stratum[sid] = codes.pop()
    metres = {p[1] for p in ps if p[1]}
    if len(metres) == 1:
        stanza_metre[sid] = metres.pop()
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

# Finding C of the 2026-09-07 adversarial review. The Aufrecht->vNH delta
# cannot all be attributed to metrical restoration, because the two texts
# also differ in SEGMENTATION: Aufrecht joins pada pairs into one line and
# so writes sandhi across the junction, while vNH never does. The delta
# therefore decomposes into a segmentation part and a metrical part, and
# only the second is what R1's sentence is about.
# Two bugs in the first version of this block, both found by the second
# adversarial review and both understating the confound:
#   (a) it counted EVERY adjacent pada pair (29,139). Aufrecht joins a+b and
#       c+d, not b+c - its line labels are a and c - so the line-internal
#       junctions are 18,228, and only those can carry junction sandhi.
#   (b) it tested for a vowel with `ta[-1] in "aāiīuūeoṛṝ"` on a string that
#       uses combining marks. A pada ending in an accented vowel has U+0301
#       as its last character, and vocalic r is written r + U+0325, never ṛ,
#       so ṛ and ṝ never match anything in these files at all.
LINE_INTERNAL = {("a", "b"), ("c", "d"), ("e", "f"), ("g", "h")}
VOWELS = set("aiueo")


def _final_base(t):
    """Last base character of a pada, and whether it carries the ring below."""
    d = unicodedata.normalize("NFD", t)
    marks = []
    for ch in reversed(d):
        if unicodedata.category(ch)[0] == "M":
            marks.append(ch)
            continue
        return ch, RING in marks
    return "", False


def _ends_in_vowel(t):
    """A syllable nucleus in final position.

    Third version of this test. The second accepted `ch in "rl"` with the
    comment "vocalic r and l are nuclei" and never checked for the ring
    below, so it also accepted CONSONANTAL final -r - ŕ̥ṣibhir, kavír,
    savitar - at 424 junctions. Those are not sites where the mechanism
    being bounded operates: -r before a vowel stays -r V- in Samhita
    sandhi and no syllable is lost. The census printed below is the check
    that would have shown it: consonantal r is the seventh commonest final
    base character at these junctions and vocalic r does not occur at one
    at all.
    """
    ch, ring = _final_base(t)
    return ch in VOWELS or (ch in "rl" and ring)


def _starts_with_vowel(t):
    d = unicodedata.normalize("NFD", t)
    if not d:
        return False
    if d[0].lower() in VOWELS:
        return True
    return d[0].lower() in "rl" and len(d) > 1 and d[1] == RING


by_stanza = collections.defaultdict(list)
for (s2, l) in vnh:
    by_stanza[s2].append(l)
junctions = vowel_junctions = 0
for sid in common:
    letters = sorted(by_stanza.get(sid, []))
    for a_, b_ in zip(letters, letters[1:]):
        if (a_, b_) not in LINE_INTERNAL:
            continue
        ta, tb = vnh[(sid, a_)], vnh[(sid, b_)]
        if not ta or not tb:
            continue
        junctions += 1
        if _ends_in_vowel(ta) and _starts_with_vowel(tb):
            vowel_junctions += 1
sa_c = sum(TA[s] for s in common); sl_c = sum(TL[s] for s in common)
sv_c = sum(TV[s] for s in common)
print()
print("R1b decomposing the +%.2f%%" % (100.0*(sv_c-sa_c)/sa_c))
print("    Aufrecht -> Lubotsky  %+.2f%%  both de-sandhied, segmentation differs"
      % (100.0*(sl_c-sa_c)/sa_c))
print("    Lubotsky -> van N.-H. %+.2f%%  same pada segmentation, metre only"
      % (100.0*(sv_c-sl_c)/sa_c))
census = collections.Counter()
for sid in common:
    letters = sorted(by_stanza.get(sid, []))
    for a_, b_ in zip(letters, letters[1:]):
        if (a_, b_) in LINE_INTERNAL and vnh.get((sid, a_)):
            ch, ring = _final_base(vnh[(sid, a_)])
            census[ch + ("\u0325" if ring else "")] += 1
print("    final base characters at those junctions, commonest first:")
print("      " + "  ".join("%s=%d" % kv for kv in census.most_common(8)))
print("      (BF-023's control. Consonantal r appears here and vocalic r does")
print("      not; the second version of this test conflated them.)")
print("    pada-pair junctions Aufrecht writes inside one line: %d, of which"
      % junctions)
print("    vowel against vowel: %d (%.1f%% of junctions)"
      % (vowel_junctions, pct(vowel_junctions, junctions)))
print("    So an upper bound of %.1f%% of the %d-syllable delta is segmentation,"
      % (pct(vowel_junctions, sv_c - sa_c), sv_c - sa_c))
print("    not metrical requirement. The claim R1 supports without qualification")
print("    is the Lubotsky -> van Nooten and Holland step.")
w("r1b-delta-decomposition.tsv", ["measure", "value"],
  [["syllables_aufrecht", sa_c], ["syllables_lubotsky", sl_c],
   ["syllables_vnh", sv_c],
   ["pct_aufrecht_to_lubotsky", "%.2f" % (100.0*(sl_c-sa_c)/sa_c)],
   ["pct_lubotsky_to_vnh", "%.2f" % (100.0*(sv_c-sl_c)/sa_c)],
   ["pada_pair_junctions", junctions],
   ["vowel_vowel_junctions", vowel_junctions],
   ["upper_bound_pct_of_delta_from_segmentation",
    "%.1f" % pct(vowel_junctions, sv_c - sa_c)]])

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


# ------------------------------- R5 does the stratum difference survive?
# Findings F and L of the 2026-09-07 adversarial review. The chi-square this
# section used to report treated ~397,000 syllables as independent draws;
# syllables inside a stanza are not independent, and that is what inflated
# it. The stanza-level rank test carries the result, and the ordering claim
# is checked against the medians rather than the means, because a rank test
# is what is being run.
from scipy.stats import kruskal
print()
print("R5  is the stratum difference in R4 more than noise?")
codes = sorted({c for c in stanza_stratum.values()})
groups, med = [], {}
for c in codes:
    ss = [s for s in common if stanza_stratum.get(s) == c]
    g = sorted((TV[s] - TA[s]) / TA[s] for s in ss if TA[s])
    groups.append(g); med[c] = g[len(g) // 2]
h, pk = kruskal(*groups)
print("    Kruskal-Wallis on per-stanza restoration rate: H = %.1f, p = %.3g"
      % (h, pk))
for c, g in zip(codes, groups):
    print("       %-3s n=%5d  median %.4f  mean %.4f"
          % (c, len(g), med[c], sum(g) / len(g)))
# The row asserts a three-tier structure - Archaic, then Strophic, then the
# rest undifferentiated. The second adversarial review pointed out that it
# asserted it on medians alone. Each tier boundary is tested here.
from scipy.stats import mannwhitneyu
gi = {c: g for c, g in zip(codes, groups)}
_, p_as = mannwhitneyu(gi["A"], gi["S"], alternative="greater")
rest = gi["C"] + gi["N"] + gi["P"]
_, p_sr = mannwhitneyu(gi["S"], rest, alternative="greater")
_, p_cnp = kruskal(gi["C"], gi["N"], gi["P"])
print("    the three tiers, tested rather than read off the medians:")
print("      Archaic > Strophic                : Mann-Whitney p = %.3g" % p_as)
print("      Strophic > Cretic+Normal+Popular  : Mann-Whitney p = %.3g" % p_sr)
print("      Cretic vs Normal vs Popular       : Kruskal-Wallis p = %.3g" % p_cnp)
ties = [c for c in codes if abs(med[c] - med["N"]) < 1e-9]
print("    strata sharing the Normal median exactly: %s" % ", ".join(ties))
print("    So the rank test separates Archaic, and Strophic behind it. It does")
print("    NOT order Normal, Cretic and Popular among themselves.")

# and the two harder controls: within one metre label, and within book
print("    -- the harder controls")
by_metre = collections.defaultdict(list)
for sid in common:
    st = stanza_stratum.get(sid)
    mt = stanza_metre.get(sid)
    if st and mt and TA[sid]:
        by_metre[mt].append((st, (TV[sid] - TA[sid]) / TA[sid]))
big = max(by_metre, key=lambda k: len(by_metre[k]))
gm = collections.defaultdict(list)
for st, r in by_metre[big]:
    gm[st].append(r)
gm = {k: v for k, v in gm.items() if len(v) >= 20}
if len(gm) > 1:
    h2, p2 = kruskal(*gm.values())
    print("       inside the single commonest metre label %r (n=%d, %d strata):"
          % (big, len(by_metre[big]), len(gm)))
    print("         H = %.1f, p = %.3g" % (h2, p2))
rows_c = []
print("       inside each book:")
for b in range(1, 11):
    gb = collections.defaultdict(list)
    for sid in common:
        if int(sid.split(".")[0]) == b and stanza_stratum.get(sid) and TA[sid]:
            gb[stanza_stratum[sid]].append((TV[sid] - TA[sid]) / TA[sid])
    gb = {k: v for k, v in gb.items() if len(v) >= 20}
    if len(gb) > 1:
        hb, pb = kruskal(*gb.values())
        rows_c.append([b, len(gb), "%.1f" % hb, "%.3g" % pb])
        print("         book %-3d %d strata  H = %6.1f  p = %.3g"
              % (b, len(gb), hb, pb))
sig = sum(1 for r in rows_c if float(r[3]) < 0.05)
print("       significant at 0.05 in %d of the %d books testable"
      % (sig, len(rows_c)))
w("r5-stratum-significance.tsv",
  ["stratum", "stanzas", "median_rate", "mean_rate"],
  [[c, len(g), "%.5f" % med[c], "%.5f" % (sum(g) / len(g))]
   for c, g in zip(codes, groups)])
w("r5b-stratum-within-book.tsv",
  ["book", "strata_tested", "kruskal_H", "p"], rows_c)

# ------------------------------------ R6 the Padapatha against the Samhita
# Constitution s.4.A names the Padapatha specifically. It is a fourth text,
# stanza-keyed and word-separated by the tradition itself rather than by a
# modern lexicographer.
#   versions/padapatha.csv   GRETIL / Sansknet data entry, contributed by
#                            Reinhold Gruenendahl, TEI markup by Maximilian
#                            Mehner                                SRC-108
import statistics
pada_p = {}
with open(os.path.join(VW, "versions/padapatha.csv"), newline="", encoding="utf-8") as f:
    for row in csv.reader(f, delimiter="\t"):
        if len(row) >= 2 and row[1].strip():
            pada_p[row[0]] = row[1].strip()


def pp_syllables(s):
    """The Padapatha marks word and compound boundaries with | and -."""
    return syllables(s.replace("|", " ").replace("-", " "))


print()
print("R6  the Padapatha against the Samhita, %d stanzas" % len(pada_p))
shared = sorted(set(pada_p) & set(TA) & set(TV))
delta = {s: pp_syllables(pada_p[s]) - TA[s] for s in shared}

# Finding E of the 2026-09-07 adversarial review. The first version of this
# section lumped two different things under one data-chosen window and named
# none of them. They are separated here and every excluded stanza is written
# out, and the headline is reported with and without the exclusion.
#
# DEFECTIVE is a property of the cell, decided by reading it, not by its
# delta: the Padapatha text is missing or is a stray fragment.
defective = sorted(s for s in shared
                   if pada_p[s].strip().upper() in {"N/A", "NA", "ITI", "-"}
                   or len(pada_p[s].replace("|", "").strip()) < 8)
# DIVERGENT is a property of the delta and is NOT evidence of a defect. It
# is reported separately and is NOT excluded from the headline.
divergent = sorted(s for s in shared
                   if s not in defective and not (-5 <= delta[s] <= 15))
print("    stanzas whose Padapatha cell is defective on inspection: %d" % len(defective))
for s in defective[:5]:
    print("      %s reads %r (Samhita has %d syllables)"
          % (s, pada_p[s][:28], TA[s]))
print("    stanzas whose delta is far from the rest but whose cell is intact: %d"
      % len(divergent))
print("      these are NOT excluded; nothing shows them to be defective")

def totals(keys):
    return (sum(TA[s] for s in keys), sum(pp_syllables(pada_p[s]) for s in keys),
            sum(TV[s] for s in keys))

for label, keys in (("all stanzas", shared),
                    ("less the defective cells", [s for s in shared if s not in defective]),
                    ("less defective and divergent",
                     [s for s in shared if s not in defective and s not in divergent])):
    a, pp_, v = totals(keys)
    print("    %-30s n=%5d  Samhita %7d  Padapatha %+.2f%%  restored %+.2f%%"
          % (label, len(keys), a, 100.0*(pp_-a)/a, 100.0*(v-a)/a))

keys = [s for s in shared if s not in defective]
a, pp_, v = totals(keys)
eq_a = sum(1 for s in keys if pp_syllables(pada_p[s]) == TA[s])
eq_v = sum(1 for s in keys if pp_syllables(pada_p[s]) == TV[s])
print("    The headline figure is the middle row: defective cells removed,")
print("    divergent ones kept. The Padapatha resolves MORE than the metre")
print("    asks for - it undoes every sandhi, including the ones the poets")
print("    made themselves.")
print("      Padapatha == Samhita  in %5d of %d (%.1f%%)" % (eq_a, len(keys), pct(eq_a, len(keys))))
print("      Padapatha == restored in %5d of %d (%.1f%%)" % (eq_v, len(keys), pct(eq_v, len(keys))))

w("r6-padapatha-excluded-stanzas.tsv",
  ["stanza", "class", "padapatha_cell", "padapatha_syllables",
   "samhita_syllables", "delta"],
  [[s, "defective", pada_p[s][:60], pp_syllables(pada_p[s]), TA[s], delta[s]]
   for s in defective]
  + [[s, "divergent-but-intact", pada_p[s][:60], pp_syllables(pada_p[s]),
      TA[s], delta[s]] for s in divergent])
w("r6-padapatha-vs-samhita.tsv", ["measure", "value"],
  [["stanzas_compared", len(keys)],
   ["stanzas_excluded_defective", len(defective)],
   ["stanzas_divergent_but_kept", len(divergent)],
   ["syllables_samhita", a], ["syllables_padapatha", pp_],
   ["syllables_restored", v],
   ["pct_padapatha_over_samhita", "%.2f" % (100.0*(pp_-a)/a)],
   ["pct_restored_over_samhita", "%.2f" % (100.0*(v-a)/a)],
   ["stanzas_padapatha_equals_samhita", eq_a],
   ["stanzas_padapatha_equals_restored", eq_v]])
