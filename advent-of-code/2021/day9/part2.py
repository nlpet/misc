# --- Day 9: Smoke Basin ---

import numpy as np


ALL_MODIFIERS = [
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]

NON_DIAGONAL_MODIFIERS = [
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
]


def find_adjacent_points(i, j, n_rows, n_cols, diagonal=True):
    modifiers = ALL_MODIFIERS if diagonal else NON_DIAGONAL_MODIFIERS
    return [
        (i + m1, j + m2)
        for m1, m2 in modifiers
        if 0 <= i + m1 < n_rows and 0 <= j + m2 < n_cols
    ]


def is_low_point(heightmap, i, j, n_rows, n_cols):
    points = find_adjacent_points(i, j, n_rows, n_cols)
    points = [heightmap[x][y] for x, y in points]

    if all([heightmap[i][j] < p for p in points]):
        return True

    return False


def find_low_points(heightmap):
    n_rows, n_cols = len(heightmap), len(heightmap[0])
    low_points = []
    for i in range(n_rows):
        for j in range(n_cols):
            point = heightmap[i][j]
            if point != 9 and is_low_point(heightmap, i, j, n_rows, n_cols):
                low_points.append((i, j))

    return low_points


def find_basin(heightmap, i, j, visited):
    stack = [(i, j)]
    n_rows, n_cols = len(heightmap), len(heightmap[0])
    size_of_basin = 1

    while stack:
        i, j = stack.pop()
        points = find_adjacent_points(i, j, n_rows, n_cols, False)

        for x, y in points:
            if (x, y) in visited:
                continue

            if heightmap[x][y] == 9:
                visited.add((x, y))
            elif heightmap[x][y] > heightmap[i][j]:
                size_of_basin += 1
                visited.add((x, y))
                stack.append((x, y))

    return size_of_basin


def find_basins(heightmap, low_points):
    return [find_basin(heightmap, i, j, set([])) for i, j in low_points]


def solution():
    with open("input.txt") as fr:
        heightmap = [[int(n) for n in line.strip()] for line in fr.readlines()]

    low_points = find_low_points(heightmap)
    basins = find_basins(heightmap, low_points)
    three_largest_basins = sorted(basins, reverse=True)[:3]
    print(np.prod(three_largest_basins))


if __name__ == "__main__":
    solution()
