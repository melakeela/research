# HOLD-004 — the evidence that would decide North Dravidian is unreachable

**Raised by:** domain M, Brahui position unit, 2026-09-07
**Blocks:** DMB-018, DMB-019, DMB-023, DMB-024, DMB-026 — everything about
whether Brahui belongs with Kurukh and Malto, in either direction.
**Ledger:** `SRC-049`, `SRC-051`, `SRC-052`; inherits `SRC-037`, `SRC-040`,
`SRC-041` from HOLD-002.

## What is needed

The conventional case for a North Dravidian subgroup is phonological and
morphological, not lexical. What this unit could measure was lexical
sharing on a hundred-concept wordlist, which is the wrong instrument for
the question and says so in its own header. To decide it:

1. **Krishnamurti, Bhadriraju, *The Dravidian Languages*, Cambridge:
   Cambridge University Press, 2003** (Cambridge Language Surveys,
   xxvii+545, ISBN 9780521771115, OCLC 57417931). This is the load-bearing
   source. Glottolog's North Dravidian node cites it and nothing else, and
   so do Glottolog's Central and South Dravidian nodes; DravLex's cognate
   coding lists it among five sources. Everything retrievable in this
   session that asserts the subgroup traces back to this one book, which
   this project has never read — it stands at "Named, not read" (`IH-237`,
   `01-INHERITED/claude-project-handoff.md` L451). Needed: the chapter and
   section that state the North Dravidian innovations, cited by page.
2. **Kobayashi, Masato and Bablu Tirkey, *The Kurux Language: Grammar,
   Texts, and Lexicon*, Leiden: Brill, 2017**, Brill's Studies in South and
   Southwest Asian Languages 8, xvii+791. Glottolog cites **pages 11–14**
   for the Kurux–Malto node specifically. That is a precise locator for the
   lower node and it is the one place the classification has a second,
   independent source.
3. **Emeneau, M. B., *Brahui and Dravidian Comparative Grammar*,
   Berkeley: University of California Press, 1962**, University of
   California Publications in Linguistics 27, xi+91.
4. **McAlpin, David, "Is Brahui Really Dravidian?"**, *Proceedings of the
   Sixth Annual Meeting of the Berkeley Linguistics Society*, 1980, 66–73.
   Retrieved as a bibliographic record only. What it argues is unknown here
   and no inference from its title is licensed (`DMB-023`).
5. **Elfenbein, Josef, "Brahui"**, in Sanford B. Steever (ed.), *The
   Dravidian Languages*, London and New York: Routledge, 1998, 388–414.
   This is the late-migration source the inherited record has carried as
   load-bearing and unread since the handoff (`IH-236`).
6. **DEDR** — see HOLD-002, unchanged.

## What was tried

| Host | Channel | Result |
|---|---|---|
| `dsal.uchicago.edu` | curl | 403 at CONNECT |
| `archive.org` | curl | 403 at CONNECT |
| `glottolog.org` | curl | 403 at CONNECT |
| `doi.org` | curl | 403 at CONNECT |
| `api.crossref.org` | curl | 403 at CONNECT |
| `api.openalex.org` | curl | 403 at CONNECT |
| `api.semanticscholar.org` | curl | 403 at CONNECT |
| `zenodo.org` | curl | 403 at CONNECT |
| `royalsocietypublishing.org` | curl | 403 at CONNECT |
| `pmc.ncbi.nlm.nih.gov`, `europepmc.org` | curl | 403 at CONNECT |
| `degruyter.com`, `benjamins.com` | curl | 403 at CONNECT |
| `arxiv.org` | curl | 403 at CONNECT |
| `api.github.com` | curl | 403 at CONNECT |
| `github.com`, `raw.githubusercontent.com` | git, curl | **200** |

Only GitHub answers. `SRC-052` records this as tighter than the `SRC-045`
characterisation taken earlier the same day: `doi.org` and `arxiv.org`
answered at 02:19Z and do not answer at 03:03Z. `RA-003` already warns that
`SRC-025` and `SRC-027` to `SRC-036` record reachability that no longer
holds; this hold is a second instance of the same drift and the warning
should be read as covering `SRC-045` too.

What GitHub did yield is not nothing, and it is why this hold is narrower
than HOLD-002: `lexibank/dravlex` gave a cognate-coded twenty-variety
dataset (`SRC-049`) and `glottolog/glottolog` gave the classification tree
and the bibliography that names every source above (`SRC-051`). What GitHub
cannot yield is a page of any of them.

## What is *not* claimed

