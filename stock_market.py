"""
Stock Market Problem

Given an array of n integers (positive / zero / negative) that
represent the price of a stock over n days, write a function to
compute the maximum profit you can make, given that you buy and
sell exactly 1 stock within these n days.
"""
import unittest


class TestStockMarket(unittest.TestCase):

    """Unit tests for stock market."""

    def tests(self):
        """Tests."""
        self.assertEqual(stock_market([1, 2, 3, 4], 4), 3)
        self.assertEqual(stock_market([2, 3, -1, -3], 4), 1)
        self.assertEqual(stock_market([-5, -7, 8, 15], 4), 22)
        
        
def maximal_subarray(array, n):
    """

    :list : array
    """
    if min(array) >= 0:
        return sum(array)
    if max(array) <= 0:
        return 0

    current_sum, max_sum = 0, 0
    for i in range(n):
        current_sum = max(current_sum + array[i], 0)
        max_sum = max(max_sum, current_sum)
    return max_sum        

    
def stock_market(array, n):
    """

    :list : array
    :int : n (length of array)
    """
    days_deltas = [0 for _ in range(n)]
    for i in range(1, n):
        days_deltas[i] = array[i] - array[i - 1]

    max_profit = maximal_subarray(days_deltas, n)
    return max_profit
    
    
  
if __name__ == '__main__':
    unittest.main()
