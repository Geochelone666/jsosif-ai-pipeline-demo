# CAT Intelligence Report

- ticker: **CAT**
- Report as_of: **2026-10-24**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/CAT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CAT/key-statistics/
- AI analysis snapshot as_of: **2026-10-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-25T00:56:29.254752+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 5, 'ai': 13, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 13 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-10-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 687.0000 |
| Return 1D (%) | -2.4217 |
| Return 1W (%) | -5.9883 |
| Return 1M (%) | -15.3962 |
| Return YTD (%) | 20.6553 |
| Return 1Y (%) | 32.7950 |
| Annualized volatility (%) | 40.5118 |
| Beta vs SPY | 1.8366 |
| Max drawdown (%) | -35.3672 |
| Sharpe (rf=0) | 0.9037 |
| Downside deviation (rf=0, %) | 26.5358 |
| Sortino (rf=0) | 1.3796 |
| Historical VaR 95% (1D, %) | 4.0274 |
| Historical ES 95% (1D, %) | 5.1314 |
| Correlation vs SPY | 0.5779 |
| Tracking error vs SPY (%) | 34.7400 |
| P/E (trailing) | 29.57 |
| P/B | 16.28 |
| EV/EBITDA | 21.84 |
| Revenue growth (%) | 24.00 |
| Forward P/E (estimate) | 21.08 |
| Gross margin (%) | 29.71 |
| Operating margin (%) | 22.18 |
| Return on equity (%) | 56.97 |
| Free cash flow yield (%) | 1.60 |
| MA50 | 799.7366 |
| Close vs MA50 (%) | -14.0967 |
| MA200 | 807.1243 |
| Close vs MA200 (%) | -14.8830 |
| RSI (14, Wilder) | 26.7463 |
| MACD (12,26) | -29.4600 |
| MACD signal (9) | -19.6071 |
| MACD histogram | -9.8529 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CAT': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 687.0000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.4217 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -5.9883 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -15.3962 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 20.6553 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 32.7950 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 40.5118 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.5358 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3796 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.0274 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1314 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5779 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 34.7400 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.8366 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -35.3672 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9037 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.0831 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 29.7130 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 22.1830 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 56.9720 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.5988 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 29.5738 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 26.7463 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -9.8529 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -14.0967 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -14.8830 -> Clearly below the moving-average trend level.

## TAILWINDS

### Caterpillar (NYSE:CAT) stock rises as power-equipment demand lifts backlog today
- Summary: Caterpillar (NYSE:CAT) stock rises as power-equipment demand lifts backlog today
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNRGpqRjJZNHBDRXJMcUVTUHhXSmdfNjQzMnVyaTBDUzRwOUk1WGxLQVN1aDRfeGg1czZqY3NlbFFRWjNqVlRTUjNNaEVCdlI4SWI5dHV5MUVsN09VZ1R0WmEtSlluRWk1QVQxY2hjRnZqNjdldTVGQXdROWlpbDhfbGpWR2ZQRFBNT0pvRGJWZlpvaHEwUXRqNlUzdFlaTUJEMkNEVjBFbENxQ2Iwclkwd0M1cWozd0R5VWNWNFhIdTU?oc=5>

### Caterpillar Is Quietly Becoming an AI Stock. Here's the Segment Growing 72% That Proves It.
- Summary: AI segment growth of 72% signals strong tech adoption.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxOTUNwa0o0U2pLQWMwbnJZWVAzREVDV2xVQ3NuX09BRlhBWmlzWVoyVEw4MHhITjdlQzM2UnUxYVFOSlNBa1A2bllCN25LUFFMdXpPbHdSVHdjVlgxblNtQnFVNjQzTThod1pvc1BVNmNXWGtLdWFzN3RIN1NHZ0YycHlva1NpT0ZvWFpydEUzUHhjLU5zaVUyTjVSSWtEVGY0Wm40?oc=5>

