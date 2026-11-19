# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-11-18**
- Market data as_of: **2026-11-18**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-11-18**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-19T05:53:38.515460+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 6, 'ai': 11, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261118T054934Z-e0d070d9/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 1, 'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 14 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 34.78%; oldest publication 2026-11-12

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 530.1400 |
| Return 1D (%) | 5.3098 |
| Return 1W (%) | -4.1165 |
| Return 1M (%) | 0.2629 |
| Return YTD (%) | 147.5439 |
| Return 1Y (%) | 130.2054 |
| Annualized volatility (%) | 73.6169 |
| Beta vs SPY | 3.4062 |
| Max drawdown (%) | -37.7290 |
| Sharpe (rf=0) | 1.5055 |
| Downside deviation (rf=0, %) | 47.8172 |
| Sortino (rf=0) | 2.3178 |
| Historical VaR 95% (1D, %) | 6.7006 |
| Historical ES 95% (1D, %) | 9.6472 |
| Correlation vs SPY | 0.6365 |
| Tracking error vs SPY (%) | 65.7226 |
| P/E (trailing) | 113.28 |
| P/B | 12.71 |
| EV/EBITDA | 77.44 |
| Revenue growth (%) | 44.70 |
| Forward P/E (estimate) | 30.06 |
| Gross margin (%) | 56.00 |
| Operating margin (%) | 17.82 |
| Return on equity (%) | 11.96 |
| Free cash flow yield (%) | 0.84 |
| MA50 | 555.2206 |
| Close vs MA50 (%) | -4.5172 |
| MA200 | 427.1817 |
| Close vs MA200 (%) | 24.1018 |
| RSI (14, Wilder) | 50.3386 |
| MACD (12,26) | -8.0334 |
| MACD signal (9) | -12.4876 |
| MACD histogram | 4.4542 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 285, 'SPY': 285}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 530.1400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 5.3098 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.1165 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 0.2629 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 147.5439 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 130.2054 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 73.6169 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 47.8172 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.3178 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.7006 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 9.6472 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6365 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 65.7226 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4062 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -37.7290 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.5055 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 30.0563 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 56.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.8210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.9600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.8385 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 113.2778 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 50.3386 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 4.4542 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -4.5172 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 24.1018 -> Clearly above the moving-average trend level.

## TAILWINDS

### AMD Shares Climb as CEO Lisa Su Brushes Off Nvidia's Huang Turmoil, But the Real Opening Isn't Demand
- Summary: AMD Shares Climb as CEO Lisa Su Brushes Off Nvidia's Huang Turmoil, But the Real Opening Isn't Demand
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxPN1NUNGlyTGNwWHdmVDBTY2RVSWpGQkEtMnZ5bExGY0U1eHhOa2UxRFVKXzJJZXVaUktBeEppcFJaMnFsc1BhNGkyNUV1em9MdVdTM1JJQzNleGkzb0dFQmtlUlpyVi1haGRJb0tUQ0xRY1Ywd0ZyWXp0X0JQLVFTbDJ1eFFhMmJaVWFPLTNjaGtkN1pnODNQczkyVVV0YXNLdkw1ZnAwN294eGh1VVA4M3hIdXktbmlUNHJHd0xPRVdhRVJOTDhMTy1nNzk2TVliVE9sUjhSVDVhTDNw?oc=5>

### Advanced Micro Devices (NASDAQ:AMD) Stock Jumps 5.3% - Here's What Happened
- Summary: Advanced Micro Devices (NASDAQ:AMD) Stock Jumps 5.3% - Here's What Happened
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNQ2VqNnluNFQ3ZjBWTGlDMUFiU0tVR0NxbDlUNlYtNjNJSHYwYXlIZDk5d0padUQ0VzJ5ZUUxNFMyUGtQaW9tREhHNUJ6S2VwSjdaVkkySmp6aDNRMDdWN3IxY3RlOVBxdmpFUGRSU3YwMVEzNUhsT3dvSm5UZGxIVVpvTkJ2dzhweFpVWTY5eUJMeXFzZDFYcE4zZmdlZWNoUDgzYm10QXQxbWV0V21uMHFnZkI2ekk2SEZNN0dZTG45YWp2THBN?oc=5>

