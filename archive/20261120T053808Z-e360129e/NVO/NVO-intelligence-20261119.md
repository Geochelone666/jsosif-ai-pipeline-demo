# NVO Intelligence Report

- ticker: **NVO**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-19**
- Quant sources: https://finance.yahoo.com/quote/NVO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVO/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T05:49:28.085789+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 21, 'rule': 2, 'ai': 13, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261118T054934Z-e0d070d9/NVO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 21 unique headlines; 10 named publishers; 0 exact duplicates; 21 HTTPS source links; largest publisher share 23.81%; oldest publication 2026-11-15

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 38.8700 |
| Return 1D (%) | -1.4202 |
| Return 1W (%) | -4.3789 |
| Return 1M (%) | 1.1713 |
| Return YTD (%) | -19.7908 |
| Return 1Y (%) | -16.7133 |
| Annualized volatility (%) | 45.3748 |
| Beta vs SPY | 0.9316 |
| Max drawdown (%) | -43.6699 |
| Sharpe (rf=0) | -0.1731 |
| Downside deviation (rf=0, %) | 34.0759 |
| Sortino (rf=0) | -0.2305 |
| Historical VaR 95% (1D, %) | 3.1211 |
| Historical ES 95% (1D, %) | 7.1674 |
| Correlation vs SPY | 0.2854 |
| Tracking error vs SPY (%) | 43.4985 |
| P/E (trailing) | 9.82 |
| P/B | 5.24 |
| EV/EBITDA | 1.43 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 11.07 |
| Gross margin (%) | 83.33 |
| Operating margin (%) | 50.78 |
| Return on equity (%) | 58.38 |
| Free cash flow yield (%) | N/A |
| MA50 | 39.6922 |
| Close vs MA50 (%) | -2.0714 |
| MA200 | 42.2847 |
| Close vs MA200 (%) | -8.0754 |
| RSI (14, Wilder) | 42.5522 |
| MACD (12,26) | 0.1133 |
| MACD signal (9) | 0.2254 |
| MACD histogram | -0.1121 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVO': 286, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 38.8700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.4202 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.3789 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 1.1713 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -19.7908 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -16.7133 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 45.3748 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 34.0759 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.2305 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.1211 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 7.1674 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2854 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 43.4985 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.9316 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.6699 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.1731 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.0664 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 83.3330 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 50.7790 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 58.3840 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 9.8157 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 42.5522 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1121 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -2.0714 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -8.0754 -> Clearly below the moving-average trend level.

## TAILWINDS

### Novo Nordisk reports additional CagriSema weight-loss findings (NVO:NYSE)
- Summary: Novo Nordisk announces new weight‑loss study results for CagriSema, supporting its efficacy and expanding its product portfolio.
- Date: 2026-11-15 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNaFdxUTJqNDdlLVA1b3FTR0ZJM1BzR3diSVlGSE9pQy1ZNmxpQS1HcHRsR0c5TEFaNzFGN3VlVDF0bU96REVEblFpOGtSQ0x4a3dMdU0ybVhjNVd3SlVZRDVyR0VkV2VKV3hSMHUyOUFONFRLMUhaYVlKRjhBYmN6bHptY0ZaeTJWNGJDZGstUnNpOVJtZDZzNlRRbVlIQUU5bEE?oc=5>

### What Could Novo Nordisk (NYSE:NVO) Reveal in Its Next Quarterly Results?
- Summary: Speculation on upcoming quarterly earnings highlights potential financial performance and guidance from Novo Nordisk.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOcHBNWHh3dEtZWUotYV92ZXg4VEpHbVlOeVhhRjdDeXNETE1pUE9yUFRYLWlrV0lPZGNqXzJDTjc2aHBOQ0tsTmRuUGdEQm9fSkRPLVNXM2RHeTdhTzQ2Zk5tQ1VPekdveWM2Mi1KVmo1T2xSVC1RMkxrMTAwMXhrQktiWkxHVjRlYUFHWHo4MmRFMXVRUTBoYjdlZmJIQkZGb0pLNU1PNkJhaGNualNhUFRDWFI?oc=5>

