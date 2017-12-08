# --- Day 8: I Heard You Like Registers ---

import re
from collections import Counter, defaultdict
from operator import add, sub, eq, ne, gt, lt, ge, le
from typing import Dict


def main() -> None:
    registers: Dict[str, int] = defaultdict(int)
    regex = r'(?:(\w+)\s(inc|dec)\s(-?\d+))\sif\s(?:(\w+)\s([!<>=]+)\s(-?\d+))'
    reg = re.compile(regex)
    modifiers = {'inc': add, 'dec': sub}
    conditions = {'>': gt, '<': lt, '==': eq, '!=': ne, '>=': ge, '<=': le}
    highest_ever = 0

    with open('input.txt', 'r') as fr:
        for line in fr.readlines():
            match = reg.match(line)
            if not match:
                print('{} does not contain valid instructions'.format({line}))

            groups = match.groups()
            a, modifier, b, c, condition, d = groups

            if conditions[condition](registers[c], int(d)):
                registers[a] = modifiers[modifier](registers[a], int(b))
                if registers[a] > highest_ever:
                    highest_ever = registers[a]

    highest = Counter(registers).most_common(1)
    print('The highest value in any register is {}'.format(highest))
    print('The highest value ever held is {}'.format(highest_ever))


if __name__ == '__main__':
    main()
