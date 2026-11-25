# PFE Intelligence Report

- ticker: **PFE**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/PFE/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PFE/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T06:56:27.152295+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 15, 'rule': 3, 'ai': 5, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261123T053847Z-45053549/PFE** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 15 unique headlines; 7 named publishers; 0 exact duplicates; 15 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 28.4600 |
| Return 1D (%) | 3.8686 |
| Return 1W (%) | -0.0351 |
| Return 1M (%) | -3.8443 |
| Return YTD (%) | 21.9516 |
| Return 1Y (%) | 20.4042 |
| Annualized volatility (%) | 21.1924 |
| Beta vs SPY | 0.2232 |
| Max drawdown (%) | -15.7243 |
| Sharpe (rf=0) | 0.9854 |
| Downside deviation (rf=0, %) | 13.9042 |
| Sortino (rf=0) | 1.5018 |
| Historical VaR 95% (1D, %) | 2.0116 |
| Historical ES 95% (1D, %) | 2.6076 |
| Correlation vs SPY | 0.1575 |
| Tracking error vs SPY (%) | 23.9354 |
| P/E (trailing) | 40.66 |
| P/B | 1.82 |
| EV/EBITDA | 8.49 |
| Revenue growth (%) | -0.40 |
| Forward P/E (estimate) | 9.63 |
| Gross margin (%) | 74.90 |
| Operating margin (%) | 29.07 |
| Return on equity (%) | 4.47 |
| Free cash flow yield (%) | 8.02 |
| MA50 | 28.5244 |
| Close vs MA50 (%) | -0.2256 |
| MA200 | 26.2902 |
| Close vs MA200 (%) | 8.2532 |
| RSI (14, Wilder) | 48.0824 |
| MACD (12,26) | -0.2629 |
| MACD signal (9) | -0.0510 |
| MACD histogram | -0.2119 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PFE': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 28.4600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 3.8686 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.0351 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -3.8443 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 21.9516 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 20.4042 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.1924 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.9042 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.5018 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0116 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6076 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1575 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.9354 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2232 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.7243 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9854 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 9.6341 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.8980 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 29.0660 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 4.4680 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 8.0182 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 40.6571 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 48.0824 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.2119 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.2256 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 8.2532 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### Pfizer: Struggling To Meet Dividend Beyond 2027
- Summary: Indicates challenges in sustaining dividends past 2027.
- Date: 2026-11-21 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQZUJsbERxaUtiZENJdV83d0VPSEdjcHpDUWpkZC1UNnZlR0w4VnpkV1EtTVFwSV9JdVBBcjV2d2d4R1NKeWJtNlVlS3A2RThtS0tXOVp3Q0RIekstZk9oWXQwN2RBcVVRejRKWXQ0RHFqWk9Ocld5VTNLQ0NjQUZobUpFRXp4Qkl5dEdoT3JuMS0?oc=5>

## CATALYSTS

### Pfizer's Launched and Acquired Drugs Grew 32% in Q3 — and 3 Other Reasons to Buy the Stock Before 2027
- Summary: Pfizer's Launched and Acquired Drugs Grew 32% in Q3 — and 3 Other Reasons to Buy the Stock Before 2027
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxPalVZaXhkalFLX09FdnVUUGhuMGtaQlpaWWZ0clJac041eE50TmpxMlZ5YUx1UHI2UURTUDA4ejU0REs2czNiMjY4MllFd1BacFRua1V5VjBoWjBKOGV3Y19KM2tWZHdZNXFaZE8yTjM0ZVZWQ3lxZlhTYW5CdFZ3Nkt0YW0tWWJsSzlMMDZoU0Zvc1ctbGNsSDR0RmRQWXVUYnZwa3hzckFpRmRETHJKXzZkZDk3TEF2MmlCT3BPNFY4VzBKSnh3Y05zaFI5d0V1QkVfSWd1YWY?oc=5>

