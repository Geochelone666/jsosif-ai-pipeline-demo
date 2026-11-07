# MU Intelligence Report

- ticker: **MU**
- Report as_of: **2026-11-06**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/MU/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MU/key-statistics/
- AI analysis snapshot as_of: **2026-11-06**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-07T04:52:23.242269+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 0, 'ai': 18, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **14** exact headline/source/date matches; prior report **20261106T045829Z-1db1e5a7/MU** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 9 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 28.0%; oldest publication 2026-11-04

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 690.0000 |
| Return 1D (%) | 5.1204 |
| Return 1W (%) | -22.0110 |
| Return 1M (%) | -33.9963 |
| Return YTD (%) | 141.9343 |
| Return 1Y (%) | 189.8433 |
| Annualized volatility (%) | 83.6953 |
| Beta vs SPY | 3.3751 |
| Max drawdown (%) | -45.8952 |
| Sharpe (rf=0) | 1.6927 |
| Downside deviation (rf=0, %) | 52.7372 |
| Sortino (rf=0) | 2.6863 |
| Historical VaR 95% (1D, %) | 7.0090 |
| Historical ES 95% (1D, %) | 10.3312 |
| Correlation vs SPY | 0.5464 |
| Tracking error vs SPY (%) | 77.1307 |
| P/E (trailing) | 9.28 |
| P/B | 5.64 |
| EV/EBITDA | 6.82 |
| Revenue growth (%) | 379.30 |
| Forward P/E (estimate) | 3.32 |
| Gross margin (%) | 80.72 |
| Operating margin (%) | 80.68 |
| Return on equity (%) | 88.26 |
| Free cash flow yield (%) | 3.73 |
| MA50 | 961.5337 |
| Close vs MA50 (%) | -28.2396 |
| MA200 | 756.5279 |
| Close vs MA200 (%) | -8.7938 |
| RSI (14, Wilder) | 31.2702 |
| MACD (12,26) | -63.1884 |
| MACD signal (9) | -39.9706 |
| MACD histogram | -23.2178 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MU': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 690.0000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 5.1204 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -22.0110 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -33.9963 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 141.9343 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 189.8433 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 83.6953 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 52.7372 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.6863 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.0090 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 10.3312 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5464 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 77.1307 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.3751 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -45.8952 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.6927 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 3.3211 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 80.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 80.6780 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 88.2600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.7327 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 9.2829 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 31.2702 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -23.2178 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -28.2396 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -8.7938 -> Clearly below the moving-average trend level.

## TAILWINDS

### Micron: Buy The Panic Before The Market Wakes Up (NASDAQ:MU)
- Summary: Analyst urges buying before market rebound.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxQU2REbjB6bHZPTGpVRTlQNW5pclVCdjRBU09tYzdhYzUtaUVNWDRIbnBwenB2TEV6RTR3MFN0WUxFdkRIRk9yaW9vanFUMXhRZUxRQUZvdmFiNUk5eXlQRUtuSjEybldsMXFZRVJoT1VxeWVtMnI1WG92RUgwWmZ4UWdfaFBuek5YVmlFVzBhSGNaZw?oc=5>

### Micron's Selloff Is A Once-In-A-Decade Opportunity (NASDAQ:MU)
- Summary: Selloff seen as a rare buying opportunity for investors.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxONk5hLVZLVGVod0hrUmtVSlN5UXN2NWFXMmQ2NmJYNWVYc3NDem1aRnYxTmFtLTlKUFpDcW1jdTRLSDlNVlViVjVCQjhPU19wQTFFVDREUmlQOHE1cDF1TVpoOVBHRHdaX0tkY20wRi1UWTk2OWhQSFBqcGltOHpYUzYyTG9zQWYtemlwclpyWHRZU1k?oc=5>

