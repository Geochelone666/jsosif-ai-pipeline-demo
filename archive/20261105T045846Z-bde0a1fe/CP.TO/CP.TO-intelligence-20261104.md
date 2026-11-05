# CP.TO Intelligence Report

- ticker: **CP.TO**
- Report as_of: **2026-11-04**
- Market data as_of: **2026-11-04**
- Quant sources: https://finance.yahoo.com/quote/CP.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CP.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-04**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-05T05:06:44.035627+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 12, 'rule': 3, 'ai': 8, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261104T044411Z-6b13f9ec/CP.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 12 unique headlines; 7 named publishers; 0 exact duplicates; 12 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 131.6800 |
| Return 1D (%) | 3.1005 |
| Return 1W (%) | 4.7574 |
| Return 1M (%) | 7.4851 |
| Return YTD (%) | 31.1519 |
| Return 1Y (%) | 33.4940 |
| Annualized volatility (%) | 22.1528 |
| Beta vs SPY | 0.3981 |
| Max drawdown (%) | -11.9692 |
| Sharpe (rf=0) | 1.4202 |
| Downside deviation (rf=0, %) | 14.5292 |
| Sortino (rf=0) | 2.1654 |
| Historical VaR 95% (1D, %) | 1.8654 |
| Historical ES 95% (1D, %) | 2.9512 |
| Correlation vs SPY | 0.2298 |
| Tracking error vs SPY (%) | 23.0785 |
| P/E (trailing) | 30.41 |
| P/B | 2.50 |
| EV/EBITDA | 16.69 |
| Revenue growth (%) | 15.20 |
| Forward P/E (estimate) | 22.31 |
| Gross margin (%) | 52.76 |
| Operating margin (%) | 38.56 |
| Return on equity (%) | 8.27 |
| Free cash flow yield (%) | 2.39 |
| MA50 | 124.3786 |
| Close vs MA50 (%) | 5.8703 |
| MA200 | 119.3948 |
| Close vs MA200 (%) | 10.2895 |
| RSI (14, Wilder) | 66.7212 |
| MACD (12,26) | 1.3597 |
| MACD signal (9) | 0.6430 |
| MACD histogram | 0.7167 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CP.TO': 274, 'SPY': 275}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 131.6800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 3.1005 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.7574 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.4851 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 31.1519 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 33.4940 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.1528 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.5292 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.1654 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8654 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.9512 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2298 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.0785 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3981 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -11.9692 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.4202 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 22.3096 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 52.7640 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.5640 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 8.2680 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.3926 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 30.4111 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 66.7212 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.7167 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.8703 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 10.2895 -> Clearly above the moving-average trend level.

## TAILWINDS

### Canadian Pacific Kansas City stock gains about 2.5% after stronger Q3 revenue and ongoing Kansas City Southern integration
- Summary: Canadian Pacific Kansas City stock gains about 2.5% after stronger Q3 revenue and ongoing Kansas City Southern integration
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQMHlkV1cxRWxGWjhGbEI3WTRka05OczJNdGhQZ0xLQjFYa3JlX0Zka3A5Sm50VDFqZlBESl8wbDB1ZzAtNm1CTkV0Rnk4c1RBa0JJY19mZUp2YzE5cVVIa0NULTc2Q0lzOEpJTklfZWY2NEo1bGdpUHpIOEpyOWJDUlE3b1czTU5Rc2l1TEFlalBuN0hNa0NB?oc=5>

### Will Canadian Pacific Kansas City stock break higher as upside momentum builds?
- Summary: Positive market sentiment as stock shows potential upward movement.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPUkFTd0lFUXBaYlVocFhHaVNCMDBIdTNHenhxLUVSUEdjSEhTQ29TMXdBUzVSUkVDOE1Veno0Zk9ESVBGVU9DYTdVQzJhdTVNbjhkb015NkRLSm9KbndUUGZydXFFY2toeVUzYUVEak5acFFjSHFsZFBqYXNZWml6clVLLUt5Ty1rZWc?oc=5>

## HEADWINDS

