# PEP Intelligence Report

- ticker: **PEP**
- Report as_of: **2026-10-30**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/PEP/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PEP/key-statistics/
- AI analysis snapshot as_of: **2026-10-30**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-31T02:02:31.570900+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 7, 'ai': 9, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261030T021807Z-b9de7146/PEP** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 9 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 31.82%; oldest publication 2026-10-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 137.3400 |
| Return 1D (%) | 2.6534 |
| Return 1W (%) | 1.1564 |
| Return 1M (%) | 8.3807 |
| Return YTD (%) | -1.3930 |
| Return 1Y (%) | -3.1481 |
| Annualized volatility (%) | 21.1557 |
| Beta vs SPY | -0.2426 |
| Max drawdown (%) | -25.2176 |
| Sharpe (rf=0) | -0.0467 |
| Downside deviation (rf=0, %) | 14.2689 |
| Sortino (rf=0) | -0.0693 |
| Historical VaR 95% (1D, %) | 2.0797 |
| Historical ES 95% (1D, %) | 2.6375 |
| Correlation vs SPY | -0.1467 |
| Tracking error vs SPY (%) | 26.2771 |
| P/E (trailing) | 17.28 |
| P/B | 8.40 |
| EV/EBITDA | 11.90 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 15.90 |
| Gross margin (%) | 54.33 |
| Operating margin (%) | 16.88 |
| Return on equity (%) | 52.19 |
| Free cash flow yield (%) | 4.83 |
| MA50 | 133.1945 |
| Close vs MA50 (%) | 3.1124 |
| MA200 | 143.7094 |
| Close vs MA200 (%) | -4.4322 |
| RSI (14, Wilder) | 61.3146 |
| MACD (12,26) | 1.1984 |
| MACD signal (9) | 0.5089 |
| MACD histogram | 0.6894 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PEP': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 137.3400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.6534 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.1564 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 8.3807 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -1.3930 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -3.1481 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.1557 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.2689 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.0693 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0797 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6375 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1467 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.2771 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.2426 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -25.2176 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.0467 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.8980 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3270 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.8830 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 52.1870 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.8324 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.2755 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 61.3146 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.6894 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.1124 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -4.4322 -> Slightly below the moving-average trend level.

## TAILWINDS

### PepsiCo (NASDAQ:PEP) Shares Climb 2.7% - Here's Why
- Summary: PepsiCo (NASDAQ:PEP) Shares Climb 2.7% - Here's Why
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPOF9pb0pjZzZCeXR3cVNsd0tjUVU5Ujl6QWh1LUpyOWVPSWR6TXJ0elhQdHpVZlIwTEZzNi1sRE5lNnZLMklncGl6YmFESWZKa3JnMzd3NFZqdzQyS0NVclc5YzFwX3B3U3Vqd0F4alBlNVJNN2hMdXhvODV1YjN6NVQ5NjhGNURiYm4wZnlqemo1N1Q4UlNSdEdKTm01QXBfTTZEYzN1WQ?oc=5>

### Should You Buy PepsiCo Stock For Its Cash?
- Summary: Examines PepsiCo's cash position as a factor for buying the stock.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxOT3JfOWJBTWttSmV5el9tckxzajNCVEMxNmNSNmZLZEdvSTNfcE5Td3RPd1RQdXZxSHAxSlBqZVlXSG0zNlFiQ1JPbGwzdWJzRTVlaFpWYnkyTnJjaGVKSmtwWkJHdmpkLVZ3SjhacHJDSVYwWWtNN1dFZVdQenN1S0dFM2c1YVJhNTR4VmYwcEdkd3lHSERKa3RqaGh0U19jaG13?oc=5>

### Is PepsiCo Stock Stronger Than It Looks?
- Summary: Questioning PepsiCo’s stock strength suggests potential undervaluation and future upside for investors.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQdGI1al9tWm5HV2dzcWcxOWtxbWg5Rm9rMlFSWldnZG9tb3Nib2VNZXAxa0RXVVlxcnp3am9DN1J6TmFYNzBVazVaUmh0cnAyZlJSVWRyNVhuVHhpaXJKVURfWGllQjVmZnhhM09OUkVVdTFHWDBfcmIxRUIwd0FKNTFiNV9fZ2VQU2NGcncyYnRCV2dsNTQyQ1E4RVI3UUxS?oc=5>

