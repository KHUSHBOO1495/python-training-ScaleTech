import asyncio
import time

async def task(name):
    print(f"{name} started")
    await asyncio.sleep(2)
    print(f"{name} completed")

async def main():
    await task("Task 1")
    await task("Task 2")
    await task("Task 3")

start = time.time()
asyncio.run(main())
print(f"Time: {time.time() - start:.2f} seconds")




async def task(name):
    print(f"{name} started")
    await asyncio.sleep(2)
    print(f"{name} completed")

async def main():
    await asyncio.gather(
        task("Task 1"),
        task("Task 2"),
        task("Task 3")
    )

start = time.time()
asyncio.run(main())
print(f"Time: {time.time() - start:.2f} seconds")
