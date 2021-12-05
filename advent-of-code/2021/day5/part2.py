# --- Day 5: Hydrothermal Venture ---

import re
from collections import defaultdict


def get_range(a, b):
    step = 1 if a < b else -1
    return range(a, b + step, step)


def solution():
    points = defaultdict(int)

    with open("input.txt") as fr:
        for line in fr.readlines():
            match = re.match(r"(\d+),(\d+) -> (\d+),(\d+)", line.strip()).groups()
            x1, y1, x2, y2 = map(int, match)

            if y1 == y2:
                xs = range(min(x1, x2), max(x1, x2) + 1)
                for x in xs:
                    points[(x, y1)] += 1
            elif x1 == x2:
                ys = range(min(y1, y2), max(y1, y2) + 1)
                for y in ys:
                    points[(x1, y)] += 1
            elif (abs(x1 - y1) == abs(x2 - y2)) or (abs(x1 - x2) == abs(y1 - y2)):
                xs = get_range(x1, x2)
                ys = get_range(y1, y2)

                for x, y in zip(xs, ys):
                    points[(x, y)] += 1
            else:
                print("Skipping line {}".format((x1, y1, x2, y2)))

    n_points = len([x for x in points.values() if x >= 2])
    print(f"The number of points where at least two lines overlap is {n_points}")


if __name__ == "__main__":
    solution()
