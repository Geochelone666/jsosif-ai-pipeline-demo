# AMZN Intelligence Report

- ticker: **AMZN**
- Report as_of: **2026-10-26**
- Market data as_of: **2026-10-26**
- Quant sources: https://finance.yahoo.com/quote/AMZN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMZN/key-statistics/
- AI analysis snapshot as_of: **2026-10-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-27T02:15:21.125819+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 2, 'ai': 12, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261026T005504Z-6368ad31/AMZN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 8 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-10-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 249.0900 |
| Return 1D (%) | 0.4395 |
| Return 1W (%) | -5.0905 |
| Return 1M (%) | -0.2323 |
| Return YTD (%) | 7.9153 |
| Return 1Y (%) | 11.0967 |
| Annualized volatility (%) | 34.7966 |
| Beta vs SPY | 1.4732 |
| Max drawdown (%) | -21.7362 |
| Sharpe (rf=0) | 0.4390 |
| Downside deviation (rf=0, %) | 20.9984 |
| Sortino (rf=0) | 0.7274 |
| Historical VaR 95% (1D, %) | 2.9695 |
| Historical ES 95% (1D, %) | 3.9961 |
| Correlation vs SPY | 0.5384 |
| Tracking error vs SPY (%) | 29.9343 |
| P/E (trailing) | 20.04 |
| P/B | 4.87 |
| EV/EBITDA | 16.67 |
| Revenue growth (%) | 19.60 |
| Forward P/E (estimate) | 23.88 |
| Gross margin (%) | 50.77 |
| Operating margin (%) | 13.69 |
| Return on equity (%) | 30.56 |
| Free cash flow yield (%) | 0.12 |
| MA50 | 255.3764 |
| Close vs MA50 (%) | -2.4616 |
| MA200 | 243.3069 |
| Close vs MA200 (%) | 2.3769 |
| RSI (14, Wilder) | 44.3486 |
| MACD (12,26) | -0.3134 |
| MACD signal (9) | 0.4300 |
| MACD histogram | -0.7434 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMZN': 268, 'SPY': 268}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 249.0900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.4395 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -5.0905 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -0.2323 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 7.9153 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 11.0967 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.7966 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.9984 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.7274 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9695 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9961 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5384 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.9343 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.4732 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -21.7362 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4390 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.8753 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.7700 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 13.6890 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 30.5580 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.1198 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.0394 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 44.3486 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.7434 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -2.4616 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 2.3769 -> Slightly above the moving-average trend level.

## TAILWINDS

### Amazon Shares Rise 1.1% Premarket After Anthr
- Summary: Amazon Shares Rise 1.1% Premarket After Anthr
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNX2ZXMDNIanhBZG4yZEotczlQRERaRFBNR0RBT2lDNHZjRGNFV2IxNU9vWENDaUI0X2drZUVyeXJiWDR4TG92em96LXlGVkZScXVLRnZHSEpRQXJVakQ4NG5jYWlkcm5Rd3VzNkRQSzhhQ1E1MXFLcFFERTZfYllWdXlGSFFJTHE3WFVJNUdWM3hJV2hzR2NISHJfeEdyVU5fN1poSWtR?oc=5>

### Why Amazon (AMZN) Stock Is Up Today
- Summary: Amazon stock rises today.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQU3pTZEJjVGVLLUg3WmZTV2xmN1R6Zm9wWTB2bXdYOGNtNXNKVTdqTHNFTDMyLVNjZERUa1U5blotTG5hVEtseGZCRkcxazlkdVpsOVh6c1YxSzBSMGNQT3lBclB4VUgyajN4SUpDODNEQTBUWGgwNUVrclhWVjhyc3prZHY1TjhObjdsakZLaXRxcTAyRXJ3?oc=5>

### Amazon (AMZN) Suffers a Larger Drop Than the General Market: Key Insights
- Summary: Amazon stock drops more than market.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQNFU0TGNVU1Iwa3hrYXNvYmMxVW5mejhzMENQclJpUVRseWpGSVYyM2tfUUFrWktKTE9qdTI1RmdRbVh6VUJLQ3dlQjVVNVVXMkJWUFJWZFB2OHJtamFrZzlKN21VX2xNTjlnd2RtMEFYUC13elVKMjhXSy1HUmowSHFEN0w0MFlPU0ZpbEFhRlZsT1h1SXZRajhmazI?oc=5>

