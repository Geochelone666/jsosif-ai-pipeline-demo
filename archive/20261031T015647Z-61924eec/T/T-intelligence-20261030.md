# T Intelligence Report

- ticker: **T**
- Report as_of: **2026-10-30**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/T/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/T/key-statistics/
- AI analysis snapshot as_of: **2026-10-30**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-31T02:04:20.663793+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 5, 'ai': 13, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **12** exact headline/source/date matches; prior report **20261030T021807Z-b9de7146/T** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 11 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 24.0%; oldest publication 2026-10-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 21.4100 |
| Return 1D (%) | 2.3423 |
| Return 1W (%) | 2.2934 |
| Return 1M (%) | -11.2622 |
| Return YTD (%) | -9.6959 |
| Return 1Y (%) | -9.1105 |
| Annualized volatility (%) | 28.6338 |
| Beta vs SPY | -0.4390 |
| Max drawdown (%) | -28.8854 |
| Sharpe (rf=0) | -0.1903 |
| Downside deviation (rf=0, %) | 21.9824 |
| Sortino (rf=0) | -0.2479 |
| Historical VaR 95% (1D, %) | 2.8546 |
| Historical ES 95% (1D, %) | 4.6484 |
| Correlation vs SPY | -0.1961 |
| Tracking error vs SPY (%) | 33.5718 |
| P/E (trailing) | 11.45 |
| P/B | 1.36 |
| EV/EBITDA | 7.23 |
| Revenue growth (%) | 5.30 |
| Forward P/E (estimate) | 8.26 |
| Gross margin (%) | 59.74 |
| Operating margin (%) | 24.65 |
| Return on equity (%) | 11.61 |
| Free cash flow yield (%) | 8.29 |
| MA50 | 24.1592 |
| Close vs MA50 (%) | -11.3797 |
| MA200 | 24.4453 |
| Close vs MA200 (%) | -12.4166 |
| RSI (14, Wilder) | 38.6282 |
| MACD (12,26) | -0.9010 |
| MACD signal (9) | -0.7606 |
| MACD histogram | -0.1404 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'T': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 21.4100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.3423 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.2934 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -11.2622 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -9.6959 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -9.1105 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.6338 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.9824 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.2479 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8546 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6484 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1961 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.5718 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.4390 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.8854 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.1903 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.2576 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 59.7420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 24.6520 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.6130 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 8.2936 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 11.4492 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.6282 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1404 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -11.3797 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -12.4166 -> Clearly below the moving-average trend level.

## TAILWINDS

### AT&T (NYSE:T) Stock Jumps 2.5% - Here's Why
- Summary: AT&T (NYSE:T) Stock Jumps 2.5% - Here's Why
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPNC0tbXk1WVdCWndUc1EzNFIwLTVLTXpvQVc5VFJwbEt6ZGRMeG56Wk5XUHRMbGt6SjMxbkJjSjltRXB4c1JpNGpqSTZtZUlUOUJKb3BmbEFaYnBYYmJLejdMRERyQ00wM2lfTDBQUWJpeGNhX0xrd3ppQ3I5cm45RDNKUHFRQ3BMUkxGaHEtMmEyUGNVanVGLXVOOA?oc=5>

### AT&T stock weighs record internet growth against higher debt
- Summary: AT&T stock weighs record internet growth against higher debt
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxPY244Q1d3SWVnVzg2d3dRY19WQS1UekZqd282VUhSd1ZYbHFGR1ZKTzI3bXhQUXdWa0doSDhsZEl0RU9WeFc2Z0ZuZ3BaUnNVZWJoUWk3emR6NUJ5V1BjMHFZWmJrdFZKd1hrbHZOTmN2a01GaVdWLWFPdW1Hc2haek00dmt0OG55Mm5nTHVrWDh2SGRnWjkxVXVhWE9FV0lwMUZ4TTB1MWFaUmkxcFFhOXc3Sm1nTXNoSkdsT2VBeXI?oc=5>

### AT&T (T) Stock Looks Cheap Relative To Its Earnings Outlook
- Summary: AT&T’s stock appears undervalued compared to earnings outlook.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQc1BkUDFaVkRUUEg5LTI4eVZuN3FOUEs2TFl4SmJEOERMRWV1RU9VNU5yVDZ0T25MTmliZVRxV0d2S05jMllRd0lRbFNjdHo3N1FLb1l5U2hLOHVQcVM0WXhOeUhjSkRWTVZmcWlSRDI5RjVNSlFnSXdLWHBlQ3NiZkpxMXZMMkk3VEZnaWZBaw?oc=5>

