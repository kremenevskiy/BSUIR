import numpy as np
from extra_tools import print_equation
from gauss_standart import *


def gauss_column_selection(matrix_a, answers_b, verbose=1):
    A = np.array(matrix_a, dtype=float)
    b = np.array(answers_b, dtype=float)
    x = list()
    n = A.shape[0]
    m = A.shape[1]

    if verbose == 1:
        print('Default matrix:')
        print_equation(A, b)

    # forward move
    for k in range(0, n):

        max_in_col = A[k, k]
        min_col = k
        for i in range(k+1, n):
            if (abs(A[i, k]) > abs(max_in_col)) & (A[i, k] != 0):
                max_in_col = A[i, k]
                min_col = i

        A[[min_col, k]] = A[[k, min_col]]
        b[[min_col, k]] = b[[k, min_col]]

        if verbose == 1:
            print(f'k={k})')
            print_equation(A, b)

        A, b = make_zeros(A, b, k, verbose)
    return compute_roots(A, b)
