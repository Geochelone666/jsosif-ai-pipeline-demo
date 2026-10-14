#!/usr/bin/env python3
"""Prepare local drafts for Lucas's review without refreshing data or sending mail."""
import argparse
from datetime import date
from html import escape
import json
from pathlib import Path
import re
import shutil
from tempfile import TemporaryDirectory

if __package__:
    from . import email_delivery as email
    from . import snapshot_contract as contract
    from . import snapshot_freeze_check as freeze
else:
    import email_delivery as email
    import snapshot_contract as contract
    import snapshot_freeze_check as freeze

ROOT = Path(__file__).resolve().parents[1]
STYLE = 'body{font:16px sans-serif;max-width:1100px;margin:2em auto;padding:1em}table{border-collapse:collapse}td,th{border:1px solid #ccc;padding:.5em;text-align:left}pre{white-space:pre-wrap}'


def page(body):
    return f'<!doctype html><html><head><meta charset="utf-8"><title>Draft review</title><style>{STYLE}</style></head><body>{body}</body></html>\n'


def snapshot_payload(path):
    """Adapt legacy Markdown locally; existing frozen sidecars remain authoritative."""
    ticker, day, header, sections, metadata = email.load_snapshot(path)
    if path.with_suffix('.json').exists():
        return metadata
    def field(label):
        match = re.search(r'^- ' + re.escape(label) + r': (.+)$', header, re.M)
        return match.group(1) if match else 'N/A: missing from snapshot'
    quant = []
    for line in sections.get('QUANTITATIVE', '').splitlines():
        cells = [cell.strip() for cell in line.strip('|').split('|')]
        if (line.startswith('|') and len(cells) == 2 and cells[0] != 'Metric'
                and not re.fullmatch(r'[-: ]+', cells[0])):
            quant.append(dict(metric=cells[0], value=cells[1], availability='ok', reason=None))
    return {
        'contract_version': contract.CONTRACT_VERSION,
        'identity': dict(ticker=ticker, as_of=day, report_stamp=day.replace('-', '')),
        'quant': quant,
        'ai_summary': {'status': field('AI status'), 'sections': {
            key: sections.get(key, email.MISSING) for key in email.AI_SECTIONS}},
        'freshness': dict(report_as_of=day, market_data_as_of=field('Market data as_of'),
                          market_data_fetched_at=field('Market data fetched_at (UTC)'),
                          ai_snapshot_as_of=field('AI analysis snapshot as_of'),
                          snapshot_note=field('Snapshot note'), assumptions_version='N/A',
                          assumptions_checked={}, no_refresh_note=contract.NO_REFRESH_NOTE),
        'disclaimer': email.DISCLAIMER,
    }


def discover():
    latest = {}
    for path in sorted((ROOT / 'reports').glob('*-intelligence-*.*')):
        match = re.fullmatch(r'([A-Z0-9][A-Z0-9.-]*)-intelligence-(\d{8})\.(md|json)', path.name)
        if match:
            ticker, stamp, _ = match.groups()
            if ticker not in latest or stamp >= latest[ticker][0]:
                latest[ticker] = (stamp, path)
    return [(ticker, value[1]) for ticker, value in sorted(latest.items())]


def load_recipients(path):
    payload = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(payload, dict) or not isinstance(payload.get('recipients'), list):
        raise ValueError('Expected a recipients list in recipients JSON')
    addresses = payload['recipients']
    return email.validate_recipients(addresses) if addresses else []


