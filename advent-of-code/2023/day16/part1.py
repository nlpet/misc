def reflect_down(row, col, h, new_beams):
    if row + 1 < h:
        new_beams.append((row + 1, col, "d"))


def reflect_up(row, col, new_beams):
    if row > 0:
        new_beams.append((row - 1, col, "u"))


def reflect_right(row, col, l, new_beams):
    if col + 1 < l:
        new_beams.append((row, col + 1, "r"))


def reflect_left(row, col, new_beams):
    if col > 0:
        new_beams.append((row, col - 1, "l"))


def move_right(layout, row, col, h, l, new_beams, energised):
    if col == l:
        return

    energised.add((row, col))
    if layout[row][col] == "\\":
        reflect_down(row, col, h, new_beams)
    elif layout[row][col] == "/":
        reflect_up(row, col, new_beams)
    elif layout[row][col] == "|":
        reflect_up(row, col, new_beams)
        reflect_down(row, col, h, new_beams)
    else:
        new_beams.append((row, col + 1, "r"))


def move_left(layout, row, col, h, new_beams, energised):
    if col < 0:
        return

    energised.add((row, col))

    if layout[row][col] == "\\":
        reflect_up(row, col, new_beams)
    elif layout[row][col] == "/":
        reflect_down(row, col, h, new_beams)
    elif layout[row][col] == "|":
        reflect_up(row, col, new_beams)
        reflect_down(row, col, h, new_beams)
    else:
        new_beams.append((row, col - 1, "l"))


def move_down(layout, row, col, h, l, new_beams, energised):
    if row == h:
        return

    energised.add((row, col))

    if layout[row][col] == "\\":
        reflect_right(row, col, l, new_beams)
    elif layout[row][col] == "/":
        reflect_left(row, col, new_beams)
    elif layout[row][col] == "-":
        reflect_left(row, col, new_beams)
        reflect_right(row, col, l, new_beams)
    else:
        new_beams.append((row + 1, col, "d"))


def move_up(layout, row, col, l, new_beams, energised):
    if row < 0:
        return

    energised.add((row, col))

    if layout[row][col] == "\\":
        reflect_left(row, col, new_beams)
    elif layout[row][col] == "/":
        reflect_right(row, col, l, new_beams)
    elif layout[row][col] == "-":
        reflect_left(row, col, new_beams)
        reflect_right(row, col, l, new_beams)
    else:
        new_beams.append((row - 1, col, "u"))


def show(layout):
    for row in layout:
        print("".join(row))


def solve():
    with open("input.txt") as fr:
        layout = [[c for c in l.strip()] for l in fr.readlines()]

    l, h = len(layout), len(layout[0])
    beams = [[0, 0, "r"]]
    energised = set([(0, 0)])
    seen = set([])

    while len(beams) > 0:
        new_beams = []
        for row, col, direction in beams:
            if (row, col, direction) in seen:
                continue
            seen.add((row, col, direction))
            if direction == "r":
                move_right(layout, row, col, h, l, new_beams, energised)
            elif direction == "d":
                move_down(layout, row, col, h, l, new_beams, energised)
            elif direction == "l":
                move_left(layout, row, col, h, new_beams, energised)
            else:
                move_up(layout, row, col, l, new_beams, energised)

        beams = new_beams

    print(len(energised))


if __name__ == "__main__":
    solve()
