import time
import random

def cach1(a):
    n = len(a)
    max_sum = a[0]
    for i in range(n):
        for j in range(i, n):
            cur = sum(a[i:j+1])
            if cur > max_sum: max_sum = cur
    return max_sum

def cach2(a):
    n = len(a)
    max_sum = a[0]
    for i in range(n):
        cur = 0
        for j in range(i, n):
            cur += a[j]
            if cur > max_sum: max_sum = cur
    return max_sum

def kadane(a):
    max_sum = a[0]
    cur_sum = a[0]
    for x in a[1:]:
        cur_sum = max(x, cur_sum + x)
        max_sum = max(max_sum, cur_sum)
    return max_sum

print("--- PYTHON BENCHMARK ---")
for n in [200, 400, 800]:
    random.seed(42)
    a = [random.randint(-100, 100) for _ in range(n)]

    t0 = time.perf_counter()
    cach1(a)
    t_c1 = time.perf_counter() - t0

    t0 = time.perf_counter()
    cach2(a)
    t_c2 = time.perf_counter() - t0

    t0 = time.perf_counter()
    for _ in range(1000):
        kadane(a)
    t_c3 = (time.perf_counter() - t0) / 1000

    print(f"n = {n} | Cach 1: {t_c1:.6f}s | Cach 2: {t_c2:.6f}s | Kadane: {t_c3:.8f}s")
