# GOOGL Intelligence Report

- ticker: **GOOGL**
- Report as_of: **2026-11-12**
- Market data as_of: **2026-11-12**
- Quant sources: https://finance.yahoo.com/quote/GOOGL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GOOGL/key-statistics/
- AI analysis snapshot as_of: **2026-11-12**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-13T05:12:35.111091+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 5, 'ai': 13, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261112T054014Z-6c47e7f9/GOOGL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'positive_sentiment_in_headwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 10 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 36.0%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 298.7000 |
| Return 1D (%) | 1.7891 |
| Return 1W (%) | 5.7083 |
| Return 1M (%) | -15.3153 |
| Return YTD (%) | -4.3831 |
| Return 1Y (%) | 4.4529 |
| Annualized volatility (%) | 33.6050 |
| Beta vs SPY | 1.2822 |
| Max drawdown (%) | -30.6204 |
| Sharpe (rf=0) | 0.2986 |
| Downside deviation (rf=0, %) | 23.6359 |
| Sortino (rf=0) | 0.4246 |
| Historical VaR 95% (1D, %) | 2.9365 |
| Historical ES 95% (1D, %) | 4.7232 |
| Correlation vs SPY | 0.5240 |
| Tracking error vs SPY (%) | 28.8824 |
| P/E (trailing) | 15.60 |
| P/B | 5.57 |
| EV/EBITDA | 19.27 |
| Revenue growth (%) | 24.70 |
| Forward P/E (estimate) | 19.35 |
| Gross margin (%) | 60.86 |
| Operating margin (%) | 33.32 |
| Return on equity (%) | 44.29 |
| Free cash flow yield (%) | -0.03 |
| MA50 | 329.1156 |
| Close vs MA50 (%) | -9.2416 |
| MA200 | 338.4090 |
| Close vs MA200 (%) | -11.7340 |
| RSI (14, Wilder) | 42.2819 |
| MACD (12,26) | -13.2617 |
| MACD signal (9) | -13.8884 |
| MACD histogram | 0.6267 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GOOGL': 281, 'SPY': 281}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 298.7000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.7891 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 5.7083 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -15.3153 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -4.3831 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 4.4529 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.6050 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 23.6359 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4246 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9365 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.7232 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5240 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 28.8824 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.2822 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -30.6204 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2986 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 19.3520 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 60.8570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.3210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 44.2860 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -0.0317 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 15.5979 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 42.2819 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.6267 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -9.2416 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -11.7340 -> Clearly below the moving-average trend level.

## TAILWINDS

### Alphabet Climbs 3% as NVIDIA's Leadership Shake-Up Puts Google's AI Chips in the Spotlight; Microsoft Gains 2%, Amazon Ticks Up
- Summary: Alphabet Climbs 3% as NVIDIA's Leadership Shake-Up Puts Google's AI Chips in the Spotlight; Microsoft Gains 2%, Amazon Ticks Up
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi-AFBVV95cUxPN01iVHhIREJrc3F1cWwydjNTZG1oekcxc1hxLXhpczNmQlZPUk9IZnd3Q2pHTjh5OG1vRWdXOWRQT0ZXbUQ1WTNuTGdEd05NUHpLR2ZGcVh4al9ENkcxeTg4dlctdFhFN09fNTJhTF9LTUtnR2JlT1JvQU1YRkFvd1pWY1VuWGRaMGlYMEZPM3hFcklxWjl3NjBIYllfWHVEZ0xRNjA0Q1J1anF3ZU1QS01xUjNHWGNRWXB2M0FDWTQwUWdzM1R4OUpBM0l4b2NOWGpCX2pSdXVvUmxLbEI4bHBvc19kc2ZGdWQwSkdRZWpSeThZZWlucw?oc=5>

