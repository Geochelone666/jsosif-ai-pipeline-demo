# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-11-04**
- Market data as_of: **2026-11-04**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-11-04**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-05T05:17:20.570814+00:00**
- AI status: **Partial: 2 headlines remain unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 1, 'ai': 14, 'unknown': 2, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261104T044411Z-6b13f9ec/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 13 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 37.5%; oldest publication 2026-11-01

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 200.1300 |
| Return 1D (%) | -3.1738 |
| Return 1W (%) | -7.0805 |
| Return 1M (%) | -14.4561 |
| Return YTD (%) | 7.5594 |
| Return 1Y (%) | 0.9661 |
| Annualized volatility (%) | 37.3213 |
| Beta vs SPY | 1.8639 |
| Max drawdown (%) | -19.3046 |
| Sharpe (rf=0) | 0.2111 |
| Downside deviation (rf=0, %) | 25.4987 |
| Sortino (rf=0) | 0.3090 |
| Historical VaR 95% (1D, %) | 3.7736 |
| Historical ES 95% (1D, %) | 4.5802 |
| Correlation vs SPY | 0.6412 |
| Tracking error vs SPY (%) | 30.7120 |
| P/E (trailing) | 25.30 |
| P/B | 21.10 |
| EV/EBITDA | 23.85 |
| Revenue growth (%) | 105.90 |
| Forward P/E (estimate) | 12.58 |
| Gross margin (%) | 74.67 |
| Operating margin (%) | 66.24 |
| Return on equity (%) | 117.21 |
| Free cash flow yield (%) | 0.87 |
| MA50 | 221.1514 |
| Close vs MA50 (%) | -9.5054 |
| MA200 | 204.3863 |
| Close vs MA200 (%) | -2.0825 |
| RSI (14, Wilder) | 34.5448 |
| MACD (12,26) | -5.2957 |
| MACD signal (9) | -3.4809 |
| MACD histogram | -1.8147 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 275, 'SPY': 275}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 200.1300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.1738 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -7.0805 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -14.4561 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 7.5594 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 0.9661 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 37.3213 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.4987 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3090 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.7736 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.5802 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6412 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.7120 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.8639 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.3046 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2111 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 12.5752 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.2370 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.2110 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.8652 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 25.3009 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 34.5448 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.8147 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -9.5054 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -2.0825 -> Slightly below the moving-average trend level.

## TAILWINDS

### NVDA Shares Inch Higher Overnight After 4-Day Rout: Chipmaker Reportedly Tells Cloud Clients To Limit China Exposure
- Summary: NVDA Shares Inch Higher Overnight After 4-Day Rout: Chipmaker Reportedly Tells Cloud Clients To Limit China Exposure
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOeThaYzJPQ3BBeXF3WF9WMGZZSFhGdGZWLVpMSzE4NWJzRE5GSnVmcU8zVE5Zc2NyVVZfNFBPbXJsb3g3Wjc1R1lERGdXZmxlU0F3SWt2T0xLZFc1Rk03UE1LYlpyR2FpakowbWdiN19wVy1QQTNZdnp3a21rUVhkU3hQWXZtOTB2TlBoNDNKekVXTGFlUEliWmZPS29Tckk?oc=5>

### Nvidia Stock Looks Surprisingly Cheap. Why NVDA Could Rise 61%.
- Summary: Positive market sentiment suggests potential upside for NVDA shares.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQYjA4NDQtRjBtaDZMX05LdkpMeWZrOVYxWFc2TTgtU0phdXlnc1RvZlJVb3NxWjlfbnkwY3VIOXpvZWpzUklKWEh3LTF6NVBxLWs3OWlsVDY2bXpwa2MwZXczNDhXelFzYUNfWHhwaDVKSnhWZnZDQ1FiRWN4TUNjUVdsaHNHWjJCMDNmbFR0SHFscGpZekx4b21zYmZ5aDVsSkF2UTRmQQ?oc=5>

