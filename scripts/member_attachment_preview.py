"""Prepare private member attachment reviews without SMTP, network or ledger writes."""
import argparse
from datetime import datetime, timedelta
from email import policy
from email.message import EmailMessage
from email.utils import format_datetime
import hashlib
import json
import os
from pathlib import Path
from zoneinfo import ZoneInfo

from deliver_weekly import due_period, eligible_report
from report_store import resolve_file, verified_report_files, report_advisory
from shared_research_pack import ROOT, digest, exact_date, teams
from subscriptions import validate, tickers_for

MAX_MESSAGE_BYTES = 20 * 1024 * 1024
MAX_JSON_BYTES = 2 * 1024 * 1024
MAX_INDEX_BYTES = 32 * 1024 * 1024
CONTENT_FIELDS = {'sector_brief', 'macro_overview', 'news_catalysts'}


def read_bytes(path, limit):
    with Path(path).open('rb') as stream:
        raw = stream.read(limit + 1)
    if len(raw) > limit:
        raise ValueError('Review input exceeds size limit')
    return raw


def read_object(path, *, limit=MAX_JSON_BYTES):
    value = json.loads(read_bytes(path, limit))
    if not isinstance(value, dict):
        raise ValueError('Expected a JSON object')
    return value


def checksum(raw):
    return hashlib.sha256(raw).hexdigest()


def load_briefs(root):
    """Verify the completed draft bundle, preserving bytes for later MIME assembly.

    Checksums prove local bundle consistency, not publisher authorization. No
    accepted/live state is inferred from a manifest or the PDF's historical label.
    """
    if root is None:
        return {}
    root = Path(root)
    manifest = read_object(root / 'manifest.json')
    if (type(manifest.get('schema_version')) is not int or manifest['schema_version'] != 1
            or manifest.get('status') != 'draft_incomplete_evidence'
            or manifest.get('delivery_ready') is not False
            or not isinstance(manifest.get('briefs'), list) or len(manifest['briefs']) != 8):
        raise ValueError('Expected a completed eight-sector draft bundle')
    exact_date(manifest['as_of'])
    configured = {t['id']: t for t in teams(ROOT / 'config/research_teams.json')}
    result = {}
    for entry in manifest['briefs']:
        identity = entry['sector_id']
        if identity not in configured or identity in result:
            raise ValueError('Unknown or duplicate sector identity')
        loaded = {}
        for kind, limit in (('json', MAX_JSON_BYTES), ('pdf', MAX_MESSAGE_BYTES)):
            name = entry[kind]
            expected = identity.removeprefix('sector:') + '-' + manifest['as_of'] + '.' + kind
            if name != expected:
                raise ValueError('Sector filename does not match bundle identity')
            path = resolve_file(root, name)
            raw = read_bytes(path, limit)
            if checksum(raw) != entry['sha256'][kind]:
                raise ValueError('Sector artifact checksum mismatch')
            loaded[kind] = raw
        brief = json.loads(loaded['json'])
        if (brief['brief_id'] != entry['brief_id'] or
                brief['brief_id'] != digest({k:v for k,v in brief.items() if k != 'brief_id'}) or
                brief['dataset_id'] != manifest['dataset_id'] or brief['sector_id'] != identity or
                brief['as_of'] != manifest['as_of'] or brief['status'] != 'draft_incomplete_evidence' or
                brief['delivery_ready'] is not False or brief['name'] != configured[identity]['name']):
            raise ValueError('Sector companion and manifest disagree')
        stocks = [s['ticker'] for s in brief['stocks']]
        if sorted(stocks) != configured[identity]['tickers']:
            raise ValueError('Sector coverage differs from the configured taxonomy')
        # Inspect the captured PDF bytes, not a second unverified file read.
        inspect_captured_pdf(loaded['pdf'], brief)
        result[identity] = {'brief_id': brief['brief_id'], 'name': brief['name'],
                            'as_of': brief['as_of'], 'tickers': stocks,
                            'report_versions': {s['ticker']: s['report_id'] for s in brief['stocks']},
                            'filename': entry['pdf'], 'sha256': entry['sha256']['pdf'],
                            'bytes': loaded['pdf']}
    return result


