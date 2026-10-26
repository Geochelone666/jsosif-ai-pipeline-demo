# AMZN Intelligence Report

- ticker: **AMZN**
- Report as_of: **2026-10-25**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/AMZN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMZN/key-statistics/
- AI analysis snapshot as_of: **2026-10-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-26T01:06:43.738228+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 5, 'ai': 11, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 11 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 34.78%; oldest publication 2026-10-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 248.0000 |
| Return 1D (%) | -0.9506 |
| Return 1W (%) | -0.8000 |
| Return 1M (%) | -0.5095 |
| Return YTD (%) | 7.4430 |
| Return 1Y (%) | 12.1715 |
| Annualized volatility (%) | 34.7709 |
| Beta vs SPY | 1.4732 |
| Max drawdown (%) | -21.7362 |
| Sharpe (rf=0) | 0.5011 |
| Downside deviation (rf=0, %) | 20.9566 |
| Sortino (rf=0) | 0.8315 |
| Historical VaR 95% (1D, %) | 2.9597 |
| Historical ES 95% (1D, %) | 3.9961 |
| Correlation vs SPY | 0.5401 |
| Tracking error vs SPY (%) | 29.8788 |
| P/E (trailing) | 19.95 |
| P/B | 4.85 |
| EV/EBITDA | 16.60 |
| Revenue growth (%) | 19.60 |
| Forward P/E (estimate) | 23.78 |
| Gross margin (%) | 50.77 |
| Operating margin (%) | 13.69 |
| Return on equity (%) | 30.56 |
| Free cash flow yield (%) | 0.12 |
| MA50 | 255.6476 |
| Close vs MA50 (%) | -2.9915 |
| MA200 | 243.2929 |
| Close vs MA200 (%) | 1.9347 |
| RSI (14, Wilder) | 43.1691 |
| MACD (12,26) | 0.1900 |
| MACD signal (9) | 0.6158 |
| MACD histogram | -0.4259 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMZN': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 248.0000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.9506 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.8000 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -0.5095 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 7.4430 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 12.1715 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.7709 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.9566 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.8315 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9597 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9961 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5401 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.8788 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.4732 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -21.7362 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5011 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.7774 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.7700 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 13.6890 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 30.5580 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.1203 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 19.9517 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 43.1691 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.4259 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -2.9915 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 1.9347 -> Slightly above the moving-average trend level.

## TAILWINDS

### Amazon’s Bee AI Wearables Could Be a New Growth Driver for AMZN Stock
- Summary: New Bee AI wearables may boost Amazon.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNNEFZWklmV1BYT19HSERSSDZSTXF2ZXlrS0VHMU4ta3ZmdzdJZDBvNVBDb3o5Yk5mMGlmQk53SXBqR1d2YTFheHVVUHVJdUNLazd5Q19RZl9pQWhMTlRialo4MG9fNEhIS2wtdmY5WEgtbnYwZGk2RERsZ1VNYThiMHlyaXBGR0trekhMWDJPWnotMFMzNXJZYw?oc=5>

### Stock Market Today, Oct. 19: Amazon Surges on Morgan Stanley Top Pick and $350 Price Target
- Summary: Amazon stock jumps after Morgan Stanley upgrades to top pick with $350 target.
- Date: 2026-10-19 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPU05Balk3MG8zWGx6OHlXT3NxU2hjbzNDU1lzYzB3VHhXTGdnZ00zS1VVR0c0eVFYS0ZyMGZDMm9peGVHbUk4VTRVRDFZZDJkZ09KaVdWYWc0aFNCaTRHdE5QQ3JqVTFRZG8zVlM1a3E5bUtxa3VKdWJrTmhDMW5QSmZ0TTluR3F5RFMydV84bXR1UXpt?oc=5>

### Wall Street Firm Names Amazon Its Top Pick With More Than 30% Upside. Is the Stock a Buy?
- Summary: Analyst names Amazon top pick, citing 30% upside potential.
- Date: 2026-10-22 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQbnRpTmJ5SUZvWmJUSlN1cW0wMmhwZUpmQU5lbGtvZnpTSkZJX0tLN3dlcmtTUm1LZ1RSUXhwRUo3TGhiVmYzc1c0dVppTXNEVjZ6Z0thOFhaeHg5aXlWWDRRYm1zX052eURpRC1QdDZzazNGTTlEb0xxSnNNa2EtdmJlR0xoUGRUS1VheWVLdVg5T3ZFemxDUg?oc=5>

