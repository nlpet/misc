from math import lcm


def parse(line):
    module, destination = line.split(" -> ")
    destination_modules = destination.split(", ")

    if module.startswith("%"):
        module_type, module_name = "flip-flop", module[1:]
    elif module.startswith("&"):
        module_type, module_name = "conj", module[1:]
    else:
        module_type, module_name = "broadcaster", module

    return {"type": module_type, "name": module_name, "dest": destination_modules}


def setup(configuration):
    program = {}
    for mc in configuration:
        if mc["type"] == "flip-flop":
            program[mc["name"]] = {"dest": mc["dest"], "state": 0, "type": mc["type"]}
        elif mc["type"] == "broadcaster":
            program[mc["name"]] = {"dest": mc["dest"], "type": mc["type"]}
        elif mc["type"] == "conj":
            program[mc["name"]] = {"dest": mc["dest"], "type": mc["type"], "state": {}}

    for cm in [c["name"] for c in configuration if c["type"] == "conj"]:
        connected = []
        for mc in configuration:
            if cm in mc["dest"]:
                connected.append(mc["name"])
        program[cm]["state"] = {c: "low" for c in connected}

    return program


def push_button(pulses):
    pulses.append(("aptly", "broadcaster", 1))


def process(program, pulses, seen, cycles, connected, n_button_presses):
    while pulses:
        sender, receiver, pulse = pulses.pop(0)
        m = program.get(receiver)

        if m is None:  # testing
            continue

        if receiver == connected and pulse == 0:
            seen[sender] += 1

            if sender not in cycles:
                cycles[sender] = n_button_presses

            if all(seen.values()):
                answer = lcm(*list(cycles.values()))
                print(f"Answer: {answer}")
                return -1

        if m["type"] == "broadcaster":
            for d in m["dest"]:
                pulses.append((receiver, d, pulse))
        elif m["type"] == "flip-flop":
            prev_state = program[receiver]["state"]
            program[receiver]["state"] = program[receiver]["state"] ^ pulse
            if prev_state == 1 and program[receiver]["state"] == 0:
                for d in m["dest"]:
                    pulses.append((receiver, d, 1))
            if prev_state == 0 and program[receiver]["state"] == 1:
                for d in m["dest"]:
                    pulses.append((receiver, d, 0))
        elif m["type"] == "conj":
            m["state"][sender] = "low" if pulse == 1 else "high"
            memory = [s == "high" for s in m["state"].values()]
            pulse = 1 if all(memory) else 0
            for d in m["dest"]:
                pulses.append((receiver, d, pulse))


def solve():
    with open("input.txt") as fr:
        configuration = [parse(line.strip()) for line in fr.readlines()]

    program = setup(configuration)
    pulses = []

    (connected,) = [k for k, v in program.items() if "rx" in v["dest"]]
    seen = {k: 0 for k, v in program.items() if connected in v["dest"]}
    cycles = {}
    n_button_presses = 0

    while True:
        n_button_presses += 1
        push_button(pulses)
        resp = process(program, pulses, seen, cycles, connected, n_button_presses)
        if resp == -1:
            break


if __name__ == "__main__":
    solve()
