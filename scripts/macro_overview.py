"""Build and verify a standalone retrospective macro overview draft."""
import argparse
import hashlib
from io import BytesIO
import json
from pathlib import Path
import re

from pypdf import PdfReader
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Spacer, PageBreak
from reportlab.pdfgen.canvas import Canvas

from report_store import resolve_file
from research_workspace import FRED_UNITS
from sector_brief_pdf import para, table, TEAL, MUTED
from shared_research_pack import build, digest, exact_date, validate_pack
from universe import SUPPORTED

UNITS = {'macro:fred:' + k: v for k, v in FRED_UNITS.items()} | {'macro:boc:FXUSDCAD': 'CAD per USD'}
LIMITATIONS = [
    'Retrospective archive reconstruction. The cutoff is not a live refresh or a publication timestamp.',
    'Publication times and historical vintages are unavailable; no point-in-time backtest eligibility.',
    'Different series have different observation dates. No interpolation, forecast, causal claim or FX conversion is made.',
    'A newer missing observation is not replaced with an older available value. Latest-date conflicts stay unavailable.',
    'Source hashes check archive/capture consistency, not provider signatures or investment suitability.',
    'Draft evidence only; delivery readiness is false. For analyst preparation, not investment advice.',
]
HEADINGS = ('Macro observation snapshot', 'Provenance and missing evidence')


def summarize(observations, as_of):
    result = []
    for subject, unit in sorted(UNITS.items()):
        rows = [r for r in observations if r['subject'] == subject]
        history = []
        for day in sorted({r['observed_on'] for r in rows if r['observed_on']}):
            same_day = [r for r in rows if r['observed_on'] == day]
            values = {r['value'] for r in same_day if r['status'] == 'observed'}
            missing = sum(r['status'] != 'observed' for r in same_day)
            status = ('conflicting' if len(values) > 1 else 'missing' if not values else
                      'incomplete' if missing else 'observed')
            history.append({'observed_on': day, 'status': status,
                            'value': next(iter(values)) if status == 'observed' else None,
                            'observation_ids': sorted(r['id'] for r in same_day), 'missing_records': missing})
        latest = history[-1] if history else {'observed_on': None, 'status': 'missing', 'value': None}
        result.append({'subject': subject, 'unit': unit, 'status': latest['status'], 'value': latest['value'],
                       'observed_on': latest['observed_on'],
                       'age_days': (exact_date(as_of) - exact_date(latest['observed_on'])).days if latest['observed_on'] else None,
                       'history': history, 'undated_observation_ids': sorted(r['id'] for r in rows if not r['observed_on']),
                       'source_ids': sorted({r['source_id'] for r in rows if r['source_id']})})
    return result


def assemble(pack):
    validate_pack(pack)
    observations = sorted((r for r in pack['observations'] if r['subject'] in UNITS), key=lambda r:r['id'])
    used = {key for r in observations for key in (r['source_id'], r['currency_source_id']) if key}
    sources = {r['id']: r for r in pack['sources']}
    payload = {'schema_version': 1, 'kind': 'macro_overview', 'dataset_id': pack['dataset_id'], 'as_of': pack['as_of'],
               'status': 'draft_incomplete_evidence', 'delivery_ready': False, 'temporal_scope': pack['temporal_scope'],
               'series': summarize(observations, pack['as_of']), 'observations': observations,
               'sources': [sources[k] for k in sorted(used)],
               'report_versions': {r['ticker']: {'report_id': r['report_id'], 'as_of': r['as_of'],
                   'snapshot_sha256': sources[r['snapshot_source_id']]['sha256']} for r in sorted(pack['reports'], key=lambda r:r['ticker'])},
               'limitations': LIMITATIONS}
    return validate_overview({'overview_id': digest(payload), **payload})


def validate_overview(value):
    keys = {'overview_id', 'schema_version', 'kind', 'dataset_id', 'as_of', 'status', 'delivery_ready',
            'temporal_scope', 'series', 'observations', 'sources', 'report_versions', 'limitations'}
    if (not isinstance(value, dict) or set(value) != keys or type(value['schema_version']) is not int or
            value['schema_version'] != 1 or value['kind'] != 'macro_overview' or
            value['overview_id'] != digest({k:v for k,v in value.items() if k != 'overview_id'}) or
            value['status'] != 'draft_incomplete_evidence' or value['delivery_ready'] is not False or
            not isinstance(value['dataset_id'], str) or not re.fullmatch('[0-9a-f]{64}', value['dataset_id']) or
            value['limitations'] != LIMITATIONS):
        raise ValueError('Invalid macro overview identity or draft contract')
    # Reuse the versioned evidence contract on the macro-only projection. Report
    # lineage below is separate: it references stock snapshots, not macro sources.
    subset = {'schema_version': 1, 'as_of': value['as_of'], 'temporal_scope': value['temporal_scope'],
              'sectors': [], 'reports': [], 'relationships': [], 'limitations': value['limitations'],
              'entities': [{'id': k, 'kind': 'macro'} for k in sorted(UNITS)],
              'sources': value['sources'], 'observations': value['observations'],
              'additional_macro_observations': [r['id'] for r in value['observations']]}
    validate_pack({'dataset_id': digest(subset), **subset})
    if any(r['subject'] not in UNITS or r['unit'] != UNITS[r['subject']] for r in value['observations']):
        raise ValueError('Unexpected macro series or unit')
    if any(s['kind'] not in ('fred', 'boc') for s in value['sources']):
        raise ValueError('Unexpected macro source')
    if value['series'] != summarize(value['observations'], value['as_of']):
        raise ValueError('Macro summary disagrees with retained evidence')
    if not isinstance(value['report_versions'], dict):
        raise ValueError('Invalid report lineage')
    for ticker, row in value['report_versions'].items():
        if (ticker not in SUPPORTED or set(row) != {'report_id', 'as_of', 'snapshot_sha256'} or
                not isinstance(row['report_id'], str) or not row['report_id'] or
                not isinstance(row['snapshot_sha256'], str) or not re.fullmatch('[0-9a-f]{64}', row['snapshot_sha256']) or
                exact_date(row['as_of']) > exact_date(value['as_of'])):
            raise ValueError('Invalid report lineage')
    return value


