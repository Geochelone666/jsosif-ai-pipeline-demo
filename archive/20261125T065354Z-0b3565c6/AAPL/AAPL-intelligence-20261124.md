# AAPL Intelligence Report

- ticker: **AAPL**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/AAPL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AAPL/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T06:58:56.415570+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 8, 'ai': 7, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/AAPL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 8 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 354.0700 |
| Return 1D (%) | 1.4295 |
| Return 1W (%) | 0.6138 |
| Return 1M (%) | 1.9006 |
| Return YTD (%) | 30.6936 |
| Return 1Y (%) | 28.7705 |
| Annualized volatility (%) | 24.9487 |
| Beta vs SPY | 0.5713 |
| Max drawdown (%) | -13.7985 |
| Sharpe (rf=0) | 1.1427 |
| Downside deviation (rf=0, %) | 16.9835 |
| Sortino (rf=0) | 1.6787 |
| Historical VaR 95% (1D, %) | 2.0034 |
| Historical ES 95% (1D, %) | 3.4742 |
| Correlation vs SPY | 0.3425 |
| Tracking error vs SPY (%) | 24.3011 |
| P/E (trailing) | 39.43 |
| P/B | 45.91 |
| EV/EBITDA | 30.23 |
| Revenue growth (%) | 11.70 |
| Forward P/E (estimate) | 33.49 |
| Gross margin (%) | 48.79 |
| Operating margin (%) | 33.01 |
| Return on equity (%) | 142.26 |
| Free cash flow yield (%) | 2.05 |
| MA50 | 342.3697 |
| Close vs MA50 (%) | 3.4174 |
| MA200 | 303.5461 |
| Close vs MA200 (%) | 16.6446 |
| RSI (14, Wilder) | 56.8556 |
| MACD (12,26) | 2.7697 |
| MACD signal (9) | 3.1886 |
| MACD histogram | -0.4189 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AAPL': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 354.0700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.4295 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.6138 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 1.9006 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 30.6936 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 28.7705 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 24.9487 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.9835 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.6787 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0034 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3425 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.3011 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5713 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.7985 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1427 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 33.4890 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 48.7860 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.0100 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 142.2570 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.0534 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 39.4287 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 56.8556 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.4189 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.4174 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 16.6446 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### Apple (AAPL) Stock Could Be 33% Overvalued On Fresh Service Outage Concerns
- Summary: Service outage worries may depress Apple’s valuation, signaling potential short‑term downside.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPcW1UV2NiYVZ2ZmxTbDc1dVoxblRuVWpUSlFHdWlaRXhzMmFUWFoxRHY2c2hMTEFyNmdrbUwwTHU0YUswM1VDMF9XZGVpbUhEaHRhSEwzdXZxaFFVVlNUWEJhNU5MTXRvY2tVd1FVbldtX0JfYUlyRG94MTh6WnEyWHF6Nl9mRkszMGJ4SW5mOWZDOTBK?oc=5>

### How Investors May Respond To Apple (AAPL) Service Outages
- Summary: Service outages could negatively affect investor sentiment.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOXy02WGZ5d1JKRjdEUFlEZm92TmEwYy1Kd2F6X0lobUIyd0sxSFJrNlhGR3hOMkxma2ZpQmQ0V3RaUXVnUFNGR3dLc3RzTHFCcEJOaXNsRlVCS2dxZWVwOWExbUFiQi1pYnFuNGZlTzExLWZmNXd2WlJHWkV4WWdtLUFleE5iWTdMeW9wb1d5RTBjbHRXblhqVDY5WkpTUQ?oc=5>

## CATALYSTS

### Apple Stock Has 3 Things Going for It in 2027. Here’s My Price Target
- Summary: Apple Stock Has 3 Things Going for It in 2027. Here’s My Price Target
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPSUhjckIzQThzNXJUVXhqNzRLVUp1eEhsY1p2VDVNTGhOblRmOFJxXzRKV09wZkFhbmF1U3JIaEsxclB4Y0Fwc0RiajhCMGJDanpSbEVZdGg1SlhaNy1VNGxaTWJKU1RnUmdPSFMxdkxSYkFXb2F3azV3TGdlVVhDT1pmQldxVklzTXJiR3E2bVppNkQzeVE?oc=5>

