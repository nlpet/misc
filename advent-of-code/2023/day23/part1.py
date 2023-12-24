import heapq


def is_downhill(grid, dr, dc, row, col):
    mapping = {(0, 1): ">", (1, 0): "v", (0, -1): "<", (-1, 0): "^"}
    return mapping[(dr, dc)] == grid[row][col]


def is_uphill(grid, dr, dc, row, col):
    mapping = {(0, 1): "<", (1, 0): "^", (0, -1): ">", (-1, 0): "v"}
    return mapping[(dr, dc)] == grid[row][col]


def show(grid, p, h, l):
    for row in range(h):
        print("".join([" " if (row, col) in p else grid[row][col] for col in range(l)]))


def solve():
    with open("input.txt") as fr:
        grid = [row.strip() for row in fr.readlines()]

    h, l = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    start = (0, 1)
    goal = (h - 1, l - 2)

    # priority, path length, current position, is previous position uphill, visited
    queue = [(0, 0, start, False, set())]

    is_out_of_bounds = lambda nr, nc: nr < 0 or nr == h or nc < 0 or nc == l
    paths = []

    while queue:
        priority, steps, (row, col), prev_uphill, visited = heapq.heappop(queue)

        if (row, col) == goal:
            paths.append(visited)
            continue

        for dr, dc in directions:
            nr, nc = row + dr, col + dc

            if is_out_of_bounds(nr, nc) or (nr, nc) in visited or grid[nr][nc] == "#":
                continue

            visited.add((row, col))
            uphill = is_uphill(grid, dr, dc, nr, nc)
            state = (priority - 1, steps + 1, (nr, nc), uphill, set(visited))

            if prev_uphill and not is_downhill(grid, dr, dc, nr, nc):
                continue

            heapq.heappush(queue, state)

    path_lengths = [len(p) for p in paths]
    print(max(path_lengths))

    # for p in paths:
    #     print(f"Path with length {len(p)}")
    #     show(grid, p, h, l)
    #     print()


if __name__ == "__main__":
    solve()