def number(value):
    if value is None:
        return 'N/A'
    return f'{value:.6g}'  # Preserve small nonzero observations instead of rounding to zero.


def render(value):
    output = BytesIO()
    def header(title):
        return [para('JSOSIF / MACRO OVERVIEW', size=10, bold=True, color=TEAL),
                para(title, size=21, bold=True),
                para('Cutoff ' + value['as_of'] + ' | Draft - incomplete evidence', size=10, color=MUTED)]
    def footer(canvas, doc):
        canvas.saveState(); canvas.setStrokeColor(TEAL); canvas.line(44, 39, A4[0]-44, 39)
        canvas.setFont('Helvetica', 8); canvas.setFillColor(MUTED)
        canvas.drawString(44, 26, 'JSOSIF | Retrospective draft | Not investment advice')
        canvas.drawRightString(A4[0]-44, 26, f'{doc.page} / 2'); canvas.restoreState()
    story = header(HEADINGS[0])
    story += [para('Five configured macro series, with their actual observation dates. A date shown here is not a '
                   'publication time. Source age is measured against the cutoff; no live refresh is performed.'),
              table(['Series', 'Value', 'Unit', 'Observed on', 'Age / days', 'Status'],
                    [[r['subject'].removeprefix('macro:'), number(r['value']), r['unit'], r['observed_on'] or 'unknown',
                      r['age_days'] if r['age_days'] is not None else '-', r['status']] for r in value['series']],
                    [.20, .12, .23, .18, .10, .17]), Spacer(1, 16),
              para('Captured USD/CAD observations', size=13, bold=True)]
    boc = next(r for r in value['series'] if r['subject'] == 'macro:boc:FXUSDCAD')
    rows = [[r['observed_on'], number(r['value']), r['status']] for r in boc['history'][-5:]]
    story += [para('Up to five latest dated observations present in the capture; unit: CAD per USD. '
                   'Missing dates are not interpolated. This is a data snapshot, not a trend or currency forecast.'),
              table(['Observation date', 'CAD per USD', 'Status'], rows or [['Unavailable', 'N/A', 'missing']], [.35, .3, .35]),
              Spacer(1, 12), para('Evidence interpretation', size=13, bold=True),
              para('Observed means the retained value has a unit, date and source. Missing means no usable value. '
                   'Incomplete means available and missing records coexist at that date. Conflicting means '
                   'different available values coexist; no preferred source is silently selected.'),
              para('The latest dated record determines the snapshot, including when that record is missing. '
                   'All dated history, missing records and source identities remain in the companion JSON.'), PageBreak()]
    story += header(HEADINGS[1])
    story += [para(f"Lineage: {len(value['report_versions'])} archived stock versions, {len(value['observations'])} unique macro evidence records, "
                   f"{len(value['sources'])} source versions. Repeated references do not create additional observations."),
              table(['Series', 'Dated observations', 'Source versions', 'Retrieval evidence'],
                    [[r['subject'].removeprefix('macro:'), len(r['history']), len(r['source_ids']),
                      'Capture timestamp in JSON' if r['subject'].startswith('macro:boc:') and r['source_ids'] else
                      'Unavailable in archive'] for r in value['series']], [.26, .20, .20, .34]),
              Spacer(1, 14), para('Source ledger', size=13, bold=True)]
    source_rows = []
    for kind in ('fred', 'boc'):
        rows = [r for r in value['sources'] if r['kind'] == kind]
        source_rows.append([kind.upper(), len(rows), ', '.join(r['sha256'][:12] for r in rows[:3]) or 'Unavailable'])
    story += [table(['Provider', 'Source versions', 'SHA-256 prefixes (up to three)'], source_rows, [.22, .20, .58]),
              para('Full hashes, integrity labels, public attribution URLs and evidence references are retained in '
                   'macro-overview-' + value['as_of'] + '.json. A checksum is not a provider signature.', size=8),
              para('Public attribution: https://fred.stlouisfed.org/ ; https://www.bankofcanada.ca/valet/docs', size=8),
              para('Risks and missing evidence', size=13, bold=True)]
    story += [para(item, size=9) for item in value['limitations']]
    story += [para('Dataset SHA-256: ' + value['dataset_id'], size=7),
              para('Overview SHA-256: ' + value['overview_id'], size=7)]
    doc = SimpleDocTemplate(output, pagesize=A4, leftMargin=44, rightMargin=44, topMargin=36,
                            bottomMargin=54, title='JSOSIF Macro Overview - ' + value['as_of'], author='JSOSIF')
    doc.build(story, onFirstPage=footer, onLaterPages=footer,
              canvasmaker=lambda *a, **kw: Canvas(*a, **{**kw, 'invariant': 1}))
    return output.getvalue()


