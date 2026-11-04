# SPGI Intelligence Report

- ticker: **SPGI**
- Report as_of: **2026-11-03**
- Market data as_of: **2026-11-03**
- Quant sources: https://finance.yahoo.com/quote/SPGI/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SPGI/key-statistics/
- AI analysis snapshot as_of: **2026-11-03**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-04T04:45:48.094917+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 20, 'rule': 3, 'ai': 11, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261103T051441Z-8b1c85d8/SPGI** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 20 unique headlines; 11 named publishers; 2 exact duplicates; 20 HTTPS source links; largest publisher share 30.0%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 466.0300 |
| Return 1D (%) | -1.9235 |
| Return 1W (%) | 3.8091 |
| Return 1M (%) | 20.6488 |
| Return YTD (%) | -5.0883 |
| Return 1Y (%) | -0.0092 |
| Annualized volatility (%) | 30.7513 |
| Beta vs SPY | 0.3114 |
| Max drawdown (%) | -28.4781 |
| Sharpe (rf=0) | 0.1550 |
| Downside deviation (rf=0, %) | 23.0254 |
| Sortino (rf=0) | 0.2070 |
| Historical VaR 95% (1D, %) | 2.8749 |
| Historical ES 95% (1D, %) | 4.6345 |
| Correlation vs SPY | 0.1296 |
| Tracking error vs SPY (%) | 31.7403 |
| P/E (trailing) | 28.38 |
| P/B | 6.85 |
| EV/EBITDA | 18.05 |
| Revenue growth (%) | 6.80 |
| Forward P/E (estimate) | 23.09 |
| Gross margin (%) | 70.99 |
| Operating margin (%) | 48.21 |
| Return on equity (%) | 17.88 |
| Free cash flow yield (%) | 4.47 |
| MA50 | 422.9948 |
| Close vs MA50 (%) | 10.1739 |
| MA200 | 415.3217 |
| Close vs MA200 (%) | 12.2094 |
| RSI (14, Wilder) | 70.5470 |
| MACD (12,26) | 15.1141 |
| MACD signal (9) | 11.3969 |
| MACD histogram | 3.7173 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SPGI': 274, 'SPY': 274}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 466.0300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.9235 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.8091 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 20.6488 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -5.0883 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -0.0092 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.7513 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 23.0254 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2070 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8749 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6345 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1296 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.7403 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3114 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.4781 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1550 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.0901 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 70.9940 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 48.2060 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.8760 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.4699 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 28.3819 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 70.5470 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 3.7173 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 10.1739 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 12.2094 -> Clearly above the moving-average trend level.

## TAILWINDS

### SPGI Stock Outlook Improves as S&P Global Raises 2026 Guidance
- Summary: SPGI Stock Outlook Improves as S&P Global Raises 2026 Guidance
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxONEZJNlgxVUhTazVVR3NHVTNfV0tKelhFSDlpNHluZGtpWmthMUtSNVBpVDIzMTBnNjF3Rm50ZzJidGlpQlZqcXRXOHBjQzZsUWZmNTNpVV9URFpiek1IaldPeGJBckJlU0Z5dG9JS1JUTnBSUnNFNkNNdzB0SjRKT2RnYkdjWF9fdG0weWtlV1poZ182Y0lZTWRKdXZKN1JIYy1z0gGoAUFVX3lxTE91UlpfZFIzNERRaWNtTGpOVnVMNWNfb3BHQVBwRGZpYzNlYkFBSjV1VUVaTlE5MGlDU1VTMkdEc0ZzTGZtaTVHTl9pOEF1anpDQUhHVkNmZWxTbG85YUsyQkxGUjhPTlZpMzRHc21XUzNiMTNZaS15VGZmdjBoelMxNzQ5UFJISk4xUXpMLW1OX25yOGxmS2lhWk9BSFBvSUozUTZpaXhTdg?oc=5>

### S&P Global (SPGI) Stock Looks Fully Priced Despite Strong Excess Returns
- Summary: Stock appears fully priced, indicating market confidence.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNZkJOcnNoTVNDRElhOU9KUkcxOTYtbVFYY0JDTXNXbGpIaW9kRmt3SVo0OS1kdHpCdUNydGdUMUpQYTlMaFZpUkZVTE11WW96c2Z1UVZGOGgwT1FxTldCUmxFQW44UE93czlNTnY3dmhMSkprVlEyR3RCdDBwWk96QnBuVFBuaE91QXljODVDUWdhcEdW?oc=5>

