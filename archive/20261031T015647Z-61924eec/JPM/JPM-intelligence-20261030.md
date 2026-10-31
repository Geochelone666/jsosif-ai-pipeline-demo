# JPM Intelligence Report

- ticker: **JPM**
- Report as_of: **2026-10-30**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/JPM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/JPM/key-statistics/
- AI analysis snapshot as_of: **2026-10-30**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-31T02:23:35.729373+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 9, 'ai': 10, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261030T021807Z-b9de7146/JPM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 9 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 60.0%; oldest publication 2026-10-25

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 337.0400 |
| Return 1D (%) | -1.9035 |
| Return 1W (%) | 1.6467 |
| Return 1M (%) | 2.3854 |
| Return YTD (%) | 6.6139 |
| Return 1Y (%) | 11.0171 |
| Annualized volatility (%) | 22.1062 |
| Beta vs SPY | 0.7482 |
| Max drawdown (%) | -15.4717 |
| Sharpe (rf=0) | 0.5852 |
| Downside deviation (rf=0, %) | 15.9965 |
| Sortino (rf=0) | 0.8087 |
| Historical VaR 95% (1D, %) | 2.3879 |
| Historical ES 95% (1D, %) | 3.2600 |
| Correlation vs SPY | 0.4329 |
| Tracking error vs SPY (%) | 20.1862 |
| P/E (trailing) | 14.14 |
| P/B | 2.55 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 10.20 |
| Forward P/E (estimate) | 13.20 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 42.58 |
| Return on equity (%) | 18.01 |
| Free cash flow yield (%) | N/A |
| MA50 | 342.2142 |
| Close vs MA50 (%) | -1.5120 |
| MA200 | 320.3024 |
| Close vs MA200 (%) | 5.2256 |
| RSI (14, Wilder) | 49.5854 |
| MACD (12,26) | -0.5271 |
| MACD signal (9) | -1.7185 |
| MACD histogram | 1.1914 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'JPM': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 337.0400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.9035 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.6467 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.3854 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 6.6139 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 11.0171 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.1062 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 15.9965 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.8087 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.3879 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.2600 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4329 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.1862 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.7482 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.4717 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5852 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 13.2011 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 42.5840 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 18.0130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 14.1376 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 49.5854 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.1914 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -1.5120 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 5.2256 -> Clearly above the moving-average trend level.

## TAILWINDS

### JPM Stock Gains 0.52%, Testing Key: Full Details
- Summary: JPM Stock Gains 0.52%, Testing Key: Full Details
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNc2lLY2s0SjBQZ2R6a2JRNmJXcy1rY3Z5SzJxcjZrMVlDcXExWnlNT2JDeEEtT1Zwa1B1VjJyckxpeG9tX0pOZXVFVlJwNnRyOFNOYkhqVmVRRVVWRmtyOC1lYVZGS0htSTNoOF9zX3Azd0FRWW5CdFBJRlBnT2lsU0owTVR0SGJiYklNYTIwX21YbUlsVEE?oc=5>

### JPMorgan Chase & Co. (NYSE:JPM) Stock Jumps 1.3% - Here's What Happened
- Summary: JPMorgan Chase & Co. (NYSE:JPM) Stock Jumps 1.3% - Here's What Happened
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxQUkJ4WmtfOUVNSmVqNE5wWTRoelpORGlRQUhCTUpsVUhmYlN2OUdfVmZDeUo4ZExqNFFBMEptQVNtR1pLVENjeDBHbzItRjh5b0ZMb3dJc0J6RU5YeFFhNTBDYk9VRXpmMXdMTHlwTFRTLWZ2dXdVMWRjNGF5NmVDeklrVVBrVl9GaFJ2MWxwU1lfeUpMYWdGd3RBOXoxa1hhQ3JwR1N2MC1zUFJwRWcyU3hqeVlnVHdWejlOV3Bn?oc=5>

