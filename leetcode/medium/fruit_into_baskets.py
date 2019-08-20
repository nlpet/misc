# https://leetcode.com/problems/fruit-into-baskets/


class Solution:
    def totalFruit(self, tree):
        collected = 0
        types, n_types, order, cons = {}, 0, [], {}

        for idx, fruit in enumerate(tree):
            if fruit in types:
                types[fruit] += 1

                if fruit == tree[idx - 1]:
                    cons[fruit] += 1
                else:
                    cons[fruit] = 1
            else:
                if n_types < 2:
                    types[fruit] = 1
                    cons[fruit] = 1
                    n_types += 1
                    order.append(fruit)
                else:
                    collected = max(collected, sum(types.values()))
                    didx = 0 if order[0] != tree[idx - 1] else 1

                    delfruit = order.pop(didx)
                    del types[delfruit]
                    del cons[delfruit]

                    types[order[0]] = cons[order[0]]

                    types[fruit] = 1
                    cons[fruit] = 1
                    order.append(fruit)

        return max(collected, sum(types.values()))


def run_tests():
    sol = Solution()
    assert sol.totalFruit([1, 2, 1]) == 3
    assert sol.totalFruit([0, 1, 2, 2]) == 3
    assert sol.totalFruit([1, 2, 3, 2, 2]) == 4
    assert sol.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5
    assert sol.totalFruit([1]) == 1
    assert sol.totalFruit([1] * 10) == 10
    assert sol.totalFruit([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 11
    assert sol.totalFruit([1, 0, 1, 4, 1, 4, 1, 2, 3]) == 5
    assert sol.totalFruit([0, 1, 6, 6, 4, 4, 6]) == 5
    assert sol.totalFruit([1, 1, 6, 5, 6, 6, 1, 1, 1, 1]) == 6


if __name__ == '__main__':
    run_tests()
