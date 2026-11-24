# PFE Intelligence Report

- ticker: **PFE**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/PFE/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PFE/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:22:26.942738+00:00**
- AI status: **Partial: 1 headline remains unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 16, 'rule': 5, 'ai': 3, 'unknown': 1, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261123T053847Z-45053549/PFE** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 16 unique headlines; 10 named publishers; 0 exact duplicates; 16 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 27.4000 |
| Return 1D (%) | 0.0000 |
| Return 1W (%) | -5.0589 |
| Return 1M (%) | -7.4257 |
| Return YTD (%) | 17.4095 |
| Return 1Y (%) | 16.7530 |
| Annualized volatility (%) | 20.8892 |
| Beta vs SPY | 0.2325 |
| Max drawdown (%) | -15.7243 |
| Sharpe (rf=0) | 0.8170 |
| Downside deviation (rf=0, %) | 13.9320 |
| Sortino (rf=0) | 1.2250 |
| Historical VaR 95% (1D, %) | 2.0205 |
| Historical ES 95% (1D, %) | 2.6076 |
| Correlation vs SPY | 0.1667 |
| Tracking error vs SPY (%) | 23.5868 |
| P/E (trailing) | 39.14 |
| P/B | 1.75 |
| EV/EBITDA | 8.24 |
| Revenue growth (%) | -0.40 |
| Forward P/E (estimate) | 9.28 |
| Gross margin (%) | 74.90 |
| Operating margin (%) | 29.07 |
| Return on equity (%) | 4.47 |
| Free cash flow yield (%) | 8.33 |
| MA50 | 28.4982 |
| Close vs MA50 (%) | -3.8537 |
| MA200 | 26.2768 |
| Close vs MA200 (%) | 4.2745 |
| RSI (14, Wilder) | 33.7682 |
| MACD (12,26) | -0.2929 |
| MACD signal (9) | 0.0020 |
| MACD histogram | -0.2949 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PFE': 288, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 27.4000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.0000 -> Unchanged adjusted price over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -5.0589 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -7.4257 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 17.4095 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 16.7530 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 20.8892 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.9320 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.2250 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0205 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6076 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1667 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.5868 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2325 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.7243 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8170 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 9.2753 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.8980 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 29.0660 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 4.4680 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 8.3284 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 39.1429 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 33.7682 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.2949 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.8537 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 4.2745 -> Slightly above the moving-average trend level.

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

### Pfizer, Starna ink cell therapy licensing deal worth up to $2.6B
- Summary: Pfizer, Starna ink cell therapy licensing deal worth up to $2.6B
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQMEFONURLdjJfUVZSa2hydU95eWp2NlEtU3BaSHl5RWhjemZCbkVCSDNlRERiVnhheHhnT1F1Vk5PRXJyRjZjU1NqMHNOTzhHUE1tbFVLWGtHamUxRi1tWmliM09aVkFOVlZpcU56ZjVxdVBrYWtLai10RnRxQ1g5eGNGSmRSOW1QNmxJRHR0WEVjVF94SFZ0cA?oc=5>

### Pfizer Enters into Exclusive Licensing Agreement with Starna Therapeutics for Autoimmune Diseases
- Summary: Pfizer Enters into Exclusive Licensing Agreement with Starna Therapeutics for Autoimmune Diseases
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxQOWdaR1VoajdEU3l1WFJZV1dLaWJpcG0yUTNqYzhnVThkb2FONWZNTnZybkk3d2RHMmRHTG14dEpDaXBEMkNPdFV6andRVVZFcWxxZTFfQ3ZETi1kZVdpVFFJOGlfQ2h0a2hYaWdhY1hqOGdBSDhlRTFuZ0hOLWI1ZXNrN1ZQQWlpOWtwOWRHX3MxbFNZaWw3Y0JtQ1RkMERDYmo0NkJLQjJwSWE2aGhFWkdTclQ?oc=5>

