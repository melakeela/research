#!/usr/bin/env python3
"""
Two searches of the Rigveda for the vocabulary of writing, marking, incising
and sealing, run so that a negative result is a measurement rather than an
impression.

Source: VedaWebProject/vedaweb-data @ d3eb8af (CC-BY-4.0)
        Zurich token layer via 04-AUDITS/rv-token-extract.py    (SRC-106, SRC-107)
        rigveda/info/matched_lemmata.json, Grassmann glosses per surface form
Ledger: SRC-106, SRC-107; dependency DEP-032, DEP-021

WHY TWO SEARCHES

A hand-written candidate list can only find words someone thought to look
for, and §4.K asks a question a candidate list cannot answer: whether
relevant terminology is present but unrecognised. So:

  SEARCH A - candidate census. A declared list of stems, looked up by
  normalised lemma, reported present or absent, per lemma and never merged
  across lemmas. It carries positive controls, so that a row of zeros is
  distinguishable from a broken lookup. One control, gó- 'cow', is kept in
  its failing form in the output: the Zurich lemma is the alternation
  "gáv- ~ gó-", and a lookup that does not split alternants misses 543
  tokens. That is what a control is for.

  SEARCH B - gloss scan. Every lemma attested in the corpus, matched against
  the semantic field of writing, marking, incising and sealing in the German
  and Latin of the Grassmann glosses, then ADJUDICATED hit by hit. The
  method is 04-AUDITS/rv-pur-numeral-scan.py's, applied to a different field.
  Its three known failure modes are handled: substring rather than
  word-bounded matching, Latin as well as German, and an explicit report of
  gloss coverage rather than an assertion of exhaustiveness.

  Substring matching is what makes adjudication compulsory rather than
  optional. German "ausgezeichnet" (excellent) contains zeichn, "spritzen"
  (to spray) contains ritz, "Vorschrift" (prescription) contains schrift,
  "bestrichen" (smeared) contains strich, "ackerbauend" (farming) contains
  kerb, and Grassmann's own metalanguage - "Bezeichnung eines Volkes",
  "the designation of a people" - contains bezeichn on 90 lemmas that have
  nothing to do with marking. Every hit below is classified, with a reason,
  and the false positives are printed rather than deleted.

GLOSSES ARE ATTACHED PER SURFACE FORM, NOT PER LEMMA

matched_lemmata.json is keyed by surface form and distinguishes homonyms the
Zurich lemma layer merges: akṣī́ resolves to ákṣ- "Auge", while níraṣṭāḥ
resolves to √akṣ- 1 "kennzeichnen, Ohrenmarken einstechen" and ákṣat to
√akṣ- 2 "erreichen (?)". A lemma-keyed lookup silently merges the eye, the
ear-mark and the reaching. This script keys on the surface form and prints
lemma-plus-gloss pairs.

Neither search assigns a sense to a passage. The Zurich layer carries lemma
and morphology, not sense; Grassmann's gloss is a nineteenth-century
lexicographer's judgement, reported as his.

Usage: rv-writing-lexicon-scan.py TOKENS_TSV VEDAWEB_RIGVEDA_DIR [OUT_PREFIX]
"""
import sys, csv, json, re, collections, unicodedata

TOK = sys.argv[1] if len(sys.argv) > 1 else "rv_tokens.tsv"
RV = sys.argv[2] if len(sys.argv) > 2 else "vedaweb/rigveda"
OUT = sys.argv[3] if len(sys.argv) > 3 else "rv-writing"

ACCENTS = {"́", "̀", "̂"}


def stem(s):
    """Bare stem of a Zurich lemma, with roots kept distinct from nominals.

    The layer writes roots with a leading √, uses r̥ for ṛ, marks set-roots
    with superscript vowels (janⁱ-), numbers homonyms (√vid- 1) and writes
    alternations with a tilde (gáv- ~ gó-). Returns the set of keys a lemma
    can be looked up under; roots keep a ROOT: prefix so that ákṣ- "eye" and
    √akṣ- "mark" cannot collide.
    """
    root = "√" in s
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if c not in ACCENTS)
    s = unicodedata.normalize("NFC", s)
    s = s.replace("√", "").replace("r̥̄", "ṝ").replace("r̥", "ṛ").replace("l̥", "ḷ")
    s = re.sub(r"[ⁱᵘ]", "", s)
    keys = set()
    for part in s.split("~"):
        part = re.sub(r"\s*\d+\s*$", "", part).strip().strip("-").strip()
        if part:
            keys.add(("ROOT:" if root else "") + part)
    return keys


def key(q, root=False):
    k = list(stem(q))[0]
    return ("ROOT:" if root else "") + k.replace("ROOT:", "")


