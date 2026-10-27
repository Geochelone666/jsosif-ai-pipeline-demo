# CAT Intelligence Report

- ticker: **CAT**
- Report as_of: **2026-10-26**
- Market data as_of: **2026-10-26**
- Quant sources: https://finance.yahoo.com/quote/CAT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CAT/key-statistics/
- AI analysis snapshot as_of: **2026-10-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-27T01:59:30.464937+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 3, 'ai': 16, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261026T005504Z-6368ad31/CAT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'short_term_price_move_in_structural_risks': 2}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 11 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-10-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 692.1300 |
| Return 1D (%) | 0.9863 |
| Return 1W (%) | -4.4109 |
| Return 1M (%) | -15.5559 |
| Return YTD (%) | 21.8454 |
| Return 1Y (%) | 33.5328 |
| Annualized volatility (%) | 40.5951 |
| Beta vs SPY | 1.8501 |
| Max drawdown (%) | -35.3672 |
| Sharpe (rf=0) | 0.8986 |
| Downside deviation (rf=0, %) | 26.5888 |
| Sortino (rf=0) | 1.3720 |
| Historical VaR 95% (1D, %) | 4.0279 |
| Historical ES 95% (1D, %) | 5.1314 |
| Correlation vs SPY | 0.5795 |
| Tracking error vs SPY (%) | 34.8041 |
| P/E (trailing) | 29.79 |
| P/B | 16.40 |
| EV/EBITDA | 21.99 |
| Revenue growth (%) | 24.00 |
| Forward P/E (estimate) | 21.24 |
| Gross margin (%) | 29.71 |
| Operating margin (%) | 22.18 |
| Return on equity (%) | 56.97 |
| Free cash flow yield (%) | 1.59 |
| MA50 | 794.5910 |
| Close vs MA50 (%) | -12.8948 |
| MA200 | 805.6549 |
| Close vs MA200 (%) | -14.0910 |
| RSI (14, Wilder) | 29.3247 |
| MACD (12,26) | -31.0911 |
| MACD signal (9) | -21.8667 |
| MACD histogram | -9.2244 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CAT': 268, 'SPY': 268}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 692.1300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.9863 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.4109 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -15.5559 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 21.8454 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 33.5328 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 40.5951 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.5888 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3720 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.0279 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1314 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5795 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 34.8041 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.8501 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -35.3672 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8986 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.2406 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 29.7130 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 22.1830 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 56.9720 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.5870 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 29.7947 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 29.3247 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -9.2244 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -12.8948 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -14.0910 -> Clearly below the moving-average trend level.

## TAILWINDS

### Bears are Losing Control Over Caterpillar (CAT), Here's Why It's a 'Buy' Now
- Summary: Analysts view current dip as buying opportunity.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxQS195elp0TUR6MkxjdzRZTFRjd1VwZklHNUk0UDF4NXFzY0xWZlNEZnM0Y1dCUXpXSklhdmV4Qi1MLVpSTkEzT3Q1dGJyTW5yRHFZOXg3eU03clhYZjlFN1g3SlJtZUxHT0ZkZ3ZzZlRQOFhRU2NiTTZ2TmU2LWM1OEszSTdRWXQ0S2hsc1JyRXNCRmFjd1BwWm5PTU1TZFF0VFVxVQ?oc=5>

### Caterpillar (CAT) Laps the Stock Market: Here's Why
- Summary: Positive stock performance attributed to strong fundamentals and market sentiment.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPdXd6c1dXUXJFUkdfUEtBbXdMYlkwYkdZTlRSa1R6WDZ3S2dFZDhzYThnV1FVdHZubXZKb1F0RXNuWkgxOFpiaE9NVE04cmRCaU9va3RYR1k3NlJJYVJFc1h6RkFnZmpEZGZ0c2Rrb044UGRzUXlIYXR2YXE1OHEyb1V3dHNsRGVqaHo4dWx0QnlVVm5nbExoNjVDVGItUjA?oc=5>

