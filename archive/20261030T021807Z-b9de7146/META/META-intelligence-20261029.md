# META Intelligence Report

- ticker: **META**
- Report as_of: **2026-10-29**
- Market data as_of: **2026-10-29**
- Quant sources: https://finance.yahoo.com/quote/META/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/META/key-statistics/
- AI analysis snapshot as_of: **2026-10-29**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-30T02:28:34.028497+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 7, 'ai': 12, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261029T020157Z-688a53f0/META** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 17 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-10-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 624.5200 |
| Return 1D (%) | 1.9641 |
| Return 1W (%) | -3.7497 |
| Return 1M (%) | -15.4672 |
| Return YTD (%) | -5.1451 |
| Return 1Y (%) | -16.6338 |
| Annualized volatility (%) | 42.7884 |
| Beta vs SPY | 1.4968 |
| Max drawdown (%) | -29.9428 |
| Sharpe (rf=0) | -0.2139 |
| Downside deviation (rf=0, %) | 29.7613 |
| Sortino (rf=0) | -0.3075 |
| Historical VaR 95% (1D, %) | 3.7761 |
| Historical ES 95% (1D, %) | 6.2110 |
| Correlation vs SPY | 0.4446 |
| Tracking error vs SPY (%) | 38.8432 |
| P/E (trailing) | 21.31 |
| P/B | 5.86 |
| EV/EBITDA | 14.02 |
| Revenue growth (%) | 26.10 |
| Forward P/E (estimate) | 17.55 |
| Gross margin (%) | 81.03 |
| Operating margin (%) | 35.41 |
| Return on equity (%) | 32.26 |
| Free cash flow yield (%) | 1.06 |
| MA50 | 668.3969 |
| Close vs MA50 (%) | -6.5645 |
| MA200 | 631.2701 |
| Close vs MA200 (%) | -1.0693 |
| RSI (14, Wilder) | 34.9936 |
| MACD (12,26) | -18.2313 |
| MACD signal (9) | -3.3854 |
| MACD histogram | -14.8459 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'META': 271, 'SPY': 271}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 624.5200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.9641 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.7497 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -15.4672 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -5.1451 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -16.6338 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 42.7884 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 29.7613 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.3075 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.7761 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.2110 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4446 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 38.8432 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.4968 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -29.9428 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.2139 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.5487 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.0340 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 35.4140 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.2640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0551 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.3074 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 34.9936 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -14.8459 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -6.5645 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -1.0693 -> Slightly below the moving-average trend level.

## TAILWINDS

### Meta Platforms (NASDAQ:META) Stock Price Up 2% - Still a Buy?
- Summary: Meta Platforms (NASDAQ:META) Stock Price Up 2% - Still a Buy?
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxNVDBWc0s0NUZMSVoyZlhEbWk2LWZTT2UwRGlUak94bUVDNFFKZjBVdWxhS1lXT1BCZTZlM2I4YUJHWWN3c1VQSnFTdUJYQnVNNTZPblhlQ05MUFotWEdERktETU1qazBNVnExajVsY20wMnMwWXRMLURJbWR4cUNzbEpobVFnVzNlclBKcUlZOVBjbFduZjJOVGNIUUdSQnAtdms3aXh3WWpmb1I3NjAtV093b2gyQQ?oc=5>

### Meta Stock Falls On Plan For $95 Billion Equity Raise. Analysts Are Offering A Positive View.
- Summary: Meta Stock Falls On Plan For $95 Billion Equity Raise. Analysts Are Offering A Positive View.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxQRVNaVzVKMV9fbDV0TlVybC05NnZsay1zWEc3ZDBtbDVBVWxuYkltbE9DSmRVY2RsR2Z3RTJaREF1MWZ6ZWhfeVdxTHVhdV9PYS1zRG1LVGplM1ViYnBVbEZmUVhoTHh5cFduaWhkbG51SEhVaXd6OVIybjc5ekI4Z1Nrbw?oc=5>

