# --- Day 1: No Time for a Taxicab ---
# 0 for North (Up)
# 1 for East (Right)
# 2 of South (Down)
# 3 for West (Left)

from operator import add
from math import fabs
from typing import Set, Tuple, List


def get_distance(x: int, y: int) -> int:
    return int(fabs(x) + fabs(y))


def move(directions: List[str]) -> None:
    facing, x, y = 0, 0, 0

    for direction in directions:
        steps = int(direction[1:])
        if direction[0] == 'R':
            facing = (facing + 1) % 4
        elif direction[0] == 'L':
            facing = (facing - 1) % 4
        if facing == 0:
            y += steps
        elif facing == 1:
            x += steps
        elif facing == 2:
            y -= steps
        else:
            x -= steps

    dist = get_distance(x, y)
    num_steps = len(directions)
    print('After {} steps, position is {}'.format(steps, dist))


def main() -> None:
    with open('input.txt', 'r') as fr:
        for line in fr.readlines():
            directions = line.strip().split(', ')
            move(directions)


if __name__ == '__main__':
    main()
