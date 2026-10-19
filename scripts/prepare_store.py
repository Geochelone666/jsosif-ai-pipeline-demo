"""Open or initialize the report-data branch using checkout's configured credential helper."""
import argparse
from pathlib import Path
import subprocess


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', type=Path)
    args = parser.parse_args()
    path = args.path.resolve()
    if path.exists():
        raise ValueError('Store path must not exist')
    remote = subprocess.run(['git', 'ls-remote', '--exit-code', '--heads', 'origin', 'report-data'],
                            capture_output=True)
    if remote.returncode not in (0, 2):
        raise RuntimeError('Cannot inspect persistent store; refusing to initialize over unknown state')
    if remote.returncode == 0:
        subprocess.run(['git', 'fetch', 'origin', 'refs/heads/report-data:refs/remotes/origin/report-data'],
                       check=True, capture_output=True)
        subprocess.run(['git', 'worktree', 'add', '--detach', str(path),
                        'refs/remotes/origin/report-data'], check=True)
    else:
        # Git >= 2.42 supports a clean orphan worktree, without changing source HEAD.
        subprocess.run(['git', 'worktree', 'add', '--orphan', '-b', 'report-data', str(path)], check=True)
        (path / '.gitignore').write_text('.delivery.lock\n*.tmp\n', encoding='utf-8')


if __name__ == '__main__':
    main()
