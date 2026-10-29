# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-10-28**
- Market data as_of: **2026-10-28**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-10-28**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-29T02:10:23.058908+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 6, 'ai': 12, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261028T015717Z-533e470c/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 15 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 29.17%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 578.4400 |
| Return 1D (%) | 3.2449 |
| Return 1W (%) | 4.6534 |
| Return 1M (%) | -4.8415 |
| Return YTD (%) | 170.0971 |
| Return 1Y (%) | 124.1929 |
| Annualized volatility (%) | 68.2034 |
| Beta vs SPY | 3.2457 |
| Max drawdown (%) | -27.7608 |
| Sharpe (rf=0) | 1.5273 |
| Downside deviation (rf=0, %) | 42.7990 |
| Sortino (rf=0) | 2.4338 |
| Historical VaR 95% (1D, %) | 5.8580 |
| Historical ES 95% (1D, %) | 8.2198 |
| Correlation vs SPY | 0.6045 |
| Tracking error vs SPY (%) | 61.3648 |
| P/E (trailing) | 142.82 |
| P/B | 14.04 |
| EV/EBITDA | 97.83 |
| Revenue growth (%) | 50.10 |
| Forward P/E (estimate) | 36.50 |
| Gross margin (%) | 55.72 |
| Operating margin (%) | 17.25 |
| Return on equity (%) | 10.20 |
| Free cash flow yield (%) | 0.94 |
| MA50 | 545.5834 |
| Close vs MA50 (%) | 6.0223 |
| MA200 | 407.3555 |
| Close vs MA200 (%) | 41.9988 |
| RSI (14, Wilder) | 53.6184 |
| MACD (12,26) | -6.5638 |
| MACD signal (9) | -2.1652 |
| MACD histogram | -4.3986 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 270, 'SPY': 270}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 578.4400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 3.2449 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.6534 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -4.8415 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 170.0971 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 124.1929 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 68.2034 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 42.7990 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.4338 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 5.8580 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 8.2198 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6045 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 61.3648 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.2457 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.7608 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.5273 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 36.5011 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 55.7240 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.2500 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.1960 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.9363 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 142.8247 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 53.6184 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -4.3986 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.0223 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 41.9988 -> Clearly above the moving-average trend level.

## TAILWINDS

### Advanced Micro Devices (NASDAQ:AMD) Stock Price Up 3.2% Following Analyst Upgrade
- Summary: Advanced Micro Devices (NASDAQ:AMD) Stock Price Up 3.2% Following Analyst Upgrade
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxQamJzOU5ZZVFFb09TS1NBY3ExTmxiVS1TYmdYSEJGeU1YR3ZPQUZ4eHZlMTdTeVNhT1N4dVdnRmF6WndfUmZuS3BBdm91ZC1yOHNBTkhZSllSU1NUeUhWcTRVdjR6YXdMTEhPUUp1akJRRkx3UVZVU09Ubkhmc1lrWjdaMVpwc3BZVnQ0RklqaE83NnkyMkRyb3JQR3FRSGRmUjlaMW9vcWtSVklUdnlRMm9fNDBvb21SWUFjS0ZsdUpTc0JwOHhvM3kxUFFCSGFtRGs4?oc=5>

### AMD (NASDAQ:AMD) Stock Surges 5% as US$1 Billion Meta Investment Boosts AI Partnership
- Summary: AMD (NASDAQ:AMD) Stock Surges 5% as US$1 Billion Meta Investment Boosts AI Partnership
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTFA1MXF5NFpBeU9EU2lfajFKTHFjZmpuLWg2aFNTZ3VkaWtsY0t4SVNJSlNWb1E1V2FCYnFnTU1kMVdkekx6MDB6bkVsaExRSFEwMFhvZjVCNE9FaG1ZLTQ2RjJlb2p1elpGS2NPQlhJaFA5anZwQ3EySQ?oc=5>

### Advanced Micro Devices Inc (AMD) Shares Surge 5.5% -- What GF Sc
- Summary: Advanced Micro Devices Inc (AMD) Shares Surge 5.5% -- What GF Sc
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPd29MNjIzX0M4T3ZFU0sxU3RubDZkb3MzNzZrUG9Tak03cjNzV2lVNTdRQ1JRX1hyY25IQmkybmh0VXB0MmhpQkVqUW8xaWx4d0I1Sm9vNGd0dHc5VDJKWjc5Q2wwYTBsdnkwdlRUdnZuaUdVVGtxeWFKRGwyUDhMMmFxc21MT05LbWE4M09tRWIxdFFuZGtoOVZVOXhGSXRRVXNYaE9TbmYteWhqanU0ckNOc2NVSEpTRkhuOXhR?oc=5>