### Should You Buy AT&T Stock For Its Cash?
- Summary: AT&T’s cash holdings make it an attractive buy.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPTEZORThKcjZjV213ckw5R2dPNTFIMFA1d0kyV1FJX1pXR2R5NkZDQzdwbW0yQ0tXejlxd3J3Z2c0WEtMMzJIUmdIeDJDbnN1TjRtWVhZalpxNUJGTDZuMzdnT0RyLWk4dFJOeFRpaGxob3dVd0JyU01ibTdGVzZUamt5bzFZUl9Jd0NXV09JZUJjTG0tV0hvNUJKWQ?oc=5>

### AT&T: The SpaceX Panic Is A Gift (NYSE:T)
- Summary: SpaceX issues benefit AT&T amid panic.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxNXzU1S2c5UEFSSzJMbDIzSWZnb0F6V09vRjdqQVU3QVZ1YXkyV2J3SXhRZjZRY3BRajU1UGRSSERZbXFDNzBIZWhON21WUzRGQmoxV0FJWE1qYzZSRXJJSlByN1FEM1NRSlMtd0wwU2NhQ3hWWW0xek9HbWVJcXA4UEJB?oc=5>

### T-Mobile Rallies 7% and SpaceX Falls 4% as Price Tag for Musk's Wireless Push Balloons; Verizon Rises 3%, AT&T Gains 2%
- Summary: AT&T stock rose 2% amid market rally, reflecting short‑term positive momentum.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxPcTdGZ3YtX2ZNN0pWTklOZ3JoUnJ1UmpVNU1BQVUxMEkza1I3R3Rtb05QczJVRzBCTmY1Y3l1eUM4Z3BUcjFtTXJwa0JRa1lhZXd1TmkzTGtoVTR4VHFPU29xdXRxdGUxYjlxSzJEU2JzRTdod1gxRG80Q041cUVwWHhMTnBRSjg5ZmtkZ0M2bTJ5QzlKTVlpNWlleWpTQkYyclBrYTF6QlNGU21aakVUUlpsX3pBcGZ0ZDNpeUs0SUxTd3pDYWtfWnNoeDI2QVVXTzItR2toXzJiNUhlLUxuMThiSm9ZTXBJdFA4?oc=5>

### What Just Happened To AT&T Stock?
- Summary: AT&T shares experienced a short‑term price change, indicating immediate market reaction.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQTXFZWnp5RUtLRTdjVDNjVkp5OHJoVEd0bW9MdXVLX0QzWkgxOFU0R2dQZWdhT0hYa0o5VWRkTW9xX0FZOE9JSGljVzNKSW9sZkxpcXpFd0FROE5YWjhJazVmbmVMMEl5ZlBjdVp0anlObjNhc2FqNEZFZHFZam0xZ3Z6bERqSk4ybTc3eE14S1R6SEU?oc=5>

### Is AT&T Stock a Great Dividend Investment or a Value Trap?
- Summary: Analyst opinion weighing dividend appeal versus value concerns for AT&T.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQbXNTXy1rY0NmbE03M0Q0UVNFOGctcEpjWENFSmJpOVMyXy04SGo0LXk4cjZ2djRyTlR3YU9BZ0doMUlDOE9GSXMxcVVFeVlxejNoXzBlNEllcDBBb2tSOFphdVJSY09WN0R4Y2dOb2M3NW1KU3I0QjJwU1FlQUd0M2xPNkptNC13VmdzaHp1RW9uUkstc0U5RV82bUlvRUE?oc=5>

### Moderately bullish activity in AT&T with shares up 2.37%
- Summary: AT&T shares rise 2.37%, indicating positive market sentiment.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOZFk5a2VqVWxBM3VNOEpkMU5EY21yb2VtYUlPZ29hZ042YXhlZno2Z01CMnZzN0tsSDU1YnRSa0ltejNzeEd6SHBZWHNvY0Z2NGFDampvcUVJdVlhSllrcG5uUWU0aXYwSzM1dlNXVlJzdlQ5cnlqSTNTMERVeHlrdTUtcXFDMC1WcGxieEtaeG9ZMVZFelNHUVoyYzZXLW1UajlOc2Y0Zw?oc=5>

## HEADWINDS

