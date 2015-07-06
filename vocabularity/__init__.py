'''
 vocabularity
 ------------

Implements a software quality metric that allows to inspect the vocabulary
of the the source code. E.g. it helps answering how many English words vs.
abbreviation are a part of the code.


The MIT License (MIT)

Copyright (c) 2015 Yauhen Yakimovich

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
import re

from vocabularity.version import __version__ as vocabularity_version


class VocabularityMetricBase(object):
    '''
    This class is inherited by all types of metrics.
    '''

    def __init__(self):
        self.words = dict()
        self.results = {
            'metrics_version': vocabularity_version,
        }

    def parse_words(self, filestream):
        '''Parse all words in the file. Compute a histogram.'''

    def measure(self, filename):
        '''Find value of `vocabulary` metric'''
        self.results['num_of_all_words'] = sum([val for key, val
                                               in self.num_of_all_words])
        self.results['num_of_vocab_words'] = 0


class TypeZeroMetric(VocabularityMetricBase):
    '''
    TYPE0 vocabularity metric is a metric that does not take into account
    any source code parsing. This metric cannot even decide between if a
    line of the source code is a part of the comment or not. For some languages
    this is a rather difficult task and requires of full implementation of
    grammar parsing step. Even if one wants to do a simple Line Of Code
    (LOC) metrics.
    '''

    _SPLIT_RE = re.compile('\W+')

    def parse_words(self, filestream):
        for line in filestream.readlines():
            for word in self._SPLIT_RE.split(line.strip()):
                if not word:
                    # skip empty
                    continue
                if word not in self.words:
                    self.words[word] = 1
                else:
                    self.words[word] += 1
