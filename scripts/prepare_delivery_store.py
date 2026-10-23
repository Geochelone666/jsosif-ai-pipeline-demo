"""Open the independent ledger; migration preserves every legacy reservation."""
import argparse
from datetime import date, datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess

from prepare_store import open_store
from report_store import persist, write_json


def load_ledger(root, *, require_manifest=True):
    # Missing or damaged state must never become an empty sending history.
    ledger = json.loads((Path(root) / 'state/deliveries.json').read_text(encoding='utf-8'))
    if not isinstance(ledger, dict):
        raise ValueError('Invalid delivery ledger')
    for key, record in ledger.items():
        if (not isinstance(key, str) or not re.fullmatch('[a-f0-9]{64}', key)
                or not isinstance(record, dict) or record.get('status') not in ('accepted', 'sending', 'unknown')
                or set(record) != {'period', 'status', 'reports', 'updated_at'}
                or not isinstance(record.get('reports'), list)
                or not record['reports']
                or not all(isinstance(value, str) and re.fullmatch(r'[A-Za-z0-9._-]+/[A-Z0-9][A-Z0-9.-]*', value)
                           for value in record['reports'])):
            raise ValueError('Invalid delivery reservation')
        date.fromisoformat(record['period'])
        if datetime.fromisoformat(record['updated_at']).utcoffset() is None:
            raise ValueError('Delivery timestamps must include a time zone')
    if require_manifest:
        manifest = json.loads((Path(root) / 'state/migration.json').read_text(encoding='utf-8'))
        if (not isinstance(manifest, dict)
                or set(manifest) != {'schema_version', 'source_branch', 'source_commit', 'entries', 'seed_keys', 'migrated_at'}
                or type(manifest.get('schema_version')) is not int or manifest['schema_version'] != 1
                or manifest.get('source_branch') != 'report-data'
                or not isinstance(manifest.get('source_commit'), str)
                or not re.fullmatch('[a-f0-9]{40}|[a-f0-9]{64}', manifest['source_commit'])
                or not isinstance(manifest.get('seed_keys'), list)
                or not all(isinstance(key, str) and re.fullmatch('[a-f0-9]{64}', key)
                           for key in manifest['seed_keys'])
                or type(manifest.get('entries')) is not int
                or manifest['entries'] != len(set(manifest['seed_keys']))
                or not set(manifest['seed_keys']) <= ledger.keys()):
            raise ValueError('Migrated delivery reservations are missing or invalid')
        if datetime.fromisoformat(manifest['migrated_at']).utcoffset() is None:
            raise ValueError('Migration timestamps must include a time zone')
    return ledger


def assert_legacy_senders_drained(repo, head):
    names = ('Weekly member PDF delivery', 'Internal email acceptance')
    expression = '.workflow_runs[] | select(.name == "' + names[0] + '" or .name == "' + names[1] + '") | .head_sha'
    for status in ('queued', 'in_progress', 'waiting', 'pending', 'requested'):
        result = subprocess.run(['gh', 'api', '--paginate',
            f'repos/{repo}/actions/runs?status={status}&per_page=100', '--jq', expression],
            capture_output=True, text=True, check=True)
        if any(value != head for value in result.stdout.splitlines() if value):
            raise ValueError('Drain or cancel old sender runs before migrating the delivery ledger')


def assert_cutover(archive, ledger_root):
    archive, ledger_root = Path(archive), Path(ledger_root)
    manifest = json.loads((ledger_root / 'state/migration.json').read_text(encoding='utf-8'))
    marker = json.loads((archive / 'state/delivery-migration.json').read_text(encoding='utf-8'))
    legacy = json.loads((archive / 'state/deliveries.json').read_text(encoding='utf-8'))
    if (legacy is not None or not isinstance(marker, dict)
            or marker.get('branch') != 'delivery-state'
            or marker.get('source_commit') != manifest['source_commit']):
        raise ValueError('Delivery cutover is incomplete; do not send until migration completes')


def retire_legacy(archive, ledger_root, *, git=False):
    archive, ledger_root = Path(archive), Path(ledger_root)
    legacy = json.loads((archive / 'state/deliveries.json').read_text(encoding='utf-8'))
    if legacy is None:
        assert_cutover(archive, ledger_root)
        return
    ledger = load_ledger(ledger_root)
    if load_ledger(archive, require_manifest=False) != ledger:
        raise ValueError('Legacy state changed during cutover; reconcile reservations before retrying')
    manifest = json.loads((ledger_root / 'state/migration.json').read_text(encoding='utf-8'))
    # A valid JSON null makes pre-cutover senders fail before SMTP instead of
    # silently using a stale history. The full original ledger remains in Git
    # and in the independent branch; no historical report files are changed.
    write_json(archive / 'state/deliveries.json', None)
    write_json(archive / 'state/delivery-migration.json', {
        'branch': 'delivery-state', 'source_commit': manifest['source_commit']})
    persist(archive, git)


def prepare(path, *, archive=None, initialize=False, git=False):
    created = open_store(path, branch='delivery-state', initialize=initialize)
    if created:
        if archive is None:
            raise ValueError('Migration requires the legacy report archive')
        ledger = load_ledger(archive, require_manifest=False)
        source = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=archive,
                                capture_output=True, text=True, check=True).stdout.strip()
        write_json(Path(path) / 'state/deliveries.json', ledger)
        write_json(Path(path) / 'state/migration.json', {
            'schema_version': 1, 'source_branch': 'report-data', 'source_commit': source,
            'entries': len(ledger), 'seed_keys': sorted(ledger),
            'migrated_at': datetime.now(timezone.utc).isoformat()})
        persist(path, git, branch='delivery-state')
    else:
        ledger = load_ledger(path)
    if archive is not None:
        if initialize:
            retire_legacy(archive, path, git=git)
        assert_cutover(archive, path)
    return len(ledger)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', type=Path)
    parser.add_argument('--archive', type=Path)
    parser.add_argument('--initialize', action='store_true')
    parser.add_argument('--persist-git', action='store_true')
    args = parser.parse_args()
    if not args.archive:
        parser.error('--archive is required to verify the completed cutover')
    if args.initialize:
        if not args.archive or not args.persist_git:
            parser.error('Migration requires --archive and --persist-git')
        if os.environ.get('GITHUB_ACTIONS') == 'true':
            assert_legacy_senders_drained(os.environ['GITHUB_REPOSITORY'], os.environ['GITHUB_SHA'])
    count = prepare(args.path, archive=args.archive, initialize=args.initialize, git=args.persist_git)
    print(f'Independent delivery ledger validated: {count} reservations')


if __name__ == '__main__':
    main()
