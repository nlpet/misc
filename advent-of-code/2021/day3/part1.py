# --- Day 3: Binary Diagnostic ---

from collections import defaultdict


def solution():
    with open("input.txt") as fr:
        length, counts = 0, defaultdict(int)
        for line in fr.readlines():
            for idx, char in enumerate(line.strip()):
                counts[idx] += int(char == "0")

            length += 1

        gamma_rate_bits, epsilon_rate_bits = [], []
        for count in counts.values():
            bit = int(length - count > count)
            gamma_rate_bits.append(str(bit))
            epsilon_rate_bits.append(str(int(not bit)))

        gamma_rate = int(f"0b{''.join(gamma_rate_bits)}", 2)
        epsilon_rate = int(f"0b{''.join(epsilon_rate_bits)}", 2)
        print(f"The power consumption is {gamma_rate * epsilon_rate}")


if __name__ == "__main__":
    solution()
