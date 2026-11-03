# T Intelligence Report

- ticker: **T**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/T/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/T/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:26:01.716337+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 2, 'ai': 12, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **12** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/T** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **5**; {'directional_claim_without_event_type': 5}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 10 named publishers; 2 exact duplicates; 22 HTTPS source links; largest publisher share 31.82%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 21.4400 |
| Return 1D (%) | 0.1401 |
| Return 1W (%) | 2.8297 |
| Return 1M (%) | -10.7721 |
| Return YTD (%) | -9.5694 |
| Return 1Y (%) | -9.2406 |
| Annualized volatility (%) | 28.6768 |
| Beta vs SPY | -0.4388 |
| Max drawdown (%) | -28.8854 |
| Sharpe (rf=0) | -0.1646 |
| Downside deviation (rf=0, %) | 22.0083 |
| Sortino (rf=0) | -0.2145 |
| Historical VaR 95% (1D, %) | 2.8611 |
| Historical ES 95% (1D, %) | 4.6484 |
| Correlation vs SPY | -0.1962 |
| Tracking error vs SPY (%) | 33.6309 |
| P/E (trailing) | 11.47 |
| P/B | 1.36 |
| EV/EBITDA | 7.23 |
| Revenue growth (%) | 5.30 |
| Forward P/E (estimate) | 8.26 |
| Gross margin (%) | 59.74 |
| Operating margin (%) | 24.65 |
| Return on equity (%) | 11.61 |
| Free cash flow yield (%) | 8.28 |
| MA50 | 24.0879 |
| Close vs MA50 (%) | -10.9927 |
| MA200 | 24.4379 |
| Close vs MA200 (%) | -12.2674 |
| RSI (14, Wilder) | 38.9414 |
| MACD (12,26) | -0.8625 |
| MACD signal (9) | -0.7810 |
| MACD histogram | -0.0815 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'T': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 21.4400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.1401 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.8297 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -10.7721 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -9.5694 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -9.2406 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.6768 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.0083 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.2145 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8611 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6484 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1962 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.6309 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.4388 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.8854 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.1646 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.2595 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 59.7420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 24.6520 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.6130 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 8.2820 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 11.4652 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.9414 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0815 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -10.9927 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -12.2674 -> Clearly below the moving-average trend level.

## TAILWINDS

### AT&T (T) Stock Looks Cheap Relative To Its Earnings Outlook
- Summary: AT&T’s stock appears undervalued compared to earnings outlook.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQc1BkUDFaVkRUUEg5LTI4eVZuN3FOUEs2TFl4SmJEOERMRWV1RU9VNU5yVDZ0T25MTmliZVRxV0d2S05jMllRd0lRbFNjdHo3N1FLb1l5U2hLOHVQcVM0WXhOeUhjSkRWTVZmcWlSRDI5RjVNSlFnSXdLWHBlQ3NiZkpxMXZMMkk3VEZnaWZBaw?oc=5>

### Should You Buy AT&T Stock For Its Cash?
- Summary: AT&T’s cash holdings make it an attractive buy.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPTEZORThKcjZjV213ckw5R2dPNTFIMFA1d0kyV1FJX1pXR2R5NkZDQzdwbW0yQ0tXejlxd3J3Z2c0WEtMMzJIUmdIeDJDbnN1TjRtWVhZalpxNUJGTDZuMzdnT0RyLWk4dFJOeFRpaGxob3dVd0JyU01ibTdGVzZUamt5bzFZUl9Jd0NXV09JZUJjTG0tV0hvNUJKWQ?oc=5>

