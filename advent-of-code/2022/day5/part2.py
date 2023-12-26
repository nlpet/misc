import re


def solve():
    with open("input.txt") as fr:
        crates, procedure = fr.read().split("\n\n")

    crates = crates.split("\n")
    crates, n_stacks = crates[:-1], crates[-1]
    n_stacks = len(re.findall(r"(\d+)", n_stacks))

    stacks = [[] for _ in range(n_stacks)]

    for row in crates:
        row = row.replace("    ", " X ").replace("  ", " ").strip().split(" ")
        for idx, c in enumerate(row):
            if c == "X":
                continue

            stacks[idx].insert(0, c[1:-1])

    procedure = procedure.strip().split("\n")

    for p in procedure:
        n, start, finish = map(int, re.findall(r"(\d+)", p))
        to_move = stacks[start - 1][-n:]
        stacks[start - 1] = stacks[start - 1][:-n]
        stacks[finish - 1].extend(to_move)

    top = "".join([s[-1] for s in stacks])
    print(top)


if __name__ == "__main__":
    solve()
