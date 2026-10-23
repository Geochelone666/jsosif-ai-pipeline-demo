"""Deliver one personalized PDF digest per member per local calendar week."""
import argparse
from datetime import date, datetime, timedelta, timezone
from email.utils import format_datetime, make_msgid
import fcntl
import hashlib
import json
import os
from pathlib import Path
from zoneinfo import ZoneInfo
from tempfile import NamedTemporaryFile

from email_delivery import build_email, send, GmailSmtpBackend
from report_store import read_json, write_json, verified_report_files, persist, report_advisory
from subscriptions import load, tickers_for


def eligible_report(entry, ticker, config, now):
    """Malformed metadata cannot prevent other reports or members being processed."""
    try:
        if not isinstance(entry, dict) or entry['ticker'] != ticker:
            return False
        if any(not isinstance(entry.get(field), str) or not entry[field]
               for field in ('report_id', 'md', 'json', 'pdf')):
            return False
        hashes = entry.get('sha256')
        if not isinstance(hashes, dict) or any(
                not isinstance(hashes.get(kind), str) or len(hashes[kind]) != 64
                for kind in ('md', 'json', 'pdf')):
            return False
        if entry['quality'] != 'ready' and not (
                entry['quality'] == 'degraded' and config.get('allow_degraded', False)):
            return False
        as_of = date.fromisoformat(entry['as_of'])
        generated = datetime.fromisoformat(entry['generated_at'])
        if generated.tzinfo is None or generated.utcoffset() is None:
            return False
        age = config.get('max_report_age_days', 4)
        # Report dates belong to Toronto, independently of the recipient's zone.
        report_today = now.astimezone(ZoneInfo('America/Toronto')).date()
        return (timedelta(0) <= report_today - as_of <= timedelta(days=age) and
                timedelta(0) <= now - generated <= timedelta(days=max(1, age)))
    except (KeyError, TypeError, ValueError, OverflowError):
        return False


def due_period(member, now):
    if now.tzinfo is None:
        raise ValueError('now must be timezone-aware')
    local = now.astimezone(ZoneInfo(member['timezone']))
    monday = local.date() - timedelta(days=local.weekday())
    hour, minute = map(int, member['send_time'].split(':'))
    due = datetime.combine(monday + timedelta(days=member['send_weekday']),
                           datetime.min.time(), tzinfo=local.tzinfo).replace(hour=hour, minute=minute)
    if member.get('delivery_start_date') and due.date() < date.fromisoformat(member['delivery_start_date']):
        return None
    # Compare instants: the repeated fall-back hour must not move an already due
    # send back into the future. ZoneInfo's default fold=0 chooses its first occurrence.
    return monday.isoformat() if now.astimezone(timezone.utc) >= due.astimezone(timezone.utc) else None


