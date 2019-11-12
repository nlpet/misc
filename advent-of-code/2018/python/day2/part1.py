from collections import defaultdict


def get_matches(box_id):
    counts, matches = defaultdict(int), {2: False, 3: False}

    for ch in box_id:
        counts[ch] += 1

        if counts[ch] in {2, 3}:
            matches[counts[ch]] = True

            if matches[2] and matches[3]:
                break

    return int(matches[2]), int(matches[3])


def main():
    counts = [0, 0]

    with open('input.txt', 'r') as fr:
        for line in fr:
            twos, threes = get_matches(line.strip())
            counts[0] += twos
            counts[1] += threes

    print('Answer to part 1: {}'.format(counts[0] * counts[1]))


if __name__ == '__main__':
    main()
