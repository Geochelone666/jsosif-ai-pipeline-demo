# CAT Intelligence Report

- ticker: **CAT**
- Report as_of: **2026-11-06**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/CAT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CAT/key-statistics/
- AI analysis snapshot as_of: **2026-11-06**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-07T04:40:51.656835+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 2, 'ai': 13, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261106T045829Z-1db1e5a7/CAT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 15 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 29.17%; oldest publication 2026-10-31

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 558.6300 |
| Return 1D (%) | 0.9013 |
| Return 1W (%) | -10.2963 |
| Return 1M (%) | -35.1479 |
| Return YTD (%) | -1.6565 |
| Return 1Y (%) | -1.1232 |
| Annualized volatility (%) | 40.7404 |
| Beta vs SPY | 1.7774 |
| Max drawdown (%) | -47.7898 |
| Sharpe (rf=0) | 0.1757 |
| Downside deviation (rf=0, %) | 29.2552 |
| Sortino (rf=0) | 0.2446 |
| Historical VaR 95% (1D, %) | 4.2437 |
| Historical ES 95% (1D, %) | 5.7878 |
| Correlation vs SPY | 0.5911 |
| Tracking error vs SPY (%) | 34.5067 |
| P/E (trailing) | 21.73 |
| P/B | 11.90 |
| EV/EBITDA | 16.81 |
| Revenue growth (%) | 17.30 |
| Forward P/E (estimate) | 17.32 |
| Gross margin (%) | 30.21 |
| Operating margin (%) | 20.81 |
| Return on equity (%) | 56.14 |
| Free cash flow yield (%) | 1.68 |
| MA50 | 758.8394 |
| Close vs MA50 (%) | -26.3836 |
| MA200 | 805.3668 |
| Close vs MA200 (%) | -30.6366 |
| RSI (14, Wilder) | 21.3252 |
| MACD (12,26) | -56.5942 |
| MACD signal (9) | -43.5923 |
| MACD histogram | -13.0018 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CAT': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 558.6300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.9013 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -10.2963 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -35.1479 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -1.6565 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -1.1232 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 40.7404 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 29.2552 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2446 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.2437 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.7878 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5911 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 34.5067 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.7774 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -47.7898 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1757 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.3205 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 30.2110 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 20.8100 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 56.1350 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.6815 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.7281 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 21.3252 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -13.0018 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -26.3836 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -30.6366 -> Clearly below the moving-average trend level.

## TAILWINDS

### Caterpillar Crashed By 25% Over 6 Months But This Global Banking Giant Says 85% Gains Will Come
- Summary: Analyst predicts 85% upside after 25% decline.
- Date: 2026-11-02 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNZkROdDhoUDNnTnpVcjhLWTdMWk91dk94d3o3T1JvbkdzeWphbjNLWTBpZU9GVkwtcTF2TFNTV0dvVnJRU3BVQ3BaNFFCNG56c2s3QUlZWnJKTHF6UDluV3VaaG1iblhCT1ZXVlV1UVZrLWVyeEw5aFlXRGxJZUVGUXVYbnQ2S2VKNmtaVUZCMHNWMHotXzM5eTBn?oc=5>

### Caterpillar Inc. (CAT) is Attracting Investor Attention: Here is What You Should Know
- Summary: Investor interest in CAT signals positive market sentiment.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOV1Jhck51RTVLT1FVR3dERFdBa3VIQUF4ekRrY0k5SWhFYWlTaklKM19EdkJ4NlNlU0NQR2c5QS1jcWFpUDVkWEpmVm1CVjJaRUhJR01jWG1YeXNrY21LWEVmX3lRNmRheFc3SXJmZFZWSFRya2JIMzNsUjdKQU95TzkwZkNBSkVyaTNfV2pHM1hNZ0loRkcxOW8yVFI3aVhudTMzS3IxVQ?oc=5>

