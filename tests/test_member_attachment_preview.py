from copy import deepcopy
from datetime import datetime, timezone
from email import policy
from email.parser import BytesParser
import hashlib
import json
from pathlib import Path
import socket
import stat
import subprocess
import sys

import pytest

import news_review
import news_evidence

import member_attachment_preview as preview
from report_store import write_json, read_json, digest
from sector_briefs import write_bundle
from shared_research_pack import build, digest as payload_digest
from snapshot_emit import emit_frozen_snapshot

NOW = datetime(2026, 11, 6, 22, tzinfo=timezone.utc)


@pytest.fixture
def inputs(tmp_path):
    root = tmp_path / 'store'; entries = []
    for ticker in ('CSCO', 'MSFT', 'JPM'):
        base = Path('archive/synthetic') / ticker
        entry = {'ticker': ticker, 'report_id': 'synthetic/' + ticker, 'as_of': '2026-11-06',
                 'generated_at': '2026-11-06T21:00:00+00:00', 'quality': 'ready'}
        snap = emit_frozen_snapshot(ticker=ticker, as_of=entry['as_of'], quant_metrics={'Close': 100},
                                   ai={'status': 'Available'}, freshness={}, disclaimer='Synthetic fixture')
        snap['quality'] = 'ready'
        for kind in ('json', 'md', 'pdf'):
            relative = base / f'{ticker}-intelligence-20261106.{kind}'
            path = root / relative; path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text({'json': json.dumps(snap), 'md': '# ' + ticker, 'pdf': '%PDF-1.4 fixture ' + ticker}[kind])
            entry[kind] = str(relative)
        entry['sha256'] = {k: digest(root / entry[k]) for k in ('json', 'md', 'pdf')}
        entries.append(entry)
    write_json(root / 'index.json', {'reports': entries})
    write_json(root / 'state/deliveries.json', {'unknown-record': {'status': 'unknown'}})
    bundle = tmp_path / 'sectors'; write_bundle(build(root, as_of='2026-11-06'), bundle)
    config = {'groups': {'desk-a': {'tickers': ['CSCO', 'MSFT']}, 'desk-b': {'tickers': ['CSCO', 'JPM']}},
              'members': [{'id': 'synthetic-1', 'name': 'Example Reviewer', 'email': 'reviewer@example.com',
                           'enabled': True, 'timezone': 'America/Toronto', 'send_weekday': 4, 'send_time': '09:00',
                           'groups': ['desk-a', 'desk-b'], 'content_preferences': {'sector_brief': True}}]}
    return config, root, bundle


def prepare(inputs, **kwargs):
    config, root, bundle = inputs
    return preview.prepare(config, root, now=kwargs.pop('now', NOW), sector_bundle=bundle, **kwargs)


def parse_one(messages):
    assert len(messages) == 1
    return BytesParser(policy=policy.default).parsebytes(next(iter(messages.values())))


def test_overlap_and_sector_dedup_use_coverage_not_private_group_names(inputs):
    review, messages = prepare(inputs, include_sector_drafts=True)
    plan = review['members'][0]
    assert plan['status'] == 'prepared' and plan['delivery_ready'] is False
    assert len(plan['attachments']) == 5  # Three stocks, two sectors, not one sector per stock.
    assert sum(a['kind'] == 'sector_draft' for a in plan['attachments']) == 2
    message = parse_one(messages)
    assert len(list(message.iter_attachments())) == 5
    assert message['To'] == 'reviewer@example.com' and message['From'] is None
    assert 'DO NOT SEND' in message['Subject']
    assert len(message.get_boundary()) <= 70
    assert plan['encoded_bytes'] == len(next(iter(messages.values())))


def test_drafts_require_both_content_preference_and_review_switch(inputs):
    review, _ = prepare(inputs)
    assert len(review['members'][0]['attachments']) == 3
    assert len(review['members'][0]['gaps']) == 2
    inputs[0]['members'][0]['content_preferences']['sector_brief'] = False
    review, _ = prepare(inputs, include_sector_drafts=True)
    assert len(review['members'][0]['attachments']) == 3 and not review['members'][0]['gaps']
    inputs[0]['members'][0].pop('content_preferences')
    review, _ = prepare(inputs, include_sector_drafts=True)
    assert len(review['members'][0]['attachments']) == 3


