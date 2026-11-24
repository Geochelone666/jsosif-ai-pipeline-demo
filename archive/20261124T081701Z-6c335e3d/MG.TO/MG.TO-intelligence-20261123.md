# MG.TO Intelligence Report

- ticker: **MG.TO**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/MG.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MG.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:41:47.428356+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 5, 'rule': 1, 'ai': 2, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261123T053847Z-45053549/MG.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 5 unique headlines; 5 named publishers; 0 exact duplicates; 5 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 88.2600 |
| Return 1D (%) | 5.0589 |
| Return 1W (%) | 0.7189 |
| Return 1M (%) | -0.5855 |
| Return YTD (%) | 24.3761 |
| Return 1Y (%) | 33.7733 |
| Annualized volatility (%) | 37.1457 |
| Beta vs SPY | 1.0929 |
| Max drawdown (%) | -22.7904 |
| Sharpe (rf=0) | 0.9645 |
| Downside deviation (rf=0, %) | 21.7444 |
| Sortino (rf=0) | 1.6477 |
| Historical VaR 95% (1D, %) | 2.8900 |
| Historical ES 95% (1D, %) | 4.2406 |
| Correlation vs SPY | 0.4393 |
| Tracking error vs SPY (%) | 33.6858 |
| P/E (trailing) | 21.74 |
| P/B | 1.41 |
| EV/EBITDA | 6.44 |
| Revenue growth (%) | -3.90 |
| Forward P/E (estimate) | 7.95 |
| Gross margin (%) | 15.18 |
| Operating margin (%) | 5.74 |
| Return on equity (%) | 7.09 |
| Free cash flow yield (%) | N/A |
| MA50 | 89.4455 |
| Close vs MA50 (%) | -1.3254 |
| MA200 | 86.9476 |
| Close vs MA200 (%) | 1.5094 |
| RSI (14, Wilder) | 49.2486 |
| MACD (12,26) | -0.7258 |
| MACD signal (9) | -0.6981 |
| MACD histogram | -0.0277 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MG.TO': 287, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 88.2600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 5.0589 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.7189 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -0.5855 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 24.3761 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 33.7733 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 37.1457 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.7444 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.6477 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8900 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.2406 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4393 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.6858 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.0929 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -22.7904 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9645 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 7.9491 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 15.1770 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 5.7440 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 7.0910 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.7389 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 49.2486 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0277 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -1.3254 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 1.5094 -> Slightly above the moving-average trend level.

## TAILWINDS

### Magna International (TSX:MG) Stock Looks Overvalued Despite Its 35% Gain
- Summary: Magna International (TSX:MG) Stock Looks Overvalued Despite Its 35% Gain
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxOUVNzSDhTZldiSndmNk5fV2R5Z0pXOW1iVUdfWFhpQzE1Uno1TGt0eFFTWnA1cjFuQkRHYVVad0FtbnJyckI4V2pTU3Z0LWFXb0FXbWV4dEwySDJlMzRRVkdldHNCRDg2QzNTRnhFZHpGYi1iQ2szbUNabm9PTWJIdHphbVlFaWdLMVZZeS1ldlhiTGZYM0pvODRuNUpienBvbXNpUnpPMjFlb29yaEdmYkhqNUxTMGtiQUFaZzBMS180WjdVUjRUUWdHRnAxcnRpb2F6UGhWWEZLTTDSAeABQVVfeXFMTWEtOVRlQUVqWWV5TUl5TkVDY203ZjZIUXJ6Y3BKZ3NRREJQaTZrRjVqTGQxNEZaY2tsbGVTb2hhZVEwbUlQWTRad2lNemMzZ2M2aVY0S2VNR19lV0RGbVYxcDlPRlVoY2FLaFlXT0dtUWFST2dTYzYzc2FIdVhIdDRiaDJ6eEd6dTMxX3ZxaVZTbTh4RnpKbm8yRW04b1gySVE2QVp0SWctZTJnRDdPeXdDdnBTMURRaGROdTIyUVZ6eW5SamxlcFFzSDdRVjBISjA5NTJxSU5pVF9lVG5oQ08?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Magna International Inc. (MG.TO) stock price, news, quote and history
- Summary: Magna’s stock price movement reported.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiU0FVX3lxTE5KMFRxVXZNQ0x2dG9WWFRoMktHNTNmb2ZsWGR0dThNYXA5X3NwUWZ2dXdCcGZtYW0tN2pRR2FSbE5fZVlfNkdJaDVnUmxJSXAtRmN3?oc=5>

