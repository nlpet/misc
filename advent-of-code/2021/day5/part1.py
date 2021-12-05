# --- Day 5: Hydrothermal Venture ---

import re
from collections import defaultdict


def solution():
    points = defaultdict(int)

    with open("input.txt") as fr:
        for line in fr.readlines():
            match = re.match(r"(\d+),(\d+) -> (\d+),(\d+)", line.strip()).groups()
            x1, y1, x2, y2 = map(int, match)

            if x1 == x2 or y1 == y2:
                xs = range(min(x1, x2), max(x1, x2) + 1)
                ys = range(min(y1, y2), max(y1, y2) + 1)

                for x in xs:
                    for y in ys:
                        points[(x, y)] += 1

    n_points = len([x for x in points.values() if x >= 2])

    print(f"The number of points where at least two lines overlap is {n_points}")


if __name__ == "__main__":
    solution()
