import unittest


class TestMaximalSubarray(unittest.TestCase):

    """Unit tests maximal subarray."""

    def tests(self):
        """Tests."""
        self.assertEqual(maximal_subarray([1, 2, 3, 4]), 10)
        self.assertEqual(maximal_subarray([2, 3, -1, -3]), 5)
        self.assertEqual(maximal_subarray([-1, 5, 100, -1000]), 105)
        self.assertEqual(maximal_subarray([-1, -2, -3, -4]), 0)
        self.assertEqual(maximal_subarray([1000, 20000, -1, 300000000]), 300020999)
        self.assertEqual(maximal_subarray([3, 4, -3, -5, 1, 0, -1, 2, -4, -2]), 7)
        self.assertEqual(maximal_subarray([-5, 0, -4, 1, 4, 3, -2, -1, 2, -3]), 8)
        

def maximal_subarray(array):
    """

    :list : array
    """
    if min(array) >= 0:
        return sum(array)
    if max(array) <= 0:
        return 0
    length = len(array)
    result_array = [0 for _ in range(length)]
    result_array[0] = array[0] if array[0] > 0 else 0
    for i in range(1, length):
        if array[i] <= 0:
            if result_array[i - 1] > 0:
                result_array[i] = result_array[i - 1] + array[i]
            else:
                result_array[i] = result_array[i - 1]
        else:
            result_array[i] = result_array[i - 1] + array[i]
    return max(result_array)
    
  
if __name__ == '__main__':
    unittest.main()
