# BRK-B Intelligence Report

- ticker: **BRK-B**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/BRK-B/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BRK-B/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:04:10.773596+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 21, 'rule': 1, 'ai': 13, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/BRK-B** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 21 unique headlines; 4 named publishers; 4 exact duplicates; 21 HTTPS source links; largest publisher share 66.67%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 577.2100 |
| Return 1D (%) | 0.8474 |
| Return 1W (%) | -1.6276 |
| Return 1M (%) | 6.4590 |
| Return YTD (%) | 14.8334 |
| Return 1Y (%) | 13.6665 |
| Annualized volatility (%) | 15.1458 |
| Beta vs SPY | 0.0789 |
| Max drawdown (%) | -9.4218 |
| Sharpe (rf=0) | 0.9248 |
| Downside deviation (rf=0, %) | 10.2423 |
| Sortino (rf=0) | 1.3676 |
| Historical VaR 95% (1D, %) | 1.4206 |
| Historical ES 95% (1D, %) | 2.0519 |
| Correlation vs SPY | 0.0779 |
| Tracking error vs SPY (%) | 20.4382 |
| P/E (trailing) | 16.15 |
| P/B | 0.00 |
| EV/EBITDA | -2.04 |
| Revenue growth (%) | 11.20 |
| Forward P/E (estimate) | 25.30 |
| Gross margin (%) | 26.60 |
| Operating margin (%) | 26.60 |
| Return on equity (%) | 10.57 |
| Free cash flow yield (%) | 4.28 |
| MA50 | 539.2214 |
| Close vs MA50 (%) | 7.0451 |
| MA200 | 503.2860 |
| Close vs MA200 (%) | 14.6883 |
| RSI (14, Wilder) | 61.3785 |
| MACD (12,26) | 10.9062 |
| MACD signal (9) | 13.7086 |
| MACD histogram | -2.8024 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BRK-B': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 577.2100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.8474 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.6276 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 6.4590 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 14.8334 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 13.6665 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 15.1458 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 10.2423 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3676 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.4206 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.0519 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0779 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.4382 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0789 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -9.4218 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9248 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.2978 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 26.6020 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 26.6020 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.5740 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.2791 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 16.1548 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 61.3785 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.8024 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.0451 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 14.6883 -> Clearly above the moving-average trend level.

## TAILWINDS

### Berkshire Hathaway (BRK.A) Looks Fairly Valued As It Raises Yen Debt
- Summary: Berkshire Hathaway (BRK.A) Looks Fairly Valued As It Raises Yen Debt
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQVkY4QUtya1pnMThjUnd0SGxRMXMzNUw3cVh6N1VKb05TRWdqU0ZFTUE4OHJqMlp4ZlpxZ196NHIzVERZT3ZLSUtHTS1uWDR3VVpXbV9VYVZHMEZvNndUelYzMVZUR09mVGp2Slk2WGhSYjIwYm9EcXc3a29aWF9sZENQaklwb1V2cWl0YlAyM1ZBT3V0WklDUV9DSjBGcndNV0E?oc=5>

### I'm Raising My Fair Value Estimate for Berkshire Hathaway Stock. Here's What I Think It's Worth.
- Summary: Analyst raises Berkshire Hathaway fair value estimate, suggesting potential upside for investors.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxQWHRsZlZodkt5dFpjZzVZaXhVUGxmMXE4S3FuZXlIOTlsUDhRMTVQbGxPd3M3c1FHQ2VIR285dVFyR3hrcktkUVcxQzY2V2dSQ0VKQWlTUHYtSzRWMlI2TGpEN2xMRjN5SFFfWEVmNGFMeUhqRlVWd3pIanBycmVtZy16aHJyakZ0WXlIRVg1dENZemJyUnRBXzJnZVo1aVlCdENXalhfQWVZeFg1dF9XYWhZd2NjWlNNMnpNdzdWdl94NkpNY0l5WjBmSHlVYVNQdWtj?oc=5>

### 41.6% of Berkshire Hathaway's $358 Billion Portfolio Is Parked in 3 Artificial Intelligence (AI) Stocks
- Summary: Portfolio heavily weighted in three AI stocks, indicating exposure to AI sector.
- Date: 2026-11-22 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxQOHZwendMTjFORVBNdGZ1VEVHeXZWVWtSRjVTT0JfVVpLeWRBS0YtTnptTEJzRjFfR3FUS1VMd1NhVGZ6ZUc4WlNUUTBpQ2lvRnE5QmVzTDdvMHd4OFY2VXJKc1Qtem4zclRQTmQxdmZNamNQYmNaT3R4VzJENTJuTFJ4ZU85akxHWGtmSWJUcWxVNnJ0ck5sVGY1MmN4T19SNmh3WUh0ZzNuTWYzbFZvY19EeVNyZjFBNEItbURWcjVOQ1YtMjJGd29YUWE?oc=5>

