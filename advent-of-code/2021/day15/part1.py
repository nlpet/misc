# --- Day 15: Chiton ---

from heapq import heappush, heappop
import numpy as np


def solution():
    with open("input.txt") as fr:
        risk_map = [[int(n) for n in line.strip()] for line in fr.readlines()]

    n_rows, n_cols = len(risk_map), len(risk_map[0])

    psx = {(row, col) for row in range(n_rows) for col in range(n_cols)}
    adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    grid = np.zeros((n_rows, n_cols), dtype=int)
    pos = [(0, (0, 0))]

    while pos:
        _, (row, col) = heappop(pos)

        if (row, col) not in psx:
            continue

        psx.remove((row, col))

        p = [(row + dr, col + dc) for dr, dc in adj if (row + dr, col + dc) in psx]

        for dr, dc in p:
            if not grid[dr][dc] or grid[row][col] + risk_map[dr][dc] < grid[dr][dc]:
                grid[dr][dc] = grid[row][col] + risk_map[dr][dc]
                heappush(pos, (grid[dr][dc], (dr, dc)))

    print(grid[-1][-1])


if __name__ == "__main__":
    solution()
