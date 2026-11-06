# META Intelligence Report

- ticker: **META**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/META/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/META/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:01:21.004257+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 3, 'ai': 13, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/META** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 11 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 41.67%; oldest publication 2026-11-01

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 605.0800 |
| Return 1D (%) | -3.9556 |
| Return 1W (%) | -3.1128 |
| Return 1M (%) | -18.4418 |
| Return YTD (%) | -8.0977 |
| Return 1Y (%) | -4.5314 |
| Annualized volatility (%) | 41.4066 |
| Beta vs SPY | 1.3608 |
| Max drawdown (%) | -28.7332 |
| Sharpe (rf=0) | 0.0924 |
| Downside deviation (rf=0, %) | 27.6372 |
| Sortino (rf=0) | 0.1384 |
| Historical VaR 95% (1D, %) | 3.7761 |
| Historical ES 95% (1D, %) | 5.6434 |
| Correlation vs SPY | 0.4467 |
| Tracking error vs SPY (%) | 37.3682 |
| P/E (trailing) | 21.49 |
| P/B | 5.68 |
| EV/EBITDA | 13.59 |
| Revenue growth (%) | 26.10 |
| Forward P/E (estimate) | 17.00 |
| Gross margin (%) | 81.03 |
| Operating margin (%) | 35.41 |
| Return on equity (%) | 32.26 |
| Free cash flow yield (%) | 1.09 |
| MA50 | 673.9789 |
| Close vs MA50 (%) | -10.2227 |
| MA200 | 631.3304 |
| Close vs MA200 (%) | -4.1580 |
| RSI (14, Wilder) | 34.9500 |
| MACD (12,26) | -23.4192 |
| MACD signal (9) | -16.2960 |
| MACD histogram | -7.1232 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'META': 276, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 605.0800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.9556 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.1128 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -18.4418 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -8.0977 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -4.5314 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.4066 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 27.6372 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.1384 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.7761 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.6434 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4467 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.3682 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3608 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.7332 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0924 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.0024 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.0340 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 35.4140 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.2640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0890 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.4948 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 34.9500 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -7.1232 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -10.2227 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -4.1580 -> Slightly below the moving-average trend level.

## TAILWINDS

### Investors Are Beginning to Say That Meta Is The Best Buy And Hold Stock Through 2030
- Summary: Highlights investor sentiment favoring Meta as a long-term hold.
- Date: 2026-11-03 | Impact: low | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQekVac0tXM3pEX253R1RuMlJoeXlHUEc5T0dIeHEwVkJQOHZ0SWI1XzlNWk5EZURWbl9xOEQ2Um5mTE1KeDhuMkIzTG83aGhPQ2R4WGFSMmctT0laR2VIOVRUUXg0NllPMU9TMlRpRWx5TUJPcVNLc1U5SWp2WnJEdHlqZHdZU0FLYk9Lc2h5OFMyMjEyUWdrSS1BMWpKa1U?oc=5>

### What Is Going On With Meta Platforms Stock on Monday?
- Summary: Meta’s stock movement on Monday is discussed, highlighting potential market dynamics.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQWW1uaWJkbk9BMm5MZnh4RG5IVGFsTV81MFJyRFhKR3k1N3c0OVRWRlkzSFJUY1FheGpmVkplZ0xCN1JMMVFhSDhqdHIxN0Q3bEw3ZnBSSWxpV3BJMzN2UDVqMGRfRDRaSFJXWXZheU8zeXVRX1VmcmI2WG9HdVpuRDcyVmVFMEJNZzAzVUlCZGRRcUNFUU1BUTRwSzkxaEk?oc=5>

### Meta Platforms, Inc. (META) Is Spending Billions on AI: Will the Bet Pay Off?
- Summary: Meta invests billions in AI, potentially boosting future capabilities.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQOXBqcHhOdEM3MkZxZG5aOVJqbWY1ZF8zYXJSMnhXb2JqZWpkNGVTU01nbERXeFdoQnZkTm9NN3htVVktME1VVF9DcVlQdHQ5R1Mta1NYbU5xX21RYkNlTE9BNjFlY21kRlRjTzRnVG9GLTFyNzgyYW96MTE0VVRVQ2ZaMnJGZXBIM1RRdFJiU0tHTjVKUFNBYkluY1U?oc=5>

### ETFs Are Buying Meta Platforms (META) on Monday
- Summary: ETF purchases of Meta shares on Monday indicate institutional interest.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxObXlMMUZPdTgwelhHYnVDZXBuMHlFNGNWZHp5ZTNpTE5iVkxTODFRcWoyNUtrOHRlcC01QmxOZ0JOS0RzS1J1c0RwdkpBcFoxMW8xRVNTVllXbGVjUjd6eFNKdThtVnhHQmV0alRrM0REQUVBbW1lZDlITEJhWlZndjJqTi1uRFRBamxPaG51Sktld3ZRVkRtYVlqZEs?oc=5>

