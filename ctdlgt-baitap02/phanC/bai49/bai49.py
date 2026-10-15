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
        first_line = f.readline().split()
        n, d = int(first_line[0]), int(first_line[1])
        D = []
        for i in range(1, n + 1):
            parts = f.readline().split()
            if not parts:
                continue
            x = [float(val) for val in parts[:d]]
            y = parts[d]
            D.append((i, x, y))
    return D, d

def bo_mot_mau(D, kc=kc_euclid):
    n = len(D)
    so_dung = 0
    danh_sach_sai = []

    for i in range(n):
        id_i, xi, yi = D[i]
        min_dist = float('inf')
        best_nhan = ""
        best_id = -1

        for j in range(n):
            if i == j:
                continue
            id_j, xj, yj = D[j]
            dist = kc(xi, xj)
            if dist < min_dist:
                min_dist = dist
                best_nhan = yj
                best_id = id_j

        if best_nhan == yi:
            so_dung += 1
        else:
            danh_sach_sai.append((id_i, yi, best_nhan, best_id))

    return so_dung, n, danh_sach_sai

def main():
    D, d = doc_du_lieu("hoa30.txt")

    dung_e, n, sai_e = bo_mot_mau(D, kc=kc_euclid)
    dung_m, _, sai_m = bo_mot_mau(D, kc=kc_manhattan)

    msg_e = " — khong mau nao sai" if not sai_e else ""
    print(f"Euclid: {dung_e}/{n} = {dung_e/n*100:.2f}%{msg_e}")

    msg_m = f" — sai mau {sai_m[0][0]} (that: {sai_m[0][1]}, du doan: {sai_m[0][2]})" if sai_m else ""
    print(f"Manhattan: {dung_m}/{n} = {dung_m/n*100:.2f}%{msg_m}")

if __name__ == "__main__":
    main()
