# META Intelligence Report

- ticker: **META**
- Report as_of: **2026-10-27**
- Market data as_of: **2026-10-27**
- Quant sources: https://finance.yahoo.com/quote/META/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/META/key-statistics/
- AI analysis snapshot as_of: **2026-10-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-28T02:01:18.673766+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 20, 'rule': 6, 'ai': 11, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261027T014607Z-b66f6bd5/META** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 20 unique headlines; 14 named publishers; 5 exact duplicates; 20 HTTPS source links; largest publisher share 30.0%; oldest publication 2026-10-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 620.1900 |
| Return 1D (%) | -1.6446 |
| Return 1W (%) | -10.6676 |
| Return 1M (%) | -17.4906 |
| Return YTD (%) | -5.8028 |
| Return 1Y (%) | -17.1181 |
| Annualized volatility (%) | 42.7243 |
| Beta vs SPY | 1.5067 |
| Max drawdown (%) | -29.9428 |
| Sharpe (rf=0) | -0.2285 |
| Downside deviation (rf=0, %) | 29.7353 |
| Sortino (rf=0) | -0.3284 |
| Historical VaR 95% (1D, %) | 3.7761 |
| Historical ES 95% (1D, %) | 6.2110 |
| Correlation vs SPY | 0.4479 |
| Tracking error vs SPY (%) | 38.7372 |
| P/E (trailing) | 21.16 |
| P/B | 5.82 |
| EV/EBITDA | 13.92 |
| Revenue growth (%) | 26.10 |
| Forward P/E (estimate) | 17.64 |
| Gross margin (%) | 81.03 |
| Operating margin (%) | 35.41 |
| Return on equity (%) | 32.26 |
| Free cash flow yield (%) | 1.06 |
| MA50 | 665.4335 |
| Close vs MA50 (%) | -6.7991 |
| MA200 | 631.4340 |
| Close vs MA200 (%) | -1.7807 |
| RSI (14, Wilder) | 31.9449 |
| MACD (12,26) | -11.8384 |
| MACD signal (9) | 4.4235 |
| MACD histogram | -16.2619 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'META': 269, 'SPY': 269}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 620.1900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.6446 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -10.6676 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -17.4906 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -5.8028 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -17.1181 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 42.7243 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 29.7353 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.3284 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.7761 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.2110 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4479 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 38.7372 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.5067 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -29.9428 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.2285 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.6441 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.0340 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 35.4140 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.2640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0625 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.1597 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 31.9449 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -16.2619 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -6.7991 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -1.7807 -> Slightly below the moving-average trend level.

## TAILWINDS

### Meta Stock Falls On Plan For $95 Billion Equity Raise. Analysts Are Offering A Positive View.
- Summary: Meta Stock Falls On Plan For $95 Billion Equity Raise. Analysts Are Offering A Positive View.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxQRVNaVzVKMV9fbDV0TlVybC05NnZsay1zWEc3ZDBtbDVBVWxuYkltbE9DSmRVY2RsR2Z3RTJaREF1MWZ6ZWhfeVdxTHVhdV9PYS1zRG1LVGplM1ViYnBVbEZmUVhoTHh5cFduaWhkbG51SEhVaXd6OVIybjc5ekI4Z1Nrbw?oc=5>

### Meta Platforms: Muse May Be Metaverse 2.0, But It’s Too Late (NASDAQ:META)
- Summary: Meta’s Muse platform aims to revitalize its metaverse vision, though critics question its timeliness and competitive edge.
- Date: 2026-10-26 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQU1U5NGk4c1k0U0Jfa2hBQUZmaVVFcndyNmQ5bUxXdmhVbjBDMWhnNy1SdDFvckd0cmxDOW9LY09hQ3EwTlpHRE9Ha2gwdnBEVHJrUWJJdFdDckk0a0lGeHE2RVFCS09leGI0czFWbHQ1VFc0d2dSR0dDZml0N1F5YXE4QWoxS2xDRlg0RWVQcjNkYzNNSUdMUWgxclJFbUk?oc=5>

