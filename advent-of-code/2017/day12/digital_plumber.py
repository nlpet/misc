# --- Day 12: Digital Plumber ---

from collections import defaultdict
from typing import List


def main() -> None:
    group = defaultdict(set)
    target = 0

    with open('test.txt', 'r') as fr:
        for line in fr.readlines():
            left, right = line.split('<->')
            program = int(left.strip())
            programs = [int(x) for x in right.strip().split(', ')]
            group[program] = group[program].union(set(programs))

    stack: List[int] = list(group[target])
    connected_to_target = set()
    visited = [0 for _ in range(len(group))]

    while stack:
        connected = stack.pop()
        if not visited[connected]:
            connected_to_target.add(connected)
            visited[connected] = 1

        for connection in group[connected]:
            if not visited[connection]:
                stack.append(connection)
                visited[connected] = 1

    print(('Number of programs in the group that contain '
           'program ID 0 are {} '.format(len(connected_to_target))))


if __name__ == '__main__':
    main()
