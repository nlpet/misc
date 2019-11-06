import unittest

from math import ceil
from collections import defaultdict, OrderedDict
from typing import List, Dict, Tuple, Set

Remainders = Dict[int, int]
Solutions = Set[Tuple[Tuple[int]]]


def group_remainders(groups: List[int], p: int) -> Tuple[Remainders, int]:
    """Calculate group remainders (number of chocolates that would be left over
    if the group was given packets with total chocolates count that are equal
    to or exceed p. Exclude evenly divisible groups and add them to the solutions
    count. Create a remainders ordered dictionary to contain the remaining groups
    and their counts.

    Arguments:
        groups -- list of given group sizes
        p -- packet size
    """
    rems, num_groups = defaultdict(int), 0

    for group_size in groups:
        if group_size <= 0:
            continue

        if group_size >= p:
            rem = p * ceil(group_size / p) % group_size
        else:
            rem = p - group_size

        if rem == 0:
            num_groups += 1
        else:
            rems[rem] += 1

    rems = OrderedDict(sorted(rems.items()))
    return rems, num_groups


def find_groups(rems: Remainders,
                p: int,
                current=[],
                branch_solutions=[],
                solutions=set([])
                ) -> Tuple[Remainders, int, List, List, Solutions]:
    """Recursively find groups that satisfy the constraints (sum up to p).

    Arguments:
        rems -- dictionary of the remainders of the groups
        p -- packet size
        current -- currently explored solution
        branch_solutions -- solutions obtained from exploring a path
        solutions -- all candidate solutions
    """
    current_sum = sum(current)

    if current_sum == p:
        branch_solutions.append(current)
        return rems, p, [], branch_solutions, solutions

    if len(rems) == 0 and len(branch_solutions) > 0:
        t = tuple(tuple(s) for s in branch_solutions)

        if t not in solutions:
            solutions.add(t)

        branch_solutions = []

    for rem, count in rems.items():
        if current_sum + (p - rem) > p:
            continue

        rems = rems.copy()

        if rems[rem] == 1:
            del rems[rem]
        else:
            rems[rem] -= 1

        find_groups(rems, p, current + [p - rem], branch_solutions, solutions)

    return rems, p, current, branch_solutions, solutions


def find_pairs(rems: Remainders, num_groups: int,
               p: int) -> Tuple[Remainders, int]:
    """Find all pairs of groups that sum up to p and remove them from the
    remaining groups dictionary.

    Arguments:
        rems -- dictionary of the remainders of the groups
        num_groups -- current total of found solutions
        p -- packet size
    """
    for rem, count in rems.items():
        if count > 0 and rems.get(p - rem, 0) > 0 and rem != p - rem:
            n_pairs = min(count, rems[p - rem])
            num_groups += n_pairs
            rems[rem] -= n_pairs
            rems[p - rem] -= n_pairs

    rems = {k: v for k, v in rems.items() if v != 0}

    return rems, num_groups


def find_best_solution(rems: Remainders, solutions: Solutions, p: int) -> int:
    """Find solution with highest count of groups that get fresh chocolate.

    Arguments:
        rems -- dictionary of the remainders of the groups
        solutions -- set of branch solutions, evaluated separately
        p -- packet size
    """
    best = 0

    for solution in solutions:
        working_rems, current_best = rems.copy(), 0
        for subset in solution:
            if len(subset) > len(working_rems):
                continue

            for n in subset:
                if working_rems.get(p - n) is None:
                    break

                if working_rems[p - n] == 1:
                    del working_rems[p - n]
                else:
                    working_rems[p - n] -= 1

            current_best += 1

        best = max(best, current_best + int(len(working_rems) > 0))

    return best


