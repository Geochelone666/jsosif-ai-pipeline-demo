# CSCO Intelligence Report

- ticker: **CSCO**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/CSCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CSCO/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:33:01.868687+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 5, 'ai': 17, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261123T053847Z-45053549/CSCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 10 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 96.8000 |
| Return 1D (%) | 6.7961 |
| Return 1W (%) | 2.4122 |
| Return 1M (%) | -9.1080 |
| Return YTD (%) | 27.9918 |
| Return 1Y (%) | 29.5560 |
| Annualized volatility (%) | 37.9419 |
| Beta vs SPY | 1.3022 |
| Max drawdown (%) | -29.7448 |
| Sharpe (rf=0) | 0.8731 |
| Downside deviation (rf=0, %) | 26.4633 |
| Sortino (rf=0) | 1.2518 |
| Historical VaR 95% (1D, %) | 3.2248 |
| Historical ES 95% (1D, %) | 5.6237 |
| Correlation vs SPY | 0.5139 |
| Tracking error vs SPY (%) | 32.8605 |
| P/E (trailing) | 27.50 |
| P/B | 7.38 |
| EV/EBITDA | 19.19 |
| Revenue growth (%) | 24.40 |
| Forward P/E (estimate) | 15.98 |
| Gross margin (%) | 64.07 |
| Operating margin (%) | 27.17 |
| Return on equity (%) | 30.38 |
| Free cash flow yield (%) | 2.73 |
| MA50 | 105.8782 |
| Close vs MA50 (%) | -8.5742 |
| MA200 | 102.1657 |
| Close vs MA200 (%) | -5.2520 |
| RSI (14, Wilder) | 44.3387 |
| MACD (12,26) | -3.5962 |
| MACD signal (9) | -3.3754 |
| MACD histogram | -0.2208 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CSCO': 288, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 96.8000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 6.7961 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.4122 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -9.1080 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 27.9918 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 29.5560 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 37.9419 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.4633 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.2518 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.2248 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.6237 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5139 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.8605 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3022 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -29.7448 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8731 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.9819 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 64.0740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 27.1720 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 30.3800 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.7278 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.5000 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 44.3387 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.2208 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -8.5742 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -5.2520 -> Clearly below the moving-average trend level.

## TAILWINDS

### Cisco Systems (NASDAQ:CSCO) Stock Jumps 6.8% - Here's Why
- Summary: Cisco Systems (NASDAQ:CSCO) Stock Jumps 6.8% - Here's Why
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQaHZ4VHhKWW9SaGUtMjY3elhGSzlrX2ZMUWwwNURmcUJpR0hwVnZaM1ItT1RhR0FiQVBVWW1ubUZJc2k1bHF1SGlmaEJsazNMMGxEWWlPdHN0UnltcTBpRllHTzFOTWdXd2xvUzdobWxNaEljSF9DcFlDcDF6YnhTNDliQ0ktcVpNT3JtNUJjY0xMTU14MHA2WWtFZEhqazdlR1Y3WDFMUmhJdC1PeHU0?oc=5>

### Cisco: Its $22 Billion AI Supply Bet Looks Worth Taking
- Summary: Cisco invests $22B in AI supply chain, signaling strategic expansion.
- Date: 2026-11-19 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPRVVEN2VyeUR1UFJzOXczaW1IQ1dfOTBzWEsyc2YycmZZUTR6YVgtUmw3Q2dZQ3pGNWZhU294VWd1ZnYzV0Mtc180ancyUENfVHhnM1QwZ1BJRkNEZUVkZjhENm9CbGFpY0hhcHRwOWhoYmIzMmpfZzZ5YUpEQjF4REYyNzlBbkxfdzNUV3dUdHFXbm8wRVRtUVJB?oc=5>

### A new Cisco-OpenAI tool can protect systems while teams work on a fix.
- Summary: Cisco launches a new OpenAI-powered security tool to protect systems during fixes.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPMFpXbU5jSk5sYzdFRGhDU2p2X0puVjVxbEpMWVBmVlBETzJSYWs5RmRvMWF2OFpKcEFkQ2QyT0pSMEVnT25JdlNVNkRxNE05MjBoMy00ZURxdlctemo3YWFOSlpKM1ZEdTQ5c3J6d2EzOERrNVlDOXUtb1YyeEd3YUFiOUZjbXd2d2E2N2syR0szV3VYM24xRTdvUk1LQVo0UkNRTHFNOXpfZFhsZkNXU29yajBHQkhhc0lLalY3aw?oc=5>

