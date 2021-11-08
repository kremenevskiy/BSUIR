import threading
import time
import sys


def producer():
    print(f'Set locking in {threading.current_thread().name}')

    with lock:
        print(f'locked {threading.current_thread().name}')
        time.sleep(2)
        sys.stdout.flush()
        # time.sleep(10)  # почему не работает потому что щелкает?
        with lock:
            print(f'its great 2nd lock in {threading.current_thread().name}')
    print(f'locking release in {threading.current_thread().name}')


lock = threading.RLock()
# lock.acquire()
# print(1)
# print(2)
# lock.release()


task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=producer)

task1.start()
task2.start()


task1.join()
task2.join()
