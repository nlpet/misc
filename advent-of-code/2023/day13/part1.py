import numpy as np


def process_pattern(line):
    pattern = [[1 if c == "#" else 0 for c in row] for row in line.split("\n")]
    return np.array(pattern)


def reflection(pattern, rows):
    for idx in range(1, rows):
        size = min(rows - idx, idx)
        patt1 = pattern[idx - size : idx]
        patt2 = np.flip(pattern[idx : idx + size], axis=0)
        if (patt1 == patt2).all():
            return idx
    return 0


def solve():
    with open("input.txt") as fr:
        patterns = [process_pattern(line) for line in fr.read().split("\n\n")]

    n_cols, n_rows = 0, 0

    for pattern in patterns:
        rows, cols = pattern.shape
        n_rows += reflection(pattern, rows)
        n_cols += reflection(np.rot90(pattern, -1), cols)

    print(f"Answer: {n_cols + 100 * n_rows}")


if __name__ == "__main__":
    solve()
