def main():

    with open("input.txt", "r") as fr:
        program = [int(n) for n in fr.read().strip().split(",")]

    program[1] = 12
    program[2] = 2

    for i in range(0, len(program), 4):
        if program[i] == 1:
            n, m, idx = program[i + 1 : i + 1 + 3]
            program[idx] = program[n] + program[m]
        elif program[i] == 2:
            n, m, idx = program[i + 1 : i + 1 + 3]
            program[idx] = program[n] * program[m]
        elif program[i] == 99:
            break
        else:
            print(f"Unknown opcode {program[i]} at position {i}!")

    print(f"Value at position 0 is {program[0]}")


if __name__ == "__main__":
    main()
