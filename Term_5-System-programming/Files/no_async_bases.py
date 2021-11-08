import time
import random
import queue


def task(name, work_queue):

    with open('Log_2.txt', 'a') as f:
        while not work_queue.empty():
            delay = work_queue.get()
            start = time.time()
            # with open('Log.txt', 'a') as f:
            f.write(f'Task {name} started!\n')
            time.sleep(delay)
            f.write(f"Task {name} total elapsed time: {time.time() - start:.1f}\n")


def main():
    with open('Log_2.txt', 'w') as f:
        f.write(f'Time now: {time.strftime("%H:%M:%S", time.localtime())}\n')

    work_queue = queue.Queue()

    n_work = 10**1
    works = [random.randint(0, 10) for _ in range(n_work)]
    for work in works:
        work_queue.put(work)

    start = time.time()

    tasks = []

    while work_queue.not_empty:
        i = 0
        task(str(i), work_queue)

    with open('Log_2.txt', 'a') as f:
        f.write(f'Time ended: {time.strftime("%H:%M:%S", time.localtime())}')
        f.write(f"\nTotal elapsed time: {time.time() - start:.1f}")


if __name__ == "__main__":
    main()
