from gevent import monkey

monkey.patch_all()

import gevent
import requests

urls = [
    'https://www.python.org',
    'https://www.github.com',
    'https://www.baidu.com',
]


def fetch(url):
    print(f'开始抓取: {url}')
    resp = requests.get(url)
    print(f'{url} 抓取完成，长度: {len(resp.text)}')
    return resp.text


tasks = [gevent.spawn(fetch, url) for url in urls]
gevent.joinall(tasks)

# 通过 task.value 获取的结果顺序与任务创建（也就是 urls 顺序）顺序一致
# 直接获取结果
results = [task.value for task in tasks]

# 输出每个结果的长度
for url, task in zip(urls, tasks):
    print(f'{url} 的内容长度: {len(task.value)}')
