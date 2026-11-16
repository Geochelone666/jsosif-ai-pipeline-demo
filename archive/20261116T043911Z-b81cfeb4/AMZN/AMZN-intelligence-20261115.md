# AMZN Intelligence Report

- ticker: **AMZN**
- Report as_of: **2026-11-15**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/AMZN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMZN/key-statistics/
- AI analysis snapshot as_of: **2026-11-15**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-16T04:45:21.876916+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 9, 'ai': 11, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261115T044154Z-6abfba73/AMZN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 10 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 37.5%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 266.6600 |
| Return 1D (%) | -0.2917 |
| Return 1W (%) | 2.8384 |
| Return 1M (%) | 3.1248 |
| Return YTD (%) | 15.5272 |
| Return 1Y (%) | 12.2401 |
| Annualized volatility (%) | 33.8859 |
| Beta vs SPY | 1.3210 |
| Max drawdown (%) | -19.6419 |
| Sharpe (rf=0) | 0.5077 |
| Downside deviation (rf=0, %) | 20.8312 |
| Sortino (rf=0) | 0.8259 |
| Historical VaR 95% (1D, %) | 2.8374 |
| Historical ES 95% (1D, %) | 4.0742 |
| Correlation vs SPY | 0.5315 |
| Tracking error vs SPY (%) | 29.0356 |
| P/E (trailing) | 21.56 |
| P/B | 4.70 |
| EV/EBITDA | 16.73 |
| Revenue growth (%) | 12.10 |
| Forward P/E (estimate) | 24.41 |
| Gross margin (%) | 51.37 |
| Operating margin (%) | 13.09 |
| Return on equity (%) | 27.42 |
| Free cash flow yield (%) | -1.20 |
| MA50 | 254.8116 |
| Close vs MA50 (%) | 4.6499 |
| MA200 | 244.5955 |
| Close vs MA200 (%) | 9.0208 |
| RSI (14, Wilder) | 57.4345 |
| MACD (12,26) | 3.5019 |
| MACD signal (9) | 1.7996 |
| MACD histogram | 1.7023 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMZN': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 266.6600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.2917 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.8384 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.1248 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 15.5272 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 12.2401 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.8859 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.8312 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.8259 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8374 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.0742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5315 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.0356 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3210 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.6419 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5077 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.4058 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 51.3740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 13.0870 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.4160 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -1.2045 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.5570 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 57.4345 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.7023 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 4.6499 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.0208 -> Clearly above the moving-average trend level.

## TAILWINDS

### Amazon Stock (AMZN) Climbs on Reports It Wants to Be ‘Go-To’ Search Engine for Shoppers
- Summary: Amazon Stock (AMZN) Climbs on Reports It Wants to Be ‘Go-To’ Search Engine for Shoppers
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxQYzJTVFNQMURzZDVQTHlWVkVMQV9jb0lhSkRZM1prTl9KQm9qQXpUd29WNEhzSXhRVXo0Qy13enRueGZwTHVhQ3B1LTJrY3RGSGpOOUQ3c2cwT0hRYjBBeU1BaFljX0ZoOGxWV0VnSWRiMjl6VmJjTXVMWXlKb2RVc2ZITmdQWElmNjlLRmk4SGFLUDlGdFRJZTBGd1pPWEMwbzJFSlBLVy1ObkVuZmVELVA1NA?oc=5>

### AWS Will Keep Amazon Profitable For Years To Come
- Summary: AWS continues to drive Amazon’s profitability into the future.
- Date: 2026-11-12 | Impact: high | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQVVNPUTA5NDJDMWlEOTdhaXlNZ3NsTzRWT1RJQkJQQmhEZjRyN0VoV082blR5VEh5dzNEWkFvU2pTTFhrUEk0cG1KWExNaTh4dEE1R1lhZTVGWkVIb1pQMjF0ZjFDRnZ1WTNROTZhYWlaMDhLZzZqQXR1VlFlV1ZMOWs3cWVkVVlwMG9maUhoUTRqbmVZ?oc=5>

### Why Amazon (AMZN) stock is up today
- Summary: Amazon shares rise today, indicating positive market sentiment.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPSmtpSlppcWtONkZFU2NsbkpzU1RzUXFDMzAzNDBnelNLc1ZadnoxMUpSemNvN1phamhHTnJIUzBDLWw4TzAwWFdpOG0xX2tCWTBaTzBUay1GMkdSRFRvU0RBcFRSc1BqVVJJV2ZDLU5SdUdCckd5TUo4XzBVVGQtLVp3U2NwRVpQbE5PMklUbTdZWjViZThEOXpkdmZGWjlkdkN6QVRqQ2xrUQ?oc=5>

