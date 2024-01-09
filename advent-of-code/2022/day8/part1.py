import numpy as np


def solve():
    with open("input.txt") as fr:
        trees = np.array([[int(h) for h in line.strip()] for line in fr.readlines()])

    h, l = len(trees), len(trees[0])

    visible = (h - 1) * 2 + (l - 1) * 2

    for row in range(1, h - 1):
        for col in range(1, l - 1):
            height = trees[row, col]
            conditions = [
                max(trees[:row, col]) < height,
                max(trees[row + 1 :, col]) < height,
                max(trees[row, :col]) < height,
                max(trees[row, col + 1 :]) < height,
            ]

            if any(conditions):
                visible += 1

    print(visible)


if __name__ == "__main__":
    solve()