### AT&T’s Dividend Payments Fell 46%. Now It’s Spending Billions on Stock Buybacks
- Summary: AT&T’s Dividend Payments Fell 46%. Now It’s Spending Billions on Stock Buybacks
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPdlRDV1VqY053eU9fTFZVSWZRSnh1QndUc25rNENFWmlFVnJYcmFmc0d1dUtaQ0FKcmxHZmg3SnBCTEtXUkZUdDVCMTQ0Q21MMXZZM3Qxa243NUQ5c3o0X25zNzFRbjhaa0pXb2hSaDlkSFV3ZlNrTFJRZWlIOEl4emlGbkFPU0htZk1uWnplRjFLUTdfNU4wMW5jcGttS2RYam02djdTTmozdDFkSVhoZy13aVAzMjBiMHc?oc=5>

### AT&T (NYSE:T) Stock Price Down 1.2% - Here's What Happened
- Summary: AT&T (NYSE:T) Stock Price Down 1.2% - Here's What Happened
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPdlBtczdGUmtETUR6Qi1JOWdlSTJCbElibDIyMVZjS2I1cmJ6WDBoSWg5dGhkbnBnTGd0VEUyZ0ZOY0NZcVhiTkxfUzRlRFBMNmNmOTVud2FjcURkemM2anVNYVZTWjgyUVlZbEc1a1JWcEkzbFdCa2NDazZFbExfb0Q3b2VKaGx5dDBmbFdfY1NhUEU0NUYwWE5YQWZObUFwTHBrampzTUhnb2VMUkow?oc=5>

### AT&T: 80,000 Reasons To Worry (NYSE:T)
- Summary: AT&T faces widespread concerns, indicating potential operational or financial challenges.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTFA3NV9JQnhaTjM4SlJTN2VsaUd4MXZLUVpLUGc2NXcxM0RBUmxycGdSVjZ5c19RT2xCUktWTDdWYUZ2a3RTSmNrdUZZalBMRDlHUlhvb2gwT2lxdE8wTzktNDZ0ZHRrTUxfeU9vdTJSdUJ1emdUUlFxME51N00?oc=5>

### VZ, TMUS, T Stocks Face Valuation Pressure From SpaceX Wireless Push But Tower Operators Stand To Gain, Says Citi
- Summary: Citi highlights valuation pressure on AT&T due to SpaceX push, a potential headwind.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQMDZuQWQ2eENQbDluYW5yVVZJSWJwekd6OGFZZ2lQTjUyLV8yTHJWVkxSeE1uT0ZEZ1dEUi1odlpQc3BoSGZGcF9QX2Y2RXV6eUJCRjJxa1BDRWFyYmw2WExMSnc1dUJyTWZqV3hzdlFYRENlSWRzM2FRc1pxU0Nub1AzUHJ5MEJQaEF2dDZNTQ?oc=5>

## CATALYSTS

### AT&T Stock In Focus After Earnings And Copper Network Phaseout Push
- Summary: AT&T Stock In Focus After Earnings And Copper Network Phaseout Push
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNcXhqMEVrRl9PS0ZTNjRFZ05pWUNlVVE4dkMyWWlJeDQ4dDk3eWZNYjJEc3VObWYtV3BNMXFyQzRSbU41Y1M1bmU5Y084aG9xVUpncHJkYXZLNDhlVlFvZ2U3VkFoTUZsbnF1YXk1d0JpZF9JVXpXSDVRZV9JOXpPMFhmQlVsRUVDc3JBdHBmV2hranc1cmZqckQzaWY4TVhrajVQMUo4VFJ0MU16OG5DZmU5WVNYSUXSAbwBQVVfeXFMUGlESjIydThuX3E2Smt4Q211YWtGSnJMaTN4dXhURE42emhOcWluRER1bUR1eURWU3VnU0R6RDlZbkEwUjdVTkxxZW1tTjNoRmRwY0Vhd1hORnZMNDVuNWE0QUxjUnhKRk94c21RN2VNXzkzOE1kRW9HOExua28zdEVvQk84OWN3QWtJbTRiTHRsMXQ3QUpCeWFFTVVaNFZMbWpodmU5NXM3clNlXzdJNkdOVFVqT2hzcGNhRFo?oc=5>

