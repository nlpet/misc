import re


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
                current_bitmask = {}

                for idx, char in enumerate(bitmask):
                    if char in {"0", "1"}:
                        current_bitmask[idx] = char
                continue

            instruction = re.search(update_patt, line)
            if instruction:
                address, value = map(int, instruction.groups())
                bin_value = list(bin(value)[2:].zfill(36))
                for k, v in current_bitmask.items():
                    bin_value[k] = v

                masked_value = int(f"0b{''.join(bin_value)}", 2)
                memory[address] = masked_value

    print(sum(memory.values()))


if __name__ == "__main__":
    main()