### Sandisk Is Splitting Its Stock 8-for-1. Is Micron Technology Next?
- Summary: Speculation that Micron may split its stock following SanDisk's 8-for-1 split.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPc2w1eVBtTDFQa0VKSDhRRGhsM09TalNHa0lnVWJ0alJjTzIwQ2RpR2ptVUVoeGc2aFFvTWM5UXBmLVdqWmQ0S1BoT2xkYVJVOG5DWnFoNjZsVUdGenZ6OEVUSFNtajRiYjlQYU05M1VYRFA2X1Nna3VRTGxiSnlqOVItbXdvdlBncjNGM3NlcFMxMmhTSC1kcDR3Y0xPYV9jX21SY1A4cmVnRmc?oc=5>

### Micron Technology Stock Is Surging Friday: What's Going On?
- Summary: Micron shares rise, possibly due to stock split rumors.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxQajV3dEFsT2JWRVlVa25XTVk3M1ZqTm5uaGM3aTRib3RyWGVLMEkyWmJTbXVfY01iSUZreFlPVkswbV9mYWowVUJxVjNiVkpubkxnZVR3MzFEOVdObjFWRVp3VGhhN2VYdFlPbmRQb0VLVFVpdEY3SUllT0gtMmFZdHltc1FBSmtoTEhyUUpEellOdjhVOFZXdnN4bTA1RDBNMFk0Z2xxOGRwalNzSEE?oc=5>

### A 60-Year-Old Who Bought 1,000 Micron Shares at $192 Just Lost $138,840. He's Still Up $464,000. Here's What Happens Next.
- Summary: Investor's gains amid Micron stock movement, likely linked to split speculation.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxOUFpWSFpNS21wZW5QMWRYaW5xdko2SWJEd1VXSy0yV2RSc2pPSGFQdEVOYURsVHlkLVRMUWVtSlZMUTJRdGNwQmxXNS13QVBvQ2VLVkFITUhPUTNvcTNpX3pkOWQ2M2plTEFHT2ZuX0k1c0UxSXVOd1JNbjJFeEMwSWNaVThXYkR5aG9DcDZZSDBlSG5kUmNiMFQ4TnZ6YmpqZ0hTd0JZUGtJNnZwOVV3VWpFNTNfdHlLX0M1M0Y5TmpIY28zME5XMEhqZFc3ZVRxOS1WYjd4RlVwSmhQSjJ5M01BWk5wWkVJQUV3?oc=5>

### Micron: When A 3.8x Forward 2028 P/E Is Too Expensive (NASDAQ:MU)
- Summary: Analysis of Micron's valuation, referencing potential stock split impact.
- Date: 2026-11-05 | Impact: low | Horizon: medium | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPMlJkSVpoVjVBZ2wydGkzTWRTbThIa2tuTUNScjFOdXdPaUpoVll1elVmZGtCTUlVVnJkdTFNaXdaTGlEUmZ0blJuakRNcE9XQzNzbnRnNWI4S1V5bzBDUUFNb043V2NlNjFwTG0zV1JIanZqUjhqVXlfWDdGUHJPV0xqZVZxS0FqT0RGWUN6U3JoS2oxYlN0Mw?oc=5>

### Stock-Split Watch: Is Micron (MU) Next?
- Summary: Monitoring potential Micron stock split following industry trends.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxNZEtzX2U2NE9kV2RKT2tybFU1MUpvTDZ6d0dqakExR2dUY0VMMTBvbWxnVlp6WEtZN1Z2ZzJzQmpLRk1ZUzJlT0dpVldNcW5WMTNUNDhKZURCc09uWWVDclIyWktJbmN4NUJ6Rk9ZVU8wdjc5S294NWdxME5UdHRqLXJKM0Y?oc=5>

### Micron Technology Shares Jump 4.11% After Hours Following Sharp Selloff - Micron Technology (NASDAQ:MU)
- Summary: Micron shares rise 4.11% after hours following a sharp selloff.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQLUczZzlCdmVZa0dQYm5uVE8yTFgtaUpMR3NsTXRPVzBpTy1taUNKbV9MZ3NHZi1nOHpkdC10c245dkJUNUFwOHMwQ2FkMG1XXzBvY3ltRzlucHpFN3dNX3F3OE1ZeEJoNHBRX25WNHg1QXRWYmVfS21qdHk2amlKU2lJbHoyZTIwa29UVHFvUDEwTUY5X1kzY2VqLXBLa1A4T3Z3eVlIbDJTZkpC?oc=5>