def test_personal_holdings_override_group_coverage(inputs):
    inputs[0]['members'][0]['tickers'] = ['CSCO', 'CSCO']
    review, _ = prepare(inputs, include_sector_drafts=True)
    assert [a['kind'] for a in review['members'][0]['attachments']] == ['stock_report', 'sector_draft']
    assert 'technology' in review['members'][0]['attachments'][1]['filename']


def test_member_attachments_and_recipients_are_isolated(inputs):
    first = inputs[0]['members'][0]; first['tickers'] = ['CSCO']
    second = dict(first, id='synthetic-2', name='Second Reviewer', email='second@example.com', tickers=['JPM'])
    inputs[0]['members'].append(second)
    review, messages = prepare(inputs, include_sector_drafts=True)
    assert len(messages) == 2
    for plan in review['members']:
        message = BytesParser(policy=policy.default).parsebytes(messages[plan['eml']])
        names = [p.get_filename() for p in message.iter_attachments()]
        if message['To'] == 'reviewer@example.com':
            assert names == ['CSCO-intelligence-20261106.pdf', 'technology-2026-11-06.pdf']
            assert 'second@example.com' not in message.as_string()
        else:
            assert message['To'] == 'second@example.com'
            assert names == ['JPM-intelligence-20261106.pdf', 'financial-services-2026-11-06.pdf']
            assert 'reviewer@example.com' not in message.as_string()


def test_standalone_preferences_are_not_silently_satisfied_by_sector_context(inputs):
    inputs[0]['members'][0]['content_preferences'].update(macro_overview=True, news_catalysts=True)
    review, messages = prepare(inputs, include_sector_drafts=True)
    assert review['members'][0]['status'] == 'prepared_with_gaps'
    assert review['members'][0]['gaps'] == ['macro_overview: standalone artifact unavailable', 'news_catalysts: standalone artifact unavailable']
    assert 'standalone artifact unavailable' in parse_one(messages).get_body().get_content()


@pytest.mark.parametrize('content', [None, [], {'sector_brief': 'true'}, {'unknown': True}])
def test_invalid_content_preferences_fail_closed(inputs, content):
    inputs[0]['members'][0]['content_preferences'] = content
    with pytest.raises(ValueError, match='Content'): prepare(inputs)


def test_paused_and_not_due_are_never_prepared_unless_schedule_review_requested(inputs):
    member = inputs[0]['members'][0]
    member['enabled'] = False
    review, messages = prepare(inputs, preview_all=True)
    assert not messages and review['members'][0]['reason'] == 'paused'
    member['enabled'] = True; member['send_weekday'] = 6
    review, messages = prepare(inputs)
    assert not messages and review['members'][0]['reason'] == 'not_due'
    review, messages = prepare(inputs, preview_all=True)
    assert messages and review['members'][0]['schedule_bypassed'] is True


def test_stale_reports_prevent_partial_digest(inputs):
    review, messages = prepare(inputs, now=datetime(2026, 11, 26, 22, tzinfo=timezone.utc), preview_all=True)
    assert not messages and review['members'][0]['status'] == 'deferred_reports'
    assert review['members'][0]['attachments'] == []


def test_missing_one_stock_does_not_silently_deliver_other_stocks(inputs):
    index = read_json(inputs[1] / 'index.json'); index['reports'].pop(); write_json(inputs[1] / 'index.json', index)
    review, messages = prepare(inputs)
    assert not messages and review['members'][0]['status'] == 'deferred_reports'


def test_sector_must_match_selected_stock_version(inputs):
    index = read_json(inputs[1] / 'index.json'); index['reports'][0]['report_id'] = 'new/CSCO'
    write_json(inputs[1] / 'index.json', index)
    review, _ = prepare(inputs, include_sector_drafts=True)
    assert 'sector:technology: stock report version mismatch' in review['members'][0]['gaps']
    assert len(review['members'][0]['attachments']) == 4


def test_future_sector_bundle_is_not_attached(inputs, tmp_path):
    config, root, _ = inputs
    bundle = tmp_path / 'future'; write_bundle(build(root, as_of='2026-11-07'), bundle)
    review, _ = preview.prepare(config, root, now=NOW, sector_bundle=bundle, include_sector_drafts=True)
    assert len(review['members'][0]['attachments']) == 3
    assert all('future' in gap for gap in review['members'][0]['gaps'])


