# T Intelligence Report

- ticker: **T**
- Report as_of: **2026-11-03**
- Market data as_of: **2026-11-03**
- Quant sources: https://finance.yahoo.com/quote/T/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/T/key-statistics/
- AI analysis snapshot as_of: **2026-11-03**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-04T04:46:48.866239+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 9, 'ai': 10, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261103T051441Z-8b1c85d8/T** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'directional_claim_without_event_type': 3}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 11 named publishers; 1 exact duplicates; 22 HTTPS source links; largest publisher share 31.82%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 21.3900 |
| Return 1D (%) | -0.2332 |
| Return 1W (%) | 2.1490 |
| Return 1M (%) | -10.9802 |
| Return YTD (%) | -9.7803 |
| Return 1Y (%) | -8.6401 |
| Annualized volatility (%) | 28.6202 |
| Beta vs SPY | -0.4390 |
| Max drawdown (%) | -28.8854 |
| Sharpe (rf=0) | -0.1725 |
| Downside deviation (rf=0, %) | 21.9656 |
| Sortino (rf=0) | -0.2247 |
| Historical VaR 95% (1D, %) | 2.8546 |
| Historical ES 95% (1D, %) | 4.6484 |
| Correlation vs SPY | -0.1963 |
| Tracking error vs SPY (%) | 33.5668 |
| P/E (trailing) | 11.44 |
| P/B | 1.35 |
| EV/EBITDA | 7.22 |
| Revenue growth (%) | 5.30 |
| Forward P/E (estimate) | 8.24 |
| Gross margin (%) | 59.74 |
| Operating margin (%) | 24.65 |
| Return on equity (%) | 11.61 |
| Free cash flow yield (%) | 8.30 |
| MA50 | 24.0076 |
| Close vs MA50 (%) | -10.9034 |
| MA200 | 24.4314 |
| Close vs MA200 (%) | -12.4488 |
| RSI (14, Wilder) | 38.5880 |
| MACD (12,26) | -0.8265 |
| MACD signal (9) | -0.7901 |
| MACD histogram | -0.0364 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'T': 274, 'SPY': 274}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 21.3900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.2332 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.1490 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -10.9802 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -9.7803 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -8.6401 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.6202 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.9656 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.2247 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8546 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6484 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1963 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.5668 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.4390 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.8854 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.1725 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.2402 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 59.7420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 24.6520 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.6130 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 8.3014 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 11.4385 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.5880 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0364 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -10.9034 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -12.4488 -> Clearly below the moving-average trend level.

## TAILWINDS

### What Are AT&T Stock Bulls Not Worried About?
- Summary: Explores reasons investors remain bullish on AT&T despite market concerns.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNSXRWRW9oXy1xdXNnckFLLUJ1bGFZS1lTS282LTl3cGtnb0ZJMU1RWG42TlQxWFdac3hKM1hOeUxxTGN6ZERVNTNyYUhkWFo0VE5uaG9qRzlpSWQtY2JXRHhnUExueGs5a1F5LTFlSENsQVZkbm96UDRTaHQtUEdZSzkzazJCLWpPSTdwNW93eG5BaVJqbnowN2tXZmR5RFI0N2c?oc=5>

### Do Wall Street Analysts Like AT&T Stock?
- Summary: Survey of analyst opinions and ratings on AT&T stock.
- Date: 2026-11-01 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNbHVYTElaajZTMFN3Uy11UExZcXM2bWtmT2FZLVprVkVjS3B4QndlbGluWDlabDBsbGNndGpZMmNFOVRYbVBRTVNHdDRXd25vLXp6NnlrMWlEYXp1VEpHUUI1Sm1GVEg2WVZiOXIydkFYcm5IQTBnVlZCRjhVLXRFRVdyMVpfT2NRMUlUWDRSMEFyWmwxcl9ibQ?oc=5>

### AT&T (T) Stock Looks Cheap Relative To Its Earnings Outlook
- Summary: AT&T’s stock appears undervalued compared to earnings outlook.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQc1BkUDFaVkRUUEg5LTI4eVZuN3FOUEs2TFl4SmJEOERMRWV1RU9VNU5yVDZ0T25MTmliZVRxV0d2S05jMllRd0lRbFNjdHo3N1FLb1l5U2hLOHVQcVM0WXhOeUhjSkRWTVZmcWlSRDI5RjVNSlFnSXdLWHBlQ3NiZkpxMXZMMkk3VEZnaWZBaw?oc=5>

