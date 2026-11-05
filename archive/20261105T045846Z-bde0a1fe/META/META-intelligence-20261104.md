# META Intelligence Report

- ticker: **META**
- Report as_of: **2026-11-04**
- Market data as_of: **2026-11-04**
- Quant sources: https://finance.yahoo.com/quote/META/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/META/key-statistics/
- AI analysis snapshot as_of: **2026-11-04**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-05T05:13:40.922760+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 2, 'ai': 16, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261104T044411Z-6b13f9ec/META** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 10 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 31.82%; oldest publication 2026-11-01

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 630.0000 |
| Return 1D (%) | 1.4444 |
| Return 1W (%) | 2.8588 |
| Return 1M (%) | -13.4710 |
| Return YTD (%) | -4.3128 |
| Return 1Y (%) | 0.7679 |
| Annualized volatility (%) | 41.2355 |
| Beta vs SPY | 1.4194 |
| Max drawdown (%) | -28.7332 |
| Sharpe (rf=0) | 0.2226 |
| Downside deviation (rf=0, %) | 27.3515 |
| Sortino (rf=0) | 0.3355 |
| Historical VaR 95% (1D, %) | 3.6289 |
| Historical ES 95% (1D, %) | 5.6251 |
| Correlation vs SPY | 0.4419 |
| Tracking error vs SPY (%) | 37.3801 |
| P/E (trailing) | 21.19 |
| P/B | 5.91 |
| EV/EBITDA | 14.14 |
| Revenue growth (%) | 26.10 |
| Forward P/E (estimate) | 17.70 |
| Gross margin (%) | 81.03 |
| Operating margin (%) | 35.41 |
| Return on equity (%) | 32.26 |
| Free cash flow yield (%) | 1.05 |
| MA50 | 673.3910 |
| Close vs MA50 (%) | -6.4437 |
| MA200 | 631.3620 |
| Close vs MA200 (%) | -0.2157 |
| RSI (14, Wilder) | 40.1334 |
| MACD (12,26) | -22.2569 |
| MACD signal (9) | -14.5152 |
| MACD histogram | -7.7417 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'META': 275, 'SPY': 275}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 630.0000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.4444 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.8588 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -13.4710 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -4.3128 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 0.7679 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.2355 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 27.3515 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3355 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.6289 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.6251 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4419 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.3801 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.4194 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.7332 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2226 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.7027 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.0340 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 35.4140 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.2640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0460 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.1907 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 40.1334 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -7.7417 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -6.4437 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -0.2157 -> Slightly below the moving-average trend level.

## TAILWINDS

### Investors Are Beginning to Say That Meta Is The Best Buy And Hold Stock Through 2030
- Summary: Highlights investor sentiment favoring Meta as a long-term hold.
- Date: 2026-11-03 | Impact: low | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQekVac0tXM3pEX253R1RuMlJoeXlHUEc5T0dIeHEwVkJQOHZ0SWI1XzlNWk5EZURWbl9xOEQ2Um5mTE1KeDhuMkIzTG83aGhPQ2R4WGFSMmctT0laR2VIOVRUUXg0NllPMU9TMlRpRWx5TUJPcVNLc1U5SWp2WnJEdHlqZHdZU0FLYk9Lc2h5OFMyMjEyUWdrSS1BMWpKa1U?oc=5>

### Meta Platforms, Inc. (META) Is Spending Billions on AI: Will the Bet Pay Off?
- Summary: Meta invests billions in AI, potentially boosting future capabilities.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQOXBqcHhOdEM3MkZxZG5aOVJqbWY1ZF8zYXJSMnhXb2JqZWpkNGVTU01nbERXeFdoQnZkTm9NN3htVVktME1VVF9DcVlQdHQ5R1Mta1NYbU5xX21RYkNlTE9BNjFlY21kRlRjTzRnVG9GLTFyNzgyYW96MTE0VVRVQ2ZaMnJGZXBIM1RRdFJiU0tHTjVKUFNBYkluY1U?oc=5>

