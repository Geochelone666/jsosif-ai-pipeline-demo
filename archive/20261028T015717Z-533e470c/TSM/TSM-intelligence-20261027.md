# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-10-27**
- Market data as_of: **2026-10-27**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-10-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-28T02:12:16.200336+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 21, 'rule': 2, 'ai': 11, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261027T014607Z-b66f6bd5/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 1, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 21 unique headlines; 13 named publishers; 4 exact duplicates; 21 HTTPS source links; largest publisher share 19.05%; oldest publication 2026-10-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 436.8700 |
| Return 1D (%) | 2.9455 |
| Return 1W (%) | 2.7736 |
| Return 1M (%) | -3.0492 |
| Return YTD (%) | 44.8896 |
| Return 1Y (%) | 48.0281 |
| Annualized volatility (%) | 39.2236 |
| Beta vs SPY | 2.1441 |
| Max drawdown (%) | -21.5466 |
| Sharpe (rf=0) | 1.1998 |
| Downside deviation (rf=0, %) | 26.0366 |
| Sortino (rf=0) | 1.8075 |
| Historical VaR 95% (1D, %) | 4.1383 |
| Historical ES 95% (1D, %) | 5.1216 |
| Correlation vs SPY | 0.6943 |
| Tracking error vs SPY (%) | 31.7498 |
| P/E (trailing) | 28.31 |
| P/B | 83.37 |
| EV/EBITDA | 4.13 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 18.68 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 58.66 |
| Return on equity (%) | 41.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 433.7490 |
| Close vs MA50 (%) | 0.7195 |
| MA200 | 397.1737 |
| Close vs MA200 (%) | 9.9947 |
| RSI (14, Wilder) | 50.6914 |
| MACD (12,26) | -4.9155 |
| MACD signal (9) | -2.6590 |
| MACD histogram | -2.2564 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 269, 'SPY': 269}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 436.8700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.9455 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.7736 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -3.0492 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 44.8896 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 48.0281 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 39.2236 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.0366 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.8075 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.1383 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1216 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6943 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.7498 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.1441 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -21.5466 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1998 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.6814 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 58.6550 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8550 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 28.3130 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 50.6914 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.2564 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.7195 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.9947 -> Clearly above the moving-average trend level.

## TAILWINDS

### Taiwan Semiconductor Manufacturing Co Ltd Stock (TSM) Moved Up by 3.04% on Oct 27: What Investors Need To Know
- Summary: TSM shares rose 3.04% on Oct 27, indicating positive investor sentiment and potential short-term upside.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxOaG5CWk5SejZ1OHJIM0xfMWdiUTUzRWViWUNudzIyZlBGWWRDdEhuUWpZbnhNZng1OHdoZWxrTDN2UlhGOXlDSEljSjh1eGs3MlNxTk5ENXdsR3VjcVdxVUZST3JBNmtJVFkySWRlNmJKWjF5eFRVdEI4MTRBQl9laUxxZ2lPU3gzQWc?oc=5>

### Taiwan Semiconductor Manufacturing (NYSE:TSM) Stock Jumps 3% - Should You Buy?
- Summary: TSM stock increased 3% on NYSE, suggesting a favorable short-term market move for investors.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxQZXI1X3lsUEdCTUVncTBaaTlJaWlqMGRfWlZ3Z293d1hqb0NidmY5WFVfVF9lLTFwM25VeUxKWHBSSkZKTmtUMUlYZGI3TTF0aTk3Yi1paEt0eHd0LUtlQzRJLTVlTDlVYkV0bEItYUJSWDd5VlotRkdyYWhROWU2YjVrMEZnSWdWVThSWE9weUtZZnAwbXdpMXgyV2dNQ2c5bncybU8xYWFFWDBBU1FOT1V3UkRwaW9KU2JoQVNDak1NWnBLTFliZkhWQ1Q?oc=5>

## HEADWINDS

