# MSFT Intelligence Report

- ticker: **MSFT**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/MSFT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MSFT/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T05:55:22.630687+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 6, 'ai': 12, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261117T062519Z-6171f6c2/MSFT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 14 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 44.0%; oldest publication 2026-11-13

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 506.2400 |
| Return 1D (%) | -2.2684 |
| Return 1W (%) | -5.0491 |
| Return 1M (%) | -4.3115 |
| Return YTD (%) | 5.3413 |
| Return 1Y (%) | 0.5744 |
| Annualized volatility (%) | 34.0444 |
| Beta vs SPY | 1.0104 |
| Max drawdown (%) | -30.0352 |
| Sharpe (rf=0) | 0.1838 |
| Downside deviation (rf=0, %) | 21.8371 |
| Sortino (rf=0) | 0.2866 |
| Historical VaR 95% (1D, %) | 2.8530 |
| Historical ES 95% (1D, %) | 4.1000 |
| Correlation vs SPY | 0.4090 |
| Tracking error vs SPY (%) | 31.0668 |
| P/E (trailing) | 26.42 |
| P/B | 7.99 |
| EV/EBITDA | 18.61 |
| Revenue growth (%) | 18.80 |
| Forward P/E (estimate) | 20.94 |
| Gross margin (%) | 67.66 |
| Operating margin (%) | 47.10 |
| Return on equity (%) | 34.22 |
| Free cash flow yield (%) | 0.08 |
| MA50 | 519.6088 |
| Close vs MA50 (%) | -2.5729 |
| MA200 | 441.3715 |
| Close vs MA200 (%) | 14.6970 |
| RSI (14, Wilder) | 41.8623 |
| MACD (12,26) | -0.7348 |
| MACD signal (9) | 2.4821 |
| MACD histogram | -3.2170 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MSFT': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 506.2400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.2684 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -5.0491 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -4.3115 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 5.3413 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 0.5744 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.0444 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.8371 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2866 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8530 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.1000 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4090 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.0668 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.0104 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -30.0352 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1838 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 20.9379 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 67.6570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 47.1040 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 34.2210 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.0796 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 26.4217 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.8623 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.2170 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -2.5729 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 14.6970 -> Clearly above the moving-average trend level.

## TAILWINDS

### Microsoft Corporation (MSFT) is Attracting Investor Attention: Here is What You Should Know
- Summary: Microsoft draws investor interest, potentially boosting demand for its shares.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQNHdZOGRjaEJQWVQ5Tm9NMklaaGwyWHRFX3VYLU0xMmpBbVI2anJxTjZoQXI0eGpOVno3c3BRS1Z2a0kxSWFVRFFuNzU4WGdWNDl3S3RRb0lYeVhLVEY4aHF2aTNYNXFKbWxFU3ZvUU93WUlZT3hwVlQzQzgtR21EX0FkOTh2N0pMUXlhaWlaVUdqbHZTTGVkdzR5a0tDa2l5dDBDdXR6NC03TFJYLXJNUA?oc=5>

### Microsoft Corporation (MSFT) Rose on Strong Fiscal Year-End Results and Robust Outlook
- Summary: Microsoft reported strong fiscal year-end results and a robust outlook, boosting investor confidence.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOOUctNExwQ2VPbVZTWGdBdjZWTnNhU1hjZUxQZWdUSzhhVWRKRUt2ZHZORkZ3V3dxc3RCbE83Ny1JX2o4NkxhZ2RxblFuTFdNUjJJaWZhT3VfQWxkZFN2RlVXclZlVU1Ua3FJbERLbHRkc1pFbjRpNlNZUHlKS2xYR1BNVDI3bWtUOXd3RmV6RjBwUWptb1ZiaVJsTkVyVGN4TENHR0pn?oc=5>

## HEADWINDS

