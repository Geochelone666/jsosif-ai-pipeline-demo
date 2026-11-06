# CAT Intelligence Report

- ticker: **CAT**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/CAT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CAT/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:16:42.277345+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 6, 'ai': 12, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **15** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/CAT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 1, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 15 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 553.6400 |
| Return 1D (%) | -6.3690 |
| Return 1W (%) | -14.4812 |
| Return 1M (%) | -34.5678 |
| Return YTD (%) | -2.5349 |
| Return 1Y (%) | -1.8979 |
| Annualized volatility (%) | 40.7310 |
| Beta vs SPY | 1.7642 |
| Max drawdown (%) | -47.7898 |
| Sharpe (rf=0) | 0.1562 |
| Downside deviation (rf=0, %) | 29.2552 |
| Sortino (rf=0) | 0.2175 |
| Historical VaR 95% (1D, %) | 4.2437 |
| Historical ES 95% (1D, %) | 5.7878 |
| Correlation vs SPY | 0.5888 |
| Tracking error vs SPY (%) | 34.5224 |
| P/E (trailing) | 23.20 |
| P/B | 11.83 |
| EV/EBITDA | 16.96 |
| Revenue growth (%) | 17.30 |
| Forward P/E (estimate) | 17.17 |
| Gross margin (%) | 30.21 |
| Operating margin (%) | 20.51 |
| Return on equity (%) | 56.14 |
| Free cash flow yield (%) | 1.63 |
| MA50 | 763.9680 |
| Close vs MA50 (%) | -27.5310 |
| MA200 | 805.7958 |
| Close vs MA200 (%) | -31.2928 |
| RSI (14, Wilder) | 19.7409 |
| MACD (12,26) | -53.4709 |
| MACD signal (9) | -40.3419 |
| MACD histogram | -13.1291 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CAT': 276, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 553.6400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -6.3690 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -14.4812 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -34.5678 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -2.5349 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -1.8979 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 40.7310 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 29.2552 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2175 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.2437 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.7878 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5888 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 34.5224 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.7642 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -47.7898 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1562 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.1658 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 30.2110 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 20.5060 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 56.1350 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.6288 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 23.2037 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 19.7409 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -13.1291 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -27.5310 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -31.2928 -> Clearly below the moving-average trend level.

## TAILWINDS

### Caterpillar Inc. (CAT) is Attracting Investor Attention: Here is What You Should Know
- Summary: Investor interest in CAT signals positive market sentiment.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOV1Jhck51RTVLT1FVR3dERFdBa3VIQUF4ekRrY0k5SWhFYWlTaklKM19EdkJ4NlNlU0NQR2c5QS1jcWFpUDVkWEpmVm1CVjJaRUhJR01jWG1YeXNrY21LWEVmX3lRNmRheFc3SXJmZFZWSFRya2JIMzNsUjdKQU95TzkwZkNBSkVyaTNfV2pHM1hNZ0loRkcxOW8yVFI3aVhudTMzS3IxVQ?oc=5>

### Caterpillar Crashed By 25% Over 6 Months But This Global Banking Giant Says 85% Gains Will Come
- Summary: Analyst predicts 85% upside after 25% decline.
- Date: 2026-11-02 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNZkROdDhoUDNnTnpVcjhLWTdMWk91dk94d3o3T1JvbkdzeWphbjNLWTBpZU9GVkwtcTF2TFNTV0dvVnJRU3BVQ3BaNFFCNG56c2s3QUlZWnJKTHF6UDluV3VaaG1iblhCT1ZXVlV1UVZrLWVyeEw5aFlXRGxJZUVGUXVYbnQ2S2VKNmtaVUZCMHNWMHotXzM5eTBn?oc=5>

