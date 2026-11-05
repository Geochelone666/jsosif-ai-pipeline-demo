# V Intelligence Report

- ticker: **V**
- Report as_of: **2026-11-04**
- Market data as_of: **2026-11-04**
- Quant sources: https://finance.yahoo.com/quote/V/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/V/key-statistics/
- AI analysis snapshot as_of: **2026-11-04**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-05T05:22:55.737220+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 19, 'rule': 9, 'ai': 4, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261104T044411Z-6b13f9ec/V** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 19 unique headlines; 6 named publishers; 0 exact duplicates; 19 HTTPS source links; largest publisher share 31.58%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 436.5700 |
| Return 1D (%) | 3.8414 |
| Return 1W (%) | 8.9790 |
| Return 1M (%) | 21.0475 |
| Return YTD (%) | 25.2293 |
| Return 1Y (%) | 29.3157 |
| Annualized volatility (%) | 22.7328 |
| Beta vs SPY | 0.2979 |
| Max drawdown (%) | -17.1805 |
| Sharpe (rf=0) | 1.2482 |
| Downside deviation (rf=0, %) | 13.8054 |
| Sortino (rf=0) | 2.0554 |
| Historical VaR 95% (1D, %) | 1.7961 |
| Historical ES 95% (1D, %) | 2.6824 |
| Correlation vs SPY | 0.1683 |
| Tracking error vs SPY (%) | 24.1537 |
| P/E (trailing) | 34.13 |
| P/B | 22.41 |
| EV/EBITDA | 24.95 |
| Revenue growth (%) | 13.20 |
| Forward P/E (estimate) | 25.49 |
| Gross margin (%) | 97.68 |
| Operating margin (%) | 63.73 |
| Return on equity (%) | 63.51 |
| Free cash flow yield (%) | 2.59 |
| MA50 | 384.2092 |
| Close vs MA50 (%) | 13.6282 |
| MA200 | 342.9873 |
| Close vs MA200 (%) | 27.2846 |
| RSI (14, Wilder) | 75.7176 |
| MACD (12,26) | 12.3980 |
| MACD signal (9) | 10.2851 |
| MACD histogram | 2.1130 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'V': 275, 'SPY': 275}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 436.5700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 3.8414 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 8.9790 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 21.0475 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 25.2293 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 29.3157 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.7328 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.8054 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.0554 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.7961 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6824 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1683 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.1537 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2979 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -17.1805 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.2482 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.4907 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.6780 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 63.7280 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 63.5070 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.5882 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 34.1337 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 75.7176 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 2.1130 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 13.6282 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 27.2846 -> Clearly above the moving-average trend level.

## TAILWINDS

### Visa (V) Upgraded to Buy: Here's What You Should Know
- Summary: Visa (V) Upgraded to Buy: Here's What You Should Know
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPSnRvc3BiVWJzdF9ZWUsxa0p6eU1maWFQck5iQVVaTW5SZ1lOcXFmZjhUZi1LM01YX25LM1M1dVREYnM4T1VjMjFQVUR0bC1JUWw3WWNEVmNaOEVFbkFPT00wR0N2dUpSLUJMekVHNTl2amdhejF4QXNsN093U2lmcGx5S3Y5dlhpakxpWEllN1d3S3cw?oc=5>

### Visa’s Record Year Pushes Shares Higher
- Summary: Visa’s Record Year Pushes Shares Higher
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNOVdnMkQ3UTRZTjJXN2lxcGRIM0pBaUZYNS1JQm1UNmdXc0tORnJmTXl4ZEFVR1Q2LW5QQ2M5Y0lkektFZElVSjN6OVgzblZtSllkcEpFV2NHVlMwOWNub2JJY0J2aHpNcVozeEJnY2lERjJpcmV3eS02RnBuQVdvWDhCTm5UeFF1UGJmRzIySUljeWpJaE01d2JmS3hndw?oc=5>

### Visa (NYSE:V) Stock Price Up 2.9% - What's Next?
- Summary: Visa (NYSE:V) Stock Price Up 2.9% - What's Next?
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQWVNBeVJfdFhEYkZDb0lHRHBYN0NqaFNZYmFnbUw4aUxMMkRXcWpSeTFidDBUbWZVeDYzWGtRU2RFRjIxamhyTVlyRG5tajBtNDZfMW00TjFHTGRrLUlwaWNjVmlyRl9PT2NkRjJkQmd3TUY1SkJNdjRKeU81NWJCWTdsWXJrNWstTFlUOWVLRllJTl9hOXBGb0ZmT2hQZnQ4MWc?oc=5>

