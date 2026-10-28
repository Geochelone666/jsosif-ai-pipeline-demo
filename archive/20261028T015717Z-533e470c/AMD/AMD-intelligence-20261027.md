# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-10-27**
- Market data as_of: **2026-10-27**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-10-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-28T01:57:22.080676+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 8, 'ai': 11, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261026T005504Z-6368ad31/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 17 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 24.0%; oldest publication 2026-10-25

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 560.2600 |
| Return 1D (%) | 5.4547 |
| Return 1W (%) | 4.7724 |
| Return 1M (%) | -11.1587 |
| Return YTD (%) | 161.6081 |
| Return 1Y (%) | 115.7585 |
| Annualized volatility (%) | 68.1518 |
| Beta vs SPY | 3.2400 |
| Max drawdown (%) | -27.7608 |
| Sharpe (rf=0) | 1.4712 |
| Downside deviation (rf=0, %) | 42.8038 |
| Sortino (rf=0) | 2.3425 |
| Historical VaR 95% (1D, %) | 5.8580 |
| Historical ES 95% (1D, %) | 8.2198 |
| Correlation vs SPY | 0.6038 |
| Tracking error vs SPY (%) | 61.3244 |
| P/E (trailing) | 142.92 |
| P/B | 13.60 |
| EV/EBITDA | 94.73 |
| Revenue growth (%) | 50.10 |
| Forward P/E (estimate) | 35.56 |
| Gross margin (%) | 55.72 |
| Operating margin (%) | 17.25 |
| Return on equity (%) | 10.20 |
| Free cash flow yield (%) | 0.97 |
| MA50 | 543.7024 |
| Close vs MA50 (%) | 3.0453 |
| MA200 | 405.5017 |
| Close vs MA200 (%) | 38.1647 |
| RSI (14, Wilder) | 49.8169 |
| MACD (12,26) | -9.3818 |
| MACD signal (9) | -1.0655 |
| MACD histogram | -8.3162 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 269, 'SPY': 269}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 560.2600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 5.4547 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.7724 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -11.1587 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 161.6081 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 115.7585 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 68.1518 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 42.8038 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.3425 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 5.8580 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 8.2198 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6038 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 61.3244 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.2400 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.7608 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.4712 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 35.5590 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 55.7240 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.2500 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.1960 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.9667 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 142.9235 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 49.8169 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -8.3162 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.0453 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 38.1647 -> Clearly above the moving-average trend level.

## TAILWINDS

### AMD stock rallies on expanded Meta AI infrastructure deal and broader chip rally
- Summary: AMD stock rallies on expanded Meta AI infrastructure deal and broader chip rally
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPTDhaMUlBSC1CWUlWZGcxLU5GRnJ3NlZROGRCdHpOZW5VZDlYOTJCRlprelVEX1ZoM2xWdGVJdFUtNUFfMFpOQzh5T1V0ZGZ5N3VsWmNZUi0wU19feVJCRUVSd25jTzlFOEFUbnBRVlFneF95WThxZlROVVYxS0JFdU51RTBmSmp6QkJmd1NuLVZKOHZ0VjFQaGhrRQ?oc=5>

### AMD (NASDAQ:AMD) Stock Surges 5% as US$1 Billion Meta Investment Boosts AI Partnership
- Summary: AMD (NASDAQ:AMD) Stock Surges 5% as US$1 Billion Meta Investment Boosts AI Partnership
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTFA1MXF5NFpBeU9EU2lfajFKTHFjZmpuLWg2aFNTZ3VkaWtsY0t4SVNJSlNWb1E1V2FCYnFnTU1kMVdkekx6MDB6bkVsaExRSFEwMFhvZjVCNE9FaG1ZLTQ2RjJlb2p1elpGS2NPQlhJaFA5anZwQ3EySQ?oc=5>