### Microsoft Stock (NASDAQ:MSFT) Drops as Bill Ackman Sells 35% of His Stake
- Summary: Microsoft Stock (NASDAQ:MSFT) Drops as Bill Ackman Sells 35% of His Stake
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOY2VnYmp6ZTM1SFVFMGlXbzVud2dja1c1RlBRaUdleDQ2eUFiZEY4WDhYM2VRTnNGUTlGZl9DbF9FMG1sNTVfVFNDcW9SRlpXZXFlZVp5ZlpJWXZyY2JQSWdNd3RySzUtMi1pYTZScl8xQm9jaFdSMVdNNzEwbUpjS19OTGw1aVFua1NKQkNfMjZNTHVBdzRQZ3BWRWpBVXM4?oc=5>

### Microsoft Stock (NASDAQ:MSFT) Slips as Massive Outlook Outage Post-Mortem Begins
- Summary: Microsoft Stock (NASDAQ:MSFT) Slips as Massive Outlook Outage Post-Mortem Begins
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPY2ZBT0k0ZkJ2N1Utb2k5RjIyWnp0SzNQQnhITVdET1Awa09pWmtyekJrekxqVXJaVzAwZkRDTmpaaWVyWGpJdGZ2Qi1ZTnNTeW9rRmtZd0lPdUY1WnNIcnFrZmdlODYxQ3lYbVJubjdUdElYOE04M09ZM0NrNGd5NWNEb0lXRXViaXNHMXhDSklLanN4Wi1QZXJHMWdIUk1MVktTbHdWdDJoWFk?oc=5>

### Microsoft Stock Falls Amid Sector Weakness and Outages
- Summary: Microsoft Stock Falls Amid Sector Weakness and Outages
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxQU2lsc3FrLXo4S1lodE02VFdNc3RlbGY5a2NTTTVjVmtPRDhic3FfME5UQmc3cWhVSWVjbFY0RlBpZ2dTUGMyX2J2N2hQSnBScjhFMjdrMUFXVzNjYldjcExQeEJvYkpEazUxQ3djbU9POXRpWjJpbjd3c3NqeGpKR0QxY0lod3JvdXd4QUFiQ2JmVXRaMmt2cUt4Z2dlNlloYTBpOE55RE40SUlmbG81WFplY1dfQQ?oc=5>

### Microsoft Stock MSFT Drops Below $500 as Cybersecurity Concerns Hit Tech Stocks
- Summary: Microsoft Stock MSFT Drops Below $500 as Cybersecurity Concerns Hit Tech Stocks
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxQTy11YjZDbFFZcDE0VWg3UkJXTGNrOHF5TjZfZ3ZSX3JSLUhwZUIzU0gtRlZQbUI4bERLTE1ZWXV2ZkxNdlp6b2RfM2dEUklSNEc1UFhEQWlzUW9TSFNUckRqOXNPbnhsazZNZUlJd01fOF8zdDZXZUNjb0ExOWYtejB4N1NxNmhEVUZMenNER21wbXpWNUE4X2ItREhQZS1IcmFfbWd2dzE4b0hXVXdDUERwdmVUTWxUaDd3al93?oc=5>

### Microsoft (MSFT) Is One of NVIDIA’s Biggest Customers, and a Growing Rival
- Summary: Microsoft’s dual role as NVIDIA customer and competitor may create strategic tension.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQUWl6NDdVVHVoUnJ0TVJBaDRMWW1mX0U2M29TQ2xTbksyaXFWSDI0bldFYTBYOGdPcmN6bWFwSDhjZFpad3RDOFE1SFJ6azJaUDlLN05adEI4TlJfRlJxTW1kWWtqLWs2TjJIeUFVWWlTdUlHMUdfUVI0UzN0UVYySm9UYzM0aGtOTmZPYld3X2lrc3N1Q2RTaTVrbjVwT0E?oc=5>

