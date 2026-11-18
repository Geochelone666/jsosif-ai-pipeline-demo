# JPM Intelligence Report

- ticker: **JPM**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/JPM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/JPM/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T05:51:22.710808+00:00**
- AI status: **Partial: 1 headline remains unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 1, 'ai': 15, 'unknown': 1, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261116T043911Z-b81cfeb4/JPM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 13 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 28.0%; oldest publication 2026-11-12

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 329.9600 |
| Return 1D (%) | -2.4393 |
| Return 1W (%) | -3.5402 |
| Return 1M (%) | -2.8730 |
| Return YTD (%) | 4.3743 |
| Return 1Y (%) | 11.9669 |
| Annualized volatility (%) | 22.8626 |
| Beta vs SPY | 0.7986 |
| Max drawdown (%) | -15.4717 |
| Sharpe (rf=0) | 0.6106 |
| Downside deviation (rf=0, %) | 16.4093 |
| Sortino (rf=0) | 0.8508 |
| Historical VaR 95% (1D, %) | 2.4357 |
| Historical ES 95% (1D, %) | 3.3208 |
| Correlation vs SPY | 0.4814 |
| Tracking error vs SPY (%) | 20.2308 |
| P/E (trailing) | 14.19 |
| P/B | 2.49 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 10.20 |
| Forward P/E (estimate) | 12.90 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 44.79 |
| Return on equity (%) | 18.01 |
| Free cash flow yield (%) | N/A |
| MA50 | 338.8950 |
| Close vs MA50 (%) | -2.6365 |
| MA200 | 322.7504 |
| Close vs MA200 (%) | 2.2338 |
| RSI (14, Wilder) | 42.1045 |
| MACD (12,26) | 0.2071 |
| MACD signal (9) | 0.6630 |
| MACD histogram | -0.4559 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'JPM': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 329.9600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.4393 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.5402 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -2.8730 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 4.3743 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 11.9669 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.8626 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.4093 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.8508 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4357 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.3208 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4814 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.2308 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.7986 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.4717 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.6106 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 12.9026 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 44.7880 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 18.0130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 14.1857 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 42.1045 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.4559 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -2.6365 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 2.2338 -> Slightly above the moving-average trend level.

## TAILWINDS

### Jamie Dimon Just Said 5 Words Blocking Outside AI Agents From JPMorgan Accounts: "You Don't Want Rogue Agents." Here's Why That Security Stance Matters for JPM and Its Tech Rivals.
- Summary: JPM emphasizes security against rogue AI agents, potentially strengthening trust and compliance.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNQWQ4UlBOQ3VlbjFqcEpma1BDMjRRczVfalJRVWZaUjdyY2l0Rmw2NWtvb2gzVXZ2R2JTR09LSlFIcmd5aVh1NklOcU1BUGhVVTY3ZEFwdEdlcWZuLXZTbzNsOVoybXdOcDJTR3A3T2FvbDNaMmZZbmVTQTVGZGhCY3RGQVllZmN1ZG9DbXNfd090MzkwRHdR?oc=5>

### JPMorgan Chase (JPM) Sees 40% Jump In Asia Pacific Alternative Asset Allocations
- Summary: JPM reports a 40% increase in Asia Pacific alternative asset allocations, indicating strong regional growth.
- Date: 2026-11-14 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNVXlGcTdFelZ3d1ZtRUFjQk9scHlWSU5fWFE2TEd4OUtEZnRQWGVad0lBN1NKWWVfU0pOTFNJd001b1lOWDNEck1BcHpBSVNXaExWV1ZDMkdpLU9FWW8wYklvOFliblhUaHR3TXpza3VKeTcwZ3pjSW5WQjJ1ME05M0tNeGRIbWFpcmVDOFVfT3hudTRaRmc?oc=5>

### JPMorgan Chase (JPM) names its next CFO. Jeremy Barnum will become vice chairman.
- Summary: JPMorgan appoints Jeremy Barnum as CFO, signaling leadership continuity and potential strategic focus.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPLUo5Q1VwbWpnem5zNTdRZDhselFCQkMzQ3QybXE2ZktONndGVGxyNXM4RUdETFhRQ19DNWRKRFp4aXNWYzJMZ2hmTjBEdF9DWl9uM1k4UmwyeE5GaGxfTTFyMzJUaXpYMWsyQlRoQU9wXzhZUHNNLWdmR05jNVRyTG1icy1ROW51S0pXRVM4cGFzSENTTzU2ZnU1b3hnZVliSHlNTW5nSEk?oc=5>

