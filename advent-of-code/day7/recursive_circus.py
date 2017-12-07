# --- Day 7: Recursive Circus ---
import re
from collections import Counter
from typing import List, Set


def invert_map(d):
    return {v: k for k, v in d.items()}


def main() -> None:
    stack = []
    towers_children = {}
    towers_children_count = {}
    towers_weight_count = {}
    structures_reg = re.compile(r'(\w+)\s(\(\d+\))(\s->\s(.+))*')

    with open('test.txt', 'r') as fr:
        for line in fr.readlines():
            match = structures_reg.match(line)
            if match:
                groups = match.groups()
                tower, weight = groups[0], int(groups[1][1:-1])
                children = groups[3].split(', ') if groups[3] else []
                towers_children[tower] = (children, weight)
                towers_children_count[tower] = len(children)
                towers_weight_count[tower] = weight

    for tower, children_and_weights in towers_children.items():
        for child in children_and_weights[0]:
            towers_children_count[tower] += towers_children_count[child]
            towers_weight_count[tower] += towers_weight_count[child]
            stack.extend(towers_children[child][0])

        while stack:
            child = stack.pop()
            towers_children_count[tower] += towers_children_count[child]
            towers_weight_count[tower] += towers_weight_count[child]
            stack.extend(towers_children[child][0])

    root = Counter(towers_children_count).most_common(1)[0][0]
    print('The name of the bottom program is "{}"'.format(root))



if __name__ == '__main__':
    main()