### AMD Stock: $560.26 After 5.45% Jump on Meta Helios Deal Before 3 November Results – Bull $658, Bear $516
- Summary: AMD Stock: $560.26 After 5.45% Jump on Meta Helios Deal Before 3 November Results – Bull $658, Bear $516
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPb0tZV3p4SV9tY3hSS1FvMlpxd0VkUHJSV3lPenM3RXE3YVlLX2lvQU82M3dkUENXYlFGZG5RYThsMjhGVGliQkZlZjcwZ3JBdDNMRGsxSDdnLTRsSUhvQ2tmblJrM19ET1BoUFMzSGhEaUpLeWF4SkZIMUxhZ05nVy1lRUdSLUFBdm1uYnpwZ1lwa29zTk8zS2ZMYlFIbF9BNGt6RkJhdXR0RUpLMXVyU1o5MmFyNENmelpveVFSRExkODIz?oc=5>

### Advanced Micro Devices (AMD) Rises Higher Than Market: Key Facts
- Summary: AMD stock outperforms market, indicating strong investor confidence.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNZzYtRE1JWERFWUdyTHdsRzdScUtHN3ZQRHlyZ3B2WW5qU3plWk9JWXc5Um9FZlJvOU03MkhKSFBnV2pCUTNqZjBvaVQ4eXJkamNnd01VNFp3MFZRY1M3R1VSNmlLNVNBa1pNclozc0FtU190NnV1U1ZpNlNGbWlVc3VXSkJNbGEzMTAtaEdtX1R5NWZOUjFFUmgtaDU2dw?oc=5>

## HEADWINDS

### Cathie Wood’s ARK sells AMD stock, buys Circle Internet Group
- Summary: ARK sells AMD shares, reducing exposure to the chipmaker.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxQc2ExdnJLZ3N0UXNmZHdFRWt5UFNLMGxMOFhXdGlVMlBJR056QktyUHE0SE5CMlZOR1pXdENGVm1WYXNrei1IaHRiZ2VwSnQ5U0VYbkMzeHd1amdrZXc3a3NJTkdKeDZYRU5UUElyTnhZZ2lXNG90cVpHOUJJOXNKSld2bXZkd3NzeWJON2YzeklEWWZmb1BDS1o5b0tldDJXaG5rVTJzWHBFM011b3pJRFFzOHFIZTg?oc=5>

## CATALYSTS

### Advanced Micro Devices (AMD) Ties AI Deals To $95 Billion Infrastructure Push
- Summary: Advanced Micro Devices (AMD) Ties AI Deals To $95 Billion Infrastructure Push
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNQ2NvRFJMOTVERnp2TEFXSjhyd0N2THZyMGtaNDg1VlJTMUt4OC1vd3F3Zll3SmJvSGFtMjYycHFILXNybHBzMHlPc19RR0trWDJybmxjeVB4TEkwT0ZrS1hsQnMyM1dlSlpWYWNDblJUZC1NYUtGM29PSVZZazIwV2g1NE1DR0ZBVEIyTmtNQzc1bUg5RzRmWWY1QQ?oc=5>

### AMD To Invest $1B In Meta Stock Offering As AI Partnership Expands — Helios Systems Now Running At Meta
- Summary: AMD To Invest $1B In Meta Stock Offering As AI Partnership Expands — Helios Systems Now Running At Meta
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPMVZONEsxU01Pa2dLUzZQWFFrM0VMQzJLWFQ1UzVkNW5zS0VIeDNCUDFYbmZMSWVnODBFWkJhLWVfWGNabFlTWEpicjYxcjItbHV5OE9pMkp2dzBKLUh3dFdGT0c5V19wWTBXQmVUQ3doNGRwa3BqalozWUx0M0lsVE9vdERua2Q1aGN2VWZzaVc3Zw?oc=5>

### Nvidia, AMD Get Their Jollies Hooking Up With Meta's Muse
- Summary: AMD partners with Meta, enhancing chip integration.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQYUYtTUVGcVg1OEY2WFpMeXZWTmQ0XzB0NGNEdTRTcE5vdGhGaTd3Yzg1XzlLbmZMMTNHUmhGcGxFNXJyNjhmM01KdVU3ZlNsc09IT1o0UWdRSW1fZUdLVVY5UGZOTnVsRXZxUUMtelh0eVFXRUF3YWY4UlQ1OEhLNi1KSVBpcHl5VHRB?oc=5>

