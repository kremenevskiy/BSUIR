import os, sys, time

print(f'Parent pid: {os.getpid()}')
pid = os.fork()

if pid == 0:
    print(f'im child: {os.getpid()}')
    time.sleep(3)
    os.execlp('ls', 'ls', '-a')  # replace
    time.sleep(2)
    print('closing child')
else:
    print(f'i m a parent: {os.getpid()}')
    time.sleep(7)
    print('closing parent')