### SanDisk Surges 10%, Micron and Western Digital Jump 8% as Memory and Storage Stocks Rebound From AI Sell-Off
- Summary: Micron shares jump 8% as memory stocks rebound from AI sell‑off.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxPZS1YbHc4X3E2bTJFVVlNa2MxelRtN28wVVNqR0wzRXBUMXJaQTJTN3E5WTh2M3BHZllVb01pc18tOWhjbGowQlpwVmZCMWtNV3dxdDJrZE41akxCdkpNY1c4aGtpdE5MekswV21LRjV6UjNockY3Qk5hVUQ0NWVFTlB5WVUyOEplZjlCdVlQTUdZTWdJTVhZQ3VmQl92YmtzeGkwQ1JJYks0UzNUdXI4R2ZVNE1aTXV1Mm5jWTMtdjJmVmNwYkp6RGFQbUdTM1UyZW5wbzRaRmc0WEN5eW1vRXpacw?oc=5>

## HEADWINDS

### Micron Stock Gets Crushed by AI Selloff. Don’t Ignore the $200 Billion Silver Lining.
- Summary: AI selloff hits Micron stock.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMic0FVX3lxTE15TVY0YUJZQXZIYUpKcWRPci1VWGZlbFRXT3pmNkJUcF9MbVFtUWdhdnNnRDRGU1ktWXZ5SExlRjViYkpZSGtrTEtadE1TdDJjWk51eDV5eE1lMi03bTFxb0YxdFIteEU5OWFyZ0s4cnlrTTA?oc=5>

### Why Micron Stock Is Falling Today
- Summary: Stock decline attributed to recent factors.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPU0RwVjVWeDQ2RENzVzNYZXRJT0E4ZWtkWE5VcXdnbm5Fb0VpTksyVG92UXFNNWpybVBoMFJ3WWtZZGQ4ZGoxM2YyRzkxLWI0SnNnQ3UtbnRCQmpsQ0V6WkpQdE1PNDRnWFhEVUZTbndmNktZeVlwdW03bzJLand6Ri1STm9VTHkzU083bHZSM2VJYnFWUWJJeW9EYw?oc=5>

### Micron Stock Plunges As Memory-Chip Shortages Cause Ripple Effects
- Summary: Memory‑chip shortages trigger plunge.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxPX0lGaFVmall4RXFtb05Ud0FrYk4wdVVPZ1pMaURhckZhZE41VktXclRSV2FNZW1uLVFfQUNITTFIZ25WNkFSX3ZzQzJMOFBEUUE1YV9Qc3A2Q0E4SGwzZkZ5LV9BcnRHdzQwbF9SSUlscUxlQ1RmVGpiRE56VXJxSVpUUV9Ud3BzVjcxUTFR?oc=5>

### Micron Stock Hits 3-Month Low. Is MU a Buy at These Levels?
- Summary: Stock at 3‑month low, raising concerns.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxPVExmbVgwRmdpZEUxb0J1U2tqcUtPdHVxUUhwZ3NUWXkwYWJIQkJCeEV5LW1ETHJub0RQcGFIeWdhVFViNU9rdVJBNk9TWWhzUFF5OFg1VFBXU2ticzFqR0hVSzFaUl9ZazIwX0F1akpVVDI5V1hwNTJwVlh6MkczSFhn?oc=5>

### Micron (MU) Stock Sinks As Market Gains: Here's Why
- Summary: Micron shares decline amid market gains.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQc3NNb1RNWmpjTFRUWWdBOC1mampaLWQ1YWFoYW9aRlNCcndUWXBWSkJEb2RnWWFPMVhkTS1mSG5sNmFNS0RmaEJ1aXFPVnBhTzdHc1hyUDA5enpSeFgzUjBqRnBhSURweGtoNHRNNTA5MWpabi1MMHpxTE91MFdJSzRDUGdmVkNCbERuV21fYVZMdUFyS2FHcg?oc=5>

