def solution(A):
    missing = {n + 1: True for n in range(len(A) + 1)}
    for n in A:
        del missing[n]

    return list(missing.keys())[0]


def run_tests():
    assert solution([2, 3, 1, 5]) == 4
    assert solution([]) == 1
    assert solution([1, 2, 3, 4, 5, 6, 7, 9]) == 8


if __name__ == '__main__':
    run_tests()
