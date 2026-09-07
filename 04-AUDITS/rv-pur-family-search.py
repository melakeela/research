#!/usr/bin/env python3
"""
pur-family search over the VedaWeb Zurich lemma layer, with Arnold strata.
Input: rv_tokens_vedaweb.tsv (from 04-AUDITS/rv-token-extract.py)
"""
import csv, collections, sys, math

FAMILY = {  # Grassmann lemma id -> (lemma, gloss, why it is in the family)
 'lemma_pur_5549':     ('púr-',         'Wall aus Steinen und Lehm, Verschanzung, Palisade', 'simplex'),
 'lemma_puraMdara_5552':('puraṃdará-',  'Zerstörer der Wälle (meist von Indra gesagt)',      'compound púr- + √dr̥̄'),
 'lemma_pUrBid_5700':  ('pūrbhíd-',     'die Wälle aufbrechend',                              'compound púr- + √bhid; includes the superlative pūrbhíttama-'),
 'lemma_pUrBidya_5701':('pūrbhídya-',   'das Aufbrechen der Wälle',                           'derivative of pūrbhíd-'),
 'lemma_pUrpati_5699': ('pū́rpati-',    'Herr der Burg',                                      'compound púr- + páti-'),
 'lemma_purohan_5658': ('purohán-',     'die Wälle zerschlagend, zerschmetternd',             'compound; fort reading follows Grassmann'),
 'lemma_purya_5661':   ('púrya-',       'in einem festen Platz befindlich',                   'adjective derived from púr-'),
}
FLAGGED = {  # excluded, but recorded because the exclusion is a judgement
 'lemma_puraMDi_5553':  ('púraṃdhi-',      "etwa: 'Segensfülle, Reichtum'"),
 'lemma_puraMDivat_5554':('púraṃdhivant-', 'von der Segensfülle begleitet'),
 'lemma_smatpuraMDi_10319':('smátpuraṃdhi-','mit Fülle versehen'),
 'lemma_purAsah_5564':  ('purāṣáh-',       'von alters her siegreich'),
}
STRAT = {'A':'Archaic','S':'Strophic','N':'Normal','C':'Cretic','P':'Popular'}

rows = list(csv.DictReader(open(sys.argv[1] if len(sys.argv)>1 else
            'rv_tokens_vedaweb.tsv', encoding='utf-8'), delimiter='\t'))
hits = [r for r in rows if r['lemma_id'] in FAMILY]

def strat_name(code):
    if not code: return ('', '')
    return (STRAT.get(code.upper(), '?'), 'certain' if code.isupper() else 'metrical-variations-only')

print('CORPUS: %d tokens, %d stanzas, %d padas' % (
    len(rows), len(set(r['stanza'] for r in rows)),
    len(set((r['stanza'], r['pada']) for r in rows))))
print('FAMILY TOKENS: %d' % len(hits))
print()

print('=== A. tokens per family lemma ===')
per = collections.Counter(r['lemma_id'] for r in hits)
for lid,(lem,gloss,why) in FAMILY.items():
    print('%-22s %-14s %3d   %s' % (lid, lem, per[lid], gloss))
print()

print('=== B. counts by Arnold stratum (whole family) ===')
byS = collections.Counter(r['stratum'].upper() for r in hits)
tot = collections.Counter(r['stratum'].upper() for r in rows)
print('%-10s %6s %6s %9s %9s' % ('stratum','fam','corpus','fam %','corpus %'))
for c in 'ASNCP':
    print('%-10s %6d %6d %8.1f%% %8.1f%%' % (
        STRAT[c], byS[c], tot[c], 100*byS[c]/len(hits), 100*tot[c]/len(rows)))
print('%-10s %6d %6d' % ('(no code)', byS.get('',0), tot.get('',0)))
print()

print('=== C. counts by Arnold stratum, split by certainty ===')
print('uppercase = period assigned outright; lowercase = period indicated by')
print('metrical variations alone (Arnold 1905: 269, App. IV section 265)')
cert = collections.Counter((r['stratum'].upper(), r['stratum'].isupper()) for r in hits if r['stratum'])
print('%-10s %8s %8s' % ('stratum','certain','metr.only'))
for c in 'ASNCP':
    print('%-10s %8d %8d' % (STRAT[c], cert[(c,True)], cert[(c,False)]))
print()

print('=== D. counts by stratum per lemma ===')
print('%-14s %s %6s' % ('lemma', ' '.join('%8s'%STRAT[c] for c in 'ASNCP'), 'total'))
for lid,(lem,_,_) in FAMILY.items():
    sub = collections.Counter(r['stratum'].upper() for r in hits if r['lemma_id']==lid)
    print('%-14s %s %6d' % (lem, ' '.join('%8d'%sub[c] for c in 'ASNCP'),
                            sum(sub.values())))
