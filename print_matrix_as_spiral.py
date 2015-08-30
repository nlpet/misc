"""Print a n x m matrix as a spiral."""


def spiral(p, l, flag):
    """Create a spiral."""
    m, n = 50, 50
    matrix = [list(range(m)) for _ in range(n)]
    for row in matrix:
        for n in row:
            print('%s%d' % (' '*p, n))
            if p == l or p == 0:
                flag = not flag
            if flag:
                p += 1
            else:
                p -= 1

if __name__ == '__main__':
    p, l = 0, 5
    flag = False
    spiral(p, l, flag)
