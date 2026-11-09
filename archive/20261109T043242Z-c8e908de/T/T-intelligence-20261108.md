# T Intelligence Report

- ticker: **T**
- Report as_of: **2026-11-08**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/T/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/T/key-statistics/
- AI analysis snapshot as_of: **2026-11-08**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-09T04:39:31.564482+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 4, 'ai': 13, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **12** exact headline/source/date matches; prior report **20261108T041758Z-43fb2458/T** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **4**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 3}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 11 named publishers; 1 exact duplicates; 22 HTTPS source links; largest publisher share 31.82%; oldest publication 2026-11-01

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 21.6300 |
| Return 1D (%) | -0.8708 |
| Return 1W (%) | 1.0276 |
| Return 1M (%) | -10.4604 |
| Return YTD (%) | -8.7680 |
| Return 1Y (%) | -8.3992 |
| Annualized volatility (%) | 28.6921 |
| Beta vs SPY | -0.3725 |
| Max drawdown (%) | -28.8854 |
| Sharpe (rf=0) | -0.1621 |
| Downside deviation (rf=0, %) | 21.9799 |
| Sortino (rf=0) | -0.2116 |
| Historical VaR 95% (1D, %) | 2.8546 |
| Historical ES 95% (1D, %) | 4.6484 |
| Correlation vs SPY | -0.1759 |
| Tracking error vs SPY (%) | 33.8175 |
| P/E (trailing) | 11.57 |
| P/B | 1.37 |
| EV/EBITDA | 7.26 |
| Revenue growth (%) | 5.30 |
| Forward P/E (estimate) | 8.33 |
| Gross margin (%) | 59.74 |
| Operating margin (%) | 24.65 |
| Return on equity (%) | 11.61 |
| Free cash flow yield (%) | 8.21 |
| MA50 | 23.7891 |
| Close vs MA50 (%) | -9.0759 |
| MA200 | 24.4173 |
| Close vs MA200 (%) | -11.4152 |
| RSI (14, Wilder) | 41.7162 |
| MACD (12,26) | -0.6457 |
| MACD signal (9) | -0.7404 |
| MACD histogram | 0.0948 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'T': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 21.6300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.8708 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.0276 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -10.4604 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -8.7680 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -8.3992 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.6921 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.9799 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.2116 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8546 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6484 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1759 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.8175 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.3725 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.8854 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.1621 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.3327 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 59.7420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 24.6520 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.6130 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 8.2093 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 11.5668 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.7162 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0948 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -9.0759 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -11.4152 -> Clearly below the moving-average trend level.

## TAILWINDS

### AT&T stock: Higher outlook meets Georgia network risk
- Summary: AT&T stock: Higher outlook meets Georgia network risk
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxOUUdLal9aVjlfcHlkN0NHc0RvWmNKdXJDSlhBUlRlbHdxaDlpanFnY21RYlhRbHN2UjF2emhFMTBTUW5GMk5LdjR0NUhRZ2FMaVNLd0R3SVVTWDV3Vk4ta091UWJabE5XQlBZbXNYdUJucUJEV29tdzRPUm1waXh2ZHJOMGlqTkhLZi1yRHVxRjZabkdrdWdnNWhHVi1YZEU5Y2ZzUV9ab3hLc2ZnLW1CUDBBamJwUQ?oc=5>

### AT&T stock gains satellite handoff milestone as beta nears
- Summary: AT&T stock gains satellite handoff milestone as beta nears
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPcEpFOTZmc2lwREkwb2dvVUlSUmNrR0NKaFUzSTBVbXhjNWIteWJ1Q3NqOEVWRXdZUnFzaU0zak5BQnVIaFB0TWd6Qk5NUTgxWFZnX1B5UDBiaVBOckdoMWxBVWhnT0hwLTR3MDZLQ0FOQjlnc0xOLWtjOHdELWJmejFOZWZlZUVaN3o0NmpjTFJtazdSTmlLYmxTek1uV1M4OXcwSHREdVd5dDQtb1BwaU9sOFZBekxwTVhBY09n?oc=5>

