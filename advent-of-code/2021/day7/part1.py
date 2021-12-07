# --- Day 7: The Treachery of Whales ---

from statistics import median


def fuel_usage(positions, p):
    return sum([abs(pos - p) for pos in positions])


def solution():
    with open("input.txt") as fr:
        positions = [int(n) for n in fr.readline().split(",")]

    m = int(median(positions))
    f = fuel_usage(positions, m)
    print(f"Fuel usage is {f} at position {m}")


if __name__ == "__main__":
    solution()
