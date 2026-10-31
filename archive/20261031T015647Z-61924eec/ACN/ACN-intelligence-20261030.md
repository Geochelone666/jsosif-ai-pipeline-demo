# ACN Intelligence Report

- ticker: **ACN**
- Report as_of: **2026-10-30**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/ACN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ACN/key-statistics/
- AI analysis snapshot as_of: **2026-10-30**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-31T02:08:39.349546+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 17, 'rule': 1, 'ai': 13, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261030T021807Z-b9de7146/ACN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 17 unique headlines; 9 named publishers; 0 exact duplicates; 17 HTTPS source links; largest publisher share 17.65%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 258.2400 |
| Return 1D (%) | 4.4576 |
| Return 1W (%) | 3.5570 |
| Return 1M (%) | 41.9598 |
| Return YTD (%) | -0.9781 |
| Return 1Y (%) | 6.5901 |
| Annualized volatility (%) | 49.8666 |
| Beta vs SPY | 0.0065 |
| Max drawdown (%) | -56.5068 |
| Sharpe (rf=0) | 0.3788 |
| Downside deviation (rf=0, %) | 34.6378 |
| Sortino (rf=0) | 0.5453 |
| Historical VaR 95% (1D, %) | 4.5949 |
| Historical ES 95% (1D, %) | 6.8005 |
| Correlation vs SPY | 0.0017 |
| Tracking error vs SPY (%) | 51.4597 |
| P/E (trailing) | 19.04 |
| P/B | 4.87 |
| EV/EBITDA | 11.54 |
| Revenue growth (%) | 6.20 |
| Forward P/E (estimate) | 16.25 |
| Gross margin (%) | 32.05 |
| Operating margin (%) | 17.83 |
| Return on equity (%) | 26.02 |
| Free cash flow yield (%) | 6.76 |
| MA50 | 201.6766 |
| Close vs MA50 (%) | 28.0466 |
| MA200 | 188.1011 |
| Close vs MA200 (%) | 37.2878 |
| RSI (14, Wilder) | 70.5517 |
| MACD (12,26) | 15.8639 |
| MACD signal (9) | 14.7018 |
| MACD histogram | 1.1622 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ACN': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 258.2400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 4.4576 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.5570 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 41.9598 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -0.9781 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 6.5901 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 49.8666 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 34.6378 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.5453 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.5949 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.8005 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0017 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 51.4597 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0065 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -56.5068 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3788 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.2540 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 32.0500 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.8280 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 26.0250 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.7611 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 19.0442 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 70.5517 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.1622 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 28.0466 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 37.2878 -> Clearly above the moving-average trend level.

## TAILWINDS

### Accenture PLC (ACN) Shares Surge 4.5% -- What GF Score of 91 Tel
- Summary: Accenture PLC (ACN) Shares Surge 4.5% -- What GF Score of 91 Tel
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxNZlRfSHNlSTlBaWhBdkdGUjBGTmxSR1dxaExZclpvNEVuWDdKZDZmbmdyQ1U4VWQtVkFTSXdELWdSQmljQVItSmVLd0V0aTFnMTEyck9jVzBFUXBqV2s2eTZzWmhUOXdLNWM5OU8yME5sa2xDZDV3aEdNTmFObHA4TmMtV1JVN0luUFZQbFp2akk5LWZTVVU1UFg5S3R0dHp3czlfb19YM1VmWEps?oc=5>

### Investors Heavily Search Accenture PLC (ACN): Here is What You Need to Know
- Summary: High search volume indicates growing investor interest in Accenture, suggesting potential market attention and possible valuation reconsideration.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQWDdRZmdQeFp2NHRYRGZja1duVmNsYm54WlN5bWdMdEsyZUQ4VFFpN3NOR0toUDVFTkg2MEFpWWltb3EzUkw0LXpZbnR5SkcyaGJWWkR6RDJzcUNWdjJFcXJ1aERieWxSc2d5bmNuYzVORWtNNHJvME9MMUx6Vl9BTW1fVk1nMFY2bjh0ZjJOVTNLUjl3U2psdV9MTU1ZRTdwZnFKRHNn?oc=5>

