# PFE Intelligence Demo

- ticker: **PFE**
- Report as_of: **2026-10-08**
- Market data as_of: **2026-10-07**
- Quant sources: https://finance.yahoo.com/quote/PFE/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PFE/key-statistics/
- AI analysis snapshot as_of: **2026-10-03** (retained; this run refreshes market data only)
- Snapshot note: the report-date daily bar may be intraday until the US market closes; its Close field is provisional. News, peers, earnings, EDGAR and macro sections reuse their existing snapshots.
- Market data fetched_at (UTC): **2026-10-08T04:13:21.411146+00:00**
- AI status: **Available**
- AI model: **gemini-3.5-flash-lite** (25 Google News RSS headlines -> AI extraction and classification; free-tier grounding unavailable, using RSS + AI)

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 28.0000 |
| Return 1D (%) | 1.8182 |
| Return 1W (%) | -1.8233 |
| Return 1M (%) | -1.5817 |
| Return YTD (%) | 18.2539 |
| Return 1Y (%) | 14.0605 |
| Annualized volatility (%) | 21.0347 |
| Beta vs SPY | 0.2938 |
| Max drawdown (%) | -15.7243 |
| Sharpe (rf=0) | 0.7327 |
| P/E (trailing) | 36.84 |
| P/B | 1.87 |
| EV/EBITDA | 8.23 |
| Revenue growth (%) | 2.60 |
| MA50 | 27.4974 |
| Close vs MA50 (%) | 1.8278 |
| MA200 | 25.8599 |
| Close vs MA200 (%) | 8.2756 |
| RSI (14, Wilder) | 52.1671 |
| MACD (12,26) | 0.1012 |
| MACD signal (9) | 0.2140 |
| MACD histogram | -0.1128 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PFE': 255, 'SPY': 255}.

## TAILWINDS

### Why Pfizer (PFE) Stock Is Trading Up Today
- Summary: Why Pfizer (PFE) Stock Is Trading Up Today
- Date: 2026-08-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPWkpvYTBGdzNJQl9TUVJrTXJUbVFqWTBwcFEwOXlSeDBacHhJazhrWjF2dldkTkZxTkk2V29NQ0tRam5FclRQNkpKYlpIVFhiaDJYN3M3UDZlTlFsZW1tNktUUGRxWkhrbDlmZ0tGX2dQODdWbkNublRDRnhuZFZBaEdacWRTX2sxOHA4VzBaOFRjSmc?oc=5>

### Pfizer Rises Almost 7% Post Q2 Results: How to Play the Stock
- Summary: Pfizer Rises Almost 7% Post Q2 Results: How to Play the Stock
- Date: 2026-08-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQSk9ITXFpQ3oxNHN0OGwzMDgxZ0UtajB4RGFmamhVLW9OOWJVYl9pVTI2X1ZJZWNTUzBnZi04aVdhUjRWRFdUMjRDdGVXNGJkaTB0VGgxTVQwVDFYUGZzTUZ5MEEtMld2WUJyVG91djFGSV9Fd0JBWUFhYS1vbjdDQ3N5WjY2bjBoRlRrcG1reTI?oc=5>

### Pfizer (PFE) Outpaces Stock Market Gains: What You Should Know
- Summary: Pfizer (PFE) Outpaces Stock Market Gains: What You Should Know
- Date: 2026-06-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNMTN3Q2M3elVjNGhhMU01N2p4SUFiUEZLdmJTVWRjeFBwVEpVZm1KQl83M21hbFplb2Y1ckZYM2loNVJsb2l4TGtaSjZEMWFRSDB2cFFsT25mTHdNT0h3aVdwU2I5ODZjb3pKckRSZ2VWd1htTWVHODR2RHU4ZFVVcWd2SUtuclY0Ql9ac1dMSXl2VTNnNGRGUkd2NEd6UQ?oc=5>

### Pfizer (PFE) Could Be 12% Undervalued Following Raised 2026 Revenue Guidance
- Summary: Pfizer could be 12% undervalued following raised 2026 revenue guidance.
- Date: 2026-08-05 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQam9Db19TdF9ySkFGdlZ1dDVTMkVHVmQ2MTVZUGd4ZzN0Z2xHdnQ3OFZjRUtJVUZRQVl5cEV2dW02b3VPYkRzdHJUcktKRjBxcVNGVFJKYkhramFtVXlObVU4YkJzLTZEVThJV2xia1cwTUtkSmh4OW5SYmNKOFV4ak51bG5BcWdmNjdPTFlFWllaM1RoM2lFYVlMNTQ?oc=5>

