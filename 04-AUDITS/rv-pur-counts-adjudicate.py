#!/usr/bin/env python3
"""
rv-pur-counts-adjudicate.py — emit 03-REGISTERS/rigveda-pur-counts.csv.

Takes the mechanical attachment test (rv-pur-counts.py) and adds, per numeral
token, a hand verdict on whether the numeral counts a púr- or counts something
else in the same stanza. The mechanical instruments are carried through
unchanged in their own columns so a reader can see where the verdict agrees
with them and where it overrides them.

VERDICTS
  COUNTS-PUR        the numeral counts the fort word
  COUNTS-OTHER      the numeral counts something else in the stanza
  CANNOT-DECIDE     the text does not settle it

Every verdict carries its basis in the row. Where a verdict overrides an
instrument, the row says which instrument and why.
"""
import csv, sys

IN = sys.argv[1] if len(sys.argv) > 1 else "rv_pur_counts.tsv"
OUT = sys.argv[2] if len(sys.argv) > 2 else \
    "/home/user/research/03-REGISTERS/rigveda-pur-counts.csv"

# key: (stanza, numeral_pada, numeral_surface)
# value: (verdict, counts_of, expression, basis)
A = {
 # ---- counts of forts -------------------------------------------------------
 ("01.053.08","c","śatā́"): ("COUNTS-PUR","100","śatā́ … púraḥ",
   "c: 'tváṁ śatā́ váṅgr̥dasyābhinat púro' — śatā́ (n.pl.) and púraḥ in one clause, "
   "váṅgr̥dasya genitive. Griffith, Geldner and Grassmann all render 'the hundred forts of Vaṅgṛda'."),
 ("01.054.06","d","navatím"): ("COUNTS-PUR","99","púro navatíṁ … náva",
   "d: 'tvám púro navatíṁ dambhayo náva'. navatím and náva are split around the verb; "
   "all three full translators read 99, not 90 and 9 separately."),
 ("01.054.06","d","náva"): ("COUNTS-PUR","99","púro navatíṁ … náva","Second half of the same 99 expression; not a separate count."),
 ("01.063.07","a","saptá"): ("COUNTS-PUR","7","saptá … púraḥ",
   "a-b: 'tváṁ ha tyád indra saptá yúdhyan / púro vajrin purukútsāya dardaḥ'. saptá ACC.PL agrees with púraḥ."),
 ("01.130.07","a","navatím"): ("COUNTS-PUR","90","púro navatím",
   "a: 'bhinát púro navatím indra pūráve'. Adjacent, no náva anywhere in the stanza. "
   "A bare ninety, and one of only two."),
 ("01.174.02","b","saptá"): ("COUNTS-PUR","7","saptá … púraḥ śā́radīḥ",
   "b: 'saptá yát púraḥ śárma śā́radīr dárt'. saptá ACC.PL with púraḥ; śā́radīḥ 'autumnal' agrees with púraḥ."),
 ("02.014.06","a","śatám"): ("COUNTS-PUR","100","śatáṁ śámbarasya púraḥ",
   "a-b: 'yáḥ śatáṁ śámbarasya / púro bibhéda'. The pāda-a śatám governs púraḥ across the pāda break."),
 ("02.019.06","c","navatím"): ("COUNTS-PUR","99","navatíṁ ca náva … púraḥ śámbarasya",
   "c-d: 'dívodāsāya navatíṁ ca náva / índraḥ púro vy àirac chámbarasya'. ca joins the two numerals."),
 ("02.019.06","c","náva"): ("COUNTS-PUR","99","navatíṁ ca náva … púraḥ","Second half of the same expression."),
 ("03.012.06","a","navatím"): ("COUNTS-PUR","90","navatím púro dāsápatnīḥ",
   "a: 'índrāgnī navatím púro'. Adjacent; no náva in the stanza. The second bare ninety."),
 ("04.026.03","b","navatī́ḥ"): ("COUNTS-PUR","99","náva … navatī́ḥ śámbarasya",
   "a: 'ahám púro … náva sākáṁ navatī́ḥ śámbarasya'. navatī́ḥ is ACC.PL.F here and agrees with "
   "púraḥ FULLY in case, gender and number — the only such agreement in the corpus."),
 ("04.026.03","b","náva"): ("COUNTS-PUR","99","náva … navatī́ḥ","Second half of the same expression."),
 ("04.027.01","c","śatám"): ("COUNTS-PUR","100","śatám … púra ā́yasīḥ",
   "c: 'śatám mā púra ā́yasīr arakṣann'. The forts CONFINE the speaker rather than being stormed."),
 ("04.030.20","a","śatám"): ("COUNTS-PUR","100","śatám aśmanmáyīnām purā́m",
   "a-b: 'śatám aśmanmáyīnām / purā́m índro vy àsyat'. Genitive plural purā́m governed by śatám."),
 ("06.020.10","c","saptá"): ("COUNTS-PUR","7","saptá … púraḥ śā́radīḥ",
   "c: 'saptá yát púraḥ śárma śā́radīr dárd'. Near-identical wording to 01.174.02b."),
 ("06.031.04","a","śatā́ni"): ("COUNTS-PUR","100+","śatā́ni … śámbarasya púraḥ",
   "a-b: 'tváṁ śatā́ny áva śámbarasya / púro jaghantha'. śatā́ni is PLURAL 'hundreds', "
   "not 'a hundred' — the passage counts Śambara's forts in hundreds, an unbounded figure."),
 ("06.048.08","c","śatám"): ("COUNTS-PUR","100","śatám pūrbhíḥ",
   "c: 'śatám pūrbhír yaviṣṭha pāhy áṁhasaḥ'. Instrumental: Agni is asked to protect WITH a "
   "hundred forts. The forts are the worshipper's defence, not an enemy's."),
 ("07.003.07","d","śatám"): ("COUNTS-PUR","100","śatám pūrbhír ā́yasībhiḥ",
   "d: 'śatám pūrbhír ā́yasībhir ní pāhi'. Protective, and the forts are ā́yasī- 'of metal'."),
 ("07.016.10","d","śatám"): ("COUNTS-PUR","100","śatám pūrbhíḥ",
   "d: 'partŕ̥bhiṣ ṭváṁ śatám pūrbhír yaviṣṭhya'. Protective."),
 ("07.018.13","b","saptá"): ("COUNTS-PUR","7","púraḥ … saptá",
   "b: 'índraḥ púraḥ sáhasā saptá dardaḥ'. Adjacent, ACC.PL."),
 ("07.019.05","b","navatím"): ("COUNTS-PUR","99","náva … púro navatíṁ ca",
   "b: 'náva yát púro navatíṁ ca sadyáḥ'. ca joins the numerals around púraḥ."),
 ("07.019.05","b","náva"): ("COUNTS-PUR","99","náva … púro navatíṁ ca","Second half of the same expression."),
 ("07.099.05","b","navatím"): ("COUNTS-PUR","99","náva púro navatíṁ ca śámbarasya",
   "b: 'náva púro navatíṁ ca śnathiṣṭam', with śámbarasya in pāda a."),
 ("07.099.05","b","náva"): ("COUNTS-PUR","99","náva púro navatíṁ ca","Second half of the same expression."),
 ("08.093.02","a","navatím"): ("COUNTS-PUR","99","náva … navatím púraḥ",
   "a: 'náva yó navatím púro bibhéda'. All three numeral words and púraḥ in one pāda."),
 ("08.093.02","a","náva"): ("COUNTS-PUR","99","náva … navatím púraḥ","Second half of the same expression."),
 ("09.048.02","c","śatám"): ("COUNTS-PUR","100","śatám púraḥ",
   "c: 'śatám púro rurukṣáṇim'. Of Soma, not Indra: 'wishing to break a hundred forts'."),

 # ---- ordinals: the hundredth that completes a ninety-nine ------------------
 ("04.026.03","c","śatatamám"): ("COUNTS-PUR","100th","śatatamáṁ veśyàm",
   "c: 'śatatamáṁ veśyàṁ sarvátātā'. An ORDINAL completing the 99 of pāda a, and it is applied to "
   "veśyà- (dwelling/inhabitant), not to púr-. Recorded as a count because it is the 100th of the "
   "same series; the noun it modifies is not the fort word."),
 ("07.019.05","c","śatatamā́"): ("COUNTS-PUR","100th","nivéśane śatatamā́",
   "c: 'nivéśane śatatamā́viveṣīr'. Same schema as 04.026.03c: 99 in pāda b, the hundredth in pāda c, "
   "again on a dwelling word (nivéśana-) rather than on púr-."),

 # ---- counts of something else ---------------------------------------------
 ("01.102.07","a","śatā́t"): ("COUNTS-OTHER","-","śatā́t … sahásrāt (of śrávas 'glory')",
   "a: 'út te śatā́n maghavann úc ca bhū́yasa út sahásrād ririce … śrávaḥ'. The hundred and the "
   "thousand are what Indra's GLORY exceeds. puraṁdara in pāda d is a vocative epithet with no numeral."),
 ("01.102.07","b","sahásrāt"): ("COUNTS-OTHER","-","śatā́t … sahásrāt (of śrávas)","As above."),
 ("02.014.06","c","śatám"): ("COUNTS-OTHER","-","śatáṁ … sahásram (of varcín's men)",
   "c: 'yó varcínaḥ śatám índraḥ sahásram'. A SECOND hundred in the same stanza, counting Varcin's "
   "men. A stanza-level co-occurrence count reads this as evidence for 'hundred forts'; it is not."),
 ("02.014.06","c","sahásram"): ("COUNTS-OTHER","-","śatáṁ … sahásram (of varcín's men)","As above."),
 ("03.034.01","d","ubhé"): ("COUNTS-OTHER","-","ubhé ródasī 'both worlds'",
   "d: 'ā́pr̥ṇad ródasī ubhé'. A dual quantifier on the two world-halves. pūrbhíd in pāda a is an epithet."),
 ("03.054.15","b","ubhé"): ("COUNTS-OTHER","-","ubhé ródasī 'both worlds'",
   "b: 'ubhé ā́ paprau ródasī mahitvā́'. As above; puraṁdaráḥ in pāda c is an epithet."),
 ("03.012.06","c","ékena"): ("COUNTS-OTHER","-","ékena kármaṇā 'with one deed'",
   "c: 'sākám ékena kármaṇā'. Instrumental singular with kárman-. The ninety of pāda a is the fort count."),
 ("04.016.13","c","pañcāśát"): ("COUNTS-OTHER","-","pañcāśát … sahásrā kr̥ṣṇā́ḥ '50,000 black ones'",
   "c: 'pañcāśát kr̥ṣṇā́ ní vapaḥ sahásrā'. Griffith 'fifty thousand', Geldner 'Fünfzigtausend Schwarze'. "
   "púraḥ in pāda d is uncounted: 'átkaṁ ná púro jarimā́ ví dardaḥ', torn like a garment."),
 ("04.016.13","c","sahásrā"): ("COUNTS-OTHER","-","pañcāśát … sahásrā kr̥ṣṇā́ḥ","As above."),
 ("07.099.05","c","śatám"): ("COUNTS-OTHER","-","śatáṁ … sahásraṁ varcínaḥ",
   "c: 'śatáṁ varcínaḥ sahásraṁ ca sākáṁ'. Varcin's men, in the very stanza whose pāda b states 99 forts. "
   "The clearest demonstration that stanza co-occurrence is not attachment."),
 ("07.099.05","c","sahásram"): ("COUNTS-OTHER","-","śatáṁ … sahásraṁ varcínaḥ","As above."),
 ("06.048.08","d","śatám"): ("COUNTS-OTHER","-","śatáṁ hímāḥ 'a hundred winters'",
   "d: 'sameddhā́raṁ śatáṁ hímā'. A SECOND hundred in the same stanza, counting winters — a "
   "lifespan formula. Pāda c's hundred is the fort count."),
 ("07.026.03","c","ékaḥ"): ("COUNTS-OTHER","-","pátir ékaḥ 'one husband' (simile)",
   "c: 'jánīr iva pátir ékaḥ samānó'. Inside the simile. The forts in pāda d are sárvāḥ 'all', uncounted."),
 ("08.033.05","c","sahásrā"): ("COUNTS-OTHER","-","sahásrā … śatā́magha (of Indra's gifts)",
   "c: 'yá ākaráḥ sahásrā yáḥ śatā́magha'. Indra's giving. pūrbhíd in pāda d is an epithet with no numeral."),
 ("08.061.08","a","sahásrāṇi"): ("COUNTS-OTHER","-","sahásrāṇi śatā́ni yūthā́ 'thousands and hundreds of herds'",
   "a: 'tvám purū́ sahásrāṇi śatā́ni ca yūthā́ dānā́ya'. Cattle, not forts. puraṁdarám in pāda c is an epithet."),
 ("08.061.08","a","śatā́ni"): ("COUNTS-OTHER","-","sahásrāṇi śatā́ni yūthā́","As above."),
 ("10.067.05","b","trī́ṇi"): ("COUNTS-OTHER","-","nís trī́ṇi … udadhér 'three from the sea'",
   "b: 'nís trī́ṇi sākám udadhér akr̥ntat'. Geldner 'erlöste er auf einmal die Drei aus dem Meere'; the three "
   "are enumerated in pāda c as dawn, sun and cow. púram in pāda a is singular and uncounted."),
 ("10.104.08","a","saptá"): ("COUNTS-OTHER","-","saptá ā́paḥ 'seven waters'",
   "a: 'saptā́po devī́ḥ suráṇā ámr̥ktā'. Waters, not forts."),
 ("10.104.08","c","navatím"): ("COUNTS-OTHER","-","navatíṁ … náva ca srávantīḥ '99 flowing streams'",
   "c: 'navatíṁ srotyā́ náva ca srávantīr'. THE CONTROL CASE. The identical náva…navatí- expression, "
   "in the identical ACC.SG.F construction, counting RIVERS. Griffith 'nine-and-ninety flowing streams', "
   "Geldner 'die neunundneunzig fließenden Ströme', Grassmann 'Die neunundneunzig Flüsse'. All three agree. "
   "pūrbhít in pāda b is a vocative-position epithet of Indra and takes no numeral."),
 ("10.104.08","c","náva"): ("COUNTS-OTHER","-","navatíṁ … náva ca srávantīḥ","Second half of the 99-rivers expression."),
}


