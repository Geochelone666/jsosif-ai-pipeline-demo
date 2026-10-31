# PFE Intelligence Report

- ticker: **PFE**
- Report as_of: **2026-10-30**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/PFE/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PFE/key-statistics/
- AI analysis snapshot as_of: **2026-10-30**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-31T02:02:45.196277+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 14, 'rule': 1, 'ai': 4, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261030T021807Z-b9de7146/PFE** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 14 unique headlines; 8 named publishers; 0 exact duplicates; 14 HTTPS source links; largest publisher share 35.71%; oldest publication 2026-10-24

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 30.5200 |
| Return 1D (%) | 1.9032 |
| Return 1W (%) | 1.6317 |
| Return 1M (%) | 7.0126 |
| Return YTD (%) | 28.8967 |
| Return 1Y (%) | 34.4604 |
| Annualized volatility (%) | 21.3288 |
| Beta vs SPY | 0.2129 |
| Max drawdown (%) | -15.7243 |
| Sharpe (rf=0) | 1.5006 |
| Downside deviation (rf=0, %) | 13.6537 |
| Sortino (rf=0) | 2.3441 |
| Historical VaR 95% (1D, %) | 1.9258 |
| Historical ES 95% (1D, %) | 2.5887 |
| Correlation vs SPY | 0.1277 |
| Tracking error vs SPY (%) | 23.4273 |
| P/E (trailing) | 40.16 |
| P/B | 2.04 |
| EV/EBITDA | 8.90 |
| Revenue growth (%) | 2.60 |
| Forward P/E (estimate) | 10.58 |
| Gross margin (%) | 74.72 |
| Operating margin (%) | 27.88 |
| Return on equity (%) | 5.01 |
| Free cash flow yield (%) | 7.18 |
| MA50 | 28.5466 |
| Close vs MA50 (%) | 6.9129 |
| MA200 | 26.3267 |
| Close vs MA200 (%) | 15.9279 |
| RSI (14, Wilder) | 66.5780 |
| MACD (12,26) | 0.5489 |
| MACD signal (9) | 0.5044 |
| MACD histogram | 0.0446 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PFE': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 30.5200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.9032 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.6317 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.0126 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 28.8967 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 34.4604 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.3288 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.6537 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.3441 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.9258 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.5887 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1277 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.4273 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2129 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.7243 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.5006 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 10.5822 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 27.8770 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 5.0140 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.1775 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 40.1579 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 66.5780 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0446 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.9129 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 15.9279 -> Clearly above the moving-average trend level.

## TAILWINDS

### Pfizer (PFE) Expected to Beat Earnings Estimates: Should You Buy?
- Summary: Pfizer is projected to exceed earnings estimates, indicating strong financial performance.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQLWFLYVV5V19FWkE5dklMNEY3MUdrTVdfekFiVnR2bFNscGVXc0p4anhtSmpzcUNRMmxTRUc3MTVoUmF5cUdtdHZJMnZrTmQtSEhuNlFoWEF1cHV2ckRWZWZQT2JlTnRPUEFPWEE0RmN4V1JyNkdsUHVMR3FySW1wTDdKZFQ1ZGdCN1ByWjlodW5UcGdYYWFMZnNIU0ZWZm8?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Pfizer (PFE) Stock Looks Above Fair Value As 30% Run Continues
- Summary: Pfizer (PFE) Stock Looks Above Fair Value As 30% Run Continues
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPcE5idEFfcVprMUpfcFJoVnlJdW1SYjNxbGExZGRkWTBqZ25JSlhJNDZRQ1FRek03QWx6UlpVZ0RkVkJYWjlFMXpJbmdlWXlheDEtWjk3LTRLbFJrbmxNTjlORTlRMDAwZWFlQ3pfLUZaYTRKaHZ1bzBSdEpLQy1JQU55LUJMdkhqN3hGSC1Tam51eW9Xd3hjSA?oc=5>

### Exploring Analyst Estimates for Pfizer (PFE) Q3 Earnings, Beyond Revenue and EPS
- Summary: Analysts discuss Pfizer’s Q3 earnings outlook, focusing on revenue and EPS projections.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQRjA0eEVyLWJIeGUtNGlBYXpwNjlseWozeFBieEFwSzdLWmxkQ0ZCS0VwYkpZZzRUN0FWNlpBNUNSam80cHNGS3dEYzFHaG1aNEdybFV0N1JlMGdwRnBVbnQycE41eU15dEhfdlBhaHZzejZQWG53dFR4cTcwa0toWDV3SGNmeWpiaGVaamtNanphb0NWdUE4N2djOTJSMHN4UlVxT2V3?oc=5>

