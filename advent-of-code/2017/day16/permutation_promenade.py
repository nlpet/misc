# --- Day 16: Permutation Promenade ---

from string import ascii_lowercase
from typing import List


def perform_moves(moves: List[str], progs: List[str]) -> List[str]:
    for move in moves:
        if move[0] == 's':
            x = int(move[1:])
            progs = progs[-x:] + progs[:-x]
        elif move[0] == 'x':
            a, b = map(int, move[1:].split('/'))
            progs[a], progs[b] = progs[b], progs[a]
        else:
            ch1, ch2 = move[1:].split('/')
            a, b = progs.index(ch1), progs.index(ch2)
            progs[a], progs[b] = progs[b], progs[a]

    return progs


def main() -> None:
    repeats = 44
    progs = list(ascii_lowercase[:16])

    with open('input.txt', 'r') as fr:
        moves = fr.read().strip().split(',')

    progs = perform_moves(moves, progs)
    print('Part 1: {}'.format(''.join(progs)))

    for i in range((int(1e9) % repeats) - 1):
        progs = perform_moves(moves, progs)

    print('Part 2: {}'.format(''.join(progs)))


if __name__ == '__main__':
    main()