### Visa (NYSE:V) Stock Jumps 2.4% Following Analyst Upgrade
- Summary: Visa (NYSE:V) Stock Jumps 2.4% Following Analyst Upgrade
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQWWcwUmVJT0JLazdPdUNSYXBCSjBEV3ZqNVlKdHFYbnhyWDVIbk52NGlqVFhEck1Ba1E3NlN5dG56WGtQaDlMQkRydkFTZUM2YUw1bTIwdUswc2ZYX1Vma2xQcjJ5VGdzeVNKYm5UckMtLUp0STRSZ0JhTHR6ajM0VVlkb0xNaW5QbVE1X1NWWWtydDZLSFJJU1JBUGE1TldZTm9tcnY0VkN4RVRDS1ZmNTJn?oc=5>

### Visa reports strong quarterly results and new partnership: V gains momentum
- Summary: Visa reports strong quarterly results and new partnership: V gains momentum
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQdjZuYU4zb0NubmxLUTkxZ3RuWncxRF9vNm14VUxESEQybUc5Y3RTZjczbUdZNVEzQ2lybWI2THM4RHZOeko5OWhsdmpXMlp5ZnU5T3NzV2xRWWpEVlFKX3ltdWdaanN0MTh3YWdQYkptWThiS0hWNS1RU0xPRHdkb2pTTE1iNk81WGc?oc=5>

### Visa Inc Stock (V) Moved Up by 3.14% on Nov 2: What Investors Need To Know
- Summary: Shares rose 3.14% on Nov 2, indicating positive market sentiment.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxQbHJiazdqS3VVeVJpS2Rob2dNRUV2c3Y3WS0tSExLZzFkSVBmbWw3ZERwT05GLVRCcjctMnh6WWxlV2pWNzJldlJjUUVoa1dtMHJoS0RFTkhrNUJSVmR3M1diVkhkR2pTNEg0eTdtakRwSC1pOUw3bzRYRkw5MVQ5RElxQ2JKZjQ?oc=5>

### Visa Stock And Other Safe Havens for Crypto Flight to Safety
- Summary: Visa stock viewed as a safe haven amid crypto market volatility.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQcmJGdUxpQUtVS3ZXZWIyRWtpSGk1S2RJQlhObjBWbXU3U044ZVhKeUV5dFl2MTg2cVpoUFJsdzh5eXBZeGFSU3NqU1BSY2JER1pxQ0E2aFFZRUNLcFZpVm16NFRfSVZZOTZwWTluSFdFLURCRFFIb2FaZjN3YTdtUUhhWks5YUw1ZUdfVGtIZFJfX05qZzk0YXRydTk3azN6U3pXQk9BQXptV1ZqWTlVS2xfaTJuT0ZVX0wtUG9VdjBHQdIBxwFBVV95cUxORGxqRlJjTnlJU0hwSU1va3o0Z3pqRFhUNmJGY2VfcGVoeDJiM2tSd25hSUN5ZkZaSFdBQzFTRlZXcWwzREZtTmxpNmRacmdUSFBBWm1QY1RmNGJvQmFQSHprTXdpLWNETHd3ZGlGR0d6dTRQSGl2d2tINV9wUFdnQUpwWGQ5WnpDUnpwalJrRWtiek1kT2hjNzAxc09Na0FQYWlaM0diMTJjUUs4S3dQM3lOZTBmOEdxUjVkYXh3QnZuSFdxa01J?oc=5>

