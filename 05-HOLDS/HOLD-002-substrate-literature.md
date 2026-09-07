# HOLD-002 — the substrate literature itself is unretrieved

**Opened:** 2026-09-07
**Domain:** E (Dravidian, Munda and unidentified substrate claims)
**Ledger row:** `SRC-052`
**Blocks:** distinctions 8, 9 and 10 of constitution §4.E — Witzel's
Para-Munda, the Kubhā-Vipāś prefixing-language fallback, and Masica's
Language X.

## What is needed

| Work | Why it is load-bearing | Where it might be |
|---|---|---|
| Witzel, "Early Sources for South Asian Substrate Languages", *Mother Tongue* extra number, 1999 | the Para-Munda proposal itself | EJVS/Laurasian Academy site; archive.org |
| Witzel, "Substrate Languages in Old Indo-Aryan (Ṛgvedic, Middle and Late Vedic)", *EJVS* 5-1, 1999 | the prefix-segmentation argument and the word lists | EJVS site |
| Witzel 2019 (the "keeps the question open" position) | the current standing of the proposal by its own author | reached in this programme only via Mukhopadhyay 2021 — see `IH-231` |
| Kuiper, *Aryans in the Rigveda*, Rodopi 1991 | the foreign-word list that the site's substrate pages rest on | archive.org |
| Masica, "Aryan and Non-Aryan Elements in North Indian Agriculture", 1979 | the Language X residue | archive.org; JSTOR |
| Krishnamurti, *The Dravidian Languages*, CUP 2003 | the Proto-Dravidian reconstructions used at one remove as `SRC-046` | archive.org |
| Rau 2019 (Proto-Munda) | the reconstructions used at one remove as `SRC-048` | — |
| Shorto, *A Mon-Khmer Comparative Dictionary*, 2006 | the deeper-Austroasiatic comparanda carried inside `SRC-048` | — |

## Why it is blocked

Every plausible host is refused at the egress gateway in this session:
`archive.org` (`SRC-037`), `www.jstor.org` (`SRC-032`),
`www.ejvs.laurasianacademy.com`, `dsal.uchicago.edu` (`SRC-040`),
`gretil.sub.uni-goettingen.de` (`SRC-038`),
`titus.uni-frankfurt.de` (`SRC-039`). Both available channels — `curl`
through the container proxy and the `WebFetch` service — were tried.
The one open retrieval channel, the git proxy's anonymous lane
(`SRC-042`), serves public git repositories and nothing else.

## What this hold does and does not permit

**Permits.** Naming these proposals, stating their content as reported
second-hand, stating their evidential burden, and recording that the
burden is undischarged *in this record*.

**Forbids.** Any row that characterises what Witzel, Kuiper, Masica,
Krishnamurti, Rau or Shorto actually argue at `VERIFIED`. Any count of
"Kuiper's foreign words" or "Witzel's prefixed forms". Any claim that
Para-Munda has been refuted — non-retrieval of an argument is not
refutation of it, and the negative-evidence standard types this absence
as `NOT ACCESSIBLE`, which is the weakest kind of silence there is.

## The asymmetry this creates, stated plainly

The blocked side is not random. Attested Dravidian, reconstructed
Proto-Dravidian, attested Munda, reconstructed Proto-Munda and
Indo-Aryan all have machine-readable derivatives on GitHub and were
retrieved. Para-Munda, the Kubhā-Vipāś language and Language X exist
only as arguments in journal articles and monographs, and none of those
are reachable. So this session can measure five of the eleven
distinctions and can only report the other three.

That is a fact about the retrieval channel, **not** a finding about the
hypotheses. It would be a methodological failure to let "we could
measure Dravidian and could not measure Para-Munda" become "Dravidian is
supported and Para-Munda is not". The measurement registers are
therefore restricted to what was measured, and the hypothesis gate
(`03-REGISTERS/HYPOTHESIS-ELIGIBILITY.csv`) records this hold as the
reason certain gate cells read `UNTESTED-HERE` rather than `FAIL`.

## Escalation

Not an owner escalation under the controller's list: it is a network
policy question, already carried as `D-001`/`D-003` in
`DECISIONS-NEEDED.md`. Adding `archive.org` and `dsal.uchicago.edu` to
the egress allowlist would close most of it.
