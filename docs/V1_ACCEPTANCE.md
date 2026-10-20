# V1 prelaunch acceptance evidence

Recorded on 2026-10-19. This document distinguishes simulated business checks from
real external integration and deployment acceptance.

| Check | Evidence | Result |
| --- | --- | --- |
| Full offline regression | Python 3.12, pinned development dependencies, `PYTHONPATH=scripts python -m pytest --import-mode=importlib -q` | 703 passed |
| Full portfolio rehearsal | 25 holdings, 30 synthetic Excel members, three timezones, two simulated weeks; external source stages and SMTP replaced with fixtures | Passed |
| Personalized messages | 29 private previews, five attachments for the first member, individual choices, one opted-out member, no real SMTP submission | Passed |
| Delivery recovery | Duplicate scans, expired reports, an uncertain submission and later scans that continue to flag reconciliation | Passed |
| Historical retention | Two simulated collections retained 50 versions and original hashes | Passed |
| Remote archive recovery | Fresh clone of `report-data`; all 25 pre-existing historical versions verified | Passed |
| Browser acceptance | Chromium: history inspector, filters, refresh, CSV import/export, invalid-import preservation and mobile layout; no JavaScript errors | Passed |
| Public-site verification | Real local HTTP server: expected date, publication metadata, coverage and file hashes; broken PDFs and stale publications rejected | Passed |
| Workflow structure | All five workflow YAML files parsed; branch review still precedes GitHub execution | Passed locally |
| Runtime dependencies | `pip check` in the pinned environment | Passed |
| Authenticated Groq and source access | Current development runtime has no injected Groq key and has not applied saved source-domain configuration | Not verified here |
| Gmail authentication | No Gmail credentials in the current runtime; the new live workflow authenticates without submitting a message | Not verified here |
| Current-day production collection | Restored remote store had historical reports only and no recorded daily attempt | Not passed |
| Public Pages deployment | Requires a current successful production collection and deployed HTTP verification | Not verified here |
| Inbox placement | No real email was sent during this acceptance work | Not tested |

## Fixes covered by this update

- Report freshness uses Toronto dates while member delivery uses each member's
  own timezone. UTC midnight no longer rejects a same-day Toronto report.
- Due deliveries without eligible reports fail visibly and leave their slots
  retryable. Uncertain or interrupted submissions remain visible on later scans
  without automatic resubmission.
- Release verification requires the expected daily date and a complete strict
  run; a healthy historical store cannot stand in for today's successful update.
- Deployment verifies real HTTP responses and hashes after Pages reports success.
- Provider credentials never follow redirects. Groq pacing across UTC midnight
  charges the correct application day. A persistence failure after a successful
  HTTP response does not trigger another API call.
- Invalid AI summaries remain unclassified; batched Groq responses are normalized
  before merging, using the same schema checks as single batches.
- Offline tests isolate live credentials. CI includes the report-compatibility
  checks and a repeatable desktop/mobile browser job.
- Empty or entirely opted-out rosters leave the weekly workflow idle. Invalid
  private configuration cannot enable delivery.

## Remaining acceptance sequence

1. Merge the hardening change and require the offline and browser CI checks.
2. Check the automatically started **Live launch acceptance (no email delivery)**
   artifact. It makes one real Groq request and independently checks sources,
   Gmail login, production switches and the deployed site. No roster is needed.
3. Correct only the blocked settings. Run **Daily production research pipeline**
   and inspect its strict acceptance result and deployed verification. Use `force`
   only to recover an already attempted date after correcting its cause.
4. After reviewing and removing any old test roster, arm
   `PAGES_DEPLOY_ENABLED=true` and `EMAIL_DELIVERY_ENABLED=true`, then rerun live
   acceptance. A missing or empty roster remains idle.
5. Import the reviewed formal Excel roster, inspect private previews and update
   the repository's private roster Secret. Subsequent scans use enabled members'
   settings automatically; new holdings enter the next daily collection.

See [V1 launch and operations](V1_LAUNCH.md) for settings, commands, recovery and
scope. Do not describe this release as waiting only for member information until
the real integration and deployment checks have passed.


## Post-merge live follow-up

Follow-up on 2026-10-19 using repository Secrets in GitHub Actions:

| Integration | Observed result |
| --- | --- |
| Groq authenticated JSON | Passed with `openai/gpt-oss-20b`; the old default was unavailable |
| Market history | Passed |
| Google News RSS | Passed |
| SEC directory | Passed using the configured sender as the contact identity |
| Gmail STARTTLS/login | Passed; no email submitted |
| Isolated real CSCO report | Strict check passed: one current report, no degraded holdings or integrity errors |
| Real news extraction | 24 unique headlines; 3 rule classifications, 14 AI classifications, 7 retained unclassified |
| Isolated report artifacts | Markdown, JSON, PDF and static site preview generated in temporary storage |
| Production website | Blocked: Pages uses `main/docs`; production data URLs return 404 |
| Production switches | `PAGES_DEPLOY_ENABLED` and `EMAIL_DELIVERY_ENABLED` were false |

The isolated real-report run is
[39306349643](https://github.com/Geochelone666/jsosif-ai-pipeline-demo/actions/runs/39306349643).
Its `research_smoke` job succeeded; the separate `verify` job correctly failed for
the remaining deployment/switch settings. This is not a failed CSCO generation.
The temporary report did not change the production `report-data` branch and did
not consume today's automatic collection slot. A complete 25-holding daily run,
production Pages verification and an explicitly authorized inbox test are still
required. The code follow-up is tracked in PR #6.

The follow-up also enforces request/token caps with a rolling-minute reservation
window. Successful calls reconcile both daily and rolling token usage; failed
calls retain their reservation. This avoids both unnecessary waits based on a
byte-bound estimate and bursts that average-rate spacing alone would permit.

Latest local follow-up regression: 714 tests passed with pinned Python 3.12 dependencies.

## First complete production collection

Run [39312761141](https://github.com/Geochelone666/jsosif-ai-pipeline-demo/actions/runs/39312761141)
collected and archived all 25 holdings on 2026-10-19 and deployed the site. The
persistent store retained 50 report versions: 25 historical and 25 new. No source
stage failed outright, but strict acceptance correctly failed because 12 new
reports had degraded news evidence. The durable ledger recorded 59 Groq attempts
and 49,519 tokens for that UTC application day.

Observed causes included listing-identity mismatches, three extraction failures
associated with failed report-store pushes, successful empty RSS queries and
headlines left unclassified when the model skipped them without an explicit
relevance decision. A successful later trigger that skips collection does not
replace this degraded result with a ready publication.

The recovery change adds strict listing-bound output, explicit irrelevant-news
records, honest quiet-day status, lower-frequency durable API checkpoint pushes,
bounded transient push retries and preservation of the evening scheduled slot
after an earlier manual acceptance run. All original report versions remain intact.

Recovery regression evidence: 750 tests passed with pinned Python 3.12 dependencies.
The quiet-day report also passed real PDF rendering and Chromium desktop/mobile
checks. A two-week synthetic roster rehearsal verified the internal self-preview's
five attachments and confirmed that previewing did not change the delivery ledger.

## Full isolated acceptance timing follow-up

The first isolated full-portfolio recovery run
[39439070045](https://github.com/Geochelone666/jsosif-ai-pipeline-demo/actions/runs/39439070045)
hit its 90-minute job limit before the strict release check. It supplies no proof
that all 25 current reports are ready. A subsequent latest-code CSCO check in
[39448205363](https://github.com/Geochelone666/jsosif-ai-pipeline-demo/actions/runs/39448205363)
passed strict acceptance: 23 headlines, 2 rule classifications, 18 AI
classifications, 3 explicit irrelevant decisions and no unclassified headlines.
The research job passed; the separate live verification still failed for the
existing degraded production site and intentionally disabled email switch.

The isolated job now has the same 120-minute ceiling as production, with a
110-minute collection-step limit to leave time for partial evidence checks and
artifact upload. Each completed holding records per-stage durations; acceptance
reports include those durations and safe API request/token totals. An interrupted
collection remains unready. The index artifact is retained even if site building
fails. These diagnostics do not turn a timeout into a successful release.

## Pending-run preservation

GitHub's default concurrency group retains only one pending run even when
`cancel-in-progress` is false. A later workflow can therefore replace a waiting
daily refresh or member delivery scan. The existing shared store/API group now
uses `queue: max`, preserving up to 100 pending runs while retaining a single
active writer. GitHub documents this behavior in its
[concurrency reference](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency).
Queueing prevents replacement; it does not guarantee exact dispatch times.

Live queue validation on 2026-10-20 retained all three test runs
`39480403715`, `39480448767` and `39480453534` in the pending state behind an
active run. None replaced another. After observing the three pending runs, they
were explicitly canceled as test cleanup before executing their API probes.
The cancellations are expected cleanup, not failed provider checks.

Same-day earnings regression checks also passed: a scheduled date of today stays
visible when actual EPS is missing; a reported result today becomes the latest
past event and is not reintroduced by the calendar fallback; an unavailable
results table can still retain today's scheduled calendar date.

Peer configuration was also reviewed against the archived SEC company directory.
`JNPR`, `ETFC` and `K` are absent, and `PARA` now identifies Banzai International,
not the intended media peer. They were replaced with currently listed sector
peers `FFIV`, `LPLA`, `KHC` and `PSKY`. Convenience-store peers now use `CASY`,
`MUSA` and `SUN`; the unrelated `ANDE` and legacy `PKI.TO` were removed. OpenText's
CGI peer uses SEC-listed `GIB` (CGI Inc), replacing the different Canadian
investment-company symbol `CGI.TO`. Currency labels remain per issuer; monetary
amounts in different currencies must not be ranked as if converted. All current
US peer symbols are present in the archived directory. Listing and sector
membership still require periodic review; a symbol can be reused.

SEC listing resolution now uses explicit verified dual-listing aliases instead
of removing `.TO`. The archived directory confirms `MG` is Mistras
(CIK 1436126), while Magna uses `MGA` (CIK 749098). `JWEL` is Jowell Global,
not Jamieson Wellness. `MG.TO` now resolves through `MGA`; unverified foreign
mappings including `JWEL.TO` and `ATD.TO` return unavailable rather than querying
a different issuer. Seven listing-identity regressions passed. The isolated
acceptance input also supports a comma-separated subset for focused source and
configuration regression runs; all entries must remain supported holdings.


Archived foreign-issuer checks are now separate from immutable file integrity.
The real 50-version archive contains two affected October 19 versions: `MG.TO`
with Mistras SEC data and `JWEL.TO` with Jowell's issuer identifier. Site builds
annotate those versions with a correction notice; strict current-release checks
and email selection reject them. Original PDFs, JSON, Markdown and hashes remain
unchanged. A corrected latest version can pass while the annotated original
remains accessible in history. Verified Canadian aliases are also bound to their
expected SEC CIK, preventing an alias reused by another issuer from being accepted.

Chromium checks passed against all 50 real archived versions, including the
correction filter, report inspector, ready-only exclusion and mobile layout.
The smoke script no longer assumes that CSCO has only one historical version.
CI also exercises a synthetic repeated version and wrong-issuer correction case;
that 26-version browser fixture passed locally. No real member data or messages
were used. The complete pinned regression suite passed 750 tests.

During rollout, the corrected-source run `39482375158` was canceled by a waiting
scheduled workflow still using the main branch's old shared concurrency policy.
It completed seven holdings without degraded or failed reports before cancellation,
but did not complete strict portfolio acceptance. Read-only live/API checks now
use a separate `jsosif-ai-acceptance` queue. Production archive/delivery writers
retain `jsosif-report-data` with `queue: max`, applied at job level after the main
branch and schedule/enable gates. Disabled or irrelevant jobs therefore do not
join the writer queue. The two queues share provider account quotas even though
isolated checks never write production state. Weekly member delivery also requires
main, so unmerged code cannot submit member email through that workflow.

## Structured-generation recovery

The first main collection after PR #7 observed a real `V` news failure: Groq
returned HTTP 400 / `json_validate_failed` for a five-headline structured request.
RSS and market sources were available. The report was retained as degraded and
remained ineligible for normal delivery. A specific safe diagnostic identifies this as a structured-generation failure.

The follow-up retries only that specific generation error with successively
smaller headline batches, retaining the same strict listing-bound schema.
Each request still passes through durable request/token reservations. A failed
single-headline request stops; credential, request, rate-limit and exhausted-budget
errors are not split into extra requests. CI recovery notices include only the
symbol and batch sizes. Failed-generation content and provider response bodies
remain private. Offline tests cover recursive recovery, complete relevance-decision
preservation, bounded persistent failure and listing-identity rejection.
