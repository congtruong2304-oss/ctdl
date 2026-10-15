import time
from time import perf_counter
import random

# Cách 2 của Bài 39: O(n^2)
def cach2(a: list) -> int:
    n = len(a)
    max_sum = a[0]
    for i in range(n):
        cur = 0
        for j in range(i, n):
            cur += a[j]
            if cur > max_sum:
                max_sum = cur
    return max_sum

def do_thoi_gian(f, a: list, lap: int = 3) -> float:
    times = []
    for _ in range(lap):
        t0 = perf_counter()
        f(a)
        times.append(perf_counter() - t0)
    return min(times)

def main():
    random.seed(42)
    Ns = [500, 1000, 2000, 4000]
    py_times = []

    print("--- PYTHON BENCHMARK O(n^2) ---")
    for n in Ns:
        a = [random.randint(-100, 100) for _ in range(n)]
        t = do_thoi_gian(cach2, a, lap=3)
        py_times.append(t)
        print(f"n = {n} : {t:.6f}s")

    print("\n--- TI LE TANG ---")
    for i in range(1, len(Ns)):
        print(f"n = {Ns[i-1]} -> {Ns[i]} : ti le = {py_times[i] / py_times[i-1]:.2f}")

    # Tạo đồ thị bằng matplotlib
    try:
        import matplotlib.pyplot as plt
        plt.figure(figsize=(7, 4.5))
        plt.plot(Ns, py_times, marker='o', color='crimson', linewidth=2, label="Python O(n²)")
        plt.title("Thời gian chạy của thuật toán O(n²)", fontsize=12, fontweight='bold')
        plt.xlabel("Kích thước dữ liệu n", fontsize=10)
        plt.ylabel("Thời gian chạy (giây)", fontsize=10)
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.legend()
        plt.tight_layout()
        plt.savefig("do_thi_bai44.png", dpi=300)
        print("\nDa xuat do thi thanh cong: 'do_thi_bai44.png'")
    except Exception as e:
        print(f"\nChua cai matplotlib (dung pip install matplotlib de tao anh do thi): {e}")

if __name__ == "__main__":
    main()
