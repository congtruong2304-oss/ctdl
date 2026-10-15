import random
import math
from time import perf_counter

def kc_euclid(u: list, v: list) -> float:
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(u, v)))

def phan_loai(q: list, D: list) -> int:
    min_dist = float('inf')
    best_nhan = -1
    for x, y in D:
        dist = kc_euclid(q, x)
        if dist < min_dist:
            min_dist = dist
            best_nhan = y
    return best_nhan

def sinh_du_lieu(n: int, d: int):
    return [([random.random() for _ in range(d)], random.randint(0, 2)) for _ in range(n)]

def main():
    random.seed(12345)
    d = 20
    q_size = 1000

    Q = [[random.random() for _ in range(d)] for _ in range(q_size)]
    N_list = [1000, 10000, 100000]
    T = []

    for n in N_list:
        D = sinh_du_lieu(n, d)
        t0 = perf_counter()
        for q in Q:
            phan_loai(q, D)
        t = perf_counter() - t0
        T.append(t)
        print(f"n = {n}: {t:.4f} s")

    print(f"Ti le: T(10^4)/T(10^3) = {T[1]/T[0]:.2f}x, T(10^5)/T(10^4) = {T[2]/T[1]:.2f}x")

if __name__ == "__main__":
    main()
