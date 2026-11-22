# MSFT Intelligence Report

- ticker: **MSFT**
- Report as_of: **2026-11-21**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/MSFT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MSFT/key-statistics/
- AI analysis snapshot as_of: **2026-11-21**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-22T04:58:20.753813+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 4, 'ai': 17, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261120T053808Z-e360129e/MSFT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 12 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 32.0%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 484.5200 |
| Return 1D (%) | -2.7654 |
| Return 1W (%) | -7.3345 |
| Return 1M (%) | -8.7266 |
| Return YTD (%) | 1.0165 |
| Return 1Y (%) | 2.1123 |
| Annualized volatility (%) | 34.0327 |
| Beta vs SPY | 0.9849 |
| Max drawdown (%) | -27.9702 |
| Sharpe (rf=0) | 0.2285 |
| Downside deviation (rf=0, %) | 21.8171 |
| Sortino (rf=0) | 0.3565 |
| Historical VaR 95% (1D, %) | 2.8530 |
| Historical ES 95% (1D, %) | 4.1000 |
| Correlation vs SPY | 0.4137 |
| Tracking error vs SPY (%) | 30.9845 |
| P/E (trailing) | 25.29 |
| P/B | 7.65 |
| EV/EBITDA | 17.83 |
| Revenue growth (%) | 18.80 |
| Forward P/E (estimate) | 20.02 |
| Gross margin (%) | 67.66 |
| Operating margin (%) | 47.10 |
| Return on equity (%) | 34.22 |
| Free cash flow yield (%) | 0.08 |
| MA50 | 518.8722 |
| Close vs MA50 (%) | -6.6206 |
| MA200 | 441.9259 |
| Close vs MA200 (%) | 9.6383 |
| RSI (14, Wilder) | 35.0152 |
| MACD (12,26) | -5.8943 |
| MACD signal (9) | -0.7262 |
| MACD histogram | -5.1681 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MSFT': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 484.5200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.7654 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -7.3345 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -8.7266 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 1.0165 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 2.1123 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.0327 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.8171 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3565 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8530 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.1000 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4137 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.9845 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.9849 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.9702 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2285 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 20.0208 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 67.6570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 47.1040 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 34.2210 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.0832 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 25.2881 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 35.0152 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -5.1681 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -6.6206 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.6383 -> Clearly above the moving-average trend level.

## TAILWINDS

### Microsoft Stock (MSFT) Forecast – Mizuho Stays Bullish on Strong Revenue Growth Prospects
- Summary: Microsoft Stock (MSFT) Forecast – Mizuho Stays Bullish on Strong Revenue Growth Prospects
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNbkpCQ3NWcTBELXRDand5VERMRC1yU1lKS0txQmlDWHEwTFljTU5SeVR6elRCZ1FzdkNCSEV2QU96TWRqTlpvcWNBamJQXzV4TV9TNFBKb1l6clVrTERjcVZPM09YRlFpcEp3cTNNSkJhV3p4OGk1X2ZiMzg2SlhuWkZNbUptcVhCa0w4bFIwN0RRNnAzbFQ4WGg1SUNlUlVFQXJV?oc=5>

### Microsoft Stock (MSFT) Rises 0.4% to $508.29 (Nov 18)
- Summary: Microsoft Stock (MSFT) Rises 0.4% to $508.29 (Nov 18)
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxNRDU5QzhENlNLSXBJMjNkRUllSFZhMHhOSkhWM1hGU3JaZmloRHJYZ3lCVWlHS21vUEVBM2N3UmJEV1FndlJScHdrZFJ6Rkloc05YdlMxV0lWQWJkUXc0QnY1QXd5UUZTeDVsdENvQjgwbXROcm1QNFR6VVpqTGMxaVlrZXo?oc=5>

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

