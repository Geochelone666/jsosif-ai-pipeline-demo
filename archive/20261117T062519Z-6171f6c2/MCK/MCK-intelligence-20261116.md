# MCK Intelligence Report

- ticker: **MCK**
- Report as_of: **2026-11-16**
- Market data as_of: **2026-11-16**
- Quant sources: https://finance.yahoo.com/quote/MCK/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MCK/key-statistics/
- AI analysis snapshot as_of: **2026-11-16**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-17T06:32:26.884161+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 9, 'rule': 0, 'ai': 4, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261116T043911Z-b81cfeb4/MCK** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 9 unique headlines; 8 named publishers; 0 exact duplicates; 9 HTTPS source links; largest publisher share 22.22%; oldest publication 2026-11-10

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1105.0400 |
| Return 1D (%) | 0.2022 |
| Return 1W (%) | 4.3111 |
| Return 1M (%) | 9.9717 |
| Return YTD (%) | 35.1179 |
| Return 1Y (%) | 31.7425 |
| Annualized volatility (%) | 31.7571 |
| Beta vs SPY | -0.1739 |
| Max drawdown (%) | -27.1691 |
| Sharpe (rf=0) | 0.9801 |
| Downside deviation (rf=0, %) | 18.3055 |
| Sortino (rf=0) | 1.7004 |
| Historical VaR 95% (1D, %) | 2.5993 |
| Historical ES 95% (1D, %) | 3.6083 |
| Correlation vs SPY | -0.0754 |
| Tracking error vs SPY (%) | 35.5522 |
| P/E (trailing) | 28.50 |
| P/B | -32.14 |
| EV/EBITDA | 18.52 |
| Revenue growth (%) | 7.60 |
| Forward P/E (estimate) | 21.14 |
| Gross margin (%) | 3.65 |
| Operating margin (%) | 1.59 |
| Return on equity (%) | N/A |
| Free cash flow yield (%) | 5.80 |
| MA50 | 959.0328 |
| Close vs MA50 (%) | 15.2244 |
| MA200 | 874.5046 |
| Close vs MA200 (%) | 26.3618 |
| RSI (14, Wilder) | 75.2424 |
| MACD (12,26) | 39.2517 |
| MACD signal (9) | 34.4003 |
| MACD histogram | 4.8514 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MCK': 283, 'SPY': 283}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1105.0400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.2022 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.3111 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 9.9717 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 35.1179 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 31.7425 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.7571 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 18.3055 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.7004 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5993 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.6083 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0754 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 35.5522 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1739 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.1691 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9801 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.1432 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 3.6530 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 1.5900 -> No interpretation rule is available for this metric.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 5.8021 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 28.5024 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 75.2424 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 4.8514 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 15.2244 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 26.3618 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### McKesson: Slower FY2028 Revenue Growth Makes Today's Premium Less Attractive (NYSE:MCK)
- Summary: McKesson signals slower FY2028 revenue growth, reducing the attractiveness of its current premium.
- Date: 2026-11-13 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxNcm12VnNWQi0yNmpNV1c0VVQ3SENILXpBazhGaHoxR01NRDdCbUpzVDZ3Q2R4VEdsTVNfblNxdThmSk5vVGhfcXRrYzExMjRsR2NVdE1aTUdVVExCbTZ0REVjMzZ6aVdKbzI1NlFtSkh5S1Y5dWp6bFIyWUQ4SXlHUVZ2QjhXYkFpbDUwWEl2MWtkVjB0NEh0SHdiWEVXcVFlTGhwNTZJY0tDbHFxYVhlNFJKeUFkUQ?oc=5>

### Healthcare providers & services stocks Q3 results: Benchmarking McKesson
- Summary: McKesson’s Q3 earnings reported, benchmarking against peers.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxQX2xtRkF2Q2VLV0wyMXhHaWJ6a3hUS18ybDhINks0azIxMjBzZ3Y3cVV4Z0I2Y3VlMUhXeUU5UUJTbTNLWUlCV09EcXQ2UWp6bkpaRFlDTGNUN2k3MEl5ZTB2dUpVQVdKYnp4X0Rlb0FCbHhCako3MjQ0RXM0bmQ1YXdQcjhjbmZBTVF4Z0JZS0xQM3FwWFZPVGliV3JidFV3ZmJoekw5al9vUzEzcVpvc0tkVVVFMnRTTXJ3RThoVzVCOTRIMHhZc0Jn?oc=5>

### McKesson (MCK) Posts Strong Q2 Growth, Is The Upside Already Priced In?
- Summary: McKesson reports robust Q2 growth, prompting analysis of whether upside potential is already reflected in the stock price.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPYVV4N1V4cWFTZ05qem9Xai1UU0JuYndoTG8yWEZrREYzaGZ3c2V5TGFNWGoxblZqUnJCY3M4YmlyOUlhNjdNS3JUX2ZpQktaZ2NhaFRaS2xyQnRsWmd2MlRmX2RYVDhmNHFOR3VtdldwT3BFQ1ppYm9rc2ZaM2RjaHFWR2J3dER1UF9JajdyUG0wRmxFYkNyUGw4WFl3dC1tQlZLRWI2VkZJeFNEYTZ0elNHbjRRV3l5eHJyWWFQcElHc3JP0gHKAUFVX3lxTE1lV0VTbVFMT25LSlhGb2V0dmpXMTlMUVpGaDFYUFdOTi0wMi1tamNXem5nbXhpVUhONnk3MGtmRDZLUzB1Q2h6c2hYd090QVgzTjlGZDhrRHNrOXd5Q1NMSzZyNmJ3eFNMeU1FMnNkaC1pM1BNZm5fVnYxYVlseWpINC1vUWFtSmRyd2o5QncwYmZzcGRsODkwd1luc09aZ2NvT0ZVa09fZUUteG81UHZVdXJjYjhhRWItUFNySFBvemsydGgtTEZoZWc?oc=5>

