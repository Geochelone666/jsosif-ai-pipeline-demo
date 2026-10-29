# SCHW Intelligence Report

- ticker: **SCHW**
- Report as_of: **2026-10-28**
- Market data as_of: **2026-10-28**
- Quant sources: https://finance.yahoo.com/quote/SCHW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SCHW/key-statistics/
- AI analysis snapshot as_of: **2026-10-28**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-29T02:02:22.918347+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 15, 'rule': 0, 'ai': 6, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261028T015717Z-533e470c/SCHW** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 15 unique headlines; 4 named publishers; 0 exact duplicates; 15 HTTPS source links; largest publisher share 66.67%; oldest publication 2026-10-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 88.7600 |
| Return 1D (%) | -0.6047 |
| Return 1W (%) | -3.1427 |
| Return 1M (%) | -9.7050 |
| Return YTD (%) | -10.2793 |
| Return 1Y (%) | -4.2147 |
| Annualized volatility (%) | 25.4512 |
| Beta vs SPY | 0.4209 |
| Max drawdown (%) | -21.9006 |
| Sharpe (rf=0) | -0.0416 |
| Downside deviation (rf=0, %) | 19.6526 |
| Sortino (rf=0) | -0.0539 |
| Historical VaR 95% (1D, %) | 2.5523 |
| Historical ES 95% (1D, %) | 3.9505 |
| Correlation vs SPY | 0.2101 |
| Tracking error vs SPY (%) | 25.9480 |
| P/E (trailing) | 15.28 |
| P/B | 2.98 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 16.90 |
| Forward P/E (estimate) | 11.38 |
| Gross margin (%) | 97.51 |
| Operating margin (%) | 52.67 |
| Return on equity (%) | 21.12 |
| Free cash flow yield (%) | N/A |
| MA50 | 101.3568 |
| Close vs MA50 (%) | -12.4282 |
| MA200 | 97.3093 |
| Close vs MA200 (%) | -8.7857 |
| RSI (14, Wilder) | 27.0853 |
| MACD (12,26) | -3.3024 |
| MACD signal (9) | -3.1263 |
| MACD histogram | -0.1761 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SCHW': 270, 'SPY': 270}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 88.7600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.6047 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.1427 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -9.7050 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -10.2793 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -4.2147 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.4512 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 19.6526 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.0539 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5523 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9505 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2101 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 25.9480 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4209 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -21.9006 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.0416 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.3810 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.5060 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 52.6700 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 21.1220 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 15.2771 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 27.0853 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1761 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -12.4282 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -8.7857 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### The Charles Schwab Corporation $SCHW Stock Sold by Mondrian Investment Partners LTD
- Summary: Shares of SCHW sold by Mondrian Investment Partners LTD, indicating a market transaction involving the company’s stock.
- Date: 2026-10-25 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxNYWRzYS1KY2ZtRW0tenNIb1BzT0NCVXBlTWREOGc4NEdxYkpTSjBVbGRhVVFyU2hOYmxrd0pGd3JIODU2NlFqazgzZHdWUHo1a2FBLVEwWDZBWDgtMUxkQ1lDejZQYXJyakdONU02TmpBT2NDV3FRTXJoYnF2b21NNVgxa3FNMmNLOEE1QkV0M1VPNkJVSGNFclhQQTFTM0FkUlliWlBLdTdNYTVSMFpEdEFVbGlCbkpfZDE4SWV6c1NaUldmVXZkSHo5VGg3WGRTNlp1bU9WMmtoejA?oc=5>

### SCHW 261030 100.00P (SCHW261030P100000) Stock Options Chain | Quotes & News
- Summary: Charles Schwab option chain for 26/10/2026, 100.00 strike put. Indicates potential bearish sentiment or hedging activity.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiYEFVX3lxTE44X2d0Vk4zcXJKMXBfajRvYkNVR0Z6bTBuWDB6Ykw2cVRLNk9CT09IdXFQREppYXhRV1I1T0xtTmZkX3Q5Zkd0VllHS3VZRElVcmc0TXdXR3pTeU9Bck1XWA?oc=5>

### Traders Purchase Large Volume of Charles Schwab Put Options (NYSE:SCHW)
- Summary: Large volume of Schwab puts purchased, suggesting bearish outlook or hedging by traders.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxQNWNsTnlVYi1PdUVFSXJyNkV1ODk4SEN2XzJPTUdtSEdwc28wMTdWLVJZTVQ4ZnhTRDFqM0RjVmhMbl9qOXo1M2dUZHllMEQ3ZXVxYlZweVM1WEw4QUI3MkNtWmxyTkpuNmdMT051YWxHR3BZWExTTXRPR1BhLTVwN3F2LUpzVldpZVpZaHBCWjlCMTRxNHNiaGFZTEhwTXYtRGxwa3UteVM4cTJtUEdPMVZkekc0bHBmXzB6WnlKdE93VjZUR1lZcDZUUQ?oc=5>

### Advisers can now ask Claude about Schwab client accounts
- Summary: Advisers can query Claude AI about Schwab client accounts, enhancing advisory services.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxQSl9GZUQtcEpITVdQRUZUVkpWbWVzLXhTWmZoQjBxSzc1TXhUcnkzeU9VX0JKaXh3eHhJeVZPYzVqNnRCN01nNUdLekEwVi15VHotSlg3bDlfbDZHaVpQbXphby0yeFRnckljRHlpbGx6Qjh1dGhjSUhLdXlwXzBmYmJFMngxZTNqSGl3N0tRc3ZjU2FEMG1aS0M1Sk5GcDczUDlaTTQzM3pXOF96c0F6cUZ5al84MXBIZmlzRlJn?oc=5>

