from itertools import product
import numpy as np


def is_cube_active(is_currently_active, neighbours, dim, dim_size):
    active_neighbours = 0
    for i, j, k, l in neighbours:
        if active_neighbours > 3:
            return False
        if (
            0 <= i < dim_size
            and 0 <= j < dim_size
            and 0 <= k < dim_size
            and 0 <= l < dim_size
        ):
            if dim[i, j, k, l]:
                active_neighbours += 1

    conditions = [
        is_currently_active and active_neighbours in {2, 3},
        not is_currently_active and active_neighbours == 3,
    ]

    return any(conditions)


def main():
    dim_size = 23
    middle = dim_size // 2 - 1
    dim = np.zeros((dim_size, dim_size, dim_size, dim_size), dtype=int)
    adjacent = (-1, 0, 1)
    neighbours = list(product(adjacent, adjacent, adjacent, adjacent))
    neighbours.remove((0, 0, 0, 0))
    neighbours = np.array(neighbours)

    with open("input.txt", "r") as fr:
        for y, line in enumerate(fr.readlines()):
            for x, state in enumerate(line.strip()):
                dim[(y + middle, x + middle, middle, middle)] = state == "#"

    for _ in range(6):
        tdim = dim.copy()
        for i in range(dim_size):
            for j in range(dim_size):
                for k in range(dim_size):
                    for l in range(dim_size):
                        tdim[i, j, k, l] = is_cube_active(
                            dim[i, j, k, l],
                            neighbours + [i, j, k, l],
                            dim,
                            dim_size,
                        )

        dim = tdim.copy()

    print(dim.sum())


if __name__ == "__main__":
    main()
