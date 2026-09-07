#!/usr/bin/env python3
"""
Domain E, measurement 1: how much evidence actually stands behind each of
the eleven distinctions the constitution's §4.E requires be kept apart.

The point is not that eleven categories exist. The point is that they are
not the same size, and the programme's recorded failure was treating an
attested family and a hypothetical donor as equally standing. This script
measures the sizes from the retrieved tables and refuses to fill in the
ones it cannot measure.

Sources (02-SOURCES/access-ledger.csv):
  SRC-045  JAMBU data/dedr/dedr_new.csv     DEDR reflexes
  SRC-046  JAMBU data/dedr/pdr.csv          Proto-Dravidian after Krishnamurti
  SRC-047  JAMBU data/munda/forms.csv       attested Munda reflexes
  SRC-048  JAMBU data/munda/rau_2019.csv    Proto-Munda, Rau 2019
  SRC-049  JAMBU data/cdial/params.csv      CDIAL entry texts (Turner)
  SRC-051  lexibank/dravlex cldf/           DravLex cognate coding
  SRC-052  HOLD: the substrate literature is unretrieved

Usage:  domain-e-evidence-mass.py [JAMBU_DATA_DIR] [DRAVLEX_CLDF_DIR] [OUT_CSV]
"""
import csv, sys, re, collections, hashlib, os

JAMBU   = sys.argv[1] if len(sys.argv) > 1 else "/tmp/jambu/data"
DRAVLEX = sys.argv[2] if len(sys.argv) > 2 else "/tmp/dravlex/cldf"
OUT     = sys.argv[3] if len(sys.argv) > 3 else "domain-e-evidence-mass.csv"

TAG = re.compile(r"<[^>]+>")


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def strip(s):
    return TAG.sub("", s or "")


# ---------------------------------------------------------------- 1, 2
dedr_rows, dedr_langs, dedr_entries = 0, collections.Counter(), set()
for r in csv.reader(open(f"{JAMBU}/dedr/dedr_new.csv")):
    if len(r) < 3:
        continue
    dedr_rows += 1
    dedr_langs[r[0]] += 1
    dedr_entries.add(r[1])

pdr_rows, pdr_entries, pdr_forms = 0, set(), set()
for r in csv.reader(open(f"{JAMBU}/dedr/pdr.csv")):
    if len(r) < 3:
        continue
    pdr_rows += 1
    pdr_entries.add(r[1])
    pdr_forms.add(r[2].strip())

# DravLex is a second, independent-of-DEDR sample of attested Dravidian.
dl_langs = dl_forms = dl_cogsets = 0
if os.path.isdir(DRAVLEX):
    dl_langs = sum(1 for _ in csv.DictReader(open(f"{DRAVLEX}/languages.csv"))) 
    dl_forms = sum(1 for _ in csv.DictReader(open(f"{DRAVLEX}/forms.csv")))
    dl_cogsets = len({r["Cognateset_ID"]
                      for r in csv.DictReader(open(f"{DRAVLEX}/cognates.csv"))})

# ---------------------------------------------------------------- 5, 6, 7
mu_rows, mu_langs, mu_etyma, pmu_forms = 0, collections.Counter(), set(), set()
for r in csv.reader(open(f"{JAMBU}/munda/forms.csv")):
    if len(r) < 3:
        continue
    mu_rows += 1
    mu_etyma.add(r[1])
    if r[0] == "PMu":
        pmu_forms.add(r[2].strip())
    else:
        mu_langs[r[0]] += 1

rau = list(csv.DictReader(open(f"{JAMBU}/munda/rau_2019.csv")))
rau_etyma = len(rau)
rau_with_mkcd = sum(1 for r in rau if (r.get("mkcd_no") or "").strip() not in ("", "—"))
rau_with_pinnow = sum(1 for r in rau if (r.get("pinnow") or "").strip() not in ("", "—"))

# ---------------------------------------------------------------- 3, 11
# Turner's own etymological brackets. "←" is his loan arrow; a bare mention
# ("Cf. Drav.", "Poss. Muṇḍa") is a comparison, not an attribution, and the
# two are counted apart because collapsing them is exactly the kind of
# upgrade-by-paraphrase this register exists to prevent.
cdial = [(r[0], r[1], strip(r[3])) for r in csv.reader(open(f"{JAMBU}/cdial/params.csv"))
         if len(r) >= 4]
