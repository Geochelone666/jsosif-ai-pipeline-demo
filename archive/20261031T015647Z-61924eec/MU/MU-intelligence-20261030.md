# MU Intelligence Report

- ticker: **MU**
- Report as_of: **2026-10-30**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/MU/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MU/key-statistics/
- AI analysis snapshot as_of: **2026-10-30**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-31T01:59:19.135851+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 2, 'ai': 17, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261030T021807Z-b9de7146/MU** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **5**; {'directional_claim_without_event_type': 5}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 8 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 54.17%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 884.7400 |
| Return 1D (%) | -5.3015 |
| Return 1W (%) | 0.8193 |
| Return 1M (%) | -16.9213 |
| Return YTD (%) | 210.2159 |
| Return 1Y (%) | 295.4041 |
| Annualized volatility (%) | 81.8529 |
| Beta vs SPY | 3.4146 |
| Max drawdown (%) | -39.0954 |
| Sharpe (rf=0) | 2.0925 |
| Downside deviation (rf=0, %) | 49.4274 |
| Sortino (rf=0) | 3.4653 |
| Historical VaR 95% (1D, %) | 7.0055 |
| Historical ES 95% (1D, %) | 9.5345 |
| Correlation vs SPY | 0.5335 |
| Tracking error vs SPY (%) | 75.8053 |
| P/E (trailing) | 11.90 |
| P/B | 7.23 |
| EV/EBITDA | 8.85 |
| Revenue growth (%) | 379.30 |
| Forward P/E (estimate) | 4.26 |
| Gross margin (%) | 80.72 |
| Operating margin (%) | 80.68 |
| Return on equity (%) | 88.26 |
| Free cash flow yield (%) | 2.91 |
| MA50 | 978.5922 |
| Close vs MA50 (%) | -9.5905 |
| MA200 | 746.6249 |
| Close vs MA200 (%) | 18.4986 |
| RSI (14, Wilder) | 41.9835 |
| MACD (12,26) | -24.9150 |
| MACD signal (9) | -23.8433 |
| MACD histogram | -1.0717 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MU': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 884.7400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -5.3015 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.8193 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -16.9213 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 210.2159 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 295.4041 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 81.8529 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 49.4274 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 3.4653 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.0055 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 9.5345 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5335 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 75.8053 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4146 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -39.0954 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 2.0925 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 4.2576 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 80.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 80.6780 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 88.2600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.9111 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 11.9029 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.9835 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.0717 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -9.5905 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 18.4986 -> Clearly above the moving-average trend level.

## TAILWINDS

### Micron Just Unveiled a New Bonus Plan. What That Means for MU Stock.
- Summary: Micron introduces a new bonus plan, potentially boosting shareholder value.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPSVp0SEVqV2ZKY1BKYXJGZXhZcGZNVzZwdnBrV0NhWGtTaTEwMVNBb0hjZEx4b1VYR1B6UzdJNzdXaE5OZFhSZzhZQlhhWmNSelFxYXRCaG8tTEVHRU9DZE5TcmZDaXdHRzdBTjhlbDhqNGM2d1lQbnZpbVdlb1ExSTlXaDB3UzhXd081UzU1Wkp0OE9YT1pOWFFUZjR3V252TkxBTHI1T3J5aEdzdDcw?oc=5>

### Why Micron Stock Is Up Today
- Summary: Positive market sentiment drives the stock higher today.
- Date: 2026-10-28 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQYTJMOG1zSzlhSmpGWWI2MEp6Z3N5REo2Z1lUbzBjNkN6YzBVOEI3VlNBTkNUODJQaVRnU3Zfb2RvRTROMWQzemhaVXZmX2piQ3NBTGxSNDFfaEt6RmJiNWQxSFpvTkQzQmJQWW1uY0VlbFhZSGFTRTNVdklodWFIb01mazJPTUlmeVg3Sk15aXc?oc=5>

### Micron Technology And 2 High Growth Stocks To Watch
- Summary: Analyst highlights Micron as a high-growth candidate, suggesting bullish outlook.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQbzV4YU5OcU1iY09HVlFneGh3SWE5S1VLQ0xWdE9OZDFYcmpMX2tuUGdKckhlTEs0dTFCbE5OY1EwRjhNdV80VTU2bnJRSmpGQ2M5al9CcXBvMEhaTk1lLWhRM0pxcWtEX1dZQXZ0b1pNRXp5V25zT09UYUFkMThZbV9ZbS1lR1R5N2NpSE41ZjhmbWFiYWRzZTVMcm8?oc=5>