### AT&T Inc (T) Stock News Today
- Summary: Daily update on AT&T stock performance and recent news.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMidEFVX3lxTE5PMTRjblhqT2g0ZjZ6NTBqdGpveVl5S2dWZDZ1cTRUY1Fxc3dBbjV0NE42QnI0T1JUWXY3MWl4bWFiNTdPeUU5ZVVkTzZYV0lwcGxMRmlwdTB0c1IzdTJ3S1g5TXFsSXNoZ29WYlQzeVBRMWtU?oc=5>

### Should You Buy AT&T Stock For Its Cash?
- Summary: AT&T’s cash holdings make it an attractive buy.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPTEZORThKcjZjV213ckw5R2dPNTFIMFA1d0kyV1FJX1pXR2R5NkZDQzdwbW0yQ0tXejlxd3J3Z2c0WEtMMzJIUmdIeDJDbnN1TjRtWVhZalpxNUJGTDZuMzdnT0RyLWk4dFJOeFRpaGxob3dVd0JyU01ibTdGVzZUamt5bzFZUl9Jd0NXV09JZUJjTG0tV0hvNUJKWQ?oc=5>

### T-Mobile Rallies 7% and SpaceX Falls 4% as Price Tag for Musk's Wireless Push Balloons; Verizon Rises 3%, AT&T Gains 2%
- Summary: AT&T stock rose 2% amid market rally, reflecting short‑term positive momentum.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxPcTdGZ3YtX2ZNN0pWTklOZ3JoUnJ1UmpVNU1BQVUxMEkza1I3R3Rtb05QczJVRzBCTmY1Y3l1eUM4Z3BUcjFtTXJwa0JRa1lhZXd1TmkzTGtoVTR4VHFPU29xdXRxdGUxYjlxSzJEU2JzRTdod1gxRG80Q041cUVwWHhMTnBRSjg5ZmtkZ0M2bTJ5QzlKTVlpNWlleWpTQkYyclBrYTF6QlNGU21aakVUUlpsX3pBcGZ0ZDNpeUs0SUxTd3pDYWtfWnNoeDI2QVVXTzItR2toXzJiNUhlLUxuMThiSm9ZTXBJdFA4?oc=5>

## HEADWINDS

### AT&T’s Dividend Payments Fell 46%. Now It’s Spending Billions on Stock Buybacks
- Summary: AT&T’s Dividend Payments Fell 46%. Now It’s Spending Billions on Stock Buybacks
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOaDIyWHJGdlVQM2oyZG01Wi1KeDJxUVZucTVtNjBTM1JWb01UMWhyU2R1VWN2dUdGUHQyak9ieXFNdU5JRUZiT0hwTmZFbGtjY3I1UzNmajhRdUVQbVVyT1pZbkRpRW52alJUOHpHdFRTVmV6azJURGJuZkdjUzBCZlM4RUl2QlpIdFpuUW9fdVZjNTVJU2FN?oc=5>

### AT&T Shares Are Down 11% Since Earnings. Is the Stock a Buy?
- Summary: AT&T Shares Are Down 11% Since Earnings. Is the Stock a Buy?
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxPVDZCR3JLcW92cG85Z1g0My1SV3hUWVA2R1Z5S19ELTlpMlJGS3ppV1pqenhNdTFsaGFLTzE1T3d0VHYtaVQzeDVONVVlQVItd0pVWGZZaUlRQjMzUzFETENON3pZUmVUZVBFT1JrVzJ4VXB6dkQ5OFFYNVl0MjNlQ29HSFktTnVMVWZpUVpB?oc=5>

## CATALYSTS

### AT&T (T) director Beth E. Mooney acquires 2,571.5965 cash-payable stock units through a benefit plan.
- Summary: AT&T (T) director Beth E. Mooney acquires 2,571.5965 cash-payable stock units through a benefit plan.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQV1NKWTQwN2x3aXEtR1NROWpOOTVnczdmclBkODNZODl6aFZ6ZnNGWDNRa213bngxRjdmNjBHU0xJMjJCWXlVQVF3bVFNejJ0VWJnY3NReDZ3QnFVbzRZS2ZGdVdZaHVJUE4xX1hUaFVoMkUtX0JKX0VQOVJZZXpBZXR4QjczNFVUdWhNdkN0NWtZeE5xNkMzS1NaZV80N0kw?oc=5>

