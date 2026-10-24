"""Build a static latest/history site from the persisted archive, excluding private state."""
import argparse
from datetime import datetime, timezone
from pathlib import Path
import shutil
from tempfile import TemporaryDirectory

from report_store import read_json, write_json, verified_report_files, report_advisory


def public_index(index):
    """Project archive metadata into the public schema; unknown fields stay private.

    Report files retain their verified bytes. This boundary applies to index
    metadata only, including nested report hashes and collection diagnostics.
    """
    def strings(source, fields):
        result = {}
        for key in fields:
            if key in source:
                value = source[key]
                if value is not None and not isinstance(value, str):
                    raise ValueError('Invalid public metadata field: ' + key)
                result[key] = value
        return result

    result = strings(index, ('last_complete_refresh', 'last_complete_business_date'))
    result['reports'] = []
    for entry in index['reports']:
        report = strings(entry, (
            'ticker', 'report_id', 'quality', 'as_of', 'generated_at', 'imported_at',
            'market_as_of', 'news_as_of', 'legacy_source_sha256', 'md', 'json', 'pdf'))
        report['sha256'] = strings(entry['sha256'], ('md', 'json', 'pdf'))
        result['reports'].append(report)
    if 'last_attempt' in index:
        source = index['last_attempt']
        attempt = strings(source, ('at', 'business_date', 'status', 'finished_at', 'last_progress_at'))
        for key in ('expected_tickers', 'successful_tickers', 'degraded_tickers',
                    'failed_tickers', 'pending_tickers', 'reused_tickers'):
            if key in source:
                if not isinstance(source[key], list) or not all(isinstance(t, str) for t in source[key]):
                    raise ValueError('Invalid public ticker list: ' + key)
                attempt[key] = list(source[key])
        result['last_attempt'] = attempt
    return result


def report_summary(snapshot):
    """Publish a small, source-derived overview without private delivery information."""
    metrics = {row['metric']: row['value'] for row in snapshot['quant']}
    return {'close': metrics.get('Close'), 'return_1d': metrics.get('Return 1D (%)'),
            'return_1y': metrics.get('Return 1Y (%)'),
            'ai_status': snapshot['ai_summary']['status']}


def health_summary(index):
    """Count verified current versions, rather than trusting progress counters.

    Failed is a run outcome and can overlap missing. Pending includes missing or
    degraded evidence, even when an interrupted writer omitted its recovery list.
    Publication is a local build timestamp, not proof of a successful deployment.
    """
    attempt = index.get('last_attempt', {})
    expected = set(attempt.get('expected_tickers', []))
    current = {}
    for entry in index['reports']:
        ticker = entry['ticker']
        if (ticker in expected and entry['as_of'] == attempt.get('business_date')
                and entry['quality'] != 'historical'):
            if ticker not in current or entry['generated_at'] > current[ticker]['generated_at']:
                current[ticker] = entry
    degraded = {ticker for ticker, entry in current.items()
                if entry['quality'] != 'ready' or entry.get('advisory')}
    missing = expected - current.keys()
    failed = expected & set(attempt.get('failed_tickers', []))
    pending = missing | degraded | failed | (expected & set(attempt.get('pending_tickers', [])))
    return {
        'version': index['publication']['version'],
        'published_at': index['publication']['published_at'],
        'business_date': attempt.get('business_date'),
        'status': attempt.get('status', 'historical_only'),
        'last_attempt_at': attempt.get('at'), 'finished_at': attempt.get('finished_at'),
        'expected': len(expected), 'updated': len(current),
        'ready': len(current) - len(degraded), 'degraded': len(degraded),
        'failed': len(failed), 'missing': len(missing), 'pending': len(pending),
    }


def build(store, output, template=None):
    if Path(output).is_symlink():
        raise ValueError('Site output must not be a symlink')
    store, output = Path(store).resolve(), Path(output).resolve()
    if store == output or store in output.parents or output in store.parents:
        raise ValueError('Site output and report store must not overlap')
    index = read_json(store / 'index.json')
    if not isinstance(index, dict) or not isinstance(index.get('reports'), list):
        raise ValueError('A valid persisted archive index is required before building the site')
    index = public_index(index)
    version_file = Path(__file__).resolve().parents[1] / 'VERSION'
    index['publication'] = {'published_at': datetime.now(timezone.utc).isoformat(),
                            'schedule': 'Daily at 19:00 America/Toronto; execution can be delayed',
                            'version': version_file.read_text().strip(), 'refresh_seconds': 60,
                            'data_type': 'Research snapshots; not a live market feed'}
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
        excel_template = Path(template).with_name('members.example.xlsx')
        if excel_template.is_file():
            shutil.copy2(excel_template, stage / 'members.example.xlsx')
        for entry in index['reports']:
            files = verified_report_files(store, entry)
            advisory = report_advisory(store, entry)
            if advisory:
                entry['advisory'] = advisory
            entry['summary'] = report_summary(read_json(files['json']))
            for kind in ('md', 'json', 'pdf'):
                source = files[kind]
                target = stage / entry[kind]
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
        # Delivery/quota state, member config and credentials never enter the site.
        write_json(stage / 'index.json', index)
        write_json(stage / 'health.json', health_summary(index))
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
