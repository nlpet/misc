def hash(s):
    value = 0
    for ch in s:
        value += ord(ch)
        value *= 17
        value = value % 256
    return value


def solve():
    with open("input.txt") as fr:
        sequence = fr.read().strip().split(",")

    result = sum([hash(s) for s in sequence])
    print(result)


if __name__ == "__main__":
    solve()
