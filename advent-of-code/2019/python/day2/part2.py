def search_for_params(program, target, default_program):
    for noun in range(100):
        for verb in range(100):

            program = default_program[:]
            program[1] = noun
            program[2] = verb

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

            if program[0] == target:
                print(f"100 x noun + verb = {100 * noun + verb}")
                return


def main():
    with open("input.txt", "r") as fr:
        program = [int(n) for n in fr.read().strip().split(",")]

    target = 19690720
    default_program = program[:]
    search_for_params(program, target, default_program)


if __name__ == "__main__":
    main()