### Meta Platforms Completes $15 Billion Senior Notes Offering; Stock Option Fully Exercised
- Summary: Meta Platforms raised $15 billion through a senior notes offering, fully exercising stock options, strengthening its balance sheet and providing liquidity for future initiatives.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxOOHpYN2d2STZDaDdUOVdlSHZyVWJNd0FHaVZURDM5NUVMbDA0TFFRdmkzQ05VVHhpVnFsNUxuSHd3WVl6RDMzQ181d1R2M0h4Q0lIaXQ4TXloV1ozUGhwZ20tYWlONThrUFMxT2dCMGlmQ2dmT2lPSURJS0tyRE0zTDRzMlA4a0NLOGw0czBSd01RaWpwWGZpbGRPRW5Od1lmMGFjVlpxQVcwLUFQTkxWajM0emQ1bVJVb3J2QUVZT0NMUG5rbjlHbS1velk3dGVXQnpOcEw2QkZDYXZnVFhtZmh3?oc=5>

### As Big Tech Sheds Billions, Meta (META) Signals a Top Buying Opportunity
- Summary: Meta highlights a buying opportunity amid big tech divestitures, suggesting favorable market conditions.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPNVNIdTFHNlVvNzhicnVvYVF1aTVIRG9MWkVFdERSZ1Awd2dHTDVaUHd1WXRVVkJBRjd5UzI4cHdJMm1nbjlMUjcyUXJ6eHJ0ckQ5NGdGZVl5b2gwdnJualZPZVRhOU5Tb3p6MUEzY2p2bzVTR3VSSkMyR1VLcWZja0M1dXVGTERwY3UwcHpRWnRWZTlpcFJ0Uw?oc=5>

## HEADWINDS

### Meta Shares Are Down Since Earnings. Is the Stock a Buy?
- Summary: Meta Shares Are Down Since Earnings. Is the Stock a Buy?
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQamFKWmVYLUc0VkRSZ3U2anMwaXJBVWNsM251R0UwVUpSUDBLM29LeDhGTGlLOEJUVDR2SDVGRGxFUFRfX3hQOUR2NXI5OGhibWVldkw1eWktYkRuTWY2T09fRFhoNXBxRE9sTFYxTlB2Rm9OYXhPNC1QQnNreXNFeEdkaDRjOFhHRHZ4d0FaN3JPMF8zRnlz?oc=5>

### As Meta Stock Suffers Its Worst Month in Years, S&P Delivers a Brutal $39 Billion Cash Flow Warning
- Summary: Meta stock worst month; S&P warns of cash flow issues.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNU3VvajNzS2xKY0VxU2ZhdXNXX3RMelRqeGxPWDZOQmhTYWFqMnRtZ1JFd2dxQkozT210dk00b3VVMU9NcklMM0xIUjRKOG40ZzU2VFlnd2dfTWhVc2xLQ3RiTWJJUW5vR0hTRndyczZDblhIamx2ekhoZzU1cDlyRVhoSUVfOG9oMkdtWUhPSmJCci1ILWs3Q3lLMA?oc=5>

### Meta Stocks Edge Lower 0.06% With UK Inquiry Challenging Its AI Content Terms
- Summary: UK inquiry questions Meta's AI content terms, causing a slight stock dip.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNLVFVNDR4WnRfS2UtUW1BNkQwbWZiOWVUN0JSVHgtQ0haZ1FVdW53NTByTjduemVYY3RtR01LNnMyaEtoalQyUnplUFI4LVZpOHFVR1U5N1hDZVR0OXZTV2xOU295NWd0UGZFVGIzRk94U3JfcHEtVHBqNWlkYW9OYnhGSVJXMnFMMVpHUmpKVnpudw?oc=5>

## CATALYSTS

### Meta, Sandisk Unveil First-Ever Stock Splits in 8 Days, Adding Fresh Catalyst to US Equities
- Summary: Meta, Sandisk Unveil First-Ever Stock Splits in 8 Days, Adding Fresh Catalyst to US Equities
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxPd1QyTGNwVmVPajRJSWdGc0hzS29ITXNwN2JPMy1lVEFvbGtEbGFnNDZ1TDZhUFBKaXhwVG4yaHRVVmlaMWlSNWpjY04xcTV4SDJlbVBSd1BzWlp6ZzdTbEpMS2dyRkhuWjMzLWtyM2JSZVc1eVAzcFhLT0lvNTg1VDJIaGRSWm9USXhxNWJxVHhBcU01cWVGUnpILUxxbmNaMERwbHJPdVRKV1ZVS25OZzBWM25lY05neUdqOE9zdzg?oc=5>