### Alphabet (GOOGL) stock is up, what you need to know
- Summary: Alphabet (GOOGL) stock is up, what you need to know
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxObjU0eTV0SzhZTnhLa20zOUtGeUFnZnh2TDc1T09MMXJFcUoya1BPLXVsUm5abjUxdHB5eTY3Z0Z5OVA2NWVuQndzaVRXOTI1X2sxME4ySHJOcXFLSFJtTWZUbWo1YlVGNmlsU3A0Uk05aDdscEk5SjhfTWRsQ2o3dUYyaGtUMFFXNHBrMU1FUnUtc2JicXJFWjBGaWhGR1dGdTBDVG5DcVpoa2c0Nmc?oc=5>

### Alphabet Climbs 3% as NVIDIA’s Leadership Shake-Up Puts Google’s AI Chips in the Spotlight; Microsoft Gains 2%, Amazon Ticks Up
- Summary: Alphabet Climbs 3% as NVIDIA’s Leadership Shake-Up Puts Google’s AI Chips in the Spotlight; Microsoft Gains 2%, Amazon Ticks Up
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQeUxVUGczQUl6QzBJeEt1N29mdHVLMHBoMUVjWmJjUHhkclB3YVNTSksxN05oZnZrUmlZV0Y5X0xhai1NcFRDZ0hlWl9vWlp2UTdXNTRUSDF0bktKeGFSdGg0WmJScUpHdEFvdUVKVkd3NVcxMHY4MHM4aHkwYURtM1Z0SHJBVkFqMHdWNkJPTWxiN1JXYzJsMy1oeDNYeHNt?oc=5>

### Alphabet Stocks Rise 0.34% as Google Lines Up $10 Billion Anthropic Stake Purchase
- Summary: Alphabet Stocks Rise 0.34% as Google Lines Up $10 Billion Anthropic Stake Purchase
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPc1A1VlA1M0tHb2xJN2VYeHJhSlBnNUJ3bzlqV0R5UGZ2VkJEbW5UUjlEMUlnLVk2NnI3bWxmTkdTQWFyOHpMenZTYzg2VlJySV9TR3Nlb2R1M2dqMG1HalZaOHJFMVkxTE5HMGdxaHhmZk9tYTk2UXBwR1VrUUItcHBXYjc3VS1BeFItUG9uMHRKNEh1?oc=5>

### Alphabet Edged Higher After Revealing a Pair of New TPUs for Agentic AI. A Bigger Challenge for GOOGL Stock Is Its Cash Flow.
- Summary: Alphabet Edged Higher After Revealing a Pair of New TPUs for Agentic AI. A Bigger Challenge for GOOGL Stock Is Its Cash Flow.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi-wFBVV95cUxNYVhqNnNpLVYxcDZtTHdFUnhMY211dmpic1IweVkwNUZURjJncGRnN1J5QklvUGl3Y2dZMnNmS21qNjRmaHJlTjlxdU5xb0s5NmNUcXVGc3BTTVZjZzRzOHAzNlVJNlpCSEcwSVlKM1g2QkhrVUgwMlVVNUJMbDdqMGcwa1c3eTFvcXI2OUVQR1Y4aVlpWTBDbGwySExQUmVhbEt4b1ZqdzZlTmF6dEdZY1pYR0t6RWJnUlBDaVZWMjFhX0RkZk9tNTJyYnlrZE0zemRjakJfQ1FvZHdLcTVwcXI0Q3ktdFB0M0FCLU5VOEQwSW1XNmRrZ3RCZw?oc=5>

### Alphabet Inc. (GOOGL) Is Part of a Massive AI Spending Race: Can the Investment Deliver Enough Returns?
- Summary: Alphabet’s AI investment may boost returns, signaling growth potential.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOY2N4MGZjMkpaLXRjN0N0RExnNmYtZjZhT0VyQU50cXRhMDF4RnpPM0RGMm1uZlBOVE1CSklDY0xqVWVfYU1UTlY4RHhlczRxMlZOWXIzQV84Ujd3dGtZUFRXV2V3S3ExeGFOZzhRaV9CLVQ1alFueWVndjFZV1ZmcDBFbzRlbV9kUDV5bndvQ1NzRkdIbkF0R3lfOA?oc=5>

