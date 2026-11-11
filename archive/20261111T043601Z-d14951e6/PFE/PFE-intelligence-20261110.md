# PFE Intelligence Report

- ticker: **PFE**
- Report as_of: **2026-11-10**
- Market data as_of: **2026-11-10**
- Quant sources: https://finance.yahoo.com/quote/PFE/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PFE/key-statistics/
- AI analysis snapshot as_of: **2026-11-10**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-11T04:46:26.508288+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 15, 'rule': 3, 'ai': 9, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261110T055129Z-abd33250/PFE** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 15 unique headlines; 10 named publishers; 0 exact duplicates; 15 HTTPS source links; largest publisher share 26.67%; oldest publication 2026-11-03

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 29.3600 |
| Return 1D (%) | 0.4448 |
| Return 1W (%) | -0.7044 |
| Return 1M (%) | 5.3348 |
| Return YTD (%) | 25.8081 |
| Return 1Y (%) | 28.4388 |
| Annualized volatility (%) | 21.6884 |
| Beta vs SPY | 0.2614 |
| Max drawdown (%) | -15.7243 |
| Sharpe (rf=0) | 1.2670 |
| Downside deviation (rf=0, %) | 14.0768 |
| Sortino (rf=0) | 1.9520 |
| Historical VaR 95% (1D, %) | 2.1427 |
| Historical ES 95% (1D, %) | 2.6741 |
| Correlation vs SPY | 0.1648 |
| Tracking error vs SPY (%) | 23.6549 |
| P/E (trailing) | 41.94 |
| P/B | 1.88 |
| EV/EBITDA | 8.69 |
| Revenue growth (%) | -0.40 |
| Forward P/E (estimate) | 10.00 |
| Gross margin (%) | 74.90 |
| Operating margin (%) | 33.38 |
| Return on equity (%) | 4.47 |
| Free cash flow yield (%) | 7.77 |
| MA50 | 28.3971 |
| Close vs MA50 (%) | 3.3910 |
| MA200 | 26.1354 |
| Close vs MA200 (%) | 12.3379 |
| RSI (14, Wilder) | 53.1235 |
| MACD (12,26) | 0.3655 |
| MACD signal (9) | 0.4680 |
| MACD histogram | -0.1025 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PFE': 279, 'SPY': 279}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 29.3600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.4448 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.7044 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 5.3348 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 25.8081 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 28.4388 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.6884 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.0768 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.9520 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1427 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6741 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1648 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.6549 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2614 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.7243 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.2670 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 9.9965 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.8980 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.3840 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 4.4680 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.7724 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 41.9429 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 53.1235 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1025 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.3910 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 12.3379 -> Clearly above the moving-average trend level.

## TAILWINDS

### Pfizer (PFE) Stock Looks Overvalued On Its 29% One Year Gain
- Summary: Pfizer (PFE) Stock Looks Overvalued On Its 29% One Year Gain
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPeGFIdkFCbTJ4ZjMxak5HTk5oVU5qcWFSRjRRZldJZDFnYlhrRzU1RzM1dXE1S2hzNW55LXZoN1U2QkNVM0czTnM0ZWp1a0tNR0FLUTh5U3JxSS1OWnBmTWNQeUhIZHV1LXA3bFRFcFFrWU04ck9kT0psLWl6NklmekdLM2VicmdUdlFJZnloZ0llOWVjamtGNE1ZQWdKUGM?oc=5>

### Pfizer hikes full-year outlook on new product growth, taps company veteran as new CFO
- Summary: Pfizer hikes full-year outlook on new product growth, taps company veteran as new CFO
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMickFVX3lxTFBfVElSNTY2SkVSU0NJOUpBalpLNVRMUThqV3ZTb1RwcVhkWndyUHdFTTFJZVNhWXJOWDRXckVMVHVRdU1TLTFGdlNBbmMtM0JDdzlSbEVwanJrUElJT1huRGhsdUJDa3JZUGtxRm8tcjJ0UdIBd0FVX3lxTE5sX2ZVWW5pM29Fc2RUZ2lhLV9uM2RidDdWLXFGRkhhcnhpQ0NfVjBpVFBPbDloZU9HdXVhaF9nZXFrUTR1eVEtLU9uWUhNaXNKSmJmV2J3MUNybnVnVkFPU19QeWZ5QUJPdmFHbExqbFFoNHVFbEF3?oc=5>

