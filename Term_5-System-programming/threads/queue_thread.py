import threading
from collections import deque
import time
import random as rd
import queue

q = deque()
cond = threading.Condition()


def producer():
    while True:

        cond.acquire()
        num = rd.randint(0, 10)
        q.append(num)
        cond.notify()
        cond.release()
        time.sleep(5)
        if num == 7:
            break


def consumer():

    while True:
        cond.acquire()
        while not q:
            cond.wait()

        num = q.popleft()
        cond.release()
        print(f'Number : {num} got')
        if num == 7:
            break



t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()






