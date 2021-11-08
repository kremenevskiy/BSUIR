import asyncio
import aiofiles
import time
import random


async def task(name, work_queue, f):
    try:
        while not work_queue.empty():
            delay = await work_queue.get()
            start = time.time()
            # with open('Log.txt', 'a') as f:
            await f.write(f'Task {name} started!\n')
            await asyncio.sleep(delay)
            await f.write(f"Task {name} total elapsed time: {time.time() - start:.1f}\n")
    finally:
        f.close()


async def main():
    async with aiofiles.open('Log.txt', 'w') as f:
        await f.write(f'Time now: {time.strftime("%H:%M:%S", time.localtime())}\n')

        work_queue = asyncio.Queue()
        n_tasks = 10**4
        n_work = 10**4
        works = [random.randint(0, 10) for _ in range(n_work)]
        for work in works:
            await work_queue.put(work)

        start = time.time()

        tasks = []
        for taska in range(n_tasks):
            tasks.append(asyncio.create_task(task(f'task-{taska}', work_queue, f)))

        await asyncio.gather(
            *tasks
        )

        await f.write(f'Time ended: {time.strftime("%H:%M:%S", time.localtime())}')
        await f.write(f"\nTotal elapsed time: {time.time() - start:.1f}")


if __name__ == "__main__":
    asyncio.run(main())
