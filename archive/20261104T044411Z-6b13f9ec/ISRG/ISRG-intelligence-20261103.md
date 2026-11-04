# ISRG Intelligence Report

- ticker: **ISRG**
- Report as_of: **2026-11-03**
- Market data as_of: **2026-11-03**
- Quant sources: https://finance.yahoo.com/quote/ISRG/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ISRG/key-statistics/
- AI analysis snapshot as_of: **2026-11-03**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-04T04:58:04.619853+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 16, 'rule': 1, 'ai': 4, 'unknown': 0, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261103T051441Z-8b1c85d8/ISRG** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 16 unique headlines; 10 named publishers; 1 exact duplicates; 16 HTTPS source links; largest publisher share 18.75%; oldest publication 2026-10-28

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 440.7500 |
| Return 1D (%) | 0.8881 |
| Return 1W (%) | -1.1505 |
| Return 1M (%) | 12.4506 |
| Return YTD (%) | -22.1785 |
| Return 1Y (%) | -19.0110 |
| Annualized volatility (%) | 34.1099 |
| Beta vs SPY | 0.8874 |
| Max drawdown (%) | -43.9960 |
| Sharpe (rf=0) | -0.4476 |
| Downside deviation (rf=0, %) | 25.8340 |
| Sortino (rf=0) | -0.5909 |
| Historical VaR 95% (1D, %) | 2.9944 |
| Historical ES 95% (1D, %) | 5.1080 |
| Correlation vs SPY | 0.3330 |
| Tracking error vs SPY (%) | 32.1956 |
| P/E (trailing) | 52.85 |
| P/B | 9.56 |
| EV/EBITDA | 33.30 |
| Revenue growth (%) | 21.70 |
| Forward P/E (estimate) | 35.35 |
| Gross margin (%) | 66.64 |
| Operating margin (%) | 33.29 |
| Return on equity (%) | 17.93 |
| Free cash flow yield (%) | 2.21 |
| MA50 | 404.0480 |
| Close vs MA50 (%) | 9.0836 |
| MA200 | 432.0674 |
| Close vs MA200 (%) | 2.0095 |
| RSI (14, Wilder) | 58.5615 |
| MACD (12,26) | 10.4991 |
| MACD signal (9) | 11.9712 |
| MACD histogram | -1.4721 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ISRG': 274, 'SPY': 274}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 440.7500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.8881 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.1505 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 12.4506 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -22.1785 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -19.0110 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.1099 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.8340 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.5909 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9944 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1080 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3330 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.1956 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8874 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.9960 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.4476 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 35.3483 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 66.6420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.2860 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.9320 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.2059 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 52.8477 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 58.5615 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.4721 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 9.0836 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 2.0095 -> Slightly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Intuitive Surgical (ISRG) Insider Sale: EVP & Chief Manufacturin
- Summary: Intuitive Surgical (ISRG) Insider Sale: EVP & Chief Manufacturin
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxNWVJYSW1jTHdXXzAzSFBJUFU2WEpORGhMaEhLdTZsZjhOS0hYY0d2SklxSXpQbWNDUUktRV90SjhUeWhyTi1WblNWZHlJTkhwNHU5TDZ6akM5YkozNlh6VnQ4Zk0tMkRINzNjYTRjcUQyeG9qOHR6Y0ZJRExLWlJHWFJrS2dZVFFnMzFmemVwV0RVTHozOU5uZElKY0JEYlpqOWwtTFA5Yk93aG55SEE2RGV1TUR1dGpRT3lZN2JEclRUMXdEZzBLblpfRFdGd3hnZ0RKaG5fUjEtalp4VkxZZE5FeHppV2FPWnJj?oc=5>

### Intuitive Surgical Stock Just Fell Despite a 22% Revenue Jump. Here's What Investors Are Missing.
- Summary: Stock decline amid strong revenue, indicating market skepticism.
- Date: 2026-11-01 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOVzVGQXhQVHBIdmRpcGgweEFJNVhUWFpEZVdYYk1CelFJMmVpM29pOV8zREhFWWJSU2Y5QXNSX3JIM1FOS2poUjFaSTFCdm05YlJFbVltV1A4Q0gzNml3bUYwOUFZWWdTNFNLbktxLS04WVJQOEtfZDQ1MmdiVnppbU50VWhYa01yb2VvU3ZvVllzeG92VUZzOA?oc=5>

### Is Intuitive Surgical Inc (ISRG) a Bargain After 3.7% Drop? GF V
- Summary: Shares fell 3.7%, prompting a price‑drop analysis.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxNTXJ1bkY2UUZ6NFhHMTR2c0VpUUhBS0tPcFNGeDNvOC1BVndCaWx2c3RiSF95eUFCTEZqTFhBS2czZnplMFpISGcwQjlQZGo2dDhURjVucnJkT0xzZFM2cFlzNE1mR1hDdWc4MDR2M3lOS2xndWJpQWFWNE9iRUxRUEhtTXdBbDFMbzRoYVhlMy1uZkp0Tm1GQmdSSDFuRzNvVmR1M0xoVGFwZkVQU1VmYVpLZlBPdXF4LW5j?oc=5>