### Pfizer (PFE) Stock Looks Stretched Even With New Pipeline Deals
- Summary: Pfizer (PFE) Stock Looks Stretched Even With New Pipeline Deals
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxQY2I0dk1icDR1OTRESTZSMTU3TmV4M3U4ejRnTWQwdlZKck5jWUxOZElpb0NoYWRuYzd2WHhWUmxjYUpPTjlHY3JyYVZiel9ZbnVXVk1WSVRIek9oT3hINk03ZmZITEtZUEdUd2U3d3Flc0hfMUpRcVdhYXlQZ3AxenZZM2pZTmJuUzlObk5JcW5pN3VSTlQzMTdxajVDMmg4alVhOGV1YUVVTGVFY3JXMmdHSkw2YVFhQUFWVWFOaDVuQ2U1ZllPS2tIT1FzRmd2bkYw0gHYAUFVX3lxTFBIOGFBaUVHS1BVTTJIVF8zOG9SMTY1ZDJwNkp2NEp5YThWdWFWdFNIUkpyTmZrLUtwb1ZIV2M0VVo4NlQ4d1lKUWNSMDhrcnNObTF2Z0pvUkdDa2Z3NG4zRXRydkM5OWU0ZGdHbVNyeXVvdTR3U0diT2NEVDRnR2FsMVFRRnFqZk1DX3lRU19MSmQzZy1nNzRtSU1rVm1hR3hZTktMTGdVa3lJZUNDWTh2VDVEVGtWTVhzUV9RUFB0UFNJQ3FfbVZtdXVCOElwN2U4eUNaci0tQQ?oc=5>

### PFE Inks $2.6B Licensing Deal With Chinese Biotech for CAR-T Therapies
- Summary: PFE Inks $2.6B Licensing Deal With Chinese Biotech for CAR-T Therapies
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxNRVVpbGxXOWhFWUFlXzJEc0FKUHJ2TTVDVDVUTFNMaUV6OThnb2k4TGNQRUROLU5QT2NqaWxJbUFfeFo5bUFvNm1fQnNsX0hjSVRab3NYU3paUzNyVkhidnkxNXNfMkY0UUh2a3N1Y1VlTDcybWpyTHNKTEpfR0oyb2ZVckpNMnA0N0h0SzNLbmJvYkdnQzNETVNRYThxeF9XZzd1eEowcXhTeVZUTjR6VnNDbHFRcl91NTlzbUpRSHBrVWc?oc=5>

### What Do Pfizer (PFE) Investors Need To Know About The New Patent Lawsuits?
- Summary: Pfizer faces new patent lawsuits that could impact its revenue streams and market position.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQU2VCRkFvXzhPWEVMeDZhSnRLRkJqVmplcUdFT3Y5TzlyWTQwYldfZXpNOW01RFZ2WHdJTHRsby13akxha3JEQml0R01TbmpQeW1xY1A0ZEJuaVZmc3pGSXpaVUU3dEptR2NPYXNmNUtjTE0zMEY4N0RPV2VjaS1DVXVCd1dlMmphRHUwaGF1NDNJTGpIbTZrdw?oc=5>

### Pfizer, Inc. (PFE) Stock Forecasts
- Summary: Analysts provide stock price forecasts for Pfizer, indicating potential upside or downside for investors.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxOeXRUUmpOMTJHZUJCMjdDV3d5d0xreV9qZzY4Z0xKazNlQUZ3ZWJfdHpLSHNQZ0E4UXktYjNfRjJ5dWh3aXpxamxGRERTbWM5MVBuMDY3b1FBdFRhNXh6alNSWTRyNEZSODFMYy1kYWZBcW52WWN3UUZzNWNrU1o0UndqQWdrYk1VbE5ybw?oc=5>

