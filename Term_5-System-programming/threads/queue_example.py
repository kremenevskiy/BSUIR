from queue import Queue
from threading import Thread
import time


def worker(q):
    while True:
        print(t1.is_alive())
        print(t2.is_alive())
        print('getting item')
        time.sleep(1)
        item = q.get()
        print(item)
        # q.task_done()


def master(q):
    for item in source:
        q.put(item)

    q.join()
    print('join passed')



q = Queue()
source = "hi friend"


t1 = Thread(target=worker, args=(q,))
t2 = Thread(target=master, args=(q,))

t1.start()
t2.start()


time.sleep(15)

print(t1.is_alive())
print(t2.is_alive())