### What Is Going On With Meta Platforms Stock on Monday?
- Summary: Meta’s stock movement on Monday is discussed, highlighting potential market dynamics.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQWW1uaWJkbk9BMm5MZnh4RG5IVGFsTV81MFJyRFhKR3k1N3c0OVRWRlkzSFJUY1FheGpmVkplZ0xCN1JMMVFhSDhqdHIxN0Q3bEw3ZnBSSWxpV3BJMzN2UDVqMGRfRDRaSFJXWXZheU8zeXVRX1VmcmI2WG9HdVpuRDcyVmVFMEJNZzAzVUlCZGRRcUNFUU1BUTRwSzkxaEk?oc=5>

### The Nasdaq-100 Is Outperforming Nvidia, Microsoft, Amazon, Meta Platforms, Alphabet, and Tesla This Year. Here's My Favorite Low-Cost ETF to Buy the Dip.
- Summary: Meta’s inclusion in Nasdaq-100 outperformance noted, suggesting broader market sentiment.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPRHVTVGF6UWh0bW5RTmZVRlozWU9KU3J1QURKQXJQMzlRTjA3c0lFQ09HZldGYkNiYkFDYnB5cFVfcWNwempXRl9NUDd5cXpFQy15eEE0OXFGTENYRFVaaVM4dEVzSkhwQ0h0eFRrMDkySHRFUE9hUWxPbjlXVnpsY2VfaGMtVlA4MmhXbmNYQl91cWdxRW9aSg?oc=5>

### ETFs Are Buying Meta Platforms (META) on Monday
- Summary: ETF purchases of Meta shares on Monday indicate institutional interest.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxObXlMMUZPdTgwelhHYnVDZXBuMHlFNGNWZHp5ZTNpTE5iVkxTODFRcWoyNUtrOHRlcC01QmxOZ0JOS0RzS1J1c0RwdkpBcFoxMW8xRVNTVllXbGVjUjd6eFNKdThtVnhHQmV0alRrM0REQUVBbW1lZDlITEJhWlZndjJqTi1uRFRBamxPaG51Sktld3ZRVkRtYVlqZEs?oc=5>

### Meta (META) Stock Could Trade At A Discount Despite AI Spending
- Summary: Meta’s stock may trade at a discount due to AI spending concerns.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxNUGZ6dUhvNEpRZFpmcXVSMUZST0hqUFFFb0lGZnZ6MzJrU3JPWlpscXFxbTRpZHRuTVV5QWtQbHFwSGxpS09lYldid2lheDN4V1NncHZvNUVUaXNfSHVwT3RyeWpYWXh3MDJpZDBDRGNSTlJ4QmhLVVdmM0owWndKX2pFdmM4eERkQ0tzajZDSEs0a2lGakhqR2cyN3hOcUxmdTRkYl9SZkEzclZpanUxUktvd0Vsb0lYT0R6aGpVMnltWFpqOWFaMW5R0gHPAUFVX3lxTE0weVVCaGg5RDZOcEc0OGpjV1djTjN3NmZHa2pNU2dZTG1RZXNYZjd4V3JWYmhSb3J1ZTY1TlByRjJPOFJXdnBWN3p4YjBVYmU5Mkd0TGY4UjZDRnF2Q2lxM2ZzdC13TmIycURreXBVUkhvSjJoVU43aDUydGVxWHAxSng5ZGZUUi15X2l5NzV1clNvVXlYdXJiRGpmQjNmX19rVlQ1RE41b3A2UzVFSElucGZCOTBJMDhFNUxiWmFxMlVWcFEzdC1nVVc0dkdWZw?oc=5>

## HEADWINDS

### Meta Shares Are Down Since Earnings. Is the Stock a Buy?
- Summary: Meta Shares Are Down Since Earnings. Is the Stock a Buy?
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQamFKWmVYLUc0VkRSZ3U2anMwaXJBVWNsM251R0UwVUpSUDBLM29LeDhGTGlLOEJUVDR2SDVGRGxFUFRfX3hQOUR2NXI5OGhibWVldkw1eWktYkRuTWY2T09fRFhoNXBxRE9sTFYxTlB2Rm9OYXhPNC1QQnNreXNFeEdkaDRjOFhHRHZ4d0FaN3JPMF8zRnlz?oc=5>

