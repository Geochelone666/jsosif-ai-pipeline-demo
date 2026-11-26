# ENB Intelligence Report

- ticker: **ENB**
- Report as_of: **2026-11-25**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/ENB/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ENB/key-statistics/
- AI analysis snapshot as_of: **2026-11-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-26T06:45:23.849171+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 17, 'rule': 7, 'ai': 5, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261125T065354Z-0b3565c6/ENB** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 17 unique headlines; 8 named publishers; 0 exact duplicates; 17 HTTPS source links; largest publisher share 29.41%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 46.9500 |
| Return 1D (%) | 1.5355 |
| Return 1W (%) | 0.3634 |
| Return 1M (%) | -1.0943 |
| Return YTD (%) | 3.5916 |
| Return 1Y (%) | 4.1797 |
| Annualized volatility (%) | 18.3921 |
| Beta vs SPY | -0.0816 |
| Max drawdown (%) | -19.8462 |
| Sharpe (rf=0) | 0.3152 |
| Downside deviation (rf=0, %) | 12.9555 |
| Sortino (rf=0) | 0.4474 |
| Historical VaR 95% (1D, %) | 1.8065 |
| Historical ES 95% (1D, %) | 2.5127 |
| Correlation vs SPY | -0.0662 |
| Tracking error vs SPY (%) | 24.4447 |
| P/E (trailing) | 22.57 |
| P/B | 2.42 |
| EV/EBITDA | 13.02 |
| Revenue growth (%) | 44.00 |
| Forward P/E (estimate) | 21.14 |
| Gross margin (%) | 30.20 |
| Operating margin (%) | 12.82 |
| Return on equity (%) | 9.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 46.8767 |
| Close vs MA50 (%) | 0.1564 |
| MA200 | 50.7081 |
| Close vs MA200 (%) | -7.4113 |
| RSI (14, Wilder) | 50.1135 |
| MACD (12,26) | -0.2976 |
| MACD signal (9) | -0.1907 |
| MACD histogram | -0.1069 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ENB': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 46.9500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.5355 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.3634 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -1.0943 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 3.5916 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 4.1797 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 18.3921 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 12.9555 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4474 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8065 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.5127 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0662 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.4447 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.0816 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.8462 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3152 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.1421 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 30.1950 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 12.8210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.8490 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.5721 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 50.1135 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1069 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.1564 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -7.4113 -> Clearly below the moving-average trend level.

## TAILWINDS

### Enbridge Inc. (TSX:ENB) Stock Climbs 1.06%: Diversified Energy Infrastructure and Recurring Cash Flows Support Growth Outlook
- Summary: Enbridge Inc. (TSX:ENB) Stock Climbs 1.06%: Diversified Energy Infrastructure and Recurring Cash Flows Support Growth Outlook
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxNbHJmaUt0R0NhWjU5SDg0SnNoUUhkMERFNXE3QktPdnVVUWFjOF84X3N4ODc4X0hET0w1NXR4bk1iakwtYXVqVy1JLVNFaDhMS21QemFNck9XV3JrMDVxSVE3cTJqYnBpYzAxTnpCcm1zQmJFUkhnRnlmalEzbzRZb0p4YVljMWlnQTlDa3QwRTlxRzFRMXFVVFQ2eF9QdUFaekJaTVVqbU9sRGFvaGZrUEYtNXhENTh4Umt0di1FVy1tSlhqNFYyVl9lMHlSUkhzLVFneDdUbWRtZWZGanFYaXBOZw?oc=5>

### Utilities Focus: Enbridge Inc. (TSX:ENB) — S&P/TSX Composite Large Cap Value Stock in Focus After Fresh Corporate News
- Summary: Enbridge highlighted as a value stock in the TSX Composite after recent corporate updates.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxNR2ZjM1kza0RlcU9zaEZKSWVzUUFhNnJXNUZFNnlGSFF4OFNqd2tLWENNdVZXU1FXT1NDc2NWN29idGozTDRId1hXS1p5MzNKeWhnQ2FhSWNSaHVhLVotLTVrY2Q1V1J5TEE2bzJXTzU5YklSM0ljdmpfeU1sWDUtcTlmMnJLMlduNVFtNmxWaVowUmZrWGJUbjV6aDhVbGVrMTJmcDEyd1RKRUZwN3NFZHdOdnZRRzV3RnAtd3B6QXlxR3ozeHVUR1ZuR0JpS1lkUjF6eGJnamZjdE0?oc=5>

