# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-11-10**
- Market data as_of: **2026-11-10**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-11-10**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-11T04:53:38.549535+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 6, 'ai': 14, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261110T055129Z-abd33250/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 23 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 8.0%; oldest publication 2026-11-07

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 515.2100 |
| Return 1D (%) | 1.3036 |
| Return 1W (%) | 6.4704 |
| Return 1M (%) | -15.2754 |
| Return YTD (%) | 140.5725 |
| Return 1Y (%) | 111.1690 |
| Annualized volatility (%) | 73.0289 |
| Beta vs SPY | 3.4144 |
| Max drawdown (%) | -37.7290 |
| Sharpe (rf=0) | 1.3922 |
| Downside deviation (rf=0, %) | 47.2030 |
| Sortino (rf=0) | 2.1540 |
| Historical VaR 95% (1D, %) | 6.3184 |
| Historical ES 95% (1D, %) | 9.4746 |
| Correlation vs SPY | 0.6392 |
| Tracking error vs SPY (%) | 65.1451 |
| P/E (trailing) | 110.09 |
| P/B | 12.35 |
| EV/EBITDA | 75.24 |
| Revenue growth (%) | 44.70 |
| Forward P/E (estimate) | 29.13 |
| Gross margin (%) | 56.00 |
| Operating margin (%) | 21.17 |
| Return on equity (%) | 11.96 |
| Free cash flow yield (%) | 0.87 |
| MA50 | 548.5636 |
| Close vs MA50 (%) | -6.0802 |
| MA200 | 418.5415 |
| Close vs MA200 (%) | 23.0965 |
| RSI (14, Wilder) | 48.5984 |
| MACD (12,26) | -23.5598 |
| MACD signal (9) | -20.1904 |
| MACD histogram | -3.3694 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 279, 'SPY': 279}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 515.2100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.3036 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 6.4704 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -15.2754 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 140.5725 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 111.1690 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 73.0289 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 47.2030 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.1540 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.3184 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 9.4746 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6392 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 65.1451 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4144 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -37.7290 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.3922 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 29.1252 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 56.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 21.1710 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.9600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.8707 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 110.0876 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 48.5984 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.3694 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -6.0802 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 23.0965 -> Clearly above the moving-average trend level.

## TAILWINDS

### AMD Stock Reverses Morning Gains, Slowly Recovers After Google AI Deal
- Summary: AMD Stock Reverses Morning Gains, Slowly Recovers After Google AI Deal
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxQTHNiaWhiVENxYXhKbXg5eWQzZGU5eFFXNGhNSDBrYWsxQUY3Qm1zbUdMREUweWRvM2RvSDFqS0dSQlhELWw4TjJIRFRqbUpXQ1U5QkxEaGZQUnZqSjktWlVtRmVycjd1b1RaZjdGUGp5eU5EODVUd1RwMTJyWGYtQXV3Rm9iVmxOcldJdndJR0JYN1Bac1hHbHk3YVRyS2pCS2FrWTRvM0NWcVpFQjRfYlZmUmhRZTQwVjM4R005Qmxad01RTE1Pc3VR?oc=5>

### Advanced Micro Devices Stocks Rise 2.66% on $2.5 Billion Anthropic Stake Commitment
- Summary: Advanced Micro Devices Stocks Rise 2.66% on $2.5 Billion Anthropic Stake Commitment
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPQWlUVlRiRzY4eVFhLXBDSWdWMjcwcVVMbURhcU85bC1MM2d3ejFIT2pMRUtPMzFOWnBtcTZjbFllQmRxR2NqbkFJc0g3Y2gwaGlLYUlidFZrX21iTEVXbE01WXJ2TEJJUGN5aHJMeGxTU0NPS3RLMnJ3Y3d3XzhwQTZrLThDQ0NSb3FPblRUUHlnUW9vajVSVU9PWkVLd1VPTWd4ZFFvYWpWMUlsOVdIT1AyTlZzTFpvb0E?oc=5>

