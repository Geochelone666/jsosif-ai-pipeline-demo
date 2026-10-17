"""Private member/group configuration, including a CSV import for manual entry."""
import argparse
import csv
import json
import re
from pathlib import Path
from zoneinfo import ZoneInfo

from email_delivery import validate_recipients
from universe import SUPPORTED


def validate(config):
    if not isinstance(config, dict) or not isinstance(config.get('groups'), dict):
        raise ValueError('Expected groups object and members list')
    groups, members = config['groups'], config.get('members')
    if not isinstance(members, list):
        raise ValueError('members must be a list')
    for key, group in groups.items():
        if not isinstance(key, str) or not key.strip() or not isinstance(group, dict):
            raise ValueError('Each group needs a nonblank id and an object')
        tickers = group.get('tickers')
        if not isinstance(tickers, list) or not tickers or any(not isinstance(t, str) or t not in SUPPORTED for t in tickers):
            raise ValueError(f'Group {key}: tickers must be supported symbols')
    ids, emails = set(), set()
    for member in members:
        if not isinstance(member, dict):
            raise ValueError('Each member must be an object')
        for field in ('id', 'name', 'email', 'timezone', 'send_time'):
            value = member.get(field)
            if not isinstance(value, str) or not value.strip() or any(ord(c) < 32 for c in value):
                raise ValueError(f'Member {field} must be nonblank text without control characters')
        validate_recipients([member['email']])
        if member['id'] in ids or member['email'].lower() in emails:
            raise ValueError('Duplicate member id or email; combine group memberships into one record')
        ids.add(member['id']); emails.add(member['email'].lower())
        if type(member.get('enabled')) is not bool:
            raise ValueError('enabled must be true or false')
        if type(member.get('send_weekday')) is not int or not 0 <= member['send_weekday'] <= 6:
            raise ValueError('send_weekday must be 0 (Monday) to 6 (Sunday)')
        if not re.fullmatch(r'(?:[01][0-9]|2[0-3]):[0-5][0-9]', member['send_time']):
            raise ValueError('send_time must be HH:MM')
        try:
            ZoneInfo(member['timezone'])
        except (KeyError, ValueError):
            raise ValueError('timezone must be an IANA time zone') from None
        assigned = member.get('groups')
        if not isinstance(assigned, list) or not assigned or any(not isinstance(g, str) or g not in groups for g in assigned):
            raise ValueError('Every member needs known group ids')
    for key in ('allow_degraded',):
        if key in config and type(config[key]) is not bool:
            raise ValueError(f'{key} must be boolean')
    max_age = config.get('max_report_age_days', 4)
    if type(max_age) is not int or not 0 <= max_age <= 30:
        raise ValueError('max_report_age_days must be 0 to 30')
    return config


def load(path):
    return validate(json.loads(Path(path).read_text(encoding='utf-8')))


def tickers_for(config, member=None):
    group_ids = member['groups'] if member else {
        group for m in config['members'] if m['enabled'] for group in m['groups']}
    return sorted({ticker for group in group_ids for ticker in config['groups'][group]['tickers']})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('config', type=Path)
    parser.add_argument('--import-csv', type=Path, help='Replace members from a manually entered CSV')
    args = parser.parse_args()
    config = json.loads(args.config.read_text(encoding='utf-8'))
    if args.import_csv:
        rows = []
        with args.import_csv.open(encoding='utf-8-sig', newline='') as stream:
            for row in csv.DictReader(stream):
                if row.get('enabled', '').lower() not in ('true', 'false'):
                    raise ValueError('CSV enabled must be true/false')
                rows.append({**row, 'enabled': row['enabled'].lower() == 'true',
                             'send_weekday': int(row['send_weekday']),
                             'groups': [g.strip() for g in row['groups'].split(';') if g.strip()]})
        config['members'] = rows
    validate(config)
    if args.import_csv:
        args.config.write_text(json.dumps(config, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Configuration valid: {len(config["members"])} members; {len(tickers_for(config))} active tickers')


if __name__ == '__main__':
    main()
