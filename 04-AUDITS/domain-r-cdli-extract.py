#!/usr/bin/env python3
"""
domain-r-cdli-extract.py — measure the domain R textual record in the CDLI corpus.

Inputs, both retrieved 2026-09-08 and verified byte-for-byte against the
sha256 in the publisher's own Git LFS pointer file:
  cdliatf_unblocked.atf  SRC-103  sha256 2896ec25...84d836
  cdli_cat.csv           SRC-102  sha256 2e3232f7...53d09c

Why this script exists rather than a grep. A grep on these strings does not
measure what it appears to measure, and the gap is the whole point of the
domain:

  * "gug" matches 1,520 lines, of which the great majority are gug2, a
    baked good, and {u2}gug4, a plant. Carnelian is only gug written with
    the stone determinative {na4}. Not every gug is a stone.
  * "dilmun" matches 936 lines, of which the single largest form is
    GIN2-DILMUN, a unit of account, not a reference to the place.
  * "ma2-gan" also matches the divine name {d}sza-ma-gan, which has nothing
    to do with the toponym.
  * "me-luh-ha" carries at least four different determinatives across the
    corpus — {kur}, {ki}, {muszen}, {gesz} — which are four different kinds
    of thing sharing one sign sequence.

So every hit is classified by its determinative and its immediate
morphology, false positives are excluded by rule and counted, and the
excluded set is written out so the exclusion can be checked rather than
trusted.

What this script does NOT do. It does not translate. It does not lemmatise.
It does not assign a language to any object. It reports which sign sequences
occur, in which texts, of which period and provenience by CDLI's own
attribution, and in whose custody CDLI last recorded them.
"""
import csv, json, re, sys, collections, hashlib, os

SCRATCH = os.environ.get("DOMAIN_R_DATA", ".")
ATF = os.path.join(SCRATCH, "cdliatf_unblocked.atf")
CAT = os.path.join(SCRATCH, "cdli_cat.csv")
OUT = os.environ.get("DOMAIN_R_OUT", "03-REGISTERS")

EXPECT = {
    ATF: "2896ec253767fa07fcaa5424af6fc25d6a047dc30b99c95f99d57ce75384d836",
    CAT: "2e3232f75325b61c4d1e788d4d8c074c6230a947aed422110f9f35a6e353d09c",
}

# ---------------------------------------------------------------- markup

# ATF markup that carries no sign value: damage, collation, uncertainty,
# erasure and break brackets. Stripped only for matching; the raw token is
# always kept and written out so a reader can see the damage.
NOISE = re.compile(r"[#!?*\[\]<>_]")

def bare(tok):
    return NOISE.sub("", tok).strip(" ,.")

def dets(tok):
    """Determinatives, in order, as written between braces."""
    return [d.lower() for d in re.findall(r"\{([^}]*)\}", NOISE.sub("", tok))]

def core(tok):
    """The token with its determinatives removed."""
    return re.sub(r"\{[^}]*\}", "", bare(tok)).strip("-")

# ---------------------------------------------------------------- targets

def cls_meluhha(tok, d, c):
    if "muszen" in d:  return "BIRD-DETERMINATIVE"
    if "gesz" in d:    return "WOOD-DETERMINATIVE"
    if "kur" in d:     return "LAND-DETERMINATIVE (kur)"
    if "ki" in d:      return "PLACE-DETERMINATIVE (ki)"
    if c.startswith(("mes-", "ab-ba-", "ur-", "lu2-")): return "BOUND-IN-COMPOUND-OR-NAME"
    return "UNMARKED"

def cls_magan(tok, d, c):
    if c.startswith("sza-ma-gan") or "sza-ma-gan" in c: return "REJECT-DIVINE-NAME"
    if "d" in d and "sza-ma-gan" in c:                  return "REJECT-DIVINE-NAME"
    if not re.match(r"^(lu2-|mes-)?ma2?-(gan|kan)", c): return "REJECT-NOT-TOPONYM"
    if c.startswith("lu2-"): return "PERSON-OF (lu2-)"
    if "ki" in d:            return "PLACE-DETERMINATIVE (ki)"
    if c.startswith("mes-"): return "BOUND-IN-COMPOUND-OR-NAME"
    return "UNMARKED"

def cls_dilmun(tok, d, c):
    u = bare(tok).upper()
    if "GIN2-DILMUN" in u or "GIN2.DILMUN" in u: return "UNIT-OF-ACCOUNT (gin2 dilmun)"
    if not re.search(r"\b(dilmun|tilmun|ni-tuk)\b", c): return "REJECT-NOT-TOPONYM"
    if "ki" in d:                        return "PLACE-DETERMINATIVE (ki)"
    if c.startswith(("nimbar-", "gada-")) or "gada" in d: return "COMMODITY-QUALIFIER"
    if c.startswith("e2-"):              return "BOUND-IN-COMPOUND-OR-NAME"
    return "UNMARKED"

def cls_marhasi(tok, d, c):
    if "ki" in d: return "PLACE-DETERMINATIVE (ki)"
    return "UNMARKED"

def cls_lapis(tok, d, c):
    if "na4" in d: return "STONE-DETERMINATIVE ({na4})"
    if "_" in tok: return "AKKADIAN-LOGOGRAM (no {na4})"
    return "UNMARKED (may be the colour or quality term)"

def cls_carnelian(tok, d, c):
    if "na4" not in d: return "REJECT-NOT-THE-STONE"
    return "STONE-DETERMINATIVE ({na4})"

