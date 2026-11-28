# BRK-B Intelligence Report

- ticker: **BRK-B**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/BRK-B/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BRK-B/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:17:21.436517+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 1, 'ai': 15, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **12** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/BRK-B** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **8**; {'directional_claim_without_event_type': 7, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 6 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 41.67%; oldest publication 2026-11-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 580.7900 |
| Return 1D (%) | 0.2537 |
| Return 1W (%) | 1.8930 |
| Return 1M (%) | 6.9615 |
| Return YTD (%) | 15.5456 |
| Return 1Y (%) | 13.6064 |
| Annualized volatility (%) | 15.1664 |
| Beta vs SPY | 0.0767 |
| Max drawdown (%) | -9.4218 |
| Sharpe (rf=0) | 0.8902 |
| Downside deviation (rf=0, %) | 10.2627 |
| Sortino (rf=0) | 1.3155 |
| Historical VaR 95% (1D, %) | 1.4212 |
| Historical ES 95% (1D, %) | 2.0519 |
| Correlation vs SPY | 0.0760 |
| Tracking error vs SPY (%) | 20.5195 |
| P/E (trailing) | 16.25 |
| P/B | 0.00 |
| EV/EBITDA | -2.04 |
| Revenue growth (%) | 11.20 |
| Forward P/E (estimate) | 25.45 |
| Gross margin (%) | 26.60 |
| Operating margin (%) | 26.60 |
| Return on equity (%) | 10.57 |
| Free cash flow yield (%) | 4.25 |
| MA50 | 541.8436 |
| Close vs MA50 (%) | 7.1878 |
| MA200 | 504.0849 |
| Close vs MA200 (%) | 15.2167 |
| RSI (14, Wilder) | 63.6377 |
| MACD (12,26) | 10.0205 |
| MACD signal (9) | 12.4433 |
| MACD histogram | -2.4228 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BRK-B': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 580.7900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.2537 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.8930 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 6.9615 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 15.5456 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 13.6064 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 15.1664 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 10.2627 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3155 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.4212 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.0519 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0760 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.5195 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0767 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -9.4218 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8902 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.4547 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 26.6020 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 26.6020 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.5740 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.2527 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 16.2550 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 63.6377 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.4228 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.1878 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 15.2167 -> Clearly above the moving-average trend level.

## TAILWINDS

### Berkshire Hathaway (BRK.A) Looks Fairly Valued As It Raises Yen Debt
- Summary: Berkshire Hathaway (BRK.A) Looks Fairly Valued As It Raises Yen Debt
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQVkY4QUtya1pnMThjUnd0SGxRMXMzNUw3cVh6N1VKb05TRWdqU0ZFTUE4OHJqMlp4ZlpxZ196NHIzVERZT3ZLSUtHTS1uWDR3VVpXbV9VYVZHMEZvNndUelYzMVZUR09mVGp2Slk2WGhSYjIwYm9EcXc3a29aWF9sZENQaklwb1V2cWl0YlAyM1ZBT3V0WklDUV9DSjBGcndNV0E?oc=5>

### Warren Buffett and Greg Abel Collect Billions From These Untouchable Berkshire Hathaway Dividend Stocks
- Summary: Buffett and Abel benefit from high dividend Berkshire stocks.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQOHVHSFBBV1dzME9KU1o1LWFOaGtkVmhodWRXN2hrTnNNVDdXNmtxTkVfeHQ5N2dJQWJIaGlnaXhrb3llbHAwV2ppc3dJeWQyM08tMWJQVVlFdElZV3BVcDd6Zl9FdUhXUnpNUW5YWXlvM2g5MlJSS2hJZzNnWWdaaUY4M25aNC1XSkRIbjdmbEZQOFVWdFlaZUF3MzV4QQ?oc=5>

### Berkshire Hathaway Beating S&P 500 by 3X: Market Expert Credits Greg Abel - Alphabet (NASDAQ:GOOGL), Berk
- Summary: Berkshire’s returns triple S&P 500, attributed to Greg Abel.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMijgJBVV95cUxNTGFtbWlFemJiRzAwdFdpY3hXLXBlTDYwNUFlZkI4dnd3QWFGRHkzY1dMOW9OQXBzWkxDLUFHOXdGb0ZYYmZuZU4yb1BjTXlpUWNLeXpOSG1hbXlldWFyc1ZrdGpKNEY0RTkzcFpNeUNZcWZzUFpuUVBBSUF1STh3bW94UXFPNFZTVE4tUVVsZkpLdnEyYUFFc3UwbUZERVRCUnZPN0tyZkp1V3FqaWNVQlhoZ2JIU1dWSWoyV1Y5ZkxKVzF6bXEtaWpEMFhEUlh6VjFkTlJWc25BT3RwejJ2anM2MVUtT0xsZE1RV1Q5Nlo5ek1vVzJtYmM3WTRxdWN1ZG9VOC1DaGhram8xcUE?oc=5>

### Even Without Warren Buffett as CEO, Berkshire Hathaway Is Outperforming the S&P 500, Nasdaq, and Dow by the Widest Margin Since 2022. History Says This Is What Happens Next.
- Summary: Berkshire continues strong performance post-Buffett.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuwJBVV95cUxPZ292dWJ4c1JyNWJFQ3BOUG00eE1NOWNTSkNOU0J3OWFLZlZqQXVCeE9qek9lTTBGdU42UUNMY0FGUDVlOFFqMFhkcnVLMVBWa05KQXJ5cjBVWXVRRVVKLWNKcWlySE02ZFZaWHVMU3Q0QW1OazdjcldxSmlmMWkwNVY3SUhRU1V6aUgwMElDMHRjSGVWbzVmWS1kT1VySmtzeUYxRUlKZG40Yklpc0psalN1MTNINnk1Y2hPUGUwSThTSlhSeXliMTB3bm0wZDBXSHJZcDVwNUx1ZFRRalJRTldrN0REZkpJVGVXT0Q4Rnk0Q3FSV0NaN0RlSXhQdVhVS19TQnNEeDNwRUNnTHBCeWN0N3d6M3A3Qjh4NTh4SV9rMkNTSUpKQk9tLWFIa1BwMGQ4YkNpQ1BMUVU?oc=5>

### Berkshire Gains 15% YTD, Outperforms Industry: Time to Buy the Stock?
- Summary: Berkshire Hathaway’s year‑to‑date performance outpaces the industry, indicating strong market momentum.
- Date: 2026-11-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOalk1YXFCRzloSmRpTzAwYVpheVI0RTlZVV9MaTdmT2w0LW1zSmpPajJ1T0dyTUpuS3FLdlp1UlY4VjFVNFdsTjJ3SmdIU2dMeURBYk03dC1sWHFQOFpIakZwakxYSHF2TDFKLXFBYWR3eWQxRzlQQ0dDTGs0QkZlak4xN21ORjZ2WTI5UnBCYmh3a2xaTTA3QXo5NENxdXNy?oc=5>

### Warren Buffett's Successor, Greg Abel, Has 47% of Berkshire Hathaway's $346 Billion Portfolio Invested in 3 Proven Winners
- Summary: Greg Abel’s 47% allocation to proven winners signals strong portfolio performance.
- Date: 2026-11-27 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5gFBVV95cUxOMzhDTnlmeVJhWHZzR0RIeFF5RmtrSHZEOGgzVEhQTVJhNzhyd014MjhrT1NrSWI0NkJ1UFJpX1ZWSHZGV3ZYNXJ4bzdUa1lPTkxZa2EzQ05yMS0tai1MRDhNaG5rUGotRW1KWkFmeFI1cjhYVG5wamJoX2YtTUgzcWpjRF95Q1ZpN0lIeHBQQXdkN2otUTM3NjlFUm4xeTFUenNubXZQSS1fUksxcjZXb0p6LUtqM0lmRl9hSkxhY1ZzcGMtRk95azNPNmZhd3R4aXcwajlsY2hsMjFfTXc2eTRNQXdQdw?oc=5>

### Warren Buffett’s Record Cash Pile Is Sending Investors a Message About AI Stocks
- Summary: Buffett’s large cash pile indicates confidence in AI investments.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPYjlhZUN6ZFNZd2dzTHZyaHUzQmVCazRSNE5rVUstVEN4SEQ1eFBibERzSG1zV19xdzBEVGZvVGd4R1hyaG9UQktwdGxCU0FYdHZpODROXzVWQTJJZVVTQVZZb244WF95V3psdG1pNF9WU2hqRmtVNzZfaVhWZWJMc09CbDN3WWd3T3NROXYyMDF6R3ZIdXZ4U1V5T2hhQndQdGR4R250NEFXa2V0eUJIa3I0YklESnBPSHN4RHo5bw?oc=5>

### Apple Is Now 25% of Berkshire Hathaway's Stock Portfolio. Here's What Holding Every Share Tells Investors.
- Summary: Apple’s 25% stake highlights significant exposure to the tech giant.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQTGlwRjNCLVc0LW1XMUY3VjVfSW5NSlp2UUx2NFVhN04yMlg5aVg2elF6cG9VbHFmSXU1cWpWd3ZYajhaSFppRzRRTC1pVmdJOTVHZDRPb25lRzhQNlJFU2wyUlIwSG96QzM5RXJ5RmtfYVpxLXltdlM5Vm9xWnNjejFpTlVzQUx0UENUVVI2WktjQkxRTjlQcGlpVENnQQ?oc=5>

## HEADWINDS

### Warren Buffett's 'worst deal,' a $433-million bet on Dexter Shoe, made billions — just not for him
- Summary: Buffett’s $433M Dexter Shoe bet yielded billions for others, not him.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNUVJGUmREZkZwRU1kaklYZzloSFVrMDlVZHlMd04tSExMWUo5TWxFaWE1bGZEcnU5OU9zbGdzM0Fhbk5Nc21oUlVVZzJxRG5OMHdTSDVVcVlhckhDQUVuVmhEamg0NXEyWUNfOHdZU2R3eWFsWkVlN2ZjRFJFLTNBckd1dUhqb2V4dWdZZF9nekt0M0oyT0Vxa29pQQ?oc=5>

## CATALYSTS

### Is Berkshire Hathaway Stock a Buy if the Fed Keeps Raising Rates?
- Summary: Questions Berkshire’s attractiveness amid potential Fed rate hikes.
- Date: 2026-11-25 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPTHZLVUVOT3BTR0lpekxMbTl5c3FzM3Z2X0lCXzhWLUx3YkJfNG5IY2hXdnJOaHhYVHQwbU5rYkoxQkdiX3M0UlF2Mnp5OE1OQUY4bUpzT3BUTDJlazNfallwcjhlQ185dlRpbHRGTHFtV0QzS3pEWWFIbE1fRGgyUEtUOUw4M2xzakpVYllCYWpTYlNtWEdpYThhUTdLRDUwMzIyMmhfVWJfOVU?oc=5>

### Is Berkshire Hathaway (BRK.B) Reasonable After A Record Cash Pile?
- Summary: Evaluates Berkshire’s valuation after accumulating record cash reserves.
- Date: 2026-11-26 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNYlRfZmNoXzktQmp2YXlvdzN6SU9BRzB2d3pZR3ZoT2JVZ2ZpVkVaTDJuZk53UTZ2T2QzWUktVHdIMzVQUS0xbXJvQ0l5WFhJRGJjRW5lTHdOclVXXzh3VHNpcDhYVGQzMjU0U0ljb1RfclFzb0VyZzJYbGQxTXdiSnNoM0JVLWN1cVJHaUdyWXByZTg0N3BRZlpPc2hRcm5vSFE?oc=5>

### Warren Buffett's Successor, Greg Abel, Has Quietly Purchased 3 Stocks Since the Start of the Fourth Quarter, Including Shares of a Legal Monopoly
- Summary: Greg Abel quietly bought three stocks, including a legal monopoly, for Berkshire Hathaway.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxNQVVWcmRVUEtYa2pDNVpjOUVqTVVNV3lKcGRXbWZ4SjZ2VmZrYS1Za09RdTAzbVdyMVMzRkNnbXVIMUVUanEydXhpTmtUcnFrVzBaVlgzOXdwdWlWWUNkWHNGSHB6ZDJaeURYOUR4dkhBZTFUM1dUUzNiQW9GZ25VbkVQTGtVa0sxUWNoS1RZTlB2and2c0dtb0VzRThacUpBSkZuRGtWRmVzTmI0YTN1bVFkRlFQVjB1NEZxX0xXQldEVnV5ZmVGcF85NjNYVDQzRDB6RlRhYk9EM1VPVGhEd1hn?oc=5>

### Warren Buffett’s Successor, Greg Abel, Has Invested Nearly 47% of Berkshire Hathaway’s $360 Billion Stock Portfolio in Just 3 Stocks (and None Are AI Hyperscalers)
- Summary: Greg Abel concentrated portfolio in three stocks, excluding AI hyperscalers.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPam9lcUIybDhzMEFMZkFsU2xZWkdJR19fOGplTllISm95UXQ5SmVkLXlUMnZobzhDMmVWWlAtYjFsVzFfQjhPWGZwSkl2bnFvLTZnajEtYnlyQkFYcFUyYVRDMVoxb25UYmJNdWZnaXlJQzhMdHFZYUl3Z0RxbGxLUWNoeU5fQW85REdLWmMtRmNONnV4MXBWLU8zWVlLV3lF?oc=5>

### Warren Buffett's Successor, Greg Abel, Just Gave Investors a Big Clue as to What's Next for Stocks
- Summary: Greg Abel hints at Berkshire’s future strategy, suggesting potential shifts in investment focus.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOeEZrZDRQWmV6U3lXSE1LbThlYVdhbVNaTlNacjhwczdJTE9xSF9NTVJIRWNmUXQwZXloLTBSN3lkcVBZQ011WmQ5bXZVU2hWeVBWYVJFeXFFOU0zYmlsUlo2NGNUWHljSE1OYWtpRDlzNlRpaGMxS1FWX1hOcHBuNEtEeWVod1dnUUNza1JVeFl6STE5alJ4enJjS0V4Q0pnLVE?oc=5>

### Berkshire Hathaway’s CEO, Greg Abel, Just Bought $9.6 Billion Worth of 1 of Buffett’s Favorite Stocks
- Summary: CEO Greg Abel purchased $9.6B of a favored stock, increasing Berkshire’s ownership stake.
- Date: 2026-11-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxOOXY0amtEaGU0QzFZSWF4VnIyRDJZdTh4YUZOYWxNeElOeXlERTlNclNNdC1tX1NhbzhValBScTlxejZzdThUbjM1ejdIYUVfRlowUnY0MG9EVk1ZOTJ2cE5qQlpiOE5EVHpVNHBWME1yUS1CaE9DOGs2N2o2MFBjVjlReDZMSzkxeXU3WTN3NUxqMHhLTWFxaElTcFpUZGZIUVBHSHZ4VzA4V1ZuVVduMDNXV1RkNGRsYzhMa1k0U1lZUzdONzh0ZGI4Y3JjZENaWms1OXVLVV9aYWhw?oc=5>

### Berkshire Hathaway (BRK.A) Takes $930 Million Equity Stake In A Private Tech Company
- Summary: Berkshire Hathaway acquires a $930 million equity stake in a private tech firm, expanding its investment portfolio.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOZUZnd19kdk5xbmZ4Wm1keWE3b2stdDBVdnRwN1QwQjZrTVNOMXE2UEQ0UVd5LTZLRDBzU1JRLWdTR3p0MmxtSGJvVC1rSGV5ZHQ2dGRPRUpOU2tZVFF1eXhBT1JFS1N6MUdqVUlhclFjcVBfUnVzNUdMR09IOEZ0dERRU21icWJBb185TmNlQlN6X0hNV2NwMlhjc1F1Zw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BRK-B** | **16.25** | **0.00** | **-2.04** | **11.20** | **1,233,899,487,232.00 USD** | **13.61** |
| MKL | 14.14 | 1.31 | 8.13 | -11.20 | 24,294,000,640.00 USD | -4.60 |
| FFH.TO | 9.84 | 1.42 | 8.72 | 1.90 | 55,948,050,432.00 CAD | 12.60 |
| L | 15.40 | 1.23 | 8.72 | 1.90 | 22,515,757,056.00 USD | 3.08 |

Peers fetched as_of: 2026-11-27; BRK-B reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-07
- Next expected earnings: 2027-03-01 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

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
- https://news.google.com/rss/articles/CBMingFBVV95cUxQOHVHSFBBV1dzME9KU1o1LWFOaGtkVmhodWRXN2hrTnNNVDdXNmtxTkVfeHQ5N2dJQWJIaGlnaXhrb3llbHAwV2ppc3dJeWQyM08tMWJQVVlFdElZV3BVcDd6Zl9FdUhXUnpNUW5YWXlvM2g5MlJSS2hJZzNnWWdaaUY4M25aNC1XSkRIbjdmbEZQOFVWdFlaZUF3MzV4QQ?oc=5
- https://news.google.com/rss/articles/CBMijgJBVV95cUxNTGFtbWlFemJiRzAwdFdpY3hXLXBlTDYwNUFlZkI4dnd3QWFGRHkzY1dMOW9OQXBzWkxDLUFHOXdGb0ZYYmZuZU4yb1BjTXlpUWNLeXpOSG1hbXlldWFyc1ZrdGpKNEY0RTkzcFpNeUNZcWZzUFpuUVBBSUF1STh3bW94UXFPNFZTVE4tUVVsZkpLdnEyYUFFc3UwbUZERVRCUnZPN0tyZkp1V3FqaWNVQlhoZ2JIU1dWSWoyV1Y5ZkxKVzF6bXEtaWpEMFhEUlh6VjFkTlJWc25BT3RwejJ2anM2MVUtT0xsZE1RV1Q5Nlo5ek1vVzJtYmM3WTRxdWN1ZG9VOC1DaGhram8xcUE?oc=5
- https://news.google.com/rss/articles/CBMiuwJBVV95cUxPZ292dWJ4c1JyNWJFQ3BOUG00eE1NOWNTSkNOU0J3OWFLZlZqQXVCeE9qek9lTTBGdU42UUNMY0FGUDVlOFFqMFhkcnVLMVBWa05KQXJ5cjBVWXVRRVVKLWNKcWlySE02ZFZaWHVMU3Q0QW1OazdjcldxSmlmMWkwNVY3SUhRU1V6aUgwMElDMHRjSGVWbzVmWS1kT1VySmtzeUYxRUlKZG40Yklpc0psalN1MTNINnk1Y2hPUGUwSThTSlhSeXliMTB3bm0wZDBXSHJZcDVwNUx1ZFRRalJRTldrN0REZkpJVGVXT0Q4Rnk0Q3FSV0NaN0RlSXhQdVhVS19TQnNEeDNwRUNnTHBCeWN0N3d6M3A3Qjh4NTh4SV9rMkNTSUpKQk9tLWFIa1BwMGQ4YkNpQ1BMUVU?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOalk1YXFCRzloSmRpTzAwYVpheVI0RTlZVV9MaTdmT2w0LW1zSmpPajJ1T0dyTUpuS3FLdlp1UlY4VjFVNFdsTjJ3SmdIU2dMeURBYk03dC1sWHFQOFpIakZwakxYSHF2TDFKLXFBYWR3eWQxRzlQQ0dDTGs0QkZlak4xN21ORjZ2WTI5UnBCYmh3a2xaTTA3QXo5NENxdXNy?oc=5
- https://news.google.com/rss/articles/CBMi5gFBVV95cUxOMzhDTnlmeVJhWHZzR0RIeFF5RmtrSHZEOGgzVEhQTVJhNzhyd014MjhrT1NrSWI0NkJ1UFJpX1ZWSHZGV3ZYNXJ4bzdUa1lPTkxZa2EzQ05yMS0tai1MRDhNaG5rUGotRW1KWkFmeFI1cjhYVG5wamJoX2YtTUgzcWpjRF95Q1ZpN0lIeHBQQXdkN2otUTM3NjlFUm4xeTFUenNubXZQSS1fUksxcjZXb0p6LUtqM0lmRl9hSkxhY1ZzcGMtRk95azNPNmZhd3R4aXcwajlsY2hsMjFfTXc2eTRNQXdQdw?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxPYjlhZUN6ZFNZd2dzTHZyaHUzQmVCazRSNE5rVUstVEN4SEQ1eFBibERzSG1zV19xdzBEVGZvVGd4R1hyaG9UQktwdGxCU0FYdHZpODROXzVWQTJJZVVTQVZZb244WF95V3psdG1pNF9WU2hqRmtVNzZfaVhWZWJMc09CbDN3WWd3T3NROXYyMDF6R3ZIdXZ4U1V5T2hhQndQdGR4R250NEFXa2V0eUJIa3I0YklESnBPSHN4RHo5bw?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQTGlwRjNCLVc0LW1XMUY3VjVfSW5NSlp2UUx2NFVhN04yMlg5aVg2elF6cG9VbHFmSXU1cWpWd3ZYajhaSFppRzRRTC1pVmdJOTVHZDRPb25lRzhQNlJFU2wyUlIwSG96QzM5RXJ5RmtfYVpxLXltdlM5Vm9xWnNjejFpTlVzQUx0UENUVVI2WktjQkxRTjlQcGlpVENnQQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNUVJGUmREZkZwRU1kaklYZzloSFVrMDlVZHlMd04tSExMWUo5TWxFaWE1bGZEcnU5OU9zbGdzM0Fhbk5Nc21oUlVVZzJxRG5OMHdTSDVVcVlhckhDQUVuVmhEamg0NXEyWUNfOHdZU2R3eWFsWkVlN2ZjRFJFLTNBckd1dUhqb2V4dWdZZF9nekt0M0oyT0Vxa29pQQ?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPTHZLVUVOT3BTR0lpekxMbTl5c3FzM3Z2X0lCXzhWLUx3YkJfNG5IY2hXdnJOaHhYVHQwbU5rYkoxQkdiX3M0UlF2Mnp5OE1OQUY4bUpzT3BUTDJlazNfallwcjhlQ185dlRpbHRGTHFtV0QzS3pEWWFIbE1fRGgyUEtUOUw4M2xzakpVYllCYWpTYlNtWEdpYThhUTdLRDUwMzIyMmhfVWJfOVU?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNYlRfZmNoXzktQmp2YXlvdzN6SU9BRzB2d3pZR3ZoT2JVZ2ZpVkVaTDJuZk53UTZ2T2QzWUktVHdIMzVQUS0xbXJvQ0l5WFhJRGJjRW5lTHdOclVXXzh3VHNpcDhYVGQzMjU0U0ljb1RfclFzb0VyZzJYbGQxTXdiSnNoM0JVLWN1cVJHaUdyWXByZTg0N3BRZlpPc2hRcm5vSFE?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxNQVVWcmRVUEtYa2pDNVpjOUVqTVVNV3lKcGRXbWZ4SjZ2VmZrYS1Za09RdTAzbVdyMVMzRkNnbXVIMUVUanEydXhpTmtUcnFrVzBaVlgzOXdwdWlWWUNkWHNGSHB6ZDJaeURYOUR4dkhBZTFUM1dUUzNiQW9GZ25VbkVQTGtVa0sxUWNoS1RZTlB2and2c0dtb0VzRThacUpBSkZuRGtWRmVzTmI0YTN1bVFkRlFQVjB1NEZxX0xXQldEVnV5ZmVGcF85NjNYVDQzRDB6RlRhYk9EM1VPVGhEd1hn?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPam9lcUIybDhzMEFMZkFsU2xZWkdJR19fOGplTllISm95UXQ5SmVkLXlUMnZobzhDMmVWWlAtYjFsVzFfQjhPWGZwSkl2bnFvLTZnajEtYnlyQkFYcFUyYVRDMVoxb25UYmJNdWZnaXlJQzhMdHFZYUl3Z0RxbGxLUWNoeU5fQW85REdLWmMtRmNONnV4MXBWLU8zWVlLV3lF?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOeEZrZDRQWmV6U3lXSE1LbThlYVdhbVNaTlNacjhwczdJTE9xSF9NTVJIRWNmUXQwZXloLTBSN3lkcVBZQ011WmQ5bXZVU2hWeVBWYVJFeXFFOU0zYmlsUlo2NGNUWHljSE1OYWtpRDlzNlRpaGMxS1FWX1hOcHBuNEtEeWVod1dnUUNza1JVeFl6STE5alJ4enJjS0V4Q0pnLVE?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxOOXY0amtEaGU0QzFZSWF4VnIyRDJZdTh4YUZOYWxNeElOeXlERTlNclNNdC1tX1NhbzhValBScTlxejZzdThUbjM1ejdIYUVfRlowUnY0MG9EVk1ZOTJ2cE5qQlpiOE5EVHpVNHBWME1yUS1CaE9DOGs2N2o2MFBjVjlReDZMSzkxeXU3WTN3NUxqMHhLTWFxaElTcFpUZGZIUVBHSHZ4VzA4V1ZuVVduMDNXV1RkNGRsYzhMa1k0U1lZUzdONzh0ZGI4Y3JjZENaWms1OXVLVV9aYWhw?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOZUZnd19kdk5xbmZ4Wm1keWE3b2stdDBVdnRwN1QwQjZrTVNOMXE2UEQ0UVd5LTZLRDBzU1JRLWdTR3p0MmxtSGJvVC1rSGV5ZHQ2dGRPRUpOU2tZVFF1eXhBT1JFS1N6MUdqVUlhclFjcVBfUnVzNUdMR09IOEZ0dERRU21icWJBb185TmNlQlN6X0hNV2NwMlhjc1F1Zw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
