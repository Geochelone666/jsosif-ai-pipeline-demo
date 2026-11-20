# MSFT Intelligence Report

- ticker: **MSFT**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-19**
- Quant sources: https://finance.yahoo.com/quote/MSFT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MSFT/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T05:45:03.591905+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 4, 'ai': 18, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261118T054934Z-e0d070d9/MSFT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 14 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 36.0%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 498.3000 |
| Return 1D (%) | -1.7760 |
| Return 1W (%) | -4.5387 |
| Return 1M (%) | -6.4210 |
| Return YTD (%) | 3.8894 |
| Return 1Y (%) | 3.3360 |
| Annualized volatility (%) | 33.9562 |
| Beta vs SPY | 1.0014 |
| Max drawdown (%) | -27.9702 |
| Sharpe (rf=0) | 0.2635 |
| Downside deviation (rf=0, %) | 21.6997 |
| Sortino (rf=0) | 0.4123 |
| Historical VaR 95% (1D, %) | 2.8530 |
| Historical ES 95% (1D, %) | 4.1000 |
| Correlation vs SPY | 0.4099 |
| Tracking error vs SPY (%) | 30.9721 |
| P/E (trailing) | 26.01 |
| P/B | 7.87 |
| EV/EBITDA | 18.33 |
| Revenue growth (%) | 18.80 |
| Forward P/E (estimate) | 20.59 |
| Gross margin (%) | 67.66 |
| Operating margin (%) | 47.10 |
| Return on equity (%) | 34.22 |
| Free cash flow yield (%) | 0.08 |
| MA50 | 519.0753 |
| Close vs MA50 (%) | -4.0024 |
| MA200 | 441.4555 |
| Close vs MA200 (%) | 12.8766 |
| RSI (14, Wilder) | 39.5398 |
| MACD (12,26) | -3.5575 |
| MACD signal (9) | 0.5658 |
| MACD histogram | -4.1233 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MSFT': 286, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 498.3000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.7760 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.5387 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -6.4210 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 3.8894 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.3360 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.9562 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.6997 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4123 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8530 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.1000 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4099 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.9721 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.0014 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.9702 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2635 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 20.5877 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 67.6570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 47.1040 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 34.2210 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.0809 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 26.0073 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 39.5398 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -4.1233 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -4.0024 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 12.8766 -> Clearly above the moving-average trend level.

## TAILWINDS

### Microsoft Stocks Rise 3.16% as Anthropic Commits $47.2 Billion Minimum to Azure
- Summary: Microsoft Stocks Rise 3.16% as Anthropic Commits $47.2 Billion Minimum to Azure
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxQN19QXy1YcGVvTkZuMUlxVnllcTJBNFhUWTZDX2ZrNnA3MWtuUVZ1dXRWYUwwYjMxLVhkZDFmSnQ2LU8zY1JZY1BWeDVXUU9jVTBEczNNcVlGOFFjdDZaS1I3TEZRZW9oa0VrNUZRMy0tTlEwQ1BBeG1pVklwTXMxZmt6NFJ5M29Gb2Mwd19EdVFYVGhwSGNnTUJEVGQtbnMxc2EtZEhoRms0ZVFHSXBNVVhlVl9nLWxQMzI2UHlyVXYzbzl5WGVuaTVtTHd4djc2RE9J?oc=5>

### Microsoft Stock (MSFT) Forecast – Mizuho Stays Bullish on Strong Revenue Growth Prospects
- Summary: Microsoft Stock (MSFT) Forecast – Mizuho Stays Bullish on Strong Revenue Growth Prospects
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNbkpCQ3NWcTBELXRDand5VERMRC1yU1lKS0txQmlDWHEwTFljTU5SeVR6elRCZ1FzdkNCSEV2QU96TWRqTlpvcWNBamJQXzV4TV9TNFBKb1l6clVrTERjcVZPM09YRlFpcEp3cTNNSkJhV3p4OGk1X2ZiMzg2SlhuWkZNbUptcVhCa0w4bFIwN0RRNnAzbFQ4WGg1SUNlUlVFQXJV?oc=5>