## HEADWINDS

### Amazon Stock (AMZN) Falls 1.7% on Anthropic IPO Filing (Nov 11)
- Summary: Amazon Stock (AMZN) Falls 1.7% on Anthropic IPO Filing (Nov 11)
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxPTnFTRlNiXzM3Qk5oZDhsSkRnRU1GZm9KN2x0eDIyWkZ5bV9TZF9sdVFkV1hzRWU2VDhkN3lZN3FkeWtzUkUxZjlhRVRVRk4yWkJRb3p2dkNqZXRkczJrd1RrWkFIV1I0TnRZV2E4c1RuVjlwYmhVWXBuNEF6Z3dvNQ?oc=5>

### Amazon.com, Inc. (AMZN) Sold Off After AWS Growth Accelerated: What Changed?
- Summary: Amazon stock fell after accelerated AWS growth, indicating potential concerns.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNT2w3Um9jU09tYUlBRXFqYXZkZ3NxbG9Mb2k0ZnA0X0lZR2hlNFZONHJqZzg4aGoxbGJ4TUNLOGhPZUVOZzBuek9JTXlGWjVmbFZpLWFuNXFPU0dMd3ZfaGFTaWt0TDNqWF9OQ1FMMFN3U3h5dTlJUUZVVnE2NWUtdkVTSU85WjVmcVA2YktRNDdDdWc?oc=5>

### What's Wrong With Amazon.com (AMZN) Stock, and Is It a Buy in November?
- Summary: Analyst questions Amazon's valuation, suggesting potential downside.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOMFl3MDR4U2RDeG1zaEdBOFNtN2dHYnVZYTNwdkIwVk1YaVVEaFFJR0dSM19kaUVzbU1PQVVRcHZIWEZLb0czYXZlUXJzOU1ybWtlTWRyR3ducktjeG5NS08xTXJTTkNfMjNrM2h6UHk3ekNvNWNwTHhrQzBwd1JLZjdKSzdrYWhQZXZPNjBFZGJhemlUMlE4?oc=5>

## CATALYSTS

### Amazon Has Quietly Recouped Its Post Q3 Earnings Losses. AMZN Stock Could Hit $300 Next.
- Summary: Amazon Has Quietly Recouped Its Post Q3 Earnings Losses. AMZN Stock Could Hit $300 Next.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxNVDFMMWpzTHFWNVpraFphOVZad0Rza2psdnFrb3UwU2FES3JEZ2VaNHNudE80T2NOejIwTDJUaXJBMFdFSzNQZjFNYXZmc2tucTlPUXFobVpRLUJva2lGb0ItbVR1SkktLWhuaXRaUDA2VVV5SlJpSE5zaldBd19fSE5LNDFRbWZuLUZNT3l4VkRtTVRjRFIwNy15ZzdNWXZSSkg2TVFtUmN6Y2ZwbF9oaFJoby1ORER1UmRXVkNhQjRVaTF6b3dqMg?oc=5>

### Amazon.com, Inc. $AMZN Stock: VestGen Advisors LLC Reduces Stake
- Summary: Amazon.com, Inc. $AMZN Stock: VestGen Advisors LLC Reduces Stake
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxQQ2NYcEpZVmJ4VnhJcFgtRlVSZHh2VmxLS2QzZ0pIbUpjU0liS1Zvb1JFX3dJblc2MzdBeXY4QlRoRlA0bTZncmpNUG5jUjNxamN2OG5UU2k5YnRQdXd6U3Q1SE5tMHB3T3EyVFF5a3pEQzFySUp5MFdCV2Q0Y1FWWm9uc1kzWFRNRWtpbFh0ZzJJUm90TVNMdEZiWEhSZS1jZV9ZSC1tSU52aTF5NXB4bjdhWGNMTWZSN1Z4QQ?oc=5>