### AMD Stock Up 135% as Nvidia CEO Exit Tests a 100x P/E
- Summary: AMD Stock Up 135% as Nvidia CEO Exit Tests a 100x P/E
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNc1ljR2JaX3VQeTJad2dZS0JWQ18tZXc0S1kxYTFIZHF5WUNIcEd1eFE4MjRnV2RydVZxNDNjX1ppY01LRUQ0X3lIYkZ3NE5FdTRYa2NER1J3Z2Y2ZTM0NlByYmtOZkhrLVFieF9oWnM5cFp0TUg1bzduZGl5UWx2N3ZFTUNubjFvZU00Tm1uNVFtVXM0cGR4dXVWQWEtN1paMXhyRkdR?oc=5>

### AMD Stock Climbs After Nvidia's Blowout Results
- Summary: AMD Stock Climbs After Nvidia's Blowout Results
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxOeVQxR0RfOGhjaDZUY1VNSm5IYi0xX2NiRzI1d3lJdXpKRWlNbG1RVjZTOW1Yai1QUFFoOXlVVGVKcFZBdkdRTXU1azBJUHpCd0hmalVOSms5akhPUlcwRWhHM25md28tcE9IejcyMzhuaG53V2xHRHNwZzhCakU1UXQtOUt1U2l5dDA0MzdTcDVlRVNJX0lnWjAtZGl2czM4OFJSQ2RNZkNNUGs?oc=5>

### Nvidia’s soap opera could be AMD’s big opportunity. Here’s why I’m buying
- Summary: AMD may benefit from Nvidia’s struggles, presenting a buying opportunity for investors.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPVE5KOHVIeDZjZ0k0ZEtSYkk2SUNFOGdZNldnNG1mZDFZZmViVDRyY3loZG8yeDREUmpTelByT3NYeXdTOEV0eEZCaVFPOEMtdklVd2Q0RS1rNERIbl92V2xCVExqaXNkYTNUakMxSDVmTWctb0tyMFRwZy1iaTJ4Ti10ZDBEN1pwZGlN?oc=5>

### Why AMD Stock Was Sliding Today
- Summary: AMD shares fell today, indicating short-term weakness for the company.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNb2ctVEw4Q2ZFLXlpc2ZpeUFwaS0xSDI2Q2tRc2dtMzJmaGJwZjNoakZiTGxZVDhXUUJsWjRwR0dFamttd25sZWk4b0h6bDJZa3llbFE0YV9ub3NfbnItZ0xRejR0MzZoSy02bzh5bXVGWHJBLXVsQjN3ZHhmOXRWQlZJSEtONzQ5cXpsX0dxTGtuZWpnTDBn?oc=5>

### Advanced Micro Devices And 2 Other High Growth Stocks
- Summary: AMD highlighted among high growth stocks.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNTUhzLTRyOXRpNzlWd2hJcmhOS3A3MUtUUXdJQU4wOFpsWFktU0M5RHJMM1pHaDhTNEFLSFp6TEN2SzNVeTQtZ3czSXFqWVlldkJsQnJfLXViWWg5anBQMTdsb2JnTEZwcGFaZHQ0aHk3S2ZLM2VmZ0lBanp4Z1FDN3pUVXgyTTFrSVZxcnhTOUh6U0p1U1Q1d2FKRQ?oc=5>

## HEADWINDS

### AMD Stock Is Falling Monday: What's Going On?
- Summary: AMD Stock Is Falling Monday: What's Going On?
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNVEx2ZDZhQ3JoM0s1WnlsUE9icG5hQjRnT1pIR250WkNWU0ZkclVubEMwWmNOSFBSX3M3dGpsSHltWVdSRWZka3plbnlodFRVdTZTRFIzcUluNnJnRlVScFBtcEFkVXVPQkpmMVZabXZFRXlSUEotNnA5cWw2MnVFb0RNZTMxQThjS3pNNVBESl9ueUVjQm9jOHRkNA?oc=5>

