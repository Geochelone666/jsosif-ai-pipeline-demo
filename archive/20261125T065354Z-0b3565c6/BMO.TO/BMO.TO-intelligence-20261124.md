# BMO.TO Intelligence Report

- ticker: **BMO.TO**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/BMO.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BMO.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:03:09.529024+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 12, 'rule': 1, 'ai': 7, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 12 unique headlines; 8 named publishers; 0 exact duplicates; 12 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 229.4200 |
| Return 1D (%) | -0.4685 |
| Return 1W (%) | -3.5969 |
| Return 1M (%) | -2.4680 |
| Return YTD (%) | 32.7326 |
| Return 1Y (%) | 37.0776 |
| Annualized volatility (%) | 20.1511 |
| Beta vs SPY | 0.8152 |
| Max drawdown (%) | -12.3392 |
| Sharpe (rf=0) | 1.6729 |
| Downside deviation (rf=0, %) | 13.9185 |
| Sortino (rf=0) | 2.4220 |
| Historical VaR 95% (1D, %) | 2.1035 |
| Historical ES 95% (1D, %) | 2.7378 |
| Correlation vs SPY | 0.6033 |
| Tracking error vs SPY (%) | 16.4450 |
| P/E (trailing) | 18.70 |
| P/B | 1.88 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 12.00 |
| Forward P/E (estimate) | 13.93 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 37.94 |
| Return on equity (%) | 10.57 |
| Free cash flow yield (%) | N/A |
| MA50 | 238.0820 |
| Close vs MA50 (%) | -3.6382 |
| MA200 | 223.7686 |
| Close vs MA200 (%) | 2.5256 |
| RSI (14, Wilder) | 39.8767 |
| MACD (12,26) | -2.2606 |
| MACD signal (9) | -0.2725 |
| MACD histogram | -1.9881 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BMO.TO': 288, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 229.4200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.4685 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.5969 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -2.4680 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 32.7326 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 37.0776 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 20.1511 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.9185 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.4220 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1035 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.7378 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6033 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 16.4450 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8152 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -12.3392 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.6729 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 13.9256 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 37.9380 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.5740 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.6976 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 39.8767 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.9881 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.6382 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 2.5256 -> Slightly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Bank Of Montreal $BMO Stock: Healthcare of Ontario Pension Plan Trust Fund Increases Holdings
- Summary: Bank Of Montreal $BMO Stock: Healthcare of Ontario Pension Plan Trust Fund Increases Holdings
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5wFBVV95cUxOTllNY1BHZW1aMU9Mdm12T0h4VUxNejBGdy02Z0d5TVRVRGNfRWlQX3dWa0VDQ3hSajdnb3ZHZ2d0MWx4VHVhandwZV9ubzNIQ2JtNnhyUmVLeFdubS1xbmJ5bVRqVE9qMnpLeC1zaUlZd1hINEluaFlqdXFReFNVTW1WcGhHUGdNVE9iclJVWHhIeTdtMHRoX09OcEwwVk5tNVBkaHppMXo4ZzhMcFBUV0M3VXFTVjMwdHpyVUdiREtkbW4wd00zS05tMWkwaHl6VXVzNkowckI4NHkydVdDNjQ5TVlrVEE?oc=5>

### Bank of Montreal (TSX:BMO) - Stock Analysis
- Summary: Analyst review of BMO’s financial performance and outlook.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTFBtQ3BNMmZCRDdYekR3TDNwYVFLT25tUmREejJ2UHhxTkc0Nm9iblhSY3pQcHY5TE9ZQnREai1DSHJEN1dxWFo5eWJSbWVGWUFVZmJYbzk1bzNfeXI3UnNaZnZxclk5MnhIeWdKV1FyWVR1elVnQkVSRQ?oc=5>

### Bank Of Montreal (BMO): Notes tied to SpaceX stock pay 14.20% annual contingent coupon
- Summary: BMO issues notes linked to SpaceX stock with 14.20% annual coupon.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxNZTljZXR1dk9oSnlva3g3SjY0bmdTZWhOOFRvckpUbC1Qc2hzd0VQRHdQYzlWcF9iZWhWdk8wbnVHUW9QUWt6Um5JTTZJVDBiRF9BdnZzR0RCckt4SXo3X2hYQ2tia0ZtNFh6RW1obE13clN4cHJRcHNCV0FyQWtIdmlJbGFHUC1P?oc=5>

