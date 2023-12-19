import numpy as np


def show(terrain_map):
    m = {0: ".", 1: "#", -1: "X"}
    for row in terrain_map:
        print("".join([m[c] for c in row]))


def mark_exterior(terrain, moves):
    queue = [(0, 0)]
    seen = set()
    marked = np.copy(terrain)

    while queue:
        row, col = queue.pop()

        if (
            (row, col) in seen
            or row < 0
            or row >= len(terrain)
            or col < 0
            or col >= len(terrain[0])
            or terrain[row][col] == 1
        ):
            continue

        seen.add((row, col))

        if terrain[row][col] == 0:
            marked[row][col] = -1

        for dr, dc in moves.values():
            queue.append((row + dr, col + dc))

    return marked


def solve():
    with open("input.txt") as fr:
        plan = [t.strip().split(" ") for t in fr.readlines()]

    coords = set()
    row, col = 0, 0
    moves = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}

    for dir, l, _ in plan:
        dr, dc = moves[dir]
        for _ in range(int(l)):
            coords.add((row, col))
            row += dr
            col += dc

    min_row = abs(min([k[0] for k in coords]))
    min_col = abs(min([k[1] for k in coords]))
    coords = [(row + min_row, col + min_col) for row, col in coords]

    h = max([k[0] for k in coords]) + 1
    l = max([k[1] for k in coords]) + 1
    terrain = np.array(
        [
            [1 if (i, j) in coords else 0 for j in range(-1, l + 1)]
            for i in range(-1, h + 1)
        ]
    )

    marked = mark_exterior(terrain, moves)
    marked[marked == 0] = 1
    marked[marked == -1] = 0

    print(marked.sum())


if __name__ == "__main__":
    solve()
