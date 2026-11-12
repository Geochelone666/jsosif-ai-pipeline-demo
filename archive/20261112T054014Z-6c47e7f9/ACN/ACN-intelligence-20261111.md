# ACN Intelligence Report

- ticker: **ACN**
- Report as_of: **2026-11-11**
- Market data as_of: **2026-11-11**
- Quant sources: https://finance.yahoo.com/quote/ACN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ACN/key-statistics/
- AI analysis snapshot as_of: **2026-11-11**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-12T05:52:36.248310+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 13, 'rule': 3, 'ai': 3, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261111T043601Z-d14951e6/ACN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 13 unique headlines; 8 named publishers; 0 exact duplicates; 13 HTTPS source links; largest publisher share 30.77%; oldest publication 2026-11-04

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 253.6600 |
| Return 1D (%) | -1.8761 |
| Return 1W (%) | -4.0148 |
| Return 1M (%) | 22.3069 |
| Return YTD (%) | -2.7343 |
| Return 1Y (%) | 7.5874 |
| Annualized volatility (%) | 50.0244 |
| Beta vs SPY | -0.0534 |
| Max drawdown (%) | -56.5068 |
| Sharpe (rf=0) | 0.3978 |
| Downside deviation (rf=0, %) | 34.7097 |
| Sortino (rf=0) | 0.5734 |
| Historical VaR 95% (1D, %) | 4.5949 |
| Historical ES 95% (1D, %) | 6.8005 |
| Correlation vs SPY | -0.0146 |
| Tracking error vs SPY (%) | 52.0677 |
| P/E (trailing) | 18.71 |
| P/B | 4.79 |
| EV/EBITDA | 11.33 |
| Revenue growth (%) | 6.20 |
| Forward P/E (estimate) | 15.95 |
| Gross margin (%) | 32.05 |
| Operating margin (%) | 16.42 |
| Return on equity (%) | 26.02 |
| Free cash flow yield (%) | 7.13 |
| MA50 | 213.4548 |
| Close vs MA50 (%) | 18.8355 |
| MA200 | 187.5255 |
| Close vs MA200 (%) | 35.2670 |
| RSI (14, Wilder) | 59.6324 |
| MACD (12,26) | 13.4180 |
| MACD signal (9) | 15.0079 |
| MACD histogram | -1.5899 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ACN': 280, 'SPY': 280}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 253.6600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.8761 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.0148 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 22.3069 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -2.7343 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 7.5874 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 50.0244 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 34.7097 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.5734 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.5949 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.8005 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0146 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 52.0677 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.0534 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -56.5068 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3978 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.9456 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 32.0500 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.4190 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 26.0250 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.1303 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.7065 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 59.6324 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.5899 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 18.8355 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 35.2670 -> Clearly above the moving-average trend level.

## TAILWINDS

### Accenture (ACN) Stock Looks Fairly Priced After Its 25% Jump
- Summary: Accenture (ACN) Stock Looks Fairly Priced After Its 25% Jump
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPRGdRY1FwaW1HUzF5SjRMOE5ULWJFX2ZUYWQ4Qm5tWjdfY0Z5Z3IxYjNZVlo1eFEybng0MFNMbW5Xb29aRUhzN3p3VDlBS3RmRXVLVEFmb0xIc2JYYllxODNxQVFXZExnNUpmUzVjeFdBdDBLdkpWb2VOdXhyX0FsU0RlSDNBZmNyRzhRdmtwTnV3N29QMlhsdms5U256QWlsODZ6Vzk0a2xVbjIzd1RqZElVMmJqNlVNQUNCNmVGMNIBxAFBVV95cUxOY0hhTmNwVlRMWENKSm5TckJwYnpzd2RWSnpuRWxwbFJiNUlkTXp1c0dpcUt0bzdwZWZpWTlfT1ZuMjFYVGp5TExiSHFPRHBQYzUtVkExdVZrSE9sXzFQdGRJLTBuTTFDbm1ORDZfcHE1Y2c4MjRaSFV6YWxFM0RfeXo4b21CMlgzc3V4dEhmWDdPOEg5aC1WZ0ZDS3BSYnl6VlNxNTNmRk95VFJyd0NsYzJYd01Xb1V3ZjcyeDZ2MXZtbllS?oc=5>