### Micron Stock: Why I'm Buying, Not Panicking (NASDAQ:MU)
- Summary: Investor confidence remains high, driving a positive market reaction.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.92
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxQMk1nQ0FUSXQtejZyZ2tjX2N3S19ManMxSG02bU5tVGowb3BzejFBUllTaVlqMUR6M1A0a3dpUldiRVBRWktfbnR4LVhjOXhldVBDSm1GWlNrU0ZNWnFrNDRtSjUyZHVHa2RBU1dpVFFJcFZTbTQ4UFdWVTVFaTR4dU1WaUJweEs1?oc=5>

### Why Micron Technology Stock Rallied Today
- Summary: Recent positive market activity boosts Micron’s stock price.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQU0NKUDZrYmo5dEcyMllySC1BZFRZTUxPZFp5TzJmOGl5ZTdIaEpXcWJVSWtlNDhuWGFSclN6ZkJ3d29CLUluMWtUcGowaXBadVVBY0tqVS1mUkstcHFsLXI1RWp0RmpOdm5OZzJLSktYZ0tmZ0gwRG1XMFN5ZFdtaGNnenc4TVBsczR3d25fVlFrd3dMdGJjVXlMVFlUV2JqdkE?oc=5>

### SK Hynix Just Delivered Fantastic News for Micron
- Summary: SK Hynix’s announcement benefits Micron’s market perception.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.88
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNV2lvRktXWjlieHRGMlFNNy12X053eHcwNnZqV1NCSFE5Y21WVzh0OVpNSUh1bXloNl9FTGZmRW5Ua1cxR1ExYU9sU3BFNmFCSWRrbDBDbWhZQ3JTVHVNSTNJNk5EeTd0WHZuYldTNExwWXh3akIzcmxTdjVyWEZESFUwSnpkMVpOb2V0WnB2UEhHSEVvNVFr?oc=5>

### Micron Is Trading for Less Than 6 Times Forward Earnings. Here's Why That's a Sign to Buy.
- Summary: Valuation suggests buying opportunity.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQZ2V2MTU0emZlbW9TQ0xyNlI3emk1UXAyN0xMbVVsYzd4bmlMUTRDcmlLNGR2V05xTUVaaHBpWC02Y3VSeDNib3J4SlBlc3diSHAxcjNoYU1XZ0hqZ3I2UWVRcHplQm95TnJMa2k5NVNXUWZZcTRvS254enZteTNjZ1N5ajFNVTNtYmpLQ0c5MG1OTEV6bDE4?oc=5>

### Micron Peer Enthusiasm Entices Me To Buy Again
- Summary: Investor expresses renewed enthusiasm to purchase Micron shares.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNX3NjTVlkYmZmREpLWlZrTkRNTC03RVVaUDRha2trbHNsZkNlU1B6RG1OMExlazJha1l1ZHRFUVRTVFlPRjNRcWF4MndsYXJ3WW0yaVc4WmxSZXZqVHJNSUNqODZKVWxuWUN3ZmtGc1k5TWhMZFJyTmVsTks5ajFFeDNJX0xsdm9DZGJ6Y1dQejVrc2dw?oc=5>

### 52 ETFs Add to Micron (MU) Holdings on Wednesday
- Summary: ETFs increased Micron holdings, indicating positive market movement.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxNdFc3T2dVR1JHTHhWb2JDbmZuREhtWkgxajVWWmExMVFvbWxYTXcyRzhsb25iSjNUVUc0NGRLcVV1bG1yaXc4ell1MXBEVjlQd0IxN1QzLW9ZcUhWbFF6amdLbHZ3T3FyMld4cUZ2bzNLZHBaeGd1QVZqTG1YWlowUGZvaVBGS09UTnZ5MEpNbw?oc=5>

## HEADWINDS

