# --- Day 13: Transparent Origami ---

import numpy as np


def print_paper(paper):
    for i in range(len(paper)):
        for j in range(len(paper[0])):
            v = "▓" if paper[i][j] else "░"
            print(v, end=" ")
        print()
    print()


def solution():
    with open("input.txt") as fr:
        cx, folds = fr.read().split("\n\n")
        xs, ys = zip(*[[int(n) for n in c.strip().split(",")] for c in cx.split("\n")])
        folds = [fold.split()[-1].split("=") for fold in folds.strip().split("\n")]

    l = 2 * (max([int(x[1]) for x in folds if x[0] == "x"])) + 1
    w = 2 * (max([int(y[1]) for y in folds if y[0] == "y"])) + 1

    paper = np.zeros((w + 1, l + 1), dtype=int)
    paper[ys, xs] = 1

    for axis, n in folds[:1]:
        n = int(n)
        if axis == "y":
            top = paper[:n, :]
            bottom = paper[2 * n : n : -1, :]
            paper = top | bottom
        else:
            left = paper[:, :n]
            right = paper[:, 2 * n : n : -1]
            paper = left | right

    print(np.count_nonzero(paper))


if __name__ == "__main__":
    solution()
