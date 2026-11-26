# NFLX Intelligence Report

- ticker: **NFLX**
- Report as_of: **2026-11-25**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/NFLX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NFLX/key-statistics/
- AI analysis snapshot as_of: **2026-11-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-26T06:52:31.144210+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 3, 'ai': 5, 'unknown': 0, 'irrelevant': 14})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **14** exact headline/source/date matches; prior report **20261125T065354Z-0b3565c6/NFLX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 10 named publishers; 2 exact duplicates; 22 HTTPS source links; largest publisher share 31.82%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 59.4100 |
| Return 1D (%) | 0.9173 |
| Return 1W (%) | -0.6854 |
| Return 1M (%) | -9.7798 |
| Return YTD (%) | -36.6361 |
| Return 1Y (%) | -43.0939 |
| Annualized volatility (%) | 35.8451 |
| Beta vs SPY | 0.3338 |
| Max drawdown (%) | -48.1207 |
| Sharpe (rf=0) | -1.3995 |
| Downside deviation (rf=0, %) | 26.2792 |
| Sortino (rf=0) | -1.9090 |
| Historical VaR 95% (1D, %) | 3.3880 |
| Historical ES 95% (1D, %) | 5.0633 |
| Correlation vs SPY | 0.1390 |
| Tracking error vs SPY (%) | 36.8644 |
| P/E (trailing) | 17.17 |
| P/B | 8.33 |
| EV/EBITDA | 15.87 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 15.76 |
| Gross margin (%) | 50.69 |
| Operating margin (%) | 31.30 |
| Return on equity (%) | 53.46 |
| Free cash flow yield (%) | 10.44 |
| MA50 | 66.2392 |
| Close vs MA50 (%) | -10.3099 |
| MA200 | 79.5914 |
| Close vs MA200 (%) | -25.3563 |
| RSI (14, Wilder) | 38.7830 |
| MACD (12,26) | -2.3759 |
| MACD signal (9) | -2.2951 |
| MACD histogram | -0.0807 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NFLX': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 59.4100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.9173 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.6854 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -9.7798 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -36.6361 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -43.0939 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 35.8451 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.2792 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.9090 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.3880 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.0633 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1390 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 36.8644 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3338 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -48.1207 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.3995 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.7610 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.6850 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 31.2960 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 53.4630 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 10.4428 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.1705 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.7830 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0807 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -10.3099 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -25.3563 -> Clearly below the moving-average trend level.

## TAILWINDS

### Netflix (NASDAQ: NFLX) Stock Price Trades At Half Its Historical Multiple As January Guidance Looms Large
- Summary: Netflix stock trades at half its historical multiple amid upcoming guidance.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5gFBVV95cUxPQ3V0RTMtTk0tSFNZMjMyam5oa19zaGlZcmZWOEE2N09iLVFkMVpLWTg3M2JqNVJxMzMwWWlFOGM1WU00N1c3YUQ3WjMwMWdKN1VTZ0dLNzZ0dkdDa1BoWjZEbDVXclNlVVpiTVBRYUxPZHBSMG9aSnczcTZYUW0zTXRjdEE2aXBzWDdBdUk0OUJ2SDVSODl1WUhnRF9VaXFFVTUxUWNFaVlUY2JqS2E0dUNCVEhnV2M1ckdLeXFEMGdJby1kNVNNcDFZcUtLeDU1U1B5UDZOamVjUXFjelBrUFRRcWRHZw?oc=5>

### Netflix Has 2 Growth Engines That Could Drive Its Stock Higher in 2027
- Summary: Netflix highlights two growth engines projected to boost stock by 2027.
- Date: 2026-11-25 | Impact: high | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxPSVN4SUFNQmtBLUNWLXhGMFc2NW9mWjRPOGsyaTZoVEdOZmt4V2duNUhSYWRpeFhRTWVrUktHQUx2dldzYkdiaXFOZktOdmpBNUpsSWtVU2pTcXduaHpISGxJeXJzMktHcmhGYndpMXBDVlU1RjNRcXZyeUZBbmxYTExSQlJTWWN4blBkRURzblhsZ0lMdGhsV1p2Yk5tMzdvS1REdzJvdFBtZHd5NnhzeTlzNlM?oc=5>

## HEADWINDS

### Netflix Stock Is Down 36% and Wall Street Keeps Downgrading It. History Says That's a Mistake.
- Summary: Netflix Stock Is Down 36% and Wall Street Keeps Downgrading It. History Says That's a Mistake.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOazJVaF9Sd3Q3TnBVTEMxU3VTbGtvUjVKUkR1U2dXTlFiRFh4cldtdDRzaUd0elVPQkdlbi01NUR1NHNaNFVydWYzcmlhSllrek85d3ZsNnFTeGdPWi1nekR3ZUVNRXJKSjlZLWo5Q050OWZUYW5ZQ1pfS1V1Z3lBemdFQ2dlR3g2c0JwYUlRanNldl9rRGc?oc=5>

