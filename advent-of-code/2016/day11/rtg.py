# --- Day 11: Radioisotope Thermoelectric Generators ---

from typing import List


State = List[List[str]]


def print_state(state: State) -> None:
    width = len(state[0]) * 3
    print('┌' + width * '─' + '┐', flush=True)
    for floor in state:
        fl = '│' + ''.join(['{0:3}'.format(item) for item in floor]) + '│'
        print(fl, flush=True)
    print('└' + width * '─' + '┘', flush=True)


def get_min_steps(inp: List[int]) -> int:
    min_moves = 0
    while inp[-1] != sum(inp):
        floor = 0
        while inp[floor] == 0:
            floor += 1
        min_moves += 2 * (inp[floor] - 1) - 1
        inp[floor + 1] += inp[floor]
        inp[floor] = 0
    return min_moves


def main() -> None:
    inp = [
        ['F4', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['F3', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'TM'],
        ['F2', '.', 'TG', '.', 'RG', '.', 'RM', '.', 'CG', '.', 'CM', '.'],
        ['F1', 'E', '.', 'SG', '.', 'SM', '.', 'PG', '.', 'PM', '.', '.']
    ]

    inp_part1 = [4, 5, 1, 0]
    inp_part2 = [8, 5, 1, 0]

    print_state(inp)
    print('Min number of steps (Part 1): {}'.format(get_min_steps(inp_part1)))
    print('Min number of steps (Part 2): {}'.format(get_min_steps(inp_part2)))


if __name__ == '__main__':
    main()
