"""Audited RSS breadth and recency without a provider or a network dependency."""
import pytest

from news_source_audit import audit_rss


def item(headline, source, published='Fri, 23 Oct 2026 12:00:00 GMT', link='https://example.com/x'):
    return {'headline': headline, 'source': source, 'pubDate': published, 'link': link}


def test_publishers_duplicate_counts_and_freshness():
    rows = [
        item('A', 'Journal A'),
        item('B', 'Journal A', 'Wed, 21 Oct 2026 12:00:00 GMT'),
        item('C', 'Journal B', 'Thu, 22 Oct 2026 12:00:00 GMT'),
        item('A', 'Journal A'),
    ]
    x = audit_rss(rows, '2026-10-23')
    assert x['raw_items'] == 4
    assert x['unique_headlines'] == 3
    assert x['duplicates_excluded'] == 1
    assert x['unique_publishers'] == 2
    assert x['largest_publisher_share_pct'] == pytest.approx(66.67)
    assert x['publisher_hhi'] == pytest.approx(5/9, abs=1e-4)
    assert x['https_link_headlines'] == 3
    assert x['oldest_publication_date'] == '2026-10-21'
    assert x['newest_publication_date'] == '2026-10-23'
    assert x['oldest_headline_age_days'] == 2


def test_malformed_missing_source_or_date_never_claims_verified_links():
    rows = [
        item('A', '', 'bad-date', 'http://example.com'),
        item('B', None, 'Sun, 25 Oct 2026 12:00:00 GMT', 'not a URL'),
        item('', 'Unknown'),
        {'source': 'Unknown'},
    ]
    x = audit_rss(rows, '2026-10-23')
    assert x['invalid_headline_items'] == 2
    assert x['duplicates_excluded'] == 0
    assert x['unique_headlines'] == 2
    assert x['unknown_publisher_headlines'] == 2
    assert x['unique_publishers'] == 0
    assert x['publisher_hhi'] is None
    assert x['largest_publisher_share_pct'] is None
    assert x['missing_or_insecure_link_headlines'] == 2
    assert x['invalid_publication_dates'] == 1
    assert x['future_publication_dates'] == 1


def test_no_headlines_returns_explicit_zero_or_null():
    x = audit_rss([], '2026-10-23')
    assert x['raw_items'] == 0
    assert x['unique_publishers'] == 0
    assert x['oldest_publication_date'] is None
    assert x['oldest_headline_age_days'] is None
    assert x['publisher_hhi'] is None


def test_publisher_normalization_and_one_headline_one_vote():
    x = audit_rss([item('A', '  NEWS CO  '), item('B', 'news co')], '2026-10-23')
    assert x['unique_publishers'] == 1
    assert x['publisher_hhi'] == 1.