### Micron Technology Inc (MU) Shares Fall 5.3% -- GF Value Says Sti
- Summary: Micron Technology Inc (MU) Shares Fall 5.3% -- GF Value Says Sti
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxPMmkzdG5wQWZ5aVdVY2g5XzdQcXJ6NGo3NmJCUzhaenFscDZtcmplNFkyQi11Y0MzQ0hVZ0xKM0xRMzdrNWpNQ3Z2MDhaVTVvOWlyYmxIQnNYb09BTWdJd1pPbW9xYnhuZjAxTC1IQVBIMGt3UG1XdTJEOEw2ZTZ0X0x0UjMyRm02WVFmSVdFMXUyQ2FzMDAxdWFJaTdyUVhPSHpBeGxpQWc3V0pObWc?oc=5>

### Why Is Micron Stock Falling on Thursday? - Micron Technology (NASDAQ:MU)
- Summary: Micron shares declined on Thursday, reflecting negative market sentiment.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPdUZDRV81aENnRmpoMFo1cVU0UkZPc21pZEwyM2hpTWlQZlZFWGNMWEl0ZkVkNzBNdXVIUjhfMkNJV1ltOHVsQ0lYNFFTcHlLbFlTMXJIR0FtT3doNGdxUDBTMEEzV080R0RoOWsyYTRBMmNVNWYxdVFrRDdfUWdUY1FZTnB6R3RkNlVldXZEcTlRQk5hQzJQTlNOZmtMV091YmpRYw?oc=5>

### Micron Stock Falls as Samsung Earnings Show the High Bar for Memory Stocks.
- Summary: Micron shares fell after Samsung's earnings set a high benchmark for memory stocks.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxQYVprRmdFU1M2cmhCUUhmd0RnNFFpX19leG13UjlOOUwwMVUzSTA5NW5wNllZd0JGem1IOFpCeS1yQXlPS3FrTWZ5TWptanlvbkNtQllncjE2ZE9pVkRFX1NVNEFDTUo2NWVDYUw3VGw3TWhKbGVsMThGc1lxSFhiUFRkRS0?oc=5>

### Learn Why The Bull Case For Micron Stock Could Change Following Memory Shortage Warning
- Summary: Memory shortage warning threatens Micron’s bullish outlook.
- Date: 2026-10-30 | Impact: high | Horizon: short | Confidence: 0.93
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPZUxjeUhlazZTeHFBTjRIblhSdlRzVThHSFNzQ1liVFJ3WDFlSG9KUDdRUC1rS2pfRVRuczNsTlRGeDNrVl9pajBsTHhkMzItSm05SUR6T2hVNUxkUFdaYVJhUWQ5VHlnaGxzWlh1T3RrMjE5ckZlV0F5T0dMaFI4UE51ejhIY3YxaGJjRkh1aWRMVmdSdkE?oc=5>

### Micron Stock Drops Again. Surging Memory Prices Aren’t All Good News.
- Summary: Rising memory prices contribute to a decline in Micron’s stock.
- Date: 2026-10-30 | Impact: high | Horizon: short | Confidence: 0.91
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE1HbWpqcXhhOUVfOWUwMnJIZDd3NTREaG0tQTNDX0N5YnkyaUxMRWxFNWNQS1JKRTc1NTMyVHgzNUN1djAtQ3NtMWs4VWJ3Sk0tSDhNbGg0S3FSMXJGQVdKVC14Nlh1VnVndVBBbFAtVzBxdi04TS1iZGpNU2g1UQ?oc=5>

### Why Micron Stock Dove Today
- Summary: Micron shares fell today.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOZHFrRXNRVkhJazl2RzN5dDhTbVgwa2hieW1GRFpZdjAzT180TldxWl9feXlIbFNuZk1sVTN5cG1fdEQ3dGNadmpTQ3ZDQkh5eGNhblE5a3NvSGVYcFU0ankzRnBiNW5KWGVERmlPcDc2T3R0aURmWlIyRzJNWXlXWTdkNEpoUWo4SjZkMW44QktyWU9ZY2NJ?oc=5>

