def solution(N, A):
    counters = [0 for _ in range(N)]
    cmx, lu = 0, 0

    for n in A:
        if n == N + 1:
            lu = cmx
        else:
            if counters[n - 1] < lu:
                counters[n - 1] = lu + 1
            else:
                counters[n - 1] += 1

            if counters[n - 1] > cmx:
                cmx = counters[n - 1]

    for i, c in enumerate(counters):
        if counters[i] < lu:
            counters[i] = lu

    return counters


def run_tests():
    assert solution(5, [3, 4, 4, 6, 1, 4, 4]) == [3, 2, 2, 4, 2]
    assert solution(5, [6, 6, 6, 6, 6]) == [0, 0, 0, 0, 0]
    assert solution(3, [1, 4, 1, 4, 1, 4]) == [3, 3, 3]


if __name__ == '__main__':
    run_tests()
