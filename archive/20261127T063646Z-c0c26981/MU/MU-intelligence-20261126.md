# MU Intelligence Report

- ticker: **MU**
- Report as_of: **2026-11-26**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/MU/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MU/key-statistics/
- AI analysis snapshot as_of: **2026-11-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-27T06:56:53.077868+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 0, 'ai': 15, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **15** exact headline/source/date matches; prior report **20261126T064454Z-dbdd6f45/MU** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 7 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 54.17%; oldest publication 2026-11-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 601.2500 |
| Return 1D (%) | -4.5317 |
| Return 1W (%) | -14.7490 |
| Return 1M (%) | -31.4854 |
| Return YTD (%) | 110.8159 |
| Return 1Y (%) | 168.0857 |
| Annualized volatility (%) | 87.4359 |
| Beta vs SPY | 3.4540 |
| Max drawdown (%) | -50.9958 |
| Sharpe (rf=0) | 1.5654 |
| Downside deviation (rf=0, %) | 54.8028 |
| Sortino (rf=0) | 2.4975 |
| Historical VaR 95% (1D, %) | 7.6794 |
| Historical ES 95% (1D, %) | 10.8711 |
| Correlation vs SPY | 0.5898 |
| Tracking error vs SPY (%) | 79.5492 |
| P/E (trailing) | 8.09 |
| P/B | 4.91 |
| EV/EBITDA | 5.90 |
| Revenue growth (%) | 379.30 |
| Forward P/E (estimate) | 2.93 |
| Gross margin (%) | 80.72 |
| Operating margin (%) | 74.59 |
| Return on equity (%) | 88.26 |
| Free cash flow yield (%) | 4.27 |
| MA50 | 895.4125 |
| Close vs MA50 (%) | -32.8522 |
| MA200 | 776.3011 |
| Close vs MA200 (%) | -22.5494 |
| RSI (14, Wilder) | 35.6844 |
| MACD (12,26) | -72.0064 |
| MACD signal (9) | -64.2344 |
| MACD histogram | -7.7721 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MU': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 601.2500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -4.5317 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -14.7490 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -31.4854 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 110.8159 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 168.0857 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 87.4359 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 54.8028 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.4975 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.6794 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 10.8711 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5898 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 79.5492 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4540 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -50.9958 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.5654 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 2.9331 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 80.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 74.5860 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 88.2600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.2704 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 8.0889 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 35.6844 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -7.7721 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -32.8522 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -22.5494 -> Clearly below the moving-average trend level.

## TAILWINDS

### Why Micron Stock Is Up Today
- Summary: Micron shares rise, reflecting positive market sentiment.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxPaERiNmxSTXBoZkV2YXktd3BMTGJqeDFFUjMtc1dPZEMwcXpjOVlmeW5HQS1JMkwyM3JxV1pSRzVYUTdsTEwtaXJ6S2R6TVRQcGp4WFpsWnp3cjk5a1JVVmZTYWRuMTBhM0JNdGhJX0dtVjlSRTZ4V2pMb2JDWEhPR2x5TFlrek9aVkM2T3RKOG8?oc=5>

### Micron Technology, Inc. (MU) is Attracting Investor Attention: Here is What You Should Know
- Summary: Investor interest in Micron grows, boosting stock visibility.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPOGJrYjVsOS1VejkyRzlkTUMzd0FMZXBpODRGWVN1Z1J3b2NSdVVmR0pKUnNWWlpoME9qLXlTcklVMC1tU3RFNk5lWnpRNndweWlBN0dHajNweXNVOUR3RWdTTHBDRXRFVVpETnR2XzdQdjNOQmU4WjVPUXB3ejdBOXhQUkw2bGNHQlpsV05QNlozSk5EV21takpmeU56MDBmamc?oc=5>

## HEADWINDS

### Why Micron Stock Just Dropped Again
- Summary: Micron shares fell again, indicating a negative market reaction.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQWkpQcm91R3l5eFo3OVEtQ2lXN2I2WmVhZmFFZ0hvN2RTZ2hWd1dwNDRveEEtQzBFV1hCLWZiUE1JNklNeVNIRUUwbTdvUklvNlNyWkFGT2VQSG5ia2k5QjNGeG5lQWJGdjVMRUZiQ1h6UE91OURpVUR6bDFUNjZ3SnVvNXp4M1Q4dzFjZmU3Yno2WkZzamd4aVl3?oc=5>

