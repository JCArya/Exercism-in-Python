from itertools import count
def outer_square(matrix, size, start, num_iter):
    if size <= 0:
        return
    x, y = start
    # Go right
    for i in range(y, y + size):
        matrix[x][i] = next(num_iter)
    # Go down
    for i in range(x + 1, x + size):
        matrix[i][y + size - 1] = next(num_iter)
    # Go left
    for i in range(y + size - 2, y - 1, -1):
        matrix[x + size - 1][i] = next(num_iter)
    # Go up
    for i in range(x + size - 2, x, -1):
        matrix[i][y] = next(num_iter)
    outer_square(matrix, size - 2, (x + 1, y + 1), num_iter)
def spiral_matrix(size):
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    outer_square(matrix, size, (0, 0), count(1))
    return matrix