# ---------------------------------------------------------------- tokens
rows = [l.rstrip("\n").split("\t") for l in open(TOK, encoding="utf-8")]
head, rows = rows[0], rows[1:]
c = {k: i for i, k in enumerate(head)}
tokens = collections.Counter(r[c["lemma"]] for r in rows)
stanzas = collections.defaultdict(set)
for r in rows:
    stanzas[r[c["lemma"]]].add(r[c["stanza"]])
by_key = collections.defaultdict(set)
for lem in tokens:
    for k in stem(lem):
        by_key[k].add(lem)

# ------------------------------------------------- glosses, per surface
md = json.load(open(f"{RV}/info/matched_lemmata.json", encoding="utf-8"))
pair = collections.Counter()          # (zurich lemma, grassmann lemma, gloss) -> tokens
lemma_gloss = collections.defaultdict(set)
glossed_tokens = 0
for r in rows:
    d = md.get(r[c["surface"]])
    if d and d.get("meaning"):
        glossed_tokens += 1
        pair[(r[c["lemma"]], (d.get("lemma") or "").strip(), d["meaning"])] += 1
        lemma_gloss[r[c["lemma"]]].add(d["meaning"])

# ------------------------------------------------- SEARCH A: candidates
CANDIDATES = [
    ("likh", False, "WRITING", "√likh- 'scratch, write', the ordinary Classical verb for writing"),
    ("likh", True, "WRITING", "the same as a root"),
    ("rikh", True, "WRITING", "√rikh-, the Rigvedic form of the same root family"),
    ("lekha", False, "WRITING", "lekha- 'writing, letter, document'"),
    ("lipi", False, "WRITING", "lipi- 'script, writing', the Aśokan-period word"),
    ("libi", False, "WRITING", "libi-, the Old Persian-influenced variant"),
    ("akṣara", False, "WRITING", "akṣara- 'syllable', later 'written character'"),
    ("varṇa", False, "WRITING", "varṇa- 'colour, class', later also 'letter'"),
    ("grantha", False, "WRITING", "grantha- 'knot', later 'composition, book'"),
    ("pattra", False, "WRITING", "pattra- 'leaf', later 'writing leaf'"),
    ("patra", False, "WRITING", "patra-, the same word written short"),
    ("pustaka", False, "WRITING", "pustaka- 'book'"),
    ("phalaka", False, "WRITING", "phalaka- 'board, tablet'"),
    ("masi", False, "WRITING", "masi- 'ink'"),
    ("kalama", False, "WRITING", "kalama- 'reed pen'"),
    ("lekhaka", False, "WRITING", "lekhaka- 'scribe'"),
    ("mudra", False, "SEALING", "mudrā- 'seal, stamp, impression'"),
    ("mudrā", False, "SEALING", "the same, long final"),
    ("aṅka", False, "SEALING", "aṅká- 'mark, brand, hook'"),
    ("aṅkana", False, "SEALING", "aṅkana- 'marking, branding'"),
    ("cihna", False, "SEALING", "cihna- 'mark, sign'"),
    ("lāñchana", False, "SEALING", "lāñchana- 'mark, token'"),
    ("lakṣa", False, "SEALING", "lakṣá- 'mark, target, stake'"),
    ("lakṣman", False, "SEALING", "lakṣman- 'mark, sign'"),
    ("salakṣman", False, "SEALING", "sálakṣman- 'having the same mark'"),
    ("lakṣaṇa", False, "SEALING", "lakṣaṇa- 'mark, characteristic'"),
    ("akṣ", True, "SEALING", "√akṣ- 1, glossed 'kennzeichnen, Ohrenmarken einstechen'"),
    ("aṣṭakarṇa", False, "SEALING", "aṣṭakarṇá- 'with marked ears', of cattle and horses"),
    ("takṣ", True, "INCISING", "√takṣ- 'fashion, hew, carve'"),
    ("tvakṣ", True, "INCISING", "√tvakṣ- 'fashion'"),
    ("piś", True, "INCISING", "√piś- 'shape, adorn, carve'"),
    ("peśas", False, "INCISING", "péśas- 'form, adornment'"),
    ("vraśc", True, "INCISING", "√vraśc- 'cut down, hew'"),
    ("khan", True, "INCISING", "√khan- 'dig'"),
    ("lip", True, "INCISING", "√lip- 'smear', the root behind lipi-"),
    ("citra", False, "INCISING", "citrá- 'bright, conspicuous, variegated'"),
    ("rūpa", False, "INCISING", "rūpá- 'form, shape'"),
    ("ketu", False, "SIGN", "ketú- 'appearance, sign, banner'"),
    ("nāman", False, "SIGN", "nā́man- 'name, mark'"),
    ("yakṣa", False, "SIGN", "yakṣá- 'apparition, portent'"),
    ("lakṣmī", False, "SIGN", "lakṣmī́- 'auspicious sign'"),
    ("gaṇ", True, "RECKONING", "the root gaṇ- 'count', if present"),
    ("saṃkhyā", False, "RECKONING", "saṃkhyā- 'number, reckoning'"),
    ("tulā", False, "RECKONING", "tulā- 'balance, scales'"),
    ("mā", True, "RECKONING", "√mā- 'measure'"),
    ("māna", False, "RECKONING", "māna- 'measure'"),
    ("śulka", False, "RECKONING", "śulká- 'toll, price'"),
    ("bali", False, "RECKONING", "balí- 'tribute, offering'"),
    ("bhāga", False, "RECKONING", "bhāgá- 'share, portion'"),
    ("ṛṇa", False, "RECKONING", "ṛṇá- 'debt, obligation'"),
    ("krī", True, "RECKONING", "√krī- 'buy'"),
    ("paṇ", True, "RECKONING", "√paṇ- 'bargain'"),
    ("pur", False, "CONTROL", "púr-, measured by an earlier unit of this repository"),
    ("ratha", False, "CONTROL", "rátha- 'chariot'"),
    ("go", False, "CONTROL", "gó- 'cow' - deliberately queried in the form that fails"),
    ("gav", False, "CONTROL", "gáv-, the alternant that succeeds"),
    ("vac", True, "CONTROL", "√vac- 'speak'"),
    ("stoma", False, "CONTROL", "stóma- 'praise-song'"),
]

