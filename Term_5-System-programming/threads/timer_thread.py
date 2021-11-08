import threading
import os


def exec_watcher():
    timer = threading.Timer(5, print_files)
    timer.start()


def print_files():
    for i in os.listdir('.'):
        print(i)
    exec_watcher()


exec_watcher()
