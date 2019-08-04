def solution(A, K):
    l = len(A)

    if l == 0:
        return A

    k = K % len(A)

    if k == 0:
        return A

    return A[l - k:] + A[:l - k]


def run_tests():
    assert solution([], 0) == []
    assert solution([1, 2], 1) == [2, 1]
    assert solution([1, 2], 2) == [1, 2]
    assert solution([1, 2, 3], 1) == [3, 1, 2]
    assert solution([1, 2, 3], 2) == [2, 3, 1]


if __name__ == '__main__':
    run_tests()
