# MU Intelligence Report

- ticker: **MU**
- Report as_of: **2026-11-10**
- Market data as_of: **2026-11-10**
- Quant sources: https://finance.yahoo.com/quote/MU/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MU/key-statistics/
- AI analysis snapshot as_of: **2026-11-10**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-11T04:43:47.014699+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 1, 'ai': 16, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261110T055129Z-abd33250/MU** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 2}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 10 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-06

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 725.1100 |
| Return 1D (%) | -1.0966 |
| Return 1W (%) | -15.2017 |
| Return 1M (%) | -29.5215 |
| Return YTD (%) | 154.2449 |
| Return 1Y (%) | 186.5904 |
| Annualized volatility (%) | 83.6938 |
| Beta vs SPY | 3.3427 |
| Max drawdown (%) | -45.8952 |
| Sharpe (rf=0) | 1.6791 |
| Downside deviation (rf=0, %) | 52.7484 |
| Sortino (rf=0) | 2.6641 |
| Historical VaR 95% (1D, %) | 7.0090 |
| Historical ES 95% (1D, %) | 10.3312 |
| Correlation vs SPY | 0.5460 |
| Tracking error vs SPY (%) | 77.0852 |
| P/E (trailing) | 9.86 |
| P/B | 5.93 |
| EV/EBITDA | 7.19 |
| Revenue growth (%) | 379.30 |
| Forward P/E (estimate) | 3.49 |
| Gross margin (%) | 80.72 |
| Operating margin (%) | 80.68 |
| Return on equity (%) | 88.26 |
| Free cash flow yield (%) | 3.55 |
| MA50 | 952.8730 |
| Close vs MA50 (%) | -23.9028 |
| MA200 | 759.8783 |
| Close vs MA200 (%) | -4.5755 |
| RSI (14, Wilder) | 35.8258 |
| MACD (12,26) | -67.9836 |
| MACD signal (9) | -49.7281 |
| MACD histogram | -18.2555 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MU': 279, 'SPY': 279}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 725.1100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.0966 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -15.2017 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -29.5215 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 154.2449 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 186.5904 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 83.6938 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 52.7484 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.6641 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.0090 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 10.3312 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5460 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 77.0852 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.3427 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -45.8952 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.6791 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 3.4901 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 80.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 80.6780 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 88.2600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.5519 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 9.8641 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 35.8258 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -18.2555 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -23.9028 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -4.5755 -> Slightly below the moving-average trend level.

## TAILWINDS

### Micron Technology (MU) Shares Surge Over 6% Amid Tech Rally on N
- Summary: Micron Technology (MU) Shares Surge Over 6% Amid Tech Rally on N
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOMHNNRkRQZUIxZ0k1dGZDS0ppWWtyLThyc0M3a0pUaTBQZHhUakVIdm5UaWVZTUJzT3BvZHBMaDAwTDJ2VTMxUUZCRzdGOWs5bEVvckJmaVdtSk1hbkVuSm5acng5b05aV3I0akNBQzg0Vm93MUlwOEQyQWJBWFBLRU5NR2dMcGpFOG9kVHdLQzJYUFNNczVnNnZBNmZnMUQ0MUFHc0kzSUNJbUlFUUZDeVcwYm0?oc=5>

### Micron Stock Gets Some Relief as This Big Threat Got Kicked Into the Long Grass
- Summary: Micron shares gained after a major threat was dismissed, boosting investor confidence.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTE52bHNuTVI3U1V6RDY2d0N4ZFBER2lSSXNSVVh4NnFXQWJ1VkYwNjY3VDR5Yk9FM1p5UVIxSTdPRTh4YmYySTJZV2h0TG9LRTRSd1dCUnVjOEwtZnFIbmh6dEstWm5VMk5KV1JXa2xNcURVbjhxcGlkQjVYdXJBYk0?oc=5>

