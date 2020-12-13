from collections import Counter


def main():
    with open("input.txt", "r") as fr:
        numbers = sorted([int(line.strip()) for line in fr.readlines()])

    numbers.append(numbers[-1] + 3)
    paths = {0: 1}
    for n in numbers:
        paths[n] = paths.get(n - 3, 0) + paths.get(n - 2, 0) + paths.get(n - 1, 0)
    print(paths[numbers[-1]])


if __name__ == "__main__":
    main()