### Anyone can watch Pfizer's CEO at a healthcare conference on Nov. 17
- Summary: Pfizer CEO will speak at a healthcare conference on Nov. 17.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxPU3VOekRpWlJ2aHJmTWZzRkJfTDBTWHF6alRjRGlqZlBqVmpySGhBS2NPY1QtMXE0b0V3bFJMNm9fdDBfelI3MFNldldxLWl6elZSOVJQUlFfY2NaSm9qOHhTbmlKVFNqd3BYWU4yVjBtUUoxVjVESVZhdmp6cFB6MnRWSTFIZ3NMRE9RWUFpV2lHMlU1X1FFdHNwYUxvYUhpWXJnZjBSNG4xX0VzUTFEaW9QQ1VNUQ?oc=5>

### Analysts Are Bullish on These Healthcare Stocks: Sotera Health (SHC), Pfizer (PFE)
- Summary: Analysts express bullish outlook on Pfizer stock.
- Date: 2026-11-05 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi8gFBVV95cUxOZ0R5WFRSaFlDM0FJbWZSRGlWYVBYZmlZRTJIX3BTTG00OG9TZlhwUTNFMFFUT2JSeTN5MDh4WG4wRW1VQmZuZmlNNzFWVmVaTk1QWTlxMUtrZzlmT1M5cHpSSHB6SVVVQUM4cVF6VWVJWkdZX2FvTWJjUGhpd1RfTURjanAzQXNXeU5qdWhkQU1KT3B2Q1hubWhoWEwtTERoSkRYMWZYdHRoTXhyZGFCbEFyODZMNlNMSXo4QS1jSkVUODRNRHlEZi1fU2pZT0gtLW9YaUt2YWM3eXRtRzJFcDh1V090RHlwdF9FRmZlWmUyZw?oc=5>

## HEADWINDS

### Pfizer (PFE) Q3 Results Contrast Profit Rebound With Margin Pressure
- Summary: Pfizer (PFE) Q3 Results Contrast Profit Rebound With Margin Pressure
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxPalM1eTlURTd1NWRhQjBGWm4yeU0tREI1WkZiT3dqNXBqQWVES3hkSzBKTlNzZW9WLUJkSWJSN3k5N1lkTlpRZ1NidTJ5Z0ZRSHlHT05tMlpZV09lMHl2elRpMlFPZV9OdDZQanc1ZTZtZjFuTVRuSHVORXFKTXdkWUdrX0lkaGh2UVJzcWJtbWs3NlhaM0dzS3BPSFJJQ3Ewa2hiU1JuUzFiYjlMa2dmZWdwOGNDVklIbVdTVkJhQTdsWTlSb2RKeUZnUjBkLWxqeDFv0gHYAUFVX3lxTFBpTDBuX0pxekZXNlVERG1Wd0lxMTBrMThRSWN1Yy1wUFFUTUhDTTkxSk85b3ZBTHhDbFFwY0tveEl3ZER3QmpSM0dkMzV2UWZ0ekxCWnRfRU5NbE01N2g4TkRUSHA0LUNEcnhKQ0l6bW1fMFlrUTYtVmNyaURHY0Y2eXgtMTg5Q0tqcERyOTFZREE3WEdGUWNVQTh4RTBaWHNuMFNCaGNkM2dmTHRqZkhDN0JDUGNxZXpZbE5rU0V4OHFVamx1U3lpdS1TTGpMRVo5a1o0OHk0Sg?oc=5>

## CATALYSTS

### Pfizer Inc. (PFE) is Attracting Investor Attention: Here is What You Should Know
- Summary: Investor focus on Pfizer highlighted, no specific event announced.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQNEVrbjdIN3B6MElNNWRXOEEtRkdJdDNVeE8xWVhLOG5XT2JJQzZkOHdaU1hKZDZYeE9mLU9OaFdodGZuWEFlTXpwRVAyeDcxbEhFcU9EYUxROGR6cWNkWERWNzFINjcwT0wzUjM4bE1xOVBKaHpiSFQyOFZwUndYVWkwRFhvMG9VTk1BWFVqdi0xT2ZSYXExdmRuQTUxTWtj?oc=5>