### What Are AT&T Stock Bulls Not Worried About?
- Summary: Explores reasons investors remain bullish on AT&T despite market concerns.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNSXRWRW9oXy1xdXNnckFLLUJ1bGFZS1lTS282LTl3cGtnb0ZJMU1RWG42TlQxWFdac3hKM1hOeUxxTGN6ZERVNTNyYUhkWFo0VE5uaG9qRzlpSWQtY2JXRHhnUExueGs5a1F5LTFlSENsQVZkbm96UDRTaHQtUEdZSzkzazJCLWpPSTdwNW93eG5BaVJqbnowN2tXZmR5RFI0N2c?oc=5>

### AT&T stock: Fiber momentum lifts 2026 earnings outlook
- Summary: Fiber growth boosts 2026 earnings outlook.
- Date: 2026-11-03 | Impact: high | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxPX210U1RTc0VPU2M4M3pZNjNkSnVIWXFCOGw2elYzYVJQbVV3TXlwQUhJckQ2VVVxMkpKUU1GZEdmcERITzdLc1A2cTRzclkzUmM3Wi1PYnRJOXZvT0FVbVVVVHg0a2N5MnpKc3VEWklNMW44a0ItanlkMkdPOGxITVBhd3ViOVZMbnNKY3lKV0d5blBadFduX05ReUh3NXdBRTlMZW9KTzJvYTBIMzJwVXdxaWNneFE?oc=5>

### AT&T, T-Mobile Are Reportedly Ready To Boot Boost Mobile If SpaceX Buys It
- Summary: AT&T positions to block Boost Mobile acquisition by SpaceX, potentially protecting its market share.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxNOTBicHN0a1hkd3pjMGFKUjBpWVNMMTJmc2FGdjZRODBwd1VqcjZTTzVuSXFsd3duOEFhM2htVUlfX2lrbWcyUE9DN2xnMFlzVWlPNlhTbWNNOXlkQkw5eUh0d3U5UHlkM3ZXRVVRbGJCcUtwU3MxcThiWHc2V0FtU0t5NmZVQlhEYzJnWnNfV250aV9zUVJXNFIzQ3FiVEp3YXpPMnJERnhGYVdoSGJHWjQzMWFyVVNhTEFyUVNHSmZ3VUMwaWlHRnlEV09MSGVabVhhZmZPUnBOUQ?oc=5>

## HEADWINDS

### Do Wall Street Analysts Like AT&T Stock?
- Summary: Analysts' sentiment toward AT&T stock questioned.
- Date: 2026-11-01 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNbHVYTElaajZTMFN3Uy11UExZcXM2bWtmT2FZLVprVkVjS3B4QndlbGluWDlabDBsbGNndGpZMmNFOVRYbVBRTVNHdDRXd25vLXp6NnlrMWlEYXp1VEpHUUI1Sm1GVEg2WVZiOXIydkFYcm5IQTBnVlZCRjhVLXRFRVdyMVpfT2NRMUlUWDRSMEFyWmwxcl9ibQ?oc=5>

### Why AT&T Stock Slumped in October
- Summary: AT&T shares fell sharply in October, indicating investor concern.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxNcm8tYWtGY1RKVEpGcGc3THl3dXNvOTRQN0xoTXNBdnJwUmswMVg0d180VjlELTRFeFd2ejhvR1M5cE5QeUF3WDAwLTJpbFZQaFRuRG1NdkVON0drcGpFbjNvVU9uTngxU05FcmdWU2cwbDE0dS01MXRZSUdBZk9rSzJlRXdIRVE?oc=5>

### AT&T Stock Falls 11.8% in a Year: Should You Buy the Dip?
- Summary: AT&T shares dropped 11.8% over the year, raising doubts about value.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxOX1RqTnRGQkpieEpOckpkVlRHb0J2NUtFUkRJLTRyQWRMTDVvSFF3WWlidHZ6ZHZpN1FOQ0RfVzVSWGxWVVlOWHU1cm5rd0VBbC1RMC1KdzZPdFVHZUlad2FNbEp4Sk1vWjZuMXAwMlhOT05HbnJFRERRRjBmcnBkUVhRNk14ZlhHMmx6MUVVY3RDV0lIbnB3UnN2a1JaczN2eHpyTkNjN1ZYemU3QVkzdXdtamNueUNpWTFncGphd2t5NXJnN0lmcnY0UGxjcG01?oc=5>

## CATALYSTS

