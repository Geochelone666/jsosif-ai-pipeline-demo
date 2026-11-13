# PFE Intelligence Report

- ticker: **PFE**
- Report as_of: **2026-11-12**
- Market data as_of: **2026-11-12**
- Quant sources: https://finance.yahoo.com/quote/PFE/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PFE/key-statistics/
- AI analysis snapshot as_of: **2026-11-12**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-13T05:19:54.331744+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 9, 'rule': 2, 'ai': 5, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261112T054014Z-6c47e7f9/PFE** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 9 unique headlines; 7 named publishers; 0 exact duplicates; 9 HTTPS source links; largest publisher share 22.22%; oldest publication 2026-11-05

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 28.8300 |
| Return 1D (%) | -2.1053 |
| Return 1W (%) | -2.1053 |
| Return 1M (%) | 2.9963 |
| Return YTD (%) | 23.5371 |
| Return 1Y (%) | 18.9050 |
| Annualized volatility (%) | 21.2875 |
| Beta vs SPY | 0.2608 |
| Max drawdown (%) | -15.7243 |
| Sharpe (rf=0) | 0.9229 |
| Downside deviation (rf=0, %) | 14.2340 |
| Sortino (rf=0) | 1.3802 |
| Historical VaR 95% (1D, %) | 2.1449 |
| Historical ES 95% (1D, %) | 2.6741 |
| Correlation vs SPY | 0.1682 |
| Tracking error vs SPY (%) | 23.3115 |
| P/E (trailing) | 41.19 |
| P/B | 1.85 |
| EV/EBITDA | 8.57 |
| Revenue growth (%) | -0.40 |
| Forward P/E (estimate) | 9.78 |
| Gross margin (%) | 74.90 |
| Operating margin (%) | 29.07 |
| Return on equity (%) | 4.47 |
| Free cash flow yield (%) | 7.92 |
| MA50 | 28.4278 |
| Close vs MA50 (%) | 1.4147 |
| MA200 | 26.1774 |
| Close vs MA200 (%) | 10.1333 |
| RSI (14, Wilder) | 47.1352 |
| MACD (12,26) | 0.2602 |
| MACD signal (9) | 0.4054 |
| MACD histogram | -0.1451 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PFE': 281, 'SPY': 281}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 28.8300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.1053 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.1053 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.9963 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 23.5371 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 18.9050 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.2875 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.2340 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3802 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1449 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6741 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1682 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.3115 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2608 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.7243 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9229 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 9.7785 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.8980 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 29.0660 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 4.4680 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.9153 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 41.1857 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 47.1352 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1451 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.4147 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 10.1333 -> Clearly above the moving-average trend level.

## TAILWINDS

### Pfizer (PFE) Stock Looks Overvalued On Its 29% One Year Gain
- Summary: Pfizer (PFE) Stock Looks Overvalued On Its 29% One Year Gain
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPeGFIdkFCbTJ4ZjMxak5HTk5oVU5qcWFSRjRRZldJZDFnYlhrRzU1RzM1dXE1S2hzNW55LXZoN1U2QkNVM0czTnM0ZWp1a0tNR0FLUTh5U3JxSS1OWnBmTWNQeUhIZHV1LXA3bFRFcFFrWU04ck9kT0psLWl6NklmekdLM2VicmdUdlFJZnloZ0llOWVjamtGNE1ZQWdKUGM?oc=5>

### Pfizer (PFE) Lifts Guidance Following Pipeline Wins While Fair Value Looks Near Reach
- Summary: Pfizer (PFE) Lifts Guidance Following Pipeline Wins While Fair Value Looks Near Reach
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxOM3dwUUczT0QzVEhDd0lZRW5qQjZqa2dMbmZ3THVDNEo3YzV3N04tUm56SFUzTjM1T0t6UXhCWDU0TDVqVGZDYktIa1RGZnVLbWFVcWE5Mk9VelJXV0psdmh2V3pEZld3cXlwUDJmNmFscmNFdVhULVpSdkQxeGgtVW4yb3ZYeUhhTUtjU1JQUlJRdkdrQVRrckNYbEFDNGdDZE5hSzdwd0VvamRmNlZJbWowUTZIaVRGcTdCLUdWb1pGdldtRy1EQUY3LWpSb3hBMFAw0gHYAUFVX3lxTE1JRkh5YXg3ajRGSzE1ZkNCd1FxVGxEbEZzRU1tclE1N19MNUhxSEcxZ3pUYkJfWDhlNG04MkhNUFVoN1pSeVFCcFdTbUNnZ2pxWXFHZ2lucUlTUnpNckJsN1c0ai1nZkpSalpYS0NjV0lQXzdyNFAybS1qT3gzT1BscWNQbjR2NHQ0OG53X3lWVUg2aW1xY1huM2ZHWXM3bkJaWDBwOU8zNWQyMmd5SU9GUUtQMm1vbng5ejlEYW1mNHo4aWlfU1dxZUFaS3djOWxhSGJuRUhhOQ?oc=5>