@pytest.mark.parametrize('kind', ['pdf', 'json'])
def test_tampered_sector_artifact_blocks_review(inputs, kind):
    entry = read_json(inputs[2] / 'manifest.json')['briefs'][0]
    with (inputs[2] / entry[kind]).open('ab') as stream: stream.write(b'changed')
    with pytest.raises(ValueError, match='checksum'): prepare(inputs)


def test_manifest_cannot_promote_draft_to_delivery_ready(inputs):
    path = inputs[2] / 'manifest.json'; manifest = read_json(path); manifest['delivery_ready'] = True
    write_json(path, manifest)
    with pytest.raises(ValueError, match='draft bundle'): prepare(inputs)


def test_rehashed_cross_sector_coverage_is_rejected(inputs):
    path = inputs[2] / 'manifest.json'; manifest = read_json(path); entry = manifest['briefs'][0]
    companion = inputs[2] / entry['json']; brief = read_json(companion)
    brief['stocks'][0]['ticker'] = 'CSCO'
    brief['brief_id'] = payload_digest({k:v for k,v in brief.items() if k != 'brief_id'})
    write_json(companion, brief); entry['sha256']['json'] = digest(companion); entry['brief_id'] = brief['brief_id']
    write_json(path, manifest)
    with pytest.raises(ValueError, match='coverage'): prepare(inputs)


def test_mime_bytes_not_raw_pdf_size_control_the_budget(inputs):
    review, messages = prepare(inputs, include_sector_drafts=True)
    encoded = len(next(iter(messages.values())))
    exact, _ = prepare(inputs, include_sector_drafts=True, max_bytes=encoded)
    assert exact['members'][0]['status'] == 'prepared'
    blocked, messages = prepare(inputs, include_sector_drafts=True, max_bytes=encoded - 1)
    plan = blocked['members'][0]
    assert plan['status'] == 'deferred_size' and not messages and plan['eml'] is None
    assert plan['link_fallback'] == 'unavailable_requires_approved_access_control'
    assert 'https://' not in json.dumps(blocked)
    with pytest.raises(ValueError): prepare(inputs, max_bytes=preview.MAX_MESSAGE_BYTES + 1)


def test_duplicate_pdf_bytes_are_attached_once_with_all_logical_identities(inputs):
    index = read_json(inputs[1] / 'index.json')
    first, second = index['reports'][:2]
    (inputs[1] / second['pdf']).write_bytes((inputs[1] / first['pdf']).read_bytes())
    second['sha256']['pdf'] = first['sha256']['pdf']; write_json(inputs[1] / 'index.json', index)
    review, messages = prepare(inputs)
    assert len(review['members'][0]['attachments']) == 2
    assert sorted(len(a['identities']) for a in review['members'][0]['attachments']) == [1, 2]
    assert len(list(parse_one(messages).iter_attachments())) == 2


def test_no_network_no_ledger_mutation_and_deterministic_preview(inputs, monkeypatch):
    def denied(*args, **kwargs): raise AssertionError('Network prohibited')
    monkeypatch.setattr(socket.socket, 'connect', denied)
    before = {str(p): digest(p) for root in inputs[1:] for p in root.rglob('*') if p.is_file()}
    config_before = deepcopy(inputs[0])
    first = prepare(inputs, include_sector_drafts=True)
    assert first == prepare(inputs, include_sector_drafts=True)
    assert inputs[0] == config_before
    assert before == {str(p): digest(p) for root in inputs[1:] for p in root.rglob('*') if p.is_file()}
    assert first[0]['ledger_consulted'] is False and not (inputs[1] / '.delivery.lock').exists()


def test_verified_pdf_bytes_are_retained_if_file_changes_later(inputs, monkeypatch):
    original = preview.load_briefs
    def load_and_change(root):
        result = original(root)
        for row in result.values(): (root / row['filename']).write_bytes(b'changed later')
        return result
    monkeypatch.setattr(preview, 'load_briefs', load_and_change)
    review, messages = prepare(inputs, include_sector_drafts=True)
    parts = list(parse_one(messages).iter_attachments())
    for attachment, part in zip(review['members'][0]['attachments'], parts):
        assert hashlib.sha256(part.get_payload(decode=True)).hexdigest() == attachment['sha256']


