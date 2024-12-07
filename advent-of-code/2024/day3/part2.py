import re


def solve():
    with open("input.txt") as fr:
        corrupted_memory = fr.read().strip()

    memory = []

    patt = re.compile(r"don't()|do()")
    start = 0
    ignore = False

    for m in re.finditer(patt, corrupted_memory):
        if m.group() == "don't":
            if not ignore:
                memory.append(corrupted_memory[start : m.start()])
                start = m.end()
                ignore = True
        else:
            if ignore:
                start = m.end()
            else:
                memory.append(corrupted_memory[start : m.start()])
                start = m.end()
            ignore = False

    if not ignore:
        memory.append(corrupted_memory[start:])

    memory = "".join(memory)
    patt = re.compile(r"mul\(\d{1,3},\d{1,3}\)")

    answer = 0

    for mul in re.findall(patt, memory):
        a, b = map(int, mul[4:-1].split(","))
        answer += a * b

    print(f"Answer: {answer}")


if __name__ == "__main__":
    solve()
