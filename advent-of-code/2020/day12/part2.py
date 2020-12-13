def rotate(facing, direction, degrees):
    orientations = ["N", "E", "S", "W"]

    idx = orientations.index(facing)
    n_rotations = degrees // 90

    if direction == "R":
        return orientations[(idx + n_rotations) % len(orientations)]

    return orientations[(idx - n_rotations) % len(orientations)]


def rotate_waypoint(waypoint, degrees, direction):
    orientations = [
        rotate("E" if waypoint[0] >= 0 else "W", direction, degrees),
        rotate("N" if waypoint[1] < 0 else "S", direction, degrees),
    ]

    magnitudes = [abs(waypoint[0]), abs(waypoint[1])]

    for orientation, magnitude in zip(orientations, magnitudes):
        if orientation == "N":
            waypoint[1] = -magnitude
        elif orientation == "S":
            waypoint[1] = magnitude
        elif orientation == "E":
            waypoint[0] = magnitude
        else:
            waypoint[0] = -magnitude


def move_waypoint(direction, waypoint, magnitude):
    if direction == "E":
        waypoint[0] += magnitude
    elif direction == "W":
        waypoint[0] -= magnitude
    elif direction == "N":
        waypoint[1] -= magnitude
    else:
        waypoint[1] += magnitude


def main():
    position = [0, 0]
    waypoint = [10, -1]

    with open("input.txt", "r") as fr:
        for line in fr.readlines():
            instruction = line.strip()
            direction, magnitude = instruction[0], int(instruction[1:])

            if direction == "F":
                position[0] += magnitude * waypoint[0]
                position[1] += magnitude * waypoint[1]
            elif direction in {"N", "S", "E", "W"}:
                move_waypoint(direction, waypoint, magnitude)
            elif direction in {"L", "R"}:
                rotate_waypoint(waypoint, magnitude, direction)

    distance = abs(0 + position[0]) + abs(0 + position[1])
    print(distance)


if __name__ == "__main__":
    main()
