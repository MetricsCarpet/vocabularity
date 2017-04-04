"""
Vocabularity is a measure of software being readable by a human.

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
"""
import re
import enchant

from vocabularity.version import __version__ as vocabularity_version


class VocabularityMetricBase(object):
    """The base class inherited by all types of vocab metrics."""

    def __init__(self):
        """Construct a metric."""
        self.words = dict()
        self.results = {
            'metrics_version': vocabularity_version,
        }
        self._normalized_words = list()

    def parse_words(self, filestream):
        """Parse all words in the file. Compute a histogram."""

    def measure(self):
        """Find value of `vocabulary` metric."""
        self.results['num_of_unique_words'] = len(self.words)
        self.results['total_num_of_words'] = sum([count for count
                                                 in self.words.values()])

    # Is pascal or camel case?
    def _convert_camel_case(self, word):
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', word).lower()

    _SEP = '[_-]'
    _NUMBERS = re.compile(r'^[0-9]+?$')

    def normalize_word(self, word):
        """Normalize words in code to words in natural language."""
        if len(self._normalized_words) == 0:
            word = self._convert_camel_case(word)
            self._normalized_words = re.split(self._SEP, word)
            # print self._normalized_words
        while len(self._normalized_words) > 0:
            item = self._normalized_words.pop(0)
            if len(item) == 0 or self._NUMBERS.match(item):
                # Ignore empty strings or numbers.
                continue
            yield item


class TypeZeroMetric(VocabularityMetricBase):
    """
    Type0 metric is a context free metric.

    TYPE0 vocabularity metric is a metric that does not take into account
    any source code parsing. This metric cannot even decide between if a
    line of the source code is a part of the comment or not. For some languages
    this is a rather difficult task and requires of full implementation of
    grammar parsing step. Even if one wants to do a simple Line Of Code
    (LOC) metrics. E.g. total number of lines is type0 but number of comment
    lines versus number of code lines is type1.
    """

    _SPLIT_RE = re.compile('\W+')

    def parse_words(self, filestream):
        for line in filestream.readlines():
            for word in self._SPLIT_RE.split(line.strip()):
                if not word:
                    continue  # skip empty
                # Normalize the word - be case insensitive.
                # Treat parts of camel or snake case as separate words.
                for norm_word in self.normalize_word(word):
                    if norm_word not in self.words:
                        self.words[norm_word] = 1
                    else:
                        self.words[norm_word] += 1

    _DICT = enchant.Dict("en_US")

    def is_vocab(self, word):
        """Return False if the word is not found in spelling."""
        x = self._DICT.check(word)
        return x

    def measure(self):
        super(TypeZeroMetric, self).measure()
        vocab_words = dict()
        for key in self.words:
            if len(key) == 0:
                raise ValueError()
            if self.is_vocab(key):
                vocab_words[key] = self.words[key]
        self.results['num_of_unique_vocab_words'] = len(vocab_words)
        self.results['num_of_vocab_words'] = sum([count for count
                                                 in vocab_words.values()])
        self.vocab_words = vocab_words