### Microsoft Corporation (MSFT) Rose on Strong Fiscal Year-End Results and Robust Outlook
- Summary: Microsoft reported strong fiscal year-end results and a robust outlook, boosting investor confidence.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOOUctNExwQ2VPbVZTWGdBdjZWTnNhU1hjZUxQZWdUSzhhVWRKRUt2ZHZORkZ3V3dxc3RCbE83Ny1JX2o4NkxhZ2RxblFuTFdNUjJJaWZhT3VfQWxkZFN2RlVXclZlVU1Ua3FJbERLbHRkc1pFbjRpNlNZUHlKS2xYR1BNVDI3bWtUOXd3RmV6RjBwUWptb1ZiaVJsTkVyVGN4TENHR0pn?oc=5>

### Microsoft (MSFT) Stock May Look Reasonable As AI Commitments Draw Scrutiny
- Summary: Analyst suggests MSFT stock appears reasonable amid scrutiny of AI commitments.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNalJYeUVUa3czcERnOXA2LUVJUlJaM0owQlJvZm9Gek1DeHZXV3lwREJFZVM5Nm9KVjdMbC1KRGJmeWg4Rk15M0FZV0ZMNEM0dF9wLXF3dWRpRjhZNVY4Y19fSU9ucUR0QVZKZ1hEQl91eVdnYmlZZ0E4X2RlWmxOWV9KTmpWcEZLZUxBYUJwV3plM3pUOU1MdzF3?oc=5>

### Microsoft (NASDAQ:MSFT): A High-ROIC Quality Stock for Long-Term Investors
- Summary: Analyst highlights MSFT’s high ROIC and quality for long-term investors.
- Date: 2026-11-19 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxOYjRsQUxKOXhBUjh2NlRZRDFiVGMwYUtWbUJXeXRJQmtLZFBZVThMTU1nbFUxY2UwWXg5d2R5a3p4ZzN1WW1ITF9ZSkV2Unh1TEczTkF3R3VyU1R6UWpYMkNWa0ZreWd6RzE5b0NXeGQ0dlAzaDVvbG96RHhDYWV5dVFUdWx0NVY1OVN6TjB5RmxneUxCendmTGtmTEFsaHl3OGRuQjZCYlFIOE9scG9teTk4OUZrdHlvTEhKNnNzQQ?oc=5>

### Microsoft: Remains My Pick Amongst Hyperscalers
- Summary: Analyst maintains MSFT as preferred hyperscaler choice.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQeGlPQ2Y0R2NqTU9qOS1oUEo3dnBISkxVeGtVR1ZLbjlpV21sbW5HNk5zZ0hXamZFZE1XVTNva0xCaDZXTG93YjB5dTZqUF9UMjVRZEpfUTNHeDlGMUQ2U2xhc21IdWNxODdzdEg0WnpidnhwcXlNaVNtT3ZJNl95TVhXTUNlLU9XVVExcS1wems?oc=5>

### Bill Ackman Says His Microsoft “Sale” Was Really a Swap Into Options
- Summary: Analyst commentary on Ackman’s MSFT option swap strategy.
- Date: 2026-11-19 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxOX1BvZHFVcWc0VGhsYUlJYmUzenZreG12bzJrcW82bjVENjBTTDhaX0t6OU5rdW8xMVNDWTNQUTdBSG81OFo1RWYyaUJaQV9QTTNnNkRmbHN2SmpWWUhiVjAtWFdpQzdIVnFVRHJ2aXpoT2pXNjg1WEdmeEw1NlRXYmlFejZfSkFMcmk1NUlOM040Um4xTkwxcVN2SmVzUnJ6Z0M4X0tyYW1GSzRMYkg0?oc=5>

### Microsoft purchase follows Michael Rulli stock sales
- Summary: Analyst notes MSFT purchase following Rulli’s stock sales.
- Date: 2026-11-19 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxOQjg1ckktVmZ0N1V0cXdya2xLdnBjcEJQSV9GQkg5WjduVGVHcGxJNTNrUkI1VmE3N25HN1dDN3VvUWZwNW05YmlVTWJRNGhZZHl2di13OEszTXFldHNMWG5LWGpRcHJlZ1RIcVJkTEpPMlBCRzNuSGJhdHpNT0RZRzhsRXBPcTI3akJvUWNFNU83S2Rsc2F0cTh4bWVjX3QyXzJoaThZWVB1V0tidGc?oc=5>

