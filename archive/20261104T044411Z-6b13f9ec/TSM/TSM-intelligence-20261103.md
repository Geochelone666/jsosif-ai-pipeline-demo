# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-11-03**
- Market data as_of: **2026-11-03**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-11-03**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-04T04:47:53.319580+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 21, 'rule': 3, 'ai': 11, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261103T051441Z-8b1c85d8/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 21 unique headlines; 9 named publishers; 4 exact duplicates; 21 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-10-28

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 404.8000 |
| Return 1D (%) | 1.5478 |
| Return 1W (%) | -7.3409 |
| Return 1M (%) | -14.3788 |
| Return YTD (%) | 34.2535 |
| Return 1Y (%) | 34.1876 |
| Annualized volatility (%) | 39.7575 |
| Beta vs SPY | 2.1887 |
| Max drawdown (%) | -21.5466 |
| Sharpe (rf=0) | 0.9409 |
| Downside deviation (rf=0, %) | 26.8084 |
| Sortino (rf=0) | 1.3953 |
| Historical VaR 95% (1D, %) | 4.2163 |
| Historical ES 95% (1D, %) | 5.2558 |
| Correlation vs SPY | 0.7046 |
| Tracking error vs SPY (%) | 32.0534 |
| P/E (trailing) | 25.83 |
| P/B | 77.25 |
| EV/EBITDA | 3.77 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 17.31 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 58.66 |
| Return on equity (%) | 41.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 434.0660 |
| Close vs MA50 (%) | -6.7423 |
| MA200 | 399.2727 |
| Close vs MA200 (%) | 1.3843 |
| RSI (14, Wilder) | 39.3177 |
| MACD (12,26) | -8.2108 |
| MACD signal (9) | -5.0350 |
| MACD histogram | -3.1758 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 274, 'SPY': 274}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 404.8000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.5478 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -7.3409 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -14.3788 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 34.2535 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 34.1876 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 39.7575 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.8084 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3953 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.2163 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.2558 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.7046 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.0534 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.1887 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -21.5466 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9409 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.3100 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 58.6550 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8550 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 25.8328 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 39.3177 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.1758 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -6.7423 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 1.3843 -> Slightly above the moving-average trend level.

## TAILWINDS

### Taiwan Semiconductor Manufacturing (NYSE:TSM) Shares Up 1.6% After Insider Buying Activity
- Summary: Taiwan Semiconductor Manufacturing (NYSE:TSM) Shares Up 1.6% After Insider Buying Activity
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxNcmNfZEczOGZfTTk4cFZQaGNEQTV4LVEtWXZ2R3ktcVk3ckRFNkNEVHE0MlVQcFc5QkNkelJQV2NvbjJTSGNUR3JINUUxOTdDNHdjN2F6b0NJVmhJa21UOUVJa0I0SmU0ZFpjWUkzbmN0WGIwNjd4NDg4WGVtM1ZwcHF2b1dCQU9mc2N3Ti1jb2lfSV9RNjQ4MmVqZTlZaTdFd3lycnNHNGVzUWthcEgzNl9qWjFsbGF6UUlxTjgxczZSX3E2TFRJNnJXdTg3bW5wNnJ6cEp6OFBKdzh4VG5B?oc=5>

### Why Did Taiwan Semiconductor Manufacturing (NYSE:TSM) Shares Drop?
- Summary: Explores reasons behind recent TSM share price decline, analyzing market factors and company performance.
- Date: 2026-11-01 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxNUWxQTWdUN0RiZ1RWclVYTGU4T2plYkhPRWFNb1N0aTZGOWF6eVpGSEQxUGVLZEVDNEt3MENjSzcxcGxyRWs3b0NWX1RQSHVIRlRla1RrcG9VTVBCVzdUVXA4ekxydklCMGVTbVNrODRQLWxDUmlwdXlEX2xIdFZSSjVqRm52aEN0d1MzcW9OdWx4TmY4aHNhWVJnRU1zdWVBdDJzUUpaOTZieDQ?oc=5>