### Alphabet Inc. (GOOGL) Is Seeing Its AI Investments Pay Off: Is More Upside Ahead?
- Summary: Alphabet reports AI investments are yielding returns, suggesting potential upside.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNb3o5b0Y4ZHIzSkdldmliN0VBZnpwVkJJY0VIVTVoNHBUUURpTGNvaFRmUEtmQWJmYnFpclpSdWhieFlwVHRJSVBkNVBJNmkyYnJrU2o4eWY0TWFNenVFVzZaZGRJaGVvb3JVemFxOVlETEtHZ2k0TGxWd0RWR3hzUmN0X2V6SVRFTld4dXY1OUwyRXhqZWxN?oc=5>

### How Low Can Alphabet Stock Go?
- Summary: Analysts discuss potential lower price levels for Alphabet shares.
- Date: 2026-11-12 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPSWpKUC0xMEFyM0pIMmVDVmN1SGQ0a3dDRng4XzFsOHVQM3paeVMwdkhibDMxdGNsS1Y4cTV1M3FvS2s5Y3RjV0pOTHBjajZIRzFQMFZDeDk0YjVMZzVFb0hicl9obTdQMzU4REUzQWlzWjFxclNjYWxTWGJUSFlvQjB1WXdQeE8wc3daTHByaWpaNU92RFE?oc=5>

### Alphabet Draws $5 Billion in Orders as AI Frenzy Builds
- Summary: Alphabet reports $5B in orders, indicating strong AI demand.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOaFJOMTVYNnlES1ZxSXJxcVg1SzFycEdEaDN5OGlKOFFGTHpCTjU3ZVp6NDZPY25yNmRncjlYc01fNWNucGNhU1Ezd0JOMDNrZ3lRdVZzT3BGUm5hMHJDWDdLYzM0THRCUWNYWUFyMFVCYWR0MkpEOGRkbVRBdVhpQWh5d0RfMXhoVHRoQ3NTSWxULV9nVWZtSFRtUQ?oc=5>

### Alphabet shares appear to have bottomed. How to play it for a quick rebound
- Summary: Alphabet shares bottomed, potential quick rebound indicated.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNVEdUUHd6WEdOZFlVRm5COXRVN0hLSXVyLXdzVTVhMjlibmdqMXJPRlp3WWJHc3NaWDlmcWRrUmJwNmJuNzFJLUt3Vm5PUXYxczM3bE9Calh5SXJRVk5JcGZTQVJZMXNsM1hOeVBHclFwQnM3U3JRS1NlaHZKWUNEaTd0Xzg2eVlYbW9NR3VwRnA0cElsNkJ6SS1PUUVZcnZINEdmbFZaZjJzLUN3R2ZrT9IBtgFBVV95cUxNOFBzMVVuSWFXcUcwMjU1NmJjdFh1NUF6emJWdldFSHBuYkVtR0Q4OTV5NWtRZXVqNlpiVTZEeFVOVWVoQzl2ZEJaaXRyaUw5bWRfR2ZCN2xkVnp6b1RQdGxhc2I2VUl4UUNvTzZ0TzFhMkh1d3Y2bXZBbWVuSnRQbFM3OEQyYzZidDBDRmpYTVlINTZzX25nbWJKVUxDNFJvUXoxZkE3c0pKaG1mSm1WVFpzdXBqQQ?oc=5>

### Alphabet (GOOGL) Sees $91.2 Million in Net ETF Buying on Nov. 10
- Summary: Alphabet attracted $91.2M net ETF buying, signaling positive investor interest.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOT1BIV3JJcnNrOE5nczNCUzhVVUdoRUplV0Nzb01PYjNkYlRMWHo5TmxiWV8ycHJVSE1PcEJ6SERldGFZSWNjcnBmN0lEUFBZWlVCSnRFM3o4NWxnQzZyZElnaWNaVG9WTVV6M1BPWUlfX2tCQkNxRGlsUzZaSVBkV2lKbERWYmlwT3JIdU9IY29wdFk?oc=5>

## HEADWINDS

