# --- Day 13: A Maze of Twisty Little Cubicles ---

from typing import Tuple


Coord = Tuple[int, int]


def is_open_space(x: int, y: int, fav: int) -> bool:
    return bin(x*x + 3*x + 2*x*y + y + y*y + fav).count('1') % 2 == 0


def mark_coordinate(curr: Coord, fav: int, start: Coord, goal: Coord) -> str:
    symbol = None
    if curr == start:
        symbol = 'S'
    elif curr == goal:
        symbol = 'E'
    else:
        if is_open_space(curr[0], curr[1], fav):
            symbol = u'\u00B7'
        else:
            symbol = u"\u25CF"

    return '{:>2}'.format(symbol)


def print_layout(n: int, fav: int, start: Coord, goal: Coord) -> None:
    cols = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print('\n {}'.format(''.join(['{:>2}'.format(str(x)) for x in cols[:n]])))
    for y in range(n - 3):
        row = ''.join([mark_coordinate((x, y), fav, start, goal)
                       for x in range(n)])
        print('{}{}'.format(cols[y], row))


def main() -> None:
    size = 50
    fav = 1358
    start = (1, 1)
    goal = (31, 39)
    print_layout(size, fav, start, goal)


if __name__ == '__main__':
    main()
