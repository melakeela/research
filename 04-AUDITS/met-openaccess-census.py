#!/usr/bin/env python3
"""Census of the Met Open Access dataset for South Asian material.

Ledger: SRC-092. Reproduces the counts recorded there.

Run:
  curl -sS -L https://media.githubusercontent.com/media/metmuseum/openaccess/master/MetObjects.csv \
    | python3 04-AUDITS/met-openaccess-census.py

The dataset is a 317,650,992-byte Git-LFS object; it is streamed, not stored.
The first column header carries a UTF-8 BOM, so 'Object Number' is read
positionally rather than by name.

What this measures and what it does not:
  - It measures rows in the Met's own catalogue whose descriptive fields
    mention South Asia. The Met's Country column is populated only for the
    Islamic Art and Musical Instruments departments, so a Country-only filter
    finds 24 pre-1300 CE public-domain rows and a descriptive-field filter
    finds 1,005. The larger number is the right one and the discrepancy is
    itself a finding about the catalogue.
  - 'Is Public Domain' is the Met's assertion about the artwork, which is the
    basis of the CC0 image offer. It is not a statement about findspot,
    export legality, or the acquisition chain.
  - The keyword list is a modern geographic and dynastic vocabulary imposed on
    a curatorial catalogue. It will over-collect ('Indus' matches river-named
    objects) and under-collect (an object catalogued only as 'Deccan' region
    or with a blank Culture). Counts are approximate and directional.
"""
import csv, sys, collections

csv.field_size_limit(10 ** 7)

KEYWORDS = ['india', 'pakistan', 'bangladesh', 'sri lanka', 'nepal', 'deccan',
            'tamil', 'gandhara', 'indus', 'harappa', 'sindh', 'bengal',
            'punjab', 'mughal', 'chola', 'pallava', 'maurya', 'kushan',
            'gupta', 'satavahana', 'ceylon', 'baluchistan', 'swat']

SEARCH_FIELDS = ('Culture', 'Country', 'Region', 'Subregion', 'Period',
                 'Dynasty', 'Geography Type', 'Locale', 'Excavation',
                 'Title', 'Object Name')

ANCIENT_CUTOFF_CE = 1300


def main() -> None:
    reader = csv.DictReader(sys.stdin)
    total = public_domain = 0
    hits = hits_pd = hits_pd_ancient = 0
    dept = collections.Counter()
    ancient_dept = collections.Counter()
    ancient_culture = collections.Counter()
    ancient_class = collections.Counter()
    excavation = collections.Counter()
    rights_repro = collections.Counter()

    for row in reader:
        total += 1
        dept[row.get('Department', '')] += 1
        is_pd = row.get('Is Public Domain', '') == 'True'
        if is_pd:
            public_domain += 1
        blob = ' '.join((row.get(f) or '') for f in SEARCH_FIELDS).lower()
        if not any(k in blob for k in KEYWORDS):
            continue
        hits += 1
        if not is_pd:
            continue
        hits_pd += 1
        try:
            end = int(row.get('Object End Date') or 9999)
        except ValueError:
            end = 9999
        if end > ANCIENT_CUTOFF_CE:
            continue
        hits_pd_ancient += 1
        ancient_dept[row.get('Department', '')] += 1
        ancient_culture[(row.get('Culture') or '(blank)')[:50]] += 1
        ancient_class[(row.get('Classification') or '(blank)')[:40]] += 1
        if (row.get('Excavation') or '').strip():
            excavation[row['Excavation'][:50]] += 1
        rights_repro[(row.get('Rights and Reproduction') or '(blank)')[:40]] += 1

    print(f'rows                                  {total}')
    print(f'Is Public Domain = True               {public_domain}')
    print(f'South Asia keyword hits               {hits}')
    print(f'  of which public domain              {hits_pd}')
    print(f'  and Object End Date <= {ANCIENT_CUTOFF_CE} CE      {hits_pd_ancient}')
    print(f'departments (all rows, top 6)         {dept.most_common(6)}')
    print(f'ancient PD by department              {ancient_dept.most_common(10)}')
    print(f'ancient PD by culture (top 15)        {ancient_culture.most_common(15)}')
    print(f'ancient PD by classification (top 12) {ancient_class.most_common(12)}')
    print(f'ancient PD with Excavation populated  {sum(excavation.values())} {excavation.most_common(8)}')
    print(f'ancient PD Rights and Reproduction    {rights_repro.most_common(5)}')


if __name__ == '__main__':
    main()


# Appended 2026-09-08T22:26Z after the preferred-counter-narrative test.
# Ledger SRC-099. Register AS-007 (SUPERSEDED) -> AS-022.
#
# The first pass reported "Excavation populated on 2 of 1,005" and it was
# about to be read as "the Met's South Asian records have lost their
# findspots." That reading does not survive asking what the column does
# elsewhere in the same file. Run this before repeating the earlier one:
#
#   curl -sS -L <MetObjects.csv> | python3 -c "$(sed -n '/^def excavation_scope/,$p' \
#     04-AUDITS/met-openaccess-census.py); import sys; excavation_scope(sys.stdin)"

def excavation_scope(stream) -> None:
    """Which departments populate Excavation at all, and with what values."""
    import csv as _csv, collections as _c
    reader = _csv.DictReader(stream)
    dept_total, dept_filled, values = _c.Counter(), _c.Counter(), _c.Counter()
    for row in reader:
        d = row.get('Department', '')
        dept_total[d] += 1
        e = (row.get('Excavation') or '').strip()
        if e:
            dept_filled[d] += 1
            values[e[:60]] += 1
    print(f'Excavation populated: {sum(dept_filled.values())} of {sum(dept_total.values())}')
    for d, n in dept_total.most_common():
        if dept_filled[d]:
            print(f'  {d:38} {dept_filled[d]:6} of {n:6} ({100 * dept_filled[d] / n:.1f}%)')
    print('top values:', values.most_common(10))
