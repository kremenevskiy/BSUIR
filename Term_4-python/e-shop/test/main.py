from threading import *
from multiprocessing import Process
import os
import math



class GreetHi(Thread):
    def run(self):
        for i in range(5000):
            print('Hi')


class GreetHello(Thread):
    def run(self):
        for i in range(5000):
            print('Hello')


t1 = GreetHi()
t2 = GreetHello()

t1.start()
t2.start()


# other staff
def calc():
    for i in range(0, 4000000):
        math.sqrt(i)


threads = []


for i in range(os.cpu_count()):
    print('registered thread %d' % i)
    threads.append(Thread(target=calc))


for thread in threads:
    thread.start()

for thread in threads:
    thread.join()


# multiprocessing
processes = []

for i in range(os.cpu_count()):
    print('registered process %d' % i)
    threads.append(Process(target=calc))

for process in processes:
    process.start()

for process in processes:
    process.join()


