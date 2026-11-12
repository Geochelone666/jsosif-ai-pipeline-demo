# MCK Intelligence Report

- ticker: **MCK**
- Report as_of: **2026-11-11**
- Market data as_of: **2026-11-11**
- Quant sources: https://finance.yahoo.com/quote/MCK/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MCK/key-statistics/
- AI analysis snapshot as_of: **2026-11-11**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-12T06:03:14.256327+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 13, 'rule': 6, 'ai': 7, 'unknown': 0})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261111T043601Z-d14951e6/MCK** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 13 unique headlines; 6 named publishers; 0 exact duplicates; 13 HTTPS source links; largest publisher share 30.77%; oldest publication 2026-11-04

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1079.7900 |
| Return 1D (%) | -0.2586 |
| Return 1W (%) | 0.9678 |
| Return 1M (%) | 15.0132 |
| Return YTD (%) | 32.0304 |
| Return 1Y (%) | 26.5753 |
| Annualized volatility (%) | 31.7130 |
| Beta vs SPY | -0.1813 |
| Max drawdown (%) | -27.1691 |
| Sharpe (rf=0) | 0.9000 |
| Downside deviation (rf=0, %) | 18.3658 |
| Sortino (rf=0) | 1.5541 |
| Historical VaR 95% (1D, %) | 2.5988 |
| Historical ES 95% (1D, %) | 3.6083 |
| Correlation vs SPY | -0.0785 |
| Tracking error vs SPY (%) | 35.5325 |
| P/E (trailing) | 27.85 |
| P/B | -31.40 |
| EV/EBITDA | 18.12 |
| Revenue growth (%) | 7.60 |
| Forward P/E (estimate) | 20.69 |
| Gross margin (%) | 3.65 |
| Operating margin (%) | 1.59 |
| Return on equity (%) | N/A |
| Free cash flow yield (%) | 5.94 |
| MA50 | 948.4178 |
| Close vs MA50 (%) | 13.8517 |
| MA200 | 870.4437 |
| Close vs MA200 (%) | 24.0505 |
| RSI (14, Wilder) | 72.1190 |
| MACD (12,26) | 36.0536 |
| MACD signal (9) | 30.8849 |
| MACD histogram | 5.1687 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MCK': 280, 'SPY': 280}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1079.7900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.2586 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.9678 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 15.0132 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 32.0304 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 26.5753 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.7130 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 18.3658 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.5541 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5988 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.6083 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0785 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 35.5325 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1813 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.1691 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9000 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 20.6872 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 3.6530 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 1.5900 -> No interpretation rule is available for this metric.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 5.9378 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.8512 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 72.1190 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 5.1687 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 13.8517 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 24.0505 -> Clearly above the moving-average trend level.

## TAILWINDS

### McKesson (MCK) Upgraded to Buy: Here's What You Should Know
- Summary: McKesson (MCK) Upgraded to Buy: Here's What You Should Know
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOQ3p3Z3lxSHBKbHlXYUJ2UWZhTWJJdERxR2lJR1ZFd1UxelhJbnlaNVFCcmc5N21xQUNzMUJPdHhOYk44TkVaRjZCZ01fZlFoeWZLeWQ2VDF2bUF5ckJNdEtQc3NaUGlXQmF5eDZRUW42STRzVTJaM2FCMWdEX3BhY1Ixb1RaQ1d4RXcyN2pmSDdqYXA5NndncUlpaUg?oc=5>

### MCK Q2 Earnings Beat Estimates on Specialty Growth, Outlook Raised
- Summary: MCK Q2 Earnings Beat Estimates on Specialty Growth, Outlook Raised
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxQUDAxR1dQVjZyNGc5bmIyWEN3OExkOW9LQURMdjdnX0dZWnZ6TXdLR3lRNnNIMHAzX2lkTmdtMlU5d1poVXk0LVk1dE9VQUJBdGJkbmd1M3JXN2daOWNYaEVZVUlhcVlQVjVJSWxBOFM3REptYmxUMF9wQlhzUmlNYXZFcFBlMVhWTTh2QUQ5YTA4aFdncE1SckFoaXB4bWxJUHdwcWg4aW1sWGdPcU02OVJTWTBfdkkyRGIzWEdR?oc=5>