### Caterpillar Inc. stock outperforms competitors on strong trading day
- Summary: CAT stock outperformed peers, indicating strong trading performance.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxPSkJPU0x4Rlg2eDlzZGtzckNDZ0xTSS0wak00aHZ3aDhkLTZ1d1VHWXB5b1lkN010WXExWFFfcGt6dnRBX3hmdUZlZndVQnEtb0l6b1hZbzVZQVZXZkNxY2RQRjlTelpnVVZpaFVmblZ6RDc5WnBBeXh2c25hMmg4U2pRaXZaQ0lLVjcxZjRxbUh5dHpObG9WMFZRUFlNLUVELVlrWkVDdUUyMXA4SGZLZHd4Z0NyOTV3amU3bFFsS2Vxbm9vb2pCamxKWmltZlg5RUJXM0RuV2FIUnFMM1E?oc=5>

### A dealer with 100+ years of customer ties is now owned by Caterpillar.
- Summary: Caterpillar acquires long‑standing dealer, expanding distribution network.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQdk5fYUZpMG1NbTN5cFBmZVV3YjJ4QXdBWDd4UTA0NGh3NEkwSGVVVjFwVlRZRVBNbnR0VGdGMXh6N05jeGVsR2hzbDRVc1pTWE1CSjR6TWJkTHFmZ3gxMGNzV09FSUszVzZpdTRadkxsdWlhVllJeVFrakRSd0xoQnVJOU9hV1BWUGxzWUk2Szk5REk?oc=5>

### Top 3 Industrials Stocks That May Rocket Higher In November
- Summary: Highlights potential upside for industrial stocks, including CAT, in November.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQTWVYUGFBWFJBb3VCU1owNmtTdVNWMVVISER3V0hMNGFYOVdhbjdKYkFxZXYzUFNBemgtUFhubXhqTHV1WEFNUTZhY2pBTWljVlZLMUxIWUdRclQzV1Q1M1dpc3dhX2pjMDQ2SnlOeFI2bllEdE9yYW83Q1ZOczFHRU5zZ2tmY0NEaFdhT1FkVVQyNHhyQ3VIeU0xYmliZ2F6dG5qV1l1Y1hyVHdnR0RpRTFEU1c4Zlc2NnFENGpXejJwUQ?oc=5>

### Caterpillar (CAT) Stock Looks Undervalued On Future Cash Flow
- Summary: CAT appears undervalued based on projected future cash flow.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxPVGoxYXJOVFIyVTZxQ2FWenNtdDhKM2M4cl9LNkRFdVBOMXg4cVQ2ZU5xcjh2aTV5ZC1lNU9rVkR1ajI5OFdPd2hnSlpHOEQta0Q5Uno5YWd1enBlU09GMUNScWlEZ0tjQnpzQmVnU3JGUnB1a3dIcDF0QTRSYi1HQ01BWGpHVGFvTzZkbXhNWmYxTklmalJmWlpjYjlDQkhQbjN0WjgwMjR0TG02Q293X2tCQWVmOHl4aHdyYTU2Y1NYblB5V2ZlcDl0NE1qd9IB0wFBVV95cUxNblpMSmZtUm9HTUl5YzEyMjl4bW5DWU9kZUhKTVRxbkhaVkM4cmp6MHdTUWFXb1R2X2M0UlBEQ182WFhhOWI3YU5vM0tmWHNUb0ZQYnN3OV9FWWk1UGEyLTdzOEF1V2lNUmg1RjhOT3YyZk9JYl9vYXE4ZXB1VmdiSHVrVnAzbU5ka1BxajJKYm5zMXdrdE1PZl9Pby1HVkZaaVN2TW12aVBPc0dHejFyWEd4UVdBaW1vQ0NhYS1Kamk1TThhWGNHZ3cyVzdfbEVQQUlN?oc=5>

## HEADWINDS

### Caterpillar (CAT) Stock Slides As Q3 Results Leave Tariff Questions
- Summary: Caterpillar (CAT) Stock Slides As Q3 Results Leave Tariff Questions
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOMlBwYlpXM2FiMVFzcHJtem9USGJuVU04NGNROUJWM0t6SmkzcFdPUllPSElXYjRuaDAyY0hGcDdkN3Z3RUUtb1VOeWJ3c183X3VLNU5zYlhKcDllZVVXcTE3aVdrekNHVjBrYUpUMlpQWl9uMElVbDFGSTdfdlNocERHZzhVMHZRVklvQ3hHYl9ZM19ZNWl1Nmt6dmg?oc=5>