### Coca-Cola Yields Just 2.2% Compared to 4.3% for PepsiCo. Here's the Better Dividend King Stock for Generating Long-Term Passive Income.
- Summary: PepsiCo offers a higher dividend yield than Coca-Cola, positioning it as a more attractive income stock for long-term investors.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxON0NhSHRndFp3TWVQZlFmNWU2Yy13LThiTmd5OUdqRFllLTI1UXR0aEJBVVhXeVVmSDlTb0F4M19lR3prYVVvRHFpZGh0OXNGbk9Qc01FRWIybVJyTFhpMlJwa1YxUUpZQmVKSnl5ZG1lRTYwQUoyY0I0QTNMTG92Z3hndmFZbUZ3dGdiUnRCdlJ5Z1E?oc=5>

### PepsiCo vs. Coca-Cola: Which Beverage Titan Is the Better Bet?
- Summary: Compares PepsiCo and Coca-Cola to determine better investment choice.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQSklmSWRETGI3YmpGOVBmMERsUlJPNm5FVl9hekdmZkFjR1dXN2ZQQW5kYVpra204bzVWdFpBTVVRaTdsdHZTQ0ZfbU92bWg3b1V2V3BrbHZGUVBCLWdFYnE1YVh4X2dQUVpTRVJ4b1VDa0V3dllONV9DRlQyXzktQTNpelVrRjVSWmFwUjAzM3lNTENucGlmNWdR?oc=5>

### Unusual Options Volume Report: PepsiCo Stock
- Summary: Reports of higher-than-normal options trading activity for PepsiCo, indicating increased market interest.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPOUF0bmJkQ1VJZXZkeG5WRk9YUWllcDh1NERKc1JXTEZ0VG1RVkFmR21XN01KRGh5aTNKbjRJWnNqaVc0UndnbzNSZDR1M3ZQSFJtUG5DN1NEaHJQNGNtSFNuWVJFcUVmQXJfWjZ1NHZmcVM4X2t1c2EycGhCMFRlTlFfSDhla09YbV8tM3FmeVpjVDM2SG9kVC1yOTJtS0hPY2lHUUh3?oc=5>

### PepsiCo (PEP) Stock May Be Worth More On Its Supply Chain Reset
- Summary: Analysts suggest supply chain reset could boost PepsiCo’s valuation.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxNcWJTVndPbTdlcEFvZ1JyZmJPSUVpR1NKSGFOeHFiWUlzRXVGQTd6akxfbmQzUG54Q0VnR2pQVVVQRG5zODhIRHFrZEZsLXRMSGQzeF9DcUloRVBBUnJ5MlRaeEpRYnpQbmVUZl9BWjd2TkRiS1ZmVjFkd2h3NFNtUEVvQW1feGppS2JTZkUxZ2NNcTNhMVBHTi1TalpLVEVQQjZmOUFwSk1jRFoyV2pDaUhHLUpkNE5QUkIxSjNYbmwwRUNtbnNZUy1UMElTOExQX29XRtIB2gFBVV95cUxOaUR5dGVLRGxsbkJHS3dZNFV6T2tocE12Qk5LVUotTGR3WTFySWtJQm55SDV3ZXo0YUV1LThWNTY2V0ZiMm5rZGFuTms2WXFxb19kaVg2RHh6OEo5M3FtVmZqMmxGU296YnhjNmx0cEFWUV84cmpKLTY4dEVEMUFGbC1WRXZNbFg1LWlibzh2Unp3T2xLOE9sTlBQYlQtMm8xMi11UU1IRXh0bzNMb3psQ2VUMTZoQjkwN19IZkd5ZS1hZFFVa3lUbEtjWERIU21PODMtM21GVFNLZw?oc=5>

