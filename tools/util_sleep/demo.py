import time


def wait_ms(ms=20):
    time.sleep(ms / 1000.0)
    return


start = time.perf_counter()
wait_ms()
end = time.perf_counter()
elapsed_ms = (end - start) * 1000
print(f"耗时: {elapsed_ms:.3f} ms")




