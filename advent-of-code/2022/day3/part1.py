from string import ascii_letters


def solve():
    priorities = {l: i + 1 for i, l in enumerate(ascii_letters)}

    total = 0

    with open("input.txt") as fr:
        for line in fr.readlines():
            contents = line.strip()
            hl = len(contents) // 2
            fst = set(contents[:hl])
            snd = set(contents[hl:])
            (common,) = fst & snd
            total += priorities[common]

    print(total)


if __name__ == "__main__":
    solve()