### MCK Q2 Earnings Call Highlights Raised Outlook and Specialty Growth
- Summary: MCK Q2 Earnings Call Highlights Raised Outlook and Specialty Growth
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxORlA3d2h2czB1N21TaXJQLXROMmU4bGNYcUNfQjBEWDNOQUx3TnlZVlNZVEZ4TjRpLXFBcmY0cmZ2Ym50bENBaTQxaG1KQkE2QnJhazN5Nk50blJlelp5YmIzZkxVU0RoVGpIZm1TWDJfUExGU3Z3Q1Vkd2V0VF84c3JrM1I4S0twRDVKLXVwd0l5V3hIaXExc0laaFZwbHZjOFFCenFlMmlDbHhuaHM0MFFadlg1dTFYREkzdUt1eTE?oc=5>

### McKesson’s (NYSE:MCK) Q3 CY2026 adjusted EPS top estimates
- Summary: McKesson’s (NYSE:MCK) Q3 CY2026 adjusted EPS top estimates
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQVkRURThFQXlfakZQbVBKVjVTYWtvalZsZmhpckk5aUlzXy0ySDFmU0JWN3pRT2R5aEtzVXRFVWlKenROQ3JwblE2dENUMDFKZU1DVmNYQndnd2lwd2VFVEZzN1JfRkpwUTduZW14d2t5VEZySWRVeDc2Mnp6eVh0dXNvR2pkbnJtTVRza0I5LUtSMjVjU1hlSHZOOFZoYUw0V1Vjb2Z3?oc=5>

### McKesson (MCK) Stock May Be 37% Undervalued On Raised Full Year Guidance
- Summary: Guidance raised, stock undervalued, positive outlook.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxOMjJiZm1TQzFkNjBDSlBfTXowMTZOREI3blhmTk1ESzNZZl9QcG5oTDVPMHQtSW5MOUVOSG9CQjFETTVHMC0tMGZ1aUt4UHpxeld5NVBoa0pYdU1JbkxpWUllVGRIcVNiZ1dQQk1SaHBJTVIwOXItTGhrWUhGSTFqWFV3MEx4RW9lbzhMUGtJaVAxWEFIT2QtTlRiRW9lWDhVcjJTSTdBSFc4RUhPMXI5ekxKYWUtQ3FKTUtMV2pCNF8ybDlN0gHKAUFVX3lxTE9GWlY4ZURyWG5tVm15RV8tdGxjemp3YUgxaFp5N2s0V1ZvT184ckdvUy04MktKSnJsZ1BjbVRqZnBpd1hjcDBWUFdPcl81S2oxOUNvQVNxUjdaWmFQMEx1ck1sWHBPVzZiYVlqcmhRNjFldnhxdm5oNHl1TXhzUVNuUDRfWkdtUmNnOW1tbGhnWkxNNU9qZ2xjQUdGNmlyOU8zakpmUmpDb3N2Ni0zeVBHRTJkNlpUdS1obmhXLXFsOHY3U1lvUUZBQnc?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### McKesson Corp.: Normalized Earnings Suggest Attractive Valuation (MCK)
- Summary: McKesson Corp.: Normalized Earnings Suggest Attractive Valuation (MCK)
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOT2VzOTZScDhOR3JFZGpFVGdNMlgxWTQ1RS1hSkJJMUJVU2s0VC11bGRDMXU3MmROaGdIcnNLMGw2LUlXcmt5WWhVRDVsOUtEczBTRENGakQ0bXo4bkJMU0lmb245cXZaVU1FbFljX0ZlUnhUOGU3ZHJjVWFyN1Z2WlQ3RE04SHlSancxUU9UaU94YUhGaWNwMVNhNy1WS292TlBfQ2V3?oc=5>

### McKesson Corporation 2027 Q2 - Results - Earnings Call Presentation (NYSE:MCK) 2026-11-04
- Summary: McKesson Corporation 2027 Q2 - Results - Earnings Call Presentation (NYSE:MCK) 2026-11-04
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOZ0FTeGJWajY5blJaWW9wVzVqVkRqUjNib3NjSnpOaGxmRTFmdnNlVWN4VWdhVDU4elBXVVlPeV84UWJweGF2aENCRXJKYWEyWE5lR2FXY3lxSkNPVDZSeDl6X1FlNGNKX2xzci1Panlja19OazNvd2Jield2QlQ4NVJ3YVZhV0twWUtwaEdRSzM5YUJwRVNxYUVpR20yNlhTSUx2UXowMA?oc=5>

### 3 Reasons Why Growth Investors Shouldn't Overlook McKesson (MCK)
- Summary: Growth investors are encouraged to consider McKesson for its potential upside, highlighting strategic initiatives and market positioning.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNNWQ5bDd6VGdGRmFGYXltY0NYUnl3UUpRRml1RjBFQ2J0MWFDamZfMU42NzRZWVRleGpXdndzRHNmZFZEQjVHeFE4NEYyX3JUYkNlWFVrVExwakJLZjJGbHBKT193NVlNNmR1dlhyWmZaWXZxVTdDU1Y2SV9hcWhfcmNlWUlsamVGaGZmc1E3UU93a3FBbThzcEtMOA?oc=5>

