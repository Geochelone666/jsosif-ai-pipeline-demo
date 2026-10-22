#!/usr/bin/env python3
"""Render existing intelligence snapshots as offline multipart email; never send."""
import argparse
from datetime import date
from email.message import EmailMessage
from email import policy
from html import escape
import json
import os
from pathlib import Path
import re
import sys
from typing import Protocol

ROOT = Path(__file__).resolve().parents[1]
AI_SECTIONS = ('TAILWINDS', 'HEADWINDS', 'CATALYSTS', 'RISKS')
MISSING = 'N/A: section or evidence missing from snapshot.'
DISCLAIMER = 'Not investment advice. For analyst research preparation only; verify source data and AI claims.'


def validate_recipients(recipients):
    """Accept a nonempty, unique list of bare ASCII mailbox addresses."""
    pattern = r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~.-]+@[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+"
    if not isinstance(recipients, list) or not recipients:
        raise ValueError('recipients must be a nonempty list of email addresses')
    seen = set()
    for address in recipients:
        if (not isinstance(address, str) or len(address) > 254
                or not re.fullmatch(pattern, address)
                or address.startswith('.') or '..' in address
                or '.@' in address or len(address.split('@')[0]) > 64):
            raise ValueError('Invalid recipient: use bare ASCII email addresses')
        if address.lower() in seen:
            raise ValueError('Duplicate recipient')
        seen.add(address.lower())
    return recipients


def load_recipients(path):
    # Separate file deliberately avoids loading pipeline/provider credentials.
    try:
        payload = json.loads(Path(path).read_text(encoding='utf-8'))
    except (OSError, ValueError):
        raise ValueError('Cannot read recipients JSON') from None
    if not isinstance(payload, dict):
        raise ValueError('Recipient configuration must be an object')
    return validate_recipients(payload.get('recipients'))


def load_snapshot(path):
    path = Path(path)
    match = re.fullmatch(r'([A-Z0-9][A-Z0-9.-]*)-intelligence-(\d{8})\.(md|json)', path.name)
    if not match or not path.is_file():
        raise ValueError('Expected an existing TICKER-intelligence-YYYYMMDD.md/json snapshot')
    ticker, stamp, _ = match.groups()
    as_of = date.fromisoformat(f'{stamp[:4]}-{stamp[4:6]}-{stamp[6:]}').isoformat()
    md, sidecar = path.with_suffix('.md'), path.with_suffix('.json')
    text = md.read_text(encoding='utf-8') if md.is_file() else ''
    metadata = json.loads(sidecar.read_text(encoding='utf-8')) if sidecar.is_file() else {}
    if not isinstance(metadata, dict):
        raise ValueError('Snapshot sidecar must be an object')
    if metadata.get('ticker', ticker) != ticker or metadata.get('as_of', as_of) != as_of:
        raise ValueError('Snapshot filename and sidecar identity disagree')
    if 'contract_version' in metadata:
        from snapshot_contract import validate_snapshot
        if validate_snapshot(metadata) or metadata['identity']['ticker'] != ticker or metadata['identity']['as_of'] != as_of:
            raise ValueError('Invalid frozen snapshot identity or contract')
    for label, expected in (('ticker', ticker), ('Report as_of', as_of)):
        found = re.search(r'^- ' + label + r': \*\*([^*]+)\*\*', text, re.M)
        if found and found.group(1) != expected:
            raise ValueError('Snapshot filename and Markdown identity disagree')
    parts = re.split(r'^## (.+)\s*$', text, flags=re.M)
    sections = dict(zip(parts[1::2], (part.strip() for part in parts[2::2])))
    return ticker, as_of, parts[0], sections, metadata


def _recipient_display_name(address):
    """Derive a display name from a mailbox address (local part, first letter capitalized)."""
    local = address.split('@', 1)[0]
    return local[:1].upper() + local[1:] if local else address


def _normalize_pdf_paths(pdf_path):
    if pdf_path is None:
        return []
    paths = pdf_path if isinstance(pdf_path, (list, tuple)) else [pdf_path]
    result = []
    for p in paths:
        pdf = Path(p)
        if not pdf.is_file():
            raise ValueError(f'PDF attachment not found: {pdf}')
        result.append(pdf)
    return result


def _build_brief_email(snapshots, recipients, pdf_paths, display_name=None):
    """Short cover-note format: greeting, report list, sign-off.

    Details live in the PDF attachments; the body only introduces them.
    """
    title = 'JSOSIF Intelligence Reports | ' + '; '.join(f'{day} {ticker}' for ticker, day, *_ in snapshots)
    name = display_name or _recipient_display_name(recipients[0])
    plain = [
        f'Hi {name},',
        '',
        'Here are the latest JSOSIF intelligence reports:',
        '',
    ]
    plain += [f'- {ticker} — {day}' for ticker, day, *_ in snapshots]
    plain += ['', 'Best,', 'Tech Team']
    html = [
        '<html><body>',
        f'<p>Hi {escape(name)},</p>',
        '<p>Here are the latest JSOSIF intelligence reports:</p>',
        '<ul>',
    ]
    html += [f'<li>{escape(ticker)} &mdash; {escape(day)}</li>' for ticker, day, *_ in snapshots]
    html += ['</ul>', '<p>Best,<br>Tech Team</p>', '</body></html>']
    message = EmailMessage(policy=policy.SMTP)
    message['Subject'] = title
    message['To'] = ', '.join(recipients)
    message.set_content('\n'.join(plain))
    message.add_alternative('\n'.join(html), subtype='html')
    for pdf in pdf_paths:
        message.add_attachment(pdf.read_bytes(), maintype='application',
                               subtype='pdf', filename=pdf.name)
    return message


def build_email(paths, recipients, *, review_only=False, pdf_path=None, brief=False, display_name=None):
    # Empty recipients remain visibly pending in offline review artifacts.
    if not (review_only and recipients == []):
        recipients = validate_recipients(recipients)
    snapshots = []
    seen = set()
    for path in paths:
        identity = Path(path).resolve().with_suffix('')
        if identity not in seen:
            snapshots.append(load_snapshot(path))
            seen.add(identity)
    if not snapshots:
        raise ValueError('At least one snapshot is required')
    pdf_paths = _normalize_pdf_paths(pdf_path)
    if brief:
        return _build_brief_email(snapshots, recipients, pdf_paths, display_name)
    title = 'JSOSIF snapshot | ' + '; '.join(f'{day} {ticker}' for ticker, day, *_ in snapshots)
    plain, html = [title], [f'<html><body><h1>{escape(title)}</h1>']

    def section(name, content):
        plain.extend(['', name, content])
        html.extend([f'<h3>{escape(name)}</h3>', f'<pre style="white-space:pre-wrap">{escape(content)}</pre>'])

    for ticker, day, header, sections, metadata in snapshots:
        heading = f'{day} | Holding: {ticker}'
        plain.extend(['', heading, 'Quant metrics'])
        html.extend([f'<h2>{escape(heading)}</h2>', '<h3>Quant metrics</h3>', '<table>', '<tr><th>Metric</th><th>Value</th></tr>'])
        rows = []
        for line in sections.get('QUANTITATIVE', '').splitlines():
            if line.startswith('|'):
                cells = [cell.strip() for cell in line.strip('|').split('|')]
                if len(cells) == 2 and cells[0] != 'Metric' and not re.fullmatch(r'[-: ]+', cells[0]):
                    rows.append(cells)
        for key, value in rows or [('N/A', MISSING)]:
            plain.append(f'{key} | {value}')
            html.append(f'<tr><td>{escape(key)}</td><td>{escape(value)}</td></tr>')
        html.append('</table>')
        plain.extend(['', 'AI summary'])
        html.append('<h3>AI summary</h3>')
        status = next((line for line in header.splitlines() if line.startswith('- AI status:')), 'AI status: ' + MISSING)
        section('AI status', status)
        for name in AI_SECTIONS:
            section(name, sections.get(name) or MISSING)
        freshness = []
        for label in ('Report as_of', 'Market data as_of', 'Market data fetched_at (UTC)', 'AI analysis snapshot as_of', 'Snapshot note'):
            freshness.append(next((line for line in header.splitlines() if line.startswith(f'- {label}:')), f'{label}: {MISSING}'))
        freshness.append('Report date is not a guarantee of data freshness. Daily Close may be provisional; retained AI and other source snapshots may be older. No data is refreshed by email generation.')
        freshness.append('Assumptions version: ' + str(metadata.get('assumptions_version', 'N/A')))
        checks = metadata.get('assumptions_checked')
        freshness.append(json.dumps(checks, ensure_ascii=False, indent=2) if checks else MISSING)
        freshness.append('Missing evidence is not a passed check. Human review is required.')
        section('Assumptions / data freshness', '\n'.join(freshness))
    section('Disclaimer', DISCLAIMER)
    html.append('</body></html>')
    message = EmailMessage(policy=policy.SMTP)
    message['Subject'] = title
    message['To'] = ', '.join(recipients)
    message.set_content('\n'.join(plain))
    message.add_alternative('\n'.join(html), subtype='html')
    for pdf in pdf_paths:
        message.add_attachment(pdf.read_bytes(), maintype='application',
                               subtype='pdf', filename=pdf.name)
    return message


class DeliveryBackend(Protocol):
    """Backend extension point; adding a transport requires explicit approval."""
    def deliver(self, message: EmailMessage) -> None: ...


class DryRunBackend:
    def __init__(self, output=None):
        self.output = Path(output) if output else None

    def deliver(self, message):
        if self.output:
            self.output.write_bytes(message.as_bytes())
        else:
            sys.stdout.write(message.as_string())


class GmailSmtpBackend:
    """Send via Gmail SMTP using an App Password from project config.

    Config file (default: ROOT/config/gmail.json):
        {"address": "team-sender@example.com", "app_password": "..."}

    The config lives in the project, not in Muse's vault — team-owned.
    """
    def __init__(self, config_path=None):
        self.config_path = Path(config_path) if config_path else ROOT / 'config' / 'gmail.json'

    def credentials(self):
        cfg = {'address': os.environ.get('GMAIL_USER'), 'app_password': os.environ.get('GMAIL_APP_PASSWORD')}
        if not all(cfg.values()):
            try:
                cfg = json.loads(self.config_path.read_text(encoding='utf-8'))
            except (OSError, ValueError):
                raise ValueError('Gmail credentials are not configured') from None
        address = cfg.get('address')
        app_password = cfg.get('app_password')
        if not address or not app_password or app_password.startswith('FILL_IN'):
            raise ValueError(f'Gmail config incomplete: set address and app_password in {self.config_path}')
        validate_recipients([address])
        return address, app_password

    def deliver(self, message):
        import smtplib
        import ssl
        address, app_password = self.credentials()
        message['From'] = address
        with smtplib.SMTP('smtp.gmail.com', 587, timeout=60) as smtp:
            smtp.starttls(context=ssl.create_default_context())
            smtp.login(address, app_password)
            refused = smtp.send_message(message)
            if refused:
                raise RuntimeError('SMTP rejected one or more recipients')


def send(message, backend=None):
    """Send via the configured backend. Requires explicit --send flag."""
    (backend or GmailSmtpBackend()).deliver(message)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('snapshots', nargs='+', type=Path)
    parser.add_argument('--recipients', type=Path, default=ROOT / 'recipients.json')
    parser.add_argument('--output', type=Path, help='Write an .eml file instead of stdout')
    parser.add_argument('--pdf', nargs='*', default=None,
                        help='Attach PDF report file(s) to the email')
    parser.add_argument('--brief', action='store_true',
                        help='Use short cover-note body (greeting + report list + sign-off)')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--dry-run', action='store_true', help='Generate only (default)')
    mode.add_argument('--send', action='store_true', help='Send via Gmail SMTP (requires config/gmail.json)')
    args = parser.parse_args(argv)
    if args.send and os.environ.get('JSOSIF_APPROVED_SEND') != '1':
        raise NotImplementedError('Explicit approval is required for email delivery')
    try:
        message = build_email(args.snapshots, load_recipients(args.recipients),
                              pdf_path=args.pdf, brief=args.brief)
    except (ValueError, OSError):
        parser.error('Invalid snapshot or recipients configuration; check filenames, identities and JSON schema')
    if args.send:
        send(message)
        return
    backend: DeliveryBackend = DryRunBackend(args.output)
    backend.deliver(message)


if __name__ == '__main__':
    main()

