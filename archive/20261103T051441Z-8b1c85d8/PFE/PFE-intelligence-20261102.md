# PFE Intelligence Report

- ticker: **PFE**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/PFE/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PFE/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:23:26.011605+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 11, 'rule': 3, 'ai': 5, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/PFE** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 11 unique headlines; 4 named publishers; 0 exact duplicates; 11 HTTPS source links; largest publisher share 54.55%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 30.6700 |
| Return 1D (%) | 0.4915 |
| Return 1W (%) | 2.9540 |
| Return 1M (%) | 10.3237 |
| Return YTD (%) | 29.5302 |
| Return 1Y (%) | 33.1479 |
| Annualized volatility (%) | 21.3310 |
| Beta vs SPY | 0.2092 |
| Max drawdown (%) | -15.7243 |
| Sharpe (rf=0) | 1.4577 |
| Downside deviation (rf=0, %) | 13.6809 |
| Sortino (rf=0) | 2.2728 |
| Historical VaR 95% (1D, %) | 1.9262 |
| Historical ES 95% (1D, %) | 2.5887 |
| Correlation vs SPY | 0.1257 |
| Tracking error vs SPY (%) | 23.4654 |
| P/E (trailing) | 40.36 |
| P/B | 2.05 |
| EV/EBITDA | 8.94 |
| Revenue growth (%) | 2.60 |
| Forward P/E (estimate) | 10.62 |
| Gross margin (%) | 74.72 |
| Operating margin (%) | 27.88 |
| Return on equity (%) | 5.01 |
| Free cash flow yield (%) | 7.14 |
| MA50 | 28.5986 |
| Close vs MA50 (%) | 7.2430 |
| MA200 | 26.3570 |
| Close vs MA200 (%) | 16.3640 |
| RSI (14, Wilder) | 67.7421 |
| MACD (12,26) | 0.5837 |
| MACD signal (9) | 0.5203 |
| MACD histogram | 0.0635 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PFE': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 30.6700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.4915 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.9540 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 10.3237 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 29.5302 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 33.1479 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.3310 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.6809 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.2728 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.9262 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.5887 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1257 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.4654 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2092 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.7243 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.4577 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 10.6240 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 27.8770 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 5.0140 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.1424 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 40.3553 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 67.7421 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0635 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.2430 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 16.3640 -> Clearly above the moving-average trend level.

## TAILWINDS

### How Investors May Respond To Pfizer (PFE) Phase 3 Cancer Trial Win
- Summary: Pfizer’s Phase 3 cancer trial success could boost investor confidence and stock value.
- Date: 2026-10-30 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOY2xpOUpJZHlybnYtNWZVOEszc21hMGptcWF0cmZsdVc2SkFxUHh1V3ZfWTdvMkRWNnVXWllEbHhhbDVCY2hqMnNfSmZIMnB0WTVQZDIwc2NISi1rQUtvRDlyRTlZLTc4MHhla1NhTmtiRXB2UFVUblhYanc2V1BwQVliUFdwUmdKeXpycE5vUk9rUEhoTk5iQw?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Pfizer Q3 preview: Analysts look to obesity pipeline amid diverging growth expectations (PFE:NYSE)
- Summary: Pfizer Q3 preview: Analysts look to obesity pipeline amid diverging growth expectations (PFE:NYSE)
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxOaVA1cGtvS25jb25FMnNKX0VyUGk5UVljVjVpZndtMVFWQ01ZRWtvNVpvSFBRdVpDU0lZend5ZVhLbVk0VlVuNk9vSnRHaDRCOVVIcU9uTWhxWUx4RVRNWkhaWnRHVUFZenk3SHU1Tk5PQmtoWnpCMTV4cVp3MnU0SHlqZTNfLU1IMjlHM3ZGbEdpWG11OEZ2RmtkR1pPNHBPMHBtQVhmTlBTcHRiN2hTUHB0Y0VyVXByTjJZeGZqVE56UQ?oc=5>

### Pfizer (PFE) Stock Looks Above Fair Value As 30% Run Continues
- Summary: Pfizer (PFE) Stock Looks Above Fair Value As 30% Run Continues
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPcE5idEFfcVprMUpfcFJoVnlJdW1SYjNxbGExZGRkWTBqZ25JSlhJNDZRQ1FRek03QWx6UlpVZ0RkVkJYWjlFMXpJbmdlWXlheDEtWjk3LTRLbFJrbmxNTjlORTlRMDAwZWFlQ3pfLUZaYTRKaHZ1bzBSdEpLQy1JQU55LUJMdkhqN3hGSC1Tam51eW9Xd3hjSA?oc=5>

