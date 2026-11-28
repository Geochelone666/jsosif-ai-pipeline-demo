# VRTX Intelligence Report

- ticker: **VRTX**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/VRTX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/VRTX/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:33:55.799337+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 3, 'ai': 16, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/VRTX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 15 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 12.0%; oldest publication 2026-11-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 534.5700 |
| Return 1D (%) | -5.2382 |
| Return 1W (%) | 3.7960 |
| Return 1M (%) | 2.5987 |
| Return YTD (%) | 17.9129 |
| Return 1Y (%) | 23.6944 |
| Annualized volatility (%) | 30.7776 |
| Beta vs SPY | 0.4531 |
| Max drawdown (%) | -15.2113 |
| Sharpe (rf=0) | 0.8377 |
| Downside deviation (rf=0, %) | 19.0045 |
| Sortino (rf=0) | 1.3566 |
| Historical VaR 95% (1D, %) | 2.9212 |
| Historical ES 95% (1D, %) | 3.6465 |
| Correlation vs SPY | 0.2211 |
| Tracking error vs SPY (%) | 31.1197 |
| P/E (trailing) | 34.40 |
| P/B | 6.48 |
| EV/EBITDA | 26.61 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 26.84 |
| Gross margin (%) | 54.81 |
| Operating margin (%) | 37.79 |
| Return on equity (%) | 20.80 |
| Free cash flow yield (%) | 1.72 |
| MA50 | 525.4752 |
| Close vs MA50 (%) | 1.7308 |
| MA200 | 486.5170 |
| Close vs MA200 (%) | 9.8770 |
| RSI (14, Wilder) | 49.3443 |
| MACD (12,26) | 4.6180 |
| MACD signal (9) | 4.6007 |
| MACD histogram | 0.0173 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'VRTX': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 534.5700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -5.2382 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.7960 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.5987 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 17.9129 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 23.6944 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.7776 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 19.0045 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3566 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9212 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.6465 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2211 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.1197 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4531 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.2113 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8377 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 26.8397 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.8090 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 37.7920 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 20.8020 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.7249 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 34.3996 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 49.3443 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0173 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.7308 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.8770 -> Clearly above the moving-average trend level.

## TAILWINDS

### Vertex Pharmaceuticals Inc Stock (VRTX) Moved Up by 4.43% on Nov 24: Facts Behind the Movement
- Summary: Vertex Pharmaceuticals Inc Stock (VRTX) Moved Up by 4.43% on Nov 24: Facts Behind the Movement
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPMjdZYjNsbWhQU2JCdlBFdG9Mb3VmcFplcDUyUTIxNUN6UVV0YnN5VTd5M3RsZGYyWERRMl9iY3N2T3RQZkFXNHhCbE1kTHE1cUZ0S0h6d0N3S1NUdUFFOHZ4QjBPb3g3VXFXUzVOUTBLa0JVZ2VfWkJuX2VGVndHUWZPMjh3OXAzTmUw?oc=5>

## HEADWINDS

### Vertex Pharmaceuticals Inc Stock (VRTX) Moved Down by 7.74% on Nov 27: What Investors Need To Know
- Summary: Vertex Pharmaceuticals Inc Stock (VRTX) Moved Down by 7.74% on Nov 27: What Investors Need To Know
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPeFY0Sk9DQm94bXVMVFpCWTc5clBRdGRoQjRHUGFMQU42d3dXc1BMblBYdFhfQW84OFBlbmxRa2otcEdvQnE1a2xkX2pma0J3Wjg0YmxITkRMQ1B0UFFZMU1DVnhZazZIMG83dVk5OUpUblotd3h5WHhDUV8zcjRVbHdOQm9JMUROV3RF?oc=5>

