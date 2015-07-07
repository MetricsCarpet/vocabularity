import unittest
from vocabularity import TypeZeroMetric


class BasicTests(unittest.TestCase):
    '''Test basic metrics'''

    def test_metrics_type0(self):
        metric = TypeZeroMetric()
        filename = __file__.replace('.pyc', '.py')
        metric.parse_words(open(filename))
        # print(metric.words)
        assert metric.words['zero'] == 3
        metric.measure()
        # print(metric.vocab_words)
        # print(metric.results)
        # Update the test?
        assert metric.results['num_of_unique_vocab_words'] == 30, \
            "Actual num of unique vocab words: %d" % \
            metric.results['num_of_unique_vocab_words']