### PepsiCo's North America Reset: Can Cost Cuts Restore Growth?
- Summary: Cost-cutting plan in North America may revive growth prospects.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxQckpKSHpXZzJlZE9kVGUxdk1qbW5aY25LdVQzd2NFWnQySVpDRXZhQmZsRjNEd3hKby1za1lfY0FIb2dZRllIUlZHRHZBeGJJYktyZHRUV0k0SWhJWlhaei15RHNUMzBjd282cUVWMVZUTkw0NmJXT3RKM0xYZ0VjWGEySnRKUi1mbms4YXhQMXZMMW9ORFJ1eE9rR19USENtN1dLY3NNcl9hV0J6RFJ0MDlQT1o?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### PepsiCo (PEP) Stock Looks Below Fair Value After A Choppy Year
- Summary: PepsiCo (PEP) Stock Looks Below Fair Value After A Choppy Year
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNZzY1UzBpLS14VFl2UVBpU1FJYXJJRU9BaTNibm9OQkFQQ3g5NTZBWVNOUk9xRHV5dVptYmJYYnlwa0RpYUpuVGZvTmNqV09YcUpWSXk4YjNVNDFub0hQcXJRMGwweHJRSTR5eHBRam9uQmNXdHdLLVp6X0M2R2Zlb3k1UjlzRzl2YUt0VVJaeGtLUmhrYUJUaENB?oc=5>

### PepsiCo Hasn't Been This Cheap Relative to Earnings in 6 Years. Here's Why That's the Signal to Buy.
- Summary: PepsiCo Hasn't Been This Cheap Relative to Earnings in 6 Years. Here's Why That's the Signal to Buy.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPMklRamY4NTlwSXBhcnNLbjVrWjU0VnVPYTc3WG9NY1NianJJZVN4b2JRWmpHcktGYm5rVHJiU3h6dk9DTVhqLTVleEd3LTZqWmozQlQ2WWxsYkc3d2piTVVfel9VMF9qdjA3YmNveTdKRVlyOFc0TDk3cDMxSnZudEU3SzRKdG92UE16ZVNHYlUxTFB4N3Uw?oc=5>

### PepsiCo, Inc. $PEP Stock Bought by Soltis Investment Advisors LLC
- Summary: PepsiCo, Inc. $PEP Stock Bought by Soltis Investment Advisors LLC
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxPcjQ4TF92RzBmTUxSZTdpazlWUk9fLW03SEtmanRNRk9jMVZ0V1pPd09pMFFIOGpzZHdoSFhORmgtMUtiV1ZZQU9IZ1NpenRoZXZHQ2I0TzRNSEl0cHA4bXBHTGQyN0JnOWtERE1NRV8wU3RLS3k2RGRhdUNETU10QkNoeEN4VG1lOFZTZ3VCUjl1SVA5OGN0OTZvTjBRaHpEeTh2ZjZiQWZLQW8tZjU3ai1Ka2FCRlRRQWQxSElidXo?oc=5>

### PepsiCo, Inc. $PEP Stock Sold by Bokf Na
- Summary: PepsiCo, Inc. $PEP Stock Sold by Bokf Na
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPTWNzZmJUS09rb3l6WkNSQ0h0c3Jqd1F3X3pmUzVfRzJTOGhrd2g5c290Q2JZTW1JZDl3MFNCZFVoWE81LTRJZjEweUtYVjA0VnRDRDVXNVZCMm1OOEZqU2h3UFFHRkNTcERaejhldE9JTktPV3huZHpxVFRjSFpVWjlkNXN3WlI3SlExc1M4Z3A1RnV3cTRPS2d0b29iTUE?oc=5>

### PepsiCo Pays More, Coca-Cola Looks Stronger. Which Dividend Wins for Retirement?
- Summary: PepsiCo Pays More, Coca-Cola Looks Stronger. Which Dividend Wins for Retirement?
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPNHNDNXNfQjBkU0xrcWp5STBoc1l1VFJXelVOVVJqSkJtUXhKa1d3MkR6c1JqLTkwZEtDVFJ2RFVpamw4a09SXzF6VFJRM1JodFJlQl9ESzhUNV9WalJvc3FfeFctb3E1OUs1Y2FXcmNmMHVtbGFxeFN5MDVfcFozMFBrS213RF9lUkp0RUk4MVNOSGVNdlNlMUlOcVFnX3dHdUpOMldWek5ZeTZ0WVp1WW1PMm52cVAxY0lvNjNB?oc=5>