## HEADWINDS

### Enbridge shares technical analysis: Trading flat under seller pressure near key support
- Summary: Enbridge shares technical analysis: Trading flat under seller pressure near key support
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPeGxzNTdkZDYwTWc0WUFSQ0pwYzJLS1RMV1lEWGM3eEMtVmFhOTBfTXp4SFpvSl93dUwwZnAyaWpIWXdSYVRUcXhJandYaGtXb1FyWWpDMXktNUJ0dzkzdk83c1dRekctdEFJbk9TRU1VM1lObjZmY2U3bEhPTWp4VTNWeXZ2ZGdjLUJ6Y0RYbnR4aFU?oc=5>

### Enbridge Inc. (TSX:ENB) Stock Under Pressure: 1.42% Decline Raises Valuation Concerns Despite Resilient Energy Infrastructure Business
- Summary: Enbridge Inc. (TSX:ENB) Stock Under Pressure: 1.42% Decline Raises Valuation Concerns Despite Resilient Energy Infrastructure Business
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxQZlJ1WkpaNnoxRF9XaVNPZ1VPSEktb0Q1WW5zVll3bVA3UVIzR3dVTmZ3elJnZ2F5UlpjZ0ZhSkhJUFJ3RTBfU3h2cmc1b3MzNUFBcm13Tm42MHZZdEZTZlBwREFTbC1RVlRqNTN5RFdaRGtCbVdsNUVndkRSWGdIdlN2R01BX0FZQUtZblRUZldDSnNFQmpRLTZGaVFxazUyRjRDYjFta3J5cTAtTU1lR1Z3a2lkdHA3N0NfWk8wcjlKb2FWV18tNDFSRjU4RzRGQ0dEU1Bib2VmS1ZYU2wyTnhTYWh0ZVhuVzljaVhhVQ?oc=5>

## CATALYSTS

### Enbridge sees large fund acquisition: ENB remains range-bound
- Summary: Enbridge sees large fund acquisition: ENB remains range-bound
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPS0FoRnJaaGtLakkxeTNhYTRQNjU1VC1VanpYYlRmWnlpNzZWNEtER05GR1BOR1VHMXJUNTRmczFPaTNBTEJZM1ZYM04zb0oyWE5mNEFjUmZPZ01xWlIzcjdlN0dJY2NXMVIyUEdkLUhPX1NBREtRU3pRbm80bVU4eVFlSWYtOWVtTjZWd0tycVMtWDg?oc=5>

### Enbridge reaffirms 2026 guidance and raises dividend: ENB tests C$65.94 resistance
- Summary: Enbridge reaffirms 2026 guidance and raises dividend: ENB tests C$65.94 resistance
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQaTRha1ljQjNDVHRGQkVwdDJ2bTVLeG11clk5cE4za2E5V284c3ZzWUpQWlc0cUtvRnRwTDFkYlFCYURkOFFyVU1Lc1hCTk5aZ2tIcnZOY2R1amJhTko0SDFGUFBOcjdKXzBxNTJtZWx4eWpWdHJUTm8yWHZ0dlAxc2w0bUVDdXJVQ2pNaUtPRU5KV2Nza0E?oc=5>

### Enbridge Stock: Is It Still a Top Passive Income Pick for Retirees?
- Summary: Enbridge Stock: Is It Still a Top Passive Income Pick for Retirees?
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxNaHJLNGp5dW44UnlHVEhKMmZvazQ0bmJpV2x4bGtlMjM3MURBUHBYSEtpbFJid3hYdkRKZzhiNUJwWnluSWFJLUczNEo2clNxYkx6eEhvSVJzWks4VjU4Q0IydGVVbEZNMlVzWmoyeEdCUFNsbkVKT1JGUlhDQUNVZDdFYUlsUncw?oc=5>

