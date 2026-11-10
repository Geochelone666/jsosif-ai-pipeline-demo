# MSFT Intelligence Report

- ticker: **MSFT**
- Report as_of: **2026-11-09**
- Market data as_of: **2026-11-09**
- Quant sources: https://finance.yahoo.com/quote/MSFT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MSFT/key-statistics/
- AI analysis snapshot as_of: **2026-11-09**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-10T06:08:41.143542+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 18, 'rule': 5, 'ai': 11, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261109T043242Z-c8e908de/MSFT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 18 unique headlines; 11 named publishers; 0 exact duplicates; 18 HTTPS source links; largest publisher share 22.22%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 545.1800 |
| Return 1D (%) | 2.7459 |
| Return 1W (%) | 7.5051 |
| Return 1M (%) | 1.8895 |
| Return YTD (%) | 13.4442 |
| Return 1Y (%) | 10.6368 |
| Annualized volatility (%) | 33.9326 |
| Beta vs SPY | 1.0315 |
| Max drawdown (%) | -30.5348 |
| Sharpe (rf=0) | 0.4123 |
| Downside deviation (rf=0, %) | 21.5623 |
| Sortino (rf=0) | 0.6488 |
| Historical VaR 95% (1D, %) | 2.8549 |
| Historical ES 95% (1D, %) | 4.1000 |
| Correlation vs SPY | 0.4162 |
| Tracking error vs SPY (%) | 30.8570 |
| P/E (trailing) | 28.45 |
| P/B | 8.61 |
| EV/EBITDA | 20.02 |
| Revenue growth (%) | 18.80 |
| Forward P/E (estimate) | 22.53 |
| Gross margin (%) | 67.66 |
| Operating margin (%) | 49.76 |
| Return on equity (%) | 34.22 |
| Free cash flow yield (%) | 0.07 |
| MA50 | 517.2788 |
| Close vs MA50 (%) | 5.3938 |
| MA200 | 439.2570 |
| Close vs MA200 (%) | 24.1141 |
| RSI (14, Wilder) | 57.4651 |
| MACD (12,26) | 5.2358 |
| MACD signal (9) | 5.0266 |
| MACD histogram | 0.2092 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MSFT': 278, 'SPY': 278}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 545.1800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.7459 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 7.5051 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 1.8895 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 13.4442 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 10.6368 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.9326 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.5623 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.6488 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8549 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.1000 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4162 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.8570 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.0315 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -30.5348 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4123 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 22.5321 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 67.6570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 49.7570 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 34.2210 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.0740 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 28.4541 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 57.4651 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2092 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.3938 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 24.1141 -> Clearly above the moving-average trend level.

## TAILWINDS

### Microsoft Stock (NASDAQ:MSFT) Gains Despite New, Overzealous Outlook Security
- Summary: Microsoft Stock (NASDAQ:MSFT) Gains Despite New, Overzealous Outlook Security
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNTEhMamI2YjVpOVNWUHJ3WDdPZ1hGa2xKMnhETTB0Uk1Yd0l1OFY2Sk5TanNoaExwR00yY0lKcHV3Q2JEVDlhbWpLUE80SV9LTno1T0NRdVBMaFIzZDR0LWN5VnhlcVlXLVhtbUlhQ0cwZkI2N2FhZGtWRU5heF9VMFMwZ295eDF4TnNSSVp1eE9hdWdpbThEaW1ZX0NnUURxOHFFMV9B?oc=5>

### Microsoft Stock: Azure Drives Growth (NASDAQ:MSFT)
- Summary: Azure growth boosts Microsoft’s revenue prospects.
- Date: 2026-11-07 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxPVDRzTEx3dG1KcURGdmJEUHByUE1UOGtFWnNxcjJzaVhDZXNoS2E1ZUo0UjRidkpXWkVnc0N0QXRVMEpaUkJLSFVCVGtLcEhqV0JBdm1ZV3hoSDduTFpRRkVldXlGb2NfOUZvR2E4M29QMHBfQ2NqcTc0ZW5tS0c4QmpR?oc=5>

### Microsoft, Oracle, SAP considered 'AI winners' among software companies: Oppenheimer (MSFT:NASDAQ)
- Summary: Oppenheimer labels Microsoft an AI winner, boosting investor confidence.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOMUw3cXRyR2pWU2hkLTVEMlJsRlNaSGZIZWpXRUg1UjVEbjAwY0RjWTlJM291UmJBaUFCaUxsQURYNFVWcUxpWHhaM1gxdnlIQUl0TUNqYWRTSWVOSmQ1OHozd200dXJOUUpuZTY4eG12bkhvV3laZlAwX29GTzl4bEJFeGNQaE5OZEVSbkhwRkFZNzNaX1h2U3VrazlZMFZreVJVRkp3dkZoaTVRbWh1SF9oN3M?oc=5>

