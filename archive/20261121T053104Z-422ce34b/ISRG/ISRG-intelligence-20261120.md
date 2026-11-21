# ISRG Intelligence Report

- ticker: **ISRG**
- Report as_of: **2026-11-20**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/ISRG/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ISRG/key-statistics/
- AI analysis snapshot as_of: **2026-11-20**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-21T05:52:58.958676+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 15, 'rule': 1, 'ai': 8, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261120T053808Z-e360129e/ISRG** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **4**; {'directional_claim_without_event_type': 4}
- RSS source audit (metadata only, not article fact-checking): 15 unique headlines; 8 named publishers; 0 exact duplicates; 15 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 399.0500 |
| Return 1D (%) | -2.0111 |
| Return 1W (%) | -10.0408 |
| Return 1M (%) | -8.8927 |
| Return YTD (%) | -29.5413 |
| Return 1Y (%) | -27.7384 |
| Annualized volatility (%) | 35.5510 |
| Beta vs SPY | 0.8942 |
| Max drawdown (%) | -43.9960 |
| Sharpe (rf=0) | -0.7377 |
| Downside deviation (rf=0, %) | 26.5437 |
| Sortino (rf=0) | -0.9880 |
| Historical VaR 95% (1D, %) | 3.3061 |
| Historical ES 95% (1D, %) | 5.1297 |
| Correlation vs SPY | 0.3596 |
| Tracking error vs SPY (%) | 33.2078 |
| P/E (trailing) | 48.25 |
| P/B | 8.65 |
| EV/EBITDA | 30.07 |
| Revenue growth (%) | 21.70 |
| Forward P/E (estimate) | 32.00 |
| Gross margin (%) | 66.64 |
| Operating margin (%) | 31.70 |
| Return on equity (%) | 17.93 |
| Free cash flow yield (%) | 2.48 |
| MA50 | 423.5098 |
| Close vs MA50 (%) | -5.7755 |
| MA200 | 427.6851 |
| Close vs MA200 (%) | -6.6954 |
| RSI (14, Wilder) | 35.2934 |
| MACD (12,26) | -2.8037 |
| MACD signal (9) | 4.6157 |
| MACD histogram | -7.4194 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ISRG': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 399.0500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.0111 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -10.0408 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -8.8927 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -29.5413 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -27.7384 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 35.5510 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.5437 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.9880 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.3061 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1297 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3596 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.2078 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8942 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.9960 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.7377 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 32.0040 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 66.6420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 31.7020 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.9320 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.4831 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 48.2527 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 35.2934 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -7.4194 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.7755 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -6.6954 -> Clearly below the moving-average trend level.

## TAILWINDS

### Intuitive Surgical (ISRG) Stock May Be Near Fair Value Despite 22% Revenue Growth
- Summary: Analysts suggest ISRG stock is close to fair value amid strong revenue growth, indicating potential upside.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQNm5nT296UEhuUmRBTGluVElaZFFjLThLajVZcHZhRDAzV3hwZG0zakY5SWRGZVVjSFgzWl9LMWtfbHFSODFKOGw2SUZIb1ZBSEp3eWFWZE9fSGhwTGE1TVJvTEltNWtUdWJ5OTBKemlueUpxNEdxR3ZjYkxabVpUc1M1WHg3WVppcVJLLXdyRlV6VDF3N1lYVlFsRkFJQ2s?oc=5>

### Why Is Intuitive Surgical (ISRG) At The Center Of The Robotics Boom?
- Summary: ISRG positioned as a key player in the robotics boom, benefiting from industry momentum.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPNlM1eFVHd2JZQ2taWXNjSm1tZXlCLXp2V2FYUVExcXM0UktHakxsbG1Hcng1dGNBM1pQTG4taTBxNF9ZY0t1WnVVQ2sxRXE4MmZxbllSa0NGNDUyTTlGcGwyYXNFT0d5LXhzdVg4eTVyYU1DME5yM1JBSFhMelE2R2E2U2d0emNlLUNzWkhlSHRrYWlWZUM5ZVMwTQ?oc=5>