### Caterpillar Inc. stock outperforms competitors on strong trading day
- Summary: CAT stock outperformed peers, indicating strong trading performance.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxPSkJPU0x4Rlg2eDlzZGtzckNDZ0xTSS0wak00aHZ3aDhkLTZ1d1VHWXB5b1lkN010WXExWFFfcGt6dnRBX3hmdUZlZndVQnEtb0l6b1hZbzVZQVZXZkNxY2RQRjlTelpnVVZpaFVmblZ6RDc5WnBBeXh2c25hMmg4U2pRaXZaQ0lLVjcxZjRxbUh5dHpObG9WMFZRUFlNLUVELVlrWkVDdUUyMXA4SGZLZHd4Z0NyOTV3amU3bFFsS2Vxbm9vb2pCamxKWmltZlg5RUJXM0RuV2FIUnFMM1E?oc=5>

### A dealer with 100+ years of customer ties is now owned by Caterpillar.
- Summary: Caterpillar acquires long‑standing dealer, expanding distribution network.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQdk5fYUZpMG1NbTN5cFBmZVV3YjJ4QXdBWDd4UTA0NGh3NEkwSGVVVjFwVlRZRVBNbnR0VGdGMXh6N05jeGVsR2hzbDRVc1pTWE1CSjR6TWJkTHFmZ3gxMGNzV09FSUszVzZpdTRadkxsdWlhVllJeVFrakRSd0xoQnVJOU9hV1BWUGxzWUk2Szk5REk?oc=5>

## HEADWINDS

### Caterpillar (CAT) Stock Slides As Q3 Results Leave Tariff Questions
- Summary: Caterpillar (CAT) Stock Slides As Q3 Results Leave Tariff Questions
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOMlBwYlpXM2FiMVFzcHJtem9USGJuVU04NGNROUJWM0t6SmkzcFdPUllPSElXYjRuaDAyY0hGcDdkN3Z3RUUtb1VOeWJ3c183X3VLNU5zYlhKcDllZVVXcTE3aVdrekNHVjBrYUpUMlpQWl9uMElVbDFGSTdfdlNocERHZzhVMHZRVklvQ3hHYl9ZM19ZNWl1Nmt6dmg?oc=5>

### Caterpillar Stock Fell Nearly 13% in Two Days Despite a Record $78 Billion Backlog. Its CEO Says Margins Are “Skipping Along the Bottom” of Its Target
- Summary: Caterpillar Stock Fell Nearly 13% in Two Days Despite a Record $78 Billion Backlog. Its CEO Says Margins Are “Skipping Along the Bottom” of Its Target
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOWUJSUEJRVFczaThZX015WnRGZ0ZyMmE2RUp6QW85bWFqbzl6SXVZU0xDZjNkT0JfZ0YzSklXQmpQTkNIQkJzVGlVcjhFc05oLWFmb2lkbVdEOEhKZzhKSjlpQVlnN05mZXVGMGZQdjZ0aHZjWVFiaE1WTzlvZE80WHV3TWRKckhLQUlzS0FWeXZhc2xfNlRad29YTDFLdw?oc=5>

### Caterpillar Revenue Miss, Outlook Dig Hole For Dow Jones Industrial Average
- Summary: Revenue miss signals weaker performance, negatively impacting market outlook.
- Date: 2026-10-29 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNRk54ajQ4MHcydlBCcGgtb21UekZtYnFXdVJGVF91d1ZwSjJqYUsxaXlZUWhoMFJaekV5QjlvU2tlTThoS0w3aUpIRzJqVkRoeDg2VUQzaGRjNmM3dnpzQUZVUE81czY2VUxseEVwZU5KQVJBbURuY3RRUDY3N2ZNaUpsY3kzMGFwcjRlaDBaRTRXOTdXTG9DYk93?oc=5>

