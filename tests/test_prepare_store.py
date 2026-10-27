"""open_store must initialize a clean orphan branch on old and new Git alike."""
import subprocess

import pytest

from prepare_store import open_store


def git(*args, cwd=None):
    return subprocess.run(['git', *args], cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


@pytest.fixture
def source(tmp_path, monkeypatch):
    remote = tmp_path / 'remote.git'
    git('init', '--bare', str(remote))
    repo = tmp_path / 'src'
    git('init', '-b', 'main', str(repo))
    git('config', 'user.email', 'test@example.com', cwd=repo)
    git('config', 'user.name', 'Test', cwd=repo)
    (repo / 'code.py').write_text('x = 1\n')
    git('add', '.', cwd=repo)
    git('commit', '-m', 'init', cwd=repo)
    git('remote', 'add', 'origin', str(remote), cwd=repo)
    monkeypatch.chdir(repo)
    return repo


def test_initializes_empty_orphan_without_touching_source_head(source, tmp_path):
    head = git('rev-parse', 'HEAD', cwd=source)
    store = tmp_path / 'store'
    assert open_store(store) is True
    assert git('rev-parse', 'HEAD', cwd=source) == head
    assert git('branch', '--show-current', cwd=source) == 'main'
    assert git('branch', '--show-current', cwd=store) == 'report-data'
    assert not (store / 'code.py').exists()
    assert (store / '.gitignore').read_text() == '.delivery.lock\n*.tmp\n'
    assert git('ls-files', cwd=store) == ''


def test_rejects_unknown_branch_existing_path_and_uninitialized_state(source, tmp_path):
    with pytest.raises(ValueError):
        open_store(tmp_path / 'a', branch='main')
    (tmp_path / 'b').mkdir()
    with pytest.raises(ValueError):
        open_store(tmp_path / 'b')
    with pytest.raises(ValueError):
        open_store(tmp_path / 'c', branch='delivery-state', initialize=False)
