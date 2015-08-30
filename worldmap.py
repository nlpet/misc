"""
2D array as a world map.

Use a 2D integer array as a worldmap where neighbouring array elements
of the same value are considered to be the same country. Find the number
of countries in the array.
"""
import unittest


def find_adjacent(map, visited, i, j, l, w):
    """Find adjacent cells of the same value."""
    neighbours = ((i - 1, j), (i, j + 1),
                  (i + 1, j), (i, j - 1))

    neighbour_indices = set()
    visited[i][j] = True

    for y, x in neighbours:
        if 0 <= y < l and 0 <= x < w and map[y][x] == map[i][j]:
            neighbour_indices.add((y, x))
    return neighbour_indices


def find_num_countries(map):
    """Count the number of distinct countries."""
    # If map is empty, return 0
    assert len(map) > 0, "Error - empty list"
    assert type(map[0]) == list, "Error - expected 2D array of ints"

    l, w = len(map), len(map[0])
    visited = [[False] * w for _ in range(l)]
    countries = {}

    for i in range(l):
        for j in range(w):
            if not visited[i][j]:
                if map[i][j] in countries.keys():
                    countries[map[i][j]].update(
                        find_adjacent(map, visited, i, j, l, w))
                else:
                    countries[map[i][j]] = {(i, j)}
                    countries[map[i][j]].update(
                        find_adjacent(map, visited, i, j, l, w))
    return sum([1 for v in countries.values() if len(v) > 1])


class TestFindNumCountries(unittest.TestCase):

    """Unit tests for finding number of countries."""

    def test_empty_map(self):
        """Run tests for map 1."""
        empty_map = []
        with self.assertRaises(AssertionError):
            find_num_countries(empty_map)

    def test_map1(self):
        """Run tests for map 1."""
        map1 = [[0, 1, 2, 2, 2, 3],
                [0, 0, 3, 2, 0, 1],
                [0, 4, 0, 5, 9, 8],
                [0, 0, 0, 3, 0, 1]]
        self.assertEqual(find_num_countries(map1), 2)

    def test_map2(self):
        """Run tests for map 2."""
        map2 = [1]
        with self.assertRaises(AssertionError):
            find_num_countries(map2)

    def test_map3(self):
        """Run tests for map 3."""
        map3 = [[1]]
        self.assertEqual(find_num_countries(map3), 0)

    def test_map4(self):
        """Run tests for map 4."""
        map4 = [[1, 0, 2, 3, 4, 5, 7, 8],
                [1, 1, 1, 2, 5, 4, 5, 9],
                [0, 2, 1, 1, 3, 6, 4, 0]]
        self.assertEqual(find_num_countries(map4), 1)

    def test_map5(self):
        """Run tests for map 5."""
        map5 = [[1, 1, 2, 3, 3, 0, 7, 7],
                [2, 0, 4, 4, 0, 9, 9, 9],
                [5, 5, 0, 6, 6, 0, 10, 10]]
        self.assertEqual(find_num_countries(map5), 8)


if __name__ == '__main__':
    unittest.main()