### T-Mobile Rallies 7% and SpaceX Falls 4% as Price Tag for Musk's Wireless Push Balloons; Verizon Rises 3%, AT&T Gains 2%
- Summary: AT&T stock rose 2% amid market rally, reflecting short‑term positive momentum.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxPcTdGZ3YtX2ZNN0pWTklOZ3JoUnJ1UmpVNU1BQVUxMEkza1I3R3Rtb05QczJVRzBCTmY1Y3l1eUM4Z3BUcjFtTXJwa0JRa1lhZXd1TmkzTGtoVTR4VHFPU29xdXRxdGUxYjlxSzJEU2JzRTdod1gxRG80Q041cUVwWHhMTnBRSjg5ZmtkZ0M2bTJ5QzlKTVlpNWlleWpTQkYyclBrYTF6QlNGU21aakVUUlpsX3pBcGZ0ZDNpeUs0SUxTd3pDYWtfWnNoeDI2QVVXTzItR2toXzJiNUhlLUxuMThiSm9ZTXBJdFA4?oc=5>

### AT&T: The SpaceX Panic Is A Gift (NYSE:T)
- Summary: SpaceX issues benefit AT&T amid panic.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxNXzU1S2c5UEFSSzJMbDIzSWZnb0F6V09vRjdqQVU3QVZ1YXkyV2J3SXhRZjZRY3BRajU1UGRSSERZbXFDNzBIZWhON21WUzRGQmoxV0FJWE1qYzZSRXJJSlByN1FEM1NRSlMtd0wwU2NhQ3hWWW0xek9HbWVJcXA4UEJB?oc=5>

### What Are AT&T Stock Bulls Not Worried About?
- Summary: Explores reasons investors remain bullish on AT&T despite market concerns.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNSXRWRW9oXy1xdXNnckFLLUJ1bGFZS1lTS282LTl3cGtnb0ZJMU1RWG42TlQxWFdac3hKM1hOeUxxTGN6ZERVNTNyYUhkWFo0VE5uaG9qRzlpSWQtY2JXRHhnUExueGs5a1F5LTFlSENsQVZkbm96UDRTaHQtUEdZSzkzazJCLWpPSTdwNW93eG5BaVJqbnowN2tXZmR5RFI0N2c?oc=5>

### AT&T Inc (T) Stock News Today
- Summary: Daily update on AT&T stock performance and recent news.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMidEFVX3lxTE5PMTRjblhqT2g0ZjZ6NTBqdGpveVl5S2dWZDZ1cTRUY1Fxc3dBbjV0NE42QnI0T1JUWXY3MWl4bWFiNTdPeUU5ZVVkTzZYV0lwcGxMRmlwdTB0c1IzdTJ3S1g5TXFsSXNoZ29WYlQzeVBRMWtU?oc=5>

### David Taylor buys AT&T, sells Marathon Petroleum stock
- Summary: Investor David Taylor shifts holdings to AT&T, selling Marathon Petroleum shares.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxPTUhYSW5PN2ZJZUlzX0hjNXhpMExxZm5ndU1MTTNmVEpMUGp3WTRiRmdTU2dORTQ2ay0zcHZmWHdia1ZLSzQ0V3gxbmdpRWJXQ01oaUxHM1BOdWJMMzZqckNzTnF3Z0ZmSnQydU4wQ3ptQ3RLWlYwUlZEZ044SEVQellYTjdyMmtUWjZXVTBoalhFM0FOTW95eDI5aHZycENFejZHam9oeWZOeWJMWFE?oc=5>

### What Just Happened To AT&T Stock?
- Summary: Examines recent movements in AT&T stock price and underlying factors.
- Date: 2026-10-26 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxNNDJMd2R3QkRqZ1U2dXMzT0VEMXEyVV9Ia1BCUDFvRk1OYy1GNV9HTWdqVlRXV3ZFd2tZSmRUT05PV1RoQ0JQTlBnZmJENC1TMUFxdGE2eW5nR2hSR2NqNkZHdzJ6aTNWZHJFS1RUM0dIa2hLZ3FWX2I4aFQ3UVBSNkhmSWJOZVVqcDJ3SjBnOA?oc=5>

### Do Wall Street Analysts Like AT&T Stock?
- Summary: Survey of analyst opinions and ratings on AT&T stock.
- Date: 2026-11-01 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNbHVYTElaajZTMFN3Uy11UExZcXM2bWtmT2FZLVprVkVjS3B4QndlbGluWDlabDBsbGNndGpZMmNFOVRYbVBRTVNHdDRXd25vLXp6NnlrMWlEYXp1VEpHUUI1Sm1GVEg2WVZiOXIydkFYcm5IQTBnVlZCRjhVLXRFRVdyMVpfT2NRMUlUWDRSMEFyWmwxcl9ibQ?oc=5>