### What Is Going on With Micron Tech Stock on Wednesday?
- Summary: Questions about Micron's current market performance.
- Date: 2026-11-25 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxQS25kX3lFaktpdXJYNUw0SFdDV3lHUjdiX2xZSUxoUDlKYUJYNFFrY1dpbXh4VW9VN1I2TWZ0djRYT2Vnem43NlhRZXF1Vkl5aEFBeDdtWTNOWVBtOHpoMTJSNFVXbUNEUmRLWkpIaVlOV0RXUnFfbUlXNTFYUmgyaXZjUlVMMmJqSk5VOWVVc1pRUzVtaHVyTUFoSUNaak1JbmpaT1Njd1BwN2FVeThtcDFETndkUQ?oc=5>

### Micron Stock: The Earnings Peak Is Nowhere In Sight (NASDAQ:MU)
- Summary: Earnings outlook appears weak, no peak expected soon.
- Date: 2026-11-24 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOWFlyeDJJeXg4SmMwaTdrdXZwc0tHTFFrLWRieFl2UnBnVkFFcFV2dHVncTE1dnRDa1VsSUVNRUo0cnpaTzRKb3FCcDBiS29mRlhnblk4d3NOVGt1UGxWQWw5Z3NmMjBUaHNSejVBWlI4dW5ZdDVPa3kyWFlNMXVqcW91dWRxdjlINm5CMzl6ckRpZ29wRHc?oc=5>

### Micron Falls 7% as a Weaker DRAM Outlook and New Tariffs Hit Memory Stocks; SanDisk Drops 7%: Are Micron and Memory Stocks Now a Value Play?
- Summary: Stock drop due to weaker DRAM outlook and tariffs.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwJBVV95cUxPMHo3cGJWUUhPeEoxeTRsSTRvWldWNF9yUG9tbTlpR0Q4QW80S1g2cnJyUHMtZm1pM3h6QUxtLV9JMktCYXRicFltVUxfWFRXNWJxOGh0b283S1FlSkNBOWV0eDJpQUdxZWRfX0hXeHIwR3JROWt2N3ZFaUdJcGRDQ2QwLVBuMGlvVzVlWGtjUlJmRnA4b1JhTUNRMGRZRG16a01EUG9ZV0ROWkF0MFpoYldLWEZMeTl6TlJSMDVfZjV3dG9ndGFsb1Z0eEV0dm9QWFN6bVRiS2hlbzVhYndvbk5SeVluWnIySGxIeFdocDFqTDNYLWFRdXZXX1RXZmNONUFDSFljOFFnVW8?oc=5>

### Micron Stock Falls as UBS Cuts Price Target, BNP Paribas Downgrade Weighs
- Summary: Stock decline following analyst downgrades.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxOcm5uSzFucTZkd1dyRWJzTGRZYWZQLUhhQXJyUUZsWTh5VEVpUjlBVVVnMkl4bWdyc1ZLZ1I2eVFTQzQ5NGV5eE5GMTl4VnlvcnhKY2phSTRZSlltWVdVVGVSWHVWYWxfZEJqYkN4OXZmcWRjcVQxLVFHZ0lodXdqNHhIWnFRSFE3dGZJUWhLQU1tOXNVNnZJdDVQd2ZhV19TNkZSVGtEVmsybEk4OW9TQS1qWVZYZngydVR3cTRwMGluRDRVX0dEMi16RUVBZw?oc=5>

## CATALYSTS

### Is Micron Technology Stock a Buy at $700?
- Summary: Analyst inquiry on Micron’s valuation at $700.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPN25CbDJEbTJVNVlOd3Q1bEVndjlGcU85NE03RkVNLVJsZWNGZlNHYW16QjJKMW1NYkV3LU9IcWhDenphdmNCVWd5Q1pyVlYwdzRoa09XQjV6aExveWUyNHBIdlBFSmNOdmg1VGJZMnRrU092YkpGbUZKdzRMNW1MUjI1SVJJZXRvNzFsY2hVZFZlS1ZWOWVKbzQ1bXQ?oc=5>

### Micron Technology (MU) Stock Price Quote & News
- Summary: Current Micron share price and recent news updates.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwJBVV95cUxPVjg1WVpOb2ZWTXFSOHNocS1CN0RRZkFtT3BBNUx5bXU0bmxaczQxX3VTQ3JGQjBKUEZqX1hCc3QxNEtSS1lWOUMycWRDUEptY2xMWGZlNTg4NkdJRTFVbmtReGUyelVYb1JuVWJDSUN1RHpLOVY1NHRHZW5TNXhhbUFPRFpzcVNJMkYwWkJPZmlZUFZBdk5qazMwbEsxYnh5SVEyWk10RWR2VkVCUlp5bmlFcnhodVJTTFM4VzNjdUEwN0NOVERzUk1xOGNCVlBvRDY0VXNLbFByQTlWY0J3SG5HREttVFlKbDlnODk5dzdRMXZPVC11NXZ1OE5wRHFDZUF2bEhaNDN1al82dGViVlFvSDgwdjF5QTl3?oc=5>