### Apple Inc. (AAPL) Delivered Strong Results: Why Investors Are Watching Its Next Move Closely
- Summary: Apple Inc. (AAPL) Delivered Strong Results: Why Investors Are Watching Its Next Move Closely
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPLTlCTmhMLXRPNjhlZnU1Q2Z0V3VwR3FTR0haUlBObWNOWjdWM3luWnhwWWNfNnhxVXlrT1kwMlVpdEYySEFMMkxTbi1sR0Nza19XS2tQUjFkWHQ4V3dzT1VIQTFyVzRPU2RZd2Q1N2hENkxuN09TU3llRWRjMVZCZGNlbzFOXzBJbDZ0QXlQbHZfLUoybUl3N2VDQlU?oc=5>

### Apple Nears a Rare Long-Term DRAM Supply Deal With Samsung Electronics. What This Means for AAPL Stock.
- Summary: Apple Nears a Rare Long-Term DRAM Supply Deal With Samsung Electronics. What This Means for AAPL Stock.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQZTAzU2dvbVdZTzN2Smttc1pjc3lsSW5qWTdldDFETUFxNmx4Y2Z1RkZSNG5EcXR0bFlueDdLY2Y4cWxfdGxiYktmeWVDODhnclQ5eEpWZVZRVHlJZjhkalNMVlk1UUpKaW9IS3NRN3RVcnF1MHhEbnVaZWdQaThJRjdud3VSSGkxREdfWHVTelZxSGdXTXc?oc=5>

### Apple Inc. $AAPL Stock Bought by Investment Partners LTD.
- Summary: Apple Inc. $AAPL Stock Bought by Investment Partners LTD.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxNV0MyNHFRQXdJLXFlX0p2SGxBYnJvM3hueDNPV1Vha0tTZzhIbUNldnJPZUN6cUxHa2hnN29QbldsMWtMTlVYSVVHczkzNGM1Q1pWN1FaQXNTeDZ2TVNlckIxR3gyTDJJNzA2Skd4czNJZGFFaGNGRUdDdlczR3pGTk5XUi11dFM1bUJ6U1RvM1hSVm9mMHhQNWdURDctSzg5VjRvS001dXQwM3hjSjY3S3h0OEpldw?oc=5>

### Apple Inc. $AAPL Stock: Moss Adams Wealth Advisors LLC Cuts Position
- Summary: Apple Inc. $AAPL Stock: Moss Adams Wealth Advisors LLC Cuts Position
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxNZ1BZMldHMWlfNG43bmhLQkhHMnl4alBvQWU5UTltVlNHNVk0dHFFOVFwbUVlbkllYlBKNGJ3NVN2T05ic0RRLVZPTnBYekY1NHNqek11NFJteHVBSW1OcGNad0JKVGwzRFpGRWp6ejZsMDJFT1JzdndBTFF6R1ViVS1uLTR2d1I1ajU4bVFlSTFwRUM1cFhNUVhldzdiQllGYldJNkZ3dTF2MUdyOWJidU1fTF90bVhtQzRYLUpMT2tQWm8w?oc=5>

### Apple Inc. $AAPL Stock Sold by Raleigh Capital Management Inc.
- Summary: Apple Inc. $AAPL Stock Sold by Raleigh Capital Management Inc.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxOcm1CLVpuU1QzUk9GQ3EwU1lvc3F3QjZPaUZLdllnY2p3eUFiU0Q5ZnN6VEU4OWh1RXdUR3BvTjFqZS00WkVBTzNIQ1BuYURXVzN0OUN4OUc0em92NFlTN1pQUW5IODBUQms0ei04MlZSUm54SnNGMEUwUGdnbjlseEZXX0FZaFZpOUV2MmV3dW9LVUgteVhpbzd1OElLdm9tQmxaMUNVNlk1SVRlcHRkaUJoVVh3SXowOWx6Xw?oc=5>

### Apple Inc. $AAPL Stock Acquired by CFC Planning Co LLC
- Summary: Apple Inc. $AAPL Stock Acquired by CFC Planning Co LLC
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPa0E0Rzk0Nl9rejYyMU83aFc1YmNVZ0Y1UjlBN1JBTV9pSEY3cVZ5bW1iRmZOSGNrNU91dHBhTEU5S2hHdEZ0cllLNnc1Vk4tRGJWOE5TNHU1ajExUlJWVkhKU01odkVJd0lza0JzRlpxWHp3dVdzZVJsUHJUNVJfd3oxNWlOZktfVWhhNjJOS2VwWHZKQmZnZHBmVFBuZDdEMWtlQmdyWEJrMW45MHY5YU13MA?oc=5>

