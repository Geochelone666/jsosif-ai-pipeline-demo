# META Intelligence Report

- ticker: **META**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/META/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/META/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T05:54:20.818664+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 6, 'ai': 14, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261116T043911Z-b81cfeb4/META** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 12 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 34.78%; oldest publication 2026-11-13

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 618.8700 |
| Return 1D (%) | -1.2037 |
| Return 1W (%) | -3.5111 |
| Return 1M (%) | -12.7529 |
| Return YTD (%) | -6.0032 |
| Return 1Y (%) | 3.1493 |
| Annualized volatility (%) | 41.7234 |
| Beta vs SPY | 1.3685 |
| Max drawdown (%) | -28.7332 |
| Sharpe (rf=0) | 0.2809 |
| Downside deviation (rf=0, %) | 27.5309 |
| Sortino (rf=0) | 0.4257 |
| Historical VaR 95% (1D, %) | 3.7761 |
| Historical ES 95% (1D, %) | 5.6434 |
| Correlation vs SPY | 0.4520 |
| Tracking error vs SPY (%) | 37.5625 |
| P/E (trailing) | 21.37 |
| P/B | 5.81 |
| EV/EBITDA | 13.89 |
| Revenue growth (%) | 26.10 |
| Forward P/E (estimate) | 17.35 |
| Gross margin (%) | 81.03 |
| Operating margin (%) | 37.78 |
| Return on equity (%) | 32.26 |
| Free cash flow yield (%) | 1.07 |
| MA50 | 680.0232 |
| Close vs MA50 (%) | -8.9928 |
| MA200 | 629.1538 |
| Close vs MA200 (%) | -1.6345 |
| RSI (14, Wilder) | 42.0484 |
| MACD (12,26) | -14.6183 |
| MACD signal (9) | -16.5132 |
| MACD histogram | 1.8949 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'META': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 618.8700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.2037 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.5111 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -12.7529 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -6.0032 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.1493 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.7234 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 27.5309 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4257 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.7761 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.6434 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4520 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.5625 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3685 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.7332 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2809 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.3474 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.0340 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 37.7770 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.2640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0650 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.3698 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 42.0484 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.8949 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -8.9928 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -1.6345 -> Slightly below the moving-average trend level.

## TAILWINDS

### Meta Platforms (META) Surges as AI Ranking Models Accelerate U.S. Ad Revenue Growth to 31%
- Summary: Meta Platforms (META) Surges as AI Ranking Models Accelerate U.S. Ad Revenue Growth to 31%
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOajhtMTV2NGZ2MExsOHhtT0U3VUtUNG1jZGg5SW1TTWZCOW9OVWpiTmRaeUZHdy1CT1p6R29ieFBNNVZkZ3UxVWFWa0lMUDZjNE1xQ3I1aHFDVi10aVdMNDJXZ1JEWTdHNEVWLW9SOFFzbEJBSjUwZkNFRWtURUhqVEtralp1ZFJSNjl4M3ZPeHk2WTE1VWJhM3RR?oc=5>

### Will ETF Buying Change Meta Stock Narrative
- Summary: ETF buying could shift Meta’s stock narrative, potentially boosting investor interest.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNUnhObF9vcWxydnRua1J4T2hsVjhTOExiYjFWYUJhTmxGazE1ZS1zTzVBN3JuUTkwaHVKM3h0bm95ZXU4NlBLQkFmbkk1cnlYVTBlc1F4Rk9VaVV4cnhtd1Y1QnVETzNjbkZvM3FObVc5Y182VjVjc1B4SXBIbjAwSUp3WUZlVXpqOHpFbkkxT2pqbGhKQWxEMw?oc=5>

### 55 ETFs Add to Meta Platforms (META) on Nov. 11
- Summary: Fifty-five ETFs added Meta shares, boosting demand.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQZkc4MEpkMmtxWldrMnI5ZUdHVjMyb1ZBU3duZklHdnBQekw0VnYzR0hoZWRMV3EtOUdScmpzd2E1ZEYxcjNfR3NKNWR6R3JzZWJtWE5SbG4ydTcxSzZRN3lXMmFHV01JaU1SSDNXVF8yRnM3U1VJS2RQYllEd0p3cGNTWV9jc3JTcjRpQkVla0ZLMUd3V1E?oc=5>

