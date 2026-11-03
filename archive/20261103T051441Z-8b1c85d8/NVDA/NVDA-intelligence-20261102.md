# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:21:35.796956+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 2, 'ai': 16, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 13 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 29.17%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 202.0600 |
| Return 1D (%) | -1.2608 |
| Return 1W (%) | -6.4537 |
| Return 1M (%) | -13.6311 |
| Return YTD (%) | 8.5967 |
| Return 1Y (%) | 0.0267 |
| Annualized volatility (%) | 37.4029 |
| Beta vs SPY | 1.9348 |
| Max drawdown (%) | -20.1527 |
| Sharpe (rf=0) | 0.1286 |
| Downside deviation (rf=0, %) | 25.6599 |
| Sortino (rf=0) | 0.1874 |
| Historical VaR 95% (1D, %) | 3.8941 |
| Historical ES 95% (1D, %) | 4.5913 |
| Correlation vs SPY | 0.6633 |
| Tracking error vs SPY (%) | 30.4503 |
| P/E (trailing) | 25.54 |
| P/B | 21.31 |
| EV/EBITDA | 24.08 |
| Revenue growth (%) | 105.90 |
| Forward P/E (estimate) | 12.70 |
| Gross margin (%) | 74.67 |
| Operating margin (%) | 66.24 |
| Return on equity (%) | 117.21 |
| Free cash flow yield (%) | 0.86 |
| MA50 | 221.4362 |
| Close vs MA50 (%) | -8.7502 |
| MA200 | 204.1694 |
| Close vs MA200 (%) | -1.0332 |
| RSI (14, Wilder) | 33.3141 |
| MACD (12,26) | -4.4493 |
| MACD signal (9) | -2.6190 |
| MACD histogram | -1.8302 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 202.0600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.2608 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -6.4537 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -13.6311 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 8.5967 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 0.0267 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 37.4029 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.6599 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.1874 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.8941 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.5913 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6633 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.4503 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.9348 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.1527 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1286 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 12.6965 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.2370 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.2110 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.8569 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 25.5449 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 33.3141 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.8302 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -8.7502 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -1.0332 -> Slightly below the moving-average trend level.

## TAILWINDS

### Nvidia stock edges higher after SEC rule enforcement blocks unauthorized tokenized shares
- Summary: Nvidia stock edges higher after SEC rule enforcement blocks unauthorized tokenized shares
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNTnJwYmVQbk0zRndnTURTOURsb2tRUDhiRUpJaF9HaWFabDh1c0VqWXdlMzcwX1NNbGQ3cWZ1TXVCQWFCZUx2bVRqUFMwaGVlVWc3Q3NiOHhTSkptQ1dUZTlGZlVpTzdCM1BCQ2xxekRNZnVWZ2hPN1NtZWdQamVvNUlqTXhmdU12WC1oZUtCZ0czdw?oc=5>

### Nvidia Stock Looks Surprisingly Cheap. Why NVDA Could Rise 61%.
- Summary: Positive market sentiment suggests potential upside for NVDA shares.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQYjA4NDQtRjBtaDZMX05LdkpMeWZrOVYxWFc2TTgtU0phdXlnc1RvZlJVb3NxWjlfbnkwY3VIOXpvZWpzUklKWEh3LTF6NVBxLWs3OWlsVDY2bXpwa2MwZXczNDhXelFzYUNfWHhwaDVKSnhWZnZDQ1FiRWN4TUNjUVdsaHNHWjJCMDNmbFR0SHFscGpZekx4b21zYmZ5aDVsSkF2UTRmQQ?oc=5>

### Bank of America Analysts Maintain Bullish View on Nvidia (NVDA) Amid AI Demand and Election Uncertainty
- Summary: BofA analysts remain bullish on NVDA, citing strong AI demand and election uncertainty as supportive factors.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxPSXJQaVRhR3ZkZEpFWWlYX3N4OWZwQV9EMVhTdkFVWUhSMVdkdlRWZXRRMVNhZjBPQTBwYWcweks0dGJVRzZmUFhhVEg4ckRsSTQ2aE15QUdpZVJzS1ExYVBEU3F1OVNGQUxKNjNHMjg4X1hLcUJJNndFUEo0VDdUZTZyOGJ6Uml3VHd3MWgzX3VMTUhvemxJSkI2bDNnaFlSbGJ5R0hKLXY2dGozOUtVZ3puX2RDQ3BvWUtrOEh3emlhamN2ZVp1VHlja3hSQXBxUWRKV0FGRQ?oc=5>