### Fund Update: 44,390 CATERPILLAR (CAT) shares added to UniSuper Management Pty Ltd portfolio
- Summary: UniSuper added 44,390 CAT shares, indicating institutional confidence.
- Date: 2026-10-26 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxOSmZzNDUxcFNFQ2FqcWcwWG9XQ1lkczFaX0JuNG9SZnU0LTlaTjN2ZXdJSjQ2TlUyeUpEc0F5NHNnem9HVEZRMDIxU3JMRHo3V2tkaHV3OTluTHlwZUtzOVoydGIzMXcyZW9JSUxLYl8tSWVKMjVMUFJZSmJoLUZISzJNa3lhRHVJeXBVTGhleTNVb3R5enpXNXFzS1dwMEs1cjJOaGs3LXptVkJsa2hiSkd1eHRIa2lzUS1XeG5MQi1FcGYwNTVQd1VDR3hHUQ?oc=5>

### Caterpillar Is Quietly Becoming an AI Stock. Here's the Segment Growing 72% That Proves It.
- Summary: Caterpillar’s AI segment grew 72%, indicating strong AI adoption and potential future revenue growth.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxOcGNqdHpUTzEzbFFndGpOSDlCTnJTbmM1MHJsN0tVQ3hMY2hnNktidnZ2Q2hfa19lYlR4ZlhyRHAzTWVpaWxlbVJIZWE0b2ZkQ1YyYTF3WUl1bEVLUGpCbzFndk9qTkZMV25iNlh1a0ExZ3l0Y2lxN3RabzJOelRibVZXNWRMVExp?oc=5>

## HEADWINDS

### Caterpillar Inc (CAT) Stock Down 4.9% but Still Overvalued -- GF Score: 90/100
- Summary: Caterpillar Inc (CAT) Stock Down 4.9% but Still Overvalued -- GF Score: 90/100
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxNMlo2YVcxejRBY1FnRU15Z1o3V1MzenRjUGRpVlpNTmFNLWxfemVtRmcyNUIxcUlndmhYUXFwb2lta0R4eVlvNzN6UVN6UFkwT0Iyel8tNm15RFpsSHFrZHZkUlR3b292YW5XV25xay1ubF80NFpycmxfcUJ2ZzlLU3ViV1NRemgtdXlsalF1dUNabGd5dmczM1EzT2hCbmtTb0JvQmpBQm5SS1FU?oc=5>

### What Has The Market Missed In Caterpillar Stock’s Drop?
- Summary: Highlights factors contributing to recent stock decline.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxQeWhwRUFFUFRFc2FKa0pxNjVpbEo3YmFBSURSd0wwV2pnV2JUYllHQ1NEelhVM21MQ0o5MW5xNmNQRHlSZ1cxYTVwaWw1ejBJZUpMVTVRZURCYjBsZW9adjl0M1FDdXNJTmhpX3JFV3BBYlFZS1l6M3Y5ek1lb3ViZ3BEUkJOYzNEbGUtSWlxbWJoRHM2U1hsUVR5a1pLc1dUSHMzcTNfU3AyQThtOHRiVzBSbw?oc=5>

### How Big Could Caterpillar Stock’s Next Fall Be?
- Summary: Speculates on potential magnitude of future decline.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQellmZ1ZFejhCWHFzUmEtUjlUZTRjZWRxaklWblhWYldqbGlYLTlJV0ROd2w2Nm1YaXU2clp6WjNob25iRmE4dG5PX2U4WlhtTm9vN2lDQkpuOV92R1NuUERlY0U5Y2pBeUFVbHdyTzh6bEJwbEdGeEFiY1RYVldPS09NTVppSjcwek9Ja1QwVmRWWmZRSnpsR2FCUTFaVU9lUjJCS25nNFk?oc=5>

## CATALYSTS

