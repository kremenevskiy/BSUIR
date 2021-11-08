import threading
import time


def producer():
    with lock:
        print(f'Set locking: {lock._value}  in {threading.current_thread().name}')
        time.sleep(3)
        print(f'im free {threading.current_thread().name}')


max_workers = 5
lock = threading.BoundedSemaphore(value=max_workers)


task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=producer)
task3 = threading.Thread(target=producer)
task4 = threading.Thread(target=producer)
task5 = threading.Thread(target=producer)

task1.start()
task2.start()
task3.start()
task4.start()
task5.start()

task1.join()
task2.join()
task3.join()
task4.join()
task5.join()
 

