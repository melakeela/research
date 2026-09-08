#!/usr/bin/env python3
"""
rv-pur-passages-csv.py — emit 03-REGISTERS/rigveda-pur-passages.csv from
rv_pur_passages.json (04-AUDITS/rv-pur-passage-build.py).

The passage index proper: one row per §4J passage, carrying its address, the
family tokens it contains with their morphology, the Arnold metre and stratum,
the hymn's addressee and poet-group heading, and which editions and
translations carry it. Measurements only.
"""
import csv, json, sys

SRC = sys.argv[1] if len(sys.argv) > 1 else "rv_pur_passages.json"
OUT = sys.argv[2] if len(sys.argv) > 2 else \
    "/home/user/research/03-REGISTERS/rigveda-pur-passages.csv"

# Arnold 1905 App. IV §265, verified in the register (PUR-013): uppercase =
# assigned on the full evidence; lowercase = "the corresponding period is
# indicated by the metrical variations alone".
STRATUM = {"A": "Archaic", "S": "Strophic", "N": "Normal",
           "C": "Cretic", "P": "Popular"}

FIELDS = [
    "passage_id", "stanza", "book", "hymn", "stanza_n",
    "n_family_tokens", "family_surfaces", "family_lemmas", "family_padas",
    "family_morphology",
    "n_padas", "arnold_metre_labels", "arnold_stratum_code",
    "arnold_stratum", "stratum_certainty",
    "addressee", "poet_group",
    "stanza_properties_flags",
    "samhita_text", "padapatha",
    "translations_present", "translations_absent",
    "source_id", "retrieval_date", "supports_page", "notes",
]


def main():
    data = json.load(open(SRC, encoding="utf-8"))
    rows = []
    for r in data:
        codes = r["stratum_codes"]
        code = codes[0] if codes else ""
        certainty = ("certain" if code.isupper()
                     else "metrical-variations-only" if code else "")
        auf = " / ".join(v for _, v in sorted(r["text"]["aufrecht"].items()) if v)
        present = sorted(k for k, v in r["translations"].items() if v)
        absent = sorted(k for k, v in r["translations"].items() if not v)
        rows.append({
            "passage_id": r["passage_id"],
            "stanza": r["stanza"], "book": r["book"],
            "hymn": r["hymn"], "stanza_n": r["stanza_n"],
            "n_family_tokens": r["n_family_tokens"],
            "family_surfaces": " ".join(t["surface"] for t in r["family"]),
            "family_lemmas": " ".join(t["lemma"] for t in r["family"]),
            "family_padas": " ".join(t["pada"] for t in r["family"]),
            "family_morphology": " ; ".join(
                "%s%d %s" % (t["pada"], t["tok_i"], t["morph"] or t["gramm"])
                for t in r["family"]),
            "n_padas": r["n_padas"],
            "arnold_metre_labels": " ".join(
                r["strata"][p]["metre"] for p in r["padas"]),
            "arnold_stratum_code": code,
            "arnold_stratum": STRATUM.get(code.upper(), ""),
            "stratum_certainty": certainty,
            "addressee": r["addressee"],
            "poet_group": r["poet_group"],
            "stanza_properties_flags": " ".join(sorted(r["stanza_properties"]))
                                        or "(none)",
            "samhita_text": auf,
            "padapatha": r["text"]["padapatha"],
            "translations_present": " ".join(present),
            "translations_absent": " ".join(absent) or "(none)",
            "source_id": "SRC-069; SRC-020; SRC-021; SRC-022; SRC-023; "
                         "SRC-070; SRC-071; SRC-072; SRC-073; SRC-074; "
                         "SRC-075; SRC-076; SRC-077",
            "retrieval_date": "2026-09-07",
            "supports_page": "forts (proposed)",
            "notes": "",
        })

    # per-row notes that record what the row cannot carry
    for row in rows:
        n = []
        if row["stratum_certainty"] == "metrical-variations-only":
            n.append("Arnold assigns this stanza's period on metrical "
                     "variations alone (lowercase code); lower confidence "
                     "than the uppercase assignments.")
        if int(row["n_family_tokens"]) > 1:
            n.append("Carries %s family tokens; a token-unit count would "
                     "enter this passage more than once."
                     % row["n_family_tokens"])
        if row["stanza_properties_flags"] == "(none)":
            n.append("No stanza-level lateness flag from Grassmann, "
                     "Oldenberg, Arnold 1897, Wuest or Witzel. Absence of a "
                     "flag is NOT PRODUCED, not a judgement of authenticity.")
        row["notes"] = " ".join(n)

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)
    print("%d passages -> %s" % (len(rows), OUT), file=sys.stderr)


if __name__ == "__main__":
    main()