### A controller exercises options and sells 5,448 shares at Intuitive Surgical (ISRG).
- Summary: Controller’s option exercise and share sale may signal insider activity.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxONF9tNi1nT1ptbXprVlQwcWtaVTI0Z0QzeXV2MHNLMGxmWmNDR09zOVJRQ3NHWUtSREx6TWZtNnJpQ2dfZENNQi04UllkM1pEd2poU2wtc2FGSTMtWmdMa3pod0dNbFItVDlGUDlkZ3hHYlh1U2ptZzFiYnZZanVEZlhUT0R0M1VQMjhvaUlGc1pQQjdZSncxMXZnWVhYUVZjclFrS09kYkhnXzMyYXpKQk9CbjlJd2s?oc=5>

## RISKS

### Is This Number The Biggest Risk To Intuitive Surgical Stock?
- Summary: Questioning a key risk factor for ISRG, potentially affecting investor confidence.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPM3g0TU1KTFdMLXpCSmJXTjVybXNkdlNDcW1UY2RvdmxnSksya3JxME0wVGxqaDFKTU51UUV2QUVlbm1QTThsRUI0YTUyNTFSMnIzNlU3N0R3cW4yLWZ4aUdWd1N2OGR2NEZiMnVRaUlBNXAyMUlsM3dNVi1pdmV3Nmd4T1A5Z3ZGTVFVYlNubTQ4Ym5uOVNwVnhFYVdRUDdrNlFjV21HZS12OE9VUFVSZkJ2Y25EWlBOdm5CLQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ISRG** | **52.85** | **9.56** | **33.30** | **21.70** | **155,707,293,696.00 USD** | **-19.01** |
| MDT | 24.41 | 2.52 | 14.07 | 13.70 | 126,481,154,048.00 USD | 13.26 |
| SYK | 32.69 | 5.04 | 17.36 | 7.60 | 118,223,585,280.00 USD | -12.33 |
| BSX | 18.67 | 2.52 | 13.24 | 1.40 | 63,041,486,848.00 USD | -55.88 |

Peers fetched as_of: 2026-11-03; ISRG reuses existing data (market data as_of: 2026-11-03); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 3,048,700,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 522,800,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1035267/000103526726000071/isrg-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi6wFBVV95cUxNWVJYSW1jTHdXXzAzSFBJUFU2WEpORGhMaEhLdTZsZjhOS0hYY0d2SklxSXpQbWNDUUktRV90SjhUeWhyTi1WblNWZHlJTkhwNHU5TDZ6akM5YkozNlh6VnQ4Zk0tMkRINzNjYTRjcUQyeG9qOHR6Y0ZJRExLWlJHWFJrS2dZVFFnMzFmemVwV0RVTHozOU5uZElKY0JEYlpqOWwtTFA5Yk93aG55SEE2RGV1TUR1dGpRT3lZN2JEclRUMXdEZzBLblpfRFdGd3hnZ0RKaG5fUjEtalp4VkxZZE5FeHppV2FPWnJj?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOVzVGQXhQVHBIdmRpcGgweEFJNVhUWFpEZVdYYk1CelFJMmVpM29pOV8zREhFWWJSU2Y5QXNSX3JIM1FOS2poUjFaSTFCdm05YlJFbVltV1A4Q0gzNml3bUYwOUFZWWdTNFNLbktxLS04WVJQOEtfZDQ1MmdiVnppbU50VWhYa01yb2VvU3ZvVllzeG92VUZzOA?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxNTXJ1bkY2UUZ6NFhHMTR2c0VpUUhBS0tPcFNGeDNvOC1BVndCaWx2c3RiSF95eUFCTEZqTFhBS2czZnplMFpISGcwQjlQZGo2dDhURjVucnJkT0xzZFM2cFlzNE1mR1hDdWc4MDR2M3lOS2xndWJpQWFWNE9iRUxRUEhtTXdBbDFMbzRoYVhlMy1uZkp0Tm1GQmdSSDFuRzNvVmR1M0xoVGFwZkVQU1VmYVpLZlBPdXF4LW5j?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxONF9tNi1nT1ptbXprVlQwcWtaVTI0Z0QzeXV2MHNLMGxmWmNDR09zOVJRQ3NHWUtSREx6TWZtNnJpQ2dfZENNQi04UllkM1pEd2poU2wtc2FGSTMtWmdMa3pod0dNbFItVDlGUDlkZ3hHYlh1U2ptZzFiYnZZanVEZlhUT0R0M1VQMjhvaUlGc1pQQjdZSncxMXZnWVhYUVZjclFrS09kYkhnXzMyYXpKQk9CbjlJd2s?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPM3g0TU1KTFdMLXpCSmJXTjVybXNkdlNDcW1UY2RvdmxnSksya3JxME0wVGxqaDFKTU51UUV2QUVlbm1QTThsRUI0YTUyNTFSMnIzNlU3N0R3cW4yLWZ4aUdWd1N2OGR2NEZiMnVRaUlBNXAyMUlsM3dNVi1pdmV3Nmd4T1A5Z3ZGTVFVYlNubTQ4Ym5uOVNwVnhFYVdRUDdrNlFjV21HZS12OE9VUFVSZkJ2Y25EWlBOdm5CLQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
