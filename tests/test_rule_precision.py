"""Regression checks for high-precision price-direction cues.

These are deliberately selected edge cases, not a statistical accuracy sample.
"""
import pytest

from ai_extract import classify_rule


def headline(value):
    return {
        'headline': value, 'source': 'Fixture',
        'link': 'https://example.test/story',
        'pubDate': 'Fri, 23 Oct 2026 12:00:00 GMT',
    }


@pytest.mark.parametrize('ticker,title,category,sentiment,event', [
    ('SPGI', 'SPGI Gears Up to Report Q3 Earnings', 'catalysts', 'neutral', 'earnings'),
    ('SPGI', 'SPGI stock up 2.4% after quarterly results', 'tailwinds', 'positive', 'earnings'),
    ('SPGI', 'SPGI shares down 2.4% after quarterly results', 'headwinds', 'negative', 'earnings'),
    ('SPGI', 'SPGI stock is up after earnings', 'tailwinds', 'positive', 'earnings'),
    ('SPGI', 'SPGI shares are down after earnings', 'headwinds', 'negative', 'earnings'),
    ('V', 'Visa (NYSE:V) Stock Jumps 1.6% - Still a Buy?', 'tailwinds', 'positive', 'market_move'),
    ('XYL', 'Xylem (NYSE:XYL) Stock Price Target Lowered at JPMorgan Chase & Co.',
     'headwinds', 'negative', 'analyst'),
])
def test_price_cues_must_be_explicit(ticker, title, category, sentiment, event):
    assigned, record = classify_rule(headline(title), ticker)
    assert (assigned, record['sentiment'], record['event_type']) == (category, sentiment, event)
    assert record['extraction_method'] == 'rule'


@pytest.mark.parametrize('ticker,title', [
    ('V', 'Will Visa stock be up after its next earnings?'),
    ('SPGI', 'Could SPGI stock go down after quarterly earnings?'),
    ('SPGI', 'A competitor gears up to report SPGI earnings expectations'),
])
def test_questions_and_unrelated_subjects_remain_unclassified(ticker, title):
    _, record = classify_rule(headline(title), ticker)
    assert record['extraction_method'] == 'unknown'


def test_event_calendar_is_not_a_directional_return_signal():
    _, record = classify_rule(headline('SPGI Gears Up to Report Q3 Earnings'), 'SPGI')
    assert record['confidence'] == 0.8  # heuristic score, not a calibrated probability
    assert record['sentiment'] == 'neutral'
