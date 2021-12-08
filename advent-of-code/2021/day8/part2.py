# --- Day 8: Seven Segment Search ---

from collections import defaultdict

display = {
    0: ["a", "b", "c", "e", "f", "g"],
    1: ["c", "f"],
    2: ["a", "c", "d", "e", "g"],
    3: ["a", "c", "d", "f", "g"],
    4: ["b", "c", "d", "f"],
    5: ["a", "b", "d", "f", "g"],
    6: ["a", "b", "d", "e", "f", "g"],
    7: ["a", "c", "f"],
    8: ["a", "b", "c", "d", "e", "f", "g"],
    9: ["a", "b", "c", "d", "f", "g"],
}


def calculate_frequencies(sequences):
    letters = defaultdict(int)
    for seq in sequences:
        for s in seq:
            letters[s] += 1

    return letters


def get_reference_encodings(frequencies):
    encoding = {}
    for k, v in display.items():
        enc = "".join(sorted([str(frequencies[s]) for s in v]))
        encoding[enc] = k

    return encoding


def get_encoding(frequencies, seq):
    return "".join(map(str, sorted(str(frequencies[s]) for s in seq)))


def solution():

    frequencies = calculate_frequencies(display.values())
    ref_encodings = get_reference_encodings(frequencies)

    output_values = 0

    with open("input.txt") as fr:
        for line in fr.readlines():
            signal, output_seq = line.strip().split(" | ")
            signal = signal.split(" ")
            output_seq = output_seq.split(" ")
            freqs = calculate_frequencies(signal)

            output_value = []
            for s in output_seq:
                enc = get_encoding(freqs, s)
                output_value.append(ref_encodings[enc])

            output_value = [
                str(ref_encodings[get_encoding(freqs, s)]) for s in output_seq
            ]

            output_values += int("".join(output_value))

    print(output_values)


if __name__ == "__main__":
    solution()
