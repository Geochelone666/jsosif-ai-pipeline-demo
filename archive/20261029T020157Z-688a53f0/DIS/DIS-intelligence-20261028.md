# DIS Intelligence Report

- ticker: **DIS**
- Report as_of: **2026-10-28**
- Market data as_of: **2026-10-28**
- Quant sources: https://finance.yahoo.com/quote/DIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/DIS/key-statistics/
- AI analysis snapshot as_of: **2026-10-28**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-29T02:15:44.877704+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 16, 'rule': 1, 'ai': 11, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261028T015717Z-533e470c/DIS** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 1, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 16 unique headlines; 8 named publishers; 0 exact duplicates; 16 HTTPS source links; largest publisher share 43.75%; oldest publication 2026-10-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 109.0400 |
| Return 1D (%) | -1.0796 |
| Return 1W (%) | -2.4949 |
| Return 1M (%) | 3.2674 |
| Return YTD (%) | -3.4231 |
| Return 1Y (%) | -0.9235 |
| Annualized volatility (%) | 26.9241 |
| Beta vs SPY | 0.6164 |
| Max drawdown (%) | -20.2451 |
| Sharpe (rf=0) | 0.1001 |
| Downside deviation (rf=0, %) | 19.2598 |
| Sortino (rf=0) | 0.1399 |
| Historical VaR 95% (1D, %) | 2.4075 |
| Historical ES 95% (1D, %) | 3.7715 |
| Correlation vs SPY | 0.2908 |
| Tracking error vs SPY (%) | 26.2173 |
| P/E (trailing) | 22.72 |
| P/B | 1.71 |
| EV/EBITDA | 11.26 |
| Revenue growth (%) | 6.80 |
| Forward P/E (estimate) | 14.55 |
| Gross margin (%) | 37.59 |
| Operating margin (%) | 19.30 |
| Return on equity (%) | 8.01 |
| Free cash flow yield (%) | 2.58 |
| MA50 | 107.2026 |
| Close vs MA50 (%) | 1.7140 |
| MA200 | 103.0277 |
| Close vs MA200 (%) | 5.8356 |
| RSI (14, Wilder) | 52.1371 |
| MACD (12,26) | 1.4668 |
| MACD signal (9) | 1.4815 |
| MACD histogram | -0.0147 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'DIS': 270, 'SPY': 270}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 109.0400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.0796 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.4949 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.2674 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -3.4231 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -0.9235 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 26.9241 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 19.2598 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.1399 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4075 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.7715 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2908 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.2173 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6164 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.2451 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1001 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 14.5483 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 37.5950 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 19.3010 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 8.0100 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.5815 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.7167 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 52.1371 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0147 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.7140 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 5.8356 -> Clearly above the moving-average trend level.

## TAILWINDS

### Walt Disney (DIS) Rises As Market Takes a Dip: Key Facts
- Summary: Disney stock rises as market dips, indicating a positive market move.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQZGhWalpQSjhncTE1ZEsyRy1KTHNXQ18yX0FRNlV6ekUyM1l1TzVOYUlfVFNiaFc3a256TFFVY3lwWXo4VGl5UElMalZYb3FMNHRDWjNZQWpBV3p4aVdpUmV4V1VzZlUyM1VHNEdaTlpMY3k2N3lESEpkb1ZVRWVlWkR5QTBLQ1JIYWNTTHRJV3pxanYwTi1NcA?oc=5>

### Disney (DIS) Stock Looks Reasonably Priced After A 43% Gain
- Summary: Stock appears fairly priced following a 43% gain.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQOEdDdXl2bGNjMmg5WEs1T0I2RjE1V1lrdlpTR1hfYmYxa0EwT3NxN1lOUTdmVmpwc0tRRnVZcUI4QUV5dko3RGhnTmxkc1N4d3hFMTQ1UmpkM2xCSVVJUlA1b1NXSnpQUHZpUGFJSU53blZwVjl3QlJCczk2SkpkSmFYOUFycUdUWmQzTmpvZ0ItQ0ZRZ21JVk9MNS1fRWM?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Walt Disney Earnings Preview: What to Expect
- Summary: Walt Disney Earnings Preview: What to Expect
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQMldKcDFFX2poOGxTdDBWdGEwSS1tRlI0NUVGaHYtNlVIazlqMFVTempwSlBpbV9uR2sxZDhOTzlKX3cxRFhldjFFa3FNc2d5M0dpdE9YX1hpeFZCWHQ3SGg5NFNpek5fSHBkUDdtWWJLVjUzVGJJWXU5LVZGMEtISmlJbkVoczMzbXl6Yk5wZ0U5dl9RSTlkNGZHVlAyTHliSXc?oc=5>