def inspect_pdf(raw, value):
    reader = PdfReader(BytesIO(raw))
    if reader.is_encrypted or len(reader.pages) != 2:
        raise ValueError('Macro overview must fit its two-page layout')
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ''
        if (HEADINGS[i] not in text or 'Draft - incomplete evidence' not in text or
                value['as_of'] not in text or f'{i+1} / 2' not in text):
            raise ValueError('Missing macro identity or draft label')
    first = reader.pages[0].extract_text()
    if any(subject.removeprefix('macro:') not in first for subject in UNITS):
        raise ValueError('Missing macro series')
    return {'pages': 2, 'bytes': len(raw), 'visual_review_required': True}


def write_bundle(value, output):
    validate_overview(value)
    raw_pdf = render(value); validation = inspect_pdf(raw_pdf, value)
    stem = 'macro-overview-' + value['as_of']
    raw_json = (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n').encode()
    manifest = {'schema_version': 1, 'kind': 'macro_overview', 'status': value['status'], 'delivery_ready': False,
                'overview_id': value['overview_id'], 'dataset_id': value['dataset_id'], 'as_of': value['as_of'],
                'pdf': stem + '.pdf', 'json': stem + '.json', 'validation': validation,
                'sha256': {'pdf': hashlib.sha256(raw_pdf).hexdigest(), 'json': hashlib.sha256(raw_json).hexdigest()}}
    output = Path(output); output.mkdir(parents=False, exist_ok=False)
    for name, raw in ((manifest['pdf'], raw_pdf), (manifest['json'], raw_json),
                      ('manifest.json', (json.dumps(manifest, indent=2) + '\n').encode())):
        with (output / name).open('xb') as stream:
            stream.write(raw)
    return manifest


def load_bundle(root):
    if root is None:
        return None
    def read(name, limit):
        with resolve_file(root, name).open('rb') as stream:
            raw = stream.read(limit + 1)
        if len(raw) > limit:
            raise ValueError('Macro artifact exceeds size limit')
        return raw
    manifest = json.loads(read('manifest.json', 2 * 1024 * 1024))
    if (type(manifest.get('schema_version')) is not int or manifest['schema_version'] != 1 or
            manifest.get('kind') != 'macro_overview' or manifest.get('status') != 'draft_incomplete_evidence' or
            manifest.get('delivery_ready') is not False):
        raise ValueError('Invalid macro draft manifest')
    exact_date(manifest['as_of']); loaded = {}
    for kind, limit in (('json', 2 * 1024 * 1024), ('pdf', 20 * 1024 * 1024)):
        if manifest[kind] != 'macro-overview-' + manifest['as_of'] + '.' + kind:
            raise ValueError('Invalid macro artifact filename')
        raw = read(manifest[kind], limit)
        if hashlib.sha256(raw).hexdigest() != manifest['sha256'][kind]:
            raise ValueError('Macro artifact checksum mismatch')
        loaded[kind] = raw
    value = validate_overview(json.loads(loaded['json']))
    if any(value[k] != manifest[k] for k in ('overview_id', 'dataset_id', 'as_of', 'status', 'delivery_ready')):
        raise ValueError('Macro companion and manifest disagree')
    inspect_pdf(loaded['pdf'], value)
    return {'overview_id': value['overview_id'], 'as_of': value['as_of'], 'report_versions': value['report_versions'],
            'filename': manifest['pdf'], 'sha256': manifest['sha256']['pdf'], 'bytes': loaded['pdf']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--store', type=Path, required=True); parser.add_argument('--as-of', required=True)
    parser.add_argument('--boc-capture', type=Path); parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.output.resolve().is_relative_to(args.store.resolve()):
            raise ValueError('Output must not alter the archive')
        write_bundle(assemble(build(args.store, as_of=args.as_of, boc_capture=args.boc_capture)), args.output)
    except (ValueError, OSError, TypeError, KeyError, AttributeError):
        parser.error('Macro build failed; verify inputs and use a new output directory')
    print('Built one standalone macro draft; no refresh or production activation')


if __name__ == '__main__':
    main()
