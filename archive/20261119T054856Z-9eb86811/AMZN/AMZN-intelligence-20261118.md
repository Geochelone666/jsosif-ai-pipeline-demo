# AMZN Intelligence Report

- ticker: **AMZN**
- Report as_of: **2026-11-18**
- Market data as_of: **2026-11-18**
- Quant sources: https://finance.yahoo.com/quote/AMZN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMZN/key-statistics/
- AI analysis snapshot as_of: **2026-11-18**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-19T05:54:28.710287+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 4, 'ai': 11, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261118T054934Z-e0d070d9/AMZN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 11 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 34.78%; oldest publication 2026-11-12

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 267.7400 |
| Return 1D (%) | 3.8194 |
| Return 1W (%) | 0.5898 |
| Return 1M (%) | 7.0960 |
| Return YTD (%) | 15.9951 |
| Return 1Y (%) | 20.3055 |
| Annualized volatility (%) | 33.9289 |
| Beta vs SPY | 1.2998 |
| Max drawdown (%) | -19.6419 |
| Sharpe (rf=0) | 0.7129 |
| Downside deviation (rf=0, %) | 20.5753 |
| Sortino (rf=0) | 1.1756 |
| Historical VaR 95% (1D, %) | 2.8374 |
| Historical ES 95% (1D, %) | 3.9903 |
| Correlation vs SPY | 0.5270 |
| Tracking error vs SPY (%) | 29.1278 |
| P/E (trailing) | 21.64 |
| P/B | 4.72 |
| EV/EBITDA | 16.80 |
| Revenue growth (%) | 12.10 |
| Forward P/E (estimate) | 24.50 |
| Gross margin (%) | 51.37 |
| Operating margin (%) | 13.09 |
| Return on equity (%) | 27.42 |
| Free cash flow yield (%) | -1.20 |
| MA50 | 255.1216 |
| Close vs MA50 (%) | 4.9460 |
| MA200 | 244.9080 |
| Close vs MA200 (%) | 9.3227 |
| RSI (14, Wilder) | 57.1873 |
| MACD (12,26) | 2.8114 |
| MACD signal (9) | 2.2457 |
| MACD histogram | 0.5657 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMZN': 285, 'SPY': 285}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 267.7400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 3.8194 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.5898 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.0960 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 15.9951 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 20.3055 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.9289 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.5753 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.1756 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8374 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9903 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5270 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.1278 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.2998 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.6419 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7129 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.5047 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 51.3740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 13.0870 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.4160 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -1.1997 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.6443 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 57.1873 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.5657 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 4.9460 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.3227 -> Clearly above the moving-average trend level.

## TAILWINDS

### Amazon Stock Moves Higher: What's Going On?
- Summary: Amazon Stock Moves Higher: What's Going On?
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOMlZzcndHVHcxM3A0VFVKY2NVZUhMejNRLXJJVjZBV1RiR3o1cXk3c28xcnRNbjAtTl8wUmtsUVFxc1RUZGxtNzVza3Y5cmNoZTF5dExRNUNuWnRSV0RFU1BFaFVxeHd2VHljbW5iUTVQMFR2QmR6VDN0Q1VLazNjZXRwVU81b0M2MHVXY3AydVpXb1FXQTBiMnpQLXBrR1MxQTVXZUJn?oc=5>

### Amazon.com (NASDAQ:AMZN) Stock Jumps 3.8% - Here's Why
- Summary: Amazon.com (NASDAQ:AMZN) Stock Jumps 3.8% - Here's Why
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxNY3FYSHN1WVd5R2I5T0lTUXhrMmhMRVhwZ0FiTEZGTHRmaF92aHF2LUFpLVpWSXpUM2ZKYXdmbWRZUkp1MkV4aDluQzZSNncxTURrcmF2bU8xTWRFNzE2NU15WU1jVkRFY2NWeDFDekVQRjBHdi1tODg4SUtwR1pkajcwVmNjYmVEUFVteUVqOEk5elBpUkt4TjBVVEdFc0dTVm9qQ1lHN0MtQQ?oc=5>

### Amazon (AMZN) Is Building Its Own Answer to NVIDIA. Here’s How It’s Going
- Summary: Amazon is developing its own AI hardware to compete with NVIDIA, signaling innovation and potential market expansion.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPWTZXSmptWXNhdDBlVUZFN2xDRE4xdzI2TDJ2b1NrN0paY0dyY2dUNFBKUUJHdi1zbnVyX0lGYm1teVI4ZEJXZU1sa1IwVjBnbTRld3JZd1FVVE9CYVIzOE9UNDI0Z0Vrb2doRFd4UGdkMUpJMGhjY3NWU1FzUW5IZzBVODBpdHU0NjltYmpPM18tekNTNGVJQ3FWcw?oc=5>

