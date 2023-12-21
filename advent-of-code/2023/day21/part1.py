def show(plot, visited, h, l):
    for i in range(h):
        row = ["O" if (i, j) in visited else plot[i][j] for j in range(l)]
        print("".join(row))


def solve():
    with open("input.txt") as fr:
        plot = [[c for c in line.strip()] for line in fr.readlines()]

    h, l = len(plot), len(plot[0])
    ((row, col),) = [
        (row, col) for row in range(h) for col in range(l) if plot[row][col] == "S"
    ]
    plot[row][col] = "."

    visited = []
    tovisit = [(row, col)]

    tovisit_next = set()

    for step in range(65):
        visited_step = []
        while len(tovisit) > 0:
            row, col = tovisit.pop(0)
            visited_step.append((row, col))
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = row + dr, col + dc
                if nr >= 0 and nr < h and nc >= 0 and nc < l and plot[nr][nc] == ".":
                    tovisit_next.add((nr, nc))
        tovisit = list(tovisit_next)
        tovisit_next = set()
        visited.append(visited_step)

    show(plot, visited[-1], h, l)
    print(len(visited[-1]))


if __name__ == "__main__":
    solve()
