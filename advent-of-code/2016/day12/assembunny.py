# --- Day 12: Leonardo's Monorail ---

from collections import defaultdict


def main() -> None:
    with open('input.txt', 'r') as fr:
        instructions = [line.strip().split(' ') for line in fr.readlines()]

    registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    index = 0
    num_instructions = len(instructions)

    while index < num_instructions:
        instr = instructions[index]
        if instr[0] == 'inc':
            registers[instr[1]] += 1
            index += 1
        elif instr[0] == 'dec':
            registers[instr[1]] -= 1
            index += 1
        elif instr[0] == 'jnz':
            if instr[1] == '1' or registers.get(instr[1], 0):
                index += int(instr[2])
            else:
                index += 1
        elif instr[0] == 'cpy':
            if registers.get(instr[1], None) is not None:
                registers[instr[2]] = registers[instr[1]]
            else:
                registers[instr[2]] = int(instr[1])
            index += 1

    print(registers['a'])


if __name__ == '__main__':
    main()
