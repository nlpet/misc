def solve():
    lst = []
    lookup = {}

    with open("input.txt") as fr:
        for line in fr.readlines():
            n1, n2 = [int(x) for x in line.strip().split()]
            lst.append(n1)

            if lookup.get(n2) is None:
                lookup[n2] = 0

            lookup[n2] += 1

    similarity_score = 0

    for n in lst:
        similarity_score += n * lookup.get(n, 0)

    print(f"Answer: {similarity_score}")


if __name__ == "__main__":
    solve()
