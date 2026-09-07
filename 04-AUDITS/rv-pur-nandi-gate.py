#!/usr/bin/env python3
"""
rv-pur-nandi-gate.py — the measurements behind the Nandi gate, and behind the
corpus-wide control on the ninety-nine expression.

Constitution §4J names one prohibition — "Do not automatically translate pur
into a Mature Harappan city" — and R. N. Nandi, "The City and the Citadel"
(An Outline of the Aryan Civilization, ch. 4, Routledge 2017,
DOI 10.4324/9781315101149-4) is that translation in its canonical published
form. The chapter is NOT retrieved (SRC-086 identified-not-retrieved; SRC-087
EGRESS_BLOCKED on both channels). SRC-088 is Semenenko, a different work.
What is gated here is the thesis as its publisher's abstract states it, and
the gate is over this corpus, not over Nandi's argument, which has not been
read.

This script only measures. Every verdict is in
03-REGISTERS/domain-j-interpretations.csv and 03-REGISTERS/HYPOTHESIS-
ELIGIBILITY.csv, and every measurement in 03-REGISTERS/domain-j-measurements.csv.

Sources (02-SOURCES/access-ledger.csv):
  SRC-069  clone @ d3eb8af7324338161520d2d35eae8f7e985a19a5
  SRC-020  aufrecht.csv        SRC-022 Zurich token layer
  SRC-072  geldner   SRC-073 griffith   SRC-074 grassmann
  SRC-022  Zurich annotation layer, incl. info/matched_lemmata.json.
  SRC-089  the TEI header, which establishes what that gloss field IS. It is
           column V, LEMMA_ZÜRICH_BEDEUTUNG - the Zurich lemma-meaning column,
           a modern composite citing Geldner, EWAia/Mayrhofer, Scarlata,
           Oldenberg, Lubotsky, Renou and Kuiper, with Grassmann marked 'GM:'
           where followed. It is NOT Grassmann's Worterbuch, which this
           repository has never retrieved. Earlier versions of this script and
           of every row built on it said "Grassmann"; that was wrong (BF-017,
           DEP-026). Per DEP-005 the lemmatisation and the gloss are still ONE
           source, so no gloss-based result below is independent of it.
  SRC-084  this session's re-clone and reproduction check

Input:  rv_tokens_vedaweb.tsv, from 04-AUDITS/rv-token-extract.py
Usage:  python3 rv-pur-nandi-gate.py <clone>/rigveda rv_tokens_vedaweb.tsv
"""
import csv, json, os, sys, collections

csv.field_size_limit(10 ** 8)

CL = sys.argv[1] if len(sys.argv) > 1 else \
    "/home/user/vedawebproject/vedaweb-data/rigveda"
TOKENS = sys.argv[2] if len(sys.argv) > 2 else "rv_tokens_vedaweb.tsv"

# The seven lemmas of PUR-006, over eight lemma strings.
FAMILY = {"púr-", "puraṃdará-", "pūrbhíd-", "pūrbhíttama-",
          "pūrbhídya-", "pū́rpati-", "purohán-", "púrya-"}

# The six fort-adjacent non-púr- lemmas PUR-006 excluded by design. They are
# the semantic reading of "the complete corpus" that reconciliation C-2 leaves
# open, and they are searched here so the exclusion is measured, not assumed.
ADJACENT = ["paridhí-", "dehī́-", "saṃdíh-", "harmyá-", "ádhr̥ṣṭa-", "dārú-"]

# Cardinals, keyed on the corpus's own lemma strings. 'náva- 1' is nine;
# 'náva- 2' is new. The corpus disambiguates the homograph and a search on a
# bare 'náva-' silently returns nothing at all — which is how this script's
# first draft "established" that the 99 expression does not occur.
NUMERAL = {
    "éka-": 1, "dvá-": 2, "trí-": 3, "catúr-": 4, "páñca-": 5, "ṣáṣ-": 6,
    "saptá-": 7, "aṣṭá-": 8, "náva- 1": 9, "dáśa-": 10, "viṃśatí-": 20,
    "triṃśát-": 30, "catvāriṃśát-": 40, "pañcāśát-": 50, "ṣaṣṭí-": 60,
    "saptatí-": 70, "aśītí-": 80, "navatí-": 90, "śatá-": 100,
    "sahásra-": 1000,
}

