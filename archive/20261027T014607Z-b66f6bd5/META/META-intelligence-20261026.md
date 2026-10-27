# META Intelligence Report

- ticker: **META**
- Report as_of: **2026-10-26**
- Market data as_of: **2026-10-26**
- Quant sources: https://finance.yahoo.com/quote/META/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/META/key-statistics/
- AI analysis snapshot as_of: **2026-10-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-27T02:07:09.329206+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 9, 'ai': 12, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261026T005504Z-6368ad31/META** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 16 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-10-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 630.5600 |
| Return 1D (%) | -1.8767 |
| Return 1W (%) | -10.6147 |
| Return 1M (%) | -16.1110 |
| Return YTD (%) | -4.2277 |
| Return 1Y (%) | -14.3102 |
| Annualized volatility (%) | 42.7794 |
| Beta vs SPY | 1.5143 |
| Max drawdown (%) | -29.9428 |
| Sharpe (rf=0) | -0.1904 |
| Downside deviation (rf=0, %) | 29.7489 |
| Sortino (rf=0) | -0.2738 |
| Historical VaR 95% (1D, %) | 3.7819 |
| Historical ES 95% (1D, %) | 6.2110 |
| Correlation vs SPY | 0.4501 |
| Tracking error vs SPY (%) | 38.7564 |
| P/E (trailing) | 21.51 |
| P/B | 5.92 |
| EV/EBITDA | 14.15 |
| Revenue growth (%) | 26.10 |
| Forward P/E (estimate) | 17.97 |
| Gross margin (%) | 81.03 |
| Operating margin (%) | 35.41 |
| Return on equity (%) | 32.26 |
| Free cash flow yield (%) | 1.05 |
| MA50 | 664.4002 |
| Close vs MA50 (%) | -5.0933 |
| MA200 | 631.5900 |
| Close vs MA200 (%) | -0.1631 |
| RSI (14, Wilder) | 33.6707 |
| MACD (12,26) | -7.0572 |
| MACD signal (9) | 8.4889 |
| MACD histogram | -15.5461 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'META': 268, 'SPY': 268}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 630.5600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.8767 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -10.6147 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -16.1110 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -4.2277 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -14.3102 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 42.7794 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 29.7489 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.2738 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.7819 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.2110 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4501 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 38.7564 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.5143 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -29.9428 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.1904 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.9683 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.0340 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 35.4140 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.2640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0489 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.5135 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 33.6707 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -15.5461 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.0933 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -0.1631 -> Slightly below the moving-average trend level.

## TAILWINDS

### Meta Stock Falls On Plan For $95 Billion Equity Raise. Analysts Are Offering A Positive View.
- Summary: Meta Stock Falls On Plan For $95 Billion Equity Raise. Analysts Are Offering A Positive View.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxQRVNaVzVKMV9fbDV0TlVybC05NnZsay1zWEc3ZDBtbDVBVWxuYkltbE9DSmRVY2RsR2Z3RTJaREF1MWZ6ZWhfeVdxTHVhdV9PYS1zRG1LVGplM1ViYnBVbEZmUVhoTHh5cFduaWhkbG51SEhVaXd6OVIybjc5ekI4Z1Nrbw?oc=5>

### Meta Will Offer Up to $95 Billion in Stock. What That Means for Its Big AI Push.
- Summary: Meta plans a $95B stock issuance to fund AI initiatives, potentially diluting shares but boosting capital for growth.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE10bm9vdXZ0RDJuVWNfMGo5bnQtLTJ6b2c3WTlMNExXaEsyOUpiNEd0cGt0YVNldlZHNEtvaThTOXV3LUpBVEFmcmNOOTBSZDNPbTBmNGlFVzgwYkFqQmY2eExVUjR6UEEtNk1hNzdkWEgtTWs2bTZNbGl2a0hOUQ?oc=5>

