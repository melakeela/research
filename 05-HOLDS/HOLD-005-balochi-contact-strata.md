# HOLD-005 — the Balochi and Indo-Aryan strata in Brahui are not measurable here

**Raised by:** domain M, six-models unit, 2026-09-07
**Blocks:** `DMI-008`, `DMM-016`, `DMM-019`, and the "Balochi influence",
"Indo-Aryan contact layers", "Old and Middle Iranian contact possibilities"
and "what contact should actually be expected" items of constitution §4.M.
**Ledger:** `SRC-062`, `SRC-070`, `SRC-072`, `SRC-059`. Companion to `HOLD-004`.

## What was asked

The owner asked for the Indo-Aryan and Balochi contact layers in Brahui to
be measured from retrieved data. They cannot be, and this hold records why
in the terms the negative-evidence standard requires, so that the failure
is not mistaken for a finding about contact.

## What was reached, and what each reached source can and cannot carry

**Korn, *Towards a Historical Grammar of Balochi*, 2005** (`SRC-062`) is the
work that describes the strata. Its abstract states that the Balochi lexicon
shows layers of loanwords, with Persian influence continuous "from the
earliest times to the present day", relationships to Kurdish, Pashto and
Brahui, and "particularly in the field of kinship terminology, intense
contact with speakers of Modern Indic languages". That is the shape of the
answer. It supplies no item, no stratum boundary, no date and no direction.
The book was not opened. **NOT ACCESSIBLE.**

**Smirnitskaya 2020** (`SRC-070`) is the one source that states a
*stratified* result rather than convergence in general: Brahui kinship terms
for father, grandfather and aunt are borrowings, while mother, brother,
grandmother and mother's brother are Dravidian, with Persian, Balochi,
Punjabi and Sindhi named as donors. That is a testable shape — borrowing at
the senior and affinal edges, retention at the core. No item list and no
counts are in the abstract, so no rate is measurable from it. **NOT
ACCESSIBLE** for the rest.

**Cathcart 2022** (`SRC-072`) was retrieved as full text and is the one
source here with a resolvable DOI. It places Balochi as transitional between
Northwest and Southwest Iranian and argues that West Iranian irregularity is
not reducible to lexical borrowing from Persian — that multilingual speakers
imposing pronunciations across cognates is a documented alternative. That
bears on *what contact to expect*, which §4.M asks about: the Brahui–Balochi
relationship should be looked for in sound substitution as well as in
wordlists. It says nothing about Brahui.

## What the reachable data cannot do, and why that is not a finding

The DEDR re-encoding (`SRC-059`) carries DEDR's form and gloss fields only.
It has no headnotes, no etymological discussion and no loanword annotation,
and a search across `data/dedr/dedr.csv`, `data/dedr/params.csv` and
`cldf/entry-texts.csv` for *baloch* or *baluch* returns **zero lines**.

That absence is typed **NOT PRODUCED**: the encoding does not generate
evidence of this kind. DEDR itself says more than its encoding carries. This
is a property of the file, not of the dictionary, and under the
negative-evidence standard it is not evidence that Brahui has no Balochi
loans — a proposition that every retrieved source contradicts.

The Indo-Aryan side is measurable only where Turner's `CDIAL` cross-references
DEDR: 604 cross-references, 118 of which resolve to a DEDR entry present here,
**12** of them landing on a Brahui-bearing entry (`DMM-008`). And `CDIAL`
names Brahui on **one line in 159,756** (`DMM-009`). That second absence is
typed **ABSENT DESPITE ADEQUATE SEARCH**, bounded strictly to that dictionary:
`CDIAL` is exhaustive for Indo-Aryan and its author did compare across
families 604 times, so the near-total absence of Brahui by name is a real
fact about the standard Indo-Aryan comparative record. It shows that the
contact has not been worked into the reference work that would carry it. It
does not show that the contact is absent.

## What is needed

1. **Korn 2005**, read: the stratum boundaries, the items assigned to each,
   and the direction of each assignment.
2. **Elfenbein, "Brahui", in Steever (ed.), *The Dravidian Languages*, 1998,
   388–414** — carried in the inherited record as load-bearing and unread
   since the handoff (`IH-236`), and still unread. Also on `HOLD-004`.
3. **Emeneau, *Brahui and Dravidian Comparative Grammar*, 1962** — on
   `HOLD-004`; needed here too, because DEDR's Brahui entries and this book
   are one evidentiary chain (`DEP-011`) and the loan discussion is in the
   book rather than in the dictionary's data fields.
4. **Smirnitskaya 2020** in full, for the item list behind the shape.
5. **DEDR with its headnotes**, i.e. what `HOLD-002` has always asked for.
   The re-encoding narrows `HOLD-002` for cognate counting and does nothing
   for it here.

## What would change

Item 1 alone would make the question measurable. With stratum assignments
in hand, the Balochi layer in Brahui could be dated *relative to* the
Balochi expansion frame at `DMC-001`, and that is the one place in this
domain where a contact measurement could begin to discriminate among the
six §4.M models — because the models differ in how long Brahui and Balochi
have been in contact, and a stratified loan inventory is a record of that
duration. Nothing currently in this repository can make that comparison.

## What is *not* claimed

That Brahui's Balochi contact is shallow, or deep. Nothing here bears on it.

That the Indo-Aryan layer is thin. `DMM-009` measures a dictionary, not a
language, and `DMM-019` reports Indo-Aryan donors in Brahui kinship
vocabulary from a source that looked for them.

That the twelve `CDIAL`–DEDR touchpoints on Brahui-bearing entries are loans.
78% of the 604 relations are of undetermined direction and the twelve were
not individually examined.
