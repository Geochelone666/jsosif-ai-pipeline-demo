# AAPL Intelligence Report

- ticker: **AAPL**
- Report as_of: **2026-11-03**
- Market data as_of: **2026-11-03**
- Quant sources: https://finance.yahoo.com/quote/AAPL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AAPL/key-statistics/
- AI analysis snapshot as_of: **2026-11-03**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-04T04:49:58.325951+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 7, 'ai': 13, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261103T051441Z-8b1c85d8/AAPL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 10 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 331.9000 |
| Return 1D (%) | -1.8976 |
| Return 1W (%) | -4.3791 |
| Return 1M (%) | -0.5364 |
| Return YTD (%) | 22.4172 |
| Return 1Y (%) | 23.8157 |
| Annualized volatility (%) | 24.2270 |
| Beta vs SPY | 0.5685 |
| Max drawdown (%) | -13.7985 |
| Sharpe (rf=0) | 1.0069 |
| Downside deviation (rf=0, %) | 16.8732 |
| Sortino (rf=0) | 1.4457 |
| Historical VaR 95% (1D, %) | 2.0034 |
| Historical ES 95% (1D, %) | 3.4742 |
| Correlation vs SPY | 0.3003 |
| Tracking error vs SPY (%) | 23.7597 |
| P/E (trailing) | 37.67 |
| P/B | 45.10 |
| EV/EBITDA | 29.53 |
| Revenue growth (%) | 16.40 |
| Forward P/E (estimate) | 31.07 |
| Gross margin (%) | 48.65 |
| Operating margin (%) | 32.62 |
| Return on equity (%) | 148.75 |
| Free cash flow yield (%) | 2.22 |
| MA50 | 334.0514 |
| Close vs MA50 (%) | -0.6440 |
| MA200 | 297.0586 |
| Close vs MA200 (%) | 11.7288 |
| RSI (14, Wilder) | 41.7045 |
| MACD (12,26) | 1.8790 |
| MACD signal (9) | 3.4260 |
| MACD histogram | -1.5470 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AAPL': 274, 'SPY': 274}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 331.9000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.8976 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.3791 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -0.5364 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 22.4172 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 23.8157 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 24.2270 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.8732 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4457 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0034 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3003 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.7597 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5685 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.7985 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0069 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 31.0735 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 48.6530 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 32.6230 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 148.7510 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.2239 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 37.6731 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.7045 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.5470 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.6440 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 11.7288 -> Clearly above the moving-average trend level.

## TAILWINDS

### AAPL Stock Ekes Out Minor Gains After-Hours After Tapering Q4 China Sales Growth Offsets Earnings Beat
- Summary: AAPL Stock Ekes Out Minor Gains After-Hours After Tapering Q4 China Sales Growth Offsets Earnings Beat
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxObzdtN1B3QVIxc1dVNk9Cd2xmZUVPTm1SVDM2TVRpeVNfOUpwRzQxQ091Rkx4WEJlS1NUb3lFVFp4d1BDT1BqRkhJdUpSeTNqQkJoNi1acG1lTnpxV1l6QnhMT1ZsdjBRLUtvajdkTjZabHhXLUFYaGt3QVFWWnZ4ekYzempKcS1mY0Q5S25qTkpnejlCRkZn?oc=5>

### Apple’s (NASDAQ:AAPL) Q3 CY2026 sales beat estimates
- Summary: Apple’s (NASDAQ:AAPL) Q3 CY2026 sales beat estimates
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQSE5CdzZJSUNib0pJNnlFaWpqQjJfUkIxME9lNGdYZmZMWk5aTFotTldPY09Db2lNNEFKSzZqZl93YThIM0VZZjV0aFJaN2lPTDY5UEUyLVNPTlNyeGF6cGFEd05XZkVCRm9zYTNwSEEyazBYOW5veHhHWm9BOGllNkw2XzhPRk5WWEJaS3ZBclJoLXVaLTVV?oc=5>

