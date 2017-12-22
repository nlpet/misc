# --- Day 21: Fractal Art ---

import numpy as np
from typing import Set, Tuple, Dict


Matrix = np.ndarray
ImmutableArray = Tuple[Tuple[int]]
Rules = Dict[ImmutableArray, np.ndarray]

PIXELS_TO_BINARY = {'#': 1, '.': 0}


def to_tuple(matrix: Matrix) -> ImmutableArray:
    return tuple(map(tuple, matrix))


def get_variations(pattern: Matrix) -> Set[Matrix]:
    all_variations = set([])
    for i in range(4):
        all_variations.add(to_tuple(pattern))
        all_variations.add(to_tuple(np.flip(pattern, 0)))
        all_variations.add(to_tuple(np.flip(pattern, 1)))
        pattern = np.rot90(pattern)
    return all_variations


def to_matrix(image: str) -> Matrix:
    return np.array([[PIXELS_TO_BINARY[ch] for ch in row]
                     for row in image.split('/')])


def apply_enchancement(matrix: Matrix, rules: Rules) -> Matrix:
    block_size = 2 if matrix.shape[0] % 2 == 0 else 3
    blocks = divide_into_blocks(matrix, block_size)
    step = matrix.shape[0] // block_size
    enchanced_patterns = np.array([rules[to_tuple(m)] for m in blocks])
    whole_pattern = [np.hstack(enchanced_patterns[i:i+step])
                     for i in range(0, len(blocks), step)]
    return np.vstack(np.array(whole_pattern))


def divide_into_blocks(m: Matrix, n: int) -> Matrix:
    h, w = m.shape
    return (m.reshape(h // n, n, -1, n)
             .swapaxes(1, 2)
             .reshape(-1, n, n))


def main():
    rules = {}
    pattern = np.array([[0, 1, 0],
                        [0, 0, 1],
                        [1, 1, 1]])

    with open('input.txt', 'r') as fr:
        for rule in fr.readlines():
            images = rule.strip().split(' => ')
            before = to_tuple(to_matrix(images[0]))
            after = to_matrix(images[1])
            rules.update({patt: after for patt in get_variations(before)})

    for i in range(18):
        pattern = apply_enchancement(pattern, rules)

    print(np.sum(pattern))


if __name__ == '__main__':
    main()
