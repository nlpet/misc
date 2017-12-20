# --- Day 19: A Series of Tubes ---

import numpy as np
from string import ascii_uppercase
from typing import Tuple, Dict, List


Grid = np.ndarray
Row = np.ndarray
Col = np.ndarray
Coord = Tuple[int, int]
LetterCoords = Dict[Coord, str]
Word = List[str]


def get(grid: Grid, row: Row, col: Col):
    try:
        return grid[row][col]
    except IndexError:
        return None


def deal_with_crossroads(row: Row, col: Col, grid: Grid,
                         pd: str) -> Tuple[int, int, str]:
    if pd in {'up', 'down'}:
        if get(grid, row, col - 1):
            return row, col - 1, 'left'
        else:
            return row, col + 1, 'right'
    else:
        if get(grid, row - 1, col):
            return row - 1, col, 'up'
        else:
            return row + 1, col, 'down'


def is_out_of_bounds(grid: Grid, row: Row, col: Col) -> bool:
    l, w = grid.shape
    if row < 0 or row >= l or col < 0 or col >= w or grid[row][col] == 0:
        return True
    return False


def walk(grid: Grid, start: Coord, pd: str,
         lcoords: LetterCoords) -> Tuple[Word, int]:
    word: Word = []
    steps = 0

    row, col = start
    dirs: Dict[str, function] = {
        'down': lambda x, y: (x + 1, y),
        'up': lambda x, y: (x - 1, y),
        'left': lambda x, y: (x, y - 1),
        'right': lambda x, y: (x, y + 1)
    }

    while True:
        cell = grid[row][col]
        if is_out_of_bounds(grid, row, col):
            return word, steps
        if cell == 1:
            row, col = dirs[pd](row, col)
        elif cell == 2:
            row, col, pd = deal_with_crossroads(row, col, grid, pd)
        elif cell == 3:
            word.append(lcoords[(row, col)])
            row, col = dirs[pd](row, col)
        steps += 1


def main() -> None:
    diagram = []
    elements = {'|': 1, '-': 1, '+': 2}
    lcoords = {}
    letters = set(ascii_uppercase)
    cols_lengths = []

    with open('input.txt', 'r') as fr:
        for line in fr.readlines():
            diagram.append(line)
            cols_lengths.append(len(line))

    rows = len(diagram)
    cols = max(cols_lengths)
    grid = np.zeros((rows, cols), dtype=np.int)

    for row, line in enumerate(diagram):
        for col, ch in enumerate(line):
            if ch in letters:
                lcoords[(row, col)] = ch
                grid[row][col] = 3
            else:
                grid[row][col] = elements.get(ch, 0)

    start = (0, grid[0].argmax())
    word, steps = walk(grid, start, 'down', lcoords)
    print('Answer is {}, with {} steps'.format(''.join(word), steps))


if __name__ == '__main__':
    main()
