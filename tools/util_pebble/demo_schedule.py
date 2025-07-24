"""进程池
最多同时运行4个进程（即并行4个任务）
每个进程最多可执行10个任务后会被回收重启（防止内存泄漏等问题）
pool.schedule() 会立即返回一个 Future 对象，代表一个异步任务
当 pool.schedule 提交100个任务时，pebble 会自动调度这些任务，把它们分配到这4个进程上并行处理
这意味着同一时刻，最多有4个任务在同时运行，分别在4个独立的进程里
不保证结果顺序与输入顺序一致
"""
from pebble import ProcessPool


def worker(x):
    return x * 2


with ProcessPool(max_workers=4, max_tasks=10) as pool:
    futures = [pool.schedule(worker, args=(i,)) for i in range(100)]
    results = [f.result() for f in futures]
