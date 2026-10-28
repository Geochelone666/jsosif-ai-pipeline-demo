# NVO Intelligence Report

- ticker: **NVO**
- Report as_of: **2026-10-27**
- Market data as_of: **2026-10-27**
- Quant sources: https://finance.yahoo.com/quote/NVO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVO/key-statistics/
- AI analysis snapshot as_of: **2026-10-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-28T02:07:48.747215+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 10, 'rule': 2, 'ai': 7, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261027T014607Z-b66f6bd5/NVO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 10 unique headlines; 7 named publishers; 0 exact duplicates; 10 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-10-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 38.6700 |
| Return 1D (%) | -1.1756 |
| Return 1W (%) | -1.7281 |
| Return 1M (%) | -0.3351 |
| Return YTD (%) | -20.2035 |
| Return 1Y (%) | -23.2360 |
| Annualized volatility (%) | 45.5875 |
| Beta vs SPY | 1.0010 |
| Max drawdown (%) | -43.6699 |
| Sharpe (rf=0) | -0.3498 |
| Downside deviation (rf=0, %) | 34.1547 |
| Sortino (rf=0) | -0.4669 |
| Historical VaR 95% (1D, %) | 3.1060 |
| Historical ES 95% (1D, %) | 7.1341 |
| Correlation vs SPY | 0.2789 |
| Tracking error vs SPY (%) | 43.7786 |
| P/E (trailing) | 9.36 |
| P/B | 5.15 |
| EV/EBITDA | 1.53 |
| Revenue growth (%) | 2.10 |
| Forward P/E (estimate) | 11.24 |
| Gross margin (%) | 81.99 |
| Operating margin (%) | 42.54 |
| Return on equity (%) | 59.81 |
| Free cash flow yield (%) | N/A |
| MA50 | 41.6494 |
| Close vs MA50 (%) | -7.1535 |
| MA200 | 43.6349 |
| Close vs MA200 (%) | -11.3783 |
| RSI (14, Wilder) | 43.2289 |
| MACD (12,26) | -0.5684 |
| MACD signal (9) | -0.8762 |
| MACD histogram | 0.3078 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVO': 269, 'SPY': 269}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 38.6700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.1756 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.7281 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -0.3351 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -20.2035 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -23.2360 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 45.5875 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 34.1547 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.4669 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.1060 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 7.1341 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2789 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 43.7786 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.0010 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.6699 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.3498 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.2427 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.9870 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 42.5400 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 59.8150 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 9.3632 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 43.2289 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.3078 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -7.1535 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -11.3783 -> Clearly below the moving-average trend level.

## TAILWINDS

### Novo Nordisk Stock (NVO) Climbs 2% Today on Positive CagriSema Weight-Loss Data
- Summary: Novo Nordisk Stock (NVO) Climbs 2% Today on Positive CagriSema Weight-Loss Data
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQaDNPVlFwU2VwZDJIdWZXQUhEdnA2V1ZPZWUtTC1UUmJ1V0l2QjFRUExEaWNXRnF1UmVRbXJIT0N1XzBERWM5bVJWRTZfSllpUENiV0RMbFpmMU9TNVVlNk9zSXdxbzE4UDNxdUt0YVUtMEl4aXl4bkZrS1M5SEF1SDg0MGJNTHdQOXhtb0QzQmI2Vk40alRVUzRkS3NEWTQyYi1qcFU2ZmY2QQ?oc=5>

### Novo Nordisk stock consolidates near recent highs as buyer support steadies the price
- Summary: Stock consolidates near highs with buyer support.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxNakhQWHBnRS1fVS11aDBucmd6cXpSbmJ0dXAzVTJqd01QbUhIeFFqMmwyc2VaVE5rU1RwMGVWdFowRHZ5WWR5R0VFUXQ2bHp6cDE2OThzQmFuN3pRUGNFbUNMalF5T0xnRHRJaGlPV0ZiSWktRlBzaEpRdHlaYTV2QURwclRXVkJq?oc=5>

