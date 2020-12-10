from collections import defaultdict


def check_sequence(preamble, numbers, preamble_len):
    idx = 0

    for i in range(preamble_len, len(numbers)):
        found = False
        for p in preamble:
            if numbers[i] - p in preamble:
                found = True
                break

        if not found:
            return numbers[i]

        preamble.remove(numbers[idx])
        idx += 1
        preamble.add(numbers[i])


def main():
    with open("input.txt", "r") as fr:
        numbers = [int(line.strip()) for line in fr.readlines()]

    preamble_len = 25
    preamble = set(numbers[:preamble_len])

    print(check_sequence(preamble, numbers, preamble_len))


if __name__ == "__main__":
    main()