That North Dravidian is invalid. `DMB-018` and `DMB-019` report that a
lexical instrument does not support the Brahui attachment; `DMB-020` types
that absence as **NOT PRODUCED** — the instrument does not generate
evidence of the required kind — and **NOT ACCESSIBLE** for the rest. Under
the negative-evidence standard neither type is a refutation, and a
hundred-concept wordlist returning two exclusive sets is not an adequate
search for a phonological innovation.

That Brahui is not Dravidian. Nothing in this unit bears on that. The
question is recorded as posed in the literature (`DMB-023`) and as
unanswerable here.

That the subgroup is validated. `DMB-026` refuses both verdicts, which is
what the owner's instruction required.

## What the answer would change

Item 1 alone would settle whether there are stated North Dravidian
innovations and how many rest on Brahui rather than on Kurukh and Malto.
That is the difference between `DMB-026` staying `PROVISIONAL` and the
subgroup question becoming answerable at all. It would also convert
`DEP-008` from a live circularity warning into a checkable claim: if
Krishnamurti's innovations are phonological, DravLex's lexical coding is
substantially independent of them after all, and `DMB-018` gets stronger.

---

## Update, 2026-09-07, domain M six-models unit

Two of the six items moved. The hold stays open.

**Item 6, DEDR — partially met, and only in one respect.** `SRC-059` reached
a machine-readable re-encoding of DEDR inside the Jambu database on GitHub,
GitHub being the one host that answers. 5,520 entries, 26 attested languages,
68,808 form lines parsed with zero failures. This is the first time this
project has read any Dravidian etymological dictionary, and it made the
measurement at `DMM-001` to `DMM-005` possible — including a permutation test
that `DravLex` was too small to support.

It does **not** meet what this hold and `HOLD-002` actually asked for. The
encoding carries form and gloss fields only: no headnotes, no etymological
discussion, no loanword annotation. It is a derived copy, and `DEP-010`
records that it is DEDR parsed rather than a second witness to it. What it
answers is "how did Burrow and Emeneau distribute these forms across the
family"; what it cannot answer is anything DEDR says in prose.

**Item 2, Kobayashi and Tirkey — met at abstract level, not at the locator.**
`SRC-063` returned the 2019 *Kurux* chapter's abstract, which states the
morphological case for the lower node (shared past stem formation, agreement
and case suffixes), that "there is no doubt that Kurux and Malto constitute a
close subgroup", that "the position of Kurux-Malto in the Dravidian family
has been much debated", and that the difficulty is that "few innovations
shared with other subgroups are identified". Glottolog's locator — Kobayashi
and Tirkey 2017, pp. 11–14 — is still unread, and an abstract carries no page.

**Item 1, Krishnamurti 2003 — unchanged and still load-bearing.** Nothing
reached it. Cambridge University Press is outside every reachable connector's
corpus: `SRC-054` is Wiley-only, `SRC-053` is abstract-level, and every
publisher host returns no connection (`SRC-058`). It remains the book that
everything traces to and that this project has never read.

**Items 3, 4 and 5 — Emeneau 1962, McAlpin 1980, Elfenbein 1998 — unread.**
One thing did change around item 4. `SRC-065` reached the abstract of
McAlpin's 2003 *Velars, Uvulars, and the North Dravidian Hypothesis*, which
states that "no serious scholar has denied that a valid genetic connection
exists between Brahui and the Dravidian languages" and that the paper
"explore[s] the phonology which connects Brahui with Kurux and Malto". That
settles the *direction* of `DMB-023` — the question posed in McAlpin 1980 is
about the nature of the connection, not its existence — and settles nothing
else. What McAlpin's "new solution" is remains unknown here. `SRC-066` adds
that McAlpin was still arguing an Elamite descent for Brahui in 2022.

**One item now answers itself in the negative.** `DMM-011`: Nair 2003 reports
that the initial *v-/b-* change "cannot be considered as a valid phonological
isogloss for sub grouping NDr", being areal rather than a shared innovation,
and attributes the contact reading to Krishnamurti. So at least one named
North Dravidian isogloss has been withdrawn in print. That sharpens item 1
rather than replacing it: the question this hold asks is *which* innovations
Krishnamurti states and how many of them rest on Brahui, and one withdrawal
does not answer it.

**What the hold now blocks.** `DMB-018`, `DMB-019`, `DMB-023`, `DMB-024`,
`DMB-026` as before, plus `DMI-001` and `DMI-002` — which is to say, whether
the seven exclusive Brahui–Kurux–Malto etymologies at `DMM-003` are
inherited or areal, and whether the 176 Kurux–Malto sets at `DMM-002` are a
clade or a neighbourhood. A lexical instrument cannot answer either, however
large. `HOLD-005` is the companion hold for the contact-stratum half.
