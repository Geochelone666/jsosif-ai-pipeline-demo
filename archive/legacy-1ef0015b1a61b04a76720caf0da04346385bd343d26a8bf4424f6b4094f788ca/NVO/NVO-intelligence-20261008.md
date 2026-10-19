# NVO Intelligence Demo

- ticker: **NVO**
- Report as_of: **2026-10-08**
- Market data as_of: **2026-10-07**
- Quant sources: https://finance.yahoo.com/quote/NVO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVO/key-statistics/
- AI analysis snapshot as_of: **2026-10-03** (retained; this run refreshes market data only)
- Snapshot note: the report-date daily bar may be intraday until the US market closes; its Close field is provisional. News, peers, earnings, EDGAR and macro sections reuse their existing snapshots.
- Market data fetched_at (UTC): **2026-10-08T04:17:40.156008+00:00**
- AI status: **Available**
- AI model: **gemini-3.5-flash-lite** (25 Google News RSS headlines -> AI extraction and classification; free-tier grounding unavailable, using RSS + AI)

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 38.2600 |
| Return 1D (%) | 1.9451 |
| Return 1W (%) | 0.9232 |
| Return 1M (%) | -17.8970 |
| Return YTD (%) | -21.0495 |
| Return 1Y (%) | -31.9383 |
| Annualized volatility (%) | 45.7727 |
| Beta vs SPY | 1.0266 |
| Max drawdown (%) | -43.6699 |
| Sharpe (rf=0) | -0.6102 |
| P/E (trailing) | 9.35 |
| P/B | 5.09 |
| EV/EBITDA | 1.50 |
| Revenue growth (%) | 2.10 |
| MA50 | 43.8034 |
| Close vs MA50 (%) | -12.6553 |
| MA200 | 44.4586 |
| Close vs MA200 (%) | -13.9425 |
| RSI (14, Wilder) | 34.6927 |
| MACD (12,26) | -1.9714 |
| MACD signal (9) | -1.9657 |
| MACD histogram | -0.0057 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVO': 255, 'SPY': 255}.

## TAILWINDS

### Novo Nordisk (NVO) Upgraded to Buy at Nordea. Here is Why
- Summary: Novo Nordisk (NVO) Upgraded to Buy at Nordea. Here is Why
- Date: 2026-06-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPMXByUFoxYkg4OUZtNDktTG9oNHZObnM3Ti1MV1NCN25BTjB4d0JpM242Zy1Sb0dXMGNMZENxeG11WEVkaWJibHNnSGJvTm1UWWdJV3RoeHpVWXlMVG0xZXBiTUNIckhtQnZEMU5sY2NZOWt0RExVTUprV0NUZjFseVFWSG1VSm9QNUtuZVk2cTVLQjFj?oc=5>

### Jim Cramer Reevaluates Novo Nordisk (NVO) as Wegovy Pill Adoption Accelerates
- Summary: Jim Cramer reevaluates Novo Nordisk as Wegovy pill adoption accelerates.
- Date: 2026-08-14 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPMUJDbmdDVTBnSkJuQWU3b0s5RUtkNXlyRFFKR0FudVcweUFrRGhMRmxjbHRWYlF1YUtaUkEzenJuakFMTnI5cV8zd2VXcUpPcW53N080QmlqaW55dERjY01ld09heFhQcE9yQWJOZnBiUXFDTjRXUnk5SkJBOEhHM1pjR2hvZUIwelVXd1hpTWhPaExSTEpGQVBCcWk?oc=5>

## HEADWINDS

### Novo Nordisk Targets Over Five New Blockbusters By 2030, But NVO Stock Slides On Growth Concerns
- Summary: Novo Nordisk Targets Over Five New Blockbusters By 2030, But NVO Stock Slides On Growth Concerns
- Date: 2026-09-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNRG54c1JnN2xUZGVwSm5Oc0FraVZoY2dvbWZpd3o1VnBKTGFNSEZuNk50WDdXbGxWc2hpbkxhdUk1X3czalRiRlRMZEpTMmF6NnRpaUVQQzRTTlNianRmOFVNQmxUeDg3TnFjaXRpMDFKbnlRWmdhZGM1cjRvTDItVjFFdFhaZ1BQT0JZVFkxbTZQc0dTU2c?oc=5>

