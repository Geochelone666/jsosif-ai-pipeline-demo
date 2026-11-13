# ACN Intelligence Report

- ticker: **ACN**
- Report as_of: **2026-11-12**
- Market data as_of: **2026-11-12**
- Quant sources: https://finance.yahoo.com/quote/ACN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ACN/key-statistics/
- AI analysis snapshot as_of: **2026-11-12**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-13T05:03:17.566620+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 14, 'rule': 2, 'ai': 6, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261112T054014Z-6c47e7f9/ACN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 14 unique headlines; 8 named publishers; 0 exact duplicates; 14 HTTPS source links; largest publisher share 28.57%; oldest publication 2026-11-06

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 249.9500 |
| Return 1D (%) | -1.4626 |
| Return 1W (%) | -5.7362 |
| Return 1M (%) | 17.2593 |
| Return YTD (%) | -4.1569 |
| Return 1Y (%) | 4.3066 |
| Annualized volatility (%) | 50.0235 |
| Beta vs SPY | -0.0501 |
| Max drawdown (%) | -56.5068 |
| Sharpe (rf=0) | 0.3357 |
| Downside deviation (rf=0, %) | 34.7406 |
| Sortino (rf=0) | 0.4833 |
| Historical VaR 95% (1D, %) | 4.5949 |
| Historical ES 95% (1D, %) | 6.8005 |
| Correlation vs SPY | -0.0137 |
| Tracking error vs SPY (%) | 52.0566 |
| P/E (trailing) | 18.43 |
| P/B | 4.72 |
| EV/EBITDA | 11.17 |
| Revenue growth (%) | 6.20 |
| Forward P/E (estimate) | 15.71 |
| Gross margin (%) | 32.05 |
| Operating margin (%) | 16.42 |
| Return on equity (%) | 26.02 |
| Free cash flow yield (%) | 7.24 |
| MA50 | 214.7300 |
| Close vs MA50 (%) | 16.4020 |
| MA200 | 187.4609 |
| Close vs MA200 (%) | 33.3345 |
| RSI (14, Wilder) | 56.8442 |
| MACD (12,26) | 12.1459 |
| MACD signal (9) | 14.4355 |
| MACD histogram | -2.2896 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ACN': 281, 'SPY': 281}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 249.9500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.4626 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -5.7362 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 17.2593 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -4.1569 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 4.3066 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 50.0235 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 34.7406 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4833 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.5949 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.8005 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0137 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 52.0566 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.0501 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -56.5068 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3357 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.7124 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 32.0500 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.4190 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 26.0250 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.2361 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.4329 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 56.8442 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.2896 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 16.4020 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 33.3345 -> Clearly above the moving-average trend level.

## TAILWINDS

### Accenture (ACN) Stock Looks Fairly Priced After Its 25% Jump
- Summary: Accenture (ACN) Stock Looks Fairly Priced After Its 25% Jump
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPRGdRY1FwaW1HUzF5SjRMOE5ULWJFX2ZUYWQ4Qm5tWjdfY0Z5Z3IxYjNZVlo1eFEybng0MFNMbW5Xb29aRUhzN3p3VDlBS3RmRXVLVEFmb0xIc2JYYllxODNxQVFXZExnNUpmUzVjeFdBdDBLdkpWb2VOdXhyX0FsU0RlSDNBZmNyRzhRdmtwTnV3N29QMlhsdms5U256QWlsODZ6Vzk0a2xVbjIzd1RqZElVMmJqNlVNQUNCNmVGMNIBxAFBVV95cUxOY0hhTmNwVlRMWENKSm5TckJwYnpzd2RWSnpuRWxwbFJiNUlkTXp1c0dpcUt0bzdwZWZpWTlfT1ZuMjFYVGp5TExiSHFPRHBQYzUtVkExdVZrSE9sXzFQdGRJLTBuTTFDbm1ORDZfcHE1Y2c4MjRaSFV6YWxFM0RfeXo4b21CMlgzc3V4dEhmWDdPOEg5aC1WZ0ZDS3BSYnl6VlNxNTNmRk95VFJyd0NsYzJYd01Xb1V3ZjcyeDZ2MXZtbllS?oc=5>

