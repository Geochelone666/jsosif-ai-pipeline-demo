# CAT Intelligence Report

- ticker: **CAT**
- Report as_of: **2026-11-10**
- Market data as_of: **2026-11-10**
- Quant sources: https://finance.yahoo.com/quote/CAT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CAT/key-statistics/
- AI analysis snapshot as_of: **2026-11-10**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-11T04:57:53.054517+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 2, 'ai': 11, 'unknown': 0, 'irrelevant': 12})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **12** exact headline/source/date matches; prior report **20261110T055129Z-abd33250/CAT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 14 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-11-05

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 584.5700 |
| Return 1D (%) | -2.3895 |
| Return 1W (%) | -6.3099 |
| Return 1M (%) | -26.7980 |
| Return YTD (%) | 2.9101 |
| Return 1Y (%) | 3.2742 |
| Annualized volatility (%) | 41.4031 |
| Beta vs SPY | 1.8307 |
| Max drawdown (%) | -47.7898 |
| Sharpe (rf=0) | 0.2847 |
| Downside deviation (rf=0, %) | 29.3295 |
| Sortino (rf=0) | 0.4019 |
| Historical VaR 95% (1D, %) | 4.2437 |
| Historical ES 95% (1D, %) | 5.7878 |
| Correlation vs SPY | 0.6045 |
| Tracking error vs SPY (%) | 34.8832 |
| P/E (trailing) | 22.94 |
| P/B | 12.45 |
| EV/EBITDA | 18.03 |
| Revenue growth (%) | 17.30 |
| Forward P/E (estimate) | 18.13 |
| Gross margin (%) | 29.54 |
| Operating margin (%) | 20.19 |
| Return on equity (%) | 56.14 |
| Free cash flow yield (%) | 1.49 |
| MA50 | 750.6298 |
| Close vs MA50 (%) | -22.1227 |
| MA200 | 805.0099 |
| Close vs MA200 (%) | -27.3835 |
| RSI (14, Wilder) | 31.0982 |
| MACD (12,26) | -54.5942 |
| MACD signal (9) | -47.6476 |
| MACD histogram | -6.9467 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CAT': 279, 'SPY': 279}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 584.5700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.3895 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -6.3099 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -26.7980 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 2.9101 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.2742 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.4031 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 29.3295 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4019 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.2437 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.7878 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6045 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 34.8832 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.8307 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -47.7898 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2847 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.1279 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 29.5420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 20.1910 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 56.1350 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.4854 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.9423 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 31.0982 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -6.9467 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -22.1227 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -27.3835 -> Clearly below the moving-average trend level.

## TAILWINDS

### Caterpillar Stock Jumps 7% on Anthropic's $3.4 Billion Deal, With $628.70 Next
- Summary: Caterpillar Stock Jumps 7% on Anthropic's $3.4 Billion Deal, With $628.70 Next
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi-gFBVV95cUxQZ3N5d2hOR2ZJLTYzX2NKUGYzVnRqZ0c5RWJNMUFobWR1Z2xCdlRiaXNpNjBzZWp3U0tRWmF3aTZSZUZPMmxzSTMzcmk3dTRsVGdudmFpSkhjU3MtVmFVcXNza2N6UmExQzJJRGxnMnNvSWQtdklRYnJLYU9JQXNMTVJ1VmRmY2JKOWZBZ3AtWUxlM1V3akpVUTNOV3JjUGpVTzJVdzV0TnNlUk1MQXFSazhNX3NxV0RHcE9NTnNRN2Vfd28zSXpmNUVuYnpIOHJlaktoLVlDd3dDOGJKR1VGUXhvRkRBdGJUbUd6clJkS0FyOHlLYzUyNU93?oc=5>

