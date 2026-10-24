"""Optional free FRED observations; no requests when no key is configured."""
from datetime import date
import json
import os
from urllib.parse import urlencode
from urllib.request import urlopen
from data_utils import number, save, as_of_date

CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', 'fred.json')
SERIES = {'UNRATE': 'Unemployment rate (%)', 'CPIAUCSL': 'Consumer Price Index (1982–1984=100)', 'FEDFUNDS': 'Federal funds rate (%)', 'NAPM': 'ISM Manufacturing PMI'}

def main():
    # Team key: project config first, then env var (legacy personal key).
    key = ''
    try:
        with open(CONFIG_PATH, encoding='utf-8') as f:
            key = json.load(f).get('api_key', '').strip()
    except (OSError, ValueError, AttributeError):
        # Unreadable, non-object or non-string api_key: fall back to the env var.
        key = ''
    if not key:
        key = os.environ.get('FRED_API_KEY', '').strip()
    if not key:
        save('fred.json', {'available': False, 'reason': 'no key'})
        print('FRED SKIP: no key; 0 indicator rows')
        return
    indicators = []
    for series_id, name in SERIES.items():
        row = {'series_id': series_id, 'name': name, 'value': None, 'date': None}
        params = urlencode({'api_key': key, 'series_id': series_id, 'file_type': 'json', 'sort_order': 'desc', 'limit': 100, 'observation_end': as_of_date().isoformat()})
        try:
            with urlopen('https://api.stlouisfed.org/fred/series/observations?' + params, timeout=30) as response:
                observations = json.load(response)['observations']
            for obs in observations:
                value = number(obs.get('value'))
                if value is not None:
                    row.update(value=value, date=obs['date'])
                    break
        except Exception as exc:
            # Never print the request URL containing the API key.
            print(f'{series_id} unavailable: {type(exc).__name__}')
        indicators.append(row)
    save('fred.json', {'available': any(row['value'] is not None for row in indicators), 'as_of': as_of_date().isoformat(), 'indicators': indicators})
    print(f'FRED: {len(indicators)} rows; {sum(r["value"] is not None for r in indicators)}/4 values')

if __name__ == '__main__':
    main()

