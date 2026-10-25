# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-10-24**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-10-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-25T00:46:46.708521+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 4, 'ai': 3, 'unknown': 0, 'irrelevant': 17})
- AI model(s) actually used: **openai/gpt-oss-20b**
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 13 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 37.5%; oldest publication 2026-10-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 516.7900 |
| Return 1D (%) | 1.7443 |
| Return 1W (%) | -2.2619 |
| Return 1M (%) | -15.9158 |
| Return YTD (%) | 141.3102 |
| Return 1Y (%) | 119.9200 |
| Annualized volatility (%) | 68.3445 |
| Beta vs SPY | 3.2410 |
| Max drawdown (%) | -27.7608 |
| Sharpe (rf=0) | 1.4970 |
| Downside deviation (rf=0, %) | 42.8038 |
| Sortino (rf=0) | 2.3903 |
| Historical VaR 95% (1D, %) | 5.8580 |
| Historical ES 95% (1D, %) | 8.2198 |
| Correlation vs SPY | 0.6045 |
| Tracking error vs SPY (%) | 61.4836 |
| P/E (trailing) | 131.83 |
| P/B | 12.55 |
| EV/EBITDA | 87.31 |
| Revenue growth (%) | 50.10 |
| Forward P/E (estimate) | 32.79 |
| Gross margin (%) | 55.72 |
| Operating margin (%) | 17.25 |
| Return on equity (%) | 10.20 |
| Free cash flow yield (%) | 1.05 |
| MA50 | 542.2794 |
| Close vs MA50 (%) | -4.7004 |
| MA200 | 402.0832 |
| Close vs MA200 (%) | 28.5281 |
| RSI (14, Wilder) | 38.9761 |
| MACD (12,26) | -9.9345 |
| MACD signal (9) | 4.0147 |
| MACD histogram | -13.9492 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 516.7900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.7443 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.2619 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -15.9158 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 141.3102 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 119.9200 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 68.3445 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 42.8038 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.3903 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 5.8580 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 8.2198 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6045 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 61.4836 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.2410 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.7608 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.4970 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 32.7852 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 55.7240 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.2500 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.1960 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0480 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 131.8342 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.9761 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -13.9492 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -4.7004 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 28.5281 -> Clearly above the moving-average trend level.

## TAILWINDS

### Advanced Micro Devices (NASDAQ:AMD) Stock Price Up 1.7% - Here's Why
- Summary: Advanced Micro Devices (NASDAQ:AMD) Stock Price Up 1.7% - Here's Why
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPeXduSXo5TnJHYXpRNVBMc1NJQXhUcVpEd0RtWU90bVVxMmdkblRRNVBiLW56NHlCOUp6S0lselpjQXdUR1FyWnZiV3ZYU05DQXJHOFlaMUJuT1JDbk45ZHhOWFRKbVQ4eGY4R2RoWmZCVlBBMUduTnlWYnBhQlZIcHlYTmRfSzBTVjA4NmxvWWQyUkhmbTk3TmlnWkRCMXBCaFB2ZFlSMVpFLUJGS0UzSFZKdVNkc2JYYmhkUnB3?oc=5>

### Does The Move In AMD Stock Change Anything?
- Summary: Discussion on whether recent AMD stock movement impacts the company.
- Date: 2026-10-22 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPcjJRMDVEMzlYTzhBRFRBbEZEbkJSLWtvLXkzY3FzVXVfVTNkc3hmNkEzYXI2YzNrdkVwS1BadnFYWmNfcW5MWTNILUduVWZYTkw4OU5feS1JcEZndkxyUkRsR0U5a1ZidjlFUVliV0xuTzgtb1lNR0UtLUIwSmxad0FTNkIwd2p2RF9oMnRsT3FHczNkblFtelN3UFBnUGhrZF93Sw?oc=5>

