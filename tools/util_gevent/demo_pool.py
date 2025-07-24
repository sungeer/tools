from gevent.pool import Pool


def work(n):
    print(f'任务 {n} 开始')
    gevent.sleep(1)
    print(f'任务 {n} 完成')


pool = Pool(3)  # 最多允许 3 个并发任务

tasks = [pool.spawn(work, i) for i in range(10)]

pool.join()
print('所有任务处理完成')
