#!/usr/bin/env python3
"""Prepare local drafts for Lucas's review without refreshing data or sending mail."""
import argparse
from datetime import date
from html import escape
import json
from pathlib import Path
import re
from tempfile import TemporaryDirectory

if __package__:
    from . import recipients as teams
    from . import email_delivery as email
    from . import snapshot_contract as contract
    from . import snapshot_freeze_check as freeze
else:
    import recipients as teams
    import email_delivery as email
    import snapshot_contract as contract
    import snapshot_freeze_check as freeze

ROOT = Path(__file__).resolve().parents[1]
STYLE = 'body{font:16px sans-serif;max-width:1100px;margin:2em auto;padding:1em}table{border-collapse:collapse}td,th{border:1px solid #ccc;padding:.5em;text-align:left}pre{white-space:pre-wrap}'


def page(body):
    return f'<!doctype html><html><head><meta charset="utf-8"><title>Draft review</title><style>{STYLE}</style></head><body>{body}</body></html>\n'


def snapshot_payload(path, *, from_markdown=False):
    """Adapt legacy Markdown locally; existing frozen sidecars remain authoritative."""
    ticker, day, header, sections, metadata = email.load_snapshot(path)
    if path.with_suffix('.json').exists() and not from_markdown:
        return metadata
    def field(label):
        match = re.search(r'^- ' + re.escape(label) + r': (.+)$', header, re.M)
        return match.group(1).replace('**', '') if match else 'N/A: missing from snapshot'
    quant = []
    for line in sections.get('QUANTITATIVE', '').splitlines():
        cells = [cell.strip() for cell in line.strip('|').split('|')]
        if (line.startswith('|') and len(cells) == 2 and cells[0] != 'Metric'
                and not re.fullmatch(r'[-: ]+', cells[0])):
            missing = cells[1] in ('N/A', 'Unavailable')
            quant.append(dict(metric=cells[0], value=None if missing else cells[1],
                              availability='missing' if missing else 'ok',
                              reason='N/A: source data unavailable' if missing else None))
    return {
        'contract_version': contract.CONTRACT_VERSION,
        'identity': dict(ticker=ticker, as_of=day, report_stamp=day.replace('-', '')),
        'quant': quant,
        'ai_summary': {'status': field('AI status'), 'sections': {
            key: sections.get(key, email.MISSING) for key in email.AI_SECTIONS}},
        'freshness': dict(report_as_of=day, market_data_as_of=field('Market data as_of'),
                          market_data_fetched_at=field('Market data fetched_at (UTC)'),
                          ai_snapshot_as_of=field('AI analysis snapshot as_of'),
                          snapshot_note=field('Snapshot note'),
                          assumptions_version=str(metadata.get('assumptions_version', 'N/A')),
                          assumptions_checked=metadata.get('assumptions_checked', {}),
                          no_refresh_note=contract.NO_REFRESH_NOTE),
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


def load_recipients(path, sector=None):
    if path.suffix.lower() in ('.yaml', '.yml'):
        config = teams.load_recipients(path)
        return list(dict.fromkeys(entry['email'] for entry in config.values()
                                  if sector is None or sector in entry['sectors']))
    payload = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(payload, dict) or not isinstance(payload.get('recipients'), list):
        raise ValueError('Expected a recipients list in recipients JSON')
    addresses = payload['recipients']
    if addresses:
        email.validate_recipients(addresses)
    if sector and addresses:
        matching = {entry['email'].lower() for entry in teams.recipients_for_sector(sector)}
        addresses = [address for address in addresses if address.lower() in matching]
    return addresses


def select_holdings(sector):
    holdings = discover()
    if sector is None:
        return holdings
    selected = []
    for ticker, path in holdings:
        info_path = ROOT / 'data' / f'{ticker.lower()}-info.json'
        if info_path.is_file():
            info = json.loads(info_path.read_text(encoding='utf-8'))
            if not isinstance(info, dict):
                raise ValueError(f'Invalid cached sector data for {ticker}')
            key = info.get('sectorKey', str(info.get('sector', '')).lower())
        else:
            # data/ is a per-run working directory and is not committed; fall
            # back to the tracked sector map so a fresh clone can still filter.
            key = _sector_map().get(ticker)
            if key is None:
                raise ValueError(f'No sector data for {ticker}: run the pipeline or add it to config/sectors.json')
        if key == sector:
            selected.append((ticker, path))
    return selected


def _sector_map():
    path = ROOT / 'config' / 'sectors.json'
    if not path.is_file():
        return {}
    sectors = json.loads(path.read_text(encoding='utf-8')).get('sectors')
    if not isinstance(sectors, dict):
        raise ValueError(f'Invalid sector map {path}')
    return sectors


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
                if not errors and path.with_suffix('.json').exists():
                    if {key: payload.get(key) for key in contract.REQUIRED_TOP_LEVEL} != snapshot_payload(path, from_markdown=True):
                        errors.append('Frozen sidecar / Markdown drift detected')
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
    parser.add_argument('--sector', help='Sector key from cached info and recipient teams (for example technology)')
    args = parser.parse_args(argv)
    try:
        manifest = build(args.out, load_recipients(args.recipients, args.sector), select_holdings(args.sector))
    except (ValueError, OSError, UnicodeError) as exc:
        parser.error(str(exc))
    print(f'Review bundle: {args.out} ({sum(not row["validation_errors"] for row in manifest)} clean drafts)')


if __name__ == '__main__':
    main()