### Advanced Micro Devices (NASDAQ:AMD) Shares Climb 1.3% - What's Next?
- Summary: Advanced Micro Devices (NASDAQ:AMD) Shares Climb 1.3% - What's Next?
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxOcGg0ZVM5TEI2clc1ZWE2WUk3NFpEMlY1SWtMZjUydi1FYUlyUTVBdkk0Y242czBOeU14REF4eHZoNXowOWpUTXp4WlpVYWxZT0NVZkk4LWhWZXcwcVhpOUlpVEpjdGZIRExBMkt1Qm9aVU5TYkhLWmk5M0d4VEphUzJjVWVWWTNQN1BEajVBZ1FRYkFGcnd4bC02TG9zNkNLLTBwVHBxWURqeGt1N2plNzJLYW5ZLXhnRkNlaQ?oc=5>

### AMD Stock Rises On Google Cloud Deal, Wall Street Upgrade
- Summary: AMD Stock Rises On Google Cloud Deal, Wall Street Upgrade
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNc0pob1FQZVItVXBmSHRhb1kzQkg0T3ZaR1FlT3hqQ3NEUEpPUDZoN19qTHRHZ1R4UHN2dUI3MEg4OVRITGNxc3V3WjRNZTJpQndZbm1SY2J1Wm1SRGZWRVRkQm5HaGZhWlBhbG15dHdYaWc5cUdYZjN5QjBjWk5kVlhDZ0N6WlJzbEdfWUU3QU1FaFhraTVUNzBORFVhOVRG?oc=5>

### AMD (NASDAQ:AMD) Stock Surges Nearly 9% on $600 Upgrade as Nvidia Falls 4%
- Summary: AMD stock jumps 9% after analyst upgrade, while Nvidia falls 4%.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiekFVX3lxTE1hVmlvSWJGWWloQVNqWkN6b1JVM0tFd0NrNF9qYWptMXVHWmF2S09mZVdfb2Zjb21mTHpaZ0Q0blZIZTR2N3AteEhkSVJIUlkxeGVpWXhHeTBqZnpjODB0V2hmbXowUmgtby1la2RwTlFRTWFYQkJpeFBB?oc=5>

### AMD Is Up 110% in 2026, but Down Sharply From Its High. Time to Sell, or Load Up?
- Summary: AMD shares up 110% in 2026 but have fallen from peak, prompting sell or buy debate.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPcm5ZSTd5TThzWkJTVWNoQXJFcWFBRG9LX1lBRmRLVUx0Y25kYUFuLVB6ZmpNa01YWGJqY2xMakt4RkcwSDdNbmFHV2NCakhTcGdmUTNFdUJMeXo0VkVOZmE3cjVSTkRUNzhvbEFLZk5MWEVRb2R3VjZfQl92Tm9wRTQ0N2gxYTBVWTBYSWk1VVJ5SGp2MkFaR0FfR2F2MGFjMmlycw?oc=5>

### Why is Advanced Micro Devices stock rallying today?
- Summary: Questioning the reasons behind AMD's current stock rally.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNSWpJYjh3LTd2N0JXS01nQUNBTW5mSE1DMkFXb1hGdDRnbW5IUTFaUmlGa3JBcnJFTWVXanNUUEJKbTdTbzRXSkxYcDVJVVd6RnZVeGFVaDN0UFcwc2NhLVBldUxja3lPZ2RDa0xNUWZDRHIzbG4xSVFtV05vWXlSU1FKa21VVkY4R1BQUWpiaHlpV0ZMbzlzYk1SSFhwQVhQMkhJSHc5X1BhS2VFR1J2NVZn?oc=5>

### AMD, Micron, and Applied Materials Stocks Are Soaring Today. What’s Behind the Rally?
- Summary: All three chip stocks rallying today; article explores underlying causes.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQblJEb0dsY3hZeGlKTjdpNVpYUzl5dGRKVDVTNUdHTXROX21TZWw0LUZueXlJMzhfZllqZEk5NWhYeFphZkJzVzI4VFJlR3B2Z0xNWWxXa2x5cjZ5MnlRZE4ya0lPUnZ0d0xaOXFYZEgydThuOV9FSmp6Xy1yeS1iWXdNME5WNnhrTm1ZSFhpT2RxS1l5STBiQlJ4c3ZoVXNYZkE4TTljYW53WWF4TjZB?oc=5>

