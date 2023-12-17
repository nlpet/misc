def display_platform(platform):
    for i in range(len(platform)):
        print("".join(platform[i]))


def solve():
    with open("input.txt") as fr:
        platform = [[r for r in line.strip()] for line in fr.readlines()]

    l, h = len(platform[0]), len(platform)

    for col_idx in range(l):
        for row_idx in range(h):
            if platform[row_idx][col_idx] == "O":
                roll_idx = row_idx
                while roll_idx > 0 and platform[roll_idx - 1][col_idx] == ".":
                    platform[roll_idx - 1][col_idx] = "O"
                    platform[roll_idx][col_idx] = "."
                    roll_idx -= 1

    total_load = 0
    for row_idx in range(h):
        total_load += sum([c == "O" for c in platform[row_idx]]) * (h - row_idx)

    print(f"Answer: {total_load}")


if __name__ == "__main__":
    solve()