### AT&T Inc. $T Stock Sold by AIA Group Ltd
- Summary: AT&T Inc. $T Stock Sold by AIA Group Ltd
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPMTBzX0o1OTU0dTRQeGR4T0VHejFyM19Vdl9FZUpqNE5zZDIxamktWDg5eVN0czBiU0l3YTk5dDlzeXQwTG5YQ25nZlUxTGZPZ2E2eUhENVF5OHhDN2lEZlY4MW5LcVBfdVpMdmZaeDd5WDV3ZDMwNm8zWUVyZGM1MEFINHZVZTVfeFd1RG02U2w5Y2VjbTF1X0gzaUZYZ0k?oc=5>

### AT&T Inc. $T Stock Sold by Hennessy Advisors Inc.
- Summary: AT&T Inc. $T Stock Sold by Hennessy Advisors Inc.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOMGlUNEtuai12dU1id1JBNXNXdUo4Q0YxWkVLRTlQOTlpMkxWa1dGbGlrNFp6c04tcVVaa1NqUFVJamJpX0dWNU82b0c4Y1JSSW9BVklVM1VpTjNIS0VaX1hVSURUbl9fY1dhR1pwdXNTTTFmVVNaWktTQVVuVEVvaWxkQTN0OE1LdnRJb0dEaklBWmFXbWhKTjd2d1ZXZHZ5aGMzY1EwWXZKZw?oc=5>

### Is AT&T (T) Undervalued As Its Satellite Handoff Opens A New Coverage Question?
- Summary: AT&T’s satellite handoff raises coverage concerns, potentially affecting valuation.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQMENnU1dvSXNRUjl6S1hnVUZJT0oxRUphNUxqYTBFcHRjQmE0R1ROYVRfdDh6di1jT0Y0bWpYUk1LbU9uczBEMEhkNERQRW1TMUFLQUppSnNSSXBVSjUxNldYUGhSeEowcGtJSXA1clpvODV3R1BrcWdQMVIzSG9yREthclI4c3JwVUZxS2o1V043Xzg4cWluQXhGUnRERm8?oc=5>

### TELUS Faces Q3 Challenges Amid Strategic Shift; AT&T (T) Dividen
- Summary: AT&T announced a dividend amid TELUS’s Q3 challenges.
- Date: 2026-11-07 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNSTNSUU9EenFtcnVyRHdYNm5mMXU3MDUwcEJaT3FnaWhSRElpSjVwV1NsQUphRmN4SV9GLTk4cXJFNnFtc1c2dGF0cG91aXFCdXVSc044UWhJdDBPN2VIak5NWXptZHRraUJvRGVvdVVtUF90S2NPejRnWExXNHlLVEp4dF9wMXh5WWdVV2RRVXNDZlZ3cWREOGNyRnJhUTFoeTlhQ2NCSmduNk0zWlFFSlJnZlVjbDhXbnZZZXJhcjlMdw?oc=5>

### AT&T Inc. $T Stock Holdings Decreased by International Assets Investment Management LLC
- Summary: International Assets Investment Management reduced its AT&T stake.
- Date: 2026-11-06 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxNWngzbGdtalpYRlpjU2w5cUtsTldiLUZMVVcxZElOODVZdkpNc0pJSlYzc0dqc0MyQ0h3enlmbHpJNWZBdDBDRXFRLUNMUjJtSXNRSVJiVjJfT2JhMkF4MS1JY0psQVBFekRwcHgtU3FsSDRyQ1RYWmxibUZvVlV1Y0d1d2RyNUplRElTOUtfaWlFdUNYZ3JlUERyZjI0N19NUTBKY0luTS1YT3I0UmUxU0xZV0xEdmR0Qk5WYnF1R3lmSzlQYUx0Sk1SYnprUXduSFBZOG5SckxTYmpEZ1E?oc=5>

### AT&T Inc. $T Stock Position Lifted by Alps Advisors Inc.
- Summary: Alps Advisors increased its AT&T holdings.
- Date: 2026-11-07 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxNelZ5NTR5S09hQVlkZ2Y3dFdHNG93ZkFOc3ZGckt0UU5VdTVCRGpnT0JYam13bGJveUxMR090anM3RVdmcWNCOV8tSkstWGhPc2dUamVuWWtXeC0xd0JfZ3hkeXRDY2piVzFvVmwwaFlmdUwyckFHVnpDejY4My16YzhzS1NwNTV5OFlRWGpvQ0VoSXlqTHhWazR1TkhTY2xkMlhRbkZjQzhGakZPMFRDbFB5cw?oc=5>

