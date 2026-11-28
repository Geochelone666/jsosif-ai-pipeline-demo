# PFE Intelligence Report

- ticker: **PFE**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/PFE/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PFE/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:30:38.211316+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 8, 'rule': 2, 'ai': 3, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/PFE** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 8 unique headlines; 5 named publishers; 0 exact duplicates; 8 HTTPS source links; largest publisher share 37.5%; oldest publication 2026-11-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 28.5200 |
| Return 1D (%) | 0.2108 |
| Return 1W (%) | 4.0876 |
| Return 1M (%) | -2.8979 |
| Return YTD (%) | 22.2087 |
| Return 1Y (%) | 18.3585 |
| Annualized volatility (%) | 21.1486 |
| Beta vs SPY | 0.2157 |
| Max drawdown (%) | -15.7243 |
| Sharpe (rf=0) | 0.9032 |
| Downside deviation (rf=0, %) | 13.9319 |
| Sortino (rf=0) | 1.3710 |
| Historical VaR 95% (1D, %) | 2.0205 |
| Historical ES 95% (1D, %) | 2.6076 |
| Correlation vs SPY | 0.1532 |
| Tracking error vs SPY (%) | 23.9910 |
| P/E (trailing) | 40.74 |
| P/B | 1.83 |
| EV/EBITDA | 8.50 |
| Revenue growth (%) | -0.40 |
| Forward P/E (estimate) | 9.65 |
| Gross margin (%) | 74.90 |
| Operating margin (%) | 29.07 |
| Return on equity (%) | 4.47 |
| Free cash flow yield (%) | 8.00 |
| MA50 | 28.5778 |
| Close vs MA50 (%) | -0.2023 |
| MA200 | 26.3114 |
| Close vs MA200 (%) | 8.3939 |
| RSI (14, Wilder) | 48.8087 |
| MACD (12,26) | -0.2081 |
| MACD signal (9) | -0.1121 |
| MACD histogram | -0.0961 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PFE': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 28.5200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.2108 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.0876 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -2.8979 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 22.2087 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 18.3585 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.1486 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.9319 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3710 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0205 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6076 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1532 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.9910 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2157 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.7243 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9032 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 9.6544 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.8980 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 29.0660 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 4.4680 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 8.0014 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 40.7429 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 48.8087 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0961 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.2023 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 8.3939 -> Clearly above the moving-average trend level.

## TAILWINDS

### Pfizer Inc Stock (PFE) Moved Up by 4.18% on Nov 24: What Investors Need To Know
- Summary: Pfizer Inc Stock (PFE) Moved Up by 4.18% on Nov 24: What Investors Need To Know
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPdjV4N1Z5RE5fUXNZSHFtdU5hSmNFekoyaWF3enpaTDhKelpKQmd1b1VMeGtQdEp4VTFiYUc1VGI4QWE3bWZxaWduc2F5SWFoUHRRR2F4b1FZQmlJeFQ3MWxleFpadDRyQkNhbTRUVWI0MlhYaVB2eUI5NGVJcFoyYWIzYW43eDBkR2c?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Pfizer (PFE) Stock Looks Stretched Even With New Pipeline Deals
- Summary: Pfizer (PFE) Stock Looks Stretched Even With New Pipeline Deals
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxQY2I0dk1icDR1OTRESTZSMTU3TmV4M3U4ejRnTWQwdlZKck5jWUxOZElpb0NoYWRuYzd2WHhWUmxjYUpPTjlHY3JyYVZiel9ZbnVXVk1WSVRIek9oT3hINk03ZmZITEtZUEdUd2U3d3Flc0hfMUpRcVdhYXlQZ3AxenZZM2pZTmJuUzlObk5JcW5pN3VSTlQzMTdxajVDMmg4alVhOGV1YUVVTGVFY3JXMmdHSkw2YVFhQUFWVWFOaDVuQ2U1ZllPS2tIT1FzRmd2bkYw0gHYAUFVX3lxTFBIOGFBaUVHS1BVTTJIVF8zOG9SMTY1ZDJwNkp2NEp5YThWdWFWdFNIUkpyTmZrLUtwb1ZIV2M0VVo4NlQ4d1lKUWNSMDhrcnNObTF2Z0pvUkdDa2Z3NG4zRXRydkM5OWU0ZGdHbVNyeXVvdTR3U0diT2NEVDRnR2FsMVFRRnFqZk1DX3lRU19MSmQzZy1nNzRtSU1rVm1hR3hZTktMTGdVa3lJZUNDWTh2VDVEVGtWTVhzUV9RUFB0UFNJQ3FfbVZtdXVCOElwN2U4eUNaci0tQQ?oc=5>