### Caterpillar Stock’s (CAT) Sell-Off Has Gone Too Far. Here’s Why
- Summary: Indicates a significant sell-off in CAT shares, suggesting negative market sentiment.
- Date: 2026-11-06 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPQjM0clMzSlJzQzhJVml5LXFZOUYtaVNQNGFWZXNnRXNHMURDbHVSUndROGRzY0dUZlp0aXp4dl9mdlFLbVU2eFgxQzJCSE9jeHdZanQ0amYtSnRjaE9iVF9ZTXdxUDAzS3FmRVVVVkFCMG02RWx2SFE2c2JkSzBzd1NzUDhxWEhScjRyeTJjMkd6cGFFVkhmLTNMZ24?oc=5>

### The AI Trade Selloff Is Crushing Industrial Stocks. What Caterpillar’s Valuation Tells Us.
- Summary: Shows AI-driven selloff affecting industrial stocks, impacting CAT valuation negatively.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQMUJTRThwQm5WTzNHb2tfR2Y3VUVqRGEzZUF2ZEl3ZWVFTVB6VzdCVGluQll6UGdvSkducHBJdFNhenhXVHpHSnR0SUVmaHlVS1V1aGIzVndLUkRTNjlQNGhxU0FqVWNRX0gxeWtIS2I4cWhKOTBxbVhOaFhHbEJoZHdnTFFfcnFoX0U1Vkw2QS1heWc?oc=5>

### CAT Shares Fall Despite Q3 Earnings Beat: How to Play the Stock?
- Summary: CAT shares dropped even after Q3 earnings beat expectations.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQVjJ2QU4yQ2dnWldyc0VTQV9tV0xKRF9LRThnd1NxNll1bUlCTjZsMm5jR3pKQTNYYWQxTzJaS2NiV01DS2dYTUtNSVBKMVNOQWNnWTdxYlRGRzI5U0Q4YkpPcElYT2pqS294SHVEay1fZi15OFVkUHZOMV9jbEI2YmJMZ1dWRGoyaVR6MUtxVDFDYXhtVkE?oc=5>

### Caterpillar’s Sell-Off: Is the Market Missing Its AI Power Play?
- Summary: CAT experienced a sell‑off amid concerns over AI strategy.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxNdVAxamRuLTRSM0JRNW5uWWNnMEJ2V3BQbHRSeE1kSU83ZWRpdHg5WFhySnhMSVdVdGFhRmNXNGxGQ3lqTGxfaHAwaVplZjBLdGpFMERISmdDakpJNS1KZndKQ2U1QWw0X2loVU9ucTZhcUhVYzh4dHRGczR2MWlMNVpmRUJseUFtUzZielFDVUhOWEZqaldWdlRtb0t6czRtYzJRamlhbzhvWnpwT1BsNW95TnZ5bVZLQzhoMFBDRzJBNnlaakt5Z1pxSXNpTVN6VmJ0aGh1U0RTZ0NkV2c?oc=5>

## CATALYSTS

### Caterpillar Inc. Acquires Fabick Cat Dealership
- Summary: Caterpillar Inc. Acquires Fabick Cat Dealership
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNdWhHeHNNemRFWjlvaERmMFhnVDNDanZvZGdlU282QzRoSkJvLVJqakQ1XzNBYnQyR0ozdXhYRlZVVjY4c2JaUGlMYWZRMmNFazZfUEdZQU84WWVKRzlndjhDbkJuZFNuakpvQjZQZ2NXTHpZb3o2b2Q3cVlpZzczcW5OT1RMWEt6YnZKNGVDejlIODNSVFd0ZDBJR3ptQThTV0E?oc=5>

