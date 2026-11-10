# CAT Intelligence Report

- ticker: **CAT**
- Report as_of: **2026-11-09**
- Market data as_of: **2026-11-09**
- Quant sources: https://finance.yahoo.com/quote/CAT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CAT/key-statistics/
- AI analysis snapshot as_of: **2026-11-09**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-10T06:00:56.594065+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 2, 'ai': 13, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **12** exact headline/source/date matches; prior report **20261109T043242Z-c8e908de/CAT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'short_term_price_move_in_structural_risks': 2}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 13 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 24.0%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 598.8800 |
| Return 1D (%) | 7.2051 |
| Return 1W (%) | -2.4021 |
| Return 1M (%) | -25.0060 |
| Return YTD (%) | 5.4293 |
| Return 1Y (%) | 7.2585 |
| Annualized volatility (%) | 41.4134 |
| Beta vs SPY | 1.8269 |
| Max drawdown (%) | -47.7898 |
| Sharpe (rf=0) | 0.3439 |
| Downside deviation (rf=0, %) | 29.2900 |
| Sortino (rf=0) | 0.4862 |
| Historical VaR 95% (1D, %) | 4.2458 |
| Historical ES 95% (1D, %) | 5.7878 |
| Correlation vs SPY | 0.6040 |
| Tracking error vs SPY (%) | 34.8937 |
| P/E (trailing) | 23.50 |
| P/B | 12.76 |
| EV/EBITDA | 18.41 |
| Revenue growth (%) | 17.30 |
| Forward P/E (estimate) | 18.57 |
| Gross margin (%) | 29.54 |
| Operating margin (%) | 20.19 |
| Return on equity (%) | 56.14 |
| Free cash flow yield (%) | 1.45 |
| MA50 | 754.8499 |
| Close vs MA50 (%) | -20.6624 |
| MA200 | 805.2472 |
| Close vs MA200 (%) | -25.6278 |
| RSI (14, Wilder) | 32.8410 |
| MACD (12,26) | -55.1854 |
| MACD signal (9) | -45.9109 |
| MACD histogram | -9.2744 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CAT': 278, 'SPY': 278}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 598.8800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 7.2051 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.4021 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -25.0060 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 5.4293 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 7.2585 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.4134 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 29.2900 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4862 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.2458 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.7878 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6040 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 34.8937 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.8269 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -47.7898 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3439 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.5716 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 29.5420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 20.1910 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 56.1350 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.4499 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 23.5039 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 32.8410 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -9.2744 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -20.6624 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -25.6278 -> Clearly below the moving-average trend level.

## TAILWINDS

### Caterpillar (CAT) Stock Looks Undervalued On Future Cash Flow
- Summary: CAT appears undervalued based on projected future cash flow.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxPVGoxYXJOVFIyVTZxQ2FWenNtdDhKM2M4cl9LNkRFdVBOMXg4cVQ2ZU5xcjh2aTV5ZC1lNU9rVkR1ajI5OFdPd2hnSlpHOEQta0Q5Uno5YWd1enBlU09GMUNScWlEZ0tjQnpzQmVnU3JGUnB1a3dIcDF0QTRSYi1HQ01BWGpHVGFvTzZkbXhNWmYxTklmalJmWlpjYjlDQkhQbjN0WjgwMjR0TG02Q293X2tCQWVmOHl4aHdyYTU2Y1NYblB5V2ZlcDl0NE1qd9IB0wFBVV95cUxNblpMSmZtUm9HTUl5YzEyMjl4bW5DWU9kZUhKTVRxbkhaVkM4cmp6MHdTUWFXb1R2X2M0UlBEQ182WFhhOWI3YU5vM0tmWHNUb0ZQYnN3OV9FWWk1UGEyLTdzOEF1V2lNUmg1RjhOT3YyZk9JYl9vYXE4ZXB1VmdiSHVrVnAzbU5ka1BxajJKYm5zMXdrdE1PZl9Pby1HVkZaaVN2TW12aVBPc0dHejFyWEd4UVdBaW1vQ0NhYS1Kamk1TThhWGNHZ3cyVzdfbEVQQUlN?oc=5>