### Meta Platforms, Inc. (META): Strong Advertising Growth Supports Its Long-Term Investment Case
- Summary: Positive analyst view on Meta’s advertising growth and long-term value.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQTWVldU50RklZVlZIS3ZFanQxVWZ2Wmt2TXVlVTU3OVpoTWN6aThIYmFCYXJYd3l0NDNQVWU4enZlWWcySXYtWjBadFdZSEx1MF9TQjFfcU1nOW5UeHBiaDNGbWhNZExZOFA0MlRxN1BrazVuLXktVTA0b3NFNXl3TF8tekROcmdtZTQwMGlQdjRwMWxyamc?oc=5>

### Meta Platforms is Cheap at 18.78X P/E: Buy, Sell or Hold the Stock?
- Summary: Neutral assessment of Meta’s valuation, suggesting possible action.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxOMGZwclMxVEtFaXU5X0RJV1ZxM0FTd0lGQzFuNEJGWUhaTzJJSzNfUHI0SHU5MGZXcVE4bzlVaWswbjN0RGp4aUdOWHFkY2Zpc2x6bXU5bHdLVnh4Rmo0c2xQekxUQ2k4S2JnNF95aWFhd2VBbml3TmJjNThSNkh2c3BNYkl4ZHhzMURfeVQ3aTFkc3A1bWw2S09fMWdzdlpVckZjWjR4dnBJUlVVTGhLRHVJMl9BLVNCZXhpYw?oc=5>

## HEADWINDS

### Meta Platforms (NASDAQ:META) Stock Price Down 1.2% - Here's Why
- Summary: Meta Platforms (NASDAQ:META) Stock Price Down 1.2% - Here's Why
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxPc016YU5ocVJaODRsckZ6Q0tNWDFybVJSMXkzVGctZzBETnlKdnVMUWthMVdZbm1lWl9vS09YVmRfblprUjI5Q0F0dEpoQ1NKTXp1Z0hYV2F2QWVRV1N1MHhfRzB1cThfdEtTTU9vZ09pbG1YU3FGWWJjLVN5ajY2QV8yVTNQdW1Kc2FEeDRWTzhWYlRueWtnWVZhU241d3FkR012ZkFxQUprRVJxdTkwNTFTbmZRcUk?oc=5>

### Meta Stock Falls 2.4% as AI Stocks Slide (Nov 16)
- Summary: Meta Stock Falls 2.4% as AI Stocks Slide (Nov 16)
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE1USnRYOHF3MW9LT3RmelZXUXZ0NDIyREJUZHdTUmUtaDBkMG9RLVBrRTRCbDQ1OVVhSkVnekZ5Y3owYmJXVGdKNXkyWjU0SUMtSmI3TWxtZkFZUUE5RXlnejNMS3Z6SlVGTVc3Z1NSRWxaMXluby1qajJWVEdZZw?oc=5>

### Meta Stocks Fall 2.5% After Italy Fines Facebook 805 Million Over Photo Access
- Summary: Meta Stocks Fall 2.5% After Italy Fines Facebook 805 Million Over Photo Access
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxON2RHX0dtc09zZU9JbXRhSnVETUpuZ1BaMlI1V0dwR0dKYWpnbjZPX0hfenlOa0pXNzVZSUc3YVItbFFhcWdueWYwN2R5U255cnpyNmtWODZjQ04zd1BPVWJlUEZCU1BsX2s4V1o4QnNqSFVmR1F2ekZQNGZPS3V2bUk2anV0eGgybXR3M0pzaEVNM1pseDFfSk1ldHlaall3Tno0NTJKWVhPLThUem5IVTR6LTdXdVptbjRub2I0S05JZjN6eVJBZVVza0dnS1RHTVFZ?oc=5>

### ‘You Don’t Want Rogue Agents’: Jamie Dimon Shuts Meta’s Muse AI Agent Out of JPMorgan. What It Means for META Stock.
- Summary: JPMorgan removed Meta’s Muse AI agent, signaling product concerns.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi6AFBVV95cUxQWnVuTHBtMHBwdV95Q2hjemI1dmE0bGQ2YkNjNVUtcGNNOE5pRWNFenhUbThJcmF3QkxIalI4SWx3UGlPS3VvVHpYN1ZZd0phR043dzZTcTZuaUY4eWcyeDJ4Z2k0VnVnNmpnZkVlejZ6SzdEdDNJM05qZ0hoQ0JDVTY1dnE4eTM2cVdHYkVjU0FUODNnczRudDc0TmNoendwallmdTRxU2hjdy04Zi16SWVTY3dvSFZsU1VWUzRSTkNidTVGb0xjVjBWZFNRdEtQdWdwNVhlc3lTV2ZXMmtscXFOXzNsLUV6?oc=5>