### AMD Stocks Gain 3.3% With Meta Testing Helios and a $1 Billion I
- Summary: AMD Stocks Gain 3.3% With Meta Testing Helios and a $1 Billion I
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxPZ3phT3AwSHlId3RuZjdfNS1iTDRBZFYtdWNMZ3Nxc3VwWUU0bU1mUXE3a3ZsaTlWUHFhNTJmYjFDNGZvZlV6MGJGbFhoZ2hkSXB1N3I0ektva3h4cUMzQTVIQWZzdHZNRFZHYlFKY2RTaWlLNEtORE1kSDU2NzNMdGk4dVNXVXh4LWUycmFkVHJyTThVN1d2MF9sM0xuSy14MWVROHc4UHZVRXJtdXc?oc=5>

### AMD Stock: $531 After 2.8% Gain, Bull $620, Bear $500
- Summary: AMD Stock: $531 After 2.8% Gain, Bull $620, Bear $500
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxPNjhiaG95ZjRValdtS1doSVByWlk2djdSdlNhb0NOTmN3bnVqQUYtQngteWl3ZVBYWGcyR3hwcHp4bjdGZnhvcVBBT0ZXVUdudnRrSE5KWWF5bG1IXzRMMFVuQUNvYXFMUVNlLXFQSjFrdW5TWUI2T011YjNfb1hMNENWWHFlSlF0MEpSaXhuNDlfd3IxTVhoNkViRGQ2b0I4NEJjRHZmLUZfZTdtcXhfMHR5aXhyTmNhZDZMbkYzNEZ3YUU?oc=5>

### Advanced Micro Devices Inc (AMD) Shares Surge 5.5% -- What GF Sc
- Summary: Advanced Micro Devices Inc (AMD) Shares Surge 5.5% -- What GF Sc
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPd29MNjIzX0M4T3ZFU0sxU3RubDZkb3MzNzZrUG9Tak03cjNzV2lVNTdRQ1JRX1hyY25IQmkybmh0VXB0MmhpQkVqUW8xaWx4d0I1Sm9vNGd0dHc5VDJKWjc5Q2wwYTBsdnkwdlRUdnZuaUdVVGtxeWFKRGwyUDhMMmFxc21MT05LbWE4M09tRWIxdFFuZGtoOVZVOXhGSXRRVXNYaE9TbmYteWhqanU0ckNOc2NVSEpTRkhuOXhR?oc=5>

### Dell, Lenovo, Cisco, HPE, Supermicro: Why AMD’s New AI Blueprint Has Everyone Signing On
- Summary: AMD’s new AI blueprint attracts major OEMs, boosting demand for its processors.
- Date: 2026-10-25 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxOd2diNGt0TW1ZUUlXdjNzdnk0SkF3MTd3cm1taWR6dkUwNlZ6OTBFN2YweTVDbFFDcDBjNExrRFRRVVBMVEdxd080YTlrRUhxVVN3OUFsUzFwM0JkRkNaVkstcDlFdS1Mc0VWVHlJM09xSjAxeDIxU1E5RGVCNkVZWF9ES0JycVdSQURTSHBodWJVVXNLYXZJTGJKS0lEZThSVGNuNnFoTUhoZmZ3dFFxTnRRRmFETnZtaDVrSGZTeERRRW1j?oc=5>

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

### AMD rises as GF ups price target ahead of Q3 results (AMD:NASDAQ)
- Summary: AMD rises as GF ups price target ahead of Q3 results (AMD:NASDAQ)
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQMk5SZjNON1Z0X0dORHRoNk5NRjZuZjRabmZXTE1tRTA5V0hiTGFRdEJLZUhDQ1VQUFRoTC1HTnc1OU5ZUGtWUTc4eENadTVRRTRsWlRmUWhRa1FXVk1UTm85b0x6NmdrTGZYRUl2TzhGc2lLcGpsRl84NFpiU09vbDl4UVl5cUdWZUo3cEdKN3FPdGc0?oc=5>

### Nvidia, AMD and Broadcom could buy Meta shares as part of $35 billion stock offering
- Summary: AMD may participate in a $35B Meta share purchase, a corporate action unrelated to its own operations.
- Date: 2026-10-26 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxPdDYyd2VndnhVdFI0ckxsUnVKbVRRaGxOMEoxOUpZTFcxeWJIdW5MbzlIWElaUW05RDdfNlM1b01jM3lFTkNCN184YzZwaU9PMWxOOVBKZkNrY2tGZldMc3U3THdNU0FST1ZKcmgtTF95ZlIwV3ZiYlBaVU12RXNoUjdIcVNBRGdnMldGUXllTXRxazY2SWNfZjZ0cks5T3p4LWppMUZqb1E3MWdpdThjVEU1OGNKdng4SUZHQndKalFVOTA?oc=5>

