def has_two_adj_digits(s):
    for i in range(1, 6):
        if s[i - 1] == s[i]:
            return True
    return False


def is_in_ascending_order(s):
    return s == "".join(sorted(s))


def main():
    n_passwords = 0
    puzzle_input = "178416-676461"
    start, end = map(int, puzzle_input.split("-"))

    for n in range(start, end + 1):
        s = str(n)
        if has_two_adj_digits(s) and is_in_ascending_order(s):
            n_passwords += 1

    print("Different passwords meeting criteria {}".format(n_passwords))


if __name__ == "__main__":
    main()