### Meta Platforms faces negative S&P credit outlook and Italian fine: Can META avoid deeper losses?
- Summary: Negative credit outlook and regulatory fine threaten Meta’s financial standing.
- Date: 2026-11-17 | Impact: high | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxPRTNmUkFENGd3VUdENTdLeVJhNVdrdWZxSUNhdGNoRTI5eVhHSjZENzlPaUFmbVVENDMzaEx1NU5GZ3h5c0FJWlNjVHh4NmJtNjVYSGxpNGtRZEZzV1pZajhwcHdEa3dIX0o1MHN1ZWdsb0tYTk9nTFZNU2dnNE1MQW9zXzJWcVVWVGx5ZkNnZVE?oc=5>

### Why is Meta Platforms stock sliding today?
- Summary: Current stock decline indicates market pressure on Meta.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQcHNmVmZmZ1hYcVM5ZVAyNHZKU3NnNFhLRzBpZ1g5OVFuRktuSi1RZVpCYnlySEtOQjdMcjhrLTVGSEpQZVdZQWktQmhrZ29xMGFEal9fZzR6dDJ6TXY1dW1qS3JjTlk4QUFjUE5fdUxNeWE0ZUtKWXVzMm5PSGRISlRnQTRHN0N0Sl9lVjB4bEtSSE52VmpUZWxzLXkyTVA4MjY1eWNR?oc=5>

### As Meta Platforms Continues To Weaken, A Bearish Trade May Be In Order
- Summary: Negative outlook on Meta’s performance, recommending bearish position.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPeXYtc0wwTWRuR29fdGRXZE83a0JHb3Y2Q2Y4b3NPOXVZSjM3TEc5VzJhTkFBN1dHekhaUm9XOWdrbWl2OUx5eWRraVVIWm02YjhQV2M3MWpLbk5ld1c5TG1rRGE5Sm1Td0dMWFQ0b2dMYVp2Wko5SmxEMGEtSDFJWldKXzFEV3hjOTNtQkVFeVRpSjEzOFE?oc=5>

### Should You Be Worried About Meta Stock?
- Summary: Negative sentiment questioning Meta’s stability.
- Date: 2026-11-16 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQSEEtMlFKdlpSZkhPeUpYMThkT2ZmZHVZYjhpOEc2QXJSbUN1dm9lRnhvUEpqb0psX2hGTUtQR0Fla0g5U051ZTBQS1VUS0wzdjNlNldhOXFPTmV6YjZoVXVMYlpJQUVpWDliZnh3WUxoeUVjYlBZdHU1eExFT3l3V0xna2NTbGQwT2t1Y2RlUzJLOWdQVGFyd0hreWt3M3VT?oc=5>

## CATALYSTS

### Meta AI Momentum Offsetting Spending Concerns, Says UBS — Analyst Sees 30% Potential Upside
- Summary: Meta AI Momentum Offsetting Spending Concerns, Says UBS — Analyst Sees 30% Potential Upside
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxNU1NVb3ZzTC1qdVNoWUFfbXRCSG1sVG8tU0RpbXlsQmRhYjlPTWxHUldSZlRXNmdrZHY2NmE2YUZMTy02ZDNsRzNUbTFPOTBxdWJsQjU4WDltQzRtYmtRbFZValpGUGQ0V2h3MUVTN2JNcmdBY21XaV9PQi1KT2lXdi1TQ3pNZEptdHRrUEpaaFFPb0hIUnNWajdTaXBCV3JtSEFjLUE4eDBPRWJOZDFGbkVKTEdBMS1BT19nbnNWeFlxeC1MNzRzTmxDV2pSd3RwTXpzcVlyVlk3ZDk4ZWdNMG5B?oc=5>