### Taiwan Semiconductor Manufacturing (TSM) Stock Looks Pricey Against Cash Flow
- Summary: Valuation concerns relative to cash flow.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxORldEaFpNSnljQTZVWGtRUmV3X0R2QTZQTE9pNm0yWDlremFDNV85cHVhRnlZTy02c2Zkd0dsTTE0Zkx4LWJibjZVR0RHWlhZdy1WcHRVZ2dHQlpHOWxGWEVHUnlJRU5mcFVhU1FnWXk5TzB4ZFdMYjkzRDctYjJ0d0tYeGxfbHlBU1ducHNRZEFOYkwzZy1TTXRGNjRkcDlZZTUwcDNLdlZXSGFsb3c?oc=5>

## CATALYSTS

### TSM Q3 Earnings Call Highlights Strong AI Demand and Expansion
- Summary: TSM Q3 Earnings Call Highlights Strong AI Demand and Expansion
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPQ2xSQ3FXUFVrcEpDVVdKTGV2aHR0UXA5bnRvOXdXVHZkNU5ENl9lZXNpRDNiUU9PVHA2b2JEdkdzVVhBTE5ORkRaeTV0dTBXT1NaV1FpQnhzcG1uODQ4ZHFDdGpfdWFJSHAyNEoweXhEZ0RZbi1XX3BONWFMTzNlRnY1OVZCR2ZLNi1rT3poRFhmYVBuSGN1bFhlQURXMm9TbnFJVzVEenNwWENtajRyZkZEaEtNZDBZemc?oc=5>

### Taiwan Semiconductor Manufacturing Company Limited 2026 Q3 - Results - Earnings Call Presentation
- Summary: Taiwan Semiconductor Manufacturing Company Limited 2026 Q3 - Results - Earnings Call Presentation
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxQcUd6a0dTbklKcC1hSlZQQXp5VnRWZUszUE9iaEhtcWJ4eFN0SHItNG0tV2tKVnZqSjZCM2N2c0dLMVQyQURGR05QV0dBdkpGWm9DcUNVRENHZWEzUkg4UVZfckpoTGZxLUVYYk1CTnUzWXhTcTc1YllhbFhaeW1FT2VLdE43cTBwLTFOcEl4Y1d0NmFwY0NEZEd3bFh1cktLTkJXd0VoTV9PSmVZbU1aM3M2RkNfVkMtbzJDWTFnUUF6SXJ6TjlNSjJRUE95YTQ?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) Draws Fund Managers Leaving Firms To Invest Personally
- Summary: TSM attracts fund managers who are investing their own money in the company.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxQNWwxM1BhNzBha1B4WGV1WDllaDBXMVByYW9peGwxSmE0WWotQ09qQWlhc3RFMS1TTkhIbDBEcXZGZ2FIRXVlX3Q1UkRDUTJXbjlZNFI0YXcwTVV1OWZXVUhBYTk5bnlqWVJXQUlCUzlxSGVPaVg5UFV3WjVzbnZTV0l3VTNmSG1YbXVNNUdtTnB5cVEtWVRJcFlSbTEzTUNIWUpfcWZKMU1tdzd5alE?oc=5>

### Why TSMC's Q3 2026 Results Highlight Pitfalls In The AI Hype (NYSE:TSM)
- Summary: TSMC’s upcoming Q3 2026 earnings may reveal challenges in AI demand, potentially affecting future revenue growth.
- Date: 2026-10-27 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQZEN1M1JmbHlBV3NidEFjN2xfTF9CazJKaTRUT0JJblVyZ3ZVcjNCNC1pdDFrSFFQcEFUOF9Lb1RtU0hnYUxwblQ5Y0tjSXlvZHlnVlZqaHdUZ1JCblZGRHZLT2xucHVVSElKOEtnSlVZaWpwZjRlTUw1Q2J3VUtfWFU1RWl5Y3ZSOUw5bmRJSndxcFVzMGZxQXpiZTJJdzlsNEE?oc=5>

