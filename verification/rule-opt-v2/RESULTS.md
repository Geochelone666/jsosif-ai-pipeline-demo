# JSOSIF rule-opt-v2 Comparison Report — 2026-10-05

Explored only on the local `rule-opt-v2` branch; no merge, push, Notion operations, model/API calls, or added credentials.

## Metrics

Same six companies' cached news: 150 inputs, 147 after deduplication by company.

| Metric | v1 | v2 | Change |
|---|---:|---:|---:|
| Rule coverage | 41/147 = 27.89% | 74/147 = 50.34% | +22.45 pp |
| AI candidate headlines | 106 | 73 | -33 |
| Historical AI category agreement | 11/24 = 45.83% | 21/29 = 72.41% | +26.58 pp |

Met the targets of ≥50% coverage and ≥70% historical AI agreement on this cached set. On the 23 commonly comparable headlines, agreements rose from 11 to 16 (47.83% → 69.57%); the denominator for overall agreement also shifts with coverage.

Historical AI has only four category labels, not human ground truth; this does not represent event/sentiment extraction accuracy nor generalization to new data. Rules were developed and evaluated on the same cached set — exploratory results with no held-out set; online fallback not verified. Fewer headlines does not necessarily mean fewer API calls (the original pipeline already batches).

## Miss Analysis and Changes

v1's 106 misses included verb inflections (rise/dropped/raised), earnings beat/miss phrasing, rating and price-target adjustments, institutional buy/sell holdings, Chinese company aliases, and factual statements followed by commentary questions. Most of the rest were price predictions, valuation speculation, questions, or conflicting signals.

Added or expanded:
- Company matching: ticker, GOOG, Amazon.com, Azure, plus Nvidia, Microsoft, Apple, Google, Amazon, Tesla; English word boundaries preserved to prevent Pineapple matching Apple.
- Events: M&A, spin-off/stock split, buyback, dividend, guidance, rating/price-target, institutional holdings, explicit calendar reminders, and specific risks; earnings beats/misses estimates and cuts/raises guidance directly recognized.
- More specific company events take precedence over generic earnings/stock vocabulary; product, buyback, split announcements as catalysts; rating upgrades/downgrades keep direction.
- Factual statements followed by commentary questions are recognized, but leading predictions, conditional mood, and conflicting signals still fall back; fixed competitor stock moves being attributed to the target company, and "falls shy" being treated as a decline.
- Institutional holding buys/sells are neutral events; no inference about company outlook; summaries still copy headlines without fabricating information.

Event distribution of new rule hits: {'risk': 3, 'analyst': 4, 'market_move': 18, 'calendar': 1, 'ownership': 6, 'product': 1, 'partnership': 1, 'earnings': 3}.
Event distribution of the 73 still-falling-back: {'market_move': 48, 'earnings': 3, 'unknown': 10, 'buyback': 1, 'stock_split': 1, 'workforce': 1, 'analyst': 2, 'product': 6, 'guidance': 1}. Per-item v1/v2 classifications, historical labels, and remaining misses are in `comparison.json`.

| Company | v1 hits/total | v2 hits/total |
|---|---:|---:|
| NVDA | 7/25 | 10/25 |
| MSFT | 5/23 | 11/23 |
| AAPL | 5/25 | 13/25 |
| GOOGL | 8/25 | 10/25 |
| AMZN | 6/24 | 13/24 |
| TSLA | 10/25 | 17/25 |

## Schema and Verification

Kept the four category arrays and all original fields, including `extraction_method=rule/ai/unknown`, RSS metadata, unclassified list, and stats. Event vocabulary added ownership/calendar/risk; field structure is compatible, but if external consumers hardcode the event_type enum, they need to sync the new values. impact/horizon remain conservative fixed defaults.

Reproducible commands that passed:

```bash
python3 -m unittest -v test_ai_extract test_rule_opt_v2
python3 verification/rule-opt-v2/compare.py
python3 verification/rule-opt-v2/check_reports.py
```

All 4 original tests passed; 3 new parameterized tests cover event phrasing, aliases, conflict/prediction, dates, and fields. Reports are byte-identical when only metadata was added for the six companies; all v2 output reports render; the existing validate_phase1.py in the isolated directory passes. All verification completed offline.

## Branch and Baseline Notes

The directory had no `.git` at start. Fetched Git history from remote, kept all local files, ran `git checkout -b rule-opt-v2`. Remote main differed from the local v1, so this report explicitly uses the frozen local `v1_ai_extract.py` as baseline; the 12 news/historical-AI fixture files are also frozen in this directory. Main references unchanged. Only staged this task's rules, tests, and verification files; other existing workspace modifications were not staged. The repo had no Git commit identity configured; no commit was created and no identity was filled in without authorization. Changes remain in the rule-opt-v2 branch workspace, not pushed or merged, pending user review.
