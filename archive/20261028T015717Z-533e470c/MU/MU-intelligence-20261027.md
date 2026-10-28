# MU Intelligence Report

- ticker: **MU**
- Report as_of: **2026-10-27**
- Market data as_of: **2026-10-27**
- Quant sources: https://finance.yahoo.com/quote/MU/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MU/key-statistics/
- AI analysis snapshot as_of: **2026-10-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-28T02:03:33.211801+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 2, 'ai': 12, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261027T014607Z-b66f6bd5/MU** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 12 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 29.17%; oldest publication 2026-10-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 928.7600 |
| Return 1D (%) | 2.7730 |
| Return 1W (%) | 3.6482 |
| Return 1M (%) | -14.1714 |
| Return YTD (%) | 225.6506 |
| Return 1Y (%) | 322.4511 |
| Annualized volatility (%) | 81.3008 |
| Beta vs SPY | 3.3825 |
| Max drawdown (%) | -39.0954 |
| Sharpe (rf=0) | 2.1834 |
| Downside deviation (rf=0, %) | 48.9009 |
| Sortino (rf=0) | 3.6301 |
| Historical VaR 95% (1D, %) | 7.0055 |
| Historical ES 95% (1D, %) | 9.5345 |
| Correlation vs SPY | 0.5284 |
| Tracking error vs SPY (%) | 75.3648 |
| P/E (trailing) | 12.50 |
| P/B | 7.59 |
| EV/EBITDA | 9.30 |
| Revenue growth (%) | 379.30 |
| Forward P/E (estimate) | 4.49 |
| Gross margin (%) | 80.72 |
| Operating margin (%) | 80.68 |
| Return on equity (%) | 88.26 |
| Free cash flow yield (%) | 2.77 |
| MA50 | 979.5824 |
| Close vs MA50 (%) | -5.1882 |
| MA200 | 737.6967 |
| Close vs MA200 (%) | 25.9000 |
| RSI (14, Wilder) | 46.0614 |
| MACD (12,26) | -31.6398 |
| MACD signal (9) | -23.5918 |
| MACD histogram | -8.0480 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MU': 269, 'SPY': 269}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 928.7600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.7730 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.6482 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -14.1714 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 225.6506 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 322.4511 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 81.3008 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 48.9009 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 3.6301 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.0055 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 9.5345 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5284 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 75.3648 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.3825 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -39.0954 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 2.1834 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 4.4891 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 80.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 80.6780 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 88.2600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.7731 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 12.4951 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 46.0614 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -8.0480 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.1882 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 25.9000 -> Clearly above the moving-average trend level.

## TAILWINDS

### Micron Technology (MU) Stock Rises 2.5% on Bullish Outlook from Bank of America
- Summary: Micron Technology (MU) Stock Rises 2.5% on Bullish Outlook from Bank of America
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOTi1sQmRCX2tzWWlIZlhMdWdPejVZOTRaejM3d1dFVnNfcjE5VGVnaTgxbTV1cDJHUnZOUHJJSG12RXM3N0RUOEpZLVZ2d2x3QnlhNU1OeHU4M3hfbENvaDNyMXVpSEt2emx3Nk44NDNXVlpsNVhxOS1idjVzR3JyUTB3TkxsLV9OeEFtY0xyQ0tnQ1A4Y01tSkRmQkl4aEFXRlV3VlNpaWlfSlRJVGZBM3BrcWw?oc=5>

### Micron Just Unveiled a New Bonus Plan. What That Means for MU Stock.
- Summary: Micron introduces a new bonus plan, potentially boosting shareholder value.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPSVp0SEVqV2ZKY1BKYXJGZXhZcGZNVzZwdnBrV0NhWGtTaTEwMVNBb0hjZEx4b1VYR1B6UzdJNzdXaE5OZFhSZzhZQlhhWmNSelFxYXRCaG8tTEVHRU9DZE5TcmZDaXdHRzdBTjhlbDhqNGM2d1lQbnZpbVdlb1ExSTlXaDB3UzhXd081UzU1Wkp0OE9YT1pOWFFUZjR3V252TkxBTHI1T3J5aEdzdDcw?oc=5>

