# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-11-15**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-11-15**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-16T04:44:51.081440+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 3, 'ai': 9, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261115T044154Z-6abfba73/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 14 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 27.27%; oldest publication 2026-11-11

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 534.0600 |
| Return 1D (%) | -8.7545 |
| Return 1W (%) | 18.9337 |
| Return 1M (%) | -11.8029 |
| Return YTD (%) | 149.3743 |
| Return 1Y (%) | 115.3815 |
| Annualized volatility (%) | 73.4201 |
| Beta vs SPY | 3.4490 |
| Max drawdown (%) | -37.7290 |
| Sharpe (rf=0) | 1.4162 |
| Downside deviation (rf=0, %) | 47.7508 |
| Sortino (rf=0) | 2.1775 |
| Historical VaR 95% (1D, %) | 6.7006 |
| Historical ES 95% (1D, %) | 9.6472 |
| Correlation vs SPY | 0.6404 |
| Tracking error vs SPY (%) | 65.5306 |
| P/E (trailing) | 114.12 |
| P/B | 12.81 |
| EV/EBITDA | 78.02 |
| Revenue growth (%) | 44.70 |
| Forward P/E (estimate) | 30.19 |
| Gross margin (%) | 56.00 |
| Operating margin (%) | 17.82 |
| Return on equity (%) | 11.96 |
| Free cash flow yield (%) | 0.84 |
| MA50 | 554.5522 |
| Close vs MA50 (%) | -3.6953 |
| MA200 | 423.1181 |
| Close vs MA200 (%) | 26.2201 |
| RSI (14, Wilder) | 50.3561 |
| MACD (12,26) | -8.3491 |
| MACD signal (9) | -15.8960 |
| MACD histogram | 7.5469 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 534.0600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -8.7545 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 18.9337 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -11.8029 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 149.3743 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 115.3815 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 73.4201 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 47.7508 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.1775 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.7006 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 9.6472 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6404 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 65.5306 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4490 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -37.7290 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.4162 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 30.1888 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 56.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.8210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.9600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.8399 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 114.1154 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 50.3561 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 7.5469 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.6953 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 26.2201 -> Clearly above the moving-average trend level.

## TAILWINDS

### AMD Soars 19% in a Week on Oppenheimer’s Upgrade and Nvidia’s Turmoil: “Demand Is Higher Than Supply”
- Summary: AMD Soars 19% in a Week on Oppenheimer’s Upgrade and Nvidia’s Turmoil: “Demand Is Higher Than Supply”
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPcmVMTGswUS0wN3NIX3JINlBfam5uWUhmZURPNC1Tbkl6dk5GRF92LW54dGNRWGlCQjVmWml6QnBhQkZYRkpOVGMzenZnMkIwMDEyQ3JRMF9RVWR5SXkyLUVmSEY3MlN1cHRfdnpwM2FBbkhXTkJpQ2h6OVVKUXllbm56NVNXcndqdTFqdklwdEZhUEdEd3Zyb0o3dW1wMFBBLXRUbE1adnR5Rk5XYmhSQlNVa0NYS3Vra255TkNHcw?oc=5>

### AMD Stock Looks Poised to Revisit Its All-Time Highs
- Summary: AMD Stock Looks Poised to Revisit Its All-Time Highs
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOeDl0eVNFcjZJei1OVm5qY2xST0t2MmFpMEVOQ2tnbkprelUyQ2ZudGJ5SENDSnlyaE5kaDRhX1V1aXhkOF9fTVRxS0lOWDBiNG1GdXJqT1BBdHVHcXVwYjlRdUFScW94dDE4V0ZOcHBQYTd3XzNBX293bmFnci11M0NZRzBsNkExQnViQ0Q4Nk5fREItRzF3V1J6cw?oc=5>

### Advanced Micro Devices Stock Climbs 45% On A 5-Day Winning Streak
- Summary: Advanced Micro Devices Stock Climbs 45% On A 5-Day Winning Streak
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNLVczQjEtckJ5SUxEX1dPYk1JUU9aSkFjUUNhM25Ed28zT2pGeURvcXJ2Q04wY2Q1Z05ENVBObGlOZFRZZ2cwbGduSUw2c2pjZEtkaEIxUmc1OWgwb1NkcEVXdXk3M3hGbGRjaXBtTWRQd3NabE9CRUEtQ2dLcmZxWEF5T3UzSjZjNWQ0UU1jZlNqeXQwVGhOQlVCMHhOdEw4Vmt2dE1GUFI2b0RMVDY2dDU3ZFhJT3JfNDc2dFprWENMQQ?oc=5>