### Meet the Spectacular Vanguard ETF With 44.6% of Its Portfolio Parked in Nvidia, Alphabet, Apple, and Microsoft
- Summary: Vanguard ETF heavily allocates to NVDA, indicating institutional confidence and potential upside support.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQRDdWWXJhS3d4bDdMUldCUWxrdS03NWFubzVpNDFnNnlPcjVKczNuaDhkekc0NFpuQUhPU0xlWDF5WVFDUUtBWlA5eXNZQ3RjTXJMTGtlLWkzOWxBZXNnVUNnQi12RTN3cFZuYjB6c2NlNm9OdTBrMU5pZGEwbUNVRkE1MjA0akFFNEVmN21Za0FmMW5v?oc=5>

### NVIDIA (NVDA) Stock Analysis – Entry & Exit Strategy
- Summary: Provides entry and exit guidance for NVDA investors, suggesting strategic trading opportunities.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTE5IUDFwNTU0N2FMNDluR1o0Z0dqNElaMWRna1hWYVFTa3BiYW9udEtZa1RsU081czNoS2ZVa0VpMjlLOUZvcXRyVWh2Si15bGpDMWh4clcxbldTQU1uRFZQN3ZiNVp4bjVsWEtNUXJkX2R3ZXRLUFk2anRpSWI?oc=5>

## HEADWINDS

### NVDA Stock Drops: Nvidia May Back Data Center Loan For Its Own Customer, Analyst Sees Little Impact From Intel’s Weak Report
- Summary: Stock fell after announcement of potential loan backing, indicating a short‑term negative market reaction.
- Date: 2026-10-30 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQTGdFWTJ1Wm1ISjFPRjVLdVowSFF0RHpiODd4cldVU1VEX3FUU1VFc3hROVlzM3Nsd0RONGE2emNfZ1hsTm9MUUNUR05IWFFnVTJpeEV4TjMzRTZ5eG1scm0yT1VOTWF1X2F1VmoxeG9NaUJqa1hKX0JlbDhGVmY5dEhZcUc0d2hBMGdNUWo2eDdyMlJ0Y3dZ?oc=5>

### Seaport Reiterates Its ‘Sell’ Rating on Nvidia Stock as Competition Is ‘Mounting’
- Summary: Seaport’s sell rating signals increased competition, potentially dampening Nvidia’s market prospects.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxQN200NHVhcmVraEtRODN6b0ZnWjdjNlQxY3BxbkVzajV1Z0p0ZGc3SUtLUFVya1JmTTRMX1hPdWs2Ym5XMEtBZTJhS1hxbnBiV3VNZjdGNTljbkltRUYwZ3dOaGtfaVl3UFNTSzZEeUExMjZYMXhWT2dpZ1pvSkd1bV91TUVvUVVQQ2J3Smx4WTRkMjdReUF0R0xWcjExUmM5MUZsRg?oc=5>

### Nvidia stock valuation gets torched by tech stock rout
- Summary: Negative market move impacting NVDA valuation.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNcGZseDhYeDZxTDFzcm9tLVdXRlo0RzdnTzR6U284RVFhTW1Rc09WU2R6TG1iODczZUQ0RUdPTDdPR09CajZWc0tNMV9laGxQZktza2RtZXRKTE5YT0xfY2FFWFRmVTkyWUxnb251UEJ5TWV5UFJ0VzU1LVgtTzEyZ0RjcURPUXItdEc2YzdSREtuRGZhVUlHQ3JMbWNOZmllc1RzNUphcFBRSjFTakZrT0dpTENVMFhFVVE?oc=5>

### Nvidia Flashes Sell Signals As Earnings Loom; Is Nvidia A Buy Now?
- Summary: Negative sell signals ahead of earnings.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQNlNYZi1HUzQyS0s4YlN6TUtGZG5JYXI3VXQ0cW1hNjhzNzlmQ2JSdGxSWTBuX1JiMW04LUVTcFptOE9ORjY1YjJRNG15cVpyaHBzVGZ0X3FLeGRyUUg0OVRlNWcwNUlCNzJ6ZWUtdEYtc0wyMFlIMzR4QjVlOHRwcHRKOFNoMnRQZjVOcg?oc=5>