## HEADWINDS

### Cisco Systems, Inc. (CSCO) Posted Record $17.3 Billion Revenue, but Margins Slipped: Is the Stock Still Worth Buying?
- Summary: Cisco Systems, Inc. (CSCO) Posted Record $17.3 Billion Revenue, but Margins Slipped: Is the Stock Still Worth Buying?
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQazVldGNaeWhMdGxVX3lmZlJjRHh5OE91TFUzUGhzYXJjUDB6aXh4Y0hITjZMREZPTmZ0UmYwRGxzY0VoSlRVWlF2UmVCeHZ2NWlIbEtja3V3RHhNNmtoYlBTcjNQQ3pXQm5zNXdUYnZuY2hGeXNPbHVCUDBDSDEzQTdhbXBSWDRyeHZ6dzl4QlQwNEVES0lQVlZB?oc=5>

### Cisco Stock Fell 15.5% Despite Its Strongest Growth in 15 Years. Is the Dividend Safe?
- Summary: Cisco Stock Fell 15.5% Despite Its Strongest Growth in 15 Years. Is the Dividend Safe?
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxOLW5SV3lqa1B5SE1SMHZhUDhKaWNlaG5fUnZvNk00NHU1eHU4bVdxWXVFZDQ2bmtpOVRwUUp1SXg1dnB4S2h6WFdYWmJxODJLOTFacmtoLXFPam1TUTRCdDlpN0FEcElWS1dHMFFRWUd0NjN3b0JUQ2lXcTh1dmhmcHpLbzlDQWlzX0VZMnRBNVpEY3JCSXlIazVqTzBuWVp4azJ2QXFUSXFtNkRlQzdPdWc0alhIVlpFTGVyNEx4b0JQWHo3NWc?oc=5>

### Cisco insider share sales: Can CSCO avoid deeper losses?
- Summary: Insider share sales may signal declining confidence, potentially impacting stock negatively.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQWUdpdXY2TlhoRDBwTWNzZU9Nb3plYWFHZ1JXSEdhejlUOHVMd0ZVQklBc1p0dHRjT0lpYWdUMWZmc0QwSS1XNFN2eU1ibnpFM2ZTNzhkeS1JbmpiN3dPcTZ6c0x6emtYVlFqNXRHRWZkMGw5ZEJGb0puN1k2RlJySEZmcXlWTExHR1Q4NjNTaw?oc=5>

### Cisco Systems Inc Stock (CSCO) Moved Down by 3.10% on Nov 20: A Full Analysis
- Summary: Stock fell 3.10%, indicating a short-term negative market reaction.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPbVRIOElDNVBrZkR1MHZrcDNvVXIyT0lObnNwcTVQR3Z1dHA3VHFGdVNvLUpGN21pZTJUVDFMMzZiNnJZME9NbTRsU0lBZTdUSHVsYVFOSGZuMFNaWldXenU1cFhRVDUwTjhTYlpzd2hGOHU3STRxUS1wR09jS0wwdkRyYUdqTnlOZllV?oc=5>

## CATALYSTS

### Cisco (CSCO) Stock Gets Fair Value Trim As Analysts Cut Targets After Strong Q1
- Summary: Cisco (CSCO) Stock Gets Fair Value Trim As Analysts Cut Targets After Strong Q1
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOd0psSW1iRElNXzlmeTI0QTZrM1J1UU5QaUJnS1J4NXFMYzhMM2dvb3dxeG5zSHRFTG5IRkhPTklXMy1vM01GaDBRSlRYNjQxM3E2aEZtYXlyTEdRR0x3STNMMUlyQ1A4aWNERVNQTW1RazVaZUc2WFJ2UjY1eVVUanA2U3ZGMXZITlRJOVRNeF9QTzhJaHc?oc=5>