### AMD: The AI Trade Just Entered Another Phase (NASDAQ:AMD)
- Summary: AMD’s AI market position is evolving, indicating new opportunities for growth.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxNa2VtWVFyQnFuVlFEeGpfN0NNUXlkYWNEZVRtM2dvMmpNX2FsREdkcGtoLVFIYThOeUJMbHN5WDVVMGIwR3pRZTJURzlUeTJnLVVLUEV4c2dwOV9BQl82WGEweGZZZnc1cHJ4Tkg2bVQzM09NMjZqNllLb0wtcGh5Q3BmNEt5TEk?oc=5>

### AMD and Broadcom Stock Get a Boost From Nvidia’s Loss
- Summary: Competitor loss lifts AMD and Broadcom stocks.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxOMGJPR1pTTlRRSUZBTFNIZTZCd1JYRHltdEx2N2F3OVpvRzRDbFZ2UWlhR01SLWZadTlKNnRjbi1sQU5RazZKaDdReWZmdHhqOEVuemFRTlQ3dWk5SUt2RnMtTU1CcTlDbGctMWZGLUhNREtPNXNnZXNNRUJwQkpMQTVB?oc=5>

### Why Advanced Micro Devices Stock Surged This Week
- Summary: AMD shares experienced a significant weekly rise, reflecting strong investor confidence.
- Date: 2026-11-14 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxONHhDVHZUbUdDaDg0ejlST2JLRkFNdFMtTnNuNmxjN2c1a00wcFpVbEp1VFpaRTlxZmpYMGdUam44cXFXQmN6aUtCakVqeGdta1BlTXhaMUFOVFRfVUh2U0ZYOFlxSFZYQmZHcUNEdzJvZnotdWtaS1RUZGpQR1RQazJfMzlXOWZUNFZIaGdJb2d4N0RTMVZtRmRqOGJSUQ?oc=5>

## HEADWINDS

### Stock Market Today, Nov. 13: AMD Sinks 8.75% on Sector AI-Chip Sell-Off After Early Gains Reverse
- Summary: AMD shares fell 8.75% amid a broader AI-chip sell-off, reversing earlier gains.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOcHVQMlQwdWpSNW5jTDVlNEttZmI0WUd4N0pDU1hZb1ctMF8tVGtLSUFMX2NoRXN6MlpTYnN6cnFvZjVwMEdYYWdLTjdWWTdEUTg0dktuZmpRcmxDU0cxOENFWGZVc1Z6M0xMQmdteXJBSF85VWFRYkJsYl9UVVB1cnJKeDJqb3JxQkNOTDFaX3QyOU01?oc=5>

### Why Advanced Micro Devices Stock Is Down Today
- Summary: AMD shares declined today, indicating a short-term negative market reaction.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPeExFb0d0c2NOZHdERDE3Z0JRXzhrR3VvenE3ZDNIWUJTZkpSd2RhVUU5SEJqTkhTRHZRZkdYLV9pUXlGbk5nQk5tbDJLQTQ2b2pHQWtrWE5NNkVraDdUQXhIeHR5WE9zX0RSeTc2MGdJM2NWYjI4SlJBbHFZYWlUWU9OWTUyXzhITE5Z?oc=5>

## CATALYSTS

### Harvard Cut Nvidia by a Third and Bought AMD
- Summary: Harvard sold Nvidia shares and purchased AMD shares.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNcmV1aE9qckN5S01UeTc3VHB6TmJLMGRKRUNGdU1UdG5QTVZLZng1bW1RSDNEd19jX0lyLW1wNnFNVHJRLXA1LUlzWDJOeE95dlhUdV9WMTRzYzltaTEzMGxZT2IzNWw0bzc0RzktM3hnMGJULXRIWmZubUJMOURXb0psTnJPMXNtS0R5MG1UbHhmQQ?oc=5>

### Why this $7-billion money manager is buying AMD, Alphabet and selling Canadian telecoms
- Summary: A large money manager purchased AMD shares, signaling bullish sentiment.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxPdHg0ZEw5ejF0SF81NFNpV3ByYnhCQVh4WE5faV9oYW5Ka1hFTnVRSG9iNllRRmF1OHNWcEdxTmVaT0ZnQlpERGktMGxSSUJQYWdIVE53UzRfVHhMeHcxamFxZTV2MHJyQlZKSzBtVm5HcUYxMXpBQ3Q2ZlNTNEd6SC1uT1pKTTBrTkZZVFREbWtqa0ZRQWNSdWVQR2pKdTNPX3lmUDYyT0VvN1ZZRC1neTJqWUw1YzZBV2RId01BS3pHWmJiU3lvS3JWVGtXdGFzNGhtZE1ncG1sWWJfMngxZw?oc=5>

