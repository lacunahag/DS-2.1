#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility
from random import randrange


class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__()  # Initialize this as a new dict
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # Increase word frequency by count
        try:
            self[word] += count
            self.tokens += count
        except KeyError:
            self[word] = count
            self.tokens += count
            self.types += 1

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        try:
            return self[word]
        except KeyError:
            return 0

    def random_word(self):
        random_word = ''
        sum_of_weights = sum(self.values())
        random_weight = randrange(sum_of_weights)

        for key, value in self.items():
            if random_weight - value < 0:
                random_word = key
                break
            else:
                random_weight -= value
        
        return random_word


def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()