### Micron: The $300 Nightmare And The $1,500 Opportunity (NASDAQ:MU)
- Summary: Micron’s valuation could swing from a $300 to a $1,500 upside, highlighting a potential upside opportunity for investors.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQUV84VUtKd0JJdFpTMkR5YzhqWXhYdDQxWklYbzdVV2N2QW5zZHlwWnFrc3JHRVBVQ1gwWWlCdEN5WHhXczNXUHZXWnU3SU9HODM0STFtVmY5NGxkUVo2N2JfeHR6TEg5Rzl3M0JCaGc5aDlicVNtMlpWVFR5SmdEWklKMnNISXZpRTJET1YyaFhzR1Fa?oc=5>

### Micron Technology Shares Jump 4.11% After Hours Following Sharp Selloff - Micron Technology (NASDAQ:MU)
- Summary: Micron shares rise 4.11% after hours following a sharp selloff.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQLUczZzlCdmVZa0dQYm5uVE8yTFgtaUpMR3NsTXRPVzBpTy1taUNKbV9MZ3NHZi1nOHpkdC10c245dkJUNUFwOHMwQ2FkMG1XXzBvY3ltRzlucHpFN3dNX3F3OE1ZeEJoNHBRX25WNHg1QXRWYmVfS21qdHk2amlKU2lJbHoyZTIwa29UVHFvUDEwTUY5X1kzY2VqLXBLa1A4T3Z3eVlIbDJTZkpC?oc=5>

### Micron Has Lost Over 40% Since June. Where Does Its Price Target Stand Now?
- Summary: Micron’s stock has declined over 40% since June, raising questions about current price targets and future upside potential.
- Date: 2026-11-09 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNcmxpcHd4RmU1VWFqNjRWTlRzZzdBbmRMUjZmVjIxMW41T0RWXzB5Smc0U2diTHJJN0NISTlMTkk0V1VaeWpDM1BhREtJTElDSVJSY1E4U0xDTlpSVEZlY0xHZldzTVFqeW9tcWdHY0lqbU5LNFppaW5KV3NXd2VIX1BqTlVrc2FJX3BNNjZYRzRObkZr?oc=5>

### Micron Technology Inc Stock (MU) Moved Up by 5.73% on Nov 9: What Investors Need To Know
- Summary: Micron shares rose 5.73% on Nov 9, prompting investors to review the stock’s recent performance and potential catalysts for the uptick.
- Date: 2026-11-09 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxQbXA3S3lxWkhQTUNQYmpqd1JSUFNUelRadTUtQzJLYWJmX0FTS3pGalBEWGFTWHNQMG5jVmZhQkRnenVrQ1E5ZThQUXRydkxzSnoxR25zN2kyZTdxdU5oYUFVY1MxRUtXdXViX05fQmNQQ2NmTV9NcXlVcWVCaGExSEV4VkJ1U20z?oc=5>

### Micron Technology climbs 6% amid broad tech rally (MU:NASDAQ)
- Summary: Micron shares surged 6% alongside a broader tech rally.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxON3JqNzJwYXFJLTRwQkJXbm9mbVdDcGdRbFJad0kzcUxOMmF6YW5BTG8wdldZWUFkNVJHU3NYRmRldzJuQnZwdXN5bkFmV2d3VFR1eXJ1T1luejVhNFRkWW9MMU1BYldJdVM4MDhvNmo3WndRNkJlaE1XYUpnd0dBckdXdy1EOTJUU2E3V013dWZjR3IxOFlUWGF3?oc=5>

### I Still Think Micron Stock Is a Buy. Here's the Price at Which I'd Sell It.
- Summary: Analyst expresses bullish view and target sell price for Micron shares.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNY2stTE5ZNjFmLXlvbkxTMFNzZXduV1BwdDdRRmV6YnBPa2xlWTZqUjhaNmoxb0J0MG10THZQSXBDWEVUWkgwdVpUVE9Zd3dDYlh5aWVrUkZiS3E4LURZbV9xMS1pSlpVU1ZjVnpUbXNIelR6aldwWlVYdFBpWnNkbHplTUFLeEtpNkFmQTkzN1hMN3hwd0lnX0dYang5a3FzQ256SzNELWpwTDhzNl81Vk5oX2ZDbDA?oc=5>

