import numpy as np


def show(terrain_map):
    m = {0: ".", 1: "#", -1: "X"}
    for row in terrain_map:
        print("".join([m[c] for c in row]))


def solve():
    dm = {"0": "R", "1": "D", "2": "L", "3": "U"}
    moves = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}

    coords = [(0, 0)]
    boundary_points = 0

    with open("input.txt") as fr:
        for line in fr.readlines():
            _, _, code = line.split()
            code = code[2:-1]
            n = int(code[:-1], 16)
            d = dm[code[-1]]
            dr, dc = moves[d]
            row, col = coords[-1]
            coords.append((row + dr * n, col + dc * n))
            boundary_points += n

    l = len(coords)
    area = [
        coords[i][0] * (coords[i - 1][1] - coords[(i + 1) % l][1]) for i in range(l)
    ]
    area = abs(sum(area)) // 2
    interior = area - boundary_points // 2 + 1
    print(interior + boundary_points)


if __name__ == "__main__":
    solve()