### Meta Will Offer Up to $95 Billion in Stock. What That Means for Its Big AI Push.
- Summary: Meta plans a $95B stock issuance to fund AI initiatives, potentially diluting shares but boosting capital for growth.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE10bm9vdXZ0RDJuVWNfMGo5bnQtLTJ6b2c3WTlMNExXaEsyOUpiNEd0cGt0YVNldlZHNEtvaThTOXV3LUpBVEFmcmNOOTBSZDNPbTBmNGlFVzgwYkFqQmY2eExVUjR6UEEtNk1hNzdkWEgtTWs2bTZNbGl2a0hOUQ?oc=5>

### Meta Is Creating a New Class of Stock. What Shareholders Need to Know
- Summary: Meta introduces a new stock class, affecting shareholder rights and voting power, signaling strategic capital structure changes.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNbFdZaW9qLV9QZGhYMXMzT1dHM0pvVEl1V3BGaGtJa0JCMDRrb0lRckJhc1d5ejR5eDk0WkhrRzV3VjF6UXRmand6TXM0ek53bjZya2h0aUFYMjR6dlZGdWFQcHRRejMxdHVBN3NjS0JHME1hWjJfeE5RLWV3SW5MRmt2ZmFxOGFUQWRGaXFwVnRuMUtLNzE0Q1lvVUt5WGJyX2YyMWlZUktndkhkdmlsanln?oc=5>

### Why You Should Buy Meta Stock Before It Touches $1,050
- Summary: Analyst urges buying Meta shares pre-$1,050, citing undervaluation and growth prospects in AI and metaverse.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNWHd0bEhHMmtQdnlmTEpiXy1fZVhjRW1HV2FLcy11R2RaUGFwdjdLbVpPcmtldkROcS1hSEFuX3FYTDVHM2VBd3BsUU12UGthNUFDa2FZWnk3RzZsNDBtTzlKbEgteXU2Mk5YSmVqejQtNm9hLTZZeEw1RkRfNm9ScG5oUXJjVlhPd0UyNEoycTVqWDVVd0E?oc=5>

### Nvidia, AMD to buy $4B in Meta shares as part of expanded chip partnerships
- Summary: Meta partners with Nvidia and AMD, buying $4B in shares to strengthen chip collaboration.
- Date: 2026-10-27 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQbzNoNElDckgyajBzR3NPZ0tkQ2taREVmc3p1NHZFZDBDT0dPY1NQa29vZElHZGhsQUcxQ2wxV1BGaDVpLXJTSjluQ0hNWWE5U1A1R3Ezc2lkTWZ5X3ZzU1VxV29CM0txQmFFT2xrdUg1bFUzaFV3bDAya2FkMFdBVjh1dEp6ZmZXZEZkWWpNRmY3eHNyVGs0dWNvUHplZWVLZzhZQng3cDdkRklKWjlJ?oc=5>

### 3 Reasons to Buy Meta Platforms Stock Before 2027
- Summary: Analyst highlights potential upside for Meta stock through 2027.
- Date: 2026-10-27 | Impact: medium | Horizon: long | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPMXlMR0xiQVpuM094aTVfdGd6NWlsMmpVV3VEQUY0ODI5VWd6SGpQR2tRNjM4SkMzOWtiNkt3Q2s4ZHNGdmJTM3ZudGM1a3FQTkdhay1veFhMYmhwXzBHTkVqSHo1c08ybXNMMDl1OGhSQ3o4S1p4MEtYZ0Z4empWSjZYSmYyLWdwZ2NndDE5Z285MUVla1FB?oc=5>

## HEADWINDS

### Meta Stock Has Dropped the Day After 3 Straight Earnings Reports. Is It a Buy Now?
- Summary: Meta Stock Has Dropped the Day After 3 Straight Earnings Reports. Is It a Buy Now?
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNeklvb08xd1ZtTzkySTRZbVhLZzY2QzMyRTI4dFk5ZmlYdGx6Z1JsS21pZWl4SEVpTXBPYWJLaU5LYmhVbTFuMUxRR0wwSXhzTlZmWDN2TC1yb3BYRHNJRXVmY0gtNmtNMTVpbU84WXI4S0E4Snc5Vk8wcDBxelZOOG5pTmpfbURqZ0dVczN4OGtreFU?oc=5>

