"""Open or initialize the report-data branch using checkout's configured credential helper."""
import argparse
from pathlib import Path
import subprocess


def _add_orphan_worktree(path, branch):
    """Create an empty orphan worktree on `branch` without changing source HEAD.

    Git >= 2.42 has `worktree add --orphan`. Older Git (for example 2.34 on
    Ubuntu 22.04) rejects it, so fall back to a detached worktree whose index
    and files are emptied after `checkout --orphan`.
    """
    modern = subprocess.run(['git', 'worktree', 'add', '--orphan', '-b', branch, str(path)],
                            capture_output=True)
    if modern.returncode == 0:
        return
    if path.exists() and any(path.iterdir()):
        raise RuntimeError('Cannot create orphan worktree: ' + modern.stderr.decode(errors='replace').strip())
    subprocess.run(['git', 'worktree', 'prune'], check=True, capture_output=True)
    subprocess.run(['git', 'worktree', 'add', '--detach', str(path), 'HEAD'],
                   check=True, capture_output=True)
    try:
        subprocess.run(['git', '-C', str(path), 'checkout', '--orphan', branch],
                       check=True, capture_output=True)
        subprocess.run(['git', '-C', str(path), 'rm', '-rfq', '--ignore-unmatch', '.'],
                       check=True, capture_output=True)
    except Exception:
        subprocess.run(['git', 'worktree', 'remove', '--force', str(path)], capture_output=True)
        raise


def open_store(path, *, branch='report-data', initialize=True):
    if branch not in ('report-data', 'delivery-state'):
        raise ValueError('Unknown persistent store branch')
    path = Path(path).resolve()
    if path.exists():
        raise ValueError('Store path must not exist')
    remote = subprocess.run(['git', 'ls-remote', '--exit-code', '--heads', 'origin', branch],
                            capture_output=True)
    if remote.returncode not in (0, 2):
        raise RuntimeError('Cannot inspect persistent store; refusing to initialize over unknown state')
    if remote.returncode == 0:
        subprocess.run(['git', 'fetch', 'origin', f'refs/heads/{branch}:refs/remotes/origin/{branch}'],
                       check=True, capture_output=True)
        subprocess.run(['git', 'worktree', 'add', '--detach', str(path),
                        f'refs/remotes/origin/{branch}'], check=True)
    else:
        if not initialize:
            raise ValueError('Persistent delivery state is not initialized; run the guarded migration first')
        _add_orphan_worktree(path, branch)
        (path / '.gitignore').write_text('.delivery.lock\n*.tmp\n', encoding='utf-8')
    return remote.returncode == 2


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', type=Path)
    args = parser.parse_args()
    open_store(args.path)


if __name__ == '__main__':
    main()