### Caterpillar (CAT) Q3 Earnings Preview: What You Should Know Beyond the Headline Estimates
- Summary: Caterpillar (CAT) Q3 Earnings Preview: What You Should Know Beyond the Headline Estimates
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNUnN0U2NDdGs2MjQwVGduaVZLcWxsT0RJbUpxRHppV2pZVHA0a3FxTmxET1ZQUEpVRkxNY2lfMC1oWVBGYUU5XzJwSGsxZDFBdFJqclFlWjlsdzNXZlg1WjlhLTc4Z05nQ21vRFhkRC1Cek1oSzJ6T1B3a0gwODdqeVpCYzdVcXphX0JOLVRFYVNHX3VXVFBLS25rNVEwcWR3WXc?oc=5>

### Caterpillar (CAT) Reports Next Week: Wall Street Expects Earnings Growth
- Summary: Caterpillar (CAT) Reports Next Week: Wall Street Expects Earnings Growth
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNTWROdHc0S3hGTEFFUmswNDVGMUxadkZ2ZU4yT0tCSXhQU0Z6anc5dkpySWlnbkJPeVVLUlpUUkVlTzVUS2REdFZiTWNTZ0lLSVd3MGFMVGlmZXlManduVzdOUm9BTHZEQmlKaVlma0FLTnNWZUNRU1FjVjJhWTVNZklPVjJTRXZMUlVReFVSNkJGZXAzd1V5M054ZnNxclk?oc=5>

### Will Caterpillar (CAT) Beat Estimates Again in Its Next Earnings Report?
- Summary: Upcoming earnings report may confirm earnings beat expectations.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNdFZSODYwSGZHTTZTaUprVElfRTRzZDJ0dFpfUzluYkl0U1c0WG9HTnk4dWRuSm1OR1FyaXNPd3RvRVJPVGRNNjA0bHlvT3R5MXdpaXhjY2xjemRkOGp3VTNmeng3NXVURG9ldVBTbHN1ZEZQbmI1LWNnV2lQVlc0aFJFZnZvWGk3elZFV1k5TUJZU2VNYVo5NlM3UURQam5kZXFB?oc=5>

### All You Need to Know About Caterpillar (CAT) Rating Upgrade to Buy
- Summary: Caterpillar receives a buy rating upgrade, signaling positive analyst outlook and potential upside for investors.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxNaTdyWjk1dmZBT2Vmeng5UndvTG10YVNpZDBzVjJ2OUtYaW1YbUNpRjZEdHJZVG1YeHV0MkNLSUVZdVBDWTZrOXpFNVlyaGJuNzlrNEdnVkNoc0kwTjBvWV9OWVlkSzd3aVN1LVVhR0Vva0gxaDhmTVdKNlNKQ1QyUlVZbWlrYW51a2JrWg?oc=5>

### Can Caterpillar’s $72B Backlog Save Its Stock From a 10% Slump?
- Summary: Speculation that a large backlog may protect stock from decline.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxPaG1Walo3MGUtb2VDRklGaUVNZVBPXy1TY09iUG9ZNGNJSFIyS1Z1QmtNYjhpckM4NkNFaTk1enlrV25TTFl6VVo0Q0hPR05uY0NtTDBBRkJsQm8xbVJqdFpINm5DeGFFTGpmczJEZVR5MEhRaWREU0lqRlpBem9PS3ZlTE8?oc=5>

### What to Expect From Caterpillar's Next Quarterly Earnings Report
- Summary: Upcoming earnings report may reveal financial performance.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPWTEtdUxJUVJINzRwV05aLXduNWxRdjF3ejl2SXdSQkVsM3RqSWZCeEgwZjdkaGpBb3pRX0x5MzF2eU15Y2laTjdwb093bGhINjZHOG9vdTlVMV9pdUtIQkpTS0hNRHZIdXZZVzRfSDRQTlFaTjE1ejVkVFZCUUhKU0NaWW9OUUFMS09VU0xOTXVMUFRyRHM1TUhkaURwZDJqWjNFbk1tdWZtVjd2?oc=5>

