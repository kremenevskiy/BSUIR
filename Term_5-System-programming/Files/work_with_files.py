import threading
import time


def write_to_file(timeout):
    with open('file_1.txt', 'a') as f:
        for i in range(10000):
            f.write(str(f'from thread: {threading.current_thread().name}\n'))
            # time.sleep(timeout)


if __name__ == '__main__':
    threads = []
    for i in range(3):
        t = threading.Thread(target=write_to_file, args=(1, ), name=f'Thread {i}')
        t.start()
        threads.append(t)

    print(threading.enumerate())

    for thread in threads:
        thread.join()