def main():
    rows = list(csv.DictReader(open(IN, encoding="utf-8"), delimiter="\t"))
    out, missing = [], []
    for r in rows:
        key = (r["stanza"], r["numeral_pada"], r["numeral_surface"])
        if key not in A:
            missing.append(key); continue
        verdict, of, expr, basis = A[key]
        override = ""
        mech_says_attached = (r["agreement"].startswith("FULL")
                              or r["proximity"] == "same-pada")
        if verdict == "COUNTS-OTHER" and mech_says_attached:
            override = ("Verdict overrides the mechanical instruments: "
                        "agreement=%s, proximity=%s would place this numeral on the fort word."
                        % (r["agreement"], r["proximity"]))
        if verdict == "COUNTS-PUR" and not mech_says_attached:
            override = ("Verdict is reached against the instruments: agreement=%s, "
                        "proximity=%s. navatí- is a FEMININE SINGULAR collective ('a ninety') "
                        "governing a plural noun, so it agrees in case and gender but never in "
                        "number; a number-agreement test therefore under-reports it by "
                        "construction." % (r["agreement"], r["proximity"]))
        out.append({
            "count_id": "PUR-N-%03d" % (len(out) + 1),
            "passage_id": r["passage_id"], "stanza": r["stanza"],
            "numeral_lemma": r["numeral_lemma"],
            "numeral_surface": r["numeral_surface"],
            "numeral_pada": r["numeral_pada"],
            "numeral_morph": r["numeral_morph"],
            "grassmann_gloss": r["grassmann_gloss"],
            "verdict": verdict,
            "count_of_forts": of if verdict == "COUNTS-PUR" else "",
            "expression": expr,
            "nearest_pur_surface": r["pur_surface"],
            "nearest_pur_pada": r["pur_pada"],
            "nearest_pur_morph": r["pur_morph"],
            "instrument_agreement": r["agreement"],
            "instrument_agreement_keys": r["agreement_keys_compared"],
            "instrument_proximity": r["proximity"],
            "instrument_translators": r["translators_attaching"],
            "instrument_translators_n": "%s/%s" % (
                r["n_translators_attaching"], r["n_translators_available"]),
            "verdict_basis": basis,
            "instrument_override": override,
            "status": "VERIFIED",
            "source_id": "SRC-069; SRC-020; SRC-021; SRC-022; SRC-072; SRC-073; SRC-074",
            "locator": "RV %s pāda %s, token %s; Aufrecht and padapāṭha at that stanza; "
                       "Griffith, Geldner and Grassmann at that stanza"
                       % (r["stanza"], r["numeral_pada"], r["numeral_surface"]),
            "retrieval_date": "2026-09-07",
            "supports_page": "forts (proposed)",
        })
    if missing:
        print("UNADJUDICATED: %s" % missing, file=sys.stderr); sys.exit(1)

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()),
                           quoting=csv.QUOTE_ALL)
        w.writeheader(); w.writerows(out)
    print("%d numeral rows -> %s" % (len(out), OUT), file=sys.stderr)


if __name__ == "__main__":
    main()
