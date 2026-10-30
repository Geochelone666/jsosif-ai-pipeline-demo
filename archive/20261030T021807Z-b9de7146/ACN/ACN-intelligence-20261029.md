# ACN Intelligence Report

- ticker: **ACN**
- Report as_of: **2026-10-29**
- Market data as_of: **2026-10-29**
- Quant sources: https://finance.yahoo.com/quote/ACN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ACN/key-statistics/
- AI analysis snapshot as_of: **2026-10-29**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-30T02:39:15.636815+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 1, 'ai': 17, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **19** exact headline/source/date matches; prior report **20261029T020157Z-688a53f0/ACN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 12 named publishers; 0 exact duplicates; 23 HTTPS source links; largest publisher share 21.74%; oldest publication 2026-10-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 247.2200 |
| Return 1D (%) | 1.5694 |
| Return 1W (%) | -4.4523 |
| Return 1M (%) | 40.6974 |
| Return YTD (%) | -5.2037 |
| Return 1Y (%) | 2.6593 |
| Annualized volatility (%) | 49.6743 |
| Beta vs SPY | 0.0527 |
| Max drawdown (%) | -56.5068 |
| Sharpe (rf=0) | 0.3024 |
| Downside deviation (rf=0, %) | 34.6378 |
| Sortino (rf=0) | 0.4337 |
| Historical VaR 95% (1D, %) | 4.5949 |
| Historical ES 95% (1D, %) | 6.8005 |
| Correlation vs SPY | 0.0135 |
| Tracking error vs SPY (%) | 51.1082 |
| P/E (trailing) | 18.23 |
| P/B | 4.66 |
| EV/EBITDA | 11.05 |
| Revenue growth (%) | 6.20 |
| Forward P/E (estimate) | 15.56 |
| Gross margin (%) | 32.05 |
| Operating margin (%) | 17.83 |
| Return on equity (%) | 26.02 |
| Free cash flow yield (%) | 7.06 |
| MA50 | 200.1099 |
| Close vs MA50 (%) | 23.5421 |
| MA200 | 188.2123 |
| Close vs MA200 (%) | 31.3517 |
| RSI (14, Wilder) | 66.5291 |
| MACD (12,26) | 15.2782 |
| MACD signal (9) | 14.4112 |
| MACD histogram | 0.8670 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ACN': 271, 'SPY': 271}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 247.2200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.5694 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.4523 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 40.6974 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -5.2037 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 2.6593 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 49.6743 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 34.6378 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4337 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.5949 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.8005 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0135 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 51.1082 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0527 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -56.5068 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3024 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.5604 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 32.0500 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.8280 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 26.0250 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.0625 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.2316 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 66.5291 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.8670 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 23.5421 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 31.3517 -> Clearly above the moving-average trend level.

## TAILWINDS

### Accenture PLC (ACN) Stock Up 7.7% and Still Undervalued -- GF Sc
- Summary: Accenture PLC (ACN) Stock Up 7.7% and Still Undervalued -- GF Sc
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNYzN3b1o1cG85eDhLaTFlSWw1cTJWUXRoUU9iRnVldzBfbXhRQjBINHFiLTVDWXo5QUx4R1IyTU42NUJVVG9KWFNUX1h6TEJHMWhIMzZXWmE5SmtTZWdnRXdnZVJqQkN1cmZTUmRuNU90c1VjMWFlLUhqam5FTW91V1J0dzV1YXpBZXFuNXVLSnJVMlJZdEptR0xfQk5VYW9vT2N6V0NKSWM?oc=5>

### Investors Heavily Search Accenture PLC (ACN): Here is What You Need to Know
- Summary: High search volume indicates growing investor interest in Accenture, suggesting potential market attention and possible valuation reconsideration.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQWDdRZmdQeFp2NHRYRGZja1duVmNsYm54WlN5bWdMdEsyZUQ4VFFpN3NOR0toUDVFTkg2MEFpWWltb3EzUkw0LXpZbnR5SkcyaGJWWkR6RDJzcUNWdjJFcXJ1aERieWxSc2d5bmNuYzVORWtNNHJvME9MMUx6Vl9BTW1fVk1nMFY2bjh0ZjJOVTNLUjl3U2psdV9MTU1ZRTdwZnFKRHNn?oc=5>