### Accelerating Azure Growth and Copilot Adoption Fuel Microsoft Corp.’s (MSFT) AI Momentum
- Summary: Azure and Copilot growth boost Microsoft’s AI momentum.
- Date: 2026-11-19 | Impact: high | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQeGRmcVNfdUJlRkItWGpUU3RkQVJTcnZIQlU5cjJjU3NsSUREMmVuRVBoZXNqODVoeTR0X29DQmRjMDlZRy1OQkNHRk5XaWk0bmRjQVF4NW9TSVhMcFRMemVZNFEzaGZrWWRwbGRPTHlxX2M1U0JJWDhNanFldTJDeW5YZnhnWGxfazhYY1NaOU9zSFhaWXFabVVtZDVuQUloRHo3ckZqdDAxZw?oc=5>

## HEADWINDS

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

### Microsoft Is Making Voluntary Exit Offers to Engineers for the First Time
- Summary: Microsoft is offering voluntary exit packages to engineers, indicating workforce adjustments.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQci1qeVFnbVdRbUVhYm1FWkZPallwbTFJWXFqc3IybkxFbFlqX09oZXVLamMwaXpTaEZjb0hqODFRR19TQ1ItQkFaOXFhMU4yU1FhNFpZYUhHekhocktoQXVIQ21KTmlTM1ZLOHdxNUd5LU5kb2pMTWhfbzhVc1ZGS21NSko0cnhZMks5OWswNFFDYmR0MkE0b3JXWWVBd0QwTkZMakJR?oc=5>

### Microsoft stock consolidates near $512.23 resistance as mixed momentum signals persist
- Summary: Stock consolidates near resistance, mixed signals persist.
- Date: 2026-11-19 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNTzlWV0NHWEFVLURNSi1Ua1FZQk5pUkRTZnRpWklvS3JCWEItZzNWLVlLWjFaTHZEUkl4dnJVcnlsRmdEOURLeHdaZmozVHVlbmhVU1lWYkdYb1d6OTJkMUJXUVFxamswRjZBTVZVZllwajAxNFd3NHFPYVhpT1NKWXF5OEFjdXVtN052TmVOVWtmdw?oc=5>

### Microsoft Stock Hits Seven-Week Low: Is a Bigger Drop Coming?
- Summary: Stock hits seven‑week low, potential further decline.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMibkFVX3lxTE9MNUlzT3liQ3N6bGx5RjJsLU5mNk5LdUFCVE8tNk1HMzBCbVlZa0F3Rzg5S3VSZjF5UlVLN2xSYXFqbS1ZX0oyS3BsbUVKOVliTXEzYVRsZTk2ZFk3bFpOc1ZXNGk3ckUtTkc5RGF3?oc=5>

### Microsoft Stocks Move Lower as $1 Billion Anthropic Bet Precedes Ignite
- Summary: Stock falls ahead of Anthropic bet and Ignite event.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNTjI5ZjByTHA3QnJ6dVI5WGVVeFpwUWFUNXZCeno5Nk9NZXlQcHZDRHhWTnpGVXVJU2xYWGZMb1NTNEVnOWhoaUZUUEg2Nm55emdvVDBIMkNCQnFNZlFZX2lfQW9wLXhEbXdQdEU0cFpRbjZ1QjBwcWZ4TnJscnd1M29UVk9EV2dCc2hCNjE3MTlmZk5DdmZBNDR3?oc=5>

## CATALYSTS

### Microsoft Corporation (MSFT) Climbs Amid Broad-Based Growth Drivers
- Summary: Microsoft’s stock rises driven by broad growth factors.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNQ2xqdVc0Qi1tZ2lRbWVmeVVxZzZ5TnlHRl9fSlNiYXJ5VnBCNjREb012Q2RxRDE2OUF3SHVUek9GMkFCM01vck5aTXJkc3NQZWswZTRPY3BNQU4yN2lueHYyLXc0T3VSV3FzLWRBVzgwOWZYTDhBa3VXYWNZY3ZOZS0zUmZCX29pZGdxTGpLbl9MMGZTTjEzcl9fYTBSam5OM0pSNmJn?oc=5>