### JPMorgan (JPM) Stock Could Be 33% Undervalued Following JPM Coin Expansion
- Summary: JPM Coin expansion may boost JPM stock, suggesting undervaluation.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNaU9vbG5tendjbUhPc05YeUpNSjN0MDMyTWswQzFkd1g1NWppUUJxeWlfVEpVQmVlTDF6Z2NsLU52NGxnaVl5bDdNYWRvNVQ0WjZNbnZRZVlQcjRRd2FRU3o0WFpmbHJQR2toVDB4Vm9LLXV1c0Z5NXliRnhSYThKVVF1N25UdmdBT2xlQW9fUGtwMVpUOTdz?oc=5>

### Is JPMorgan Chase (JPM) Undervalued As Bond Issuance And Earnings Strength Meet A Pullback?
- Summary: Bond issuance and earnings strength hint at undervaluation.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxQQWdlQWJZZE1LUzdSdVVuRHlmZmJtMVZTdE1ZcTVJRUJrTF9SdGxTWFpxdGNwQkQtenVtNW1JdS1KS0JxSlJpWDNZQ01YMFBBZFlwRXVDR3FyRUc5NkVZV0R5aVZ6dloyMGtwUm1VMHBJLVkxSjJFZnc5elF6VWhqM2F2ZDhJWE9SN01MNUU2TVA4cHFCMmtiWC1SRGVpeTUxczVHRzdqQU9uYnRjYTB0RTdzWlF1U0J4aEs5MElMYXo2cS1PaXfSAcsBQVVfeXFMTk5uY1ZmZmk4bkxka3JUUmw1UlFoWi1FQ3RyUGtDMWxXUGdzR1d3S043R2J2aVA2X3RYTW1VdDh4SzVFS3dETk9YbmwwX20waDg4dnZWREpxQm5iVzNnazZjVFByV0VDOWVaeDFWZEVrcldfblkwdjg0M0xpZE85TXpMUVZTZEhpX0pLOG5Bb1BVeGJvZW1ZNUMydnFuZXY3MVp5MnFPQ1VFR2tVSnpjbG1jOEtFVUZnSlFkVlJLbHpOZVBjVE1GalNMdEE?oc=5>

## HEADWINDS

### JPMorgan Chase & Co. (NYSE:JPM) Shares Down 1.9% - Here's Why
- Summary: JPMorgan Chase & Co. (NYSE:JPM) Shares Down 1.9% - Here's Why
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxONjItaEJtcUNLWXd2Rk5DZzRXcDFLQXY4WWo3dEZrLWlHaTl6WmZiU2NwQ2s1bjFza0xuLTJycHFYbkpzMzE5LUhGNExJelRlUjNBWE9tRG9zVzdPQW90X2xqRWJXY1dSQ21BdlRib0FyOWM2Mm1FdE9BNDIzY09xU01TMkhuRXpKWW0zZUFBdXFmLWdTOGk2UE1YM24tX0NFMThCUjBJRlFncUtWcmV3RQ?oc=5>

## CATALYSTS

### JPMorgan Chase & Co. $JPM Shares Bought by Simplicity Wealth LLC
- Summary: JPMorgan Chase & Co. $JPM Shares Bought by Simplicity Wealth LLC
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxOM0Q5clM5emdZTjdjZU95SE9zeHdiSHhyT01Ha1BjN1dzRWk0MF81akNSVkpJbEhVaGhNamtoTVJtUmRadTdHQm83aHIxYW5XVkdCaXhSb3M5MG43OE4wREpOVzNjT3pOZ2NaMllDLVpFc0FiSkw0VXlBNXd1S0c3TGZBcTFkN0hiX0N1cWMtV3o1QWctbDNxdDloVVlPazk4MnRvOUZsNlljdWdHbEEyXzlBejF1VkZpZHBVSVNn?oc=5>

