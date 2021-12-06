# --- Day 6: Lanternfish ---

from collections import defaultdict


def solution():
    days = 256
    ages = defaultdict(int)

    with open("input.txt") as fr:
        for n in fr.readline().split(","):
            ages[int(n)] += 1

    for _ in range(days):
        next_day = defaultdict(int)
        for age, count in ages.items():
            if age == 0:
                next_day[6] += count
                next_day[8] += count
            else:
                next_day[age - 1] += count

        ages = next_day

    print(f"Number of laternfish after {days} days is {sum(ages.values())}")


if __name__ == "__main__":
    solution()
