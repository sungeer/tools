"""协程中独立运行同步函数
@asynchronous.thread 装饰器会自动把被装饰的同步函数放到 Pebble 管理的线程池中执行
每次调用这个函数，相当于向线程池提交了一个任务，线程池会调度可用线程来执行它
"""
import asyncio

from pebble import asynchronous


@asynchronous.thread
def sync_func(x):
    # 这里的代码会在 Pebble 的线程池中的某个线程里执行
    return x * 2


async def main():
    result = await sync_func(10)
    print(result)


asyncio.run(main())
