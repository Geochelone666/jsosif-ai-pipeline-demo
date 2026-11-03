# MCK Intelligence Report

- ticker: **MCK**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/MCK/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MCK/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:15:11.647836+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 7, 'rule': 1, 'ai': 5, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/MCK** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'directional_claim_without_event_type': 3}
- RSS source audit (metadata only, not article fact-checking): 7 unique headlines; 3 named publishers; 0 exact duplicates; 7 HTTPS source links; largest publisher share 71.43%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 998.3800 |
| Return 1D (%) | 0.3821 |
| Return 1W (%) | 0.5550 |
| Return 1M (%) | 10.6508 |
| Return YTD (%) | 22.0761 |
| Return 1Y (%) | 23.5377 |
| Annualized volatility (%) | 31.0874 |
| Beta vs SPY | -0.2828 |
| Max drawdown (%) | -27.1691 |
| Sharpe (rf=0) | 0.8008 |
| Downside deviation (rf=0, %) | 18.3900 |
| Sortino (rf=0) | 1.3537 |
| Historical VaR 95% (1D, %) | 2.5993 |
| Historical ES 95% (1D, %) | 3.6083 |
| Correlation vs SPY | -0.1166 |
| Tracking error vs SPY (%) | 34.9828 |
| P/E (trailing) | 26.76 |
| P/B | -27.31 |
| EV/EBITDA | 17.82 |
| Revenue growth (%) | 7.70 |
| Forward P/E (estimate) | 19.72 |
| Gross margin (%) | 3.63 |
| Operating margin (%) | 1.35 |
| Return on equity (%) | N/A |
| Free cash flow yield (%) | 5.84 |
| MA50 | 924.8617 |
| Close vs MA50 (%) | 7.9491 |
| MA200 | 862.1570 |
| Close vs MA200 (%) | 15.8003 |
| RSI (14, Wilder) | 61.5405 |
| MACD (12,26) | 21.7888 |
| MACD signal (9) | 25.2682 |
| MACD histogram | -3.4794 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MCK': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 998.3800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.3821 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.5550 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 10.6508 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 22.0761 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 23.5377 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.0874 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 18.3900 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3537 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5993 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.6083 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1166 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 34.9828 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.2828 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.1691 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8008 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 19.7188 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 3.6330 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 1.3480 -> No interpretation rule is available for this metric.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 5.8429 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 26.7590 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 61.5405 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.4794 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.9491 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 15.8003 -> Clearly above the moving-average trend level.

## TAILWINDS

### McKesson (MCK) Stock Dips While Market Gains: Key Facts
- Summary: McKesson (MCK) Stock Dips While Market Gains: Key Facts
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOUVo1eHd1dXQ2cEpOZG9ETkhlbXVJWHBpdkRXRG1rQmhSNjcxUDlzVTI3TXRRZ2llR3p1SUtnLWF6cWQ3d0piNmlWdmFRamlqNjNtY25XVDA0c3g4YVNIRW8zSEpzWDA4QWhxc0R3QnJUVXFOdXRBeVlRT1ljc2UtcS1uRlNwcDNQaUExWmdmN1ozOG5GUVFXY29B?oc=5>

### McKesson (MCK) Stock Could Be 43% Undervalued Despite Strong Cash Flow Doubts
- Summary: Potential upside if undervalued, despite cash flow concerns.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNUjJEeENFTHN4NV9HVzZYRmZQbElGQjR3WnA4UV9hRHBVZ3BVZ2l3RmpHSUpGeDBOaHFPb1hVcHJNdzF0aXUtRkY3aDJTck5naGI2elNnMlQ1R2dfbzJWODFfMC1ta2YyYmJFdml6Z3A5N2RLamVDZHNrc2xlVDNaMFRZcWJoQk1iXzk1VkhWUXE0eWt3eFFN?oc=5>

