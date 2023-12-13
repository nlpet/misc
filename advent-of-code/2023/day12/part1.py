def arrangements(springs, groups):
    if len(groups) == 0:
        return int(all(s != "#" for s in springs))

    if len(springs) < sum(groups):
        return 0

    if springs[0] == ".":
        return arrangements(springs[1:], groups)

    first_group_unk = all(s != "." for s in springs[: groups[0]])
    unk = first_group_unk and (
        len(springs) > groups[0]
        and springs[groups[0]] != "#"
        or len(springs) <= groups[0]
    )

    first = arrangements(springs[groups[0] + 1 :], groups[1:]) if unk else 0
    after = arrangements(springs[1:], groups) if springs[0] == "?" else 0

    return first + after


def solve():
    counts = 0
    with open("input.txt") as fr:
        for line in fr.readlines():
            springs, groups = line.strip().split(" ")
            groups = tuple(map(int, groups.split(",")))
            counts += arrangements(springs, groups)

    print(f"Answer: {counts}")


if __name__ == "__main__":
    solve()
