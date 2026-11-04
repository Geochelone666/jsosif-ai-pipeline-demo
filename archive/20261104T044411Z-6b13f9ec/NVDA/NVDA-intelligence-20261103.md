# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-11-03**
- Market data as_of: **2026-11-03**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-11-03**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-04T05:05:50.230912+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 1, 'ai': 15, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **13** exact headline/source/date matches; prior report **20261103T051441Z-8b1c85d8/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 13 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 36.0%; oldest publication 2026-10-30

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 206.6900 |
| Return 1D (%) | 2.2914 |
| Return 1W (%) | -5.1620 |
| Return 1M (%) | -11.6521 |
| Return YTD (%) | 11.0851 |
| Return 1Y (%) | 0.1475 |
| Annualized volatility (%) | 37.3974 |
| Beta vs SPY | 1.9375 |
| Max drawdown (%) | -20.1527 |
| Sharpe (rf=0) | 0.1896 |
| Downside deviation (rf=0, %) | 25.6087 |
| Sortino (rf=0) | 0.2769 |
| Historical VaR 95% (1D, %) | 3.8869 |
| Historical ES 95% (1D, %) | 4.5913 |
| Correlation vs SPY | 0.6631 |
| Tracking error vs SPY (%) | 30.4566 |
| P/E (trailing) | 25.55 |
| P/B | 21.80 |
| EV/EBITDA | 24.63 |
| Revenue growth (%) | 105.90 |
| Forward P/E (estimate) | 12.99 |
| Gross margin (%) | 74.67 |
| Operating margin (%) | 66.24 |
| Return on equity (%) | 117.21 |
| Free cash flow yield (%) | 0.84 |
| MA50 | 221.4051 |
| Close vs MA50 (%) | -6.6462 |
| MA200 | 204.2739 |
| Close vs MA200 (%) | 1.1828 |
| RSI (14, Wilder) | 39.1859 |
| MACD (12,26) | -4.6602 |
| MACD signal (9) | -3.0273 |
| MACD histogram | -1.6329 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 274, 'SPY': 274}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 206.6900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.2914 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -5.1620 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -11.6521 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 11.0851 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 0.1475 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 37.3974 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.6087 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2769 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.8869 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.5913 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6631 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.4566 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.9375 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.1527 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1896 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 12.9874 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.2370 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.2110 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.8377 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 25.5488 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 39.1859 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.6329 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -6.6462 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 1.1828 -> Slightly above the moving-average trend level.

## TAILWINDS

### NVDA Shares Inch Higher Overnight After 4-Day Rout: Chipmaker Reportedly Tells Cloud Clients To Limit China Exposure
- Summary: NVDA Shares Inch Higher Overnight After 4-Day Rout: Chipmaker Reportedly Tells Cloud Clients To Limit China Exposure
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOeThaYzJPQ3BBeXF3WF9WMGZZSFhGdGZWLVpMSzE4NWJzRE5GSnVmcU8zVE5Zc2NyVVZfNFBPbXJsb3g3Wjc1R1lERGdXZmxlU0F3SWt2T0xLZFc1Rk03UE1LYlpyR2FpakowbWdiN19wVy1QQTNZdnp3a21rUVhkU3hQWXZtOTB2TlBoNDNKekVXTGFlUEliWmZPS29Tckk?oc=5>

### Nvidia Stock Looks Surprisingly Cheap. Why NVDA Could Rise 61%.
- Summary: Positive market sentiment suggests potential upside for NVDA shares.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQYjA4NDQtRjBtaDZMX05LdkpMeWZrOVYxWFc2TTgtU0phdXlnc1RvZlJVb3NxWjlfbnkwY3VIOXpvZWpzUklKWEh3LTF6NVBxLWs3OWlsVDY2bXpwa2MwZXczNDhXelFzYUNfWHhwaDVKSnhWZnZDQ1FiRWN4TUNjUVdsaHNHWjJCMDNmbFR0SHFscGpZekx4b21zYmZ5aDVsSkF2UTRmQQ?oc=5>

