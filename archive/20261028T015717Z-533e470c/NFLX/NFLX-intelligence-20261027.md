# NFLX Intelligence Report

- ticker: **NFLX**
- Report as_of: **2026-10-27**
- Market data as_of: **2026-10-27**
- Quant sources: https://finance.yahoo.com/quote/NFLX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NFLX/key-statistics/
- AI analysis snapshot as_of: **2026-10-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-28T02:04:32.856693+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 7, 'ai': 9, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261027T014607Z-b66f6bd5/NFLX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 8 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-10-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 62.5200 |
| Return 1D (%) | -2.1596 |
| Return 1W (%) | -8.9824 |
| Return 1M (%) | -12.1293 |
| Return YTD (%) | -33.3191 |
| Return 1Y (%) | -42.8812 |
| Annualized volatility (%) | 35.9221 |
| Beta vs SPY | 0.2102 |
| Max drawdown (%) | -45.9870 |
| Sharpe (rf=0) | -1.3853 |
| Downside deviation (rf=0, %) | 26.4492 |
| Sortino (rf=0) | -1.8814 |
| Historical VaR 95% (1D, %) | 3.5133 |
| Historical ES 95% (1D, %) | 5.1308 |
| Correlation vs SPY | 0.0743 |
| Tracking error vs SPY (%) | 37.2007 |
| P/E (trailing) | 18.07 |
| P/B | 8.77 |
| EV/EBITDA | 16.67 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 16.58 |
| Gross margin (%) | 50.69 |
| Operating margin (%) | 34.63 |
| Return on equity (%) | 53.46 |
| Free cash flow yield (%) | 9.79 |
| MA50 | 73.7128 |
| Close vs MA50 (%) | -15.1843 |
| MA200 | 82.0071 |
| Close vs MA200 (%) | -23.7627 |
| RSI (14, Wilder) | 31.1265 |
| MACD (12,26) | -2.2636 |
| MACD signal (9) | -1.7512 |
| MACD histogram | -0.5124 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NFLX': 269, 'SPY': 269}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 62.5200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.1596 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -8.9824 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -12.1293 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -33.3191 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -42.8812 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 35.9221 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.4492 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.8814 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.5133 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1308 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0743 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.2007 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2102 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -45.9870 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.3853 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.5777 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.6850 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 34.6320 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 53.4630 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 9.7860 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.0694 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 31.1265 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.5124 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -15.1843 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -23.7627 -> Clearly below the moving-average trend level.

## TAILWINDS

### Netflix (NFLX) Stock Stays Cheap After Its 58% Three Year Gain
- Summary: Netflix (NFLX) Stock Stays Cheap After Its 58% Three Year Gain
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOVmpXNWh4OWZNOUI5d0lnd1NGYzBBU2tLSFhPeDY3UFpFM1ZXODVVdzNuMy1CM1pMelUxdFZEQ25XVW5NMHlPYnZ1WFZ3RXZXbXB6aDg2eFpWNUF5RC1KWUFJc2dmMHlkbkJQY1k2Z2JLb25RY0J6cURXR2hxV1AzZDZMM0dvWW84WHFIalR2Q05pbDZzMlBpekhKdw?oc=5>

### Netflix: The Ad Miss Is Offset By Record Buybacks
- Summary: Record buybacks counteract ad revenue miss, supporting financial health.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOQUVBS2FkdDBjMEpaN2tqRm00OG1WOEJFUnFTMHctQWVVamxSOFdhUkdnLWhqVi1wZ1VOUXRuNGNJOTV2LUpmcW9OSXdFTVRfcFJUb19CWEl1ek1MU1RXcTlhRzU1M0cxWnRWbzh3dGk0S2VIcXh0STRiRkRiVHdfN0hncFFpVHVuXzlTRjgwcTAtMG8?oc=5>

