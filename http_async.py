"""
Summary:
    Simple way to run synchronous tasks asynchronously
Description:
    Good video about this from ArjanCodes
    - https://www.youtube.com/watch?v=GpqAQxH1Afck"""
import asyncio
from time import perf_counter

import requests


async def counter(until: int = 10) -> None:
    now = perf_counter()
    print("Started")
    for i in range(0, until):
        last = now
        await asyncio.sleep(0.01)
        now = perf_counter()
        print(f"{i}: Was asleep for {now - last}")


def send_request(url: str) -> int:
    print("Sending HTTP request")
    response = requests.get(url)
    return response.status_code


async def send_async_request(url: str) -> int:
    return await asyncio.to_thread(send_request, url)


async def main() -> None:
    # time_before = perf_counter()
    task = asyncio.create_task(counter())
    code = await send_async_request("https://www.arjancodes.com")
    print(f"Got response: {code}")
    await task


async def main_gather_simple() -> None:
    status_code, *_ = await asyncio.gather(
        send_async_request("https://www.arjancodes.com"), counter()
    )
    print(status_code)


if __name__ == "__main__":
    asyncio.run(main_gather_simple())
