def display_platform(platform):
    for i in range(len(platform)):
        print("".join(platform[i]))


def roll_north(platform, l, h):
    for col_idx in range(l):
        for row_idx in range(1, h):
            if platform[row_idx][col_idx] == "O":
                roll_idx = row_idx
                while roll_idx > 0 and platform[roll_idx - 1][col_idx] == ".":
                    platform[roll_idx - 1][col_idx] = "O"
                    platform[roll_idx][col_idx] = "."
                    roll_idx -= 1


def roll_west(platform, l, h):
    for row_idx in range(h):
        for col_idx in range(1, l):
            if platform[row_idx][col_idx] == "O":
                roll_idx = col_idx
                while roll_idx > 0 and platform[row_idx][roll_idx - 1] == ".":
                    platform[row_idx][roll_idx - 1] = "O"
                    platform[row_idx][roll_idx] = "."
                    roll_idx -= 1


def roll_south(platform, l, h):
    for col_idx in range(l):
        for row_idx in range(h - 1, -1, -1):
            if platform[row_idx][col_idx] == "O":
                roll_idx = row_idx
                while roll_idx + 1 < h and platform[roll_idx + 1][col_idx] == ".":
                    platform[roll_idx + 1][col_idx] = "O"
                    platform[roll_idx][col_idx] = "."
                    roll_idx += 1


def roll_east(platform, l, h):
    for row_idx in range(h):
        for col_idx in range(l - 1, -1, -1):
            if platform[row_idx][col_idx] == "O":
                roll_idx = col_idx
                while roll_idx + 1 < l and platform[row_idx][roll_idx + 1] == ".":
                    platform[row_idx][roll_idx + 1] = "O"
                    platform[row_idx][roll_idx] = "."
                    roll_idx += 1


def spin(platform, l, h):
    roll_north(platform, l, h)
    roll_west(platform, l, h)
    roll_south(platform, l, h)
    roll_east(platform, l, h)


def total_load(platform, h):
    tl = 0
    for row_idx in range(h):
        tl += sum([c == "O" for c in platform[row_idx]]) * (h - row_idx)
    return tl


def solve():
    with open("input.txt") as fr:
        platform = [[r for r in line.strip()] for line in fr.readlines()]

    l, h = len(platform[0]), len(platform)

    seen = {}
    cycles = 1000000000
    total_loads = {}

    for i in range(cycles):
        spin(platform, l, h)

        platform_hash = tuple(tuple(p) for p in platform)
        if platform_hash in seen:
            seen[platform_hash].append(i)
            total_loads[i] = total_load(platform, h)
            break
        else:
            seen[platform_hash] = [i]
            total_loads[i] = total_load(platform, h)

    start_idx, end_idx = seen[platform_hash]
    idx = start_idx + (cycles - start_idx) % (end_idx - start_idx) - 1
    tl = total_loads[idx]

    print(f"Answer: {tl}")


if __name__ == "__main__":
    solve()
