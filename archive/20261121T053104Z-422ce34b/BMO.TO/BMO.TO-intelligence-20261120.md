# BMO.TO Intelligence Report

- ticker: **BMO.TO**
- Report as_of: **2026-11-20**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/BMO.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BMO.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-20**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-21T05:44:00.148750+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 12, 'rule': 3, 'ai': 4, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261120T053808Z-e360129e/BMO.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 12 unique headlines; 8 named publishers; 1 exact duplicates; 12 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-13

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 224.4900 |
| Return 1D (%) | -2.8434 |
| Return 1W (%) | -9.1207 |
| Return 1M (%) | -3.9679 |
| Return YTD (%) | 29.8803 |
| Return 1Y (%) | 36.8839 |
| Annualized volatility (%) | 20.0199 |
| Beta vs SPY | 0.8431 |
| Max drawdown (%) | -12.3392 |
| Sharpe (rf=0) | 1.6754 |
| Downside deviation (rf=0, %) | 13.9106 |
| Sortino (rf=0) | 2.4113 |
| Historical VaR 95% (1D, %) | 2.1035 |
| Historical ES 95% (1D, %) | 2.7378 |
| Correlation vs SPY | 0.6000 |
| Tracking error vs SPY (%) | 16.3087 |
| P/E (trailing) | 18.30 |
| P/B | 1.84 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 12.00 |
| Forward P/E (estimate) | 13.58 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 37.94 |
| Return on equity (%) | 10.57 |
| Free cash flow yield (%) | N/A |
| MA50 | 238.5138 |
| Close vs MA50 (%) | -5.8797 |
| MA200 | 223.3525 |
| Close vs MA200 (%) | 0.5093 |
| RSI (14, Wilder) | 31.9471 |
| MACD (12,26) | -1.3965 |
| MACD signal (9) | 0.7418 |
| MACD histogram | -2.1383 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BMO.TO': 286, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 224.4900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.8434 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -9.1207 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -3.9679 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 29.8803 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 36.8839 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 20.0199 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.9106 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.4113 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1035 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.7378 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6000 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 16.3087 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8431 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -12.3392 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.6754 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 13.5797 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 37.9380 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.5740 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.2958 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 31.9471 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.1383 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.8797 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 0.5093 -> Slightly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### Bank of Montreal falls 2.84% in Friday's session
- Summary: Bank of Montreal falls 2.84% in Friday's session
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxONnJWeUpMVXRIbmZDM0RaTXVCc1VTWFR2SGVBanBsNERacVFDWEdWemVDemRLX1lOeFZHVnFBMWZ5NUdmVUI0R3k5RGlsR3VIeTFHaUxpaW9hUDJ6RVBsUk9Ba19yNWJtaHNEMEhUWFBlenl4VDRfdkZOWFVSN1NyZ1ZJOEFPaXhO?oc=5>

### Bank of Montreal (TSX:BMO) Stock Under Pressure: 0.55% Decline Raises Credit Risk and Valuation Concerns Amid Banking Sector Uncertainty
- Summary: Bank of Montreal (TSX:BMO) Stock Under Pressure: 0.55% Decline Raises Credit Risk and Valuation Concerns Amid Banking Sector Uncertainty
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi9wFBVV95cUxQN2hoa0N6RHhWNk5wRDluYlZRdXhkeWl6bFg0VGUyaEdxU0F2VnBUOTNKZklPcjJmU01XMFBPZmpRX3R0a2tuVUJfbjFiTWptNUNQNml0VjlpWWJPWEVsdHprdnNMdk5tMmY0TVhkRHBMVE9acVlyS2QtTEZ6cDBJQkpnUXNERThmQ2ttSWtBSUd5RTJOdDVBSU0zdUNNV2VvTDMyVUEzSDFwZERrbXdaVDhuSEFNS2dYenhvdUVjZGpoTXFoOG1QejBicGN6S1FDQUM2N29WY0RZb0JGTFV1cUctYmprNXprNkJBRWsydEstWUEyNk4w?oc=5>

## CATALYSTS