### Novo Nordisk (NVO) Stock May Be Undervalued On Raised 2026 Outlook
- Summary: Raised 2026 outlook suggests potential undervaluation, indicating positive future prospects.
- Date: 2026-11-18 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxQVURxcXYxR3g3SzdwZHNCZGVyWkxqMkJpUVRYLVFtNDllMTVsemtZU1VmRTlMSVFnazU0Ynhtc3FPWS0yUjg4ZWEybTlOWFR6SGpPX29kRGVQMl9kdWQ4SnBiWUF1Z3ZJRWl1Rlp6RFIxRnZicVN3OWRjVVdsb2VtQQ?oc=5>

### Novo Nordisk: A Return To Growth May Be Just Around The Corner (NYSE:NVO)
- Summary: Anticipated return to growth signals favorable outlook for the company.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNYi1OZnF4N2hudHlDM1lRQjVwd2xHOG1UamNXX1pKLVBjMTBaVWVoWTkwdXZQV0YtVy1EYy0xYzJ6Q2Vwc1BqR3FKYnNFZk83TjBXdE1QdDh3a2RZYmNiZ1NZdUd6Q2R3akttNnk3dGhaOXNUeVJJV0hEMGFIc2tQOE4wQVlqa0k0cWNvUWZOZEdmTmpkaDhfRkxsVFJDaEpqRks5Vg?oc=5>

## HEADWINDS

### Novo Nordisk stock falls as sellers keep control and support remains in focus
- Summary: Novo Nordisk stock falls as sellers keep control and support remains in focus
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxNNmM1ZzlMd1F4THI0VHI3LVA0c0hUU2xEX3A1dUxSMzFyeFcwUzNmNVhIRWhpbGl1SXN3N184NDhoR0hNRzNLWWNmM3hSeGVUMXhwRndCeXVlVnE5bDVxcGFYV0pjS0M0a1dDdTRHeFQyNDZSVllXVWpTUUdEUzJLZHQzU2tuc2gwaVd5UWx3?oc=5>

### What's behind Novo Nordisk's latest 2.8% stock pullback?
- Summary: Recent 2.8% stock pullback indicates short‑term market pressure.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxORTZKTGNsM29zVEpQbW4ySjVRZ0pGN0VOVG9aNjdqaWpPUDJpaEQ0MHVqVENLdV9hU1ZLaXFDcFVsNk9CSE50M2hzY1Q1V0xHRDR0dTNEd2JqdXBVOUhodlI5Sl91TndCbnh3aVAzZk0xLUdLZmRtU3NwcGl2cFF6cmVMdVQ0MDlWNlQ0UXN0a3A?oc=5>

### Novo Nordisk (NVO) Could Be 47% Below Fair Value Following Its AI Push
- Summary: AI push may have led to undervaluation, suggesting a short‑term headwind.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxNVVh1Z1RmUDEwd3JUV3J0V3VqeGVGaks0RGVhMVFjcDFveEVQX0xuQjhrbTNoazVzZVhFNGJUR3FlNTZUUG5xWmduaTVfQWF4akYzbEItc1BRYXlfb1N6TG5xaXZfcmlKUGJJOWJCbE9felhCd3ZRRUNtSGhDU2dpRnl1Q1lGZHBYVlh1RXotNA?oc=5>

## CATALYSTS

### Novo Nordisk Details Share Repurchases Through November 13
- Summary: Novo Nordisk Details Share Repurchases Through November 13
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQWnRVYXd1cHFIVFZhTkt6YVB0RGdmMXIwMUtWTzdrLVhLZTRsLUw3RkpWak0wUmpVb3oxSjg2dV9zdThzekFTRUVVazYwWTJqTl9WejFfck5aeUpLd05oN2Rjc25SWEVuREFEVVdjdExycC00Zm5va040dm9iUS1kenVzNHR2NER6X1kwSFlJVHFzWGxtUWk5Q19OV3pDQkFXR21CMnZkbDBPRS1wYXU4?oc=5>

### Buybacks at Novo Nordisk (NVO) total 43.7 million B shares; treasury holdings equal 1.3%.
- Summary: Company repurchases 43.7M shares, reducing shares outstanding.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQSm1sdVlfVVg2ZEZHTU9PNTl3UmdFb21SRHZGaV9YdTFXWXczdDlONkZkVEE1QXJYcjBPU0FXWF9QSHBWbjc5ek04X3F3WE5hQzBuUFFvXzAzbF8xQWpiTFpIOFF6WjhTN2Qzb0RHa2tHZkZGS1RnM25LWENCTFlLNjNVQlRYOWF1Y0FjZUZfbjl0UGpLX1BKbFJkMXM3TGZmaGs3Umw1UHZCX3RYdEdueQ?oc=5>