### Pfizer (PFE) Stock Could Be Above Fair Value Despite Fresh CAR T Deal
- Summary: Pfizer’s recent CAR T deal may boost valuation, but market remains uncertain about long-term impact.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNX1RKa3dIWHBNQk04YXZOTkthd3dLeTlDUnVSMVJQdVY0OEZORlA4bGtPWUhnNGpFSEdiMmFlN2Z4NTJVUmJ3WWw1VDN6QnFzTnRDUWFLWklKT2JPTWg4UFdhRU9jbGY1elRLenNFVDRjdGhWeUJwUk1LZTZaWi0xZHh0Q2tpTG1LNEcxMFFQYTFESkR2X0ZpWg?oc=5>

### Does In Vivo CAR T Deal Change The Bull Case For Pfizer (PFE)?
- Summary: Questioning if In Vivo CAR T deal strengthens Pfizer’s bullish outlook.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxQNktqcHdsOHJZV2VuNEk1S0hOazdqNTdMODJnT3hQeGtWak1LTWI1bXZuRzRjdzF4OTRHTno4WldHZGVmV3h6WUFlLXFBeXl5b0JfV0NOU1Y5NWJNTW1mQVZhVXRuZHpwNThNRFY0cnZSSmNkZlY1YVVNZjBpR2JqS0dVNExoV0Rr?oc=5>

### Pfizer (PFE) Signs New CAR T Deal, Is The Stock Undervalued?
- Summary: Pfizer announces a new CAR T therapy partnership, potentially boosting its oncology pipeline and shareholder value.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxNQTZnS2VYNEliLTUwOVZXeXIxWVZiUWFPdmw0UkFBNXBlR3VTM3kwNERFNjJBMVhMLTBJQjJkTWkzNW1PVU51MjVCTkhxTGdjX1o4QWVlY0w2MDNwMzVBUzUyQnl3RlZsZjRxQTNMdGtYU3JmdlBtOGtod2RJaTZaNWRzeG1sS3NhQnBJNkROR0JPc01QY2dlc2daalJCcmFud05QOWZMdWF3eXQzZlBuS2JwbVF0VHo0cThuNFE2NF83azRfdXV5N3JrbXNQUdIB0wFBVV95cUxPdVlHR0Y1QlJZczc1aVlEWDA2Q05rZlNZVjhWb1ZvMkpfZ1BrQzU4UkRUUkJYRmlTTXJPXzg1Ykk1Y2E1eXlBeTJ1NE1xMlAwTmpRSG1WeVhkLWpDaFZsUDZ5M3MtVlJBRnp2Sk1XZk5CSzZpcmVPNlFwd1J2UXhPT2hDQXI5Ym96ZnJ4X1lpQldrRXRYcVlGdUlDanVyYm5WMXBlZGg0ckxCMDdNd3VOY2NMdHN4c2NvVldQXy00ZmNCVTYxbzdZcjdFXzBJSDNmemln?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PFE** | **40.74** | **1.83** | **8.50** | **-0.40** | **162,559,836,160.00 USD** | **18.36** |
| MRK | 142.75 | 7.77 | 13.31 | 4.70 | 348,388,524,032.00 USD | 39.03 |
| JNJ | 41.81 | 8.13 | 20.02 | 5.90 | 663,238,082,560.00 USD | 35.55 |
| LLY | 45.19 | 30.81 | 27.64 | 38.60 | 1,240,255,561,728.00 USD | 26.85 |

