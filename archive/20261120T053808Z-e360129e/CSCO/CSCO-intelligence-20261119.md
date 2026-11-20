# CSCO Intelligence Report

- ticker: **CSCO**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-19**
- Quant sources: https://finance.yahoo.com/quote/CSCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CSCO/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T05:55:48.200891+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 2, 'ai': 15, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261119T054856Z-9eb86811/CSCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'low_uncalibrated_model_confidence': 3}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 7 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 40.91%; oldest publication 2026-11-13

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 94.7000 |
| Return 1D (%) | -2.5520 |
| Return 1W (%) | -7.1660 |
| Return 1M (%) | -11.0798 |
| Return YTD (%) | 25.2151 |
| Return 1Y (%) | 23.0427 |
| Annualized volatility (%) | 37.2170 |
| Beta vs SPY | 1.2942 |
| Max drawdown (%) | -27.2567 |
| Sharpe (rf=0) | 0.7459 |
| Downside deviation (rf=0, %) | 26.3302 |
| Sortino (rf=0) | 1.0544 |
| Historical VaR 95% (1D, %) | 3.2126 |
| Historical ES 95% (1D, %) | 5.5834 |
| Correlation vs SPY | 0.4833 |
| Tracking error vs SPY (%) | 32.8369 |
| P/E (trailing) | 25.87 |
| P/B | 7.22 |
| EV/EBITDA | 18.79 |
| Revenue growth (%) | 24.40 |
| Forward P/E (estimate) | 15.64 |
| Gross margin (%) | 64.07 |
| Operating margin (%) | 27.17 |
| Return on equity (%) | 30.38 |
| Free cash flow yield (%) | 2.79 |
| MA50 | 106.5561 |
| Close vs MA50 (%) | -11.1266 |
| MA200 | 102.0536 |
| Close vs MA200 (%) | -7.2057 |
| RSI (14, Wilder) | 37.9941 |
| MACD (12,26) | -3.5317 |
| MACD signal (9) | -3.1832 |
| MACD histogram | -0.3485 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CSCO': 286, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 94.7000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.5520 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -7.1660 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -11.0798 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 25.2151 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 23.0427 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 37.2170 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.3302 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.0544 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.2126 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.5834 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4833 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.8369 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.2942 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.2567 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7459 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.6352 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 64.0740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 27.1720 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 30.3800 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.7883 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 25.8743 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 37.9941 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.3485 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -11.1266 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -7.2057 -> Clearly below the moving-average trend level.

## TAILWINDS

### Cisco upgraded to Buy at HSBC as firm sees 'attractive valuation' (CSCO:NASDAQ)
- Summary: Cisco upgraded to Buy at HSBC as firm sees 'attractive valuation' (CSCO:NASDAQ)
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPaG5CX1poZ0t3MEsyRjk0SGVNNmdEYWRjQkdYX3g2TU9RUHJ3bGs3SHp6UTZnVnQ5R2RodTlYY3lwRk82SXM1elhGaThlcEFGRTluOUkzQ1d2bDk0UzdQMGNPSGg2NERYNGZ1ZldzWjQyOWppQVFUeG9RM0xPeUQxemxybmV0NWpXcW9GdTUxd2hpaUJYc3JXTzFKM1FpWE5GZU5F?oc=5>

### Cisco: Its $22 Billion AI Supply Bet Looks Worth Taking
- Summary: Cisco invests $22B in AI supply chain, signaling strategic expansion.
- Date: 2026-11-19 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPRVVEN2VyeUR1UFJzOXczaW1IQ1dfOTBzWEsyc2YycmZZUTR6YVgtUmw3Q2dZQ3pGNWZhU294VWd1ZnYzV0Mtc180ancyUENfVHhnM1QwZ1BJRkNEZUVkZjhENm9CbGFpY0hhcHRwOWhoYmIzMmpfZzZ5YUpEQjF4REYyNzlBbkxfdzNUV3dUdHFXbm8wRVRtUVJB?oc=5>

### Cisco posts its best growth in 15 years. Why isn't Wall Street buying?
- Summary: Cisco records 15‑year high growth, yet market underreacts.
- Date: 2026-11-16 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNaEZDb3R6LWM1R0FOem9SZXYtSWMyT3VwbTEyWFRBVnNLTzlPWGJhQWtLdGcyU3NfYkNTdWxnc0QxMFBBYzhjS21mN1JiRVlXeUd5WDExOHo3VmtNWnhval9SUnB2djdmenh4TzRqRG1KVW1aeG5kUGNFUU1IdVR6OHN2bXdhb3lxVXUzc1VMQzM2Q29WYmc?oc=5>

