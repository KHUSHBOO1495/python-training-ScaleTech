def get_numbers():
    for i in range(5):
        yield i
numbers = get_numbers()
for number in numbers:
    print(number)


import asyncio

async def hello():
    print("Hello")
    await asyncio.sleep(2)
    print("World")
asyncio.run(hello())
