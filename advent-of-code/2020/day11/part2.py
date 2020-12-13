from copy import deepcopy
from functools import partial


def display_layout(layout):
    for row in layout:
        print("".join(row))

    print()


def count_first(layout, row, col, n_rows, n_cols, inc_row, inc_col):
    curr_row, curr_col = row + inc_row, col + inc_col
    while 1:
        if 0 <= curr_row < n_rows and 0 <= curr_col < n_cols:
            seat = layout[curr_row][curr_col]
            if seat == "L":
                return 0
            if seat == "#":
                return 1

            curr_row += inc_row
            curr_col += inc_col
        else:
            return 0


def count_occupied(layout, row, col, n_rows, n_cols):
    cfn = partial(count_first, layout, row, col, n_rows, n_cols)

    seen_seats = [
        cfn(-1, -1),
        cfn(-1, 0),
        cfn(-1, 1),
        cfn(0, -1),
        cfn(0, 1),
        cfn(1, -1),
        cfn(1, 0),
        cfn(1, 1),
    ]

    return sum(seen_seats)


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
                n_occupied = count_occupied(layout, i, j, n_rows, n_cols)
                if layout[i][j] == "L" and n_occupied == 0:
                    current_layout[i][j] = "#"
                    n_changes += 1
                elif layout[i][j] == "#" and n_occupied >= 5:
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
