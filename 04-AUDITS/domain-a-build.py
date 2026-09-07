#!/usr/bin/env python3
"""
Domain A - Rigvedic chronology and transmission.
Build the per-pada, per-stanza and per-hymn tables the measurements run on.

Source: VedaWebProject/vedaweb-data @ d3eb8af7324338161520d2d35eae8f7e985a19a5
        (ledger SRC-019 / SRC-059 / SRC-069; CC-BY-4.0 and CC-BY-NC-SA-4.0
        per file, see rigveda/TEI/vedaweb_corpus.tei)

Nothing here interprets anything. It only aligns the layers so that the
measurement scripts can count over them.

Outputs, written to the directory given as argv[2] (default ./dom-a-work):
  padas.tsv    one row per pada present in ANY of the pada-level layers
  stanzas.tsv  one row per stanza
  hymns.tsv    one row per hymn
"""
import sys, os, json, csv, re, unicodedata, collections

RV  = sys.argv[1] if len(sys.argv) > 1 else "/home/user/vedawebproject/vedaweb-data/rigveda"
OUT = sys.argv[2] if len(sys.argv) > 2 else "dom-a-work"
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- readers
def read_pada_csv(path):
    """stanza \t pada \t text  ->  {(stanza, pada): text}"""
    d = {}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            p = line.rstrip("\n").split("\t")
            if len(p) < 3:
                continue
            d[(p[0], p[1])] = p[2]
    return d

def read_stanza_csv(path):
    d = {}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            p = line.rstrip("\n").split("\t")
            if len(p) < 2:
                continue
            d[p[0]] = p[1]
    return d

aufrecht = read_pada_csv(os.path.join(RV, "versions/aufrecht.csv"))
vnh      = read_pada_csv(os.path.join(RV, "versions/vnh.csv"))
lubotsky = read_pada_csv(os.path.join(RV, "versions/lubotsky.csv"))
padapatha = read_stanza_csv(os.path.join(RV, "versions/padapatha.csv"))

strata = json.load(open(os.path.join(RV, "info/strata.json"), encoding="utf-8"))
props  = json.load(open(os.path.join(RV, "info/stanza_properties.json"),
                       encoding="utf-8"))
PROP_HEADER = props.pop("Book.Hymn.Verse")
addressees = json.load(open(os.path.join(RV, "info/addressees.json"),
                            encoding="utf-8"))

# Oldenberg Noten page concordance (external-resources/Oldenberg)
old_noten = collections.defaultdict(list)
for band in ("Oldenberg_Band_1.csv", "Oldenberg_Band_2.csv"):
    p = os.path.join(RV, "external-resources/Oldenberg", band)
    with open(p, encoding="utf-8") as fh:
        for row in csv.reader(fh, delimiter=";", quotechar='"'):
            if len(row) >= 2 and row[0]:
                old_noten[row[0]].append(band[-5] + row[1])

# ------------------------------------------------------- syllable counting
# The VedaWeb romanisation writes vocalic r and l as r/l + U+0325 and marks
# udatta with U+0301, svarita-ish with U+0300, nasalisation with U+0310.
# Diacritics are stripped before nuclei are counted; the diphthongs e o ai au
# are one nucleus each, and "ai"/"au" are only ever the diphthong inside a
# word in this transliteration.
COMBINING = "".join(chr(c) for c in (0x0301, 0x0300, 0x0310))
VOWEL_RE = re.compile(r"a[iu]|[aāiīuūeo]|r̥̄?|l̥")

def strip_marks(s, keep_hiatus=False):
    """Remove editorial marks; NFD, drop accents, recompose the ring below."""
    s = unicodedata.normalize("NFD", s)
    s = "".join(ch for ch in s if ch not in COMBINING)
    # editorial marks used in vnh.csv and lubotsky.csv
    drop = "+@&*\\!?}=/#[]()<>0123456789NAVf"
    if not keep_hiatus:
        drop += "~"
    s = "".join(ch for ch in s if ch not in drop)
    s = s.replace("'", "").replace("|", " ").replace("_", " ")
    return s

def syllables(s):
    return len(VOWEL_RE.findall(strip_marks(s)))

def skeleton(s):
    """Comparable segment string: marks, accents, spaces and hyphens gone."""
    return re.sub(r"[\s\-]", "", strip_marks(s))

# -------------------------------------------------------------- pada table
pada_keys = set(vnh) | set(lubotsky) | set(aufrecht)
for stz, entries in strata.items():
    for e in entries:
        pada_keys.add((stz, e[0]))

strata_lookup = {}
for stz, entries in strata.items():
    for e in entries:
        # [pada, metre label, stratum code]
        strata_lookup[(stz, e[0])] = (e[1], e[2])