### JPMorgan Chase & Co. $JPM Stock Sold by Baypointe Partners LLC
- Summary: JPMorgan Chase & Co. $JPM Stock Sold by Baypointe Partners LLC
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxOSnE5SW1jb0VUZ2Y2SjJiLVFWLVl0cVJ5a0l6TW1BYk1lc3EyeU83ZkFoQU1xSk5XeVNPbU5uZERPTmJqeEY5WmRsWFZ6VXYtVmVPdy0xTlctdGNZWU95bDJPcEoxdDFsd0RHSXpUYkN6VlA4TkVENFc3MEg2UE1GcW5KalVweW5PUy0xOUo1NzJYRG0xZUxlajRGcWlCSGpaekk5UGpJWE9fMnJySU00Vjh4akZHQXlPREVB?oc=5>

### JPMorgan Chase & Co. (NYSE:JPM) Stock Has Average Price Target of $368.10
- Summary: JPMorgan Chase & Co. (NYSE:JPM) Stock Has Average Price Target of $368.10
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPcld3RmNSdENHSUlneUZGT2tLTlRnMllveGxtZ2I0VHB6ZnBmWmQyQU5YQjN6WTF1dnF4R3BGajctOTBiLW4zbjNuNEx2cmhJYmp4Snl2YXVBRlVvZWZPTzVybXI3T0ZWN3FhenZpaWwxRUJNaHg3b29NejhSTjlwNDJod19NU3pfSjBkdVMzdFVGX1ZfVVJ5aE11aThDRlExbnphY0h5N1ltMzNiNHlhVFpxZEM5MkRTemhzSGU2RlJzaFE5MktwaW5n?oc=5>

### JPMorgan Chase & Co. $JPM Stock Sold by Arvest Investments Inc.
- Summary: JPMorgan Chase & Co. $JPM Stock Sold by Arvest Investments Inc.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxPMHhtUGxlUnBQcWJhTC1BdnZtaS1TMnJJUVpqZkQ2VkhpWDZ5OUlXWUJQRnpOM0pROXhwZXQ3TlFvZkE0cnhxbTgyc2ROczFZNHROWG5UUU5BTUQ5YWVzSnNyWW11YUt4d1pQTGpqU2diUy1JNmtTU1NrWWI5VVoyd2VZam5OQVhpNnBTRTVidTI5OWdOZU5sOEZFcDJUNGZWLUg3Y0M1aGJvenZCVTgzY09SclRlSEZ3b0Jz?oc=5>

### JPMorgan Chase & Co. $JPM Stock Sold by Hosking Partners LLP
- Summary: JPMorgan Chase & Co. $JPM Stock Sold by Hosking Partners LLP
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPTVBTZmJ3Vk9acUQ5M09uVjA3V3plM0xwOWhkcURiVkl6cE5WY2JMbXUyTmkwTkE1RmltaGM4MkQ2VzVsYl9xdkhBbS03NGh3OTY4UllVSkpzbWVocWpkcElOQTQxQ1hDQUs3cG4xdzlwQThOMjZ5RU1KYVVfZEY1MFFLSWhvMVNoeGJzWHZQcHBESlVfSXc0LThNLWMyd2hjQTBVXzg2VXlFamh4bW5WcW5STm5nMGlt?oc=5>

### JPMorgan Chase & Co. $JPM Stock: Sepio Capital LP Cuts Position
- Summary: JPMorgan Chase & Co. $JPM Stock: Sepio Capital LP Cuts Position
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxQMVlPYy0yYS1wM2ZPYy1rVngtaDRzZmRmenlNNUZoeTIzY2xDNmpvb3NINV9TR3RRdHJZTVJkLUpuRHZGa0VMUWJZaXk0WWVfa3BtZUd0bWhjb09aS05ZUDdhbTYyb0V5WHhkNTZiNExYcTVZQkE1MmpRcmJtVVltMUpxdEpSaEpPWE41MFBjcWhTZkpqTENyU2RyUkdBb0kwSms5cHlIdzYxdDVkNmxwY1hFbVVkSG9ZR3Nn?oc=5>

