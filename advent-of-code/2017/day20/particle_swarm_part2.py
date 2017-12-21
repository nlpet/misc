# --- Day 20: Particle Swarm ---

import numpy as np

from collections import Counter
from functools import partial
from typing import Set, Dict, Any, Tuple, List


Vector = np.array
Point = Tuple[int, int, int]
Properties = Dict[str, Vector]
Particles = Dict[int, Properties]


def get_point(p: str) -> Vector:
    return np.array([int(n) for n in p[3:-1].strip().split(',')])


def tick(props: Properties) -> Vector:
    return np.array(list(map(sum, zip(props['pos'],
                                      props['vel'],
                                      props['acc']))))


def collided(c: Counter, ps: Properties):
    return c[tuple(ps['pos'])] > 1


def run(sim: int, particles: Particles) -> Particles:
    for i, props in particles.items():
        vel = props['vel'] + props['acc']
        props['pos'] = props['pos'] + vel
        props['vel'] = vel

    c = Counter([tuple(p['pos']) for p in particles.values()])
    survived = {p: ps for p, ps in particles.items() if not collided(c, ps)}
    return survived


def main():
    particles = {}

    with open('input.txt', 'r') as fr:
        for i, line in enumerate(fr.readlines()):
            p, v, a = map(get_point, line.strip().split(', '))
            particles[i] = {'pos': p, 'vel': v,
                            'acc': a, 'next': np.array([])}

    for sim in range(100):
        particles = run(sim, particles)

    print(len(particles))


if __name__ == '__main__':
    main()
