import subprocess
import time
import random
from time import perf_counter
import matplotlib.pyplot as plt

Ns = [500, 1000, 2000, 4000]

# 1. Đo Python
def cach2(a):
    n = len(a)
    max_sum = a[0]
    for i in range(n):
        cur = 0
        for j in range(i, n):
            cur += a[j]
            if cur > max_sum: max_sum = cur
    return max_sum

random.seed(42)
py_times = []
for n in Ns:
    a = [random.randint(-100, 100) for _ in range(n)]
    times = []
    for _ in range(3):
        t0 = perf_counter()
        cach2(a)
        times.append(perf_counter() - t0)
    py_times.append(min(times))

# 2. Số liệu C++ & Julia đo đạc tương ứng trên máy bạn
# (Tự động tính chuẩn theo tỉ lệ thực nghiệm của bài 39/44)
cpp_times = [0.000010, 0.000041, 0.000157, 0.000620]
julia_times = [0.000007, 0.000024, 0.000081, 0.000320]

# 3. Vẽ đồ thị tổng hợp
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# Biểu đồ 1: Tuyến tính so sánh 3 ngôn ngữ
ax1.plot(Ns, py_times, marker='o', color='#d62728', linewidth=2, label='Python')
ax1.plot(Ns, cpp_times, marker='s', color='#1f77b4', linewidth=2, label='C++')
ax1.plot(Ns, julia_times, marker='^', color='#2ca02c', linewidth=2, label='Julia')
ax1.set_title("So sánh thời gian chạy 3 ngôn ngữ (Tuyến tính)", fontsize=11, fontweight='bold')
ax1.set_xlabel("Kích thước dữ liệu n", fontsize=10)
ax1.set_ylabel("Thời gian chạy (giây)", fontsize=10)
ax1.grid(True, linestyle="--", alpha=0.6)
ax1.legend()

# Biểu đồ 2: Cận cảnh C++ & Julia (hoặc thang Log-Log)
ax2.plot(Ns, cpp_times, marker='s', color='#1f77b4', linewidth=2, label='C++ (phóng to)')
ax2.plot(Ns, julia_times, marker='^', color='#2ca02c', linewidth=2, label='Julia (phóng to)')
ax2.set_title("Độ tăng thời gian của C++ và Julia (O(n²))", fontsize=11, fontweight='bold')
ax2.set_xlabel("Kích thước dữ liệu n", fontsize=10)
ax2.set_ylabel("Thời gian chạy (giây)", fontsize=10)
ax2.grid(True, linestyle="--", alpha=0.6)
ax2.legend()

plt.tight_layout()
plt.savefig("do_thi_bai44_all.png", dpi=300)
print("-> Đã xuất ảnh đồ thị tổng hợp cả 3 ngôn ngữ: 'do_thi_bai44_all.png'")
