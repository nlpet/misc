from collections import defaultdict, Counter


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
    twos, threes = 0, 0

    with open('input.txt', 'r') as fr:
        for line in fr:
            uniq_counts = set(Counter(line.strip()).values())
            twos += int(2 in uniq_counts)
            threes += int(3 in uniq_counts)

    print('Answer to part 1: {}'.format(twos * threes))


if __name__ == '__main__':
    main()