### How Much Upside Is Left In Disney Stock?
- Summary: Analysis of potential upside in Disney shares, considering current valuation and future prospects.
- Date: 2026-10-27 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQRkwzeUFCNXMtMzV6T2hVRXVmYVhhWVlfbnRUbHJQY1RHcHU4M1Bvd05fQ1hOV1hWVmFhcFV4bkRWY3hDZmdKOHUzWW5mYjZ5RVBkdGtHM1hDejkzc1I5STZBb1RRNjQzd0ZFN1RUa2hEWXdhcHVRTV81azZlVlJYMzRMZ0YzQTdWOW0zV2hPaldXQVlPSnd3OGVUbThvcC1t?oc=5>

### The Walt Disney Company (DIS) is Attracting Investor Attention: Here is What You Should Know
- Summary: Overview of factors drawing investor focus to Disney, including financials and strategic moves.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQTTM0MEdOT2hXVGFBWU9rLW5FMS1pU2NnSHdBWmlmQjBsYlRlQmx6ZkZ6U0pIWU5FTU5Ncy1xQW4waUdVWnk4cFpGY1M0eDNFcnhCU205emoyQ05zZ0xiRHhGbmtrb09TSGpiX3NWLVpKS0RlektrWGl6VnpjRzhtNF94QnhUNFhZNkJySUJYdzhpMEpPMFB0Sk42YVFyTjhv?oc=5>

### Walt Disney (DIS) Bids For Character.AI, Is The 13% Discount Enough?
- Summary: Disney is bidding for Character.AI, evaluating if the 13% discount justifies the acquisition.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPQ3gxelZ2T29IdUFpdHVkZ0pMdGFWX0ZpRnlUcWJKczduQXl6N2JwQTM1M2wtc3VlQ3BaNVRZZjRHUmQ4dll6V0FBVlU2ZG5VYWdNNkxQa01BU2w0TVJpNDRobjZCN1VpQ3lMOUpuXzRub0Y5OFpTMEZJd0pCYUNDdnFHZGNzck9TM3d4UEJ4WXF3VWozR1JUZWtHOA?oc=5>

### Disney Stock Rose 10 Sessions in a Row While Bidding $20 Million for Character.AI’s Technology. Here’s Where It Could Go by 2030
- Summary: Disney bids $20M for Character.AI tech, boosting future growth prospects.
- Date: 2026-10-26 | Impact: high | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPZ294WFdGSTBPODM0MVEySGh1SnZnelZtSFNOT0xkTWNEUHZhZU5GREVGbERDUDd6ZlVQczROYTNTUGstaXE2amY2d3R4RU5hZHBab2FOYS1ZLWdZb3ozQXk5VGdDLVpsSDBHLWxSZHZ4OHVpbV84QVgzeDQ0VXJ1Sjd4aTl2bDFQOTFTR1dvTmo0MmJteURiLTJR?oc=5>

### Disney has the Super Bowl and some super drama (DIS:NYSE)
- Summary: Discussion of Disney's Super Bowl involvement and related controversies impacting its brand.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQM0xtYVgyMVRPTHBvQjN3M0pjdDZXTW9DcUlIU3dIRmZGdHpLeDFqeWppU3Z2Uk1tTkpMRExrb3daWklXc0UtSzhPa3NXcGU4elVnRlRaQlpYS1hoSThCRzNxeW5Wb1hwWUxKc3F1UDljemxhNEVac1RKclRVRm5xLVFfdHZzOHFPeGZqRw?oc=5>

