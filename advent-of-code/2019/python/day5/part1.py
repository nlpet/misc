def get_params(opcode, program, params):
    l = 2 + len(params)
    if len(opcode) != l:
        opcode = opcode.zfill(l)

    return [program[p] if m == "0" else p for p, m in zip(params, opcode[:-2][::-1])]


def main():

    params_lookup = {"1": 3, "2": 3, "3": 1, "4": 1, "9": 0}

    with open("input.txt", "r") as fr:
        program = [int(n) for n in fr.read().strip().split(",")]

    pointer = 0

    while True:
        opcode = str(program[pointer])
        n_inst = params_lookup[opcode[-1]]

        if opcode == "99":
            break

        if opcode[-1] == "1":
            n, m, idx = program[pointer + 1 : pointer + n_inst + 1]
            n, m = get_params(opcode, program, [n, m])
            program[idx] = n + m
        elif opcode[-1] == "2":
            n, m, idx = program[pointer + 1 : pointer + n_inst + 1]
            n, m = get_params(opcode, program, [n, m])
            program[idx] = n * m
        elif opcode[-1] == "3":
            p = program[pointer + 1]
            n = int(input("Please provide an input integer: "))
            program[p] = n
        elif opcode[-1] == "4":
            params = [program[pointer + 1]]
            n = get_params(opcode, program, params)[0]
            print(n)
        else:
            print(f"Unknown opcode {opcode} at position {pointer}!")

        pointer += n_inst + 1


if __name__ == "__main__":
    main()