### Meta Is Creating a New Class of Stock. What Shareholders Need to Know
- Summary: Meta introduces a new stock class, affecting shareholder rights and voting power, signaling strategic capital structure changes.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNbFdZaW9qLV9QZGhYMXMzT1dHM0pvVEl1V3BGaGtJa0JCMDRrb0lRckJhc1d5ejR5eDk0WkhrRzV3VjF6UXRmand6TXM0ek53bjZya2h0aUFYMjR6dlZGdWFQcHRRejMxdHVBN3NjS0JHME1hWjJfeE5RLWV3SW5MRmt2ZmFxOGFUQWRGaXFwVnRuMUtLNzE0Q1lvVUt5WGJyX2YyMWlZUktndkhkdmlsanln?oc=5>

### Meta Platforms: Muse May Be Metaverse 2.0, But It’s Too Late (NASDAQ:META)
- Summary: Meta’s Muse platform aims to revitalize its metaverse vision, though critics question its timeliness and competitive edge.
- Date: 2026-10-26 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQU1U5NGk4c1k0U0Jfa2hBQUZmaVVFcndyNmQ5bUxXdmhVbjBDMWhnNy1SdDFvckd0cmxDOW9LY09hQ3EwTlpHRE9Ha2gwdnBEVHJrUWJJdFdDckk0a0lGeHE2RVFCS09leGI0czFWbHQ1VFc0d2dSR0dDZml0N1F5YXE4QWoxS2xDRlg0RWVQcjNkYzNNSUdMUWgxclJFbUk?oc=5>

### Why You Should Buy Meta Stock Before It Touches $1,050
- Summary: Analyst urges buying Meta shares pre-$1,050, citing undervaluation and growth prospects in AI and metaverse.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNWHd0bEhHMmtQdnlmTEpiXy1fZVhjRW1HV2FLcy11R2RaUGFwdjdLbVpPcmtldkROcS1hSEFuX3FYTDVHM2VBd3BsUU12UGthNUFDa2FZWnk3RzZsNDBtTzlKbEgteXU2Mk5YSmVqejQtNm9hLTZZeEw1RkRfNm9ScG5oUXJjVlhPd0UyNEoycTVqWDVVd0E?oc=5>

### 1 Reason to Buy Meta Stock Now and Hold for the Long Term
- Summary: Investor highlights a single long-term catalyst for Meta, encouraging current and prospective shareholders to hold.
- Date: 2026-10-26 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPTzBZX0dJYlE3NTlTRlcyNi1yQ19raVpJR2RScE41VzRLTVp2SzFMT211Z3I0cVl3R0tBcjM1djh6YmZqaHhlLXRWUGdZMUlMelNkdUJpZENXZkRjaEhHMFVsakszUHpIWUhtV3ktRjl1RkUtbk8tcUFVU1VONnVxV2x0aWJUTWNzSnRxRA?oc=5>

### Meta eyes record $95 billion equity raise to fund AI expansion
- Summary: Meta plans a $95B equity raise to fund AI expansion.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPclhjOFJvYkM0S0hLUmxaY0l2X3hCdWI0N1prZlo2QXhXdmt5T0pNQVpFODVpYzgycWdZcHM2NkZ2LTdaMEVUVlpTXzVFUzc2ZEdVdlpTeThUVkZtc3V4cEFTelk5bDd2Z0dfRDFsb0dGQ0MxRXhYMExFZTlXVkNjRXF6TDBLalZ5ZTFBbFMyX24wMVBTQW1GQkJNRjNYWTRiVGJJWWdialBfV1oyQUZNN3I4RQ?oc=5>

## HEADWINDS

### Meta Stock Has Dropped the Day After 3 Straight Earnings Reports. Is It a Buy Now?
- Summary: Meta Stock Has Dropped the Day After 3 Straight Earnings Reports. Is It a Buy Now?
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNamJrMEYxSG9NeTJWRVlfMjdWWS1veVlyS19zZlVicFJCVng5WTdmQ2wybEZnVjl2dkJoOTB5U3VROGhENnZITmNobklfdGtFRGlPeWlocUFldUlZbG1TQTRLQnpKVUNVTXNSXzMxdjVPZnhCd2RHLVBBcUptOHpsbnhDSXZENHhBdmFwMHItZjJfYk9xdTBBWDVhbVVBSVczaDNCZF8xMFJGOEtSVVJPa1NhczVld3JRdFNGYmw2Yno?oc=5>

