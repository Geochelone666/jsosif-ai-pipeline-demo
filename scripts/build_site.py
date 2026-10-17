"""Build a static latest/history site from the persisted archive, excluding private state."""
import argparse
from pathlib import Path
import shutil

from report_store import read_json, write_json, resolve_file, digest


def build(store, output, template=None):
    store, output = Path(store).resolve(), Path(output).resolve()
    if store == output or store in output.parents or output in store.parents:
        raise ValueError('Site output and report store must not overlap')
    index = read_json(store / 'index.json', {'reports': []})
    if output.exists():
        if any(output.iterdir()) and not (output / '.jsosif-site-build').is_file():
            raise ValueError('Refusing to replace a nonempty directory without the site-build marker')
        shutil.rmtree(output)
    output.mkdir(parents=True)
    template = template or Path(__file__).resolve().parents[1] / 'docs/index.html'
    shutil.copy2(template, output / 'index.html')
    for entry in index['reports']:
        for kind in ('md', 'json', 'pdf'):
            source = resolve_file(store, entry[kind])
            if digest(source) != entry['sha256'][kind]:
                raise ValueError('Report integrity check failed')
            target = output / entry[kind]
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
    # Delivery/quota state, member config and credentials never enter the site.
    write_json(output / 'index.json', index)
    (output / '.nojekyll').touch()
    (output / '.jsosif-site-build').touch()
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