### TSM vs. MU: Which Semiconductor Stock Is the Better Buy Post-Earnings?
- Summary: Analyst comparison of TSM and MU post-earnings, evaluating valuation and growth prospects.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQMTFTOFFaSGRRUElGckpCT00zVmhxT0o0X1k3di00ejZWSEVIV1g4QXFVdUd4SXFfRk5wTGtnRUtnUVhPX1pOZVpsVnlDQlg4YmdBeGw4emY5N0VMLWt1dmxVa0wwOHRLSUxuOW42OGZ6aWNoN0pQWWlTR3NTd280ZUM2T3pMSUVxYlVSTzZxQjNaTElSUmVMbldR?oc=5>

### Bull of the Day: Taiwan Semiconductor Manufacturing Company (TSM)
- Summary: Positive market commentary highlighting TSM’s strong performance and investor sentiment.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxOSlQ1eDdidUUyaGxEMXNHVXJfdlFyX2lMaFplZmxfU3lzQlF0LVVoMVZYekpvUzg1Q05fTzhxREJ5dFl0ZkRqZi1iUktLWTdpbHZNajJQMUNZSnE5cUdRMHRtejFvcjFKTUlxM29TdDFLWFdGdkdJWXFnRlQyNEd3bmt5blFmc1E0TVY5RnJaeDAtbktxbXI0WVRBZVdBbm9NZUhTanZSQWZjOVpoWjkxdkcyUFYyYzJXS3ZfenRReFBXdWdHSTQtOWVLM3FpdGlXT3M1djdhR0xqR1VpWElBUkZn?oc=5>

### Cathie Wood Sells $22.5M of AMD and TSMC Stocks, Buys $6.8M of Two Air Taxi Stocks
- Summary: Cathie Wood sold $22.5M of TSMC shares, reducing her stake.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxPSlNYSE5WdlB6cGxpTnlNZjUtNHpXc2hSVHo5RFdWN1VhVmphSjBHUWV6Vm5IVTZEZ2pvaXFkZXQxMTU4S095bWk0Z1ZVb1N0LWc3UURyeXFDR2hJT0NtUmVsTlNRZjZyV1RIOTZTVDhaenZhaTR0SkhuZTl3S0xwbUdRWmtVbFBQYmg1dGt4NnJhZTlrUnJYVGEwSjNFNFV6THR1aU9Nb2FTZjF4NEE?oc=5>

### TSMC: The Toll Road Of The AI Economy Is On Sale (NYSE:TSM)
- Summary: TSMC highlights its role in AI economy, suggesting growth potential.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNMXNDRzVKSl9XSDFyUlRwRWctZzJFQVExcGZsZmhKZzVfUnRTYUtlUm5TTHZPR1dZakx3c2VEUjBtTWxGdjFoODB3RFFOVDE0Q1BKVGRpRW1hTzdxcHUxbjVkcUdLWGVfVWx1RVNCN3lWbjZOcGI2cUVlNHVwTWUwUVJ6OGlLcnp6RmV5WjBaRFhfUQ?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) Stock Looks Reasonable With Cash Flow Priced For Growth
- Summary: TSM’s valuation appears fair, with cash flow supporting growth expectations.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxPZzdQdWg1cXVkY2ZuSlk0cmt6STFjUlhTb1pqeEYwNGFlQTFyY25XUllPSkxCZF9sR1RqZjlCSlR3WE9WNkNTWVFrVWFMSzFkZVEyZ2dtU2xyeDJxNGZreFhnSGZDTDBOUFRqS1paV0cwNnNYZnowcGliVTJKOVBvNWxhTmNQektOc2cxenN2ZGRGd3J5TlhLc25rNF92VTcxcnBqaTRFbnR0ckJWQlQwSGFNRlNWY09GempVUVlqODZPS2UzZHVLUFU5NUNUNzB1QkY1ekIzdlh2R3MyTzZjVWZrNC1TVDA2ZkdpWNIB8gFBVV95cUxOX3pRSEt3eUVqeVZjNGsza3ZEUFEyOGtOa0xaUDJWTDNzcllUbGZqaERPaUdOenpkTFBaZEJqSFFRNWhXanJ0aC1rZEJhQ0N1S3dlSHZEbGx1TUtEemppY2JuV0JRcWhDYWZMVzBJTTc5c3lFejZjYnRkNXEwZUFleTBGZTZGUW5qc2x5eUh5c2FmSGlZTHJiWktKU1B1U3Y3OHhMRVZFUEVPS2pwNjc2XzNuc1BYelFMME1xVXdISlhjbkJzYlRSY2xzbzROYldXcHliRDF6NGcxQS05eGtPRjdpYThUckNEOFlJWTRpc3dfZw?oc=5>

