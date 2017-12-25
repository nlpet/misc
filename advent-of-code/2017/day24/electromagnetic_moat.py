# --- Day 24: Electromagnetic Moat ---

from collections import defaultdict
from operator import itemgetter
from typing import Dict, Set, Tuple, Optional


Graph = Dict[int, Set[int]]
Bridge = Tuple[Set[Tuple[int, int]], int, int, int]


def get_all_bridges(graph: Graph, bridge: Bridge=None):
    comps, a, strength, length = bridge or (set(), 0, 0, 0)

    for b in graph[a]:
        next_comp = (b, a) if b > a else (a, b)

        if next_comp not in comps:
            new_comps = comps.union({next_comp})
            new_bridge = (new_comps, b, strength + a + b, length + 1)
            yield new_bridge
            yield from get_all_bridges(graph, new_bridge)


def main() -> None:
    graph: Graph = defaultdict(set)

    with open('input.txt', 'r') as fr:
        for line in fr.readlines():
            a, b = map(int, line.strip().split('/'))
            graph[b].add(a)
            graph[a].add(b)

    bridges = [bridge[2:] for bridge in get_all_bridges(graph)]
    strongest = sorted(bridges)[-1][0]
    longest = sorted(bridges, key=itemgetter(1))[-1][0]

    print('Strength of the strongest bridge is {}'.format(strongest))
    print('Strength of the longest bridge is {}'.format(longest))


if __name__ == '__main__':
    main()
