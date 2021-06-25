import numpy as np
matrix = np.array([
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 1, 1]
])


def get_islands(matrix):

    def check_title(nn, mm):
        if nn >= n or nn < 0 or mm >= m or mm < 0:
            return 0
        if marked[nn, mm]:
            return 0

        marked[nn, mm] = 1
        if matrix[nn, mm] == 0:
            return 0
        else:

            check_title(nn-1, mm)
            check_title(nn+1, mm)
            check_title(nn, mm-1)
            check_title(nn, mm+1)
        return 1

    n = matrix.shape[0]
    m = matrix.shape[1]
    marked = np.zeros((n, m))

    islands_cnt = 0
    for i in range(n):
        for j in range(m):
            islands_cnt += check_title(i, j)
    return islands_cnt


print(get_islands(matrix))