### Microsoft (MSFT) Stock May Be 33% Undervalued Following $25 Billion AI Bond Raise
- Summary: Microsoft’s AI bond raise may leave stock undervalued, suggesting upside.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxQOGEwcGgybldTbnNVZ1RsSWdzYV9mQUotWXY3Uk9BelFWNm4tMG5mc2IySFRKNzJybHIyaDNqVms0aFBSWV9sSFNQdkxBQTlOY1pYYzN5Nkw2S25wU044UGtvVjAtZUlObGtDOUNhVjNuTjlXVVBJQWYyT0xJVkpCdjdyc2dKc2FienVCSUJuS19KRXRWd21DS21rTE9adnROWU5PRmY0MXVhZ0ktZEJBTjRUbm9yZGh2bW1vTHRxbjZuV0luTWJj0gHMAUFVX3lxTE9ENkxxeWFQZG1qc2xkRTdvRnZ4ek1IS2pCZG9BYTFSSzZlckJzcjFsdE45TVNrWllNX25jU1dMdWdRVEgzMjE2a1BvdGRjbU5JUTltYVpLQWF2b00wTmQ0Zlp0OEFMalNERElPdThEdjdsTUZUYUN5clZxRTFTTF9Mb0lhYzQ0b1VMdlhMdEE4R1pYbHZYbXhqVTAzU0M4SnJTU2FBeDJOUFFPU28wMXl0eGhONGdYelAtcUtBdmZIcmVaUThYRFEzNDJhQg?oc=5>

### Microsoft and Northern Trust use AI to cut client data prep from about 2½ weeks to 3 days.
- Summary: AI cuts data prep time, improving efficiency for Microsoft and Northern Trust.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxPRjdjaFVEclMyQmY5ZW0xZ25mOFJ1RlJRVGVGV1l1c2IzdEE2Q0I2RVZlcG1uRnk4cXJURzhmT0p3QVZmUDNoVk5GdEJVbHF6ZnlwTEdYUldyNzVFTTBoT1hETTJuelFJclY2UU1aU1lqQ0x0MVNlZHRGLVlnZzlaUjFOZEZNMGNZS0x4UlhvWnVOTWtFUU1XMTJ1MUtaWXlwZ2J0RkNfcHB2MWNmdzlhWnYzQnE5UQ?oc=5>

## HEADWINDS

### Microsoft: The AI Numbers Are Telling Two Stories (NASDAQ:MSFT)
- Summary: Mixed AI performance signals uncertainty.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQMmVCU3lEYUFULXFuME9keUgwSm9mb3pudnpEdFFJS092QnJacDZuQi1fdFFNR1lyd3J5WHU1ZUJ0RFZYMGZuUmlWOHBBd0RWVFFzYm02b2t1U3dKZzlZMmRuMEdTTVJYdDZkaGo2ZG9ZWUtubGFhajhTWFlfTW1RSTBsRzBkWC1zX3ZFcFVNYnhKZ1k?oc=5>

### ETFs Are Net Sellers of Microsoft (MSFT) on Nov. 5
- Summary: ETF net selling indicates negative market sentiment.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOajREVXB1X0Fpa25Ha3Y2Q1ZuZTlMNTlpay1oU3pwR01vNVdNWlZaOFRNdFljelFDOUNpaDlkdkUxeFdZY3N2RVVGMFJhSnpuTWlNM3FOajdMWEQwN3pJVWxvWG9tU3k5Qno5LVF0TzRfTl9uVWloLVBBYmE4aXkyOHV4QnVMLVdPY0U4LUFZemZoNVJ3V1JUZlBqWkg?oc=5>

### The Stock Market Is “Petrified of Oracle’s Balance Sheet” as Microsoft Walks Away
- Summary: Microsoft’s exit from Oracle concerns investors, creating market unease.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQM1pqQWpCS2FEMElhSHlscGJrYjJiTlhEc1VhZkxad1Rjb3ZQX0pvdUxiQ1JWRTliZFhSdFFkZWFncV8wTFZIbi1hZmIzRUJmaUxYT3hMNlA0aF9qa2kyT1dTaFAyZWpyd3dhZ1BMR2xFSzBEUzJxcUVWY2JEZ1dJaU5KZ1M3Z1BtZlVFQ0hUcUtMck5TVGNVa2dCdDBpTXZPNVNLZkJlcw?oc=5>