### Novo Nordisk presents new research that includes cagrilintide study
- Summary: Novo Nordisk announced new research featuring a cagrilintide study, indicating potential therapeutic advancements.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxOcnppenhTdFVSVFY2VDNPWnBIbE9ralhlWE1rYk83NmMzOUZVMGZHSXMxSTdSaWNEbkJhSXpRaGo4Sy0tVGwxU3YwSjhMcmdQbGZPVlEyXzBBY3l5cUxXa2tWNHlGa2xOUWdmRE83NjZveThvb2xBNThKTDBjcGVaRnFGeW9mMW5NZlRyQV80THJGUWQyRm5TMFBVUU9Lay03RlRvRmhFdnN2dTRwYjNJMXR4d0JFcXFN?oc=5>

### Prediction: $10,000 Equally Split Between Eli Lilly and Novo Nordisk Will Be Worth This Much by the End of 2027
- Summary: Forecast of split value between Eli Lilly and Novo Nordisk by 2027.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxQdWRfSklGakphaGhZZGRVaFZkblJuOVR4UlBJRXNoQjVHSXV3ODQtbW5yUHpSQWNnMk1pMDIxSkc5cXA0THBONUREa3BleWJNLThhNFpELWlGVUpidXNWUE5haVhCMkdEQUJGSnJvZGFnalRMYzFCaU1JWVpURjh0a0lVWnNBX3FmejdDMHhqc2hieFlkcC1idnItNzBsSUM1NzBjMk1SUE5GbzNLT0VCZG5SRzFjdW9fcEZaUzZzUnl6RnNSejV2RkpVbl9GR2RyU01Fek44UzM3VERRY1Q5emtVZ3Y5MzBsaTlB?oc=5>

### Will Novo Nordisk stock avoid deeper losses amid seller dominance?
- Summary: Question on potential stock decline amid seller dominance.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxNQWV5aHNUNlVtV1ItQkpyRDkyc2dUSTFtSHp1THl3cEZzT0dqaTcxakFIUjZ2eEJ0ZVNSN1lJQzdzLXVVcTJyc2dnNjZlWUNIS0loQzdBXzRfUFBQaW83bTAyVEtYOVhjVVUxZ2FaX0l0djNFN25ZR2RPdnVkdElLcTVMRnZ3WWxUVkhEMw?oc=5>

### Novo Nordisk: The Worst May Be Behind (NYSE:NVO)
- Summary: Positive outlook suggesting improvement for Novo Nordisk.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxQeng0TGVnR1BPRG5ENFZNNE1OX2JaTmlOMTFKNlBqcVhtaHF3aWRtaGVuQXZWUjItUG43T1RBWEtTaElFbXVuVURaem1tWmlwaWlRTHBlcGJGdmhYU3VzMTdDLU5oakdwUFVsU1EyYjFRMl9zSDh6QmpBdjFDcVUtT1pvZw?oc=5>

### Novo Nordisk A/S Stock (NVO) Moved Down by 3.12% on Nov 18: What Investors Need To Know
- Summary: Stock fell 3.12% on Nov 18, investors advised.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxONGNNMV9xVGhZcUlCa0VIWEI1S1ZPZFY4R05nbGNURHNOb294YldzYVRGUEVYMXpRd19STWsxWGNfQ0xNZ2p6clZ1Q1dpYmVna0NJOG0tVU00NVVQRDc3dlFISS1VSGlnQWhWS2NZanRLV3o0Z2hERGZ2TVl1X2plbjQwYk1oU0dUcnc?oc=5>

