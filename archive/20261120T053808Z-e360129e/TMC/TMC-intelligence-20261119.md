# TMC Intelligence Report

- ticker: **TMC**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-18**
- Quant sources: https://finance.yahoo.com/quote/TMC/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TMC/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T05:55:01.849180+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 11, 'rule': 5, 'ai': 2, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 11 unique headlines; 9 named publishers; 0 exact duplicates; 11 HTTPS source links; largest publisher share 18.18%; oldest publication 2026-11-12

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1.7300 |
| Return 1D (%) | -6.9892 |
| Return 1W (%) | -29.5316 |
| Return 1M (%) | -32.9457 |
| Return YTD (%) | -71.9611 |
| Return 1Y (%) | -68.0812 |
| Annualized volatility (%) | 94.5336 |
| Beta vs SPY | 3.6010 |
| Max drawdown (%) | -81.6737 |
| Sharpe (rf=0) | -0.7453 |
| Downside deviation (rf=0, %) | 64.4139 |
| Sortino (rf=0) | -1.0938 |
| Historical VaR 95% (1D, %) | 9.3843 |
| Historical ES 95% (1D, %) | 12.0481 |
| Correlation vs SPY | 0.5240 |
| Tracking error vs SPY (%) | 88.1071 |
| P/E (trailing) | N/A |
| P/B | -16.77 |
| EV/EBITDA | -3.56 |
| Revenue growth (%) | N/A |
| Forward P/E (estimate) | N/A |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 0.00 |
| Return on equity (%) | N/A |
| Free cash flow yield (%) | -2.22 |
| MA50 | 3.0565 |
| Close vs MA50 (%) | -43.3993 |
| MA200 | 4.5426 |
| Close vs MA200 (%) | -61.9159 |
| RSI (14, Wilder) | 28.8355 |
| MACD (12,26) | -0.2954 |
| MACD signal (9) | -0.2768 |
| MACD histogram | -0.0186 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TMC': 285, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1.7300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -6.9892 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -29.5316 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -32.9457 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -71.9611 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -68.0812 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 94.5336 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 64.4139 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.0938 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 9.3843 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 12.0481 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5240 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 88.1071 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.6010 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -81.6737 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.7453 -> Negative risk-adjusted return.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -2.2229 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 28.8355 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0186 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -43.3993 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -61.9159 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### The Metals Company Falls 7% Near Annual Low
- Summary: The Metals Company Falls 7% Near Annual Low
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxONXYyRUw4a3RZTzBjQUFjMHhabERrUVJKRzNHelVlak1adjZobFl5QVN5ZDZYVEJpTkRJVVRTb0JUcEhPSjlHaDRKTWhFQi1SNmM5WFN2ampMaE1Sckx2aG9zSWk0d1Ryc0gtRExMNTBTbVlaVG04SzVrazM1cVo1V2VzN3c?oc=5>

## CATALYSTS

### TMC the metals company Inc. Stock 12‑Month Price Target Cut to $9.63, Implies 319% Upside
- Summary: TMC the metals company Inc. Stock 12‑Month Price Target Cut to $9.63, Implies 319% Upside
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxQSm5HRy1zenU5YmRyQXRSc0JXaGo5Vm41UDlPVENUdHFWZmZVUnZFOUJvcmNQRTNqNVV4TmVQRU42LVJucTJzeGNOaUJ3Yk9XZWdDRHdmemllZFJ3RC1BV3FpSVpQX1NsT0E1aXpzVlFLcFFzVHBQd2wwTTV6MFNDT0RvX1pNcDQ1ZnBiVGNyQnpmQjRGVVBaYnBLVlpLc0NFSXA5VWJIaXRBN1R2R2pGS2VZeFBNSFRkeG9Kdi0yQWVodElEVEN3eWJPSGtWT3BNeTJ4RWFuWmpWNmczVUJVSQ?oc=5>

### TMC the metals company Inc. Q3 2026 Earnings Call Summary
- Summary: TMC the metals company Inc. Q3 2026 Earnings Call Summary
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPMFFWaEFLVGVlQ0RKM0FCWmRUOURIOGp2VVZoUXRVbnZQM1FDZ3BKdWJ1RlhsR2NzMmlldTFVOVZsUVlsZXgyVTNTaGM2TkM5cDdLSFd6dXJJajM4eTl3aGNLQ1RHeXYtQ0VQeEtpbng4cDVmeFhXLUhZTE44MVpOUDF6bzNOY0JaeUxYdGV6YzVudGhS?oc=5>

