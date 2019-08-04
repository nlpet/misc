import bisect
from time import time
from random import shuffle


def solution(A):
    start = time()
    seen = [0 for _ in range(1000000 + 1)]

    for n in A:
        if n > 0:
            seen[n - 1] += 1

    for idx, s in enumerate(seen):
        if s == 0:
            print('Took {:.2f}s'.format(time() - start))
            return idx + 1

    print('Took {:.2f}s'.format(time() - start))
    return idx + 1


def run_tests():
    assert solution([1, 2, 3]) == 4
    assert solution([-1, -3]) == 1
    assert solution([1, 3, 6, 4, 1, 2]) == 5

    test_a = list(range(1, 1000000 + 1))
    shuffle(test_a)

    assert solution(test_a) == 1000001
    assert solution([-1000000, 1000000]) == 1


if __name__ == '__main__':
    run_tests()
