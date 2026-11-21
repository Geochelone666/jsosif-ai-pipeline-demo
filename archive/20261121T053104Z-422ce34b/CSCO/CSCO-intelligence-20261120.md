# CSCO Intelligence Report

- ticker: **CSCO**
- Report as_of: **2026-11-20**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/CSCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CSCO/key-statistics/
- AI analysis snapshot as_of: **2026-11-20**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-21T05:48:03.044017+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 3, 'ai': 17, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261120T053808Z-e360129e/CSCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 9 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 30.43%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 90.6400 |
| Return 1D (%) | -4.2872 |
| Return 1W (%) | -5.2279 |
| Return 1M (%) | -15.0595 |
| Return YTD (%) | 19.8469 |
| Return 1Y (%) | 22.3728 |
| Annualized volatility (%) | 37.2757 |
| Beta vs SPY | 1.2734 |
| Max drawdown (%) | -29.7448 |
| Sharpe (rf=0) | 0.7307 |
| Downside deviation (rf=0, %) | 26.4105 |
| Sortino (rf=0) | 1.0312 |
| Historical VaR 95% (1D, %) | 3.2126 |
| Historical ES 95% (1D, %) | 5.6237 |
| Correlation vs SPY | 0.4883 |
| Tracking error vs SPY (%) | 32.7627 |
| P/E (trailing) | 24.11 |
| P/B | 6.91 |
| EV/EBITDA | 18.02 |
| Revenue growth (%) | 24.40 |
| Forward P/E (estimate) | 14.96 |
| Gross margin (%) | 64.07 |
| Operating margin (%) | 27.17 |
| Return on equity (%) | 30.38 |
| Free cash flow yield (%) | 2.91 |
| MA50 | 106.1349 |
| Close vs MA50 (%) | -14.5993 |
| MA200 | 102.1004 |
| Close vs MA200 (%) | -11.2246 |
| RSI (14, Wilder) | 33.4419 |
| MACD (12,26) | -3.8681 |
| MACD signal (9) | -3.3202 |
| MACD histogram | -0.5479 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CSCO': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 90.6400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -4.2872 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -5.2279 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -15.0595 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 19.8469 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 22.3728 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 37.2757 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.4105 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.0312 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.2126 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.6237 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4883 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.7627 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.2734 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -29.7448 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7307 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 14.9649 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 64.0740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 27.1720 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 30.3800 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.9132 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 24.1064 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 33.4419 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.5479 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -14.5993 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -11.2246 -> Clearly below the moving-average trend level.

## TAILWINDS

### Cisco upgraded to Buy at HSBC as firm sees 'attractive valuation' (CSCO:NASDAQ)
- Summary: Cisco upgraded to Buy at HSBC as firm sees 'attractive valuation' (CSCO:NASDAQ)
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPaG5CX1poZ0t3MEsyRjk0SGVNNmdEYWRjQkdYX3g2TU9RUHJ3bGs3SHp6UTZnVnQ5R2RodTlYY3lwRk82SXM1elhGaThlcEFGRTluOUkzQ1d2bDk0UzdQMGNPSGg2NERYNGZ1ZldzWjQyOWppQVFUeG9RM0xPeUQxemxybmV0NWpXcW9GdTUxd2hpaUJYc3JXTzFKM1FpWE5GZU5F?oc=5>

### Cisco posts its best growth in 15 years. Why isn't Wall Street buying?
- Summary: Cisco records 15‑year high growth, yet market underreacts.
- Date: 2026-11-16 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNaEZDb3R6LWM1R0FOem9SZXYtSWMyT3VwbTEyWFRBVnNLTzlPWGJhQWtLdGcyU3NfYkNTdWxnc0QxMFBBYzhjS21mN1JiRVlXeUd5WDExOHo3VmtNWnhval9SUnB2djdmenh4TzRqRG1KVW1aeG5kUGNFUU1IdVR6OHN2bXdhb3lxVXUzc1VMQzM2Q29WYmc?oc=5>