### Why is Advanced Micro Devices stock sliding today?
- Summary: Analysis of AMD stock slide and potential causes.
- Date: 2026-10-22 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxOZ1dnc1ZUV1F6R1R1V25JMExWellfT1dwUFhuSG14alNqVGhQN1kyRWJPX0V5SWhjY0N4dkdpQnV0M2dET2lZV2VEYjN6Q3UxQmdYYS1SeEFvOW5WTzlJYlNWSHl6Ump5NGVpZUh6R2w0UnNRVERzTTQyV1lueHBzQ3UtTVNLdDM0eEFXZk1PbEFuTEZ2YmN4OWZhODNMbUxUWG9OampKeDF6dXBERVJybg?oc=5>

## HEADWINDS

### AMD Stock Fell 8% in a Day as Lam Research’s Supply Warning Sank Chip Stocks. Here’s Where the Stock Could Go by 2030
- Summary: AMD Stock Fell 8% in a Day as Lam Research’s Supply Warning Sank Chip Stocks. Here’s Where the Stock Could Go by 2030
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxQX180eHE3R3dPZGxZZngtbDlRbk53Q1kyZnUtaTcwZEZRZE1PeGwxMC05UTFVMWhzT09hanoxeDVLTGN0Ry1tRXdvUTFsTTVNbWJOOVRET0ppRmhuaU1pWnpUcUotVGxraEwxSlB1UXlabVJOY2xzaC1IQTZaWEhjMUxhbUNlQzZpSE43VXVZQ2lFV2R5REUyTmdyLU1RWjV3VmJsVEFzYy1xU2hOblpPdFVkbUxWZDRwY0xHdklETlRQVVdiazZ6SGVaOTZ4RGtfRUNnVi1B?oc=5>

### AMD pulled lower by tech slide, falls 8% (AMD:NASDAQ)
- Summary: AMD pulled lower by tech slide, falls 8% (AMD:NASDAQ)
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxPY2lkd3hiVjE5em5HUHJFQXlMT1h6TU5mUWpNbVVmc0J5a2Jvc2pkVHkxellvSFZtb3FSdEpDWVBBV2lmLUtEODFkUWVuWmxrX291STAzWjlBc3NKNThCR1lZVGdCUzdXMS1adFhOVXgyTGlUVG5NV2xjNVRoV05wRVNn?oc=5>

### AMD Stock Drops 7% in Chip Sell-Off - Here's Why
- Summary: AMD Stock Drops 7% in Chip Sell-Off - Here's Why
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNM3VPRURJWHYtb2thbFlGa283LUhseWRJcnNOaVdnNHdFU183c24wTS1jdThnREZBNjJCRGRkbThObWRxc0V3ZHIyVlUyQWdyZ0FGLXdvSHdBT200cklRWDFKTnJtUFotYjEzemRaSlZnN2ZCeVlfSDZETURlUVNvYUdnZzdrWjgzdjFBeG5YOHZNTEF5SmxiaW5kLWVpTF9abllkZU9fRmY?oc=5>

## CATALYSTS

No items in this run

## RISKS

### Why Are Nvidia, AMD and Micron Stocks Crashing Today? AI Spending Fears Hit Chips
- Summary: AMD stock crash amid AI spending fears affecting chip sector.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTE0zc25iZ1RZenM5U3N2QkJMQ2Q1UVBscjFreDQ5cDZ1LW1EUGdiNVFHU2JIeEJmajJfaThMN3RqNExGNWRnVFlqblEtb0o2OFMwaF9FZmJicloxemtoZzJRNFhtOXhmMXI4YWxtd2ZEcklyRDZOVWNyZ1RMTXhxWTg?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **131.83** | **12.55** | **87.31** | **50.10** | **843,646,697,472.00 USD** | **119.92** |
| NVDA | 26.67 | 22.25 | 25.14 | 105.90 | 5,094,050,889,728.00 USD | 16.09 |
| INTC | N/A | 5.01 | 28.21 | 25.40 | 459,679,694,848.00 USD | 127.88 |
| AVGO | 42.95 | 15.40 | 30.06 | 85.50 | 1,535,581,224,960.00 USD | -5.87 |

