#!/usr/bin/env python3
"""
rv-pur-typology.py — emit 03-REGISTERS/rigveda-pur-typology.csv, classifying
every one of the 103 passages against constitution §4J's five-way typology:

    textual stronghold · poetic formula · inferred geography ·
    archaeological fortification · unsupported identification

THE STRUCTURAL FINDING, WHICH DECIDES HOW THIS REGISTER IS SHAPED

The five types are not five values of one variable. Two of them are properties
of the TEXT and three are properties of CLAIMS MADE ABOUT the text:

  textual stronghold  — the passage presents a púr as an object in its own
                        narrative world. Decidable from the text.
  poetic formula      — the púr is figurative: a divine epithet, a simile, a
                        metaphor, a formulaic protective request. Decidable
                        from the text.
  inferred geography  — someone has placed the fort somewhere.
  archaeological fortification
                      — someone has matched the passage to an excavated site.
  unsupported identification
                      — someone has made an identification the evidence does
                        not carry.

The last three cannot be read off a Rigvedic stanza in any state of knowledge,
because none of them is about the stanza. They are verdicts on an argument that
someone else has to make first. This unit has no geographic source (the pinned
corpus has none — PUR4J-018) and no archaeological source, so **no passage is
assigned any of the three**, and the columns record why rather than standing
empty and unexplained.

Assigning them anyway would be the failure §4J's typology exists to prevent:
it is exactly the move by which a textual stronghold silently becomes an
archaeological one.

THE TWO TEXT-DECIDABLE TYPES

  TEXTUAL-STRONGHOLD  a púr is an object in the narrative: held, broken,
                      entered, or belonging to a named holder.
  POETIC-FORMULA      the púr is figurative — one of four sub-kinds recorded
                      separately: DIVINE-EPITHET, SIMILE, METAPHOR,
                      PROTECTIVE-FORMULA.
  BOTH                the text supports both readings at once. §4J says
                      "distinguish", not "choose": a stronghold described in
                      formulaic language is both, and forcing one label would
                      destroy the distinction the section asks for.
  CANNOT-CLASSIFY     the text does not decide. Recorded as such rather than
                      resolved to the likelier type.

Rules are applied first, then a hand-override table corrects the cases the
rules get wrong. Every row carries which rule fired and, where an override
applied, why.
"""
import csv, json, sys, collections

SRC = sys.argv[1] if len(sys.argv) > 1 else "rv_pur_passages.json"
OUT = sys.argv[2] if len(sys.argv) > 2 else \
    "/home/user/research/03-REGISTERS/rigveda-pur-typology.csv"

EPITHET_LEMMAS = {"puraṃdará-", "pūrbhíd-", "pūrbhíttama-", "purohán-",
                  "pūrbhídya-", "pū́rpati-"}