def inspect_captured_pdf(raw, brief):
    # The existing inspector supports paths; its semantic checks are repeated on
    # the retained bytes here so a changed path cannot alter the reviewed message.
    from io import BytesIO
    from pypdf import PdfReader
    from sector_brief_pdf import PAGE_TITLES
    reader = PdfReader(BytesIO(raw))
    if reader.is_encrypted or len(reader.pages) != 4:
        raise ValueError('Invalid sector PDF structure')
    pages = [p.extract_text() or '' for p in reader.pages]
    for i, page in enumerate(pages):
        if PAGE_TITLES[i] not in page or 'Draft - incomplete evidence' not in page or f'{i+1} / 4' not in page:
            raise ValueError('Invalid sector PDF draft labels')
    if any(s['ticker'] not in pages[0] or s['ticker'] not in pages[2] for s in brief['stocks']):
        raise ValueError('Sector PDF is missing covered stocks')


def validate_review_config(config):
    validate(config)
    for member in config['members']:
        content = member.get('content_preferences', {})
        if (not isinstance(content, dict) or set(content) - CONTENT_FIELDS
                or any(type(v) is not bool for v in content.values())):
            raise ValueError('Content preferences must use known boolean fields')
    return config


def encode_message(member, attachments, gaps, now, plan_id):
    message = EmailMessage(policy=policy.SMTP)
    message['Subject'] = '[REVIEW ONLY - DO NOT SEND] JSOSIF attachment selection'
    message['To'] = member['email']
    message['Date'] = format_datetime(now)
    message['Message-ID'] = '<' + plan_id + '@preview.invalid>'
    lines = ['Private offline review for ' + member['name'] + '.', '',
             'This preview is not approved for delivery. No mail was sent or reserved.',
             'No current subscription authority or delivery ledger was consulted.', '', 'Selected attachments:']
    lines += ['- ' + a['filename'] + ' | ' + a['kind'] + ' | as of ' + a['as_of'] for a in attachments]
    if any(a['kind'] == 'sector_draft' for a in attachments):
        lines += ['', 'Sector PDFs are incomplete retrospective drafts. Their macro context is part of the',
                  'sector document, not a separately requested macro overview. No benchmark/KPI/event readiness is implied.']
    if any(a['kind'] == 'macro_draft' for a in attachments):
        lines += ['', 'The standalone macro overview is a retrospective draft with explicit observation dates.',
                  'It is not a live refresh, forecast or point-in-time backtest dataset.']
    if gaps:
        lines += ['', 'Requested content not included:'] + ['- ' + g for g in gaps]
    lines += ['', 'Do not send this file. Rebuild through an authorized delivery flow after live acceptance.']
    message.set_content('\n'.join(lines))
    for attachment in attachments:
        message.add_attachment(attachment['bytes'], maintype='application', subtype='pdf', filename=attachment['filename'])
    message.set_boundary('jsosif-' + plan_id[:56])  # RFC 2046 boundary length <= 70.
    return message.as_bytes()