### NVIDIA (NVDA) Stock Analysis – Entry & Exit Strategy
- Summary: Provides entry and exit guidance for NVDA investors, suggesting strategic trading opportunities.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTE5IUDFwNTU0N2FMNDluR1o0Z0dqNElaMWRna1hWYVFTa3BiYW9udEtZa1RsU081czNoS2ZVa0VpMjlLOUZvcXRyVWh2Si15bGpDMWh4clcxbldTQU1uRFZQN3ZiNVp4bjVsWEtNUXJkX2R3ZXRLUFk2anRpSWI?oc=5>

### Micron, Nvidia, and AMD lead chip stocks' rebound
- Summary: Chip stocks rebound led by Nvidia, Micron, AMD, boosting market sentiment.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOR241WmdKTExjbmZJcndhY3BOVG91eVFPT29xVzBLcVQ4NGQtUExYVDlray1hM1c5dENLekg3bkxyaHFramhTTVEwclZnci1uLWdvbi0zc21pbUMzazNZOFlRUEduSDF5al9jRjMxUG5FOGlTaTdTQVVKZVNRTWplRzh4UjdiYnNhZzBpTHlzS0Q4NzZLZmpfcjJLM1p3TlI3?oc=5>

### ETFs Bought $505.7 Million of NVIDIA (NVDA) on Friday
- Summary: Large ETF purchases of NVDA indicate institutional confidence.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOUzZ5XzJ3b29Ha0lwVWNYRDh0QnR2ZGRuZFVxQldKZjZxdDYwZmYtTl9rU3d2cF93U2tMYVdndzlpTHlQdmFaTDBJNG5EelkzS1JRRExaRnlWbVVnZzkxNEhyUFc0TDJHN1JadGV1eVlLaVlCd0g1dElpX19kVThET2ZIV2FGYmZzQnA5TDE1elRLYTNv?oc=5>

### Nvidia Stock Price Today: NVDA Rebounds 3% From $200 Support Level
- Summary: NVDA shares rebound 3% from $200 support, reflecting bullish momentum.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNbHlWVUxvODMyR0hTd3FycDlMc1FYd0djV00tZWRHbTQtTjVNMTYybEJXRDR2ZnpQV3l6Ri1mRHBnVEhlelVteUp6MExjSGhqMWZZUFl1akQ1THB4cUhKVkE2RlN6dFVhd3E5TDRxTlQ4bEZTMDUtWXF0M3ZBMWpVTnV5Vy1NQXM1c3o3MG5FeWdmVjBqcjhNdkVxeDY3WjlLeDkyckN30gGrAUFVX3lxTE54cWdtLWp6UVpsTGJXTVRBQU0xd0pNeEVfZTJzdTRfYkRRazB5aldSbkt3cUt0TVp5LU1HSzd5V29fcmpNZVhUNVdYeW50R201RHJZX2ZpUTItakJoNGJfQXBFRUEzdDBhSlBsN3BEQjRwQnlPay1GcElMSVRLWFhleFdQV1A4ZnRpSFRwZlp0dVp0bVZmbUZ1Tmpib2xQVWNiVnc1UEFEZVdOVQ?oc=5>

### NVDA Stock Rebounds Off $200 Support after Nvidia CEO Comments and Anthropic Expansion
- Summary: NVDA shares rebound after CEO comments and Anthropic expansion, signaling positive outlook.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNb2lQX2ZYRjUtMllnYlVSelRyaWJ4QmxwYndzTnhOcUZyLUlSd0Z1NWNxUnR2QWN6MGlLY3lncTlaMkZna0MybWlJUEFVemY2Z0EyM1FNMnpSQ3g5MGpiSUVGVWlITnJQRXhjZDBVaFphLXpUOWNtWHozYU5SUjRNcGRZZllDSFB6ZjUyQlMtSE5rM0lNaW9iUXFUQ0ZzQXNGUDN0ZDI2bFBIV0FKWHltSG1GMkZiTU1rRVBoTnByYzd4eTNQblFj?oc=5>