### Microsoft Corporation (MSFT) Rose on Strong Fiscal Year-End Results and Robust Outlook
- Summary: Microsoft reported strong fiscal year-end results and a robust outlook, boosting investor confidence.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOOUctNExwQ2VPbVZTWGdBdjZWTnNhU1hjZUxQZWdUSzhhVWRKRUt2ZHZORkZ3V3dxc3RCbE83Ny1JX2o4NkxhZ2RxblFuTFdNUjJJaWZhT3VfQWxkZFN2RlVXclZlVU1Ua3FJbERLbHRkc1pFbjRpNlNZUHlKS2xYR1BNVDI3bWtUOXd3RmV6RjBwUWptb1ZiaVJsTkVyVGN4TENHR0pn?oc=5>

### Accelerating Azure Growth and Copilot Adoption Fuel Microsoft Corp.’s (MSFT) AI Momentum
- Summary: Azure and Copilot growth boost Microsoft’s AI momentum.
- Date: 2026-11-19 | Impact: high | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQeGRmcVNfdUJlRkItWGpUU3RkQVJTcnZIQlU5cjJjU3NsSUREMmVuRVBoZXNqODVoeTR0X29DQmRjMDlZRy1OQkNHRk5XaWk0bmRjQVF4NW9TSVhMcFRMemVZNFEzaGZrWWRwbGRPTHlxX2M1U0JJWDhNanFldTJDeW5YZnhnWGxfazhYY1NaOU9zSFhaWXFabVVtZDVuQUloRHo3ckZqdDAxZw?oc=5>

### Bill Ackman Says His Microsoft “Sale” Was Really a Swap Into Options
- Summary: Analyst commentary on Ackman’s MSFT option swap strategy.
- Date: 2026-11-19 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxOX1BvZHFVcWc0VGhsYUlJYmUzenZreG12bzJrcW82bjVENjBTTDhaX0t6OU5rdW8xMVNDWTNQUTdBSG81OFo1RWYyaUJaQV9QTTNnNkRmbHN2SmpWWUhiVjAtWFdpQzdIVnFVRHJ2aXpoT2pXNjg1WEdmeEw1NlRXYmlFejZfSkFMcmk1NUlOM040Um4xTkwxcVN2SmVzUnJ6Z0M4X0tyYW1GSzRMYkg0?oc=5>

### Analysts Are Bullish on Top Technology Stocks: Microsoft (MSFT), STMicroelectronics (STM)
- Summary: Analysts express optimism about Microsoft’s prospects, boosting investor sentiment.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi_wFBVV95cUxQS0RCNmNmeWRxUlpqbkF3QzFLQWgxZkRrVXZMVFNfcjZ1OGdMa1NsRFEyTXozd3dyR21Jcy1heVBneFNZOUVjZEV3N2VPTzRjT3BiZWU2NVF6VVJ1MngzQ0N6VlY2TmxJWGtpTXpKTGt1RkM4YkJGYUIzaDdtNUVXUTg2ejFEMEpObTNRSUl6aWljMDZzRk9yRENZcl95eTJwRk1MZDlMLTYyaXQ4eS01WUtNeE81aG5ja1lubDlGTHBEUGtsZzB0VmdkTnE1dk9jWmZOLXpQRzhnckdVTGVZRGUtb0hlRk1OTVUwYXRfLW1QMUQwNVJLRkJRMmZ6Q1U?oc=5>

### Microsoft (MSFT) and Its Rivals Are Making a Huge AI Bet – Here’s What Investors Should Know
- Summary: Microsoft is investing heavily in AI, positioning itself for future growth.
- Date: 2026-11-20 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQZkJwODVzRnptNlFrc3UtMlA0NUN2bkVNYnNDcGQ3MDBNRzdVbnJPT0Q1c21xNndPMUY5eVA4NzVCUW1fdkx3bGJUMnFUdTV6cjNPUkY4RWpCMXpsNHZjQVp0bHd6RVFmMEpxcGkyNEtNSWJZTklOdVd1Z1RwaWlJX3N1emMxQ0FYUjRaeHlzcXozeFV5bXgzbzZMUERoQQ?oc=5>

## HEADWINDS

