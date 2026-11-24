# DIS Intelligence Report

- ticker: **DIS**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/DIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/DIS/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:33:50.723447+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 2, 'ai': 12, 'unknown': 0, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261123T053847Z-45053549/DIS** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 13 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 32.0%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 120.2700 |
| Return 1D (%) | 1.9410 |
| Return 1W (%) | 1.3227 |
| Return 1M (%) | 6.8877 |
| Return YTD (%) | 6.5233 |
| Return 1Y (%) | 17.0038 |
| Annualized volatility (%) | 26.4886 |
| Beta vs SPY | 0.5389 |
| Max drawdown (%) | -20.2451 |
| Sharpe (rf=0) | 0.8160 |
| Downside deviation (rf=0, %) | 17.5460 |
| Sortino (rf=0) | 1.2318 |
| Historical VaR 95% (1D, %) | 2.3432 |
| Historical ES 95% (1D, %) | 3.3566 |
| Correlation vs SPY | 0.3046 |
| Tracking error vs SPY (%) | 26.1575 |
| P/E (trailing) | 21.36 |
| P/B | 1.87 |
| EV/EBITDA | 11.25 |
| Revenue growth (%) | 15.50 |
| Forward P/E (estimate) | 14.05 |
| Gross margin (%) | 38.02 |
| Operating margin (%) | 16.57 |
| Return on equity (%) | 9.13 |
| Free cash flow yield (%) | 3.63 |
| MA50 | 110.8202 |
| Close vs MA50 (%) | 8.5271 |
| MA200 | 103.7514 |
| Close vs MA200 (%) | 15.9213 |
| RSI (14, Wilder) | 60.7547 |
| MACD (12,26) | 2.6488 |
| MACD signal (9) | 2.7343 |
| MACD histogram | -0.0855 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'DIS': 288, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 120.2700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.9410 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.3227 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 6.8877 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 6.5233 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 17.0038 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 26.4886 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 17.5460 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.2318 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.3432 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.3566 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3046 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.1575 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5389 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.2451 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8160 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 14.0474 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 38.0230 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.5650 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.1270 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.6273 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.3623 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 60.7547 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0855 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 8.5271 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 15.9213 -> Clearly above the moving-average trend level.

## TAILWINDS

### Walt Disney (DIS) Beats Q4 Earnings and Revenue Estimates
- Summary: Walt Disney (DIS) Beats Q4 Earnings and Revenue Estimates
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQZ2hDaXFGQUsyQkpHOUJ3UWRLRXNxWWdSdmljN0pFOEZxNFZpNzNjSW94bjRwSmFMOHRJSUdqR3RodDBodl9tUFo0Wl9RVVhrVGsyVTdkbHV5alZfeERRdjhRTHhCVkxrbXVWOUFweGpCbGFMeTNNWGtsUDhIeEN1eG14bkF0ME5yTXo2SmtxdWRzNVU?oc=5>

### Why Walt Disney (DIS) Stock Is Up Today
- Summary: Positive market sentiment drives Disney stock upward today.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxQNGlYTnBaUjFDcDFSa0VZUjBjYnJoTFNKUWViNEFOb0ZHSzdaS2Q1dXlFd19jTkVPZTZDQWJUcHBneHBDT1R6MXpSTU12MFVINWNyamN6Z0l1WlNLdXUtdjFQTlNiYVBHSXVQSWpJMl9ueUloY01XdkMtT0VzX241Y1lhb01seFpQ?oc=5>

### How Record Earnings Will Impact Disney Stock Investors
- Summary: Record earnings boost Disney stock investors.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPeTJaTWxRYWlkUHpsRmlxeFg3QTQyVFZ2VVVCX3NiOVZOYWR5VVM1NkNFSmFIQ1VXeWVUM3R1dkx5dk02ZTFKQ2hPV29NWGNOQXJmdmVuZmstUmt3LUtEWkhZTS1nV0ZXaXc5MTBCLWVYdzdjVDJzZk5sMGljelBxQjhxblp3NUo1SmxZUFNnMGpvTGF3eE85RzMwQzJlbkxKby0wekNTZDdwUnd2S3EyUjBWbnNFMjBNNEHSAb8BQVVfeXFMUHYyTFo4ekswb2NNOEc0VWowbXhDaTN0d1JQMmJtMlhQZWhKdnFVbzdQcy1aTnZmYWZXZXF1MzFkV1cxLVhrUlMtc3lINjNPOHlwUy1vZFh2amNjS3dIRlFuelpGeWJMOU5VU0ZsN0FMSXUtTUZPSEQxOW5ZaU1OMS03N2FzYmdyN0IzRGs3cWsweEs5WDZWT3k0M1RoSHU5ZVJicG9FeVJrOFo0cDAweTZpd296TVlfMkttVmpqUnM?oc=5>