DRAV = re.compile(r"\bDrav\.|\bDravidian\b")
MUND = re.compile(r"\bMuṇḍ\w*|\bMunda\b")
ARROW_DRAV = re.compile(r"←[^.\]]{0,40}?Drav\.")
ARROW_MUND = re.compile(r"←[^.\]]{0,40}?Muṇḍ")
UNKNOWN = re.compile(r"orig(?:in)?\.?\s+(?:unknown|obscure|doubtful)|of\s+unkn\.|"
                     r"Of\s+doubtful\s+origin|non-Aryan|Origin\s+unknown", re.I)

c_drav = [c for c in cdial if DRAV.search(c[2])]
c_drav_arrow = [c for c in c_drav if ARROW_DRAV.search(c[2])]
c_mund = [c for c in cdial if MUND.search(c[2])]
c_mund_arrow = [c for c in c_mund if ARROW_MUND.search(c[2])]
c_unknown = [c for c in cdial if UNKNOWN.search(c[2])]

# ---------------------------------------------------------------- emit
H = ["measure_id", "distinction_no", "distinction", "quantity", "value",
     "source_id", "locator", "what_this_cannot_show"]
rows = [
 ("EM-01", "1", "attested Dravidian languages",
  "distinct language labels carrying at least one reflex in the retrieved DEDR table",
  len(dedr_langs), "SRC-045", "JAMBU data/dedr/dedr_new.csv, field 1",
  "Labels are DEDR's own and mix languages with dialects and fieldnote lects; this is not a count of Dravidian languages in the world."),
 ("EM-02", "1", "attested Dravidian languages",
  "reflex rows in the retrieved DEDR table", dedr_rows, "SRC-045",
  "JAMBU data/dedr/dedr_new.csv, all rows",
  "One printed DEDR sub-entry can yield several rows; this is a row count, not a word count."),
 ("EM-03", "1", "attested Dravidian languages",
  "distinct DEDR entry numbers in the retrieved table", len(dedr_entries), "SRC-045",
  "JAMBU data/dedr/dedr_new.csv, field 2",
  "Cannot be checked against the printed 1984 edition: dsal.uchicago.edu is EGRESS_BLOCKED (SRC-040)."),
 ("EM-04", "1", "attested Dravidian languages",
  "varieties in DravLex, a second and differently built sample", dl_langs, "SRC-051",
  "lexibank/dravlex @ 3757807, cldf/languages.csv",
  "100 basic-vocabulary concepts only. Not a lexicon and not independent evidence for any individual etymology."),
 ("EM-05", "1", "attested Dravidian languages",
  "cognate sets coded in DravLex", dl_cogsets, "SRC-051",
  "lexibank/dravlex @ 3757807, cldf/cognates.csv",
  "Cognacy coding, not reconstruction. A cognate set is not a Proto-Dravidian form."),
 ("EM-06", "2", "reconstructed Proto-Dravidian",
  "distinct starred Proto-Dravidian forms in the retrieved reconstruction set",
  len(pdr_forms), "SRC-046", "JAMBU data/dedr/pdr.csv, field 3",
  "Krishnamurti's reconstructions as carried by JAMBU, at one remove from Krishnamurti 2003, which is not retrieved. A starred form is not an attestation."),
 ("EM-07", "2", "reconstructed Proto-Dravidian",
  "DEDR entries for which a Proto-Dravidian form is offered", len(pdr_entries), "SRC-046",
  "JAMBU data/dedr/pdr.csv, field 2",
  "Coverage is partial by design; DEDR itself offers no reconstructions, which is why this is a separate table and a separate distinction."),
 ("EM-08", "2", "reconstructed Proto-Dravidian",
  "share of retrieved DEDR entries carrying a Proto-Dravidian reconstruction (percent)",
  round(100.0 * len(pdr_entries) / len(dedr_entries), 1), "SRC-045; SRC-046",
  "ratio of EM-07 to EM-03",
  "A low share is a fact about this reconstruction set's coverage, not a measure of Proto-Dravidian's security."),
 ("EM-09", "3", "accepted Old Indo-Aryan Dravidian loans",
  "CDIAL entries where Turner writes the loan arrow to Dravidian", len(c_drav_arrow),
  "SRC-049", "JAMBU data/cdial/params.csv, entry text, regex '←...Drav.'",
  "Turner's attribution, made in the 1960s. Retrieving it is not confirming it, and 'accepted' here means accepted by Turner."),
 ("EM-10", "3", "accepted Old Indo-Aryan Dravidian loans",
  "CDIAL entries mentioning Dravidian at all, including comparisons and rejections",
  len(c_drav), "SRC-049", "JAMBU data/cdial/params.csv, entry text, regex 'Drav.'",
  "A mention is not an attribution. The gap between this and EM-09 is the space in which loan lists get inflated by paraphrase."),
 ("EM-11", "5", "attested Munda languages",
  "distinct Munda languages with reflexes in the retrieved comparative table",
  len(mu_langs), "SRC-047", "JAMBU data/munda/forms.csv, field 1 excluding PMu",
  "This table is a comparative wordlist assembled for reconstruction, not a lexicon of any Munda language."),
 ("EM-12", "5", "attested Munda languages",
  "attested Munda reflex rows in that table", mu_rows - len(pmu_forms), "SRC-047",
  "JAMBU data/munda/forms.csv",
  "Nothing in this table is located in the northwest. Its languages are eastern and central Indian."),
 ("EM-13", "6", "reconstructed Proto-Munda",
  "Proto-Munda etyma reconstructed in Rau 2019 as carried by JAMBU", rau_etyma,
  "SRC-048", "JAMBU data/munda/rau_2019.csv, one row per etymon",
  "Rau alone, at one remove. 127 etyma is a comparative core, not the reconstructible lexicon."),
 ("EM-14", "7", "pre-Proto-Munda / deeper Austroasiatic",
  "of those etyma, the number carrying a Mon-Khmer Comparative Dictionary number",
  rau_with_mkcd, "SRC-048", "JAMBU data/munda/rau_2019.csv, field mkcd_no",
  "Shorto's MKCD is cited inside Rau's table; it was not retrieved. This measures Rau's citation of Shorto, not Shorto."),
 ("EM-15", "7", "pre-Proto-Munda / deeper Austroasiatic",
  "of those etyma, the number carrying a Pinnow number", rau_with_pinnow, "SRC-048",
  "JAMBU data/munda/rau_2019.csv, field pinnow",
  "Same: this is Rau citing Pinnow."),
 ("EM-16", "5,6,7", "Munda, all three layers together",
  "CDIAL entries where Turner writes the loan arrow to Munda", len(c_mund_arrow),
  "SRC-049", "JAMBU data/cdial/params.csv, entry text, regex '←...Muṇḍ'",
  "Turner's attribution, and several of his Munda attributions are themselves credited to Kuiper, who is not retrieved (HOLD-002)."),
 ("EM-17", "5,6,7", "Munda, all three layers together",
  "CDIAL entries mentioning Munda at all", len(c_mund), "SRC-049",
  "JAMBU data/cdial/params.csv, entry text, regex 'Muṇḍ|Munda'",
  "As EM-10: mention is not attribution."),
 ("EM-18", "11", "genuinely unidentified vocabulary",
  "CDIAL entries where Turner declares the origin unknown, obscure, doubtful or non-Aryan",
  len(c_unknown), "SRC-049",
  "JAMBU data/cdial/params.csv, entry text, regex on 'orig. unknown|obscure|doubtful|non-Aryan'",
  "This is Turner's residue, in Indo-Aryan, not a Rigvedic residue and not anyone's substrate list. It is a floor on unidentified vocabulary, not an estimate of it."),
 ("EM-19", "4", "proposed Dravidian substrate forms",
  "items measurable from sources retrieved in this session", 0, "SRC-052",
  "05-HOLDS/HOLD-002-substrate-literature.md",
  "NOT MEASURED. Southworth, Kuiper and Witzel are unretrieved. Zero here means zero retrieved, and must never be read as zero proposed."),
 ("EM-20", "8", "Witzel's historical Para-Munda proposal",
  "items measurable from sources retrieved in this session", 0, "SRC-052",
  "05-HOLDS/HOLD-002-substrate-literature.md",
  "NOT MEASURED, for the same reason. The proposal is not refuted by its absence from this table."),
 ("EM-21", "9", "Kubha-Vipas / unknown-prefixing-language fallback",
  "items measurable from sources retrieved in this session", 0, "SRC-052",
  "05-HOLDS/HOLD-002-substrate-literature.md",
  "NOT MEASURED, same reason."),
 ("EM-22", "10", "Masica's Language X residue",
  "items measurable from sources retrieved in this session", 0, "SRC-052",
  "05-HOLDS/HOLD-002-substrate-literature.md",
  "NOT MEASURED, same reason. Masica 1979 is unretrieved."),
]

with open(OUT, "w", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(H)
    for r in rows:
        w.writerow(r)

print(f"{len(rows)} measures -> {OUT}")
for label, path in [("dedr_new.csv", f"{JAMBU}/dedr/dedr_new.csv"),
                    ("pdr.csv", f"{JAMBU}/dedr/pdr.csv"),
                    ("munda/forms.csv", f"{JAMBU}/munda/forms.csv"),
                    ("munda/rau_2019.csv", f"{JAMBU}/munda/rau_2019.csv"),
                    ("cdial/params.csv", f"{JAMBU}/cdial/params.csv")]:
    print(f"  {sha(path)}  {label}")
