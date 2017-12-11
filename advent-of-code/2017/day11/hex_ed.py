# --- Day 11: Hex Ed ---

from typing import Tuple

"""
                         -z (N)  *
                                 *
                                 *
                               ,. ,.
                           .,        ..
                        ,.               ,.
                    ,,                      .,
                    .  .                  .. ,
                    .     ..          ..     ,
                    .         .    ..        ,
 +y (NW) *          .            .           ,          *  +x (NE)
            *       .            .           ,       *
               *    .            .           ,    *
                  * .            .           , *
                 .,   .,         .        .,   ..
              ..          ,      .     ..         .,
           ,.                ..  .  ,                 ,.
        ,                       .,                       ..
        ,  ..                ..  .  ..                ..  .
        ,      .         ..      .      .         ..      .
        ,         .   ..         .         .   ..         .
        ,           .            .           .            .
        ,           .            .           .            .
        ,           .            .           .            .
        ,           .            .           .            .
      *    ,        .        .,  *  ,        .        .,     *
  *           ,.    .     ,      *     ,.    .     ,             *
-x (SW)           . . .,         *         . . .,               -y (SE)
                                 *
                         +z (S)  *

"""

Point = Tuple[int, int, int]


def distance(a: Point, b: Point) -> int:
    return int((abs(a[0] - b[0]) +
                abs(a[1] - b[1]) +
                abs(a[2] - b[2])) / 2)


def move_south(x: int, y: int, z: int) -> Point:
    return x - 1, y, z + 1


def move_north(x: int, y: int, z: int) -> Point:
    return x + 1, y, z - 1


def move_northwest(x: int, y: int, z: int) -> Point:
    return x, y + 1, z - 1


def move_southeast(x: int, y: int, z: int) -> Point:
    return x, y - 1, z + 1


def move_northeast(x: int, y: int, z: int) -> Point:
    return x + 1, y - 1, z


def move_southwest(x: int, y: int, z: int) -> Point:
    return x - 1, y + 1, z


def main() -> None:
    origin = (0, 0, 0)
    move = {
        's': move_south, 'n': move_north,
        'nw': move_northwest, 'ne': move_northeast,
        'se': move_southeast, 'sw': move_southwest
    }

    with open('input.txt', 'r') as fr:
        for line in fr.readlines():
            x, y, z, furthest = 0, 0, 0, 0
            for direction in line.strip().split(','):
                x, y, z = move[direction](x, y, z)
                dist = distance(origin, (x, y, z))
                if dist > furthest:
                    furthest = dist

            dist = distance(origin, (x, y, z))
            print('Point is {} steps away'.format(dist))
            print('Futhest point was at {} steps away'.format(furthest))


if __name__ == '__main__':
    main()
