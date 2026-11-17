# T Intelligence Report

- ticker: **T**
- Report as_of: **2026-11-16**
- Market data as_of: **2026-11-16**
- Quant sources: https://finance.yahoo.com/quote/T/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/T/key-statistics/
- AI analysis snapshot as_of: **2026-11-16**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-17T06:41:14.670828+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 16, 'rule': 1, 'ai': 7, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261116T043911Z-b81cfeb4/T** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 16 unique headlines; 8 named publishers; 0 exact duplicates; 16 HTTPS source links; largest publisher share 43.75%; oldest publication 2026-11-10

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 22.3600 |
| Return 1D (%) | 0.8115 |
| Return 1W (%) | 2.5688 |
| Return 1M (%) | -4.6075 |
| Return YTD (%) | -5.6890 |
| Return 1Y (%) | -8.4531 |
| Annualized volatility (%) | 28.7073 |
| Beta vs SPY | -0.3523 |
| Max drawdown (%) | -28.8854 |
| Sharpe (rf=0) | -0.1487 |
| Downside deviation (rf=0, %) | 22.0129 |
| Sortino (rf=0) | -0.1939 |
| Historical VaR 95% (1D, %) | 2.8611 |
| Historical ES 95% (1D, %) | 4.6484 |
| Correlation vs SPY | -0.1690 |
| Tracking error vs SPY (%) | 33.8704 |
| P/E (trailing) | 11.96 |
| P/B | 1.42 |
| EV/EBITDA | 7.37 |
| Revenue growth (%) | 5.30 |
| Forward P/E (estimate) | 8.61 |
| Gross margin (%) | 59.74 |
| Operating margin (%) | 22.59 |
| Return on equity (%) | 11.61 |
| Free cash flow yield (%) | 7.94 |
| MA50 | 23.3639 |
| Close vs MA50 (%) | -4.2967 |
| MA200 | 24.3786 |
| Close vs MA200 (%) | -8.2803 |
| RSI (14, Wilder) | 50.7482 |
| MACD (12,26) | -0.2784 |
| MACD signal (9) | -0.4819 |
| MACD histogram | 0.2035 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'T': 283, 'SPY': 283}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 22.3600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.8115 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.5688 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -4.6075 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -5.6890 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -8.4531 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.7073 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.0129 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.1939 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8611 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6484 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1690 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.8704 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.3523 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.8854 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.1487 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.6139 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 59.7420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 22.5930 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.6130 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.9413 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 11.9572 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 50.7482 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2035 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -4.2967 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -8.2803 -> Clearly below the moving-average trend level.

## TAILWINDS

### AT&T stock gains 0.52% to EUR 20.18 before Xetra
- Summary: AT&T stock gains 0.52% to EUR 20.18 before Xetra
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQTG1Ub1RYSHoyRXpWZ2hBSmNsZENoNDAyVWFBNm0tdk1Jd3l1WE5peTlBazBwYm9kV3dzNTQ4eFFvSmZwWE1OX0NoeDE5cERXYjRuaTRteGxfdUlmd3VHRUhtMWpCSVlnQkdiZFdVcjduejlHTWYyVk8wT3luSUhWd2doRVh3bnRiNVA0ZVV1Q1N2dnlabnhZTjJFOF9NTXA5aHdhQTV0Y0s?oc=5>

### Could AT&T Be The Value Stock For Your Portfolio?
- Summary: Analyst opinion that AT&T may be a value investment for portfolios.
- Date: 2026-11-12 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPMy1qLUZsZVBUcDZ2UkRvelROOUFjUTZYM3dVajNvejlJOWNfZWd6QnpSTEVxUGRlUzY0LXNUaktXN2xjRmUtTVFxQW9ZM0JiYXNvN1F3bEFvZC1rc3Z3OGxBT0d6cy1DWGFwUGl1SlVXR1h1Q1E2R0dsaklnS3hPaHVqSHFfWk44M0ppM3U2RVpIT25VbDJNT19n?oc=5>

