# V Intelligence Report

- ticker: **V**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/V/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/V/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:10:08.710664+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 18, 'rule': 6, 'ai': 8, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/V** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 18 unique headlines; 8 named publishers; 0 exact duplicates; 18 HTTPS source links; largest publisher share 22.22%; oldest publication 2026-10-31

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 422.5900 |
| Return 1D (%) | -3.2022 |
| Return 1W (%) | 2.9352 |
| Return 1M (%) | 14.3031 |
| Return YTD (%) | 21.2191 |
| Return 1Y (%) | 25.2705 |
| Annualized volatility (%) | 22.9735 |
| Beta vs SPY | 0.3465 |
| Max drawdown (%) | -17.1805 |
| Sharpe (rf=0) | 1.0985 |
| Downside deviation (rf=0, %) | 14.1731 |
| Sortino (rf=0) | 1.7806 |
| Historical VaR 95% (1D, %) | 1.8026 |
| Historical ES 95% (1D, %) | 2.7901 |
| Correlation vs SPY | 0.2050 |
| Tracking error vs SPY (%) | 24.1765 |
| P/E (trailing) | 35.42 |
| P/B | 21.69 |
| EV/EBITDA | 24.16 |
| Revenue growth (%) | 13.20 |
| Forward P/E (estimate) | 24.67 |
| Gross margin (%) | 97.68 |
| Operating margin (%) | 63.73 |
| Return on equity (%) | 63.51 |
| Free cash flow yield (%) | 2.67 |
| MA50 | 384.9830 |
| Close vs MA50 (%) | 9.7685 |
| MA200 | 343.4836 |
| Close vs MA200 (%) | 23.0306 |
| RSI (14, Wilder) | 63.2504 |
| MACD (12,26) | 12.2319 |
| MACD signal (9) | 10.6744 |
| MACD histogram | 1.5574 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'V': 276, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 422.5900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.2022 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.9352 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 14.3031 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 21.2191 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 25.2705 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.9735 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.1731 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.7806 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8026 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.7901 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2050 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.1765 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3465 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -17.1805 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0985 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.6745 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.6780 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 63.7280 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 63.5070 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.6738 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 35.4225 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 63.2504 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.5574 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 9.7685 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 23.0306 -> Clearly above the moving-average trend level.

## TAILWINDS

### Visa (V) Upgraded to Buy: Here's What You Should Know
- Summary: Visa (V) Upgraded to Buy: Here's What You Should Know
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPSnRvc3BiVWJzdF9ZWUsxa0p6eU1maWFQck5iQVVaTW5SZ1lOcXFmZjhUZi1LM01YX25LM1M1dVREYnM4T1VjMjFQVUR0bC1JUWw3WWNEVmNaOEVFbkFPT00wR0N2dUpSLUJMekVHNTl2amdhejF4QXNsN093U2lmcGx5S3Y5dlhpakxpWEllN1d3S3cw?oc=5>

### Visa (NYSE:V) Stock Price Up 2.9% - What's Next?
- Summary: Visa (NYSE:V) Stock Price Up 2.9% - What's Next?
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQWVNBeVJfdFhEYkZDb0lHRHBYN0NqaFNZYmFnbUw4aUxMMkRXcWpSeTFidDBUbWZVeDYzWGtRU2RFRjIxamhyTVlyRG5tajBtNDZfMW00TjFHTGRrLUlwaWNjVmlyRl9PT2NkRjJkQmd3TUY1SkJNdjRKeU81NWJCWTdsWXJrNWstTFlUOWVLRllJTl9hOXBGb0ZmT2hQZnQ4MWc?oc=5>

### Visa Inc Stock (V) Moved Up by 3.14% on Nov 2: What Investors Need To Know
- Summary: Shares rose 3.14% on Nov 2, indicating positive market sentiment.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxQbHJiazdqS3VVeVJpS2Rob2dNRUV2c3Y3WS0tSExLZzFkSVBmbWw3ZERwT05GLVRCcjctMnh6WWxlV2pWNzJldlJjUUVoa1dtMHJoS0RFTkhrNUJSVmR3M1diVkhkR2pTNEg0eTdtakRwSC1pOUw3bzRYRkw5MVQ5RElxQ2JKZjQ?oc=5>