### Here’s What a $10,000 Investment in TSMC Stock Will Be Worth by 2030
- Summary: Projected $10,000 TSMC investment could grow significantly by 2030, indicating strong long‑term potential.
- Date: 2026-10-30 | Impact: high | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxOU1hNeUxiYWNYT2JHOHRZVm9JOEx2RmtSU1I3SUV6emRrUmgzUmtvR2k0clBENDlDRTF6SEtIQTRGOVZ4Tm9wTVlDam01bklqRzljU1U0akEzNW5iOGY0cmZVU21QTWJkMlZvTVBHWVpVanhlTVFRQXAteGJ5SzlLcG9ublZqQkw1SlRVZ1BjUjkxWl92dXJvT3VaWWQ2R2lhU29BOVpBUGRXMnNzWGpsakRVRQ?oc=5>

### If the AI Bubble Scare Gets Worse, This Is the Chip Stock I'd Still Hold
- Summary: Despite AI bubble concerns, the author maintains confidence in TSM, highlighting resilience.
- Date: 2026-10-30 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNSU1IMGY2WElySS1YWHNuclN0enIybWVCekVJVU82Z2lIdUh5NjFHZXpmZDl6TEV4SFloN0hmUGw0enpNTi1ENE1LV0xMNXJIV1I1eVh3QUZ3eEM5eThjODFLdW9MX1V4b3Ytam80cVpMOExkN2hKYmpFdjZYY3R6MlJLTVJQSFJyVGxBU2tZQkpweEZqZEluag?oc=5>

### Taiwan Semiconductor Manufacturing Company Ltd. (TSM) is Attracting Investor Attention: Here is What You Should Know
- Summary: TSM is drawing investor focus, offering insights into its market position.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxPMlBUNlRGNktfa0JOdWxDeTFIZkdoMHhhaEkzSVRVek9acWpFNHpIYkN1dVBaVktiRXloUkcwVGtNSEdRT3AwdFdFMTJnTkNaLXFyT2p3LXF3WEVNaHo1cjdoaEszelBJbWJXbTR3NGIzTzhZSFFBUWN4SGo0aE9OcmFiWnM1R1ZsYzEtNFJFejVlMUlJR01QQU1TU0xwRE9GcklWakU1MUNWZXBBakpUTg?oc=5>

### TSMC Is Down 18%: The 2nm Ramp Should Change That (NYSE:TSM)
- Summary: TSMC’s 2nm ramp expected to lift stock after 18% decline.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQSm9ZUm5aN3VpLUFlOUd1eGRTVTJaMGdlVl9fNjgtRldkUDMxVUw5TFIzRlZuX3N4Zl9MTVBDYmNBQ3BUb1hmMVVLdThJTDVBQzF1ZzY5bGh1M2lqRkFRdnpRWEtRWDR1bF9iMGlJbm0td1BoNHVVT0M0MXhfaGpOZmNoVW04a0NVNWY0NnNKY1dQaFdLNXIwbmpKaGI?oc=5>

### Midterm Election Market Outlook Highlights Taiwan Semiconductor (TSM) as a Key Tech Stock
- Summary: Market outlook positions TSM as a key tech stock amid midterm elections.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxQalVrNW8tNlFyaHlJSnNmd1JlTHI2SlBRVmxyOE9SbGxqSUlhOW9kNEIwcFdnZDFqRzJkbzlGNWw0aUs3MGphWXI0U1p4a1hRTFJoYXpsaVdsd21lRDZRU0lHdzl3SDhGSno0cnRNNi00ZEZfNTNabU1mby00OTJsSzZKVGc0YmJiUXNZMGRkZ0VjRG1lNl9XcDBMLV9lTDZmYWVmRjNCd0ZMbDNIc2J6aVlFNXBhQ3NhS1dNT2ZpOWlOSVJG?oc=5>

