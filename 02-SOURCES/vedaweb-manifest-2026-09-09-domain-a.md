# VedaWeb corpus — manifest for the domain A chronology unit

**Written:** 2026-09-09
**Extends:** `02-SOURCES/vedaweb-manifest-2026-09-07.md` and
`02-SOURCES/vedaweb-manifest-2026-09-07-extension.md`
**Backing record for ledger rows:** `SRC-099` … `SRC-118`

This unit examines the dependency that every chronological claim in this
repository rests on. It therefore re-opens the same clone rather than a new
one, and it pins the *comparison* layers — the ones that could in principle
check Arnold — as carefully as the strata layer itself.

## Re-retrieval event

| Field | Value |
|---|---|
| Repository | `VedaWebProject/vedaweb-data` |
| Command | `GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/VedaWebProject/vedaweb-data` |
| HEAD commit | `d3eb8af7324338161520d2d35eae8f7e985a19a5` |
| Retrieval UTC | 2026-09-08T23:53Z |
| Local path | `/home/user/vw-a/vedaweb-data` (session-local, not committed) |
| Licence | CC-BY-4.0, declared in `rigveda/TEI/vedaweb_corpus.tei` |
| Access channel | session git proxy anonymous read lane |

**This is the fifth recorded clone of one repository** (`SRC-019`, `SRC-047`,
`SRC-059`, `SRC-069`, `SRC-085` precede it). `DEP-029` records that the five are
one source and several events. Nothing in this unit is corroborated by having
been fetched again.

## Files used, with sha256 as re-verified

Paths relative to `rigveda/` in the clone. Every one reproduces the value
recorded on 2026-09-07. Zero mismatches.

| sha256 | bytes | path | what it is here |
|---|---|---|---|
| `484e657e32ab7304aece763c072a1fa75d4042ffc4513d1426ba248776e0ed75` | 2566642 | `info/strata.json` | the instrument under examination |
| `a40c53cab4a41107436ecf6b982e54068ee90e3b661cf7dffe59f11d93ef1e64` | 155153 | `info/stanza_properties.json` | the four candidate non-Arnold instruments |
| `9c94db2b5c0b01e899fa1143dad5f9ceece551c0a50d6f21623312df29496447` | 1985098 | `versions/vnh.csv` | metrically restored text |
| `7b99eb3da956b54bc45a0c77ba825b22599aec35cde794a3a3fe21fedaf21c10` | 1734119 | `versions/aufrecht.csv` | transmitted Saṃhitāpāṭha |
| `2b4ba84dd5ca3d271e40c1cb5c64111bf7412376dac2915d627068d555dd6c11` | 1816322 | `versions/padapatha.csv` | padapāṭha |
| `14f892794f32da89d1a6304b27209ebdfec9273f46e317f8811c32dd21105bee` | 2112144 | `versions/lubotsky.csv` | Lubotsky pāda-split padapāṭha |
| `7ba145d984d5a669318e144fbd1b7154adf982827a5385f323ea7ef4e797a15b` | 111892 | `TEI/vedaweb_corpus.tei` | the provenance statements quoted below |
| `94b4c4cca379475f591c3aad1657e1871b627a393db837d10d3416431ac742fa` | 3110 | `info/codes_abbreviations.csv` | checked, and see §"What is *not* documented" |

## The provenance statements, quoted from the TEI header

**`strata.json`** — `biblFull xml:id="strata"`: *Rigveda - Strata Information*,
"Compiled by" **Dr. Dieter Gunkel** (Historical Linguistics, Department of
Classical Studies, University of Richmond) and **Prof. Dr. Kevin M. Ryan**
(Department of Linguistics, Harvard University); publisher Cologne Center for
eHumanities, 2020, CC-BY-4.0. Its `sourceDesc` (`biblFull xml:id="strata_src"`)
names exactly one source: *Vedic Metre in its Historical Development*, Edward
Vernon Arnold, "Unversity Press", Cambridge, 1905.

That is `DEP-001` in the bundle's own words. **One source, one author, 1905.**

**`stanza_properties.json`** — `biblFull xml:id="stanza_properties"`, compiled
by **Dieter Gunkel** and **Dr. Salvatore Scarlata** (Institut für Vergleichende
Sprachwissenschaft, Universität Zürich), CCeH 2020. Its
`sourceDesc xml:id="stanza_properties_src"` names five works:

- Arnold, *Sketch of the Historical Grammar of the Rig and Atharva Vedas*, 1897,
  JAOS 18: 203–353
- Grassmann, *Rig-veda: Übersetzt und mit kritischen erläuternden Anmerkungen
  versehen*, Brockhaus, Leipzig, 1876–7
- Oldenberg, *Die Hymnen des Ṛigveda. Metrische und textgeschichtliche
  Prolegomena*, Hertz, Berlin, 1888
- Oldenberg, *R̥gveda: Textkritische und exegetische Noten*, Weidmann, Berlin,
  1909 (books 1–6, AGWG ph.-hist. Kl. XI.5) and 1912 (books 7–10, XIII.3)
- Witzel, in Erdosy ed. (the file's column header reads `Witzel(RVHist)`); Wüst,
  *Stil*, 1928

Gunkel appears on **both** layers, and Scarlata is a co-author of
`SRC-105`. `DEP-032`.

## What is *not* documented anywhere in the bundle

Three things a reader would need, and none of them is in the retrieved files:

1. **What the stratum letters mean.** `info/codes_abbreviations.csv` documents
   the Leipzig glossing abbreviations and the present-stem classes. It does
   **not** document `A S N C P` or their lowercase variants, and neither does
   `vedaweb.odd`, which lists `strata` as a permitted value with an empty
   `<desc>`. The gloss used throughout this repository — A Archaic, S Strophic,
   N Normal, C Cretic, P Popular, lowercase = period indicated by metrical
   variations alone — comes from the Arnold OCR read on 2026-09-07 (`SRC-026`,
   Appendix IV §265, printed p. 269) and is recorded at `PUR-011`. **It was not
   re-checked in this session**, because archive.org refused (`SRC-100`).
2. **What the stanza-properties codes mean.** `vedaweb.odd` lists the permitted
   values `w W G z Z o O C1 C2` with empty `<desc>` elements. What distinguishes
   `o` from `O`, or `C1` from `C2`, is not stated. This unit therefore treats
   every column as a **binary flag** — the stanza is marked by that scholar or
   it is not — and makes no use of the letter values. That is a deliberate loss
   of resolution, taken because the alternative is guessing.
3. **Any statement that the strata are chronological.** The file is called
   *Strata Information*; the word "chronology" does not appear in its TEI
   block. The chronological reading is Arnold's and this repository's, not the
   bundle's.

## Layers deliberately **not** used

- `info/rv_locations.*` — inspected and rejected for this unit for the reason
  the 2026-09-07 extension already records.
- `versions/zurich.xlsx` / `vedaweb_zurich.xlsx` — the morphological layer was
  not needed: this unit measures strata, flags and text-forms, not lemmas.
- The nine translations — a chronology question is not settled by a translator.

## Reproducing every number in this unit

```
python3 04-AUDITS/domain-a-instruments.py <clone>/rigveda <outdir>
```

writes the seventeen tables in `04-AUDITS/domain-a-tables/`, which are the tables
`03-REGISTERS/domain-a-measurements.csv` cites by name. The script reads only
the files pinned above.
