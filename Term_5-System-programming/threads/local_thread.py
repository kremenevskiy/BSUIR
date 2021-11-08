import threading

print(threading.active_count())
current = threading.current_thread()
print('Thread name: ', current.getName())
print('Thread alive: ', current.is_alive())

try:
    current.start()
except RuntimeError as e:
    print(f'ERROR: {e}')

current.setName('Super Thread')
print(f'New thread name: {current.getName()}')


current.name = 'SuperThread_1'
print(current.name)  # то же самое
print(current.getName())

# all working threads
print(threading.enumerate())


# Thread safe storing
thread_data = threading.local()
thread_data.value = 5


def print_thread_local():
    print(f'Current thread: {threading.current_thread()}')
    print(f'Local value: {thread_data.value}')


def counter(started, end_value):
    print(f'has value attr: {hasattr(thread_data, "value")}')
    thread_data.value = started
    for i in range(end_value):
        thread_data.value += 1
    print_thread_local()


task1 = threading.Thread(target=counter, args=(0, 10), name='Task1')
task2 = threading.Thread(target=counter, args=(100, 3), name='Task2')
task1.name = 'task1'
task2.name = 'task2'

task1.start()
task2.start()

print_thread_local()

task1.join()
task2.join()

print_thread_local()