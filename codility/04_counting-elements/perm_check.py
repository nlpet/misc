def solution(A):
    missing = {n + 1: True for n in range(len(A))}

    for n in A:
        if missing.get(n):
            del missing[n]
        else:
            return 0

    return int(len(missing.keys()) == 0)


def run_tests():
    assert solution([4, 1, 3, 2]) == 1
    assert solution([4, 1, 3]) == 0


if __name__ == '__main__':
    run_tests()
