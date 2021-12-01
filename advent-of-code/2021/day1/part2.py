# --- Day 1: Sonar Sweep ---


def solution():
    with open("input.txt") as fr:
        n = 0
        window_size = 3
        measurements = [int(line.strip()) for line in fr.readlines()]

        for i in range(1, len(measurements) - window_size + 1):
            s1 = sum(measurements[i - 1 : i - 1 + window_size])
            s2 = sum(measurements[i : i + window_size])

            if s2 > s1:
                n += 1

    print(f'Sums larger than previous sum: {n}')


if __name__ == "__main__":
    solution()
