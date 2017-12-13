# --- Day 13: Packet Scanners ---

from typing import List, Any
from operator import add, sub


Layers = List[Any]

DIRECTIONS = {
    True: add,
    False: sub
}


def cycle(layers: Layers) -> None:
    for depth, items in enumerate(layers):
        if items:
            index, range_, direction = items
            new_index = DIRECTIONS[direction](index, 1)
            if new_index <= 0 or new_index >= range_ - 1:
                layers[depth][2] = not layers[depth][2]
            layers[depth][0] = new_index % range_


def move_packet(layers: Layers, packet_index: int) -> int:
    if layers[packet_index] and layers[packet_index][0] == 0:
        return packet_index * layers[packet_index][1]
    return 0


def main() -> None:
    layers_dict = {}
    severity = 0
    packet_index = 0

    with open('input.txt', 'r') as fr:
        for line in fr.readlines():
            depth, range_ = map(int, line.strip().split(': '))
            layers_dict[depth] = [0, range_, True]

    layers = [layers_dict.get(l) for l in range(0, max(layers_dict) + 1)]

    for picosecond in range(len(layers)):
        severity += move_packet(layers, packet_index)
        cycle(layers)
        packet_index += 1

    print('The severity of the whole trip is {}'.format(severity))


if __name__ == '__main__':
    main()