### Meta Platforms: Muse May Be Metaverse 2.0, But It’s Too Late (NASDAQ:META)
- Summary: Meta’s Muse platform aims to revitalize its metaverse vision, though critics question its timeliness and competitive edge.
- Date: 2026-10-26 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQU1U5NGk4c1k0U0Jfa2hBQUZmaVVFcndyNmQ5bUxXdmhVbjBDMWhnNy1SdDFvckd0cmxDOW9LY09hQ3EwTlpHRE9Ha2gwdnBEVHJrUWJJdFdDckk0a0lGeHE2RVFCS09leGI0czFWbHQ1VFc0d2dSR0dDZml0N1F5YXE4QWoxS2xDRlg0RWVQcjNkYzNNSUdMUWgxclJFbUk?oc=5>

### One Big Reason Meta Stock Could Be a Winner Through 2030
- Summary: Meta’s long-term growth prospects could make its stock attractive through 2030.
- Date: 2026-10-29 | Impact: high | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPRVBPRktCcEhZbWhwNHJ5LTdQWGNnbG9PNEhtUzV4ZzZPZ2V4blA0MmdZQmJ1OTdqZkdQMnVXODhDSHlpdjRXam1BT2xjQi1WZXZhUXJVanRaajgxMVFPeVJtQS1Nd2Y5ZDQzb204ZW82NkNubFZSUUhLWHZKM3JVNDVmVDEwa01rVk91WXVZa3ozaEhqeUdfODZacjIzUTFuRmc?oc=5>

### Meta eyes record $97.5 billion equity raise to fund AI expansion
- Summary: Meta plans a record equity raise to fund AI initiatives, boosting capital for growth.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPclhjOFJvYkM0S0hLUmxaY0l2X3hCdWI0N1prZlo2QXhXdmt5T0pNQVpFODVpYzgycWdZcHM2NkZ2LTdaMEVUVlpTXzVFUzc2ZEdVdlpTeThUVkZtc3V4cEFTelk5bDd2Z0dfRDFsb0dGQ0MxRXhYMExFZTlXVkNjRXF6TDBLalZ5ZTFBbFMyX24wMVBTQW1GQkJNRjNYWTRiVGJJWWdialBfV1oyQUZNN3I4RQ?oc=5>

## HEADWINDS

### Meta Shares Are Down 12% Since Earnings. Is the Stock a Buy?
- Summary: Meta Shares Are Down 12% Since Earnings. Is the Stock a Buy?
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPeEFsRjB6d2lwTVZ1UWhyVnhEZmkwRG9rQmo1dVp5d3plSFNEVzZHQllCakFVdXJaM2dQUklnQTEwMHp6MDlud0pmOERnSFVpeEtuMFY1ZjFGMmtkcGFlN2JSUVVMLTBDNEJqazJDUXVRWTBFczdKTXJVVTlXcHk2VHZJUE1aTTVfZm1uM2YzRQ?oc=5>

### Meta Stock Falls Following Launch Of $35 Billion Stock Offering
- Summary: Meta Stock Falls Following Launch Of $35 Billion Stock Offering
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMid0FVX3lxTFA5WXQzNmRlc3JsVFdGZkFSWXhtRFlQX2ZzQkpRa0VlTmZxNFBpQmZJREZrZGR3YVI1SHBnR2FjVE1VOF9EYVBsWUctV3ZxVnc2QWw1MDB4REpGY0ExZWRoRnh4aHJlU1c5RW5Xa3lBTnVaQXlTNVZR?oc=5>

### Meta Stock Falls. Earnings Show Just How Much Future Growth Will Cost.
- Summary: Meta Stock Falls. Earnings Show Just How Much Future Growth Will Cost.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTE4tdTM5U2kwQ295eEpWaTdjamk4SDdmT09TWjFBNHBhZkRxcmR6SmpNT1lEbTZGZTl0LVZpYUxXUERlOEtsaWdFLXF2QTFSUG9LM0RjbkZyR21YR1dlNmN2NnhvTWFqanY4Q09IYjBqT29SOHBGeWxrZg?oc=5>

### Meta Stock Sell-Off Looks Like an Overreaction
- Summary: Meta shares fell sharply, seen as overreaction to market fears.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxQcHJtRUdQWm1ocmFuMnFtMTU0Zzc4WE9QTWZVSWllaWVaejhGQW13ZTZRMjZrWmt5Qm1LS1BackpkNXdqT1ozbTlEUzNJUS02X3RhZGs4cjJNT1lyMUhVaVRHX3RFdm1vcFNYSkREUEFNblQwR01KdDFSazNIMDRYUkVB?oc=5>