### Vertex Pharmaceuticals (VRTX) Shares Drop After FDA Review Delay for Kidney Drug
- Summary: Vertex Pharmaceuticals (VRTX) Shares Drop After FDA Review Delay for Kidney Drug
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxQM3NnMXF2ZXRmNlYycVpiZFE4YTJ4MzA4dFEtMERVYkdwYW9leUxZUFpRVC1fWEFsNWp4LThNTWtpbmVOZFEweVliSzFsVmhzMHNZMjh1aE9hNlk0ZnlqUFBzdHR6ZTRkZW5VeDA3LXVscmNDU25HTDVnRkUzWThkc0NyRW5rZ1VteWY1MHV4RWpqMklya3BCM1R4ZlJxbnlzdjdUMllRZ0tNdFBPLXhRcWh5NVAyZDRC?oc=5>

### Vertex Announces Extension of PDUFA Target Action Date by up to...
- Summary: Vertex extends PDUFA target action date, delaying approval.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNYzVITm1kd3RhNDc3TmtpMFhUWkdfOTVndkdhRS1Mb041NDlRR280dUp0a2s0Q3o4cGN5dWp1ZnFpQWJCbm5GMGdOejNhRWdMa2RsLTd5YWRLWG83VE9xYzBvaDFhN1FMbk5ibVdaQndVa1hiZWFsR3NWZ3VNSjY0LURZQ2JVNzVLWDFQYUtyeWpBdDZ0ZFNQVy1SZEZ4bldWYkp5bFpR?oc=5>

### Vertex Stock Drops After Hours on FDA PDUFA Delay - Vertex Pharmaceuticals (NASDAQ:VRTX)
- Summary: FDA PDUFA delay causes after-hours stock drop.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxQd19CWE90RHNQVkxkNUdRZFpaZlg5NWpucHhfS0hlSmxkY1RvYVZ0TVd0MGNXWmw2X0tZVWczdjd4Q3BJcTdaZ1FJc0FMT0k3WnRhUjBBV01PbmliQ3hTM3pvek9KSThOczY3TFpwQ1FSVGRKTFRrZHFIeWRjSERFX0dGMXRxbWxfOHN6U2xSbVk5OXVkM0xxZ3o0Nm5rY2lUUEk0bExsMnhwSXFPQ3NWSEpDYUxCVVdhVXc?oc=5>

### Vertex (VERX) Stock Looks Reasonable On A 34% Three Year Slide
- Summary: Vertex stock has declined 34% over three years, raising concerns about valuation and growth prospects.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOdktVOUE5NGpyQW1nV0xLUjkyZUZYQnpxZU5ubmZpUEJHLTk1YVJ1aUwwUXExNkhEaDZQWXV5MUl4bVczbmM2Q2V5MmRCLXpvbk9nXzEwMzhDYm95TkQ2Z3NUcndzbGZLVmtkeEpSV0N1dzJkRGFqWmlGRGZzQVJYcWdlbkFHNTNiRHh4Zk5PRXdQWExUX05mY0dPZzJKazdy?oc=5>

### Vertex Pharmaceuticals Plunges On FDA Delay. It Could Have Been Worse.
- Summary: FDA delay pushes Vertex stock down, signaling regulatory setback.
- Date: 2026-11-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNbzd3TU9HQ2I0NVJ0WFVyRHp1b3V2SE91SGp3QlNFWFUxWS1EWXY2UFJJUXR3R2lkTUxaejVkV09zS1RETDdyNHZvdTk5WDhfSXlhOEpCMjNaNXd3STV4Z0dQcXVESTJhck1rS0dzeG5IemxCdmNvbUhkMzR1Q1RzZ1BmNXlkWi1ibjAw?oc=5>

### Pharma Giant Slips After FDA Delays Drug Review
- Summary: FDA delay causes Vertex shares to fall, reflecting investor concern.
- Date: 2026-11-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOcFZtSXpRQXlNMXoweDRVN0pBUkhQQzlhaDJnOG1ZalRjeHpXZ3JiaTV6QVNwYThDN055aTJsTm1ZektxaGZYVV9Yb2UxdTM1X0ozWWZGQnlEU3VtTC1Xd29fMHBOR1oybjR4ODdTMWpIMnExdGxfQnhWbVpLQldzd2ZvaHI0cU1vaFppUHJ4cjAwbTJ2RTlBakxhSjl1OHd3dTBRRW5aTVNSUQ?oc=5>

