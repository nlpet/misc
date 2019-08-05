import unittest


# https://www.interviewcake.com/question/python3/top-scores
def sort_scores(unsorted_scores, highest_possible_score):
    sorted_scores = [0 for _ in range(highest_possible_score)]
    final_scores = []

    for us in unsorted_scores:
        sorted_scores[us - 1] += 1

    for n in range(highest_possible_score, 0, -1):
        if sorted_scores[n - 1] == 1:
            final_scores.append(n)
        elif sorted_scores[n - 1] > 1:
            final_scores.extend([n] * sorted_scores[n - 1])

    return final_scores


class Test(unittest.TestCase):
    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)

    def test_repeated_scores(self):
        actual = sort_scores([20, 10, 30, 30, 10, 20], 100)
        expected = [30, 30, 20, 20, 10, 10]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
