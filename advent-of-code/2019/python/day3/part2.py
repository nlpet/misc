import numpy as np


def distance(a, b):
    return np.abs(a - b).sum()


def follow_wire_path(central_port, wire):
    y, x = central_port
    coords = set([])
    steps = {}
    step_num = 0

    for instructions in wire:
        direction, magnitude = instructions[0], int(instructions[1:])
        if direction == "U":
            for y1 in range(y, y - magnitude, -1):
                coords.add((y1, x))

                if not steps.get((y1, x)):
                    steps[(y1, x)] = step_num
                step_num += 1
            y -= magnitude
        elif direction == "D":
            for y1 in range(y, y + magnitude):
                coords.add((y1, x))

                if not steps.get((y1, x)):
                    steps[(y1, x)] = step_num
                step_num += 1
            y += magnitude
        elif direction == "R":
            for x1 in range(x, x + magnitude):
                coords.add((y, x1))

                if not steps.get((y, x1)):
                    steps[(y, x1)] = step_num
                step_num += 1
            x += magnitude
        else:
            for x1 in range(x, x - magnitude, -1):
                coords.add((y, x1))

                if not steps.get((y, x1)):
                    steps[(y, x1)] = step_num
                step_num += 1
            x -= magnitude

    return coords, steps


def main():
    central_port = np.array((0, 0))

    with open("input.txt", "r") as fr:
        lines = fr.readlines()
        wires = [line.strip().split(",") for line in lines]
        wire1, wire2 = wires

        wire1_coords, wire1_steps = follow_wire_path(central_port, wire1)
        wire2_coords, wire2_steps = follow_wire_path(central_port, wire2)
        common = wire1_coords.intersection(wire2_coords)
        common.remove((0, 0))

        steps = []
        for coord in common:
            steps.append(wire1_steps[coord] + wire2_steps[coord])

        print(
            f"The fewest combined steps the wires must take to reach an intersection is {min(steps)}"
        )


if __name__ == "__main__":
    main()