### Accenture Stock Rallied 31.5% Since October 6. Is Cognizant Now the Better Buy?
- Summary: Accenture Stock Rallied 31.5% Since October 6. Is Cognizant Now the Better Buy?
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNa3NyVmdza0xUZGJOWElXMkdtVXA3RnVUaWFRaTQ2NlFILXJCWF9JNnZxV0FJTmY2b3JfTjJocF95ckJ2NW5WMWdSSkRkUWp2a3dadlc2VzlOUEJ5ZHZuRzhnMk0xdHBhZWF1T3V3LVRPc1QwUV8wdkR0OEhvRVJjc1hxa2xYQnBKRnRvOXBoWHZ4Zkkwbk0ya2N6LXFCQWlBZnJld3l3?oc=5>

### Why Is Accenture (NYSE:ACN) Expanding Its AI Capabilities?
- Summary: Accenture is expanding AI capabilities, indicating product development.
- Date: 2026-11-09 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNTUtPYVV4RksxMDluN1hFMFlFRlI4b0tvMnAtM05iT1RfcXB5bUJCLXZyWW8tX0w2VjVjNzBpYzhpTzR0cVJndVN6NVFMZUx1Z3NYUW9qTThqOGZOaml6cl9fMmNCODJ1SXk2bDVmTGJnSnh4M3pNSmpvcS1Ec3BWU2pGSWNxYUNjaWs4cXlnSkNwWE5aM1RuWVRKLWdZalU?oc=5>

### Accenture: Market Sentiment Is Aligning With Fundamentals
- Summary: Positive market sentiment matches fundamentals, supporting stock outlook.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOT01yM1M0N3ZyYVBxcFVKS19lY242eEFlT2RzbV94WWhoZUlxaVFqMi01Y2c2Sm5SSlA4RGVPVGw4MGZ1UEhCVHZoLVBFR2luWVY3RHJpUWZwYTdWUWdBVEQxUkd5UHlHRndYTW5NdVlHMDBnaVNscnVGYUh4YUZiemFTWW9OV0FYcEF0WXQ4TEJYcm1SbHdLV1Z3?oc=5>

### Accenture PLC (ACN) Is a Trending Stock: Facts to Know Before Betting on It
- Summary: Stock trending upward, indicating investor interest.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxOWkVVZU0wbUxiWkZ0Y0VOUUtVQ1Rra1lHMUxNZmhKYW8xMmpGX3VUQTFMc3RWTGVMcWZPN3FyQ3V3Qk9QaktRTHhVWGNlZThWTTB0eF8xWVhqSkRMS2JxSUxQRzg3dzhydUpRaF84RTdSOThYdlJlTTJtWXBSR0dIaGpyVlNGUVFR?oc=5>

## HEADWINDS

### Accenture (ACN): Record Managed Services Contracts Meet a Tougher Regulatory Backdrop
- Summary: Regulatory challenges may pressure managed services contracts.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOZGkwVktaYVIwcDlmNWI5RVhUd3ZkVkp1RTA2aXMwSDkyejBmOGlVek5hMS1fSjRyc2xVV0NMRUtmUEFDUmpoVzdmUmVVcG54ZWN2UTUtOEJRcHZpbU5QNWxxc1UtVWdXTi0xbVY1MDJpS3VWVlJvZF9KczlUTXYySG5ZMWxqdURTWXJueHNnUWN5allSUllUNzdlQ3RzcjRnWkNEbg?oc=5>

### Why Accenture (ACN) Dipped More Than Broader Market Today
- Summary: Stock fell more than market, indicating weakness.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNa09Ld2JvUTNDdHM0SnZkZEYzMlIyaWk0cXJsYzdoNE5kWDJ5TFBzelEwWmRVLTFDMENFeTFwb2owYVVta2ZOUnF1alBBZmdKbmtadXdzZDAxd0M0NjN1Rms5d3htQ2pGRXNTTzdNYTJwV1RQemNJY1BnR0pxbXA3UFd6ckg3Y1MwTTJLNGVEMlZVRmtMYml3Z09B?oc=5>

## CATALYSTS