### Disney Stock Hits New Highs After Strong Q4 Earnings: Time to Buy DIS?
- Summary: Strong Q4 earnings push Disney stock to new highs, signaling robust performance.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNMy1vczBlNUd2RGtCVlBzVl9qYUs4Ty1ubk1WTFVVRjBHUFRfTDJKZU9LWVdVS3BPU3phTEV6cVhKTlpJQWtPdE9mV180VXRiSlRhVEd4YlUtVURScF9sOFFmSllsaTlBTGQ0aG0yNHY3c1lFb2tqVkxEQ1M3c2pmZGdxWUtPZ3RwcEd4UzhValc2ODlYZUNJbHd1MA?oc=5>

## HEADWINDS

### What Could Derail Disney Stock?
- Summary: Potential risks that could negatively impact Disney stock.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOMFZaMHd3UjJfY3VxSTR5YWJxc1h3bzJJRENFbTdRUkluM1pTeEVxSTAtTVNSUmNQZ04zZzRITHo5N0JucmpzTDM1UEVEbFdaU1pwSGd0TDdCd05LQlFtNVI3Y0pQSnhCMC1LMXVSajc3NWtxYVZxdm1pRExtem44OXJ2NU1IcHNYWXUtTURvdVZaLVo5?oc=5>

### Walt Disney director Robert Iger sells $39.5 million of DIS stock
- Summary: Insider sells $39.5M DIS shares.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxQMXV6UEJxV0FqM0N1VUY1eDhsZGtNc3dBVjFfNk5DS2hkc1I2UjAxQkxrbHg2NGRSMW9FVlpOS0VqZWo5N1pvanBfTzZKeFdzMjl5MlN1bFdqeS1SQXZUSmJmR05zWFprRkR3ZnlWcWc4SzZJamUtN0U3WW1EdUozdWNyQjU0c011bk42THJEQWdYazExazdmclFsREN6QUI2VXllbXRsYnVnTjhiVzlWbUNkY1h0OXVtYVQ2eTRZUE1WU2gzU2x3?oc=5>

### Disney: Economic Outlook Clashes With Disney Goals (NYSE:DIS)
- Summary: Economic outlook conflicts with Disney goals.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxPZ045aXBtZG91UTRuUmQ2N0J6bHVOUlppVHBZTkhyRmVNa2FKS3oyTzByRWJUekRLdEJUeTVXdnphVTBOSnBZMENPWDVUSDhGeUN4eWlmQWc2YTA5NGl6NkVSVWJnblBkWVgyZjMzYzZpcFN2NlpIWWk3TmFEUVZiNUtwMHRfRzFHZ0ZZb1FXUzZFV3RFUWlHWE5EWng4Zmgtc3pGcThjQXlkSTJ2bmc?oc=5>

### Disney Stops Reporting Streaming Profit. Should You Worry?
- Summary: Disney ceases streaming profit reporting.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNTy1FUDdSVTVGYWN4OHZXTkxUT3NIRm41b2F1LWVIUHNwNFBVd1hJTlpmQUpodjB2ckFPVU5vY196UzJzNHQ5M3VMWWRlLXI5d2F2X2V6YnYzSlBwSS02ejhEd0hDNk1MZ3RWNXg5ajcwTnduNFd6cVpGV3VURVJleUlFdERVZzY5aXNKVnBiYkpfNy1NVE43VXA4RENVUG1mQjIzeC1DN09CeHJ4M1lqSFJsZ096ODg?oc=5>

## CATALYSTS

