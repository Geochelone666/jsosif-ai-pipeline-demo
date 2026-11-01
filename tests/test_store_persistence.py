"""Exercise real Git persistence and recovery without external network or credentials."""
from pathlib import Path
import subprocess

import pytest

from report_store import persist, read_json, write_json


def git(*args, cwd=None):
    return subprocess.run(['git', *args], cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


@pytest.fixture
def archive(tmp_path):
    remote = tmp_path / 'remote.git'
    git('init', '--bare', str(remote))
    store = tmp_path / 'store'
    git('init', '-b', 'report-data', str(store))
    git('remote', 'add', 'origin', str(remote), cwd=store)
    write_json(store / 'index.json', {'reports': [], 'sequence': 1})
    write_json(store / 'state/deliveries.json', {'synthetic-member-hash': {'status': 'sending'}})
    return store, remote


def test_persist_and_fresh_clone_restore_archive_and_delivery_reservations(archive, tmp_path):
    store, remote = archive
    persist(store, git=True)
    first = git('rev-parse', 'HEAD', cwd=store)
    persist(store, git=True)
    assert git('rev-parse', 'HEAD', cwd=store) == first
    write_json(store / 'index.json', {'reports': [], 'sequence': 2})
    persist(store, git=True)
    assert git('show', f'{first}:index.json', cwd=store).endswith('}')
    restored = tmp_path / 'restored'
    git('clone', '--branch', 'report-data', str(remote), str(restored))
    assert read_json(restored / 'index.json')['sequence'] == 2
    assert read_json(restored / 'state/deliveries.json')['synthetic-member-hash']['status'] == 'sending'


def test_rejected_push_is_not_success_and_can_be_recovered(archive):
    store, remote = archive
    hook = remote / 'hooks/pre-receive'
    hook.write_text('#!/bin/sh\nexit 1\n')
    hook.chmod(0o700)
    with pytest.raises(subprocess.CalledProcessError):
        persist(store, git=True)
    local = git('rev-parse', 'HEAD', cwd=store)
    hook.unlink()
    persist(store, git=True)
    assert git('rev-parse', 'HEAD', cwd=store) == local
    assert git('--git-dir', str(remote), 'rev-parse', 'refs/heads/report-data') == local


def test_transient_push_failure_retries_the_same_commit_without_force(archive, monkeypatch):
    import report_store
    store, remote = archive
    real_run = subprocess.run
    pushes = []
    def run(command, **kwargs):
        if command[:2] == ['git', 'push']:
            pushes.append(command)
            if len(pushes) == 1:
                return subprocess.CompletedProcess(command, 1, b'', b'temporarily unavailable')
        return real_run(command, **kwargs)
    monkeypatch.setattr(report_store.subprocess, 'run', run)
    delays = []
    persist(store, git=True, sleep=delays.append)
    assert delays == [2] and len(pushes) == 2
    assert all('--force' not in command for command in pushes)
    assert git('--git-dir', str(remote), 'rev-parse', 'refs/heads/report-data') == git('rev-parse', 'HEAD', cwd=store)


def test_push_category_classification():
    from report_store import push_category
    assert push_category('error: failed to push some refs (non-fast-forward)') == 'concurrent_writer'
    assert push_category('! [remote rejected] main (protected branch hook declined)') == 'repository_policy'
    assert push_category('Permission denied (publickey).') == 'authorization'
    assert push_category('Connection timed out during banner exchange') == 'transport_or_service'


def test_concurrent_writer_push_fails_closed_and_recovers_without_force(archive, tmp_path, monkeypatch):
    """A non-fast-forward push is classified concurrent_writer, never retried
    automatically and never forced; the local commit survives and a reviewed
    fast-forward reconciliation recovers the store."""
    import report_store
    store, remote = archive
    persist(store, git=True)  # establish the shared branch

    # A concurrent writer advances the shared branch independently.
    other = tmp_path / 'other'
    git('clone', '--branch', 'report-data', str(remote), str(other))
    write_json(other / 'concurrent.json', {'writer': 'other'})
    git('add', '--all', cwd=other)
    git('-c', 'user.name=test', '-c', 'user.email=test@example.com',
        'commit', '-m', 'Concurrent writer', cwd=other)
    git('push', 'origin', 'HEAD:report-data', cwd=other)

    # The stale writer fails closed: classified, single attempt, commit retained.
    write_json(store / 'index.json', {'reports': [], 'sequence': 2})
    pushes = []
    real_run = subprocess.run

    def run(command, **kwargs):
        if command[:2] == ['git', 'push']:
            pushes.append(command)
        return real_run(command, **kwargs)

    monkeypatch.setattr(report_store.subprocess, 'run', run)
    with pytest.raises(report_store.StorePushError) as err:
        persist(store, git=True)
    assert err.value.category == 'concurrent_writer'
    assert len(pushes) == 1
    assert all('--force' not in command for command in pushes)
    assert git('rev-parse', 'HEAD', cwd=store) != \
        git('--git-dir', str(remote), 'rev-parse', 'refs/heads/report-data')
    assert read_json(store / 'index.json')['sequence'] == 2

    # Runbook recovery: fetch, reconcile as a normal fast-forward merge, push.
    monkeypatch.setattr(report_store.subprocess, 'run', real_run)
    git('fetch', 'origin', cwd=store)
    git('-c', 'user.name=test', '-c', 'user.email=test@example.com',
        'merge', '--no-edit', 'origin/report-data', cwd=store)
    persist(store, git=True)
    head = git('rev-parse', 'HEAD', cwd=store)
    assert git('--git-dir', str(remote), 'rev-parse', 'refs/heads/report-data') == head
    assert git('show', head + ':concurrent.json', cwd=store) != ''
    assert read_json(store / 'index.json')['sequence'] == 2
