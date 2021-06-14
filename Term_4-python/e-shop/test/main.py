from threading import *


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