### Micron Technology plunges 17% amid chip selloff, Taiwan plant halt (MU:NASDAQ)
- Summary: 17% drop due to chip selloff and Taiwan plant halt.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNRDhzVlRiSVpJay1TNlJ4c0ZnUzRBUjZ4TFJZaEVFbjVIZmJVbzVzR0RWUGFjUS1rTXdmWjdlRjlSd2VpVFN1WVBDeWd1Z2FXYlNqbkdxbFkyM3NGbTNROG90MV9HR0Q4aFUxeWhyWllCdGYwV2FSNEtISnpaZWpBUTZCZUx4OE9SUmRaRHBsdVdYLUZRZy1jZ1NTZEUyWEZlX3c1Uw?oc=5>

### Why Micron Stock Keeps Going Down
- Summary: Continued decline signals ongoing pressure.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxQbjBleVA1OXJDbThsRkhnRUZzWTZDYUFtS3VCTUllTDlWSWpneURNVkd2M0dJa2dxaXZSclRWU1JIVEk5aE5SdmY0SlNlc1U5Q3VnOGdRUkZjNHBlWnhqTVgwMzZ3Z3BIRkowMURSTlZLSFpHWHEyNjMxdFdGbWFQMkhB?oc=5>

## CATALYSTS

### What Wall Street is Missing About Micron’s (MU) Ultra-Low Earnings Multiple
- Summary: Earnings multiple lower than expected, analysts may overlook.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOZm5OcG9fOWsxbGR6RGlCZXVQRFdDNFZYb1dWUVZqNUw3UUdKcWd6Rk1XVkFZVFZTc0RKMUZuRTVIZmxZSUhFTVZZYm81al9uT3B4QXQzUzRKR3FjdXVhOW55WF94enVWdWpha3RJUHJPZ0JGUEtvTjNxbmtmNTQzOEdNbldicGtjNXU1TGd4dzJqeld2bjZEalV3?oc=5>

### Micron Technology (MU) is Holding Firm on High-Bandwidth Memory (HBM)
- Summary: Micron maintains its commitment to high‑bandwidth memory development.
- Date: 2026-11-04 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPbmE2VkVuZlFSb045UDJrTXdTNE1QMVlzblhoM2hqUVdqU3pzRGQwZzFWeS1wRHVaNktxN01QYXFwUHYxOGtWY0s2M2k4MWdXem11YThKc1BJTVgxWTBwcVFmVk1LTzJ4UzJrTUZic01VekRoNk5hUEs0MUU2b2U2b1EtRlBwZ1pWdFlzempvWHkzdVNTMzNZOW9ueE9TWkk?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MU** | **9.28** | **5.64** | **6.82** | **379.30** | **780,682,002,432.00 USD** | **189.84** |
| WDC | 9.28 | 10.55 | 15.58 | 55.50 | 98,738,987,008.00 USD | 61.54 |
| STX | 24.47 | 30.67 | 18.28 | 61.00 | 105,825,370,112.00 USD | 66.52 |
| NXPI | 19.54 | 5.18 | 12.99 | 19.30 | 62,582,235,136.00 USD | 22.39 |