### Caterpillar vs. Deere: The Better Heavy Equipment Stock for the Data Center Boom
- Summary: Caterpillar outperforms Deere in data center boom, indicating strong growth prospects.
- Date: 2026-10-20 | Impact: high | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPaXVvS2V6aFFqZWd3U0lUSTBsc1pPNG5QcG51cWhkNVFqSkwzZTlEejVEWHk5aDlQdnRUc201WnRDLXk3NmtfUjRIa0p5RThrN2xTNk9RMzI2d2xnTlRZNzA5REl4bGZZVm5uYjJhZGRPVFNNeUVvb1NYNUVjaXRIejVJcklRUk1yWmotR0gyWnM0TnlUcHFEaDlHTjAxUWs0Z0pKUzRvNEhpbE02ajNyVmdMUjNaaU9YazJnUVhuVQ?oc=5>

### Caterpillar, Cummins, Quanta Services poised to gain from 2027 data-center growth: UBS (CAT:NYSE)
- Summary: UBS forecasts 2027 data-center growth benefiting Caterpillar.
- Date: 2026-10-19 | Impact: medium | Horizon: long | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxNVjhKaGRxbVhkMFV4blJVX0x2WVVIUm9haDVCazVveW1mR1JPSG9ST2g1V0lGd3ZNVUE5anVlZ0VZQl9VR0ZZLWVWTlRpbWZxUExjTkllM2pIakZjUllNeU9YQmp3MkxiN0lrR0RFNG0xSWpxZ3pwUUhjRllkNmhRcEtqQXJrcXdqQzB5bk1sQkFQSjFlY0RtQ0ZyTlZuT2JaMmhOV1VYYnRkX1V2OFVUMHRSSzhoRnh5WXBYZ0ZB?oc=5>

### Caterpillar (CAT) Expands In North Carolina As Investors Ask If The Stock Is A Bargain
- Summary: Caterpillar expands in NC, signaling growth and value potential.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxPeXV4RTZDTGNLdHJVVDVRUDQ2ak9lSGJ4X2wyQkVPY3F1UlZVdFdteUxQYk1zZ0NjT3pBMW1abXBSWXRKcUlVSzZwZ0hmWG9PZTRoTHBlYTI3TlVNLVhlSVpSLVZ1eTNUeFQxejU2bDB0cXRLS0tmS2xGTFVSZDQtQ0hHV3J5U1ZqbDFoTW5oZ2ZyYy10Yl82LW80MWhLRnpEb2Nkc3pGS3IwS0hDRUMyMWRtaDlCcjJ5OExfVWRLNEV2Z3EyU2hQQTE4QWLSAdIBQVVfeXFMUFBuM2NocmlIc2ZXRHNfMUFZV25pWms2VWhvVXk0Umk0UEZRaEpNdWlIUG54TFpUYjQ2Wk9pLVFsUGJOY0QtN3JNRHJ6T3B2V1A3dDhjNUlrVFN5RUhWOVMzSnl4VWlaNEwtLVBFOXdPNWFnZDEwVTJTajE2VXEta1NWR3FLaXJwUHZBM1dmSGxQM2VSQzVldE1RdnpFcGVieEYzTW9vOVhvdEVJN0pHdWE3cDNiZDUxeHBoellTbkVkaGk5YVNEX3VfdXkzRVg4VDFB?oc=5>

### Why Is Caterpillar (NYSE:CAT) in Focus as Infrastructure Themes Shift?
- Summary: Caterpillar gains attention as infrastructure trends shift, potentially boosting demand.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxPT2FJd1FGa29pZC1tbTdTRklyb2RZU0p2NEExZkE3OWl0ZG8yLWVwMjBFbms0d3FsWkJBVTNnSHVlVi1jUmZVeFgtU1g4NUw3bDUtQVpCM2RVUWY5SUgzZmtHTGRGX0xvakFQRzFJNWx4TUZtU1VQVmtnUTVRQWlEYXBlRXJNWmhtM1M0bWJlcXRlbjRKMlFHZHJpelpmeTRjYnZqUGQtTkt3cEpqRklYd04yS1Z0SXdGa0Y5aXBnMG5JYXpGcGc3X0RrekY?oc=5>

