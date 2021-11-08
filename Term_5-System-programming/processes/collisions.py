from multiprocessing import Process, Lock, Manager
import time
import random
import os


def now():
    return time.time()


def add_num_no_lock(arr, lock, num):

    if num not in arr:
        print('waiting... in ', os.getpid())
        time.sleep(2)
        arr.append(num)
        # print(f'Process: {os.getpid()} added {num}')
    else:
        print(f'Process: {os.getpid()} value {num} already in arr')


def add_num(arr, lock, num):
    with lock:
        if num not in arr:
            print('waiting... in ', os.getpid())
            time.sleep(2)
            arr.append(num)
            # print(f'Process: {os.getpid()} added {num}')
        else:
            print(f'Process: {os.getpid()} value {num} already in arr')


def producer(arr, lock):
    start = now()
    while now() - start < 10:
        num = random.randint(0, 10)
        print(f'Process: {os.getpid()} putting {num}')
        add_num(arr, lock, num)
        # add_num_no_lock(arr, lock, num)





if __name__ == '__main__':
    manager = Manager()
    shared_lock = Manager().Lock()
    shared_arr = manager.list()
    print(f'Array at start: {list(shared_arr)}')
    processes = []
    n_jobs = 4
    for i in range(n_jobs):
        p = Process(target=producer, args=(shared_arr, shared_lock, ))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print(f'Array: {shared_arr}')