## HEADWINDS

### Micron Stock Drops Again. The Case for It Soaring 148%.
- Summary: Stock fell, but article suggests potential large upside.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMid0FVX3lxTE1FTlNRaGxKTExzb0JlTGtscEUxeE1wVEF2clFJeVdicTJrbmliMkVyQURoUGZnYWlRWGFsU2RWS3ByX0RzSjh4SEFVX1YtT3VaZThlbC1HZGlvU1d0Q0xBOENMS3pXRDNPa21NV0FkMGRKSEQwVzRR?oc=5>

### Micron Technology Inc Stock (MU) Moved Down by 3.61% on Nov 10: Facts Behind the Movement
- Summary: Shares declined 3.61% on Nov 10, citing underlying factors.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxPazBiZHBGVnM3b2M5c1p2OEVrOUpwZkhoSFBjM1cwOWY0Mngxbkdmc1lJYzRaM0YxWlI5NUF6YWdLVTBvbzFtSy02UVhDZGpyd3J0Nl90MVItTHpzRHJSWFFiTUhVOC1KeWM3VEFQa3JCUjdUclhSSm1FMlVySEZJa1pocjh1SmNs?oc=5>

### Micron Technology Stocks Slip 1.27% as Hot CPI Overshadows $1 Billion Anthropic Bet
- Summary: Micron shares fell 1.27% amid high CPI, eclipsing a $1B Anthropic investment.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxNVVFmUjRncFN2VnljQmJvYlM5VExSdnVWa1c5LUFOZnZXRUc3dEVubGpjSmJHcS1hNXhQQzhac2w4ZGZmeF8xQUJwS1BodXBEX2pBNjlDNVZSX0szTjFfdmk2RUIzTWYtVzhrSmtiQ1dSZGR2Z0FLTlZIV004V3pueHpyS3M1dE9zbkw1TC1weEoxakFrT1hrZnNiNVNvZkY1dlJhbkZzdE1VVUtsYkZNc3lERzZjZF9vaFUwbkZqemU3cGl0QkpqZDk0azF0cHZJYndSa0lCTjY?oc=5>

### What Does Micron Technology (MU) Taiwan Plant Halt Mean For Its Capacity Plans?
- Summary: Micron’s Taiwan plant halt could constrain future capacity, affecting supply plans.
- Date: 2026-11-08 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQVHZEczc4Sk80aWZLc1NfQmhub01tUTRicHEwM2lUTWpHRW9xVzJ3OWZSNmFMWG01Vjl0YjUyaTk0bE4zdXVGWHhXb2NDWlJSelI1MVlnTGlkaGl6MmY5YVVGeFlqMU5haEFmZWRDaVpCY183QVVJSk5sZUZiYTBqQWlfcWZ0S0FxdjZNdTVwSEtKUk1sN0dEWA?oc=5>

## CATALYSTS

### Micron: Why I Added $5,000 Worth Of Shares During The Selloff (Rating Downgrade)
- Summary: Author added $5k Micron shares during selloff, citing long-term upside.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQRVUwam11U3lCbXRBRlRUQ1JVTHJwZm9NdmZYN0xCWC00azIxNkVoTDZtT2I5RUJmNW1DRlBsbmxOa3ExNEFWTDZ1R0pvRVU4ZkdOblBWOFIzRVVvOEFnWWRidnR3YnpGdXYwb1RjNGgzLV91WUY0bklkYS1PVzhIS093aE9VZlVRWnd5NnB3THozRENSclZVTGNXXzNMSllz?oc=5>

### Micron: Market Mistook A Slowdown For A Total Collapse (NASDAQ:MU)
- Summary: Commentary that market overreacted to a slowdown, suggesting a rebound for Micron.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQRUNlUS1HX0EyN3lLVE9oNldoUU40UlZaSHgxbGRQNm5aVjBtNERjc1E2dmR5NDI0VnhGLXFoYlp1VVNXa2J2WllQTkp6eXVWUFJ0dEhkeFdMZ2pNTmRDbTAyMTdkalJXMVR1bUp2WnJHd0NBNVhBT0daN0N0UzIwQkZjVklUZUxvdG1tZUZOODF0TkFCenBZbzNB?oc=5>

