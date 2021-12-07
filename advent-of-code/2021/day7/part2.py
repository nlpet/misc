# --- Day 7: The Treachery of Whales ---

from statistics import mean


def partial_sum(n):
    return int((n * (n + 1)) / 2)


def fuel_usage(positions, p):
    return sum([partial_sum(abs(pos - p)) for pos in positions])


def solution():
    with open("input.txt") as fr:
        positions = [int(n) for n in fr.readline().split(",")]

    m = int(mean(positions))
    f = fuel_usage(positions, m)

    print(f"Fuel usage is {f} at position {m}")


if __name__ == "__main__":
    solution()
