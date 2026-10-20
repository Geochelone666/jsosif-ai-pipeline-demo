"""Check archive integrity and daily coverage before declaring a v1 release ready."""
import argparse
from datetime import date, datetime
import json
from pathlib import Path
from zoneinfo import ZoneInfo

from report_store import read_json, verified_report_files, report_advisory


def check(store, *, business_date=None, require_ready=False):
    root = Path(store)
    index = read_json(root / 'index.json', {})
    reports = index.get('reports', [])
    attempt = index.get('last_attempt', {})
    errors = []
    if not isinstance(reports, list) or not reports:
        return {'ready': False, 'checked': 0, 'errors': ['No archived reports exist']}
    for entry in reports:
        try:
            verified_report_files(root, entry)
        except (ValueError, OSError, KeyError, TypeError):
            errors.append('An archived report failed its integrity or contract check')
    selected_date = business_date or attempt.get('business_date')
    if not selected_date:
        errors.append('No daily collection has been recorded')
    else:
        date.fromisoformat(selected_date)
    expected = set(attempt.get('expected_tickers', []))
    if selected_date != attempt.get('business_date'):
        errors.append('The recorded run does not match the expected business date')
    if not expected:
        errors.append('No expected holdings were recorded for the daily run')
    latest = {}
    for entry in reports:
        if entry.get('as_of') == selected_date and entry.get('quality') != 'historical':
            ticker = entry['ticker']
            if ticker not in latest or entry['generated_at'] > latest[ticker]['generated_at']:
                latest[ticker] = entry
    missing = sorted(expected - latest.keys())
    degraded = sorted(t for t in expected & latest.keys()
                      if latest[t]['quality'] != 'ready' or latest[t].get('advisory') or report_advisory(root, latest[t]))
    if missing:
        errors.append('Missing current-day reports: ' + ', '.join(missing))
    if require_ready and degraded:
        errors.append('Reports require complete source evidence: ' + ', '.join(degraded))
    if attempt.get('status') in ('running', 'partial', 'failed'):
        errors.append('The last daily run failed, is incomplete, or was interrupted')
    if require_ready and attempt.get('status') != 'complete':
        errors.append('Strict acceptance requires a completed daily run with full source evidence')
    return {'ready': not errors, 'business_date': selected_date, 'checked': len(reports),
            'expected': len(expected), 'current': len(expected & latest.keys()),
            'degraded_tickers': degraded, 'errors': errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--store', type=Path, required=True)
    parser.add_argument('--business-date', default=datetime.now(ZoneInfo('America/Toronto')).date().isoformat(),
                        help='Expected Toronto report date; defaults to today')
    parser.add_argument('--require-ready', action='store_true')
    args = parser.parse_args()
    result = check(args.store, business_date=args.business_date, require_ready=args.require_ready)
    print(json.dumps(result, indent=2))
    if not result['ready']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