### Nvidia, AMD and Broadcom could buy Meta shares as part of $35 billion stock offering
- Summary: AMD may participate in a $35B Meta share purchase, a corporate action unrelated to its own operations.
- Date: 2026-10-26 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxPdDYyd2VndnhVdFI0ckxsUnVKbVRRaGxOMEoxOUpZTFcxeWJIdW5MbzlIWElaUW05RDdfNlM1b01jM3lFTkNCN184YzZwaU9PMWxOOVBKZkNrY2tGZldMc3U3THdNU0FST1ZKcmgtTF95ZlIwV3ZiYlBaVU12RXNoUjdIcVNBRGdnMldGUXllTXRxazY2SWNfZjZ0cks5T3p4LWppMUZqb1E3MWdpdThjVEU1OGNKdng4SUZHQndKalFVOTA?oc=5>

### AMD and Nvidia Split the AI Chip Market. 1 Stock Is Far Cheaper Today.
- Summary: AMD holds a larger AI chip market share, but is pricier than Nvidia.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPa05Cb1NpWEpwbmpNOVRNV3E4ZTZqNFFLTUhpNERwRWd5N2dlQkFIV05feGs0am5uSDFTWDAzNzRpRlYzdjVwdDdtaXQ5WGhyQTA1bURwT3AyMlpEV0F5LWY2MHpSUnM1SzZFaVN4bzdqdzRTYkY3bTh6M2FhWUk4TlVLUzQ5WVJuOGVtQVpCWUdDZw?oc=5>

### Advanced Micro Devices (AMD) Earnings Expected to Grow: Should You Buy?
- Summary: Analysts forecast AMD earnings growth, indicating potential upside.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNekRsZGVrS3pGUDBHdmNrOS1KREpLcUlEdmpDOElCcVk1RDB4WU5kdnM5ZTRLMzRsMU1MSm5tazAydTVPNWZ3aU0xa3F1RWV1M1VCYmpPeWEtSXpXTER5Smh4TGpGS3ZzSXhYU3FhMmgxUzVqazVLVlpKbmEyUE44ZmMzUUNHT3kxZHEwWUJJT1Y0Z3F6bW5vSmF5ajE4cTJBUXc?oc=5>

### Dear AMD Stock Fans, Mark Your Calendar for November 3
- Summary: AMD announces a significant event scheduled for November 3, urging investors to note the date for upcoming developments.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQM1A2S19LMEpnSUJCWDcxNnZERzNhTkR2dnFTSkd3X0NMWjBFZjRBcm5ldVo0UnJ3a1g0ZFhjOWwtcmxETGF0Mk5yWC1Gb1dzaGJwU1Y3dGpTeG5fVE5GOEJyMEtmaDlMRWctYUJQamcxMzllQ0MzUThTQ2hiUGZNUHVYOWpxNm96QmxTYTVWSUQtS3JIVzY4Y2U2MjBoQQ?oc=5>

### Is AMD Stock a Buy, Sell, or Hold Right Now? Here's What I'm Doing.
- Summary: An analyst shares personal investment stance on AMD, offering buy/sell/hold guidance.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQT2VSZWtSUHFfTTgxRDVWeHVURFpyQ0tOeFpsYU5sbURaeEZ5LUF6TVdZYS05VEQxTF9fWDQzaFQ4ZXNHOWhCUFVrM29JZ3V6RDdOZGd6aHZIT0djQmNpSXRzemQ1SVhNMnozUC1SNUZLWUs3UGJLQ2x3T1FPc1lVOEVoMWdSYUdOaUtXa3ZWTk80YXJK?oc=5>

### AMD Q3 Preview: The Market Is Watching OpenAI, I'm Watching EPYC (NASDAQ:AMD)
- Summary: Preview of AMD Q3 earnings, highlighting focus on EPYC processors amid OpenAI market interest.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNY3IzX3Q4eEEzdVBuN0p2WEpQYmtOQ0hYV2VXV0hFejZnRUlLT1c5bnMwbmtiYXRxT1dGZUUwajFIMVNxR2o4UDlaeFJVVFZ0aEJiOXVQMGthWjhMR2pZQWJ4M3RhZTBKV0JjYmViX3RCWVJaMnh3YjhYcy0xaXd5S2w2QmttNzBNczhQYlR4ZU1UVmZDQ01WR3F3SHlnOWdYZGxQYg?oc=5>

