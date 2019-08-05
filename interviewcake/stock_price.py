import unittest

from math import inf


# https://www.interviewcake.com/question/python3/stock-price
def get_max_profit(stock_prices):

    if len(stock_prices) < 2:
        raise Exception('Cannot purchase stock.')

    buy, sell, profit = stock_prices[0], 0, -inf

    for p in stock_prices[1:]:
        if p < buy:
            profit = max(profit, p - buy)
            buy = p
        elif p > sell:
            profit = max(profit, p - buy)
            sell = p

    return profit


def get_max_profit_solution(stock_prices):

    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    min_price = stock_prices[0]
    max_profit = stock_prices[1] - min_price

    for current_price in stock_prices[1:]:
        potential_profit = current_price - min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, current_price)

    return max_profit


class Test(unittest.TestCase):
    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])


unittest.main(verbosity=2)