### Terex, Titan International, Caterpillar, AGCO, and AeroVironment shares skyrocket, what you need to know
- Summary: Shares of multiple companies, including Caterpillar, surged, indicating a positive market reaction.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxOZmJPQXRjdjY5V0tCbnhVeDlUSHIwaVFYeF9kREhkM1RSeGloN0NmZ3pRdlRYeXNKZFNhc0YwM1hQS2N1UjJYdWJubmQzSUxiaEgwTTkzeWxJQjN0TG1Ydm9GRGxyZmRXOHlUOWpQckFkVUdPeE4yakJ1d1ZnelNVUzhFbENoRW9EU2lIZnFxTWp4S0F3NzNwX2VYTUVhMldEUTRyU2pBZDQ3SG02dkQ3VU9rOFpiZi05c1B4SmhZdlpxUGNMSFJNWk92Ql9zeFVwUXhUc1E4cm9tZDU0MU5fVC1iZTZ5Nmt2OE9lbnI2WQ?oc=5>

## HEADWINDS

### Caterpillar (CAT) Falls After Steady Guidance As Fair Value Debate Grows
- Summary: Caterpillar (CAT) Falls After Steady Guidance As Fair Value Debate Grows
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxOZHZsV0Y5djZMZ3ZtRmZuZmdIcUwweVh5MUhUOVlFelYzRzhib19PNm9MR0tEc0xYVFNiTmdSYThZSThfT3lMYUs1ei1iMzBsa083NkUxX1c0UVRjVmFybTdRNUxUM0poMmpDV3VNT3hrdFRVd3lnQU9YaGRFV0JYcmZkV2dSX1RuTFE2NEVqcw?oc=5>

### CAT Shares Fall Despite Q3 Earnings Beat: How to Play the Stock?
- Summary: CAT shares dropped even after Q3 earnings beat expectations.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQVjJ2QU4yQ2dnWldyc0VTQV9tV0xKRF9LRThnd1NxNll1bUlCTjZsMm5jR3pKQTNYYWQxTzJaS2NiV01DS2dYTUtNSVBKMVNOQWNnWTdxYlRGRzI5U0Q4YkpPcElYT2pqS294SHVEay1fZi15OFVkUHZOMV9jbEI2YmJMZ1dWRGoyaVR6MUtxVDFDYXhtVkE?oc=5>

## CATALYSTS

### CAT Stock Gets Price Target Cuts – Analyst Flags ‘50% Premium’ To Peers
- Summary: CAT Stock Gets Price Target Cuts – Analyst Flags ‘50% Premium’ To Peers
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQX21nNFl0am9GM0VHNlZESnBDenRxVmI0UnNlRnVLVUw3VXJIT05nZ2FyWk5KZDhFTG4zbjlJUEtSejcxRUxSaHlfSllJWi1iUjUyM19lazQ4dlZhOE1Gb0JjMWx2SGVXWk9QTEhjQnpacjVMcHh3T1U4VTh1TS02NG5LREpndjk1UnF6cTRDbk5WRmVMQ2dB?oc=5>

### A Look at Caterpillar Inc (CAT) After 6.4% Decline -- GF Value $503.24 vs Price $553.64
- Summary: Market commentary on post‑decline valuation versus price.
- Date: 2026-11-05 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxOYnE5LVJmSmZVNUpwdHBvbFJ5NEdpTlFJeDJQeUNBME0yY2Q1c1g3Q0xTZjZ6Snh6akotMWZscEpsWXUzREJidFRKLXJYcW1uNmtIZjF1a1RjbmNMZEVxTVBpTzlGYlZXbkFHRmExY0FYWVQ5R3JiN0tLWEZQeFhEVUMwdkF1UG1SVUg2cXR6eTdES25pTWp3OWloYkFhdDAzNHNqdHVmZ3RIelhNN0JSS2NLa2pSQQ?oc=5>

### What Could Caterpillar (CAT) Gain From This Dealer Acquisition?
- Summary: Explores potential benefits of a dealer acquisition for Caterpillar, including market expansion and cost synergies.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOMjZvcW9FcFFlNFJTUXVNVEswUjUzNmZCYVlCVlNBUThjLUVXOFR5RHpMQm5jLWZmdF9BQnJmdU5DeWhaRkYzQTJxU3VCNEozaExWRGFQblJUTXJiNTU3ZEFNTHdncjRNQ3ZMMmtIckxkd0NmUGxOUlBFUDVpSW5RVlpqZHpiT2hpMTZMV09Rd2NyRC1YMlIzRUNEMkdxcFE?oc=5>

