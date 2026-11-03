# MU Intelligence Report

- ticker: **MU**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/MU/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MU/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:18:06.163820+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 2, 'ai': 11, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/MU** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 11 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 34.78%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 833.5900 |
| Return 1D (%) | -5.7814 |
| Return 1W (%) | -7.7581 |
| Return 1M (%) | -22.4366 |
| Return YTD (%) | 192.2812 |
| Return 1Y (%) | 272.9440 |
| Annualized volatility (%) | 82.1592 |
| Beta vs SPY | 3.4294 |
| Max drawdown (%) | -39.0954 |
| Sharpe (rf=0) | 1.9635 |
| Downside deviation (rf=0, %) | 49.8650 |
| Sortino (rf=0) | 3.2352 |
| Historical VaR 95% (1D, %) | 7.0066 |
| Historical ES 95% (1D, %) | 9.5345 |
| Correlation vs SPY | 0.5352 |
| Tracking error vs SPY (%) | 76.0719 |
| P/E (trailing) | 11.21 |
| P/B | 6.81 |
| EV/EBITDA | 8.31 |
| Revenue growth (%) | 379.30 |
| Forward P/E (estimate) | 4.01 |
| Gross margin (%) | 80.72 |
| Operating margin (%) | 80.68 |
| Return on equity (%) | 88.26 |
| Free cash flow yield (%) | 3.09 |
| MA50 | 975.9314 |
| Close vs MA50 (%) | -14.5852 |
| MA200 | 749.1109 |
| Close vs MA200 (%) | 11.2772 |
| RSI (14, Wilder) | 37.4205 |
| MACD (12,26) | -30.4428 |
| MACD signal (9) | -25.1632 |
| MACD histogram | -5.2796 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MU': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 833.5900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -5.7814 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -7.7581 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -22.4366 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 192.2812 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 272.9440 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 82.1592 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 49.8650 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 3.2352 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.0066 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 9.5345 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5352 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 76.0719 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4294 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -39.0954 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.9635 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 4.0123 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 80.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 80.6780 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 88.2600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.0897 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 11.2147 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 37.4205 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -5.2796 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -14.5852 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 11.2772 -> Clearly above the moving-average trend level.

## TAILWINDS

### MU Stock Falls to $840 as Kioxia Outlook and Big Tech Earnings Raise Memory Market Concerns
- Summary: MU Stock Falls to $840 as Kioxia Outlook and Big Tech Earnings Raise Memory Market Concerns
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxNREFsa1Jma1JjenEtQ280RlRaTThBRkFxSFJ2VW95WUMxZ215NkVjeHBJNTdOby1ZU3pfbVQ0VkdlTmF0TnFsOFZqMkgwWXR2N1RGaFdna2lNQ1RxajhkNDRmQ1Bsa1VmMzh6ZWdrZlh6Q2FtdTIzTndyYnI0VFUwb2ZlRVI4ZGR2YXBZTDVZSkNQTmZ1dEJWYW9kajdtcTR2eUx0WUlfTTJ2SjRjUzN0c0ZULVVMeEhOUTRGUFk4enhDN3lPUzBRcUFiWlk4QQ?oc=5>

### Micron Stock: Why I'm Buying, Not Panicking (NASDAQ:MU)
- Summary: Investor confidence remains high, driving a positive market reaction.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.92
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxQMk1nQ0FUSXQtejZyZ2tjX2N3S19ManMxSG02bU5tVGowb3BzejFBUllTaVlqMUR6M1A0a3dpUldiRVBRWktfbnR4LVhjOXhldVBDSm1GWlNrU0ZNWnFrNDRtSjUyZHVHa2RBU1dpVFFJcFZTbTQ4UFdWVTVFaTR4dU1WaUJweEs1?oc=5>

### Micron Just Unveiled a New Bonus Plan. What That Means for MU Stock.
- Summary: Micron introduces a new bonus plan, potentially boosting shareholder value.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPSVp0SEVqV2ZKY1BKYXJGZXhZcGZNVzZwdnBrV0NhWGtTaTEwMVNBb0hjZEx4b1VYR1B6UzdJNzdXaE5OZFhSZzhZQlhhWmNSelFxYXRCaG8tTEVHRU9DZE5TcmZDaXdHRzdBTjhlbDhqNGM2d1lQbnZpbVdlb1ExSTlXaDB3UzhXd081UzU1Wkp0OE9YT1pOWFFUZjR3V252TkxBTHI1T3J5aEdzdDcw?oc=5>

### Micron Expected to Launch Massive Stock Buybacks in December. What to Know.
- Summary: Micron plans large December buybacks, signaling confidence and shareholder value support.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTE1PaEJIZWFJMXNaTnNieTMyTzFvT1NtOVVPT1FURXRpTEtQdWtIVDl6VTZsWjZrLWQyTDhHc19qUUN4OVNkLUpqUjN2Q3FLemM1SzNnb1VwcldfSmIwVzJ5VUpLWmQ4NFhPdWoxZ3BOczRuYmdzUEFxdEdIVTFCSnM?oc=5>

