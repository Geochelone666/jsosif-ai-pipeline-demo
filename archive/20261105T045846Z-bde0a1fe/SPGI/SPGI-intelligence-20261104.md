# SPGI Intelligence Report

- ticker: **SPGI**
- Report as_of: **2026-11-04**
- Market data as_of: **2026-11-04**
- Quant sources: https://finance.yahoo.com/quote/SPGI/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SPGI/key-statistics/
- AI analysis snapshot as_of: **2026-11-04**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-05T05:20:53.189196+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 14, 'rule': 2, 'ai': 7, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261104T044411Z-6b13f9ec/SPGI** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 14 unique headlines; 7 named publishers; 1 exact duplicates; 14 HTTPS source links; largest publisher share 35.71%; oldest publication 2026-10-28

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 481.6900 |
| Return 1D (%) | 3.3603 |
| Return 1W (%) | 7.2018 |
| Return 1M (%) | 24.7029 |
| Return YTD (%) | -1.8990 |
| Return 1Y (%) | 2.8974 |
| Annualized volatility (%) | 30.9303 |
| Beta vs SPY | 0.3452 |
| Max drawdown (%) | -28.4781 |
| Sharpe (rf=0) | 0.2489 |
| Downside deviation (rf=0, %) | 23.0254 |
| Sortino (rf=0) | 0.3343 |
| Historical VaR 95% (1D, %) | 2.8749 |
| Historical ES 95% (1D, %) | 4.6345 |
| Correlation vs SPY | 0.1433 |
| Tracking error vs SPY (%) | 31.7447 |
| P/E (trailing) | 27.84 |
| P/B | 7.08 |
| EV/EBITDA | 18.59 |
| Revenue growth (%) | 6.80 |
| Forward P/E (estimate) | 23.87 |
| Gross margin (%) | 70.99 |
| Operating margin (%) | 48.21 |
| Return on equity (%) | 17.88 |
| Free cash flow yield (%) | 4.32 |
| MA50 | 423.9882 |
| Close vs MA50 (%) | 13.6093 |
| MA200 | 415.2918 |
| Close vs MA200 (%) | 15.9883 |
| RSI (14, Wilder) | 75.7988 |
| MACD (12,26) | 16.3509 |
| MACD signal (9) | 12.3877 |
| MACD histogram | 3.9632 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SPGI': 275, 'SPY': 275}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 481.6900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 3.3603 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 7.2018 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 24.7029 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -1.8990 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 2.8974 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.9303 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 23.0254 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3343 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8749 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6345 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1433 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.7447 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3452 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.4781 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2489 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.8660 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 70.9940 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 48.2060 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.8760 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.3245 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.8434 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 75.7988 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 3.9632 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 13.6093 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 15.9883 -> Clearly above the moving-average trend level.

## TAILWINDS

### S&P Global Inc (SPGI) Stock Up 3.4% and Still Undervalued -- GF Score: 94/100
- Summary: S&P Global Inc (SPGI) Stock Up 3.4% and Still Undervalued -- GF Score: 94/100
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxNY0NSSEM0anBJYWg2TkduT0Q0TmE0cFJlZ0dudUpYNVZaOFdRY1VJd1lWeS1COFROVWdVeE4tMzNwTTdLcUthWFJZVEFjS3JtWXNWUEtmOUFldlhic0dfTW1ZYW5QaWdCWG5ZSGlaX2lNNklCSFdBSm14aXVTNEIzSWtVRDRXLXdGMVhISU1VVzBxX3g2bGZTR2UtcmExaS1VVS13S3pNWGpvQQ?oc=5>

### S&P Global Inc. (SPGI) Remains a Key Player in Financial Markets: Is Its Competitive Edge Underestimated?
- Summary: Highlights SPGI’s strong market position and potential undervaluation.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQd3dFNUo5YTJMdzdlV0pENWgtYTdxNElxU00xdUxfMGZ0WTBMdjJlekR0TEd1VEZXQ1ZFbXJURmlsRGFzS0dsNm1oVzFLM2Z0clpjYmdoRFh6YWVrQjhMNHh3ODdoTHc5ZFBvcHNON254RUtjbHZMTTdFampXU0x5Zm8zVWpyMkZ0ME5yTlZiT0FKc2Va?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### S&P Global Earnings Call: Growth, AI And Buybacks
- Summary: S&P Global Earnings Call: Growth, AI And Buybacks
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOS2lCVWpEQnh6NktkaFNHQU9NMDhteDYzVF9FMVBDS2pXOEhXU2g2VGdxZHc3R0xZeXlsbzI5S3o5Zk5JVlRPSXNWY0pJalhGUmtaOHp2VjZYMUxTV3ozMk5XNDh5cWRYYUtOYUVTREQ2YWZma29WazhDaWM1di0wRHJXSEFoc3QwcmVVLWtJV0RCWXBSNmxjalhyc2pSYUU?oc=5>

