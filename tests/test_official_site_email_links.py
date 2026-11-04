"""Regression coverage for official-site links in weekly digest cover notes."""
import os
from unittest.mock import patch

import pytest

from email_delivery import _build_brief_email


SAMPLE = [('AAPL', '2026-11-02')]


def _parts(message):
    plain = message.get_body(preferencelist=('plain',)).get_content()
    html = message.get_body(preferencelist=('html',)).get_content()
    return plain, html


def test_weekly_digest_links_to_official_and_research_websites():
    with patch.dict(os.environ, {}, clear=True):
        plain, html = _parts(_build_brief_email(SAMPLE, ['test@example.com'], []))
    for url in ('https://www.jsosif.com/', 'https://geochelone666.github.io/jsosif-ai-pipeline-demo/'):
        assert url in plain and url in html
    assert 'research snapshots' in plain
    assert 'Manage your subscribed stocks' not in plain
    assert '/research-updates' not in html


def test_profile_link_only_when_verified_portal_flag_is_on():
    with patch.dict(os.environ, {
        'SUBSCRIPTION_PORTAL_ENABLED': '1',
        'SUBSCRIPTION_PORTAL_URL': 'https://www.jsosif.com/research-updates',
    }):
        plain, html = _parts(_build_brief_email(SAMPLE, ['test@example.com'], []))
    assert 'Manage your subscribed stocks' in plain
    assert 'https://www.jsosif.com/research-updates' in plain
    assert 'your subscription profile' in html


def test_enabled_portal_rejects_unreviewed_url():
    with patch.dict(os.environ, {
        'SUBSCRIPTION_PORTAL_ENABLED': '1',
        'SUBSCRIPTION_PORTAL_URL': 'https://evil.example/collect',
    }):
        with pytest.raises(ValueError, match='reviewed official URL'):
            _build_brief_email(SAMPLE, ['test@example.com'], [])