def prepare(config, store, *, now, sector_bundle=None, include_sector_drafts=False,
            macro_bundle=None, include_macro_drafts=False, preview_all=False, max_bytes=MAX_MESSAGE_BYTES):
    validate_review_config(config)
    if now.utcoffset() is None:
        raise ValueError('Review time must include a timezone')
    if type(max_bytes) is not int or not 1 <= max_bytes <= MAX_MESSAGE_BYTES:
        raise ValueError('Message budget must not exceed 20 MiB')
    if any(type(flag) is not bool for flag in (include_sector_drafts, include_macro_drafts, preview_all)):
        raise ValueError('Review options must be booleans')
    briefs = load_briefs(sector_bundle)
    from macro_overview import load_bundle
    macro = load_bundle(macro_bundle)
    mapping = {ticker: row['id'] for row in teams(ROOT / 'config/research_teams.json') for ticker in row['tickers']}
    index = read_object(Path(store) / 'index.json', limit=MAX_INDEX_BYTES)
    if not isinstance(index.get('reports'), list):
        raise ValueError('Report index required')
    report_ids = [r.get('report_id') for r in index['reports'] if isinstance(r, dict) and isinstance(r.get('report_id'), str)]
    if len(report_ids) != len(set(report_ids)):
        raise ValueError('Ambiguous duplicate report identity')
    plans = []
    messages = {}
    for member in sorted(config['members'], key=lambda m: m['id']):
        local = now.astimezone(ZoneInfo(member['timezone']))
        period = (local.date() - timedelta(days=local.weekday())).isoformat()
        key = digest({'member_id': member['id'], 'period': period})
        plan = {'member_key': key, 'period': period, 'status': 'skipped', 'reason': None,
                'attachments': [], 'gaps': [], 'delivery_ready': False, 'schedule_bypassed': preview_all,
                'encoded_bytes': None, 'max_bytes': max_bytes, 'eml': None}
        plans.append(plan)
        if not member['enabled']:
            plan['reason'] = 'paused'; continue
        if not preview_all and due_period(member, now) is None:
            plan['reason'] = 'not_due'; continue
        attachments = []
        selected = {}
        for ticker in tickers_for(config, member):
            candidates = [r for r in index['reports'] if eligible_report(r, ticker, config, now)
                          and not r.get('advisory') and not report_advisory(store, r)]
            if not candidates:
                plan.update(status='deferred_reports', reason='missing_or_ineligible_report')
                break
            entry = max(candidates, key=lambda r: (datetime.fromisoformat(r['generated_at']), r['report_id']))
            files = verified_report_files(store, entry)
            raw = read_bytes(files['pdf'], MAX_MESSAGE_BYTES)
            if checksum(raw) != entry['sha256']['pdf']:
                raise ValueError('Report PDF changed after archive verification')
            selected[ticker] = entry
            attachments.append({'kind': 'stock_report', 'id': entry['report_id'], 'as_of': entry['as_of'],
                                'filename': files['pdf'].name, 'sha256': checksum(raw), 'bytes': raw})
        if plan['status'] == 'deferred_reports':
            continue  # No silently partial stock digest.
        content = member.get('content_preferences', {})
        gaps = plan['gaps']
        if content.get('macro_overview') is True:
            if macro is None:
                gaps.append('macro_overview: standalone artifact unavailable')
            else:
                age = (now.astimezone(ZoneInfo('America/Toronto')).date() - exact_date(macro['as_of'])).days
                matching = all(macro['report_versions'].get(t) == {
                    'report_id': r['report_id'], 'as_of': r['as_of'], 'snapshot_sha256': r['sha256']['json']}
                    for t, r in selected.items())
                if not 0 <= age <= config.get('max_report_age_days', 4):
                    gaps.append('macro_overview: stale or future draft')
                elif not matching:
                    gaps.append('macro_overview: stock snapshot lineage mismatch')
                elif not include_macro_drafts:
                    gaps.append('macro_overview: draft review not enabled')
                else:
                    attachments.append({'kind': 'macro_draft', 'id': macro['overview_id'], 'as_of': macro['as_of'],
                                        'filename': macro['filename'], 'sha256': macro['sha256'], 'bytes': macro['bytes']})
        if content.get('news_catalysts') is True:
            gaps.append('news_catalysts: standalone artifact unavailable')
        if content.get('sector_brief') is True:
            for sector_id in sorted({mapping[t] for t in selected}):
                brief = briefs.get(sector_id)
                if brief is None:
                    gaps.append(sector_id + ': bundle unavailable'); continue
                age = (now.astimezone(ZoneInfo('America/Toronto')).date() - exact_date(brief['as_of'])).days
                if not 0 <= age <= config.get('max_report_age_days', 4):
                    gaps.append(sector_id + ': stale or future draft'); continue
                if any(brief['report_versions'].get(t) != r['report_id'] for t, r in selected.items() if mapping[t] == sector_id):
                    gaps.append(sector_id + ': stock report version mismatch'); continue
                if not include_sector_drafts:
                    gaps.append(sector_id + ': draft review not enabled'); continue
                attachments.append({'kind': 'sector_draft', 'id': brief['brief_id'], 'as_of': brief['as_of'],
                                    'filename': brief['filename'], 'sha256': brief['sha256'], 'bytes': brief['bytes']})
        # Content duplicates are represented once, even if distinct logical references
        # happen to carry identical PDF bytes. Retain their logical identities for review.
        unique = {}
        for attachment in attachments:
            sha = attachment['sha256']
            if sha not in unique:
                unique[sha] = dict(attachment, identities=[])
            unique[sha]['identities'].append({'kind': attachment['kind'], 'id': attachment['id']})
        attachments = list(unique.values())
        plan['attachments'] = [{k:v for k,v in a.items() if k != 'bytes'} for a in attachments]
        plan_id = digest({'config': config, 'member_key': key, 'at': now.isoformat(),
                          'attachments': plan['attachments'], 'gaps': gaps})
        encoded = encode_message(member, attachments, gaps, now, plan_id)
        plan['encoded_bytes'] = len(encoded)
        if len(encoded) > max_bytes:
            plan.update(status='deferred_size', reason='encoded_message_exceeds_budget')
            # Never replace a private attachment with an invented or public link.
            plan['link_fallback'] = 'unavailable_requires_approved_access_control'
            continue
        plan.update(status='prepared_with_gaps' if gaps else 'prepared', eml=key + '.eml')
        plan['eml_sha256'] = checksum(encoded)
        messages[plan['eml']] = encoded
    return {'schema_version': 1, 'mode': 'private_offline_review', 'at': now.isoformat(),
            'delivery_ready': False, 'ledger_consulted': False, 'members': plans}, messages


