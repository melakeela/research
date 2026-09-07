# Mela Keela / Veḷi — Claude Chat live-site audit prompt

**Prepared 5 September 2026.** Paste this into a fresh Claude Chat with web access before commissioning the research packets. Attach the current Mela Keela master work list and the language-research prompt pack. Do not attach a repository ZIP at this stage.

## Copy/paste prompt

You are conducting a read-only coverage and research-needs audit of the public Mela Keela / Veḷi museum at <https://melakeela.com>.

The public website is the baseline for what visitors can see today. It is **not** necessarily identical to the current development branch. Do not generate HTML, redesign the site, edit anything, log in, submit forms or deploy.

Start with these discovery routes:

- `https://melakeela.com/`
- `https://melakeela.com/enter`
- `https://melakeela.com/research-index`
- the site's Explore, Exhibits, Evidence/Ledger and Search routes;
- any sitemap or robots file that is actually reachable;
- all internal links discoverable from those surfaces.

The research index presently describes itself as the grouped list of public content pages. Verify its visible count and use it as the principal route inventory, but do not assume it is complete merely because it says it is. Record the crawl date. If JavaScript, access controls, robots policy, a tool limitation or an unlinked route prevents inspection, mark the route **INACCESSIBLE/UNKNOWN**, not absent. Distinguish:

`CONFIRMED COVERAGE | PARTIAL COVERAGE | PASSING MENTION | CONFLICTING COVERAGE | NOT FOUND IN PUBLIC AUDIT | INACCESSIBLE/UNKNOWN`

For every discoverable content page, record:

- URL, title, section/category and review-status badge;
- where it was discovered;
- questions and claims it currently addresses;
- evidence, source links, data or interactive elements exposed to the visitor;
- explicit caveats, corrections and “what would change this” statements;
- overlaps with other routes;
- claims that appear stronger than their cited evidence or require specialist checking;
- whether the proposed programme should extend, correct, merge with or sit beside it.

Reconcile the public site against every stable work-list ID in the attached master document, including the language, Rigvedic, BMAC/Oxus, resource-corridor and trade/raiding additions. Do not infer page absence from a title mismatch: read the relevant page. Do not infer full coverage from one paragraph that mentions a topic.

Pay particular attention to existing public coverage already likely to overlap the programme:

- Pāṇini/Tolkāppiyam and histories of grammar;
- the Sanskrit sound grid and Dravidian sounds;
- tiṇai and Tamil intellectual architecture;
- Rigvedic strata, patronage, enemies, forts and the “ninety-nine forts” treatment;
- Mitanni and Indo-Aryan material outside South Asia;
- Meluhha trade, Magan/Dilmun, Indus exchange and the Artifact Atlas;
- substrate vocabulary, lost languages, Brahui/Kurukh/Malto, the northwest Dravidian pages and named peoples;
- the Strait/Gulf, lapis, carnelian, the ninety-nine forts and ancient-to-modern corridor claims;
- source/correction/ledger pages.

Treat every supplied historical assertion as a research hypothesis, not an instruction to confirm it. In particular, do not publish as settled: a Dravidian etymology of *kīnāśa* from Tamil *kiṇṭu*; a BMAC origin for Vedic/Avestan religion; a Greek borrowing of Indian phonetic theory; an Elamo-Dravidian identity for BMAC or Indus languages; an identification of Rigvedic forts with a specific excavated culture; or a general claim that Tamil is harder for AI than other languages. Report what evidence would decide each question.

Return a downloadable ZIP named `MK-live-site-audit-2026-09-05.zip`. Do not create production HTML, CSS or JavaScript. If you cannot create a ZIP, return the same files separately with the exact filenames below.

```text
MK-live-site-audit-2026-09-05/
  README.md
  crawl-log.csv
  route-inventory.csv
  programme-coverage.csv
  current-claim-risks.csv
  overlap-and-merge-map.csv
  research-priorities.md
  preliminary-route-disposition.csv
  research-inputs/
    R1-current-public-coverage.md
    R2-current-public-coverage.md
    ...
    R19-current-public-coverage.md
```

Required fields for `programme-coverage.csv`:

```text
work_id,topic,current_url,coverage_status,current_claim_summary,evidence_present,correction_needed,research_needed,provisional_disposition,research_packet,notes
```

Required fields for `current-claim-risks.csv`:

```text
url,claim_excerpt_or_paraphrase,risk_type,why_review_needed,source_visible,required_check,affected_work_ids
```

In `research-priorities.md`, divide the result into:

1. corrections to existing public pages;
2. extensions to existing public pages;
3. genuinely new investigations/pages;
4. shared features or datasets that should serve several pages;
5. research holds requiring primary-source or specialist work;
6. probable duplicates that should not become separate pages.

End with a recommended packet order and identify which packets can run concurrently. This audit authorizes research planning only. Every route decision remains provisional until Claude Code later reconciles the public audit with the current repository branch, routes, data, components and correction history.

## What to do with the audit ZIP

Use the audit's `research-inputs/R#-current-public-coverage.md` in the corresponding bounded research chat. After the reviewed packets exist, give the audit and packets to Claude Code for a read-only repository reconciliation before any implementation.