### Why Micron Stock Looks Cheap After a Record Year
- Summary: Investors see Micron undervalued post-record earnings, boosting buying interest.
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNYnFkdWZsZ2RTLVM3dkNBZWEzVXdETlRsbDRnVTRvdmRqbkt2Nk1ERS1SazA1NDVzZ29VUFhHX0ZzY3pSZ2Vwa29Sd3BxaVc3TDIyYlJTS0lQTFNvY3hPQzQtdWtfTWRCRHFiSWFNS0pSWko2eFdzM1U5V1RRQWlwaUdNVXRQUXA5WkVmNUNwYzlMcEVmTGc?oc=5>

## HEADWINDS

### Micron Technology Inc (MU) Shares Fall 5.8% -- GF Value Says Sti
- Summary: Micron Technology Inc (MU) Shares Fall 5.8% -- GF Value Says Sti
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxOQ2FJQTV3dmQtZ1RZU280b1ZVTWM3NGNjbUpJRDVZeVhZN2VHMGdOLWE0MjNNNzZLQU10T1U1WjdnM2JWaXpaaEh0YWZnMTlWX0dvTGdQRnBkZlpUNTJQRFJZUmo3Q240azlRQnc4U0NuTE41M05zQlQ5NERUVThoYVZCaGY2REVkOFNJX2M1TlYzcGg2QjJVTVpfcmhzZUNUdXhzSVIxcW4wNDhzSFE?oc=5>

### Micron Falls 4% as Kioxia's Cautious Outlook Hits Memory Stocks; Western Digital Drops 5%, SanDisk Slides 3%
- Summary: Micron shares dropped 4% following Kioxia’s cautious outlook, impacting memory sector sentiment.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxQd24xZ3lROHBoV1M2WWN3VmlMUjNjZ1ZfZnNNNGFmWnhZZ2d5Qnl4TjZMd3FPSm44N0VIRFhVM2s2RkNpVmdvMWJYeUZnRWR5YWhIdmtKdUpiQndZV19vaFlFRU1hZ1FfTk9GRzJ4M3lXLVJHclZ0cmpzYW9CbkJvb1BYNGNDYmpJTkJhWkRmMklmN3EtM2ZYc2V2bzEzdGZCVTJtZmVvVVk1SjhTQUQtNzZ2MDlQaXQ3T3NSaVBjQ0FCRm53Mkc3UEtzOGNWaUc2XzhVb0NNS3Ryc1JsZkVN?oc=5>

### Micron Falls 4% as Kioxia’s Cautious Outlook Hits Memory Stocks; Western Digital Drops 5%, SanDisk Slides 3%
- Summary: Memory stocks fell after Kioxia’s cautious outlook, dragging Micron down 4%.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQRFdaTWVZNFItSTAwUXVrUURyUndmWDRHX3VJeE5XRDFGaGIyZWZHNTNQRnAwZHVuZVNkenFzSHpGc1BwLTBEWnlmRjJSOV9XcmpvVjV3N1Y5MEsxNFpLaXVQczB0SWV0Ni03c3VKa3N4UEdNbnQxOThBdmxWWnFTRjNaWk5neDItcFJqRHhNcGNXVEtkQndmaFI1WQ?oc=5>

### Micron Stock Needs Markets to Clear These 3 Hurdles
- Summary: Micron faces three market obstacles that could hinder its performance.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxOUWhELWk4QTd2akFpU0NnMlVqS2NIM0NIQVpkYXRBX3B4QV95Mjh4ZUg2WHdObFozc3hMLU9iVTZSeEFQX2ZJZVZ6RnhzR2RHZkNlSWpXUVlpMXgtY1YtQ05qYTZsVlFlUkVDc2l4cUg4LS1raWVRODBHQ2EzODBjZGlR?oc=5>

### Micron Technology Inc Stock (MU) Moved Down by 3.07% on Nov 2: Facts Behind the Movement
- Summary: Micron’s share price dropped 3.07% on Nov 2 due to market factors.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxQVG9JSnU2c1Y4WWJwenIzWnBocTZUM3haNHFaYWFBdHV1bllRdGFscGYwcnY4eWRfVkZKcGN4ckFOSDJaWXNFSy1PZzFWMmV2R0xHVmE2Qml1T3h6ekhPcV8wTjJtQVFDVkxTWTdXeEtTZHdadG96d0ZPbVpxczVWaDZ1RHRGRGJK?oc=5>

## CATALYSTS

