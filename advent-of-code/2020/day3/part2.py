def main():
    with open("input.txt", "r") as fr:
        grid = [line.strip() for line in fr.readlines()]

    start = (0, 0)
    steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    result = 1
    n_rows = len(grid)
    n_cols = len(grid[0])

    for step in steps:
        num_trees = 0
        current = start

        while current[1] < n_rows:
            x, y = current
            if grid[y][x] == "#":
                num_trees += 1

            current = ((x + step[0]) % n_cols, y + step[1])

        result *= num_trees

    print(f"Trees encountered: {result}")


if __name__ == "__main__":
    main()