### ‘SaaSpocalypse’ Fears Hit Microsoft Stock Again. Don’t Rush to Buy the Dip.
- Summary: Continued SaaS concerns pressure MSFT shares.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxNaGtTRGVaNHpadHlTY1NJQy1mQXpJQ1ZOaFVrY3Z3eU15STMxeE5fbXFuTi1VLWlqdmFYd0xyZ1pBaE1oSE41WC1zWVc4TW04S2s2bDlVMlVHZWZubi1iNFVuRnBUcFV5UXh0WlBoWmQ3Q0lGY3otcWk3eXBSUHRzQi00SEZIcHh3dXc2MEdGdXJWYmpGNTNVMm1BbEdfSTB2STNKTWcyRQ?oc=5>

### The Microsoft outage didn’t lose your email — here’s what it does mean for you
- Summary: Microsoft experienced a service outage affecting email, but no data loss occurred. Users may face temporary disruptions.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxPT0U5d29Od01qNm5mUGY0WU5hdTN5eTV1M3ZxMUNiMXhzWGZtZWdlOExJZ1ZCLURsTGwxQ1p4OFBRX3hyZGNQN2Jfd2FGRUl6UG1kMzBDYjVTU2J1WnQ3QzdadzQ3ZU9zaEdPUG1XbUhNdmkyc1ktNVVsVW5XUjJBTGpUb3RsbVdaRkpvYVliQl9JWHhrU1Jab0hwVmhGOEZNbFY3NWFyME42bjVpNFZZSXZJS2FwM2ZGZVdzTjI1bUM?oc=5>

### Microsoft Is Making Voluntary Exit Offers to Engineers for the First Time
- Summary: Microsoft is offering voluntary exit packages to engineers, indicating workforce adjustments.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQci1qeVFnbVdRbUVhYm1FWkZPallwbTFJWXFqc3IybkxFbFlqX09oZXVLamMwaXpTaEZjb0hqODFRR19TQ1ItQkFaOXFhMU4yU1FhNFpZYUhHekhocktoQXVIQ21KTmlTM1ZLOHdxNUd5LU5kb2pMTWhfbzhVc1ZGS21NSko0cnhZMks5OWswNFFDYmR0MkE0b3JXWWVBd0QwTkZMakJR?oc=5>

## CATALYSTS

### Microsoft Leads 4 Stocks That Just Announced Bigger Dividend Payments
- Summary: Microsoft Leads 4 Stocks That Just Announced Bigger Dividend Payments
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxOVFJQSElqMm1uWXJuemFQcVFxVzRYaV9yU1UxWHFJQlY0ZlEyNkxTNHA3UHh2aEx4aGsyUHBLMllHMTNpbV8zZGZwcENuQk14bVZmc1dVNmhvY09NcnFKaTlOZklnV0lQZ2pfQWM1TUMzdHZ5TGU3NDg2MVpidEZMYVJ6c2lRWUdUX1JOemdzakxTZ3hqSThDQ1VIMW9sMG1KbUdmX2ExSFRJSFNoMnBIR2Z5Zw?oc=5>

### Microsoft (MSFT) Strikes AI Deal That Broadens Its Chip Supplier Base
- Summary: Microsoft (MSFT) Strikes AI Deal That Broadens Its Chip Supplier Base
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOX3prYWZxNFJ4T3VWLVVoT0NaUHRrbXg2UkFsX0RYQlRqQ1I3SXByUkVtckxqT1hJbi1Kc3lLUDRKX3loMTdaRVFyTzUxUHN6aVlmUDVIOVVvYVZRQmJYWHRXTUdxdC1Tek5jQ3owWHEzN2JxeTZnYXdkU3gxYm1VSXlWeEhvUmNxd3pjSzk3bnI1Nkpwa2MzRXR3?oc=5>

