#!/usr/bin/env python3
"""
Aggregate the output of 04-AUDITS/rv-retroflex-classify.py.

Produces, all from the pinned VedaWeb corpus (SRC-019/022/023/047):

  1. a formal sub-typology of the UNCONDITIONED residue, on string
     criteria only -- no etymology is asserted;
  2. the distribution of that residue over Arnold's five metrical strata
     and over the ten books, at token level AND at lemma (type) level;
  3. chi-square on the type-level tables, which is the unit a
     vocabulary-stratification claim is actually about.

Usage: rv-retroflex-aggregate.py rv_retroflex-lemmas.tsv rv_tokens_vedaweb.tsv
"""
import csv, sys, collections, math

LEM = sys.argv[1] if len(sys.argv) > 1 else "rv_retroflex-lemmas.tsv"
TOK = sys.argv[2] if len(sys.argv) > 2 else "rv_tokens_vedaweb.tsv"

STRATA = [("A", "Archaic"), ("S", "Strophic"), ("N", "Normal"),
          ("C", "Cretic"),  ("P", "Popular")]
RETRO_STOP = {"ṭ", "ṭh", "ḍ", "ḍh", "ḷ", "ḷh"}


def chisq(obs, exp):
    return sum((o - e) ** 2 / e for o, e in zip(obs, exp) if e > 0)


def p_from_chisq(x2, df):
    """Upper tail of chi-square. Exact for even df, series for odd."""
    if x2 <= 0:
        return 1.0
    if df % 2 == 0:
        k, term, s = df // 2, 1.0, 1.0
        for i in range(1, k):
            term *= (x2 / 2) / i
            s += term
        return math.exp(-x2 / 2) * s
    # odd df: regularised upper incomplete gamma by continued fraction
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


def subtype(row):
    """Formal sub-typology of an UNCONDITIONED lemma. String criteria only.
    Each name records the shape of the residue, NOT a derivation."""
    segs = row["segments"].split()
    rules = row["rules"] or ""
    tags = []
    for part in rules.split("; "):
        if "=UNCONDITIONED" not in part:
            continue
        ph = part.split("=", 1)[0]
        idx = None
        for i, s in enumerate(segs):
            if s == ph:
                idx = i
                break
        if ph == "ṣ" and "word-initial" in part:
            tags.append("F4-initial-ṣ")
        elif ph == "ṣ" and idx is not None and idx + 1 < len(segs) \
                and segs[idx + 1] in RETRO_STOP:
            tags.append("F1-ṣṬ-cluster")
        elif ph in ("ḷh", "ḍh"):
            tags.append("F2-aspirated-retroflex")
        elif row["bare"].startswith("dū"):
            tags.append("F3-dū-compound")
        else:
            tags.append("F5-residue")
    if row["bare"].startswith("dū") and "F5-residue" in tags:
        tags = ["F3-dū-compound" if t == "F5-residue" else t for t in tags]
    # a lemma counts as residue only if no unconditioned segment is
    # accounted for by F1-F4
    return "F5-residue" if all(t == "F5-residue" for t in tags) \
        else "+".join(sorted(set(t for t in tags if t != "F5-residue")))


