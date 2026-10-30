# MU Intelligence Report

- ticker: **MU**
- Report as_of: **2026-10-29**
- Market data as_of: **2026-10-29**
- Quant sources: https://finance.yahoo.com/quote/MU/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MU/key-statistics/
- AI analysis snapshot as_of: **2026-10-29**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-30T02:29:45.604874+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 1, 'ai': 18, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261029T020157Z-688a53f0/MU** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 9 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 52.17%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 934.2700 |
| Return 1D (%) | -4.9795 |
| Return 1W (%) | 9.0813 |
| Return 1M (%) | -12.2679 |
| Return YTD (%) | 227.5826 |
| Return 1Y (%) | 312.7128 |
| Annualized volatility (%) | 81.6527 |
| Beta vs SPY | 3.4024 |
| Max drawdown (%) | -39.0954 |
| Sharpe (rf=0) | 2.1486 |
| Downside deviation (rf=0, %) | 49.1547 |
| Sortino (rf=0) | 3.5692 |
| Historical VaR 95% (1D, %) | 7.0055 |
| Historical ES 95% (1D, %) | 9.5345 |
| Correlation vs SPY | 0.5296 |
| Tracking error vs SPY (%) | 75.6931 |
| P/E (trailing) | 12.57 |
| P/B | 7.64 |
| EV/EBITDA | 9.36 |
| Revenue growth (%) | 379.30 |
| Forward P/E (estimate) | 4.50 |
| Gross margin (%) | 80.72 |
| Operating margin (%) | 80.68 |
| Return on equity (%) | 88.26 |
| Free cash flow yield (%) | 2.76 |
| MA50 | 980.3809 |
| Close vs MA50 (%) | -4.7034 |
| MA200 | 743.8667 |
| Close vs MA200 (%) | 25.5964 |
| RSI (14, Wilder) | 47.1534 |
| MACD (12,26) | -22.7051 |
| MACD signal (9) | -23.5753 |
| MACD histogram | 0.8702 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MU': 271, 'SPY': 271}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 934.2700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -4.9795 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 9.0813 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -12.2679 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 227.5826 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 312.7128 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 81.6527 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 49.1547 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 3.5692 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.0055 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 9.5345 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5296 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 75.6931 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4024 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -39.0954 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 2.1486 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 4.4959 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 80.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 80.6780 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 88.2600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.7567 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 12.5692 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 47.1534 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.8702 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -4.7034 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 25.5964 -> Clearly above the moving-average trend level.

## TAILWINDS

### Micron Just Unveiled a New Bonus Plan. What That Means for MU Stock.
- Summary: Micron introduces a new bonus plan, potentially boosting shareholder value.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPSVp0SEVqV2ZKY1BKYXJGZXhZcGZNVzZwdnBrV0NhWGtTaTEwMVNBb0hjZEx4b1VYR1B6UzdJNzdXaE5OZFhSZzhZQlhhWmNSelFxYXRCaG8tTEVHRU9DZE5TcmZDaXdHRzdBTjhlbDhqNGM2d1lQbnZpbVdlb1ExSTlXaDB3UzhXd081UzU1Wkp0OE9YT1pOWFFUZjR3V252TkxBTHI1T3J5aEdzdDcw?oc=5>

### Micron Technology And 2 High Growth Stocks To Watch
- Summary: Analyst highlights Micron as a high-growth candidate, suggesting bullish outlook.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQbzV4YU5OcU1iY09HVlFneGh3SWE5S1VLQ0xWdE9OZDFYcmpMX2tuUGdKckhlTEs0dTFCbE5OY1EwRjhNdV80VTU2bnJRSmpGQ2M5al9CcXBvMEhaTk1lLWhRM0pxcWtEX1dZQXZ0b1pNRXp5V25zT09UYUFkMThZbV9ZbS1lR1R5N2NpSE41ZjhmbWFiYWRzZTVMcm8?oc=5>

### Why Micron Technology Stock Rallied Today
- Summary: Micron shares experienced a rally today, indicating positive market sentiment.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxNbzJCRVVpMElSTVRlQ2ZoTmE2RUtEVWFYei15Ykg5TUhobGVhaGZabGtUZzJ1VFM0WHFCWGdETHQ0dVFnQ3N5SDFyRjQ4c250OG43ei14YUs4bjB5VUVRWmtVTWtTN0J2TVVHVzZQcG40X1hSbzJubnVYUGJHRE5ueXUzRDVsQUV3M0RWdQ?oc=5>