### Microsoft Stock Has Grown Roughly 14-Fold Since Satya Nadella Became CEO in 2014, a 23% Annual Growth Rate. Can That Pace Continue Under Heavy AI Spending?
- Summary: MSFT’s stock growth since 2014 is highlighted, questioning future pace amid AI spending.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi0wJBVV95cUxNLVl5MmpVTTY2Q1U0dk9tbFotRi0wOXAwcF9pVDE2UVQzZzN2WW1rcXR2QW9mX3RwZE1MZ1lreGdPU2l1WGZYVUxvN2xMeXpURWtrVVVrNm4zcVdoVFNFQjYzbjVPMlRBbDhFRVdpSzM1N0hyUWR2RFJJWGN3MG5KSExPWkVXNDd2TURfcUdDQmk1Q25BU2EwR3ZhaW9sM3BNUnBzNTA3cmJ3UC1fN1VQSUR6bGR6eWpaRUREeUI3cnZQWlhMM213OVlFR3JwQTVSLW1xSVV6VmhkQTBBTTlBTnhMOVhmLVoxYUJZRXk1WnNoMEN6Q0M2S0FSMlN3Q2xSZVptU1J0dGw2N0Y0ZGIyRmhyalI0eEp0a014dGxKbEFvN3ZCMTc4QVFxSC1hRjJmUUhkNDVnN3ZTeXA2NU5hRWtFVnBNdjNkdHNudVEwZ0JuVHM?oc=5>

### New Buy Rating for Microsoft (MSFT), the Technology Giant
- Summary: Analyst upgrades Microsoft to buy, boosting investor confidence.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxPN3hZRnJJbk9zLWxkWm11ZEY2Nk1Mbkctd19kT3lUakI5enpDbldNRnlmSl90d3JIVUNBQWZ3ang1Y2d6RW5DUU9JNVotelVrNElzWG5VSDl3cktQU1RyckxrRFFZb1BoR0w1VXVtTGFHU2hiX3lmS1pKU2diUTBONHZHaEhId3BUQ050bEM4QW5nT3kzV2hXdkNEVTdsRjFfWWNGOE1TN0tZNXB3TXUxSXpqamQtX0Nkb045QzI2UEFmUExBTmVpb0hKbWxWVGNtNGgtOS1yQm4?oc=5>

## RISKS

### Has Microsoft Stock Become A Different Bet?
- Summary: Investor uncertainty about Microsoft’s valuation raises risk concerns.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPenQ0X1kweC0yd1FQelFMQXdjMjFMbklTbWxMOXRzb056WElTbVZzVS0wUmVlVHVzYmNmUnlqSktuV1pON3ZwU2RabWpDV001clNIYW1fWDNSbEUtUkFDdHcyUHVpb3lxWFBQQ2c2bFF0VWxaczB6eklrZkZwSHd5YktyV1g3Q3p0SDZzVW5PcFl4TnZwbHBzMzFkb0lQampwWElEZ0FB?oc=5>

### Microsoft Corp Stock (MSFT) Moved Down by 3.35% on Nov 17: A Full Analysis
- Summary: Microsoft’s stock fell 3.35% on Nov 17.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPTjBCbjI0blNJMTVHeld3VzRjNHFSbHcxMXRCSlpYeDhmbFN6aUZSS05FYVI1SEhsTkUxZmJrNzdjeEFMTjZ1cWJpT3dhUGZKeFZQdFg3TC1wWG1kZEtsX25KOXNGYWdYQ2tkYy1INF9UVEFDaHFxQ1JCX0JLNU9DOVR4WXlkQ001bGtr?oc=5>

### Microsoft’s CEO Says He’s “Extremely Sorry” for the Outlook Outage
- Summary: CEO apologizes for service outage, indicating operational risk.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQQU5mb3lfUm10QlcyU0hXTjA0dXVDdXlIVHRET0ZMd1ZyTWhSSENKa01wM0ctR194NE4zdmdfLVhSTkRZRXpseDlUVVhRZ01mZWY2LVZIbTBXMDJOdHhIUG9KNUMwN3VvTTRNNzBzVVFVZlRCclFlbENPNHJJWVh5Z3Rmd0NKYVJhXzg4eGtEZnRZRjc1N2dnel9Va2JtcTZFbkdCQzMtbHNvQQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MSFT** | **26.01** | **7.87** | **18.33** | **18.80** | **3,700,472,676,352.00 USD** | **3.34** |
| ORCL | 17.33 | 5.41 | 13.70 | 29.60 | 344,724,963,328.00 USD | -50.32 |
| GOOGL | 14.24 | 5.08 | 17.55 | 24.70 | 3,352,081,989,632.00 USD | -6.64 |
| AMZN | 20.81 | 4.53 | 16.19 | 12.10 | 2,782,977,327,104.00 USD | 15.57 |

