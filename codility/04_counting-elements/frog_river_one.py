def solution(X, A):
    missing = set(list(range(1, X + 1)))

    for sec, n in enumerate(A):
        if not missing:
            return sec - 1

        missing.discard(n)

    if not missing:
        return sec

    return -1


def run_tests():
    assert solution(5, [1, 3, 1, 4, 2, 3, 5, 4]) == 6
    assert solution(3, [
        1,
        1,
        1,
        1,
    ]) == -1
    assert solution(2, [1, 2]) == 1


if __name__ == '__main__':
    run_tests()
