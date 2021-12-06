# --- Day 20: Jurassic Jigsaw ---

from collections import defaultdict
from math import prod


def main():
    with open("input.txt") as fr:
        tiles = [tile.split("\n") for tile in fr.read().split("\n\n")]

    reference = {}

    for tile in tiles:
        tid = int(tile[0].split("Tile ")[1][:-1])
        reference[tid] = {
            "top": tile[1],
            "bottom": tile[-1],
            "left": "".join([row[0] for row in tile[1:]]),
            "right": "".join([row[-1] for row in tile[1:]]),
        }

    matches = defaultdict(lambda: defaultdict(set))

    for t1, bs1 in reference.items():
        for t2, bs2 in reference.items():
            if t1 == t2:
                continue

            for b1, s1 in bs1.items():
                for b2, s2 in bs2.items():
                    if s1 == s2:
                        matches[t1][t2].add(f"{b1}.{b2}")
                        matches[t2][t1].add(f"{b2}.{b1}")
                    elif s1 == s2[::-1]:
                        matches[t1][t2].add(f"{b1}.{b2}[flipped]")
                        matches[t2][t1].add(f"{b2}[flipped].{b1}")
                    elif s1[::-1] == s2:
                        matches[t1][t2].add(f"{b1}[flipped].{b2}")
                        matches[t2][t1].add(f"{b2}.{b1}[flipped]")

    corner_tiles = [k for k, v in matches.items() if len(v) == 2]
    print(prod(corner_tiles))


if __name__ == "__main__":
    main()