### The Evidence Is Piling Up: AMD Could Be the Best Artificial Intelligence (AI) Stock to Buy Amid the Sell-Off
- Summary: Analyst opinion highlights AMD as a top AI stock amid market sell-off.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxOV212VERNUTlDS3VueEZDd19WaG12V3FseS0ydmZITFhmWi1kcEpsQVVOSE43cXYyWWJUbllDUzltNGZyTWk1VWRzS2JnVE13bkNRamFTQ0hWMkZNY3NITHl6VmlUMk10cWFsODJrWGtGMjNLSEpsN3VuMzNwNi1UMEg3TEEyRkRSWi1rcTJMaHZvNFU3ODRwMFZxVmhIMzQxeFJLeHZtcGFQaWxSakZBblY0eHY2SkE2TF9TT21zYURrbDNEOWRtV1dVV29qSTBsQUEyeU91WDhwYTg4c01hdHFn?oc=5>

## RISKS

### AMD and other chip stocks slide as Wall Street rethinks the AI trade without Jensen Huang
- Summary: AMD shares fell as AI trade sentiment weakened.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxPYVlEMXlPemQ5eVY1Y2F2Tmc1Ukx3bHBYSlZBQWVpamplYUNRcE5PdEd5a21IcGVRVlVIWW1jdDVfdTVVV0pTeENORTVvc3hpeGg1MTRrZDRTNnI3QktKbEJYZTdCOXQtRFBlb0wta2ZMc1otTElpV252bS1uQnFXX21zVEdsYlBhUUhzQnNpLWpTQTl2eWIyRGxsX0pURDJFaWZPY0dkeGs0ZTM4U2RpWU9uX2RmdGZtVUhnbnNidDBVWFJzRGt6QVhWREw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **114.12** | **12.81** | **78.02** | **44.70** | **875,905,024,000.00 USD** | **115.38** |
| NVDA | 20.59 | 17.17 | 19.38 | 105.90 | 3,932,339,044,352.00 USD | -12.64 |
| INTC | N/A | 2.76 | 17.24 | 20.90 | 317,092,888,576.00 USD | 66.14 |
| AVGO | 44.32 | 16.62 | 32.38 | 85.50 | 1,656,497,373,184.00 USD | 2.83 |