### Stock Market Today, Nov. 9: AMD Jumps on Oppenheimer Upgrade and Google Cloud Chip Selection
- Summary: AMD shares rise after Oppenheimer upgrade and Google Cloud chip selection announcement.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNWmdqcWFZM0NCdGU1RC1LZlRfejRBeVNkekItNHNtck1vZ1RnMFpMdWl4OGZMNlpGRVlHSEhOaEtSQ0xZNDhwNldNUEt0b0l5UXY4b2tYWmdWbFpYdFZXUFAwUzAyN3h0YjBNRmV4SWhJU0pOTl9veU1SWHdjbHpkbEw2VkkwLUlCM3lGN2I4cGJ2TnM?oc=5>

## HEADWINDS

### Advanced Micro Devices (AMD) Recently Crashed Out of the $1 Trillion Club. Should You Buy the Dip?
- Summary: AMD loses $1 trillion market cap, indicating a negative market move.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOeEpRMjVrSzZYZENMSFgxdHVucTIxajJzb0xQVXptZGVjRUh3eEMxUEU4MDVpUFJEMnBSYnU5UFhOYXI2SHFjdHQ0NW9QdDczV2MtVlczVzZCbEE0RDN5R0l3NnhkbE40bkJUR3FZSXpZMmVTQ0VPRHNFR3lWcW9mQ2FxTlJpQl9pZ01YTGV2RzlXNVdoVHFV?oc=5>

### AMD's Stock Fades as Investors Weigh Whether Nvidia's Turmoil Will Mean Lasting Wins
- Summary: Investors concerned that Nvidia's issues may hurt AMD's market position, leading to a decline in AMD shares.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPaUZDQ3VHNU1YV2Q5MU5NLXFUYTloblM5bEV0UjVGQWluMVZNVXRMamJ0N0NEby1zQnkwOFJPTkVvODlEZUVtNGdrU3F4UF9lY3BVRDdOdktaT3BKdm80eTZ5ZUtKSDQ2TG9tYlpIRWszZFNVaEZvYzBwcjN4UW55dkJHQW5LTEhnRk5SZ284RkhOY3lrc2k2N202Wmc?oc=5>

## CATALYSTS

### AMD Gains 25% Against NVDA in 2 Days: Chip Analyst Says Lisa Su Is ‘at Her Best’
- Summary: AMD Gains 25% Against NVDA in 2 Days: Chip Analyst Says Lisa Su Is ‘at Her Best’
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQM0FIQVdoN2dpcDVvT1FZNnkxeWJfbU9xVTFhSUFkLTZ6SVlsTGczdUVhcVlwcElfbk1rVlJBSmxheFY0OXo0RTFQU2pSd1lxVkFsZllMcG42MlExYTlEbENPTFp1eTVwMnUxMFA4MWRjNzZ1Y0Y3Tk53SGVsVWJRdTNtSlAza2NFOWlEMHVINA?oc=5>

### AMD stock jumps 13% after 5-star analyst resets price target
- Summary: AMD stock jumps 13% after 5-star analyst resets price target
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPYlRIejllVjJBT1VWTzZjVFRYYUtIOUJUS0kyVm02aS02YkhQWVhmM2JmcVJwaVVQbW96aUpZMEpiVnZoclhlS3lqZnF3YnA2NnRWRTQ5TEZiU1Q3eC02dVU4bXZlMXhPTWU1LUE3YWlCNUNuN01Vak5KX05hUVEyMWgyemJLdllOOGNhMTljNDlSTW4zb1Rr?oc=5>

### AMD shares are primed for a comeback, says Oppenheimer
- Summary: Analyst predicts short‑term rebound for AMD shares.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMie0FVX3lxTE1CYmI5cjRwNEFyb0VzcTdZb3Fic0Jkck9Cd1RLNURuYVdTWEpDSzktSER6TjBCNlplV3VyRkc1NmZnOThHYnBoZTRibUYwWkNkbktuUGE5d2JLM2pQNW9VdnJ5Rl92WjZ5Z0dobmdTLWdySUFSUDl1REVKdw?oc=5>