### Meta Plunged After Earnings in 2025 Too. Here’s What Buyers Got a Year Later
- Summary: Meta Plunged After Earnings in 2025 Too. Here’s What Buyers Got a Year Later
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPY1U3di1QYW5mN3NoYXJWUUdqVHVDSHNOV3hnbTVNZE9zQmE5YjZSMXp0SW9BWjJORjNfakJibjZDa01zWmFzajZHUDdpc1U4UmJmeEpucTFrcnRsWGtOaE1DOGNTaEhzR0lrSFdkY3o2QTdlSTNBTWh2SWN4el9ZQ1Z1Ukg2a3dPNTVSdzVkZEc3RGdGRm5JdDdjSVRLVmNRQ1AtTHNHVUQ2ZlBGdlNCa0VfWTZhVEtjR0E?oc=5>

### UBS assumes coverage on Meta stock with buy rating on AI momentum
- Summary: UBS upgrades Meta to buy, citing AI momentum.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxPYWh1UVdtSVlJRXVPckZzbjRqQU1kNnBiNzRxZ0NWVThQclFRV2VZM3I3VFBtcG1sN3VwdTdoOVBZZHV1YXlZUEZ3aEQ5WTlOdkpkTDJ0cVlCY0hmSlhXR3BGNFBEdFFabVBteHNUbXRWTF9Ha1NRUmZyRy1fZ1RFb2t4QWhEYVN6djZzQ3JZckNIeTh1SldRbnFJNzRjLUFvTlpPYnBUR0NaWjMtVEZxcFdzT0ViNjJ6ZFhvMVZQWlhsZkU?oc=5>

### Is Meta Stock Still a Buy After Borrowing About $25 Billion This Month?
- Summary: Meta's $25B borrowing raises financial risk concerns.
- Date: 2026-11-15 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxOX3VnN3lfRkVjaVdFejdqMU5FRTdWalgzeDlRa2FxVVJmVjgwTElnS3lZMVVMWl9vY29KSEpyX3FMQ0l6MXFwLUZRYm5WaGUwSk9kbzlKWEVMU3JwSjA1UDZzai1obVI2YkVMb0hDc2x2T3hvd1pLRFpOX3A5R3cwWE5IcG1ybmo2TmlZUktfRXU2aW5CM1hyRmstWkpTRU12bUd4bzRJRC1EeVZaWWhHTy1MMFZSdw?oc=5>

### Is Trending Stock Meta Platforms, Inc. (META) a Buy Now?
- Summary: Analyst recommends buying Meta stock.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPSTBYOEhPRmxzaDFtY3Q0TDZwWWtnTHZNbF9JeWhabWt0NVllMHQ5ZTJQVDZYTkpzTHZ6Yi1iVkNiaGpmV0dlQXVIZlgxc2V4RnRUcHFRZDB2TldsTk5Lb1FONEZVRFN3ZmZaNERLall3LXM1VzVMd29BLXlCWXpvdTBHOGdoc0JWNm1Nb3E3SDdsTGlCUjNlVHhXc1AzWFk?oc=5>

### Meta Stock Has Fallen 3% YTD. Its Cheapest AI Model Could Change Everything.
- Summary: Meta shares down 3% YTD amid AI model speculation.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxOeHFlaXBvVWhiTmtvbkJleXlOQnVNNWladTcwdWtFbDF0MFJ3OENoZWxsRHpsZVNabVVyZzZOdHJDZUR4QmZCOVdicG5lOVdGcEVxR1FvRzRuMTZJMGZGdGpFMHRwWWpSVmVWa2o2Y0xmRjlwSGZtQWVWVmhYQW5lcVJwZ2ZCYVJ6aC1nNHVCbXQ?oc=5>

## RISKS

### Meta (META) Faces $880 Million Italy Fine Over User Photo Access
- Summary: Meta fined $880M in Italy for user photo access violations, posing regulatory and financial risk.
- Date: 2026-11-15 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxOTUdFQ3JuakFLZUxCSzVwSDIzRmcxR0lVX1V0Tks5eVdXNkRKM21EaWh5dXh6T2lzTnQtWkNjLThJTC1oeElFU2wyLXNGM3dzMGhGd2RULXQ2TEhkaUJVU284Wk9YeXNkdmJ2cDdsSHB5ZGd6VjBybXRkU1JiR0xOZE82ZVB0bVl5NzY5OUFjN2s4QQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **META** | **21.37** | **5.81** | **13.89** | **26.10** | **1,581,980,975,104.00 USD** | **3.15** |
| GOOGL | 14.82 | 5.22 | 18.05 | 24.70 | 3,444,778,729,472.00 USD | -1.44 |
| SNAP | N/A | 4.23 | 57.30 | 14.30 | 9,496,172,544.00 USD | -32.76 |
| PINS | 75.29 | 3.33 | 34.07 | 11.90 | 10,363,286,528.00 USD | -29.19 |