### Why Is Intuitive Surgical (ISRG) Seeing Faster Da Vinci Adoption Worldwide?
- Summary: Rapid global adoption of Da Vinci systems boosts ISRG’s market presence and revenue prospects.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxQN0NlbWFwM3RFV194U2o2bE9kMVRjVWJCVVZQNzAzZGV0cjVwbkhsTmNpNnBzb0V0QWh6SUxkaHk3UTh3QzV5Um9CNF9ETlF5M0pVdVFCVDhCdzBYU2c4TzBINU1HUHhvOTlaNG5LRGUwSVA3bi02VkI2U1dtNV9ZVGdoUUFaM2pWbVVIRms5ZmFWT0RGMXVrZEstZkM3c0ZMVDdTc19La0FacFBGeHZINktQeHYyT1pERHRGYUNrdjZuRjhEZl9rcmptdzdsVFBRb3NlRDd30gHbAUFVX3lxTE9ONF9RTXljS08wWkFRNi1QVEJCOEM1bV9IMFZYcXVrX0lIMEdmQm9KcDVwaURPLXZxeWxpb3lCdllqWHVYcHhmYUdFcmFWRkFXem5aT3ZYcnNjQTd0OGtsUEt5TUlaeGNIWjhmM2hqTXZmdHM3VURoM3VSU291dWhqd3RpazFnV1lQZXNFenpJWUhaQnl5LVRBYXA5TzUtd2s3cWRVUVE0aUVoUVktMVNJWVR6bW5yaXo3U01ycldqTDMxNGgwOThNajg1U0FoYUhOV3k1MkVtRXBYcw?oc=5>

### Is Intuitive Surgical Inc (ISRG) a Bargain After 3.3% Drop? GF V
- Summary: Post‑drop valuation suggests ISRG may be undervalued, offering a buying opportunity.
- Date: 2026-11-19 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxQeS1GU2I2R1FmSFAzVjBoQ05FdllxVW5kZkR5WnlnNUZ2V1F6LUxMVUNaaFFuMTRabnhycFJOZFdTc0Y0MGhKTFBNWlhKYTNwdmtvTFZQWmFOWkFuNW8yWnhYMWE1ZFhRNWVmd2JQczhLamhqVVpzN2IxWk1rMDhZQW4zbjJzenhhSzd4M3ZVelF1NEN1anhsMi1LYW5zQV9UX2pPaDJqMDhsRUhzcGFiRU5GR0hVT3l2bVFJ?oc=5>

## HEADWINDS

### Intuitive Surgical stock falls as weak momentum weighs on price
- Summary: Intuitive Surgical stock falls as weak momentum weighs on price
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNTGRnaXJtNDBTeWVDYkNiWWlraHJzV0ZXeGFhbUxsRGgwYmZlanh3c0pqS2oyWGpkVks4VUVEUjJOZGY5LURkeHNIZzJJTDdMckJxekUxMUZIbUZIX01aSUZaSHp6dlFRVHNOc21rTm9DaWFoLUpwd2hLVk1YeUM0Y0JoRkdhYlVTX3ljbk5FeHhaVHRvOFJXdA?oc=5>

## CATALYSTS

### ISRG EPS Climbs 25% to $3: Is Innovation Driving Profitable Growth?
- Summary: Intuitive Surgical reports a 25% rise in EPS to $3, highlighting strong profitability and potential growth driven by innovation.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxONm8xWW9BY1VqdzdJdDcyTlU1bVJHYlp1UGcwUWlIZEpmdmNvSDdyVXNJWXJJc1lvOGtwQlF6VVF6Q2RvSHp3WmtLVjlvazRVRjRZSHV0bUFoc3VaNzR1RUxjUGQ3YnZjcGViYlpYaWN3bWIyVjB4SXdORzNRVkxtaUo4R3RpNVV2?oc=5>

