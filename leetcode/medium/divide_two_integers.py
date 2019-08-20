# https://leetcode.com/problems/divide-two-integers/

MAX_INT = 2**31 - 1
MIN_INT = -MAX_INT - 1


class Solution:
    def divide(self, dividend, divisor):
        pass


def run_tests():
    sol = Solution()
    assert sol.divide(10, 3) == 3
    assert sol.divide(7, -3) == -2


if __name__ == '__main__':
    run_tests()
