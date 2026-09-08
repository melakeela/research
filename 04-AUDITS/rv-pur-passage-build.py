#!/usr/bin/env python3
"""
rv-pur-passage-build.py — build the §4J passage index for the púr- corpus.

Constitution §4J asks for a corpus of *passages*, with fifteen enumerated
items per passage. 03-REGISTERS/rigveda-pur-family-occurrences.csv is an
index of *tokens*. This script fixes the passage as the stanza and assembles,
for every stanza containing a púr-family token, the text in four editions,
nine translations, the hymn's addressee and poet-group heading, the Arnold
metre and stratum of each of its pādas, and the five scholars' stanza-level
judgements.

It extracts. It does not interpret: no field here says what a passage means,
who held a fort, or where one was. Those are separate units and separate
registers.

Sources (02-SOURCES/access-ledger.csv):
  SRC-019/069 clone @ d3eb8af7324338161520d2d35eae8f7e985a19a5
  SRC-020 aufrecht.csv        SRC-021 padapatha.csv, lubotsky.csv
  SRC-022 zurich token layer   SRC-023 strata.json
  SRC-070 addressees.json      SRC-071 stanza_properties.json
  SRC-072 geldner  SRC-073 griffith  SRC-074 grassmann
  SRC-075 elizarenkova  SRC-076 renou  SRC-077 macdonell/mueller/oldenberg
  SRC-078 vnh.csv

Input:  rv_tokens_vedaweb.tsv, from 04-AUDITS/rv-token-extract.py
Output: rv_pur_passages.json  (one object per passage, all layers attached)
"""
import csv, json, os, sys, collections

csv.field_size_limit(10 ** 8)

CLONE = sys.argv[1] if len(sys.argv) > 1 else \
    "/home/user/vedawebproject/vedaweb-data/rigveda"
TOKENS = sys.argv[2] if len(sys.argv) > 2 else "rv_tokens_vedaweb.tsv"
OUT = sys.argv[3] if len(sys.argv) > 3 else "rv_pur_passages.json"

# The seven lemmas of the register's family (PUR-006). pūrbhíttama- is the
# superlative of pūrbhíd- and shares its Grassmann id; the register counts
# them as one lemma, so the family is seven lemmas over eight lemma strings.
FAMILY = {"púr-", "puraṃdará-", "pūrbhíd-", "pūrbhíttama-",
          "pūrbhídya-", "pū́rpati-", "purohán-", "púrya-"}