### What's Going on With Alphabet Stock on Tuesday? - Alphabet (NASDAQ:GOOGL), Alphabet (NASDAQ:GOOG)
- Summary: Alphabet stock activity on Tuesday is uncertain, with mixed market signals.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNeWNyYXFOZlF0WkN3dFhPUkxBMU9FQnZudVBlVUNkQWFFZER6OUNMVzFIUlBTVFF3b3RtbHRZMlppWEROVlhwMHVrck1vNGN6NHV2cXYzU3NHT2o0M0U5Sk5pNHUxTEVjTkFWQVFKSVFhRGZrUllEMGd3NVFneWVNN3ZlV09WaHRUZ05TQmlTTFB3bHkwOGtLNlBfNWcwQXM?oc=5>

### ETFs Are Net Sellers of Alphabet (GOOGL) on Nov. 5
- Summary: ETFs sold Alphabet shares, causing a short-term sell pressure.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQY3lxNXZ5cHRiOTN4QXM2ZnZmTkNjNDlaRDB0aS1GMXBRZTZxUTZjSnBLaVBYaElZSlUyX0Z1Q2tERlpna0VZZ0kwbU54QlljLW5xMkluZzQ3R0Z0T1J4MVAzb3BSMl9ucW1iT3dwVER5UXBVLVpMU1BiZzlJRGxOM19lRFE3YlJXTWFuQjRmSmwycUE3N0VvYTlhT0w?oc=5>

### Why Alphabet Stock Was Moving Higher Today
- Summary: Alphabet shares rose today, reflecting positive market sentiment.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxQQ3FMT05oTFhaX2xsZTE3dEEyR3FEV2psTUpib3FqajRNLVVqei1IcGRqa2xXWk45WUF2M1FhS0FETkYwd2o5dkVMQXg2Q1p6TWNmWjRmVk5fMVNDcFpiSW9aQTNsLXU2bDVJRGtfdTVzemxSTFQ0RnBCNzY4eF9Bd0I0aVhuU29ob2w2UEVn?oc=5>

### Alphabet: Punished For Its Cash Flow, Not Its Business (NASDAQ:GOOGL)
- Summary: Alphabet criticized for cash flow issues, implying financial pressure.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOVlRzemNhVjZYcXBVSWNxZlJYeXdHVDBBN0xiR21ISUJDbXViM0U0NS1xakZNMWkzY2V3QlA3VGVDR0VtSms4b0hhYmc2bnV3Zy1OY2RfS3FKcWVreDhDUmFGZ1U5NmxfbjQ5NFluMlZsRW9XbWxhOXZfTHdvajBKVzJPbkVUUG1ycDhlOEFOSWJRUW51d0h6cg?oc=5>

## CATALYSTS

### Alphabet Stocks Rise as Google Commits $10 Billion to Anthropic IPO
- Summary: Alphabet shares climb after Google pledges $10B to Anthropic IPO.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxOaDhxbUFQYl9aLWJtTFdOZGhVdy1aU1R1N2tsa0p5RDh6eE9rNnJGWWlPX3EwWEpVRUEtUUdTb21ULUJWcTFFMFIwMnpxbnItdUwtU18wWXJfMjV6bzRRaEJUbzBIdXZnZ1hEbTZsSjBpSm1LZWJXWmhnZXBJamZvWFpyaWxzdG5mcjVVbA?oc=5>

### Nvidia and Alphabet Just Agreed to Buy $10 Billion Each of Anthropic Stock at Its IPO Price
- Summary: Alphabet and Nvidia jointly purchase $10B Anthropic stock at IPO price, expanding AI partnership.
- Date: 2026-11-11 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxNZ1NPRnN4V1I4SmpvVG5PU1FQYnUwMDA2Y3pOc1FRclg1cm1hR1hmR042TUFGYzNETTdPVlFJR2hWUVBCeXZMQ3g4bVhYYjB1R3FLdzVQZjNUUW85ZHNKZDBHTlBEc0VEUC1ud0pXR3U2VUZJZ1BfdnMyeVNJWDRTMWY0Yktwd0pWWGh5Qm1qX2hqT0lCMlo1ckI0MnNad0ZmWTdQS2c4ZldwcnE3VGZiczB5QmZPY3NyZWQzZkZ1YzNnLTk1M2Q4SmQwM21ub0NfeWc?oc=5>