def n_groups_fresh_chocolate(groups: List[int], p: int) -> int:
    """Return the optimal number of groups that get fresh chocolate by
        1. Finding the remainders of the group sizes and excluding
           evenly divisible groups from later calculations.
        2. Find pairs that sum up to p and exclude them from later calculations.
        3. Recursively compose groups of size >=3 and prioritise groups found
           earlier in the search due to their smaller size.
        4. Find the best solution by iterating through the candidate solutions
           and greedily matching the items in the solutions with the available
           groups until there are no available groups to select.

        Arguments:
            groups -- list of given group sizes
            p -- packet size
    """
    if p <= 0:
        return 0

    rems, num_groups = group_remainders(groups, p)
    rems, num_groups = find_pairs(rems, num_groups, p)

    lrems = len(rems)

    if lrems == 0:
        return num_groups
    elif lrems < 3:
        return num_groups + 1

    _, _, _, _, solutions = find_groups(rems, p)
    num_groups += find_best_solution(rems, solutions, p)

    return num_groups


class Tests(unittest.TestCase):
    def test_empty_groups(self):
        groups = []
        p, answer = 1, 0
        n_groups = n_groups_fresh_chocolate(groups, p)
        self.assertEqual(n_groups, answer)

    def test_empty_packet(self):
        groups = [1, 2, 3]
        p, answer = 0, 0
        n_groups = n_groups_fresh_chocolate(groups, p)
        self.assertEqual(n_groups, answer)

    def test_include_empty_groups(self):
        groups = [1, 2, 0]
        p, answer = 2, 2
        n_groups = n_groups_fresh_chocolate(groups, p)
        self.assertEqual(n_groups, answer)

    def test_include_packet_of_one(self):
        groups = [1, 2, 3]
        p, answer = 1, 3
        n_groups = n_groups_fresh_chocolate(groups, p)
        self.assertEqual(n_groups, answer)

    def test_all_same_p_bigger_coprime(self):
        groups = [3, 3, 3]
        p, answer = 7, 1
        solutions = n_groups_fresh_chocolate(groups, p)
        self.assertEqual(solutions, answer)

    def test_all_same_p_smaller_coprime(self):
        groups = [5, 5, 5]
        p, answer = 3, 1
        solutions = n_groups_fresh_chocolate(groups, p)
        self.assertEqual(solutions, answer)

    def test_all_same_p_same(self):
        groups = [5, 5, 5]
        p, answer = 5, 3
        solutions = n_groups_fresh_chocolate(groups, p)
        self.assertEqual(solutions, answer)

    def test_larger_groups(self):
        groups = [5, 3, 3, 1]
        p, answer = 7, 2
        solutions = n_groups_fresh_chocolate(groups, p)
        self.assertEqual(solutions, answer)

    def test_larger_group_unique_occurrences(self):
        groups = [3, 4, 5, 13]
        p, answer = 12, 2
        solutions = n_groups_fresh_chocolate(groups, p)
        self.assertEqual(solutions, answer)

    def test_larger_group_duplicate_occurrences(self):
        groups = [3, 3, 4, 4, 5, 5, 13]
        p, answer = 12, 3
        solutions = n_groups_fresh_chocolate(groups, p)
        self.assertEqual(solutions, answer)

    def test_example(self):
        groups = [5, 6, 4, 4]
        p, answer = 3, 3
        solutions = n_groups_fresh_chocolate(groups, p)
        self.assertEqual(solutions, answer)

    def test_large_array_same_value(self):
        groups = [2] * 10000
        p, answer = 2, 10000
        solutions = n_groups_fresh_chocolate(groups, p)
        self.assertEqual(solutions, answer)

    def test_large_array_pairs(self):
        groups = [2, 3] * 10000
        p, answer = 5, 10000
        solutions = n_groups_fresh_chocolate(groups, p)
        self.assertEqual(solutions, answer)

    def test_large_subgroup(self):
        groups = [1, 2, 3, 4, 5, 2, 6]
        p, answer = 23, 1
        solutions = n_groups_fresh_chocolate(groups, p)
        self.assertEqual(solutions, answer)


unittest.main(verbosity=2)
