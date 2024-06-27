import asyncio


async def print_delayed_message():
    await asyncio.sleep(2)
    print("Python Exercises!")


async def main():
    await print_delayed_message()

asyncio.run(main())
