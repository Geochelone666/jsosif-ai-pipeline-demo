# JSOSIF research pipeline: operational acceptance and release gates

**Audit snapshot: 2026-10-25 UTC.** This page documents a point-in-time
assessment; it does not update automatically or imply current provider health.
Use the linked CLI and Actions health artifact for fresh evidence.

## Implemented and checked offline

| Area | Evidence / behavior |
| --- | --- |
| 50-ticker collection | Each daily attempt keeps a full roster and independently captures market/RSS/fundamentals even after AI quota exhaustion |
| Quota fairness | Least-recently-ready prioritized first, deterministic daily tie rotation; no extra quota is created |
| AI spending | Model-scoped RPD/RPM/TPD/TPM ledger, bounded retries, budget exhaustion diagnostics, no pointless calls after local exhaustion |
| Cross-day reuse | Exact ticker/title/date/link decisions only, at most two dates old, from ready and source-SHA-verified archives |
| AI backup | `GROQ_FALLBACK_MODEL` is optional; not enabled by this code rollout; no bypass of provider limits |
| News quality | Seven-day RSS ingestion; source diversity/time-age metadata; unknown/irrelevant counts; explicit abstention and semantic review flags |
| Historical risk and fundamentals | Eleven additional source-derived metrics with sample, currency and unavailable-data limitations |
| PDFs | A4, source hyperlinks, repeated table headers, concise print glossary, source dates and classification provenance; structural PDF validation before archive |
| PDF visual QA | Re-rendered 50 immutable 2026-10-24 source snapshots offline; all passed structural checks; first-page median text extent 25.2% → 90.5%, mean pages 6.1 → 4.76 |
| Release safety | Archive/source hashes, strict ready coverage gate, source-date checks, immutable historical versions |
| Personalized delivery | Existing member-week idempotency ledger, per-recipient preferences, preview mode, approved-send requirement and SMTP uncertainty handling |
| Observability | Action artifacts with per-ticker failure categories, exact source integrity, classifier counts and model reuse totals |
| Regressions | Offline Python, live-like synthetic PDF generation and browser smoke tests are required for code merges |

## Still required for true production sign-off

1. A new scheduled production run on the latest main branch must show
   **50/50 ready**, or explicitly justify acceptable incomplete coverage.
   The last archived 2026-10-24 business-date run showed **37 ready, 13 degraded**
   from a previously deployed version. The new changes do not rewrite that run.
2. Real Groq/Google provider limits must be verified at the **project** level.
   The Groq free-tier model's published 200K tokens/day is not sufficient to
   promise 50 fresh full model classifications on each date without reuse or
   explicitly authorized alternative capacity. Optional backup remains off
   until configured and separately confirmed.
3. Human reviewers need to label a representative 200–400 item sample,
   including ambiguity and irrelevant cases, **blind to model predictions**.
   Until then, rule `0.8` confidence and model self-reported confidence
   must not be advertised as validated correctness probabilities.
4. End-to-end recipient-specific sending, delivery receipts, and deduplication
   must be verified with authorized synthetic/self-test recipients before
   broad rollout. No production mailing is triggered by a code merge.
5. The PDF render checks prevent structural faults, but typography on the
   deployment's precise renderer and long non-English/special-character
   sources still benefit from a human spot-check.

## Safe operator commands

```bash
PYTHONPATH=scripts python -m pytest --import-mode=importlib -q
python scripts/production_health.py --store ../report-store \
  --json-out /private/health.json
python scripts/check_release.py --store ../report-store --require-ready
python scripts/pdf_quality.py --pdf reports/AAPL-intelligence-20261024.pdf \
  --ticker AAPL --as-of 2026-10-24
```

For review calibration use:
```bash
python scripts/build_news_review_queue.py sample \
  --root ../report-store/archive/<run-id> --count 300 \
  --out /private/review.csv
python scripts/build_news_review_queue.py finalize \
  --review-csv /private/review.csv --gold-json /private/gold.json
python scripts/eval_news_classification.py --gold /private/gold.json
```

Use the daily workflow's `resume=true` dispatch **only when explicitly
recovering the same business date**; it reuses verified ready versions and
recomputes still-degraded versions. Do not repeatedly force production runs,
change paid API configuration, or bypass strict release acceptance to make a
dashboard display 50/50. The delivery workflow has separate locking and state;
do not conflate 'pipeline complete' with 'member email received'.

Detailed runbooks: [Groq quotas](groq-quota-runbook.md),
[news reuse](news-reuse-runbook.md), [PDF validation](pdf-quality-runbook.md),
[human label evaluation](news-classification-evaluation.md), and
[research data dictionary](research-data-dictionary.md).
