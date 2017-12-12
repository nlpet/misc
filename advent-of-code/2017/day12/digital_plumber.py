# --- Day 12: Digital Plumber ---

from collections import defaultdict
from typing import List


def main() -> None:
    group = defaultdict(set)

    with open('input.txt', 'r') as fr:
        for line in fr.readlines():
            left, right = line.split('<->')
            program = int(left.strip())
            programs = [int(x) for x in right.strip().split(', ')]
            group[program] = group[program].union(set(programs))

    visited = [0 for _ in range(len(group))]
    all_programs = set(group.keys())
    target_part1 = 0
    connected_to_target_part1 = set([target_part1])
    num_groups = 0

    while all_programs:
        target = all_programs.pop()
        visited[target] = 1
        stack: List[int] = list(group[target])
        connected_to_target = set([target])
        while stack:
            connected = stack.pop()
            if not visited[connected]:
                connected_to_target.add(connected)
                visited[connected] = 1

            for connection in group[connected]:
                if not visited[connection]:
                    stack.append(connection)
                    visited[connected] = 1

            if target == target_part1:
                connected_to_target_part1 = connected_to_target

        all_programs = all_programs.difference(connected_to_target)
        num_groups += 1

    print(('Number of programs in the group that contain '
           'program ID 0 are {} '.format(len(connected_to_target_part1))))
    print('There are {} groups'.format(num_groups))


if __name__ == '__main__':
    main()
