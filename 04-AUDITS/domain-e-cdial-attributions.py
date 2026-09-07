#!/usr/bin/env python3
"""
Domain E, measurement 2: Turner's own non-Aryan attributions in CDIAL,
classified by donor family, and cross-checked against the Rigveda.

Why this exists. Distinction 3 of constitution §4.E is "accepted Old
Indo-Aryan Dravidian loans". The programme has been carrying the loan
lists second-hand (IH-231, IH-232). CDIAL is the one large etymological
dictionary of Indo-Aryan reachable in this session, and Turner marks his
loan attributions with an explicit arrow and his own abbreviation. So the
attributions can be counted directly instead of being recalled.

Three traps this script is built to avoid, all of them observed:

 1. "MuṇḍUp." is the Muṇḍaka Upaniṣad, a text, not the Muṇḍā language.
    A naive /Muṇḍ/ search returns 10 entries that are citations of an
    Upaniṣad and no evidence about Munda at all.
 2. Turner's abbreviation for the language is "Mu.", not "Muṇḍā". A
    search for the spelled-out name misses most of the real cases. The
    donor sets here are read out of CDIAL's own abbreviation key
    (cdial/abbrevs.py) rather than guessed.
 3. An arrow has a direction. "→ Muṇḍāri" is Indo-Aryan lending *to*
    Munda and is evidence against a substrate reading of that word, not
    for it. In and out are counted separately.

Sources: SRC-049 (CDIAL), SRC-043 (VedaWeb), SRC-022/023 (Zurich, Arnold).
Usage: domain-e-cdial-attributions.py [JAMBU_DATA] [RV_TOKENS_TSV] [OUTDIR]
"""
import csv, sys, re, os, collections, unicodedata, importlib.util

JAMBU  = sys.argv[1] if len(sys.argv) > 1 else "/tmp/jambu/data"
RVTOK  = sys.argv[2] if len(sys.argv) > 2 else "/tmp/rv_tokens_vedaweb.tsv"
OUTDIR = sys.argv[3] if len(sys.argv) > 3 else "/tmp"

# ---------------------------------------------------------------- donors
spec = importlib.util.spec_from_file_location("cd_abbrevs", f"{JAMBU}/cdial/abbrevs.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
ABB = mod.abbrevs

DRAV_ABB  = {k for k, v in ABB.items() if "Dravidian" in v}
MUNDA_ABB = {k for k, v in ABB.items() if "Muṇḍā" in v or v.strip() == "Muṇḍā"}
# "Drav" and "Mu" are themselves keys; keep the family labels explicit.
DRAV_ABB.add("Drav")
MUNDA_ABB.add("Mu")

TAG = re.compile(r"<[^>]+>")
# Muṇḍaka / Muṇḍakopaniṣad citations, which are not the language.
UPANISAD = re.compile(r"Muṇḍ(?:Up|akUp|aka)\b")


def alt(names):
    return "|".join(sorted((re.escape(n) for n in names), key=len, reverse=True))


ARROW_IN = {
    "dravidian": re.compile(r"←[^←→\]]{0,80}?(?:\b(?:%s)\b\.?|\bDravidian\b)" % alt(DRAV_ABB)),
    "munda":     re.compile(r"←[^←→\]]{0,80}?(?:\b(?:%s)\b\.?|Muṇḍ\w*|\bMunda\b)" % alt(MUNDA_ABB)),
}
ARROW_OUT = {
    "dravidian": re.compile(r"→[^←→\]]{0,80}?(?:\b(?:%s)\b\.?|\bDravidian\b)" % alt(DRAV_ABB)),
    "munda":     re.compile(r"→[^←→\]]{0,80}?(?:\b(?:%s)\b\.?|Muṇḍ\w*|\bMunda\b)" % alt(MUNDA_ABB)),
}
# Turner's key names only two Munda abbreviations (Mu., Sant.); the family
# and its languages are also written out in his running prose, so the
# mention test adds the spelled-out name. UPANISAD has already been removed
# from `clean`, so "Muṇḍ\w*" here cannot pick up Muṇḍaka Upaniṣad.
MUNDA_NAME = r"Muṇḍ\w*|Munda\b|Muṇḍāri|Savara|Kūrkū|Kharia"
MENTION = {
    "dravidian": re.compile(r"\b(?:%s)\b\.?|\bDravidian\b" % alt(DRAV_ABB)),
    "munda":     re.compile(r"\b(?:%s)\b\.?|(?:%s)" % (alt(MUNDA_ABB), MUNDA_NAME)),
}
# Turner hedges his attributions and the hedge must not be silently dropped.
HEDGE = re.compile(r"\b(?:[Pp]oss\.|[Pp]erh\.|[Pp]rob\.|[Dd]oubtful|"
                   r"[Uu]ncert\.|\?|ac\. to)\b|\?")
# Turner's first-attestation tag for the Rigveda.
RV_TAG = re.compile(r"\bRV\.")

NUM = re.compile(r"^\s*(\d+)")


def strip_tags(s):
    return TAG.sub("", s or "")


# Vedic tone marks only. Macron (U+0304), dot-below (U+0323), line-below
# (U+0331), tilde and ring are NOT accents: they carry vowel length,
# retroflexion, syllabicity and nasality, and stripping them merges
# kala/kala, kuta/kuta, mala/mala and sava/sava into false matches. That is
# the same error correction C-04 records, and it was caught here by reading
# the first output rather than by assumption.
TONE = "\u0301\u0300\u0341\u0340\u0951\u0952\u1cda\u1cdb\u1cdc\u1cdd\u1cde"


# Orthographic conventions that differ between the two editions without
# any phonemic difference. Sanskrit has no short e or o, so Turner's macron
# on them is redundant marking, not length; and the anusvara is written
# with an overdot in CDIAL and an underdot in the Zurich layer. Folding
# these is recall, not licence: nothing phonemic is merged.
FOLD = {"\u014d": "o", "\u014c": "O", "\u0113": "e", "\u0112": "E",
        "\u1e41": "\u1e43", "\u1e40": "\u1e42"}


def norm(s):
    """Strip Vedic tone marking and fold the two purely orthographic
    conventions; keep every diacritic that distinguishes a phoneme.
    Case-folded, with a leading star or trailing hyphen removed."""
    s = unicodedata.normalize("NFC", s)
    s = "".join(FOLD.get(c, c) for c in s)
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if c not in TONE)
    return unicodedata.normalize("NFC", s).lower().strip(" -*")


