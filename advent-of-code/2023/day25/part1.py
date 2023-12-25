from collections import defaultdict, Counter
from random import choice
from operator import mul
from functools import reduce
import networkx as nx


def read_graph(filename):
    graph = defaultdict(list)

    with open(filename) as fr:
        for line in fr.readlines():
            node, connected = line.strip().split(": ")
            connected = connected.split(" ")
            graph[node].extend(connected)

            for c in connected:
                graph[c].append(node)
    return graph


def read_graph_nodes_edges(filename):
    nodes, edges = set(), set()

    with open(filename) as fr:
        for line in fr.readlines():
            node, connected = line.strip().split(": ")
            connected = connected.split(" ")
            nodes.update([node] + connected)

            for c in connected:
                edges.add((node, c))
                edges.add((c, node))

    return nodes, edges


def find_subgraphs(graph, cut):
    label_idx = 0
    nodes = set([n for lst in graph.values() for n in lst + list(graph.keys())])
    labelled_nodes = {k: None for k in nodes}
    unlabelled_nodes = len(labelled_nodes)

    while unlabelled_nodes > 0:
        node = choice(list([n for n, l in labelled_nodes.items() if l is None]))
        stack = [node]
        seen = set()

        while stack:
            node = stack.pop()
            seen.add(node)

            if labelled_nodes[node] is not None:
                continue

            labelled_nodes[node] = label_idx
            unlabelled_nodes -= 1

            for c in graph[node]:
                if (node, c) in cut or (c, node) in cut:
                    continue

                if labelled_nodes[c] is None and c not in seen:
                    stack.append(c)
                    seen.add(c)

        label_idx += 1

    return labelled_nodes, label_idx


def hash(cut):
    return tuple(sorted([tuple(sorted(t)) for t in cut]))


def search(sorted_edges, edges, cut, seen):
    for edge in cut:
        for n1, n2 in sorted_edges:
            if (n1, n2) in cut or (n2, n1) in cut:
                continue

            new_cut = cut - {edge} | {(n1, n2)}
            cut_id = hash(new_cut)

            if cut_id in seen:
                continue

            seen.add(cut_id)
            labelled_nodes, n_labels = find_subgraphs(edges, new_cut)

            if n_labels == 2:
                c = Counter(labelled_nodes.values())
                sg_sizes = [v for k, v in c.items()]
                total = reduce(mul, sg_sizes, 1)
                return total


def solve():
    filename = "input.txt"
    graph = read_graph(filename)
    _, edges = read_graph_nodes_edges(filename)

    k = 3
    max_iter = 5
    seen = set()

    g = nx.Graph()
    g.add_edges_from(edges)
    bs = nx.edge_betweenness_centrality(g)
    sorted_edges = [t[0] for t in sorted(bs.items(), key=lambda x: x[1], reverse=True)]
    offset = 0

    for _ in range(max_iter):
        cut = set(sorted_edges[offset : offset + k])
        offset += 1
        cut_id = hash(cut)

        if cut_id in seen:
            continue

        seen.add(cut_id)
        labelled_nodes, n_labels = find_subgraphs(graph, cut)

        if n_labels == 2:
            c = Counter(labelled_nodes.values())
            sg_sizes = [v for k, v in c.items()]
            total = reduce(mul, sg_sizes, 1)
            print(total)
            break

        res = search(sorted_edges, edges, cut, seen)
        if res is not None:
            print(res)
            break


if __name__ == "__main__":
    solve()