### Better High-Yield Dividend Stock: AT&T vs. General Mills
- Summary: Comparison of AT&T and General Mills as high-yield dividend stocks.
- Date: 2026-11-12 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQdjNvcTB0aUotSmlzTmdkMVFQZUR3cXVCczZHd3pRaXBJejlqTUZmOXNKUklFc3hpb1R6RW1DUF9jQm1BSUhPNGw1clBaREc3UU9JUzdYX1NCV0dRYmZnQ05SYVBUTHlCdjc3aml5QkpwczdVbkpJdkFqTEExZzc3RDFyZ0ZIUnlSTnl4QjBkaTB5ZFFSS2g3d3Q4WGFmdw?oc=5>

### Can AT&T (T) Turn Satellite Handoffs Into A Real Wireless Edge?
- Summary: Analysis of AT&T's satellite handoff technology as a potential edge.
- Date: 2026-11-15 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxON1BWQ3hUQ2xuQnJyVE9haU1leGlrZVBTUWE3bFVXYnNDUWVydG1TTmN0cVJqWXRaTDFkNERJTXZvV1JKUlNtb0xfQWdMVUxyZVZ2MGFoLXZNOHpQUXpCZmphRGhGOW9VZGFiaG1yZXB6bEMzcmF0VWV2VktOZlBlRlFtckt0WXJQZmJmdXV2SUVMQQ?oc=5>

### AT&T (T) Stock Looks Reasonable On Its 62% Three Year Run
- Summary: Assessment of AT&T's stock performance over three years.
- Date: 2026-11-15 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNeWlWTVNHb1JxQ3c0amtDcjNhZDlwTXFPd25YeXk0YUVhYlBCS3VDdXNlb2d1WUZqOS1mY2s4SThiMzhMUDJxUTJvOFRjdDZSa2xpOHl2b0Z3REEtb24zRlJZWUtqd1RYTVRxQ0c3SzFBNzgzWktqQ1RjX2NJNzVwZmNpQy00UHpVQmllcnNZWTJWYVNOYzZMeEppel9xc0FLemU0ajdLaXdoUk92OHfSAbMBQVVfeXFMTmxmZzB2LURENGF6VkxKbkt5SUgwdFUwMEJzZHJ6aHI5d3FzQ0Q1Vm0xLUZSd3QzQUluZmJxVi0zMzMtSTlDZUhvclY0ZzFtQVRPelJjQ0swb0xpSE5TbWFZZ2RmSVB4ZVVoaC1NNE5ZSHhsSHlTb28tRlliMERpOFlFQ0N2LTZQbXpvLWRZQ0h1VFJ3dzVPOHhyejBhVmVBUnBwdjIxM1RwRjRBLXRXdTZfSzA?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Verizon, AT&T and T-Mobile shut out Elon Musk’s phone service. Now the FCC is reviewing SpaceX’s plan to build its own
- Summary: AT&T participates in blocking Elon Musk’s service, prompting FCC review of SpaceX’s infrastructure plans.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQVzJFZFlzQmplRmxxcEtrRmlSUjk4anJsbUlBVlhjYURlZUQ2WmVmZm12dmgyd0lEdHVSakItcHZwM2pYQ3AtTTkxSER0cWRndEg5b3VBOUM2WXRyYWpVR0UwMGxBeWZwenRidWVrby15cFVfVGg2RVBQcjJrSHRWVk9jM2J5V0xzRDdGSw?oc=5>

### Better Dividend Stock for Retirees: AT&T vs. Air Products and Chemicals
- Summary: AT&T offers a more attractive dividend yield for retirees compared to Air Products, highlighting its stable cash flow and shareholder-friendly policy.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQclpGaFp1V2xJSjBXVDk0Mi1fUUtOZW5HeGtqU0hrd0RqRUZqRUE1allYY2VnNFA4emNCc21ldEZHLW9nb2NGSHJKdmRWTG80LVBLYXd5eDRlZEhYNUNuSzNQMl9ud1l0ZTBvWENFQ1A1emRTaVFvZ1FZNzRRREkwUHVsZFFYYnZHUUNmaGN5cW9LUjE2RTh4a0Z3?oc=5>

