"""Capture bounded daily adjusted prices for offline candidate-benchmark review."""
import argparse
from datetime import datetime, timedelta, timezone
import hashlib
import json
import math
from pathlib import Path
import re
from zoneinfo import ZoneInfo

from report_store import resolve_file
from shared_research_pack import ROOT, digest, exact_date, number, teams, timestamp
from universe import SUPPORTED

MAX_BYTES = 8 * 1024 * 1024


def allowed_symbols():
    return set(SUPPORTED) | {b['ticker'] for t in teams(ROOT / 'config/research_teams.json') for b in t['benchmark_candidates']}


def source_url(symbol):
    return 'https://finance.yahoo.com/quote/' + symbol + '/history'


def window(start, end):
    a, b = exact_date(start), exact_date(end)
    if not 0 < (b-a).days <= 366:
        raise ValueError('Expected a positive price window of at most 366 days')
    return a, b


def fetch_history(symbol, start, end):
    # Import only in the explicit collection path. Offline review has no provider dependency.
    import yfinance as yf
    ticker = yf.Ticker(symbol)
    frame = ticker.history(start=start, end=(exact_date(end)+timedelta(days=1)).isoformat(),
                           interval='1d', auto_adjust=True, actions=False, repair=False, keepna=True,
                           timeout=15, raise_errors=True)
    metadata = ticker.history_metadata
    zone = ZoneInfo(metadata['exchangeTimezoneName'])
    rows = []
    for stamp, close in frame['Close'].items():
        if stamp.tzinfo is None:
            raise ValueError('Provider bars must have an exchange timezone')
        stamp = stamp.tz_convert(zone)
        close = float(close)
        rows.append({'observed_on': stamp.date().isoformat(), 'value': None if math.isnan(close) else close})
    return {'symbol': metadata.get('symbol'), 'currency': metadata.get('currency'),
            'exchange_timezone': metadata.get('exchangeTimezoneName'), 'exchange_name': metadata.get('exchangeName'),
            'instrument_type': metadata.get('instrumentType'), 'provider_version': yf.__version__, 'observations': rows}


def validate_series(row, start, end):
    keys = {'symbol', 'currency', 'exchange_timezone', 'exchange_name', 'instrument_type', 'provider_version',
            'observations', 'retrieved_at', 'source_url', 'adjustment_basis', 'status', 'reason'}
    if (not isinstance(row, dict) or set(row) != keys or not isinstance(row['symbol'], str) or row['symbol'] not in allowed_symbols()
            or not timestamp(row['retrieved_at']) or timestamp(row['retrieved_at']) != row['retrieved_at']
            or row['source_url'] != source_url(row['symbol']) or row['adjustment_basis'] != 'adjusted_close'
            or row['status'] not in ('observed', 'missing', 'unavailable') or not isinstance(row['observations'], list)):
        raise ValueError('Invalid price series contract')
    if row['status'] == 'unavailable':
        if (row['reason'] not in ('PROVIDER_UNAVAILABLE', 'DATA_VALIDATION_ERROR') or row['observations']
                or any(row[k] is not None for k in ('currency', 'exchange_timezone', 'exchange_name', 'instrument_type', 'provider_version'))):
            raise ValueError('Invalid unavailable series')
        return row
    expected_type = 'EQUITY' if row['symbol'] in SUPPORTED else 'ETF'
    if (not isinstance(row['currency'], str) or not re.fullmatch('[A-Z]{3}', row['currency'])
            or row['instrument_type'] != expected_type or not isinstance(row['exchange_name'], str)
            or not re.fullmatch(r'[A-Za-z0-9 ._/-]{1,80}', row['exchange_name'])
            or not isinstance(row['provider_version'], str) or not re.fullmatch(r'[0-9A-Za-z.+_-]{1,40}', row['provider_version'])):
        raise ValueError('Invalid price provider metadata')
    try:
        zone = ZoneInfo(row['exchange_timezone'])
    except (ValueError, TypeError, KeyError):
        raise ValueError('Invalid exchange timezone') from None
    # A requested end day must precede retrieval's exchange-local date. This
    # conservative gate does not certify an exchange calendar or after-hours close.
    if exact_date(end) >= datetime.fromisoformat(row['retrieved_at']).astimezone(zone).date():
        raise ValueError('Price window must precede the exchange-local retrieval day')
    seen = set(); available = 0
    for cell in row['observations']:
        if not isinstance(cell, dict) or set(cell) != {'observed_on', 'value'}:
            raise ValueError('Invalid price cell')
        day = exact_date(cell['observed_on']); price = cell['value']
        if not exact_date(start) <= day <= exact_date(end) or day in seen:
            raise ValueError('Duplicate or out-of-window price date')
        seen.add(day)
        if price is not None:
            if number(price) is None or price <= 0:
                raise ValueError('Invalid adjusted close')
            available += 1
    if (row['observations'] != sorted(row['observations'], key=lambda r:r['observed_on'])
            or row['status'] != ('observed' if available else 'missing')
            or row['reason'] != (None if available else 'NO_USABLE_OBSERVATIONS')):
        raise ValueError('Price availability does not match retained observations')
    return row


