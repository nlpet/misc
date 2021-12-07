# --- Day 6: Universal Orbit Map ---

from collections import defaultdict


def solution():
    orbits = defaultdict(str)

    with open("input.txt") as fr:
        for line in fr.readlines():
            obj, orbiter = line.strip().split(")")
            orbits[orbiter] = obj

    n_orbits = 0

    for os in orbits.values():
        n_orbits += 1
        o = os

        while orbits.get(o):
            n_orbits += 1
            o = orbits.get(o)

    print(f"Total number of direct and indirect orbits is {n_orbits}")


if __name__ == "__main__":
    solution()
