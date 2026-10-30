# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-10-29**
- Market data as_of: **2026-10-29**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-10-29**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-30T02:39:43.044454+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 5, 'ai': 9, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261029T020157Z-688a53f0/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 1, 'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 13 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 40.91%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 566.4200 |
| Return 1D (%) | -2.0780 |
| Return 1W (%) | 11.5154 |
| Return 1M (%) | -6.7729 |
| Return YTD (%) | 164.4845 |
| Return 1Y (%) | 114.2852 |
| Annualized volatility (%) | 68.2180 |
| Beta vs SPY | 3.2487 |
| Max drawdown (%) | -27.7608 |
| Sharpe (rf=0) | 1.4603 |
| Downside deviation (rf=0, %) | 42.8497 |
| Sortino (rf=0) | 2.3249 |
| Historical VaR 95% (1D, %) | 5.8580 |
| Historical ES 95% (1D, %) | 8.2198 |
| Correlation vs SPY | 0.6053 |
| Tracking error vs SPY (%) | 61.3647 |
| P/E (trailing) | 144.49 |
| P/B | 13.75 |
| EV/EBITDA | 95.78 |
| Revenue growth (%) | 50.10 |
| Forward P/E (estimate) | 35.61 |
| Gross margin (%) | 55.72 |
| Operating margin (%) | 17.25 |
| Return on equity (%) | 10.20 |
| Free cash flow yield (%) | 0.96 |
| MA50 | 547.5834 |
| Close vs MA50 (%) | 3.4399 |
| MA200 | 409.0827 |
| Close vs MA200 (%) | 38.4610 |
| RSI (14, Wilder) | 50.8743 |
| MACD (12,26) | -5.2400 |
| MACD signal (9) | -2.7802 |
| MACD histogram | -2.4599 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 271, 'SPY': 271}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 566.4200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.0780 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 11.5154 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -6.7729 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 164.4845 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 114.2852 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 68.2180 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 42.8497 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.3249 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 5.8580 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 8.2198 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6053 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 61.3647 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.2487 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.7608 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.4603 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 35.6107 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 55.7240 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.2500 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.1960 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.9562 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 144.4949 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 50.8743 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.4599 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.4399 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 38.4610 -> Clearly above the moving-average trend level.

## TAILWINDS

### AMD (NASDAQ:AMD) Stock Surges 5% as US$1 Billion Meta Investment Boosts AI Partnership
- Summary: AMD (NASDAQ:AMD) Stock Surges 5% as US$1 Billion Meta Investment Boosts AI Partnership
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTFA1MXF5NFpBeU9EU2lfajFKTHFjZmpuLWg2aFNTZ3VkaWtsY0t4SVNJSlNWb1E1V2FCYnFnTU1kMVdkekx6MDB6bkVsaExRSFEwMFhvZjVCNE9FaG1ZLTQ2RjJlb2p1elpGS2NPQlhJaFA5anZwQ3EySQ?oc=5>

### Advanced Micro Devices Inc (AMD) Shares Surge 5.5% -- What GF Sc
- Summary: Advanced Micro Devices Inc (AMD) Shares Surge 5.5% -- What GF Sc
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPd29MNjIzX0M4T3ZFU0sxU3RubDZkb3MzNzZrUG9Tak03cjNzV2lVNTdRQ1JRX1hyY25IQmkybmh0VXB0MmhpQkVqUW8xaWx4d0I1Sm9vNGd0dHc5VDJKWjc5Q2wwYTBsdnkwdlRUdnZuaUdVVGtxeWFKRGwyUDhMMmFxc21MT05LbWE4M09tRWIxdFFuZGtoOVZVOXhGSXRRVXNYaE9TbmYteWhqanU0ckNOc2NVSEpTRkhuOXhR?oc=5>

### AMD Stock Outlook: AMD's Meta Deal Boosts AI Growth Prospects
- Summary: AMD Stock Outlook: AMD's Meta Deal Boosts AI Growth Prospects
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPX1V4WXJycDRlMFRxN1I5eEhncUplV3dncEZoRWFHNWlPaGd4WDlWY0NRczhpNHlJaFc4VnBkSk0xY213dnA1TkdvRktoclVUMkRYSG1ZMW5FQndXNEZ5ZFBybEloY21NS0R0LVg4ME5Fd1dpSHA3Rl9uZnA3WTUtYjl5LWd0MlY1OHVKaTkxVHFaZnJXblhyeGloTldpMHRIV3h3VHJXUQ?oc=5>