### What Could Send Pfizer Stock Soaring?
- Summary: Speculation on factors that could boost Pfizer’s stock price.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNbmZ2UWVhQnFxckMwRkc4MzZ1c0o0STlHaFowd2ZxZnVhZEtIS09ZLUEwU1Z2d2pSeWxWdXZlNlRxcTFxOXQ0MGg2WXpSVVRCYmdHRzYzR2YxVHhEaEZhbUEyd0tTOUg2VEJxMG1RaWJHaDZvRjBqUjBnMU51QWRMWXMtMGZrQmJfX2NuN2dBMkFfOTFGRU5PVVN5UHRqWkk?oc=5>

### Pfizer (PFE) Stock Looks Attractive for Income Investors
- Summary: Income investors find Pfizer’s stock appealing due to dividend yield and stable earnings.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPQ2pCSkNOWGtCR09IaXRTWXhrcFN4NGRWNmViaklVUXA4dmFuelE0cjRaR3VNQUVDNXFEa0VscWdmaW5HQ0tXQjJwSlN4YkJldnpWMVg5R1BpYUhMaks3TmRrcVZ6Nk4wVkRRLXpnRUhFazdQOEJhMVFaOXN6R29INFYyZFZQSGk4cDR2c3pzdFVNb0lxMUVrVGJn?oc=5>

### Pfizer, Inc. (PFE) Stock Forecasts
- Summary: Analyst forecasts for Pfizer stock discussed.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxQV09Ia1VhZXBEWFF3Y0ZrYUNtUk9maWh4cjBzN19FbVc1WFRrTDFxME4yRWdkN1U2VVF2T2YtaGltZjZZamJfLVFrWmJGUE4tM2VIYzF3OVVWcFZvbk4wT2RlbHFvc1dVQjh4NGp4RjRSS3lwRG5rWU9nTExMR2FFTTJtT0IwWWxO?oc=5>

### Pfizer: The Portfolio Transformation Is Gaining Momentum (NYSE:PFE)
- Summary: Pfizer is actively reshaping its product portfolio, indicating strategic focus on high-growth areas.
- Date: 2026-11-05 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPWkhFWVJuMGRVSDktTlZ2VG16SVkxd2hDZ3ZpMmNzbjJpRG1uMk5wRzNlNWhKT0RPZlY0TTY3czZMZy1yc3ltdzMtcURXTUxDbjlWLVJESXFHWkNJVHJWZGhYNU5mSU5TcEprU3ZCNGlqaUhQVXVtWGR5VnNJTU41aVVhZUh1RjlsSW41SkhDQ3VwTGs4NUtVYU13R0U?oc=5>

### Pfizer Q3: The Street Is Pricing In Too Much Deceleration For This 5.7% Yield (NYSE:PFE)
- Summary: Market expects slower growth, affecting Q3 earnings outlook.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxOOHAyM3o1eVlzNVJKd2NBdnhsZXJuZXBBdjhSQUEtZllhNUs4WVY0aW5acGllSDBELWZuaWljMUtfWUZkdmZ1cC1icnN4Uzh6QWV5cUk5MWc4c0lFclBkRU0xNklod2hRdGtyVVZBLWVIY2dkSG1zSkFINTc2WVZDRmJ5Q0R3REZCaTlaZVU0X0U0cXlyZWpnT3hNZU5yUGVscFV5cUt5SEpMQklOTmxveFFQOTJhWVZycDJGdEZwS193QQ?oc=5>

### Pfizer Just Gained 12% in a Month to a 52-Week High: Take Profits, or Buy More?
- Summary: Pfizer shares surged 12% in a month, reaching a 52-week high, indicating strong market momentum.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxPdWR2N3E2eHExakpuX1VBVzR6YlVIb1RhNFYwSU9kVnZKemdoYXRXeEZoVnNYUzZlQVlLOWlabnA4aDEwQlU0XzNXMWNOMHBLVGNHSzRDOFVieF9DMHQ0UVgtYVp4RGpYRVFmMENCNmdER2t1cXRubWg3LW9qTmdBVkVaQnEyQm8?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PFE** | **41.94** | **1.88** | **8.69** | **-0.40** | **167,347,716,096.00 USD** | **28.44** |
| MRK | 149.55 | 8.14 | 13.88 | 4.70 | 364,979,617,792.00 USD | 75.67 |
| JNJ | 42.80 | 8.29 | 20.39 | 5.90 | 675,924,606,976.00 USD | 52.38 |
| LLY | 45.83 | 31.70 | 28.40 | 38.60 | 1,275,805,171,712.00 USD | 49.11 |

