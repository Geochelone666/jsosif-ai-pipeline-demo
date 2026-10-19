"""Load a private JSON configuration and/or member spreadsheet from workflow secrets."""
import argparse
import json
import os
from pathlib import Path

from subscriptions import import_members_csv, validate, write_private_config, load


def prepare(path, *, required=False):
    raw_json = os.environ.get('SUBSCRIPTIONS_JSON', '').strip()
    raw_csv = os.environ.get('MEMBERS_CSV', '').strip()
    if not raw_json and not raw_csv:
        if required:
            raise ValueError('Configure the private MEMBERS_CSV or SUBSCRIPTIONS_JSON repository secret')
        return False
    config = json.loads(raw_json) if raw_json else {'groups': {}, 'members': []}
    if raw_csv:
        config = import_members_csv(config, raw_csv)
    write_private_config(path, validate(config))
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', type=Path)
    parser.add_argument('--required', action='store_true')
    args = parser.parse_args()
    try:
        saved = prepare(args.path, required=args.required)
    except (ValueError, OSError):
        parser.error('Private member configuration is missing or invalid; check the JSON/CSV and schema')
    enabled = sum(member['enabled'] for member in load(args.path)['members']) if saved else 0
    if os.environ.get('GITHUB_OUTPUT'):
        with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as output:
            output.write('configured=' + str(saved).lower() + '\n')
            output.write('email_members=' + str(enabled) + '\n')
    print('Private subscriptions validated and loaded' if saved else 'No private roster configured')


if __name__ == '__main__':
    main()
