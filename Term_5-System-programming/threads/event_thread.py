import threading
import time


def producer():
    time.sleep(10)
    print('Product created')
    product.set()
    product.clear()
    product.set()  # no deadlock


def consumer():
    print('product waiting')
    product.wait()
    print('product exists!')
    product.wait()  # deadlock


product = threading.Event()


task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=consumer)

task1.start()
task2.start()

task1.join()
task2.join()


