"""Shuffle array in place."""
from random import randint


def shuffle(array):
    length = len(array)
    for i in range(length - 1):
        r = randint(i, length - 1)
        array[i], array[r] = array[r], array[i]
    return array


if __name__ == '__main__':
    array = list(range(-10, 11))
    print(' '.join([str(n) for n in array]))
    shuffled_array = shuffle(array)
    print(' '.join([str(n) for n in shuffled_array]))