### Walt Disney (DIS) Q4 2026 Earnings Call Transcript
- Summary: Walt Disney (DIS) Q4 2026 Earnings Call Transcript
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPXzRybUMyclhWdjBFcjV2NnNzaE9mbVVMQTR2YTFuTHJOdXU4Ukc2TG1NY1pCSnNrbVN2X29HSUxKd3NITFIzZFIzQ2h0YjZpcHh3cGh1RElzT0o1VXJuM2dkNjBiSEhpb0hYV1VIVkY5cDRQVXpVbzdBak9jbGZRbGZPTlhNd1ZudWY5UWpsUTNFZkRyWGdiRUptLWRUMTNaeDliYTZuRy0wZmc?oc=5>

### Disney Just Boosted Its Dividend by 33%. That Gives DIS Stock Investors a Real Reason to Stick Around.
- Summary: Disney increased dividend by 33%.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxPSlowejN5VDB0OWxkUnJIMmhHclNmWWNaM3M5SE9FTFJHb09JYnRiQjNZSWxha3JrUUw4SFQ3UXhJQkhBbDJMYkg1dEw2Ym1IdG1tZDIwTWZicVhfLW0zQlVzanVGaUppNm54SlphanNyZ3ZEanhPQ0hhc2Y2Q0lQWGFlUVgtZEhPOXB5ODQ4ejI2QlV3TktSZFZZdVFGV1ZnaURiSU1HdklOc0tpYjBVb1Y0aUV2cjhOeE9SU0R2Zi13czNYemVkSFI3RW0zWnliYUR3MjFJYmp5QUk?oc=5>

### Disney (DIS) Stock Slips As Q4 Earnings Contrast Margin Compression
- Summary: Margin compression in Q4 earnings leads to a stock decline.
- Date: 2026-11-18 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOZ2VGTzJFbDNmLV9HcDNCekJ4ODh6Q0ZVaXZENUNtR2o5Sm5BamdyQnhJZlpfWG9HeWxCMmp3TlFmQnI4TkZCS0pXVDJqdGlXN2cxSnNidnI4aklkYUo0XzB1MjhhX1M1YmhBYlQ1ckhCd1BmaDIwc3RJYlhuWmZNd3BseV9QYWN3dS1nMURMS0tyRGFo?oc=5>

### The Walt Disney Company Q4 2026 Earnings Call Summary
- Summary: Summarizes Disney’s Q4 2026 earnings call, highlighting key financial metrics and management commentary.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQQWRXWEl0Nk5obGhZeU1nTkNmaXR0aTFsMk9LN29ZMHg1ajRxNmZpTUFUM1paemxlY3o5c3dmSF9KNXlZTVZ4YUo5ZHdXbktyVzZsX0hPdk52cXVZWUI3ejBKa3FiN0FSSnB1OXhQTkxPb3JtcVhWNnB5RlY1LWVrOWxURWZsc0Eyai1Seks1Ykt4cXIwQ0xz?oc=5>

### DIS: Walt Disney Company filed SEC Form 8-K: Leadership Update, Financial Statements and Exhibits
- Summary: Leadership update and financial statements filed in SEC 8-K.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxORll2WnljNW55VXE0NkNxU2VJMERnWDhYaVdQdDZ2T2lxUFpsRDBxOUVNYTlxLWZPQUtPSk1HSW52UFFaS05uZ21QWmxXeEJwVTBiUkxKdkJkUUpoZU5IR1o0NkhfcHNkYV9lYUd5Q25pWWxERk9PeUF1Ylc1MXhjUHR1OEtuOWl4NG00eTdVRjVLc2JyejRzRVVOa0lGVDhPTmpnVlNTanlITm13NkE?oc=5>

### The Walt Disney Company Declares Cash Dividend of $2.00 Per Share
- Summary: Disney declares a $2.00 per share cash dividend, rewarding shareholders.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQdVNHZ3J6UWw3bUlLcDRHQkpWTFJMaXVsTUp1bWxoMGN1Q0NLTUlVbThUMXdmd0NfNkdPZHJtTnR4Z0NSQ0R5OE5BLWVRSUw0RHpuOFYtQmtHTkRjRTMwa1laeGc2d3paUzlKUzRQU2dNYmM1MGpsQm4wUVBUZlJQenJwWTdEb0QyaTBBandMeVJqM3h4RFh2Q25MbHBfanlVUnc?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **DIS** | **21.36** | **1.87** | **11.25** | **15.50** | **205,424,721,920.00 USD** | **17.00** |
| NFLX | 16.79 | 8.15 | 15.53 | 11.80 | 238,577,532,928.00 USD | -44.30 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| PSKY | N/A | 0.93 | 7.95 | 0.90 | 10,992,190,464.00 USD | N/A |

