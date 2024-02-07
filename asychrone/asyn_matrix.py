import asyncio
import random

ass = int(input("Введите длину одного списка: "))
ass_ass = int(input("Введите  кол-во списков: "))


async def async_generator():
    ass_list = []
    for a in range(ass_ass):
        ass_ass_list = []
        for i in range(ass):
            ass_ass_list.append(random.randint(0, 9))
        ass_list.append(ass_ass_list)
        print(f"Значение {ass_ass_list}")
        await asyncio.sleep(0.3)
    await asyncio.sleep(0.8)
    yield ass_list


async def main():
    # итератор по генератору
    o = 0
    async for a in async_generator():
        for i in a:
            o += 1
            print(f"Получена матрица, {o} список: {i}")
            await asyncio.sleep(0.6)
        print()


asyncio.run(main())
