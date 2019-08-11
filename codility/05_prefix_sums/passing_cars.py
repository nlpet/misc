def solution(A):
    n_passing, east_count, west_count = 0, 0, 0

    for n in A:
        if n == 0:
            east_count += 1
        else:
            west_count += 1
            n_passing += east_count

    return -1 if n_passing > 1000000000 else n_passing


def run_tests():
    assert solution([0, 1, 0, 1, 1]) == 5


if __name__ == '__main__':
    run_tests()