### Netflix Stock Is Down 37% in 2026, But the Business Is Still Growing. Here's Why I'd Buy It Before the End of November.
- Summary: Netflix Stock Is Down 37% in 2026, But the Business Is Still Growing. Here's Why I'd Buy It Before the End of November.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxPNjlzblZCRWc1NUFGMW9CVWluRWlqOUdGYjU4V1FoOFptQThibXRCNG1vLXhsNTZncmdNd1dDQmJ2WXlsZURyV3djbWp1OGFWSkVXMXFPMlNaZGJlSlRTbElPZV90NDNkZGhyMElZa2pVNFBIbGtPbG5xQ2pVSjVJU3U0S3YyckN4b0R4N3h2TjhFYmV0RUNybDNONXBMLUVPNURtQ0pyWXFBZ3czX3U5elNBMUNOYm9PSkFLT2RlbmhMWEFjbExWSmQyVlZjS01LT1A1YjFzakZQQkpEb25uVWQyUFc4WkNrNzFCNQ?oc=5>

### NFLX Stock Edges Lower Overnight: Streaming Giant Buys Historic ‘Seinfeld’ Studio Lot In Reported $380M Deal
- Summary: NFLX Stock Edges Lower Overnight: Streaming Giant Buys Historic ‘Seinfeld’ Studio Lot In Reported $380M Deal
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNdzRobTQyMnVLaHV4Z3EyWGpSVlYwQ3ctelBHZjBhY051MVB5QnEtV3A1dXFzTXlMdWRyNGdXSXBDUVRWSVpiRm9qN1dEc3F4TklzN2pnZTZERXpiY3NvSWoxM01DS3QwMGRlVi1IZ2EtTm84SHBaWWNBY3hQU1B6bElzd0tnQTRvN1AyZzVLX29IZjJydTEyaUlsaGkzbGdjMGc?oc=5>

### Netflix (NFLX) Down 8% Since Last Earnings Report: Can It Rebound?
- Summary: Recent earnings underperformance causing decline.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxONUloejNrRDQ0bVZldllmOFlsVDM3dnp6ektqVDdXcU8taHduYjRuXzVhdi10T1B6VmVUcG93WDhrUEIzejdMT284a2lzbDZWYnctTFJHQXJfeGoxWXAwTFIwNmlRRU14aFMta3M1c1kxWUtfUzNrVE5TV1hNN3hZXzgtdmtqa1doZW5BR0pEaUR4VUZB?oc=5>

### Netflix Falls Below $60. Bill Ackman Explains Why That’s an Incredible Investment Opportunity.
- Summary: Netflix stock dips below $60, seen as a downside risk.
- Date: 2026-11-22 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQNms5aUFqSmw1RkF6YXM5N2lnT2tTbzFyOEJkTUZlWFRUWDNlM1daOG9ldmVuV3d6SlVZbU5wSS01QlM1NWRDc0hfS2NRSFE2NlN0WDhNUVU2eExSSWprZ1hUS0J6TmJyc0VnaHI3QVZtUEI5dUZnS2p1bHZTMzA5VTdpZmhQdHVIV0Z6cUtyYS1PQnRZY3Mw?oc=5>

## CATALYSTS

### Netflix Stock in Focus After $380 Million Radford Studio Center Purchase
- Summary: Netflix acquires Radford Studio Center for $380M.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxNSXVRTHZsYk1XQ0xidGNSb0l3NlptRFVzOVJGMEJpS280TV9vbzNndDQ3VGtpTWlmSU0tUS1VUEhiaDRqYVE4emJkd0RMUzBUYlZMSHJTLTl0SnVuRGpyaVFFZ2JZMnA0a1ZYd25jOVVieFdKVjllUnN6U0JMTExtTFdZQlNmZW1HOThCdVIyWGl4dk5USFZ5dzRrT3BDTFJvRnFPZHIyR290Q1VQRFliNVAwTXFkeldBX2xPbGw5QWVZd3dsNmtxM0xWQQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NFLX** | **17.17** | **8.33** | **15.87** | **11.80** | **243,956,826,112.00 USD** | **-43.09** |
| DIS | 22.31 | 1.95 | 11.65 | 15.50 | 214,528,524,288.00 USD | 23.34 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| CMCSA | 8.14 | 0.99 | 5.11 | -6.10 | 91,367,391,232.00 USD | 8.41 |

Peers fetched as_of: 2026-11-25; NFLX reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-19 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-25

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