### TSM Soars 33% in the Past Year: Is It a Solid Investment Proposition?
- Summary: TSM's stock rose 33% over the past year, prompting investment discussion.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxNTWNYM0lGbnVRSThTS0dRNUpraG1ha0l4dTFEbXlWZlI4Q25wbnY5Tjd5S3JJcUw3eWtrYU9BT2RZT3JxSHA5b3poZ2lPcGZPSkx6Mld5dWdLNDk2eVNZNlBxUkFwNzI5Vm9Vbkp3clhUbGdDM3p4SGRKVF9xOGl5Ml84Z1k4dTlmZVZxT0ZPMWQ5c0JDSTBGOFV1anRhWWtPUmx5czI0VldwM1lGVG1NcVhRQnhIdkNQVHZabGFn?oc=5>

### Insider Move: Lipen Yuan Invests $71K In Taiwan Semiconductor Stock
- Summary: Insider Lipen Yuan purchased $71K worth of TSM shares.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxOb1Y2N3BqdFN1YlRmbTc3S3BVTG5tSnA3NF96OTA3WVkyTnlJamE2Vnc5Sm1zNDdGWEM3ejlieFFocjlaZVZHYkJQZk1yYWRRYTNyRW5VQjh6dThZWkQxMG00WWhlbUVaVlpueXhEOFR6aF9QQUxONjE3OEE1T09LOUdDZjVEcE1QcGRhX1pvWGY1WmJYMmF6dTh5eXZ3elRGOHN6eEtVMU9VdVk?oc=5>

## HEADWINDS

### Taiwan Semiconductor Manufacturing Co Ltd (TSM) Stock Down 6.0% but Still Overvalued -- GF Score: 98/100
- Summary: Taiwan Semiconductor Manufacturing Co Ltd (TSM) Stock Down 6.0% but Still Overvalued -- GF Score: 98/100
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxNanJjTkhQMUhmbFpvaGxmRzhsWTdNVDl2T1R2Ml82b0o2NGV3MjRhTy1neFlDSjR5dUlxSlg0c3RWUkhSWEY5UDI3UmFFXzk0cFNHOVRoUXdUUkh1MWNfbEwzMFhVRmpKVHJSbElOMm5JODdVcHhTMDVncURVQnVBT0ZaVlIwemc1ZTZKVDllSGVha3otWjVELVdBbHhzYWt2dTlrbFNIcUVnT19nZHhzbkVucmhPRmhLWkRmdi1GOEZlMUpCWEVuaVo2ZjZWMXc?oc=5>

### 8 ETFs Cut Taiwan Semiconductor (TSM) Holdings on Thursday
- Summary: Eight ETFs reduced TSM holdings, signaling potential market caution.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOUkY5cnBtaDA0VDRiSWpibDAzVzktck92aXA0dkR4VENJal9URjhETVo4V05yLVExVGhpaU1JTnllNUxvcGxDdnVvUzFGQmZGQURpVWNhaU5jSGUwejhCY3FKVzFOekNyYnJBeWJwaWYxYkFseWJTV3BUaWoyLTYyVk15b29mdkRoQjdZTndkdWlfa2Q2bXpDdXZGa00?oc=5>

### TSMC: The Cracks Are Showing (NYSE:TSM)
- Summary: Report indicates operational or financial challenges for TSM, raising concerns.
- Date: 2026-10-29 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMid0FVX3lxTE5NM2ZPNW5mb2NfMHdER3RRX2QyeVkwSDl3anVfdVdWUTQ4UkxyRHBxeGJ0QkFRb0tybEpVNWNXRXZwR0gyWm5UNV9PQUIwOWV5M0xVc1lxZXdKeTV2eFVzTWc1MUF0cEdtYW1NRTMyamVWX0t6V0Y0?oc=5>

## CATALYSTS

