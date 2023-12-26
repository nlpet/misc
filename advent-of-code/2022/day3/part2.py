from string import ascii_letters


def solve():
    with open("input.txt") as fr:
        lines = [line.strip() for line in fr.readlines()]

    priorities = {l: i + 1 for i, l in enumerate(ascii_letters)}
    group_size = 3
    total = 0

    for group in zip(*(iter(lines),) * group_size):
        (common,) = set.intersection(*map(set, group))
        total += priorities[common]

    print(total)


if __name__ == "__main__":
    solve()