### Bank of Montreal stock: RBC lifts target to CAD 258
- Summary: RBC raises its price target for BMO stock to CAD 258, signaling optimism about the bank’s prospects.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxQUU1TRlUycVlpNjhnVG5rWlIza3BBRWw4dlJhenpSOG1JM1BKR1JIUGt2bzN1TjJGYkZWa3I3R2V2dThad2E5U09sN25jTHotcWtXcWx3Mkp2d3Zaa0YtUHRSYUE1MFhySGJVQ3NxUDFMN1VMQXZXN1RQbEtSVVBsdWdyOHRZbGlyNDhJWmFoUTNOWE1INU5IY3p3WVJHSWMxQmxicFJxd2VlMksxLWw4OF9fdw?oc=5>

### Can Quantum Utility Change The Bull Case For BMO (TSX:BMO)?
- Summary: Speculation on quantum utility’s impact on BMO’s valuation.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPYnNabndDUFFHaHNQTmJtSXVnVGw1MkpEVzBya2VmQWxiTWpjRVhPYWZiT2lmREJnSno0bmFvVUhnSzFuclM1Yl9rM2s2TUNWWnJhRzAwcHh1U1g2Rm05QlNrQTFTQTIwMjduWUMyV1h2RkNUNEhYNE96a0d4ZzFxTmdqbGFuMmRPLWZYNEd1REFzY21pX1ZOdVlyWjNrQQ?oc=5>

### EXCLUSIVE: Canada's BMO returning to US oil and gas investment banking, sources say
- Summary: BMO re-enters US oil and gas investment banking services.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxPMEJnU0FpNlBIQVVrY3RZWkxwVzV5a0RJajBPLWpIZW5DX1Y1cDBuZnJsWU14dHBGcGV3aE9LRkx6aVg4VDRjVHB1UmphaWN1VVJCQVQ1bEhnel9rTnNzSmZVZUJlTHZsTHVsdWpmZjM2aHQ1R09mZEZTUVpqbV9VZ18tMC15WkhxOW5PN2FtNHRXMHkwUndMV3NBQVZtaGNKajVzZkZfMWNwd0pYS21Ea0ZBNkZtUQ?oc=5>

### BMO: SEC Form FWP filed by Bank Of Montreal
- Summary: BMO files SEC Form FWP, regulatory disclosure.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxOTlpTWG5JSnlrWm5WTll4Mk1OZUZDVGpMRmFQY1VVcGhQaFJSenhTSTJFbHp4bndJd0JadnVmYzF4ZXBrckd1dVV0SWZVQVhzcmFiYnBrM0Q2ZjhWRVlTYjJKTjhZVVctMDNLYjNnWmZCRlFZTnd6bGhmQ3RMcXZCTlZtRnhZU3Jy?oc=5>

### Bank of Montreal (TSE:BMO) Stock Price Expected to Rise, Jefferies Financial Group Analyst Says
- Summary: Analyst predicts BMO stock price increase.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi6gFBVV95cUxPc1R3WHFXODh6Uko4ZDFNWmdONHktbXQ1LVNnUWh2WVNZeWZfMnI0NmF6X21ROGJKanZXN0V1bDJPNTZXQ3RZUHpLYUx3ek5iTkJmTkVHMGdmb2xXWi00RU9meEtjaDY0NUlPbk9OWG9tNzN3QkJFYUhRN2MySlZTZnBieGhnTzdqOGdBTG1UMDJ6TVF2Z0JleGdpVzBKQXQxM1FRSjA5dWllN1l1N3dOWlhzV2hlT3FpaEZkeWIyY2xNRXI5bW1qejVXTUlsOEEtczhXMHhQalczYlN0ZHpxTjZQOWI0X01faFE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BMO.TO** | **18.70** | **1.88** | **N/A** | **12.00** | **159,468,060,672.00 CAD** | **37.08** |
| RY.TO | 17.00 | 2.79 | N/A | 8.90 | 373,297,676,288.00 CAD | 30.93 |
| TD.TO | 17.56 | 2.18 | N/A | 11.50 | 269,545,734,144.00 CAD | 45.69 |
| BNS.TO | 15.68 | 1.66 | N/A | 11.70 | 147,880,640,512.00 CAD | 34.43 |

Peers fetched as_of: 2026-11-24; BMO.TO reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-25
- Next expected earnings: 2026-12-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

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

