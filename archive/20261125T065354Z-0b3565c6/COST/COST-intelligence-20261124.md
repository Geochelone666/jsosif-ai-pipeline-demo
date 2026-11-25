# COST Intelligence Report

- ticker: **COST**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/COST/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/COST/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:07:09.096614+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 21, 'rule': 7, 'ai': 11, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/COST** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 21 unique headlines; 10 named publishers; 4 exact duplicates; 21 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1091.7100 |
| Return 1D (%) | 2.2286 |
| Return 1W (%) | 1.1079 |
| Return 1M (%) | 12.0318 |
| Return YTD (%) | 30.9226 |
| Return 1Y (%) | 27.4092 |
| Annualized volatility (%) | 20.3643 |
| Beta vs SPY | -0.1627 |
| Max drawdown (%) | -18.1993 |
| Sharpe (rf=0) | 1.2963 |
| Downside deviation (rf=0, %) | 13.5854 |
| Sortino (rf=0) | 1.9431 |
| Historical VaR 95% (1D, %) | 2.0802 |
| Historical ES 95% (1D, %) | 2.7374 |
| Correlation vs SPY | -0.1195 |
| Tracking error vs SPY (%) | 26.6665 |
| P/E (trailing) | 52.59 |
| P/B | 13.52 |
| EV/EBITDA | 33.32 |
| Revenue growth (%) | 11.10 |
| Forward P/E (estimate) | 43.59 |
| Gross margin (%) | 12.77 |
| Operating margin (%) | 3.80 |
| Return on equity (%) | 28.40 |
| Free cash flow yield (%) | 1.40 |
| MA50 | 966.6799 |
| Close vs MA50 (%) | 12.9340 |
| MA200 | 950.8039 |
| Close vs MA200 (%) | 14.8197 |
| RSI (14, Wilder) | 72.6449 |
| MACD (12,26) | 32.6003 |
| MACD signal (9) | 32.6938 |
| MACD histogram | -0.0934 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'COST': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1091.7100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.2286 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.1079 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 12.0318 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 30.9226 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 27.4092 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 20.3643 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.5854 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.9431 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0802 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.7374 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1195 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.6665 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1627 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -18.1993 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.2963 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 43.5926 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 12.7660 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 3.7970 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 28.4020 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.3959 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 52.5872 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 72.6449 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0934 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 12.9340 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 14.8197 -> Clearly above the moving-average trend level.

## TAILWINDS

### Costco Shares Lift Higher on Sales, Warehouse Growth
- Summary: Costco Shares Lift Higher on Sales, Warehouse Growth
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPcE00SUE2SWxUeTFOVEpXVFF4YXFiVTJpNXl0ZVU2TXU2MUZHTEF2ZXhPWkRUdVlsT0dCTkh4RUdvMlpQZlRRR1dERGo4VTFKZ2ZqS3Y0eC05aVlxR0plS1hHYUVDdnR0TWN6NFJLeW81WmF6Wkh4R1dXcWRFcEVSME1DRGVSMmFmcVpqTkZxOXlRSDhNUzBMWjlaWHlsdVZ6aUFFSA?oc=5>

### Costco Stands to Benefit as Shoppers Rush to Stock Up Amid Multiple Tech Outages
- Summary: Costco Stands to Benefit as Shoppers Rush to Stock Up Amid Multiple Tech Outages
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPNWxuVkllUkNyek80TGxaYTJfMTk1VnJwbFY1YzdILXF6ODkwQWptNkwzeTM1QkdrS1liSGdySlpmVDFJVW51U2J3UnVVRDVpbUZjQzlNeWk5V1dpNDBWRmlGc0xYRFB2VlVpYk9QdGNJVlh3dVVzUUJMcVhBTlNWTUdOVkJ3ZlUxOV9ucThsMzFoTXItbXNZek1zSHBpSUk5dU9YdjI0WlhUYnBjVmtRV0NpU0NEMGJRQWpMT3JnZ2s1Zw?oc=5>