### The Walt Disney Company $DIS Stock Holdings Lessened by Prime Capital Investment Advisors LLC
- Summary: Prime Capital Investment Advisors LLC reduced its Disney holdings, reflecting a change in shareholder composition.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi6AFBVV95cUxOaGh3SUVLS3MzejhVU085TEIwNFVIUU9laUZ5UWtEY01xcS13RHdyWkRVN3kyaDRRMWVLQzNNUGFoWTZ0enI2Nnp2bnBUTVItUUR0ZXJXbjdfWFo3Tm81a3FScmFHZ0U4eFlUeDZaUnFwRjhKQ0RoLUhNZWdjbTZmTzRMVjU5VzlhQmRUYV9fUGt6YTBiaUNBR1ljUzlvZng3djNzaVgxM3kxaTlrWkcwQmlKdXlxdWhkOTNwTU94VFEwZXFTSVc0Xy1zOVhRUE1jQXc4a2t0S05LdFVndXlXdlphbkxSZENt?oc=5>

### Disney (DIS) Stock May Be Near Fair Value Despite AI Asset Bid
- Summary: Disney stock appears near fair value amid AI asset bid concerns.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPR1h5SUU0LXFib0pMaUxjOE9VR0Z1ZDhhWUhycl9YYXFlV2s1Ml80bHhBWm9oRllXTVNGNEoxUkVabW50VjVvaEx1dTgxZUIxdEkyamllVkE5QjM2Qmh1bVJNR3NnZW12YllJNGE5VEZhUDJ3dVFudGVjd2hTSmtBaUVoWnJjNXYzcWxTamxobG5pX3Z4Tlh6VWR2eFpNZkhaWUlYLTkxZFVNYXNKWDBtWnlLV1J5SmR0U3RsOUR3Qk04Z9IBxwFBVV95cUxNeGhLcHdfSmNlRFhESm16X3pkUmVIUEhpZVVsNzRjWWR5UGNsREJnZVU4TGRtVmtyZW5vNV9za054aVAtTHkzaEVfdWp1QmVSV2pPd1R6NVNiZjdHV0RwV182U3JfSldqQ3FSQXFyQlFZVXZET0ctQ0NxRDRibnViZHlpWUNXR1ZBdm9MVU9WeUFfbTdwdktOS3I5WjJjdXFFMUN0cFh6Y2R5U3l0QzNNdExuWkxsUEw5ajJ5eDVmazVha2dOVkpB?oc=5>

### Walt Disney (DIS) Bids For Character.AI, Is The Stock Still A Bargain?
- Summary: Disney announces bid for Character.AI, potentially expanding AI capabilities and content creation.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxPbmZUeHNOZkh6OFdld0NnVnVfUE1NbVJGMXJjNzNaQXpUQlJzbUV0b1dNeFQwNzl3dV9NdXhjb203eGpONGI0VGI4ZHRrN2g4VDQtWlJwc3hWVXFhcC1NbDRmLTRmMXdsR2NVTjNhSFNBTnNMdUZGX3dvcHdxRW5PN3RJMV9HQngtYUprYzByWVZrQ0NyNlR0VXgwWHpvNkJETU9iX05KX3FLMllReW9Wb1pGLWhBMkxhZXpJM2ZMSUdKdU5wZWZB0gHHAUFVX3lxTE9uZlR4c05mSHo4V2V3Q2dWdV9QTU1tUkYxcmM3M1pBelRCUnNtRXRvV014VDA3OXd1X011eGNvbTd4ak40YjRUYjhkdGs3aDhUNC1aUnBzeFZVcWFwLU1sNGYtNGYxd2xHY1VOM2FIU0FOc0x1RkZfd29wd3FFbk83dEkxX0dCeC1hSmtjMHJZVmtDQ3I2VHRVeDBYem82QkRNT2JfTkpfcUsyWVF5b1ZvWkYtaEEyTGFlekkzZkxJR0p1TnBlZkE?oc=5>

## RISKS

### Walt Disney (DIS) Stock Drops Despite Market Gains: Important Facts to Note
- Summary: Disney shares fell amid broader market gains, indicating investor concern over recent performance.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOYlBMWmx5TjRucnVzN1dpOVN4dG9wRFJFdEF0NHRkX1FhMnpLVmpiai1oTXI4VUtTSXdrdmF1N2gzQjZDX3l6UjJKb2U5M3V4NDcxNEJFdVVYTF8ySkJxZkY1ZEtrNmdoQXBhVXlLTDFIY2dMcmdoN19XVE5UVHBsbUN3N3NKLTJOdGF5ZWxJOGVoYWVldVI4?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **DIS** | **22.72** | **1.71** | **11.26** | **6.80** | **188,277,932,032.00 USD** | **-0.92** |
| NFLX | 18.07 | 8.69 | 16.54 | 11.80 | 258,122,629,120.00 USD | -43.77 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| PSKY | N/A | 0.93 | 7.95 | 0.90 | 10,992,190,464.00 USD | N/A |