### Enbridge Inc (NYSE:ENB) Stock Has Consensus Price Target of $65.88 According to Brokerages
- Summary: Enbridge Inc (NYSE:ENB) Stock Has Consensus Price Target of $65.88 According to Brokerages
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5AFBVV95cUxOWWFTMEo5QjRsaHZNTDBwYTdfNVZXaDhzbmJSRE5RY0pSNmNzU1RyUnJsU1lVNExoT29HWHctNnFNNUZxbXpBY1NJVEdnMXgyV2FGdHpCdzZhMHEtcUVqVmVVdExpQmNmT1pXTDRzRmdBMThYNkMwSHJxN1RGQS1oZW93MzZMUjBnVVdUZm54d05XNTAxRUVTLWxsRUJSMzVBMGJSdUdIY25qQTlLLVFXaHR0Q1RKcUFQQk9UdU9heWxWOTdsRmJ3NDdlS0FoOFBKLTlsc2k1VWs5TElYdGJZcllMLVI?oc=5>

### Is Enbridge (TSX:ENB) Undervalued As Investors Reassess Its Acquisition Driven Growth?
- Summary: Analysts question Enbridge’s valuation, suggesting potential upside from acquisition-driven growth.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxPTGRfRnpycWZUUlNzUnpaZVFTZGswakdQRmZWRDVXbldPTk1tVUhheWNCbUdEVDBoUFRPdlRPZGwwUGs0UHNucWNtMHZ3U0ZOaVpzbkh3VXI5V1hra2JJUG1PVjVpYzJpdi14Q2Q0Mm54RG55cEc3andwODdYNXAyNVJxQ2Fkd19OSnppbVItN2Q1NFhLaWpLX2YtYVhSUDRMbjBWVXF0VU1udmt1U1FONVl0VFc2VUlsWWVhWE9ENlhQeThKV3Bj0gHMAUFVX3lxTE9hUW10el9ZaXJFbGdLN2wxajhyVHFiNXlxZDRRZjRCeVJwUERfbFdJblFOUTJsSW9PaERCaXhyZ2xpSlRNZWNuTkJBQUI4RXJBZGw3aF9kc3p5NVRDTzJoelpLdUNIQk15dDVWcldyZUdIN1pJWXpKcldtY05aNHNBRmJKV00taXhHY3dPSUNHZm1lR3dJM2hoVWdBZmN2VkVsa0FUMzlOWEVGSDJITDk2bzNwNjREdDJYVTdCV3QzekhHenJpLXhiSzJTQw?oc=5>

### Enbridge: Yield Is Very Attractive, But Performance Is Underwhelming (NYSE:ENB)
- Summary: Analyst notes attractive dividend yield but weak performance, suggesting cautious investment.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxQWENkQ3JydFBJb2JlejRXUFhHYjRzRjdBczRzSWdfU1NEVENHQkVXNzllczNKN1ZodXptakZiZnZxa0I4OU5oVWpGendfai1tT2Z3OTBqSzdlU2xKQzBObzIwVXY5NzdNTm5LSmJwWU5xRkY4S3JYT3JsY3VrQUZMMzhLdFliWkVjSDRqTWctcUNYaDU0SUE3LUthaG9SQm1xUmYyVkFOYmFkdUk?oc=5>

### Enbridge vs. Pembina: Which Pipeline Stock Is the Better Buy Today?
- Summary: Comparison of Enbridge and Pembina, advising investors to evaluate which pipeline stock offers better value.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQcjJMelZGV3ZJaDhNdXdadTNqYVZMWEd2ZTAwamg1a0lxR3V2Yk9Qcl9Yb2dlLXpUckhrdTFoOWZwV093TlppYXZmVGhRNmFSZWhfUTF6TlQ3cjJKV0NOWkg2dHphaVdDVVVGMXpCSkZzMnVSRWtUNGZYUW1ZcU9jR1V4WnRiWGRRWnZN?oc=5>