Peers fetched as_of: 2026-10-24; AMD reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-03 (yfinance; expected dates may change)

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
- Filing date: 2026-08-05
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,297,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMivgFBVV95cUxPeXduSXo5TnJHYXpRNVBMc1NJQXhUcVpEd0RtWU90bVVxMmdkblRRNVBiLW56NHlCOUp6S0lselpjQXdUR1FyWnZiV3ZYU05DQXJHOFlaMUJuT1JDbk45ZHhOWFRKbVQ4eGY4R2RoWmZCVlBBMUduTnlWYnBhQlZIcHlYTmRfSzBTVjA4NmxvWWQyUkhmbTk3TmlnWkRCMXBCaFB2ZFlSMVpFLUJGS0UzSFZKdVNkc2JYYmhkUnB3?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPcjJRMDVEMzlYTzhBRFRBbEZEbkJSLWtvLXkzY3FzVXVfVTNkc3hmNkEzYXI2YzNrdkVwS1BadnFYWmNfcW5MWTNILUduVWZYTkw4OU5feS1JcEZndkxyUkRsR0U5a1ZidjlFUVliV0xuTzgtb1lNR0UtLUIwSmxad0FTNkIwd2p2RF9oMnRsT3FHczNkblFtelN3UFBnUGhrZF93Sw?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxOZ1dnc1ZUV1F6R1R1V25JMExWellfT1dwUFhuSG14alNqVGhQN1kyRWJPX0V5SWhjY0N4dkdpQnV0M2dET2lZV2VEYjN6Q3UxQmdYYS1SeEFvOW5WTzlJYlNWSHl6Ump5NGVpZUh6R2w0UnNRVERzTTQyV1lueHBzQ3UtTVNLdDM0eEFXZk1PbEFuTEZ2YmN4OWZhODNMbUxUWG9OampKeDF6dXBERVJybg?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQX180eHE3R3dPZGxZZngtbDlRbk53Q1kyZnUtaTcwZEZRZE1PeGwxMC05UTFVMWhzT09hanoxeDVLTGN0Ry1tRXdvUTFsTTVNbWJOOVRET0ppRmhuaU1pWnpUcUotVGxraEwxSlB1UXlabVJOY2xzaC1IQTZaWEhjMUxhbUNlQzZpSE43VXVZQ2lFV2R5REUyTmdyLU1RWjV3VmJsVEFzYy1xU2hOblpPdFVkbUxWZDRwY0xHdklETlRQVVdiazZ6SGVaOTZ4RGtfRUNnVi1B?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxPY2lkd3hiVjE5em5HUHJFQXlMT1h6TU5mUWpNbVVmc0J5a2Jvc2pkVHkxellvSFZtb3FSdEpDWVBBV2lmLUtEODFkUWVuWmxrX291STAzWjlBc3NKNThCR1lZVGdCUzdXMS1adFhOVXgyTGlUVG5NV2xjNVRoV05wRVNn?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNM3VPRURJWHYtb2thbFlGa283LUhseWRJcnNOaVdnNHdFU183c24wTS1jdThnREZBNjJCRGRkbThObWRxc0V3ZHIyVlUyQWdyZ0FGLXdvSHdBT200cklRWDFKTnJtUFotYjEzemRaSlZnN2ZCeVlfSDZETURlUVNvYUdnZzdrWjgzdjFBeG5YOHZNTEF5SmxiaW5kLWVpTF9abllkZU9fRmY?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTE0zc25iZ1RZenM5U3N2QkJMQ2Q1UVBscjFreDQ5cDZ1LW1EUGdiNVFHU2JIeEJmajJfaThMN3RqNExGNWRnVFlqblEtb0o2OFMwaF9FZmJicloxemtoZzJRNFhtOXhmMXI4YWxtd2ZEcklyRDZOVWNyZ1RMTXhxWTg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