### Nvidia, AMD Get Their Jollies Hooking Up With Meta's Muse
- Summary: AMD partners with Meta, enhancing chip integration.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQYUYtTUVGcVg1OEY2WFpMeXZWTmQ0XzB0NGNEdTRTcE5vdGhGaTd3Yzg1XzlLbmZMMTNHUmhGcGxFNXJyNjhmM01KdVU3ZlNsc09IT1o0UWdRSW1fZUdLVVY5UGZOTnVsRXZxUUMtelh0eVFXRUF3YWY4UlQ1OEhLNi1KSVBpcHl5VHRB?oc=5>

### Nvidia, AMD to buy $4B in Meta shares as part of expanded chip partnerships
- Summary: AMD purchases Meta shares, deepening partnership.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQbzNoNElDckgyajBzR3NPZ0tkQ2taREVmc3p1NHZFZDBDT0dPY1NQa29vZElHZGhsQUcxQ2wxV1BGaDVpLXJTSjluQ0hNWWE5U1A1R3Ezc2lkTWZ5X3ZzU1VxV29CM0txQmFFT2xrdUg1bFUzaFV3bDAya2FkMFdBVjh1dEp6ZmZXZEZkWWpNRmY3eHNyVGs0dWNvUHplZWVLZzhZQng3cDdkRklKWjlJ?oc=5>

### New Buy Rating for Advanced Micro Devices (AMD), the Technology Giant
- Summary: Analyst upgrades AMD to buy, signaling confidence in future performance.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5wFBVV95cUxQbXpOQkVqZUlpMWkxZHFlX0tzTVZXY2d6MXdGSlFOZ1U1TTl6cmdnSG52U0VlSnlUZ2txTWhteEV2X1djZHJSU1NCcDhLMk15dFJOdUdtbkMxZTBubXFUaG45V0dBUHB0VTc5RDI0SnM1WlN3TnFCa09NY1owTkZZUlNDUE5INFZVWHJsc1VVYkFyNnVIUDIySGh5ZG5KSFJrS2dqY1NuUWRHQXNYX0tmRkRseThiZjdISVMta2psWmZvR2ZIRjFIb3JtMTN5dVczSDRtWFJNUUM4SDM1aVhINmlESzViNGs?oc=5>

### Advanced Micro Devices (NASDAQ:AMD) Shares Up 5.5% - Time to Buy?
- Summary: AMD shares rise 5.5% in premarket, suggesting a buying opportunity.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNTURldUZOaTN5Z1ZKN1FIUEhBdko2bTFoT2dmX0Z4Mk5vYlpUME1kbmtZNkFHRzRDWmVfZ3YtMWs4TFBGRU5pb0YzS0x1VjJvTUtTSGxRd3FBbHF2cjM2SEZYM2FueU5WVXdTbkgwWTZod1YxMlUzS0R1bWdfZWszM3pGN1dyR2dBbG1Pb19velJ6YThsUHhQU2dGd3lvVk9UbWp3TGVGNi1KT0RYam5ocTd6SnJUUldITUE?oc=5>

### Why Are AI Chip Stocks Broadcom, AMD, and Nvidia Rising in Premarket Today, October 27?
- Summary: AMD and peers see premarket gains, reflecting positive market sentiment.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQZy1QN3JZOEcxcXdFWkpkUWpycG5FMF9YQ1dkVW5ETV9IY0JILXYyQWRhSEtZMDFnNXpaM2ZjcEV2ZzU4YThBak92M2FsRXRSQVMwal9SUEVOODhPODgwTEdoOE5fOGtra0ZZb0ZWTUF4MnU0MGVwYWh2R0RpREhrN3JGcEF1cWJmeEd2NDNGV3hPaEZfbERzcUpPZ3J0SktYWVp3MWRqbnc?oc=5>

