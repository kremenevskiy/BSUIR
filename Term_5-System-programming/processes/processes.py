import multiprocessing
import time
import sys


def worker():
    name = multiprocessing.current_process().name
    print(f"{name} Process is started")
    print('...Working...')
    time.sleep(10)
    print(f"{name} Process is ended")
    return


def my_service():
    name = multiprocessing.current_process().name
    print(f"{name} Process is started")
    print('...Working...')
    time.sleep(10)
    print(f"{name} Process is ended")


def daemon():
    p = multiprocessing.current_process()
    print('Starting:', p.name, p.pid)
    sys.stdout.flush()
    time.sleep(20)
    print('Exiting :', p.name, p.pid)
    sys.stdout.flush()


def non_daemon():
    p = multiprocessing.current_process()
    print('Starting:', p.name, p.pid)
    sys.stdout.flush()
    time.sleep(10)
    print('Exiting :', p.name, p.pid)
    sys.stdout.flush()


def slow_worker():
    print('Starting worker')
    time.sleep(0.1)
    print('Finished worker')


if __name__ == '__main__':
    # jobs = []
    # for i in range(5):
    #     p = multiprocessing.Process(target=worker)
    #     jobs.append(p)
    #     p.start()

    # service = multiprocessing.Process(name='my_service', target=my_service)
    # worker_1 = multiprocessing.Process(name='worker 1', target=worker)
    # worker_2 = multiprocessing.Process(target=worker)  # use default name
    #
    # worker_1.start()
    # worker_2.start()
    # service.start()




    # d = multiprocessing.Process(name='daemon', target=daemon)
    # d.daemon = True
    #
    # n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    # n.daemon = False
    #
    # d.start()
    # # time.sleep(6)
    # n.start()
    #
    # d.join(5)
    # print(d.is_alive())
    # print(n.is_alive())



    p = multiprocessing.Process(target=slow_worker)
    print('BEFORE:', p, p.is_alive())

    p.start()
    print('DURING:', p, p.is_alive())

    p.terminate()
    # time.sleep(1)
    print('TERMINATED:', p, p.is_alive())

    p.join()
    print('JOINED:', p, p.is_alive())