### Apple Inc. $AAPL Stock Bought by United Asset Strategies Inc.
- Summary: Apple Inc. $AAPL Stock Bought by United Asset Strategies Inc.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxQd2R0dnZub2w2YVV1Ri1YRXBUdTRGMC02dVphM1F0R2Jtajh1SzlIMXBaQTFvNHZBNzJQeklrbEIwZDRPSnNTUE02Q0lPZjVrTVc1SmRDQjM3NDZKRkExUS1RUkhNQzc5Wk82ZGVSZF9lSnZWNXpkbExEQXJXMTJDa2s1aThidzdCdkZZSXh6M293THViTlQxTEJnSk1jVzNncHp4YmdvLUlIeGktLTBHSW5kU0p5NzJveV9r?oc=5>

### Apple Is Now Worth Over $5 Trillion Without Betting Big on AI Data Centers. AAPL Stock Now Trades Near Wall Street’s Targets.
- Summary: Apple’s market cap surpasses $5 trillion; stock trades near analyst targets, indicating bullish sentiment.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi-AFBVV95cUxNRXVwb1laS1Btbm1iTjFsMEg3OGRxd2I4MDBheXBhTmpLTnBpLVpFaGZCdmVabEZnS3FWREh5WDAxcW1KVGpOVFB5NzltWnAyakRibjhhckdQM3BpcVRtSTdHckRoY2RtRFdmZG82T3NlY0xkLS1MczU4b29KQXFXVGdXSjNHMUxBT0NoZmRSb0tuYTdCOEZYWWhGRW8xbUVOTlhkZjJFVGhOUEVaQVptUW05eW1UalZBeG9wRUhLVXljWlVFU0JLc0dkVm1aZjM5OHJEWlVuUmFUd1FJNW1Rdi1UdDN5YlRER0JMZnVpaGNvSVUyRUx5ZA?oc=5>

### AAPL Stock Alert: What to Know as Apple Develops AI Agent to Compete With Muse
- Summary: Apple’s new AI agent launch could boost product portfolio and market share.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQekFPM3ZncUc5OWU5R3NERDJHalhFbE9WNURJNUNmc3RnelpCTW9OcHNHcXZuTDMxVGtMbWkwUnM3WDBCSHVYalU4dnhzWFY4NW10dGJROGVEOE5KNXNIUjJUY1ltN1A3SHJTZE9XS0ZUQTNUT0c5S1BVUzJGRDlzVlVuZkV4YUNNTHFxZVhmai05QUcwdmc?oc=5>

### SA analyst upgrades/downgrades: NVDA, CMCSA, ANET, AAPL (SP500:)
- Summary: Analyst action on Apple may influence investor perception and stock movement.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxQbWg0cFB4Vk41bk5zYng3OXJzQ1VkTHVDVzJlZXBsRGhBUExzX2tuSHBvdFUycHc4d2gxcUMtenhQUGFLYjhEOHRqMTdoNG9rdzllQWxMd09TOEJzTDgwSWdtbTFiMWRWQVZsb29yS0dtWVdQdFVlampkQTkzaml5emJHcFBoZy1OcngyOHNfZzFmQQ?oc=5>

### Apple (NASDAQ:AAPL) Stock Jumps 1.4% - Time to Buy?
- Summary: Apple shares rose 1.4% on the day, reflecting positive market sentiment and potential investor interest.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxNUFRwY3ViWDBsZy1aMUMzUkIzdjV1bDFSdkdFM0VYR3dTTVZzbm5RYzVZbXhxZVltQ2VCM2NZU2lCaHFBcUV3SDA1TTd3XzFSYWZfeUhqTDRVNldpVnM5VGx6Y0FicUI0NG1FaG15aldRNTZoVE9hTG5RQjlESnV4Z09PaFpPWHplOXEyVEljcjg3ZFpDb25ieFQtYk4wYUNiSnpUN3ZOUQ?oc=5>

## RISKS