### Amazon.com, Inc. $AMZN Stock: Vantage Investment Partners LLC Cuts Holdings
- Summary: Amazon.com, Inc. $AMZN Stock: Vantage Investment Partners LLC Cuts Holdings
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxOX0hHWTRrdUtyTzJlTzQwdnA5MDZJMktkV1BiTnRmZkRSdkhIaXNZaVAySVpxWFo3Z2d0MzF5cy1lYWt0OGJ5NnlZR1NaWHBoVVNfZ1pIbElBdGNTR0tjb25MV0pleUJZZmVuTVhnOGJMcWpYQ2dtNlNZU3J1akRma09PNDBSaERJUWxwUGxwaEZYVTg0Vnk4QXdDNVFUeGFJSUxVUElpaEFlWXVNWWlEcmhmNWR5M0lueGJ1SmFpcmJRWFRmT3Jla2c2dw?oc=5>

### Amazon.com, Inc. $AMZN Stock Sold by Mcdonald Capital Investors Inc. CA
- Summary: Amazon.com, Inc. $AMZN Stock Sold by Mcdonald Capital Investors Inc. CA
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxQbEc2Y3ZfOXp3bWpROVRSWVpjQ2lMdzY3bWhHM1FWcVFwemYyX3hhX1BRSmYwb2s0TDN6Q3hlQURUZWlMQ2Q4N3d3MHI2aUhCc3JSY1BCaWtpSC1RUzVCZ3FKbFhaYmZGNHM1N3JJQkdTZGJ4ZGJnby1pUEhfZVNiYUI5Sk5abTVLcjJFWlJTbXM1T0NRYkpaMV9RVFNOeldLOGNDbXBqM3NHMGJxazNHMkpGdU5KSk5GX280ZjlUVVFmM0E5ZkE?oc=5>

### Amazon.com, Inc. $AMZN Stock: WestEnd Advisors LLC Reduces Stake
- Summary: Amazon.com, Inc. $AMZN Stock: WestEnd Advisors LLC Reduces Stake
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxQM3AyVmJoNy02Wnczek52endTSkZJaHVGNmszR2dtbTZLX3VxRG1SNVVmYTI4bDhqLTVweW1jdW8tYW85Nmgzc25qcmNCWEFmaUtBR3BaR05ZWnhNWEt3NXIyaFNOaEZxbVZNRHlRcWZ4QU40S3JpWmtCS19Obl9aSTNwSkNmR3IxQmtxSUVOQ0s5ZFBVR0FLR1NJYnNzUW9yU0RhOGtzeWJUTm9NbUcwcUFCNzEzQlVJZjF1SQ?oc=5>

### Amazon.com, Inc. $AMZN Stock: Axon Capital LP Reduces Position
- Summary: Amazon.com, Inc. $AMZN Stock: Axon Capital LP Reduces Position
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOVHVJZ1B0aUNQYW5WNjBHc0cwSlJvbzNGVEFQQ2MwZ2JyRjZCcWdyQ2lJbjJBM2xCdzVpNkdCRjRqc0VXWXBXZWpYblJRbjgwa2t3WVdVNzZVYVZubUFQZlBSUHM4QTM4OWFEbV9oSXVpWU5hR0pOMll2RFJaQXpLUkhmcFR4ZkJJelpFVnlad3pNd1QtY3AyVkdkak5qV3hUXzZsOTJOQVNfYXZONlZXc2pKbmxNcWhIWGc?oc=5>

### Amazon.com, Inc. $AMZN Stock Acquired by AMI Investment Management Inc.
- Summary: Amazon.com, Inc. $AMZN Stock Acquired by AMI Investment Management Inc.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxQQ1E2VFNXck13cmZWMWJhVXRTeWxzV1FKWHpTUFJlcm9QblJKQ2FBdk04dHFNWXJHcEZDUHROUlU1enZ3OC1BNUZFRm5FTnhfMlFMM1ZuQzVzdzYzM3hUalgyRW1tZE5LU3pXaHZ1VUQ1c0ZNd2RUWWVKQ0dVU1BtNjBfNnkzM25kVU5rR0UwOWVyV19fLU05WngwNnV3a1g5WDIzOE1WdFl0MTA0YzlNMExVeUZHcGV1YzFaNk9OczhaSWFpTmc?oc=5>

