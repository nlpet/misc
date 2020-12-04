def main():
    with open("input.txt", "r") as fr:
        grid = [line.strip() for line in fr.readlines()]

    current = (0, 0)
    step = (3, 1)
    num_trees = 0
    n_rows = len(grid)
    n_cols = len(grid[0])

    while current[1] < n_rows:
        x, y = current
        if grid[y][x] == "#":
            num_trees += 1

        current = ((x + step[0]) % n_cols, y + step[1])

    print(f"Trees encountered: {num_trees}")


if __name__ == "__main__":
    main()