### Apple: The Hidden Risk Behind My Downgrade (NASDAQ:AAPL)
- Summary: Analyst downgrade highlights hidden risks to Apple’s outlook.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNaG1BZDFsdExZcmFBTHcwYkZGMElvdlhwMk1kRVl0RUlOTk90REhiRVJubWI0RlFqVWYyYWYxTUk1UjVkZzFtZGNyMXd6U0FuT0FTY2pPSDlVN3JCODFrSTFjZjEzSFY5TlhoenhTcDZ5ckVjWllwXzlNV0k1dGlwOTRCbE1RVWxmRFE?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AAPL** | **39.43** | **45.91** | **30.23** | **11.70** | **5,145,409,617,920.00 USD** | **28.77** |
| MSFT | 25.89 | 7.83 | 18.25 | 18.80 | 3,684,357,898,240.00 USD | 5.54 |
| GOOGL | 14.57 | 5.20 | 17.97 | 24.70 | 3,430,640,517,120.00 USD | -12.18 |
| SONY | 20.74 | 3.00 | 0.30 | 10.30 | 161,967,177,728.00 USD | -4.21 |

Peers fetched as_of: 2026-11-24; AAPL reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-01-28 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 62,900,000,000.00 USD; period 2018-07-01/2018-09-29; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 29,789,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/320193/000032019326000026/aapl-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilAFBVV95cUxPcW1UV2NiYVZ2ZmxTbDc1dVoxblRuVWpUSlFHdWlaRXhzMmFUWFoxRHY2c2hMTEFyNmdrbUwwTHU0YUswM1VDMF9XZGVpbUhEaHRhSEwzdXZxaFFVVlNUWEJhNU5MTXRvY2tVd1FVbldtX0JfYUlyRG94MTh6WnEyWHF6Nl9mRkszMGJ4SW5mOWZDOTBK?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOXy02WGZ5d1JKRjdEUFlEZm92TmEwYy1Kd2F6X0lobUIyd0sxSFJrNlhGR3hOMkxma2ZpQmQ0V3RaUXVnUFNGR3dLc3RzTHFCcEJOaXNsRlVCS2dxZWVwOWExbUFiQi1pYnFuNGZlTzExLWZmNXd2WlJHWkV4WWdtLUFleE5iWTdMeW9wb1d5RTBjbHRXblhqVDY5WkpTUQ?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPSUhjckIzQThzNXJUVXhqNzRLVUp1eEhsY1p2VDVNTGhOblRmOFJxXzRKV09wZkFhbmF1U3JIaEsxclB4Y0Fwc0RiajhCMGJDanpSbEVZdGg1SlhaNy1VNGxaTWJKU1RnUmdPSFMxdkxSYkFXb2F3azV3TGdlVVhDT1pmQldxVklzTXJiR3E2bVppNkQzeVE?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPLTlCTmhMLXRPNjhlZnU1Q2Z0V3VwR3FTR0haUlBObWNOWjdWM3luWnhwWWNfNnhxVXlrT1kwMlVpdEYySEFMMkxTbi1sR0Nza19XS2tQUjFkWHQ4V3dzT1VIQTFyVzRPU2RZd2Q1N2hENkxuN09TU3llRWRjMVZCZGNlbzFOXzBJbDZ0QXlQbHZfLUoybUl3N2VDQlU?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQZTAzU2dvbVdZTzN2Smttc1pjc3lsSW5qWTdldDFETUFxNmx4Y2Z1RkZSNG5EcXR0bFlueDdLY2Y4cWxfdGxiYktmeWVDODhnclQ5eEpWZVZRVHlJZjhkalNMVlk1UUpKaW9IS3NRN3RVcnF1MHhEbnVaZWdQaThJRjdud3VSSGkxREdfWHVTelZxSGdXTXc?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxNV0MyNHFRQXdJLXFlX0p2SGxBYnJvM3hueDNPV1Vha0tTZzhIbUNldnJPZUN6cUxHa2hnN29QbldsMWtMTlVYSVVHczkzNGM1Q1pWN1FaQXNTeDZ2TVNlckIxR3gyTDJJNzA2Skd4czNJZGFFaGNGRUdDdlczR3pGTk5XUi11dFM1bUJ6U1RvM1hSVm9mMHhQNWdURDctSzg5VjRvS001dXQwM3hjSjY3S3h0OEpldw?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxNZ1BZMldHMWlfNG43bmhLQkhHMnl4alBvQWU5UTltVlNHNVk0dHFFOVFwbUVlbkllYlBKNGJ3NVN2T05ic0RRLVZPTnBYekY1NHNqek11NFJteHVBSW1OcGNad0JKVGwzRFpGRWp6ejZsMDJFT1JzdndBTFF6R1ViVS1uLTR2d1I1ajU4bVFlSTFwRUM1cFhNUVhldzdiQllGYldJNkZ3dTF2MUdyOWJidU1fTF90bVhtQzRYLUpMT2tQWm8w?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxOcm1CLVpuU1QzUk9GQ3EwU1lvc3F3QjZPaUZLdllnY2p3eUFiU0Q5ZnN6VEU4OWh1RXdUR3BvTjFqZS00WkVBTzNIQ1BuYURXVzN0OUN4OUc0em92NFlTN1pQUW5IODBUQms0ei04MlZSUm54SnNGMEUwUGdnbjlseEZXX0FZaFZpOUV2MmV3dW9LVUgteVhpbzd1OElLdm9tQmxaMUNVNlk1SVRlcHRkaUJoVVh3SXowOWx6Xw?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxPa0E0Rzk0Nl9rejYyMU83aFc1YmNVZ0Y1UjlBN1JBTV9pSEY3cVZ5bW1iRmZOSGNrNU91dHBhTEU5S2hHdEZ0cllLNnc1Vk4tRGJWOE5TNHU1ajExUlJWVkhKU01odkVJd0lza0JzRlpxWHp3dVdzZVJsUHJUNVJfd3oxNWlOZktfVWhhNjJOS2VwWHZKQmZnZHBmVFBuZDdEMWtlQmdyWEJrMW45MHY5YU13MA?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxQd2R0dnZub2w2YVV1Ri1YRXBUdTRGMC02dVphM1F0R2Jtajh1SzlIMXBaQTFvNHZBNzJQeklrbEIwZDRPSnNTUE02Q0lPZjVrTVc1SmRDQjM3NDZKRkExUS1RUkhNQzc5Wk82ZGVSZF9lSnZWNXpkbExEQXJXMTJDa2s1aThidzdCdkZZSXh6M293THViTlQxTEJnSk1jVzNncHp4YmdvLUlIeGktLTBHSW5kU0p5NzJveV9r?oc=5
- https://news.google.com/rss/articles/CBMi-AFBVV95cUxNRXVwb1laS1Btbm1iTjFsMEg3OGRxd2I4MDBheXBhTmpLTnBpLVpFaGZCdmVabEZnS3FWREh5WDAxcW1KVGpOVFB5NzltWnAyakRibjhhckdQM3BpcVRtSTdHckRoY2RtRFdmZG82T3NlY0xkLS1MczU4b29KQXFXVGdXSjNHMUxBT0NoZmRSb0tuYTdCOEZYWWhGRW8xbUVOTlhkZjJFVGhOUEVaQVptUW05eW1UalZBeG9wRUhLVXljWlVFU0JLc0dkVm1aZjM5OHJEWlVuUmFUd1FJNW1Rdi1UdDN5YlRER0JMZnVpaGNvSVUyRUx5ZA?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQekFPM3ZncUc5OWU5R3NERDJHalhFbE9WNURJNUNmc3RnelpCTW9OcHNHcXZuTDMxVGtMbWkwUnM3WDBCSHVYalU4dnhzWFY4NW10dGJROGVEOE5KNXNIUjJUY1ltN1A3SHJTZE9XS0ZUQTNUT0c5S1BVUzJGRDlzVlVuZkV4YUNNTHFxZVhmai05QUcwdmc?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxQbWg0cFB4Vk41bk5zYng3OXJzQ1VkTHVDVzJlZXBsRGhBUExzX2tuSHBvdFUycHc4d2gxcUMtenhQUGFLYjhEOHRqMTdoNG9rdzllQWxMd09TOEJzTDgwSWdtbTFiMWRWQVZsb29yS0dtWVdQdFVlampkQTkzaml5emJHcFBoZy1OcngyOHNfZzFmQQ?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxNUFRwY3ViWDBsZy1aMUMzUkIzdjV1bDFSdkdFM0VYR3dTTVZzbm5RYzVZbXhxZVltQ2VCM2NZU2lCaHFBcUV3SDA1TTd3XzFSYWZfeUhqTDRVNldpVnM5VGx6Y0FicUI0NG1FaG15aldRNTZoVE9hTG5RQjlESnV4Z09PaFpPWHplOXEyVEljcjg3ZFpDb25ieFQtYk4wYUNiSnpUN3ZOUQ?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNaG1BZDFsdExZcmFBTHcwYkZGMElvdlhwMk1kRVl0RUlOTk90REhiRVJubWI0RlFqVWYyYWYxTUk1UjVkZzFtZGNyMXd6U0FuT0FTY2pPSDlVN3JCODFrSTFjZjEzSFY5TlhoenhTcDZ5ckVjWllwXzlNV0k1dGlwOTRCbE1RVWxmRFE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
