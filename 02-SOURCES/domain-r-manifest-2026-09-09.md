# Domain R retrieval manifest — 2026-09-08 / 2026-09-09

What was retrieved, from where, by what call, and how to re-derive it. Written
so that a later session can reproduce every measurement in this unit without
re-deciding anything, and so that a reviewer can check the counts rather than
accept them.

---

## 1. The two primary files

Both were retrieved through the **Git LFS media endpoint**, not through the
repository clone. `git clone` of `cdli-gh/data` returns LFS *pointer* files —
133 and 134 bytes — and `git-lfs` is not installed in this container. The
pointer files name the content hash and size, and the media endpoint serves the
content.

```
git clone --depth 1 https://github.com/cdli-gh/data          # commit d66b12b0
curl -sS -L -o cdli_cat.csv \
  https://media.githubusercontent.com/media/cdli-gh/data/master/cdli_cat.csv
curl -sS -L -o cdliatf_unblocked.atf \
  https://media.githubusercontent.com/media/cdli-gh/data/master/cdliatf_unblocked.atf
```

| File | Bytes | sha256 | Ledger |
|---|---|---|---|
| `cdli_cat.csv` | 154,768,722 | `2e3232f75325b61c4d1e788d4d8c074c6230a947aed422110f9f35a6e353d09c` | `SRC-102` |
| `cdliatf_unblocked.atf` | 86,897,831 | `2896ec253767fa07fcaa5424af6fc25d6a047dc30b99c95f99d57ce75384d836` | `SRC-103` |

**Both hashes are byte-for-byte the `oid` recorded in the repository's own Git
LFS pointer files.** The retrieval is therefore checked against the publisher's
manifest and not merely against itself. `04-AUDITS/domain-r-cdli-extract.py`
re-verifies both hashes on every run and refuses to proceed if either differs.

### Vintage — this is a 2022 snapshot

- Repository commit `d66b12b065af39a57d640576b4c7e098db5dac7f`, dated
  **2023-10-11**, whose subject is "Update README.md".
- That README states: **"Last update was August 2022."**
- The latest `date_updated` value across the 353,283 catalogue rows is
  **2022-08-21**.

Every custody, findspot and material statement drawn from this file is
therefore **as CDLI recorded it on or before 2022-08-21**, and the registers say
so in a `custody_as_of` column rather than implying the present tense.

### Shape

- `cdli_cat.csv` — 353,283 data rows, 64 columns. The columns this unit uses:
  `id_text`, `material`, `provenience`, `provenience_remarks`, `excavation_no`,
  `findspot_remarks`, `findspot_square`, `stratigraphic_level`, `collection`,
  `museum_no`, `accession_no`, `acquisition_history`, `period`, `object_type`,
  `designation`, `primary_publication`, `photo_up`, `date_updated`.
- `cdliatf_unblocked.atf` — 3,559,111 lines, ASCII ATF transliteration, keyed by
  `&P######` headers.

### The join, and the trap in it

The catalogue keys texts by `id_text`, a **bare integer**; the ATF keys them by
a **zero-padded P-number**. `id_text` `1` is the ATF's `&P000001`. Comparing the
two columns as written matches nothing, and the first run of the extraction
script reported `catalogue join: 0 of 1688` while producing a complete,
well-formed register in which every findspot and custody field was empty.

The key is rebuilt (`"P%06d" % int(id_text)`), the fix is commented at the point
of failure in the script, and the join now prints its match rate on every run:
**1,763 of 1,765 matched, 2 absent from the catalogue** (the figures moved as the classifiers were repaired; see `BF-032`, `BF-039`, `BF-041`). Logged as `BF-029`;
`RA-025` asks the same question of every other join in this repository.

---

## 2. Re-deriving the registers

```
DOMAIN_R_DATA=<dir holding the two files> python3 04-AUDITS/domain-r-cdli-extract.py
DOMAIN_R_DATA=<dir> python3 04-AUDITS/domain-r-museum-candidates.py
python3 04-AUDITS/domain-r-cdli-distributions.py
```

Producing:

| Output | Rows | What it is |
|---|---|---|
| `03-REGISTERS/domain-r-cdli-attestations.csv` | 3,788 | Accepted occurrences, classified by determinative and morphology, joined to the catalogue |
| `03-REGISTERS/domain-r-cdli-rejected.csv` | 348 | Occurrences excluded by rule, published so the exclusions can be checked |
| `03-REGISTERS/domain-r-cdli-summary.json` | — | Target × classification counts |
| `03-REGISTERS/domain-r-museum-candidates.csv` | 796 | Objects attributed to lapis, carnelian, or a look-alike |

The scripts are deterministic and take no input other than the two hashed files.

### Why the exclusions are published

A raw grep on these strings does not measure what it appears to. `gug` matches
1,520 lines and carnelian is only `gug` written with the stone determinative
`{na4}`; 257 of the matches are `gug2`, a baked good, and `{u2}gug4`, a plant.
`dilmun` matches 936 lines and its largest single form, 218 occurrences, is
`GIN2-DILMUN`, a unit of account. `ma2-gan` also matches the divine name
`{d}sza-ma-gan`, 29 times. The rejected file exists so that the exclusion rule
can be audited rather than trusted.

---

## 3. The literature lane

`SRC-105`, the Scholar Gateway MCP connector, over the **Wiley** full-text
corpus. Six queries between **2026-09-09T02:12Z and 02:30Z**; retrieval is
**passage-level, not article-level**.

| Query | Passages | Articles |
|---|---|---|
| Lapis trace-element and isotopic provenance | 15 | 3 |
| Harappan carnelian sources, Gujarat and Kutch | 20 | 4 |
| Shortugai, Harappan settlement, Badakhshan lapis, BMAC | 20 | 9 |
| Etched carnelian manufacture and distribution | 20 | 10 |
| Dilmun, Magan, Meluhha, Marhaši identification | 20 | 13 |
| Methodological criticism of geochemical provenance | 18 | 14 |
| Location of Marhaši | 18 | 13 |

**The Shortugai row is the calibration.** Twenty passages, nine articles, and
not one about Shortugai — because the site is published in French monographs
outside this corpus. That is the demonstration of `BF-027`, kept deliberately.

The standing status rule this lane imposes is at `SRC-105` and is applied
throughout: *"this article states X"* is `VERIFIED` against the passage;
*"X is true of the world"* is at most `PROVISIONAL`, because figures, tables,
supplementary data and reference lists were not delivered and `doi.org` is
refused (`SRC-095`), so no passage could be checked against its article.

---

## 4. What was refused

Twenty-nine hosts, all returning `curl (56) CONNECT tunnel failed, response
403`, zero bytes transferred, recorded by the proxy as
`connect_rejected — gateway answered 403 to CONNECT`. Listed at `SRC-099` and
`SRC-100`; the request is `D-055`.

The refusal is **protocol-shaped, not host-shaped**: plain `curl` to
`https://github.com/cdli-gh/data` returns 403 while `git clone` of the same
repository succeeds (`SRC-101`). A 403 from `curl` does not establish that a
host is unreachable by `git`, and a later session should probe both.

`raw.githubusercontent.com` and `media.githubusercontent.com` answer;
`api.github.com/repos/.../contents` does not (`SRC-104`). Retrieval from that
lane must therefore be **by known path** and cannot be by repository listing.