### Why Nvidia Stock Took a Dive Today
- Summary: Recent decline in NVDA share price.
- Date: 2026-10-30 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxQZWpnVVNKVXlKQzRrdEl1SmhxZWVWd2ZFZjlEdUxCU1NCal91ZHpWVlo4NnE4WnlvQzVUVkhIVkdpVXRRSWUtcDQ3YThveWU1WnlQQ3VBMDk0aDhmMFRUV2VxcUxOT2pmZlp2WmpZSnpnczQtLVAzXzkyVTNGQXY2X242NA?oc=5>

### Nvidia Stock Is Rebounding but Stock Chart Is Really Ugly
- Summary: Nvidia shares rebound, yet chart remains unattractive.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxNTVM2cFd2cHpQRW5qUmlXUGhLMlBHTUc5aVgtSTNGZFNDcGZXM3N6aUR6ZVVCZ3ZUSkdwRi15d2lhOHJTWXAxc2N0RXJ6M0x3U3hBVk5yTktPcS12Rl85b3d0aUN5cVpSUEJaTFlWM2ItUloxcEExTHN1cU9ienBTak5DeDQ?oc=5>

### Why is NVIDIA stock climbing today?
- Summary: Explores reasons behind today's rise in Nvidia stock price.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNVXdoSFFaUF8zM2tBTEs4SGlRM25wMk1VSUtOMUFLQW5ZTVRReS1fVDdUM05vQkR4TFFpcUZTX3JsanlxM29VR213eTF0RklSYWNCeVpRUksweERPNGZTZ2J5ZEg4UlV1c3JTSDVDUHdRdktWNlB0TGM5NEF0V1V1bnAxeGhkUGVZaDE1YjRZQzhxVUtXbWh4cHpqN0c?oc=5>

### Nvidia (NVDA) Falls More Steeply Than Broader Market: What Investors Need to Know
- Summary: NVDA shares dropped more sharply than the broader market, raising concerns about short-term volatility.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNNjROdjdjOVlRX3RIOVVXbDVmSm0yTkJDZUZOcDY3NlJTLXFjSFFTV1A1SHVYeVIxeWw2R1B1anVKaDl0R3RLYmxqTVRiX2hQT18tbm5lVVNBdE9CU3JUZnY3MlBMNDBwSHFDNlJPX2JsdXEtcFdDOVJRNDhFQXg3aXNEX09yck9UbC1vXzZSNmE3cmQ3NHE2Q3o2Yw?oc=5>

## CATALYSTS

### NVIDIA Stock: Analyst Estimates & Ratings
- Summary: NVIDIA Stock: Analyst Estimates & Ratings
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNS3F4WldNbXdBemQ2d2I5OUZkQmJrYTdFcUZGRHpCSlV3TDlQSjZVbzRsMUFXWmh4M2RIYjRKUERieUhBUkN2Ym9ENElqZ19JWEtLWHkyaEZBTTRYemR1MVR0WHltSlNpN0tZcy1vTE0yRTJUVGdlckNxX0JNeVRZdlpqbEFTUHcwci1FZEhCOUtQM19FRG9WNERqa0Uxd293a1lKSHpR?oc=5>

### Can You Make Money Off NVIDIA Stock Now?
- Summary: Discusses current NVDA stock valuation and potential returns.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQd3NKR0JBQldHLU45bXdMd1g3ZFBDby0tMURjdVNBelJOUW9OcXJfUmJ6cFN4NkdXUHo5Zkk3Z1pyeHRTMTdfTWNVY3prZmptVEJ2NHdGUmJrVEVGQ2xQUGIxZUs1dTk5Q09rWlRsRGt3UHM0YmdoaERWblc1dzF2RlJURHRyRnZCSi1WekRiazFaVDhEc0VMdFR3Q3V0MjJBaVE?oc=5>

