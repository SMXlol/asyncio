import requests
import asyncio

urls = ['https://www.1tv.ru/news', 'https://www.dns-shop.ru/?utm_medium=organic&utm_source=google&utm_referrer=https'
                                   '%3A%2F%2Fwww.google.com%2F',
        'https://music.yandex.ru/', 'https://www.gosuslugi.ru/', 'https://www.aviasales.ru/']


async def receiving():
    for i in urls:
        page = requests.get(i)
        print(f"Сайт {i}:")
        status = page.status_code
        await asyncio.sleep(1)
        yield status


async def main():
    async for a in receiving():
        print(f"Статус доступности сайта: {a}")
        print()
        await asyncio.sleep(1)


asyncio.run(main())