Peers fetched as_of: 2026-11-06; MU reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-30
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-06

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMikgFBVV95cUxQU2REbjB6bHZPTGpVRTlQNW5pclVCdjRBU09tYzdhYzUtaUVNWDRIbnBwenB2TEV6RTR3MFN0WUxFdkRIRk9yaW9vanFUMXhRZUxRQUZvdmFiNUk5eXlQRUtuSjEybldsMXFZRVJoT1VxeWVtMnI1WG92RUgwWmZ4UWdfaFBuek5YVmlFVzBhSGNaZw?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxONk5hLVZLVGVod0hrUmtVSlN5UXN2NWFXMmQ2NmJYNWVYc3NDem1aRnYxTmFtLTlKUFpDcW1jdTRLSDlNVlViVjVCQjhPU19wQTFFVDREUmlQOHE1cDF1TVpoOVBHRHdaX0tkY20wRi1UWTk2OWhQSFBqcGltOHpYUzYyTG9zQWYtemlwclpyWHRZU1k?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPc2w1eVBtTDFQa0VKSDhRRGhsM09TalNHa0lnVWJ0alJjTzIwQ2RpR2ptVUVoeGc2aFFvTWM5UXBmLVdqWmQ0S1BoT2xkYVJVOG5DWnFoNjZsVUdGenZ6OEVUSFNtajRiYjlQYU05M1VYRFA2X1Nna3VRTGxiSnlqOVItbXdvdlBncjNGM3NlcFMxMmhTSC1kcDR3Y0xPYV9jX21SY1A4cmVnRmc?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxQajV3dEFsT2JWRVlVa25XTVk3M1ZqTm5uaGM3aTRib3RyWGVLMEkyWmJTbXVfY01iSUZreFlPVkswbV9mYWowVUJxVjNiVkpubkxnZVR3MzFEOVdObjFWRVp3VGhhN2VYdFlPbmRQb0VLVFVpdEY3SUllT0gtMmFZdHltc1FBSmtoTEhyUUpEellOdjhVOFZXdnN4bTA1RDBNMFk0Z2xxOGRwalNzSEE?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxOUFpWSFpNS21wZW5QMWRYaW5xdko2SWJEd1VXSy0yV2RSc2pPSGFQdEVOYURsVHlkLVRMUWVtSlZMUTJRdGNwQmxXNS13QVBvQ2VLVkFITUhPUTNvcTNpX3pkOWQ2M2plTEFHT2ZuX0k1c0UxSXVOd1JNbjJFeEMwSWNaVThXYkR5aG9DcDZZSDBlSG5kUmNiMFQ4TnZ6YmpqZ0hTd0JZUGtJNnZwOVV3VWpFNTNfdHlLX0M1M0Y5TmpIY28zME5XMEhqZFc3ZVRxOS1WYjd4RlVwSmhQSjJ5M01BWk5wWkVJQUV3?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPMlJkSVpoVjVBZ2wydGkzTWRTbThIa2tuTUNScjFOdXdPaUpoVll1elVmZGtCTUlVVnJkdTFNaXdaTGlEUmZ0blJuakRNcE9XQzNzbnRnNWI4S1V5bzBDUUFNb043V2NlNjFwTG0zV1JIanZqUjhqVXlfWDdGUHJPV0xqZVZxS0FqT0RGWUN6U3JoS2oxYlN0Mw?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxNZEtzX2U2NE9kV2RKT2tybFU1MUpvTDZ6d0dqakExR2dUY0VMMTBvbWxnVlp6WEtZN1Z2ZzJzQmpLRk1ZUzJlT0dpVldNcW5WMTNUNDhKZURCc09uWWVDclIyWktJbmN4NUJ6Rk9ZVU8wdjc5S294NWdxME5UdHRqLXJKM0Y?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQLUczZzlCdmVZa0dQYm5uVE8yTFgtaUpMR3NsTXRPVzBpTy1taUNKbV9MZ3NHZi1nOHpkdC10c245dkJUNUFwOHMwQ2FkMG1XXzBvY3ltRzlucHpFN3dNX3F3OE1ZeEJoNHBRX25WNHg1QXRWYmVfS21qdHk2amlKU2lJbHoyZTIwa29UVHFvUDEwTUY5X1kzY2VqLXBLa1A4T3Z3eVlIbDJTZkpC?oc=5
- https://news.google.com/rss/articles/CBMi4wFBVV95cUxPZS1YbHc4X3E2bTJFVVlNa2MxelRtN28wVVNqR0wzRXBUMXJaQTJTN3E5WTh2M3BHZllVb01pc18tOWhjbGowQlpwVmZCMWtNV3dxdDJrZE41akxCdkpNY1c4aGtpdE5MekswV21LRjV6UjNockY3Qk5hVUQ0NWVFTlB5WVUyOEplZjlCdVlQTUdZTWdJTVhZQ3VmQl92YmtzeGkwQ1JJYks0UzNUdXI4R2ZVNE1aTXV1Mm5jWTMtdjJmVmNwYkp6RGFQbUdTM1UyZW5wbzRaRmc0WEN5eW1vRXpacw?oc=5
- https://news.google.com/rss/articles/CBMic0FVX3lxTE15TVY0YUJZQXZIYUpKcWRPci1VWGZlbFRXT3pmNkJUcF9MbVFtUWdhdnNnRDRGU1ktWXZ5SExlRjViYkpZSGtrTEtadE1TdDJjWk51eDV5eE1lMi03bTFxb0YxdFIteEU5OWFyZ0s4cnlrTTA?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPU0RwVjVWeDQ2RENzVzNYZXRJT0E4ZWtkWE5VcXdnbm5Fb0VpTksyVG92UXFNNWpybVBoMFJ3WWtZZGQ4ZGoxM2YyRzkxLWI0SnNnQ3UtbnRCQmpsQ0V6WkpQdE1PNDRnWFhEVUZTbndmNktZeVlwdW03bzJLand6Ri1STm9VTHkzU083bHZSM2VJYnFWUWJJeW9EYw?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPX0lGaFVmall4RXFtb05Ud0FrYk4wdVVPZ1pMaURhckZhZE41VktXclRSV2FNZW1uLVFfQUNITTFIZ25WNkFSX3ZzQzJMOFBEUUE1YV9Qc3A2Q0E4SGwzZkZ5LV9BcnRHdzQwbF9SSUlscUxlQ1RmVGpiRE56VXJxSVpUUV9Ud3BzVjcxUTFR?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxPVExmbVgwRmdpZEUxb0J1U2tqcUtPdHVxUUhwZ3NUWXkwYWJIQkJCeEV5LW1ETHJub0RQcGFIeWdhVFViNU9rdVJBNk9TWWhzUFF5OFg1VFBXU2ticzFqR0hVSzFaUl9ZazIwX0F1akpVVDI5V1hwNTJwVlh6MkczSFhn?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQc3NNb1RNWmpjTFRUWWdBOC1mampaLWQ1YWFoYW9aRlNCcndUWXBWSkJEb2RnWWFPMVhkTS1mSG5sNmFNS0RmaEJ1aXFPVnBhTzdHc1hyUDA5enpSeFgzUjBqRnBhSURweGtoNHRNNTA5MWpabi1MMHpxTE91MFdJSzRDUGdmVkNCbERuV21fYVZMdUFyS2FHcg?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNRDhzVlRiSVpJay1TNlJ4c0ZnUzRBUjZ4TFJZaEVFbjVIZmJVbzVzR0RWUGFjUS1rTXdmWjdlRjlSd2VpVFN1WVBDeWd1Z2FXYlNqbkdxbFkyM3NGbTNROG90MV9HR0Q4aFUxeWhyWllCdGYwV2FSNEtISnpaZWpBUTZCZUx4OE9SUmRaRHBsdVdYLUZRZy1jZ1NTZEUyWEZlX3c1Uw?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxQbjBleVA1OXJDbThsRkhnRUZzWTZDYUFtS3VCTUllTDlWSWpneURNVkd2M0dJa2dxaXZSclRWU1JIVEk5aE5SdmY0SlNlc1U5Q3VnOGdRUkZjNHBlWnhqTVgwMzZ3Z3BIRkowMURSTlZLSFpHWHEyNjMxdFdGbWFQMkhB?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOZm5OcG9fOWsxbGR6RGlCZXVQRFdDNFZYb1dWUVZqNUw3UUdKcWd6Rk1XVkFZVFZTc0RKMUZuRTVIZmxZSUhFTVZZYm81al9uT3B4QXQzUzRKR3FjdXVhOW55WF94enVWdWpha3RJUHJPZ0JGUEtvTjNxbmtmNTQzOEdNbldicGtjNXU1TGd4dzJqeld2bjZEalV3?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPbmE2VkVuZlFSb045UDJrTXdTNE1QMVlzblhoM2hqUVdqU3pzRGQwZzFWeS1wRHVaNktxN01QYXFwUHYxOGtWY0s2M2k4MWdXem11YThKc1BJTVgxWTBwcVFmVk1LTzJ4UzJrTUZic01VekRoNk5hUEs0MUU2b2U2b1EtRlBwZ1pWdFlzempvWHkzdVNTMzNZOW9ueE9TWkk?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
