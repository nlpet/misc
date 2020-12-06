def get_params(opcode, program, params):
    l = 2 + len(params)
    if len(opcode) != l:
        opcode = opcode.zfill(l)

    return [program[p] if m == "0" else p for p, m in zip(params, opcode[:-2][::-1])]


def addition(program, pointer, opcode, n_inst):
    n, m, idx = program[pointer + 1 : pointer + n_inst + 1]
    n, m = get_params(opcode, program, [n, m])
    program[idx] = n + m

    return pointer + n_inst + 1


def multiplication(program, pointer, opcode, n_inst):
    n, m, idx = program[pointer + 1 : pointer + n_inst + 1]
    n, m = get_params(opcode, program, [n, m])
    program[idx] = n * m

    return pointer + n_inst + 1


def user_input(program, pointer, _, n_inst):
    p = program[pointer + 1]
    n = int(input("Please provide an input integer: "))
    program[p] = n

    return pointer + n_inst + 1


def output(program, pointer, opcode, n_inst):
    params = [program[pointer + 1]]
    n = get_params(opcode, program, params)[0]
    print(n)

    return pointer + n_inst + 1


def jump_if_true(program, pointer, opcode, n_inst):
    params = program[pointer + 1 : pointer + n_inst + 1]
    n, m = get_params(opcode, program, params)

    if n > 0:
        pointer = m
        return pointer

    return pointer + n_inst + 1


def jump_if_false(program, pointer, opcode, n_inst):
    params = program[pointer + 1 : pointer + n_inst + 1]
    n, m = get_params(opcode, program, params)

    if n == 0:
        pointer = m
        return pointer

    return pointer + n_inst + 1


def less_than(program, pointer, opcode, n_inst):
    n, m, idx = program[pointer + 1 : pointer + n_inst + 1]
    n, m = get_params(opcode, program, [n, m])
    program[idx] = 1 if n < m else 0
    return pointer + n_inst + 1


def equals(program, pointer, opcode, n_inst):
    n, m, idx = program[pointer + 1 : pointer + n_inst + 1]
    n, m = get_params(opcode, program, [n, m])
    program[idx] = 1 if n == m else 0
    return pointer + n_inst + 1


def halt():
    pass


def main():
    params_lookup = {
        "1": 3,
        "2": 3,
        "3": 1,
        "4": 1,
        "5": 2,
        "6": 2,
        "7": 3,
        "8": 3,
        "9": 0,
    }
    instructions = {
        "1": addition,
        "2": multiplication,
        "3": user_input,
        "4": output,
        "5": jump_if_true,
        "6": jump_if_false,
        "7": less_than,
        "8": equals,
        "9": halt,
    }

    with open("input.txt", "r") as fr:
        program = [int(n) for n in fr.read().strip().split(",")]

    pointer = 0

    while True:
        opcode = str(program[pointer])
        n_inst = params_lookup[opcode[-1]]

        if opcode == "99":
            break

        if not instructions.get(opcode[-1]):
            print(f"Unknown opcode {opcode} at position {pointer}!")
            break

        pointer = instructions[opcode[-1]](program, pointer, opcode, n_inst)


if __name__ == "__main__":
    main()