### Cisco: Its $22 Billion AI Supply Bet Looks Worth Taking
- Summary: Cisco invests $22B in AI supply chain, signaling strategic expansion.
- Date: 2026-11-19 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPRVVEN2VyeUR1UFJzOXczaW1IQ1dfOTBzWEsyc2YycmZZUTR6YVgtUmw3Q2dZQ3pGNWZhU294VWd1ZnYzV0Mtc180ancyUENfVHhnM1QwZ1BJRkNEZUVkZjhENm9CbGFpY0hhcHRwOWhoYmIzMmpfZzZ5YUpEQjF4REYyNzlBbkxfdzNUV3dUdHFXbm8wRVRtUVJB?oc=5>

### Cisco Had A Very Good Quarter And A Quick Look At Nvidia’s Estimates Before Reporting
- Summary: Cisco reports strong quarter, referencing Nvidia estimates.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxOTnlNUDNGWjAyU05oM1Bpem94c0hLd19USzZxSElzQlhIN2x3X21XTGlUS3IwV0FLYkJmYl9sQ05yanlTZWtpRS1faUdZeUFzaFdQemhBczRMdVBMQmRYS2NtVUZJSURneDJOcDZoQlQ0UHJpTm5VVnVJSjBTVDFILTFBWUxoMUpvSXFTcm1mTG9DMi1TN0Y4b09aejQ2T2dvLXJRekpIR2ZkV3hrTUE?oc=5>

### Cisco Systems, Inc. (CSCO) Stock Forecasts
- Summary: Cisco releases future performance projections for investors.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxNd2dxNjJnclhCR195N3JKQnlXd3hFdmZ2bExObjRLSGRlRWEtRkNJVHpLNTFxQXBDMzJGU2J3amVRN2NVWWl5VUtiZnlDd1Q3eEpGbTF2NlczZXlvMTJ0ZllmU0VpNEU1em82a3NmOENJREFpd1c3UlVwYS1pSHhONkFBNVFOWDFZUm4tVA?oc=5>

## HEADWINDS

### Cisco Systems, Inc. (CSCO) Posted Record $17.3 Billion Revenue, but Margins Slipped: Is the Stock Still Worth Buying?
- Summary: Cisco Systems, Inc. (CSCO) Posted Record $17.3 Billion Revenue, but Margins Slipped: Is the Stock Still Worth Buying?
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQazVldGNaeWhMdGxVX3lmZlJjRHh5OE91TFUzUGhzYXJjUDB6aXh4Y0hITjZMREZPTmZ0UmYwRGxzY0VoSlRVWlF2UmVCeHZ2NWlIbEtja3V3RHhNNmtoYlBTcjNQQ3pXQm5zNXdUYnZuY2hGeXNPbHVCUDBDSDEzQTdhbXBSWDRyeHZ6dzl4QlQwNEVES0lQVlZB?oc=5>

### Cisco insider share sales: Can CSCO avoid deeper losses?
- Summary: Insider share sales may signal declining confidence, potentially impacting stock negatively.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQWUdpdXY2TlhoRDBwTWNzZU9Nb3plYWFHZ1JXSEdhejlUOHVMd0ZVQklBc1p0dHRjT0lpYWdUMWZmc0QwSS1XNFN2eU1ibnpFM2ZTNzhkeS1JbmpiN3dPcTZ6c0x6emtYVlFqNXRHRWZkMGw5ZEJGb0puN1k2RlJySEZmcXlWTExHR1Q4NjNTaw?oc=5>

### Cisco Systems Inc Stock (CSCO) Moved Down by 3.10% on Nov 20: A Full Analysis
- Summary: Stock fell 3.10%, indicating a short-term negative market reaction.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPbVRIOElDNVBrZkR1MHZrcDNvVXIyT0lObnNwcTVQR3Z1dHA3VHFGdVNvLUpGN21pZTJUVDFMMzZiNnJZME9NbTRsU0lBZTdUSHVsYVFOSGZuMFNaWldXenU1cFhRVDUwTjhTYlpzd2hGOHU3STRxUS1wR09jS0wwdkRyYUdqTnlOZllV?oc=5>

### At Cisco Systems (CSCO), 3,288 of the CFO’s shares were withheld for taxes tied to early vesting.
- Summary: CFO shares withheld for taxes, limiting liquidity.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxOdVl0YkpvYzJTT0JlWDJ0QUZjTDVQV1Qta21qeVJ2NDlRam01Vkh3VW1tVlFCU0tPR1hQeGRNMjl3ZWdVaGxqZjZVdjdENVcteWxvODctYzFwQTRpa3lzTEpjSzkzbVYzRTBqRXlmUXcxa0NNWHdjeENocmVqbmdSVHBabG1hWTJEUXJIOTJwVndKbU9vUHE5eWd1R09lWGdId3lDZVVMRTJueno4LUxleQ?oc=5>

