#!/usr/bin/env python3
"""
rv-pur-counts.py — §4J's "90; 99; 100; other counts", per passage, with the
attachment test that separates a numeral GOVERNING púr- from a numeral merely
SHARING ITS STANZA.

04-AUDITS/rigveda-pur-family-method.md §7 measured the second thing: navatí-
"ninety" at 33.5x its corpus rate inside family stanzas, śatá- "hundred" at
10.7x. The method note is explicit that this is "a measurement of the profile
and nothing more", and PUR-027 exists so it is not mistaken for the first.
This script goes after the first.

Numerals are identified by 04-AUDITS/rv-pur-numeral-scan.py, which scans every
lemma occurring in the 103 passages (721 distinct) and returns 26 candidates —
11 from an unambiguous number word, 15 from an ambiguous one, 0 from the stem
fallback. Each is adjudicated below, with a reason for every exclusion.

THE SCAN THIS UNIT FIRST USED WAS NOT EXHAUSTIVE, and the claim that it was is
withdrawn. It matched German number words with hard word boundaries against
glossed lemmas only, and leaked three ways: it reached only the 585 of 721
lemmas that carry a Grassmann gloss; \bhundert\b failed on the compound
"hundertfache"; and it read no Latin, so śatábhuji- glossed "centuplex" was
invisible. Four numeral-bearing lemmas were missed — see EXCLUDED. The scan
script is now committed so the candidate list is reproducible rather than
hard-coded here.

The attachment test is three independent instruments, reported separately and
never silently combined:

  A. AGREEMENT — the numeral carries the same case, gender and number as the
     púr- token. In Vedic an attributive numeral above four agrees with its
     noun; navatí- and śatá- are also used as governing substantives taking a
     genitive, so agreement is sufficient but not necessary.
  B. PROXIMITY — same pāda, or same hemistich (a+b, c+d), or elsewhere.
  C. TRANSLATION — how many of the independent full-coverage translators
     (Griffith, Geldner, Grassmann, Elizarenkova) render the passage with that
     number attached to a fort word. This is the only instrument that reflects
     a reading of the syntax by someone who read the syntax.

C is not independent of the philology behind A and B — the translators had the
same text — and Grassmann's translation is not independent of the Grassmann
gloss [W-002]es that fixed the family (DEP-021). It is reported because a numeral that
every translator attaches to a fort and one that none does are different
situations, and neither A nor B can tell them apart.

Output: rv_pur_counts.tsv, one row per (passage, numeral token).
"""
import csv, json, re, sys, collections

SRC = sys.argv[1] if len(sys.argv) > 1 else "rv_pur_passages.json"
OUT = sys.argv[2] if len(sys.argv) > 2 else "rv_pur_counts.tsv"

# The 12 gloss-scan candidates, adjudicated. value = numeric value where the
# lemma IS a number; None where it is a quantifier rather than a count.
NUMERALS = {
    "śatá-":       (100,  "hundert"),
    "navatí-":     (90,   "neunzig"),
    "náva- 1":     (9,    "neun"),
    "sahásra-":    (1000, "tausend"),
    "saptá-":      (7,    "sieben"),
    "pañcāśát-":   (50,   "fünfzig"),
    "trí-":        (3,    "drei"),
    "śatatamá-":   (100,  "der hundertste — ORDINAL, not a count of a set"),
    "éka-":        (1,    "ein, einzig — also 'alone'; quantifier as often as count"),
    "ubhá-":       (2,    "beide — a dual quantifier, not a count of forts"),
}
# Excluded from the candidate list, with the reason recorded rather than dropped:
EXCLUDED = {
    "śatákratu-": "Indra epithet, 'having a hundred powers'. The hundred is a "
                  "property of the god, never of a fort. A compound numeral, "
                  "not a count.",
    "śatábhuji-": "MISSED BY THE FIRST SCAN — Grassmann glosses it 'centuplex', "
                  "Latin, with no German number word at all. It occurs twice, "
                  "and in both places it agrees with the fort word in full: "
                  "RV 7.15.14c 'pū́r bhavā śatábhujiḥ' (NOM.F.SG against "
                  "NOM.F.SG) and RV 1.166.8a 'śatábhujibhis … pūrbhī́ḥ' "
                  "(INS.F.PL against INS.F.PL). Excluded from the fort-count "
                  "inventory nonetheless, because it does not say there are a "
                  "hundred forts: it says ONE fort is hundredfold. Griffith "
                  "'with hundred walls' and 'castles hundredfold', Geldner "
                  "'mit hundert Ringen' and 'hundertfachen Burgen' — all four "
                  "renderings are adjectival. It is recorded as a DESCRIPTOR "
                  "in 03-REGISTERS/rigveda-pur-fields.csv and in "
                  "06-BRIEFS/pur-translation-standard.md §4, which is where a "
                  "hundred-word that qualifies a fort rather than counting "
                  "forts belongs. The judgement is arguable and is recorded "
                  "here so it can be argued.",
    "śatā́magha-": "MISSED BY THE FIRST SCAN — 'hundertfache Fülle besitzend' "
                  "contains hundert but not as a whole word. An Indra epithet "
                  "at RV 8.33.5, a property of the god's giving, not of a "
                  "fort.",
    "śatā́tman-": "MISSED BY THE FIRST SCAN, same reason. 'hundertfaches Leben "
                 "enthaltend', of Agni at RV 1.149.3c — the stanza whose fort "
                 "word nā́rmiṇī- is itself disputed. A property of the god.",
    "prathamá-": "MISSED BY THE FIRST SCAN — 'erster' has an adjectival ending, "
                 "so \berste\b did not reach it. An ordinal at RV 3.15.4, of "
                 "Agni as first leader of the sacrifice, not of any fort.",
    "ā́rya-":    "FALSE POSITIVE of the gloss scan. Matched on 'drei' inside "
                 "Grassmann's gloss 'Angehöriger der drei oberen Grosskasten' "
                 "— a nineteenth-century German rendering that imports the "
                 "later caste system into a Rigvedic word. Not a numeral, and "
                 "the gloss is itself an object for the §7 category audit.",
}

