import multiprocessing as mp
import time
import sys
import os
import numpy


def sum_squared(nums):
    res = 0
    for num in nums:
        res += num ** 2
    print(f'____ Sum : {res}')


if __name__ == "__main__":
    numbers = list(range(10**7))
    n_jobs = 5

    # one process
    start = time.time()

    for _ in range(n_jobs):
        sum_squared(numbers)

    finished = time.time()
    print(f'Time 1 Process: {finished-start}')

    # Multiprocessing
    start = time.time()
    processes = []
    for _ in range(n_jobs):
        p = mp.Process(target=sum_squared, args=(numbers,))
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finished = time.time()
    print(f'Time 2 Processes: {finished - start}')








