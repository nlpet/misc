import re
from collections import Counter


def main():
    num_valid = 0

    with open("input.txt", "r") as fr:
        for line in fr.readlines():
            patt = re.search(r"(\d+)-(\d+)\s(\w):\s(\w+)$", line.strip())
            if not patt:
                print(f"WARNING - line missing pattern ({line.strip()})")

            low, high, char, s = patt.groups()
            low, high = int(low), int(high)
            counter = Counter(s)

            if low <= counter.get(char, -1) <= high:
                num_valid += 1

    print(f"Number of valid passwords {num_valid}")


if __name__ == "__main__":
    main()
