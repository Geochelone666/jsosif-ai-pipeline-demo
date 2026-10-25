# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-10-24**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-10-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-25T01:21:34.635030+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 5, 'ai': 13, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 8 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 52.0%; oldest publication 2026-10-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 210.9600 |
| Return 1D (%) | -0.5890 |
| Return 1W (%) | -1.4804 |
| Return 1M (%) | -6.4520 |
| Return YTD (%) | 13.3800 |
| Return 1Y (%) | 16.0877 |
| Annualized volatility (%) | 37.6734 |
| Beta vs SPY | 1.9371 |
| Max drawdown (%) | -20.2144 |
| Sharpe (rf=0) | 0.5846 |
| Downside deviation (rf=0, %) | 25.2659 |
| Sortino (rf=0) | 0.8716 |
| Historical VaR 95% (1D, %) | 3.7736 |
| Historical ES 95% (1D, %) | 4.5600 |
| Correlation vs SPY | 0.6554 |
| Tracking error vs SPY (%) | 30.8591 |
| P/E (trailing) | 26.67 |
| P/B | 22.25 |
| EV/EBITDA | 25.14 |
| Revenue growth (%) | 105.90 |
| Forward P/E (estimate) | 13.26 |
| Gross margin (%) | 74.67 |
| Operating margin (%) | 66.24 |
| Return on equity (%) | 117.21 |
| Free cash flow yield (%) | 0.82 |
| MA50 | 222.3939 |
| Close vs MA50 (%) | -5.1413 |
| MA200 | 203.3622 |
| Close vs MA200 (%) | 3.7361 |
| RSI (14, Wilder) | 38.1063 |
| MACD (12,26) | -2.6295 |
| MACD signal (9) | -0.4706 |
| MACD histogram | -2.1589 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 210.9600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.5890 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.4804 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -6.4520 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 13.3800 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 16.0877 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 37.6734 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.2659 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.8716 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.7736 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.5600 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6554 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.8591 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.9371 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.2144 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5846 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 13.2558 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.2370 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.2110 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.8208 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 26.6700 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.1063 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.1589 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.1413 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 3.7361 -> Slightly above the moving-average trend level.

## TAILWINDS

### NVDA, ZM, SPCX Stocks Rise Premarket: Nvidia Announces AI Factory Pods, Zoom Gets Upgrade, SpaceX Target Rises
- Summary: NVDA, ZM, SPCX Stocks Rise Premarket: Nvidia Announces AI Factory Pods, Zoom Gets Upgrade, SpaceX Target Rises
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOelAyY21HT3RjY0t4X005MDk4Z1M0akpYRGlXUTJkNkZONTRIYVh5b0M5bWNYbVJtOTAyeDU0cURuODZNMnlRMExqS3dqdnJPcUVkZEh2VkxpLXkxT3c1TFk0ek8taU0xN1ZPMEVmb21xaWJXYm96WEZWVm5JdjNXWWc1SVBYZS1kZFlOeVR1SjJ4ZkE?oc=5>

### Jim Cramer’s 5% to 8% rule puts Nvidia stock in focus
- Summary: Jim Cramer highlights Nvidia’s potential, suggesting its stock may benefit from his 5%-8% rule, indicating positive investor interest.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQQXVnYnlTVmxDSXpQTnU4R0dYMk12TVVUcW5wMXNyck5rNzhEZ3JIMFVlT05Qc0JUYmRzdV9rcy1aQXl6QVVJV3QxNWp3Y3hwT25HTmRqQXFFcFgyZG1EaE95Q0dhdVlLS1lydnplYnNmakhlOW81OXhVTks2RlRCUzZFQ1hJd1dMTl82dF8zY0FvUzA?oc=5>

