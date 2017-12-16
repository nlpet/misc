# --- Day 14: One-Time Pad ---

from collections import defaultdict
from hashlib import md5
from typing import Union, List, DefaultDict, Tuple
from bisect import insort


Hashes = List[int]
Cache = DefaultDict[str, Hashes]


def find_x_in_a_row(h: str, n: int) -> Union[str, None]:
    for i in range(len(h) - (n - 1)):
        if len(set(h[i: i + n])) == 1:
            return h[i]
    return None


def main() -> None:
    salt = 'qzyelonm'
    hashes_found = 0
    hash_indices: Hashes = []
    threes_in_a_row: Cache = defaultdict(list)
    index = 0

    while hashes_found <= 64 or index - hash_indices[-1] >= 1000:
        h = md5('{}{}'.format(salt, index).encode()).hexdigest()

        # Part 2
        for _ in range(2016):
            h = md5(h.encode()).hexdigest()

        fives_char = find_x_in_a_row(h, 5)
        threes_char = find_x_in_a_row(h, 3)

        if fives_char is not None:
            for j in threes_in_a_row[fives_char]:
                if index - j <= 1000:
                    insort(hash_indices, j)
                    hashes_found += 1
            threes_in_a_row[fives_char] = []

        if threes_char is not None:
            threes_in_a_row[threes_char].append(index)

        index += 1

    print(hash_indices[63])


if __name__ == '__main__':
    main()
