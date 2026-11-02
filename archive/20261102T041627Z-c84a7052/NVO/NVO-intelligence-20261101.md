# NVO Intelligence Report

- ticker: **NVO**
- Report as_of: **2026-11-01**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/NVO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVO/key-statistics/
- AI analysis snapshot as_of: **2026-11-01**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-02T04:27:49.799333+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 17, 'rule': 3, 'ai': 8, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261101T014405Z-e49d1192/NVO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **4**; {'low_uncalibrated_model_confidence': 4}
- RSS source audit (metadata only, not article fact-checking): 17 unique headlines; 12 named publishers; 0 exact duplicates; 17 HTTPS source links; largest publisher share 29.41%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 40.0000 |
| Return 1D (%) | 2.1972 |
| Return 1W (%) | 2.4328 |
| Return 1M (%) | 5.5131 |
| Return YTD (%) | -17.4590 |
| Return 1Y (%) | -16.0734 |
| Annualized volatility (%) | 45.5941 |
| Beta vs SPY | 0.9383 |
| Max drawdown (%) | -43.6699 |
| Sharpe (rf=0) | -0.1534 |
| Downside deviation (rf=0, %) | 34.0079 |
| Sortino (rf=0) | -0.2057 |
| Historical VaR 95% (1D, %) | 3.1060 |
| Historical ES 95% (1D, %) | 7.1341 |
| Correlation vs SPY | 0.2632 |
| Tracking error vs SPY (%) | 43.9938 |
| P/E (trailing) | 9.78 |
| P/B | 5.33 |
| EV/EBITDA | 1.57 |
| Revenue growth (%) | 2.10 |
| Forward P/E (estimate) | 11.63 |
| Gross margin (%) | 81.99 |
| Operating margin (%) | 42.54 |
| Return on equity (%) | 59.81 |
| Free cash flow yield (%) | N/A |
| MA50 | 41.2314 |
| Close vs MA50 (%) | -2.9866 |
| MA200 | 43.3724 |
| Close vs MA200 (%) | -7.7755 |
| RSI (14, Wilder) | 53.9926 |
| MACD (12,26) | -0.3746 |
| MACD signal (9) | -0.6776 |
| MACD histogram | 0.3030 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVO': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 40.0000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.1972 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.4328 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 5.5131 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -17.4590 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -16.0734 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 45.5941 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 34.0079 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.2057 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.1060 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 7.1341 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2632 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 43.9938 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.9383 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.6699 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.1534 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.6294 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.9870 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 42.5400 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 59.8150 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 9.7800 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 53.9926 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.3030 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -2.9866 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -7.7755 -> Clearly below the moving-average trend level.

## TAILWINDS

### Can Novo Nordisk (NYSE:NVO) Trade Below Fair Value On Earnings?
- Summary: Questioning if NVO trades below fair value based on earnings.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOc3ZtQjBQOENCS3Uxb1doRDc5a1l1bTVyRUxuSUN0Y3IxanZHMjJmWVlTTW5oVGR5V3p6YXlKdEc5a1BocUREd25DOHBJTC1jNnRDZGdpbGtzN2xTVmZYdDk4UVNEZXlFSElyTm9PYUJ3UXowV3JCcUlIWV9fWE5PLWx5UHlfZlRDbDBBT1NXcUFIUDVFdWpr?oc=5>

### NVO Stock Price and Chart — NYSE:NVO
- Summary: Provides current stock price and chart for NVO.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMiWEFVX3lxTE9vWUdKazJfWDVVMC1fTVJOd19xY05lc0RtZ0ZqekJENUtIZXdLcWlqSTZXQ3BFa3VFRkV1Q18ycWVOTzVHYjVJYXBGTEZFdU5ZYUtEdi0tQWo?oc=5>

### Novo Nordisk (NVO) Could Be 62% Undervalued On GLP 1 Growth Expectations
- Summary: Suggests NVO may be undervalued due to GLP-1 growth prospects.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxPTE1DMVdvNG0xclNDckRmeF9CR1RJb19ZR1pENE0zSUtKYUt2d2luRU1wOTZVN2cweHAtXzZjNW9RTjg2QkRUTk5OOUlYakJqUFR4eTdCUzJCUGZfZl9IaV9EVGFDZ2FucVo2UzBSOXV6MTNsOEgwUjZPZUNLU3FrNmRFaWp0a3RwZVl1M18ybURUQlQzc0s5TE9HSUZfNHhRZWtfeFJTUjZTMkhPaWd5ME1nZ1JwSy1mQ1NjX19ySi1HaGoxNGVCbmJWdDh1VnNjczNvU1cza2hZNFHSAeABQVVfeXFMTU1vSG50Mk5ERGNSbjRRRTVpZUFKcVJyRUJzY24wX0padmlDVE5wQm0yZnRoQndqMng2T2tNYVdkeVpoZjRUMjc0UjNHemp4WjFIWDlnaVBSaU10WU1rSVF2WkZsMlM5SUh0R2VvNXJmejJBVTExejhzd2w2ekU0R1lqYlpud0V5ZXdsTi0zMVVMSGhObERyaG1HVmRTUXJZdHpZZHpqSVVkc3JNMWFiZllPODlpVGVvSmVkckY5eXZqYmtXQzlfQl9rSW5qcWxZRkhZZXk5Vi1RRmF2ZXN3Uks?oc=5>