### Prediction: $200 a Month Invested in Nvidia Will Be Worth This Much by 2035
- Summary: Forecast predicts significant growth for Nvidia shares, projecting a $200 monthly investment to yield substantial returns by 2035.
- Date: 2026-10-24 | Impact: medium | Horizon: long | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPQjRKeXR1Y2ZxeVBnS21lRDA2S0t4a18yNHJfdVpwUS1DbC1qZEZ2NUFBdnBVMVk4QldTdlVYZjRNWml0LWNpdTNucFYwbVBnMzBjWjZyYV9DMEp2by1ma0lpNW84RUNwYTBpT0l4VHh3MEZHZlVLcU5ITld0Nzg5RjFQNi13eEZha0Z3M1ByVGx1aEVnRjRF?oc=5>

### Nvidia (NVDA) Is Trading Like Growth Will Stop. The Numbers Say Otherwise.
- Summary: Analysis shows Nvidia’s stock trading at levels suggesting halted growth, yet underlying data indicates continued expansion.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.88
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPWmZRM3VWRTlhU2ZBMW9Gek9TdDhFdEN3b3hra3JpYmdEcjJHTFdVdE9vX1N6M1N6RGhIbFo2TVVweldTV1hCVDBBelFlZHREODVud0ZRODlvRzlyT1JfV3BVYUh2S1hnMjNTSDdFamc3dHp5MGt0QWl6T3pGMkxCb3o4bTMzNEVFNV9COEYyajUwb0hfODJZZEZwT2c?oc=5>

### Is Nvidia (NVDA) Stock Priced Right?
- Summary: Analysts question if current price reflects Nvidia’s value, suggesting potential upside or downside.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOSVFUQnhDODFOX1o0Zkl1WWJQbTRfRkZjSFNNdnBYaGV5TkMydWFxX3VGdTJzRzh4RlVyNXpIMXhPb1NscWlMS1h4NG5TV3pCNXhPekIyOGkwbktPWnJMdFFESjdRbVJheVVJV2t4X3FXemlvYThrTWRFZHF0YkM0NjRtTzNmU3VkLS03VzBLb1c5X28?oc=5>

### Wall Street Didn’t Expect This AI Stock to Become This Important
- Summary: Highlights Nvidia’s growing importance in AI, indicating potential for significant future growth.
- Date: 2026-10-22 | Impact: high | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNdHlRVGdTbjJiaHp2c1NXajNTd0FiS0tnN0tJTzBWYnh5SzBPWFVpTjR4VGtFNDJDTldzUXdMZVNxZDNMYWVPSlYxenVvUFNZY0Y1dkdDcmsxNV9zTF9SdjU3UGY0MVJrU2d3Q1V6YlJ6YTRWQW1ZdVBmV1NsYWhCYlhMUDhHaFJUTXNidUJOQzNoSUlj?oc=5>

### Dan Ives Calls the Selloff in NVDA Stock a Buying Opportunity as Analysts See 53% Upside
- Summary: Analyst sees selloff as chance to buy, projecting substantial upside for Nvidia shares.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPaUZUTjRrMXpoYXFnZlNiQlpkZEVwMllWMXB2akU5MXY1bDJES2h6SURONkZsYVdqUmxZcGNsc3BOWHBmTUJrR01IN1FPRS1QZjBIaDBaWURsTlZncy0xdFV1SzFRWUphTkRNTHRyS2ptRG5kSFNhaGVPYzFFYTVDLXVNNVcxQk5HamlkMGgyU2Q3TS11bGs0?oc=5>

### Elon Musk Just Gave Fantastic News for Nvidia Investors
- Summary: Musk’s announcement is expected to boost investor sentiment toward Nvidia.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQUmhlUTRQcmF3XzFZOVdfX2JlY25od1lnQ3U0TU1jTzFBQTN3M1BHWDhmUDNYMUJ1dGZEbGpUOXdrbERmemtLM1JtaVg0dHFCX3ZNNWJkUk1zSmpYMmhsNDlwTnpBNU1QNWpzZmdlUU1UOEJvM19rNTJpUEJFcnloc1d0VzJXQXAxODRGVm1UaFg5aEU?oc=5>

