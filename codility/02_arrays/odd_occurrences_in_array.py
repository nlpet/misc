


def solution(A):
    seen = {}

    for n in A:
        if seen.get(n):
            del seen[n]
        else:
            seen[n] = True

    return list(seen.keys())[0]