### Advanced Micro Devices (AMD) Rises Higher Than Market: Key Facts
- Summary: AMD stock outperforms market, indicating strong investor confidence.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNZzYtRE1JWERFWUdyTHdsRzdScUtHN3ZQRHlyZ3B2WW5qU3plWk9JWXc5Um9FZlJvOU03MkhKSFBnV2pCUTNqZjBvaVQ4eXJkamNnd01VNFp3MFZRY1M3R1VSNmlLNVNBa1pNclozc0FtU190NnV1U1ZpNlNGbWlVc3VXSkJNbGEzMTAtaEdtX1R5NWZOUjFFUmgtaDU2dw?oc=5>

### INTC, AMD, AVGO, MU Decline On Samsung’s Profit Miss, Lighter Capex From Microsoft, Alphabet
- Summary: AMD shares fell as Samsung missed profits and capex cuts from Microsoft and Alphabet were noted.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPc2ZMRUR5SGxXOExveVpWbURvMjlSc3lCcmIyN3EydF9CSjRkTVpTR1N1YkowTTlJVnE1RnBTSk1DNzBVV0hjRkFGNE9KbGFHSTBaN1o2MmNDaDlZbk1HRDh6Ui15WngzWjloUmJ4U3BWcllmNF9GYWc2WXk5c0d1c293bXZkNWptcXl4eVFrY0NGU0k?oc=5>

### Was There Any Sign AMD Stock Would Run?
- Summary: Questioning potential upward movement of AMD stock.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOS3R6ZFFtLVFoNFc1dldRRHZRa2F0RmdpSjF5OGJXVEFtUzcwczVESkZyb05PWVJ2Zkd4NEEzbXFHSGp0ckF6ZXdWNHBSN2JIV0I3c0tFUzRQdmxudDhGeGdibnNuVzVfV3Q1Ul9MNTRma0l5SVRqTENYLTJraGxGUnhwZkYwUGJib0U0bmhEYk5FYWNVSDgyRUViVHdXMnc?oc=5>

### AMD Stock Could Surprise on the Upside, but One Number Matters Most
- Summary: Analyst highlights upside potential tied to a key metric.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPalJsX05vVFplVmlJN1BKUWFuZHExNWxCUDBJUWJfRTk5Y2s1bWJibk8yUHVfTlY2LU9mWEhsaE9zbFdXbEJqdXNud3g0dTJUaS1iVUNZUnFKUjdfOEVMRHVrVkp1bVlkVkh0UEtUbjBUQVliVlUwYkVqTmFmWm9kUTZfV1hWN0M0UWxDWXVnTWlCeHVhTG9WVjlkTFFsTDRIRGFDUE9PY0NIX0hCZjlR?oc=5>

### Jefferies reiterates Buy on AMD stock, sees data center upside
- Summary: Jefferies maintains buy rating citing data center growth.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxQSjVabmw1RURDTERFdVV6NDljSThqVFJfWG51Qlk2dXN1MGRpY0YzazlLNGZ1dEl5eUs5REFUcXQ0Tk10dTBwWVdza1lDeFF5VWtHSjlFc2w5TEludmJKS0Zyb3lGdUFNME5KYVJFQjJZYmYxdUlHY2UtOEFBR21OLWo2ZnFZV2FvelpaWE5ldW5wbmhXR3NudThSbG5TNWhWSjg3XzhuMm9nUDk0aHdrLXhwQnpuSkJMOHVDckln?oc=5>

## HEADWINDS