### Canadian Pacific Kansas City stock faces fuel pressure after Q3 growth
- Summary: Canadian Pacific Kansas City stock faces fuel pressure after Q3 growth
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxPZFVEdjVCRUc3eE1iUGJZUHhjczZib05WR2N6cWthQldvOHBvNzliWHBnVm10amNQTjlkZk9QV3pyV0g3N0I5UE9vWXctaDJ2OV9GVm02RHdZM05XaHg0TVVOUWFmdXp6ZkpPbVdTaHRkX2pSLUlhVUpQSW1Yc0x4U1NtbHlBdEMwZnVSMDkycF90enphc1I3eDRESEswem9NZWw0LWNtUHJQX3gwT0xUTjM5VFNxXzQ2ODU3ZGFxYmdfYWYwYzEtbFNjeFhaZw?oc=5>

### Can CPKC (TSX:CP) Maintain Third-Quarter Momentum Amid Higher Operating Expenses?
- Summary: Higher operating expenses may dampen momentum, posing a risk to performance.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPaUx6d0ZKcFZ1YXM4TGlJc3VQN2RlODVZNDV2TFdDMTJ0eFZuSHJZaGF4dm51NWxXeEJJWGhGUE9IcFpPbGtCa0RKQnVDYmU0SmdKbWk4a1pjUFhENUlRRWNqZ1JDeFJleTFDd1ZRS0Jvc2Y3U1Q1MmhtenhYT0Nja2lfbmZ6NVVJalBMV2NrVjRNQklCQnUwX3J1U2RnbmNpa081NWRDUjRNcUw4clVnQ1FjQTlDTUNaZERvd2JR?oc=5>

### Why is Canadian Pacific Kansas City stock sliding today? By Investing.com
- Summary: Current stock slide indicates negative market sentiment and potential downside risk.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNcnRlZ1JiSlFrU2VuTTFQbndJQ3FUMW12eVFZcmFhZTZMTGJVYTZPT2FPbjJNSzUtODhnTndRMHNMLW0ybFoxOElQQzV3bmM3OXJFTUt4VFF3ZWFSbElDWE9pYzBNM05jbjlUbHNnVDFibExJeHBFVFZXQjU3RTBDQmx4cVRha1VOcWFuSHdEeExuVU1zT3hUUlNoUHFpMF9Mb2lvbWN6UHlGemItSUxKQUh1ZTlSQmc?oc=5>

## CATALYSTS

### Canadian Pacific Kansas City stock posts 15% Q3 revenue growth
- Summary: Canadian Pacific Kansas City stock posts 15% Q3 revenue growth
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxOVm1IazNZZkJ2MWJoRkJwOEdEbXNOSHlVN1d5OUR1YmR6cktiT3J4Ni1EMEFyeHBrZFNUWGxuOGNQNHhHOGhpLUd1M0VmT09tWlBJYmZtLVg5V0M4N2dMa1ZmSEZTa2xTZV9WaWh6Nkk3WUtROEpSR3hTWkZjZkZRXzNlRWRQMnJWWFZuVGhtYkFXRDJsUUR2THdueDBxS3dyQmdjUnFWSkxkVDBqLTU4UnVwbUFCczJVQml2MkYzUGsyUQ?oc=5>

### CPKC sets new October grain records in Canada, U.S.
- Summary: CPKC achieves record grain volumes in Oct, boosting freight revenue.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPRFRrc1l2VmxuUmo1SnRQZ21Da1RGbEtaVElXZlI4a0g3Y19IS2NSMG9sQUp1dmpPYXl5aU1mMnY3a3pjdF9SQ1NpQl9rSm9pVXVzaTE4S0luSjFmRzdiQ29YSklPNVl1VXdGMVFZa0pRNlBjRUlRSzNEWnNYWXMyeVlpeEFvcTFmdl9aU19KYm5QRG9ZbXk5TXItNUNjVkxWaE1F?oc=5>

