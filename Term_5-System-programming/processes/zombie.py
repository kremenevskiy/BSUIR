import os, sys, time

ttlForParent = 60
for i in range(0, 10):
    pid_1 = os.fork()
    print('hello worlds')
    if pid_1 == 0:
        print(os.getpid())
        sys.exit()

time.sleep(ttlForParent)
status = os.wait()
print(f'parent child id: {status[0]}')

