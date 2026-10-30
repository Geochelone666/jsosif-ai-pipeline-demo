# NFLX Intelligence Report

- ticker: **NFLX**
- Report as_of: **2026-10-29**
- Market data as_of: **2026-10-29**
- Quant sources: https://finance.yahoo.com/quote/NFLX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NFLX/key-statistics/
- AI analysis snapshot as_of: **2026-10-29**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-30T02:18:32.374716+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 3, 'ai': 17, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261028T015717Z-533e470c/NFLX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 9 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 29.17%; oldest publication 2026-10-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 62.0500 |
| Return 1D (%) | 0.0968 |
| Return 1W (%) | -7.4571 |
| Return 1M (%) | -11.7354 |
| Return YTD (%) | -33.8204 |
| Return 1Y (%) | -43.6119 |
| Annualized volatility (%) | 35.9172 |
| Beta vs SPY | 0.2067 |
| Max drawdown (%) | -46.4449 |
| Sharpe (rf=0) | -1.4214 |
| Downside deviation (rf=0, %) | 26.4621 |
| Sortino (rf=0) | -1.9293 |
| Historical VaR 95% (1D, %) | 3.5133 |
| Historical ES 95% (1D, %) | 5.1308 |
| Correlation vs SPY | 0.0731 |
| Tracking error vs SPY (%) | 37.2130 |
| P/E (trailing) | 17.93 |
| P/B | 8.70 |
| EV/EBITDA | 16.55 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 16.45 |
| Gross margin (%) | 50.69 |
| Operating margin (%) | 34.63 |
| Return on equity (%) | 53.46 |
| Free cash flow yield (%) | 9.86 |
| MA50 | 73.0338 |
| Close vs MA50 (%) | -15.0393 |
| MA200 | 81.7287 |
| Close vs MA200 (%) | -24.0781 |
| RSI (14, Wilder) | 30.4905 |
| MACD (12,26) | -2.6520 |
| MACD signal (9) | -2.0512 |
| MACD histogram | -0.6008 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NFLX': 271, 'SPY': 271}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 62.0500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.0968 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -7.4571 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -11.7354 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -33.8204 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -43.6119 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 35.9172 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.4621 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.9293 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.5133 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1308 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0731 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.2130 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2067 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -46.4449 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.4214 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.4530 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.6850 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 34.6320 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 53.4630 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 9.8601 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.9335 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 30.4905 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.6008 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -15.0393 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -24.0781 -> Clearly below the moving-average trend level.

## TAILWINDS

### Netflix (NFLX) Stock Stays Cheap After Its 58% Three Year Gain
- Summary: Netflix (NFLX) Stock Stays Cheap After Its 58% Three Year Gain
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOVmpXNWh4OWZNOUI5d0lnd1NGYzBBU2tLSFhPeDY3UFpFM1ZXODVVdzNuMy1CM1pMelUxdFZEQ25XVW5NMHlPYnZ1WFZ3RXZXbXB6aDg2eFpWNUF5RC1KWUFJc2dmMHlkbkJQY1k2Z2JLb25RY0J6cURXR2hxV1AzZDZMM0dvWW84WHFIalR2Q05pbDZzMlBpekhKdw?oc=5>

### Netflix: The Ad Miss Is Offset By Record Buybacks
- Summary: Record buybacks counteract ad revenue miss, supporting financial health.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOQUVBS2FkdDBjMEpaN2tqRm00OG1WOEJFUnFTMHctQWVVamxSOFdhUkdnLWhqVi1wZ1VOUXRuNGNJOTV2LUpmcW9OSXdFTVRfcFJUb19CWEl1ek1MU1RXcTlhRzU1M0cxWnRWbzh3dGk0S2VIcXh0STRiRkRiVHdfN0hncFFpVHVuXzlTRjgwcTAtMG8?oc=5>

