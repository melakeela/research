#!/usr/bin/env python3
"""
rv-pur-fields.py — emit 03-REGISTERS/rigveda-pur-fields.csv, the §4J semantic
fields per passage: patron, poet lineage, opponent, description, material,
water, cattle, treasure, mountain or river, proposed geography.

06-BRIEFS/rv01-reconciliation.md §6 said of water/cattle/treasure: "Not
retrievable until the semantic fields are stated. Undefined, they become places
to put what the reader already believes." So each field is DEFINED HERE, before
it is filled, and every definition is a rule over the corpus's own lexicon —
Grassmann's glosses for all 721 lemmas occurring in the 103 passages — rather
than a list of words chosen for what they would show.

DEFINITIONS

  description  A token that agrees with a púr- family token in case, gender AND
               number, in the same pāda (tight) or the same hemistich (loose).
               Agreement is the corpus's own marking of attribution; nothing is
               called a descriptor because it "sounds like" one. Both scopes are
               reported: the tight scope misses aśmanmáya- at RV 4.30.20, which
               modifies purā́m across a pāda break, and the loose scope admits
               noise, so neither is used alone.

  material     The subset of `description` whose Grassmann gloss denotes a
               substance. Reported as its own column because §4J separates
               material from description and RV-01 merged them away — the
               reconciliation brief's C-7.

  water        Lemmas glossed with a water word (Wasser, Fluss, Strom, Flut,
  cattle       Meer, Gewässer, Woge, Quell); with a cattle word (Kuh, Rind,
  treasure     Vieh, Stier, Herde, Pferch); or with a possession word (Schatz,
  mountain     Reichtum, Beute, Gut, Besitz, Habe, Gabe); or with a highland
               word (Berg, Fels, Gebirge, Hügel).

               TWO EXCLUSIONS APPLIED TO ALL FOUR, each recorded because it
               changes the result:
               (a) bahuvrīhi epithets — glosses containing habend, besitzend,
                   gewinnend, findend, enthaltend, spendend. Without this,
                   `treasure` returns 56 lemmas for the 103 passages, most of
                   them "having X" epithets of Indra. It is the field most
                   exposed to the brief's warning and the one most tightened.
               (b) praise-song senses — Preislied, Lobpreisung, Lob. Grassmann's
                   `Preis` covers both "prize" and "praise", so an unfiltered
                   treasure field silently collects the words for hymns.

  river        Lemmas that could name a river. Reported as
               `river_lemma_present`, NOT as "named river": the only such lemma
               in the 103 passages is síndhu-, and Grassmann glosses it
               "Fluss, Strom; der Indus" — BOTH the common noun and the
               proper name. Which one a passage needs is a reading, and the
               translators split on it (PUR4J-028), so the column records
               presence and the claim records the split.

               A hydronym in a passage is in any case a TEXTUAL fact. The step
               from it to a place on a map is a separate claim and this
               register does not take it.

  patron       Lemmas whose Grassmann gloss marks a proper name (N. pr., Name
  opponent     eines …), split by the ROLE WORD IN GRASSMANN'S OWN GLOSS:
               Schützling/Günstling/König/Fürst/Sänger → patron side;
               Dämon/Feind/Dasyu/bekämpft/getötet → opponent side.

               This is Grassmann's classification of the NAME, not a reading of
               this passage's syntax. A name can appear in a passage without
               holding or attacking anything in it. The column is headed
               `_candidates` for that reason and every row says so.

               It also imports Grassmann's categories, and `Dämon` is one of
               them. The constitution §7 list of inherited categories to audit
               before use — race, tribe, slave, barbarian, fort, religion,
               caste, civilization, invasion, indigenous — does not name
               "demon", and on the evidence of this field it should.

  poet lineage Geldner's per-hymn group heading (SRC-070). Where the heading
               names a deity rather than a poet, the field records that, and
               the absence is typed NOT PRODUCED. HOLD-006.

  geography    NOT FILLED. There is no geographic content in the pinned corpus
               (manifest extension, "What rv_locations is not"). What this
               register can carry is which hydronyms and toponyms occur; the
               proposed-geography field needs a source this unit does not have,
               and it is bounded by the research hold at Version 12 line 1175.
"""
import csv, json, re, sys, collections