### Meta Platforms Stock Falls Despite Posting Strong Q3 Numbers. Should Investors Buy the Dip?
- Summary: Meta Platforms Stock Falls Despite Posting Strong Q3 Numbers. Should Investors Buy the Dip?
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOOWZYUTZlenV1VWkzZ3pTYkE4bTNnVGZkeUhReW96LVIxWnZZMmM5WmROdVVMRjJIM1hLelRMbXYwSTRLNU1uLTNCYnJLOHNZVV8zZGJ1R3RNQmtyV240bUItUkhXV0JWLTVwbDRKUUZlYXpmWEE5NnZIRy1ucUNmUUhkaGxMX1g0NnNTNlhQQlJSb3lhbGx5dzhEN2tJdy1u?oc=5>

### Meta Stock Sell-Off Looks Like an Overreaction
- Summary: Meta shares fell sharply, seen as overreaction to market fears.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxQcHJtRUdQWm1ocmFuMnFtMTU0Zzc4WE9QTWZVSWllaWVaejhGQW13ZTZRMjZrWmt5Qm1LS1BackpkNXdqT1ozbTlEUzNJUS02X3RhZGs4cjJNT1lyMUhVaVRHX3RFdm1vcFNYSkREUEFNblQwR01KdDFSazNIMDRYUkVB?oc=5>

### Meta stock closes out Friday down as AI spending fears continue to rattle markets
- Summary: Meta shares closed lower amid AI spending concerns.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxNOVBsWC1HZmNiRnJHT3RIbzlmcmZLZVpRVVlibk5sMFhyLUJfSHVtZlhxNzBLWkJ6RkgtWWprZnl2ZUVCeVBzb3NOVzlJQkYwbjBvVzQtaFZDSk9rZGxlYWVjMEJnWFY0LVFiUVM0S2J1T0ExVTJMcFY4QjJ1ZDgwNVVrVEpENFpJMHVrRkpoVXJvSTktOE9fMU94dnpLR1UxWWlSTFVHallWRG1DTDBhNXJobzJpek5UeTk3dUFRZl9QMnJhaGo1OXo3TUhSeEg0LTVQeHZiZ0NuZw?oc=5>

## CATALYSTS

### Meta Announces Launch of Offering of Depositary Shares Representing Series A Mandatory Convertible Preferred Stock and Offering of Class A Common Stock in Connection with Forward Sale Agreements
- Summary: Meta Announces Launch of Offering of Depositary Shares Representing Series A Mandatory Convertible Preferred Stock and Offering of Class A Common Stock in Connection with Forward Sale Agreements
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijANBVV95cUxON0lNaXV6RThzZ0ltRF9MS3VXbHJpTkdETG81Y2toYkd5QXN2NUVhX3BiSnNkVWhhUU1sNzdMV1RIS1lNSm44Z05LdmZiWk42WlB4OGE2YUZZSlRIX3ZQN3ByNUVrYmFBdWFnLVBwUUNqMW14bllLZnV0OTB2WG9CMHlBWXl6SUhZWnYyU1lmdHBNNm41dDVzb2RESnFuNElWallZa2ZMamtpc3lLNms3N2VyOUxpZjl0QlZ6UzRORkpadGJ1bTV0NG5NaERaNDdTc0NFSVExWVREaHFMaGZzOFU5bFZ2anl4aFRHaW5BdjBNbzdKU01NM211OHFubTlGV2stRHJBdlVjYlRSeUVLMnE3TGpNaU9Ya2FScjJyWlBRUnd6Z0xZdUR5djdQb2ZDQkVsZUkzSEw1d1V1SzNIcXBweTBvMVRIRmNTd0JFcWhsMlZhczJlVFkxcnhNMkVER0JqQU10Tm9JQzVZU3BkM1lFWVZEaXVYYnJ2Z3FCQW9DQks4TWZmbUQyWFg?oc=5>

