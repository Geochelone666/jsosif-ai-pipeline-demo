# AAPL Intelligence Report

- ticker: **AAPL**
- Report as_of: **2026-11-04**
- Market data as_of: **2026-11-04**
- Quant sources: https://finance.yahoo.com/quote/AAPL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AAPL/key-statistics/
- AI analysis snapshot as_of: **2026-11-04**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-05T05:23:57.618339+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 7, 'ai': 12, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261104T044411Z-6b13f9ec/AAPL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 14 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 45.83%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 349.5100 |
| Return 1D (%) | 5.3058 |
| Return 1W (%) | 1.6520 |
| Return 1M (%) | 4.7409 |
| Return YTD (%) | 28.9124 |
| Return 1Y (%) | 29.9071 |
| Annualized volatility (%) | 24.7816 |
| Beta vs SPY | 0.6177 |
| Max drawdown (%) | -13.7985 |
| Sharpe (rf=0) | 1.1844 |
| Downside deviation (rf=0, %) | 16.8732 |
| Sortino (rf=0) | 1.7395 |
| Historical VaR 95% (1D, %) | 2.0034 |
| Historical ES 95% (1D, %) | 3.4742 |
| Correlation vs SPY | 0.3200 |
| Tracking error vs SPY (%) | 23.9858 |
| P/E (trailing) | 36.95 |
| P/B | 45.31 |
| EV/EBITDA | 29.75 |
| Revenue growth (%) | 11.70 |
| Forward P/E (estimate) | 32.82 |
| Gross margin (%) | 48.79 |
| Operating margin (%) | 31.13 |
| Return on equity (%) | 142.26 |
| Free cash flow yield (%) | 2.12 |
| MA50 | 334.8436 |
| Close vs MA50 (%) | 4.3801 |
| MA200 | 297.5760 |
| Close vs MA200 (%) | 17.4524 |
| RSI (14, Wilder) | 57.7819 |
| MACD (12,26) | 2.3659 |
| MACD signal (9) | 3.2140 |
| MACD histogram | -0.8481 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AAPL': 275, 'SPY': 275}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 349.5100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 5.3058 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.6520 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 4.7409 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 28.9124 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 29.9071 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 24.7816 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.8732 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.7395 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0034 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3200 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.9858 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6177 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.7985 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1844 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 32.8235 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 48.7860 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 31.1250 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 142.2570 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.1246 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 36.9461 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 57.7819 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.8481 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 4.3801 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 17.4524 -> Clearly above the moving-average trend level.

## TAILWINDS

### Apple stock price today hits record high: Why AAPL market cap surpasses $5 trillion after Democrats win mi
- Summary: Apple stock price today hits record high: Why AAPL market cap surpasses $5 trillion after Democrats win mi
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAJBVV95cUxQT3BuQ2g4NlE3NC14OTV6SUkweDdxU0VrZDRTTkl6aWx2Xzk1MWhaUjFLOHBnRE0xcktGVmVpVkFCakl6QXgtZzhzRDlseHRLZGstRHdoS1Z2SGRDaTgwRVNLMnNIZ1NNa19nWHNhYy1xaU5OX0xKV0VxM1FMaFRWNHFKUlpaZlBvb0RxUk1wZmwwQzhRS0hMRUZfN0t0MnJPLWRvSHA2YjRMcGY4cmFnZVNXWWF2ZUUyMEhjVDAyUnhpTmttVXNZMmt0anlhRDQwa1VtdGFVZHpLaE1GQlVpbU1YNGpycHNaTjhUSERwRFJIMlNWSWsxSXE4SWc3T3dVNGd2VXpTR2hheVpFLUR4MHhnNkNYZ0hmSmdrNlpHaGHSAaYCQVVfeXFMTjFFUW02M1J0QXJoTFpjSXlnZkUzd1Q2dC1ONVd6cWw3dE56RXFtcDJKam5CZjJ2eVNuOGZFeGc3cXhQRWZfQjRSRElFQWdvMzVxYWZab2dKMkdUeUs2aGZyd2VTVlVuMGtlc0FTRUtsVzdoZUs0X0djSWFJRzNvM1BoUkpzN1Q1UUVNMENmTGo5el9BMV9oaG9XRko2UFExbVVQS0xOWjFVVUhud1dzRnU3RU9sMmNoRkU0WlpuMTdmUlU5NmJ0NDdrMTRoWHZHZm5mNzVYb000Z1owY0JyV1ZUM1dSdFFxaXNHYjVjcU0wc0pHY29DTXdXdjFCZnduSVduN2tCTURrME5HYnNxSlk4SUJrRkNCX0JXbm1yUTNVRTQ1QzRn?oc=5>

