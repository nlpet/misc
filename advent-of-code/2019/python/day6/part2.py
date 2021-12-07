# --- Day 6: Universal Orbit Map ---

from collections import defaultdict


def get_path(orbits, start):
    path, dist = {}, 0
    while orbits.get(start):
        path[orbits.get(start)] = dist
        start = orbits.get(start)
        dist += 1

    return path


def find_number_of_transfers(p1, p2):
    for o, d in p1.items():
        if p2.get(o) is not None:
            return d + p2.get(o)


def solution():
    orbits = defaultdict(str)

    with open("input.txt") as fr:
        for line in fr.readlines():
            obj, orbiter = line.strip().split(")")
            orbits[orbiter] = obj

    you_path = get_path(orbits, "YOU")
    san_path = get_path(orbits, "SAN")

    n_transfers = find_number_of_transfers(you_path, san_path)
    print(f"Minimum number of orbital transfers: {n_transfers}")


if __name__ == "__main__":
    solution()