### Caterpillar (CAT) Stock Looks Undervalued On Future Cash Flow
- Summary: CAT appears undervalued based on projected future cash flow.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxPVGoxYXJOVFIyVTZxQ2FWenNtdDhKM2M4cl9LNkRFdVBOMXg4cVQ2ZU5xcjh2aTV5ZC1lNU9rVkR1ajI5OFdPd2hnSlpHOEQta0Q5Uno5YWd1enBlU09GMUNScWlEZ0tjQnpzQmVnU3JGUnB1a3dIcDF0QTRSYi1HQ01BWGpHVGFvTzZkbXhNWmYxTklmalJmWlpjYjlDQkhQbjN0WjgwMjR0TG02Q293X2tCQWVmOHl4aHdyYTU2Y1NYblB5V2ZlcDl0NE1qd9IB0wFBVV95cUxNblpMSmZtUm9HTUl5YzEyMjl4bW5DWU9kZUhKTVRxbkhaVkM4cmp6MHdTUWFXb1R2X2M0UlBEQ182WFhhOWI3YU5vM0tmWHNUb0ZQYnN3OV9FWWk1UGEyLTdzOEF1V2lNUmg1RjhOT3YyZk9JYl9vYXE4ZXB1VmdiSHVrVnAzbU5ka1BxajJKYm5zMXdrdE1PZl9Pby1HVkZaaVN2TW12aVBPc0dHejFyWEd4UVdBaW1vQ0NhYS1Kamk1TThhWGNHZ3cyVzdfbEVQQUlN?oc=5>

### Caterpillar (CAT) Is Amongst The Notable Names Insiders Are Loading Up On After the Recent Crash
- Summary: Insider buying after crash signals potential upside.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNUy1ZR3NCUUJ3bVh4R3lpOFBkVlAxa0hkaE1peWdVUHR6SXFPZVg3bC1hRldCc1ZWS0xrLTdfSkRoaWxUMzEwcldURzlmMDFSTnllakpmYlRyY0t5Mi1xQjllV1JkY2dkbkVJbGtfNUYzZXJNOVVJbHMzSWRGcWxMRWtyd25oUFR3MnN4YXJIZzJPa2o1Mmp4QkxtSGxlS0doRXFlbw?oc=5>

## HEADWINDS

### Caterpillar Stock Sinks 10% in a Week Despite Record Backlog: Is It a Buy?
- Summary: Caterpillar Stock Sinks 10% in a Week Despite Record Backlog: Is It a Buy?
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQejZtY3VabmQ4VHhlRU9zZ1owV3F5dkpmSWEtYzFGR0dQLTVKcGtvMUloR1QyejZoSHFGdk80Q1EwU1Z6WUlyZWFIc0xvRUJfNm5KWXBFSGV1MjFyUjdXLUp4TVhXelBraEI5QVREMVBQdTFPVzE5WUZ3X19yaENmbUdSaTNWSFNuOXhabU1yMnVnd3ljejkwdkp4OWtVZw?oc=5>

### CAT Shares Fall Despite Q3 Earnings Beat: How to Play the Stock?
- Summary: CAT shares dropped even after Q3 earnings beat expectations.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQVjJ2QU4yQ2dnWldyc0VTQV9tV0xKRF9LRThnd1NxNll1bUlCTjZsMm5jR3pKQTNYYWQxTzJaS2NiV01DS2dYTUtNSVBKMVNOQWNnWTdxYlRGRzI5U0Q4YkpPcElYT2pqS294SHVEay1fZi15OFVkUHZOMV9jbEI2YmJMZ1dWRGoyaVR6MUtxVDFDYXhtVkE?oc=5>

### Michael Burry Cashes In On Caterpillar Puts After 4X Gain — Is CAT Stock Still Overvalued?
- Summary: Burry’s puts suggest bearish sentiment.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNWlFPd3JLaXpOZVZXUHJYOF9tOVFIS3lJUFNjSi1maUZnRFNCN3hNWjRpSXI0a0lla05ibDhiYWlDbXRlUnF6WmtHUzhmVFhDUGZ1WWxCeXNvTXE1TGNNTDl5WjdmVFlyb0RGbG1EM3BWeWIxY0gtbnVhTlNTQkZvQVBwOXpTQ3RzQ1BnZUJObWtzejhHVFlDWDY5RXVhMVNZTkt0cQ?oc=5>

### Caterpillar Inc Stock (CAT) Opened Down by 3.21% on Nov 10: What Investors Need To Know
- Summary: Opening decline indicates short‑term downside pressure.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNQlM1U25JV09KYWxJRkU1cTV4RFFOZmUyS3FHNlhSYmlOSldQM1hxZ0pZZFJfNDlLQzFXbkstaHRuSTBQR3llNEM2WUNfaGV1bmV4TTBmN1JaNVI2elZieHZqZzNXeFBfc2ZwcURndkdRVW52YlRkUlBhdnRHMnA3a0J5MUlZajh0OEE?oc=5>