### Novo Nordisk (NYSE: NVO) CagriSema Shows 25% Weight Loss In Women As Investors Eye Stock Recovery
- Summary: Novo Nordisk’s CagriSema study shows 25% weight loss in women, boosting investor confidence.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxOcTlVS1JTVVpuZ2RLc3JjS19Pc3F6UUt2TjI0M1RrSE81WG8xUVJxREtIS3Vhelk2OVU4WTNaU3FSUm9mWm9KZnlyWTMzdXl4enpwcXZoaGFfX19UVFpQejE0amwteExoLU03cE15M1hyaVlyR3BWQzZmOWNodEpXYnB1TjB2VUQ1X01GbV9LcmJwbWt3UzBWQXJmM2pUWmt2SDdrbDY4aGRzOEZjcUVZVk5NSjhmM05BaWwtT2pNR2xMRTkxWW42OUtjMHJtMklmS3pOMl9Tc21IUQ?oc=5>

## HEADWINDS

### FDA proposal weighs on Novo Nordisk stock as downward price move persists
- Summary: FDA proposal weighs on stock, price decline continues.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxPQ1A5ZmVjcUpGZGg0VEhhdllXX3dOeUh4bnNFQzhMSVNfRkRPck1xTEdIa29TT1YzbDdzU3hjQ2FCeUVOc2RSajNXdG52NWlkU2NiQzBfNWQyRjQ3d1JnalBLMFc3STlJSkxCTWhuN1VoaEQ5cVhOOUppeF91OVJZaDN6SnhUZlZTZlYtZVBR?oc=5>

## CATALYSTS

### Novo Nordisk (NYSE: NVO) Has Deployed Over DKK 11 Billion Of Its DKK 15 Billion Buyback With Months Still To Run
- Summary: Novo Nordisk (NYSE: NVO) Has Deployed Over DKK 11 Billion Of Its DKK 15 Billion Buyback With Months Still To Run
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxOc3c4UnZPckFzemgyc0dVOGJxYU1ieUZObkdqTzNrOWZ5MjROMklEcFhuT21fQjFOQmtjam00Wk9ZYkVvcmVMUFJubFNCRUZuMmtlQ01td0h3MW5vZGZPRlFKMUNjTzIyc0NOT3YxZG5hWE44eFFaSFZaRmpDUEd6eVBTcjh3OUpXRWk1NHhnb3NETEEwOHFJb29Pdk93RXA1UXNHYjRCN1hjZFB0MGxENG5mUUFvRkw2S1llc1VYek5oR1RPNnpLRVRyYkFPWVQxV1BDNnBrSldERXpEcFYySEZvZ1VXSXRXaFppQ1pQNA?oc=5>

### Treasury shares total 1.2% of capital as Novo Nordisk (NVO) buybacks reach DKK 11.2B.
- Summary: Buybacks reach DKK 11.2B, treasury shares 1.2%.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxPeHV1MVhwRnVkNkpKenJyczFpLWZBLUs5LWFKbTVkMFFRQnBlOTRIWE9Ecnc4dG54ajhWd01SbnBiRWpvS3pWazBMeG44NG5hbVc4QXJNYVd0N0VMZHlBOEtsNFJfb1Yybi0zNzJ4b3NaOVlDam5maVo2WHFpOFBsWUQ1enRqaVMyM2VMSjRoLXNWNm5uSkJvYWZwWlo1YTBUU05KYUpRdHQ1V05EQlVzWQ?oc=5>

