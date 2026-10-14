"""Append-only email send audit trail; override storage with SEND_LEDGER_PATH."""
import argparse
from datetime import datetime, time, timezone
import json
import logging
import os
from pathlib import Path


DEFAULT_PATH = Path(__file__).resolve().parents[1] / 'data' / 'send_ledger.jsonl'
logger = logging.getLogger(__name__)


def _path():
    return Path(os.environ.get('SEND_LEDGER_PATH', DEFAULT_PATH))


def _timestamp(value):
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        raise ValueError('timestamp must include a timezone')
    return parsed.astimezone(timezone.utc)


def _validate(entry):
    if not isinstance(entry, dict):
        raise ValueError('entry must be an object')
    if not isinstance(entry['snapshot_id'], str) or not entry['snapshot_id']:
        raise ValueError('snapshot_id must be a nonempty string')
    if not isinstance(entry['recipients'], list) or not all(
            isinstance(value, str) for value in entry['recipients']):
        raise ValueError('recipients must be a list of strings')
    if type(entry['dry_run']) is not bool:
        raise ValueError('dry_run must be a bool')
    if entry['status'] not in ('sent', 'dry-run', 'failed'):
        raise ValueError('invalid status')
    if entry.get('error') is not None and not isinstance(entry['error'], str):
        raise ValueError('error must be a string or null')
    return _timestamp(entry['timestamp'])


def record(entry: dict) -> None:
    """Append an attempt; omitted timestamp defaults to now and error to null."""
    row = dict(entry)
    row.setdefault('timestamp', datetime.now(timezone.utc).isoformat())
    row.setdefault('error', None)
    timestamp = _validate(row)
    if row['status'] != 'failed':
        row['error'] = None
    if datetime.fromisoformat(row['timestamp']).utcoffset().total_seconds() != 0:
        row['timestamp'] = timestamp.isoformat()
    line = json.dumps(row, ensure_ascii=False, allow_nan=False) + '\n'
    path = _path()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a', encoding='utf-8') as stream:
        stream.write(line)


def _bound(value, end=False):
    if value is None:
        return None
    if len(value) == 10:
        day = datetime.strptime(value, '%Y-%m-%d').date()
        return datetime.combine(day, time.max if end else time.min, timezone.utc)
    return _timestamp(value)


def query(since=None, until=None, ticker=None, dry_run=None) -> list[dict]:
    """Filter inclusively by UTC dates/timestamps and ticker prefix (TICKER-)."""
    lower, upper = _bound(since), _bound(until, end=True)
    rows = []
    try:
        stream = _path().open(encoding='utf-8')
    except FileNotFoundError:
        return rows
    with stream:
        for number, line in enumerate(stream, 1):
            try:
                row = json.loads(line)
                timestamp = _validate(row)
            except (ValueError, KeyError, TypeError):
                logger.warning('Skipping malformed ledger line %d', number)
                continue
            if lower is not None and timestamp < lower:
                continue
            if upper is not None and timestamp > upper:
                continue
            if ticker is not None and not row['snapshot_id'].startswith(ticker + '-'):
                continue
            if dry_run is not None and row['dry_run'] != dry_run:
                continue
            rows.append(row)
    return rows


def main(argv=None):
    """Print matching attempts as a compact table."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--list', action='store_true', required=True)
    parser.add_argument('--since')
    parser.add_argument('--until')
    parser.add_argument('--ticker')
    parser.add_argument('--dry-run', action='store_const', const=True, default=None)
    args = parser.parse_args(argv)
    try:
        rows = query(args.since, args.until, args.ticker, args.dry_run)
    except ValueError as exc:
        parser.error(str(exc))
    table = [['SNAPSHOT', 'TIMESTAMP (UTC)', 'RECIPIENTS', 'DRY RUN', 'STATUS', 'ERROR']]
    for row in rows:
        table.append([row['snapshot_id'], row['timestamp'], ','.join(row['recipients']),
                      str(row['dry_run']).lower(), row['status'], row.get('error') or '-'])
    table = [[' '.join(cell.split()) for cell in row] for row in table]
    widths = [max(len(row[i]) for row in table) for i in range(len(table[0]))]
    for row in table:
        print('  '.join(cell.ljust(width) for cell, width in zip(row, widths)).rstrip())


if __name__ == '__main__':
    main()
