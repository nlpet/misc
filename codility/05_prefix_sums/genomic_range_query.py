impfs = {'A': 1, 'C': 2, 'G': 3, 'T': 4}


def minimal_impact_factors(S, P, Q, N):
    L = [[0] * N, [0] * N, [0] * N]

    for i in range(3):
        L[i][-1] = N - 1 if impfs[S[N - 1]] <= i + 1 else N

    for k in range(N - 2, -1, -1):
        if impfs[S[k]] == 3:
            L[0][k] = L[0][k + 1]
            L[1][k] = L[1][k + 1]
            L[2][k] = k
        elif impfs[S[k]] == 2:
            L[0][k] = L[0][k + 1]
            L[1][k] = k
            L[2][k] = k
        elif impfs[S[k]] == 1:
            for i in range(3):
                L[i][k] = k
        else:
            for i in range(3):
                L[i][k] = L[i][k + 1]

    return L


def solution(S, P, Q):
    N = len(S)
    L = minimal_impact_factors(S, P, Q, N)
    solutions = []

    for i in range(len(P)):
        sidx, eidx = P[i], Q[i]
        minn = min(impfs[S[sidx]], impfs[S[eidx]])

        if minn == 1 or L[0][sidx] < eidx:
            solutions.append(1)
        elif minn == 2 or L[1][sidx] < eidx:
            solutions.append(2)
        elif minn == 3 or L[2][sidx] < eidx:
            solutions.append(3)
        else:
            solutions.append(4)

    return solutions


def run_tests():
    S = 'CAGCCTA'
    P = [2, 5, 0, 2]
    Q = [4, 5, 6, 5]

    assert solution(S, P, Q) == [2, 4, 1, 2]
    assert solution('C', [0], [0]) == [2]


if __name__ == '__main__':
    run_tests()