### AMD and Coherent: What the Biggest Gainers Since the Midterm Selloff Say About the AI Trade
- Summary: Analysis of AMD and Coherent’s gains post-midterm selloff, highlighting AI trade trends.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMie0FVX3lxTE5la2wydkhvVGI4X2w3OGpMXzdsenFEYjFBOHJ6NEp6QXh2U19URDVsVFpIX2I4aU9iNTNjMmlvcnFENkNfZ3ZUc1dqMUtlZGN5TzZMRndnMElTU3FFRjVKc2pMMkpkUXZtc0RTMmo1ZkJwaWlDTXM4NGNYbw?oc=5>

### AMD Stock Clocks Best Day In 6 Months — But Michael Burry Won’t Touch The Nvidia Headline Trade
- Summary: AMD shares hit six‑month high; analyst Burry remains cautious.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxOSGEzbEdlTTBTalRHYUNxS096dFFIZ0NzMkZGQUcyVWRKWjRGZS1jTFlLcHBWNEEwbmxSbzBTSF8wVXJMZHhiZVZKd3R1bnJOM2lzc3BhbDB0MEt2Si1tX3BickV3ZkQxTG1TVXJCT0Z2UDlQZEpiN0o4bmVDQllZcU5UXzVGeVBxYmRIb3hGR2tTUWl4bnJWR2lWYzhVS1NiT0tNbXdod0JVYW5CS2pTYWpGR0F5aElwN1R2bg?oc=5>

### US Stock Futures Mixed As Investors Await CPI Data — AMD, CRWV, RKLB Stocks In Focus
- Summary: Futures mixed; AMD among stocks watched ahead of CPI release.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxNajBuaUs4bEtDTEQzVVdRU1Zva3NnUk1lQzlXelFIdHdZOVRlQzFOVTU2N2x4WGRDelEtMTZfRElkV2VZMWJRQ04xM1FWUlIwbW9IS2Z2cXRqaTV2dV9vYU1VV2h2ck9STEN6RzUtLU1qcTNEZzFrUzB5U21aZms0dkhGZGlhZ2pfa1plZ083c3F3SmRiVnNzbEZoZ2dCbjd3ck1zc3FnSW00YTdqZzI2R1o2V0xFUXpxWlM4TjJwWExuRkI4MEVmMV9MRkN4eFQ1ZnYzS2ltQ0I?oc=5>

### NVIDIA Falls 4% as Board Probe of Jensen Huang Weighs on Shares; AMD and Broadcom Gain 3%
- Summary: AMD shares rise 3% amid NVIDIA’s board probe, reflecting market reaction.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxQb2s1ekxJVnk0YTFNZ3lIU3VXUk5ScGNGSzVtU2tZRWZkWUdEVVlWV3BDZGdPMy1GZG0tdjdpSUg2bXJReWtrNzkwdWNVM2ZuTEpoMDFURlRyYWRseXI5SGJtakZseVVxekdoRGlidGp3cTlkUEp3MndZSnFVcHp6YWJmaTg1NGQ3SU9YcVFpbEZoWmZrREpZYnNYR2tWMGJQT0syYUlnWGJHcUt4NDdfX24xVHFTc3Q3YjhxSFFwNUswOWFxbU44V053?oc=5>

### Stock Market Today, Nov. 10: AMD Rises on Plan to Invest $2.5 Billion in Anthropic
- Summary: AMD announces $2.5B investment in Anthropic, boosting stock.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi9wFBVV95cUxQdFVPM1N6MEcyTjdrOU1pck4yZWxid3NXOW50T3JjaEtEaEVjam0tbmloa3BVbEp6RWx5S25SSjlyRWhRUlplZTZMUGhCaHQ1X0lhYTFQZ25nM3haZGNMZUNDcDFvbTBjeGt6bUoyOWdRSjQ2YVZNQXlnR1RHSUVsTTlSUnVtM2RfZnBIWk1sVzRTRkU2OFdDdGpOS1B6Tmg0emk4TkJ3VHkzcERWWmJTUDV3Q3BvZncwalRuc3FDQ2t0NlltbENoUERrX3ZMTlh5TnBsZDlVTlZSZWkzSHlvS0ZPNmI2b3BJZ3pnQ3FDU2pMdHVyeHVR?oc=5>