### Cisco Had A Very Good Quarter And A Quick Look At Nvidia’s Estimates Before Reporting
- Summary: Cisco reports strong quarter, referencing Nvidia estimates.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxOTnlNUDNGWjAyU05oM1Bpem94c0hLd19USzZxSElzQlhIN2x3X21XTGlUS3IwV0FLYkJmYl9sQ05yanlTZWtpRS1faUdZeUFzaFdQemhBczRMdVBMQmRYS2NtVUZJSURneDJOcDZoQlQ0UHJpTm5VVnVJSjBTVDFILTFBWUxoMUpvSXFTcm1mTG9DMi1TN0Y4b09aejQ2T2dvLXJRekpIR2ZkV3hrTUE?oc=5>

## HEADWINDS

### Cisco’s CEO Just Sold $27 Million of Stock in 3 Days
- Summary: CEO sold $27M stock over 3 days, raising concerns.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxObk1wZmhoMzladm0wOVlmakNfWXdhTWN1ZHZ2WmFfVzN0OTVBWVpvMW1vY290c1hyalBfMS1vcGVzWXNidFFlUGtZSjJ6UXpnQ1JyNktMVEg3RklqdnYzZ1o3cEpETlRpUXRNNUdoUmJfY21QQXczRGpWU280c3FTRUZqR1U0elNSSGRvWHBpb3M?oc=5>

### Why Cisco Systems (CSCO) Stock Is Down Today
- Summary: Stock decline today indicates short-term market pressure.
- Date: 2026-11-13 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxOMnlUbGVDUnBVbDMwa3QzUTJwbE11YlF3OUpLNkNRTzlXaFNRVUlNN1hpNVk4Y0J4a3dENjl2OHJfdmk0djBjSjhCdGo3Q0JSLWMyTW5wWjNHdW5QekoyWkhlZ0xjSDEtVU8yZjM4Z0RIMnhORThzTnV1ZmhadGlpREJLS2xZbGlo?oc=5>

### Cisco Systems (CSCO) executive Nichlas A. Fink sells 3,287 shares under a prearranged plan.
- Summary: Insider sale may signal lack of confidence.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxOMXNHdFp6SjlGRFIxaTJyemhVZWxfRDJWSF8ydmlWbm1VOS0xVTZMVFMyOUpaTHZSZy1SVEEyTUxYY2hBdFRlWGpJRG9NcDJlMThOcW9JZHM0N3hzazVvV1hRVXhOZ2pCX3ljY29sejh0R0RUeUo4cmpwdFdMNi04di1XTzdEbEFNdG5qb2ZnVW1iV1R6MEZWYkN5SVQzckFUTzN6SWpLeXVkMFVWR05hUQ?oc=5>

### Over three days, Cisco Systems (CSCO) CEO Charles Robbins sold company stock in 11 trades.
- Summary: CEO stock sales raise concerns about company outlook.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQcFAtMzM5Q0dnamlhSllqMzRyR0lzUTdVWnFEcWlvaVQwTGVDWFRIc3p1elBmRXk1alFFUDBxbkl0dnRET1hpSjAzdUpia2ZKSkQtY2JZN0VVYS1kN2ZHMjBNU0tiYWFJVnp6Ul9mRTBHUEw3QWotMkFkTjBLMGhHMHlfYzlNb09iWVJfVS1QY1Bia21wakVSRlpWMjVMSmFaV0R4Z095cllacldjODZhMA?oc=5>

## CATALYSTS

### Cisco (CSCO) Stock Gets Fair Value Trim As Analysts Cut Targets After Strong Q1
- Summary: Cisco (CSCO) Stock Gets Fair Value Trim As Analysts Cut Targets After Strong Q1
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOd0psSW1iRElNXzlmeTI0QTZrM1J1UU5QaUJnS1J4NXFMYzhMM2dvb3dxeG5zSHRFTG5IRkhPTklXMy1vM01GaDBRSlRYNjQxM3E2aEZtYXlyTEdRR0x3STNMMUlyQ1A4aWNERVNQTW1RazVaZUc2WFJ2UjY1eVVUanA2U3ZGMXZITlRJOVRNeF9QTzhJaHc?oc=5>

