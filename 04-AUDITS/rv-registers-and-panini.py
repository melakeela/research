#!/usr/bin/env python3
"""
rv-registers-and-panini.py — two smaller domain-A measurements.

P.  Panini's chandas rules, counted. Constitution s.4.A asks what the
    chandasi rules imply. The first thing they imply is a proportion, and
    the proportion is countable.
    Source: ashtadhyayi-com/data @ 24109f7, sutraani/data.txt      SRC-098
    A community edition with no stated critical apparatus: these are
    counts over that file, not over a critical edition of the Astadhyayi.

M.  The instrumental plural of a-stems, -ebhih against -aih. The standard
    diagnostic pair, used by Arnold himself and re-tested with a metrical
    control in Hellwig, Scarlata and Widmer 2021. Measured here by book,
    by Arnold stratum, and by position in the pada, because the whole
    point of the 2021 paper is that the third of those confounds the
    first two.
    Source: the Zurich token layer, rv_tokens.tsv              SRC-019/022

Reads only.
"""
import csv, json, os, sys, collections, unicodedata
from scipy.stats import chi2_contingency, fisher_exact

SUTRA = sys.argv[1] if len(sys.argv) > 1 else \
    "/home/user/ashtadhyayi-com_data/sutraani/data.txt"
TOK   = sys.argv[2] if len(sys.argv) > 2 else "rv_tokens.tsv"
OUT   = sys.argv[3] if len(sys.argv) > 3 else "."