### Pfizer (PFE) Stock Could Be 10% Undervalued After Recent Results
- Summary: Pfizer stock could be 10% undervalued after recent results.
- Date: 2026-06-20 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNRUxiNTR1QWl5bl9QWVVWaUZQR2FHdm11VTJrODU1RGVhc1daSUJXSFNwQlBBakZDZU81T1ZZdjlyM0VTcDVvb0RxVHBLQ3MwS2R0MlA5RTdvS3VyQXk1ZUJka29DQTIzOC1yS2tFLTZVTmxaSEZLS185b0RnaXZJZVI3ZmFEM0FEdG1KMGNPUjNPaDRV?oc=5>

## HEADWINDS

### Pfizer (PFE) Stock Sinks As Market Gains: What You Should Know
- Summary: Pfizer stock sinks as the market gains.
- Date: 2026-10-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNalNqTHVMRUpwVUdxYjdKODgtUkhLcVk2S1lkMEF3dzlOOVN4QnpRdmZiVkxHRF9Ec3RPMjNsMWI2UnFvalJxVDJ0Y3RhWEQtcDI1VkJRS3FBR3ExWjNsTVBzNUxkRjNqUTRFVUI1WnZxRzRFSF9CT096RHNJUjUySHdpM09aZ2ItUnM0Q0N2cS1xWVpib1lNenZB?oc=5>

### Pfizer (PFE) Stock May Be Overvalued After Overseas Pricing Deal
- Summary: Pfizer stock may be overvalued after an overseas pricing deal.
- Date: 2026-09-23 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNcHo4Q19nNUItc0JqTXpBakZydkN0YkZfZW1xdWxDbGN3dy1DcHItV2RMdnZnSzBqN0E1TVN6T1V3SDUzS3puOTNEZ2tvcE9wWXUxakUxNVZVNWxtcHdLZ2N6T05DVFRUc1c0S2c4cm1meW81LWtIZWFGLUlfQjV6bzJSM3k2TlBjSE05S3pSdzd5WUtUTWc4VFQ5c3o?oc=5>

### Pfizer (PFE) Stock Declines While Market Improves: Some Information for Investors
- Summary: Pfizer stock declines while the market improves.
- Date: 2026-06-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNY0tRMEFHVTZfMl9weDBXMGdVSEFuVWRrN3ZtTk1kV1ZvczlnQ0hwMk5tX19NU0pBS0VfZWhERlNJelJzWGNLQWdHR2xPVGh5OXJVVGdBa3AtSnZMQlIwQTM1QUV5OEY1cFU2RUxhLVJ0Y1VWbG1PcmFUZm1HS05MamszX1k0QjJFRU5nWG9VN2ZKb2dDXzBZSmJTeEs?oc=5>

### Pfizer (PFE) Stock Sinks As Market Gains: Here's Why
- Summary: Pfizer stock sinks as the market gains.
- Date: 2026-07-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNd1Q0MzYyc0JtUmFoanl5dGpTem9jcEdKX3lNLVRyb2x2Zk9nYW1BeW9RLWRJMGYzSmQ1Rm9QZHZ1MWZ1UkpwSXdCSk52dms0UF9SV2UxeC1VelVUaFdockhrWjhQejFHQzBxdWlBanp0UkFIeXBrczZGMVNHNkhsdHIzNHp3RkVJelI4VG5LWTNnUml6SEMwUy1n?oc=5>

### Why Is Pfizer (PFE) Down 4.5% Since Last Earnings Report?
- Summary: Pfizer is down 4.5% since its last earnings report.
- Date: 2026-06-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxOQnhFM0M5N1pScy1lck1qRFFUTE5EZDdXNnpjNF9aLVdQWi10enBReHl5U1IyV2JwVHNJMEpKZ19BSjB0OHlQeUl6ODlOMjF1YWw2YjRMNzNyRm01X2JUSHNGZGp6ejRnWG1LZ2JMSTlWenowQUhRUnY0UU9xVm5kSU9XVnRTYm1nbzI1bjVJMA?oc=5>

### Pfizer (PFE) Falls More Steeply Than Broader Market: What Investors Need to Know
- Summary: Pfizer falls more steeply than the broader market.
- Date: 2026-06-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPMEhoNTl1UEU0dVZJV01xQ0FaZks3OE5QZ1VubGNlYUNTOUZZM0M5dkxxeWFaRzdtSjMxYkh3dzc0LWtHOHdkYzJxVUk3YXBVbTRnSE56ZnRmRFVhRHktbF9QX3hTN2VWMHpwUkJOVllHakNhRTc0QWhEeV9BdXdnTzlXLWNHZVV6Y3F4SkRPakloVjJsZ24zUkp3?oc=5>