### AT&T (T) Has The Market Looking Closer, What Is Behind The Attention?
- Summary: Analysts are scrutinizing AT&T’s recent performance and strategic moves, potentially signaling upcoming guidance or market shifts.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxQQXk1aDczX2prZ3FwVC14bEhZa1YxVU5BYzNNMmZZcm00dFpJLW82QVBkcUFwZjNiZTc5ZGotWEZfbGMxTTBvbGpEdmlJRnp2SEt2RF9JZElha2lING1ySzdOT0lMWk1tYjZEODNuTGlyelk1Q0VXY3hPQ1NPV2xaRlJrNVAwcWtoUjRpYi1Ta29RYjVTdC1ORUk4TDBaN1FqNDA0ZFRBS1RQRV9PU2EwZlJyNGtLWDTSAbwBQVVfeXFMTktVTlJMc1dBSTA0LVVYRlJhRnpBXzBNeTdjdjh2WTFfOFJmMVBkRGpXcGs2d2I1aVFYbXhwbTZqQzlrSi1vT2YyN1BXVnRBbS1BaGVfSkE2Y3NiX1FfNzFuOEpnYzhDbUlnX0FXVzNxaW83MVY3a21tdWl3OTlyNjJZbmdjblVmQWFub3lkblN4ZFhnb2hGaFhmMzZmcnptWWxzS0dIOFpCWHh5R0ZQbEUxS29FdjBDbjVkd24?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **T** | **11.96** | **1.42** | **7.37** | **5.30** | **150,627,549,184.00 USD** | **-8.45** |
| VZ | 11.82 | 1.81 | 7.38 | 1.50 | 192,060,686,336.00 USD | 20.37 |
| TMUS | 16.39 | 3.21 | 8.30 | 7.40 | 180,086,931,456.00 USD | -19.66 |
| BCE | 11.96 | 1.39 | 7.43 | 2.20 | 20,636,794,880.00 USD | 2.13 |