### Telecom Stocks Fall as SpaceX Eyes 80,000 Cell Sites: T-Mobile Sinks 5%, AT&T Drops 4%, Verizon Slides 3%
- Summary: AT&T shares fell 4% amid broader telecom sell‑off linked to SpaceX’s cell‑site plans.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQeW9YX2JfMVZfN2FVVGZXWmdNS181YzFZaWU5elRHeFlpMmNWZGJ3eWUtcmtPWnl1cFEzZE1aa3lZYkMxM1lYWW93WWw4dzgyQUVuRUd3ZTZiSjdhRVh0Wk0xVndjU2hLdmJHR1FrMExCdFVubWM3QXJubnpXX2NJcUpJQnB0VDFYVlo2STBjYlJ3YUtDdU1vM1Ezb1Y?oc=5>

### This House of Representative Just Bought Up To $75K In AT&T Stock
- Summary: Rep purchase may signal confidence, acting as a catalyst for AT&T stock.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQZUlBRzlmSEF6YzlvZWd4M0cxSWdGV3ZqVzlheElJNTNmVXdFVmhpWV8xb181dWFBSmE0VHhNQThzVTJQWnRENWpTNlQxc21DRnQxcnpMLUhyd1E2ZzIxVVBHZ29rLUVVYkdiZmR2M0ttY2hMd0VtUUNXaUFqd1Y1UXo3a1dNR1RSWHR6TjJncUdDNUhBanVMeXpsQQ?oc=5>

## RISKS

### ‘Real consequences’: AT&T, Verizon and T-Mobile warn FCC as Elon Musk plots a SpaceX phone network for the US by 2028
- Summary: Regulatory warning over potential competition from SpaceX phone network, posing future risk to AT&T.
- Date: 2026-10-25 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQWXc0TzBOUndZQ1Q2Y0xrRlZMZmU5VlhhWm1tOEt5WXhHaERMeFE4TjhWUnFlTzl5bDBrZFFxWDhxNXdreEpOdU9zQkUtQi12QUZ5SkZMdnFPNjlsUlBUNmxZcGpKaHl6Yzg5aTd1eU9aYm5RdkVUMEZiWC1uenY3ZHlpX0N1UFVjM1dVZWdhNVgtT1U2?oc=5>

### T Stock Update: AT&T 2024 Data Breach Settlements Could Arrive Soon
- Summary: Potential data breach settlements may impact AT&T's financials.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOaHNQa3M3bTI2SGJnemZwMTlSTEdQMHNJRGZOY0lRcGl3VXhmQ01DS3pvNlFBbHR5ME9wdzJDTTRqei1OU2FnbkNmWTgzTFR2cHFHS2ZubTBCMUVab3NKSG45UGlUTktkQmpZSTBqUTdQR2xIU2xFWVE0OFFkSTJmVVFIa0h3b3B5c2tZaDQwSkltR2RxRGNTVnlvUQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **T** | **11.45** | **1.36** | **7.23** | **5.30** | **144,227,893,248.00 USD** | **-9.11** |
| VZ | 11.41 | 1.75 | 7.28 | 1.50 | 185,387,876,352.00 USD | 22.45 |
| TMUS | 15.09 | 2.95 | 7.89 | 7.40 | 165,712,609,280.00 USD | -24.17 |
| BCE | 4.18 | 1.29 | 7.34 | 1.50 | 19,004,874,752.00 USD | -7.08 |

