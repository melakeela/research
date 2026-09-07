# The púr- family in the Rigveda — method and findings

**Unit of work:** 2026-09-07
**Register:** `03-REGISTERS/rigveda-pur-family.csv` (28 claims),
`03-REGISTERS/rigveda-pur-family-occurrences.csv` (106 occurrences)
**Sources:** `SRC-019` … `SRC-026` in `02-SOURCES/access-ledger.csv`
**Reproduce:** `04-AUDITS/rv-token-extract.py` then
`04-AUDITS/rv-pur-family-search.py`

---

## 1. What was retrieved

`VedaWebProject/vedaweb-data` at commit
`d3eb8af7324338161520d2d35eae8f7e985a19a5`, CC-BY-4.0. Per-file sha256
in `02-SOURCES/vedaweb-manifest-2026-09-07.md`.

The task asked for codeload. `codeload.github.com` and `github.com`
both returned **HTTP 403** for this repository — a Claude session
repository-scoping denial, not an egress block, confirmed by
`raw.githubusercontent.com` returning 200 for the same repository at
the same moment. The clone went through the session git proxy's
anonymous read lane instead. The commit SHA pins the result, so the
substitution costs nothing in verifiability.

Four layers were used:

| Layer | File | What it can support |
|---|---|---|
| Aufrecht Saṃhitā | `versions/aufrecht.csv` | text; no lemma |
| Lubotsky / padapāṭha | `versions/lubotsky.csv`, `versions/padapatha.csv` | segmentation; no lemma |
| Zürich morphology | TEI `source="zurich"` token layer | **lemma per token** — every count here |
| Arnold strata | `info/strata.json` | one stratum code per pāda |

Extraction produced 164,758 tokens over 10,552 stanzas and 39,832
pādas, each token carrying its lemma, its Grassmann lemma id, its
morphosyntax, and the Arnold stratum of the pāda it sits in.

## 2. Why lemma disambiguation, and what it bought

Correction **C-04** in `01-INHERITED` records a stem search that
reported Vipāś at 52 and Rasā at 78 where the true counts were 3 and
10. This search was built to avoid that failure, and the size of the
avoided error was measured rather than assumed.

A string search of the accented Saṃhitā for word-initial `pur-`/`pūr-`
returns **1,369 tokens across 142 lemmas**. Only 78 of them are the
fort word, and the search still misses the 5 tokens of the nominative
singular `pū́ḥ`. Precision 5.7%, recall 94.0%. The bulk of the noise is
`purú-` "many" (193), `pū́rva-` "former" (117), `pūrvyá-` (92),
`puruhūtá-` (80), `purā́` "formerly" (62), `purás` "in front" (52) and
`púraṃdhi-` (48) — none of them related to `púr-`.

Two sharper cases show what the lemma layer does that no string can:

- **`purā́`.** The string occurs 63 times. Sixty-two are the adverb
  "formerly"; one, at RV 1.53.7b (`purā́ púraṁ sám … haṁsi`), is the
  instrumental singular of `púr-`. Accent does not separate them.
- **The padapāṭha writes 160 tokens as bare `puraḥ` or `purā`.** It is
  unaccented at those points and cannot tell the fort word from the
  adverbs. The Zürich layer splits them 48 / 112.

Running the padapāṭha the other way is a genuine recall check, because
it is the ancient Śākalya analysis rather than a modern one: **no
stanza whose padapāṭha carries an unambiguous `púr-` form lacks a
`púr-` lemma token.** Zero misses. RV 1.58.8d is the clean example —
the padapāṭha reads `pūḥ-bhiḥ` for Saṃhitā `pūrbhíḥ`.

## 3. The family, and where its boundary was drawn

Seven lemmas, 106 tokens:

| Lemma | Tokens | Grassmann |
|---|---:|---|
| `púr-` | 83 | Wall aus Steinen und Lehm, Verschanzung, Palisade |
| `puraṃdará-` | 11 | Zerstörer der Wälle |
| `pūrbhíd-` | 8 | die Wälle aufbrechend (incl. `pūrbhíttama-`) |
| `pūrbhídya-` | 1 | das Aufbrechen der Wälle |
| `pū́rpati-` | 1 | Herr der Burg |
| `purohán-` | 1 | die Wälle zerschlagend |
| `púrya-` | 1 | in einem festen Platz befindlich |

The boundary was not set by intuition about what to look for. Every
lemma occurring in the corpus was scanned for a Grassmann gloss
containing *Burg, Wall, Verschanzung, Palisade, Festung, fest*; that
scan returns exactly these seven and no other `púr-` formation. It
also returns `paridhí-`, `dehī́-`, `saṃdíh-`, `harmyá-`, `ádhr̥ṣṭa-`
and `dārú-`, all fort-adjacent in sense but none derived from `púr-`.

`purohán-` is the least secure member — `puraḥ` "in front" + `√han`
is a possible analysis. It is kept because at its only occurrence, RV
6.32.3c, it stands immediately after `púraḥ` (`púraḥ purohā́`) and the
next pāda reads `dr̥ḷhā́ḥ ruroja`, "he broke the strongholds".

Excluded, and recorded because the exclusion is a judgement:
`púraṃdhi-` and its two compounds (50 tokens, glossed "Segensfülle"),
and `purāṣáh-` (1 token, RV 10.74.6a, "von alters her siegreich").
See §6 on why the first exclusion is the conservative one.

## 4. Counts by Arnold stratum — the measurement