## HEADWINDS

### Nvidia Flashes Sell Signals As Earnings Loom; Is Nvidia A Buy Now?
- Summary: Negative sell signals ahead of earnings.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQNlNYZi1HUzQyS0s4YlN6TUtGZG5JYXI3VXQ0cW1hNjhzNzlmQ2JSdGxSWTBuX1JiMW04LUVTcFptOE9ORjY1YjJRNG15cVpyaHBzVGZ0X3FLeGRyUUg0OVRlNWcwNUlCNzJ6ZWUtdEYtc0wyMFlIMzR4QjVlOHRwcHRKOFNoMnRQZjVOcg?oc=5>

### Nvidia stock valuation gets torched by tech stock rout
- Summary: Negative market move impacting NVDA valuation.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNcGZseDhYeDZxTDFzcm9tLVdXRlo0RzdnTzR6U284RVFhTW1Rc09WU2R6TG1iODczZUQ0RUdPTDdPR09CajZWc0tNMV9laGxQZktza2RtZXRKTE5YT0xfY2FFWFRmVTkyWUxnb251UEJ5TWV5UFJ0VzU1LVgtTzEyZ0RjcURPUXItdEc2YzdSREtuRGZhVUlHQ3JMbWNOZmllc1RzNUphcFBRSjFTakZrT0dpTENVMFhFVVE?oc=5>

### Nvidia Stock Is Rebounding but Stock Chart Is Really Ugly
- Summary: Nvidia shares rebound, yet chart remains unattractive.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxNTVM2cFd2cHpQRW5qUmlXUGhLMlBHTUc5aVgtSTNGZFNDcGZXM3N6aUR6ZVVCZ3ZUSkdwRi15d2lhOHJTWXAxc2N0RXJ6M0x3U3hBVk5yTktPcS12Rl85b3d0aUN5cVpSUEJaTFlWM2ItUloxcEExTHN1cU9ienBTak5DeDQ?oc=5>

### NVDA Stock Drops: Nvidia May Back Data Center Loan For Its Own Customer, Analyst Sees Little Impact From Intel’s Weak Report
- Summary: Stock fell after announcement of potential loan backing, indicating a short‑term negative market reaction.
- Date: 2026-10-30 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQTGdFWTJ1Wm1ISjFPRjVLdVowSFF0RHpiODd4cldVU1VEX3FUU1VFc3hROVlzM3Nsd0RONGE2emNfZ1hsTm9MUUNUR05IWFFnVTJpeEV4TjMzRTZ5eG1scm0yT1VOTWF1X2F1VmoxeG9NaUJqa1hKX0JlbDhGVmY5dEhZcUc0d2hBMGdNUWo2eDdyMlJ0Y3dZ?oc=5>

### Nvidia (NVDA) Falls More Steeply Than Broader Market: What Investors Need to Know
- Summary: NVDA shares dropped more sharply than the broader market, raising concerns about short-term volatility.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNNjROdjdjOVlRX3RIOVVXbDVmSm0yTkJDZUZOcDY3NlJTLXFjSFFTV1A1SHVYeVIxeWw2R1B1anVKaDl0R3RLYmxqTVRiX2hQT18tbm5lVVNBdE9CU3JUZnY3MlBMNDBwSHFDNlJPX2JsdXEtcFdDOVJRNDhFQXg3aXNEX09yck9UbC1vXzZSNmE3cmQ3NHE2Q3o2Yw?oc=5>

### What Is Nvidia (NVDA) Asking Cloud Clients To Change Under New China Rules?
- Summary: Nvidia is requiring its cloud clients to adjust operations due to new Chinese regulations, potentially limiting service offerings and increasing compliance costs.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxORHMwU0xmOXo5U29lbUJIbVJmdDhjVHdqcTMwcm8xUnMtTEw1X285b0VCS25NaWtuX19obHcyLTBLdUxCT2ptUTRlSklnS2c0RTJMLXp3NUJkOEZlbFdFUkNEUTQwcEQ3d3Z1d3BsMmFFUy1rVmJweGE5ZHp2UW0xdzlYX3dWQUtwdkQ3SFBnQ0JGYWNhY2FwNXlYU1A?oc=5>