Peers fetched as_of: 2026-11-17; META reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

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
- Filing date: 2026-10-22
- Revenue (latest available single quarter): 13,727,000,000.00 USD; period 2018-07-01/2018-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 9,860,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimgFBVV95cUxOajhtMTV2NGZ2MExsOHhtT0U3VUtUNG1jZGg5SW1TTWZCOW9OVWpiTmRaeUZHdy1CT1p6R29ieFBNNVZkZ3UxVWFWa0lMUDZjNE1xQ3I1aHFDVi10aVdMNDJXZ1JEWTdHNEVWLW9SOFFzbEJBSjUwZkNFRWtURUhqVEtralp1ZFJSNjl4M3ZPeHk2WTE1VWJhM3RR?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNUnhObF9vcWxydnRua1J4T2hsVjhTOExiYjFWYUJhTmxGazE1ZS1zTzVBN3JuUTkwaHVKM3h0bm95ZXU4NlBLQkFmbkk1cnlYVTBlc1F4Rk9VaVV4cnhtd1Y1QnVETzNjbkZvM3FObVc5Y182VjVjc1B4SXBIbjAwSUp3WUZlVXpqOHpFbkkxT2pqbGhKQWxEMw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQZkc4MEpkMmtxWldrMnI5ZUdHVjMyb1ZBU3duZklHdnBQekw0VnYzR0hoZWRMV3EtOUdScmpzd2E1ZEYxcjNfR3NKNWR6R3JzZWJtWE5SbG4ydTcxSzZRN3lXMmFHV01JaU1SSDNXVF8yRnM3U1VJS2RQYllEd0p3cGNTWV9jc3JTcjRpQkVla0ZLMUd3V1E?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQTWVldU50RklZVlZIS3ZFanQxVWZ2Wmt2TXVlVTU3OVpoTWN6aThIYmFCYXJYd3l0NDNQVWU4enZlWWcySXYtWjBadFdZSEx1MF9TQjFfcU1nOW5UeHBiaDNGbWhNZExZOFA0MlRxN1BrazVuLXktVTA0b3NFNXl3TF8tekROcmdtZTQwMGlQdjRwMWxyamc?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxOMGZwclMxVEtFaXU5X0RJV1ZxM0FTd0lGQzFuNEJGWUhaTzJJSzNfUHI0SHU5MGZXcVE4bzlVaWswbjN0RGp4aUdOWHFkY2Zpc2x6bXU5bHdLVnh4Rmo0c2xQekxUQ2k4S2JnNF95aWFhd2VBbml3TmJjNThSNkh2c3BNYkl4ZHhzMURfeVQ3aTFkc3A1bWw2S09fMWdzdlpVckZjWjR4dnBJUlVVTGhLRHVJMl9BLVNCZXhpYw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPbnEycDVUY09YNUpselQtRk0zcm45R0t3UGJveUhxdWxPV1F3OHMtY05lc2g4RU1lSnNTSV9NTG9kSjd3d3BKU0tRVEtWZXF0T3doWmxPbkR3Rjk0QWtYM3BGakY2NGFXVFRfT3V3TDh6Z0sza1lsYlZVV09KYW1SdDUwMFVCUVdkTXhIVEYzUlZHanZWWFVDa0llOW1PMERnblo4T1N3?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxPc016YU5ocVJaODRsckZ6Q0tNWDFybVJSMXkzVGctZzBETnlKdnVMUWthMVdZbm1lWl9vS09YVmRfblprUjI5Q0F0dEpoQ1NKTXp1Z0hYV2F2QWVRV1N1MHhfRzB1cThfdEtTTU9vZ09pbG1YU3FGWWJjLVN5ajY2QV8yVTNQdW1Kc2FEeDRWTzhWYlRueWtnWVZhU241d3FkR012ZkFxQUprRVJxdTkwNTFTbmZRcUk?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE1USnRYOHF3MW9LT3RmelZXUXZ0NDIyREJUZHdTUmUtaDBkMG9RLVBrRTRCbDQ1OVVhSkVnekZ5Y3owYmJXVGdKNXkyWjU0SUMtSmI3TWxtZkFZUUE5RXlnejNMS3Z6SlVGTVc3Z1NSRWxaMXluby1qajJWVEdZZw?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxON2RHX0dtc09zZU9JbXRhSnVETUpuZ1BaMlI1V0dwR0dKYWpnbjZPX0hfenlOa0pXNzVZSUc3YVItbFFhcWdueWYwN2R5U255cnpyNmtWODZjQ04zd1BPVWJlUEZCU1BsX2s4V1o4QnNqSFVmR1F2ekZQNGZPS3V2bUk2anV0eGgybXR3M0pzaEVNM1pseDFfSk1ldHlaall3Tno0NTJKWVhPLThUem5IVTR6LTdXdVptbjRub2I0S05JZjN6eVJBZVVza0dnS1RHTVFZ?oc=5
- https://news.google.com/rss/articles/CBMi6AFBVV95cUxQWnVuTHBtMHBwdV95Q2hjemI1dmE0bGQ2YkNjNVUtcGNNOE5pRWNFenhUbThJcmF3QkxIalI4SWx3UGlPS3VvVHpYN1ZZd0phR043dzZTcTZuaUY4eWcyeDJ4Z2k0VnVnNmpnZkVlejZ6SzdEdDNJM05qZ0hoQ0JDVTY1dnE4eTM2cVdHYkVjU0FUODNnczRudDc0TmNoendwallmdTRxU2hjdy04Zi16SWVTY3dvSFZsU1VWUzRSTkNidTVGb0xjVjBWZFNRdEtQdWdwNVhlc3lTV2ZXMmtscXFOXzNsLUV6?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxPRTNmUkFENGd3VUdENTdLeVJhNVdrdWZxSUNhdGNoRTI5eVhHSjZENzlPaUFmbVVENDMzaEx1NU5GZ3h5c0FJWlNjVHh4NmJtNjVYSGxpNGtRZEZzV1pZajhwcHdEa3dIX0o1MHN1ZWdsb0tYTk9nTFZNU2dnNE1MQW9zXzJWcVVWVGx5ZkNnZVE?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQcHNmVmZmZ1hYcVM5ZVAyNHZKU3NnNFhLRzBpZ1g5OVFuRktuSi1RZVpCYnlySEtOQjdMcjhrLTVGSEpQZVdZQWktQmhrZ29xMGFEal9fZzR6dDJ6TXY1dW1qS3JjTlk4QUFjUE5fdUxNeWE0ZUtKWXVzMm5PSGRISlRnQTRHN0N0Sl9lVjB4bEtSSE52VmpUZWxzLXkyTVA4MjY1eWNR?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPeXYtc0wwTWRuR29fdGRXZE83a0JHb3Y2Q2Y4b3NPOXVZSjM3TEc5VzJhTkFBN1dHekhaUm9XOWdrbWl2OUx5eWRraVVIWm02YjhQV2M3MWpLbk5ld1c5TG1rRGE5Sm1Td0dMWFQ0b2dMYVp2Wko5SmxEMGEtSDFJWldKXzFEV3hjOTNtQkVFeVRpSjEzOFE?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQSEEtMlFKdlpSZkhPeUpYMThkT2ZmZHVZYjhpOEc2QXJSbUN1dm9lRnhvUEpqb0psX2hGTUtQR0Fla0g5U051ZTBQS1VUS0wzdjNlNldhOXFPTmV6YjZoVXVMYlpJQUVpWDliZnh3WUxoeUVjYlBZdHU1eExFT3l3V0xna2NTbGQwT2t1Y2RlUzJLOWdQVGFyd0hreWt3M3VT?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxNU1NVb3ZzTC1qdVNoWUFfbXRCSG1sVG8tU0RpbXlsQmRhYjlPTWxHUldSZlRXNmdrZHY2NmE2YUZMTy02ZDNsRzNUbTFPOTBxdWJsQjU4WDltQzRtYmtRbFZValpGUGQ0V2h3MUVTN2JNcmdBY21XaV9PQi1KT2lXdi1TQ3pNZEptdHRrUEpaaFFPb0hIUnNWajdTaXBCV3JtSEFjLUE4eDBPRWJOZDFGbkVKTEdBMS1BT19nbnNWeFlxeC1MNzRzTmxDV2pSd3RwTXpzcVlyVlk3ZDk4ZWdNMG5B?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPY1U3di1QYW5mN3NoYXJWUUdqVHVDSHNOV3hnbTVNZE9zQmE5YjZSMXp0SW9BWjJORjNfakJibjZDa01zWmFzajZHUDdpc1U4UmJmeEpucTFrcnRsWGtOaE1DOGNTaEhzR0lrSFdkY3o2QTdlSTNBTWh2SWN4el9ZQ1Z1Ukg2a3dPNTVSdzVkZEc3RGdGRm5JdDdjSVRLVmNRQ1AtTHNHVUQ2ZlBGdlNCa0VfWTZhVEtjR0E?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxPYWh1UVdtSVlJRXVPckZzbjRqQU1kNnBiNzRxZ0NWVThQclFRV2VZM3I3VFBtcG1sN3VwdTdoOVBZZHV1YXlZUEZ3aEQ5WTlOdkpkTDJ0cVlCY0hmSlhXR3BGNFBEdFFabVBteHNUbXRWTF9Ha1NRUmZyRy1fZ1RFb2t4QWhEYVN6djZzQ3JZckNIeTh1SldRbnFJNzRjLUFvTlpPYnBUR0NaWjMtVEZxcFdzT0ViNjJ6ZFhvMVZQWlhsZkU?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxOX3VnN3lfRkVjaVdFejdqMU5FRTdWalgzeDlRa2FxVVJmVjgwTElnS3lZMVVMWl9vY29KSEpyX3FMQ0l6MXFwLUZRYm5WaGUwSk9kbzlKWEVMU3JwSjA1UDZzai1obVI2YkVMb0hDc2x2T3hvd1pLRFpOX3A5R3cwWE5IcG1ybmo2TmlZUktfRXU2aW5CM1hyRmstWkpTRU12bUd4bzRJRC1EeVZaWWhHTy1MMFZSdw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQOTdPWXF1LXZSeEZuUEp6VXo2dWF2VDBCN1E4aEZ4dXg1OURyTFZuSXM2MFFwa1I4MHoxbkRtQkRQTTU1TDQwQW5FYjl4RnpSOHVXZERfV2QyWllTVm45SEY4Sk9iN3JXUFBCOW9penZlNEdYRXVwc0pnVDhUYmhlVWd2WjdEY2UxN0FFRi1jUFJJYzlVcHl4QXJYdw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPSTBYOEhPRmxzaDFtY3Q0TDZwWWtnTHZNbF9JeWhabWt0NVllMHQ5ZTJQVDZYTkpzTHZ6Yi1iVkNiaGpmV0dlQXVIZlgxc2V4RnRUcHFRZDB2TldsTk5Lb1FONEZVRFN3ZmZaNERLall3LXM1VzVMd29BLXlCWXpvdTBHOGdoc0JWNm1Nb3E3SDdsTGlCUjNlVHhXc1AzWFk?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxOeHFlaXBvVWhiTmtvbkJleXlOQnVNNWladTcwdWtFbDF0MFJ3OENoZWxsRHpsZVNabVVyZzZOdHJDZUR4QmZCOVdicG5lOVdGcEVxR1FvRzRuMTZJMGZGdGpFMHRwWWpSVmVWa2o2Y0xmRjlwSGZtQWVWVmhYQW5lcVJwZ2ZCYVJ6aC1nNHVCbXQ?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxOTUdFQ3JuakFLZUxCSzVwSDIzRmcxR0lVX1V0Tks5eVdXNkRKM21EaWh5dXh6T2lzTnQtWkNjLThJTC1oeElFU2wyLXNGM3dzMGhGd2RULXQ2TEhkaUJVU284Wk9YeXNkdmJ2cDdsSHB5ZGd6VjBybXRkU1JiR0xOZE82ZVB0bVl5NzY5OUFjN2s4QQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