# ---------------------------------------------------------------- CDIAL
entries = []
for r in csv.reader(open(f"{JAMBU}/cdial/params.csv")):
    if len(r) < 4:
        continue
    eid, head, text = r[0], r[1], strip_tags(r[3])
    clean = UPANISAD.sub(" ", text)
    e = dict(cdial_id=eid, headword=head, text=text, clean=clean)
    for fam in ("dravidian", "munda"):
        e[f"{fam}_in"] = bool(ARROW_IN[fam].search(clean))
        e[f"{fam}_out"] = bool(ARROW_OUT[fam].search(clean))
        e[f"{fam}_mention"] = bool(MENTION[fam].search(clean))
    e["rv_tag"] = bool(RV_TAG.search(text))
    e["upanisad_only"] = bool(UPANISAD.search(text)) and not MENTION["munda"].search(clean)
    entries.append(e)

# ---------------------------------------------------------------- Rigveda
rv_lemma_count = collections.Counter()
rv_lemma_books = collections.defaultdict(collections.Counter)
rv_lemma_strata = collections.defaultdict(collections.Counter)
with open(RVTOK) as f:
    rd = csv.DictReader(f, delimiter="\t")
    for t in rd:
        lem = t["lemma"]
        rv_lemma_count[lem] += 1
        rv_lemma_books[lem][t["book"]] += 1
        rv_lemma_strata[lem][t["stratum"]] += 1

rv_index = collections.defaultdict(set)          # normalised -> {lemma}
for lem in rv_lemma_count:
    rv_index[norm(lem)].add(lem)


def rv_lookup(headword):
    """Match a CDIAL headword against the Zurich lemma inventory at three
    separate strengths, because they are three different kinds of
    attestation and the attestation gradient forbids merging them:

      simplex     the lemma IS the headword
      compound    the headword is a component of a longer lemma
      derivative  a longer lemma begins with the headword

    Turner marks this distinction himself. CDIAL 9865 mayūra reads
    "'peacock' VS., in cmpds. RV., mayūrī- f. 'peahen' RV." — and the
    Zurich layer indeed has no simplex mayūra-, but does have
    mayūraroman-, mayūraśepya- and mayūrī-. Reporting that as "attested
    in the Rigveda" without saying how would be false; reporting it as
    "not attested" would be false too.

    The containment search needs a floor, or short headwords match
    everything; 4 characters is that floor and short headwords are
    therefore simplex-only. That is a stated recall limit, not a silent one.
    """
    h = norm(headword)
    out = {"simplex": set(), "derivative": set(), "compound": set()}
    if not h:
        return out
    out["simplex"] = set(rv_index.get(h, ()))
    if len(h) >= 4:
        for nl, lemmas in rv_index.items():
            if nl == h:
                continue
            if nl.startswith(h):
                out["derivative"] |= lemmas
            elif h in nl:
                out["compound"] |= lemmas
    return out


# ---------------------------------------------------------------- outputs
os.makedirs(OUTDIR, exist_ok=True)