### Amazon’s Bee AI Wearables Could Be a New Growth Driver for AMZN Stock
- Summary: New Bee AI wearables may boost Amazon.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNNEFZWklmV1BYT19HSERSSDZSTXF2ZXlrS0VHMU4ta3ZmdzdJZDBvNVBDb3o5Yk5mMGlmQk53SXBqR1d2YTFheHVVUHVJdUNLazd5Q19RZl9pQWhMTlRialo4MG9fNEhIS2wtdmY5WEgtbnYwZGk2RERsZ1VNYThiMHlyaXBGR0trekhMWDJPWnotMFMzNXJZYw?oc=5>

### UBS Sets Bold Amazon Stock Target Ahead of Earnings
- Summary: UBS projects a significant upside for Amazon stock before earnings release.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPTWN3cXhlTi1oTDJXY3BIbGZUYl9DV1YzNWZPVmYzZHhZczNlMm1YdnY2bElNNEEtQ2ZtTGFzYi0yOGZpbEVpaU93cEJoaFhrTzdOZ01TQWNVMm54QUM1T0VsZ2h4aXNGeVBWeWNsS1p1U2hRTktmVXdKVGJVWlFKc3pJTXV5dWxLb3FZN09xTE5KdEUtdnc?oc=5>

### Ahead of Earnings, Is Amazon Stock a Buy, a Sell, or Fairly Valued?
- Summary: Analyst debate suggests potential upside for Amazon stock ahead of earnings.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOU3ZWanZTdVJOZjZiV21CWVQzeTZYSTZiQkVQS192N2xLNm0tUVFMWmJOeWxQVEctMUpPRmZZTm1NZ1JzUTlEMWNYT1V0S3dwNW9KWUlwQXVVM0VrZ3UyejlDSUgxeGxrcXdtakRWY3ZZZ2JwaUMtUlBoSEt4elV6ZEZWSFhJSEp5dm9yZ1NkWkxDQXNXTWFOQ0dXX3hwbndIY1Fvag?oc=5>

### Amazon Into Earnings: The Parts Add Up To $290, And Anthropic's IPO Could Add More
- Summary: Projected earnings of $290 per share with potential boost from Anthropic IPO.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxPaXFWeXBVMnhscGpOLXo3Z1dsM203TmVJdDVzcHkwRjdvSmszWjF4MGdLaGJIdDRUeENIbDZ1YTRhbWJKSFBEOHN0N0dLUU50d3lveG1Zd1VLZDcyZkJBNEpzdUNMcVotWUpTR1ZSR2std1hpNWhfQWhvZzJPalBNQ0l0WWVNa0oxRU5qVzltdGhnZUdKWHRBdDhtQ2xRUDdYSzZuVXpKN0hTLTM5cU9XSWlTeHU2TXV1dXcw?oc=5>

### Morgan Stanley Sees Amazon Stock Surging 100% with AWS Hitting $1 Trillion in Revenue Sooner Than People Think
- Summary: Morgan Stanley forecasts 100% stock surge driven by AWS revenue milestone.
- Date: 2026-10-25 | Impact: high | Horizon: short | Confidence: 0.88
- Sources: <https://news.google.com/rss/articles/CBMi5wFBVV95cUxNRTlMTHZLbXU2X3RFdmhmRlg0RFBMNXNodVhKODRZQ2stU1k4eEd2Q1lHV1Itdm8zajZOOGxpNEpTTnVqUGdQMHlqSzBreUk5M3Jpei1Ma0treWYzVnRPS0drUnk2cXJYa3dlNG9ROXVYbF8ybDJtMTNFMzZ0MC1HRVZCaTd3RDZxMUlfeGRvemJDSXotemd0VUp3QzR0cWV5VGcxcXRXeGdOSzYzVkNwTGk3WUFpbmNCclVYX2p2dDZ1RC10eVRMNUxqb1dGYjcyZ29UM2twOXdYSFQ3R1c3a0JiSG9GbWM?oc=5>