### Here's What Key Metrics Tell Us About McKesson (MCK) Q2 Earnings
- Summary: Analysis of McKesson's Q2 earnings metrics and performance indicators.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQV3VxdlpheEw3LW92SmJNSHkyRHpWbXJwdzlEbkp3Y3JtUVc4MEhCOFVNX2NLZFdQTzQzQ3VPdUpHNWZHVmdQLWZBMGdpeUdweTNVUElNV3A4MVdaZElMX0FLaDE4eUxCTlYyMjdJdXp1SEU0eE9TTnJ1MHVxOUdSVGhjalBTMjUweTBUMHRUbVVTMlVo?oc=5>

### McKesson Corporation (MCK) Stock Forecasts
- Summary: McKesson releases stock price forecasts for the upcoming period.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPWUZxUnpUcnRpMFN0NWN4WDVHZmY3X1hBZ3I0WGlxN3N5cTloSjBCNmJiV2xQLVFIeUw0OExLNU5fVzdEMjFvdzZ4MTdTd1poZlFxbU8xUDByMVJEVW1Ic1dxdE14X3FQRjRHc1o0YWU5RFVkSnNEYldXMXR6azAtWGh0WEtlSE9IQm40Ug?oc=5>

### 5 insightful analyst questions from McKesson’s Q3 CY2026 earnings call
- Summary: Earnings call provides new information.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxPVHkxS1pGeU9kWGlVdDlKbU9NdHBZMWphQnBfZVo4a1JfbC1fcWpyUS00dzRVYWIwR3hienZIWUViU09hQVlKRHJ2SDh2UzdfOVY2UW9jdjJpakZpQ2hRTXFNYktZc0lVSWMwdmFSenVvYlhfbHJjcGIxUExEY2NSNkQ3Y1djSkMtTzZvTXhDeGJOV1JOYVQxcUR6NnNMZXZoQVRGNC1sYl8yQzN6dzU5VnNST2RTWmI5N3p6elhCc1YzYkl4Qml4R0JTZw?oc=5>

### McKesson (MCK) Posts Strong Q2 Growth, Is The Upside Already Priced In?
- Summary: McKesson reports robust Q2 growth, prompting analysis of whether upside potential is already reflected in the stock price.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPYVV4N1V4cWFTZ05qem9Xai1UU0JuYndoTG8yWEZrREYzaGZ3c2V5TGFNWGoxblZqUnJCY3M4YmlyOUlhNjdNS3JUX2ZpQktaZ2NhaFRaS2xyQnRsWmd2MlRmX2RYVDhmNHFOR3VtdldwT3BFQ1ppYm9rc2ZaM2RjaHFWR2J3dER1UF9JajdyUG0wRmxFYkNyUGw4WFl3dC1tQlZLRWI2VkZJeFNEYTZ0elNHbjRRV3l5eHJyWWFQcElHc3JP0gHKAUFVX3lxTE1lV0VTbVFMT25LSlhGb2V0dmpXMTlMUVpGaDFYUFdOTi0wMi1tamNXem5nbXhpVUhONnk3MGtmRDZLUzB1Q2h6c2hYd090QVgzTjlGZDhrRHNrOXd5Q1NMSzZyNmJ3eFNMeU1FMnNkaC1pM1BNZm5fVnYxYVlseWpINC1vUWFtSmRyd2o5QncwYmZzcGRsODkwd1luc09aZ2NvT0ZVa09fZUUteG81UHZVdXJjYjhhRWItUFNySFBvemsydGgtTEZoZWc?oc=5>

## RISKS

### Officer Francisco Fraga proposes selling 600 shares of McKesson (MCK).
- Summary: An officer's proposal to sell 600 shares may signal internal concerns or liquidity needs, potentially affecting investor confidence.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPbDFkVFBxcXZUNkc4eGhzdG9VdFlHeUxpQjg3RjdXNUxuYzhNeEdpZzVWUXYyTEdfRC1WSEhxTkhUX0NvLV9zOWhRQ3BIMWFIc0dSMFc0NTQzQ2xORl82enJJMVhtQjRoMDNmNzBoUVM1S3FZZ2VXYlQxR2RWYm55dUJMdXNMXzVjUlgtTi1fSi04RlE?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MCK** | **27.85** | **-31.40** | **18.12** | **7.60** | **124,668,952,576.00 USD** | **26.58** |
| COR | 19.49 | 18.14 | 12.79 | 5.50 | 66,766,610,432.00 USD | -3.43 |
| CAH | 35.80 | -21.28 | 15.46 | 5.50 | 64,128,868,352.00 USD | 36.75 |
| CNC | 24.22 | 1.57 | 5.74 | 0.20 | 34,892,394,496.00 USD | 99.32 |