### Advanced Micro Devices (AMD) Earnings Expected to Grow: Should You Buy?
- Summary: Analysts forecast AMD earnings growth, indicating potential upside.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNekRsZGVrS3pGUDBHdmNrOS1KREpLcUlEdmpDOElCcVk1RDB4WU5kdnM5ZTRLMzRsMU1MSm5tazAydTVPNWZ3aU0xa3F1RWV1M1VCYmpPeWEtSXpXTER5Smh4TGpGS3ZzSXhYU3FhMmgxUzVqazVLVlpKbmEyUE44ZmMzUUNHT3kxZHEwWUJJT1Y0Z3F6bW5vSmF5ajE4cTJBUXc?oc=5>

### AMD and Nvidia Split the AI Chip Market. 1 Stock Is Far Cheaper Today.
- Summary: AMD holds a larger AI chip market share, but is pricier than Nvidia.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPa05Cb1NpWEpwbmpNOVRNV3E4ZTZqNFFLTUhpNERwRWd5N2dlQkFIV05feGs0am5uSDFTWDAzNzRpRlYzdjVwdDdtaXQ5WGhyQTA1bURwT3AyMlpEV0F5LWY2MHpSUnM1SzZFaVN4bzdqdzRTYkY3bTh6M2FhWUk4TlVLUzQ5WVJuOGVtQVpCWUdDZw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **142.92** | **13.60** | **94.73** | **50.10** | **914,610,454,528.00 USD** | **115.76** |
| NVDA | 27.55 | 22.98 | 25.98 | 105.90 | 5,262,596,898,816.00 USD | 14.09 |
| INTC | N/A | 5.40 | 30.24 | 25.40 | 495,519,465,472.00 USD | 137.08 |
| AVGO | 43.72 | 16.39 | 31.95 | 85.50 | 1,634,156,675,072.00 USD | -4.74 |

