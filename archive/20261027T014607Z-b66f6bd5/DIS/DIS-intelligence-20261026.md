# DIS Intelligence Report

- ticker: **DIS**
- Report as_of: **2026-10-26**
- Market data as_of: **2026-10-26**
- Quant sources: https://finance.yahoo.com/quote/DIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/DIS/key-statistics/
- AI analysis snapshot as_of: **2026-10-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-27T02:01:56.761797+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 13, 'rule': 0, 'ai': 9, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261026T005504Z-6368ad31/DIS** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 13 unique headlines; 8 named publishers; 0 exact duplicates; 13 HTTPS source links; largest publisher share 30.77%; oldest publication 2026-10-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 110.4000 |
| Return 1D (%) | -1.8841 |
| Return 1W (%) | 0.7391 |
| Return 1M (%) | 4.0038 |
| Return YTD (%) | -2.2186 |
| Return 1Y (%) | 0.2853 |
| Annualized volatility (%) | 26.9626 |
| Beta vs SPY | 0.6192 |
| Max drawdown (%) | -20.2451 |
| Sharpe (rf=0) | 0.1235 |
| Downside deviation (rf=0, %) | 19.2770 |
| Sortino (rf=0) | 0.1727 |
| Historical VaR 95% (1D, %) | 2.4126 |
| Historical ES 95% (1D, %) | 3.7715 |
| Correlation vs SPY | 0.2920 |
| Tracking error vs SPY (%) | 26.2378 |
| P/E (trailing) | 22.76 |
| P/B | 1.74 |
| EV/EBITDA | 11.37 |
| Revenue growth (%) | 6.80 |
| Forward P/E (estimate) | 14.73 |
| Gross margin (%) | 37.59 |
| Operating margin (%) | 19.30 |
| Return on equity (%) | 8.01 |
| Free cash flow yield (%) | 2.55 |
| MA50 | 106.9662 |
| Close vs MA50 (%) | 3.2102 |
| MA200 | 103.0661 |
| Close vs MA200 (%) | 7.1157 |
| RSI (14, Wilder) | 57.3961 |
| MACD (12,26) | 1.8128 |
| MACD signal (9) | 1.4358 |
| MACD histogram | 0.3771 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'DIS': 268, 'SPY': 268}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 110.4000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.8841 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.7391 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 4.0038 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -2.2186 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 0.2853 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 26.9626 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 19.2770 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.1727 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4126 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.7715 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2920 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.2378 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6192 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.2451 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1235 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 14.7274 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 37.5950 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 19.3010 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 8.0100 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.5497 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.7629 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 57.3961 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.3771 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.2102 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 7.1157 -> Clearly above the moving-average trend level.

## TAILWINDS

### Walt Disney (DIS) Rises As Market Takes a Dip: Key Facts
- Summary: Disney stock rises as market dips, indicating a positive market move.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQZGhWalpQSjhncTE1ZEsyRy1KTHNXQ18yX0FRNlV6ekUyM1l1TzVOYUlfVFNiaFc3a256TFFVY3lwWXo4VGl5UElMalZYb3FMNHRDWjNZQWpBV3p4aVdpUmV4V1VzZlUyM1VHNEdaTlpMY3k2N3lESEpkb1ZVRWVlWkR5QTBLQ1JIYWNTTHRJV3pxanYwTi1NcA?oc=5>

### Disney (DIS) Stock Looks Reasonably Priced After A 43% Gain
- Summary: Stock appears fairly priced following a 43% gain.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQOEdDdXl2bGNjMmg5WEs1T0I2RjE1V1lrdlpTR1hfYmYxa0EwT3NxN1lOUTdmVmpwc0tRRnVZcUI4QUV5dko3RGhnTmxkc1N4d3hFMTQ1UmpkM2xCSVVJUlA1b1NXSnpQUHZpUGFJSU53blZwVjl3QlJCczk2SkpkSmFYOUFycUdUWmQzTmpvZ0ItQ0ZRZ21JVk9MNS1fRWM?oc=5>