### Treasury shares total 1.2% of capital as Novo Nordisk (NVO) buybacks reach DKK 11.2B.
- Summary: NVO completed buybacks totaling DKK 11.2B, increasing treasury shares.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxPeHV1MVhwRnVkNkpKenJyczFpLWZBLUs5LWFKbTVkMFFRQnBlOTRIWE9Ecnc4dG54ajhWd01SbnBiRWpvS3pWazBMeG44NG5hbVc4QXJNYVd0N0VMZHlBOEtsNFJfb1Yybi0zNzJ4b3NaOVlDam5maVo2WHFpOFBsWUQ1enRqaVMyM2VMSjRoLXNWNm5uSkJvYWZwWlo1YTBUU05KYUpRdHQ1V05EQlVzWQ?oc=5>

### Will NVO break higher as buyer support offsets competitive headwinds?
- Summary: Speculates on NVO's potential price rise amid buyer support.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxONUkxTHdEVWhQMGFTVHR1bEYwV0p6cU9ocndaeTNrWlVHUWhmNHVpd1FEbzR4VEpMdEJwOXVmYXFCM21qSEoydEZDNHA2Q1RhRDQ0RDVtS3FpVU1SOEZSekM1cFNTYUlTVngzOS1ENVJieDFQWUVCR1g3eExpbGNPRWFHYWdmYzZ2Q3Jncw?oc=5>

### Moderately bullish activity in Novo Nordisk with shares up 1.27%
- Summary: Shares of Novo Nordisk rose 1.27%, indicating moderate bullish market activity.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxQSEtWMVJLaVY2NWdaZmcxNFVkemwxS1lpYk9RTVFaX1Vwa3B2RzJYUy1WeWpPUHlOcGdtMDNVX1kxUHI1VDVmLXpmcnRMSktaYzZSWUVmZGc4Zl9uSWF4NkNQUmRQX1I3cGx6WHgzdFJGXy1HMHg5UmV0RzVRSDJEN0lKS1kxeG5kUkZVakY2cERuZVVZckhNTml4YXlPUEF1LUFzQ1dfaGl1X1p0NWdzV195UQ?oc=5>

### Cboe data suggests bullish flow in Novo Nordisk with shares up 1.49%
- Summary: Cboe data shows a 1.49% rise in Novo Nordisk shares, reflecting bullish flow.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxQRVd4TnNrTjhYTUZRdlFvbmE1VG40ZWYwWHpjYThITjh1SDNiMFlpdHNyZ0xOcE1CTlpUM0JORVh5YWpMbU43aUNGc1lHZXJGTnJKekNmMVdvQkFpV0tWcFNfOEFZMG81NDFKZXNvNUR1RVJ6Y3BfOHVkTWxjcUhDY2FoN0l5ZW0zcEpkMmVyUzhaRjBrcDRWSVdNcVF3Z25Sd25GdUpvdDd1SlpVSTJhbDJta1RadnNO?oc=5>

## HEADWINDS

### Novo Nordisk (CPSE:NOVO B) Stock Looks Cheap Even With Rival Pressure
- Summary: Novo Nordisk (CPSE:NOVO B) Stock Looks Cheap Even With Rival Pressure
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOd0FrNlVNb2xVTWRmY191SEhMVGJmQWhpOVlfbG11WXFTOTdoUndqd3Fob0l6cEZkSU1oTXdlc3Y0UEo0azF0ZHFwMHRpaXg4NE1WNU5PeWQ4UDhKd2NHOFVYQkZodk1KLUd3OVNGQTEzZlExMnRxemhUVUluNkQ1UWVQMHZRbWxKUTdOUUQwLXhkNG8?oc=5>

## CATALYSTS

### Novo Nordisk Trades at 10 Times Earnings While Buying Back Billions in Stock. Is This the Bottom?
- Summary: Novo Nordisk Trades at 10 Times Earnings While Buying Back Billions in Stock. Is This the Bottom?
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQRkcxLUFGd0VDS2xKVmI4SlZhOHpqT1NjV2VRVGU2ekdvVnVIOWx5cWZLT19HNWdxTXN4Wk11MEVLaVkwN2lVR0tjTXRSNXd5MGxvLVJXb0dPUlhmNHhydDlGSzhvR3lYdzkyYUFiOG9Wb3VndE96R09TVVhySjkyajhBTGNNWHRJLVJxbHA4YmphRHpMT0p5cA?oc=5>