### Meta Platforms, Inc. $META Stock: Obermeyer Wealth Partners Increases Holdings
- Summary: Meta Platforms, Inc. $META Stock: Obermeyer Wealth Partners Increases Holdings
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxPVTNwam9TX2MwTG1rM2t5aEhISkVaVTVlem9SMkhDRnIxX3R6SWg3VldhWm5WekdIcFk0VWd6cGZ4UjNkN3VpY3ExVkJBOGIwSTBSVXptZG9XX1lYQjJTaWlsSXQ2VnI1R0RfVno2OHZmdzBNLTkxUmxBblp2ckt0N2dPSlRpSnRPS2N4REhKejVUM0tmcTlUc3ZGanhnaWw1MHhENDNmdko5UXl3MDIzalUtemxMd0Q5QjZWUkhiMjNVa3dkdTYwLXF4NEVRS3Rr?oc=5>

### Meta Launches $35B Stock Offering, Plans Another $60B Program In 2027: Nvidia, AMD, Broadcom Eye Up To $5B Investment
- Summary: Meta Launches $35B Stock Offering, Plans Another $60B Program In 2027: Nvidia, AMD, Broadcom Eye Up To $5B Investment
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPRUZTaHN0QlFyYk9uM1pRZWtkcWV4T19femtzQ3FwWXpGQnhDZDh0WFdQUU1EREtESlhjeUVKRUpfTkxfUjVhVGFFNFFnSUJ6NEc4RWNoUkJqZ19WdlNUNDZMb3U3N3RKUzZKa24zaTd0dkM0R0VLdThfUThyM1lIU2NOdlRXSHJTVXJyeUxfS1AtUnZqaVotNElVakI2QQ?oc=5>

### Meta’s $25 Billion Stock Sale Ended Five Times Oversubscribed
- Summary: Meta completed a $25B stock sale, oversubscribed five times, signaling strong investor demand.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNdmR1WjllZWo5S013MU1kTmgzNWdZXzd3ejl4bHZFRlR6NUpLbWt5aHdaYkpzc3g4eG55M0Q2UGVHb01oSHBIUWZyY0tzTHNzMlU2clZ6NVFoZmJ3clRtYkZLWHFsWElfRHRibEw0UkZYMUNtQzNQcFVtejBQUjM4QVh6Yk9LdVMzOENZU1U3S0syTWRxSU9zdmFkQUlLY2hVQkFtVlFrN3lseGhEcWNPdA?oc=5>

### AMD To Invest $1B In Meta Stock Offering As AI Partnership Expands — Helios Systems Now Running At Meta
- Summary: AMD invests $1B in Meta's stock offering, reinforcing AI partnership and Helios system deployment.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPMVZONEsxU01Pa2dLUzZQWFFrM0VMQzJLWFQ1UzVkNW5zS0VIeDNCUDFYbmZMSWVnODBFWkJhLWVfWGNabFlTWEpicjYxcjItbHV5OE9pMkp2dzBKLUh3dFdGT0c5V19wWTBXQmVUQ3doNGRwa3BqalozWUx0M0lsVE9vdERua2Q1aGN2VWZzaVc3Zw?oc=5>

### Meta eyes record $97.5 billion equity raise to fund AI expansion
- Summary: Meta plans a record $97.5B equity raise to fund AI expansion, indicating aggressive growth strategy.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPclhjOFJvYkM0S0hLUmxaY0l2X3hCdWI0N1prZlo2QXhXdmt5T0pNQVpFODVpYzgycWdZcHM2NkZ2LTdaMEVUVlpTXzVFUzc2ZEdVdlpTeThUVkZtc3V4cEFTelk5bDd2Z0dfRDFsb0dGQ0MxRXhYMExFZTlXVkNjRXF6TDBLalZ5ZTFBbFMyX24wMVBTQW1GQkJNRjNYWTRiVGJJWWdialBfV1oyQUZNN3I4RQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **META** | **21.16** | **5.82** | **13.92** | **26.10** | **1,585,722,294,272.00 USD** | **-17.12** |
| GOOGL | 16.09 | 6.30 | 22.04 | 24.20 | 3,920,672,325,632.00 USD | 19.36 |
| SNAP | N/A | 5.31 | -81.00 | 18.90 | 10,282,481,664.00 USD | -23.14 |
| PINS | 60.53 | 4.02 | 36.57 | 18.20 | 11,654,721,536.00 USD | -41.60 |