Peers fetched as_of: 2026-11-15; AMD reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

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
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,428,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMivwFBVV95cUxPcmVMTGswUS0wN3NIX3JINlBfam5uWUhmZURPNC1Tbkl6dk5GRF92LW54dGNRWGlCQjVmWml6QnBhQkZYRkpOVGMzenZnMkIwMDEyQ3JRMF9RVWR5SXkyLUVmSEY3MlN1cHRfdnpwM2FBbkhXTkJpQ2h6OVVKUXllbm56NVNXcndqdTFqdklwdEZhUEdEd3Zyb0o3dW1wMFBBLXRUbE1adnR5Rk5XYmhSQlNVa0NYS3Vra255TkNHcw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOeDl0eVNFcjZJei1OVm5qY2xST0t2MmFpMEVOQ2tnbkprelUyQ2ZudGJ5SENDSnlyaE5kaDRhX1V1aXhkOF9fTVRxS0lOWDBiNG1GdXJqT1BBdHVHcXVwYjlRdUFScW94dDE4V0ZOcHBQYTd3XzNBX293bmFnci11M0NZRzBsNkExQnViQ0Q4Nk5fREItRzF3V1J6cw?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNLVczQjEtckJ5SUxEX1dPYk1JUU9aSkFjUUNhM25Ed28zT2pGeURvcXJ2Q04wY2Q1Z05ENVBObGlOZFRZZ2cwbGduSUw2c2pjZEtkaEIxUmc1OWgwb1NkcEVXdXk3M3hGbGRjaXBtTWRQd3NabE9CRUEtQ2dLcmZxWEF5T3UzSjZjNWQ0UU1jZlNqeXQwVGhOQlVCMHhOdEw4Vmt2dE1GUFI2b0RMVDY2dDU3ZFhJT3JfNDc2dFprWENMQQ?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxNa2VtWVFyQnFuVlFEeGpfN0NNUXlkYWNEZVRtM2dvMmpNX2FsREdkcGtoLVFIYThOeUJMbHN5WDVVMGIwR3pRZTJURzlUeTJnLVVLUEV4c2dwOV9BQl82WGEweGZZZnc1cHJ4Tkg2bVQzM09NMjZqNllLb0wtcGh5Q3BmNEt5TEk?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxOMGJPR1pTTlRRSUZBTFNIZTZCd1JYRHltdEx2N2F3OVpvRzRDbFZ2UWlhR01SLWZadTlKNnRjbi1sQU5RazZKaDdReWZmdHhqOEVuemFRTlQ3dWk5SUt2RnMtTU1CcTlDbGctMWZGLUhNREtPNXNnZXNNRUJwQkpMQTVB?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxONHhDVHZUbUdDaDg0ejlST2JLRkFNdFMtTnNuNmxjN2c1a00wcFpVbEp1VFpaRTlxZmpYMGdUam44cXFXQmN6aUtCakVqeGdta1BlTXhaMUFOVFRfVUh2U0ZYOFlxSFZYQmZHcUNEdzJvZnotdWtaS1RUZGpQR1RQazJfMzlXOWZUNFZIaGdJb2d4N0RTMVZtRmRqOGJSUQ?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNY2ZFMjdSWTFDS3UtR1c0NWJneU1QdGZLZEFBRzY1SC05U2hyXzE3QlNMa193bk1USTFfMHRNVGY0LUxGT0ZPNHZ6RXFTMk1keGYzdnhSRTdvQ1hicDF6SXVmQzlhamJvczJfMk1VVGN2dWZsUjFSdGRoQmgyZ0l2R2Y2QkExbHByZGpmVWFyVkI1ZVFyVnNiUEt3R3lndHlYVkFzME9JNDE?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOcHVQMlQwdWpSNW5jTDVlNEttZmI0WUd4N0pDU1hZb1ctMF8tVGtLSUFMX2NoRXN6MlpTYnN6cnFvZjVwMEdYYWdLTjdWWTdEUTg0dktuZmpRcmxDU0cxOENFWGZVc1Z6M0xMQmdteXJBSF85VWFRYkJsYl9UVVB1cnJKeDJqb3JxQkNOTDFaX3QyOU01?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPeExFb0d0c2NOZHdERDE3Z0JRXzhrR3VvenE3ZDNIWUJTZkpSd2RhVUU5SEJqTkhTRHZRZkdYLV9pUXlGbk5nQk5tbDJLQTQ2b2pHQWtrWE5NNkVraDdUQXhIeHR5WE9zX0RSeTc2MGdJM2NWYjI4SlJBbHFZYWlUWU9OWTUyXzhITE5Z?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOVEFLanBoU3haWmJMX3Y5aVNYcVdjSnI2LTJPYlNFTUFoMGdxQnB0UFpKV2pmalBMd1ZNSS1kZTVBSzBWQXJhY2Y2TjJYbFcydE5LODRqX3BXRWJ3RmstN0YzTFZVS2Y0OWM3OVhwNWtJWWhLRkJmZHdTdFA4Tl8yVU90cEg0YUhMN19KUHlHa05oNWRRUmVTSzVjN1N3Zw?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNcmV1aE9qckN5S01UeTc3VHB6TmJLMGRKRUNGdU1UdG5QTVZLZng1bW1RSDNEd19jX0lyLW1wNnFNVHJRLXA1LUlzWDJOeE95dlhUdV9WMTRzYzltaTEzMGxZT2IzNWw0bzc0RzktM3hnMGJULXRIWmZubUJMOURXb0psTnJPMXNtS0R5MG1UbHhmQQ?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxPdHg0ZEw5ejF0SF81NFNpV3ByYnhCQVh4WE5faV9oYW5Ka1hFTnVRSG9iNllRRmF1OHNWcEdxTmVaT0ZnQlpERGktMGxSSUJQYWdIVE53UzRfVHhMeHcxamFxZTV2MHJyQlZKSzBtVm5HcUYxMXpBQ3Q2ZlNTNEd6SC1uT1pKTTBrTkZZVFREbWtqa0ZRQWNSdWVQR2pKdTNPX3lmUDYyT0VvN1ZZRC1neTJqWUw1YzZBV2RId01BS3pHWmJiU3lvS3JWVGtXdGFzNGhtZE1ncG1sWWJfMngxZw?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxOV212VERNUTlDS3VueEZDd19WaG12V3FseS0ydmZITFhmWi1kcEpsQVVOSE43cXYyWWJUbllDUzltNGZyTWk1VWRzS2JnVE13bkNRamFTQ0hWMkZNY3NITHl6VmlUMk10cWFsODJrWGtGMjNLSEpsN3VuMzNwNi1UMEg3TEEyRkRSWi1rcTJMaHZvNFU3ODRwMFZxVmhIMzQxeFJLeHZtcGFQaWxSakZBblY0eHY2SkE2TF9TT21zYURrbDNEOWRtV1dVV29qSTBsQUEyeU91WDhwYTg4c01hdHFn?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxPYVlEMXlPemQ5eVY1Y2F2Tmc1Ukx3bHBYSlZBQWVpamplYUNRcE5PdEd5a21IcGVRVlVIWW1jdDVfdTVVV0pTeENORTVvc3hpeGg1MTRrZDRTNnI3QktKbEJYZTdCOXQtRFBlb0wta2ZMc1otTElpV252bS1uQnFXX21zVEdsYlBhUUhzQnNpLWpTQTl2eWIyRGxsX0pURDJFaWZPY0dkeGs0ZTM4U2RpWU9uX2RmdGZtVUhnbnNidDBVWFJzRGt6QVhWREw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
