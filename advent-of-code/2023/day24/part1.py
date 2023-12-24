from itertools import combinations


def parse(line):
    pos, vel = line.strip().split(" @ ")
    pos = [int(n) for n in pos.split(", ")]
    vel = [int(n) for n in vel.split(", ")]
    return pos, vel


def solve():
    with open("input.txt") as fr:
        hailstones = [parse(line) for line in fr.readlines()]

    bs, be = 200000000000000, 400000000000000
    n = 0

    for h1, h2 in combinations(hailstones, 2):
        (p1x, p1y, _), (v1x, v1y, _) = h1
        (p2x, p2y, _), (v2x, v2y, _) = h2

        if (v1x * v2y - v1y * v2x) == 0 or (v2x * v1y - v2y * v1x) == 0:
            continue

        t1 = (v2y * (p2x - p1x) - v2x * (p2y - p1y)) / (v1x * v2y - v1y * v2x)
        t2 = (v1y * (p1x - p2x) - v1x * (p1y - p2y)) / (v2x * v1y - v2y * v1x)

        if t1 < 0 or t2 < 0:
            continue

        x1, y1 = (round(p1x + v1x * t1), round(p1y + v1y * t1))

        if bs <= x1 <= be and bs <= y1 <= be:
            n += 1

    print(n)


if __name__ == "__main__":
    solve()
