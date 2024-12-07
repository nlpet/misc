from math import inf


def sign(x):
    return -1 if x < 0 else 1


def is_safe(levels):
    min_diff, max_diff = inf, 0
    level_sign = None

    for f, s in zip(levels, levels[1:]):
        diff = s - f
        s = sign(diff)

        if level_sign is None:
            level_sign = s
        if level_sign != s:
            return 0

        min_diff = min(min_diff, abs(diff))
        max_diff = max(max_diff, abs(diff))

    if min_diff >= 1 and max_diff <= 3:
        return 1

    return 0


def solve():
    n_safe = 0

    with open("input.txt") as fr:
        for report in fr.readlines():
            levels = [int(x) for x in report.strip().split()]
            n_safe += is_safe(levels)

    print(f"Answer: {n_safe}")


if __name__ == "__main__":
    solve()