print()

print('=== E. counts by book (the second chronological instrument) ===')
byB = collections.Counter(int(r['book']) for r in hits)
totB = collections.Counter(int(r['book']) for r in rows)
print('%-6s %5s %8s %9s' % ('book','fam','corpus','fam per 10k'))
for b in range(1,11):
    print('%-6d %5d %8d %11.1f' % (b, byB[b], totB[b], 10000*byB[b]/totB[b]))
print()

print('=== F. flagged exclusions ===')
for lid,(lem,gloss) in FLAGGED.items():
    n = sum(1 for r in rows if r['lemma_id']==lid)
    s = collections.Counter(r['stratum'].upper() for r in rows if r['lemma_id']==lid)
    print('%-16s %3d  %s' % (lem, n, gloss))
    print('%-16s      strata: %s' % ('', dict(s)))
print()

print()
print('=== H. dispersion tests ===')
def chi2sf(x, k):          # survival function, k even
    m = k // 2
    return sum(math.exp(-x/2) * (x/2)**i / math.factorial(i) for i in range(m))

tt = collections.Counter(r['stratum'].upper() for r in rows)
ft = collections.Counter(r['stratum'].upper() for r in hits)
chi = 0.0
for c in 'ASNCP':
    exp = len(hits) * tt[c] / len(rows)
    chi += (ft[c] - exp) ** 2 / exp
print('token level : chi-square (4 df) = %.2f, p = %.4g' % (chi, chi2sf(chi, 4)))

# hymn level: each hymn takes its majority stratum code
cnt = collections.defaultdict(collections.Counter)
for r in rows:
    cnt[(r['book'], r['hymn'])][r['stratum'].upper()] += 1
hymaj = {k: c.most_common(1)[0][0] for k, c in cnt.items()}
famhy = set((r['book'], r['hymn']) for r in hits)
fo = collections.Counter(hymaj[k] for k in famhy)
to = collections.Counter(hymaj.values())
chi = 0.0
for c in 'ASNCP':
    exp = len(famhy) * to[c] / len(hymaj)
    chi += (fo[c] - exp) ** 2 / exp
print('hymn level  : chi-square (4 df) = %.2f, p = %.4g  (n=%d hymns of %d)'
      % (chi, chi2sf(chi, 4), len(famhy), len(hymaj)))

# book order, grouped family books (2-7) against the rest
a = sum(1 for r in hits if 2 <= int(r['book']) <= 7)
A = sum(1 for r in rows if 2 <= int(r['book']) <= 7)
b, B = len(hits) - a, len(rows) - A
ea, eb = len(hits) * A / len(rows), len(hits) * B / len(rows)
chi = ((a-ea)**2/ea + (b-eb)**2/eb
       + ((A-a)-(A-ea))**2/(A-ea) + ((B-b)-(B-eb))**2/(B-eb))
print('books 2-7 %.2f per 10k vs books 1,8,9,10 %.2f per 10k'
      % (10000*a/A, 10000*b/B))
print('book order  : chi-square (1 df) = %.2f, p = %.3g'
      % (chi, math.erfc(math.sqrt(chi/2))))

# sensitivity: admit the puraṃdhi- group
EXT = set(FAMILY) | set(FLAGGED) - {'lemma_purAsah_5564'}
ext = [r for r in rows if r['lemma_id'] in EXT]
eo = collections.Counter(r['stratum'].upper() for r in ext)
chi = 0.0
for c in 'ASNCP':
    exp = len(ext) * tt[c] / len(rows)
    chi += (eo[c] - exp) ** 2 / exp
print('with puraṃdhi- admitted (n=%d): chi-square (4 df) = %.2f, p = %.4g'
      % (len(ext), chi, chi2sf(chi, 4)))

print()
print('=== I. entanglement of the two instruments ===')
P = [r for r in rows if r['stratum'].upper() == 'P']
b10 = sum(1 for r in P if r['book'] == '10')
t10 = sum(1 for r in rows if r['book'] == '10')
print('%.1f%% of Popular-stratum tokens are in book 10; book 10 is %.1f%% Popular'
      % (100*b10/len(P), 100*b10/t10))

print()
print('=== G. full occurrence list ===')
print('\t'.join(['stanza','pada','tok','surface','lemma','morph','metre',
                 'stratum','stratum_name','certainty']))
for r in sorted(hits, key=lambda r:(int(r['book']),int(r['hymn']),
                                    int(r['stanza_n']),r['pada'],int(r['tok_i']))):
    name, certn = strat_name(r['stratum'])
    print('\t'.join([r['stanza'], r['pada'], r['tok_i'], r['surface'],
                     r['lemma'], r['morph'], r['metre'], r['stratum'],
                     name, certn]))
