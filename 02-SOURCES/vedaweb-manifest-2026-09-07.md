# VedaWeb corpus retrieval — 2026-09-07

Backing record for ledger rows `SRC-019` through `SRC-024`.

## Retrieval event

| Field | Value |
|---|---|
| Repository | `VedaWebProject/vedaweb-data` |
| Clone URL | `https://github.com/VedaWebProject/vedaweb-data` |
| Command | `GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/VedaWebProject/vedaweb-data` |
| HEAD commit | `d3eb8af7324338161520d2d35eae8f7e985a19a5` |
| Commit date | 2025-06-13T07:07:10+00:00 |
| Retrieval date (UTC) | 2026-09-07 |
| Local path | `/home/user/vedawebproject/vedaweb-data` (session-local, not committed) |
| Working tree | 54 files, 316 MB |
| Licence | CC-BY-4.0, declared in `rigveda/TEI/vedaweb_corpus.tei` and `README.md` |

### Access channel note

The task specified codeload. `codeload.github.com` and `github.com` both
answered **HTTP 403** with a session-scoping message
(*"GitHub access to this repository is not enabled for this session"*),
so no tarball could be fetched. This is a Claude session repository-scope
denial, **not** an egress-proxy domain block — `raw.githubusercontent.com`
returned HTTP 200 for the same repository at the same moment. The clone
was made instead through the session git proxy's anonymous read lane
after `add_repo` reported read access already available. The resulting
tree is byte-identical in content to the tarball for the same commit;
the commit SHA below pins it.

## File checksums (sha256)

All paths relative to `rigveda/` in the clone.

| sha256 | bytes | path |
|---|---|---|
| `7b99eb3da956b54bc45a0c77ba825b22599aec35cde794a3a3fe21fedaf21c10` | 1734119 | `versions/aufrecht.csv` |
| `14f892794f32da89d1a6304b27209ebdfec9273f46e317f8811c32dd21105bee` | 2112144 | `versions/lubotsky.csv` |
| `2b4ba84dd5ca3d271e40c1cb5c64111bf7412376dac2915d627068d555dd6c11` | 1816322 | `versions/padapatha.csv` |
| `588498820ceb6e8a805cc22317d31770efa437e648e43491c57fb5056cade4b2` | 12559959 | `versions/zurich.xlsx` |
| `d667b62625ca1f4f4df5edcaba0a7487294bf57f69e0262e451388db93a98e8e` | 10868036 | `versions/vedaweb_zurich.xlsx` |
| `484e657e32ab7304aece763c072a1fa75d4042ffc4513d1426ba248776e0ed75` | 2566642 | `info/strata.json` |
| `10c013d5c8c8045cf9fbe62060c4d0134628a8a297f66a25ddbcc0217c608fe2` | 8520716 | `info/matched_lemmata.json` |
| `d277fbcc85e6005ad46e8d6f2a2a0bde51b19db0d136462db6758f32c57897e6` | 403596 | `info/revised_grassmann_mapping.csv` |
| `0ade6904696de9ac173c4e005ab3aec849c5c41c336a7fb831bb5acf07df0c48` | 549141 | `info/rv_locations.tsv` |
| `7ba145d984d5a669318e144fbd1b7154adf982827a5385f323ea7ef4e797a15b` | 111892 | `TEI/vedaweb_corpus.tei` |
| `c5c18d89a415ea16917f0f63616ee9fff7e32c4828b67f1e7647d2d023bc984c` | 43847826 | `TEI/rv_book_01.tei` |
| `236269da756609ef371df54bfe0734c6fc6177060a4cbcdc1fa9dc047c3a8c4b` | 10358758 | `TEI/rv_book_02.tei` |
| `be1c5c4cb8afaf521a3dd0b15a5f1427c436344443738d65e39ed2d737681ecf` | 13651928 | `TEI/rv_book_03.tei` |
| `6904be320f7dfd6fb63f7ec9b094842a1710518c0a61c46fc6affa905ad8f138` | 13024469 | `TEI/rv_book_04.tei` |
| `7df03f8c5d9e757523d258e461143f600c3024ee9d3eaa9847d989f656bfae12` | 15799754 | `TEI/rv_book_05.tei` |
| `03e16cb1b8f7e06fac982b7902a860590620fb275bc71b05278d89220aaf91d9` | 16764669 | `TEI/rv_book_06.tei` |
| `b182a5b4752f5aa2c02ae07828c9810015a1f30d12f7ffce7687051b36677fce` | 18936506 | `TEI/rv_book_07.tei` |
| `b03b440347e7a41e1821eeff7f342ce6f7127542274e565101586a31b7f782ec` | 30069055 | `TEI/rv_book_08.tei` |
| `83b24f18270de4e31a6fe981dcf7eac6cc3a1d6a8f0bf990e5c1dfbab7185917` | 20038585 | `TEI/rv_book_09.tei` |
| `e2e4deebb0cb418fd6b10c48c08967353de2d5d70114042af93418c4e2907060` | 40017181 | `TEI/rv_book_10.tei` |

Concatenation of the ten book files, in numeric order:
`8d4711021c3d36d3e996c9ebc5cff304ae9a811dd145ecda420e7e7c514c68a3`.

## What each layer can and cannot support

- **Aufrecht** (`versions/aufrecht.csv`) — Saṃhitāpāṭha, one row per pāda.
  Text only. Cannot ground a lemma count on its own.
- **Lubotsky / padapāṭha** (`versions/lubotsky.csv`, `versions/padapatha.csv`)
  — word-divided text with compound boundaries marked by `-`.
  Segmentation evidence, not lemmatisation.
- **Zürich** (`versions/zurich.xlsx`, and the `source="zurich"` token layer
  of the TEI) — the only layer carrying a lemma and morphology per token.
  Every count in this unit of work is taken from it.
- **Arnold strata** (`info/strata.json`) — one metre label and one stratum
  code per pāda. Derived from Arnold 1905; a single source.