## CATALYSTS

### Caterpillar Stocks Jump 6.61% as Anthropic Takes Over $3.4 Billion Generator Order
- Summary: Caterpillar’s stock surged after Anthropic secured a $3.4B generator contract, signaling a significant product win.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPeHNqTHAxVnZNSjZwbkNvYVRQSGpZTjFfUUhyOGRvVmswVl9Fb2NqaWtSQzc4bWFjb25fZzl3VmhyS0lhV2pHdkNYM3JTdHd4RVEyMkdRa0xPOUdBaFFEXzdDWFVnd1ZMSmtmUURSOTkzaEUtYTEtOVNGNGEzR2VfbG12ci1YeWlENXRDcmlialo5UUQwWW9RYg?oc=5>

### Caterpillar Inc Stock (CAT) Moved Up by 6.33% on Nov 9: Facts Behind the Movement
- Summary: CAT shares rose 6.33% on Nov 9, reflecting positive market sentiment and potential underlying catalysts.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPYWhHMi1yN2MyUnhlZmlPdFdLOTNjeURLWFlFWEc1THo3Y2JRUllZVWNIcG5PbVU2SVVIWXFQb3c5WHJxTnpPT2tmYVNxSzZXb3QyME91X2lmdXVUOHl0eW91UFA5WXBtN0dPSWlIbHVybkU2ZENISENkMTJ4WUJwaGtfMXMwbTVaRmc?oc=5>

### Caterpillar stock support and resistance levels after 5.8% rebound
- Summary: Technical analysis shows CAT rebounded 5.8%, with key support and resistance levels identified for traders.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPdnFFSGFMckxMbjBEMXpXYS1FQVhzT293aE5ZbW5pX0lTYkZRaFdXMkRzS1NfSDFHUm12ZW03V29KSnlybkdCSU5wanYzdlZXV2psTjl0OWRQUU1zMExHcXpsZ2I3cWhVNU1OcTZwcks5X21fT0lWcUFIUEtjYzJaU25uekFJLUo4bGtrZ0ZxeDBaQkpWTEs0?oc=5>

### A Look at Caterpillar Inc (CAT) After 7.2% Gain -- GF Value $504
- Summary: CAT experienced a 7.2% gain, boosting its GF value to $504 and indicating strong investor confidence.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNTnRjQmJITUVpQkcyejM3NEppdUJyRldHaXJfOUZiZEd0RElCXzgyMGRYb0FQUzBnOFRaU0J2NEUwZUFXRW43Nkl0MElPOXBwQVVWN2hMMzg4SDRZaDNwVmxEWllHSDg4VmZmREc4ak9YRS0wQ0k1Z3JkSjlhckEwOG9mZ1ZHT0c3RVpvLUJseHg1em12eFVCRnE3M015UXNIWHIwVXV4WHAxV0l4RnVOVW1R?oc=5>

### Caterpillar Inc. (CAT) Posted a Record $20 Billion Quarter: Is the AI Power Boom Fueling Its Next Growth Phase?
- Summary: Caterpillar reported record $20B earnings, citing AI-driven growth potential.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPNFQ2b0ZPcnJJdXZkNVpMcnJtRmQ1eVo0SkUyMENXSEplc0lvSF9wZGlVbnQ5anBhLW9xY3JCcm5LbmFteDlLQ3VhT0dXeW5SUERjR3Ywek5UdE1LdUtpa0ROQkE2eDNPUW8wVTdfNVZBV253aE9aRTNOOWxiejZOLXZqY2didnBNcHc?oc=5>

