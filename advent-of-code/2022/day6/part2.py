def solve():
    k = 14

    with open("input.txt") as fr:
        sequence = fr.read().strip()

    for i in range(len(sequence) - 4):
        chunk = sequence[i : i + k]
        if len(chunk) == len(set(chunk)):
            print(i + k)
            break


if __name__ == "__main__":
    solve()