### Novo Nordisk Stock Slides After Unveiling Long Term Pipeline Growth Targets
- Summary: Novo Nordisk Stock Slides After Unveiling Long Term Pipeline Growth Targets
- Date: 2026-09-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxPMWMzX1oxVjE3N1Rsb1RwOTNnbWFxcFNyYlQ2eDNISFMxMTBweEZ0cU9kQzFZUkIxeG5XSmFCWGFZQVlnMEF4aDhlckZZQURybkxmZDFKN3hXUjhQbGt3cldBeXZPQlFVX05ESDV1b3NTZ2xEUExnNjREeC1uLTB4c3F0OGF5a0JxdjFOMUhR?oc=5>

### Novo Nordisk Stock Slips as Pill Strategy Reframes Obesity Race
- Summary: Novo Nordisk Stock Slips as Pill Strategy Reframes Obesity Race
- Date: 2026-08-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNM2tNWHBHSDI2THlXbjdIUTVqMGJrZWtpNVlYNl91eXZDdTlENWxDeGxUaWJGX3ZSWlJGR3RMU2dFZWd3OV84ZXN2YVZYamFmMzlaMHlwMk5qYlBtR19qMm5saWRDaUwyUmJUYW4wTGdGTm1aTlpZRkRTa3c3SWhPX25Ka205OW9oV3I1Z3RCaXpaU0Jj?oc=5>

### Novo shares slide as drugmaker lays out post-Wegovy growth strategy
- Summary: Novo shares slide as the drugmaker lays out its post-Wegovy growth strategy.
- Date: 2026-09-21 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNZFAtUVFDOHFJMHFvZHBWSll4SFJZM1VTQWhWX2g0VkVPSTVUclpDVlpCX2gzRVY3SEFTV3liTTgzU1BNcm9aX01TVHlsdjNKbS1UbGhtU3lhXzFpTjNLR1pvZGk3cUZkLVI2Wk9qaS1mOTZPYVhDaXBacjJrZS0zamZSdEpVcWtRWWfSAY8BQVVfeXFMTzZOWXBXMzNpbjZJa1RhLXg5MnNhYS03dnVHTllSekFJWXppa09zbkpOVF9QX1k3SHdhejNPYjRZbnhybGpjNmdEbW43RGtiUVdUTTdrbmJNTE5BaGN6cmtEczNOQnM5UEtRMW42dFVmMEw1SnI3aEhHeDJ5MU9yS1N1dXpUeTlWekE0RTFwOTA?oc=5>

### Novo Nordisk (NVO) Stock May Be Cheap As GLP 1 Legal Risks Shift
- Summary: GLP 1 legal risks shift while Novo Nordisk stock may be cheap.
- Date: 2026-08-27 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOY0ZzNHRRRUNvVXNrQlVkTzNrSTJfaXNxcjMzaWUwbHduMUFiN2JybGd1ejZMbmo0U3J3NEg0SGZwTFkyaGRGTjhCdEpmNzFhdXdfU05EeF9OMXZFaGV0ejNPSTlQVzdWZXFiTmViRVFvckFOQXVYWWJPUW11aEtmN244T1EwOGVDR2E2X0ctQUhGUl85bGc?oc=5>

### Novo Nordisk (NVO) Trial Setback Hits Sentiment, Is The Stock Still Cheap?
- Summary: A trial setback hits sentiment for Novo Nordisk.
- Date: 2026-08-01 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQQy1ZR1B1Z2pEZUhFaGpJM0U4dEV1YnRzU0FuT3VEV1hTM2lCMWtiaXpxQ0V1ZmxkckFhVWhfX1E3ajhuWktaOTQwc3A1MVhLWVhleGZaOURBTW9ZMVlxMWFld3JIZDlUOElLZ196YTU1OVgzSHZ5dmRIeE0xbUMwRUM2dHBSQUlPZFFhWmJqMUYtZzJXWlE?oc=5>

### Why Novo Nordisk Stock Just Crashed
- Summary: Novo Nordisk stock just crashed.
- Date: 2026-09-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxNRE9NVEdNSWVIMkFUd21FWWJHcklVQ09NSmVnWW91Um9fczRZYl9JZEZVNllmUkVQcFF3WmZGSTRkX2hqamx1YnBrdWVqdWlCdGR0Y0dPbEQ4QUtlMXVqNklCalprQWxaakNqT2g4VW1KVlhvQlZqVWFJZ0xkQTY1bWhHbmk?oc=5>