### MU Stock Alert: What to Know as Micron Reveals Surprising Spending Increase
- Summary: Micron announced higher spending, suggesting increased investment plans.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxQWWgwRmxaQm4tRHVtY1FnUElyZFZNTk15dG05S1hlWmo5aTZZVUZSRHBjb0lIS0FBZktDZXRoUTEwZkllVUd2Rzl3SFU2Y2poeFM4cUNPWmxXVmc5ZHRYSHNpUzRDSUt1TWRxa2xwTlJyMlRYTUN0ZU02SkhoRzNlVWVQVkRQT0FTcDBzZnZlUXlMYmxESWhIbkVIODRZU3Q4NUtYMmNfaVd1VGVOaTA3LWxtYnJGNV9pVGc?oc=5>

### The Consensus on Micron Stock Is Changing. Here’s What Investors Should Know
- Summary: Investors reassess Micron’s outlook amid shifting consensus, potentially influencing short-term stock performance.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPdDdMdFhtUF9jN20zTHZsZVBmQ2tncU1MODhRVzhHTkU1dGxuMmc3dGJaOUV1Z3d6dXlRa1RtUGJXWWJfR0htYkF2bzJfd3FaVWZHeHV2RlNQR1dIb1JRN0d6N1lHT25MUW8tc1hONEhLUVlNZXM3M1VQeG9zNGp0YVpLU2JfZEtrQTIwRTRiZ3JhYUM3NS16TkItaWlFUnRUblB0STNva3hhUQ?oc=5>

### Micron Technology (MU) Dropped, So What Is Drawing Attention Now?
- Summary: Micron’s recent decline prompts analysis of underlying factors affecting its market trajectory.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxONEhmZjdQYXZtRENTeXQ5QVhoTlU5QjlPTlBsTzA1eGFtWmJLQl8xSkx3YlJiVzg4THJ6VF9fWjFyTnZPVGJObUZkVEhJZzdFdzMxd1JfYkRhTWQ2S2Z3T1pUTHJjeGotQjFOc0xCZlJjUUMxZllVV3J1aDF6NENwSUZiUnBEbVdNTE5raHBmc19Gams3cmtPMUdQeEFzRXRSdFNz?oc=5>

### Micron’s Taiwan Expansion Plans Face Uncertainty Amid Ongoing Labour Dispute
- Summary: Labour dispute threatens Micron’s Taiwan expansion, potentially delaying production capacity growth.
- Date: 2026-11-26 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNS2dkSFhwQVBpRG9rYlB3YWZqZkRRbVh4eW01a3BKdmM5dlZKaE9YNTJud3JNSWRVdU1rdkZJSkp5alBYMmJPUGlMYjlENGxYeFhCX2Itd1Zud0RyTnVxb3R0S1BLemR3MVVfNFlzR2tFNGR4d3VNeEU0SlZsQW5Yczl3QmxOS2Q2eDVpUWF1cHRya0VSaXFTMjJyZw?oc=5>

### Why Micron Stock Is Falling Today?
- Summary: Explores reasons behind Micron’s current stock decline, impacting short-term investor sentiment.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxOX0ZiQWZJMk1hcGVMQld4QlRyNlZBWmdNZk5fOGMxX3lva3JkbzR6clFfWFFCSlpQWDZzaGNiSDhmTVoyeE9DTUw3cWhmZXV2bEs3Wl9XZ3Rvdjl1ZTNYZnJVdlVSYzh1OTBnWmVQcWd6b3lPdldUQkl4MFF3eDNkUDR0d3VmMnhoX0dPbTNfVQ?oc=5>

## RISKS

### Micron Just Hit a $700 Ceiling, Caught a Downgrade, and Is Down 10% Today. Is MU a Toxic Stock or a Prime Bargain?
- Summary: Micron’s stock fell 10% after a downgrade, hitting a $700 ceiling. The downgrade reflects concerns over valuation and future performance.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNX2ZQczZGWkZfbjNvak9BdndhRFE4UzRCNlU2ZGpub3NkRDR2YTdVYjVjVTh5Z0Z0RjRUZFFjV1RmRkxySjRoWnV3VUh5VnYtNlJ1ZW94NmVsaHVHeUN1WTNHV3RCODJqbXFYM2VSWWNTYTRrQWJkN2lkcEVLTWlmNFRiV2J1TjNmUEIzbGhBVUlwSmdaa0Jz?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MU** | **8.09** | **4.91** | **5.90** | **379.30** | **682,379,247,616.00 USD** | **168.09** |
| WDC | 9.58 | 10.90 | 16.09 | 55.50 | 101,984,378,880.00 USD | 75.64 |
| STX | 24.77 | 31.42 | 18.72 | 61.00 | 108,428,591,104.00 USD | 81.42 |
| NXPI | 19.12 | 5.07 | 12.74 | 19.30 | 61,238,796,288.00 USD | 29.44 |

