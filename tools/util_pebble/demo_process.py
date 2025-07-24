from gevent import monkey

monkey.patch_all()

from multiprocessing import current_process

import gevent
import requests
from pebble import ProcessPool

URLS = [
    'https://www.example.com',
    'https://www.python.org',
    'https://docs.python.org/3/library/asyncio.html',
]


def chunk_urls(urls, num_chunks):
    avg = len(urls) // num_chunks
    return [urls[i * avg:(i + 1) * avg] for i in range(num_chunks - 1)] + [urls[(num_chunks - 1) * avg:]]


def fetch(url):
    try:
        resp = requests.get(url, timeout=10)
        print(f"[{current_process().name}] Fetched {url} ({len(resp.text)} bytes)")
    except Exception as e:
        print(f"[{current_process().name}] Error fetching {url}: {e}")


def gevent_crawler(urls):
    print(f"[{current_process().name}] Start with {len(urls)} urls")
    jobs = [gevent.spawn(fetch, url) for url in urls]
    gevent.joinall(jobs)
    print(f"[{current_process().name}] Done.")


if __name__ == '__main__':
    num_processes = 4
    url_groups = chunk_urls(URLS, num_processes)

    with ProcessPool(max_workers=num_processes) as pool:
        # 提交每个进程的任务
        futures = []
        for i in range(num_processes):
            future = pool.submit(gevent_crawler, url_groups[i])
            futures.append(future)

        # 等待所有进程完成
        for future in futures:
            try:
                future.result()
            except Exception as e:
                print(f"Process error: {e}")
