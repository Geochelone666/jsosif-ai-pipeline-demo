# PFE Intelligence Report

- ticker: **PFE**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-19**
- Quant sources: https://finance.yahoo.com/quote/PFE/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PFE/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T05:51:28.227930+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 7, 'rule': 3, 'ai': 2, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261118T054934Z-e0d070d9/PFE** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 7 unique headlines; 5 named publishers; 0 exact duplicates; 7 HTTPS source links; largest publisher share 42.86%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 27.5400 |
| Return 1D (%) | -1.8532 |
| Return 1W (%) | -4.4745 |
| Return 1M (%) | -5.0879 |
| Return YTD (%) | 18.0094 |
| Return 1Y (%) | 18.1043 |
| Annualized volatility (%) | 21.1018 |
| Beta vs SPY | 0.2933 |
| Max drawdown (%) | -15.7243 |
| Sharpe (rf=0) | 0.8969 |
| Downside deviation (rf=0, %) | 14.0287 |
| Sortino (rf=0) | 1.3491 |
| Historical VaR 95% (1D, %) | 2.0151 |
| Historical ES 95% (1D, %) | 2.6076 |
| Correlation vs SPY | 0.1932 |
| Tracking error vs SPY (%) | 22.9161 |
| P/E (trailing) | 39.34 |
| P/B | 1.76 |
| EV/EBITDA | 8.28 |
| Revenue growth (%) | -0.40 |
| Forward P/E (estimate) | 9.32 |
| Gross margin (%) | 74.90 |
| Operating margin (%) | 29.07 |
| Return on equity (%) | 4.47 |
| Free cash flow yield (%) | 8.29 |
| MA50 | 28.4951 |
| Close vs MA50 (%) | -3.3517 |
| MA200 | 26.2587 |
| Close vs MA200 (%) | 4.8795 |
| RSI (14, Wilder) | 34.8629 |
| MACD (12,26) | -0.1216 |
| MACD signal (9) | 0.1494 |
| MACD histogram | -0.2710 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PFE': 286, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 27.5400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.8532 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.4745 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -5.0879 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 18.0094 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 18.1043 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.1018 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.0287 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3491 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0151 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6076 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1932 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 22.9161 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2933 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.7243 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8969 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 9.3227 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.8980 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 29.0660 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 4.4680 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 8.2861 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 39.3429 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 34.8629 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.2710 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.3517 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 4.8795 -> Slightly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### One Unsettled Question Sits Under Pfizer Stock
- Summary: An unresolved issue affecting Pfizer's stock performance.
- Date: 2026-11-16 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPYS11dW5CTEV0WUNZbU8xQUZ3ZWR4R1ozRkh0VGpSMVB2eURRYmYxMnV0MEFxTEdKMVFqUWoweWZiNW52bVVlcGsyeVVOQ1p6cGxmQ2k1UTJvUGRBUkFtU0RjdHNFSmZJb25jZTdGcjN1YUdGSjV2ak5NR0JTSjNDVmcxMW5DYXQ2VkRicU1uTzNLSW5STmFFQ054WWtqTkNwaWVJTU15N3JaUQ?oc=5>

## CATALYSTS

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

## RISKS

### Pfizer: The Patent Cliff Fears Are Overblown (NYSE:PFE)
- Summary: Pfizer argues patent cliff concerns are exaggerated, suggesting continued revenue stability.
- Date: 2026-11-18 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPcTdLUVhqTlNQajY0aGl2UGNxTl9RYldsRE9OMzNVNU5peVV4RDJ0LV9WYzVNR2dHTmd2bXpYM1BHZHhpQmhxemVJMU9mX01nUzBmMmhGMlVmNGVsUTh5Z1JiT1FxdXBaaDZrOVNNQ0lXWWM5QThtc3lUWE0zVmRBWWFSalItcF9NUDFqSw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PFE** | **39.34** | **1.76** | **8.28** | **-0.40** | **156,973,973,504.00 USD** | **18.10** |
| MRK | 134.15 | 7.30 | 12.60 | 4.70 | 327,409,270,784.00 USD | 43.83 |
| JNJ | 40.54 | 7.89 | 19.43 | 5.90 | 643,088,908,288.00 USD | 34.89 |
| LLY | 43.85 | 29.90 | 26.85 | 38.60 | 1,203,503,366,144.00 USD | 29.51 |

Peers fetched as_of: 2026-11-19; PFE reuses existing data (market data as_of: 2026-11-19); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

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
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 16,583,000,000.00 USD; period 2026-06-29/2026-09-27; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,242,000,000.00 USD; period 2026-06-29/2026-09-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/78003/000007800326000127/pfe-20260927.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPYS11dW5CTEV0WUNZbU8xQUZ3ZWR4R1ozRkh0VGpSMVB2eURRYmYxMnV0MEFxTEdKMVFqUWoweWZiNW52bVVlcGsyeVVOQ1p6cGxmQ2k1UTJvUGRBUkFtU0RjdHNFSmZJb25jZTdGcjN1YUdGSjV2ak5NR0JTSjNDVmcxMW5DYXQ2VkRicU1uTzNLSW5STmFFQ054WWtqTkNwaWVJTU15N3JaUQ?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNRVVpbGxXOWhFWUFlXzJEc0FKUHJ2TTVDVDVUTFNMaUV6OThnb2k4TGNQRUROLU5QT2NqaWxJbUFfeFo5bUFvNm1fQnNsX0hjSVRab3NYU3paUzNyVkhidnkxNXNfMkY0UUh2a3N1Y1VlTDcybWpyTHNKTEpfR0oyb2ZVckpNMnA0N0h0SzNLbmJvYkdnQzNETVNRYThxeF9XZzd1eEowcXhTeVZUTjR6VnNDbHFRcl91NTlzbUpRSHBrVWc?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQMEFONURLdjJfUVZSa2hydU95eWp2NlEtU3BaSHl5RWhjemZCbkVCSDNlRERiVnhheHhnT1F1Vk5PRXJyRjZjU1NqMHNOTzhHUE1tbFVLWGtHamUxRi1tWmliM09aVkFOVlZpcU56ZjVxdVBrYWtLai10RnRxQ1g5eGNGSmRSOW1QNmxJRHR0WEVjVF94SFZ0cA?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxQOWdaR1VoajdEU3l1WFJZV1dLaWJpcG0yUTNqYzhnVThkb2FONWZNTnZybkk3d2RHMmRHTG14dEpDaXBEMkNPdFV6andRVVZFcWxxZTFfQ3ZETi1kZVdpVFFJOGlfQ2h0a2hYaWdhY1hqOGdBSDhlRTFuZ0hOLWI1ZXNrN1ZQQWlpOWtwOWRHX3MxbFNZaWw3Y0JtQ1RkMERDYmo0NkJLQjJwSWE2aGhFWkdTclQ?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPcTdLUVhqTlNQajY0aGl2UGNxTl9RYldsRE9OMzNVNU5peVV4RDJ0LV9WYzVNR2dHTmd2bXpYM1BHZHhpQmhxemVJMU9mX01nUzBmMmhGMlVmNGVsUTh5Z1JiT1FxdXBaaDZrOVNNQ0lXWWM5QThtc3lUWE0zVmRBWWFSalItcF9NUDFqSw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