## RISKS

### S&P/TSX Composite: Magna International Inc. (TSX:MG) — Large Cap Value Stock in Focus as Investors Track the Next Catalyst
- Summary: Investors monitoring potential future catalyst for Magna.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6gFBVV95cUxNRXNyWDBReV9Kblh0WkE0X2hPTHlmbU9oY2Z1OE1GQldWX184bWg4b25lUTNuc1RVOXFtd2JGbklmMDZncFdiOGRzcFBHbEVnQTh0bXo0M2RCSG1BelhUNk9KdEtEYVluRktvNU1KeEE3TjdHNDZJY2MyNTdrLXpGeFU2UVlOWGtFNnBTcXdlSkxfeFNJb1BVdE5Oc3Foa0hOZEZlZE1kUEN0SGVKaGUxVjJjLTdwNUxTOGZfR2hSS2R1VW02OHRTbHlMS0pxanlpd05nMmJuWHltaHQtaXpjeWNfdlI3UFk4YlE?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MG.TO** | **21.74** | **1.41** | **6.44** | **-3.90** | **22,804,928,512.00 CAD** | **33.77** |
| APTV | 10.59 | 0.88 | 3.96 | 2.30 | 7,674,124,288.00 USD | -48.86 |
| BWA | 21.53 | 1.80 | 5.92 | -2.90 | 10,203,363,328.00 USD | 19.69 |
| LEA | 9.20 | 1.02 | 4.63 | 1.60 | 5,088,597,504.00 USD | 3.94 |

Peers fetched as_of: 2026-11-23; MG.TO reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-30
- Next expected earnings: 2027-02-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-23

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: N/A
- Filing date: N/A
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: N/A

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi2wFBVV95cUxOUVNzSDhTZldiSndmNk5fV2R5Z0pXOW1iVUdfWFhpQzE1Uno1TGt0eFFTWnA1cjFuQkRHYVVad0FtbnJyckI4V2pTU3Z0LWFXb0FXbWV4dEwySDJlMzRRVkdldHNCRDg2QzNTRnhFZHpGYi1iQ2szbUNabm9PTWJIdHphbVlFaWdLMVZZeS1ldlhiTGZYM0pvODRuNUpienBvbXNpUnpPMjFlb29yaEdmYkhqNUxTMGtiQUFaZzBMS180WjdVUjRUUWdHRnAxcnRpb2F6UGhWWEZLTTDSAeABQVVfeXFMTWEtOVRlQUVqWWV5TUl5TkVDY203ZjZIUXJ6Y3BKZ3NRREJQaTZrRjVqTGQxNEZaY2tsbGVTb2hhZVEwbUlQWTRad2lNemMzZ2M2aVY0S2VNR19lV0RGbVYxcDlPRlVoY2FLaFlXT0dtUWFST2dTYzYzc2FIdVhIdDRiaDJ6eEd6dTMxX3ZxaVZTbTh4RnpKbm8yRW04b1gySVE2QVp0SWctZTJnRDdPeXdDdnBTMURRaGROdTIyUVZ6eW5SamxlcFFzSDdRVjBISjA5NTJxSU5pVF9lVG5oQ08?oc=5
- https://news.google.com/rss/articles/CBMiU0FVX3lxTE5KMFRxVXZNQ0x2dG9WWFRoMktHNTNmb2ZsWGR0dThNYXA5X3NwUWZ2dXdCcGZtYW0tN2pRR2FSbE5fZVlfNkdJaDVnUmxJSXAtRmN3?oc=5
- https://news.google.com/rss/articles/CBMi6gFBVV95cUxNRXNyWDBReV9Kblh0WkE0X2hPTHlmbU9oY2Z1OE1GQldWX184bWg4b25lUTNuc1RVOXFtd2JGbklmMDZncFdiOGRzcFBHbEVnQTh0bXo0M2RCSG1BelhUNk9KdEtEYVluRktvNU1KeEE3TjdHNDZJY2MyNTdrLXpGeFU2UVlOWGtFNnBTcXdlSkxfeFNJb1BVdE5Oc3Foa0hOZEZlZE1kUEN0SGVKaGUxVjJjLTdwNUxTOGZfR2hSS2R1VW02OHRTbHlMS0pxanlpd05nMmJuWHltaHQtaXpjeWNfdlI3UFk4YlE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