### Visa (V) Stock Could Be A Bargain On Record Revenue Growth
- Summary: Visa’s record revenue growth suggests a potential bargain for investors.
- Date: 2026-10-29 | Impact: high | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxQeWc0ZUwxcXpTaVdIQ1NCenRubXBzNDBHclFqYkxqWDgzemxKemlITnh5MXNDYjVkYmVIMmpNazZPZXVVQWpUQndFd2Y5eEVBc1Y3R0xvNWdtbXBOYXVkMENxbEhBQ19sajJEZEF4T1RPTWhySjdwMjlMUnQxM1Vkc1BJZ0JPQV9zZ2lFQnFjQWYtZXhPdks2WXlkVlJWOGRUbTRGNFhRM1FtMklZdXBNN3RaejNMVlRqYVdMaGxNc01wMXQxN09F0gHMAUFVX3lxTE5tNU1qLUgtNUZMeXFxV09hLUtJaExqVmswcUN6OXIybzdzQ1RBM0ZXOEx0TkxuVGZoNVdRMzh4MWx3M3pDemVkX0dKZFB0akg2T1BwbHlNUzRuQ0tlbjljNzU1VkxHUjRYQklOVmd1Z0xiTU5WNjExWTF6VXBRbmwteWFxVlZvTXFhOWVpNUVkSm56ZzdQbW1SbG4zaHluSEttT3F2dWlPTHRRMVFuRThEcVlmMjBBUEhlWTUweVZqelh5QWR3cDZUOVU1Sw?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Visa (V) Stock Fair Value Edges Higher After Analysts Lift Targets On Q4 Results
- Summary: Visa (V) Stock Fair Value Edges Higher After Analysts Lift Targets On Q4 Results
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPSUM0T3phd1lPUkhkRlpMdUdNVWZRYnlHNk5sLXhwSjBxd3J0OXVMb1lMaGxsMGRWMmptQVNjT3dYcUVNazZiRzBNX3dpOE0yYS1Nd2tHeXJENlQwcFV5MFlqZ3ZZNFJjWFI4RlhwN3FKbmhTcVJhWkV3dW1oTkgybExxeDBtc1plbVFXdG82V0RBQQ?oc=5>

### Visa Just Hiked Its Dividend by More Than 16%, But Investors Should Consider Waiting for V to Pull Back Before Buying.
- Summary: Visa Just Hiked Its Dividend by More Than 16%, But Investors Should Consider Waiting for V to Pull Back Before Buying.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPV2R5bnA1Z2FTQ0tCRmFNeVJQUUZBZlFDaHloVE82YVlDcmhtZS1WTXVsVDFuZmh4V0doLW9SbXBrblFudDNQUkR0WUl2YnBoYkMyMWNmQXIwMGpTYlVCTUFoQzlVcXBEbG16RXBQOFp2eVo4ZmxoOUFuaXk2a2pmZXVIT1dGeXdHUllBSWtwNUJ4aHJyaTkzUnZR?oc=5>

### Visa Inc. $V Stock: AIA Group Ltd Increases Stake
- Summary: Visa Inc. $V Stock: AIA Group Ltd Increases Stake
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxOa01kRk1xSWNvSktKYmRhNUp1Y1J2RkN4YUEyVzhmLTBGYXpBOGVvclBPU3pkc0hfaU9lZWJUNjhqUjRtUmwzMjBtdEYxUFhjQVZYV3NtYkVVU2R2dEVmdDZCQWdyT3JuMy1mOVB2dnRCM3MzOXViX3AweDVWS2dLSWYtMk1rb05ycTZWQV9obXJQcnR0M1VhRFh5M0tnREdzOG9XeXRXZHdxRGc?oc=5>

### Visa Inc. $V Stock Purchased by Vise Technologies Inc.
- Summary: Visa Inc. $V Stock Purchased by Vise Technologies Inc.
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxOSzBMWnlUbm5zX0c1U3pNZ2FXc3pVWFdqNGRWeUZIc3dzRE9hUHZTbjF5WUtyakNia3YwWjExNWFaR1lSdHdrN3NERkZKa092XzYwN2UtUFFrbVRJRHE2a0lJM3FyQWFNdTdJc1J4V0p0S2hJOGpxQndFeWNZOVhndlBKNFM0a3Z3X3FnbzhMQ1dMZFRPS0xsbE1QVjhBY3dCSE1DMlBrSy1qaDVid1NQZkd3?oc=5>

### Visa raises dividend by 16%: Can V stock continue its gains?
- Summary: Visa increases dividend by 16%, potentially boosting shareholder returns.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxNdUZJWVpmVWxsQ2g3enhpYUk1eGs3a2hkaXVTX21PQWtCZF9LcjB5LUJSZkNzblp5VnBWNE5FMzY4NGRzSld3UVAyUXYwM1BnMFBFcUxEX0VUMDQ0bXlDZlhyRFNXOVBoLWZrNGhBUUF6X0laakt5ME0xelhmUXlWSDNRUUd1bDdQeU9KenFR?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **V** | **34.13** | **22.41** | **24.95** | **13.20** | **815,951,970,304.00 USD** | **29.32** |
| MA | 33.87 | 86.88 | 26.03 | 14.00 | 586,022,780,928.00 USD | 22.48 |
| PYPL | 11.11 | 2.59 | 8.28 | 2.00 | 50,005,630,976.00 USD | -7.88 |
| AXP | 18.33 | 6.23 | N/A | 11.30 | 223,018,893,312.00 USD | -6.70 |