### Caterpillar Stocks Jump 6.61% as Anthropic Takes Over $3.4 Billion Generator Order
- Summary: Caterpillar’s stock surged after Anthropic secured a $3.4B generator contract, signaling a significant product win.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPeHNqTHAxVnZNSjZwbkNvYVRQSGpZTjFfUUhyOGRvVmswVl9Fb2NqaWtSQzc4bWFjb25fZzl3VmhyS0lhV2pHdkNYM3JTdHd4RVEyMkdRa0xPOUdBaFFEXzdDWFVnd1ZMSmtmUURSOTkzaEUtYTEtOVNGNGEzR2VfbG12ci1YeWlENXRDcmlialo5UUQwWW9RYg?oc=5>

### Caterpillar Inc Stock (CAT) Moved Up by 6.33% on Nov 9: Facts Behind the Movement
- Summary: CAT shares rose 6.33% on Nov 9, reflecting positive market sentiment and potential underlying catalysts.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPYWhHMi1yN2MyUnhlZmlPdFdLOTNjeURLWFlFWEc1THo3Y2JRUllZVWNIcG5PbVU2SVVIWXFQb3c5WHJxTnpPT2tmYVNxSzZXb3QyME91X2lmdXVUOHl0eW91UFA5WXBtN0dPSWlIbHVybkU2ZENISENkMTJ4WUJwaGtfMXMwbTVaRmc?oc=5>

### A Look at Caterpillar Inc (CAT) After 7.2% Gain -- GF Value $504
- Summary: CAT experienced a 7.2% gain, boosting its GF value to $504 and indicating strong investor confidence.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNTnRjQmJITUVpQkcyejM3NEppdUJyRldHaXJfOUZiZEd0RElCXzgyMGRYb0FQUzBnOFRaU0J2NEUwZUFXRW43Nkl0MElPOXBwQVVWN2hMMzg4SDRZaDNwVmxEWllHSDg4VmZmREc4ak9YRS0wQ0k1Z3JkSjlhckEwOG9mZ1ZHT0c3RVpvLUJseHg1em12eFVCRnE3M015UXNIWHIwVXV4WHAxV0l4RnVOVW1R?oc=5>

### Caterpillar stock support and resistance levels after 5.8% rebound
- Summary: Technical analysis shows CAT rebounded 5.8%, with key support and resistance levels identified for traders.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPdnFFSGFMckxMbjBEMXpXYS1FQVhzT293aE5ZbW5pX0lTYkZRaFdXMkRzS1NfSDFHUm12ZW03V29KSnlybkdCSU5wanYzdlZXV2psTjl0OWRQUU1zMExHcXpsZ2I3cWhVNU1OcTZwcks5X21fT0lWcUFIUEtjYzJaU25uekFJLUo4bGtrZ0ZxeDBaQkpWTEs0?oc=5>

### A dealer with 100+ years of customer ties is now owned by Caterpillar.
- Summary: Caterpillar acquired a long‑standing dealer, expanding its distribution network.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQdk5fYUZpMG1NbTN5cFBmZVV3YjJ4QXdBWDd4UTA0NGh3NEkwSGVVVjFwVlRZRVBNbnR0VGdGMXh6N05jeGVsR2hzbDRVc1pTWE1CSjR6TWJkTHFmZ3gxMGNzV09FSUszVzZpdTRadkxsdWlhVllJeVFrakRSd0xoQnVJOU9hV1BWUGxzWUk2Szk5REk?oc=5>

