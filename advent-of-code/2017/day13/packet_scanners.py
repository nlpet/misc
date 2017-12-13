# --- Day 13: Packet Scanners ---

from typing import List, Tuple


Layer = Tuple[int, int]
Layers = List[Layer]


def get_severity(pair: Layer) -> int:
    depth, range_ = pair
    return depth * range_ if depth % (range_ * 2 - 2) == 0 else 0


def get_lowest_delay(layers: Layers) -> int:
    while True:
        severities = sum(map(get_severity, layers))
        (delay, _), *_ = layers
        if severities == 0:
            return delay

        layers = [(d + 1, r) for d, r in layers]


def main() -> None:
    layers = []

    with open('test.txt', 'r') as fr:
        for line in fr.readlines():
            depth, range_ = map(int, line.strip().split(': '))
            layers.append((depth, range_))

    # Part 1
    severity = sum(map(get_severity, layers))
    print('The severity of the whole trip is {}'.format(severity))

    # Part 2
    lowest_delay = get_lowest_delay(layers)
    print('The fewest number of picoseconds is {}'.format(lowest_delay))


if __name__ == '__main__':
    main()