### The Truth About Netflix’s Massive Stock Buybacks
- Summary: Netflix’s large stock buybacks signal confidence and may support share price.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQVEUtMFZRVENHVjlINnNTTjVST0htSWJnMFlKNEY1V2FtNWRQUDFMenlrNTRRVWd3N3FyUXNmRXdVVlQ2TkxrbXZEZDNxSGZlbTVUSjZFcTM4MGt4X0tUM2k4NUw4a0FySWdBOFBqNENTVmw3b0drSDJFRjhIcVotSGJNNEthSjUxTExuaFVfdy1WS3Bkbk85RFZibEh3a0pFa3A0?oc=5>

## HEADWINDS

### Netflix (NFLX) Stock Price Falls As Q3 Earnings Stir Valuation Doubts
- Summary: Netflix (NFLX) Stock Price Falls As Q3 Earnings Stir Valuation Doubts
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOVmRBaFZXZGZad2d5SGVQS2J4c2xPOTdpNjNqRmlQWXliMWpIVFdpV2RsSlZ1NHRiUFBtZ0hQbGxDS2U3bjBSNE5pR2hlUFNPY3Y4YVp2LUhsRHlvZ1dhemdCc2twWXJYX2JBZm1ELU5fRGJVWnpFOTlQcU5sOGlGZl9qazJhajZTaFRqWnQ4X3kxVTBqWXFyMDdKRQ?oc=5>

### Netflix Drops 4% as Engagement Worries Outweigh Earnings Beat; Disney and Spotify Slip
- Summary: Netflix Drops 4% as Engagement Worries Outweigh Earnings Beat; Disney and Spotify Slip
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQRElvSkJSVnJ6NkNVSmN5TU15dmtGemdCRWFwRE0tcGtvUmxxbXBpOXIybUltTENZZDBtNm1aVjM0bFVJX1UxeVRVV0xYSjFrS1Y4WXY1U3psN3pzcmxvdkNhY1JUb3B1bTJIYVN6LURRS3lTRDM5bHhxSmkxOElpTzgxaUNpNktOeHQ2aEdyWTc2UlhDSkNWOVBqbXpHUlR3?oc=5>

### NFLX Stock Slips More Than 6% Premarket: Morningstar Sees 'Best Buying Opportunity' For Netflix Amid Negative Sentiment
- Summary: NFLX Stock Slips More Than 6% Premarket: Morningstar Sees 'Best Buying Opportunity' For Netflix Amid Negative Sentiment
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNYXVuTzRUeVNQZHhoTUpSZzg5aEE4VnhPYWh5YVQ4UmplQ1B4T1ktSDN5aHpMVFY2cm01QnRGS2FWWWxSMmlOTmYxS2kyaWVCZHdDZ0Q0NC1Bd1JGWG54cVdBdDktWnJKMEJZVldCOGRaUVhCQkdNYjBMTVNxakdjYjRyZFVSRUNrX3BrbERTUXJmdw?oc=5>

### NFLX Stock Tumbles Overnight: Co-CEO Wants Netflix To Be Last Service Customers 'Ever Cancel', Says Live Events 'Drive New Membership'
- Summary: NFLX Stock Tumbles Overnight: Co-CEO Wants Netflix To Be Last Service Customers 'Ever Cancel', Says Live Events 'Drive New Membership'
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNVTBxOTVRYmtvSHVoYlluTGwyQjZNR3ZEeHZ2Nno3SzNmaHFPQ2YxMTU1enN6aExMMW1rRVg2dC1oQ1Z1WjJCcGNHVDhVUUJpWWJEOVFfZnRpUXpKYWVYTmRsclE3ZjJiY2dNZ0NxSGswb25zTy1xSzBHRmNKWjlzOVduNTRKRXRXeEtBS3RCRG81RTg4VXNPMHBKWTg?oc=5>

