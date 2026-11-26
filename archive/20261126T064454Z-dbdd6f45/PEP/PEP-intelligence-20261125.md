# PEP Intelligence Report

- ticker: **PEP**
- Report as_of: **2026-11-25**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/PEP/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PEP/key-statistics/
- AI analysis snapshot as_of: **2026-11-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-26T06:56:31.323314+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 20, 'rule': 5, 'ai': 12, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261125T065354Z-0b3565c6/PEP** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 20 unique headlines; 8 named publishers; 0 exact duplicates; 20 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 143.9300 |
| Return 1D (%) | 0.8761 |
| Return 1W (%) | 1.4520 |
| Return 1M (%) | 6.0102 |
| Return YTD (%) | 3.3385 |
| Return 1Y (%) | 2.4995 |
| Annualized volatility (%) | 22.0361 |
| Beta vs SPY | -0.1593 |
| Max drawdown (%) | -25.2176 |
| Sharpe (rf=0) | 0.2219 |
| Downside deviation (rf=0, %) | 14.7294 |
| Sortino (rf=0) | 0.3320 |
| Historical VaR 95% (1D, %) | 2.2237 |
| Historical ES 95% (1D, %) | 2.7033 |
| Correlation vs SPY | -0.1080 |
| Tracking error vs SPY (%) | 27.9203 |
| P/E (trailing) | 18.10 |
| P/B | 8.81 |
| EV/EBITDA | 12.37 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 16.75 |
| Gross margin (%) | 54.33 |
| Operating margin (%) | 16.05 |
| Return on equity (%) | 52.19 |
| Free cash flow yield (%) | 4.61 |
| MA50 | 134.5330 |
| Close vs MA50 (%) | 6.9849 |
| MA200 | 143.0224 |
| Close vs MA200 (%) | 0.6346 |
| RSI (14, Wilder) | 59.3406 |
| MACD (12,26) | 2.0102 |
| MACD signal (9) | 2.3490 |
| MACD histogram | -0.3388 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PEP': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 143.9300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.8761 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.4520 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 6.0102 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 3.3385 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 2.4995 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.0361 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.7294 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3320 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.2237 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.7033 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1080 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 27.9203 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1593 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -25.2176 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2219 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.7480 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3270 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.0460 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 52.1870 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.6111 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.1044 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 59.3406 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.3388 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.9849 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 0.6346 -> Slightly above the moving-average trend level.

## TAILWINDS

### PepsiCo Stock And Other Defensive Value Picks For Higher Rates
- Summary: PepsiCo Stock And Other Defensive Value Picks For Higher Rates
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQY2FmbDdLMzQtYnc2ekdOSUl3RHJaQ3BkTWkzSXV6TlE5Q2p4YXJ4OUVXQU5SSU1nVVpLOEdlOUpSOC1aN2ZYSjljSEtGZ3RtV1p5eDdDUXcwR0wzdVROZWMtY3pMaldLaFRSZ2hpVmxYdVFDTTRoOGJzTm5rRjlRU0E1bTBGTmc4YVNOYVl0aF9tZ0lETzZCZkNKSjlxc3JvRmc?oc=5>

### PEPSICO INC (NASDAQ:PEP): A Quality Investing Case With High ROIC but Mature Growth
- Summary: High ROIC but mature growth suggests stable returns, supporting a defensive buy.
- Date: 2026-11-21 | Impact: medium | Horizon: long | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxNOUplZFJ4dUlHX1FGSHE0dFZ5RlVSVXdBWkduY1BoaTRXYWpsT3NIbllraG1aVTlCRTRuUG05RmNseDZJbDhZSlc0enRBbk5qME5yWUdQbkh6dDNXaVRsQVNuVkJJVThIZVNyYmxsbjRsNjkxNjZjdmRNREZReDQtTWVFSmhUa2tjMERKQkpJMmdJMFdiMzJuZC1sekRDamxQSHN6bXhyVTZLRDNFWmZCaExIcjUycXZRUzdJZldlT0gzSmJlSTU0OE5B?oc=5>