### Caterpillar (NYSE:CAT) Draws Focus as Data-Center Power Demand Surges
- Summary: Data-center power demand surge puts Caterpillar in spotlight, indicating potential upside.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxPdjVhd0gtajhwVFprMUNmemxmMGYtQmw0amN6M3c5c3VnVnJ0N05PV0dyVjJ0V09fMkdzVFlvZDRRZ0VPQk5VbE5XMFlxT013VWl4VlN1VWlGYWxBdGxydFVEN1JkUW5BMTRCOWY3SXgwVC12Rlc1OFVIbS0zOVlwTGQ0LVFnM3lyZWdoR1VIY3oxSnQwVHd0U2hFdUhBYmt6WnJEWE9GQWdJNW1DRVNrNXBB?oc=5>

## HEADWINDS

### Caterpillar Inc (CAT) Stock Down 4.9% but Still Overvalued -- GF Score: 90/100
- Summary: Caterpillar Inc (CAT) Stock Down 4.9% but Still Overvalued -- GF Score: 90/100
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxNMlo2YVcxejRBY1FnRU15Z1o3V1MzenRjUGRpVlpNTmFNLWxfemVtRmcyNUIxcUlndmhYUXFwb2lta0R4eVlvNzN6UVN6UFkwT0Iyel8tNm15RFpsSHFrZHZkUlR3b292YW5XV25xay1ubF80NFpycmxfcUJ2ZzlLU3ViV1NRemgtdXlsalF1dUNabGd5dmczM1EzT2hCbmtTb0JvQmpBQm5SS1FU?oc=5>

### Caterpillar Inc Stock (CAT) Moved Down by 3.96% on Oct 22: What Investors Need To Know
- Summary: Caterpillar Inc Stock (CAT) Moved Down by 3.96% on Oct 22: What Investors Need To Know
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNUUNnamh6SDVQY0xFTG95UHpNYUw5YlMyRFltQk5kazJ5emRJLUpELUhCdDFWdTQ2VU1DaUV2UzRzMjc0SVUzd2RrVzktdXo1MXNfSUtCSXhKNzZXMl8wR1pGMmVBOHNGRXR0S3hZRmV0RHZvakRWbkxCaWNhNFVhR0hCcWVJNmxpQ3c?oc=5>

### Caterpillar (CAT) Formally Objects To Tokenized Trading Of Its Shares
- Summary: Formal objection to tokenized trading may limit liquidity.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxOR1VBLUMxWG9GXzZJWVdWM2kzSy0ycmUyeDRYRmJxTm5LNzNDd0xiVDM3MjVqa2dSNmpZWTZCZXhwZzBIRDhySExOZTdoYXU5VGtZeDNJS19aSUxERUREakFOSENWVDFON0hrMHdoRS1oMmF4STNUdUJkZzdXdUpuUGxaMi0xaldlWkVuNnVJZUVxMGlIMGdWNkVzRFVjdkFCc2w3QUQyMUxNOFk?oc=5>

## CATALYSTS

### Caterpillar (CAT) Reports Next Week: Wall Street Expects Earnings Growth
- Summary: Caterpillar (CAT) Reports Next Week: Wall Street Expects Earnings Growth
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNTWROdHc0S3hGTEFFUmswNDVGMUxadkZ2ZU4yT0tCSXhQU0Z6anc5dkpySWlnbkJPeVVLUlpUUkVlTzVUS2REdFZiTWNTZ0lLSVd3MGFMVGlmZXlManduVzdOUm9BTHZEQmlKaVlma0FLTnNWZUNRU1FjVjJhWTVNZklPVjJTRXZMUlVReFVSNkJGZXAzd1V5M054ZnNxclk?oc=5>

### Caterpillar, Inc. Stock 12‑Month Price Target Cut to $964.84, Implies 32% Upside
- Summary: Caterpillar, Inc. Stock 12‑Month Price Target Cut to $964.84, Implies 32% Upside
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxOMTViZ0JDRXpJbkNPYXpDVHk5Rk0wam56R1loVE9UREtmNUdMN041b1pFdzJzTTU0QmdWam54UUZla1JQTWlWT09QSFVyUEZlZ3BiSTB5M2RmcWN6R2Q4Z2JmRm5SU3RKUnU0c2h3UjNNODl2RWVyRksyWnFhR1cxbjR2RWdkQ2JuT2xBS2hqb1hvQkdaX1pqTXdvbHVWMC13MTlnMm9rS3Y1TVhyMUVxdFRFSEFBdm9BYW5hOFlFSncwaGhLV2FnYTdGR21SY0l0YnNV?oc=5>