### Sales of Pharmaceuticals, GLP-1s Send McKesson Shares to New Highs
- Summary: Strong GLP-1 sales lift McKesson shares to record highs, indicating positive market reception.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxOY1RnM1dWV2JPdHp4aTFYS2VBMU54cTZzcnVtUENVWmdNc0RvWExLeTJfY0NxTXdwa1JfSlh0T3hwU1pObVJRMjFoV2JNdzlsRDJVUkEzM2lsa2pGQWg4aWZ3VVJiejM2X21TWkxQbUZUUmJVWktHanNSdlNXWUUtTmZ0RlotYTUxekJrenMtRDJUNGRCcHNsaGdISTZGcFRLdlpIcDUtWHFGd19mY1k3dXAwU0xtT2M?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MCK** | **28.50** | **-32.14** | **18.52** | **7.60** | **127,584,239,616.00 USD** | **31.74** |
| COR | 19.89 | 18.50 | 13.03 | 5.50 | 68,113,850,368.00 USD | -0.61 |
| CAH | 36.72 | -21.77 | 15.80 | 5.50 | 65,608,142,848.00 USD | 39.52 |
| CNC | 25.69 | 1.67 | 6.20 | 0.20 | 37,016,231,936.00 USD | 105.52 |

Peers fetched as_of: 2026-11-16; MCK reuses existing data (market data as_of: 2026-11-16); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

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
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 29,980,000,000.00 USD; period 2011-04-01/2011-06-30; fiscal year/reporting period 2011/Q1
- Net income (latest available single quarter): 1,218,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2027/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/927653/000092765326000281/mck-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMitgFBVV95cUxNcm12VnNWQi0yNmpNV1c0VVQ3SENILXpBazhGaHoxR01NRDdCbUpzVDZ3Q2R4VEdsTVNfblNxdThmSk5vVGhfcXRrYzExMjRsR2NVdE1aTUdVVExCbTZ0REVjMzZ6aVdKbzI1NlFtSkh5S1Y5dWp6bFIyWUQ4SXlHUVZ2QjhXYkFpbDUwWEl2MWtkVjB0NEh0SHdiWEVXcVFlTGhwNTZJY0tDbHFxYVhlNFJKeUFkUQ?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxQX2xtRkF2Q2VLV0wyMXhHaWJ6a3hUS18ybDhINks0azIxMjBzZ3Y3cVV4Z0I2Y3VlMUhXeUU5UUJTbTNLWUlCV09EcXQ2UWp6bkpaRFlDTGNUN2k3MEl5ZTB2dUpVQVdKYnp4X0Rlb0FCbHhCako3MjQ0RXM0bmQ1YXdQcjhjbmZBTVF4Z0JZS0xQM3FwWFZPVGliV3JidFV3ZmJoekw5al9vUzEzcVpvc0tkVVVFMnRTTXJ3RThoVzVCOTRIMHhZc0Jn?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPYVV4N1V4cWFTZ05qem9Xai1UU0JuYndoTG8yWEZrREYzaGZ3c2V5TGFNWGoxblZqUnJCY3M4YmlyOUlhNjdNS3JUX2ZpQktaZ2NhaFRaS2xyQnRsWmd2MlRmX2RYVDhmNHFOR3VtdldwT3BFQ1ppYm9rc2ZaM2RjaHFWR2J3dER1UF9JajdyUG0wRmxFYkNyUGw4WFl3dC1tQlZLRWI2VkZJeFNEYTZ0elNHbjRRV3l5eHJyWWFQcElHc3JP0gHKAUFVX3lxTE1lV0VTbVFMT25LSlhGb2V0dmpXMTlMUVpGaDFYUFdOTi0wMi1tamNXem5nbXhpVUhONnk3MGtmRDZLUzB1Q2h6c2hYd090QVgzTjlGZDhrRHNrOXd5Q1NMSzZyNmJ3eFNMeU1FMnNkaC1pM1BNZm5fVnYxYVlseWpINC1vUWFtSmRyd2o5QncwYmZzcGRsODkwd1luc09aZ2NvT0ZVa09fZUUteG81UHZVdXJjYjhhRWItUFNySFBvemsydGgtTEZoZWc?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxOY1RnM1dWV2JPdHp4aTFYS2VBMU54cTZzcnVtUENVWmdNc0RvWExLeTJfY0NxTXdwa1JfSlh0T3hwU1pObVJRMjFoV2JNdzlsRDJVUkEzM2lsa2pGQWg4aWZ3VVJiejM2X21TWkxQbUZUUmJVWktHanNSdlNXWUUtTmZ0RlotYTUxekJrenMtRDJUNGRCcHNsaGdISTZGcFRLdlpIcDUtWHFGd19mY1k3dXAwU0xtT2M?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