### Zuckerberg Stock Deal, Meta Restructuring Hit With Challenge (2)
- Summary: Zuckerberg's stock deal faces restructuring challenge.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPbzRhY1NjSWVPZlI2eHBBdkdfN2JvblJESXFmRUZ3dE5JUkVxUjZZdzY1d2VFWE1YLTlEbFE4ck56Wk1jTTk3U2J1bzdfVmpuWHUzcVZmOElYYWh5M0U4eXBndUNhS2VtaGNEOHhMSTlSWUI1MjJrdDZKM3YtVWthNXlwM2ZzOHZMWmY2YnBOdEYyN0R0bkZQS3NB?oc=5>

### Is Meta Stock's Fall A Bargain Or A Warning?
- Summary: Meta’s stock decline raises concerns about valuation and future performance.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNNldtWTlCU0xyQnBfVk1taE9kemFRaDd3MWszdFpPOFluZGtBNENMSDZSellsenhxd0lWS2F0VHBiUXJ1cDJ5QmYwaEVnMVJoRmRSY3g4clRtVXhuTEx6V3lKcURiU2dKQnVRdGxHa2g2QlpjQ1l3OElWNFFuUnlveVp6WlNmRFliOFdyLXRpQU82OE9LcHg2VHowbzc4QQ?oc=5>

### Meta stock closes out Friday down as AI spending fears continue to rattle markets
- Summary: Meta’s share price fell amid AI spending fears, reflecting market volatility.
- Date: 2026-10-23 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxNOVBsWC1HZmNiRnJHT3RIbzlmcmZLZVpRVVlibk5sMFhyLUJfSHVtZlhxNzBLWkJ6RkgtWWprZnl2ZUVCeVBzb3NOVzlJQkYwbjBvVzQtaFZDSk9rZGxlYWVjMEJnWFY0LVFiUVM0S2J1T0ExVTJMcFY4QjJ1ZDgwNVVrVEpENFpJMHVrRkpoVXJvSTktOE9fMU94dnpLR1UxWWlSTFVHallWRG1DTDBhNXJobzJpek5UeTk3dUFRZl9QMnJhaGo1OXo3TUhSeEg0LTVQeHZiZ0NuZw?oc=5>

### Is Meta Stock’s Fall A Bargain Or A Warning?
- Summary: Meta’s stock decline raises concerns about valuation and future performance.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQdHR6ZEd6RloxRHdXdUk4cDVPUmJuX3ltU1NiZjh3RHFQc0R2LVdUaVZPdEYzelIxQ1JrZUpMampCVFM1ZGhOeXZoajJZdVlWb2p3SS1lbWlQMFlYVnVxYnpNdE1EeVUxeFlNZEhsVE9jQzQwQU5GdEVvcDhudnd2WXdNNEhwN3BPSDVFZGNBXzdxenhqT1hyMVdBMjM0M1lWclhxcWtB?oc=5>

### A 5-Day Losing Streak Has Meta Platforms Stock Down 12%
- Summary: Meta stock fell 12% over five days, indicating short-term downside pressure.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxPYnY1MVNTNUk4ZGt1LVRCZll4bXdkRXRBb3pkX1drYl9WUTN4ZDRBamp3OWo3cl92UjhKM2FHZVhCM054bDU4eXdzM2M0T0ZxVjZhNE44QnN6X2hlajVaS0wtb2VobWJNQllQU1RNRF9aQzhfZ3h3Rk13ZThXeHowLUpqZnhsNGZIclhfajBzRDlEU3A0d0pXSG9SVklNWFNxc3ZZdnIxQmRjVEdrZG8xZ0JoWTAwQQ?oc=5>

## CATALYSTS

### Meta Loses $400 Billion, Auctions More Stock, But Analysts Still See 1.4x Upside
- Summary: Meta Loses $400 Billion, Auctions More Stock, But Analysts Still See 1.4x Upside
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQZDZCVy1CLS1KV1plaWZjVXo4UnZuWWVXbGRQNmtQcTRlM0lIeHBnaE5tVGg2dzN0MFJ2N0tQejFjbklESHhoTS1UX2p4SlUzQWhUZXFZTzJGM2NpTDFGUHJRSXVSS0N3YVpYRG9fUEM5Z2dMQmdYbkV0TEZkYUIxMUtWT2h3eVR6MGhqRFFUeFVqdklVQzd1TzlLeUw?oc=5>

