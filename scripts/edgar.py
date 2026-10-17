"""SEC free APIs. Demo User-Agent uses a placeholder contact email."""
from datetime import date
import json
import os
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from data_utils import number, save, ticker_arg, ticker_file, as_of_date

def resolve_cik(symbol):
    # SEC uses the US listing symbol for Canadian dual listings.
    sec_symbol = symbol.removesuffix('.TO')
    if symbol.endswith('.PA'):
        return None
    cache = Path(os.environ['JSOSIF_SEC_CACHE']) if os.environ.get('JSOSIF_SEC_CACHE') else None
    if cache and cache.is_file() and time.time() - cache.stat().st_mtime < 86400:
        entries = json.loads(cache.read_text())
    else:
        entries = fetch('https://www.sec.gov/files/company_tickers.json')
        if cache:
            cache.parent.mkdir(parents=True, exist_ok=True)
            cache.write_text(json.dumps(entries))
    return next((str(row['cik_str']) for row in entries.values()
                 if row['ticker'].upper() == sec_symbol), None)

HEADERS = {'User-Agent': 'JSOSIF-demo contact@example.com (demo placeholder contact)', 'Accept': 'application/json'}

def fetch(url):
    headers = dict(HEADERS)
    headers['User-Agent'] = os.environ.get('SEC_USER_AGENT', HEADERS['User-Agent'])
    for attempt in range(3):
        # Serial pipeline plus a conservative 2 req/sec ceiling per process.
        time.sleep(.5)
        try:
            with urlopen(Request(url, headers=headers), timeout=30) as response:
                return json.load(response)
        except HTTPError as exc:
            if exc.code not in (429, 500, 502, 503, 504) or attempt == 2:
                raise
        except (URLError, TimeoutError):
            if attempt == 2:
                raise
        time.sleep(2 ** (attempt + 1))

def quarter_value(concept, CIK):
    data = fetch(f'https://data.sec.gov/api/xbrl/companyconcept/CIK{CIK.zfill(10)}/us-gaap/{concept}.json')
    candidates = []
    for obs in data.get('units', {}).get('USD', []):
        if obs.get('form') not in ('10-Q', '10-K') or obs.get('filed', '9999') > as_of_date().isoformat():
            continue
        try:
            duration = (date.fromisoformat(obs['end']) - date.fromisoformat(obs['start'])).days
            if 70 <= duration <= 110 and number(obs.get('val')) is not None:
                candidates.append(obs)
        except (KeyError, ValueError, TypeError):
            continue
    if not candidates:
        return None
    obs = max(candidates, key=lambda item: (item['end'], item.get('filed', '')))
    return {'value': number(obs['val']), 'period': f'{obs["start"]}/{obs["end"]}', 'unit': 'USD', 'fiscal_year': obs.get('fy'), 'fiscal_period': obs.get('fp')}

def main():
    symbol = ticker_arg()
    try:
        CIK = resolve_cik(symbol)
    except Exception as exc:
        CIK = None
        print(f'SEC ticker lookup unavailable: {type(exc).__name__}')
    data = {'ticker': symbol, 'cik': CIK, 'latest_filing': None, 'revenue': None, 'net_income': None}
    if CIK is None:
        data['error'] = 'N/A: SEC issuer mapping unavailable for this listing'
        save(ticker_file(symbol, 'edgar.json'), data)
        return
    try:
        recent = fetch(f'https://data.sec.gov/submissions/CIK{CIK.zfill(10)}.json')['filings']['recent']
        matches = [i for i, form in enumerate(recent['form']) if form in ('10-Q', '10-K') and recent['filingDate'][i] <= as_of_date().isoformat()]
        if matches:
            i = max(matches, key=lambda i: recent['filingDate'][i])
            accession = recent['accessionNumber'][i]
            data['latest_filing'] = {'form': recent['form'][i], 'filing_date': recent['filingDate'][i], 'accession': accession, 'url': f'https://www.sec.gov/Archives/edgar/data/{CIK}/{accession.replace("-", "")}/{recent["primaryDocument"][i]}'}
    except Exception as exc:
        print(f'SEC submissions unavailable: {type(exc).__name__}')
    for field, concept in [('revenue', 'Revenues'), ('net_income', 'NetIncomeLoss')]:
        try:
            data[field] = quarter_value(concept, CIK)
            if field == 'revenue' and data[field] is None:
                data[field] = quarter_value('RevenueFromContractWithCustomerExcludingAssessedTax', CIK)
        except Exception as exc:
            print(f'SEC {concept} unavailable: {type(exc).__name__}')
            if field == 'revenue':
                try:
                    data[field] = quarter_value('RevenueFromContractWithCustomerExcludingAssessedTax', CIK)
                except Exception as fallback_exc:
                    print(f'SEC revenue fallback unavailable: {type(fallback_exc).__name__}')
    save(ticker_file(symbol, 'edgar.json'), data)
    print(f'EDGAR: {sum(data[k] is not None for k in ("latest_filing", "revenue", "net_income"))}/3 data fields')

if __name__ == '__main__':
    main()