## CATALYSTS

### Microsoft Is Reportedly Getting Pickier About AI Data Center Deals. Is the Stock a Buy Now?
- Summary: Microsoft Is Reportedly Getting Pickier About AI Data Center Deals. Is the Stock a Buy Now?
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNdmxmRExkR3Bmc3lfdW8zM3A4c3lGZFlEMUVxYlFmSk1sTmt0TkNGZk5JRDh2bEVtT1loMDU5LTVnOUNOcTBSMW1hckloZm0wQksyclNlMHVEa1RTXzRJdDBVS0dMdm1CMTZZclFPa09oQnNVUDdCdnlZaUk5aXJfUlRORHhSMnJDQ2NWOExCTjZHTm5GQTdJeEl6blNYczE3NVJXMUVHUlhQOWJkcm5YMzZ0cm5CMDZIVE1tSy02aTlzV29pT2xFeWh1LUg?oc=5>

### Microsoft (MSFT) Is Pulling Back From Key Neocloud Data Center Deals
- Summary: Microsoft (MSFT) Is Pulling Back From Key Neocloud Data Center Deals
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOMl9UODZoUFhCcm5lSkVLRnpNOC1aUjJDTGpfYnRhZkdYZllZb0R2MWJZQjhZekFFZjVwZUJ4OGRYdU01cHl1aldmYVJaaEtqZmtKMDVqWlBKWk83TEh4alptZHF1dlVYb0h1UllvY283ZnRwaENMRUlIUmVEcmZlUmZ0WU1zU1BMT2h5SDBhRzNfQTN0N0Nz?oc=5>

### Microsoft (MSFT) Stock Gets Fair Value Bump On Azure And AI Optimism
- Summary: Microsoft (MSFT) Stock Gets Fair Value Bump On Azure And AI Optimism
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOOGFuV1U3LUZsekt0ZU1FV3RlMWN4RDdGUENlVlM3SXhHUFlJSkk3S1AyU2taci1pMGN2ZTE3VDR5UmpqN19rajZQQXNsbmtQaEQyOHY0R1ZRZzZDNXVhTkk5MzBYOEk2WjAtX2JWZ3lWQWU1bmdYZHJLNk9LaW9BWEl2am5PTXo4UHlXaTNJYk5obEZwdl9RSVJfZw?oc=5>

### Microsoft Corporation (MSFT) Stock: Jumps as Northern Trust Unveils AI-Powered Onboarding Agent
- Summary: Microsoft Corporation (MSFT) Stock: Jumps as Northern Trust Unveils AI-Powered Onboarding Agent
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNREExSVVWdkhFVlNrSkl2TUFOSXU3YzBUMkVtbFEyQ0Fsb0JlajB6YlY3WUpremdMWGwwSUF3VTZ1MmdXcEMxQ2ZmUURIQlJTREw0Qm5Pb1NrVlZLdFF0ak9TYWY5QUNIem9lTm1EQUN4Nm85dFZUY0FmRXFxYlNoSjVrZXUxcWlIc2ZOSl9YaVh2clNidmZ2UmlrS3lmZmhYZjByU2cxQzNYR3pGOWRFVUd3Z3ZtLWc?oc=5>

### Microsoft (MSFT) Stock Could Be Undervalued After Its 74% Five Year Run
- Summary: Analysts suggest MSFT stock may be undervalued based on its strong five‑year performance.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQWHQ3RXM0cG00eE1IN192dkg5cGtlMUFnUzRVUkRNQnB2TFpLRXh6VjFxZVliTF9vdjU3anZxZTZPeHJERTV4bUZQN05na1BkOWxqeVpKYXc2d3M5c25uT1ZxWFRodFNzNmliMjNhYnYzNldKbXE3Wm9uRG1pSHNmNHBBaHdlZFUxbFppN3FlY0xMd0cwVXduUHdQcjVBWHB4SktqZFdB?oc=5>

