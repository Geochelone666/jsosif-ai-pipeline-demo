# NFLX Intelligence Report

- ticker: **NFLX**
- Report as_of: **2026-11-03**
- Market data as_of: **2026-11-03**
- Quant sources: https://finance.yahoo.com/quote/NFLX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NFLX/key-statistics/
- AI analysis snapshot as_of: **2026-11-03**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-04T05:04:41.352845+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 4, 'ai': 10, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **12** exact headline/source/date matches; prior report **20261103T051441Z-8b1c85d8/NFLX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **7**; {'directional_claim_without_event_type': 3, 'low_uncalibrated_model_confidence': 4}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 10 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 26.09%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 63.4200 |
| Return 1D (%) | 1.7324 |
| Return 1W (%) | 1.4395 |
| Return 1M (%) | -5.4280 |
| Return YTD (%) | -32.3592 |
| Return 1Y (%) | -42.3502 |
| Annualized volatility (%) | 35.8137 |
| Beta vs SPY | 0.1923 |
| Max drawdown (%) | -46.4449 |
| Sharpe (rf=0) | -1.3646 |
| Downside deviation (rf=0, %) | 26.3882 |
| Sortino (rf=0) | -1.8521 |
| Historical VaR 95% (1D, %) | 3.5133 |
| Historical ES 95% (1D, %) | 5.1308 |
| Correlation vs SPY | 0.0687 |
| Tracking error vs SPY (%) | 37.1943 |
| P/E (trailing) | 18.02 |
| P/B | 8.89 |
| EV/EBITDA | 16.90 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 16.82 |
| Gross margin (%) | 50.69 |
| Operating margin (%) | 34.63 |
| Return on equity (%) | 53.46 |
| Free cash flow yield (%) | 9.65 |
| MA50 | 71.9958 |
| Close vs MA50 (%) | -11.9115 |
| MA200 | 81.3449 |
| Close vs MA200 (%) | -22.0357 |
| RSI (14, Wilder) | 36.5593 |
| MACD (12,26) | -2.6489 |
| MACD signal (9) | -2.3712 |
| MACD histogram | -0.2778 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NFLX': 274, 'SPY': 274}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 63.4200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.7324 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.4395 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -5.4280 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -32.3592 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -42.3502 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 35.8137 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.3882 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.8521 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.5133 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1308 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0687 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.1943 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.1923 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -46.4449 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.3646 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.8163 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.6850 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 34.6320 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 53.4630 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 9.6471 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.0170 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 36.5593 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.2778 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -11.9115 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -22.0357 -> Clearly below the moving-average trend level.

## TAILWINDS

### Netflix(NFLX) Stock Options Chain | Quotes & News
- Summary: Provides options data, no direct event impact.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMi-wJBVV95cUxQWHdXaEZ4N1luTTYtS1J5cVpWbExEMWtOWi1vbXNFRVFLTU5TSDIzZWJkQVlfclg2N0FsUDdNaFl4aG9IRWI2dThKRm4wRzJsSGszY29zMjR0R3NCdEJwbVlqOTZmWEJDUVFfeXREcG10dVNxaDZBTGNsWmFmSUZqdUdhVlFLNjdfWWo2bUJscm5henljWGJHSkg2N0xNanBhY3JqRTFlRkE5dzB2eW9JSmFKbF9yX2oxUEFTLXRBcWtoaXlCODNvS2dUTUFKbG5QcXFYZXY0RFpCb1dnR2ViVmt2bzJWelJfUlVRQ2o3bWpjVDlPeWk0d2R5b3JWdTFnUGNCekttT1pkMDNKT29sdEphc0dWRDRpbjF5UUJBTnYyMS11ekRtLWJxOUFEZDlmeDVDbkYwNnFHbmk1ckZwZWR1TFJjUHRQajIyVUo3M3JVN0F2a3YzYUdpNmg3X2RaeDFkeFFHNXlMRHRQb1RIY1dzR1oybjBQUHlr?oc=5>

### How Much Should One Number Worry Netflix Stock Holders?
- Summary: Analytical focus on valuation metric, no event.
- Date: 2026-11-01 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxQVllxOXphY0ZBQ19kR1h0aFpjU0VDenQ2SktFanRqX25FNThHc1F1d2Rob0laOHhFamZlLVFmLTEwTThLY1p0OWRld0hkWmd2OUFmc1VQeFZmMDdQNVJ1RmZ4YVRxdndnTWh6akxHZThuT2YwT0VHaTdrOExCVEs5b09Ud2piWmhuZFRVY2x1RjA2a1BSUkhrclRaeTFzS0VheHY2YzNGWUk5WHE0OTVHMTRKZ1BfUQ?oc=5>