### Enbridge: My Verdict Is Buy – Here’s the Dividend $6,000 Would Collect
- Summary: Strong buy recommendation with projected $6,000 dividend income, highlighting Enbridge’s attractive yield.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxQU1ZvWnMtR3pJVDA5N29kZXZ1cGR6VE4tY0g2aEhCR3FUNk9aSWoxUDQyY1Fqc0Rtd2FNcDl6RnBhZEpuWll2Ullndk9EVEVyNkJrcGF1ZUdFdXNtY3h0VGFBNHQzbHRpY1hvczFhVXoyZktHakdGdjh2SVdZTFVRRkFWQ0xtUWs?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ENB** | **22.57** | **2.42** | **13.02** | **44.00** | **104,646,295,552.00 USD** | **4.18** |
| TRP.TO | 24.34 | 3.64 | 16.45 | 8.80 | 93,061,038,080.00 CAD | 22.93 |
| KMI | 19.56 | 2.23 | 13.58 | 9.30 | 70,596,296,704.00 USD | 24.00 |
| EPD | 11.94 | 2.56 | 10.64 | 49.30 | 77,767,180,288.00 USD | 17.72 |

Peers fetched as_of: 2026-11-25; ENB reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-06
- Next expected earnings: 2027-02-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-25

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-06
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: https://www.sec.gov/Archives/edgar/data/895728/000119312526450714/enb-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi4wFBVV95cUxNbHJmaUt0R0NhWjU5SDg0SnNoUUhkMERFNXE3QktPdnVVUWFjOF84X3N4ODc4X0hET0w1NXR4bk1iakwtYXVqVy1JLVNFaDhMS21QemFNck9XV3JrMDVxSVE3cTJqYnBpYzAxTnpCcm1zQmJFUkhnRnlmalEzbzRZb0p4YVljMWlnQTlDa3QwRTlxRzFRMXFVVFQ2eF9QdUFaekJaTVVqbU9sRGFvaGZrUEYtNXhENTh4Umt0di1FVy1tSlhqNFYyVl9lMHlSUkhzLVFneDdUbWRtZWZGanFYaXBOZw?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxNR2ZjM1kza0RlcU9zaEZKSWVzUUFhNnJXNUZFNnlGSFF4OFNqd2tLWENNdVZXU1FXT1NDc2NWN29idGozTDRId1hXS1p5MzNKeWhnQ2FhSWNSaHVhLVotLTVrY2Q1V1J5TEE2bzJXTzU5YklSM0ljdmpfeU1sWDUtcTlmMnJLMlduNVFtNmxWaVowUmZrWGJUbjV6aDhVbGVrMTJmcDEyd1RKRUZwN3NFZHdOdnZRRzV3RnAtd3B6QXlxR3ozeHVUR1ZuR0JpS1lkUjF6eGJnamZjdE0?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPeGxzNTdkZDYwTWc0WUFSQ0pwYzJLS1RMV1lEWGM3eEMtVmFhOTBfTXp4SFpvSl93dUwwZnAyaWpIWXdSYVRUcXhJandYaGtXb1FyWWpDMXktNUJ0dzkzdk83c1dRekctdEFJbk9TRU1VM1lObjZmY2U3bEhPTWp4VTNWeXZ2ZGdjLUJ6Y0RYbnR4aFU?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxQZlJ1WkpaNnoxRF9XaVNPZ1VPSEktb0Q1WW5zVll3bVA3UVIzR3dVTmZ3elJnZ2F5UlpjZ0ZhSkhJUFJ3RTBfU3h2cmc1b3MzNUFBcm13Tm42MHZZdEZTZlBwREFTbC1RVlRqNTN5RFdaRGtCbVdsNUVndkRSWGdIdlN2R01BX0FZQUtZblRUZldDSnNFQmpRLTZGaVFxazUyRjRDYjFta3J5cTAtTU1lR1Z3a2lkdHA3N0NfWk8wcjlKb2FWV18tNDFSRjU4RzRGQ0dEU1Bib2VmS1ZYU2wyTnhTYWh0ZVhuVzljaVhhVQ?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPS0FoRnJaaGtLakkxeTNhYTRQNjU1VC1VanpYYlRmWnlpNzZWNEtER05GR1BOR1VHMXJUNTRmczFPaTNBTEJZM1ZYM04zb0oyWE5mNEFjUmZPZ01xWlIzcjdlN0dJY2NXMVIyUEdkLUhPX1NBREtRU3pRbm80bVU4eVFlSWYtOWVtTjZWd0tycVMtWDg?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQaTRha1ljQjNDVHRGQkVwdDJ2bTVLeG11clk5cE4za2E5V284c3ZzWUpQWlc0cUtvRnRwTDFkYlFCYURkOFFyVU1Lc1hCTk5aZ2tIcnZOY2R1amJhTko0SDFGUFBOcjdKXzBxNTJtZWx4eWpWdHJUTm8yWHZ0dlAxc2w0bUVDdXJVQ2pNaUtPRU5KV2Nza0E?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxNaHJLNGp5dW44UnlHVEhKMmZvazQ0bmJpV2x4bGtlMjM3MURBUHBYSEtpbFJid3hYdkRKZzhiNUJwWnluSWFJLUczNEo2clNxYkx6eEhvSVJzWks4VjU4Q0IydGVVbEZNMlVzWmoyeEdCUFNsbkVKT1JGUlhDQUNVZDdFYUlsUncw?oc=5
- https://news.google.com/rss/articles/CBMi5AFBVV95cUxOWWFTMEo5QjRsaHZNTDBwYTdfNVZXaDhzbmJSRE5RY0pSNmNzU1RyUnJsU1lVNExoT29HWHctNnFNNUZxbXpBY1NJVEdnMXgyV2FGdHpCdzZhMHEtcUVqVmVVdExpQmNmT1pXTDRzRmdBMThYNkMwSHJxN1RGQS1oZW93MzZMUjBnVVdUZm54d05XNTAxRUVTLWxsRUJSMzVBMGJSdUdIY25qQTlLLVFXaHR0Q1RKcUFQQk9UdU9heWxWOTdsRmJ3NDdlS0FoOFBKLTlsc2k1VWs5TElYdGJZcllMLVI?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxPTGRfRnpycWZUUlNzUnpaZVFTZGswakdQRmZWRDVXbldPTk1tVUhheWNCbUdEVDBoUFRPdlRPZGwwUGs0UHNucWNtMHZ3U0ZOaVpzbkh3VXI5V1hra2JJUG1PVjVpYzJpdi14Q2Q0Mm54RG55cEc3andwODdYNXAyNVJxQ2Fkd19OSnppbVItN2Q1NFhLaWpLX2YtYVhSUDRMbjBWVXF0VU1udmt1U1FONVl0VFc2VUlsWWVhWE9ENlhQeThKV3Bj0gHMAUFVX3lxTE9hUW10el9ZaXJFbGdLN2wxajhyVHFiNXlxZDRRZjRCeVJwUERfbFdJblFOUTJsSW9PaERCaXhyZ2xpSlRNZWNuTkJBQUI4RXJBZGw3aF9kc3p5NVRDTzJoelpLdUNIQk15dDVWcldyZUdIN1pJWXpKcldtY05aNHNBRmJKV00taXhHY3dPSUNHZm1lR3dJM2hoVWdBZmN2VkVsa0FUMzlOWEVGSDJITDk2bzNwNjREdDJYVTdCV3QzekhHenJpLXhiSzJTQw?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxQWENkQ3JydFBJb2JlejRXUFhHYjRzRjdBczRzSWdfU1NEVENHQkVXNzllczNKN1ZodXptakZiZnZxa0I4OU5oVWpGendfai1tT2Z3OTBqSzdlU2xKQzBObzIwVXY5NzdNTm5LSmJwWU5xRkY4S3JYT3JsY3VrQUZMMzhLdFliWkVjSDRqTWctcUNYaDU0SUE3LUthaG9SQm1xUmYyVkFOYmFkdUk?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQcjJMelZGV3ZJaDhNdXdadTNqYVZMWEd2ZTAwamg1a0lxR3V2Yk9Qcl9Yb2dlLXpUckhrdTFoOWZwV093TlppYXZmVGhRNmFSZWhfUTF6TlQ3cjJKV0NOWkg2dHphaVdDVVVGMXpCSkZzMnVSRWtUNGZYUW1ZcU9jR1V4WnRiWGRRWnZN?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxQU1ZvWnMtR3pJVDA5N29kZXZ1cGR6VE4tY0g2aEhCR3FUNk9aSWoxUDQyY1Fqc0Rtd2FNcDl6RnBhZEpuWll2Ullndk9EVEVyNkJrcGF1ZUdFdXNtY3h0VGFBNHQzbHRpY1hvczFhVXoyZktHakdGdjh2SVdZTFVRRkFWQ0xtUWs?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