### AAPL Stock Claims Record Highs As Dems Win Helps Apple’s China and Global Business
- Summary: AAPL Stock Claims Record Highs As Dems Win Helps Apple’s China and Global Business
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPTHpVVzBtem5vOEZTWUZnZ0R3ZmFBMHlqWVkyTVY1RGNobHZYaVk5N0NMd3FDTFk0QURhQ0xJTTdEQ3k1RU5oUV9MZGVwWmVvdV9qdjNIbEtpYk0wa0JpdVFkNW9LNUJ5RUtkaUJjNGg3dnp5dVdrVlVUWU40amVoSGlfelEzb09FQ3FIc0UxdUc3NnJYNWNCdWhZSldoejU1XzBTN2d1SG9IZmZHYURYNmZsTUVERFJUSFBPbmxVeWpfZw?oc=5>

### Apple’s (NASDAQ:AAPL) Q3 CY2026 sales beat estimates
- Summary: Apple’s (NASDAQ:AAPL) Q3 CY2026 sales beat estimates
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQSE5CdzZJSUNib0pJNnlFaWpqQjJfUkIxME9lNGdYZmZMWk5aTFotTldPY09Db2lNNEFKSzZqZl93YThIM0VZZjV0aFJaN2lPTDY5UEUyLVNPTlNyeGF6cGFEd05XZkVCRm9zYTNwSEEyazBYOW5veHhHWm9BOGllNkw2XzhPRk5WWEJaS3ZBclJoLXVaLTVV?oc=5>

### Why the Democrat blue wave could be a good thing for Apple stock
- Summary: Political shift may boost Apple’s market perception, potentially lifting stock value.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNbzZxNU01Z0RMd3lqLXNsQ2o3cEVfZ18xcWhydHlsZHVMY3UtNFliYzBnNEMtdXBnMzhLdENvcGctdXJMV1hYTmtVMlZIM0NVc0l2VWV5M3BLdUtoXy1NVEphRnowV05yQWgwYTZfYTgyZGRBaGlESUF1c3RVMUw1OTBkNG9GdHZFTFBqSEFmQVhTN2kwWFc4X01iZHhRWGY5MWhqMlk1dVhnTkFmWG0wY1hJbVJHMGNpaUNrMl9uMHZoZHZ1b21B?oc=5>

### Why is Apple stock surging today?
- Summary: Short‑term price surge likely driven by market sentiment and recent positive news.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPQWVmMDRBVVE2MFlPWno1MFZxM0M4MzlwTHU5ZS1IaHhxNUVYNTZqU3d3TXczOWo0QlpPTm9iZkgweThyMjdoMGZTQ1k3VmFUN1ZVeklzT25uZ3ZwNFBVbUdzb1lsSVgtd3U3enk3c0xBQzBjMDRpTmxmTnFZZlk0RVUzbi1tZmwtcnVveklLZDgwUUJxU1NOT0RR?oc=5>

### Apple Inc Stock (AAPL) Opened Up by 5.54% on Nov 4: A Full Analysis
- Summary: Day‑to‑day price jump reflects investor optimism and recent earnings expectations.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNaXMxM1oyWXVFcTlwZHJMSDAzVWdCNm5KUkQyYUhsUnpWMnF3WGttaGtZVmJ5Nkc5MVZhSmFTcFZTSXhTRV9sdEtjc3Y3TGwzNWpUVnZRdVZOY1NoZGd1R0dObWl3ZlhIVmxYNVFqWVN5NVd3TTctVVBvXzJwVlpMbDdJSTAwZnVCQ3lB?oc=5>

