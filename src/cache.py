import asyncio
from datetime import datetime, timedelta

from redis.asyncio import Redis


def seconds_until_next_1411(now=None) -> int:
    now = now or datetime.now()
    t = now.replace(hour=14, minute=11, second=0, microsecond=0)
    if now > t:
        t += timedelta(days=1)
    return int((t - now).total_seconds())



r = Redis(host="localhost", port=6379, db=0, decode_responses=True)


async def set(key, value):
    await r.set(key, value, ex=seconds_until_next_1411())


async def get(key):
    return await r.get(key)


async def shutdown():
    await r.aclose()



async def main():
    print(await get("dev"))
    print(await get("ewrverf"))



if __name__ == "__main__":
    asyncio.run(main())