Peers fetched as_of: 2026-11-04; V reuses existing data (market data as_of: 2026-11-04); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-01-26 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-04

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-07-29
- Revenue (latest available single quarter): 5,840,000,000.00 USD; period 2019-04-01/2019-06-30; fiscal year/reporting period 2019/Q3
- Net income (latest available single quarter): N/A
- SEC link: https://www.sec.gov/Archives/edgar/data/1403161/000140316126000104/v-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilAFBVV95cUxPSnRvc3BiVWJzdF9ZWUsxa0p6eU1maWFQck5iQVVaTW5SZ1lOcXFmZjhUZi1LM01YX25LM1M1dVREYnM4T1VjMjFQVUR0bC1JUWw3WWNEVmNaOEVFbkFPT00wR0N2dUpSLUJMekVHNTl2amdhejF4QXNsN093U2lmcGx5S3Y5dlhpakxpWEllN1d3S3cw?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNOVdnMkQ3UTRZTjJXN2lxcGRIM0pBaUZYNS1JQm1UNmdXc0tORnJmTXl4ZEFVR1Q2LW5QQ2M5Y0lkektFZElVSjN6OVgzblZtSllkcEpFV2NHVlMwOWNub2JJY0J2aHpNcVozeEJnY2lERjJpcmV3eS02RnBuQVdvWDhCTm5UeFF1UGJmRzIySUljeWpJaE01d2JmS3hndw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQWVNBeVJfdFhEYkZDb0lHRHBYN0NqaFNZYmFnbUw4aUxMMkRXcWpSeTFidDBUbWZVeDYzWGtRU2RFRjIxamhyTVlyRG5tajBtNDZfMW00TjFHTGRrLUlwaWNjVmlyRl9PT2NkRjJkQmd3TUY1SkJNdjRKeU81NWJCWTdsWXJrNWstTFlUOWVLRllJTl9hOXBGb0ZmT2hQZnQ4MWc?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQWWcwUmVJT0JLazdPdUNSYXBCSjBEV3ZqNVlKdHFYbnhyWDVIbk52NGlqVFhEck1Ba1E3NlN5dG56WGtQaDlMQkRydkFTZUM2YUw1bTIwdUswc2ZYX1Vma2xQcjJ5VGdzeVNKYm5UckMtLUp0STRSZ0JhTHR6ajM0VVlkb0xNaW5QbVE1X1NWWWtydDZLSFJJU1JBUGE1TldZTm9tcnY0VkN4RVRDS1ZmNTJn?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQdjZuYU4zb0NubmxLUTkxZ3RuWncxRF9vNm14VUxESEQybUc5Y3RTZjczbUdZNVEzQ2lybWI2THM4RHZOeko5OWhsdmpXMlp5ZnU5T3NzV2xRWWpEVlFKX3ltdWdaanN0MTh3YWdQYkptWThiS0hWNS1RU0xPRHdkb2pTTE1iNk81WGc?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxQbHJiazdqS3VVeVJpS2Rob2dNRUV2c3Y3WS0tSExLZzFkSVBmbWw3ZERwT05GLVRCcjctMnh6WWxlV2pWNzJldlJjUUVoa1dtMHJoS0RFTkhrNUJSVmR3M1diVkhkR2pTNEg0eTdtakRwSC1pOUw3bzRYRkw5MVQ5RElxQ2JKZjQ?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQcmJGdUxpQUtVS3ZXZWIyRWtpSGk1S2RJQlhObjBWbXU3U044ZVhKeUV5dFl2MTg2cVpoUFJsdzh5eXBZeGFSU3NqU1BSY2JER1pxQ0E2aFFZRUNLcFZpVm16NFRfSVZZOTZwWTluSFdFLURCRFFIb2FaZjN3YTdtUUhhWks5YUw1ZUdfVGtIZFJfX05qZzk0YXRydTk3azN6U3pXQk9BQXptV1ZqWTlVS2xfaTJuT0ZVX0wtUG9VdjBHQdIBxwFBVV95cUxORGxqRlJjTnlJU0hwSU1va3o0Z3pqRFhUNmJGY2VfcGVoeDJiM2tSd25hSUN5ZkZaSFdBQzFTRlZXcWwzREZtTmxpNmRacmdUSFBBWm1QY1RmNGJvQmFQSHprTXdpLWNETHd3ZGlGR0d6dTRQSGl2d2tINV9wUFdnQUpwWGQ5WnpDUnpwalJrRWtiek1kT2hjNzAxc09Na0FQYWlaM0diMTJjUUs4S3dQM3lOZTBmOEdxUjVkYXh3QnZuSFdxa01J?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxQeWc0ZUwxcXpTaVdIQ1NCenRubXBzNDBHclFqYkxqWDgzemxKemlITnh5MXNDYjVkYmVIMmpNazZPZXVVQWpUQndFd2Y5eEVBc1Y3R0xvNWdtbXBOYXVkMENxbEhBQ19sajJEZEF4T1RPTWhySjdwMjlMUnQxM1Vkc1BJZ0JPQV9zZ2lFQnFjQWYtZXhPdks2WXlkVlJWOGRUbTRGNFhRM1FtMklZdXBNN3RaejNMVlRqYVdMaGxNc01wMXQxN09F0gHMAUFVX3lxTE5tNU1qLUgtNUZMeXFxV09hLUtJaExqVmswcUN6OXIybzdzQ1RBM0ZXOEx0TkxuVGZoNVdRMzh4MWx3M3pDemVkX0dKZFB0akg2T1BwbHlNUzRuQ0tlbjljNzU1VkxHUjRYQklOVmd1Z0xiTU5WNjExWTF6VXBRbmwteWFxVlZvTXFhOWVpNUVkSm56ZzdQbW1SbG4zaHluSEttT3F2dWlPTHRRMVFuRThEcVlmMjBBUEhlWTUweVZqelh5QWR3cDZUOVU1Sw?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPSUM0T3phd1lPUkhkRlpMdUdNVWZRYnlHNk5sLXhwSjBxd3J0OXVMb1lMaGxsMGRWMmptQVNjT3dYcUVNazZiRzBNX3dpOE0yYS1Nd2tHeXJENlQwcFV5MFlqZ3ZZNFJjWFI4RlhwN3FKbmhTcVJhWkV3dW1oTkgybExxeDBtc1plbVFXdG82V0RBQQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPV2R5bnA1Z2FTQ0tCRmFNeVJQUUZBZlFDaHloVE82YVlDcmhtZS1WTXVsVDFuZmh4V0doLW9SbXBrblFudDNQUkR0WUl2YnBoYkMyMWNmQXIwMGpTYlVCTUFoQzlVcXBEbG16RXBQOFp2eVo4ZmxoOUFuaXk2a2pmZXVIT1dGeXdHUllBSWtwNUJ4aHJyaTkzUnZR?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxOa01kRk1xSWNvSktKYmRhNUp1Y1J2RkN4YUEyVzhmLTBGYXpBOGVvclBPU3pkc0hfaU9lZWJUNjhqUjRtUmwzMjBtdEYxUFhjQVZYV3NtYkVVU2R2dEVmdDZCQWdyT3JuMy1mOVB2dnRCM3MzOXViX3AweDVWS2dLSWYtMk1rb05ycTZWQV9obXJQcnR0M1VhRFh5M0tnREdzOG9XeXRXZHdxRGc?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxOSzBMWnlUbm5zX0c1U3pNZ2FXc3pVWFdqNGRWeUZIc3dzRE9hUHZTbjF5WUtyakNia3YwWjExNWFaR1lSdHdrN3NERkZKa092XzYwN2UtUFFrbVRJRHE2a0lJM3FyQWFNdTdJc1J4V0p0S2hJOGpxQndFeWNZOVhndlBKNFM0a3Z3X3FnbzhMQ1dMZFRPS0xsbE1QVjhBY3dCSE1DMlBrSy1qaDVid1NQZkd3?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxNdUZJWVpmVWxsQ2g3enhpYUk1eGs3a2hkaXVTX21PQWtCZF9LcjB5LUJSZkNzblp5VnBWNE5FMzY4NGRzSld3UVAyUXYwM1BnMFBFcUxEX0VUMDQ0bXlDZlhyRFNXOVBoLWZrNGhBUUF6X0laakt5ME0xelhmUXlWSDNRUUd1bDdQeU9KenFR?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
