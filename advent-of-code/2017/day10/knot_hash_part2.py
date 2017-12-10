# --- Day 10: Knot Hash ---

from typing import List, Any
from functools import partial, reduce
from operator import xor
import numpy as np


def execute_rounds(rounds: int, lengths: List[int]) -> List[int]:
    lst = np.arange(256)
    index = 0
    skip_size = 0

    for _ in range(rounds):
        for length in lengths:
            if index + length >= lst.size:
                indices = np.concatenate(
                    (np.arange(index, lst.size),
                     np.arange(0, (index + length) % lst.size)))

                lst[indices] = lst[indices][::-1]
            else:
                end = index + length
                lst[index:end] = lst[index: end % lst.size][::-1]

            index = (index + length + skip_size) % lst.size
            skip_size += 1

    return lst


def get_dense_hash(sparse_hash: Any) -> List[int]:
    return map(partial(reduce, xor), sparse_hash.reshape((16, 16)))


def main() -> None:
    with open('input.txt', 'r') as fr:
        lengths = [ord(ch) for ch in fr.read().strip()]
        lengths += [17, 31, 73, 47, 23]

    sparse_hash = execute_rounds(64, lengths)
    dense_hash = get_dense_hash(sparse_hash)

    print(''.join(['{0:02x}'.format(n) for n in dense_hash]))


if __name__ == '__main__':
    main()
