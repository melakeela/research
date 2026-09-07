#!/usr/bin/env python3
"""
Classify every Rigvedic lemma by whether the retroflex consonants it
contains are derivable by the two regular Old Indo-Aryan retroflexion
rules, or are not.

Input:  rv_tokens_vedaweb.tsv, the output of 04-AUDITS/rv-token-extract.py
        (VedaWebProject/vedaweb-data @ d3eb8af, Zurich token layer;
        ledger SRC-019, SRC-022, SRC-023, SRC-047)
Output: three TSVs -- per-lemma classification, per-segment decisions,
        and the aggregate tables.

WHAT THIS SCRIPT DOES AND DOES NOT MEASURE
------------------------------------------
It measures one thing: whether a retroflex segment stands in an
environment in which a stated Old Indo-Aryan rule produces retroflexion
from a non-retroflex source.

"UNCONDITIONED" here means *not derived by the two rules implemented
below*. It does not mean non-Indo-European, non-inherited, borrowed, or
substrate. Several further internal sources of retroflexion exist and are
deliberately NOT implemented, because implementing them requires an
etymology per word rather than a rule over a string:

  - *-zdh- > -DH-        (miDha- < *mizdha-)
  - *-lt-, *-ln- clusters
  - cluster assimilation and dissimilation at morpheme seams
  - PIE *l / *r merger effects
  - retroflexion in reduplicated and secondary formations
  - sandhi retroflexion frozen into a citation form

So the UNCONDITIONED set is an upper bound on the residue, never a word
list of loans. It is the pool a substrate hypothesis would have to
explain, before any of the ordinary internal explanations above have been
tried on it.

THE TWO RULES
-------------
RUKI      s > S after i I u U r r-vocalic e o ai au k, immediately.
          Word-initial S is not RUKI-derived.
NATI      n > N when a trigger r / r-vocalic / S precedes anywhere in the
          same word with no blocking segment intervening, and N is
          followed by a vowel, y, v, n, m, or is word-final.
          Blockers: the palatals, the dentals, the retroflex stops,
          l, s, S.  (Velars, labials, vowels, y, v, r, h do not block.)
CLUSTER   A retroflex stop immediately after S or after another
          retroflex is taken as cluster-conditioned (STa, STha).

Every decision is written out per segment so that any of them can be
re-checked individually.
"""
import csv, re, sys, unicodedata, collections, json

IN  = sys.argv[1] if len(sys.argv) > 1 else "rv_tokens_vedaweb.tsv"
PRE = sys.argv[2] if len(sys.argv) > 2 else "rv_retroflex"
LEX = sys.argv[3] if len(sys.argv) > 3 else ""   # matched_lemmata.json

# ---------------------------------------------------------------- cleaning
ACCENTS = {"́", "̀", "̐"}          # acute, grave, candrabindu
RING    = "̥"                                 # vocalic r/l
MACRON  = "̄"
STRIP   = set("-√1234567890()?:,+ ")

DEACCENT = {"á":"a","à":"a","í":"i","ì":"i","ú":"u","ù":"u",
            "ó":"o","ò":"o","é":"e","è":"e","ŕ":"r","ⁱ":"i"}

def clean(lemma):
    """Citation form -> bare phoneme string. Accents and the root mark go;
    length marks and the vocalic ring stay, because both are phonemic."""
    s = unicodedata.normalize("NFC", lemma)
    s = s.split("~")[0]                 # first variant of 'A- ~ B-'
    out = []
    for ch in s:
        if ch in ACCENTS:               # combining acute/grave on r, r-long
            continue
        if ch in STRIP:
            continue
        out.append(DEACCENT.get(ch, ch))
    return "".join(out)

# ------------------------------------------------------------- segmenting
STOPS   = set("kgcjtdpb") | {"ṭ", "ḍ"}
VOWELS  = {"a","ā","i","ī","u","ū","e","o","ai","au","r̥","r̥̄","l̥"}
RETRO   = {"ṭ","ṭh","ḍ","ḍh","ṇ","ṣ","ḷ","ḷh"}
# nati blockers: palatals, dentals, retroflex stops, l, s, ś
BLOCK   = {"c","ch","j","jh","ñ","ṭ","ṭh","ḍ","ḍh","ḷ","ḷh",
           "t","th","d","dh","n","l","s","ś"}