### Caterpillar’s Sell-Off: Is the Market Missing Its AI Power Play?
- Summary: CAT shares declined, suggesting market skepticism.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxQOHNpSVI1NUxiR0xtUGNVa081TEdfSnV3QXhha2xwcGxtZ01laUotaVhOVEZkclQ5RmoyeUd6NFAxaXowUW9IT0xDbHRuTjRwS3VEQjhnRm9JM09ibmlCUEw2WFN1TndmdHFSUUhnUHlpcWVQX2tVRTFCOTdEclhMNnV5aHZpVUEtNl9hTTB0clVkRVMxYnVyXzVVQ0JsNTRWeUlvZ0YzM0FkUG5yLXFPOUFSMm56b2Yyd3ZnVjlET2M?oc=5>

### DA Davidson cuts Caterpillar stock price target on valuation concerns By Investing.com
- Summary: Analyst lowers price target due to valuation worries.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxQaTk4TjNrV21nUWwtcWNyNlI0dS0xMHdQR0cwZmpYLTRfakZLTFNXZjVWUmtxYkNuTk96dU1xVnVnTS12VW9mMWpYaEY3MVJXdUpJaVd5bE9EZ013aWlJNEZQdkR6MF9FRmhFS2pTMHByZEdqX1ZoRmN5OGl4bVBiRExFNzV5ck82WmgzWlk1dFh0VENmN0YyZnRYYy1tWE50bnBDbTg3TjJSdEVyR2I4UjB0c0NnN3oxY21ZYXVFbGpzNENfSVBwVjlR?oc=5>

### Caterpillar price deepens losses - Forecast today - 03-11-2026
- Summary: Stock price continues to decline, widening losses.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxNRjExWDAtVDRlM01TQXRtSHQ0SUtFclVnU01OYjZHdW95cUFBZ3ZsVlNfcEtWLXBYQWNXMC1HM25LY1ljamQ3U3A2WG9ZU0l3V3FaZVhqbE1ybGIxY1Z3WHdpSDBMcWpLTnpRVGNJT0JLVDJiVVMwakFfelp2d2R2MXc5WUdVNEFoWWxkaTFBbjVzcmFyZHRoT2ZVSHc4aG5va0FIZEdvYW8yaVBYODhlV0dvaEJ0SzI3YmxqcjlCdHlRZE0?oc=5>

## CATALYSTS

### CAT Stock Gets Price Target Cuts – Analyst Flags ‘50% Premium’ To Peers
- Summary: CAT Stock Gets Price Target Cuts – Analyst Flags ‘50% Premium’ To Peers
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQX21nNFl0am9GM0VHNlZESnBDenRxVmI0UnNlRnVLVUw3VXJIT05nZ2FyWk5KZDhFTG4zbjlJUEtSejcxRUxSaHlfSllJWi1iUjUyM19lazQ4dlZhOE1Gb0JjMWx2SGVXWk9QTEhjQnpacjVMcHh3T1U4VTh1TS02NG5LREpndjk1UnF6cTRDbk5WRmVMQ2dB?oc=5>

### Caterpillar Inc. (NYSE:CAT) Just Reported Earnings, And Analysts Cut Their Target Price
- Summary: Caterpillar Inc. (NYSE:CAT) Just Reported Earnings, And Analysts Cut Their Target Price
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQVk9ZNHYzTHN0ZWVjZDZqMnpuWE56NnJpNDZraXVtN1RqamhWcXlPa1c5N2ZYS2ZaczF0d21QWHBfTU1TSExyNzhIZFRORlY3M1BtTmpXaXlxeWgwQ29lem53MEhIMUk3QmJqZjBOT0RsdzZQRXBNSXVKY290UkVUSUdxRGJEM3c5Y1RzOUJEcUNiaHJhR0VnT3ZSQUhzNjh1QVoyczNfdTFlMXV1?oc=5>