### SCHW 261023 82.00P (SCHW261023P82000) Stock Options Chain | Quotes & News
- Summary: Option chain for 26/10/2023, 82.00 strike put, indicating potential downside view.
- Date: 2026-10-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiX0FVX3lxTE9TSUh1NFIzYXJzSS1FeUpGa0doV0kwQjQxa2hkTEkySnFHOXFDVXQyVnRyR01KLTF6QnM1S2Q0SXdDSnRaYnRsTlZ6RjNiMzZxOHhWcVNSd1hBNFUyUVNn?oc=5>

### SCHW 261023 117.00P (SCHW261023P117000) Stock Options Chain | Quotes & News
- Summary: Option chain for 26/10/2023, 117.00 strike put, reflecting bearish positioning.
- Date: 2026-10-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiYEFVX3lxTFBHT2hZZ282TkRWYVVHYmduTmV2bTZZWTFwTWxJOGVEWm94NkdhemtwZzNLbll2UzN0cWtXTmxRRXBwWGs5TGhwcGJYR29LSDNMcWVoTnQtOG9oZUs0WlRWMw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SCHW** | **15.28** | **2.98** | **N/A** | **16.90** | **153,495,830,528.00 USD** | **-4.21** |
| IBKR | 31.41 | 6.08 | N/A | 13.50 | 142,336,753,664.00 USD | 22.20 |
| HOOD | 41.75 | 9.02 | N/A | 32.30 | 82,203,099,136.00 USD | -37.48 |
| LPLA | 25.28 | 4.03 | N/A | 36.40 | 21,196,636,160.00 USD | -21.26 |

Peers fetched as_of: 2026-10-28; SCHW reuses existing data (market data as_of: 2026-10-28); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

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
- Filing date: 2026-08-07
- Revenue (latest available single quarter): 7,072,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 2,800,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/316709/000031670926000031/schw-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi2wFBVV95cUxNYWRzYS1KY2ZtRW0tenNIb1BzT0NCVXBlTWREOGc4NEdxYkpTSjBVbGRhVVFyU2hOYmxrd0pGd3JIODU2NlFqazgzZHdWUHo1a2FBLVEwWDZBWDgtMUxkQ1lDejZQYXJyakdONU02TmpBT2NDV3FRTXJoYnF2b21NNVgxa3FNMmNLOEE1QkV0M1VPNkJVSGNFclhQQTFTM0FkUlliWlBLdTdNYTVSMFpEdEFVbGlCbkpfZDE4SWV6c1NaUldmVXZkSHo5VGg3WGRTNlp1bU9WMmtoejA?oc=5
- https://news.google.com/rss/articles/CBMiYEFVX3lxTE44X2d0Vk4zcXJKMXBfajRvYkNVR0Z6bTBuWDB6Ykw2cVRLNk9CT09IdXFQREppYXhRV1I1T0xtTmZkX3Q5Zkd0VllHS3VZRElVcmc0TXdXR3pTeU9Bck1XWA?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxQNWNsTnlVYi1PdUVFSXJyNkV1ODk4SEN2XzJPTUdtSEdwc28wMTdWLVJZTVQ4ZnhTRDFqM0RjVmhMbl9qOXo1M2dUZHllMEQ3ZXVxYlZweVM1WEw4QUI3MkNtWmxyTkpuNmdMT051YWxHR3BZWExTTXRPR1BhLTVwN3F2LUpzVldpZVpZaHBCWjlCMTRxNHNiaGFZTEhwTXYtRGxwa3UteVM4cTJtUEdPMVZkekc0bHBmXzB6WnlKdE93VjZUR1lZcDZUUQ?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxQSl9GZUQtcEpITVdQRUZUVkpWbWVzLXhTWmZoQjBxSzc1TXhUcnkzeU9VX0JKaXh3eHhJeVZPYzVqNnRCN01nNUdLekEwVi15VHotSlg3bDlfbDZHaVpQbXphby0yeFRnckljRHlpbGx6Qjh1dGhjSUhLdXlwXzBmYmJFMngxZTNqSGl3N0tRc3ZjU2FEMG1aS0M1Sk5GcDczUDlaTTQzM3pXOF96c0F6cUZ5al84MXBIZmlzRlJn?oc=5
- https://news.google.com/rss/articles/CBMiX0FVX3lxTE9TSUh1NFIzYXJzSS1FeUpGa0doV0kwQjQxa2hkTEkySnFHOXFDVXQyVnRyR01KLTF6QnM1S2Q0SXdDSnRaYnRsTlZ6RjNiMzZxOHhWcVNSd1hBNFUyUVNn?oc=5
- https://news.google.com/rss/articles/CBMiYEFVX3lxTFBHT2hZZ282TkRWYVVHYmduTmV2bTZZWTFwTWxJOGVEWm94NkdhemtwZzNLbll2UzN0cWtXTmxRRXBwWGs5TGhwcGJYR29LSDNMcWVoTnQtOG9oZUs0WlRWMw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