Peers fetched as_of: 2026-11-16; T reuses existing data (market data as_of: 2026-11-16); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-16

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 32,322,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 891,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/732717/000073271726000372/t-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQTG1Ub1RYSHoyRXpWZ2hBSmNsZENoNDAyVWFBNm0tdk1Jd3l1WE5peTlBazBwYm9kV3dzNTQ4eFFvSmZwWE1OX0NoeDE5cERXYjRuaTRteGxfdUlmd3VHRUhtMWpCSVlnQkdiZFdVcjduejlHTWYyVk8wT3luSUhWd2doRVh3bnRiNVA0ZVV1Q1N2dnlabnhZTjJFOF9NTXA5aHdhQTV0Y0s?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPMy1qLUZsZVBUcDZ2UkRvelROOUFjUTZYM3dVajNvejlJOWNfZWd6QnpSTEVxUGRlUzY0LXNUaktXN2xjRmUtTVFxQW9ZM0JiYXNvN1F3bEFvZC1rc3Z3OGxBT0d6cy1DWGFwUGl1SlVXR1h1Q1E2R0dsaklnS3hPaHVqSHFfWk44M0ppM3U2RVpIT25VbDJNT19n?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQdjNvcTB0aUotSmlzTmdkMVFQZUR3cXVCczZHd3pRaXBJejlqTUZmOXNKUklFc3hpb1R6RW1DUF9jQm1BSUhPNGw1clBaREc3UU9JUzdYX1NCV0dRYmZnQ05SYVBUTHlCdjc3aml5QkpwczdVbkpJdkFqTEExZzc3RDFyZ0ZIUnlSTnl4QjBkaTB5ZFFSS2g3d3Q4WGFmdw?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxON1BWQ3hUQ2xuQnJyVE9haU1leGlrZVBTUWE3bFVXYnNDUWVydG1TTmN0cVJqWXRaTDFkNERJTXZvV1JKUlNtb0xfQWdMVUxyZVZ2MGFoLXZNOHpQUXpCZmphRGhGOW9VZGFiaG1yZXB6bEMzcmF0VWV2VktOZlBlRlFtckt0WXJQZmJmdXV2SUVMQQ?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNeWlWTVNHb1JxQ3c0amtDcjNhZDlwTXFPd25YeXk0YUVhYlBCS3VDdXNlb2d1WUZqOS1mY2s4SThiMzhMUDJxUTJvOFRjdDZSa2xpOHl2b0Z3REEtb24zRlJZWUtqd1RYTVRxQ0c3SzFBNzgzWktqQ1RjX2NJNzVwZmNpQy00UHpVQmllcnNZWTJWYVNOYzZMeEppel9xc0FLemU0ajdLaXdoUk92OHfSAbMBQVVfeXFMTmxmZzB2LURENGF6VkxKbkt5SUgwdFUwMEJzZHJ6aHI5d3FzQ0Q1Vm0xLUZSd3QzQUluZmJxVi0zMzMtSTlDZUhvclY0ZzFtQVRPelJjQ0swb0xpSE5TbWFZZ2RmSVB4ZVVoaC1NNE5ZSHhsSHlTb28tRlliMERpOFlFQ0N2LTZQbXpvLWRZQ0h1VFJ3dzVPOHhyejBhVmVBUnBwdjIxM1RwRjRBLXRXdTZfSzA?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQVzJFZFlzQmplRmxxcEtrRmlSUjk4anJsbUlBVlhjYURlZUQ2WmVmZm12dmgyd0lEdHVSakItcHZwM2pYQ3AtTTkxSER0cWRndEg5b3VBOUM2WXRyYWpVR0UwMGxBeWZwenRidWVrby15cFVfVGg2RVBQcjJrSHRWVk9jM2J5V0xzRDdGSw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQclpGaFp1V2xJSjBXVDk0Mi1fUUtOZW5HeGtqU0hrd0RqRUZqRUE1allYY2VnNFA4emNCc21ldEZHLW9nb2NGSHJKdmRWTG80LVBLYXd5eDRlZEhYNUNuSzNQMl9ud1l0ZTBvWENFQ1A1emRTaVFvZ1FZNzRRREkwUHVsZFFYYnZHUUNmaGN5cW9LUjE2RTh4a0Z3?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxQQXk1aDczX2prZ3FwVC14bEhZa1YxVU5BYzNNMmZZcm00dFpJLW82QVBkcUFwZjNiZTc5ZGotWEZfbGMxTTBvbGpEdmlJRnp2SEt2RF9JZElha2lING1ySzdOT0lMWk1tYjZEODNuTGlyelk1Q0VXY3hPQ1NPV2xaRlJrNVAwcWtoUjRpYi1Ta29RYjVTdC1ORUk4TDBaN1FqNDA0ZFRBS1RQRV9PU2EwZlJyNGtLWDTSAbwBQVVfeXFMTktVTlJMc1dBSTA0LVVYRlJhRnpBXzBNeTdjdjh2WTFfOFJmMVBkRGpXcGs2d2I1aVFYbXhwbTZqQzlrSi1vT2YyN1BXVnRBbS1BaGVfSkE2Y3NiX1FfNzFuOEpnYzhDbUlnX0FXVzNxaW83MVY3a21tdWl3OTlyNjJZbmdjblVmQWFub3lkblN4ZFhnb2hGaFhmMzZmcnptWWxzS0dIOFpCWHh5R0ZQbEUxS29FdjBDbjVkd24?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