### Novo Nordisk (NYSE: NVO) Has Deployed Over DKK 11 Billion Of Its DKK 15 Billion Buyback With Months Still To Run
- Summary: Novo Nordisk (NYSE: NVO) Has Deployed Over DKK 11 Billion Of Its DKK 15 Billion Buyback With Months Still To Run
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxOc3c4UnZPckFzemgyc0dVOGJxYU1ieUZObkdqTzNrOWZ5MjROMklEcFhuT21fQjFOQmtjam00Wk9ZYkVvcmVMUFJubFNCRUZuMmtlQ01td0h3MW5vZGZPRlFKMUNjTzIyc0NOT3YxZG5hWE44eFFaSFZaRmpDUEd6eVBTcjh3OUpXRWk1NHhnb3NETEEwOHFJb29Pdk93RXA1UXNHYjRCN1hjZFB0MGxENG5mUUFvRkw2S1llc1VYek5oR1RPNnpLRVRyYkFPWVQxV1BDNnBrSldERXpEcFYySEZvZ1VXSXRXaFppQ1pQNA?oc=5>

### Novo Nordisk Vs. Eli Lilly Q3 Preview: I'd (Now) Buy Both, But Lilly Is My Top Pick (NVO)
- Summary: An analyst preview suggests buying both Novo Nordisk and Eli Lilly, with a preference for Lilly, indicating a neutral market view.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOdThxQ3V4b1RqMXktQklBMTg0ZjRMLUxaLWtGcndLT2toU2g2czNoQnJnWWJYV3R6ZjJLR01YSFd3bTVmVTZhVE5tVnpFbjI5RFF2VDJFTlJoWVdmNEdIcmoxRS03VnZBaVVFUUF6TVNTbkhIOExhWF9Ed19mRGFTQ2tORWpBQ2JWNExHQ21yeG80aHZYTU55cmtaU3o1bm9BUGZLTjZsM3JNMEN2Q3hkWnV2cVB3Y3loVVE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVO** | **9.78** | **5.33** | **1.57** | **2.10** | **176,427,401,216.00 USD** | **-16.07** |
| LLY | 46.01 | 31.37 | 28.12 | 38.60 | 1,262,666,776,576.00 USD | 68.91 |
| ROG.SW | N/A | N/A | N/A | N/A | N/A unknown currency | N/A |
| SAN.PA | 23.05 | 1.31 | 7.60 | 15.70 | 95,533,998,080.00 EUR | -4.40 |

Peers fetched as_of: 2026-11-01; NVO reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-01

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