### Walt Disney (DIS) vs. Netflix (NFLX): Which Entertainment Stock Offers More Upside, According to Wall Street?
- Summary: Comparative analysis of Disney and Netflix stock upside potential for investors.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxOM1dDa19uWmF4RFhGdXhhM2FlVy1KcFNRV01aQ0VJWFRoVFR3a0Y0NDlfc0l6X3h4YmNoTllFaFVBMzBacG1LMWdLY1hXYlB4Sy1FMmpUbWFHbFBWdjJlTW1yTHhld21WYUZRclFsVkhkaEdGUWlybUdXUG82OExSV0p6NS1fWDdYQnRpYjVLdThocE1JMTlmYnVrU3dRRDlPTVNkQ0VZbEktcTJIRjJDOWdCc1N0cTloemRKbDY3emJQT1ZnekVIZWNCQQ?oc=5>

### The Battle That May Matter Most for Netflix Stock Isn't Against Disney
- Summary: Explores other competitors impacting Netflix stock beyond Disney.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNMEJjQl9vSl9kWk5nemlNQW5QangydndZUU9JRW52bjhwZ1ozX0Fnd0xhc21iUjBfNXNUV0VibVVUaHpmeFpWLVBEcHlpMXFkbXFZSzBBUzd1OV93a091XzVxdjQ0bDNyV0dYTFVaMmJuektoVmM3Z21XQW9aZUVxRVpPemFIaU5NdGZDX2tJY2pUYnRHRmY0?oc=5>

### 3 Magnificent Stocks Trading Near Their 52-Week Lows
- Summary: Highlights Netflix among three stocks near 52-week lows, suggesting potential buying opportunities.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxOeWlPLXk0VGRHRGZZb2ZCVWxiNmI1cW9sVFd3Um5iNDZVeW1HY1lOaXRiRVdMc1RBdWI1ZDlSRU16cmd2bDJ5WU1zeWNFemo4WnczYWtjamhSdENwOWJKc3p2cUNhS2h3czdKYXpJSUJfT202MWpTMDZJT0gzcE8tYWNwUEJLZkR0dkN0bktIQ1lDeGpIcGtHZnEyQ091WUpObzBrRmFjWlhORFdRRWVDQzZHdFJEck5JU1N5LWdzMVJmMnQtSjhTMV9jWTk0enBiMkVaTnNB?oc=5>

### What Should Netflix Stock Investors Be Watching Now?
- Summary: Provides current factors investors should monitor for Netflix stock performance.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQUHJTT2tVYjBfMGpTdlVzaE1DWlF4NHdNOFZpeENYcjB0OEw4QzlPSF84Q3hGYy1EQVFmZHp6V0l1N2J3SUNHNTdMb0RMS3FTMUFYV1EzWGZxTmtTM2lUYmVHLWp6Q3lMZU9sQ0FMVEJGaHNGOTVSb2pnWDlQRnJvSXBMSl93SWxmWVlENklwbmlHcEcxdWpnNGx1VkJNdkxVSlE4bm9yd0dxYlVTVmNUSWpR?oc=5>

### Netflix Stock: Should You Buy the Post-Earnings Dip?
- Summary: Discusses buying Netflix stock after earnings dip, evaluating risk and reward.
- Date: 2026-10-26 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOUVpFVXFOOVlVNWNkMUFEVzJhZjlPaEdVU1lfTzRtLUtlcF9QdEVwU0drNnkxMlRialctYlZhcUJ4d3kxenBQNFlkVE1BT0tadHZBNVc0by1hWjhoVjJyUDQxcEZXUFZVSERaaGRwV2JyeHRhQ3pTbkpxVVdOdzBFTW9pSFJVZll0VmRoMjVkR2tIU3Iyal9ZZ1U0WGQ?oc=5>

### Netflix Q3: An Opportunity Hiding In Plain Sight (NASDAQ:NFLX)
- Summary: Netflix's Q3 earnings reveal hidden growth opportunities.
- Date: 2026-10-26 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxQUTBjcy1lMWVqMHEwVzJ6dmNJYmJuM011ZG5pUXFlQTRWbGs3MkpEYlhzSmp5ajJhcWUzYnQyQkQwV2ZuZllmOFZlYm5lYWRITHZHcS1rS201OWg4ZElvSU1jVFdMeHhsck9qZkZtN0IyWWFkZndsSHVoUDRYclczaVNCTWVsanVLTUUxS285U3NQdw?oc=5>