### As Tech Stocks Crash, Is Berkshire Hathaway a Safe-Haven Investment?
- Summary: Berkshire may serve as a safe-haven amid tech selloff, suggesting potential upside.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQRnRuQlV0eEVKcnljTFlyNkRyRlVzWmRvUGpuSURNZjJ1ZnhqclJxNkY3QjlnQVhfU3U2YXZYZ2xqNHRSQWtVNC1fZU4wX0tqMHZ2aHBwWl9FaTZiNVJ6STduSWwtc2lzY0dBWU51cjZGN0VPYjlYWXB3UEJkNWFSdW0td2Y3VUxaTmpqeDdRNG53RHdIUWo3aTFMT3NBUFVYREw0?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Warren Buffett’s Successor, Greg Abel, Has Invested Nearly 47% of Berkshire Hathaway’s $360 Billion Stock Portfolio in Just 3 Stocks (and None Are AI Hyperscalers)
- Summary: Greg Abel concentrated portfolio in three stocks, excluding AI hyperscalers.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPam9lcUIybDhzMEFMZkFsU2xZWkdJR19fOGplTllISm95UXQ5SmVkLXlUMnZobzhDMmVWWlAtYjFsVzFfQjhPWGZwSkl2bnFvLTZnajEtYnlyQkFYcFUyYVRDMVoxb25UYmJNdWZnaXlJQzhMdHFZYUl3Z0RxbGxLUWNoeU5fQW85REdLWmMtRmNONnV4MXBWLU8zWVlLV3lF?oc=5>

### The Gates Foundation Trust Sold 2.2 Million Berkshire Shares and Opened a $155 Million Dollar Tree Stake
- Summary: Gates Foundation sold Berkshire shares and opened a Tree stake, indicating a shift in ownership structure.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxPVzEwSTQ1X1RDcWxieG1jMl8yWGU0RnVxUjZPMEoyQVhoNkE1NWxCR0JtVlRhbzVxb3NBYVpLeXltelBSa2V5M1BFTUY2SV9KYzZIVERWR3J4VnZNUTFCYzMzWUVFekF6bmxNWVpBQjFIRzVreDJWb0Jrc1VEazYwNjNVaDV4Q2FGUVBHTVZNNVRiRjJKbmxtMUhmQlJVdGdSaEc5YkN3TnNlcy1OTE5laTFjWFZ5RjBLcjFIZU9nSVNqNS1Wc24taE1MNHJ4NC1DZDZvc2lqNXMzcUtkTWlsag?oc=5>

### Berkshire Hathaway Has Sold More Than Half Its Bank of America Shares Since 2024. Is the Stock a Buy, Sell, or Hold 25% Below Its High?
- Summary: Berkshire sold over half its Bank of America shares, reflecting a divestment strategy.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPV0tuNUpjeVM5VXlnanhTZVJmc3E5VTV2VmEyNWNWWnVzbWt3UE9wck9nV1dNdzluelFlY1BlUTBUNTZGcFF3ZlZkVkIyVGJhNHlnXzBQY3FhY0F3UzNaUlJWUDB2bnNTQ1N5X1VqVGJHZDVIOThfZkFKUVhBaUxDVkE3cDBHdEw0T0FNS0wxRjNJTnN5dHl4VlF2OWNzY0E?oc=5>

### Berkshire Hit a Record High While AI Power Stocks Sold Off. Here’s What That Says About Where Energy Money Is Going.
- Summary: Berkshire reached a record high, indicating strong performance and investor confidence.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxPTTcyTC1NTnpFOFJvemRlUmtoa01lOWxoMzFhbzliOWhOMlJCWUpfaXJEelB1dTQ1dEdNbnJ3cm8xZWZ2U2pyQ2Y3QjBhX0h2QVpJdFQySl9NVGg5bFU2M0pmcE5tQmEwR25xekpVazJRQzl0RWJyeVF0dWYyRXhrcGFidmRwamVGcGlfMGJUQURlQXhUQW5YRjBDWUs5TWhMeTVpejBDb010ZkE2Yms2endMYUt4dXlDSmw2bkdjNlUzQV9FZ3drWHZQdkFzWjFDeF84TFpDMDluX0NHSzg5SFpjX1BTdGxkWmJtVA?oc=5>