# Passages where a simile particle ná stands in the same pāda as a púr- token
# AND the simile is ON the fort word. Hand-checked against Griffith, Geldner
# and Grassmann one by one, because the particle is common and attaches freely.
SIMILE_ON_PUR = {
    "01.174.08": "bhinát púro ná bhído ádevīr — the godless are crushed LIKE forts.",
    "05.041.12": "ā́paḥ púro ná śubhrā́ḥ — the waters are bright LIKE forts.",
    "08.006.23": "púraṁ ná darṣi gómatīm — open food for us LIKE a fort rich in cattle.",
    "08.032.05": "púraṁ ná śūra darṣasi — burst the cattle-stall LIKE a fort.",
    "08.069.08": "púraṁ ná dhr̥ṣṇv àrcata — praise him, bold, LIKE a fort.",
    "08.073.18": "púraṁ ná dhr̥ṣṇav ā́ ruja — break it down LIKE a fort.",
    "09.107.10": "jáno ná purí camvòr viśad — Soma enters the bowls as a man a fort. "
                 "One of only three locative tokens in the corpus, and it is inside a simile.",
    "06.002.07": "raṇváḥ purī́va jū́ryaḥ — 'welcome like an old man in a fort'. The "
                 "simile particle here is iva, not ná, so the ná rule missed it. Of the "
                 "three passages with iva in a púr- pāda, this is the only one where it "
                 "modifies the fort word: at RV 2.14.6 it is áśmaneva 'as with a stone' "
                 "and at RV 10.138.4 māséva 'like the moon'. A second locative inside a "
                 "simile, leaving RV 2.35.6 as the corpus's only unfigured locative.",
}
# ná in the same pāda but NOT modifying the fort word. Recorded so the rule's
# false-positive rate is visible: 3 of 10.
NA_NOT_ON_PUR = {
    "04.016.13": "átkaṁ ná púro jarimā́ ví dardaḥ — the simile is 'like a garment', "
                 "átkaṁ ná; púraḥ is the object torn.",
    "06.020.07": "ví pípror … dr̥ḷhā́ḥ púro … śávasā ná dardaḥ — ná goes with śávasā. "
                 "Griffith and Geldner both read Pipru's firm forts as real objects.",
    "10.089.07": "rurója púro áradan ná síndhūn — ná goes with síndhūn, the rivers.",
}
# PERIPHRASTIC EPITHETS. The lexicalised epithets (puraṃdará- and kin) are
# caught by rule R1. But the corpus also builds the same epithet analytically,
# with a genitive plural purā́m depending on an agent noun of breaking, and R1
# cannot see those: they are simplex púr- tokens in the genitive. Found by
# stress-testing R5 — asking which TEXTUAL-STRONGHOLD passages have neither a
# breaking root nor a named opponent — and reading all ten genitive-plural
# passages. Nine of the ten are this; the tenth (RV 4.30.20) is a genuine
# object, where purā́m is governed by śatám "a hundred".
PERIPHRASTIC_EPITHET = {
    "01.011.04": "purā́m bhindúr — 'breaker of forts', of Indra.",
    "01.061.05": "purā́ṁ … darmā́ṇam — 'splitter of forts', of Indra.",
    "01.130.10": "púrāṁ dartaḥ — 'O splitter of forts', vocative.",
    "03.045.02": "purā́ṁ darmó — 'splitter of forts'.",
    "06.020.03": "puráaṁ dartnúm — 'fort-splitting', of the bolt.",
    "08.017.14": "bhettā́ puráaṁ śáśvatīnām — 'breaker of all forts', of the Soma drop.",
    "08.098.06": "índra dartā́ purā́m ási — 'thou art the splitter of forts'.",
    "10.046.05": "purā́ṁ darmā́ṇam — 'splitter of forts'.",
}