### Sandisk Sinks 9% Despite Earnings Beat, Raised Guidance and 8-for-1 Split; Western Digital Tumbles 8%, Seagate Slides 7%, Micron Falls 6%
- Summary: Micron shares dropped 6%.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMigwJBVV95cUxPRHRncUhXeEE4ajg0RnF2WVhka1ZpVFdYM1BhOGFjRlRaMndMQmh6VGVCekx0TTJzQmZKUVJ4d0JsSm02RjM4MjF3b2p2blY0ZlZ6R0dVbE5NWTVuOHBqTTctY0czUVdYbnZHanNTYXR2ODlwNkd2S1RKaENyejg5REpWQUdzOHRaTFcwUVYxLV8tUlRmcHVCNTlWNk5ld0Q1R1lHV1RpZ0xDLTRNQ2x3S3VkdEVZVXpieEc4TEg4UkFsdG1IZnVTeFMxV1c5Sk00U3ljeWN3aG56N1J4Y25ZUHRUQnUxS0dzZnc0NnVINlowNDcyMzhuNmFjaUM2ZDlDQzdR?oc=5>

## CATALYSTS

### Micron Technology Stock: Is Now the Time for Investors to Take Profits or Buy More?
- Summary: Micron Technology Stock: Is Now the Time for Investors to Take Profits or Buy More?
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPNDVmcHh4WlRMQVZydHJ2QnRCM0E3NF9aTGd1OTRVM016LWxQU2JSLUQ0Q3NKbHVaSmRfZXVYOEhac1hkSGJHSG43elF6SEtOXy1PYW5sWk9VbUV1MWNkVU1SZ3RlM25VbUFiVUxNM0tFdTh3NEtZUnExaUd5REJEQUdyVXZEMVhNcEdiMlp5OERHUnFRVGpxYXBDYVN3NjJtcG91WUxfOVZzQnpaMzQyb1JBRTRIQ2VtUFlWYkNuSnBmdw?oc=5>

### Here's Why Micron (MU) Fell More Than Broader Market
- Summary: Micron’s share price dropped more than the broader market due to concerns over demand and earnings expectations.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPM1BFc09DcGY0QXFlMnQ5X0ZZSllHTnJDUlNlVFhwTFc4N2VSUnJqcE9jVEJ2d1E3SjFXckRRYUhkejQzQ09sNXllMnd6LUl6OFMySVB5VVVxNjVCOGRGVVBka1ZJNEM0UjZvanBBbFBIMjRKQUtKaVlpQmV6Vzg1V0hOaVRMYWpRanI2dzRMWkM0eWc?oc=5>

### What Could Robot Memory Demand Mean For Micron Technology (MU) Stock?
- Summary: Increased robot memory demand could boost Micron’s revenue prospects.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNR0xMVWVZZjAtdzlUbkdZdlAwSGpTM1dpd2VibzlxR0xoeVpjVlZuWVBXSFQ5dGhKRHV5TnlYLXdqdXBNZWp4VmJ3a0tBMnhRazF0WkU1Q1ZYeElwU0JFVE5zWVF6d0Z3eEJDQUwzOEczNEhDUmlCT2dxSkE3UEE1NHUyTHhoSDVlM3JmZUMzM2Fsc2g1TlZEMjVn?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MU** | **11.90** | **7.23** | **8.85** | **379.30** | **1,001,015,410,688.00 USD** | **295.40** |
| WDC | 12.88 | 14.65 | 21.64 | 55.50 | 137,043,484,672.00 USD | 165.54 |
| STX | 33.80 | 42.93 | 25.45 | 61.00 | 148,253,409,280.00 USD | 141.63 |
| NXPI | 20.43 | 5.41 | 13.53 | 19.30 | 65,435,471,872.00 USD | 28.01 |

