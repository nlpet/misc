# --- Day 4: Security Through Obscurity ---

import re
from collections import Counter
from string import ascii_lowercase
from typing import List, Any

Name = List[str]


def is_real_room(name: Name) -> str:
    all_letters = Counter(''.join(name))
    most_common = all_letters.most_common()
    result, stack, lsc = [], [], 0

    for l, c in most_common:
        if not stack or c == lsc:
            stack.append(l)
            lsc = c
        else:
            result.extend(sorted(stack))
            lsc = c
            stack = [l]

    result.extend(sorted(stack))
    return ''.join(result[:5])


def shift_letter(l: str, sector_id: int) -> str:
    index = ascii_lowercase.index(l)
    new_index = (index + (sector_id % 26)) % 26
    return ascii_lowercase[new_index]


def decrypt(name: Name, sector_id: int) -> str:
    decrypted = [[shift_letter(c, sector_id) for c in w] for w in name]
    return ' '.join([''.join(w) for w in decrypted])


def find_north_pole_object_storage(name: Name, sector_id: int) -> int:
    decrypted = decrypt(name, sector_id)
    if decrypted.find('north') != -1:
        return sector_id


def main() -> None:
    north_pole = None
    sum_sector_ids = 0
    room_reg = re.compile(r'([a-z0-9]+)')

    with open('input.txt', 'r') as fr:
        for line in fr.readlines():
            ps = room_reg.findall(line.strip())
            name, sector_id, checksum = ps[:-2], int(ps[-2]), ps[-1]
            expected_checksum = is_real_room(name)
            if north_pole is None:
                north_pole = find_north_pole_object_storage(name, sector_id)

            if expected_checksum == checksum:
                sum_sector_ids += sector_id

    print('Sum of sector IDs: {}'.format(sum_sector_ids))
    print('North Pole object storage: {}'.format(north_pole))


if __name__ == '__main__':
    main()
