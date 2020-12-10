from collections import defaultdict


def main():
    with open("input.txt", "r") as fr:
        numbers = [int(line.strip()) for line in fr.readlines()]

    target = 375054920
    s, e = 0, 0
    current_sum = numbers[s]

    while 1:
        if current_sum == target:
            contiguous_set = numbers[s:e]
            smallest, largest = min(contiguous_set), max(contiguous_set)
            print(f"{smallest}+{largest}={smallest + largest}")
            break

        if current_sum > target:
            while current_sum > target:
                current_sum -= numbers[s]
                s += 1

            continue

        e += 1
        current_sum += numbers[e]


if __name__ == "__main__":
    main()