Peers fetched as_of: 2026-10-28; DIS reuses existing data (market data as_of: 2026-10-28); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-05
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-28

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-05
- Revenue (latest available single quarter): 25,248,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 2,638,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1744489/000174448926000057/dis-20260627.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimAFBVV95cUxQZGhWalpQSjhncTE1ZEsyRy1KTHNXQ18yX0FRNlV6ekUyM1l1TzVOYUlfVFNiaFc3a256TFFVY3lwWXo4VGl5UElMalZYb3FMNHRDWjNZQWpBV3p4aVdpUmV4V1VzZlUyM1VHNEdaTlpMY3k2N3lESEpkb1ZVRWVlWkR5QTBLQ1JIYWNTTHRJV3pxanYwTi1NcA?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQOEdDdXl2bGNjMmg5WEs1T0I2RjE1V1lrdlpTR1hfYmYxa0EwT3NxN1lOUTdmVmpwc0tRRnVZcUI4QUV5dko3RGhnTmxkc1N4d3hFMTQ1UmpkM2xCSVVJUlA1b1NXSnpQUHZpUGFJSU53blZwVjl3QlJCczk2SkpkSmFYOUFycUdUWmQzTmpvZ0ItQ0ZRZ21JVk9MNS1fRWM?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQMldKcDFFX2poOGxTdDBWdGEwSS1tRlI0NUVGaHYtNlVIazlqMFVTempwSlBpbV9uR2sxZDhOTzlKX3cxRFhldjFFa3FNc2d5M0dpdE9YX1hpeFZCWHQ3SGg5NFNpek5fSHBkUDdtWWJLVjUzVGJJWXU5LVZGMEtISmlJbkVoczMzbXl6Yk5wZ0U5dl9RSTlkNGZHVlAyTHliSXc?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQRkwzeUFCNXMtMzV6T2hVRXVmYVhhWVlfbnRUbHJQY1RHcHU4M1Bvd05fQ1hOV1hWVmFhcFV4bkRWY3hDZmdKOHUzWW5mYjZ5RVBkdGtHM1hDejkzc1I5STZBb1RRNjQzd0ZFN1RUa2hEWXdhcHVRTV81azZlVlJYMzRMZ0YzQTdWOW0zV2hPaldXQVlPSnd3OGVUbThvcC1t?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQTTM0MEdOT2hXVGFBWU9rLW5FMS1pU2NnSHdBWmlmQjBsYlRlQmx6ZkZ6U0pIWU5FTU5Ncy1xQW4waUdVWnk4cFpGY1M0eDNFcnhCU205emoyQ05zZ0xiRHhGbmtrb09TSGpiX3NWLVpKS0RlektrWGl6VnpjRzhtNF94QnhUNFhZNkJySUJYdzhpMEpPMFB0Sk42YVFyTjhv?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPQ3gxelZ2T29IdUFpdHVkZ0pMdGFWX0ZpRnlUcWJKczduQXl6N2JwQTM1M2wtc3VlQ3BaNVRZZjRHUmQ4dll6V0FBVlU2ZG5VYWdNNkxQa01BU2w0TVJpNDRobjZCN1VpQ3lMOUpuXzRub0Y5OFpTMEZJd0pCYUNDdnFHZGNzck9TM3d4UEJ4WXF3VWozR1JUZWtHOA?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPZ294WFdGSTBPODM0MVEySGh1SnZnelZtSFNOT0xkTWNEUHZhZU5GREVGbERDUDd6ZlVQczROYTNTUGstaXE2amY2d3R4RU5hZHBab2FOYS1ZLWdZb3ozQXk5VGdDLVpsSDBHLWxSZHZ4OHVpbV84QVgzeDQ0VXJ1Sjd4aTl2bDFQOTFTR1dvTmo0MmJteURiLTJR?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQM0xtYVgyMVRPTHBvQjN3M0pjdDZXTW9DcUlIU3dIRmZGdHpLeDFqeWppU3Z2Uk1tTkpMRExrb3daWklXc0UtSzhPa3NXcGU4elVnRlRaQlpYS1hoSThCRzNxeW5Wb1hwWUxKc3F1UDljemxhNEVac1RKclRVRm5xLVFfdHZzOHFPeGZqRw?oc=5
- https://news.google.com/rss/articles/CBMi6AFBVV95cUxOaGh3SUVLS3MzejhVU085TEIwNFVIUU9laUZ5UWtEY01xcS13RHdyWkRVN3kyaDRRMWVLQzNNUGFoWTZ0enI2Nnp2bnBUTVItUUR0ZXJXbjdfWFo3Tm81a3FScmFHZ0U4eFlUeDZaUnFwRjhKQ0RoLUhNZWdjbTZmTzRMVjU5VzlhQmRUYV9fUGt6YTBiaUNBR1ljUzlvZng3djNzaVgxM3kxaTlrWkcwQmlKdXlxdWhkOTNwTU94VFEwZXFTSVc0Xy1zOVhRUE1jQXc4a2t0S05LdFVndXlXdlphbkxSZENt?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPR1h5SUU0LXFib0pMaUxjOE9VR0Z1ZDhhWUhycl9YYXFlV2s1Ml80bHhBWm9oRllXTVNGNEoxUkVabW50VjVvaEx1dTgxZUIxdEkyamllVkE5QjM2Qmh1bVJNR3NnZW12YllJNGE5VEZhUDJ3dVFudGVjd2hTSmtBaUVoWnJjNXYzcWxTamxobG5pX3Z4Tlh6VWR2eFpNZkhaWUlYLTkxZFVNYXNKWDBtWnlLV1J5SmR0U3RsOUR3Qk04Z9IBxwFBVV95cUxNeGhLcHdfSmNlRFhESm16X3pkUmVIUEhpZVVsNzRjWWR5UGNsREJnZVU4TGRtVmtyZW5vNV9za054aVAtTHkzaEVfdWp1QmVSV2pPd1R6NVNiZjdHV0RwV182U3JfSldqQ3FSQXFyQlFZVXZET0ctQ0NxRDRibnViZHlpWUNXR1ZBdm9MVU9WeUFfbTdwdktOS3I5WjJjdXFFMUN0cFh6Y2R5U3l0QzNNdExuWkxsUEw5ajJ5eDVmazVha2dOVkpB?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxPbmZUeHNOZkh6OFdld0NnVnVfUE1NbVJGMXJjNzNaQXpUQlJzbUV0b1dNeFQwNzl3dV9NdXhjb203eGpONGI0VGI4ZHRrN2g4VDQtWlJwc3hWVXFhcC1NbDRmLTRmMXdsR2NVTjNhSFNBTnNMdUZGX3dvcHdxRW5PN3RJMV9HQngtYUprYzByWVZrQ0NyNlR0VXgwWHpvNkJETU9iX05KX3FLMllReW9Wb1pGLWhBMkxhZXpJM2ZMSUdKdU5wZWZB0gHHAUFVX3lxTE9uZlR4c05mSHo4V2V3Q2dWdV9QTU1tUkYxcmM3M1pBelRCUnNtRXRvV014VDA3OXd1X011eGNvbTd4ak40YjRUYjhkdGs3aDhUNC1aUnBzeFZVcWFwLU1sNGYtNGYxd2xHY1VOM2FIU0FOc0x1RkZfd29wd3FFbk83dEkxX0dCeC1hSmtjMHJZVmtDQ3I2VHRVeDBYem82QkRNT2JfTkpfcUsyWVF5b1ZvWkYtaEEyTGFlekkzZkxJR0p1TnBlZkE?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOYlBMWmx5TjRucnVzN1dpOVN4dG9wRFJFdEF0NHRkX1FhMnpLVmpiai1oTXI4VUtTSXdrdmF1N2gzQjZDX3l6UjJKb2U5M3V4NDcxNEJFdVVYTF8ySkJxZkY1ZEtrNmdoQXBhVXlLTDFIY2dMcmdoN19XVE5UVHBsbUN3N3NKLTJOdGF5ZWxJOGVoYWVldVI4?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
