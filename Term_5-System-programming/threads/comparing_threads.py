import threading
import time


def handler(started=0, finished=0):
    result = 0
    for i in range(started, finished):
        result += i
    results.append(result)


results = []
task1 = threading.Thread(target=handler, kwargs={'finished': 2**12})
task2 = threading.Thread(target=handler, kwargs={'started': 2**12, 'finished': 2**24})

started_at = time.time()

task1.start()
task2.start()

task1.join()
task2.join()
print('Results with Threads:')
print(f'Time: {time.time() - started_at}')
print('Result: ', sum(results))


results = []

started_at = time.time()

handler(finished=2**24)
print('\nResults no Threads:')
print(f'Time: {time.time() - started_at}')
print('Result: ', sum(results))