### Dear Amazon Stock Fans, Mark Your Calendars for November 19
- Summary: Upcoming event on November 19 likely earnings release.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxQMnJtUndPUnpyWXp5MHlQSzF1Tm5reUZubHRqSk5GU3dOY2RQU3FqTUEyWmdOYjNMNjVYMC1neWdkOXRaWHpHZkRiUEJkcno3MDBWYVp2U0xKWXM2d0pMM2xPUnFkZXBzaVUyZHF3aklEWGdCLW9EcktqQU5tSHN0T3pKUThTNUZnakZ2TW11TzBMT0h5UHhFZ1Q2M2RVS2ZFRjdtTg?oc=5>

### Amazon sets Black Friday and Cyber Week plans (AMZN:NASDAQ)
- Summary: Amazon announces its Black Friday and Cyber Week schedule, outlining promotional plans and expected traffic.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQQ0RfWi1DdG9pbllGTWhYLXN1VzRla0RMOEx6TlhjZDdsb3h2WXpLaF9EVWhKZkJpSXlTeHgwTzkyWm56N3NkTlpUeVkwVTMtMUp1bHo0N2RBN0lmX1JlQ2xQN1BiZmFveEFRWmVjdEYwdXNYRkFqY3lLVEtvYUZOOVVndkh1UlcxVTBB?oc=5>

### Amazon.com, Inc. $AMZN Stock: Sigma Investment Counselors Inc. Grows Position
- Summary: Investment firm increases Amazon holdings, signaling confidence.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNRFhzZ3ljMXpNQU54ZzVEN0kzWV9wVjVWUnZLSTdSa0xkS1FnVEFDdWd1QVZzc3RraEZ6VHVjcnVrODgyMmVmbDMzX2lSZlp0QkRiRThmN2V1OTBmR0xiZXZmcWFSajg2SHRaeVpLMTFtSU8wMUp3NmYyakg1VkIzYnNhOVdrM3p2MjNabmwxb2txcmNzWG01anVCR0gyOHV0VzVrMUFrQjhSQmV1eDB3YkpQWlVNSFFDeHhqSldjTjBJNTg5TWlHTF9BZXU?oc=5>

### Amazon.com, Inc. $AMZN Stock: Convergence Financial LLC Decreases Holdings
- Summary: Investment firm reduces Amazon holdings, indicating potential concerns.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxNbzBHZjM2QmdlRWpVeU1raGtqZmR5aktRczJNYkFsOUphYmprUVdLbW1vRlpGaHd3RXV1YWJnbjhwdlFXV0dreVJFN2poLWMxTGE0OWpHODBpaC1VelhTMVpMTzU4WHYxRFJUMGtDaUlxdnlPT2FJSk11c0FXeDYyUHdyQjFzVDZMNGU4ZDdlMGhGRnJfUzhQejU3c2VLM0d2R2VxMlgzYktrTU1IcHRqVzMtRlJGTURzSzdDcDlpckUyYnUybC1GS3Jn?oc=5>

## RISKS

### Amazon: AI Bet Getting Riskier (NASDAQ:AMZN)
- Summary: Amazon is increasing its AI investment, raising potential risks to its operations and financials.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiekFVX3lxTE1COEZ0M0p2RHl5US1uaEtOckxaRlRXUXRMc1hlR01pNE4yV0NGTHJIb0Vma3FzZUtKX3RCbVg3ZmpUNHpnaHJZeTBjVFV0YmdFWDc0R2N5RFRObTY0bllEUU15N0J0aGFkUWdNdF9HOHg0WWtMSDJpdTl3?oc=5>

### Will Rising AI Capex Weigh on Amazon's Free Cash Flow Prospects?
- Summary: Higher AI capital expenditures could reduce Amazon's free cash flow, posing a potential risk to profitability.
- Date: 2026-11-11 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxNaWZxTUVPSUtleUJrb2VoMnh2Z2NrTkxGRlRZMXdDcm53S2ROajhOcG9vZ3dkVnRUcVhBLUhzcWMyVXF1RUFhU01BM2lLQVVMSFRJWWZYTXRjenBCaHpTRE5ZcjMtOVNfdTloc1gtZ3hDaE1kTTIwWVRYSTJnaGwzemJGTXpBTlVNTXk1eVVQWVFOdDZBZjZ2QnNNWHI5UFJCUUMzRlpkcVhyM09xUEN5eHkxci1zR0dKbVNR?oc=5>