### Cisco (CSCO) CEO Charles Robbins had 5,201.545 shares withheld for taxes as he became eligible to retire.
- Summary: CEO Charles Robbins' shares withheld for taxes upon retirement eligibility.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQb1dBek9CSUlKaWxnZTN6eUFSejl4UWFySE9wMlR6TDhERnZ5M2dBQzdwNzhZbXU4Q0ZzVWt5LWtfb1QyWllsaG5CQW1KdGM3Uk8xbl9iWkduTWdTR0RKNDk4YmdCSWpTQmZkeGtoMjdpeW0tb2N6ZGNXRWw4T1E0amlLb1p0MUpZN3RXNjJ1V19PUV9jT1lLNEJZR21KYkFuYTE1d2ViNUtZVGhEMFFZcg?oc=5>

### In five trades on Nov. 19, Cisco Systems (CSCO) operations EVP Thimaya K. Subaiya sold 21,186 shares.
- Summary: EVP Thimaya Subaiya sold 21,186 shares in five trades.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxObWhjZW9kbC1GalZrcmFyUnZnTTdjd3A5bV9lQlF1NGI3RVFpM3FENlEyNjJROE5GRDNYZVEwWktkcXhONXVIMnppeXMtTDVmaWlicS1kQ2h6d1FvTUotN2k5WUV4ZURhcEU0RGhFTmxFbzJHY0FYS21GYl9PRWJ5YVVoX1ZhaHZmLXI1Z2NYS0tqakcwcndwZ0t0T2dzZFRKNlNYQnB2Y2w4dUNabmdQQw?oc=5>

### Cisco Systems (NASDAQ:CSCO) Stock: Insider Thimaya Subaiya Sells 21,186 Shares
- Summary: Insider Thimaya Subaiya sold 21,186 shares.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxPem43azhEckx0OUlLMzdXRGxZbFNHd0NrRjJyY2ZCaTdoYndXRnNHRzdfb2ZPWldnbEtuTHdrSVVZLTNNWE9yc1o1ck16cFljVzMxamV2ZzVncDlvR05NaWx0UnpOWFdjRThzZ1BEVk1GQjFmYl9USlREVDk5T08tWFlEdjBwSlBxMWh0Y0p1T0RzMlNBTTVieHNCQ2RmM1p3blFjeEhDUDdHSU5jUkVDdUVhcVRqSW4ycE5uQ2VXN3RqVUVHQVl1SW1lbUpxak1IR0E?oc=5>

## CATALYSTS

### Cisco (CSCO) Stock Gets Fair Value Trim As Analysts Cut Targets After Strong Q1
- Summary: Cisco (CSCO) Stock Gets Fair Value Trim As Analysts Cut Targets After Strong Q1
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOd0psSW1iRElNXzlmeTI0QTZrM1J1UU5QaUJnS1J4NXFMYzhMM2dvb3dxeG5zSHRFTG5IRkhPTklXMy1vM01GaDBRSlRYNjQxM3E2aEZtYXlyTEdRR0x3STNMMUlyQ1A4aWNERVNQTW1RazVaZUc2WFJ2UjY1eVVUanA2U3ZGMXZITlRJOVRNeF9QTzhJaHc?oc=5>

### Cisco: Better Earnings, Cheaper Stock (NASDAQ:CSCO)
- Summary: Cisco reports improved earnings and a lower stock price, indicating stronger financial performance and potential upside for investors.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxOQW1JNjZlRklwSUJiX3pwLW13UG5WZF9NbTc3Mlk4dmhTeUNReWlfLWloUFNrbG5GY3ZfczdIZ0tHbUI0VGZ4dGFub252Z3dfMTdGX0ZDQi1LRVVxYW1wdkhlLXRhbzAyMXhsMHVUcXExRWlHbW52N2EyRlQ0OThlOWhB?oc=5>