TARGETS = [
    ("MELUHHA",   re.compile(r"me-luh-ha"),                                          cls_meluhha),
    ("MAGAN",     re.compile(r"ma2?-(gan|kan)\b|ma2?-gan"),                          cls_magan),
    ("DILMUN",    re.compile(r"dilmun|tilmun|\bni-tuk\b", re.I),                     cls_dilmun),
    ("MARHASI",   re.compile(r"mar2?-ha-(szi|s,i|s,u)|bar-ah-szi|wa-ra-ah-s"),       cls_marhasi),
    ("LAPIS",     re.compile(r"za-gin3", re.I),                                      cls_lapis),
    ("CARNELIAN", re.compile(r"(?<![a-z0-9])gug(?![0-9])", re.I),                    cls_carnelian),
]

def main():
    for p, want in EXPECT.items():
        if not os.path.exists(p):
            sys.exit(f"missing input {p}; set DOMAIN_R_DATA to the directory holding it")
        h = hashlib.sha256()
        with open(p, "rb") as f:
            for blk in iter(lambda: f.read(1 << 20), b""):
                h.update(blk)
        got = h.hexdigest()
        if got != want:
            sys.exit(f"{p}: sha256 {got} != expected {want}; the input is not the retrieved file")
        print(f"ok  {os.path.basename(p)}  sha256 verified")

    occ, excluded = [], []
    pid, lineref = None, None
    with open(ATF, encoding="utf-8", errors="replace") as f:
        for raw in f:
            raw = raw.rstrip("\n")
            if raw.startswith("&"):
                m = re.match(r"&(P\d+|Q\d+)", raw)
                pid = m.group(1) if m else None
                continue
            if raw.startswith(("#", "@", "$", ">>")) or not raw.strip():
                continue
            m = re.match(r"\s*([0-9]+'?\.)\s*(.*)$", raw)
            if not m:
                continue
            lineref, body = m.group(1).rstrip("."), m.group(2)
            for tok in body.replace(",", " ").split():
                b, c, d = bare(tok), core(tok), dets(tok)
                if not b:
                    continue
                for name, pat, clsf in TARGETS:
                    if not pat.search(b):
                        continue
                    verdict = clsf(tok, d, c)
                    row = dict(target=name, p_number=pid, line_ref=lineref,
                               raw_token=tok, core=c, determinatives="|".join(d),
                               classification=verdict, line=body.strip()[:300])
                    (excluded if verdict.startswith("REJECT") else occ).append(row)
    print(f"    {len(occ)} accepted occurrences, {len(excluded)} rejected")

    # ---- join to the catalogue
    csv.field_size_limit(1 << 30)
    # The catalogue keys texts by id_text, a bare integer, while the ATF keys
    # them by zero-padded P-number: id_text "1" is the ATF's &P000001. Joining
    # the two columns as written matches nothing, which is how the first run of
    # this script reported 0 of 1688. The key is rebuilt rather than the columns
    # compared.
    want = {r["p_number"] for r in occ if r["p_number"]}
    cat = {}
    with open(CAT, newline="", encoding="utf-8", errors="replace") as f:
        for row in csv.DictReader(f):
            v = (row.get("id_text") or "").strip()
            if not v.isdigit():
                continue
            key = "P%06d" % int(v)
            if key in want:
                cat[key] = row
    missing = len(want) - len(cat)
    print(f"    catalogue join: {len(cat)} of {len(want)} P-numbers matched, {missing} absent from the catalogue")

    def cget(p, col):
        r = cat.get(p or "")
        return ((r or {}).get(col) or "").strip()

    with open(os.path.join(OUT, "domain-r-cdli-attestations.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(["att_id", "target", "classification", "p_number", "line_ref", "raw_token",
                    "determinatives", "line", "cdli_period", "cdli_provenience",
                    "cdli_collection", "cdli_museum_no", "cdli_material",
                    "cdli_excavation_no", "cdli_primary_publication", "source_id",
                    "retrieval_date"])
        for i, r in enumerate(sorted(occ, key=lambda r: (r["target"], r["classification"], r["p_number"] or "")), 1):
            p = r["p_number"]
            w.writerow(["DRA-%04d" % i, r["target"], r["classification"], p, r["line_ref"], r["raw_token"],
                        r["determinatives"], r["line"],
                        cget(p, "period"), cget(p, "provenience"), cget(p, "collection"),
                        cget(p, "museum_no"), cget(p, "material"),
                        cget(p, "excavation_no"), cget(p, "primary_publication"),
                        "SRC-103; SRC-102", "2026-09-08"])

    with open(os.path.join(OUT, "domain-r-cdli-rejected.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(["rej_id", "target", "classification", "p_number", "line_ref",
                    "raw_token", "line", "source_id", "retrieval_date"])
        for i, r in enumerate(sorted(excluded, key=lambda r: (r["target"], r["raw_token"])), 1):
            w.writerow(["DRX-%04d" % i, r["target"], r["classification"], r["p_number"],
                        r["line_ref"], r["raw_token"], r["line"], "SRC-103", "2026-09-08"])

    # ---- summary
    summ = collections.Counter((r["target"], r["classification"]) for r in occ)
    rej = collections.Counter((r["target"], r["classification"]) for r in excluded)
    texts = collections.defaultdict(set)
    for r in occ:
        texts[r["target"]].add(r["p_number"])
    print("\n  target      classification                              occ   texts")
    for (t, c), n in sorted(summ.items()):
        print(f"  {t:<11} {c:<42} {n:>5}")
    for t in sorted(texts):
        print(f"  {t}: {len(texts[t])} distinct texts")
    print("\n  rejected:")
    for (t, c), n in sorted(rej.items()):
        print(f"  {t:<11} {c:<42} {n:>5}")
    json.dump({f"{t}|{c}": n for (t, c), n in summ.items()},
              open(os.path.join(OUT, "domain-r-cdli-summary.json"), "w"), indent=1, sort_keys=True)

if __name__ == "__main__":
    main()