### Micron, Nvidia, and AMD lead chip stocks' rebound
- Summary: Chip stocks rebound led by Nvidia, Micron, AMD, boosting market sentiment.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOR241WmdKTExjbmZJcndhY3BOVG91eVFPT29xVzBLcVQ4NGQtUExYVDlray1hM1c5dENLekg3bkxyaHFramhTTVEwclZnci1uLWdvbi0zc21pbUMzazNZOFlRUEduSDF5al9jRjMxUG5FOGlTaTdTQVVKZVNRTWplRzh4UjdiYnNhZzBpTHlzS0Q4NzZLZmpfcjJLM1p3TlI3?oc=5>

### Nvidia’s Dismal Run Might Be Coming to an End. Grab NVDA Stock While It’s Still Around $200.
- Summary: Speculation that Nvidia’s recent decline may reverse, offering upside potential.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxQaS1sOHNjaEtZdEY0aG9yTEZuRDVNU3M2a0EwckVaZG9HaE9MUVRNNkE0b1BlWlk2eEdVWkdzX0FGZHB5dGlpQ1kxU2ZoUkQxVHY5amFVNEdEaGRfTUpIMnhadHp0NXo2RDNLTFJ4aVVfZTVDc3I4RUpXdnpva1Nnc1J3TEJRUHQtUDhwUVA4N1N6bzQ0b3ZmUU91azFrSVp1ajcwZUM3X1BoM0JlQWpER1NnZzhRdWlaUWRLUG04UU9LSTJGQmdEc1Awdw?oc=5>

### Why Nvidia Stock Can Ride Out a Data-Center Crackdown
- Summary: Nvidia expected to withstand data‑center slowdown, maintaining performance.
- Date: 2026-11-04 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE0xS01LbkZsaFVHUndoOHltS1lFSzg3dnI0SVdRZ1p1Mm40MEtoM2QxcWxnb01OOFJhTlBPZ09WdjZxYy1XWjdJZzJ2NEo4clZjOGljMm9zb0RZNzJlVU1XRGwtVmF4LUlpelh6V1Bsbl8teG84MTBDbFZGeF9FZw?oc=5>

### 55 ETFs Add to NVIDIA (NVDA) on Nov. 2
- Summary: Fifty-five ETFs added NVDA to their portfolios on Nov. 2, boosting institutional support.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPTXk4Q3RpQ3dybXhwSDc5V09faWQwOS1aaEw0WFVmd3BRU2o4cG5IZ01WckszalE0VTJNazh0MEdKU1VxZjNvUVM4aXdQWi02eENtaFJ0Tkx3UkYtbEZBeGtxY1N4TFZGaTd2amdvZ0Vyd3IyVGNxM08xX3hTeF9iSkp2bTEtZlozU1RQT21Cak5yUQ?oc=5>

## HEADWINDS

### Nvidia Flashes Sell Signals As Earnings Loom; Is Nvidia A Buy Now?
- Summary: Negative sell signals ahead of earnings.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQNlNYZi1HUzQyS0s4YlN6TUtGZG5JYXI3VXQ0cW1hNjhzNzlmQ2JSdGxSWTBuX1JiMW04LUVTcFptOE9ORjY1YjJRNG15cVpyaHBzVGZ0X3FLeGRyUUg0OVRlNWcwNUlCNzJ6ZWUtdEYtc0wyMFlIMzR4QjVlOHRwcHRKOFNoMnRQZjVOcg?oc=5>

### Nvidia stock valuation gets torched by tech stock rout
- Summary: Negative market move impacting NVDA valuation.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNcGZseDhYeDZxTDFzcm9tLVdXRlo0RzdnTzR6U284RVFhTW1Rc09WU2R6TG1iODczZUQ0RUdPTDdPR09CajZWc0tNMV9laGxQZktza2RtZXRKTE5YT0xfY2FFWFRmVTkyWUxnb251UEJ5TWV5UFJ0VzU1LVgtTzEyZ0RjcURPUXItdEc2YzdSREtuRGZhVUlHQ3JMbWNOZmllc1RzNUphcFBRSjFTakZrT0dpTENVMFhFVVE?oc=5>