Peers fetched as_of: 2026-11-11; MCK reuses existing data (market data as_of: 2026-11-11); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-11

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 29,980,000,000.00 USD; period 2011-04-01/2011-06-30; fiscal year/reporting period 2011/Q1
- Net income (latest available single quarter): 1,218,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2027/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/927653/000092765326000281/mck-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMinAFBVV95cUxOQ3p3Z3lxSHBKbHlXYUJ2UWZhTWJJdERxR2lJR1ZFd1UxelhJbnlaNVFCcmc5N21xQUNzMUJPdHhOYk44TkVaRjZCZ01fZlFoeWZLeWQ2VDF2bUF5ckJNdEtQc3NaUGlXQmF5eDZRUW42STRzVTJaM2FCMWdEX3BhY1Ixb1RaQ1d4RXcyN2pmSDdqYXA5NndncUlpaUg?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxQUDAxR1dQVjZyNGc5bmIyWEN3OExkOW9LQURMdjdnX0dZWnZ6TXdLR3lRNnNIMHAzX2lkTmdtMlU5d1poVXk0LVk1dE9VQUJBdGJkbmd1M3JXN2daOWNYaEVZVUlhcVlQVjVJSWxBOFM3REptYmxUMF9wQlhzUmlNYXZFcFBlMVhWTTh2QUQ5YTA4aFdncE1SckFoaXB4bWxJUHdwcWg4aW1sWGdPcU02OVJTWTBfdkkyRGIzWEdR?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxORlA3d2h2czB1N21TaXJQLXROMmU4bGNYcUNfQjBEWDNOQUx3TnlZVlNZVEZ4TjRpLXFBcmY0cmZ2Ym50bENBaTQxaG1KQkE2QnJhazN5Nk50blJlelp5YmIzZkxVU0RoVGpIZm1TWDJfUExGU3Z3Q1Vkd2V0VF84c3JrM1I4S0twRDVKLXVwd0l5V3hIaXExc0laaFZwbHZjOFFCenFlMmlDbHhuaHM0MFFadlg1dTFYREkzdUt1eTE?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQVkRURThFQXlfakZQbVBKVjVTYWtvalZsZmhpckk5aUlzXy0ySDFmU0JWN3pRT2R5aEtzVXRFVWlKenROQ3JwblE2dENUMDFKZU1DVmNYQndnd2lwd2VFVEZzN1JfRkpwUTduZW14d2t5VEZySWRVeDc2Mnp6eVh0dXNvR2pkbnJtTVRza0I5LUtSMjVjU1hlSHZOOFZoYUw0V1Vjb2Z3?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxOMjJiZm1TQzFkNjBDSlBfTXowMTZOREI3blhmTk1ESzNZZl9QcG5oTDVPMHQtSW5MOUVOSG9CQjFETTVHMC0tMGZ1aUt4UHpxeld5NVBoa0pYdU1JbkxpWUllVGRIcVNiZ1dQQk1SaHBJTVIwOXItTGhrWUhGSTFqWFV3MEx4RW9lbzhMUGtJaVAxWEFIT2QtTlRiRW9lWDhVcjJTSTdBSFc4RUhPMXI5ekxKYWUtQ3FKTUtMV2pCNF8ybDlN0gHKAUFVX3lxTE9GWlY4ZURyWG5tVm15RV8tdGxjemp3YUgxaFp5N2s0V1ZvT184ckdvUy04MktKSnJsZ1BjbVRqZnBpd1hjcDBWUFdPcl81S2oxOUNvQVNxUjdaWmFQMEx1ck1sWHBPVzZiYVlqcmhRNjFldnhxdm5oNHl1TXhzUVNuUDRfWkdtUmNnOW1tbGhnWkxNNU9qZ2xjQUdGNmlyOU8zakpmUmpDb3N2Ni0zeVBHRTJkNlpUdS1obmhXLXFsOHY3U1lvUUZBQnc?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOT2VzOTZScDhOR3JFZGpFVGdNMlgxWTQ1RS1hSkJJMUJVU2s0VC11bGRDMXU3MmROaGdIcnNLMGw2LUlXcmt5WWhVRDVsOUtEczBTRENGakQ0bXo4bkJMU0lmb245cXZaVU1FbFljX0ZlUnhUOGU3ZHJjVWFyN1Z2WlQ3RE04SHlSancxUU9UaU94YUhGaWNwMVNhNy1WS292TlBfQ2V3?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOZ0FTeGJWajY5blJaWW9wVzVqVkRqUjNib3NjSnpOaGxmRTFmdnNlVWN4VWdhVDU4elBXVVlPeV84UWJweGF2aENCRXJKYWEyWE5lR2FXY3lxSkNPVDZSeDl6X1FlNGNKX2xzci1Panlja19OazNvd2Jield2QlQ4NVJ3YVZhV0twWUtwaEdRSzM5YUJwRVNxYUVpR20yNlhTSUx2UXowMA?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNNWQ5bDd6VGdGRmFGYXltY0NYUnl3UUpRRml1RjBFQ2J0MWFDamZfMU42NzRZWVRleGpXdndzRHNmZFZEQjVHeFE4NEYyX3JUYkNlWFVrVExwakJLZjJGbHBKT193NVlNNmR1dlhyWmZaWXZxVTdDU1Y2SV9hcWhfcmNlWUlsamVGaGZmc1E3UU93a3FBbThzcEtMOA?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQV3VxdlpheEw3LW92SmJNSHkyRHpWbXJwdzlEbkp3Y3JtUVc4MEhCOFVNX2NLZFdQTzQzQ3VPdUpHNWZHVmdQLWZBMGdpeUdweTNVUElNV3A4MVdaZElMX0FLaDE4eUxCTlYyMjdJdXp1SEU0eE9TTnJ1MHVxOUdSVGhjalBTMjUweTBUMHRUbVVTMlVo?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPWUZxUnpUcnRpMFN0NWN4WDVHZmY3X1hBZ3I0WGlxN3N5cTloSjBCNmJiV2xQLVFIeUw0OExLNU5fVzdEMjFvdzZ4MTdTd1poZlFxbU8xUDByMVJEVW1Ic1dxdE14X3FQRjRHc1o0YWU5RFVkSnNEYldXMXR6azAtWGh0WEtlSE9IQm40Ug?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxPVHkxS1pGeU9kWGlVdDlKbU9NdHBZMWphQnBfZVo4a1JfbC1fcWpyUS00dzRVYWIwR3hienZIWUViU09hQVlKRHJ2SDh2UzdfOVY2UW9jdjJpakZpQ2hRTXFNYktZc0lVSWMwdmFSenVvYlhfbHJjcGIxUExEY2NSNkQ3Y1djSkMtTzZvTXhDeGJOV1JOYVQxcUR6NnNMZXZoQVRGNC1sYl8yQzN6dzU5VnNST2RTWmI5N3p6elhCc1YzYkl4Qml4R0JTZw?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPYVV4N1V4cWFTZ05qem9Xai1UU0JuYndoTG8yWEZrREYzaGZ3c2V5TGFNWGoxblZqUnJCY3M4YmlyOUlhNjdNS3JUX2ZpQktaZ2NhaFRaS2xyQnRsWmd2MlRmX2RYVDhmNHFOR3VtdldwT3BFQ1ppYm9rc2ZaM2RjaHFWR2J3dER1UF9JajdyUG0wRmxFYkNyUGw4WFl3dC1tQlZLRWI2VkZJeFNEYTZ0elNHbjRRV3l5eHJyWWFQcElHc3JP0gHKAUFVX3lxTE1lV0VTbVFMT25LSlhGb2V0dmpXMTlMUVpGaDFYUFdOTi0wMi1tamNXem5nbXhpVUhONnk3MGtmRDZLUzB1Q2h6c2hYd090QVgzTjlGZDhrRHNrOXd5Q1NMSzZyNmJ3eFNMeU1FMnNkaC1pM1BNZm5fVnYxYVlseWpINC1vUWFtSmRyd2o5QncwYmZzcGRsODkwd1luc09aZ2NvT0ZVa09fZUUteG81UHZVdXJjYjhhRWItUFNySFBvemsydGgtTEZoZWc?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPbDFkVFBxcXZUNkc4eGhzdG9VdFlHeUxpQjg3RjdXNUxuYzhNeEdpZzVWUXYyTEdfRC1WSEhxTkhUX0NvLV9zOWhRQ3BIMWFIc0dSMFc0NTQzQ2xORl82enJJMVhtQjRoMDNmNzBoUVM1S3FZZ2VXYlQxR2RWYm55dUJMdXNMXzVjUlgtTi1fSi04RlE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