# ------------------------------------------------------ SEARCH B: field
FIELD = {
    "WRITING": ["schreib", "schrift", "geschrieben", "buchstab", "brief",
                "urkunde", "griffel", "tafel", "täfel", "scrib", "littera",
                "scriptum"],
    "MARK": ["zeichen", "bezeichn", "zeichn", "merkmal", "marke", "markier",
             "kennzeichen", "kerbe", "kerb", "strich", "linie", "signum",
             "nota", "signare"],
    "SEAL": ["siegel", "stempel", "abdruck", "prägen", "gepräg", "sigill"],
    "INCISE": ["ritz", "eingrab", "gravier", "einschneid", "schnitz",
               "meissel", "meißel", "sculp", "incid"],
}

# Adjudication. A hit is TRUE only if the GLOSS puts the word in the field;
# whether the word is used of a durable inscribed medium is a separate
# question, answered per passage in
# 03-REGISTERS/domain-k-rigveda-marking-occurrences.csv and not here.
ADJ_TRUE = {
    "√rikh-": "Grassmann glosses it 'ritzen', to scratch or incise. The only root in the corpus so glossed.",
    "√akṣ-": "Grassmann's √akṣ- 1 is 'kennzeichnen, Ohrenmarken einstechen', to mark, to cut ear-marks. Only the surface níraṣṭāḥ resolves to it; ákṣat and ā́kṣiṣuḥ resolve to √akṣ- 2 'erreichen (?)', a different root the Zurich lemma string merges with it.",
    "aṣṭakarṇá-": "'mit gekennzeichneten Ohren (von Rind und Ross)', of marked ears on cattle and horses: property marking on animals.",
    "sálakṣman-": "'gleiches Merkmal habend', having the same mark.",
    "lakṣmī́-": "'gutes, glückliches Zeichen', an auspicious sign.",
    "nā́man-": "'Name, Benennung, Kennzeichen', where Kennzeichen is a distinguishing mark.",
    "ketú-": "'Erscheinung, Kennzeichen, Lichterscheinung, Helle, Gestalt': a visible sign, in the corpus typically a light or a banner.",
    "yakṣá-": "'Erscheinung, Wundererscheinung, Blendwerk, Vorzeichen': a portent.",
    "yakṣabhŕ̥t-": "'ein Zeichen (?) tragend', bearing a sign - Grassmann's own question mark retained.",
    "tryàruṣa-": "'an drei Stellen rötlich gezeichnet', marked with red in three places.",
    "śréṇi-": "'Reihe, Linie Zug, Schar, Gruppe': a line in the sense of a rank of people or things, not a drawn line.",
}
ADJ_FALSE_RULES = [
    ("bezeichn", "METALANGUAGE. Grassmann's German 'Bezeichnung eines Volkes', 'the designation of a people', describes what the dictionary entry does, not what the Vedic word means."),
    ("ausgezeichnet", "GERMAN MORPHOLOGY. 'ausgezeichnet' means excellent and contains the substring zeichn."),
    ("auszeichn", "GERMAN MORPHOLOGY. 'sich auszeichnen' means to excel."),
    ("spritz", "GERMAN MORPHOLOGY. 'spritzen', to spray, contains the substring ritz."),
    ("sprengen", "GERMAN MORPHOLOGY. 'besprengen', to sprinkle, reached through a spritzen gloss."),
    ("vorschrift", "GERMAN MORPHOLOGY. 'Vorschrift' means prescription and contains schrift."),
    ("zugeschrieben", "GERMAN MORPHOLOGY. 'zugeschrieben' means ascribed, said of hymns attributed to a poet."),
    ("bestrichen", "GERMAN MORPHOLOGY. 'bestrichen', smeared, contains strich."),
    ("ackerbau", "GERMAN MORPHOLOGY. 'ackerbauend', farming, contains kerb."),
    ("eine kennzeichnung", "METALANGUAGE. 'eine Kennzeichnung der Marut' is Grassmann saying the word characterises the Maruts, not that it means a mark."),
    ("gekennzeichnet ist", "METALANGUAGE. The gloss is a starred paraphrase of the compound's structure, '*Gut habend das durch Gedanken gekennzeichnet ist', not a sense of the word."),
]


