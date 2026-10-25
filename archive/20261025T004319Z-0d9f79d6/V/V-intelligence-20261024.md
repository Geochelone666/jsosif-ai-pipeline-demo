# V Intelligence Report

- ticker: **V**
- Report as_of: **2026-10-24**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/V/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/V/key-statistics/
- AI analysis snapshot as_of: **2026-10-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-25T01:27:39.894820+00:00**
- AI status: **N/A: AI unavailable: Groq application daily budget exhausted (tokens)**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 21, 'rule': 3, 'ai': 0, 'unknown': 18})
- AI model(s) actually used: **N/A (no successful AI classification call)**
- RSS source audit (metadata only, not article fact-checking): 21 unique headlines; 10 named publishers; 0 exact duplicates; 21 HTTPS source links; largest publisher share 28.57%; oldest publication 2026-10-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 407.9200 |
| Return 1D (%) | -1.5494 |
| Return 1W (%) | 1.3189 |
| Return 1M (%) | 12.8347 |
| Return YTD (%) | 17.0111 |
| Return 1Y (%) | 18.8526 |
| Annualized volatility (%) | 22.2189 |
| Beta vs SPY | 0.2810 |
| Max drawdown (%) | -17.1805 |
| Sharpe (rf=0) | 0.8904 |
| Downside deviation (rf=0, %) | 13.9071 |
| Sortino (rf=0) | 1.4226 |
| Historical VaR 95% (1D, %) | 1.7961 |
| Historical ES 95% (1D, %) | 2.6824 |
| Correlation vs SPY | 0.1612 |
| Tracking error vs SPY (%) | 23.7663 |
| P/E (trailing) | 34.72 |
| P/B | 21.62 |
| EV/EBITDA | 24.45 |
| Revenue growth (%) | 14.40 |
| Forward P/E (estimate) | 27.15 |
| Gross margin (%) | 97.72 |
| Operating margin (%) | 66.13 |
| Return on equity (%) | 61.19 |
| Free cash flow yield (%) | 2.66 |
| MA50 | 377.0662 |
| Close vs MA50 (%) | 8.1826 |
| MA200 | 339.7616 |
| Close vs MA200 (%) | 20.0607 |
| RSI (14, Wilder) | 70.0175 |
| MACD (12,26) | 10.8560 |
| MACD signal (9) | 8.0276 |
| MACD histogram | 2.8284 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'V': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 407.9200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.5494 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.3189 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 12.8347 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 17.0111 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 18.8526 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.2189 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.9071 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4226 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.7961 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6824 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1612 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.7663 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2810 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -17.1805 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8904 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 27.1523 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.7250 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.1310 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 61.1900 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.6644 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 34.7166 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 70.0175 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 2.8284 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 8.1826 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 20.0607 -> Clearly above the moving-average trend level.

## TAILWINDS

N/A: AI unavailable: Groq application daily budget exhausted (tokens)

## HEADWINDS

### Visa (NYSE:V) Stock Falls 1.5% - Here's What Happened
- Summary: Visa (NYSE:V) Stock Falls 1.5% - Here's What Happened
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOZDY4S2RIempKSjBIYnZETWVPdkRKcG1CT3NKbGFxbHN1QndIYThkY0V4ZzlqejRSV3laQnIwRVR1ZDNNWGpvV0lvckFLN1hxNjBIQjFiWWc1NzA5MmJSS3I2XzZZMzdFME05dWZrZVBVbzAwcWFtRnIxZng1ZGwtY1pTVC1fRGNZeWtHb3BZYlNZYVRCQzY2Z3A1bEhBYVFnUXQxcnFlXy11QQ?oc=5>

## CATALYSTS

### Visa Inc. $V Stock: Sepio Capital LP Lowers Stake
- Summary: Visa Inc. $V Stock: Sepio Capital LP Lowers Stake
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxOT0JiWGVuZ1drazV1bzVoMGRObThoQnRCN0JEWmR6WTFRWmVCalZZTmstWXBFQzZZSWphZTJjUGxKQkx6cnVOcWR0dXdhX3pwaUhBakhRcXJNODBmVS1KTFVPMTBYTThyX2hjc0FGSEUyVDh3VHY4Tk96eERVMllnaE5sY1lSMnJyNFg5WGlncFVvWmxrNGk3NWV1VEdYQ1NnblVNeHdPc044N2M?oc=5>

### Visa Inc. $V Stock Sold by Axxcess Wealth Management LLC
- Summary: Visa Inc. $V Stock Sold by Axxcess Wealth Management LLC
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxQRldWcnpJTmZ3YWd1Vm45RXR6ZG9kMHZZazlNbERidDQ3UDdCYldhZDRDT01DeDVrT3Azd3Y4dTFCdDh1YzRqSEwwNTR1dmRQWFdvSm9aY2pXc21kdl9ibk54Yk1QZ2pYTDdtZzhJNlllWlpMeVhpVkczSV94SGFPUC1nallpQ0RUUzdVYnJIejlrRFVETGhTODFLdTU1Tl8tOWtubmhiREcyWmRNcm5tV3ZJV2RiUQ?oc=5>

## RISKS

N/A: AI unavailable: Groq application daily budget exhausted (tokens)

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **V** | **34.72** | **21.62** | **24.45** | **14.40** | **765,810,769,920.00 USD** | **18.85** |
| MA | 34.30 | 97.50 | 25.19 | 14.10 | 546,279,751,680.00 USD | 9.38 |
| PYPL | 10.78 | 2.48 | 8.02 | 4.80 | 48,778,379,264.00 USD | -17.23 |
| AXP | 19.01 | 5.89 | N/A | 15.30 | 211,520,536,576.00 USD | -10.76 |

Peers fetched as_of: 2026-10-24; V reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-28
- Next expected earnings: 2026-10-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOZDY4S2RIempKSjBIYnZETWVPdkRKcG1CT3NKbGFxbHN1QndIYThkY0V4ZzlqejRSV3laQnIwRVR1ZDNNWGpvV0lvckFLN1hxNjBIQjFiWWc1NzA5MmJSS3I2XzZZMzdFME05dWZrZVBVbzAwcWFtRnIxZng1ZGwtY1pTVC1fRGNZeWtHb3BZYlNZYVRCQzY2Z3A1bEhBYVFnUXQxcnFlXy11QQ?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxOT0JiWGVuZ1drazV1bzVoMGRObThoQnRCN0JEWmR6WTFRWmVCalZZTmstWXBFQzZZSWphZTJjUGxKQkx6cnVOcWR0dXdhX3pwaUhBakhRcXJNODBmVS1KTFVPMTBYTThyX2hjc0FGSEUyVDh3VHY4Tk96eERVMllnaE5sY1lSMnJyNFg5WGlncFVvWmxrNGk3NWV1VEdYQ1NnblVNeHdPc044N2M?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQRldWcnpJTmZ3YWd1Vm45RXR6ZG9kMHZZazlNbERidDQ3UDdCYldhZDRDT01DeDVrT3Azd3Y4dTFCdDh1YzRqSEwwNTR1dmRQWFdvSm9aY2pXc21kdl9ibk54Yk1QZ2pYTDdtZzhJNlllWlpMeVhpVkczSV94SGFPUC1nallpQ0RUUzdVYnJIejlrRFVETGhTODFLdTU1Tl8tOWtubmhiREcyWmRNcm5tV3ZJV2RiUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