- https://news.google.com/rss/articles/CBMi5gFBVV95cUxPQ3V0RTMtTk0tSFNZMjMyam5oa19zaGlZcmZWOEE2N09iLVFkMVpLWTg3M2JqNVJxMzMwWWlFOGM1WU00N1c3YUQ3WjMwMWdKN1VTZ0dLNzZ0dkdDa1BoWjZEbDVXclNlVVpiTVBRYUxPZHBSMG9aSnczcTZYUW0zTXRjdEE2aXBzWDdBdUk0OUJ2SDVSODl1WUhnRF9VaXFFVTUxUWNFaVlUY2JqS2E0dUNCVEhnV2M1ckdLeXFEMGdJby1kNVNNcDFZcUtLeDU1U1B5UDZOamVjUXFjelBrUFRRcWRHZw?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxPSVN4SUFNQmtBLUNWLXhGMFc2NW9mWjRPOGsyaTZoVEdOZmt4V2duNUhSYWRpeFhRTWVrUktHQUx2dldzYkdiaXFOZktOdmpBNUpsSWtVU2pTcXduaHpISGxJeXJzMktHcmhGYndpMXBDVlU1RjNRcXZyeUZBbmxYTExSQlJTWWN4blBkRURzblhsZ0lMdGhsV1p2Yk5tMzdvS1REdzJvdFBtZHd5NnhzeTlzNlM?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOazJVaF9Sd3Q3TnBVTEMxU3VTbGtvUjVKUkR1U2dXTlFiRFh4cldtdDRzaUd0elVPQkdlbi01NUR1NHNaNFVydWYzcmlhSllrek85d3ZsNnFTeGdPWi1nekR3ZUVNRXJKSjlZLWo5Q050OWZUYW5ZQ1pfS1V1Z3lBemdFQ2dlR3g2c0JwYUlRanNldl9rRGc?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxPNjlzblZCRWc1NUFGMW9CVWluRWlqOUdGYjU4V1FoOFptQThibXRCNG1vLXhsNTZncmdNd1dDQmJ2WXlsZURyV3djbWp1OGFWSkVXMXFPMlNaZGJlSlRTbElPZV90NDNkZGhyMElZa2pVNFBIbGtPbG5xQ2pVSjVJU3U0S3YyckN4b0R4N3h2TjhFYmV0RUNybDNONXBMLUVPNURtQ0pyWXFBZ3czX3U5elNBMUNOYm9PSkFLT2RlbmhMWEFjbExWSmQyVlZjS01LT1A1YjFzakZQQkpEb25uVWQyUFc4WkNrNzFCNQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNdzRobTQyMnVLaHV4Z3EyWGpSVlYwQ3ctelBHZjBhY051MVB5QnEtV3A1dXFzTXlMdWRyNGdXSXBDUVRWSVpiRm9qN1dEc3F4TklzN2pnZTZERXpiY3NvSWoxM01DS3QwMGRlVi1IZ2EtTm84SHBaWWNBY3hQU1B6bElzd0tnQTRvN1AyZzVLX29IZjJydTEyaUlsaGkzbGdjMGc?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxONUloejNrRDQ0bVZldllmOFlsVDM3dnp6ektqVDdXcU8taHduYjRuXzVhdi10T1B6VmVUcG93WDhrUEIzejdMT284a2lzbDZWYnctTFJHQXJfeGoxWXAwTFIwNmlRRU14aFMta3M1c1kxWUtfUzNrVE5TV1hNN3hZXzgtdmtqa1doZW5BR0pEaUR4VUZB?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQNms5aUFqSmw1RkF6YXM5N2lnT2tTbzFyOEJkTUZlWFRUWDNlM1daOG9ldmVuV3d6SlVZbU5wSS01QlM1NWRDc0hfS2NRSFE2NlN0WDhNUVU2eExSSWprZ1hUS0J6TmJyc0VnaHI3QVZtUEI5dUZnS2p1bHZTMzA5VTdpZmhQdHVIV0Z6cUtyYS1PQnRZY3Mw?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQUlJNYzhtcEhGeTRodEZCX1BuYW5Nai1vT19jS2dlRF9DMms0V2E3M2VMTFZfMDY4NldHcXQ5WjBvWDRyVTZGTkxmN0hqekRHSjE1N1RnbUFvYmxrSW5tT3ZtZGw1TGFRYTc4OWhTOHRnc2lBSjFsWThrR0FrVnlUZ1c4OGZHdmlxNUlSS0tSODUyWHNnX1Z6QzU1X0tJU1VMeHpwcGJ6VGZwR2JvV2c3RTJQdU54bFBBRUhTWVFtOGZLRzFzdklZSEo5X2lJZUYzcElz?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxNSXVRTHZsYk1XQ0xidGNSb0l3NlptRFVzOVJGMEJpS280TV9vbzNndDQ3VGtpTWlmSU0tUS1VUEhiaDRqYVE4emJkd0RMUzBUYlZMSHJTLTl0SnVuRGpyaVFFZ2JZMnA0a1ZYd25jOVVieFdKVjllUnN6U0JMTExtTFdZQlNmZW1HOThCdVIyWGl4dk5USFZ5dzRrT3BDTFJvRnFPZHIyR290Q1VQRFliNVAwTXFkeldBX2xPbGw5QWVZd3dsNmtxM0xWQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
