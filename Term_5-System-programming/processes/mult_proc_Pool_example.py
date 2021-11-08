from concurrent.futures import ProcessPoolExecutor
import concurrent.futures
import time
import sys
import os
import numpy


def sum_squared(nums):
    res = 0
    print(f'____ sum_squared working')
    for num in nums:
        res += num ** 2
    return res


if __name__ == "__main__":
    numbers = list(range(10**7))
    n_jobs = 10

    # one process
    start = time.time()

    for _ in range(n_jobs):
        sum_squared(numbers)

    finished = time.time()
    print(f'Time 1 Process: {finished-start}')

    # Multiprocessing

    start = time.time()
    with ProcessPoolExecutor() as executor:
        results = [executor.submit(sum_squared, numbers) for _ in range(n_jobs)]
        for f in concurrent.futures.as_completed(results):
            print(f.result())


    finished = time.time()
    print(f'Time Process executor: {finished - start}')