### AT&T (T) director Marissa A. Mayer acquires stock units at $21.41 through a director plan.
- Summary: AT&T (T) director Marissa A. Mayer acquires stock units at $21.41 through a director plan.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOS0Rieko0WG5LMUVLajVJZEhSR01UcTdBa1gtUkZLdGVSdFg4eGpTdWlHd1F6RVp3aDdwOVlNeGU4bTBIRWtvTWZsbG5ObEliYWxMSnFFY1hXLUNRQTBZZV9KNDZjOHRzN2pMSC1tamdZMExHeWRtQzJ1OHNIcTBJQVhtTlhZb05Pc20ta2J0ZnRjaUFnaE55S1Z3MHNoampq?oc=5>

### AT&T (T) director acquires 955.0378 stock units under its non-employee director deferral plan.
- Summary: AT&T (T) director acquires 955.0378 stock units under its non-employee director deferral plan.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPZGxWQ3JIOTFnRWNwNzdPYlR4Rkw2TE8tcm5PRDc1LWxxcUdhYkFVLVFSUzRVOEViMHFjWjZvOWljcEZHMVFBZ2YyMk1ZQUNvS2RVcnI4eUZHUzZxMWtzbDJ0ejJ2cHNwbnhVUFIxLTlEb2Y5VnVVbE9qZ2N4ZDF6Z3lELVFxTUp4Z2lmemhjV2lEQ3RGdm53N0R2clUtX3RE?oc=5>

### AT&T (T) director Michael B. McCallister acquires stock units at $21.41 each.
- Summary: AT&T (T) director Michael B. McCallister acquires stock units at $21.41 each.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPNWUtbjUyZzh1MWhzd1FuZ19VeWhBS2lVVFN5dVduNDlTUzJQQVkzbWVNVkc5U3RpZWFJTDBMcHBURHlXNlpDQWpBQXMzaGRsX1M5amhoQ1ZkcUNsLWdmeWVGVlcxRjlfczhhTTQ4OERjdTV1WkhGeE1zblY4RW9JMHhIeE51Z2t3S1JlNzBxLVNZNGlKV1MyUl9WdnZtT2VI?oc=5>

### AT&T (T) director Matthew K. Rose acquires 4,657 stock-linked units through a benefit plan.
- Summary: AT&T (T) director Matthew K. Rose acquires 4,657 stock-linked units through a benefit plan.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOWXJYakFPNzNNVHF6dFV0QU9pRlpXUll1bFJJdjBKbVNjYXZxXzVIMUNJX0ZuUkZLR2thRC14M29aM2MwdGdkNkhlU2RGU3p3aVA2OXRwSGJGbW53SUw5R3E4R3hxMW82cTl0Y2pfbnZuLS1BbkZnNFYtTEI3eWF2eTk5VnNFdTdPeWFtZ3NYWTFiUHR6Ry1Iai15ZHZUR29w?oc=5>

### AT&T (T) director acquires stock units, bringing her cash-payable unit holdings to 229,046.
- Summary: AT&T (T) director acquires stock units, bringing her cash-payable unit holdings to 229,046.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPQ0tuRXZHbzlDb2pJd3VLcXRwaGNYQWI4d0J0MC0zUVRKckp2WUNZd1lHTTdUWnlnWFh1LVgycGN2QXQzeVctS09UZ2ZUeXNZdC05VmliV3pTUk1tWEc5OG5jR280NlExSWhBbzZFMVFpemdvOE9GVW9vN3F1ZzBZejFKbDAySzV1VXVOYk9uU2xLbzNRTUhZU1JGNm05Qk9q?oc=5>

### AT&T Inc. $T Stock Sold by Hennessy Advisors Inc.
- Summary: AT&T Inc. $T Stock Sold by Hennessy Advisors Inc.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOMGlUNEtuai12dU1id1JBNXNXdUo4Q0YxWkVLRTlQOTlpMkxWa1dGbGlrNFp6c04tcVVaa1NqUFVJamJpX0dWNU82b0c4Y1JSSW9BVklVM1VpTjNIS0VaX1hVSURUbl9fY1dhR1pwdXNTTTFmVVNaWktTQVVuVEVvaWxkQTN0OE1LdnRJb0dEaklBWmFXbWhKTjd2d1ZXZHZ5aGMzY1EwWXZKZw?oc=5>