### JPMorgan Chase Says That Bitcoin Will Outperform Stocks, Bonds, and Gold Over the Next 10 Years. Here's Why It Might Be Right
- Summary: JPM predicts Bitcoin will outperform traditional assets over a decade.
- Date: 2026-10-27 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQekswYkZxS2I1RXFzQ0w3Y0QtZlF4X1FrRzIxdlFzZEtrNGlISXowbzV2cVBwWGcwcUg2d1hlbkZYeDExMTNycGNKWjRCd2syUndfZ2pWNGRMbDBoNjcwZGZIQkxKdGdyYXZLdUZkWHR4blFxRE9ld0NmWkw0akFOa3BnOFNuMjlTaE9QbzlmX05uaU5UVFhOZg?oc=5>

### JPMorgan to lead Anthropic's U.S. retail IPO offering - report (ANT:Pending)
- Summary: JPMorgan is set to lead Anthropic’s U.S. retail IPO, positioning the bank as a key underwriter for the AI firm’s public debut.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOdEFrNlV2MlJVWEh5LWM1ZFdVcHBaSDhqdk15Y2UxUVdCSUEtaGI1QmE1TmhhVmtGelJ4a3U2cVp6bHJBS0ZwZTJZSnQwSGJxdXhRamxhVV9DTnhtTmM3bUsta3ZUYnROT3RzRjE3bTNQRGVfX1ZiR3lOME9fX2FjRlBzU3EyclB6QUlIT1FQT0tWVEFFWkNlbE1YX01DZw?oc=5>

### JPMorgan Raises NII Outlook: Is JPM Stock Too Expensive?
- Summary: JPMorgan lifts its net interest income outlook, signaling stronger future earnings.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPRjh5WlY0dUdDSy1HSzdSM0pVQVVRLUlpbS0xMThXZDRYVzUzYTdQb0Q3OVh3R1ZGTm1ueWd5XzUzNWE3X3VjemIyZTV4SHJKRWhoeVoteDI1RDV2c1JFWk53Y0J4ZWtBR09VcEkzTC14dTNxTUNBcHNCRmlSa0VZMXByQ3V0cmtWRGNCdy01cEJ6Vmh1OF84Q0Q2UzFOTmpTVW1INFBvR2dLQUc1Qk9N?oc=5>

### JPMorgan Chase & Co. $JPM Shares Newly Purchased by Norris Perne & French LLP MI
- Summary: Shares of JPM acquired by Norris Perne & French LLP MI.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxNSlpSWXQzejNTajgzM3Rvc1hNREhScVpYNDluTmdad01SN1ZtM2xodWJRcWk2aGFiMDBuVGdSR2d2Ukc5NndOeHFoWUd4V1RWQ1o5OGU0djR0dUFCWGRDMnR6QXJ2NHJlRFo5aVN0b3V4WHE2UHR1NGpFaWdUVUR6QzNLRjI5TWdMVy1vcUQ3eWg0ZzRrXzk1VWQtekQ4Z01OaENURVFYYXRZY1hOMXUtNGV3T3c0VlNDandkN2lXSlQtSGUzMnVmNDhUcjBVU3Jo?oc=5>

### JPMorgan Chase & Co. $JPM Stock Position Trimmed by Anderson Hoagland & Co.
- Summary: Anderson Hoagland & Co. reduced its JPM holdings.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxPaTlpeE1xeHViLVlyVGNDTC1peVlRSVE0X3BQbEdOcVl3aGtCUDd0TWJRU05KZTViWXpfM0xxMVdDWWZHakVsWHlmRzhEcTJTYzVCYVR2Ynk3cUJ3amU4Z2V1MDZxbk5nSUt2R3JpcXpYY2J5VmlPbGpjVFdkWXpaU2hTMC1lMzdIeE9CSGtTbVdDYmtaWVZqRGNUb0hrbl9zZjBmQWVSQmlLQUJaUmlJbS1HQ19kSUtvYXZ2NFA1dkxfc0FWazhYSg?oc=5>