### Amazon (AMZN) Stock Costs $250 a Share. Here's Why I'd Still Buy It.
- Summary: Amazon stock at $250, recommendation to buy.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQVFk1Tlk3Sk5saVdyWElPVGJaRHVPODl5cWJhV2NTNG1jWjJJeVhoU3pNMkdVNmlfWmpidHlDZFZ5S01iRFpNOUxnQUw1bllheTVreW93U2VoNzluUGR3V0oxa1JVakVzRHNRR0JoUXIyT3VRQnFhcEJ0a2d1NVAxSFpFR0FYNDlXZTlvUmV2M2ltZkpndG45Zw?oc=5>

### Why Amazon (AMZN) Stock Is Up Today
- Summary: Amazon stock rises today.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQU3pTZEJjVGVLLUg3WmZTV2xmN1R6Zm9wWTB2bXdYOGNtNXNKVTdqTHNFTDMyLVNjZERUa1U5blotTG5hVEtseGZCRkcxazlkdVpsOVh6c1YxSzBSMGNQT3lBclB4VUgyajN4SUpDODNEQTBUWGgwNUVrclhWVjhyc3prZHY1TjhObjdsakZLaXRxcTAyRXJ3?oc=5>

### Amazon (AMZN) Suffers a Larger Drop Than the General Market: Key Insights
- Summary: Amazon stock drops more than market.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQNFU0TGNVU1Iwa3hrYXNvYmMxVW5mejhzMENQclJpUVRseWpGSVYyM2tfUUFrWktKTE9qdTI1RmdRbVh6VUJLQ3dlQjVVNVVXMkJWUFJWZFB2OHJtamFrZzlKN21VX2xNTjlnd2RtMEFYUC13elVKMjhXSy1HUmowSHFEN0w0MFlPU0ZpbEFhRlZsT1h1SXZRajhmazI?oc=5>

## HEADWINDS

### Microsoft (MSFT), Alphabet (GOOGL) and Amazon (AMZN) Earnings: Can They Save the AI Stock Rally?
- Summary: Earnings season may dampen AI rally, affecting Amazon.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxPOG5TZHpqYkVsSTVEUDhRZGdualhHTnFTSTBtaHBrWE1tUVp1clNEbHFxWEVfNDZlV01NNjYzdjczM3lrSkFiN2E3el9NOHZKV1hqZEFkblVTdnZDN0lrd0tUUXp3Zkk1U3JmX0ZxbktGay0xMWlxdHV4SFY3cW0tcQ?oc=5>

## CATALYSTS

### AMZN Stock Sees A Slew Of Price Hikes After ‘Clean’ Quarter – Amazon Sits 'Atop the AI Hyperscaler Pedestal', Says Analyst
- Summary: AMZN Stock Sees A Slew Of Price Hikes After ‘Clean’ Quarter – Amazon Sits 'Atop the AI Hyperscaler Pedestal', Says Analyst
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxOd1UzS01WRGZDM0otSzZPYlVOemMyZkRVY2ZGTTB3bjdTYmQwUE82TWhiSVBNZTgtaU1VT1NpbkxrYkFxOGVKWjJ3ZFg1djJQRktUZFJueklNLUpDbXVJMkVoaHR2TW92YlR4YmdOTmR2bWwzYXJBcXVEQjBqemZEV1F4bDZjU2ZMSW5yZGZjMm1SelVtU0ZqT0R4SmhrTnhWTFhuUkRGZDliT2pJU09naXdrdHJrMm5UYUFqX0JycUgzZw?oc=5>

### Amazon Q3 Preview: CAPEX Spending In Focus, Shares Fairly Valued (NASDAQ:AMZN)
- Summary: Amazon Q3 Preview: CAPEX Spending In Focus, Shares Fairly Valued (NASDAQ:AMZN)
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQRVlYdWNNeGtGS3BWTnJhQU41SHpwbXlaWjd3U3NsQ0VmamJSUmxSUkpZTk83aU92aUhuNkVYaThmTmZURHZNSjloUS05aDB3ZG5rMlNUREFVczdRUkNKaGN5aE5aZ3Q0SjhsZ2U3VzQ2M3dGTXhBNkdWWE1WSmF5NkZVT1BBOTh3dUVOeXZTS3Z1TkNSRXVMbDFaVl9MTVlKaG5UUzR3?oc=5>

