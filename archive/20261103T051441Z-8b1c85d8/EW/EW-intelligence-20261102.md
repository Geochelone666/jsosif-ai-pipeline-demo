# EW Intelligence Report

- ticker: **EW**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/EW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/EW/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:38:48.563105+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 15, 'rule': 1, 'ai': 7, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/EW** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 15 unique headlines; 8 named publishers; 0 exact duplicates; 15 HTTPS source links; largest publisher share 26.67%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 93.2600 |
| Return 1D (%) | 1.3585 |
| Return 1W (%) | 2.9815 |
| Return 1M (%) | 9.5244 |
| Return YTD (%) | 9.3959 |
| Return 1Y (%) | 13.1110 |
| Annualized volatility (%) | 25.0983 |
| Beta vs SPY | 0.5639 |
| Max drawdown (%) | -13.1855 |
| Sharpe (rf=0) | 0.5896 |
| Downside deviation (rf=0, %) | 16.9815 |
| Sortino (rf=0) | 0.8714 |
| Historical VaR 95% (1D, %) | 2.5358 |
| Historical ES 95% (1D, %) | 3.1155 |
| Correlation vs SPY | 0.2881 |
| Tracking error vs SPY (%) | 24.6760 |
| P/E (trailing) | 54.86 |
| P/B | 5.06 |
| EV/EBITDA | 25.20 |
| Revenue growth (%) | 13.60 |
| Forward P/E (estimate) | 27.58 |
| Gross margin (%) | 77.84 |
| Operating margin (%) | 29.84 |
| Return on equity (%) | 9.18 |
| Free cash flow yield (%) | 2.29 |
| MA50 | 88.2122 |
| Close vs MA50 (%) | 5.7223 |
| MA200 | 85.4713 |
| Close vs MA200 (%) | 9.1127 |
| RSI (14, Wilder) | 62.7647 |
| MACD (12,26) | 1.4875 |
| MACD signal (9) | 0.8251 |
| MACD histogram | 0.6623 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'EW': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 93.2600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.3585 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.9815 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 9.5244 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 9.3959 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 13.1110 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.0983 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.9815 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.8714 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5358 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.1155 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2881 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.6760 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5639 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.1855 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5896 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 27.5819 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 77.8390 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 29.8390 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.1750 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.2926 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 54.8588 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 62.7647 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.6623 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.7223 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.1127 -> Clearly above the moving-average trend level.

## TAILWINDS

### Curious about Edwards Lifesciences (EW) Q3 Performance? Explore Wall Street Estimates for Key Metrics
- Summary: Wall Street estimates for EW’s Q3 performance are discussed, indicating potential earnings outlook.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQcUxYRldwUFpxWERpMmstOThqQ0x4bDVJUW9kM2lpbnp3c3k3ZGpINE93Q0l4VXdVVmRPYm5ocm9mSngtM2dlNm5BQkNhSkphbHUtN0hteFhtVDlTanU3WG5DNmNpckZfTkpCU01ZWTltc3B5WjY2U0lwbDFjUjFuNWx0b25zanJGenA2cDc4SE5QX0pVU19ROThJU1pPNzJu?oc=5>

### Edwards Lifesciences' PASCAL System Trial Success Boosts Prospec
- Summary: Positive trial results for PASCAL System, indicating improved patient outcomes.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPLTNNVF91VC1xTndlSFVLRzhuazZJM1d4MnZXVlUyRVZfeGRtUVJ5bml0THNBYnV6ZzRYcm5BcmRCRFVjYnUwSEN5OEVPRUVDWWUwR3dIV0JJU0pUQjdmOHJjNVZRbDR0aFhjcUpRMmwtcEpzOUpNOWx2TTJUbXhYd3FReG83aUtIUWRmR2pjWThZNjJ2UWtEMHJJdklhdXVSaWR6NkNyZzNvS256UTRXX3dKZm44OUoz?oc=5>

### Edwards Lifesciences (EW) Reports Positive CLASP II TR Trial Res
- Summary: CLASP II TR trial shows favorable results for Edwards device.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxOb0pDekI2dTZDeXNHOXZMM1lRX0VVQUtLTjEzSEtQMjN1aTdiR3BqcUJCWk4wSFJ2bnB2QUNnNG1CMWRiN1c4QXplRlVrV3dXTjhuTFZjNUhUb00yQWN0TG9GdmdXM2RVaXJYZVFEd1Y3UWZ0eTZVdV9DNTRnQVRlM2NhN0V4QXFOZmhKY2lEWTQzVV8yQjBxOUtoVFhhX0gzcUtSYTdkVUJDSy1OMm81cWNZQmRqa0ZYdGZMLVBrUHQ?oc=5>

