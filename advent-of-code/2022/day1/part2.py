def solve():
    elves_cals = []

    with open("input.txt") as fr:
        for line in fr.read().strip().split("\n\n"):
            cals = sum([int(n) for n in line.split("\n")])
            elves_cals.append(cals)

    total = sum(sorted(elves_cals, reverse=True)[:3])
    print(total)


if __name__ == "__main__":
    solve()
