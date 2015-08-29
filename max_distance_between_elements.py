"""Largest distance between same valued elements in array.

Given a 1D int array, find the largest distance between 2 elements with
the same value.

Optimize it to O(n)
"""
import unittest


def largest_distance(array):
    """Find largest distance. Expects a list of integers."""
    assert type(array) == list, "Error - expected a list"
    assert len(array) > 0, "Error - empty list"

    for el in array:
        assert type(el) == int, "Error - expected a list of integers"

    # [distance, n]
    largest_distance = [0, 0]
    d = {}
    for i, n in enumerate(array):
        if n in d.keys():
            distance = i - d[n][0]
            if distance > d[n][1]:
                d[n][1] = distance
                if distance > largest_distance[0]:
                    largest_distance = [distance, n]
        else:
            d[n] = [i, 0]
    return largest_distance


class TestLargestDistance(unittest.TestCase):

    """Unit tests for largest_distance."""

    def test_empty_list(self):
        """Test empty list."""
        with self.assertRaises(AssertionError):
            largest_distance([])

    def test_impure_list(self):
        """Test whether list is made of integers only."""
        with self.assertRaises(AssertionError):
            largest_distance([1, 2, 3, 4, "a", 5])

    def test(self):
        """Run tests."""
        self.assertEqual(largest_distance([1, 2, 3, 4, 1, 2, 2]), [5, 2])
        self.assertEqual(largest_distance([1, 1]), [1, 1])
        self.assertEqual(largest_distance([1, 0, 0, 0, 0, 1]), [5, 1])
        self.assertEqual(largest_distance([1, 0, 0, 0, 0, 2]), [3, 0])


if __name__ == '__main__':
    unittest.main()
