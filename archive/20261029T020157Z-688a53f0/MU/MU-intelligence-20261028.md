# MU Intelligence Report

- ticker: **MU**
- Report as_of: **2026-10-28**
- Market data as_of: **2026-10-28**
- Quant sources: https://finance.yahoo.com/quote/MU/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MU/key-statistics/
- AI analysis snapshot as_of: **2026-10-28**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-29T02:22:24.623872+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 2, 'ai': 16, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261028T015717Z-533e470c/MU** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 10 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 36.36%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 983.2300 |
| Return 1D (%) | 5.8648 |
| Return 1W (%) | 7.6133 |
| Return 1M (%) | -6.6980 |
| Return YTD (%) | 244.7494 |
| Return 1Y (%) | 343.5792 |
| Annualized volatility (%) | 81.4650 |
| Beta vs SPY | 3.3909 |
| Max drawdown (%) | -39.0954 |
| Sharpe (rf=0) | 2.2412 |
| Downside deviation (rf=0, %) | 48.9009 |
| Sortino (rf=0) | 3.7336 |
| Historical VaR 95% (1D, %) | 7.0055 |
| Historical ES 95% (1D, %) | 9.5345 |
| Correlation vs SPY | 0.5287 |
| Tracking error vs SPY (%) | 75.5225 |
| P/E (trailing) | 12.49 |
| P/B | 8.04 |
| EV/EBITDA | 9.87 |
| Revenue growth (%) | 379.30 |
| Forward P/E (estimate) | 4.75 |
| Gross margin (%) | 80.72 |
| Operating margin (%) | 80.68 |
| Return on equity (%) | 88.26 |
| Free cash flow yield (%) | 2.62 |
| MA50 | 980.4347 |
| Close vs MA50 (%) | 0.2851 |
| MA200 | 740.8848 |
| Close vs MA200 (%) | 32.7102 |
| RSI (14, Wilder) | 53.1623 |
| MACD (12,26) | -24.5974 |
| MACD signal (9) | -23.7929 |
| MACD histogram | -0.8045 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MU': 270, 'SPY': 270}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 983.2300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 5.8648 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 7.6133 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -6.6980 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 244.7494 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 343.5792 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 81.4650 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 48.9009 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 3.7336 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.0055 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 9.5345 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5287 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 75.5225 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.3909 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -39.0954 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 2.2412 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 4.7523 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 80.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 80.6780 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 88.2600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.6195 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 12.4950 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 53.1623 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.8045 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.2851 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 32.7102 -> Clearly above the moving-average trend level.

## TAILWINDS

### Micron Technology Shares Rise 1.37% After Hours - Tesla (NASDAQ:TSLA), Micron Technology (NASDAQ:MU)
- Summary: Micron Technology Shares Rise 1.37% After Hours - Tesla (NASDAQ:TSLA), Micron Technology (NASDAQ:MU)
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOQXM1N1o1ME1jS09hZ0xQRzVqZlRiMHlfd3lra25nTEhuVVJndnNzdFJpQ01SQUZHUnJqQ3FmS0tvcWdpbmtxaDN1ZXZLbGNRajBmMm9pbF82ZUtwNms3R0JwbXo3Uzc1bmlvQ3VZTEtOVElJVHlGZUFLRWlVSU55MHpGQlNlWXBncUpRaG5waV8yTmxYazBFY1VDendfWk94Tm4yMm5iVHFiZWJaRlpfaC1CSDNqYXJiVUE?oc=5>

### Micron Just Unveiled a New Bonus Plan. What That Means for MU Stock.
- Summary: Micron introduces a new bonus plan, potentially boosting shareholder value.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPSVp0SEVqV2ZKY1BKYXJGZXhZcGZNVzZwdnBrV0NhWGtTaTEwMVNBb0hjZEx4b1VYR1B6UzdJNzdXaE5OZFhSZzhZQlhhWmNSelFxYXRCaG8tTEVHRU9DZE5TcmZDaXdHRzdBTjhlbDhqNGM2d1lQbnZpbVdlb1ExSTlXaDB3UzhXd081UzU1Wkp0OE9YT1pOWFFUZjR3V252TkxBTHI1T3J5aEdzdDcw?oc=5>

