import unittest
from ai_extract import classify_rule, extract
from test_ai_extract import news

class RuleV2Tests(unittest.TestCase):
    def test_event_templates(self):
        for headline,event,category in [
            ('NVDA beats Q3 estimates','earnings','tailwinds'),
            ('Nvidia misses Q3 estimates','earnings','headwinds'),
            ('Nvidia cuts guidance','guidance','headwinds'),
            ('Nvidia raises outlook','guidance','tailwinds'),
            ('Nvidia price target raised at UBS','analyst','tailwinds'),
            ('Nvidia downgraded to sell','analyst','headwinds'),
            ('Nvidia announces share repurchase','buyback','catalysts'),
            ('Nvidia acquires chip startup','acquisition','catalysts'),
            ('Nvidia announces stock split','stock_split','catalysts'),
            ('Nvidia spins off its software division','stock_split','catalysts'),
            ('Nvidia stock sold by Example Fund','ownership','catalysts'),
            ('英伟达 announces acquisition','acquisition','catalysts'),
            ('英伟达财报营收超预期','earnings','tailwinds'),
            ('英伟达下调指引','guidance','headwinds'),
            ('Nvidia shares rise - What happened?','market_move','tailwinds'),
        ]:
            with self.subTest(headline=headline):
                c,r=classify_rule(news(headline),'NVDA')
                self.assertEqual((r['extraction_method'],r['event_type'],c),('rule',event,category))

    def test_unsafe_inferences_remain_pending(self):
        for headline in ['Will Nvidia split its stock?', 'Nvidia may raise guidance',
                         'Nvidia beats estimates but shares fall',
                         'Cerebras stock falls on Nvidia pressure',
                         'Nvidia stock falls just shy of record']:
            with self.subTest(headline=headline):
                self.assertEqual(classify_rule(news(headline),'NVDA')[1]['extraction_method'],'unknown')

    def test_missing_date_and_schema(self):
        item=news('NVDA beats Q3 estimates');item['pubDate']='invalid'
        self.assertEqual(extract([item],'NVDA')['extraction_stats']['unknown'],1)
        r=classify_rule(news('NVDA beats Q3 estimates'),'NVDA')[1]
        self.assertTrue({'headline','summary','date','impact','horizon','confidence','sources','extraction_method'} <= r.keys())
        self.assertEqual(r['summary'],r['headline'])