### SPGI Q3 Earnings Call Highlights Strategic Review and Growth Outlook
- Summary: SPGI’s Q3 earnings call detailed strategic review and growth outlook, indicating positive future prospects.
- Date: 2026-10-28 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxOZGtyS2w3OXRhZDR6dEdYTVkweGNVTUxnYkp3WUEyQ1NBYkEzRklBamNySllsM2pnS0FCZ3B3cWRjaG9YbEhwaFdLS1hnTF9waFVwbUtnS1VoN2ZIMGxHM09ENU1WN3FmamhfYks0eVpJYjVGT25DcUttY1IzRURLalRSTFltelNHOWdPVHF4TGxKOUVVZmdWZDBPY1FSMHczRXozM3hXM1FKY1BKbkF2QU9DUXE2bkxhUmxHS2FOdndUUQ?oc=5>

### S&P Global (NYSE:SPGI) exceeds Q3 2026 expectations
- Summary: SPGI surpassed Q3 2026 earnings expectations, signaling strong performance.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPMFg2OHJzM1N0cHVZclQ3R09acFJrMF9jeFdpeXAtMTFPRFA0d2FGbkJCdXdiQjNld2FoRElXSDdXZ2FoUVZMSlJaQmNveDBBYzVfMUxBaTdvaWdtbzdYNHo1d09GTzJHUTljOTE3WDBfV2EyQmFnTjRCRFhkUGZzbFdQZFdpaG40RHZNeGRXT3IwMEtuaVkwbktuWFR1NW5yTUx0aHplX1dIRmM?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### S&P Global confirms strategic review of Capital IQ, data businesses; Q3 earnings beat (SPGI:NYSE)
- Summary: S&P Global confirms strategic review of Capital IQ, data businesses; Q3 earnings beat (SPGI:NYSE)
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxNZ2NVLUdkWW8yY0g0VmQzNlY5T0NDVjdGa2pqRnBWNllLUDBFVVNRUGxpd3c0X09ncThWVUF0Wk9ORUgyUTJzUjNHdnRCb0dvVE94VzJjd2NYYzBWX3kxWlRneVZoRUt2aUo0RkVoX2duNWlZdkRKd2tUOFVERU1EUHdWVnBPcDBraHB5aGRkRTd5TlRKTUYtdGVfWnRNZDdhcExPYk1VVHBiYmE4dHVZZWpNZGdaUWlPb2RtUA?oc=5>

### S&P Global Earnings Call: Growth, AI And Buybacks
- Summary: S&P Global Earnings Call: Growth, AI And Buybacks
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOS2lCVWpEQnh6NktkaFNHQU9NMDhteDYzVF9FMVBDS2pXOEhXU2g2VGdxZHc3R0xZeXlsbzI5S3o5Zk5JVlRPSXNWY0pJalhGUmtaOHp2VjZYMUxTV3ozMk5XNDh5cWRYYUtOYUVTREQ2YWZma29WazhDaWM1di0wRHJXSEFoc3QwcmVVLWtJV0RCWXBSNmxjalhyc2pSYUU?oc=5>

### S&P Global (SPGI) Stock Faces Q3 Earnings Puzzle After Guidance Lift
- Summary: SPGI’s guidance lift creates earnings uncertainty, raising questions about future profitability.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNQ3d6ZEw2NXY4Y0JEQy1QazBTYjNuRjlTYWtBNFFodTJ6bjNXalRCdlZ0VkZfVTNuNmtzTndiOFd1U202Ul9zWW5KM3lBdG9wWXNmWEEwbVpGTURvMG1OeU4wRjZ4aG80WTM1SE9kbkxXWEZYVm5iT0Jrdms0QTRXTi1lcDd0ZUFHcFgtclg0MF9SSDZy?oc=5>

### SPGI Q3 deep dive: strategic review and AI drive business evolution
- Summary: SPGI's Q3 review highlights strategic initiatives and AI integration driving business evolution.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNdnhRYzhvMTJyQzE0a0NXVUN6aFlqczc4VzhSQzd0YVRiRlB6YmZMQWFIaDlSclB3T0FHSmlYTEhxRjctTTVGWldpQTdKTlV0NHk4Z01KajU4THVGSEVRZmE5SlhwMjhMLTdtWUNteW9uVHlKYVhrYlVVN1RndzRjTzVBcXZZMjBvdzNaZDk5SUFXX0k2Wm5n?oc=5>

