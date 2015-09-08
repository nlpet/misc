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
    """
    :list, np.array : array
    """
    return int(round(np.median(array)))


def distance_2d(matrix):
    """
    : n x n list of lists : matrix
    """
    matrix = np.array(matrix)
    height, width = matrix.shape
    row_vector, column_vector = [], []
    for row in range(height):
        column_vector.append(distance_1d(matrix[row]))
    for col in range(width):
        row_vector.append(distance_1d(matrix[:, col]))
    return (distance_1d(row_vector), distance_1d(column_vector))


if __name__ == '__main__':
    width, height = 10, 10
    start, finish = 1, 10
    mapp = np.array([np.random.random_integers(start, finish, width)
                    for _ in range(height)])
    print '\nGrid:'
    print mapp
    print '\nMeeting point:'
    print distance_2d(mapp)