## HEADWINDS

### AT&T’s Dividend Payments Fell 46%. Now It’s Spending Billions on Stock Buybacks
- Summary: AT&T’s Dividend Payments Fell 46%. Now It’s Spending Billions on Stock Buybacks
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOaDIyWHJGdlVQM2oyZG01Wi1KeDJxUVZucTVtNjBTM1JWb01UMWhyU2R1VWN2dUdGUHQyak9ieXFNdU5JRUZiT0hwTmZFbGtjY3I1UzNmajhRdUVQbVVyT1pZbkRpRW52alJUOHpHdFRTVmV6azJURGJuZkdjUzBCZlM4RUl2QlpIdFpuUW9fdVZjNTVJU2FN?oc=5>

### AT&T Shares Are Down 11% Since Earnings. Is the Stock a Buy?
- Summary: AT&T Shares Are Down 11% Since Earnings. Is the Stock a Buy?
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxPVDZCR3JLcW92cG85Z1g0My1SV3hUWVA2R1Z5S19ELTlpMlJGS3ppV1pqenhNdTFsaGFLTzE1T3d0VHYtaVQzeDVONVVlQVItd0pVWGZZaUlRQjMzUzFETENON3pZUmVUZVBFT1JrVzJ4VXB6dkQ5OFFYNVl0MjNlQ29HSFktTnVMVWZpUVpB?oc=5>

### AT&T: 80,000 Reasons To Worry (NYSE:T)
- Summary: AT&T faces widespread concerns, indicating potential operational or financial challenges.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTFA3NV9JQnhaTjM4SlJTN2VsaUd4MXZLUVpLUGc2NXcxM0RBUmxycGdSVjZ5c19RT2xCUktWTDdWYUZ2a3RTSmNrdUZZalBMRDlHUlhvb2gwT2lxdE8wTzktNDZ0ZHRrTUxfeU9vdTJSdUJ1emdUUlFxME51N00?oc=5>

## CATALYSTS

### This House of Representative Just Bought Up To $75K In AT&T Stock
- Summary: Rep purchase may signal confidence, acting as a catalyst for AT&T stock.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQZUlBRzlmSEF6YzlvZWd4M0cxSWdGV3ZqVzlheElJNTNmVXdFVmhpWV8xb181dWFBSmE0VHhNQThzVTJQWnRENWpTNlQxc21DRnQxcnpMLUhyd1E2ZzIxVVBHZ29rLUVVYkdiZmR2M0ttY2hMd0VtUUNXaUFqd1Y1UXo3a1dNR1RSWHR6TjJncUdDNUhBanVMeXpsQQ?oc=5>

## RISKS

### SpaceX Pursues Wireless Back Door After Verizon, T-Mobile, AT&T Reportedly Said No
- Summary: AT&T reportedly declined SpaceX's wireless back‑door proposal, potentially limiting future connectivity options.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxNQ2VOSUFlSE1OakItek1jYlQyM1ZjMDNTOTV4S2VTZE9OZzBFd3VkdkU4SzdzWHo1WjBHLUo0cTh3Zk5oLW5YcmNLaWg3U3UwZ0tQUVhOd1lwaGl4SzQyeHgxWWlSd2tJd2VLVDVUQzl4ajFDZ1R0X0tvRFN5WkJzaWhfMFdVSkdJZjk4NmVuQXFCNmx3T3hWdHNROW5RQmRObC1ZczhpWWpJa2pxR2NPSm1qUzY2dTZSZXV2MHNzOF9MTzJmb0FIWHZaeXBjZGtYLUNNbVU2NEZiYVE?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **T** | **11.47** | **1.36** | **7.23** | **5.30** | **144,429,989,888.00 USD** | **-9.24** |
| VZ | 11.49 | 1.76 | 7.27 | 1.50 | 186,714,144,768.00 USD | 20.91 |
| TMUS | 15.44 | 3.02 | 8.00 | 7.40 | 169,642,491,904.00 USD | -22.15 |
| BCE | 4.18 | 1.31 | 7.37 | 1.50 | 19,275,309,056.00 USD | -4.73 |