### Anyone can watch Pfizer's CEO at a healthcare conference on Nov. 17
- Summary: Pfizer CEO will speak at a healthcare conference on Nov. 17.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxPU3VOekRpWlJ2aHJmTWZzRkJfTDBTWHF6alRjRGlqZlBqVmpySGhBS2NPY1QtMXE0b0V3bFJMNm9fdDBfelI3MFNldldxLWl6elZSOVJQUlFfY2NaSm9qOHhTbmlKVFNqd3BYWU4yVjBtUUoxVjVESVZhdmp6cFB6MnRWSTFIZ3NMRE9RWUFpV2lHMlU1X1FFdHNwYUxvYUhpWXJnZjBSNG4xX0VzUTFEaW9QQ1VNUQ?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Pfizer (PFE) Stock Looks Attractive for Income Investors
- Summary: Income investors find Pfizer’s stock appealing due to dividend yield and stable earnings.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPQ2pCSkNOWGtCR09IaXRTWXhrcFN4NGRWNmViaklVUXA4dmFuelE0cjRaR3VNQUVDNXFEa0VscWdmaW5HQ0tXQjJwSlN4YkJldnpWMVg5R1BpYUhMaks3TmRrcVZ6Nk4wVkRRLXpnRUhFazdQOEJhMVFaOXN6R29INFYyZFZQSGk4cDR2c3pzdFVNb0lxMUVrVGJn?oc=5>

### Pfizer: $1.5bn Of Blackstone Funding Doesn't Make Berobenatide A Winning Obesity Drug
- Summary: Pfizer receives $1.5bn Blackstone funding for obesity program, though drug success remains uncertain.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxPamZNcm1Fa1FNbXVNb2pId3JHMGU3V1doZzFnS1EyTi1hMmszR2Q4Rzc3QlVCbFprS0M5YUtYQUd0WXItdFRuSDVvYW9QRVNBVURUT01YUDd0VVFLZ1paTmd4Y1J3Vmt5cWlXSHF3bGt3S0tnWENsRmY4ajVNV1BkLVFmT0EydXFUTDd3RGpfQjBNblBVckJCc1RWOEZ0Sk1BS0h6U0NHY2hHdUZKS1FIZmNB?oc=5>

### Pfizer Secures Up to $1.5B Funding From Blackstone for Obesity Program
- Summary: Pfizer secures $1.5bn Blackstone funding to advance obesity drug development.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxPMFlGUHhEdXpRazlMaTMxUV81dllKc1RvMEtaUFV6Zk9IOW5jSGtqVGVaUHZJN0hkOHUzVzBpRjZBa21aY2x2ck4xZFoxUV9zWGE2aFpDemlRVlY3cGdMZmNCRGFEUG44dzdIYVE0dzl6dWtNMlRCNGIzVmpCWU9xTHdCRnBhRFNjQWd6Umlyb3owdW9RLXJWUmg4YjBQcTNEa3dCVEU2MXRZRG1TWEpVOE5HYlE5WHBVUE9SYUs1eEtKMUU?oc=5>

## RISKS

### Why Is Pfizer (PFE) Facing Fresh Global mRNA Patent Lawsuits?
- Summary: Pfizer faces new global mRNA patent lawsuits, potentially impacting its intellectual property and revenue streams.
- Date: 2026-11-11 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxQVkNiM1J2SEVuM0FuaHBpX0dmRUFhY1ZTV2RRb013LTQwN25PQ2FxcWprSkhvX2xKSEpDeXkzeml0R3VfYXNsMndhdVc2ZlZuSXF6MlNfbE9jOFlVdUtRSW80UmhyZF9TX3lqNF82aXJBdS1RNFlxWDdkYmd6WF9lYkpndDZWbUU0dVVhM3B3b05KRTRYdFpMTmxlcXNBZlRQMU80cXZFbENCTVp3RzlTTFhyNWE5ZUhxc0VVazlqQ3ROWGNYcEJqYW4xN2pWbUVr0gHWAUFVX3lxTE1hWU9FWDczMlRfV3kzRFJ4bXhYZDZmdzZJWmV1d1hpSnFDSThrTHRlU3JndE1FNk9ncUk0U0ZQekNSZlJ5M1BBajFjUTBhbnpYd1RiWUVFUkNOeFpUNk12NnNUS3VWZ3l6NWZHU1V3WlVid2lsbGhIWmFtZmFud1h1amdhU2h5UmRranpvb2tKczNGOFZ1MUF4Y1BGVmxvOWpEcjlUcmYwWHZscGFKbnd0WU1vc2ZtZWlIVUFINHU2T081NVRPc1hMQkJ0RHNHT1JzZk0yUEE?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PFE** | **41.19** | **1.85** | **8.57** | **-0.40** | **164,326,785,024.00 USD** | **18.91** |
| MRK | 148.43 | 8.07 | 13.79 | 4.70 | 362,267,836,416.00 USD | 65.41 |
| JNJ | 43.02 | 8.37 | 20.58 | 5.90 | 682,520,608,768.00 USD | 49.14 |
| LLY | 46.33 | 31.59 | 28.31 | 38.60 | 1,271,342,563,328.00 USD | 41.12 |