### Down Roughly 50% From Its Highs, Is Netflix Stock Finally a Buy?
- Summary: Stock price has dropped 50%, questioning buy potential.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPaUxsUFM0YmRJeEtMU3VUTG1kT0FEMVpHckhVenVyMXZ5Y25YZFlhWGc5SklnZWJJNHljMzA0NmlGTGdTU3VYTUtlenBKcFhLcXhYN0MxdGVyQkk4eDZfQU9WZ3hOelJoU01ocnQ3UEQ0R0ZNWWRiSEZIOERkaTBoMnMtY3Jnam9CaTlKMk41OGpPMVdl?oc=5>

### Netflix Is Now Down 29% This Year: Is NFLX Stock Hopeless or Ready for a Rebound?
- Summary: Netflix shares fell 29% YTD, raising concerns about future growth and valuation.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxQLUd5d2xvbWNXbkpvYmY3VmhEYUtsbU83V2VIMnptYW5WbUNMZ1dibkJmZEwxYUg0RXhmOWRQZ0t6aW5RaTNoUkQ4Y3ZEZ3FaU2FGSjl2VC1uQlE3bkNnVUtaNi1DY1RzS05zeE55ZGNuS2UtYmlSbTR2ZDlqRXNvaTF1V3QyalNmNkdYN3JsTU50bDZwNXFvR0FVajlpODFvWlZrSGlpYmhDRTg0a0RkWTRLWXFFdzg1YmxZc3RFSQ?oc=5>

### Netflix stock price is down 32 per cent this year: What led to this downfall? Check predicted target price, market value
- Summary: Netflix shares fell 32% YTD, raising concerns about valuation and growth.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingJBVV95cUxQMHV6eVZzRlhXZkJNVXlRTzlGb1dDVGNQdHdqbXctakc3dkJqX0IwdnVXbXpLVUFja09KM3Z2LURKV29JODg0cWlId0xBS1FJSFRtUVVtbExGSllTYjhYTU5DdTJwcXFoUy1HSVBZTnRKTkIzMW9DUzF1a0lKVzZZUDJOU1l5dzJJUkRsNEpyYnhzcnpfREszMTVMTUM1OFU4YkZvU2J1RmZNQnRKZjZZSnNuR19ucWdxZDVPQ1k2OGkyR1Zsd2Nkenp2blVGNF9nQ2NVMWtURlNaS1paYXY5dWtTeWJBa3NISWdGUEZRZzZENGVXMHlBeDItVWlxdWpPMktEUFJ3Q3I1MDl3dFhzVEtLdl9tbmd3YVdsTmJB?oc=5>

### Netflix Is Down 51% From Its High. History Suggests This Is What Happens Next.
- Summary: Shares dropped 51% from peak, hinting at potential further decline.
- Date: 2026-10-25 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPZTg4c2VtT2d1SV9meTFhZFpzN2ItRk85YXlQWnAwQUxDRm5VMmhBU0RrVXAyRWROcWk4RUpFdk4yWlhkc3dlUjFyU3hkVDVkaklFNC0zTmRPRmJZNHQxN2xvYmQtMVlDVm9Bd2VJdkZIOEI1Mnh0blZMNEJ4d0FGOXBvY25ic1UwV2NYa2ZPcw?oc=5>

## CATALYSTS

### Netflix (NFLX) Stock Fair Value Falls After Cautious Q3 Analyst Revisions
- Summary: Netflix (NFLX) Stock Fair Value Falls After Cautious Q3 Analyst Revisions
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQSE1oLXBDN2dSRUZabVZhbzJvTDZpSVV3NmNVQ2VlYjJJQVVRSTBfQmJHT2FhWGt6LUl4NjFBMElxaVFGajh2eWlIRm1abUp2cFVoekg1VGdZN0pmbGV2ckZjWXB2ZzcwRWV2RkZ6S1pqVTBFNjRuamREVk5RMkoxZUw5ZjZyQXg1SDNHdzRIWDhweXJYTGpacC1R?oc=5>