### Cisco Systems, Inc. (CSCO) - What Are Analysts Saying About This Stock?
- Summary: Cisco Systems, Inc. (CSCO) - What Are Analysts Saying About This Stock?
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxPM3ZtdUpuUWJsTHIycGc5Zks1dGpGcjNfbjBjZGNyWEwwRWFseXBXMjg5eXVTNnpNekxrVXJleXpUNHhQWXQxQ2thbGRrbU5lWDZkRG5PZkN5UWJLeDVjcS1iTjk1bk5ZU3lUcHlza0d4VkN5NjVWWWxveGk0NWZ5X3p2Uk1SeHhtTm1GZnBSZHB0MzE4ZEdKTW4yUmJRZW0zRHNjN0I5RThrSVJZbEJFNEh6Y01hOUNfOEFqUXAzZHdEbWhCOW9j?oc=5>

### What Did Cisco’s Quarter Change For Its Stock?
- Summary: Cisco’s latest quarterly results and their impact on the stock price.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPZkpSempEOHAyWU5QVVlKUGw2Zl81RHBKRnBGT3ljMmQ5Q21VazV1azg0ZzdUek5zZHQ0MVZfRkJGVWNzQXpHUkk5dVVZMENON3JuYWJsQ3RDVlVqNS1FeGp1dUprLUFWSnUxd0xDdFg2dUJmZ2tXVU9HS2RyaHJKeEVVTmZULUpoUVlDZzVjNHVNMGVfNTRiOC11OG5sbkhEVzhZODRlMlg?oc=5>

### How Investors May Respond To Cisco Stock After Earnings Beat
- Summary: Earnings beat may boost investor sentiment and drive stock upward.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOMHZiWHc0TlV6cUxOTTNTbDQzdkczcWFEZ2RELUhIaG1vbDhjcFJreXZleXRmc0Q3UHNqbm84SW9pZlIwdmY2Z0xLcUt5RXd2c2RQT3NCREI2RmdmRGthaUJhU3pTd09NZUg0RllpZ3hVNmFGZlRBbVAwZ2ltajRiQ1lYQmFwMmFBSHNqSDl1WmtXbmtmRWZtOUVFNkFiYXM?oc=5>

### Cisco Drops 7% Post Earnings: Should You Buy the Stock on the Dip?
- Summary: Cisco’s earnings miss caused a 7% drop, prompting investors to consider buying at the dip.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOR2gxQW9fU2tUZlVfZ3k0RGw2UF9KWjAwVGVFUFU4c2R1VE5PWERjTkMtNnF6OUNQNjYtQzhsN1RrUFU0OHU1MjJaeS0wYUdIdlY1TmVpajRVZWh1TWhrNG82OWRmeHBaZzg2dEREcGFOc01mVE4tR2ZPUWtGc1dkRmM3dVlJTjNXaHpENFhzUXEzN29SOGdv?oc=5>

### Cisco: Better Earnings, Cheaper Stock (NASDAQ:CSCO)
- Summary: Cisco reports improved earnings and a lower stock price, indicating stronger financial performance and potential upside for investors.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxOQW1JNjZlRklwSUJiX3pwLW13UG5WZF9NbTc3Mlk4dmhTeUNReWlfLWloUFNrbG5GY3ZfczdIZ0tHbUI0VGZ4dGFub252Z3dfMTdGX0ZDQi1LRVVxYW1wdkhlLXRhbzAyMXhsMHVUcXExRWlHbW52N2EyRlQ0OThlOWhB?oc=5>

### Cisco (CSCO) Stock Can Q1 Results Sustain The AI Rebound?
- Summary: Potential Q1 earnings could support AI-driven growth.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxQNzl3YVozazZGRThYdDlEWklreDVRS2hzUnNDcXFDZUpjNUxjbm1adFNaTWtRSWRVYkUtSzFxZ1U0RVFCNnJpZnZQYzhubUZYYnRSNjZYWEVsZjZncm5kQ0xpSDVwWFdoaDNiWl9XUmQ1RTQ4LTJ5bkJFLWRMeUpremluV3Q0TUVVdkhwMkVXd1AyWGRPQVBySHYwTVFyeGxPN01mSTVQSW5FUHlReDFSTllQTFFXTnRXTXhWaFExMNIBxAFBVV95cUxPQWVFV253MkNwaVBQdU96ZVoyTW4zN0NDNUNvWjBjMnJCZTZ4czE4bEc4MWZzbDlNZl9saFNkZllxMXZYUVdNTmpxanFWUzNGeldqNFFmUjEwQXptQlZ0dGQtaHhFRko1ckZmYTF5Q3B1WTNWR3ljU1J5QzBZTGV6ZHZDeURHTGliMDVNbjJqT2gtNnVkeENDVGRMYWcwQTR0NHM2UXM1Ql83TndpVlZmeXFjTGVEd2NYMnQ1V2dDWnFrOXBZ?oc=5>