def build(out, addresses, holdings):
    """Stage the whole bundle so write failures cannot publish an incomplete review."""
    if not holdings:
        raise ValueError('Zero holdings selected')
    out = out.absolute()
    if out.exists() and (not out.is_dir() or out.is_symlink()):
        raise ValueError('Output must be a directory, not a file or symlink')
    if out.exists() and any(out.iterdir()) and not (out / 'manifest.json').is_file():
        raise ValueError('Refusing to replace a directory without a review manifest')
    out.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(prefix='.review-', dir=out.parent) as temporary:
        stage = Path(temporary) / 'bundle'
        stage.mkdir()
        manifest, rows, blocked = [], [], []
        checklist = [
            '# Draft review checklist', f'Contract version: {contract.CONTRACT_VERSION}',
            'Sending is blocked until Lucas approves every draft individually and resolves both pending decisions.',
            '- [ ] Pending send-from account choice: ____________________',
            "- [ ] Pending recipient list approval (Joseph's email still pending): ____________________",
            'Each draft contains quant metrics, AI status, tailwinds, headwinds, catalysts, risks, assumptions / data freshness notes, and the not investment advice disclaimer.',
            'Missing recipients are shown as PENDING; no address is invented. No source data was refreshed.',
        ]
        for ticker, path in holdings:
            subject = f'JSOSIF snapshot | {path.stem[-8:-4]}-{path.stem[-4:-2]}-{path.stem[-2:]} {ticker}'
            errors, files = [], []
            status = 'BLOCKED'
            try:
                payload = snapshot_payload(path)
                errors.extend(contract.validate_snapshot(payload))
                if not freeze.determinism_check(snapshot_payload, path):
                    errors.append('Snapshot repeat-build drift detected')
                if not errors:
                    message = email.build_email([path], addresses, review_only=True)
                    def rendered():
                        repeated = email.build_email([path], addresses, review_only=True)
                        return [repeated['Subject'], repeated['To'],
                                repeated.get_body(preferencelist=('plain',)).get_content(),
                                repeated.get_body(preferencelist=('html',)).get_content()]
                    if not freeze.determinism_check(rendered):
                        errors.append('Email repeat-build drift detected')
                    else:
                        subject = str(message['Subject'])
                        label = f'Contract version: {contract.CONTRACT_VERSION}'
                        recipients_label = ', '.join(addresses) or 'PENDING — recipient list requires approval'
                        plain = message.get_body(preferencelist=('plain',)).get_content()
                        html = message.get_body(preferencelist=('html',)).get_content()
                        body = html.split('<body>', 1)[1].rsplit('</body>', 1)[0]
                        (stage / f'{ticker}.txt').write_text(f'{label}\nRecipients: {recipients_label}\n\n{plain}', encoding='utf-8')
                        (stage / f'{ticker}.html').write_text(page(f'<p>{escape(label)}</p><p>Recipients: {escape(recipients_label)}</p>{body}'), encoding='utf-8')
                        files = [f'{ticker}.txt', f'{ticker}.html']
                        status = 'PASS'
            except (ValueError, OSError, UnicodeError) as exc:
                errors.append(str(exc))
                for suffix in ('txt', 'html'):
                    (stage / f'{ticker}.{suffix}').unlink(missing_ok=True)
            manifest.append(dict(ticker=ticker, subject=subject, recipients=addresses,
                                 contract_version=contract.CONTRACT_VERSION,
                                 validation_errors=errors, freeze_check=status, files=files))
            if errors:
                reason = f'{ticker}: BLOCKED — ' + '; '.join(errors)
                blocked.append(f'<li>{escape(reason)}</li>')
                checklist.append(f'- {reason}')
            else:
                cells = [ticker, ', '.join(addresses) or 'PENDING', subject, contract.CONTRACT_VERSION, status]
                rows.append('<tr>' + ''.join(f'<td>{escape(cell)}</td>' for cell in cells)
                            + '<td>' + ' '.join(f'<a href="{name}">{name}</a>' for name in files) + '</td></tr>')
                checklist.append(f'- [ ] {ticker}: review both formats; confirm recipient list correctness, data freshness notes / retained source dates, missing evidence, and the "not investment advice" disclaimer. Approval / date: __________')
        (stage / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        (stage / 'index.html').write_text(page(
            '<h1>Draft review</h1><p>Sending is blocked until Lucas approves.</p>'
            '<table><tr><th>Ticker</th><th>Recipients</th><th>Subject</th><th>Contract version</th><th>Freeze check</th><th>Drafts</th></tr>'
            + ''.join(rows) + '</table><h2>Blocked drafts</h2><ul>' + ''.join(blocked) + '</ul>'), encoding='utf-8')
        (stage / 'REVIEW-CHECKLIST.md').write_text('\n\n'.join(checklist) + '\n', encoding='utf-8')
        backup = Path(temporary) / 'previous'
        if out.exists():
            out.rename(backup)
        try:
            stage.rename(out)
        except OSError:
            if backup.exists():
                backup.rename(out)
            raise
    if not any(not item['validation_errors'] for item in manifest):
        raise ValueError('Zero clean drafts; see manifest.json and REVIEW-CHECKLIST.md')
    return manifest


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--recipients', type=Path, default=ROOT / 'recipients.json')
    parser.add_argument('--out', type=Path, default=ROOT / 'review' / date.today().strftime('%Y%m%d'))
    args = parser.parse_args(argv)
    try:
        manifest = build(args.out, load_recipients(args.recipients), discover())
    except (ValueError, OSError, UnicodeError) as exc:
        parser.error(str(exc))
    print(f'Review bundle: {args.out} ({sum(not row["validation_errors"] for row in manifest)} clean drafts)')


if __name__ == '__main__':
    main()