### 7,816 JPMorgan Chase & Co. $JPM Shares Purchased by BG Investment Services LLC
- Summary: BG Investment Services LLC bought 7,816 JPM shares.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxNSHNyXzF3dngxZ2xlY2Jjc2xwZ0gxa0N1NDA1b2NmWE1jVkpIbno0aFE0SjRsVC0ybEhGWDN2d2lQN3B2UXZkcEFUMXpGcVphVF9HS29UTTdONG12VjQ4RjZLa2J4b1NBc25NRkdiZW1LSUVPZUU0QkZnV2k1N1V4RzI1VFBFbFlweXJZVWNCc3U2TVgyWXRsTU1UZUNJTWJLUGhRejJhZFllTHhxWWpWcUtvMkVYbWNhSGxjam1lZEI2elRMWGxwR0lFaXFxdGM?oc=5>

### JPMorgan Chase & Co. $JPM Position Lessened by Brookmont Capital Management
- Summary: Brookmont Capital Management decreased its JPM position.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxPTGM2NUlSMnpoeEtVU0xIdXZLVWc5Q3djMmtiNy1PT0gzcjRFdlR0cVBOSEZWd1B0YTFMUUw3YUQ3OXFkRllzZXktN0U0Ui1lYUZVcXpGdGQ4MnhJNlVnOXVfekdzTXhDYXdGWW9mX0gyekc3QTkyLWJsYml3eV9mUGpaTjllTkIyaGFhV0hBcFZxbkl5NXBCRjZ5Yk5LdzlrRXN6TWxjbGV2RVlObnhMS1VmQjZNUEJCOVlLeThxbFpLVm5SZnZ4cnlJZUQ?oc=5>

### 6,567 JPMorgan Chase & Co. $JPM Shares Sold by OLD Second National Bank of Aurora
- Summary: OLD Second National Bank of Aurora sold 6,567 JPM shares.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxNaEtNWVpCQ2hSNnFOLVBadW1DcG53NkFPdEJBM2o5RkFUWGZyZmxHZkd3d0Q4QVZLbHg3OGVHYUxmRWU5Y2I2VmNpLXpfVmo2aXBWVXFUUHFESEE0ZzVIc3FBUFhIYVpIYWVLcFVDQzIzVmVrbFhzOGliWU5wQlRzakVDS2k2T2REaHY0UU5RNFA4SFFzWW54YjU3aldrVHhLdEhnUzRhbWNKbHNoOXE0eFRHb2x2Y1ZuRkwwWUU1VmNwZElsTTN6c1FvTWk0TEsyZ3ZF?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **JPM** | **14.14** | **2.55** | **N/A** | **10.20** | **895,043,502,080.00 USD** | **11.02** |
| BAC | 11.94 | 1.27 | N/A | 7.10 | 346,203,979,776.00 USD | -3.68 |
| C | 11.95 | 1.06 | N/A | 8.00 | 202,993,729,536.00 USD | 24.96 |
| WFC | 11.76 | 1.58 | N/A | 0.40 | 250,354,319,360.00 USD | -0.90 |