### Meta (META) Acquires Conductor As New U.S. AI Rules Cloud The Payoff
- Summary: Meta (META) Acquires Conductor As New U.S. AI Rules Cloud The Payoff
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOOXBmY3ZHb1FqZURHY1pYaFlXUENmelRYSDlrZ2ZyV2wycHFYY2FBTHZTQzdrbktoUnRxTl9LOG1ZTEp0NmlzU1VXTmlTdFZueUV0TnRvWFU5NDZvRHBkMEk5TTJYUXhMWndkT01IUHMyRk44d2l0THhnZTQ2MUI0MWxGcTlDcThhLXExMkZoT21uSldJQmROZlZ3?oc=5>

### Here's Where I Think Meta Stock Will Be in 2030
- Summary: Long‑term price projection for Meta shares.
- Date: 2026-11-01 | Impact: low | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPclByLUdFWGlDVHB2TmloYlpXdUdJRlJwc2lhQzl5YmR5Q3VraFJGQU4wVzhGN1hKbFhhN1ZWTGhCTnN4UGZfcU5XbUtmd21uaHFOdk5FdDBhWE5MamFjU3VOZlROQVZZMlY0VGtLamRmbHBlZ2FQaWY1MXVtRTNJalpjQjNBRmJpZzl4REh3c0w3cHp1?oc=5>

### ETFs Are Net Sellers of Meta Platforms (META) on Thursday
- Summary: ETFs sold Meta shares, indicating negative market sentiment.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOZ2ItaERBamlLbk94ZjhjQy1BcnBCcGd6UTEyaU9XQXVEREdtNE8tYnZhYWxMc1k0a3pEMnI5VE0yR1dFeHByVGNmSGNlcXNQUVFRSTFTa05HeC1LZHdTdHlIei1oVFpBc1JzMGZWVF9HSXp0M243OEFqREpBMlhLVzh2YlRqcVp1WHJJU3BkMms4ZG9QZUN4dGtpNDQ?oc=5>

### Meta Stock Forecast: AI Funding Push Puts $648.82 in Focus
- Summary: Forecast emphasizes AI funding push, projecting a $648.82 target price for Meta shares.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxQMHR2WWZZanFiZEZVa2RZZ2VSZXFrNE9RSGk2WXZ2S21aQnNyRnJwanh5ejU2ajFOR3FHQXRuVGlVdi1RWThmbFdGdGJVMVBkcHhEaDhtOTJvUzE4SDRqek5KYURBTFRodFJXT1dtZHJmRFhfekFRcmlsYTdoRF9NNUdGVTFOM3JDV0VhREFQNVhSUjVMYkhZX3YxbURkb283cldUYW4xb0g2aVFjX2w3Y3c3OFEzUDMtQ1Y4?oc=5>

### Meta Platforms completes $15 billion senior notes offering and issues additional shares
- Summary: Meta raises $15B via senior notes and new shares, increasing debt and equity supply.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxPZGV3Mk1QV2FBSGl5MHh3Q2t6cnB1VE1wVXptUUx2NUNKZUJEYVM0ZXJJaHVXZk1uWXUwRGdqa00tS19lcjRMX2Q2dVdicWtYRFlqdzVXYTZlZWZSU2xYZC1VRXJ4ZnlxeTRIemd5eDRmOEtYQTZnRjByTnVfaUVMaVc0NmtETE5Xcm02X3dOcEVnLWhaNHNYZmxub2pwejZFQno3X3FjSjFOcmlsS3ZqYmh4X1RPSm10MEJkaFFLUFVfOC1wSTJFU3RUeDJrRjlYV1lKMGNkRVI5QQ?oc=5>

### What Are Wall Street Analysts' Target Price for Meta Platforms Stock?
- Summary: Analysts provide target price estimates for Meta, reflecting market expectations.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPTlJYeVhYSENXbTJPTXRLZ0xFdkp3S1dKaGFNYUh5alQyd3BUc3dXb005Szh1R1VjQWg4bXVKY2diMmRWT3l2cXE3cmY5aU9Ib19JTllMMFp0ODFfS04zbGJDYks0VjNOaUNTOGY4OFdvb1FqR0FwRUM3S3hHNXJYQldya0RoRGlnMFJzMlRKeXM3RFZ4d3JZZ2Mwei1sQUU?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **META** | **21.49** | **5.68** | **13.59** | **26.10** | **1,547,088,560,128.00 USD** | **-4.53** |
| GOOGL | 15.09 | 5.27 | 18.20 | 24.70 | 3,473,915,510,784.00 USD | -0.35 |
| SNAP | N/A | 3.82 | -79.15 | 18.90 | 8,608,196,608.00 USD | -30.27 |
| PINS | 82.46 | 3.65 | 37.40 | 11.90 | 11,349,721,088.00 USD | -23.15 |

