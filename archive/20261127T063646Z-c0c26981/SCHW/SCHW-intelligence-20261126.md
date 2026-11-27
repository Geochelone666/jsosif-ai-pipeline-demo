# SCHW Intelligence Report

- ticker: **SCHW**
- Report as_of: **2026-11-26**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/SCHW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SCHW/key-statistics/
- AI analysis snapshot as_of: **2026-11-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-27T06:39:06.620658+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 1, 'rule': 0, 'ai': 1, 'unknown': 0})
- AI model(s) actually used: **N/A (no successful AI classification call)**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261126T064454Z-dbdd6f45/SCHW** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 1 unique headlines; 1 named publishers; 0 exact duplicates; 1 HTTPS source links; largest publisher share 100.0%; oldest publication 2026-11-25

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 93.4500 |
| Return 1D (%) | -0.4898 |
| Return 1W (%) | 0.9615 |
| Return 1M (%) | 3.5297 |
| Return YTD (%) | -5.2078 |
| Return 1Y (%) | 4.3717 |
| Annualized volatility (%) | 25.8834 |
| Beta vs SPY | 0.4250 |
| Max drawdown (%) | -22.5253 |
| Sharpe (rf=0) | 0.2962 |
| Downside deviation (rf=0, %) | 19.4370 |
| Sortino (rf=0) | 0.3945 |
| Historical VaR 95% (1D, %) | 2.5277 |
| Historical ES 95% (1D, %) | 3.9438 |
| Correlation vs SPY | 0.2451 |
| Tracking error vs SPY (%) | 26.5216 |
| P/E (trailing) | 15.97 |
| P/B | 3.56 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 16.90 |
| Forward P/E (estimate) | 11.99 |
| Gross margin (%) | 97.51 |
| Operating margin (%) | 51.11 |
| Return on equity (%) | 21.11 |
| Free cash flow yield (%) | N/A |
| MA50 | 94.1811 |
| Close vs MA50 (%) | -0.7763 |
| MA200 | 95.9542 |
| Close vs MA200 (%) | -2.6098 |
| RSI (14, Wilder) | 52.7603 |
| MACD (12,26) | -0.2481 |
| MACD signal (9) | -0.7124 |
| MACD histogram | 0.4643 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SCHW': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 93.4500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.4898 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.9615 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.5297 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -5.2078 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 4.3717 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.8834 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 19.4370 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3945 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5277 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9438 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2451 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.5216 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4250 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -22.5253 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2962 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.9861 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.5060 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 51.1070 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 21.1130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 15.9744 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 52.7603 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.4643 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.7763 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -2.6098 -> Slightly below the moving-average trend level.

## TAILWINDS

### Does AI Trading Tools Change The Bull Case For Schwab (SCHW)?
- Summary: Analyst question on AI tools' impact on Schwab's valuation.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxPR3VXVUtaNm15WjlnTTI5b2VfbWE4UlB1dlRmYWhobzdCVGZIV2M2SjU5MkpXUDVNdTdtU1N3V3ZpSWtqUVN6aW1YLUo1ZjNaQ0EyRUpYVnN1aGI0MGFrSlprelhZQnFvRGpyZ25aZkpuMlp2WlJuOFNKN2pKOHdkQXJBenFaMGRCOXppNExBRWNQRlNqcmx4NXYzWW1ReWNoTjhmNHBJLXNYeVA1T21iZVNfYUVyUFlJeGhUYW9venRnbjFENnpPamQ1eHRabFVUYlNQd1VUajNqX1HSAeABQVVfeXFMT0lVUWVqNExXM1lEVHZEd1NIenoxX2tYc0l4SGxSYWR2QnVyVmxHMnRMcDMtakpJQlQyU3h0MEtqZWRZOTRZZnBfNkpTWHhmOURCT19YX3N3bGF1dkNaVkJGMHNWSGZoTFhYUm9TYTRqdEJ2ZzFDVm5mWG5FN1R5OVBZbFEwZ3ZTdzFBeURZdDBxS2tzVWFCcERJUDU0dk9mNndSd1RQa3VSLVhlLUNoWktpNEowNlk2ZkFhTGdSUWY2SzY0cXVONXAzSXhIWTFzRDhtamNEUjViZVlwVVpEZlg?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

No items in this run

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SCHW** | **15.97** | **3.56** | **N/A** | **16.90** | **161,295,417,344.00 USD** | **4.37** |
| IBKR | 28.53 | 5.45 | N/A | 13.50 | 127,345,082,368.00 USD | 18.82 |
| HOOD | 30.31 | 5.93 | N/A | 11.80 | 59,234,316,288.00 USD | -43.08 |
| LPLA | 15.79 | 3.71 | N/A | 17.80 | 21,450,412,032.00 USD | -20.63 |

Peers fetched as_of: 2026-11-26; SCHW reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-06
- Revenue (latest available single quarter): 7,171,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 2,906,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/316709/000031670926000038/schw-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi2wFBVV95cUxPR3VXVUtaNm15WjlnTTI5b2VfbWE4UlB1dlRmYWhobzdCVGZIV2M2SjU5MkpXUDVNdTdtU1N3V3ZpSWtqUVN6aW1YLUo1ZjNaQ0EyRUpYVnN1aGI0MGFrSlprelhZQnFvRGpyZ25aZkpuMlp2WlJuOFNKN2pKOHdkQXJBenFaMGRCOXppNExBRWNQRlNqcmx4NXYzWW1ReWNoTjhmNHBJLXNYeVA1T21iZVNfYUVyUFlJeGhUYW9venRnbjFENnpPamQ1eHRabFVUYlNQd1VUajNqX1HSAeABQVVfeXFMT0lVUWVqNExXM1lEVHZEd1NIenoxX2tYc0l4SGxSYWR2QnVyVmxHMnRMcDMtakpJQlQyU3h0MEtqZWRZOTRZZnBfNkpTWHhmOURCT19YX3N3bGF1dkNaVkJGMHNWSGZoTFhYUm9TYTRqdEJ2ZzFDVm5mWG5FN1R5OVBZbFEwZ3ZTdzFBeURZdDBxS2tzVWFCcERJUDU0dk9mNndSd1RQa3VSLVhlLUNoWktpNEowNlk2ZkFhTGdSUWY2SzY0cXVONXAzSXhIWTFzRDhtamNEUjViZVlwVVpEZlg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
