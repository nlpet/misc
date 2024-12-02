def solve():
    lst1, lst2 = [], []

    with open("input.txt") as fr:
        for line in fr.readlines():
            n1, n2 = [int(x) for x in line.strip().split()]
            lst1.append(n1)
            lst2.append(n2)

    total = 0

    for a, b in zip(sorted(lst1), sorted(lst2)):
        total += abs(a - b)

    print(f"Answer: {total}")


if __name__ == "__main__":
    solve()