def read_tsv(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def pada_keyed(path):
    """versions/*.csv with columns stanza, pada, text.

    QUOTE_NONE is load-bearing. These are plain tab-separated files with no
    quoting convention, and Geldner, Grassmann and Griffith all open direct
    speech with a bare '"'. Under the csv default that character starts a
    quoted field, and the reader swallows every following line until the next
    one — silently merging rows and attaching one stanza's translation to
    another. Five Geldner rows and one Grassmann row vanished this way before
    the flag was set, and the surviving neighbours were wrong rather than
    merely absent.
    """
    out = collections.defaultdict(dict)
    with open(os.path.join(CLONE, path), encoding="utf-8", newline="") as f:
        for row in csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
            if len(row) >= 3:
                out[row[0]][row[1]] = row[2]
    return out


def stanza_keyed(path, joiner=" "):
    """One row per stanza: stanza, text. Multi-row files are joined.

    QUOTE_NONE for the reason given on pada_keyed.
    """
    out = collections.defaultdict(list)
    with open(os.path.join(CLONE, path), encoding="utf-8", newline="") as f:
        for row in csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
            if len(row) >= 2:
                out[row[0]].append(row[-1])
    return {k: joiner.join(v) for k, v in out.items()}


def main():
    toks = read_tsv(TOKENS)
    fam = [t for t in toks if t["lemma"] in FAMILY]

    by_stanza = collections.defaultdict(list)
    for t in toks:
        by_stanza[t["stanza"]].append(t)

    stanzas = sorted({t["stanza"] for t in fam})

    aufrecht = pada_keyed("versions/aufrecht.csv")
    vnh = pada_keyed("versions/vnh.csv")
    lubotsky = pada_keyed("versions/lubotsky.csv")
    padapatha = stanza_keyed("versions/padapatha.csv")

    tr = {}
    for name, path, join in (
        ("geldner", "translations/deu/geldner.csv", " "),
        ("griffith", "translations/eng/griffith.csv", " "),
        ("grassmann", "translations/deu/grassmann.csv", " "),
        ("elizarenkova", "translations/rus/elizarenkova.csv", " "),
        ("renou", "translations/fra/renou.csv", " "),
        ("macdonell", "translations/eng/macdonell.csv", " "),
        ("mueller", "translations/eng/mueller.csv", " "),
        ("oldenberg_tr", "translations/eng/oldenberg.csv", " "),
        ("otto", "translations/deu/otto.csv", " "),
    ):
        tr[name] = stanza_keyed(path, join)

    with open(os.path.join(CLONE, "info/addressees.json"), encoding="utf-8") as f:
        addressees = json.load(f)
    with open(os.path.join(CLONE, "info/stanza_properties.json"), encoding="utf-8") as f:
        props = json.load(f)

    out = []
    for i, sid in enumerate(stanzas, 1):
        book, hymn, stz = sid.split(".")
        hid = "%s.%s" % (book, hymn)
        stoks = sorted(by_stanza[sid], key=lambda t: (t["pada"], int(t["tok_i"])))
        ftoks = [t for t in stoks if t["lemma"] in FAMILY]

        padas = sorted({t["pada"] for t in stoks})
        strata = {}
        for p in padas:
            pt = [t for t in stoks if t["pada"] == p]
            strata[p] = {"metre": pt[0]["metre"], "stratum": pt[0]["stratum"]}
        codes = {v["stratum"] for v in strata.values() if v["stratum"]}

        add = addressees.get(hid, [])
        addressee = add[0][1] if len(add) > 0 and len(add[0]) > 1 else ""
        group = add[1][1] if len(add) > 1 and len(add[1]) > 1 else ""

        out.append({
            "passage_id": "PUR-P-%03d" % i,
            "stanza": sid,
            "book": int(book), "hymn": int(hymn), "stanza_n": int(stz),
            "hymn_id": hid,
            "n_family_tokens": len(ftoks),
            "family": [{
                "pada": t["pada"], "tok_i": int(t["tok_i"]),
                "surface": t["surface"], "lemma": t["lemma"],
                "lemma_id": t["lemma_id"], "morph": t["morph"],
                "gramm": t["gramm"],
            } for t in ftoks],
            "n_padas": len(padas),
            "padas": padas,
            "strata": strata,
            "stratum_codes": sorted(codes),
            "stratum_uniform": len(codes) <= 1,
            "text": {
                "aufrecht": {p: aufrecht.get(sid, {}).get(p, "") for p in
                             sorted(aufrecht.get(sid, {}))},
                "vnh": {p: vnh.get(sid, {}).get(p, "") for p in
                        sorted(vnh.get(sid, {}))},
                "lubotsky": {p: lubotsky.get(sid, {}).get(p, "") for p in
                             sorted(lubotsky.get(sid, {}))},
                "padapatha": padapatha.get(sid, ""),
            },
            "translations": {k: v.get(sid, "") for k, v in tr.items()},
            "addressee": addressee,
            "poet_group": group,
            "stanza_properties": props.get(sid, {}),
            "tokens": [{
                "pada": t["pada"], "tok_i": int(t["tok_i"]),
                "surface": t["surface"], "lemma": t["lemma"],
                "morph": t["morph"], "gramm": t["gramm"],
            } for t in stoks],
        })

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)

    # ---- denominators and exclusions, printed so they are never implicit ----
    print("family tokens           : %d" % len(fam), file=sys.stderr)
    print("distinct padas          : %d" %
          len({(t["stanza"], t["pada"]) for t in fam}), file=sys.stderr)
    print("distinct stanzas (rows) : %d" % len(stanzas), file=sys.stderr)
    print("distinct hymns          : %d" %
          len({(t["book"], t["hymn"]) for t in fam}), file=sys.stderr)
    c = collections.Counter(t["stanza"] for t in fam)
    print("stanzas carrying >1 family token: %s" %
          sorted((k, v) for k, v in c.items() if v > 1), file=sys.stderr)
    miss = collections.Counter()
    for r in out:
        for k, v in r["translations"].items():
            if not v:
                miss[k] += 1
        for k in ("aufrecht", "vnh", "lubotsky"):
            if not r["text"][k]:
                miss["text:" + k] += 1
        if not r["text"]["padapatha"]:
            miss["text:padapatha"] += 1
        if not r["addressee"]:
            miss["addressee"] += 1
        if not r["poet_group"]:
            miss["poet_group"] += 1
    print("absent per layer, of %d passages: %s" %
          (len(out), dict(sorted(miss.items()))), file=sys.stderr)
    print("non-uniform stratum passages: %s" %
          [r["stanza"] for r in out if not r["stratum_uniform"]], file=sys.stderr)
    print("-> %s (%d passages)" % (OUT, len(out)), file=sys.stderr)


if __name__ == "__main__":
    main()
