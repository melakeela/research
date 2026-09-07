#!/usr/bin/env python3
"""
rv-pur-numeral-scan.py — build the numeral inventory for the §4J counts unit,
and report honestly what the scan can and cannot reach.

This script was MISSING from the first version of this unit. `rv-pur-counts.py`
hard-coded the inventory it produced, so the "12 candidates" figure could not be
reproduced from anything committed. That was the finding; this is the repair.

WHAT THE FIRST SCAN DID, AND ITS THREE FAILURE MODES

It scanned the Grassmann gloss of every lemma occurring in the 103 passages for
a German number word, with word boundaries. All three parts of that leaked:

  1. GLOSS COVERAGE. Only 585 of the 721 distinct lemmas carry a Grassmann
     gloss in info/matched_lemmata.json. The scan reached 81% of the lexicon,
     and the unit called it "an exhaustive scan of the corpus's own lexicon".
     It was not.
  2. WORD BOUNDARIES. `\bhundert\b` matches "hundert Kräfte" and fails on
     "hundertfache". That is why śatā́magha- "hundertfache Fülle besitzend" and
     śatā́tman- "hundertfaches Leben enthaltend" were never candidates.
  3. GERMAN ONLY. Grassmann glosses śatábhuji- as "centuplex" — Latin. No
     German number word appears in it at all, so the lemma was invisible to the
     scan even though it carries a hundred and agrees in full with the fort word
     at RV 7.15.14 and 1.166.8.

This script fixes all three: substring matching rather than word-bounded, Latin
and German number words, and an explicit stem fallback for the 136 lemmas with
no gloss. It prints its own coverage rather than asserting exhaustiveness.
"""
import csv, json, re, sys, collections

CLONE = sys.argv[1] if len(sys.argv) > 1 else \
    "/home/user/vedawebproject/vedaweb-data/rigveda"
SRC = sys.argv[2] if len(sys.argv) > 2 else "rv_pur_passages.json"

# Two classes, because one rule cannot serve both.
#
# UNAMBIGUOUS numerals are matched word-INITIALLY (\b...\w*), so that German
# compounds are reached: "hundertfache Fülle" matches, which the first scan's
# \bhundert\b did not. These stems do not occur inside unrelated German words.
NUM_UNAMBIGUOUS = re.compile(
    r"\b(hundert|tausend|neunzig|achtzig|siebzig|sechzig|fünfzig|vierzig|"
    r"dreissig|dreißig|zwanzig|zwölf|elf|zehn|neun|sieben|fünf|"
    r"hundertste|tausendste|neunte|siebente|siebte|zehnte|"
    # Latin — Grassmann glosses śatábhuji- as "centuplex" and nothing else.
    r"centuplex|centum|mille|septem|novem|nonaginta)\w*", re.I)
# AMBIGUOUS ones must stay word-BOUNDED on both sides. "ein" is the indefinite
# article and sits inside Feind, eine, Erscheinung, kein…; "acht" inside
# beachten, Macht; "drei" inside dreist; "vier" inside vierte but also
# Klavier. Bounded, they cost precision but not correctness, and every hit is
# adjudicated by hand anyway.
# German ordinals inflect (erster, erstem, ersten…), so they take an optional
# adjectival ending rather than a hard right boundary; "beide" likewise. Without
# this, prathamá- "erster, vorderster, frühester" and ubhá- "beide" are missed.
NUM_AMBIGUOUS = re.compile(
    r"\b(ein|eins|zwei|drei|vier|sechs|acht|Zahl|"
    r"beide[rnms]?|"
    r"erste[rnms]?|zweite[rnms]?|dritte[rnms]?|vierte[rnms]?|fünfte[rnms]?|"
    r"sechste[rnms]?|achte[rnms]?)\b", re.I)
# Stem fallback for the lemmas with no gloss at all — failure mode 1.
NUMSTEM = re.compile(
    r"(śatá|śatā|śata|navatí|navati|náva|nava|sahásra|sahasra|saptá|sapta|"
    r"pañcāśát|pañcā|trí|tri|éka|eka|ubhá|ubha|dvá|dvi|dáśa|daśa|viṃśatí|"
    r"triṃśát|ṣaṣṭí|saptatí|aśītí|prathamá|prathama|dvitī|tr̥tī|caturthá|ayúta)")


def main():
    ml = json.load(open(CLONE + "/info/matched_lemmata.json", encoding="utf-8"))
    gl = {}
    for _, v in ml.items():
        l, m = v.get("lemma"), v.get("meaning")
        if l and m:
            gl.setdefault(l, set()).add(m)

    data = json.load(open(SRC, encoding="utf-8"))
    lem = collections.Counter()
    for r in data:
        for t in r["tokens"]:
            lem[t["lemma"]] += 1

    glossed = [l for l in lem if l in gl]
    unglossed = [l for l in lem if l not in gl]

    by_gloss, by_stem = [], []
    for l in sorted(lem):
        gs = sorted(gl.get(l, []))
        if gs and any(NUM_UNAMBIGUOUS.search(g) for g in gs):
            by_gloss.append((l, lem[l], "U", " | ".join(gs)))
        elif gs and any(NUM_AMBIGUOUS.search(g) for g in gs):
            by_gloss.append((l, lem[l], "A", " | ".join(gs)))
        elif not gs and NUMSTEM.search(l):
            by_stem.append((l, lem[l], "S",
                            "(no Grassmann gloss — found by stem)"))

    print("distinct lemmas in the 103 passages : %d" % len(lem))
    print("  with a Grassmann gloss            : %d (%.1f%%)"
          % (len(glossed), 100.0 * len(glossed) / len(lem)))
    print("  without                           : %d — reachable only by stem"
          % len(unglossed))
    print()
    unamb = [x for x in by_gloss if x[2] == "U"]
    amb = [x for x in by_gloss if x[2] == "A"]
    print("candidates from an UNAMBIGUOUS number word (%d):" % len(unamb))
    for l, n, _, g in unamb:
        print("   %-20s %3d  %s" % (l, n, g[:86]))
    print()
    print("candidates from an AMBIGUOUS number word, bounded (%d) — mostly "
          "noise, adjudicated by hand:" % len(amb))
    for l, n, _, g in amb:
        print("   %-20s %3d  %s" % (l, n, g[:86]))
    print()
    print("candidates by stem, no gloss (%d):" % len(by_stem))
    for l, n, _, g in by_stem:
        print("   %-20s %3d  %s" % (l, n, g))
    print()
    print("TOTAL candidates: %d" % (len(by_gloss) + len(by_stem)))
    print()
    print("Adjudication of each candidate is in 04-AUDITS/rv-pur-counts.py")
    print("(NUMERALS and EXCLUDED) and in 03-REGISTERS/rigveda-pur-counts.csv.")


if __name__ == "__main__":
    main()
