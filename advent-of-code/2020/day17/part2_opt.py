from itertools import product, chain
from collections import Counter
import numpy as np


def get_adjacent():
    adjacent = (-1, 0, 1)
    neighbours = list(product(adjacent, adjacent, adjacent, adjacent))
    neighbours.remove((0, 0, 0, 0))

    return np.array(neighbours)


def main():
    cycles = 6
    adjacent = get_adjacent()
    active_cubes = set([])

    with open("input.txt", "r") as fr:
        for y, line in enumerate(fr.readlines()):
            for x, state in enumerate(line.strip()):
                if state == "#":
                    active_cubes.add((x, y, 0, 0))

    for _ in range(cycles):
        next_active_cubes = set([])
        adjacent_cubes = []

        for cube in active_cubes:
            adj = [tuple(a) for a in (adjacent + cube)]
            adjacent_cubes.append(adj)
            num_active = 0
            for a in adj:
                if tuple(a) in active_cubes:
                    num_active += 1

            if num_active in {2, 3}:
                next_active_cubes.add(cube)

        adjacent_cubes = [*chain.from_iterable(adjacent_cubes)]
        adj_counts = Counter(adjacent_cubes)

        for c in adj_counts:
            if c not in active_cubes and adj_counts[c] == 3:
                next_active_cubes.add(c)

        active_cubes = next_active_cubes

    print(len(active_cubes))


if __name__ == "__main__":
    main()
