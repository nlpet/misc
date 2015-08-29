"""Implement a trie."""
from pprint import pprint


class Trie:

    """Trie class."""

    def __init__(self):
        """Initialize the trie."""
        self.end = '_end_'
        self.trie = {}

    def create(self, words):
        """Create trie."""
        assert type(words) == list, "Error - expected a list of words."
        root = dict()
        for word in words:
            current_dict = root
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict[self.end] = self.end
        self.trie = root

    def contains(self, word):
        """Check if word is in trie."""
        assert type(word) == str, "Error - word should be a string."
        current_dict = self.trie
        for letter in word:
            if letter in current_dict:
                current_dict = current_dict[letter]
            else:
                return False
        if self.end in current_dict:
            return True
        else:
            return False

    def pretty_print(self):
        """Print string."""
        pprint(self.trie, indent=2)


if __name__ == '__main__':
    words = ["cat", "catter", "caterpillar"]
    trie = Trie()
    trie.create(words)
    trie.pretty_print()