## HEADWINDS

### Apple (AAPL) Stock Faces Pressure Despite Strong Q4 Earnings and Climate Goals
- Summary: Apple (AAPL) Stock Faces Pressure Despite Strong Q4 Earnings and Climate Goals
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNMUh0UW9DdHJ4YUZBdWNKNjBzeGRfMUgyZ2JFSHY2RnR3eGs1YTJGQWJsd0J2ZDVHaGpBbXhhdzl0c2FpR0R1UnhPd2gwZlVqZjFzVDBRM3ZDOGk0a1dnS0JFV2NYZjI3VWJIMWJZZWpiajNWanpKUC1hWEFObGd3VjF1R2Q1b3V5SzhYVzBHYkZ4bzh6SDBMTGEyclFzYWp0MmpNdURR?oc=5>

### Should Apple (AAPL) Stock Worry About Ternus’ First Call And Rising Chip Costs?
- Summary: Rising chip costs and Ternus first call may pressure Apple’s margins.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNMXVISmxvelljSS1JeS1CU1Z0QUhWNnk5bzhWdTFZVUxwc0wza1BXWHVkbjU2TGlEYjVDNDZYV05pMURCNlpGT01yUmxMTmtfWWRQMWFNNlRfNEpLMV84WENXcjVETzJZQkRYaFZuM3ozVy1OZEJjcU9qRm9OU3I2akx3dlB3NVhsMmtSSEV5ckpMQTZueDhZc19n?oc=5>

### Stock Market Today, Nov. 2: Apple Stock Slides Ahead of Earnings, but Its Latest Results Tell a Different Story
- Summary: Apple shares fell before earnings, but recent results suggest a different outlook.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPMmVyaDFCbFUzN2owbVpab2hVYmNHTU5MMWVSQkhqV3l2TDFIaE5KaEdYSGJ5N2dTLXphVFBhN1dCQVI5NzRfcFdNZlB3dzJBZ2VmTFVwRGNnUlVHYnM5WEJfT3Juc0pab21qcGpSWXpjSkNGYWM2eGd5U25tTHAybXo4MGdrRFJyWGRIdV9jbE5ZUkE?oc=5>

### Apple 2027 Growth Outlook Faces Scrutiny — Analysts See iPhone Upside, Flag Services Slowdown And Margin Risks
- Summary: Analysts question Apple’s 2027 outlook, citing services slowdown and margin risks.
- Date: 2026-11-03 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNWW01ZUZ0UlRKbVl5cTRyS2tXUmc2S0Q2ampkSnpGX2NBdGtOdjBycnV3V2pYUWYzZ0Fmel9SNjdYTm9KejVCQlowQk9Gb1RWNmFCZVBfUjNjVGlEaGViNnp1TmVVdlNpVUVVNXlWa0VMN21mVWRseFBaMGtfOEhjMHpTTTZOQXVVdTQ3UEduaVpzOXNMenJVc1dubmM?oc=5>

## CATALYSTS

### Apple (AAPL) Stock Faces Q4 Earnings Margin Squeeze
- Summary: Apple (AAPL) Stock Faces Q4 Earnings Margin Squeeze
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOdDdteU5mbzM5MUZVUnZKLWJkdUNXX3JKVlhQVXMtRFdhWExJb2s1Q1Y4VDNrMVRZQ1JnYTVfaHpCeEhrZFpWbVQySDZUM3k1V3RtdXJuNmRuVHpxRDFIdWU3VWY5VURSeDZackdpRFZaRHFYb3FnalBHaWRLWUxXcFNMYmRfU3M0bWRGTi1YUG1Pdkxt?oc=5>

### Apple Posts Fiscal Q4 Beat On Strong iPhone, Services Sales
- Summary: Apple Posts Fiscal Q4 Beat On Strong iPhone, Services Sales
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxORVFkV01YZnRtcVJERHpnS1piZVFreC1kRmNmQV85UWxTekN6UVRtT1hMT3hDRmJiTC0yajF6VUJRaFVibmhTamowNlBqa1R6a0hSTm8wRjdFb3FZdUZvMlhrenF0YmcyUnJIOGc1YTNVNzdMNkVSQkw2LVAtWmp3Y2h0dzVRMmlSX1pB?oc=5>

