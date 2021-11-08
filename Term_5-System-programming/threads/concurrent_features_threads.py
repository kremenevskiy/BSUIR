from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


def handler(started=0, finished=0):
    # print('VALUES: ', started, finished)
    result = 0
    for i in range(started, finished):
        result += i
    return result


def run_by_executor(executor_class, n_jobs=2):
    executor = executor_class(max_workers=n_jobs)
    started = time.time()
    future1 = executor.submit(handler, started=0, finished=2**26)
    future2 = executor.submit(handler, started=2**26, finished=2**28)
    print('waiting for result...')
    result = future2.result() + future2.result()
    print(f'Result: {result}. Time for {executor_class.__name__}: {time.time() - started}')


def run_by_executor_map(executor_class, n_jobs=2):
    executor = executor_class(max_workers=n_jobs)
    started = time.time()
    params = [
        [0, 2**26],
        [2**26, 2**28]
    ]
    result = sum(executor.map(handler, *params))
    print(f'Result: {result}. Time for {executor_class.__name__}: {time.time() - started}')


if __name__ == '__main__':
    print('Execute using map...')
    run_by_executor_map(ThreadPoolExecutor)
    run_by_executor_map(ProcessPoolExecutor)

    print('Execute using submit...')
    run_by_executor(ThreadPoolExecutor)
    run_by_executor(ProcessPoolExecutor)
