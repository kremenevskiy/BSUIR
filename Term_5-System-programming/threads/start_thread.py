import threading
import time


def handler(started=0, finished=0):
    result = 0
    for i in range(started, finished):
        result += i
    print('Result: ', result)


params = {'finished': 2**26}
task = threading.Thread(target=handler, kwargs=params)
started_at = time.time()
print('Results with Thread:')
task.start()
task.join()
print(f'Time: {time.time() - started_at}\n')

started_at = time.time()
print('Results no Threads:')
handler(**params)
print(f'Time: {time.time() - started_at}')