### Meta’s Unusual Stock Split Comes With a $60 Billion Twist Investors Should Know About
- Summary: Meta’s Unusual Stock Split Comes With a $60 Billion Twist Investors Should Know About
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOM2xkR0Z4TFBwOUVtd2JTOFNTWmJOdENmNU9kUXViMXNlZVBHTEpwYzhaUzcxelZsNmFRQ09PdG1iTmFKOEdaOUFhVU1MNFhiWERYN0trQVc4WUtubGVWaEtwRnphTzFRX3UtU19SUUZYclpRNlB6YWV0ZnFIN3VKXzUzSG5IOEt1YWpGRXBXUnBBOUVvdE1uaGtJcw?oc=5>

### Meta’s $25 Billion Stock Sale Ended Five Times Oversubscribed
- Summary: Meta completed a $25B stock sale, oversubscribed five times, signaling strong investor demand.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNdmR1WjllZWo5S013MU1kTmgzNWdZXzd3ejl4bHZFRlR6NUpLbWt5aHdaYkpzc3g4eG55M0Q2UGVHb01oSHBIUWZyY0tzTHNzMlU2clZ6NVFoZmJ3clRtYkZLWHFsWElfRHRibEw0UkZYMUNtQzNQcFVtejBQUjM4QVh6Yk9LdVMzOENZU1U3S0syTWRxSU9zdmFkQUlLY2hVQkFtVlFrN3lseGhEcWNPdA?oc=5>

### Meta Will Offer Up to $95 Billion in Stock. What That Means for Its Big AI Push.
- Summary: Meta plans to sell up to $95B in shares to fund AI initiatives.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE10bm9vdXZ0RDJuVWNfMGo5bnQtLTJ6b2c3WTlMNExXaEsyOUpiNEd0cGt0YVNldlZHNEtvaThTOXV3LUpBVEFmcmNOOTBSZDNPbTBmNGlFVzgwYkFqQmY2eExVUjR6UEEtNk1hNzdkWEgtTWs2bTZNbGl2a0hOUQ?oc=5>

### Meta’s $100 billion stock sale shrinks your slice of the company
- Summary: Meta’s $100B share sale reduces individual ownership stakes.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOU0VRWHJGQjJ6RVYyWnVsYzZBdWg0MWVSVTlTLWptRkM1S0RaOUoxYy1fMnpjTFZWVEZwZXZEREE1c0hlSWEwMldITDhDYjFwRUJ3Z2V3ZW1pd19lV0JRaUpCbXEtZlctLWFGbnlHdTVwOE9RN0dfcVRqVWhsREFQclJDazdOUVZMX0lQci11VDUtSnNtT3EyM3RB?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **META** | **21.31** | **5.86** | **14.02** | **26.10** | **1,596,793,421,824.00 USD** | **-16.63** |
| GOOGL | 14.82 | 8.26 | 22.35 | 24.20 | 3,471,100,346,368.00 USD | 3.64 |
| SNAP | N/A | 4.96 | -76.38 | 18.90 | 9,606,002,688.00 USD | -26.61 |
| PINS | 58.59 | 3.89 | 35.39 | 18.20 | 11,280,955,392.00 USD | -39.29 |

Peers fetched as_of: 2026-10-29; META reuses existing data (market data as_of: 2026-10-29); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-29

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

