# NFLX Intelligence Report

- ticker: **NFLX**
- Report as_of: **2026-11-20**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/NFLX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NFLX/key-statistics/
- AI analysis snapshot as_of: **2026-11-20**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-21T05:34:43.393115+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 4, 'ai': 7, 'unknown': 0, 'irrelevant': 13})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **14** exact headline/source/date matches; prior report **20261120T053808Z-e360129e/NFLX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **4**; {'directional_claim_without_event_type': 2, 'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 11 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 56.7300 |
| Return 1D (%) | -2.9593 |
| Return 1W (%) | -8.7208 |
| Return 1M (%) | -17.4116 |
| Return YTD (%) | -39.4945 |
| Return 1Y (%) | -46.3140 |
| Annualized volatility (%) | 35.8881 |
| Beta vs SPY | 0.3139 |
| Max drawdown (%) | -48.1207 |
| Sharpe (rf=0) | -1.5600 |
| Downside deviation (rf=0, %) | 26.4207 |
| Sortino (rf=0) | -2.1191 |
| Historical VaR 95% (1D, %) | 3.3880 |
| Historical ES 95% (1D, %) | 5.0633 |
| Correlation vs SPY | 0.1250 |
| Tracking error vs SPY (%) | 36.9327 |
| P/E (trailing) | 16.88 |
| P/B | 7.95 |
| EV/EBITDA | 15.18 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 15.04 |
| Gross margin (%) | 50.69 |
| Operating margin (%) | 31.30 |
| Return on equity (%) | 53.46 |
| Free cash flow yield (%) | 10.94 |
| MA50 | 67.4042 |
| Close vs MA50 (%) | -15.8361 |
| MA200 | 79.9389 |
| Close vs MA200 (%) | -29.0333 |
| RSI (14, Wilder) | 27.4878 |
| MACD (12,26) | -2.5065 |
| MACD signal (9) | -2.1386 |
| MACD histogram | -0.3680 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NFLX': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 56.7300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.9593 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -8.7208 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -17.4116 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -39.4945 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -46.3140 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 35.8881 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.4207 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -2.1191 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.3880 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.0633 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1250 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 36.9327 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3139 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -48.1207 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.5600 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.0424 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.6850 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 31.2960 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 53.4630 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 10.9361 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 16.8839 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 27.4878 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.3680 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -15.8361 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -29.0333 -> Clearly below the moving-average trend level.

## TAILWINDS

### NFLX Stock Edges Higher Overnight: Evercore Swaps Netflix For Spotify On Top Picks List
- Summary: NFLX Stock Edges Higher Overnight: Evercore Swaps Netflix For Spotify On Top Picks List
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQQ3VZcm5lRlRBZE15a3pBMWxZRHBRVlhhYjQwQU9YWEhQYktpdWNkTngyN3R6VkZQaEZTMEp1OHZLQTJCbml1eElwSDljampSQ3RDMWx4MVZYUjNKRlRqdFpRWTVtU2NNeDYtWDdoenRyaHlOWV9aYlBTYUVHUlRRWTFIUjZST2k0U2ZVSlFIN3NGbk00Vjd4eVByNVFfT00?oc=5>

### Netflix Stock Hasn't Been This Cheap in Over 2 Years. Is Now the Time to Buy?
- Summary: Low valuation suggests buying opportunity.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxQcHU2SGUwcTA0R2doTDRkZVp5X0w0U2w4d0FGand1OEx5M0tLeWZvRUYxd2NmZEg5V09OVGVuOWk3TXJuV1RuNFFXTDBIOTRBVENnM04wRTZkUk53VWNONmlTN3ByQXI1YThtMEIwRDE4MjdGaFZvX1MxUWU1alNIdWZCQXNjLS1Sd2NTYUJUUjN4TlBYOWVXem1YaGVUU0k1bjJaWDJ6MUVuYWVTaGJvYko3QzgxWkpMRHc?oc=5>

## HEADWINDS

### Netflix Stock Is Down 36% and Wall Street Keeps Downgrading It. History Says That's a Mistake.
- Summary: Netflix Stock Is Down 36% and Wall Street Keeps Downgrading It. History Says That's a Mistake.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOazJVaF9Sd3Q3TnBVTEMxU3VTbGtvUjVKUkR1U2dXTlFiRFh4cldtdDRzaUd0elVPQkdlbi01NUR1NHNaNFVydWYzcmlhSllrek85d3ZsNnFTeGdPWi1nekR3ZUVNRXJKSjlZLWo5Q050OWZUYW5ZQ1pfS1V1Z3lBemdFQ2dlR3g2c0JwYUlRanNldl9rRGc?oc=5>

### Netflix (NASDAQ:NFLX) Stock Today: Unusual Volume as Shares Move Lower
- Summary: Netflix (NASDAQ:NFLX) Stock Today: Unusual Volume as Shares Move Lower
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQUi1Da2Rza2JhSjRLZ2ZNTXQ4QWdGcXJfU0FrV19JREUyZk44MVFqcDhtLVlIeDJ4cWttNnVWelBUTk9pYmhIU0E1c29HVy1xQkE3ZkF0RG5sanVES1VPVDNkWGxsU0d6OGlDajdhaGJ1a0VHZDZ4OUNScDdycUM2R1ZzQndGcVM4Qy1nT0llekdWM1hOWUFEUmxyQ1Q5alpCb0hN?oc=5>

### Netflix (NASDAQ:NFLX) Stock Falls 3% - What's Next?
- Summary: Netflix (NASDAQ:NFLX) Stock Falls 3% - What's Next?
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPMjBGVnNIRlctUklaR2JUdEpmVlI3VUVQU2NJRXJsZTgxVGJoSVFxTGxUYjdqVU1UREJzR29Uc1lvQ1BOeEZ3NGpiSE1BR0hqMXNSelROYXJBb1g1M2ZjOEJYVzBfVTNfT3RQcVQ0cHduQUlYV0lnRDliY2U5UExzWUxHaXZ4T2R3dFVGSjVqRURuZVNxaUt6a0l5Q25oUndBZmJJM0ZPaw?oc=5>

### As Netflix Stock Hovers Near Its 52-Week Low, Analyst Sentiment Remains Mixed. Here's Why.
- Summary: Mixed analyst sentiment amid low price.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxQSklFZERTbzBCd0dwSGJ2aVFsWnljWnJIWTJnVTA4TlJ4ckx1ODlFV2hUeHBnaE5nZWdBdnlQcnFKT252dmFYNWtXV2hVYkNGd1hvNF9OYVV6dHBZUzlXMTd5OVZ2bXR5MEZfZVQwbE45R3dpY1ZFaF9JWF92YVB1OVd0aHRKalk0Z0t5RkEySjVGNGpVSHdkcFEwTjI3cGRBUk9TRzB3YVJyWlA4U2VDMllvQXl1UXZibjB0dXdHOE9uemFWcmRZTDBMMA?oc=5>

### Netflix (NFLX) Down 8% Since Last Earnings Report: Can It Rebound?
- Summary: Recent earnings underperformance causing decline.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxONUloejNrRDQ0bVZldllmOFlsVDM3dnp6ektqVDdXcU8taHduYjRuXzVhdi10T1B6VmVUcG93WDhrUEIzejdMT284a2lzbDZWYnctTFJHQXJfeGoxWXAwTFIwNmlRRU14aFMta3M1c1kxWUtfUzNrVE5TV1hNN3hZXzgtdmtqa1doZW5BR0pEaUR4VUZB?oc=5>

## CATALYSTS

### Can Netflix Stock Fall 50%?
- Summary: Questions potential 50% decline in Netflix shares.
- Date: 2026-11-16 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPWW05ekMtcWpHNzBsWDk3ZElHMUtwbW9LR19UWU9DVjRBanZuT21sTjljQlo5b2JJcWhWQ25LTUtzaEVRQjJhTXZfdWl4WU9Gakp4R2E5X3lLcVRTb3l5aXg2cWVHQ1o5cEsyY0lKaE01SVFHeTJSUlV3MXIyT1Y3bjhHRlRlNjYwUnA1UkU5WEFodw?oc=5>

### Netflix Stock Hits New 52-Week Low: Here's What Investors Need to Know
- Summary: Netflix shares reach a new 52-week low, signaling potential downside risk for investors.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxQOUk0TTJyaWQyc1RHT05KNGJzVEhsT05qNWN2V2xtb2NCc2R0czFjbDR1V1hSOTBUcEN2RnYwT25aOWdnQ2xUTnQydmxBV1Juc3RoN0cxSk1mQ08zZWRsdEpVX21INzlpMUtUdHJGTTZiTk9VLUFPVW9BM3pOZW5zMTNUcW1sQ182VEI1UkVfbmtpS25QOExOb2hBZWNRbl9LNlZodXpXRkV2M3N1bkVqOVBBc25hbXBUUnUyOU1rb3VBTmJQMkJkZA?oc=5>

### Netflix is considered the frontrunner to win the 2030 World Cup media rights (NFLX:NASDAQ)
- Summary: Netflix is positioned to secure 2030 World Cup media rights, potentially expanding its sports content portfolio and boosting subscriber growth.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxONUt6c2YwTEJXdjh4UzJCQnZJRlFHRFRveFFkSW8wWExZeWlRVDRmdklsdTA1T3ZaN3BEMXgwemI2b2VIN0dTU3BBbG9lbDN5dFlMcWFaTDdGTUFZR0UxYjdOUzc2R0xOMU9NNVd6SDJONFhUSDZJcVdMY3kxVjB4WmpsS1B2VFRWTmpuNHJHaEk4bEx6TTc4cHhYcUVjalM4QlJYQ1lyUHZuejNJNDNVbmlUbzE?oc=5>

### Netflix (NASDAQ: NFLX) Stock Price Trades At Half Its Historical Multiple As January Guidance Looms Large
- Summary: Upcoming guidance may impact valuation.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5gFBVV95cUxPQ3V0RTMtTk0tSFNZMjMyam5oa19zaGlZcmZWOEE2N09iLVFkMVpLWTg3M2JqNVJxMzMwWWlFOGM1WU00N1c3YUQ3WjMwMWdKN1VTZ0dLNzZ0dkdDa1BoWjZEbDVXclNlVVpiTVBRYUxPZHBSMG9aSnczcTZYUW0zTXRjdEE2aXBzWDdBdUk0OUJ2SDVSODl1WUhnRF9VaXFFVTUxUWNFaVlUY2JqS2E0dUNCVEhnV2M1ckdLeXFEMGdJby1kNVNNcDFZcUtLeDU1U1B5UDZOamVjUXFjelBrUFRRcWRHZw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NFLX** | **16.88** | **7.95** | **15.18** | **11.80** | **232,951,873,536.00 USD** | **-46.31** |
| DIS | 20.96 | 1.83 | 11.07 | 15.50 | 201,513,353,216.00 USD | 16.54 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| CMCSA | 7.85 | 0.96 | 5.02 | -6.10 | 88,420,057,088.00 USD | 5.11 |

Peers fetched as_of: 2026-11-20; NFLX reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-19 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-20

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMinwFBVV95cUxQQ3VZcm5lRlRBZE15a3pBMWxZRHBRVlhhYjQwQU9YWEhQYktpdWNkTngyN3R6VkZQaEZTMEp1OHZLQTJCbml1eElwSDljampSQ3RDMWx4MVZYUjNKRlRqdFpRWTVtU2NNeDYtWDdoenRyaHlOWV9aYlBTYUVHUlRRWTFIUjZST2k0U2ZVSlFIN3NGbk00Vjd4eVByNVFfT00?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxQcHU2SGUwcTA0R2doTDRkZVp5X0w0U2w4d0FGand1OEx5M0tLeWZvRUYxd2NmZEg5V09OVGVuOWk3TXJuV1RuNFFXTDBIOTRBVENnM04wRTZkUk53VWNONmlTN3ByQXI1YThtMEIwRDE4MjdGaFZvX1MxUWU1alNIdWZCQXNjLS1Sd2NTYUJUUjN4TlBYOWVXem1YaGVUU0k1bjJaWDJ6MUVuYWVTaGJvYko3QzgxWkpMRHc?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNeWR3UHpyS2psOTBZaGZHY3hCZm5sVFNkLU5Ob2tfMWUtd1hhZ1A5aGFCaXgtYTE5QV9aWXl6OG9zQ0ZRcW1UZ3BWZTgxbjBGcmhoaExaelJFRlVSbUZ4Vm41eEplWWNveTlJUGZIa2ZUcXVBUjRMUlhSLXVXWFNFakRCeG52TlFFbXVHM2ViQ3dzZjE5ZGJIXzNpTQ?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOazJVaF9Sd3Q3TnBVTEMxU3VTbGtvUjVKUkR1U2dXTlFiRFh4cldtdDRzaUd0elVPQkdlbi01NUR1NHNaNFVydWYzcmlhSllrek85d3ZsNnFTeGdPWi1nekR3ZUVNRXJKSjlZLWo5Q050OWZUYW5ZQ1pfS1V1Z3lBemdFQ2dlR3g2c0JwYUlRanNldl9rRGc?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQUi1Da2Rza2JhSjRLZ2ZNTXQ4QWdGcXJfU0FrV19JREUyZk44MVFqcDhtLVlIeDJ4cWttNnVWelBUTk9pYmhIU0E1c29HVy1xQkE3ZkF0RG5sanVES1VPVDNkWGxsU0d6OGlDajdhaGJ1a0VHZDZ4OUNScDdycUM2R1ZzQndGcVM4Qy1nT0llekdWM1hOWUFEUmxyQ1Q5alpCb0hN?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPMjBGVnNIRlctUklaR2JUdEpmVlI3VUVQU2NJRXJsZTgxVGJoSVFxTGxUYjdqVU1UREJzR29Uc1lvQ1BOeEZ3NGpiSE1BR0hqMXNSelROYXJBb1g1M2ZjOEJYVzBfVTNfT3RQcVQ0cHduQUlYV0lnRDliY2U5UExzWUxHaXZ4T2R3dFVGSjVqRURuZVNxaUt6a0l5Q25oUndBZmJJM0ZPaw?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxQSklFZERTbzBCd0dwSGJ2aVFsWnljWnJIWTJnVTA4TlJ4ckx1ODlFV2hUeHBnaE5nZWdBdnlQcnFKT252dmFYNWtXV2hVYkNGd1hvNF9OYVV6dHBZUzlXMTd5OVZ2bXR5MEZfZVQwbE45R3dpY1ZFaF9JWF92YVB1OVd0aHRKalk0Z0t5RkEySjVGNGpVSHdkcFEwTjI3cGRBUk9TRzB3YVJyWlA4U2VDMllvQXl1UXZibjB0dXdHOE9uemFWcmRZTDBMMA?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxONUloejNrRDQ0bVZldllmOFlsVDM3dnp6ektqVDdXcU8taHduYjRuXzVhdi10T1B6VmVUcG93WDhrUEIzejdMT284a2lzbDZWYnctTFJHQXJfeGoxWXAwTFIwNmlRRU14aFMta3M1c1kxWUtfUzNrVE5TV1hNN3hZXzgtdmtqa1doZW5BR0pEaUR4VUZB?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPWW05ekMtcWpHNzBsWDk3ZElHMUtwbW9LR19UWU9DVjRBanZuT21sTjljQlo5b2JJcWhWQ25LTUtzaEVRQjJhTXZfdWl4WU9Gakp4R2E5X3lLcVRTb3l5aXg2cWVHQ1o5cEsyY0lKaE01SVFHeTJSUlV3MXIyT1Y3bjhHRlRlNjYwUnA1UkU5WEFodw?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxQOUk0TTJyaWQyc1RHT05KNGJzVEhsT05qNWN2V2xtb2NCc2R0czFjbDR1V1hSOTBUcEN2RnYwT25aOWdnQ2xUTnQydmxBV1Juc3RoN0cxSk1mQ08zZWRsdEpVX21INzlpMUtUdHJGTTZiTk9VLUFPVW9BM3pOZW5zMTNUcW1sQ182VEI1UkVfbmtpS25QOExOb2hBZWNRbl9LNlZodXpXRkV2M3N1bkVqOVBBc25hbXBUUnUyOU1rb3VBTmJQMkJkZA?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxONUt6c2YwTEJXdjh4UzJCQnZJRlFHRFRveFFkSW8wWExZeWlRVDRmdklsdTA1T3ZaN3BEMXgwemI2b2VIN0dTU3BBbG9lbDN5dFlMcWFaTDdGTUFZR0UxYjdOUzc2R0xOMU9NNVd6SDJONFhUSDZJcVdMY3kxVjB4WmpsS1B2VFRWTmpuNHJHaEk4bEx6TTc4cHhYcUVjalM4QlJYQ1lyUHZuejNJNDNVbmlUbzE?oc=5
- https://news.google.com/rss/articles/CBMi5gFBVV95cUxPQ3V0RTMtTk0tSFNZMjMyam5oa19zaGlZcmZWOEE2N09iLVFkMVpLWTg3M2JqNVJxMzMwWWlFOGM1WU00N1c3YUQ3WjMwMWdKN1VTZ0dLNzZ0dkdDa1BoWjZEbDVXclNlVVpiTVBRYUxPZHBSMG9aSnczcTZYUW0zTXRjdEE2aXBzWDdBdUk0OUJ2SDVSODl1WUhnRF9VaXFFVTUxUWNFaVlUY2JqS2E0dUNCVEhnV2M1ckdLeXFEMGdJby1kNVNNcDFZcUtLeDU1U1B5UDZOamVjUXFjelBrUFRRcWRHZw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