Peers fetched as_of: 2026-11-02; T reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 32,322,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 891,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/732717/000073271726000372/t-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMijwFBVV95cUxQc1BkUDFaVkRUUEg5LTI4eVZuN3FOUEs2TFl4SmJEOERMRWV1RU9VNU5yVDZ0T25MTmliZVRxV0d2S05jMllRd0lRbFNjdHo3N1FLb1l5U2hLOHVQcVM0WXhOeUhjSkRWTVZmcWlSRDI5RjVNSlFnSXdLWHBlQ3NiZkpxMXZMMkk3VEZnaWZBaw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPTEZORThKcjZjV213ckw5R2dPNTFIMFA1d0kyV1FJX1pXR2R5NkZDQzdwbW0yQ0tXejlxd3J3Z2c0WEtMMzJIUmdIeDJDbnN1TjRtWVhZalpxNUJGTDZuMzdnT0RyLWk4dFJOeFRpaGxob3dVd0JyU01ibTdGVzZUamt5bzFZUl9Jd0NXV09JZUJjTG0tV0hvNUJKWQ?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxPcTdGZ3YtX2ZNN0pWTklOZ3JoUnJ1UmpVNU1BQVUxMEkza1I3R3Rtb05QczJVRzBCTmY1Y3l1eUM4Z3BUcjFtTXJwa0JRa1lhZXd1TmkzTGtoVTR4VHFPU29xdXRxdGUxYjlxSzJEU2JzRTdod1gxRG80Q041cUVwWHhMTnBRSjg5ZmtkZ0M2bTJ5QzlKTVlpNWlleWpTQkYyclBrYTF6QlNGU21aakVUUlpsX3pBcGZ0ZDNpeUs0SUxTd3pDYWtfWnNoeDI2QVVXTzItR2toXzJiNUhlLUxuMThiSm9ZTXBJdFA4?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxNXzU1S2c5UEFSSzJMbDIzSWZnb0F6V09vRjdqQVU3QVZ1YXkyV2J3SXhRZjZRY3BRajU1UGRSSERZbXFDNzBIZWhON21WUzRGQmoxV0FJWE1qYzZSRXJJSlByN1FEM1NRSlMtd0wwU2NhQ3hWWW0xek9HbWVJcXA4UEJB?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNSXRWRW9oXy1xdXNnckFLLUJ1bGFZS1lTS282LTl3cGtnb0ZJMU1RWG42TlQxWFdac3hKM1hOeUxxTGN6ZERVNTNyYUhkWFo0VE5uaG9qRzlpSWQtY2JXRHhnUExueGs5a1F5LTFlSENsQVZkbm96UDRTaHQtUEdZSzkzazJCLWpPSTdwNW93eG5BaVJqbnowN2tXZmR5RFI0N2c?oc=5
- https://news.google.com/rss/articles/CBMidEFVX3lxTE5PMTRjblhqT2g0ZjZ6NTBqdGpveVl5S2dWZDZ1cTRUY1Fxc3dBbjV0NE42QnI0T1JUWXY3MWl4bWFiNTdPeUU5ZVVkTzZYV0lwcGxMRmlwdTB0c1IzdTJ3S1g5TXFsSXNoZ29WYlQzeVBRMWtU?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPTUhYSW5PN2ZJZUlzX0hjNXhpMExxZm5ndU1MTTNmVEpMUGp3WTRiRmdTU2dORTQ2ay0zcHZmWHdia1ZLSzQ0V3gxbmdpRWJXQ01oaUxHM1BOdWJMMzZqckNzTnF3Z0ZmSnQydU4wQ3ptQ3RLWlYwUlZEZ044SEVQellYTjdyMmtUWjZXVTBoalhFM0FOTW95eDI5aHZycENFejZHam9oeWZOeWJMWFE?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNNDJMd2R3QkRqZ1U2dXMzT0VEMXEyVV9Ia1BCUDFvRk1OYy1GNV9HTWdqVlRXV3ZFd2tZSmRUT05PV1RoQ0JQTlBnZmJENC1TMUFxdGE2eW5nR2hSR2NqNkZHdzJ6aTNWZHJFS1RUM0dIa2hLZ3FWX2I4aFQ3UVBSNkhmSWJOZVVqcDJ3SjBnOA?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNbHVYTElaajZTMFN3Uy11UExZcXM2bWtmT2FZLVprVkVjS3B4QndlbGluWDlabDBsbGNndGpZMmNFOVRYbVBRTVNHdDRXd25vLXp6NnlrMWlEYXp1VEpHUUI1Sm1GVEg2WVZiOXIydkFYcm5IQTBnVlZCRjhVLXRFRVdyMVpfT2NRMUlUWDRSMEFyWmwxcl9ibQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOaDIyWHJGdlVQM2oyZG01Wi1KeDJxUVZucTVtNjBTM1JWb01UMWhyU2R1VWN2dUdGUHQyak9ieXFNdU5JRUZiT0hwTmZFbGtjY3I1UzNmajhRdUVQbVVyT1pZbkRpRW52alJUOHpHdFRTVmV6azJURGJuZkdjUzBCZlM4RUl2QlpIdFpuUW9fdVZjNTVJU2FN?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPdlRDV1VqY053eU9fTFZVSWZRSnh1QndUc25rNENFWmlFVnJYcmFmc0d1dUtaQ0FKcmxHZmg3SnBCTEtXUkZUdDVCMTQ0Q21MMXZZM3Qxa243NUQ5c3o0X25zNzFRbjhaa0pXb2hSaDlkSFV3ZlNrTFJRZWlIOEl4emlGbkFPU0htZk1uWnplRjFLUTdfNU4wMW5jcGttS2RYam02djdTTmozdDFkSVhoZy13aVAzMjBiMHc?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPVDZCR3JLcW92cG85Z1g0My1SV3hUWVA2R1Z5S19ELTlpMlJGS3ppV1pqenhNdTFsaGFLTzE1T3d0VHYtaVQzeDVONVVlQVItd0pVWGZZaUlRQjMzUzFETENON3pZUmVUZVBFT1JrVzJ4VXB6dkQ5OFFYNVl0MjNlQ29HSFktTnVMVWZpUVpB?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTFA3NV9JQnhaTjM4SlJTN2VsaUd4MXZLUVpLUGc2NXcxM0RBUmxycGdSVjZ5c19RT2xCUktWTDdWYUZ2a3RTSmNrdUZZalBMRDlHUlhvb2gwT2lxdE8wTzktNDZ0ZHRrTUxfeU9vdTJSdUJ1emdUUlFxME51N00?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQZUlBRzlmSEF6YzlvZWd4M0cxSWdGV3ZqVzlheElJNTNmVXdFVmhpWV8xb181dWFBSmE0VHhNQThzVTJQWnRENWpTNlQxc21DRnQxcnpMLUhyd1E2ZzIxVVBHZ29rLUVVYkdiZmR2M0ttY2hMd0VtUUNXaUFqd1Y1UXo3a1dNR1RSWHR6TjJncUdDNUhBanVMeXpsQQ?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxNQ2VOSUFlSE1OakItek1jYlQyM1ZjMDNTOTV4S2VTZE9OZzBFd3VkdkU4SzdzWHo1WjBHLUo0cTh3Zk5oLW5YcmNLaWg3U3UwZ0tQUVhOd1lwaGl4SzQyeHgxWWlSd2tJd2VLVDVUQzl4ajFDZ1R0X0tvRFN5WkJzaWhfMFdVSkdJZjk4NmVuQXFCNmx3T3hWdHNROW5RQmRObC1ZczhpWWpJa2pxR2NPSm1qUzY2dTZSZXV2MHNzOF9MTzJmb0FIWHZaeXBjZGtYLUNNbVU2NEZiYVE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