### Under a trading plan, Mark Brosius sold 46 shares of Intuitive Surgical (ISRG) on each of two days.
- Summary: Insider sold 46 shares twice under a trading plan.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxPLWc0bnRUWE9PcFc2NGF4QXV1eGMwN29sc3FUZzFsbmNNbFk1QV9wdnhHalU0eDJaTUg3QTgydERBTl9ZTHRtQ1lnLXlYWnlxdlgzbE5zbXhEdmxBc3ZkVkNJbXFPWWJwZG5qR0MyaEl3dmlTdk5Jbkt1Y29HbUdZYTN3cmVOQjd0QnYzakw5cTRxNDZ0QmQwWEtaOWpaUWRMSF9nWDFkSVhCU0pRNjlNbVd2T0lmRXc?oc=5>

### Intuitive Surgical, Inc. (ISRG) Stock Forecasts
- Summary: Company issued stock price forecasts.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxNYzhkdlpTUElXZ2tRSlhSX2lqMHhvTEpxcnlGSGpJVi1HMkVxaXRCb2dWMlRROHJBbjgzUEp0bHZEWDB4bThzLUFEMFI3TTkyZmhfMmtwYXZOYUFqcmczdk9LYS15c2RwVXVQU1JRR1VfU0RIUUNfQ0h2UzNuRXE2MmFZclVtbTZPSkcyNA?oc=5>

### Over three days, an Intuitive Surgical (ISRG) executive sold 46 shares a day, for 138 in all.
- Summary: Insider sold 46 shares daily over three days.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxQM0YwZ191VHFBVzlFNEQ1ZUxNaXZtN2dwcHpKUlI1T1N6akJPY3pRRmdzZVVQUDJoNlhfMkJEVkJsX25LSUF0UkMwYTVUUnhSSTVpRWJ5MHJEa1lvTG1wLVhJSDhudUloUEx2bC1fT0JXZWItOFBsMEdXRUlrS1BLVTJIdGdVWS1MRllCeEE1cDc0LWxKWVBFaEhIblpQVDY3M0tXcDQ3Qld2TDVuMkZOcjF2bGZlYkE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ISRG** | **48.25** | **8.65** | **30.07** | **21.70** | **138,328,162,304.00 USD** | **-27.74** |
| MDT | 24.56 | 2.55 | 14.22 | 13.70 | 127,837,044,736.00 USD | 3.93 |
| SYK | 33.01 | 5.03 | 17.33 | 7.60 | 118,014,214,144.00 USD | -13.05 |
| BSX | 18.17 | 2.37 | 13.01 | 1.40 | 60,848,885,760.00 USD | -56.54 |