### Rocket failure destroys 40 Amazon satellites, threatening broadband rollout (AMZN:NASDAQ)
- Summary: Satellite launch failure threatens Amazon's broadband expansion.
- Date: 2026-11-15 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxPWDhBeDRCZ21nOExrVzluVTk3dWpYQlE2VGgtSVUyRFdXSUI0VVJybVNQTms5V2czZjNtRE1QZ0xTM2NwUWwyUmNsSS10dm5CVE5PeGJ1QVl2djlXNFI2NVhKN0F6YVVfdEF1aE1lWUw2ZFEyT1B5VWM4WVF6VUVncDVfSGE0bzA2RjZrSjdwX3ZlSDhISVRQT2Vzc3pFZlVKVFNmRDNJaG5vcGxVTjhZX2h3?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMZN** | **21.56** | **4.70** | **16.73** | **12.10** | **2,883,431,432,192.00 USD** | **12.24** |
| WMT | 46.41 | 10.36 | 24.65 | 5.90 | 1,016,233,525,248.00 USD | 25.97 |
| MSFT | 27.34 | 8.27 | 19.25 | 18.80 | 3,890,434,801,664.00 USD | 4.95 |
| GOOGL | 15.44 | 5.51 | 19.08 | 24.70 | 3,636,196,016,128.00 USD | 6.45 |