Peers fetched as_of: 2026-10-30; T reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-30

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMimwFBVV95cUxPNC0tbXk1WVdCWndUc1EzNFIwLTVLTXpvQVc5VFJwbEt6ZGRMeG56Wk5XUHRMbGt6SjMxbkJjSjltRXB4c1JpNGpqSTZtZUlUOUJKb3BmbEFaYnBYYmJLejdMRERyQ00wM2lfTDBQUWJpeGNhX0xrd3ppQ3I5cm45RDNKUHFRQ3BMUkxGaHEtMmEyUGNVanVGLXVOOA?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxPY244Q1d3SWVnVzg2d3dRY19WQS1UekZqd282VUhSd1ZYbHFGR1ZKTzI3bXhQUXdWa0doSDhsZEl0RU9WeFc2Z0ZuZ3BaUnNVZWJoUWk3emR6NUJ5V1BjMHFZWmJrdFZKd1hrbHZOTmN2a01GaVdWLWFPdW1Hc2haek00dmt0OG55Mm5nTHVrWDh2SGRnWjkxVXVhWE9FV0lwMUZ4TTB1MWFaUmkxcFFhOXc3Sm1nTXNoSkdsT2VBeXI?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQc1BkUDFaVkRUUEg5LTI4eVZuN3FOUEs2TFl4SmJEOERMRWV1RU9VNU5yVDZ0T25MTmliZVRxV0d2S05jMllRd0lRbFNjdHo3N1FLb1l5U2hLOHVQcVM0WXhOeUhjSkRWTVZmcWlSRDI5RjVNSlFnSXdLWHBlQ3NiZkpxMXZMMkk3VEZnaWZBaw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPTEZORThKcjZjV213ckw5R2dPNTFIMFA1d0kyV1FJX1pXR2R5NkZDQzdwbW0yQ0tXejlxd3J3Z2c0WEtMMzJIUmdIeDJDbnN1TjRtWVhZalpxNUJGTDZuMzdnT0RyLWk4dFJOeFRpaGxob3dVd0JyU01ibTdGVzZUamt5bzFZUl9Jd0NXV09JZUJjTG0tV0hvNUJKWQ?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxNXzU1S2c5UEFSSzJMbDIzSWZnb0F6V09vRjdqQVU3QVZ1YXkyV2J3SXhRZjZRY3BRajU1UGRSSERZbXFDNzBIZWhON21WUzRGQmoxV0FJWE1qYzZSRXJJSlByN1FEM1NRSlMtd0wwU2NhQ3hWWW0xek9HbWVJcXA4UEJB?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxPcTdGZ3YtX2ZNN0pWTklOZ3JoUnJ1UmpVNU1BQVUxMEkza1I3R3Rtb05QczJVRzBCTmY1Y3l1eUM4Z3BUcjFtTXJwa0JRa1lhZXd1TmkzTGtoVTR4VHFPU29xdXRxdGUxYjlxSzJEU2JzRTdod1gxRG80Q041cUVwWHhMTnBRSjg5ZmtkZ0M2bTJ5QzlKTVlpNWlleWpTQkYyclBrYTF6QlNGU21aakVUUlpsX3pBcGZ0ZDNpeUs0SUxTd3pDYWtfWnNoeDI2QVVXTzItR2toXzJiNUhlLUxuMThiSm9ZTXBJdFA4?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxQTXFZWnp5RUtLRTdjVDNjVkp5OHJoVEd0bW9MdXVLX0QzWkgxOFU0R2dQZWdhT0hYa0o5VWRkTW9xX0FZOE9JSGljVzNKSW9sZkxpcXpFd0FROE5YWjhJazVmbmVMMEl5ZlBjdVp0anlObjNhc2FqNEZFZHFZam0xZ3Z6bERqSk4ybTc3eE14S1R6SEU?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQbXNTXy1rY0NmbE03M0Q0UVNFOGctcEpjWENFSmJpOVMyXy04SGo0LXk4cjZ2djRyTlR3YU9BZ0doMUlDOE9GSXMxcVVFeVlxejNoXzBlNEllcDBBb2tSOFphdVJSY09WN0R4Y2dOb2M3NW1KU3I0QjJwU1FlQUd0M2xPNkptNC13VmdzaHp1RW9uUkstc0U5RV82bUlvRUE?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOZFk5a2VqVWxBM3VNOEpkMU5EY21yb2VtYUlPZ29hZ042YXhlZno2Z01CMnZzN0tsSDU1YnRSa0ltejNzeEd6SHBZWHNvY0Z2NGFDampvcUVJdVlhSllrcG5uUWU0aXYwSzM1dlNXVlJzdlQ5cnlqSTNTMERVeHlrdTUtcXFDMC1WcGxieEtaeG9ZMVZFelNHUVoyYzZXLW1UajlOc2Y0Zw?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPdlRDV1VqY053eU9fTFZVSWZRSnh1QndUc25rNENFWmlFVnJYcmFmc0d1dUtaQ0FKcmxHZmg3SnBCTEtXUkZUdDVCMTQ0Q21MMXZZM3Qxa243NUQ5c3o0X25zNzFRbjhaa0pXb2hSaDlkSFV3ZlNrTFJRZWlIOEl4emlGbkFPU0htZk1uWnplRjFLUTdfNU4wMW5jcGttS2RYam02djdTTmozdDFkSVhoZy13aVAzMjBiMHc?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPdlBtczdGUmtETUR6Qi1JOWdlSTJCbElibDIyMVZjS2I1cmJ6WDBoSWg5dGhkbnBnTGd0VEUyZ0ZOY0NZcVhiTkxfUzRlRFBMNmNmOTVud2FjcURkemM2anVNYVZTWjgyUVlZbEc1a1JWcEkzbFdCa2NDazZFbExfb0Q3b2VKaGx5dDBmbFdfY1NhUEU0NUYwWE5YQWZObUFwTHBrampzTUhnb2VMUkow?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTFA3NV9JQnhaTjM4SlJTN2VsaUd4MXZLUVpLUGc2NXcxM0RBUmxycGdSVjZ5c19RT2xCUktWTDdWYUZ2a3RTSmNrdUZZalBMRDlHUlhvb2gwT2lxdE8wTzktNDZ0ZHRrTUxfeU9vdTJSdUJ1emdUUlFxME51N00?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQMDZuQWQ2eENQbDluYW5yVVZJSWJwekd6OGFZZ2lQTjUyLV8yTHJWVkxSeE1uT0ZEZ1dEUi1odlpQc3BoSGZGcF9QX2Y2RXV6eUJCRjJxa1BDRWFyYmw2WExMSnc1dUJyTWZqV3hzdlFYRENlSWRzM2FRc1pxU0Nub1AzUHJ5MEJQaEF2dDZNTQ?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNcXhqMEVrRl9PS0ZTNjRFZ05pWUNlVVE4dkMyWWlJeDQ4dDk3eWZNYjJEc3VObWYtV3BNMXFyQzRSbU41Y1M1bmU5Y084aG9xVUpncHJkYXZLNDhlVlFvZ2U3VkFoTUZsbnF1YXk1d0JpZF9JVXpXSDVRZV9JOXpPMFhmQlVsRUVDc3JBdHBmV2hranc1cmZqckQzaWY4TVhrajVQMUo4VFJ0MU16OG5DZmU5WVNYSUXSAbwBQVVfeXFMUGlESjIydThuX3E2Smt4Q211YWtGSnJMaTN4dXhURE42emhOcWluRER1bUR1eURWU3VnU0R6RDlZbkEwUjdVTkxxZW1tTjNoRmRwY0Vhd1hORnZMNDVuNWE0QUxjUnhKRk94c21RN2VNXzkzOE1kRW9HOExua28zdEVvQk84OWN3QWtJbTRiTHRsMXQ3QUpCeWFFTVVaNFZMbWpodmU5NXM3clNlXzdJNkdOVFVqT2hzcGNhRFo?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQeW9YX2JfMVZfN2FVVGZXWmdNS181YzFZaWU5elRHeFlpMmNWZGJ3eWUtcmtPWnl1cFEzZE1aa3lZYkMxM1lYWW93WWw4dzgyQUVuRUd3ZTZiSjdhRVh0Wk0xVndjU2hLdmJHR1FrMExCdFVubWM3QXJubnpXX2NJcUpJQnB0VDFYVlo2STBjYlJ3YUtDdU1vM1Ezb1Y?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQZUlBRzlmSEF6YzlvZWd4M0cxSWdGV3ZqVzlheElJNTNmVXdFVmhpWV8xb181dWFBSmE0VHhNQThzVTJQWnRENWpTNlQxc21DRnQxcnpMLUhyd1E2ZzIxVVBHZ29rLUVVYkdiZmR2M0ttY2hMd0VtUUNXaUFqd1Y1UXo3a1dNR1RSWHR6TjJncUdDNUhBanVMeXpsQQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQWXc0TzBOUndZQ1Q2Y0xrRlZMZmU5VlhhWm1tOEt5WXhHaERMeFE4TjhWUnFlTzl5bDBrZFFxWDhxNXdreEpOdU9zQkUtQi12QUZ5SkZMdnFPNjlsUlBUNmxZcGpKaHl6Yzg5aTd1eU9aYm5RdkVUMEZiWC1uenY3ZHlpX0N1UFVjM1dVZWdhNVgtT1U2?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOaHNQa3M3bTI2SGJnemZwMTlSTEdQMHNJRGZOY0lRcGl3VXhmQ01DS3pvNlFBbHR5ME9wdzJDTTRqei1OU2FnbkNmWTgzTFR2cHFHS2ZubTBCMUVab3NKSG45UGlUTktkQmpZSTBqUTdQR2xIU2xFWVE0OFFkSTJmVVFIa0h3b3B5c2tZaDQwSkltR2RxRGNTVnlvUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
