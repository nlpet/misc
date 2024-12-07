def sign(x):
    return -1 if x < 0 else 1


def is_safe(levels, tolerance=1):
    level_sign = None
    previous = levels.pop(0)

    while len(levels) > 0:
        current = levels.pop(0)
        diff = current - previous
        s = sign(diff)

        if level_sign is None:
            level_sign = s

        if level_sign != s:
            if tolerance > 0:
                tolerance -= 1
                continue
            return False

        if abs(diff) < 1 or abs(diff) > 3:
            if tolerance > 0:
                tolerance -= 1
                continue
            return False

        previous = current
    return True


def test_safety(levels):
    for i in range(len(levels)):
        if is_safe([x for j, x in enumerate(levels) if j != i], tolerance=0):
            return True
    return False


def solve():
    n_safe = 0

    with open("input.txt") as fr:
        for report in fr.readlines():
            levels = [int(x) for x in report.strip().split()]
            safe = is_safe(levels[:])

            if not safe:
                safe = test_safety(levels)

            n_safe += safe

    print(f"Answer: {n_safe}")


if __name__ == "__main__":
    solve()