### How Big Could Caterpillar Stock's Next Fall Be?
- Summary: Speculation on potential future decline in Caterpillar shares.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPU3laYWVQZXdwNEs0ZmxOZ2RKTGU5X1hoa1pwSE9pMmtDS0twblQxRU9IR0s0MFY3dXptaG9ET0pSbVBTeFpGbnJOeUJyNnNVWkFWakFiY3k5UGlydW9JVEZtaUQ5bEI4bWI1R1A3YkVBTjhCTFZrblV5QUVtN2x0d01YUXFsOEllTURPY3FteVVBTUJXRnFlSnBrUWo3WU0?oc=5>

### How Big Could Caterpillar Stock’s Next Fall Be?
- Summary: Speculation on potential future decline in Caterpillar shares.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQellmZ1ZFejhCWHFzUmEtUjlUZTRjZWRxaklWblhWYldqbGlYLTlJV0ROd2w2Nm1YaXU2clp6WjNob25iRmE4dG5PX2U4WlhtTm9vN2lDQkpuOV92R1NuUERlY0U5Y2pBeUFVbHdyTzh6bEJwbEdGeEFiY1RYVldPS09NTVppSjcwek9Ja1QwVmRWWmZRSnpsR2FCUTFaVU9lUjJCS25nNFk?oc=5>

### Will Caterpillar (CAT) Beat Estimates Again in Its Next Earnings Report?
- Summary: Upcoming earnings could exceed expectations.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNdFZSODYwSGZHTTZTaUprVElfRTRzZDJ0dFpfUzluYkl0U1c0WG9HTnk4dWRuSm1OR1FyaXNPd3RvRVJPVGRNNjA0bHlvT3R5MXdpaXhjY2xjemRkOGp3VTNmeng3NXVURG9ldVBTbHN1ZEZQbmI1LWNnV2lQVlc0aFJFZnZvWGk3elZFV1k5TUJZU2VNYVo5NlM3UURQam5kZXFB?oc=5>

### All You Need to Know About Caterpillar (CAT) Rating Upgrade to Buy
- Summary: Rating upgrade to buy boosts investor confidence.
- Date: 2026-10-20 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxNaTdyWjk1dmZBT2Vmeng5UndvTG10YVNpZDBzVjJ2OUtYaW1YbUNpRjZEdHJZVG1YeHV0MkNLSUVZdVBDWTZrOXpFNVlyaGJuNzlrNEdnVkNoc0kwTjBvWV9OWVlkSzd3aVN1LVVhR0Vva0gxaDhmTVdKNlNKQ1QyUlVZbWlrYW51a2JrWg?oc=5>

### Caterpillar stock may move 6.3% on Oct. 29 earnings report By Investing.com
- Summary: Caterpillar's earnings report on Oct. 29 could drive a 6.3% stock movement.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNbkFJOTNJT2h1NXhLa0pRS3h0RWdxc3FCX0l6RDQ5cy1QWXRpcDNRcnZyS2YtRjF4UTlDbzNuUlBXZk9GLVM5UEc1QkxIaC1oaHRaWVRuRmxzWGJUbUFUMEh4aUljVFVoZENOM1JGaEZkYUEtNlJCV3BudEI1bTR4RF94RmdfeHJ3MVlBdXpET013QW8td3ozYlBMQWM2c0lxOXlYRWdfZ0JDMmM4dldSSTU5NU1TbXM?oc=5>

## RISKS