### Accenture PLC Stock (ACN) Moved Up by 4.43% on Oct 28: A Full Analysis
- Summary: Positive price movement indicates favorable market sentiment.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNNXk1MVNuS3ktZW9oOUFuazFHZkgxU0h6MWhjZ213aGN4d01RZFZJMkY5N3RSTDZXdUVIY1dzYS1LQ3pMeGFvUmYwYjBaWWEyanprTHBReU4ycTI2a2lITlhuOW5sLTRjbzRXRjRRWDJTSW9VaEhYZ2x4ejQ2Z0h0QkRyMFFiaGNFLVE?oc=5>

### A 12-Day Winning Streak Has Accenture Stock Up 35%
- Summary: Extended gains suggest strong momentum and investor confidence.
- Date: 2026-10-23 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNbFRPdzh4RGNBNnBJOTNIVXRQdjV5RUM4dzI3d0RxdFVyWDV2RGgwenRabmNySWctWFhyZkdIM1pvMDdNQXUxb0RLaExZQlJvMlVQRHAtRldGZTktRzgya19MakpjSHpvVHQzLTFiRHNtdmJVYU10bXRaeGpEOXBDSHU0YkVBcGpjLXdIOExMVHNEY1pHMUloYUktbkwtVWM4TExLMEZZVEg3Tkc0S0E?oc=5>

### S&P 500's Worst Stocks Rally: Accenture (ACN) Surges 107.9% Afte
- Summary: Accenture stock surged 107.9% after rallying among S&P 500's worst performers.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxPUXBiT25yMmNsaTlUMEl6d2Zxanc3ZFZhX1puWENtNmY0ekxYV3BRUUZ0LUhnZ0otMjZKXzI3UjJibHpiRFZma1VNQWZNYjFoSTZjSnNQV2xjSDI5bjZJdUtDR1ZtTlk0RjlEMW44aldsaGs4SGRJR0k1bXJaTWNERzh1VTRXajhLUHBCTlFXQ21VQk93OEwyOWhZdGltTnVCRXM1REV6NE1hQk9UUk9PRQ?oc=5>

### Accenture Stock: 11 Straight Green Days, Up 25%
- Summary: Accenture shares rose 25% over 11 consecutive trading days.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOcU1TSFZoNFBoLXJNTFlRM2dWMzd0R2MwbjJNdnY2MklsSkVURVI4c2tOcC1FMW5UMGhveWhidkN2NDdlQ2tEUjU3ZTJBYWg2aGE1SEI5TDVhUmstODZpSUl0QTh4WWpiSWtLb193YUVwQmNyQmFTNFNRTGdNdkl6U296Q3RyTHV5SVp3VlpZTEdIYWh0d1NSQTFQa1RuTDctblJxMnBIYw?oc=5>

### Accenture: 75% Total Return Since July, 23% More By December 2027 (NYSE:ACN)
- Summary: Accenture’s total return has risen 75% since July, with projections of an additional 23% by Dec 2027.
- Date: 2026-10-23 | Impact: medium | Horizon: long | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPWkV3TXZFbXhsN3dBUnRYdmI2UWZmUkJNUm9sMmc2TEZzMXhMaEJfaFBqVjdSOWhBNUl6UVZXODMtb2JUblhyT19oY0RlV2ZRYm1JRUp3c1FoRThIR2pKcEpuREZtcWZGbjBrbG9oQXZ5bFNZN3Rodl9WUUlNMVlMSHBidVl6ZFM1ZENwU0NqYmJ5MVI2QjUxSk04a2txeDVCVEIyQmJrRk5Gam9UczMwTzNsQXdlMGI4cFE?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### What's behind Accenture's latest stock pullback?
- Summary: Accenture's recent stock pullback attributed to market factors and investor sentiment.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPVWVGZko1dXNtUTVHa2JReDhMMjR2Nng4SGhzVWN0RjdSYlg1U3dxWHpnY012SnMyOENkMUxEWlozNjRxcXV5a0pNVndDcUtBREhLejBtWmtfY1Eya1J0WTBwQkRDWkZZTndiNm9lemxXLXlLVl9RSElkTmZ3c013WnMyTDRFcDA0MFRpb3RkbFppZw?oc=5>

