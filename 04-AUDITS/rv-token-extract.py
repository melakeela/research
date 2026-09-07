#!/usr/bin/env python3
"""
Extract the Zurich token layer from the VedaWeb TEI and attach Arnold's
per-pada metrical stratum to every token.

Source: VedaWebProject/vedaweb-data @ d3eb8af7324338161520d2d35eae8f7e985a19a5
        rigveda/TEI/rv_book_01.tei ... rv_book_10.tei   (CC-BY-4.0)
Ledger: SRC-019, SRC-022, SRC-023

Output TSV columns:
  stanza      stanza id in DOTS_AND_ZEROS form, e.g. 01.001.01
  book        1-10
  hymn        hymn number within the book
  stanza_n    stanza number within the hymn
  pada        pada label a..h
  tok_i       1-based token index within the pada
  surface     Zurich surface form
  lemma       Zurich lemma (TEI f name="gra_lemma")
  lemma_id    Grassmann lemma id from the correction attribute, or ""
  gramm       Zurich grammatical category (TEI f name="gra_gramm")
  morph       morphosyntax, "key=VALUE" joined by "|"
  metre       Arnold metre label for this pada (TEI f name="label")
  stratum     Arnold stratum code for this pada (TEI f name="strata")

Every token in a pada carries that pada's stratum. Padas absent from
strata.json get metre and stratum "".
"""
import sys, os, re
import xml.etree.ElementTree as ET

TEI = "{http://www.tei-c.org/ns/1.0}"
XML = "{http://www.w3.org/XML/1998/namespace}"
SRC = sys.argv[1] if len(sys.argv) > 1 else \
    "/home/user/vedawebproject/vedaweb-data/rigveda/TEI"
OUT = sys.argv[2] if len(sys.argv) > 2 else "rv_tokens_vedaweb.tsv"

# b01_h001_01 -> ("01.001.01", 1, 1, 1)
STANZA_ID = re.compile(r"^b(\d+)_h(\d+)_(\d+)$")
# b01_h001_01_zur_a_tokens -> "a" ; b01_h001_01_strata_a -> "a"
PADA_SUF = re.compile(r"_(?:zur|strata)_([a-h])(?:_tokens)?$")


def text_of(el):
    return "".join(el.itertext()).strip()


def parse_stanza(div):
    sid = div.get(XML + "id", "")
    m = STANZA_ID.match(sid)
    if not m:
        return []
    book, hymn, stz = (int(x) for x in m.groups())
    dots = "%02d.%03d.%02d" % (book, hymn, stz)

    # pada -> (metre label, stratum code)
    strata = {}
    for lg in div.findall(TEI + "lg"):
        if lg.get("type") != "strata":
            continue
        for l in lg.findall(TEI + "l"):
            pm = PADA_SUF.search(l.get(XML + "id", ""))
            if not pm:
                continue
            label = stratum = ""
            for fs in l.iter(TEI + "fs"):
                for f in fs.findall(TEI + "f"):
                    if f.get("name") == "label":
                        label = text_of(f)
                    elif f.get("name") == "strata":
                        stratum = text_of(f)
            strata[pm.group(1)] = (label, stratum)

    rows = []
    for lg in div.findall(TEI + "lg"):
        if lg.get("source") != "zurich":
            continue
        for l in lg.findall(TEI + "l"):
            lid = l.get(XML + "id", "")
            if not lid.endswith("_tokens"):
                continue
            pm = PADA_SUF.search(lid)
            if not pm:
                continue
            pada = pm.group(1)
            metre, stratum = strata.get(pada, ("", ""))
            for i, fs in enumerate(l.findall(TEI + "fs"), 1):
                if fs.get("type") != "zurich_info":
                    continue
                surface = lemma = lemma_id = gramm = ""
                morph = []
                for f in fs.findall(TEI + "f"):
                    name = f.get("name")
                    if name == "surface":
                        surface = text_of(f)
                    elif name == "gra_lemma":
                        lemma = text_of(f)
                        s = f.find(TEI + "string")
                        if s is not None:
                            lemma_id = (s.get("correction") or "").lstrip("#")
                    elif name == "gra_gramm":
                        sym = f.find(TEI + "symbol")
                        gramm = (sym.get("value") if sym is not None
                                 else text_of(f)) or ""
                    elif name == "morphosyntax":
                        for sub in f.iter(TEI + "f"):
                            k = sub.get("name")
                            sym = sub.find(TEI + "symbol")
                            if k and sym is not None:
                                morph.append("%s=%s" % (k, sym.get("value")))
                rows.append([
                    dots, book, hymn, stz, pada, i,
                    surface, lemma, lemma_id, gramm, "|".join(morph),
                    metre, stratum,
                ])
    return rows


def main():
    header = ["stanza", "book", "hymn", "stanza_n", "pada", "tok_i",
              "surface", "lemma", "lemma_id", "gramm", "morph",
              "metre", "stratum"]
    n = 0
    with open(OUT, "w", encoding="utf-8") as out:
        out.write("\t".join(header) + "\n")
        for b in range(1, 11):
            path = os.path.join(SRC, "rv_book_%02d.tei" % b)
            for _, el in ET.iterparse(path, events=("end",)):
                if el.tag != TEI + "div" or el.get("type") != "stanza":
                    continue
                for r in parse_stanza(el):
                    out.write("\t".join(str(x) for x in r) + "\n")
                    n += 1
                el.clear()
            print("book %02d done, %d tokens so far" % (b, n), file=sys.stderr)
    print("%d tokens -> %s" % (n, OUT), file=sys.stderr)


if __name__ == "__main__":
    main()