### The Hidden $496 Billion Catalyst Waiting to Ignite Amazon Stock on Oct. 29
- Summary: Speculation of a $496B catalyst could boost Amazon stock on earnings day.
- Date: 2026-10-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxPRk5GeFJXSXF1aDliN0R3Rk80S0dNQm5sM3RDUW1mZ0c1NFVWVGlWMUpOSGpPSTBxS1B2cWlfNXlxX2ppZ1V1ajJHZlQ3OWtVcU90R2R0ZkFfaElIRU1VYkg4dk5ZbF9GNEpHMENQbm53c01iaE4zMkJ5eVpoX3FOV1BXakVKVkhKMG03R1lDUWtaT082NG1vZDhNckh5R3NrbUxOSFlBTS1iSUNSUmVIZGRTQjczTEU?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Amazon Q3 Preview: CAPEX Spending In Focus, Shares Fairly Valued (NASDAQ:AMZN)
- Summary: Amazon Q3 Preview: CAPEX Spending In Focus, Shares Fairly Valued (NASDAQ:AMZN)
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQRVlYdWNNeGtGS3BWTnJhQU41SHpwbXlaWjd3U3NsQ0VmamJSUmxSUkpZTk83aU92aUhuNkVYaThmTmZURHZNSjloUS05aDB3ZG5rMlNUREFVczdRUkNKaGN5aE5aZ3Q0SjhsZ2U3VzQ2M3dGTXhBNkdWWE1WSmF5NkZVT1BBOTh3dUVOeXZTS3Z1TkNSRXVMbDFaVl9MTVlKaG5UUzR3?oc=5>

### UBS Sees 40% Upside For AMZN Stock — AWS Margins Take Center Stage Ahead Of Earnings
- Summary: UBS forecasts a 40% upside for Amazon stock, highlighting AWS margin improvements ahead of earnings.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNRlMyWWZmRU9HNFFxam9fOXp4WjlRcl9LNUtjTjAtWmIwOHhyZ2NWSnZOWUxzYXVJX0NNMUxtNkhLbUs2ZDZUMkdjcHI5TU5RVXppYVg3SmZQc3ViOXQyeE5JUkFsMldWNGctOC1jQ08yd2pCelJEMWJZTmZscF9adk9SZjRFdW96UHRnRWdhdVlFQQ?oc=5>

### Gear Up for Amazon (AMZN) Q3 Earnings: Wall Street Estimates for Key Metrics
- Summary: Wall Street estimates key metrics for Amazon's Q3 earnings, setting expectations for the upcoming report.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQdGZpTVBwWkxLQzF0RUNxb2U0OHNURGlWSzZNMjVJb0hIeVBocTJZek9JUG5tRDRnVVc4TGRXaGE4bzByUFJoRVRRTWhVemVRbm5pRmVEZ3ltcDZqMVNpRmVHZG1Bck8zdUNHNE9ob1BWN0xwaUVNODJBWFdtU2R5YVlxVWRYT0QybDNkRHNzT1NEN3pCT3R3dg?oc=5>

### Microsoft, Alphabet, Amazon Earnings Meet Fed Rate Decision: 3 Charts To Watch This Week
- Summary: Amazon's earnings release coincides with the Fed rate decision, impacting market charts and investor sentiment.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxNNkdIbG5Fc1RXeW9YMXN0VC1hbjhSd25JSU9OWnBRR2c3SXFzU3otVEVzLU1HQWtrbzVGYmJPekxfUlc1WDFCNm9wTVIxY29sY0J5eVBueFB2T1lkX2xITmVHb0tpZ2pnTmZETkRCZVlhd014X0FzTC1CSkZVNGFPSHlGS2VEMVh6TjBEM2NHcVhjTE1mLTZLWWJWcHdJbnhCcUdqbnJ0UXFHb2doNjNxS18yRkczbm5JbG95M2R2dkJOVUJBbDZBTlpqZmx3UG5pNjN1YTFRdWZCTDlyTHpF?oc=5>

## RISKS

### Amazon Just Walked Away From a $427 Million Data Center Plan After Neighbors Fought Back
- Summary: Amazon canceled a $427M data center due to local opposition, impacting expansion plans.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxOamw0clpNLVEyY0hST1QyUlNJZlRRN3FLelU2bEJ1THJ6YkZmR1h0N3hmQjlsYWVJLWZvanBJaWRLd0w3dzRxWnBVQVVBTnNXdmZUa09FX1RhOS1VOGU2akVWSDc0aTZRZ1MtTDRmRXlxcXFYNW5odEY0djV2a3JKd0dBMVE2YUl6WEdOTVpOaVlYUmFvQThONk8xejg5V0drZ0lPNGhESE5XTEF2blhLRldYbTBvYUFiNXFZeGhGWGRTQ3FUcE9tZEVkMA?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMZN** | **20.04** | **4.87** | **16.67** | **19.60** | **2,686,762,614,784.00 USD** | **11.10** |
| WMT | 43.58 | 9.73 | 23.25 | 5.90 | 957,277,339,648.00 USD | 14.25 |
| MSFT | 29.67 | 8.94 | 20.63 | 17.70 | 3,954,845,417,472.00 USD | 2.55 |
| GOOGL | 15.90 | 6.22 | 21.78 | 24.20 | 3,874,443,231,232.00 USD | 22.20 |