### Pfizer (PFE) Signs New CAR T Deal, Is The Stock Undervalued?
- Summary: Pfizer signs a new CAR T partnership, potentially boosting its oncology portfolio and shareholder value.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxNQTZnS2VYNEliLTUwOVZXeXIxWVZiUWFPdmw0UkFBNXBlR3VTM3kwNERFNjJBMVhMLTBJQjJkTWkzNW1PVU51MjVCTkhxTGdjX1o4QWVlY0w2MDNwMzVBUzUyQnl3RlZsZjRxQTNMdGtYU3JmdlBtOGtod2RJaTZaNWRzeG1sS3NhQnBJNkROR0JPc01QY2dlc2daalJCcmFud05QOWZMdWF3eXQzZlBuS2JwbVF0VHo0cThuNFE2NF83azRfdXV5N3JrbXNQUdIB0wFBVV95cUxPdVlHR0Y1QlJZczc1aVlEWDA2Q05rZlNZVjhWb1ZvMkpfZ1BrQzU4UkRUUkJYRmlTTXJPXzg1Ykk1Y2E1eXlBeTJ1NE1xMlAwTmpRSG1WeVhkLWpDaFZsUDZ5M3MtVlJBRnp2Sk1XZk5CSzZpcmVPNlFwd1J2UXhPT2hDQXI5Ym96ZnJ4X1lpQldrRXRYcVlGdUlDanVyYm5WMXBlZGg0ckxCMDdNd3VOY2NMdHN4c2NvVldQXy00ZmNCVTYxbzdZcjdFXzBJSDNmemln?oc=5>

## RISKS

### Pfizer: The Patent Cliff Fears Are Overblown (NYSE:PFE)
- Summary: Pfizer argues patent cliff concerns are exaggerated, suggesting continued revenue stability.
- Date: 2026-11-18 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPcTdLUVhqTlNQajY0aGl2UGNxTl9RYldsRE9OMzNVNU5peVV4RDJ0LV9WYzVNR2dHTmd2bXpYM1BHZHhpQmhxemVJMU9mX01nUzBmMmhGMlVmNGVsUTh5Z1JiT1FxdXBaaDZrOVNNQ0lXWWM5QThtc3lUWE0zVmRBWWFSalItcF9NUDFqSw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PFE** | **40.66** | **1.82** | **8.49** | **-0.40** | **162,217,836,544.00 USD** | **20.40** |
| MRK | 143.00 | 7.78 | 13.34 | 4.70 | 349,004,857,344.00 USD | 45.15 |
| JNJ | 41.95 | 8.16 | 20.08 | 5.90 | 665,525,026,816.00 USD | 37.88 |
| LLY | 45.69 | 31.15 | 27.93 | 38.60 | 1,253,803,819,008.00 USD | 32.33 |

Peers fetched as_of: 2026-11-24; PFE reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

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