### Why Is AMD Stock Up Today, 10/28/26?
- Summary: Explains short‑term price increase of AMD shares on October 28, 2026.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMickFVX3lxTE9MTjdBd05Ic001SUVqSmtzNVdaall4RWVISjc0QXcwQ01LeDY5N1ZrUnRobzJ1ZjhKRTU2cWJQa3N2VVdpM2duMXZSX2ZKUldYYWpmanNUV2hkWWl5WTUtZmZ4aTJhNDg1M3BOV3pMam9iZw?oc=5>

### Cathie Wood Extends Archer, Joby Buying Spree; Ark Sells More AMD, Taiwan Semiconductor Shares
- Summary: Ark Invest sells additional AMD shares as part of portfolio adjustments.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxQNlI2alFjamgtbVhhUERmYUx1SmIwdWRsbTV5UUtKWVo4TXNiUzZHd3o5MGZ5bXZTM3RUd3ZDNEZwSmtQWVVRbDk0bVR4UVFEUmY0UjdJM0pYVDJaTDNmRC1xbHNKRVRRSGpiZWljYTR4RVZzZHFWUXRORnpsa05zSDJod08tVWVBVVphRkllalhjdUFtSUdRbFlCdlIyWmRqUUQzQlVnZl8wb25hMTdGUVVLZzg0RlMxYl9oR1NWNTlrWTg3Mk9ITnU3OUpNZUc0VFFCSVNyY0V5WjM2TVN4VDdtUTJNXzZ4WDZZYjJRdw?oc=5>

### AMD CFO Delivers Bullish Update That Investors Will Want to Hear
- Summary: AMD CFO issues a bullish outlook, signaling potential upside for investors.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNXzNrZkxRVlRMRDg4SUZYeVI4cDVqSTl3QkpXVkJ6MnlPVzBJZ3BoTWhYNGtKUTNVMGdaNUZTX3V6RGw3WVRpSEI0YTExbUZ1cmtva1hTM3FYamhTckJZb3dOaUdsSkZ6bkZaM1E2WERhMThUemEyLTZBYkNScTZiWTYyaTlVLUVLV1lNOUhrMFdVNVZSRkdvd0FzYlhHdXRw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **142.82** | **14.04** | **97.83** | **50.10** | **944,288,825,344.00 USD** | **124.19** |
| NVDA | 27.54 | 22.71 | 25.67 | 105.90 | 5,200,780,722,176.00 USD | 7.39 |
| INTC | N/A | 5.50 | 30.78 | 25.40 | 504,981,618,688.00 USD | 130.03 |
| AVGO | 44.93 | 16.85 | 32.81 | 85.50 | 1,679,410,724,864.00 USD | -4.97 |