### Micron, Musk, and Memory. A Big Prediction Is Lifting the Stock.
- Summary: A prediction involving Micron and Musk is positively influencing the stock.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTE1NSnA4QTg5U0hoaGRRRFdFZC1wS2REemx2em5RTHl0Q3R6YVFQSW1QVmFaTTBGM3F0N0RWT2ZWTm5WeDVIODVqUHN5S3hBeExPRXVJZ08wQ2JBejJtVHRBYVRnRnpPbFNOcldMcVV1ZEhiZDdIQUJDY2JJVWI?oc=5>

### The Memory Bottleneck Divide: SK Hynix Sells out to Tier-1s, Micron Absorbs the Spills
- Summary: Micron benefits from SK Hynix's sell‑out, absorbing excess supply.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNRGQ3ZGk0YUlTcXhNWHBPMkJWbDJROVQzdUM4MnZCd080S3BDeC14NVp2YjhCdXI5NTdqY3d3VV9EaWFyeDdXYl90bjVBWWlDZGRPbWFEWl9YdjBYUEw4Q082aTN2Zk1pZWRGSGtnQ05wdW1ETnVpNmNQdjhxdzV3azk1UG5FdFhHdW5IZnY0NUxqam0wYzBCQUhKV2IyX1NOOU96WUUxeUZVVHBPajdmYVFrWVU4RndIckphekdDc0JFTFhHdjRj?oc=5>

## HEADWINDS

### Stock-Split Watch: Is Micron Next?
- Summary: Uncertainty over a potential stock split may affect investor sentiment.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxNOHYtZHJvQ0tOM0VDOTlZeWdQTmYwY2JSSGpZS1ROYWRHMi1xQWdxN1d5Tk96dDR3ZFQ2ZnhKTDlUOExWRV9JUW83ZkQwb2RtMHE2U1FXNk9kbjRUeXlaaDZ3R3dZMk1FNDgwUjVMUk02bU9hUzFyQ3NrUFo4cE9sUA?oc=5>

### SA analyst upgrades/downgrades: GOOG, MSFT, NBIS, MU
- Summary: Analyst changes for MU could impact market perception.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxPMDhIM08yQmdNbkJDS2lzak9KeTdRMkpndnZjNmNvZE9EaE1sNGNoaDhqTGNWT21VVVhLRTZfbGxkdmQ3Y05RMW83Ml80YXVqYmtXR2VXTkZsWXg5eVB0a2QtLUFERTNoVUtwc1BJTjBNT2p1Y1JJbFlKdzRSVWt4MWFYS1ZOYW1WRUprQ2h3?oc=5>

### Micron Just Rejected a Technology Its Biggest Rivals Are Chasing. Here’s Why.
- Summary: Micron declined a technology pursued by competitors, potentially limiting future growth.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxONmVyMVg4dW5lTFlWSUllcVNuUE0zc1h5eWV2NW1GMk1keFFWWnBtYnFFbkZNckNyZHJoRjdGU2V2dXZKWWRVX0haNjhqMWFCMnlESXk2dHN0cUZ2TUhJSnZxeHVSZ1RwbDBXWWxBeHpJNHhINmYxT0xfMXBEbmRLWERXN0U5SDQ5LUg4RkJvUkpYYm5yeWpheUhIckY2SWdIYWc?oc=5>

## CATALYSTS

### Micron Technology Stock: Is Now the Time for Investors to Take Profits or Buy More?
- Summary: Micron Technology Stock: Is Now the Time for Investors to Take Profits or Buy More?
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPNDVmcHh4WlRMQVZydHJ2QnRCM0E3NF9aTGd1OTRVM016LWxQU2JSLUQ0Q3NKbHVaSmRfZXVYOEhac1hkSGJHSG43elF6SEtOXy1PYW5sWk9VbUV1MWNkVU1SZ3RlM25VbUFiVUxNM0tFdTh3NEtZUnExaUd5REJEQUdyVXZEMVhNcEdiMlp5OERHUnFRVGpxYXBDYVN3NjJtcG91WUxfOVZzQnpaMzQyb1JBRTRIQ2VtUFlWYkNuSnBmdw?oc=5>