### Amazon makes major investments in renewable energy projects in India (AMZN:NASDAQ)
- Summary: Amazon is investing heavily in renewable energy projects in India, supporting sustainability and reducing operational costs.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPTkpLSzFzQVZ5V0xHYmhnVE5HSU1fMEZ5SVZjc2ZTLThtWHFfMDI3dWNiNkl5emt2TnhoUVRZd0dzM0ROS2VpWmxpcGw2SC1HQm5CVVNqUUhZRlFjLTFGb0FTN2VKUTMyODd5X3hfVzBjWmxieTB6NjE3c1QwMWVmYU05WnNzR0g3eEctY3RUMENMdERlYVdMUzZERm5wRzVjaDlvMTRxSGljQQ?oc=5>

### Amazon Cranks Up Its India Clean Energy Investment With Fresh $7 Billion Bet
- Summary: Amazon is increasing its clean energy investment in India with a new $7 billion commitment.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxOYTVRLVBIMzJZaVFPWVh6SlFDUXFwcUM3Z0JZVEYyM2ozbWdnUlBpNThUVkI2RnRoQWktUTg1c0tQcUdaM2tBcTR2Vk5rVm1DS1lPRkE5OUJwR0IwMWUwOHBlcng0dUxMcXpNdmF5OGlWRWhBaWpPRDVkbmZIa0ZSdjBIMnpKczZWZlFLUWx4OFY0bTF5YnBxeDZ4WHZHM0h0RXRDU1JIblZmbE5lMG93c0RGOVlmek1vNkFVMWNyY2pFWlNqT1pSWUY0THZsZw?oc=5>

## HEADWINDS

### Amazon Stock (AMZN) Dips Despite a $7B Sustainability Investment in India
- Summary: Amazon shares fell despite a $7B sustainability investment in India.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNMC1xVGJpZTVvS3d0bDg4WkVDQW50ZHB5UmY4TEhGc0t4aFViZzB2Z1g1blNINzU5Tkd2bW5fZlhQRm1SMjBVUG9DTEVTRS1nZkdJRmQ2NUQ0TElYcVR6OUtSM196ZmUwRnhobGZsNnlYTF8weGF6WTVHQm9CVUZfTnlRdHhaa3RwTjV3VTlwMFJTRFlmMmRQcklkS09NM29Pb1E?oc=5>

## CATALYSTS

### Amazon Has Quietly Recouped Its Post Q3 Earnings Losses. AMZN Stock Could Hit $300 Next.
- Summary: Amazon Has Quietly Recouped Its Post Q3 Earnings Losses. AMZN Stock Could Hit $300 Next.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNUGk3cGhNR3c1UEE1dHgwakYwRW1fYmV4NXcxbXdqcWhxV1dtQ2JmbUdFRkFjYm4yU3R5Y0NnaDlPbFhmNXc1WEpxRlplVXYwWkxHQVZLUDhSOTQ5WFZNeXlzdEpSLVVnUF9ycmV6SnVYUXRuWm56c1BXWW1pZWp0RkdGVFRseUhGRDlxME0wSEJjZlRNNkVjLTZ6eEg?oc=5>

### Amazon's AWS Strikes $5B Data Center Deal With Blackstone Digital — A Look At Some Key Highlights
- Summary: Amazon's AWS Strikes $5B Data Center Deal With Blackstone Digital — A Look At Some Key Highlights
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPcFRWN0I0NVFPbC03RXNNTzdjLTg0RkFSM2dSVDNQOWJUSnA5NVl6SFRmLTRCMEVJVm5HeUFrZkxzb1JkZ21MT1dsb2V6b2RFYzZJR0drS0VpcFdBV1ZBZTBJcEtvT0E3MVZNSDYydWNTUEVRb2M4THo2bFlpdEF5eXU5UGJjSTJCVEFpWkROcjRkNFE?oc=5>

### Anthropic’s New IPO Filing Shows Amazon, Google Will Own Over A Quarter Of The Claude Maker
- Summary: Amazon will own over 25% of Anthropic after its IPO filing, indicating a significant partnership and potential AI collaboration.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNWnBIQWE0a2JUME11UzNpeTZUa0lqOEg0aFNMT05BV29YVldtdzNISHM1OWtrdHZsYkRHc2xTZmFjekh4dTltVEpROVRsZlFjcW8xR21QZ2t2aXpNcHNpb2QyU0lkdU5aZXV6bFVkdXNES09NRnh2MHJTeER1R2hud3o1UWdkSmR5ZnZoQmpRQjhvQk5nTlZtVnBMS1FGUDA?oc=5>

