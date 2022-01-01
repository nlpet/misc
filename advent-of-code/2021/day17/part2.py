# --- Day 17: Trick Shot ---

import re


def search(vx, vy, xmin, xmax, ymin, ymax, x=0, y=0):
    while x <= xmax and y >= ymin:
        if x >= xmin and y <= ymax:
            return 1

        x, y = (x + vx, y + vy)
        vy -= 1

        if vx > 0:
            vx -= 1

    return 0


def find_valid_velocities(xmin, xmax, ymin, ymax):
    total = [
        search(vx, vy, xmin, xmax, ymin, ymax)
        for vy in range(ymin, -ymin)
        for vx in range(1, xmax + 1)
    ]

    return sum(total)


def solution():
    with open("input.txt") as fr:
        xmin, xmax, ymin, ymax = map(int, re.findall(r"-?\d+", fr.read()))

    total = find_valid_velocities(xmin, xmax, ymin, ymax)
    print(total)


if __name__ == "__main__":
    solution()