### What Could Robot Memory Demand Mean For Micron Technology (MU) Stock?
- Summary: Increased robot memory demand could boost Micron’s revenue prospects.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNR0xMVWVZZjAtdzlUbkdZdlAwSGpTM1dpd2VibzlxR0xoeVpjVlZuWVBXSFQ5dGhKRHV5TnlYLXdqdXBNZWp4VmJ3a0tBMnhRazF0WkU1Q1ZYeElwU0JFVE5zWVF6d0Z3eEJDQUwzOEczNEhDUmlCT2dxSkE3UEE1NHUyTHhoSDVlM3JmZUMzM2Fsc2g1TlZEMjVn?oc=5>

## RISKS

### Micron is the Real Loser in Lumentum Deal Which Assumes “Market Will Collapse in Two to Three Years”
- Summary: Micron loses in Lumentum deal amid pessimistic market outlook.
- Date: 2026-11-02 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPeGxLa3pNZmJCekw5Rk53S3RTY1lFM0ZQR3JDX2ctZTJHeXViUU5tZkk2TjAtU0tjM0FyV2NaYnFja2lwYVM4T1hIZTB1VHI5LThCT1I4Zm1taFlqZENmQVZ4bXFjT2ppNUJnTDRVLXBhcWtOLWVfd011Q3RRd21ETUVMdlFBRFFpQkRWaWpJS2JFYUN5djdFUkVWbVc?oc=5>

### Micron vs. SanDisk: China's DRAM Scare Hit Both Stocks, but 1 Is the Better Buy
- Summary: DRAM scare impacts Micron, raising risk concerns.
- Date: 2026-11-02 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxOdEFZQXlVNFZTZjFXRTBSdEFXZ0FWeGdHczdqVFV5dXNYNXppOUlhR0t6T3ZRX1lVcU1PQjVveFhYVFdLOEtIc0NSdXp4MWVuZkROaF9pbEpGNVJjZ25XUkVSYmtERlY4MUJyT1d6Q3c4U2NiSTRNYnBma1Y0WUdYN252eFAxTkFUNXh0QnE5UWplNDFzeHI0X1NlZFpmWVZxb2lfa1FRNy10cE56ZjhWTnMyQzVSVmY5bWtDaw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MU** | **11.21** | **6.81** | **8.31** | **379.30** | **943,143,124,992.00 USD** | **272.94** |
| WDC | 11.91 | 13.55 | 20.02 | 55.50 | 126,742,110,208.00 USD | 125.83 |
| STX | 33.79 | 39.50 | 23.47 | 61.00 | 136,304,205,824.00 USD | 133.41 |
| NXPI | 20.24 | 5.36 | 13.41 | 19.30 | 64,838,111,232.00 USD | 25.18 |

