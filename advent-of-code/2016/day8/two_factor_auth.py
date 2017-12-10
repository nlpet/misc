# --- Day 8: Two-Factor Authentication ---

import re
import numpy as np


def main() -> None:
    screen = np.zeros((6, 50))
    with open('input.txt', 'r') as fr:
        for line in fr.readlines():
            instr = line.strip().split(' ')
            if instr[0] == 'rect':
                x, y = map(int, instr[1].split('x'))
                screen[:y, :x] = 1
            elif instr[1] == 'column':
                col, by = int(instr[2][2:]), int(instr[-1])
                screen[:, col] = np.roll(screen[:, col], by)
            elif instr[1] == 'row':
                row, by = int(instr[2][2:]), int(instr[-1])
                screen[row] = np.roll(screen[row], by)

    print('Number of pixels lit: {}\n'.format(int(np.sum(screen))))
    mapper = {'1': '#', '0': '.'}

    for row in screen:
        print(''.join([mapper[str(int(x))] for x in row]))


if __name__ == '__main__':
    main()