## CATALYSTS

### Can You Make Money Off NVIDIA Stock Now?
- Summary: Discusses current NVDA stock valuation and potential returns.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQd3NKR0JBQldHLU45bXdMd1g3ZFBDby0tMURjdVNBelJOUW9OcXJfUmJ6cFN4NkdXUHo5Zkk3Z1pyeHRTMTdfTWNVY3prZmptVEJ2NHdGUmJrVEVGQ2xQUGIxZUs1dTk5Q09rWlRsRGt3UHM0YmdoaERWblc1dzF2RlJURHRyRnZCSi1WekRiazFaVDhEc0VMdFR3Q3V0MjJBaVE?oc=5>

### Nvidia Reports Nov. 17. History Says What Its Stock Usually Does Next.
- Summary: NVIDIA releases its earnings report for the period ending Nov. 17, potentially influencing short-term stock movement.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPbGJJZXFlWmhxcWo4RHFDWXFyN1JkcER6LW11MkZNaUpqb09hLS1ycVEzcjFVUkdwbjFxdzRQaEVrdTlUa1NVNlZ4ZDJVMUpfVHQzdlVHdE1zRVptbm9CSVh1R2hqSHBUYy1HMGQyencySVZnWV82VVBlNlJ4eC1HYTZmMzBaX0JXSGw0NEpWNkt6eUY5ZkRfOTZmTUxuakxscGZuRU5nVVZLLXl3X3Bv?oc=5>

## RISKS

### Nvidia (NVDA), Costco (COST), Nike (NKE) join OKX–ICE tokenized stock objections, bringing total to 50
- Summary: Nvidia joins 50 companies objecting to tokenized stocks, raising regulatory concerns.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxNT2JRbThULWtaaVVVeGEyVlZPSTQ0alVKSk1Qc2VKRGppaHVtSFoyM3Uzam1jWE1iVXFsT0dTNmFuTWJhQ3d1ZXZ6dWc3X0RvaVBSeGV5MTNvNm9MdmtyYWVNcmlkRWNMbWttQ2JQTzdEVlZ2SW5UZDRQZnJpOWtsN0V3dmtXaVdTOEZWZm5MeGpoRXZ3NjFHOGZkWEZSc2FObEZFT2hWSk1iYmZJSWxDamlQbWxFN0ppTzRv?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **25.55** | **21.80** | **24.63** | **105.90** | **4,990,943,363,072.00 USD** | **0.15** |
| AMD | 123.44 | 11.75 | 81.69 | 50.10 | 789,954,625,536.00 USD | 86.37 |
| AVGO | 41.16 | 15.91 | 31.02 | 85.50 | 1,585,465,786,368.00 USD | -7.71 |
| INTC | N/A | 2.80 | 17.49 | 20.90 | 321,823,244,288.00 USD | 53.29 |