Peers fetched as_of: 2026-11-20; ISRG reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-20

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 3,048,700,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 522,800,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1035267/000103526726000071/isrg-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMinwFBVV95cUxQNm5nT296UEhuUmRBTGluVElaZFFjLThLajVZcHZhRDAzV3hwZG0zakY5SWRGZVVjSFgzWl9LMWtfbHFSODFKOGw2SUZIb1ZBSEp3eWFWZE9fSGhwTGE1TVJvTEltNWtUdWJ5OTBKemlueUpxNEdxR3ZjYkxabVpUc1M1WHg3WVppcVJLLXdyRlV6VDF3N1lYVlFsRkFJQ2s?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPNlM1eFVHd2JZQ2taWXNjSm1tZXlCLXp2V2FYUVExcXM0UktHakxsbG1Hcng1dGNBM1pQTG4taTBxNF9ZY0t1WnVVQ2sxRXE4MmZxbllSa0NGNDUyTTlGcGwyYXNFT0d5LXhzdVg4eTVyYU1DME5yM1JBSFhMelE2R2E2U2d0emNlLUNzWkhlSHRrYWlWZUM5ZVMwTQ?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQN0NlbWFwM3RFV194U2o2bE9kMVRjVWJCVVZQNzAzZGV0cjVwbkhsTmNpNnBzb0V0QWh6SUxkaHk3UTh3QzV5Um9CNF9ETlF5M0pVdVFCVDhCdzBYU2c4TzBINU1HUHhvOTlaNG5LRGUwSVA3bi02VkI2U1dtNV9ZVGdoUUFaM2pWbVVIRms5ZmFWT0RGMXVrZEstZkM3c0ZMVDdTc19La0FacFBGeHZINktQeHYyT1pERHRGYUNrdjZuRjhEZl9rcmptdzdsVFBRb3NlRDd30gHbAUFVX3lxTE9ONF9RTXljS08wWkFRNi1QVEJCOEM1bV9IMFZYcXVrX0lIMEdmQm9KcDVwaURPLXZxeWxpb3lCdllqWHVYcHhmYUdFcmFWRkFXem5aT3ZYcnNjQTd0OGtsUEt5TUlaeGNIWjhmM2hqTXZmdHM3VURoM3VSU291dWhqd3RpazFnV1lQZXNFenpJWUhaQnl5LVRBYXA5TzUtd2s3cWRVUVE0aUVoUVktMVNJWVR6bW5yaXo3U01ycldqTDMxNGgwOThNajg1U0FoYUhOV3k1MkVtRXBYcw?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxQeS1GU2I2R1FmSFAzVjBoQ05FdllxVW5kZkR5WnlnNUZ2V1F6LUxMVUNaaFFuMTRabnhycFJOZFdTc0Y0MGhKTFBNWlhKYTNwdmtvTFZQWmFOWkFuNW8yWnhYMWE1ZFhRNWVmd2JQczhLamhqVVpzN2IxWk1rMDhZQW4zbjJzenhhSzd4M3ZVelF1NEN1anhsMi1LYW5zQV9UX2pPaDJqMDhsRUhzcGFiRU5GR0hVT3l2bVFJ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNTGRnaXJtNDBTeWVDYkNiWWlraHJzV0ZXeGFhbUxsRGgwYmZlanh3c0pqS2oyWGpkVks4VUVEUjJOZGY5LURkeHNIZzJJTDdMckJxekUxMUZIbUZIX01aSUZaSHp6dlFRVHNOc21rTm9DaWFoLUpwd2hLVk1YeUM0Y0JoRkdhYlVTX3ljbk5FeHhaVHRvOFJXdA?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxONm8xWW9BY1VqdzdJdDcyTlU1bVJHYlp1UGcwUWlIZEpmdmNvSDdyVXNJWXJJc1lvOGtwQlF6VVF6Q2RvSHp3WmtLVjlvazRVRjRZSHV0bUFoc3VaNzR1RUxjUGQ3YnZjcGViYlpYaWN3bWIyVjB4SXdORzNRVkxtaUo4R3RpNVV2?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxPLWc0bnRUWE9PcFc2NGF4QXV1eGMwN29sc3FUZzFsbmNNbFk1QV9wdnhHalU0eDJaTUg3QTgydERBTl9ZTHRtQ1lnLXlYWnlxdlgzbE5zbXhEdmxBc3ZkVkNJbXFPWWJwZG5qR0MyaEl3dmlTdk5Jbkt1Y29HbUdZYTN3cmVOQjd0QnYzakw5cTRxNDZ0QmQwWEtaOWpaUWRMSF9nWDFkSVhCU0pRNjlNbVd2T0lmRXc?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNYzhkdlpTUElXZ2tRSlhSX2lqMHhvTEpxcnlGSGpJVi1HMkVxaXRCb2dWMlRROHJBbjgzUEp0bHZEWDB4bThzLUFEMFI3TTkyZmhfMmtwYXZOYUFqcmczdk9LYS15c2RwVXVQU1JRR1VfU0RIUUNfQ0h2UzNuRXE2MmFZclVtbTZPSkcyNA?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxQM0YwZ191VHFBVzlFNEQ1ZUxNaXZtN2dwcHpKUlI1T1N6akJPY3pRRmdzZVVQUDJoNlhfMkJEVkJsX25LSUF0UkMwYTVUUnhSSTVpRWJ5MHJEa1lvTG1wLVhJSDhudUloUEx2bC1fT0JXZWItOFBsMEdXRUlrS1BLVTJIdGdVWS1MRllCeEE1cDc0LWxKWVBFaEhIblpQVDY3M0tXcDQ3Qld2TDVuMkZOcjF2bGZlYkE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