def test_private_outputs_refuse_existing_paths_and_public_stores(inputs, tmp_path):
    review, messages = prepare(inputs)
    out = tmp_path / 'private'
    preview.write_private(out, review, messages, forbidden_roots=inputs[1:])
    assert stat.S_IMODE(out.stat().st_mode) == 0o700
    assert all(stat.S_IMODE(p.stat().st_mode) == 0o600 for p in out.iterdir())
    with pytest.raises(FileExistsError): preview.write_private(out, review, messages, forbidden_roots=[])
    link = tmp_path / 'link'; link.symlink_to(out, target_is_directory=True)
    with pytest.raises(FileExistsError): preview.write_private(link, review, messages, forbidden_roots=[])
    with pytest.raises(ValueError): preview.write_private(inputs[1] / 'private', review, messages, forbidden_roots=inputs[1:])


def test_duplicate_archive_report_identity_fails(inputs):
    path = inputs[1] / 'index.json'; index = read_json(path); index['reports'].append(index['reports'][0]); write_json(path,index)
    with pytest.raises(ValueError, match='duplicate'): prepare(inputs)


def test_growing_archive_index_has_a_separate_bounded_budget(inputs):
    path = inputs[1] / 'index.json'; index = read_json(path)
    index['historical_index_metadata'] = 'x' * (preview.MAX_JSON_BYTES + 1)
    write_json(path, index)
    review, messages = prepare(inputs)
    assert messages and review['members'][0]['status'] == 'prepared_with_gaps'
    with pytest.raises(ValueError, match='size limit'): preview.read_object(path)