### Nvidia, AMD, Marvell Targets Cut: Melius Pulls Back on AI Stocks as Big Tech Lines Up to Raise Cash
- Summary: Analysts cut targets for Nvidia, AMD, Marvell amid AI stock pullback.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxPdmFVNG00aDdBdENWS1RKQmJYMzdKaUpwVGEzS05BbzZEdGY1cDV1MFplNWROcFpXQ0ctMEN0d2hCUmEwclFucHJaTDd4NmlGbTNxWTdFTmxzekJSTG9zWVA4VE5mRDlpMFpuMFc4UEpUbGl5S1NsV1RzR01JdnVMeE9nR3llVHFWUnVuY09iTGZzdkg4R0lLWnJIc0ZMSmVVYjVNX0ZZODJpNW54Q1B5ZzVYajVYVHJnRk1uUFAxbzI?oc=5>

### Nvidia Reports Nov. 17. History Says What Its Stock Usually Does Next.
- Summary: NVIDIA releases its earnings report for the period ending Nov. 17, potentially influencing short-term stock movement.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPbGJJZXFlWmhxcWo4RHFDWXFyN1JkcER6LW11MkZNaUpqb09hLS1ycVEzcjFVUkdwbjFxdzRQaEVrdTlUa1NVNlZ4ZDJVMUpfVHQzdlVHdE1zRVptbm9CSVh1R2hqSHBUYy1HMGQyencySVZnWV82VVBlNlJ4eC1HYTZmMzBaX0JXSGw0NEpWNkt6eUY5ZkRfOTZmTUxuakxscGZuRU5nVVZLLXl3X3Bv?oc=5>

## RISKS

### Nvidia (NVDA), Costco (COST), Nike (NKE) join OKX–ICE tokenized stock objections, bringing total to 50
- Summary: Nvidia joins 50 companies objecting to tokenized stocks, raising regulatory concerns.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxNT2JRbThULWtaaVVVeGEyVlZPSTQ0alVKSk1Qc2VKRGppaHVtSFoyM3Uzam1jWE1iVXFsT0dTNmFuTWJhQ3d1ZXZ6dWc3X0RvaVBSeGV5MTNvNm9MdmtyYWVNcmlkRWNMbWttQ2JQTzdEVlZ2SW5UZDRQZnJpOWtsN0V3dmtXaVdTOEZWZm5MeGpoRXZ3NjFHOGZkWEZSc2FObEZFT2hWSk1iYmZJSWxDamlQbWxFN0ppTzRv?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **25.54** | **21.31** | **24.08** | **105.90** | **4,879,142,617,088.00 USD** | **0.03** |
| AMD | 119.09 | 11.33 | 78.78 | 50.10 | 762,104,643,584.00 USD | 82.27 |
| AVGO | 41.63 | 15.43 | 30.11 | 85.50 | 1,538,206,859,264.00 USD | -12.18 |
| INTC | N/A | 2.77 | 17.32 | 20.90 | 318,740,529,152.00 USD | 49.96 |

