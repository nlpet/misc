# --- Day 25: The Halting Problem ---

import numpy as np
from typing import Dict, Tuple, Any


Blueprint = Dict[str, Tuple[Tuple[int, int, str]]]


def main() -> None:
    steps, state = 12317297, 'A'
    tape = np.zeros(steps, dtype=np.int)
    cursor = tape.size // 2
    blueprint: Blueprint = {
        'A': ((1, 1, 'B'),  (0, -1, 'D')),
        'B': ((1, 1, 'C'),  (0, 1, 'F')),
        'C': ((1, -1, 'C'), (1, -1, 'A')),
        'D': ((0, -1, 'E'), (1, 1, 'A')),
        'E': ((1, -1, 'A'), (0, 1, 'B')),
        'F': ((0, 1, 'C'),  (0, 1, 'E')),
    }

    for _ in range(steps):
        value, move, state = blueprint[state][tape[cursor]]
        tape[cursor] = value
        cursor += move

    print('The diagnostic checksum is {}'.format(np.sum(tape)))


if __name__ == '__main__':
    main()