def test_cli_writes_only_private_previews_and_logs_no_member_data(inputs, tmp_path):
    config, root, bundle = inputs
    config_file = tmp_path / 'members.json'; write_json(config_file, config)
    output = tmp_path / 'review'
    result = subprocess.run([sys.executable, 'scripts/member_attachment_preview.py', '--config', str(config_file),
        '--store', str(root), '--sector-bundle', str(bundle), '--at', NOW.isoformat(),
        '--include-sector-drafts', '--output', str(output)], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert len(list(output.glob('*.eml'))) == 1
    for secret in ('reviewer@example.com', 'Example Reviewer', 'synthetic-1'):
        assert secret not in result.stdout + result.stderr


def macro_bundle_for(inputs, tmp_path, as_of='2026-11-06'):
    from macro_overview import assemble, write_bundle
    path = tmp_path / ('macro-' + as_of)
    write_bundle(assemble(build(inputs[1], as_of=as_of)), path)
    return path


def test_macro_is_independent_of_sector_preference_and_requires_own_switch(inputs, tmp_path):
    macro = macro_bundle_for(inputs, tmp_path)
    content = inputs[0]['members'][0]['content_preferences']
    content.update(macro_overview=True, sector_brief=False)
    review, _ = prepare(inputs, macro_bundle=macro, include_sector_drafts=True)
    assert 'macro_overview: draft review not enabled' in review['members'][0]['gaps']
    assert len(review['members'][0]['attachments']) == 3
    review, messages = prepare(inputs, macro_bundle=macro, include_macro_drafts=True)
    assert [a['kind'] for a in review['members'][0]['attachments']].count('macro_draft') == 1
    assert len(list(parse_one(messages).iter_attachments())) == 4 and not review['members'][0]['gaps']
    content['macro_overview'] = False
    review, _ = prepare(inputs, macro_bundle=macro, include_macro_drafts=True)
    assert len(review['members'][0]['attachments']) == 3


def test_macro_snapshot_hash_must_match_even_when_report_id_is_unchanged(inputs, tmp_path):
    macro = macro_bundle_for(inputs, tmp_path)
    inputs[0]['members'][0]['content_preferences'] = {'macro_overview': True}
    index = read_json(inputs[1] / 'index.json'); entry = index['reports'][0]
    path = inputs[1] / entry['json']; snapshot = read_json(path)
    snapshot['quant'][0]['value'] = '123'; write_json(path, snapshot)
    entry['sha256']['json'] = digest(path); write_json(inputs[1] / 'index.json', index)
    review, _ = prepare(inputs, macro_bundle=macro, include_macro_drafts=True)
    assert 'macro_overview: stock snapshot lineage mismatch' in review['members'][0]['gaps']
    assert len(review['members'][0]['attachments']) == 3


def test_future_macro_is_disclosed_and_not_attached(inputs, tmp_path):
    macro = macro_bundle_for(inputs, tmp_path, '2026-11-07')
    inputs[0]['members'][0]['content_preferences'] = {'macro_overview': True}
    review, _ = prepare(inputs, macro_bundle=macro, include_macro_drafts=True)
    assert review['members'][0]['gaps'] == ['macro_overview: stale or future draft']
    assert len(review['members'][0]['attachments']) == 3


def test_macro_counts_toward_encoded_budget_and_news_remains_missing(inputs, tmp_path):
    macro = macro_bundle_for(inputs, tmp_path)
    inputs[0]['members'][0]['content_preferences'] = {'macro_overview': True, 'news_catalysts': True}
    review, messages = prepare(inputs, macro_bundle=macro, include_macro_drafts=True)
    assert review['members'][0]['gaps'] == ['news_catalysts: standalone artifact unavailable']
    size = len(next(iter(messages.values())))
    blocked, messages = prepare(inputs, macro_bundle=macro, include_macro_drafts=True, max_bytes=size-1)
    assert not messages and blocked['members'][0]['status'] == 'deferred_size'


def test_macro_cli_builds_a_private_preview(inputs, tmp_path):
    macro = macro_bundle_for(inputs, tmp_path)
    config, root, _ = inputs
    config['members'][0]['content_preferences'] = {'macro_overview': True}
    config_file = tmp_path / 'macro-members.json'; write_json(config_file, config)
    output = tmp_path / 'macro-review'
    result = subprocess.run([sys.executable, 'scripts/member_attachment_preview.py', '--config', str(config_file),
        '--store', str(root), '--macro-bundle', str(macro), '--at', NOW.isoformat(), '--include-macro-drafts',
        '--output', str(output)], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    plan = read_json(output / 'review.json')['members'][0]
    assert plan['attachments'][-1]['kind'] == 'macro_draft' and plan['delivery_ready'] is False


def news_bundle_for(inputs, tmp_path, *, as_of='2026-11-06'):
    out = tmp_path / ('news-' + as_of)
    news_review.write_bundle(news_review.assemble(news_evidence.build(inputs[1], as_of=as_of)), out, store=inputs[1])
    return out


def test_news_requires_own_preference_and_independent_draft_switch(inputs, tmp_path):
    bundle = news_bundle_for(inputs, tmp_path)
    config = inputs[0]; config['members'][0]['content_preferences'] = {}
    review, _ = prepare(inputs, news_bundle=bundle, include_news_drafts=True)
    assert len(review['members'][0]['attachments']) == 3
    config['members'][0]['content_preferences'] = {'news_catalysts': True}
    review, _ = prepare(inputs, news_bundle=bundle, include_macro_drafts=True, include_sector_drafts=True)
    assert review['members'][0]['gaps'] == ['news_catalysts: draft review not enabled']
    review, messages = prepare(inputs, news_bundle=bundle, include_news_drafts=True)
    plan = review['members'][0]
    assert plan['status'] == 'prepared' and not plan['delivery_ready'] and not review['ledger_consulted']
    assert [a['kind'] for a in plan['attachments']] == ['stock_report']*3 + ['news_draft']
    message = parse_one(messages)
    assert len(list(message.iter_attachments())) == 4 and message['From'] is None
    assert 'not only your holdings' in message.get_body(preferencelist=('plain',)).get_content()


def test_news_preview_keeps_pause_personal_override_and_recipients_separate(inputs, tmp_path):
    bundle = news_bundle_for(inputs, tmp_path)
    first = inputs[0]['members'][0]; first['tickers'] = ['CSCO']; first['content_preferences'] = {'news_catalysts': True}
    second = deepcopy(first); second.update(id='second', email='second@example.com', enabled=False)
    third = deepcopy(first); third.update(id='third', email='third@example.com', content_preferences={'news_catalysts': False})
    inputs[0]['members'] += [second, third]
    review, messages = prepare(inputs, news_bundle=bundle, include_news_drafts=True, preview_all=True)
    assert len(messages) == 2
    assert sorted(len(m['attachments']) for m in review['members']) == [0, 1, 2]
    assert sum(a['kind'] == 'news_draft' for m in review['members'] for a in m['attachments']) == 1
    assert any(m['reason'] == 'paused' for m in review['members'])


def test_news_snapshot_lineage_mismatch_is_explicit(inputs, tmp_path):
    bundle = news_bundle_for(inputs, tmp_path)
    inputs[0]['members'][0]['content_preferences'] = {'news_catalysts': True}
    index = read_json(inputs[1] / 'index.json'); entry = index['reports'][0]
    path = inputs[1] / entry['json']; snap = read_json(path); snap['disclaimer'] = 'Changed source snapshot'
    write_json(path, snap); entry['sha256']['json'] = digest(path); write_json(inputs[1] / 'index.json', index)
    review, _ = prepare(inputs, news_bundle=bundle, include_news_drafts=True)
    assert review['members'][0]['gaps'] == ['news_catalysts: stock snapshot lineage mismatch']
    assert len(review['members'][0]['attachments']) == 3


@pytest.mark.parametrize('as_of', ['2026-11-07', '2026-11-01'])
def test_news_future_or_stale_drafts_are_not_attached(inputs, tmp_path, as_of):
    bundle = news_bundle_for(inputs, tmp_path, as_of=as_of)
    inputs[0]['members'][0]['content_preferences'] = {'news_catalysts': True}
    review, _ = prepare(inputs, news_bundle=bundle, include_news_drafts=True)
    assert review['members'][0]['gaps'] == ['news_catalysts: stale or future draft']


def test_news_uses_verified_captured_bytes_even_if_file_changes(inputs, tmp_path, monkeypatch):
    bundle = news_bundle_for(inputs, tmp_path); manifest = read_json(bundle / 'manifest.json')
    expected = (bundle / manifest['pdf']).read_bytes()
    original = news_review.load_bundle
    def load_then_change(root):
        result = original(root)
        (root / manifest['pdf']).write_bytes(b'changed after capture')
        return result
    monkeypatch.setattr(news_review, 'load_bundle', load_then_change)
    inputs[0]['members'][0]['content_preferences'] = {'news_catalysts': True}
    _, messages = prepare(inputs, news_bundle=bundle, include_news_drafts=True)
    attachments = list(parse_one(messages).iter_attachments())
    assert attachments[-1].get_payload(decode=True) == expected


def test_news_counts_toward_actual_encoded_mime_budget(inputs, tmp_path):
    bundle = news_bundle_for(inputs, tmp_path)
    inputs[0]['members'][0]['content_preferences'] = {'news_catalysts': True}
    baseline, _ = prepare(inputs)
    cap = baseline['members'][0]['encoded_bytes'] + 1
    review, messages = prepare(inputs, news_bundle=bundle, include_news_drafts=True, max_bytes=cap)
    plan = review['members'][0]
    assert not messages and plan['status'] == 'deferred_size'
    assert plan['encoded_bytes'] > cap and plan['link_fallback'] == 'unavailable_requires_approved_access_control'


def test_news_cli_writes_private_outputs_and_leaves_inputs_unchanged(inputs, tmp_path):
    bundle = news_bundle_for(inputs, tmp_path); config, root, _ = inputs
    config['members'][0]['content_preferences'] = {'news_catalysts': True}
    before = {p: p.read_bytes() for folder in (root, bundle) for p in folder.rglob('*') if p.is_file()}
    config_file = tmp_path / 'news-members.json'; write_json(config_file, config)
    output = tmp_path / 'private-news'
    result = subprocess.run([sys.executable, 'scripts/member_attachment_preview.py', '--config', str(config_file),
        '--store', str(root), '--news-bundle', str(bundle), '--at', NOW.isoformat(), '--include-news-drafts',
        '--output', str(output)], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    plan = read_json(output / 'review.json')['members'][0]
    assert plan['attachments'][-1]['kind'] == 'news_draft' and not plan['delivery_ready']
    assert stat.S_IMODE(output.stat().st_mode) == 0o700
    assert all(stat.S_IMODE(p.stat().st_mode) == 0o600 for p in output.iterdir())
    assert all(p.read_bytes() == raw for p, raw in before.items())