def capture(symbols, *, start, end, fetcher=None, clock=None):
    window(start, end)
    if (not isinstance(symbols, (list, tuple)) or not symbols or
            any(not isinstance(s, str) or s not in allowed_symbols() for s in symbols)):
        raise ValueError('Expected supported stocks or configured benchmark candidates')
    symbols = sorted(set(symbols)); provider_clock = clock or (lambda: datetime.now(timezone.utc))
    def now():
        value = provider_clock()
        if not isinstance(value, datetime) or value.utcoffset() is None:
            raise ValueError('Expected a zoned capture clock')
        return value.astimezone(timezone.utc)
    began = now()
    if exact_date(end) >= began.date():
        raise ValueError('Capture requires a completed past date window and zoned clock')
    result = []
    for symbol in symbols:
        failure = 'PROVIDER_UNAVAILABLE'
        try:
            raw = (fetcher or fetch_history)(symbol, start, end)
            retrieved = now().isoformat()
            failure = 'DATA_VALIDATION_ERROR'
            if not isinstance(raw, dict) or raw.get('symbol') != symbol:
                raise ValueError('Provider symbol mismatch')
            row = {k: raw.get(k) for k in ('symbol', 'currency', 'exchange_timezone', 'exchange_name',
                                          'instrument_type', 'provider_version', 'observations')}
            rows = row['observations']
            if not isinstance(rows, list): raise ValueError('Invalid observation list')
            row['observations'] = sorted(rows, key=lambda r:r['observed_on'])
            available = any(r['value'] is not None for r in rows)
            row.update(retrieved_at=retrieved, source_url=source_url(symbol), adjustment_basis='adjusted_close',
                       status='observed' if available else 'missing', reason=None if available else 'NO_USABLE_OBSERVATIONS')
            validate_series(row, start, end)
        except Exception:
            # Never persist provider exception text, URLs, cookies or arbitrary fields.
            row = {k: None for k in ('currency', 'exchange_timezone', 'exchange_name', 'instrument_type', 'provider_version')}
            row.update(symbol=symbol, retrieved_at=now().isoformat(),
                       source_url=source_url(symbol), adjustment_basis='adjusted_close', observations=[],
                       status='unavailable', reason=failure)
        result.append(row)
    payload = {'schema_version': 1, 'kind': 'benchmark_price_capture', 'provider': 'yfinance',
               'capture_mode': 'injected_fetcher' if fetcher is not None else 'provider',
               'start': start, 'end': end, 'started_at': began.astimezone(timezone.utc).isoformat(),
               'finished_at': now().isoformat(), 'series': result,
               'listing_identity': 'provider_symbol_metadata_only', 'point_in_time_eligible': False}
    return validate_capture({'capture_id': digest(payload), **payload})