### What Could Lift Amazon Stock From Here?
- Summary: Speculative piece on factors that could boost Amazon's stock performance.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPdnhpdEhzanE4RkFZb3FsR1hjYl93aktwY3hjV0NCQ1EtQzBBbDRMSzgzYjZoVEdKS2c1ZWU0RTRoMVd5Si1pSlR5R0VaOXQwRVByX1YzdUhLV1djN2ZoSmF1OTAycm5kanF1Y014ZXBSbVp0Q3Nqd0RmWjdJaEFtM3ptUDZsT25temNOTEY3YncxMU1SOHpzSU5fU0JNbjRT?oc=5>

### Amazon and Alphabet Will Own Over 28% of Anthropic After Its IPO. Here’s What That Means for Their Stocks.
- Summary: Amazon and Alphabet to hold 28% of Anthropic post-IPO.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQaV9WVUdzMk5hM0tDU1FaeFB0dkpRenRRaUFFWWdFaVZCVUdpT3hVc3cxeWZfeTlQNjVBVHJjRzdxS1dsclRZeHBIblVhQWkzMEliOU5vUzVFODgtQUI3VHJjVnVVZGd4V1lnNUVvWVdBc0hzUW5wX1JlZ2FMV0hVOXViZEFfTE1WcDFpVE1ySXRrZkVGRk5F?oc=5>

### AMZN Stock Rebounds Despite UBS Downgrade, as Amazon Anthropic Investment Could Be Worth $150 Billion
- Summary: Amazon stock rebounds after UBS downgrade, driven by potential $150B Anthropic investment.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxNTmhQcEsxU3pxQ0llWWdvenNGWTdTY29QOExSU1c0VDFQOGhpajdJeFo5d0tlUzc4RmdjYzh3aV9uc0xhYXQxejRRVDI5ZmFzczQxVlFiZU0yYXR3emU3WlRfb1U4Wi1sNW9QbUFFR3FiLTRjVDIxY0hCazBGSzRjOVR3OXUwdHN1SEpaZGxEaGU5andpSUN0TXNnME5fS2stVGN6a3JCbnNmc0k3bmtpanMwcmdtUXlTcXlWNE1TY2l2UERhRTc3TkJHemo3b3cwM3AzYTFrOE44Zw?oc=5>

### Amazon Is Up 11% in a Year. UBS Sees Another 32%, Even After Cutting Its AWS Estimates
- Summary: Amazon up 11% yearly; UBS forecasts 32% growth despite lower AWS estimates.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNc0pidzdBcEk3V1dKRlVNYXNTcXRvRW9VRU9iZnp1VTlvQVY4SXlKQ3JNMGdKbUZ5TE1lck1XZ056clJjT25QVUxfaTllQzZaYnNpZ21jWFVKVHF1NUFjYkVMLUw4QU5kXy1STE5qQ2x5bGotMkxiRDRKWXNFTzZya1BaVDZ6dTZxcWhfclNLeDFOVXdxdVE?oc=5>

### 59 Analysts Rate Amazon a Buy. Here’s Where the Stock Could Go
- Summary: Fifty-nine analysts recommend buying Amazon shares, suggesting potential upside and positive outlook.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQUGxDLTZ2a2xVbkd3SEppX1ctS0JqazBNeEV4YW1iNDdBeUprMWZUSXBfS1RrU1ZEZWYyOHJhN1ZUZXlINTl1TzNqbmpkWVJHUk5qSE9XREt6b3dPdVhib2otRVF1NnpIS21QcmxndTlFa09rUTdLWHhESUUtS2p5dWg3RHp2NnFLdjJka0hmdjVLNFdDbVFXOFg1NWVlYm9qXzNZQkVfaw?oc=5>

## RISKS

### Amazon: The Age Of Inference (And Big E-Commerce Profits) (NASDAQ:AMZN)
- Summary: Amazon's inference tech promises growth but may face execution risk.
- Date: 2026-11-16 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNQnRLX2xlM3NNZ3ctbTl3OF9OdlRwYktiRHBTeUN1bjZNRG0yTFBYaGw5OTdaVXRHcEVrMWt6WlRJWXpLT05xVEJoSFJnUEgxSDg0R1pmYXFMMWlYX2U2QU5kWlZtTUx0eWpWVjFxSnNaNWhRS0tIWUdOUkRkZk5td2dRanFxR1ZyNklUS2hpUXJKS1hT?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMZN** | **21.64** | **4.72** | **16.80** | **12.10** | **2,895,109,423,104.00 USD** | **20.31** |
| WMT | 46.14 | 10.30 | 24.52 | 5.90 | 1,010,441,912,320.00 USD | 26.67 |
| MSFT | 26.53 | 8.02 | 18.69 | 18.80 | 3,774,660,476,928.00 USD | 3.78 |
| GOOGL | 14.75 | 5.26 | 18.20 | 24.70 | 3,472,317,218,816.00 USD | -0.39 |