### Disney (DIS) Ticks Higher to $111.83 as Shares Sit Mid-Range - Put Wall
- Summary: Shares rise to $111.83, indicating a modest positive market move.
- Date: 2026-10-22 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPMDFfZFZhb182SmwtMlREdGlEbHhsX3RjLTN4ZTVFS2FieTItOTRsZ1NuTi1yWUlqWTM4dmE3M2FPNjg4QXJIc3FXZzV2WXhSUGkzbXJocDFWeTNpQk9pZnZseXVLZUZSOF9HRC1wUHNucUZzRnlST0JCWEhoTFMyRmJJQ0ZzQmNPczRaVjB1cWxxV2V4SFRNbzh0bXo4QQ?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Disney (DIS) Stock May Be Near Fair Value Despite AI Asset Bid
- Summary: Disney stock appears near fair value amid AI asset bid concerns.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPR1h5SUU0LXFib0pMaUxjOE9VR0Z1ZDhhWUhycl9YYXFlV2s1Ml80bHhBWm9oRllXTVNGNEoxUkVabW50VjVvaEx1dTgxZUIxdEkyamllVkE5QjM2Qmh1bVJNR3NnZW12YllJNGE5VEZhUDJ3dVFudGVjd2hTSmtBaUVoWnJjNXYzcWxTamxobG5pX3Z4Tlh6VWR2eFpNZkhaWUlYLTkxZFVNYXNKWDBtWnlLV1J5SmR0U3RsOUR3Qk04Z9IBxwFBVV95cUxNeGhLcHdfSmNlRFhESm16X3pkUmVIUEhpZVVsNzRjWWR5UGNsREJnZVU4TGRtVmtyZW5vNV9za054aVAtTHkzaEVfdWp1QmVSV2pPd1R6NVNiZjdHV0RwV182U3JfSldqQ3FSQXFyQlFZVXZET0ctQ0NxRDRibnViZHlpWUNXR1ZBdm9MVU9WeUFfbTdwdktOS3I5WjJjdXFFMUN0cFh6Y2R5U3l0QzNNdExuWkxsUEw5ajJ5eDVmazVha2dOVkpB?oc=5>

### Skydance Rises 5% as Steep Post-Merger Slide Pauses; Disney Gains 2%, Netflix Slips
- Summary: Disney shares up 2% following Skydance rally.
- Date: 2026-10-20 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxOdWxiN2xCcHc3eVhrakhMaEV2eENPdVpaTzVJalNWMjBsTVp4UnpPVFdsTnV2YVY3R0JwTzNRSlRtV2JmUEZzZHZQR0V0d0NkSGplWlhoSy0tWVVid3luUkl3UXJoZnljc19OTlMxWHFkLUMwa0UxOGJFY1Zyek5ibmFER2NBQWhIY2ljV0ZwQm9jbEpGSENNZ3JkSFN2MGRHckxaem11MTlqeVhjMk1USUtZbUt4MGVlRnYwQ2hKbGo?oc=5>

### Disney Stock Rose 10 Sessions in a Row While Bidding $20 Million for Character.AI’s Technology. Here’s Where It Could Go by 2030
- Summary: Disney bids $20M for Character.AI tech, boosting future growth prospects.
- Date: 2026-10-26 | Impact: high | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPZ294WFdGSTBPODM0MVEySGh1SnZnelZtSFNOT0xkTWNEUHZhZU5GREVGbERDUDd6ZlVQczROYTNTUGstaXE2amY2d3R4RU5hZHBab2FOYS1ZLWdZb3ozQXk5VGdDLVpsSDBHLWxSZHZ4OHVpbV84QVgzeDQ0VXJ1Sjd4aTl2bDFQOTFTR1dvTmo0MmJteURiLTJR?oc=5>