### S&P Global (SPGI) Stock Faces Q3 Earnings Puzzle After Guidance Lift
- Summary: SPGI’s guidance lift creates earnings uncertainty, raising questions about future profitability.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNQ3d6ZEw2NXY4Y0JEQy1QazBTYjNuRjlTYWtBNFFodTJ6bjNXalRCdlZ0VkZfVTNuNmtzTndiOFd1U202Ul9zWW5KM3lBdG9wWXNmWEEwbVpGTURvMG1OeU4wRjZ4aG80WTM1SE9kbkxXWEZYVm5iT0Jrdms0QTRXTi1lcDd0ZUFHcFgtclg0MF9SSDZy?oc=5>

### S&P Global Inc. (SPGI) Stock Forecasts
- Summary: Forecasts for S&P Global's stock performance based on earnings projections.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxNdVdISHpmUjBoYUhidWVHakF1ZDV5ZXhrM241eU4zTEFEbE9GR0xQRlFueUd5TjJEb0FEdjJVOUlNLU5TMTdrOGlrd0NKbkFGZXVMeU5vUENzcXlNMlhkdlRBR094RS1NcmczOXNqTnF5MHJaVE93VGwwT3BBOGdlUDBTNWJERFRfbVh1VQ?oc=5>

### S&P Global (SPGI) Could Be 23% Above Fair Value After Q3 Beat
- Summary: SPGI’s valuation may be 23% above fair value following a Q3 earnings beat, indicating potential upside.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxON1ljWFZSZmFkOW00UjVnNnp5b3pxNXR4VHVmTXpkaDdIQ0VwSmtuY0JqRXBfMVRoWTN0TksxT0pHcHRpak5MVDRJVmRoN3FCeElXS2diNjlkNmpESk5MT2w4N0RKZWpJWHQteV9XSFRWcDR1M0RCUFdKa1pCekg3Z3RfN0c4SkF4MFBEQllGZjl2amt4Y2I5WUN3a3FhSXcxd0xQLUloTEJzbzRXTU13RDZXbzhHcElfeUMwSGxnTmRoSnA2SVN4a1M0V3NJdDh6a2o00gHYAUFVX3lxTE5TaHkxTTk4SzBtdXFaRDZpTVNqMEJEZ0ZhLUpMZU45NHZKV05DMGJUYnV0REdISDE3Uk5NX3Iza3lpZVMxajg0QVVYUDZrbXdaZXhxXzBRYVJSSEFRUGlBdnE4cmZYNmstSE1KaldlYmtpR3phczlVYlhMdEl3NDdyQ2h6Wm5sbUtCRWRLeWE1QUxlWHAyenZWSTVoY0JPdThJR3FnM1JZV01oWEtlUGNNU3IwZmVLLThtS25HbVJab0lNYmMxZmtVWmlpS0tyRGJJN3RyM0ZvUw?oc=5>

### Could S&P Global (SPGI) Recast Its Business With A Capital IQ Review?
- Summary: S&P Global may reshape its business model through a Capital IQ review, potentially enhancing product offerings and market positioning.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxQcFhFSHRRamVwRW1GMmpSNXQ0dnVfX0ZKT0FHblBzSlhqMW85bUhTZ05YT0xLNDZCYi14Tl9lU2FVWFNsUFdTaWloTnhlaG1STlBKcHZseUVSakhrTndkcXptUUFGNVQ3dUtRUWc1Z1FPNWxqZDM2WVFtWVdkbHk5d1Z2SWdlRExRbjNHMDlGRkJyeVpLc1RSTHZCbFM5dlF6T1NSOTJNQ1FVek1RdENsRkY0SUtxVEU1UDNqNlkyQV9JUnNMODZULW9rVVF6U3lwcUQ3SXJXZ9IB3AFBVV95cUxPcUdhYVVJR0xSSnhvVDRTcmMteEdtRktJZGR6emlZQk5lalBYVGF5MzdDNFA2dWFzb2pLLVMzcExyQVpOQVFkM0oySTYxMlRGMXBSSXRyRzRPZGd5LVVsM0o0cHRseURITE94Qm01MzQ0Qmd5N09tbnBSX0VBd0ZBOU5ZZ1BINEVRcDZuR0Y1YW1fMDcwbUp4VGQ2OXZrMXc4Tlh0bGxVVzJLYmtiV0tPRzBLLTV0b1JwYmJCc0h0NzNkSDRnR0dkeDJVV29oYmVfMlNhb08tNG42Uk9l?oc=5>

