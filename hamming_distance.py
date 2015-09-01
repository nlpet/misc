"""Compute Hamming distance."""


def xor(s1, s2):
    """s1 ^ s2."""
    s1, s2 = '{0:032b}'.format(s1), '{0:032b}'.format(s2)
    ns = ''
    for i in range(len(s1)):
        n, m = int(s1[i]), int(s2[i])
        if (n and not m) or (m and not n):
            ns += '1'
        else:
            ns += '0'
    return int(ns, 2)


def hamming_strings(s1, s2):
    """Get Hamming distance between strings s1 and s2."""
    return sum([1 if c1 != c2 else 0 for c1, c2 in zip(s1, s2)])


def hamming_numbers(s1, s2):
    """Get Hamming distance between numbers s1 and s2."""
    count, z = 0, xor(s1, s2)
    while z:
        if z & 1:
            count += 1
        z >>= 1
    return count


if __name__ == '__main__':
    s1 = "5"
    s2 = "3"
    mode = "num"
    maxx = 2 ** 32
    assert len(s1) == len(s2), "Input strings should have the same length."
    if mode == "num":
        try:
            s1, s2 = int(s1), int(s2)
            assert s1 <= maxx, "Ints only up to %d" % maxx
            assert s2 <= maxx, "Ints only up to %d" % maxx

            print("Hamming dist between {0:d} and {1:d} is {2:n}."
                  .format(s1, s2, hamming_numbers(s1, s2)))
        except ValueError:
            raise AssertionError("Inputs should be strings of digits.")
    else:
        print("Hamming dist between {0:s} and {1:s} is {2:n}."
              .format(s1, s2, hamming_strings(s1, s2)))
