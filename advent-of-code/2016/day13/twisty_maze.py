# --- Day 13: A Maze of Twisty Little Cubicles ---

from typing import List, Tuple, Set


def is_wall(x: int, y: int, inp: int):
    result = x ** 2 + y ** 2 + 2 * x * y + 3 * x + y + inp
    ones = bin(result).count('1')
    return ones % 2 == 1


def surronding_cells(x: int, y: int) -> List[Tuple[int, int]]:
    return [(x + 1, y), (x, y + 1),
            (x - 1, y), (x, y - 1)]


def invalid_cell(x: int, y: int, inp: int, visited: Set[Tuple[int, int]]):
    return x < 0 or y < 0 or is_wall(x, y, inp) or (x, y) in visited


def main():
    inp = 1358
    goal = (31, 39)
    steps, completed = 0, 0
    visited = {(1, 1)}
    locations = visited

    while completed < 2:
        to_visit = locations.copy()
        locations = set([])
        for x, y in to_visit:
            for n, m in surronding_cells(x, y):
                if invalid_cell(n, m, inp, visited):
                    continue
                visited.add((n, m))
                locations.add((n, m))
        steps += 1

        if goal in locations:
            print('Number of steps to {} is {}'.format(goal, steps))
            completed += 1
        if steps == 50:
            n = len(visited)
            print('Number of new locations within 50 steps is {}'.format(n))
            completed += 1


if __name__ == '__main__':
    main()