### What Did Cisco’s Quarter Change For Its Stock?
- Summary: Cisco’s latest quarterly results and their impact on the stock price.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPZkpSempEOHAyWU5QVVlKUGw2Zl81RHBKRnBGT3ljMmQ5Q21VazV1azg0ZzdUek5zZHQ0MVZfRkJGVWNzQXpHUkk5dVVZMENON3JuYWJsQ3RDVlVqNS1FeGp1dUprLUFWSnUxd0xDdFg2dUJmZ2tXVU9HS2RyaHJKeEVVTmZULUpoUVlDZzVjNHVNMGVfNTRiOC11OG5sbkhEVzhZODRlMlg?oc=5>

### Cisco: Better Earnings, Cheaper Stock (NASDAQ:CSCO)
- Summary: Cisco reports improved earnings and a lower stock price, indicating stronger financial performance and potential upside for investors.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxOQW1JNjZlRklwSUJiX3pwLW13UG5WZF9NbTc3Mlk4dmhTeUNReWlfLWloUFNrbG5GY3ZfczdIZ0tHbUI0VGZ4dGFub252Z3dfMTdGX0ZDQi1LRVVxYW1wdkhlLXRhbzAyMXhsMHVUcXExRWlHbW52N2EyRlQ0OThlOWhB?oc=5>

### Cisco Drops 7% Post Earnings: Should You Buy the Stock on the Dip?
- Summary: Cisco’s earnings miss caused a 7% drop, prompting investors to consider buying at the dip.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOR2gxQW9fU2tUZlVfZ3k0RGw2UF9KWjAwVGVFUFU4c2R1VE5PWERjTkMtNnF6OUNQNjYtQzhsN1RrUFU0OHU1MjJaeS0wYUdIdlY1TmVpajRVZWh1TWhrNG82OWRmeHBaZzg2dEREcGFOc01mVE4tR2ZPUWtGc1dkRmM3dVlJTjNXaHpENFhzUXEzN29SOGdv?oc=5>

### Cisco Systems, Inc. (CSCO) Stock Forecasts
- Summary: Analysts predict future stock performance for Cisco.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxNd2dxNjJnclhCR195N3JKQnlXd3hFdmZ2bExObjRLSGRlRWEtRkNJVHpLNTFxQXBDMzJGU2J3amVRN2NVWWl5VUtiZnlDd1Q3eEpGbTF2NlczZXlvMTJ0ZllmU0VpNEU1em82a3NmOENJREFpd1c3UlVwYS1pSHhONkFBNVFOWDFZUm4tVA?oc=5>

### Cisco’s Growth May Have Peaked Despite Raised AI Revenue Outlook, Says Citi — Barclays Sees Margins Holding Up
- Summary: Citi raises AI revenue outlook, noting margins remain stable, suggesting potential growth plateau.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQU296WWh2dWhYa0dscGY4S1J1NXctalp4YmhOQWFpOS1id1dORzEyM3B2czB2SjVGWjlQTzIxN2hOMHJTYzFZUFNOR29ZRjY0OVRLalZTdDVQUjhkOTJ3c0JGaVFoc2E1aFFLN3JfTEtzc2JBQUFhZkw3b3l2WEdGQXpEdk0xOWdESEx6aXdrNFkxM2o1OGZmUGZuWDk?oc=5>

### Cisco (CSCO) Stock Can Q1 Results Sustain The AI Rebound?
- Summary: Potential Q1 earnings could support AI-driven growth.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxQNzl3YVozazZGRThYdDlEWklreDVRS2hzUnNDcXFDZUpjNUxjbm1adFNaTWtRSWRVYkUtSzFxZ1U0RVFCNnJpZnZQYzhubUZYYnRSNjZYWEVsZjZncm5kQ0xpSDVwWFdoaDNiWl9XUmQ1RTQ4LTJ5bkJFLWRMeUpremluV3Q0TUVVdkhwMkVXd1AyWGRPQVBySHYwTVFyeGxPN01mSTVQSW5FUHlReDFSTllQTFFXTnRXTXhWaFExMNIBxAFBVV95cUxPQWVFV253MkNwaVBQdU96ZVoyTW4zN0NDNUNvWjBjMnJCZTZ4czE4bEc4MWZzbDlNZl9saFNkZllxMXZYUVdNTmpxanFWUzNGeldqNFFmUjEwQXptQlZ0dGQtaHhFRko1ckZmYTF5Q3B1WTNWR3ljU1J5QzBZTGV6ZHZDeURHTGliMDVNbjJqT2gtNnVkeENDVGRMYWcwQTR0NHM2UXM1Ql83TndpVlZmeXFjTGVEd2NYMnQ1V2dDWnFrOXBZ?oc=5>