## HEADWINDS

### Bearish Signal Threatens JPMorgan Stock’s Rally
- Summary: Bearish signal threatens JPM rally, raising downside concerns.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQQ3ZJZ3dUellBTGpNWnp6U1p5QXR2S2pLcERRRF9KTTRScURXNkJsbzFJOWNwNmNzTlVOSXM4OG1mVVFJTEttRWFJWnZuWUxtMGViZ0x2bm82SHBXazJCNEVPUmVVSldkem5MYWwzNTFIbUgtTVNVS0VHNFkwZGRFdDdobGVMUWNmdWt3REdvMlY5X2Y0NW9nbkM4ZnowSHIzblhKTVMxZDU?oc=5>

### What Does JPMorgan Chase (JPM) Mean For Investors If Card Rates Are Capped?
- Summary: Cap on card rates could reduce JPM’s revenue from card services.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxOaUR6ZDNoRFpjanljYXQ2UmlNTHgzek1xcloyVTdHd0FoWHBJNlBFQmJLMkhPSVpHOTNOSGR1dkt5MnVqSVZycFBZdlVWQ0JLMEpDd2c0Vi1JQmoyemprRGtYQmtaQ2VtdDRsbGdDa1RyMC1GT0MzdDhXV0NoelFGcWU1TmRxTDZIRGdsQnJhRzFFdWtoRkxpdFk5V0trUjJSckhYX2x4M0pUWGYxclVmM2F1bXVsZFZIQURFT0tWSlVFelpYYUHSAcsBQVVfeXFMTlU0c1J6VFJ2ZjFvWmRlNHZ5TXE1b2otOFF2VmdJRXRyaTFoS3hnQVEzcE0zOTc3Z1hWTFlFZlluWFFld2lwSTRzN3NYWUpfaTcyblEyZjZlQnJWNXd5SWFqaS1MdEtLU09wUUpobXl5ODVEUVlwWGlmaGN0VEtQVHJfbTk1NE9HNzZZSW02ZGFxcXFvMEt4Y2RQdlBuWXhMV1RFak4xazB2cnE4THFsTTJxaks1dkxWWnR5MHkwS0V1d2toOHpYRXhVRkE?oc=5>

### Chase, Big Banks Hit By Customer Reports of Outages. The Stocks Are Falling.
- Summary: Customer outage reports hit Chase and other banks, causing stock declines.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNRWlic0R4ampmbllNUC1OcUJxdW1BMmhZMnEtekdPY2g1RWJrNGx4UlE2SWVDSm9BdlA3dV9Ya0FjZEQxWHVORE5yQkZMSXF6VjQxR2tSTTZSQ2VqTEFJZ0Ywa0hHemdNR0RXTWdMWVQ4TEkzMURsQ0tTcHpOMlFmamU4a3JvamhsQk1xTDBGOEc1UVJSNnhQYVhPX093eU1E?oc=5>

### JPMorgan, BofA, Wells Fargo, other banks trade lower amid user reports indicating problems
- Summary: JPMorgan shares fell as market concerns over banking issues spread.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxNVWNFXzhUZ184SWp2TkR3VV9WUzdaVFpWT0ZmZUczNXI2WmZudzdRS0pHUHdxb1BsYnBrdGhOUS1HT1UtdmpsVFVRNG5JaE5RZHJvQ0VTdWlMR21uSHhiTms4ek44UjU2bTRualAtLXVma1FVaWlHLTB5NzdMQjRlLXlnUlZ2azh0OW5UMHRDcThfU2xveWllbXFSOGJlamd1MFg5LTlpOXZlSV9ySkFMT2tzN3Z3RWVkVFJMZmR1UEZWSDA?oc=5>