## HEADWINDS

### Apple (AAPL) Stock Faces Pressure Despite Strong Q4 Earnings and Climate Goals
- Summary: Apple (AAPL) Stock Faces Pressure Despite Strong Q4 Earnings and Climate Goals
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNMUh0UW9DdHJ4YUZBdWNKNjBzeGRfMUgyZ2JFSHY2RnR3eGs1YTJGQWJsd0J2ZDVHaGpBbXhhdzl0c2FpR0R1UnhPd2gwZlVqZjFzVDBRM3ZDOGk0a1dnS0JFV2NYZjI3VWJIMWJZZWpiajNWanpKUC1hWEFObGd3VjF1R2Q1b3V5SzhYVzBHYkZ4bzh6SDBMTGEyclFzYWp0MmpNdURR?oc=5>

### Apple slips even as Q4 results, guidance top estimates on iPhone strength (AAPL:NASDAQ)
- Summary: Apple slips even as Q4 results, guidance top estimates on iPhone strength (AAPL:NASDAQ)
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQWUtsRTlqS3NvM2NITnJMVTY0MjZTVkFzdng4dnRoMjd1RVBIU3RaeVV0TGIxUmYyd2tKNnNsOTZQT3k2cVJHUDYwQ3FnRVNaMkVKbC1MS2dvYlgzY0RUWm4tb05aanpTc044OXJGcGdYZ3JzT0p5dVlJdnhXN0FrTkxUNF9oVXhOZk9EUTRPeHFLZmo0NDJqaEtUaDk?oc=5>

### Should Apple (AAPL) Stock Worry About Ternus’ First Call And Rising Chip Costs?
- Summary: Rising chip costs and Ternus first call may pressure Apple’s margins.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNMXVISmxvelljSS1JeS1CU1Z0QUhWNnk5bzhWdTFZVUxwc0wza1BXWHVkbjU2TGlEYjVDNDZYV05pMURCNlpGT01yUmxMTmtfWWRQMWFNNlRfNEpLMV84WENXcjVETzJZQkRYaFZuM3ozVy1OZEJjcU9qRm9OU3I2akx3dlB3NVhsMmtSSEV5ckpMQTZueDhZc19n?oc=5>

### Stock Market Today, Nov. 2: Apple Stock Slides Ahead of Earnings, but Its Latest Results Tell a Different Story
- Summary: Apple shares fell before earnings, but recent results suggest a different outlook.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPMmVyaDFCbFUzN2owbVpab2hVYmNHTU5MMWVSQkhqV3l2TDFIaE5KaEdYSGJ5N2dTLXphVFBhN1dCQVI5NzRfcFdNZlB3dzJBZ2VmTFVwRGNnUlVHYnM5WEJfT3Juc0pab21qcGpSWXpjSkNGYWM2eGd5U25tTHAybXo4MGdrRFJyWGRIdV9jbE5ZUkE?oc=5>

### Apple (NASDAQ:AAPL) Stock Slides Despite US$114.5 Billion Revenue Beat: What Went Wrong?
- Summary: Apple shares fell after revenue beat, indicating market concerns.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxPVDJEM1V3RE91VEdDRFFTZE9OXy1qVEpHMXlNeWJlbG9oQzNLRFl0cy01MXNXZXM2Z3BwM1FKdnFRNkFUX1NKSlJRR1RCXzdOXzB3X2dETTFPVlNMN0R0NDAzVDZ4UlZDQXhYYWx2R0RGd0V3aU5OSmd4b2tIdkdCMw?oc=5>

### AAPL Stock Tumbles Overnight On Margin Pressure From Surging Memory Prices; MU, SNDK Inch Higher
- Summary: Apple shares fell due to margin pressure from rising memory costs.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQeDNsM1M0anhZM1l0Y3Z1S0RtbHlvZFVNTi1RTEI4THpheTlpYXlESlFQWUtGVU8wc0h4TXdDWVBtMG5keC1aR1ZZT2gtU19Za200NGZnN3NLX1NMaTBrc0xyQ2lOVVJDWVRCcFVJVzhtWi0ybWh1S05naElaYmE0WU5OMENZUTZsMlVLbWV2WlZrV21IYVJJcmFjM291dUp1cGc?oc=5>

