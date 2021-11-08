import time
import random
import queue


def task(name, work_queue):
    print('new task...')
    with open('Log_2.txt', 'a') as f:
        if work_queue.empty():
            f.write(f'Task {name} have nothing to do(\n')
            print(f'Task {name} have nothing to do(\n')
        while not work_queue.empty():
            delay = work_queue.get()
            start = time.time()
            # with open('Log.txt', 'a') as f:
            f.write(f'Task {name} started!\n')
            f.write(f'doing task ... N {name} : t-{delay}\n')
            print(f'doing task... {name}: t-{delay}')
            time.sleep(delay)
            f.write(f"Task {name} total elapsed time: {time.time() - start:.1f}\n")
            # print('queue', work_queue)
            print(bool(work_queue.empty()))


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

    i = 0
    while not work_queue.empty():
        task(str(i), work_queue)
        i += 1

    with open('Log_2.txt', 'a') as f:
        f.write(f'Time ended: {time.strftime("%H:%M:%S", time.localtime())}')
        f.write(f"\nTotal elapsed time: {time.time() - start:.1f}")


if __name__ == "__main__":
    main()