Peers fetched as_of: 2026-11-02; MU reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-30
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMizgFBVV95cUxNREFsa1Jma1JjenEtQ280RlRaTThBRkFxSFJ2VW95WUMxZ215NkVjeHBJNTdOby1ZU3pfbVQ0VkdlTmF0TnFsOFZqMkgwWXR2N1RGaFdna2lNQ1RxajhkNDRmQ1Bsa1VmMzh6ZWdrZlh6Q2FtdTIzTndyYnI0VFUwb2ZlRVI4ZGR2YXBZTDVZSkNQTmZ1dEJWYW9kajdtcTR2eUx0WUlfTTJ2SjRjUzN0c0ZULVVMeEhOUTRGUFk4enhDN3lPUzBRcUFiWlk4QQ?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxQMk1nQ0FUSXQtejZyZ2tjX2N3S19ManMxSG02bU5tVGowb3BzejFBUllTaVlqMUR6M1A0a3dpUldiRVBRWktfbnR4LVhjOXhldVBDSm1GWlNrU0ZNWnFrNDRtSjUyZHVHa2RBU1dpVFFJcFZTbTQ4UFdWVTVFaTR4dU1WaUJweEs1?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPSVp0SEVqV2ZKY1BKYXJGZXhZcGZNVzZwdnBrV0NhWGtTaTEwMVNBb0hjZEx4b1VYR1B6UzdJNzdXaE5OZFhSZzhZQlhhWmNSelFxYXRCaG8tTEVHRU9DZE5TcmZDaXdHRzdBTjhlbDhqNGM2d1lQbnZpbVdlb1ExSTlXaDB3UzhXd081UzU1Wkp0OE9YT1pOWFFUZjR3V252TkxBTHI1T3J5aEdzdDcw?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTE1PaEJIZWFJMXNaTnNieTMyTzFvT1NtOVVPT1FURXRpTEtQdWtIVDl6VTZsWjZrLWQyTDhHc19qUUN4OVNkLUpqUjN2Q3FLemM1SzNnb1VwcldfSmIwVzJ5VUpLWmQ4NFhPdWoxZ3BOczRuYmdzUEFxdEdIVTFCSnM?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNYnFkdWZsZ2RTLVM3dkNBZWEzVXdETlRsbDRnVTRvdmRqbkt2Nk1ERS1SazA1NDVzZ29VUFhHX0ZzY3pSZ2Vwa29Sd3BxaVc3TDIyYlJTS0lQTFNvY3hPQzQtdWtfTWRCRHFiSWFNS0pSWko2eFdzM1U5V1RRQWlwaUdNVXRQUXA5WkVmNUNwYzlMcEVmTGc?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxOQ2FJQTV3dmQtZ1RZU280b1ZVTWM3NGNjbUpJRDVZeVhZN2VHMGdOLWE0MjNNNzZLQU10T1U1WjdnM2JWaXpaaEh0YWZnMTlWX0dvTGdQRnBkZlpUNTJQRFJZUmo3Q240azlRQnc4U0NuTE41M05zQlQ5NERUVThoYVZCaGY2REVkOFNJX2M1TlYzcGg2QjJVTVpfcmhzZUNUdXhzSVIxcW4wNDhzSFE?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxQd24xZ3lROHBoV1M2WWN3VmlMUjNjZ1ZfZnNNNGFmWnhZZ2d5Qnl4TjZMd3FPSm44N0VIRFhVM2s2RkNpVmdvMWJYeUZnRWR5YWhIdmtKdUpiQndZV19vaFlFRU1hZ1FfTk9GRzJ4M3lXLVJHclZ0cmpzYW9CbkJvb1BYNGNDYmpJTkJhWkRmMklmN3EtM2ZYc2V2bzEzdGZCVTJtZmVvVVk1SjhTQUQtNzZ2MDlQaXQ3T3NSaVBjQ0FCRm53Mkc3UEtzOGNWaUc2XzhVb0NNS3Ryc1JsZkVN?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQRFdaTWVZNFItSTAwUXVrUURyUndmWDRHX3VJeE5XRDFGaGIyZWZHNTNQRnAwZHVuZVNkenFzSHpGc1BwLTBEWnlmRjJSOV9XcmpvVjV3N1Y5MEsxNFpLaXVQczB0SWV0Ni03c3VKa3N4UEdNbnQxOThBdmxWWnFTRjNaWk5neDItcFJqRHhNcGNXVEtkQndmaFI1WQ?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxOUWhELWk4QTd2akFpU0NnMlVqS2NIM0NIQVpkYXRBX3B4QV95Mjh4ZUg2WHdObFozc3hMLU9iVTZSeEFQX2ZJZVZ6RnhzR2RHZkNlSWpXUVlpMXgtY1YtQ05qYTZsVlFlUkVDc2l4cUg4LS1raWVRODBHQ2EzODBjZGlR?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxQVG9JSnU2c1Y4WWJwenIzWnBocTZUM3haNHFaYWFBdHV1bllRdGFscGYwcnY4eWRfVkZKcGN4ckFOSDJaWXNFSy1PZzFWMmV2R0xHVmE2Qml1T3h6ekhPcV8wTjJtQVFDVkxTWTdXeEtTZHdadG96d0ZPbVpxczVWaDZ1RHRGRGJK?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNR0xMVWVZZjAtdzlUbkdZdlAwSGpTM1dpd2VibzlxR0xoeVpjVlZuWVBXSFQ5dGhKRHV5TnlYLXdqdXBNZWp4VmJ3a0tBMnhRazF0WkU1Q1ZYeElwU0JFVE5zWVF6d0Z3eEJDQUwzOEczNEhDUmlCT2dxSkE3UEE1NHUyTHhoSDVlM3JmZUMzM2Fsc2g1TlZEMjVn?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPeGxLa3pNZmJCekw5Rk53S3RTY1lFM0ZQR3JDX2ctZTJHeXViUU5tZkk2TjAtU0tjM0FyV2NaYnFja2lwYVM4T1hIZTB1VHI5LThCT1I4Zm1taFlqZENmQVZ4bXFjT2ppNUJnTDRVLXBhcWtOLWVfd011Q3RRd21ETUVMdlFBRFFpQkRWaWpJS2JFYUN5djdFUkVWbVc?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxOdEFZQXlVNFZTZjFXRTBSdEFXZ0FWeGdHczdqVFV5dXNYNXppOUlhR0t6T3ZRX1lVcU1PQjVveFhYVFdLOEtIc0NSdXp4MWVuZkROaF9pbEpGNVJjZ25XUkVSYmtERlY4MUJyT1d6Q3c4U2NiSTRNYnBma1Y0WUdYN252eFAxTkFUNXh0QnE5UWplNDFzeHI0X1NlZFpmWVZxb2lfa1FRNy10cE56ZjhWTnMyQzVSVmY5bWtDaw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