### Apple 2027 Growth Outlook Faces Scrutiny — Analysts See iPhone Upside, Flag Services Slowdown And Margin Risks
- Summary: Analysts question Apple’s 2027 outlook, citing services slowdown and margin risks.
- Date: 2026-11-03 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNWW01ZUZ0UlRKbVl5cTRyS2tXUmc2S0Q2ampkSnpGX2NBdGtOdjBycnV3V2pYUWYzZ0Fmel9SNjdYTm9KejVCQlowQk9Gb1RWNmFCZVBfUjNjVGlEaGViNnp1TmVVdlNpVUVVNXlWa0VMN21mVWRseFBaMGtfOEhjMHpTTTZOQXVVdTQ3UEduaVpzOXNMenJVc1dubmM?oc=5>

### Apple Inc. (AAPL) Stock Forecasts
- Summary: General stock forecasts for Apple without specific details.
- Date: 2026-11-03 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxPNnUwaUFXTy01S1FsVnpfUDZIdWd1UWJqTFdHaE0zYm5DWlF2Z05qSTBQS0tiSHNhd2hEMzZDcW1yRERnWWFaVU8zd0FNV0M2WktydmpUbkVBUFRBM1B4TXN2TGI3QnBfNm1TMjZCdlZHSlFBZk9RV2hsekpreFVRS1h1YTlPYkNF?oc=5>

## CATALYSTS

### Apple Posts Fiscal Q4 Beat On Strong iPhone, Services Sales
- Summary: Apple Posts Fiscal Q4 Beat On Strong iPhone, Services Sales
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxORVFkV01YZnRtcVJERHpnS1piZVFreC1kRmNmQV85UWxTekN6UVRtT1hMT3hDRmJiTC0yajF6VUJRaFVibmhTamowNlBqa1R6a0hSTm8wRjdFb3FZdUZvMlhrenF0YmcyUnJIOGc1YTNVNzdMNkVSQkw2LVAtWmp3Y2h0dzVRMmlSX1pB?oc=5>

### Apple’s Biggest Threat Isn’t Android — It’s AAPL's Own Devices, Analyst Says Ahead Of Q4 Earnings
- Summary: Apple’s Biggest Threat Isn’t Android — It’s AAPL's Own Devices, Analyst Says Ahead Of Q4 Earnings
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNTkduelBMSXpnTy1iQXVlbTJfT2ktbjhHejFBYXpwWTN2d2lMeDByRElZaklzc1J1b3c4NG1TQkxqd1ZMMlRRT3Fwc0dyTlQ3Q05KWmdlN3dEei1ESWYtUXdnX2xoTTVjbDJpOWQ5ZnpuU2IzbGFFT2l1NVlRZGwtTmZWVmhYd0tXczYyc2dPcndoUjhPMXc?oc=5>

### Apple to report Q4 earnings Monday, with iPhone 18 sales in the spotlight
- Summary: Apple to report Q4 earnings Monday, with iPhone 18 sales in the spotlight
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxPM0xOOWdDN2pXdGpnZnlHTzliX1ZST05ITXdYZXZ5WVN2WFI1eGYxYlcwVnZvWGFkMWNhcklYaXJYQkN1dlR2OHA4RzZSNDRQNjd2ejd2N0k5UW1QeGk1dVdQbHpjVmZaMWhoamc0Ml83bkZWRTBPc1B6aUVLRUUwVTJpM0JxYWpLYnhkc3Q1SXpwdnZpSkFuWEJrWVlyNzZjOXNOZG5CdHgwaEhReWM3SE9Dd09tT2h4SzFzQk0zTFcxR1BNT2oyRF9NMjU?oc=5>