### Microsoft MSFT Stock Drops but $500 Holds as New Cybersecurity Concerns Hit Tech
- Summary: Microsoft MSFT Stock Drops but $500 Holds as New Cybersecurity Concerns Hit Tech
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxQMzdIamo3aFJCeDlxRWVEZWJmdTNtNElVM3pER2ozc2tkNGlBa01XdmNfdDBURDVVVFgySXN0eXk3NEtHNGQ3dmJXMHRFTDZHOFRPSnlJZGpUY2ZzcTZqUjhXaHBaemc2dmV1VXloZnZqb3FZRzVVd0Vmd2JReUJHSmNUTURzbWQ0ajA4S1RhT096cFZUTThKVVR2MkVLRzVtc1VsVHlFd2NMMXZYaE15d2JyR3hDaVhYTWZCeDFVQQ?oc=5>

### What Could Stall Microsoft Stock’s Run?
- Summary: Article discusses potential factors that could hinder Microsoft’s stock performance.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPd1NYMThWX2pISm1GWnk1MGZFU0lxUi1lV2FIMVFJV3BJa3lvSmVlOXRJTEhHVm90cTFjOEhjVDc3OVRvbWVpc2FEMUVwRlQzOWJPQTVYYWREVEF0V0RQUWpZVjgwdWs1eDhsY21sMjdFZXFEaFNMaDVibW9ibjYyQ1gxYWxfRXd1cXJZN09zWGVEN2lZRHIwY3BYZ190aHM?oc=5>

### How Microsoft’s (MSFT) Valuation Crashed From 75x to 10x – Even as Earnings Kept Growing
- Summary: Valuation dropped sharply despite earnings growth, raising concerns.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQdmtjd3Z4UGFpS2c5OUNDX3FkMlFzNGo1WVROYThDcmVIZlRjRXBmbGluTmlrNERVNTRqYXk3UHpXZUxLM0lmUGttbV9rQVpKR3YyUnFMcXo0RV9iam9IRzFnTTk3cTV6dC12a2FDZmoyUEhJR09EUDBlUmIyS19zUVljQW45SnB3RUQtVE9ZLTEwWlVzaEx5cXJxbld4LWFrQmpV?oc=5>

## CATALYSTS

### Microsoft CEO explains why the company asked 60K workers to quit. How to know when to accept a buyout or turn it down
- Summary: Microsoft CEO explains why the company asked 60K workers to quit. How to know when to accept a buyout or turn it down
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNMzZYUVViV012NGpKNnFSYWRnbG8zc2VrWUV0anV6WXFieXg0RktiSXFqUnV0Y1VYeVpIQUoyczJyVEFuSnRWcTRkanNzSF8yQjdCc05WeDN1cWY5Zk4xaS1vM2F4NmpBamttMUtvVmdfZHpxbm4xX2gzcDBJVVlXMnRlOEotM0U3cm5XS3FxMTlqR1FTRlg0Y3R3T1RZSGs?oc=5>

### New Buy Rating for Microsoft (MSFT), the Technology Giant
- Summary: Analyst upgraded Microsoft to buy, boosting confidence.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNcllITFdRQy1wY0NxVWxIXzQxdUczaDdXeDdyU1NwcWQzdzB4LTlUajhjUS1HQVhZM29Dek1mVGlpczUwZXZYY1F2dVB4aFZMN0lHV2FoWERYRVdmakRWMlI1Q1VvV1BvTWJTODFzc3F2aHNzY0Y1U1Z1MjZfeE1LZlU2d3R6YVcxRXhoeFlLcEwtdzlQOTZUdzNjbHBKT1BiYy1mSzZBc2NtOUN0dzctQTkwYXoxTFk3UklOT1lKRkdWMTVIVDN5OVE4ZnlxN2ZvdmZXemV3?oc=5>

### Microsoft (MSFT): New Buy Recommendation for This Technology Giant
- Summary: Analyst issued a new buy recommendation for Microsoft.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi5AFBVV95cUxOVXd1YVdWMXBTM2F0NWJ4Q1FLaE1SU0NmWmgycVBWQkgweXhTTzZBZS1mdGxzUmtOYzVfcFRFeUJQcFRHYkZpQW5kYnVQbXBXelpMSVNqVEpLMWFUVC1qSHZwdU9ydnIxRzNGV2JUY3kxdU45eU1WakpkdHRCUGs5RzZJd2ZyZF8xbHVGX0dvRGQ3MWxjVmlVelNkY0s3bkFhbWcwQzU5dkNVUFl2ZUFSSWpDS1ZremEtNVNiN3hWVi1mVUZ3RWZ1aGMzdjlneEppcjNoTm03d19vbldnc3VzU2lfY28?oc=5>