### Does McKesson (MCK) Trade Below Fair Value On Cash Flow?
- Summary: Questioning undervaluation based on cash flow metrics.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxNMFVyYjlobC1UYWhNLVRONVd0LTdDdjBuanZ6UEZUVnoyY1pWX3F3bmJYd2RNOXhOSUkwbGNuZmg0UEhFMVlDSHU0aFhtcmtNV2sxYmFrUFBpVEVick9hV2VYZFhqVmdaZFNkczRlS2t6Rms0MEc0QmxpX3NpQmUtcUxfRmtHdFlwTmk2WnE5RDJIeHhnemJYWmk1a1J4YURUVWdkZzNqNjlwamVCOE5HOVBzSEJYaVlHdDdV0gHAAUFVX3lxTE1CQ285WDdiV1FMcjJDVmlnNFJaaHpHQ1dwY3JwQVJ5XzFmN01ZS1VYLVU1TktMTEFFTjQ3UXV0MzB6VWtKTWVFNTVwVW5VbG1SdXpPOFE5eVoxaEtrc1FEeG1fYnVuNmdVbXI3T01kcGdiMHhzNnpQY19KaTdlYU9IdXdlYnJNOVpYb05mUnFFSmkzTTJsTUhReC1JU0ZleE5ReWVZcDZZM18tXzBTSXdScXJNMVMyRW8zeHA3Y0ZxSA?oc=5>

## HEADWINDS

### Earnings Uncertainty Might Change The Case For Investing In McKesson Stock
- Summary: Uncertain earnings could deter investment.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNU1JsYmpKNHcwTkVaM09pOHZTQUFERl9odFFaU2FkMno2Zk44N01GalBpMlpHejNhV3dnRkF6TFZMNE9XV1Q4MkY0ejNMY0xjSFNYUTRya0dKMTVjZlQ5d0hZRW90UGQ2ZGRwdHBFeE5VUjhaZ3d0TUU1RVgwaTliV3VDUkNlVU85REdzTHl2Z0d2eThOQkhsSFI5c2d5LTJmSExCR1JB?oc=5>

## CATALYSTS

### Stay Ahead of the Game With McKesson (MCK) Q2 Earnings: Wall Street's Insights on Key Metrics
- Summary: McKesson reported Q2 earnings, detailing revenue, operating income, and guidance for the next quarter.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQM0l4Y2hyMUlGNXBuYWFKaUZlSXFKU2pwSU1JMV9JMFVtSkc2MEt1NGpYODM0Q2UtQVlaTkFMYW9VMFpNd0VEZER5WmNTbDJNeUM1QldHcWNrWjFQRngyVTlVZklFVDBxVDI4WlZpdHVXck5CdU1uOTk0MVZTUXlSNXFueV90a09VbVVSWlNrY0xUcjRLeUY3cg?oc=5>

### McKesson (MCK) Surged 13% Following Strong Q3 Results
- Summary: McKesson’s Q3 earnings beat expectations, driving a 13% stock jump.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOXzZNN0F1OVZZdVNGVVM0eUNNQ29vQ2lqZWlpRXN0QkpZQ1B0d0xMZlkxdE9oZm5hanhEZy16dU9lT1ZWQldzdFdhUmlYMl9PMUFkSHU2aEFtdllOcW1TWmFQcFRwOVdIQ0t1NmlIOWdLY0Z3U0pDTU9rUFJIMEkwdmhBOS15ck8zNVNoXzVFeTZ6WldFSkZRVg?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MCK** | **26.76** | **-27.31** | **17.82** | **7.70** | **116,401,487,872.00 USD** | **23.54** |
| COR | 25.08 | 21.13 | 13.76 | 5.10 | 64,469,049,344.00 USD | 0.77 |
| CAH | 34.65 | -20.56 | 15.19 | 5.80 | 58,892,488,704.00 USD | 34.58 |
| CNC | 22.86 | 1.48 | 5.33 | 0.20 | 32,936,873,984.00 USD | 88.10 |