### What Is Caterpillar (CAT) Asking With Its Ultra Low Methane Engine Breakthrough?
- Summary: Caterpillar announces a breakthrough ultra‑low methane engine, potentially enhancing fuel efficiency and reducing emissions.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxPUWlrZHk4TEhaNmlmR1VzenhJdXpHZHJfT1JHeGpNSFdidk05Uzdqa20zYzJ5Y0ljUVlwWTBPTVJfSnktaU90dVZUemY4d01iVGVULURGQWxPNEwweWdWRkl0aGtWSVd2TWlCcG82UE1xNkpjdU5XcEJEVjFEck9HTmhiMThFTE1yRFJtbDNpakFPWmpfaG0zRDBtMkR5ZlMteUE5eS1jSk5DY2NJd1M2MEhIdXo2MGIzcGtscnp2allVdjFjMDloS0Z3aWzSAdIBQVVfeXFMT0JqTUNZbHJvQS1IbmRKdXBvSnRFenRfUTBZWlByX2twWjFSTzU1UWxmbzVhWFIwY0J5Vk1kQi1CYkk4Z1E0WXVEdEstMWxCX2VQNHNiUEx5YzRlYUhVQW94eGlyYURuY1VvMm1rVGR2V1pBNGs3d0NjQ0lnOUtkcFFoeDZZZHQzNGxjZ0FrTjBBU0dzbFlUSWxnLW95R1RLRzhtRmhLWXhRNGYxdi1WVGtKMUdYUEZwRW54Xzg2dWhtcUVHcTVmOFNIZjVTZktMWmxR?oc=5>

## RISKS

### Caterpillar Inc Stock (CAT) Moved Down by 5.03% on Nov 5: Drivers Behind the Movement
- Summary: CAT shares fell 5.03% on Nov 5 due to market selloff and valuation concerns.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQVE5MSkpSQ0tVbnVQMUlxdG5KWno4SDFhc1F6ZXhXcDlMODFxSDJIdzNDMktxeDFWWlVPQ2tOMF9UMkZnaFl3Zk9mZFEyUV93NE1CSFZvWVNPc2lRei1JNU5LSWFyM2FVVHlUWHRLZkM3UG5ZeFdISDBRSHlxOXRKbDBZdmhXc0pHNVE?oc=5>

### Caterpillar’s Sell-Off: Is the Market Missing Its AI Power Play?
- Summary: Shares of Caterpillar have been declining, raising concerns about missed AI opportunities and potential market undervaluation.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPeFFhVlZab1RURE5HZzBkSVMydlBCNmJzOURnaDhXVHYxN2RGa2t1Q0ZjWm0zR3lveHJMUVEwaExMYU5Ud1RlcTg1aXljZXZibjR5M2F4VHhsTjRBcnE2M1JyclZfYndvVHk3WmRSTU9adWxfcjJYa0Nkb0hGRktNVGVudlRBSzRWZElTT2FsQVZpOENEZzE1MTRXLUc3UmM?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CAT** | **23.50** | **12.76** | **18.41** | **17.30** | **274,044,010,496.00 USD** | **7.26** |
| DE | 38.43 | 6.66 | 28.38 | 4.90 | 186,386,661,376.00 USD | 49.46 |
| CNH | 61.05 | 2.06 | 37.29 | 2.00 | 20,616,593,408.00 USD | 33.99 |
| CMI | 19.46 | 4.79 | 12.66 | 13.50 | 63,942,721,536.00 USD | -0.01 |

Peers fetched as_of: 2026-11-09; CAT reuses existing data (market data as_of: 2026-11-09); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-09

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