### Accenture PLC Stock (ACN) Moved Up by 4.43% on Oct 28: A Full Analysis
- Summary: Positive price movement indicates favorable market sentiment.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNNXk1MVNuS3ktZW9oOUFuazFHZkgxU0h6MWhjZ213aGN4d01RZFZJMkY5N3RSTDZXdUVIY1dzYS1LQ3pMeGFvUmYwYjBaWWEyanprTHBReU4ycTI2a2lITlhuOW5sLTRjbzRXRjRRWDJTSW9VaEhYZ2x4ejQ2Z0h0QkRyMFFiaGNFLVE?oc=5>

### Intel’s Plunge Today Makes It October’s Worst S&P 500 Stock. Accenture Is the Biggest Winner.
- Summary: Accenture stock rose as Intel fell, making it the top performer in the S&P 500 for the day.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxOaldpVGFpbkplUnhmS2xFSlNiNkNWc3hVeXJPNGprVDJQVVQ0c2doU1d6SHhoTUs4RmEzY1BlTkliNmtrWDFOYnF6ZmNJTGROV19DaTNrOWdqSXRRSXJzSVZMa0RZakd0OGoyUVE4N29ubExsTDVRUFI1T3VaR0F2Sk5qVE0xSXFlX2Y0YzYtQ3dXUQ?oc=5>

### Accenture PLC Stock (ACN) Closed Up by 4.46% on Oct 30: Facts Behind the Movement
- Summary: Accenture shares closed 4.46% higher on Oct 30, indicating a positive price movement.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxOT1ZmaHVvYVhiUHNncFhEcTZSUGxCeERXZXlSbHNOR2FZNkFCOFJFU2o2eGE1b0FVczJfWHBTR012bndna2JOYTFQSzMxTHFQUXFjekVvWmt1QU9SNGNsa25rbUxrMjNwZGU0NTIyVmhkRFpwUW1PNC1UR1VrRlBibHdvV2tqaGFoMnc?oc=5>

### Fund Update: 912,506 ACCENTURE (ACN) shares added to PZENA INVESTMENT MANAGEMENT LLC portfolio
- Summary: PZENA Investment Management added 912,506 Accenture shares to its portfolio, signaling institutional support.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxQZVRETm8tR0tSTFR5MHFiOXNrWXk1OG9RMnBBOHB0RFNMTVdXWk40RS04OUp2a1FMSGJkZWpPbTJFYVRMdUxNQlIwVEpBSG9iWjZhYjhrMlNqVkVlTy1TQ1dsNktOZzJLazNGM0ZSbDlSVVZpZEZicVJGamVUdEtxQ25YSXZMbUNHVW4xdGNuc2NCbXg2NGFUdGN2T0IzVTBwT1Bjb0xETF9od0NBNmxlNkJzY0tvV0dtZWdpSnE0RExaYmg4ZUxBNXY3aWpXNk11?oc=5>

### After buying 800 shares, Accenture (ACN) director Price directly holds 9,361 shares.
- Summary: Director Price increased holdings to 9,361 shares after purchasing 800, indicating insider confidence.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxNUjhXUFN2YnlCRlBLUk9EZVg3NndLMEoxR0xMdVBncTJRekk4RWxqWkpoblNUTzF2Q2RRbndqZWRINmxXcXplcTJveXZxVXJuYkN6OEZGSU5kY2M4VHdzVU5GdlQtUHI3WWZhMUxXY2ZrZEF4UE9EVjYtVTc1NE8xYjRLMld4eG5aOXl0RkRPZE0zaWZIUi10U0xGVnRyenpUZ3d0YjZNQW5Ndw?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### What's behind Accenture's latest stock pullback?
- Summary: Accenture's recent stock pullback attributed to market factors and investor sentiment.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPVWVGZko1dXNtUTVHa2JReDhMMjR2Nng4SGhzVWN0RjdSYlg1U3dxWHpnY012SnMyOENkMUxEWlozNjRxcXV5a0pNVndDcUtBREhLejBtWmtfY1Eya1J0WTBwQkRDWkZZTndiNm9lemxXLXlLVl9RSElkTmZ3c013WnMyTDRFcDA0MFRpb3RkbFppZw?oc=5>

