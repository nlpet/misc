"""
Naive string compression algorithm.

Good for strings which have long runs of the same char.
"""


def run_length_encoding(s):
    """Implement the run-length encoding algorithm."""
    assert type(s) == str, "Error - string required."
    new_string = ""
    current_char = s[0]
    current_count = 1
    length = len(s)
    for i in range(1, length):
        if s[i] != current_char:
            new_string += "%d%s" % (current_count, current_char)
            current_char = s[i]
            current_count = 1
        else:
            current_count += 1
            if i == length - 1:
                new_string += "%d%s" % (current_count, current_char)
    new_length = len(new_string)
    if new_length >= length:
        print("Compression algorithm not effective against input string.")
        return("String: %s" % s)
    else:
        print("Space saved: %.2f%%" % ((1 - (new_length / length)) * 100))
        return("New string: %s" % new_string)


if __name__ == "__main__":
    s = "AAIJFF"
    print(run_length_encoding(s))