### Alphabet Stocks Rise as Google Commits $10 Billion to Anthropic at IPO
- Summary: Alphabet announces a $10B investment in Anthropic, signaling strategic partnership and AI expansion.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxPcHZoWWx2MjVlcjctUlRxRUpFanZZSzhxd2dWMEtUYzhidHlZM3BZUUs4QzNlZ1lqcjJPVzFVOUhHZGhlRDlYNlBNS1BiNkpSRzhLbjJHN0ZuMGROZWpUZlQtNmpJa19LY2Rjbm9qSEZET3FlTTcyOTV4UVZaalM0TmptSGYwdV82SVM4SzFMelV4OGJZckdNM2U3QW9faXRSQzNkYk5vMVpDZy16dWY2ak9oWFMwaklINzZFVFNzYkRvaEJCVk5adg?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GOOGL** | **15.60** | **5.57** | **19.27** | **24.70** | **3,672,217,747,456.00 USD** | **4.45** |
| META | 21.28 | 5.85 | 14.00 | 26.10 | 1,594,466,631,680.00 USD | 2.74 |
| MSFT | 27.30 | 8.26 | 19.22 | 18.80 | 3,883,899,813,888.00 USD | 3.16 |
| AMZN | 21.62 | 4.71 | 16.78 | 12.10 | 2,891,865,653,248.00 USD | 9.52 |

