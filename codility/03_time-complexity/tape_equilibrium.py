from math import inf


def solution(A):
    left, right = A[0], sum(A[1:])
    min_diff = abs(left - right)

    for p in range(1, len(A) - 1):
        left += A[p]
        right -= A[p]
        min_diff = min(min_diff, abs(left - right))

    return min_diff


def run_tests():
    assert solution([3, 1, 2, 4, 3]) == 1


if __name__ == '__main__':
    run_tests()