### Oppenheimer Just Set a Whopping $600 Target on AMD Stock. Here's Why.
- Summary: Analyst Oppenheimer raised AMD's target price to $600, signaling strong upside potential.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxNLWlQYjJ2bUk0WTdqNkRKN29EZ2o1d3NkQTBUbmktOVdTamZGeWU5WHpLcmxCT0Z1UzdaOF8zbU8tVmNsN2FURTNYdndhUi0wNm1hM1dXd1ZBc1ZxV0tySVRfd0dKWTg3bmk1T245Z2E2Y05yaEU2U21QMGNMamM4dk44ZFA0Y2sxVjRTVDhhcEx0UlZCa25QQkdZQVY5S2ZyVUxlUXJxemxFaGlJQ3lz?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **110.09** | **12.35** | **75.24** | **44.70** | **844,989,399,040.00 USD** | **111.17** |
| NVDA | 22.58 | 17.81 | 20.11 | 105.90 | 4,078,186,790,912.00 USD | -14.95 |
| INTC | N/A | 2.69 | 16.81 | 20.90 | 308,960,952,320.00 USD | 51.18 |
| AVGO | 42.40 | 15.90 | 31.00 | 85.50 | 1,584,749,740,032.00 USD | -6.68 |

Peers fetched as_of: 2026-11-10; AMD reuses existing data (market data as_of: 2026-11-10); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-10

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,428,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiygFBVV95cUxQTHNiaWhiVENxYXhKbXg5eWQzZGU5eFFXNGhNSDBrYWsxQUY3Qm1zbUdMREUweWRvM2RvSDFqS0dSQlhELWw4TjJIRFRqbUpXQ1U5QkxEaGZQUnZqSjktWlVtRmVycjd1b1RaZjdGUGp5eU5EODVUd1RwMTJyWGYtQXV3Rm9iVmxOcldJdndJR0JYN1Bac1hHbHk3YVRyS2pCS2FrWTRvM0NWcVpFQjRfYlZmUmhRZTQwVjM4R005Qmxad01RTE1Pc3VR?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPQWlUVlRiRzY4eVFhLXBDSWdWMjcwcVVMbURhcU85bC1MM2d3ejFIT2pMRUtPMzFOWnBtcTZjbFllQmRxR2NqbkFJc0g3Y2gwaGlLYUlidFZrX21iTEVXbE01WXJ2TEJJUGN5aHJMeGxTU0NPS3RLMnJ3Y3d3XzhwQTZrLThDQ0NSb3FPblRUUHlnUW9vajVSVU9PWkVLd1VPTWd4ZFFvYWpWMUlsOVdIT1AyTlZzTFpvb0E?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxOcGg0ZVM5TEI2clc1ZWE2WUk3NFpEMlY1SWtMZjUydi1FYUlyUTVBdkk0Y242czBOeU14REF4eHZoNXowOWpUTXp4WlpVYWxZT0NVZkk4LWhWZXcwcVhpOUlpVEpjdGZIRExBMkt1Qm9aVU5TYkhLWmk5M0d4VEphUzJjVWVWWTNQN1BEajVBZ1FRYkFGcnd4bC02TG9zNkNLLTBwVHBxWURqeGt1N2plNzJLYW5ZLXhnRkNlaQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNc0pob1FQZVItVXBmSHRhb1kzQkg0T3ZaR1FlT3hqQ3NEUEpPUDZoN19qTHRHZ1R4UHN2dUI3MEg4OVRITGNxc3V3WjRNZTJpQndZbm1SY2J1Wm1SRGZWRVRkQm5HaGZhWlBhbG15dHdYaWc5cUdYZjN5QjBjWk5kVlhDZ0N6WlJzbEdfWUU3QU1FaFhraTVUNzBORFVhOVRG?oc=5
- https://news.google.com/rss/articles/CBMiekFVX3lxTE1hVmlvSWJGWWloQVNqWkN6b1JVM0tFd0NrNF9qYWptMXVHWmF2S09mZVdfb2Zjb21mTHpaZ0Q0blZIZTR2N3AteEhkSVJIUlkxeGVpWXhHeTBqZnpjODB0V2hmbXowUmgtby1la2RwTlFRTWFYQkJpeFBB?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPcm5ZSTd5TThzWkJTVWNoQXJFcWFBRG9LX1lBRmRLVUx0Y25kYUFuLVB6ZmpNa01YWGJqY2xMakt4RkcwSDdNbmFHV2NCakhTcGdmUTNFdUJMeXo0VkVOZmE3cjVSTkRUNzhvbEFLZk5MWEVRb2R3VjZfQl92Tm9wRTQ0N2gxYTBVWTBYSWk1VVJ5SGp2MkFaR0FfR2F2MGFjMmlycw?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNSWpJYjh3LTd2N0JXS01nQUNBTW5mSE1DMkFXb1hGdDRnbW5IUTFaUmlGa3JBcnJFTWVXanNUUEJKbTdTbzRXSkxYcDVJVVd6RnZVeGFVaDN0UFcwc2NhLVBldUxja3lPZ2RDa0xNUWZDRHIzbG4xSVFtV05vWXlSU1FKa21VVkY4R1BQUWpiaHlpV0ZMbzlzYk1SSFhwQVhQMkhJSHc5X1BhS2VFR1J2NVZn?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQblJEb0dsY3hZeGlKTjdpNVpYUzl5dGRKVDVTNUdHTXROX21TZWw0LUZueXlJMzhfZllqZEk5NWhYeFphZkJzVzI4VFJlR3B2Z0xNWWxXa2x5cjZ5MnlRZE4ya0lPUnZ0d0xaOXFYZEgydThuOV9FSmp6Xy1yeS1iWXdNME5WNnhrTm1ZSFhpT2RxS1l5STBiQlJ4c3ZoVXNYZkE4TTljYW53WWF4TjZB?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNWmdqcWFZM0NCdGU1RC1LZlRfejRBeVNkekItNHNtck1vZ1RnMFpMdWl4OGZMNlpGRVlHSEhOaEtSQ0xZNDhwNldNUEt0b0l5UXY4b2tYWmdWbFpYdFZXUFAwUzAyN3h0YjBNRmV4SWhJU0pOTl9veU1SWHdjbHpkbEw2VkkwLUlCM3lGN2I4cGJ2TnM?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOeEpRMjVrSzZYZENMSFgxdHVucTIxajJzb0xQVXptZGVjRUh3eEMxUEU4MDVpUFJEMnBSYnU5UFhOYXI2SHFjdHQ0NW9QdDczV2MtVlczVzZCbEE0RDN5R0l3NnhkbE40bkJUR3FZSXpZMmVTQ0VPRHNFR3lWcW9mQ2FxTlJpQl9pZ01YTGV2RzlXNVdoVHFV?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPaUZDQ3VHNU1YV2Q5MU5NLXFUYTloblM5bEV0UjVGQWluMVZNVXRMamJ0N0NEby1zQnkwOFJPTkVvODlEZUVtNGdrU3F4UF9lY3BVRDdOdktaT3BKdm80eTZ5ZUtKSDQ2TG9tYlpIRWszZFNVaEZvYzBwcjN4UW55dkJHQW5LTEhnRk5SZ284RkhOY3lrc2k2N202Wmc?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQM0FIQVdoN2dpcDVvT1FZNnkxeWJfbU9xVTFhSUFkLTZ6SVlsTGczdUVhcVlwcElfbk1rVlJBSmxheFY0OXo0RTFQU2pSd1lxVkFsZllMcG42MlExYTlEbENPTFp1eTVwMnUxMFA4MWRjNzZ1Y0Y3Tk53SGVsVWJRdTNtSlAza2NFOWlEMHVINA?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPYlRIejllVjJBT1VWTzZjVFRYYUtIOUJUS0kyVm02aS02YkhQWVhmM2JmcVJwaVVQbW96aUpZMEpiVnZoclhlS3lqZnF3YnA2NnRWRTQ5TEZiU1Q3eC02dVU4bXZlMXhPTWU1LUE3YWlCNUNuN01Vak5KX05hUVEyMWgyemJLdllOOGNhMTljNDlSTW4zb1Rr?oc=5
- https://news.google.com/rss/articles/CBMie0FVX3lxTE1CYmI5cjRwNEFyb0VzcTdZb3Fic0Jkck9Cd1RLNURuYVdTWEpDSzktSER6TjBCNlplV3VyRkc1NmZnOThHYnBoZTRibUYwWkNkbktuUGE5d2JLM2pQNW9VdnJ5Rl92WjZ5Z0dobmdTLWdySUFSUDl1REVKdw?oc=5
- https://news.google.com/rss/articles/CBMie0FVX3lxTE5la2wydkhvVGI4X2w3OGpMXzdsenFEYjFBOHJ6NEp6QXh2U19URDVsVFpIX2I4aU9iNTNjMmlvcnFENkNfZ3ZUc1dqMUtlZGN5TzZMRndnMElTU3FFRjVKc2pMMkpkUXZtc0RTMmo1ZkJwaWlDTXM4NGNYbw?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxOSGEzbEdlTTBTalRHYUNxS096dFFIZ0NzMkZGQUcyVWRKWjRGZS1jTFlLcHBWNEEwbmxSbzBTSF8wVXJMZHhiZVZKd3R1bnJOM2lzc3BhbDB0MEt2Si1tX3BickV3ZkQxTG1TVXJCT0Z2UDlQZEpiN0o4bmVDQllZcU5UXzVGeVBxYmRIb3hGR2tTUWl4bnJWR2lWYzhVS1NiT0tNbXdod0JVYW5CS2pTYWpGR0F5aElwN1R2bg?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxNajBuaUs4bEtDTEQzVVdRU1Zva3NnUk1lQzlXelFIdHdZOVRlQzFOVTU2N2x4WGRDelEtMTZfRElkV2VZMWJRQ04xM1FWUlIwbW9IS2Z2cXRqaTV2dV9vYU1VV2h2ck9STEN6RzUtLU1qcTNEZzFrUzB5U21aZms0dkhGZGlhZ2pfa1plZ083c3F3SmRiVnNzbEZoZ2dCbjd3ck1zc3FnSW00YTdqZzI2R1o2V0xFUXpxWlM4TjJwWExuRkI4MEVmMV9MRkN4eFQ1ZnYzS2ltQ0I?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxQb2s1ekxJVnk0YTFNZ3lIU3VXUk5ScGNGSzVtU2tZRWZkWUdEVVlWV3BDZGdPMy1GZG0tdjdpSUg2bXJReWtrNzkwdWNVM2ZuTEpoMDFURlRyYWRseXI5SGJtakZseVVxekdoRGlidGp3cTlkUEp3MndZSnFVcHp6YWJmaTg1NGQ3SU9YcVFpbEZoWmZrREpZYnNYR2tWMGJQT0syYUlnWGJHcUt4NDdfX24xVHFTc3Q3YjhxSFFwNUswOWFxbU44V053?oc=5
- https://news.google.com/rss/articles/CBMi9wFBVV95cUxQdFVPM1N6MEcyTjdrOU1pck4yZWxid3NXOW50T3JjaEtEaEVjam0tbmloa3BVbEp6RWx5S25SSjlyRWhRUlplZTZMUGhCaHQ1X0lhYTFQZ25nM3haZGNMZUNDcDFvbTBjeGt6bUoyOWdRSjQ2YVZNQXlnR1RHSUVsTTlSUnVtM2RfZnBIWk1sVzRTRkU2OFdDdGpOS1B6Tmg0emk4TkJ3VHkzcERWWmJTUDV3Q3BvZncwalRuc3FDQ2t0NlltbENoUERrX3ZMTlh5TnBsZDlVTlZSZWkzSHlvS0ZPNmI2b3BJZ3pnQ3FDU2pMdHVyeHVR?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxNLWlQYjJ2bUk0WTdqNkRKN29EZ2o1d3NkQTBUbmktOVdTamZGeWU5WHpLcmxCT0Z1UzdaOF8zbU8tVmNsN2FURTNYdndhUi0wNm1hM1dXd1ZBc1ZxV0tySVRfd0dKWTg3bmk1T245Z2E2Y05yaEU2U21QMGNMamM4dk44ZFA0Y2sxVjRTVDhhcEx0UlZCa25QQkdZQVY5S2ZyVUxlUXJxemxFaGlJQ3lz?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
