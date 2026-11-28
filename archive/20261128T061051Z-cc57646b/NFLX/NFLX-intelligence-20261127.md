# NFLX Intelligence Report

- ticker: **NFLX**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/NFLX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NFLX/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:27:52.746462+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 3, 'ai': 11, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **12** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/NFLX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **4**; {'directional_claim_without_event_type': 3, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 10 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 30.43%; oldest publication 2026-11-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 60.9300 |
| Return 1D (%) | 2.5585 |
| Return 1W (%) | 7.4035 |
| Return 1M (%) | -2.5432 |
| Return YTD (%) | -35.0149 |
| Return 1Y (%) | -42.5947 |
| Annualized volatility (%) | 35.9410 |
| Beta vs SPY | 0.3416 |
| Max drawdown (%) | -48.1207 |
| Sharpe (rf=0) | -1.4144 |
| Downside deviation (rf=0, %) | 26.3317 |
| Sortino (rf=0) | -1.9306 |
| Historical VaR 95% (1D, %) | 3.3899 |
| Historical ES 95% (1D, %) | 5.0633 |
| Correlation vs SPY | 0.1428 |
| Tracking error vs SPY (%) | 36.9222 |
| P/E (trailing) | 17.61 |
| P/B | 8.54 |
| EV/EBITDA | 16.26 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 16.17 |
| Gross margin (%) | 50.69 |
| Operating margin (%) | 31.30 |
| Return on equity (%) | 53.46 |
| Free cash flow yield (%) | 10.18 |
| MA50 | 65.9516 |
| Close vs MA50 (%) | -7.6141 |
| MA200 | 79.4980 |
| Close vs MA200 (%) | -23.3566 |
| RSI (14, Wilder) | 44.5831 |
| MACD (12,26) | -2.1365 |
| MACD signal (9) | -2.2634 |
| MACD histogram | 0.1269 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NFLX': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 60.9300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.5585 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 7.4035 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -2.5432 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -35.0149 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -42.5947 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 35.9410 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.3317 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.9306 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.3899 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.0633 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1428 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 36.9222 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3416 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -48.1207 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.4144 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.1668 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.6850 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 31.2960 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 53.4630 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 10.1822 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.6098 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 44.5831 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.1269 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -7.6141 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -23.3566 -> Clearly below the moving-average trend level.

## TAILWINDS

### Netflix Has 2 Growth Engines That Could Drive Its Stock Higher in 2027
- Summary: Netflix highlights two growth engines projected to boost stock by 2027.
- Date: 2026-11-25 | Impact: high | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxPSVN4SUFNQmtBLUNWLXhGMFc2NW9mWjRPOGsyaTZoVEdOZmt4V2duNUhSYWRpeFhRTWVrUktHQUx2dldzYkdiaXFOZktOdmpBNUpsSWtVU2pTcXduaHpISGxJeXJzMktHcmhGYndpMXBDVlU1RjNRcXZyeUZBbmxYTExSQlJTWWN4blBkRURzblhsZ0lMdGhsV1p2Yk5tMzdvS1REdzJvdFBtZHd5NnhzeTlzNlM?oc=5>

### The Last Time Netflix Was This Cheap, the Stock Jumped 600%. Is It a Buy Now?
- Summary: Notes past cheap valuation and potential upside.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxONldhZWlzSXprUmo2SnVQSEFlRHpSVWpsOG5US3JESzFDVDRaMHlSUVFUcHFHenFlbVVBX0Eyd0ktai00c1ZHXzhsTXpaNzYwczdoVE84QzhTQ3cxbVB2OENPa3c1a2lMSXNVM2E4eC1RZFpfVXZlbWNrTUFfa0w0aHkxUUJDUmFDQ1BrbkJJenk2WWpreXExRWJwTDNmTktiS0EwNjY4NzRGejNmSndVV0ZwSEQ3NzA?oc=5>

### Netflix, Inc. (NFLX) Stock Forecasts
- Summary: Provides stock price forecasts for Netflix.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxOSFVFbU9TdkRZcFRaYnFfLWlvQ25yaTFZOVVUTDRrcDJBVWlyM1IxcWozYk43WnlKWEFMUGVZVTZzT0g1eWtjX1JQRTRTUTlmNkxpWDRveUhrQ0gwN0dCb0JYMkp4SWVCVEx6ellsSWluN3ZPWUQ0UU9ITkhFTWZENy05TlRibFYzSEpwMA?oc=5>

### Netflix (NFLX) Falls 38% This Year, Is It Now A Bargain?
- Summary: Reports 38% decline and asks if it's a bargain.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNRVprYUU0T045ZVdsNU5aZDN2OXRJTG9GLUo3eWRUWVhZdGxmcUFFMEtqLWNhNVpRSnh3VTl2S0xUbzEzbXdRLUh2R1k0d0h0M1VoSnRPOWdQcmFQZzc0MTRHdW9Da3NfS2RTS3JkWFJFMlRiOGVJLU50R0syVEpBcjcxQy15NFF2LURqWWdHT1huSUV2UnBZbnNhSFI2ZjlHZmY2MnRFdk9VUFd3Yl9xeTNNQUrSAboBQVVfeXFMTVlmaUFIOF8zR3V1R1BXVmZ5QmVXWEVEclpXM1REeEw4WVBJeWlfeHk4MEVTdmtGN3NPbVpRQlpZSEMxenh6U0dLMUlmd0JuUFRYaXpuVlgyYXEzZEY0d3JGVklKNTl6enpsRnhncklhSk9NZDI5aWRyRmFsQUg1SGR5aHB4UEpQRE5PVGxhcGw2NVRhT0dmdmJZVjhLbVNfN05CTVpGcWpuclNuZ2RfTWZ1dVM1bklUSjVB?oc=5>

### Netflix (NFLX) Beats Stock Market Upswing: What Investors Need to Know
- Summary: Positive market sentiment as Netflix outperforms broader market, suggesting strong investor confidence.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOaEZGWnVIVjdSdUNFNjNDa29udFlOTjRZcEtKN0hWM09jajViXzVQcUphMF9FdTFiVm1Bc2lLWWVXN3JMbXJ5STRPWHVTcGd2UUp5Skg0dF9EVjBCc2VOM0E5Y3ZuOWxkcFRiVHczakVzUXc0bjdSc1M3amZOdEVVU3g0MHVjc0gzNXQ5a0RnY29KY1Y0aWI0Rm04a0M?oc=5>

### Netflix (NASDAQ:NFLX) Stock Jumps 2% - Time to Buy?
- Summary: Stock price rises 2%, indicating potential buying opportunity for investors.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQZ3BiVE55OHFSQ182TzFMVjRCWE5KY3N2UkZmSjJOY1ltU2YyQWMzQUFmOGtacUZKdkEwNHpOSEN4WnB1NHQtWFFObXNMSEhMNkF1OFF4cDVUTng1WThxQXp6anpFbk84TXUzMG9aNkNSZ1ZBUnhDNHpnLXd0YU5xU1BOeDJTSTdtSURYTl9QY21ZWFFhYXhRd3FyUmR6VmJfVEFhWG4zOVQ?oc=5>

## HEADWINDS

### Netflix Stock Is Down 36% in 2026. Can Its Disney Partnership Make It a Buy Again?
- Summary: Netflix Stock Is Down 36% in 2026. Can Its Disney Partnership Make It a Buy Again?
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxPbkYwVFpLZ0tDaWRLYl84YUp2eEdtNEp2TzdudWhkc1YzOUdrT1hmbnYtSmxmalprTXlxaXlZSlBJejUxTjhfNWJOTm56bGlaRndRWHU4Vzlkc0JBVDA0dGdGU3F6TVIxSWFHeTM3cHVnR3F5aS1QTFZENzhDNFhLQ1dJYXpZMFNBSkJEZHBOTlFlNTFCUGZ1bTJsTWZZbUlxTmNWZTBMT3VIRkhUWEhLeElKRWtvNklCdmhCelk1Sno?oc=5>

### Netflix Stock Is Down 37% in 2026, But the Business Is Still Growing. Here's Why I'd Buy It Before the End of November.
- Summary: Netflix Stock Is Down 37% in 2026, But the Business Is Still Growing. Here's Why I'd Buy It Before the End of November.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxPNjlzblZCRWc1NUFGMW9CVWluRWlqOUdGYjU4V1FoOFptQThibXRCNG1vLXhsNTZncmdNd1dDQmJ2WXlsZURyV3djbWp1OGFWSkVXMXFPMlNaZGJlSlRTbElPZV90NDNkZGhyMElZa2pVNFBIbGtPbG5xQ2pVSjVJU3U0S3YyckN4b0R4N3h2TjhFYmV0RUNybDNONXBMLUVPNURtQ0pyWXFBZ3czX3U5elNBMUNOYm9PSkFLT2RlbmhMWEFjbExWSmQyVlZjS01LT1A1YjFzakZQQkpEb25uVWQyUFc4WkNrNzFCNQ?oc=5>

### NFLX Stock Edges Lower Overnight: Streaming Giant Buys Historic ‘Seinfeld’ Studio Lot In Reported $380M Deal
- Summary: NFLX Stock Edges Lower Overnight: Streaming Giant Buys Historic ‘Seinfeld’ Studio Lot In Reported $380M Deal
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNdzRobTQyMnVLaHV4Z3EyWGpSVlYwQ3ctelBHZjBhY051MVB5QnEtV3A1dXFzTXlMdWRyNGdXSXBDUVRWSVpiRm9qN1dEc3F4TklzN2pnZTZERXpiY3NvSWoxM01DS3QwMGRlVi1IZ2EtTm84SHBaWWNBY3hQU1B6bElzd0tnQTRvN1AyZzVLX29IZjJydTEyaUlsaGkzbGdjMGc?oc=5>

### Netflix Stock and Higher Content Spend: Can Margins Hold Firm in 2027?
- Summary: Higher content spend may pressure margins by 2027.
- Date: 2026-11-26 | Impact: medium | Horizon: long | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPbmRkZDR2SlI1RHhVMnZDZEljcmp0YkwyRXcxd1dnTkY3TjNxclhFd3RqNnRoSWIzV2RJckJDX0hGV3p3Z2ZwOTI1bGRpU3duMkxVQ282VDhfc25ZeHg2ei1Qd1U1cmwtQ0lkNnF3OXFQYU1xMDJqa09YT08tXzRRcm9yWm9VUU9FUEQ3R1R2NnFvU0hoUVJiQm9zS2Q5NEc1ZTZUTTJ5U084cEo2dUNRVlVxNHQ2ZVJTMjNudGY1RW1TUQ?oc=5>

### Netflix Falls Below $60. Bill Ackman Explains Why That’s an Incredible Investment Opportunity.
- Summary: Stock dips below $60, raising concerns despite analyst endorsement of long-term value.
- Date: 2026-11-22 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQNms5aUFqSmw1RkF6YXM5N2lnT2tTbzFyOEJkTUZlWFRUWDNlM1daOG9ldmVuV3d6SlVZbU5wSS01QlM1NWRDc0hfS2NRSFE2NlN0WDhNUVU2eExSSWprZ1hUS0J6TmJyc0VnaHI3QVZtUEI5dUZnS2p1bHZTMzA5VTdpZmhQdHVIV0Z6cUtyYS1PQnRZY3Mw?oc=5>

## CATALYSTS

### NFLX Stock Quote Price and Forecast
- Summary: Provides current price and future outlook, useful for decision-making.
- Date: 2026-11-26 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiUEFVX3lxTE9SYmJDZmdYamJZM2g0dmgxclVLUWRnbGY3MkZkcDBUTHhDMmM3UXpkZ1VyVUhBeHZKRTdOVEg5MTNBZHZ1UTVMQ1ZFR3hKb2Fx?oc=5>

### Here's What Would Prove Me Wrong About Netflix Stock
- Summary: Speculative analysis questioning current stock valuation, no concrete event.
- Date: 2026-11-26 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNd0xpNl9aMFJRbWpVWTdkQkpoTUhpd0ZYWDBHbUxTb2VFNzgwdUR1MXc4Z0lXZzNNOFRSRHZ1QWgxZUVsR042amdVQlU1dWgwMEJURHZMaThoTFpMS0tyTm0yaGRtMUtFd1NYQlEtR0hFVlFrckh3UUtPYlZRellpOXQxSW1FMUNoakN0X1gxTExuOGdzRGozZkxhRQ?oc=5>

### Netflix Stock in Focus After $380 Million Radford Studio Center Purchase
- Summary: Netflix announced a $380 million purchase of Radford Studio Center, expanding its production footprint and potentially boosting content output.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxNSXVRTHZsYk1XQ0xidGNSb0l3NlptRFVzOVJGMEJpS280TV9vbzNndDQ3VGtpTWlmSU0tUS1VUEhiaDRqYVE4emJkd0RMUzBUYlZMSHJTLTl0SnVuRGpyaVFFZ2JZMnA0a1ZYd25jOVVieFdKVjllUnN6U0JMTExtTFdZQlNmZW1HOThCdVIyWGl4dk5USFZ5dzRrT3BDTFJvRnFPZHIyR290Q1VQRFliNVAwTXFkeldBX2xPbGw5QWVZd3dsNmtxM0xWQQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NFLX** | **17.61** | **8.54** | **16.26** | **11.80** | **250,198,441,984.00 USD** | **-42.59** |
| DIS | 22.60 | 1.98 | 11.78 | 15.50 | 217,329,696,768.00 USD | 24.80 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| CMCSA | 8.25 | 1.00 | 5.14 | -6.10 | 92,610,240,512.00 USD | 10.34 |

Peers fetched as_of: 2026-11-27; NFLX reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-19 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

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

- https://news.google.com/rss/articles/CBMitAFBVV95cUxPSVN4SUFNQmtBLUNWLXhGMFc2NW9mWjRPOGsyaTZoVEdOZmt4V2duNUhSYWRpeFhRTWVrUktHQUx2dldzYkdiaXFOZktOdmpBNUpsSWtVU2pTcXduaHpISGxJeXJzMktHcmhGYndpMXBDVlU1RjNRcXZyeUZBbmxYTExSQlJTWWN4blBkRURzblhsZ0lMdGhsV1p2Yk5tMzdvS1REdzJvdFBtZHd5NnhzeTlzNlM?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxONldhZWlzSXprUmo2SnVQSEFlRHpSVWpsOG5US3JESzFDVDRaMHlSUVFUcHFHenFlbVVBX0Eyd0ktai00c1ZHXzhsTXpaNzYwczdoVE84QzhTQ3cxbVB2OENPa3c1a2lMSXNVM2E4eC1RZFpfVXZlbWNrTUFfa0w0aHkxUUJDUmFDQ1BrbkJJenk2WWpreXExRWJwTDNmTktiS0EwNjY4NzRGejNmSndVV0ZwSEQ3NzA?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxOSFVFbU9TdkRZcFRaYnFfLWlvQ25yaTFZOVVUTDRrcDJBVWlyM1IxcWozYk43WnlKWEFMUGVZVTZzT0g1eWtjX1JQRTRTUTlmNkxpWDRveUhrQ0gwN0dCb0JYMkp4SWVCVEx6ellsSWluN3ZPWUQ0UU9ITkhFTWZENy05TlRibFYzSEpwMA?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNRVprYUU0T045ZVdsNU5aZDN2OXRJTG9GLUo3eWRUWVhZdGxmcUFFMEtqLWNhNVpRSnh3VTl2S0xUbzEzbXdRLUh2R1k0d0h0M1VoSnRPOWdQcmFQZzc0MTRHdW9Da3NfS2RTS3JkWFJFMlRiOGVJLU50R0syVEpBcjcxQy15NFF2LURqWWdHT1huSUV2UnBZbnNhSFI2ZjlHZmY2MnRFdk9VUFd3Yl9xeTNNQUrSAboBQVVfeXFMTVlmaUFIOF8zR3V1R1BXVmZ5QmVXWEVEclpXM1REeEw4WVBJeWlfeHk4MEVTdmtGN3NPbVpRQlpZSEMxenh6U0dLMUlmd0JuUFRYaXpuVlgyYXEzZEY0d3JGVklKNTl6enpsRnhncklhSk9NZDI5aWRyRmFsQUg1SGR5aHB4UEpQRE5PVGxhcGw2NVRhT0dmdmJZVjhLbVNfN05CTVpGcWpuclNuZ2RfTWZ1dVM1bklUSjVB?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOaEZGWnVIVjdSdUNFNjNDa29udFlOTjRZcEtKN0hWM09jajViXzVQcUphMF9FdTFiVm1Bc2lLWWVXN3JMbXJ5STRPWHVTcGd2UUp5Skg0dF9EVjBCc2VOM0E5Y3ZuOWxkcFRiVHczakVzUXc0bjdSc1M3amZOdEVVU3g0MHVjc0gzNXQ5a0RnY29KY1Y0aWI0Rm04a0M?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQZ3BiVE55OHFSQ182TzFMVjRCWE5KY3N2UkZmSjJOY1ltU2YyQWMzQUFmOGtacUZKdkEwNHpOSEN4WnB1NHQtWFFObXNMSEhMNkF1OFF4cDVUTng1WThxQXp6anpFbk84TXUzMG9aNkNSZ1ZBUnhDNHpnLXd0YU5xU1BOeDJTSTdtSURYTl9QY21ZWFFhYXhRd3FyUmR6VmJfVEFhWG4zOVQ?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxPbkYwVFpLZ0tDaWRLYl84YUp2eEdtNEp2TzdudWhkc1YzOUdrT1hmbnYtSmxmalprTXlxaXlZSlBJejUxTjhfNWJOTm56bGlaRndRWHU4Vzlkc0JBVDA0dGdGU3F6TVIxSWFHeTM3cHVnR3F5aS1QTFZENzhDNFhLQ1dJYXpZMFNBSkJEZHBOTlFlNTFCUGZ1bTJsTWZZbUlxTmNWZTBMT3VIRkhUWEhLeElKRWtvNklCdmhCelk1Sno?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxPNjlzblZCRWc1NUFGMW9CVWluRWlqOUdGYjU4V1FoOFptQThibXRCNG1vLXhsNTZncmdNd1dDQmJ2WXlsZURyV3djbWp1OGFWSkVXMXFPMlNaZGJlSlRTbElPZV90NDNkZGhyMElZa2pVNFBIbGtPbG5xQ2pVSjVJU3U0S3YyckN4b0R4N3h2TjhFYmV0RUNybDNONXBMLUVPNURtQ0pyWXFBZ3czX3U5elNBMUNOYm9PSkFLT2RlbmhMWEFjbExWSmQyVlZjS01LT1A1YjFzakZQQkpEb25uVWQyUFc4WkNrNzFCNQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNdzRobTQyMnVLaHV4Z3EyWGpSVlYwQ3ctelBHZjBhY051MVB5QnEtV3A1dXFzTXlMdWRyNGdXSXBDUVRWSVpiRm9qN1dEc3F4TklzN2pnZTZERXpiY3NvSWoxM01DS3QwMGRlVi1IZ2EtTm84SHBaWWNBY3hQU1B6bElzd0tnQTRvN1AyZzVLX29IZjJydTEyaUlsaGkzbGdjMGc?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPbmRkZDR2SlI1RHhVMnZDZEljcmp0YkwyRXcxd1dnTkY3TjNxclhFd3RqNnRoSWIzV2RJckJDX0hGV3p3Z2ZwOTI1bGRpU3duMkxVQ282VDhfc25ZeHg2ei1Qd1U1cmwtQ0lkNnF3OXFQYU1xMDJqa09YT08tXzRRcm9yWm9VUU9FUEQ3R1R2NnFvU0hoUVJiQm9zS2Q5NEc1ZTZUTTJ5U084cEo2dUNRVlVxNHQ2ZVJTMjNudGY1RW1TUQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQNms5aUFqSmw1RkF6YXM5N2lnT2tTbzFyOEJkTUZlWFRUWDNlM1daOG9ldmVuV3d6SlVZbU5wSS01QlM1NWRDc0hfS2NRSFE2NlN0WDhNUVU2eExSSWprZ1hUS0J6TmJyc0VnaHI3QVZtUEI5dUZnS2p1bHZTMzA5VTdpZmhQdHVIV0Z6cUtyYS1PQnRZY3Mw?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQUlJNYzhtcEhGeTRodEZCX1BuYW5Nai1vT19jS2dlRF9DMms0V2E3M2VMTFZfMDY4NldHcXQ5WjBvWDRyVTZGTkxmN0hqekRHSjE1N1RnbUFvYmxrSW5tT3ZtZGw1TGFRYTc4OWhTOHRnc2lBSjFsWThrR0FrVnlUZ1c4OGZHdmlxNUlSS0tSODUyWHNnX1Z6QzU1X0tJU1VMeHpwcGJ6VGZwR2JvV2c3RTJQdU54bFBBRUhTWVFtOGZLRzFzdklZSEo5X2lJZUYzcElz?oc=5
- https://news.google.com/rss/articles/CBMiUEFVX3lxTE9SYmJDZmdYamJZM2g0dmgxclVLUWRnbGY3MkZkcDBUTHhDMmM3UXpkZ1VyVUhBeHZKRTdOVEg5MTNBZHZ1UTVMQ1ZFR3hKb2Fx?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNd0xpNl9aMFJRbWpVWTdkQkpoTUhpd0ZYWDBHbUxTb2VFNzgwdUR1MXc4Z0lXZzNNOFRSRHZ1QWgxZUVsR042amdVQlU1dWgwMEJURHZMaThoTFpMS0tyTm0yaGRtMUtFd1NYQlEtR0hFVlFrckh3UUtPYlZRellpOXQxSW1FMUNoakN0X1gxTExuOGdzRGozZkxhRQ?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxQYWQwY2RzNnR4SFQ4UUxrNUtzNmlId1BiRVUyXzFNNllab1lENmRYZzAzckkwX1pnUC1sR19LSW93Q1dJWDhxY1dBNVFLdW5vZnpCdG1JSWNGSTRNd1lnLVNlc2p0ZzdteGFGdnBUN3JiUTdQQU5UUk5EQjhreEQ1MlVtQkpJMnZ3RzRVLUVGcVFtTWZCRXZkUTlPYUEwcFE1S3hBa3EwX3hsR3U2YjFpTWk4eHdackRRWGlQbDV6MmRvdkgyQU5xVV93TUhJRE9pMlE?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxNSXVRTHZsYk1XQ0xidGNSb0l3NlptRFVzOVJGMEJpS280TV9vbzNndDQ3VGtpTWlmSU0tUS1VUEhiaDRqYVE4emJkd0RMUzBUYlZMSHJTLTl0SnVuRGpyaVFFZ2JZMnA0a1ZYd25jOVVieFdKVjllUnN6U0JMTExtTFdZQlNmZW1HOThCdVIyWGl4dk5USFZ5dzRrT3BDTFJvRnFPZHIyR290Q1VQRFliNVAwTXFkeldBX2xPbGw5QWVZd3dsNmtxM0xWQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