### Meta Platforms (NASDAQ:META) Stock Price Down 1.9% - Here's Why
- Summary: Meta Platforms (NASDAQ:META) Stock Price Down 1.9% - Here's Why
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxOYTFfSGJYY05LMjBNTVNBdmFoa3FseFlnMGtpNVhodDRfXzJzQ1QyUUU2RjQ4WFBVUnp6UE5VaGtIXzNsMWNmdHJicXlZeEs5Q3I1TjNGdE1rd1V6bGtMX2ZNMnZwTEkyLWF2X01ZY3gtTzBLWnI2TDZXSm9MQnBvaWNRSFAtaldrMEdaNEZkYllzbEhKQXd1WjExMlBsckVPYlZDR2l5ZlBKU0h0UmtlN1lkcUtIdUk?oc=5>

### Meta stock drops more than 7% despite strong Q3 results as AI spending fears return
- Summary: Meta stock drops more than 7% despite strong Q3 results as AI spending fears return
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxNOVBsWC1HZmNiRnJHT3RIbzlmcmZLZVpRVVlibk5sMFhyLUJfSHVtZlhxNzBLWkJ6RkgtWWprZnl2ZUVCeVBzb3NOVzlJQkYwbjBvVzQtaFZDSk9rZGxlYWVjMEJnWFY0LVFiUVM0S2J1T0ExVTJMcFY4QjJ1ZDgwNVVrVEpENFpJMHVrRkpoVXJvSTktOE9fMU94dnpLR1UxWWlSTFVHallWRG1DTDBhNXJobzJpek5UeTk3dUFRZl9QMnJhaGo1OXo3TUhSeEg0LTVQeHZiZ0NuZw?oc=5>

### Meta Stock Falls. Earnings Show Just How Much Future Growth Will Cost.
- Summary: Meta Stock Falls. Earnings Show Just How Much Future Growth Will Cost.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTE4tdTM5U2kwQ295eEpWaTdjamk4SDdmT09TWjFBNHBhZkRxcmR6SmpNT1lEbTZGZTl0LVZpYUxXUERlOEtsaWdFLXF2QTFSUG9LM0RjbkZyR21YR1dlNmN2NnhvTWFqanY4Q09IYjBqT29SOHBGeWxrZg?oc=5>

## CATALYSTS

### Meta Announces Launch of Offering of Depositary Shares Representing Series A Mandatory Convertible Preferred Stock and Offering of Class A Common Stock in Connection with Forward Sale Agreements
- Summary: Meta Announces Launch of Offering of Depositary Shares Representing Series A Mandatory Convertible Preferred Stock and Offering of Class A Common Stock in Connection with Forward Sale Agreements
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijANBVV95cUxON0lNaXV6RThzZ0ltRF9MS3VXbHJpTkdETG81Y2toYkd5QXN2NUVhX3BiSnNkVWhhUU1sNzdMV1RIS1lNSm44Z05LdmZiWk42WlB4OGE2YUZZSlRIX3ZQN3ByNUVrYmFBdWFnLVBwUUNqMW14bllLZnV0OTB2WG9CMHlBWXl6SUhZWnYyU1lmdHBNNm41dDVzb2RESnFuNElWallZa2ZMamtpc3lLNms3N2VyOUxpZjl0QlZ6UzRORkpadGJ1bTV0NG5NaERaNDdTc0NFSVExWVREaHFMaGZzOFU5bFZ2anl4aFRHaW5BdjBNbzdKU01NM211OHFubTlGV2stRHJBdlVjYlRSeUVLMnE3TGpNaU9Ya2FScjJyWlBRUnd6Z0xZdUR5djdQb2ZDQkVsZUkzSEw1d1V1SzNIcXBweTBvMVRIRmNTd0JFcWhsMlZhczJlVFkxcnhNMkVER0JqQU10Tm9JQzVZU3BkM1lFWVZEaXVYYnJ2Z3FCQW9DQks4TWZmbUQyWFg?oc=5>