### Netflix Stock Is Trading at a Historically Low Valuation. Is This a Generational Buying Opportunity?
- Summary: Highlights low valuation, potential buying signal.
- Date: 2026-11-01 | Impact: medium | Horizon: medium | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxPQ1lRWWc3cEFBTEVxNzlnRHUyYnVvdGV6MElkWmpmUGI2M1NSclZZQ291RDd5ZEdsZE5uMVhpMWxtclJYY0dSNGZ4cExGWWpvel9kUDc4QWVPR2xuWjNyQi1fWmNRZ0NGaG9xTHlNdVhxZ3otM1ZDRGpTV1c3bE05ck9zYnpDZ2N2b2MwdDNyVUhYLXRkb25DNzFiM2lXX1dvdjh5Nm43OXBMdHM0WUNHU2h5RDcwSzdEMW9BZlo4ZnhhWHZSVWxYY21PQjJoZmt4cWlDalEyQ3U?oc=5>

### The Battle That May Matter Most for Netflix Stock Isn't Against Disney
- Summary: Explores other competitors impacting Netflix stock beyond Disney.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNMEJjQl9vSl9kWk5nemlNQW5QangydndZUU9JRW52bjhwZ1ozX0Fnd0xhc21iUjBfNXNUV0VibVVUaHpmeFpWLVBEcHlpMXFkbXFZSzBBUzd1OV93a091XzVxdjQ0bDNyV0dYTFVaMmJuektoVmM3Z21XQW9aZUVxRVpPemFIaU5NdGZDX2tJY2pUYnRHRmY0?oc=5>

### Netflix Should Never Say Never To Reinventing Itself (NASDAQ:NFLX)
- Summary: Netflix emphasizes continuous reinvention, highlighting strategic product innovation and long-term growth prospects.
- Date: 2026-10-30 | Impact: medium | Horizon: long | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQY25aRjVOYlpTOUFjenBCbW8wQ1BEMU55SFZ2dlkwaUVydjBWOFdDREFzelhBeTBpanN3ZUgzUTdLWFRtamNYZDQxOGFacFlkeTZ1ak5KX2FWMGc4NXBEeGZIYkxKTVNBOC0xU0JFR09FT0NiV2xMc2xQVGFHQmFpdzBKSTJXdkl4Yk9PQzlCVVZXaWtFUHJRUw?oc=5>

### What Should Netflix Stock Investors Be Watching Now?
- Summary: Provides current factors investors should monitor for Netflix stock performance.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQUHJTT2tVYjBfMGpTdlVzaE1DWlF4NHdNOFZpeENYcjB0OEw4QzlPSF84Q3hGYy1EQVFmZHp6V0l1N2J3SUNHNTdMb0RMS3FTMUFYV1EzWGZxTmtTM2lUYmVHLWp6Q3lMZU9sQ0FMVEJGaHNGOTVSb2pnWDlQRnJvSXBMSl93SWxmWVlENklwbmlHcEcxdWpnNGx1VkJNdkxVSlE4bm9yd0dxYlVTVmNUSWpR?oc=5>

## HEADWINDS

### How Investors May Respond To Netflix (NFLX) Lower Ad Revenue Guidance
- Summary: Lower ad revenue guidance may hurt investor sentiment.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNTmpuUm0tQldPM0g2UUNrdFpYUHVvZ05XM3JUVTVzYTVQV3JwSFJWRFM5aU14dlRGbDFHWUhaNDNsWXc4ZEl2RVVtcXRLN29wMU1xRXJGQWVQemU1MkZYMmRDVXFkMjgwR0txQkpza0phNXZFbWlCbzJNZ0VNek1sRmFiczNjVEF2UEFhcTV1ZW1sRDNwWHBBdG5qTE9Fc2Z5?oc=5>

## CATALYSTS

### Netflix Unveils ‘AI Discover’ To Take The Guesswork Out Of Streaming TV
- Summary: Netflix Unveils ‘AI Discover’ To Take The Guesswork Out Of Streaming TV
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPVmFCMjkxWERhcDluVjRRWGIyOTkzR3RSNXNHSGsxRGhZa1FoY1BDcEdkQXBOVER6WXIxcjJjYnBDOTBNemJOak9kNDBzV29CaDBLX2hPN19BUzJSQTJMU0taNzdzZE1QUUJQVkpGWHBPUE5QWm05NTl6eld4Zm5qaVVCVEs4Q2UxR0pSdUVZWDdGZGFwV2ZPc1djNWRNRVRfUnc0cEF6MXhaSHJjRnA2SzVSNUZXTlBsWlJsWkRBTEp4enZ3aW9Ed3NB?oc=5>

