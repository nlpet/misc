from collections import Counter


def main():
    with open("input.txt", "r") as fr:
        numbers = sorted([int(line.strip()) for line in fr.readlines()])

    numbers.insert(0, 0)
    diffs = []

    for i in range(1, len(numbers)):
        diffs.append(numbers[i] - numbers[i - 1])

    c = Counter(diffs)
    one_jolt = c[1]
    three_jolt = c[3] + 1
    print(f"{one_jolt} x {three_jolt} = {one_jolt * three_jolt}")


if __name__ == "__main__":
    main()
