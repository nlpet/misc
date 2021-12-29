# --- Day 16: Packet Decoder ---


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


def bin_to_dec(b):
    if isinstance(b, str):
        return int(f"0b{b}", 2)

    return int(f"0b{''.join(b)}", 2)


def hex_to_bin(h):
    b = []
    for ch in h:
        b.append(mapping[ch])

    return "".join(b)


def read_packet(packet, versions=[], size=5):
    version = bin_to_dec(packet[:3])
    type_id = bin_to_dec(packet[3:6])
    start, n_packets, length = 6, 0, 0

    versions.append(version)

    if type_id == 4:  # literal
        packet_bits = []

        for i in range(start, len(packet), size):
            label, *bits = packet[i : i + size]

            packet_bits.extend(bits)
            n_packets += 1

            if label == "0":
                break

        return versions, start + n_packets * size

    # operator
    length_type_id = packet[start]

    if length_type_id == "0":
        n_bits = 15
        total_length_in_bits = bin_to_dec(packet[start + 1 : start + 1 + n_bits])
        loc = start + 1 + n_bits
        subpackets = packet[loc : loc + total_length_in_bits]

        while length < total_length_in_bits:
            versions, l = read_packet(subpackets, versions)
            subpackets = subpackets[l:]
            length += l
            n_packets += 1
    else:
        n_bits = 11
        n_packets = bin_to_dec(packet[start + 1 : start + 1 + n_bits])
        loc = start + 1 + n_bits
        subpackets = packet[loc:]
        for _ in range(n_packets):
            versions, l = read_packet(subpackets, versions)
            subpackets = subpackets[l:]
            length += l

    length += loc

    return versions, length


def solution():
    with open("input.txt") as fr:
        packet = hex_to_bin(fr.readline().strip())

    versions, _ = read_packet(packet)
    print(sum(versions))


if __name__ == "__main__":
    solution()