Peers fetched as_of: 2026-11-26; MU reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-30
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMikAFBVV95cUxPaERiNmxSTXBoZkV2YXktd3BMTGJqeDFFUjMtc1dPZEMwcXpjOVlmeW5HQS1JMkwyM3JxV1pSRzVYUTdsTEwtaXJ6S2R6TVRQcGp4WFpsWnp3cjk5a1JVVmZTYWRuMTBhM0JNdGhJX0dtVjlSRTZ4V2pMb2JDWEhPR2x5TFlrek9aVkM2T3RKOG8?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPOGJrYjVsOS1VejkyRzlkTUMzd0FMZXBpODRGWVN1Z1J3b2NSdVVmR0pKUnNWWlpoME9qLXlTcklVMC1tU3RFNk5lWnpRNndweWlBN0dHajNweXNVOUR3RWdTTHBDRXRFVVpETnR2XzdQdjNOQmU4WjVPUXB3ejdBOXhQUkw2bGNHQlpsV05QNlozSk5EV21takpmeU56MDBmamc?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQWkpQcm91R3l5eFo3OVEtQ2lXN2I2WmVhZmFFZ0hvN2RTZ2hWd1dwNDRveEEtQzBFV1hCLWZiUE1JNklNeVNIRUUwbTdvUklvNlNyWkFGT2VQSG5ia2k5QjNGeG5lQWJGdjVMRUZiQ1h6UE91OURpVUR6bDFUNjZ3SnVvNXp4M1Q4dzFjZmU3Yno2WkZzamd4aVl3?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQS25kX3lFaktpdXJYNUw0SFdDV3lHUjdiX2xZSUxoUDlKYUJYNFFrY1dpbXh4VW9VN1I2TWZ0djRYT2Vnem43NlhRZXF1Vkl5aEFBeDdtWTNOWVBtOHpoMTJSNFVXbUNEUmRLWkpIaVlOV0RXUnFfbUlXNTFYUmgyaXZjUlVMMmJqSk5VOWVVc1pRUzVtaHVyTUFoSUNaak1JbmpaT1Njd1BwN2FVeThtcDFETndkUQ?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOWFlyeDJJeXg4SmMwaTdrdXZwc0tHTFFrLWRieFl2UnBnVkFFcFV2dHVncTE1dnRDa1VsSUVNRUo0cnpaTzRKb3FCcDBiS29mRlhnblk4d3NOVGt1UGxWQWw5Z3NmMjBUaHNSejVBWlI4dW5ZdDVPa3kyWFlNMXVqcW91dWRxdjlINm5CMzl6ckRpZ29wRHc?oc=5
- https://news.google.com/rss/articles/CBMiiwJBVV95cUxPMHo3cGJWUUhPeEoxeTRsSTRvWldWNF9yUG9tbTlpR0Q4QW80S1g2cnJyUHMtZm1pM3h6QUxtLV9JMktCYXRicFltVUxfWFRXNWJxOGh0b283S1FlSkNBOWV0eDJpQUdxZWRfX0hXeHIwR3JROWt2N3ZFaUdJcGRDQ2QwLVBuMGlvVzVlWGtjUlJmRnA4b1JhTUNRMGRZRG16a01EUG9ZV0ROWkF0MFpoYldLWEZMeTl6TlJSMDVfZjV3dG9ndGFsb1Z0eEV0dm9QWFN6bVRiS2hlbzVhYndvbk5SeVluWnIySGxIeFdocDFqTDNYLWFRdXZXX1RXZmNONUFDSFljOFFnVW8?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxOcm5uSzFucTZkd1dyRWJzTGRZYWZQLUhhQXJyUUZsWTh5VEVpUjlBVVVnMkl4bWdyc1ZLZ1I2eVFTQzQ5NGV5eE5GMTl4VnlvcnhKY2phSTRZSlltWVdVVGVSWHVWYWxfZEJqYkN4OXZmcWRjcVQxLVFHZ0lodXdqNHhIWnFRSFE3dGZJUWhLQU1tOXNVNnZJdDVQd2ZhV19TNkZSVGtEVmsybEk4OW9TQS1qWVZYZngydVR3cTRwMGluRDRVX0dEMi16RUVBZw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPN25CbDJEbTJVNVlOd3Q1bEVndjlGcU85NE03RkVNLVJsZWNGZlNHYW16QjJKMW1NYkV3LU9IcWhDenphdmNCVWd5Q1pyVlYwdzRoa09XQjV6aExveWUyNHBIdlBFSmNOdmg1VGJZMnRrU092YkpGbUZKdzRMNW1MUjI1SVJJZXRvNzFsY2hVZFZlS1ZWOWVKbzQ1bXQ?oc=5
- https://news.google.com/rss/articles/CBMimwJBVV95cUxPVjg1WVpOb2ZWTXFSOHNocS1CN0RRZkFtT3BBNUx5bXU0bmxaczQxX3VTQ3JGQjBKUEZqX1hCc3QxNEtSS1lWOUMycWRDUEptY2xMWGZlNTg4NkdJRTFVbmtReGUyelVYb1JuVWJDSUN1RHpLOVY1NHRHZW5TNXhhbUFPRFpzcVNJMkYwWkJPZmlZUFZBdk5qazMwbEsxYnh5SVEyWk10RWR2VkVCUlp5bmlFcnhodVJTTFM4VzNjdUEwN0NOVERzUk1xOGNCVlBvRDY0VXNLbFByQTlWY0J3SG5HREttVFlKbDlnODk5dzdRMXZPVC11NXZ1OE5wRHFDZUF2bEhaNDN1al82dGViVlFvSDgwdjF5QTl3?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxQWWgwRmxaQm4tRHVtY1FnUElyZFZNTk15dG05S1hlWmo5aTZZVUZSRHBjb0lIS0FBZktDZXRoUTEwZkllVUd2Rzl3SFU2Y2poeFM4cUNPWmxXVmc5ZHRYSHNpUzRDSUt1TWRxa2xwTlJyMlRYTUN0ZU02SkhoRzNlVWVQVkRQT0FTcDBzZnZlUXlMYmxESWhIbkVIODRZU3Q4NUtYMmNfaVd1VGVOaTA3LWxtYnJGNV9pVGc?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPdDdMdFhtUF9jN20zTHZsZVBmQ2tncU1MODhRVzhHTkU1dGxuMmc3dGJaOUV1Z3d6dXlRa1RtUGJXWWJfR0htYkF2bzJfd3FaVWZHeHV2RlNQR1dIb1JRN0d6N1lHT25MUW8tc1hONEhLUVlNZXM3M1VQeG9zNGp0YVpLU2JfZEtrQTIwRTRiZ3JhYUM3NS16TkItaWlFUnRUblB0STNva3hhUQ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxONEhmZjdQYXZtRENTeXQ5QVhoTlU5QjlPTlBsTzA1eGFtWmJLQl8xSkx3YlJiVzg4THJ6VF9fWjFyTnZPVGJObUZkVEhJZzdFdzMxd1JfYkRhTWQ2S2Z3T1pUTHJjeGotQjFOc0xCZlJjUUMxZllVV3J1aDF6NENwSUZiUnBEbVdNTE5raHBmc19Gams3cmtPMUdQeEFzRXRSdFNz?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNS2dkSFhwQVBpRG9rYlB3YWZqZkRRbVh4eW01a3BKdmM5dlZKaE9YNTJud3JNSWRVdU1rdkZJSkp5alBYMmJPUGlMYjlENGxYeFhCX2Itd1Zud0RyTnVxb3R0S1BLemR3MVVfNFlzR2tFNGR4d3VNeEU0SlZsQW5Yczl3QmxOS2Q2eDVpUWF1cHRya0VSaXFTMjJyZw?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxOX0ZiQWZJMk1hcGVMQld4QlRyNlZBWmdNZk5fOGMxX3lva3JkbzR6clFfWFFCSlpQWDZzaGNiSDhmTVoyeE9DTUw3cWhmZXV2bEs3Wl9XZ3Rvdjl1ZTNYZnJVdlVSYzh1OTBnWmVQcWd6b3lPdldUQkl4MFF3eDNkUDR0d3VmMnhoX0dPbTNfVQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNX2ZQczZGWkZfbjNvak9BdndhRFE4UzRCNlU2ZGpub3NkRDR2YTdVYjVjVTh5Z0Z0RjRUZFFjV1RmRkxySjRoWnV3VUh5VnYtNlJ1ZW94NmVsaHVHeUN1WTNHV3RCODJqbXFYM2VSWWNTYTRrQWJkN2lkcEVLTWlmNFRiV2J1TjNmUEIzbGhBVUlwSmdaa0Jz?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