Peers fetched as_of: 2026-10-26; AMZN reuses existing data (market data as_of: 2026-10-26); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-30
- Next expected earnings: 2026-10-29 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-07-31
- Revenue (latest available single quarter): 200,606,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 62,647,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMipgFBVV95cUxNX2ZXMDNIanhBZG4yZEotczlQRERaRFBNR0RBT2lDNHZjRGNFV2IxNU9vWENDaUI0X2drZUVyeXJiWDR4TG92em96LXlGVkZScXVLRnZHSEpRQXJVakQ4NG5jYWlkcm5Rd3VzNkRQSzhhQ1E1MXFLcFFERTZfYllWdXlGSFFJTHE3WFVJNUdWM3hJV2hzR2NISHJfeEdyVU5fN1poSWtR?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQU3pTZEJjVGVLLUg3WmZTV2xmN1R6Zm9wWTB2bXdYOGNtNXNKVTdqTHNFTDMyLVNjZERUa1U5blotTG5hVEtseGZCRkcxazlkdVpsOVh6c1YxSzBSMGNQT3lBclB4VUgyajN4SUpDODNEQTBUWGgwNUVrclhWVjhyc3prZHY1TjhObjdsakZLaXRxcTAyRXJ3?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQNFU0TGNVU1Iwa3hrYXNvYmMxVW5mejhzMENQclJpUVRseWpGSVYyM2tfUUFrWktKTE9qdTI1RmdRbVh6VUJLQ3dlQjVVNVVXMkJWUFJWZFB2OHJtamFrZzlKN21VX2xNTjlnd2RtMEFYUC13elVKMjhXSy1HUmowSHFEN0w0MFlPU0ZpbEFhRlZsT1h1SXZRajhmazI?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNNEFZWklmV1BYT19HSERSSDZSTXF2ZXlrS0VHMU4ta3ZmdzdJZDBvNVBDb3o5Yk5mMGlmQk53SXBqR1d2YTFheHVVUHVJdUNLazd5Q19RZl9pQWhMTlRialo4MG9fNEhIS2wtdmY5WEgtbnYwZGk2RERsZ1VNYThiMHlyaXBGR0trekhMWDJPWnotMFMzNXJZYw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPTWN3cXhlTi1oTDJXY3BIbGZUYl9DV1YzNWZPVmYzZHhZczNlMm1YdnY2bElNNEEtQ2ZtTGFzYi0yOGZpbEVpaU93cEJoaFhrTzdOZ01TQWNVMm54QUM1T0VsZ2h4aXNGeVBWeWNsS1p1U2hRTktmVXdKVGJVWlFKc3pJTXV5dWxLb3FZN09xTE5KdEUtdnc?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOU3ZWanZTdVJOZjZiV21CWVQzeTZYSTZiQkVQS192N2xLNm0tUVFMWmJOeWxQVEctMUpPRmZZTm1NZ1JzUTlEMWNYT1V0S3dwNW9KWUlwQXVVM0VrZ3UyejlDSUgxeGxrcXdtakRWY3ZZZ2JwaUMtUlBoSEt4elV6ZEZWSFhJSEp5dm9yZ1NkWkxDQXNXTWFOQ0dXX3hwbndIY1Fvag?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxPaXFWeXBVMnhscGpOLXo3Z1dsM203TmVJdDVzcHkwRjdvSmszWjF4MGdLaGJIdDRUeENIbDZ1YTRhbWJKSFBEOHN0N0dLUU50d3lveG1Zd1VLZDcyZkJBNEpzdUNMcVotWUpTR1ZSR2std1hpNWhfQWhvZzJPalBNQ0l0WWVNa0oxRU5qVzltdGhnZUdKWHRBdDhtQ2xRUDdYSzZuVXpKN0hTLTM5cU9XSWlTeHU2TXV1dXcw?oc=5
- https://news.google.com/rss/articles/CBMi5wFBVV95cUxNRTlMTHZLbXU2X3RFdmhmRlg0RFBMNXNodVhKODRZQ2stU1k4eEd2Q1lHV1Itdm8zajZOOGxpNEpTTnVqUGdQMHlqSzBreUk5M3Jpei1Ma0treWYzVnRPS0drUnk2cXJYa3dlNG9ROXVYbF8ybDJtMTNFMzZ0MC1HRVZCaTd3RDZxMUlfeGRvemJDSXotemd0VUp3QzR0cWV5VGcxcXRXeGdOSzYzVkNwTGk3WUFpbmNCclVYX2p2dDZ1RC10eVRMNUxqb1dGYjcyZ29UM2twOXdYSFQ3R1c3a0JiSG9GbWM?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxPRk5GeFJXSXF1aDliN0R3Rk80S0dNQm5sM3RDUW1mZ0c1NFVWVGlWMUpOSGpPSTBxS1B2cWlfNXlxX2ppZ1V1ajJHZlQ3OWtVcU90R2R0ZkFfaElIRU1VYkg4dk5ZbF9GNEpHMENQbm53c01iaE4zMkJ5eVpoX3FOV1BXakVKVkhKMG03R1lDUWtaT082NG1vZDhNckh5R3NrbUxOSFlBTS1iSUNSUmVIZGRTQjczTEU?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQU2VwS1p3Q1ptTlRKY0ZXeUVvOGF6QUxQY0wxN1UxeXFRVFFlQnBrT3FIdWdDcW10SlhPQlFnUW5iaUlIZnM1TU0zVkl0aXpwc1AzMVlxS0tnaDBaSFhaYm91dDdzdkhTOS13MTQzOUlJbDYzekdOYnFaZEhWdDJ1WmwxNDZCSUFUUnlCMS1Ja3cwVEF4b1p5S0N4eXMzWUdpM3c?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQRVlYdWNNeGtGS3BWTnJhQU41SHpwbXlaWjd3U3NsQ0VmamJSUmxSUkpZTk83aU92aUhuNkVYaThmTmZURHZNSjloUS05aDB3ZG5rMlNUREFVczdRUkNKaGN5aE5aZ3Q0SjhsZ2U3VzQ2M3dGTXhBNkdWWE1WSmF5NkZVT1BBOTh3dUVOeXZTS3Z1TkNSRXVMbDFaVl9MTVlKaG5UUzR3?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNRlMyWWZmRU9HNFFxam9fOXp4WjlRcl9LNUtjTjAtWmIwOHhyZ2NWSnZOWUxzYXVJX0NNMUxtNkhLbUs2ZDZUMkdjcHI5TU5RVXppYVg3SmZQc3ViOXQyeE5JUkFsMldWNGctOC1jQ08yd2pCelJEMWJZTmZscF9adk9SZjRFdW96UHRnRWdhdVlFQQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQdGZpTVBwWkxLQzF0RUNxb2U0OHNURGlWSzZNMjVJb0hIeVBocTJZek9JUG5tRDRnVVc4TGRXaGE4bzByUFJoRVRRTWhVemVRbm5pRmVEZ3ltcDZqMVNpRmVHZG1Bck8zdUNHNE9ob1BWN0xwaUVNODJBWFdtU2R5YVlxVWRYT0QybDNkRHNzT1NEN3pCT3R3dg?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxNNkdIbG5Fc1RXeW9YMXN0VC1hbjhSd25JSU9OWnBRR2c3SXFzU3otVEVzLU1HQWtrbzVGYmJPekxfUlc1WDFCNm9wTVIxY29sY0J5eVBueFB2T1lkX2xITmVHb0tpZ2pnTmZETkRCZVlhd014X0FzTC1CSkZVNGFPSHlGS2VEMVh6TjBEM2NHcVhjTE1mLTZLWWJWcHdJbnhCcUdqbnJ0UXFHb2doNjNxS18yRkczbm5JbG95M2R2dkJOVUJBbDZBTlpqZmx3UG5pNjN1YTFRdWZCTDlyTHpF?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxOamw0clpNLVEyY0hST1QyUlNJZlRRN3FLelU2bEJ1THJ6YkZmR1h0N3hmQjlsYWVJLWZvanBJaWRLd0w3dzRxWnBVQVVBTnNXdmZUa09FX1RhOS1VOGU2akVWSDc0aTZRZ1MtTDRmRXlxcXFYNW5odEY0djV2a3JKd0dBMVE2YUl6WEdOTVpOaVlYUmFvQThONk8xejg5V0drZ0lPNGhESE5XTEF2blhLRldYbTBvYUFiNXFZeGhGWGRTQ3FUcE9tZEVkMA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
