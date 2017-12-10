# --- Day 10: Balance Bots ---

from collections import defaultdict
from typing import List
from functools import reduce
from operator import mul


def main() -> None:
    bins = {'bot': defaultdict(list),
            'input': defaultdict(list),
            'output': defaultdict(list)}
    actions = defaultdict(list)
    target = (17, 61)
    outputs = ('0', '1', '2')
    result = 1

    with open('input.txt', 'r') as fr:
        for line in fr.readlines():
            instr = line.strip().split(' ')
            if len(instr) == 6:
                bins['bot'][instr[-1]].append(int(instr[1]))
            else:
                actions[instr[1]].append({
                    'low': (instr[5], instr[6]),
                    'high': (instr[-2], instr[-1])
                })

    bots_with_actions = [k for k, v in bins['bot'].items() if len(v) == 2]

    while bots_with_actions:
        bot_with_action = bots_with_actions.pop()
        low, high = sorted(bins['bot'][bot_with_action])

        if low == target[0] and high == target[1]:
            print('Bot with microships {} is {}'.format(target,
                                                        bot_with_action))

        bins['bot'][bot_with_action] = []
        action = actions[bot_with_action].pop()
        bins[action['low'][0]][action['low'][1]].append(low)
        bins[action['high'][0]][action['high'][1]].append(high)

        if action['low'][0] == 'bot' and \
           len(bins['bot'][action['low'][1]]) == 2:
            bots_with_actions.append(action['low'][1])
        if action['high'][0] == 'bot' and \
           len(bins['bot'][action['high'][1]]) == 2:
            bots_with_actions.append(action['high'][1])

    print('Result for Part 2 is {}'.format(
        reduce(mul, [bins['output'][o][0] for o in outputs])))


if __name__ == '__main__':
    main()