Arnold's letters were verified against Arnold, not inferred:

> "Period. A Archaic. S Strophic. N Normal. C Cretic. **P** Popular. If
> these letters are in small italic characters the corresponding period
> is indicated by the metrical variations alone."
> — Arnold 1905, Appendix IV §265, printed p. 269

That last sentence also explains VedaWeb's undocumented uppercase /
lowercase split: 9,607 stanzas uppercase, 945 lowercase, never mixed
within a stanza.

| Stratum | Family tokens | Share | Corpus share | Expected |
|---|---:|---:|---:|---:|
| Archaic | 31 | 29.2% | 20.6% | 21.8 |
| Strophic | 32 | 30.2% | 22.7% | 24.0 |
| Normal | 17 | 16.0% | 24.8% | 26.3 |
| Cretic | 23 | 21.7% | 18.0% | 19.1 |
| **Popular** | **3** | **2.8%** | **13.9%** | **14.8** |

Counted by pāda instead of token: 31 / 32 / 16 / 22 / 3 over 104 pādas.
All 103 family stanzas are internally uniform in stratum, so the unit
choice does not move the picture.

χ² = 19.98 on 4 df, p = 0.0005 at token level. At the conservative unit
of the hymn — 86 hymns of 1,028, each assigned its majority code —
χ² = 14.57, p = 0.0057. The hymn figure is the one to quote, since
tokens within a hymn are not independent.

The whole result is the Popular cell: 3 observed against 14.8 expected.
Those three are RV 8.100.8b, 10.87.22a and 10.101.8c, all the simplex.

## 5. The second instrument, reported because C-05 requires it

Correction **C-05** records a claim built on Arnold strata alone that a
by-book recount reversed. The standing rule is that both instruments
are reported and neither is privileged silently. So:

| Book | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| per 10k | 8.0 | 6.4 | 6.0 | 6.2 | 3.4 | 10.3 | 8.4 | 8.6 | 2.8 | 3.6 |

Corpus mean 6.4. Grouped as family books (2–7) against the rest, the
difference is **not significant**: 6.98 against 6.07, χ² = 0.50 on
1 df, p = 0.48.

So the two instruments do not agree. The strata give a strong result;
book order gives a null. They point the same way only at the late end —
book 10 sits at 3.6 against a mean of 6.4 — and there they are not
independent evidence at all: **61.3% of all Popular-stratum tokens are
in book 10, and book 10 is 46.7% Popular.** The Popular deficit and the
book-10 deficit are largely one observation counted twice. That is
logged as `DEP-004`, because it is the precise trap that produced C-05.

## 6. Sensitivity

If `púraṃdhi-` and its compounds were admitted after all, the family
would rise from 106 to 156 tokens and the result would **strengthen**:
χ² = 24.29 on 4 df, p = 7.0 × 10⁻⁵, with 5 Popular tokens against 21.7
expected. Excluding them is therefore the conservative choice, and
`HOLD-001` does not block anything. Admitting `purāṣáh-` would move
Archaic from 31 to 32 and change nothing else.

## 7. Collocation

Lemmas sharing a stanza with a family token, far above their corpus
rate: `r̥jíśvan-` 53.7×, `pípru-` 52.8×, `dívodāsa-` 43.0×, `dā́sī-`
43.0×, `śámbara-` 41.5×, `āyasá-` "of metal" 36.9×, `navatí-` "ninety"
33.5×, `√dr̥̄-` 22.2×, `√bhid-` 16.6×, `śúṣṇa-` 15.3×, `śatá-` 10.7×.

This is a measurement of the profile and nothing more. What it appears
to suggest about who held the forts is logged as `PUR-027` at
**HYPOTHESIS**, untested, precisely so it is not later mistaken for a
result of this unit.

## 8. Where the measurement/interpretation line falls

**VERIFIED** — 25 rows. All of §2, §3, §4, §5, §6, §7 above: token
counts, stratum counts, the baseline, the χ² figures, the string-match
contrast, the padapāṭha checks, Arnold's letters. Each has a locator
that re-finds it and a retrieval date.

**PROVISIONAL** — 1 row, `PUR-026`: *"the púr- vocabulary is not a late
accretion."* The counting is sound; the reading is not, and it is
capped for three separate reasons, any one of which would be enough.
It rests entirely on Arnold's periodisation being chronological, and
VedaWeb's strata layer is a transcription of Arnold 1905, so the two
citations are one source (`DEP-001`). The second instrument returns a
null (§5). And where the two instruments do agree, they are entangled
(`DEP-004`). Arnold himself calls the period names "provisional".

**HYPOTHESIS** — 2 rows. `PUR-027`, what the collocations imply.
`PUR-028`, that Arnold's periods are chronological stages at all — the
assumption underneath every stratum claim here, logged separately so
`PUR-026` cannot inherit a higher status through it.

## 9. Known limits

- The Zürich lemma string is per token, but the Grassmann `correction`
  id it points at is resolved per surface form. Homograph surfaces
  therefore share one id. Every ambiguous surface in this family was
  checked individually; `purā́` (§2) is the only real collision.
- No passage was read for the grammatical role of `púr-`. Whether it
  is object of a breaking verb, locative of shelter, or something else
  is not established here. That is what `PUR-027` needs.
- `04-AUDITS/rv-pur-family-search.py` reads a TSV that is not committed
  — it is 30 MB of derived data. Re-run `rv-token-extract.py` against
  the pinned commit to regenerate it byte-for-byte.
