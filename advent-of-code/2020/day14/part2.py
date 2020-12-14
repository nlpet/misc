import re


def decimal_to_binary(value):
    return list(bin(value)[2:].zfill(36))


def binary_to_decimal(value):
    return int(f"0b{''.join(value)}", 2)


def main():
    bitmask_patt = re.compile(r"mask = (.+)$")
    update_patt = re.compile(r"mem\[(\d+)\] = (\d+)")

    current_bitmask = {}
    memory = {}

    with open("input.txt", "r") as fr:
        for line in fr.readlines():
            match = re.search(bitmask_patt, line)
            if match:
                bitmask = match.groups()[0]
                current_bitmask = {"X": [], "1": []}

                for idx, char in enumerate(bitmask):
                    if char in {"X", "1"}:
                        current_bitmask[char].append(idx)
                continue

            instruction = re.search(update_patt, line)
            if instruction:
                address, value = map(int, instruction.groups())
                bin_address = decimal_to_binary(address)

                for idx in current_bitmask["1"]:
                    bin_address[idx] = "1"

                if len(current_bitmask["X"]) > 0:
                    stack = [bin_address]

                    for idx in current_bitmask["X"]:
                        current_stack = []
                        for address in stack:
                            address[idx] = "1"
                            current_stack.append(address[:])
                            address[idx] = "0"
                            current_stack.append(address[:])

                        stack = current_stack[:]
                    addresses = list(map(binary_to_decimal, stack))
                else:
                    addresses = [binary_to_decimal(bin_address)]

                for address in addresses:
                    memory[address] = value

    print(sum(memory.values()))


if __name__ == "__main__":
    main()
