"""Offline evaluation arithmetic is independent of the sampled labels."""
import json

import pytest

from eval_news_classification import (
    ABSTAIN, load_gold, rule_predictions, score, snapshot_predictions, main,
)


def row(ticker, headline, label, day='2026-10-24'):
    return {
        'ticker': ticker, 'headline': headline, 'label': label,
        'source': 'Synthetic fixture',
        'link': 'https://example.test/news',
        'pubDate': 'Sat, 24 Oct 2026 12:00:00 GMT', 'as_of': day,
    }


def key(item):
    return (item['ticker'], item['headline'], item['pubDate'])


def test_precision_does_not_count_abstention_as_correct():
    gold = [row('SPGI', 'SPGI stock up 2%', 'tailwinds'),
            row('SPGI', 'SPGI reports earnings', 'catalysts'),
            row('SPGI', 'SPGI supplier wins unrelated contract', 'irrelevant')]
    predictions = {key(gold[0]): 'tailwinds', key(gold[1]): ABSTAIN,
                   key(gold[2]): 'tailwinds'}
    result = score(gold, predictions)
    assert result['sample_size'] == 3
    assert result['coverage'] == pytest.approx(2 / 3)
    assert result['selective_precision'] == pytest.approx(1 / 2)
    assert result['correct'] == 1
    assert result['wrong'] == 1
    assert result['abstained'] == 1
    assert result['false_company_event_on_irrelevant'] == 1


def test_rule_predictions_abstain_on_conditional_headlines():
    gold = [row('SPGI', 'SPGI Gears Up to Report Q3 Earnings', 'catalysts'),
            row('SPGI', 'Could SPGI stock go up after earnings?', 'tailwinds'),
            row('SPGI', 'SPGI shares down 2% today', 'headwinds')]
    predictions = rule_predictions(gold)
    assert predictions[key(gold[0])] == 'catalysts'
    assert predictions[key(gold[1])] == ABSTAIN
    assert predictions[key(gold[2])] == 'headwinds'


def test_snapshot_scoring_tracks_unresolved_ai_candidates(tmp_path, capsys):
    gold = [row('V', 'Visa stock rises 2%', 'tailwinds'),
            row('V', 'Will Visa acquire a competitor?', 'insufficient_evidence'),
            row('V', 'Could Visa shares fall next quarter?', 'insufficient_evidence')]
    gold_file = tmp_path / 'gold.json'
    gold_file.write_text(json.dumps(gold))
    saved = {
        'ticker': 'V', 'as_of': '2026-10-24',
        'tailwinds': [{'headline': gold[0]['headline'], 'extraction_method': 'rule'}],
        'headwinds': [], 'risks': [], 'catalysts': [
            {'headline': gold[1]['headline'], 'extraction_method': 'ai'}],
        'irrelevant': [], 'unclassified': [
            {'headline': gold[2]['headline'], 'extraction_method': 'unknown'}],
    }
    saved_file = tmp_path / 'ai.json'
    saved_file.write_text(json.dumps(saved))
    eligible, predictions = snapshot_predictions(gold, [saved_file])
    assert len(eligible) == 3
    assert score(eligible, predictions)['coverage'] == pytest.approx(2 / 3)
    main(['--gold', str(gold_file), '--snapshots', str(saved_file)])
    output = json.loads(capsys.readouterr().out)
    assert output['observed_pipeline']['sample_size'] == 3
    assert output['ai_candidate_subset']['sample_size'] == 2
    assert output['ai_candidate_subset']['abstained'] == 1
    assert output['ai_candidate_subset']['selective_precision'] == 0
    assert output['ai_candidate_subset']['false_decisions_on_insufficient_evidence'] == 1
    assert output['ai_candidate_subset']['correct_abstentions_on_insufficient_evidence'] == 1
    assert 'not directly' in output['caution']


@pytest.mark.parametrize('bad', [
    [], [{'ticker': 'SPGI', 'headline': 'Example', 'pubDate': 'x', 'label': 'fabricated'}],
    [{'ticker': 'SPGI', 'headline': 'Example', 'pubDate': 'x', 'label': 'tailwinds'}]*2,
])
def test_gold_input_rejects_invalid_or_duplicate_labels(tmp_path, bad):
    path = tmp_path / 'gold.json'
    path.write_text(json.dumps(bad))
    with pytest.raises(ValueError):
        load_gold(path)
