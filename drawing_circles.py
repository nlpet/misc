"""Drawing a circle."""
from __future__ import division
import matplotlib.pyplot as plt
import math


def bresenham(x0, y0, x1, y1):
    x_points, y_points = [], []
    if x0 == x1 and y0 == y1:
        return [0], [0]

    dx = x1 - x0
    sx = -1 if dx < 0 else 1
    dy = y1 - y0
    sy = -1 if dy < 0 else 1

    if math.fabs(dy) < math.fabs(dx):
        m = dy / dx
        b = y0 - m * x0

        while x0 != x1:
            x_points.append(x0)
            y_points.append(int(round(m * x0 + b)))
            x0 += sx
    else:
        m = dx / dy
        b = x0 - m * y0

        while y0 != y1:
            x_points.append(int(round(m * y0 + b)))
            y_points.append(y0)

    x_points.append(x1)
    y_points.append(y1)
    return (x_points, y_points)


def draw(x_points, y_points):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    p = ax.plot(x_points, y_points, 'b')
    ax.set_xlabel('x-points')
    ax.set_ylabel('y-points')
    ax.set_title('Simple XY point plot')
    fig.show()


if __name__ == '__main__':
    x_points, y_points = bresenham(0, 10, 10, 1)
    print x_points
    print y_points
    draw(x_points, y_points)
