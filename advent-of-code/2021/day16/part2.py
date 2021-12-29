# --- Day 16: Packet Decoder ---

import numpy as np

mapping = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

types_mapping = {
    0: "+",
    1: "*",
    2: "min",
    3: "max",
    5: ">",
    6: "<",
    7: "==",
}


def bin_to_dec(b):
    if isinstance(b, str):
        return int(f"0b{b}", 2)

    return int(f"0b{''.join(b)}", 2)


def hex_to_bin(h):
    b = []
    for ch in h:
        b.append(mapping[ch])

    return "".join(b)


def evaluate(operator, vs):
    if operator == "+":
        return sum(vs)
    elif operator == "*":
        return np.prod(vs)
    elif operator == "min":
        return min(vs)
    elif operator == "max":
        return max(vs)
    elif operator == ">":
        return int(vs[0] > vs[1])
    elif operator == "<":
        return int(vs[0] < vs[1])

    return int(vs[0] == vs[1])


def process_literal_packet(packet, values, start, size):
    packet_bits = []
    n_packets = 0

    for i in range(start, len(packet), size):
        label, *bits = packet[i : i + size]

        packet_bits.extend(bits)
        n_packets += 1

        if label == "0":
            break

    values.append(bin_to_dec(packet_bits))
    return values, start + n_packets * size


def read_packet(packet, values=[], size=5):
    type_id = bin_to_dec(packet[3:6])
    start, n_packets, length = 6, 0, 0

    if type_id == 4:  # literal
        return process_literal_packet(packet, values, start, size)

    # operator
    length_type_id = packet[start]

    if length_type_id == "0":
        n_bits = 15
        total_length_in_bits = bin_to_dec(packet[start + 1 : start + 1 + n_bits])
        loc = start + 1 + n_bits
        subpackets = packet[loc : loc + total_length_in_bits]
        vs = []

        while length < total_length_in_bits:
            vs, l = read_packet(subpackets, vs)
            subpackets = subpackets[l:]
            length += l
            n_packets += 1

        evaluated = evaluate(types_mapping[type_id], vs)
        values.append(evaluated)
    else:
        n_bits = 11
        n_packets = bin_to_dec(packet[start + 1 : start + 1 + n_bits])
        loc = start + 1 + n_bits
        subpackets = packet[loc:]
        vs = []

        for _ in range(n_packets):
            vs, l = read_packet(subpackets, vs)
            subpackets = subpackets[l:]
            length += l

        evaluated = evaluate(types_mapping[type_id], vs)
        values.append(evaluated)

    length += loc

    return values, length


def solution():
    with open("input.txt") as fr:
        packet = hex_to_bin(fr.readline().strip())

    values, _ = read_packet(packet)
    print(values[0])


if __name__ == "__main__":
    solution()
