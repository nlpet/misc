import re


def solve():

    with open("input.txt") as fr:
        memory = fr.read().strip()

    patt = re.compile(r"mul\(\d{1,3},\d{1,3}\)")

    answer = 0

    for mul in re.findall(patt, memory):
        a, b = map(int, mul[4:-1].split(","))
        answer += a * b

    print(f"Answer: {answer}")


if __name__ == "__main__":
    solve()
