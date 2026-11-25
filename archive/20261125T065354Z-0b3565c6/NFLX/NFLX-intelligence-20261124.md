# NFLX Intelligence Report

- ticker: **NFLX**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/NFLX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NFLX/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:17:19.266961+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 2, 'ai': 5, 'unknown': 0, 'irrelevant': 18})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **15** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/NFLX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 12 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 58.8700 |
| Return 1D (%) | 1.3253 |
| Return 1W (%) | -1.3572 |
| Return 1M (%) | -10.5998 |
| Return YTD (%) | -37.2120 |
| Return 1Y (%) | -44.9659 |
| Annualized volatility (%) | 35.8952 |
| Beta vs SPY | 0.3254 |
| Max drawdown (%) | -48.1207 |
| Sharpe (rf=0) | -1.4904 |
| Downside deviation (rf=0, %) | 26.3892 |
| Sortino (rf=0) | -2.0273 |
| Historical VaR 95% (1D, %) | 3.3880 |
| Historical ES 95% (1D, %) | 5.0633 |
| Correlation vs SPY | 0.1355 |
| Tracking error vs SPY (%) | 36.9672 |
| P/E (trailing) | 17.01 |
| P/B | 8.25 |
| EV/EBITDA | 15.73 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 15.62 |
| Gross margin (%) | 50.69 |
| Operating margin (%) | 31.30 |
| Return on equity (%) | 53.46 |
| Free cash flow yield (%) | 10.54 |
| MA50 | 66.5792 |
| Close vs MA50 (%) | -11.5790 |
| MA200 | 79.7054 |
| Close vs MA200 (%) | -26.1406 |
| RSI (14, Wilder) | 36.5938 |
| MACD (12,26) | -2.4921 |
| MACD signal (9) | -2.2750 |
| MACD histogram | -0.2171 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NFLX': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 58.8700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.3253 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.3572 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -10.5998 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -37.2120 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -44.9659 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 35.8952 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.3892 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -2.0273 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.3880 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.0633 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1355 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 36.9672 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3254 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -48.1207 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.4904 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.6177 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.6850 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 31.2960 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 53.4630 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 10.5385 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.0145 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 36.5938 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.2171 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -11.5790 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -26.1406 -> Clearly below the moving-average trend level.

## TAILWINDS

### Netflix Falls Below $60. Bill Ackman Explains Why That’s an Incredible Investment Opportunity.
- Summary: Ackman sees Netflix’s drop below $60 as a buying opportunity.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxQUlJNYzhtcEhGeTRodEZCX1BuYW5Nai1vT19jS2dlRF9DMms0V2E3M2VMTFZfMDY4NldHcXQ5WjBvWDRyVTZGTkxmN0hqekRHSjE1N1RnbUFvYmxrSW5tT3ZtZGw1TGFRYTc4OWhTOHRnc2lBSjFsWThrR0FrVnlUZ1c4OGZHdmlxNUlSS0tSODUyWHNnX1Z6QzU1X0tJU1VMeHpwcGJ6VGZwR2JvV2c3RTJQdU54bFBBRUhTWVFtOGZLRzFzdklZSEo5X2lJZUYzcElz?oc=5>

### Netflix (NASDAQ: NFLX) Stock Price Trades At Half Its Historical Multiple As January Guidance Looms Large
- Summary: Netflix stock trades at half its historical multiple amid upcoming guidance.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5gFBVV95cUxPQ3V0RTMtTk0tSFNZMjMyam5oa19zaGlZcmZWOEE2N09iLVFkMVpLWTg3M2JqNVJxMzMwWWlFOGM1WU00N1c3YUQ3WjMwMWdKN1VTZ0dLNzZ0dkdDa1BoWjZEbDVXclNlVVpiTVBRYUxPZHBSMG9aSnczcTZYUW0zTXRjdEE2aXBzWDdBdUk0OUJ2SDVSODl1WUhnRF9VaXFFVTUxUWNFaVlUY2JqS2E0dUNCVEhnV2M1ckdLeXFEMGdJby1kNVNNcDFZcUtLeDU1U1B5UDZOamVjUXFjelBrUFRRcWRHZw?oc=5>

