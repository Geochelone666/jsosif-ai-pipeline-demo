# Research and private draft review integration

This candidate brings the previously reviewed research deliverables onto main at
`0473e9b35a7f8fbbe0c040015c9028892c4ff739`. It combines the following unmerged
increments in one reviewable change; it does not activate production delivery.

| Source PR | Source commit | Increment |
| --- | --- | --- |
| #55 | `d8b0ccd900ce86f81c55a23bbe3627f42345f747` | Captured BoC contract validation |
| #57 | `d3df8b02fb207b4d19488e6955e6db267ea36409` | Shared retrospective research evidence |
| #58 | `73887fa5aab27bc5f440ba2f487bad1cc206f616` | Eight independent sector brief drafts |
| #60 | `9f7655f95000c8d3085d34d69a0b760e76381c6a` | Private offline member attachment previews |
| #67 | `741a76dd9b4216376b4f55c15c494f24730e7046` | Standalone macro overview and optional preview attachment |

The integration starts from current main rather than replacing it with the old
feature branch. Main already contains the foundation, security queue, migration
review and administrator correction changes from #63–#66, plus independent
release and news classification fixes.

## Preserved main behavior

The daily and weekly production workflows, strict pre-deploy release checks,
Pages artifact discoverability wait, explicit target-led price-move classification,
sender, delivery ledger, all configuration files and Supabase migrations are
byte-identical to the stated main base. Subscription backend defaults and the
empty release announcement catalogue remain unchanged. Only the offline test
workflow gains research artifact builds and the configuration files needed to
reproduce those builds.

Imported Python and fixture files are byte-identical to the source feature tip
`741a76dd9b4216376b4f55c15c494f24730e7046`. No alternative implementation of the
main subscription changes or production release guards is introduced.

## Integration acceptance

Local regression on Python 3.12: **1,222 tests and 57 subtests passed**. This includes
main's strict release and price-move regression cases as well as the imported
evidence, sector, macro and private attachment cases.

Rebuilding the fixed 50-stock archive at cutoff 2026-11-13 produced byte-identical
shared evidence, eight four-page sector PDFs and companions, the two-page macro
PDF and companion, and private previews compared with their prior acceptance
artifacts. Those PDF bytes retain the prior visual acceptance; this integration
does not claim a new visual review or current market data. All 551 input archive
files and the synthetic member configuration were unchanged.

Five synthetic members produced three private previews with 2, 3 and 6 attachments;
two were skipped by pause/schedule rules. One preview retains an explicit missing
news-content gap. Each prepared preview contains exactly one macro draft. Directory
0700 / file 0600 permissions, independent draft opt-ins and false delivery readiness
were verified. No real members, provider refresh, email or ledger operations were
used for this acceptance.

CI additionally runs browser acceptance and disposable PostgreSQL isolation,
concurrency and rollback-first migration checks. Its run-specific results belong
to the PR checks and delivery evidence, not to a claim of live team acceptance.

## Remaining delivery boundaries

The source PRs remain historical review references; this candidate does not merge
or close them. The integration itself still requires review and merge. Live team
Supabase acceptance, authorized migration/source switching, complete current-data
research, benchmark/KPI/event evidence, standalone news, controlled private links
and production attachment delivery remain pending. All generated research artifacts
remain retrospective drafts with `delivery_ready: false`.
