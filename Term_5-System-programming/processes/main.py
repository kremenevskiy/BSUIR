import multiprocessing as mulp
import time

def workFunc():
    for i in range(10**10):
        print('hi')
    print('done')


if __name__ == "__main__":
    print('hi')