### Microsoft Corporation (MSFT) Stock Forecasts
- Summary: Analysts provided stock forecasts for Microsoft.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPQTVtR182YU9iMFIxRHBBTHlWeFRJTWJmMDI4WWwyWUFmem1IWFBPeTYyY3pKQ3o1bkJBZnVwY0xwZ0ZsRHA2UHNzVGFMTjhiRnRMWEtNY2pJLWxnNm1uLTFpZ1cxdUxpZlVaaWl5d2ZtWlJPY2Q5SERuYWNncEQ3UnFlQkxxVTl3MDhOWA?oc=5>

### Key facts: Anthropic's $47.2B Azure Pledge; Intel Chips; MSFT $1B Stake
- Summary: Microsoft acquires a $1B stake, indicating expansion in Azure and AI partnerships.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxOUkU2MVNvazFLdzZkaEc3Qi15RXljajVmSkVLY1BqNXI4S09rWllSaGpzU2ZIS0VOWldWQ3Z2UmozT055SHBCLXZONU5KOEh4QUtVY3pyQnQtSi1EU0FGNUdJT3FndG9zTjFLSW9vMzRJMDd1Q0FzR2pnMUUxTTBOYmstek8tUzkzbHVPanZHYUhEMURZZTdKMFRkUHBWMGZiRmNSQVpCUG1qZG1lRUVwSG44QjBMZDJ2V1ltQVdINTFWM3BVd3Jz?oc=5>

### Pershing Square remains bullish on Microsoft despite selling 2M shares
- Summary: Investor Pershing Square maintains a positive outlook on Microsoft after divesting shares.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPcjRLdnBKSmtZbDBWSUlKTjR1SEVicUR6T2VROEptY2VIOU1odHFTR0xoZm8wS2pGenBYR3B2SkNrSFExMktIVFNLdnNkU3kzWkl2RmE3SktzTDZMUEdERDVRSXpyNFNCZjd1aUtNUHZob0FPbTVtUW92QWNkM1otRUJ2VlJ6UU9HUDdhVEhuR2VuVXlzODMyXy1sZlUxbmJfd1o5VU9EWnc5aUhW?oc=5>

### Microsoft emphasizes 'pay-for-performance' in its Azure cloud division: report
- Summary: Microsoft introduces pay-for-performance model for Azure cloud services.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPSjlwdzByRXV3R0NCMnZ3NU1VQktxYmNIdDVyaTZRNTRCSmtoU0k5NkpXcmdDTmFDNmZlUEw1dFRhRlp1anJJdmNqdzVERFpQX2xIajZ0c0FuZ2tiN0tTckhkSDB1dVFvb3U3eTIyUE1JX0hmSFN1N0RYaDZsNTVXLS1mWl9TSXF4Ums3UWJ4MlNjVHhfM3M4b0RZdWNuM0lNSkVER29CMFY4SDVuUUtsb29LQQ?oc=5>

## RISKS

### Microsoft’s CEO Says He’s “Extremely Sorry” for the Outlook Outage
- Summary: CEO apologizes for service outage, indicating operational risk.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQQU5mb3lfUm10QlcyU0hXTjA0dXVDdXlIVHRET0ZMd1ZyTWhSSENKa01wM0ctR194NE4zdmdfLVhSTkRZRXpseDlUVVhRZ01mZWY2LVZIbTBXMDJOdHhIUG9KNUMwN3VvTTRNNzBzVVFVZlRCclFlbENPNHJJWVh5Z3Rmd0NKYVJhXzg4eGtEZnRZRjc1N2dnel9Va2JtcTZFbkdCQzMtbHNvQQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MSFT** | **25.29** | **7.65** | **17.83** | **18.80** | **3,598,139,523,072.00 USD** | **2.11** |
| ORCL | 15.86 | 4.95 | 12.88 | 29.60 | 315,480,899,584.00 USD | -51.33 |
| GOOGL | 13.85 | 4.95 | 17.06 | 24.70 | 3,261,475,323,904.00 USD | -8.11 |
| AMZN | 19.95 | 4.35 | 15.56 | 12.10 | 2,668,898,811,904.00 USD | 13.67 |

