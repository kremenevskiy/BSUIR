import os, sys, time

# ps aux | grep 'Z'
print(f"main process: {os.getpid()}\n")
ttlForParent = 60
for i in range(0, 10):
    # time.sleep(3)
    pid_1 = os.fork()
    print(f"Hello from {os.getpid()}")
    if pid_1 == 0:
        sys.exit()
    else:
        # time.sleep(5)
        # os.wait()
        print(f'not ended: {os.getpid()}')

        
time.sleep(ttlForParent)
os.wait()

