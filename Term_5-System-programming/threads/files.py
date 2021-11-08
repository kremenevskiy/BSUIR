import itertools
import threading
import queue


import string
import random

with open('test.txt', 'w') as f:
    for _ in range(20):
        line = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
        print(line, file=f)


def extract_from_queue(queue):
    while not queue.empty():
        yield queue.get()


def count_characters(lines, accumulator):
    length = sum(len(line) - 1 for line in lines)
    accumulator.put(length)


def count_characters_in_file(filename, chunk_size=200000):
    threads = []
    lengths = queue.Queue()

    with open(filename) as f:
        while True:
            print('1')
            lines = list(itertools.islice(f, 4))
            print(lines)

            if not lines:
                break
            t = threading.Thread(target=count_characters, args=(lines, lengths))
            t.start()
            threads.append(t)

    for t in threads:
        t.join()
    return sum(extract_from_queue(lengths))


if __name__ == '__main__':
    import sys
    print(count_characters_in_file('test.txt'))