### Bank of Montreal (TSX:BMO): S&P/TSX Large-Cap Value Stock and the Outlook for Its Dividend
- Summary: Bank of Montreal (TSX:BMO): S&P/TSX Large-Cap Value Stock and the Outlook for Its Dividend
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNajRldVoxRV8wYjQyeHp5V09OdVhIN2tqdlR0RDFZVmoyWXQ3M3o5QWhUVTUtREY3QWlkRFJEMmxnLVFMeE4wUTNGaHRkZXdkWm9nX0NnY3JpQkVpMmliWW1QenhxQ09IeUpHQ0lsRDRiNFhFLUg5QlR2SXdCTl9WV2dFbVJEM09MVGNjcDNJWTNUU2VCWGE0bDhRaFZSc1JNZnd5N1BpNWd2bXBCMVhFXzc5eFd4S29DUm9tYmtvTzROdw?oc=5>

### Bank of Montreal (TSX:BMO) Pushes Digital Banking While Valuation Stays In Focus
- Summary: BMO emphasizes digital banking expansion while maintaining valuation focus.
- Date: 2026-11-13 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOa2dUZmEwdWxkaGVCUnB0SVNTTWU3ekl0M2lEcDk4TDhTNFpva1h5RHpqWkw0V1dZOElLa1E3RENvQ3FxNGx4cnVfSVNjNHpzbkxVU1JrRXh6UmxOR2w3eUV1QkhuQU15ZEhtM21PQkN4Ukd6aGhYZGU4aXNic0pHTGlMQ0lETVZpSWVISWN3YmR6VkJ0RkZmaw?oc=5>

### Bank of Montreal (BMO.TO) - What Are Brokerages Thinking About This Stock?
- Summary: Brokerages are evaluating BMO’s prospects, potentially influencing investor sentiment and valuation.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNQ2Z3Ym1zQlk0YUJsd01EWm53aFhPcDJJZXI3V3cyeUhhbDhqWnk4bEMybHh4NWRxT2FDdlh2SjVDSGlPUXRZNXFwbWFfaXZkSnczaEd6d3RRS0ctb1NFdkpIUzF1T1IwUWUyeGVXdVIyMTRWeVhpNTBfYzNhenNKc3NWYm1fV2dhWXhtZzRNSlU3X1EzVVlJMjM3aUc1OUZTTlN6V2Q2V1d4QjlkV0FCVzk4U2xKRGJKR1pudHFJYTFteFYxVEg5MHkzRUk?oc=5>

### EXCLUSIVE: Canada's BMO returning to US oil and gas investment banking, sources say
- Summary: BMO re-enters US oil and gas investment banking, expanding its service portfolio.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxPMEJnU0FpNlBIQVVrY3RZWkxwVzV5a0RJajBPLWpIZW5DX1Y1cDBuZnJsWU14dHBGcGV3aE9LRkx6aVg4VDRjVHB1UmphaWN1VVJCQVQ1bEhnel9rTnNzSmZVZUJlTHZsTHVsdWpmZjM2aHQ1R09mZEZTUVpqbV9VZ18tMC15WkhxOW5PN2FtNHRXMHkwUndMV3NBQVZtaGNKajVzZkZfMWNwd0pYS21Ea0ZBNkZtUQ?oc=5>

### Bank Of Montreal (TSX:BMO) Reached Quantum Utility In Banking Machine Learning
- Summary: BMO achieves quantum utility in banking machine learning, enhancing tech capabilities.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPMVBzSG9mMFpkNllsM3k3aXJmRXBYdThOWEpTRER6MTZ4WnNZZ1NGQkV1OFpBamtxY052ZWljS2U2cE1xSkhzaHRHdl9ZNmQ0eldwY1I3RGdfemhmVG5iNTl6LVBZYWg0aExuWDBXWW5vVmh5V1JsVlV0d0ZHeUFELTh0OGY4SmQzVXhpNXZ0dWhwUHR5UDFWNA?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BMO.TO** | **18.30** | **1.84** | **N/A** | **12.00** | **156,041,265,152.00 CAD** | **36.88** |
| RY.TO | 16.59 | 2.72 | N/A | 8.90 | 364,174,245,888.00 CAD | 29.83 |
| TD.TO | 17.00 | 2.14 | N/A | 11.50 | 264,630,353,920.00 CAD | 45.59 |
| BNS.TO | 15.22 | 1.64 | N/A | 11.70 | 146,137,710,592.00 CAD | 33.37 |