Peers fetched as_of: 2026-10-27; META reuses existing data (market data as_of: 2026-10-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-27

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
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQU1U5NGk4c1k0U0Jfa2hBQUZmaVVFcndyNmQ5bUxXdmhVbjBDMWhnNy1SdDFvckd0cmxDOW9LY09hQ3EwTlpHRE9Ha2gwdnBEVHJrUWJJdFdDckk0a0lGeHE2RVFCS09leGI0czFWbHQ1VFc0d2dSR0dDZml0N1F5YXE4QWoxS2xDRlg0RWVQcjNkYzNNSUdMUWgxclJFbUk?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE10bm9vdXZ0RDJuVWNfMGo5bnQtLTJ6b2c3WTlMNExXaEsyOUpiNEd0cGt0YVNldlZHNEtvaThTOXV3LUpBVEFmcmNOOTBSZDNPbTBmNGlFVzgwYkFqQmY2eExVUjR6UEEtNk1hNzdkWEgtTWs2bTZNbGl2a0hOUQ?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNbFdZaW9qLV9QZGhYMXMzT1dHM0pvVEl1V3BGaGtJa0JCMDRrb0lRckJhc1d5ejR5eDk0WkhrRzV3VjF6UXRmand6TXM0ek53bjZya2h0aUFYMjR6dlZGdWFQcHRRejMxdHVBN3NjS0JHME1hWjJfeE5RLWV3SW5MRmt2ZmFxOGFUQWRGaXFwVnRuMUtLNzE0Q1lvVUt5WGJyX2YyMWlZUktndkhkdmlsanln?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPeFFUWkhxYlJNc3labzFqU1hldXAwd3A4VHB0Wl9heUZ4d21vQnc0bWVoSVBwNlZiOERENjBTekYwODFoSk5uRGozUjdRQjdCd0JZLXpLSGplbjIxX1psNXBUY2NPeGZWM2FqemJBdU9LcHE0TTQyS1Q5TkY4OTZuUHUyVHdNRGlqRXZ2V3pvR2ZHaDR0d3pmR3Z5cS05eDFJVDBYcnVn?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNWHd0bEhHMmtQdnlmTEpiXy1fZVhjRW1HV2FLcy11R2RaUGFwdjdLbVpPcmtldkROcS1hSEFuX3FYTDVHM2VBd3BsUU12UGthNUFDa2FZWnk3RzZsNDBtTzlKbEgteXU2Mk5YSmVqejQtNm9hLTZZeEw1RkRfNm9ScG5oUXJjVlhPd0UyNEoycTVqWDVVd0E?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQbzNoNElDckgyajBzR3NPZ0tkQ2taREVmc3p1NHZFZDBDT0dPY1NQa29vZElHZGhsQUcxQ2wxV1BGaDVpLXJTSjluQ0hNWWE5U1A1R3Ezc2lkTWZ5X3ZzU1VxV29CM0txQmFFT2xrdUg1bFUzaFV3bDAya2FkMFdBVjh1dEp6ZmZXZEZkWWpNRmY3eHNyVGs0dWNvUHplZWVLZzhZQng3cDdkRklKWjlJ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPMXlMR0xiQVpuM094aTVfdGd6NWlsMmpVV3VEQUY0ODI5VWd6SGpQR2tRNjM4SkMzOWtiNkt3Q2s4ZHNGdmJTM3ZudGM1a3FQTkdhay1veFhMYmhwXzBHTkVqSHo1c08ybXNMMDl1OGhSQ3o4S1p4MEtYZ0Z4empWSjZYSmYyLWdwZ2NndDE5Z285MUVla1FB?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNbDFJTkVkVk9jU3VmNkFzSGdjY1Y5QVN2TUtTcERHMUlIM0NCV2lBeFZxY1R6NVZrR2pqSks2ZVRXMFFHeUdzb05qcVVpb0RVNFozLW4xendvYVlhc0dJNjdjb0lJV0x3NVdPNWNQMkhrdUxkcENZMF9zWGVmTllWZ3VjVFZJQnNOOS1kYWxQOU9lT3NkS3lhSg?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNeklvb08xd1ZtTzkySTRZbVhLZzY2QzMyRTI4dFk5ZmlYdGx6Z1JsS21pZWl4SEVpTXBPYWJLaU5LYmhVbTFuMUxRR0wwSXhzTlZmWDN2TC1yb3BYRHNJRXVmY0gtNmtNMTVpbU84WXI4S0E4Snc5Vk8wcDBxelZOOG5pTmpfbURqZ0dVczN4OGtreFU?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNamJrMEYxSG9NeTJWRVlfMjdWWS1veVlyS19zZlVicFJCVng5WTdmQ2wybEZnVjl2dkJoOTB5U3VROGhENnZITmNobklfdGtFRGlPeWlocUFldUlZbG1TQTRLQnpKVUNVTXNSXzMxdjVPZnhCd2RHLVBBcUptOHpsbnhDSXZENHhBdmFwMHItZjJfYk9xdTBBWDVhbVVBSVczaDNCZF8xMFJGOEtSVVJPa1NhczVld3JRdFNGYmw2Yno?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOOWZYUTZlenV1VWkzZ3pTYkE4bTNnVGZkeUhReW96LVIxWnZZMmM5WmROdVVMRjJIM1hLelRMbXYwSTRLNU1uLTNCYnJLOHNZVV8zZGJ1R3RNQmtyV240bUItUkhXV0JWLTVwbDRKUUZlYXpmWEE5NnZIRy1ucUNmUUhkaGxMX1g0NnNTNlhQQlJSb3lhbGx5dzhEN2tJdy1u?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNQmhialNHNjhOVUdScy1kQnJ5eHg4WnptZEhmN3RGb1FGWF82emxEVTFaa1lHeURwalI2SEZpb0E1ay1RTXFjazBweGhQTEFpdEZjTjNkMjhrT0pvMmtSTWU0Tl9JSWtKaDlFNlRlNnRuYXVOZG1ObjBVcC14ZlFDcVBSMEJzNERXNjBnTFJmT3AzWmc0eFlhdm1vU3R4MGRJQWFCcExFb3hyb0lqckJBQncxRVEtekZLTFQyeEdCaEFSeVpwUjEyMVR4UXE?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxQcHJtRUdQWm1ocmFuMnFtMTU0Zzc4WE9QTWZVSWllaWVaejhGQW13ZTZRMjZrWmt5Qm1LS1BackpkNXdqT1ozbTlEUzNJUS02X3RhZGs4cjJNT1lyMUhVaVRHX3RFdm1vcFNYSkREUEFNblQwR01KdDFSazNIMDRYUkVB?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxNOVBsWC1HZmNiRnJHT3RIbzlmcmZLZVpRVVlibk5sMFhyLUJfSHVtZlhxNzBLWkJ6RkgtWWprZnl2ZUVCeVBzb3NOVzlJQkYwbjBvVzQtaFZDSk9rZGxlYWVjMEJnWFY0LVFiUVM0S2J1T0ExVTJMcFY4QjJ1ZDgwNVVrVEpENFpJMHVrRkpoVXJvSTktOE9fMU94dnpLR1UxWWlSTFVHallWRG1DTDBhNXJobzJpek5UeTk3dUFRZl9QMnJhaGo1OXo3TUhSeEg0LTVQeHZiZ0NuZw?oc=5
- https://news.google.com/rss/articles/CBMijANBVV95cUxON0lNaXV6RThzZ0ltRF9MS3VXbHJpTkdETG81Y2toYkd5QXN2NUVhX3BiSnNkVWhhUU1sNzdMV1RIS1lNSm44Z05LdmZiWk42WlB4OGE2YUZZSlRIX3ZQN3ByNUVrYmFBdWFnLVBwUUNqMW14bllLZnV0OTB2WG9CMHlBWXl6SUhZWnYyU1lmdHBNNm41dDVzb2RESnFuNElWallZa2ZMamtpc3lLNms3N2VyOUxpZjl0QlZ6UzRORkpadGJ1bTV0NG5NaERaNDdTc0NFSVExWVREaHFMaGZzOFU5bFZ2anl4aFRHaW5BdjBNbzdKU01NM211OHFubTlGV2stRHJBdlVjYlRSeUVLMnE3TGpNaU9Ya2FScjJyWlBRUnd6Z0xZdUR5djdQb2ZDQkVsZUkzSEw1d1V1SzNIcXBweTBvMVRIRmNTd0JFcWhsMlZhczJlVFkxcnhNMkVER0JqQU10Tm9JQzVZU3BkM1lFWVZEaXVYYnJ2Z3FCQW9DQks4TWZmbUQyWFg?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxPVTNwam9TX2MwTG1rM2t5aEhISkVaVTVlem9SMkhDRnIxX3R6SWg3VldhWm5WekdIcFk0VWd6cGZ4UjNkN3VpY3ExVkJBOGIwSTBSVXptZG9XX1lYQjJTaWlsSXQ2VnI1R0RfVno2OHZmdzBNLTkxUmxBblp2ckt0N2dPSlRpSnRPS2N4REhKejVUM0tmcTlUc3ZGanhnaWw1MHhENDNmdko5UXl3MDIzalUtemxMd0Q5QjZWUkhiMjNVa3dkdTYwLXF4NEVRS3Rr?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPRUZTaHN0QlFyYk9uM1pRZWtkcWV4T19femtzQ3FwWXpGQnhDZDh0WFdQUU1EREtESlhjeUVKRUpfTkxfUjVhVGFFNFFnSUJ6NEc4RWNoUkJqZ19WdlNUNDZMb3U3N3RKUzZKa24zaTd0dkM0R0VLdThfUThyM1lIU2NOdlRXSHJTVXJyeUxfS1AtUnZqaVotNElVakI2QQ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNdmR1WjllZWo5S013MU1kTmgzNWdZXzd3ejl4bHZFRlR6NUpLbWt5aHdaYkpzc3g4eG55M0Q2UGVHb01oSHBIUWZyY0tzTHNzMlU2clZ6NVFoZmJ3clRtYkZLWHFsWElfRHRibEw0UkZYMUNtQzNQcFVtejBQUjM4QVh6Yk9LdVMzOENZU1U3S0syTWRxSU9zdmFkQUlLY2hVQkFtVlFrN3lseGhEcWNPdA?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPMVZONEsxU01Pa2dLUzZQWFFrM0VMQzJLWFQ1UzVkNW5zS0VIeDNCUDFYbmZMSWVnODBFWkJhLWVfWGNabFlTWEpicjYxcjItbHV5OE9pMkp2dzBKLUh3dFdGT0c5V19wWTBXQmVUQ3doNGRwa3BqalozWUx0M0lsVE9vdERua2Q1aGN2VWZzaVc3Zw?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxPclhjOFJvYkM0S0hLUmxaY0l2X3hCdWI0N1prZlo2QXhXdmt5T0pNQVpFODVpYzgycWdZcHM2NkZ2LTdaMEVUVlpTXzVFUzc2ZEdVdlpTeThUVkZtc3V4cEFTelk5bDd2Z0dfRDFsb0dGQ0MxRXhYMExFZTlXVkNjRXF6TDBLalZ5ZTFBbFMyX24wMVBTQW1GQkJNRjNYWTRiVGJJWWdialBfV1oyQUZNN3I4RQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