Peers fetched as_of: 2026-11-02; MCK reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-05
- Next expected earnings: 2026-11-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-05
- Revenue (latest available single quarter): 29,980,000,000.00 USD; period 2011-04-01/2011-06-30; fiscal year/reporting period 2011/Q1
- Net income (latest available single quarter): 614,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/927653/000092765326000234/mck-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimgFBVV95cUxOUVo1eHd1dXQ2cEpOZG9ETkhlbXVJWHBpdkRXRG1rQmhSNjcxUDlzVTI3TXRRZ2llR3p1SUtnLWF6cWQ3d0piNmlWdmFRamlqNjNtY25XVDA0c3g4YVNIRW8zSEpzWDA4QWhxc0R3QnJUVXFOdXRBeVlRT1ljc2UtcS1uRlNwcDNQaUExWmdmN1ozOG5GUVFXY29B?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNUjJEeENFTHN4NV9HVzZYRmZQbElGQjR3WnA4UV9hRHBVZ3BVZ2l3RmpHSUpGeDBOaHFPb1hVcHJNdzF0aXUtRkY3aDJTck5naGI2elNnMlQ1R2dfbzJWODFfMC1ta2YyYmJFdml6Z3A5N2RLamVDZHNrc2xlVDNaMFRZcWJoQk1iXzk1VkhWUXE0eWt3eFFN?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxNMFVyYjlobC1UYWhNLVRONVd0LTdDdjBuanZ6UEZUVnoyY1pWX3F3bmJYd2RNOXhOSUkwbGNuZmg0UEhFMVlDSHU0aFhtcmtNV2sxYmFrUFBpVEVick9hV2VYZFhqVmdaZFNkczRlS2t6Rms0MEc0QmxpX3NpQmUtcUxfRmtHdFlwTmk2WnE5RDJIeHhnemJYWmk1a1J4YURUVWdkZzNqNjlwamVCOE5HOVBzSEJYaVlHdDdV0gHAAUFVX3lxTE1CQ285WDdiV1FMcjJDVmlnNFJaaHpHQ1dwY3JwQVJ5XzFmN01ZS1VYLVU1TktMTEFFTjQ3UXV0MzB6VWtKTWVFNTVwVW5VbG1SdXpPOFE5eVoxaEtrc1FEeG1fYnVuNmdVbXI3T01kcGdiMHhzNnpQY19KaTdlYU9IdXdlYnJNOVpYb05mUnFFSmkzTTJsTUhReC1JU0ZleE5ReWVZcDZZM18tXzBTSXdScXJNMVMyRW8zeHA3Y0ZxSA?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNU1JsYmpKNHcwTkVaM09pOHZTQUFERl9odFFaU2FkMno2Zk44N01GalBpMlpHejNhV3dnRkF6TFZMNE9XV1Q4MkY0ejNMY0xjSFNYUTRya0dKMTVjZlQ5d0hZRW90UGQ2ZGRwdHBFeE5VUjhaZ3d0TUU1RVgwaTliV3VDUkNlVU85REdzTHl2Z0d2eThOQkhsSFI5c2d5LTJmSExCR1JB?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQM0l4Y2hyMUlGNXBuYWFKaUZlSXFKU2pwSU1JMV9JMFVtSkc2MEt1NGpYODM0Q2UtQVlaTkFMYW9VMFpNd0VEZER5WmNTbDJNeUM1QldHcWNrWjFQRngyVTlVZklFVDBxVDI4WlZpdHVXck5CdU1uOTk0MVZTUXlSNXFueV90a09VbVVSWlNrY0xUcjRLeUY3cg?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOXzZNN0F1OVZZdVNGVVM0eUNNQ29vQ2lqZWlpRXN0QkpZQ1B0d0xMZlkxdE9oZm5hanhEZy16dU9lT1ZWQldzdFdhUmlYMl9PMUFkSHU2aEFtdllOcW1TWmFQcFRwOVdIQ0t1NmlIOWdLY0Z3U0pDTU9rUFJIMEkwdmhBOS15ck8zNVNoXzVFeTZ6WldFSkZRVg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