### Cisco: I Downgraded It At The Top, Look At It Now (Rating Upgrade) (NASDAQ:CSCO)
- Summary: Analyst upgrade may boost investor sentiment.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQVFpybG9LeWxHcFNRZlh3Ni1VcnlwOENLTzRiQlpWSllOR1A5YUJDSEFMNHFjbktyRFhoUGx4dHZXbUxfSEQzbEU2SlJjTlYzMDE2NEJiTDNHMl90VlMwdHdnWS1LYVBicGxvM1RrWEtZaTd5TWthYzZtQzNzakFTeEpBQ2duNHVockpJSmxYN0JSZ3RGMmVuMjd4QS1PX0dPZkVpVFVB?oc=5>

## RISKS

### Cisco Systems (CSCO) Tied To FAA Ground Stop After Router Failures Hit Flights
- Summary: Router failures linked to FAA ground stop raise operational risk for Cisco.
- Date: 2026-11-16 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNOUtrNHlJcnBPQU5yVmpMeENvZG14bThqM2UzRmFsWEd2VUpEa21JWEduak84czByeUJpNkFaNWxrbEtnQlI0SDlyTEVpZUxELV9vdTdBYkt0VmhaNFcxX0xLRTRMSkxkWllwZ0lRaU9hV0VhcUZIR2FJNjAtT2ItQ1RPRGFPTnJSb09nQUZyN1JZdw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CSCO** | **25.87** | **7.22** | **18.79** | **24.40** | **373,349,810,176.00 USD** | **23.04** |
| ANET | 50.83 | 14.56 | 42.45 | 58.50 | 239,528,443,904.00 USD | 57.10 |
| FFIV | 25.41 | 4.51 | 18.19 | 13.30 | 18,110,799,872.00 USD | 42.01 |
| HPE | 23.45 | 2.28 | 10.82 | 33.70 | 60,386,377,728.00 USD | 122.99 |