### Taiwan Semiconductor Manufacturing (TSM) Stock Looks Fairly Valued on Cash Flow
- Summary: Taiwan Semiconductor Manufacturing (TSM) Stock Looks Fairly Valued on Cash Flow
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxOWUhsbVBmcl9hU1BjOF9qN2N6T3ZfaGN1WElGT2ZDZHZDa1lEcTNna0hWUXozQnNsLW5SWTlNQ05RVEc2cFJNNlJjdEoxVVlyZE5oYlpCQnBvOTgwRkY5ekh3X1V4T0JzYlVfR25HV2xLWGxNNGI5WHdNaF9CLTBXWTIwR1o0MmFCMGRXWmxSaWp1R3lyRy1wRFNGWVE3TXl6OGhFeGZJRGFjc0pGX0I1OHNrdkc4YUZGOFdnQzJzUUJyem9kVlREWHVVUFhiYldZcmY0UFF0UXpHM1lXR0dsWDZkQlJZMjdPTlRVZtIB8gFBVV95cUxPTGtJNWdzOXVHNlhuTDRUYjc2TVRQWGRYQ2xKb2FTX1RlWXlWd1djUnRQOE5tRkdBdU5yY1dJalcyckFQSWhhazE0SHZtNEl4UXFZelhjVUJyWkdsQzE3MFA3bEdJVlphVVp6YmxtbEFXaUt4RTVVU1RCSHhkY1VZTFdMbFRiMlVpdXV2RzV4blJCbm9PRENROFFSanBXMHZPcWlGMTJERTBBd1pDaHdJN0F4M3hJOWpQcmZzalhmUVhEUXZ0cHZxbktmaFZZSnRKeFBjUmVacEN6SGdvSUduUmYwLWpfa2habGp0VmZfbHJ2dw?oc=5>

### Beyond NVIDIA: Why TSMC Stock Looks Attractive After Q3 Earnings
- Summary: TSMC’s Q3 earnings boost investor interest, making the stock attractive.
- Date: 2026-10-28 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOTl9Qckw0VV9Ud2FBeDJiSnRJXzdhX2c0VGtNVklNTVZUNlZXaG14Q3VicGQ5SHhnUF9kYWRfZmNXNjJLUW9RMTdBb0d3VXlTejhyQVJsb3JLX3JjTTV0bkJlTnZ0bFEtSlZ6MkNoNDZVSHNwYktuWDF4YlBnNGlObk10WFY2enpwS0RRMk14aGFsTWVGZFdV?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **25.83** | **77.25** | **3.77** | **50.90** | **2,099,484,557,312.00 USD** | **34.19** |
| UMC | 15.47 | 2.83 | -0.26 | 25.60 | 41,127,821,312.00 USD | 112.86 |
| GFS | 32.74 | 1.99 | 11.57 | 5.80 | 23,907,684,352.00 USD | 20.75 |
| INTC | N/A | 2.80 | 17.49 | 20.90 | 321,823,244,288.00 USD | 53.29 |

