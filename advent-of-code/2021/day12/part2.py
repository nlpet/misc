# --- Day 12: Passage Pathing ---

from collections import defaultdict, Counter
import time


def find_paths(graph, start, end, path=[]):
    path = path + [start]
    cp = Counter([p for p in path if p == p.lower() and p not in {"start", "end"}])
    visited, count = None, 0

    if len(cp):
        visited, count = cp.most_common(1)[0]

    if start == end:
        return [path]

    paths = []

    for node in graph[start]:
        if count > 1:
            if node == visited or (node == node.lower() and node in path):
                continue

        subpaths = find_paths(graph, node, end, path)
        paths.extend(subpaths)

    return paths


def solution():
    graph = defaultdict(list)

    with open("input.txt") as fr:
        for line in fr.readlines():
            a, b = line.strip().split("-")

            if a != "end" and b != "start":
                graph[a].append(b)

            if b != "end" and a != "start":
                graph[b].append(a)

    paths = find_paths(graph, "start", "end")
    print(len(paths))


if __name__ == "__main__":
    solution()