### Meta Launches $35B Stock Offering, Plans Another $60B Program In 2027: Nvidia, AMD, Broadcom Eye Up To $5B Investment
- Summary: Meta Launches $35B Stock Offering, Plans Another $60B Program In 2027: Nvidia, AMD, Broadcom Eye Up To $5B Investment
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPRUZTaHN0QlFyYk9uM1pRZWtkcWV4T19femtzQ3FwWXpGQnhDZDh0WFdQUU1EREtESlhjeUVKRUpfTkxfUjVhVGFFNFFnSUJ6NEc4RWNoUkJqZ19WdlNUNDZMb3U3N3RKUzZKa24zaTd0dkM0R0VLdThfUThyM1lIU2NOdlRXSHJTVXJyeUxfS1AtUnZqaVotNElVakI2QQ?oc=5>

### Meta Platforms, Inc. (META) Launches $22.5B Common Stock Offering And Preferred Issue
- Summary: Meta Platforms, Inc. (META) Launches $22.5B Common Stock Offering And Preferred Issue
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxQZTZ5bjJiT3BLTlBsblpLWjV5SmZlXzRKRDJkRTQxWVFhUlI5RHJwUExjWFVWRVAybVVqYXN0ZUI2SkdFT1pQVkNzTDNSVGN2bzlXbTEzcmo5SGxUelNJeklpejZucDgyeTdLMlRsbkJrQUR3ME5HSU11cUFfdkV6bE1LcERRM1ZQRDNfeWluV1B1Q3JiM3htTm5GOTJmZEZIQ1EzbHpsUWRKemlXemhYQlNfUGl3OExpSVpHN0pOUElhVmR0UVZPMlJTa0o0WksxTFJhd3hlTjJfZw?oc=5>

### Meta Plans What Amounts to a 2-for-1 Stock Split. Is the Stock a Buy?
- Summary: Meta Plans What Amounts to a 2-for-1 Stock Split. Is the Stock a Buy?
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxNSjVHa0NBOElLQ0tPaHpYOXhvN2MwU3cxNU4xZ0NndG9QMlBRVVNOY1A4RzdMcEtEaGxiQWhOZWMtV1NURmVhRkVhYUVlTUNRT1VoY1NvUld5R040LVpwNXF0MWZDR0w4ZGpFR2FHbXg1MXA5RmJiTWJ5YVFDam5RX0wtbXNMNFhwZy12NFNzQkwwcmM0VDJVN015a1NJZ1NrX0loaG5OWFRmVHV5QnI0?oc=5>

### Bank of America revamps Meta stock price target once again
- Summary: Bank of America updates Meta price target.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPZ3Y4UTVnSVh3bGc5c1FkNUwwc1ZibllGZklVLXFrVDd6Q1RUVVRqNk9pb1RKTVFQaDNMeXpPMTYzek56MFpwbi1sVWlEMkR0akVWcFAxcWVKSk5oeVlaVzlXNlNqZGZiNzdteHhQOHRxOURDMkNjWmJ4UzlEUEpyeTR6NWhxdkZENmxVeHVjYVlaejhIdGhKR2hiRjdNNTIyOTk4?oc=5>

### What Is Meta Platforms (META) Telling Investors With Its Sundial Deal And New Stock?
- Summary: Meta announces a partnership with Sundial, potentially expanding its platform services and attracting new investors.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxQellpUEtWaVd5djc3TllEamtxdENZMlFLQnBsanVmZjlpeTRWSjVpTEtzUDRkbzhSVHE5Y2hPQ3ViS0ZtSDZveUNnTHU0RC1jY3hKUEYxbGd1NzRjbWZFal8zR0FUZy1uczROcmVna2dqY2wtdl9lSlA2bE9adk95T01NVV9HbWdxWWpUWkdYc280cmRMY1YweGZKWjRzZTY4bkFpNA?oc=5>