### Why Micron Stock Is Up Today
- Summary: Positive market sentiment drives the stock higher today.
- Date: 2026-10-28 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQYTJMOG1zSzlhSmpGWWI2MEp6Z3N5REo2Z1lUbzBjNkN6YzBVOEI3VlNBTkNUODJQaVRnU3Zfb2RvRTROMWQzemhaVXZmX2piQ3NBTGxSNDFfaEt6RmJiNWQxSFpvTkQzQmJQWW1uY0VlbFhZSGFTRTNVdklodWFIb01mazJPTUlmeVg3Sk15aXc?oc=5>

### Micron (MU) Sees $70.4 Million in Net ETF Buying on Tuesday
- Summary: Significant ETF inflows support the stock.
- Date: 2026-10-29 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQeTVLdENfbVBoUzFuQXEwUWhidFQ4X1VGemlDZ0huSExaRDFMVGU1ODljWVFDZUNXbjQyZGEtaUZFZ09pVURjeTB3Q1pKVHpOOFpGejZiQzFLd0h3U0dKaDEwcVZqYldFS2xybGxmeTJoam03TS1FSlVhdTJoSWU4RXd3bE5fRVRpUWwtUg?oc=5>

## HEADWINDS

### SA analyst upgrades/downgrades: GOOG, MSFT, NBIS, MU
- Summary: Analyst changes for MU could impact market perception.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxPMDhIM08yQmdNbkJDS2lzak9KeTdRMkpndnZjNmNvZE9EaE1sNGNoaDhqTGNWT21VVVhLRTZfbGxkdmQ3Y05RMW83Ml80YXVqYmtXR2VXTkZsWXg5eVB0a2QtLUFERTNoVUtwc1BJTjBNT2p1Y1JJbFlKdzRSVWt4MWFYS1ZOYW1WRUprQ2h3?oc=5>

### Why Is Micron Stock Falling on Thursday? - Micron Technology (NASDAQ:MU)
- Summary: Micron shares declined on Thursday, reflecting negative market sentiment.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPdUZDRV81aENnRmpoMFo1cVU0UkZPc21pZEwyM2hpTWlQZlZFWGNMWEl0ZkVkNzBNdXVIUjhfMkNJV1ltOHVsQ0lYNFFTcHlLbFlTMXJIR0FtT3doNGdxUDBTMEEzV080R0RoOWsyYTRBMmNVNWYxdVFrRDdfUWdUY1FZTnB6R3RkNlVldXZEcTlRQk5hQzJQTlNOZmtMV091YmpRYw?oc=5>

### Micron Stock Falls as Samsung Earnings Show the High Bar for Memory Stocks.
- Summary: Micron shares fell after Samsung's earnings set a high benchmark for memory stocks.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxQYVprRmdFU1M2cmhCUUhmd0RnNFFpX19leG13UjlOOUwwMVUzSTA5NW5wNllZd0JGem1IOFpCeS1yQXlPS3FrTWZ5TWptanlvbkNtQllncjE2ZE9pVkRFX1NVNEFDTUo2NWVDYUw3VGw3TWhKbGVsMThGc1lxSFhiUFRkRS0?oc=5>

### Micron’s Operational Execution Collided with Macro Tape Fatigue, So Now What?
- Summary: Operational challenges amid macro fatigue weigh on the stock.
- Date: 2026-10-29 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxNREROVnE2dFN6STRQajJhbEsyRjBlRkVzVHd2X2xtR3JTbUtMWTNpYXZDbTVBRi1uZ3RULXIwaGIxTGFEMHRYZkxHclF5ZmdZWXo1MUtMRE03eGpQdUhDX19sN0hFRjR6cmdtblF5MzNuZ2NLcnVxRkVrZDA4VWk4T2Z2bVNhYmFBZEZKWGxBUzBKaFN6V1FpRkFBdGQzZ0FhTlZRYlBaVXBIazAy?oc=5>

### Is Micron Stock Riskier Than It Looks?
- Summary: Risk perception may be higher than fundamentals suggest.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPakhON3hhTlhKQ2Zqdkp6djZHZDNnWklCV1lZRmdiMzBfM2VzbFNza2swWFJnS01zUTR0dFYwZkc3VE1FZk9GdVdvc1Judnp3RU9NYjhYcTRlYVNyeGFhNkJSX3RaQjNsd0dNYnMtVEpfWkNSbld2a253Zkc4Y2lQeXZORXlhVlpiT2h0Q2NnSzFISEVadXc?oc=5>

