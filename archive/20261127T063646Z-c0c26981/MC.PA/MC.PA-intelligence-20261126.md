# MC.PA Intelligence Report

- ticker: **MC.PA**
- Report as_of: **2026-11-26**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/MC.PA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MC.PA/key-statistics/
- AI analysis snapshot as_of: **2026-11-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-27T06:54:42.119509+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 10, 'rule': 0, 'ai': 2, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261126T064454Z-dbdd6f45/MC.PA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 10 unique headlines; 4 named publishers; 0 exact duplicates; 10 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-11-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 391.0000 |
| Return 1D (%) | -0.9374 |
| Return 1W (%) | 0.7472 |
| Return 1M (%) | 2.0888 |
| Return YTD (%) | -38.3914 |
| Return 1Y (%) | -35.2809 |
| Annualized volatility (%) | 27.2114 |
| Beta vs SPY | 0.4490 |
| Max drawdown (%) | -41.0025 |
| Sharpe (rf=0) | -1.4429 |
| Downside deviation (rf=0, %) | 20.6835 |
| Sortino (rf=0) | -1.8983 |
| Historical VaR 95% (1D, %) | 2.7546 |
| Historical ES 95% (1D, %) | 3.9949 |
| Correlation vs SPY | 0.2479 |
| Tracking error vs SPY (%) | 27.6087 |
| P/E (trailing) | 18.05 |
| P/B | 2.90 |
| EV/EBITDA | 11.18 |
| Revenue growth (%) | -2.90 |
| Forward P/E (estimate) | 16.78 |
| Gross margin (%) | 66.36 |
| Operating margin (%) | 21.82 |
| Return on equity (%) | 16.59 |
| Free cash flow yield (%) | 5.86 |
| MA50 | 393.5340 |
| Close vs MA50 (%) | -0.6439 |
| MA200 | 454.2101 |
| Close vs MA200 (%) | -13.9165 |
| RSI (14, Wilder) | 46.3872 |
| MACD (12,26) | -1.7352 |
| MACD signal (9) | -0.6032 |
| MACD histogram | -1.1319 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MC.PA': 294, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 391.0000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.9374 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.7472 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.0888 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -38.3914 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -35.2809 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 27.2114 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.6835 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.8983 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.7546 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9949 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2479 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 27.6087 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4490 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -41.0025 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.4429 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.7770 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 66.3650 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 21.8230 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 16.5860 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 5.8633 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.0491 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 46.3872 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.1319 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.6439 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -13.9165 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### LVMH stock: BofA cuts target to EUR 500, keeps Buy rating
- Summary: Bank of America lowers LVMH price target to €500 while maintaining a Buy recommendation, signaling a more cautious outlook.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOMlZEX3VVNURScDR4UXpxelF3R09tQXdxekhrcVpIa29VY2RlUXZvN2FXWXJremU4LWJUd0c4ampzZmJoUkhlTEVWZjZ6dmh2NlM5dUpQc0tqVFVIc2I3NVd6UTZxdmxSNHpVemNUcnZfRGxtX09lalBBYlZzQjB6VDZyd3ZjRmgydnYtelExSkdDQTlGMFAxbklHZUdYU3pWRkJrbjBuZjRfZW5GSmNfa0VIQ0ZSTURicXc?oc=5>

### LVMH stock: Oddo BHF trims target as luxury outlook stays tough
- Summary: Oddo BHF reduces its price target for LVMH amid a challenging luxury market, reflecting a more conservative view.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxOWHN5ejVhTWdyYjFsVGRZbnNDLU14c29PN1BieXdaLTlLYjJTMVZ3ODNGMThyYU5CMWpsa0dwdzJsZ05JVVRtXzcwLWdFNXJZLWRaaDZGd3BNY2JVWGp1N2F1T2gzUlBHWVIySUVNbm1BWk9PQ1Q0elg1OFNYTlh3OVNmNEg4dk9KbmZuOXBCUC02dzVEMkcyUEZzSVpOWXdqWjJQa3ZjbDBDNU5hc1VrY2s2U0QzenpuVTBLNzJpbHRkc1E?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MC.PA** | **18.05** | **2.90** | **11.18** | **-2.90** | **196,767,219,712.00 EUR** | **-35.28** |
| RMS.PA | 29.54 | 7.01 | 17.47 | 1.60 | 133,107,294,208.00 EUR | -40.52 |
| CFR.SW | 26.09 | 4.67 | 16.01 | 15.70 | 101,096,333,312.00 CHF | 3.90 |
| KER.PA | N/A | 1.51 | 12.76 | -2.90 | 21,819,136,000.00 EUR | -39.87 |

Peers fetched as_of: 2026-11-26; MC.PA reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: N/A
- Next expected earnings: 2027-01-26 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-26

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

- https://news.google.com/rss/articles/CBMiugFBVV95cUxOMlZEX3VVNURScDR4UXpxelF3R09tQXdxekhrcVpIa29VY2RlUXZvN2FXWXJremU4LWJUd0c4ampzZmJoUkhlTEVWZjZ6dmh2NlM5dUpQc0tqVFVIc2I3NVd6UTZxdmxSNHpVemNUcnZfRGxtX09lalBBYlZzQjB6VDZyd3ZjRmgydnYtelExSkdDQTlGMFAxbklHZUdYU3pWRkJrbjBuZjRfZW5GSmNfa0VIQ0ZSTURicXc?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxOWHN5ejVhTWdyYjFsVGRZbnNDLU14c29PN1BieXdaLTlLYjJTMVZ3ODNGMThyYU5CMWpsa0dwdzJsZ05JVVRtXzcwLWdFNXJZLWRaaDZGd3BNY2JVWGp1N2F1T2gzUlBHWVIySUVNbm1BWk9PQ1Q0elg1OFNYTlh3OVNmNEg4dk9KbmZuOXBCUC02dzVEMkcyUEZzSVpOWXdqWjJQa3ZjbDBDNU5hc1VrY2s2U0QzenpuVTBLNzJpbHRkc1E?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