def deliver(config, root, *, now=None, really_send=False, git=False, backend=send,
            preview_dir=None, preview_all=False, ledger_store=None):
    if really_send and (preview_dir is not None or preview_all):
        raise ValueError('Preview options cannot be combined with real delivery')
    now = now or datetime.now(timezone.utc)
    root = Path(root)
    root.mkdir(parents=True, exist_ok=True)
    ledger_root = Path(ledger_store) if ledger_store is not None else root
    if ledger_store is not None:
        if root.resolve() == ledger_root.resolve() or root.resolve() in ledger_root.resolve().parents or ledger_root.resolve() in root.resolve().parents:
            raise ValueError('Report and delivery stores must be separate directories')
        from prepare_delivery_store import load_ledger, assert_cutover

    def checkpoint():
        if ledger_store is None:
            persist(ledger_root, git)
        else:
            persist(ledger_root, git, branch='delivery-state')

    # Sender runs serialize with each other, independently of report collection.
    with (ledger_root / '.delivery.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        index = read_json(root / 'index.json', {'reports': []})
        ledger = (load_ledger(ledger_root) if ledger_store is not None
                  else read_json(root / 'state/deliveries.json', {}))
        if not isinstance(ledger, dict):
            raise ValueError('Legacy delivery state is retired or invalid; use the independent delivery ledger')
        if ledger_store is not None:
            assert_cutover(root, ledger_root)
        summary = {'sent': 0, 'prepared': 0, 'skipped': 0, 'deferred': 0, 'unknown': 0}
        deferred_reasons = {'missing_or_ineligible_report': 0, 'invalid_report_or_message': 0}
        for member in config['members']:
            period = due_period(member, now) if member['enabled'] else None
            if preview_all and member['enabled']:
                local = now.astimezone(ZoneInfo(member['timezone']))
                period = (local.date() - timedelta(days=local.weekday())).isoformat()
            if not period:
                summary['skipped'] += 1
                continue
            # Public archive state never includes names, addresses, or message bodies.
            key = hashlib.sha256((member['id'] + ':' + period).encode()).hexdigest()
            if key in ledger and not preview_all:
                if ledger[key].get('status') in ('sending', 'unknown'):
                    summary['unknown'] += 1
                else:
                    summary['skipped'] += 1
                continue
            selected = []
            for ticker in tickers_for(config, member):
                candidates = [r for r in index['reports'] if eligible_report(r, ticker, config, now)
                              and not r.get('advisory') and not report_advisory(root, r)]
                if not candidates:
                    selected = []
                    break
                selected.append(max(candidates, key=lambda r: datetime.fromisoformat(r['generated_at'])))
            if not selected:
                summary['deferred'] += 1
                deferred_reasons['missing_or_ineligible_report'] += 1
                continue
            paths, pdfs = [], []
            try:
                for entry in selected:
                    files = verified_report_files(root, entry)
                    paths.append(files['md']); pdfs.append(files['pdf'])
                message = build_email(paths, [member['email']], pdf_path=pdfs,
                                      brief=True, display_name=member['name'])
                message['Date'] = format_datetime(now)
                message['Message-ID'] = make_msgid()
                if len(message.as_bytes()) > 20 * 1024 * 1024:
                    raise ValueError('Digest exceeds the 20 MiB encoded message budget')
            except (ValueError, OSError, KeyError, TypeError):
                summary['deferred'] += 1
                deferred_reasons['invalid_report_or_message'] += 1
                continue
            if not really_send:
                if preview_dir is not None:
                    directory = Path(preview_dir)
                    # Never put a private email body in the public report archive.
                    resolved = directory.resolve()
                    store = root.resolve()
                    if resolved == store or store in resolved.parents:
                        raise ValueError('Private email previews must be outside the report store')
                    if resolved == ledger_root.resolve() or ledger_root.resolve() in resolved.parents:
                        raise ValueError('Private email previews must be outside the delivery store')
                    directory.mkdir(parents=True, exist_ok=True, mode=0o700)
                    target = directory / f'{key}.eml'
                    temporary = None
                    try:
                        with NamedTemporaryFile(dir=directory, delete=False) as stream:
                            temporary = Path(stream.name)
                            stream.write(message.as_bytes())
                        os.replace(temporary, target)
                    finally:
                        if temporary is not None:
                            temporary.unlink(missing_ok=True)
                summary['prepared'] += 1
                continue
            ledger[key] = {'period': period, 'status': 'sending', 'updated_at': now.isoformat(),
                           'reports': [r['report_id'] for r in selected]}
            write_json(ledger_root / 'state/deliveries.json', ledger)
            checkpoint()  # Failure here prevents the SMTP call.
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
            write_json(ledger_root / 'state/deliveries.json', ledger)
            checkpoint()
        if summary['deferred']:
            # Aggregate-only diagnostics: never expose member IDs, email addresses,
            # private holdings, or message content in GitHub Actions logs.
            print('Delivery deferral reasons: ' + json.dumps(deferred_reasons, sort_keys=True), flush=True)
        return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--store', type=Path, required=True)
    parser.add_argument('--ledger-store', type=Path, help='Independent delivery-state worktree')
    parser.add_argument('--send', action='store_true')
    parser.add_argument('--persist-git', action='store_true')
    parser.add_argument('--preview-dir', type=Path, help='Write private .eml previews outside the report store')
    parser.add_argument('--preview-all', action='store_true', help='Preview enabled members regardless of schedule or sent state')
    args = parser.parse_args()
    if args.send and os.environ.get('JSOSIF_APPROVED_SEND') != '1':
        parser.error('Set JSOSIF_APPROVED_SEND=1 to enable delivery')
    if args.send and args.ledger_store is None:
        parser.error('Real delivery requires --ledger-store; initialize the independent ledger first')
    if args.send and (args.preview_dir or args.preview_all):
        parser.error('Preview options cannot be combined with send')
    if args.send:
        GmailSmtpBackend().credentials()  # Fail configuration checks before reserving a weekly slot.
    result = deliver(load(args.config), args.store, really_send=args.send, git=args.persist_git,
                     preview_dir=args.preview_dir, preview_all=args.preview_all, ledger_store=args.ledger_store)
    if os.environ.get('GITHUB_ACTIONS') == 'true':
        print('::notice title=Weekly delivery summary::' + json.dumps(
            {'mode': 'send' if args.send else 'preview', **result}), flush=True)
    print(result)
    if result['unknown']:
        raise SystemExit('Delivery needs reconciliation; uncertain messages will not be retried automatically')
    if args.send and result['deferred']:
        raise SystemExit('Delivery deferred: eligible reports are missing or invalid; unreserved slots will be retried')


if __name__ == '__main__':
    main()