- https://news.google.com/rss/articles/CBMilwFBVV95cUxOc3ZtQjBQOENCS3Uxb1doRDc5a1l1bTVyRUxuSUN0Y3IxanZHMjJmWVlTTW5oVGR5V3p6YXlKdEc5a1BocUREd25DOHBJTC1jNnRDZGdpbGtzN2xTVmZYdDk4UVNEZXlFSElyTm9PYUJ3UXowV3JCcUlIWV9fWE5PLWx5UHlfZlRDbDBBT1NXcUFIUDVFdWpr?oc=5
- https://news.google.com/rss/articles/CBMiWEFVX3lxTE9vWUdKazJfWDVVMC1fTVJOd19xY05lc0RtZ0ZqekJENUtIZXdLcWlqSTZXQ3BFa3VFRkV1Q18ycWVOTzVHYjVJYXBGTEZFdU5ZYUtEdi0tQWo?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxPTE1DMVdvNG0xclNDckRmeF9CR1RJb19ZR1pENE0zSUtKYUt2d2luRU1wOTZVN2cweHAtXzZjNW9RTjg2QkRUTk5OOUlYakJqUFR4eTdCUzJCUGZfZl9IaV9EVGFDZ2FucVo2UzBSOXV6MTNsOEgwUjZPZUNLU3FrNmRFaWp0a3RwZVl1M18ybURUQlQzc0s5TE9HSUZfNHhRZWtfeFJTUjZTMkhPaWd5ME1nZ1JwSy1mQ1NjX19ySi1HaGoxNGVCbmJWdDh1VnNjczNvU1cza2hZNFHSAeABQVVfeXFMTU1vSG50Mk5ERGNSbjRRRTVpZUFKcVJyRUJzY24wX0padmlDVE5wQm0yZnRoQndqMng2T2tNYVdkeVpoZjRUMjc0UjNHemp4WjFIWDlnaVBSaU10WU1rSVF2WkZsMlM5SUh0R2VvNXJmejJBVTExejhzd2w2ekU0R1lqYlpud0V5ZXdsTi0zMVVMSGhObERyaG1HVmRTUXJZdHpZZHpqSVVkc3JNMWFiZllPODlpVGVvSmVkckY5eXZqYmtXQzlfQl9rSW5qcWxZRkhZZXk5Vi1RRmF2ZXN3Uks?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxPeHV1MVhwRnVkNkpKenJyczFpLWZBLUs5LWFKbTVkMFFRQnBlOTRIWE9Ecnc4dG54ajhWd01SbnBiRWpvS3pWazBMeG44NG5hbVc4QXJNYVd0N0VMZHlBOEtsNFJfb1Yybi0zNzJ4b3NaOVlDam5maVo2WHFpOFBsWUQ1enRqaVMyM2VMSjRoLXNWNm5uSkJvYWZwWlo1YTBUU05KYUpRdHQ1V05EQlVzWQ?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxONUkxTHdEVWhQMGFTVHR1bEYwV0p6cU9ocndaeTNrWlVHUWhmNHVpd1FEbzR4VEpMdEJwOXVmYXFCM21qSEoydEZDNHA2Q1RhRDQ0RDVtS3FpVU1SOEZSekM1cFNTYUlTVngzOS1ENVJieDFQWUVCR1g3eExpbGNPRWFHYWdmYzZ2Q3Jncw?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxQSEtWMVJLaVY2NWdaZmcxNFVkemwxS1lpYk9RTVFaX1Vwa3B2RzJYUy1WeWpPUHlOcGdtMDNVX1kxUHI1VDVmLXpmcnRMSktaYzZSWUVmZGc4Zl9uSWF4NkNQUmRQX1I3cGx6WHgzdFJGXy1HMHg5UmV0RzVRSDJEN0lKS1kxeG5kUkZVakY2cERuZVVZckhNTml4YXlPUEF1LUFzQ1dfaGl1X1p0NWdzV195UQ?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxQRVd4TnNrTjhYTUZRdlFvbmE1VG40ZWYwWHpjYThITjh1SDNiMFlpdHNyZ0xOcE1CTlpUM0JORVh5YWpMbU43aUNGc1lHZXJGTnJKekNmMVdvQkFpV0tWcFNfOEFZMG81NDFKZXNvNUR1RVJ6Y3BfOHVkTWxjcUhDY2FoN0l5ZW0zcEpkMmVyUzhaRjBrcDRWSVdNcVF3Z25Sd25GdUpvdDd1SlpVSTJhbDJta1RadnNO?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOd0FrNlVNb2xVTWRmY191SEhMVGJmQWhpOVlfbG11WXFTOTdoUndqd3Fob0l6cEZkSU1oTXdlc3Y0UEo0azF0ZHFwMHRpaXg4NE1WNU5PeWQ4UDhKd2NHOFVYQkZodk1KLUd3OVNGQTEzZlExMnRxemhUVUluNkQ1UWVQMHZRbWxKUTdOUUQwLXhkNG8?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQRkcxLUFGd0VDS2xKVmI4SlZhOHpqT1NjV2VRVGU2ekdvVnVIOWx5cWZLT19HNWdxTXN4Wk11MEVLaVkwN2lVR0tjTXRSNXd5MGxvLVJXb0dPUlhmNHhydDlGSzhvR3lYdzkyYUFiOG9Wb3VndE96R09TVVhySjkyajhBTGNNWHRJLVJxbHA4YmphRHpMT0p5cA?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxOc3c4UnZPckFzemgyc0dVOGJxYU1ieUZObkdqTzNrOWZ5MjROMklEcFhuT21fQjFOQmtjam00Wk9ZYkVvcmVMUFJubFNCRUZuMmtlQ01td0h3MW5vZGZPRlFKMUNjTzIyc0NOT3YxZG5hWE44eFFaSFZaRmpDUEd6eVBTcjh3OUpXRWk1NHhnb3NETEEwOHFJb29Pdk93RXA1UXNHYjRCN1hjZFB0MGxENG5mUUFvRkw2S1llc1VYek5oR1RPNnpLRVRyYkFPWVQxV1BDNnBrSldERXpEcFYySEZvZ1VXSXRXaFppQ1pQNA?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOdThxQ3V4b1RqMXktQklBMTg0ZjRMLUxaLWtGcndLT2toU2g2czNoQnJnWWJYV3R6ZjJLR01YSFd3bTVmVTZhVE5tVnpFbjI5RFF2VDJFTlJoWVdmNEdIcmoxRS03VnZBaVVFUUF6TVNTbkhIOExhWF9Ed19mRGFTQ2tORWpBQ2JWNExHQ21yeG80aHZYTU55cmtaU3o1bm9BUGZLTjZsM3JNMEN2Q3hkWnV2cVB3Y3loVVE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
