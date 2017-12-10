# --- Day 10: Knot Hash ---

from typing import List
import numpy as np


def main() -> None:
    with open('input.txt', 'r') as fr:
        lengths = [int(n) for n in fr.read().strip().split(',')]

    lst = np.arange(256)
    index = 0
    skip_size = 0

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

    print('The result of multiplying the first two '
          'numbers in the list is {}'.format(lst[0] * lst[1]))




if __name__ == '__main__':
    main()