### Visa Stock And Other Safe Havens for Crypto Flight to Safety
- Summary: Visa stock viewed as a safe haven amid crypto market volatility.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQcmJGdUxpQUtVS3ZXZWIyRWtpSGk1S2RJQlhObjBWbXU3U044ZVhKeUV5dFl2MTg2cVpoUFJsdzh5eXBZeGFSU3NqU1BSY2JER1pxQ0E2aFFZRUNLcFZpVm16NFRfSVZZOTZwWTluSFdFLURCRFFIb2FaZjN3YTdtUUhhWks5YUw1ZUdfVGtIZFJfX05qZzk0YXRydTk3azN6U3pXQk9BQXptV1ZqWTlVS2xfaTJuT0ZVX0wtUG9VdjBHQdIBxwFBVV95cUxORGxqRlJjTnlJU0hwSU1va3o0Z3pqRFhUNmJGY2VfcGVoeDJiM2tSd25hSUN5ZkZaSFdBQzFTRlZXcWwzREZtTmxpNmRacmdUSFBBWm1QY1RmNGJvQmFQSHprTXdpLWNETHd3ZGlGR0d6dTRQSGl2d2tINV9wUFdnQUpwWGQ5WnpDUnpwalJrRWtiek1kT2hjNzAxc09Na0FQYWlaM0diMTJjUUs4S3dQM3lOZTBmOEdxUjVkYXh3QnZuSFdxa01J?oc=5>

### Visa's Solid Q4 Masks Rising Incentives: Is V Still Worth Buying?
- Summary: Visa reports strong Q4 earnings, offsetting rising incentive costs, suggesting continued value for investors.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxPdnNRUXNhekR0Mlp0SVRHLTZMR1dVYjl3OEh6MlRTLUlucjE2NlVDNkpyNkVsa3VERVFaX0dhY01EczhOSWFEd2pFNldRVkdkdHZTREE2RzRpT1dXa19VX215aHJxdFBraWlPRXhQX1ljS1ZlUVdVQlNxNDFWZE8tYVJpM2tvWHNZVElmSDBidHZyM2hreHlXRmM4Z0NseGNCVzNiSnBrT0QwQmNENWEwdzhGa0ZVcXRVRmNn?oc=5>

## HEADWINDS

### Visa Stock Drops 3.8%, Shedding Nearly $28 Billion in One Session
- Summary: Visa Stock Drops 3.8%, Shedding Nearly $28 Billion in One Session
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE5fT1NLR3lPeDJtLWNPQkQzM1Y2eEUweWx5Y3BPZHJfeXFCQVhWOW5JUHcycmRjNmlwWDhGRU4wVFRmbVZTU3ZLdEhaU2VVcHNtUWlZTEJnUk9rRlk2di1iamJnbmdONGtVSjBvOFRJNk5iV2ZMR0NSZmdBb2gzQQ?oc=5>

### Visa (NYSE:V) Stock Falls 3.3% - Here's Why
- Summary: Visa (NYSE:V) Stock Falls 3.3% - Here's Why
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQUEpYckR2d0x3OXIwaXhxajhOQ0Z6RzZ5VjNHM19GTDBsVTZ2YlMzMGNzRXR3TUYtcjJqeVNTcUFhbUdZZl9JdnhVeVpNMEdEZWtHQ1F6MlIxeVRDQTI2VkFscm9UbWF3Y19uOU9DXzJ3azNSVEFaTUJUQmI4M0lZWjZkV243ZHRoWTJlZlhIM21LNTBrZHBhRWhabVI?oc=5>

### Visa Inc Stock (V) Closed Down by 3.20% on Nov 5: Key Drivers Unveiled
- Summary: Visa stock fell 3.2% on Nov 5, citing key drivers.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxNLU9BLS1xM1p6VEFhS1dPejBMM3V0LWVkOVFSRUc3ajNKaGNFOHpIQmt1UzQtcXpQSjFxa2hOb210aEJkZ016M2VqeU1tUjB5cXVYQVBCa0ZfWTJqVTk0Z2dlMWNlU3oxZUJhN2szR2FkVHZGZUNremlFcmZrY2dIR0w2OFBjVGs?oc=5>

## CATALYSTS