### Micron Just Revealed a New Business Strategy. That Change Makes It a Screaming Buy.
- Summary: Micron unveiled a new strategy, signaling growth potential.
- Date: 2026-10-25 | Impact: high | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxONzJEanVQYlFGY2pNd3VnRC1zZllfbG1LLVRsVWwtbGtMNVNsVWZ4Y3k5M09OZTBNdWdTUEVScUVMeXY5N0I2UElNVFdkNUh6R2IxUnlWMkFJQXA4Nm5rZ3VUNGlIOXVqSnEteHRQekhOS2I4YUs5RmtlQ1RxUi1tTmpSUFJjQXlpa1pnc2steERfdGRMaGFtby11cWdzTXZEcTV5alhR?oc=5>

### “Durability and Predictability”: Micron Is Up 200% in 2026. Take Profits, or Buy More?
- Summary: Micron's stock surged, prompting buy/hold debate.
- Date: 2026-10-26 | Impact: high | Horizon: long | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxNeVJqX0Z5T2dHeTN6M0pFN2pJU01oTmpnN0h1T1RFVmNBb3IxMzBNZzBieDV1RlExRUY2Q2FkRkZJYV9QMGc4N2pYR3NTdjBCQ0Z6OU5SXzRSeHVldmNfR1kwS1Nob2VOUklvV2hwZWw1blJibkMwTXhMNkFjQlRta1FNT1A1VllGdmZZWWpQSjNoMlFXcUl0MUcxR3J1SGhnUTRuYkU2cmJEZw?oc=5>

### After Two Spectacular Micron Buy Ratings, I’m Calling It Quits (Downgrade To Sell) (MU)
- Summary: Two analysts downgraded Micron to sell after strong buy ratings, signaling a shift in outlook.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxOSnRNMG1HUzBaZFhtVjE1LU5pMVZ2RExucVN1OWlCX2tmU3I5YW00TDBtSG9jR0E4bG40QzNzV1liM2w0R1JjR3kxZC1fLUNhUmNRSzhYeGlkTTYyU09tVGJnUDd6MVp2TW12Sk40ZHdXUWxNSXJoblZQQkN3UEJHWDVyaFpOV2dnR09JWGxDWGRLdkl3ejV5LWlZWFVmLTVEdkM1RjJqMC1SSzBkUlljUVluTE43eUNpU0l0Xw?oc=5>

### If You Invest $1,000 in Micron Today, Here’s What It Could Be Worth by 2030
- Summary: Projected future value of a $1,000 investment in Micron by 2030, based on current performance.
- Date: 2026-10-26 | Impact: low | Horizon: long | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxPQmQyNldxZjlIVW9tVzdRaG5hbW43dUtNVjRaY0YyT09aU1NWT3RucDJQTzM1UzFnZzdoR19nRERPdEU1Q3FFSFRBSnlzMklXUFh1YjlZX3NBc2g3X3Y2S0EwUmhkUVhOaEdRRFlROGRUVjBRbDFoLXZ1YjJCNl9GUVRSZWZOaDRDbDVQWUUtSmg4NHM0V0Q2aDA4amNWazhlM2dLQ1NYY1JIT2xGWUFjWGxmT2Z1dw?oc=5>

### Micron Just Delivered a Monster Quarter, but the Stock Is Plummeting. The Reason Is Obvious.
- Summary: Strong earnings reported, yet stock price fell sharply.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOaG8tM2JnYmdKRVRUTjhrVVpYT3l0a2J6VDNhYkJlTjVHNzdhYzNQVmlPNDdPd2paOWZ2LUxDVzN0MGNBbFdoQmZkaGZsM3pBQ0Rwbm8xRC04SFBtQ0NEM09ueFdsTDRycHp0NnloNGNGZWZNTnd3S0VJeS05dmwzcU02RV9iRjlLWGNlTmE5R0tybUNOU21NNFFoQUNMb3FFLXloUA?oc=5>

## RISKS