# German gloss probes. The Zurich gloss column is written in German; an English
# probe returns nothing and would read as an absence. Exactly ONE gloss in the
# corpus is Latin — śatábhuji- "centuplex" — and no German probe reaches it.
# Its two tokens are RV 7.15.14 and 1.166.8, both already inside the púr- corpus
# and adjudicated at PUR4J-032, so the Latin gap has no live exposure here.
# ("A handful are Latin" was asserted in an earlier version of this comment and
# in DJ-008, from plausibility rather than from a count. BF-017.)
#
# AND A HARD LIMIT ON WHAT MAY BE PROBED AT ALL: this column has ZERO coverage
# of verb roots — 0 of 700 root lemmas carry a meaning field, 19.4% of corpus
# tokens. A probe here for bauen, errichten, zimmern or any other VERB returns a
# guaranteed zero whatever the corpus contains, and reporting one as an absence
# is BF-015's failure mode. Nominal probes (Ziegel, Stadt) are sound; verbal
# ones are not available from this source. BF-018, RA-021.
GLOSS_PROBES = {
    "brick":              ["ziegel"],
    "city":               ["stadt", "städt"],
    "wall/rampart":       ["mauer", "wall", "verschanz", "palisad", "damm",
                           "aufwurf"],
    "clay":               ["lehm"],
    "stone":              ["stein"],
    "well/cistern":       ["brunnen", "zisterne"],
    "street":             ["strasse", "straße", "gasse"],
    "house/dwelling":     ["haus", "wohnung", "behausung"],
    "village/settlement": ["dorf", "siedlung", "ansiedl", "niederlassung"],
    "fortress":           ["burg", "festung"],
}

# Nandi's four terms, as the abstract names them, by lemma stem.
NANDI_TERMS = ["púr", "durg", "vr̥tra", "vr̥jána"]


def load_glosses():
    path = os.path.join(CL, "info/matched_lemmata.json")
    gl = json.load(open(path, encoding="utf-8"))
    by_lemma = collections.defaultdict(set)
    for _surface, e in gl.items():
        if e.get("lemma") and e.get("meaning"):
            by_lemma[e["lemma"]].add(e["meaning"])
    return by_lemma


# The cooked/raw pair. DJ-009 claims RV 2.35.6 is the only place either word is
# applied to a structure. That is a claim about a CLOSED set of 36 tokens, so it
# is checked by enumeration rather than disclosed as unsurveyed — the previous
# two versions of DJ-009 were an unmeasured assertion and a wrong
# characterisation, and this function exists so the third is neither.
COOKED_RAW = {"pakvá-", "āmá-"}

# Structures, to test the "only place" clause against something positive.
#
# THIS IS A HAND-WRITTEN CLOSED SET OF TEN LEMMAS, and DJ-009's phrase "applied
# to a structure" reads as a semantic category rather than a list. The check
# that licenses the word is the wider one below: STRUCTURE_WIDE derives ~346
# lemmas from the gloss column itself, and cooked_raw_scan runs it at STANZA
# scope as a negative control, because a modifier's head can sit in another
# pāda — 8 of the 11 āmá- tokens have no agreement partner in their own pāda at
# all, so same-pāda scope alone could not support a negative.
STRUCTURE = {"púr-", "dehī́-", "paridhí-", "harmyá-", "gr̥há-", "dáma-",
             "duroṇá-", "sádas-", "kṣáya-", "víś-"}

STRUCTURE_GLOSS_KEYS = ("haus", "wohn", "burg", "wall", "palisad", "verschanz",
                        "siedl", "dorf", "stätte", "sitz", "mauer", "damm",
                        "aufwurf", "behausung", "niederlassung", "ansiedl")