### PepsiCo: A Defensive 'Buy' In A Market Sell-Off (NASDAQ:PEP)
- Summary: Defensive buy recommendation amid market sell-off signals resilience.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxPUmtpWWdERFlMcFNZOTJ3eFhBNUFpSEZTVWhPczBpS3p5RUJyZGFZYV9LYUxDb1RtajhzOFRqZDJVQmRYbzA0M3lCVjAwY182NDZEaTlNMndiUEg1dFEzUEpRdXVESVZUWEF6blEtTHdRdlE5RnJIemtWRXQyR2lLNmN6SlVUS2dyRktJb2JB?oc=5>

### PepsiCo (PEP) Stock May Be 50% Undervalued Following Partnership Renewal
- Summary: Partnership renewal may signal undervaluation, boosting investor confidence.
- Date: 2026-11-21 | Impact: high | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxNQ0V2bUwxb1Y4Y2NrS2ZkNm1LOWx5S19rLUJHSVhyZy1lLWJEZVVsMng0R05OWUV2NlN3S1hVVXVzUndlZnJMV3ppQUNuT3dsMFF3cjE0RlpZTXVXSE90dVJzQ05CWlJtRm1KWFdJMm1HdkNrV2ZQdkhQQ2NzOFNLRkVOWjlUZ3NFdmNSMzJNWHFURG1vOV9SZDFPV3N6SHFXOEN4eVpUU3NleUNSRlZOZWZweHB3S09QcFA1bnBPaTFIcHVCbDhOZVotS0dkVkhqUUR4UNIB2gFBVV95cUxPaU9CUFBiUnptNnFLNVE5MlFhdEEyYlI2MXEtNEhRLVlMS1pDOEdoc0NQbkRvQUc5eDhfV3ZOUW96M3FtbDBweElJdTZrZEl4ZWQ3YjNtUzFnU3BUbG9vdGZtQkVjbXVvbWhHd3lwa3AycnhacGg2MW5pSjZtY0sxZ1pMSFluUEJSRUZEOTFZbzVWTnRUb0g2cEhPWGFhTlZQaS1fQ0lkMU00MXFORjVsUTZySVMydTV6ZUZydER4SC1Rck5jM2Q4dkZWWjRydFhfMDQ1dElKMk8yZw?oc=5>

## HEADWINDS

### PepsiCo (PEP) Stock May Be 49% Undervalued Following Margin Concerns
- Summary: Margin concerns suggest potential downside, questioning valuation.
- Date: 2026-11-23 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQVUdmVlJzZ1hCcW1ubUtSVU5sUnpPTkNmUklJOHhRRG1DVV92MkZKVWd6YkVaU0lLTml2dmJ0b1pyZkpLSFVJYnpXcXE5T1hJSkVoQWlhQWxzWWlCS3AtOTNLdnkyaGNYVG5MMVBiSVZXWmYweXJubkFQcEhadDZOUGxmdGRXdm1vWHJOQU9JcXdydGs?oc=5>

### PepsiCo: Still Not Refreshing, Remains A Sell (NASDAQ:PEP)
- Summary: Negative outlook, recommending a sell due to lack of growth.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPRGlRbFpjUVZkM1B0Rk4wZVVLRlhuaVN6ZHZkY2tCT3ZiU3p1XzVBRG1KbWFiVEFHR19GSkpyOGlRYXF2blRfUEZ2QkZ2TXBPb1ZMZnFzOFFqUjVyaFRydks0QzRWbjI1MEhWbUpJakd1UFJ1Vi1GNnRBMjRmNG5RTFZJV0lRcnQ5LVlwUA?oc=5>

## CATALYSTS

### PepsiCo (PEP) Lands Hyatt Deal On A Fair Value Debate
- Summary: PepsiCo (PEP) Lands Hyatt Deal On A Fair Value Debate
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNTVFiVXNnMmNNTlZ4UzA0QlFEZV94WVluckhCT1hsVjJnTXc5NkhiRnVyR0tTQ3phaWNDci0xZWpjQmpoWjA0X2JTU3dzalcyc1djU3gxY0hDV0ZKM0lBZDhINS1LM3VvMHRLUHpTbVhqTVdQb2I1ZU1nbS1BazlCS1pUSWp0TjUtX1NaZDRYVmZzR0VNUDZUeA?oc=5>

