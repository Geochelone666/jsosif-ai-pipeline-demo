# MCK Intelligence Report

- ticker: **MCK**
- Report as_of: **2026-11-13**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/MCK/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MCK/key-statistics/
- AI analysis snapshot as_of: **2026-11-13**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-14T04:59:53.526180+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 6, 'rule': 0, 'ai': 5, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261113T045636Z-34122c9a/MCK** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 6 unique headlines; 6 named publishers; 0 exact duplicates; 6 HTTPS source links; largest publisher share 16.67%; oldest publication 2026-11-06

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1102.8101 |
| Return 1D (%) | 2.3917 |
| Return 1W (%) | 3.9563 |
| Return 1M (%) | 14.6515 |
| Return YTD (%) | 34.8452 |
| Return 1Y (%) | 30.8319 |
| Annualized volatility (%) | 31.7322 |
| Beta vs SPY | -0.1832 |
| Max drawdown (%) | -27.1691 |
| Sharpe (rf=0) | 1.0044 |
| Downside deviation (rf=0, %) | 18.2756 |
| Sortino (rf=0) | 1.7440 |
| Historical VaR 95% (1D, %) | 2.5988 |
| Historical ES 95% (1D, %) | 3.6083 |
| Correlation vs SPY | -0.0787 |
| Tracking error vs SPY (%) | 35.5092 |
| P/E (trailing) | 27.78 |
| P/B | -32.07 |
| EV/EBITDA | 18.48 |
| Revenue growth (%) | 7.60 |
| Forward P/E (estimate) | 21.10 |
| Gross margin (%) | 3.65 |
| Operating margin (%) | 1.59 |
| Return on equity (%) | N/A |
| Free cash flow yield (%) | 5.81 |
| MA50 | 955.0918 |
| Close vs MA50 (%) | 15.4664 |
| MA200 | 873.1230 |
| Close vs MA200 (%) | 26.3064 |
| RSI (14, Wilder) | 74.9299 |
| MACD (12,26) | 38.0869 |
| MACD signal (9) | 33.1874 |
| MACD histogram | 4.8994 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MCK': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1102.8101 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.3917 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.9563 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 14.6515 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 34.8452 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 30.8319 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.7322 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 18.2756 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.7440 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5988 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.6083 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0787 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 35.5092 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1832 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.1691 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0044 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.1005 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 3.6530 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 1.5900 -> No interpretation rule is available for this metric.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 5.8139 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.7786 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 74.9299 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 4.8994 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 15.4664 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 26.3064 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Healthcare providers & services stocks Q3 results: Benchmarking McKesson
- Summary: McKesson’s Q3 earnings reported, benchmarking against peers.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxQX2xtRkF2Q2VLV0wyMXhHaWJ6a3hUS18ybDhINks0azIxMjBzZ3Y3cVV4Z0I2Y3VlMUhXeUU5UUJTbTNLWUlCV09EcXQ2UWp6bkpaRFlDTGNUN2k3MEl5ZTB2dUpVQVdKYnp4X0Rlb0FCbHhCako3MjQ0RXM0bmQ1YXdQcjhjbmZBTVF4Z0JZS0xQM3FwWFZPVGliV3JidFV3ZmJoekw5al9vUzEzcVpvc0tkVVVFMnRTTXJ3RThoVzVCOTRIMHhZc0Jn?oc=5>

### McKesson (MCK) Posts Strong Q2 Growth, Is The Upside Already Priced In?
- Summary: McKesson reports robust Q2 growth, prompting analysis of whether upside potential is already reflected in the stock price.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPYVV4N1V4cWFTZ05qem9Xai1UU0JuYndoTG8yWEZrREYzaGZ3c2V5TGFNWGoxblZqUnJCY3M4YmlyOUlhNjdNS3JUX2ZpQktaZ2NhaFRaS2xyQnRsWmd2MlRmX2RYVDhmNHFOR3VtdldwT3BFQ1ppYm9rc2ZaM2RjaHFWR2J3dER1UF9JajdyUG0wRmxFYkNyUGw4WFl3dC1tQlZLRWI2VkZJeFNEYTZ0elNHbjRRV3l5eHJyWWFQcElHc3JP0gHKAUFVX3lxTE1lV0VTbVFMT25LSlhGb2V0dmpXMTlMUVpGaDFYUFdOTi0wMi1tamNXem5nbXhpVUhONnk3MGtmRDZLUzB1Q2h6c2hYd090QVgzTjlGZDhrRHNrOXd5Q1NMSzZyNmJ3eFNMeU1FMnNkaC1pM1BNZm5fVnYxYVlseWpINC1vUWFtSmRyd2o5QncwYmZzcGRsODkwd1luc09aZ2NvT0ZVa09fZUUteG81UHZVdXJjYjhhRWItUFNySFBvemsydGgtTEZoZWc?oc=5>

### McKesson: Slower FY2028 Revenue Growth Makes Today's Premium Less Attractive (NYSE:MCK)
- Summary: McKesson signals slower FY2028 revenue growth, reducing the attractiveness of its current premium.
- Date: 2026-11-13 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxNcm12VnNWQi0yNmpNV1c0VVQ3SENILXpBazhGaHoxR01NRDdCbUpzVDZ3Q2R4VEdsTVNfblNxdThmSk5vVGhfcXRrYzExMjRsR2NVdE1aTUdVVExCbTZ0REVjMzZ6aVdKbzI1NlFtSkh5S1Y5dWp6bFIyWUQ4SXlHUVZ2QjhXYkFpbDUwWEl2MWtkVjB0NEh0SHdiWEVXcVFlTGhwNTZJY0tDbHFxYVhlNFJKeUFkUQ?oc=5>

