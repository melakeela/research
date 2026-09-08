# HOLD-009 — Arnold 1905 could not be read in this session

**Raised** 2026-09-07, domain A.
**Blocks** RCI-012, RCT-005, and any promotion of PUR-011 or PUR-013 that
depends on re-checking them.

## What is needed

E. Vernon Arnold, *Vedic Metre in its Historical Development*, Cambridge
1905 — specifically:

1. Appendix IV §265, the explanatory notes that give the stratum letters.
   `PUR-011` was verified against this page in an earlier session, from the
   archive.org scan `vedicmetreinitsh00arnouoft`, OBJECT 289.
2. Arnold's own account of **how he assigned the Popular period** — whether
   Grassmann's 1876–7 and Oldenberg's 1888 judgements were among his inputs.

## Why it is blocked

archive.org refused at CONNECT with HTTP 403 through the session egress
proxy, and `WebFetch` returned `EGRESS_BLOCKED` (`SRC-104`). The scan that
`PUR-011` cites was reachable when that claim was verified and is not
reachable now.

## What turns on it

`RCI-006` and `RCI-008` establish that Grassmann 1876–7, Oldenberg 1888 and
Witzel 1995 all concentrate their late-addition marks in Arnold 1905's
Popular stratum, and that the agreement is not the book-10 effect. The
direction of possible influence is fixed by publication dates: Grassmann and
Oldenberg cannot be following Arnold. Whether **Arnold was following them**
is the open question, and it is answerable only from item 2 above.

If Arnold built the Popular period partly out of Grassmann's and Oldenberg's
verdicts, the agreement measured in `RCI-006` is substantially one judgement
counted twice, and `RCI-012` would move from PROVISIONAL toward REJECTED as
a claim of corroboration — though the measurements themselves would stand
unchanged, as a description of how the layers relate.

If he did not, `RCI-012` strengthens toward VERIFIED.

## Negative-evidence typing

`NOT ACCESSIBLE`. The text exists, is out of copyright, is digitised, and was
reachable from this repository three days ago. Nothing about the historical
record is at issue; this is an egress policy.

## What would clear it

`archive.org` on the environment egress allowlist — already requested under
`D-043` for a different domain — or the owner supplying the two page ranges
as files.