### Amazon stock pops after Morgan Stanley details 5 catalysts, lifts price target
- Summary: Amazon stock pops after Morgan Stanley details 5 catalysts, lifts price target
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxNR1N4OXljU1k1MUpnU1VlQ0tjY3ZZR1ZIQzdEaGJwSkZoMEkwUlRyTGJNR1BpSUg4QWpsRHJXOW9EZzFaQ3pOQUZFaFMyTUpudVhONDJFWWJneHBDQ0JlX2paTkV3UnFmaUZPNzZBM3ZzZGQ1RU1WS25keXZBYW9aSThxTnNOY0tjMVltakZnRHE4RnZONFFLTHNSWGdvalVtT2prb1h5YXFjVlU2ZFZGcXZTd2ZlMFY3eFNEdFcxLWkxU1J0VWdiN0FHSEpWRjJoM0szT2dnNjQ?oc=5>

### Amazon (AMZN) Reports Next Week: Wall Street Expects Earnings Growth
- Summary: Amazon (AMZN) Reports Next Week: Wall Street Expects Earnings Growth
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOWlRBTi1nNDItY2IwMzgxbkUwQm9FN1BfZ3lNYnRURFdfRGN1dkZJNS15UC1abmdCdEdyRHZFTVhpenJXNTZwUGZxUzMwWU94dFNXaVd1VkxYenJqdGtNU0M1OUFLYkxoejRxNklvb2ZYcjVkX003SmtHNDRhZktoU0hQRnBvVU5TVTZhSGJ6bEZUS3RqdzBzdkVR?oc=5>

### Amazon.com, Inc. $AMZN Stock Sold by First Merchants Corp
- Summary: Amazon.com, Inc. $AMZN Stock Sold by First Merchants Corp
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxPT3ZFVi1mT2xiX0hfMGRjMHBjc2xmWXNBaERaTmJYYkFmZEstRzh5YklyeWp0NXZyMFpGbTJuNjBLX1p4RzV2dXJHbS1GeWlMRW5kakdDalZqMEdzOTd2LXJDUFhmQzN2T3lrcGlUamZnWGNvakl3a0JobVZyMWRTNnQtNkE2UFRzbkFxVHl0RkNINWx5QzZWSHpkVHdHZlR6UmplWTFJSUtKSDRLRE9pNDc0UFc?oc=5>

### With Amazon Earnings On Tap, Here's How To Ride Out The Volatility
- Summary: Amazon’s upcoming earnings create volatility; investors advised to navigate.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOeS1MSVRTMV9VMTJpZlk5T3lpVFhHQWV1UWE0MUU0RDVwUmlLM0h4QWFhM21KVmt6RVlpVjd2aWlnZnByZGFrb1pITm9wUGZJRU1ESl9ya2FhM2ktZHNzUUtHOUVhWHJCcUtvRks2X2lDbVAwelhaQ0hyQTR4NklaT1hzcm1FeUwyT3hOUEtfbDZLRGJDVi1XSTZoX1Ixdw?oc=5>

### 1 Analyst Says Amazon Stock Has 30% Upside. What's the Bull Case for Buying Amazon Right Now?
- Summary: Analyst projects 30% upside for Amazon shares.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxOc3o4a3QxaE5aa2h6eWY2NW4tMS1tNkZYSGd1NTZWMWdZd2VlaHc3eE9KazlCQnBqUVdJdWlyTHExbE5FYUQ5czVkWDBnY21SV3ZGLVA1YjkyWVFNYUtUU0RReHpXRV9ValZ3dVMxQ0JsaHN6Y005dXM4RUlPWWFmZ1FFaVdFZ0t3TTQ2Nw?oc=5>

## RISKS

### What Could Go Wrong With Amazon Stock?
- Summary: Highlights potential risks to Amazon stock.
- Date: 2026-10-23 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOanJhbW1jX2FZNDY4TXZEWGFjc1U5dWdQLTV0a3hsME5CZmtYUEI4QXFGWFV0QmRpSmc4OUVCNzVXNmVqcTA1cGRxX2pjbTVzTGxwUTE4OHJobUV2ak5wZXJGbFMza1pJd19oc3hVNU4yTThHTnp4YTYyeG9QOXg2SGYyZTdtaHBTOXEtTnZnazRGUy1sQUZrWWZvSk5oNzg?oc=5>

