# --- Day 1: No Time for a Taxicab ---
# 0 for North (Up)
# 1 for East (Right)
# 2 of South (Down)
# 3 for West (Left)

from operator import add
from math import fabs
from typing import Set, Tuple, List


Coordinate = Tuple[int, int]
CoordinatesSet = Set[Coordinate]
CoordinatesList = List[Coordinate]


def get_distance(x: int, y: int) -> int:
    return int(fabs(x) + fabs(y))


def orient(facing: int, direction: str) -> int:
    if direction[0] == 'R':
        return (facing + 1) % 4
    return (facing - 1) % 4


def find_loc(coords: CoordinatesList, visited: CoordinatesSet) -> bool:
    for coord in coords:
        if coord in visited:
            print(('\nFirst location visited twice is'
                   ' {} blocks away'.format(get_distance(*coord))))
            return True
        visited.add(coord)
    return False


def move(directions: List[str]) -> None:
    facing, x, y = 0, 0, 0
    found = False
    visited: CoordinatesSet = set()

    for direction in directions:
        steps = int(direction[1:])
        facing = orient(facing, direction)

        if facing == 0:
            coords = [(x, y) for y in range(y + 1, y + steps + 1)]
            y += steps
        elif facing == 1:
            coords = [(x, y) for x in range(x + 1, x + steps + 1)]
            x += steps
        elif facing == 2:
            coords = [(x, y) for y in range(y - steps, y)]
            y -= steps
        else:
            coords = [(x, y) for x in range(x - steps, x)]
            x -= steps

        if not found:
            found = find_loc(coords, visited)

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
