# --- Day 7: Recursive Circus ---
import re
from collections import Counter
from typing import List, Dict, Tuple

Children = Dict[str, Tuple[List[str], int]]


def get_weights_mismatch(root: str, children: Children) -> int:
    expected_weight = None
    root_weight = children[root][1]
    for child in children[root][0]:
        child_weight = get_weights_mismatch(child, children)
        root_weight += child_weight
        if expected_weight is None:
            expected_weight = child_weight
        elif expected_weight != child_weight:
            diff = children[child][1] - (child_weight - expected_weight)
            print(child, diff)

    return root_weight


def main() -> None:
    stack = []
    towers_children = {}
    towers_children_count = {}
    structures_reg = re.compile(r'(\w+)\s(\(\d+\))(\s->\s(.+))*')

    with open('input.txt', 'r') as fr:
        for line in fr.readlines():
            match = structures_reg.match(line)
            if match:
                groups = match.groups()
                tower, weight = groups[0], int(groups[1][1:-1])
                children = groups[3].split(', ') if groups[3] else []
                towers_children[tower] = (children, weight)
                towers_children_count[tower] = len(children)

    for tower, children_and_weights in towers_children.items():
        for child in children_and_weights[0]:
            towers_children_count[tower] += towers_children_count[child]
            stack.extend(towers_children[child][0])

        while stack:
            child = stack.pop()
            towers_children_count[tower] += towers_children_count[child]
            stack.extend(towers_children[child][0])

    root = Counter(towers_children_count).most_common(1)[0][0]
    print('The name of the bottom program is "{}"\n'.format(root))

    get_weights_mismatch(root, towers_children)


if __name__ == '__main__':
    main()