### AI Revenue Target Could Be A Big Moment For Cisco Stock (CSCO)
- Summary: Cisco announces AI revenue target, potentially boosting investor confidence.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxQMTdVWXJXZVV6SEJjNTl1c3RUNU1KaDBNandHbjNobHVjajR1Z0VOT3B5cUhueFlDdnN2ZklTTTV6QWp0Y3FFazdHZEwyRmV5Wm1kOURvQ2NkY2VWU19ISjB5clA0eEV6YjdHQldlRXBkVXlfbGw5dzF4cjhXZk9EZkxwYjVkMHNZcS1WY2dPTnNZR3A0MF9VVWZHRFd2bl9aNTdpUXNjRnhuOTRRUXp1TVNEbVM2SGZWN21LQnBqRzBodFZVZ0o4?oc=5>

### Cisco Systems Inc Stock (CSCO) Moved Up by 6.44% on Nov 23: Key Drivers Unveiled
- Summary: Cisco shares rose 6.44% on Nov 23, driven by key factors.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOdEUwVkdOckx1ZUhBUVhfc1VpWk1jckhFYmFkc2ZkamNlOTlMdy14ZE8xX1BsN1Z4eENlRHJESFBHckNkd3FDUEVjLUNWUlBOdlJ1M0MxaEVfdWI4bGFCLUM5U2N1cVIxMGNQYUtvcVZneUIzc3BuanE4MmRpeGRVak9BN1NJTzdfcU1B?oc=5>

### Cisco’s CEO Just Sold $27 Million of Stock in 3 Days
- Summary: Cisco CEO sold $27M of shares over three days.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxObk1wZmhoMzladm0wOVlmakNfWXdhTWN1ZHZ2WmFfVzN0OTVBWVpvMW1vY290c1hyalBfMS1vcGVzWXNidFFlUGtZSjJ6UXpnQ1JyNktMVEg3RklqdnYzZ1o3cEpETlRpUXRNNUdoUmJfY21QQXczRGpWU280c3FTRUZqR1U0elNSSGRvWHBpb3M?oc=5>

### Can Cisco Stock Hit $120?
- Summary: Speculation on whether Cisco stock can reach $120.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQTlB1aWlkZlVUd1pFYkpGVzhlaDUtWEs1MHhyZlVQUkV4bkRjdWRLbmdLME1McGRvNDIwMFgtVkVqcUhHOGhocDZsX2l5SExvTW1iY3pGRzRNamVFcDZWZ2xuREN6aTN4Sm9tcEp2M3RDRmhfbUdlZXhBS0RFREcwZGJjVmN0Z0g1TnFRSg?oc=5>

### Cisco Systems, Inc. (CSCO) Stock Forecasts
- Summary: Forecasts for Cisco stock performance.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxNd2dxNjJnclhCR195N3JKQnlXd3hFdmZ2bExObjRLSGRlRWEtRkNJVHpLNTFxQXBDMzJGU2J3amVRN2NVWWl5VUtiZnlDd1Q3eEpGbTF2NlczZXlvMTJ0ZllmU0VpNEU1em82a3NmOENJREFpd1c3UlVwYS1pSHhONkFBNVFOWDFZUm4tVA?oc=5>

### Cisco: I Downgraded It At The Top, Look At It Now (Rating Upgrade) (NASDAQ:CSCO)
- Summary: Analyst upgraded Cisco’s rating, signaling improved outlook.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQVFpybG9LeWxHcFNRZlh3Ni1VcnlwOENLTzRiQlpWSllOR1A5YUJDSEFMNHFjbktyRFhoUGx4dHZXbUxfSEQzbEU2SlJjTlYzMDE2NEJiTDNHMl90VlMwdHdnWS1LYVBicGxvM1RrWEtZaTd5TWthYzZtQzNzakFTeEpBQ2duNHVockpJSmxYN0JSZ3RGMmVuMjd4QS1PX0dPZkVpVFVB?oc=5>