### Accenture CEO Buys $3 Million of Stock After Shares Double Off June Lows
- Summary: CEO purchase reflects confidence, boosting stock perception.
- Date: 2026-10-28 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxQQjJqeENUUGZHbDlPYVRFQk5iNEJpQURoSlFWT2FORDJzN09hOUtWdjZGd2huMzJlX2kwVEV6MXIxYm9rVGhRMkVRRkxveFBlSFcyb0xISC1HdVlEMmdQMm5JTG1Kb1FlSVBxSVVuNS1odVpuR0VoMVZpVWVIZEF1Y29R?oc=5>

### Accenture (ACN) vs. CTSH and IBM: Can Valuation Recovery and Dividend Growth Drive the Next Upside?
- Summary: Analyst compares Accenture's valuation recovery and dividend growth potential against competitors.
- Date: 2026-10-27 | Impact: low | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQN29ZdmJ3OFdfTXRLVHNvWnVCa3pCWE5HdlJBRkQ1cUlRcHNSOENSZmg1a2Y1SEhuRDNqdnU0RDA1RTNTZUpWal9xTHJhZVMtdkhDT0wycVI4QjJQX19vMzBHcTNFYmF1NEt4NG1aR2kyRXBmcDVnZHdibGNPaTV5VXAyN0hSLUVWU1llT2x0REpLbEFR?oc=5>

### Accenture (ACN) Chair and CEO Julie Sweet Buys 12,200 Shares
- Summary: CEO share purchase signals strong confidence in company prospects.
- Date: 2026-10-28 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPYXBVR1BaSFhJamNBMlNCbDhoM2J0NTZFaXJKci1iQWM5TVN4THM5bF9OMFBxajhQRjNVVmxvdXhxT0NzRGJIb2hYaGVfM2x2OS1vRVMxQXhhLTFKNXE0RGFabFo5WFpzWHNuMXFqbHZpZTBjeFhCc1NtWHNubGVYczhGQ2JNczd1eGJYRlJoQ0lOS0dEMWhTQW9zSHc?oc=5>

### Zacks Investment Ideas feature highlights: Accenture, Hasbro and MSCI
- Summary: Zacks highlights Accenture among investment ideas alongside Hasbro and MSCI.
- Date: 2026-10-22 | Impact: low | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxObXZIOGJENy1YVmZVZndNUUxRZ202WDdTQlNZbklPTEJYVkw3RGhTaENtRC1mQ2VCTU5UMld5NlJzcmhFcXdYb2hfYzN2clpYUzN4Rkg3QjZZeXZFQUVDNlFzWHdNNlcxdURoamVCWWttbjdTbXhTMklaMDNzWUlKcUQ0ZkVUdks1U09fTndmUVhfSlVWV1k5bS15Z2N5eGhGWUJmT1hRZENSQQ?oc=5>

### Is Accenture PLC (ACN) a Bargain After 4.9% Drop? GF Value Says Undervalued
- Summary: Analyst GF Value labels Accenture undervalued after a 4.9% share drop, implying potential upside for investors.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxOMHhGQmVkNV9uU3VQb0pyZXRnLUVHT1YyMlVtUld6ZjA4MTJxNXRCM25hVFNXQWFOT0NXdGR5c0dESFNOMmdrWDBqemx1dGp4bFlFTTVDaDNCRVRNT0lKVG4yM1JuMnloUkNqT2dxVHlPTlRLckdaY1FhTDdJaDZULTQwZ2ppakZzUnFSanFURTN4UEhROW5XejlXN3VyOTJRWEZqXzRVb0dfRXI1QVE?oc=5>

### Accenture PLC Stock (ACN) Moved Down by 4.41% on Oct 27: Key Drivers Unveiled
- Summary: Accenture shares fell 4.41% on Oct 27 due to identified key drivers.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNT0NCZ21GY2RlNUUyVkVnNEpxbzJJZlFXa0x1RllfcXV4UzlIaGllRlVaa0pJaS1Zb2NPcnBLSWtRdm53d3cySU14Si1tRXVlRmtPNTQwMW5kU2UzeldwMFlJQVpIRkF2MXZ4VE40TjZlcnpraEotWG1uYnhKX0tESkpRYkhxVW5NWUE?oc=5>