### Vertex Stock Dips After FDA Delays PDUFA to 2027
- Summary: Vertex shares drop as FDA pushes drug review to 2027.
- Date: 2026-11-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxPd3F4bWlPOC01ZkpoT2RaamFxM2pxYmlpNlFUX0JIYmJMcWJkT1dwVUxYMG9XS1pGUEM0Tnk4Q29rZGoxc3hZMjRTcnBld1FJbDEyVG5jdEhBOXJwTm5wU3dRdDlhQ2o1VWpZSm9ITEtERmFZeE1ORHptZm4zNlc3ZWRrVzJ1dHp4c1dHdDVQWTQ3eVVwVGRnSV9GOFhNVkxIZlFqcmUzeXVKYUN6N0E?oc=5>

### Vertex falls on “disappointing” FDA delay on kidney drug review; Vera rises
- Summary: FDA delay on kidney drug leads Vertex shares to decline.
- Date: 2026-11-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxPM3dicmZ0cVd3UzR0a0ZJTnRoX1pEUGFCQ3RmX0JpcWtuZ2lSbGdJRjlFQ1JsTUJ6aHE0V1JJR0NNSW45LV9OZjV0STJ0RmNFWGNrR0o3X0NxS2o2SDhzdW83RHZQUzBUY1MtU2VDVVVSUDlTbG03RTN5S2lCdHE2M0lzREZVdw?oc=5>

### Vertex Pharmaceuticals (VRTX) Valuation Review: Is the Stock Fairly Priced After Recent Declines?
- Summary: Analysts question if VRTX stock is overvalued after recent price drops.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxPdGN2NVZ1c0lYTm1pWjJuV2h1LUpHYnZudkxlaW1GUHNtaVl4VUNDYjJoczlnN2ZBeVFrZzc5SlpaRkxkc21CaEpCZkJsOUNsNGdWeFZuVjBQc2xHYkpnTGZDTlhQMW1CSUJZRk9uUW5jUFRUYlFFdUkzeWR0VFhnT1VPeW8wTWpfOFFxRjU2Vkd1NXJBMDNMQ0FzeVhsMTJxcUlXNzc4QVBPQ0VNSUFCdldCYXZaTzZuTXRoQUxLSUFCU1B5ODBGQ003WUk?oc=5>

### Vertex (VRTX) Stock Falls 7.3% Premarket Without Company News
- Summary: VRTX shares drop 7.3% premarket despite no new company announcements.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPNUIwZDlKQ2JRZWZqZ0dWd3V2OGlRMmo4NGI4UW5uenNTZC1hMnNkOC1OMXVsTmNRYTZZR21ISW9oU1RBMC1ZdEp6Vk0ySTNLcEFoWWRXb1BNM01IQnNsWU1zRkpGbmsyMTd4ZzYzbDQ2TWZWbDlmZGo2U2x2OERKZEpEdmlydlBjbHRPZW8zX2tWV1FFdWtmWUNyb1g?oc=5>

## CATALYSTS

### Vertex Pharmaceuticals Incorporated (VRTX) CF Dominance and Pipeline Strengthen Investment Outlook
- Summary: Positive outlook on CF pipeline strengthens investment view.
- Date: 2026-11-26 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQZGFMeFZzY0t2YUVwN3FIdTMwQ1NEbGFzLVR3aDJqX0h0ZUYxUVFTQUZ4R1pIdEZwTlhXTHlmdnQwNzFGSWFvNVJrQlpHWE43VUFhMGRmQndDT1U0QUhOWXpJVThNOS1zbTZ1cDlmOWp6VDRUQklxcm12QXduel9mX3JBVndMOS01dnBhN2Y0aTRieVQ2empaSUZLcUJoSWdlWUFSMUY3bw?oc=5>

