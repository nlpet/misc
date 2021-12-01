# --- Day 1: Sonar Sweep ---


def solution():
    with open("input.txt") as fr:
        n = 0
        previous = int(fr.readline().strip())

        for line in fr.readlines():
            measurement = int(line.strip())
            if measurement > previous:
                n += 1

            previous = measurement

    print(f"Measurements larger than previous measurement: {n}")


if __name__ == "__main__":
    solution()
