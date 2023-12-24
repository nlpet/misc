import heapq
from collections import defaultdict
from time import time


def show(grid, p, h, l):
    mapping = {"#": "■"}
    for r in range(h):
        row = ["x" if (r, c) in p else mapping.get(grid[r][c], ".") for c in range(l)]
        print("".join(row))


def create_graph(grid, h, l, start, end):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    is_out_of_bounds = lambda nr, nc: nr < 0 or nr == h or nc < 0 or nc == l
    junctions = [start, end]

    for row in range(h):
        for col in range(l):
            if grid[row][col] == "#":
                continue

            adjacent = 0
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if not is_out_of_bounds(nr, nc) and grid[nr][nc] != "#":
                    adjacent += 1

                if adjacent >= 3:
                    junctions.append((row, col))

    graph = defaultdict(dict)

    for row, col in junctions:
        stack = [(row, col, 0)]
        visited = {(row, col)}

        while stack:
            r, c, steps = stack.pop()

            if steps != 0 and (r, c) in junctions:
                graph[(row, col)][(r, c)] = steps
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    not is_out_of_bounds(nr, nc)
                    and grid[nr][nc] != "#"
                    and (nr, nc) not in visited
                ):
                    stack.append((nr, nc, steps + 1))
                    visited.add((nr, nc))

    return graph


def longest_path(graph, start, end):
    # priority, path length, current position, visited
    queue = [(-1, 1, start, {start: 0})]
    l = 0

    while queue:
        _, steps, (row, col), visited = heapq.heappop(queue)

        if (row, col) == end:
            if visited[end] - 1 > l:
                l = visited[end] - 1
            continue

        for (nr, nc), ns in graph[(row, col)].items():
            if (nr, nc) in visited:
                continue

            priority = -(ns + steps)
            state = (priority, ns + steps, (nr, nc), {**visited, (nr, nc): ns + steps})
            heapq.heappush(queue, state)

    return l


def solve():
    with open("input.txt") as fr:
        grid = [row.strip() for row in fr.readlines()]

    h, l = len(grid), len(grid[0])

    start = (0, 1)
    end = (h - 1, l - 2)

    graph = create_graph(grid, h, l, start, end)

    l = longest_path(graph, start, end)
    print(f"Answer: {l}")


if __name__ == "__main__":
    solve()
