# PFE Intelligence Report

- ticker: **PFE**
- Report as_of: **2026-10-28**
- Market data as_of: **2026-10-28**
- Quant sources: https://finance.yahoo.com/quote/PFE/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PFE/key-statistics/
- AI analysis snapshot as_of: **2026-10-28**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-29T02:26:19.811657+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 11, 'rule': 1, 'ai': 6, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261028T015717Z-533e470c/PFE** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **4**; {'directional_claim_without_event_type': 2, 'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 11 unique headlines; 7 named publishers; 0 exact duplicates; 11 HTTPS source links; largest publisher share 36.36%; oldest publication 2026-10-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 29.4500 |
| Return 1D (%) | -1.1745 |
| Return 1W (%) | -1.3400 |
| Return 1M (%) | 2.5418 |
| Return YTD (%) | 24.3777 |
| Return 1Y (%) | 28.6343 |
| Annualized volatility (%) | 21.2171 |
| Beta vs SPY | 0.2413 |
| Max drawdown (%) | -15.7243 |
| Sharpe (rf=0) | 1.2975 |
| Downside deviation (rf=0, %) | 13.6806 |
| Sortino (rf=0) | 2.0123 |
| Historical VaR 95% (1D, %) | 1.9258 |
| Historical ES 95% (1D, %) | 2.5887 |
| Correlation vs SPY | 0.1445 |
| Tracking error vs SPY (%) | 23.1008 |
| P/E (trailing) | 38.75 |
| P/B | 1.97 |
| EV/EBITDA | 8.66 |
| Revenue growth (%) | 2.60 |
| Forward P/E (estimate) | 10.21 |
| Gross margin (%) | 74.72 |
| Operating margin (%) | 27.88 |
| Return on equity (%) | 5.01 |
| Free cash flow yield (%) | 7.44 |
| MA50 | 28.4578 |
| Close vs MA50 (%) | 3.4866 |
| MA200 | 26.2656 |
| Close vs MA200 (%) | 12.1240 |
| RSI (14, Wilder) | 56.5352 |
| MACD (12,26) | 0.5151 |
| MACD signal (9) | 0.4886 |
| MACD histogram | 0.0265 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PFE': 270, 'SPY': 270}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 29.4500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.1745 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.3400 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.5418 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 24.3777 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 28.6343 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.2171 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.6806 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.0123 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.9258 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.5887 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1445 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.1008 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2413 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.7243 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.2975 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 10.2112 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 27.8770 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 5.0140 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.4383 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 38.7500 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 56.5352 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0265 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.4866 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 12.1240 -> Clearly above the moving-average trend level.

## TAILWINDS

### Pfizer (PFE) Expected to Beat Earnings Estimates: Should You Buy?
- Summary: Pfizer is projected to exceed earnings estimates, indicating strong financial performance.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQLWFLYVV5V19FWkE5dklMNEY3MUdrTVdfekFiVnR2bFNscGVXc0p4anhtSmpzcUNRMmxTRUc3MTVoUmF5cUdtdHZJMnZrTmQtSEhuNlFoWEF1cHV2ckRWZWZQT2JlTnRPUEFPWEE0RmN4V1JyNkdsUHVMR3FySW1wTDdKZFQ1ZGdCN1ByWjlodW5UcGdYYWFMZnNIU0ZWZm8?oc=5>

### What Have Pfizer Stock Holders Really Earned?
- Summary: Examines actual earnings realized by Pfizer shareholders.
- Date: 2026-10-21 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPYllPVEJjWnV3MnBlcGRhWm1tS1VJVWZrclNDUFNlajhKUzdiYmNiWnVPcHBzTl9GbVhTR2JtU09EYUx0dWZudDhrQ2pveC15ZlF6clZPTkI2TzgwWlZVendSZEI1TVVXQllNVHptTWhuYUdodTVSR3BrY1hrZEllZ08xVXpIeHpwTnBydDlBcVJYZVRERk11djhoTjJ1VzJj?oc=5>

### How To Boost The Dividend Yield On This Drugmaking Behemoth
- Summary: Provides strategies to increase dividend yield for Pfizer shareholders.
- Date: 2026-10-22 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNQ0NpWENzSnJwcUxsVVBFMlJBa2wwb0FxOXFXZWtXazZFOEdYajVLTEdCdG0xaV9IMG1aVkp0V19fRVVWMFBLY3dLRDFKdTZqZmlhQ0VSNzBVY3RGZFc3bDdkanlHd3JqbnpDR1FPdWtMZHBISkFvVWFqU3VMZkg4cFozZ0hMVTZHQmxtUEV6ZGlwUEs2dm9lUmVocHg?oc=5>

### Pfizer’s drug pair cut the risk of prostate cancer worsening or death by 52% in a trial. FDA approved earlier use.
- Summary: Pfizer’s drug pair reduces prostate cancer risk by 52% and received FDA approval for earlier use.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxORFRjVnNhQTNqM1pfQjFrNWZuenF6ZEIxYlcxak5CMy1feVQxQmNFeUlFb3pTd3RRaGN6Q0NpZWxRWEgyQmRwdFJtaHNrdTI2dDEybmxmNDVfUXFTR2E2YVJXcXozSkdWbFpOMnZ6Mi1HVkhnaGxPd3hINkN1T1loV2RIWTF0cDdad3A0cHR2dGZmdmtINGM0OHplbU0xQTBBT21jUnVLaW1mWllmWjRhdmJOQkEzR0Mxdk1tTFQxTQ?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Pfizer (PFE) Stock Looks Above Fair Value As 30% Run Continues
- Summary: Pfizer (PFE) Stock Looks Above Fair Value As 30% Run Continues
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPcE5idEFfcVprMUpfcFJoVnlJdW1SYjNxbGExZGRkWTBqZ25JSlhJNDZRQ1FRek03QWx6UlpVZ0RkVkJYWjlFMXpJbmdlWXlheDEtWjk3LTRLbFJrbmxNTjlORTlRMDAwZWFlQ3pfLUZaYTRKaHZ1bzBSdEpLQy1JQU55LUJMdkhqN3hGSC1Tam51eW9Xd3hjSA?oc=5>

### Pfizer posts late-stage trial win for multiple myeloma drug Elrexfio in an earlier line setting
- Summary: Late-stage trial success for Elrexfio shows promising efficacy in earlier treatment line.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQdjAzOEluRTNteXVYWmJpWWZLd1YteHp1Y3RQTTVvWmFvTUdNTEc4Q0xFRVY2eTVPamU3dmJVckNydElESGZhb0M0bHF0b25IS2w2MU1VMFpLNjJRcEp1enMyNzRXei1oRGRBT1U2WEVFVldvS082YnF0akdHUWM5aW02cXhIR3NoU3k4VU54eF9iYVpDdTdGYw?oc=5>

### More than 75% of patients on Pfizer’s drug had no cancer progression or death at analysis
- Summary: High disease control rate in trial indicates strong therapeutic benefit.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxPZ19JeUp6eHNqNFlKSEZpQ2NZNEhkbTQyZURVZHRDNy1vN2RMWmloRDVYZjZJVi12ZkdReGgySmJEUUExNXRPbmRTZGZlX3UwRWdJYks5SnlGZVEyMXdaRVRYQVB5TWhhekUxTklBQ1JWQlJuUFZjc1Z3dnVhME9pLWI0aVJZQzlLM3Z3Ui1PMXlEMTU4akQ1YVlwS09nSUJVTGJUbXF4SUREUEQyMXZEcTBVakxGemhjUHdN?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PFE** | **38.75** | **1.97** | **8.66** | **2.60** | **167,855,390,720.00 USD** | **28.63** |
| MRK | 111.85 | 8.30 | 13.66 | 5.10 | 347,698,462,720.00 USD | 66.69 |
| JNJ | 40.76 | 8.00 | 19.71 | 5.90 | 652,477,399,040.00 USD | 48.26 |
| LLY | 43.03 | 33.90 | 28.64 | 47.70 | 1,148,830,482,432.00 USD | 58.08 |

Peers fetched as_of: 2026-10-28; PFE reuses existing data (market data as_of: 2026-10-28); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-28

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-04
- Revenue (latest available single quarter): 15,034,000,000.00 USD; period 2026-03-30/2026-06-28; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): -248,000,000.00 USD; period 2026-03-30/2026-06-28; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/78003/000007800326000095/pfe-20260628.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMinwFBVV95cUxQLWFLYVV5V19FWkE5dklMNEY3MUdrTVdfekFiVnR2bFNscGVXc0p4anhtSmpzcUNRMmxTRUc3MTVoUmF5cUdtdHZJMnZrTmQtSEhuNlFoWEF1cHV2ckRWZWZQT2JlTnRPUEFPWEE0RmN4V1JyNkdsUHVMR3FySW1wTDdKZFQ1ZGdCN1ByWjlodW5UcGdYYWFMZnNIU0ZWZm8?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPYllPVEJjWnV3MnBlcGRhWm1tS1VJVWZrclNDUFNlajhKUzdiYmNiWnVPcHBzTl9GbVhTR2JtU09EYUx0dWZudDhrQ2pveC15ZlF6clZPTkI2TzgwWlZVendSZEI1TVVXQllNVHptTWhuYUdodTVSR3BrY1hrZEllZ08xVXpIeHpwTnBydDlBcVJYZVRERk11djhoTjJ1VzJj?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNQ0NpWENzSnJwcUxsVVBFMlJBa2wwb0FxOXFXZWtXazZFOEdYajVLTEdCdG0xaV9IMG1aVkp0V19fRVVWMFBLY3dLRDFKdTZqZmlhQ0VSNzBVY3RGZFc3bDdkanlHd3JqbnpDR1FPdWtMZHBISkFvVWFqU3VMZkg4cFozZ0hMVTZHQmxtUEV6ZGlwUEs2dm9lUmVocHg?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxORFRjVnNhQTNqM1pfQjFrNWZuenF6ZEIxYlcxak5CMy1feVQxQmNFeUlFb3pTd3RRaGN6Q0NpZWxRWEgyQmRwdFJtaHNrdTI2dDEybmxmNDVfUXFTR2E2YVJXcXozSkdWbFpOMnZ6Mi1HVkhnaGxPd3hINkN1T1loV2RIWTF0cDdad3A0cHR2dGZmdmtINGM0OHplbU0xQTBBT21jUnVLaW1mWllmWjRhdmJOQkEzR0Mxdk1tTFQxTQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPcE5idEFfcVprMUpfcFJoVnlJdW1SYjNxbGExZGRkWTBqZ25JSlhJNDZRQ1FRek03QWx6UlpVZ0RkVkJYWjlFMXpJbmdlWXlheDEtWjk3LTRLbFJrbmxNTjlORTlRMDAwZWFlQ3pfLUZaYTRKaHZ1bzBSdEpLQy1JQU55LUJMdkhqN3hGSC1Tam51eW9Xd3hjSA?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQdjAzOEluRTNteXVYWmJpWWZLd1YteHp1Y3RQTTVvWmFvTUdNTEc4Q0xFRVY2eTVPamU3dmJVckNydElESGZhb0M0bHF0b25IS2w2MU1VMFpLNjJRcEp1enMyNzRXei1oRGRBT1U2WEVFVldvS082YnF0akdHUWM5aW02cXhIR3NoU3k4VU54eF9iYVpDdTdGYw?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxPZ19JeUp6eHNqNFlKSEZpQ2NZNEhkbTQyZURVZHRDNy1vN2RMWmloRDVYZjZJVi12ZkdReGgySmJEUUExNXRPbmRTZGZlX3UwRWdJYks5SnlGZVEyMXdaRVRYQVB5TWhhekUxTklBQ1JWQlJuUFZjc1Z3dnVhME9pLWI0aVJZQzlLM3Z3Ui1PMXlEMTU4akQ1YVlwS09nSUJVTGJUbXF4SUREUEQyMXZEcTBVakxGemhjUHdN?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
