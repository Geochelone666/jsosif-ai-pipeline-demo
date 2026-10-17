"""Import existing Markdown as historical versions without refreshing or inventing data."""
import argparse
from datetime import datetime, timezone
from html import escape
import json
from pathlib import Path
import shutil
from tempfile import TemporaryDirectory

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

from build_review_bundle import snapshot_payload
from report_store import digest, read_json, write_json
from snapshot_contract import validate_snapshot


def historical_pdf(source, target, as_of):
    """Render the original text, never today's mutable data/ snapshots."""
    styles = getSampleStyleSheet()
    body = styles['BodyText'].clone('HistoryBody', fontSize=8, leading=11,
                                    wordWrap='CJK', spaceAfter=3)
    story = [Paragraph('Historical report', styles['Title']),
             Paragraph(f'Original report date: {escape(as_of)}. Imported from saved Markdown; '
                       'no source data was refreshed. The original Markdown is preserved alongside this PDF.', body),
             Spacer(1, 12)]
    for line in source.read_text(encoding='utf-8').splitlines():
        if line.startswith('#'):
            story.append(Paragraph(escape(line.lstrip('#').strip()), styles['Heading2']))
        else:
            story.append(Paragraph(escape(line) or '&#160;', body))
    SimpleDocTemplate(str(target), pagesize=A4, title='Historical report ' + as_of,
                      author='JSOSIF').build(story)


def import_history(reports, store, *, now=None):
    reports, store = Path(reports), Path(store)
    now = now or datetime.now(timezone.utc)
    index = read_json(store / 'index.json', {'reports': []})
    known = {entry['report_id'] for entry in index['reports']}
    archived_sources = {entry.get('sha256', {}).get('md') for entry in index['reports']}
    imported = skipped = 0
    for source in sorted(reports.glob('*-intelligence-????????.md')):
        payload = snapshot_payload(source, from_markdown=True)
        errors = validate_snapshot(payload)
        if errors:
            raise ValueError('Historical report is invalid: ' + source.name)
        ticker = payload['identity']['ticker']
        source_hash = digest(source)
        report_id = f'legacy-{source_hash}/{ticker}'
        if report_id in known or source_hash in archived_sources:
            skipped += 1
            continue
        relative = Path('archive') / report_id
        destination = store / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists():
            raise ValueError('An unindexed historical directory requires reconciliation')
        payload.update(ticker=ticker, as_of=payload['identity']['as_of'], quality='historical',
                       source_status={'market': 'historical', 'news': 'historical'},
                       imported_at=now.isoformat(), legacy_source_sha256=source_hash)
        entry = dict(report_id=report_id, ticker=ticker, as_of=payload['identity']['as_of'],
                     generated_at=now.isoformat(), imported_at=now.isoformat(),
                     quality='historical', legacy_source_sha256=source_hash,
                     market_as_of=payload['freshness']['market_data_as_of'],
                     news_as_of=payload['freshness']['ai_snapshot_as_of'], sha256={})
        with TemporaryDirectory(prefix='.history-', dir=destination.parent) as temporary:
            stage = Path(temporary) / 'report'
            stage.mkdir()
            md = stage / source.name
            shutil.copy2(source, md)
            write_json(md.with_suffix('.json'), payload)
            historical_pdf(source, md.with_suffix('.pdf'), entry['as_of'])
            if source.with_suffix('.json').is_file():
                shutil.copy2(source.with_suffix('.json'), stage / 'original-metadata.json')
            for kind in ('md', 'json', 'pdf'):
                target = md.with_suffix('.' + kind)
                entry[kind] = (relative / target.name).as_posix()
                entry['sha256'][kind] = digest(target)
            stage.rename(destination)
        index['reports'].append(entry)
        try:
            write_json(store / 'index.json', index)
        except Exception:
            shutil.rmtree(destination)
            raise
        known.add(report_id)
        archived_sources.add(source_hash)
        imported += 1
    return {'imported': imported, 'already_archived': skipped}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reports', type=Path, default=Path(__file__).resolve().parents[1] / 'reports')
    parser.add_argument('--store', type=Path, required=True)
    args = parser.parse_args()
    print(import_history(args.reports, args.store))


if __name__ == '__main__':
    main()