### NVIDIA (NVDA) is Strengthening AI Conviction Balanced Against Evolving Competitive Risks
- Summary: NVIDIA boosts AI focus while noting competitive risks.
- Date: 2026-10-21 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNN1Rpd0dfWEJrS19ReUk5RlF5NWhJaVB5SEhvNldOTTdHLXFfbkVka0VYNWFhcENZOVdNd0gxaWViY0lLTlAzUzZlMjJLNUdtNU1Oa1RUQzE5elE1Z2ZaNUhoSF9QcmxFVXBmYUhpcG82MEJWT2pRdHBXQnlhLS1iWVYxTjRwYUZfY2kzUXJZemlVVmozREpQQzh4eUdmS09Sa014bFpB?oc=5>

### NVIDIA (NVDA) Leverages AI Growth to Expand Its Autonomous Driving Opportunity
- Summary: NVIDIA expands autonomous driving via AI.
- Date: 2026-10-21 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPQS1Yczc4QnhSUFFxa3ZVWkxoN0F2NGVPWFJSUWRQbnBEU2VCZmhqQjNadVgxVUtJSy1QWVJzODBLY2pCNEVhRllCcDdENG92dDBnNmY1TzlQVFE5UVdfYVY4NjQwZy0tbGNKQWlqcWZjdDkxUlNhb1MycTlGZ0pTdEZmZ2FsQUhna1BPcTEtYVRkWkJDVnR4RlBfQQ?oc=5>

## HEADWINDS

### Nvidia NVDA Stock Falls 4.4% to $212.21 as AI Financing Fears Hit Chips
- Summary: Nvidia NVDA Stock Falls 4.4% to $212.21 as AI Financing Fears Hit Chips
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxPREx6X3R5Rkdjb2hBdTJZSEZIekw4NWotVGlyaFFOc1U2ZjlBaHhTd3l4S3NhX3djUVNLbXJidXFpOG5leGlEalIyeDhsbWFMOHVFczZTMVR0Z3FqbnZObm5FZDhxVFVSZmNNOG5VT3YzTDJMaHg0Qy1ZS0lWNzY4TXlZR1pVS2x6a0ZmUFpMVFVJZERoZVFISzNYOU56UVlaYzNfWHJFamlubXRDbUl3TjBR?oc=5>

### NVIDIA Corporation (NVDA) Remains a Key AI Growth Driver Despite Benchmark Headwinds
- Summary: NVDA continues to drive AI growth, but faces benchmark headwinds that could temper performance.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNcVdHR2hGTWJjT2pSVUV3YUM3cUhBeHFlejVVUkdmM05DUHNsLVBVWk5mX2VqSFVQWmpMMnFVN0dmb3F6bUlXTW5CUGxXX0RGYmplbnNXVEJpQ0J2bllqU1RTdzFFa2M4bFlSeFctUTR5ODBjNTRXX25iOEFNRDJUTFFtdHF2cEE5b3R1QlFfbGd3VmJTN0pQYnJ4NllsWWFC?oc=5>

## CATALYSTS

### Nvidia Earnings Are Coming Next Month and the Stock Looks Poised to Dip Regardless of the Outcome
- Summary: Nvidia Earnings Are Coming Next Month and the Stock Looks Poised to Dip Regardless of the Outcome
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQbTNVTmJUcmZjdmpCZFMzdVZObFBqY1BIME4wLWtDUC1CMGFZZTRQaUd3aFBfZEFqUXNyLXFabThtQzUzdVFsbVg3VXlxZ2kxT3pQNWp1T2lHNV8tbThXM19YRkVIaWxjV3J5a2xlTUJTc1lUcnlXVDJYM2pvRElXR2tRbXVCbHhBWHAyTmx5TjBTMzNLenBGQQ?oc=5>

### Nvidia Stock’s 2 Critical Flaws and More Reasons an Analyst Says Sell
- Summary: Nvidia Stock’s 2 Critical Flaws and More Reasons an Analyst Says Sell
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE5SVktBZjJfVEV6cG1KNTRURUZ5MUNuSmFSeW5aeldtcWg4LWNkZC05TVVmRmhZYzhSWnNtbG81Vkt0ellCTWZ3dGRYMGptZ0xfZGdCTU8xY3lmR2tjNE80NE5MZ0l1R3M5M0xHV0k2THFIYk13QXlRRU5hSFdzZw?oc=5>