### What Could Micron Technology (MU) Strike Risk And Supply Moves Mean For Investors?
- Summary: Potential risks and supply chain moves affecting Micron.
- Date: 2026-10-23 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQc1NSLUxySzlsNnBqd2dQNjhQeHliel8wRHFXNmR2WFpIbFhRbnVobnFaQXBtOXAwTGh1R2hLajFKcHVJcXU2cEx5d19UWXhFNDQ1aVlHYWxBT25DSGVrSzQ1UTN5R2pIVXFOZlBsSnJzSHZqTnhqUXVDUUZucWpoUnJSWXBvWjhOcXBxcEVQbWRuX2JGMHZyV2ZUS216dGM?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MU** | **12.50** | **7.59** | **9.30** | **379.30** | **1,050,820,673,536.00 USD** | **322.45** |
| WDC | 13.40 | 15.24 | 22.52 | 55.50 | 142,572,240,896.00 USD | 201.25 |
| STX | 48.05 | 69.90 | 34.11 | 48.50 | 151,864,410,112.00 USD | 191.68 |
| NXPI | 21.65 | 5.61 | 14.21 | 19.50 | 63,923,617,792.00 USD | 16.44 |

Peers fetched as_of: 2026-10-27; MU reuses existing data (market data as_of: 2026-10-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-30
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-09
- Revenue (latest available single quarter): 8,440,000,000.00 USD; period 2018-06-01/2018-08-30; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 28,243,000,000.00 USD; period 2026-02-27/2026-05-28; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMitAFBVV95cUxOTi1sQmRCX2tzWWlIZlhMdWdPejVZOTRaejM3d1dFVnNfcjE5VGVnaTgxbTV1cDJHUnZOUHJJSG12RXM3N0RUOEpZLVZ2d2x3QnlhNU1OeHU4M3hfbENvaDNyMXVpSEt2emx3Nk44NDNXVlpsNVhxOS1idjVzR3JyUTB3TkxsLV9OeEFtY0xyQ0tnQ1A4Y01tSkRmQkl4aEFXRlV3VlNpaWlfSlRJVGZBM3BrcWw?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPSVp0SEVqV2ZKY1BKYXJGZXhZcGZNVzZwdnBrV0NhWGtTaTEwMVNBb0hjZEx4b1VYR1B6UzdJNzdXaE5OZFhSZzhZQlhhWmNSelFxYXRCaG8tTEVHRU9DZE5TcmZDaXdHRzdBTjhlbDhqNGM2d1lQbnZpbVdlb1ExSTlXaDB3UzhXd081UzU1Wkp0OE9YT1pOWFFUZjR3V252TkxBTHI1T3J5aEdzdDcw?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTE1NSnA4QTg5U0hoaGRRRFdFZC1wS2REemx2em5RTHl0Q3R6YVFQSW1QVmFaTTBGM3F0N0RWT2ZWTm5WeDVIODVqUHN5S3hBeExPRXVJZ08wQ2JBejJtVHRBYVRnRnpPbFNOcldMcVV1ZEhiZDdIQUJDY2JJVWI?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNRGQ3ZGk0YUlTcXhNWHBPMkJWbDJROVQzdUM4MnZCd080S3BDeC14NVp2YjhCdXI5NTdqY3d3VV9EaWFyeDdXYl90bjVBWWlDZGRPbWFEWl9YdjBYUEw4Q082aTN2Zk1pZWRGSGtnQ05wdW1ETnVpNmNQdjhxdzV3azk1UG5FdFhHdW5IZnY0NUxqam0wYzBCQUhKV2IyX1NOOU96WUUxeUZVVHBPajdmYVFrWVU4RndIckphekdDc0JFTFhHdjRj?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxNOHYtZHJvQ0tOM0VDOTlZeWdQTmYwY2JSSGpZS1ROYWRHMi1xQWdxN1d5Tk96dDR3ZFQ2ZnhKTDlUOExWRV9JUW83ZkQwb2RtMHE2U1FXNk9kbjRUeXlaaDZ3R3dZMk1FNDgwUjVMUk02bU9hUzFyQ3NrUFo4cE9sUA?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPMDhIM08yQmdNbkJDS2lzak9KeTdRMkpndnZjNmNvZE9EaE1sNGNoaDhqTGNWT21VVVhLRTZfbGxkdmQ3Y05RMW83Ml80YXVqYmtXR2VXTkZsWXg5eVB0a2QtLUFERTNoVUtwc1BJTjBNT2p1Y1JJbFlKdzRSVWt4MWFYS1ZOYW1WRUprQ2h3?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxONmVyMVg4dW5lTFlWSUllcVNuUE0zc1h5eWV2NW1GMk1keFFWWnBtYnFFbkZNckNyZHJoRjdGU2V2dXZKWWRVX0haNjhqMWFCMnlESXk2dHN0cUZ2TUhJSnZxeHVSZ1RwbDBXWWxBeHpJNHhINmYxT0xfMXBEbmRLWERXN0U5SDQ5LUg4RkJvUkpYYm5yeWpheUhIckY2SWdIYWc?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPNDVmcHh4WlRMQVZydHJ2QnRCM0E3NF9aTGd1OTRVM016LWxQU2JSLUQ0Q3NKbHVaSmRfZXVYOEhac1hkSGJHSG43elF6SEtOXy1PYW5sWk9VbUV1MWNkVU1SZ3RlM25VbUFiVUxNM0tFdTh3NEtZUnExaUd5REJEQUdyVXZEMVhNcEdiMlp5OERHUnFRVGpxYXBDYVN3NjJtcG91WUxfOVZzQnpaMzQyb1JBRTRIQ2VtUFlWYkNuSnBmdw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxONzJEanVQYlFGY2pNd3VnRC1zZllfbG1LLVRsVWwtbGtMNVNsVWZ4Y3k5M09OZTBNdWdTUEVScUVMeXY5N0I2UElNVFdkNUh6R2IxUnlWMkFJQXA4Nm5rZ3VUNGlIOXVqSnEteHRQekhOS2I4YUs5RmtlQ1RxUi1tTmpSUFJjQXlpa1pnc2steERfdGRMaGFtby11cWdzTXZEcTV5alhR?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNeVJqX0Z5T2dHeTN6M0pFN2pJU01oTmpnN0h1T1RFVmNBb3IxMzBNZzBieDV1RlExRUY2Q2FkRkZJYV9QMGc4N2pYR3NTdjBCQ0Z6OU5SXzRSeHVldmNfR1kwS1Nob2VOUklvV2hwZWw1blJibkMwTXhMNkFjQlRta1FNT1A1VllGdmZZWWpQSjNoMlFXcUl0MUcxR3J1SGhnUTRuYkU2cmJEZw?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxOSnRNMG1HUzBaZFhtVjE1LU5pMVZ2RExucVN1OWlCX2tmU3I5YW00TDBtSG9jR0E4bG40QzNzV1liM2w0R1JjR3kxZC1fLUNhUmNRSzhYeGlkTTYyU09tVGJnUDd6MVp2TW12Sk40ZHdXUWxNSXJoblZQQkN3UEJHWDVyaFpOV2dnR09JWGxDWGRLdkl3ejV5LWlZWFVmLTVEdkM1RjJqMC1SSzBkUlljUVluTE43eUNpU0l0Xw?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxPQmQyNldxZjlIVW9tVzdRaG5hbW43dUtNVjRaY0YyT09aU1NWT3RucDJQTzM1UzFnZzdoR19nRERPdEU1Q3FFSFRBSnlzMklXUFh1YjlZX3NBc2g3X3Y2S0EwUmhkUVhOaEdRRFlROGRUVjBRbDFoLXZ1YjJCNl9GUVRSZWZOaDRDbDVQWUUtSmg4NHM0V0Q2aDA4amNWazhlM2dLQ1NYY1JIT2xGWUFjWGxmT2Z1dw?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOaG8tM2JnYmdKRVRUTjhrVVpYT3l0a2J6VDNhYkJlTjVHNzdhYzNQVmlPNDdPd2paOWZ2LUxDVzN0MGNBbFdoQmZkaGZsM3pBQ0Rwbm8xRC04SFBtQ0NEM09ueFdsTDRycHp0NnloNGNGZWZNTnd3S0VJeS05dmwzcU02RV9iRjlLWGNlTmE5R0tybUNOU21NNFFoQUNMb3FFLXloUA?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQc1NSLUxySzlsNnBqd2dQNjhQeHliel8wRHFXNmR2WFpIbFhRbnVobnFaQXBtOXAwTGh1R2hLajFKcHVJcXU2cEx5d19UWXhFNDQ1aVlHYWxBT25DSGVrSzQ1UTN5R2pIVXFOZlBsSnJzSHZqTnhqUXVDUUZucWpoUnJSWXBvWjhOcXBxcEVQbWRuX2JGMHZyV2ZUS216dGM?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