### With Netflix Stock Down Nearly 46% In The Last Year, Michael Burry Reveals The Price He'd Think About Buying
- Summary: Burry cites a 46% drop as a buying target for Netflix.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxQVW1fa1lPbm00Nmx2VFRXaWR3MnprRGc4Y2ZzNGFKSDcwc2hHUlVaODRKNkxGLUt1Z205aFRtVnBxd0lxRGlzQlFOdmpJQktLbmNMT1Y5T2FhWWNPR3JEY1dtVTRuZ1pJMm5hM2pXLXRENWY5OXotMkhrYXczWHBhdjdZdlZMOExQMG94YzBhSklablhxcXpyeWVsWU9VOHVwQlBheHY0bXNGXzJGaEhEcHA2TUEzRUJwS3VZYW1DaU9zdjVldGZMamVfUzNaSGRyUXVPYThvVUlXSVJNYVZqQmRNbw?oc=5>

## HEADWINDS

### Netflix Stock Is Down 36% and Wall Street Keeps Downgrading It. History Says That's a Mistake.
- Summary: Netflix Stock Is Down 36% and Wall Street Keeps Downgrading It. History Says That's a Mistake.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOR0JLbjlwdTNNb1hNOVc2US1uNDhfdmFSZHdONkJISlJSR3ROYjgyQVNQOEFtZ09DcDAyWkNDSnZfNGsyTndVLTBtSlFlSGUwbExYd19TbFlzOWN5ZDFERjBKNW9wc3lPMEZqc182c0JObUh3a1NIczM3RWJ6OUZRUUQyaUM2OGFPaWliYzhteGdKbjN0QjlVWQ?oc=5>

### Netflix (NASDAQ:NFLX) Stock Today: Unusual Volume as Shares Move Lower
- Summary: Netflix (NASDAQ:NFLX) Stock Today: Unusual Volume as Shares Move Lower
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQUi1Da2Rza2JhSjRLZ2ZNTXQ4QWdGcXJfU0FrV19JREUyZk44MVFqcDhtLVlIeDJ4cWttNnVWelBUTk9pYmhIU0E1c29HVy1xQkE3ZkF0RG5sanVES1VPVDNkWGxsU0d6OGlDajdhaGJ1a0VHZDZ4OUNScDdycUM2R1ZzQndGcVM4Qy1nT0llekdWM1hOWUFEUmxyQ1Q5alpCb0hN?oc=5>

### Netflix (NFLX) Down 8% Since Last Earnings Report: Can It Rebound?
- Summary: Recent earnings underperformance causing decline.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxONUloejNrRDQ0bVZldllmOFlsVDM3dnp6ektqVDdXcU8taHduYjRuXzVhdi10T1B6VmVUcG93WDhrUEIzejdMT284a2lzbDZWYnctTFJHQXJfeGoxWXAwTFIwNmlRRU14aFMta3M1c1kxWUtfUzNrVE5TV1hNN3hZXzgtdmtqa1doZW5BR0pEaUR4VUZB?oc=5>

### As Netflix Stock Hovers Near Its 52-Week Low, Analyst Sentiment Remains Mixed. Here's Why.
- Summary: Mixed analyst sentiment amid low price.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxQSklFZERTbzBCd0dwSGJ2aVFsWnljWnJIWTJnVTA4TlJ4ckx1ODlFV2hUeHBnaE5nZWdBdnlQcnFKT252dmFYNWtXV2hVYkNGd1hvNF9OYVV6dHBZUzlXMTd5OVZ2bXR5MEZfZVQwbE45R3dpY1ZFaF9JWF92YVB1OVd0aHRKalk0Z0t5RkEySjVGNGpVSHdkcFEwTjI3cGRBUk9TRzB3YVJyWlA4U2VDMllvQXl1UXZibjB0dXdHOE9uemFWcmRZTDBMMA?oc=5>

## CATALYSTS

No items in this run

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NFLX** | **17.01** | **8.25** | **15.73** | **11.80** | **241,739,415,552.00 USD** | **-44.97** |
| DIS | 21.76 | 1.90 | 11.42 | 15.50 | 209,250,713,600.00 USD | 21.92 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| CMCSA | 8.03 | 0.97 | 5.07 | -6.10 | 90,124,533,760.00 USD | 7.83 |

Peers fetched as_of: 2026-11-24; NFLX reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-19 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

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

- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQUlJNYzhtcEhGeTRodEZCX1BuYW5Nai1vT19jS2dlRF9DMms0V2E3M2VMTFZfMDY4NldHcXQ5WjBvWDRyVTZGTkxmN0hqekRHSjE1N1RnbUFvYmxrSW5tT3ZtZGw1TGFRYTc4OWhTOHRnc2lBSjFsWThrR0FrVnlUZ1c4OGZHdmlxNUlSS0tSODUyWHNnX1Z6QzU1X0tJU1VMeHpwcGJ6VGZwR2JvV2c3RTJQdU54bFBBRUhTWVFtOGZLRzFzdklZSEo5X2lJZUYzcElz?oc=5
- https://news.google.com/rss/articles/CBMi5gFBVV95cUxPQ3V0RTMtTk0tSFNZMjMyam5oa19zaGlZcmZWOEE2N09iLVFkMVpLWTg3M2JqNVJxMzMwWWlFOGM1WU00N1c3YUQ3WjMwMWdKN1VTZ0dLNzZ0dkdDa1BoWjZEbDVXclNlVVpiTVBRYUxPZHBSMG9aSnczcTZYUW0zTXRjdEE2aXBzWDdBdUk0OUJ2SDVSODl1WUhnRF9VaXFFVTUxUWNFaVlUY2JqS2E0dUNCVEhnV2M1ckdLeXFEMGdJby1kNVNNcDFZcUtLeDU1U1B5UDZOamVjUXFjelBrUFRRcWRHZw?oc=5
- https://news.google.com/rss/articles/CBMi4wFBVV95cUxQVW1fa1lPbm00Nmx2VFRXaWR3MnprRGc4Y2ZzNGFKSDcwc2hHUlVaODRKNkxGLUt1Z205aFRtVnBxd0lxRGlzQlFOdmpJQktLbmNMT1Y5T2FhWWNPR3JEY1dtVTRuZ1pJMm5hM2pXLXRENWY5OXotMkhrYXczWHBhdjdZdlZMOExQMG94YzBhSklablhxcXpyeWVsWU9VOHVwQlBheHY0bXNGXzJGaEhEcHA2TUEzRUJwS3VZYW1DaU9zdjVldGZMamVfUzNaSGRyUXVPYThvVUlXSVJNYVZqQmRNbw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOR0JLbjlwdTNNb1hNOVc2US1uNDhfdmFSZHdONkJISlJSR3ROYjgyQVNQOEFtZ09DcDAyWkNDSnZfNGsyTndVLTBtSlFlSGUwbExYd19TbFlzOWN5ZDFERjBKNW9wc3lPMEZqc182c0JObUh3a1NIczM3RWJ6OUZRUUQyaUM2OGFPaWliYzhteGdKbjN0QjlVWQ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQUi1Da2Rza2JhSjRLZ2ZNTXQ4QWdGcXJfU0FrV19JREUyZk44MVFqcDhtLVlIeDJ4cWttNnVWelBUTk9pYmhIU0E1c29HVy1xQkE3ZkF0RG5sanVES1VPVDNkWGxsU0d6OGlDajdhaGJ1a0VHZDZ4OUNScDdycUM2R1ZzQndGcVM4Qy1nT0llekdWM1hOWUFEUmxyQ1Q5alpCb0hN?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxONUloejNrRDQ0bVZldllmOFlsVDM3dnp6ektqVDdXcU8taHduYjRuXzVhdi10T1B6VmVUcG93WDhrUEIzejdMT284a2lzbDZWYnctTFJHQXJfeGoxWXAwTFIwNmlRRU14aFMta3M1c1kxWUtfUzNrVE5TV1hNN3hZXzgtdmtqa1doZW5BR0pEaUR4VUZB?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxQSklFZERTbzBCd0dwSGJ2aVFsWnljWnJIWTJnVTA4TlJ4ckx1ODlFV2hUeHBnaE5nZWdBdnlQcnFKT252dmFYNWtXV2hVYkNGd1hvNF9OYVV6dHBZUzlXMTd5OVZ2bXR5MEZfZVQwbE45R3dpY1ZFaF9JWF92YVB1OVd0aHRKalk0Z0t5RkEySjVGNGpVSHdkcFEwTjI3cGRBUk9TRzB3YVJyWlA4U2VDMllvQXl1UXZibjB0dXdHOE9uemFWcmRZTDBMMA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