### Nvidia (NVDA) Falls More Steeply Than Broader Market: What Investors Need to Know
- Summary: NVDA shares dropped more sharply than the broader market, raising concerns about short-term volatility.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNNjROdjdjOVlRX3RIOVVXbDVmSm0yTkJDZUZOcDY3NlJTLXFjSFFTV1A1SHVYeVIxeWw2R1B1anVKaDl0R3RLYmxqTVRiX2hQT18tbm5lVVNBdE9CU3JUZnY3MlBMNDBwSHFDNlJPX2JsdXEtcFdDOVJRNDhFQXg3aXNEX09yck9UbC1vXzZSNmE3cmQ3NHE2Q3o2Yw?oc=5>

### Why Couldn’t Nvidia Stock (NVDA) Hang on to Its Premarket Gains Today?
- Summary: Premarket gains failed to sustain, indicating short‑term weakness.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQeWN2Zkw0cElZVnEtQXZHeGR6Z0UyWXhMM3RMSUlkdXJLeU5LaEJSOXB4ajk5MW8ta29mVVZiS184WEppdmk1LXRxS0lMSXZKYWlUbGpqLVRBdUF5TnA0WXFqMVZvRU9vN3FNSUlyZ0pLSndHQ1VIZnFPS09hS0x2X2FKOGZnYjRUc3VvTmxZVVR3dkFsSENqMGZkOF8?oc=5>

### NVDA Stock Tests $200 Support as Political Backlash Hits Nvidia and Chip Sector
- Summary: NVDA stock tested $200 support amid political backlash affecting the chip sector.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxQRXNWWjRJb2UyOFZjVFNlWW82UG1nS1dmX0ZEVDFlMjVjMl83QW5LOTIwMWJHRzI3M3dZVWhSUGUtSGJjeE80MUdQcXNITnFaOVliei1GV203N0tTSVZQa0xpLTV5OFU3WXRTYWZNMDlPYV93bVlZYjZTMGdwNGliTFY2LTc3VzZQUDdOQjVmaGhiT2tMNlRHQlk2N0plb2x0ZFpzbHRZM3dWdjd5MDNoS05mUXdXSlZWc0k0SkV3?oc=5>

### NVIDIA Corp Stock (NVDA) Closed Down by 3.12% on Nov 4: What Investors Need To Know
- Summary: NVDA shares fell 3.12% on Nov. 4, reflecting market concerns.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPSHFObXJxc3NCal9CZVJhTTllZ2V3Z0dWWVBnUDM2YzNaRURETU9DQm5BVmpHbmNyM3Rsb25VdHlWcHNCYmd0WUtHQ1lyOFJ4OGFHY014M1J4SVhra2Y0T1YxS3kxUVI5MEZPMEs1UGhNZjBmRVZWTnRjeUVON1pCenI5WUF4dXhseUt3?oc=5>

## CATALYSTS

### Nvidia Reports Nov. 17. History Says What Its Stock Usually Does Next.
- Summary: NVIDIA releases its earnings report for the period ending Nov. 17, potentially influencing short-term stock movement.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPbGJJZXFlWmhxcWo4RHFDWXFyN1JkcER6LW11MkZNaUpqb09hLS1ycVEzcjFVUkdwbjFxdzRQaEVrdTlUa1NVNlZ4ZDJVMUpfVHQzdlVHdE1zRVptbm9CSVh1R2hqSHBUYy1HMGQyencySVZnWV82VVBlNlJ4eC1HYTZmMzBaX0JXSGw0NEpWNkt6eUY5ZkRfOTZmTUxuakxscGZuRU5nVVZLLXl3X3Bv?oc=5>

### Is Nvidia a Buy Right Now?
- Summary: Analyst recommends buying Nvidia shares, citing growth prospects.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxQMHpCWmxRUWppeFZTUFNpNWlpRVctcWczOVc2UzE3ZGFqazVyUDJZNHZoZTFJcjlSSTA4dzc3b0xiMk91QTlUSHVJTVdCN2FMRkFucVh2N2ZsRURlbkR3ai1GdGdNUXNES0NkMURvcDRUeEhTYXVENjNKbVdPcF8xcnlpM0U5Zw?oc=5>

## RISKS

