"""Deliver one personalized PDF digest per member per local calendar week."""
import argparse
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime, make_msgid
import fcntl
import hashlib
import os
from pathlib import Path
from zoneinfo import ZoneInfo

from email_delivery import build_email, send, GmailSmtpBackend
from report_store import read_json, write_json, resolve_file, digest, persist
from subscriptions import load, tickers_for


def due_period(member, now):
    if now.tzinfo is None:
        raise ValueError('now must be timezone-aware')
    local = now.astimezone(ZoneInfo(member['timezone']))
    monday = local.date() - timedelta(days=local.weekday())
    hour, minute = map(int, member['send_time'].split(':'))
    due = datetime.combine(monday + timedelta(days=member['send_weekday']),
                           datetime.min.time(), tzinfo=local.tzinfo).replace(hour=hour, minute=minute)
    return monday.isoformat() if local >= due else None


def deliver(config, root, *, now=None, really_send=False, git=False, backend=send):
    now = now or datetime.now(timezone.utc)
    root = Path(root)
    root.mkdir(parents=True, exist_ok=True)
    # All writers use this same store and the workflow also serializes across runners.
    with (root / '.delivery.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        index = read_json(root / 'index.json', {'reports': []})
        ledger = read_json(root / 'state/deliveries.json', {})
        summary = {'sent': 0, 'prepared': 0, 'skipped': 0, 'deferred': 0, 'unknown': 0}
        for member in config['members']:
            period = due_period(member, now) if member['enabled'] else None
            if not period:
                summary['skipped'] += 1
                continue
            # Public archive state never includes names, addresses, or message bodies.
            key = hashlib.sha256((member['id'] + ':' + period).encode()).hexdigest()
            if key in ledger:
                summary['skipped'] += 1
                continue
            selected = []
            for ticker in tickers_for(config, member):
                candidates = [r for r in index['reports'] if r['ticker'] == ticker and
                              (r['quality'] == 'ready' or config.get('allow_degraded', False)) and
                              timedelta(0) <= now - datetime.fromisoformat(r['generated_at']) <=
                              timedelta(days=config.get('max_report_age_days', 4))]
                if not candidates:
                    selected = []
                    break
                selected.append(max(candidates, key=lambda r: r['generated_at']))
            if not selected:
                summary['deferred'] += 1
                continue
            paths, pdfs = [], []
            try:
                for entry in selected:
                    md = resolve_file(root, entry['md'])
                    pdf = resolve_file(root, entry['pdf'])
                    snapshot = resolve_file(root, entry['json'])
                    if any(digest(path) != entry['sha256'][kind]
                           for kind, path in [('md', md), ('pdf', pdf), ('json', snapshot)]):
                        raise ValueError('Archived report integrity check failed')
                    paths.append(md); pdfs.append(pdf)
                message = build_email(paths, [member['email']], pdf_path=pdfs,
                                      brief=True, display_name=member['name'])
                message['Date'] = format_datetime(now)
                message['Message-ID'] = make_msgid()
                if len(message.as_bytes()) > 20 * 1024 * 1024:
                    raise ValueError('Digest exceeds the 20 MiB encoded message budget')
            except (ValueError, OSError):
                summary['deferred'] += 1
                continue
            if not really_send:
                summary['prepared'] += 1
                continue
            ledger[key] = {'period': period, 'status': 'sending', 'updated_at': now.isoformat(),
                           'reports': [r['report_id'] for r in selected]}
            write_json(root / 'state/deliveries.json', ledger)
            persist(root, git)  # Failure here prevents the SMTP call.
            try:
                backend(message)
            except Exception:
                # SMTP may have accepted the message before the connection failed.
                # Keep it for manual reconciliation rather than duplicate delivery.
                ledger[key]['status'] = 'unknown'
                summary['unknown'] += 1
            else:
                ledger[key]['status'] = 'accepted'
                summary['sent'] += 1
            write_json(root / 'state/deliveries.json', ledger)
            persist(root, git)
        return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--store', type=Path, required=True)
    parser.add_argument('--send', action='store_true')
    parser.add_argument('--persist-git', action='store_true')
    args = parser.parse_args()
    if args.send and os.environ.get('JSOSIF_APPROVED_SEND') != '1':
        parser.error('Set JSOSIF_APPROVED_SEND=1 to enable delivery')
    if args.send:
        GmailSmtpBackend().credentials()  # Fail configuration checks before reserving a weekly slot.
    result = deliver(load(args.config), args.store, really_send=args.send, git=args.persist_git)
    print(result)
    if result['unknown']:
        raise SystemExit('Delivery needs reconciliation; uncertain messages will not be retried automatically')


if __name__ == '__main__':
    main()
