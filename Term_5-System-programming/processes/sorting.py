from multiprocessing import Manager, Process
import random
import time
import os
from concurrent.futures import ProcessPoolExecutor


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:

        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high


def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


def get_chunks_indexes(length, n_jobs):
    indexes = []
    chunk_size = length // n_jobs

    right = -1
    for _ in range(n_jobs):
        left = right + 1
        right = left + chunk_size - 1
        indexes.append([left, right])
    indexes[-1][-1] = length - 1
    return indexes


def parallel_sorting(array, n_jobs):
    # array = narray[:]

    # array shared поэтому медленно

    # print(array)
    result_arr = []
    processes = []
    chunks_ind = get_chunks_indexes(len(array), n_jobs)

    for i in range(n_jobs):
        p = Process(target=quick_sort, args=(array, chunks_ind[i][0], chunks_ind[i][1]))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    # print(array)



    print('Chunks are sorted! Making Last array...')

    if n_jobs == 2:
        i, j = 0, chunks_ind[1][0]

        while i <= chunks_ind[0][1] and j <= chunks_ind[1][1]:
            if array[i] <= array[j]:
                result_arr.append(array[i])
                i += 1
            else:
                result_arr.append(array[j])
                j += 1

        while i <= chunks_ind[0][1]:
            result_arr.append(array[i])
            i += 1

        while j <= chunks_ind[1][1]:
            result_arr.append(array[j])
            j += 1

    else:
        marked = [0] * len(array)
        start_ind = [chunk[0] for chunk in chunks_ind]
        while len(result_arr) != len(array):
            cmp_nums_d = {ind: array[i] for ind, i in enumerate(start_ind) if marked[i] == 0}
            cmp_nums = list(cmp_nums_d.values())
            min_el = min(cmp_nums)
            min_el_group = [k for k, v in cmp_nums_d.items() if v == min_el][0]

            min_el_index = [index for index, element in enumerate(array) if element == min_el and marked[index] == 0][0]
            if check_index_bounds(min_el_index, chunks_ind, min_el_group):
                start_ind[min_el_group] += 1
            marked[min_el_index] = 1

            result_arr.append(min_el)
    return result_arr


def check_index_bounds(min_el_index, chunks_ind, group):
    return min_el_index < chunks_ind[group][1]

    # started = [ind[0] for ind in chunks_ind[1:]]
    # return all(min_el_index < i for i in started)


if __name__ == '__main__':
    n_jobs = 2
    N = 2 ** 5
    MAX_NUM = 10**3

    not_sorted = [random.randint(0, MAX_NUM) for _ in range(N)]
    # not_sorted = [1, 8, 5, 1]
    # print('Starting Arr: ', not_sorted)
    arr_no_proc = not_sorted[:]
    arr_with_proc = not_sorted[:]
    shared_arr = Manager().list(arr_with_proc)

    print('Sorting array with no multiprocessing....')
    start = time.time()
    quick_sort(arr_no_proc, 0, len(arr_no_proc) - 1)
    # print('Sorted: ', arr_no_proc)
    print(f'Time sorting no processing: {time.time() - start}\n\n')

    start = time.time()
    result_python = sorted(not_sorted)
    # print('Sorted: ', result)
    print(f'Time Python sort: {time.time() - start}\n\n')

    print(f'Python == NotParallel: {arr_no_proc == result_python}')

    print(f'Sorting array with Multiprocessing....Cores: {n_jobs}')
    start = time.time()
    result = parallel_sorting(shared_arr, n_jobs)
    # print('Sorted: ', result)
    print(f'Time sorting with processing: {time.time() - start}\n\n')

    print(f'Parallel == Python: {result_python == result}')
