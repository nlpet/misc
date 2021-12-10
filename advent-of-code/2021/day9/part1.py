# --- Day 9: Smoke Basin ---


def is_low_point(heightmap, i, j, n_rows, n_cols):
    modifiers = [(0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)]
    points = [
        heightmap[i + m1][j + m2]
        for m1, m2 in modifiers
        if 0 <= i + m1 < n_rows and 0 <= j + m2 < n_cols
    ]

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
                low_points.append(point)

    return low_points


def solution():
    with open("input.txt") as fr:
        heightmap = [[int(n) for n in line.strip()] for line in fr.readlines()]

    low_points = find_low_points(heightmap)
    risk_levels = [n + 1 for n in low_points]

    print(f"The sum of the risk levels of all low points is {sum(risk_levels)}")


if __name__ == "__main__":
    solution()
