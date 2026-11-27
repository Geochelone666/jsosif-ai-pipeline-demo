# XYL Intelligence Report

- ticker: **XYL**
- Report as_of: **2026-11-26**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/XYL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/XYL/key-statistics/
- AI analysis snapshot as_of: **2026-11-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-27T06:43:02.078613+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 9, 'rule': 2, 'ai': 1, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261126T064454Z-dbdd6f45/XYL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 9 unique headlines; 5 named publishers; 0 exact duplicates; 9 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 96.4200 |
| Return 1D (%) | 1.3028 |
| Return 1W (%) | 1.7337 |
| Return 1M (%) | -10.9339 |
| Return YTD (%) | -28.0870 |
| Return 1Y (%) | -30.7956 |
| Annualized volatility (%) | 30.7298 |
| Beta vs SPY | 0.5258 |
| Max drawdown (%) | -38.9486 |
| Sharpe (rf=0) | -1.0445 |
| Downside deviation (rf=0, %) | 25.1413 |
| Sortino (rf=0) | -1.2767 |
| Historical VaR 95% (1D, %) | 2.9628 |
| Historical ES 95% (1D, %) | 5.0928 |
| Correlation vs SPY | 0.2554 |
| Tracking error vs SPY (%) | 30.5424 |
| P/E (trailing) | 21.38 |
| P/B | 2.16 |
| EV/EBITDA | 12.56 |
| Revenue growth (%) | -3.00 |
| Forward P/E (estimate) | 16.55 |
| Gross margin (%) | 39.32 |
| Operating margin (%) | 15.51 |
| Return on equity (%) | 9.76 |
| Free cash flow yield (%) | 5.47 |
| MA50 | 99.9720 |
| Close vs MA50 (%) | -3.5530 |
| MA200 | 112.3936 |
| Close vs MA200 (%) | -14.2122 |
| RSI (14, Wilder) | 48.0991 |
| MACD (12,26) | -1.4504 |
| MACD signal (9) | -1.8282 |
| MACD histogram | 0.3778 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'XYL': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 96.4200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.3028 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.7337 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -10.9339 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -28.0870 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -30.7956 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.7298 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.1413 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.2767 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9628 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.0928 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2554 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.5424 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5258 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -38.9486 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.0445 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.5455 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 39.3200 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 15.5090 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.7560 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 5.4737 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.3792 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 48.0991 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.3778 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.5530 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -14.2122 -> Clearly below the moving-average trend level.

## TAILWINDS

### Xylem (XYL) Authorizes $1.5b Buyback, Is It Still 42% Below Fair Value?
- Summary: Xylem announces a $1.5 billion share buyback program, signaling confidence in its valuation and aiming to return capital to shareholders.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxQVmpOX282aTBaOUc5Wi1WY0s0Y0M0SnpobDk4dk5MTmROcXFvdEctOUkxN1QzN2hOMkQ0cC1DWmxjVkNLelZMNEVWM1JDRzA0cTNWcE1jMkc3aklUeWp4eEtfUE9Na3F4ZXZNY0hUS2FjVm9CS2pOaXZmMTIyS01kMi0xa051N0hQazQ0MUltcGxaVjByR0dlUXRHZlZ6RW5qYmFDRFNDclFpMTg5bVBwXzFkNzVGQXBLbmJ5V2pNNEc5Y2hm0gHKAUFVX3lxTE5YZkdDRGhlNldVRlRVYVA0cHd3MXFHLW1iWjNZOVRPRlJSZFJmVXR4VU96aVdxSUFhcjFRUVRpQ1BvUFVGa2NDVEU2dVgyTUZhZ3ptYkl5VUREY1hlazdXS3ByRDZiM041eUZDQW5BYTFyUkVDU2tIZjBJeVg0OHk2TE8wejB0SWdQWk5HbHVISlVRc19mUUwtNThJY1kyVl9vRHY4RTBtVEVCeFIwblJXa2kzeFVkLUpyOEU1bVk4Y1Vyei04SHJKVkE?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Xylem (XYL) Buyback Puts Value In Focus As Investors Ask If Shares Are A Bargain
- Summary: Xylem (XYL) Buyback Puts Value In Focus As Investors Ask If Shares Are A Bargain
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPWnVmcjdxS2pUSGhGT2hNclVvVmVQdjlIaHV2S0F0ZjQ1eU5jaDJ4RS1mSTktZ1oxNEtxUnZPMnNrcXI0ank2VTFHcElpeUF2TDVWS3ZWX3pJa1JkVV93NGlXYXltYzh5eU5PRzdXd0owcUIzMXNxTnFRMkd0eDB6SUFnTVlKN1JZWDhyRmJVLUVJQUlfdGk1dmdVeFhOcTJNRE1ycFdUZHlHVkVucDRYNFRjZjQwcjBPMllLMElGa1B4U1Ay0gHKAUFVX3lxTE93bndUUVhxS3lDNl8tQlk2QU02RjRYdDRXRWREdnBCekZzTzg2VHFKZ3ZoZ0RJSlk3QlktVWFMaU1pQXB2V1RwV3dWLTdIeXF1OTkwbjlwOFlpSHpKNENaNVdhdS1Kd2VEUUlmZF92aDJRLXlocTczRTJWVmllMUNyRWF2Q29udDZ5VjRrV3RCaWRTNFdxYkUxWUdWeEl6VjZEYzVoRUZ2OWRYZldJTWlkQ2tQN1c0R294clBqb1dFS041VkJ1RVZ0RGc?oc=5>

