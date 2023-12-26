def process(pair):
    s, e = map(int, pair.split("-"))
    sections = set(list(range(s, e + 1)))
    return sections


def solve():
    total = 0
    with open("input.txt") as fr:
        for line in fr.readlines():
            p1, p2 = line.strip().split(",")
            p1, p2 = process(p1), process(p2)
            overlap = p1 & p2
            is_contained = overlap == p1 if len(p1) < len(p2) else overlap == p2
            total += int(is_contained)

    print(total)


if __name__ == "__main__":
    solve()