### Micron, Musk, and Memory. A Big Prediction Is Lifting the Stock.
- Summary: A prediction involving Micron and Musk is positively influencing the stock.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTE1NSnA4QTg5U0hoaGRRRFdFZC1wS2REemx2em5RTHl0Q3R6YVFQSW1QVmFaTTBGM3F0N0RWT2ZWTm5WeDVIODVqUHN5S3hBeExPRXVJZ08wQ2JBejJtVHRBYVRnRnpPbFNOcldMcVV1ZEhiZDdIQUJDY2JJVWI?oc=5>

### Why Micron Stock Is Up Today
- Summary: Micron shares rise, indicating positive market sentiment and potential short-term upside.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQYTJMOG1zSzlhSmpGWWI2MEp6Z3N5REo2Z1lUbzBjNkN6YzBVOEI3VlNBTkNUODJQaVRnU3Zfb2RvRTROMWQzemhaVXZmX2piQ3NBTGxSNDFfaEt6RmJiNWQxSFpvTkQzQmJQWW1uY0VlbFhZSGFTRTNVdklodWFIb01mazJPTUlmeVg3Sk15aXc?oc=5>

### Micron Technology And 2 High Growth Stocks To Watch
- Summary: Analyst highlights Micron as a high-growth candidate, suggesting bullish outlook.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQbzV4YU5OcU1iY09HVlFneGh3SWE5S1VLQ0xWdE9OZDFYcmpMX2tuUGdKckhlTEs0dTFCbE5OY1EwRjhNdV80VTU2bnJRSmpGQ2M5al9CcXBvMEhaTk1lLWhRM0pxcWtEX1dZQXZ0b1pNRXp5V25zT09UYUFkMThZbV9ZbS1lR1R5N2NpSE41ZjhmbWFiYWRzZTVMcm8?oc=5>

### Jim Cramer Says Micron Shouldn't Follow 'Whatever' SK Hynix Does As MU Shares Jump After Hours: 'I'm Hoping The Linkage Ends One Day'
- Summary: Cramer praises Micron’s independent strategy amid after-hours rally, boosting investor confidence.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQTUNoNzFRRHJBOHBKS1NiMnQyX1d4dEtIN29zaV9OeFp1bUtHNXZ5NC1WUnFGdWVyc3l3bl8wQ0FTbG5Hb0dmQnBqcU16bENvYTVLbERjbkY5VVo0dHk5WWZYS0J0bF9IVERYZGt1T2J5T3pneEdwUFpDNjFuQmFWTzhxSFhqQjg1NE5CN1BoSGIybkdUUENhb3R5d1E?oc=5>

## HEADWINDS

### SA analyst upgrades/downgrades: GOOG, MSFT, NBIS, MU
- Summary: Analyst changes for MU could impact market perception.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxPMDhIM08yQmdNbkJDS2lzak9KeTdRMkpndnZjNmNvZE9EaE1sNGNoaDhqTGNWT21VVVhLRTZfbGxkdmQ3Y05RMW83Ml80YXVqYmtXR2VXTkZsWXg5eVB0a2QtLUFERTNoVUtwc1BJTjBNT2p1Y1JJbFlKdzRSVWt4MWFYS1ZOYW1WRUprQ2h3?oc=5>

### ETFs Are Net Sellers of Micron Technology (MU) on Oct. 26
- Summary: Net ETF selling indicates potential downside pressure on Micron shares.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQQnBiNHhYVEFQWUxqR2ZpYUlHTXUzbHI5ekRwMGhRbmRtRno1UmdicEhNcVlYQ0U4Q29CcU9Xak1lcW9JVDZnbWJmdVZLdk5KbEh4allmemNMVWY5bXNGVkhqdHQ3Uy1NV1llVDJXMDVXbzFsWE5ibHB0emxBYi11c2pwUDBHNzd3Vy12enNJdm1NRC1tTC1CeDRtNUczbzdl?oc=5>

## CATALYSTS

