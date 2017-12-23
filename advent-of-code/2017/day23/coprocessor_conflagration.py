# --- Day 23: Coprocessor Conflagration ---


from collections import defaultdict
from string import ascii_lowercase
from typing import Set


def get(y: str, reg_names: Set[str], registers: defaultdict) -> int:
    if y in reg_names:
        return registers[y]
    return int(y)


def is_prime(n: int) -> bool:
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(n ** 0.5) + 1, 2))


def main():
    n, h, index = 0, 0, 0
    reg_names = set(ascii_lowercase[:8])
    registers = defaultdict(int)

    with open('input.txt', 'r') as fr:
        instructions = [l.strip().split(' ') for l in fr.readlines()]

    while 0 <= index < len(instructions):
        op, x, y = instructions[index]
        v = get(y, reg_names, registers)

        if op == 'set':
            registers[x] = v
        elif op == 'sub':
            registers[x] -= v
        elif op == 'mul':
            registers[x] *= v
            n += 1
        elif op == 'jnz':
            vx = get(x, reg_names, registers)
            if vx != 0:
                index += v - 1

        index += 1

    for i in range(109900, 126901, 17):
        if not is_prime(i):
            h += 1

    print('Number of times the mul instruction was invoked is {}'.format(n))
    print('The value left in register h is {}'.format(h))


if __name__ == '__main__':
    main()