### Netflix Stock Tanks 5% as Revenue Growth Slows in Q3. How to Play NFLX Here.
- Summary: Netflix Stock Tanks 5% as Revenue Growth Slows in Q3. How to Play NFLX Here.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPUU4zX0ktN0t1V3gyYkZ1NEY0SmkzdUozTl90UTRxU0ZBZmZDUDhzWEZJbjViZmxGMnpJbTdOWlpTam4zczktWnlJaW5lSFllOTRYS05iVFkwMUNfNmNWOHE5LUVHbVM5SUNhSzFpdkJaYmpsY2NwZlhCSTNIMFBHNnFwRXo4WERtbjRGaXRSOFYwdHNjVmVLSWRIcG9zU25GdG1RQ2t5WUhjc1Q0X29QdEpJQWxaVC1o?oc=5>

### Why Netflix (NFLX) shares are falling today
- Summary: Explains factors behind today's decline in Netflix stock price.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQMi1rUzE5c3J6OEZESUJ3RmhEZkNsYldiRXMxRDRBX1g1eFRLd2pZQ3dHUl9ZZDFlVF9KYlk0OThYS3Q2bG9mVGtYWUIxTUhYdFNRVF83bUtFemNmQ29xSk1vd1ZQUURvbWJVMjEtdnEzUWl1cW0yRmE1LVNWYUZzamNCbEVDamFZeFczblY0ZHdzU0JZLXRBNEM0RjQ?oc=5>

### Why Netflix Stock Dropped Today
- Summary: Details reasons for the recent drop in Netflix shares.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQVW92S2lTTzBKRUp2ejdoX1MzMGVGZTQzTFJ0Qk51WFI2SEVIMEJDQ25SUm8xcTZaZ0ROaml0WVF5RHptLUM2UDI3Wmg0SXowX2Rhazd0X1BUSWUwLXpMemxwc09mTUtMQmFrUWUwQmxkZW5CcmFjYl9DVVJYZEJyRmMxV1htWm5oVEwyVU8tYjNIZXp0VzN0UlZKb0s?oc=5>

### Here’s How Much Traders See Netflix Stock Moving After Earnings
- Summary: Earnings releases are expected to drive significant share price swings.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNOTBOOTBwcXFiX0NRUk9LcVJiUjhyVUh2Vm9pY0l5ZW1ORENMTlJuY1d1Y2MtM1NfVzNtU2pCY2tkaVgwd080WnpvclZDTy0ybXdnRU81M2NWdUMxZUxFWXB5WlRHNlZSamRpbG9pdzFwNXZDemhWQjU1UEhpUGRfLVlJVmM0cTVwR2Z5QzV1SlJMUWUzenBtYWQ0WGI0S0hxWmo4ZkhraGJLMDNzMHBBYjZ3N1lDRWN4TmtONFhBbUM1QQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NFLX** | **18.07** | **8.77** | **16.67** | **11.80** | **260,329,504,768.00 USD** | **-42.88** |
| DIS | 22.73 | 1.73 | 11.35 | 6.80 | 190,332,698,624.00 USD | -0.46 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| CMCSA | 6.91 | 0.84 | 4.70 | -6.10 | 77,553,975,296.00 USD | -16.55 |

