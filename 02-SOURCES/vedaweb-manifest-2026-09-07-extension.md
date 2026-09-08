# VedaWeb corpus — manifest extension for the §4J forts corpus

**Written:** 2026-09-07
**Extends:** `02-SOURCES/vedaweb-manifest-2026-09-07.md`
**Backing record for ledger rows:** `SRC-069` … `SRC-079`

The earlier manifest pins twenty files at commit
`d3eb8af7324338161520d2d35eae8f7e985a19a5`. Those twenty are the layers the
`púr-` family register needed: text, lemma, morphology, metre. Constitution §4J
asks for fields that none of them carries — patron, poet lineage, opponent,
description, material, water, cattle, treasure, mountain or river, geography.
This extension pins the further files in the **same clone at the same commit**
that bear on those fields, so that the §4J build is reproducible from one
commit SHA exactly as the register is.

Nothing here is a new retrieval target. It is the same repository, the same
commit, the same licence position, and files that were present in the earlier
clone but not brought into use.

## Re-retrieval event behind this extension

| Field | Value |
|---|---|
| Repository | `VedaWebProject/vedaweb-data` |
| Command | `GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/VedaWebProject/vedaweb-data` |
| HEAD commit | `d3eb8af7324338161520d2d35eae8f7e985a19a5` |
| Retrieval date (UTC) | 2026-09-07 |
| Local path | `/home/user/vedawebproject/vedaweb-data` (session-local, not committed) |
| Verification | **All 20 files of the earlier manifest reproduce their recorded sha256 and byte length exactly.** The concatenation of the ten book TEI files reproduces `8d4711021c3d36d3e996c9ebc5cff304ae9a811dd145ecda420e7e7c514c68a3`. Zero mismatches. |
| Access channel | Session git proxy anonymous read lane. `codeload.github.com` was not re-probed; the earlier `SRC-019` finding stands. |

This is the third recorded clone of this repository (`SRC-019`, `SRC-047`,
`SRC-059` precede it). Per `DEP-020` these are **one retrieval target, several
events**, and a claim citing more than one of them cites one source.

## Files pinned by this extension (sha256)

Paths relative to `rigveda/` in the clone.

| sha256 | bytes | path |
|---|---|---|
| `1b8096f9867227ec93ede1beb82a3957a5a2500ad86ca569c06f486831ec8189` | 193879 | `info/addressees.json` |
| `a40c53cab4a41107436ecf6b982e54068ee90e3b661cf7dffe59f11d93ef1e64` | 155153 | `info/stanza_properties.json` |
| `94b4c4cca379475f591c3aad1657e1871b627a393db837d10d3416431ac742fa` | 3110 | `info/codes_abbreviations.csv` |
| `b6c329643ed74239d2a35eb6afe0c5764c99572542ed892477894b212513f9e5` | 7622 | `info/translation_version_stanza_coverage.md` |
| `473db34d6a4c7eace7a08a8d6628b899d49eff7dfd104013d1445b81b9074854` | 1777145 | `translations/eng/griffith.csv` |
| `4eef1cdb0c06ecd3a0dfcb2a83c0ef91784a13d1f3be749015949f826e4b5ab9` | 1968193 | `translations/deu/geldner.csv` |
| `06fe3b72dd65274e4bbe0a4e84de02f951eb9b1034b4d17df3a917201e795bf5` | 1746668 | `translations/deu/grassmann.csv` |
| `777e696721a6b9cbacff1fcfdad5ef68e149b1607865c2b12c433202bcf78d7f` | 3493115 | `translations/rus/elizarenkova.csv` |
| `18402e54d9961e81964c49fda820834fd25b6476455ff398a01a59abc92819d3` | 1569336 | `translations/fra/renou.csv` |
| `f2d0bfe755bf04ed21612ef836a6df0fcebc0a7d5324e7c117bf57208165be00` | 73912 | `translations/eng/macdonell.csv` |
| `d48cf533ee6be4309a98a59c50826105f81814fd8fcd1c173aea179916b858cc` | 94157 | `translations/eng/mueller.csv` |
| `91009acc147a8011ec65a3a394211620e1bd08fc9ebcb3bba8a3fb3143987235` | 221536 | `translations/eng/oldenberg.csv` |
| `9c94db2b5c0b01e899fa1143dad5f9ceece551c0a50d6f21623312df29496447` | 1985098 | `versions/vnh.csv` |
| `76728d05ab4f400efe0379f25479358f6cc35b4f6f7f396678a19bc01fa1c0e5` | 3405905 | `versions/eichler.csv` |
| `9d9de96b690f54c4a1a49d9082e5b5145d1fa58a84fe235ae24b6caf76b57c14` | 56227 | `external-resources/Oldenberg/Oldenberg_Band_1.csv` |
| `71d2a32303111afbf9ab865751dc22e3d572ff175a6eb4c966b96f97d617534c` | 58289 | `external-resources/Oldenberg/Oldenberg_Band_2.csv` |
| `3123a5252fc9265fd793408be235f76856aafe9a50ad6cb5c68e5cfc14182dd6` | 59432 | `external-resources/Ludwig/Ludwig_Band_1.csv` |
| `b29317acc6f7c3c19d2c036673728e36a24a17c2d74c96318d09dad77eceae6c` | 97384 | `external-resources/Ludwig/Ludwig_Band_2.csv` |
| `e541b8f354b083f99a44697f9d2924ab1322e49a54a97a62d2ca43aa18b04ac2` | 43146 | `external-resources/Delbrueck/Delbrueck_1888.csv` |