### TMC the metals company Inc. 2026 Q3 - Results - Earnings Call Presentation
- Summary: TMC the metals company Inc. 2026 Q3 - Results - Earnings Call Presentation
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxNV3g4NHZwdDFEbUIwU1phdkxNUE5BWjhQaEJvX19xMkJtWUg0SmlHMWpFTXQxQnBFb3FPWTBndlhDQU9ZY1NkNXJYQlNBXzcxMkFqaW93OTQwVzhpZ0RwVVA3LUpCODhRMkRIUmNKbWdJMzNRZnJIWjFoRFNxTWdXQnI0eUtMaUNITEFlRVd5MFFfbHlSaExPZy1XX3ZTd3VGUS1oMkVfbHVqY1NDZ0dn?oc=5>

### TMC the metals company Inc. Reports Earnings Results for the Third Quarter and Nine Months Ended September 30, 2026
- Summary: TMC the metals company Inc. Reports Earnings Results for the Third Quarter and Nine Months Ended September 30, 2026
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5wFBVV95cUxQWEd0eGF5Mk13UUNibGd5VFJPZWc2OFFMekExazBYTmg4bGpxNlVvMV9Hc1Fuc1ZRNjBzT3FvR0wwQkJiR1pZOFoxZnRYVzI0a3NKSEVuckxDdWVnTk5qc3BMclFxYWFfQURLWkJDcG5RQl9WVUNxQ0oybVMyekFhX3d3bmRFMUhLLVpLYTNmRV9oakl1b1VXekNHOUZLX3o2dWdMUHFhQUR5TnNhMEhOajJpRHZ3WFdoMXVBbDR6dVZSYlBJSU5YbDdSRFNPbVpta1JqVWNMYlNpOGJ6bTJ2N1JiWno5NEE?oc=5>

### TMC The Metals Company Q3 Loss Narrows
- Summary: Q3 loss narrowed, indicating improved profitability.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQRFlJTEZfOGE1dWxTRzFsTnhWaUJSdjE1NlZtaHFDMVI2Y2doaVYwRGhmd0JuS0JVd2hFRDhNX28wYUZpMC02MWo1cUVBc1dRMjA1Z0hHNHJkVHdac3E5QXhLWHpnYjd0WlVsblJuRzVkSzRzZ2pMM1NyR3EwU0V4UmFBZ0lhdTlFM3VsVWY0NUpoVldoZVE?oc=5>

### Weekly Recap: TMC needs commercialization financing and Q3 net loss narrows
- Summary: TMC seeks financing while narrowing Q3 loss, indicating potential operational improvement.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxOZ1lTNXpwN2lwMV9wWENBWnVjNzRRdWtlcEJadFRZTUIySE5qdzBleFM0RTl0TjBJd0NJZnJ0RWU0RkxTam9xdFlTbFlYNExpaXZkd2hDVW1PNmlydWttSFBuUFJHTHgxQUV5NnQ2OU1XVGVhbFVDWnZUMFB0OTg2dEZJQU92ZGMzTThTZW1kdVNQYUFWLTZ1X21JcEduQnNiZTlpY1l3NldrSEYtdkJKN0l5eHFjaFAxX3h0blBySnVrVGk5Z2M1SHhxbDJGTDZxRVE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TMC** | **N/A** | **-16.77** | **-3.56** | **N/A** | **939,548,288.00 USD** | **-68.08** |
| MP | N/A | 3.35 | 105.81 | 190.90 | 6,535,303,680.00 USD | -38.56 |
| LAC | 3.80 | 0.32 | -22.24 | N/A | 501,855,232.00 USD | -72.55 |
| VALE | 61.44 | 1.08 | 1.86 | -3.90 | 41,834,156,032.00 USD | -12.17 |