## HEADWINDS

### Edwards Lifesciences (EW) Short Interest & Short Float | Updated Nov 2026 $EW
- Summary: High short interest indicates bearish sentiment, possibly pressuring the stock price.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiaEFVX3lxTE9tRHlLRzRBNUEyNWJSdDBXUVZoaGl1cXkzb2QxUHFINks5a1gta2tvNTFqanE1d29wdmpSWjFPa2hJRmpuN1VlTWgtejNZNGkxQTBISFJfLW13N0JGX1JPMG83anRlcWpG?oc=5>

## CATALYSTS

### Edwards Lifesciences Corporation $EW Stock: Generali Asset Management SPA SGR Lowers Position
- Summary: Edwards Lifesciences Corporation $EW Stock: Generali Asset Management SPA SGR Lowers Position
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5wFBVV95cUxNMzQ0THN2UUoyeGZNRjdOdm1RNjg3akkxQThTaUFPRC11ck93YzkzSWtzZmlvWXUyQUxaOUEya0pablJFRkp1YWRZRUl3VzMwWmxnM1BDQVlOV0hqc2ZqbWhuS1Ewc2U2d3N1cnQtX2ZmZjlLM01yMXp6ZG9PejkwSW1BSjhZdnZrWDJDWHQ5N01qa1FqaVJGYTRaSFlMdFpvaGt2Z0NQS1RHR2twSk9ZcUxXUmlJR044UVYtR3NMbi1zWWxWa21UVGQ1eWh6eXh0VVM5UlNhUVA2dER1VXFvaVQwVjJlZHM?oc=5>

### Edwards Lifesciences Continually Innovating Ahead Of Q3 Results, Cardio Portfolio Thrives
- Summary: Edwards Lifesciences highlights ongoing innovation and strong cardio portfolio performance ahead of Q3 results.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNeGNQODFnODBXNHpLc1BVWWI5SndlUnkxdzZBX2dIX1V2MkJrb09OSXB6cGdNZ2k3NF9JSkJOSERwTmtaZ0M2NkhEOUVOWVJOWVdPUVZwRGNtNWs1ZVpGczdTa01leDFiTXVVWDBNUlFiNnk2Y3VuZzE0bmZ5TDRCOXFyZEZVZEtFTXBMdVIwRXkzemJEbUZqMWt4aWpWNklTMkdWYlFFSXJHSjJJQ1BadW9qSGNZdUx4NHpPRXRRVUJwak5HTlE?oc=5>

### Is FDA Valve Repair Approval Altering The Investment Case For Edwards Lifesciences (EW)?
- Summary: FDA approval of valve repair technology may influence Edwards Lifesciences' market position and investor perception.
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxQaWx4VEVYTHNJczJMVG9ObzUweDJ6R1J3b3ZrOGgzUHZSdjV3MC1idmk3d25lX0JvR2luWEtfSmhaZ2ZlbVJDRkpDQjZjTzhkYWpzaVlralV5Nm8wRl92SXBlc1l0RG80VVRlMDFZUlh5SHphdFVzaDF0eGlJSnBPUWJsMGJNNV9YT215VUVOd3hLcG9iY05ZWU1mc1VGT1dkT3lRWVdDc1RxOEpVN0RuZmJ2SlQ1LWVNZnVfM1hybng2VlBFdmp1ejdsdUgxa01pZy0w0gHYAUFVX3lxTE5mSlluaXJyRy1xb0hBd3NfNVNrakVlU3RZeDM0NkRiWThYSnI3YWF5cC1xbFZweHYtTERtSng3eFI5SFNTbDAtaDZXVThNdkpfaWt1NVI3d1VuTVNTenZBN1dvZ1ZqZHc2M2NNRWpITEVSbVZBQzdDeTE2dXhGSFFCU0FUSjlpQmRyeEIxaUJUb0dQMm41b3loYlNFSzFZaU1UMGNvNHJVeEwxQ3pvMDFNUFBjRjZyZXNkU1hhN2phY0FrTEp0TnBma2kzMXBiRG5XOUhrNWhfVg?oc=5>