### Meta Stock Slips as S&P Delivers Stark Warning Over AI Spending
- Summary: Meta Stock Slips as S&P Delivers Stark Warning Over AI Spending
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNM0tTajVlck0wTDZTRk8zN2tTQndHRFNLd0I2OGFfdU5TTjZ2WHE4SXVFTkZiT0tJN2RQb1RLcURQRnlEeWVFZHhXR0FlbHZlQ2d2OFE0NkdTUFQ0OUhkMkEwMmQ2R0cyZWdleV9hWXJKRkIxSW1OQXd5RldaMDl3LWZFXzZ2Mm1kX0lSakRVeHEzT0VvRkFvZlY2cW1FRHNwX3RKTUEzSUE5MUJWaDJOZHVMWXFaZWpleG9oUkRuX1E?oc=5>

### Meta Platforms: Even With AI Growing Like The Cloud Giants, The Shares Are Overvalued
- Summary: Shares deemed overvalued despite AI growth.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNS3NLUmtWVTMyZzRaaHVHYmFQc0xzOWphZmRoQld0SGpIcnkyY2ZTWHdHbXRkbHMzNzNUeHg5ZXZ3THV3dmU2c2daNHFmYmFnMDZXNDE3Q1NtNnNkZk9YTGZ0VGh2UEVwOUt4ZmpnT1BJU2hSV3R6RS05WlB1NFJoVFBtbnhiRnFNMUJuWXNsWW1IVFcwRXdGbW56QWpRTlJ3c2psX0VMMFRJejRfdnpkT1RBcXFnSUpSeG5fVG1ieldpUQ?oc=5>

### As Meta Stock Suffers Its Worst Month in Years, S&P Delivers a Brutal $39 Billion Cash Flow Warning
- Summary: Meta stock worst month; S&P warns of cash flow issues.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNU3VvajNzS2xKY0VxU2ZhdXNXX3RMelRqeGxPWDZOQmhTYWFqMnRtZ1JFd2dxQkozT210dk00b3VVMU9NcklMM0xIUjRKOG40ZzU2VFlnd2dfTWhVc2xLQ3RiTWJJUW5vR0hTRndyczZDblhIamx2ekhoZzU1cDlyRVhoSUVfOG9oMkdtWUhPSmJCci1ILWs3Q3lLMA?oc=5>

## CATALYSTS

### ETFs Are Net Sellers of Meta Platforms (META) on Thursday
- Summary: ETFs sold Meta shares, indicating negative market sentiment.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOZ2ItaERBamlLbk94ZjhjQy1BcnBCcGd6UTEyaU9XQXVEREdtNE8tYnZhYWxMc1k0a3pEMnI5VE0yR1dFeHByVGNmSGNlcXNQUVFRSTFTa05HeC1LZHdTdHlIei1oVFpBc1JzMGZWVF9HSXp0M243OEFqREpBMlhLVzh2YlRqcVp1WHJJU3BkMms4ZG9QZUN4dGtpNDQ?oc=5>

### Meta Reportedly Plans To Raise $20B From Its Cross-Border Bond Sales, Including Debut Euro Offering
- Summary: Meta plans to issue $20B in cross-border bonds, debuting a Euro offering to raise capital.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxPNzR0Q0ZNM2h6X3ZnbWg1WkJrOFBseEt5ZE9tZWpjTGhXcWEzYzRCOC1OSWotOWpndmVBY01HMUUwN0h6aWtCWlE2R3R1S0N5N0hLUVVLc2ZmTXVlR21iV2VhNWUtZURWNFVmWnF5alB6LXd1eUpvZlpXRGl5bjhOWVN6eHA4d2NkaE5sc25nOWg3WGhxMzZ0cm5HSVZQRm45QV95TnNGM0p1YXppbWczOWU3LWVSTUIxTGQwUXFnQmhuMDRzOUJDTEp4YlRuTTA5RHVFUmVteXU2TmhXOWNCSXBJb3VHM0xISHUyUnlBMA?oc=5>