### Sales of Pharmaceuticals, GLP-1s Send McKesson Shares to New Highs
- Summary: Strong pharmaceutical and GLP-1 sales lift McKesson shares to new highs.
- Date: 2026-11-11 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxOY1RnM1dWV2JPdHp4aTFYS2VBMU54cTZzcnVtUENVWmdNc0RvWExLeTJfY0NxTXdwa1JfSlh0T3hwU1pObVJRMjFoV2JNdzlsRDJVUkEzM2lsa2pGQWg4aWZ3VVJiejM2X21TWkxQbUZUUmJVWktHanNSdlNXWUUtTmZ0RlotYTUxekJrenMtRDJUNGRCcHNsaGdISTZGcFRLdlpIcDUtWHFGd19mY1k3dXAwU0xtT2M?oc=5>

## RISKS

### Is McKesson Stock Increasing Your Market Risk?
- Summary: Questioning McKesson’s impact on portfolio risk.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNQVpTYzNPcmZRVFlvclIzdWJiQW4xVGRMSmFZMENfalFBOGxnSWZ4Q29yUWl5clNCcHk0eUhCaXcya0NuWkFGVHFnZGYycWdMSmZFcUktYWtaRGp4VHpwUHY5TlFmczh0dVNVRS1CYkV1SF9DaTN1Z3VsQWFmQVA4QTV1Tlhzd0wxMHpHSnBXTXNpUV9Lc2J0eEx4R29ha2R4UFlHWFhNNlo?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MCK** | **27.78** | **-32.07** | **18.48** | **7.60** | **127,326,773,248.00 USD** | **30.83** |
| COR | 19.46 | 18.61 | 13.10 | 5.50 | 68,512,677,888.00 USD | -0.82 |
| CAH | 35.99 | -21.56 | 15.65 | 5.50 | 64,972,517,376.00 USD | 37.71 |
| CNC | 24.16 | 1.59 | 5.83 | 0.20 | 35,283,492,864.00 USD | 97.48 |

Peers fetched as_of: 2026-11-13; MCK reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-13

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

- https://news.google.com/rss/articles/CBMiygFBVV95cUxQX2xtRkF2Q2VLV0wyMXhHaWJ6a3hUS18ybDhINks0azIxMjBzZ3Y3cVV4Z0I2Y3VlMUhXeUU5UUJTbTNLWUlCV09EcXQ2UWp6bkpaRFlDTGNUN2k3MEl5ZTB2dUpVQVdKYnp4X0Rlb0FCbHhCako3MjQ0RXM0bmQ1YXdQcjhjbmZBTVF4Z0JZS0xQM3FwWFZPVGliV3JidFV3ZmJoekw5al9vUzEzcVpvc0tkVVVFMnRTTXJ3RThoVzVCOTRIMHhZc0Jn?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPYVV4N1V4cWFTZ05qem9Xai1UU0JuYndoTG8yWEZrREYzaGZ3c2V5TGFNWGoxblZqUnJCY3M4YmlyOUlhNjdNS3JUX2ZpQktaZ2NhaFRaS2xyQnRsWmd2MlRmX2RYVDhmNHFOR3VtdldwT3BFQ1ppYm9rc2ZaM2RjaHFWR2J3dER1UF9JajdyUG0wRmxFYkNyUGw4WFl3dC1tQlZLRWI2VkZJeFNEYTZ0elNHbjRRV3l5eHJyWWFQcElHc3JP0gHKAUFVX3lxTE1lV0VTbVFMT25LSlhGb2V0dmpXMTlMUVpGaDFYUFdOTi0wMi1tamNXem5nbXhpVUhONnk3MGtmRDZLUzB1Q2h6c2hYd090QVgzTjlGZDhrRHNrOXd5Q1NMSzZyNmJ3eFNMeU1FMnNkaC1pM1BNZm5fVnYxYVlseWpINC1vUWFtSmRyd2o5QncwYmZzcGRsODkwd1luc09aZ2NvT0ZVa09fZUUteG81UHZVdXJjYjhhRWItUFNySFBvemsydGgtTEZoZWc?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxNcm12VnNWQi0yNmpNV1c0VVQ3SENILXpBazhGaHoxR01NRDdCbUpzVDZ3Q2R4VEdsTVNfblNxdThmSk5vVGhfcXRrYzExMjRsR2NVdE1aTUdVVExCbTZ0REVjMzZ6aVdKbzI1NlFtSkh5S1Y5dWp6bFIyWUQ4SXlHUVZ2QjhXYkFpbDUwWEl2MWtkVjB0NEh0SHdiWEVXcVFlTGhwNTZJY0tDbHFxYVhlNFJKeUFkUQ?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxOY1RnM1dWV2JPdHp4aTFYS2VBMU54cTZzcnVtUENVWmdNc0RvWExLeTJfY0NxTXdwa1JfSlh0T3hwU1pObVJRMjFoV2JNdzlsRDJVUkEzM2lsa2pGQWg4aWZ3VVJiejM2X21TWkxQbUZUUmJVWktHanNSdlNXWUUtTmZ0RlotYTUxekJrenMtRDJUNGRCcHNsaGdISTZGcFRLdlpIcDUtWHFGd19mY1k3dXAwU0xtT2M?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNQVpTYzNPcmZRVFlvclIzdWJiQW4xVGRMSmFZMENfalFBOGxnSWZ4Q29yUWl5clNCcHk0eUhCaXcya0NuWkFGVHFnZGYycWdMSmZFcUktYWtaRGp4VHpwUHY5TlFmczh0dVNVRS1CYkV1SF9DaTN1Z3VsQWFmQVA4QTV1Tlhzd0wxMHpHSnBXTXNpUV9Lc2J0eEx4R29ha2R4UFlHWFhNNlo?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