## RISKS

### TSMC to raise advanced chip packaging prices by up to 20%, report says
- Summary: TSMC plans to increase advanced chip packaging prices by up to 20%.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxNTDRSLV9rNmhWLXNCMm5id0w4Wi1uVU5ySHZSR0ZXSGQwZEQwaExrMnNMWGMxa0pYbktnLS15WGswZUxVOE8xY0dfVWItc0RHYjlGVnQ0UFdvOWZYMVRJRldqbFNiVDdTVUlXby1sY2tDQ2ZzR3hiLVZuWWs0cHlXRFE1ZWVvMUZVc1A2TmV4OTgwZlRzMm42eW1fTlZMcktmYmZQQ3pqUllZenZlQU5RNm5oREhJazYzbm5fX1hFZkFuVUE?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **28.31** | **83.37** | **4.13** | **50.90** | **2,265,814,925,312.00 USD** | **48.03** |
| UMC | 19.65 | 3.57 | -0.32 | 17.00 | 48,778,825,728.00 USD | 161.46 |
| GFS | 36.48 | 2.17 | 12.62 | 5.80 | 26,031,450,112.00 USD | 32.37 |
| INTC | N/A | 5.40 | 30.24 | 25.40 | 495,519,465,472.00 USD | 137.08 |

Peers fetched as_of: 2026-10-27; TSM reuses existing data (market data as_of: 2026-10-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMiigFBVV95cUxOaG5CWk5SejZ1OHJIM0xfMWdiUTUzRWViWUNudzIyZlBGWWRDdEhuUWpZbnhNZng1OHdoZWxrTDN2UlhGOXlDSEljSjh1eGs3MlNxTk5ENXdsR3VjcVdxVUZST3JBNmtJVFkySWRlNmJKWjF5eFRVdEI4MTRBQl9laUxxZ2lPU3gzQWc?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxQZXI1X3lsUEdCTUVncTBaaTlJaWlqMGRfWlZ3Z293d1hqb0NidmY5WFVfVF9lLTFwM25VeUxKWHBSSkZKTmtUMUlYZGI3TTF0aTk3Yi1paEt0eHd0LUtlQzRJLTVlTDlVYkV0bEItYUJSWDd5VlotRkdyYWhROWU2YjVrMEZnSWdWVThSWE9weUtZZnAwbXdpMXgyV2dNQ2c5bncybU8xYWFFWDBBU1FOT1V3UkRwaW9KU2JoQVNDak1NWnBLTFliZkhWQ1Q?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxORldEaFpNSnljQTZVWGtRUmV3X0R2QTZQTE9pNm0yWDlremFDNV85cHVhRnlZTy02c2Zkd0dsTTE0Zkx4LWJibjZVR0RHWlhZdy1WcHRVZ2dHQlpHOWxGWEVHUnlJRU5mcFVhU1FnWXk5TzB4ZFdMYjkzRDctYjJ0d0tYeGxfbHlBU1ducHNRZEFOYkwzZy1TTXRGNjRkcDlZZTUwcDNLdlZXSGFsb3c?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPQ2xSQ3FXUFVrcEpDVVdKTGV2aHR0UXA5bnRvOXdXVHZkNU5ENl9lZXNpRDNiUU9PVHA2b2JEdkdzVVhBTE5ORkRaeTV0dTBXT1NaV1FpQnhzcG1uODQ4ZHFDdGpfdWFJSHAyNEoweXhEZ0RZbi1XX3BONWFMTzNlRnY1OVZCR2ZLNi1rT3poRFhmYVBuSGN1bFhlQURXMm9TbnFJVzVEenNwWENtajRyZkZEaEtNZDBZemc?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxQcUd6a0dTbklKcC1hSlZQQXp5VnRWZUszUE9iaEhtcWJ4eFN0SHItNG0tV2tKVnZqSjZCM2N2c0dLMVQyQURGR05QV0dBdkpGWm9DcUNVRENHZWEzUkg4UVZfckpoTGZxLUVYYk1CTnUzWXhTcTc1YllhbFhaeW1FT2VLdE43cTBwLTFOcEl4Y1d0NmFwY0NEZEd3bFh1cktLTkJXd0VoTV9PSmVZbU1aM3M2RkNfVkMtbzJDWTFnUUF6SXJ6TjlNSjJRUE95YTQ?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxQNWwxM1BhNzBha1B4WGV1WDllaDBXMVByYW9peGwxSmE0WWotQ09qQWlhc3RFMS1TTkhIbDBEcXZGZ2FIRXVlX3Q1UkRDUTJXbjlZNFI0YXcwTVV1OWZXVUhBYTk5bnlqWVJXQUlCUzlxSGVPaVg5UFV3WjVzbnZTV0l3VTNmSG1YbXVNNUdtTnB5cVEtWVRJcFlSbTEzTUNIWUpfcWZKMU1tdzd5alE?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQZEN1M1JmbHlBV3NidEFjN2xfTF9CazJKaTRUT0JJblVyZ3ZVcjNCNC1pdDFrSFFQcEFUOF9Lb1RtU0hnYUxwblQ5Y0tjSXlvZHlnVlZqaHdUZ1JCblZGRHZLT2xucHVVSElKOEtnSlVZaWpwZjRlTUw1Q2J3VUtfWFU1RWl5Y3ZSOUw5bmRJSndxcFVzMGZxQXpiZTJJdzlsNEE?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQMTFTOFFaSGRRUElGckpCT00zVmhxT0o0X1k3di00ejZWSEVIV1g4QXFVdUd4SXFfRk5wTGtnRUtnUVhPX1pOZVpsVnlDQlg4YmdBeGw4emY5N0VMLWt1dmxVa0wwOHRLSUxuOW42OGZ6aWNoN0pQWWlTR3NTd280ZUM2T3pMSUVxYlVSTzZxQjNaTElSUmVMbldR?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQaENOcWdsTlVLMWFHLTlhTzRpR0lrNzZiRDV5dzRZNUphdUwtbkZNTGVaWlJOMWpUbkNxVTlXa05mWWplY2YzRjBIVzR1Q19XRkFmX1drWUZuRkNOMng4ZF96Rk5zdFhqWXlnb1l4aXpJeGplRVYwbS1kcV9IakliUFdDVmhSV0pnaklnODZHa0h2VjVET0lRUlVrN0dKTU82UWtKYTZJaVJUak5I?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxOSlQ1eDdidUUyaGxEMXNHVXJfdlFyX2lMaFplZmxfU3lzQlF0LVVoMVZYekpvUzg1Q05fTzhxREJ5dFl0ZkRqZi1iUktLWTdpbHZNajJQMUNZSnE5cUdRMHRtejFvcjFKTUlxM29TdDFLWFdGdkdJWXFnRlQyNEd3bmt5blFmc1E0TVY5RnJaeDAtbktxbXI0WVRBZVdBbm9NZUhTanZSQWZjOVpoWjkxdkcyUFYyYzJXS3ZfenRReFBXdWdHSTQtOWVLM3FpdGlXT3M1djdhR0xqR1VpWElBUkZn?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQM2NXeFZEN1AwYlZkSmdSTEdHelNieFFYSkZQaWR5RHJRVnAyRHIweXZ4Ny04TkdhNkpxa3ZiZXF2XzVwUVFnMEppRG00YnJ5TTFFa2xSVXU1a25mcERMLU9FY2d1clFld2pXU2QwTzdYZ2tnWVVMYU01MkhDbUlWeUF1UVdNU1I1bWtoZFRfZ2lmX09fcHY4d21XWXBadE43S1BrVC1n?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPSlNYSE5WdlB6cGxpTnlNZjUtNHpXc2hSVHo5RFdWN1VhVmphSjBHUWV6Vm5IVTZEZ2pvaXFkZXQxMTU4S095bWk0Z1ZVb1N0LWc3UURyeXFDR2hJT0NtUmVsTlNRZjZyV1RIOTZTVDhaenZhaTR0SkhuZTl3S0xwbUdRWmtVbFBQYmg1dGt4NnJhZTlrUnJYVGEwSjNFNFV6THR1aU9Nb2FTZjF4NEE?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNMXNDRzVKSl9XSDFyUlRwRWctZzJFQVExcGZsZmhKZzVfUnRTYUtlUm5TTHZPR1dZakx3c2VEUjBtTWxGdjFoODB3RFFOVDE0Q1BKVGRpRW1hTzdxcHUxbjVkcUdLWGVfVWx1RVNCN3lWbjZOcGI2cUVlNHVwTWUwUVJ6OGlLcnp6RmV5WjBaRFhfUQ?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxPZzdQdWg1cXVkY2ZuSlk0cmt6STFjUlhTb1pqeEYwNGFlQTFyY25XUllPSkxCZF9sR1RqZjlCSlR3WE9WNkNTWVFrVWFMSzFkZVEyZ2dtU2xyeDJxNGZreFhnSGZDTDBOUFRqS1paV0cwNnNYZnowcGliVTJKOVBvNWxhTmNQektOc2cxenN2ZGRGd3J5TlhLc25rNF92VTcxcnBqaTRFbnR0ckJWQlQwSGFNRlNWY09GempVUVlqODZPS2UzZHVLUFU5NUNUNzB1QkY1ekIzdlh2R3MyTzZjVWZrNC1TVDA2ZkdpWNIB8gFBVV95cUxOX3pRSEt3eUVqeVZjNGsza3ZEUFEyOGtOa0xaUDJWTDNzcllUbGZqaERPaUdOenpkTFBaZEJqSFFRNWhXanJ0aC1rZEJhQ0N1S3dlSHZEbGx1TUtEemppY2JuV0JRcWhDYWZMVzBJTTc5c3lFejZjYnRkNXEwZUFleTBGZTZGUW5qc2x5eUh5c2FmSGlZTHJiWktKU1B1U3Y3OHhMRVZFUEVPS2pwNjc2XzNuc1BYelFMME1xVXdISlhjbkJzYlRSY2xzbzROYldXcHliRDF6NGcxQS05eGtPRjdpYThUckNEOFlJWTRpc3dfZw?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNTDRSLV9rNmhWLXNCMm5id0w4Wi1uVU5ySHZSR0ZXSGQwZEQwaExrMnNMWGMxa0pYbktnLS15WGswZUxVOE8xY0dfVWItc0RHYjlGVnQ0UFdvOWZYMVRJRldqbFNiVDdTVUlXby1sY2tDQ2ZzR3hiLVZuWWs0cHlXRFE1ZWVvMUZVc1A2TmV4OTgwZlRzMm42eW1fTlZMcktmYmZQQ3pqUllZenZlQU5RNm5oREhJazYzbm5fX1hFZkFuVUE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
