import asyncio
import time
import aiohttp


def now():
    return time.time()


async def task(name, work_queue):
    async with aiohttp.ClientSession() as session:
        while not work_queue.empty():
            url = await work_queue.get()
            print(f"Task {name} getting URL: {url}")
            start = now()
            async with session.get(url) as response:
                await response.text()
            print(f"Task {name} total elapsed time: {now() - start:.1f}")


async def main():
    work_queue = asyncio.Queue()
    for url in [
        "http://google.com",
        "http://yahoo.com",
        "http://linkedin.com",
        "http://apple.com",
        "http://microsoft.com",
        "http://facebook.com",
        "http://twitter.com",
    ]:
        await work_queue.put(url)
    # Run the tasks
    start = now()
    await asyncio.gather(
        asyncio.create_task(task("One", work_queue)),
        asyncio.create_task(task("Two", work_queue)),
    )
    print(f"\nTotal elapsed time: {now() - start:.1f}")


if __name__ == "__main__":
    asyncio.run(main())