### PepsiCo (PEP) Shelf Filing Leaves Investors Asking If The Stock Is Already Fairly Valued
- Summary: PepsiCo (PEP) Shelf Filing Leaves Investors Asking If The Stock Is Already Fairly Valued
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxPYnFEbHFZX3FuWkpHeWxoRjJtb0RJX09sbnFVclVHSWJTcmREQmdwVldaUVJvU1JETk1TZk4tVkVoTTRtSDM3TS1NTHZYT3NTazdwTnAtbzNzN2ZrS0Fld25nWUE3cElGZVlvenFJY3lVbFRTWjdOUWdPdGZWLW9xdTJ0ZjEyVXZqSzlxUzgwWUJjaWF0b3o2WTJYVWN6MXltQ1pvRnluSnJ4Z3BLMzJKUG9FRGRhWkxmYVUxTkZnS3RwaVpuOVBaZUFiaW0xaXp1MUlhONIB2gFBVV95cUxPY1RDT3BNamFzeFl5MElfMVFfVnd3UlNzQlM0MGlfWG1SRFhuRDQwQm5NdXpHa2FPNHFHWGtkNDZuMGs1cVlwYW9NTEFEWm9hT0tPOUc2RUttUEtteFhxdzREaEZrZEpIMGJ3R3k0OTJVSmdsMThxR2J3NzAzUUpTUUVYbFpmOEtfelFSY0hFR1BvbnY0MXZ5M0lfS0JfRndmaEhMMGtZVy1SenJnb3EyMTZHVEktT2xrUnUxWE9BUkF3eWZGUG85ZGNYdXpkU3RNMGI0NVkxdDV1Zw?oc=5>

### PepsiCo, Inc. $PEP Stock Sold by Healthcare of Ontario Pension Plan Trust Fund
- Summary: PepsiCo, Inc. $PEP Stock Sold by Healthcare of Ontario Pension Plan Trust Fund
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxOVzJ3WUN4SkF0ZG1sTjFmR0RMQ2FTeGo4c2RJekQwNGhSMDRmdjlralo3OGR2Q0RXV2tsMlZwa2RJN3J6Uk1JVlR4U2tfdFJrVE1ycDB0STc5ZVlpOWROTElkVHNaM2M1WkdYRnB4aThBTEM5dE9iaDE1QUI1WDBGa29UVW16V3ZIeXREdG90ZjZlM1NaSC1KeGJTZmFpZGo3ZlBNdGRhNWV2bnNUQnljMUZGNjdhNVNXY3o1OTB1VVhnaWc2WUhTcVhocmV1RUl6SWc?oc=5>

### PepsiCo (PEP) Raises Quarterly Dividend 4% to $1.48 Per Share
- Summary: PepsiCo (PEP) Raises Quarterly Dividend 4% to $1.48 Per Share
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxOYmpxQzEwXzFmWFVlNi11VmxIYVAxTmFweHd6Y01uTkNObUlQQTNMVWJaZVZrN0psUjRGSnJpQVdnVXdnY1JwSGRpNmxHSi1RWGdyMGV4OExZQVNER0ZyUlNxR0VsSVdUT3JrOVdocThBcFZRQ09RV3RNYkxhamwzdW5nLTM4R0k4ODBTOE5RR2R4M1pGXzRYYzZHd1RrdnFxaDRSdVdsc0dLUHMwWEZIS3dfNzBPamo5NUJR?oc=5>

### PepsiCo: Staples Ugly Duckling (Rating Downgrade) (NASDAQ:PEP)
- Summary: Analysts downgrade PepsiCo’s rating, citing concerns over its staples segment performance.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxQUzhlU2RhMjJZcHpGWHd0VjJMaGdOdmZxN092LTZiMkRmc2k1V3prUk1xdFViRkRoblNUXy1VUTFneWgyeXIxR3hCNnZOb0dKQ3RYNUVtZW1wQ3hxd09ESFBOc1dELUR1VXFrZ2daU1dXbnVZSVVqZWRtcnhGT1VLcTNpRkZQRjg?oc=5>

