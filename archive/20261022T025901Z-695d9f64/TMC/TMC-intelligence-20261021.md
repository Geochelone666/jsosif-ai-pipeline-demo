# TMC Intelligence Report

- ticker: **TMC**
- Report as_of: **2026-10-21**
- Market data as_of: **2026-10-21**
- Quant sources: https://finance.yahoo.com/quote/TMC/history/, https://finance.yahoo.com/quote/TMC/key-statistics/
- AI analysis snapshot as_of: **2026-10-21**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-22T04:22:32.751342+00:00**
- AI status: **No recent headlines returned by RSS; no AI classification performed**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 0, 'rule': 0, 'ai': 0, 'unknown': 0})

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 2.6500 |
| Return 1D (%) | 1.1450 |
| Return 1W (%) | 0.7605 |
| Return 1M (%) | -35.9903 |
| Return YTD (%) | -57.0502 |
| Return 1Y (%) | -66.0691 |
| Annualized volatility (%) | 90.4531 |
| Beta vs SPY | N/A |
| Max drawdown (%) | -72.6695 |
| Sharpe (rf=0) | -0.7521 |
| P/E (trailing) | N/A |
| P/B | -42.06 |
| EV/EBITDA | -5.21 |
| Revenue growth (%) | N/A |
| MA50 | 3.8946 |
| Close vs MA50 (%) | -31.9571 |
| MA200 | 5.0632 |
| Close vs MA200 (%) | -47.6618 |
| RSI (14, Wilder) | 25.9750 |
| MACD (12,26) | -0.3914 |
| MACD signal (9) | -0.3286 |
| MACD histogram | -0.0629 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TMC': 265}.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 2.6500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.1450 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.7605 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -35.9903 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -57.0502 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -66.0691 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 90.4531 -> High annualized volatility.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -72.6695 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.7521 -> Negative risk-adjusted return.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 25.9750 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0629 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -31.9571 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -47.6618 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

No items in this run

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TMC** | **N/A** | **-42.06** | **-5.21** | **N/A** | **1,169,009,024.00 USD** | **-66.07** |
| MP | N/A | 3.59 | 171.54 | 119.70 | 7,035,012,608.00 USD | -46.70 |
| LAC | N/A | 0.55 | -25.49 | N/A | 776,911,936.00 USD | -69.16 |
| VALE | 25.92 | 1.38 | 1.80 | 6.40 | 54,048,186,368.00 USD | 22.04 |

Peers fetched as_of: 2026-10-21; TMC reuses existing data (market data as_of: 2026-10-21); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-13
- Next expected earnings: 2026-11-12 (yfinance; expected dates may change)

## MACRO (FRED)

N/A: no FRED API key configured; skipped

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-13
- Revenue (latest available single quarter): 410,000.00 USD; period 2024-04-01/2024-06-30; fiscal year/reporting period 2024/Q2
- Net income (latest available single quarter): -60,123,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1798562/000110465926096051/tmc-20260630x10q.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES



## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