### What Are Wall Street Analysts' Target Price for Meta Platforms Stock?
- Summary: Analysts discuss target price for Meta shares.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQYmtUOURXZENzTi1wQjRHREwwczFiRUh5Y3dPYXdXaXJoSlp2S2xyS3FFX2p1cG55SG1GdHVPTkFLZ25IOTRnbGR0bEJ6YVIxZVpKTTc0QnNwZTJBV1pLVU9Ycm9QeDZTNmRxQ1NKS0EwQWtERFRNbDMzSVhyN0twdnlqWTFCQlp4b3lXWkY3N0RuQmFSWllmUVVVVmVCQkFEc3lKYTRpVmhaTm9CUU5wWQ?oc=5>

### Meta Platforms, Inc. $META Stock Holdings Increased by D.A. Davidson & CO.
- Summary: Institutional investor increased Meta holdings.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxOaHI2ZGZveFFqQVJ5NFAtOFo0SFBIeHYzbnVxeFIzbXgxdU8zNW85SGkyUE5xdDYzWm1lM0NDbEJTMS1JWTQ5aTQwVHhIOTRvbnAxSmhqSUthX2V6XzM4UkVMWW10WUl3M05mWlNjQXNsTnJKM1ctODVPc1RHZlJGYVc5WEhMaU52b1NQeFE4NFZHOFZmcE11dXFPWi1WMFByZWxFVHJRaXRQU0F2eGFGVnNyb3Q0VkZYRGZiMEY3TDFHejlNbEE?oc=5>

### Down 18% From Its October High, Should You Buy the Dip on Meta Stock?
- Summary: Investors consider buying Meta after price drop.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQczByTk95VmVDbS1BMl9qQUdobDhqRVZVLTBiMGxNSFpuWmNzQkxtM0VrRmlQUWZIWVdIRmtLdi0wTmk0cTRTeE9xNS1iRll1Zm5aYzdFTUg4QUhybWFqZHMtdEdqOG1oZjhfWHRHa3JlT1V6RlVQQlNTU1otM05pd2MyQXZySXFmS25LWVEySlRoVGJzaExIYg?oc=5>

### What Is Going on With Meta Platforms Stock on Tuesday? - Meta Platforms (NASDAQ:META)
- Summary: Daily update on Meta stock activity.
- Date: 2026-11-03 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOSHZNbkpUWEwzeC1QOW9idTNpVjI2U29mTGFpYTBLYjhJMGZZNEhVVi1KOWVDcVRiUTNXZU4yLXBqaXpaUnVuX19vdDE2SFZvZ1B6Mk82eExLR28yUUVzYzRVdFB4MThVc3hfN0RHRU51d1RLMThnOVF6XzJlUjl2ZGdVN1JRMEhPd0h6dVY3WFhBczVCbGRodHNrYV8zWTRYVE5lN3RxZXVXdw?oc=5>

### Here's Where I Think Meta Stock Will Be in 2030
- Summary: Long‑term price projection for Meta shares.
- Date: 2026-11-01 | Impact: low | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPclByLUdFWGlDVHB2TmloYlpXdUdJRlJwc2lhQzl5YmR5Q3VraFJGQU4wVzhGN1hKbFhhN1ZWTGhCTnN4UGZfcU5XbUtmd21uaHFOdk5FdDBhWE5MamFjU3VOZlROQVZZMlY0VGtLamRmbHBlZ2FQaWY1MXVtRTNJalpjQjNBRmJpZzl4REh3c0w3cHp1?oc=5>

