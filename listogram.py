#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility


class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for i, word in enumerate(word_list):
                self.add_count(word, i)

    def add_count(self, word, i, count=1):
        """Increase frequency count of given word by given count amount."""
        if word in self:
            for i, char in enumerate(self):
                if char[0] == word:
                    entry = self[i]
                    entry[1] += count
        else:
            self.append([word,count])
            self.types += count
        self.tokens += count
        # TODO: Increase word frequency by count

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        for entry in self:
            if entry[0] == word:
                return entry[1]
            else:
                continue
        return 0
        # TODO: Retrieve word frequency count

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        for entry in self:
            if entry[0] == word:
                return True
            else:
                continue
        return False
        # TODO: Check if word is in this histogram

    def _index(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        if target in self:
            return target
        else:
            return "Target word is not found."
        # TODO: Implement linear search to find index of entry with target word


def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
