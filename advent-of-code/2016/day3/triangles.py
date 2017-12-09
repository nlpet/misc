# --- Day 3: Squares With Three Sides ---

import numpy as np
from typing import List


def is_triangle(a: int, b: int, c: int) -> bool:
    return a + b > c and a + c > b and b + c > a


def find_valid_triangles(triangles: List[List[int]]) -> int:
    return sum([1 for t in triangles if is_triangle(*t)])


def main() -> None:
    with open('input.txt', 'r') as fr:
        lines = [[int(n) for n in line.strip().split()]
                 for line in fr.readlines()]

    valid1 = find_valid_triangles(lines)

    nplines = np.array(lines)
    triangles = nplines.T.reshape(nplines.shape)
    valid2 = find_valid_triangles(triangles)

    print('Valid triangles (Part 1): {}'.format(valid1))
    print('Valid triangles (Part 2): {}'.format(valid2))



if __name__ == '__main__':
    main()