`info/rv_locations.tsv` and `info/rv_locations.json` were pinned by the earlier
manifest (`rv_locations.tsv` at
`0ade6904696de9ac173c4e005ab3aec849c5c41c336a7fb831bb5acf07df0c48`). They are
inspected in this unit; see §"What rv_locations is not" below.

## What each new layer can and cannot support

### `info/addressees.json` — 1028 entries, one per hymn

Two strings per hymn, each in German and English:

1. an **addressee** (devatā) — `"An Agni"` / `"Agni"`;
2. a **group heading** — `"1. Gruppe: Lieder des Madhucchandas"` /
   `"1. group: hymns of Madhucchandas"`.

The group heading is the only per-hymn poet attribution anywhere in this clone,
and it is the field §4J's *poet lineage* has to be built from unless a separate
Anukramaṇī is retrieved.

**What it is.** The corpus TEI header credits *Rigveda – Addressees* to the
Cologne Center for eHumanities, 2020, CC-BY-4.0, with no upstream cited. The
German wording (`Lieder des …`, `Gruppe`) is Geldner's editorial apparatus in
*Der Rig-Veda* (HOS 33–35), and the groups reproduce Geldner's hymn-group
divisions. Geldner's groups in turn follow the Anukramaṇī tradition, which is a
late-Vedic to post-Vedic ascription, not a statement the Rigveda makes about
itself.

**What it therefore cannot support.** It cannot support a claim that a named
poet composed a hymn. It supports a claim that *Geldner grouped this hymn under
this poet's name*, which is an editorial fact of 1951 resting on a tradition
whose own date is later than the text. Three removes separate the field from the
composition event, and every §4J *poet lineage* value carries all three.

### `info/stanza_properties.json` — 2372 stanzas flagged

Keys are stanza ids; values are a dict over five scholars' judgements, whose
column names the file's own header row gives as `grassmann` (Grassmann),
`oldenberg` (Oldenberg, *Prolegomena* notes), `arnold` (Arnold, *Sketch*),
`wuest` (Wüst, *Stil*), `witzel` (Witzel, *RVHist*). The TEI header supplies the
full bibliography: Grassmann 1876–7; Oldenberg 1888 and 1909/1912; Arnold 1897
JAOS 18:203–353; Wüst 1928; Witzel 1995 in Erdosy ed.

**Why this matters here.** `PUR-026` is capped at `PROVISIONAL` partly because
the register's stratum column has **one** chronological instrument behind it —
Arnold 1905's metre, transcribed (`DEP-001`) — and the by-book second instrument
returns a null and is entangled with it (`DEP-004`). This file supplies four
further scholars' judgements about which stanzas are late or interpolated, from
different evidence (style, grammar, textual criticism, history). Whether they
agree with Arnold's metre is a question this unit can now ask rather than assume.

**What it cannot support.** These are flags, not a periodisation: a stanza is
marked or not marked by a given scholar. Arnold 1897 (*Sketch*, grammar) and
Arnold 1905 (*Vedic Metre*, metre) are the same author and not independent of
each other; that dependency is logged.

### `translations/` — nine translations, four independent lines

Full-corpus coverage per `info/translation_version_stanza_coverage.md`:
Elizarenkova 100.00 %; Grassmann 99.97 % (3 stanzas missing); Geldner 99.96 %
(4 stanzas missing); Griffith (10550 rows). Partial: Renou 6730 rows,
Oldenberg 1140, Müller 533, Macdonell 414, Otto 74.

These make the §7 translation standard runnable on `púr-`: the *alternative
translations* requirement stops being a literature question and becomes an
extraction. Nine renderings of the same accented word at the same locator, from
1876 to 1999, in five languages.

**Dependency warning, load-bearing.** `translations/deu/grassmann.csv` and the
Grassmann *Wörterbuch zum Rig-Veda* glosses that fixed the register's family
boundary (`PUR-006`, method §3) are **the same man's judgement**. A `púr-`
passage where Grassmann's translation agrees with Grassmann's dictionary is one
opinion, not two. Logged as `DEP-021`.

### `versions/vnh.csv` — van Nooten & Holland 1994

The metrically restored text. An independent editorial reconstruction against
Aufrecht's Saṃhitāpāṭha (`SRC-020`), usable as a check on whether a `púr-`
reading is stable across editions.

### `external-resources/` — Oldenberg, Ludwig, Delbrück note indexes

Locator indexes into the printed commentaries (Oldenberg *Noten* Bd. 1–2,
Ludwig Bd. 1–2, Delbrück 1888), not the commentary text. They tell you which
page discusses a stanza. Useful for citing where a crux is argued; they cannot
tell you what was argued.

## What `rv_locations` is not

`info/rv_locations.tsv` (10552 rows) and `info/rv_locations.json` were flagged in
`06-BRIEFS/rv01-reconciliation.md` §4 as possibly bearing on §4J's *proposed
geography* field. They do not. The eight columns are
`DOTS_AND_ZEROS`, `COMMAS_AND_ZEROS`, `DOTS`, `COMMAS`, `GRASSMANN`,
`BOOK_INDEX`, `HYMN_INDEX`, `STANZA_INDEX` — a citation-format conversion table
mapping one stanza addressing convention onto another. "Location" here means
*location in the text*, not location on the earth.

**This is recorded because the guess was reasonable and wrong.** No geographic
content of any kind exists in this clone. §4J's *mountain or river* and
*proposed geography* fields cannot be filled from VedaWeb; what the corpus can
supply is which toponym and hydronym **lemmas** occur in a `púr-` passage, which
is a textual fact, and the step from a hydronym to a place on a map is a
separate claim requiring separate evidence.
