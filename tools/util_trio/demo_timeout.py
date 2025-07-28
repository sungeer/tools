import trio
import httpx


# 带超时的网络请求
async def fetch_with_timeout(url, timeout_seconds):
    try:
        with trio.move_on_after(timeout_seconds) as cancel_scope:
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                return response.text
        # 如果到了这里 说明超时了
        if cancel_scope.cancelled_caught:
            return f'请求 {url} 超时了'
    except Exception as e:
        return f'请求失败： {e}'


async def batch_fetch_demo():
    urls = [
        'https：//httpbin.org/delay/1',
        'https：//httpbin.org/delay/10',  # 这个会超时
        'https：//httpbin.org/delay/2'
    ]

    async with trio.open_nursery() as nursery:
        for url in urls:
            nursery.start_soon(fetch_with_timeout, url, 5)