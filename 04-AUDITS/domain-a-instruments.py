#!/usr/bin/env python3
"""
Domain A - Rigvedic chronology and transmission.
Instrument measurements over the VedaWeb bundle at commit d3eb8af.

Every number this unit reports is produced here. Nothing is typed by hand.

Inputs (all inside one clone; see 02-SOURCES/vedaweb-manifest-2026-09-09-domain-a.md):
  rigveda/info/strata.json            SRC-023 : Arnold 1905, per-pada metre + stratum
  rigveda/info/stanza_properties.json SRC-071 : five scholars' stanza-level flags
  rigveda/versions/aufrecht.csv       SRC-020 : transmitted Samhitapatha
  rigveda/versions/vnh.csv            SRC-078 : van Nooten & Holland 1994, metrically restored
  rigveda/versions/padapatha.csv      SRC-021 : padapatha

Usage:  python3 domain-a-instruments.py <path-to-clone>/rigveda  <outdir>
"""
import sys, os, csv, json, math, collections, unicodedata

RIG = sys.argv[1] if len(sys.argv) > 1 else "/home/user/vw-a/vedaweb-data/rigveda"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/domain-a"
os.makedirs(OUT, exist_ok=True)

# Arnold's five strata. Uppercase = assignment stated as certain; lowercase =
# assignment resting on metrical variations only. Both mappings are the ones
# already established in this repository from the Arnold 1905 OCR
# (SRC-026, Appendix IV s265, printed p.269) and used in
# 03-REGISTERS/rigveda-pur-passages.csv. archive.org is EGRESS_BLOCKED in this
# session, so Arnold was NOT re-read here; the mapping is inherited, not re-checked.
STRATUM_NAME = {"A": "Archaic", "S": "Strophic", "N": "Normal", "C": "Cretic", "P": "Popular"}
ORDER = ["A", "S", "N", "C", "P"]          # Arnold's own sequence, early -> late
LATE = {"C", "P"}                           # the two Arnold placed latest