### Microsoft (MSFT) stock price forecast: Wall Street analysts see 22% upside
- Summary: Analysts project a 22% upside for MSFT shares, indicating bullish outlook.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQYXJNSTlyS19oSERrUGpmR2pyQ0F4Y1FDZ0hqY0d5R2c4U1o3QlBaRnVJOHZOSmFqMW1kNGYwSGZhY0lZMU4zN3JTZlBzWVFtdWlXSFpYUGE0VWlZVHlwbzVOM1BlQUVjdzJ0alZIc0pXV2dPOXZrN0hxSlE4aEpFTWtlUlpSVFl2MGNsRHQxOHBubVBkbFY0N1VuT05UZw?oc=5>

### Microsoft Corporation (MSFT) Climbs Amid Broad-Based Growth Drivers
- Summary: Microsoft’s stock rises driven by broad growth factors.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNQ2xqdVc0Qi1tZ2lRbWVmeVVxZzZ5TnlHRl9fSlNiYXJ5VnBCNjREb012Q2RxRDE2OUF3SHVUek9GMkFCM01vck5aTXJkc3NQZWswZTRPY3BNQU4yN2lueHYyLXc0T3VSV3FzLWRBVzgwOWZYTDhBa3VXYWNZY3ZOZS0zUmZCX29pZGdxTGpLbl9MMGZTTjEzcl9fYTBSam5OM0pSNmJn?oc=5>

### Microsoft (MSFT) Sees $360.6 Million in Net ETF Buying on Nov. 11
- Summary: Microsoft reports $360.6M net ETF buying on Nov. 11, indicating institutional interest.
- Date: 2026-11-13 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPWmdKX2VHelFFazNocWt6TDZUNTJoNGZRbnloaVV6QWZ2WWt3T2ZHNm5BSEdrT25hcXlucURMQ1hWRXVZc3VHa2xZSlpjY2RpTWFPaGN4NGp2S2REeXV0aW9zcHp6eGNxN3lBZVl3U2FnQ3NxdnZVVmx6NzV0bGZUbDlzdTJXTWNTWTlrU205bXUyNllS?oc=5>

### Microsoft Stock Has Grown Roughly 14-Fold Since Satya Nadella Became CEO in 2014, a 23% Annual Growth Rate. Can That Pace Continue Under Heavy AI Spending?
- Summary: MSFT’s stock growth since 2014 is highlighted, questioning future pace amid AI spending.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi0wJBVV95cUxNLVl5MmpVTTY2Q1U0dk9tbFotRi0wOXAwcF9pVDE2UVQzZzN2WW1rcXR2QW9mX3RwZE1MZ1lreGdPU2l1WGZYVUxvN2xMeXpURWtrVVVrNm4zcVdoVFNFQjYzbjVPMlRBbDhFRVdpSzM1N0hyUWR2RFJJWGN3MG5KSExPWkVXNDd2TURfcUdDQmk1Q25BU2EwR3ZhaW9sM3BNUnBzNTA3cmJ3UC1fN1VQSUR6bGR6eWpaRUREeUI3cnZQWlhMM213OVlFR3JwQTVSLW1xSVV6VmhkQTBBTTlBTnhMOVhmLVoxYUJZRXk1WnNoMEN6Q0M2S0FSMlN3Q2xSZVptU1J0dGw2N0Y0ZGIyRmhyalI0eEp0a014dGxKbEFvN3ZCMTc4QVFxSC1hRjJmUUhkNDVnN3ZTeXA2NU5hRWtFVnBNdjNkdHNudVEwZ0JuVHM?oc=5>

## RISKS

### Has Microsoft Stock Become A Different Bet?
- Summary: Investor uncertainty about Microsoft’s valuation raises risk concerns.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPenQ0X1kweC0yd1FQelFMQXdjMjFMbklTbWxMOXRzb056WElTbVZzVS0wUmVlVHVzYmNmUnlqSktuV1pON3ZwU2RabWpDV001clNIYW1fWDNSbEUtUkFDdHcyUHVpb3lxWFBQQ2c2bFF0VWxaczB6eklrZkZwSHd5YktyV1g3Q3p0SDZzVW5PcFl4TnZwbHBzMzFkb0lQampwWElEZ0FB?oc=5>