### What Could Caterpillar (CAT) Gain From This Dealer Acquisition?
- Summary: Potential dealer acquisition could boost CAT's market reach.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOMjZvcW9FcFFlNFJTUXVNVEswUjUzNmZCYVlCVlNBUThjLUVXOFR5RHpMQm5jLWZmdF9BQnJmdU5DeWhaRkYzQTJxU3VCNEozaExWRGFQblJUTXJiNTU3ZEFNTHdncjRNQ3ZMMmtIckxkd0NmUGxOUlBFUDVpSW5RVlpqZHpiT2hpMTZMV09Rd2NyRC1YMlIzRUNEMkdxcFE?oc=5>

### A $1 billion investment targets more factory capacity in North Carolina. Caterpillar is expected to discuss it Nov. 17.
- Summary: CAT plans a $1B investment to expand factory capacity in NC.
- Date: 2026-11-06 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPOGZ2ck5XZGsxeDJkX05JWjhvcHRORnl0OEZWcjRDdXRJcjZUSUJ3d0RxQS1mS2pLTG02d29wOG5MN1F2Q3NRRmxZN1FLbTVON3lsckRUUHY2UlhMTGRLZi11QzRLLU1wakdQNkxfZV9Ndy1YYXZqdDVOLXpIdHhYWk1RLWdBd2Y1VHM4WHMtckxmc1FKVWlVb2xadkg3RkdxajVlSGtTNlR5d2NqdFdaVGZmVUpwZEU2NjJ1MA?oc=5>

## RISKS

### Caterpillar Inc Stock (CAT) Moved Down by 5.03% on Nov 5: Drivers Behind the Movement
- Summary: CAT shares fell 5.03% on Nov 5 due to market selloff and valuation concerns.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQVE5MSkpSQ0tVbnVQMUlxdG5KWno4SDFhc1F6ZXhXcDlMODFxSDJIdzNDMktxeDFWWlVPQ2tOMF9UMkZnaFl3Zk9mZFEyUV93NE1CSFZvWVNPc2lRei1JNU5LSWFyM2FVVHlUWHRLZkM3UG5ZeFdISDBRSHlxOXRKbDBZdmhXc0pHNVE?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CAT** | **21.73** | **11.90** | **16.81** | **17.30** | **255,625,838,592.00 USD** | **-1.12** |
| DE | 36.86 | 6.47 | 27.77 | 4.90 | 181,093,908,480.00 USD | 42.90 |
| CNH | 46.24 | 1.84 | 37.29 | 2.00 | 18,590,314,496.00 USD | 13.76 |
| CMI | 18.78 | 5.03 | 14.02 | 9.40 | 61,958,651,904.00 USD | -1.33 |