### Novo Nordisk (NVO) Stock Declines While Market Improves: Some Information for Investors
- Summary: Shares of Novo Nordisk fell while the broader market improved, indicating a short‑term negative market move for the company.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPQmd4b2gtbWYza0N6N0NfQWs1YXJnVUhoMWh2Q3J5MEdtdzdzbkFxdVpPOFY3OGRLWHBDV05ObGNoQTlsMzlTTVVmNVZwbVMyeWNWOUNXTEpxblM2RGRvYVpObFQwR0J0eU1iaWhOZWhQZV85QlVldERNckQ3X3drTXVPdU9VU05JLUU3S0F0ZVM2TlZhWUhFbngzXzQ?oc=5>

### Moderately bullish activity in Novo Nordisk with shares up 0.24%
- Summary: Novo Nordisk shares rose modestly, reflecting a short‑term positive market move and bullish investor sentiment.
- Date: 2026-10-26 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxNWFNrM2tZbjltY2NPZEJDdXdnLXA2YXk5VDNHM2JmbHFVZDdpSDBacEhDVTFvdGxiRC1YUk51QlR6bFhzOXk1VjVYMFBrWmpRSklFd296cVNJa3IwZWpUVnBDczVLRzVEZkt3VGJLRy1tWDFtTFhhaThGQVkwRXNGNzg3QUtsUF9VVHF3eTlTVFlyNUtQclA3WkR5NW81b2N6amNWRy1GSUFWbGJFSnZjLTRaRQ?oc=5>

### Novo Nordisk Vs. Eli Lilly Q3 Preview: I'd (Now) Buy Both, But Lilly Is My Top Pick (NVO)
- Summary: An analyst preview suggests buying both Novo Nordisk and Eli Lilly, with a preference for Lilly, indicating a neutral market view.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOdThxQ3V4b1RqMXktQklBMTg0ZjRMLUxaLWtGcndLT2toU2g2czNoQnJnWWJYV3R6ZjJLR01YSFd3bTVmVTZhVE5tVnpFbjI5RFF2VDJFTlJoWVdmNEdIcmoxRS03VnZBaVVFUUF6TVNTbkhIOExhWF9Ed19mRGFTQ2tORWpBQ2JWNExHQ21yeG80aHZYTU55cmtaU3o1bm9BUGZLTjZsM3JNMEN2Q3hkWnV2cVB3Y3loVVE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVO** | **9.36** | **5.15** | **1.53** | **2.10** | **170,607,591,424.00 USD** | **-23.24** |
| LLY | 43.03 | 33.73 | 28.50 | 47.70 | 1,143,132,258,304.00 USD | 56.10 |
| ROG.SW | N/A | N/A | N/A | N/A | N/A unknown currency | N/A |
| SAN.PA | 23.12 | 1.30 | 7.95 | 14.60 | 90,034,864,128.00 EUR | -11.31 |