### Did Capacity Deal Changes Just Shift Microsoft (MSFT) Stock Narrative?
- Summary: Capacity deal changes may alter investor perception of Microsoft’s stock.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxQNHJNMzlYeFlrbU5SeUhHclFoazAxdTBCeDJ3VmJuTWl0YlpjYXlEbXMzT3FtSlRrMXZNblBXWHppTFI3RlE2THgtdTJSajdhVGZtR1h0WlZwVUlmbGtxQlpVaHJQY1Y0ZTFvZ256Q1ZCS1lJYUJUc3pzcHIwS0djeHhnS2ltcUtYRWlnbzJ0N2p1MDUwUlNTLVRZc0p3azVWbzNBTWlZUFlYaEtHQnBQZVdhNXZoNlc0clgyekdZRjkwZ3h2Y05Z0gHMAUFVX3lxTE9RelByQTREM1dua0k2OWt6b0xmd1RFdDliV0hKSDE1MTlJeXRLQW14aE8zS3Vkek5YMEFVSWJMV3lGVnVkWnJvV3BNY1JHVlUyRjh0S2JBOUxLbExaY0RYanZGcnJqSWRZUFdndEthcFhoNkRfSUtHeGU0WTFyMXI4NkV4SjlXZGp4ekRwTFNaMmlVbHpkenFaZTJGclVPdTFrc2xWbExnSVRudEYyM1RyX2ZuRnRLdXljTE5fWkdVTzJyV1piYThial9KZQ?oc=5>

### Microsoft Corp Stock (MSFT) Moved Up by 3.24% on Nov 9: Facts Behind the Movement
- Summary: Microsoft stock rose 3.24% on Nov 9, driven by unspecified factors. The article examines the reasons behind the price increase.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOTV9JenpiWDE3bXZSWERMblpmMi1zY1VBbHZuNnRDUXpVWml3TzhDSmJ0RDVxX0xPV25uTnpMQ3ZhU0NnVm5lcDg3dVlnMUZ5d2I1bGl6R0k4RUJSSlVXQTB5anNNb2YzNmR6NGwyendtWWNzblVEenlnNFhYRzhlWExvTkE4c3M2NWY0?oc=5>

### Microsoft (MSFT) Stock Price Prediction: Microsoft holds above short-term trend support as traders split on direction
- Summary: Analysts predict Microsoft stock remains above short-term support, but traders are divided on future direction.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPaEpHSnFSOHVaZEd2SFNHbndXRXFiNHYyOWhzeUZLSmZCb1RlZVZQYjRsbk0xU1lKZ29nVFpPVTdGMmdnSGFldHdnaWJHeFdCb3d2V2tBdjBCX096RkN0RGRFVFpVVHhVZk9zX3g2STRsaThtbHAxdjR4MW9JRnVVcmduOUdLREFjUWJ6WHJpMWNBTHcxSDFKNTRmVVNQdXc?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MSFT** | **28.45** | **8.61** | **20.02** | **18.80** | **4,048,612,753,408.00 USD** | **10.64** |
| ORCL | 18.78 | 5.86 | 14.51 | 29.60 | 373,470,232,576.00 USD | -49.26 |
| GOOGL | 15.05 | 5.37 | 18.57 | 24.70 | 3,542,515,974,144.00 USD | 3.61 |
| AMZN | 21.58 | 4.70 | 16.75 | 12.10 | 2,886,350,929,920.00 USD | 9.21 |