### JPMorgan Stock Slides: What's Going On?
- Summary: JPM stock has declined, reflecting market concerns or recent negative news.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPY25wTkZqdFZDWF93OFdXcFRsSmJWM0oybzR3b3N1OHZ1bURYVjlFZkoySHhQVkxrNjluVTBqQzNIQ2pGWGQwN0ZheXhvbk8yT18xQzYtaDhnSVJYTVA4VVQ4eUNkZDFzNDc5TW1fMXZsMzRGR0FnelpUaVZLeEhkNnpPd2RVLTNncEY4SGluTVA5dE5IbnF3aFFFdFFSQQ?oc=5>

### JPMorgan Chase & Co. (NYSE:JPM) Stock Price Down 2.3% - Should You Sell?
- Summary: JPM stock fell 2.3%, reflecting market concerns or short-term volatility. Investors may reassess positions.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxOeTYyMXg5NERqWVdFXzBTTEZFOVpsUHZKRHZkSEFNUUhiLU11djRUbmtRU2VxU2F6b2lZczBGZFZld2g5UDRYZWUyUkV2Qkl2VjBlOTVpNFpiVjdNQlg2eWVXNW9sYmJRNkhWc0J2NUN5NGVlQlh6NDdfQ2VMYVRxUTlJMDNsRXVzX2IwOGxvbERtTHV0ajlmWThOazdGS1NYa051b043TzdxRjdsZlMySll4dXdKdWt3M1NtNGtlUQ?oc=5>

## CATALYSTS

### JPMorgan Chase (JPM) Launches After Hours Token Transfers And Backs $500 Million Financing
- Summary: JPMorgan Chase (JPM) Launches After Hours Token Transfers And Backs $500 Million Financing
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNZFlCWkwwVG1XV0ticWR0NGR2d1dTN29wMk9vVllpbVJ6VVVSRXFuQUtaY0xwUmFoSk5wSVJQYlhvS1hmdkhsN01kQXBucU1YLTdoNEVkcmp2ekxBTzd5LV9TdFUzNzM3U2h3S01KNjItbHZWQ2xQakpEMDlDUlA1TFpKYUxPaWJQejZHNTRLd2VPcUtXTFg4bTd4bXZVeDg?oc=5>

### JPMorgan Chase & Co. (JPM) Up 2.4% Since Last Earnings Report: Can It Continue?
- Summary: Shares of JPM rose 2.4% after the latest earnings release, raising questions about sustaining the upward trend.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPeTd2Z2g4LXpqenNnYkozQUZBV1JUODhBeHdkcERHZENfOWpYWm5wU1pTXzRpcFBDX2d1dDdDcmk3cHFDTGtFVGdzYlpPYV9HWnVTeTc5SV90ekEtR29KVTFyb1JPb29FUGZNbXM5bzFuY3NxWWkyR3Q4SmVRZkhfUWN5WW5WbGJ4MGRqeGR3TVpqdw?oc=5>

### JPMorgan Chase Increases Crypto Exposure
- Summary: JPM expands crypto services, signaling new product offering.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQTmFqNmhWdGc2ZXhyZDhQcHdWMjhUWGxLeWFFdHFVekg2bjdJbDUtYlBhSFVoVGwxUXM3T1R0bkZyVDNjMDVaMUFrbUFqWHptZTVta01lbmp2Z1ZYQVYyY1BIYkg2VlY0NnNkTEVXMTg5NEY1dnhvS3pSRDhXZHhEUm1WSEFLVFA4TWdVQS1qeXItWTA4RzdranBmR1VZbmdQU0owR3gweEc?oc=5>

### JPMorgan Chase announces CFO transition, confirms resolving 'technical issue' (JPM:NYSE)
- Summary: JPM announces CFO transition and resolves a technical issue, indicating internal operational changes.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNbUgxQkh0ZkRTNW9FNlV6TElsVVdudTRKcG9GYlVrYnF4dFNsMVB1LU0wdGVobGxYLTFuSWtSOEVhZThSYy11Q3lJUmRZYWF3V2I3cndtb3plS25NMmtleUxNR21DcFRwajZqR0E1bXFYS253VjVwTUNMRnJyeUtjb3F2Ulpzd3BnVWY1MHdkR2xncGRxMndDQ0prcll2VE5ndlBPVGpFakZIdmlUTU9RRkxB?oc=5>

## RISKS