### Form 4 Caterpillar For: 23 October By Investing.com
- Summary: Insider transaction reported, potential market impact.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQR3V5MlpKaWtBVWpuZEt2b25BU3FzblBlbG5VX0ZzR1lMamg1Z1RNMHdoZFdXaHhoNmhiS19HZXhQYlYxUEZyYmJVUlVFd0cxYmZMVXk1MmxUTXRFVlJPQlJyWHFwVnFXVl9vVzRUSjJ6OHcxRzNvYTRZVEVxV3dPSlpqREhvcFpuckYyejdNZGJiMkhENDBva3pR?oc=5>

### Caterpillar Set to Report Q3 Earnings: Buy, Sell or Hold the Stock?
- Summary: Caterpillar will announce Q3 earnings, potentially influencing stock valuation.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQMUFqOFpQTDhPdlFBajh6SDRjQkdiSERCTnhyeEc1LXo4a3BMV3hjaXFtcGtZS01iQVR5YkM3UkZkS2stcjU4ZGh3T1dpdk1wZVFValBuWU44cThnLVFQclQ4VWFrb0d1UGZzbUlBclVRc3djd1A2NjlJaXNlRXhJNzRjaG51aTBrVXNXajdMeDFkWkhjUzdLQmF0cU44QzNF?oc=5>

### Form 4 Caterpillar: Kyle Joseph Epley (CFO) For: 25 September By Investing.com
- Summary: CFO Kyle Epley filed a Form 4, indicating insider trading activity.
- Date: 2026-10-26 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNUGFLUzVFdWVTRGdJdzNBUVYzbnJ1SGs5OVJWRzhIQ0YxdlhkZFBCOXp3UWFtQkNOaE83c1g4UUREdGk5Vk1rbTB5WlhUZDVkbXRyeUhIcG5TWEptS2R6UGJKSndKS1l1b0dnYklJZkFEYldWNzYxU0swS1JsRU5HYnFrZ2JuUThnbGhzQTVGZ0lyQnh3WklvVEE4STMyTkFOQkpBSU1zNktaT0lac3BHaUN5ZHFzM0FzSFE?oc=5>

## RISKS

### Caterpillar Inc Stock (CAT) Moved Down by 3.96% on Oct 22: What Investors Need To Know
- Summary: CAT shares fell 3.96% on Oct 22, reflecting a short‑term market decline.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNUUNnamh6SDVQY0xFTG95UHpNYUw5YlMyRFltQk5kazJ5emRJLUpELUhCdDFWdTQ2VU1DaUV2UzRzMjc0SVUzd2RrVzktdXo1MXNfSUtCSXhKNzZXMl8wR1pGMmVBOHNGRXR0S3hZRmV0RHZvakRWbkxCaWNhNFVhR0hCcWVJNmxpQ3c?oc=5>

### Caterpillar Stocks Move Higher Before Data-Center Backlog Test
- Summary: Stock rises ahead of backlog test, potential volatility.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQdUtqNHNZRXAxNkNDZDlpOFZESXFJbUdnbmQ2bTRvQzEzZXR0Ui1qQXJGMUFpYzJpQ2pxV21FeGJDRV9SemlxOFhidUlTby1xVERqLWJGSndzejRZMFhIa3dvWkVWSXFoeE1SRzBKdmtHSUZ5TWJFeXJXQTVqZFRXUzFJbmhtV3hYV3lObkVfTi1SX3NaOTRqUm9fa0Fpbmo3NkE?oc=5>

