import asyncio
import aiohttp


async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    url_1 = "http://www.wikipedia.org/"
    url_2 = "http://www.google.com"
    task1 = asyncio.create_task(fetch_url(url_1))
    task2 = asyncio.create_task(fetch_url(url_2))
    data1 = await task1
    data2 = await task2
    print("Data from ", url_1, len(data1), "bytes")
    print("Data from ", url_2, len(data2), "bytes")

asyncio.run(main())
