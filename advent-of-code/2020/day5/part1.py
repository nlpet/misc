def find_seat(chars, s, e, h):
    for c in chars[:-1]:
        if c == h:
            e -= int(round((e - s) / 2))
        else:
            s += int(round((e - s) / 2))

    return s if chars[-1] == h else e


def get_seat_id(row, col):
    return row * 8 + col


def main():
    max_seat_id = 0
    with open("input.txt", "r") as fr:
        for line in fr.readlines():
            boarding_pass = line.strip()
            row = find_seat(boarding_pass[:-3], 0, 127, "F")
            col = find_seat(boarding_pass[-3:], 0, 7, "L")
            seat_id = get_seat_id(row, col)
            if seat_id > max_seat_id:
                max_seat_id = seat_id

    print("Highest seat ID on a boarding pass is {}".format(max_seat_id))


if __name__ == "__main__":
    main()