### Caterpillar Inc. Acquires Fabick Cat Dealership
- Summary: Caterpillar Inc. Acquires Fabick Cat Dealership
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNdWhHeHNNemRFWjlvaERmMFhnVDNDanZvZGdlU282QzRoSkJvLVJqakQ1XzNBYnQyR0ozdXhYRlZVVjY4c2JaUGlMYWZRMmNFazZfUEdZQU84WWVKRzlndjhDbkJuZFNuakpvQjZQZ2NXTHpZb3o2b2Q3cVlpZzczcW5OT1RMWEt6YnZKNGVDejlIODNSVFd0ZDBJR3ptQThTV0E?oc=5>

### Caterpillar Q3: Growth With A Caveat, Shares Fairly Valued (NYSE:CAT)
- Summary: Caterpillar Q3: Growth With A Caveat, Shares Fairly Valued (NYSE:CAT)
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQVlF3UlBDVFhsSkg0bGNPX2VuRXI0V2ZvdklaXzF0bS1TMWJjcU9fN0RvT3JPbWpBdkU1VEJxbDhEWFhqal9HaFBmSGFOejVqLW5sbmhhazlKQ1BDTjBYQW1VVmJ5QmFHYzg0R2dsa1hhSXBKRE91OVVyUHh1MnVfS3lodFlOWGdWVFZuMnZIbUlnOC1nU0E3Q3QtT2xMdw?oc=5>

### What Could Caterpillar (CAT) Gain From This Dealer Acquisition?
- Summary: Potential dealer acquisition could boost CAT's market reach.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOMjZvcW9FcFFlNFJTUXVNVEswUjUzNmZCYVlCVlNBUThjLUVXOFR5RHpMQm5jLWZmdF9BQnJmdU5DeWhaRkYzQTJxU3VCNEozaExWRGFQblJUTXJiNTU3ZEFNTHdncjRNQ3ZMMmtIckxkd0NmUGxOUlBFUDVpSW5RVlpqZHpiT2hpMTZMV09Rd2NyRC1YMlIzRUNEMkdxcFE?oc=5>

### Caterpillar Stocks Move Lower With Target Cut Putting Its Margin Premium on Trial
- Summary: Caterpillar shares fell after analysts lowered earnings target, testing the company's margin premium.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPQ2tBSV9ER1FJOG42QXE3U25MT1lDMFQxQVpPSklsODFnejNESFFUenpBNXJRZmJkODF6Sl9RTHdhWk02cUNvbDJaNUpVS1h5YV84S3ZCRU1wdjk2YjVJelJGaHpUQTFQVG9Zem4xcE1SQ0JFUkE4Q29tLVhscjVnSE04dFRvOFQ2bDlrY3hlMk9FOXlwQlpWR0c0a3F0T3UzY3dkSEczdFNoTHJoS3FXYm5OOTNQTGVBWGJ3Zg?oc=5>

### Could Caterpillar Actually Climb 65% After Its Earnings Slide? Or Is Truist Totally Wrong?
- Summary: Speculation on post‑earnings rally after earnings dip.
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNUmtGRzkzSXdiSHFRWGZTSXNxZ0xnQ0pFc0NhLXJNREdYWXM3bHpjU0ViMmpUSHVpeTR0VmlzRE5oZ01feDBVN2d5eXduc0pyU0tEQm1YSTVxejhNcy1tblliZGxiRVBrUmMxeEM3b0tIdHNPNWhqcUxMQ3FaMVVwS3pPaDRWbnYzcDlqX1pqcmg?oc=5>

## RISKS