### Nvidia, Alphabet, and Micron Just Agreed to Buy $26 Billion of Stock in One of Their Biggest Customers
- Summary: Micron agreed to purchase $26B of stock in a major customer, expanding equity stake.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxOMjFLeTI3UDd6aTRDcTNHcGpvenN2VXMyd1FVempYWGZpV3hkcDFtR1N0UnVZWXdmMjhMdlVjN1h6TV9kMHlhZjgxdm14OXFvQkFxM2VDYndEM0pmVVJJX3JtVnlrRnVpd3JPM2UyQjZOSl9xdTVtSzN2YUVoSElzUlFGbDJWa3RwY1BDdURTUnJ2Q3dveUdQTGUxdU05bDVlSUdiUTNLc1JOeC1RdE9zZklFVi1vWWVxeWx4T3V6MTNMbDJUdWVfczB0Ti1FRjBidzBrVnB2OTN4QQ?oc=5>

### Micron Rises 6% as Bulls Tout Its Bargain Valuation and Buyback Firepower; Seagate and Western Digital Jump 11%
- Summary: Positive sentiment on Micron’s valuation and buyback potential drives a 6% stock jump.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNdXN0NEpHWm1Xb2ZxUzB6UFlEVGxmUERJMDZUQXJla0FVcHJ4d1ZFTE05bzBSaG5TeGZRNFFRYnd4RlZjaWVJVEh3LXI4Ml9vWnFGNGhjU3VUdTRaYWNGQjYwMzdOanFwcmhiVXBJN3BCZ1MxekEydDdQZFpoS3F2VG1YUnZXM1BTbFc5S0tVem9od0tz?oc=5>

## RISKS

### Bank of America Removes Micron Technology (MU) from US 1 List Am
- Summary: Bank of America removed MU from its US 1 list, signaling a downgrade.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPbC1wX2VFVW45S3pOdWFPOFBZQjd1bzgyVHU0U0dRaURTczNIWWh2bTg1WjN6T1JYbEVKam53N3RrOFNpS0JjWlRMM1J4cE9HMVdpRUs0QmJmQkxUWnNRM0R5ZHNIaW9PSGJtRUpYMFBybjdXeXRnRjFHUl9BcWpaNmxrRFJNa0VuYjVTd0R1WjE5WE5lSXQxYUdpbnZIQW5UcmM4Vlk5U1plMGY5c09VUUhvUjN0eUJkS0hubnFR?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MU** | **9.86** | **5.93** | **7.19** | **379.30** | **820,406,255,616.00 USD** | **186.59** |
| WDC | 10.19 | 11.57 | 17.09 | 55.50 | 108,254,289,920.00 USD | 66.31 |
| STX | 26.54 | 33.37 | 19.87 | 61.00 | 115,152,437,248.00 USD | 71.63 |
| NXPI | 20.58 | 5.45 | 13.61 | 19.30 | 65,926,979,584.00 USD | 29.76 |

