# --- Day 6: Memory Reallocation ---
import numpy as np
from datetime import datetime


def cycle(memory):
    length = memory.size
    index = np.argmax(memory)
    max_blocks = memory[index]
    memory[index] = 0

    if max_blocks >= length:
        div = max_blocks // length
        memory += div
        max_blocks -= div * length

    while max_blocks > 0:
        index = (index + 1) % length
        memory[index] += 1
        max_blocks -= 1

    # if max_blocks > 0:
    #     if index + max_blocks >= l:
    #         to_end = np.arange(index + 1, l)
    #         from_start = np.arange(0, max_blocks - to_end.size)
    #         indices = np.concatenate((from_start, to_end))
    #     else:
    #         indices = np.arange(index + 1, index + 1 + max_blocks)
    #
    #     memory[indices] += 1


def find_cycle(memory, seen):
    while np.array_str(memory) not in seen:
        seen.add(np.array_str(memory))
        cycle(memory)
    return seen


def main():
    with open('input.txt', 'r') as fr:
        memory = np.array([int(n) for n in fr.read().strip().split('\t')])

    start = datetime.now()

    seen = find_cycle(memory, set())
    print('Redistribution cycles: {}'.format(len(seen)))

    seen = find_cycle(memory, set())
    print('Cycles: {}'.format(len(seen)))

    end = datetime.now()
    print('Finished in {}s'.format((end - start).total_seconds()))



if __name__ == '__main__':
    main()