def agreement_partners(toks_in_pada, tok):
    """Nominal stems in the same pāda agreeing with tok in case/number.

    Adjective-noun agreement is the only evidence available here that a word
    modifies another; sharing a stanza is not, which is the mistake PUR-022's
    collocation profile was written to avoid and DJ-009 v2 made anyway.
    """
    def feats(t):
        d = dict(x.split("=", 1) for x in t["morph"].split("|") if "=" in x)
        return d.get("case"), d.get("number")
    c, n = feats(tok)
    if not c:
        return []
    out = []
    for o in toks_in_pada:
        if o is tok or o["lemma"] in COOKED_RAW:
            continue
        oc, on = feats(o)
        if oc == c and on == n:
            out.append(o["lemma"])
    return out


def cooked_raw_scan(toks):
    """Print every pakvá-/āmá- token with what it agrees with. DJ-009."""
    by_pada = collections.defaultdict(list)
    for t in toks:
        by_pada[(t["stanza"], t["pada"])].append(t)
    print("\n== THE COOKED/RAW PAIR, EVERY TOKEN, WITH ITS AGREEMENT PARTNERS ==")
    hits_on_structure = []
    for lem in ("pakvá-", "āmá-"):
        rows = [t for t in toks if t["lemma"] == lem]
        print("  %s — %d tokens" % (lem, len(rows)))
        for t in rows:
            partners = agreement_partners(by_pada[(t["stanza"], t["pada"])], t)
            struct = [p for p in partners if p in STRUCTURE]
            if struct:
                hits_on_structure.append((t["stanza"], lem, struct))
            print("      %s %s %-12s agrees with %s%s"
                  % (t["stanza"], t["pada"], t["surface"],
                     partners or "(nothing in this pāda)",
                     "   <-- STRUCTURE" if struct else ""))
    print("  tokens agreeing with a structure word: %d %s"
          % (len(hits_on_structure), hits_on_structure))
    print("  DJ-009's 'only place' clause holds iff that list is exactly"
          " [('02.035.06', 'āmá-', ['púr-'])].")

    # Negative control: a structure vocabulary derived from the gloss column
    # rather than hand-written, matched at STANZA scope rather than pāda.
    gloss = load_glosses()
    wide = {l for l in gloss
            if any(k in m.lower() for m in gloss[l]
                   for k in STRUCTURE_GLOSS_KEYS)}
    by_stanza = collections.defaultdict(list)
    for t in toks:
        by_stanza[t["stanza"]].append(t)
    print("  -- negative control: %d structure lemmas from the gloss column,"
          " matched at stanza scope --" % len(wide))
    for t in toks:
        if t["lemma"] not in COOKED_RAW:
            continue
        def feats(x):
            d = dict(y.split("=", 1) for y in x["morph"].split("|") if "=" in y)
            return d.get("case"), d.get("number"), d.get("gender")
        c, n, g = feats(t)
        for o in by_stanza[t["stanza"]]:
            if o["lemma"] not in wide:
                continue
            oc, on, og = feats(o)
            if (oc, on) == (c, n):
                strict = "STRICT" if og == g else "excluded on gender"
                print("      %s %s ~ %s (%s) %s"
                      % (t["stanza"], t["lemma"], o["lemma"], o["pada"],
                         strict))


