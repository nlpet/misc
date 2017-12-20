# --- Day 18: Duet ---

from typing import Any, Dict


Registers = Dict[str, Any]


def get_value(val: str, regs: Registers) -> int:
    try:
        return int(val)
    except ValueError:
        return regs.get(val, 0)


def main():
    with open('input.txt', 'r') as fr:
        instructions = [line.strip().split(' ') for
                        line in fr.readlines()]

    regs: Registers = {'sounds': []}
    length = len(instructions)
    i = 0

    while 0 <= i < length:
        ins = instructions[i]
        if ins[0] == 'set':
            regs[ins[1]] = get_value(ins[2], regs)
        elif ins[0] == 'snd':
            freq = regs.get(ins[1], -1)
            regs['sounds'].append(freq)
            print('Play sound with frequency {}'.format(freq))
        elif ins[0] == 'add':
            regs[ins[1]] = regs.get(ins[1], 0) + get_value(ins[2], regs)
        elif ins[0] == 'mul':
            regs[ins[1]] = regs.get(ins[1], 0) * get_value(ins[2], regs)
        elif ins[0] == 'mod':
            regs[ins[1]] = regs[ins[1]] % get_value(ins[2], regs)
        elif ins[0] == 'rcv':
            if get_value(ins[1], regs):
                print('Recover {}'.format(regs['sounds'].pop()))
                break
        elif ins[0] == 'jgz':
            val = get_value(ins[1], regs)
            if val > 0:
                i = (i + get_value(ins[2], regs)) % length - 1

        i += 1

    print('Done')


if __name__ == '__main__':
    main()