### Will Costco stock drop on November 24? About $30 comes off the price as the dividend goes ex
- Summary: Ex-dividend date may affect stock price; dividend payout expected.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPeWkwTHlnNzNnZEZ4Yk0wZWhQdEFnM0NmY0kzaV9WS202WFFDNTc2XzM0anc3ZnI3eGZIYkRnUE1SaUVMTUltXzVMenktenNXZXZmbGJnYnFablJMM1Q2SXctM0oyTGQ3MmNYX2E0UzltYjlTX18xTzdZdHFMLW9GalJfR05PdjJJU0g4eE4wYklGUGlnSDRVWkVyaXd3ZVR4bTdKR0phOG1SVVFteW1z?oc=5>

### Walmart, Costco see some panic-buying after tech outages
- Summary: Panic-buying post-outages boosts Costco sales, indicating short-term demand spike.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxOTHh0Qnd1ZUs1di12Tjd5LXVVR1lTc3pWWVlnVTlDbWZ3Q25id2YxMFhndk9nQzdNNDVvQkdobXlBY0xZd1Y1QmUyTVlmWGo0VHY2VTNaMHBnek5vdU5JZWdaTlZpckpUWnNydUVnMnlCMENKbXIyMkxqaGhpcDNRT0ZXQnBZTUNjNDJXVUlGSEFxT20xQU1KSVpzQlB4b1QzOTJRbmFub2NrZjRxTWdRU2pn?oc=5>

## HEADWINDS

### Costco share price slips while investors weigh effects of special dividend on capital return sentiment
- Summary: Costco share price slips while investors weigh effects of special dividend on capital return sentiment
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNZDE3eXY3WWJseGp6UEZfM3E5ZEhvX2ZfaVZJVEtQNFVQTzV3UDkyaGNGWWNPV2dsU1B3S00wWm5WSjZvdTFwbEZpQTNEU1l2YllSWmowZF80QTN3WkxpUTNyUnkxdlVOQk9PdmI3S09ERWxrVkVlS3o4OUdWUXU3TU5pb2ZFaG5pVS1Z?oc=5>

### Costco (COST) Stock Could Be Above Fair Value Despite Its Record $30 Dividend
- Summary: Potential overvaluation despite high dividend, may deter investors.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQbVVVRktRbjFCOXBrT2EtQ0JQbzhVVWdHTzh1eGpEakpTZEVxanEwYmVnc3ROT0Z6eG1SeEhDb25fQlE3RHFfUEhfQ0YtREc5Z1k0RFZJQ3l5M2RIZTN3VjNBdnpDdk15NFJwWW1wZ1lyZ2prbjZJZkdsQkhvXzNVNGhnMnBOR0xyZFl5QktCelZsWmx4NkNoWmJn?oc=5>

### Costco (COST) Declines More Than Market: Some Information for Investors
- Summary: Stock underperforms market, raising concerns about valuation.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQX1J1VDdwdDR4V3JnNzlkdXEtZ0JhZTl2OUxvQ0hhd25jR1ZyUzdxb3EwU0taVVhFOXc1a0NuaENOa1BRQWdKNk41Wk52MTliQ0lqYV9EczR0bDFfWXNtcUwyUnc5bHF5Sm9XYW91cUtQQ0twenNKdnB1VnBmcm5DdFB1SUNNNGQ0Q0F3bThZRVl5a2VFdGhkV2NndXpqZw?oc=5>

## CATALYSTS

### Costco Just Announced a Special Dividend for Shareholders as of Nov. 24. Should You Buy Shares Before Then?
- Summary: Costco Just Announced a Special Dividend for Shareholders as of Nov. 24. Should You Buy Shares Before Then?
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxNRGpzcm0tOTcwalVOcjk3RGk2dEpHbGN6Wl80NGc5SFpXeC1WbFBhUWRpVkxVSHN6NXNjYlQyQ0ZMWWRJVFR4emowWXAzSHdmcWVicEdBQmY0VXJVLTN4ZnAwaFlnMnVJN1c3V212c3ZhOUZoekszdFk4U1RodW96Ri1ROGJ1NUdZaVVUUlJwcDBMeUZ2elhfT2xlZDduaWtIZS1xWks0Z1dtbGdFdThOLUdfdmRNUWRUdmNKZDRsTmhENFRkLVZSYll5ckxXbnVxV0p0WVk2S2piZw?oc=5>

