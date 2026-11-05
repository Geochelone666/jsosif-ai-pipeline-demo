# Platform 2.0 delivery register

Scope: every goal in the team's seven-page AI Pipeline 2.0 plan. Current topology
is the existing personal GitHub repository plus team-owned Supabase. Repository
transfer is a future administrative operation, not a dependency for this release.
Do not describe local implementations or mock tests as production acceptance.

Statuses: **implemented locally** means code and local tests exist; **pending**
means there is no completed implementation/acceptance evidence. All new capabilities
still require review, deployment and actual integration acceptance.

## Phase 1 — member experience and announcements

| Requirement | Status / evidence |
| --- | --- |
| Own-account subscription read/write | Implemented locally: RLS, approved_members, versioned/idempotent RPCs; SQL isolation and concurrency checks |
| Email-code sign-in and session expiry | Implemented locally: subscriptions.html/js; isolated browser Auth fixtures; actual Supabase mail/session acceptance pending |
| Personal stock/group/day/time/timezone preferences | Implemented locally: existing validators, RPCs and browser editor; shared sender snapshot path |
| Pause and participation | Implemented locally; browser save and sender pre-reservation checks; in-flight SMTP cannot be recalled |
| Email changes | Auth request implemented locally; actual old/new mailbox confirmation and notification acceptance pending |
| Team-approved signup | Auth signup UI plus database approval requirement implemented locally; operational invitation/approval UI pending |
| Administrator member correction | Pending reviewed admin workflow/tooling; not exposed through member RPCs |
| Legacy JSON/CSV migration preserving member IDs | Compatibility and schema support implemented; real migration tooling, reviewed identity map and production import pending |
| Unknown security request queue | Pending; current UI and server reject unsupported activation |
| One authoritative sender configuration | Implemented locally, opt-in; real service credential, source switch and integration acceptance pending |
| Verified release records / website What's new | Implemented locally; catalogue intentionally empty |
| Relevant announcement in next eligible weekly mail, deduplication | Implemented locally; bounded selection, reservation before SMTP, uncertain-outcome suppression |
| Live authenticated portal access / publication | Pending team-project acceptance; default site build emits a disabled portal |

## Phase 2 — shared research foundation

Existing V1 has market/SEC/FRED/peer collectors, frozen stock snapshots and source
archives. These are prerequisites, not completion of the new shared data layer.

| Requirement | Remaining implementation |
| --- | --- |
| Stock/Sector/Industry/Peer/Macro identity model | Versioned shared model with units, currency, observation/publication/retrieval times and source references |
| FRED and Bank of Canada adapters | Reuse FRED; add reviewed BoC series, explicit missing data and source contracts |
| Sector benchmark and ETF-relative performance | Shared, budgeted observations with aligned calendars/currency and disclosed coverage |
| Industry KPI templates / peer universe | Team-reviewed mapping; do not infer eight team identities from Yahoo sector labels |
| Validated security onboarding | Identity/listing checks, quality/cost gates and Pending/Active transitions |
| Shared cache and failure isolation | Cache keys bind source, instrument and date; corruption recovery preserves quotas/history |

The team delegated the taxonomy choice. Eight configurable product defaults now
cover all 50 instruments exactly once; benchmark candidates and KPI research
topics are defined in config/research_teams.json. Shared price observations and
relative-return contracts reject missing endpoints, inconsistent adjustment bases
and unsupported currency comparisons. Real adapter/cache/KPI evidence remains pending.

## Phase 3 — sector intelligence and email assembly

Pending: eight team templates; independent Sector Weekly Brief; stock-specific
Sector Context and 3–5 peer snapshots; deterministic, sourced catalysts/events;
relevant sector attachment selection; per-member attachment deduplication;
controlled-link fallback for oversized messages. Existing 20 MiB message gating
remains in force. Public links must never be used as a substitute for an approved
access-control design for private research.

## Phase 4 — interactive workspace

Existing V1 report search/filters/history and local member editor remain available.
New authenticated subscription and What's new candidates are implemented locally.
An archive-backed Sectors/Compare/Macro workspace is now implemented locally,
with source-linked stock metrics, provider peers, macro observation dates and
explicit supplemental-source limitations. It is not a current-data dashboard.

Pending: unified Overview/Stocks/Sectors/Macro/Compare/Research Library navigation,
sector/macro time-series dashboards, adjustable peer comparisons, event calendar,
news/catalyst filtering and history charts. Each needs desktop/mobile, keyboard,
source-date and missing-data checks against actual validated shared observations.

## Phase 5 — advanced research intelligence

Pending: sector/portfolio exposures and factor-risk views, explainable anomaly
alerts, historical valuation percentiles, earnings expectation tracking, thesis
tracking and reproducible backtests. No unsupported price targets, causal claims
or investment recommendations. Features require suitable historical evidence and
explicit coverage/limitations before presentation as signals.

## Acceptance and operational dependencies

- Review the actual project's read-only inventory before any migration; retain
  Auth/Storage/platform objects. User-supplied inventory showed no Auth users or
  public business tables at that observation time, not a timeless empty-project claim.
- Apply reviewed SQL through an approved execution route. Do not run disposable
  SQL fixtures on the team project. Obtain and test service credentials securely.
- Verify cross-user denial, approval/revocation, real email confirmation, actual
  save-to-sender read-back and opt-out behavior on staging. Add the exact deployed
  callback to Auth redirect settings; homepage configuration alone is insufficient.
- Preserve report-data and delivery-state, stable member IDs, API reservations,
  immutable report hashes and ambiguous sending reservations throughout migration.
- Verify deployment and report quality separately. Verify backup restore, SMTP
  acceptance and inbox placement separately. Only reviewed deployed features may
  enter published release records.
- Production sends, paid services, real member import, source switch and destructive
  operations remain subject to the team's explicit authorization boundaries.

The local integration branch combines the two backend/announcement candidates
without merging them into main. New tests provide evidence for implementation;
this register intentionally leaves unfinished PDF goals open.
