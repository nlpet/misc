# --- Day 3: Binary Diagnostic ---

import pydash.objects as po


def get_counts(filename):
    counts = {}

    with open(filename) as fr:
        n_bits = len(fr.readline().strip())
        fr.seek(0)

        for line in fr.readlines():
            path = []

            for char in line.strip():
                path.append(char)
                v = po.get(counts, ".".join(path))

                if v is None:
                    po.set_(counts, path, {"count": 1})
                else:
                    v["count"] += 1

    return counts, n_bits


def solution():
    counts, n_bits = get_counts("input.txt")
    oxygen_path, co2_path = [], []

    while n_bits > 0:
        for path, condition in [(oxygen_path, "more"), (co2_path, "fewer")]:
            zero_branch = po.get(counts, ".".join([*path, "0"]))
            one_branch = po.get(counts, ".".join([*path, "1"]))

            if not zero_branch:
                path.append("1")
            elif not one_branch:
                path.append("0")
            else:
                bit = int(one_branch["count"] >= zero_branch["count"])
                bit = str(bit) if condition == "more" else str(int(not bit))
                path.append(bit)

        n_bits -= 1

    oxygen_gen_rating = int(f"0b{''.join(oxygen_path)}", 2)
    co2_scrubber_rating = int(f"0b{''.join(co2_path)}", 2)
    print(f"The life support rating is {oxygen_gen_rating * co2_scrubber_rating}")


if __name__ == "__main__":
    solution()