Peers fetched as_of: 2026-11-19; CSCO reuses existing data (market data as_of: 2026-11-19); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-12
- Next expected earnings: 2027-02-10 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-19

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-17
- Revenue (latest available single quarter): 12,844,000,000.00 USD; period 2018-04-29/2018-07-28; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 4,552,000,000.00 USD; period 2026-07-26/2026-10-24; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/858877/000085887726000185/csco-20261024.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiowFBVV95cUxPaG5CX1poZ0t3MEsyRjk0SGVNNmdEYWRjQkdYX3g2TU9RUHJ3bGs3SHp6UTZnVnQ5R2RodTlYY3lwRk82SXM1elhGaThlcEFGRTluOUkzQ1d2bDk0UzdQMGNPSGg2NERYNGZ1ZldzWjQyOWppQVFUeG9RM0xPeUQxemxybmV0NWpXcW9GdTUxd2hpaUJYc3JXTzFKM1FpWE5GZU5F?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPRVVEN2VyeUR1UFJzOXczaW1IQ1dfOTBzWEsyc2YycmZZUTR6YVgtUmw3Q2dZQ3pGNWZhU294VWd1ZnYzV0Mtc180ancyUENfVHhnM1QwZ1BJRkNEZUVkZjhENm9CbGFpY0hhcHRwOWhoYmIzMmpfZzZ5YUpEQjF4REYyNzlBbkxfdzNUV3dUdHFXbm8wRVRtUVJB?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNaEZDb3R6LWM1R0FOem9SZXYtSWMyT3VwbTEyWFRBVnNLTzlPWGJhQWtLdGcyU3NfYkNTdWxnc0QxMFBBYzhjS21mN1JiRVlXeUd5WDExOHo3VmtNWnhval9SUnB2djdmenh4TzRqRG1KVW1aeG5kUGNFUU1IdVR6OHN2bXdhb3lxVXUzc1VMQzM2Q29WYmc?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxOTnlNUDNGWjAyU05oM1Bpem94c0hLd19USzZxSElzQlhIN2x3X21XTGlUS3IwV0FLYkJmYl9sQ05yanlTZWtpRS1faUdZeUFzaFdQemhBczRMdVBMQmRYS2NtVUZJSURneDJOcDZoQlQ0UHJpTm5VVnVJSjBTVDFILTFBWUxoMUpvSXFTcm1mTG9DMi1TN0Y4b09aejQ2T2dvLXJRekpIR2ZkV3hrTUE?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxObk1wZmhoMzladm0wOVlmakNfWXdhTWN1ZHZ2WmFfVzN0OTVBWVpvMW1vY290c1hyalBfMS1vcGVzWXNidFFlUGtZSjJ6UXpnQ1JyNktMVEg3RklqdnYzZ1o3cEpETlRpUXRNNUdoUmJfY21QQXczRGpWU280c3FTRUZqR1U0elNSSGRvWHBpb3M?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPdDNIY29LZWFpZ1lHNHBiTmdBVHN1NmkxM05pWTVOdEZuSTNGeFJVaFVwLS1FZE9PU1k5QWEtRm95UjMtUlpKTmU0VkRpMDBUbVptQ0RDRmJGR0x6c1J5amNCZnpkbURheE9lUDNGTVU0OW5UeWtwREdpVVR6eDgxTmJERS12Y2xGdFU2OXhPQXNLMHY0M1FpRVBn?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxOMnlUbGVDUnBVbDMwa3QzUTJwbE11YlF3OUpLNkNRTzlXaFNRVUlNN1hpNVk4Y0J4a3dENjl2OHJfdmk0djBjSjhCdGo3Q0JSLWMyTW5wWjNHdW5QekoyWkhlZ0xjSDEtVU8yZjM4Z0RIMnhORThzTnV1ZmhadGlpREJLS2xZbGlo?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxOMXNHdFp6SjlGRFIxaTJyemhVZWxfRDJWSF8ydmlWbm1VOS0xVTZMVFMyOUpaTHZSZy1SVEEyTUxYY2hBdFRlWGpJRG9NcDJlMThOcW9JZHM0N3hzazVvV1hRVXhOZ2pCX3ljY29sejh0R0RUeUo4cmpwdFdMNi04di1XTzdEbEFNdG5qb2ZnVW1iV1R6MEZWYkN5SVQzckFUTzN6SWpLeXVkMFVWR05hUQ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQcFAtMzM5Q0dnamlhSllqMzRyR0lzUTdVWnFEcWlvaVQwTGVDWFRIc3p1elBmRXk1alFFUDBxbkl0dnRET1hpSjAzdUpia2ZKSkQtY2JZN0VVYS1kN2ZHMjBNU0tiYWFJVnp6Ul9mRTBHUEw3QWotMkFkTjBLMGhHMHlfYzlNb09iWVJfVS1QY1Bia21wakVSRlpWMjVMSmFaV0R4Z095cllacldjODZhMA?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOd0psSW1iRElNXzlmeTI0QTZrM1J1UU5QaUJnS1J4NXFMYzhMM2dvb3dxeG5zSHRFTG5IRkhPTklXMy1vM01GaDBRSlRYNjQxM3E2aEZtYXlyTEdRR0x3STNMMUlyQ1A4aWNERVNQTW1RazVaZUc2WFJ2UjY1eVVUanA2U3ZGMXZITlRJOVRNeF9QTzhJaHc?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPZkpSempEOHAyWU5QVVlKUGw2Zl81RHBKRnBGT3ljMmQ5Q21VazV1azg0ZzdUek5zZHQ0MVZfRkJGVWNzQXpHUkk5dVVZMENON3JuYWJsQ3RDVlVqNS1FeGp1dUprLUFWSnUxd0xDdFg2dUJmZ2tXVU9HS2RyaHJKeEVVTmZULUpoUVlDZzVjNHVNMGVfNTRiOC11OG5sbkhEVzhZODRlMlg?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxOQW1JNjZlRklwSUJiX3pwLW13UG5WZF9NbTc3Mlk4dmhTeUNReWlfLWloUFNrbG5GY3ZfczdIZ0tHbUI0VGZ4dGFub252Z3dfMTdGX0ZDQi1LRVVxYW1wdkhlLXRhbzAyMXhsMHVUcXExRWlHbW52N2EyRlQ0OThlOWhB?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOR2gxQW9fU2tUZlVfZ3k0RGw2UF9KWjAwVGVFUFU4c2R1VE5PWERjTkMtNnF6OUNQNjYtQzhsN1RrUFU0OHU1MjJaeS0wYUdIdlY1TmVpajRVZWh1TWhrNG82OWRmeHBaZzg2dEREcGFOc01mVE4tR2ZPUWtGc1dkRmM3dVlJTjNXaHpENFhzUXEzN29SOGdv?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNd2dxNjJnclhCR195N3JKQnlXd3hFdmZ2bExObjRLSGRlRWEtRkNJVHpLNTFxQXBDMzJGU2J3amVRN2NVWWl5VUtiZnlDd1Q3eEpGbTF2NlczZXlvMTJ0ZllmU0VpNEU1em82a3NmOENJREFpd1c3UlVwYS1pSHhONkFBNVFOWDFZUm4tVA?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNT0twUWhpNkRoVG5zMDB1VzBZV1dpcVA3Q212eXNOTC1MdjhUR1hJT2FUZFhLdnIxZ2ppY3E1TE1rblpROFRyMXhUTmh4WFNCM2dNQ3BxUTg1eDVvTEpMcV9fd1ZSemlxS1RJV1B1VGotLXhYSHlISk52V2ZRcUpMa09udXBkQmdBb0pNRmVROFA?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQU296WWh2dWhYa0dscGY4S1J1NXctalp4YmhOQWFpOS1id1dORzEyM3B2czB2SjVGWjlQTzIxN2hOMHJTYzFZUFNOR29ZRjY0OVRLalZTdDVQUjhkOTJ3c0JGaVFoc2E1aFFLN3JfTEtzc2JBQUFhZkw3b3l2WEdGQXpEdk0xOWdESEx6aXdrNFkxM2o1OGZmUGZuWDk?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxQNzl3YVozazZGRThYdDlEWklreDVRS2hzUnNDcXFDZUpjNUxjbm1adFNaTWtRSWRVYkUtSzFxZ1U0RVFCNnJpZnZQYzhubUZYYnRSNjZYWEVsZjZncm5kQ0xpSDVwWFdoaDNiWl9XUmQ1RTQ4LTJ5bkJFLWRMeUpremluV3Q0TUVVdkhwMkVXd1AyWGRPQVBySHYwTVFyeGxPN01mSTVQSW5FUHlReDFSTllQTFFXTnRXTXhWaFExMNIBxAFBVV95cUxPQWVFV253MkNwaVBQdU96ZVoyTW4zN0NDNUNvWjBjMnJCZTZ4czE4bEc4MWZzbDlNZl9saFNkZllxMXZYUVdNTmpxanFWUzNGeldqNFFmUjEwQXptQlZ0dGQtaHhFRko1ckZmYTF5Q3B1WTNWR3ljU1J5QzBZTGV6ZHZDeURHTGliMDVNbjJqT2gtNnVkeENDVGRMYWcwQTR0NHM2UXM1Ql83TndpVlZmeXFjTGVEd2NYMnQ1V2dDWnFrOXBZ?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQVFpybG9LeWxHcFNRZlh3Ni1VcnlwOENLTzRiQlpWSllOR1A5YUJDSEFMNHFjbktyRFhoUGx4dHZXbUxfSEQzbEU2SlJjTlYzMDE2NEJiTDNHMl90VlMwdHdnWS1LYVBicGxvM1RrWEtZaTd5TWthYzZtQzNzakFTeEpBQ2duNHVockpJSmxYN0JSZ3RGMmVuMjd4QS1PX0dPZkVpVFVB?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNOUtrNHlJcnBPQU5yVmpMeENvZG14bThqM2UzRmFsWEd2VUpEa21JWEduak84czByeUJpNkFaNWxrbEtnQlI0SDlyTEVpZUxELV9vdTdBYkt0VmhaNFcxX0xLRTRMSkxkWllwZ0lRaU9hV0VhcUZIR2FJNjAtT2ItQ1RPRGFPTnJSb09nQUZyN1JZdw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
