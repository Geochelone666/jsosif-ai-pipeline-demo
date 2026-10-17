"""Build a static latest/history site from the persisted archive, excluding private state."""
import argparse
from pathlib import Path
import shutil
from tempfile import TemporaryDirectory

from report_store import read_json, write_json, resolve_file, digest


def build(store, output, template=None):
    if Path(output).is_symlink():
        raise ValueError('Site output must not be a symlink')
    store, output = Path(store).resolve(), Path(output).resolve()
    if store == output or store in output.parents or output in store.parents:
        raise ValueError('Site output and report store must not overlap')
    index = read_json(store / 'index.json')
    if not isinstance(index, dict) or not isinstance(index.get('reports'), list):
        raise ValueError('A valid persisted archive index is required before building the site')
    if output.exists():
        if not output.is_dir() or (any(output.iterdir()) and not (output / '.jsosif-site-build').is_file()):
            raise ValueError('Refusing to replace a nonempty directory without the site-build marker')
    output.parent.mkdir(parents=True, exist_ok=True)
    template = template or Path(__file__).resolve().parents[1] / 'docs/index.html'
    # Build in a sibling directory first; a bad report must preserve the last good site.
    with TemporaryDirectory(prefix='.jsosif-site-', dir=output.parent) as temporary:
        stage = Path(temporary) / 'build'
        stage.mkdir()
        shutil.copy2(template, stage / 'index.html')
        members_page = Path(template).with_name('members.html')
        if members_page.is_file():
            shutil.copy2(members_page, stage / 'members.html')
        for entry in index['reports']:
            for kind in ('md', 'json', 'pdf'):
                source = resolve_file(store, entry[kind])
                if digest(source) != entry['sha256'][kind]:
                    raise ValueError('Report integrity check failed')
                target = stage / entry[kind]
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
        # Delivery/quota state, member config and credentials never enter the site.
        write_json(stage / 'index.json', index)
        (stage / '.nojekyll').touch()
        (stage / '.jsosif-site-build').touch()
        backup = Path(temporary) / 'previous'
        if output.exists():
            output.rename(backup)
        try:
            stage.rename(output)
        except OSError:
            if backup.exists():
                backup.rename(output)
            raise
    return index


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--store', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    index = build(args.store, args.output)
    print(f'Site built: {len(index["reports"])} report versions')


if __name__ == '__main__':
    main()