### S&P Global Inc. (SPGI) Stock Forecasts
- Summary: Forecasts for S&P Global's stock performance based on earnings projections.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxNdVdISHpmUjBoYUhidWVHakF1ZDV5ZXhrM241eU4zTEFEbE9GR0xQRlFueUd5TjJEb0FEdjJVOUlNLU5TMTdrOGlrd0NKbkFGZXVMeU5vUENzcXlNMlhkdlRBR094RS1NcmczOXNqTnF5MHJaVE93VGwwT3BBOGdlUDBTNWJERFRfbVh1VQ?oc=5>

### S&P Global Reports Third Quarter Results; Announces Strategic Review for Capital IQ and Associated Data Businesses
- Summary: SPGI releases Q3 results and announces strategic review of Capital IQ and Associated Data.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPS1RxWGVmczhnMUdrRkJwMjM0dmMyZ3ZMZUhrSEtoekk2TEpuajhxSU52eU85TXJqQ2lTdmZlb1lFVVZPYjJsWWVab1RRWUduZDdaZFFQVkNWcDJpRDNNajNZbENnQmFtcmVnSG1zcjQ5TzBzZ0FzelpfUUhPZXdVaUxnd1ZfU3hRYi1qcWhSakZjanNPOTR5WUFVSQ?oc=5>

### S&P Global starts review for Capital IQ and related data business
- Summary: Internal review of Capital IQ and related data business.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNUTlPSHg5RWh2UEZuY2lDSmF1Z0Z3UkVscm42OHFKRjRlZ21MemFjNVF1ZmNwaVVHVDgwTW9hd29kRHhLMGpKQU9sV0xubG5JdGs5SEdqTkJiWkJwN1QwWmlCZnFNTHJtc2dNNjVyN2k5LTVrX0c1NDdpUlVxZXNJQ1VzREt1SUsxTGd5MVhfV3o2TWlHbkFQVVBQT0NQcVQ4UEI5Y0pyaThEYTZDOWU4SUxkU2w1Wjl2R1l2aTdBTExNLWN5azhz?oc=5>

### 5 must-read analyst questions from S&P Global’s Q3 earnings call
- Summary: Analysts pose key questions to SPGI during its Q3 earnings call, focusing on performance and outlook.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNRkhSalE2SlJmTWZQZ3ZTLXVvY2ppdEhtbFRhS2ZaWXhvV1ljMU85MmVtY2ZKTzd2ZGIwS2xBZDJ4amtwVldoTmN4alhFeTE2c1FTd3NJZmJTVnZ0QmF2aUpBN3dzTlBrOVRoTm9Sc3E3TTByWEhRczFHTDdqVlBBSDF2STMtbmhDUTdPZUJWeDRJQkxXNHp1UTlB?oc=5>

### S&P Global (SPGI) Could Be 23% Above Fair Value After Q3 Beat
- Summary: SPGI’s valuation may be 23% above fair value following a Q3 earnings beat, indicating potential upside.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxON1ljWFZSZmFkOW00UjVnNnp5b3pxNXR4VHVmTXpkaDdIQ0VwSmtuY0JqRXBfMVRoWTN0TksxT0pHcHRpak5MVDRJVmRoN3FCeElXS2diNjlkNmpESk5MT2w4N0RKZWpJWHQteV9XSFRWcDR1M0RCUFdKa1pCekg3Z3RfN0c4SkF4MFBEQllGZjl2amt4Y2I5WUN3a3FhSXcxd0xQLUloTEJzbzRXTU13RDZXbzhHcElfeUMwSGxnTmRoSnA2SVN4a1M0V3NJdDh6a2o00gHYAUFVX3lxTE5TaHkxTTk4SzBtdXFaRDZpTVNqMEJEZ0ZhLUpMZU45NHZKV05DMGJUYnV0REdISDE3Uk5NX3Iza3lpZVMxajg0QVVYUDZrbXdaZXhxXzBRYVJSSEFRUGlBdnE4cmZYNmstSE1KaldlYmtpR3phczlVYlhMdEl3NDdyQ2h6Wm5sbUtCRWRLeWE1QUxlWHAyenZWSTVoY0JPdThJR3FnM1JZV01oWEtlUGNNU3IwZmVLLThtS25HbVJab0lNYmMxZmtVWmlpS0tyRGJJN3RyM0ZvUw?oc=5>