### Accenture (ACN) Secures $151.46M Task Order for ICBM Engineering Services
- Summary: Accenture wins a $151.46M contract for ICBM engineering, expanding its defense services portfolio and revenue base.
- Date: 2026-10-28 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQVHhSX0ppTUQzaVNXMkxwMjJ4VFlPQkNTdm9yelE5aEJHblpleV9NY2RLSzdMcmp5S2d6Ykw0M0h6azNtNXlGXzBOVXByWjlTZmpBdUxjTVJQMHpUTmhMRDl0TUlLZnZjenhqeDROMWk0cVc0ckhYR19BV0pmaWJmMjc1cmM3ZFlmX0FTVHc5WDNNTkNRUmhjazVrQ2pwMlUyVTE5djc4Y2NrX0pH?oc=5>

### Accenture (ACN) Gets a Buy from UBS
- Summary: UBS upgrades Accenture to a buy rating, signaling confidence in the company's growth prospects.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxObERaU19RVU9mUG9ubVhZTlQ0MFBZcUs2RUt4enVQcmVMTXBFejg3bkpBN05MajdCby1QYVFBWVFaT21UWjJ5dG9ERDE4WVg3cDFpeW5VbXM3TWthbXAtU3ZIUWNHZk9ibmFIVjUtMk5NUzRXcnBsT3VURUJ2SjNWQVZ2MlppNWhUbGtWM0dzWHUzcEw5U1hhMFBpNjZ5UXZqcF94QXFZLVBUazdZc180Y3RQYWc?oc=5>

### Accenture CEO Julie Sweet Buys $3 Million in Stock as Director Also Purchases Shares
- Summary: CEO Julie Sweet purchased $3M of shares, indicating confidence in the company.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxPMWJ0ZDVWdC1VQUZNOVlDV0d5Ti02cU5tTHBjQkdsdUtNSF9tNUJBZkJrMk1kLTRHR3RnU0dmeG1OYk9UUTlGamtwTmhlR0NWN3JrbXhYdmFKOGlxY1dBS1EwNlp0Rmk3R3Vxck1WZnlCZmpFa0pKTDN4OG54QWtDRUE0TlM1Nmp0cHVtRUoyOTdWSjcxaVowT3BSMUZacF9XbW45TEVtUEplVHZEMVdPcTBOYjVpZnk4d2o0?oc=5>

### Accenture (ACN) Increases Despite Market Slip: Here's What You Need to Know
- Summary: Accenture shares rise amid broader market decline, indicating resilience and potential upside.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOTHpaZ0RYVTJfbm5Hd3JueTYwNDFYZm1pLXpyRExoek5uaTZESUlNSWJPSkc1Mm5tSnd3blBRWjlLSHZqdFdUMWxOQU15dE03SmdPdmFSZ2tSczgxUjJoREZGUW91dG5OZHJlT3FmUDFmVmFQY3dfTDhqZWNrcGFIam9NNi1hcUVJYmRWNThTZWlaLWFfbWRnekYtMmNzc2piQWEyOGhn?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ACN** | **18.23** | **4.66** | **11.05** | **6.20** | **151,284,318,208.00 USD** | **2.66** |
| IBM | 22.04 | 6.87 | 18.09 | 4.70 | 244,105,805,824.00 USD | -14.02 |
| CTSH | 13.45 | 1.95 | 7.24 | 4.50 | 28,161,773,568.00 USD | -10.82 |
| INFY | 15.06 | 9.56 | 21.23 | 1.40 | 49,414,590,464.00 USD | -26.16 |

Peers fetched as_of: 2026-10-29; ACN reuses existing data (market data as_of: 2026-10-29); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-01
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-29

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

- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNYzN3b1o1cG85eDhLaTFlSWw1cTJWUXRoUU9iRnVldzBfbXhRQjBINHFiLTVDWXo5QUx4R1IyTU42NUJVVG9KWFNUX1h6TEJHMWhIMzZXWmE5SmtTZWdnRXdnZVJqQkN1cmZTUmRuNU90c1VjMWFlLUhqam5FTW91V1J0dzV1YXpBZXFuNXVLSnJVMlJZdEptR0xfQk5VYW9vT2N6V0NKSWM?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQWDdRZmdQeFp2NHRYRGZja1duVmNsYm54WlN5bWdMdEsyZUQ4VFFpN3NOR0toUDVFTkg2MEFpWWltb3EzUkw0LXpZbnR5SkcyaGJWWkR6RDJzcUNWdjJFcXJ1aERieWxSc2d5bmNuYzVORWtNNHJvME9MMUx6Vl9BTW1fVk1nMFY2bjh0ZjJOVTNLUjl3U2psdV9MTU1ZRTdwZnFKRHNn?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNNXk1MVNuS3ktZW9oOUFuazFHZkgxU0h6MWhjZ213aGN4d01RZFZJMkY5N3RSTDZXdUVIY1dzYS1LQ3pMeGFvUmYwYjBaWWEyanprTHBReU4ycTI2a2lITlhuOW5sLTRjbzRXRjRRWDJTSW9VaEhYZ2x4ejQ2Z0h0QkRyMFFiaGNFLVE?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNbFRPdzh4RGNBNnBJOTNIVXRQdjV5RUM4dzI3d0RxdFVyWDV2RGgwenRabmNySWctWFhyZkdIM1pvMDdNQXUxb0RLaExZQlJvMlVQRHAtRldGZTktRzgya19MakpjSHpvVHQzLTFiRHNtdmJVYU10bXRaeGpEOXBDSHU0YkVBcGpjLXdIOExMVHNEY1pHMUloYUktbkwtVWM4TExLMEZZVEg3Tkc0S0E?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxPUXBiT25yMmNsaTlUMEl6d2Zxanc3ZFZhX1puWENtNmY0ekxYV3BRUUZ0LUhnZ0otMjZKXzI3UjJibHpiRFZma1VNQWZNYjFoSTZjSnNQV2xjSDI5bjZJdUtDR1ZtTlk0RjlEMW44aldsaGs4SGRJR0k1bXJaTWNERzh1VTRXajhLUHBCTlFXQ21VQk93OEwyOWhZdGltTnVCRXM1REV6NE1hQk9UUk9PRQ?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOcU1TSFZoNFBoLXJNTFlRM2dWMzd0R2MwbjJNdnY2MklsSkVURVI4c2tOcC1FMW5UMGhveWhidkN2NDdlQ2tEUjU3ZTJBYWg2aGE1SEI5TDVhUmstODZpSUl0QTh4WWpiSWtLb193YUVwQmNyQmFTNFNRTGdNdkl6U296Q3RyTHV5SVp3VlpZTEdIYWh0d1NSQTFQa1RuTDctblJxMnBIYw?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPWkV3TXZFbXhsN3dBUnRYdmI2UWZmUkJNUm9sMmc2TEZzMXhMaEJfaFBqVjdSOWhBNUl6UVZXODMtb2JUblhyT19oY0RlV2ZRYm1JRUp3c1FoRThIR2pKcEpuREZtcWZGbjBrbG9oQXZ5bFNZN3Rodl9WUUlNMVlMSHBidVl6ZFM1ZENwU0NqYmJ5MVI2QjUxSk04a2txeDVCVEIyQmJrRk5Gam9UczMwTzNsQXdlMGI4cFE?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPVWVGZko1dXNtUTVHa2JReDhMMjR2Nng4SGhzVWN0RjdSYlg1U3dxWHpnY012SnMyOENkMUxEWlozNjRxcXV5a0pNVndDcUtBREhLejBtWmtfY1Eya1J0WTBwQkRDWkZZTndiNm9lemxXLXlLVl9RSElkTmZ3c013WnMyTDRFcDA0MFRpb3RkbFppZw?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxQQjJqeENUUGZHbDlPYVRFQk5iNEJpQURoSlFWT2FORDJzN09hOUtWdjZGd2huMzJlX2kwVEV6MXIxYm9rVGhRMkVRRkxveFBlSFcyb0xISC1HdVlEMmdQMm5JTG1Kb1FlSVBxSVVuNS1odVpuR0VoMVZpVWVIZEF1Y29R?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQN29ZdmJ3OFdfTXRLVHNvWnVCa3pCWE5HdlJBRkQ1cUlRcHNSOENSZmg1a2Y1SEhuRDNqdnU0RDA1RTNTZUpWal9xTHJhZVMtdkhDT0wycVI4QjJQX19vMzBHcTNFYmF1NEt4NG1aR2kyRXBmcDVnZHdibGNPaTV5VXAyN0hSLUVWU1llT2x0REpLbEFR?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPYXBVR1BaSFhJamNBMlNCbDhoM2J0NTZFaXJKci1iQWM5TVN4THM5bF9OMFBxajhQRjNVVmxvdXhxT0NzRGJIb2hYaGVfM2x2OS1vRVMxQXhhLTFKNXE0RGFabFo5WFpzWHNuMXFqbHZpZTBjeFhCc1NtWHNubGVYczhGQ2JNczd1eGJYRlJoQ0lOS0dEMWhTQW9zSHc?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxObXZIOGJENy1YVmZVZndNUUxRZ202WDdTQlNZbklPTEJYVkw3RGhTaENtRC1mQ2VCTU5UMld5NlJzcmhFcXdYb2hfYzN2clpYUzN4Rkg3QjZZeXZFQUVDNlFzWHdNNlcxdURoamVCWWttbjdTbXhTMklaMDNzWUlKcUQ0ZkVUdks1U09fTndmUVhfSlVWV1k5bS15Z2N5eGhGWUJmT1hRZENSQQ?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxOMHhGQmVkNV9uU3VQb0pyZXRnLUVHT1YyMlVtUld6ZjA4MTJxNXRCM25hVFNXQWFOT0NXdGR5c0dESFNOMmdrWDBqemx1dGp4bFlFTTVDaDNCRVRNT0lKVG4yM1JuMnloUkNqT2dxVHlPTlRLckdaY1FhTDdJaDZULTQwZ2ppakZzUnFSanFURTN4UEhROW5XejlXN3VyOTJRWEZqXzRVb0dfRXI1QVE?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNT0NCZ21GY2RlNUUyVkVnNEpxbzJJZlFXa0x1RllfcXV4UzlIaGllRlVaa0pJaS1Zb2NPcnBLSWtRdm53d3cySU14Si1tRXVlRmtPNTQwMW5kU2UzeldwMFlJQVpIRkF2MXZ4VE40TjZlcnpraEotWG1uYnhKX0tESkpRYkhxVW5NWUE?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQVHhSX0ppTUQzaVNXMkxwMjJ4VFlPQkNTdm9yelE5aEJHblpleV9NY2RLSzdMcmp5S2d6Ykw0M0h6azNtNXlGXzBOVXByWjlTZmpBdUxjTVJQMHpUTmhMRDl0TUlLZnZjenhqeDROMWk0cVc0ckhYR19BV0pmaWJmMjc1cmM3ZFlmX0FTVHc5WDNNTkNRUmhjazVrQ2pwMlUyVTE5djc4Y2NrX0pH?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxObERaU19RVU9mUG9ubVhZTlQ0MFBZcUs2RUt4enVQcmVMTXBFejg3bkpBN05MajdCby1QYVFBWVFaT21UWjJ5dG9ERDE4WVg3cDFpeW5VbXM3TWthbXAtU3ZIUWNHZk9ibmFIVjUtMk5NUzRXcnBsT3VURUJ2SjNWQVZ2MlppNWhUbGtWM0dzWHUzcEw5U1hhMFBpNjZ5UXZqcF94QXFZLVBUazdZc180Y3RQYWc?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxPMWJ0ZDVWdC1VQUZNOVlDV0d5Ti02cU5tTHBjQkdsdUtNSF9tNUJBZkJrMk1kLTRHR3RnU0dmeG1OYk9UUTlGamtwTmhlR0NWN3JrbXhYdmFKOGlxY1dBS1EwNlp0Rmk3R3Vxck1WZnlCZmpFa0pKTDN4OG54QWtDRUE0TlM1Nmp0cHVtRUoyOTdWSjcxaVowT3BSMUZacF9XbW45TEVtUEplVHZEMVdPcTBOYjVpZnk4d2o0?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOTHpaZ0RYVTJfbm5Hd3JueTYwNDFYZm1pLXpyRExoek5uaTZESUlNSWJPSkc1Mm5tSnd3blBRWjlLSHZqdFdUMWxOQU15dE03SmdPdmFSZ2tSczgxUjJoREZGUW91dG5OZHJlT3FmUDFmVmFQY3dfTDhqZWNrcGFIam9NNi1hcUVJYmRWNThTZWlaLWFfbWRnekYtMmNzc2piQWEyOGhn?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