TRIGGER = {"r","r̥","r̥̄","ṣ"}
RUKI_PREV = {"i","ī","u","ū","e","o","ai","au","r","r̥","r̥̄","k"}
FOLLOW_N  = VOWELS | {"y","v","n","m"}

def segment(s):
    """IAST string -> list of phonemes. Handles aspirates, r-vocalic and
    the diphthongs written ai/au."""
    seg, i, n = [], 0, len(s)
    while i < n:
        c = s[i]
        # vocalic r / l  (r + combining ring, optionally + macron)
        if i + 1 < n and s[i+1] == RING and c in "rl":
            j = i + 2
            if j < n and s[j] == MACRON:
                seg.append(c + RING + MACRON); i = j + 1
            else:
                seg.append(c + RING); i = j
            continue
        # diphthongs: only when 'a' is followed by i/u AND that i/u is not
        # itself the nucleus of the next syllable. Grassmann citation forms
        # write the diphthongs as e/o/ai/au, so 'ai'/'au' here are real.
        if c == "a" and i + 1 < n and s[i+1] in "iu":
            seg.append(s[i:i+2]); i += 2; continue
        # aspirates
        if i + 1 < n and s[i+1] == "h" and (c in STOPS or c == "ḷ"):
            seg.append(s[i:i+2]); i += 2; continue
        seg.append(c); i += 1
    return seg

# ----------------------------------------------------------- the two rules
def classify(segs):
    """-> list of (index, phoneme, verdict, rule) for retroflex segments."""
    out = []
    for i, ph in enumerate(segs):
        if ph not in RETRO:
            continue
        prev = segs[i-1] if i else None
        nxt  = segs[i+1] if i + 1 < len(segs) else None

        if ph == "ṣ":
            if prev is None:
                out.append((i, ph, "UNCONDITIONED", "word-initial"))
            elif prev in RUKI_PREV:
                out.append((i, ph, "CONDITIONED", "RUKI after %s" % prev))
            else:
                out.append((i, ph, "UNCONDITIONED", "no RUKI trigger (after %s)" % prev))

        elif ph == "ṇ":
            if prev is None:
                out.append((i, ph, "UNCONDITIONED", "word-initial"))
                continue
            if nxt is not None and nxt not in FOLLOW_N:
                out.append((i, ph, "UNCONDITIONED",
                            "nati environment fails: followed by %s" % nxt))
                continue
            trig = None
            for j in range(i - 1, -1, -1):
                if segs[j] in BLOCK:
                    break
                if segs[j] in TRIGGER:
                    trig = segs[j]; break
            if trig:
                out.append((i, ph, "CONDITIONED", "nati after %s" % trig))
            else:
                out.append((i, ph, "UNCONDITIONED", "no nati trigger"))

        else:   # retroflex stop or lateral
            if prev == "ṣ":
                out.append((i, ph, "CONDITIONED", "cluster after ṣ"))
            elif prev in RETRO:
                out.append((i, ph, "CONDITIONED", "cluster after %s" % prev))
            elif prev is None:
                out.append((i, ph, "UNCONDITIONED", "word-initial"))
            else:
                out.append((i, ph, "UNCONDITIONED", "no cluster source")) 
    return out