Peers fetched as_of: 2026-11-19; TMC reuses existing data (market data as_of: 2026-11-18); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-12
- Next expected earnings: 2027-03-25 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-19

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-12
- Revenue (latest available single quarter): 410,000.00 USD; period 2024-04-01/2024-06-30; fiscal year/reporting period 2024/Q2
- Net income (latest available single quarter): -28,361,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1798562/000162828026073463/tmc-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMihAFBVV95cUxONXYyRUw4a3RZTzBjQUFjMHhabERrUVJKRzNHelVlak1adjZobFl5QVN5ZDZYVEJpTkRJVVRTb0JUcEhPSjlHaDRKTWhFQi1SNmM5WFN2ampMaE1Sckx2aG9zSWk0d1Ryc0gtRExMNTBTbVlaVG04SzVrazM1cVo1V2VzN3c?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxQSm5HRy1zenU5YmRyQXRSc0JXaGo5Vm41UDlPVENUdHFWZmZVUnZFOUJvcmNQRTNqNVV4TmVQRU42LVJucTJzeGNOaUJ3Yk9XZWdDRHdmemllZFJ3RC1BV3FpSVpQX1NsT0E1aXpzVlFLcFFzVHBQd2wwTTV6MFNDT0RvX1pNcDQ1ZnBiVGNyQnpmQjRGVVBaYnBLVlpLc0NFSXA5VWJIaXRBN1R2R2pGS2VZeFBNSFRkeG9Kdi0yQWVodElEVEN3eWJPSGtWT3BNeTJ4RWFuWmpWNmczVUJVSQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPMFFWaEFLVGVlQ0RKM0FCWmRUOURIOGp2VVZoUXRVbnZQM1FDZ3BKdWJ1RlhsR2NzMmlldTFVOVZsUVlsZXgyVTNTaGM2TkM5cDdLSFd6dXJJajM4eTl3aGNLQ1RHeXYtQ0VQeEtpbng4cDVmeFhXLUhZTE44MVpOUDF6bzNOY0JaeUxYdGV6YzVudGhS?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxNV3g4NHZwdDFEbUIwU1phdkxNUE5BWjhQaEJvX19xMkJtWUg0SmlHMWpFTXQxQnBFb3FPWTBndlhDQU9ZY1NkNXJYQlNBXzcxMkFqaW93OTQwVzhpZ0RwVVA3LUpCODhRMkRIUmNKbWdJMzNRZnJIWjFoRFNxTWdXQnI0eUtMaUNITEFlRVd5MFFfbHlSaExPZy1XX3ZTd3VGUS1oMkVfbHVqY1NDZ0dn?oc=5
- https://news.google.com/rss/articles/CBMi5wFBVV95cUxQWEd0eGF5Mk13UUNibGd5VFJPZWc2OFFMekExazBYTmg4bGpxNlVvMV9Hc1Fuc1ZRNjBzT3FvR0wwQkJiR1pZOFoxZnRYVzI0a3NKSEVuckxDdWVnTk5qc3BMclFxYWFfQURLWkJDcG5RQl9WVUNxQ0oybVMyekFhX3d3bmRFMUhLLVpLYTNmRV9oakl1b1VXekNHOUZLX3o2dWdMUHFhQUR5TnNhMEhOajJpRHZ3WFdoMXVBbDR6dVZSYlBJSU5YbDdSRFNPbVpta1JqVWNMYlNpOGJ6bTJ2N1JiWno5NEE?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQRFlJTEZfOGE1dWxTRzFsTnhWaUJSdjE1NlZtaHFDMVI2Y2doaVYwRGhmd0JuS0JVd2hFRDhNX28wYUZpMC02MWo1cUVBc1dRMjA1Z0hHNHJkVHdac3E5QXhLWHpnYjd0WlVsblJuRzVkSzRzZ2pMM1NyR3EwU0V4UmFBZ0lhdTlFM3VsVWY0NUpoVldoZVE?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxOZ1lTNXpwN2lwMV9wWENBWnVjNzRRdWtlcEJadFRZTUIySE5qdzBleFM0RTl0TjBJd0NJZnJ0RWU0RkxTam9xdFlTbFlYNExpaXZkd2hDVW1PNmlydWttSFBuUFJHTHgxQUV5NnQ2OU1XVGVhbFVDWnZUMFB0OTg2dEZJQU92ZGMzTThTZW1kdVNQYUFWLTZ1X21JcEduQnNiZTlpY1l3NldrSEYtdkJKN0l5eHFjaFAxX3h0blBySnVrVGk5Z2M1SHhxbDJGTDZxRVE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
