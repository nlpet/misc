# --- Day 2: Dive! ---


def solution():
    with open("input.txt") as fr:
        position, depth = 0, 0

        for line in fr.readlines():
            direction, magnitude = line.strip().split(" ")
            if direction == "forward":
                position += int(magnitude)
            elif direction == "up":
                depth -= int(magnitude)
            elif direction == "down":
                depth += int(magnitude)
            else:
                print(f"Unrecognised direction {direction}")

    print(f"position x depth = {position * depth}")


if __name__ == "__main__":
    solution()