### Accenture (ACN) vs. CTSH and IBM: Can Valuation Recovery and Dividend Growth Drive the Next Upside?
- Summary: Analyst compares Accenture's valuation recovery and dividend growth potential against competitors.
- Date: 2026-10-27 | Impact: low | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQN29ZdmJ3OFdfTXRLVHNvWnVCa3pCWE5HdlJBRkQ1cUlRcHNSOENSZmg1a2Y1SEhuRDNqdnU0RDA1RTNTZUpWal9xTHJhZVMtdkhDT0wycVI4QjJQX19vMzBHcTNFYmF1NEt4NG1aR2kyRXBmcDVnZHdibGNPaTV5VXAyN0hSLUVWU1llT2x0REpLbEFR?oc=5>

### Accenture (ACN) Increases Despite Market Slip: Here's What You Need to Know
- Summary: Accenture shares rise amid broader market decline, indicating resilience and potential upside.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOTHpaZ0RYVTJfbm5Hd3JueTYwNDFYZm1pLXpyRExoek5uaTZESUlNSWJPSkc1Mm5tSnd3blBRWjlLSHZqdFdUMWxOQU15dE03SmdPdmFSZ2tSczgxUjJoREZGUW91dG5OZHJlT3FmUDFmVmFQY3dfTDhqZWNrcGFIam9NNi1hcUVJYmRWNThTZWlaLWFfbWRnekYtMmNzc2piQWEyOGhn?oc=5>

### Accenture PLC Stock (ACN) Moved Down by 4.41% on Oct 27: Key Drivers Unveiled
- Summary: Accenture shares fell 4.41% on Oct 27 due to identified key drivers.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNT0NCZ21GY2RlNUUyVkVnNEpxbzJJZlFXa0x1RllfcXV4UzlIaGllRlVaa0pJaS1Zb2NPcnBLSWtRdm53d3cySU14Si1tRXVlRmtPNTQwMW5kU2UzeldwMFlJQVpIRkF2MXZ4VE40TjZlcnpraEotWG1uYnhKX0tESkpRYkhxVW5NWUE?oc=5>

### Accenture CEO Julie Sweet Buys $3 Million in Stock as Director Also Purchases Shares
- Summary: CEO Julie Sweet purchased $3M of shares, indicating confidence in the company.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxPMWJ0ZDVWdC1VQUZNOVlDV0d5Ti02cU5tTHBjQkdsdUtNSF9tNUJBZkJrMk1kLTRHR3RnU0dmeG1OYk9UUTlGamtwTmhlR0NWN3JrbXhYdmFKOGlxY1dBS1EwNlp0Rmk3R3Vxck1WZnlCZmpFa0pKTDN4OG54QWtDRUE0TlM1Nmp0cHVtRUoyOTdWSjcxaVowT3BSMUZacF9XbW45TEVtUEplVHZEMVdPcTBOYjVpZnk4d2o0?oc=5>

### Accenture (ACN) Chair and CEO Julie Sweet Buys 12,200 Shares
- Summary: CEO share purchase signals strong confidence in company prospects.
- Date: 2026-10-28 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPYXBVR1BaSFhJamNBMlNCbDhoM2J0NTZFaXJKci1iQWM5TVN4THM5bF9OMFBxajhQRjNVVmxvdXhxT0NzRGJIb2hYaGVfM2x2OS1vRVMxQXhhLTFKNXE0RGFabFo5WFpzWHNuMXFqbHZpZTBjeFhCc1NtWHNubGVYczhGQ2JNczd1eGJYRlJoQ0lOS0dEMWhTQW9zSHc?oc=5>