def w(name, header, rows):
    with open(os.path.join(OUT, name), "w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f, delimiter="\t", lineterminator="\n")
        wr.writerow(header); wr.writerows(rows)


def pct(a, b):
    return 0.0 if not b else 100.0 * a / b


# ============================================================== P: Panini
sut = json.load(open(SUTRA, encoding="utf-8"))["data"]
N = len(sut)
CHANDAS = "छन्दस"
OTHER = {"मन्त्रे": "mantre", "निगमे": "nigame", "ब्राह्मणे": "brahmane",
         "ऋचि": "rci", "यजुषि": "yajusi"}

# Finding S of the 2026-09-07 adversarial review. A substring match on
# "chandas-" catches two different things: the locative scope marker
# chandasi, "in the Vedic", which is what this measurement is about; and
# chandas- as an ordinary stem inside a rule that is ABOUT the word, e.g.
# 4.3.71 chandaso yad-anau. The second is not a Vedic-scope rule. The
# scope-marker form is counted separately so the headline is a range, not
# a point.
SCOPE_FORMS = ("छन्दसि",)
explicit = {r["i"] for r in sut if CHANDAS in (r.get("s") or "")}
scope_marker = {r["i"] for r in sut
                if any(f in (r.get("s") or "") for f in SCOPE_FORMS)}
about_the_word = explicit - scope_marker
inherited = {r["i"] for r in sut if CHANDAS in (r.get("an") or "")}
other = {r["i"] for r in sut
         if any(k in (r.get("s") or "") for k in OTHER)}
scope = explicit | inherited

print("P   Panini's Vedic-scope rules, counted over %d sutras" % N)
print("    'chandas-' in the sutra's own text          : %4d (%.2f%%)"
      % (len(explicit), pct(len(explicit), N)))
print("    'chandas-' carried in by anuvrtti           : %4d (%.2f%%)"
      % (len(inherited), pct(len(inherited), N)))
print("    union, rules operating in the Vedic register: %4d (%.2f%%)"
      % (len(scope), pct(len(scope), N)))
for k, v in OTHER.items():
    n = sum(1 for r in sut if k in (r.get("s") or ""))
    print("    other Vedic scope words: %-10s %-10s      %4d" % (k, v, n))
print("    union with those as well                    : %4d (%.2f%%)"
      % (len(scope | other), pct(len(scope | other), N)))
print()
print("    the two senses of chandas-, separated:")
print("      in the locative scope form chandasi           : %4d" % len(scope_marker))
print("      other chandas- forms in a sutra's own text    : %4d" % len(about_the_word))
for r in sut:
    if r["i"] in about_the_word:
        print("        %s.%s.%s  %s" % (r["a"], r["p"], r["n"], r.get("s", "")))
print("    Some of the second group are rules ABOUT the word chandas, not")
print("    rules operating in the Vedic register. The union of 253 is")
print("    therefore an UPPER BOUND. The lower bound, taking only the")
print("    locative scope form and its anuvrtti inheritance, is %d (%.2f%%)."
      % (len(scope_marker | inherited), pct(len(scope_marker | inherited), N)))

by_adhyaya = collections.Counter(r["a"] for r in sut if r["i"] in scope)
tot_adhyaya = collections.Counter(r["a"] for r in sut)
print("    by adhyaya:")
rows = []
for a in sorted(tot_adhyaya, key=int):
    rows.append([a, tot_adhyaya[a], by_adhyaya[a],
                 "%.2f" % pct(by_adhyaya[a], tot_adhyaya[a])])
    print("       %s: %4d sutras, %3d in Vedic scope (%.2f%%)"
          % (a, tot_adhyaya[a], by_adhyaya[a],
             pct(by_adhyaya[a], tot_adhyaya[a])))
w("p1-panini-chandas-scope.tsv",
  ["adhyaya", "sutras", "vedic_scope", "pct"], rows)
w("p2-panini-chandas-sutras.tsv",
  ["sutra_id", "adhyaya", "pada", "number", "sutra", "explicit", "by_anuvrtti"],
  [[r["i"], r["a"], r["p"], r["n"], r.get("s", ""),
    int(r["i"] in explicit), int(r["i"] in inherited)]
   for r in sut if r["i"] in scope])

# ================================================ M: -ebhih against -aih
rows = list(csv.DictReader(open(TOK, newline="", encoding="utf-8"), delimiter="\t"))
print()
print("M   instrumental plural of a-stems: -ebhih against -aih")


def strip_acc(s):
    """Remove the Vedic pitch accents, keep every other diacritic.

    NFD then NFC: the visarga is a precomposed character, so a decomposed
    string will not match a composed literal.
    """
    d = unicodedata.normalize("NFD", s)
    return unicodedata.normalize(
        "NFC", "".join(c for c in d if c not in {"\u0301", "\u0300"}))


# Nominal a-stems only. The -ebhih / -aih alternation is a property of that
# class: ri-stems, i-stems and consonant stems take -bhih with no alternant.
#
# Finding J of the 2026-09-07 adversarial review. An earlier version of this
# filter tested only the lemma ending, which admitted 72 PRONOMINAL tokens
# (sa- ~ ta-, ya-, sva-, sya- ~ tya-, ka-). Pronominal stems take -ebhih
# almost categorically, and every one of their non-final tokens sits on the
# -ebhih side, so they load directly onto the position effect that is this
# measurement's whole result. They are excluded by gramm, and the figures
# with them included are printed alongside so the difference is visible.
def is_a_stem(r):
    return strip_acc(r["lemma"]).endswith("a-")

ins_all = [r for r in rows
           if "case=INS" in r["morph"] and "number=PL" in r["morph"]
           and strip_acc(r["lemma"]).endswith(("a-", "\u0101-"))]
ins = [r for r in rows
       if "case=INS" in r["morph"] and "number=PL" in r["morph"]
       and is_a_stem(r) and r["gramm"] != "pronoun"]
n_pron = sum(1 for r in ins_all if r["gramm"] == "pronoun")
n_long = sum(1 for r in ins_all if not is_a_stem(r))
print("    instrumental plural tokens whose lemma ends -a- or -ā-: %d"
      % len(ins_all))
print("      of those, pronouns excluded : %d" % n_pron)
print("      of those, ā-stems excluded  : %d" % n_long)
EBHIH = ("ebhiḥ", "ebhir", "ebhis")
AIH   = ("aiḥ", "air", "ais")
pairs = []
for r in ins:
    s = strip_acc(r["surface"])
    if s.endswith(EBHIH):
        pairs.append((r, "ebhih"))
    elif s.endswith(AIH):
        pairs.append((r, "aih"))
print("    nominal a-stem instrumental plural tokens: %d" % len(ins))
print("    of which end in -ebhih or -aih                : %d" % len(pairs))

# pada-final position: is this token the last of its pada?
last = {}
for r in rows:
    k = (r["stanza"], r["pada"])
    last[k] = max(last.get(k, 0), int(r["tok_i"]))


def variant_table(keyf, label):
    agg = collections.defaultdict(collections.Counter)
    for r, v in pairs:
        agg[keyf(r)][v] += 1
    ks = sorted(agg, key=lambda x: (x == "", x))
    tab = [[agg[k]["ebhih"], agg[k]["aih"]] for k in ks]
    out = []
    print("    -- by %s" % label)
    for k, t in zip(ks, tab):
        n = t[0] + t[1]
        out.append([label, k, t[0], t[1], n, "%.1f" % pct(t[0], n)])
        print("       %-10s -ebhih %4d  -aih %4d  n=%4d  archaic share %5.1f%%"
              % (k or "(none)", t[0], t[1], n, pct(t[0], n)))
    live = [t for t in tab if sum(t) >= 5]
    if len(live) > 1:
        chi2, p, dof, _ = chi2_contingency(live)
        exp = chi2_contingency(live)[3]
        thin = (exp < 5).sum()
        note = ""
        if thin:
            # Finding K: an expected cell below 5 makes the asymptotic
            # chi-square unreliable. Report a Monte Carlo p as well.
            p_mc = simulated_p(live)
            note = "  [%d expected cells < 5; Monte Carlo p = %.3g]" % (thin, p_mc)
        print("       chi-square %.1f, %d df, p = %.3g%s" % (chi2, dof, p, note))
        print("       smallest group n = %d" % min(sum(t) for t in live))
    return out


def simulated_p(table, reps=20000, seed=20260907):
    """Monte Carlo p for independence, conditioning on the margins."""
    import random
    obs = chi2_contingency(table)[0]
    rowt = [sum(r) for r in table]
    colt = [sum(c) for c in zip(*table)]
    n = sum(rowt)
    pool = []
    for j, ct in enumerate(colt):
        pool += [j] * ct
    rnd = random.Random(seed)
    hits = 0
    for _ in range(reps):
        rnd.shuffle(pool)
        sim, k = [], 0
        for rt in rowt:
            chunk = pool[k:k + rt]; k += rt
            sim.append([chunk.count(j) for j in range(len(colt))])
        try:
            if chi2_contingency(sim)[0] >= obs:
                hits += 1
        except ValueError:
            pass
    return (hits + 1) / (reps + 1)


out = []
out += variant_table(lambda r: int(r["book"]), "book")
out += variant_table(lambda r: r["stratum"].upper(), "stratum")
out += variant_table(
    lambda r: "pada-final" if int(r["tok_i"]) == last[(r["stanza"], r["pada"])]
    else "not final", "position")
w("m9-ebhih-vs-aih.tsv",
  ["grouping", "value", "ebhih", "aih", "n", "pct_ebhih"], out)

# the control: does the stratum effect survive inside one position?
print()
print("    -- the control: stratum effect inside each pada position")
for posname, want in (("pada-final", True), ("not final", False)):
    agg = collections.defaultdict(collections.Counter)
    for r, v in pairs:
        isf = int(r["tok_i"]) == last[(r["stanza"], r["pada"])]
        if isf == want:
            agg[r["stratum"].upper()][v] += 1
    ks = [k for k in sorted(agg) if sum(agg[k].values()) >= 5]
    tab = [[agg[k]["ebhih"], agg[k]["aih"]] for k in ks]
    if len(tab) > 1:
        chi2, p, dof, exp = chi2_contingency(tab)
        thin = (exp < 5).sum()
        p_mc = simulated_p(tab)
        print("       %-10s  %s"
              % (posname, "  ".join("%s %.0f%%" % (k, pct(t[0], sum(t)))
                                    for k, t in zip(ks, tab))))
        print("                   chi-square %.1f, %d df, p = %.3g | "
              "Monte Carlo p = %.3g | %d expected cells < 5 | smallest n = %d"
              % (chi2, dof, p, p_mc, thin, min(sum(t) for t in tab)))
        print("                   %d tests are run on these 1,2xx tokens in "
              "total; Bonferroni on 5 gives p = %.3g"
              % (5, min(1.0, p_mc * 5)))
