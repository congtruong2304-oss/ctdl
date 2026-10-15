import sys
import os
import math

def kc_euclid(u: list, v: list) -> float:
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(u, v)))

def kc_manhattan(u: list, v: list) -> float:
    return sum(abs(a - b) for a, b in zip(u, v))

def doc_du_lieu(ten_tep: str):
    duong_dan = ten_tep
    if not os.path.exists(duong_dan):
        duong_dan = os.path.join("..", "..", "data", ten_tep)
        if not os.path.exists(duong_dan):
            duong_dan = os.path.join("data", ten_tep)

    with open(duong_dan, "r", encoding="utf-8") as f:
        dong_dau = f.readline().split()
        n = int(dong_dau[0])
        d = int(dong_dau[1])

        D = []
        for i in range(1, n + 1):
            parts = f.readline().split()
            if not parts:
                continue
            x = [float(val) for val in parts[:d]]
            y = parts[d]
            D.append((i, x, y))
    return D, d

def lang_gieng_gan_nhat(q: list, D: list, kc=kc_euclid, bo_qua_id=-1):
    min_dist = float('inf')
    best_nhan = ""
    best_id = -1

    for m_id, x, y in D:
        if m_id == bo_qua_id:
            continue
        dist = kc(q, x)
        if dist < min_dist:
            min_dist = dist
            best_nhan = y
            best_id = m_id

    return best_nhan, min_dist, best_id

def main():
    D, d = doc_du_lieu("hoa30.txt")

    q = [6.5, 3.0, 5.5, 2.0]
    nhan_e, dist_e, idx_e = lang_gieng_gan_nhat(q, D, kc=kc_euclid)
    nhan_m, dist_m, idx_m = lang_gieng_gan_nhat(q, D, kc=kc_manhattan)

    print(f"Mau {q}:")
    print(f"  Euclid:    {nhan_e} (mau {idx_e}, kc {dist_e:.4f})")
    print(f"  Manhattan: {nhan_m} (mau {idx_m}, kc {dist_m:.4f})")

    dung_e, dung_m = 0, 0
    n = len(D)
    for m_id, x, y in D:
        ke = lang_gieng_gan_nhat(x, D, kc=kc_euclid, bo_qua_id=m_id)
        km = lang_gieng_gan_nhat(x, D, kc=kc_manhattan, bo_qua_id=m_id)
        if ke[0] == y:
            dung_e += 1
        if km[0] == y:
            dung_m += 1
        if m_id == 26:
            print(f"Mau 26 bi bo ra:")
            print(f"  Manhattan du doan: {km[0]} (mau {km[2]}, kc {km[1]:.1f})")

    print("Do chinh xac LOO:")
    print(f"  Euclid:    {dung_e}/{n} = {dung_e / n * 100:.2f}%")
    print(f"  Manhattan: {dung_m}/{n} = {dung_m / n * 100:.2f}%")

if __name__ == "__main__":
    main()