### This House of Representative Just Bought Up To $75K In AT&T Stock
- Summary: Rep purchase may signal confidence, acting as a catalyst for AT&T stock.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQZUlBRzlmSEF6YzlvZWd4M0cxSWdGV3ZqVzlheElJNTNmVXdFVmhpWV8xb181dWFBSmE0VHhNQThzVTJQWnRENWpTNlQxc21DRnQxcnpMLUhyd1E2ZzIxVVBHZ29rLUVVYkdiZmR2M0ttY2hMd0VtUUNXaUFqd1Y1UXo3a1dNR1RSWHR6TjJncUdDNUhBanVMeXpsQQ?oc=5>

### AT&T (T) director receives 138.7882 stock units payable in cash after leaving the board.
- Summary: Director awarded cash‑payable stock units after board departure.
- Date: 2026-11-03 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOdmJDdnAxOXZTLUtNOVVRUXczY2xWSmN4LW80RXhxRXZZbTk4VG5zUi1lUVR5dVJkd2xlZFN4Wnc0SWJsck1YMkxWUDNhaFp0RlhQQkp6Y1ZyOVpRYWUzUV95bEdjaTU3RS1sSDM1RWN2c21BWk5IcUN5NzJwOVM5bDNUdUFFNHUzTjM3Zk8zN3B0V2p1WWdZRkVJU0g2dmpy?oc=5>

### AT&T Inc. $T Stock: Trek Financial LLC Boosts Stake
- Summary: Trek Financial LLC increased its AT&T shareholding.
- Date: 2026-11-03 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQbXgwckVldlJXcnJWMDhzazFkb05uVW1YeXpUZ0NPb2tMYUlFVFZ0M3pQVGo2ZGk3ZHptTWdqcWZaQ2JfNHlCZWhaVVNDQ0NpcHhzdkF2RlZ4ejFVdTZrblB6X1p6UDdiRkJhQkRodk1xczhPQkw3YVVKTVRxdllnTnlBdG5zOEcyNEd1UWI3TmZpcTRUZFE1dmFDUzlOZHgwbzVYaHF3LXVERjV6?oc=5>

### David Taylor buys AT&T, sells Marathon Petroleum stock
- Summary: Investor David Taylor purchased AT&T shares.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxPTUhYSW5PN2ZJZUlzX0hjNXhpMExxZm5ndU1MTTNmVEpMUGp3WTRiRmdTU2dORTQ2ay0zcHZmWHdia1ZLSzQ0V3gxbmdpRWJXQ01oaUxHM1BOdWJMMzZqckNzTnF3Z0ZmSnQydU4wQ3ptQ3RLWlYwUlZEZ044SEVQellYTjdyMmtUWjZXVTBoalhFM0FOTW95eDI5aHZycENFejZHam9oeWZOeWJMWFE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **T** | **11.44** | **1.35** | **7.22** | **5.30** | **144,093,167,616.00 USD** | **-8.64** |
| VZ | 11.54 | 1.77 | 7.29 | 1.50 | 187,501,625,344.00 USD | 22.25 |
| TMUS | 14.89 | 2.91 | 7.83 | 7.40 | 163,562,274,816.00 USD | -22.45 |
| BCE | 4.24 | 1.30 | 7.36 | 1.50 | 19,154,081,792.00 USD | -4.54 |

Peers fetched as_of: 2026-11-03; T reuses existing data (market data as_of: 2026-11-03); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-03

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