Peers fetched as_of: 2026-11-15; AMZN reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-15

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-30
- Revenue (latest available single quarter): 201,944,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 20,685,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiswFBVV95cUxQYzJTVFNQMURzZDVQTHlWVkVMQV9jb0lhSkRZM1prTl9KQm9qQXpUd29WNEhzSXhRVXo0Qy13enRueGZwTHVhQ3B1LTJrY3RGSGpOOUQ3c2cwT0hRYjBBeU1BaFljX0ZoOGxWV0VnSWRiMjl6VmJjTXVMWXlKb2RVc2ZITmdQWElmNjlLRmk4SGFLUDlGdFRJZTBGd1pPWEMwbzJFSlBLVy1ObkVuZmVELVA1NA?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQVVNPUTA5NDJDMWlEOTdhaXlNZ3NsTzRWT1RJQkJQQmhEZjRyN0VoV082blR5VEh5dzNEWkFvU2pTTFhrUEk0cG1KWExNaTh4dEE1R1lhZTVGWkVIb1pQMjF0ZjFDRnZ1WTNROTZhYWlaMDhLZzZqQXR1VlFlV1ZMOWs3cWVkVVlwMG9maUhoUTRqbmVZ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPSmtpSlppcWtONkZFU2NsbkpzU1RzUXFDMzAzNDBnelNLc1ZadnoxMUpSemNvN1phamhHTnJIUzBDLWw4TzAwWFdpOG0xX2tCWTBaTzBUay1GMkdSRFRvU0RBcFRSc1BqVVJJV2ZDLU5SdUdCckd5TUo4XzBVVGQtLVp3U2NwRVpQbE5PMklUbTdZWjViZThEOXpkdmZGWjlkdkN6QVRqQ2xrUQ?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxPTnFTRlNiXzM3Qk5oZDhsSkRnRU1GZm9KN2x0eDIyWkZ5bV9TZF9sdVFkV1hzRWU2VDhkN3lZN3FkeWtzUkUxZjlhRVRVRk4yWkJRb3p2dkNqZXRkczJrd1RrWkFIV1I0TnRZV2E4c1RuVjlwYmhVWXBuNEF6Z3dvNQ?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNT2w3Um9jU09tYUlBRXFqYXZkZ3NxbG9Mb2k0ZnA0X0lZR2hlNFZONHJqZzg4aGoxbGJ4TUNLOGhPZUVOZzBuek9JTXlGWjVmbFZpLWFuNXFPU0dMd3ZfaGFTaWt0TDNqWF9OQ1FMMFN3U3h5dTlJUUZVVnE2NWUtdkVTSU85WjVmcVA2YktRNDdDdWc?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOMFl3MDR4U2RDeG1zaEdBOFNtN2dHYnVZYTNwdkIwVk1YaVVEaFFJR0dSM19kaUVzbU1PQVVRcHZIWEZLb0czYXZlUXJzOU1ybWtlTWRyR3ducktjeG5NS08xTXJTTkNfMjNrM2h6UHk3ekNvNWNwTHhrQzBwd1JLZjdKSzdrYWhQZXZPNjBFZGJhemlUMlE4?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQcUx4anBZX18yWlJYR2QzZ2ZUNHhubUJLWHU0MkplNFRDb1RXMFB6d0VmcVhwSGszbWV1MWFLZURwa2RRZTNQYl8tMVRVa2ZiWXVDOVlfZ0dEZDFPdGEtODl5cTUtSE1JdnVyNWlFWkRNVHk2TXlDNjZWeHR5YzZ1d0xjMlZQVGlYcGdVSFNIdXJJTzQzU29v?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxNVDFMMWpzTHFWNVpraFphOVZad0Rza2psdnFrb3UwU2FES3JEZ2VaNHNudE80T2NOejIwTDJUaXJBMFdFSzNQZjFNYXZmc2tucTlPUXFobVpRLUJva2lGb0ItbVR1SkktLWhuaXRaUDA2VVV5SlJpSE5zaldBd19fSE5LNDFRbWZuLUZNT3l4VkRtTVRjRFIwNy15ZzdNWXZSSkg2TVFtUmN6Y2ZwbF9oaFJoby1ORER1UmRXVkNhQjRVaTF6b3dqMg?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxQQ2NYcEpZVmJ4VnhJcFgtRlVSZHh2VmxLS2QzZ0pIbUpjU0liS1Zvb1JFX3dJblc2MzdBeXY4QlRoRlA0bTZncmpNUG5jUjNxamN2OG5UU2k5YnRQdXd6U3Q1SE5tMHB3T3EyVFF5a3pEQzFySUp5MFdCV2Q0Y1FWWm9uc1kzWFRNRWtpbFh0ZzJJUm90TVNMdEZiWEhSZS1jZV9ZSC1tSU52aTF5NXB4bjdhWGNMTWZSN1Z4QQ?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxOX0hHWTRrdUtyTzJlTzQwdnA5MDZJMktkV1BiTnRmZkRSdkhIaXNZaVAySVpxWFo3Z2d0MzF5cy1lYWt0OGJ5NnlZR1NaWHBoVVNfZ1pIbElBdGNTR0tjb25MV0pleUJZZmVuTVhnOGJMcWpYQ2dtNlNZU3J1akRma09PNDBSaERJUWxwUGxwaEZYVTg0Vnk4QXdDNVFUeGFJSUxVUElpaEFlWXVNWWlEcmhmNWR5M0lueGJ1SmFpcmJRWFRmT3Jla2c2dw?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxQbEc2Y3ZfOXp3bWpROVRSWVpjQ2lMdzY3bWhHM1FWcVFwemYyX3hhX1BRSmYwb2s0TDN6Q3hlQURUZWlMQ2Q4N3d3MHI2aUhCc3JSY1BCaWtpSC1RUzVCZ3FKbFhaYmZGNHM1N3JJQkdTZGJ4ZGJnby1pUEhfZVNiYUI5Sk5abTVLcjJFWlJTbXM1T0NRYkpaMV9RVFNOeldLOGNDbXBqM3NHMGJxazNHMkpGdU5KSk5GX280ZjlUVVFmM0E5ZkE?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxQM3AyVmJoNy02Wnczek52endTSkZJaHVGNmszR2dtbTZLX3VxRG1SNVVmYTI4bDhqLTVweW1jdW8tYW85Nmgzc25qcmNCWEFmaUtBR3BaR05ZWnhNWEt3NXIyaFNOaEZxbVZNRHlRcWZ4QU40S3JpWmtCS19Obl9aSTNwSkNmR3IxQmtxSUVOQ0s5ZFBVR0FLR1NJYnNzUW9yU0RhOGtzeWJUTm9NbUcwcUFCNzEzQlVJZjF1SQ?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOVHVJZ1B0aUNQYW5WNjBHc0cwSlJvbzNGVEFQQ2MwZ2JyRjZCcWdyQ2lJbjJBM2xCdzVpNkdCRjRqc0VXWXBXZWpYblJRbjgwa2t3WVdVNzZVYVZubUFQZlBSUHM4QTM4OWFEbV9oSXVpWU5hR0pOMll2RFJaQXpLUkhmcFR4ZkJJelpFVnlad3pNd1QtY3AyVkdkak5qV3hUXzZsOTJOQVNfYXZONlZXc2pKbmxNcWhIWGc?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxQQ1E2VFNXck13cmZWMWJhVXRTeWxzV1FKWHpTUFJlcm9QblJKQ2FBdk04dHFNWXJHcEZDUHROUlU1enZ3OC1BNUZFRm5FTnhfMlFMM1ZuQzVzdzYzM3hUalgyRW1tZE5LU3pXaHZ1VUQ1c0ZNd2RUWWVKQ0dVU1BtNjBfNnkzM25kVU5rR0UwOWVyV19fLU05WngwNnV3a1g5WDIzOE1WdFl0MTA0YzlNMExVeUZHcGV1YzFaNk9OczhaSWFpTmc?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxQMnJtUndPUnpyWXp5MHlQSzF1Tm5reUZubHRqSk5GU3dOY2RQU3FqTUEyWmdOYjNMNjVYMC1neWdkOXRaWHpHZkRiUEJkcno3MDBWYVp2U0xKWXM2d0pMM2xPUnFkZXBzaVUyZHF3aklEWGdCLW9EcktqQU5tSHN0T3pKUThTNUZnakZ2TW11TzBMT0h5UHhFZ1Q2M2RVS2ZFRjdtTg?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQQ0RfWi1DdG9pbllGTWhYLXN1VzRla0RMOEx6TlhjZDdsb3h2WXpLaF9EVWhKZkJpSXlTeHgwTzkyWm56N3NkTlpUeVkwVTMtMUp1bHo0N2RBN0lmX1JlQ2xQN1BiZmFveEFRWmVjdEYwdXNYRkFqY3lLVEtvYUZOOVVndkh1UlcxVTBB?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNRFhzZ3ljMXpNQU54ZzVEN0kzWV9wVjVWUnZLSTdSa0xkS1FnVEFDdWd1QVZzc3RraEZ6VHVjcnVrODgyMmVmbDMzX2lSZlp0QkRiRThmN2V1OTBmR0xiZXZmcWFSajg2SHRaeVpLMTFtSU8wMUp3NmYyakg1VkIzYnNhOVdrM3p2MjNabmwxb2txcmNzWG01anVCR0gyOHV0VzVrMUFrQjhSQmV1eDB3YkpQWlVNSFFDeHhqSldjTjBJNTg5TWlHTF9BZXU?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxNbzBHZjM2QmdlRWpVeU1raGtqZmR5aktRczJNYkFsOUphYmprUVdLbW1vRlpGaHd3RXV1YWJnbjhwdlFXV0dreVJFN2poLWMxTGE0OWpHODBpaC1VelhTMVpMTzU4WHYxRFJUMGtDaUlxdnlPT2FJSk11c0FXeDYyUHdyQjFzVDZMNGU4ZDdlMGhGRnJfUzhQejU3c2VLM0d2R2VxMlgzYktrTU1IcHRqVzMtRlJGTURzSzdDcDlpckUyYnUybC1GS3Jn?oc=5
- https://news.google.com/rss/articles/CBMiekFVX3lxTE1COEZ0M0p2RHl5US1uaEtOckxaRlRXUXRMc1hlR01pNE4yV0NGTHJIb0Vma3FzZUtKX3RCbVg3ZmpUNHpnaHJZeTBjVFV0YmdFWDc0R2N5RFRObTY0bllEUU15N0J0aGFkUWdNdF9HOHg0WWtMSDJpdTl3?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxNaWZxTUVPSUtleUJrb2VoMnh2Z2NrTkxGRlRZMXdDcm53S2ROajhOcG9vZ3dkVnRUcVhBLUhzcWMyVXF1RUFhU01BM2lLQVVMSFRJWWZYTXRjenBCaHpTRE5ZcjMtOVNfdTloc1gtZ3hDaE1kTTIwWVRYSTJnaGwzemJGTXpBTlVNTXk1eVVQWVFOdDZBZjZ2QnNNWHI5UFJCUUMzRlpkcVhyM09xUEN5eHkxci1zR0dKbVNR?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxPWDhBeDRCZ21nOExrVzluVTk3dWpYQlE2VGgtSVUyRFdXSUI0VVJybVNQTms5V2czZjNtRE1QZ0xTM2NwUWwyUmNsSS10dm5CVE5PeGJ1QVl2djlXNFI2NVhKN0F6YVVfdEF1aE1lWUw2ZFEyT1B5VWM4WVF6VUVncDVfSGE0bzA2RjZrSjdwX3ZlSDhISVRQT2Vzc3pFZlVKVFNmRDNJaG5vcGxVTjhZX2h3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