### What the New Class C Share Structure Actually Means for Meta Platforms Stock Investors
- Summary: New Class C shares affect investor ownership structure.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQcFljUHJ1VDNsd0ZCOWwtYUdTRWhfdkRyaVVWZXl3ejVOMHRNRnJON0NGd3RwU1Q4ZFhKcllMNlF3MTdOMzQzbWFQUjM4ZEpRMzRPdF9iUkF5cEZvUUltSEQ2bVg1Nms1bkxKNFBFX1FSNEo0T2pGTFpFUml4enk3bFk1TURBdm1oTF9tTDBINlEyQ052TUhtOElDVHdSZw?oc=5>

### Here’s How Much Meta Stock Is Expected to Move After Earnings
- Summary: Analysts forecast post-earnings price movement for Meta shares.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNNDlGN05oelNLdkV4ZXJWRFVsZl80RDlnVFBhY044cjFTNEc5a3ZoU2NVeFdmejZYQTlZMXFQdm9POU5mcFlEcmhCLVhFZ2NDN3dFM1hrU2Zmdm42NlVGNTZWTE95YnF0ZlBjSzMyM2FqelpxR0ljMXZHYjF4THRCcEMwaTNDRUpvdlR2UndBanpMa0dVSGtTaWZWUFJVNEpCQ1NhLWdNaTR3SGpLNlBpZVdzb0UxVWdy?oc=5>

### Meta plans $95bn stock offering to bankroll AI expansion
- Summary: Meta plans $95bn stock offering to fund AI expansion.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxQaUtNaHFNcWhwbXByd1BLYTlMcjgxN1A4M1RpVHQtT0JJTWp5SG9sZm5uQlJIaURJME1ZOVY5ZThyTVdPcW5TbTlRWXhNcU0yb3hXMjl6dzRMMnZXNm9sOUluMFdaY19rNlFMVWRmNEQ5WUs2ZDlNSDAzUnZ5S1Z3V0g2aDI?oc=5>

### Meta Plans up to $95 Billion in Financing to Power Its AI Growth
- Summary: Meta announces a $95B financing plan to boost AI initiatives, signaling strong investment in future growth.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxOWWVJZlJtQjJkZTMyWV9zMXNqV3RxZERPOE1CZlliQTVqR3VaTFk5anp5bHViM0pVTlVlc3lmMTU2YzVkb01hRXVsYU9yWUVFWjJxVHlrbW5TRVZoMWw3SzM1VUZ3UmpZN1NRODBhZmpHQXI4OXFCZDI5dWpMOGlTcGlWblREUUhmWHRCLWtZeW9zcnNUMVlRa2JTN0pwZ2dkSXBKQS14emotVmM1LWMtb2RxMEF5Y3RqNHBFZndn?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **META** | **21.51** | **5.92** | **14.15** | **26.10** | **1,606,355,517,440.00 USD** | **-14.31** |
| GOOGL | 15.90 | 6.22 | 21.78 | 24.20 | 3,874,443,231,232.00 USD | 22.20 |
| SNAP | N/A | 5.53 | -84.00 | 18.90 | 10,722,193,408.00 USD | -20.25 |
| PINS | 62.44 | 4.15 | 37.73 | 18.20 | 12,022,824,960.00 USD | -37.50 |

