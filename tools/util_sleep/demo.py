import time


def precise_sleep_ms(ms, spin_ms=0.2):
    # ms: 目标延时（毫秒）
    # spin_ms: 最后忙等窗口（毫秒），可根据机器调整为 0.1–0.5 ms
    deadline = time.perf_counter() + ms / 1000.0
    spin = spin_ms / 1000.0

    # 先睡到接近目标（若剩余时间比忙等窗口大，就先 sleep）
    remain = deadline - time.perf_counter()
    if remain > spin:
        time.sleep(remain - spin)

    # 后忙：自旋直到达到截止时间
    while time.perf_counter() < deadline:
        pass


start = time.perf_counter()
precise_sleep_ms(5, 0.5)
end = time.perf_counter()
elapsed_ms = (end - start) * 1000
print(f"耗时: {elapsed_ms:.3f} ms")