## HEADWINDS

### Netflix Shares Are Down 9% Since Earnings. Is the Stock a Buy?
- Summary: Netflix Shares Are Down 9% Since Earnings. Is the Stock a Buy?
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPZ1pZb216M0NKaGhqWmdoXzkwOC1TQjFzRExLVEpXYVpSU19HTWN5QUVKbTg3cGNYem9nQmw5Mmsxd0V1M2IyMmJQWDJrdUszTllwRmFsRG5UNTZpTjRrVWRCYzBsdGlGazhkeGFwNW5ENUhXRzFEOUJ1U0J4aHJtaDhYdW5hNWdPM1FCajlZZk1pUQ?oc=5>

### Netflix Is Now Down 29% This Year: Is NFLX Stock Hopeless or Ready for a Rebound?
- Summary: Netflix shares fell 29% YTD, raising concerns about future growth and valuation.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxQLUd5d2xvbWNXbkpvYmY3VmhEYUtsbU83V2VIMnptYW5WbUNMZ1dibkJmZEwxYUg0RXhmOWRQZ0t6aW5RaTNoUkQ4Y3ZEZ3FaU2FGSjl2VC1uQlE3bkNnVUtaNi1DY1RzS05zeE55ZGNuS2UtYmlSbTR2ZDlqRXNvaTF1V3QyalNmNkdYN3JsTU50bDZwNXFvR0FVajlpODFvWlZrSGlpYmhDRTg0a0RkWTRLWXFFdzg1YmxZc3RFSQ?oc=5>

### Netflix Is Down 51% From Its High. History Suggests This Is What Happens Next.
- Summary: Shares dropped 51% from peak, hinting at potential further decline.
- Date: 2026-10-25 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPZTg4c2VtT2d1SV9meTFhZFpzN2ItRk85YXlQWnAwQUxDRm5VMmhBU0RrVXAyRWROcWk4RUpFdk4yWlhkc3dlUjFyU3hkVDVkaklFNC0zTmRPRmJZNHQxN2xvYmQtMVlDVm9Bd2VJdkZIOEI1Mnh0blZMNEJ4d0FGOXBvY25ic1UwV2NYa2ZPcw?oc=5>

### Down Roughly 50% From Its Highs, Is Netflix Stock Finally a Buy?
- Summary: Stock price has dropped 50%, questioning buy potential.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPaUxsUFM0YmRJeEtMU3VUTG1kT0FEMVpHckhVenVyMXZ5Y25YZFlhWGc5SklnZWJJNHljMzA0NmlGTGdTU3VYTUtlenBKcFhLcXhYN0MxdGVyQkk4eDZfQU9WZ3hOelJoU01ocnQ3UEQ0R0ZNWWRiSEZIOERkaTBoMnMtY3Jnam9CaTlKMk41OGpPMVdl?oc=5>

### Netflix Just Posted a Record Margin. So Why Is Wall Street Panicking?
- Summary: Despite record margin, market panic suggests concerns over future growth.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQVnpmQm5iU3RTNWg3S19pMUNyeXIxdnFXMXItXzJRNUxnQmpfUDlCZTlJc0dGN3hBRXNVYmpTaG8wVlluQmZwOWVBQ0NEdWc5dG1ZUkhka0gya0hQem5rMUI3NlZMS3V3bVZMdVFCSGRycFRfWmJxMU9ja0JtNHlEb3dNRUJ0cDF5NDVXQWN3S3FmRC1GanRVM2toSnY2YXc?oc=5>