Peers fetched as_of: 2026-10-30; JPM reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-13
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

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
- Filing date: 2026-08-06
- Revenue (latest available single quarter): 24,246,000,000.00 USD; period 2014-07-01/2014-09-30; fiscal year/reporting period 2014/Q3
- Net income (latest available single quarter): 21,155,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/19617/000162828026054343/jpm-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilgFBVV95cUxNc2lLY2s0SjBQZ2R6a2JRNmJXcy1rY3Z5SzJxcjZrMVlDcXExWnlNT2JDeEEtT1Zwa1B1VjJyckxpeG9tX0pOZXVFVlJwNnRyOFNOYkhqVmVRRVVWRmtyOC1lYVZGS0htSTNoOF9zX3Azd0FRWW5CdFBJRlBnT2lsU0owTVR0SGJiYklNYTIwX21YbUlsVEE?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxQUkJ4WmtfOUVNSmVqNE5wWTRoelpORGlRQUhCTUpsVUhmYlN2OUdfVmZDeUo4ZExqNFFBMEptQVNtR1pLVENjeDBHbzItRjh5b0ZMb3dJc0J6RU5YeFFhNTBDYk9VRXpmMXdMTHlwTFRTLWZ2dXdVMWRjNGF5NmVDeklrVVBrVl9GaFJ2MWxwU1lfeUpMYWdGd3RBOXoxa1hhQ3JwR1N2MC1zUFJwRWcyU3hqeVlnVHdWejlOV3Bn?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNaU9vbG5tendjbUhPc05YeUpNSjN0MDMyTWswQzFkd1g1NWppUUJxeWlfVEpVQmVlTDF6Z2NsLU52NGxnaVl5bDdNYWRvNVQ0WjZNbnZRZVlQcjRRd2FRU3o0WFpmbHJQR2toVDB4Vm9LLXV1c0Z5NXliRnhSYThKVVF1N25UdmdBT2xlQW9fUGtwMVpUOTdz?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxQQWdlQWJZZE1LUzdSdVVuRHlmZmJtMVZTdE1ZcTVJRUJrTF9SdGxTWFpxdGNwQkQtenVtNW1JdS1KS0JxSlJpWDNZQ01YMFBBZFlwRXVDR3FyRUc5NkVZV0R5aVZ6dloyMGtwUm1VMHBJLVkxSjJFZnc5elF6VWhqM2F2ZDhJWE9SN01MNUU2TVA4cHFCMmtiWC1SRGVpeTUxczVHRzdqQU9uYnRjYTB0RTdzWlF1U0J4aEs5MElMYXo2cS1PaXfSAcsBQVVfeXFMTk5uY1ZmZmk4bkxka3JUUmw1UlFoWi1FQ3RyUGtDMWxXUGdzR1d3S043R2J2aVA2X3RYTW1VdDh4SzVFS3dETk9YbmwwX20waDg4dnZWREpxQm5iVzNnazZjVFByV0VDOWVaeDFWZEVrcldfblkwdjg0M0xpZE85TXpMUVZTZEhpX0pLOG5Bb1BVeGJvZW1ZNUMydnFuZXY3MVp5MnFPQ1VFR2tVSnpjbG1jOEtFVUZnSlFkVlJLbHpOZVBjVE1GalNMdEE?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxONjItaEJtcUNLWXd2Rk5DZzRXcDFLQXY4WWo3dEZrLWlHaTl6WmZiU2NwQ2s1bjFza0xuLTJycHFYbkpzMzE5LUhGNExJelRlUjNBWE9tRG9zVzdPQW90X2xqRWJXY1dSQ21BdlRib0FyOWM2Mm1FdE9BNDIzY09xU01TMkhuRXpKWW0zZUFBdXFmLWdTOGk2UE1YM24tX0NFMThCUjBJRlFncUtWcmV3RQ?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxOM0Q5clM5emdZTjdjZU95SE9zeHdiSHhyT01Ha1BjN1dzRWk0MF81akNSVkpJbEhVaGhNamtoTVJtUmRadTdHQm83aHIxYW5XVkdCaXhSb3M5MG43OE4wREpOVzNjT3pOZ2NaMllDLVpFc0FiSkw0VXlBNXd1S0c3TGZBcTFkN0hiX0N1cWMtV3o1QWctbDNxdDloVVlPazk4MnRvOUZsNlljdWdHbEEyXzlBejF1VkZpZHBVSVNn?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxOSnE5SW1jb0VUZ2Y2SjJiLVFWLVl0cVJ5a0l6TW1BYk1lc3EyeU83ZkFoQU1xSk5XeVNPbU5uZERPTmJqeEY5WmRsWFZ6VXYtVmVPdy0xTlctdGNZWU95bDJPcEoxdDFsd0RHSXpUYkN6VlA4TkVENFc3MEg2UE1GcW5KalVweW5PUy0xOUo1NzJYRG0xZUxlajRGcWlCSGpaekk5UGpJWE9fMnJySU00Vjh4akZHQXlPREVB?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPcld3RmNSdENHSUlneUZGT2tLTlRnMllveGxtZ2I0VHB6ZnBmWmQyQU5YQjN6WTF1dnF4R3BGajctOTBiLW4zbjNuNEx2cmhJYmp4Snl2YXVBRlVvZWZPTzVybXI3T0ZWN3FhenZpaWwxRUJNaHg3b29NejhSTjlwNDJod19NU3pfSjBkdVMzdFVGX1ZfVVJ5aE11aThDRlExbnphY0h5N1ltMzNiNHlhVFpxZEM5MkRTemhzSGU2RlJzaFE5MktwaW5n?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxPMHhtUGxlUnBQcWJhTC1BdnZtaS1TMnJJUVpqZkQ2VkhpWDZ5OUlXWUJQRnpOM0pROXhwZXQ3TlFvZkE0cnhxbTgyc2ROczFZNHROWG5UUU5BTUQ5YWVzSnNyWW11YUt4d1pQTGpqU2diUy1JNmtTU1NrWWI5VVoyd2VZam5OQVhpNnBTRTVidTI5OWdOZU5sOEZFcDJUNGZWLUg3Y0M1aGJvenZCVTgzY09SclRlSEZ3b0Jz?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPTVBTZmJ3Vk9acUQ5M09uVjA3V3plM0xwOWhkcURiVkl6cE5WY2JMbXUyTmkwTkE1RmltaGM4MkQ2VzVsYl9xdkhBbS03NGh3OTY4UllVSkpzbWVocWpkcElOQTQxQ1hDQUs3cG4xdzlwQThOMjZ5RU1KYVVfZEY1MFFLSWhvMVNoeGJzWHZQcHBESlVfSXc0LThNLWMyd2hjQTBVXzg2VXlFamh4bW5WcW5STm5nMGlt?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxQMVlPYy0yYS1wM2ZPYy1rVngtaDRzZmRmenlNNUZoeTIzY2xDNmpvb3NINV9TR3RRdHJZTVJkLUpuRHZGa0VMUWJZaXk0WWVfa3BtZUd0bWhjb09aS05ZUDdhbTYyb0V5WHhkNTZiNExYcTVZQkE1MmpRcmJtVVltMUpxdEpSaEpPWE41MFBjcWhTZkpqTENyU2RyUkdBb0kwSms5cHlIdzYxdDVkNmxwY1hFbVVkSG9ZR3Nn?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQekswYkZxS2I1RXFzQ0w3Y0QtZlF4X1FrRzIxdlFzZEtrNGlISXowbzV2cVBwWGcwcUg2d1hlbkZYeDExMTNycGNKWjRCd2syUndfZ2pWNGRMbDBoNjcwZGZIQkxKdGdyYXZLdUZkWHR4blFxRE9ld0NmWkw0akFOa3BnOFNuMjlTaE9QbzlmX05uaU5UVFhOZg?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOdEFrNlV2MlJVWEh5LWM1ZFdVcHBaSDhqdk15Y2UxUVdCSUEtaGI1QmE1TmhhVmtGelJ4a3U2cVp6bHJBS0ZwZTJZSnQwSGJxdXhRamxhVV9DTnhtTmM3bUsta3ZUYnROT3RzRjE3bTNQRGVfX1ZiR3lOME9fX2FjRlBzU3EyclB6QUlIT1FQT0tWVEFFWkNlbE1YX01DZw?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPRjh5WlY0dUdDSy1HSzdSM0pVQVVRLUlpbS0xMThXZDRYVzUzYTdQb0Q3OVh3R1ZGTm1ueWd5XzUzNWE3X3VjemIyZTV4SHJKRWhoeVoteDI1RDV2c1JFWk53Y0J4ZWtBR09VcEkzTC14dTNxTUNBcHNCRmlSa0VZMXByQ3V0cmtWRGNCdy01cEJ6Vmh1OF84Q0Q2UzFOTmpTVW1INFBvR2dLQUc1Qk9N?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxNSlpSWXQzejNTajgzM3Rvc1hNREhScVpYNDluTmdad01SN1ZtM2xodWJRcWk2aGFiMDBuVGdSR2d2Ukc5NndOeHFoWUd4V1RWQ1o5OGU0djR0dUFCWGRDMnR6QXJ2NHJlRFo5aVN0b3V4WHE2UHR1NGpFaWdUVUR6QzNLRjI5TWdMVy1vcUQ3eWg0ZzRrXzk1VWQtekQ4Z01OaENURVFYYXRZY1hOMXUtNGV3T3c0VlNDandkN2lXSlQtSGUzMnVmNDhUcjBVU3Jo?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxPaTlpeE1xeHViLVlyVGNDTC1peVlRSVE0X3BQbEdOcVl3aGtCUDd0TWJRU05KZTViWXpfM0xxMVdDWWZHakVsWHlmRzhEcTJTYzVCYVR2Ynk3cUJ3amU4Z2V1MDZxbk5nSUt2R3JpcXpYY2J5VmlPbGpjVFdkWXpaU2hTMC1lMzdIeE9CSGtTbVdDYmtaWVZqRGNUb0hrbl9zZjBmQWVSQmlLQUJaUmlJbS1HQ19kSUtvYXZ2NFA1dkxfc0FWazhYSg?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxNSHNyXzF3dngxZ2xlY2Jjc2xwZ0gxa0N1NDA1b2NmWE1jVkpIbno0aFE0SjRsVC0ybEhGWDN2d2lQN3B2UXZkcEFUMXpGcVphVF9HS29UTTdONG12VjQ4RjZLa2J4b1NBc25NRkdiZW1LSUVPZUU0QkZnV2k1N1V4RzI1VFBFbFlweXJZVWNCc3U2TVgyWXRsTU1UZUNJTWJLUGhRejJhZFllTHhxWWpWcUtvMkVYbWNhSGxjam1lZEI2elRMWGxwR0lFaXFxdGM?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxPTGM2NUlSMnpoeEtVU0xIdXZLVWc5Q3djMmtiNy1PT0gzcjRFdlR0cVBOSEZWd1B0YTFMUUw3YUQ3OXFkRllzZXktN0U0Ui1lYUZVcXpGdGQ4MnhJNlVnOXVfekdzTXhDYXdGWW9mX0gyekc3QTkyLWJsYml3eV9mUGpaTjllTkIyaGFhV0hBcFZxbkl5NXBCRjZ5Yk5LdzlrRXN6TWxjbGV2RVlObnhMS1VmQjZNUEJCOVlLeThxbFpLVm5SZnZ4cnlJZUQ?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxNaEtNWVpCQ2hSNnFOLVBadW1DcG53NkFPdEJBM2o5RkFUWGZyZmxHZkd3d0Q4QVZLbHg3OGVHYUxmRWU5Y2I2VmNpLXpfVmo2aXBWVXFUUHFESEE0ZzVIc3FBUFhIYVpIYWVLcFVDQzIzVmVrbFhzOGliWU5wQlRzakVDS2k2T2REaHY0UU5RNFA4SFFzWW54YjU3aldrVHhLdEhnUzRhbWNKbHNoOXE0eFRHb2x2Y1ZuRkwwWUU1VmNwZElsTTN6c1FvTWk0TEsyZ3ZF?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
