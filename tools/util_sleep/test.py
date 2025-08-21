"""
样本数: 10000 | 目标: 5 ms, spin: 0.2 ms
平均误差: 0.162 ms, 中位数: 0.084 ms
P90: 0.414 ms, P99: 1.053 ms, 最大: 1.668 ms, 最小: 0.000 ms
"""

import time
import statistics
import threading


def precise_sleep_ms(ms, spin_ms=0.2):
    deadline = time.perf_counter() + ms / 1000.0
    spin = spin_ms / 1000.0
    remain = deadline - time.perf_counter()
    if remain > spin:
        time.sleep(remain - spin)
    while time.perf_counter() < deadline:
        pass


def benchmark(n=10000, ms=5, spin_ms=0.2):
    errs = []
    for _ in range(n):
        t0 = time.perf_counter()
        precise_sleep_ms(ms, spin_ms)
        t1 = time.perf_counter()
        err_ms = (t1 - t0) * 1000 - ms
        errs.append(err_ms)
    errs.sort()

    def p(q):  # 简单分位数
        idx = int(q * (len(errs) - 1))
        return errs[idx]

    print(f"样本数: {len(errs)} | 目标: {ms} ms, spin: {spin_ms} ms")
    print(f"平均误差: {statistics.mean(errs):.3f} ms, 中位数: {statistics.median(errs):.3f} ms")
    print(f"P90: {p(0.90):.3f} ms, P99: {p(0.99):.3f} ms, 最大: {errs[-1]:.3f} ms, 最小: {errs[0]:.3f} ms")


if __name__ == "__main__":
    benchmark(n=10000, ms=5, spin_ms=0.8)
