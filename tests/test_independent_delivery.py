"""Real Git branch isolation and durable duplicate guards, without live SMTP."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess

import pytest

from deliver_weekly import deliver
from prepare_delivery_store import prepare, load_ledger, assert_legacy_senders_drained
from report_store import persist, write_json, digest, StorePushError
from snapshot_emit import emit_frozen_snapshot


NOW = datetime(2026, 10, 23, 14, tzinfo=timezone.utc)


def git(*args, cwd=None):
    return subprocess.run(['git', *args], cwd=cwd, capture_output=True, text=True, check=True).stdout.strip()


def key(member):
    return hashlib.sha256((member + ':2026-10-19').encode()).hexdigest()


def record(status):
    return {'status': status, 'period': '2026-10-19', 'reports': ['old/CSCO'], 'updated_at': NOW.isoformat()}


@pytest.fixture
def stores(tmp_path, monkeypatch):
    remote, source, reports, ledger = [tmp_path / name for name in ('remote.git', 'source', 'reports', 'ledger')]
    git('init', '--bare', str(remote))
    git('init', '-b', 'main', str(source))
    git('remote', 'add', 'origin', str(remote), cwd=source)
    (source / 'README').write_text('Synthetic source checkout\n')
    git('add', '.', cwd=source)
    git('-c', 'user.name=Test', '-c', 'user.email=test@example.com', 'commit', '-m', 'Initialize', cwd=source)
    monkeypatch.chdir(source)
    git('worktree', 'add', '--orphan', '-b', 'report-data', str(reports))
    entry = {'ticker': 'CSCO', 'report_id': 'current/CSCO', 'quality': 'ready',
             'generated_at': NOW.isoformat(), 'as_of': '2026-10-23', 'sha256': {}}
    snapshot = emit_frozen_snapshot(ticker='CSCO', as_of='2026-10-23', quant_metrics={'Close': 100},
                                    ai={'status': 'Available'}, freshness={}, disclaimer='Not investment advice.')
    snapshot['quality'] = 'ready'
    for kind, value in [('md', '# CSCO\n'), ('pdf', '%PDF-1.4 synthetic'), ('json', json.dumps(snapshot))]:
        target = reports / 'archive' / ('CSCO-intelligence-20261023.' + kind)
        target.parent.mkdir(exist_ok=True)
        target.write_text(value)
        entry[kind] = target.relative_to(reports).as_posix()
        entry['sha256'][kind] = digest(target)
    write_json(reports / 'index.json', {'reports': [entry]})
    write_json(reports / 'state/deliveries.json', {key('old'): record('accepted'), key('uncertain'): record('unknown')})
    persist(reports, git=True)
    config = {'groups': {}, 'members': [{'id': 'new', 'name': 'Example Analyst', 'email': 'analyst@example.com',
              'tickers': ['CSCO'], 'groups': [], 'enabled': True, 'timezone': 'America/Toronto',
              'send_weekday': 4, 'send_time': '09:00'}]}
    return remote, reports, ledger, config


def initialize(stores):
    _, reports, ledger, _ = stores
    assert prepare(ledger, archive=reports, initialize=True, git=True) == 2


def test_migration_preserves_history_and_will_not_reseed_existing_state(stores, tmp_path):
    remote, reports, ledger, _ = stores
    before = (reports / 'state/deliveries.json').read_bytes()
    initialize(stores)
    assert (ledger / 'state/deliveries.json').read_bytes() == before
    assert json.loads((reports / 'state/deliveries.json').read_text()) is None
    manifest = json.loads((ledger / 'state/migration.json').read_text())
    original = git('--git-dir', str(remote), 'show', manifest['source_commit'] + ':state/deliveries.json')
    assert json.loads(original) == json.loads(before)
    assert not (ledger / 'index.json').exists()
    reopened = tmp_path / 'reopened'
    assert prepare(reopened, archive=reports, initialize=True, git=True) == 2
    assert (reopened / 'state/deliveries.json').read_bytes() == before


def test_old_sender_and_incomplete_cutover_cannot_submit_mail(stores):
    _, reports, ledger, config = stores
    initialize(stores)
    never = lambda message: pytest.fail('Incomplete or retired sender must not contact SMTP')
    with pytest.raises(ValueError, match='retired'):
        deliver(config, reports, now=NOW, really_send=True, backend=never)
    (reports / 'state/delivery-migration.json').unlink()
    with pytest.raises(FileNotFoundError):
        deliver(config, reports, ledger_store=ledger, now=NOW, really_send=True, backend=never)


def test_missing_migration_fails_without_creating_a_remote_branch(stores):
    remote, _, ledger, _ = stores
    with pytest.raises(ValueError, match='migration'):
        prepare(ledger)
    assert git('ls-remote', '--heads', str(remote), 'delivery-state') == ''


@pytest.mark.parametrize('member,status,summary_field', [('old', 'accepted', 'skipped'), ('uncertain', 'unknown', 'unknown')])
def test_migrated_reservations_prevent_resubmission(stores, member, status, summary_field):
    _, reports, ledger, config = stores
    initialize(stores)
    config['members'][0]['id'] = member
    result = deliver(config, reports, ledger_store=ledger, now=NOW, really_send=True, git=True,
                     backend=lambda message: pytest.fail('Migrated reservations must prevent SMTP'))
    assert result[summary_field] == 1
    assert load_ledger(ledger)[key(member)]['status'] == status


def test_bad_legacy_state_cannot_publish_an_empty_delivery_branch(stores):
    remote, reports, ledger, _ = stores
    (reports / 'state/deliveries.json').write_text('invalid json')
    with pytest.raises(ValueError):
        prepare(ledger, archive=reports, initialize=True, git=True)
    assert git('ls-remote', '--heads', str(remote), 'delivery-state') == ''


def test_migration_rejects_private_fields_instead_of_publishing_them(stores):
    remote, reports, ledger, _ = stores
    source = json.loads((reports / 'state/deliveries.json').read_text())
    source[key('old')]['email'] = 'analyst@example.com'
    write_json(reports / 'state/deliveries.json', source)
    with pytest.raises(ValueError, match='Invalid delivery reservation'):
        prepare(ledger, archive=reports, initialize=True, git=True)
    assert git('ls-remote', '--heads', str(remote), 'delivery-state') == ''


def test_failed_cutover_stops_senders_and_can_resume_without_reseeding(stores, tmp_path):
    remote, reports, ledger, config = stores
    hook = remote / 'hooks/pre-receive'
    hook.write_text('#!/bin/sh\nwhile read previous next ref; do\n'
                    '  if [ "$ref" = refs/heads/report-data ]; then exit 1; fi\ndone\nexit 0\n')
    hook.chmod(0o700)
    with pytest.raises(StorePushError):
        prepare(ledger, archive=reports, initialize=True, git=True)
    fresh_reports, fresh_ledger = tmp_path / 'fresh-reports', tmp_path / 'fresh-ledger'
    git('clone', '--branch', 'report-data', str(remote), str(fresh_reports))
    prepare(fresh_ledger)
    with pytest.raises(FileNotFoundError):
        deliver(config, fresh_reports, ledger_store=fresh_ledger, now=NOW, really_send=True,
                backend=lambda message: pytest.fail('An incomplete cutover must not contact SMTP'))
    hook.unlink()
    repaired = tmp_path / 'repaired-ledger'
    assert prepare(repaired, archive=fresh_reports, initialize=True, git=True) == 2
    assert load_ledger(repaired) == load_ledger(ledger)


def test_sender_and_collector_push_independently_and_retry_skips(stores, tmp_path):
    remote, reports, ledger, config = stores
    initialize(stores)
    original_files = {str(p.relative_to(reports)): p.read_bytes()
                      for p in reports.rglob('*') if p.is_file() and p.name != '.git'}
    collector = tmp_path / 'collector'
    git('clone', '--branch', 'report-data', str(remote), str(collector))
    write_json(collector / 'progress.json', {'ticker': 'JPM', 'status': 'running'})
    persist(collector, git=True)
    report_heads = [git('--git-dir', str(remote), 'rev-parse', 'refs/heads/report-data')]
    submitted = []

    def smtp(message):
        reserved = json.loads(git('--git-dir', str(remote), 'show', 'delivery-state:state/deliveries.json'))
        assert reserved[key('new')]['status'] == 'sending'
        write_json(collector / 'progress.json', {'ticker': 'JPM', 'status': 'complete'})
        persist(collector, git=True)
        report_heads.append(git('--git-dir', str(remote), 'rev-parse', 'refs/heads/report-data'))
        submitted.append(message)

    result = deliver(config, reports, ledger_store=ledger, now=NOW, really_send=True, git=True, backend=smtp)
    assert result['sent'] == 1 and len(submitted) == 1
    assert len(set(report_heads)) == 2
    assert git('--git-dir', str(remote), 'rev-parse', 'refs/heads/report-data') == report_heads[-1]
    assert all((reports / name).read_bytes() == value for name, value in original_files.items())
    assert not (reports / '.delivery.lock').exists()
    restored = tmp_path / 'restored-ledger'
    prepare(restored)
    retry = deliver(config, reports, ledger_store=restored, now=NOW, really_send=True, git=True, backend=smtp)
    assert retry['skipped'] == 1 and len(submitted) == 1
    assert load_ledger(restored)[key('uncertain')]['status'] == 'unknown'


def test_stale_sender_push_fails_before_a_duplicate_smtp_submission(stores, tmp_path):
    _, reports, ledger, config = stores
    initialize(stores)
    stale = tmp_path / 'stale'
    prepare(stale)
    calls = []
    deliver(config, reports, ledger_store=ledger, now=NOW, really_send=True, git=True, backend=calls.append)
    with pytest.raises(StorePushError) as error:
        deliver(config, reports, ledger_store=stale, now=NOW, really_send=True, git=True, backend=calls.append)
    assert error.value.category == 'concurrent_writer'
    assert len(calls) == 1


def test_uncertain_smtp_result_survives_restore_without_resubmission(stores, tmp_path):
    _, reports, ledger, config = stores
    initialize(stores)

    def uncertain(message):
        raise TimeoutError('Synthetic lost acknowledgement')

    result = deliver(config, reports, ledger_store=ledger, now=NOW, really_send=True, git=True, backend=uncertain)
    assert result['unknown'] == 1
    restored = tmp_path / 'restored'
    prepare(restored)
    retry = deliver(config, reports, ledger_store=restored, now=NOW, really_send=True,
                    backend=lambda message: pytest.fail('Never resubmit an uncertain message'))
    assert retry['unknown'] == 1


@pytest.mark.parametrize('damaged', [None, 'not json', '[]', '{}'])
def test_missing_or_corrupt_state_cannot_fall_back_to_legacy_history(stores, damaged):
    _, reports, ledger, config = stores
    initialize(stores)
    path = ledger / 'state/deliveries.json'
    if damaged is None:
        path.unlink()
    else:
        path.write_text(damaged)
    with pytest.raises((ValueError, FileNotFoundError)):
        deliver(config, reports, ledger_store=ledger, now=NOW, really_send=True,
                backend=lambda message: pytest.fail('Broken ledger must stop SMTP'))


def test_preview_cannot_write_private_messages_into_the_ledger(stores):
    _, reports, ledger, config = stores
    initialize(stores)
    with pytest.raises(ValueError, match='outside the delivery store'):
        deliver(config, reports, ledger_store=ledger, now=NOW, preview_all=True, preview_dir=ledger / 'previews')


def test_migration_blocks_old_senders_but_accepts_current_queued_runs(monkeypatch):
    import prepare_delivery_store as migration

    def response(command, **kwargs):
        return subprocess.CompletedProcess(command, 0, 'new-head\n', '')

    monkeypatch.setattr(migration.subprocess, 'run', response)
    assert_legacy_senders_drained('example/repository', 'new-head')
    monkeypatch.setattr(migration.subprocess, 'run', lambda command, **kwargs:
                        subprocess.CompletedProcess(command, 0, 'old-head\n', ''))
    with pytest.raises(ValueError, match='old sender'):
        assert_legacy_senders_drained('example/repository', 'new-head')