### Pfizer (PFE) Reports Q3 Earnings Tomorrow — Here’s Why Wall Street Remains Split
- Summary: Pfizer (PFE) Reports Q3 Earnings Tomorrow — Here’s Why Wall Street Remains Split
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPWUN6OU0xMTFqbFZfLVEwYjJrc2lESDJhaHV1ZXA4MEwwd1hzVlRmMEFoUkhoazA1UDk1QTlLRmlSNmVpTkF4RnZZaWVxSFp2aFp6d1NxRDd2amc5cG92MEhVZlFwdV9URWZWS0Rod0FLZXU1ZFlxQkNVQnB5V1ZEbWM0VVh4eUxldXdiaWNYUWpsbndSUHhGaldQTjUxcWJ0TENzSDEyS1Q?oc=5>

### Exploring Analyst Estimates for Pfizer (PFE) Q3 Earnings, Beyond Revenue and EPS
- Summary: Analysts discuss Pfizer’s Q3 earnings outlook, focusing on revenue and EPS projections.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQRjA0eEVyLWJIeGUtNGlBYXpwNjlseWozeFBieEFwSzdLWmxkQ0ZCS0VwYkpZZzRUN0FWNlpBNUNSam80cHNGS3dEYzFHaG1aNEdybFV0N1JlMGdwRnBVbnQycE41eU15dEhfdlBhaHZzejZQWG53dFR4cTcwa0toWDV3SGNmeWpiaGVaamtNanphb0NWdUE4N2djOTJSMHN4UlVxT2V3?oc=5>

### Pfizer: Reality Check Ahead Of Earnings (NYSE:PFE)
- Summary: Pfizer prepares for earnings release, highlighting potential risks and opportunities for investors.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxOUDIxNEZ5V2hrbnBDNUlMbzdjT2xOY1h6b2N4T3h6Tk9FZ0ZhRWh6MDZ1ajdoVGhnQ1J3cUxvaVJncU91b3FyVHVOenRMU2F0b1V0UngxOFV3Tnh5am9raG55V3d0QVNvUlJ4S2xNMHNUUXhsaVRocUxRTWgxOWI3cUYyek9NUQ?oc=5>

### What to expect from Pfizer’s (PFE) Q3 earnings
- Summary: Analysts discuss expected Q3 earnings, guidance, and potential impact on stock.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPN1Itd1VZUGl5dVBWVmhjS29zWk1FbmdRaFhwWVBPcjRTOWtTbzVHNmFPeThRTGZqaE95VDB4YmNnRHUzTlNUclVtM3V2Tkp1S2lCeVVKX3BhSGhsdVN3Rm1Vd1Nmb1NlQldUb0ZqUXY5RG5uZGZmaUt4TXR5b3RzSGlrVXMyRDlFVms5YmFyTzFvcmNx?oc=5>

### Pfizer (PFE) Scores Legal And Product Wins, Is The Stock Now Too Expensive?
- Summary: Pfizer reports legal victories and product successes, potentially boosting investor confidence.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxNbU4yUE8yOEw2YV9RYTRrS09acDh0S3I2VU9ldVdwNnVFak1STWtIX0RHaVU3bkNtalRzV1pHYW5QSG4xSzNsX1RCcWtuU0tCNDhZSVRsblVxVjJzeTRLMnVLM3lhSndwcFFSZW1fRkNaRHFvdndBTEhEM0VKdkN6NGU5cWJLUkRYRlBmY0Z0Z3NUMkZxV3pOUHhuZDZwLU1VUUs2MFhYLXU2QXlvcnl3V0ZJM013b2dGZG93ajRFT2RDdFdEM0Q5N1R3ZmZZd1VNMnVZ0gHYAUFVX3lxTE5BbGpKQ0FlTGNLekFIQWpodXA3VDhxUVVUdjFUdDEzcnBKM3RXdkdXeU9TVlFkeDAwamw3MEdudWlhRWRBWS1ZNld4V3RmLVZyQXBrdmg2ZWhfdC1pOUlhZUlfZEloTnpmMURVb1RSekdCZ29Wcjc1Y1g2WjFZcTJXLUc2aF82T3BJOE5xQjlicTlfVnNqbXBQWjJiWHBmcVpObFdLWWlpRGpCeGtHRHhtSVJDZEJoUDk2VGV3Y2ZCSkFmenRFRmkxdmc0SXdlMHotTGlINmx4Vg?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PFE** | **40.36** | **2.05** | **8.94** | **2.60** | **174,808,989,696.00 USD** | **33.15** |
| MRK | 149.86 | 8.73 | 25.86 | 4.70 | 366,029,570,048.00 USD | 77.62 |
| JNJ | 41.06 | 7.99 | 19.67 | 5.90 | 651,321,868,288.00 USD | 46.48 |
| LLY | 45.80 | 31.23 | 28.00 | 38.60 | 1,256,832,368,640.00 USD | 64.56 |