Peers fetched as_of: 2026-10-27; NVO reuses existing data (market data as_of: 2026-10-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: N/A
- Filing date: N/A
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: N/A

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQaDNPVlFwU2VwZDJIdWZXQUhEdnA2V1ZPZWUtTC1UUmJ1V0l2QjFRUExEaWNXRnF1UmVRbXJIT0N1XzBERWM5bVJWRTZfSllpUENiV0RMbFpmMU9TNVVlNk9zSXdxbzE4UDNxdUt0YVUtMEl4aXl4bkZrS1M5SEF1SDg0MGJNTHdQOXhtb0QzQmI2Vk40alRVUzRkS3NEWTQyYi1qcFU2ZmY2QQ?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxNakhQWHBnRS1fVS11aDBucmd6cXpSbmJ0dXAzVTJqd01QbUhIeFFqMmwyc2VaVE5rU1RwMGVWdFowRHZ5WWR5R0VFUXQ2bHp6cDE2OThzQmFuN3pRUGNFbUNMalF5T0xnRHRJaGlPV0ZiSWktRlBzaEpRdHlaYTV2QURwclRXVkJq?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxOcTlVS1JTVVpuZ2RLc3JjS19Pc3F6UUt2TjI0M1RrSE81WG8xUVJxREtIS3Vhelk2OVU4WTNaU3FSUm9mWm9KZnlyWTMzdXl4enpwcXZoaGFfX19UVFpQejE0amwteExoLU03cE15M1hyaVlyR3BWQzZmOWNodEpXYnB1TjB2VUQ1X01GbV9LcmJwbWt3UzBWQXJmM2pUWmt2SDdrbDY4aGRzOEZjcUVZVk5NSjhmM05BaWwtT2pNR2xMRTkxWW42OUtjMHJtMklmS3pOMl9Tc21IUQ?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPQ1A5ZmVjcUpGZGg0VEhhdllXX3dOeUh4bnNFQzhMSVNfRkRPck1xTEdIa29TT1YzbDdzU3hjQ2FCeUVOc2RSajNXdG52NWlkU2NiQzBfNWQyRjQ3d1JnalBLMFc3STlJSkxCTWhuN1VoaEQ5cVhOOUppeF91OVJZaDN6SnhUZlZTZlYtZVBR?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxOc3c4UnZPckFzemgyc0dVOGJxYU1ieUZObkdqTzNrOWZ5MjROMklEcFhuT21fQjFOQmtjam00Wk9ZYkVvcmVMUFJubFNCRUZuMmtlQ01td0h3MW5vZGZPRlFKMUNjTzIyc0NOT3YxZG5hWE44eFFaSFZaRmpDUEd6eVBTcjh3OUpXRWk1NHhnb3NETEEwOHFJb29Pdk93RXA1UXNHYjRCN1hjZFB0MGxENG5mUUFvRkw2S1llc1VYek5oR1RPNnpLRVRyYkFPWVQxV1BDNnBrSldERXpEcFYySEZvZ1VXSXRXaFppQ1pQNA?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxPeHV1MVhwRnVkNkpKenJyczFpLWZBLUs5LWFKbTVkMFFRQnBlOTRIWE9Ecnc4dG54ajhWd01SbnBiRWpvS3pWazBMeG44NG5hbVc4QXJNYVd0N0VMZHlBOEtsNFJfb1Yybi0zNzJ4b3NaOVlDam5maVo2WHFpOFBsWUQ1enRqaVMyM2VMSjRoLXNWNm5uSkJvYWZwWlo1YTBUU05KYUpRdHQ1V05EQlVzWQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPQmd4b2gtbWYza0N6N0NfQWs1YXJnVUhoMWh2Q3J5MEdtdzdzbkFxdVpPOFY3OGRLWHBDV05ObGNoQTlsMzlTTVVmNVZwbVMyeWNWOUNXTEpxblM2RGRvYVpObFQwR0J0eU1iaWhOZWhQZV85QlVldERNckQ3X3drTXVPdU9VU05JLUU3S0F0ZVM2TlZhWUhFbngzXzQ?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxNWFNrM2tZbjltY2NPZEJDdXdnLXA2YXk5VDNHM2JmbHFVZDdpSDBacEhDVTFvdGxiRC1YUk51QlR6bFhzOXk1VjVYMFBrWmpRSklFd296cVNJa3IwZWpUVnBDczVLRzVEZkt3VGJLRy1tWDFtTFhhaThGQVkwRXNGNzg3QUtsUF9VVHF3eTlTVFlyNUtQclA3WkR5NW81b2N6amNWRy1GSUFWbGJFSnZjLTRaRQ?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOdThxQ3V4b1RqMXktQklBMTg0ZjRMLUxaLWtGcndLT2toU2g2czNoQnJnWWJYV3R6ZjJLR01YSFd3bTVmVTZhVE5tVnpFbjI5RFF2VDJFTlJoWVdmNEdIcmoxRS03VnZBaVVFUUF6TVNTbkhIOExhWF9Ed19mRGFTQ2tORWpBQ2JWNExHQ21yeG80aHZYTU55cmtaU3o1bm9BUGZLTjZsM3JNMEN2Q3hkWnV2cVB3Y3loVVE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