Peers fetched as_of: 2026-11-02; NVDA reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-26
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-26
- Revenue (latest available single quarter): 96,221,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- Net income (latest available single quarter): 59,688,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMikgFBVV95cUxNTnJwYmVQbk0zRndnTURTOURsb2tRUDhiRUpJaF9HaWFabDh1c0VqWXdlMzcwX1NNbGQ3cWZ1TXVCQWFCZUx2bVRqUFMwaGVlVWc3Q3NiOHhTSkptQ1dUZTlGZlVpTzdCM1BCQ2xxekRNZnVWZ2hPN1NtZWdQamVvNUlqTXhmdU12WC1oZUtCZ0czdw?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQYjA4NDQtRjBtaDZMX05LdkpMeWZrOVYxWFc2TTgtU0phdXlnc1RvZlJVb3NxWjlfbnkwY3VIOXpvZWpzUklKWEh3LTF6NVBxLWs3OWlsVDY2bXpwa2MwZXczNDhXelFzYUNfWHhwaDVKSnhWZnZDQ1FiRWN4TUNjUVdsaHNHWjJCMDNmbFR0SHFscGpZekx4b21zYmZ5aDVsSkF2UTRmQQ?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxPSXJQaVRhR3ZkZEpFWWlYX3N4OWZwQV9EMVhTdkFVWUhSMVdkdlRWZXRRMVNhZjBPQTBwYWcweks0dGJVRzZmUFhhVEg4ckRsSTQ2aE15QUdpZVJzS1ExYVBEU3F1OVNGQUxKNjNHMjg4X1hLcUJJNndFUEo0VDdUZTZyOGJ6Uml3VHd3MWgzX3VMTUhvemxJSkI2bDNnaFlSbGJ5R0hKLXY2dGozOUtVZ3puX2RDQ3BvWUtrOEh3emlhamN2ZVp1VHlja3hSQXBxUWRKV0FGRQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQRDdWWXJhS3d4bDdMUldCUWxrdS03NWFubzVpNDFnNnlPcjVKczNuaDhkekc0NFpuQUhPU0xlWDF5WVFDUUtBWlA5eXNZQ3RjTXJMTGtlLWkzOWxBZXNnVUNnQi12RTN3cFZuYjB6c2NlNm9OdTBrMU5pZGEwbUNVRkE1MjA0akFFNEVmN21Za0FmMW5v?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTE5IUDFwNTU0N2FMNDluR1o0Z0dqNElaMWRna1hWYVFTa3BiYW9udEtZa1RsU081czNoS2ZVa0VpMjlLOUZvcXRyVWh2Si15bGpDMWh4clcxbldTQU1uRFZQN3ZiNVp4bjVsWEtNUXJkX2R3ZXRLUFk2anRpSWI?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQTGdFWTJ1Wm1ISjFPRjVLdVowSFF0RHpiODd4cldVU1VEX3FUU1VFc3hROVlzM3Nsd0RONGE2emNfZ1hsTm9MUUNUR05IWFFnVTJpeEV4TjMzRTZ5eG1scm0yT1VOTWF1X2F1VmoxeG9NaUJqa1hKX0JlbDhGVmY5dEhZcUc0d2hBMGdNUWo2eDdyMlJ0Y3dZ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxQN200NHVhcmVraEtRODN6b0ZnWjdjNlQxY3BxbkVzajV1Z0p0ZGc3SUtLUFVya1JmTTRMX1hPdWs2Ym5XMEtBZTJhS1hxbnBiV3VNZjdGNTljbkltRUYwZ3dOaGtfaVl3UFNTSzZEeUExMjZYMXhWT2dpZ1pvSkd1bV91TUVvUVVQQ2J3Smx4WTRkMjdReUF0R0xWcjExUmM5MUZsRg?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNcGZseDhYeDZxTDFzcm9tLVdXRlo0RzdnTzR6U284RVFhTW1Rc09WU2R6TG1iODczZUQ0RUdPTDdPR09CajZWc0tNMV9laGxQZktza2RtZXRKTE5YT0xfY2FFWFRmVTkyWUxnb251UEJ5TWV5UFJ0VzU1LVgtTzEyZ0RjcURPUXItdEc2YzdSREtuRGZhVUlHQ3JMbWNOZmllc1RzNUphcFBRSjFTakZrT0dpTENVMFhFVVE?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQNlNYZi1HUzQyS0s4YlN6TUtGZG5JYXI3VXQ0cW1hNjhzNzlmQ2JSdGxSWTBuX1JiMW04LUVTcFptOE9ORjY1YjJRNG15cVpyaHBzVGZ0X3FLeGRyUUg0OVRlNWcwNUlCNzJ6ZWUtdEYtc0wyMFlIMzR4QjVlOHRwcHRKOFNoMnRQZjVOcg?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxQZWpnVVNKVXlKQzRrdEl1SmhxZWVWd2ZFZjlEdUxCU1NCal91ZHpWVlo4NnE4WnlvQzVUVkhIVkdpVXRRSWUtcDQ3YThveWU1WnlQQ3VBMDk0aDhmMFRUV2VxcUxOT2pmZlp2WmpZSnpnczQtLVAzXzkyVTNGQXY2X242NA?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPNzZBOEVPMWhVUV83Q1lVMEEyTFotVlgyT3pzWV9rdHFDaWRfNlZid3NjLUFXa1Z6MFJfUW5WVWdnUHVHRVlLUk5CTUUtTkdsSkRIdzB2S2NTOGNYSGRxcHIzN0tjLW5TUzdzWjZnTmk1VFpEWWlrV3NFeTRaNzU1cjJSb3VuRURBNXhXMXAwS3NZTTBJRWc?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxNTVM2cFd2cHpQRW5qUmlXUGhLMlBHTUc5aVgtSTNGZFNDcGZXM3N6aUR6ZVVCZ3ZUSkdwRi15d2lhOHJTWXAxc2N0RXJ6M0x3U3hBVk5yTktPcS12Rl85b3d0aUN5cVpSUEJaTFlWM2ItUloxcEExTHN1cU9ienBTak5DeDQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNVXdoSFFaUF8zM2tBTEs4SGlRM25wMk1VSUtOMUFLQW5ZTVRReS1fVDdUM05vQkR4TFFpcUZTX3JsanlxM29VR213eTF0RklSYWNCeVpRUksweERPNGZTZ2J5ZEg4UlV1c3JTSDVDUHdRdktWNlB0TGM5NEF0V1V1bnAxeGhkUGVZaDE1YjRZQzhxVUtXbWh4cHpqN0c?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNNjROdjdjOVlRX3RIOVVXbDVmSm0yTkJDZUZOcDY3NlJTLXFjSFFTV1A1SHVYeVIxeWw2R1B1anVKaDl0R3RLYmxqTVRiX2hQT18tbm5lVVNBdE9CU3JUZnY3MlBMNDBwSHFDNlJPX2JsdXEtcFdDOVJRNDhFQXg3aXNEX09yck9UbC1vXzZSNmE3cmQ3NHE2Q3o2Yw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNS3F4WldNbXdBemQ2d2I5OUZkQmJrYTdFcUZGRHpCSlV3TDlQSjZVbzRsMUFXWmh4M2RIYjRKUERieUhBUkN2Ym9ENElqZ19JWEtLWHkyaEZBTTRYemR1MVR0WHltSlNpN0tZcy1vTE0yRTJUVGdlckNxX0JNeVRZdlpqbEFTUHcwci1FZEhCOUtQM19FRG9WNERqa0Uxd293a1lKSHpR?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQd3NKR0JBQldHLU45bXdMd1g3ZFBDby0tMURjdVNBelJOUW9OcXJfUmJ6cFN4NkdXUHo5Zkk3Z1pyeHRTMTdfTWNVY3prZmptVEJ2NHdGUmJrVEVGQ2xQUGIxZUs1dTk5Q09rWlRsRGt3UHM0YmdoaERWblc1dzF2RlJURHRyRnZCSi1WekRiazFaVDhEc0VMdFR3Q3V0MjJBaVE?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxPdmFVNG00aDdBdENWS1RKQmJYMzdKaUpwVGEzS05BbzZEdGY1cDV1MFplNWROcFpXQ0ctMEN0d2hCUmEwclFucHJaTDd4NmlGbTNxWTdFTmxzekJSTG9zWVA4VE5mRDlpMFpuMFc4UEpUbGl5S1NsV1RzR01JdnVMeE9nR3llVHFWUnVuY09iTGZzdkg4R0lLWnJIc0ZMSmVVYjVNX0ZZODJpNW54Q1B5ZzVYajVYVHJnRk1uUFAxbzI?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPbGJJZXFlWmhxcWo4RHFDWXFyN1JkcER6LW11MkZNaUpqb09hLS1ycVEzcjFVUkdwbjFxdzRQaEVrdTlUa1NVNlZ4ZDJVMUpfVHQzdlVHdE1zRVptbm9CSVh1R2hqSHBUYy1HMGQyencySVZnWV82VVBlNlJ4eC1HYTZmMzBaX0JXSGw0NEpWNkt6eUY5ZkRfOTZmTUxuakxscGZuRU5nVVZLLXl3X3Bv?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxNT2JRbThULWtaaVVVeGEyVlZPSTQ0alVKSk1Qc2VKRGppaHVtSFoyM3Uzam1jWE1iVXFsT0dTNmFuTWJhQ3d1ZXZ6dWc3X0RvaVBSeGV5MTNvNm9MdmtyYWVNcmlkRWNMbWttQ2JQTzdEVlZ2SW5UZDRQZnJpOWtsN0V3dmtXaVdTOEZWZm5MeGpoRXZ3NjFHOGZkWEZSc2FObEZFT2hWSk1iYmZJSWxDamlQbWxFN0ppTzRv?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