### Advanced Micro Devices (NASDAQ:AMD) Stock Price Down 2.1% - Here's What Happened
- Summary: Advanced Micro Devices (NASDAQ:AMD) Stock Price Down 2.1% - Here's What Happened
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxOZzQyVjFnQzVIZlJBNVl2V1RKTDMzWUNYWTY0X25SbmZzYW13RXhXVXNJaEVhZm5WRlRhalktX25jUEFUdFMtS0pEaTdrUkJZa0pXYnpmWV9nMUZENy04VWxlaklma0JZa1N2M21ER3huTThfa0JmVWFiSnBXYkV4R1pmSy1kaU0xVG9oMGJ0dnQzbm1MUUYtQmJmWTgzUVJTX25yS2hwTHdBMUFjcWZUUks5WTVWWkp3dko1YWdZaDNGajh0WjBUa2R2ZkRKZw?oc=5>

### Cathie Wood Buys $7.37M in ACHR and JOBY Stocks, Sells More of AMD
- Summary: Cathie Wood sold additional AMD shares, indicating a negative sentiment.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQVUhoMzlONGZNdFZLNUJFMkRrMU5wS1JDWkdvM3ZxU3VDSGFubll3NnRlRTFzc0F2aGtaWjlzSEcxOHAyOXlGV0QxbE43MElNYVY0WmJ2THUxSlRoYWlkUUxRelJ3OVA3S3c1M3dLWDNzNnVOaVRXdlBsMDQxdFVWMWppUnRSNFdIS2U0TVNGOWdYSGt2ZmdPVk9R?oc=5>

## CATALYSTS

### AMD rises as GF ups price target ahead of Q3 results (AMD:NASDAQ)
- Summary: AMD rises as GF ups price target ahead of Q3 results (AMD:NASDAQ)
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQMk5SZjNON1Z0X0dORHRoNk5NRjZuZjRabmZXTE1tRTA5V0hiTGFRdEJLZUhDQ1VQUFRoTC1HTnc1OU5ZUGtWUTc4eENadTVRRTRsWlRmUWhRa1FXVk1UTm85b0x6NmdrTGZYRUl2TzhGc2lLcGpsRl84NFpiU09vbDl4UVl5cUdWZUo3cEdKN3FPdGc0?oc=5>

### AMD CFO Delivers Bullish Update That Investors Will Want to Hear
- Summary: AMD CFO issues a bullish outlook, signaling potential upside for investors.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNXzNrZkxRVlRMRDg4SUZYeVI4cDVqSTl3QkpXVkJ6MnlPVzBJZ3BoTWhYNGtKUTNVMGdaNUZTX3V6RGw3WVRpSEI0YTExbUZ1cmtva1hTM3FYamhTckJZb3dOaUdsSkZ6bkZaM1E2WERhMThUemEyLTZBYkNScTZiWTYyaTlVLUVLV1lNOUhrMFdVNVZSRkdvd0FzYlhHdXRw?oc=5>

### Advanced Micro Devices (AMD) Earnings Expected to Grow: Should You Buy?
- Summary: Analysts forecast AMD earnings growth, indicating potential upside.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNekRsZGVrS3pGUDBHdmNrOS1KREpLcUlEdmpDOElCcVk1RDB4WU5kdnM5ZTRLMzRsMU1MSm5tazAydTVPNWZ3aU0xa3F1RWV1M1VCYmpPeWEtSXpXTER5Smh4TGpGS3ZzSXhYU3FhMmgxUzVqazVLVlpKbmEyUE44ZmMzUUNHT3kxZHEwWUJJT1Y0Z3F6bW5vSmF5ajE4cTJBUXc?oc=5>

### AMD and Nvidia Split the AI Chip Market. 1 Stock Is Far Cheaper Today.
- Summary: AMD holds a larger AI chip market share, but is pricier than Nvidia.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPa05Cb1NpWEpwbmpNOVRNV3E4ZTZqNFFLTUhpNERwRWd5N2dlQkFIV05feGs0am5uSDFTWDAzNzRpRlYzdjVwdDdtaXQ5WGhyQTA1bURwT3AyMlpEV0F5LWY2MHpSUnM1SzZFaVN4bzdqdzRTYkY3bTh6M2FhWUk4TlVLUzQ5WVJuOGVtQVpCWUdDZw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **144.49** | **13.75** | **95.78** | **50.10** | **924,666,494,976.00 USD** | **114.29** |
| NVDA | 27.01 | 22.53 | 25.47 | 105.90 | 5,159,248,199,680.00 USD | 3.44 |
| INTC | N/A | 5.30 | 29.74 | 25.40 | 486,691,700,736.00 USD | 122.71 |
| AVGO | 44.06 | 16.52 | 32.19 | 85.50 | 1,646,902,378,496.00 USD | -9.95 |