# Passages where a púr IS a god or a river, or is asked to be one.
METAPHOR = {
    "07.015.14": "pū́r bhavā śatábhujiḥ — Agni is ASKED TO BE a hundredfold iron púr.",
    "07.095.01": "sárasvatī dharúṇam ā́yasī pū́ḥ — the river Sarasvatī IS an iron púr.",
    "01.189.02": "pū́ś ca pr̥thvī́ bahulā́ na urvī́ bhávā — Agni asked to BE a broad, "
                 "ample, wide púr.",
    "07.052.01": "pū́r devatrā́ vasavo martyatrā́ — a púr among gods and among mortals, "
                 "asked of the Ādityas and Vasus.",
    "08.080.07": "índra dŕ̥hyasva pū́r asi — 'Indra, be firm: thou ART a púr.'",
    "10.087.22": "pári tvāgne púraṁ vayáṁ … dhīmahi — 'we set thee, Agni, "
                 "around us as a púr'. Griffith 'We set thee round us as a "
                 "fort'; Geldner 'Als einen Burgwall wollen wir dich … um "
                 "(uns) legen'. The same figure as RV 7.15.14 and 1.189.2, and "
                 "missed by the first run for the same reason those two nearly "
                 "were: the fort word is an accusative predicate, so the case "
                 "test in R5 claims it.",
}
# Instrumental púr in a request for protection: "guard us WITH a hundred forts".
PROTECTIVE = {
    "01.058.08": "pūrbhír ā́yasībhiḥ … uruṣya — protect the singer with iron forts.",
    "01.166.08": "śatábhujibhis … pūrbhī́ rakṣatā maruto — Maruts guard with "
                 "hundredfold forts.",
    "06.048.08": "śatám pūrbhír yaviṣṭha pāhy áṁhasaḥ — guard with a hundred forts.",
    "07.003.07": "śatám pūrbhír ā́yasībhir ní pāhi — guard us with a hundred iron forts.",
    "07.016.10": "partŕ̥bhiṣ ṭváṁ śatám pūrbhír yaviṣṭhya — guard them with a "
                 "hundred forts.",
}
# Hand overrides of the rule output, each with its reason.
OVERRIDE = {
    "04.027.01": ("BOTH",
        "A hundred metal forts CONFINE the speaking eagle. The púr is an object "
        "with a stated count and material, so it is a textual stronghold; but "
        "the speaker is a bird in a myth of Soma's theft, so it is not a "
        "stronghold in a human landscape either. Both, and neither alone."),
    "08.100.08": ("BOTH",
        "The falcon escapes the metal fort — the same myth as RV 4.27.1, from "
        "the other side. Same reasoning."),
    "10.101.08": ("BOTH",
        "'púraḥ kr̥ṇudhvam ā́yasīr ádhr̥ṣṭā' — priests are told to MAKE "
        "unassailable metal forts, in a list beside stitching armour and "
        "building a cattle-pen. Either a ritual figure for the works of the "
        "sacrifice, or an instruction about actual construction. The text "
        "carries both and settles neither."),
    "01.149.03": ("CANNOT-CLASSIFY",
        "'púraṁ nā́rmiṇīm'. If nā́rmiṇī- is a proper name (Geldner: 'die Burg "
        "Nārmiṇī') this is the only named fort in the corpus and a textual "
        "stronghold. If it is an adjective (Griffith: 'the joyous castle') it "
        "is a formulaic epithet. Grassmann's gloss declines to choose. The "
        "classification turns entirely on a disputed word class."),
    "02.035.06": ("CANNOT-CLASSIFY",
        "'āmā́su pūrṣú paró apramr̥ṣyám' — in the raw/unbaked forts, malice does "
        "not reach him. A locative, so someone is in it; but the subject is "
        "Apāṃ Napāt, a divine figure in the waters, so whether the púr is a "
        "place or a figure of inaccessibility is undecided by the text."),
    "08.001.28": ("CANNOT-CLASSIFY",
        "'púraṁ cariṣṇvàṁ … śúṣṇasya' — Śuṣṇa's MOVING fort. cariṣṇú- is not "
        "compatible with a fixed fortification, and no other reading is "
        "supplied by the passage. The one passage whose descriptor rules out "
        "the ordinary sense without supplying a replacement."),
    "05.066.04": ("CANNOT-CLASSIFY",
        "'dákṣasya pūrbhíḥ' — instrumental plural in an abstract clause about "
        "Mitra and Varuṇa. Geldner reads 'mit den Burgen des Verstandes', the "
        "forts OF UNDERSTANDING, which is a metaphor; Grassmann renders the "
        "phrase without a fort word at all ('in Geistes Fülle'); Griffith's "
        "line is garbled. Three translators, three different things. The text "
        "does not decide, and no majority is available to lean on."),
    "10.138.04": ("CANNOT-CLASSIFY",
        "'vásu púryam ā́ dade' — púrya- is an ADJECTIVE, ACC.N.SG, modifying "
        "vásu 'wealth': the fort-wealth, Geldner's 'Burggut'. The stanza's "
        "objects are the wealth and the ánādhr̥ṣṭāni, the unassailable ones, "
        "which the translators supply as forts. So a púr is implied by a "
        "derived adjective and never named. Whether the passage presents a "
        "stronghold or uses a stronghold-adjective for plunder is not "
        "decidable from it."),
    "01.173.10": ("POETIC-FORMULA", "SIMILE",
        "pū́rpati- 'lord of a púr' inside a simile: petitioners approach Indra "
        "as men approach a fort-lord. The office is the vehicle of the simile, "
        "not a fact asserted about a fort. Griffith's single 'city' in 103 "
        "passages falls here — see 06-BRIEFS/pur-translation-standard.md §8."),
}


def md(m):
    return dict(p.split("=", 1) for p in m.split("|") if "=" in p)