### Vertex Pharmaceuticals Rises as Investors Position for Key FDA Decision
- Summary: Investors anticipate FDA decision, driving stock up.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPNTV3RlVEOEpYSUVEcUFXZE9NZXVTRjVmZFBGTjVRajdrLUZvVndpcUxldHVHM2hiaF9EZ1VDdURyVTdsa0wwS3hQUjFJd3FaeHJCTWttMFJJZ1J6UmV6cFFUM1FWVEJYb2Y3M2tEaE9aZDJiN1h0NTZ4Q21WT3pTa3JmRUlLQmVUSFRTSjVMZ0stOXAySHdFVWhWbFAxYzNrMmhhQVo4SQ?oc=5>

### A stock option exercise supplied the shares a Vertex Pharmaceuticals (VRTX) officer proposes to sell.
- Summary: Officer plans to sell shares after option exercise.
- Date: 2026-11-25 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQeUFjTDdEbDFjNHRuQkJrQ01tbmtDY2x0SElRRldweTNyeENXYy1uWjJXTU9PYm05V2N5Zm54dUY1UXRBUHlRMUFuQXZIQ0lKRDBFME84TmVHYWxnOXh2RkJQN0xjTmJOR1Q1OHUzdlZweUVWdHBpbU1DSWxIMUM1VVdidUM5eFZZcHUwZmV4Q1NCUmloOW9xSFU0ZFJpTjJBN3lQOEtyUTU4dw?oc=5>

## RISKS

### VRTX Down as FDA Extends Review Timeline for Povetacicept BLA
- Summary: FDA review extension delays product launch, increasing risk.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNOUNqVFZuZ1ptX3NGT1NHNXctTHlaUHdVUDkzUTJqZ2VadnlLTm5ocGNrTnJ3TXJfS3Y5RTRRSXpleHI2Tlg4dUJhVi04MWZZZXhEd1ZMSXotNnRhSG5HX0l5Y3J0NmhOV3FDamw5eDNSZDEwcFBLM3hzTG1qU0JkU1UzRkdKVWl3ZWtlNEtqdFdhVXRTbk9ZMHRRZ2xjZGhNcVpMcmdRb3VJcU9kYXVpQ2JrdUdOUEEx?oc=5>

### Vertex Faces FDA Delay for Povetacicept, Analyst Sees Likely Approval
- Summary: FDA delay on Vertex's povetacicept approval may postpone revenue, affecting short-term outlook.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxNQlBuXzlzNUZ2UFVJQTZzdXMydTA3OW8yckVMNHVzaVVkc2M4RnJzU3RXWTVWdU1qb0xfbEduUHdOQmpjUkZTXzJUVnVLWlRTaGs3akZUVXJ2VTYtaUk5RzllVWhINUlHWkhwUlg5cjN0ZHR1TmhZZ20wR19hSFRCWFFmelFieHRISDVYdkxUM0oyRE1OZ3hhNURPVG9iSnYxQThkQzREbEJoUWpVNlVLQ1NPYWV3bjlRcGc2REZMWEFFX3VkV05sT3RheUpScUtHZGo4bVEtOVdOLTlh?oc=5>

### Vertex Pharmaceuticals faces FDA review delay f...
- Summary: Partial FDA review delay for Vertex's povetacicept could delay product launch.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPb1JZZkNmcGZ3NjR1bmNrT3J1UFU1RmhKb3lYSm5mNFV0Q2RQQTU2VGFpVEVpTnFBV2VtZ29ZMnZTT1FReHUyQV81VnBsb0U2WGxHY2tUVUR3MWs0ZGtrS3FwVDBKWllIcGNMTk11RlFPNzRfcXltRDNXVDBqVjlLYzN1NnZGcHZOdDZLeW8tNWgtZk9F?oc=5>