def validate_capture(value):
    if (not isinstance(value, dict) or set(value) != {'capture_id', 'schema_version', 'kind', 'provider', 'start',
            'end', 'started_at', 'finished_at', 'series', 'listing_identity', 'point_in_time_eligible', 'capture_mode'}
            or type(value['schema_version']) is not int or value['schema_version'] != 1
            or value['kind'] != 'benchmark_price_capture' or value['provider'] != 'yfinance'
            or value['capture_mode'] not in ('provider', 'injected_fetcher')
            or value['capture_id'] != digest({k:v for k,v in value.items() if k != 'capture_id'})
            or value['listing_identity'] != 'provider_symbol_metadata_only' or value['point_in_time_eligible'] is not False):
        raise ValueError('Invalid price capture identity')
    window(value['start'], value['end'])
    for key in ('started_at', 'finished_at'):
        if not timestamp(value[key]) or timestamp(value[key]) != value[key]:
            raise ValueError('Invalid capture timestamp')
    began, finished = (datetime.fromisoformat(value[k]) for k in ('started_at', 'finished_at'))
    if not 0 <= (finished-began).total_seconds() <= 3600 or exact_date(value['end']) >= began.date():
        raise ValueError('Invalid capture duration or date window')
    if not isinstance(value['series'], list) or not 1 <= len(value['series']) <= len(allowed_symbols()):
        raise ValueError('Invalid capture series count')
    symbols = []
    for row in value['series']:
        validate_series(row, value['start'], value['end']); symbols.append(row['symbol'])
        if not began <= datetime.fromisoformat(row['retrieved_at']) <= finished:
            raise ValueError('Series retrieval is outside capture batch')
    if symbols != sorted(set(symbols)):
        raise ValueError('Duplicate or unsorted capture symbols')
    return value


def write_bundle(value, output):
    validate_capture(value); output = Path(output)
    if output.resolve().is_relative_to(ROOT):
        raise ValueError('Capture output must be outside the repository')
    raw = (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+'\n').encode()
    if len(raw) > MAX_BYTES: raise ValueError('Capture exceeds size limit')
    manifest = {'schema_version': 1, 'kind': value['kind'], 'capture_id': value['capture_id'],
                'json': 'prices.json', 'sha256': hashlib.sha256(raw).hexdigest()}
    output.mkdir(parents=False, exist_ok=False)
    for name, data in (('prices.json', raw), ('manifest.json', (json.dumps(manifest, indent=2)+'\n').encode())):
        with (output/name).open('xb') as stream: stream.write(data)
    return manifest


def load_bundle(root):
    def read(name, limit):
        with resolve_file(root, name).open('rb') as stream: raw = stream.read(limit+1)
        if len(raw) > limit: raise ValueError('Capture input exceeds size limit')
        return raw
    manifest = json.loads(read('manifest.json', 65536))
    if (not isinstance(manifest, dict) or set(manifest) != {'schema_version', 'kind', 'capture_id', 'json', 'sha256'}
            or type(manifest['schema_version']) is not int or manifest['schema_version'] != 1
            or manifest['kind'] != 'benchmark_price_capture' or manifest['json'] != 'prices.json'):
        raise ValueError('Invalid capture manifest')
    raw = read(manifest['json'], MAX_BYTES)
    if hashlib.sha256(raw).hexdigest() != manifest['sha256']: raise ValueError('Capture checksum mismatch')
    value = validate_capture(json.loads(raw))
    if value['capture_id'] != manifest['capture_id']: raise ValueError('Capture and manifest identity mismatch')
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--symbols', nargs='+', required=True)
    parser.add_argument('--start', required=True); parser.add_argument('--end', required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        # Refuse an existing/unsafe destination before making provider calls.
        if (args.output.exists() or args.output.is_symlink() or args.output.resolve().is_relative_to(ROOT)
                or not args.output.parent.is_dir()):
            raise ValueError('A new output directory outside the repository is required')
        value = capture(args.symbols, start=args.start, end=args.end)
        write_bundle(value, args.output)
    except (OSError, ValueError, TypeError, KeyError, AttributeError):
        parser.error('Capture failed; check the bounded window, supported symbols and a new output directory')
    print('Price capture saved: ' + str(len(value['series'])) + ' series; observed=' + str(sum(r['status']=='observed' for r in value['series'])))


if __name__ == '__main__': main()
