from math import ceil


def solution(X, Y, D):
    dist = Y - X

    if dist <= 0:
        return 0

    return ceil(dist / D)