Peers fetched as_of: 2026-11-19; MSFT reuses existing data (market data as_of: 2026-11-19); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-19

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

- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQN19QXy1YcGVvTkZuMUlxVnllcTJBNFhUWTZDX2ZrNnA3MWtuUVZ1dXRWYUwwYjMxLVhkZDFmSnQ2LU8zY1JZY1BWeDVXUU9jVTBEczNNcVlGOFFjdDZaS1I3TEZRZW9oa0VrNUZRMy0tTlEwQ1BBeG1pVklwTXMxZmt6NFJ5M29Gb2Mwd19EdVFYVGhwSGNnTUJEVGQtbnMxc2EtZEhoRms0ZVFHSXBNVVhlVl9nLWxQMzI2UHlyVXYzbzl5WGVuaTVtTHd4djc2RE9J?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNbkpCQ3NWcTBELXRDand5VERMRC1yU1lKS0txQmlDWHEwTFljTU5SeVR6elRCZ1FzdkNCSEV2QU96TWRqTlpvcWNBamJQXzV4TV9TNFBKb1l6clVrTERjcVZPM09YRlFpcEp3cTNNSkJhV3p4OGk1X2ZiMzg2SlhuWkZNbUptcVhCa0w4bFIwN0RRNnAzbFQ4WGg1SUNlUlVFQXJV?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOOUctNExwQ2VPbVZTWGdBdjZWTnNhU1hjZUxQZWdUSzhhVWRKRUt2ZHZORkZ3V3dxc3RCbE83Ny1JX2o4NkxhZ2RxblFuTFdNUjJJaWZhT3VfQWxkZFN2RlVXclZlVU1Ua3FJbERLbHRkc1pFbjRpNlNZUHlKS2xYR1BNVDI3bWtUOXd3RmV6RjBwUWptb1ZiaVJsTkVyVGN4TENHR0pn?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNalJYeUVUa3czcERnOXA2LUVJUlJaM0owQlJvZm9Gek1DeHZXV3lwREJFZVM5Nm9KVjdMbC1KRGJmeWg4Rk15M0FZV0ZMNEM0dF9wLXF3dWRpRjhZNVY4Y19fSU9ucUR0QVZKZ1hEQl91eVdnYmlZZ0E4X2RlWmxOWV9KTmpWcEZLZUxBYUJwV3plM3pUOU1MdzF3?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxOYjRsQUxKOXhBUjh2NlRZRDFiVGMwYUtWbUJXeXRJQmtLZFBZVThMTU1nbFUxY2UwWXg5d2R5a3p4ZzN1WW1ITF9ZSkV2Unh1TEczTkF3R3VyU1R6UWpYMkNWa0ZreWd6RzE5b0NXeGQ0dlAzaDVvbG96RHhDYWV5dVFUdWx0NVY1OVN6TjB5RmxneUxCendmTGtmTEFsaHl3OGRuQjZCYlFIOE9scG9teTk4OUZrdHlvTEhKNnNzQQ?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQeGlPQ2Y0R2NqTU9qOS1oUEo3dnBISkxVeGtVR1ZLbjlpV21sbW5HNk5zZ0hXamZFZE1XVTNva0xCaDZXTG93YjB5dTZqUF9UMjVRZEpfUTNHeDlGMUQ2U2xhc21IdWNxODdzdEg0WnpidnhwcXlNaVNtT3ZJNl95TVhXTUNlLU9XVVExcS1wems?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxOX1BvZHFVcWc0VGhsYUlJYmUzenZreG12bzJrcW82bjVENjBTTDhaX0t6OU5rdW8xMVNDWTNQUTdBSG81OFo1RWYyaUJaQV9QTTNnNkRmbHN2SmpWWUhiVjAtWFdpQzdIVnFVRHJ2aXpoT2pXNjg1WEdmeEw1NlRXYmlFejZfSkFMcmk1NUlOM040Um4xTkwxcVN2SmVzUnJ6Z0M4X0tyYW1GSzRMYkg0?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxOQjg1ckktVmZ0N1V0cXdya2xLdnBjcEJQSV9GQkg5WjduVGVHcGxJNTNrUkI1VmE3N25HN1dDN3VvUWZwNW05YmlVTWJRNGhZZHl2di13OEszTXFldHNMWG5LWGpRcHJlZ1RIcVJkTEpPMlBCRzNuSGJhdHpNT0RZRzhsRXBPcTI3akJvUWNFNU83S2Rsc2F0cTh4bWVjX3QyXzJoaThZWVB1V0tidGc?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQeGRmcVNfdUJlRkItWGpUU3RkQVJTcnZIQlU5cjJjU3NsSUREMmVuRVBoZXNqODVoeTR0X29DQmRjMDlZRy1OQkNHRk5XaWk0bmRjQVF4NW9TSVhMcFRMemVZNFEzaGZrWWRwbGRPTHlxX2M1U0JJWDhNanFldTJDeW5YZnhnWGxfazhYY1NaOU9zSFhaWXFabVVtZDVuQUloRHo3ckZqdDAxZw?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQU2lsc3FrLXo4S1lodE02VFdNc3RlbGY5a2NTTTVjVmtPRDhic3FfME5UQmc3cWhVSWVjbFY0RlBpZ2dTUGMyX2J2N2hQSnBScjhFMjdrMUFXVzNjYldjcExQeEJvYkpEazUxQ3djbU9POXRpWjJpbjd3c3NqeGpKR0QxY0lod3JvdXd4QUFiQ2JmVXRaMmt2cUt4Z2dlNlloYTBpOE55RE40SUlmbG81WFplY1dfQQ?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxQTy11YjZDbFFZcDE0VWg3UkJXTGNrOHF5TjZfZ3ZSX3JSLUhwZUIzU0gtRlZQbUI4bERLTE1ZWXV2ZkxNdlp6b2RfM2dEUklSNEc1UFhEQWlzUW9TSFNUckRqOXNPbnhsazZNZUlJd01fOF8zdDZXZUNjb0ExOWYtejB4N1NxNmhEVUZMenNER21wbXpWNUE4X2ItREhQZS1IcmFfbWd2dzE4b0hXVXdDUERwdmVUTWxUaDd3al93?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQUWl6NDdVVHVoUnJ0TVJBaDRMWW1mX0U2M29TQ2xTbksyaXFWSDI0bldFYTBYOGdPcmN6bWFwSDhjZFpad3RDOFE1SFJ6azJaUDlLN05adEI4TlJfRlJxTW1kWWtqLWs2TjJIeUFVWWlTdUlHMUdfUVI0UzN0UVYySm9UYzM0aGtOTmZPYld3X2lrc3N1Q2RTaTVrbjVwT0E?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQci1qeVFnbVdRbUVhYm1FWkZPallwbTFJWXFqc3IybkxFbFlqX09oZXVLamMwaXpTaEZjb0hqODFRR19TQ1ItQkFaOXFhMU4yU1FhNFpZYUhHekhocktoQXVIQ21KTmlTM1ZLOHdxNUd5LU5kb2pMTWhfbzhVc1ZGS21NSko0cnhZMks5OWswNFFDYmR0MkE0b3JXWWVBd0QwTkZMakJR?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNTzlWV0NHWEFVLURNSi1Ua1FZQk5pUkRTZnRpWklvS3JCWEItZzNWLVlLWjFaTHZEUkl4dnJVcnlsRmdEOURLeHdaZmozVHVlbmhVU1lWYkdYb1d6OTJkMUJXUVFxamswRjZBTVZVZllwajAxNFd3NHFPYVhpT1NKWXF5OEFjdXVtN052TmVOVWtmdw?oc=5
- https://news.google.com/rss/articles/CBMibkFVX3lxTE9MNUlzT3liQ3N6bGx5RjJsLU5mNk5LdUFCVE8tNk1HMzBCbVlZa0F3Rzg5S3VSZjF5UlVLN2xSYXFqbS1ZX0oyS3BsbUVKOVliTXEzYVRsZTk2ZFk3bFpOc1ZXNGk3ckUtTkc5RGF3?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNTjI5ZjByTHA3QnJ6dVI5WGVVeFpwUWFUNXZCeno5Nk9NZXlQcHZDRHhWTnpGVXVJU2xYWGZMb1NTNEVnOWhoaUZUUEg2Nm55emdvVDBIMkNCQnFNZlFZX2lfQW9wLXhEbXdQdEU0cFpRbjZ1QjBwcWZ4TnJscnd1M29UVk9EV2dCc2hCNjE3MTlmZk5DdmZBNDR3?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNQ2xqdVc0Qi1tZ2lRbWVmeVVxZzZ5TnlHRl9fSlNiYXJ5VnBCNjREb012Q2RxRDE2OUF3SHVUek9GMkFCM01vck5aTXJkc3NQZWswZTRPY3BNQU4yN2lueHYyLXc0T3VSV3FzLWRBVzgwOWZYTDhBa3VXYWNZY3ZOZS0zUmZCX29pZGdxTGpLbl9MMGZTTjEzcl9fYTBSam5OM0pSNmJn?oc=5
- https://news.google.com/rss/articles/CBMi0wJBVV95cUxNLVl5MmpVTTY2Q1U0dk9tbFotRi0wOXAwcF9pVDE2UVQzZzN2WW1rcXR2QW9mX3RwZE1MZ1lreGdPU2l1WGZYVUxvN2xMeXpURWtrVVVrNm4zcVdoVFNFQjYzbjVPMlRBbDhFRVdpSzM1N0hyUWR2RFJJWGN3MG5KSExPWkVXNDd2TURfcUdDQmk1Q25BU2EwR3ZhaW9sM3BNUnBzNTA3cmJ3UC1fN1VQSUR6bGR6eWpaRUREeUI3cnZQWlhMM213OVlFR3JwQTVSLW1xSVV6VmhkQTBBTTlBTnhMOVhmLVoxYUJZRXk1WnNoMEN6Q0M2S0FSMlN3Q2xSZVptU1J0dGw2N0Y0ZGIyRmhyalI0eEp0a014dGxKbEFvN3ZCMTc4QVFxSC1hRjJmUUhkNDVnN3ZTeXA2NU5hRWtFVnBNdjNkdHNudVEwZ0JuVHM?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxPN3hZRnJJbk9zLWxkWm11ZEY2Nk1Mbkctd19kT3lUakI5enpDbldNRnlmSl90d3JIVUNBQWZ3ang1Y2d6RW5DUU9JNVotelVrNElzWG5VSDl3cktQU1RyckxrRFFZb1BoR0w1VXVtTGFHU2hiX3lmS1pKU2diUTBONHZHaEhId3BUQ050bEM4QW5nT3kzV2hXdkNEVTdsRjFfWWNGOE1TN0tZNXB3TXUxSXpqamQtX0Nkb045QzI2UEFmUExBTmVpb0hKbWxWVGNtNGgtOS1yQm4?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPenQ0X1kweC0yd1FQelFMQXdjMjFMbklTbWxMOXRzb056WElTbVZzVS0wUmVlVHVzYmNmUnlqSktuV1pON3ZwU2RabWpDV001clNIYW1fWDNSbEUtUkFDdHcyUHVpb3lxWFBQQ2c2bFF0VWxaczB6eklrZkZwSHd5YktyV1g3Q3p0SDZzVW5PcFl4TnZwbHBzMzFkb0lQampwWElEZ0FB?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPTjBCbjI0blNJMTVHeld3VzRjNHFSbHcxMXRCSlpYeDhmbFN6aUZSS05FYVI1SEhsTkUxZmJrNzdjeEFMTjZ1cWJpT3dhUGZKeFZQdFg3TC1wWG1kZEtsX25KOXNGYWdYQ2tkYy1INF9UVEFDaHFxQ1JCX0JLNU9DOVR4WXlkQ001bGtr?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQQU5mb3lfUm10QlcyU0hXTjA0dXVDdXlIVHRET0ZMd1ZyTWhSSENKa01wM0ctR194NE4zdmdfLVhSTkRZRXpseDlUVVhRZ01mZWY2LVZIbTBXMDJOdHhIUG9KNUMwN3VvTTRNNzBzVVFVZlRCclFlbENPNHJJWVh5Z3Rmd0NKYVJhXzg4eGtEZnRZRjc1N2dnel9Va2JtcTZFbkdCQzMtbHNvQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