### US Stock Futures Edge Lower After Tech Sell-Off — NVDA Earnings, AMD, SPCX, DIS In Focus
- Summary: Tech sell-off pressures AMD, reflecting negative market sentiment.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxQdzE5aHpjcnRIZTlvSV90VEhaU2o0b2NkSktXUW0ySTRjSG1KMC1IS2FZWUFkUTN3TlBqMjJJNzVZWURFTmlERXZNS2dOQ3J6c3g5SmxGNXo5eU0wbmt6eFJKQWRydFBvVFhCTHhYUlFfakhVOFJCTnVDS1g0UDVWQV9kdnR0cURfUHQ1anpzdmptNklBaUtpVmJZS0luZko0d0R0NHJYR1FNa0NlWDRGZHlMZjAxX1BFVVFFcFBHZVNqTkdGbUhnWFBfTTdhWm9nSllHVWdzV0FzcDZO?oc=5>

### Is NVIDIA’s Turmoil Advanced Micro Devices’ (AMD) Biggest Opening Yet?
- Summary: Nvidia turmoil may negatively impact AMD’s market performance.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPeE4zN25uZ3h5c01LT2hKdFVrSncwaTlUWXpTUmNKZnpBZnB6b01JQTFIaW9IRms3NFVMS1lTLWZPNWVFajh5Vl90WXdjdEwxX29aTWhjLWtLeExZelZXRkpaZmV3VzVzakN2VzgwRjFkbi1BZkVESTlXZGx5d05LYm1SNnZRdlRhUW9NQ2d6UEh1R05TRFA0Q1MxcmJ6LXFmclRVbg?oc=5>

## CATALYSTS

### AMD Stock Gets A New EPYC Launch And Quantum Computing Push
- Summary: AMD Stock Gets A New EPYC Launch And Quantum Computing Push
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNbFFCdEJNYmhzNmZINjg1anZuUWZiTjJoakpnSzBZWDd6TmJ2UnJfVHE3eFNqd1BsQUFfNGlmSFZnMmkxMEhSdG5mbVZ0ZUlMNFF6LUxDdEI0Ri1CcGdwbmQ4djk4RmlhV2JOVFZEc3dTay02YnUzS1NncTQxT0N5aUdibmFJZ0o1alFXbjh1T3VLdnU4aEE?oc=5>

### Broadcom Is Better Positioned Than AMD As Nvidia Struggles (NASDAQ:AMD)
- Summary: Comparison of AMD with Broadcom and Nvidia, suggesting Broadcom may outperform AMD.
- Date: 2026-11-16 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPeVNvOVdabnY3cFlGR0MtVm9ZcTRSRjlKS2t5WVBYbElRelBic3VORTdpYkZoclg3c3gxOHJ6b0NRLVNnbFUyTGdaMl9RQzREaWc4cl9wUEpCRXlyT1hoZkFzQkdsV3pvQ0F3V0FUWkw5dnkzUGVUYkVMM1N1RExBYUw5clJiVUN1UEJOQ0N1Z2I4cWVQcmpDREpWYkdEZFZm?oc=5>

### Why Chip Stocks Micron, AMD, and Broadcom Are Rising in Pre-Market Trading, November 18
- Summary: Pre‑market rise of AMD alongside Micron and Broadcom, indicating positive market sentiment.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxPYVFINDZtZU8yVzMzUFhBTU1iRW1kcW1iSTFURzg3Z01fNk91b0NBY3ZkSGtXM2FEZW5DaDc2LWZReFU4Ri1oZzBUakJPVFlvVDA0RVN3QmZJUFhKODVrMzkwQWZaczRwN2w1NWxIUTBrcVlIY0hPQUVOWnV0Xy1nNkpYVGY4a3M2aEp5NHN1WVlySXRQVUYxQzhxUUp0clJaeHBjWjFVRWpibkpvbFFXVGhSQlE?oc=5>

