"""
A map of streets is given, which has the shape of a rectangular grid
with N columns and M rows. At the intersections of these streets there
are people. They all want to meet at one single intersection. The goal
is to choose such an intersection, which minimizes the total walking
distance of all people. Remember that they can only walk along the streets
(the so called "Manhattan distance").
"""
import numpy as np


def distance_1d(array):
    return int(round(np.median(array)))


def distance_2d(matrix):
    matrix = np.array(matrix)
    h, w = matrix.shape
    row_vector, column_vector = [], []
    for r in range(h):
        column_vector.append(distance_1d(matrix[r]))
    for c in range(w):
        row_vector.append(distance_1d(matrix[:, c]))
    return (distance_1d(row_vector), distance_1d(column_vector))



if __name__ == '__main__':
    x, y = 10, 10
    start, finish = 1, 10
    matrix = np.array([np.random.random_integers(start, finish, x) for _ in range(y)])
    print('\nStreet:')
    print(matrix)
    print('\nMeeting point:')
    print(distance_2d(matrix))
