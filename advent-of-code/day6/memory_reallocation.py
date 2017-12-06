# --- Day 6: Memory Reallocation ---
from datetime import datetime
from typing import List, Set

Memory = List[int]
Cache = Set[str]


def cycle(memory: Memory) -> None:
    length = len(memory)
    index = memory.index(max(memory))
    max_blocks = memory[index]
    memory[index] = 0

    while max_blocks > 0:
        index = (index + 1) % length
        memory[index] += 1
        max_blocks -= 1


def to_string(array: Memory) -> str:
    return ''.join([str(n) for n in array])


def find_cycle(memory: Memory, seen: Cache) -> Cache:
    while to_string(memory) not in seen:
        seen.add(to_string(memory))
        cycle(memory)
    return seen


def main() -> None:
    with open('input.txt', 'r') as fr:
        memory = [int(n) for n in fr.read().strip().split('\t')]

    start = datetime.now()

    seen = find_cycle(memory, set())
    print('Redistribution cycles: {}'.format(len(seen)))

    seen = find_cycle(memory, set())
    print('Cycles: {}'.format(len(seen)))

    end = datetime.now()
    print('Finished in {}s'.format((end - start).total_seconds()))



if __name__ == '__main__':
    main()