Peers fetched as_of: 2026-11-12; GOOGL reuses existing data (market data as_of: 2026-11-12); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-12

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-29
- Revenue (latest available single quarter): 127,577,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 26,468,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi-AFBVV95cUxPN01iVHhIREJrc3F1cWwydjNTZG1oekcxc1hxLXhpczNmQlZPUk9IZnd3Q2pHTjh5OG1vRWdXOWRQT0ZXbUQ1WTNuTGdEd05NUHpLR2ZGcVh4al9ENkcxeTg4dlctdFhFN09fNTJhTF9LTUtnR2JlT1JvQU1YRkFvd1pWY1VuWGRaMGlYMEZPM3hFcklxWjl3NjBIYllfWHVEZ0xRNjA0Q1J1anF3ZU1QS01xUjNHWGNRWXB2M0FDWTQwUWdzM1R4OUpBM0l4b2NOWGpCX2pSdXVvUmxLbEI4bHBvc19kc2ZGdWQwSkdRZWpSeThZZWlucw?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxObjU0eTV0SzhZTnhLa20zOUtGeUFnZnh2TDc1T09MMXJFcUoya1BPLXVsUm5abjUxdHB5eTY3Z0Z5OVA2NWVuQndzaVRXOTI1X2sxME4ySHJOcXFLSFJtTWZUbWo1YlVGNmlsU3A0Uk05aDdscEk5SjhfTWRsQ2o3dUYyaGtUMFFXNHBrMU1FUnUtc2JicXJFWjBGaWhGR1dGdTBDVG5DcVpoa2c0Nmc?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQeUxVUGczQUl6QzBJeEt1N29mdHVLMHBoMUVjWmJjUHhkclB3YVNTSksxN05oZnZrUmlZV0Y5X0xhai1NcFRDZ0hlWl9vWlp2UTdXNTRUSDF0bktKeGFSdGg0WmJScUpHdEFvdUVKVkd3NVcxMHY4MHM4aHkwYURtM1Z0SHJBVkFqMHdWNkJPTWxiN1JXYzJsMy1oeDNYeHNt?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPc1A1VlA1M0tHb2xJN2VYeHJhSlBnNUJ3bzlqV0R5UGZ2VkJEbW5UUjlEMUlnLVk2NnI3bWxmTkdTQWFyOHpMenZTYzg2VlJySV9TR3Nlb2R1M2dqMG1HalZaOHJFMVkxTE5HMGdxaHhmZk9tYTk2UXBwR1VrUUItcHBXYjc3VS1BeFItUG9uMHRKNEh1?oc=5
- https://news.google.com/rss/articles/CBMi-wFBVV95cUxNYVhqNnNpLVYxcDZtTHdFUnhMY211dmpic1IweVkwNUZURjJncGRnN1J5QklvUGl3Y2dZMnNmS21qNjRmaHJlTjlxdU5xb0s5NmNUcXVGc3BTTVZjZzRzOHAzNlVJNlpCSEcwSVlKM1g2QkhrVUgwMlVVNUJMbDdqMGcwa1c3eTFvcXI2OUVQR1Y4aVlpWTBDbGwySExQUmVhbEt4b1ZqdzZlTmF6dEdZY1pYR0t6RWJnUlBDaVZWMjFhX0RkZk9tNTJyYnlrZE0zemRjakJfQ1FvZHdLcTVwcXI0Q3ktdFB0M0FCLU5VOEQwSW1XNmRrZ3RCZw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOY2N4MGZjMkpaLXRjN0N0RExnNmYtZjZhT0VyQU50cXRhMDF4RnpPM0RGMm1uZlBOVE1CSklDY0xqVWVfYU1UTlY4RHhlczRxMlZOWXIzQV84Ujd3dGtZUFRXV2V3S3ExeGFOZzhRaV9CLVQ1alFueWVndjFZV1ZmcDBFbzRlbV9kUDV5bndvQ1NzRkdIbkF0R3lfOA?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNb3o5b0Y4ZHIzSkdldmliN0VBZnpwVkJJY0VIVTVoNHBUUURpTGNvaFRmUEtmQWJmYnFpclpSdWhieFlwVHRJSVBkNVBJNmkyYnJrU2o4eWY0TWFNenVFVzZaZGRJaGVvb3JVemFxOVlETEtHZ2k0TGxWd0RWR3hzUmN0X2V6SVRFTld4dXY1OUwyRXhqZWxN?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPSWpKUC0xMEFyM0pIMmVDVmN1SGQ0a3dDRng4XzFsOHVQM3paeVMwdkhibDMxdGNsS1Y4cTV1M3FvS2s5Y3RjV0pOTHBjajZIRzFQMFZDeDk0YjVMZzVFb0hicl9obTdQMzU4REUzQWlzWjFxclNjYWxTWGJUSFlvQjB1WXdQeE8wc3daTHByaWpaNU92RFE?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOaFJOMTVYNnlES1ZxSXJxcVg1SzFycEdEaDN5OGlKOFFGTHpCTjU3ZVp6NDZPY25yNmRncjlYc01fNWNucGNhU1Ezd0JOMDNrZ3lRdVZzT3BGUm5hMHJDWDdLYzM0THRCUWNYWUFyMFVCYWR0MkpEOGRkbVRBdVhpQWh5d0RfMXhoVHRoQ3NTSWxULV9nVWZtSFRtUQ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNVEdUUHd6WEdOZFlVRm5COXRVN0hLSXVyLXdzVTVhMjlibmdqMXJPRlp3WWJHc3NaWDlmcWRrUmJwNmJuNzFJLUt3Vm5PUXYxczM3bE9Calh5SXJRVk5JcGZTQVJZMXNsM1hOeVBHclFwQnM3U3JRS1NlaHZKWUNEaTd0Xzg2eVlYbW9NR3VwRnA0cElsNkJ6SS1PUUVZcnZINEdmbFZaZjJzLUN3R2ZrT9IBtgFBVV95cUxNOFBzMVVuSWFXcUcwMjU1NmJjdFh1NUF6emJWdldFSHBuYkVtR0Q4OTV5NWtRZXVqNlpiVTZEeFVOVWVoQzl2ZEJaaXRyaUw5bWRfR2ZCN2xkVnp6b1RQdGxhc2I2VUl4UUNvTzZ0TzFhMkh1d3Y2bXZBbWVuSnRQbFM3OEQyYzZidDBDRmpYTVlINTZzX25nbWJKVUxDNFJvUXoxZkE3c0pKaG1mSm1WVFpzdXBqQQ?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOT1BIV3JJcnNrOE5nczNCUzhVVUdoRUplV0Nzb01PYjNkYlRMWHo5TmxiWV8ycHJVSE1PcEJ6SERldGFZSWNjcnBmN0lEUFBZWlVCSnRFM3o4NWxnQzZyZElnaWNaVG9WTVV6M1BPWUlfX2tCQkNxRGlsUzZaSVBkV2lKbERWYmlwT3JIdU9IY29wdFk?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNeWNyYXFOZlF0WkN3dFhPUkxBMU9FQnZudVBlVUNkQWFFZER6OUNMVzFIUlBTVFF3b3RtbHRZMlppWEROVlhwMHVrck1vNGN6NHV2cXYzU3NHT2o0M0U5Sk5pNHUxTEVjTkFWQVFKSVFhRGZrUllEMGd3NVFneWVNN3ZlV09WaHRUZ05TQmlTTFB3bHkwOGtLNlBfNWcwQXM?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQY3lxNXZ5cHRiOTN4QXM2ZnZmTkNjNDlaRDB0aS1GMXBRZTZxUTZjSnBLaVBYaElZSlUyX0Z1Q2tERlpna0VZZ0kwbU54QlljLW5xMkluZzQ3R0Z0T1J4MVAzb3BSMl9ucW1iT3dwVER5UXBVLVpMU1BiZzlJRGxOM19lRFE3YlJXTWFuQjRmSmwycUE3N0VvYTlhT0w?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxQQ3FMT05oTFhaX2xsZTE3dEEyR3FEV2psTUpib3FqajRNLVVqei1IcGRqa2xXWk45WUF2M1FhS0FETkYwd2o5dkVMQXg2Q1p6TWNmWjRmVk5fMVNDcFpiSW9aQTNsLXU2bDVJRGtfdTVzemxSTFQ0RnBCNzY4eF9Bd0I0aVhuU29ob2w2UEVn?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOVlRzemNhVjZYcXBVSWNxZlJYeXdHVDBBN0xiR21ISUJDbXViM0U0NS1xakZNMWkzY2V3QlA3VGVDR0VtSms4b0hhYmc2bnV3Zy1OY2RfS3FKcWVreDhDUmFGZ1U5NmxfbjQ5NFluMlZsRW9XbWxhOXZfTHdvajBKVzJPbkVUUG1ycDhlOEFOSWJRUW51d0h6cg?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxOaDhxbUFQYl9aLWJtTFdOZGhVdy1aU1R1N2tsa0p5RDh6eE9rNnJGWWlPX3EwWEpVRUEtUUdTb21ULUJWcTFFMFIwMnpxbnItdUwtU18wWXJfMjV6bzRRaEJUbzBIdXZnZ1hEbTZsSjBpSm1LZWJXWmhnZXBJamZvWFpyaWxzdG5mcjVVbA?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxNZ1NPRnN4V1I4SmpvVG5PU1FQYnUwMDA2Y3pOc1FRclg1cm1hR1hmR042TUFGYzNETTdPVlFJR2hWUVBCeXZMQ3g4bVhYYjB1R3FLdzVQZjNUUW85ZHNKZDBHTlBEc0VEUC1ud0pXR3U2VUZJZ1BfdnMyeVNJWDRTMWY0Yktwd0pWWGh5Qm1qX2hqT0lCMlo1ckI0MnNad0ZmWTdQS2c4ZldwcnE3VGZiczB5QmZPY3NyZWQzZkZ1YzNnLTk1M2Q4SmQwM21ub0NfeWc?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxPcHZoWWx2MjVlcjctUlRxRUpFanZZSzhxd2dWMEtUYzhidHlZM3BZUUs4QzNlZ1lqcjJPVzFVOUhHZGhlRDlYNlBNS1BiNkpSRzhLbjJHN0ZuMGROZWpUZlQtNmpJa19LY2Rjbm9qSEZET3FlTTcyOTV4UVZaalM0TmptSGYwdV82SVM4SzFMelV4OGJZckdNM2U3QW9faXRSQzNkYk5vMVpDZy16dWY2ak9oWFMwaklINzZFVFNzYkRvaEJCVk5adg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