Peers fetched as_of: 2026-11-02; PFE reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMimAFBVV95cUxOY2xpOUpJZHlybnYtNWZVOEszc21hMGptcWF0cmZsdVc2SkFxUHh1V3ZfWTdvMkRWNnVXWllEbHhhbDVCY2hqMnNfSmZIMnB0WTVQZDIwc2NISi1rQUtvRDlyRTlZLTc4MHhla1NhTmtiRXB2UFVUblhYanc2V1BwQVliUFdwUmdKeXpycE5vUk9rUEhoTk5iQw?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxOaVA1cGtvS25jb25FMnNKX0VyUGk5UVljVjVpZndtMVFWQ01ZRWtvNVpvSFBRdVpDU0lZend5ZVhLbVk0VlVuNk9vSnRHaDRCOVVIcU9uTWhxWUx4RVRNWkhaWnRHVUFZenk3SHU1Tk5PQmtoWnpCMTV4cVp3MnU0SHlqZTNfLU1IMjlHM3ZGbEdpWG11OEZ2RmtkR1pPNHBPMHBtQVhmTlBTcHRiN2hTUHB0Y0VyVXByTjJZeGZqVE56UQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPcE5idEFfcVprMUpfcFJoVnlJdW1SYjNxbGExZGRkWTBqZ25JSlhJNDZRQ1FRek03QWx6UlpVZ0RkVkJYWjlFMXpJbmdlWXlheDEtWjk3LTRLbFJrbmxNTjlORTlRMDAwZWFlQ3pfLUZaYTRKaHZ1bzBSdEpLQy1JQU55LUJMdkhqN3hGSC1Tam51eW9Xd3hjSA?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPWUN6OU0xMTFqbFZfLVEwYjJrc2lESDJhaHV1ZXA4MEwwd1hzVlRmMEFoUkhoazA1UDk1QTlLRmlSNmVpTkF4RnZZaWVxSFp2aFp6d1NxRDd2amc5cG92MEhVZlFwdV9URWZWS0Rod0FLZXU1ZFlxQkNVQnB5V1ZEbWM0VVh4eUxldXdiaWNYUWpsbndSUHhGaldQTjUxcWJ0TENzSDEyS1Q?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQRjA0eEVyLWJIeGUtNGlBYXpwNjlseWozeFBieEFwSzdLWmxkQ0ZCS0VwYkpZZzRUN0FWNlpBNUNSam80cHNGS3dEYzFHaG1aNEdybFV0N1JlMGdwRnBVbnQycE41eU15dEhfdlBhaHZzejZQWG53dFR4cTcwa0toWDV3SGNmeWpiaGVaamtNanphb0NWdUE4N2djOTJSMHN4UlVxT2V3?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxOUDIxNEZ5V2hrbnBDNUlMbzdjT2xOY1h6b2N4T3h6Tk9FZ0ZhRWh6MDZ1ajdoVGhnQ1J3cUxvaVJncU91b3FyVHVOenRMU2F0b1V0UngxOFV3Tnh5am9raG55V3d0QVNvUlJ4S2xNMHNUUXhsaVRocUxRTWgxOWI3cUYyek9NUQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPN1Itd1VZUGl5dVBWVmhjS29zWk1FbmdRaFhwWVBPcjRTOWtTbzVHNmFPeThRTGZqaE95VDB4YmNnRHUzTlNUclVtM3V2Tkp1S2lCeVVKX3BhSGhsdVN3Rm1Vd1Nmb1NlQldUb0ZqUXY5RG5uZGZmaUt4TXR5b3RzSGlrVXMyRDlFVms5YmFyTzFvcmNx?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxNbU4yUE8yOEw2YV9RYTRrS09acDh0S3I2VU9ldVdwNnVFak1STWtIX0RHaVU3bkNtalRzV1pHYW5QSG4xSzNsX1RCcWtuU0tCNDhZSVRsblVxVjJzeTRLMnVLM3lhSndwcFFSZW1fRkNaRHFvdndBTEhEM0VKdkN6NGU5cWJLUkRYRlBmY0Z0Z3NUMkZxV3pOUHhuZDZwLU1VUUs2MFhYLXU2QXlvcnl3V0ZJM013b2dGZG93ajRFT2RDdFdEM0Q5N1R3ZmZZd1VNMnVZ0gHYAUFVX3lxTE5BbGpKQ0FlTGNLekFIQWpodXA3VDhxUVVUdjFUdDEzcnBKM3RXdkdXeU9TVlFkeDAwamw3MEdudWlhRWRBWS1ZNld4V3RmLVZyQXBrdmg2ZWhfdC1pOUlhZUlfZEloTnpmMURVb1RSekdCZ29Wcjc1Y1g2WjFZcTJXLUc2aF82T3BJOE5xQjlicTlfVnNqbXBQWjJiWHBmcVpObFdLWWlpRGpCeGtHRHhtSVJDZEJoUDk2VGV3Y2ZCSkFmenRFRmkxdmc0SXdlMHotTGlINmx4Vg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