## CATALYSTS

### Pfizer (PFE) Stock Looks Fully Valued As Earnings Run Ahead Of Value
- Summary: Pfizer (PFE) Stock Looks Fully Valued As Earnings Run Ahead Of Value
- Date: 2026-09-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPYkptSERKWlNCcWR6NjRwTm84cmJtYXhlaUdzd2V3V1czLXhhMjNXSWhWSTRzNjkyaEo0RW5PRjB1N1ZYakdwUW5sWkJzbEVadzNLQm5CLWh0NF9FV1JwZ1hEYWs1ampMSXlMOWdRbGFhYlZjd0Z2cFpCR245U05tMUtQNFdNbi0zV0kza2x1VG0yX2pXOVVPOA?oc=5>

### Pfizer (PFE) Stock Looks Reasonable On Returns But Stretched On Earnings
- Summary: Pfizer (PFE) Stock Looks Reasonable On Returns But Stretched On Earnings
- Date: 2026-08-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPb3BDOE9oNEZmeWwxQnpBV1gyVDJqVVJidTZBOEhOYmo4c3JTUDAxNXdxY1hCNUlYSVNCeHNlX2dsSXVMYUpZTWVfRWk1OC1QRkFhTU1NcmJ4R2p2TjZPU1hzUFdaN3lLX3VraU9pZ182R3dUMlpGMzJaM1JDTld6VVB2VFJyeHFaVWZFQVFObXFFQnhfRjRzVE9MX2lWZ2c?oc=5>

### Pfizer Stock: Wall Street Sees a Rebound, Here’s Our Price Target
- Summary: Pfizer Stock: Wall Street Sees a Rebound, Here’s Our Price Target
- Date: 2026-08-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOTjlqakVlbjYwdzhzRGxlck1laUFkdjdwX21vbm9TNi1LcF9XRGZmMk1hQVd2SHRLd3NhMURlT2ZYTVpxZC1TZThyMEQ0RVdZRzJkU01PQXI4OUl4dU1RTjY5VXg2Q21RMGk2dlViWXM3Y0s5ZmRxNXJOUl9OaXEwVkEyNXRSX1NPal9CYWhFVEZNQmdYS2txTURR?oc=5>

### Why 1 Wall Street Analyst Thinks Pfizer (PFE) Stock Could Soar 38%
- Summary: One Wall Street analyst thinks Pfizer stock could soar 38%.
- Date: 2026-05-25 | Impact: high | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQclNCTEs4YUVmSXlDZ3dwX2RfaUpQeUVuWWQ2UTRrdVVQaE0yZVlfejdpNFZoUk84aUxFZ040VjVIWWV3WGpxMkRfdlI1cWFaakJPZUNyWklXWWtqaTdBc1U5WWNuQ2dFcUkybUx6V2lIU2w5YlgxMUhieExfbndiZ1lDRkw0b3EycDd3VjZsYmlRTzdj?oc=5>

## RISKS

### Pfizer (PFE) Stock Looks Fairly Priced With Pipeline Risks In View
- Summary: Pfizer stock looks fairly priced with pipeline risks in view.
- Date: 2026-07-16 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPVWVkT0lTcnVOZXlXMG9STFhCUEtqYzdPTkFLTWlYeXZaZV9JOXpNTW1xRkR6akZ1LTJGa3g3MHlmTWNOYnBWNWVSMmwzeEFtbXJ4M0tMQ2ttR3FfQlA5UjBiTVhuN21HbVp2N21TRlYyQzU4US1Qamt4NXp5YmVqLVBqeUpGZzJRMHNJTlFhcHg0U05jbGtBRHpR?oc=5>

### Pfizer (PFE) Faces Fresh Legal Questions, Does It Look Fully Valued?
- Summary: Pfizer faces fresh legal questions.
- Date: 2026-08-19 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQbkRWMWlhUjh0andoajdNblA4cG55Tk1wa25vZHFNUzF3S2RqQWRUNlFMbU5wdlBSaDZlTGFOc3F3dVlMWlhGdzZma21lUkQ0UDVpc3djQWh6c1FxM2duNUVSdExrXzhmZ2l1TExlNnVGOWtyelZINkktMmU4UEEyaDlhTWdEeVduR0l0YVhZdS1QczVCTjAtNQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (USD) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PFE** | **36.84** | **1.87** | **8.23** | **2.60** | **159,590,858,752.00** | **14.06** |

