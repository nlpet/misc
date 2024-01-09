import numpy as np


def viewing_distance(height, row):
    d = 0
    for th in row:
        if th < height:
            d += 1
        elif th >= height:
            d += 1
            break
    return d


def solve():
    with open("input.txt") as fr:
        trees = np.array([[int(h) for h in line.strip()] for line in fr.readlines()])

    h, l = len(trees), len(trees[0])

    scenic_scores = []

    for row in range(1, h - 1):
        for col in range(1, l - 1):
            height = trees[row, col]

            vd_up = viewing_distance(height, trees[:row, col][::-1])
            vd_down = viewing_distance(height, trees[row + 1 :, col])
            vd_left = viewing_distance(height, trees[row, :col][::-1])
            vd_right = viewing_distance(height, trees[row, col + 1 :])

            score = vd_up * vd_down * vd_left * vd_right
            scenic_scores.append(score)

    print(max(scenic_scores))


if __name__ == "__main__":
    solve()
