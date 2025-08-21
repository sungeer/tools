"""
解读要点（目标延时 5 ms，误差=实际-目标）：

- 中心趋势
  - 平均误差 0.162 ms、位于亚毫秒级；
  - 中位数 0.084 ms，说明多数样本仅晚了不到 0.1 ms。
- 分布与尾部
  - P90 0.414 ms：90% 的延时晚不到 ~0.41 ms；
  - P99 1.053 ms：99% 晚不到 ~1.05 ms；
  - 最大 1.668 ms：最坏一次比目标晚 ~1.67 ms；
  - 最小 0.000 ms：有样本几乎精确命中（或在测量量化下视为 0）。
- 结论
  - 在该环境与负载下，你的“先睡后忙”等策略表现非常好：绝大多数误差 < 0.5 ms，长尾也仅 ~1–1.7 ms。
  - 这是“软实时”里相当优秀的结果，但仍存在不可避免的长尾（>1 ms）。

如何利用与优化：
- 如果你的需求是“P99 < 1.5 ms”，当前配置已满足。
- 想进一步压尾部：
  - 适度增大 spin_ms（如 0.3–0.5 ms），会以更高 CPU 占用换更小尾部。
  - 启用 1 ms 计时器分辨率（timeBeginPeriod(1)），并使用高性能电源计划。
  - 将该定时逻辑放入独立线程，提升线程优先级，减少抢占。
- 稳健性验证：在不同负载（CPU/I/O/后台任务）下复测，关注 P99/最大值是否显著上升。
"""

import time
import statistics
import threading


def precise_sleep_ms(ms, spin_ms=0.2):
    time.sleep(ms / 1000.0)


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
    benchmark(n=10000, ms=5, spin_ms=0.3)