# ------------------------------------------------------------------- main
def main():
    rows = list(csv.DictReader(open(IN, encoding="utf-8"), delimiter="\t"))

    # Grassmann glosses. matched_lemmata.json is keyed by surface form and
    # its id_matched is a string for a simple lemma and a list for a lemma
    # written with variants ("dyu- ~ div-"), so index by the normalised
    # lemma string as well as by every id offered.
    gloss = {}
    if LEX:
        for v in json.load(open(LEX, encoding="utf-8")).values():
            m = v.get("meaning", "")
            if not m:
                continue
            key = re.sub(r"\s+", "", v.get("lemma", ""))
            if key:
                gloss.setdefault("L:" + key, m)
            ids = v.get("id_matched") or []
            if isinstance(ids, str):
                ids = [ids]
            for i in list(ids) + ([v["id_correction"]] if v.get("id_correction") else []):
                if isinstance(i, str):
                    gloss.setdefault(i, m)

    lemmas = {}                       # lemma -> dict
    for r in rows:
        L = r["lemma"]
        d = lemmas.get(L)
        if d is None:
            bare = clean(L)
            segs = segment(bare)
            dec  = classify(segs)
            d = lemmas[L] = {
                "lemma": L, "bare": bare, "segs": " ".join(segs),
                "lemma_id": r["lemma_id"], "gramm": r["gramm"],
                "decisions": dec, "tokens": 0,
                "books": collections.Counter(),
                "strata": collections.Counter(),
                "hymns": set(),
            }
        d["tokens"] += 1
        d["books"][r["book"]] += 1
        d["strata"][r["stratum"].upper()] += 1
        d["hymns"].add((r["book"], r["hymn"]))
        if not d["lemma_id"]:
            d["lemma_id"] = r["lemma_id"]

    for d in lemmas.values():
        nu = sum(1 for _, _, v, _ in d["decisions"] if v == "UNCONDITIONED")
        nc = len(d["decisions"]) - nu
        d["n_unconditioned"], d["n_conditioned"] = nu, nc
        d["category"] = ("NO-RETROFLEX" if not d["decisions"]
                         else "UNCONDITIONED" if nu else "CONDITIONED-ONLY")
        d["gloss"] = (gloss.get("L:" + re.sub(r"\s+", "", d["lemma"]), "")
                      or gloss.get(d["lemma_id"], ""))

    # ---- per-lemma table
    with open(PRE + "-lemmas.tsv", "w", encoding="utf-8") as f:
        f.write("\t".join(["lemma","lemma_id","gramm","bare","segments",
                           "category","n_unconditioned","n_conditioned",
                           "rules","tokens","hymns","books","strata",
                           "gloss"]) + "\n")
        for L in sorted(lemmas, key=lambda x: (-lemmas[x]["tokens"], x)):
            d = lemmas[L]
            f.write("\t".join([
                d["lemma"], d["lemma_id"], d["gramm"], d["bare"], d["segs"],
                d["category"], str(d["n_unconditioned"]), str(d["n_conditioned"]),
                "; ".join("%s=%s(%s)" % (p, v, ru) for _, p, v, ru in d["decisions"]),
                str(d["tokens"]), str(len(d["hymns"])),
                ",".join("%s:%d" % kv for kv in sorted(d["books"].items(),
                                                       key=lambda x: int(x[0]))),
                ",".join("%s:%d" % kv for kv in sorted(d["strata"].items())),
                d["gloss"].replace("\t", " "),
            ]) + "\n")

    # ---- per-segment decision table, for audit
    with open(PRE + "-segments.tsv", "w", encoding="utf-8") as f:
        f.write("lemma\tindex\tphoneme\tverdict\trule\tsegments\ttokens\n")
        for L in sorted(lemmas):
            d = lemmas[L]
            for i, p, v, ru in d["decisions"]:
                f.write("%s\t%d\t%s\t%s\t%s\t%s\t%d\n"
                        % (d["lemma"], i, p, v, ru, d["segs"], d["tokens"]))

    # ---- aggregates
    cat_l = collections.Counter(d["category"] for d in lemmas.values())
    cat_t = collections.Counter()
    for d in lemmas.values():
        cat_t[d["category"]] += d["tokens"]
    print("distinct lemmas: %d   tokens: %d" % (len(lemmas), sum(cat_t.values())),
          file=sys.stderr)
    for c in ("NO-RETROFLEX", "CONDITIONED-ONLY", "UNCONDITIONED"):
        print("  %-17s lemmas %5d (%5.1f%%)   tokens %6d (%5.1f%%)"
              % (c, cat_l[c], 100.0*cat_l[c]/len(lemmas),
                 cat_t[c], 100.0*cat_t[c]/sum(cat_t.values())), file=sys.stderr)

    with open(PRE + "-summary.json", "w", encoding="utf-8") as f:
        json.dump({"lemmas_by_category": cat_l,
                   "tokens_by_category": cat_t}, f, indent=2)


if __name__ == "__main__":
    main()