Peers fetched as_of: 2026-11-05; META reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-05

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-22
- Revenue (latest available single quarter): 13,727,000,000.00 USD; period 2018-07-01/2018-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 9,860,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMinwFBVV95cUxQekVac0tXM3pEX253R1RuMlJoeXlHUEc5T0dIeHEwVkJQOHZ0SWI1XzlNWk5EZURWbl9xOEQ2Um5mTE1KeDhuMkIzTG83aGhPQ2R4WGFSMmctT0laR2VIOVRUUXg0NllPMU9TMlRpRWx5TUJPcVNLc1U5SWp2WnJEdHlqZHdZU0FLYk9Lc2h5OFMyMjEyUWdrSS1BMWpKa1U?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQWW1uaWJkbk9BMm5MZnh4RG5IVGFsTV81MFJyRFhKR3k1N3c0OVRWRlkzSFJUY1FheGpmVkplZ0xCN1JMMVFhSDhqdHIxN0Q3bEw3ZnBSSWxpV3BJMzN2UDVqMGRfRDRaSFJXWXZheU8zeXVRX1VmcmI2WG9HdVpuRDcyVmVFMEJNZzAzVUlCZGRRcUNFUU1BUTRwSzkxaEk?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQOXBqcHhOdEM3MkZxZG5aOVJqbWY1ZF8zYXJSMnhXb2JqZWpkNGVTU01nbERXeFdoQnZkTm9NN3htVVktME1VVF9DcVlQdHQ5R1Mta1NYbU5xX21RYkNlTE9BNjFlY21kRlRjTzRnVG9GLTFyNzgyYW96MTE0VVRVQ2ZaMnJGZXBIM1RRdFJiU0tHTjVKUFNBYkluY1U?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxObXlMMUZPdTgwelhHYnVDZXBuMHlFNGNWZHp5ZTNpTE5iVkxTODFRcWoyNUtrOHRlcC01QmxOZ0JOS0RzS1J1c0RwdkpBcFoxMW8xRVNTVllXbGVjUjd6eFNKdThtVnhHQmV0alRrM0REQUVBbW1lZDlITEJhWlZndjJqTi1uRFRBamxPaG51Sktld3ZRVkRtYVlqZEs?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxOOHpYN2d2STZDaDdUOVdlSHZyVWJNd0FHaVZURDM5NUVMbDA0TFFRdmkzQ05VVHhpVnFsNUxuSHd3WVl6RDMzQ181d1R2M0h4Q0lIaXQ4TXloV1ozUGhwZ20tYWlONThrUFMxT2dCMGlmQ2dmT2lPSURJS0tyRE0zTDRzMlA4a0NLOGw0czBSd01RaWpwWGZpbGRPRW5Od1lmMGFjVlpxQVcwLUFQTkxWajM0emQ1bVJVb3J2QUVZT0NMUG5rbjlHbS1velk3dGVXQnpOcEw2QkZDYXZnVFhtZmh3?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPNVNIdTFHNlVvNzhicnVvYVF1aTVIRG9MWkVFdERSZ1Awd2dHTDVaUHd1WXRVVkJBRjd5UzI4cHdJMm1nbjlMUjcyUXJ6eHJ0ckQ5NGdGZVl5b2gwdnJualZPZVRhOU5Tb3p6MUEzY2p2bzVTR3VSSkMyR1VLcWZja0M1dXVGTERwY3UwcHpRWnRWZTlpcFJ0Uw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQamFKWmVYLUc0VkRSZ3U2anMwaXJBVWNsM251R0UwVUpSUDBLM29LeDhGTGlLOEJUVDR2SDVGRGxFUFRfX3hQOUR2NXI5OGhibWVldkw1eWktYkRuTWY2T09fRFhoNXBxRE9sTFYxTlB2Rm9OYXhPNC1QQnNreXNFeEdkaDRjOFhHRHZ4d0FaN3JPMF8zRnlz?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNU3VvajNzS2xKY0VxU2ZhdXNXX3RMelRqeGxPWDZOQmhTYWFqMnRtZ1JFd2dxQkozT210dk00b3VVMU9NcklMM0xIUjRKOG40ZzU2VFlnd2dfTWhVc2xLQ3RiTWJJUW5vR0hTRndyczZDblhIamx2ekhoZzU1cDlyRVhoSUVfOG9oMkdtWUhPSmJCci1ILWs3Q3lLMA?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNLVFVNDR4WnRfS2UtUW1BNkQwbWZiOWVUN0JSVHgtQ0haZ1FVdW53NTByTjduemVYY3RtR01LNnMyaEtoalQyUnplUFI4LVZpOHFVR1U5N1hDZVR0OXZTV2xOU295NWd0UGZFVGIzRk94U3JfcHEtVHBqNWlkYW9OYnhGSVJXMnFMMVpHUmpKVnpudw?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxPd1QyTGNwVmVPajRJSWdGc0hzS29ITXNwN2JPMy1lVEFvbGtEbGFnNDZ1TDZhUFBKaXhwVG4yaHRVVmlaMWlSNWpjY04xcTV4SDJlbVBSd1BzWlp6ZzdTbEpMS2dyRkhuWjMzLWtyM2JSZVc1eVAzcFhLT0lvNTg1VDJIaGRSWm9USXhxNWJxVHhBcU01cWVGUnpILUxxbmNaMERwbHJPdVRKV1ZVS25OZzBWM25lY05neUdqOE9zdzg?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOOXBmY3ZHb1FqZURHY1pYaFlXUENmelRYSDlrZ2ZyV2wycHFYY2FBTHZTQzdrbktoUnRxTl9LOG1ZTEp0NmlzU1VXTmlTdFZueUV0TnRvWFU5NDZvRHBkMEk5TTJYUXhMWndkT01IUHMyRk44d2l0THhnZTQ2MUI0MWxGcTlDcThhLXExMkZoT21uSldJQmROZlZ3?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPclByLUdFWGlDVHB2TmloYlpXdUdJRlJwc2lhQzl5YmR5Q3VraFJGQU4wVzhGN1hKbFhhN1ZWTGhCTnN4UGZfcU5XbUtmd21uaHFOdk5FdDBhWE5MamFjU3VOZlROQVZZMlY0VGtLamRmbHBlZ2FQaWY1MXVtRTNJalpjQjNBRmJpZzl4REh3c0w3cHp1?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOZ2ItaERBamlLbk94ZjhjQy1BcnBCcGd6UTEyaU9XQXVEREdtNE8tYnZhYWxMc1k0a3pEMnI5VE0yR1dFeHByVGNmSGNlcXNQUVFRSTFTa05HeC1LZHdTdHlIei1oVFpBc1JzMGZWVF9HSXp0M243OEFqREpBMlhLVzh2YlRqcVp1WHJJU3BkMms4ZG9QZUN4dGtpNDQ?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxQMHR2WWZZanFiZEZVa2RZZ2VSZXFrNE9RSGk2WXZ2S21aQnNyRnJwanh5ejU2ajFOR3FHQXRuVGlVdi1RWThmbFdGdGJVMVBkcHhEaDhtOTJvUzE4SDRqek5KYURBTFRodFJXT1dtZHJmRFhfekFRcmlsYTdoRF9NNUdGVTFOM3JDV0VhREFQNVhSUjVMYkhZX3YxbURkb283cldUYW4xb0g2aVFjX2w3Y3c3OFEzUDMtQ1Y4?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxPZGV3Mk1QV2FBSGl5MHh3Q2t6cnB1VE1wVXptUUx2NUNKZUJEYVM0ZXJJaHVXZk1uWXUwRGdqa00tS19lcjRMX2Q2dVdicWtYRFlqdzVXYTZlZWZSU2xYZC1VRXJ4ZnlxeTRIemd5eDRmOEtYQTZnRjByTnVfaUVMaVc0NmtETE5Xcm02X3dOcEVnLWhaNHNYZmxub2pwejZFQno3X3FjSjFOcmlsS3ZqYmh4X1RPSm10MEJkaFFLUFVfOC1wSTJFU3RUeDJrRjlYV1lKMGNkRVI5QQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPTlJYeVhYSENXbTJPTXRLZ0xFdkp3S1dKaGFNYUh5alQyd3BUc3dXb005Szh1R1VjQWg4bXVKY2diMmRWT3l2cXE3cmY5aU9Ib19JTllMMFp0ODFfS04zbGJDYks0VjNOaUNTOGY4OFdvb1FqR0FwRUM3S3hHNXJYQldya0RoRGlnMFJzMlRKeXM3RFZ4d3JZZ2Mwei1sQUU?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
