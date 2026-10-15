import time
import random

def benchmark():
    n = 1000000
    k = 1000
    random.seed(42)
    a = [random.randint(-100, 100) for _ in range(n)]

    print("--- PYTHON BENCHMARK (n=10^6, k=1000) ---")

    # Đo ngây thơ trên mẫu 1000 bước rồi ngoại suy
    sample_steps = 1000
    t0 = time.perf_counter()
    max_sum = -float('inf')
    for i in range(sample_steps):
        cur = sum(a[i:i+k])
        if cur > max_sum: max_sum = cur
    t_sample = time.perf_counter() - t0
    t_ngay_tho = t_sample * ((n - k + 1) / sample_steps)

    # Đo cửa sổ trượt
    t0 = time.perf_counter()
    cur = sum(a[:k])
    max_sum = cur
    for i in range(k, n):
        cur += a[i] - a[i - k]
        if cur > max_sum:
            max_sum = cur
    t_truot = time.perf_counter() - t0

    print(f"Ngay tho O(n*k) : {t_ngay_tho:.4f}s")
    print(f"Cua so truot O(n): {t_truot:.4f}s")
    print(f"Ti le nhanh hon : {(t_ngay_tho / t_truot):.2f} lan")

if __name__ == "__main__":
    benchmark()