### Micron Technology Stock: Is Now the Time for Investors to Take Profits or Buy More?
- Summary: Micron Technology Stock: Is Now the Time for Investors to Take Profits or Buy More?
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPNDVmcHh4WlRMQVZydHJ2QnRCM0E3NF9aTGd1OTRVM016LWxQU2JSLUQ0Q3NKbHVaSmRfZXVYOEhac1hkSGJHSG43elF6SEtOXy1PYW5sWk9VbUV1MWNkVU1SZ3RlM25VbUFiVUxNM0tFdTh3NEtZUnExaUd5REJEQUdyVXZEMVhNcEdiMlp5OERHUnFRVGpxYXBDYVN3NjJtcG91WUxfOVZzQnpaMzQyb1JBRTRIQ2VtUFlWYkNuSnBmdw?oc=5>

### Micron Just Delivered a Monster Quarter, but the Stock Is Plummeting. The Reason Is Obvious.
- Summary: Strong earnings reported, yet stock price fell sharply.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOaG8tM2JnYmdKRVRUTjhrVVpYT3l0a2J6VDNhYkJlTjVHNzdhYzNQVmlPNDdPd2paOWZ2LUxDVzN0MGNBbFdoQmZkaGZsM3pBQ0Rwbm8xRC04SFBtQ0NEM09ueFdsTDRycHp0NnloNGNGZWZNTnd3S0VJeS05dmwzcU02RV9iRjlLWGNlTmE5R0tybUNOU21NNFFoQUNMb3FFLXloUA?oc=5>

### Why Micron Technology Stock Rallied Today
- Summary: Micron shares surged due to positive market sentiment and strong demand expectations.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQU0NKUDZrYmo5dEcyMllySC1BZFRZTUxPZFp5TzJmOGl5ZTdIaEpXcWJVSWtlNDhuWGFSclN6ZkJ3d29CLUluMWtUcGowaXBadVVBY0tqVS1mUkstcHFsLXI1RWp0RmpOdm5OZzJLSktYZ0tmZ0gwRG1XMFN5ZFdtaGNnenc4TVBsczR3d25fVlFrd3dMdGJjVXlMVFlUV2JqdkE?oc=5>

### What Could Robot Memory Demand Mean For Micron Technology (MU) Stock?
- Summary: Increased robot memory demand could boost Micron’s revenue prospects.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNR0xMVWVZZjAtdzlUbkdZdlAwSGpTM1dpd2VibzlxR0xoeVpjVlZuWVBXSFQ5dGhKRHV5TnlYLXdqdXBNZWp4VmJ3a0tBMnhRazF0WkU1Q1ZYeElwU0JFVE5zWVF6d0Z3eEJDQUwzOEczNEhDUmlCT2dxSkE3UEE1NHUyTHhoSDVlM3JmZUMzM2Fsc2g1TlZEMjVn?oc=5>

### MU Stock Quote Price and Forecast
- Summary: Current price and analyst forecasts indicate bullish outlook for Micron.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiTkFVX3lxTE12OGhUSWtGTk9iWTJqbXhwZ2hpa25tNUxnRWlMam1RYkNBckpUdlVCMXgzY2ZDbG1HUkdxeFlUMWRkZ3ljR2xXUkdJb285UQ?oc=5>

### AI Spending Is Nearing $1 Trillion Annually. These 2 Stocks Are Most at Risk If It Slows.
- Summary: Micron may be exposed to AI spending slowdown, potentially impacting demand.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPRDRVb21DVDRrNGdwTllmTFZ6RGVFVlV5d2huRENFNVlZTThTZGZEQnBDWEJKQUlGYU9FNGRQdThLekZmblY3WFY0X3B3MDRlY1JNcjd2ejZscjdQVVJPQm5JdmczM2NnZFdiaVQxSmU2Q2w3V0FKazhHcVNVMDJtMmNvZUZxR3ctVXYwMDd6Uk1BVk5EYkZSRQ?oc=5>

### Why Is Micron (NASDAQ:MU) Stock Surging Today? SK Hynix Signals AI Memory Shortage
- Summary: Micron shares rise amid AI memory shortage signals from competitor SK Hynix.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTE1oLXBKdVlfWWwwOGhMNjVkNlZyLVp0SkVsMFA0bFRmWXZiMVAwbkZVNE8tdXFOcUVaaU1Kem5tZExGdWpCTmEzUUNKZXdUVThrMy1YaG92cXhuN2U4Z1VPRXF0RjNrUUQ1Ykl4dlh6M0gxd09nQklYMw?oc=5>