### AT&T Inc. $T Stock Position Boosted by Rakuten Investment Management Inc.
- Summary: Rakuten Investment Management increased its stake in AT&T, signaling confidence in the telecom's prospects.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPbnU2VlpQa1YwTy1XSVJEWXZZUVU0dGlnNzVqazBMbUpBV281cmt0bW40cE1JUy01YTBvWS11dXNlLWF2ZTlQTDRIZjN6c3V1QXVPcU50UEZCekpjTHEtNENtd25vRUdBZ2RQMElnQmVRR2kxMzN6cU14ejFxNWhCaUVOZ01WYmloSGhwT1dybXJ3eWgydlpsbldDUTBZR2c3a2FBVTNJYTZhNG9VWDZYRUxTZjhMOHRPcWpuWl82NzVBeEdlNnFJdHVR?oc=5>

### AT&T Inc. $T Stock: Trek Financial LLC Boosts Stake
- Summary: Trek Financial LLC increases its stake in AT&T, signaling confidence in the company.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQbXgwckVldlJXcnJWMDhzazFkb05uVW1YeXpUZ0NPb2tMYUlFVFZ0M3pQVGo2ZGk3ZHptTWdqcWZaQ2JfNHlCZWhaVVNDQ0NpcHhzdkF2RlZ4ejFVdTZrblB6X1p6UDdiRkJhQkRodk1xczhPQkw3YVVKTVRxdllnTnlBdG5zOEcyNEd1UWI3TmZpcTRUZFE1dmFDUzlOZHgwbzVYaHF3LXVERjV6?oc=5>

### A phone connection switched from towers to a satellite without interruption. AT&T expects real-world trials next.
- Summary: AT&T plans real‑world trials of satellite‑based phone service after successful tower‑to‑satellite switch.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxQSnJWY2hhNzhnRDd6TDhzNU1RMVpMajVBQ1dDNVRVaFBZQWM4blQ5eHlnLTdfczFGdGtobVp5YS1wRHZBSHNfZ09QdndRMndNbE40Y0UwSWtLZWJMMlh0OFJ4bVU5U2NMWWFUaFZwZUV5bGtzR2VmNFpEZHNBc0FMWV9VQjQtQTBzejdGMkNKMVBHaV9vZzN6SFlzdjVIVlFFZnBmSUZnb0dFeHB3YWFrQ2ZoNA?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **T** | **11.57** | **1.37** | **7.26** | **5.30** | **145,709,924,352.00 USD** | **-8.40** |
| VZ | 11.66 | 1.79 | N/A | 1.50 | 189,366,681,600.00 USD | 22.38 |
| TMUS | 15.62 | 3.06 | N/A | 7.40 | 171,612,749,824.00 USD | -17.70 |
| BCE | 11.69 | 1.35 | 7.38 | 2.20 | 20,161,208,320.00 USD | -1.68 |