### What Did Cisco’s Quarter Change For Its Stock?
- Summary: Cisco’s latest quarterly results and their impact on the stock price.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPZkpSempEOHAyWU5QVVlKUGw2Zl81RHBKRnBGT3ljMmQ5Q21VazV1azg0ZzdUek5zZHQ0MVZfRkJGVWNzQXpHUkk5dVVZMENON3JuYWJsQ3RDVlVqNS1FeGp1dUprLUFWSnUxd0xDdFg2dUJmZ2tXVU9HS2RyaHJKeEVVTmZULUpoUVlDZzVjNHVNMGVfNTRiOC11OG5sbkhEVzhZODRlMlg?oc=5>

### Cisco Drops 7% Post Earnings: Should You Buy the Stock on the Dip?
- Summary: Cisco’s earnings miss caused a 7% drop, prompting investors to consider buying at the dip.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOR2gxQW9fU2tUZlVfZ3k0RGw2UF9KWjAwVGVFUFU4c2R1VE5PWERjTkMtNnF6OUNQNjYtQzhsN1RrUFU0OHU1MjJaeS0wYUdIdlY1TmVpajRVZWh1TWhrNG82OWRmeHBaZzg2dEREcGFOc01mVE4tR2ZPUWtGc1dkRmM3dVlJTjNXaHpENFhzUXEzN29SOGdv?oc=5>

### Cisco (CSCO) Stock Can Q1 Results Sustain The AI Rebound?
- Summary: Potential Q1 earnings could support AI-driven growth.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxQNzl3YVozazZGRThYdDlEWklreDVRS2hzUnNDcXFDZUpjNUxjbm1adFNaTWtRSWRVYkUtSzFxZ1U0RVFCNnJpZnZQYzhubUZYYnRSNjZYWEVsZjZncm5kQ0xpSDVwWFdoaDNiWl9XUmQ1RTQ4LTJ5bkJFLWRMeUpremluV3Q0TUVVdkhwMkVXd1AyWGRPQVBySHYwTVFyeGxPN01mSTVQSW5FUHlReDFSTllQTFFXTnRXTXhWaFExMNIBxAFBVV95cUxPQWVFV253MkNwaVBQdU96ZVoyTW4zN0NDNUNvWjBjMnJCZTZ4czE4bEc4MWZzbDlNZl9saFNkZllxMXZYUVdNTmpxanFWUzNGeldqNFFmUjEwQXptQlZ0dGQtaHhFRko1ckZmYTF5Q3B1WTNWR3ljU1J5QzBZTGV6ZHZDeURHTGliMDVNbjJqT2gtNnVkeENDVGRMYWcwQTR0NHM2UXM1Ql83TndpVlZmeXFjTGVEd2NYMnQ1V2dDWnFrOXBZ?oc=5>

### How Investors May Respond To Cisco Stock After Earnings Beat
- Summary: Earnings beat may boost investor sentiment and drive stock upward.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOMHZiWHc0TlV6cUxOTTNTbDQzdkczcWFEZ2RELUhIaG1vbDhjcFJreXZleXRmc0Q3UHNqbm84SW9pZlIwdmY2Z0xLcUt5RXd2c2RQT3NCREI2RmdmRGthaUJhU3pTd09NZUg0RllpZ3hVNmFGZlRBbVAwZ2ltajRiQ1lYQmFwMmFBSHNqSDl1WmtXbmtmRWZtOUVFNkFiYXM?oc=5>

### Cisco Systems (NASDAQ:CSCO) Stock Rating Reaffirmed as "Buy" by Rosenblatt Securities
- Summary: Rosenblatt Securities reaffirmed a Buy rating on Cisco stock.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxPaVIwOFhuSWFhV01nd3BaN2VoS2U3eE5hTlk0WC1CVnBsY2FLSEhialBMU1g4TV8yOC1PZ0pnMVpna1VjWGhhbGdOTHVKZ0UwMlJENlNnTG52am4tMmszblNOczBwdlV5b0UzUTZOUnN2RElfZWdVRmtCVWJFNXRCYXppMWROWFFENjhhLXdoekRsMTlKYXBhZlFJWnBwRmx6NHBheTgwQTBzd1dORUluWG5HN0U3bFU1QmpSRW94Q2lYTG41T1dvTzlDMkxmY2hGTFBST0ttZldsQkk?oc=5>

## RISKS

