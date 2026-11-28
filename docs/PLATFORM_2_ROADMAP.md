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
| Team-approved signup | Auth signup UI plus explicit approval; named-admin approval/revocation RPC and private review CLI implemented locally; invitation/approval UI and live acceptance pending |
| Administrator member correction | Named verified admin permissions, shared preference validation, optimistic versions, exact retries and private before/after audit implemented locally with inspect/review/apply CLI; hosted admin UI and team acceptance pending; see SUBSCRIPTION_ADMINISTRATION.md |
| Legacy JSON/CSV migration preserving member IDs | Offline private, rollback-by-default fresh-authority review generator implemented; exact IDs/opt-outs and verified-identity/revision/non-overwrite guards tested. Real reviewed map, import acceptance and incremental migration pending; see SUBSCRIPTION_MIGRATION.md |
| Unknown security request queue | Implemented locally: own-request RLS, portal submission/status, bounded duplicate-safe queue and backend versioned review audit; live acceptance and automated listing/source/cost onboarding pending |
| One authoritative sender configuration | Implemented locally, opt-in; real service credential, source switch and integration acceptance pending |
| Verified release records / website What's new | Implemented locally; catalogue intentionally empty |
| Relevant announcement in next eligible weekly mail, deduplication | Implemented locally; bounded selection, reservation before SMTP, uncertain-outcome suppression |
| Live authenticated portal access / publication | Pending team-project acceptance; default site build emits a disabled portal |

## Phase 2 — shared research foundation

Existing V1 has market/SEC/FRED/peer collectors, frozen stock snapshots and source
archives. These are prerequisites, not completion of the new shared data layer.

| Requirement | Remaining implementation |
| --- | --- |
| Stock/Sector/Industry/Peer/Macro identity model | Deterministic retrospective evidence package implemented locally with units, currency provenance, explicit missing timestamps and verified source references; formal listing identities and point-in-time evidence pending; see SHARED_RESEARCH_PACK.md |
| FRED and Bank of Canada adapters | Archived FRED/SEC and captured BoC USD/CAD integrated into local evidence package; BoC single-window live/cache acceptance recorded below; shared live refresh and historical vintages pending |
| Sector benchmark and ETF-relative performance | Standalone capture, exact-batch cache/local quota, offline candidate review and optional five-page sector appendix implemented; aligned endpoints/currency and explicit period/coverage gaps. Unified provider-wide refresh, approved/current/full coverage and formal listing review pending; see SECTOR_BENCHMARK_APPENDIX.md |
| Industry KPI templates / peer universe | Team-reviewed mapping; do not infer eight team identities from Yahoo sector labels |
| Validated security onboarding | Identity/listing checks, quality/cost gates and Pending/Active transitions |
| Shared cache and failure isolation | Standalone benchmark exact-batch cache binds provider/version, symbols, window and adjustment contract; local reservations survive failures/crashes, invalid entries refresh within quota, corrupt budget state fails closed. Cross-provider budgets, per-instrument reuse and production integration pending; see BENCHMARK_CACHE.md |

The team delegated the taxonomy choice. Eight configurable product defaults now
cover all 50 instruments exactly once; benchmark candidates and KPI research
topics are defined in config/research_teams.json. Shared price observations and
relative-return contracts reject missing endpoints, inconsistent adjustment bases
and unsupported currency comparisons. Shared evidence acceptance covers 50 latest
archived stocks at the 2026-11-13 cutoff. A separate retrospective candidate review
now computes individual comparable stock/ETF pairs from retained adjusted-price
captures; Consumer candidates stay separate and currency mismatches remain gaps.
The optional benchmark batch cache preserves original retrieval evidence and
shares a durable local adapter-call allowance across processes. Unified live
refresh, approved benchmarks, complete/current benchmark coverage and company
KPI evidence remain pending.

## Phase 3 — sector intelligence and email assembly

Implemented locally: eight independent four-page Sector Weekly Brief **drafts**,
with group-specific coverage/KPI research topics, stock industry context and up to
five sourced peer snapshots. Deterministic JSON companions preserve full evidence
and missing fields. See SECTOR_BRIEFS.md. These retrospective drafts always have
delivery readiness false; they are not completed current weekly intelligence.
An optional fifth page now projects retained candidate benchmark evidence with
explicit observation windows and source links. The private preview validates
version-two bundles; default four-page artifacts remain byte-compatible. See
SECTOR_BENCHMARK_APPENDIX.md.

Offline private member attachment selection, per-member content deduplication and
encoded-MIME size review are implemented locally; see MEMBER_ATTACHMENT_PREVIEW.md.
They preserve content opt-in, pause/schedule rules and explicit draft gates, with
no sender or ledger integration.

An independent two-page macro overview draft is implemented locally from verified
FRED/BoC archive evidence. Source ages, missing/latest-date conflicts and complete
lineage remain explicit. Private attachment review requires separate macro consent
and a draft switch, plus matching stock snapshot hashes; see MACRO_OVERVIEW.md.

An archive-backed news evidence index is implemented locally; see NEWS_EVIDENCE.md.
It retains exact RSS identities, UTC publication metadata, per-stock saved prediction
references, source hashes and explicit unmatched/conflicting evidence. Publication
dates do not establish event occurrence dates. Standalone four-page news review
drafts and separately opted-in private attachment previews are implemented locally;
see NEWS_REVIEW.md. The archive-wide draft is not personalized or live-accepted
news intelligence and remains ineligible for production delivery. Optional private
news scoping by effective holdings is implemented locally, preserving archived
report associations without inferring relevance; see SCOPED_NEWS_PREVIEW.md.

Pending: live-complete sector briefs; verified, sourced catalysts/events;
authorized attachment delivery integration; controlled-link fallback for oversized
messages. Existing 20 MiB message gating
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

Main now contains the foundation, security queue, offline migration review and
administrator correction integrations (#63–#66). The current research integration
candidate combines the remaining shared evidence, sector/macro drafts and private
attachment previews on that base; see MAIN_RESEARCH_INTEGRATION.md. Tests provide
implementation evidence, not production acceptance. This register intentionally
leaves unfinished PDF goals open.

### Macro adapter progress

A Bank of Canada Valet USD/CAD CLI and shared date-window cache are implemented
with synthetic parser/failure/concurrency tests. Local real-endpoint acceptance
on 2026-11-14 obtained five observations for 2026-11-02 through 2026-11-06 and
verified cache replay; the public capture is retained as a regression fixture.
Contradictory provider metadata fails closed. This single-window check is not
acceptance of all macro series or historical coverage. It is not enabled in
production or used for inferred FX conversion. Archive publication now retains
expected source checksums for verification before creating the public projection.