### Sandisk and Micron Slide 5% as Samsung Miss Cools Memory Rally Ahead of Sandisk Earnings; SK Hynix Falls 3%, Western Digital Dips
- Summary: Micron shares fell 5% amid a broader memory market slowdown triggered by Samsung’s miss and weak earnings outlook for Sandisk.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPb0lURlNVYTFJWUJFR1VKbnJGTzdTTGstMXJNVjhudzNZc1NKQ25uVUY2TTBjZm1Hc2x4d2paYl95WXVqMXJuQkoweHVOVEhrdjlkUk1RcktucjVMb2lqc2JMTkk1c19VY1NVaHNMcjRFWVV1VVpfeTNkaS16amVpcno3ZnhLbmZnUk81bW1tNGlMV3hHcDZNRjd3dw?oc=5>

### Micron Technology Inc Stock (MU) Opened Down by 3.07% on Oct 29: What Investors Need To Know
- Summary: MU stock opened down 3.07% on Oct 29, reflecting investor concerns over recent earnings and market conditions.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxQV0VRS3liSWhhR3VJaTJodjUtTnFhcGxETHg3b1k5Y3RIMnFzdWdtZy1kaC1WcDdMZHFtWllOOEx3UUdRd2tDdWV6S3B2SFR2d3hadmtmTFcyRk12NXBOMEVBVUU4NThhZXpxOFl6RmZlekJqVUFjM1lySjhCUktROWpxeGhVdXcz?oc=5>

### Micron MU Stock Falls Below $930 as Big Tech Spending Misses Expectations
- Summary: MU shares dropped below $930 as big‑tech spending fell short of expectations, signaling weaker demand for memory products.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.88
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxOd1k1c3VxRVFQdU5QYVlGa01hM0Y2V0xDRkd1QUhrQy12eUhPR0hJYjNpaFViNUFiZ3p1ZXVUbEpydDRMdld6VlFaRWpJYVU0SFlObm54dGU5bk5WSHF6SmJqa20yX19QYzdFZXRTQ2htTUZ3VGRxTE94X3ZTQXY0czJmLTI3Q1BkdFFWU25pR05Yc2lCZFl6eWhCRHMzT3hEeEpNSDJYX01ILTVEdklkdjZJdWtnQQ?oc=5>

## CATALYSTS

### Micron Technology Stock: Is Now the Time for Investors to Take Profits or Buy More?
- Summary: Micron Technology Stock: Is Now the Time for Investors to Take Profits or Buy More?
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPNDVmcHh4WlRMQVZydHJ2QnRCM0E3NF9aTGd1OTRVM016LWxQU2JSLUQ0Q3NKbHVaSmRfZXVYOEhac1hkSGJHSG43elF6SEtOXy1PYW5sWk9VbUV1MWNkVU1SZ3RlM25VbUFiVUxNM0tFdTh3NEtZUnExaUd5REJEQUdyVXZEMVhNcEdiMlp5OERHUnFRVGpxYXBDYVN3NjJtcG91WUxfOVZzQnpaMzQyb1JBRTRIQ2VtUFlWYkNuSnBmdw?oc=5>

### What Could Robot Memory Demand Mean For Micron Technology (MU) Stock?
- Summary: Increased robot memory demand could boost Micron’s revenue prospects.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNR0xMVWVZZjAtdzlUbkdZdlAwSGpTM1dpd2VibzlxR0xoeVpjVlZuWVBXSFQ5dGhKRHV5TnlYLXdqdXBNZWp4VmJ3a0tBMnhRazF0WkU1Q1ZYeElwU0JFVE5zWVF6d0Z3eEJDQUwzOEczNEhDUmlCT2dxSkE3UEE1NHUyTHhoSDVlM3JmZUMzM2Fsc2g1TlZEMjVn?oc=5>

### Here's Why Micron (MU) Fell More Than Broader Market
- Summary: Micron’s share price dropped more than the broader market due to concerns over demand and earnings expectations.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPM1BFc09DcGY0QXFlMnQ5X0ZZSllHTnJDUlNlVFhwTFc4N2VSUnJqcE9jVEJ2d1E3SjFXckRRYUhkejQzQ09sNXllMnd6LUl6OFMySVB5VVVxNjVCOGRGVVBka1ZJNEM0UjZvanBBbFBIMjRKQUtKaVlpQmV6Vzg1V0hOaVRMYWpRanI2dzRMWkM0eWc?oc=5>