### Accenture Stock Rallied 31.5% Since October 6. Is Cognizant Now the Better Buy?
- Summary: Accenture Stock Rallied 31.5% Since October 6. Is Cognizant Now the Better Buy?
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNa3NyVmdza0xUZGJOWElXMkdtVXA3RnVUaWFRaTQ2NlFILXJCWF9JNnZxV0FJTmY2b3JfTjJocF95ckJ2NW5WMWdSSkRkUWp2a3dadlc2VzlOUEJ5ZHZuRzhnMk0xdHBhZWF1T3V3LVRPc1QwUV8wdkR0OEhvRVJjc1hxa2xYQnBKRnRvOXBoWHZ4Zkkwbk0ya2N6LXFCQWlBZnJld3l3?oc=5>

### Accenture PLC (ACN) Shares Surge 3.8% -- What GF Score of 94 Tel
- Summary: Accenture PLC (ACN) Shares Surge 3.8% -- What GF Score of 94 Tel
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQOEFlWW5RdW1VYWpSeEdhbHdhbldLQ1gzdi1xd3Zwcm1ackNhU3RJdWMxVHpvcWtLUkFTb25TRUZKWUwtOWp5Sm83UzdHOFhXMDBOb1pfaGhyUWRiaW1iX3lCcnhUWXRtN1RnV0JBZTFNYkpTVkl1dlZjOVc0VGhHUmRiMkpUZjRENUREck1RM1dZenIwU19MTEFZZXVPeFlYZGh0bk5STVBzQTNI?oc=5>

### Why Is Accenture (NYSE:ACN) Expanding Its AI Capabilities?
- Summary: Accenture is expanding AI capabilities, indicating product development.
- Date: 2026-11-09 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNTUtPYVV4RksxMDluN1hFMFlFRlI4b0tvMnAtM05iT1RfcXB5bUJCLXZyWW8tX0w2VjVjNzBpYzhpTzR0cVJndVN6NVFMZUx1Z3NYUW9qTThqOGZOaml6cl9fMmNCODJ1SXk2bDVmTGJnSnh4M3pNSmpvcS1Ec3BWU2pGSWNxYUNjaWs4cXlnSkNwWE5aM1RuWVRKLWdZalU?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Accenture (ACN) Following WSIB Win Has An Undervalued Narrative To Defend
- Summary: Accenture follows a WSIB win, arguing its narrative is undervalued.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxONFFwV3EzQVJnZXMwRjFQOGF5dGRFWHBrUXJsTTZDa2ZnSzlvS3JWU0ZfNU9OZnRmbU9mZDVNZjJZNFRLeU5MdkJiNlN3MG9ERXJOS2gyZWFOUlBQUEhkejJNdm1kRGtmbkpJMVhJN1Zrb3NGakxFVUZGUHJ6enJCLXhKQ3VaeFY1dDBneGs3bmVhUWduQ3pxTzFjczR3dw?oc=5>

### Analysts Lifted Accenture’s Price Targets After a 31% Rally. Did Their Earnings Estimates Move Too?
- Summary: Analysts raised price targets following a 31% rally, questioning earnings estimates.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxPX0JMRkJCSF9BY0J6NmhKRjdPSGxORzZDR1BhN25pd2dONm4tV2tETHpjQ25hcUtqVU9wMUxITHlRam5OVEszc3JHemlIcWU3U2ZDYTNab21fT3FqcklGaGRFMEZoT3g0MGdPRGlablo4TWJCaW9aQXhnYkV0YkdTLVJLZ243NXpmVU5QRzd3?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ACN** | **18.71** | **4.79** | **11.33** | **6.20** | **149,846,474,752.00 USD** | **7.59** |
| IBM | 21.18 | 6.60 | 17.52 | 4.70 | 234,597,892,096.00 USD | -18.71 |
| CTSH | 11.87 | 1.96 | 7.15 | 4.60 | 28,802,170,880.00 USD | -9.91 |
| INFY | 15.57 | 9.64 | 19.72 | 1.40 | 49,819,631,616.00 USD | -26.13 |