### Nvidia (NVDA) Stock Price Lags Massive Earnings Growth—A Compelling Value Opportunity
- Summary: Nvidia (NVDA) Stock Price Lags Massive Earnings Growth—A Compelling Value Opportunity
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOZWtGVi1wUVdnVHBCcFd5WFo4VWRRbWdYYjhjZ0tCaEVmT3M2YzJkMmN6VTJEUzFXdlhEWFhBcVBGMjJ3MFAtNkFMRWtNaHU4YzdiMzRhbm44MXBxcnAzdzlHcFZwSTRrVGRlWmg5ZWFDcVlSSG5qbTVscC1qY21HTm90Vm1SSDh0N0dHVm9TcnVfOXRKZzh5Tw?oc=5>

### Nvidia Stock (NVDA) Gets Rare Sell Rating. Here’s Why
- Summary: Analyst issues rare sell rating for Nvidia, signaling negative outlook.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxOMmthY0ZjT3BHV1dsSWZmZHh4bWZud1ljRHRSOEhOLTJUUTI1TXFDR0VBWUgwWnk5c2RGYTVqc2VaM2pyRFlTbUV6bUVSQlYyVUktRE9lZlktMmctWWF0ZW1tckJ4c2lSOXhCT1ZLNmxrNHJiVE1DamdYdTgxcEZnQkplMkF3dw?oc=5>

### Brokers Suggest Investing in Nvidia (NVDA): Read This Before Placing a Bet
- Summary: Brokers recommend buying NVDA, citing strong fundamentals and growth prospects.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPS3J0dHNFak5qLWJiRU01REZFS2lLaHE1MlY4UDQ4Y0prNW9mY2JfZ3FlTFI2MkpWQWN1NVVhUkNoMWFSeHlsV0FVcGI3Sl8tX05yZVJtREpKeDg1OFpuTVQxNms5OUhCNHJRN21EUjFpaUVBSnVIbTN2aGIxSHdjdWdVY3NEbTQ5VXlwVnk4MlZyZmNJQXlZWmU1TkxUN2tTenZYQw?oc=5>

## RISKS

### Apollo finds no broad AI payoff: NVDA stock forecast before earnings
- Summary: Apollo predicts limited AI impact on NVDA, warning investors of modest earnings growth.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMia0FVX3lxTE81OU10Ql9qQl9PcnlOeEUxRTMteVU3N2VLc2FYTm5xcXF5TEowVi0xWXNsVkhReE9jNU9GaFJSWXV2WEpsRkFLVGhna1hWU29vcVJnWGtUd0RPNDBWU3FOVUJrRU81Q0dPMGtR?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **26.67** | **22.25** | **25.14** | **105.90** | **5,094,050,889,728.00 USD** | **16.09** |
| AMD | 131.83 | 12.55 | 87.31 | 50.10 | 843,646,697,472.00 USD | 119.92 |
| AVGO | 42.95 | 15.40 | 30.06 | 85.50 | 1,535,581,224,960.00 USD | -5.87 |
| INTC | N/A | 5.01 | 28.21 | 25.40 | 459,679,694,848.00 USD | 127.88 |