Peers fetched as_of: 2026-11-10; MU reuses existing data (market data as_of: 2026-11-10); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-30
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-10

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-09
- Revenue (latest available single quarter): 8,440,000,000.00 USD; period 2018-06-01/2018-08-30; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 28,243,000,000.00 USD; period 2026-02-27/2026-05-28; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMitAFBVV95cUxOMHNNRkRQZUIxZ0k1dGZDS0ppWWtyLThyc0M3a0pUaTBQZHhUakVIdm5UaWVZTUJzT3BvZHBMaDAwTDJ2VTMxUUZCRzdGOWs5bEVvckJmaVdtSk1hbkVuSm5acng5b05aV3I0akNBQzg0Vm93MUlwOEQyQWJBWFBLRU5NR2dMcGpFOG9kVHdLQzJYUFNNczVnNnZBNmZnMUQ0MUFHc0kzSUNJbUlFUUZDeVcwYm0?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTE52bHNuTVI3U1V6RDY2d0N4ZFBER2lSSXNSVVh4NnFXQWJ1VkYwNjY3VDR5Yk9FM1p5UVIxSTdPRTh4YmYySTJZV2h0TG9LRTRSd1dCUnVjOEwtZnFIbmh6dEstWm5VMk5KV1JXa2xNcURVbjhxcGlkQjVYdXJBYk0?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQUV84VUtKd0JJdFpTMkR5YzhqWXhYdDQxWklYbzdVV2N2QW5zZHlwWnFrc3JHRVBVQ1gwWWlCdEN5WHhXczNXUHZXWnU3SU9HODM0STFtVmY5NGxkUVo2N2JfeHR6TEg5Rzl3M0JCaGc5aDlicVNtMlpWVFR5SmdEWklKMnNISXZpRTJET1YyaFhzR1Fa?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQLUczZzlCdmVZa0dQYm5uVE8yTFgtaUpMR3NsTXRPVzBpTy1taUNKbV9MZ3NHZi1nOHpkdC10c245dkJUNUFwOHMwQ2FkMG1XXzBvY3ltRzlucHpFN3dNX3F3OE1ZeEJoNHBRX25WNHg1QXRWYmVfS21qdHk2amlKU2lJbHoyZTIwa29UVHFvUDEwTUY5X1kzY2VqLXBLa1A4T3Z3eVlIbDJTZkpC?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNcmxpcHd4RmU1VWFqNjRWTlRzZzdBbmRMUjZmVjIxMW41T0RWXzB5Smc0U2diTHJJN0NISTlMTkk0V1VaeWpDM1BhREtJTElDSVJSY1E4U0xDTlpSVEZlY0xHZldzTVFqeW9tcWdHY0lqbU5LNFppaW5KV3NXd2VIX1BqTlVrc2FJX3BNNjZYRzRObkZr?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxQbXA3S3lxWkhQTUNQYmpqd1JSUFNUelRadTUtQzJLYWJmX0FTS3pGalBEWGFTWHNQMG5jVmZhQkRnenVrQ1E5ZThQUXRydkxzSnoxR25zN2kyZTdxdU5oYUFVY1MxRUtXdXViX05fQmNQQ2NmTV9NcXlVcWVCaGExSEV4VkJ1U20z?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxON3JqNzJwYXFJLTRwQkJXbm9mbVdDcGdRbFJad0kzcUxOMmF6YW5BTG8wdldZWUFkNVJHU3NYRmRldzJuQnZwdXN5bkFmV2d3VFR1eXJ1T1luejVhNFRkWW9MMU1BYldJdVM4MDhvNmo3WndRNkJlaE1XYUpnd0dBckdXdy1EOTJUU2E3V013dWZjR3IxOFlUWGF3?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNY2stTE5ZNjFmLXlvbkxTMFNzZXduV1BwdDdRRmV6YnBPa2xlWTZqUjhaNmoxb0J0MG10THZQSXBDWEVUWkgwdVpUVE9Zd3dDYlh5aWVrUkZiS3E4LURZbV9xMS1pSlpVU1ZjVnpUbXNIelR6aldwWlVYdFBpWnNkbHplTUFLeEtpNkFmQTkzN1hMN3hwd0lnX0dYang5a3FzQ256SzNELWpwTDhzNl81Vk5oX2ZDbDA?oc=5
- https://news.google.com/rss/articles/CBMid0FVX3lxTE1FTlNRaGxKTExzb0JlTGtscEUxeE1wVEF2clFJeVdicTJrbmliMkVyQURoUGZnYWlRWGFsU2RWS3ByX0RzSjh4SEFVX1YtT3VaZThlbC1HZGlvU1d0Q0xBOENMS3pXRDNPa21NV0FkMGRKSEQwVzRR?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxPazBiZHBGVnM3b2M5c1p2OEVrOUpwZkhoSFBjM1cwOWY0Mngxbkdmc1lJYzRaM0YxWlI5NUF6YWdLVTBvbzFtSy02UVhDZGpyd3J0Nl90MVItTHpzRHJSWFFiTUhVOC1KeWM3VEFQa3JCUjdUclhSSm1FMlVySEZJa1pocjh1SmNs?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxNVVFmUjRncFN2VnljQmJvYlM5VExSdnVWa1c5LUFOZnZXRUc3dEVubGpjSmJHcS1hNXhQQzhac2w4ZGZmeF8xQUJwS1BodXBEX2pBNjlDNVZSX0szTjFfdmk2RUIzTWYtVzhrSmtiQ1dSZGR2Z0FLTlZIV004V3pueHpyS3M1dE9zbkw1TC1weEoxakFrT1hrZnNiNVNvZkY1dlJhbkZzdE1VVUtsYkZNc3lERzZjZF9vaFUwbkZqemU3cGl0QkpqZDk0azF0cHZJYndSa0lCTjY?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQVHZEczc4Sk80aWZLc1NfQmhub01tUTRicHEwM2lUTWpHRW9xVzJ3OWZSNmFMWG01Vjl0YjUyaTk0bE4zdXVGWHhXb2NDWlJSelI1MVlnTGlkaGl6MmY5YVVGeFlqMU5haEFmZWRDaVpCY183QVVJSk5sZUZiYTBqQWlfcWZ0S0FxdjZNdTVwSEtKUk1sN0dEWA?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQRVUwam11U3lCbXRBRlRUQ1JVTHJwZm9NdmZYN0xCWC00azIxNkVoTDZtT2I5RUJmNW1DRlBsbmxOa3ExNEFWTDZ1R0pvRVU4ZkdOblBWOFIzRVVvOEFnWWRidnR3YnpGdXYwb1RjNGgzLV91WUY0bklkYS1PVzhIS093aE9VZlVRWnd5NnB3THozRENSclZVTGNXXzNMSllz?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQRUNlUS1HX0EyN3lLVE9oNldoUU40UlZaSHgxbGRQNm5aVjBtNERjc1E2dmR5NDI0VnhGLXFoYlp1VVNXa2J2WllQTkp6eXVWUFJ0dEhkeFdMZ2pNTmRDbTAyMTdkalJXMVR1bUp2WnJHd0NBNVhBT0daN0N0UzIwQkZjVklUZUxvdG1tZUZOODF0TkFCenBZbzNB?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxOMjFLeTI3UDd6aTRDcTNHcGpvenN2VXMyd1FVempYWGZpV3hkcDFtR1N0UnVZWXdmMjhMdlVjN1h6TV9kMHlhZjgxdm14OXFvQkFxM2VDYndEM0pmVVJJX3JtVnlrRnVpd3JPM2UyQjZOSl9xdTVtSzN2YUVoSElzUlFGbDJWa3RwY1BDdURTUnJ2Q3dveUdQTGUxdU05bDVlSUdiUTNLc1JOeC1RdE9zZklFVi1vWWVxeWx4T3V6MTNMbDJUdWVfczB0Ti1FRjBidzBrVnB2OTN4QQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNdXN0NEpHWm1Xb2ZxUzB6UFlEVGxmUERJMDZUQXJla0FVcHJ4d1ZFTE05bzBSaG5TeGZRNFFRYnd4RlZjaWVJVEh3LXI4Ml9vWnFGNGhjU3VUdTRaYWNGQjYwMzdOanFwcmhiVXBJN3BCZ1MxekEydDdQZFpoS3F2VG1YUnZXM1BTbFc5S0tVem9od0tz?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPbC1wX2VFVW45S3pOdWFPOFBZQjd1bzgyVHU0U0dRaURTczNIWWh2bTg1WjN6T1JYbEVKam53N3RrOFNpS0JjWlRMM1J4cE9HMVdpRUs0QmJmQkxUWnNRM0R5ZHNIaW9PSGJtRUpYMFBybjdXeXRnRjFHUl9BcWpaNmxrRFJNa0VuYjVTd0R1WjE5WE5lSXQxYUdpbnZIQW5UcmM4Vlk5U1plMGY5c09VUUhvUjN0eUJkS0hubnFR?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
