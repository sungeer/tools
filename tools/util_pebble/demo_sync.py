"""同步方法中的后台执行
在函数A中调用B函数（比如发送邮件），但希望B异步(后台执行)，不阻塞A继续往下走
不要用 future.result()，否则会阻塞等待结果
如果不关心 B 的执行结果，可以直接丢弃返回的 future
如果你希望 B 能捕获异常，可以为 future 设置回调或异常处理
"""
import time

from pebble import ThreadPool


def send_email(address, content):
    time.sleep(3)
    print(f'邮件已发送给：{address}')


pool = ThreadPool(max_workers=5)


def do_something():
    print('开始执行A任务')
    pool.schedule(send_email, args=('test@example.com', 'Hello, world!'))
    print('A中的其它逻辑继续执行...')


do_something()