### Memory Mania Has Micron Back Near $1,000
- Summary: Micron’s stock rallied close to $1,000 amid strong demand for memory chips and positive earnings outlook.
- Date: 2026-10-29 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxOVmJlNVhuWUpYV2UxaTFWSmloYWFvZmhPcng5LXlseGVKdS1OSDU3Qmh6ajI4ckdUZzJuMGd6cWZIOUZqWlUxMmRXeW1UWFBLRmJ0NVRWaENrcDNDUl9iTmhIR0JwR2IxTFlqbGZPbnZDTUVXS0FUX0c5RFkwbE5Vb0w2UVRQTUJHN0E?oc=5>

### Micron: Priced For A Peak That Keeps Moving Higher (NASDAQ:MU)
- Summary: Micron’s shares are trading near a new high, reflecting bullish sentiment and expectations of continued growth.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQbk1FYjZrZWdKS1RSLWxLQVdSYVR2VEFKMWpZUlpmMDlkMEZDUVRYMDQ3SmRmbGZ2TWdvUFN3RnI0TEdGMlVVR2FfbTZleXhwZThOZHdmd3N5QnlQWVAyc3paLWEta3dKd3VtTk5CY256dG9taV9IV2xobl8xUHZWQ05ya1RjQktnYkl2eXZIOFljRkJC?oc=5>

### Prediction: Micron’s Next Earnings Cycle Could Reset Expectations for the Stock
- Summary: Upcoming earnings may shift market expectations.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPRk1BdHBUVWlsVVRRS1VQSXVsN2VGN0RtOWdxQ3lvTFhSUENYejRubGVxMkJfOVltcjBZRjBPTF8yNzZaNU1sVmh2UkZ5U2gxdHI2WkdZajZUS0Nva1Y1Ty04ZkhtR292ZG54aVJhalE5cWtScllmLTdJY2dIbFlXNmJsNkphell3alNrZVhEZUIycFgwYjlEQVFfaVdLRVRxOHFGMw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MU** | **12.57** | **7.64** | **9.36** | **379.30** | **1,057,054,785,536.00 USD** | **312.71** |
| WDC | 13.91 | 15.82 | 23.39 | 55.50 | 148,011,155,456.00 USD | 180.20 |
| STX | 36.73 | 46.66 | N/A | 61.00 | 161,108,099,072.00 USD | 165.27 |
| NXPI | 20.93 | 5.55 | N/A | 19.30 | 67,046,096,896.00 USD | 32.24 |