def main():
    data = json.load(open(SRC, encoding="utf-8"))
    rows = []
    for r in data:
        s = r["stanza"]
        fams = r["family"]
        cases = {md(t["morph"]).get("case") for t in fams if t["lemma"] == "púr-"}
        sub, rule = "", ""

        if all(t["lemma"] in EPITHET_LEMMAS for t in fams):
            typ, sub, rule = "POETIC-FORMULA", "DIVINE-EPITHET", \
                "R1: every family token is a derivative epithet " \
                "(puraṃdará- 'fort-breaker' and kin). No fort is present as an " \
                "object; the fort word is a component of a divine title."
        elif s in SIMILE_ON_PUR:
            typ, sub, rule = "POETIC-FORMULA", "SIMILE", "R2: " + SIMILE_ON_PUR[s]
        elif s in METAPHOR:
            typ, sub, rule = "POETIC-FORMULA", "METAPHOR", "R3: " + METAPHOR[s]
        elif s in PROTECTIVE:
            typ, sub, rule = "POETIC-FORMULA", "PROTECTIVE-FORMULA", \
                "R4: " + PROTECTIVE[s]
        elif s in PERIPHRASTIC_EPITHET:
            typ, sub, rule = "POETIC-FORMULA", "DIVINE-EPITHET", \
                "R4b: genitive plural purā́m depending on an agent noun of " \
                "breaking — the analytic form of the puraṃdará- epithet, which " \
                "R1 cannot see because the token is a simplex púr-. " \
                + PERIPHRASTIC_EPITHET[s]
        elif cases & {"ACC", "GEN", "LOC", "NOM"}:
            typ, rule = "TEXTUAL-STRONGHOLD", \
                "R5: a púr- in %s stands as an object in the narrative — held, " \
                "broken, entered, or belonging to a named holder." % \
                "/".join(sorted(c for c in cases if c))
        else:
            typ, rule = "CANNOT-CLASSIFY", \
                "R6: no rule fired. Case set %s." % sorted(c for c in cases if c)

        rule_typ = typ
        override = ""
        if s in OVERRIDE:
            entry = OVERRIDE[s]
            newsub = ""
            if len(entry) == 3:
                newtyp, newsub, why = entry
            else:
                newtyp, why = entry
            override = "Rule output %s%s overridden to %s%s. %s" % (
                typ, "/" + sub if sub else "", newtyp,
                "/" + newsub if newsub else "", why)
            typ = newtyp
            # The sub-kind must follow the override, not survive it. Before this
            # was fixed, the RV 1.173.10 override reclassified the passage as a
            # SIMILE while poetic_subkind kept DIVINE-EPITHET from rule R1, so
            # the override cell and the sub-kind cell said different things and
            # the published sub-kind counts were off by one.
            sub = newsub if newtyp == "POETIC-FORMULA" else ""

        rows.append({
            "passage_id": r["passage_id"], "stanza": s,
            "type": typ,
            "type_before_override": rule_typ,
            "type_means": (
                "TEXTUAL-STRONGHOLD means the TEXT presents a fort as an object "
                "in its own narrative world. It is NOT a claim that any fort "
                "existed, was fortified, or can be located: that would be the "
                "archaeological type, which is not assigned here. A passage can "
                "be a textual stronghold and still state a formulaic count — "
                "the counts are a separate register for that reason."),
            "poetic_subkind": sub,
            "basis": rule,
            "override": override,
            "inferred_geography": "NOT ASSIGNED",
            "archaeological_fortification": "NOT ASSIGNED",
            "unsupported_identification": "NOT ASSIGNED",
            "why_three_types_unassigned":
                "These three of §4J's five types are not properties of the "
                "passage. Each is a verdict on an argument someone else must "
                "make first — a placement, a site match, an identification. "
                "This unit has no geographic source (the pinned corpus carries "
                "none, PUR4J-018) and no archaeological source, so none is "
                "assigned to any passage. Assigning one anyway is precisely how "
                "a textual stronghold becomes an archaeological one.",
            "family_surfaces": " ".join(t["surface"] for t in fams),
            "addressee": r["addressee"],
            "arnold_stratum": r["stratum_codes"][0] if r["stratum_codes"] else "",
            "status": "PROVISIONAL",
            "source_id": "SRC-069; SRC-020; SRC-022; SRC-072; SRC-073; SRC-074",
            "locator": "RV %s; Aufrecht and padapāṭha at that stanza; Griffith, "
                       "Geldner and Grassmann at that stanza" % s,
            "retrieval_date": "2026-09-07",
            "supports_page": "forts (proposed)",
        })

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()),
                           quoting=csv.QUOTE_ALL)
        w.writeheader(); w.writerows(rows)

    print("passages: %d" % len(rows), file=sys.stderr)
    for k, n in collections.Counter(x["type"] for x in rows).most_common():
        print("  %-22s %3d" % (k, n), file=sys.stderr)
    print("  poetic sub-kinds: %s" % dict(collections.Counter(
        x["poetic_subkind"] for x in rows if x["poetic_subkind"])), file=sys.stderr)
    print("  overrides applied: %d" % sum(1 for x in rows if x["override"]),
          file=sys.stderr)
    print("  WITHOUT any hand override: %s" % dict(collections.Counter(
        x["type_before_override"] for x in rows)), file=sys.stderr)
    print("  simile particle in a púr- pāda but NOT modifying the fort word, "
          "hand-excluded: 3 of 10 for ná, 2 of 3 for iva", file=sys.stderr)
    print("-> %s" % OUT, file=sys.stderr)


if __name__ == "__main__":
    main()
