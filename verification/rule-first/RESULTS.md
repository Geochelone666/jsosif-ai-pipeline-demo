# Rule-first verification — 2026-10-05

Implemented in ai_extract.py; report.py and regenerate_report.py unchanged. Existing category arrays and required fields preserved. Added event_type, sentiment, companies, source, pubDate, url, sources, extraction_method. Unresolved items remain auditable in unclassified; stats use unique headlines. Only uncertain items are passed to the existing Gemini CLI, using fixed gemini-3.5-flash-lite. No new credential or alternate model introduced. Rule summaries repeat the supplied headline rather than inventing context. Impact/horizon are conservative fixed defaults, not inferred facts.

## Results

- `python3 -m unittest -v test_ai_extract`: 4 tests passed (AI routing, RSS authority, deduplication, failure preservation, ticker boundaries).
- `python3 verification/rule-first/benchmark.py`: 150 input articles / 147 unique; 41 rule (27.89%), 106 AI candidates (72.11%). **70% target not met.** No forced neutral labels for speculative/question headlines.
- Historical pure-AI snapshots match 24 rule headlines; category agreement 11/24 (45.83%). These snapshots are not ground truth and have no event/sentiment labels. True extraction accuracy comparison is unavailable; this measurement is only category agreement. See benchmark.json for disagreements.
- `python3 verification/rule-first/check_reports.py`: all six existing snapshot reports are byte-identical when only metadata is added. All six rule-output reports render, and existing validate_phase1.py passes in the isolated report-compat directory. Rule classifications and headline-only summaries necessarily change news content.
- Full NVDA pipeline executed in isolated directory: quant → ai_extract → comparables → earnings → edgar → regenerate_report. Network denied by environment; produced N/A report. See live-pipeline.log. This is not a successful online end-to-end result.
- Separate actual Flash-Lite attempt on 18 ambiguous cached NVDA headlines failed in existing CLI dynamic credential lookup. Seven rule results retained; 18 unknown. No real AI comparison fabricated.

## Remaining acceptance work

The current implementation reduces eligible headline volume by 27.9%; it does not meet the requested 70% reduction. Existing code already batched 25 articles into one request per ticker, so headline coverage reduces prompt tokens but does not necessarily reduce request count. Broadening coverage responsibly requires labeled examples or richer article content, especially for speculative and mixed-signal news. Successful network/credential access is needed to verify the live fallback. Existing fixture files and published reports were left intact.
