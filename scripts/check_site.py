"""Verify a deployed daily publication over HTTP, including archived file hashes."""
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import PurePosixPath
import re
import time
from urllib.parse import quote, urlsplit
from urllib.request import urlopen
from zoneinfo import ZoneInfo


class SiteError(RuntimeError):
    pass


def _fetch(base, relative):
    path = PurePosixPath(relative)
    if (path.is_absolute() or '..' in path.parts or '\\' in relative or
            any(ord(c) < 32 for c in relative) or urlsplit(relative).scheme):
        raise SiteError('Invalid public archive path')
    with urlopen(base.rstrip('/') + '/' + quote(relative, safe='/.-_'), timeout=30) as response:
        data = response.read(20 * 1024 * 1024 + 1)
    if len(data) > 20 * 1024 * 1024:
        raise SiteError('Public response exceeds the verification size limit')
    return data


def check(base, *, business_date, require_ready=False):
    parts = urlsplit(base)
    if (parts.scheme not in ('http', 'https') or not parts.netloc or parts.username or
            parts.password or parts.query or parts.fragment):
        raise SiteError('Expected an HTTP website base URL without credentials or query parameters')
    index = json.loads(_fetch(base, 'index.json'))
    health = json.loads(_fetch(base, 'health.json'))
    attempt = index.get('last_attempt', {})
    if attempt.get('business_date') != business_date or health.get('business_date') != business_date:
        raise SiteError('The deployed site does not contain the expected business date')
    if attempt.get('status') not in ('complete', 'degraded') or health.get('status') != attempt['status']:
        raise SiteError('The deployed daily run is incomplete or failed')
    publication = index.get('publication', {})
    if not publication.get('version') or health.get('version') != publication['version']:
        raise SiteError('Public version metadata is missing or inconsistent')
    if health.get('published_at') != publication.get('published_at'):
        raise SiteError('Public files belong to different publications')
    if {'members', 'credentials', 'deliveries', 'secrets'} & index.keys():
        raise SiteError('Private configuration was included in the public index')
    expected = set(attempt.get('expected_tickers', []))
    if not expected or set(attempt.get('successful_tickers', [])) != expected:
        raise SiteError('Daily publication is missing expected holdings')
    if health.get('expected') != len(expected) or health.get('updated') != len(expected):
        raise SiteError('Public coverage counts disagree')
    reports = index.get('reports', [])
    selected = {}
    for entry in reports:
        if entry.get('as_of') == business_date and entry.get('quality') != 'historical':
            ticker = entry['ticker']
            if ticker not in selected or entry['generated_at'] > selected[ticker]['generated_at']:
                selected[ticker] = entry
    if not expected <= selected.keys():
        raise SiteError('Current report versions are missing from the deployed index')
    if require_ready and (attempt['status'] != 'complete' or
                          any(selected[t]['quality'] != 'ready' for t in expected)):
        raise SiteError('Deployed reports have incomplete source evidence')
    verified = 0

    def verify(entry, kind):
        relative = entry[kind]
        if not relative.startswith('archive/'):
            raise SiteError('Public report is outside the archive')
        wanted = entry['sha256'][kind]
        if not isinstance(wanted, str) or not re.fullmatch('[0-9a-f]{64}', wanted):
            raise SiteError('Public report has invalid integrity metadata')
        data = _fetch(base, relative)
        if hashlib.sha256(data).hexdigest() != wanted:
            raise SiteError('A deployed report failed its integrity check')
        if kind == 'pdf' and not data.startswith(b'%PDF-'):
            raise SiteError('The deployed PDF is not a PDF response')

    for ticker in sorted(expected):
        for kind in ('md', 'json', 'pdf'):
            verify(selected[ticker], kind)
            verified += 1
    old = next((entry for entry in reports if entry['as_of'] < business_date), None)
    if old:
        verify(old, 'pdf')
        verified += 1
    return {'status': 'verified', 'business_date': business_date, 'holdings': len(expected),
            'files_verified': verified, 'historical_pdf_verified': old is not None,
            'version': publication['version']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--url', required=True)
    parser.add_argument('--business-date', default=datetime.now(ZoneInfo('America/Toronto')).date().isoformat())
    parser.add_argument('--require-ready', action='store_true')
    args = parser.parse_args()
    for attempt in range(3):
        try:
            result = check(args.url, business_date=args.business_date, require_ready=args.require_ready)
            print(json.dumps(result))
            return
        except (OSError, ValueError, KeyError, TypeError, SiteError):
            if attempt == 2:
                raise SystemExit('Deployed site verification failed: inspect publication date, coverage and archive integrity') from None
            time.sleep(10)


if __name__ == '__main__':
    main()