### Amazon (AMZN): Can Custom AI Silicon Outpace Capex Commitments?
- Summary: Questions if AI silicon growth can outpace capex commitments.
- Date: 2026-10-21 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQOVBBRFY0SjhEM2tOMjFrMlVUd1ptdHNxOVZ6c1lEVEVaZ2g1UXBxQnN1WlFqRTRkWHRjN19YblFxVzNiU1VBLUJlbU9Mc1VFdXZGRF9QRFFkdVMzdkZPRXdmdUtuekpRT21tVWNkWFFObXQtU09WMnBBRmVoUmRla2NCcVFfTlhjTHhHOEJuMXNHTHFIcjNEWQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMZN** | **19.95** | **4.85** | **16.60** | **19.60** | **2,675,005,718,528.00 USD** | **12.17** |
| WMT | 43.44 | 9.69 | 23.17 | 5.90 | 954,094,059,520.00 USD | 13.14 |
| MSFT | 29.22 | 8.81 | 20.32 | 17.70 | 3,894,773,022,720.00 USD | 1.59 |
| GOOGL | 16.07 | 6.29 | 22.02 | 24.20 | 3,916,147,458,048.00 USD | 26.85 |

Peers fetched as_of: 2026-10-25; AMZN reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-30
- Next expected earnings: 2026-10-29 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-25

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