Peers fetched as_of: 2026-10-30; MU reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-30
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-30

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
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQYTJMOG1zSzlhSmpGWWI2MEp6Z3N5REo2Z1lUbzBjNkN6YzBVOEI3VlNBTkNUODJQaVRnU3Zfb2RvRTROMWQzemhaVXZmX2piQ3NBTGxSNDFfaEt6RmJiNWQxSFpvTkQzQmJQWW1uY0VlbFhZSGFTRTNVdklodWFIb01mazJPTUlmeVg3Sk15aXc?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQbzV4YU5OcU1iY09HVlFneGh3SWE5S1VLQ0xWdE9OZDFYcmpMX2tuUGdKckhlTEs0dTFCbE5OY1EwRjhNdV80VTU2bnJRSmpGQ2M5al9CcXBvMEhaTk1lLWhRM0pxcWtEX1dZQXZ0b1pNRXp5V25zT09UYUFkMThZbV9ZbS1lR1R5N2NpSE41ZjhmbWFiYWRzZTVMcm8?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxQMk1nQ0FUSXQtejZyZ2tjX2N3S19ManMxSG02bU5tVGowb3BzejFBUllTaVlqMUR6M1A0a3dpUldiRVBRWktfbnR4LVhjOXhldVBDSm1GWlNrU0ZNWnFrNDRtSjUyZHVHa2RBU1dpVFFJcFZTbTQ4UFdWVTVFaTR4dU1WaUJweEs1?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQU0NKUDZrYmo5dEcyMllySC1BZFRZTUxPZFp5TzJmOGl5ZTdIaEpXcWJVSWtlNDhuWGFSclN6ZkJ3d29CLUluMWtUcGowaXBadVVBY0tqVS1mUkstcHFsLXI1RWp0RmpOdm5OZzJLSktYZ0tmZ0gwRG1XMFN5ZFdtaGNnenc4TVBsczR3d25fVlFrd3dMdGJjVXlMVFlUV2JqdkE?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNbzJCRVVpMElSTVRlQ2ZoTmE2RUtEVWFYei15Ykg5TUhobGVhaGZabGtUZzJ1VFM0WHFCWGdETHQ0dVFnQ3N5SDFyRjQ4c250OG43ei14YUs4bjB5VUVRWmtVTWtTN0J2TVVHVzZQcG40X1hSbzJubnVYUGJHRE5ueXUzRDVsQUV3M0RWdQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNV2lvRktXWjlieHRGMlFNNy12X053eHcwNnZqV1NCSFE5Y21WVzh0OVpNSUh1bXloNl9FTGZmRW5Ua1cxR1ExYU9sU3BFNmFCSWRrbDBDbWhZQ3JTVHVNSTNJNk5EeTd0WHZuYldTNExwWXh3akIzcmxTdjVyWEZESFUwSnpkMVpOb2V0WnB2UEhHSEVvNVFr?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQZ2V2MTU0emZlbW9TQ0xyNlI3emk1UXAyN0xMbVVsYzd4bmlMUTRDcmlLNGR2V05xTUVaaHBpWC02Y3VSeDNib3J4SlBlc3diSHAxcjNoYU1XZ0hqZ3I2UWVRcHplQm95TnJMa2k5NVNXUWZZcTRvS254enZteTNjZ1N5ajFNVTNtYmpLQ0c5MG1OTEV6bDE4?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNX3NjTVlkYmZmREpLWlZrTkRNTC03RVVaUDRha2trbHNsZkNlU1B6RG1OMExlazJha1l1ZHRFUVRTVFlPRjNRcWF4MndsYXJ3WW0yaVc4WmxSZXZqVHJNSUNqODZKVWxuWUN3ZmtGc1k5TWhMZFJyTmVsTks5ajFFeDNJX0xsdm9DZGJ6Y1dQejVrc2dw?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNdFc3T2dVR1JHTHhWb2JDbmZuREhtWkgxajVWWmExMVFvbWxYTXcyRzhsb25iSjNUVUc0NGRLcVV1bG1yaXc4ell1MXBEVjlQd0IxN1QzLW9ZcUhWbFF6amdLbHZ3T3FyMld4cUZ2bzNLZHBaeGd1QVZqTG1YWlowUGZvaVBGS09UTnZ5MEpNbw?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPMmkzdG5wQWZ5aVdVY2g5XzdQcXJ6NGo3NmJCUzhaenFscDZtcmplNFkyQi11Y0MzQ0hVZ0xKM0xRMzdrNWpNQ3Z2MDhaVTVvOWlyYmxIQnNYb09BTWdJd1pPbW9xYnhuZjAxTC1IQVBIMGt3UG1XdTJEOEw2ZTZ0X0x0UjMyRm02WVFmSVdFMXUyQ2FzMDAxdWFJaTdyUVhPSHpBeGxpQWc3V0pObWc?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPdUZDRV81aENnRmpoMFo1cVU0UkZPc21pZEwyM2hpTWlQZlZFWGNMWEl0ZkVkNzBNdXVIUjhfMkNJV1ltOHVsQ0lYNFFTcHlLbFlTMXJIR0FtT3doNGdxUDBTMEEzV080R0RoOWsyYTRBMmNVNWYxdVFrRDdfUWdUY1FZTnB6R3RkNlVldXZEcTlRQk5hQzJQTlNOZmtMV091YmpRYw?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxQYVprRmdFU1M2cmhCUUhmd0RnNFFpX19leG13UjlOOUwwMVUzSTA5NW5wNllZd0JGem1IOFpCeS1yQXlPS3FrTWZ5TWptanlvbkNtQllncjE2ZE9pVkRFX1NVNEFDTUo2NWVDYUw3VGw3TWhKbGVsMThGc1lxSFhiUFRkRS0?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPZUxjeUhlazZTeHFBTjRIblhSdlRzVThHSFNzQ1liVFJ3WDFlSG9KUDdRUC1rS2pfRVRuczNsTlRGeDNrVl9pajBsTHhkMzItSm05SUR6T2hVNUxkUFdaYVJhUWQ5VHlnaGxzWlh1T3RrMjE5ckZlV0F5T0dMaFI4UE51ejhIY3YxaGJjRkh1aWRMVmdSdkE?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE1HbWpqcXhhOUVfOWUwMnJIZDd3NTREaG0tQTNDX0N5YnkyaUxMRWxFNWNQS1JKRTc1NTMyVHgzNUN1djAtQ3NtMWs4VWJ3Sk0tSDhNbGg0S3FSMXJGQVdKVC14Nlh1VnVndVBBbFAtVzBxdi04TS1iZGpNU2g1UQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOZHFrRXNRVkhJazl2RzN5dDhTbVgwa2hieW1GRFpZdjAzT180TldxWl9feXlIbFNuZk1sVTN5cG1fdEQ3dGNadmpTQ3ZDQkh5eGNhblE5a3NvSGVYcFU0ankzRnBiNW5KWGVERmlPcDc2T3R0aURmWlIyRzJNWXlXWTdkNEpoUWo4SjZkMW44QktyWU9ZY2NJ?oc=5
- https://news.google.com/rss/articles/CBMigwJBVV95cUxPRHRncUhXeEE4ajg0RnF2WVhka1ZpVFdYM1BhOGFjRlRaMndMQmh6VGVCekx0TTJzQmZKUVJ4d0JsSm02RjM4MjF3b2p2blY0ZlZ6R0dVbE5NWTVuOHBqTTctY0czUVdYbnZHanNTYXR2ODlwNkd2S1RKaENyejg5REpWQUdzOHRaTFcwUVYxLV8tUlRmcHVCNTlWNk5ld0Q1R1lHV1RpZ0xDLTRNQ2x3S3VkdEVZVXpieEc4TEg4UkFsdG1IZnVTeFMxV1c5Sk00U3ljeWN3aG56N1J4Y25ZUHRUQnUxS0dzZnc0NnVINlowNDcyMzhuNmFjaUM2ZDlDQzdR?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPNDVmcHh4WlRMQVZydHJ2QnRCM0E3NF9aTGd1OTRVM016LWxQU2JSLUQ0Q3NKbHVaSmRfZXVYOEhac1hkSGJHSG43elF6SEtOXy1PYW5sWk9VbUV1MWNkVU1SZ3RlM25VbUFiVUxNM0tFdTh3NEtZUnExaUd5REJEQUdyVXZEMVhNcEdiMlp5OERHUnFRVGpxYXBDYVN3NjJtcG91WUxfOVZzQnpaMzQyb1JBRTRIQ2VtUFlWYkNuSnBmdw?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPM1BFc09DcGY0QXFlMnQ5X0ZZSllHTnJDUlNlVFhwTFc4N2VSUnJqcE9jVEJ2d1E3SjFXckRRYUhkejQzQ09sNXllMnd6LUl6OFMySVB5VVVxNjVCOGRGVVBka1ZJNEM0UjZvanBBbFBIMjRKQUtKaVlpQmV6Vzg1V0hOaVRMYWpRanI2dzRMWkM0eWc?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNR0xMVWVZZjAtdzlUbkdZdlAwSGpTM1dpd2VibzlxR0xoeVpjVlZuWVBXSFQ5dGhKRHV5TnlYLXdqdXBNZWp4VmJ3a0tBMnhRazF0WkU1Q1ZYeElwU0JFVE5zWVF6d0Z3eEJDQUwzOEczNEhDUmlCT2dxSkE3UEE1NHUyTHhoSDVlM3JmZUMzM2Fsc2g1TlZEMjVn?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
