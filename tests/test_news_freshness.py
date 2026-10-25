"""Publication age never silently becomes event truth or changes release gate."""
import copy

import pytest

from news_freshness import publication_freshness, annotate_news_publication_age


@pytest.mark.parametrize('published,event,expected,age', [
    ('2026-10-24', 'market_move', 'current_window', 0),
    ('2026-10-22', 'market_move', 'current_window', 2),
    ('2026-10-21', 'market_move', 'historical_context', 3),
    ('2026-10-21', 'ownership', 'current_window', 3),
    ('2026-10-20', 'ownership', 'historical_context', 4),
    ('2026-10-17', 'earnings', 'current_window', 7),
    ('2026-10-16', 'earnings', 'outside_rss_window', 8),
    ('2026-10-25', 'earnings', 'future_dated', -1),
    ('bad-date', 'earnings', 'unknown_publication_date', None),
    (None, 'earnings', 'unknown_publication_date', None),
])
def test_relativity_and_event_context(published, event, expected, age):
    result = publication_freshness(published, '2026-10-24', event)
    assert result['label'] == expected
    assert result['age_days'] == age


def test_annotation_preserves_all_research_content_and_unresolved_items():
    data = {
        'ticker': 'V',
        'tailwinds': [{'headline': 'V price rises', 'date': '2026-10-23',
                       'event_type': 'market_move'}],
        'headwinds': [],
        'catalysts': [{'headline': 'V earnings', 'date': '2026-10-20',
                       'event_type': 'earnings'}],
        'risks': [],
        'unclassified': [{'headline': 'V unclear price direction', 'date': '2026-10-18',
                          'event_type': 'market_move'}],
        'irrelevant': [{'headline': 'General unrelated market story'}],
        'extraction_stats': {'unique_headlines': 4, 'rule': 1, 'ai': 1,
                             'unknown': 1, 'irrelevant': 1},
    }
    original = copy.deepcopy(data)
    updated = annotate_news_publication_age(data, '2026-10-24')
    assert updated is data
    assert data['extraction_stats'] == original['extraction_stats']
    assert data['irrelevant'] == original['irrelevant']
    assert all(len(data[k]) == len(original[k]) for k in (
        'tailwinds', 'headwinds', 'catalysts', 'risks', 'unclassified'))
    counts = data['publication_freshness_summary']['classified_or_unresolved_counts']
    assert counts['current_window'] == 2
    assert counts['historical_context'] == 1
    assert data['unclassified'][0]['publication_freshness']['label'] == 'historical_context'


def test_blank_dates_are_not_fabricated_and_empty_runs_are_supported():
    data = {'tailwinds': [{'date': '', 'event_type': 'market_move'}]}
    annotate_news_publication_age(data, '2026-10-24')
    assert data['publication_freshness_summary']['classified_or_unresolved_counts'][
        'unknown_publication_date'] == 1
    empty = annotate_news_publication_age({}, '2026-10-24')
    assert sum(empty['publication_freshness_summary']['classified_or_unresolved_counts'].values()) == 0