Peers fetched as_of: 2026-10-26; META reuses existing data (market data as_of: 2026-10-26); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

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
- Filing date: 2026-10-22
- Revenue (latest available single quarter): 13,727,000,000.00 USD; period 2018-07-01/2018-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 9,860,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMigwFBVV95cUxQRVNaVzVKMV9fbDV0TlVybC05NnZsay1zWEc3ZDBtbDVBVWxuYkltbE9DSmRVY2RsR2Z3RTJaREF1MWZ6ZWhfeVdxTHVhdV9PYS1zRG1LVGplM1ViYnBVbEZmUVhoTHh5cFduaWhkbG51SEhVaXd6OVIybjc5ekI4Z1Nrbw?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE10bm9vdXZ0RDJuVWNfMGo5bnQtLTJ6b2c3WTlMNExXaEsyOUpiNEd0cGt0YVNldlZHNEtvaThTOXV3LUpBVEFmcmNOOTBSZDNPbTBmNGlFVzgwYkFqQmY2eExVUjR6UEEtNk1hNzdkWEgtTWs2bTZNbGl2a0hOUQ?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNbFdZaW9qLV9QZGhYMXMzT1dHM0pvVEl1V3BGaGtJa0JCMDRrb0lRckJhc1d5ejR5eDk0WkhrRzV3VjF6UXRmand6TXM0ek53bjZya2h0aUFYMjR6dlZGdWFQcHRRejMxdHVBN3NjS0JHME1hWjJfeE5RLWV3SW5MRmt2ZmFxOGFUQWRGaXFwVnRuMUtLNzE0Q1lvVUt5WGJyX2YyMWlZUktndkhkdmlsanln?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQU1U5NGk4c1k0U0Jfa2hBQUZmaVVFcndyNmQ5bUxXdmhVbjBDMWhnNy1SdDFvckd0cmxDOW9LY09hQ3EwTlpHRE9Ha2gwdnBEVHJrUWJJdFdDckk0a0lGeHE2RVFCS09leGI0czFWbHQ1VFc0d2dSR0dDZml0N1F5YXE4QWoxS2xDRlg0RWVQcjNkYzNNSUdMUWgxclJFbUk?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNWHd0bEhHMmtQdnlmTEpiXy1fZVhjRW1HV2FLcy11R2RaUGFwdjdLbVpPcmtldkROcS1hSEFuX3FYTDVHM2VBd3BsUU12UGthNUFDa2FZWnk3RzZsNDBtTzlKbEgteXU2Mk5YSmVqejQtNm9hLTZZeEw1RkRfNm9ScG5oUXJjVlhPd0UyNEoycTVqWDVVd0E?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPTzBZX0dJYlE3NTlTRlcyNi1yQ19raVpJR2RScE41VzRLTVp2SzFMT211Z3I0cVl3R0tBcjM1djh6YmZqaHhlLXRWUGdZMUlMelNkdUJpZENXZkRjaEhHMFVsakszUHpIWUhtV3ktRjl1RkUtbk8tcUFVU1VONnVxV2x0aWJUTWNzSnRxRA?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxPclhjOFJvYkM0S0hLUmxaY0l2X3hCdWI0N1prZlo2QXhXdmt5T0pNQVpFODVpYzgycWdZcHM2NkZ2LTdaMEVUVlpTXzVFUzc2ZEdVdlpTeThUVkZtc3V4cEFTelk5bDd2Z0dfRDFsb0dGQ0MxRXhYMExFZTlXVkNjRXF6TDBLalZ5ZTFBbFMyX24wMVBTQW1GQkJNRjNYWTRiVGJJWWdialBfV1oyQUZNN3I4RQ?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNamJrMEYxSG9NeTJWRVlfMjdWWS1veVlyS19zZlVicFJCVng5WTdmQ2wybEZnVjl2dkJoOTB5U3VROGhENnZITmNobklfdGtFRGlPeWlocUFldUlZbG1TQTRLQnpKVUNVTXNSXzMxdjVPZnhCd2RHLVBBcUptOHpsbnhDSXZENHhBdmFwMHItZjJfYk9xdTBBWDVhbVVBSVczaDNCZF8xMFJGOEtSVVJPa1NhczVld3JRdFNGYmw2Yno?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNeklvb08xd1ZtTzkySTRZbVhLZzY2QzMyRTI4dFk5ZmlYdGx6Z1JsS21pZWl4SEVpTXBPYWJLaU5LYmhVbTFuMUxRR0wwSXhzTlZmWDN2TC1yb3BYRHNJRXVmY0gtNmtNMTVpbU84WXI4S0E4Snc5Vk8wcDBxelZOOG5pTmpfbURqZ0dVczN4OGtreFU?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxOYTFfSGJYY05LMjBNTVNBdmFoa3FseFlnMGtpNVhodDRfXzJzQ1QyUUU2RjQ4WFBVUnp6UE5VaGtIXzNsMWNmdHJicXlZeEs5Q3I1TjNGdE1rd1V6bGtMX2ZNMnZwTEkyLWF2X01ZY3gtTzBLWnI2TDZXSm9MQnBvaWNRSFAtaldrMEdaNEZkYllzbEhKQXd1WjExMlBsckVPYlZDR2l5ZlBKU0h0UmtlN1lkcUtIdUk?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxNOVBsWC1HZmNiRnJHT3RIbzlmcmZLZVpRVVlibk5sMFhyLUJfSHVtZlhxNzBLWkJ6RkgtWWprZnl2ZUVCeVBzb3NOVzlJQkYwbjBvVzQtaFZDSk9rZGxlYWVjMEJnWFY0LVFiUVM0S2J1T0ExVTJMcFY4QjJ1ZDgwNVVrVEpENFpJMHVrRkpoVXJvSTktOE9fMU94dnpLR1UxWWlSTFVHallWRG1DTDBhNXJobzJpek5UeTk3dUFRZl9QMnJhaGo1OXo3TUhSeEg0LTVQeHZiZ0NuZw?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTE4tdTM5U2kwQ295eEpWaTdjamk4SDdmT09TWjFBNHBhZkRxcmR6SmpNT1lEbTZGZTl0LVZpYUxXUERlOEtsaWdFLXF2QTFSUG9LM0RjbkZyR21YR1dlNmN2NnhvTWFqanY4Q09IYjBqT29SOHBGeWxrZg?oc=5
- https://news.google.com/rss/articles/CBMijANBVV95cUxON0lNaXV6RThzZ0ltRF9MS3VXbHJpTkdETG81Y2toYkd5QXN2NUVhX3BiSnNkVWhhUU1sNzdMV1RIS1lNSm44Z05LdmZiWk42WlB4OGE2YUZZSlRIX3ZQN3ByNUVrYmFBdWFnLVBwUUNqMW14bllLZnV0OTB2WG9CMHlBWXl6SUhZWnYyU1lmdHBNNm41dDVzb2RESnFuNElWallZa2ZMamtpc3lLNms3N2VyOUxpZjl0QlZ6UzRORkpadGJ1bTV0NG5NaERaNDdTc0NFSVExWVREaHFMaGZzOFU5bFZ2anl4aFRHaW5BdjBNbzdKU01NM211OHFubTlGV2stRHJBdlVjYlRSeUVLMnE3TGpNaU9Ya2FScjJyWlBRUnd6Z0xZdUR5djdQb2ZDQkVsZUkzSEw1d1V1SzNIcXBweTBvMVRIRmNTd0JFcWhsMlZhczJlVFkxcnhNMkVER0JqQU10Tm9JQzVZU3BkM1lFWVZEaXVYYnJ2Z3FCQW9DQks4TWZmbUQyWFg?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPRUZTaHN0QlFyYk9uM1pRZWtkcWV4T19femtzQ3FwWXpGQnhDZDh0WFdQUU1EREtESlhjeUVKRUpfTkxfUjVhVGFFNFFnSUJ6NEc4RWNoUkJqZ19WdlNUNDZMb3U3N3RKUzZKa24zaTd0dkM0R0VLdThfUThyM1lIU2NOdlRXSHJTVXJyeUxfS1AtUnZqaVotNElVakI2QQ?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxQZTZ5bjJiT3BLTlBsblpLWjV5SmZlXzRKRDJkRTQxWVFhUlI5RHJwUExjWFVWRVAybVVqYXN0ZUI2SkdFT1pQVkNzTDNSVGN2bzlXbTEzcmo5SGxUelNJeklpejZucDgyeTdLMlRsbkJrQUR3ME5HSU11cUFfdkV6bE1LcERRM1ZQRDNfeWluV1B1Q3JiM3htTm5GOTJmZEZIQ1EzbHpsUWRKemlXemhYQlNfUGl3OExpSVpHN0pOUElhVmR0UVZPMlJTa0o0WksxTFJhd3hlTjJfZw?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxNSjVHa0NBOElLQ0tPaHpYOXhvN2MwU3cxNU4xZ0NndG9QMlBRVVNOY1A4RzdMcEtEaGxiQWhOZWMtV1NURmVhRkVhYUVlTUNRT1VoY1NvUld5R040LVpwNXF0MWZDR0w4ZGpFR2FHbXg1MXA5RmJiTWJ5YVFDam5RX0wtbXNMNFhwZy12NFNzQkwwcmM0VDJVN015a1NJZ1NrX0loaG5OWFRmVHV5QnI0?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPZ3Y4UTVnSVh3bGc5c1FkNUwwc1ZibllGZklVLXFrVDd6Q1RUVVRqNk9pb1RKTVFQaDNMeXpPMTYzek56MFpwbi1sVWlEMkR0akVWcFAxcWVKSk5oeVlaVzlXNlNqZGZiNzdteHhQOHRxOURDMkNjWmJ4UzlEUEpyeTR6NWhxdkZENmxVeHVjYVlaejhIdGhKR2hiRjdNNTIyOTk4?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxQellpUEtWaVd5djc3TllEamtxdENZMlFLQnBsanVmZjlpeTRWSjVpTEtzUDRkbzhSVHE5Y2hPQ3ViS0ZtSDZveUNnTHU0RC1jY3hKUEYxbGd1NzRjbWZFal8zR0FUZy1uczROcmVna2dqY2wtdl9lSlA2bE9adk95T01NVV9HbWdxWWpUWkdYc280cmRMY1YweGZKWjRzZTY4bkFpNA?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQcFljUHJ1VDNsd0ZCOWwtYUdTRWhfdkRyaVVWZXl3ejVOMHRNRnJON0NGd3RwU1Q4ZFhKcllMNlF3MTdOMzQzbWFQUjM4ZEpRMzRPdF9iUkF5cEZvUUltSEQ2bVg1Nms1bkxKNFBFX1FSNEo0T2pGTFpFUml4enk3bFk1TURBdm1oTF9tTDBINlEyQ052TUhtOElDVHdSZw?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNNDlGN05oelNLdkV4ZXJWRFVsZl80RDlnVFBhY044cjFTNEc5a3ZoU2NVeFdmejZYQTlZMXFQdm9POU5mcFlEcmhCLVhFZ2NDN3dFM1hrU2Zmdm42NlVGNTZWTE95YnF0ZlBjSzMyM2FqelpxR0ljMXZHYjF4THRCcEMwaTNDRUpvdlR2UndBanpMa0dVSGtTaWZWUFJVNEpCQ1NhLWdNaTR3SGpLNlBpZVdzb0UxVWdy?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxQaUtNaHFNcWhwbXByd1BLYTlMcjgxN1A4M1RpVHQtT0JJTWp5SG9sZm5uQlJIaURJME1ZOVY5ZThyTVdPcW5TbTlRWXhNcU0yb3hXMjl6dzRMMnZXNm9sOUluMFdaY19rNlFMVWRmNEQ5WUs2ZDlNSDAzUnZ5S1Z3V0g2aDI?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxOWWVJZlJtQjJkZTMyWV9zMXNqV3RxZERPOE1CZlliQTVqR3VaTFk5anp5bHViM0pVTlVlc3lmMTU2YzVkb01hRXVsYU9yWUVFWjJxVHlrbW5TRVZoMWw3SzM1VUZ3UmpZN1NRODBhZmpHQXI4OXFCZDI5dWpMOGlTcGlWblREUUhmWHRCLWtZeW9zcnNUMVlRa2JTN0pwZ2dkSXBKQS14emotVmM1LWMtb2RxMEF5Y3RqNHBFZndn?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
