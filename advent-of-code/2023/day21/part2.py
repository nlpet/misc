from collections import deque
import numpy as np


def show(plot, visited, h, l):
    for i in range(h):
        row = ["O" if (i, j) in visited else plot[i][j] for j in range(l)]
        print("".join(row))


def solve():
    with open("input.txt") as fr:
        plot = [[c for c in line.strip()] for line in fr.readlines()]

    h, l = len(plot), len(plot[0])
    ((row, col),) = [(r, c) for r in range(h) for c in range(l) if plot[r][c] == "S"]
    plot[row][col] = "."

    visited = []
    tovisit = deque([(row, col)])
    tovisit_next = set()

    points = []

    for step in range(int(3 * h) + 1):
        visited_step = []
        while len(tovisit) > 0:
            row, col = tovisit.popleft()
            visited_step.append((row, col))
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = row + dr, col + dc
                if plot[nr % h][nc % l] == ".":
                    tovisit_next.add((nr, nc))
        tovisit = deque(tovisit_next)
        tovisit_next = set()
        visited = visited_step

        if step % h == h // 2:
            points.append(len(visited))

        if len(points) == 3:
            break

    n_steps = 26501365
    n = n_steps // h
    coeffs = np.polyfit(range(len(points)), points, 2)
    result = np.polyval(coeffs, n)
    print(round(result))


if __name__ == "__main__":
    solve()