### Cisco Systems (NASDAQ:CSCO) Stock Rating Reaffirmed as "Buy" by Rosenblatt Securities
- Summary: Rosenblatt Securities reaffirmed Cisco’s buy rating, supporting positive sentiment.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxPaVIwOFhuSWFhV01nd3BaN2VoS2U3eE5hTlk0WC1CVnBsY2FLSEhialBMU1g4TV8yOC1PZ0pnMVpna1VjWGhhbGdOTHVKZ0UwMlJENlNnTG52am4tMmszblNOczBwdlV5b0UzUTZOUnN2RElfZWdVRmtCVWJFNXRCYXppMWROWFFENjhhLXdoekRsMTlKYXBhZlFJWnBwRmx6NHBheTgwQTBzd1dORUluWG5HN0U3bFU1QmpSRW94Q2lYTG41T1dvTzlDMkxmY2hGTFBST0ttZldsQkk?oc=5>

### Cisco Systems (CSCO) On Record Results And AI Demand Has Investors Rethinking Value
- Summary: Cisco’s earnings and AI demand prompt investors to reassess value.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxPdFN2cHhBMnE4emxqbmVYbkRDZ2FyWlc2cGRsNk9obHBKb3hTNHNYUjVWRFJvY24yQUNmRmRFV1puYUJEWGRuUkU2ZjZZMDF0c2VtTnV0STNqYm9RV0tPeGlXaHZVWVlOREJOdXNvWUVZdk5MTDM1UXdpdURKYm14X3Yyek1KMzJzeEhpVFFheWhrYTFZd3AzN29memJjOTJQMFZZMXJ0MUFTZ2Y2X0NhQ3dLdW03RElJaTN3SFdKWXZtNDFKRi0w0gHMAUFVX3lxTE5JMDFGR2lXTXhtRFp5cFRzejV5eGNtb3pCQXJ0QkktRkVYOVlvRExfbjg4dGJTcjVaYXFueVFsZi1jcTRPYkt3UjhWTzhfaU4xRTlCWEQ2WnZ5cFdUYnZ3OHF2SjdiRWIxbFJZajNKd0xJRmIwdlVIbGVldXA2TDlMQnRnV0RjcVIwZTl0d2dUWUtvZVVKRGM0OVZ6SjhYemgxUUtUQWJSOUxMX1BHejd6OWRieG5RVFUtcnlVQWpmclNWb3FGTEtBdTRoTw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CSCO** | **27.50** | **7.38** | **19.19** | **24.40** | **381,629,005,824.00 USD** | **29.56** |
| ANET | 47.80 | 13.70 | 39.76 | 58.50 | 225,277,280,256.00 USD | 51.84 |
| FFIV | 25.66 | 4.56 | 18.39 | 13.30 | 18,291,572,736.00 USD | 37.12 |
| HPE | 24.75 | 2.41 | 11.31 | 33.70 | 63,744,860,160.00 USD | 138.24 |