### Why Pfizer's $330 Million Deal Could Matter More Than Its Price Tag
- Summary: Pfizer's $330M acquisition could reshape its portfolio and market position.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNQUN2YjdJOGNpb2J2S2xhYmRySlBPV2NxNmJ1b1N3eUNiOXJNOU5RT2NzbGI2NHBFcXZWSDNfSVh2X1d4TFpOQ1FOWVpuUElmNEx1bFZSUVplcGVtRXF3TVI5T3Z0c0tpU3JncDliRjRNNXFTNGVqS1p5T2FYdkZ2bkszODg2YU5fM3oxbEk3cm9kcGZsbE1FeUlabVE0QVVtbnVKNA?oc=5>

## RISKS

### Pfizer: The Patent Cliff Fears Are Overblown (NYSE:PFE)
- Summary: Pfizer argues patent cliff concerns are exaggerated, suggesting continued revenue stability.
- Date: 2026-11-18 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPcTdLUVhqTlNQajY0aGl2UGNxTl9RYldsRE9OMzNVNU5peVV4RDJ0LV9WYzVNR2dHTmd2bXpYM1BHZHhpQmhxemVJMU9mX01nUzBmMmhGMlVmNGVsUTh5Z1JiT1FxdXBaaDZrOVNNQ0lXWWM5QThtc3lUWE0zVmRBWWFSalItcF9NUDFqSw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PFE** | **39.14** | **1.75** | **8.24** | **-0.40** | **156,175,990,784.00 USD** | **16.75** |
| MRK | 136.84 | 7.44 | 12.83 | 4.70 | 333,966,835,712.00 USD | 42.64 |
| JNJ | 40.98 | 7.97 | 19.64 | 5.90 | 650,094,116,864.00 USD | 35.43 |
| LLY | 44.29 | 30.20 | 27.11 | 38.60 | 1,215,510,609,920.00 USD | 29.55 |

Peers fetched as_of: 2026-11-23; PFE reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-23

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
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQMEFONURLdjJfUVZSa2hydU95eWp2NlEtU3BaSHl5RWhjemZCbkVCSDNlRERiVnhheHhnT1F1Vk5PRXJyRjZjU1NqMHNOTzhHUE1tbFVLWGtHamUxRi1tWmliM09aVkFOVlZpcU56ZjVxdVBrYWtLai10RnRxQ1g5eGNGSmRSOW1QNmxJRHR0WEVjVF94SFZ0cA?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxQOWdaR1VoajdEU3l1WFJZV1dLaWJpcG0yUTNqYzhnVThkb2FONWZNTnZybkk3d2RHMmRHTG14dEpDaXBEMkNPdFV6andRVVZFcWxxZTFfQ3ZETi1kZVdpVFFJOGlfQ2h0a2hYaWdhY1hqOGdBSDhlRTFuZ0hOLWI1ZXNrN1ZQQWlpOWtwOWRHX3MxbFNZaWw3Y0JtQ1RkMERDYmo0NkJLQjJwSWE2aGhFWkdTclQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNQUN2YjdJOGNpb2J2S2xhYmRySlBPV2NxNmJ1b1N3eUNiOXJNOU5RT2NzbGI2NHBFcXZWSDNfSVh2X1d4TFpOQ1FOWVpuUElmNEx1bFZSUVplcGVtRXF3TVI5T3Z0c0tpU3JncDliRjRNNXFTNGVqS1p5T2FYdkZ2bkszODg2YU5fM3oxbEk3cm9kcGZsbE1FeUlabVE0QVVtbnVKNA?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPcTdLUVhqTlNQajY0aGl2UGNxTl9RYldsRE9OMzNVNU5peVV4RDJ0LV9WYzVNR2dHTmd2bXpYM1BHZHhpQmhxemVJMU9mX01nUzBmMmhGMlVmNGVsUTh5Z1JiT1FxdXBaaDZrOVNNQ0lXWWM5QThtc3lUWE0zVmRBWWFSalItcF9NUDFqSw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
