"""Price providers with bounded retries and safe, structured diagnostics."""
import io
import os
from pathlib import Path
import time
import urllib.error
import urllib.request

import pandas as pd
import yfinance as yf

from data_utils import number


class PriceFetchError(Exception):
    """A price dependency failure safe to include in reports."""

    def __init__(self, source, category, retryable, attempts, detail):
        self.source = source
        self.category = category
        self.retryable = retryable
        self.attempts = attempts
        self.detail = detail
        super().__init__(f'{source}: {detail} after {attempts} attempts ({category})')


def classify_price_error(exc, source):
    """Classify without copying exception text, URLs, or tracebacks to reports."""
    if isinstance(exc, urllib.error.HTTPError):
        return ('http_error', exc.code == 429 or 500 <= exc.code <= 599,
                f'The price service returned HTTP {exc.code}')
    reason = getattr(exc, 'reason', exc)
    if isinstance(reason, TimeoutError) or (
        isinstance(exc, urllib.error.URLError) and isinstance(reason, str)
        and ('timed out' in reason.lower() or 'timeout' in reason.lower())
    ):
        return 'timeout', True, 'The price request timed out'
    if isinstance(exc, (urllib.error.URLError, ConnectionError, OSError)):
        return 'dns_or_connection', True, 'DNS resolution or connection to the price service failed'
    if isinstance(exc, ValueError):
        if str(exc) in ('empty history', 'empty stooq'):
            return 'empty_response', False, 'The price service returned no history'
        if str(exc) == 'no valid prices':
            return 'no_valid_prices', False, 'No valid positive prices were available through the requested date'
        if source == 'stooq' and str(exc) == 'unsupported listing':
            return 'unsupported_listing', False, 'The US Stooq fallback is unavailable for international listings'
    if type(exc).__name__ == 'YFRateLimitError':
        return 'http_error', True, 'The price service returned HTTP 429'
    return 'dns_or_connection', False, 'The price request could not be completed due to an unexpected error'


def fetch_with_retry(fetch_fn, source, max_attempts=3, backoff=(0.5, 1, 2), sleep=time.sleep):
    """Return (value, attempts), retrying only transient failures."""
    if not isinstance(max_attempts, int) or isinstance(max_attempts, bool) or max_attempts < 1:
        raise ValueError('max_attempts must be a positive integer')
    for attempt in range(1, max_attempts + 1):
        try:
            return fetch_fn(), attempt
        except Exception as exc:
            category, retryable, detail = classify_price_error(exc, source)
            if not retryable or attempt == max_attempts:
                raise PriceFetchError(source, category, retryable, attempt, detail) from None
            sleep(backoff[min(attempt - 1, len(backoff) - 1)])


def clean_prices_series(h, symbol, as_of):
    """Keep valid positive closes through as_of, preserving skipped-row warnings."""
    c = h['Close'].loc[:as_of].map(number)
    valid = c.notna() & (c > 0)
    warnings = []
    if not valid.all():
        warnings.append(f'warning: {symbol} invalid/missing prices skipped')
    c = c.loc[valid].astype(float)
    if c.empty:
        exc = ValueError('no valid prices')
        exc.warnings = warnings
        raise exc
    return c, warnings


def stooq_url(symbol, price_start, as_of):
    return (f'https://stooq.com/q/d/l/?s={symbol.lower()}.us&i=d'
            f'&d1={price_start.replace("-", "")}&d2={as_of.replace("-", "")}')


def fetch_symbol_prices(symbol, price_start, as_of, end, data_dir, timeout=30,
                        max_attempts=3, sleep=time.sleep):
    """Try Yahoo then Stooq; return prices and one diagnostic per provider."""
    statuses = []
    data_dir = Path(data_dir)
    for source in ('yfinance', 'stooq'):
        warnings = []

        def fetch():
            if source == 'yfinance':
                cache = None
                if os.environ.get('JSOSIF_PRICE_CACHE'):
                    cache = Path(os.environ['JSOSIF_PRICE_CACHE']) / f'{symbol}-{price_start}-{end}.csv'
                # Cache only within one refresh batch. A later run must fetch a new
                # daily bar, which may have changed since an earlier intraday run.
                batch_start = os.environ.get('JSOSIF_PRICE_CACHE_BATCH_START')
                if cache and cache.is_file() and batch_start and cache.stat().st_mtime >= float(batch_start):
                    h = pd.read_csv(cache, index_col=0, parse_dates=True)
                else:
                    h = yf.Ticker(symbol).history(start=price_start, end=end,
                                                  auto_adjust=True, timeout=timeout)
                    if cache and not h.empty:
                        cache.parent.mkdir(parents=True, exist_ok=True)
                        h.to_csv(cache)
                if h.empty:
                    raise ValueError('empty history')
                h.index = pd.to_datetime(h.index).tz_localize(None).normalize()
            else:
                if '.' in symbol:
                    raise ValueError('unsupported listing')
                with urllib.request.urlopen(stooq_url(symbol, price_start, as_of), timeout=timeout) as response:
                    raw = response.read().decode()
                if not raw.strip() or raw.strip().lower() == 'no data':
                    raise ValueError('empty stooq')
                h = pd.read_csv(io.StringIO(raw), parse_dates=['Date']).set_index('Date').sort_index()
                if h.empty:
                    raise ValueError('empty stooq')
            try:
                prices, skipped = clean_prices_series(h, symbol, as_of)
                warnings.extend(skipped)
            except ValueError as exc:
                warnings.extend(getattr(exc, 'warnings', []))
                raise
            if source == 'yfinance':
                h.to_csv(data_dir / f'{symbol}-yfinance.csv')
            else:
                (data_dir / f'{symbol}-stooq.csv').write_text(raw)
            return prices

        try:
            prices, attempts = fetch_with_retry(fetch, source, max_attempts=max_attempts, sleep=sleep)
            status = dict(stage='price_fetch', symbol=symbol, source=source, status='ok',
                          category=None, retryable=False, attempts=attempts,
                          detail='Price history fetched successfully')
        except PriceFetchError as exc:
            status = dict(stage='price_fetch', symbol=symbol, source=source, status='failed',
                          category=exc.category, retryable=exc.retryable,
                          attempts=exc.attempts, detail=exc.detail)
        if warnings:
            status['detail'] += '; ' + '; '.join(dict.fromkeys(warnings))
        statuses.append(status)
        if status['status'] == 'ok':
            return prices, statuses
    return None, statuses