### Could S&P Global (SPGI) Recast Its Business With A Capital IQ Review?
- Summary: S&P Global may reshape its business model through a Capital IQ review, potentially enhancing product offerings and market positioning.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxQcFhFSHRRamVwRW1GMmpSNXQ0dnVfX0ZKT0FHblBzSlhqMW85bUhTZ05YT0xLNDZCYi14Tl9lU2FVWFNsUFdTaWloTnhlaG1STlBKcHZseUVSakhrTndkcXptUUFGNVQ3dUtRUWc1Z1FPNWxqZDM2WVFtWVdkbHk5d1Z2SWdlRExRbjNHMDlGRkJyeVpLc1RSTHZCbFM5dlF6T1NSOTJNQ1FVek1RdENsRkY0SUtxVEU1UDNqNlkyQV9JUnNMODZULW9rVVF6U3lwcUQ3SXJXZ9IB3AFBVV95cUxPcUdhYVVJR0xSSnhvVDRTcmMteEdtRktJZGR6emlZQk5lalBYVGF5MzdDNFA2dWFzb2pLLVMzcExyQVpOQVFkM0oySTYxMlRGMXBSSXRyRzRPZGd5LVVsM0o0cHRseURITE94Qm01MzQ0Qmd5N09tbnBSX0VBd0ZBOU5ZZ1BINEVRcDZuR0Y1YW1fMDcwbUp4VGQ2OXZrMXc4Tlh0bGxVVzJLYmtiV0tPRzBLLTV0b1JwYmJCc0h0NzNkSDRnR0dkeDJVV29oYmVfMlNhb08tNG42Uk9l?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SPGI** | **28.38** | **6.85** | **18.05** | **6.80** | **135,102,095,360.00 USD** | **-0.01** |
| MCO | 30.88 | 26.58 | 22.97 | 0.80 | 86,848,282,624.00 USD | 4.55 |
| MSCI | 33.69 | -15.21 | 25.95 | 12.40 | 46,512,009,216.00 USD | 11.68 |
| FDS | 23.59 | 5.86 | 14.44 | 6.30 | 11,730,406,400.00 USD | 27.96 |

Peers fetched as_of: 2026-11-03; SPGI reuses existing data (market data as_of: 2026-11-03); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-03

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