- https://news.google.com/rss/articles/CBMiogFBVV95cUxNSXRWRW9oXy1xdXNnckFLLUJ1bGFZS1lTS282LTl3cGtnb0ZJMU1RWG42TlQxWFdac3hKM1hOeUxxTGN6ZERVNTNyYUhkWFo0VE5uaG9qRzlpSWQtY2JXRHhnUExueGs5a1F5LTFlSENsQVZkbm96UDRTaHQtUEdZSzkzazJCLWpPSTdwNW93eG5BaVJqbnowN2tXZmR5RFI0N2c?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNbHVYTElaajZTMFN3Uy11UExZcXM2bWtmT2FZLVprVkVjS3B4QndlbGluWDlabDBsbGNndGpZMmNFOVRYbVBRTVNHdDRXd25vLXp6NnlrMWlEYXp1VEpHUUI1Sm1GVEg2WVZiOXIydkFYcm5IQTBnVlZCRjhVLXRFRVdyMVpfT2NRMUlUWDRSMEFyWmwxcl9ibQ?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQc1BkUDFaVkRUUEg5LTI4eVZuN3FOUEs2TFl4SmJEOERMRWV1RU9VNU5yVDZ0T25MTmliZVRxV0d2S05jMllRd0lRbFNjdHo3N1FLb1l5U2hLOHVQcVM0WXhOeUhjSkRWTVZmcWlSRDI5RjVNSlFnSXdLWHBlQ3NiZkpxMXZMMkk3VEZnaWZBaw?oc=5
- https://news.google.com/rss/articles/CBMidEFVX3lxTE5PMTRjblhqT2g0ZjZ6NTBqdGpveVl5S2dWZDZ1cTRUY1Fxc3dBbjV0NE42QnI0T1JUWXY3MWl4bWFiNTdPeUU5ZVVkTzZYV0lwcGxMRmlwdTB0c1IzdTJ3S1g5TXFsSXNoZ29WYlQzeVBRMWtU?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPTEZORThKcjZjV213ckw5R2dPNTFIMFA1d0kyV1FJX1pXR2R5NkZDQzdwbW0yQ0tXejlxd3J3Z2c0WEtMMzJIUmdIeDJDbnN1TjRtWVhZalpxNUJGTDZuMzdnT0RyLWk4dFJOeFRpaGxob3dVd0JyU01ibTdGVzZUamt5bzFZUl9Jd0NXV09JZUJjTG0tV0hvNUJKWQ?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxPcTdGZ3YtX2ZNN0pWTklOZ3JoUnJ1UmpVNU1BQVUxMEkza1I3R3Rtb05QczJVRzBCTmY1Y3l1eUM4Z3BUcjFtTXJwa0JRa1lhZXd1TmkzTGtoVTR4VHFPU29xdXRxdGUxYjlxSzJEU2JzRTdod1gxRG80Q041cUVwWHhMTnBRSjg5ZmtkZ0M2bTJ5QzlKTVlpNWlleWpTQkYyclBrYTF6QlNGU21aakVUUlpsX3pBcGZ0ZDNpeUs0SUxTd3pDYWtfWnNoeDI2QVVXTzItR2toXzJiNUhlLUxuMThiSm9ZTXBJdFA4?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOaDIyWHJGdlVQM2oyZG01Wi1KeDJxUVZucTVtNjBTM1JWb01UMWhyU2R1VWN2dUdGUHQyak9ieXFNdU5JRUZiT0hwTmZFbGtjY3I1UzNmajhRdUVQbVVyT1pZbkRpRW52alJUOHpHdFRTVmV6azJURGJuZkdjUzBCZlM4RUl2QlpIdFpuUW9fdVZjNTVJU2FN?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPVDZCR3JLcW92cG85Z1g0My1SV3hUWVA2R1Z5S19ELTlpMlJGS3ppV1pqenhNdTFsaGFLTzE1T3d0VHYtaVQzeDVONVVlQVItd0pVWGZZaUlRQjMzUzFETENON3pZUmVUZVBFT1JrVzJ4VXB6dkQ5OFFYNVl0MjNlQ29HSFktTnVMVWZpUVpB?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQV1NKWTQwN2x3aXEtR1NROWpOOTVnczdmclBkODNZODl6aFZ6ZnNGWDNRa213bngxRjdmNjBHU0xJMjJCWXlVQVF3bVFNejJ0VWJnY3NReDZ3QnFVbzRZS2ZGdVdZaHVJUE4xX1hUaFVoMkUtX0JKX0VQOVJZZXpBZXR4QjczNFVUdWhNdkN0NWtZeE5xNkMzS1NaZV80N0kw?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOS0Rieko0WG5LMUVLajVJZEhSR01UcTdBa1gtUkZLdGVSdFg4eGpTdWlHd1F6RVp3aDdwOVlNeGU4bTBIRWtvTWZsbG5ObEliYWxMSnFFY1hXLUNRQTBZZV9KNDZjOHRzN2pMSC1tamdZMExHeWRtQzJ1OHNIcTBJQVhtTlhZb05Pc20ta2J0ZnRjaUFnaE55S1Z3MHNoampq?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPZGxWQ3JIOTFnRWNwNzdPYlR4Rkw2TE8tcm5PRDc1LWxxcUdhYkFVLVFSUzRVOEViMHFjWjZvOWljcEZHMVFBZ2YyMk1ZQUNvS2RVcnI4eUZHUzZxMWtzbDJ0ejJ2cHNwbnhVUFIxLTlEb2Y5VnVVbE9qZ2N4ZDF6Z3lELVFxTUp4Z2lmemhjV2lEQ3RGdm53N0R2clUtX3RE?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPNWUtbjUyZzh1MWhzd1FuZ19VeWhBS2lVVFN5dVduNDlTUzJQQVkzbWVNVkc5U3RpZWFJTDBMcHBURHlXNlpDQWpBQXMzaGRsX1M5amhoQ1ZkcUNsLWdmeWVGVlcxRjlfczhhTTQ4OERjdTV1WkhGeE1zblY4RW9JMHhIeE51Z2t3S1JlNzBxLVNZNGlKV1MyUl9WdnZtT2VI?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOWXJYakFPNzNNVHF6dFV0QU9pRlpXUll1bFJJdjBKbVNjYXZxXzVIMUNJX0ZuUkZLR2thRC14M29aM2MwdGdkNkhlU2RGU3p3aVA2OXRwSGJGbW53SUw5R3E4R3hxMW82cTl0Y2pfbnZuLS1BbkZnNFYtTEI3eWF2eTk5VnNFdTdPeWFtZ3NYWTFiUHR6Ry1Iai15ZHZUR29w?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPQ0tuRXZHbzlDb2pJd3VLcXRwaGNYQWI4d0J0MC0zUVRKckp2WUNZd1lHTTdUWnlnWFh1LVgycGN2QXQzeVctS09UZ2ZUeXNZdC05VmliV3pTUk1tWEc5OG5jR280NlExSWhBbzZFMVFpemdvOE9GVW9vN3F1ZzBZejFKbDAySzV1VXVOYk9uU2xLbzNRTUhZU1JGNm05Qk9q?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOMGlUNEtuai12dU1id1JBNXNXdUo4Q0YxWkVLRTlQOTlpMkxWa1dGbGlrNFp6c04tcVVaa1NqUFVJamJpX0dWNU82b0c4Y1JSSW9BVklVM1VpTjNIS0VaX1hVSURUbl9fY1dhR1pwdXNTTTFmVVNaWktTQVVuVEVvaWxkQTN0OE1LdnRJb0dEaklBWmFXbWhKTjd2d1ZXZHZ5aGMzY1EwWXZKZw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQZUlBRzlmSEF6YzlvZWd4M0cxSWdGV3ZqVzlheElJNTNmVXdFVmhpWV8xb181dWFBSmE0VHhNQThzVTJQWnRENWpTNlQxc21DRnQxcnpMLUhyd1E2ZzIxVVBHZ29rLUVVYkdiZmR2M0ttY2hMd0VtUUNXaUFqd1Y1UXo3a1dNR1RSWHR6TjJncUdDNUhBanVMeXpsQQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOdmJDdnAxOXZTLUtNOVVRUXczY2xWSmN4LW80RXhxRXZZbTk4VG5zUi1lUVR5dVJkd2xlZFN4Wnc0SWJsck1YMkxWUDNhaFp0RlhQQkp6Y1ZyOVpRYWUzUV95bEdjaTU3RS1sSDM1RWN2c21BWk5IcUN5NzJwOVM5bDNUdUFFNHUzTjM3Zk8zN3B0V2p1WWdZRkVJU0g2dmpy?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQbXgwckVldlJXcnJWMDhzazFkb05uVW1YeXpUZ0NPb2tMYUlFVFZ0M3pQVGo2ZGk3ZHptTWdqcWZaQ2JfNHlCZWhaVVNDQ0NpcHhzdkF2RlZ4ejFVdTZrblB6X1p6UDdiRkJhQkRodk1xczhPQkw3YVVKTVRxdllnTnlBdG5zOEcyNEd1UWI3TmZpcTRUZFE1dmFDUzlOZHgwbzVYaHF3LXVERjV6?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPTUhYSW5PN2ZJZUlzX0hjNXhpMExxZm5ndU1MTTNmVEpMUGp3WTRiRmdTU2dORTQ2ay0zcHZmWHdia1ZLSzQ0V3gxbmdpRWJXQ01oaUxHM1BOdWJMMzZqckNzTnF3Z0ZmSnQydU4wQ3ptQ3RLWlYwUlZEZ044SEVQellYTjdyMmtUWjZXVTBoalhFM0FOTW95eDI5aHZycENFejZHam9oeWZOeWJMWFE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
