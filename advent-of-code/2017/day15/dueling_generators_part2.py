# --- Day 15: Dueling Generators ---

from time import time
from typing import Generator


Factory = Generator[int, None, None]


def factory(value: int, factor: int, divisor: int, div_by: int) -> Factory:
    while 1:
        value = (value * factor) % divisor
        if value % div_by == 0:
            yield value


def main() -> None:
    count = 0
    mask = 2 ** 16 - 1
    # Test A: 65, Test B: 8921
    A = factory(883, 16807, 2147483647, 4)
    B = factory(879, 48271, 2147483647, 8)

    start = time()

    for i in range(5000000):
        a, b = A.__next__(), B.__next__()
        if a & mask == b & mask:
            count += 1

    print('The count is {}'.format(count))
    print('Finished in {:.2f}'.format(time() - start))


if __name__ == '__main__':
    main()