### Apple Earnings Put New CEO John Ternus in Focus
- Summary: Apple Earnings Put New CEO John Ternus in Focus
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOZ19raXctR0QzMVNDanBoa0VPSkdlQmp4Y1RScDl0S0dNQ1ZxWmZwUTcyRGUzbDNTYVZzMkpwVWRlbkVscTNJQ0FjeHB6STN6WnhZZnVmdl9FUFhQaUYtWXJ2NXRrTGhtNUxqQzVTOFNqYXh2NDRSdWtlVDRWUS1KaW1Gd05OcG1UT1BYOGZVRnZDSDZlLVpR?oc=5>

### How to Play AAPL Stock as Apple Acquires an Agentic AI Startup
- Summary: Apple’s acquisition of an AI startup could boost innovation and revenue.
- Date: 2026-11-02 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQVllhVWNEMTl5cWo2Y2QzaFNRWG5pVmpGak5EUkhubE9ZamhUU09MSXRHcGF6WHQ5ZF9VSkM2Q2FkTmpReko5ZDYySTh0MHc1ZUIwMTBpTUJqd013NDVxRmNjendnTkFiQ3lQUVJfR1V1VTFGeHI4ajlCY05KR3Ayanp1MVJLang1T2VfTGVvYmdKcXJjTDdWRGk0VU1NempydEI0NnppOGdJZw?oc=5>

### Buy Apple Stock (AAPL) After Earnings, Says Bank of America
- Summary: Bank of America recommends buying Apple shares post-earnings, citing positive outlook.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQWG5CZ1FMYVVJRG8wWElvdkZOQnBGZjc4NlczM2Fkamk0WFloUGttdXZrQ1Q0cmNkSjlTV3U5UGdEMmwzSE5ua2o0bFp3TzdBTkNwQnl2aFdrWDR1YmVqel9xdVRDdUZIYkg0Q3djLVRTY0RpUjliWGctRnBJT0hmcW4yRktaNjdVTllaYkZtRQ?oc=5>

### Apple's Q4 Earnings Loom: Buy or Sell AAPL Stock Ahead of Results?
- Summary: Apple is preparing for Q4 earnings release, prompting investors to decide on buying or selling.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOMHN2dUpzWHQ5Zzh6ZGVBSWZsSUk5Wnozek5sbmNZQjhWYTVIQlRJZUdBT2xhU2xDZ2Jsb1dIbkkzNWtacTNRTXl6NVpwVENHdHgycTA2YmJsbXFHZmVpSnQxcTl3eVNXY045NUgwSlE4UnpLYzR4QTJOV0JrUGNGelR0TGpPTTlaQmNrVGY3eU03TXExdEtF?oc=5>

### Here’s How Much Traders Expect Apple Stock to Move After Earnings
- Summary: Market analysts predict notable post-earnings price swings for Apple.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNanVpek01ZGphUjh2TnM4dEtxZUVkVVFLYkxrcHRZbXZoWkkySTdGSXZ0aVB5T0d2S3hlQU1VVl9RLS1ncmhkUGc1NmFHX0VXTjhfZFlhTE85YmpfVFRKS0FWTnUtTm9uc1NrdE9FQU45MDI3d0RxaFRydnVPZjk4b3h5cl92eWN2cnNCa1c2eHNvVGo1eFdKQzJTSUU?oc=5>

### Apple reports fourth quarter results
- Summary: Apple announced Q4 earnings, surpassing expectations and raising guidance, boosting investor confidence.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQNl83SFNtSWtQV21ERjhKd3c1ZTFwMEhuMlVXbUhXX19CUXA4U1NTTzhDQlBXTThsVGtvMVVHczN2NjFjbGdLWDhjVF84OGtrMk9VbEYxTzJDM0h0cXNGRkNqRk0xT2VOTE1JQjI2eGNNX21RcDhDdkpGOGFZeDl6aXZrOVJoaGQ4OEZNNHAyTzY2LTB1Y1FCSVc4cWJIanZ2T1k4?oc=5>