Peers fetched as_of: 2026-10-29; MU reuses existing data (market data as_of: 2026-10-29); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-30
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-29

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-09
- Revenue (latest available single quarter): 8,440,000,000.00 USD; period 2018-06-01/2018-08-30; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 28,243,000,000.00 USD; period 2026-02-27/2026-05-28; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMirwFBVV95cUxPSVp0SEVqV2ZKY1BKYXJGZXhZcGZNVzZwdnBrV0NhWGtTaTEwMVNBb0hjZEx4b1VYR1B6UzdJNzdXaE5OZFhSZzhZQlhhWmNSelFxYXRCaG8tTEVHRU9DZE5TcmZDaXdHRzdBTjhlbDhqNGM2d1lQbnZpbVdlb1ExSTlXaDB3UzhXd081UzU1Wkp0OE9YT1pOWFFUZjR3V252TkxBTHI1T3J5aEdzdDcw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQbzV4YU5OcU1iY09HVlFneGh3SWE5S1VLQ0xWdE9OZDFYcmpMX2tuUGdKckhlTEs0dTFCbE5OY1EwRjhNdV80VTU2bnJRSmpGQ2M5al9CcXBvMEhaTk1lLWhRM0pxcWtEX1dZQXZ0b1pNRXp5V25zT09UYUFkMThZbV9ZbS1lR1R5N2NpSE41ZjhmbWFiYWRzZTVMcm8?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNbzJCRVVpMElSTVRlQ2ZoTmE2RUtEVWFYei15Ykg5TUhobGVhaGZabGtUZzJ1VFM0WHFCWGdETHQ0dVFnQ3N5SDFyRjQ4c250OG43ei14YUs4bjB5VUVRWmtVTWtTN0J2TVVHVzZQcG40X1hSbzJubnVYUGJHRE5ueXUzRDVsQUV3M0RWdQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQU0NKUDZrYmo5dEcyMllySC1BZFRZTUxPZFp5TzJmOGl5ZTdIaEpXcWJVSWtlNDhuWGFSclN6ZkJ3d29CLUluMWtUcGowaXBadVVBY0tqVS1mUkstcHFsLXI1RWp0RmpOdm5OZzJLSktYZ0tmZ0gwRG1XMFN5ZFdtaGNnenc4TVBsczR3d25fVlFrd3dMdGJjVXlMVFlUV2JqdkE?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQYTJMOG1zSzlhSmpGWWI2MEp6Z3N5REo2Z1lUbzBjNkN6YzBVOEI3VlNBTkNUODJQaVRnU3Zfb2RvRTROMWQzemhaVXZmX2piQ3NBTGxSNDFfaEt6RmJiNWQxSFpvTkQzQmJQWW1uY0VlbFhZSGFTRTNVdklodWFIb01mazJPTUlmeVg3Sk15aXc?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQeTVLdENfbVBoUzFuQXEwUWhidFQ4X1VGemlDZ0huSExaRDFMVGU1ODljWVFDZUNXbjQyZGEtaUZFZ09pVURjeTB3Q1pKVHpOOFpGejZiQzFLd0h3U0dKaDEwcVZqYldFS2xybGxmeTJoam03TS1FSlVhdTJoSWU4RXd3bE5fRVRpUWwtUg?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPMDhIM08yQmdNbkJDS2lzak9KeTdRMkpndnZjNmNvZE9EaE1sNGNoaDhqTGNWT21VVVhLRTZfbGxkdmQ3Y05RMW83Ml80YXVqYmtXR2VXTkZsWXg5eVB0a2QtLUFERTNoVUtwc1BJTjBNT2p1Y1JJbFlKdzRSVWt4MWFYS1ZOYW1WRUprQ2h3?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPdUZDRV81aENnRmpoMFo1cVU0UkZPc21pZEwyM2hpTWlQZlZFWGNMWEl0ZkVkNzBNdXVIUjhfMkNJV1ltOHVsQ0lYNFFTcHlLbFlTMXJIR0FtT3doNGdxUDBTMEEzV080R0RoOWsyYTRBMmNVNWYxdVFrRDdfUWdUY1FZTnB6R3RkNlVldXZEcTlRQk5hQzJQTlNOZmtMV091YmpRYw?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxQYVprRmdFU1M2cmhCUUhmd0RnNFFpX19leG13UjlOOUwwMVUzSTA5NW5wNllZd0JGem1IOFpCeS1yQXlPS3FrTWZ5TWptanlvbkNtQllncjE2ZE9pVkRFX1NVNEFDTUo2NWVDYUw3VGw3TWhKbGVsMThGc1lxSFhiUFRkRS0?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxNREROVnE2dFN6STRQajJhbEsyRjBlRkVzVHd2X2xtR3JTbUtMWTNpYXZDbTVBRi1uZ3RULXIwaGIxTGFEMHRYZkxHclF5ZmdZWXo1MUtMRE03eGpQdUhDX19sN0hFRjR6cmdtblF5MzNuZ2NLcnVxRkVrZDA4VWk4T2Z2bVNhYmFBZEZKWGxBUzBKaFN6V1FpRkFBdGQzZ0FhTlZRYlBaVXBIazAy?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPakhON3hhTlhKQ2Zqdkp6djZHZDNnWklCV1lZRmdiMzBfM2VzbFNza2swWFJnS01zUTR0dFYwZkc3VE1FZk9GdVdvc1Judnp3RU9NYjhYcTRlYVNyeGFhNkJSX3RaQjNsd0dNYnMtVEpfWkNSbld2a253Zkc4Y2lQeXZORXlhVlpiT2h0Q2NnSzFISEVadXc?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPb0lURlNVYTFJWUJFR1VKbnJGTzdTTGstMXJNVjhudzNZc1NKQ25uVUY2TTBjZm1Hc2x4d2paYl95WXVqMXJuQkoweHVOVEhrdjlkUk1RcktucjVMb2lqc2JMTkk1c19VY1NVaHNMcjRFWVV1VVpfeTNkaS16amVpcno3ZnhLbmZnUk81bW1tNGlMV3hHcDZNRjd3dw?oc=5
- https://news.google.com/rss/articles/CBMi_gFBVV95cUxPUTVoOHM3cGRfOTVDVENWV3cza09ETURab0FjUEhxVm0zMUVjU0txVWJodFktb2czT21aS29KUThnMHRzN1d5YUE3VFV0NDU5LXYxclVGTEtydzhGZEhZdVhQZ2hPYUsxM3p4ZE83SU56VTM4N1BaQzUzRG9HbGZnRzVURThXVUJsYUpoWmdhdlctVmNUZkRjQThyNTY3aS1lVTVJdm1QMTVfQ0xTY1Jrd3ZleW10c1AwYndnYjVkNm5qRHRCZDM1SThnbEx4YVcyNUY4RzBfNTg5QjZVcXJ1VmxXcUw0TWYtbG0zTUxTZlZvM1dabnMyN2NoYnd3QQ?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxQV0VRS3liSWhhR3VJaTJodjUtTnFhcGxETHg3b1k5Y3RIMnFzdWdtZy1kaC1WcDdMZHFtWllOOEx3UUdRd2tDdWV6S3B2SFR2d3hadmtmTFcyRk12NXBOMEVBVUU4NThhZXpxOFl6RmZlekJqVUFjM1lySjhCUktROWpxeGhVdXcz?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxOd1k1c3VxRVFQdU5QYVlGa01hM0Y2V0xDRkd1QUhrQy12eUhPR0hJYjNpaFViNUFiZ3p1ZXVUbEpydDRMdld6VlFaRWpJYVU0SFlObm54dGU5bk5WSHF6SmJqa20yX19QYzdFZXRTQ2htTUZ3VGRxTE94X3ZTQXY0czJmLTI3Q1BkdFFWU25pR05Yc2lCZFl6eWhCRHMzT3hEeEpNSDJYX01ILTVEdklkdjZJdWtnQQ?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPNDVmcHh4WlRMQVZydHJ2QnRCM0E3NF9aTGd1OTRVM016LWxQU2JSLUQ0Q3NKbHVaSmRfZXVYOEhac1hkSGJHSG43elF6SEtOXy1PYW5sWk9VbUV1MWNkVU1SZ3RlM25VbUFiVUxNM0tFdTh3NEtZUnExaUd5REJEQUdyVXZEMVhNcEdiMlp5OERHUnFRVGpxYXBDYVN3NjJtcG91WUxfOVZzQnpaMzQyb1JBRTRIQ2VtUFlWYkNuSnBmdw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNR0xMVWVZZjAtdzlUbkdZdlAwSGpTM1dpd2VibzlxR0xoeVpjVlZuWVBXSFQ5dGhKRHV5TnlYLXdqdXBNZWp4VmJ3a0tBMnhRazF0WkU1Q1ZYeElwU0JFVE5zWVF6d0Z3eEJDQUwzOEczNEhDUmlCT2dxSkE3UEE1NHUyTHhoSDVlM3JmZUMzM2Fsc2g1TlZEMjVn?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPM1BFc09DcGY0QXFlMnQ5X0ZZSllHTnJDUlNlVFhwTFc4N2VSUnJqcE9jVEJ2d1E3SjFXckRRYUhkejQzQ09sNXllMnd6LUl6OFMySVB5VVVxNjVCOGRGVVBka1ZJNEM0UjZvanBBbFBIMjRKQUtKaVlpQmV6Vzg1V0hOaVRMYWpRanI2dzRMWkM0eWc?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxOVmJlNVhuWUpYV2UxaTFWSmloYWFvZmhPcng5LXlseGVKdS1OSDU3Qmh6ajI4ckdUZzJuMGd6cWZIOUZqWlUxMmRXeW1UWFBLRmJ0NVRWaENrcDNDUl9iTmhIR0JwR2IxTFlqbGZPbnZDTUVXS0FUX0c5RFkwbE5Vb0w2UVRQTUJHN0E?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQbk1FYjZrZWdKS1RSLWxLQVdSYVR2VEFKMWpZUlpmMDlkMEZDUVRYMDQ3SmRmbGZ2TWdvUFN3RnI0TEdGMlVVR2FfbTZleXhwZThOZHdmd3N5QnlQWVAyc3paLWEta3dKd3VtTk5CY256dG9taV9IV2xobl8xUHZWQ05ya1RjQktnYkl2eXZIOFljRkJC?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPRk1BdHBUVWlsVVRRS1VQSXVsN2VGN0RtOWdxQ3lvTFhSUENYejRubGVxMkJfOVltcjBZRjBPTF8yNzZaNU1sVmh2UkZ5U2gxdHI2WkdZajZUS0Nva1Y1Ty04ZkhtR292ZG54aVJhalE5cWtScllmLTdJY2dIbFlXNmJsNkphell3alNrZVhEZUIycFgwYjlEQVFfaVdLRVRxOHFGMw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