with open(os.path.join(OUT, "padas.tsv"), "w", encoding="utf-8") as fh:
    fh.write("\t".join([
        "stanza", "book", "hymn", "stanza_n", "pada",
        "metre_label", "stratum",
        "has_aufrecht", "has_vnh", "has_lubotsky",
        "syl_vnh", "syl_vnh_hiatus", "syl_lubotsky",
        "vnh_marks", "vnh_text", "lubotsky_text"]) + "\n")
    for stz, pada in sorted(pada_keys):
        b, h, s = (int(x) for x in stz.split("."))
        label, strat = strata_lookup.get((stz, pada), ("", ""))
        v = vnh.get((stz, pada), "")
        l = lubotsky.get((stz, pada), "")
        marks = "".join(sorted(set(c for c in v if c in "+@&*~\\'/")))
        fh.write("\t".join(str(x) for x in [
            stz, b, h, s, pada, label, strat,
            int((stz, pada) in aufrecht), int(bool(v)), int(bool(l)),
            syllables(v) if v else "",
            len(VOWEL_RE.findall(strip_marks(v, keep_hiatus=True)
                                 .replace("~", " "))) if v else "",
            syllables(l) if l else "",
            marks, v, l]) + "\n")

# ------------------------------------------------------------ stanza table
all_stanzas = sorted(set(strata) | set(padapatha) |
                     {k[0] for k in pada_keys})
SCHOLARS = ["grassmann", "oldenberg", "arnold", "wuest", "witzel"]

# stanza -> concatenated aufrecht line text (Aufrecht's own lineation)
auf_by_stanza = collections.defaultdict(list)
for (stz, pada), t in aufrecht.items():
    auf_by_stanza[stz].append((pada, t))
vnh_by_stanza = collections.defaultdict(list)
for (stz, pada), t in vnh.items():
    vnh_by_stanza[stz].append((pada, t))

with open(os.path.join(OUT, "stanzas.tsv"), "w", encoding="utf-8") as fh:
    fh.write("\t".join([
        "stanza", "book", "hymn", "stanza_n",
        "n_padas_strata", "n_padas_vnh", "n_padas_aufrecht_lines",
        "strata_codes", "stratum_stanza", "stratum_case",
        "syl_vnh_stanza", "syl_aufrecht_stanza",
        "auf_vnh_same_skeleton",
        "padapatha", "n_padapatha_words", "n_padapatha_compounds",
        "oldenberg_noten_refs"] + SCHOLARS) + "\n")
    for stz in all_stanzas:
        b, h, s = (int(x) for x in stz.split("."))
        ent = strata.get(stz, [])
        codes = "".join(e[2] for e in ent)
        upper = [c for c in codes if c.isupper()]
        lower = [c for c in codes if c.islower()]
        case = ("upper" if upper and not lower else
                "lower" if lower and not upper else
                "mixed" if codes else "")
        stanza_stratum = codes.upper()[0] if codes else ""
        if codes and len(set(codes.upper())) > 1:
            stanza_stratum = "MIXED"
        av = "".join(t for _, t in sorted(vnh_by_stanza.get(stz, [])))
        aa = "".join(t for _, t in sorted(auf_by_stanza.get(stz, [])))
        pp = padapatha.get(stz, "")
        words = [w.strip() for w in pp.split("|") if w.strip()] if pp else []
        fh.write("\t".join(str(x) for x in [
            stz, b, h, s,
            len(ent), len(vnh_by_stanza.get(stz, [])),
            len(auf_by_stanza.get(stz, [])),
            codes, stanza_stratum, case,
            syllables(av) if av else "",
            syllables(aa) if aa else "",
            int(skeleton(av) == skeleton(aa)) if (av and aa) else "",
            pp, len(words), sum(1 for w in words if "-" in w),
            ";".join(old_noten.get(stz, []))]
            + [props.get(stz, {}).get(k, "") for k in SCHOLARS]) + "\n")

# -------------------------------------------------------------- hymn table
hymn_stanzas = collections.defaultdict(list)
for stz in all_stanzas:
    hymn_stanzas[stz.rsplit(".", 1)[0]].append(stz)

with open(os.path.join(OUT, "hymns.tsv"), "w", encoding="utf-8") as fh:
    fh.write("\t".join([
        "hymn_id", "book", "hymn", "n_stanzas",
        "addressee_de", "addressee_en", "group_de", "group_en",
        "syl_vnh_hymn"]) + "\n")
    for hid in sorted(hymn_stanzas):
        b, h = (int(x) for x in hid.split("."))
        adr = addressees.get(hid, [["", ""], ["", ""]])
        syl = 0
        for stz in hymn_stanzas[hid]:
            syl += sum(syllables(t) for _, t in vnh_by_stanza.get(stz, []))
        fh.write("\t".join(str(x) for x in [
            hid, b, h, len(hymn_stanzas[hid]),
            adr[0][0], adr[0][1], adr[1][0], adr[1][1], syl]) + "\n")

print("padas   ", len(pada_keys))
print("stanzas ", len(all_stanzas))
print("hymns   ", len(hymn_stanzas))
print("written to", os.path.abspath(OUT))
