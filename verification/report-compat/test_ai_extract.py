import unittest
from ai_extract import extract, KEYS, MODEL


def news(headline):
    return dict(headline=headline, source='RSS source', link='https://example.com/news', pubDate='Fri, 02 Oct 2026 12:00:00 GMT')


class ExtractionTests(unittest.TestCase):
    def test_rules_do_not_call_ai(self):
        def forbidden(*args):
            self.fail('clear news called AI')
        data = extract([news('Nvidia stock jumps after earnings')], 'NVDA', forbidden)
        item = data['tailwinds'][0]
        self.assertEqual((item['event_type'], item['sentiment'], item['extraction_method']), ('earnings', 'positive', 'rule'))
        self.assertEqual(item['companies'], ['NVDA'])

    def test_ambiguity_and_rss_authority(self):
        headline = 'Could Nvidia stock jump after earnings?'
        def ai(items, ticker):
            self.assertEqual(len(items), 1)
            return dict(ticker=ticker, **{k: [dict(headline=headline, summary='Uncertain earnings reaction.', date='2099-01-01', source='invented', sources=['https://invented'], impact='low', horizon='short', confidence=.5, event_type='earnings', sentiment='neutral')] if k == 'catalysts' else [] for k in KEYS})
        data = extract([news(headline), news(headline), news('Nvidia stock gains')], 'NVDA', ai)
        item = data['catalysts'][0]
        self.assertEqual(item['date'], '2026-10-02')
        self.assertEqual(item['source'], 'RSS source')
        self.assertEqual(item['sources'], ['https://example.com/news'])
        self.assertEqual(data['extraction_stats'], dict(unique_headlines=2, rule=1, ai=1, unknown=0))

    def test_ai_failure_preserves_rules(self):
        def failed(*args):
            raise RuntimeError('quota')
        data = extract([news('Nvidia stock gains'), news('Will Nvidia rise?')], 'NVDA', failed)
        self.assertEqual(len(data['tailwinds']), 1)
        self.assertEqual(data['unclassified'][0]['extraction_method'], 'unknown')
        self.assertIn('quota', data['error'])
        self.assertTrue(MODEL.endswith('flash-lite'))

    def test_conflicting_signals_and_boundaries(self):
        data = extract([news('Nvidia earnings rise but stock falls'), news('Pineapple stock gains')], 'AAPL')
        self.assertEqual(data['extraction_stats']['rule'], 0)
        self.assertEqual(data['unclassified'][1]['companies'], [])


if __name__ == '__main__':
    unittest.main()
