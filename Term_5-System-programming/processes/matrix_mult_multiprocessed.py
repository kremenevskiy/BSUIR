import numpy as np
import multiprocessing
import concurrent.futures as concur
import time
import functools
import os


def matrix_multiply(A, B, start=None):
    dim = A.shape[1]
    if start is None:
        arr = np.zeros(shape=(A.shape[0], B.shape[1]), dtype=int)
        for i in range(A.shape[0]):
            for j in range(dim):
                for k in range(dim):
                    arr[i, j] += A[i, k] * B[k, j]
        return arr

    arr = np.zeros(dim, dtype=int)
    for i in range(dim):
        for j in range(dim):
            arr[i] += A[start][j] * B[j][i]
    # time.sleep(10)
    return arr


def matrix_parallel(A, B, n_jobs=4):
    n_rows = A.shape[0]
    with concur.ProcessPoolExecutor(n_jobs) as executor:
        rows = list(range(n_rows))
        multiply_partial = functools.partial(matrix_multiply, A, B)
        print('...working...')
        results = executor.map(multiply_partial, rows)

        # result = np.array([*results])
        # print('..unpacking..')
    print('..done..')
    return results


def now():
    return time.time()


if __name__ == '__main__':
    A = np.array([[1, 2, 3],
                  [1, 2, 2],
                  [2, 3, 1]])
    B = np.array([[1, 1, 1],
                  [2, 1, 2],
                  [1, 1, 2]])

    n_cores = [i for i in range(1, 5)]
    n_rows = 300
    max_num = 10**3
    A = np.random.randint(max_num, size=(n_rows, n_rows))
    B = np.random.randint(max_num, size=(n_rows, n_rows))

    print(f'Matrices dimension:\n\t'
          f'A: {A.shape[0]} * {A.shape[1]}\n\t'
          f'B: {B.shape[0]} * {B.shape[1]}\n')

    print(f'\tNumpy multiplication...')
    start = now()
    result_numpy = np.dot(A, B)
    print(f'Time: {now() - start} s\n')

    for core in n_cores:
        print(f'\tParallel multiplication with {core} core...')
        start = now()
        result_multi = matrix_parallel(A, B, core)
        print(f'Time: {now() - start} s\n')

    print(f'\tSynchronous with 1 core multiplication...')
    start = now()
    result_no_parallel = matrix_multiply(A, B)
    print(f'Time: {now() - start} s\n')

    print('\b\tValidation:')
    print(f'Numpy == Parallel: {np.array_equal(result_numpy, np.array([*result_multi]))}')
    print(f'Numpy == NoParallel: {np.array_equal(result_numpy, result_no_parallel)}')