- https://news.google.com/rss/articles/CBMiowFBVV95cUxONEZJNlgxVUhTazVVR3NHVTNfV0tKelhFSDlpNHluZGtpWmthMUtSNVBpVDIzMTBnNjF3Rm50ZzJidGlpQlZqcXRXOHBjQzZsUWZmNTNpVV9URFpiek1IaldPeGJBckJlU0Z5dG9JS1JUTnBSUnNFNkNNdzB0SjRKT2RnYkdjWF9fdG0weWtlV1poZ182Y0lZTWRKdXZKN1JIYy1z0gGoAUFVX3lxTE91UlpfZFIzNERRaWNtTGpOVnVMNWNfb3BHQVBwRGZpYzNlYkFBSjV1VUVaTlE5MGlDU1VTMkdEc0ZzTGZtaTVHTl9pOEF1anpDQUhHVkNmZWxTbG85YUsyQkxGUjhPTlZpMzRHc21XUzNiMTNZaS15VGZmdjBoelMxNzQ5UFJISk4xUXpMLW1OX25yOGxmS2lhWk9BSFBvSUozUTZpaXhTdg?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNZkJOcnNoTVNDRElhOU9KUkcxOTYtbVFYY0JDTXNXbGpIaW9kRmt3SVo0OS1kdHpCdUNydGdUMUpQYTlMaFZpUkZVTE11WW96c2Z1UVZGOGgwT1FxTldCUmxFQW44UE93czlNTnY3dmhMSkprVlEyR3RCdDBwWk96QnBuVFBuaE91QXljODVDUWdhcEdW?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxOZGtyS2w3OXRhZDR6dEdYTVkweGNVTUxnYkp3WUEyQ1NBYkEzRklBamNySllsM2pnS0FCZ3B3cWRjaG9YbEhwaFdLS1hnTF9waFVwbUtnS1VoN2ZIMGxHM09ENU1WN3FmamhfYks0eVpJYjVGT25DcUttY1IzRURLalRSTFltelNHOWdPVHF4TGxKOUVVZmdWZDBPY1FSMHczRXozM3hXM1FKY1BKbkF2QU9DUXE2bkxhUmxHS2FOdndUUQ?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPMFg2OHJzM1N0cHVZclQ3R09acFJrMF9jeFdpeXAtMTFPRFA0d2FGbkJCdXdiQjNld2FoRElXSDdXZ2FoUVZMSlJaQmNveDBBYzVfMUxBaTdvaWdtbzdYNHo1d09GTzJHUTljOTE3WDBfV2EyQmFnTjRCRFhkUGZzbFdQZFdpaG40RHZNeGRXT3IwMEtuaVkwbktuWFR1NW5yTUx0aHplX1dIRmM?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxNZ2NVLUdkWW8yY0g0VmQzNlY5T0NDVjdGa2pqRnBWNllLUDBFVVNRUGxpd3c0X09ncThWVUF0Wk9ORUgyUTJzUjNHdnRCb0dvVE94VzJjd2NYYzBWX3kxWlRneVZoRUt2aUo0RkVoX2duNWlZdkRKd2tUOFVERU1EUHdWVnBPcDBraHB5aGRkRTd5TlRKTUYtdGVfWnRNZDdhcExPYk1VVHBiYmE4dHVZZWpNZGdaUWlPb2RtUA?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOS2lCVWpEQnh6NktkaFNHQU9NMDhteDYzVF9FMVBDS2pXOEhXU2g2VGdxZHc3R0xZeXlsbzI5S3o5Zk5JVlRPSXNWY0pJalhGUmtaOHp2VjZYMUxTV3ozMk5XNDh5cWRYYUtOYUVTREQ2YWZma29WazhDaWM1di0wRHJXSEFoc3QwcmVVLWtJV0RCWXBSNmxjalhyc2pSYUU?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNQ3d6ZEw2NXY4Y0JEQy1QazBTYjNuRjlTYWtBNFFodTJ6bjNXalRCdlZ0VkZfVTNuNmtzTndiOFd1U202Ul9zWW5KM3lBdG9wWXNmWEEwbVpGTURvMG1OeU4wRjZ4aG80WTM1SE9kbkxXWEZYVm5iT0Jrdms0QTRXTi1lcDd0ZUFHcFgtclg0MF9SSDZy?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNdnhRYzhvMTJyQzE0a0NXVUN6aFlqczc4VzhSQzd0YVRiRlB6YmZMQWFIaDlSclB3T0FHSmlYTEhxRjctTTVGWldpQTdKTlV0NHk4Z01KajU4THVGSEVRZmE5SlhwMjhMLTdtWUNteW9uVHlKYVhrYlVVN1RndzRjTzVBcXZZMjBvdzNaZDk5SUFXX0k2Wm5n?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxPd0ZPWnZKS0RlWkNLXzN4Ym1WVVZURHNScUJxVXdZaWRjU0RfUzZWMEtVOWxxaXVWRXY3ZEJkMGxjZ016amZSeGZLQXVOSWJYMWl2SG9XUjdyX1k2QVY1eUFDQVo3cXpTWjdidjl3RktOZkJjMVVpVVRHeVRiaFk4SkZJQ0JCNVZ1OU9kRjc1S1BReXp6aGtuaHJmQzQxTmhtRk5KTlJvd2pxaFZDVWlXcVVhM1ZBWHJqZHpxX2ZTYjlVWnNMb25j?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNdVdISHpmUjBoYUhidWVHakF1ZDV5ZXhrM241eU4zTEFEbE9GR0xQRlFueUd5TjJEb0FEdjJVOUlNLU5TMTdrOGlrd0NKbkFGZXVMeU5vUENzcXlNMlhkdlRBR094RS1NcmczOXNqTnF5MHJaVE93VGwwT3BBOGdlUDBTNWJERFRfbVh1VQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPS1RxWGVmczhnMUdrRkJwMjM0dmMyZ3ZMZUhrSEtoekk2TEpuajhxSU52eU85TXJqQ2lTdmZlb1lFVVZPYjJsWWVab1RRWUduZDdaZFFQVkNWcDJpRDNNajNZbENnQmFtcmVnSG1zcjQ5TzBzZ0FzelpfUUhPZXdVaUxnd1ZfU3hRYi1qcWhSakZjanNPOTR5WUFVSQ?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNUTlPSHg5RWh2UEZuY2lDSmF1Z0Z3UkVscm42OHFKRjRlZ21MemFjNVF1ZmNwaVVHVDgwTW9hd29kRHhLMGpKQU9sV0xubG5JdGs5SEdqTkJiWkJwN1QwWmlCZnFNTHJtc2dNNjVyN2k5LTVrX0c1NDdpUlVxZXNJQ1VzREt1SUsxTGd5MVhfV3o2TWlHbkFQVVBQT0NQcVQ4UEI5Y0pyaThEYTZDOWU4SUxkU2w1Wjl2R1l2aTdBTExNLWN5azhz?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNRkhSalE2SlJmTWZQZ3ZTLXVvY2ppdEhtbFRhS2ZaWXhvV1ljMU85MmVtY2ZKTzd2ZGIwS2xBZDJ4amtwVldoTmN4alhFeTE2c1FTd3NJZmJTVnZ0QmF2aUpBN3dzTlBrOVRoTm9Sc3E3TTByWEhRczFHTDdqVlBBSDF2STMtbmhDUTdPZUJWeDRJQkxXNHp1UTlB?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxPT3cxQW9xbEVqT3I5WjF3V0xXSnNuWktkeEozcEkzbkk0YWJ4d3ZSdy1TbGx2MUFkdTRLeHhMWExzX0tnTXZsR3VhLUtXclZGSUlRdG1ycm9xQUVuVU1lQUhJWi04aVFLR19hNm9nUGRkMzMzVnlRcm1UdFZnN3lSSFN4dGE1Q0ZxVXJUcHdBcW83RFZCZF9HeWpIMmFmODRZX2gzal95amRkR1V2NU84RHRIUzV0dGRDU1pHUEdKazgxZTcxdEE?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxON1ljWFZSZmFkOW00UjVnNnp5b3pxNXR4VHVmTXpkaDdIQ0VwSmtuY0JqRXBfMVRoWTN0TksxT0pHcHRpak5MVDRJVmRoN3FCeElXS2diNjlkNmpESk5MT2w4N0RKZWpJWHQteV9XSFRWcDR1M0RCUFdKa1pCekg3Z3RfN0c4SkF4MFBEQllGZjl2amt4Y2I5WUN3a3FhSXcxd0xQLUloTEJzbzRXTU13RDZXbzhHcElfeUMwSGxnTmRoSnA2SVN4a1M0V3NJdDh6a2o00gHYAUFVX3lxTE5TaHkxTTk4SzBtdXFaRDZpTVNqMEJEZ0ZhLUpMZU45NHZKV05DMGJUYnV0REdISDE3Uk5NX3Iza3lpZVMxajg0QVVYUDZrbXdaZXhxXzBRYVJSSEFRUGlBdnE4cmZYNmstSE1KaldlYmtpR3phczlVYlhMdEl3NDdyQ2h6Wm5sbUtCRWRLeWE1QUxlWHAyenZWSTVoY0JPdThJR3FnM1JZV01oWEtlUGNNU3IwZmVLLThtS25HbVJab0lNYmMxZmtVWmlpS0tyRGJJN3RyM0ZvUw?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxQcFhFSHRRamVwRW1GMmpSNXQ0dnVfX0ZKT0FHblBzSlhqMW85bUhTZ05YT0xLNDZCYi14Tl9lU2FVWFNsUFdTaWloTnhlaG1STlBKcHZseUVSakhrTndkcXptUUFGNVQ3dUtRUWc1Z1FPNWxqZDM2WVFtWVdkbHk5d1Z2SWdlRExRbjNHMDlGRkJyeVpLc1RSTHZCbFM5dlF6T1NSOTJNQ1FVek1RdENsRkY0SUtxVEU1UDNqNlkyQV9JUnNMODZULW9rVVF6U3lwcUQ3SXJXZ9IB3AFBVV95cUxPcUdhYVVJR0xSSnhvVDRTcmMteEdtRktJZGR6emlZQk5lalBYVGF5MzdDNFA2dWFzb2pLLVMzcExyQVpOQVFkM0oySTYxMlRGMXBSSXRyRzRPZGd5LVVsM0o0cHRseURITE94Qm01MzQ0Qmd5N09tbnBSX0VBd0ZBOU5ZZ1BINEVRcDZuR0Y1YW1fMDcwbUp4VGQ2OXZrMXc4Tlh0bGxVVzJLYmtiV0tPRzBLLTV0b1JwYmJCc0h0NzNkSDRnR0dkeDJVV29oYmVfMlNhb08tNG42Uk9l?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
