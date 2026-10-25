# Verified cross-day news decision reuse

**Goal:** reduce Groq requests on identical RSS stories without weakening source
integrity or inventing classifications. This is a deterministic evidence reuse
path, not an LLM-generated cache hit on semantically similar titles.

## Cache eligibility

A saved report may contribute decisions only if all conditions hold:

- It belongs to the exact ticker, is marked `ready`, and was generated
  **one or two report dates** earlier.
- The archived PDF, Markdown, snapshot JSON, and **all eight source files**
  pass their SHA-256 checks. Older archives that lack source digests are
  read normally but are **not eligible for cache reuse**.
- The original RSS fetch was successful and had no unresolved headlines.
- The new RSS article has an **identical headline, RFC822 publication-date
  string, and link**. Matching only the title is insufficient.
- Only AI-classified categories and explicit AI exclusions are replayed.
  New deterministic rules always run first and override an old classification.
- A cached item must still pass field-value checks before acceptance.
  Nonmatching or malformed items remain pending and go to the regular model,
  or are explicitly marked unknown if quota is exhausted.

The regenerated source item retains the **current RSS provider URL and metadata**,
records `reuse_origin=verified_prior_archive` and the original report date,
and reports the reuse count separately from fresh `models_used`. A previous
model identity may be disclosed as `prior_models`; it is **not** a new AI call.

## Limitations and controls

- This is not evidence that an article's claims were fact-checked. The original
  AI inference can itself be wrong; reviewed samples and source inspection
  remain necessary. Reuse does not add confidence to a model's score.
- Exact duplicate title/link/date across runs is acceptable, but changed
  titles, links or publication timestamps trigger fresh classification.
- A cache hit never repairs a missing market source or an incomplete RSS fetch.
  Existing strict ready/quality gates and duplicate-email safeguards remain.
- Reports archived before the digest rollout cannot be reused. The first
  complete new daily run seeds trusted source digests for subsequent runs.
- `JSOSIF_NEWS_REUSE_ENABLED=1` enables the cache on scheduled production.
  Omit it to disable. A fully disabled AI mode does not use this optimization.
- The site and email sender do not fetch external information and never
  regenerate historical report bytes in place.

## Verify effectiveness

The index stores per-ticker *candidate* counts under
`last_attempt.news_cache_candidates`. The actual accepted count is in each
ticker's saved `ai-intel.json.ai_reuse.reused_headlines`. Distinguish
candidates from accepted decisions: a story that has changed is not a hit.
Compare those counters and the Groq ledger across comparable trading days.
