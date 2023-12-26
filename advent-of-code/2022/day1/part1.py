def solve():
    most = 0

    with open("input.txt") as fr:
        for line in fr.read().strip().split("\n\n"):
            cals = sum([int(n) for n in line.split("\n")])
            most = cals if cals > most else most

    print(most)


if __name__ == "__main__":
    solve()