### Disney (DIS) Ticks Higher to $111.83 as Shares Sit Mid-Range - Range Breakout
- Summary: Shares rise to $111.83, breaking out of mid-range, indicating short-term bullish momentum.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPNUxaLTBMY2FMNTVyS3dzS2JMRHRjWkRkUk1ZRnVZVzBrT1Y1a1dpbHM3b2htRTRMbzVHa1VBc05PN2VPUTZ1c3VuZUczdnpXUUVCNUMxeFd3R191cHUyVzlPRFpDOGxtVHVGbHgwSFRBYjRSZVNyb002ZWowZ3g3THVCTV95V3dMSnFlU0Z4TF96RU1fX3ZRczFuRGV6czdp?oc=5>

### Disney Stock (NYSE:DIS) Gains After Hiring Character.AI Staff
- Summary: Disney's stock gains after announcing new hires from Character.AI, boosting workforce strength.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxOcUZnSmNVMGZjOU9UY2xZM0RMWmt3cmtlak9IbFp5c25MX3pmbVgzZUIzM3AyTTRBQXZzeWxFRExFY0d1WXM0dzM0cHhTaklKaXptTU5YQktUVjlEb3AzTW1LSmU5eDdVOTlqa08yZVF6QW9JemVKX0J5TDJrUG1NNUprUjBBdTIxMGVKSUdyc1plUQ?oc=5>

## RISKS

### Walt Disney (NYSE:DIS) EVP Brent Woodford Sells 2,856 Shares of Stock
- Summary: Executive sale of 2,856 shares may signal internal concerns.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxQSGptZm44bktNcG5aTTNNcnhCVFNHUl9XLVFQSlRxSkVUb1FweExYNWRNV1R6Q3M4MmN0S0pmLWxhNkpQcXdpUTR0dDRCX1hQTnd1d3Z0clVWS2M2a0ZWQXZ4TmI0MjgyOFRxZGVOUm5oczl1UndWSWVOR0drWVJGa0pLQlpYSnBKSEY0RDdfMWp1YV9ZdFA2cm1VZEZLeXltXzFpSThTYjVtVXJCWE41R0tndF9uV1MzblpRNG1BMWIwaU1oRnJz?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **DIS** | **22.76** | **1.74** | **11.37** | **6.80** | **190,626,234,368.00 USD** | **0.29** |
| NFLX | 18.47 | 8.96 | 17.03 | 11.80 | 266,075,750,400.00 USD | -41.63 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| PSKY | N/A | 0.93 | 7.95 | 0.90 | 10,992,190,464.00 USD | N/A |

