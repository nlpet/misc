# --- Day 2: Bathroom Security ---

from operator import add
from math import fabs
from typing import Set, Tuple, List, Union, Any


Keypad = List[List[Any]]
Code = List[Any]


keypad1: Keypad = [
    [0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 4, 5, 6, 0],
    [0, 7, 8, 9, 0],
    [0, 0, 0, 0]
]

keypad2: Keypad = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 2, 3, 4, 0, 0],
    [0, 5, 6, 7, 8, 9, 0],
    [0, 0, 'A', 'B', 'C', 0, 0],
    [0, 0, 0, 'D', 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]


def list_to_str(lst: Code) -> str:
    return ''.join([str(n) for n in lst])


def move(keypad: Keypad, d: str, i: int, j: int) -> Tuple[int, int]:
    if d == 'U' and keypad[i - 1][j] != 0:
        i -= 1
    elif d == 'D' and keypad[i + 1][j] != 0:
        i += 1
    elif d == 'L' and keypad[i][j - 1] != 0:
        j -= 1
    elif d == 'R' and keypad[i][j + 1] != 0:
        j += 1
    return i, j


def main() -> None:
    i, j, m, n = 1, 1, 3, 1
    code1: Code = []
    code2: Code = []

    with open('input.txt', 'r') as fr:
        for line in fr.readlines():
            for d in line.strip():
                i, j = move(keypad1, d, i, j)
                m, n = move(keypad2, d, m, n)
            code1.append(keypad1[i][j])
            code2.append(keypad2[m][n])

        print('Code 1: {}'.format(list_to_str(code1)))
        print('Code 2: {}'.format(list_to_str(code2)))


if __name__ == '__main__':
    main()