### Nvidia (NVDA), Costco (COST), Nike (NKE) join OKX–ICE tokenized stock objections, bringing total to 50
- Summary: Nvidia faces regulatory objections over tokenized stocks, adding compliance risk.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxNT2JRbThULWtaaVVVeGEyVlZPSTQ0alVKSk1Qc2VKRGppaHVtSFoyM3Uzam1jWE1iVXFsT0dTNmFuTWJhQ3d1ZXZ6dWc3X0RvaVBSeGV5MTNvNm9MdmtyYWVNcmlkRWNMbWttQ2JQTzdEVlZ2SW5UZDRQZnJpOWtsN0V3dmtXaVdTOEZWZm5MeGpoRXZ3NjFHOGZkWEZSc2FObEZFT2hWSk1iYmZJSWxDamlQbWxFN0ppTzRv?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **25.30** | **21.10** | **23.85** | **105.90** | **4,832,539,181,056.00 USD** | **0.97** |
| AMD | 123.43 | 12.65 | 81.69 | 50.10 | 797,921,116,160.00 USD | 95.47 |
| AVGO | 42.44 | 15.59 | 30.41 | 85.50 | 1,553,721,065,472.00 USD | -6.83 |
| INTC | N/A | 2.69 | 16.85 | 20.90 | 309,705,048,064.00 USD | 57.36 |

