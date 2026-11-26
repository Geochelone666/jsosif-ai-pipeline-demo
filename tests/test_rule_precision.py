"""Regression checks for high-precision price-direction cues.

These are deliberately selected edge cases, not a statistical accuracy sample.
"""
import pytest

from ai_extract import classify_rule, extract


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
    # An unresolved 2026-11-25 ACN RSS headline had this exact price-move format.
    # Classify only its explicit market move, not a fabricated operating catalyst.
    ('ACN', 'Accenture PLC Stock (ACN) Moved Up by 4.94% on Nov 25: What Investors Need To Know',
     'tailwinds', 'positive', 'market_move'),
    ('ACN', 'Accenture PLC Stock (ACN) Moved Down by 4.35% on Nov 19: A Full Analysis',
     'headwinds', 'negative', 'market_move'),
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
    ('ACN', 'Will Accenture stock move up by 4.94% tomorrow?'),
    ('ACN', 'Microsoft stock moved up by 4.94% while Accenture watched'),
    ('ACN', 'Accenture stock moved up by an unspecified amount'),
])
def test_questions_and_unrelated_subjects_remain_unclassified(ticker, title):
    _, record = classify_rule(headline(title), ticker)
    assert record['extraction_method'] == 'unknown'


def test_event_calendar_is_not_a_directional_return_signal():
    _, record = classify_rule(headline('SPGI Gears Up to Report Q3 Earnings'), 'SPGI')
    assert record['confidence'] == 0.8  # heuristic score, not a calibrated probability
    assert record['sentiment'] == 'neutral'


def test_explicit_market_move_does_not_spend_ai_on_unambiguous_headline():
    def forbidden(*args):
        pytest.fail('Explicit dated target-led price moves must not require an AI call')

    result = extract(
        [headline('Accenture PLC Stock (ACN) Moved Up by 4.94% on Nov 25: What Investors Need To Know')],
        'ACN',
        forbidden,
    )
    assert result['extraction_stats']['rule'] == 1
    assert result['extraction_stats']['unknown'] == 0
    assert result['tailwinds'][0]['event_type'] == 'market_move'
    assert result['tailwinds'][0]['summary'] == result['tailwinds'][0]['headline']
    assert result['tailwinds'][0]['extraction_method'] == 'rule'