Peers fetched as_of: 2026-10-26; DIS reuses existing data (market data as_of: 2026-10-26); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-05
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

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
- Filing date: 2026-08-05
- Revenue (latest available single quarter): 25,248,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 2,638,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1744489/000174448926000057/dis-20260627.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimAFBVV95cUxQZGhWalpQSjhncTE1ZEsyRy1KTHNXQ18yX0FRNlV6ekUyM1l1TzVOYUlfVFNiaFc3a256TFFVY3lwWXo4VGl5UElMalZYb3FMNHRDWjNZQWpBV3p4aVdpUmV4V1VzZlUyM1VHNEdaTlpMY3k2N3lESEpkb1ZVRWVlWkR5QTBLQ1JIYWNTTHRJV3pxanYwTi1NcA?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQOEdDdXl2bGNjMmg5WEs1T0I2RjE1V1lrdlpTR1hfYmYxa0EwT3NxN1lOUTdmVmpwc0tRRnVZcUI4QUV5dko3RGhnTmxkc1N4d3hFMTQ1UmpkM2xCSVVJUlA1b1NXSnpQUHZpUGFJSU53blZwVjl3QlJCczk2SkpkSmFYOUFycUdUWmQzTmpvZ0ItQ0ZRZ21JVk9MNS1fRWM?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPMDFfZFZhb182SmwtMlREdGlEbHhsX3RjLTN4ZTVFS2FieTItOTRsZ1NuTi1yWUlqWTM4dmE3M2FPNjg4QXJIc3FXZzV2WXhSUGkzbXJocDFWeTNpQk9pZnZseXVLZUZSOF9HRC1wUHNucUZzRnlST0JCWEhoTFMyRmJJQ0ZzQmNPczRaVjB1cWxxV2V4SFRNbzh0bXo4QQ?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPR1h5SUU0LXFib0pMaUxjOE9VR0Z1ZDhhWUhycl9YYXFlV2s1Ml80bHhBWm9oRllXTVNGNEoxUkVabW50VjVvaEx1dTgxZUIxdEkyamllVkE5QjM2Qmh1bVJNR3NnZW12YllJNGE5VEZhUDJ3dVFudGVjd2hTSmtBaUVoWnJjNXYzcWxTamxobG5pX3Z4Tlh6VWR2eFpNZkhaWUlYLTkxZFVNYXNKWDBtWnlLV1J5SmR0U3RsOUR3Qk04Z9IBxwFBVV95cUxNeGhLcHdfSmNlRFhESm16X3pkUmVIUEhpZVVsNzRjWWR5UGNsREJnZVU4TGRtVmtyZW5vNV9za054aVAtTHkzaEVfdWp1QmVSV2pPd1R6NVNiZjdHV0RwV182U3JfSldqQ3FSQXFyQlFZVXZET0ctQ0NxRDRibnViZHlpWUNXR1ZBdm9MVU9WeUFfbTdwdktOS3I5WjJjdXFFMUN0cFh6Y2R5U3l0QzNNdExuWkxsUEw5ajJ5eDVmazVha2dOVkpB?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxOdWxiN2xCcHc3eVhrakhMaEV2eENPdVpaTzVJalNWMjBsTVp4UnpPVFdsTnV2YVY3R0JwTzNRSlRtV2JmUEZzZHZQR0V0d0NkSGplWlhoSy0tWVVid3luUkl3UXJoZnljc19OTlMxWHFkLUMwa0UxOGJFY1Zyek5ibmFER2NBQWhIY2ljV0ZwQm9jbEpGSENNZ3JkSFN2MGRHckxaem11MTlqeVhjMk1USUtZbUt4MGVlRnYwQ2hKbGo?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPZ294WFdGSTBPODM0MVEySGh1SnZnelZtSFNOT0xkTWNEUHZhZU5GREVGbERDUDd6ZlVQczROYTNTUGstaXE2amY2d3R4RU5hZHBab2FOYS1ZLWdZb3ozQXk5VGdDLVpsSDBHLWxSZHZ4OHVpbV84QVgzeDQ0VXJ1Sjd4aTl2bDFQOTFTR1dvTmo0MmJteURiLTJR?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPNUxaLTBMY2FMNTVyS3dzS2JMRHRjWkRkUk1ZRnVZVzBrT1Y1a1dpbHM3b2htRTRMbzVHa1VBc05PN2VPUTZ1c3VuZUczdnpXUUVCNUMxeFd3R191cHUyVzlPRFpDOGxtVHVGbHgwSFRBYjRSZVNyb002ZWowZ3g3THVCTV95V3dMSnFlU0Z4TF96RU1fX3ZRczFuRGV6czdp?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxOcUZnSmNVMGZjOU9UY2xZM0RMWmt3cmtlak9IbFp5c25MX3pmbVgzZUIzM3AyTTRBQXZzeWxFRExFY0d1WXM0dzM0cHhTaklKaXptTU5YQktUVjlEb3AzTW1LSmU5eDdVOTlqa08yZVF6QW9JemVKX0J5TDJrUG1NNUprUjBBdTIxMGVKSUdyc1plUQ?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxQSGptZm44bktNcG5aTTNNcnhCVFNHUl9XLVFQSlRxSkVUb1FweExYNWRNV1R6Q3M4MmN0S0pmLWxhNkpQcXdpUTR0dDRCX1hQTnd1d3Z0clVWS2M2a0ZWQXZ4TmI0MjgyOFRxZGVOUm5oczl1UndWSWVOR0drWVJGa0pLQlpYSnBKSEY0RDdfMWp1YV9ZdFA2cm1VZEZLeXltXzFpSThTYjVtVXJCWE41R0tndF9uV1MzblpRNG1BMWIwaU1oRnJz?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