### CPKC (TSX:CP) Stock Faces Q3 Earnings Margin Pressure
- Summary: Q3 earnings margins under pressure, potential impact on profitability.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxNbHRYTkZIb3REZ2xOTC01YkhaX1l4ZXlCN2J4eGFvaW1vTkUxUnZKTXhac0JCT1RWWkMwTVo1cGRqVXd2RTZiUm9tRHp3OXFPTmlFZllNVHB3eG95RW1FOGJFMDh5OWlLX3M3UEs4ZU1CZXNQSlFnVUl0cmJaSnpiTkNlVWFqd0lxMDJkTXhRNzdVa0UySG5HTUNRTGdqd3dwaFMyTktHZVg2a2txUkVoNEVhRlYxc2RHTThqclpFRmhOMlFxeXhWbFd5SUwzMVdnczJ2eGJhazZvNmpfcEHSAeMBQVVfeXFMT3RLOHBvV0p6SmtrWTJhc2N3UC1QTldlbGVYUkkxbmllRENhOHYtSVVMZ0lGTWV3QXFQMzhRUkVweVgydU5vdVNpbWR3bnhzek5BZzlXdEZ4VFVVQk9BM2pCQ1JHMnpIY0U2X24zdDdvY1BTOVk2TThRN2ZJeFJlbUJXWHR2QWFJTXcxRzREM3BCVXg5cUV2XzgtQXlacW50c2ZlU29KREdVSXd2cVNyeGpoT1lDSkVsU3RfWjcyZHZabTFsNDhXWWdRa0s1d2ptMEpYWlpaQ0JzTWN5SVp1cUVNZVU?oc=5>

### Canadian Pacific Kansas City stock: Revenue rises 15 percent amid fuel pressure
- Summary: Revenue up 15% despite fuel cost pressures, indicating operational resilience.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxNa1ZSdUZKSmVtTlZycDlFdWFIN0tocnpSN2t2Z3JMM0R5Tm0xMjBndUtHM2ZySUFUZVpCRkh5ZFNnMUVRaFZuR0QzMi1YNFAtTjc5SFRsem5XaHgxWm85NzNnaXVJUUg5N29UelE1NF9EVF9aRXBKczZ4VndHeXNwTjJHRkdoVWJ1MkQ0dWxxVktDRUtDSW9EQW9fVFY2YmYyNzEzaERCeUo3ZWFYay11S0FMRlZQNXVwWHl2RmE3QzRtMEp5T0F6UjZSWVJKMzdFd0NicHhrT2c?oc=5>

### Is CPKC (TSX:CP) Making Its Cross-Border Rail Network Work Better?
- Summary: Analysis of cross-border network efficiency and its effect on service quality.
- Date: 2026-11-03 | Impact: low | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPTndiZl9iV2M3d21PSWZtU0ZVQ3JSUUhhZ2FCRjR2akNTZzZjbXdseGpfMy1qOGpobjhDQnN1UERKdXNvRE4tcVgyeFJFTjFZTG5wS29XSGhKWFpCdy1PVE4zanRlSkZFdFJjamp0YklDWTdwWTJyZ3dnYTdJZkJsV1cxNllNVXBqQm9LVHhuYzRyVnk0Y1BORTRhd2JmQ2VkTUtNcWNmckF3M2tN?oc=5>

### CPKC reports Q3 growth while Canadian Pacific Kansas City stock costs EUR 78.67
- Summary: Q3 growth reported; stock priced at EUR 78.67, reflecting market valuation.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxQeVZxVm04YmgyRTYzS1g5cG00c3NEeC1DenVtbEJMWk01amU1Rmtxd21uVXQxalNaVUN3dGNleTB0TTRZWHlVcGhrRUtzUF9RMW1kUDdDS1FIQmdSdzFKazUzNDBFSnRfVG02VUZqNm10a2liLU9NZ0hQWk4yVWxWWGswNFhzZXdIZVhKbUFJR1lMRlEwWUUzcHJ3OE5Sd2wtajJHcVlHNjhQRk1qZE1rR201WF9IWUt0Uko3WnlzdGU4bG1qRXRPdU1mclBqN3pjMC1Za1ZMbWIydw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CP.TO** | **30.41** | **2.50** | **16.69** | **15.20** | **114,502,967,296.00 CAD** | **33.49** |
| CNR.TO | 22.67 | 4.94 | 13.98 | 14.60 | 108,209,864,704.00 CAD | 36.91 |
| UNP | 23.66 | 8.33 | 15.91 | 15.30 | 183,290,118,144.00 USD | 42.61 |
| NSC | 28.58 | 4.62 | 16.03 | 13.60 | 77,299,589,120.00 USD | 23.40 |