Peers fetched as_of: 2026-11-06; CAT reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-06

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 20,682,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 1,141,000,000.00 USD; period 2011-07-01/2011-09-30; fiscal year/reporting period 2011/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/18230/000001823026000057/cat-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimgFBVV95cUxNZkROdDhoUDNnTnpVcjhLWTdMWk91dk94d3o3T1JvbkdzeWphbjNLWTBpZU9GVkwtcTF2TFNTV0dvVnJRU3BVQ3BaNFFCNG56c2s3QUlZWnJKTHF6UDluV3VaaG1iblhCT1ZXVlV1UVZrLWVyeEw5aFlXRGxJZUVGUXVYbnQ2S2VKNmtaVUZCMHNWMHotXzM5eTBn?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOV1Jhck51RTVLT1FVR3dERFdBa3VIQUF4ekRrY0k5SWhFYWlTaklKM19EdkJ4NlNlU0NQR2c5QS1jcWFpUDVkWEpmVm1CVjJaRUhJR01jWG1YeXNrY21LWEVmX3lRNmRheFc3SXJmZFZWSFRya2JIMzNsUjdKQU95TzkwZkNBSkVyaTNfV2pHM1hNZ0loRkcxOW8yVFI3aVhudTMzS3IxVQ?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxPSkJPU0x4Rlg2eDlzZGtzckNDZ0xTSS0wak00aHZ3aDhkLTZ1d1VHWXB5b1lkN010WXExWFFfcGt6dnRBX3hmdUZlZndVQnEtb0l6b1hZbzVZQVZXZkNxY2RQRjlTelpnVVZpaFVmblZ6RDc5WnBBeXh2c25hMmg4U2pRaXZaQ0lLVjcxZjRxbUh5dHpObG9WMFZRUFlNLUVELVlrWkVDdUUyMXA4SGZLZHd4Z0NyOTV3amU3bFFsS2Vxbm9vb2pCamxKWmltZlg5RUJXM0RuV2FIUnFMM1E?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxQdk5fYUZpMG1NbTN5cFBmZVV3YjJ4QXdBWDd4UTA0NGh3NEkwSGVVVjFwVlRZRVBNbnR0VGdGMXh6N05jeGVsR2hzbDRVc1pTWE1CSjR6TWJkTHFmZ3gxMGNzV09FSUszVzZpdTRadkxsdWlhVllJeVFrakRSd0xoQnVJOU9hV1BWUGxzWUk2Szk5REk?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQTWVYUGFBWFJBb3VCU1owNmtTdVNWMVVISER3V0hMNGFYOVdhbjdKYkFxZXYzUFNBemgtUFhubXhqTHV1WEFNUTZhY2pBTWljVlZLMUxIWUdRclQzV1Q1M1dpc3dhX2pjMDQ2SnlOeFI2bllEdE9yYW83Q1ZOczFHRU5zZ2tmY0NEaFdhT1FkVVQyNHhyQ3VIeU0xYmliZ2F6dG5qV1l1Y1hyVHdnR0RpRTFEU1c4Zlc2NnFENGpXejJwUQ?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxPVGoxYXJOVFIyVTZxQ2FWenNtdDhKM2M4cl9LNkRFdVBOMXg4cVQ2ZU5xcjh2aTV5ZC1lNU9rVkR1ajI5OFdPd2hnSlpHOEQta0Q5Uno5YWd1enBlU09GMUNScWlEZ0tjQnpzQmVnU3JGUnB1a3dIcDF0QTRSYi1HQ01BWGpHVGFvTzZkbXhNWmYxTklmalJmWlpjYjlDQkhQbjN0WjgwMjR0TG02Q293X2tCQWVmOHl4aHdyYTU2Y1NYblB5V2ZlcDl0NE1qd9IB0wFBVV95cUxNblpMSmZtUm9HTUl5YzEyMjl4bW5DWU9kZUhKTVRxbkhaVkM4cmp6MHdTUWFXb1R2X2M0UlBEQ182WFhhOWI3YU5vM0tmWHNUb0ZQYnN3OV9FWWk1UGEyLTdzOEF1V2lNUmg1RjhOT3YyZk9JYl9vYXE4ZXB1VmdiSHVrVnAzbU5ka1BxajJKYm5zMXdrdE1PZl9Pby1HVkZaaVN2TW12aVBPc0dHejFyWEd4UVdBaW1vQ0NhYS1Kamk1TThhWGNHZ3cyVzdfbEVQQUlN?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOMlBwYlpXM2FiMVFzcHJtem9USGJuVU04NGNROUJWM0t6SmkzcFdPUllPSElXYjRuaDAyY0hGcDdkN3Z3RUUtb1VOeWJ3c183X3VLNU5zYlhKcDllZVVXcTE3aVdrekNHVjBrYUpUMlpQWl9uMElVbDFGSTdfdlNocERHZzhVMHZRVklvQ3hHYl9ZM19ZNWl1Nmt6dmg?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPQjM0clMzSlJzQzhJVml5LXFZOUYtaVNQNGFWZXNnRXNHMURDbHVSUndROGRzY0dUZlp0aXp4dl9mdlFLbVU2eFgxQzJCSE9jeHdZanQ0amYtSnRjaE9iVF9ZTXdxUDAzS3FmRVVVVkFCMG02RWx2SFE2c2JkSzBzd1NzUDhxWEhScjRyeTJjMkd6cGFFVkhmLTNMZ24?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxQMUJTRThwQm5WTzNHb2tfR2Y3VUVqRGEzZUF2ZEl3ZWVFTVB6VzdCVGluQll6UGdvSkducHBJdFNhenhXVHpHSnR0SUVmaHlVS1V1aGIzVndLUkRTNjlQNGhxU0FqVWNRX0gxeWtIS2I4cWhKOTBxbVhOaFhHbEJoZHdnTFFfcnFoX0U1Vkw2QS1heWc?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQVjJ2QU4yQ2dnWldyc0VTQV9tV0xKRF9LRThnd1NxNll1bUlCTjZsMm5jR3pKQTNYYWQxTzJaS2NiV01DS2dYTUtNSVBKMVNOQWNnWTdxYlRGRzI5U0Q4YkpPcElYT2pqS294SHVEay1fZi15OFVkUHZOMV9jbEI2YmJMZ1dWRGoyaVR6MUtxVDFDYXhtVkE?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxNdVAxamRuLTRSM0JRNW5uWWNnMEJ2V3BQbHRSeE1kSU83ZWRpdHg5WFhySnhMSVdVdGFhRmNXNGxGQ3lqTGxfaHAwaVplZjBLdGpFMERISmdDakpJNS1KZndKQ2U1QWw0X2loVU9ucTZhcUhVYzh4dHRGczR2MWlMNVpmRUJseUFtUzZielFDVUhOWEZqaldWdlRtb0t6czRtYzJRamlhbzhvWnpwT1BsNW95TnZ5bVZLQzhoMFBDRzJBNnlaakt5Z1pxSXNpTVN6VmJ0aGh1U0RTZ0NkV2c?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNdWhHeHNNemRFWjlvaERmMFhnVDNDanZvZGdlU282QzRoSkJvLVJqakQ1XzNBYnQyR0ozdXhYRlZVVjY4c2JaUGlMYWZRMmNFazZfUEdZQU84WWVKRzlndjhDbkJuZFNuakpvQjZQZ2NXTHpZb3o2b2Q3cVlpZzczcW5OT1RMWEt6YnZKNGVDejlIODNSVFd0ZDBJR3ptQThTV0E?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxOX1VPeTVFYkM0SlAxUUZ0Tjl5WHlNRnVxYlZ2dHlBLUVSVWpoSzdKR2JGWVNfRzVPZ3FPaVJiYzRaOFJxNUZ3OEdYUFFUOWt4NU16MWlXZW1mQXJNQnlLSTZBc0xoUHRzV0ZwSWJmc3JhSXFBQnVWNXpQSlNoSWJjc0t5VFQ5ZUxKT3hCVHgzcWZ5eWlZS2ZZTElOSlFudGJ5dXh0cmJVZWlvSW8?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOMjZvcW9FcFFlNFJTUXVNVEswUjUzNmZCYVlCVlNBUThjLUVXOFR5RHpMQm5jLWZmdF9BQnJmdU5DeWhaRkYzQTJxU3VCNEozaExWRGFQblJUTXJiNTU3ZEFNTHdncjRNQ3ZMMmtIckxkd0NmUGxOUlBFUDVpSW5RVlpqZHpiT2hpMTZMV09Rd2NyRC1YMlIzRUNEMkdxcFE?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPOGZ2ck5XZGsxeDJkX05JWjhvcHRORnl0OEZWcjRDdXRJcjZUSUJ3d0RxQS1mS2pLTG02d29wOG5MN1F2Q3NRRmxZN1FLbTVON3lsckRUUHY2UlhMTGRLZi11QzRLLU1wakdQNkxfZV9Ndy1YYXZqdDVOLXpIdHhYWk1RLWdBd2Y1VHM4WHMtckxmc1FKVWlVb2xadkg3RkdxajVlSGtTNlR5d2NqdFdaVGZmVUpwZEU2NjJ1MA?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQVE5MSkpSQ0tVbnVQMUlxdG5KWno4SDFhc1F6ZXhXcDlMODFxSDJIdzNDMktxeDFWWlVPQ2tOMF9UMkZnaFl3Zk9mZFEyUV93NE1CSFZvWVNPc2lRei1JNU5LSWFyM2FVVHlUWHRLZkM3UG5ZeFdISDBRSHlxOXRKbDBZdmhXc0pHNVE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
