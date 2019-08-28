# https://leetcode.com/problems/fruit-into-baskets/


class Solution:
    def subsets(self, nums):
        subsets = []
        self.generate_subsets(0, nums, [], subsets)
        return subsets

    def generate_subsets(self, index, nums, current, subsets):
        subsets.append(list(current))
        for i in range(index, len(nums)):
            current.append(nums[i])
            self.generate_subsets(i + 1, nums, current, subsets)
            current.pop()


def run_tests():
    sol = Solution()
    assert sorted(sol.subsets([1, 2, 3])) == sorted([[3], [1], [2], [1, 2, 3],
                                                     [1, 3], [2, 3], [1, 2],
                                                     []])
    assert sorted(sol.subsets([1, 2])) == sorted([[], [1], [2], [1, 2]])
    assert sorted(sol.subsets([1])) == sorted([[], [1]])


if __name__ == '__main__':
    run_tests()