def adjudicate(lemma, gloss):
    if lemma in ADJ_TRUE:
        return "TRUE", ADJ_TRUE[lemma]
    low = gloss.lower()
    for needle, reason in ADJ_FALSE_RULES:
        if reason and needle in low:
            return "FALSE-POSITIVE", reason
    return "UNADJUDICATED", "no rule matched; must be adjudicated by hand before use"


def main():
    print("corpus: %d tokens, %d distinct lemmas" % (len(rows), len(tokens)))
    print("tokens carrying a Grassmann gloss: %d (%.1f%%)"
          % (glossed_tokens, 100.0 * glossed_tokens / len(rows)))
    print("lemmas carrying at least one gloss: %d (%.1f%%)"
          % (len(lemma_gloss), 100.0 * len(lemma_gloss) / len(tokens)))
    print()

    with open(OUT + "-candidates.tsv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["query", "root", "class", "why", "lemma", "tokens",
                    "stanzas", "glosses"])
        print("SEARCH A - candidate census, one line per matched lemma")
        for q, root, cls, why in CANDIDATES:
            hits = sorted(by_key.get(key(q, root), []))
            if not hits:
                w.writerow([q, root, cls, why, "ABSENT", 0, 0, ""])
                print("  %-10s %-9s ABSENT" % (q, cls))
                continue
            for lem in hits:
                gl = " | ".join(sorted(lemma_gloss.get(lem, [])))
                w.writerow([q, root, cls, why, lem, tokens[lem],
                            len(stanzas[lem]), gl])
                print("  %-10s %-9s %-18s %5d tokens %4d stanzas  %s"
                      % (q, cls, lem, tokens[lem], len(stanzas[lem]), gl[:70]))
        print()

    print("SEARCH B - gloss scan of the whole attested lexicon, adjudicated")
    seen, out = set(), []
    for (lem, gra, gloss), n in pair.items():
        low = gloss.lower()
        for field, keys in FIELD.items():
            hit = next((k for k in keys if k in low), None)
            if not hit:
                continue
            if (field, lem, gloss) in seen:
                continue
            seen.add((field, lem, gloss))
            verdict, reason = adjudicate(lem, gloss)
            out.append((field, lem, gra, n, hit, verdict, reason, gloss))
            break
    out.sort(key=lambda x: (x[0], x[5] != "TRUE", -x[3]))
    with open(OUT + "-glossscan.tsv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["field", "zurich_lemma", "grassmann_lemma", "tokens",
                    "keyword", "verdict", "reason", "gloss"])
        for r in out:
            w.writerow(r)
    tally = collections.Counter((r[0], r[5]) for r in out)
    for field in FIELD:
        t = tally[(field, "TRUE")]
        f = tally[(field, "FALSE-POSITIVE")]
        u = tally[(field, "UNADJUDICATED")]
        print("  %-8s %2d true, %3d false positive, %2d unadjudicated" % (field, t, f, u))
    print()
    print("  TRUE hits:")
    for r in out:
        if r[5] == "TRUE":
            print("    %-8s %-16s %4d  %s" % (r[0], r[1], r[3], r[7][:70]))
    print()
    print("  UNADJUDICATED (must be resolved before any claim rests on this scan):")
    for r in out:
        if r[5] == "UNADJUDICATED":
            print("    %-8s %-16s %4d  [%s]  %s" % (r[0], r[1], r[3], r[4], r[7][:70]))


if __name__ == "__main__":
    main()
