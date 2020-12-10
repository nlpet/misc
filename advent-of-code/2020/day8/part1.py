from collections import defaultdict


def main():
    with open("input.txt", "r") as fr:
        program = [line.strip().split(" ") for line in fr.readlines()]

    executions = defaultdict(int)
    idx = 0
    accumulator = 0

    while True:
        op, val = program[idx]
        executions[idx] += 1

        if executions[idx] > 1:
            print("Accumulator: {}".format(accumulator))
            break

        if op == "nop":
            idx += 1
        elif op == "acc":
            accumulator += int(val)
            idx += 1
        elif op == "jmp":
            idx += int(val)


if __name__ == "__main__":
    main()
