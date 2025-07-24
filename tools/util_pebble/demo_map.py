"""
ProcessPool() 创建了一个进程池（默认最大进程数是CPU核心数）
pool.map() 保证输出结果的顺序和输入参数列表（numbers）的顺序一致
results = list(future) 会阻塞，直到所有结果都收集完毕
for result in future 不保证结果顺序，谁先算完谁先输出
"""
import math

from pebble import ProcessPool


def complex_calculation(n):
    return sum(math.sqrt(i) for i in range(n))


numbers = [10 ** 6, 10 ** 7, 10 ** 6, 10 ** 7]

with ProcessPool() as pool:
    future = pool.map(complex_calculation, numbers)
    results = list(future)