# (a) the attribution counts, naive and corrected
naive_munda = sum(1 for e in entries if re.search(r"\bMuṇḍ\w*|\bMunda\b", e["text"]))
naive_munda_upanisad = sum(1 for e in entries if e["upanisad_only"])
counts = dict(
    cdial_entries=len(entries),
    drav_in=sum(1 for e in entries if e["dravidian_in"]),
    drav_out=sum(1 for e in entries if e["dravidian_out"]),
    drav_mention=sum(1 for e in entries if e["dravidian_mention"]),
    munda_in=sum(1 for e in entries if e["munda_in"]),
    munda_out=sum(1 for e in entries if e["munda_out"]),
    munda_mention=sum(1 for e in entries if e["munda_mention"]),
    naive_munda=naive_munda,
    naive_munda_upanisad=naive_munda_upanisad,
    drav_in_rvtag=sum(1 for e in entries if e["dravidian_in"] and e["rv_tag"]),
    munda_in_rvtag=sum(1 for e in entries if e["munda_in"] and e["rv_tag"]),
    drav_in_hedged=sum(1 for e in entries if e["dravidian_in"] and HEDGE.search(e["clean"])),
    munda_in_hedged=sum(1 for e in entries if e["munda_in"] and HEDGE.search(e["clean"])),
)

# (b) the candidate register: every arrow-in entry, with its Rigvedic standing
cand_path = os.path.join(OUTDIR, "domain-e-cdial-loan-candidates.csv")
with open(cand_path, "w", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(["cand_id", "cdial_id", "headword", "donor_family", "direction",
                "turner_hedged", "turner_rv_tag_in_entry", "rv_simplex_lemma",
                "rv_simplex_tokens", "rv_derivative_lemmas", "rv_compound_lemmas",
                "rv_books_simplex", "rv_strata_simplex", "bracket",
                "source_id", "retrieval_date"])
    n = 0
    for e in entries:
        for fam in ("dravidian", "munda"):
            for direction, key in (("into-Indo-Aryan", f"{fam}_in"),
                                   ("out-of-Indo-Aryan", f"{fam}_out")):
                if not e[key]:
                    continue
                n += 1
                hits = rv_lookup(e["headword"])
                sim = sorted(hits["simplex"])
                tot = sum(rv_lemma_count[l] for l in sim)
                books = collections.Counter()
                strata = collections.Counter()
                for l in sim:
                    books.update(rv_lemma_books[l])
                    strata.update(rv_lemma_strata[l])
                br = ""
                m = re.search(r"\[([^\]]*)\]", e["clean"])
                if m:
                    br = re.sub(r"\s+", " ", m.group(1))[:300]
                w.writerow([
                    "DE-CAND-%03d" % n, e["cdial_id"], e["headword"], fam, direction,
                    "yes" if HEDGE.search(e["clean"]) else "no",
                    "yes" if e["rv_tag"] else "no",
                    "; ".join(sim), tot,
                    "; ".join(sorted(hits["derivative"])[:8]),
                    "; ".join(sorted(hits["compound"])[:8]),
                    " ".join(f"{b}:{c}" for b, c in sorted(books.items(), key=lambda x: int(x[0]))),
                    " ".join(f"{s or 'none'}:{c}" for s, c in sorted(strata.items())),
                    br, "SRC-049; SRC-043; SRC-022; SRC-023", "2026-09-07"])

# (c) the naive-versus-corrected search audit, and the corpus stratum baseline
NAIVE = re.compile(r"\bMuṇḍ\w*|\bMunda\b")
naive_hits = [e for e in entries if NAIVE.search(e["text"])]
naive_true = [e for e in naive_hits if e["munda_mention"]]
all_true = [e for e in entries if e["munda_mention"]]
counts["naive_munda_precision_pct"] = round(100.0 * len(naive_true) / max(1, len(naive_hits)), 1)
counts["naive_munda_recall_pct"] = round(100.0 * len(naive_true) / max(1, len(all_true)), 1)

corpus_strata = collections.Counter()
for lem, c in rv_lemma_strata.items():
    corpus_strata.update({k: v * 1 for k, v in c.items()})
counts["rv_tokens_total"] = sum(rv_lemma_count.values())
counts["rv_lemmas_total"] = len(rv_lemma_count)

stats_path = os.path.join(OUTDIR, "domain-e-cdial-attribution-stats.csv")
with open(stats_path, "w", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(["key", "value"])
    for k, v in counts.items():
        w.writerow([k, v])
    for st, c in sorted(corpus_strata.items()):
        w.writerow([f"rv_corpus_tokens_stratum_{st or 'none'}", c])

print("counts:")
for k, v in counts.items():
    print(f"  {k:28} {v}")
print(f"\n{n} candidate rows -> {cand_path}")
print(f"stats -> {stats_path}")