### PepsiCo: 4.2% Dividend Yield Looks More Attractive As Volatility Returns (NASDAQ:PEP)
- Summary: PepsiCo’s dividend yield rises to 4.2%, making the stock more appealing amid market volatility.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxOdTh0WnU2YnM4N2xBM2E0aUJfbVltaGVEWmV0Z2M0aWpRQy1jVHZ6TDJLOFo0anVScHRtYUZUM2NqN1dEcGtfbS1NcXJVN2wyVW9jdjgyODlzRkdfWWJrd3FXNDZBbW80WU9wOGlLQlpmelF4SzU2MVp2M3V2V2UzZkQ1UzZPYWY2MWxVWE5wUFVKV2Z1YkZsbEdmQlpiTjlXX3JIT3dfZi0zdmY1Y21NUUpjM2tuYnZ5WFZZ?oc=5>

### Pepsi Has Drawn My Interest (NASDAQ:PEP)
- Summary: The author expresses interest in PepsiCo, indicating potential positive outlook.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTE9rZkZremh6dVBzNE1ETGNoVEplbXFuMUVndzlva042T2pKUnViWk5YMUF3cGN5RFNOLTgwamhna0h5TnNuaUtpWnk4eWwwWk1qUXpzU0dqcmV2NVYtYU1LbEt0UkRvWm9BM0RueVNsRWo4UW9VRGNCM044THRmUjg?oc=5>

### PepsiCo: Cheap, With A Record Dividend, But The Downtrend Channel Still Rules (NASDAQ:PEP)
- Summary: PepsiCo trades cheaply with a record dividend, yet remains in a downtrend channel.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxNbVQ3MXA0WFQ2dXNJbU1pV2V5MUE3dWF0Wnpva0prR1ZaZXlxamRNYWJNTXB4eHRQY0tqajU2TVp0eGZGWWRjMllvdDNRZkJhbkFXRWJxZnVwT05hVTdSWS1fcVZQaVlrXzlwMmlIekpyQ2NtaFZzY1R4V2k4aXlqeTN4Q21SUGh2bDlsRkhKUWEzN1RHOFBIYjdnTERzR0RZOC1UaDR0cmtWME1GMDBqUmpjQjMyUQ?oc=5>

### PepsiCo: A Dividend King With Little Room For Error
- Summary: PepsiCo maintains strong dividend stance, signaling stability and shareholder value.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNb2dYUUpLYWRlZkRWMWFKOER0Ql9faEFrRm1ORUdrUGc5UVM5SGFUeXlKU1hIbDVrNXNWWmhLY21TSUM4UUpJeDEyWTh4WjFoQVhPN3J3bFJUMEhFZk81WnpkQTNNSGVqSlFXNVA1OTJYczFBY3hTN0JSc2loTEJtalE3ekVuVzZ4d0hKRHhEYW1yY2dWQlE?oc=5>

### PepsiCo: Valuation Improved, Growth Story Hasn't
- Summary: Valuation metrics have risen, yet growth prospects remain unchanged.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPMkVxaW0xSHp4YTJQdTVZS1JCSEluQjF4VnJQUUR4dnp5V0tBVWpRc192cXJUM0RiMXBlTFg0X3ppSDB1M2lmZl9WSkRJMlpsWWp0eE9DeE9uX043UGpBOXVCZ000SndXQlJvNHZsbTk0MGtoT3ZsZ1NlM1hPRjBsclZrZmdGZE9IWmdUcTNCTQ?oc=5>

### Did Efficiency Plan Just Shift PepsiCo (PEP) Stock's Investment Narrative?
- Summary: Efficiency initiatives may alter investor perception of PepsiCo's strategy.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxOR0tGMWxMSG42dHY0RGItTUhoZXZZek04Smg0T3dmTEhhUTQtVU1IVGcxMXY1OWxNVUNkT3dGbnQ2eHRwR3JSSGE3cTQ0WkhKYjhmWFhTRG5qUmY2S2dsQ0pLWEhIUGhiYl9GQjZXczg5S3Z0TEtnR1JtdF90X0dMb2J4d012Z0RzUkVOSllGalRFR21JVkR3dFBXbUEtMFEwdFVlLW5SQW05T2lwWFdPUnI4OE1VcUZMNmF2SlNkVWhpNXNRd0hzR1ZUVEk5NGlhZ1RNUNIB2gFBVV95cUxPb3VKWEplVC1yemx2ZENzZ25rNkp6aGpUNl9OdlN0QmlidXhtWW5IbTNIRzJzcEdzd3NOUEJzcXdSUWtyTkN2NGhkZkZOTlA5aFh1d2VBbnJFZl9MZHVnQmFOcTFhVlFsVEpPNktMR3dUdXdjWkFBWE1nQUJIeHk5d2NfUEJkM3Y5azVZX0lLaW8yZ1R0YVpBbFB3M0VwOUJhLWR0bzlPLWtXZGxQdlZtWm1IemFEQXVXVmx2RzlVZUZVZVZzbXdGNkw2UERkNkhGeHNEYUxRZTh2QQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PEP** | **18.10** | **8.81** | **12.37** | **5.60** | **196,139,319,296.00 USD** | **2.50** |
| KO | 28.79 | 11.23 | 25.68 | 7.40 | 419,822,632,960.00 USD | 37.98 |
| MNST | 38.73 | 8.47 | 26.78 | 16.70 | 83,390,005,248.00 USD | 13.87 |
| KDP | 32.10 | 1.91 | 16.45 | 70.60 | 50,865,922,048.00 USD | 35.92 |