### Micron (MU) Surges 5.86% Amid Positive Market Trends
- Summary: Micron shares jumped 5.86% driven by favorable market sentiment and positive outlooks for the semiconductor sector.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxOYklrLU90MWk5cHYxQUllZUZLUFp2S19tN0ttWG5xbGtseEkxZF9ZSVh1VUgtbzNNRWc3UWtYaEZDYVFrTXJPRGxLQlBNS1pyamp4NXpXbHZOSHZxSW1LVFg4XzE3ZmZnaFZ1T2VISlZ0MHk1SWoydmJrWUR2SGVMYXpSd2ZWNGRVRVVKQkVkREY?oc=5>

### Micron Technology Inc Stock (MU) Opened Up by 4.81% on Oct 28: What Investors Need To Know
- Summary: Micron stock opened 4.81% higher on Oct 28, reflecting investor optimism and potential catalysts in the tech market.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxPRHN4dlpxOS1ORFA5TlVZNmVDS1FMbXd2eEJfU1dDLVlFNW5HV2NXNmN5SWhrWDZVcjB1UWVzaEM1X08zUGE1eHF2Z2tLbWU0bE9sUEpWMXN4WEJNZE1UbEVQODVZWFB3aFVqTUlJNGI1M2tCS05qSk9Ud3c3UHNMVDdwRmhxb1NG?oc=5>

### Why Is Micron Technology Stock Surging Wednesday?
- Summary: Investors are reacting to positive market trends and potential company-specific catalysts, causing Micron stock to surge on Wednesday.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPVWJ5TUVtNDdRbGlqMTllV2VnS1BnVzNmbHhnbGxGU0FtYjVDVGpsSGZUTXI1SEE2OW9JRmlGaXdwcnkwQzV4andSVlNXMVZfX3JBemVVVmZUTjIwbXM3NFpzZXNUYjE2Nm9GVXYxNHdLSGN3SnVscUhOTmpaX1JPNDN1a2VpV043SF85MVRLeTZMd1M3NFVFS0lxZVlhWFJsS3BiNml3?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MU** | **12.49** | **8.04** | **9.87** | **379.30** | **1,112,449,220,608.00 USD** | **343.58** |
| WDC | 13.40 | 15.86 | 23.45 | 55.50 | 148,389,232,640.00 USD | 217.93 |
| STX | 50.21 | 73.05 | 34.11 | 48.50 | 158,713,495,552.00 USD | 214.84 |
| NXPI | 21.64 | 6.33 | 14.21 | 19.50 | 63,467,200,512.00 USD | 20.27 |

Peers fetched as_of: 2026-10-28; MU reuses existing data (market data as_of: 2026-10-28); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-30
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-28

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