SRC = sys.argv[1] if len(sys.argv) > 1 else "rv_pur_passages.json"
CLONE = sys.argv[2] if len(sys.argv) > 2 else \
    "/home/user/vedawebproject/vedaweb-data/rigveda"
OUT = sys.argv[3] if len(sys.argv) > 3 else \
    "/home/user/research/03-REGISTERS/rigveda-pur-fields.csv"

EPITHET = re.compile(r"(habend|besitzend|gewinnend|findend|enthaltend|"
                     r"spendend|darreichend|bringend|erlangend)", re.I)
PRAISE = re.compile(r"(Preislied|Lobpreisung|Preis, Lob|Lobgesang|preisend)", re.I)
# A word for the OWNER of a thing is not the thing. Without this, páti- "Herr,
# Gebieter, Besitzer" enters `treasure` in 5 passages on the string "Besitz".
OWNER = re.compile(r"(Besitzer|Eigentümer|Herr, |Gebieter)", re.I)
# Grassmann's usage notes name what a word is SAID OF. ádhr̥ṣṭa- "unwiderstehlich
# (gesagt von Göttern, Felsen, Burgen etc.)" is not a word for a mountain; the
# match is in the note, not in the sense.
USAGE_NOTE = re.compile(r"\(?gesagt von[^)]*\)?|\(von [^)]*gesagt\)", re.I)

FIELD = {
    "water":    re.compile(r"\b(Wasser|Fluss|Flüsse|Flut|Strom|Ström\w*|Meer|"
                           r"Gewässer|Woge|Quell\w*|Ozean|Regen)\w*", re.I),
    "cattle":   re.compile(r"\b(Kuh|Kühe|Rind|Rinder|Vieh|Stier|Herde|Pferch|"
                           r"Hürde|Stall|Milch)\w*", re.I),
    "treasure": re.compile(r"\b(Schatz|Schätze|Reichtum|Reichtümer|Beute|"
                           r"Besitz|Habe|Gabe|Geschenk|Kampfpreis|Siegerpreis|"
                           r"Eigentum)\w*", re.I),
    "mountain": re.compile(r"\b(Berg|Berge|Fels|Felsen|Gebirg\w*|Hügel|Anhöhe)\w*", re.I),
    "material": re.compile(r"\b(eisern|ehern|Erz|Metall|Eisen|Stein|steinern|"
                           r"Holz|hölzern|Lehm|Ton|Gold|golden|roh|ungekocht)\w*", re.I),
}
NAME = re.compile(r"(N\. pr\.|Eigenname|Name ein|Name des|Name der|Personenname)")
PATRON_ROLE = re.compile(r"\b(Schützling|Günstling|König|Fürst|Sänger|Opferer|"
                         r"Stammeshelden|Volksstamm|Priestergeschlecht|Sängerfamilie|"
                         r"Dichter|R̥ṣi|Rṣi|guter Geber)", re.I)
# \b matters here and is not decoration. Without it, "Dasyu" matches inside
# TRASADASYU and PURUKUTSA's own gloss ("des Trasadasyu Vater"), and both — a
# prince and a king, each glossed Schützling, protégé — were sorted onto the
# OPPONENT side. Purukutsa is the patron of the seven-fort cycle (PUR4J-010),
# so the bug put the register in contradiction with this unit's own claim.
OPPONENT_ROLE = re.compile(r"\b(Dämon|Feind|Dasyu|bekämpft|getötet|überwundenen|"
                           r"indrafeindlich|überlisteten|Dāsa|feindselig)", re.I)
# An explicit protégé marker settles the side even when the gloss also names an
# adversary — a king is often described by who he was protected against.
PATRON_DECISIVE = re.compile(r"\b(Schützling|Günstling|Zögling)", re.I)
# §4J's "patron" is the human on whom the poet depends. A god glossed
# "Götterkönig" is not one; without this, váruṇa- enters the patron column on
# the string König.
DEITY_ONLY = re.compile(r"\b(Name eines Gottes|Name einer Gottheit|"
                        r"Bezeichnung der Götter)", re.I)
HEM = {"a": 1, "b": 1, "c": 2, "d": 2, "e": 3, "f": 3, "g": 4, "h": 4}