### Costco’s Upcoming $30 Special Dividend Is Twice the Size of Its Last Special Payout. Is This the Most Unstoppable Consumer Staples Stock to Buy Now?
- Summary: Costco’s Upcoming $30 Special Dividend Is Twice the Size of Its Last Special Payout. Is This the Most Unstoppable Consumer Staples Stock to Buy Now?
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNV21SOWVkZ2hMQTZwVS1FQXdVamRfblB5bzFubzJZVWpINVUzTjFfRWhReWxfbGdSZlQ1MWwwdWRjSVVMX0h6b2ZsU1N5TDB4LV9xQUNVN05FUmZieXFiaU9WOW1NV1lPSEZVYnBYbjZxdEpoV1JMUzB0VmhpMmdtdzhESnE0b1NXVXltbjRETG9iRFEyRklfOGIyNzlSWk1mZ0E?oc=5>

### Costco Just Made a New All-Time High After Announcing a $30-Per-Share Special Dividend. Is the Stock a Buy Before Dec. 10?
- Summary: Costco Just Made a New All-Time High After Announcing a $30-Per-Share Special Dividend. Is the Stock a Buy Before Dec. 10?
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi8wFBVV95cUxPQzVMek80dzBCRjUybkRtSG1WUzMyQzF0N2xLcmYxQ3ZQMGxIS2plYmVVeC1OWVJZNFVOU05jRTREc1ZIVlRDenI2UWxqeS1nU29tdWYxZ3hBSHVJTFRnSTZvY0t3V240NVB1YnNLc3htLVg3Y2oyTkZIcW1Ya1lxRzBMd1JGbTFPMWFOQkVOeGlLaTJXdjl2cndPeFhzTXVQZGVTNHZCOTZjOVZzcGtDWjQwOGw2clJFZXpobThNaXNPVzhHSmVGNkJwUXZZYXdCZ3RpeWxJN29EeE51VzJCSGJmeWUxdGRsQlpEdW1xT01qTXM?oc=5>

### Costco Just Surpassed $1,100 Per Share Ahead of Its $30 Special Dividend Payment. Is the Stock a Buy Before Nov. 24?.
- Summary: Costco Just Surpassed $1,100 Per Share Ahead of Its $30 Special Dividend Payment. Is the Stock a Buy Before Nov. 24?.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6AFBVV95cUxOdF9FWDEyVWh1ejBmQTV3aW50SGQtX1NjTHlQTEJHZlFPN1Q1SGRhMlpQRHoxNmVHdUFyaVBPTDdxOXcxVUZ0ZTRvQjlZZ2c1bWlSVmQ0OEVSbWtqdzdtZFRYRzBNTVBJQjNmclJicmk3M2FxTnRyRjVxNW1uM2MtV0pGc3R3bGVHbFlZOFNkT2N5d1QzdTZYTUZFUURlSEJueGRQZ2t3dTYtdkxTVkNkYjllMW9oNVJuNnp1aUJGbGJxRno5c05FdGFuNXJTdlhmSWp6UVdHZHpzN25vbGxLTkVBMjZpSjUy?oc=5>

### Costco’s U.S. Comparable Sales Jumped 12.6% in October. Here’s the Number That Shows Its Moat Is Widening.
- Summary: Costco’s U.S. comparable sales rose 12.6% in October, indicating a widening moat and strong demand.
- Date: 2026-11-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNVU51MDJmTFk1TGZFN24wSF82QTNmZFBJR3NQdnJMdTNYYzR6Q3hLenNhRVpLY25BT3lGYmtsUFNreXA2a3oxd3BCWE5tNmNka0xaNW5DdDU5MzdlczBBVk1rUDUwdTVBTUtsTVlGT05qVUJuc2FZczJPOTlWSWdZMS1PVlpjNjMzNFRHVzdCelZYXzNoZElUZ3pYNEN6WjctU2pYeXJ3QXVRc181QzlhejBTckNJNy12RExabkRPUWhhSmNqOXVr?oc=5>

### Here’s How Many Shares of Costco You’d Need for $5,000 in Yearly Dividends.
- Summary: Calculates shares needed for $5,000 annual dividends.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNMVFxTHpyUHFWY3hXWkRGSHNldUlWUU9QcnZrRnFHUDd3U1dZZk0zbkUyNHRPb256NFRWZlU2d1pCandOMkpUeUFqc2dTNEg1Z0EyVHp4b19sMVY0enpXWFlYX2h4WWxVblhHWjR5amNaWktDUjZmOGlMUEZUVXNhcnFlbDZqNFY1NmlGNWVpNGs?oc=5>