Peers fetched as_of: 2026-10-27; AMD reuses existing data (market data as_of: 2026-10-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-27

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

- https://news.google.com/rss/articles/CBMimwFBVV95cUxPTDhaMUlBSC1CWUlWZGcxLU5GRnJ3NlZROGRCdHpOZW5VZDlYOTJCRlprelVEX1ZoM2xWdGVJdFUtNUFfMFpOQzh5T1V0ZGZ5N3VsWmNZUi0wU19feVJCRUVSd25jTzlFOEFUbnBRVlFneF95WThxZlROVVYxS0JFdU51RTBmSmp6QkJmd1NuLVZKOHZ0VjFQaGhrRQ?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTFA1MXF5NFpBeU9EU2lfajFKTHFjZmpuLWg2aFNTZ3VkaWtsY0t4SVNJSlNWb1E1V2FCYnFnTU1kMVdkekx6MDB6bkVsaExRSFEwMFhvZjVCNE9FaG1ZLTQ2RjJlb2p1elpGS2NPQlhJaFA5anZwQ3EySQ?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPZ3phT3AwSHlId3RuZjdfNS1iTDRBZFYtdWNMZ3Nxc3VwWUU0bU1mUXE3a3ZsaTlWUHFhNTJmYjFDNGZvZlV6MGJGbFhoZ2hkSXB1N3I0ektva3h4cUMzQTVIQWZzdHZNRFZHYlFKY2RTaWlLNEtORE1kSDU2NzNMdGk4dVNXVXh4LWUycmFkVHJyTThVN1d2MF9sM0xuSy14MWVROHc4UHZVRXJtdXc?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxPNjhiaG95ZjRValdtS1doSVByWlk2djdSdlNhb0NOTmN3bnVqQUYtQngteWl3ZVBYWGcyR3hwcHp4bjdGZnhvcVBBT0ZXVUdudnRrSE5KWWF5bG1IXzRMMFVuQUNvYXFMUVNlLXFQSjFrdW5TWUI2T011YjNfb1hMNENWWHFlSlF0MEpSaXhuNDlfd3IxTVhoNkViRGQ2b0I4NEJjRHZmLUZfZTdtcXhfMHR5aXhyTmNhZDZMbkYzNEZ3YUU?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPd29MNjIzX0M4T3ZFU0sxU3RubDZkb3MzNzZrUG9Tak03cjNzV2lVNTdRQ1JRX1hyY25IQmkybmh0VXB0MmhpQkVqUW8xaWx4d0I1Sm9vNGd0dHc5VDJKWjc5Q2wwYTBsdnkwdlRUdnZuaUdVVGtxeWFKRGwyUDhMMmFxc21MT05LbWE4M09tRWIxdFFuZGtoOVZVOXhGSXRRVXNYaE9TbmYteWhqanU0ckNOc2NVSEpTRkhuOXhR?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxOd2diNGt0TW1ZUUlXdjNzdnk0SkF3MTd3cm1taWR6dkUwNlZ6OTBFN2YweTVDbFFDcDBjNExrRFRRVVBMVEdxd080YTlrRUhxVVN3OUFsUzFwM0JkRkNaVkstcDlFdS1Mc0VWVHlJM09xSjAxeDIxU1E5RGVCNkVZWF9ES0JycVdSQURTSHBodWJVVXNLYXZJTGJKS0lEZThSVGNuNnFoTUhoZmZ3dFFxTnRRRmFETnZtaDVrSGZTeERRRW1j?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNZzYtRE1JWERFWUdyTHdsRzdScUtHN3ZQRHlyZ3B2WW5qU3plWk9JWXc5Um9FZlJvOU03MkhKSFBnV2pCUTNqZjBvaVQ4eXJkamNnd01VNFp3MFZRY1M3R1VSNmlLNVNBa1pNclozc0FtU190NnV1U1ZpNlNGbWlVc3VXSkJNbGEzMTAtaEdtX1R5NWZOUjFFUmgtaDU2dw?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxQc2ExdnJLZ3N0UXNmZHdFRWt5UFNLMGxMOFhXdGlVMlBJR056QktyUHE0SE5CMlZOR1pXdENGVm1WYXNrei1IaHRiZ2VwSnQ5U0VYbkMzeHd1amdrZXc3a3NJTkdKeDZYRU5UUElyTnhZZ2lXNG90cVpHOUJJOXNKSld2bXZkd3NzeWJON2YzeklEWWZmb1BDS1o5b0tldDJXaG5rVTJzWHBFM011b3pJRFFzOHFIZTg?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNQ2NvRFJMOTVERnp2TEFXSjhyd0N2THZyMGtaNDg1VlJTMUt4OC1vd3F3Zll3SmJvSGFtMjYycHFILXNybHBzMHlPc19RR0trWDJybmxjeVB4TEkwT0ZrS1hsQnMyM1dlSlpWYWNDblJUZC1NYUtGM29PSVZZazIwV2g1NE1DR0ZBVEIyTmtNQzc1bUg5RzRmWWY1QQ?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPMVZONEsxU01Pa2dLUzZQWFFrM0VMQzJLWFQ1UzVkNW5zS0VIeDNCUDFYbmZMSWVnODBFWkJhLWVfWGNabFlTWEpicjYxcjItbHV5OE9pMkp2dzBKLUh3dFdGT0c5V19wWTBXQmVUQ3doNGRwa3BqalozWUx0M0lsVE9vdERua2Q1aGN2VWZzaVc3Zw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQMk5SZjNON1Z0X0dORHRoNk5NRjZuZjRabmZXTE1tRTA5V0hiTGFRdEJLZUhDQ1VQUFRoTC1HTnc1OU5ZUGtWUTc4eENadTVRRTRsWlRmUWhRa1FXVk1UTm85b0x6NmdrTGZYRUl2TzhGc2lLcGpsRl84NFpiU09vbDl4UVl5cUdWZUo3cEdKN3FPdGc0?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxPdDYyd2VndnhVdFI0ckxsUnVKbVRRaGxOMEoxOUpZTFcxeWJIdW5MbzlIWElaUW05RDdfNlM1b01jM3lFTkNCN184YzZwaU9PMWxOOVBKZkNrY2tGZldMc3U3THdNU0FST1ZKcmgtTF95ZlIwV3ZiYlBaVU12RXNoUjdIcVNBRGdnMldGUXllTXRxazY2SWNfZjZ0cks5T3p4LWppMUZqb1E3MWdpdThjVEU1OGNKdng4SUZHQndKalFVOTA?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQYUYtTUVGcVg1OEY2WFpMeXZWTmQ0XzB0NGNEdTRTcE5vdGhGaTd3Yzg1XzlLbmZMMTNHUmhGcGxFNXJyNjhmM01KdVU3ZlNsc09IT1o0UWdRSW1fZUdLVVY5UGZOTnVsRXZxUUMtelh0eVFXRUF3YWY4UlQ1OEhLNi1KSVBpcHl5VHRB?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQbzNoNElDckgyajBzR3NPZ0tkQ2taREVmc3p1NHZFZDBDT0dPY1NQa29vZElHZGhsQUcxQ2wxV1BGaDVpLXJTSjluQ0hNWWE5U1A1R3Ezc2lkTWZ5X3ZzU1VxV29CM0txQmFFT2xrdUg1bFUzaFV3bDAya2FkMFdBVjh1dEp6ZmZXZEZkWWpNRmY3eHNyVGs0dWNvUHplZWVLZzhZQng3cDdkRklKWjlJ?oc=5
- https://news.google.com/rss/articles/CBMi5wFBVV95cUxQbXpOQkVqZUlpMWkxZHFlX0tzTVZXY2d6MXdGSlFOZ1U1TTl6cmdnSG52U0VlSnlUZ2txTWhteEV2X1djZHJSU1NCcDhLMk15dFJOdUdtbkMxZTBubXFUaG45V0dBUHB0VTc5RDI0SnM1WlN3TnFCa09NY1owTkZZUlNDUE5INFZVWHJsc1VVYkFyNnVIUDIySGh5ZG5KSFJrS2dqY1NuUWRHQXNYX0tmRkRseThiZjdISVMta2psWmZvR2ZIRjFIb3JtMTN5dVczSDRtWFJNUUM4SDM1aVhINmlESzViNGs?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNTURldUZOaTN5Z1ZKN1FIUEhBdko2bTFoT2dmX0Z4Mk5vYlpUME1kbmtZNkFHRzRDWmVfZ3YtMWs4TFBGRU5pb0YzS0x1VjJvTUtTSGxRd3FBbHF2cjM2SEZYM2FueU5WVXdTbkgwWTZod1YxMlUzS0R1bWdfZWszM3pGN1dyR2dBbG1Pb19velJ6YThsUHhQU2dGd3lvVk9UbWp3TGVGNi1KT0RYam5ocTd6SnJUUldITUE?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQZy1QN3JZOEcxcXdFWkpkUWpycG5FMF9YQ1dkVW5ETV9IY0JILXYyQWRhSEtZMDFnNXpaM2ZjcEV2ZzU4YThBak92M2FsRXRSQVMwal9SUEVOODhPODgwTEdoOE5fOGtra0ZZb0ZWTUF4MnU0MGVwYWh2R0RpREhrN3JGcEF1cWJmeEd2NDNGV3hPaEZfbERzcUpPZ3J0SktYWVp3MWRqbnc?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNekRsZGVrS3pGUDBHdmNrOS1KREpLcUlEdmpDOElCcVk1RDB4WU5kdnM5ZTRLMzRsMU1MSm5tazAydTVPNWZ3aU0xa3F1RWV1M1VCYmpPeWEtSXpXTER5Smh4TGpGS3ZzSXhYU3FhMmgxUzVqazVLVlpKbmEyUE44ZmMzUUNHT3kxZHEwWUJJT1Y0Z3F6bW5vSmF5ajE4cTJBUXc?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPa05Cb1NpWEpwbmpNOVRNV3E4ZTZqNFFLTUhpNERwRWd5N2dlQkFIV05feGs0am5uSDFTWDAzNzRpRlYzdjVwdDdtaXQ5WGhyQTA1bURwT3AyMlpEV0F5LWY2MHpSUnM1SzZFaVN4bzdqdzRTYkY3bTh6M2FhWUk4TlVLUzQ5WVJuOGVtQVpCWUdDZw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