- https://news.google.com/rss/articles/CBMikAFBVV95cUxQZUJsbERxaUtiZENJdV83d0VPSEdjcHpDUWpkZC1UNnZlR0w4VnpkV1EtTVFwSV9JdVBBcjV2d2d4R1NKeWJtNlVlS3A2RThtS0tXOVp3Q0RIekstZk9oWXQwN2RBcVVRejRKWXQ0RHFqWk9Ocld5VTNLQ0NjQUZobUpFRXp4Qkl5dEdoT3JuMS0?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxPalVZaXhkalFLX09FdnVUUGhuMGtaQlpaWWZ0clJac041eE50TmpxMlZ5YUx1UHI2UURTUDA4ejU0REs2czNiMjY4MllFd1BacFRua1V5VjBoWjBKOGV3Y19KM2tWZHdZNXFaZE8yTjM0ZVZWQ3lxZlhTYW5CdFZ3Nkt0YW0tWWJsSzlMMDZoU0Zvc1ctbGNsSDR0RmRQWXVUYnZwa3hzckFpRmRETHJKXzZkZDk3TEF2MmlCT3BPNFY4VzBKSnh3Y05zaFI5d0V1QkVfSWd1YWY?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQY2I0dk1icDR1OTRESTZSMTU3TmV4M3U4ejRnTWQwdlZKck5jWUxOZElpb0NoYWRuYzd2WHhWUmxjYUpPTjlHY3JyYVZiel9ZbnVXVk1WSVRIek9oT3hINk03ZmZITEtZUEdUd2U3d3Flc0hfMUpRcVdhYXlQZ3AxenZZM2pZTmJuUzlObk5JcW5pN3VSTlQzMTdxajVDMmg4alVhOGV1YUVVTGVFY3JXMmdHSkw2YVFhQUFWVWFOaDVuQ2U1ZllPS2tIT1FzRmd2bkYw0gHYAUFVX3lxTFBIOGFBaUVHS1BVTTJIVF8zOG9SMTY1ZDJwNkp2NEp5YThWdWFWdFNIUkpyTmZrLUtwb1ZIV2M0VVo4NlQ4d1lKUWNSMDhrcnNObTF2Z0pvUkdDa2Z3NG4zRXRydkM5OWU0ZGdHbVNyeXVvdTR3U0diT2NEVDRnR2FsMVFRRnFqZk1DX3lRU19MSmQzZy1nNzRtSU1rVm1hR3hZTktMTGdVa3lJZUNDWTh2VDVEVGtWTVhzUV9RUFB0UFNJQ3FfbVZtdXVCOElwN2U4eUNaci0tQQ?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNRVVpbGxXOWhFWUFlXzJEc0FKUHJ2TTVDVDVUTFNMaUV6OThnb2k4TGNQRUROLU5QT2NqaWxJbUFfeFo5bUFvNm1fQnNsX0hjSVRab3NYU3paUzNyVkhidnkxNXNfMkY0UUh2a3N1Y1VlTDcybWpyTHNKTEpfR0oyb2ZVckpNMnA0N0h0SzNLbmJvYkdnQzNETVNRYThxeF9XZzd1eEowcXhTeVZUTjR6VnNDbHFRcl91NTlzbUpRSHBrVWc?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQU2VCRkFvXzhPWEVMeDZhSnRLRkJqVmplcUdFT3Y5TzlyWTQwYldfZXpNOW01RFZ2WHdJTHRsby13akxha3JEQml0R01TbmpQeW1xY1A0ZEJuaVZmc3pGSXpaVUU3dEptR2NPYXNmNUtjTE0zMEY4N0RPV2VjaS1DVXVCd1dlMmphRHUwaGF1NDNJTGpIbTZrdw?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxOeXRUUmpOMTJHZUJCMjdDV3d5d0xreV9qZzY4Z0xKazNlQUZ3ZWJfdHpLSHNQZ0E4UXktYjNfRjJ5dWh3aXpxamxGRERTbWM5MVBuMDY3b1FBdFRhNXh6alNSWTRyNEZSODFMYy1kYWZBcW52WWN3UUZzNWNrU1o0UndqQWdrYk1VbE5ybw?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxNQTZnS2VYNEliLTUwOVZXeXIxWVZiUWFPdmw0UkFBNXBlR3VTM3kwNERFNjJBMVhMLTBJQjJkTWkzNW1PVU51MjVCTkhxTGdjX1o4QWVlY0w2MDNwMzVBUzUyQnl3RlZsZjRxQTNMdGtYU3JmdlBtOGtod2RJaTZaNWRzeG1sS3NhQnBJNkROR0JPc01QY2dlc2daalJCcmFud05QOWZMdWF3eXQzZlBuS2JwbVF0VHo0cThuNFE2NF83azRfdXV5N3JrbXNQUdIB0wFBVV95cUxPdVlHR0Y1QlJZczc1aVlEWDA2Q05rZlNZVjhWb1ZvMkpfZ1BrQzU4UkRUUkJYRmlTTXJPXzg1Ykk1Y2E1eXlBeTJ1NE1xMlAwTmpRSG1WeVhkLWpDaFZsUDZ5M3MtVlJBRnp2Sk1XZk5CSzZpcmVPNlFwd1J2UXhPT2hDQXI5Ym96ZnJ4X1lpQldrRXRYcVlGdUlDanVyYm5WMXBlZGg0ckxCMDdNd3VOY2NMdHN4c2NvVldQXy00ZmNCVTYxbzdZcjdFXzBJSDNmemln?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPcTdLUVhqTlNQajY0aGl2UGNxTl9RYldsRE9OMzNVNU5peVV4RDJ0LV9WYzVNR2dHTmd2bXpYM1BHZHhpQmhxemVJMU9mX01nUzBmMmhGMlVmNGVsUTh5Z1JiT1FxdXBaaDZrOVNNQ0lXWWM5QThtc3lUWE0zVmRBWWFSalItcF9NUDFqSw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