Peers fetched as_of: 2026-10-28; AMD reuses existing data (market data as_of: 2026-10-28); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-28

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-05
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,297,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQamJzOU5ZZVFFb09TS1NBY3ExTmxiVS1TYmdYSEJGeU1YR3ZPQUZ4eHZlMTdTeVNhT1N4dVdnRmF6WndfUmZuS3BBdm91ZC1yOHNBTkhZSllSU1NUeUhWcTRVdjR6YXdMTEhPUUp1akJRRkx3UVZVU09Ubkhmc1lrWjdaMVpwc3BZVnQ0RklqaE83NnkyMkRyb3JQR3FRSGRmUjlaMW9vcWtSVklUdnlRMm9fNDBvb21SWUFjS0ZsdUpTc0JwOHhvM3kxUFFCSGFtRGs4?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTFA1MXF5NFpBeU9EU2lfajFKTHFjZmpuLWg2aFNTZ3VkaWtsY0t4SVNJSlNWb1E1V2FCYnFnTU1kMVdkekx6MDB6bkVsaExRSFEwMFhvZjVCNE9FaG1ZLTQ2RjJlb2p1elpGS2NPQlhJaFA5anZwQ3EySQ?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPd29MNjIzX0M4T3ZFU0sxU3RubDZkb3MzNzZrUG9Tak03cjNzV2lVNTdRQ1JRX1hyY25IQmkybmh0VXB0MmhpQkVqUW8xaWx4d0I1Sm9vNGd0dHc5VDJKWjc5Q2wwYTBsdnkwdlRUdnZuaUdVVGtxeWFKRGwyUDhMMmFxc21MT05LbWE4M09tRWIxdFFuZGtoOVZVOXhGSXRRVXNYaE9TbmYteWhqanU0ckNOc2NVSEpTRkhuOXhR?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPb0tZV3p4SV9tY3hSS1FvMlpxd0VkUHJSV3lPenM3RXE3YVlLX2lvQU82M3dkUENXYlFGZG5RYThsMjhGVGliQkZlZjcwZ3JBdDNMRGsxSDdnLTRsSUhvQ2tmblJrM19ET1BoUFMzSGhEaUpLeWF4SkZIMUxhZ05nVy1lRUdSLUFBdm1uYnpwZ1lwa29zTk8zS2ZMYlFIbF9BNGt6RkJhdXR0RUpLMXVyU1o5MmFyNENmelpveVFSRExkODIz?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNZzYtRE1JWERFWUdyTHdsRzdScUtHN3ZQRHlyZ3B2WW5qU3plWk9JWXc5Um9FZlJvOU03MkhKSFBnV2pCUTNqZjBvaVQ4eXJkamNnd01VNFp3MFZRY1M3R1VSNmlLNVNBa1pNclozc0FtU190NnV1U1ZpNlNGbWlVc3VXSkJNbGEzMTAtaEdtX1R5NWZOUjFFUmgtaDU2dw?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxQc2ExdnJLZ3N0UXNmZHdFRWt5UFNLMGxMOFhXdGlVMlBJR056QktyUHE0SE5CMlZOR1pXdENGVm1WYXNrei1IaHRiZ2VwSnQ5U0VYbkMzeHd1amdrZXc3a3NJTkdKeDZYRU5UUElyTnhZZ2lXNG90cVpHOUJJOXNKSld2bXZkd3NzeWJON2YzeklEWWZmb1BDS1o5b0tldDJXaG5rVTJzWHBFM011b3pJRFFzOHFIZTg?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNQ2NvRFJMOTVERnp2TEFXSjhyd0N2THZyMGtaNDg1VlJTMUt4OC1vd3F3Zll3SmJvSGFtMjYycHFILXNybHBzMHlPc19RR0trWDJybmxjeVB4TEkwT0ZrS1hsQnMyM1dlSlpWYWNDblJUZC1NYUtGM29PSVZZazIwV2g1NE1DR0ZBVEIyTmtNQzc1bUg5RzRmWWY1QQ?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPMVZONEsxU01Pa2dLUzZQWFFrM0VMQzJLWFQ1UzVkNW5zS0VIeDNCUDFYbmZMSWVnODBFWkJhLWVfWGNabFlTWEpicjYxcjItbHV5OE9pMkp2dzBKLUh3dFdGT0c5V19wWTBXQmVUQ3doNGRwa3BqalozWUx0M0lsVE9vdERua2Q1aGN2VWZzaVc3Zw?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQYUYtTUVGcVg1OEY2WFpMeXZWTmQ0XzB0NGNEdTRTcE5vdGhGaTd3Yzg1XzlLbmZMMTNHUmhGcGxFNXJyNjhmM01KdVU3ZlNsc09IT1o0UWdRSW1fZUdLVVY5UGZOTnVsRXZxUUMtelh0eVFXRUF3YWY4UlQ1OEhLNi1KSVBpcHl5VHRB?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxPdDYyd2VndnhVdFI0ckxsUnVKbVRRaGxOMEoxOUpZTFcxeWJIdW5MbzlIWElaUW05RDdfNlM1b01jM3lFTkNCN184YzZwaU9PMWxOOVBKZkNrY2tGZldMc3U3THdNU0FST1ZKcmgtTF95ZlIwV3ZiYlBaVU12RXNoUjdIcVNBRGdnMldGUXllTXRxazY2SWNfZjZ0cks5T3p4LWppMUZqb1E3MWdpdThjVEU1OGNKdng4SUZHQndKalFVOTA?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPa05Cb1NpWEpwbmpNOVRNV3E4ZTZqNFFLTUhpNERwRWd5N2dlQkFIV05feGs0am5uSDFTWDAzNzRpRlYzdjVwdDdtaXQ5WGhyQTA1bURwT3AyMlpEV0F5LWY2MHpSUnM1SzZFaVN4bzdqdzRTYkY3bTh6M2FhWUk4TlVLUzQ5WVJuOGVtQVpCWUdDZw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNekRsZGVrS3pGUDBHdmNrOS1KREpLcUlEdmpDOElCcVk1RDB4WU5kdnM5ZTRLMzRsMU1MSm5tazAydTVPNWZ3aU0xa3F1RWV1M1VCYmpPeWEtSXpXTER5Smh4TGpGS3ZzSXhYU3FhMmgxUzVqazVLVlpKbmEyUE44ZmMzUUNHT3kxZHEwWUJJT1Y0Z3F6bW5vSmF5ajE4cTJBUXc?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQM1A2S19LMEpnSUJCWDcxNnZERzNhTkR2dnFTSkd3X0NMWjBFZjRBcm5ldVo0UnJ3a1g0ZFhjOWwtcmxETGF0Mk5yWC1Gb1dzaGJwU1Y3dGpTeG5fVE5GOEJyMEtmaDlMRWctYUJQamcxMzllQ0MzUThTQ2hiUGZNUHVYOWpxNm96QmxTYTVWSUQtS3JIVzY4Y2U2MjBoQQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQT2VSZWtSUHFfTTgxRDVWeHVURFpyQ0tOeFpsYU5sbURaeEZ5LUF6TVdZYS05VEQxTF9fWDQzaFQ4ZXNHOWhCUFVrM29JZ3V6RDdOZGd6aHZIT0djQmNpSXRzemQ1SVhNMnozUC1SNUZLWUs3UGJLQ2x3T1FPc1lVOEVoMWdSYUdOaUtXa3ZWTk80YXJK?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxNdmh5VkVkUFpPdFBHRy1RMzk4Q3pNNTNlbU0wSE11YVJkZE5vaUREbm1HS250Zk5mQjgtNE5LSy11b3Y0OGJHNm1LV1NtWW9WZmlOc0wtTUF1ZkFqNS1ERjR2OEphU2V3YWwyLWlrcG5EaVpNRVVUQXozQXltWWMyNUVPOFJoaGpHUTJqZTlpUUNkRmhoZDQtZ1FvR21nVzVLeGkxS1FOTEFvOTFXWGZMdDdhaXhBN3hQeVU5aGVpWFdwM0JKZDNFbU5OTEp0SXh3eVhaTDFlb01EbXdaaXc?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNY3IzX3Q4eEEzdVBuN0p2WEpQYmtOQ0hYV2VXV0hFejZnRUlLT1c5bnMwbmtiYXRxT1dGZUUwajFIMVNxR2o4UDlaeFJVVFZ0aEJiOXVQMGthWjhMR2pZQWJ4M3RhZTBKV0JjYmViX3RCWVJaMnh3YjhYcy0xaXd5S2w2QmttNzBNczhQYlR4ZU1UVmZDQ01WR3F3SHlnOWdYZGxQYg?oc=5
- https://news.google.com/rss/articles/CBMickFVX3lxTE9MTjdBd05Ic001SUVqSmtzNVdaall4RWVISjc0QXcwQ01LeDY5N1ZrUnRobzJ1ZjhKRTU2cWJQa3N2VVdpM2duMXZSX2ZKUldYYWpmanNUV2hkWWl5WTUtZmZ4aTJhNDg1M3BOV3pMam9iZw?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxQNlI2alFjamgtbVhhUERmYUx1SmIwdWRsbTV5UUtKWVo4TXNiUzZHd3o5MGZ5bXZTM3RUd3ZDNEZwSmtQWVVRbDk0bVR4UVFEUmY0UjdJM0pYVDJaTDNmRC1xbHNKRVRRSGpiZWljYTR4RVZzZHFWUXRORnpsa05zSDJod08tVWVBVVphRkllalhjdUFtSUdRbFlCdlIyWmRqUUQzQlVnZl8wb25hMTdGUVVLZzg0RlMxYl9oR1NWNTlrWTg3Mk9ITnU3OUpNZUc0VFFCSVNyY0V5WjM2TVN4VDdtUTJNXzZ4WDZZYjJRdw?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNXzNrZkxRVlRMRDg4SUZYeVI4cDVqSTl3QkpXVkJ6MnlPVzBJZ3BoTWhYNGtKUTNVMGdaNUZTX3V6RGw3WVRpSEI0YTExbUZ1cmtva1hTM3FYamhTckJZb3dOaUdsSkZ6bkZaM1E2WERhMThUemEyLTZBYkNScTZiWTYyaTlVLUVLV1lNOUhrMFdVNVZSRkdvd0FzYlhHdXRw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
