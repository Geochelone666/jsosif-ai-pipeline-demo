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