### Caterpillar Inc Stock (CAT) Moved Down by 5.03% on Nov 5: Drivers Behind the Movement
- Summary: CAT shares fell 5.03% on Nov 5 due to market selloff and valuation concerns.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQVE5MSkpSQ0tVbnVQMUlxdG5KWno4SDFhc1F6ZXhXcDlMODFxSDJIdzNDMktxeDFWWlVPQ2tOMF9UMkZnaFl3Zk9mZFEyUV93NE1CSFZvWVNPc2lRei1JNU5LSWFyM2FVVHlUWHRLZkM3UG5ZeFdISDBRSHlxOXRKbDBZdmhXc0pHNVE?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CAT** | **23.20** | **11.83** | **16.96** | **17.30** | **253,342,449,664.00 USD** | **-1.90** |
| DE | 37.60 | 6.39 | 27.50 | 4.90 | 178,845,220,864.00 USD | 41.63 |
| CNH | 46.88 | 1.80 | 36.92 | 2.00 | 18,091,786,240.00 USD | 8.49 |
| CMI | 18.71 | 5.02 | 14.02 | 9.40 | 61,753,532,416.00 USD | 3.63 |

Peers fetched as_of: 2026-11-05; CAT reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-05

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMipwFBVV95cUxOV1Jhck51RTVLT1FVR3dERFdBa3VIQUF4ekRrY0k5SWhFYWlTaklKM19EdkJ4NlNlU0NQR2c5QS1jcWFpUDVkWEpmVm1CVjJaRUhJR01jWG1YeXNrY21LWEVmX3lRNmRheFc3SXJmZFZWSFRya2JIMzNsUjdKQU95TzkwZkNBSkVyaTNfV2pHM1hNZ0loRkcxOW8yVFI3aVhudTMzS3IxVQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNZkROdDhoUDNnTnpVcjhLWTdMWk91dk94d3o3T1JvbkdzeWphbjNLWTBpZU9GVkwtcTF2TFNTV0dvVnJRU3BVQ3BaNFFCNG56c2s3QUlZWnJKTHF6UDluV3VaaG1iblhCT1ZXVlV1UVZrLWVyeEw5aFlXRGxJZUVGUXVYbnQ2S2VKNmtaVUZCMHNWMHotXzM5eTBn?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxPSkJPU0x4Rlg2eDlzZGtzckNDZ0xTSS0wak00aHZ3aDhkLTZ1d1VHWXB5b1lkN010WXExWFFfcGt6dnRBX3hmdUZlZndVQnEtb0l6b1hZbzVZQVZXZkNxY2RQRjlTelpnVVZpaFVmblZ6RDc5WnBBeXh2c25hMmg4U2pRaXZaQ0lLVjcxZjRxbUh5dHpObG9WMFZRUFlNLUVELVlrWkVDdUUyMXA4SGZLZHd4Z0NyOTV3amU3bFFsS2Vxbm9vb2pCamxKWmltZlg5RUJXM0RuV2FIUnFMM1E?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxQdk5fYUZpMG1NbTN5cFBmZVV3YjJ4QXdBWDd4UTA0NGh3NEkwSGVVVjFwVlRZRVBNbnR0VGdGMXh6N05jeGVsR2hzbDRVc1pTWE1CSjR6TWJkTHFmZ3gxMGNzV09FSUszVzZpdTRadkxsdWlhVllJeVFrakRSd0xoQnVJOU9hV1BWUGxzWUk2Szk5REk?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOMlBwYlpXM2FiMVFzcHJtem9USGJuVU04NGNROUJWM0t6SmkzcFdPUllPSElXYjRuaDAyY0hGcDdkN3Z3RUUtb1VOeWJ3c183X3VLNU5zYlhKcDllZVVXcTE3aVdrekNHVjBrYUpUMlpQWl9uMElVbDFGSTdfdlNocERHZzhVMHZRVklvQ3hHYl9ZM19ZNWl1Nmt6dmg?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOWUJSUEJRVFczaThZX015WnRGZ0ZyMmE2RUp6QW85bWFqbzl6SXVZU0xDZjNkT0JfZ0YzSklXQmpQTkNIQkJzVGlVcjhFc05oLWFmb2lkbVdEOEhKZzhKSjlpQVlnN05mZXVGMGZQdjZ0aHZjWVFiaE1WTzlvZE80WHV3TWRKckhLQUlzS0FWeXZhc2xfNlRad29YTDFLdw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNRk54ajQ4MHcydlBCcGgtb21UekZtYnFXdVJGVF91d1ZwSjJqYUsxaXlZUWhoMFJaekV5QjlvU2tlTThoS0w3aUpIRzJqVkRoeDg2VUQzaGRjNmM3dnpzQUZVUE81czY2VUxseEVwZU5KQVJBbURuY3RRUDY3N2ZNaUpsY3kzMGFwcjRlaDBaRTRXOTdXTG9DYk93?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxQOHNpSVI1NUxiR0xtUGNVa081TEdfSnV3QXhha2xwcGxtZ01laUotaVhOVEZkclQ5RmoyeUd6NFAxaXowUW9IT0xDbHRuTjRwS3VEQjhnRm9JM09ibmlCUEw2WFN1TndmdHFSUUhnUHlpcWVQX2tVRTFCOTdEclhMNnV5aHZpVUEtNl9hTTB0clVkRVMxYnVyXzVVQ0JsNTRWeUlvZ0YzM0FkUG5yLXFPOUFSMm56b2Yyd3ZnVjlET2M?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxQaTk4TjNrV21nUWwtcWNyNlI0dS0xMHdQR0cwZmpYLTRfakZLTFNXZjVWUmtxYkNuTk96dU1xVnVnTS12VW9mMWpYaEY3MVJXdUpJaVd5bE9EZ013aWlJNEZQdkR6MF9FRmhFS2pTMHByZEdqX1ZoRmN5OGl4bVBiRExFNzV5ck82WmgzWlk1dFh0VENmN0YyZnRYYy1tWE50bnBDbTg3TjJSdEVyR2I4UjB0c0NnN3oxY21ZYXVFbGpzNENfSVBwVjlR?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNRjExWDAtVDRlM01TQXRtSHQ0SUtFclVnU01OYjZHdW95cUFBZ3ZsVlNfcEtWLXBYQWNXMC1HM25LY1ljamQ3U3A2WG9ZU0l3V3FaZVhqbE1ybGIxY1Z3WHdpSDBMcWpLTnpRVGNJT0JLVDJiVVMwakFfelp2d2R2MXc5WUdVNEFoWWxkaTFBbjVzcmFyZHRoT2ZVSHc4aG5va0FIZEdvYW8yaVBYODhlV0dvaEJ0SzI3YmxqcjlCdHlRZE0?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQX21nNFl0am9GM0VHNlZESnBDenRxVmI0UnNlRnVLVUw3VXJIT05nZ2FyWk5KZDhFTG4zbjlJUEtSejcxRUxSaHlfSllJWi1iUjUyM19lazQ4dlZhOE1Gb0JjMWx2SGVXWk9QTEhjQnpacjVMcHh3T1U4VTh1TS02NG5LREpndjk1UnF6cTRDbk5WRmVMQ2dB?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQVk9ZNHYzTHN0ZWVjZDZqMnpuWE56NnJpNDZraXVtN1RqamhWcXlPa1c5N2ZYS2ZaczF0d21QWHBfTU1TSExyNzhIZFRORlY3M1BtTmpXaXlxeWgwQ29lem53MEhIMUk3QmJqZjBOT0RsdzZQRXBNSXVKY290UkVUSUdxRGJEM3c5Y1RzOUJEcUNiaHJhR0VnT3ZSQUhzNjh1QVoyczNfdTFlMXV1?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxObzNjZXBpS2s1QVp3U1hVTlE0NWJ1UC0xYU5zUnJwYlFCQ0FzR0J4THpZTzNwQzBmaXBtRkgwQklrZll1OHJ1SUtjanVlZVhfWldScXE5X3UyQlFsQ1pDeEVoZDFpekFHUHJNaGlkX25OeHRyZmpKMjh6ZEVhaElrSFJYUGhVTFlKbzU5WmkxUGZQLTc5cGR6all2aVZUd3lUN29Ha0tVOTEzVFByVGZuT04zWnRnQm1iV3hReF9Db2ZsSUZIM3hXZ3djSdIB0AFBVV95cUxOa3B2NzZnY2dnLWVubkdVSXEwQ0RjU1RjN2x6djVRZlRxaDNYQ3pjVXhPUEVkNlRhN25sQVY3SUNvOE9IbGk2d0NXQjQxRmk4b1d0WGJVMFBmaWR5OUc5UkJjY1ljU096ZHZ5d1lJUGdQbFFRZHZGdWNmcjN2VG13ZXJPQlZrdTg4aExvMFJuWncyeUtBeVBxaW9UU1ltR0EwYWIzcFhQa0JZNVI2NkFLRVFUYV9GNXo3Zm9OZm1zZk8weUZYWEdBeGVDNHZRYjBv?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNdWhHeHNNemRFWjlvaERmMFhnVDNDanZvZGdlU282QzRoSkJvLVJqakQ1XzNBYnQyR0ozdXhYRlZVVjY4c2JaUGlMYWZRMmNFazZfUEdZQU84WWVKRzlndjhDbkJuZFNuakpvQjZQZ2NXTHpZb3o2b2Q3cVlpZzczcW5OT1RMWEt6YnZKNGVDejlIODNSVFd0ZDBJR3ptQThTV0E?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQVlF3UlBDVFhsSkg0bGNPX2VuRXI0V2ZvdklaXzF0bS1TMWJjcU9fN0RvT3JPbWpBdkU1VEJxbDhEWFhqal9HaFBmSGFOejVqLW5sbmhhazlKQ1BDTjBYQW1VVmJ5QmFHYzg0R2dsa1hhSXBKRE91OVVyUHh1MnVfS3lodFlOWGdWVFZuMnZIbUlnOC1nU0E3Q3QtT2xMdw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOMjZvcW9FcFFlNFJTUXVNVEswUjUzNmZCYVlCVlNBUThjLUVXOFR5RHpMQm5jLWZmdF9BQnJmdU5DeWhaRkYzQTJxU3VCNEozaExWRGFQblJUTXJiNTU3ZEFNTHdncjRNQ3ZMMmtIckxkd0NmUGxOUlBFUDVpSW5RVlpqZHpiT2hpMTZMV09Rd2NyRC1YMlIzRUNEMkdxcFE?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPQ2tBSV9ER1FJOG42QXE3U25MT1lDMFQxQVpPSklsODFnejNESFFUenpBNXJRZmJkODF6Sl9RTHdhWk02cUNvbDJaNUpVS1h5YV84S3ZCRU1wdjk2YjVJelJGaHpUQTFQVG9Zem4xcE1SQ0JFUkE4Q29tLVhscjVnSE04dFRvOFQ2bDlrY3hlMk9FOXlwQlpWR0c0a3F0T3UzY3dkSEczdFNoTHJoS3FXYm5OOTNQTGVBWGJ3Zg?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNUmtGRzkzSXdiSHFRWGZTSXNxZ0xnQ0pFc0NhLXJNREdYWXM3bHpjU0ViMmpUSHVpeTR0VmlzRE5oZ01feDBVN2d5eXduc0pyU0tEQm1YSTVxejhNcy1tblliZGxiRVBrUmMxeEM3b0tIdHNPNWhqcUxMQ3FaMVVwS3pPaDRWbnYzcDlqX1pqcmg?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQVE5MSkpSQ0tVbnVQMUlxdG5KWno4SDFhc1F6ZXhXcDlMODFxSDJIdzNDMktxeDFWWlVPQ2tOMF9UMkZnaFl3Zk9mZFEyUV93NE1CSFZvWVNPc2lRei1JNU5LSWFyM2FVVHlUWHRLZkM3UG5ZeFdISDBRSHlxOXRKbDBZdmhXc0pHNVE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