- https://news.google.com/rss/articles/CBMimAFBVV95cUxNNEFZWklmV1BYT19HSERSSDZSTXF2ZXlrS0VHMU4ta3ZmdzdJZDBvNVBDb3o5Yk5mMGlmQk53SXBqR1d2YTFheHVVUHVJdUNLazd5Q19RZl9pQWhMTlRialo4MG9fNEhIS2wtdmY5WEgtbnYwZGk2RERsZ1VNYThiMHlyaXBGR0trekhMWDJPWnotMFMzNXJZYw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPU05Balk3MG8zWGx6OHlXT3NxU2hjbzNDU1lzYzB3VHhXTGdnZ00zS1VVR0c0eVFYS0ZyMGZDMm9peGVHbUk4VTRVRDFZZDJkZ09KaVdWYWc0aFNCaTRHdE5QQ3JqVTFRZG8zVlM1a3E5bUtxa3VKdWJrTmhDMW5QSmZ0TTluR3F5RFMydV84bXR1UXpt?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQbnRpTmJ5SUZvWmJUSlN1cW0wMmhwZUpmQU5lbGtvZnpTSkZJX0tLN3dlcmtTUm1LZ1RSUXhwRUo3TGhiVmYzc1c0dVppTXNEVjZ6Z0thOFhaeHg5aXlWWDRRYm1zX052eURpRC1QdDZzazNGTTlEb0xxSnNNa2EtdmJlR0xoUGRUS1VheWVLdVg5T3ZFemxDUg?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQVFk1Tlk3Sk5saVdyWElPVGJaRHVPODl5cWJhV2NTNG1jWjJJeVhoU3pNMkdVNmlfWmpidHlDZFZ5S01iRFpNOUxnQUw1bllheTVreW93U2VoNzluUGR3V0oxa1JVakVzRHNRR0JoUXIyT3VRQnFhcEJ0a2d1NVAxSFpFR0FYNDlXZTlvUmV2M2ltZkpndG45Zw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQU3pTZEJjVGVLLUg3WmZTV2xmN1R6Zm9wWTB2bXdYOGNtNXNKVTdqTHNFTDMyLVNjZERUa1U5blotTG5hVEtseGZCRkcxazlkdVpsOVh6c1YxSzBSMGNQT3lBclB4VUgyajN4SUpDODNEQTBUWGgwNUVrclhWVjhyc3prZHY1TjhObjdsakZLaXRxcTAyRXJ3?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQNFU0TGNVU1Iwa3hrYXNvYmMxVW5mejhzMENQclJpUVRseWpGSVYyM2tfUUFrWktKTE9qdTI1RmdRbVh6VUJLQ3dlQjVVNVVXMkJWUFJWZFB2OHJtamFrZzlKN21VX2xNTjlnd2RtMEFYUC13elVKMjhXSy1HUmowSHFEN0w0MFlPU0ZpbEFhRlZsT1h1SXZRajhmazI?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxPOG5TZHpqYkVsSTVEUDhRZGdualhHTnFTSTBtaHBrWE1tUVp1clNEbHFxWEVfNDZlV01NNjYzdjczM3lrSkFiN2E3el9NOHZKV1hqZEFkblVTdnZDN0lrd0tUUXp3Zkk1U3JmX0ZxbktGay0xMWlxdHV4SFY3cW0tcQ?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxOd1UzS01WRGZDM0otSzZPYlVOemMyZkRVY2ZGTTB3bjdTYmQwUE82TWhiSVBNZTgtaU1VT1NpbkxrYkFxOGVKWjJ3ZFg1djJQRktUZFJueklNLUpDbXVJMkVoaHR2TW92YlR4YmdOTmR2bWwzYXJBcXVEQjBqemZEV1F4bDZjU2ZMSW5yZGZjMm1SelVtU0ZqT0R4SmhrTnhWTFhuUkRGZDliT2pJU09naXdrdHJrMm5UYUFqX0JycUgzZw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQRVlYdWNNeGtGS3BWTnJhQU41SHpwbXlaWjd3U3NsQ0VmamJSUmxSUkpZTk83aU92aUhuNkVYaThmTmZURHZNSjloUS05aDB3ZG5rMlNUREFVczdRUkNKaGN5aE5aZ3Q0SjhsZ2U3VzQ2M3dGTXhBNkdWWE1WSmF5NkZVT1BBOTh3dUVOeXZTS3Z1TkNSRXVMbDFaVl9MTVlKaG5UUzR3?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxNR1N4OXljU1k1MUpnU1VlQ0tjY3ZZR1ZIQzdEaGJwSkZoMEkwUlRyTGJNR1BpSUg4QWpsRHJXOW9EZzFaQ3pOQUZFaFMyTUpudVhONDJFWWJneHBDQ0JlX2paTkV3UnFmaUZPNzZBM3ZzZGQ1RU1WS25keXZBYW9aSThxTnNOY0tjMVltakZnRHE4RnZONFFLTHNSWGdvalVtT2prb1h5YXFjVlU2ZFZGcXZTd2ZlMFY3eFNEdFcxLWkxU1J0VWdiN0FHSEpWRjJoM0szT2dnNjQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOWlRBTi1nNDItY2IwMzgxbkUwQm9FN1BfZ3lNYnRURFdfRGN1dkZJNS15UC1abmdCdEdyRHZFTVhpenJXNTZwUGZxUzMwWU94dFNXaVd1VkxYenJqdGtNU0M1OUFLYkxoejRxNklvb2ZYcjVkX003SmtHNDRhZktoU0hQRnBvVU5TVTZhSGJ6bEZUS3RqdzBzdkVR?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxPT3ZFVi1mT2xiX0hfMGRjMHBjc2xmWXNBaERaTmJYYkFmZEstRzh5YklyeWp0NXZyMFpGbTJuNjBLX1p4RzV2dXJHbS1GeWlMRW5kakdDalZqMEdzOTd2LXJDUFhmQzN2T3lrcGlUamZnWGNvakl3a0JobVZyMWRTNnQtNkE2UFRzbkFxVHl0RkNINWx5QzZWSHpkVHdHZlR6UmplWTFJSUtKSDRLRE9pNDc0UFc?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOeS1MSVRTMV9VMTJpZlk5T3lpVFhHQWV1UWE0MUU0RDVwUmlLM0h4QWFhM21KVmt6RVlpVjd2aWlnZnByZGFrb1pITm9wUGZJRU1ESl9ya2FhM2ktZHNzUUtHOUVhWHJCcUtvRks2X2lDbVAwelhaQ0hyQTR4NklaT1hzcm1FeUwyT3hOUEtfbDZLRGJDVi1XSTZoX1Ixdw?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxOc3o4a3QxaE5aa2h6eWY2NW4tMS1tNkZYSGd1NTZWMWdZd2VlaHc3eE9KazlCQnBqUVdJdWlyTHExbE5FYUQ5czVkWDBnY21SV3ZGLVA1YjkyWVFNYUtUU0RReHpXRV9ValZ3dVMxQ0JsaHN6Y005dXM4RUlPWWFmZ1FFaVdFZ0t3TTQ2Nw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOanJhbW1jX2FZNDY4TXZEWGFjc1U5dWdQLTV0a3hsME5CZmtYUEI4QXFGWFV0QmRpSmc4OUVCNzVXNmVqcTA1cGRxX2pjbTVzTGxwUTE4OHJobUV2ak5wZXJGbFMza1pJd19oc3hVNU4yTThHTnp4YTYyeG9QOXg2SGYyZTdtaHBTOXEtTnZnazRGUy1sQUZrWWZvSk5oNzg?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQOVBBRFY0SjhEM2tOMjFrMlVUd1ptdHNxOVZ6c1lEVEVaZ2g1UXBxQnN1WlFqRTRkWHRjN19YblFxVzNiU1VBLUJlbU9Mc1VFdXZGRF9QRFFkdVMzdkZPRXdmdUtuekpRT21tVWNkWFFObXQtU09WMnBBRmVoUmRla2NCcVFfTlhjTHhHOEJuMXNHTHFIcjNEWQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
