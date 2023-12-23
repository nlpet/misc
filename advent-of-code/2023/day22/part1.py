import numpy as np


def move_brick(grid, brick, y, h, l, d):
    for offset in range(h - y - 1):
        yp = y + offset
        mask = grid[yp] == brick
        is_overlapping = (grid[yp][mask] * grid[yp + 1][mask]).any()
        if is_overlapping:
            return

        ys, zs = np.where(grid[yp] == brick)
        grid[yp + 1, ys, zs] = grid[yp, ys, zs]
        grid[yp, ys, zs] = 0


def play_forward(grid):
    h, l, d = grid.shape
    for y in range(h - 2, -1, -1):
        for brick in [b for b in np.unique(grid[y]) if b > 0]:
            move_brick(grid, brick, y, h, l, d)


def count_disintegratable(grid):
    h, _, _ = grid.shape
    bricks = set([])

    for y in range(h - 1, 0, -1):
        support = {}
        level = grid[y]
        above = grid[y - 1]
        for brick in [b for b in np.unique(level) if b > 0]:
            mask = level == brick
            is_overlapping = (level[mask] * above[mask]).any()

            if not is_overlapping:
                if brick not in support:
                    support[brick] = set([])

                bricks.add(brick)
                continue

            # find where it is overlapping to find which bricks
            ys, zs = np.where(level * above != 0)
            for x, z in zip(ys, zs):
                b, ba = level[x, z], above[x, z]
                if b not in support:
                    support[b] = set([])
                support[b].add(ba)

        for brick, sb in support.items():
            if len(sb) == 0:
                bricks.add(brick)

            other_supports = set([])
            other_bricks = [k for k in support.keys() if k != brick]
            for ob in other_bricks:
                other_supports.update(sb.intersection(support[ob]))

            if sb == other_supports:
                bricks.add(brick)

    return len(bricks)


def solve():
    bricks = []

    with open("input.txt") as fr:
        xl, yl, zl = 0, 0, 0
        for i, line in enumerate(fr.readlines()):
            fst, snd = line.split("~")
            x, y, z = [int(n) for n in fst.split(",")]
            x1, y1, z1 = [int(n) for n in snd.split(",")]
            bricks.append((i + 1, (x, x1), (y, y1), (z, z1)))

            xl = max(xl, x, x1)
            yl = max(yl, y, y1)
            zl = max(zl, z, z1)

    grid = np.zeros((zl + 1, xl + 1, yl + 1), dtype=int)

    for label, (x1, x2), (z1, z2), (y1, y2) in bricks:
        grid[y1 : y2 + 1, x1 : x2 + 1, z1 : z2 + 1] = label

    grid = np.flip(grid, axis=0)[:-1]

    play_forward(grid)
    n = count_disintegratable(grid)
    print(f"Answer: {n}")


if __name__ == "__main__":
    solve()
