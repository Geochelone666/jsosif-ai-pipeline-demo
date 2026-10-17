#!/usr/bin/env python3
"""Prepare one holding email per teammate; dry-run is the default."""
import argparse
from datetime import datetime
import json
import os
from pathlib import Path

from email_delivery import ROOT, DryRunBackend, build_email, send, validate_recipients
from universe import SUPPORTED


def prepare(config, reports, stamp=None):
    payload = json.loads(Path(config).read_text(encoding='utf-8'))
    assignments = payload.get('assignments') if isinstance(payload, dict) else None
    if not isinstance(assignments, dict) or not assignments:
        raise ValueError('Expected a nonempty assignments object: email -> ticker')
    validate_recipients(list(assignments))
    tickers = list(assignments.values())
    if any(not isinstance(ticker, str) or ticker not in SUPPORTED for ticker in tickers):
        raise ValueError('Every assignment must name a supported holding')
    reports = Path(reports)
    available = {}
    for ticker in tickers:
        dates = set()
        for path in reports.glob(f'{ticker}-intelligence-????????.md'):
            candidate = path.stem.rsplit('-', 1)[-1]
            try:
                datetime.strptime(candidate, '%Y%m%d')
            except ValueError:
                continue
            dates.add(candidate)
        available[ticker] = dates
    if stamp is not None:
        datetime.strptime(stamp, '%Y%m%d')
    else:
        common = set.intersection(*available.values())
        if not common:
            raise ValueError('No common report date for all assigned holdings')
        stamp = max(common)
    # Validate the entire batch before any delivery or output.
    messages = []
    for address, ticker in assignments.items():
        if stamp not in available[ticker]:
            raise ValueError(f'Missing report for {ticker} on {stamp}')
        path = reports / f'{ticker}-intelligence-{stamp}.md'
        messages.append((ticker, build_email([path], [address])))
    return stamp, messages


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, default=ROOT / 'config/team_recipients.json')
    parser.add_argument('--reports-dir', type=Path, default=ROOT / 'reports')
    parser.add_argument('--date', help='Report date YYYYMMDD; default: latest common snapshot date')
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'review/team')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--dry-run', action='store_true', help='Write .eml previews (default)')
    mode.add_argument('--send', action='store_true', help='Send via the existing Gmail backend')
    args = parser.parse_args(argv)
    if args.send and os.environ.get('JSOSIF_APPROVED_SEND') != '1':
        parser.error('发送需 Lucas 明确批准；设置 JSOSIF_APPROVED_SEND=1 后重试')
    try:
        stamp, messages = prepare(args.config, args.reports_dir, args.date)
    except (OSError, ValueError):
        parser.error('Invalid assignments or incomplete/invalid reports; check configuration and report date')
    if not args.send:
        args.output_dir.mkdir(parents=True, exist_ok=True)
    for ticker, message in messages:
        if args.send:
            send(message)
        else:
            DryRunBackend(args.output_dir / f'{ticker}-{stamp}.eml').deliver(message)
        print(f'{"Sent" if args.send else "Prepared"}: {ticker} | {stamp} | {message["To"]}')
    print(f'{len(messages)} emails {"sent" if args.send else "prepared; no email sent"}.')


if __name__ == '__main__':
    main()