### Form 4 Caterpillar For: 23 October
- Summary: Insider trading filing may signal corporate activity.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQR3V5MlpKaWtBVWpuZEt2b25BU3FzblBlbG5VX0ZzR1lMamg1Z1RNMHdoZFdXaHhoNmhiS19HZXhQYlYxUEZyYmJVUlVFd0cxYmZMVXk1MmxUTXRFVlJPQlJyWHFwVnFXVl9vVzRUSjJ6OHcxRzNvYTRZVEVxV3dPSlpqREhvcFpuckYyejdNZGJiMkhENDBva3pR?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CAT** | **29.57** | **16.28** | **21.84** | **24.00** | **315,796,652,032.00 USD** | **32.80** |
| DE | 35.92 | 6.22 | 26.97 | 4.90 | 174,218,461,184.00 USD | 39.22 |
| CNH | 45.96 | 1.83 | 37.21 | 2.00 | 18,477,744,128.00 USD | 7.52 |
| CMI | 26.44 | 5.54 | 15.27 | 9.40 | 71,227,604,992.00 USD | 25.67 |

Peers fetched as_of: 2026-10-24; CAT reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-10-29 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-05
- Revenue (latest available single quarter): 20,543,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 1,141,000,000.00 USD; period 2011-07-01/2011-09-30; fiscal year/reporting period 2011/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/18230/000001823026000046/cat-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNRGpqRjJZNHBDRXJMcUVTUHhXSmdfNjQzMnVyaTBDUzRwOUk1WGxLQVN1aDRfeGg1czZqY3NlbFFRWjNqVlRTUjNNaEVCdlI4SWI5dHV5MUVsN09VZ1R0WmEtSlluRWk1QVQxY2hjRnZqNjdldTVGQXdROWlpbDhfbGpWR2ZQRFBNT0pvRGJWZlpvaHEwUXRqNlUzdFlaTUJEMkNEVjBFbENxQ2Iwclkwd0M1cWozd0R5VWNWNFhIdTU?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxOTUNwa0o0U2pLQWMwbnJZWVAzREVDV2xVQ3NuX09BRlhBWmlzWVoyVEw4MHhITjdlQzM2UnUxYVFOSlNBa1A2bllCN25LUFFMdXpPbHdSVHdjVlgxblNtQnFVNjQzTThod1pvc1BVNmNXWGtLdWFzN3RIN1NHZ0YycHlva1NpT0ZvWFpydEUzUHhjLU5zaVUyTjVSSWtEVGY0Wm40?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxOcGNqdHpUTzEzbFFndGpOSDlCTnJTbmM1MHJsN0tVQ3hMY2hnNktidnZ2Q2hfa19lYlR4ZlhyRHAzTWVpaWxlbVJIZWE0b2ZkQ1YyYTF3WUl1bEVLUGpCbzFndk9qTkZMV25iNlh1a0ExZ3l0Y2lxN3RabzJOelRibVZXNWRMVExp?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxPaXVvS2V6aFFqZWd3U0lUSTBsc1pPNG5QcG51cWhkNVFqSkwzZTlEejVEWHk5aDlQdnRUc201WnRDLXk3NmtfUjRIa0p5RThrN2xTNk9RMzI2d2xnTlRZNzA5REl4bGZZVm5uYjJhZGRPVFNNeUVvb1NYNUVjaXRIejVJcklRUk1yWmotR0gyWnM0TnlUcHFEaDlHTjAxUWs0Z0pKUzRvNEhpbE02ajNyVmdMUjNaaU9YazJnUVhuVQ?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxNVjhKaGRxbVhkMFV4blJVX0x2WVVIUm9haDVCazVveW1mR1JPSG9ST2g1V0lGd3ZNVUE5anVlZ0VZQl9VR0ZZLWVWTlRpbWZxUExjTkllM2pIakZjUllNeU9YQmp3MkxiN0lrR0RFNG0xSWpxZ3pwUUhjRllkNmhRcEtqQXJrcXdqQzB5bk1sQkFQSjFlY0RtQ0ZyTlZuT2JaMmhOV1VYYnRkX1V2OFVUMHRSSzhoRnh5WXBYZ0ZB?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxPeXV4RTZDTGNLdHJVVDVRUDQ2ak9lSGJ4X2wyQkVPY3F1UlZVdFdteUxQYk1zZ0NjT3pBMW1abXBSWXRKcUlVSzZwZ0hmWG9PZTRoTHBlYTI3TlVNLVhlSVpSLVZ1eTNUeFQxejU2bDB0cXRLS0tmS2xGTFVSZDQtQ0hHV3J5U1ZqbDFoTW5oZ2ZyYy10Yl82LW80MWhLRnpEb2Nkc3pGS3IwS0hDRUMyMWRtaDlCcjJ5OExfVWRLNEV2Z3EyU2hQQTE4QWLSAdIBQVVfeXFMUFBuM2NocmlIc2ZXRHNfMUFZV25pWms2VWhvVXk0Umk0UEZRaEpNdWlIUG54TFpUYjQ2Wk9pLVFsUGJOY0QtN3JNRHJ6T3B2V1A3dDhjNUlrVFN5RUhWOVMzSnl4VWlaNEwtLVBFOXdPNWFnZDEwVTJTajE2VXEta1NWR3FLaXJwUHZBM1dmSGxQM2VSQzVldE1RdnpFcGVieEYzTW9vOVhvdEVJN0pHdWE3cDNiZDUxeHBoellTbkVkaGk5YVNEX3VfdXkzRVg4VDFB?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxPT2FJd1FGa29pZC1tbTdTRklyb2RZU0p2NEExZkE3OWl0ZG8yLWVwMjBFbms0d3FsWkJBVTNnSHVlVi1jUmZVeFgtU1g4NUw3bDUtQVpCM2RVUWY5SUgzZmtHTGRGX0xvakFQRzFJNWx4TUZtU1VQVmtnUTVRQWlEYXBlRXJNWmhtM1M0bWJlcXRlbjRKMlFHZHJpelpmeTRjYnZqUGQtTkt3cEpqRklYd04yS1Z0SXdGa0Y5aXBnMG5JYXpGcGc3X0RrekY?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxPdjVhd0gtajhwVFprMUNmemxmMGYtQmw0amN6M3c5c3VnVnJ0N05PV0dyVjJ0V09fMkdzVFlvZDRRZ0VPQk5VbE5XMFlxT013VWl4VlN1VWlGYWxBdGxydFVEN1JkUW5BMTRCOWY3SXgwVC12Rlc1OFVIbS0zOVlwTGQ0LVFnM3lyZWdoR1VIY3oxSnQwVHd0U2hFdUhBYmt6WnJEWE9GQWdJNW1DRVNrNXBB?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxNMlo2YVcxejRBY1FnRU15Z1o3V1MzenRjUGRpVlpNTmFNLWxfemVtRmcyNUIxcUlndmhYUXFwb2lta0R4eVlvNzN6UVN6UFkwT0Iyel8tNm15RFpsSHFrZHZkUlR3b292YW5XV25xay1ubF80NFpycmxfcUJ2ZzlLU3ViV1NRemgtdXlsalF1dUNabGd5dmczM1EzT2hCbmtTb0JvQmpBQm5SS1FU?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNUUNnamh6SDVQY0xFTG95UHpNYUw5YlMyRFltQk5kazJ5emRJLUpELUhCdDFWdTQ2VU1DaUV2UzRzMjc0SVUzd2RrVzktdXo1MXNfSUtCSXhKNzZXMl8wR1pGMmVBOHNGRXR0S3hZRmV0RHZvakRWbkxCaWNhNFVhR0hCcWVJNmxpQ3c?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxOR1VBLUMxWG9GXzZJWVdWM2kzSy0ycmUyeDRYRmJxTm5LNzNDd0xiVDM3MjVqa2dSNmpZWTZCZXhwZzBIRDhySExOZTdoYXU5VGtZeDNJS19aSUxERUREakFOSENWVDFON0hrMHdoRS1oMmF4STNUdUJkZzdXdUpuUGxaMi0xaldlWkVuNnVJZUVxMGlIMGdWNkVzRFVjdkFCc2w3QUQyMUxNOFk?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNTWROdHc0S3hGTEFFUmswNDVGMUxadkZ2ZU4yT0tCSXhQU0Z6anc5dkpySWlnbkJPeVVLUlpUUkVlTzVUS2REdFZiTWNTZ0lLSVd3MGFMVGlmZXlManduVzdOUm9BTHZEQmlKaVlma0FLTnNWZUNRU1FjVjJhWTVNZklPVjJTRXZMUlVReFVSNkJGZXAzd1V5M054ZnNxclk?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxOMTViZ0JDRXpJbkNPYXpDVHk5Rk0wam56R1loVE9UREtmNUdMN041b1pFdzJzTTU0QmdWam54UUZla1JQTWlWT09QSFVyUEZlZ3BiSTB5M2RmcWN6R2Q4Z2JmRm5SU3RKUnU0c2h3UjNNODl2RWVyRksyWnFhR1cxbjR2RWdkQ2JuT2xBS2hqb1hvQkdaX1pqTXdvbHVWMC13MTlnMm9rS3Y1TVhyMUVxdFRFSEFBdm9BYW5hOFlFSncwaGhLV2FnYTdGR21SY0l0YnNV?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPU3laYWVQZXdwNEs0ZmxOZ2RKTGU5X1hoa1pwSE9pMmtDS0twblQxRU9IR0s0MFY3dXptaG9ET0pSbVBTeFpGbnJOeUJyNnNVWkFWakFiY3k5UGlydW9JVEZtaUQ5bEI4bWI1R1A3YkVBTjhCTFZrblV5QUVtN2x0d01YUXFsOEllTURPY3FteVVBTUJXRnFlSnBrUWo3WU0?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQellmZ1ZFejhCWHFzUmEtUjlUZTRjZWRxaklWblhWYldqbGlYLTlJV0ROd2w2Nm1YaXU2clp6WjNob25iRmE4dG5PX2U4WlhtTm9vN2lDQkpuOV92R1NuUERlY0U5Y2pBeUFVbHdyTzh6bEJwbEdGeEFiY1RYVldPS09NTVppSjcwek9Ja1QwVmRWWmZRSnpsR2FCUTFaVU9lUjJCS25nNFk?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNdFZSODYwSGZHTTZTaUprVElfRTRzZDJ0dFpfUzluYkl0U1c0WG9HTnk4dWRuSm1OR1FyaXNPd3RvRVJPVGRNNjA0bHlvT3R5MXdpaXhjY2xjemRkOGp3VTNmeng3NXVURG9ldVBTbHN1ZEZQbmI1LWNnV2lQVlc0aFJFZnZvWGk3elZFV1k5TUJZU2VNYVo5NlM3UURQam5kZXFB?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNaTdyWjk1dmZBT2Vmeng5UndvTG10YVNpZDBzVjJ2OUtYaW1YbUNpRjZEdHJZVG1YeHV0MkNLSUVZdVBDWTZrOXpFNVlyaGJuNzlrNEdnVkNoc0kwTjBvWV9OWVlkSzd3aVN1LVVhR0Vva0gxaDhmTVdKNlNKQ1QyUlVZbWlrYW51a2JrWg?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNbkFJOTNJT2h1NXhLa0pRS3h0RWdxc3FCX0l6RDQ5cy1QWXRpcDNRcnZyS2YtRjF4UTlDbzNuUlBXZk9GLVM5UEc1QkxIaC1oaHRaWVRuRmxzWGJUbUFUMEh4aUljVFVoZENOM1JGaEZkYUEtNlJCV3BudEI1bTR4RF94RmdfeHJ3MVlBdXpET013QW8td3ozYlBMQWM2c0lxOXlYRWdfZ0JDMmM4dldSSTU5NU1TbXM?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQR3V5MlpKaWtBVWpuZEt2b25BU3FzblBlbG5VX0ZzR1lMamg1Z1RNMHdoZFdXaHhoNmhiS19HZXhQYlYxUEZyYmJVUlVFd0cxYmZMVXk1MmxUTXRFVlJPQlJyWHFwVnFXVl9vVzRUSjJ6OHcxRzNvYTRZVEVxV3dPSlpqREhvcFpuckYyejdNZGJiMkhENDBva3pR?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