### Cisco Systems (CSCO) Tied To FAA Ground Stop After Router Failures Hit Flights
- Summary: Router failures linked to FAA ground stop raise operational risk for Cisco.
- Date: 2026-11-16 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNOUtrNHlJcnBPQU5yVmpMeENvZG14bThqM2UzRmFsWEd2VUpEa21JWEduak84czByeUJpNkFaNWxrbEtnQlI0SDlyTEVpZUxELV9vdTdBYkt0VmhaNFcxX0xLRTRMSkxkWllwZ0lRaU9hV0VhcUZIR2FJNjAtT2ItQ1RPRGFPTnJSb09nQUZyN1JZdw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CSCO** | **24.11** | **6.91** | **18.02** | **24.40** | **357,343,494,144.00 USD** | **22.37** |
| ANET | 44.94 | 12.88 | 37.22 | 58.50 | 211,771,506,688.00 USD | 40.16 |
| FFIV | 24.28 | 4.31 | 17.32 | 13.30 | 17,308,000,256.00 USD | 34.61 |
| HPE | 21.09 | 2.05 | 9.94 | 33.70 | 54,306,586,624.00 USD | 108.03 |

Peers fetched as_of: 2026-11-20; CSCO reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-12
- Next expected earnings: 2027-02-10 (yfinance; expected dates may change)

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
- Filing date: 2026-11-17
- Revenue (latest available single quarter): 12,844,000,000.00 USD; period 2018-04-29/2018-07-28; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 4,552,000,000.00 USD; period 2026-07-26/2026-10-24; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/858877/000085887726000185/csco-20261024.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiowFBVV95cUxPaG5CX1poZ0t3MEsyRjk0SGVNNmdEYWRjQkdYX3g2TU9RUHJ3bGs3SHp6UTZnVnQ5R2RodTlYY3lwRk82SXM1elhGaThlcEFGRTluOUkzQ1d2bDk0UzdQMGNPSGg2NERYNGZ1ZldzWjQyOWppQVFUeG9RM0xPeUQxemxybmV0NWpXcW9GdTUxd2hpaUJYc3JXTzFKM1FpWE5GZU5F?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNaEZDb3R6LWM1R0FOem9SZXYtSWMyT3VwbTEyWFRBVnNLTzlPWGJhQWtLdGcyU3NfYkNTdWxnc0QxMFBBYzhjS21mN1JiRVlXeUd5WDExOHo3VmtNWnhval9SUnB2djdmenh4TzRqRG1KVW1aeG5kUGNFUU1IdVR6OHN2bXdhb3lxVXUzc1VMQzM2Q29WYmc?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPRVVEN2VyeUR1UFJzOXczaW1IQ1dfOTBzWEsyc2YycmZZUTR6YVgtUmw3Q2dZQ3pGNWZhU294VWd1ZnYzV0Mtc180ancyUENfVHhnM1QwZ1BJRkNEZUVkZjhENm9CbGFpY0hhcHRwOWhoYmIzMmpfZzZ5YUpEQjF4REYyNzlBbkxfdzNUV3dUdHFXbm8wRVRtUVJB?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxOTnlNUDNGWjAyU05oM1Bpem94c0hLd19USzZxSElzQlhIN2x3X21XTGlUS3IwV0FLYkJmYl9sQ05yanlTZWtpRS1faUdZeUFzaFdQemhBczRMdVBMQmRYS2NtVUZJSURneDJOcDZoQlQ0UHJpTm5VVnVJSjBTVDFILTFBWUxoMUpvSXFTcm1mTG9DMi1TN0Y4b09aejQ2T2dvLXJRekpIR2ZkV3hrTUE?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNd2dxNjJnclhCR195N3JKQnlXd3hFdmZ2bExObjRLSGRlRWEtRkNJVHpLNTFxQXBDMzJGU2J3amVRN2NVWWl5VUtiZnlDd1Q3eEpGbTF2NlczZXlvMTJ0ZllmU0VpNEU1em82a3NmOENJREFpd1c3UlVwYS1pSHhONkFBNVFOWDFZUm4tVA?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxOcE1nWVdZMkhlN3BZX3doYkhkSGNnd3k5RVI5el9hX3JJQkFTM1RtSnNFakoyNm1xVDJmQjlYTzh4WTNhaEZrY1Zpc012TGVzZTJXYk9DRThCVkFxYktEOTVNMEV4MHY3bmxiZ0JwN2tzVGpHSkFtQ0gxckNJaGs5cjliRlUyanI1?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQazVldGNaeWhMdGxVX3lmZlJjRHh5OE91TFUzUGhzYXJjUDB6aXh4Y0hITjZMREZPTmZ0UmYwRGxzY0VoSlRVWlF2UmVCeHZ2NWlIbEtja3V3RHhNNmtoYlBTcjNQQ3pXQm5zNXdUYnZuY2hGeXNPbHVCUDBDSDEzQTdhbXBSWDRyeHZ6dzl4QlQwNEVES0lQVlZB?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQWUdpdXY2TlhoRDBwTWNzZU9Nb3plYWFHZ1JXSEdhejlUOHVMd0ZVQklBc1p0dHRjT0lpYWdUMWZmc0QwSS1XNFN2eU1ibnpFM2ZTNzhkeS1JbmpiN3dPcTZ6c0x6emtYVlFqNXRHRWZkMGw5ZEJGb0puN1k2RlJySEZmcXlWTExHR1Q4NjNTaw?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPbVRIOElDNVBrZkR1MHZrcDNvVXIyT0lObnNwcTVQR3Z1dHA3VHFGdVNvLUpGN21pZTJUVDFMMzZiNnJZME9NbTRsU0lBZTdUSHVsYVFOSGZuMFNaWldXenU1cFhRVDUwTjhTYlpzd2hGOHU3STRxUS1wR09jS0wwdkRyYUdqTnlOZllV?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxOdVl0YkpvYzJTT0JlWDJ0QUZjTDVQV1Qta21qeVJ2NDlRam01Vkh3VW1tVlFCU0tPR1hQeGRNMjl3ZWdVaGxqZjZVdjdENVcteWxvODctYzFwQTRpa3lzTEpjSzkzbVYzRTBqRXlmUXcxa0NNWHdjeENocmVqbmdSVHBabG1hWTJEUXJIOTJwVndKbU9vUHE5eWd1R09lWGdId3lDZVVMRTJueno4LUxleQ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQb1dBek9CSUlKaWxnZTN6eUFSejl4UWFySE9wMlR6TDhERnZ5M2dBQzdwNzhZbXU4Q0ZzVWt5LWtfb1QyWllsaG5CQW1KdGM3Uk8xbl9iWkduTWdTR0RKNDk4YmdCSWpTQmZkeGtoMjdpeW0tb2N6ZGNXRWw4T1E0amlLb1p0MUpZN3RXNjJ1V19PUV9jT1lLNEJZR21KYkFuYTE1d2ViNUtZVGhEMFFZcg?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxObWhjZW9kbC1GalZrcmFyUnZnTTdjd3A5bV9lQlF1NGI3RVFpM3FENlEyNjJROE5GRDNYZVEwWktkcXhONXVIMnppeXMtTDVmaWlicS1kQ2h6d1FvTUotN2k5WUV4ZURhcEU0RGhFTmxFbzJHY0FYS21GYl9PRWJ5YVVoX1ZhaHZmLXI1Z2NYS0tqakcwcndwZ0t0T2dzZFRKNlNYQnB2Y2w4dUNabmdQQw?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxPem43azhEckx0OUlLMzdXRGxZbFNHd0NrRjJyY2ZCaTdoYndXRnNHRzdfb2ZPWldnbEtuTHdrSVVZLTNNWE9yc1o1ck16cFljVzMxamV2ZzVncDlvR05NaWx0UnpOWFdjRThzZ1BEVk1GQjFmYl9USlREVDk5T08tWFlEdjBwSlBxMWh0Y0p1T0RzMlNBTTVieHNCQ2RmM1p3blFjeEhDUDdHSU5jUkVDdUVhcVRqSW4ycE5uQ2VXN3RqVUVHQVl1SW1lbUpxak1IR0E?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOd0psSW1iRElNXzlmeTI0QTZrM1J1UU5QaUJnS1J4NXFMYzhMM2dvb3dxeG5zSHRFTG5IRkhPTklXMy1vM01GaDBRSlRYNjQxM3E2aEZtYXlyTEdRR0x3STNMMUlyQ1A4aWNERVNQTW1RazVaZUc2WFJ2UjY1eVVUanA2U3ZGMXZITlRJOVRNeF9QTzhJaHc?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxOQW1JNjZlRklwSUJiX3pwLW13UG5WZF9NbTc3Mlk4dmhTeUNReWlfLWloUFNrbG5GY3ZfczdIZ0tHbUI0VGZ4dGFub252Z3dfMTdGX0ZDQi1LRVVxYW1wdkhlLXRhbzAyMXhsMHVUcXExRWlHbW52N2EyRlQ0OThlOWhB?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPZkpSempEOHAyWU5QVVlKUGw2Zl81RHBKRnBGT3ljMmQ5Q21VazV1azg0ZzdUek5zZHQ0MVZfRkJGVWNzQXpHUkk5dVVZMENON3JuYWJsQ3RDVlVqNS1FeGp1dUprLUFWSnUxd0xDdFg2dUJmZ2tXVU9HS2RyaHJKeEVVTmZULUpoUVlDZzVjNHVNMGVfNTRiOC11OG5sbkhEVzhZODRlMlg?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOR2gxQW9fU2tUZlVfZ3k0RGw2UF9KWjAwVGVFUFU4c2R1VE5PWERjTkMtNnF6OUNQNjYtQzhsN1RrUFU0OHU1MjJaeS0wYUdIdlY1TmVpajRVZWh1TWhrNG82OWRmeHBaZzg2dEREcGFOc01mVE4tR2ZPUWtGc1dkRmM3dVlJTjNXaHpENFhzUXEzN29SOGdv?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxQNzl3YVozazZGRThYdDlEWklreDVRS2hzUnNDcXFDZUpjNUxjbm1adFNaTWtRSWRVYkUtSzFxZ1U0RVFCNnJpZnZQYzhubUZYYnRSNjZYWEVsZjZncm5kQ0xpSDVwWFdoaDNiWl9XUmQ1RTQ4LTJ5bkJFLWRMeUpremluV3Q0TUVVdkhwMkVXd1AyWGRPQVBySHYwTVFyeGxPN01mSTVQSW5FUHlReDFSTllQTFFXTnRXTXhWaFExMNIBxAFBVV95cUxPQWVFV253MkNwaVBQdU96ZVoyTW4zN0NDNUNvWjBjMnJCZTZ4czE4bEc4MWZzbDlNZl9saFNkZllxMXZYUVdNTmpxanFWUzNGeldqNFFmUjEwQXptQlZ0dGQtaHhFRko1ckZmYTF5Q3B1WTNWR3ljU1J5QzBZTGV6ZHZDeURHTGliMDVNbjJqT2gtNnVkeENDVGRMYWcwQTR0NHM2UXM1Ql83TndpVlZmeXFjTGVEd2NYMnQ1V2dDWnFrOXBZ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOMHZiWHc0TlV6cUxOTTNTbDQzdkczcWFEZ2RELUhIaG1vbDhjcFJreXZleXRmc0Q3UHNqbm84SW9pZlIwdmY2Z0xLcUt5RXd2c2RQT3NCREI2RmdmRGthaUJhU3pTd09NZUg0RllpZ3hVNmFGZlRBbVAwZ2ltajRiQ1lYQmFwMmFBSHNqSDl1WmtXbmtmRWZtOUVFNkFiYXM?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxPaVIwOFhuSWFhV01nd3BaN2VoS2U3eE5hTlk0WC1CVnBsY2FLSEhialBMU1g4TV8yOC1PZ0pnMVpna1VjWGhhbGdOTHVKZ0UwMlJENlNnTG52am4tMmszblNOczBwdlV5b0UzUTZOUnN2RElfZWdVRmtCVWJFNXRCYXppMWROWFFENjhhLXdoekRsMTlKYXBhZlFJWnBwRmx6NHBheTgwQTBzd1dORUluWG5HN0U3bFU1QmpSRW94Q2lYTG41T1dvTzlDMkxmY2hGTFBST0ttZldsQkk?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNOUtrNHlJcnBPQU5yVmpMeENvZG14bThqM2UzRmFsWEd2VUpEa21JWEduak84czByeUJpNkFaNWxrbEtnQlI0SDlyTEVpZUxELV9vdTdBYkt0VmhaNFcxX0xLRTRMSkxkWllwZ0lRaU9hV0VhcUZIR2FJNjAtT2ItQ1RPRGFPTnJSb09nQUZyN1JZdw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
