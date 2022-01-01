# --- Day 17: Trick Shot ---

import re


def solution():
    with open("input.txt") as fr:
        _, _, ymin, _ = map(int, re.findall(r"-?\d+", fr.read()))

    highest = ((-ymin) * (-ymin - 1)) // 2
    print(highest)


if __name__ == "__main__":
    solution()