### Netflix's U.S. Audience Engagement Problem Is Hurting The Stock (Rating Downgrade)
- Summary: Netflix's U.S. Audience Engagement Problem Is Hurting The Stock (Rating Downgrade)
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOY3JYbDhETktQMDhGRklxQl8wM3d0YkFPdGpia3dkaFlXdUxlczVzVlFBTlVVTkRUSWw4MF9PbHZyazd5bE9EejVzR2ZBVmowNTZ2dWZuMDZ5aGhZQ3IxS3VkMmg0TFBDSFAyQ0R3OGxIMklaLV9xUEdLZGY4Q0VxTWFsal80OUZuQjRXSUZ0QUNxR2x1aTgwcVhGUnlKY1RoblJkZGZuNjlIVHZtWkpsd3ZzYWFiSUZ1RlE?oc=5>

### Netflix's Problem Isn't Profits. It's Viewing Time.
- Summary: Netflix's Problem Isn't Profits. It's Viewing Time.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOVGhjVDQ3VGtkNk1paC1uSjIwOUYweC1FRmI3YTlHU1JpaXBsTzN5UkhsYkQ2eXVKRUdTX0JnSHNPWk1PeGVfYVJRQjZTLXB3ejR1TEhiS19BX0NzV1VNSk95OTRkV3hXZHpTdFM4V2pQQTl1aXFYUlJyeldDQWYxTk5NMndJaGROdGRVeks4WVJTeDQ?oc=5>

### Netflix, Inc. $NFLX Stock Sold by International Assets Investment Management LLC
- Summary: Netflix, Inc. $NFLX Stock Sold by International Assets Investment Management LLC
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxOVFc2eFFtOHhZaU5FZ2xCX2xYUTlLRzI1aUVOc2dLZ0JfUWZKN2ZuNHV5TUd1bC1OZUZ5OEFnUHdyeGNXR3J3Rzc0TVNZTmtrVVgyMFAzOVluNVkyZmJXdlNKc21JMUxPQkR1dzF4TjVzVXNrdHVFa1VIaDdqWDZGcjFpYXlUQnlKTnVFQkdzUjlBLWlQUTdWY0syTmJZMzB4eGFiS19EWThsTXRsekNDakYyN09TVXlyRWZ6d3FNb3lFd1czWm13dmZLSUItMzdrbHA4RA?oc=5>

### Netflix Spent $4.8 Billion Buying Back Stock in 1 Quarter. Here's What That Tells You.
- Summary: Netflix repurchased $4.8B of shares this quarter, signaling confidence and potentially boosting EPS per share.
- Date: 2026-10-30 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQUjViaXJMRjdUcktWc0Y0bWRGX2ViaHA4UXhJcTREbks0LUZjcGNYSzNqZl9CTHZEd3kwLUFhZFNhcDNwaVYtVnJ3cUltT1p4NkZNcTdrSE1oZVpZQzVLZHpySjdCYTV4QXVJdXhFcW9LWU1MUC0zcDl2RVp2QUwxb3liRDVWRVd4WHFFZWZwLV9RVzlx?oc=5>

### Netflix, Inc. (NFLX) Stock Forecasts
- Summary: Predictions for future performance of Netflix shares.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxOeFN4ZjN0Q0RPX3AxYTVZemJxVHhNemRHWDBhdWhRSXdzRklENkdic24yUloyQjNONFhobWgxb0F6R1N5ZGp3RW52SWRHWjE2RW5tRE5qOTBCYlVXZ3VoY2pQQ1lpaFp0V1c0bXpXcXlicEhVdjBWeGNBaTkweDBWWG1Tb1k1WDBXU29kLWtn?oc=5>

## RISKS

### Is Netflix (NFLX) A Bargain After Its 2026 Guidance Reset?
- Summary: Investors question if Netflix remains a bargain following its 2026 guidance reset, suggesting possible long-term downside risk.
- Date: 2026-10-30 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQYXFIRXR2UFNyNHdHZFVwM0FwMVQtdVhKRU1VTWljeTQ2Rm1qYVVWeERlaklHVklBU0pyNjRaUWZGYXVhOGJMZ0h5TmRpVERTTDVoZkJ3eW5OenNfcVhnUEhLLVBNY0VqSGdVRlZMS2FwWlgweUcwckJ3ZmYwc2dJb3lScWI2VFdKNmc3aGdpUGJFdTVVZFpIaW9qR3ZGSmN0?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NFLX** | **18.02** | **8.89** | **16.90** | **11.80** | **264,077,033,472.00 USD** | **-42.35** |
| DIS | 23.54 | 1.80 | 11.68 | 6.80 | 197,153,112,064.00 USD | 3.31 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| CMCSA | 7.56 | 0.91 | 4.89 | -6.10 | 84,052,320,256.00 USD | -1.38 |