### Why is Costco Wholesale stock climbing today?
- Summary: Explains factors behind today's price rise.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQZFBLVEpPdDJ6ZlhBczUydzZvUWFaMVctWVJLN29tS1BBRHY3T1BrblNZUVRPcEhtUTBpT3pfOE5sSENSbmsyQWZ4TlVkU0V1dHhUcVR4bzNUVXZCaWJkTV9jb2s3MDRGZGdkcTZGUkxoYkdEWmhUQU5MQm5ybHdQZTBZSUliV2xQblhNOC14eUJ1NXh6NUI5MTRlS2lIeld1T0hRdUUxYjhZdw?oc=5>

### What Happens To Costco Stock If Its Cash Pile Runs Down?
- Summary: Analyzes potential price impact of cash depletion.
- Date: 2026-11-24 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxQdE44SDRNZ19hUGp2ckZ5VjJwTGZkOHVSR203WGZwUFhLWUp5ZVQ0NzBSc3EzWTQtVU9vLTFoLTN1ajJrTE91MkkwYXNjQmpvM3ZGNTlnX1J5Q2d2TGp4RU5sdVl0SklxV0pzOW9SRmkwN2dzUUZENnhqYVVieWJNX1Fib2owOUF1S0NSRl9SWmo1RVE1QUtSNlhxcWRTaXJENVQ4RW5UUk9GUzNKbG5GbzNMTGNEVlk?oc=5>

### Costco Wholesale Corporation (COST) Is a Trending Stock: Facts to Know Before Betting on It
- Summary: Provides general info for potential investors.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxNRnYzc2pVVUVaSEd0ek5wY3duY2EtbXJ6enE3SnhkZ0tJclNVUGZaekpxWXZnR2NIVkNCUW5RN003MV9hMDhFYUxXeVlYZTJlNlpMbVpLTVM1Z1ZCOTNqNEF0YXNuajQwLVN2SVdhQTlScUVvREVPVmxPTWVUYnBrYXc4OUpsOFBZdXlyZzJxaTlnUUpDQl9oTm13NC1WdVJ5T1RGd0J6dktjeHM?oc=5>

### Costco Wholesale (COST) Could Be 27% Overvalued After Its $30 Special Dividend
- Summary: Highlights overvaluation risk post-special dividend.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPekNEZ3lzY0RJTDRta3FyTm9lajJXSnl6eUNDZlo2YzNxbGc4ckV4Ymt3U1c2b0gxVUh2VTBMaThLaHZGdU1FbHVubG1Kb19Gd0lvN3U2b2VoUnFxdnphTjViandrNEQ5T01JZTRKeXlMSjZCNGNFRkRxdGZ5SURReWlwRkJTNVZlSlpCU0cwR3U5V2c5WlhNSDdGQQ?oc=5>

### Will Costco Do a Stock Split Before the End of 2026?
- Summary: Costco may consider a stock split before 2026, potentially affecting share price and liquidity.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQV0pUNHJId1ZCM3J1V0xMcmdOZGh2bFFKOHBXQTJnbThrN0xkbFZ4WFgzZ0NITU9mVi1aM1IxYlRRLTBtUWhkOVZadkJ1NGhXWk41c2UwLW9pY1g2TXNmYUxlbjlQM3VqdWRveW5jRG5KRWVhLTJxdk0yVy1TVHpGZ0ZId2tmNkgxZ1JnTGtrR1VrYnhGZ3Zhemd3?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **COST** | **52.59** | **13.52** | **33.32** | **11.10** | **483,768,729,600.00 USD** | **27.41** |
| WMT | 47.94 | 10.70 | 23.08 | 5.20 | 1,052,933,423,104.00 USD | 28.22 |
| TGT | 16.36 | 4.34 | 10.59 | 7.10 | 79,708,454,912.00 USD | 115.50 |
| BJ | 22.77 | 5.99 | 15.34 | 17.50 | 13,146,832,896.00 USD | 18.31 |