- https://news.google.com/rss/articles/CBMi5wFBVV95cUxOTllNY1BHZW1aMU9Mdm12T0h4VUxNejBGdy02Z0d5TVRVRGNfRWlQX3dWa0VDQ3hSajdnb3ZHZ2d0MWx4VHVhandwZV9ubzNIQ2JtNnhyUmVLeFdubS1xbmJ5bVRqVE9qMnpLeC1zaUlZd1hINEluaFlqdXFReFNVTW1WcGhHUGdNVE9iclJVWHhIeTdtMHRoX09OcEwwVk5tNVBkaHppMXo4ZzhMcFBUV0M3VXFTVjMwdHpyVUdiREtkbW4wd00zS05tMWkwaHl6VXVzNkowckI4NHkydVdDNjQ5TVlrVEE?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTFBtQ3BNMmZCRDdYekR3TDNwYVFLT25tUmREejJ2UHhxTkc0Nm9iblhSY3pQcHY5TE9ZQnREai1DSHJEN1dxWFo5eWJSbWVGWUFVZmJYbzk1bzNfeXI3UnNaZnZxclk5MnhIeWdKV1FyWVR1elVnQkVSRQ?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxNZTljZXR1dk9oSnlva3g3SjY0bmdTZWhOOFRvckpUbC1Qc2hzd0VQRHdQYzlWcF9iZWhWdk8wbnVHUW9QUWt6Um5JTTZJVDBiRF9BdnZzR0RCckt4SXo3X2hYQ2tia0ZtNFh6RW1obE13clN4cHJRcHNCV0FyQWtIdmlJbGFHUC1P?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxQUU1TRlUycVlpNjhnVG5rWlIza3BBRWw4dlJhenpSOG1JM1BKR1JIUGt2bzN1TjJGYkZWa3I3R2V2dThad2E5U09sN25jTHotcWtXcWx3Mkp2d3Zaa0YtUHRSYUE1MFhySGJVQ3NxUDFMN1VMQXZXN1RQbEtSVVBsdWdyOHRZbGlyNDhJWmFoUTNOWE1INU5IY3p3WVJHSWMxQmxicFJxd2VlMksxLWw4OF9fdw?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPYnNabndDUFFHaHNQTmJtSXVnVGw1MkpEVzBya2VmQWxiTWpjRVhPYWZiT2lmREJnSno0bmFvVUhnSzFuclM1Yl9rM2s2TUNWWnJhRzAwcHh1U1g2Rm05QlNrQTFTQTIwMjduWUMyV1h2RkNUNEhYNE96a0d4ZzFxTmdqbGFuMmRPLWZYNEd1REFzY21pX1ZOdVlyWjNrQQ?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxPMEJnU0FpNlBIQVVrY3RZWkxwVzV5a0RJajBPLWpIZW5DX1Y1cDBuZnJsWU14dHBGcGV3aE9LRkx6aVg4VDRjVHB1UmphaWN1VVJCQVQ1bEhnel9rTnNzSmZVZUJlTHZsTHVsdWpmZjM2aHQ1R09mZEZTUVpqbV9VZ18tMC15WkhxOW5PN2FtNHRXMHkwUndMV3NBQVZtaGNKajVzZkZfMWNwd0pYS21Ea0ZBNkZtUQ?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxOTlpTWG5JSnlrWm5WTll4Mk1OZUZDVGpMRmFQY1VVcGhQaFJSenhTSTJFbHp4bndJd0JadnVmYzF4ZXBrckd1dVV0SWZVQVhzcmFiYnBrM0Q2ZjhWRVlTYjJKTjhZVVctMDNLYjNnWmZCRlFZTnd6bGhmQ3RMcXZCTlZtRnhZU3Jy?oc=5
- https://news.google.com/rss/articles/CBMi6gFBVV95cUxPc1R3WHFXODh6Uko4ZDFNWmdONHktbXQ1LVNnUWh2WVNZeWZfMnI0NmF6X21ROGJKanZXN0V1bDJPNTZXQ3RZUHpLYUx3ek5iTkJmTkVHMGdmb2xXWi00RU9meEtjaDY0NUlPbk9OWG9tNzN3QkJFYUhRN2MySlZTZnBieGhnTzdqOGdBTG1UMDJ6TVF2Z0JleGdpVzBKQXQxM1FRSjA5dWllN1l1N3dOWlhzV2hlT3FpaEZkeWIyY2xNRXI5bW1qejVXTUlsOEEtczhXMHhQalczYlN0ZHpxTjZQOWI0X01faFE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