### Warren Buffett's Successor, Greg Abel, Just Gave Investors a Big Clue as to What's Next for Stocks
- Summary: Greg Abel hints at Berkshire’s future strategy, suggesting potential shifts in investment focus.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOeEZrZDRQWmV6U3lXSE1LbThlYVdhbVNaTlNacjhwczdJTE9xSF9NTVJIRWNmUXQwZXloLTBSN3lkcVBZQ011WmQ5bXZVU2hWeVBWYVJFeXFFOU0zYmlsUlo2NGNUWHljSE1OYWtpRDlzNlRpaGMxS1FWX1hOcHBuNEtEeWVod1dnUUNza1JVeFl6STE5alJ4enJjS0V4Q0pnLVE?oc=5>

### Berkshire Hathaway (BRK.A) Stock May Be 25% Undervalued Following $9.6 Billion Buybacks
- Summary: Berkshire Hathaway’s $9.6B buyback may leave its stock undervalued by 25%.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNVy16ZFVFcVlRS1VEQV9hWG9CempBUEZGYnZXWm9lWV81Qk5YUGtVam02QjJKdUJPX0tGTFFENlJWTnJWOUpndjNOQ0tDSUpaaVlCWUNPQ2RKaHloUjZTQ09LQ2tWQ19GM003SnFsM0o3dmxZNUNIdU5YRUhPNXp4bTctYUpwSGxtNDRQMVFHamxUUExJS3k4dnkxUWJ1Zw?oc=5>

## RISKS

### Berkshire Hathaway: Slightly Too Expensive To Be Worth It (Rating Downgrade) (NYSE:BRK.A)
- Summary: Downgrade suggests Berkshire may be overvalued.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxONzFpZ2xoSzlkazFtUkNhX09sQ1k0T2FwT19GenVaR3dwYi03M0s4Vk9GOG5ZTHpsWkxMMnd2U2Z5TXJtUDMwYmxjWnVUSGJ1YWdLcUZ6bXlxTHdiNFlKRjBHM1htejMtN1c2RVhtRDVlZXBlcFAyM3FIREY4MW1BdWVxQ1EyUFZZUjZiUzF6bjVaaUQ0U0R2c3l5WkwtQQ?oc=5>

### Berkshire Has Owned These 2 Consumer Stocks for Decades. I'd Buy Both Before December and Never Sell.
- Summary: Recommendation to buy Berkshire-held consumer stocks.
- Date: 2026-11-23 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNOXFOWUN6T1R3ekVMRVVNeFZrQnNYSnpWUmRDYWJYZU1OUzhEbTJhZ0JHS29CTzdNZ2h4cXpXOFg1UjRyZnh0ajdUdGYxZVdwUVBEWEx4ckNhMS1uOHpaQXNJXzUzc0JJYWt4Um5aU1l5MTBrWEdHQUYyRnpRbEFObGNaQjl5ZXhLZ1ZLZUgzRUNqbFVaSUU2dVl2SGVZYVU?oc=5>

### Berkshire Hathaway is betting big on 1 beleaguered US market. Is it too late to get in?
- Summary: Bet on a struggling US market introduces potential downside.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxOYnc2NDdPMVc4Qml2NWhDalQ1Q2ZYZjJDN3U3NHVoRXJodFpxbVBRRWdsWDhlN2RSblhnSmVFQ2pDME9wQ0pVUXExQ3JWbzJ5Q0RJeXVVTUdJTS1EYzNNY29kSUtNcXVDeXNNR1JhUXgyMnNCcDFLTkRINnFvVGVPQXdOVWs?oc=5>

### Warren Buffett Expects Berkshire Hathaway (BRKA, BRKB) Stock to Drop About 50% Again Someday. Here's What He Says to Do Then.
- Summary: Buffett predicts a future 50% drop in Berkshire stock, signaling potential downside risk.
- Date: 2026-11-19 | Impact: high | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQV1FWcTNHWTNfd3pnSmZ2MUJYWXpaWm0taXI3TFE5bmRyV041UjVRSUFiYmF6SENLYVV3ZWZiM2pZZ3FISlNUeS13MDhSaWdOVW10M09XVWVJVDllSkFaby1YYm9hZElMM1huZlU1OEJINmc4Z29QZC12Ri1hUThsWmc3TmdueXNoN3dYWlc0TTRHcDMyX1FjVVA1a21jelVzVmJmZU9LTTZwUQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BRK-B** | **16.15** | **0.00** | **-2.04** | **11.20** | **1,226,293,772,288.00 USD** | **13.67** |
| MKL | 13.96 | 1.30 | 8.03 | -11.20 | 23,987,165,184.00 USD | -4.14 |
| FFH.TO | 9.81 | 1.42 | 8.70 | 1.90 | 55,778,762,752.00 CAD | 12.89 |
| L | 15.32 | 1.23 | 8.68 | 1.90 | 22,394,421,248.00 USD | 3.54 |