### FDA delays decision on Vertex's povetacicept, e...
- Summary: FDA decision delay on Vertex's povetacicept may impact near-term earnings.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOTXQ2RDdYbzRZZm1NZTNxc0RyTS1KT04wSGEzOXhXOHNJamtEc1hiZkdlZ0U1NmJqazZRVm9oZzdPbmtoTzA1S3duRllCYkxCU1ROWDloNmRsZVRFMEU2WjhIZUFoUDFXYk9WLXRtNWxWSGpXY0d4dnFLQ3AxQ3hJeGdWSWVLazhLRVo0R2ZnVkF3b1Fwb1E?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **VRTX** | **34.40** | **6.48** | **26.61** | **11.80** | **135,533,641,728.00 USD** | **23.69** |
| REGN | 21.93 | 2.97 | 16.46 | 36.30 | 102,634,758,144.00 USD | 27.07 |
| BIIB | 114.37 | 2.06 | 13.79 | 10.60 | 39,054,106,624.00 USD | 45.21 |
| AMGN | 27.48 | 17.87 | 16.86 | 8.50 | 256,435,306,496.00 USD | 41.21 |

Peers fetched as_of: 2026-11-27; VRTX reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-02-11 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 640,799,000.00 USD; period 2018-01-01/2018-03-31; fiscal year/reporting period 2018/Q1
- Net income (latest available single quarter): 653,600,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/875320/000087532026000291/vrtx-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPMjdZYjNsbWhQU2JCdlBFdG9Mb3VmcFplcDUyUTIxNUN6UVV0YnN5VTd5M3RsZGYyWERRMl9iY3N2T3RQZkFXNHhCbE1kTHE1cUZ0S0h6d0N3S1NUdUFFOHZ4QjBPb3g3VXFXUzVOUTBLa0JVZ2VfWkJuX2VGVndHUWZPMjh3OXAzTmUw?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPeFY0Sk9DQm94bXVMVFpCWTc5clBRdGRoQjRHUGFMQU42d3dXc1BMblBYdFhfQW84OFBlbmxRa2otcEdvQnE1a2xkX2pma0J3Wjg0YmxITkRMQ1B0UFFZMU1DVnhZazZIMG83dVk5OUpUblotd3h5WHhDUV8zcjRVbHdOQm9JMUROV3RF?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxQM3NnMXF2ZXRmNlYycVpiZFE4YTJ4MzA4dFEtMERVYkdwYW9leUxZUFpRVC1fWEFsNWp4LThNTWtpbmVOZFEweVliSzFsVmhzMHNZMjh1aE9hNlk0ZnlqUFBzdHR6ZTRkZW5VeDA3LXVscmNDU25HTDVnRkUzWThkc0NyRW5rZ1VteWY1MHV4RWpqMklya3BCM1R4ZlJxbnlzdjdUMllRZ0tNdFBPLXhRcWh5NVAyZDRC?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNYzVITm1kd3RhNDc3TmtpMFhUWkdfOTVndkdhRS1Mb041NDlRR280dUp0a2s0Q3o4cGN5dWp1ZnFpQWJCbm5GMGdOejNhRWdMa2RsLTd5YWRLWG83VE9xYzBvaDFhN1FMbk5ibVdaQndVa1hiZWFsR3NWZ3VNSjY0LURZQ2JVNzVLWDFQYUtyeWpBdDZ0ZFNQVy1SZEZ4bldWYkp5bFpR?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxQd19CWE90RHNQVkxkNUdRZFpaZlg5NWpucHhfS0hlSmxkY1RvYVZ0TVd0MGNXWmw2X0tZVWczdjd4Q3BJcTdaZ1FJc0FMT0k3WnRhUjBBV01PbmliQ3hTM3pvek9KSThOczY3TFpwQ1FSVGRKTFRrZHFIeWRjSERFX0dGMXRxbWxfOHN6U2xSbVk5OXVkM0xxZ3o0Nm5rY2lUUEk0bExsMnhwSXFPQ3NWSEpDYUxCVVdhVXc?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOdktVOUE5NGpyQW1nV0xLUjkyZUZYQnpxZU5ubmZpUEJHLTk1YVJ1aUwwUXExNkhEaDZQWXV5MUl4bVczbmM2Q2V5MmRCLXpvbk9nXzEwMzhDYm95TkQ2Z3NUcndzbGZLVmtkeEpSV0N1dzJkRGFqWmlGRGZzQVJYcWdlbkFHNTNiRHh4Zk5PRXdQWExUX05mY0dPZzJKazdy?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNbzd3TU9HQ2I0NVJ0WFVyRHp1b3V2SE91SGp3QlNFWFUxWS1EWXY2UFJJUXR3R2lkTUxaejVkV09zS1RETDdyNHZvdTk5WDhfSXlhOEpCMjNaNXd3STV4Z0dQcXVESTJhck1rS0dzeG5IemxCdmNvbUhkMzR1Q1RzZ1BmNXlkWi1ibjAw?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOcFZtSXpRQXlNMXoweDRVN0pBUkhQQzlhaDJnOG1ZalRjeHpXZ3JiaTV6QVNwYThDN055aTJsTm1ZektxaGZYVV9Yb2UxdTM1X0ozWWZGQnlEU3VtTC1Xd29fMHBOR1oybjR4ODdTMWpIMnExdGxfQnhWbVpLQldzd2ZvaHI0cU1vaFppUHJ4cjAwbTJ2RTlBakxhSjl1OHd3dTBRRW5aTVNSUQ?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPd3F4bWlPOC01ZkpoT2RaamFxM2pxYmlpNlFUX0JIYmJMcWJkT1dwVUxYMG9XS1pGUEM0Tnk4Q29rZGoxc3hZMjRTcnBld1FJbDEyVG5jdEhBOXJwTm5wU3dRdDlhQ2o1VWpZSm9ITEtERmFZeE1ORHptZm4zNlc3ZWRrVzJ1dHp4c1dHdDVQWTQ3eVVwVGRnSV9GOFhNVkxIZlFqcmUzeXVKYUN6N0E?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxPM3dicmZ0cVd3UzR0a0ZJTnRoX1pEUGFCQ3RmX0JpcWtuZ2lSbGdJRjlFQ1JsTUJ6aHE0V1JJR0NNSW45LV9OZjV0STJ0RmNFWGNrR0o3X0NxS2o2SDhzdW83RHZQUzBUY1MtU2VDVVVSUDlTbG03RTN5S2lCdHE2M0lzREZVdw?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxPdGN2NVZ1c0lYTm1pWjJuV2h1LUpHYnZudkxlaW1GUHNtaVl4VUNDYjJoczlnN2ZBeVFrZzc5SlpaRkxkc21CaEpCZkJsOUNsNGdWeFZuVjBQc2xHYkpnTGZDTlhQMW1CSUJZRk9uUW5jUFRUYlFFdUkzeWR0VFhnT1VPeW8wTWpfOFFxRjU2Vkd1NXJBMDNMQ0FzeVhsMTJxcUlXNzc4QVBPQ0VNSUFCdldCYXZaTzZuTXRoQUxLSUFCU1B5ODBGQ003WUk?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPNUIwZDlKQ2JRZWZqZ0dWd3V2OGlRMmo4NGI4UW5uenNTZC1hMnNkOC1OMXVsTmNRYTZZR21ISW9oU1RBMC1ZdEp6Vk0ySTNLcEFoWWRXb1BNM01IQnNsWU1zRkpGbmsyMTd4ZzYzbDQ2TWZWbDlmZGo2U2x2OERKZEpEdmlydlBjbHRPZW8zX2tWV1FFdWtmWUNyb1g?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQZGFMeFZzY0t2YUVwN3FIdTMwQ1NEbGFzLVR3aDJqX0h0ZUYxUVFTQUZ4R1pIdEZwTlhXTHlmdnQwNzFGSWFvNVJrQlpHWE43VUFhMGRmQndDT1U0QUhOWXpJVThNOS1zbTZ1cDlmOWp6VDRUQklxcm12QXduel9mX3JBVndMOS01dnBhN2Y0aTRieVQ2empaSUZLcUJoSWdlWUFSMUY3bw?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPNTV3RlVEOEpYSUVEcUFXZE9NZXVTRjVmZFBGTjVRajdrLUZvVndpcUxldHVHM2hiaF9EZ1VDdURyVTdsa0wwS3hQUjFJd3FaeHJCTWttMFJJZ1J6UmV6cFFUM1FWVEJYb2Y3M2tEaE9aZDJiN1h0NTZ4Q21WT3pTa3JmRUlLQmVUSFRTSjVMZ0stOXAySHdFVWhWbFAxYzNrMmhhQVo4SQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQeUFjTDdEbDFjNHRuQkJrQ01tbmtDY2x0SElRRldweTNyeENXYy1uWjJXTU9PYm05V2N5Zm54dUY1UXRBUHlRMUFuQXZIQ0lKRDBFME84TmVHYWxnOXh2RkJQN0xjTmJOR1Q1OHUzdlZweUVWdHBpbU1DSWxIMUM1VVdidUM5eFZZcHUwZmV4Q1NCUmloOW9xSFU0ZFJpTjJBN3lQOEtyUTU4dw?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNOUNqVFZuZ1ptX3NGT1NHNXctTHlaUHdVUDkzUTJqZ2VadnlLTm5ocGNrTnJ3TXJfS3Y5RTRRSXpleHI2Tlg4dUJhVi04MWZZZXhEd1ZMSXotNnRhSG5HX0l5Y3J0NmhOV3FDamw5eDNSZDEwcFBLM3hzTG1qU0JkU1UzRkdKVWl3ZWtlNEtqdFdhVXRTbk9ZMHRRZ2xjZGhNcVpMcmdRb3VJcU9kYXVpQ2JrdUdOUEEx?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxNQlBuXzlzNUZ2UFVJQTZzdXMydTA3OW8yckVMNHVzaVVkc2M4RnJzU3RXWTVWdU1qb0xfbEduUHdOQmpjUkZTXzJUVnVLWlRTaGs3akZUVXJ2VTYtaUk5RzllVWhINUlHWkhwUlg5cjN0ZHR1TmhZZ20wR19hSFRCWFFmelFieHRISDVYdkxUM0oyRE1OZ3hhNURPVG9iSnYxQThkQzREbEJoUWpVNlVLQ1NPYWV3bjlRcGc2REZMWEFFX3VkV05sT3RheUpScUtHZGo4bVEtOVdOLTlh?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPb1JZZkNmcGZ3NjR1bmNrT3J1UFU1RmhKb3lYSm5mNFV0Q2RQQTU2VGFpVEVpTnFBV2VtZ29ZMnZTT1FReHUyQV81VnBsb0U2WGxHY2tUVUR3MWs0ZGtrS3FwVDBKWllIcGNMTk11RlFPNzRfcXltRDNXVDBqVjlLYzN1NnZGcHZOdDZLeW8tNWgtZk9F?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOTXQ2RDdYbzRZZm1NZTNxc0RyTS1KT04wSGEzOXhXOHNJamtEc1hiZkdlZ0U1NmJqazZRVm9oZzdPbmtoTzA1S3duRllCYkxCU1ROWDloNmRsZVRFMEU2WjhIZUFoUDFXYk9WLXRtNWxWSGpXY0d4dnFLQ3AxQ3hJeGdWSWVLazhLRVo0R2ZnVkF3b1Fwb1E?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