Peers fetched as_of: 2026-11-27; PFE reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 16,583,000,000.00 USD; period 2026-06-29/2026-09-27; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,242,000,000.00 USD; period 2026-06-29/2026-09-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/78003/000007800326000127/pfe-20260927.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiigFBVV95cUxPdjV4N1Z5RE5fUXNZSHFtdU5hSmNFekoyaWF3enpaTDhKelpKQmd1b1VMeGtQdEp4VTFiYUc1VGI4QWE3bWZxaWduc2F5SWFoUHRRR2F4b1FZQmlJeFQ3MWxleFpadDRyQkNhbTRUVWI0MlhYaVB2eUI5NGVJcFoyYWIzYW43eDBkR2c?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQY2I0dk1icDR1OTRESTZSMTU3TmV4M3U4ejRnTWQwdlZKck5jWUxOZElpb0NoYWRuYzd2WHhWUmxjYUpPTjlHY3JyYVZiel9ZbnVXVk1WSVRIek9oT3hINk03ZmZITEtZUEdUd2U3d3Flc0hfMUpRcVdhYXlQZ3AxenZZM2pZTmJuUzlObk5JcW5pN3VSTlQzMTdxajVDMmg4alVhOGV1YUVVTGVFY3JXMmdHSkw2YVFhQUFWVWFOaDVuQ2U1ZllPS2tIT1FzRmd2bkYw0gHYAUFVX3lxTFBIOGFBaUVHS1BVTTJIVF8zOG9SMTY1ZDJwNkp2NEp5YThWdWFWdFNIUkpyTmZrLUtwb1ZIV2M0VVo4NlQ4d1lKUWNSMDhrcnNObTF2Z0pvUkdDa2Z3NG4zRXRydkM5OWU0ZGdHbVNyeXVvdTR3U0diT2NEVDRnR2FsMVFRRnFqZk1DX3lRU19MSmQzZy1nNzRtSU1rVm1hR3hZTktMTGdVa3lJZUNDWTh2VDVEVGtWTVhzUV9RUFB0UFNJQ3FfbVZtdXVCOElwN2U4eUNaci0tQQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNX1RKa3dIWHBNQk04YXZOTkthd3dLeTlDUnVSMVJQdVY0OEZORlA4bGtPWUhnNGpFSEdiMmFlN2Z4NTJVUmJ3WWw1VDN6QnFzTnRDUWFLWklKT2JPTWg4UFdhRU9jbGY1elRLenNFVDRjdGhWeUJwUk1LZTZaWi0xZHh0Q2tpTG1LNEcxMFFQYTFESkR2X0ZpWg?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxQNktqcHdsOHJZV2VuNEk1S0hOazdqNTdMODJnT3hQeGtWak1LTWI1bXZuRzRjdzF4OTRHTno4WldHZGVmV3h6WUFlLXFBeXl5b0JfV0NOU1Y5NWJNTW1mQVZhVXRuZHpwNThNRFY0cnZSSmNkZlY1YVVNZjBpR2JqS0dVNExoV0Rr?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxNQTZnS2VYNEliLTUwOVZXeXIxWVZiUWFPdmw0UkFBNXBlR3VTM3kwNERFNjJBMVhMLTBJQjJkTWkzNW1PVU51MjVCTkhxTGdjX1o4QWVlY0w2MDNwMzVBUzUyQnl3RlZsZjRxQTNMdGtYU3JmdlBtOGtod2RJaTZaNWRzeG1sS3NhQnBJNkROR0JPc01QY2dlc2daalJCcmFud05QOWZMdWF3eXQzZlBuS2JwbVF0VHo0cThuNFE2NF83azRfdXV5N3JrbXNQUdIB0wFBVV95cUxPdVlHR0Y1QlJZczc1aVlEWDA2Q05rZlNZVjhWb1ZvMkpfZ1BrQzU4UkRUUkJYRmlTTXJPXzg1Ykk1Y2E1eXlBeTJ1NE1xMlAwTmpRSG1WeVhkLWpDaFZsUDZ5M3MtVlJBRnp2Sk1XZk5CSzZpcmVPNlFwd1J2UXhPT2hDQXI5Ym96ZnJ4X1lpQldrRXRYcVlGdUlDanVyYm5WMXBlZGg0ckxCMDdNd3VOY2NMdHN4c2NvVldQXy00ZmNCVTYxbzdZcjdFXzBJSDNmemln?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