### Meta to raise $20B from bond offering -- Bloomberg (META:NASDAQ)
- Summary: Meta plans to issue $20B in bonds to raise capital.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQcWhSS2lqVEM2VjJ1TFlBQlY1LWtUNEhrSnFxOW5zN21wbXVUTFNzWmg0RW1RemE5d0g5MW9SVHZlN25MS1BBd2NqeTlXZFl2cEdHS3ZTVlEta3V4dk5CX05felQ2QzdZZE9YMlNWaEUyeDNENnFlVlpSX1RUQUIzX2s0OGhPWlcyaDJXZVNPUQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **META** | **21.19** | **5.91** | **14.14** | **26.10** | **1,610,804,756,480.00 USD** | **0.77** |
| GOOGL | 14.62 | 5.39 | 18.63 | 24.70 | 3,552,105,201,664.00 USD | 4.37 |
| SNAP | N/A | 5.17 | -79.15 | 18.90 | 10,011,890,688.00 USD | -20.75 |
| PINS | 84.88 | 3.91 | 40.17 | 11.90 | 12,169,835,520.00 USD | -35.52 |

Peers fetched as_of: 2026-11-04; META reuses existing data (market data as_of: 2026-11-04); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-04

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-22
- Revenue (latest available single quarter): 13,727,000,000.00 USD; period 2018-07-01/2018-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 9,860,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMinwFBVV95cUxQekVac0tXM3pEX253R1RuMlJoeXlHUEc5T0dIeHEwVkJQOHZ0SWI1XzlNWk5EZURWbl9xOEQ2Um5mTE1KeDhuMkIzTG83aGhPQ2R4WGFSMmctT0laR2VIOVRUUXg0NllPMU9TMlRpRWx5TUJPcVNLc1U5SWp2WnJEdHlqZHdZU0FLYk9Lc2h5OFMyMjEyUWdrSS1BMWpKa1U?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQOXBqcHhOdEM3MkZxZG5aOVJqbWY1ZF8zYXJSMnhXb2JqZWpkNGVTU01nbERXeFdoQnZkTm9NN3htVVktME1VVF9DcVlQdHQ5R1Mta1NYbU5xX21RYkNlTE9BNjFlY21kRlRjTzRnVG9GLTFyNzgyYW96MTE0VVRVQ2ZaMnJGZXBIM1RRdFJiU0tHTjVKUFNBYkluY1U?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQWW1uaWJkbk9BMm5MZnh4RG5IVGFsTV81MFJyRFhKR3k1N3c0OVRWRlkzSFJUY1FheGpmVkplZ0xCN1JMMVFhSDhqdHIxN0Q3bEw3ZnBSSWxpV3BJMzN2UDVqMGRfRDRaSFJXWXZheU8zeXVRX1VmcmI2WG9HdVpuRDcyVmVFMEJNZzAzVUlCZGRRcUNFUU1BUTRwSzkxaEk?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPRHVTVGF6UWh0bW5RTmZVRlozWU9KU3J1QURKQXJQMzlRTjA3c0lFQ09HZldGYkNiYkFDYnB5cFVfcWNwempXRl9NUDd5cXpFQy15eEE0OXFGTENYRFVaaVM4dEVzSkhwQ0h0eFRrMDkySHRFUE9hUWxPbjlXVnpsY2VfaGMtVlA4MmhXbmNYQl91cWdxRW9aSg?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxObXlMMUZPdTgwelhHYnVDZXBuMHlFNGNWZHp5ZTNpTE5iVkxTODFRcWoyNUtrOHRlcC01QmxOZ0JOS0RzS1J1c0RwdkpBcFoxMW8xRVNTVllXbGVjUjd6eFNKdThtVnhHQmV0alRrM0REQUVBbW1lZDlITEJhWlZndjJqTi1uRFRBamxPaG51Sktld3ZRVkRtYVlqZEs?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxNUGZ6dUhvNEpRZFpmcXVSMUZST0hqUFFFb0lGZnZ6MzJrU3JPWlpscXFxbTRpZHRuTVV5QWtQbHFwSGxpS09lYldid2lheDN4V1NncHZvNUVUaXNfSHVwT3RyeWpYWXh3MDJpZDBDRGNSTlJ4QmhLVVdmM0owWndKX2pFdmM4eERkQ0tzajZDSEs0a2lGakhqR2cyN3hOcUxmdTRkYl9SZkEzclZpanUxUktvd0Vsb0lYT0R6aGpVMnltWFpqOWFaMW5R0gHPAUFVX3lxTE0weVVCaGg5RDZOcEc0OGpjV1djTjN3NmZHa2pNU2dZTG1RZXNYZjd4V3JWYmhSb3J1ZTY1TlByRjJPOFJXdnBWN3p4YjBVYmU5Mkd0TGY4UjZDRnF2Q2lxM2ZzdC13TmIycURreXBVUkhvSjJoVU43aDUydGVxWHAxSng5ZGZUUi15X2l5NzV1clNvVXlYdXJiRGpmQjNmX19rVlQ1RE41b3A2UzVFSElucGZCOTBJMDhFNUxiWmFxMlVWcFEzdC1nVVc0dkdWZw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQamFKWmVYLUc0VkRSZ3U2anMwaXJBVWNsM251R0UwVUpSUDBLM29LeDhGTGlLOEJUVDR2SDVGRGxFUFRfX3hQOUR2NXI5OGhibWVldkw1eWktYkRuTWY2T09fRFhoNXBxRE9sTFYxTlB2Rm9OYXhPNC1QQnNreXNFeEdkaDRjOFhHRHZ4d0FaN3JPMF8zRnlz?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNM0tTajVlck0wTDZTRk8zN2tTQndHRFNLd0I2OGFfdU5TTjZ2WHE4SXVFTkZiT0tJN2RQb1RLcURQRnlEeWVFZHhXR0FlbHZlQ2d2OFE0NkdTUFQ0OUhkMkEwMmQ2R0cyZWdleV9hWXJKRkIxSW1OQXd5RldaMDl3LWZFXzZ2Mm1kX0lSakRVeHEzT0VvRkFvZlY2cW1FRHNwX3RKTUEzSUE5MUJWaDJOZHVMWXFaZWpleG9oUkRuX1E?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNS3NLUmtWVTMyZzRaaHVHYmFQc0xzOWphZmRoQld0SGpIcnkyY2ZTWHdHbXRkbHMzNzNUeHg5ZXZ3THV3dmU2c2daNHFmYmFnMDZXNDE3Q1NtNnNkZk9YTGZ0VGh2UEVwOUt4ZmpnT1BJU2hSV3R6RS05WlB1NFJoVFBtbnhiRnFNMUJuWXNsWW1IVFcwRXdGbW56QWpRTlJ3c2psX0VMMFRJejRfdnpkT1RBcXFnSUpSeG5fVG1ieldpUQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNU3VvajNzS2xKY0VxU2ZhdXNXX3RMelRqeGxPWDZOQmhTYWFqMnRtZ1JFd2dxQkozT210dk00b3VVMU9NcklMM0xIUjRKOG40ZzU2VFlnd2dfTWhVc2xLQ3RiTWJJUW5vR0hTRndyczZDblhIamx2ekhoZzU1cDlyRVhoSUVfOG9oMkdtWUhPSmJCci1ILWs3Q3lLMA?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOZ2ItaERBamlLbk94ZjhjQy1BcnBCcGd6UTEyaU9XQXVEREdtNE8tYnZhYWxMc1k0a3pEMnI5VE0yR1dFeHByVGNmSGNlcXNQUVFRSTFTa05HeC1LZHdTdHlIei1oVFpBc1JzMGZWVF9HSXp0M243OEFqREpBMlhLVzh2YlRqcVp1WHJJU3BkMms4ZG9QZUN4dGtpNDQ?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxPNzR0Q0ZNM2h6X3ZnbWg1WkJrOFBseEt5ZE9tZWpjTGhXcWEzYzRCOC1OSWotOWpndmVBY01HMUUwN0h6aWtCWlE2R3R1S0N5N0hLUVVLc2ZmTXVlR21iV2VhNWUtZURWNFVmWnF5alB6LXd1eUpvZlpXRGl5bjhOWVN6eHA4d2NkaE5sc25nOWg3WGhxMzZ0cm5HSVZQRm45QV95TnNGM0p1YXppbWczOWU3LWVSTUIxTGQwUXFnQmhuMDRzOUJDTEp4YlRuTTA5RHVFUmVteXU2TmhXOWNCSXBJb3VHM0xISHUyUnlBMA?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQYmtUOURXZENzTi1wQjRHREwwczFiRUh5Y3dPYXdXaXJoSlp2S2xyS3FFX2p1cG55SG1GdHVPTkFLZ25IOTRnbGR0bEJ6YVIxZVpKTTc0QnNwZTJBV1pLVU9Ycm9QeDZTNmRxQ1NKS0EwQWtERFRNbDMzSVhyN0twdnlqWTFCQlp4b3lXWkY3N0RuQmFSWllmUVVVVmVCQkFEc3lKYTRpVmhaTm9CUU5wWQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPTlJYeVhYSENXbTJPTXRLZ0xFdkp3S1dKaGFNYUh5alQyd3BUc3dXb005Szh1R1VjQWg4bXVKY2diMmRWT3l2cXE3cmY5aU9Ib19JTllMMFp0ODFfS04zbGJDYks0VjNOaUNTOGY4OFdvb1FqR0FwRUM3S3hHNXJYQldya0RoRGlnMFJzMlRKeXM3RFZ4d3JZZ2Mwei1sQUU?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxOaHI2ZGZveFFqQVJ5NFAtOFo0SFBIeHYzbnVxeFIzbXgxdU8zNW85SGkyUE5xdDYzWm1lM0NDbEJTMS1JWTQ5aTQwVHhIOTRvbnAxSmhqSUthX2V6XzM4UkVMWW10WUl3M05mWlNjQXNsTnJKM1ctODVPc1RHZlJGYVc5WEhMaU52b1NQeFE4NFZHOFZmcE11dXFPWi1WMFByZWxFVHJRaXRQU0F2eGFGVnNyb3Q0VkZYRGZiMEY3TDFHejlNbEE?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQczByTk95VmVDbS1BMl9qQUdobDhqRVZVLTBiMGxNSFpuWmNzQkxtM0VrRmlQUWZIWVdIRmtLdi0wTmk0cTRTeE9xNS1iRll1Zm5aYzdFTUg4QUhybWFqZHMtdEdqOG1oZjhfWHRHa3JlT1V6RlVQQlNTU1otM05pd2MyQXZySXFmS25LWVEySlRoVGJzaExIYg?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxQcm14ZnFIUXl1OHRBNFlRZEF2bnpEMWRCWjVzbl9JWWtULTVRWmlvaGh5Z2E1RGxoUzIzWVJXMC1CbDZ3VzQ3OFRFblBaMElhMVFyN1NUcHZ5UVliTE12ZkNNUkZnbXF3bW96VUxIWG5JemJrdXVjQnEycFBkTk82b1MxRXhfTXlhdWFnMElDSWotTlU?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOSHZNbkpUWEwzeC1QOW9idTNpVjI2U29mTGFpYTBLYjhJMGZZNEhVVi1KOWVDcVRiUTNXZU4yLXBqaXpaUnVuX19vdDE2SFZvZ1B6Mk82eExLR28yUUVzYzRVdFB4MThVc3hfN0RHRU51d1RLMThnOVF6XzJlUjl2ZGdVN1JRMEhPd0h6dVY3WFhBczVCbGRodHNrYV8zWTRYVE5lN3RxZXVXdw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPclByLUdFWGlDVHB2TmloYlpXdUdJRlJwc2lhQzl5YmR5Q3VraFJGQU4wVzhGN1hKbFhhN1ZWTGhCTnN4UGZfcU5XbUtmd21uaHFOdk5FdDBhWE5MamFjU3VOZlROQVZZMlY0VGtLamRmbHBlZ2FQaWY1MXVtRTNJalpjQjNBRmJpZzl4REh3c0w3cHp1?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQcWhSS2lqVEM2VjJ1TFlBQlY1LWtUNEhrSnFxOW5zN21wbXVUTFNzWmg0RW1RemE5d0g5MW9SVHZlN25MS1BBd2NqeTlXZFl2cEdHS3ZTVlEta3V4dk5CX05felQ2QzdZZE9YMlNWaEUyeDNENnFlVlpSX1RUQUIzX2s0OGhPWlcyaDJXZVNPUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
