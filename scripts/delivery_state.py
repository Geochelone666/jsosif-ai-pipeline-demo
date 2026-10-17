"""Explicitly reconcile an uncertain SMTP attempt after checking the sender mailbox."""
import argparse
import hashlib
from pathlib import Path

from report_store import read_json, write_json, persist


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--store', type=Path, required=True)
    parser.add_argument('--member-id', required=True)
    parser.add_argument('--period', required=True, help='Local Monday YYYY-MM-DD shown in the delivery ledger')
    parser.add_argument('--resolution', choices=['accepted', 'retry'], required=True)
    parser.add_argument('--persist-git', action='store_true')
    args = parser.parse_args()
    key = hashlib.sha256((args.member_id + ':' + args.period).encode()).hexdigest()
    path = args.store / 'state/deliveries.json'
    ledger = read_json(path, {})
    if key not in ledger or ledger[key]['status'] not in ('sending', 'unknown'):
        parser.error('No uncertain delivery matches this member and week')
    if args.resolution == 'retry':
        del ledger[key]
    else:
        ledger[key]['status'] = 'accepted'
    write_json(path, ledger)
    persist(args.store, args.persist_git)
    print('Delivery reconciliation saved')


if __name__ == '__main__':
    main()