Peers fetched as_of: 2026-10-29; AMD reuses existing data (market data as_of: 2026-10-29); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-29

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-05
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,297,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMieEFVX3lxTFA1MXF5NFpBeU9EU2lfajFKTHFjZmpuLWg2aFNTZ3VkaWtsY0t4SVNJSlNWb1E1V2FCYnFnTU1kMVdkekx6MDB6bkVsaExRSFEwMFhvZjVCNE9FaG1ZLTQ2RjJlb2p1elpGS2NPQlhJaFA5anZwQ3EySQ?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPd29MNjIzX0M4T3ZFU0sxU3RubDZkb3MzNzZrUG9Tak03cjNzV2lVNTdRQ1JRX1hyY25IQmkybmh0VXB0MmhpQkVqUW8xaWx4d0I1Sm9vNGd0dHc5VDJKWjc5Q2wwYTBsdnkwdlRUdnZuaUdVVGtxeWFKRGwyUDhMMmFxc21MT05LbWE4M09tRWIxdFFuZGtoOVZVOXhGSXRRVXNYaE9TbmYteWhqanU0ckNOc2NVSEpTRkhuOXhR?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPX1V4WXJycDRlMFRxN1I5eEhncUplV3dncEZoRWFHNWlPaGd4WDlWY0NRczhpNHlJaFc4VnBkSk0xY213dnA1TkdvRktoclVUMkRYSG1ZMW5FQndXNEZ5ZFBybEloY21NS0R0LVg4ME5Fd1dpSHA3Rl9uZnA3WTUtYjl5LWd0MlY1OHVKaTkxVHFaZnJXblhyeGloTldpMHRIV3h3VHJXUQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQSUsyenZQOEEyTkxVd29lMEFoRmFzWWRYVGlTZzVZcGdBZ0hwY3VjT0htaDQ2TDZWajB4dXF6YjZGeXRKVjMtM1A2Z2NGeWw3TGpCNEs1d1NIYUV0RU0wVU5qZWlQWE5pZENYWldWUkk1ekxjM0tYNXNRdzJLUEROM0lxQ3pySkQ4bklGMHRLQ1ItVmpBd2p3?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNZzYtRE1JWERFWUdyTHdsRzdScUtHN3ZQRHlyZ3B2WW5qU3plWk9JWXc5Um9FZlJvOU03MkhKSFBnV2pCUTNqZjBvaVQ4eXJkamNnd01VNFp3MFZRY1M3R1VSNmlLNVNBa1pNclozc0FtU190NnV1U1ZpNlNGbWlVc3VXSkJNbGEzMTAtaEdtX1R5NWZOUjFFUmgtaDU2dw?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPc2ZMRUR5SGxXOExveVpWbURvMjlSc3lCcmIyN3EydF9CSjRkTVpTR1N1YkowTTlJVnE1RnBTSk1DNzBVV0hjRkFGNE9KbGFHSTBaN1o2MmNDaDlZbk1HRDh6Ui15WngzWjloUmJ4U3BWcllmNF9GYWc2WXk5c0d1c293bXZkNWptcXl4eVFrY0NGU0k?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOS3R6ZFFtLVFoNFc1dldRRHZRa2F0RmdpSjF5OGJXVEFtUzcwczVESkZyb05PWVJ2Zkd4NEEzbXFHSGp0ckF6ZXdWNHBSN2JIV0I3c0tFUzRQdmxudDhGeGdibnNuVzVfV3Q1Ul9MNTRma0l5SVRqTENYLTJraGxGUnhwZkYwUGJib0U0bmhEYk5FYWNVSDgyRUViVHdXMnc?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPalJsX05vVFplVmlJN1BKUWFuZHExNWxCUDBJUWJfRTk5Y2s1bWJibk8yUHVfTlY2LU9mWEhsaE9zbFdXbEJqdXNud3g0dTJUaS1iVUNZUnFKUjdfOEVMRHVrVkp1bVlkVkh0UEtUbjBUQVliVlUwYkVqTmFmWm9kUTZfV1hWN0M0UWxDWXVnTWlCeHVhTG9WVjlkTFFsTDRIRGFDUE9PY0NIX0hCZjlR?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxQSjVabmw1RURDTERFdVV6NDljSThqVFJfWG51Qlk2dXN1MGRpY0YzazlLNGZ1dEl5eUs5REFUcXQ0Tk10dTBwWVdza1lDeFF5VWtHSjlFc2w5TEludmJKS0Zyb3lGdUFNME5KYVJFQjJZYmYxdUlHY2UtOEFBR21OLWo2ZnFZV2FvelpaWE5ldW5wbmhXR3NudThSbG5TNWhWSjg3XzhuMm9nUDk0aHdrLXhwQnpuSkJMOHVDckln?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxOZzQyVjFnQzVIZlJBNVl2V1RKTDMzWUNYWTY0X25SbmZzYW13RXhXVXNJaEVhZm5WRlRhalktX25jUEFUdFMtS0pEaTdrUkJZa0pXYnpmWV9nMUZENy04VWxlaklma0JZa1N2M21ER3huTThfa0JmVWFiSnBXYkV4R1pmSy1kaU0xVG9oMGJ0dnQzbm1MUUYtQmJmWTgzUVJTX25yS2hwTHdBMUFjcWZUUks5WTVWWkp3dko1YWdZaDNGajh0WjBUa2R2ZkRKZw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQVUhoMzlONGZNdFZLNUJFMkRrMU5wS1JDWkdvM3ZxU3VDSGFubll3NnRlRTFzc0F2aGtaWjlzSEcxOHAyOXlGV0QxbE43MElNYVY0WmJ2THUxSlRoYWlkUUxRelJ3OVA3S3c1M3dLWDNzNnVOaVRXdlBsMDQxdFVWMWppUnRSNFdIS2U0TVNGOWdYSGt2ZmdPVk9R?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQMk5SZjNON1Z0X0dORHRoNk5NRjZuZjRabmZXTE1tRTA5V0hiTGFRdEJLZUhDQ1VQUFRoTC1HTnc1OU5ZUGtWUTc4eENadTVRRTRsWlRmUWhRa1FXVk1UTm85b0x6NmdrTGZYRUl2TzhGc2lLcGpsRl84NFpiU09vbDl4UVl5cUdWZUo3cEdKN3FPdGc0?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNXzNrZkxRVlRMRDg4SUZYeVI4cDVqSTl3QkpXVkJ6MnlPVzBJZ3BoTWhYNGtKUTNVMGdaNUZTX3V6RGw3WVRpSEI0YTExbUZ1cmtva1hTM3FYamhTckJZb3dOaUdsSkZ6bkZaM1E2WERhMThUemEyLTZBYkNScTZiWTYyaTlVLUVLV1lNOUhrMFdVNVZSRkdvd0FzYlhHdXRw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNekRsZGVrS3pGUDBHdmNrOS1KREpLcUlEdmpDOElCcVk1RDB4WU5kdnM5ZTRLMzRsMU1MSm5tazAydTVPNWZ3aU0xa3F1RWV1M1VCYmpPeWEtSXpXTER5Smh4TGpGS3ZzSXhYU3FhMmgxUzVqazVLVlpKbmEyUE44ZmMzUUNHT3kxZHEwWUJJT1Y0Z3F6bW5vSmF5ajE4cTJBUXc?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPa05Cb1NpWEpwbmpNOVRNV3E4ZTZqNFFLTUhpNERwRWd5N2dlQkFIV05feGs0am5uSDFTWDAzNzRpRlYzdjVwdDdtaXQ5WGhyQTA1bURwT3AyMlpEV0F5LWY2MHpSUnM1SzZFaVN4bzdqdzRTYkY3bTh6M2FhWUk4TlVLUzQ5WVJuOGVtQVpCWUdDZw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