### Accenture (ACN) Following WSIB Win Has An Undervalued Narrative To Defend
- Summary: Accenture follows a WSIB win, arguing its narrative is undervalued.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxONFFwV3EzQVJnZXMwRjFQOGF5dGRFWHBrUXJsTTZDa2ZnSzlvS3JWU0ZfNU9OZnRmbU9mZDVNZjJZNFRLeU5MdkJiNlN3MG9ERXJOS2gyZWFOUlBQUEhkejJNdm1kRGtmbkpJMVhJN1Zrb3NGakxFVUZGUHJ6enJCLXhKQ3VaeFY1dDBneGs3bmVhUWduQ3pxTzFjczR3dw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ACN** | **18.43** | **4.72** | **11.17** | **6.20** | **147,654,836,224.00 USD** | **4.31** |
| IBM | 20.88 | 6.51 | 17.31 | 4.70 | 231,242,711,040.00 USD | -20.19 |
| CTSH | 11.76 | 1.94 | 7.08 | 4.60 | 28,498,190,336.00 USD | -12.14 |
| INFY | 15.17 | 9.64 | 19.71 | 1.40 | 49,779,126,272.00 USD | -26.53 |

Peers fetched as_of: 2026-11-12; ACN reuses existing data (market data as_of: 2026-11-12); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-01
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-12

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
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNTUtPYVV4RksxMDluN1hFMFlFRlI4b0tvMnAtM05iT1RfcXB5bUJCLXZyWW8tX0w2VjVjNzBpYzhpTzR0cVJndVN6NVFMZUx1Z3NYUW9qTThqOGZOaml6cl9fMmNCODJ1SXk2bDVmTGJnSnh4M3pNSmpvcS1Ec3BWU2pGSWNxYUNjaWs4cXlnSkNwWE5aM1RuWVRKLWdZalU?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOT01yM1M0N3ZyYVBxcFVKS19lY242eEFlT2RzbV94WWhoZUlxaVFqMi01Y2c2Sm5SSlA4RGVPVGw4MGZ1UEhCVHZoLVBFR2luWVY3RHJpUWZwYTdWUWdBVEQxUkd5UHlHRndYTW5NdVlHMDBnaVNscnVGYUh4YUZiemFTWW9OV0FYcEF0WXQ4TEJYcm1SbHdLV1Z3?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxOWkVVZU0wbUxiWkZ0Y0VOUUtVQ1Rra1lHMUxNZmhKYW8xMmpGX3VUQTFMc3RWTGVMcWZPN3FyQ3V3Qk9QaktRTHhVWGNlZThWTTB0eF8xWVhqSkRMS2JxSUxQRzg3dzhydUpRaF84RTdSOThYdlJlTTJtWXBSR0dIaGpyVlNGUVFR?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOZGkwVktaYVIwcDlmNWI5RVhUd3ZkVkp1RTA2aXMwSDkyejBmOGlVek5hMS1fSjRyc2xVV0NMRUtmUEFDUmpoVzdmUmVVcG54ZWN2UTUtOEJRcHZpbU5QNWxxc1UtVWdXTi0xbVY1MDJpS3VWVlJvZF9KczlUTXYySG5ZMWxqdURTWXJueHNnUWN5allSUllUNzdlQ3RzcjRnWkNEbg?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNa09Ld2JvUTNDdHM0SnZkZEYzMlIyaWk0cXJsYzdoNE5kWDJ5TFBzelEwWmRVLTFDMENFeTFwb2owYVVta2ZOUnF1alBBZmdKbmtadXdzZDAxd0M0NjN1Rms5d3htQ2pGRXNTTzdNYTJwV1RQemNJY1BnR0pxbXA3UFd6ckg3Y1MwTTJLNGVEMlZVRmtMYml3Z09B?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxONFFwV3EzQVJnZXMwRjFQOGF5dGRFWHBrUXJsTTZDa2ZnSzlvS3JWU0ZfNU9OZnRmbU9mZDVNZjJZNFRLeU5MdkJiNlN3MG9ERXJOS2gyZWFOUlBQUEhkejJNdm1kRGtmbkpJMVhJN1Zrb3NGakxFVUZGUHJ6enJCLXhKQ3VaeFY1dDBneGs3bmVhUWduQ3pxTzFjczR3dw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