### Advanced Micro Devices, Inc. (AMD) Stock Price, News, Quote & History
- Summary: Provides current AMD stock price and historical data, no specific event.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMiUEFVX3lxTFBpN0UzZUJHblJ0QnhpWG5oU0tNSVRTVHctNS1mR1Uyc0dydFZxS2d6dkZzRmdsQ0tEZGIwQnJ4V3FndXU0Y3daMXNET0hON1U0?oc=5>

### Why Is Advanced Micro Devices Stock Rising Today?
- Summary: Explores reasons behind AMD's recent price increase.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPUkNPRlQ0VWdjd0dOeVdRWVVDZlUwOTg0YkFDRE9UXzJHOWFuVEVFMmIwU2xOSl9Ibi1vMTFPX0liLU80SzdaeVdWLTgtamhuSS1nMlV6QjZBMVN2N1ZjN2xqYmR3NHlWYm5kY1l6a0lQUGo1UVdycjNhbzV5cmZjYlRGNGxvTVpDRXpRMGpRWkxkaVA1bm9KcTBBaTg4QQ?oc=5>

### Advanced Micro Devices Inc Stock (AMD) Moved Up by 3.20% on Nov 18: A Full Analysis
- Summary: Analysis of AMD's 3.20% price gain on Nov 18.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQanVYb1JaZEtqWXNHSGRmaFRXczYzNlZPcnRnQ09VT1hSVTBQcFFlUEthdHpGcGtuMUFJVVQzc3dLcHpFS2VOV3Y5bW1EeXNtWWlTZXNaTmhsdjU0RzJTY3loOXJRM210T1M4cXBva01LTm4yQXlqUHJEZUo1WlVhTllxNzBnbGctN2c?oc=5>

### Advanced Micro Devices finalizes Taalas buyout: Can AMD stock build sustained upside?
- Summary: AMD completes acquisition of Taalas, potentially enhancing its product portfolio.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxQMl9fYU5XYWFkbzZTbDk5Ti1lSUNfRTBfaHlOM0ZLTHpidkxfNDNETVRENGpDRmg1TFZ6d1JtRmd2RnJfR2N1RURVeWVSS194ZEVwYzB2ZW5BaDhtWjEyZC1nOE80WHhObDVMM3psR1BSWk5aM3JBTkdUODhvazFIdktYaVg?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **113.28** | **12.71** | **77.44** | **44.70** | **877,416,480,768.00 USD** | **130.21** |
| NVDA | 16.21 | 23.33 | 18.50 | 105.90 | 3,645,231,071,232.00 USD | -16.56 |
| INTC | N/A | 2.53 | 15.85 | 20.90 | 290,571,026,432.00 USD | 59.25 |
| AVGO | 45.22 | 16.95 | 33.02 | 85.50 | 1,690,103,578,624.00 USD | 4.75 |