### How to Play AAPL Stock as Apple Acquires an Agentic AI Startup
- Summary: Apple’s acquisition of an AI startup could boost innovation and revenue.
- Date: 2026-11-02 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQVllhVWNEMTl5cWo2Y2QzaFNRWG5pVmpGak5EUkhubE9ZamhUU09MSXRHcGF6WHQ5ZF9VSkM2Q2FkTmpReko5ZDYySTh0MHc1ZUIwMTBpTUJqd013NDVxRmNjendnTkFiQ3lQUVJfR1V1VTFGeHI4ajlCY05KR3Ayanp1MVJLang1T2VfTGVvYmdKcXJjTDdWRGk0VU1NempydEI0NnppOGdJZw?oc=5>

### Apple's Q4 Earnings Loom: Buy or Sell AAPL Stock Ahead of Results?
- Summary: Apple is preparing for Q4 earnings release, prompting investors to decide on buying or selling.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOMHN2dUpzWHQ5Zzh6ZGVBSWZsSUk5Wnozek5sbmNZQjhWYTVIQlRJZUdBT2xhU2xDZ2Jsb1dIbkkzNWtacTNRTXl6NVpwVENHdHgycTA2YmJsbXFHZmVpSnQxcTl3eVNXY045NUgwSlE4UnpLYzR4QTJOV0JrUGNGelR0TGpPTTlaQmNrVGY3eU03TXExdEtF?oc=5>

### Here’s How Much Traders Expect Apple Stock to Move After Earnings
- Summary: Market analysts predict notable post-earnings price swings for Apple.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNanVpek01ZGphUjh2TnM4dEtxZUVkVVFLYkxrcHRZbXZoWkkySTdGSXZ0aVB5T0d2S3hlQU1VVl9RLS1ncmhkUGc1NmFHX0VXTjhfZFlhTE85YmpfVFRKS0FWTnUtTm9uc1NrdE9FQU45MDI3d0RxaFRydnVPZjk4b3h5cl92eWN2cnNCa1c2eHNvVGo1eFdKQzJTSUU?oc=5>

### Buy Apple Stock (AAPL) After Earnings, Says Bank of America
- Summary: Bank of America recommends buying Apple shares post-earnings, citing positive outlook.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQWG5CZ1FMYVVJRG8wWElvdkZOQnBGZjc4NlczM2Fkamk0WFloUGttdXZrQ1Q0cmNkSjlTV3U5UGdEMmwzSE5ua2o0bFp3TzdBTkNwQnl2aFdrWDR1YmVqel9xdVRDdUZIYkg0Q3djLVRTY0RpUjliWGctRnBJT0hmcW4yRktaNjdVTllaYkZtRQ?oc=5>

## RISKS

### Despite Apple's earnings beat, Wall Street has a big 'concern' about next quarter
- Summary: Investors worry about upcoming quarter despite recent earnings success.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQLVNYel9tZy1lWUhULXUyT0d6ZXlkdS1HNjJ3SkpJVGRMNnh5a1dGLWhnTUlLUDc3YVg3empTcG8wZXNvVEpyV2lvTjNlVmJCMnFfUWZCRUd6WE16aDZJU0RBdkdKenQxaFNJdENtOEFQM2NDWEljZG5zQ0RMbmJ1YWpQemVScjNkbDVnTzJyeC1rV3hoVDJaRUhhNGlWNW1vOFh6Q1Y1R29EQ1duSF93R25LbXp1alVSVGNYUDE5U0FYUQ?oc=5>

### Apple: The Midterms Won’t Save It (NASDAQ:AAPL)
- Summary: Political uncertainty from upcoming midterms could negatively affect Apple’s performance.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTFB6RkNJaloxY2pfNWF6c1djdVBGV2pSUFBfNmdmRk5FNGtYODBRald2T1RjeWdET051NkRwUlB5SDdHU2ZqOWU5M19ZQ19sa1JPaUh6ZEFjZTdFT1p6UXVuTUpqV0NDelBldzFTR0s1aHdlVlJqVDRZOHVnRU4?oc=5>

