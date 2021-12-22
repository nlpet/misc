# --- Day 11: Dumbo Octopus ---

from collections import defaultdict
from os import readlink


MODIFIERS = [(0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)]


def distribute_flashes(i, j, grid, flashed, n_rows, n_cols):
    for m1, m2 in MODIFIERS:
        m, n = i + m1, j + m2
        if (m, n) not in flashed and 0 <= m < n_rows and 0 <= n < n_cols:
            grid[m][n] += 1

            if grid[m][n] > 9:
                flashed.add((m, n))
                grid[m][n] = 0
                distribute_flashes(m, n, grid, flashed, n_rows, n_cols)


def solution():
    with open("input.txt") as fr:
        grid = [[int(n) for n in line.strip()] for line in fr.readlines()]

    n_steps = 500
    n_rows, n_cols = len(grid), len(grid[0])
    flashes = 0
    octopuses = n_rows * n_cols

    for step in range(n_steps):
        flashed = set([])
        for i in range(n_rows):
            for j in range(n_cols):
                if (i, j) in flashed:
                    continue

                grid[i][j] += 1

                if grid[i][j] > 9:
                    flashed.add((i, j))
                    grid[i][j] = 0
                    distribute_flashes(i, j, grid, flashed, n_rows, n_cols)

        flashes += len(flashed)

        if len(flashed) == octopuses:
            print(f"All octopuses will flash at step {step + 1}")
            break


if __name__ == "__main__":
    solution()