Peers fetched as_of: 2026-11-23; DIS reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-17
- Next expected earnings: 2027-02-01 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-23

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-11-17
- Revenue (latest available single quarter): 25,248,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 2,638,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1744489/000174448926000066/dis-20261003.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMikwFBVV95cUxQZ2hDaXFGQUsyQkpHOUJ3UWRLRXNxWWdSdmljN0pFOEZxNFZpNzNjSW94bjRwSmFMOHRJSUdqR3RodDBodl9tUFo0Wl9RVVhrVGsyVTdkbHV5alZfeERRdjhRTHhCVkxrbXVWOUFweGpCbGFMeTNNWGtsUDhIeEN1eG14bkF0ME5yTXo2SmtxdWRzNVU?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxQNGlYTnBaUjFDcDFSa0VZUjBjYnJoTFNKUWViNEFOb0ZHSzdaS2Q1dXlFd19jTkVPZTZDQWJUcHBneHBDT1R6MXpSTU12MFVINWNyamN6Z0l1WlNLdXUtdjFQTlNiYVBHSXVQSWpJMl9ueUloY01XdkMtT0VzX241Y1lhb01seFpQ?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPeTJaTWxRYWlkUHpsRmlxeFg3QTQyVFZ2VVVCX3NiOVZOYWR5VVM1NkNFSmFIQ1VXeWVUM3R1dkx5dk02ZTFKQ2hPV29NWGNOQXJmdmVuZmstUmt3LUtEWkhZTS1nV0ZXaXc5MTBCLWVYdzdjVDJzZk5sMGljelBxQjhxblp3NUo1SmxZUFNnMGpvTGF3eE85RzMwQzJlbkxKby0wekNTZDdwUnd2S3EyUjBWbnNFMjBNNEHSAb8BQVVfeXFMUHYyTFo4ekswb2NNOEc0VWowbXhDaTN0d1JQMmJtMlhQZWhKdnFVbzdQcy1aTnZmYWZXZXF1MzFkV1cxLVhrUlMtc3lINjNPOHlwUy1vZFh2amNjS3dIRlFuelpGeWJMOU5VU0ZsN0FMSXUtTUZPSEQxOW5ZaU1OMS03N2FzYmdyN0IzRGs3cWsweEs5WDZWT3k0M1RoSHU5ZVJicG9FeVJrOFo0cDAweTZpd296TVlfMkttVmpqUnM?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNMy1vczBlNUd2RGtCVlBzVl9qYUs4Ty1ubk1WTFVVRjBHUFRfTDJKZU9LWVdVS3BPU3phTEV6cVhKTlpJQWtPdE9mV180VXRiSlRhVEd4YlUtVURScF9sOFFmSllsaTlBTGQ0aG0yNHY3c1lFb2tqVkxEQ1M3c2pmZGdxWUtPZ3RwcEd4UzhValc2ODlYZUNJbHd1MA?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOMFZaMHd3UjJfY3VxSTR5YWJxc1h3bzJJRENFbTdRUkluM1pTeEVxSTAtTVNSUmNQZ04zZzRITHo5N0JucmpzTDM1UEVEbFdaU1pwSGd0TDdCd05LQlFtNVI3Y0pQSnhCMC1LMXVSajc3NWtxYVZxdm1pRExtem44OXJ2NU1IcHNYWXUtTURvdVZaLVo5?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxQMXV6UEJxV0FqM0N1VUY1eDhsZGtNc3dBVjFfNk5DS2hkc1I2UjAxQkxrbHg2NGRSMW9FVlpOS0VqZWo5N1pvanBfTzZKeFdzMjl5MlN1bFdqeS1SQXZUSmJmR05zWFprRkR3ZnlWcWc4SzZJamUtN0U3WW1EdUozdWNyQjU0c011bk42THJEQWdYazExazdmclFsREN6QUI2VXllbXRsYnVnTjhiVzlWbUNkY1h0OXVtYVQ2eTRZUE1WU2gzU2x3?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPZ045aXBtZG91UTRuUmQ2N0J6bHVOUlppVHBZTkhyRmVNa2FKS3oyTzByRWJUekRLdEJUeTVXdnphVTBOSnBZMENPWDVUSDhGeUN4eWlmQWc2YTA5NGl6NkVSVWJnblBkWVgyZjMzYzZpcFN2NlpIWWk3TmFEUVZiNUtwMHRfRzFHZ0ZZb1FXUzZFV3RFUWlHWE5EWng4Zmgtc3pGcThjQXlkSTJ2bmc?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNTy1FUDdSVTVGYWN4OHZXTkxUT3NIRm41b2F1LWVIUHNwNFBVd1hJTlpmQUpodjB2ckFPVU5vY196UzJzNHQ5M3VMWWRlLXI5d2F2X2V6YnYzSlBwSS02ejhEd0hDNk1MZ3RWNXg5ajcwTnduNFd6cVpGV3VURVJleUlFdERVZzY5aXNKVnBiYkpfNy1NVE43VXA4RENVUG1mQjIzeC1DN09CeHJ4M1lqSFJsZ096ODg?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPXzRybUMyclhWdjBFcjV2NnNzaE9mbVVMQTR2YTFuTHJOdXU4Ukc2TG1NY1pCSnNrbVN2X29HSUxKd3NITFIzZFIzQ2h0YjZpcHh3cGh1RElzT0o1VXJuM2dkNjBiSEhpb0hYV1VIVkY5cDRQVXpVbzdBak9jbGZRbGZPTlhNd1ZudWY5UWpsUTNFZkRyWGdiRUptLWRUMTNaeDliYTZuRy0wZmc?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxPSlowejN5VDB0OWxkUnJIMmhHclNmWWNaM3M5SE9FTFJHb09JYnRiQjNZSWxha3JrUUw4SFQ3UXhJQkhBbDJMYkg1dEw2Ym1IdG1tZDIwTWZicVhfLW0zQlVzanVGaUppNm54SlphanNyZ3ZEanhPQ0hhc2Y2Q0lQWGFlUVgtZEhPOXB5ODQ4ejI2QlV3TktSZFZZdVFGV1ZnaURiSU1HdklOc0tpYjBVb1Y0aUV2cjhOeE9SU0R2Zi13czNYemVkSFI3RW0zWnliYUR3MjFJYmp5QUk?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOZ2VGTzJFbDNmLV9HcDNCekJ4ODh6Q0ZVaXZENUNtR2o5Sm5BamdyQnhJZlpfWG9HeWxCMmp3TlFmQnI4TkZCS0pXVDJqdGlXN2cxSnNidnI4aklkYUo0XzB1MjhhX1M1YmhBYlQ1ckhCd1BmaDIwc3RJYlhuWmZNd3BseV9QYWN3dS1nMURMS0tyRGFo?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQQWRXWEl0Nk5obGhZeU1nTkNmaXR0aTFsMk9LN29ZMHg1ajRxNmZpTUFUM1paemxlY3o5c3dmSF9KNXlZTVZ4YUo5ZHdXbktyVzZsX0hPdk52cXVZWUI3ejBKa3FiN0FSSnB1OXhQTkxPb3JtcVhWNnB5RlY1LWVrOWxURWZsc0Eyai1Seks1Ykt4cXIwQ0xz?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxORll2WnljNW55VXE0NkNxU2VJMERnWDhYaVdQdDZ2T2lxUFpsRDBxOUVNYTlxLWZPQUtPSk1HSW52UFFaS05uZ21QWmxXeEJwVTBiUkxKdkJkUUpoZU5IR1o0NkhfcHNkYV9lYUd5Q25pWWxERk9PeUF1Ylc1MXhjUHR1OEtuOWl4NG00eTdVRjVLc2JyejRzRVVOa0lGVDhPTmpnVlNTanlITm13NkE?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQdVNHZ3J6UWw3bUlLcDRHQkpWTFJMaXVsTUp1bWxoMGN1Q0NLTUlVbThUMXdmd0NfNkdPZHJtTnR4Z0NSQ0R5OE5BLWVRSUw0RHpuOFYtQmtHTkRjRTMwa1laeGc2d3paUzlKUzRQU2dNYmM1MGpsQm4wUVBUZlJQenJwWTdEb0QyaTBBandMeVJqM3h4RFh2Q25MbHBfanlVUnc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