- https://news.google.com/rss/articles/CBMizgFBVV95cUxPVGoxYXJOVFIyVTZxQ2FWenNtdDhKM2M4cl9LNkRFdVBOMXg4cVQ2ZU5xcjh2aTV5ZC1lNU9rVkR1ajI5OFdPd2hnSlpHOEQta0Q5Uno5YWd1enBlU09GMUNScWlEZ0tjQnpzQmVnU3JGUnB1a3dIcDF0QTRSYi1HQ01BWGpHVGFvTzZkbXhNWmYxTklmalJmWlpjYjlDQkhQbjN0WjgwMjR0TG02Q293X2tCQWVmOHl4aHdyYTU2Y1NYblB5V2ZlcDl0NE1qd9IB0wFBVV95cUxNblpMSmZtUm9HTUl5YzEyMjl4bW5DWU9kZUhKTVRxbkhaVkM4cmp6MHdTUWFXb1R2X2M0UlBEQ182WFhhOWI3YU5vM0tmWHNUb0ZQYnN3OV9FWWk1UGEyLTdzOEF1V2lNUmg1RjhOT3YyZk9JYl9vYXE4ZXB1VmdiSHVrVnAzbU5ka1BxajJKYm5zMXdrdE1PZl9Pby1HVkZaaVN2TW12aVBPc0dHejFyWEd4UVdBaW1vQ0NhYS1Kamk1TThhWGNHZ3cyVzdfbEVQQUlN?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxOZmJPQXRjdjY5V0tCbnhVeDlUSHIwaVFYeF9kREhkM1RSeGloN0NmZ3pRdlRYeXNKZFNhc0YwM1hQS2N1UjJYdWJubmQzSUxiaEgwTTkzeWxJQjN0TG1Ydm9GRGxyZmRXOHlUOWpQckFkVUdPeE4yakJ1d1ZnelNVUzhFbENoRW9EU2lIZnFxTWp4S0F3NzNwX2VYTUVhMldEUTRyU2pBZDQ3SG02dkQ3VU9rOFpiZi05c1B4SmhZdlpxUGNMSFJNWk92Ql9zeFVwUXhUc1E4cm9tZDU0MU5fVC1iZTZ5Nmt2OE9lbnI2WQ?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxOZHZsV0Y5djZMZ3ZtRmZuZmdIcUwweVh5MUhUOVlFelYzRzhib19PNm9MR0tEc0xYVFNiTmdSYThZSThfT3lMYUs1ei1iMzBsa083NkUxX1c0UVRjVmFybTdRNUxUM0poMmpDV3VNT3hrdFRVd3lnQU9YaGRFV0JYcmZkV2dSX1RuTFE2NEVqcw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQVjJ2QU4yQ2dnWldyc0VTQV9tV0xKRF9LRThnd1NxNll1bUlCTjZsMm5jR3pKQTNYYWQxTzJaS2NiV01DS2dYTUtNSVBKMVNOQWNnWTdxYlRGRzI5U0Q4YkpPcElYT2pqS294SHVEay1fZi15OFVkUHZOMV9jbEI2YmJMZ1dWRGoyaVR6MUtxVDFDYXhtVkE?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQX21nNFl0am9GM0VHNlZESnBDenRxVmI0UnNlRnVLVUw3VXJIT05nZ2FyWk5KZDhFTG4zbjlJUEtSejcxRUxSaHlfSllJWi1iUjUyM19lazQ4dlZhOE1Gb0JjMWx2SGVXWk9QTEhjQnpacjVMcHh3T1U4VTh1TS02NG5LREpndjk1UnF6cTRDbk5WRmVMQ2dB?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxOYnE5LVJmSmZVNUpwdHBvbFJ5NEdpTlFJeDJQeUNBME0yY2Q1c1g3Q0xTZjZ6Snh6akotMWZscEpsWXUzREJidFRKLXJYcW1uNmtIZjF1a1RjbmNMZEVxTVBpTzlGYlZXbkFHRmExY0FYWVQ5R3JiN0tLWEZQeFhEVUMwdkF1UG1SVUg2cXR6eTdES25pTWp3OWloYkFhdDAzNHNqdHVmZ3RIelhNN0JSS2NLa2pSQQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOMjZvcW9FcFFlNFJTUXVNVEswUjUzNmZCYVlCVlNBUThjLUVXOFR5RHpMQm5jLWZmdF9BQnJmdU5DeWhaRkYzQTJxU3VCNEozaExWRGFQblJUTXJiNTU3ZEFNTHdncjRNQ3ZMMmtIckxkd0NmUGxOUlBFUDVpSW5RVlpqZHpiT2hpMTZMV09Rd2NyRC1YMlIzRUNEMkdxcFE?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPeHNqTHAxVnZNSjZwbkNvYVRQSGpZTjFfUUhyOGRvVmswVl9Fb2NqaWtSQzc4bWFjb25fZzl3VmhyS0lhV2pHdkNYM3JTdHd4RVEyMkdRa0xPOUdBaFFEXzdDWFVnd1ZMSmtmUURSOTkzaEUtYTEtOVNGNGEzR2VfbG12ci1YeWlENXRDcmlialo5UUQwWW9RYg?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPYWhHMi1yN2MyUnhlZmlPdFdLOTNjeURLWFlFWEc1THo3Y2JRUllZVWNIcG5PbVU2SVVIWXFQb3c5WHJxTnpPT2tmYVNxSzZXb3QyME91X2lmdXVUOHl0eW91UFA5WXBtN0dPSWlIbHVybkU2ZENISENkMTJ4WUJwaGtfMXMwbTVaRmc?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNTnRjQmJITUVpQkcyejM3NEppdUJyRldHaXJfOUZiZEd0RElCXzgyMGRYb0FQUzBnOFRaU0J2NEUwZUFXRW43Nkl0MElPOXBwQVVWN2hMMzg4SDRZaDNwVmxEWllHSDg4VmZmREc4ak9YRS0wQ0k1Z3JkSjlhckEwOG9mZ1ZHT0c3RVpvLUJseHg1em12eFVCRnE3M015UXNIWHIwVXV4WHAxV0l4RnVOVW1R?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPdnFFSGFMckxMbjBEMXpXYS1FQVhzT293aE5ZbW5pX0lTYkZRaFdXMkRzS1NfSDFHUm12ZW03V29KSnlybkdCSU5wanYzdlZXV2psTjl0OWRQUU1zMExHcXpsZ2I3cWhVNU1OcTZwcks5X21fT0lWcUFIUEtjYzJaU25uekFJLUo4bGtrZ0ZxeDBaQkpWTEs0?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxQdk5fYUZpMG1NbTN5cFBmZVV3YjJ4QXdBWDd4UTA0NGh3NEkwSGVVVjFwVlRZRVBNbnR0VGdGMXh6N05jeGVsR2hzbDRVc1pTWE1CSjR6TWJkTHFmZ3gxMGNzV09FSUszVzZpdTRadkxsdWlhVllJeVFrakRSd0xoQnVJOU9hV1BWUGxzWUk2Szk5REk?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxPUWlrZHk4TEhaNmlmR1VzenhJdXpHZHJfT1JHeGpNSFdidk05Uzdqa20zYzJ5Y0ljUVlwWTBPTVJfSnktaU90dVZUemY4d01iVGVULURGQWxPNEwweWdWRkl0aGtWSVd2TWlCcG82UE1xNkpjdU5XcEJEVjFEck9HTmhiMThFTE1yRFJtbDNpakFPWmpfaG0zRDBtMkR5ZlMteUE5eS1jSk5DY2NJd1M2MEhIdXo2MGIzcGtscnp2allVdjFjMDloS0Z3aWzSAdIBQVVfeXFMT0JqTUNZbHJvQS1IbmRKdXBvSnRFenRfUTBZWlByX2twWjFSTzU1UWxmbzVhWFIwY0J5Vk1kQi1CYkk4Z1E0WXVEdEstMWxCX2VQNHNiUEx5YzRlYUhVQW94eGlyYURuY1VvMm1rVGR2V1pBNGs3d0NjQ0lnOUtkcFFoeDZZZHQzNGxjZ0FrTjBBU0dzbFlUSWxnLW95R1RLRzhtRmhLWXhRNGYxdi1WVGtKMUdYUEZwRW54Xzg2dWhtcUVHcTVmOFNIZjVTZktMWmxR?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQVE5MSkpSQ0tVbnVQMUlxdG5KWno4SDFhc1F6ZXhXcDlMODFxSDJIdzNDMktxeDFWWlVPQ2tOMF9UMkZnaFl3Zk9mZFEyUV93NE1CSFZvWVNPc2lRei1JNU5LSWFyM2FVVHlUWHRLZkM3UG5ZeFdISDBRSHlxOXRKbDBZdmhXc0pHNVE?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPeFFhVlZab1RURE5HZzBkSVMydlBCNmJzOURnaDhXVHYxN2RGa2t1Q0ZjWm0zR3lveHJMUVEwaExMYU5Ud1RlcTg1aXljZXZibjR5M2F4VHhsTjRBcnE2M1JyclZfYndvVHk3WmRSTU9adWxfcjJYa0Nkb0hGRktNVGVudlRBSzRWZElTT2FsQVZpOENEZzE1MTRXLUc3UmM?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