### 5 must-read analyst questions from S&P Global’s Q3 earnings call
- Summary: Focuses on key analyst inquiries during SPGI’s Q3 earnings call.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNRkhSalE2SlJmTWZQZ3ZTLXVvY2ppdEhtbFRhS2ZaWXhvV1ljMU85MmVtY2ZKTzd2ZGIwS2xBZDJ4amtwVldoTmN4alhFeTE2c1FTd3NJZmJTVnZ0QmF2aUpBN3dzTlBrOVRoTm9Sc3E3TTByWEhRczFHTDdqVlBBSDF2STMtbmhDUTdPZUJWeDRJQkxXNHp1UTlB?oc=5>

### SPGI Q3 deep dive: strategic review and AI drive business evolution
- Summary: Analyzes SPGI’s Q3 results, strategic review, and AI initiatives.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNdnhRYzhvMTJyQzE0a0NXVUN6aFlqczc4VzhSQzd0YVRiRlB6YmZMQWFIaDlSclB3T0FHSmlYTEhxRjctTTVGWldpQTdKTlV0NHk4Z01KajU4THVGSEVRZmE5SlhwMjhMLTdtWUNteW9uVHlKYVhrYlVVN1RndzRjTzVBcXZZMjBvdzNaZDk5SUFXX0k2Wm5n?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SPGI** | **27.84** | **7.08** | **18.59** | **6.80** | **139,641,929,728.00 USD** | **2.90** |
| MCO | 30.74 | 27.88 | 24.02 | 0.80 | 91,098,546,176.00 USD | 9.33 |
| MSCI | 33.83 | -16.03 | 27.17 | 12.40 | 49,021,607,936.00 USD | 18.97 |
| FDS | 22.83 | 6.03 | 14.82 | 6.30 | 12,068,997,120.00 USD | 31.65 |