### Pfizer posts late-stage trial win for multiple myeloma drug Elrexfio in an earlier line setting
- Summary: Late-stage trial success for Elrexfio shows promising efficacy in earlier treatment line.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQdjAzOEluRTNteXVYWmJpWWZLd1YteHp1Y3RQTTVvWmFvTUdNTEc4Q0xFRVY2eTVPamU3dmJVckNydElESGZhb0M0bHF0b25IS2w2MU1VMFpLNjJRcEp1enMyNzRXei1oRGRBT1U2WEVFVldvS082YnF0akdHUWM5aW02cXhIR3NoU3k4VU54eF9iYVpDdTdGYw?oc=5>

### Pfizer: Reality Check Ahead Of Earnings (NYSE:PFE)
- Summary: Pfizer prepares for earnings release, highlighting potential risks and opportunities for investors.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxOUDIxNEZ5V2hrbnBDNUlMbzdjT2xOY1h6b2N4T3h6Tk9FZ0ZhRWh6MDZ1ajdoVGhnQ1J3cUxvaVJncU91b3FyVHVOenRMU2F0b1V0UngxOFV3Tnh5am9raG55V3d0QVNvUlJ4S2xNMHNUUXhsaVRocUxRTWgxOWI3cUYyek9NUQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PFE** | **40.16** | **2.04** | **8.90** | **2.60** | **173,954,039,808.00 USD** | **34.46** |
| MRK | 118.67 | 8.80 | N/A | 4.70 | 368,891,494,400.00 USD | 78.38 |
| JNJ | 41.46 | 8.07 | 19.86 | 5.90 | 657,677,221,888.00 USD | 47.77 |
| LLY | 47.58 | 47.80 | N/A | 38.60 | 1,262,666,776,576.00 USD | 68.91 |

Peers fetched as_of: 2026-10-30; PFE reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-30

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-04
- Revenue (latest available single quarter): 15,034,000,000.00 USD; period 2026-03-30/2026-06-28; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): -248,000,000.00 USD; period 2026-03-30/2026-06-28; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/78003/000007800326000095/pfe-20260628.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMinwFBVV95cUxQLWFLYVV5V19FWkE5dklMNEY3MUdrTVdfekFiVnR2bFNscGVXc0p4anhtSmpzcUNRMmxTRUc3MTVoUmF5cUdtdHZJMnZrTmQtSEhuNlFoWEF1cHV2ckRWZWZQT2JlTnRPUEFPWEE0RmN4V1JyNkdsUHVMR3FySW1wTDdKZFQ1ZGdCN1ByWjlodW5UcGdYYWFMZnNIU0ZWZm8?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPcE5idEFfcVprMUpfcFJoVnlJdW1SYjNxbGExZGRkWTBqZ25JSlhJNDZRQ1FRek03QWx6UlpVZ0RkVkJYWjlFMXpJbmdlWXlheDEtWjk3LTRLbFJrbmxNTjlORTlRMDAwZWFlQ3pfLUZaYTRKaHZ1bzBSdEpLQy1JQU55LUJMdkhqN3hGSC1Tam51eW9Xd3hjSA?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQRjA0eEVyLWJIeGUtNGlBYXpwNjlseWozeFBieEFwSzdLWmxkQ0ZCS0VwYkpZZzRUN0FWNlpBNUNSam80cHNGS3dEYzFHaG1aNEdybFV0N1JlMGdwRnBVbnQycE41eU15dEhfdlBhaHZzejZQWG53dFR4cTcwa0toWDV3SGNmeWpiaGVaamtNanphb0NWdUE4N2djOTJSMHN4UlVxT2V3?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQdjAzOEluRTNteXVYWmJpWWZLd1YteHp1Y3RQTTVvWmFvTUdNTEc4Q0xFRVY2eTVPamU3dmJVckNydElESGZhb0M0bHF0b25IS2w2MU1VMFpLNjJRcEp1enMyNzRXei1oRGRBT1U2WEVFVldvS082YnF0akdHUWM5aW02cXhIR3NoU3k4VU54eF9iYVpDdTdGYw?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxOUDIxNEZ5V2hrbnBDNUlMbzdjT2xOY1h6b2N4T3h6Tk9FZ0ZhRWh6MDZ1ajdoVGhnQ1J3cUxvaVJncU91b3FyVHVOenRMU2F0b1V0UngxOFV3Tnh5am9raG55V3d0QVNvUlJ4S2xNMHNUUXhsaVRocUxRTWgxOWI3cUYyek9NUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