Peers fetched as_of: 2026-11-24; BRK-B reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-07
- Next expected earnings: 2027-03-01 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-09
- Revenue (latest available single quarter): 105,647,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 22,112,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1067983/000119312526452412/brka-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiogFBVV95cUxQVkY4QUtya1pnMThjUnd0SGxRMXMzNUw3cVh6N1VKb05TRWdqU0ZFTUE4OHJqMlp4ZlpxZ196NHIzVERZT3ZLSUtHTS1uWDR3VVpXbV9VYVZHMEZvNndUelYzMVZUR09mVGp2Slk2WGhSYjIwYm9EcXc3a29aWF9sZENQaklwb1V2cWl0YlAyM1ZBT3V0WklDUV9DSjBGcndNV0E?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQWHRsZlZodkt5dFpjZzVZaXhVUGxmMXE4S3FuZXlIOTlsUDhRMTVQbGxPd3M3c1FHQ2VIR285dVFyR3hrcktkUVcxQzY2V2dSQ0VKQWlTUHYtSzRWMlI2TGpEN2xMRjN5SFFfWEVmNGFMeUhqRlVWd3pIanBycmVtZy16aHJyakZ0WXlIRVg1dENZemJyUnRBXzJnZVo1aVlCdENXalhfQWVZeFg1dF9XYWhZd2NjWlNNMnpNdzdWdl94NkpNY0l5WjBmSHlVYVNQdWtj?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxQOHZwendMTjFORVBNdGZ1VEVHeXZWVWtSRjVTT0JfVVpLeWRBS0YtTnptTEJzRjFfR3FUS1VMd1NhVGZ6ZUc4WlNUUTBpQ2lvRnE5QmVzTDdvMHd4OFY2VXJKc1Qtem4zclRQTmQxdmZNamNQYmNaT3R4VzJENTJuTFJ4ZU85akxHWGtmSWJUcWxVNnJ0ck5sVGY1MmN4T19SNmh3WUh0ZzNuTWYzbFZvY19EeVNyZjFBNEItbURWcjVOQ1YtMjJGd29YUWE?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQRnRuQlV0eEVKcnljTFlyNkRyRlVzWmRvUGpuSURNZjJ1ZnhqclJxNkY3QjlnQVhfU3U2YXZYZ2xqNHRSQWtVNC1fZU4wX0tqMHZ2aHBwWl9FaTZiNVJ6STduSWwtc2lzY0dBWU51cjZGN0VPYjlYWXB3UEJkNWFSdW0td2Y3VUxaTmpqeDdRNG53RHdIUWo3aTFMT3NBUFVYREw0?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPRV92QnRiM0JHYTdTaEJaTnNuNXBLZk9HYmJlLUt4S3JuTmlEY3gyR0ladUdaSzFFT2lzQUh3eWdMdHRHWFpyR0QxSmtnZWdCdklGUzhYLVVXdkgyU1pJQmhDX3VuUDdLT3VPV19YejZOa0JtYTJhTl8wVjI1Ykt5Z0RKT010Ul9uYWZtS3prbDZyTXBaeVZvbk9weTNwWnB4dHkyTC12eGNOOU52TVE?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPam9lcUIybDhzMEFMZkFsU2xZWkdJR19fOGplTllISm95UXQ5SmVkLXlUMnZobzhDMmVWWlAtYjFsVzFfQjhPWGZwSkl2bnFvLTZnajEtYnlyQkFYcFUyYVRDMVoxb25UYmJNdWZnaXlJQzhMdHFZYUl3Z0RxbGxLUWNoeU5fQW85REdLWmMtRmNONnV4MXBWLU8zWVlLV3lF?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxPVzEwSTQ1X1RDcWxieG1jMl8yWGU0RnVxUjZPMEoyQVhoNkE1NWxCR0JtVlRhbzVxb3NBYVpLeXltelBSa2V5M1BFTUY2SV9KYzZIVERWR3J4VnZNUTFCYzMzWUVFekF6bmxNWVpBQjFIRzVreDJWb0Jrc1VEazYwNjNVaDV4Q2FGUVBHTVZNNVRiRjJKbmxtMUhmQlJVdGdSaEc5YkN3TnNlcy1OTE5laTFjWFZ5RjBLcjFIZU9nSVNqNS1Wc24taE1MNHJ4NC1DZDZvc2lqNXMzcUtkTWlsag?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPV0tuNUpjeVM5VXlnanhTZVJmc3E5VTV2VmEyNWNWWnVzbWt3UE9wck9nV1dNdzluelFlY1BlUTBUNTZGcFF3ZlZkVkIyVGJhNHlnXzBQY3FhY0F3UzNaUlJWUDB2bnNTQ1N5X1VqVGJHZDVIOThfZkFKUVhBaUxDVkE3cDBHdEw0T0FNS0wxRjNJTnN5dHl4VlF2OWNzY0E?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxPTTcyTC1NTnpFOFJvemRlUmtoa01lOWxoMzFhbzliOWhOMlJCWUpfaXJEelB1dTQ1dEdNbnJ3cm8xZWZ2U2pyQ2Y3QjBhX0h2QVpJdFQySl9NVGg5bFU2M0pmcE5tQmEwR25xekpVazJRQzl0RWJyeVF0dWYyRXhrcGFidmRwamVGcGlfMGJUQURlQXhUQW5YRjBDWUs5TWhMeTVpejBDb010ZkE2Yms2endMYUt4dXlDSmw2bkdjNlUzQV9FZ3drWHZQdkFzWjFDeF84TFpDMDluX0NHSzg5SFpjX1BTdGxkWmJtVA?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOeEZrZDRQWmV6U3lXSE1LbThlYVdhbVNaTlNacjhwczdJTE9xSF9NTVJIRWNmUXQwZXloLTBSN3lkcVBZQ011WmQ5bXZVU2hWeVBWYVJFeXFFOU0zYmlsUlo2NGNUWHljSE1OYWtpRDlzNlRpaGMxS1FWX1hOcHBuNEtEeWVod1dnUUNza1JVeFl6STE5alJ4enJjS0V4Q0pnLVE?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNVy16ZFVFcVlRS1VEQV9hWG9CempBUEZGYnZXWm9lWV81Qk5YUGtVam02QjJKdUJPX0tGTFFENlJWTnJWOUpndjNOQ0tDSUpaaVlCWUNPQ2RKaHloUjZTQ09LQ2tWQ19GM003SnFsM0o3dmxZNUNIdU5YRUhPNXp4bTctYUpwSGxtNDRQMVFHamxUUExJS3k4dnkxUWJ1Zw?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxONzFpZ2xoSzlkazFtUkNhX09sQ1k0T2FwT19GenVaR3dwYi03M0s4Vk9GOG5ZTHpsWkxMMnd2U2Z5TXJtUDMwYmxjWnVUSGJ1YWdLcUZ6bXlxTHdiNFlKRjBHM1htejMtN1c2RVhtRDVlZXBlcFAyM3FIREY4MW1BdWVxQ1EyUFZZUjZiUzF6bjVaaUQ0U0R2c3l5WkwtQQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNOXFOWUN6T1R3ekVMRVVNeFZrQnNYSnpWUmRDYWJYZU1OUzhEbTJhZ0JHS29CTzdNZ2h4cXpXOFg1UjRyZnh0ajdUdGYxZVdwUVBEWEx4ckNhMS1uOHpaQXNJXzUzc0JJYWt4Um5aU1l5MTBrWEdHQUYyRnpRbEFObGNaQjl5ZXhLZ1ZLZUgzRUNqbFVaSUU2dVl2SGVZYVU?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxOYnc2NDdPMVc4Qml2NWhDalQ1Q2ZYZjJDN3U3NHVoRXJodFpxbVBRRWdsWDhlN2RSblhnSmVFQ2pDME9wQ0pVUXExQ3JWbzJ5Q0RJeXVVTUdJTS1EYzNNY29kSUtNcXVDeXNNR1JhUXgyMnNCcDFLTkRINnFvVGVPQXdOVWs?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQV1FWcTNHWTNfd3pnSmZ2MUJYWXpaWm0taXI3TFE5bmRyV041UjVRSUFiYmF6SENLYVV3ZWZiM2pZZ3FISlNUeS13MDhSaWdOVW10M09XVWVJVDllSkFaby1YYm9hZElMM1huZlU1OEJINmc4Z29QZC12Ri1hUThsWmc3TmdueXNoN3dYWlc0TTRHcDMyX1FjVVA1a21jelVzVmJmZU9LTTZwUQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPa1lzNGRJZmZXMG9yOG1XaWVBRXRycW1pTXU5SXE2Z0JBbDVLUXpDQTdoREJSbENSOGFlZGwtck9xMkNzbWpwbXBCZXlXWU5MSDFET1gxM3NxWG5xalA1NUM5T0RhcjFwTWZiSEJyVjN1akZXZzVhem92blQ1X3BFeUo2cUp2N24yNmY0STBNeEVrT2RqcFRidQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
