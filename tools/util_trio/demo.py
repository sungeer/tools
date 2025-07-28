import trio
import httpx


async def fetch_url(url):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            return f'{url}: {response.status_code}'
        except Exception as e:
            return f'{url}: Error - {e}'


async def main():
    urls = [
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/2',
        'https://httpbin.org/delay/3'
    ]
    async with trio.open_nursery() as nursery:
        for url in urls:
            nursery.start_soon(fetch_url, url)


if __name__ == '__main__':
    trio.run(main)