### PepsiCo Renews Partnership With Taco Bell for 11 More Years. Here’s What Investors Need to Know.
- Summary: PepsiCo Renews Partnership With Taco Bell for 11 More Years. Here’s What Investors Need to Know.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQbERnRTlldWdUY2NTMHVQWi1Xa0F4Yy1iVjFwTGhXZ2J6X3JYa2hWVHVVNWIySFczZmJUV1pZZ3pMWXV6eFJBaThiUlVUVGtoaHRZZGZIcFZlRVdRbFcxU2M4bThpTTRSdS1TTmVWaUNPUjVHd3FhUVNBb1BJaVZ1OE9ScVVxUUg1S1l5aUJxTzdibGlqSnc4djlkNXpLeUF0bmZN?oc=5>

### PepsiCo (PEP) Renews Taco Bell Deal, Is The Stock A Bargain?
- Summary: PepsiCo renews its partnership with Taco Bell, extending the franchise agreement and potentially boosting revenue streams.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNWGNGNndxNnhNR0NTQ2Fod2UtaTFnWXFpTm01ZUtMU1UtYnBRZk9BU0FDUWR0N3cwbjY0ZTMwMDUwNGZZYndVTnFhcHN0QzBSUTdlWndZQ1VQTDEwZ0E1N1ZYWDRSMWN6QjNRdjRsd1RBZC11MEc1bmhCYTZrcFR0cjFaVDBVTnc1dmcxR2JlMFdlbXBsSlNBNA?oc=5>

### PepsiCo (NASDAQ:PEP) Share Price Crosses Above 50-Day Moving Average - Here's What Happened
- Summary: PepsiCo shares surpassed the 50‑day moving average, indicating a short‑term bullish trend.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxOTXJaRDY5NS1UOWZEVTV6bGpXX0Z2Xzg0RDFxRHh4VHFxaWg4TElreHhaUE9MTzUyX2I5NkVYcWgtZm4yN3pVLUFza19vSUxoZ3FXaEVKeFVFTTltT0lCczlZX3VoLVlUYjJweENxWXUxR2hHV0xQSlQ5eUthZlhXNnFNVXVCcHl5bFlscXZMdUhtVmp3OUZ0NjRtN1dLNEhpek9Bc3ctZG1JN2hlRmU4UlVSYk8wVk42eGtFVzNpQ3pQZl9hcmk3d0NGRnlOVGs3cjRfY1VBYVVIMXp2aW9B?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PEP** | **17.28** | **8.40** | **11.90** | **5.60** | **187,158,855,680.00 USD** | **-3.15** |
| KO | 27.75 | 10.83 | 24.81 | 7.40 | 404,722,974,720.00 USD | 40.01 |
| MNST | 43.83 | 9.90 | 30.48 | 20.20 | 92,741,509,120.00 USD | 42.23 |
| KDP | 36.20 | 1.95 | 18.60 | 75.60 | 48,772,001,792.00 USD | 33.60 |