Peers fetched as_of: 2026-11-03; TSM reuses existing data (market data as_of: 2026-11-03); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMi3wFBVV95cUxNcmNfZEczOGZfTTk4cFZQaGNEQTV4LVEtWXZ2R3ktcVk3ckRFNkNEVHE0MlVQcFc5QkNkelJQV2NvbjJTSGNUR3JINUUxOTdDNHdjN2F6b0NJVmhJa21UOUVJa0I0SmU0ZFpjWUkzbmN0WGIwNjd4NDg4WGVtM1ZwcHF2b1dCQU9mc2N3Ti1jb2lfSV9RNjQ4MmVqZTlZaTdFd3lycnNHNGVzUWthcEgzNl9qWjFsbGF6UUlxTjgxczZSX3E2TFRJNnJXdTg3bW5wNnJ6cEp6OFBKdzh4VG5B?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxNUWxQTWdUN0RiZ1RWclVYTGU4T2plYkhPRWFNb1N0aTZGOWF6eVpGSEQxUGVLZEVDNEt3MENjSzcxcGxyRWs3b0NWX1RQSHVIRlRla1RrcG9VTVBCVzdUVXA4ekxydklCMGVTbVNrODRQLWxDUmlwdXlEX2xIdFZSSjVqRm52aEN0d1MzcW9OdWx4TmY4aHNhWVJnRU1zdWVBdDJzUUpaOTZieDQ?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxOU1hNeUxiYWNYT2JHOHRZVm9JOEx2RmtSU1I3SUV6emRrUmgzUmtvR2k0clBENDlDRTF6SEtIQTRGOVZ4Tm9wTVlDam01bklqRzljU1U0akEzNW5iOGY0cmZVU21QTWJkMlZvTVBHWVpVanhlTVFRQXAteGJ5SzlLcG9ublZqQkw1SlRVZ1BjUjkxWl92dXJvT3VaWWQ2R2lhU29BOVpBUGRXMnNzWGpsakRVRQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNSU1IMGY2WElySS1YWHNuclN0enIybWVCekVJVU82Z2lIdUh5NjFHZXpmZDl6TEV4SFloN0hmUGw0enpNTi1ENE1LV0xMNXJIV1I1eVh3QUZ3eEM5eThjODFLdW9MX1V4b3Ytam80cVpMOExkN2hKYmpFdjZYY3R6MlJLTVJQSFJyVGxBU2tZQkpweEZqZEluag?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOR3B2ZXdPanBtR2ROMXhFa3RnWlp2Um9zcjVsYXpWbEtNSFB1ZnVyZkFZRDUwNTZvdGhodk1pVW5ZcWxjZGE3bUNCTzNQSEZNTTJwbjN1OVpoeVJWZVFUNDdycmFidHRjSVpTRWVMakpoSzhkX2RObDgwNXg5VUdLVDVNcEJFaHBPYlhmYmhXTm53aWpu?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxPMlBUNlRGNktfa0JOdWxDeTFIZkdoMHhhaEkzSVRVek9acWpFNHpIYkN1dVBaVktiRXloUkcwVGtNSEdRT3AwdFdFMTJnTkNaLXFyT2p3LXF3WEVNaHo1cjdoaEszelBJbWJXbTR3NGIzTzhZSFFBUWN4SGo0aE9OcmFiWnM1R1ZsYzEtNFJFejVlMUlJR01QQU1TU0xwRE9GcklWakU1MUNWZXBBakpUTg?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQSm9ZUm5aN3VpLUFlOUd1eGRTVTJaMGdlVl9fNjgtRldkUDMxVUw5TFIzRlZuX3N4Zl9MTVBDYmNBQ3BUb1hmMVVLdThJTDVBQzF1ZzY5bGh1M2lqRkFRdnpRWEtRWDR1bF9iMGlJbm0td1BoNHVVT0M0MXhfaGpOZmNoVW04a0NVNWY0NnNKY1dQaFdLNXIwbmpKaGI?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxQalVrNW8tNlFyaHlJSnNmd1JlTHI2SlBRVmxyOE9SbGxqSUlhOW9kNEIwcFdnZDFqRzJkbzlGNWw0aUs3MGphWXI0U1p4a1hRTFJoYXpsaVdsd21lRDZRU0lHdzl3SDhGSno0cnRNNi00ZEZfNTNabU1mby00OTJsSzZKVGc0YmJiUXNZMGRkZ0VjRG1lNl9XcDBMLV9lTDZmYWVmRjNCd0ZMbDNIc2J6aVlFNXBhQ3NhS1dNT2ZpOWlOSVJG?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxNTWNYM0lGbnVRSThTS0dRNUpraG1ha0l4dTFEbXlWZlI4Q25wbnY5Tjd5S3JJcUw3eWtrYU9BT2RZT3JxSHA5b3poZ2lPcGZPSkx6Mld5dWdLNDk2eVNZNlBxUkFwNzI5Vm9Vbkp3clhUbGdDM3p4SGRKVF9xOGl5Ml84Z1k4dTlmZVZxT0ZPMWQ5c0JDSTBGOFV1anRhWWtPUmx5czI0VldwM1lGVG1NcVhRQnhIdkNQVHZabGFn?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxOd3NvRTVTN09lTVZfb3JyMTZVby1zQzZPaGQxRU1Ueks4MUpaTXl5YnZtTGRtZGNMakRuUlFGOHk2YlEzXzdTbzNIeVJYb056NFhEMEZaNGZucXNHRmtBX0psVkMwXy04czNNNnpFNEZiWHVnTzJpSmh2U1JGcTNPb3NyekV5TWhEMjFhZlVxTURPdw?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxOb1Y2N3BqdFN1YlRmbTc3S3BVTG5tSnA3NF96OTA3WVkyTnlJamE2Vnc5Sm1zNDdGWEM3ejlieFFocjlaZVZHYkJQZk1yYWRRYTNyRW5VQjh6dThZWkQxMG00WWhlbUVaVlpueXhEOFR6aF9QQUxONjE3OEE1T09LOUdDZjVEcE1QcGRhX1pvWGY1WmJYMmF6dTh5eXZ3elRGOHN6eEtVMU9VdVk?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxNanJjTkhQMUhmbFpvaGxmRzhsWTdNVDl2T1R2Ml82b0o2NGV3MjRhTy1neFlDSjR5dUlxSlg0c3RWUkhSWEY5UDI3UmFFXzk0cFNHOVRoUXdUUkh1MWNfbEwzMFhVRmpKVHJSbElOMm5JODdVcHhTMDVncURVQnVBT0ZaVlIwemc1ZTZKVDllSGVha3otWjVELVdBbHhzYWt2dTlrbFNIcUVnT19nZHhzbkVucmhPRmhLWkRmdi1GOEZlMUpCWEVuaVo2ZjZWMXc?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOUkY5cnBtaDA0VDRiSWpibDAzVzktck92aXA0dkR4VENJal9URjhETVo4V05yLVExVGhpaU1JTnllNUxvcGxDdnVvUzFGQmZGQURpVWNhaU5jSGUwejhCY3FKVzFOekNyYnJBeWJwaWYxYkFseWJTV3BUaWoyLTYyVk15b29mdkRoQjdZTndkdWlfa2Q2bXpDdXZGa00?oc=5
- https://news.google.com/rss/articles/CBMid0FVX3lxTE5NM2ZPNW5mb2NfMHdER3RRX2QyeVkwSDl3anVfdVdWUTQ4UkxyRHBxeGJ0QkFRb0tybEpVNWNXRXZwR0gyWm5UNV9PQUIwOWV5M0xVc1lxZXdKeTV2eFVzTWc1MUF0cEdtYW1NRTMyamVWX0t6V0Y0?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxOWUhsbVBmcl9hU1BjOF9qN2N6T3ZfaGN1WElGT2ZDZHZDa1lEcTNna0hWUXozQnNsLW5SWTlNQ05RVEc2cFJNNlJjdEoxVVlyZE5oYlpCQnBvOTgwRkY5ekh3X1V4T0JzYlVfR25HV2xLWGxNNGI5WHdNaF9CLTBXWTIwR1o0MmFCMGRXWmxSaWp1R3lyRy1wRFNGWVE3TXl6OGhFeGZJRGFjc0pGX0I1OHNrdkc4YUZGOFdnQzJzUUJyem9kVlREWHVVUFhiYldZcmY0UFF0UXpHM1lXR0dsWDZkQlJZMjdPTlRVZtIB8gFBVV95cUxPTGtJNWdzOXVHNlhuTDRUYjc2TVRQWGRYQ2xKb2FTX1RlWXlWd1djUnRQOE5tRkdBdU5yY1dJalcyckFQSWhhazE0SHZtNEl4UXFZelhjVUJyWkdsQzE3MFA3bEdJVlphVVp6YmxtbEFXaUt4RTVVU1RCSHhkY1VZTFdMbFRiMlVpdXV2RzV4blJCbm9PRENROFFSanBXMHZPcWlGMTJERTBBd1pDaHdJN0F4M3hJOWpQcmZzalhmUVhEUXZ0cHZxbktmaFZZSnRKeFBjUmVacEN6SGdvSUduUmYwLWpfa2habGp0VmZfbHJ2dw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOTl9Qckw0VV9Ud2FBeDJiSnRJXzdhX2c0VGtNVklNTVZUNlZXaG14Q3VicGQ5SHhnUF9kYWRfZmNXNjJLUW9RMTdBb0d3VXlTejhyQVJsb3JLX3JjTTV0bkJlTnZ0bFEtSlZ6MkNoNDZVSHNwYktuWDF4YlBnNGlObk10WFY2enpwS0RRMk14aGFsTWVGZFdV?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