Peers fetched as_of: 2026-11-09; MSFT reuses existing data (market data as_of: 2026-11-09); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-09

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-28
- Revenue (latest available single quarter): 19,953,000,000.00 USD; period 2010-10-01/2010-12-31; fiscal year/reporting period 2011/Q2
- Net income (latest available single quarter): 36,629,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMipgFBVV95cUxNTEhMamI2YjVpOVNWUHJ3WDdPZ1hGa2xKMnhETTB0Uk1Yd0l1OFY2Sk5TanNoaExwR00yY0lKcHV3Q2JEVDlhbWpLUE80SV9LTno1T0NRdVBMaFIzZDR0LWN5VnhlcVlXLVhtbUlhQ0cwZkI2N2FhZGtWRU5heF9VMFMwZ295eDF4TnNSSVp1eE9hdWdpbThEaW1ZX0NnUURxOHFFMV9B?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxPVDRzTEx3dG1KcURGdmJEUHByUE1UOGtFWnNxcjJzaVhDZXNoS2E1ZUo0UjRidkpXWkVnc0N0QXRVMEpaUkJLSFVCVGtLcEhqV0JBdm1ZV3hoSDduTFpRRkVldXlGb2NfOUZvR2E4M29QMHBfQ2NqcTc0ZW5tS0c4QmpR?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxOMUw3cXRyR2pWU2hkLTVEMlJsRlNaSGZIZWpXRUg1UjVEbjAwY0RjWTlJM291UmJBaUFCaUxsQURYNFVWcUxpWHhaM1gxdnlIQUl0TUNqYWRTSWVOSmQ1OHozd200dXJOUUpuZTY4eG12bkhvV3laZlAwX29GTzl4bEJFeGNQaE5OZEVSbkhwRkFZNzNaX1h2U3VrazlZMFZreVJVRkp3dkZoaTVRbWh1SF9oN3M?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxQOGEwcGgybldTbnNVZ1RsSWdzYV9mQUotWXY3Uk9BelFWNm4tMG5mc2IySFRKNzJybHIyaDNqVms0aFBSWV9sSFNQdkxBQTlOY1pYYzN5Nkw2S25wU044UGtvVjAtZUlObGtDOUNhVjNuTjlXVVBJQWYyT0xJVkpCdjdyc2dKc2FienVCSUJuS19KRXRWd21DS21rTE9adnROWU5PRmY0MXVhZ0ktZEJBTjRUbm9yZGh2bW1vTHRxbjZuV0luTWJj0gHMAUFVX3lxTE9ENkxxeWFQZG1qc2xkRTdvRnZ4ek1IS2pCZG9BYTFSSzZlckJzcjFsdE45TVNrWllNX25jU1dMdWdRVEgzMjE2a1BvdGRjbU5JUTltYVpLQWF2b00wTmQ0Zlp0OEFMalNERElPdThEdjdsTUZUYUN5clZxRTFTTF9Mb0lhYzQ0b1VMdlhMdEE4R1pYbHZYbXhqVTAzU0M4SnJTU2FBeDJOUFFPU28wMXl0eGhONGdYelAtcUtBdmZIcmVaUThYRFEzNDJhQg?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxPRjdjaFVEclMyQmY5ZW0xZ25mOFJ1RlJRVGVGV1l1c2IzdEE2Q0I2RVZlcG1uRnk4cXJURzhmT0p3QVZmUDNoVk5GdEJVbHF6ZnlwTEdYUldyNzVFTTBoT1hETTJuelFJclY2UU1aU1lqQ0x0MVNlZHRGLVlnZzlaUjFOZEZNMGNZS0x4UlhvWnVOTWtFUU1XMTJ1MUtaWXlwZ2J0RkNfcHB2MWNmdzlhWnYzQnE5UQ?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxQMmVCU3lEYUFULXFuME9keUgwSm9mb3pudnpEdFFJS092QnJacDZuQi1fdFFNR1lyd3J5WHU1ZUJ0RFZYMGZuUmlWOHBBd0RWVFFzYm02b2t1U3dKZzlZMmRuMEdTTVJYdDZkaGo2ZG9ZWUtubGFhajhTWFlfTW1RSTBsRzBkWC1zX3ZFcFVNYnhKZ1k?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOajREVXB1X0Fpa25Ha3Y2Q1ZuZTlMNTlpay1oU3pwR01vNVdNWlZaOFRNdFljelFDOUNpaDlkdkUxeFdZY3N2RVVGMFJhSnpuTWlNM3FOajdMWEQwN3pJVWxvWG9tU3k5Qno5LVF0TzRfTl9uVWloLVBBYmE4aXkyOHV4QnVMLVdPY0U4LUFZemZoNVJ3V1JUZlBqWkg?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQM1pqQWpCS2FEMElhSHlscGJrYjJiTlhEc1VhZkxad1Rjb3ZQX0pvdUxiQ1JWRTliZFhSdFFkZWFncV8wTFZIbi1hZmIzRUJmaUxYT3hMNlA0aF9qa2kyT1dTaFAyZWpyd3dhZ1BMR2xFSzBEUzJxcUVWY2JEZ1dJaU5KZ1M3Z1BtZlVFQ0hUcUtMck5TVGNVa2dCdDBpTXZPNVNLZkJlcw?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNdmxmRExkR3Bmc3lfdW8zM3A4c3lGZFlEMUVxYlFmSk1sTmt0TkNGZk5JRDh2bEVtT1loMDU5LTVnOUNOcTBSMW1hckloZm0wQksyclNlMHVEa1RTXzRJdDBVS0dMdm1CMTZZclFPa09oQnNVUDdCdnlZaUk5aXJfUlRORHhSMnJDQ2NWOExCTjZHTm5GQTdJeEl6blNYczE3NVJXMUVHUlhQOWJkcm5YMzZ0cm5CMDZIVE1tSy02aTlzV29pT2xFeWh1LUg?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOMl9UODZoUFhCcm5lSkVLRnpNOC1aUjJDTGpfYnRhZkdYZllZb0R2MWJZQjhZekFFZjVwZUJ4OGRYdU01cHl1aldmYVJaaEtqZmtKMDVqWlBKWk83TEh4alptZHF1dlVYb0h1UllvY283ZnRwaENMRUlIUmVEcmZlUmZ0WU1zU1BMT2h5SDBhRzNfQTN0N0Nz?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOOGFuV1U3LUZsekt0ZU1FV3RlMWN4RDdGUENlVlM3SXhHUFlJSkk3S1AyU2taci1pMGN2ZTE3VDR5UmpqN19rajZQQXNsbmtQaEQyOHY0R1ZRZzZDNXVhTkk5MzBYOEk2WjAtX2JWZ3lWQWU1bmdYZHJLNk9LaW9BWEl2am5PTXo4UHlXaTNJYk5obEZwdl9RSVJfZw?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNREExSVVWdkhFVlNrSkl2TUFOSXU3YzBUMkVtbFEyQ0Fsb0JlajB6YlY3WUpremdMWGwwSUF3VTZ1MmdXcEMxQ2ZmUURIQlJTREw0Qm5Pb1NrVlZLdFF0ak9TYWY5QUNIem9lTm1EQUN4Nm85dFZUY0FmRXFxYlNoSjVrZXUxcWlIc2ZOSl9YaVh2clNidmZ2UmlrS3lmZmhYZjByU2cxQzNYR3pGOWRFVUd3Z3ZtLWc?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQWHQ3RXM0cG00eE1IN192dkg5cGtlMUFnUzRVUkRNQnB2TFpLRXh6VjFxZVliTF9vdjU3anZxZTZPeHJERTV4bUZQN05na1BkOWxqeVpKYXc2d3M5c25uT1ZxWFRodFNzNmliMjNhYnYzNldKbXE3Wm9uRG1pSHNmNHBBaHdlZFUxbFppN3FlY0xMd0cwVXduUHdQcjVBWHB4SktqZFdB?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxQNHJNMzlYeFlrbU5SeUhHclFoazAxdTBCeDJ3VmJuTWl0YlpjYXlEbXMzT3FtSlRrMXZNblBXWHppTFI3RlE2THgtdTJSajdhVGZtR1h0WlZwVUlmbGtxQlpVaHJQY1Y0ZTFvZ256Q1ZCS1lJYUJUc3pzcHIwS0djeHhnS2ltcUtYRWlnbzJ0N2p1MDUwUlNTLVRZc0p3azVWbzNBTWlZUFlYaEtHQnBQZVdhNXZoNlc0clgyekdZRjkwZ3h2Y05Z0gHMAUFVX3lxTE9RelByQTREM1dua0k2OWt6b0xmd1RFdDliV0hKSDE1MTlJeXRLQW14aE8zS3Vkek5YMEFVSWJMV3lGVnVkWnJvV3BNY1JHVlUyRjh0S2JBOUxLbExaY0RYanZGcnJqSWRZUFdndEthcFhoNkRfSUtHeGU0WTFyMXI4NkV4SjlXZGp4ekRwTFNaMmlVbHpkenFaZTJGclVPdTFrc2xWbExnSVRudEYyM1RyX2ZuRnRLdXljTE5fWkdVTzJyV1piYThial9KZQ?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOTV9JenpiWDE3bXZSWERMblpmMi1zY1VBbHZuNnRDUXpVWml3TzhDSmJ0RDVxX0xPV25uTnpMQ3ZhU0NnVm5lcDg3dVlnMUZ5d2I1bGl6R0k4RUJSSlVXQTB5anNNb2YzNmR6NGwyendtWWNzblVEenlnNFhYRzhlWExvTkE4c3M2NWY0?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPaEpHSnFSOHVaZEd2SFNHbndXRXFiNHYyOWhzeUZLSmZCb1RlZVZQYjRsbk0xU1lKZ29nVFpPVTdGMmdnSGFldHdnaWJHeFdCb3d2V2tBdjBCX096RkN0RGRFVFpVVHhVZk9zX3g2STRsaThtbHAxdjR4MW9JRnVVcmduOUdLREFjUWJ6WHJpMWNBTHcxSDFKNTRmVVNQdXc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