Peers fetched as_of: 2026-10-30; PEP reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-08
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

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
- Filing date: 2026-10-08
- Revenue (latest available single quarter): 25,274,000,000.00 USD; period 2026-06-14/2026-09-05; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,048,000,000.00 USD; period 2026-06-14/2026-09-05; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/77476/000007747626000048/pep-20260905.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMipwFBVV95cUxPOF9pb0pjZzZCeXR3cVNsd0tjUVU5Ujl6QWh1LUpyOWVPSWR6TXJ0elhQdHpVZlIwTEZzNi1sRE5lNnZLMklncGl6YmFESWZKa3JnMzd3NFZqdzQyS0NVclc5YzFwX3B3U3Vqd0F4alBlNVJNN2hMdXhvODV1YjN6NVQ5NjhGNURiYm4wZnlqemo1N1Q4UlNSdEdKTm01QXBfTTZEYzN1WQ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxOT3JfOWJBTWttSmV5el9tckxzajNCVEMxNmNSNmZLZEdvSTNfcE5Td3RPd1RQdXZxSHAxSlBqZVlXSG0zNlFiQ1JPbGwzdWJzRTVlaFpWYnkyTnJjaGVKSmtwWkJHdmpkLVZ3SjhacHJDSVYwWWtNN1dFZVdQenN1S0dFM2c1YVJhNTR4VmYwcEdkd3lHSERKa3RqaGh0U19jaG13?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQdGI1al9tWm5HV2dzcWcxOWtxbWg5Rm9rMlFSWldnZG9tb3Nib2VNZXAxa0RXVVlxcnp3am9DN1J6TmFYNzBVazVaUmh0cnAyZlJSVWRyNVhuVHhpaXJKVURfWGllQjVmZnhhM09OUkVVdTFHWDBfcmIxRUIwd0FKNTFiNV9fZ2VQU2NGcncyYnRCV2dsNTQyQ1E4RVI3UUxS?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxON0NhSHRndFp3TWVQZlFmNWU2Yy13LThiTmd5OUdqRFllLTI1UXR0aEJBVVhXeVVmSDlTb0F4M19lR3prYVVvRHFpZGh0OXNGbk9Qc01FRWIybVJyTFhpMlJwa1YxUUpZQmVKSnl5ZG1lRTYwQUoyY0I0QTNMTG92Z3hndmFZbUZ3dGdiUnRCdlJ5Z1E?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQSklmSWRETGI3YmpGOVBmMERsUlJPNm5FVl9hekdmZkFjR1dXN2ZQQW5kYVpra204bzVWdFpBTVVRaTdsdHZTQ0ZfbU92bWg3b1V2V3BrbHZGUVBCLWdFYnE1YVh4X2dQUVpTRVJ4b1VDa0V3dllONV9DRlQyXzktQTNpelVrRjVSWmFwUjAzM3lNTENucGlmNWdR?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPOUF0bmJkQ1VJZXZkeG5WRk9YUWllcDh1NERKc1JXTEZ0VG1RVkFmR21XN01KRGh5aTNKbjRJWnNqaVc0UndnbzNSZDR1M3ZQSFJtUG5DN1NEaHJQNGNtSFNuWVJFcUVmQXJfWjZ1NHZmcVM4X2t1c2EycGhCMFRlTlFfSDhla09YbV8tM3FmeVpjVDM2SG9kVC1yOTJtS0hPY2lHUUh3?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxNcWJTVndPbTdlcEFvZ1JyZmJPSUVpR1NKSGFOeHFiWUlzRXVGQTd6akxfbmQzUG54Q0VnR2pQVVVQRG5zODhIRHFrZEZsLXRMSGQzeF9DcUloRVBBUnJ5MlRaeEpRYnpQbmVUZl9BWjd2TkRiS1ZmVjFkd2h3NFNtUEVvQW1feGppS2JTZkUxZ2NNcTNhMVBHTi1TalpLVEVQQjZmOUFwSk1jRFoyV2pDaUhHLUpkNE5QUkIxSjNYbmwwRUNtbnNZUy1UMElTOExQX29XRtIB2gFBVV95cUxOaUR5dGVLRGxsbkJHS3dZNFV6T2tocE12Qk5LVUotTGR3WTFySWtJQm55SDV3ZXo0YUV1LThWNTY2V0ZiMm5rZGFuTms2WXFxb19kaVg2RHh6OEo5M3FtVmZqMmxGU296YnhjNmx0cEFWUV84cmpKLTY4dEVEMUFGbC1WRXZNbFg1LWlibzh2Unp3T2xLOE9sTlBQYlQtMm8xMi11UU1IRXh0bzNMb3psQ2VUMTZoQjkwN19IZkd5ZS1hZFFVa3lUbEtjWERIU21PODMtM21GVFNLZw?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxQckpKSHpXZzJlZE9kVGUxdk1qbW5aY25LdVQzd2NFWnQySVpDRXZhQmZsRjNEd3hKby1za1lfY0FIb2dZRllIUlZHRHZBeGJJYktyZHRUV0k0SWhJWlhaei15RHNUMzBjd282cUVWMVZUTkw0NmJXT3RKM0xYZ0VjWGEySnRKUi1mbms4YXhQMXZMMW9ORFJ1eE9rR19USENtN1dLY3NNcl9hV0J6RFJ0MDlQT1o?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNZzY1UzBpLS14VFl2UVBpU1FJYXJJRU9BaTNibm9OQkFQQ3g5NTZBWVNOUk9xRHV5dVptYmJYYnlwa0RpYUpuVGZvTmNqV09YcUpWSXk4YjNVNDFub0hQcXJRMGwweHJRSTR5eHBRam9uQmNXdHdLLVp6X0M2R2Zlb3k1UjlzRzl2YUt0VVJaeGtLUmhrYUJUaENB?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPMklRamY4NTlwSXBhcnNLbjVrWjU0VnVPYTc3WG9NY1NianJJZVN4b2JRWmpHcktGYm5rVHJiU3h6dk9DTVhqLTVleEd3LTZqWmozQlQ2WWxsYkc3d2piTVVfel9VMF9qdjA3YmNveTdKRVlyOFc0TDk3cDMxSnZudEU3SzRKdG92UE16ZVNHYlUxTFB4N3Uw?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxPcjQ4TF92RzBmTUxSZTdpazlWUk9fLW03SEtmanRNRk9jMVZ0V1pPd09pMFFIOGpzZHdoSFhORmgtMUtiV1ZZQU9IZ1NpenRoZXZHQ2I0TzRNSEl0cHA4bXBHTGQyN0JnOWtERE1NRV8wU3RLS3k2RGRhdUNETU10QkNoeEN4VG1lOFZTZ3VCUjl1SVA5OGN0OTZvTjBRaHpEeTh2ZjZiQWZLQW8tZjU3ai1Ka2FCRlRRQWQxSElidXo?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPTWNzZmJUS09rb3l6WkNSQ0h0c3Jqd1F3X3pmUzVfRzJTOGhrd2g5c290Q2JZTW1JZDl3MFNCZFVoWE81LTRJZjEweUtYVjA0VnRDRDVXNVZCMm1OOEZqU2h3UFFHRkNTcERaejhldE9JTktPV3huZHpxVFRjSFpVWjlkNXN3WlI3SlExc1M4Z3A1RnV3cTRPS2d0b29iTUE?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPNHNDNXNfQjBkU0xrcWp5STBoc1l1VFJXelVOVVJqSkJtUXhKa1d3MkR6c1JqLTkwZEtDVFJ2RFVpamw4a09SXzF6VFJRM1JodFJlQl9ESzhUNV9WalJvc3FfeFctb3E1OUs1Y2FXcmNmMHVtbGFxeFN5MDVfcFozMFBrS213RF9lUkp0RUk4MVNOSGVNdlNlMUlOcVFnX3dHdUpOMldWek5ZeTZ0WVp1WW1PMm52cVAxY0lvNjNB?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQbERnRTlldWdUY2NTMHVQWi1Xa0F4Yy1iVjFwTGhXZ2J6X3JYa2hWVHVVNWIySFczZmJUV1pZZ3pMWXV6eFJBaThiUlVUVGtoaHRZZGZIcFZlRVdRbFcxU2M4bThpTTRSdS1TTmVWaUNPUjVHd3FhUVNBb1BJaVZ1OE9ScVVxUUg1S1l5aUJxTzdibGlqSnc4djlkNXpLeUF0bmZN?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNWGNGNndxNnhNR0NTQ2Fod2UtaTFnWXFpTm01ZUtMU1UtYnBRZk9BU0FDUWR0N3cwbjY0ZTMwMDUwNGZZYndVTnFhcHN0QzBSUTdlWndZQ1VQTDEwZ0E1N1ZYWDRSMWN6QjNRdjRsd1RBZC11MEc1bmhCYTZrcFR0cjFaVDBVTnc1dmcxR2JlMFdlbXBsSlNBNA?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxOTXJaRDY5NS1UOWZEVTV6bGpXX0Z2Xzg0RDFxRHh4VHFxaWg4TElreHhaUE9MTzUyX2I5NkVYcWgtZm4yN3pVLUFza19vSUxoZ3FXaEVKeFVFTTltT0lCczlZX3VoLVlUYjJweENxWXUxR2hHV0xQSlQ5eUthZlhXNnFNVXVCcHl5bFlscXZMdUhtVmp3OUZ0NjRtN1dLNEhpek9Bc3ctZG1JN2hlRmU4UlVSYk8wVk42eGtFVzNpQ3pQZl9hcmk3d0NGRnlOVGs3cjRfY1VBYVVIMXp2aW9B?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