### Visa Just Hiked Its Dividend by More Than 16%, But Investors Should Consider Waiting for V to Pull Back Before Buying.
- Summary: Visa Just Hiked Its Dividend by More Than 16%, But Investors Should Consider Waiting for V to Pull Back Before Buying.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPV2R5bnA1Z2FTQ0tCRmFNeVJQUUZBZlFDaHloVE82YVlDcmhtZS1WTXVsVDFuZmh4V0doLW9SbXBrblFudDNQUkR0WUl2YnBoYkMyMWNmQXIwMGpTYlVCTUFoQzlVcXBEbG16RXBQOFp2eVo4ZmxoOUFuaXk2a2pmZXVIT1dGeXdHUllBSWtwNUJ4aHJyaTkzUnZR?oc=5>

### Visa (V) Stock Fair Value Edges Higher After Analysts Lift Targets On Q4 Results
- Summary: Visa (V) Stock Fair Value Edges Higher After Analysts Lift Targets On Q4 Results
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPSUM0T3phd1lPUkhkRlpMdUdNVWZRYnlHNk5sLXhwSjBxd3J0OXVMb1lMaGxsMGRWMmptQVNjT3dYcUVNazZiRzBNX3dpOE0yYS1Nd2tHeXJENlQwcFV5MFlqZ3ZZNFJjWFI4RlhwN3FKbmhTcVJhWkV3dW1oTkgybExxeDBtc1plbVFXdG82V0RBQQ?oc=5>

### Visa raises dividend by 16%: Can V stock continue its gains?
- Summary: Visa increases dividend by 16%, potentially boosting shareholder returns.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxNdUZJWVpmVWxsQ2g3enhpYUk1eGs3a2hkaXVTX21PQWtCZF9LcjB5LUJSZkNzblp5VnBWNE5FMzY4NGRzSld3UVAyUXYwM1BnMFBFcUxEX0VUMDQ0bXlDZlhyRFNXOVBoLWZrNGhBUUF6X0laakt5ME0xelhmUXlWSDNRUUd1bDdQeU9KenFR?oc=5>

### AI failed 42.8% of shopping test runs, Visa finds
- Summary: Visa reports AI test failures in 42.8% of shopping scenarios, indicating challenges in AI integration.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxQQ0x3UVNPbUo2OFN1TnczU3BId1QxYm5oQ1hRZEhjdkVjLWtxNElKTGRkNXJMSEd3ZVlVdmdtVTRKeXBVYUtTbnBqdm1MVU1PUDBhZm9ONmxGbm1ENEYwTGFIZTlPa3lGS0JIWEd4WWh3d2ZvX1BTclFwZmNSNC1nWVFnWlJYYWVyTVpRQWdDOEZhZHBfemc5dDZ4U2Y1ZlppUkxtbWptQWd3OS1aTnFDQzV1aDVhZGhoLVE?oc=5>

### Holiday shoppers plan an average of $777 for gifts as Visa says travel costs steer spending toward physical presents.
- Summary: Visa notes holiday shoppers plan $777 on gifts, attributing shift to travel costs driving physical present purchases.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxQT21EZE5vTW9oa0gwa0JXTkt1UUtFRlVtOHpPek0wZjNkQlhSS3QzTkpRSUhabUx0U3lrTExxcEhyU0FYZDQ4VVhzUl9xUjUtdHhycWdZdUJweWk3Mk8ycmRDeklnemRkYzVDN2lGNjRYYV83ZW9YMU4wUWVlSEFzMUxCU3pWcEgtbXFoVjNscnV0cXBhV1dwZGdfcnpNbHNIanVTZVVUWDV1WndYOHd1YmVEeGVrNHpt?oc=5>

### Truist Financial Issues Positive Forecast for Visa (NYSE:V) Stock Price
- Summary: Truist Financial predicts a positive outlook for Visa's stock, indicating potential upside.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxPZURreXZYSVNkWWNHZkxrbnFJc1oyQXBNeEhkcWJvN0pnVHc5WW80VGR0VUlad1cwdGlUWTBBamtQM25HYmI2NlJmUy10aWZ4V2IxY3MteWRpb00yUi16dGJMN1hvVXA3TWZvTFMyQm1oUndTWkVDT0c0dXFQNlFWUmhlT3RDbVdZZGpFUFQ5RDZfQkRUZ040Uk9WSkdKY3J2V2JyUVlFVnhGWjVzSjl4STBSd1dhOEhnaENyUy1uUW01UDM4WHFkdHA1RQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **V** | **35.42** | **21.69** | **24.16** | **13.20** | **789,823,225,856.00 USD** | **25.27** |
| MA | 35.21 | 84.71 | 25.40 | 14.00 | 571,421,818,880.00 USD | 19.31 |
| PYPL | 11.49 | 2.53 | 8.12 | 2.00 | 48,975,613,952.00 USD | -12.40 |
| AXP | 18.74 | 6.09 | N/A | 11.30 | 217,909,280,768.00 USD | -10.16 |

