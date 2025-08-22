import time
import statistics


def wait_ms(ms=20):
    time.sleep(ms / 1000.0)
    return


def benchmark(n=10000, ms=5):
    errs = []
    for _ in range(n):
        t0 = time.perf_counter()
        wait_ms(5)
        t1 = time.perf_counter()
        err_ms = (t1 - t0) * 1000 - ms
        errs.append(err_ms)
    errs.sort()

    def p(q):  # 简单分位数
        idx = int(q * (len(errs) - 1))
        return errs[idx]

    print(f"样本数: {len(errs)}")
    print(f"平均误差: {statistics.mean(errs):.3f} ms, 中位数: {statistics.median(errs):.3f} ms")
    print(f"P90: {p(0.90):.3f} ms, P99: {p(0.99):.3f} ms, 最大: {errs[-1]:.3f} ms, 最小: {errs[0]:.3f} ms")


if __name__ == "__main__":
    benchmark()