Peers fetched as_of: 2026-11-25; PEP reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-08
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-25

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-08
- Revenue (latest available single quarter): 25,274,000,000.00 USD; period 2026-06-14/2026-09-05; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,048,000,000.00 USD; period 2026-06-14/2026-09-05; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/77476/000007747626000048/pep-20260905.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiogFBVV95cUxQY2FmbDdLMzQtYnc2ekdOSUl3RHJaQ3BkTWkzSXV6TlE5Q2p4YXJ4OUVXQU5SSU1nVVpLOEdlOUpSOC1aN2ZYSjljSEtGZ3RtV1p5eDdDUXcwR0wzdVROZWMtY3pMaldLaFRSZ2hpVmxYdVFDTTRoOGJzTm5rRjlRU0E1bTBGTmc4YVNOYVl0aF9tZ0lETzZCZkNKSjlxc3JvRmc?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxNOUplZFJ4dUlHX1FGSHE0dFZ5RlVSVXdBWkduY1BoaTRXYWpsT3NIbllraG1aVTlCRTRuUG05RmNseDZJbDhZSlc0enRBbk5qME5yWUdQbkh6dDNXaVRsQVNuVkJJVThIZVNyYmxsbjRsNjkxNjZjdmRNREZReDQtTWVFSmhUa2tjMERKQkpJMmdJMFdiMzJuZC1sekRDamxQSHN6bXhyVTZLRDNFWmZCaExIcjUycXZRUzdJZldlT0gzSmJlSTU0OE5B?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPUmtpWWdERFlMcFNZOTJ3eFhBNUFpSEZTVWhPczBpS3p5RUJyZGFZYV9LYUxDb1RtajhzOFRqZDJVQmRYbzA0M3lCVjAwY182NDZEaTlNMndiUEg1dFEzUEpRdXVESVZUWEF6blEtTHdRdlE5RnJIemtWRXQyR2lLNmN6SlVUS2dyRktJb2JB?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxNQ0V2bUwxb1Y4Y2NrS2ZkNm1LOWx5S19rLUJHSVhyZy1lLWJEZVVsMng0R05OWUV2NlN3S1hVVXVzUndlZnJMV3ppQUNuT3dsMFF3cjE0RlpZTXVXSE90dVJzQ05CWlJtRm1KWFdJMm1HdkNrV2ZQdkhQQ2NzOFNLRkVOWjlUZ3NFdmNSMzJNWHFURG1vOV9SZDFPV3N6SHFXOEN4eVpUU3NleUNSRlZOZWZweHB3S09QcFA1bnBPaTFIcHVCbDhOZVotS0dkVkhqUUR4UNIB2gFBVV95cUxPaU9CUFBiUnptNnFLNVE5MlFhdEEyYlI2MXEtNEhRLVlMS1pDOEdoc0NQbkRvQUc5eDhfV3ZOUW96M3FtbDBweElJdTZrZEl4ZWQ3YjNtUzFnU3BUbG9vdGZtQkVjbXVvbWhHd3lwa3AycnhacGg2MW5pSjZtY0sxZ1pMSFluUEJSRUZEOTFZbzVWTnRUb0g2cEhPWGFhTlZQaS1fQ0lkMU00MXFORjVsUTZySVMydTV6ZUZydER4SC1Rck5jM2Q4dkZWWjRydFhfMDQ1dElKMk8yZw?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxQVUdmVlJzZ1hCcW1ubUtSVU5sUnpPTkNmUklJOHhRRG1DVV92MkZKVWd6YkVaU0lLTml2dmJ0b1pyZkpLSFVJYnpXcXE5T1hJSkVoQWlhQWxzWWlCS3AtOTNLdnkyaGNYVG5MMVBiSVZXWmYweXJubkFQcEhadDZOUGxmdGRXdm1vWHJOQU9JcXdydGs?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPRGlRbFpjUVZkM1B0Rk4wZVVLRlhuaVN6ZHZkY2tCT3ZiU3p1XzVBRG1KbWFiVEFHR19GSkpyOGlRYXF2blRfUEZ2QkZ2TXBPb1ZMZnFzOFFqUjVyaFRydks0QzRWbjI1MEhWbUpJakd1UFJ1Vi1GNnRBMjRmNG5RTFZJV0lRcnQ5LVlwUA?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNTVFiVXNnMmNNTlZ4UzA0QlFEZV94WVluckhCT1hsVjJnTXc5NkhiRnVyR0tTQ3phaWNDci0xZWpjQmpoWjA0X2JTU3dzalcyc1djU3gxY0hDV0ZKM0lBZDhINS1LM3VvMHRLUHpTbVhqTVdQb2I1ZU1nbS1BazlCS1pUSWp0TjUtX1NaZDRYVmZzR0VNUDZUeA?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxPYnFEbHFZX3FuWkpHeWxoRjJtb0RJX09sbnFVclVHSWJTcmREQmdwVldaUVJvU1JETk1TZk4tVkVoTTRtSDM3TS1NTHZYT3NTazdwTnAtbzNzN2ZrS0Fld25nWUE3cElGZVlvenFJY3lVbFRTWjdOUWdPdGZWLW9xdTJ0ZjEyVXZqSzlxUzgwWUJjaWF0b3o2WTJYVWN6MXltQ1pvRnluSnJ4Z3BLMzJKUG9FRGRhWkxmYVUxTkZnS3RwaVpuOVBaZUFiaW0xaXp1MUlhONIB2gFBVV95cUxPY1RDT3BNamFzeFl5MElfMVFfVnd3UlNzQlM0MGlfWG1SRFhuRDQwQm5NdXpHa2FPNHFHWGtkNDZuMGs1cVlwYW9NTEFEWm9hT0tPOUc2RUttUEtteFhxdzREaEZrZEpIMGJ3R3k0OTJVSmdsMThxR2J3NzAzUUpTUUVYbFpmOEtfelFSY0hFR1BvbnY0MXZ5M0lfS0JfRndmaEhMMGtZVy1SenJnb3EyMTZHVEktT2xrUnUxWE9BUkF3eWZGUG85ZGNYdXpkU3RNMGI0NVkxdDV1Zw?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxOVzJ3WUN4SkF0ZG1sTjFmR0RMQ2FTeGo4c2RJekQwNGhSMDRmdjlralo3OGR2Q0RXV2tsMlZwa2RJN3J6Uk1JVlR4U2tfdFJrVE1ycDB0STc5ZVlpOWROTElkVHNaM2M1WkdYRnB4aThBTEM5dE9iaDE1QUI1WDBGa29UVW16V3ZIeXREdG90ZjZlM1NaSC1KeGJTZmFpZGo3ZlBNdGRhNWV2bnNUQnljMUZGNjdhNVNXY3o1OTB1VVhnaWc2WUhTcVhocmV1RUl6SWc?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxOYmpxQzEwXzFmWFVlNi11VmxIYVAxTmFweHd6Y01uTkNObUlQQTNMVWJaZVZrN0psUjRGSnJpQVdnVXdnY1JwSGRpNmxHSi1RWGdyMGV4OExZQVNER0ZyUlNxR0VsSVdUT3JrOVdocThBcFZRQ09RV3RNYkxhamwzdW5nLTM4R0k4ODBTOE5RR2R4M1pGXzRYYzZHd1RrdnFxaDRSdVdsc0dLUHMwWEZIS3dfNzBPamo5NUJR?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxQUzhlU2RhMjJZcHpGWHd0VjJMaGdOdmZxN092LTZiMkRmc2k1V3prUk1xdFViRkRoblNUXy1VUTFneWgyeXIxR3hCNnZOb0dKQ3RYNUVtZW1wQ3hxd09ESFBOc1dELUR1VXFrZ2daU1dXbnVZSVVqZWRtcnhGT1VLcTNpRkZQRjg?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxOdTh0WnU2YnM4N2xBM2E0aUJfbVltaGVEWmV0Z2M0aWpRQy1jVHZ6TDJLOFo0anVScHRtYUZUM2NqN1dEcGtfbS1NcXJVN2wyVW9jdjgyODlzRkdfWWJrd3FXNDZBbW80WU9wOGlLQlpmelF4SzU2MVp2M3V2V2UzZkQ1UzZPYWY2MWxVWE5wUFVKV2Z1YkZsbEdmQlpiTjlXX3JIT3dfZi0zdmY1Y21NUUpjM2tuYnZ5WFZZ?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTE9rZkZremh6dVBzNE1ETGNoVEplbXFuMUVndzlva042T2pKUnViWk5YMUF3cGN5RFNOLTgwamhna0h5TnNuaUtpWnk4eWwwWk1qUXpzU0dqcmV2NVYtYU1LbEt0UkRvWm9BM0RueVNsRWo4UW9VRGNCM044THRmUjg?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxNbVQ3MXA0WFQ2dXNJbU1pV2V5MUE3dWF0Wnpva0prR1ZaZXlxamRNYWJNTXB4eHRQY0tqajU2TVp0eGZGWWRjMllvdDNRZkJhbkFXRWJxZnVwT05hVTdSWS1fcVZQaVlrXzlwMmlIekpyQ2NtaFZzY1R4V2k4aXlqeTN4Q21SUGh2bDlsRkhKUWEzN1RHOFBIYjdnTERzR0RZOC1UaDR0cmtWME1GMDBqUmpjQjMyUQ?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNb2dYUUpLYWRlZkRWMWFKOER0Ql9faEFrRm1ORUdrUGc5UVM5SGFUeXlKU1hIbDVrNXNWWmhLY21TSUM4UUpJeDEyWTh4WjFoQVhPN3J3bFJUMEhFZk81WnpkQTNNSGVqSlFXNVA1OTJYczFBY3hTN0JSc2loTEJtalE3ekVuVzZ4d0hKRHhEYW1yY2dWQlE?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPMkVxaW0xSHp4YTJQdTVZS1JCSEluQjF4VnJQUUR4dnp5V0tBVWpRc192cXJUM0RiMXBlTFg0X3ppSDB1M2lmZl9WSkRJMlpsWWp0eE9DeE9uX043UGpBOXVCZ000SndXQlJvNHZsbTk0MGtoT3ZsZ1NlM1hPRjBsclZrZmdGZE9IWmdUcTNCTQ?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxOR0tGMWxMSG42dHY0RGItTUhoZXZZek04Smg0T3dmTEhhUTQtVU1IVGcxMXY1OWxNVUNkT3dGbnQ2eHRwR3JSSGE3cTQ0WkhKYjhmWFhTRG5qUmY2S2dsQ0pLWEhIUGhiYl9GQjZXczg5S3Z0TEtnR1JtdF90X0dMb2J4d012Z0RzUkVOSllGalRFR21JVkR3dFBXbUEtMFEwdFVlLW5SQW05T2lwWFdPUnI4OE1VcUZMNmF2SlNkVWhpNXNRd0hzR1ZUVEk5NGlhZ1RNUNIB2gFBVV95cUxPb3VKWEplVC1yemx2ZENzZ25rNkp6aGpUNl9OdlN0QmlidXhtWW5IbTNIRzJzcEdzd3NOUEJzcXdSUWtyTkN2NGhkZkZOTlA5aFh1d2VBbnJFZl9MZHVnQmFOcTFhVlFsVEpPNktMR3dUdXdjWkFBWE1nQUJIeHk5d2NfUEJkM3Y5azVZX0lLaW8yZ1R0YVpBbFB3M0VwOUJhLWR0bzlPLWtXZGxQdlZtWm1IemFEQXVXVmx2RzlVZUZVZVZzbXdGNkw2UERkNkhGeHNEYUxRZTh2QQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