Peers fetched as_of: 2026-11-18; AMD reuses existing data (market data as_of: 2026-11-18); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-18

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,428,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi3AFBVV95cUxPN1NUNGlyTGNwWHdmVDBTY2RVSWpGQkEtMnZ5bExGY0U1eHhOa2UxRFVKXzJJZXVaUktBeEppcFJaMnFsc1BhNGkyNUV1em9MdVdTM1JJQzNleGkzb0dFQmtlUlpyVi1haGRJb0tUQ0xRY1Ywd0ZyWXp0X0JQLVFTbDJ1eFFhMmJaVWFPLTNjaGtkN1pnODNQczkyVVV0YXNLdkw1ZnAwN294eGh1VVA4M3hIdXktbmlUNHJHd0xPRVdhRVJOTDhMTy1nNzk2TVliVE9sUjhSVDVhTDNw?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNQ2VqNnluNFQ3ZjBWTGlDMUFiU0tVR0NxbDlUNlYtNjNJSHYwYXlIZDk5d0padUQ0VzJ5ZUUxNFMyUGtQaW9tREhHNUJ6S2VwSjdaVkkySmp6aDNRMDdWN3IxY3RlOVBxdmpFUGRSU3YwMVEzNUhsT3dvSm5UZGxIVVpvTkJ2dzhweFpVWTY5eUJMeXFzZDFYcE4zZmdlZWNoUDgzYm10QXQxbWV0V21uMHFnZkI2ekk2SEZNN0dZTG45YWp2THBN?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNc1ljR2JaX3VQeTJad2dZS0JWQ18tZXc0S1kxYTFIZHF5WUNIcEd1eFE4MjRnV2RydVZxNDNjX1ppY01LRUQ0X3lIYkZ3NE5FdTRYa2NER1J3Z2Y2ZTM0NlByYmtOZkhrLVFieF9oWnM5cFp0TUg1bzduZGl5UWx2N3ZFTUNubjFvZU00Tm1uNVFtVXM0cGR4dXVWQWEtN1paMXhyRkdR?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxOeVQxR0RfOGhjaDZUY1VNSm5IYi0xX2NiRzI1d3lJdXpKRWlNbG1RVjZTOW1Yai1QUFFoOXlVVGVKcFZBdkdRTXU1azBJUHpCd0hmalVOSms5akhPUlcwRWhHM25md28tcE9IejcyMzhuaG53V2xHRHNwZzhCakU1UXQtOUt1U2l5dDA0MzdTcDVlRVNJX0lnWjAtZGl2czM4OFJSQ2RNZkNNUGs?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPVE5KOHVIeDZjZ0k0ZEtSYkk2SUNFOGdZNldnNG1mZDFZZmViVDRyY3loZG8yeDREUmpTelByT3NYeXdTOEV0eEZCaVFPOEMtdklVd2Q0RS1rNERIbl92V2xCVExqaXNkYTNUakMxSDVmTWctb0tyMFRwZy1iaTJ4Ti10ZDBEN1pwZGlN?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNb2ctVEw4Q2ZFLXlpc2ZpeUFwaS0xSDI2Q2tRc2dtMzJmaGJwZjNoakZiTGxZVDhXUUJsWjRwR0dFamttd25sZWk4b0h6bDJZa3llbFE0YV9ub3NfbnItZ0xRejR0MzZoSy02bzh5bXVGWHJBLXVsQjN3ZHhmOXRWQlZJSEtONzQ5cXpsX0dxTGtuZWpnTDBn?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNTUhzLTRyOXRpNzlWd2hJcmhOS3A3MUtUUXdJQU4wOFpsWFktU0M5RHJMM1pHaDhTNEFLSFp6TEN2SzNVeTQtZ3czSXFqWVlldkJsQnJfLXViWWg5anBQMTdsb2JnTEZwcGFaZHQ0aHk3S2ZLM2VmZ0lBanp4Z1FDN3pUVXgyTTFrSVZxcnhTOUh6U0p1U1Q1d2FKRQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNVEx2ZDZhQ3JoM0s1WnlsUE9icG5hQjRnT1pIR250WkNWU0ZkclVubEMwWmNOSFBSX3M3dGpsSHltWVdSRWZka3plbnlodFRVdTZTRFIzcUluNnJnRlVScFBtcEFkVXVPQkpmMVZabXZFRXlSUEotNnA5cWw2MnVFb0RNZTMxQThjS3pNNVBESl9ueUVjQm9jOHRkNA?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxQdzE5aHpjcnRIZTlvSV90VEhaU2o0b2NkSktXUW0ySTRjSG1KMC1IS2FZWUFkUTN3TlBqMjJJNzVZWURFTmlERXZNS2dOQ3J6c3g5SmxGNXo5eU0wbmt6eFJKQWRydFBvVFhCTHhYUlFfakhVOFJCTnVDS1g0UDVWQV9kdnR0cURfUHQ1anpzdmptNklBaUtpVmJZS0luZko0d0R0NHJYR1FNa0NlWDRGZHlMZjAxX1BFVVFFcFBHZVNqTkdGbUhnWFBfTTdhWm9nSllHVWdzV0FzcDZO?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPeE4zN25uZ3h5c01LT2hKdFVrSncwaTlUWXpTUmNKZnpBZnB6b01JQTFIaW9IRms3NFVMS1lTLWZPNWVFajh5Vl90WXdjdEwxX29aTWhjLWtLeExZelZXRkpaZmV3VzVzakN2VzgwRjFkbi1BZkVESTlXZGx5d05LYm1SNnZRdlRhUW9NQ2d6UEh1R05TRFA0Q1MxcmJ6LXFmclRVbg?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNbFFCdEJNYmhzNmZINjg1anZuUWZiTjJoakpnSzBZWDd6TmJ2UnJfVHE3eFNqd1BsQUFfNGlmSFZnMmkxMEhSdG5mbVZ0ZUlMNFF6LUxDdEI0Ri1CcGdwbmQ4djk4RmlhV2JOVFZEc3dTay02YnUzS1NncTQxT0N5aUdibmFJZ0o1alFXbjh1T3VLdnU4aEE?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPeVNvOVdabnY3cFlGR0MtVm9ZcTRSRjlKS2t5WVBYbElRelBic3VORTdpYkZoclg3c3gxOHJ6b0NRLVNnbFUyTGdaMl9RQzREaWc4cl9wUEpCRXlyT1hoZkFzQkdsV3pvQ0F3V0FUWkw5dnkzUGVUYkVMM1N1RExBYUw5clJiVUN1UEJOQ0N1Z2I4cWVQcmpDREpWYkdEZFZm?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxPYVFINDZtZU8yVzMzUFhBTU1iRW1kcW1iSTFURzg3Z01fNk91b0NBY3ZkSGtXM2FEZW5DaDc2LWZReFU4Ri1oZzBUakJPVFlvVDA0RVN3QmZJUFhKODVrMzkwQWZaczRwN2w1NWxIUTBrcVlIY0hPQUVOWnV0Xy1nNkpYVGY4a3M2aEp5NHN1WVlySXRQVUYxQzhxUUp0clJaeHBjWjFVRWpibkpvbFFXVGhSQlE?oc=5
- https://news.google.com/rss/articles/CBMiUEFVX3lxTFBpN0UzZUJHblJ0QnhpWG5oU0tNSVRTVHctNS1mR1Uyc0dydFZxS2d6dkZzRmdsQ0tEZGIwQnJ4V3FndXU0Y3daMXNET0hON1U0?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPUkNPRlQ0VWdjd0dOeVdRWVVDZlUwOTg0YkFDRE9UXzJHOWFuVEVFMmIwU2xOSl9Ibi1vMTFPX0liLU80SzdaeVdWLTgtamhuSS1nMlV6QjZBMVN2N1ZjN2xqYmR3NHlWYm5kY1l6a0lQUGo1UVdycjNhbzV5cmZjYlRGNGxvTVpDRXpRMGpRWkxkaVA1bm9KcTBBaTg4QQ?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQanVYb1JaZEtqWXNHSGRmaFRXczYzNlZPcnRnQ09VT1hSVTBQcFFlUEthdHpGcGtuMUFJVVQzc3dLcHpFS2VOV3Y5bW1EeXNtWWlTZXNaTmhsdjU0RzJTY3loOXJRM210T1M4cXBva01LTm4yQXlqUHJEZUo1WlVhTllxNzBnbGctN2c?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxQMl9fYU5XYWFkbzZTbDk5Ti1lSUNfRTBfaHlOM0ZLTHpidkxfNDNETVRENGpDRmg1TFZ6d1JtRmd2RnJfR2N1RURVeWVSS194ZEVwYzB2ZW5BaDhtWjEyZC1nOE80WHhObDVMM3psR1BSWk5aM3JBTkdUODhvazFIdktYaVg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