### Microsoft Corp Stock (MSFT) Moved Down by 3.35% on Nov 17: A Full Analysis
- Summary: Microsoft’s stock fell 3.35% on Nov 17.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPTjBCbjI0blNJMTVHeld3VzRjNHFSbHcxMXRCSlpYeDhmbFN6aUZSS05FYVI1SEhsTkUxZmJrNzdjeEFMTjZ1cWJpT3dhUGZKeFZQdFg3TC1wWG1kZEtsX25KOXNGYWdYQ2tkYy1INF9UVEFDaHFxQ1JCX0JLNU9DOVR4WXlkQ001bGtr?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MSFT** | **26.42** | **7.99** | **18.61** | **18.80** | **3,759,436,726,272.00 USD** | **0.57** |
| ORCL | 18.67 | 5.63 | 14.09 | 29.60 | 358,536,413,184.00 USD | -46.99 |
| GOOGL | 14.82 | 5.22 | 18.05 | 24.70 | 3,444,778,729,472.00 USD | -1.44 |
| AMZN | 20.83 | 4.54 | 16.22 | 12.10 | 2,788,600,315,904.00 USD | 10.74 |

Peers fetched as_of: 2026-11-17; MSFT reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-17

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-28
- Revenue (latest available single quarter): 19,953,000,000.00 USD; period 2010-10-01/2010-12-31; fiscal year/reporting period 2011/Q2
- Net income (latest available single quarter): 36,629,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMisAFBVV95cUxQNHdZOGRjaEJQWVQ5Tm9NMklaaGwyWHRFX3VYLU0xMmpBbVI2anJxTjZoQXI0eGpOVno3c3BRS1Z2a0kxSWFVRFFuNzU4WGdWNDl3S3RRb0lYeVhLVEY4aHF2aTNYNXFKbWxFU3ZvUU93WUlZT3hwVlQzQzgtR21EX0FkOTh2N0pMUXlhaWlaVUdqbHZTTGVkdzR5a0tDa2l5dDBDdXR6NC03TFJYLXJNUA?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOOUctNExwQ2VPbVZTWGdBdjZWTnNhU1hjZUxQZWdUSzhhVWRKRUt2ZHZORkZ3V3dxc3RCbE83Ny1JX2o4NkxhZ2RxblFuTFdNUjJJaWZhT3VfQWxkZFN2RlVXclZlVU1Ua3FJbERLbHRkc1pFbjRpNlNZUHlKS2xYR1BNVDI3bWtUOXd3RmV6RjBwUWptb1ZiaVJsTkVyVGN4TENHR0pn?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOY2VnYmp6ZTM1SFVFMGlXbzVud2dja1c1RlBRaUdleDQ2eUFiZEY4WDhYM2VRTnNGUTlGZl9DbF9FMG1sNTVfVFNDcW9SRlpXZXFlZVp5ZlpJWXZyY2JQSWdNd3RySzUtMi1pYTZScl8xQm9jaFdSMVdNNzEwbUpjS19OTGw1aVFua1NKQkNfMjZNTHVBdzRQZ3BWRWpBVXM4?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPY2ZBT0k0ZkJ2N1Utb2k5RjIyWnp0SzNQQnhITVdET1Awa09pWmtyekJrekxqVXJaVzAwZkRDTmpaaWVyWGpJdGZ2Qi1ZTnNTeW9rRmtZd0lPdUY1WnNIcnFrZmdlODYxQ3lYbVJubjdUdElYOE04M09ZM0NrNGd5NWNEb0lXRXViaXNHMXhDSklLanN4Wi1QZXJHMWdIUk1MVktTbHdWdDJoWFk?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQU2lsc3FrLXo4S1lodE02VFdNc3RlbGY5a2NTTTVjVmtPRDhic3FfME5UQmc3cWhVSWVjbFY0RlBpZ2dTUGMyX2J2N2hQSnBScjhFMjdrMUFXVzNjYldjcExQeEJvYkpEazUxQ3djbU9POXRpWjJpbjd3c3NqeGpKR0QxY0lod3JvdXd4QUFiQ2JmVXRaMmt2cUt4Z2dlNlloYTBpOE55RE40SUlmbG81WFplY1dfQQ?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxQTy11YjZDbFFZcDE0VWg3UkJXTGNrOHF5TjZfZ3ZSX3JSLUhwZUIzU0gtRlZQbUI4bERLTE1ZWXV2ZkxNdlp6b2RfM2dEUklSNEc1UFhEQWlzUW9TSFNUckRqOXNPbnhsazZNZUlJd01fOF8zdDZXZUNjb0ExOWYtejB4N1NxNmhEVUZMenNER21wbXpWNUE4X2ItREhQZS1IcmFfbWd2dzE4b0hXVXdDUERwdmVUTWxUaDd3al93?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQUWl6NDdVVHVoUnJ0TVJBaDRMWW1mX0U2M29TQ2xTbksyaXFWSDI0bldFYTBYOGdPcmN6bWFwSDhjZFpad3RDOFE1SFJ6azJaUDlLN05adEI4TlJfRlJxTW1kWWtqLWs2TjJIeUFVWWlTdUlHMUdfUVI0UzN0UVYySm9UYzM0aGtOTmZPYld3X2lrc3N1Q2RTaTVrbjVwT0E?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxNaGtTRGVaNHpadHlTY1NJQy1mQXpJQ1ZOaFVrY3Z3eU15STMxeE5fbXFuTi1VLWlqdmFYd0xyZ1pBaE1oSE41WC1zWVc4TW04S2s2bDlVMlVHZWZubi1iNFVuRnBUcFV5UXh0WlBoWmQ3Q0lGY3otcWk3eXBSUHRzQi00SEZIcHh3dXc2MEdGdXJWYmpGNTNVMm1BbEdfSTB2STNKTWcyRQ?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxPT0U5d29Od01qNm5mUGY0WU5hdTN5eTV1M3ZxMUNiMXhzWGZtZWdlOExJZ1ZCLURsTGwxQ1p4OFBRX3hyZGNQN2Jfd2FGRUl6UG1kMzBDYjVTU2J1WnQ3QzdadzQ3ZU9zaEdPUG1XbUhNdmkyc1ktNVVsVW5XUjJBTGpUb3RsbVdaRkpvYVliQl9JWHhrU1Jab0hwVmhGOEZNbFY3NWFyME42bjVpNFZZSXZJS2FwM2ZGZVdzTjI1bUM?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQci1qeVFnbVdRbUVhYm1FWkZPallwbTFJWXFqc3IybkxFbFlqX09oZXVLamMwaXpTaEZjb0hqODFRR19TQ1ItQkFaOXFhMU4yU1FhNFpZYUhHekhocktoQXVIQ21KTmlTM1ZLOHdxNUd5LU5kb2pMTWhfbzhVc1ZGS21NSko0cnhZMks5OWswNFFDYmR0MkE0b3JXWWVBd0QwTkZMakJR?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxOVFJQSElqMm1uWXJuemFQcVFxVzRYaV9yU1UxWHFJQlY0ZlEyNkxTNHA3UHh2aEx4aGsyUHBLMllHMTNpbV8zZGZwcENuQk14bVZmc1dVNmhvY09NcnFKaTlOZklnV0lQZ2pfQWM1TUMzdHZ5TGU3NDg2MVpidEZMYVJ6c2lRWUdUX1JOemdzakxTZ3hqSThDQ1VIMW9sMG1KbUdmX2ExSFRJSFNoMnBIR2Z5Zw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOX3prYWZxNFJ4T3VWLVVoT0NaUHRrbXg2UkFsX0RYQlRqQ1I3SXByUkVtckxqT1hJbi1Kc3lLUDRKX3loMTdaRVFyTzUxUHN6aVlmUDVIOVVvYVZRQmJYWHRXTUdxdC1Tek5jQ3owWHEzN2JxeTZnYXdkU3gxYm1VSXlWeEhvUmNxd3pjSzk3bnI1Nkpwa2MzRXR3?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQYXJNSTlyS19oSERrUGpmR2pyQ0F4Y1FDZ0hqY0d5R2c4U1o3QlBaRnVJOHZOSmFqMW1kNGYwSGZhY0lZMU4zN3JTZlBzWVFtdWlXSFpYUGE0VWlZVHlwbzVOM1BlQUVjdzJ0alZIc0pXV2dPOXZrN0hxSlE4aEpFTWtlUlpSVFl2MGNsRHQxOHBubVBkbFY0N1VuT05UZw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNQ2xqdVc0Qi1tZ2lRbWVmeVVxZzZ5TnlHRl9fSlNiYXJ5VnBCNjREb012Q2RxRDE2OUF3SHVUek9GMkFCM01vck5aTXJkc3NQZWswZTRPY3BNQU4yN2lueHYyLXc0T3VSV3FzLWRBVzgwOWZYTDhBa3VXYWNZY3ZOZS0zUmZCX29pZGdxTGpLbl9MMGZTTjEzcl9fYTBSam5OM0pSNmJn?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPWmdKX2VHelFFazNocWt6TDZUNTJoNGZRbnloaVV6QWZ2WWt3T2ZHNm5BSEdrT25hcXlucURMQ1hWRXVZc3VHa2xZSlpjY2RpTWFPaGN4NGp2S2REeXV0aW9zcHp6eGNxN3lBZVl3U2FnQ3NxdnZVVmx6NzV0bGZUbDlzdTJXTWNTWTlrU205bXUyNllS?oc=5
- https://news.google.com/rss/articles/CBMi0wJBVV95cUxNLVl5MmpVTTY2Q1U0dk9tbFotRi0wOXAwcF9pVDE2UVQzZzN2WW1rcXR2QW9mX3RwZE1MZ1lreGdPU2l1WGZYVUxvN2xMeXpURWtrVVVrNm4zcVdoVFNFQjYzbjVPMlRBbDhFRVdpSzM1N0hyUWR2RFJJWGN3MG5KSExPWkVXNDd2TURfcUdDQmk1Q25BU2EwR3ZhaW9sM3BNUnBzNTA3cmJ3UC1fN1VQSUR6bGR6eWpaRUREeUI3cnZQWlhMM213OVlFR3JwQTVSLW1xSVV6VmhkQTBBTTlBTnhMOVhmLVoxYUJZRXk1WnNoMEN6Q0M2S0FSMlN3Q2xSZVptU1J0dGw2N0Y0ZGIyRmhyalI0eEp0a014dGxKbEFvN3ZCMTc4QVFxSC1hRjJmUUhkNDVnN3ZTeXA2NU5hRWtFVnBNdjNkdHNudVEwZ0JuVHM?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPenQ0X1kweC0yd1FQelFMQXdjMjFMbklTbWxMOXRzb056WElTbVZzVS0wUmVlVHVzYmNmUnlqSktuV1pON3ZwU2RabWpDV001clNIYW1fWDNSbEUtUkFDdHcyUHVpb3lxWFBQQ2c2bFF0VWxaczB6eklrZkZwSHd5YktyV1g3Q3p0SDZzVW5PcFl4TnZwbHBzMzFkb0lQampwWElEZ0FB?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPTjBCbjI0blNJMTVHeld3VzRjNHFSbHcxMXRCSlpYeDhmbFN6aUZSS05FYVI1SEhsTkUxZmJrNzdjeEFMTjZ1cWJpT3dhUGZKeFZQdFg3TC1wWG1kZEtsX25KOXNGYWdYQ2tkYy1INF9UVEFDaHFxQ1JCX0JLNU9DOVR4WXlkQ001bGtr?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
