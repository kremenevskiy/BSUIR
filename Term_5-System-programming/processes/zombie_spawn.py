import os, sys, time

print(f'Parent pid: {os.getpid()}')
# pid = os.fork()

while True:
    # time.sleep(5)
    if os.fork() == 0:
        print(f'child started and done: {os.getpid()}')
        time.sleep(2)
        # sys.exit()  # remove and don't die don't remove from table
    else:
        # os.wait()
        print(f'parent not die: {os.getpid()}')
        time.sleep(5)
