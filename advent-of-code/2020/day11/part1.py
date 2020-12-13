from copy import deepcopy


def display_layout(layout):
    for row in layout:
        print("".join(row))

    print()


def count_adj_occupied(layout, row, col, n_rows, n_cols):
    adjacent_seats = [
        (i, j) for j in range(col - 1, col + 2) for i in range(row - 1, row + 2)
    ]

    n_occupied = 0

    for i, j in adjacent_seats:
        if 0 <= i < n_rows and 0 <= j < n_cols and (i, j) != (row, col):
            if layout[i][j] == "#":
                n_occupied += 1

    return n_occupied


def main():
    with open("input.txt", "r") as fr:
        layout = [list(line.strip()) for line in fr.readlines()]

    n_rows, n_cols = len(layout), len(layout[0])
    current_layout = deepcopy(layout)

    while 1:
        n_changes = 0
        n_total_occupied = 0
        # display_layout(current_layout)

        for i in range(n_rows):
            for j in range(n_cols):
                n_occupied = count_adj_occupied(layout, i, j, n_rows, n_cols)
                if layout[i][j] == "L" and n_occupied == 0:
                    current_layout[i][j] = "#"
                    n_changes += 1
                elif layout[i][j] == "#" and n_occupied >= 4:
                    current_layout[i][j] = "L"
                    n_changes += 1

                if current_layout[i][j] == "#":
                    n_total_occupied += 1

        layout = deepcopy(current_layout)

        if n_changes == 0:
            print(n_total_occupied)
            break


if __name__ == "__main__":
    main()