Peers fetched as_of: 2026-11-12; PFE reuses existing data (market data as_of: 2026-11-12); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-12

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
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxOM3dwUUczT0QzVEhDd0lZRW5qQjZqa2dMbmZ3THVDNEo3YzV3N04tUm56SFUzTjM1T0t6UXhCWDU0TDVqVGZDYktIa1RGZnVLbWFVcWE5Mk9VelJXV0psdmh2V3pEZld3cXlwUDJmNmFscmNFdVhULVpSdkQxeGgtVW4yb3ZYeUhhTUtjU1JQUlJRdkdrQVRrckNYbEFDNGdDZE5hSzdwd0VvamRmNlZJbWowUTZIaVRGcTdCLUdWb1pGdldtRy1EQUY3LWpSb3hBMFAw0gHYAUFVX3lxTE1JRkh5YXg3ajRGSzE1ZkNCd1FxVGxEbEZzRU1tclE1N19MNUhxSEcxZ3pUYkJfWDhlNG04MkhNUFVoN1pSeVFCcFdTbUNnZ2pxWXFHZ2lucUlTUnpNckJsN1c0ai1nZkpSalpYS0NjV0lQXzdyNFAybS1qT3gzT1BscWNQbjR2NHQ0OG53X3lWVUg2aW1xY1huM2ZHWXM3bkJaWDBwOU8zNWQyMmd5SU9GUUtQMm1vbng5ejlEYW1mNHo4aWlfU1dxZUFaS3djOWxhSGJuRUhhOQ?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxPU3VOekRpWlJ2aHJmTWZzRkJfTDBTWHF6alRjRGlqZlBqVmpySGhBS2NPY1QtMXE0b0V3bFJMNm9fdDBfelI3MFNldldxLWl6elZSOVJQUlFfY2NaSm9qOHhTbmlKVFNqd3BYWU4yVjBtUUoxVjVESVZhdmp6cFB6MnRWSTFIZ3NMRE9RWUFpV2lHMlU1X1FFdHNwYUxvYUhpWXJnZjBSNG4xX0VzUTFEaW9QQ1VNUQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPQ2pCSkNOWGtCR09IaXRTWXhrcFN4NGRWNmViaklVUXA4dmFuelE0cjRaR3VNQUVDNXFEa0VscWdmaW5HQ0tXQjJwSlN4YkJldnpWMVg5R1BpYUhMaks3TmRrcVZ6Nk4wVkRRLXpnRUhFazdQOEJhMVFaOXN6R29INFYyZFZQSGk4cDR2c3pzdFVNb0lxMUVrVGJn?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxPamZNcm1Fa1FNbXVNb2pId3JHMGU3V1doZzFnS1EyTi1hMmszR2Q4Rzc3QlVCbFprS0M5YUtYQUd0WXItdFRuSDVvYW9QRVNBVURUT01YUDd0VVFLZ1paTmd4Y1J3Vmt5cWlXSHF3bGt3S0tnWENsRmY4ajVNV1BkLVFmT0EydXFUTDd3RGpfQjBNblBVckJCc1RWOEZ0Sk1BS0h6U0NHY2hHdUZKS1FIZmNB?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxPMFlGUHhEdXpRazlMaTMxUV81dllKc1RvMEtaUFV6Zk9IOW5jSGtqVGVaUHZJN0hkOHUzVzBpRjZBa21aY2x2ck4xZFoxUV9zWGE2aFpDemlRVlY3cGdMZmNCRGFEUG44dzdIYVE0dzl6dWtNMlRCNGIzVmpCWU9xTHdCRnBhRFNjQWd6Umlyb3owdW9RLXJWUmg4YjBQcTNEa3dCVEU2MXRZRG1TWEpVOE5HYlE5WHBVUE9SYUs1eEtKMUU?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxQVkNiM1J2SEVuM0FuaHBpX0dmRUFhY1ZTV2RRb013LTQwN25PQ2FxcWprSkhvX2xKSEpDeXkzeml0R3VfYXNsMndhdVc2ZlZuSXF6MlNfbE9jOFlVdUtRSW80UmhyZF9TX3lqNF82aXJBdS1RNFlxWDdkYmd6WF9lYkpndDZWbUU0dVVhM3B3b05KRTRYdFpMTmxlcXNBZlRQMU80cXZFbENCTVp3RzlTTFhyNWE5ZUhxc0VVazlqQ3ROWGNYcEJqYW4xN2pWbUVr0gHWAUFVX3lxTE1hWU9FWDczMlRfV3kzRFJ4bXhYZDZmdzZJWmV1d1hpSnFDSThrTHRlU3JndE1FNk9ncUk0U0ZQekNSZlJ5M1BBajFjUTBhbnpYd1RiWUVFUkNOeFpUNk12NnNUS3VWZ3l6NWZHU1V3WlVid2lsbGhIWmFtZmFud1h1amdhU2h5UmRranpvb2tKczNGOFZ1MUF4Y1BGVmxvOWpEcjlUcmYwWHZscGFKbnd0WU1vc2ZtZWlIVUFINHU2T081NVRPc1hMQkJ0RHNHT1JzZk0yUEE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