### Why Did NFLX, OPEN, WHR Stocks Tumble To 52-Week Lows Today?
- Summary: NFLX shares fell to 52-week lows, indicating market weakness.
- Date: 2026-10-28 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxOUnB5cE1abmFuN1Q3NkVwR2s0SG5IOXlISEMwVnJEV3hYdlVXaEd4Qi1zZHhKNnJhMWFNdzNydE54YWhEZlkyV29GY3laZ1VzRXNFRTUtbmV4aTBlWnlQS0hHMWJPeWFtaEtSOGhxeXNpX25ocXhLV2NTNmlnV1dvVDUtQVJpOTdqVnZjTkpEbw?oc=5>

### Should You Buy Netflix Stock After Its 51% Plunge?
- Summary: Netflix stock plunged 51%, raising doubts about its valuation.
- Date: 2026-10-24 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOS0JnUml0VTFqcjdudFhjaW55d3M3cnpzMjFDby1iODYyUFJiZzN5TkExMFhHVEFjb0JjRDFuSVJEaE03MWUtdkJrcXN6LWRtS01WYmtFWHI5U0Y5dFhqbUdXYS1KVkJhdE5CY2tQN0thdC01UVRUeWJLVlNUY2VKa0NMSXlka0p5MFBzZ1lxa3hydU5tVVdF?oc=5>

### Testing Support Level, NFLX Stock Drops 0.85% on Wednesday
- Summary: NFLX shares dipped 0.85% as support levels were tested.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQLU5CWG81Yk1fTTVVVkJuQ0o2dDNLd25EQlBld1VjN09SRW5mcG1ORHBjS1BRTzFnbDBWWWdCT1kxV3VoNXlTVWMyUmpOd0NvY09ENjhSSl83NTJ6bmd4al82R196clc0TVNFUFFfNE1fOVdGOWgwS0NPOVNXSFo3UlB1c2FMalBZVm9QVjdsdk1rTzIwQ3Y5MzRTUQ?oc=5>

## CATALYSTS

### Netflix (NFLX) Stock Fair Value Falls After Cautious Q3 Analyst Revisions
- Summary: Netflix (NFLX) Stock Fair Value Falls After Cautious Q3 Analyst Revisions
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQSE1oLXBDN2dSRUZabVZhbzJvTDZpSVV3NmNVQ2VlYjJJQVVRSTBfQmJHT2FhWGt6LUl4NjFBMElxaVFGajh2eWlIRm1abUp2cFVoekg1VGdZN0pmbGV2ckZjWXB2ZzcwRWV2RkZ6S1pqVTBFNjRuamREVk5RMkoxZUw5ZjZyQXg1SDNHdzRIWDhweXJYTGpacC1R?oc=5>

### Netflix: Price Increases Are No Longer Providing Unchecked Upside (Downgrade) (NFLX)
- Summary: Downgrade signals Netflix's price hikes no longer yield upside.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxONkdVeC1kd29pUUlKbjZfd3lYckhoSFNnbktmU1VIbVFBR08yV3pYcWo3TDkzbE43SnBJQ2RlTE84OUhnTnRnYWNsTVo4N2hBMlVKdVotVWdDVV9IdGhxbWJKLUd3Yk1fZDBKTzc0Uk1SUzc1RUdBLXpqVkdfWkV4ay1FOXpwTTNvMGZGUmxiUEJUdlVnZW1pZ2RXWW1GNC1JaVczaWczU01NRWJ6UTV2Rm9VNUZMZw?oc=5>

### Wall Street Is Treating Netflix Like It's Broken, But I'm Still Bullish (NASDAQ:NFLX)
- Summary: Analyst remains bullish despite market skepticism.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPRnlVQVVLX05hNGdyek9rTjNybEw5b2lJcEFnN3BlMElCNEpDZmpRcnJfSDNWbHRxS2NXS3NyQ1FkbDZLZzAzdjl0RklFMk55aTZ4REF2SDlnVWpGZmk4T2NHTGNoSVVUZWM3WTVWMkl0UEFDSFJiRllqX3RRLXBXZkpIY21HTzhWZ0ZIemdvVnoxT0VqZC1UamZPTENnWDloNmZ6VDBZVWN0QQ?oc=5>