### Spain's competition watchdog plans to sanction Apple, Amazon (AAPL:NASDAQ)
- Summary: Potential sanctions by Spain’s competition watchdog pose regulatory risk to Apple.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNUUJiRkRuV055QW45Q1pmWEN5MHRyWllIYlVpR2h2UUlNcGpuMWVaZmxnRm1FemVGVFRwX09sMmkzMlFPa2ZoT2t1ODY0LTVMRUNDVWo4R3hFajl4blVhcVd1NlRGTkJpVlRFdXktU3dRZDRJbG9qTFFxUFQ0eFBDV21iSTJmdVdrQm9DMURSZTR6cDBYc3R5TVpUWVo?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AAPL** | **37.67** | **45.10** | **29.53** | **16.40** | **4,843,808,227,328.00 USD** | **23.82** |
| MSFT | 26.47 | 8.22 | 19.15 | 18.80 | 3,868,973,072,384.00 USD | 1.59 |
| GOOGL | 14.62 | 5.22 | 18.04 | 24.70 | 3,442,688,655,360.00 USD | -1.04 |
| SONY | 21.16 | 2.82 | 0.12 | 8.20 | 148,273,676,288.00 USD | -9.16 |

Peers fetched as_of: 2026-11-03; AAPL reuses existing data (market data as_of: 2026-11-03); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-01-28 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 62,900,000,000.00 USD; period 2018-07-01/2018-09-29; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 29,789,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/320193/000032019326000026/aapl-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilwFBVV95cUxObzdtN1B3QVIxc1dVNk9Cd2xmZUVPTm1SVDM2TVRpeVNfOUpwRzQxQ091Rkx4WEJlS1NUb3lFVFp4d1BDT1BqRkhJdUpSeTNqQkJoNi1acG1lTnpxV1l6QnhMT1ZsdjBRLUtvajdkTjZabHhXLUFYaGt3QVFWWnZ4ekYzempKcS1mY0Q5S25qTkpnejlCRkZn?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQSE5CdzZJSUNib0pJNnlFaWpqQjJfUkIxME9lNGdYZmZMWk5aTFotTldPY09Db2lNNEFKSzZqZl93YThIM0VZZjV0aFJaN2lPTDY5UEUyLVNPTlNyeGF6cGFEd05XZkVCRm9zYTNwSEEyazBYOW5veHhHWm9BOGllNkw2XzhPRk5WWEJaS3ZBclJoLXVaLTVV?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNMUh0UW9DdHJ4YUZBdWNKNjBzeGRfMUgyZ2JFSHY2RnR3eGs1YTJGQWJsd0J2ZDVHaGpBbXhhdzl0c2FpR0R1UnhPd2gwZlVqZjFzVDBRM3ZDOGk0a1dnS0JFV2NYZjI3VWJIMWJZZWpiajNWanpKUC1hWEFObGd3VjF1R2Q1b3V5SzhYVzBHYkZ4bzh6SDBMTGEyclFzYWp0MmpNdURR?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQWUtsRTlqS3NvM2NITnJMVTY0MjZTVkFzdng4dnRoMjd1RVBIU3RaeVV0TGIxUmYyd2tKNnNsOTZQT3k2cVJHUDYwQ3FnRVNaMkVKbC1MS2dvYlgzY0RUWm4tb05aanpTc044OXJGcGdYZ3JzT0p5dVlJdnhXN0FrTkxUNF9oVXhOZk9EUTRPeHFLZmo0NDJqaEtUaDk?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNMXVISmxvelljSS1JeS1CU1Z0QUhWNnk5bzhWdTFZVUxwc0wza1BXWHVkbjU2TGlEYjVDNDZYV05pMURCNlpGT01yUmxMTmtfWWRQMWFNNlRfNEpLMV84WENXcjVETzJZQkRYaFZuM3ozVy1OZEJjcU9qRm9OU3I2akx3dlB3NVhsMmtSSEV5ckpMQTZueDhZc19n?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPMmVyaDFCbFUzN2owbVpab2hVYmNHTU5MMWVSQkhqV3l2TDFIaE5KaEdYSGJ5N2dTLXphVFBhN1dCQVI5NzRfcFdNZlB3dzJBZ2VmTFVwRGNnUlVHYnM5WEJfT3Juc0pab21qcGpSWXpjSkNGYWM2eGd5U25tTHAybXo4MGdrRFJyWGRIdV9jbE5ZUkE?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxPVDJEM1V3RE91VEdDRFFTZE9OXy1qVEpHMXlNeWJlbG9oQzNLRFl0cy01MXNXZXM2Z3BwM1FKdnFRNkFUX1NKSlJRR1RCXzdOXzB3X2dETTFPVlNMN0R0NDAzVDZ4UlZDQXhYYWx2R0RGd0V3aU5OSmd4b2tIdkdCMw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQeDNsM1M0anhZM1l0Y3Z1S0RtbHlvZFVNTi1RTEI4THpheTlpYXlESlFQWUtGVU8wc0h4TXdDWVBtMG5keC1aR1ZZT2gtU19Za200NGZnN3NLX1NMaTBrc0xyQ2lOVVJDWVRCcFVJVzhtWi0ybWh1S05naElaYmE0WU5OMENZUTZsMlVLbWV2WlZrV21IYVJJcmFjM291dUp1cGc?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNWW01ZUZ0UlRKbVl5cTRyS2tXUmc2S0Q2ampkSnpGX2NBdGtOdjBycnV3V2pYUWYzZ0Fmel9SNjdYTm9KejVCQlowQk9Gb1RWNmFCZVBfUjNjVGlEaGViNnp1TmVVdlNpVUVVNXlWa0VMN21mVWRseFBaMGtfOEhjMHpTTTZOQXVVdTQ3UEduaVpzOXNMenJVc1dubmM?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxPNnUwaUFXTy01S1FsVnpfUDZIdWd1UWJqTFdHaE0zYm5DWlF2Z05qSTBQS0tiSHNhd2hEMzZDcW1yRERnWWFaVU8zd0FNV0M2WktydmpUbkVBUFRBM1B4TXN2TGI3QnBfNm1TMjZCdlZHSlFBZk9RV2hsekpreFVRS1h1YTlPYkNF?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPcW0tMnhpQk8wdXlHU3VHV1VyalJ2SUlPMTZxenJkSGJBdFc4SHcyNF9GZ2Z5NnBiVTY5TmdTMlNLWFRNeFE3RFZmTEtyUVF6d0ppSzlmQ3dYWWpZMFZSWG14VTVjVl9Uc2hRa2pfdm42X0Rob2U3MGN5dzI0d04xSHNKUzYyeDI1N1E?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxORVFkV01YZnRtcVJERHpnS1piZVFreC1kRmNmQV85UWxTekN6UVRtT1hMT3hDRmJiTC0yajF6VUJRaFVibmhTamowNlBqa1R6a0hSTm8wRjdFb3FZdUZvMlhrenF0YmcyUnJIOGc1YTNVNzdMNkVSQkw2LVAtWmp3Y2h0dzVRMmlSX1pB?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNTkduelBMSXpnTy1iQXVlbTJfT2ktbjhHejFBYXpwWTN2d2lMeDByRElZaklzc1J1b3c4NG1TQkxqd1ZMMlRRT3Fwc0dyTlQ3Q05KWmdlN3dEei1ESWYtUXdnX2xoTTVjbDJpOWQ5ZnpuU2IzbGFFT2l1NVlRZGwtTmZWVmhYd0tXczYyc2dPcndoUjhPMXc?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxPM0xOOWdDN2pXdGpnZnlHTzliX1ZST05ITXdYZXZ5WVN2WFI1eGYxYlcwVnZvWGFkMWNhcklYaXJYQkN1dlR2OHA4RzZSNDRQNjd2ejd2N0k5UW1QeGk1dVdQbHpjVmZaMWhoamc0Ml83bkZWRTBPc1B6aUVLRUUwVTJpM0JxYWpLYnhkc3Q1SXpwdnZpSkFuWEJrWVlyNzZjOXNOZG5CdHgwaEhReWM3SE9Dd09tT2h4SzFzQk0zTFcxR1BNT2oyRF9NMjU?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQVllhVWNEMTl5cWo2Y2QzaFNRWG5pVmpGak5EUkhubE9ZamhUU09MSXRHcGF6WHQ5ZF9VSkM2Q2FkTmpReko5ZDYySTh0MHc1ZUIwMTBpTUJqd013NDVxRmNjendnTkFiQ3lQUVJfR1V1VTFGeHI4ajlCY05KR3Ayanp1MVJLang1T2VfTGVvYmdKcXJjTDdWRGk0VU1NempydEI0NnppOGdJZw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOMHN2dUpzWHQ5Zzh6ZGVBSWZsSUk5Wnozek5sbmNZQjhWYTVIQlRJZUdBT2xhU2xDZ2Jsb1dIbkkzNWtacTNRTXl6NVpwVENHdHgycTA2YmJsbXFHZmVpSnQxcTl3eVNXY045NUgwSlE4UnpLYzR4QTJOV0JrUGNGelR0TGpPTTlaQmNrVGY3eU03TXExdEtF?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNanVpek01ZGphUjh2TnM4dEtxZUVkVVFLYkxrcHRZbXZoWkkySTdGSXZ0aVB5T0d2S3hlQU1VVl9RLS1ncmhkUGc1NmFHX0VXTjhfZFlhTE85YmpfVFRKS0FWTnUtTm9uc1NrdE9FQU45MDI3d0RxaFRydnVPZjk4b3h5cl92eWN2cnNCa1c2eHNvVGo1eFdKQzJTSUU?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQWG5CZ1FMYVVJRG8wWElvdkZOQnBGZjc4NlczM2Fkamk0WFloUGttdXZrQ1Q0cmNkSjlTV3U5UGdEMmwzSE5ua2o0bFp3TzdBTkNwQnl2aFdrWDR1YmVqel9xdVRDdUZIYkg0Q3djLVRTY0RpUjliWGctRnBJT0hmcW4yRktaNjdVTllaYkZtRQ?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQLVNYel9tZy1lWUhULXUyT0d6ZXlkdS1HNjJ3SkpJVGRMNnh5a1dGLWhnTUlLUDc3YVg3empTcG8wZXNvVEpyV2lvTjNlVmJCMnFfUWZCRUd6WE16aDZJU0RBdkdKenQxaFNJdENtOEFQM2NDWEljZG5zQ0RMbmJ1YWpQemVScjNkbDVnTzJyeC1rV3hoVDJaRUhhNGlWNW1vOFh6Q1Y1R29EQ1duSF93R25LbXp1alVSVGNYUDE5U0FYUQ?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTFB6RkNJaloxY2pfNWF6c1djdVBGV2pSUFBfNmdmRk5FNGtYODBRald2T1RjeWdET051NkRwUlB5SDdHU2ZqOWU5M19ZQ19sa1JPaUh6ZEFjZTdFT1p6UXVuTUpqV0NDelBldzFTR0s1aHdlVlJqVDRZOHVnRU4?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNUUJiRkRuV055QW45Q1pmWEN5MHRyWllIYlVpR2h2UUlNcGpuMWVaZmxnRm1FemVGVFRwX09sMmkzMlFPa2ZoT2t1ODY0LTVMRUNDVWo4R3hFajl4blVhcVd1NlRGTkJpVlRFdXktU3dRZDRJbG9qTFFxUFQ0eFBDV21iSTJmdVdrQm9DMURSZTR6cDBYc3R5TVpUWVo?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
