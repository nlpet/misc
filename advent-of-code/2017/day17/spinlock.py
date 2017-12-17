# --- Day 17: Spinlock ---

from blist import blist
from time import time


def main() -> None:
    index = 0
    insertions = 1
    buffer = blist([0])
    step = 303
    start = time()

    while insertions <= 50000000:
        index = ((index + step) % insertions) + 1
        buffer.insert(index, insertions)
        insertions += 1

    print(buffer[1])
    print('Finished in {:.2}'.format(time() - start))


if __name__ == '__main__':
    main()