### Novo Nordisk (NVO) Stock Price Prediction: Pullback holds near lower Bollinger support as futures positioning builds
- Summary: Prediction of pullback near lower Bollinger support.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxQWXpxbTB2bHJBZ2otVXJ3TUN5TFRza0l0OXZmd3BKUFZFQkdFMGgwM2FSa25xeVliNzZWa1R2MmpncGw0MTlnUjNxanhrSVZTNjBwcGh5NFJuWnBSc1NSV3lOSXJncEl1aXJyY0xMWUdPZTQwN2hDcjZFSU5VcTNUN0llWXBVOWV5RUtYU3daSGNFUzhSTUR6NGJvcGhtakFjU2xuMA?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVO** | **9.82** | **5.24** | **1.43** | **5.60** | **171,313,872,896.00 USD** | **-16.71** |
| LLY | 43.85 | 29.90 | 26.85 | 38.60 | 1,203,503,366,144.00 USD | 29.51 |
| ROG.SW | N/A | N/A | N/A | N/A | N/A unknown currency | N/A |
| SAN.PA | 24.22 | 1.38 | 7.77 | 15.70 | 100,598,808,576.00 EUR | 3.99 |

Peers fetched as_of: 2026-11-19; NVO reuses existing data (market data as_of: 2026-11-19); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-19

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: N/A
- Filing date: N/A
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: N/A

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiogFBVV95cUxNaFdxUTJqNDdlLVA1b3FTR0ZJM1BzR3diSVlGSE9pQy1ZNmxpQS1HcHRsR0c5TEFaNzFGN3VlVDF0bU96REVEblFpOGtSQ0x4a3dMdU0ybVhjNVd3SlVZRDVyR0VkV2VKV3hSMHUyOUFONFRLMUhaYVlKRjhBYmN6bHptY0ZaeTJWNGJDZGstUnNpOVJtZDZzNlRRbVlIQUU5bEE?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxOcHBNWHh3dEtZWUotYV92ZXg4VEpHbVlOeVhhRjdDeXNETE1pUE9yUFRYLWlrV0lPZGNqXzJDTjc2aHBOQ0tsTmRuUGdEQm9fSkRPLVNXM2RHeTdhTzQ2Zk5tQ1VPekdveWM2Mi1KVmo1T2xSVC1RMkxrMTAwMXhrQktiWkxHVjRlYUFHWHo4MmRFMXVRUTBoYjdlZmJIQkZGb0pLNU1PNkJhaGNualNhUFRDWFI?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxQVURxcXYxR3g3SzdwZHNCZGVyWkxqMkJpUVRYLVFtNDllMTVsemtZU1VmRTlMSVFnazU0Ynhtc3FPWS0yUjg4ZWEybTlOWFR6SGpPX29kRGVQMl9kdWQ4SnBiWUF1Z3ZJRWl1Rlp6RFIxRnZicVN3OWRjVVdsb2VtQQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNYi1OZnF4N2hudHlDM1lRQjVwd2xHOG1UamNXX1pKLVBjMTBaVWVoWTkwdXZQV0YtVy1EYy0xYzJ6Q2Vwc1BqR3FKYnNFZk83TjBXdE1QdDh3a2RZYmNiZ1NZdUd6Q2R3akttNnk3dGhaOXNUeVJJV0hEMGFIc2tQOE4wQVlqa0k0cWNvUWZOZEdmTmpkaDhfRkxsVFJDaEpqRks5Vg?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxNNmM1ZzlMd1F4THI0VHI3LVA0c0hUU2xEX3A1dUxSMzFyeFcwUzNmNVhIRWhpbGl1SXN3N184NDhoR0hNRzNLWWNmM3hSeGVUMXhwRndCeXVlVnE5bDVxcGFYV0pjS0M0a1dDdTRHeFQyNDZSVllXVWpTUUdEUzJLZHQzU2tuc2gwaVd5UWx3?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxORTZKTGNsM29zVEpQbW4ySjVRZ0pGN0VOVG9aNjdqaWpPUDJpaEQ0MHVqVENLdV9hU1ZLaXFDcFVsNk9CSE50M2hzY1Q1V0xHRDR0dTNEd2JqdXBVOUhodlI5Sl91TndCbnh3aVAzZk0xLUdLZmRtU3NwcGl2cFF6cmVMdVQ0MDlWNlQ0UXN0a3A?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNVVh1Z1RmUDEwd3JUV3J0V3VqeGVGaks0RGVhMVFjcDFveEVQX0xuQjhrbTNoazVzZVhFNGJUR3FlNTZUUG5xWmduaTVfQWF4akYzbEItc1BRYXlfb1N6TG5xaXZfcmlKUGJJOWJCbE9felhCd3ZRRUNtSGhDU2dpRnl1Q1lGZHBYVlh1RXotNA?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQWnRVYXd1cHFIVFZhTkt6YVB0RGdmMXIwMUtWTzdrLVhLZTRsLUw3RkpWak0wUmpVb3oxSjg2dV9zdThzekFTRUVVazYwWTJqTl9WejFfck5aeUpLd05oN2Rjc25SWEVuREFEVVdjdExycC00Zm5va040dm9iUS1kenVzNHR2NER6X1kwSFlJVHFzWGxtUWk5Q19OV3pDQkFXR21CMnZkbDBPRS1wYXU4?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQSm1sdVlfVVg2ZEZHTU9PNTl3UmdFb21SRHZGaV9YdTFXWXczdDlONkZkVEE1QXJYcjBPU0FXWF9QSHBWbjc5ek04X3F3WE5hQzBuUFFvXzAzbF8xQWpiTFpIOFF6WjhTN2Qzb0RHa2tHZkZGS1RnM25LWENCTFlLNjNVQlRYOWF1Y0FjZUZfbjl0UGpLX1BKbFJkMXM3TGZmaGs3Umw1UHZCX3RYdEdueQ?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxOcnppenhTdFVSVFY2VDNPWnBIbE9ralhlWE1rYk83NmMzOUZVMGZHSXMxSTdSaWNEbkJhSXpRaGo4Sy0tVGwxU3YwSjhMcmdQbGZPVlEyXzBBY3l5cUxXa2tWNHlGa2xOUWdmRE83NjZveThvb2xBNThKTDBjcGVaRnFGeW9mMW5NZlRyQV80THJGUWQyRm5TMFBVUU9Lay03RlRvRmhFdnN2dTRwYjNJMXR4d0JFcXFN?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxQdWRfSklGakphaGhZZGRVaFZkblJuOVR4UlBJRXNoQjVHSXV3ODQtbW5yUHpSQWNnMk1pMDIxSkc5cXA0THBONUREa3BleWJNLThhNFpELWlGVUpidXNWUE5haVhCMkdEQUJGSnJvZGFnalRMYzFCaU1JWVpURjh0a0lVWnNBX3FmejdDMHhqc2hieFlkcC1idnItNzBsSUM1NzBjMk1SUE5GbzNLT0VCZG5SRzFjdW9fcEZaUzZzUnl6RnNSejV2RkpVbl9GR2RyU01Fek44UzM3VERRY1Q5emtVZ3Y5MzBsaTlB?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNQWV5aHNUNlVtV1ItQkpyRDkyc2dUSTFtSHp1THl3cEZzT0dqaTcxakFIUjZ2eEJ0ZVNSN1lJQzdzLXVVcTJyc2dnNjZlWUNIS0loQzdBXzRfUFBQaW83bTAyVEtYOVhjVVUxZ2FaX0l0djNFN25ZR2RPdnVkdElLcTVMRnZ3WWxUVkhEMw?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxQeng0TGVnR1BPRG5ENFZNNE1OX2JaTmlOMTFKNlBqcVhtaHF3aWRtaGVuQXZWUjItUG43T1RBWEtTaElFbXVuVURaem1tWmlwaWlRTHBlcGJGdmhYU3VzMTdDLU5oakdwUFVsU1EyYjFRMl9zSDh6QmpBdjFDcVUtT1pvZw?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxONGNNMV9xVGhZcUlCa0VIWEI1S1ZPZFY4R05nbGNURHNOb294YldzYVRGUEVYMXpRd19STWsxWGNfQ0xNZ2p6clZ1Q1dpYmVna0NJOG0tVU00NVVQRDc3dlFISS1VSGlnQWhWS2NZanRLV3o0Z2hERGZ2TVl1X2plbjQwYk1oU0dUcnc?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxQWXpxbTB2bHJBZ2otVXJ3TUN5TFRza0l0OXZmd3BKUFZFQkdFMGgwM2FSa25xeVliNzZWa1R2MmpncGw0MTlnUjNxanhrSVZTNjBwcGh5NFJuWnBSc1NSV3lOSXJncEl1aXJyY0xMWUdPZTQwN2hDcjZFSU5VcTNUN0llWXBVOWV5RUtYU3daSGNFUzhSTUR6NGJvcGhtakFjU2xuMA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