Peers fetched as_of: 2026-10-08; PFE reuses existing data (market data as_of: 2026-10-07); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment Rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index | CPIAUCSL | 334.13 | 2026-08-01 |
| Federal Funds Effective Rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-04
- Revenue (latest available single quarter): 15,034,000,000.00 USD; period 2026-03-30/2026-06-28; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): -248,000,000.00 USD; period 2026-03-30/2026-06-28; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/78003/000007800326000095/pfe-20260628.htm

SEC requests use the demo placeholder contact email contact@example.com. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMikwFBVV95cUxPWkpvYTBGdzNJQl9TUVJrTXJUbVFqWTBwcFEwOXlSeDBacHhJazhrWjF2dldkTkZxTkk2V29NQ0tRam5FclRQNkpKYlpIVFhiaDJYN3M3UDZlTlFsZW1tNktUUGRxWkhrbDlmZ0tGX2dQODdWbkNublRDRnhuZFZBaEdacWRTX2sxOHA4VzBaOFRjSmc?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQSk9ITXFpQ3oxNHN0OGwzMDgxZ0UtajB4RGFmamhVLW9OOWJVYl9pVTI2X1ZJZWNTUzBnZi04aVdhUjRWRFdUMjRDdGVXNGJkaTB0VGgxTVQwVDFYUGZzTUZ5MEEtMld2WUJyVG91djFGSV9Fd0JBWUFhYS1vbjdDQ3N5WjY2bjBoRlRrcG1reTI?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNMTN3Q2M3elVjNGhhMU01N2p4SUFiUEZLdmJTVWRjeFBwVEpVZm1KQl83M21hbFplb2Y1ckZYM2loNVJsb2l4TGtaSjZEMWFRSDB2cFFsT25mTHdNT0h3aVdwU2I5ODZjb3pKckRSZ2VWd1htTWVHODR2RHU4ZFVVcWd2SUtuclY0Ql9ac1dMSXl2VTNnNGRGUkd2NEd6UQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQam9Db19TdF9ySkFGdlZ1dDVTMkVHVmQ2MTVZUGd4ZzN0Z2xHdnQ3OFZjRUtJVUZRQVl5cEV2dW02b3VPYkRzdHJUcktKRjBxcVNGVFJKYkhramFtVXlObVU4YkJzLTZEVThJV2xia1cwTUtkSmh4OW5SYmNKOFV4ak51bG5BcWdmNjdPTFlFWllaM1RoM2lFYVlMNTQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNRUxiNTR1QWl5bl9QWVVWaUZQR2FHdm11VTJrODU1RGVhc1daSUJXSFNwQlBBakZDZU81T1ZZdjlyM0VTcDVvb0RxVHBLQ3MwS2R0MlA5RTdvS3VyQXk1ZUJka29DQTIzOC1yS2tFLTZVTmxaSEZLS185b0RnaXZJZVI3ZmFEM0FEdG1KMGNPUjNPaDRV?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNalNqTHVMRUpwVUdxYjdKODgtUkhLcVk2S1lkMEF3dzlOOVN4QnpRdmZiVkxHRF9Ec3RPMjNsMWI2UnFvalJxVDJ0Y3RhWEQtcDI1VkJRS3FBR3ExWjNsTVBzNUxkRjNqUTRFVUI1WnZxRzRFSF9CT096RHNJUjUySHdpM09aZ2ItUnM0Q0N2cS1xWVpib1lNenZB?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNcHo4Q19nNUItc0JqTXpBakZydkN0YkZfZW1xdWxDbGN3dy1DcHItV2RMdnZnSzBqN0E1TVN6T1V3SDUzS3puOTNEZ2tvcE9wWXUxakUxNVZVNWxtcHdLZ2N6T05DVFRUc1c0S2c4cm1meW81LWtIZWFGLUlfQjV6bzJSM3k2TlBjSE05S3pSdzd5WUtUTWc4VFQ5c3o?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNY0tRMEFHVTZfMl9weDBXMGdVSEFuVWRrN3ZtTk1kV1ZvczlnQ0hwMk5tX19NU0pBS0VfZWhERlNJelJzWGNLQWdHR2xPVGh5OXJVVGdBa3AtSnZMQlIwQTM1QUV5OEY1cFU2RUxhLVJ0Y1VWbG1PcmFUZm1HS05MamszX1k0QjJFRU5nWG9VN2ZKb2dDXzBZSmJTeEs?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPbzhnZEtKelBoR1BFNmR0UmQxOUU0S1Vsb1pwZHRkM0VvOWNpVm1xbFpmMHNHVlVicllLU25EeGxvZnNOaktCNjQxLTFUWlRXaXc5aldjcl8teFU5am9BQUxGMVI5ZFdjOUNNeFVwYk5WVWZYb3FUTVZNSzBpOWFHVm9ReWRJMlhlNWxkZzdyWFFKb3ZiYm1oU01LNXQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNd1Q0MzYyc0JtUmFoanl5dGpTem9jcEdKX3lNLVRyb2x2Zk9nYW1BeW9RLWRJMGYzSmQ1Rm9QZHZ1MWZ1UkpwSXdCSk52dms0UF9SV2UxeC1VelVUaFdockhrWjhQejFHQzBxdWlBanp0UkFIeXBrczZGMVNHNkhsdHIzNHp3RkVJelI4VG5LWTNnUml6SEMwUy1n?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxOQnhFM0M5N1pScy1lck1qRFFUTE5EZDdXNnpjNF9aLVdQWi10enBReHl5U1IyV2JwVHNJMEpKZ19BSjB0OHlQeUl6ODlOMjF1YWw2YjRMNzNyRm01X2JUSHNGZGp6ejRnWG1LZ2JMSTlWenowQUhRUnY0UU9xVm5kSU9XVnRTYm1nbzI1bjVJMA?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPMEhoNTl1UEU0dVZJV01xQ0FaZks3OE5QZ1VubGNlYUNTOUZZM0M5dkxxeWFaRzdtSjMxYkh3dzc0LWtHOHdkYzJxVUk3YXBVbTRnSE56ZnRmRFVhRHktbF9QX3hTN2VWMHpwUkJOVllHakNhRTc0QWhEeV9BdXdnTzlXLWNHZVV6Y3F4SkRPakloVjJsZ24zUkp3?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPYkptSERKWlNCcWR6NjRwTm84cmJtYXhlaUdzd2V3V1czLXhhMjNXSWhWSTRzNjkyaEo0RW5PRjB1N1ZYakdwUW5sWkJzbEVadzNLQm5CLWh0NF9FV1JwZ1hEYWs1ampMSXlMOWdRbGFhYlZjd0Z2cFpCR245U05tMUtQNFdNbi0zV0kza2x1VG0yX2pXOVVPOA?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPb3BDOE9oNEZmeWwxQnpBV1gyVDJqVVJidTZBOEhOYmo4c3JTUDAxNXdxY1hCNUlYSVNCeHNlX2dsSXVMYUpZTWVfRWk1OC1QRkFhTU1NcmJ4R2p2TjZPU1hzUFdaN3lLX3VraU9pZ182R3dUMlpGMzJaM1JDTld6VVB2VFJyeHFaVWZFQVFObXFFQnhfRjRzVE9MX2lWZ2c?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOTjlqakVlbjYwdzhzRGxlck1laUFkdjdwX21vbm9TNi1LcF9XRGZmMk1hQVd2SHRLd3NhMURlT2ZYTVpxZC1TZThyMEQ0RVdZRzJkU01PQXI4OUl4dU1RTjY5VXg2Q21RMGk2dlViWXM3Y0s5ZmRxNXJOUl9OaXEwVkEyNXRSX1NPal9CYWhFVEZNQmdYS2txTURR?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQclNCTEs4YUVmSXlDZ3dwX2RfaUpQeUVuWWQ2UTRrdVVQaE0yZVlfejdpNFZoUk84aUxFZ040VjVIWWV3WGpxMkRfdlI1cWFaakJPZUNyWklXWWtqaTdBc1U5WWNuQ2dFcUkybUx6V2lIU2w5YlgxMUhieExfbndiZ1lDRkw0b3EycDd3VjZsYmlRTzdj?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPVWVkT0lTcnVOZXlXMG9STFhCUEtqYzdPTkFLTWlYeXZaZV9JOXpNTW1xRkR6akZ1LTJGa3g3MHlmTWNOYnBWNWVSMmwzeEFtbXJ4M0tMQ2ttR3FfQlA5UjBiTVhuN21HbVp2N21TRlYyQzU4US1Qamt4NXp5YmVqLVBqeUpGZzJRMHNJTlFhcHg0U05jbGtBRHpR?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQbkRWMWlhUjh0andoajdNblA4cG55Tk1wa25vZHFNUzF3S2RqQWRUNlFMbU5wdlBSaDZlTGFOc3F3dVlMWlhGdzZma21lUkQ0UDVpc3djQWh6c1FxM2duNUVSdExrXzhmZ2l1TExlNnVGOWtyelZINkktMmU4UEEyaDlhTWdEeVduR0l0YVhZdS1QczVCTjAtNQ?oc=5

## Demo notes and limitations

- Multi-ticker local demo; AI items require human spot checks; RSS coverage is not guaranteed.
- Free-tier Gemini grounding (google_search tool) returned 429; the demo uses Google News RSS + plain-text AI extraction.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