Peers fetched as_of: 2026-11-03; NVDA reuses existing data (market data as_of: 2026-11-03); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-26
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-26
- Revenue (latest available single quarter): 96,221,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- Net income (latest available single quarter): 59,688,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMinwFBVV95cUxOeThaYzJPQ3BBeXF3WF9WMGZZSFhGdGZWLVpMSzE4NWJzRE5GSnVmcU8zVE5Zc2NyVVZfNFBPbXJsb3g3Wjc1R1lERGdXZmxlU0F3SWt2T0xLZFc1Rk03UE1LYlpyR2FpakowbWdiN19wVy1QQTNZdnp3a21rUVhkU3hQWXZtOTB2TlBoNDNKekVXTGFlUEliWmZPS29Tckk?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQYjA4NDQtRjBtaDZMX05LdkpMeWZrOVYxWFc2TTgtU0phdXlnc1RvZlJVb3NxWjlfbnkwY3VIOXpvZWpzUklKWEh3LTF6NVBxLWs3OWlsVDY2bXpwa2MwZXczNDhXelFzYUNfWHhwaDVKSnhWZnZDQ1FiRWN4TUNjUVdsaHNHWjJCMDNmbFR0SHFscGpZekx4b21zYmZ5aDVsSkF2UTRmQQ?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTE5IUDFwNTU0N2FMNDluR1o0Z0dqNElaMWRna1hWYVFTa3BiYW9udEtZa1RsU081czNoS2ZVa0VpMjlLOUZvcXRyVWh2Si15bGpDMWh4clcxbldTQU1uRFZQN3ZiNVp4bjVsWEtNUXJkX2R3ZXRLUFk2anRpSWI?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOR241WmdKTExjbmZJcndhY3BOVG91eVFPT29xVzBLcVQ4NGQtUExYVDlray1hM1c5dENLekg3bkxyaHFramhTTVEwclZnci1uLWdvbi0zc21pbUMzazNZOFlRUEduSDF5al9jRjMxUG5FOGlTaTdTQVVKZVNRTWplRzh4UjdiYnNhZzBpTHlzS0Q4NzZLZmpfcjJLM1p3TlI3?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOUzZ5XzJ3b29Ha0lwVWNYRDh0QnR2ZGRuZFVxQldKZjZxdDYwZmYtTl9rU3d2cF93U2tMYVdndzlpTHlQdmFaTDBJNG5EelkzS1JRRExaRnlWbVVnZzkxNEhyUFc0TDJHN1JadGV1eVlLaVlCd0g1dElpX19kVThET2ZIV2FGYmZzQnA5TDE1elRLYTNv?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNbHlWVUxvODMyR0hTd3FycDlMc1FYd0djV00tZWRHbTQtTjVNMTYybEJXRDR2ZnpQV3l6Ri1mRHBnVEhlelVteUp6MExjSGhqMWZZUFl1akQ1THB4cUhKVkE2RlN6dFVhd3E5TDRxTlQ4bEZTMDUtWXF0M3ZBMWpVTnV5Vy1NQXM1c3o3MG5FeWdmVjBqcjhNdkVxeDY3WjlLeDkyckN30gGrAUFVX3lxTE54cWdtLWp6UVpsTGJXTVRBQU0xd0pNeEVfZTJzdTRfYkRRazB5aldSbkt3cUt0TVp5LU1HSzd5V29fcmpNZVhUNVdYeW50R201RHJZX2ZpUTItakJoNGJfQXBFRUEzdDBhSlBsN3BEQjRwQnlPay1GcElMSVRLWFhleFdQV1A4ZnRpSFRwZlp0dVp0bVZmbUZ1Tmpib2xQVWNiVnc1UEFEZVdOVQ?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNb2lQX2ZYRjUtMllnYlVSelRyaWJ4QmxwYndzTnhOcUZyLUlSd0Z1NWNxUnR2QWN6MGlLY3lncTlaMkZna0MybWlJUEFVemY2Z0EyM1FNMnpSQ3g5MGpiSUVGVWlITnJQRXhjZDBVaFphLXpUOWNtWHozYU5SUjRNcGRZZllDSFB6ZjUyQlMtSE5rM0lNaW9iUXFUQ0ZzQXNGUDN0ZDI2bFBIV0FKWHltSG1GMkZiTU1rRVBoTnByYzd4eTNQblFj?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQNlNYZi1HUzQyS0s4YlN6TUtGZG5JYXI3VXQ0cW1hNjhzNzlmQ2JSdGxSWTBuX1JiMW04LUVTcFptOE9ORjY1YjJRNG15cVpyaHBzVGZ0X3FLeGRyUUg0OVRlNWcwNUlCNzJ6ZWUtdEYtc0wyMFlIMzR4QjVlOHRwcHRKOFNoMnRQZjVOcg?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNcGZseDhYeDZxTDFzcm9tLVdXRlo0RzdnTzR6U284RVFhTW1Rc09WU2R6TG1iODczZUQ0RUdPTDdPR09CajZWc0tNMV9laGxQZktza2RtZXRKTE5YT0xfY2FFWFRmVTkyWUxnb251UEJ5TWV5UFJ0VzU1LVgtTzEyZ0RjcURPUXItdEc2YzdSREtuRGZhVUlHQ3JMbWNOZmllc1RzNUphcFBRSjFTakZrT0dpTENVMFhFVVE?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxNTVM2cFd2cHpQRW5qUmlXUGhLMlBHTUc5aVgtSTNGZFNDcGZXM3N6aUR6ZVVCZ3ZUSkdwRi15d2lhOHJTWXAxc2N0RXJ6M0x3U3hBVk5yTktPcS12Rl85b3d0aUN5cVpSUEJaTFlWM2ItUloxcEExTHN1cU9ienBTak5DeDQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQTGdFWTJ1Wm1ISjFPRjVLdVowSFF0RHpiODd4cldVU1VEX3FUU1VFc3hROVlzM3Nsd0RONGE2emNfZ1hsTm9MUUNUR05IWFFnVTJpeEV4TjMzRTZ5eG1scm0yT1VOTWF1X2F1VmoxeG9NaUJqa1hKX0JlbDhGVmY5dEhZcUc0d2hBMGdNUWo2eDdyMlJ0Y3dZ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNNjROdjdjOVlRX3RIOVVXbDVmSm0yTkJDZUZOcDY3NlJTLXFjSFFTV1A1SHVYeVIxeWw2R1B1anVKaDl0R3RLYmxqTVRiX2hQT18tbm5lVVNBdE9CU3JUZnY3MlBMNDBwSHFDNlJPX2JsdXEtcFdDOVJRNDhFQXg3aXNEX09yck9UbC1vXzZSNmE3cmQ3NHE2Q3o2Yw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxORHMwU0xmOXo5U29lbUJIbVJmdDhjVHdqcTMwcm8xUnMtTEw1X285b0VCS25NaWtuX19obHcyLTBLdUxCT2ptUTRlSklnS2c0RTJMLXp3NUJkOEZlbFdFUkNEUTQwcEQ3d3Z1d3BsMmFFUy1rVmJweGE5ZHp2UW0xdzlYX3dWQUtwdkQ3SFBnQ0JGYWNhY2FwNXlYU1A?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQd3NKR0JBQldHLU45bXdMd1g3ZFBDby0tMURjdVNBelJOUW9OcXJfUmJ6cFN4NkdXUHo5Zkk3Z1pyeHRTMTdfTWNVY3prZmptVEJ2NHdGUmJrVEVGQ2xQUGIxZUs1dTk5Q09rWlRsRGt3UHM0YmdoaERWblc1dzF2RlJURHRyRnZCSi1WekRiazFaVDhEc0VMdFR3Q3V0MjJBaVE?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPbGJJZXFlWmhxcWo4RHFDWXFyN1JkcER6LW11MkZNaUpqb09hLS1ycVEzcjFVUkdwbjFxdzRQaEVrdTlUa1NVNlZ4ZDJVMUpfVHQzdlVHdE1zRVptbm9CSVh1R2hqSHBUYy1HMGQyencySVZnWV82VVBlNlJ4eC1HYTZmMzBaX0JXSGw0NEpWNkt6eUY5ZkRfOTZmTUxuakxscGZuRU5nVVZLLXl3X3Bv?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxNT2JRbThULWtaaVVVeGEyVlZPSTQ0alVKSk1Qc2VKRGppaHVtSFoyM3Uzam1jWE1iVXFsT0dTNmFuTWJhQ3d1ZXZ6dWc3X0RvaVBSeGV5MTNvNm9MdmtyYWVNcmlkRWNMbWttQ2JQTzdEVlZ2SW5UZDRQZnJpOWtsN0V3dmtXaVdTOEZWZm5MeGpoRXZ3NjFHOGZkWEZSc2FObEZFT2hWSk1iYmZJSWxDamlQbWxFN0ppTzRv?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