Peers fetched as_of: 2026-11-18; AMZN reuses existing data (market data as_of: 2026-11-18); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-18

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

- https://news.google.com/rss/articles/CBMipgFBVV95cUxOMlZzcndHVHcxM3A0VFVKY2NVZUhMejNRLXJJVjZBV1RiR3o1cXk3c28xcnRNbjAtTl8wUmtsUVFxc1RUZGxtNzVza3Y5cmNoZTF5dExRNUNuWnRSV0RFU1BFaFVxeHd2VHljbW5iUTVQMFR2QmR6VDN0Q1VLazNjZXRwVU81b0M2MHVXY3AydVpXb1FXQTBiMnpQLXBrR1MxQTVXZUJn?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNY3FYSHN1WVd5R2I5T0lTUXhrMmhMRVhwZ0FiTEZGTHRmaF92aHF2LUFpLVpWSXpUM2ZKYXdmbWRZUkp1MkV4aDluQzZSNncxTURrcmF2bU8xTWRFNzE2NU15WU1jVkRFY2NWeDFDekVQRjBHdi1tODg4SUtwR1pkajcwVmNjYmVEUFVteUVqOEk5elBpUkt4TjBVVEdFc0dTVm9qQ1lHN0MtQQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPWTZXSmptWXNhdDBlVUZFN2xDRE4xdzI2TDJ2b1NrN0paY0dyY2dUNFBKUUJHdi1zbnVyX0lGYm1teVI4ZEJXZU1sa1IwVjBnbTRld3JZd1FVVE9CYVIzOE9UNDI0Z0Vrb2doRFd4UGdkMUpJMGhjY3NWU1FzUW5IZzBVODBpdHU0NjltYmpPM18tekNTNGVJQ3FWcw?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPTkpLSzFzQVZ5V0xHYmhnVE5HSU1fMEZ5SVZjc2ZTLThtWHFfMDI3dWNiNkl5emt2TnhoUVRZd0dzM0ROS2VpWmxpcGw2SC1HQm5CVVNqUUhZRlFjLTFGb0FTN2VKUTMyODd5X3hfVzBjWmxieTB6NjE3c1QwMWVmYU05WnNzR0g3eEctY3RUMENMdERlYVdMUzZERm5wRzVjaDlvMTRxSGljQQ?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxOYTVRLVBIMzJZaVFPWVh6SlFDUXFwcUM3Z0JZVEYyM2ozbWdnUlBpNThUVkI2RnRoQWktUTg1c0tQcUdaM2tBcTR2Vk5rVm1DS1lPRkE5OUJwR0IwMWUwOHBlcng0dUxMcXpNdmF5OGlWRWhBaWpPRDVkbmZIa0ZSdjBIMnpKczZWZlFLUWx4OFY0bTF5YnBxeDZ4WHZHM0h0RXRDU1JIblZmbE5lMG93c0RGOVlmek1vNkFVMWNyY2pFWlNqT1pSWUY0THZsZw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNMC1xVGJpZTVvS3d0bDg4WkVDQW50ZHB5UmY4TEhGc0t4aFViZzB2Z1g1blNINzU5Tkd2bW5fZlhQRm1SMjBVUG9DTEVTRS1nZkdJRmQ2NUQ0TElYcVR6OUtSM196ZmUwRnhobGZsNnlYTF8weGF6WTVHQm9CVUZfTnlRdHhaa3RwTjV3VTlwMFJTRFlmMmRQcklkS09NM29Pb1E?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNUGk3cGhNR3c1UEE1dHgwakYwRW1fYmV4NXcxbXdqcWhxV1dtQ2JmbUdFRkFjYm4yU3R5Y0NnaDlPbFhmNXc1WEpxRlplVXYwWkxHQVZLUDhSOTQ5WFZNeXlzdEpSLVVnUF9ycmV6SnVYUXRuWm56c1BXWW1pZWp0RkdGVFRseUhGRDlxME0wSEJjZlRNNkVjLTZ6eEg?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPcFRWN0I0NVFPbC03RXNNTzdjLTg0RkFSM2dSVDNQOWJUSnA5NVl6SFRmLTRCMEVJVm5HeUFrZkxzb1JkZ21MT1dsb2V6b2RFYzZJR0drS0VpcFdBV1ZBZTBJcEtvT0E3MVZNSDYydWNTUEVRb2M4THo2bFlpdEF5eXU5UGJjSTJCVEFpWkROcjRkNFE?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNWnBIQWE0a2JUME11UzNpeTZUa0lqOEg0aFNMT05BV29YVldtdzNISHM1OWtrdHZsYkRHc2xTZmFjekh4dTltVEpROVRsZlFjcW8xR21QZ2t2aXpNcHNpb2QyU0lkdU5aZXV6bFVkdXNES09NRnh2MHJTeER1R2hud3o1UWdkSmR5ZnZoQmpRQjhvQk5nTlZtVnBMS1FGUDA?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPdnhpdEhzanE4RkFZb3FsR1hjYl93aktwY3hjV0NCQ1EtQzBBbDRMSzgzYjZoVEdKS2c1ZWU0RTRoMVd5Si1pSlR5R0VaOXQwRVByX1YzdUhLV1djN2ZoSmF1OTAycm5kanF1Y014ZXBSbVp0Q3Nqd0RmWjdJaEFtM3ptUDZsT25temNOTEY3YncxMU1SOHpzSU5fU0JNbjRT?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQaV9WVUdzMk5hM0tDU1FaeFB0dkpRenRRaUFFWWdFaVZCVUdpT3hVc3cxeWZfeTlQNjVBVHJjRzdxS1dsclRZeHBIblVhQWkzMEliOU5vUzVFODgtQUI3VHJjVnVVZGd4V1lnNUVvWVdBc0hzUW5wX1JlZ2FMV0hVOXViZEFfTE1WcDFpVE1ySXRrZkVGRk5F?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxOYU1Lcy0yRzhtLVRmZ003M0VQVVJTbUF3ZEFXMVItd3JjdElrZVdYalkzWjNsVXNvaDkzcHYtZHBEWnRVREw5T2YzaHZNUEQtRVJEeVVWUlE0WDUwMF9PXy1zS05FMFlaS0Myc3ZCVHFWVmVsYXd0VXBHQl9qOXhXMFFNQm9iaWUtbjl4VW9ZUFg1Y3VnSWIwZHl6c2dscnNUMWhFRklQZGc?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxNTmhQcEsxU3pxQ0llWWdvenNGWTdTY29QOExSU1c0VDFQOGhpajdJeFo5d0tlUzc4RmdjYzh3aV9uc0xhYXQxejRRVDI5ZmFzczQxVlFiZU0yYXR3emU3WlRfb1U4Wi1sNW9QbUFFR3FiLTRjVDIxY0hCazBGSzRjOVR3OXUwdHN1SEpaZGxEaGU5andpSUN0TXNnME5fS2stVGN6a3JCbnNmc0k3bmtpanMwcmdtUXlTcXlWNE1TY2l2UERhRTc3TkJHemo3b3cwM3AzYTFrOE44Zw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNc0pidzdBcEk3V1dKRlVNYXNTcXRvRW9VRU9iZnp1VTlvQVY4SXlKQ3JNMGdKbUZ5TE1lck1XZ056clJjT25QVUxfaTllQzZaYnNpZ21jWFVKVHF1NUFjYkVMLUw4QU5kXy1STE5qQ2x5bGotMkxiRDRKWXNFTzZya1BaVDZ6dTZxcWhfclNLeDFOVXdxdVE?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQUGxDLTZ2a2xVbkd3SEppX1ctS0JqazBNeEV4YW1iNDdBeUprMWZUSXBfS1RrU1ZEZWYyOHJhN1ZUZXlINTl1TzNqbmpkWVJHUk5qSE9XREt6b3dPdVhib2otRVF1NnpIS21QcmxndTlFa09rUTdLWHhESUUtS2p5dWg3RHp2NnFLdjJka0hmdjVLNFdDbVFXOFg1NWVlYm9qXzNZQkVfaw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNQnRLX2xlM3NNZ3ctbTl3OF9OdlRwYktiRHBTeUN1bjZNRG0yTFBYaGw5OTdaVXRHcEVrMWt6WlRJWXpLT05xVEJoSFJnUEgxSDg0R1pmYXFMMWlYX2U2QU5kWlZtTUx0eWpWVjFxSnNaNWhRS0tIWUdOUkRkZk5td2dRanFxR1ZyNklUS2hpUXJKS1hT?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