### After Monday's Banking Outage, JPMorgan Chase (NYSE:JPM) Slips as It Names a New CFO
- Summary: JPM names a new CFO following a banking outage, causing a brief stock dip.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxORC1SRjZ5SU8xVUlXeUNqa2VxbURUdW1ERERZNURkcjFDdkVHSHRjRTVSdWVTNG1qVVN4cS15d0xPQnllMUVsMDFlbUhIXzB2M0dfaXZOMVFUS29qaFZoSUJ3NnEwX01QTG1DdzZEQVNFY1VSTDc0TXdvaVFTQVdPXzBLZWd3eXlvOVoteW0wWUx4WjRMMXlaZlFBdWUxSElhNjAxUFJvRGxoSVlZVllDaV9Xbw?oc=5>

### What Drove Big Bank Stocks Such as JPMorgan Chase (NYSE:JPM) to Fall More Than 2% as the Sell-Off Widened?
- Summary: Market sell-off pushes JPM shares down over 2%, reflecting broader bank sector weakness.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxPTUVJYV8zU3dNTUhHdnZHZkxhaEI5X2tidUVtWUZ2RmV2XzdVN2h0eXNfVlBxY1BselQtX0lGWlN0YlkzMWhEeXhvQnhXX3VYdUZKbE9KZ2hudXBDUVNxZTVnV0VkOUpyaGFsUDUtUzZKakVEdjlZN3pqOVNBdFBPVHN2Z0MxclpjOE94SktMYnFLN3p2djhTRlRBdzlvRkhBYmVQcFkwamc3c3B1SThHWXc3Ri1obUVFdkh6WmpqUU5xV1RKcmFpeXVQNkFwMDBS?oc=5>

### Chase, Bank of America, Wells Fargo Customers Report Banking Problems
- Summary: Customers report banking issues at JPM, BofA, and Wells Fargo, raising operational risk concerns.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxObjAzMG50cm9JUFhqYUZBb2JKdTJsUzZQWUpaTWJJc0pZS2lNUDJLSldZQjllUlloVG9xSng4eHNOdndBUW1GcmE3XzdHY1Z1V3Y4Njc2TXY1MndBMHA2aTIweTR3VXR6RFpIeVFMQWdwZ3lOWU90ei01VVJOQ0tGYTdEcVkzUHRTaGdJVFF3ZlAtOGhaX25GcGJzTmxxc1VyMjRfVmRsaThTNE54U0hGdGxORzc0RUNUdlNV?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **JPM** | **14.19** | **2.49** | **N/A** | **10.20** | **876,244,893,696.00 USD** | **11.97** |
| BAC | 11.94 | 1.26 | N/A | 3.40 | 341,146,337,280.00 USD | -1.92 |
| C | 11.83 | 1.04 | N/A | 8.00 | 198,525,222,912.00 USD | 24.68 |
| WFC | 11.66 | 1.56 | N/A | 0.40 | 248,223,006,720.00 USD | 1.35 |

