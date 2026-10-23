"""Preview or explicitly send one internal acceptance digest to the configured sender."""
import argparse
from datetime import datetime, timezone
from email import policy
from email.parser import BytesParser
import json
import os
from pathlib import Path
from zoneinfo import ZoneInfo

from deliver_weekly import deliver
from email_delivery import GmailSmtpBackend, validate_recipients
from subscriptions import validate


HOLDINGS = ['CNQ.TO', 'CSCO', 'JPM', 'BMO.TO', 'COST']


def self_config(sender, now):
    validate_recipients([sender])
    local = now.astimezone(ZoneInfo('America/Toronto'))
    return validate({'groups': {}, 'members': [{
        'id': 'internal-email-acceptance', 'name': 'JSOSIF Test', 'email': sender,
        'groups': [], 'tickers': HOLDINGS, 'enabled': True, 'timezone': 'America/Toronto',
        'send_weekday': local.weekday(), 'send_time': '00:00'}]})


def check(store, preview_dir, *, send=False, git=False, now=None, ledger_store=None):
    now = now or datetime.now(timezone.utc)
    sender = os.environ.get('GMAIL_USER', '')
    config = self_config(sender, now)
    if send:
        if os.environ.get('INTERNAL_EMAIL_CONFIRM') != 'SEND_ONE_TO_SELF':
            raise ValueError('Confirm SEND_ONE_TO_SELF before internal delivery')
        authenticated_sender, _ = GmailSmtpBackend().credentials()
        if authenticated_sender.lower() != sender.lower():
            raise ValueError('Internal delivery must use the configured sender itself')
        result = deliver(config, store, now=now, really_send=True, git=git, ledger_store=ledger_store)
    else:
        result = deliver(config, store, now=now, preview_dir=preview_dir, preview_all=True, ledger_store=ledger_store)
        if result['prepared']:
            paths = list(Path(preview_dir).glob('*.eml'))
            if len(paths) != 1:
                raise ValueError('Expected one private internal preview')
            message = BytesParser(policy=policy.default).parsebytes(paths[0].read_bytes())
            if str(message['To']) != sender or len(list(message.iter_attachments())) != len(HOLDINGS):
                raise ValueError('Internal preview recipient or attachment contract failed')
            result['recipient_is_sender'] = True
            result['attachments'] = [part.get_filename() for part in message.iter_attachments()]
            # The approved cover note contains only the synthetic display name,
            # public symbols and dates. Recipient headers remain private.
            result['body'] = message.get_body(preferencelist=('plain',)).get_content()
    if result['deferred'] or result['unknown']:
        raise ValueError('Internal acceptance is blocked by report readiness or delivery reconciliation')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--store', type=Path, required=True)
    parser.add_argument('--ledger-store', type=Path)
    parser.add_argument('--preview-dir', type=Path, required=True)
    parser.add_argument('--send', action='store_true')
    parser.add_argument('--persist-git', action='store_true')
    args = parser.parse_args()
    if args.send and args.ledger_store is None:
        parser.error('Real internal delivery requires the independent --ledger-store')
    result = check(args.store, args.preview_dir, send=args.send, git=args.persist_git, ledger_store=args.ledger_store)
    print(json.dumps(result))


if __name__ == '__main__':
    main()
