#!/usr/bin/env python3
"""
Every occurrence of the Rigvedic marking, incising and sign vocabulary
identified by 04-AUDITS/rv-writing-lexicon-scan.py, one row per token, with
its morphology, its Arnold stratum, Grassmann's gloss for that exact surface
form, and two independent translations of the stanza it stands in.

Source: VedaWebProject/vedaweb-data @ d3eb8af (CC-BY-4.0)
        Zurich tokens (SRC-106, SRC-107); rigveda/info/matched_lemmata.json;
        rigveda/translations/eng/griffith.csv (SRC-073);
        rigveda/translations/deu/geldner.csv (SRC-072)
Ledger: SRC-072, SRC-073, SRC-106, SRC-107; dependency DEP-021, DEP-032

WHICH LEMMAS, AND WHY NOT THE OTHERS

Included: every lemma the gloss scan adjudicated TRUE, every candidate in the
WRITING, SEALING and INCISING classes that is attested, and √takṣ-, the
corpus's ordinary verb of fashioning and hewing, because the question whether
a Rigvedic poet ever describes anyone cutting signs into a durable surface
cannot be answered without reading its passages.

Excluded, and the exclusions are judgements: citrá- (147 tokens), nā́man-
(117) and rūpá- (49). All three are frequent, all three are glossed in the
field of appearance rather than of marking, and reading them passage by
passage is owed work this unit did not do. That is recorded as a limitation
of the register, not as a finding about them.

várṇa- is excluded because this repository already holds its 23 occurrences
at 03-REGISTERS/rigveda-varna-occurrences.csv. Duplicating them here would
create two registers of one measurement.

NO SENSE IS ASSIGNED. The sense column reads NOT ASSIGNED throughout, as in
the várṇa- register: the Zurich layer carries lemma and morphology, not
sense, and this unit did not do the passage-by-passage semantic work that a
sense column would require. The two translations are printed so a reader can
see the context and disagree.

Griffith 1890 is a colonial-era English translation and Geldner 1951 a German
one; they are not independent of each other's philological tradition, and
neither is independent of Grassmann, whose glosses select the lemmas here
(DEP-021). They are shown as evidence of how the passage has been read, not
as evidence of what it means.

Usage: rv-marking-occurrences.py TOKENS_TSV VEDAWEB_RIGVEDA_DIR OUT_CSV
"""
import sys, csv, json, collections

TOK = sys.argv[1] if len(sys.argv) > 1 else "rv_tokens.tsv"
RV = sys.argv[2] if len(sys.argv) > 2 else "vedaweb/rigveda"
OUT = sys.argv[3] if len(sys.argv) > 3 else "domain-k-rigveda-marking-occurrences.csv"

LEMMAS = [
    ("√rikh-", "INCISING", "the only root in the corpus Grassmann glosses 'ritzen', to scratch or incise"),
    ("√akṣ-", "MARKING", "Grassmann's √akṣ- 1 'kennzeichnen, Ohrenmarken einstechen'; the Zurich lemma string merges it with √akṣ- 2 'erreichen (?)', so the surface form decides which is which"),
    ("√piś-", "INCISING", "'aushauen, zurechtschneiden, bilden, formen, schmücken'"),
    ("péśas-", "INCISING", "'Schmuck, Zierat, Farbe'"),
    ("√takṣ-", "INCISING", "'zimmern, behauen, hämmern' - the ordinary verb of fashioning"),
    ("√lip-", "INCISING", "'alipsata: sind angeschmiert' - the root behind the later lipi- 'script'"),
    ("√khanⁱ-", "INCISING", "'graben', to dig"),
    ("aṅká-", "MARKING", "'Haken, Klammer' - later 'mark, brand'"),
    ("lakṣá-", "MARKING", "'Einsatz (beim Würfelspiel)' - the stake in a dice game"),
    ("sálakṣman-", "MARKING", "'gleiches Merkmal habend', having the same mark"),
    ("lakṣmī́-", "MARKING", "'gutes, glückliches Zeichen'"),
    ("aṣṭakarṇá-", "MARKING", "'mit gekennzeichneten Ohren (von Rind und Ross)'"),
    ("tryàruṣa-", "MARKING", "'an drei Stellen rötlich gezeichnet'"),
    ("yakṣá-", "SIGN", "'Erscheinung, Wundererscheinung, Vorzeichen'"),
    ("yakṣabhŕ̥t-", "SIGN", "'ein Zeichen (?) tragend'"),
    ("śréṇi-", "SIGN", "'Reihe, Linie Zug, Schar, Gruppe'"),
    ("ketú-", "SIGN", "'Erscheinung, Kennzeichen, Lichterscheinung, Helle, Gestalt'"),
    ("akṣára-", "WRITING-CANDIDATE", "'unvergänglich; Silbe' - the word that later means a written character"),
    ("ákṣarā-", "WRITING-CANDIDATE", "included to keep it distinct from akṣára-: a different formation with a different gloss"),
]
CLASS = {l: (c, why) for l, c, why in LEMMAS}

rows = [l.rstrip("\n").split("\t") for l in open(TOK, encoding="utf-8")]
head, rows = rows[0], rows[1:]
c = {k: i for i, k in enumerate(head)}

md = json.load(open(f"{RV}/info/matched_lemmata.json", encoding="utf-8"))


def trans(path):
    d = {}
    for line in open(path, encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if len(p) >= 2:
            d[p[0]] = p[1]
    return d


griffith = trans(f"{RV}/translations/eng/griffith.csv")
geldner = trans(f"{RV}/translations/deu/geldner.csv")

STRATA = {"A": "Archaic", "a": "Archaic, metrical variations only",
          "S": "Strophic", "s": "Strophic, metrical variations only",
          "N": "Normal", "n": "Normal, metrical variations only",
          "C": "Cretic", "c": "Cretic, metrical variations only",
          "P": "Popular", "p": "Popular, metrical variations only"}

out, n = [], collections.Counter()
for r in rows:
    lem = r[c["lemma"]]
    if lem not in CLASS:
        continue
    cls, why = CLASS[lem]
    n[lem] += 1
    d = md.get(r[c["surface"]], {})
    st = r[c["stanza"]]
    code = r[c["stratum"]]
    out.append({
        "occ_id": "",
        "lemma_class": cls,
        "stanza": st,
        "pada": r[c["pada"]],
        "token_index": r[c["tok_i"]],
        "surface": r[c["surface"]],
        "zurich_lemma": lem,
        "grassmann_lemma": (d.get("lemma") or "").strip(),
        "grassmann_gloss": d.get("meaning", ""),
        "morphology": r[c["morph"]],
        "arnold_stratum_code": code,
        "arnold_stratum": STRATA.get(code, "not assigned"),
        "why_this_lemma": why,
        "sense": "NOT ASSIGNED",
        "griffith_1890_stanza": griffith.get(st, ""),
        "geldner_1951_stanza": geldner.get(st, ""),
        "source_id": "SRC-072; SRC-073; SRC-106; SRC-107",
        "retrieval_date": "2026-09-09",
    })

out.sort(key=lambda x: (x["lemma_class"], x["zurich_lemma"], x["stanza"],
                        x["pada"], int(x["token_index"])))
for i, r in enumerate(out, 1):
    r["occ_id"] = "DK-OCC-%03d" % i

with open(OUT, "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(out[0].keys()), quoting=csv.QUOTE_ALL)
    w.writeheader()
    w.writerows(out)

print("%d occurrences of %d lemmas -> %s" % (len(out), len(n), OUT))
for lem, _, _ in LEMMAS:
    print("  %-14s %3d" % (lem, n[lem]))