### Edwards Lifesciences (EW) Could Be 6% Undervalued As FDA Approvals Lift Growth Hopes
- Summary: FDA approvals may boost EW’s growth prospects, suggesting the stock could be undervalued by 6%.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxPNXc3MWxOLUJLVUpyRXhja2ZpcWlVT2JsQTh0UWRwNkZlVVFzMzRJTUpSc1p5Z1M0ZnRNbUhjUTZXcWRtX1Bfa0pTcExTUXhweWFUUzRibUFlTHNJQXdlcENNVDFYbjhISWZycmJBWDF3MFpIV3VxSGZoRG94MTZUMEF2WkhDbjY2Rmp2NmNocVI3cVc5U3JOWDlma1lEUkw0ZXJSVGZXdVNDQjhyUzI1Qm9LR0drQXN1VGxfdlF1OHB6bU0zUXhoMF9nSmp0R2I4U01V0gHYAUFVX3lxTE85ckFEOXE2T0xsTS1UZlQ0anp2d0xYNm4tM1hiNlJJNkZvQlgya21XY0FEUG9EcFNuMVZaYnlaMHc5b1pGdXkzNVVLaE5XWGFIMEdOQUp2VDdubm1Rd1piVlItX3JkNTg2ekNjbjZ4RkkxNXlUcVExcUNzeGtVSVJJT3RYSXIwa0tGTFhXMFFpRUNUa3pmVElYbWxUTU9hS2ZMMkRySlA0UWhqaFhwaFdTUUFPTmxBOV90c3VpTi1FeUFpeGdyTnRqaDQ1Y3VUd3gyMzNCUHVweQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **EW** | **54.86** | **5.06** | **25.20** | **13.60** | **53,755,064,320.00 USD** | **13.11** |
| MDT | 23.70 | 2.53 | 14.12 | 13.70 | 127,005,605,888.00 USD | 13.10 |
| BSX | 18.70 | 2.57 | 13.45 | 1.40 | 64,229,855,232.00 USD | -56.00 |
| ABT | 40.95 | 3.73 | 18.27 | 14.50 | 190,619,041,792.00 USD | -8.67 |

