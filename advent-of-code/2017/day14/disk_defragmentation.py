# --- Day 14: Disk Defragmentation --

from typing import List, Any
from functools import partial, reduce
from operator import xor
import numpy as np
from scipy.ndimage import label


def hex_to_binary(s: str, scale: int, bits: int) -> str:
    return ''.join(map(lambda ch: bin(int(ch, scale))[2:].zfill(bits), s))


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


def generate_knot_hash(s: str) -> str:
    lengths = [ord(ch) for ch in s] + [17, 31, 73, 47, 23]
    sparse_hash = execute_rounds(64, lengths)
    dense_hash = get_dense_hash(sparse_hash)
    return ''.join(['{0:02x}'.format(n) for n in dense_hash])


def main() -> None:
    # Test input: flqrgnkx
    puzzle_input = 'uugsqrei'
    used = 0
    arr = []

    for i in range(128):
        s = puzzle_input + '-{}'.format(i)
        b = hex_to_binary(generate_knot_hash(s), 32, 4)
        used += b.count('1')
        arr.append([int(ch) for ch in b])

    _, num_regions = label(np.array(arr))

    print('Number of used squares is {}'.format(used))
    print('Number of regions are {}'.format(num_regions))


if __name__ == '__main__':
    main()