## RISKS

### Apple: The Midterms Won’t Save It (NASDAQ:AAPL)
- Summary: Political uncertainty from upcoming midterms could negatively affect Apple’s performance.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTFB6RkNJaloxY2pfNWF6c1djdVBGV2pSUFBfNmdmRk5FNGtYODBRald2T1RjeWdET051NkRwUlB5SDdHU2ZqOWU5M19ZQ19sa1JPaUh6ZEFjZTdFT1p6UXVuTUpqV0NDelBldzFTR0s1aHdlVlJqVDRZOHVnRU4?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AAPL** | **36.95** | **45.31** | **29.75** | **11.70** | **5,079,143,284,736.00 USD** | **29.91** |
| MSFT | 27.19 | 8.77 | 20.40 | 18.80 | 4,127,478,775,808.00 USD | 8.95 |
| GOOGL | 14.62 | 5.39 | 18.63 | 24.70 | 3,552,105,201,664.00 USD | 4.37 |
| SONY | 21.45 | 2.88 | 0.12 | 8.20 | 151,544,004,608.00 USD | -7.02 |

Peers fetched as_of: 2026-11-04; AAPL reuses existing data (market data as_of: 2026-11-04); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-01-28 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-04

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

- https://news.google.com/rss/articles/CBMioAJBVV95cUxQT3BuQ2g4NlE3NC14OTV6SUkweDdxU0VrZDRTTkl6aWx2Xzk1MWhaUjFLOHBnRE0xcktGVmVpVkFCakl6QXgtZzhzRDlseHRLZGstRHdoS1Z2SGRDaTgwRVNLMnNIZ1NNa19nWHNhYy1xaU5OX0xKV0VxM1FMaFRWNHFKUlpaZlBvb0RxUk1wZmwwQzhRS0hMRUZfN0t0MnJPLWRvSHA2YjRMcGY4cmFnZVNXWWF2ZUUyMEhjVDAyUnhpTmttVXNZMmt0anlhRDQwa1VtdGFVZHpLaE1GQlVpbU1YNGpycHNaTjhUSERwRFJIMlNWSWsxSXE4SWc3T3dVNGd2VXpTR2hheVpFLUR4MHhnNkNYZ0hmSmdrNlpHaGHSAaYCQVVfeXFMTjFFUW02M1J0QXJoTFpjSXlnZkUzd1Q2dC1ONVd6cWw3dE56RXFtcDJKam5CZjJ2eVNuOGZFeGc3cXhQRWZfQjRSRElFQWdvMzVxYWZab2dKMkdUeUs2aGZyd2VTVlVuMGtlc0FTRUtsVzdoZUs0X0djSWFJRzNvM1BoUkpzN1Q1UUVNMENmTGo5el9BMV9oaG9XRko2UFExbVVQS0xOWjFVVUhud1dzRnU3RU9sMmNoRkU0WlpuMTdmUlU5NmJ0NDdrMTRoWHZHZm5mNzVYb000Z1owY0JyV1ZUM1dSdFFxaXNHYjVjcU0wc0pHY29DTXdXdjFCZnduSVduN2tCTURrME5HYnNxSlk4SUJrRkNCX0JXbm1yUTNVRTQ1QzRn?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPTHpVVzBtem5vOEZTWUZnZ0R3ZmFBMHlqWVkyTVY1RGNobHZYaVk5N0NMd3FDTFk0QURhQ0xJTTdEQ3k1RU5oUV9MZGVwWmVvdV9qdjNIbEtpYk0wa0JpdVFkNW9LNUJ5RUtkaUJjNGg3dnp5dVdrVlVUWU40amVoSGlfelEzb09FQ3FIc0UxdUc3NnJYNWNCdWhZSldoejU1XzBTN2d1SG9IZmZHYURYNmZsTUVERFJUSFBPbmxVeWpfZw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQSE5CdzZJSUNib0pJNnlFaWpqQjJfUkIxME9lNGdYZmZMWk5aTFotTldPY09Db2lNNEFKSzZqZl93YThIM0VZZjV0aFJaN2lPTDY5UEUyLVNPTlNyeGF6cGFEd05XZkVCRm9zYTNwSEEyazBYOW5veHhHWm9BOGllNkw2XzhPRk5WWEJaS3ZBclJoLXVaLTVV?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNbzZxNU01Z0RMd3lqLXNsQ2o3cEVfZ18xcWhydHlsZHVMY3UtNFliYzBnNEMtdXBnMzhLdENvcGctdXJMV1hYTmtVMlZIM0NVc0l2VWV5M3BLdUtoXy1NVEphRnowV05yQWgwYTZfYTgyZGRBaGlESUF1c3RVMUw1OTBkNG9GdHZFTFBqSEFmQVhTN2kwWFc4X01iZHhRWGY5MWhqMlk1dVhnTkFmWG0wY1hJbVJHMGNpaUNrMl9uMHZoZHZ1b21B?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPQWVmMDRBVVE2MFlPWno1MFZxM0M4MzlwTHU5ZS1IaHhxNUVYNTZqU3d3TXczOWo0QlpPTm9iZkgweThyMjdoMGZTQ1k3VmFUN1ZVeklzT25uZ3ZwNFBVbUdzb1lsSVgtd3U3enk3c0xBQzBjMDRpTmxmTnFZZlk0RVUzbi1tZmwtcnVveklLZDgwUUJxU1NOT0RR?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNaXMxM1oyWXVFcTlwZHJMSDAzVWdCNm5KUkQyYUhsUnpWMnF3WGttaGtZVmJ5Nkc5MVZhSmFTcFZTSXhTRV9sdEtjc3Y3TGwzNWpUVnZRdVZOY1NoZGd1R0dObWl3ZlhIVmxYNVFqWVN5NVd3TTctVVBvXzJwVlpMbDdJSTAwZnVCQ3lB?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNMUh0UW9DdHJ4YUZBdWNKNjBzeGRfMUgyZ2JFSHY2RnR3eGs1YTJGQWJsd0J2ZDVHaGpBbXhhdzl0c2FpR0R1UnhPd2gwZlVqZjFzVDBRM3ZDOGk0a1dnS0JFV2NYZjI3VWJIMWJZZWpiajNWanpKUC1hWEFObGd3VjF1R2Q1b3V5SzhYVzBHYkZ4bzh6SDBMTGEyclFzYWp0MmpNdURR?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNMXVISmxvelljSS1JeS1CU1Z0QUhWNnk5bzhWdTFZVUxwc0wza1BXWHVkbjU2TGlEYjVDNDZYV05pMURCNlpGT01yUmxMTmtfWWRQMWFNNlRfNEpLMV84WENXcjVETzJZQkRYaFZuM3ozVy1OZEJjcU9qRm9OU3I2akx3dlB3NVhsMmtSSEV5ckpMQTZueDhZc19n?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPMmVyaDFCbFUzN2owbVpab2hVYmNHTU5MMWVSQkhqV3l2TDFIaE5KaEdYSGJ5N2dTLXphVFBhN1dCQVI5NzRfcFdNZlB3dzJBZ2VmTFVwRGNnUlVHYnM5WEJfT3Juc0pab21qcGpSWXpjSkNGYWM2eGd5U25tTHAybXo4MGdrRFJyWGRIdV9jbE5ZUkE?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNWW01ZUZ0UlRKbVl5cTRyS2tXUmc2S0Q2ampkSnpGX2NBdGtOdjBycnV3V2pYUWYzZ0Fmel9SNjdYTm9KejVCQlowQk9Gb1RWNmFCZVBfUjNjVGlEaGViNnp1TmVVdlNpVUVVNXlWa0VMN21mVWRseFBaMGtfOEhjMHpTTTZOQXVVdTQ3UEduaVpzOXNMenJVc1dubmM?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOdDdteU5mbzM5MUZVUnZKLWJkdUNXX3JKVlhQVXMtRFdhWExJb2s1Q1Y4VDNrMVRZQ1JnYTVfaHpCeEhrZFpWbVQySDZUM3k1V3RtdXJuNmRuVHpxRDFIdWU3VWY5VURSeDZackdpRFZaRHFYb3FnalBHaWRLWUxXcFNMYmRfU3M0bWRGTi1YUG1Pdkxt?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxORVFkV01YZnRtcVJERHpnS1piZVFreC1kRmNmQV85UWxTekN6UVRtT1hMT3hDRmJiTC0yajF6VUJRaFVibmhTamowNlBqa1R6a0hSTm8wRjdFb3FZdUZvMlhrenF0YmcyUnJIOGc1YTNVNzdMNkVSQkw2LVAtWmp3Y2h0dzVRMmlSX1pB?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOZ19raXctR0QzMVNDanBoa0VPSkdlQmp4Y1RScDl0S0dNQ1ZxWmZwUTcyRGUzbDNTYVZzMkpwVWRlbkVscTNJQ0FjeHB6STN6WnhZZnVmdl9FUFhQaUYtWXJ2NXRrTGhtNUxqQzVTOFNqYXh2NDRSdWtlVDRWUS1KaW1Gd05OcG1UT1BYOGZVRnZDSDZlLVpR?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQVllhVWNEMTl5cWo2Y2QzaFNRWG5pVmpGak5EUkhubE9ZamhUU09MSXRHcGF6WHQ5ZF9VSkM2Q2FkTmpReko5ZDYySTh0MHc1ZUIwMTBpTUJqd013NDVxRmNjendnTkFiQ3lQUVJfR1V1VTFGeHI4ajlCY05KR3Ayanp1MVJLang1T2VfTGVvYmdKcXJjTDdWRGk0VU1NempydEI0NnppOGdJZw?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQWG5CZ1FMYVVJRG8wWElvdkZOQnBGZjc4NlczM2Fkamk0WFloUGttdXZrQ1Q0cmNkSjlTV3U5UGdEMmwzSE5ua2o0bFp3TzdBTkNwQnl2aFdrWDR1YmVqel9xdVRDdUZIYkg0Q3djLVRTY0RpUjliWGctRnBJT0hmcW4yRktaNjdVTllaYkZtRQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOMHN2dUpzWHQ5Zzh6ZGVBSWZsSUk5Wnozek5sbmNZQjhWYTVIQlRJZUdBT2xhU2xDZ2Jsb1dIbkkzNWtacTNRTXl6NVpwVENHdHgycTA2YmJsbXFHZmVpSnQxcTl3eVNXY045NUgwSlE4UnpLYzR4QTJOV0JrUGNGelR0TGpPTTlaQmNrVGY3eU03TXExdEtF?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNanVpek01ZGphUjh2TnM4dEtxZUVkVVFLYkxrcHRZbXZoWkkySTdGSXZ0aVB5T0d2S3hlQU1VVl9RLS1ncmhkUGc1NmFHX0VXTjhfZFlhTE85YmpfVFRKS0FWTnUtTm9uc1NrdE9FQU45MDI3d0RxaFRydnVPZjk4b3h5cl92eWN2cnNCa1c2eHNvVGo1eFdKQzJTSUU?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQNl83SFNtSWtQV21ERjhKd3c1ZTFwMEhuMlVXbUhXX19CUXA4U1NTTzhDQlBXTThsVGtvMVVHczN2NjFjbGdLWDhjVF84OGtrMk9VbEYxTzJDM0h0cXNGRkNqRk0xT2VOTE1JQjI2eGNNX21RcDhDdkpGOGFZeDl6aXZrOVJoaGQ4OEZNNHAyTzY2LTB1Y1FCSVc4cWJIanZ2T1k4?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTFB6RkNJaloxY2pfNWF6c1djdVBGV2pSUFBfNmdmRk5FNGtYODBRald2T1RjeWdET051NkRwUlB5SDdHU2ZqOWU5M19ZQ19sa1JPaUh6ZEFjZTdFT1p6UXVuTUpqV0NDelBldzFTR0s1aHdlVlJqVDRZOHVnRU4?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
