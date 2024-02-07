import asyncio


async def niger():
    print("Начинающий нигер")
    await asyncio.sleep(1)
    print("Завершенный нигер")


async def niger_2():
    print("Второй начинающий нигер")
    await asyncio.sleep(1.5)
    print("Второй завершенный нигер")


async def main_niger():
    await asyncio.gather(niger(), niger_2())


asyncio.run(main_niger())