# Agreeing tokens that are NOT descriptors of a púr-, excluded by hand with the
# reason recorded rather than dropped. Keyed (stanza, lemma).
NOT_A_DESCRIPTOR = {
    ("05.041.12", "srúc-"):
        "RV 5.41.12d 'pári srúco babr̥hāṇásyā́dreḥ'. srúcaḥ (ladles) agrees with "
        "púraḥ in case, gender and number and sits in the same hemistich, but "
        "belongs to a different clause: pāda c has 'ā́paḥ púro ná śubhrā́ḥ', "
        "the waters bright LIKE forts. A coincidence of NOM.PL.F, and the "
        "measure of how much noise the stanza scope admits.",
    ("07.006.02", "ádri-"):
        "RV 7.6.2a. ádreḥ (rock, mountain) agrees with "
        "puraṃdarásya in GEN.SG.M, but it belongs to 'they bring him "
        "from the mountain' in pāda a while puraṃdarásya stands in "
        "pāda c. A coincidence of genitive singular, and the second "
        "demonstration of what the stanza scope costs.",
}
DEITY_HEADING = re.compile(r"hymns to |the Tristubh group|the Pragatha group|"
                           r"Valakhilya", re.I)


def md(m):
    return dict(p.split("=", 1) for p in m.split("|") if "=" in p)