Peers fetched as_of: 2026-11-24; COST reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-24
- Next expected earnings: 2026-12-10 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-07
- Revenue (latest available single quarter): 69,597,000,000.00 USD; period 2025-11-24/2026-02-15; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 2,192,000,000.00 USD; period 2026-02-16/2026-05-10; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMipAFBVV95cUxPcE00SUE2SWxUeTFOVEpXVFF4YXFiVTJpNXl0ZVU2TXU2MUZHTEF2ZXhPWkRUdVlsT0dCTkh4RUdvMlpQZlRRR1dERGo4VTFKZ2ZqS3Y0eC05aVlxR0plS1hHYUVDdnR0TWN6NFJLeW81WmF6Wkh4R1dXcWRFcEVSME1DRGVSMmFmcVpqTkZxOXlRSDhNUzBMWjlaWHlsdVZ6aUFFSA?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPNWxuVkllUkNyek80TGxaYTJfMTk1VnJwbFY1YzdILXF6ODkwQWptNkwzeTM1QkdrS1liSGdySlpmVDFJVW51U2J3UnVVRDVpbUZjQzlNeWk5V1dpNDBWRmlGc0xYRFB2VlVpYk9QdGNJVlh3dVVzUUJMcVhBTlNWTUdOVkJ3ZlUxOV9ucThsMzFoTXItbXNZek1zSHBpSUk5dU9YdjI0WlhUYnBjVmtRV0NpU0NEMGJRQWpMT3JnZ2s1Zw?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPeWkwTHlnNzNnZEZ4Yk0wZWhQdEFnM0NmY0kzaV9WS202WFFDNTc2XzM0anc3ZnI3eGZIYkRnUE1SaUVMTUltXzVMenktenNXZXZmbGJnYnFablJMM1Q2SXctM0oyTGQ3MmNYX2E0UzltYjlTX18xTzdZdHFMLW9GalJfR05PdjJJU0g4eE4wYklGUGlnSDRVWkVyaXd3ZVR4bTdKR0phOG1SVVFteW1z?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxOTHh0Qnd1ZUs1di12Tjd5LXVVR1lTc3pWWVlnVTlDbWZ3Q25id2YxMFhndk9nQzdNNDVvQkdobXlBY0xZd1Y1QmUyTVlmWGo0VHY2VTNaMHBnek5vdU5JZWdaTlZpckpUWnNydUVnMnlCMENKbXIyMkxqaGhpcDNRT0ZXQnBZTUNjNDJXVUlGSEFxT20xQU1KSVpzQlB4b1QzOTJRbmFub2NrZjRxTWdRU2pn?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNZDE3eXY3WWJseGp6UEZfM3E5ZEhvX2ZfaVZJVEtQNFVQTzV3UDkyaGNGWWNPV2dsU1B3S00wWm5WSjZvdTFwbEZpQTNEU1l2YllSWmowZF80QTN3WkxpUTNyUnkxdlVOQk9PdmI3S09ERWxrVkVlS3o4OUdWUXU3TU5pb2ZFaG5pVS1Z?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQbVVVRktRbjFCOXBrT2EtQ0JQbzhVVWdHTzh1eGpEakpTZEVxanEwYmVnc3ROT0Z6eG1SeEhDb25fQlE3RHFfUEhfQ0YtREc5Z1k0RFZJQ3l5M2RIZTN3VjNBdnpDdk15NFJwWW1wZ1lyZ2prbjZJZkdsQkhvXzNVNGhnMnBOR0xyZFl5QktCelZsWmx4NkNoWmJn?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQX1J1VDdwdDR4V3JnNzlkdXEtZ0JhZTl2OUxvQ0hhd25jR1ZyUzdxb3EwU0taVVhFOXc1a0NuaENOa1BRQWdKNk41Wk52MTliQ0lqYV9EczR0bDFfWXNtcUwyUnc5bHF5Sm9XYW91cUtQQ0twenNKdnB1VnBmcm5DdFB1SUNNNGQ0Q0F3bThZRVl5a2VFdGhkV2NndXpqZw?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxNRGpzcm0tOTcwalVOcjk3RGk2dEpHbGN6Wl80NGc5SFpXeC1WbFBhUWRpVkxVSHN6NXNjYlQyQ0ZMWWRJVFR4emowWXAzSHdmcWVicEdBQmY0VXJVLTN4ZnAwaFlnMnVJN1c3V212c3ZhOUZoekszdFk4U1RodW96Ri1ROGJ1NUdZaVVUUlJwcDBMeUZ2elhfT2xlZDduaWtIZS1xWks0Z1dtbGdFdThOLUdfdmRNUWRUdmNKZDRsTmhENFRkLVZSYll5ckxXbnVxV0p0WVk2S2piZw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNdUxmSnFReXZQNjJzU3JZMk15V3BCai1oVzFRWklmRjZ0ZWVBQ3lvQVVXMlVHYm9Nc094T0psX2JMc2R3ZDUwdVk3RTljOEc3MjZINzlsWVdZYUJ6UHVyd3NWNThxQi15dndWMzJPcGNJcXo5cHFZelNHQlEyRnI5LWdWTFFBMUROYkl1MzJhTkgxX3lUeUE2WGxKMUJQYktRdElGTTJR?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNV21SOWVkZ2hMQTZwVS1FQXdVamRfblB5bzFubzJZVWpINVUzTjFfRWhReWxfbGdSZlQ1MWwwdWRjSVVMX0h6b2ZsU1N5TDB4LV9xQUNVN05FUmZieXFiaU9WOW1NV1lPSEZVYnBYbjZxdEpoV1JMUzB0VmhpMmdtdzhESnE0b1NXVXltbjRETG9iRFEyRklfOGIyNzlSWk1mZ0E?oc=5
- https://news.google.com/rss/articles/CBMimwJBVV95cUxPekN6R0w0bHNncHBsRk9RZWNtTnVjci1BMUUwWGlyTTBZc25xT1cybE5sb0xRa2dJdUZfbG5jWE01MlFrWmc4RTJ2cnMtLVpYb2E5Wl85b2toeHRCYWdyTXFaVjZiZ1duMjlvUFRQZ0tzY0dRd1BtZmR1TnZJQ25faGFoTGt2LWxUQ0xSUEZwRWVhdTNWdjFnLTh3RV8yR0dyajV5N3VyNWI1N2VraG85QXZPQlB0eDNPeHJBNTVJeHN4endjeWRuTkFTNVRXRTduUUV5STJOLUVXbGlpM1ZIOEFKR05rZ092eWc1Rm5OeHJXNXliZjdIeEJuelBZNDE4TGFJSHo2eTB2d0NjY2Jjem1DcExjdmZlUllF?oc=5
- https://news.google.com/rss/articles/CBMi8wFBVV95cUxPQzVMek80dzBCRjUybkRtSG1WUzMyQzF0N2xLcmYxQ3ZQMGxIS2plYmVVeC1OWVJZNFVOU05jRTREc1ZIVlRDenI2UWxqeS1nU29tdWYxZ3hBSHVJTFRnSTZvY0t3V240NVB1YnNLc3htLVg3Y2oyTkZIcW1Ya1lxRzBMd1JGbTFPMWFOQkVOeGlLaTJXdjl2cndPeFhzTXVQZGVTNHZCOTZjOVZzcGtDWjQwOGw2clJFZXpobThNaXNPVzhHSmVGNkJwUXZZYXdCZ3RpeWxJN29EeE51VzJCSGJmeWUxdGRsQlpEdW1xT01qTXM?oc=5
- https://news.google.com/rss/articles/CBMi6AFBVV95cUxOdF9FWDEyVWh1ejBmQTV3aW50SGQtX1NjTHlQTEJHZlFPN1Q1SGRhMlpQRHoxNmVHdUFyaVBPTDdxOXcxVUZ0ZTRvQjlZZ2c1bWlSVmQ0OEVSbWtqdzdtZFRYRzBNTVBJQjNmclJicmk3M2FxTnRyRjVxNW1uM2MtV0pGc3R3bGVHbFlZOFNkT2N5d1QzdTZYTUZFUURlSEJueGRQZ2t3dTYtdkxTVkNkYjllMW9oNVJuNnp1aUJGbGJxRno5c05FdGFuNXJTdlhmSWp6UVdHZHpzN25vbGxLTkVBMjZpSjUy?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNVU51MDJmTFk1TGZFN24wSF82QTNmZFBJR3NQdnJMdTNYYzR6Q3hLenNhRVpLY25BT3lGYmtsUFNreXA2a3oxd3BCWE5tNmNka0xaNW5DdDU5MzdlczBBVk1rUDUwdTVBTUtsTVlGT05qVUJuc2FZczJPOTlWSWdZMS1PVlpjNjMzNFRHVzdCelZYXzNoZElUZ3pYNEN6WjctU2pYeXJ3QXVRc181QzlhejBTckNJNy12RExabkRPUWhhSmNqOXVr?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNMVFxTHpyUHFWY3hXWkRGSHNldUlWUU9QcnZrRnFHUDd3U1dZZk0zbkUyNHRPb256NFRWZlU2d1pCandOMkpUeUFqc2dTNEg1Z0EyVHp4b19sMVY0enpXWFlYX2h4WWxVblhHWjR5amNaWktDUjZmOGlMUEZUVXNhcnFlbDZqNFY1NmlGNWVpNGs?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxPRVRpWFdYbFNfaTR3LWowdFNuSXNUTC1TZ1lieWVQZHAyY2J5ZGpoWXhldVpRTm52UE8ya1N2Q2RTUENIOWJHY0IzRHEwWV9MaXZMZDBRU2h4cWFmUUQ2MmxodWVkcU81T1pNNE1USHR3R0tNMWFhT0hkQXBjYW0zQnBvMnNRaUJSbTJQYUhnQUkyTEFIX1hCTnJZLUJFRU1vTVJReHpyekpDSTVIbExRa2gyUQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQZFBLVEpPdDJ6ZlhBczUydzZvUWFaMVctWVJLN29tS1BBRHY3T1BrblNZUVRPcEhtUTBpT3pfOE5sSENSbmsyQWZ4TlVkU0V1dHhUcVR4bzNUVXZCaWJkTV9jb2s3MDRGZGdkcTZGUkxoYkdEWmhUQU5MQm5ybHdQZTBZSUliV2xQblhNOC14eUJ1NXh6NUI5MTRlS2lIeld1T0hRdUUxYjhZdw?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxQdE44SDRNZ19hUGp2ckZ5VjJwTGZkOHVSR203WGZwUFhLWUp5ZVQ0NzBSc3EzWTQtVU9vLTFoLTN1ajJrTE91MkkwYXNjQmpvM3ZGNTlnX1J5Q2d2TGp4RU5sdVl0SklxV0pzOW9SRmkwN2dzUUZENnhqYVVieWJNX1Fib2owOUF1S0NSRl9SWmo1RVE1QUtSNlhxcWRTaXJENVQ4RW5UUk9GUzNKbG5GbzNMTGNEVlk?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxNRnYzc2pVVUVaSEd0ek5wY3duY2EtbXJ6enE3SnhkZ0tJclNVUGZaekpxWXZnR2NIVkNCUW5RN003MV9hMDhFYUxXeVlYZTJlNlpMbVpLTVM1Z1ZCOTNqNEF0YXNuajQwLVN2SVdhQTlScUVvREVPVmxPTWVUYnBrYXc4OUpsOFBZdXlyZzJxaTlnUUpDQl9oTm13NC1WdVJ5T1RGd0J6dktjeHM?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPekNEZ3lzY0RJTDRta3FyTm9lajJXSnl6eUNDZlo2YzNxbGc4ckV4Ymt3U1c2b0gxVUh2VTBMaThLaHZGdU1FbHVubG1Kb19Gd0lvN3U2b2VoUnFxdnphTjViandrNEQ5T01JZTRKeXlMSjZCNGNFRkRxdGZ5SURReWlwRkJTNVZlSlpCU0cwR3U5V2c5WlhNSDdGQQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQV0pUNHJId1ZCM3J1V0xMcmdOZGh2bFFKOHBXQTJnbThrN0xkbFZ4WFgzZ0NITU9mVi1aM1IxYlRRLTBtUWhkOVZadkJ1NGhXWk41c2UwLW9pY1g2TXNmYUxlbjlQM3VqdWRveW5jRG5KRWVhLTJxdk0yVy1TVHpGZ0ZId2tmNkgxZ1JnTGtrR1VrYnhGZ3Zhemd3?oc=5
- https://news.google.com/rss/articles/CBMie0FVX3lxTE5xOS1seWVxRE4zWkYtT2daT0dyWW5hN2lKaEZpc1pqV08yVlVoSGJYZ1h5bWZ0ZWZWY3N6VWxfa01QUTVMS2pzbDNpWFB6b2doNE15VVNGVGVWbVlJQTZiLUdKQV9yajNKSzdJNXFFUzB6MHdiQnBxUkRSUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
