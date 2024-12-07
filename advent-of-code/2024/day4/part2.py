import numpy as np


def is_xmas(block):
    allowed = {(1, 2, 3), (3, 2, 1)}
    lr_diag = (block[0, 0], block[1, 1], block[2, 2])
    rl_diag = (block[0, 2], block[1, 1], block[2, 0])

    if lr_diag in allowed and rl_diag in allowed:
        return True

    return False


def solve():
    wordsearch = []
    mapping = {"M": 1, "A": 2, "S": 3}

    with open("input.txt") as fr:
        for line in fr.readlines():
            l = []
            for x in line.strip():
                l.append(mapping.get(x, 0))

            wordsearch.append(l)

    wordsearch = np.array(wordsearch)
    size = wordsearch.shape[0]
    count = 0

    for row in range(size - 2):
        for col in range(size - 2):
            block = wordsearch[row : row + 3, col : col + 3]
            if is_xmas(block):
                count += 1

    print(f"Answer: {count}")


if __name__ == "__main__":
    solve()
