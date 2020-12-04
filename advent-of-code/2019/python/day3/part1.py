import numpy as np

lookup = {0: " ", 1: ".", 2: "+", -1: "o"}


def print_grid(grid, size):
    grid[size // 2, size // 2] = -1
    for i in range(size):
        for j in range(size):
            print(lookup[grid[i][j]], end="")
        print()


def distance(a, b):
    return np.abs(a - b).sum()


def follow_wire_path(central_port, wire):
    y, x = central_port
    coords = set([])

    for instructions in wire:
        direction, magnitude = instructions[0], int(instructions[1:])
        if direction == "U":
            for y1 in range(y - magnitude, y):
                coords.add((y1, x))
            y -= magnitude
        elif direction == "D":
            for y1 in range(y, y + magnitude):
                coords.add((y1, x))
            y += magnitude
        elif direction == "R":
            for x1 in range(x, x + magnitude):
                coords.add((y, x1))
            x += magnitude
        else:
            for x1 in range(x - magnitude, x):
                coords.add((y, x1))
            x -= magnitude

    return coords


def main():
    central_port = np.array((0, 0))

    with open("input.txt", "r") as fr:
        lines = fr.readlines()
        wires = [line.strip().split(",") for line in lines]
        wire1, wire2 = wires

        wire1_coords = follow_wire_path(central_port, wire1)
        wire2_coords = follow_wire_path(central_port, wire2)
        common = wire1_coords.intersection(wire2_coords)

        distances = []
        for coord in common:
            dist = distance(np.array(coord), central_port)
            distances.append(dist)

        print(
            f"The Manhattan distance from the central port to the closest intersection is {min(distances)}"
        )


if __name__ == "__main__":
    main()