Peers fetched as_of: 2026-11-10; PFE reuses existing data (market data as_of: 2026-11-10); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-10

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 16,583,000,000.00 USD; period 2026-06-29/2026-09-27; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,242,000,000.00 USD; period 2026-06-29/2026-09-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/78003/000007800326000127/pfe-20260927.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMinwFBVV95cUxPeGFIdkFCbTJ4ZjMxak5HTk5oVU5qcWFSRjRRZldJZDFnYlhrRzU1RzM1dXE1S2hzNW55LXZoN1U2QkNVM0czTnM0ZWp1a0tNR0FLUTh5U3JxSS1OWnBmTWNQeUhIZHV1LXA3bFRFcFFrWU04ck9kT0psLWl6NklmekdLM2VicmdUdlFJZnloZ0llOWVjamtGNE1ZQWdKUGM?oc=5
- https://news.google.com/rss/articles/CBMickFVX3lxTFBfVElSNTY2SkVSU0NJOUpBalpLNVRMUThqV3ZTb1RwcVhkWndyUHdFTTFJZVNhWXJOWDRXckVMVHVRdU1TLTFGdlNBbmMtM0JDdzlSbEVwanJrUElJT1huRGhsdUJDa3JZUGtxRm8tcjJ0UdIBd0FVX3lxTE5sX2ZVWW5pM29Fc2RUZ2lhLV9uM2RidDdWLXFGRkhhcnhpQ0NfVjBpVFBPbDloZU9HdXVhaF9nZXFrUTR1eVEtLU9uWUhNaXNKSmJmV2J3MUNybnVnVkFPU19QeWZ5QUJPdmFHbExqbFFoNHVFbEF3?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxPU3VOekRpWlJ2aHJmTWZzRkJfTDBTWHF6alRjRGlqZlBqVmpySGhBS2NPY1QtMXE0b0V3bFJMNm9fdDBfelI3MFNldldxLWl6elZSOVJQUlFfY2NaSm9qOHhTbmlKVFNqd3BYWU4yVjBtUUoxVjVESVZhdmp6cFB6MnRWSTFIZ3NMRE9RWUFpV2lHMlU1X1FFdHNwYUxvYUhpWXJnZjBSNG4xX0VzUTFEaW9QQ1VNUQ?oc=5
- https://news.google.com/rss/articles/CBMi8gFBVV95cUxOZ0R5WFRSaFlDM0FJbWZSRGlWYVBYZmlZRTJIX3BTTG00OG9TZlhwUTNFMFFUT2JSeTN5MDh4WG4wRW1VQmZuZmlNNzFWVmVaTk1QWTlxMUtrZzlmT1M5cHpSSHB6SVVVQUM4cVF6VWVJWkdZX2FvTWJjUGhpd1RfTURjanAzQXNXeU5qdWhkQU1KT3B2Q1hubWhoWEwtTERoSkRYMWZYdHRoTXhyZGFCbEFyODZMNlNMSXo4QS1jSkVUODRNRHlEZi1fU2pZT0gtLW9YaUt2YWM3eXRtRzJFcDh1V090RHlwdF9FRmZlWmUyZw?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxPalM1eTlURTd1NWRhQjBGWm4yeU0tREI1WkZiT3dqNXBqQWVES3hkSzBKTlNzZW9WLUJkSWJSN3k5N1lkTlpRZ1NidTJ5Z0ZRSHlHT05tMlpZV09lMHl2elRpMlFPZV9OdDZQanc1ZTZtZjFuTVRuSHVORXFKTXdkWUdrX0lkaGh2UVJzcWJtbWs3NlhaM0dzS3BPSFJJQ3Ewa2hiU1JuUzFiYjlMa2dmZWdwOGNDVklIbVdTVkJhQTdsWTlSb2RKeUZnUjBkLWxqeDFv0gHYAUFVX3lxTFBpTDBuX0pxekZXNlVERG1Wd0lxMTBrMThRSWN1Yy1wUFFUTUhDTTkxSk85b3ZBTHhDbFFwY0tveEl3ZER3QmpSM0dkMzV2UWZ0ekxCWnRfRU5NbE01N2g4TkRUSHA0LUNEcnhKQ0l6bW1fMFlrUTYtVmNyaURHY0Y2eXgtMTg5Q0tqcERyOTFZREE3WEdGUWNVQTh4RTBaWHNuMFNCaGNkM2dmTHRqZkhDN0JDUGNxZXpZbE5rU0V4OHFVamx1U3lpdS1TTGpMRVo5a1o0OHk0Sg?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQNEVrbjdIN3B6MElNNWRXOEEtRkdJdDNVeE8xWVhLOG5XT2JJQzZkOHdaU1hKZDZYeE9mLU9OaFdodGZuWEFlTXpwRVAyeDcxbEhFcU9EYUxROGR6cWNkWERWNzFINjcwT0wzUjM4bE1xOVBKaHpiSFQyOFZwUndYVWkwRFhvMG9VTk1BWFVqdi0xT2ZSYXExdmRuQTUxTWtj?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNbmZ2UWVhQnFxckMwRkc4MzZ1c0o0STlHaFowd2ZxZnVhZEtIS09ZLUEwU1Z2d2pSeWxWdXZlNlRxcTFxOXQ0MGg2WXpSVVRCYmdHRzYzR2YxVHhEaEZhbUEyd0tTOUg2VEJxMG1RaWJHaDZvRjBqUjBnMU51QWRMWXMtMGZrQmJfX2NuN2dBMkFfOTFGRU5PVVN5UHRqWkk?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPQ2pCSkNOWGtCR09IaXRTWXhrcFN4NGRWNmViaklVUXA4dmFuelE0cjRaR3VNQUVDNXFEa0VscWdmaW5HQ0tXQjJwSlN4YkJldnpWMVg5R1BpYUhMaks3TmRrcVZ6Nk4wVkRRLXpnRUhFazdQOEJhMVFaOXN6R29INFYyZFZQSGk4cDR2c3pzdFVNb0lxMUVrVGJn?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxQV09Ia1VhZXBEWFF3Y0ZrYUNtUk9maWh4cjBzN19FbVc1WFRrTDFxME4yRWdkN1U2VVF2T2YtaGltZjZZamJfLVFrWmJGUE4tM2VIYzF3OVVWcFZvbk4wT2RlbHFvc1dVQjh4NGp4RjRSS3lwRG5rWU9nTExMR2FFTTJtT0IwWWxO?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPWkhFWVJuMGRVSDktTlZ2VG16SVkxd2hDZ3ZpMmNzbjJpRG1uMk5wRzNlNWhKT0RPZlY0TTY3czZMZy1yc3ltdzMtcURXTUxDbjlWLVJESXFHWkNJVHJWZGhYNU5mSU5TcEprU3ZCNGlqaUhQVXVtWGR5VnNJTU41aVVhZUh1RjlsSW41SkhDQ3VwTGs4NUtVYU13R0U?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxOOHAyM3o1eVlzNVJKd2NBdnhsZXJuZXBBdjhSQUEtZllhNUs4WVY0aW5acGllSDBELWZuaWljMUtfWUZkdmZ1cC1icnN4Uzh6QWV5cUk5MWc4c0lFclBkRU0xNklod2hRdGtyVVZBLWVIY2dkSG1zSkFINTc2WVZDRmJ5Q0R3REZCaTlaZVU0X0U0cXlyZWpnT3hNZU5yUGVscFV5cUt5SEpMQklOTmxveFFQOTJhWVZycDJGdEZwS193QQ?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxPdWR2N3E2eHExakpuX1VBVzR6YlVIb1RhNFYwSU9kVnZKemdoYXRXeEZoVnNYUzZlQVlLOWlabnA4aDEwQlU0XzNXMWNOMHBLVGNHSzRDOFVieF9DMHQ0UVgtYVp4RGpYRVFmMENCNmdER2t1cXRubWg3LW9qTmdBVkVaQnEyQm8?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