Peers fetched as_of: 2026-11-04; SPGI reuses existing data (market data as_of: 2026-11-04); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

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
- Filing date: 2026-10-28
- Revenue (latest available single quarter): 1,567,000,000.00 USD; period 2018-01-01/2018-03-31; fiscal year/reporting period 2018/Q1
- Net income (latest available single quarter): 1,240,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/64040/000006404026000058/spgi-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNY0NSSEM0anBJYWg2TkduT0Q0TmE0cFJlZ0dudUpYNVZaOFdRY1VJd1lWeS1COFROVWdVeE4tMzNwTTdLcUthWFJZVEFjS3JtWXNWUEtmOUFldlhic0dfTW1ZYW5QaWdCWG5ZSGlaX2lNNklCSFdBSm14aXVTNEIzSWtVRDRXLXdGMVhISU1VVzBxX3g2bGZTR2UtcmExaS1VVS13S3pNWGpvQQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQd3dFNUo5YTJMdzdlV0pENWgtYTdxNElxU00xdUxfMGZ0WTBMdjJlekR0TEd1VEZXQ1ZFbXJURmlsRGFzS0dsNm1oVzFLM2Z0clpjYmdoRFh6YWVrQjhMNHh3ODdoTHc5ZFBvcHNON254RUtjbHZMTTdFampXU0x5Zm8zVWpyMkZ0ME5yTlZiT0FKc2Va?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOS2lCVWpEQnh6NktkaFNHQU9NMDhteDYzVF9FMVBDS2pXOEhXU2g2VGdxZHc3R0xZeXlsbzI5S3o5Zk5JVlRPSXNWY0pJalhGUmtaOHp2VjZYMUxTV3ozMk5XNDh5cWRYYUtOYUVTREQ2YWZma29WazhDaWM1di0wRHJXSEFoc3QwcmVVLWtJV0RCWXBSNmxjalhyc2pSYUU?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNQ3d6ZEw2NXY4Y0JEQy1QazBTYjNuRjlTYWtBNFFodTJ6bjNXalRCdlZ0VkZfVTNuNmtzTndiOFd1U202Ul9zWW5KM3lBdG9wWXNmWEEwbVpGTURvMG1OeU4wRjZ4aG80WTM1SE9kbkxXWEZYVm5iT0Jrdms0QTRXTi1lcDd0ZUFHcFgtclg0MF9SSDZy?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNdVdISHpmUjBoYUhidWVHakF1ZDV5ZXhrM241eU4zTEFEbE9GR0xQRlFueUd5TjJEb0FEdjJVOUlNLU5TMTdrOGlrd0NKbkFGZXVMeU5vUENzcXlNMlhkdlRBR094RS1NcmczOXNqTnF5MHJaVE93VGwwT3BBOGdlUDBTNWJERFRfbVh1VQ?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxON1ljWFZSZmFkOW00UjVnNnp5b3pxNXR4VHVmTXpkaDdIQ0VwSmtuY0JqRXBfMVRoWTN0TksxT0pHcHRpak5MVDRJVmRoN3FCeElXS2diNjlkNmpESk5MT2w4N0RKZWpJWHQteV9XSFRWcDR1M0RCUFdKa1pCekg3Z3RfN0c4SkF4MFBEQllGZjl2amt4Y2I5WUN3a3FhSXcxd0xQLUloTEJzbzRXTU13RDZXbzhHcElfeUMwSGxnTmRoSnA2SVN4a1M0V3NJdDh6a2o00gHYAUFVX3lxTE5TaHkxTTk4SzBtdXFaRDZpTVNqMEJEZ0ZhLUpMZU45NHZKV05DMGJUYnV0REdISDE3Uk5NX3Iza3lpZVMxajg0QVVYUDZrbXdaZXhxXzBRYVJSSEFRUGlBdnE4cmZYNmstSE1KaldlYmtpR3phczlVYlhMdEl3NDdyQ2h6Wm5sbUtCRWRLeWE1QUxlWHAyenZWSTVoY0JPdThJR3FnM1JZV01oWEtlUGNNU3IwZmVLLThtS25HbVJab0lNYmMxZmtVWmlpS0tyRGJJN3RyM0ZvUw?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxQcFhFSHRRamVwRW1GMmpSNXQ0dnVfX0ZKT0FHblBzSlhqMW85bUhTZ05YT0xLNDZCYi14Tl9lU2FVWFNsUFdTaWloTnhlaG1STlBKcHZseUVSakhrTndkcXptUUFGNVQ3dUtRUWc1Z1FPNWxqZDM2WVFtWVdkbHk5d1Z2SWdlRExRbjNHMDlGRkJyeVpLc1RSTHZCbFM5dlF6T1NSOTJNQ1FVek1RdENsRkY0SUtxVEU1UDNqNlkyQV9JUnNMODZULW9rVVF6U3lwcUQ3SXJXZ9IB3AFBVV95cUxPcUdhYVVJR0xSSnhvVDRTcmMteEdtRktJZGR6emlZQk5lalBYVGF5MzdDNFA2dWFzb2pLLVMzcExyQVpOQVFkM0oySTYxMlRGMXBSSXRyRzRPZGd5LVVsM0o0cHRseURITE94Qm01MzQ0Qmd5N09tbnBSX0VBd0ZBOU5ZZ1BINEVRcDZuR0Y1YW1fMDcwbUp4VGQ2OXZrMXc4Tlh0bGxVVzJLYmtiV0tPRzBLLTV0b1JwYmJCc0h0NzNkSDRnR0dkeDJVV29oYmVfMlNhb08tNG42Uk9l?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNRkhSalE2SlJmTWZQZ3ZTLXVvY2ppdEhtbFRhS2ZaWXhvV1ljMU85MmVtY2ZKTzd2ZGIwS2xBZDJ4amtwVldoTmN4alhFeTE2c1FTd3NJZmJTVnZ0QmF2aUpBN3dzTlBrOVRoTm9Sc3E3TTByWEhRczFHTDdqVlBBSDF2STMtbmhDUTdPZUJWeDRJQkxXNHp1UTlB?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNdnhRYzhvMTJyQzE0a0NXVUN6aFlqczc4VzhSQzd0YVRiRlB6YmZMQWFIaDlSclB3T0FHSmlYTEhxRjctTTVGWldpQTdKTlV0NHk4Z01KajU4THVGSEVRZmE5SlhwMjhMLTdtWUNteW9uVHlKYVhrYlVVN1RndzRjTzVBcXZZMjBvdzNaZDk5SUFXX0k2Wm5n?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxPd0ZPWnZKS0RlWkNLXzN4Ym1WVVZURHNScUJxVXdZaWRjU0RfUzZWMEtVOWxxaXVWRXY3ZEJkMGxjZ016amZSeGZLQXVOSWJYMWl2SG9XUjdyX1k2QVY1eUFDQVo3cXpTWjdidjl3RktOZkJjMVVpVVRHeVRiaFk4SkZJQ0JCNVZ1OU9kRjc1S1BReXp6aGtuaHJmQzQxTmhtRk5KTlJvd2pxaFZDVWlXcVVhM1ZBWHJqZHpxX2ZTYjlVWnNMb25j?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