Peers fetched as_of: 2026-11-11; ACN reuses existing data (market data as_of: 2026-11-11); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-01
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-11

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-16
- Revenue (latest available single quarter): 18,679,110,000.00 USD; period 2026-06-01/2026-08-31; fiscal year/reporting period 2026/FY
- Net income (latest available single quarter): 1,991,267,000.00 USD; period 2026-06-01/2026-08-31; fiscal year/reporting period 2026/FY
- SEC link: https://www.sec.gov/Archives/edgar/data/1467373/000146737326000049/acn-20260831.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMivwFBVV95cUxPRGdRY1FwaW1HUzF5SjRMOE5ULWJFX2ZUYWQ4Qm5tWjdfY0Z5Z3IxYjNZVlo1eFEybng0MFNMbW5Xb29aRUhzN3p3VDlBS3RmRXVLVEFmb0xIc2JYYllxODNxQVFXZExnNUpmUzVjeFdBdDBLdkpWb2VOdXhyX0FsU0RlSDNBZmNyRzhRdmtwTnV3N29QMlhsdms5U256QWlsODZ6Vzk0a2xVbjIzd1RqZElVMmJqNlVNQUNCNmVGMNIBxAFBVV95cUxOY0hhTmNwVlRMWENKSm5TckJwYnpzd2RWSnpuRWxwbFJiNUlkTXp1c0dpcUt0bzdwZWZpWTlfT1ZuMjFYVGp5TExiSHFPRHBQYzUtVkExdVZrSE9sXzFQdGRJLTBuTTFDbm1ORDZfcHE1Y2c4MjRaSFV6YWxFM0RfeXo4b21CMlgzc3V4dEhmWDdPOEg5aC1WZ0ZDS3BSYnl6VlNxNTNmRk95VFJyd0NsYzJYd01Xb1V3ZjcyeDZ2MXZtbllS?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNa3NyVmdza0xUZGJOWElXMkdtVXA3RnVUaWFRaTQ2NlFILXJCWF9JNnZxV0FJTmY2b3JfTjJocF95ckJ2NW5WMWdSSkRkUWp2a3dadlc2VzlOUEJ5ZHZuRzhnMk0xdHBhZWF1T3V3LVRPc1QwUV8wdkR0OEhvRVJjc1hxa2xYQnBKRnRvOXBoWHZ4Zkkwbk0ya2N6LXFCQWlBZnJld3l3?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQOEFlWW5RdW1VYWpSeEdhbHdhbldLQ1gzdi1xd3Zwcm1ackNhU3RJdWMxVHpvcWtLUkFTb25TRUZKWUwtOWp5Sm83UzdHOFhXMDBOb1pfaGhyUWRiaW1iX3lCcnhUWXRtN1RnV0JBZTFNYkpTVkl1dlZjOVc0VGhHUmRiMkpUZjRENUREck1RM1dZenIwU19MTEFZZXVPeFlYZGh0bk5STVBzQTNI?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNTUtPYVV4RksxMDluN1hFMFlFRlI4b0tvMnAtM05iT1RfcXB5bUJCLXZyWW8tX0w2VjVjNzBpYzhpTzR0cVJndVN6NVFMZUx1Z3NYUW9qTThqOGZOaml6cl9fMmNCODJ1SXk2bDVmTGJnSnh4M3pNSmpvcS1Ec3BWU2pGSWNxYUNjaWs4cXlnSkNwWE5aM1RuWVRKLWdZalU?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxONFFwV3EzQVJnZXMwRjFQOGF5dGRFWHBrUXJsTTZDa2ZnSzlvS3JWU0ZfNU9OZnRmbU9mZDVNZjJZNFRLeU5MdkJiNlN3MG9ERXJOS2gyZWFOUlBQUEhkejJNdm1kRGtmbkpJMVhJN1Zrb3NGakxFVUZGUHJ6enJCLXhKQ3VaeFY1dDBneGs3bmVhUWduQ3pxTzFjczR3dw?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPX0JMRkJCSF9BY0J6NmhKRjdPSGxORzZDR1BhN25pd2dONm4tV2tETHpjQ25hcUtqVU9wMUxITHlRam5OVEszc3JHemlIcWU3U2ZDYTNab21fT3FqcklGaGRFMEZoT3g0MGdPRGlablo4TWJCaW9aQXhnYkV0YkdTLVJLZ243NXpmVU5QRzd3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