## CATALYSTS

### Novo Nordisk (NVO) Stock Looks Reasonable Given Uncertain Long Term Earnings
- Summary: Novo Nordisk (NVO) Stock Looks Reasonable Given Uncertain Long Term Earnings
- Date: 2026-10-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxOcndvMUNwT1BaRGtJUEhsTlNCUnY3ZWVEa3pXNExvcUt5VlNyZ1JjVEN1VFpHa0MwT0tHanZ3QmlLUm9pZkM5cENXSkluSjJkUldFNDFzdUhTVlFoQ2ZDSTZvRnpEbEs1c3R5TFBPeHdlZ04zcWQ5YjBXU3RUbFNMbDc5NlcwZ1lCLTBSTVdZMWZ5TlJVcThkczJsMlJBLW9kd0lEVWNnRWE5N18waWREb0FncUF1bklJakJ3a3FHSThSWlZWSm1FT2d4dVRLTWdscUpnaGhjZnlwUmPSAeABQVVfeXFMTjVtcTl4MXAxVFN5MnN4MGRMVlNjNDZIVW5fb0xQOE9GRnA4RTU0emR2aV90NlFOamtCME41TGxKaUNId0tTcmFZQ2x6NkU1WnhkN3lHZU9CUXd5S25kTTFJVUM5WGxTV09uYlppUnFRY2ZMOTRjd0twM1dpMWMxdHNoZzZIclZva3JHbUNacDExTGV4V1k3UFZMbzNoTXdTSzNKZ0xiODVtTjN6TGRtSHV5RjcyNnNVdUZ3ekk2aDBEWWRMMjdWeDBVeGVWLUVnN1NhZ2ZmdzU3WUJLUjVTQUs?oc=5>

### Novo Nordisk (NVO) Stock May Be 48% Undervalued On Medicare GLP 1 Coverage
- Summary: Novo Nordisk stock may be 48% undervalued on Medicare GLP 1 coverage.
- Date: 2026-07-03 | Impact: high | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQeGdsX3ZZQlZOenVVZGhidEpheEp6NmxLN0pIYlNrODNNQmlfWVc5SEt4dzBEMVJyLXJGZFVJb08xOVZEOFRubU5abkZKb0dkQlZpaFhjLWxaMENfeElBMEstZDBudlA2dmZGMmFQUVhCU0s1VnhLd1VvWXN6VnFGV1VUaTNKVHpTSDRIYUhsTzFhWlFSUFE?oc=5>

### Novo Nordisk: After A 70+% Drop, It's A Great Investment (NYSE:NVO)
- Summary: Seeking Alpha article states Novo Nordisk is a great investment after a 70+ percent drop.
- Date: 2026-09-29 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNaXdDVTZfeTdOOUFrbWJvVE5IS0ZYbFlseG96bnFtR2VPTlJjXzJqVXNrTkQtTUYxVUQxRGpEVFFtbGhPaU52YnlGTTdiZ1lFY21SS2FhTEpFd2RRcjBPUjlkNjU2eFdfeU1fd01BUHVLQjI5SFRuVHlIM1BpM0piSTRPV1h3cDZSaGpoNTZreTM2N2ZWUS1ENUpyam9XdEFCcFZhWl9KN3Q?oc=5>

## RISKS

### FDA has identified no safety or efficacy data deficiencies, but facility work extends a blood-clotting treatment's review.
- Summary: FDA identified no safety or efficacy data deficiencies, but facility work extends a blood-clotting treatment's review.
- Date: 2026-10-03 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxNQS1YYmNiQUtZaTA1c0U5aXVVdldNMXpicFNXWWlDNFJmZzZfVjgxdUszeDVHWFlfMXZJMDl1YWE1c0c1dHd3NjBFS3NOX19idnN4RExhS0IxcWotdGRrVk1NbFg5dEhLTDhlb2JEcTBYMG5wd21GVkFBUWlUUGFjcnEzR0R0b1BRc3Vocmt6MVJOd1pSVGE4SUJWQzdXTWp1eGlTR1o2WHNmX2V1elJ2MlhmVEVrYi1WR0ZOSmNn?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (USD) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVO** | **9.35** | **5.09** | **1.50** | **2.10** | **168,893,218,816.00** | **-31.94** |