### Michael Burry trims Caterpillar bearish bet after puts nearly quadruple (CAT:NYSE)
- Summary: Analyst Michael Burry reduced bearish position after significant put activity.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNenhDZnVjT3I5TWg4b2pELVpBZUl0OXRHTTZFdWs0bVotNmRhcnF0QlpUcmJoR0s1U1I3M0JidEtvU0Rqemh6VXBRZ2NsV3lYOFdIMUViMVJkZlUyZ1BZWk5scTNhc090YlVFUjhsY095c3c5Wl9ZbDB3S3dPRW9vS3ZIdzg0SUVCeFhIQ1ByZUpQUmxaY3M5QUprb0w1RDktbTZTTTdHZkpKV09UZUE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CAT** | **22.94** | **12.45** | **18.03** | **17.30** | **267,495,833,600.00 USD** | **3.27** |
| DE | 38.22 | 6.62 | 28.27 | 4.90 | 185,405,227,008.00 USD | 46.61 |
| CNH | 58.38 | 1.95 | 18.60 | -1.00 | 19,687,677,952.00 USD | 28.54 |
| CMI | 19.46 | 4.67 | 12.54 | 13.50 | 62,258,032,640.00 USD | -4.86 |

Peers fetched as_of: 2026-11-10; CAT reuses existing data (market data as_of: 2026-11-10); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-10

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 20,682,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 1,141,000,000.00 USD; period 2011-07-01/2011-09-30; fiscal year/reporting period 2011/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/18230/000001823026000057/cat-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi-gFBVV95cUxQZ3N5d2hOR2ZJLTYzX2NKUGYzVnRqZ0c5RWJNMUFobWR1Z2xCdlRiaXNpNjBzZWp3U0tRWmF3aTZSZUZPMmxzSTMzcmk3dTRsVGdudmFpSkhjU3MtVmFVcXNza2N6UmExQzJJRGxnMnNvSWQtdklRYnJLYU9JQXNMTVJ1VmRmY2JKOWZBZ3AtWUxlM1V3akpVUTNOV3JjUGpVTzJVdzV0TnNlUk1MQXFSazhNX3NxV0RHcE9NTnNRN2Vfd28zSXpmNUVuYnpIOHJlaktoLVlDd3dDOGJKR1VGUXhvRkRBdGJUbUd6clJkS0FyOHlLYzUyNU93?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxPVGoxYXJOVFIyVTZxQ2FWenNtdDhKM2M4cl9LNkRFdVBOMXg4cVQ2ZU5xcjh2aTV5ZC1lNU9rVkR1ajI5OFdPd2hnSlpHOEQta0Q5Uno5YWd1enBlU09GMUNScWlEZ0tjQnpzQmVnU3JGUnB1a3dIcDF0QTRSYi1HQ01BWGpHVGFvTzZkbXhNWmYxTklmalJmWlpjYjlDQkhQbjN0WjgwMjR0TG02Q293X2tCQWVmOHl4aHdyYTU2Y1NYblB5V2ZlcDl0NE1qd9IB0wFBVV95cUxNblpMSmZtUm9HTUl5YzEyMjl4bW5DWU9kZUhKTVRxbkhaVkM4cmp6MHdTUWFXb1R2X2M0UlBEQ182WFhhOWI3YU5vM0tmWHNUb0ZQYnN3OV9FWWk1UGEyLTdzOEF1V2lNUmg1RjhOT3YyZk9JYl9vYXE4ZXB1VmdiSHVrVnAzbU5ka1BxajJKYm5zMXdrdE1PZl9Pby1HVkZaaVN2TW12aVBPc0dHejFyWEd4UVdBaW1vQ0NhYS1Kamk1TThhWGNHZ3cyVzdfbEVQQUlN?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNUy1ZR3NCUUJ3bVh4R3lpOFBkVlAxa0hkaE1peWdVUHR6SXFPZVg3bC1hRldCc1ZWS0xrLTdfSkRoaWxUMzEwcldURzlmMDFSTnllakpmYlRyY0t5Mi1xQjllV1JkY2dkbkVJbGtfNUYzZXJNOVVJbHMzSWRGcWxMRWtyd25oUFR3MnN4YXJIZzJPa2o1Mmp4QkxtSGxlS0doRXFlbw?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQejZtY3VabmQ4VHhlRU9zZ1owV3F5dkpmSWEtYzFGR0dQLTVKcGtvMUloR1QyejZoSHFGdk80Q1EwU1Z6WUlyZWFIc0xvRUJfNm5KWXBFSGV1MjFyUjdXLUp4TVhXelBraEI5QVREMVBQdTFPVzE5WUZ3X19yaENmbUdSaTNWSFNuOXhabU1yMnVnd3ljejkwdkp4OWtVZw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQVjJ2QU4yQ2dnWldyc0VTQV9tV0xKRF9LRThnd1NxNll1bUlCTjZsMm5jR3pKQTNYYWQxTzJaS2NiV01DS2dYTUtNSVBKMVNOQWNnWTdxYlRGRzI5U0Q4YkpPcElYT2pqS294SHVEay1fZi15OFVkUHZOMV9jbEI2YmJMZ1dWRGoyaVR6MUtxVDFDYXhtVkE?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNWlFPd3JLaXpOZVZXUHJYOF9tOVFIS3lJUFNjSi1maUZnRFNCN3hNWjRpSXI0a0lla05ibDhiYWlDbXRlUnF6WmtHUzhmVFhDUGZ1WWxCeXNvTXE1TGNNTDl5WjdmVFlyb0RGbG1EM3BWeWIxY0gtbnVhTlNTQkZvQVBwOXpTQ3RzQ1BnZUJObWtzejhHVFlDWDY5RXVhMVNZTkt0cQ?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNQlM1U25JV09KYWxJRkU1cTV4RFFOZmUyS3FHNlhSYmlOSldQM1hxZ0pZZFJfNDlLQzFXbkstaHRuSTBQR3llNEM2WUNfaGV1bmV4TTBmN1JaNVI2elZieHZqZzNXeFBfc2ZwcURndkdRVW52YlRkUlBhdnRHMnA3a0J5MUlZajh0OEE?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPeHNqTHAxVnZNSjZwbkNvYVRQSGpZTjFfUUhyOGRvVmswVl9Fb2NqaWtSQzc4bWFjb25fZzl3VmhyS0lhV2pHdkNYM3JTdHd4RVEyMkdRa0xPOUdBaFFEXzdDWFVnd1ZMSmtmUURSOTkzaEUtYTEtOVNGNGEzR2VfbG12ci1YeWlENXRDcmlialo5UUQwWW9RYg?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPYWhHMi1yN2MyUnhlZmlPdFdLOTNjeURLWFlFWEc1THo3Y2JRUllZVWNIcG5PbVU2SVVIWXFQb3c5WHJxTnpPT2tmYVNxSzZXb3QyME91X2lmdXVUOHl0eW91UFA5WXBtN0dPSWlIbHVybkU2ZENISENkMTJ4WUJwaGtfMXMwbTVaRmc?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPdnFFSGFMckxMbjBEMXpXYS1FQVhzT293aE5ZbW5pX0lTYkZRaFdXMkRzS1NfSDFHUm12ZW03V29KSnlybkdCSU5wanYzdlZXV2psTjl0OWRQUU1zMExHcXpsZ2I3cWhVNU1OcTZwcks5X21fT0lWcUFIUEtjYzJaU25uekFJLUo4bGtrZ0ZxeDBaQkpWTEs0?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNTnRjQmJITUVpQkcyejM3NEppdUJyRldHaXJfOUZiZEd0RElCXzgyMGRYb0FQUzBnOFRaU0J2NEUwZUFXRW43Nkl0MElPOXBwQVVWN2hMMzg4SDRZaDNwVmxEWllHSDg4VmZmREc4ak9YRS0wQ0k1Z3JkSjlhckEwOG9mZ1ZHT0c3RVpvLUJseHg1em12eFVCRnE3M015UXNIWHIwVXV4WHAxV0l4RnVOVW1R?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPNFQ2b0ZPcnJJdXZkNVpMcnJtRmQ1eVo0SkUyMENXSEplc0lvSF9wZGlVbnQ5anBhLW9xY3JCcm5LbmFteDlLQ3VhT0dXeW5SUERjR3Ywek5UdE1LdUtpa0ROQkE2eDNPUW8wVTdfNVZBV253aE9aRTNOOWxiejZOLXZqY2didnBNcHc?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNenhDZnVjT3I5TWg4b2pELVpBZUl0OXRHTTZFdWs0bVotNmRhcnF0QlpUcmJoR0s1U1I3M0JidEtvU0Rqemh6VXBRZ2NsV3lYOFdIMUViMVJkZlUyZ1BZWk5scTNhc090YlVFUjhsY095c3c5Wl9ZbDB3S3dPRW9vS3ZIdzg0SUVCeFhIQ1ByZUpQUmxaY3M5QUprb0w1RDktbTZTTTdHZkpKV09UZUE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
