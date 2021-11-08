from multiprocessing import Process, Lock
import time

def print_arr(str):
    for i in str:
        time.sleep(0.005)
        print(i)


def print_ls(ls):
    num = []
    for i in ls:
        num.append(i)

        if len(num) > 10:
            time.sleep(1)
            for j in num:
                print(j, end=' ')
            num.clear()


if __name__ == '__main__':
    string = [str(i) + str('-') * 5 + ' ' for i in range(1000)]
    ls = [i**2 for i in range(1000)]
    p = Process(target=print_arr, args=(string,))
    p.start()
    print_ls(ls)