Peers fetched as_of: 2026-11-23; CSCO reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-12
- Next expected earnings: 2027-02-10 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-23

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-17
- Revenue (latest available single quarter): 12,844,000,000.00 USD; period 2018-04-29/2018-07-28; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 4,552,000,000.00 USD; period 2026-07-26/2026-10-24; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/858877/000085887726000185/csco-20261024.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMirwFBVV95cUxQaHZ4VHhKWW9SaGUtMjY3elhGSzlrX2ZMUWwwNURmcUJpR0hwVnZaM1ItT1RhR0FiQVBVWW1ubUZJc2k1bHF1SGlmaEJsazNMMGxEWWlPdHN0UnltcTBpRllHTzFOTWdXd2xvUzdobWxNaEljSF9DcFlDcDF6YnhTNDliQ0ktcVpNT3JtNUJjY0xMTU14MHA2WWtFZEhqazdlR1Y3WDFMUmhJdC1PeHU0?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPRVVEN2VyeUR1UFJzOXczaW1IQ1dfOTBzWEsyc2YycmZZUTR6YVgtUmw3Q2dZQ3pGNWZhU294VWd1ZnYzV0Mtc180ancyUENfVHhnM1QwZ1BJRkNEZUVkZjhENm9CbGFpY0hhcHRwOWhoYmIzMmpfZzZ5YUpEQjF4REYyNzlBbkxfdzNUV3dUdHFXbm8wRVRtUVJB?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxPMFpXbU5jSk5sYzdFRGhDU2p2X0puVjVxbEpMWVBmVlBETzJSYWs5RmRvMWF2OFpKcEFkQ2QyT0pSMEVnT25JdlNVNkRxNE05MjBoMy00ZURxdlctemo3YWFOSlpKM1ZEdTQ5c3J6d2EzOERrNVlDOXUtb1YyeEd3YUFiOUZjbXd2d2E2N2syR0szV3VYM24xRTdvUk1LQVo0UkNRTHFNOXpfZFhsZkNXU29yajBHQkhhc0lLalY3aw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQazVldGNaeWhMdGxVX3lmZlJjRHh5OE91TFUzUGhzYXJjUDB6aXh4Y0hITjZMREZPTmZ0UmYwRGxzY0VoSlRVWlF2UmVCeHZ2NWlIbEtja3V3RHhNNmtoYlBTcjNQQ3pXQm5zNXdUYnZuY2hGeXNPbHVCUDBDSDEzQTdhbXBSWDRyeHZ6dzl4QlQwNEVES0lQVlZB?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxOLW5SV3lqa1B5SE1SMHZhUDhKaWNlaG5fUnZvNk00NHU1eHU4bVdxWXVFZDQ2bmtpOVRwUUp1SXg1dnB4S2h6WFdYWmJxODJLOTFacmtoLXFPam1TUTRCdDlpN0FEcElWS1dHMFFRWUd0NjN3b0JUQ2lXcTh1dmhmcHpLbzlDQWlzX0VZMnRBNVpEY3JCSXlIazVqTzBuWVp4azJ2QXFUSXFtNkRlQzdPdWc0alhIVlpFTGVyNEx4b0JQWHo3NWc?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNWVh6MU8tWllnenNJUHZSZ0MwMDNKSE9IaVF5VXdJb3VhVzBucXI3ZDMySUhCUmRIQ0pWSHM4VWROMjFndmF6RElkV3J1aWRRckNfNGVobXNKQWtTWW8zdjJzcnZwWFA1NlRmQXJMVUVTSW9NRy1qbHhyVURZN25QMEZnOHExWl9vUWkwSy1Bcw?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQWUdpdXY2TlhoRDBwTWNzZU9Nb3plYWFHZ1JXSEdhejlUOHVMd0ZVQklBc1p0dHRjT0lpYWdUMWZmc0QwSS1XNFN2eU1ibnpFM2ZTNzhkeS1JbmpiN3dPcTZ6c0x6emtYVlFqNXRHRWZkMGw5ZEJGb0puN1k2RlJySEZmcXlWTExHR1Q4NjNTaw?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPbVRIOElDNVBrZkR1MHZrcDNvVXIyT0lObnNwcTVQR3Z1dHA3VHFGdVNvLUpGN21pZTJUVDFMMzZiNnJZME9NbTRsU0lBZTdUSHVsYVFOSGZuMFNaWldXenU1cFhRVDUwTjhTYlpzd2hGOHU3STRxUS1wR09jS0wwdkRyYUdqTnlOZllV?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOd0psSW1iRElNXzlmeTI0QTZrM1J1UU5QaUJnS1J4NXFMYzhMM2dvb3dxeG5zSHRFTG5IRkhPTklXMy1vM01GaDBRSlRYNjQxM3E2aEZtYXlyTEdRR0x3STNMMUlyQ1A4aWNERVNQTW1RazVaZUc2WFJ2UjY1eVVUanA2U3ZGMXZITlRJOVRNeF9QTzhJaHc?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxPM3ZtdUpuUWJsTHIycGc5Zks1dGpGcjNfbjBjZGNyWEwwRWFseXBXMjg5eXVTNnpNekxrVXJleXpUNHhQWXQxQ2thbGRrbU5lWDZkRG5PZkN5UWJLeDVjcS1iTjk1bk5ZU3lUcHlza0d4VkN5NjVWWWxveGk0NWZ5X3p2Uk1SeHhtTm1GZnBSZHB0MzE4ZEdKTW4yUmJRZW0zRHNjN0I5RThrSVJZbEJFNEh6Y01hOUNfOEFqUXAzZHdEbWhCOW9j?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPZkpSempEOHAyWU5QVVlKUGw2Zl81RHBKRnBGT3ljMmQ5Q21VazV1azg0ZzdUek5zZHQ0MVZfRkJGVWNzQXpHUkk5dVVZMENON3JuYWJsQ3RDVlVqNS1FeGp1dUprLUFWSnUxd0xDdFg2dUJmZ2tXVU9HS2RyaHJKeEVVTmZULUpoUVlDZzVjNHVNMGVfNTRiOC11OG5sbkhEVzhZODRlMlg?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOMHZiWHc0TlV6cUxOTTNTbDQzdkczcWFEZ2RELUhIaG1vbDhjcFJreXZleXRmc0Q3UHNqbm84SW9pZlIwdmY2Z0xLcUt5RXd2c2RQT3NCREI2RmdmRGthaUJhU3pTd09NZUg0RllpZ3hVNmFGZlRBbVAwZ2ltajRiQ1lYQmFwMmFBSHNqSDl1WmtXbmtmRWZtOUVFNkFiYXM?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOR2gxQW9fU2tUZlVfZ3k0RGw2UF9KWjAwVGVFUFU4c2R1VE5PWERjTkMtNnF6OUNQNjYtQzhsN1RrUFU0OHU1MjJaeS0wYUdIdlY1TmVpajRVZWh1TWhrNG82OWRmeHBaZzg2dEREcGFOc01mVE4tR2ZPUWtGc1dkRmM3dVlJTjNXaHpENFhzUXEzN29SOGdv?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxOQW1JNjZlRklwSUJiX3pwLW13UG5WZF9NbTc3Mlk4dmhTeUNReWlfLWloUFNrbG5GY3ZfczdIZ0tHbUI0VGZ4dGFub252Z3dfMTdGX0ZDQi1LRVVxYW1wdkhlLXRhbzAyMXhsMHVUcXExRWlHbW52N2EyRlQ0OThlOWhB?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxQNzl3YVozazZGRThYdDlEWklreDVRS2hzUnNDcXFDZUpjNUxjbm1adFNaTWtRSWRVYkUtSzFxZ1U0RVFCNnJpZnZQYzhubUZYYnRSNjZYWEVsZjZncm5kQ0xpSDVwWFdoaDNiWl9XUmQ1RTQ4LTJ5bkJFLWRMeUpremluV3Q0TUVVdkhwMkVXd1AyWGRPQVBySHYwTVFyeGxPN01mSTVQSW5FUHlReDFSTllQTFFXTnRXTXhWaFExMNIBxAFBVV95cUxPQWVFV253MkNwaVBQdU96ZVoyTW4zN0NDNUNvWjBjMnJCZTZ4czE4bEc4MWZzbDlNZl9saFNkZllxMXZYUVdNTmpxanFWUzNGeldqNFFmUjEwQXptQlZ0dGQtaHhFRko1ckZmYTF5Q3B1WTNWR3ljU1J5QzBZTGV6ZHZDeURHTGliMDVNbjJqT2gtNnVkeENDVGRMYWcwQTR0NHM2UXM1Ql83TndpVlZmeXFjTGVEd2NYMnQ1V2dDWnFrOXBZ?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxQMTdVWXJXZVV6SEJjNTl1c3RUNU1KaDBNandHbjNobHVjajR1Z0VOT3B5cUhueFlDdnN2ZklTTTV6QWp0Y3FFazdHZEwyRmV5Wm1kOURvQ2NkY2VWU19ISjB5clA0eEV6YjdHQldlRXBkVXlfbGw5dzF4cjhXZk9EZkxwYjVkMHNZcS1WY2dPTnNZR3A0MF9VVWZHRFd2bl9aNTdpUXNjRnhuOTRRUXp1TVNEbVM2SGZWN21LQnBqRzBodFZVZ0o4?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOdEUwVkdOckx1ZUhBUVhfc1VpWk1jckhFYmFkc2ZkamNlOTlMdy14ZE8xX1BsN1Z4eENlRHJESFBHckNkd3FDUEVjLUNWUlBOdlJ1M0MxaEVfdWI4bGFCLUM5U2N1cVIxMGNQYUtvcVZneUIzc3BuanE4MmRpeGRVak9BN1NJTzdfcU1B?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxObk1wZmhoMzladm0wOVlmakNfWXdhTWN1ZHZ2WmFfVzN0OTVBWVpvMW1vY290c1hyalBfMS1vcGVzWXNidFFlUGtZSjJ6UXpnQ1JyNktMVEg3RklqdnYzZ1o3cEpETlRpUXRNNUdoUmJfY21QQXczRGpWU280c3FTRUZqR1U0elNSSGRvWHBpb3M?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQTlB1aWlkZlVUd1pFYkpGVzhlaDUtWEs1MHhyZlVQUkV4bkRjdWRLbmdLME1McGRvNDIwMFgtVkVqcUhHOGhocDZsX2l5SExvTW1iY3pGRzRNamVFcDZWZ2xuREN6aTN4Sm9tcEp2M3RDRmhfbUdlZXhBS0RFREcwZGJjVmN0Z0g1TnFRSg?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNd2dxNjJnclhCR195N3JKQnlXd3hFdmZ2bExObjRLSGRlRWEtRkNJVHpLNTFxQXBDMzJGU2J3amVRN2NVWWl5VUtiZnlDd1Q3eEpGbTF2NlczZXlvMTJ0ZllmU0VpNEU1em82a3NmOENJREFpd1c3UlVwYS1pSHhONkFBNVFOWDFZUm4tVA?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQVFpybG9LeWxHcFNRZlh3Ni1VcnlwOENLTzRiQlpWSllOR1A5YUJDSEFMNHFjbktyRFhoUGx4dHZXbUxfSEQzbEU2SlJjTlYzMDE2NEJiTDNHMl90VlMwdHdnWS1LYVBicGxvM1RrWEtZaTd5TWthYzZtQzNzakFTeEpBQ2duNHVockpJSmxYN0JSZ3RGMmVuMjd4QS1PX0dPZkVpVFVB?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxPaVIwOFhuSWFhV01nd3BaN2VoS2U3eE5hTlk0WC1CVnBsY2FLSEhialBMU1g4TV8yOC1PZ0pnMVpna1VjWGhhbGdOTHVKZ0UwMlJENlNnTG52am4tMmszblNOczBwdlV5b0UzUTZOUnN2RElfZWdVRmtCVWJFNXRCYXppMWROWFFENjhhLXdoekRsMTlKYXBhZlFJWnBwRmx6NHBheTgwQTBzd1dORUluWG5HN0U3bFU1QmpSRW94Q2lYTG41T1dvTzlDMkxmY2hGTFBST0ttZldsQkk?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxPdFN2cHhBMnE4emxqbmVYbkRDZ2FyWlc2cGRsNk9obHBKb3hTNHNYUjVWRFJvY24yQUNmRmRFV1puYUJEWGRuUkU2ZjZZMDF0c2VtTnV0STNqYm9RV0tPeGlXaHZVWVlOREJOdXNvWUVZdk5MTDM1UXdpdURKYm14X3Yyek1KMzJzeEhpVFFheWhrYTFZd3AzN29memJjOTJQMFZZMXJ0MUFTZ2Y2X0NhQ3dLdW03RElJaTN3SFdKWXZtNDFKRi0w0gHMAUFVX3lxTE5JMDFGR2lXTXhtRFp5cFRzejV5eGNtb3pCQXJ0QkktRkVYOVlvRExfbjg4dGJTcjVaYXFueVFsZi1jcTRPYkt3UjhWTzhfaU4xRTlCWEQ2WnZ5cFdUYnZ3OHF2SjdiRWIxbFJZajNKd0xJRmIwdlVIbGVldXA2TDlMQnRnV0RjcVIwZTl0d2dUWUtvZVVKRGM0OVZ6SjhYemgxUUtUQWJSOUxMX1BHejd6OWRieG5RVFUtcnlVQWpmclNWb3FGTEtBdTRoTw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