### Xylem Inc. (NYSE:XYL) Declares Quarterly Dividend of $0.43
- Summary: Xylem Inc. (NYSE:XYL) Declares Quarterly Dividend of $0.43
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxPM3JxcUdhVGsxRjRiMC1IU0RiSjNlVFdrUzcyWE9COVZfS1ROSkk0aDctdzJ0TDNWWEVrVlRnRlBvSkdJMlFBSzdVMGFMVzAtNmd3MEVSam1leGFtSXZTZkNOdXdyajE0dEtMc1pTcUZNY3lmTEdOOHpEaVp0NVNuYWhXcF8xaXdpNWFXUUMwUDY2X1h6cWo0bmFDT2liU1ZhZ0NObnpyaXpwOEZSc0MzbEN6U1JISnM?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **XYL** | **21.38** | **2.16** | **12.56** | **-3.00** | **22,112,440,320.00 USD** | **-30.80** |
| AOS | 18.79 | 4.96 | 12.11 | -0.20 | 9,037,651,968.00 USD | 5.21 |
| PH | 30.85 | 7.09 | 21.81 | 17.90 | 113,222,311,936.00 USD | 6.25 |
| DOV | 23.96 | 3.58 | 14.74 | 7.50 | 27,313,129,472.00 USD | 11.52 |

Peers fetched as_of: 2026-11-26; XYL reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

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
- Filing date: 2026-10-27
- Revenue (latest available single quarter): 2,201,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 291,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1524472/000152447226000148/xyl-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMixAFBVV95cUxQVmpOX282aTBaOUc5Wi1WY0s0Y0M0SnpobDk4dk5MTmROcXFvdEctOUkxN1QzN2hOMkQ0cC1DWmxjVkNLelZMNEVWM1JDRzA0cTNWcE1jMkc3aklUeWp4eEtfUE9Na3F4ZXZNY0hUS2FjVm9CS2pOaXZmMTIyS01kMi0xa051N0hQazQ0MUltcGxaVjByR0dlUXRHZlZ6RW5qYmFDRFNDclFpMTg5bVBwXzFkNzVGQXBLbmJ5V2pNNEc5Y2hm0gHKAUFVX3lxTE5YZkdDRGhlNldVRlRVYVA0cHd3MXFHLW1iWjNZOVRPRlJSZFJmVXR4VU96aVdxSUFhcjFRUVRpQ1BvUFVGa2NDVEU2dVgyTUZhZ3ptYkl5VUREY1hlazdXS3ByRDZiM041eUZDQW5BYTFyUkVDU2tIZjBJeVg0OHk2TE8wejB0SWdQWk5HbHVISlVRc19mUUwtNThJY1kyVl9vRHY4RTBtVEVCeFIwblJXa2kzeFVkLUpyOEU1bVk4Y1Vyei04SHJKVkE?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPWnVmcjdxS2pUSGhGT2hNclVvVmVQdjlIaHV2S0F0ZjQ1eU5jaDJ4RS1mSTktZ1oxNEtxUnZPMnNrcXI0ank2VTFHcElpeUF2TDVWS3ZWX3pJa1JkVV93NGlXYXltYzh5eU5PRzdXd0owcUIzMXNxTnFRMkd0eDB6SUFnTVlKN1JZWDhyRmJVLUVJQUlfdGk1dmdVeFhOcTJNRE1ycFdUZHlHVkVucDRYNFRjZjQwcjBPMllLMElGa1B4U1Ay0gHKAUFVX3lxTE93bndUUVhxS3lDNl8tQlk2QU02RjRYdDRXRWREdnBCekZzTzg2VHFKZ3ZoZ0RJSlk3QlktVWFMaU1pQXB2V1RwV3dWLTdIeXF1OTkwbjlwOFlpSHpKNENaNVdhdS1Kd2VEUUlmZF92aDJRLXlocTczRTJWVmllMUNyRWF2Q29udDZ5VjRrV3RCaWRTNFdxYkUxWUdWeEl6VjZEYzVoRUZ2OWRYZldJTWlkQ2tQN1c0R294clBqb1dFS041VkJ1RVZ0RGc?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxPM3JxcUdhVGsxRjRiMC1IU0RiSjNlVFdrUzcyWE9COVZfS1ROSkk0aDctdzJ0TDNWWEVrVlRnRlBvSkdJMlFBSzdVMGFMVzAtNmd3MEVSam1leGFtSXZTZkNOdXdyajE0dEtMc1pTcUZNY3lmTEdOOHpEaVp0NVNuYWhXcF8xaXdpNWFXUUMwUDY2X1h6cWo0bmFDT2liU1ZhZ0NObnpyaXpwOEZSc0MzbEN6U1JISnM?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