Peers fetched as_of: 2026-11-08; T reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-08

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMitgFBVV95cUxOUUdLal9aVjlfcHlkN0NHc0RvWmNKdXJDSlhBUlRlbHdxaDlpanFnY21RYlhRbHN2UjF2emhFMTBTUW5GMk5LdjR0NUhRZ2FMaVNLd0R3SVVTWDV3Vk4ta091UWJabE5XQlBZbXNYdUJucUJEV29tdzRPUm1waXh2ZHJOMGlqTkhLZi1yRHVxRjZabkdrdWdnNWhHVi1YZEU5Y2ZzUV9ab3hLc2ZnLW1CUDBBamJwUQ?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPcEpFOTZmc2lwREkwb2dvVUlSUmNrR0NKaFUzSTBVbXhjNWIteWJ1Q3NqOEVWRXdZUnFzaU0zak5BQnVIaFB0TWd6Qk5NUTgxWFZnX1B5UDBiaVBOckdoMWxBVWhnT0hwLTR3MDZLQ0FOQjlnc0xOLWtjOHdELWJmejFOZWZlZUVaN3o0NmpjTFJtazdSTmlLYmxTek1uV1M4OXcwSHREdVd5dDQtb1BwaU9sOFZBekxwTVhBY09n?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNSXRWRW9oXy1xdXNnckFLLUJ1bGFZS1lTS282LTl3cGtnb0ZJMU1RWG42TlQxWFdac3hKM1hOeUxxTGN6ZERVNTNyYUhkWFo0VE5uaG9qRzlpSWQtY2JXRHhnUExueGs5a1F5LTFlSENsQVZkbm96UDRTaHQtUEdZSzkzazJCLWpPSTdwNW93eG5BaVJqbnowN2tXZmR5RFI0N2c?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxPX210U1RTc0VPU2M4M3pZNjNkSnVIWXFCOGw2elYzYVJQbVV3TXlwQUhJckQ2VVVxMkpKUU1GZEdmcERITzdLc1A2cTRzclkzUmM3Wi1PYnRJOXZvT0FVbVVVVHg0a2N5MnpKc3VEWklNMW44a0ItanlkMkdPOGxITVBhd3ViOVZMbnNKY3lKV0d5blBadFduX05ReUh3NXdBRTlMZW9KTzJvYTBIMzJwVXdxaWNneFE?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxNOTBicHN0a1hkd3pjMGFKUjBpWVNMMTJmc2FGdjZRODBwd1VqcjZTTzVuSXFsd3duOEFhM2htVUlfX2lrbWcyUE9DN2xnMFlzVWlPNlhTbWNNOXlkQkw5eUh0d3U5UHlkM3ZXRVVRbGJCcUtwU3MxcThiWHc2V0FtU0t5NmZVQlhEYzJnWnNfV250aV9zUVJXNFIzQ3FiVEp3YXpPMnJERnhGYVdoSGJHWjQzMWFyVVNhTEFyUVNHSmZ3VUMwaWlHRnlEV09MSGVabVhhZmZPUnBOUQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNbHVYTElaajZTMFN3Uy11UExZcXM2bWtmT2FZLVprVkVjS3B4QndlbGluWDlabDBsbGNndGpZMmNFOVRYbVBRTVNHdDRXd25vLXp6NnlrMWlEYXp1VEpHUUI1Sm1GVEg2WVZiOXIydkFYcm5IQTBnVlZCRjhVLXRFRVdyMVpfT2NRMUlUWDRSMEFyWmwxcl9ibQ?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxNcm8tYWtGY1RKVEpGcGc3THl3dXNvOTRQN0xoTXNBdnJwUmswMVg0d180VjlELTRFeFd2ejhvR1M5cE5QeUF3WDAwLTJpbFZQaFRuRG1NdkVON0drcGpFbjNvVU9uTngxU05FcmdWU2cwbDE0dS01MXRZSUdBZk9rSzJlRXdIRVE?oc=5
- https://news.google.com/rss/articles/CBMie0FVX3lxTFB2YXVlREQ3R0NieWVFMkRISThWcE5kRFRqcXVfdjVzUy0zenpJNVo4eFQ2Wmt5Q1Q1N002cVZ6MTUyU2JLYk9tQVg0bFM3d0VNU013Y180allLd1ZPeHE1OUtOeURuc0xrV0N5S3h4M2pmRGxwMURMV1JlOA?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxOX1RqTnRGQkpieEpOckpkVlRHb0J2NUtFUkRJLTRyQWRMTDVvSFF3WWlidHZ6ZHZpN1FOQ0RfVzVSWGxWVVlOWHU1cm5rd0VBbC1RMC1KdzZPdFVHZUlad2FNbEp4Sk1vWjZuMXAwMlhOT05HbnJFRERRRjBmcnBkUVhRNk14ZlhHMmx6MUVVY3RDV0lIbnB3UnN2a1JaczN2eHpyTkNjN1ZYemU3QVkzdXdtamNueUNpWTFncGphd2t5NXJnN0lmcnY0UGxjcG01?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPMTBzX0o1OTU0dTRQeGR4T0VHejFyM19Vdl9FZUpqNE5zZDIxamktWDg5eVN0czBiU0l3YTk5dDlzeXQwTG5YQ25nZlUxTGZPZ2E2eUhENVF5OHhDN2lEZlY4MW5LcVBfdVpMdmZaeDd5WDV3ZDMwNm8zWUVyZGM1MEFINHZVZTVfeFd1RG02U2w5Y2VjbTF1X0gzaUZYZ0k?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOMGlUNEtuai12dU1id1JBNXNXdUo4Q0YxWkVLRTlQOTlpMkxWa1dGbGlrNFp6c04tcVVaa1NqUFVJamJpX0dWNU82b0c4Y1JSSW9BVklVM1VpTjNIS0VaX1hVSURUbl9fY1dhR1pwdXNTTTFmVVNaWktTQVVuVEVvaWxkQTN0OE1LdnRJb0dEaklBWmFXbWhKTjd2d1ZXZHZ5aGMzY1EwWXZKZw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQMENnU1dvSXNRUjl6S1hnVUZJT0oxRUphNUxqYTBFcHRjQmE0R1ROYVRfdDh6di1jT0Y0bWpYUk1LbU9uczBEMEhkNERQRW1TMUFLQUppSnNSSXBVSjUxNldYUGhSeEowcGtJSXA1clpvODV3R1BrcWdQMVIzSG9yREthclI4c3JwVUZxS2o1V043Xzg4cWluQXhGUnRERm8?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNSTNSUU9EenFtcnVyRHdYNm5mMXU3MDUwcEJaT3FnaWhSRElpSjVwV1NsQUphRmN4SV9GLTk4cXJFNnFtc1c2dGF0cG91aXFCdXVSc044UWhJdDBPN2VIak5NWXptZHRraUJvRGVvdVVtUF90S2NPejRnWExXNHlLVEp4dF9wMXh5WWdVV2RRVXNDZlZ3cWREOGNyRnJhUTFoeTlhQ2NCSmduNk0zWlFFSlJnZlVjbDhXbnZZZXJhcjlMdw?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxNWngzbGdtalpYRlpjU2w5cUtsTldiLUZMVVcxZElOODVZdkpNc0pJSlYzc0dqc0MyQ0h3enlmbHpJNWZBdDBDRXFRLUNMUjJtSXNRSVJiVjJfT2JhMkF4MS1JY0psQVBFekRwcHgtU3FsSDRyQ1RYWmxibUZvVlV1Y0d1d2RyNUplRElTOUtfaWlFdUNYZ3JlUERyZjI0N19NUTBKY0luTS1YT3I0UmUxU0xZV0xEdmR0Qk5WYnF1R3lmSzlQYUx0Sk1SYnprUXduSFBZOG5SckxTYmpEZ1E?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxNelZ5NTR5S09hQVlkZ2Y3dFdHNG93ZkFOc3ZGckt0UU5VdTVCRGpnT0JYam13bGJveUxMR090anM3RVdmcWNCOV8tSkstWGhPc2dUamVuWWtXeC0xd0JfZ3hkeXRDY2piVzFvVmwwaFlmdUwyckFHVnpDejY4My16YzhzS1NwNTV5OFlRWGpvQ0VoSXlqTHhWazR1TkhTY2xkMlhRbkZjQzhGakZPMFRDbFB5cw?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPbnU2VlpQa1YwTy1XSVJEWXZZUVU0dGlnNzVqazBMbUpBV281cmt0bW40cE1JUy01YTBvWS11dXNlLWF2ZTlQTDRIZjN6c3V1QXVPcU50UEZCekpjTHEtNENtd25vRUdBZ2RQMElnQmVRR2kxMzN6cU14ejFxNWhCaUVOZ01WYmloSGhwT1dybXJ3eWgydlpsbldDUTBZR2c3a2FBVTNJYTZhNG9VWDZYRUxTZjhMOHRPcWpuWl82NzVBeEdlNnFJdHVR?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQbXgwckVldlJXcnJWMDhzazFkb05uVW1YeXpUZ0NPb2tMYUlFVFZ0M3pQVGo2ZGk3ZHptTWdqcWZaQ2JfNHlCZWhaVVNDQ0NpcHhzdkF2RlZ4ejFVdTZrblB6X1p6UDdiRkJhQkRodk1xczhPQkw3YVVKTVRxdllnTnlBdG5zOEcyNEd1UWI3TmZpcTRUZFE1dmFDUzlOZHgwbzVYaHF3LXVERjV6?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxQSnJWY2hhNzhnRDd6TDhzNU1RMVpMajVBQ1dDNVRVaFBZQWM4blQ5eHlnLTdfczFGdGtobVp5YS1wRHZBSHNfZ09QdndRMndNbE40Y0UwSWtLZWJMMlh0OFJ4bVU5U2NMWWFUaFZwZUV5bGtzR2VmNFpEZHNBc0FMWV9VQjQtQTBzejdGMkNKMVBHaV9vZzN6SFlzdjVIVlFFZnBmSUZnb0dFeHB3YWFrQ2ZoNA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