### Netflix Stock Has Always Overcome the Odds. Has It Finally Hit a Wall?
- Summary: Questioning if Netflix's resilience has limits.
- Date: 2026-10-24 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPMlEtcTktT2NrV1BGT2V2UVhMVFE5OE9sQVFPMmhfdUh5dlF3SzI5QXdmTF9JODNXZFFIY2IyQy1uemZYZ2NIdENSOWktblBtY3RvMHlRaFR5aDRsQzl3b0JFM1ByRHpDOGhxODBwc3E5ekVpamtvTTlNVVhfNnVyOEVROGpGcno2NjZINmVwLWU3SENkN2hR?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NFLX** | **17.93** | **8.70** | **16.55** | **11.80** | **258,372,452,352.00 USD** | **-43.61** |
| DIS | 22.87 | 1.74 | 11.41 | 6.80 | 191,506,841,600.00 USD | 2.06 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| CMCSA | 7.05 | 0.85 | 4.74 | -6.10 | 79,080,906,752.00 USD | -12.25 |

Peers fetched as_of: 2026-10-29; NFLX reuses existing data (market data as_of: 2026-10-29); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-19 (yfinance; expected dates may change)

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
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 12,874,176,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,663,927,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimwFBVV95cUxOVmpXNWh4OWZNOUI5d0lnd1NGYzBBU2tLSFhPeDY3UFpFM1ZXODVVdzNuMy1CM1pMelUxdFZEQ25XVW5NMHlPYnZ1WFZ3RXZXbXB6aDg2eFpWNUF5RC1KWUFJc2dmMHlkbkJQY1k2Z2JLb25RY0J6cURXR2hxV1AzZDZMM0dvWW84WHFIalR2Q05pbDZzMlBpekhKdw?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOQUVBS2FkdDBjMEpaN2tqRm00OG1WOEJFUnFTMHctQWVVamxSOFdhUkdnLWhqVi1wZ1VOUXRuNGNJOTV2LUpmcW9OSXdFTVRfcFJUb19CWEl1ek1MU1RXcTlhRzU1M0cxWnRWbzh3dGk0S2VIcXh0STRiRkRiVHdfN0hncFFpVHVuXzlTRjgwcTAtMG8?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxOM1dDa19uWmF4RFhGdXhhM2FlVy1KcFNRV01aQ0VJWFRoVFR3a0Y0NDlfc0l6X3h4YmNoTllFaFVBMzBacG1LMWdLY1hXYlB4Sy1FMmpUbWFHbFBWdjJlTW1yTHhld21WYUZRclFsVkhkaEdGUWlybUdXUG82OExSV0p6NS1fWDdYQnRpYjVLdThocE1JMTlmYnVrU3dRRDlPTVNkQ0VZbEktcTJIRjJDOWdCc1N0cTloemRKbDY3emJQT1ZnekVIZWNCQQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNMEJjQl9vSl9kWk5nemlNQW5QangydndZUU9JRW52bjhwZ1ozX0Fnd0xhc21iUjBfNXNUV0VibVVUaHpmeFpWLVBEcHlpMXFkbXFZSzBBUzd1OV93a091XzVxdjQ0bDNyV0dYTFVaMmJuektoVmM3Z21XQW9aZUVxRVpPemFIaU5NdGZDX2tJY2pUYnRHRmY0?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxOeWlPLXk0VGRHRGZZb2ZCVWxiNmI1cW9sVFd3Um5iNDZVeW1HY1lOaXRiRVdMc1RBdWI1ZDlSRU16cmd2bDJ5WU1zeWNFemo4WnczYWtjamhSdENwOWJKc3p2cUNhS2h3czdKYXpJSUJfT202MWpTMDZJT0gzcE8tYWNwUEJLZkR0dkN0bktIQ1lDeGpIcGtHZnEyQ091WUpObzBrRmFjWlhORFdRRWVDQzZHdFJEck5JU1N5LWdzMVJmMnQtSjhTMV9jWTk0enBiMkVaTnNB?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQUHJTT2tVYjBfMGpTdlVzaE1DWlF4NHdNOFZpeENYcjB0OEw4QzlPSF84Q3hGYy1EQVFmZHp6V0l1N2J3SUNHNTdMb0RMS3FTMUFYV1EzWGZxTmtTM2lUYmVHLWp6Q3lMZU9sQ0FMVEJGaHNGOTVSb2pnWDlQRnJvSXBMSl93SWxmWVlENklwbmlHcEcxdWpnNGx1VkJNdkxVSlE4bm9yd0dxYlVTVmNUSWpR?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOUVpFVXFOOVlVNWNkMUFEVzJhZjlPaEdVU1lfTzRtLUtlcF9QdEVwU0drNnkxMlRialctYlZhcUJ4d3kxenBQNFlkVE1BT0tadHZBNVc0by1hWjhoVjJyUDQxcEZXUFZVSERaaGRwV2JyeHRhQ3pTbkpxVVdOdzBFTW9pSFJVZll0VmRoMjVkR2tIU3Iyal9ZZ1U0WGQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxONTY1Mlp1b2dvX0lvZnJVNFh6SE0xeDhWbUVnQ2FGeXB5LXJDVUNWcHhSOUpjMHRFdnB4Y0pqdlYzdW9FMWlJZktMU1BPZUQ0eUUwY01OQkk1aElSVDJzNjhnZFlOYkJLVjlzV1Bqc3g5dVprUFdWbkl5WWlacmZQeXh0YXB0OHhXR3MtUGVuUTBfdWFxMzBKNA?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxQUTBjcy1lMWVqMHEwVzJ6dmNJYmJuM011ZG5pUXFlQTRWbGs3MkpEYlhzSmp5ajJhcWUzYnQyQkQwV2ZuZllmOFZlYm5lYWRITHZHcS1rS201OWg4ZElvSU1jVFdMeHhsck9qZkZtN0IyWWFkZndsSHVoUDRYclczaVNCTWVsanVLTUUxS285U3NQdw?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPZ1pZb216M0NKaGhqWmdoXzkwOC1TQjFzRExLVEpXYVpSU19HTWN5QUVKbTg3cGNYem9nQmw5Mmsxd0V1M2IyMmJQWDJrdUszTllwRmFsRG5UNTZpTjRrVWRCYzBsdGlGazhkeGFwNW5ENUhXRzFEOUJ1U0J4aHJtaDhYdW5hNWdPM1FCajlZZk1pUQ?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxQLUd5d2xvbWNXbkpvYmY3VmhEYUtsbU83V2VIMnptYW5WbUNMZ1dibkJmZEwxYUg0RXhmOWRQZ0t6aW5RaTNoUkQ4Y3ZEZ3FaU2FGSjl2VC1uQlE3bkNnVUtaNi1DY1RzS05zeE55ZGNuS2UtYmlSbTR2ZDlqRXNvaTF1V3QyalNmNkdYN3JsTU50bDZwNXFvR0FVajlpODFvWlZrSGlpYmhDRTg0a0RkWTRLWXFFdzg1YmxZc3RFSQ?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPZTg4c2VtT2d1SV9meTFhZFpzN2ItRk85YXlQWnAwQUxDRm5VMmhBU0RrVXAyRWROcWk4RUpFdk4yWlhkc3dlUjFyU3hkVDVkaklFNC0zTmRPRmJZNHQxN2xvYmQtMVlDVm9Bd2VJdkZIOEI1Mnh0blZMNEJ4d0FGOXBvY25ic1UwV2NYa2ZPcw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPaUxsUFM0YmRJeEtMU3VUTG1kT0FEMVpHckhVenVyMXZ5Y25YZFlhWGc5SklnZWJJNHljMzA0NmlGTGdTU3VYTUtlenBKcFhLcXhYN0MxdGVyQkk4eDZfQU9WZ3hOelJoU01ocnQ3UEQ0R0ZNWWRiSEZIOERkaTBoMnMtY3Jnam9CaTlKMk41OGpPMVdl?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQVnpmQm5iU3RTNWg3S19pMUNyeXIxdnFXMXItXzJRNUxnQmpfUDlCZTlJc0dGN3hBRXNVYmpTaG8wVlluQmZwOWVBQ0NEdWc5dG1ZUkhka0gya0hQem5rMUI3NlZMS3V3bVZMdVFCSGRycFRfWmJxMU9ja0JtNHlEb3dNRUJ0cDF5NDVXQWN3S3FmRC1GanRVM2toSnY2YXc?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxOUnB5cE1abmFuN1Q3NkVwR2s0SG5IOXlISEMwVnJEV3hYdlVXaEd4Qi1zZHhKNnJhMWFNdzNydE54YWhEZlkyV29GY3laZ1VzRXNFRTUtbmV4aTBlWnlQS0hHMWJPeWFtaEtSOGhxeXNpX25ocXhLV2NTNmlnV1dvVDUtQVJpOTdqVnZjTkpEbw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOS0JnUml0VTFqcjdudFhjaW55d3M3cnpzMjFDby1iODYyUFJiZzN5TkExMFhHVEFjb0JjRDFuSVJEaE03MWUtdkJrcXN6LWRtS01WYmtFWHI5U0Y5dFhqbUdXYS1KVkJhdE5CY2tQN0thdC01UVRUeWJLVlNUY2VKa0NMSXlka0p5MFBzZ1lxa3hydU5tVVdF?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQLU5CWG81Yk1fTTVVVkJuQ0o2dDNLd25EQlBld1VjN09SRW5mcG1ORHBjS1BRTzFnbDBWWWdCT1kxV3VoNXlTVWMyUmpOd0NvY09ENjhSSl83NTJ6bmd4al82R196clc0TVNFUFFfNE1fOVdGOWgwS0NPOVNXSFo3UlB1c2FMalBZVm9QVjdsdk1rTzIwQ3Y5MzRTUQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQSE1oLXBDN2dSRUZabVZhbzJvTDZpSVV3NmNVQ2VlYjJJQVVRSTBfQmJHT2FhWGt6LUl4NjFBMElxaVFGajh2eWlIRm1abUp2cFVoekg1VGdZN0pmbGV2ckZjWXB2ZzcwRWV2RkZ6S1pqVTBFNjRuamREVk5RMkoxZUw5ZjZyQXg1SDNHdzRIWDhweXJYTGpacC1R?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxONkdVeC1kd29pUUlKbjZfd3lYckhoSFNnbktmU1VIbVFBR08yV3pYcWo3TDkzbE43SnBJQ2RlTE84OUhnTnRnYWNsTVo4N2hBMlVKdVotVWdDVV9IdGhxbWJKLUd3Yk1fZDBKTzc0Uk1SUzc1RUdBLXpqVkdfWkV4ay1FOXpwTTNvMGZGUmxiUEJUdlVnZW1pZ2RXWW1GNC1JaVczaWczU01NRWJ6UTV2Rm9VNUZMZw?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPRnlVQVVLX05hNGdyek9rTjNybEw5b2lJcEFnN3BlMElCNEpDZmpRcnJfSDNWbHRxS2NXS3NyQ1FkbDZLZzAzdjl0RklFMk55aTZ4REF2SDlnVWpGZmk4T2NHTGNoSVVUZWM3WTVWMkl0UEFDSFJiRllqX3RRLXBXZkpIY21HTzhWZ0ZIemdvVnoxT0VqZC1UamZPTENnWDloNmZ6VDBZVWN0QQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPMlEtcTktT2NrV1BGT2V2UVhMVFE5OE9sQVFPMmhfdUh5dlF3SzI5QXdmTF9JODNXZFFIY2IyQy1uemZYZ2NIdENSOWktblBtY3RvMHlRaFR5aDRsQzl3b0JFM1ByRHpDOGhxODBwc3E5ekVpamtvTTlNVVhfNnVyOEVROGpGcno2NjZINmVwLWU3SENkN2hR?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