def main():
    lem = {}
    with open(LEM, encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            for k in r:
                if r[k] is None:
                    r[k] = ""
            lem[r["lemma"]] = r

    # ---------------------------------------------- 1. sub-typology
    unc = [r for r in lem.values() if r["category"] == "UNCONDITIONED"]
    sub = collections.Counter()
    subtok = collections.Counter()
    for r in unc:
        t = subtype(r)
        r["subtype"] = t
        sub[t] += 1
        subtok[t] += int(r["tokens"])
    print("== UNCONDITIONED residue, formal sub-typology ==")
    print("%-28s %6s %8s" % ("class", "lemmas", "tokens"))
    for t, n in sorted(sub.items(), key=lambda x: -x[1]):
        print("%-28s %6d %8d" % (t, n, subtok[t]))
    print("%-28s %6d %8d" % ("TOTAL", len(unc), sum(subtok.values())))

    # ---------------------------------------------- token-level tables
    rows = list(csv.DictReader(open(TOK, encoding="utf-8"), delimiter="\t"))
    cat_of = {L: r["category"] for L, r in lem.items()}

    print("\n== token level, by Arnold stratum ==")
    tot = collections.Counter(); hit = collections.Counter()
    for r in rows:
        s = r["stratum"].upper()
        tot[s] += 1
        if cat_of.get(r["lemma"]) == "UNCONDITIONED":
            hit[s] += 1
    N, H = sum(tot[c] for c, _ in STRATA), sum(hit[c] for c, _ in STRATA)
    print("%-10s %9s %9s %9s %9s" % ("stratum", "tokens", "unc", "per 10k", "expected"))
    obs, exp = [], []
    for c, name in STRATA:
        e = H * tot[c] / N
        obs.append(hit[c]); exp.append(e)
        print("%-10s %9d %9d %9.2f %9.1f"
              % (name, tot[c], hit[c], 1e4 * hit[c] / tot[c], e))
    print("%-10s %9d %9d %9.2f" % ("ALL", N, H, 1e4 * H / N))
    x2 = chisq(obs, exp)
    print("chi2 = %.2f on 4 df, p = %.3g  (tokens are not independent)"
          % (x2, p_from_chisq(x2, 4)))

    print("\n== token level, by book ==")
    tb = collections.Counter(); hb = collections.Counter()
    for r in rows:
        tb[int(r["book"])] += 1
        if cat_of.get(r["lemma"]) == "UNCONDITIONED":
            hb[int(r["book"])] += 1
    print("book   " + " ".join("%6d" % b for b in range(1, 11)))
    print("per10k " + " ".join("%6.1f" % (1e4 * hb[b] / tb[b]) for b in range(1, 11)))
    fam = sum(hb[b] for b in range(2, 8)); famt = sum(tb[b] for b in range(2, 8))
    oth = sum(hb[b] for b in (1, 8, 9, 10)); otht = sum(tb[b] for b in (1, 8, 9, 10))
    print("family books 2-7: %.2f per 10k;  rest: %.2f per 10k"
          % (1e4 * fam / famt, 1e4 * oth / otht))
    e1 = (fam + oth) * famt / (famt + otht)
    e2 = (fam + oth) * otht / (famt + otht)
    x2b = chisq([fam, oth], [e1, e2])
    print("chi2 = %.2f on 1 df, p = %.3g" % (x2b, p_from_chisq(x2b, 1)))

    # ---------------------------------------------- type-level tables
    # every lemma is assigned the stratum holding most of its tokens;
    # lemmas with no single majority stratum are reported separately.
    print("\n== type level: lemmas assigned to their majority stratum ==")
    maj = {}
    for L, r in lem.items():
        d = dict()
        for part in (r["strata"] or "").split(","):
            if ":" in part:
                k, v = part.split(":"); d[k] = int(v)
        if not d:
            continue
        top = max(d.values()); best = [k for k, v in d.items() if v == top]
        maj[L] = best[0] if len(best) == 1 else "TIE"
    tl = collections.Counter(); ul = collections.Counter()
    for L, s in maj.items():
        tl[s] += 1
        if lem[L]["category"] == "UNCONDITIONED":
            ul[s] += 1
    N2 = sum(tl[c] for c, _ in STRATA); U2 = sum(ul[c] for c, _ in STRATA)
    print("%-10s %8s %8s %9s %9s" % ("stratum", "lemmas", "unc", "%", "expected"))
    obs2, exp2 = [], []
    for c, name in STRATA:
        e = U2 * tl[c] / N2
        obs2.append(ul[c]); exp2.append(e)
        print("%-10s %8d %8d %8.2f%% %9.1f" % (name, tl[c], ul[c],
                                               100.0 * ul[c] / tl[c], e))
    print("%-10s %8d %8d %8.2f%%" % ("ALL", N2, U2, 100.0 * U2 / N2))
    print("(%d lemmas tied across strata and excluded)" % tl["TIE"])
    x2t = chisq(obs2, exp2)
    print("chi2 = %.2f on 4 df, p = %.3g   <- the figure to quote"
          % (x2t, p_from_chisq(x2t, 4)))

    # ---------------------------------------------- restricted-vocabulary test
    print("\n== type level: lemmas confined to one part of the corpus ==")
    def books_of(r):
        out = set()
        for part in (r["books"] or "").split(","):
            if ":" in part:
                out.add(int(part.split(":")[0]))
        return out
    groups = {"only in books 2-7": lambda b: b and b <= {2,3,4,5,6,7},
              "only in book 10":   lambda b: b == {10},
              "only in book 1":    lambda b: b == {1},
              "only in books 8-9": lambda b: b and b <= {8, 9}}
    print("%-20s %8s %8s %8s" % ("group", "lemmas", "unc", "%"))
    for name, test in groups.items():
        tot_g = unc_g = 0
        for L, r in lem.items():
            b = books_of(r)
            if test(b):
                tot_g += 1
                if r["category"] == "UNCONDITIONED":
                    unc_g += 1
        print("%-20s %8d %8d %7.2f%%" % (name, tot_g, unc_g,
                                         100.0 * unc_g / tot_g if tot_g else 0))

    with open("rv_retroflex-unconditioned.tsv", "w", encoding="utf-8") as f:
        f.write("\t".join(["lemma","lemma_id","gramm","segments","subtype",
                           "rules","tokens","hymns","books","strata",
                           "majority_stratum","gloss"]) + "\n")
        for r in sorted(unc, key=lambda x: (-int(x["tokens"]), x["lemma"])):
            f.write("\t".join([r["lemma"], r["lemma_id"], r["gramm"],
                               r["segments"], r["subtype"], r["rules"],
                               r["tokens"], r["hymns"], r["books"],
                               r["strata"], maj.get(r["lemma"], ""),
                               r["gloss"]]) + "\n")
    print("\nwrote rv_retroflex-unconditioned.tsv (%d rows)" % len(unc))


if __name__ == "__main__":
    main()