Peers fetched as_of: 2026-11-02; EW reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-23
- Next expected earnings: 2026-11-04 (yfinance; expected dates may change)

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
- Revenue (latest available single quarter): 1,741,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 241,900,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1099800/000109980026000043/ew-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMioAFBVV95cUxQcUxYRldwUFpxWERpMmstOThqQ0x4bDVJUW9kM2lpbnp3c3k3ZGpINE93Q0l4VXdVVmRPYm5ocm9mSngtM2dlNm5BQkNhSkphbHUtN0hteFhtVDlTanU3WG5DNmNpckZfTkpCU01ZWTltc3B5WjY2U0lwbDFjUjFuNWx0b25zanJGenA2cDc4SE5QX0pVU19ROThJU1pPNzJu?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPLTNNVF91VC1xTndlSFVLRzhuazZJM1d4MnZXVlUyRVZfeGRtUVJ5bml0THNBYnV6ZzRYcm5BcmRCRFVjYnUwSEN5OEVPRUVDWWUwR3dIV0JJU0pUQjdmOHJjNVZRbDR0aFhjcUpRMmwtcEpzOUpNOWx2TTJUbXhYd3FReG83aUtIUWRmR2pjWThZNjJ2UWtEMHJJdklhdXVSaWR6NkNyZzNvS256UTRXX3dKZm44OUoz?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxOb0pDekI2dTZDeXNHOXZMM1lRX0VVQUtLTjEzSEtQMjN1aTdiR3BqcUJCWk4wSFJ2bnB2QUNnNG1CMWRiN1c4QXplRlVrV3dXTjhuTFZjNUhUb00yQWN0TG9GdmdXM2RVaXJYZVFEd1Y3UWZ0eTZVdV9DNTRnQVRlM2NhN0V4QXFOZmhKY2lEWTQzVV8yQjBxOUtoVFhhX0gzcUtSYTdkVUJDSy1OMm81cWNZQmRqa0ZYdGZMLVBrUHQ?oc=5
- https://news.google.com/rss/articles/CBMiaEFVX3lxTE9tRHlLRzRBNUEyNWJSdDBXUVZoaGl1cXkzb2QxUHFINks5a1gta2tvNTFqanE1d29wdmpSWjFPa2hJRmpuN1VlTWgtejNZNGkxQTBISFJfLW13N0JGX1JPMG83anRlcWpG?oc=5
- https://news.google.com/rss/articles/CBMi5wFBVV95cUxNMzQ0THN2UUoyeGZNRjdOdm1RNjg3akkxQThTaUFPRC11ck93YzkzSWtzZmlvWXUyQUxaOUEya0pablJFRkp1YWRZRUl3VzMwWmxnM1BDQVlOV0hqc2ZqbWhuS1Ewc2U2d3N1cnQtX2ZmZjlLM01yMXp6ZG9PejkwSW1BSjhZdnZrWDJDWHQ5N01qa1FqaVJGYTRaSFlMdFpvaGt2Z0NQS1RHR2twSk9ZcUxXUmlJR044UVYtR3NMbi1zWWxWa21UVGQ1eWh6eXh0VVM5UlNhUVA2dER1VXFvaVQwVjJlZHM?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNeGNQODFnODBXNHpLc1BVWWI5SndlUnkxdzZBX2dIX1V2MkJrb09OSXB6cGdNZ2k3NF9JSkJOSERwTmtaZ0M2NkhEOUVOWVJOWVdPUVZwRGNtNWs1ZVpGczdTa01leDFiTXVVWDBNUlFiNnk2Y3VuZzE0bmZ5TDRCOXFyZEZVZEtFTXBMdVIwRXkzemJEbUZqMWt4aWpWNklTMkdWYlFFSXJHSjJJQ1BadW9qSGNZdUx4NHpPRXRRVUJwak5HTlE?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQaWx4VEVYTHNJczJMVG9ObzUweDJ6R1J3b3ZrOGgzUHZSdjV3MC1idmk3d25lX0JvR2luWEtfSmhaZ2ZlbVJDRkpDQjZjTzhkYWpzaVlralV5Nm8wRl92SXBlc1l0RG80VVRlMDFZUlh5SHphdFVzaDF0eGlJSnBPUWJsMGJNNV9YT215VUVOd3hLcG9iY05ZWU1mc1VGT1dkT3lRWVdDc1RxOEpVN0RuZmJ2SlQ1LWVNZnVfM1hybng2VlBFdmp1ejdsdUgxa01pZy0w0gHYAUFVX3lxTE5mSlluaXJyRy1xb0hBd3NfNVNrakVlU3RZeDM0NkRiWThYSnI3YWF5cC1xbFZweHYtTERtSng3eFI5SFNTbDAtaDZXVThNdkpfaWt1NVI3d1VuTVNTenZBN1dvZ1ZqZHc2M2NNRWpITEVSbVZBQzdDeTE2dXhGSFFCU0FUSjlpQmRyeEIxaUJUb0dQMm41b3loYlNFSzFZaU1UMGNvNHJVeEwxQ3pvMDFNUFBjRjZyZXNkU1hhN2phY0FrTEp0TnBma2kzMXBiRG5XOUhrNWhfVg?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxPNXc3MWxOLUJLVUpyRXhja2ZpcWlVT2JsQTh0UWRwNkZlVVFzMzRJTUpSc1p5Z1M0ZnRNbUhjUTZXcWRtX1Bfa0pTcExTUXhweWFUUzRibUFlTHNJQXdlcENNVDFYbjhISWZycmJBWDF3MFpIV3VxSGZoRG94MTZUMEF2WkhDbjY2Rmp2NmNocVI3cVc5U3JOWDlma1lEUkw0ZXJSVGZXdVNDQjhyUzI1Qm9LR0drQXN1VGxfdlF1OHB6bU0zUXhoMF9nSmp0R2I4U01V0gHYAUFVX3lxTE85ckFEOXE2T0xsTS1UZlQ0anp2d0xYNm4tM1hiNlJJNkZvQlgya21XY0FEUG9EcFNuMVZaYnlaMHc5b1pGdXkzNVVLaE5XWGFIMEdOQUp2VDdubm1Rd1piVlItX3JkNTg2ekNjbjZ4RkkxNXlUcVExcUNzeGtVSVJJT3RYSXIwa0tGTFhXMFFpRUNUa3pmVElYbWxUTU9hS2ZMMkRySlA0UWhqaFhwaFdTUUFPTmxBOV90c3VpTi1FeUFpeGdyTnRqaDQ1Y3VUd3gyMzNCUHVweQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