def main():
    ml = json.load(open(CLONE + "/info/matched_lemmata.json", encoding="utf-8"))
    gl = {}
    for _, v in ml.items():
        l, m = v.get("lemma"), v.get("meaning")
        if l and m:
            gl.setdefault(l, set()).add(m)

    def glosses(l):
        return sorted(gl.get(l, []))

    def in_field(l, key):
        gs = glosses(l)
        if not gs:
            return False
        keep = [USAGE_NOTE.sub("", g) for g in gs
                if not EPITHET.search(g) and not PRAISE.search(g)
                and not OWNER.search(g)]
        return any(FIELD[key].search(g) for g in keep)

    data = json.load(open(SRC, encoding="utf-8"))
    rows = []
    for r in data:
        toks = r["tokens"]
        lem = {t["lemma"] for t in toks}

        tight, loose, wide = [], [], []
        excluded = []
        for ft in r["family"]:
            fm = md(ft["morph"])
            if not {"case", "gender", "number"} <= set(fm):
                continue
            for t in toks:
                if t["pada"] == ft["pada"] and t["tok_i"] == ft["tok_i"]:
                    continue
                if t["gramm"] != "nominal stem":
                    continue
                tm = md(t["morph"])
                if not {"case", "gender", "number"} <= set(tm):
                    continue
                if (tm["case"], tm["gender"], tm["number"]) != \
                   (fm["case"], fm["gender"], fm["number"]):
                    continue
                item = "%s (%s)" % (t["surface"], t["lemma"])
                if (r["stanza"], t["lemma"]) in NOT_A_DESCRIPTOR:
                    note = "%s — %s" % (item,
                                        NOT_A_DESCRIPTOR[(r["stanza"], t["lemma"])])
                    if note not in excluded:
                        excluded.append(note)
                    continue
                if t["pada"] == ft["pada"]:
                    if item not in tight:
                        tight.append(item)
                elif HEM[t["pada"]] == HEM[ft["pada"]]:
                    if item not in loose:
                        loose.append(item)
                elif item not in wide:
                    wide.append(item)

        desc_lemmas = {i.split("(")[1].rstrip(")")
                       for i in tight + loose + wide}
        material = sorted(l for l in desc_lemmas if in_field(l, "material"))

        f = {}
        for key in ("water", "cattle", "treasure", "mountain"):
            f[key] = sorted(l for l in lem if in_field(l, key))

        names = [l for l in lem if any(NAME.search(g) for g in glosses(l))]
        patron, opp = [], []
        for n in sorted(names):
            gs = " ".join(glosses(n))
            if PATRON_DECISIVE.search(gs):
                patron.append(n)
            elif OPPONENT_ROLE.search(gs):
                opp.append(n)
            elif PATRON_ROLE.search(gs) and not DEITY_ONLY.search(gs):
                patron.append(n)

        head = r["poet_group"]
        if DEITY_HEADING.search(head):
            poet = ""
            if "hymns to " in head:
                kind, extra = "a deity", ""
            elif "Tristubh" in head:
                kind, extra = "a metre", ""
            elif "Valakhilya" in head:
                kind, extra = "a collection", ""
            else:
                kind = "a strophe-type"
                extra = (" This one is genuinely ambiguous: Pragātha is both a "
                         "strophe-type and a poet's name, and the heading does "
                         "not say which it means. Counted here as NOT a poet "
                         "attribution, which is the conservative reading.")
            basis = ("NOT PRODUCED. Geldner's group heading for this hymn names "
                     "%s rather than a poet: \"%s\".%s Not evidence that the "
                     "hymn is anonymous — the headings are an arrangement, and "
                     "where Geldner arranged by something other than authorship "
                     "he recorded no poet. HOLD-006." % (kind, head, extra))
        else:
            poet = head
            basis = ("Geldner's hymn-group heading (SRC-070), reproduced in "
                     "VedaWeb info/addressees.json. A fact about Geldner's 1951 "
                     "arrangement, which follows the Anukramaṇī tradition, which "
                     "post-dates the text. Three removes from composition. "
                     "PROVISIONAL; HOLD-006.")

        rows.append({
            "passage_id": r["passage_id"], "stanza": r["stanza"],
            "addressee": r["addressee"],
            "poet_lineage": poet,
            "poet_lineage_basis": basis,
            "patron_candidates": "; ".join(patron) or "(none)",
            "opponent_candidates": "; ".join(opp) or "(none)",
            "roles_basis": ("Grassmann's classification of the NAME, from his own "
                            "gloss, not a reading of this passage's syntax. A name "
                            "can occur in a passage without holding or attacking "
                            "anything in it."),
            "description_same_pada": " ".join(tight) or "(none)",
            "description_same_hemistich": " ".join(loose) or "(none)",
            "description_elsewhere_in_stanza": " ".join(wide) or "(none)",
            "agreeing_but_excluded": " ; ".join(excluded) or "(none)",
            "material": "; ".join(material) or "(none)",
            "water": "; ".join(f["water"]) or "(none)",
            "cattle": "; ".join(f["cattle"]) or "(none)",
            "treasure": "; ".join(f["treasure"]) or "(none)",
            "mountain": "; ".join(f["mountain"]) or "(none)",
            "river_lemma_present": "; ".join(sorted(
                l for l in lem if l in {"síndhu-", "sárasvatī-", "sárasvant-",
                                        "rasā́-", "vipā́ś-", "śutudrī́-",
                                        "yamúnā-", "gáṅgā-", "paruṣṇī́-",
                                        "asiknī́-", "gomatī́-", "kúbhā-",
                                        "krúmu-", "sarayú-", "suvā́stu-",
                                        "marudvŕ̥dhā-", "ārjīkī́ya-"})) or "(none)",
            "river_lemma_note": (
                "Presence of a lemma that CAN name a river, not a named river. "
                "síndhu- is glossed by Grassmann as 'Fluss, Strom; der Indus' — "
                "common noun and proper name at once — and Griffith and Geldner "
                "read it differently across these passages. See PUR4J-028."),
            "proposed_geography": "NOT FILLED — no source",
            "geography_basis": ("The pinned corpus carries no geographic content: "
                                "info/rv_locations.tsv is a citation-format "
                                "conversion table. This field needs a source this "
                                "unit does not have, and it is bounded by the "
                                "research hold at Version 12 line 1175 against "
                                "identifying the forts with one archaeological "
                                "culture."),
            "arnold_stratum": (r["stratum_codes"][0] if r["stratum_codes"] else ""),
            "source_id": "SRC-069; SRC-020; SRC-022; SRC-026; SRC-070",
            "retrieval_date": "2026-09-07",
            "supports_page": "forts (proposed)",
        })

    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()),
                           quoting=csv.QUOTE_ALL)
        w.writeheader(); w.writerows(rows)

    def filled(k):
        return sum(1 for x in rows if x[k] not in ("(none)", ""))
    print("passages: %d" % len(rows), file=sys.stderr)
    for k in ("poet_lineage", "patron_candidates", "opponent_candidates",
              "description_same_pada", "description_same_hemistich",
              "description_elsewhere_in_stanza", "agreeing_but_excluded", "material",
              "water", "cattle", "treasure", "mountain", "river_lemma_present"):
        print("  %-28s filled in %3d of %d" % (k, filled(k), len(rows)),
              file=sys.stderr)
    mat = collections.Counter()
    for x in rows:
        for l in x["material"].split():
            mat[l] += 1
    print("  material lemmas: %s" % dict(mat), file=sys.stderr)
    print("-> %s" % OUT, file=sys.stderr)


if __name__ == "__main__":
    main()