Peers fetched as_of: 2026-11-20; BMO.TO reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-25
- Next expected earnings: 2026-12-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-20

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

- https://news.google.com/rss/articles/CBMiiAFBVV95cUxONnJWeUpMVXRIbmZDM0RaTXVCc1VTWFR2SGVBanBsNERacVFDWEdWemVDemRLX1lOeFZHVnFBMWZ5NUdmVUI0R3k5RGlsR3VIeTFHaUxpaW9hUDJ6RVBsUk9Ba19yNWJtaHNEMEhUWFBlenl4VDRfdkZOWFVSN1NyZ1ZJOEFPaXhO?oc=5
- https://news.google.com/rss/articles/CBMi9wFBVV95cUxQN2hoa0N6RHhWNk5wRDluYlZRdXhkeWl6bFg0VGUyaEdxU0F2VnBUOTNKZklPcjJmU01XMFBPZmpRX3R0a2tuVUJfbjFiTWptNUNQNml0VjlpWWJPWEVsdHprdnNMdk5tMmY0TVhkRHBMVE9acVlyS2QtTEZ6cDBJQkpnUXNERThmQ2ttSWtBSUd5RTJOdDVBSU0zdUNNV2VvTDMyVUEzSDFwZERrbXdaVDhuSEFNS2dYenhvdUVjZGpoTXFoOG1QejBicGN6S1FDQUM2N29WY0RZb0JGTFV1cUctYmprNXprNkJBRWsydEstWUEyNk4w?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNajRldVoxRV8wYjQyeHp5V09OdVhIN2tqdlR0RDFZVmoyWXQ3M3o5QWhUVTUtREY3QWlkRFJEMmxnLVFMeE4wUTNGaHRkZXdkWm9nX0NnY3JpQkVpMmliWW1QenhxQ09IeUpHQ0lsRDRiNFhFLUg5QlR2SXdCTl9WV2dFbVJEM09MVGNjcDNJWTNUU2VCWGE0bDhRaFZSc1JNZnd5N1BpNWd2bXBCMVhFXzc5eFd4S29DUm9tYmtvTzROdw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOa2dUZmEwdWxkaGVCUnB0SVNTTWU3ekl0M2lEcDk4TDhTNFpva1h5RHpqWkw0V1dZOElLa1E3RENvQ3FxNGx4cnVfSVNjNHpzbkxVU1JrRXh6UmxOR2w3eUV1QkhuQU15ZEhtM21PQkN4Ukd6aGhYZGU4aXNic0pHTGlMQ0lETVZpSWVISWN3YmR6VkJ0RkZmaw?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNQ2Z3Ym1zQlk0YUJsd01EWm53aFhPcDJJZXI3V3cyeUhhbDhqWnk4bEMybHh4NWRxT2FDdlh2SjVDSGlPUXRZNXFwbWFfaXZkSnczaEd6d3RRS0ctb1NFdkpIUzF1T1IwUWUyeGVXdVIyMTRWeVhpNTBfYzNhenNKc3NWYm1fV2dhWXhtZzRNSlU3X1EzVVlJMjM3aUc1OUZTTlN6V2Q2V1d4QjlkV0FCVzk4U2xKRGJKR1pudHFJYTFteFYxVEg5MHkzRUk?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxPMEJnU0FpNlBIQVVrY3RZWkxwVzV5a0RJajBPLWpIZW5DX1Y1cDBuZnJsWU14dHBGcGV3aE9LRkx6aVg4VDRjVHB1UmphaWN1VVJCQVQ1bEhnel9rTnNzSmZVZUJlTHZsTHVsdWpmZjM2aHQ1R09mZEZTUVpqbV9VZ18tMC15WkhxOW5PN2FtNHRXMHkwUndMV3NBQVZtaGNKajVzZkZfMWNwd0pYS21Ea0ZBNkZtUQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPMVBzSG9mMFpkNllsM3k3aXJmRXBYdThOWEpTRER6MTZ4WnNZZ1NGQkV1OFpBamtxY052ZWljS2U2cE1xSkhzaHRHdl9ZNmQ0eldwY1I3RGdfemhmVG5iNTl6LVBZYWg0aExuWDBXWW5vVmh5V1JsVlV0d0ZHeUFELTh0OGY4SmQzVXhpNXZ0dWhwUHR5UDFWNA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