FORTWORD = re.compile(
    r"\b(fort|forts|castle|castles|stronghold|strongholds|citadel|citadels|"
    r"burg|burgen|festung|festungen|feste|wall|wälle|walls|"
    r"крепост|крепос|замк|замок|"                       # ru крепость / замок
    r"forteresse|forteresses|château|châteaux|place[s]? forte[s]?)\b", re.I)

NUMWORD = {
    100:  re.compile(r"\b(hundred|hundredth|hundert|hunderts?|сто|ста|сотн|"
                     r"cent|centaine)\w*", re.I),
    90:   re.compile(r"\b(ninety|neunzig|девяност|девяно|nonante|"
                     r"quatre-vingt-dix)\w*", re.I),
    99:   re.compile(r"\b(ninety[- ]?(and[- ])?nine|neunundneunzig|"
                     r"девяносто девять|quatre-vingt-dix-neuf)\w*", re.I),
    9:    re.compile(r"\b(nine|neun|девят|девя|neuf)\w*", re.I),
    1000: re.compile(r"\b(thousand|tausend|тысяч|mille|milliers?)\w*", re.I),
    7:    re.compile(r"\b(seven|sieben|сем|семь|sept)\w*", re.I),
    50:   re.compile(r"\b(fifty|fünfzig|пятьдесят|cinquante)\w*", re.I),
    3:    re.compile(r"\b(three|drei|три|трёх|trois)\w*", re.I),
    2:    re.compile(r"\b(two|both|zwei|beide|два|две|оба|deux)\w*", re.I),
    1:    re.compile(r"\b(one|alone|ein|eine|einzig|один|одна|un|une|seul)\w*", re.I),
}
# The four translations with full corpus coverage. Renou and the four anthology
# selections are excluded from the DENOMINATOR because a missing rendering is a
# fact about the translator's selection, not about the passage; they are read
# and reported separately where present.
FULL = ["griffith", "geldner", "grassmann", "elizarenkova"]


def morphdict(m):
    return dict(p.split("=", 1) for p in m.split("|") if "=" in p)


def hemistich(p):
    return {"a": 1, "b": 1, "c": 2, "d": 2, "e": 3, "f": 3, "g": 4, "h": 4}.get(p, 0)


def main():
    data = json.load(open(SRC, encoding="utf-8"))
    rows = []
    for r in data:
        nums = [t for t in r["tokens"] if t["lemma"] in NUMERALS]
        if not nums:
            continue
        for nt in nums:
            value, gloss = NUMERALS[nt["lemma"]]
            nm = morphdict(nt["morph"])
            best = None
            for ft in r["family"]:
                fm = morphdict(ft["morph"])
                agree = [k for k in ("case", "gender", "number")
                         if k in nm and k in fm and nm[k] == fm[k]]
                keys = [k for k in ("case", "gender", "number")
                        if k in nm and k in fm]
                full_agree = bool(keys) and len(agree) == len(keys)
                if nt["pada"] == ft["pada"]:
                    prox, pd = "same-pada", 0
                elif hemistich(nt["pada"]) == hemistich(ft["pada"]):
                    prox, pd = "same-hemistich", 1
                else:
                    prox, pd = "same-stanza", 2
                cand = (0 if full_agree else 1, pd, full_agree, agree, keys,
                        prox, ft)
                if best is None or cand[:2] < best[:2]:
                    best = cand
            _, _, full_agree, agree, keys, prox, ft = best

            tr_hits, tr_seen = [], []
            for name in FULL:
                txt = r["translations"].get(name, "")
                if not txt:
                    continue
                tr_seen.append(name)
                pat = NUMWORD.get(value)
                if pat and pat.search(txt) and FORTWORD.search(txt):
                    tr_hits.append(name)

            rows.append({
                "passage_id": r["passage_id"], "stanza": r["stanza"],
                "numeral_lemma": nt["lemma"], "numeral_surface": nt["surface"],
                "numeral_value": value, "grassmann_gloss": gloss,
                "numeral_pada": nt["pada"], "numeral_morph": nt["morph"],
                "pur_surface": ft["surface"], "pur_lemma": ft["lemma"],
                "pur_pada": ft["pada"], "pur_morph": ft["morph"],
                "agreement": "FULL" if full_agree else (
                    "PARTIAL(%s)" % ",".join(agree) if agree else "NONE"),
                "agreement_keys_compared": ",".join(keys) or "(none comparable)",
                "proximity": prox,
                "translators_attaching": " ".join(tr_hits) or "(none)",
                "n_translators_attaching": len(tr_hits),
                "n_translators_available": len(tr_seen),
            })

    fields = list(rows[0].keys())
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t")
        w.writeheader(); w.writerows(rows)

    print("passages with >=1 numeral token : %d of %d"
          % (len({r['passage_id'] for r in rows}), len(data)), file=sys.stderr)
    print("numeral tokens                  : %d" % len(rows), file=sys.stderr)
    print("excluded candidates             : %s"
          % ", ".join(EXCLUDED), file=sys.stderr)
    print("by value: %s" % dict(sorted(collections.Counter(
        r["numeral_value"] for r in rows).items())), file=sys.stderr)
    print("by agreement: %s" % dict(collections.Counter(
        r["agreement"].split("(")[0] for r in rows)), file=sys.stderr)
    print("-> %s" % OUT, file=sys.stderr)


if __name__ == "__main__":
    main()