Peers fetched as_of: 2026-10-27; NFLX reuses existing data (market data as_of: 2026-10-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-19 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMimwFBVV95cUxOVmpXNWh4OWZNOUI5d0lnd1NGYzBBU2tLSFhPeDY3UFpFM1ZXODVVdzNuMy1CM1pMelUxdFZEQ25XVW5NMHlPYnZ1WFZ3RXZXbXB6aDg2eFpWNUF5RC1KWUFJc2dmMHlkbkJQY1k2Z2JLb25RY0J6cURXR2hxV1AzZDZMM0dvWW84WHFIalR2Q05pbDZzMlBpekhKdw?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOQUVBS2FkdDBjMEpaN2tqRm00OG1WOEJFUnFTMHctQWVVamxSOFdhUkdnLWhqVi1wZ1VOUXRuNGNJOTV2LUpmcW9OSXdFTVRfcFJUb19CWEl1ek1MU1RXcTlhRzU1M0cxWnRWbzh3dGk0S2VIcXh0STRiRkRiVHdfN0hncFFpVHVuXzlTRjgwcTAtMG8?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQVEUtMFZRVENHVjlINnNTTjVST0htSWJnMFlKNEY1V2FtNWRQUDFMenlrNTRRVWd3N3FyUXNmRXdVVlQ2TkxrbXZEZDNxSGZlbTVUSjZFcTM4MGt4X0tUM2k4NUw4a0FySWdBOFBqNENTVmw3b0drSDJFRjhIcVotSGJNNEthSjUxTExuaFVfdy1WS3Bkbk85RFZibEh3a0pFa3A0?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOVmRBaFZXZGZad2d5SGVQS2J4c2xPOTdpNjNqRmlQWXliMWpIVFdpV2RsSlZ1NHRiUFBtZ0hQbGxDS2U3bjBSNE5pR2hlUFNPY3Y4YVp2LUhsRHlvZ1dhemdCc2twWXJYX2JBZm1ELU5fRGJVWnpFOTlQcU5sOGlGZl9qazJhajZTaFRqWnQ4X3kxVTBqWXFyMDdKRQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQRElvSkJSVnJ6NkNVSmN5TU15dmtGemdCRWFwRE0tcGtvUmxxbXBpOXIybUltTENZZDBtNm1aVjM0bFVJX1UxeVRVV0xYSjFrS1Y4WXY1U3psN3pzcmxvdkNhY1JUb3B1bTJIYVN6LURRS3lTRDM5bHhxSmkxOElpTzgxaUNpNktOeHQ2aEdyWTc2UlhDSkNWOVBqbXpHUlR3?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNYXVuTzRUeVNQZHhoTUpSZzg5aEE4VnhPYWh5YVQ4UmplQ1B4T1ktSDN5aHpMVFY2cm01QnRGS2FWWWxSMmlOTmYxS2kyaWVCZHdDZ0Q0NC1Bd1JGWG54cVdBdDktWnJKMEJZVldCOGRaUVhCQkdNYjBMTVNxakdjYjRyZFVSRUNrX3BrbERTUXJmdw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNVTBxOTVRYmtvSHVoYlluTGwyQjZNR3ZEeHZ2Nno3SzNmaHFPQ2YxMTU1enN6aExMMW1rRVg2dC1oQ1Z1WjJCcGNHVDhVUUJpWWJEOVFfZnRpUXpKYWVYTmRsclE3ZjJiY2dNZ0NxSGswb25zTy1xSzBHRmNKWjlzOVduNTRKRXRXeEtBS3RCRG81RTg4VXNPMHBKWTg?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPaUxsUFM0YmRJeEtMU3VUTG1kT0FEMVpHckhVenVyMXZ5Y25YZFlhWGc5SklnZWJJNHljMzA0NmlGTGdTU3VYTUtlenBKcFhLcXhYN0MxdGVyQkk4eDZfQU9WZ3hOelJoU01ocnQ3UEQ0R0ZNWWRiSEZIOERkaTBoMnMtY3Jnam9CaTlKMk41OGpPMVdl?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxQLUd5d2xvbWNXbkpvYmY3VmhEYUtsbU83V2VIMnptYW5WbUNMZ1dibkJmZEwxYUg0RXhmOWRQZ0t6aW5RaTNoUkQ4Y3ZEZ3FaU2FGSjl2VC1uQlE3bkNnVUtaNi1DY1RzS05zeE55ZGNuS2UtYmlSbTR2ZDlqRXNvaTF1V3QyalNmNkdYN3JsTU50bDZwNXFvR0FVajlpODFvWlZrSGlpYmhDRTg0a0RkWTRLWXFFdzg1YmxZc3RFSQ?oc=5
- https://news.google.com/rss/articles/CBMingJBVV95cUxQMHV6eVZzRlhXZkJNVXlRTzlGb1dDVGNQdHdqbXctakc3dkJqX0IwdnVXbXpLVUFja09KM3Z2LURKV29JODg0cWlId0xBS1FJSFRtUVVtbExGSllTYjhYTU5DdTJwcXFoUy1HSVBZTnRKTkIzMW9DUzF1a0lKVzZZUDJOU1l5dzJJUkRsNEpyYnhzcnpfREszMTVMTUM1OFU4YkZvU2J1RmZNQnRKZjZZSnNuR19ucWdxZDVPQ1k2OGkyR1Zsd2Nkenp2blVGNF9nQ2NVMWtURlNaS1paYXY5dWtTeWJBa3NISWdGUEZRZzZENGVXMHlBeDItVWlxdWpPMktEUFJ3Q3I1MDl3dFhzVEtLdl9tbmd3YVdsTmJB?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPZTg4c2VtT2d1SV9meTFhZFpzN2ItRk85YXlQWnAwQUxDRm5VMmhBU0RrVXAyRWROcWk4RUpFdk4yWlhkc3dlUjFyU3hkVDVkaklFNC0zTmRPRmJZNHQxN2xvYmQtMVlDVm9Bd2VJdkZIOEI1Mnh0blZMNEJ4d0FGOXBvY25ic1UwV2NYa2ZPcw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQSE1oLXBDN2dSRUZabVZhbzJvTDZpSVV3NmNVQ2VlYjJJQVVRSTBfQmJHT2FhWGt6LUl4NjFBMElxaVFGajh2eWlIRm1abUp2cFVoekg1VGdZN0pmbGV2ckZjWXB2ZzcwRWV2RkZ6S1pqVTBFNjRuamREVk5RMkoxZUw5ZjZyQXg1SDNHdzRIWDhweXJYTGpacC1R?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPUU4zX0ktN0t1V3gyYkZ1NEY0SmkzdUozTl90UTRxU0ZBZmZDUDhzWEZJbjViZmxGMnpJbTdOWlpTam4zczktWnlJaW5lSFllOTRYS05iVFkwMUNfNmNWOHE5LUVHbVM5SUNhSzFpdkJaYmpsY2NwZlhCSTNIMFBHNnFwRXo4WERtbjRGaXRSOFYwdHNjVmVLSWRIcG9zU25GdG1RQ2t5WUhjc1Q0X29QdEpJQWxaVC1o?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQMi1rUzE5c3J6OEZESUJ3RmhEZkNsYldiRXMxRDRBX1g1eFRLd2pZQ3dHUl9ZZDFlVF9KYlk0OThYS3Q2bG9mVGtYWUIxTUhYdFNRVF83bUtFemNmQ29xSk1vd1ZQUURvbWJVMjEtdnEzUWl1cW0yRmE1LVNWYUZzamNCbEVDamFZeFczblY0ZHdzU0JZLXRBNEM0RjQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQVW92S2lTTzBKRUp2ejdoX1MzMGVGZTQzTFJ0Qk51WFI2SEVIMEJDQ25SUm8xcTZaZ0ROaml0WVF5RHptLUM2UDI3Wmg0SXowX2Rhazd0X1BUSWUwLXpMemxwc09mTUtMQmFrUWUwQmxkZW5CcmFjYl9DVVJYZEJyRmMxV1htWm5oVEwyVU8tYjNIZXp0VzN0UlZKb0s?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNOTBOOTBwcXFiX0NRUk9LcVJiUjhyVUh2Vm9pY0l5ZW1ORENMTlJuY1d1Y2MtM1NfVzNtU2pCY2tkaVgwd080WnpvclZDTy0ybXdnRU81M2NWdUMxZUxFWXB5WlRHNlZSamRpbG9pdzFwNXZDemhWQjU1UEhpUGRfLVlJVmM0cTVwR2Z5QzV1SlJMUWUzenBtYWQ0WGI0S0hxWmo4ZkhraGJLMDNzMHBBYjZ3N1lDRWN4TmtONFhBbUM1QQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