Peers fetched as_of: 2026-11-04; NVDA reuses existing data (market data as_of: 2026-11-04); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-26
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-04

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
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOR241WmdKTExjbmZJcndhY3BOVG91eVFPT29xVzBLcVQ4NGQtUExYVDlray1hM1c5dENLekg3bkxyaHFramhTTVEwclZnci1uLWdvbi0zc21pbUMzazNZOFlRUEduSDF5al9jRjMxUG5FOGlTaTdTQVVKZVNRTWplRzh4UjdiYnNhZzBpTHlzS0Q4NzZLZmpfcjJLM1p3TlI3?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxQaS1sOHNjaEtZdEY0aG9yTEZuRDVNU3M2a0EwckVaZG9HaE9MUVRNNkE0b1BlWlk2eEdVWkdzX0FGZHB5dGlpQ1kxU2ZoUkQxVHY5amFVNEdEaGRfTUpIMnhadHp0NXo2RDNLTFJ4aVVfZTVDc3I4RUpXdnpva1Nnc1J3TEJRUHQtUDhwUVA4N1N6bzQ0b3ZmUU91azFrSVp1ajcwZUM3X1BoM0JlQWpER1NnZzhRdWlaUWRLUG04UU9LSTJGQmdEc1Awdw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNdEgyWm5JN1NaYmppU3BFaUktcExpOVVTbjVKQTQyV3Rvc2NDV3EySldvVk5wREtUY3NON09yLVRucW1xOW9nVTVTR0tnbm0xVmVmOHJldVYxSk9fcXFQRC0zR0x2b2JfMjJXLXFLYnUtVmtjd1pTY1UyR0RVcWI5YVhTZ2F5U1kzMWNVRGxXcFVMSVdpZk5vR0xIYw?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE0xS01LbkZsaFVHUndoOHltS1lFSzg3dnI0SVdRZ1p1Mm40MEtoM2QxcWxnb01OOFJhTlBPZ09WdjZxYy1XWjdJZzJ2NEo4clZjOGljMm9zb0RZNzJlVU1XRGwtVmF4LUlpelh6V1Bsbl8teG84MTBDbFZGeF9FZw?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPTXk4Q3RpQ3dybXhwSDc5V09faWQwOS1aaEw0WFVmd3BRU2o4cG5IZ01WckszalE0VTJNazh0MEdKU1VxZjNvUVM4aXdQWi02eENtaFJ0Tkx3UkYtbEZBeGtxY1N4TFZGaTd2amdvZ0Vyd3IyVGNxM08xX3hTeF9iSkp2bTEtZlozU1RQT21Cak5yUQ?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQNlNYZi1HUzQyS0s4YlN6TUtGZG5JYXI3VXQ0cW1hNjhzNzlmQ2JSdGxSWTBuX1JiMW04LUVTcFptOE9ORjY1YjJRNG15cVpyaHBzVGZ0X3FLeGRyUUg0OVRlNWcwNUlCNzJ6ZWUtdEYtc0wyMFlIMzR4QjVlOHRwcHRKOFNoMnRQZjVOcg?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNcGZseDhYeDZxTDFzcm9tLVdXRlo0RzdnTzR6U284RVFhTW1Rc09WU2R6TG1iODczZUQ0RUdPTDdPR09CajZWc0tNMV9laGxQZktza2RtZXRKTE5YT0xfY2FFWFRmVTkyWUxnb251UEJ5TWV5UFJ0VzU1LVgtTzEyZ0RjcURPUXItdEc2YzdSREtuRGZhVUlHQ3JMbWNOZmllc1RzNUphcFBRSjFTakZrT0dpTENVMFhFVVE?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNNjROdjdjOVlRX3RIOVVXbDVmSm0yTkJDZUZOcDY3NlJTLXFjSFFTV1A1SHVYeVIxeWw2R1B1anVKaDl0R3RLYmxqTVRiX2hQT18tbm5lVVNBdE9CU3JUZnY3MlBMNDBwSHFDNlJPX2JsdXEtcFdDOVJRNDhFQXg3aXNEX09yck9UbC1vXzZSNmE3cmQ3NHE2Q3o2Yw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQeWN2Zkw0cElZVnEtQXZHeGR6Z0UyWXhMM3RMSUlkdXJLeU5LaEJSOXB4ajk5MW8ta29mVVZiS184WEppdmk1LXRxS0lMSXZKYWlUbGpqLVRBdUF5TnA0WXFqMVZvRU9vN3FNSUlyZ0pLSndHQ1VIZnFPS09hS0x2X2FKOGZnYjRUc3VvTmxZVVR3dkFsSENqMGZkOF8?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxQRXNWWjRJb2UyOFZjVFNlWW82UG1nS1dmX0ZEVDFlMjVjMl83QW5LOTIwMWJHRzI3M3dZVWhSUGUtSGJjeE80MUdQcXNITnFaOVliei1GV203N0tTSVZQa0xpLTV5OFU3WXRTYWZNMDlPYV93bVlZYjZTMGdwNGliTFY2LTc3VzZQUDdOQjVmaGhiT2tMNlRHQlk2N0plb2x0ZFpzbHRZM3dWdjd5MDNoS05mUXdXSlZWc0k0SkV3?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPSHFObXJxc3NCal9CZVJhTTllZ2V3Z0dWWVBnUDM2YzNaRURETU9DQm5BVmpHbmNyM3Rsb25VdHlWcHNCYmd0WUtHQ1lyOFJ4OGFHY014M1J4SVhra2Y0T1YxS3kxUVI5MEZPMEs1UGhNZjBmRVZWTnRjeUVON1pCenI5WUF4dXhseUt3?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPbGJJZXFlWmhxcWo4RHFDWXFyN1JkcER6LW11MkZNaUpqb09hLS1ycVEzcjFVUkdwbjFxdzRQaEVrdTlUa1NVNlZ4ZDJVMUpfVHQzdlVHdE1zRVptbm9CSVh1R2hqSHBUYy1HMGQyencySVZnWV82VVBlNlJ4eC1HYTZmMzBaX0JXSGw0NEpWNkt6eUY5ZkRfOTZmTUxuakxscGZuRU5nVVZLLXl3X3Bv?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxQMHpCWmxRUWppeFZTUFNpNWlpRVctcWczOVc2UzE3ZGFqazVyUDJZNHZoZTFJcjlSSTA4dzc3b0xiMk91QTlUSHVJTVdCN2FMRkFucVh2N2ZsRURlbkR3ai1GdGdNUXNES0NkMURvcDRUeEhTYXVENjNKbVdPcF8xcnlpM0U5Zw?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxNT2JRbThULWtaaVVVeGEyVlZPSTQ0alVKSk1Qc2VKRGppaHVtSFoyM3Uzam1jWE1iVXFsT0dTNmFuTWJhQ3d1ZXZ6dWc3X0RvaVBSeGV5MTNvNm9MdmtyYWVNcmlkRWNMbWttQ2JQTzdEVlZ2SW5UZDRQZnJpOWtsN0V3dmtXaVdTOEZWZm5MeGpoRXZ3NjFHOGZkWEZSc2FObEZFT2hWSk1iYmZJSWxDamlQbWxFN0ppTzRv?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