def main():
    toks = list(csv.DictReader(open(TOKENS, encoding="utf-8"), delimiter="\t"))
    by_stanza = collections.defaultdict(list)
    for t in toks:
        by_stanza[t["stanza"]].append(t)
    freq = collections.Counter(t["lemma"] for t in toks)
    gloss = load_glosses()

    print("corpus: %d tokens, %d stanzas, %d distinct lemmas"
          % (len(toks), len(by_stanza), len(freq)))

    # ---- the denominator every absence below is stated against -------------
    unglossed = [l for l in freq if l not in gloss]
    ung_tokens = sum(freq[l] for l in unglossed)
    print("\n== DENOMINATOR ==")
    print("  lemmas with a Zurich gloss    : %d / %d (%.1f%%)"
          % (len(freq) - len(unglossed), len(freq),
             100.0 * (len(freq) - len(unglossed)) / len(freq)))
    print("  tokens under a glossed lemma  : %.2f%%"
          % (100.0 * (len(toks) - ung_tokens) / len(toks)))
    print("  commonest unglossed lemmas    : %s"
          % [l for _, l in sorted(((freq[l], l) for l in unglossed),
                                  reverse=True)[:10]])

    # ---- the 99 expression, over the whole corpus --------------------------
    pur_stanzas = {s for s, ts in by_stanza.items()
                   if any(t["lemma"] in FAMILY for t in ts)}
    nn = sorted(s for s, ts in by_stanza.items()
                if any(t["lemma"] == "navatí-" for t in ts)
                and any(t["lemma"] == "náva- 1" for t in ts))
    nav = sorted(s for s, ts in by_stanza.items()
                 if any(t["lemma"] == "navatí-" for t in ts))
    print("\n== THE NINETY-NINE EXPRESSION, CORPUS-WIDE ==")
    print("  stanzas with navatí- at all                  : %d" % len(nav))
    print("  stanzas with navatí- AND náva- 1 (i.e. 99)   : %d" % len(nn))
    inside = [s for s in nn if s in pur_stanzas]
    outside = [s for s in nn if s not in pur_stanzas]
    print("  of those, inside the púr- corpus            : %d %s"
          % (len(inside), inside))
    print("  of those, outside it                        : %d %s"
          % (len(outside), outside))

    # ---- the semantic reading of the corpus (reconciliation C-2) -----------
    print("\n== THE SIX FORT-ADJACENT LEMMAS, AND THEIR NUMERALS ==")
    for lem in ADJACENT:
        st = sorted(s for s, ts in by_stanza.items()
                    if any(t["lemma"] == lem for t in ts))
        withnum = [(s, sorted({t["lemma"] for t in by_stanza[s]
                               if t["lemma"] in NUMERAL})) for s in st]
        withnum = [(s, n) for s, n in withnum if n]
        print("  %-11s %2d stanzas; %d carry a cardinal: %s"
              % (lem, len(st), len(withnum), withnum))

    # ---- the locative test -------------------------------------------------
    print("\n== IS A púr- A PLACE ANYONE IS IN? ==")
    cases = collections.Counter()
    locs = []
    for t in toks:
        if t["lemma"] == "púr-":
            c = [x for x in t["morph"].split("|") if x.startswith("case=")]
            k = c[0][5:] if c else "?"
            cases[k] += 1
            if k == "LOC":
                locs.append((t["stanza"], t["pada"], t["surface"]))
    n = sum(cases.values())
    for k, v in cases.most_common():
        print("  %-4s %3d  %5.1f%%" % (k, v, 100.0 * v / n))
    print("  the locative tokens: %s" % locs)

    # ---- the architecture lexicon -----------------------------------------
    print("\n== ARCHITECTURE VOCABULARY, BY GRASSMANN GLOSS ==")
    for label, keys in GLOSS_PROBES.items():
        hits = []
        for l in freq:
            for m in gloss.get(l, ()):
                if any(k in m.lower() for k in keys):
                    hits.append((freq[l], l, m))
                    break
        hits.sort(reverse=True)
        if hits:
            print("  %-19s %2d lemmas; commonest: %s"
                  % (label, len(hits), [(l, c) for c, l, _ in hits[:5]]))
        else:
            print("  %-19s ABSENT from every glossed lemma" % label)

    # ---- Nandi's four terms ------------------------------------------------
    print("\n== NANDI'S FOUR TERMS ==")
    for stem in NANDI_TERMS:
        hits = sorted(((freq[l], l, "; ".join(sorted(gloss.get(l, {"(none)"}))))
                       for l in freq if l.startswith(stem)), reverse=True)
        print("  stem %-8s %d lemmas" % (repr(stem), len(hits)))
        for c, l, m in hits[:4]:
            print("      %5d  %-16s %s" % (c, l, m[:88]))

    cooked_raw_scan(toks)

    # durgá- is the term the gate turns on: every token, with its case.
    print("\n== EVERY durgá- TOKEN ==")
    dg = [t for t in toks if t["lemma"] == "durgá-"]
    gen = collections.Counter(
        [x[7:] for t in dg for x in t["morph"].split("|")
         if x.startswith("gender=")])
    print("  %d tokens; gender: %s" % (len(dg), dict(gen)))
    print("  stanzas: %s" % sorted({t["stanza"] for t in dg}))


if __name__ == "__main__":
    main()
