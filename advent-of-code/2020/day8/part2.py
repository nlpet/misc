from collections import defaultdict


def main():
    with open("input.txt", "r") as fr:
        program = [line.strip().split(" ") for line in fr.readlines()]

    executions = defaultdict(int)
    idx = 0
    accumulator = 0
    visited = set([])
    swapped = False

    while True:
        if idx >= len(program):
            print("Accumulator: {}".format(accumulator))
            break

        op, val = program[idx]
        executions[idx] += 1

        if executions[idx] > 1:
            idx = 0
            accumulator = 0
            executions = defaultdict(int)
            swapped = False
            continue

        if op == "jmp" and idx not in visited and not swapped:
            op = "nop"
            visited.add(idx)
            swapped = True
        elif op == "nop" and idx not in visited and not swapped:
            op = "jmp"
            visited.add(idx)
            swapped = True

        if op == "nop":
            idx += 1
        elif op == "acc":
            accumulator += int(val)
            idx += 1
        elif op == "jmp":
            idx += int(val)


if __name__ == "__main__":
    main()