Peers fetched as_of: 2026-11-05; V reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-01-26 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-05

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-11-05
- Revenue (latest available single quarter): 5,840,000,000.00 USD; period 2019-04-01/2019-06-30; fiscal year/reporting period 2019/Q3
- Net income (latest available single quarter): 5,628,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1403161/000140316126000134/v-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilAFBVV95cUxPSnRvc3BiVWJzdF9ZWUsxa0p6eU1maWFQck5iQVVaTW5SZ1lOcXFmZjhUZi1LM01YX25LM1M1dVREYnM4T1VjMjFQVUR0bC1JUWw3WWNEVmNaOEVFbkFPT00wR0N2dUpSLUJMekVHNTl2amdhejF4QXNsN093U2lmcGx5S3Y5dlhpakxpWEllN1d3S3cw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQWVNBeVJfdFhEYkZDb0lHRHBYN0NqaFNZYmFnbUw4aUxMMkRXcWpSeTFidDBUbWZVeDYzWGtRU2RFRjIxamhyTVlyRG5tajBtNDZfMW00TjFHTGRrLUlwaWNjVmlyRl9PT2NkRjJkQmd3TUY1SkJNdjRKeU81NWJCWTdsWXJrNWstTFlUOWVLRllJTl9hOXBGb0ZmT2hQZnQ4MWc?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxQbHJiazdqS3VVeVJpS2Rob2dNRUV2c3Y3WS0tSExLZzFkSVBmbWw3ZERwT05GLVRCcjctMnh6WWxlV2pWNzJldlJjUUVoa1dtMHJoS0RFTkhrNUJSVmR3M1diVkhkR2pTNEg0eTdtakRwSC1pOUw3bzRYRkw5MVQ5RElxQ2JKZjQ?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQcmJGdUxpQUtVS3ZXZWIyRWtpSGk1S2RJQlhObjBWbXU3U044ZVhKeUV5dFl2MTg2cVpoUFJsdzh5eXBZeGFSU3NqU1BSY2JER1pxQ0E2aFFZRUNLcFZpVm16NFRfSVZZOTZwWTluSFdFLURCRFFIb2FaZjN3YTdtUUhhWks5YUw1ZUdfVGtIZFJfX05qZzk0YXRydTk3azN6U3pXQk9BQXptV1ZqWTlVS2xfaTJuT0ZVX0wtUG9VdjBHQdIBxwFBVV95cUxORGxqRlJjTnlJU0hwSU1va3o0Z3pqRFhUNmJGY2VfcGVoeDJiM2tSd25hSUN5ZkZaSFdBQzFTRlZXcWwzREZtTmxpNmRacmdUSFBBWm1QY1RmNGJvQmFQSHprTXdpLWNETHd3ZGlGR0d6dTRQSGl2d2tINV9wUFdnQUpwWGQ5WnpDUnpwalJrRWtiek1kT2hjNzAxc09Na0FQYWlaM0diMTJjUUs4S3dQM3lOZTBmOEdxUjVkYXh3QnZuSFdxa01J?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxPdnNRUXNhekR0Mlp0SVRHLTZMR1dVYjl3OEh6MlRTLUlucjE2NlVDNkpyNkVsa3VERVFaX0dhY01EczhOSWFEd2pFNldRVkdkdHZTREE2RzRpT1dXa19VX215aHJxdFBraWlPRXhQX1ljS1ZlUVdVQlNxNDFWZE8tYVJpM2tvWHNZVElmSDBidHZyM2hreHlXRmM4Z0NseGNCVzNiSnBrT0QwQmNENWEwdzhGa0ZVcXRVRmNn?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE5fT1NLR3lPeDJtLWNPQkQzM1Y2eEUweWx5Y3BPZHJfeXFCQVhWOW5JUHcycmRjNmlwWDhGRU4wVFRmbVZTU3ZLdEhaU2VVcHNtUWlZTEJnUk9rRlk2di1iamJnbmdONGtVSjBvOFRJNk5iV2ZMR0NSZmdBb2gzQQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQUEpYckR2d0x3OXIwaXhxajhOQ0Z6RzZ5VjNHM19GTDBsVTZ2YlMzMGNzRXR3TUYtcjJqeVNTcUFhbUdZZl9JdnhVeVpNMEdEZWtHQ1F6MlIxeVRDQTI2VkFscm9UbWF3Y19uOU9DXzJ3azNSVEFaTUJUQmI4M0lZWjZkV243ZHRoWTJlZlhIM21LNTBrZHBhRWhabVI?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxNLU9BLS1xM1p6VEFhS1dPejBMM3V0LWVkOVFSRUc3ajNKaGNFOHpIQmt1UzQtcXpQSjFxa2hOb210aEJkZ016M2VqeU1tUjB5cXVYQVBCa0ZfWTJqVTk0Z2dlMWNlU3oxZUJhN2szR2FkVHZGZUNremlFcmZrY2dIR0w2OFBjVGs?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPV2R5bnA1Z2FTQ0tCRmFNeVJQUUZBZlFDaHloVE82YVlDcmhtZS1WTXVsVDFuZmh4V0doLW9SbXBrblFudDNQUkR0WUl2YnBoYkMyMWNmQXIwMGpTYlVCTUFoQzlVcXBEbG16RXBQOFp2eVo4ZmxoOUFuaXk2a2pmZXVIT1dGeXdHUllBSWtwNUJ4aHJyaTkzUnZR?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPSUM0T3phd1lPUkhkRlpMdUdNVWZRYnlHNk5sLXhwSjBxd3J0OXVMb1lMaGxsMGRWMmptQVNjT3dYcUVNazZiRzBNX3dpOE0yYS1Nd2tHeXJENlQwcFV5MFlqZ3ZZNFJjWFI4RlhwN3FKbmhTcVJhWkV3dW1oTkgybExxeDBtc1plbVFXdG82V0RBQQ?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxNdUZJWVpmVWxsQ2g3enhpYUk1eGs3a2hkaXVTX21PQWtCZF9LcjB5LUJSZkNzblp5VnBWNE5FMzY4NGRzSld3UVAyUXYwM1BnMFBFcUxEX0VUMDQ0bXlDZlhyRFNXOVBoLWZrNGhBUUF6X0laakt5ME0xelhmUXlWSDNRUUd1bDdQeU9KenFR?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxQQ0x3UVNPbUo2OFN1TnczU3BId1QxYm5oQ1hRZEhjdkVjLWtxNElKTGRkNXJMSEd3ZVlVdmdtVTRKeXBVYUtTbnBqdm1MVU1PUDBhZm9ONmxGbm1ENEYwTGFIZTlPa3lGS0JIWEd4WWh3d2ZvX1BTclFwZmNSNC1nWVFnWlJYYWVyTVpRQWdDOEZhZHBfemc5dDZ4U2Y1ZlppUkxtbWptQWd3OS1aTnFDQzV1aDVhZGhoLVE?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxQT21EZE5vTW9oa0gwa0JXTkt1UUtFRlVtOHpPek0wZjNkQlhSS3QzTkpRSUhabUx0U3lrTExxcEhyU0FYZDQ4VVhzUl9xUjUtdHhycWdZdUJweWk3Mk8ycmRDeklnemRkYzVDN2lGNjRYYV83ZW9YMU4wUWVlSEFzMUxCU3pWcEgtbXFoVjNscnV0cXBhV1dwZGdfcnpNbHNIanVTZVVUWDV1WndYOHd1YmVEeGVrNHpt?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxPZURreXZYSVNkWWNHZkxrbnFJc1oyQXBNeEhkcWJvN0pnVHc5WW80VGR0VUlad1cwdGlUWTBBamtQM25HYmI2NlJmUy10aWZ4V2IxY3MteWRpb00yUi16dGJMN1hvVXA3TWZvTFMyQm1oUndTWkVDT0c0dXFQNlFWUmhlT3RDbVdZZGpFUFQ5RDZfQkRUZ040Uk9WSkdKY3J2V2JyUVlFVnhGWjVzSjl4STBSd1dhOEhnaENyUy1uUW01UDM4WHFkdHA1RQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