Peers fetched as_of: 2026-11-17; JPM reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-13
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-17

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 24,246,000,000.00 USD; period 2014-07-01/2014-09-30; fiscal year/reporting period 2014/Q3
- Net income (latest available single quarter): 15,305,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/19617/000162828026069523/jpm-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilwFBVV95cUxNQWQ4UlBOQ3VlbjFqcEpma1BDMjRRczVfalJRVWZaUjdyY2l0Rmw2NWtvb2gzVXZ2R2JTR09LSlFIcmd5aVh1NklOcU1BUGhVVTY3ZEFwdEdlcWZuLXZTbzNsOVoybXdOcDJTR3A3T2FvbDNaMmZZbmVTQTVGZGhCY3RGQVllZmN1ZG9DbXNfd090MzkwRHdR?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNVXlGcTdFelZ3d1ZtRUFjQk9scHlWSU5fWFE2TEd4OUtEZnRQWGVad0lBN1NKWWVfU0pOTFNJd001b1lOWDNEck1BcHpBSVNXaExWV1ZDMkdpLU9FWW8wYklvOFliblhUaHR3TXpza3VKeTcwZ3pjSW5WQjJ1ME05M0tNeGRIbWFpcmVDOFVfT3hudTRaRmc?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPLUo5Q1VwbWpnem5zNTdRZDhselFCQkMzQ3QybXE2ZktONndGVGxyNXM4RUdETFhRQ19DNWRKRFp4aXNWYzJMZ2hmTjBEdF9DWl9uM1k4UmwyeE5GaGxfTTFyMzJUaXpYMWsyQlRoQU9wXzhZUHNNLWdmR05jNVRyTG1icy1ROW51S0pXRVM4cGFzSENTTzU2ZnU1b3hnZVliSHlNTW5nSEk?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQQ3ZJZ3dUellBTGpNWnp6U1p5QXR2S2pLcERRRF9KTTRScURXNkJsbzFJOWNwNmNzTlVOSXM4OG1mVVFJTEttRWFJWnZuWUxtMGViZ0x2bm82SHBXazJCNEVPUmVVSldkem5MYWwzNTFIbUgtTVNVS0VHNFkwZGRFdDdobGVMUWNmdWt3REdvMlY5X2Y0NW9nbkM4ZnowSHIzblhKTVMxZDU?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxOaUR6ZDNoRFpjanljYXQ2UmlNTHgzek1xcloyVTdHd0FoWHBJNlBFQmJLMkhPSVpHOTNOSGR1dkt5MnVqSVZycFBZdlVWQ0JLMEpDd2c0Vi1JQmoyemprRGtYQmtaQ2VtdDRsbGdDa1RyMC1GT0MzdDhXV0NoelFGcWU1TmRxTDZIRGdsQnJhRzFFdWtoRkxpdFk5V0trUjJSckhYX2x4M0pUWGYxclVmM2F1bXVsZFZIQURFT0tWSlVFelpYYUHSAcsBQVVfeXFMTlU0c1J6VFJ2ZjFvWmRlNHZ5TXE1b2otOFF2VmdJRXRyaTFoS3hnQVEzcE0zOTc3Z1hWTFlFZlluWFFld2lwSTRzN3NYWUpfaTcyblEyZjZlQnJWNXd5SWFqaS1MdEtLU09wUUpobXl5ODVEUVlwWGlmaGN0VEtQVHJfbTk1NE9HNzZZSW02ZGFxcXFvMEt4Y2RQdlBuWXhMV1RFak4xazB2cnE4THFsTTJxaks1dkxWWnR5MHkwS0V1d2toOHpYRXhVRkE?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNRWlic0R4ampmbllNUC1OcUJxdW1BMmhZMnEtekdPY2g1RWJrNGx4UlE2SWVDSm9BdlA3dV9Ya0FjZEQxWHVORE5yQkZMSXF6VjQxR2tSTTZSQ2VqTEFJZ0Ywa0hHemdNR0RXTWdMWVQ4TEkzMURsQ0tTcHpOMlFmamU4a3JvamhsQk1xTDBGOEc1UVJSNnhQYVhPX093eU1E?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNVWNFXzhUZ184SWp2TkR3VV9WUzdaVFpWT0ZmZUczNXI2WmZudzdRS0pHUHdxb1BsYnBrdGhOUS1HT1UtdmpsVFVRNG5JaE5RZHJvQ0VTdWlMR21uSHhiTms4ek44UjU2bTRualAtLXVma1FVaWlHLTB5NzdMQjRlLXlnUlZ2azh0OW5UMHRDcThfU2xveWllbXFSOGJlamd1MFg5LTlpOXZlSV9ySkFMT2tzN3Z3RWVkVFJMZmR1UEZWSDA?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPY25wTkZqdFZDWF93OFdXcFRsSmJWM0oybzR3b3N1OHZ1bURYVjlFZkoySHhQVkxrNjluVTBqQzNIQ2pGWGQwN0ZheXhvbk8yT18xQzYtaDhnSVJYTVA4VVQ4eUNkZDFzNDc5TW1fMXZsMzRGR0FnelpUaVZLeEhkNnpPd2RVLTNncEY4SGluTVA5dE5IbnF3aFFFdFFSQQ?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxOeTYyMXg5NERqWVdFXzBTTEZFOVpsUHZKRHZkSEFNUUhiLU11djRUbmtRU2VxU2F6b2lZczBGZFZld2g5UDRYZWUyUkV2Qkl2VjBlOTVpNFpiVjdNQlg2eWVXNW9sYmJRNkhWc0J2NUN5NGVlQlh6NDdfQ2VMYVRxUTlJMDNsRXVzX2IwOGxvbERtTHV0ajlmWThOazdGS1NYa051b043TzdxRjdsZlMySll4dXdKdWt3M1NtNGtlUQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNZFlCWkwwVG1XV0ticWR0NGR2d1dTN29wMk9vVllpbVJ6VVVSRXFuQUtaY0xwUmFoSk5wSVJQYlhvS1hmdkhsN01kQXBucU1YLTdoNEVkcmp2ekxBTzd5LV9TdFUzNzM3U2h3S01KNjItbHZWQ2xQakpEMDlDUlA1TFpKYUxPaWJQejZHNTRLd2VPcUtXTFg4bTd4bXZVeDg?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPeTd2Z2g4LXpqenNnYkozQUZBV1JUODhBeHdkcERHZENfOWpYWm5wU1pTXzRpcFBDX2d1dDdDcmk3cHFDTGtFVGdzYlpPYV9HWnVTeTc5SV90ekEtR29KVTFyb1JPb29FUGZNbXM5bzFuY3NxWWkyR3Q4SmVRZkhfUWN5WW5WbGJ4MGRqeGR3TVpqdw?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQTmFqNmhWdGc2ZXhyZDhQcHdWMjhUWGxLeWFFdHFVekg2bjdJbDUtYlBhSFVoVGwxUXM3T1R0bkZyVDNjMDVaMUFrbUFqWHptZTVta01lbmp2Z1ZYQVYyY1BIYkg2VlY0NnNkTEVXMTg5NEY1dnhvS3pSRDhXZHhEUm1WSEFLVFA4TWdVQS1qeXItWTA4RzdranBmR1VZbmdQU0owR3gweEc?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNbUgxQkh0ZkRTNW9FNlV6TElsVVdudTRKcG9GYlVrYnF4dFNsMVB1LU0wdGVobGxYLTFuSWtSOEVhZThSYy11Q3lJUmRZYWF3V2I3cndtb3plS25NMmtleUxNR21DcFRwajZqR0E1bXFYS253VjVwTUNMRnJyeUtjb3F2Ulpzd3BnVWY1MHdkR2xncGRxMndDQ0prcll2VE5ndlBPVGpFakZIdmlUTU9RRkxB?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxORC1SRjZ5SU8xVUlXeUNqa2VxbURUdW1ERERZNURkcjFDdkVHSHRjRTVSdWVTNG1qVVN4cS15d0xPQnllMUVsMDFlbUhIXzB2M0dfaXZOMVFUS29qaFZoSUJ3NnEwX01QTG1DdzZEQVNFY1VSTDc0TXdvaVFTQVdPXzBLZWd3eXlvOVoteW0wWUx4WjRMMXlaZlFBdWUxSElhNjAxUFJvRGxoSVlZVllDaV9Xbw?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxPTUVJYV8zU3dNTUhHdnZHZkxhaEI5X2tidUVtWUZ2RmV2XzdVN2h0eXNfVlBxY1BselQtX0lGWlN0YlkzMWhEeXhvQnhXX3VYdUZKbE9KZ2hudXBDUVNxZTVnV0VkOUpyaGFsUDUtUzZKakVEdjlZN3pqOVNBdFBPVHN2Z0MxclpjOE94SktMYnFLN3p2djhTRlRBdzlvRkhBYmVQcFkwamc3c3B1SThHWXc3Ri1obUVFdkh6WmpqUU5xV1RKcmFpeXVQNkFwMDBS?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxObjAzMG50cm9JUFhqYUZBb2JKdTJsUzZQWUpaTWJJc0pZS2lNUDJLSldZQjllUlloVG9xSng4eHNOdndBUW1GcmE3XzdHY1Z1V3Y4Njc2TXY1MndBMHA2aTIweTR3VXR6RFpIeVFMQWdwZ3lOWU90ei01VVJOQ0tGYTdEcVkzUHRTaGdJVFF3ZlAtOGhaX25GcGJzTmxxc1VyMjRfVmRsaThTNE54U0hGdGxORzc0RUNUdlNV?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
