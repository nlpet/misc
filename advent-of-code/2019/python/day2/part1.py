import re
from collections import Counter


def main():
    num_valid = 0

    with open("input.txt", "r") as fr:
        for line in fr.readlines():
            patt = re.search(r"(\d+)-(\d+)\s(\w):\s(\w+)$", line.strip())
            if not patt:
                print(f"WARNING - line missing pattern ({line.strip()})")

            i, j, char, s = patt.groups()
            i, j = int(i), int(j)

            if int(s[i - 1] == char) + int(s[j - 1] == char) == 1:
                num_valid += 1

    print(f"Number of valid passwords {num_valid}")


if __name__ == "__main__":
    main()
