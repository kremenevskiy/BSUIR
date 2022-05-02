from multiprocessing import Process, Condition, Queue, Manager, current_process
import time
import random as rnd
import os


def now():
    return time.time()


def prepare():
    with open('consumers.txt', 'w') as f:
        pass
    with open('producers.txt', 'w') as f:
        pass
    with open('producers_all.txt', 'w') as f:
        pass


def write_file(filename, string):
    with open(filename, 'a') as f:
        f.write(f'{string}\n')


def producer(q, condition, shared_arr):
    numbers = []
    start = now()
    time_go = False

    while True:

        if now() - start > 15:
            str_nums = map(str, numbers)
            prod_nums = ', '.join(str_nums)
            all_nums = map(str, shared_arr)
            shared_str = ', '.join(all_nums)
            write_file('producers.txt', f'{current_process().name}: {prod_nums}\n\n')
            write_file('producers_all.txt', f'{current_process()}: {shared_str}\n\n')
            numbers.clear()
            start = now()

        num = rnd.randint(0, 100)
        with condition:
            q.put(num)
            condition.notify()

        numbers.append(num)
        shared_arr.append(num)

        print(f'{os.getpid()}: put {num}')
        time.sleep(1)

        if num == 100:
            print(f'{os.getpid()}: producer stopping')
            break


def consumer(q, condition):
    numbers = []
    start = now()
    while True:
        if now() - start > 15:
            str_nums = map(str, numbers)
            cons_nums = ', '.join(str_nums)
            write_file('consumers.txt', f'{current_process().name}: {cons_nums}\n\n')
            numbers.clear()
            start = now()

        while not q:
            condition.wait()
            print(f'{os.getpid()}: waiting for element...')

        num = q.get()
        numbers.append(num)
        print(f'{os.getpid()}: Took {num}')
        time.sleep(2)


if __name__ == '__main__':
    n_producer = 3
    n_consumer = 3
    prepare()
    queue = Queue()
    cond = Condition()
    shared_nums = Manager().list()
    producers = []
    consumers = []



    for i in range(n_producer):
        pr = Process(target=producer, args=(queue, cond, shared_nums, ), name=f'Producer-{i}')
        pr.start()
        producers.append(pr)

    for i in range(n_consumer):
        cons = Process(target=consumer, args=(queue, cond, ), name=f'Consumer-{i}')
        cons.start()
        consumers.append(cons)

    for i in producers and consumers:
        i.join()