### The chair and CEO buys Accenture (ACN) shares in two direct purchases.
- Summary: Accenture's chair and CEO purchased shares directly, indicating confidence in the company's prospects.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOamVqTVQ0VFkwLVlCRVg5bEFlUmx5VV9NSnlMSmhtVDJUVUxrQ1lzSUFlTUNMbDJkV1otVkNFV3pZYS1RLXdtUUJCTk1UODZkdDA2SmZtbUQtbzVUVWZfaGRaSk85QWpWdVgzem42X2RlYTVfUU5ONHlsYTU1LVVoay12NzdOTHlleFRoVnllN3RONUFzeUFqMDE0dHRlYW85UEg1bnJVRVRPQQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ACN** | **19.04** | **4.87** | **11.54** | **6.20** | **158,027,923,456.00 USD** | **6.59** |
| IBM | 22.00 | 6.86 | 18.06 | 4.70 | 243,661,602,816.00 USD | -14.69 |
| CTSH | 14.00 | 1.98 | 7.25 | 4.60 | 29,106,151,424.00 USD | -7.77 |
| INFY | 15.49 | 9.84 | 21.86 | 1.40 | 50,832,224,256.00 USD | -22.95 |

Peers fetched as_of: 2026-10-30; ACN reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-01
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-30

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-16
- Revenue (latest available single quarter): 18,679,110,000.00 USD; period 2026-06-01/2026-08-31; fiscal year/reporting period 2026/FY
- Net income (latest available single quarter): 1,991,267,000.00 USD; period 2026-06-01/2026-08-31; fiscal year/reporting period 2026/FY
- SEC link: https://www.sec.gov/Archives/edgar/data/1467373/000146737326000049/acn-20260831.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMirAFBVV95cUxNZlRfSHNlSTlBaWhBdkdGUjBGTmxSR1dxaExZclpvNEVuWDdKZDZmbmdyQ1U4VWQtVkFTSXdELWdSQmljQVItSmVLd0V0aTFnMTEyck9jVzBFUXBqV2s2eTZzWmhUOXdLNWM5OU8yME5sa2xDZDV3aEdNTmFObHA4TmMtV1JVN0luUFZQbFp2akk5LWZTVVU1UFg5S3R0dHp3czlfb19YM1VmWEps?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQWDdRZmdQeFp2NHRYRGZja1duVmNsYm54WlN5bWdMdEsyZUQ4VFFpN3NOR0toUDVFTkg2MEFpWWltb3EzUkw0LXpZbnR5SkcyaGJWWkR6RDJzcUNWdjJFcXJ1aERieWxSc2d5bmNuYzVORWtNNHJvME9MMUx6Vl9BTW1fVk1nMFY2bjh0ZjJOVTNLUjl3U2psdV9MTU1ZRTdwZnFKRHNn?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNNXk1MVNuS3ktZW9oOUFuazFHZkgxU0h6MWhjZ213aGN4d01RZFZJMkY5N3RSTDZXdUVIY1dzYS1LQ3pMeGFvUmYwYjBaWWEyanprTHBReU4ycTI2a2lITlhuOW5sLTRjbzRXRjRRWDJTSW9VaEhYZ2x4ejQ2Z0h0QkRyMFFiaGNFLVE?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxOaldpVGFpbkplUnhmS2xFSlNiNkNWc3hVeXJPNGprVDJQVVQ0c2doU1d6SHhoTUs4RmEzY1BlTkliNmtrWDFOYnF6ZmNJTGROV19DaTNrOWdqSXRRSXJzSVZMa0RZakd0OGoyUVE4N29ubExsTDVRUFI1T3VaR0F2Sk5qVE0xSXFlX2Y0YzYtQ3dXUQ?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxOT1ZmaHVvYVhiUHNncFhEcTZSUGxCeERXZXlSbHNOR2FZNkFCOFJFU2o2eGE1b0FVczJfWHBTR012bndna2JOYTFQSzMxTHFQUXFjekVvWmt1QU9SNGNsa25rbUxrMjNwZGU0NTIyVmhkRFpwUW1PNC1UR1VrRlBibHdvV2tqaGFoMnc?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxQZVRETm8tR0tSTFR5MHFiOXNrWXk1OG9RMnBBOHB0RFNMTVdXWk40RS04OUp2a1FMSGJkZWpPbTJFYVRMdUxNQlIwVEpBSG9iWjZhYjhrMlNqVkVlTy1TQ1dsNktOZzJLazNGM0ZSbDlSVVZpZEZicVJGamVUdEtxQ25YSXZMbUNHVW4xdGNuc2NCbXg2NGFUdGN2T0IzVTBwT1Bjb0xETF9od0NBNmxlNkJzY0tvV0dtZWdpSnE0RExaYmg4ZUxBNXY3aWpXNk11?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNUjhXUFN2YnlCRlBLUk9EZVg3NndLMEoxR0xMdVBncTJRekk4RWxqWkpoblNUTzF2Q2RRbndqZWRINmxXcXplcTJveXZxVXJuYkN6OEZGSU5kY2M4VHdzVU5GdlQtUHI3WWZhMUxXY2ZrZEF4UE9EVjYtVTc1NE8xYjRLMld4eG5aOXl0RkRPZE0zaWZIUi10U0xGVnRyenpUZ3d0YjZNQW5Ndw?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPVWVGZko1dXNtUTVHa2JReDhMMjR2Nng4SGhzVWN0RjdSYlg1U3dxWHpnY012SnMyOENkMUxEWlozNjRxcXV5a0pNVndDcUtBREhLejBtWmtfY1Eya1J0WTBwQkRDWkZZTndiNm9lemxXLXlLVl9RSElkTmZ3c013WnMyTDRFcDA0MFRpb3RkbFppZw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQN29ZdmJ3OFdfTXRLVHNvWnVCa3pCWE5HdlJBRkQ1cUlRcHNSOENSZmg1a2Y1SEhuRDNqdnU0RDA1RTNTZUpWal9xTHJhZVMtdkhDT0wycVI4QjJQX19vMzBHcTNFYmF1NEt4NG1aR2kyRXBmcDVnZHdibGNPaTV5VXAyN0hSLUVWU1llT2x0REpLbEFR?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOTHpaZ0RYVTJfbm5Hd3JueTYwNDFYZm1pLXpyRExoek5uaTZESUlNSWJPSkc1Mm5tSnd3blBRWjlLSHZqdFdUMWxOQU15dE03SmdPdmFSZ2tSczgxUjJoREZGUW91dG5OZHJlT3FmUDFmVmFQY3dfTDhqZWNrcGFIam9NNi1hcUVJYmRWNThTZWlaLWFfbWRnekYtMmNzc2piQWEyOGhn?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNT0NCZ21GY2RlNUUyVkVnNEpxbzJJZlFXa0x1RllfcXV4UzlIaGllRlVaa0pJaS1Zb2NPcnBLSWtRdm53d3cySU14Si1tRXVlRmtPNTQwMW5kU2UzeldwMFlJQVpIRkF2MXZ4VE40TjZlcnpraEotWG1uYnhKX0tESkpRYkhxVW5NWUE?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxPMWJ0ZDVWdC1VQUZNOVlDV0d5Ti02cU5tTHBjQkdsdUtNSF9tNUJBZkJrMk1kLTRHR3RnU0dmeG1OYk9UUTlGamtwTmhlR0NWN3JrbXhYdmFKOGlxY1dBS1EwNlp0Rmk3R3Vxck1WZnlCZmpFa0pKTDN4OG54QWtDRUE0TlM1Nmp0cHVtRUoyOTdWSjcxaVowT3BSMUZacF9XbW45TEVtUEplVHZEMVdPcTBOYjVpZnk4d2o0?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPYXBVR1BaSFhJamNBMlNCbDhoM2J0NTZFaXJKci1iQWM5TVN4THM5bF9OMFBxajhQRjNVVmxvdXhxT0NzRGJIb2hYaGVfM2x2OS1vRVMxQXhhLTFKNXE0RGFabFo5WFpzWHNuMXFqbHZpZTBjeFhCc1NtWHNubGVYczhGQ2JNczd1eGJYRlJoQ0lOS0dEMWhTQW9zSHc?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOamVqTVQ0VFkwLVlCRVg5bEFlUmx5VV9NSnlMSmhtVDJUVUxrQ1lzSUFlTUNMbDJkV1otVkNFV3pZYS1RLXdtUUJCTk1UODZkdDA2SmZtbUQtbzVUVWZfaGRaSk85QWpWdVgzem42X2RlYTVfUU5ONHlsYTU1LVVoay12NzdOTHlleFRoVnllN3RONUFzeUFqMDE0dHRlYW85UEg1bnJVRVRPQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