### UBS cuts Caterpillar stock price target on valuation concerns By Investing.com
- Summary: UBS lowered price target due to valuation worries.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxQZThrQU1EMkZYUWY3YlA1Rlhkb0RBV3hicHQ1aEs3aXlXX0dJdGFBdGhqUFZxTU9OaG9UX2ZOT3ZxV0g3RFJlNUFrWjNhMzRMd3ZjZm5jZVpWSmlZRXkyWlh3Y2cwNDBuZHhnYzEtTHhYUUhiVnFlVFRsV3M3V2tHRlFJSGFfcEVMNGF6bEo3RXJWZGpWU085MC13S1BIeU1iUUt3RDhTc2gtNmlEU0pfaEYtSE5wVkRVaFZUM016UQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CAT** | **29.79** | **16.40** | **21.99** | **24.00** | **318,154,768,384.00 USD** | **33.53** |
| DE | 35.64 | 6.18 | 26.81 | 4.90 | 172,897,288,192.00 USD | 37.19 |
| CNH | 45.00 | 1.80 | 36.92 | 2.00 | 18,091,786,240.00 USD | 5.37 |
| CMI | 26.68 | 5.59 | 15.40 | 9.40 | 71,878,754,304.00 USD | 25.70 |

Peers fetched as_of: 2026-10-26; CAT reuses existing data (market data as_of: 2026-10-26); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-10-29 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-05
- Revenue (latest available single quarter): 20,543,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 1,141,000,000.00 USD; period 2011-07-01/2011-09-30; fiscal year/reporting period 2011/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/18230/000001823026000046/cat-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMipAFBVV95cUxQS195elp0TUR6MkxjdzRZTFRjd1VwZklHNUk0UDF4NXFzY0xWZlNEZnM0Y1dCUXpXSklhdmV4Qi1MLVpSTkEzT3Q1dGJyTW5yRHFZOXg3eU03clhYZjlFN1g3SlJtZUxHT0ZkZ3ZzZlRQOFhRU2NiTTZ2TmU2LWM1OEszSTdRWXQ0S2hsc1JyRXNCRmFjd1BwWm5PTU1TZFF0VFVxVQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPdXd6c1dXUXJFUkdfUEtBbXdMYlkwYkdZTlRSa1R6WDZ3S2dFZDhzYThnV1FVdHZubXZKb1F0RXNuWkgxOFpiaE9NVE04cmRCaU9va3RYR1k3NlJJYVJFc1h6RkFnZmpEZGZ0c2Rrb044UGRzUXlIYXR2YXE1OHEyb1V3dHNsRGVqaHo4dWx0QnlVVm5nbExoNjVDVGItUjA?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxOSmZzNDUxcFNFQ2FqcWcwWG9XQ1lkczFaX0JuNG9SZnU0LTlaTjN2ZXdJSjQ2TlUyeUpEc0F5NHNnem9HVEZRMDIxU3JMRHo3V2tkaHV3OTluTHlwZUtzOVoydGIzMXcyZW9JSUxLYl8tSWVKMjVMUFJZSmJoLUZISzJNa3lhRHVJeXBVTGhleTNVb3R5enpXNXFzS1dwMEs1cjJOaGs3LXptVkJsa2hiSkd1eHRIa2lzUS1XeG5MQi1FcGYwNTVQd1VDR3hHUQ?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxOcGNqdHpUTzEzbFFndGpOSDlCTnJTbmM1MHJsN0tVQ3hMY2hnNktidnZ2Q2hfa19lYlR4ZlhyRHAzTWVpaWxlbVJIZWE0b2ZkQ1YyYTF3WUl1bEVLUGpCbzFndk9qTkZMV25iNlh1a0ExZ3l0Y2lxN3RabzJOelRibVZXNWRMVExp?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxNMlo2YVcxejRBY1FnRU15Z1o3V1MzenRjUGRpVlpNTmFNLWxfemVtRmcyNUIxcUlndmhYUXFwb2lta0R4eVlvNzN6UVN6UFkwT0Iyel8tNm15RFpsSHFrZHZkUlR3b292YW5XV25xay1ubF80NFpycmxfcUJ2ZzlLU3ViV1NRemgtdXlsalF1dUNabGd5dmczM1EzT2hCbmtTb0JvQmpBQm5SS1FU?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxQeWhwRUFFUFRFc2FKa0pxNjVpbEo3YmFBSURSd0wwV2pnV2JUYllHQ1NEelhVM21MQ0o5MW5xNmNQRHlSZ1cxYTVwaWw1ejBJZUpMVTVRZURCYjBsZW9adjl0M1FDdXNJTmhpX3JFV3BBYlFZS1l6M3Y5ek1lb3ViZ3BEUkJOYzNEbGUtSWlxbWJoRHM2U1hsUVR5a1pLc1dUSHMzcTNfU3AyQThtOHRiVzBSbw?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQellmZ1ZFejhCWHFzUmEtUjlUZTRjZWRxaklWblhWYldqbGlYLTlJV0ROd2w2Nm1YaXU2clp6WjNob25iRmE4dG5PX2U4WlhtTm9vN2lDQkpuOV92R1NuUERlY0U5Y2pBeUFVbHdyTzh6bEJwbEdGeEFiY1RYVldPS09NTVppSjcwek9Ja1QwVmRWWmZRSnpsR2FCUTFaVU9lUjJCS25nNFk?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNUnN0U2NDdGs2MjQwVGduaVZLcWxsT0RJbUpxRHppV2pZVHA0a3FxTmxET1ZQUEpVRkxNY2lfMC1oWVBGYUU5XzJwSGsxZDFBdFJqclFlWjlsdzNXZlg1WjlhLTc4Z05nQ21vRFhkRC1Cek1oSzJ6T1B3a0gwODdqeVpCYzdVcXphX0JOLVRFYVNHX3VXVFBLS25rNVEwcWR3WXc?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNTWROdHc0S3hGTEFFUmswNDVGMUxadkZ2ZU4yT0tCSXhQU0Z6anc5dkpySWlnbkJPeVVLUlpUUkVlTzVUS2REdFZiTWNTZ0lLSVd3MGFMVGlmZXlManduVzdOUm9BTHZEQmlKaVlma0FLTnNWZUNRU1FjVjJhWTVNZklPVjJTRXZMUlVReFVSNkJGZXAzd1V5M054ZnNxclk?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNdFZSODYwSGZHTTZTaUprVElfRTRzZDJ0dFpfUzluYkl0U1c0WG9HTnk4dWRuSm1OR1FyaXNPd3RvRVJPVGRNNjA0bHlvT3R5MXdpaXhjY2xjemRkOGp3VTNmeng3NXVURG9ldVBTbHN1ZEZQbmI1LWNnV2lQVlc0aFJFZnZvWGk3elZFV1k5TUJZU2VNYVo5NlM3UURQam5kZXFB?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNaTdyWjk1dmZBT2Vmeng5UndvTG10YVNpZDBzVjJ2OUtYaW1YbUNpRjZEdHJZVG1YeHV0MkNLSUVZdVBDWTZrOXpFNVlyaGJuNzlrNEdnVkNoc0kwTjBvWV9OWVlkSzd3aVN1LVVhR0Vva0gxaDhmTVdKNlNKQ1QyUlVZbWlrYW51a2JrWg?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxPaG1Walo3MGUtb2VDRklGaUVNZVBPXy1TY09iUG9ZNGNJSFIyS1Z1QmtNYjhpckM4NkNFaTk1enlrV25TTFl6VVo0Q0hPR05uY0NtTDBBRkJsQm8xbVJqdFpINm5DeGFFTGpmczJEZVR5MEhRaWREU0lqRlpBem9PS3ZlTE8?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOLUh6NG9OMTl3Tkl1UFRBTy1SN2k0NFZPcGcyb2FSMGlCVXBVQVhwaGRMZk9vMlR1YTBFSzZXN3hSWmlYel92UDg4ODNCS0JPQzMwdzJrSTB4VmUtQ1B0ODFFU0MxbkFZTG1CeGsyTE5XM3VXY1BRSkhVRlBtRTdmN1ZnbDZFb3FvRFJvaGR2ZnZaU2VWOGthaVFxaWV0YUlJLWVUWXl3?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPWTEtdUxJUVJINzRwV05aLXduNWxRdjF3ejl2SXdSQkVsM3RqSWZCeEgwZjdkaGpBb3pRX0x5MzF2eU15Y2laTjdwb093bGhINjZHOG9vdTlVMV9pdUtIQkpTS0hNRHZIdXZZVzRfSDRQTlFaTjE1ejVkVFZCUUhKU0NaWW9OUUFMS09VU0xOTXVMUFRyRHM1TUhkaURwZDJqWjNFbk1tdWZtVjd2?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQR3V5MlpKaWtBVWpuZEt2b25BU3FzblBlbG5VX0ZzR1lMamg1Z1RNMHdoZFdXaHhoNmhiS19HZXhQYlYxUEZyYmJVUlVFd0cxYmZMVXk1MmxUTXRFVlJPQlJyWHFwVnFXVl9vVzRUSjJ6OHcxRzNvYTRZVEVxV3dPSlpqREhvcFpuckYyejdNZGJiMkhENDBva3pR?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQMUFqOFpQTDhPdlFBajh6SDRjQkdiSERCTnhyeEc1LXo4a3BMV3hjaXFtcGtZS01iQVR5YkM3UkZkS2stcjU4ZGh3T1dpdk1wZVFValBuWU44cThnLVFQclQ4VWFrb0d1UGZzbUlBclVRc3djd1A2NjlJaXNlRXhJNzRjaG51aTBrVXNXajdMeDFkWkhjUzdLQmF0cU44QzNF?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNUGFLUzVFdWVTRGdJdzNBUVYzbnJ1SGs5OVJWRzhIQ0YxdlhkZFBCOXp3UWFtQkNOaE83c1g4UUREdGk5Vk1rbTB5WlhUZDVkbXRyeUhIcG5TWEptS2R6UGJKSndKS1l1b0dnYklJZkFEYldWNzYxU0swS1JsRU5HYnFrZ2JuUThnbGhzQTVGZ0lyQnh3WklvVEE4STMyTkFOQkpBSU1zNktaT0lac3BHaUN5ZHFzM0FzSFE?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNUUNnamh6SDVQY0xFTG95UHpNYUw5YlMyRFltQk5kazJ5emRJLUpELUhCdDFWdTQ2VU1DaUV2UzRzMjc0SVUzd2RrVzktdXo1MXNfSUtCSXhKNzZXMl8wR1pGMmVBOHNGRXR0S3hZRmV0RHZvakRWbkxCaWNhNFVhR0hCcWVJNmxpQ3c?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQdUtqNHNZRXAxNkNDZDlpOFZESXFJbUdnbmQ2bTRvQzEzZXR0Ui1qQXJGMUFpYzJpQ2pxV21FeGJDRV9SemlxOFhidUlTby1xVERqLWJGSndzejRZMFhIa3dvWkVWSXFoeE1SRzBKdmtHSUZ5TWJFeXJXQTVqZFRXUzFJbmhtV3hYV3lObkVfTi1SX3NaOTRqUm9fa0Fpbmo3NkE?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxQZThrQU1EMkZYUWY3YlA1Rlhkb0RBV3hicHQ1aEs3aXlXX0dJdGFBdGhqUFZxTU9OaG9UX2ZOT3ZxV0g3RFJlNUFrWjNhMzRMd3ZjZm5jZVpWSmlZRXkyWlh3Y2cwNDBuZHhnYzEtTHhYUUhiVnFlVFRsV3M3V2tHRlFJSGFfcEVMNGF6bEo3RXJWZGpWU085MC13S1BIeU1iUUt3RDhTc2gtNmlEU0pfaEYtSE5wVkRVaFZUM016UQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