Peers fetched as_of: 2026-11-03; NFLX reuses existing data (market data as_of: 2026-11-03); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-19 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 12,874,176,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,663,927,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi-wJBVV95cUxQWHdXaEZ4N1luTTYtS1J5cVpWbExEMWtOWi1vbXNFRVFLTU5TSDIzZWJkQVlfclg2N0FsUDdNaFl4aG9IRWI2dThKRm4wRzJsSGszY29zMjR0R3NCdEJwbVlqOTZmWEJDUVFfeXREcG10dVNxaDZBTGNsWmFmSUZqdUdhVlFLNjdfWWo2bUJscm5henljWGJHSkg2N0xNanBhY3JqRTFlRkE5dzB2eW9JSmFKbF9yX2oxUEFTLXRBcWtoaXlCODNvS2dUTUFKbG5QcXFYZXY0RFpCb1dnR2ViVmt2bzJWelJfUlVRQ2o3bWpjVDlPeWk0d2R5b3JWdTFnUGNCekttT1pkMDNKT29sdEphc0dWRDRpbjF5UUJBTnYyMS11ekRtLWJxOUFEZDlmeDVDbkYwNnFHbmk1ckZwZWR1TFJjUHRQajIyVUo3M3JVN0F2a3YzYUdpNmg3X2RaeDFkeFFHNXlMRHRQb1RIY1dzR1oybjBQUHlr?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQVllxOXphY0ZBQ19kR1h0aFpjU0VDenQ2SktFanRqX25FNThHc1F1d2Rob0laOHhFamZlLVFmLTEwTThLY1p0OWRld0hkWmd2OUFmc1VQeFZmMDdQNVJ1RmZ4YVRxdndnTWh6akxHZThuT2YwT0VHaTdrOExCVEs5b09Ud2piWmhuZFRVY2x1RjA2a1BSUkhrclRaeTFzS0VheHY2YzNGWUk5WHE0OTVHMTRKZ1BfUQ?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxPQ1lRWWc3cEFBTEVxNzlnRHUyYnVvdGV6MElkWmpmUGI2M1NSclZZQ291RDd5ZEdsZE5uMVhpMWxtclJYY0dSNGZ4cExGWWpvel9kUDc4QWVPR2xuWjNyQi1fWmNRZ0NGaG9xTHlNdVhxZ3otM1ZDRGpTV1c3bE05ck9zYnpDZ2N2b2MwdDNyVUhYLXRkb25DNzFiM2lXX1dvdjh5Nm43OXBMdHM0WUNHU2h5RDcwSzdEMW9BZlo4ZnhhWHZSVWxYY21PQjJoZmt4cWlDalEyQ3U?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNMEJjQl9vSl9kWk5nemlNQW5QangydndZUU9JRW52bjhwZ1ozX0Fnd0xhc21iUjBfNXNUV0VibVVUaHpmeFpWLVBEcHlpMXFkbXFZSzBBUzd1OV93a091XzVxdjQ0bDNyV0dYTFVaMmJuektoVmM3Z21XQW9aZUVxRVpPemFIaU5NdGZDX2tJY2pUYnRHRmY0?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQY25aRjVOYlpTOUFjenBCbW8wQ1BEMU55SFZ2dlkwaUVydjBWOFdDREFzelhBeTBpanN3ZUgzUTdLWFRtamNYZDQxOGFacFlkeTZ1ak5KX2FWMGc4NXBEeGZIYkxKTVNBOC0xU0JFR09FT0NiV2xMc2xQVGFHQmFpdzBKSTJXdkl4Yk9PQzlCVVZXaWtFUHJRUw?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQUHJTT2tVYjBfMGpTdlVzaE1DWlF4NHdNOFZpeENYcjB0OEw4QzlPSF84Q3hGYy1EQVFmZHp6V0l1N2J3SUNHNTdMb0RMS3FTMUFYV1EzWGZxTmtTM2lUYmVHLWp6Q3lMZU9sQ0FMVEJGaHNGOTVSb2pnWDlQRnJvSXBMSl93SWxmWVlENklwbmlHcEcxdWpnNGx1VkJNdkxVSlE4bm9yd0dxYlVTVmNUSWpR?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNTmpuUm0tQldPM0g2UUNrdFpYUHVvZ05XM3JUVTVzYTVQV3JwSFJWRFM5aU14dlRGbDFHWUhaNDNsWXc4ZEl2RVVtcXRLN29wMU1xRXJGQWVQemU1MkZYMmRDVXFkMjgwR0txQkpza0phNXZFbWlCbzJNZ0VNek1sRmFiczNjVEF2UEFhcTV1ZW1sRDNwWHBBdG5qTE9Fc2Z5?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPVmFCMjkxWERhcDluVjRRWGIyOTkzR3RSNXNHSGsxRGhZa1FoY1BDcEdkQXBOVER6WXIxcjJjYnBDOTBNemJOak9kNDBzV29CaDBLX2hPN19BUzJSQTJMU0taNzdzZE1QUUJQVkpGWHBPUE5QWm05NTl6eld4Zm5qaVVCVEs4Q2UxR0pSdUVZWDdGZGFwV2ZPc1djNWRNRVRfUnc0cEF6MXhaSHJjRnA2SzVSNUZXTlBsWlJsWkRBTEp4enZ3aW9Ed3NB?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOY3JYbDhETktQMDhGRklxQl8wM3d0YkFPdGpia3dkaFlXdUxlczVzVlFBTlVVTkRUSWw4MF9PbHZyazd5bE9EejVzR2ZBVmowNTZ2dWZuMDZ5aGhZQ3IxS3VkMmg0TFBDSFAyQ0R3OGxIMklaLV9xUEdLZGY4Q0VxTWFsal80OUZuQjRXSUZ0QUNxR2x1aTgwcVhGUnlKY1RoblJkZGZuNjlIVHZtWkpsd3ZzYWFiSUZ1RlE?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOVGhjVDQ3VGtkNk1paC1uSjIwOUYweC1FRmI3YTlHU1JpaXBsTzN5UkhsYkQ2eXVKRUdTX0JnSHNPWk1PeGVfYVJRQjZTLXB3ejR1TEhiS19BX0NzV1VNSk95OTRkV3hXZHpTdFM4V2pQQTl1aXFYUlJyeldDQWYxTk5NMndJaGROdGRVeks4WVJTeDQ?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxOVFc2eFFtOHhZaU5FZ2xCX2xYUTlLRzI1aUVOc2dLZ0JfUWZKN2ZuNHV5TUd1bC1OZUZ5OEFnUHdyeGNXR3J3Rzc0TVNZTmtrVVgyMFAzOVluNVkyZmJXdlNKc21JMUxPQkR1dzF4TjVzVXNrdHVFa1VIaDdqWDZGcjFpYXlUQnlKTnVFQkdzUjlBLWlQUTdWY0syTmJZMzB4eGFiS19EWThsTXRsekNDakYyN09TVXlyRWZ6d3FNb3lFd1czWm13dmZLSUItMzdrbHA4RA?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQUjViaXJMRjdUcktWc0Y0bWRGX2ViaHA4UXhJcTREbks0LUZjcGNYSzNqZl9CTHZEd3kwLUFhZFNhcDNwaVYtVnJ3cUltT1p4NkZNcTdrSE1oZVpZQzVLZHpySjdCYTV4QXVJdXhFcW9LWU1MUC0zcDl2RVp2QUwxb3liRDVWRVd4WHFFZWZwLV9RVzlx?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQYl9JU3pGS0dHajliUkF3NzdSc0ZGWHFsdUVjbVc5VGZvZzhoRVpLQkkySVoxSzE0ZmhOc2tzRG40c18yS0pWdkZCZzlyUWVHMlM4S0pLbTFQUWEwMVJaRXhpOW5HR3NLdnRzRGRyMzJzeFR3NWxKSlBlOTNvWS1FUEVnSHBGSk9kZHNuY3NrV1pmUWY4a0Rr?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxOeFN4ZjN0Q0RPX3AxYTVZemJxVHhNemRHWDBhdWhRSXdzRklENkdic24yUloyQjNONFhobWgxb0F6R1N5ZGp3RW52SWRHWjE2RW5tRE5qOTBCYlVXZ3VoY2pQQ1lpaFp0V1c0bXpXcXlicEhVdjBWeGNBaTkweDBWWG1Tb1k1WDBXU29kLWtn?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQYXFIRXR2UFNyNHdHZFVwM0FwMVQtdVhKRU1VTWljeTQ2Rm1qYVVWeERlaklHVklBU0pyNjRaUWZGYXVhOGJMZ0h5TmRpVERTTDVoZkJ3eW5OenNfcVhnUEhLLVBNY0VqSGdVRlZMS2FwWlgweUcwckJ3ZmYwc2dJb3lScWI2VFdKNmc3aGdpUGJFdTVVZFpIaW9qR3ZGSmN0?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
