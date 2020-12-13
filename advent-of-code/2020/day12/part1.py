def move(facing, position, magnitude):
    if facing == "E":
        position[1] += magnitude
    elif facing == "W":
        position[1] -= magnitude
    elif facing == "N":
        position[0] -= magnitude
    else:
        position[0] += magnitude


def rotate(facing, degrees, direction):
    orientations = ["N", "E", "S", "W"]
    idx = orientations.index(facing)
    n_rotations = degrees // 90

    if direction == "R":
        return orientations[(idx + n_rotations) % len(orientations)]

    return orientations[(idx - n_rotations) % len(orientations)]


def main():

    facing = "E"
    position = [0, 0]

    with open("input.txt", "r") as fr:
        for line in fr.readlines():
            instruction = line.strip()
            direction, magnitude = instruction[0], int(instruction[1:])

            if direction == "F":
                move(facing, position, magnitude)
            elif direction in {"N", "S", "E", "W"}:
                move(direction, position, magnitude)
            elif direction in {"L", "R"}:
                facing = rotate(facing, magnitude, direction)

    distance = abs(0 + position[0]) + abs(0 + position[1])
    print(distance)


if __name__ == "__main__":
    main()
