"""Versioned report files and atomic JSON state in a separately persisted directory."""
import hashlib
import json
from pathlib import Path
import subprocess


def read_json(path, default=None):
    try:
        return json.loads(Path(path).read_text(encoding='utf-8'))
    except FileNotFoundError:
        return default


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    tmp.replace(path)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def resolve_file(root, relative):
    root = Path(root).resolve()
    path = (root / relative).resolve()
    if root not in path.parents or not path.is_file():
        raise ValueError('Report path is outside the store or missing')
    return path


def persist(root, git=False):
    """Commit before SMTP, so an interrupted transport cannot trigger a blind retry."""
    if not git:
        return
    root = Path(root)
    subprocess.run(['git', 'add', '--all'], cwd=root, check=True, capture_output=True)
    changed = subprocess.run(['git', 'diff', '--cached', '--quiet'], cwd=root).returncode
    if changed:
        subprocess.run(['git', '-c', 'user.name=github-actions[bot]', '-c',
                        'user.email=41898282+github-actions[bot]@users.noreply.github.com',
                        'commit', '-m', 'Update report archive and delivery state'],
                       cwd=root, check=True, capture_output=True)
    # Retry a pending push even if a previous commit succeeded locally.
    subprocess.run(['git', 'push', 'origin', 'HEAD:report-data'], cwd=root,
                   check=True, capture_output=True)
