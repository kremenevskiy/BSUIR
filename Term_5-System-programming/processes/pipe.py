from multiprocessing import Process, Pipe
import time

def f(conn):
    for i in range(4):
        time.sleep(4)
        conn.send([i**2, None, i])
    conn.close()


# def checkConee(conn):



if __name__ == '__main__':

    parent_conn, child_conn = Pipe()

    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    print(parent_conn.recv())
    print(parent_conn.recv())

    p.join()