- https://news.google.com/rss/articles/CBMitgFBVV95cUxNVDBWc0s0NUZMSVoyZlhEbWk2LWZTT2UwRGlUak94bUVDNFFKZjBVdWxhS1lXT1BCZTZlM2I4YUJHWWN3c1VQSnFTdUJYQnVNNTZPblhlQ05MUFotWEdERktETU1qazBNVnExajVsY20wMnMwWXRMLURJbWR4cUNzbEpobVFnVzNlclBKcUlZOVBjbFduZjJOVGNIUUdSQnAtdms3aXh3WWpmb1I3NjAtV093b2gyQQ?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxQRVNaVzVKMV9fbDV0TlVybC05NnZsay1zWEc3ZDBtbDVBVWxuYkltbE9DSmRVY2RsR2Z3RTJaREF1MWZ6ZWhfeVdxTHVhdV9PYS1zRG1LVGplM1ViYnBVbEZmUVhoTHh5cFduaWhkbG51SEhVaXd6OVIybjc5ekI4Z1Nrbw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQU1U5NGk4c1k0U0Jfa2hBQUZmaVVFcndyNmQ5bUxXdmhVbjBDMWhnNy1SdDFvckd0cmxDOW9LY09hQ3EwTlpHRE9Ha2gwdnBEVHJrUWJJdFdDckk0a0lGeHE2RVFCS09leGI0czFWbHQ1VFc0d2dSR0dDZml0N1F5YXE4QWoxS2xDRlg0RWVQcjNkYzNNSUdMUWgxclJFbUk?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPRVBPRktCcEhZbWhwNHJ5LTdQWGNnbG9PNEhtUzV4ZzZPZ2V4blA0MmdZQmJ1OTdqZkdQMnVXODhDSHlpdjRXam1BT2xjQi1WZXZhUXJVanRaajgxMVFPeVJtQS1Nd2Y5ZDQzb204ZW82NkNubFZSUUhLWHZKM3JVNDVmVDEwa01rVk91WXVZa3ozaEhqeUdfODZacjIzUTFuRmc?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxPclhjOFJvYkM0S0hLUmxaY0l2X3hCdWI0N1prZlo2QXhXdmt5T0pNQVpFODVpYzgycWdZcHM2NkZ2LTdaMEVUVlpTXzVFUzc2ZEdVdlpTeThUVkZtc3V4cEFTelk5bDd2Z0dfRDFsb0dGQ0MxRXhYMExFZTlXVkNjRXF6TDBLalZ5ZTFBbFMyX24wMVBTQW1GQkJNRjNYWTRiVGJJWWdialBfV1oyQUZNN3I4RQ?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPeEFsRjB6d2lwTVZ1UWhyVnhEZmkwRG9rQmo1dVp5d3plSFNEVzZHQllCakFVdXJaM2dQUklnQTEwMHp6MDlud0pmOERnSFVpeEtuMFY1ZjFGMmtkcGFlN2JSUVVMLTBDNEJqazJDUXVRWTBFczdKTXJVVTlXcHk2VHZJUE1aTTVfZm1uM2YzRQ?oc=5
- https://news.google.com/rss/articles/CBMid0FVX3lxTFA5WXQzNmRlc3JsVFdGZkFSWXhtRFlQX2ZzQkpRa0VlTmZxNFBpQmZJREZrZGR3YVI1SHBnR2FjVE1VOF9EYVBsWUctV3ZxVnc2QWw1MDB4REpGY0ExZWRoRnh4aHJlU1c5RW5Xa3lBTnVaQXlTNVZR?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTE4tdTM5U2kwQ295eEpWaTdjamk4SDdmT09TWjFBNHBhZkRxcmR6SmpNT1lEbTZGZTl0LVZpYUxXUERlOEtsaWdFLXF2QTFSUG9LM0RjbkZyR21YR1dlNmN2NnhvTWFqanY4Q09IYjBqT29SOHBGeWxrZg?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxQcHJtRUdQWm1ocmFuMnFtMTU0Zzc4WE9QTWZVSWllaWVaejhGQW13ZTZRMjZrWmt5Qm1LS1BackpkNXdqT1ozbTlEUzNJUS02X3RhZGs4cjJNT1lyMUhVaVRHX3RFdm1vcFNYSkREUEFNblQwR01KdDFSazNIMDRYUkVB?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPbzRhY1NjSWVPZlI2eHBBdkdfN2JvblJESXFmRUZ3dE5JUkVxUjZZdzY1d2VFWE1YLTlEbFE4ck56Wk1jTTk3U2J1bzdfVmpuWHUzcVZmOElYYWh5M0U4eXBndUNhS2VtaGNEOHhMSTlSWUI1MjJrdDZKM3YtVWthNXlwM2ZzOHZMWmY2YnBOdEYyN0R0bkZQS3NB?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNNldtWTlCU0xyQnBfVk1taE9kemFRaDd3MWszdFpPOFluZGtBNENMSDZSellsenhxd0lWS2F0VHBiUXJ1cDJ5QmYwaEVnMVJoRmRSY3g4clRtVXhuTEx6V3lKcURiU2dKQnVRdGxHa2g2QlpjQ1l3OElWNFFuUnlveVp6WlNmRFliOFdyLXRpQU82OE9LcHg2VHowbzc4QQ?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxNOVBsWC1HZmNiRnJHT3RIbzlmcmZLZVpRVVlibk5sMFhyLUJfSHVtZlhxNzBLWkJ6RkgtWWprZnl2ZUVCeVBzb3NOVzlJQkYwbjBvVzQtaFZDSk9rZGxlYWVjMEJnWFY0LVFiUVM0S2J1T0ExVTJMcFY4QjJ1ZDgwNVVrVEpENFpJMHVrRkpoVXJvSTktOE9fMU94dnpLR1UxWWlSTFVHallWRG1DTDBhNXJobzJpek5UeTk3dUFRZl9QMnJhaGo1OXo3TUhSeEg0LTVQeHZiZ0NuZw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQdHR6ZEd6RloxRHdXdUk4cDVPUmJuX3ltU1NiZjh3RHFQc0R2LVdUaVZPdEYzelIxQ1JrZUpMampCVFM1ZGhOeXZoajJZdVlWb2p3SS1lbWlQMFlYVnVxYnpNdE1EeVUxeFlNZEhsVE9jQzQwQU5GdEVvcDhudnd2WXdNNEhwN3BPSDVFZGNBXzdxenhqT1hyMVdBMjM0M1lWclhxcWtB?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxPYnY1MVNTNUk4ZGt1LVRCZll4bXdkRXRBb3pkX1drYl9WUTN4ZDRBamp3OWo3cl92UjhKM2FHZVhCM054bDU4eXdzM2M0T0ZxVjZhNE44QnN6X2hlajVaS0wtb2VobWJNQllQU1RNRF9aQzhfZ3h3Rk13ZThXeHowLUpqZnhsNGZIclhfajBzRDlEU3A0d0pXSG9SVklNWFNxc3ZZdnIxQmRjVEdrZG8xZ0JoWTAwQQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQZDZCVy1CLS1KV1plaWZjVXo4UnZuWWVXbGRQNmtQcTRlM0lIeHBnaE5tVGg2dzN0MFJ2N0tQejFjbklESHhoTS1UX2p4SlUzQWhUZXFZTzJGM2NpTDFGUHJRSXVSS0N3YVpYRG9fUEM5Z2dMQmdYbkV0TEZkYUIxMUtWT2h3eVR6MGhqRFFUeFVqdklVQzd1TzlLeUw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOM2xkR0Z4TFBwOUVtd2JTOFNTWmJOdENmNU9kUXViMXNlZVBHTEpwYzhaUzcxelZsNmFRQ09PdG1iTmFKOEdaOUFhVU1MNFhiWERYN0trQVc4WUtubGVWaEtwRnphTzFRX3UtU19SUUZYclpRNlB6YWV0ZnFIN3VKXzUzSG5IOEt1YWpGRXBXUnBBOUVvdE1uaGtJcw?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNdmR1WjllZWo5S013MU1kTmgzNWdZXzd3ejl4bHZFRlR6NUpLbWt5aHdaYkpzc3g4eG55M0Q2UGVHb01oSHBIUWZyY0tzTHNzMlU2clZ6NVFoZmJ3clRtYkZLWHFsWElfRHRibEw0UkZYMUNtQzNQcFVtejBQUjM4QVh6Yk9LdVMzOENZU1U3S0syTWRxSU9zdmFkQUlLY2hVQkFtVlFrN3lseGhEcWNPdA?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE10bm9vdXZ0RDJuVWNfMGo5bnQtLTJ6b2c3WTlMNExXaEsyOUpiNEd0cGt0YVNldlZHNEtvaThTOXV3LUpBVEFmcmNOOTBSZDNPbTBmNGlFVzgwYkFqQmY2eExVUjR6UEEtNk1hNzdkWEgtTWs2bTZNbGl2a0hOUQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOU0VRWHJGQjJ6RVYyWnVsYzZBdWg0MWVSVTlTLWptRkM1S0RaOUoxYy1fMnpjTFZWVEZwZXZEREE1c0hlSWEwMldITDhDYjFwRUJ3Z2V3ZW1pd19lV0JRaUpCbXEtZlctLWFGbnlHdTVwOE9RN0dfcVRqVWhsREFQclJDazdOUVZMX0lQci11VDUtSnNtT3EyM3RB?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