Peers fetched as_of: 2026-10-08; NVO reuses existing data (market data as_of: 2026-10-07); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment Rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index | CPIAUCSL | 334.13 | 2026-08-01 |
| Federal Funds Effective Rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |

## LATEST FILING (EDGAR)

- Form: N/A
- Filing date: N/A
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: N/A

SEC requests use the demo placeholder contact email contact@example.com. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilAFBVV95cUxPMXByUFoxYkg4OUZtNDktTG9oNHZObnM3Ti1MV1NCN25BTjB4d0JpM242Zy1Sb0dXMGNMZENxeG11WEVkaWJibHNnSGJvTm1UWWdJV3RoeHpVWXlMVG0xZXBiTUNIckhtQnZEMU5sY2NZOWt0RExVTUprV0NUZjFseVFWSG1VSm9QNUtuZVk2cTVLQjFj?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPMUJDbmdDVTBnSkJuQWU3b0s5RUtkNXlyRFFKR0FudVcweUFrRGhMRmxjbHRWYlF1YUtaUkEzenJuakFMTnI5cV8zd2VXcUpPcW53N080QmlqaW55dERjY01ld09heFhQcE9yQWJOZnBiUXFDTjRXUnk5SkJBOEhHM1pjR2hvZUIwelVXd1hpTWhPaExSTEpGQVBCcWk?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNRG54c1JnN2xUZGVwSm5Oc0FraVZoY2dvbWZpd3o1VnBKTGFNSEZuNk50WDdXbGxWc2hpbkxhdUk1X3czalRiRlRMZEpTMmF6NnRpaUVQQzRTTlNianRmOFVNQmxUeDg3TnFjaXRpMDFKbnlRWmdhZGM1cjRvTDItVjFFdFhaZ1BQT0JZVFkxbTZQc0dTU2c?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPMWMzX1oxVjE3N1Rsb1RwOTNnbWFxcFNyYlQ2eDNISFMxMTBweEZ0cU9kQzFZUkIxeG5XSmFCWGFZQVlnMEF4aDhlckZZQURybkxmZDFKN3hXUjhQbGt3cldBeXZPQlFVX05ESDV1b3NTZ2xEUExnNjREeC1uLTB4c3F0OGF5a0JxdjFOMUhR?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNM2tNWHBHSDI2THlXbjdIUTVqMGJrZWtpNVlYNl91eXZDdTlENWxDeGxUaWJGX3ZSWlJGR3RMU2dFZWd3OV84ZXN2YVZYamFmMzlaMHlwMk5qYlBtR19qMm5saWRDaUwyUmJUYW4wTGdGTm1aTlpZRkRTa3c3SWhPX25Ka205OW9oV3I1Z3RCaXpaU0Jj?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNZFAtUVFDOHFJMHFvZHBWSll4SFJZM1VTQWhWX2g0VkVPSTVUclpDVlpCX2gzRVY3SEFTV3liTTgzU1BNcm9aX01TVHlsdjNKbS1UbGhtU3lhXzFpTjNLR1pvZGk3cUZkLVI2Wk9qaS1mOTZPYVhDaXBacjJrZS0zamZSdEpVcWtRWWfSAY8BQVVfeXFMTzZOWXBXMzNpbjZJa1RhLXg5MnNhYS03dnVHTllSekFJWXppa09zbkpOVF9QX1k3SHdhejNPYjRZbnhybGpjNmdEbW43RGtiUVdUTTdrbmJNTE5BaGN6cmtEczNOQnM5UEtRMW42dFVmMEw1SnI3aEhHeDJ5MU9yS1N1dXpUeTlWekE0RTFwOTA?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOY0ZzNHRRRUNvVXNrQlVkTzNrSTJfaXNxcjMzaWUwbHduMUFiN2JybGd1ejZMbmo0U3J3NEg0SGZwTFkyaGRGTjhCdEpmNzFhdXdfU05EeF9OMXZFaGV0ejNPSTlQVzdWZXFiTmViRVFvckFOQXVYWWJPUW11aEtmN244T1EwOGVDR2E2X0ctQUhGUl85bGc?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQQy1ZR1B1Z2pEZUhFaGpJM0U4dEV1YnRzU0FuT3VEV1hTM2lCMWtiaXpxQ0V1ZmxkckFhVWhfX1E3ajhuWktaOTQwc3A1MVhLWVhleGZaOURBTW9ZMVlxMWFld3JIZDlUOElLZ196YTU1OVgzSHZ5dmRIeE0xbUMwRUM2dHBSQUlPZFFhWmJqMUYtZzJXWlE?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxNRE9NVEdNSWVIMkFUd21FWWJHcklVQ09NSmVnWW91Um9fczRZYl9JZEZVNllmUkVQcFF3WmZGSTRkX2hqamx1YnBrdWVqdWlCdGR0Y0dPbEQ4QUtlMXVqNklCalprQWxaakNqT2g4VW1KVlhvQlZqVWFJZ0xkQTY1bWhHbmk?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxOcndvMUNwT1BaRGtJUEhsTlNCUnY3ZWVEa3pXNExvcUt5VlNyZ1JjVEN1VFpHa0MwT0tHanZ3QmlLUm9pZkM5cENXSkluSjJkUldFNDFzdUhTVlFoQ2ZDSTZvRnpEbEs1c3R5TFBPeHdlZ04zcWQ5YjBXU3RUbFNMbDc5NlcwZ1lCLTBSTVdZMWZ5TlJVcThkczJsMlJBLW9kd0lEVWNnRWE5N18waWREb0FncUF1bklJakJ3a3FHSThSWlZWSm1FT2d4dVRLTWdscUpnaGhjZnlwUmPSAeABQVVfeXFMTjVtcTl4MXAxVFN5MnN4MGRMVlNjNDZIVW5fb0xQOE9GRnA4RTU0emR2aV90NlFOamtCME41TGxKaUNId0tTcmFZQ2x6NkU1WnhkN3lHZU9CUXd5S25kTTFJVUM5WGxTV09uYlppUnFRY2ZMOTRjd0twM1dpMWMxdHNoZzZIclZva3JHbUNacDExTGV4V1k3UFZMbzNoTXdTSzNKZ0xiODVtTjN6TGRtSHV5RjcyNnNVdUZ3ekk2aDBEWWRMMjdWeDBVeGVWLUVnN1NhZ2ZmdzU3WUJLUjVTQUs?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQeGdsX3ZZQlZOenVVZGhidEpheEp6NmxLN0pIYlNrODNNQmlfWVc5SEt4dzBEMVJyLXJGZFVJb08xOVZEOFRubU5abkZKb0dkQlZpaFhjLWxaMENfeElBMEstZDBudlA2dmZGMmFQUVhCU0s1VnhLd1VvWXN6VnFGV1VUaTNKVHpTSDRIYUhsTzFhWlFSUFE?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNaXdDVTZfeTdOOUFrbWJvVE5IS0ZYbFlseG96bnFtR2VPTlJjXzJqVXNrTkQtTUYxVUQxRGpEVFFtbGhPaU52YnlGTTdiZ1lFY21SS2FhTEpFd2RRcjBPUjlkNjU2eFdfeU1fd01BUHVLQjI5SFRuVHlIM1BpM0piSTRPV1h3cDZSaGpoNTZreTM2N2ZWUS1ENUpyam9XdEFCcFZhWl9KN3Q?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxNQS1YYmNiQUtZaTA1c0U5aXVVdldNMXpicFNXWWlDNFJmZzZfVjgxdUszeDVHWFlfMXZJMDl1YWE1c0c1dHd3NjBFS3NOX19idnN4RExhS0IxcWotdGRrVk1NbFg5dEhLTDhlb2JEcTBYMG5wd21GVkFBUWlUUGFjcnEzR0R0b1BRc3Vocmt6MVJOd1pSVGE4SUJWQzdXTWp1eGlTR1o2WHNmX2V1elJ2MlhmVEVrYi1WR0ZOSmNn?oc=5

## Demo notes and limitations

- Multi-ticker local demo; AI items require human spot checks; RSS coverage is not guaranteed.
- Free-tier Gemini grounding (google_search tool) returned 429; the demo uses Google News RSS + plain-text AI extraction.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
