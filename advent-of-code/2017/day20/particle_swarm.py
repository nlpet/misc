# --- Day 20: Particle Swarm ---

from collections import namedtuple
from sys import maxsize


Point = namedtuple('Point', ['x', 'y', 'z'])


def distance(p1: Point, p2: Point):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y) + abs(p1.z - p2.z)


def get_point(p: str):
    return Point(*map(int, p[3:-1].strip().split(',')))


def main():
    o = Point(0, 0, 0)
    closest = {'acc': maxsize, 'particle': maxsize}

    with open('input.txt', 'r') as fr:
        for i, line in enumerate(fr.readlines()):
            a = get_point(line.strip().split(', ')[2])
            acc = sum(map(abs, a))
            if closest['acc'] > acc:
                closest['acc'] = acc
                closest['particle'] = i

    print(closest)



if __name__ == '__main__':
    main()