- https://news.google.com/rss/articles/CBMiugFBVV95cUxOQXM1N1o1ME1jS09hZ0xQRzVqZlRiMHlfd3lra25nTEhuVVJndnNzdFJpQ01SQUZHUnJqQ3FmS0tvcWdpbmtxaDN1ZXZLbGNRajBmMm9pbF82ZUtwNms3R0JwbXo3Uzc1bmlvQ3VZTEtOVElJVHlGZUFLRWlVSU55MHpGQlNlWXBncUpRaG5waV8yTmxYazBFY1VDendfWk94Tm4yMm5iVHFiZWJaRlpfaC1CSDNqYXJiVUE?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPSVp0SEVqV2ZKY1BKYXJGZXhZcGZNVzZwdnBrV0NhWGtTaTEwMVNBb0hjZEx4b1VYR1B6UzdJNzdXaE5OZFhSZzhZQlhhWmNSelFxYXRCaG8tTEVHRU9DZE5TcmZDaXdHRzdBTjhlbDhqNGM2d1lQbnZpbVdlb1ExSTlXaDB3UzhXd081UzU1Wkp0OE9YT1pOWFFUZjR3V252TkxBTHI1T3J5aEdzdDcw?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTE1NSnA4QTg5U0hoaGRRRFdFZC1wS2REemx2em5RTHl0Q3R6YVFQSW1QVmFaTTBGM3F0N0RWT2ZWTm5WeDVIODVqUHN5S3hBeExPRXVJZ08wQ2JBejJtVHRBYVRnRnpPbFNOcldMcVV1ZEhiZDdIQUJDY2JJVWI?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQYTJMOG1zSzlhSmpGWWI2MEp6Z3N5REo2Z1lUbzBjNkN6YzBVOEI3VlNBTkNUODJQaVRnU3Zfb2RvRTROMWQzemhaVXZmX2piQ3NBTGxSNDFfaEt6RmJiNWQxSFpvTkQzQmJQWW1uY0VlbFhZSGFTRTNVdklodWFIb01mazJPTUlmeVg3Sk15aXc?oc=5
- https://news.google.com/rss/articles/CBMie0FVX3lxTE1DQWdrcE4taWZpelc0ZWF6VWV5Vml3SmZTdmljVFZIVDZuVDNLUjhBYnlPYmxDR0RIRUo1ZTlIdHhlZTZ0Y0xtb3FwN2FlNlN4RHVfSHgxMHY1SlhQR2VlYnFBUzM2dFdPaXZ0WFA5aF9mLU03ZHZCbnJfTQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQbzV4YU5OcU1iY09HVlFneGh3SWE5S1VLQ0xWdE9OZDFYcmpMX2tuUGdKckhlTEs0dTFCbE5OY1EwRjhNdV80VTU2bnJRSmpGQ2M5al9CcXBvMEhaTk1lLWhRM0pxcWtEX1dZQXZ0b1pNRXp5V25zT09UYUFkMThZbV9ZbS1lR1R5N2NpSE41ZjhmbWFiYWRzZTVMcm8?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQTUNoNzFRRHJBOHBKS1NiMnQyX1d4dEtIN29zaV9OeFp1bUtHNXZ5NC1WUnFGdWVyc3l3bl8wQ0FTbG5Hb0dmQnBqcU16bENvYTVLbERjbkY5VVo0dHk5WWZYS0J0bF9IVERYZGt1T2J5T3pneEdwUFpDNjFuQmFWTzhxSFhqQjg1NE5CN1BoSGIybkdUUENhb3R5d1E?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPMDhIM08yQmdNbkJDS2lzak9KeTdRMkpndnZjNmNvZE9EaE1sNGNoaDhqTGNWT21VVVhLRTZfbGxkdmQ3Y05RMW83Ml80YXVqYmtXR2VXTkZsWXg5eVB0a2QtLUFERTNoVUtwc1BJTjBNT2p1Y1JJbFlKdzRSVWt4MWFYS1ZOYW1WRUprQ2h3?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQQnBiNHhYVEFQWUxqR2ZpYUlHTXUzbHI5ekRwMGhRbmRtRno1UmdicEhNcVlYQ0U4Q29CcU9Xak1lcW9JVDZnbWJmdVZLdk5KbEh4allmemNMVWY5bXNGVkhqdHQ3Uy1NV1llVDJXMDVXbzFsWE5ibHB0emxBYi11c2pwUDBHNzd3Vy12enNJdm1NRC1tTC1CeDRtNUczbzdl?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPNDVmcHh4WlRMQVZydHJ2QnRCM0E3NF9aTGd1OTRVM016LWxQU2JSLUQ0Q3NKbHVaSmRfZXVYOEhac1hkSGJHSG43elF6SEtOXy1PYW5sWk9VbUV1MWNkVU1SZ3RlM25VbUFiVUxNM0tFdTh3NEtZUnExaUd5REJEQUdyVXZEMVhNcEdiMlp5OERHUnFRVGpxYXBDYVN3NjJtcG91WUxfOVZzQnpaMzQyb1JBRTRIQ2VtUFlWYkNuSnBmdw?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOaG8tM2JnYmdKRVRUTjhrVVpYT3l0a2J6VDNhYkJlTjVHNzdhYzNQVmlPNDdPd2paOWZ2LUxDVzN0MGNBbFdoQmZkaGZsM3pBQ0Rwbm8xRC04SFBtQ0NEM09ueFdsTDRycHp0NnloNGNGZWZNTnd3S0VJeS05dmwzcU02RV9iRjlLWGNlTmE5R0tybUNOU21NNFFoQUNMb3FFLXloUA?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQU0NKUDZrYmo5dEcyMllySC1BZFRZTUxPZFp5TzJmOGl5ZTdIaEpXcWJVSWtlNDhuWGFSclN6ZkJ3d29CLUluMWtUcGowaXBadVVBY0tqVS1mUkstcHFsLXI1RWp0RmpOdm5OZzJLSktYZ0tmZ0gwRG1XMFN5ZFdtaGNnenc4TVBsczR3d25fVlFrd3dMdGJjVXlMVFlUV2JqdkE?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNbzJCRVVpMElSTVRlQ2ZoTmE2RUtEVWFYei15Ykg5TUhobGVhaGZabGtUZzJ1VFM0WHFCWGdETHQ0dVFnQ3N5SDFyRjQ4c250OG43ei14YUs4bjB5VUVRWmtVTWtTN0J2TVVHVzZQcG40X1hSbzJubnVYUGJHRE5ueXUzRDVsQUV3M0RWdQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNR0xMVWVZZjAtdzlUbkdZdlAwSGpTM1dpd2VibzlxR0xoeVpjVlZuWVBXSFQ5dGhKRHV5TnlYLXdqdXBNZWp4VmJ3a0tBMnhRazF0WkU1Q1ZYeElwU0JFVE5zWVF6d0Z3eEJDQUwzOEczNEhDUmlCT2dxSkE3UEE1NHUyTHhoSDVlM3JmZUMzM2Fsc2g1TlZEMjVn?oc=5
- https://news.google.com/rss/articles/CBMiTkFVX3lxTE12OGhUSWtGTk9iWTJqbXhwZ2hpa25tNUxnRWlMam1RYkNBckpUdlVCMXgzY2ZDbG1HUkdxeFlUMWRkZ3ljR2xXUkdJb285UQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPRDRVb21DVDRrNGdwTllmTFZ6RGVFVlV5d2huRENFNVlZTThTZGZEQnBDWEJKQUlGYU9FNGRQdThLekZmblY3WFY0X3B3MDRlY1JNcjd2ejZscjdQVVJPQm5JdmczM2NnZFdiaVQxSmU2Q2w3V0FKazhHcVNVMDJtMmNvZUZxR3ctVXYwMDd6Uk1BVk5EYkZSRQ?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTE1oLXBKdVlfWWwwOGhMNjVkNlZyLVp0SkVsMFA0bFRmWXZiMVAwbkZVNE8tdXFOcUVaaU1Kem5tZExGdWpCTmEzUUNKZXdUVThrMy1YaG92cXhuN2U4Z1VPRXF0RjNrUUQ1Ykl4dlh6M0gxd09nQklYMw?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxOYklrLU90MWk5cHYxQUllZUZLUFp2S19tN0ttWG5xbGtseEkxZF9ZSVh1VUgtbzNNRWc3UWtYaEZDYVFrTXJPRGxLQlBNS1pyamp4NXpXbHZOSHZxSW1LVFg4XzE3ZmZnaFZ1T2VISlZ0MHk1SWoydmJrWUR2SGVMYXpSd2ZWNGRVRVVKQkVkREY?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxPRHN4dlpxOS1ORFA5TlVZNmVDS1FMbXd2eEJfU1dDLVlFNW5HV2NXNmN5SWhrWDZVcjB1UWVzaEM1X08zUGE1eHF2Z2tLbWU0bE9sUEpWMXN4WEJNZE1UbEVQODVZWFB3aFVqTUlJNGI1M2tCS05qSk9Ud3c3UHNMVDdwRmhxb1NG?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPVWJ5TUVtNDdRbGlqMTllV2VnS1BnVzNmbHhnbGxGU0FtYjVDVGpsSGZUTXI1SEE2OW9JRmlGaXdwcnkwQzV4andSVlNXMVZfX3JBemVVVmZUTjIwbXM3NFpzZXNUYjE2Nm9GVXYxNHdLSGN3SnVscUhOTmpaX1JPNDN1a2VpV043SF85MVRLeTZMd1M3NFVFS0lxZVlhWFJsS3BiNml3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