Peers fetched as_of: 2026-11-21; MSFT reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-21

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

- https://news.google.com/rss/articles/CBMiowFBVV95cUxNbkpCQ3NWcTBELXRDand5VERMRC1yU1lKS0txQmlDWHEwTFljTU5SeVR6elRCZ1FzdkNCSEV2QU96TWRqTlpvcWNBamJQXzV4TV9TNFBKb1l6clVrTERjcVZPM09YRlFpcEp3cTNNSkJhV3p4OGk1X2ZiMzg2SlhuWkZNbUptcVhCa0w4bFIwN0RRNnAzbFQ4WGg1SUNlUlVFQXJV?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxNRDU5QzhENlNLSXBJMjNkRUllSFZhMHhOSkhWM1hGU3JaZmloRHJYZ3lCVWlHS21vUEVBM2N3UmJEV1FndlJScHdrZFJ6Rkloc05YdlMxV0lWQWJkUXc0QnY1QXd5UUZTeDVsdENvQjgwbXROcm1QNFR6VVpqTGMxaVlrZXo?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNalJYeUVUa3czcERnOXA2LUVJUlJaM0owQlJvZm9Gek1DeHZXV3lwREJFZVM5Nm9KVjdMbC1KRGJmeWg4Rk15M0FZV0ZMNEM0dF9wLXF3dWRpRjhZNVY4Y19fSU9ucUR0QVZKZ1hEQl91eVdnYmlZZ0E4X2RlWmxOWV9KTmpWcEZLZUxBYUJwV3plM3pUOU1MdzF3?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxOYjRsQUxKOXhBUjh2NlRZRDFiVGMwYUtWbUJXeXRJQmtLZFBZVThMTU1nbFUxY2UwWXg5d2R5a3p4ZzN1WW1ITF9ZSkV2Unh1TEczTkF3R3VyU1R6UWpYMkNWa0ZreWd6RzE5b0NXeGQ0dlAzaDVvbG96RHhDYWV5dVFUdWx0NVY1OVN6TjB5RmxneUxCendmTGtmTEFsaHl3OGRuQjZCYlFIOE9scG9teTk4OUZrdHlvTEhKNnNzQQ?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQeGlPQ2Y0R2NqTU9qOS1oUEo3dnBISkxVeGtVR1ZLbjlpV21sbW5HNk5zZ0hXamZFZE1XVTNva0xCaDZXTG93YjB5dTZqUF9UMjVRZEpfUTNHeDlGMUQ2U2xhc21IdWNxODdzdEg0WnpidnhwcXlNaVNtT3ZJNl95TVhXTUNlLU9XVVExcS1wems?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOOUctNExwQ2VPbVZTWGdBdjZWTnNhU1hjZUxQZWdUSzhhVWRKRUt2ZHZORkZ3V3dxc3RCbE83Ny1JX2o4NkxhZ2RxblFuTFdNUjJJaWZhT3VfQWxkZFN2RlVXclZlVU1Ua3FJbERLbHRkc1pFbjRpNlNZUHlKS2xYR1BNVDI3bWtUOXd3RmV6RjBwUWptb1ZiaVJsTkVyVGN4TENHR0pn?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQeGRmcVNfdUJlRkItWGpUU3RkQVJTcnZIQlU5cjJjU3NsSUREMmVuRVBoZXNqODVoeTR0X29DQmRjMDlZRy1OQkNHRk5XaWk0bmRjQVF4NW9TSVhMcFRMemVZNFEzaGZrWWRwbGRPTHlxX2M1U0JJWDhNanFldTJDeW5YZnhnWGxfazhYY1NaOU9zSFhaWXFabVVtZDVuQUloRHo3ckZqdDAxZw?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxOX1BvZHFVcWc0VGhsYUlJYmUzenZreG12bzJrcW82bjVENjBTTDhaX0t6OU5rdW8xMVNDWTNQUTdBSG81OFo1RWYyaUJaQV9QTTNnNkRmbHN2SmpWWUhiVjAtWFdpQzdIVnFVRHJ2aXpoT2pXNjg1WEdmeEw1NlRXYmlFejZfSkFMcmk1NUlOM040Um4xTkwxcVN2SmVzUnJ6Z0M4X0tyYW1GSzRMYkg0?oc=5
- https://news.google.com/rss/articles/CBMi_wFBVV95cUxQS0RCNmNmeWRxUlpqbkF3QzFLQWgxZkRrVXZMVFNfcjZ1OGdMa1NsRFEyTXozd3dyR21Jcy1heVBneFNZOUVjZEV3N2VPTzRjT3BiZWU2NVF6VVJ1MngzQ0N6VlY2TmxJWGtpTXpKTGt1RkM4YkJGYUIzaDdtNUVXUTg2ejFEMEpObTNRSUl6aWljMDZzRk9yRENZcl95eTJwRk1MZDlMLTYyaXQ4eS01WUtNeE81aG5ja1lubDlGTHBEUGtsZzB0VmdkTnE1dk9jWmZOLXpQRzhnckdVTGVZRGUtb0hlRk1OTVUwYXRfLW1QMUQwNVJLRkJRMmZ6Q1U?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQZkJwODVzRnptNlFrc3UtMlA0NUN2bkVNYnNDcGQ3MDBNRzdVbnJPT0Q1c21xNndPMUY5eVA4NzVCUW1fdkx3bGJUMnFUdTV6cjNPUkY4RWpCMXpsNHZjQVp0bHd6RVFmMEpxcGkyNEtNSWJZTklOdVd1Z1RwaWlJX3N1emMxQ0FYUjRaeHlzcXozeFV5bXgzbzZMUERoQQ?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxQMzdIamo3aFJCeDlxRWVEZWJmdTNtNElVM3pER2ozc2tkNGlBa01XdmNfdDBURDVVVFgySXN0eXk3NEtHNGQ3dmJXMHRFTDZHOFRPSnlJZGpUY2ZzcTZqUjhXaHBaemc2dmV1VXloZnZqb3FZRzVVd0Vmd2JReUJHSmNUTURzbWQ0ajA4S1RhT096cFZUTThKVVR2MkVLRzVtc1VsVHlFd2NMMXZYaE15d2JyR3hDaVhYTWZCeDFVQQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPd1NYMThWX2pISm1GWnk1MGZFU0lxUi1lV2FIMVFJV3BJa3lvSmVlOXRJTEhHVm90cTFjOEhjVDc3OVRvbWVpc2FEMUVwRlQzOWJPQTVYYWREVEF0V0RQUWpZVjgwdWs1eDhsY21sMjdFZXFEaFNMaDVibW9ibjYyQ1gxYWxfRXd1cXJZN09zWGVEN2lZRHIwY3BYZ190aHM?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQdmtjd3Z4UGFpS2c5OUNDX3FkMlFzNGo1WVROYThDcmVIZlRjRXBmbGluTmlrNERVNTRqYXk3UHpXZUxLM0lmUGttbV9rQVpKR3YyUnFMcXo0RV9iam9IRzFnTTk3cTV6dC12a2FDZmoyUEhJR09EUDBlUmIyS19zUVljQW45SnB3RUQtVE9ZLTEwWlVzaEx5cXJxbld4LWFrQmpV?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNMzZYUVViV012NGpKNnFSYWRnbG8zc2VrWUV0anV6WXFieXg0RktiSXFqUnV0Y1VYeVpIQUoyczJyVEFuSnRWcTRkanNzSF8yQjdCc05WeDN1cWY5Zk4xaS1vM2F4NmpBamttMUtvVmdfZHpxbm4xX2gzcDBJVVlXMnRlOEotM0U3cm5XS3FxMTlqR1FTRlg0Y3R3T1RZSGs?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNcllITFdRQy1wY0NxVWxIXzQxdUczaDdXeDdyU1NwcWQzdzB4LTlUajhjUS1HQVhZM29Dek1mVGlpczUwZXZYY1F2dVB4aFZMN0lHV2FoWERYRVdmakRWMlI1Q1VvV1BvTWJTODFzc3F2aHNzY0Y1U1Z1MjZfeE1LZlU2d3R6YVcxRXhoeFlLcEwtdzlQOTZUdzNjbHBKT1BiYy1mSzZBc2NtOUN0dzctQTkwYXoxTFk3UklOT1lKRkdWMTVIVDN5OVE4ZnlxN2ZvdmZXemV3?oc=5
- https://news.google.com/rss/articles/CBMi5AFBVV95cUxOVXd1YVdWMXBTM2F0NWJ4Q1FLaE1SU0NmWmgycVBWQkgweXhTTzZBZS1mdGxzUmtOYzVfcFRFeUJQcFRHYkZpQW5kYnVQbXBXelpMSVNqVEpLMWFUVC1qSHZwdU9ydnIxRzNGV2JUY3kxdU45eU1WakpkdHRCUGs5RzZJd2ZyZF8xbHVGX0dvRGQ3MWxjVmlVelNkY0s3bkFhbWcwQzU5dkNVUFl2ZUFSSWpDS1ZremEtNVNiN3hWVi1mVUZ3RWZ1aGMzdjlneEppcjNoTm03d19vbldnc3VzU2lfY28?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPQTVtR182YU9iMFIxRHBBTHlWeFRJTWJmMDI4WWwyWUFmem1IWFBPeTYyY3pKQ3o1bkJBZnVwY0xwZ0ZsRHA2UHNzVGFMTjhiRnRMWEtNY2pJLWxnNm1uLTFpZ1cxdUxpZlVaaWl5d2ZtWlJPY2Q5SERuYWNncEQ3UnFlQkxxVTl3MDhOWA?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxOUkU2MVNvazFLdzZkaEc3Qi15RXljajVmSkVLY1BqNXI4S09rWllSaGpzU2ZIS0VOWldWQ3Z2UmozT055SHBCLXZONU5KOEh4QUtVY3pyQnQtSi1EU0FGNUdJT3FndG9zTjFLSW9vMzRJMDd1Q0FzR2pnMUUxTTBOYmstek8tUzkzbHVPanZHYUhEMURZZTdKMFRkUHBWMGZiRmNSQVpCUG1qZG1lRUVwSG44QjBMZDJ2V1ltQVdINTFWM3BVd3Jz?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPcjRLdnBKSmtZbDBWSUlKTjR1SEVicUR6T2VROEptY2VIOU1odHFTR0xoZm8wS2pGenBYR3B2SkNrSFExMktIVFNLdnNkU3kzWkl2RmE3SktzTDZMUEdERDVRSXpyNFNCZjd1aUtNUHZob0FPbTVtUW92QWNkM1otRUJ2VlJ6UU9HUDdhVEhuR2VuVXlzODMyXy1sZlUxbmJfd1o5VU9EWnc5aUhW?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxPSjlwdzByRXV3R0NCMnZ3NU1VQktxYmNIdDVyaTZRNTRCSmtoU0k5NkpXcmdDTmFDNmZlUEw1dFRhRlp1anJJdmNqdzVERFpQX2xIajZ0c0FuZ2tiN0tTckhkSDB1dVFvb3U3eTIyUE1JX0hmSFN1N0RYaDZsNTVXLS1mWl9TSXF4Ums3UWJ4MlNjVHhfM3M4b0RZdWNuM0lNSkVER29CMFY4SDVuUUtsb29LQQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQQU5mb3lfUm10QlcyU0hXTjA0dXVDdXlIVHRET0ZMd1ZyTWhSSENKa01wM0ctR194NE4zdmdfLVhSTkRZRXpseDlUVVhRZ01mZWY2LVZIbTBXMDJOdHhIUG9KNUMwN3VvTTRNNzBzVVFVZlRCclFlbENPNHJJWVh5Z3Rmd0NKYVJhXzg4eGtEZnRZRjc1N2dnel9Va2JtcTZFbkdCQzMtbHNvQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