Peers fetched as_of: 2026-11-04; CP.TO reuses existing data (market data as_of: 2026-11-04); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

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
- Filing date: 2026-10-29
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: https://www.sec.gov/Archives/edgar/data/16875/000001687526000033/cp-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilwFBVV95cUxQMHlkV1cxRWxGWjhGbEI3WTRka05OczJNdGhQZ0xLQjFYa3JlX0Zka3A5Sm50VDFqZlBESl8wbDB1ZzAtNm1CTkV0Rnk4c1RBa0JJY19mZUp2YzE5cVVIa0NULTc2Q0lzOEpJTklfZWY2NEo1bGdpUHpIOEpyOWJDUlE3b1czTU5Rc2l1TEFlalBuN0hNa0NB?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPUkFTd0lFUXBaYlVocFhHaVNCMDBIdTNHenhxLUVSUEdjSEhTQ29TMXdBUzVSUkVDOE1Veno0Zk9ESVBGVU9DYTdVQzJhdTVNbjhkb015NkRLSm9KbndUUGZydXFFY2toeVUzYUVEak5acFFjSHFsZFBqYXNZWml6clVLLUt5Ty1rZWc?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxPZFVEdjVCRUc3eE1iUGJZUHhjczZib05WR2N6cWthQldvOHBvNzliWHBnVm10amNQTjlkZk9QV3pyV0g3N0I5UE9vWXctaDJ2OV9GVm02RHdZM05XaHg0TVVOUWFmdXp6ZkpPbVdTaHRkX2pSLUlhVUpQSW1Yc0x4U1NtbHlBdEMwZnVSMDkycF90enphc1I3eDRESEswem9NZWw0LWNtUHJQX3gwT0xUTjM5VFNxXzQ2ODU3ZGFxYmdfYWYwYzEtbFNjeFhaZw?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPaUx6d0ZKcFZ1YXM4TGlJc3VQN2RlODVZNDV2TFdDMTJ0eFZuSHJZaGF4dm51NWxXeEJJWGhGUE9IcFpPbGtCa0RKQnVDYmU0SmdKbWk4a1pjUFhENUlRRWNqZ1JDeFJleTFDd1ZRS0Jvc2Y3U1Q1MmhtenhYT0Nja2lfbmZ6NVVJalBMV2NrVjRNQklCQnUwX3J1U2RnbmNpa081NWRDUjRNcUw4clVnQ1FjQTlDTUNaZERvd2JR?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNcnRlZ1JiSlFrU2VuTTFQbndJQ3FUMW12eVFZcmFhZTZMTGJVYTZPT2FPbjJNSzUtODhnTndRMHNMLW0ybFoxOElQQzV3bmM3OXJFTUt4VFF3ZWFSbElDWE9pYzBNM05jbjlUbHNnVDFibExJeHBFVFZXQjU3RTBDQmx4cVRha1VOcWFuSHdEeExuVU1zT3hUUlNoUHFpMF9Mb2lvbWN6UHlGemItSUxKQUh1ZTlSQmc?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxOVm1IazNZZkJ2MWJoRkJwOEdEbXNOSHlVN1d5OUR1YmR6cktiT3J4Ni1EMEFyeHBrZFNUWGxuOGNQNHhHOGhpLUd1M0VmT09tWlBJYmZtLVg5V0M4N2dMa1ZmSEZTa2xTZV9WaWh6Nkk3WUtROEpSR3hTWkZjZkZRXzNlRWRQMnJWWFZuVGhtYkFXRDJsUUR2THdueDBxS3dyQmdjUnFWSkxkVDBqLTU4UnVwbUFCczJVQml2MkYzUGsyUQ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPRFRrc1l2VmxuUmo1SnRQZ21Da1RGbEtaVElXZlI4a0g3Y19IS2NSMG9sQUp1dmpPYXl5aU1mMnY3a3pjdF9SQ1NpQl9rSm9pVXVzaTE4S0luSjFmRzdiQ29YSklPNVl1VXdGMVFZa0pRNlBjRUlRSzNEWnNYWXMyeVlpeEFvcTFmdl9aU19KYm5QRG9ZbXk5TXItNUNjVkxWaE1F?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxNbHRYTkZIb3REZ2xOTC01YkhaX1l4ZXlCN2J4eGFvaW1vTkUxUnZKTXhac0JCT1RWWkMwTVo1cGRqVXd2RTZiUm9tRHp3OXFPTmlFZllNVHB3eG95RW1FOGJFMDh5OWlLX3M3UEs4ZU1CZXNQSlFnVUl0cmJaSnpiTkNlVWFqd0lxMDJkTXhRNzdVa0UySG5HTUNRTGdqd3dwaFMyTktHZVg2a2txUkVoNEVhRlYxc2RHTThqclpFRmhOMlFxeXhWbFd5SUwzMVdnczJ2eGJhazZvNmpfcEHSAeMBQVVfeXFMT3RLOHBvV0p6SmtrWTJhc2N3UC1QTldlbGVYUkkxbmllRENhOHYtSVVMZ0lGTWV3QXFQMzhRUkVweVgydU5vdVNpbWR3bnhzek5BZzlXdEZ4VFVVQk9BM2pCQ1JHMnpIY0U2X24zdDdvY1BTOVk2TThRN2ZJeFJlbUJXWHR2QWFJTXcxRzREM3BCVXg5cUV2XzgtQXlacW50c2ZlU29KREdVSXd2cVNyeGpoT1lDSkVsU3RfWjcyZHZabTFsNDhXWWdRa0s1d2ptMEpYWlpaQ0JzTWN5SVp1cUVNZVU?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxNa1ZSdUZKSmVtTlZycDlFdWFIN0tocnpSN2t2Z3JMM0R5Tm0xMjBndUtHM2ZySUFUZVpCRkh5ZFNnMUVRaFZuR0QzMi1YNFAtTjc5SFRsem5XaHgxWm85NzNnaXVJUUg5N29UelE1NF9EVF9aRXBKczZ4VndHeXNwTjJHRkdoVWJ1MkQ0dWxxVktDRUtDSW9EQW9fVFY2YmYyNzEzaERCeUo3ZWFYay11S0FMRlZQNXVwWHl2RmE3QzRtMEp5T0F6UjZSWVJKMzdFd0NicHhrT2c?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPTndiZl9iV2M3d21PSWZtU0ZVQ3JSUUhhZ2FCRjR2akNTZzZjbXdseGpfMy1qOGpobjhDQnN1UERKdXNvRE4tcVgyeFJFTjFZTG5wS29XSGhKWFpCdy1PVE4zanRlSkZFdFJjamp0YklDWTdwWTJyZ3dnYTdJZkJsV1cxNllNVXBqQm9LVHhuYzRyVnk0Y1BORTRhd2JmQ2VkTUtNcWNmckF3M2tN?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxQeVZxVm04YmgyRTYzS1g5cG00c3NEeC1DenVtbEJMWk01amU1Rmtxd21uVXQxalNaVUN3dGNleTB0TTRZWHlVcGhrRUtzUF9RMW1kUDdDS1FIQmdSdzFKazUzNDBFSnRfVG02VUZqNm10a2liLU9NZ0hQWk4yVWxWWGswNFhzZXdIZVhKbUFJR1lMRlEwWUUzcHJ3OE5Sd2wtajJHcVlHNjhQRk1qZE1rR201WF9IWUt0Uko3WnlzdGU4bG1qRXRPdU1mclBqN3pjMC1Za1ZMbWIydw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