Peers fetched as_of: 2026-10-24; NVDA reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-26
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-26
- Revenue (latest available single quarter): 96,221,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- Net income (latest available single quarter): 59,688,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMikwFBVV95cUxOelAyY21HT3RjY0t4X005MDk4Z1M0akpYRGlXUTJkNkZONTRIYVh5b0M5bWNYbVJtOTAyeDU0cURuODZNMnlRMExqS3dqdnJPcUVkZEh2VkxpLXkxT3c1TFk0ek8taU0xN1ZPMEVmb21xaWJXYm96WEZWVm5JdjNXWWc1SVBYZS1kZFlOeVR1SjJ4ZkE?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxQQXVnYnlTVmxDSXpQTnU4R0dYMk12TVVUcW5wMXNyck5rNzhEZ3JIMFVlT05Qc0JUYmRzdV9rcy1aQXl6QVVJV3QxNWp3Y3hwT25HTmRqQXFFcFgyZG1EaE95Q0dhdVlLS1lydnplYnNmakhlOW81OXhVTks2RlRCUzZFQ1hJd1dMTl82dF8zY0FvUzA?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPQjRKeXR1Y2ZxeVBnS21lRDA2S0t4a18yNHJfdVpwUS1DbC1qZEZ2NUFBdnBVMVk4QldTdlVYZjRNWml0LWNpdTNucFYwbVBnMzBjWjZyYV9DMEp2by1ma0lpNW84RUNwYTBpT0l4VHh3MEZHZlVLcU5ITld0Nzg5RjFQNi13eEZha0Z3M1ByVGx1aEVnRjRF?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPWmZRM3VWRTlhU2ZBMW9Gek9TdDhFdEN3b3hra3JpYmdEcjJHTFdVdE9vX1N6M1N6RGhIbFo2TVVweldTV1hCVDBBelFlZHREODVud0ZRODlvRzlyT1JfV3BVYUh2S1hnMjNTSDdFamc3dHp5MGt0QWl6T3pGMkxCb3o4bTMzNEVFNV9COEYyajUwb0hfODJZZEZwT2c?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOSVFUQnhDODFOX1o0Zkl1WWJQbTRfRkZjSFNNdnBYaGV5TkMydWFxX3VGdTJzRzh4RlVyNXpIMXhPb1NscWlMS1h4NG5TV3pCNXhPekIyOGkwbktPWnJMdFFESjdRbVJheVVJV2t4X3FXemlvYThrTWRFZHF0YkM0NjRtTzNmU3VkLS03VzBLb1c5X28?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNdHlRVGdTbjJiaHp2c1NXajNTd0FiS0tnN0tJTzBWYnh5SzBPWFVpTjR4VGtFNDJDTldzUXdMZVNxZDNMYWVPSlYxenVvUFNZY0Y1dkdDcmsxNV9zTF9SdjU3UGY0MVJrU2d3Q1V6YlJ6YTRWQW1ZdVBmV1NsYWhCYlhMUDhHaFJUTXNidUJOQzNoSUlj?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPaUZUTjRrMXpoYXFnZlNiQlpkZEVwMllWMXB2akU5MXY1bDJES2h6SURONkZsYVdqUmxZcGNsc3BOWHBmTUJrR01IN1FPRS1QZjBIaDBaWURsTlZncy0xdFV1SzFRWUphTkRNTHRyS2ptRG5kSFNhaGVPYzFFYTVDLXVNNVcxQk5HamlkMGgyU2Q3TS11bGs0?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxQUmhlUTRQcmF3XzFZOVdfX2JlY25od1lnQ3U0TU1jTzFBQTN3M1BHWDhmUDNYMUJ1dGZEbGpUOXdrbERmemtLM1JtaVg0dHFCX3ZNNWJkUk1zSmpYMmhsNDlwTnpBNU1QNWpzZmdlUU1UOEJvM19rNTJpUEJFcnloc1d0VzJXQXAxODRGVm1UaFg5aEU?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNN1Rpd0dfWEJrS19ReUk5RlF5NWhJaVB5SEhvNldOTTdHLXFfbkVka0VYNWFhcENZOVdNd0gxaWViY0lLTlAzUzZlMjJLNUdtNU1Oa1RUQzE5elE1Z2ZaNUhoSF9QcmxFVXBmYUhpcG82MEJWT2pRdHBXQnlhLS1iWVYxTjRwYUZfY2kzUXJZemlVVmozREpQQzh4eUdmS09Sa014bFpB?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPQS1Yczc4QnhSUFFxa3ZVWkxoN0F2NGVPWFJSUWRQbnBEU2VCZmhqQjNadVgxVUtJSy1QWVJzODBLY2pCNEVhRllCcDdENG92dDBnNmY1TzlQVFE5UVdfYVY4NjQwZy0tbGNKQWlqcWZjdDkxUlNhb1MycTlGZ0pTdEZmZ2FsQUhna1BPcTEtYVRkWkJDVnR4RlBfQQ?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxPREx6X3R5Rkdjb2hBdTJZSEZIekw4NWotVGlyaFFOc1U2ZjlBaHhTd3l4S3NhX3djUVNLbXJidXFpOG5leGlEalIyeDhsbWFMOHVFczZTMVR0Z3FqbnZObm5FZDhxVFVSZmNNOG5VT3YzTDJMaHg0Qy1ZS0lWNzY4TXlZR1pVS2x6a0ZmUFpMVFVJZERoZVFISzNYOU56UVlaYzNfWHJFamlubXRDbUl3TjBR?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNcVdHR2hGTWJjT2pSVUV3YUM3cUhBeHFlejVVUkdmM05DUHNsLVBVWk5mX2VqSFVQWmpMMnFVN0dmb3F6bUlXTW5CUGxXX0RGYmplbnNXVEJpQ0J2bllqU1RTdzFFa2M4bFlSeFctUTR5ODBjNTRXX25iOEFNRDJUTFFtdHF2cEE5b3R1QlFfbGd3VmJTN0pQYnJ4NllsWWFC?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQbTNVTmJUcmZjdmpCZFMzdVZObFBqY1BIME4wLWtDUC1CMGFZZTRQaUd3aFBfZEFqUXNyLXFabThtQzUzdVFsbVg3VXlxZ2kxT3pQNWp1T2lHNV8tbThXM19YRkVIaWxjV3J5a2xlTUJTc1lUcnlXVDJYM2pvRElXR2tRbXVCbHhBWHAyTmx5TjBTMzNLenBGQQ?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE5SVktBZjJfVEV6cG1KNTRURUZ5MUNuSmFSeW5aeldtcWg4LWNkZC05TVVmRmhZYzhSWnNtbG81Vkt0ellCTWZ3dGRYMGptZ0xfZGdCTU8xY3lmR2tjNE80NE5MZ0l1R3M5M0xHV0k2THFIYk13QXlRRU5hSFdzZw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOZWtGVi1wUVdnVHBCcFd5WFo4VWRRbWdYYjhjZ0tCaEVmT3M2YzJkMmN6VTJEUzFXdlhEWFhBcVBGMjJ3MFAtNkFMRWtNaHU4YzdiMzRhbm44MXBxcnAzdzlHcFZwSTRrVGRlWmg5ZWFDcVlSSG5qbTVscC1qY21HTm90Vm1SSDh0N0dHVm9TcnVfOXRKZzh5Tw?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxOMmthY0ZjT3BHV1dsSWZmZHh4bWZud1ljRHRSOEhOLTJUUTI1TXFDR0VBWUgwWnk5c2RGYTVqc2VaM2pyRFlTbUV6bUVSQlYyVUktRE9lZlktMmctWWF0ZW1tckJ4c2lSOXhCT1ZLNmxrNHJiVE1DamdYdTgxcEZnQkplMkF3dw?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPS3J0dHNFak5qLWJiRU01REZFS2lLaHE1MlY4UDQ4Y0prNW9mY2JfZ3FlTFI2MkpWQWN1NVVhUkNoMWFSeHlsV0FVcGI3Sl8tX05yZVJtREpKeDg1OFpuTVQxNms5OUhCNHJRN21EUjFpaUVBSnVIbTN2aGIxSHdjdWdVY3NEbTQ5VXlwVnk4MlZyZmNJQXlZWmU1TkxUN2tTenZYQw?oc=5
- https://news.google.com/rss/articles/CBMia0FVX3lxTE81OU10Ql9qQl9PcnlOeEUxRTMteVU3N2VLc2FYTm5xcXF5TEowVi0xWXNsVkhReE9jNU9GaFJSWXV2WEpsRkFLVGhna1hWU29vcVJnWGtUd0RPNDBWU3FOVUJrRU81Q0dPMGtR?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
