import unittest
from vocabularity import TypeZeroMetric


class BasicTests(unittest.TestCase):
    '''Test basic metrics'''

    def test_metrics_type0(self):
        metric = TypeZeroMetric()
        filename = __file__.replace('.pyc', '.py')
        metric.parse_words(open(filename))
        # print(metric.words)
        assert metric.words['TypeZeroMetric'] == 3