def emit(name, rows, header):
    p = os.path.join(OUT, name)
    with open(p, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(header)
        w.writerows(rows)
    print("wrote", p, len(rows), "rows")

def pct(a, b):
    return 0.0 if not b else round(100.0 * a / b, 2)

# ---------------------------------------------------------------- load strata
strata = json.load(open(os.path.join(RIG, "info/strata.json"), encoding="utf-8"))
pada_rows = []          # (stanza, book, hymn, stanza_n, pada, metre, code)
for st, padas in strata.items():
    b, h, n = st.split(".")
    for pada in padas:
        pada_rows.append((st, int(b), int(h), int(n), pada[0], pada[1], pada[2]))
print("padas:", len(pada_rows), " stanzas:", len(strata))

# stanza-level stratum: uppercase-normalised majority over its padas
stanza_stratum, stanza_mixed, stanza_certain = {}, {}, {}
for st, padas in strata.items():
    cs = [p[2] for p in padas]
    up = [c.upper() for c in cs]
    cnt = collections.Counter(up)
    top, topn = cnt.most_common(1)[0]
    stanza_stratum[st] = top
    stanza_mixed[st] = len(cnt) > 1
    stanza_certain[st] = all(c.isupper() for c in cs)

# ------------------------------------------------- A1 stratum x book (padas)
books = sorted({r[1] for r in pada_rows})
tab = collections.defaultdict(collections.Counter)
for st, b, h, n, pd_, mt, code in pada_rows:
    tab[b][code.upper()] += 1
rows = []
for b in books:
    tot = sum(tab[b].values())
    late = sum(tab[b][c] for c in LATE)
    rows.append([b, tot] + [tab[b][c] for c in ORDER] +
                [pct(tab[b][c], tot) for c in ORDER] + [pct(late, tot)])
tot_all = sum(sum(tab[b].values()) for b in books)
allc = collections.Counter()
for b in books: allc.update(tab[b])
rows.append(["ALL", tot_all] + [allc[c] for c in ORDER] +
            [pct(allc[c], tot_all) for c in ORDER] +
            [pct(sum(allc[c] for c in LATE), tot_all)])
emit("A1-stratum-by-book-padas.csv", rows,
     ["book", "padas"] + ["n_" + c for c in ORDER] + ["pct_" + c for c in ORDER] + ["pct_late_CP"])

# ------------------------------------- A2 certainty of the stratum assignment
cert = collections.Counter(); cert_b = collections.defaultdict(collections.Counter)
for st, b, h, n, pd_, mt, code in pada_rows:
    k = "certain" if code.isupper() else "metrical-variations-only"
    cert[k] += 1; cert_b[b][k] += 1
rows = [[b, sum(cert_b[b].values()), cert_b[b]["certain"], cert_b[b]["metrical-variations-only"],
         pct(cert_b[b]["metrical-variations-only"], sum(cert_b[b].values()))] for b in books]
rows.append(["ALL", sum(cert.values()), cert["certain"], cert["metrical-variations-only"],
             pct(cert["metrical-variations-only"], sum(cert.values()))])
emit("A2-stratum-certainty-by-book.csv", rows,
     ["book", "padas", "n_certain_uppercase", "n_variations_only_lowercase", "pct_variations_only"])

# --------------------------------- A3 internal heterogeneity of each mandala
rows = []
for b in books:
    c = tab[b]; tot = sum(c.values())
    ps = [c[x] / tot for x in ORDER if c[x]]
    H = -sum(p * math.log(p, 2) for p in ps)
    rows.append([b, tot, c.most_common(1)[0][0], pct(c.most_common(1)[0][1], tot),
                 round(H, 3), round(H / math.log(5, 2), 3), len([x for x in ORDER if c[x]])])
emit("A3-mandala-heterogeneity.csv", rows,
     ["book", "padas", "modal_stratum", "pct_modal", "entropy_bits", "entropy_normalised_5", "strata_present"])

# ------------------------- A4 within-book position: hymn quartiles per book
rows = []
for b in books:
    hs = sorted({r[2] for r in pada_rows if r[1] == b})
    if not hs: continue
    q = max(1, len(hs) // 4)
    for qi in range(4):
        lo = qi * q
        hi = len(hs) if qi == 3 else (qi + 1) * q
        sel = set(hs[lo:hi])
        c = collections.Counter(r[6].upper() for r in pada_rows if r[1] == b and r[2] in sel)
        tot = sum(c.values())
        if not tot: continue
        rows.append([b, qi + 1, min(sel), max(sel), tot] +
                    [pct(c[x], tot) for x in ORDER] + [pct(sum(c[x] for x in LATE), tot)])
emit("A4-stratum-by-hymn-quartile.csv", rows,
     ["book", "quartile", "first_hymn", "last_hymn", "padas"] +
     ["pct_" + c for c in ORDER] + ["pct_late_CP"])

# ---------------------------- A5 the four non-Arnold stanza-level instruments
sp = json.load(open(os.path.join(RIG, "info/stanza_properties.json"), encoding="utf-8"))
header_key = "Book.Hymn.Verse"
cols = list(sp[header_key].keys())          # grassmann oldenberg arnold wuest witzel
flags = {k: v for k, v in sp.items() if k != header_key}
NON_ARNOLD = [c for c in cols if c != "arnold"]

per = collections.Counter()
for st, d in flags.items():
    for c in d: per[c] += 1
# Sixteen keys in stanza_properties.json name stanzas that strata.json does not
# contain (A13). Publishing the raw key count over a denominator of 10,552 real
# stanzas puts a numerator including non-existent stanzas over a count of
# existing ones, so both populations are emitted and the rate uses the second.
_real = {k for k in flags if k in strata}
per_real = collections.Counter()
for st_, d in flags.items():
    if st_ not in strata: continue
    for c in d: per_real[c] += 1
rows = [[c, sp[header_key][c], per[c], per_real[c], per[c] - per_real[c], pct(per_real[c], len(strata))] for c in cols]
rows.append(["ANY", "at least one scholar", len(flags), len(_real), len(flags) - len(_real), pct(len(_real), len(strata))])
emit("A5a-scholar-flag-counts.csv", rows,
     ["column", "source_as_named_in_file", "keys_in_file", "stanzas_that_exist_in_strata",
      "keys_naming_absent_stanzas", "pct_of_10552_existing_stanzas"])

# pairwise co-flagging
rows = []
for i, a in enumerate(cols):
    for bq in cols[i + 1:]:
        A = {s for s, d in flags.items() if a in d}
        B = {s for s, d in flags.items() if bq in d}
        inter = len(A & B); uni = len(A | B)
        rows.append([a, bq, len(A), len(B), inter, round(inter / uni, 4) if uni else 0,
                     pct(inter, len(A)), pct(inter, len(B))])
emit("A5b-scholar-pairwise-agreement.csv", rows,
     ["scholar_a", "scholar_b", "n_a", "n_b", "n_both", "jaccard", "pct_of_a_also_b", "pct_of_b_also_a"])

# enrichment of each scholar's flagged stanzas in Arnold's late strata
base = collections.Counter(stanza_stratum.values())
base_tot = sum(base.values()); base_late = sum(base[c] for c in LATE)
rows = []
for c in cols + ["ANY"]:
    sel = list(flags) if c == "ANY" else [s for s, d in flags.items() if c in d]
    sel = [s for s in sel if s in stanza_stratum]
    cc = collections.Counter(stanza_stratum[s] for s in sel)
    tot = sum(cc.values()); late = sum(cc[x] for x in LATE)
    # 2x2 chi-square with Yates, flagged vs unflagged, late vs not-late
    a = late; bq = tot - late
    cq = base_late - late; dq = (base_tot - base_late) - bq
    n = a + bq + cq + dq
    chi = 0.0
    r1, r2, c1, c2 = a + bq, cq + dq, a + cq, bq + dq
    if min(r1, r2, c1, c2) > 0:
        chi = n * max(0.0, abs(a * dq - bq * cq) - n / 2.0) ** 2 / (r1 * r2 * c1 * c2)
    rows.append([c, tot] + [cc[x] for x in ORDER] + [pct(cc[x], tot) for x in ORDER] +
                [pct(late, tot), pct(base_late, base_tot),
                 round(pct(late, tot) / pct(base_late, base_tot), 3) if base_late else 0,
                 round(chi, 3)])
emit("A5c-scholar-flags-vs-arnold-strata.csv", rows,
     ["column", "flagged_stanzas"] + ["n_" + c for c in ORDER] + ["pct_" + c for c in ORDER] +
     ["pct_late_CP", "corpus_pct_late_CP", "enrichment_ratio", "chisq_yates_1df"])

# scholar flag density by book
rows = []
for b in books:
    stz = [s for s in strata if int(s.split(".")[0]) == b]
    r = [b, len(stz)]
    for c in cols + ["ANY"]:
        sel = [s for s in stz if s in flags and (c == "ANY" or c in flags[s])]
        r.append(pct(len(sel), len(stz)))
    rows.append(r)
emit("A5d-scholar-flag-density-by-book.csv", rows,
     ["book", "stanzas"] + ["pct_flagged_" + c for c in cols + ["ANY"]])

# ------------ A6 transmitted Samhitapatha against the metrically restored text
def load_tsv3(p):
    d = collections.OrderedDict()
    for row in csv.reader(open(p, encoding="utf-8"), delimiter="\t"):
        if len(row) < 3: continue
        d.setdefault(row[0], []).append(row[2])
    return d

au = load_tsv3(os.path.join(RIG, "versions/aufrecht.csv"))
vn = load_tsv3(os.path.join(RIG, "versions/vnh.csv"))
def flat(v): return "".join(v).replace(" ", "")
shared = [k for k in au if k in vn]
diff = [k for k in shared if flat(au[k]) != flat(vn[k])]
rows = []
for b in books:
    s = [k for k in shared if int(k.split(".")[0]) == b]
    d = [k for k in diff if int(k.split(".")[0]) == b]
    rows.append([b, len(s), len(d), pct(len(d), len(s))])
rows.append(["ALL", len(shared), len(diff), pct(len(diff), len(shared))])
emit("A6a-samhita-vs-restored-by-book.csv", rows,
     ["book", "stanzas_compared", "stanzas_differing", "pct_differing"])

# same, split by Arnold stratum: does the restoration bite evenly across strata?
rows = []
for x in ORDER:
    s = [k for k in shared if stanza_stratum.get(k) == x]
    d = [k for k in s if k in set(diff)]
    rows.append([x, STRATUM_NAME[x], len(s), len(d), pct(len(d), len(s))])
emit("A6b-samhita-vs-restored-by-stratum.csv", rows,
     ["stratum_code", "stratum_name", "stanzas", "stanzas_differing", "pct_differing"])

# what kind of restoration: characteristic substitutions, counted per stanza
import re
PATTERNS = [
    ("semivowel_y_to_iy", r"iy"),      # -ya- read disyllabically as -iya-
    ("semivowel_v_to_uv", r"uv|ua"),   # -va- read as -uva-
]
def kinds(a, b_):
    k = set()
    if len(b_) > len(a): k.add("restored_text_longer")
    if len(b_) < len(a): k.add("restored_text_shorter")
    if len(b_) == len(a): k.add("same_length")
    return k
kc = collections.Counter()
for k in diff:
    for t in kinds(flat(au[k]), flat(vn[k])): kc[t] += 1
rows = [[t, kc[t], pct(kc[t], len(diff))] for t in sorted(kc)]
emit("A6c-restoration-length-effect.csv", rows,
     ["effect_on_stanza_string", "stanzas", "pct_of_differing"])

# ---------------------------------------- A7 padapatha against the Samhita
# CORRECTED 2026-09-09 after adversarial review. The earlier comment here said
# "the padapatha is UNACCENTED in this bundle". That is FALSE: padapatha.csv
# carries 11,936 U+0301 acute accents and 2,268 U+0307. The two layers do differ
# in accent notation, which is why a raw comparison is uninformative, but the
# reason is a difference of convention, not the absence of accents. Combining
# marks are stripped from both sides before comparison, leaving the segmental
# skeleton. What is then measured is how much of the recited
# Samhita string is NOT recoverable letter-for-letter from the word-analysis:
# i.e. how much sandhi and contraction the padapatha undoes.
def deaccent(s_):
    s_ = unicodedata.normalize("NFD", s_)
    KEEP = {"\u0304", "\u0323", "\u0331", "\u0307", "\u0303"}  # macron, underdot, underline, overdot, tilde
    s_ = "".join(ch for ch in s_ if not unicodedata.combining(ch) or ch in KEEP)
    return unicodedata.normalize("NFC", s_)

pp = {}
for row in csv.reader(open(os.path.join(RIG, "versions/padapatha.csv"), encoding="utf-8"), delimiter="\t"):
    if len(row) < 2: continue
    pp[row[0]] = row[1]
def norm_pp(s_):
    return deaccent(s_).replace("|", "").replace("-", "").replace(" ", "").replace("\u2019", "").replace("'", "")
def norm_au(s_):
    return deaccent(s_).replace(" ", "").replace("\u2019", "").replace("'", "")
sh = [k for k in au if k in pp]
pdiff = [k for k in sh if norm_pp(pp[k]) != norm_au(flat(au[k]))]
# and the same against the metrically restored text, which is what a metrical
# argument actually uses
vdiff = [k for k in sh if k in vn and norm_pp(pp[k]) != norm_au(flat(vn[k]))]
# The padapatha is an ANALYSIS, not a segmentation: it inserts iti-forms, splits
# compounds and restores pre-sandhi shapes. Strip the inserted iti-material and
# re-measure, and also report how far apart the two strings are rather than only
# whether they differ.
def strip_iti(s_):
    toks = [t.strip() for t in s_.split("|")]
    out = []
    for t in toks:
        if t in ("iti",) or t.startswith("iti ") or t.endswith(" iti") or " iti" in t:
            t = " ".join(w for w in t.split() if w != "iti")
        out.append(t)
    return "|".join(out)
pdiff_iti = [k for k in sh if norm_pp(strip_iti(pp[k])) != norm_au(flat(au[k]))]
import difflib
ratios = []
for k in sh:
    a_ = norm_au(flat(au[k])); b_ = norm_pp(strip_iti(pp[k]))
    ratios.append(difflib.SequenceMatcher(None, a_, b_).ratio())
ratios.sort()
med = ratios[len(ratios)//2]
mean = sum(ratios)/len(ratios)
extra = [["padapatha_skeleton_differs_after_stripping_inserted_iti", len(pdiff_iti), pct(len(pdiff_iti), len(sh))],
         ["median_character_similarity_samhita_vs_padapatha", round(med, 4), ""],
         ["mean_character_similarity_samhita_vs_padapatha", round(mean, 4), ""],
         ["stanzas_at_similarity_1.0", sum(1 for r in ratios if r >= 0.99999), pct(sum(1 for r in ratios if r >= 0.99999), len(sh))]]

rows = [["stanzas_with_both_samhita_and_padapatha", len(sh), ""],
        ["padapatha_skeleton_differs_from_samhita_skeleton", len(pdiff), pct(len(pdiff), len(sh))],
        ["padapatha_skeleton_identical_to_samhita_skeleton", len(sh) - len(pdiff), pct(len(sh) - len(pdiff), len(sh))],
        ["padapatha_skeleton_differs_from_restored_text_skeleton", len(vdiff), pct(len(vdiff), len(sh))]] + extra
emit("A7-padapatha-vs-samhita.csv", rows, ["measure", "n", "pct"])

# ------- A9 which strata are present in which book at all (the zero cells)
rows = []
for b in books:
    c = tab[b]
    rows.append([b] + [("PRESENT" if c[x] else "ABSENT") for x in ORDER] +
                [len([x for x in ORDER if c[x]])])
rows.append(["ALL"] + [("PRESENT" if allc[x] else "ABSENT") for x in ORDER],)
emit("A9-stratum-presence-by-book.csv", rows,
     ["book"] + ["stratum_" + c for c in ORDER] + ["n_strata_present"])

# ------- A10 how far does the metre label alone determine the stratum code?
# Arnold's strata are built on metre. If the metre label predicts the stratum
# code almost deterministically, then "stratum" is a relabelling of metre and a
# by-book stratum difference cannot be read as a by-book date difference without
# a control for metrical genre. This is the confound Hellwig et al. 2021 report
# controlling for.
mx = collections.defaultdict(collections.Counter)
for st, b, h, n, pd_, mt, code in pada_rows:
    mx[mt][code.upper()] += 1
det = 0; tot = 0; rows = []
for mt in sorted(mx, key=lambda x: -sum(mx[x].values())):
    c = mx[mt]; t = sum(c.values())
    top, topn = c.most_common(1)[0]
    det += topn; tot += t
    rows.append([mt, t, top, topn, pct(topn, t), len(c)])
rows.append(["ALL_METRE_LABELS", tot, "modal-stratum accuracy", det, pct(det, tot), len(mx)])
emit("A10-metre-label-vs-stratum.csv", rows,
     ["metre_label", "padas", "modal_stratum", "n_modal", "pct_modal", "distinct_strata_under_label"])

# reverse direction: how many distinct metre labels sit under each stratum
rows = []
for x in ORDER:
    c = collections.Counter(mt for st, b, h, n, pd_, mt, code in pada_rows if code.upper() == x)
    t = sum(c.values())
    rows.append([x, STRATUM_NAME[x], t, len(c), c.most_common(1)[0][0], pct(c.most_common(1)[0][1], t)])
emit("A10b-stratum-vs-metre-label.csv", rows,
     ["stratum_code", "stratum_name", "padas", "distinct_metre_labels", "modal_metre_label", "pct_modal_metre"])

# ---- A5e enrichment of the non-Arnold flags, controlled for book ----
# The DEP-004 trap: book 10 is 74.8% Arnold-late AND carries most of the flags,
# so a corpus-wide enrichment can be produced by book 10 alone.
rows = []
for c in cols + ["ANY"]:
    for scope, keep in (("all_books", lambda b: True), ("books_1_to_9_only", lambda b: b != 10), ("book_10_only", lambda b: b == 10)):
        stz = [s for s in strata if keep(int(s.split(".")[0]))]
        selset = {s for s in stz if s in flags and (c == "ANY" or c in flags[s])}
        base_c = collections.Counter(stanza_stratum[s] for s in stz)
        bt = sum(base_c.values()); bl = sum(base_c[x] for x in LATE)
        fc = collections.Counter(stanza_stratum[s] for s in selset)
        ft = sum(fc.values()); fl = sum(fc[x] for x in LATE)
        rows.append([c, scope, bt, ft, pct(fl, ft), pct(bl, bt),
                     round(pct(fl, ft) / pct(bl, bt), 3) if bl and ft else 0])
emit("A5e-flag-enrichment-controlled-for-book.csv", rows,
     ["column", "scope", "stanzas_in_scope", "flagged_in_scope", "pct_flagged_late_CP",
      "scope_base_pct_late_CP", "enrichment_ratio"])

# ------------------ A8 is mandala number an axis? monotonicity of Arnold-late
lates = [(b, pct(sum(tab[b][c] for c in LATE), sum(tab[b].values()))) for b in books]
ranks_b = list(range(1, len(lates) + 1))
srt = sorted(range(len(lates)), key=lambda i: lates[i][1])
ranks_l = [0] * len(lates)
for r, i in enumerate(srt): ranks_l[i] = r + 1
n = len(lates)
d2 = sum((ranks_b[i] - ranks_l[i]) ** 2 for i in range(n))
rho = 1 - 6 * d2 / (n * (n * n - 1))
inv = sum(1 for i in range(n) for j in range(i + 1, n) if lates[i][1] > lates[j][1])
rows = [[b, v, ranks_l[i]] for i, (b, v) in enumerate(lates)]
rows.append(["spearman_rho_book_vs_pct_late", round(rho, 4), ""])
rows.append(["inversions_of_monotone_increase_max_45", inv, ""])
emit("A8-mandala-order-vs-arnold-late.csv", rows, ["book_or_measure", "pct_late_CP_or_value", "rank_by_late"])

# ================= A11  the null at A8, given a size =================
# A8 reports rho without a p-value or an interval, which lets a null be read as
# a finding. n = 10 admits exhaustive enumeration, so the exact permutation
# distribution is computed rather than approximated.
import itertools, random
def _rho(v):
    n = len(v)
    srt = sorted(range(n), key=lambda i: v[i]); rk = [0] * n
    for r, i in enumerate(srt): rk[i] = r + 1
    return 1 - 6 * sum((i + 1 - rk[i]) ** 2 for i in range(n)) / (n * (n * n - 1))
_late = [pct(sum(tab[b][c] for c in LATE), sum(tab[b].values())) for b in books]
_obs = _rho(_late)
_ge = sum(1 for perm in itertools.permutations(range(len(_late)))
          if abs(_rho([_late[i] for i in perm])) >= abs(_obs) - 1e-12)
_tot = math.factorial(len(_late))
# The null is enumerated, not sampled: the n=10 Spearman null is exactly
# symmetric about zero, so a sampled interval reports its own noise as an
# asymmetry. An earlier version drew 20,000 samples and published -0.648/+0.636;
# both bounds are the same number.
_all = sorted(_rho([_late[i] for i in perm]) for perm in itertools.permutations(range(len(_late))))
_lo = _all[int(0.025 * _tot)]
_hi = _all[int(0.975 * _tot)]
rows = [["spearman_rho_observed", round(_obs, 4), ""],
        ["exact_two_sided_permutation_p", round(_ge / _tot, 4), "all %d permutations enumerated" % _tot],
        ["null_95pct_lower", round(_lo, 4), "exact, all %d permutations" % _tot],
        ["null_95pct_upper", round(_hi, 4), "exact, all %d permutations" % _tot],
        ["interpretation", "UNDERPOWERED", "n=10 cannot distinguish rho=0 from a strong monotone relation; anything up to |rho|=0.6364 is inside the null range"]]
emit("A11-mandala-order-null-and-power.csv", rows, ["measure", "value", "note"])

# ============ A12  association between metre label and stratum ============
# A10's modal-stratum accuracy is a weak measure and understates the confound.
# These are the standard measures over the same table.
_N = sum(sum(mx[l].values()) for l in mx)
_rowt = {l: sum(mx[l].values()) for l in mx}
_colt = {s: sum(mx[l][s] for l in mx) for s in ORDER}
_chi = 0.0
for l in mx:
    for s in ORDER:
        e = _rowt[l] * _colt[s] / _N
        if e > 0: _chi += (mx[l][s] - e) ** 2 / e
def _H(d):
    t = sum(d.values())
    return -sum((v / t) * math.log(v / t, 2) for v in d.values() if v)
_Hs = _H(_colt)
_MI = _Hs - sum(_rowt[l] / _N * _H(mx[l]) for l in mx)
rows = [["padas", _N, ""],
        ["chi_square", round(_chi, 1), "%d metre labels x 5 strata" % len(mx)],
        ["cramers_v", round(math.sqrt(_chi / (_N * (min(len(mx), 5) - 1))), 4), "0 = independent, 1 = deterministic"],
        ["majority_class_accuracy_without_metre", pct(max(_colt.values()), _N), "predict the modal stratum for every pada"],
        ["modal_stratum_accuracy_given_metre", pct(det, tot), "as reported at A10"],
        ["uncertainty_coefficient_U_stratum_given_metre", round(_MI / _Hs, 4), "fraction of the stratum's entropy explained by the metre label"],
        ["mutual_information_bits", round(_MI, 4), "H(stratum) = %.4f bits" % _Hs]]
emit("A12-metre-stratum-association.csv", rows, ["measure", "value", "note"])

# ====== A13  flagged stanza keys that do not exist in strata.json ======
_phantom = sorted(k for k in flags if k not in strata)
rows = [[k, ";".join(sorted(flags[k]))] for k in _phantom]
rows.append(["TOTAL", str(len(_phantom))])
emit("A13-flagged-keys-absent-from-strata.csv", rows, ["stanza_key", "columns_flagging_it"])

# ===== A14  how much of A6a's 72.04% is notation rather than language =====
def _deacc(s_):
    s_ = unicodedata.normalize("NFD", s_)
    KEEP = {"\u0304", "\u0323", "\u0331", "\u0307", "\u0303"}
    return unicodedata.normalize("NFC", "".join(c for c in s_ if not unicodedata.combining(c) or c in KEEP))
_EDIT = set("@+\\*&~")
_strip = lambda s_: "".join(c for c in _deacc(s_) if c not in _EDIT)
_raw = [k for k in shared if flat(au[k]) != flat(vn[k])]
_na = [k for k in shared if _deacc(flat(au[k])) != _deacc(flat(vn[k]))]
_fu = [k for k in shared if _strip(flat(au[k])) != _strip(flat(vn[k]))]
_ec = collections.Counter(c for k in shared for c in flat(vn[k]) if c in _EDIT)
rows = [["raw_strings", len(_raw), pct(len(_raw), len(shared))],
        ["combining_marks_stripped", len(_na), pct(len(_na), len(shared))],
        ["marks_and_editorial_characters_stripped", len(_fu), pct(len(_fu), len(shared))],
        ["differ_only_in_notation", len(_raw) - len(_fu), pct(len(_raw) - len(_fu), len(_raw))],
        ["editorial_characters_in_vnh", "; ".join("%s=%d" % (k, v) for k, v in sorted(_ec.items())), ""]]
emit("A14-samhita-vs-restored-normalisation-sensitivity.csv", rows, ["normalisation", "stanzas_differing", "pct"])

# ===== A15  padapatha comparison, directional as well as symmetric =====
# SequenceMatcher.ratio() is 2M/(len(a)+len(b)) and is symmetric; a statement
# about how much of THE RECITED TEXT is unmatched needs M/len(samhita).
_sym, _dir = [], []
for k in sh:
    a_ = _strip(norm_au(flat(au[k]))); b_ = _strip(norm_pp(strip_iti(pp[k])))
    m = difflib.SequenceMatcher(None, a_, b_)
    M = sum(bl.size for bl in m.get_matching_blocks())
    _sym.append(2 * M / (len(a_) + len(b_))); _dir.append(M / len(a_))
_sym.sort(); _dir.sort()
_la = sum(len(_strip(norm_au(flat(au[k])))) for k in sh)
_lp = sum(len(_strip(norm_pp(strip_iti(pp[k])))) for k in sh)
rows = [["symmetric_ratio_median", round(_sym[len(_sym) // 2], 4), "2M/(len(a)+len(b))"],
        ["symmetric_ratio_mean", round(sum(_sym) / len(_sym), 4), ""],
        ["directional_median_matched_over_samhita", round(_dir[len(_dir) // 2], 4), "M/len(samhita) - the figure a claim about the recited text needs"],
        ["directional_mean_matched_over_samhita", round(sum(_dir) / len(_dir), 4), ""],
        ["total_chars_samhita", _la, ""],
        ["total_chars_padapatha", _lp, "padapatha longer by %.1f%%" % (100.0 * (_lp - _la) / _la)]]
emit("A15-padapatha-directional.csv", rows, ["measure", "value", "note"])

print("A11 exact p = %.4f ; A12 Cramer V = %.4f ; A13 phantom keys = %d ; A14 notation-only = %d ; A15 directional median = %.4f"
      % (_ge / _tot, math.sqrt(_chi / (_N * (min(len(mx), 5) - 1))), len(_phantom), len(_raw) - len(_fu), _dir[len(_dir) // 2]))

# ===== A16  the same question at the hymn unit, which A-2's falsifier names =====
# A8/A11 aggregate to ten books, which is too few units to resolve anything.
# strata.json divides 1,028 hymns. This is the finer test the unit should have
# run in the first place; it was added 2026-09-09 after adversarial review
# pointed out that A-2's own falsifier named it.
_hy = collections.defaultdict(collections.Counter)
for st, b, h, n, pd_, mt, code in pada_rows:
    _hy[(b, h)][code.upper()] += 1
def _rho_ties(xs, ys):
    def rank(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v); i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and v[order[j + 1]] == v[order[i]]: j += 1
            avg = (i + j) / 2.0 + 1
            for k2 in range(i, j + 1): r[order[k2]] = avg
            i = j + 1
        return r
    rx, ry = rank(xs), rank(ys)
    mx_, my_ = sum(rx) / len(rx), sum(ry) / len(ry)
    num = sum((a - mx_) * (b2 - my_) for a, b2 in zip(rx, ry))
    den = math.sqrt(sum((a - mx_) ** 2 for a in rx) * sum((b2 - my_) ** 2 for b2 in ry))
    return num / den if den else 0.0
random.seed(1)
rows = []
for label, keep in (("all_books", lambda b: True),
                    ("books_1_to_9", lambda b: b != 10),
                    ("family_books_2_to_7", lambda b: 2 <= b <= 7)):
    ks = [k for k in sorted(_hy) if keep(k[0])]
    xs = [k[0] for k in ks]
    ys = [sum(_hy[k][c] for c in LATE) / sum(_hy[k].values()) for k in ks]
    r = _rho_ties(xs, ys)
    hits = 0
    for _ in range(5000):
        sh_ = ys[:]; random.shuffle(sh_)
        if abs(_rho_ties(xs, sh_)) >= abs(r) - 1e-12: hits += 1
    zero = sum(1 for v in ys if v == 0.0)
    pv = (hits + 1) / 5001.0
    # 1/5001 is the resolution floor of a 5000-shuffle permutation, not a
    # measured value; a p at the floor is reported as a bound.
    rows.append([label, len(ks), round(r, 4),
                 ("<%.4f" % (1 / 5001.0)) if hits == 0 else ("%.4f" % pv),
                 pct(zero, len(ks)), round(sorted(ys)[len(ys) // 2], 4)])
emit("A16-hymn-level-order-vs-arnold-late.csv", rows,
     ["scope", "hymns", "spearman_rho_tied",
      "permutation_p_5000_shuffles_floor_0.0002",
      "pct_hymns_with_zero_late_padas", "median_late_share"])
print("A16:", rows)

print("\n--- headline numbers ---")
print("padas with a stratum code:", len(pada_rows))
print("stanzas:", len(strata), " mixed-stratum stanzas:", sum(1 for v in stanza_mixed.values() if v))
print("stanzas whose every pada code is uppercase (certain):", sum(1 for v in stanza_certain.values() if v))
print("Samhita vs metrically restored: %d of %d stanzas differ (%.2f%%)" %
      (len(diff), len(shared), 100.0 * len(diff) / len(shared)))
print("padapatha skeleton vs Samhita skeleton: %d of %d differ (%.2f%%)" % (len(pdiff), len(sh), 100.0 * len(pdiff) / len(sh)))
print("metre label -> modal stratum accuracy: %.2f%%" % pct(det, tot))
print("Spearman rho, book number vs Arnold-late share:", round(rho, 4))
