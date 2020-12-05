import numpy as np


def display_plane(plane, rows, cols):
    for i in range(cols):
        for j in range(rows):
            print(".", end="") if plane[j][i] == 0 else print("x", end="")
        print()


def find_seat(chars, s, e, h):
    for c in chars[:-1]:
        if c == h:
            e -= int(round((e - s) / 2))
        else:
            s += int(round((e - s) / 2))

    return s if chars[-1] == h else e


def get_seat_id(row, col):
    return row * 8 + col


def generate_seat_ids(rows, cols):
    seat_ids = set([])
    for i in range(rows + 1):
        for j in range(cols + 1):
            seat_ids.add(get_seat_id(i, j))

    return seat_ids


def main():
    rows, cols = 127, 7
    possible_seat_ids = generate_seat_ids(rows, cols)
    found_seat_ids = set([])
    with open("input.txt", "r") as fr:
        for line in fr.readlines():
            boarding_pass = line.strip()
            row = find_seat(boarding_pass[:-3], 0, 127, "F")
            col = find_seat(boarding_pass[-3:], 0, 7, "L")
            found_seat_ids.add(get_seat_id(row, col))

    for seat_id in possible_seat_ids.difference(found_seat_ids):
        if seat_id - 1 in found_seat_ids and seat_id + 1 in found_seat_ids:
            print(seat_id)
            break


if __name__ == "__main__":
    main()
