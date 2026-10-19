"""Versioned report files and atomic JSON state in a separately persisted directory."""
import hashlib
import json
from datetime import date
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
    if not isinstance(relative, str) or not relative or '\\' in relative:
        raise ValueError('Report path must be a relative file path')
    relative = Path(relative)
    if relative.is_absolute() or '..' in relative.parts:
        raise ValueError('Report path must stay relative to the store')
    root = Path(root).resolve()
    path = (root / relative).resolve()
    if root not in path.parents or not path.is_file():
        raise ValueError('Report path is outside the store or missing')
    return path


def verified_report_files(root, entry):
    """Verify an archived version's files, snapshot identity and publication quality."""
    from snapshot_contract import validate_snapshot

    paths = {}
    stamp = date.fromisoformat(entry['as_of']).isoformat().replace('-', '')
    stem = f"{entry['ticker']}-intelligence-{stamp}"
    for kind in ('md', 'json', 'pdf'):
        path = resolve_file(root, entry[kind])
        relative = Path(entry[kind])
        if relative.parts[0] != 'archive' or relative.name != f'{stem}.{kind}':
            raise ValueError('Report filename and archive identity disagree')
        if digest(path) != entry['sha256'][kind]:
            raise ValueError('Report integrity check failed')
        paths[kind] = path
    if any(path.parent != paths['md'].parent for path in paths.values()):
        raise ValueError('Report files must belong to the same archived version')
    payload = read_json(paths['json'])
    if validate_snapshot(payload):
        raise ValueError('Invalid archived snapshot contract')
    if (payload['identity']['ticker'] != entry['ticker'] or
            payload['identity']['as_of'] != entry['as_of'] or
            payload.get('quality') != entry['quality']):
        raise ValueError('Archive index and snapshot metadata disagree')
    if not paths['pdf'].read_bytes().startswith(b'%PDF-'):
        raise ValueError('Invalid archived PDF')
    return paths


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