def write_private(output, review, messages, *, forbidden_roots):
    output = Path(output)
    if any(output.resolve().is_relative_to(Path(root).resolve()) for root in forbidden_roots if root):
        raise ValueError('Private preview must be outside all input stores')
    output.mkdir(mode=0o700, parents=False, exist_ok=False)
    for name, raw in [*sorted(messages.items()), ('review.json', (json.dumps(review, indent=2) + '\n').encode())]:
        if Path(name).name != name or '/' in name or '\\' in name:
            raise ValueError('Invalid private output filename')
        fd = os.open(output / name, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, 'wb') as stream:
            stream.write(raw)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--store', type=Path, required=True)
    parser.add_argument('--sector-bundle', type=Path)
    parser.add_argument('--macro-bundle', type=Path)
    parser.add_argument('--at', required=True, help='Explicit timezone-aware review timestamp')
    parser.add_argument('--include-sector-drafts', action='store_true')
    parser.add_argument('--include-macro-drafts', action='store_true')
    parser.add_argument('--preview-all', action='store_true', help='Ignore schedule/start date, never pause')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        review, messages = prepare(read_object(args.config), args.store,
            now=datetime.fromisoformat(args.at.replace('Z', '+00:00')), sector_bundle=args.sector_bundle,
            include_sector_drafts=args.include_sector_drafts, macro_bundle=args.macro_bundle,
            include_macro_drafts=args.include_macro_drafts, preview_all=args.preview_all)
        write_private(args.output, review, messages, forbidden_roots=[args.store, args.sector_bundle, args.macro_bundle, ROOT])
    except (ValueError, OSError, KeyError, TypeError, AttributeError):
        parser.error('Private review failed; check input integrity, preferences and a new output directory')
    print('Private attachment review completed; no send or ledger operation performed')


if __name__ == '__main__':
    main()
